from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.Ole
import win32more.System.Performance
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class _ICounterItemUnion(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('de1a6b74-9182-4c41-8e-2c-24-c2-cd-30-ee-83')
    @commethod(3)
    def get_Value(pdblValue: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_Color(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_Color(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_Width(iWidth: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Width(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_LineStyle(iLineStyle: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_LineStyle(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_ScaleFactor(iScale: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_ScaleFactor(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Path(pstrValue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetValue(Value: POINTER(Double), Status: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetStatistics(Max: POINTER(Double), Min: POINTER(Double), Avg: POINTER(Double), Status: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_Selected(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Selected(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Visible(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_Visible(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetDataAt(iIndex: Int32, iWhich: win32more.System.Performance.SysmonDataType, pVariant: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class _ISystemMonitorUnion(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c8a77338-265f-4de5-aa-25-c7-da-1c-e5-a8-f4')
    @commethod(3)
    def get_Appearance(iAppearance: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_Appearance(iAppearance: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_BackColor(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_BackColor(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_BorderStyle(iBorderStyle: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_BorderStyle(iBorderStyle: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_ForeColor(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_ForeColor(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Font(ppFont: POINTER(win32more.System.Ole.IFontDisp_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def putref_Font(pFont: win32more.System.Ole.IFontDisp_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Counters(ppICounters: POINTER(win32more.System.Performance.ICounters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_ShowVerticalGrid(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_ShowVerticalGrid(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_ShowHorizontalGrid(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_ShowHorizontalGrid(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_ShowLegend(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_ShowLegend(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_ShowScaleLabels(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_ShowScaleLabels(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_ShowValueBar(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_ShowValueBar(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_MaximumScale(iValue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_MaximumScale(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def put_MinimumScale(iValue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_MinimumScale(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_UpdateInterval(fValue: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_UpdateInterval(pfValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_DisplayType(eDisplayType: win32more.System.Performance.DisplayTypeConstants) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_DisplayType(peDisplayType: POINTER(win32more.System.Performance.DisplayTypeConstants)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def put_ManualUpdate(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_ManualUpdate(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_GraphTitle(bsTitle: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_GraphTitle(pbsTitle: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def put_YAxisLabel(bsTitle: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_YAxisLabel(pbsTitle: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def CollectSample() -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def UpdateGraph() -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def BrowseCounters() -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def DisplayProperties() -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def Counter(iIndex: Int32, ppICounter: POINTER(win32more.System.Performance.ICounterItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def AddCounter(bsPath: win32more.Foundation.BSTR, ppICounter: POINTER(win32more.System.Performance.ICounterItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def DeleteCounter(pCtr: win32more.System.Performance.ICounterItem_head) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def get_BackColorCtl(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def put_BackColorCtl(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def put_LogFileName(bsFileName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_LogFileName(bsFileName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def put_LogViewStart(StartTime: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def get_LogViewStart(StartTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def put_LogViewStop(StopTime: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def get_LogViewStop(StopTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def get_GridColor(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def put_GridColor(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def get_TimeBarColor(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def put_TimeBarColor(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def get_Highlight(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def put_Highlight(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def get_ShowToolbar(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def put_ShowToolbar(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def Paste() -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def Copy() -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def put_ReadOnly(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def get_ReadOnly(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def put_ReportValueType(eReportValueType: win32more.System.Performance.ReportValueTypeConstants) -> win32more.Foundation.HRESULT: ...
    @commethod(67)
    def get_ReportValueType(peReportValueType: POINTER(win32more.System.Performance.ReportValueTypeConstants)) -> win32more.Foundation.HRESULT: ...
    @commethod(68)
    def put_MonitorDuplicateInstances(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(69)
    def get_MonitorDuplicateInstances(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(70)
    def put_DisplayFilter(iValue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(71)
    def get_DisplayFilter(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(72)
    def get_LogFiles(ppILogFiles: POINTER(win32more.System.Performance.ILogFiles_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(73)
    def put_DataSourceType(eDataSourceType: win32more.System.Performance.DataSourceTypeConstants) -> win32more.Foundation.HRESULT: ...
    @commethod(74)
    def get_DataSourceType(peDataSourceType: POINTER(win32more.System.Performance.DataSourceTypeConstants)) -> win32more.Foundation.HRESULT: ...
    @commethod(75)
    def put_SqlDsnName(bsSqlDsnName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(76)
    def get_SqlDsnName(bsSqlDsnName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(77)
    def put_SqlLogSetName(bsSqlLogSetName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(78)
    def get_SqlLogSetName(bsSqlLogSetName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(79)
    def put_EnableDigitGrouping(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(80)
    def get_EnableDigitGrouping(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(81)
    def put_EnableToolTips(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(82)
    def get_EnableToolTips(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(83)
    def put_ShowTimeAxisLabels(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(84)
    def get_ShowTimeAxisLabels(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(85)
    def put_ChartScroll(bScroll: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(86)
    def get_ChartScroll(pbScroll: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(87)
    def put_DataPointCount(iNewCount: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(88)
    def get_DataPointCount(piDataPointCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(89)
    def ScaleToFit(bSelectedCountersOnly: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(90)
    def SaveAs(bstrFileName: win32more.Foundation.BSTR, eSysmonFileType: win32more.System.Performance.SysmonFileType) -> win32more.Foundation.HRESULT: ...
    @commethod(91)
    def Relog(bstrFileName: win32more.Foundation.BSTR, eSysmonFileType: win32more.System.Performance.SysmonFileType, iFilter: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(92)
    def ClearData() -> win32more.Foundation.HRESULT: ...
    @commethod(93)
    def get_LogSourceStartTime(pDate: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(94)
    def get_LogSourceStopTime(pDate: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(95)
    def SetLogViewRange(StartTime: Double, StopTime: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(96)
    def GetLogViewRange(StartTime: POINTER(Double), StopTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(97)
    def BatchingLock(fLock: win32more.Foundation.VARIANT_BOOL, eBatchReason: win32more.System.Performance.SysmonBatchReason) -> win32more.Foundation.HRESULT: ...
    @commethod(98)
    def LoadSettings(bstrSettingFileName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
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
LIBID_SystemMonitor: Guid = Guid('1b773e42-2509-11cf-94-2f-00-80-29-00-43-47')
DIID_DICounterItem: Guid = Guid('c08c4ff2-0e2e-11cf-94-2c-00-80-29-00-43-47')
DIID_DILogFileItem: Guid = Guid('8d093ffc-f777-4917-82-d1-83-3f-bc-54-c5-8f')
DIID_DISystemMonitor: Guid = Guid('13d73d81-c32e-11cf-93-98-00-aa-00-a3-dd-ea')
DIID_DISystemMonitorInternal: Guid = Guid('194eb242-c32c-11cf-93-98-00-aa-00-a3-dd-ea')
DIID_DISystemMonitorEvents: Guid = Guid('84979930-4ab3-11cf-94-3a-00-80-29-00-43-47')
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
S_PDH: Guid = Guid('04d66358-c4a1-419b-80-23-23-b7-39-02-de-2c')
@winfunctype('KERNEL32.dll')
def QueryPerformanceCounter(lpPerformanceCount: POINTER(win32more.Foundation.LARGE_INTEGER_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryPerformanceFrequency(lpFrequency: POINTER(win32more.Foundation.LARGE_INTEGER_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('loadperf.dll')
def InstallPerfDllW(szComputerName: win32more.Foundation.PWSTR, lpIniFile: win32more.Foundation.PWSTR, dwFlags: UIntPtr) -> UInt32: ...
@winfunctype('loadperf.dll')
def InstallPerfDllA(szComputerName: win32more.Foundation.PSTR, lpIniFile: win32more.Foundation.PSTR, dwFlags: UIntPtr) -> UInt32: ...
@winfunctype('loadperf.dll')
def LoadPerfCounterTextStringsA(lpCommandLine: win32more.Foundation.PSTR, bQuietModeArg: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('loadperf.dll')
def LoadPerfCounterTextStringsW(lpCommandLine: win32more.Foundation.PWSTR, bQuietModeArg: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('loadperf.dll')
def UnloadPerfCounterTextStringsW(lpCommandLine: win32more.Foundation.PWSTR, bQuietModeArg: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('loadperf.dll')
def UnloadPerfCounterTextStringsA(lpCommandLine: win32more.Foundation.PSTR, bQuietModeArg: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('loadperf.dll')
def UpdatePerfNameFilesA(szNewCtrFilePath: win32more.Foundation.PSTR, szNewHlpFilePath: win32more.Foundation.PSTR, szLanguageID: win32more.Foundation.PSTR, dwFlags: UIntPtr) -> UInt32: ...
@winfunctype('loadperf.dll')
def UpdatePerfNameFilesW(szNewCtrFilePath: win32more.Foundation.PWSTR, szNewHlpFilePath: win32more.Foundation.PWSTR, szLanguageID: win32more.Foundation.PWSTR, dwFlags: UIntPtr) -> UInt32: ...
@winfunctype('loadperf.dll')
def SetServiceAsTrustedA(szReserved: win32more.Foundation.PSTR, szServiceName: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('loadperf.dll')
def SetServiceAsTrustedW(szReserved: win32more.Foundation.PWSTR, szServiceName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('loadperf.dll')
def BackupPerfRegistryToFileW(szFileName: win32more.Foundation.PWSTR, szCommentString: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('loadperf.dll')
def RestorePerfRegistryFromFileW(szFileName: win32more.Foundation.PWSTR, szLangId: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfStartProvider(ProviderGuid: POINTER(Guid), ControlCallback: win32more.System.Performance.PERFLIBREQUEST, phProvider: POINTER(win32more.System.Performance.PerfProviderHandle)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfStartProviderEx(ProviderGuid: POINTER(Guid), ProviderContext: POINTER(win32more.System.Performance.PERF_PROVIDER_CONTEXT_head), Provider: POINTER(win32more.System.Performance.PerfProviderHandle)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfStopProvider(ProviderHandle: win32more.System.Performance.PerfProviderHandle) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfSetCounterSetInfo(ProviderHandle: win32more.Foundation.HANDLE, Template: POINTER(win32more.System.Performance.PERF_COUNTERSET_INFO_head), TemplateSize: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfCreateInstance(ProviderHandle: win32more.System.Performance.PerfProviderHandle, CounterSetGuid: POINTER(Guid), Name: win32more.Foundation.PWSTR, Id: UInt32) -> POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head): ...
@winfunctype('ADVAPI32.dll')
def PerfDeleteInstance(Provider: win32more.System.Performance.PerfProviderHandle, InstanceBlock: POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryInstance(ProviderHandle: win32more.Foundation.HANDLE, CounterSetGuid: POINTER(Guid), Name: win32more.Foundation.PWSTR, Id: UInt32) -> POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head): ...
@winfunctype('ADVAPI32.dll')
def PerfSetCounterRefValue(Provider: win32more.Foundation.HANDLE, Instance: POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Address: c_void_p) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfSetULongCounterValue(Provider: win32more.Foundation.HANDLE, Instance: POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfSetULongLongCounterValue(Provider: win32more.Foundation.HANDLE, Instance: POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfIncrementULongCounterValue(Provider: win32more.Foundation.HANDLE, Instance: POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfIncrementULongLongCounterValue(Provider: win32more.Foundation.HANDLE, Instance: POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfDecrementULongCounterValue(Provider: win32more.Foundation.HANDLE, Instance: POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfDecrementULongLongCounterValue(Provider: win32more.Foundation.HANDLE, Instance: POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfEnumerateCounterSet(szMachine: win32more.Foundation.PWSTR, pCounterSetIds: POINTER(Guid), cCounterSetIds: UInt32, pcCounterSetIdsActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfEnumerateCounterSetInstances(szMachine: win32more.Foundation.PWSTR, pCounterSetId: POINTER(Guid), pInstances: POINTER(win32more.System.Performance.PERF_INSTANCE_HEADER_head), cbInstances: UInt32, pcbInstancesActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryCounterSetRegistrationInfo(szMachine: win32more.Foundation.PWSTR, pCounterSetId: POINTER(Guid), requestCode: win32more.System.Performance.PerfRegInfoType, requestLangId: UInt32, pbRegInfo: c_char_p_no, cbRegInfo: UInt32, pcbRegInfoActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfOpenQueryHandle(szMachine: win32more.Foundation.PWSTR, phQuery: POINTER(win32more.System.Performance.PerfQueryHandle)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfCloseQueryHandle(hQuery: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryCounterInfo(hQuery: win32more.System.Performance.PerfQueryHandle, pCounters: POINTER(win32more.System.Performance.PERF_COUNTER_IDENTIFIER_head), cbCounters: UInt32, pcbCountersActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryCounterData(hQuery: win32more.System.Performance.PerfQueryHandle, pCounterBlock: POINTER(win32more.System.Performance.PERF_DATA_HEADER_head), cbCounterBlock: UInt32, pcbCounterBlockActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfAddCounters(hQuery: win32more.System.Performance.PerfQueryHandle, pCounters: POINTER(win32more.System.Performance.PERF_COUNTER_IDENTIFIER_head), cbCounters: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfDeleteCounters(hQuery: win32more.System.Performance.PerfQueryHandle, pCounters: POINTER(win32more.System.Performance.PERF_COUNTER_IDENTIFIER_head), cbCounters: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDllVersion(lpdwVersion: POINTER(win32more.System.Performance.PDH_DLL_VERSION)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenQueryW(szDataSource: win32more.Foundation.PWSTR, dwUserData: UIntPtr, phQuery: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenQueryA(szDataSource: win32more.Foundation.PSTR, dwUserData: UIntPtr, phQuery: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhAddCounterW(hQuery: IntPtr, szFullCounterPath: win32more.Foundation.PWSTR, dwUserData: UIntPtr, phCounter: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhAddCounterA(hQuery: IntPtr, szFullCounterPath: win32more.Foundation.PSTR, dwUserData: UIntPtr, phCounter: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhAddEnglishCounterW(hQuery: IntPtr, szFullCounterPath: win32more.Foundation.PWSTR, dwUserData: UIntPtr, phCounter: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhAddEnglishCounterA(hQuery: IntPtr, szFullCounterPath: win32more.Foundation.PSTR, dwUserData: UIntPtr, phCounter: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCollectQueryDataWithTime(hQuery: IntPtr, pllTimeStamp: POINTER(Int64)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhValidatePathExW(hDataSource: IntPtr, szFullPathBuffer: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhValidatePathExA(hDataSource: IntPtr, szFullPathBuffer: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhRemoveCounter(hCounter: IntPtr) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCollectQueryData(hQuery: IntPtr) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCloseQuery(hQuery: IntPtr) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetFormattedCounterValue(hCounter: IntPtr, dwFormat: win32more.System.Performance.PDH_FMT, lpdwType: POINTER(UInt32), pValue: POINTER(win32more.System.Performance.PDH_FMT_COUNTERVALUE_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetFormattedCounterArrayA(hCounter: IntPtr, dwFormat: win32more.System.Performance.PDH_FMT, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(win32more.System.Performance.PDH_FMT_COUNTERVALUE_ITEM_A_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetFormattedCounterArrayW(hCounter: IntPtr, dwFormat: win32more.System.Performance.PDH_FMT, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(win32more.System.Performance.PDH_FMT_COUNTERVALUE_ITEM_W_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetRawCounterValue(hCounter: IntPtr, lpdwType: POINTER(UInt32), pValue: POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetRawCounterArrayA(hCounter: IntPtr, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(win32more.System.Performance.PDH_RAW_COUNTER_ITEM_A_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetRawCounterArrayW(hCounter: IntPtr, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(win32more.System.Performance.PDH_RAW_COUNTER_ITEM_W_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCalculateCounterFromRawValue(hCounter: IntPtr, dwFormat: win32more.System.Performance.PDH_FMT, rawValue1: POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head), rawValue2: POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head), fmtValue: POINTER(win32more.System.Performance.PDH_FMT_COUNTERVALUE_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhComputeCounterStatistics(hCounter: IntPtr, dwFormat: win32more.System.Performance.PDH_FMT, dwFirstEntry: UInt32, dwNumEntries: UInt32, lpRawValueArray: POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head), data: POINTER(win32more.System.Performance.PDH_STATISTICS_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetCounterInfoW(hCounter: IntPtr, bRetrieveExplainText: win32more.Foundation.BOOLEAN, pdwBufferSize: POINTER(UInt32), lpBuffer: POINTER(win32more.System.Performance.PDH_COUNTER_INFO_W_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetCounterInfoA(hCounter: IntPtr, bRetrieveExplainText: win32more.Foundation.BOOLEAN, pdwBufferSize: POINTER(UInt32), lpBuffer: POINTER(win32more.System.Performance.PDH_COUNTER_INFO_A_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSetCounterScaleFactor(hCounter: IntPtr, lFactor: Int32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhConnectMachineW(szMachineName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhConnectMachineA(szMachineName: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumMachinesW(szDataSource: win32more.Foundation.PWSTR, mszMachineList: win32more.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumMachinesA(szDataSource: win32more.Foundation.PSTR, mszMachineList: win32more.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectsW(szDataSource: win32more.Foundation.PWSTR, szMachineName: win32more.Foundation.PWSTR, mszObjectList: win32more.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: win32more.System.Performance.PERF_DETAIL, bRefresh: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectsA(szDataSource: win32more.Foundation.PSTR, szMachineName: win32more.Foundation.PSTR, mszObjectList: win32more.Foundation.PSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: win32more.System.Performance.PERF_DETAIL, bRefresh: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectItemsW(szDataSource: win32more.Foundation.PWSTR, szMachineName: win32more.Foundation.PWSTR, szObjectName: win32more.Foundation.PWSTR, mszCounterList: win32more.Foundation.PWSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: win32more.Foundation.PWSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: win32more.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectItemsA(szDataSource: win32more.Foundation.PSTR, szMachineName: win32more.Foundation.PSTR, szObjectName: win32more.Foundation.PSTR, mszCounterList: win32more.Foundation.PSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: win32more.Foundation.PSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: win32more.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhMakeCounterPathW(pCounterPathElements: POINTER(win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W_head), szFullPathBuffer: win32more.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32), dwFlags: win32more.System.Performance.PDH_PATH_FLAGS) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhMakeCounterPathA(pCounterPathElements: POINTER(win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A_head), szFullPathBuffer: win32more.Foundation.PSTR, pcchBufferSize: POINTER(UInt32), dwFlags: win32more.System.Performance.PDH_PATH_FLAGS) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhParseCounterPathW(szFullPathBuffer: win32more.Foundation.PWSTR, pCounterPathElements: POINTER(win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W_head), pdwBufferSize: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhParseCounterPathA(szFullPathBuffer: win32more.Foundation.PSTR, pCounterPathElements: POINTER(win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A_head), pdwBufferSize: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhParseInstanceNameW(szInstanceString: win32more.Foundation.PWSTR, szInstanceName: win32more.Foundation.PWSTR, pcchInstanceNameLength: POINTER(UInt32), szParentName: win32more.Foundation.PWSTR, pcchParentNameLength: POINTER(UInt32), lpIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhParseInstanceNameA(szInstanceString: win32more.Foundation.PSTR, szInstanceName: win32more.Foundation.PSTR, pcchInstanceNameLength: POINTER(UInt32), szParentName: win32more.Foundation.PSTR, pcchParentNameLength: POINTER(UInt32), lpIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhValidatePathW(szFullPathBuffer: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhValidatePathA(szFullPathBuffer: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectW(szDataSource: win32more.Foundation.PWSTR, szMachineName: win32more.Foundation.PWSTR, szDefaultObjectName: win32more.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectA(szDataSource: win32more.Foundation.PSTR, szMachineName: win32more.Foundation.PSTR, szDefaultObjectName: win32more.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterW(szDataSource: win32more.Foundation.PWSTR, szMachineName: win32more.Foundation.PWSTR, szObjectName: win32more.Foundation.PWSTR, szDefaultCounterName: win32more.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterA(szDataSource: win32more.Foundation.PSTR, szMachineName: win32more.Foundation.PSTR, szObjectName: win32more.Foundation.PSTR, szDefaultCounterName: win32more.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBrowseCountersW(pBrowseDlgData: POINTER(win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_W_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBrowseCountersA(pBrowseDlgData: POINTER(win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_A_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandCounterPathW(szWildCardPath: win32more.Foundation.PWSTR, mszExpandedPathList: win32more.Foundation.PWSTR, pcchPathListLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandCounterPathA(szWildCardPath: win32more.Foundation.PSTR, mszExpandedPathList: win32more.Foundation.PSTR, pcchPathListLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhLookupPerfNameByIndexW(szMachineName: win32more.Foundation.PWSTR, dwNameIndex: UInt32, szNameBuffer: win32more.Foundation.PWSTR, pcchNameBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhLookupPerfNameByIndexA(szMachineName: win32more.Foundation.PSTR, dwNameIndex: UInt32, szNameBuffer: win32more.Foundation.PSTR, pcchNameBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhLookupPerfIndexByNameW(szMachineName: win32more.Foundation.PWSTR, szNameBuffer: win32more.Foundation.PWSTR, pdwIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhLookupPerfIndexByNameA(szMachineName: win32more.Foundation.PSTR, szNameBuffer: win32more.Foundation.PSTR, pdwIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandWildCardPathA(szDataSource: win32more.Foundation.PSTR, szWildCardPath: win32more.Foundation.PSTR, mszExpandedPathList: win32more.Foundation.PSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandWildCardPathW(szDataSource: win32more.Foundation.PWSTR, szWildCardPath: win32more.Foundation.PWSTR, mszExpandedPathList: win32more.Foundation.PWSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenLogW(szLogFileName: win32more.Foundation.PWSTR, dwAccessFlags: win32more.System.Performance.PDH_LOG, lpdwLogType: POINTER(win32more.System.Performance.PDH_LOG_TYPE), hQuery: IntPtr, dwMaxSize: UInt32, szUserCaption: win32more.Foundation.PWSTR, phLog: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenLogA(szLogFileName: win32more.Foundation.PSTR, dwAccessFlags: win32more.System.Performance.PDH_LOG, lpdwLogType: POINTER(win32more.System.Performance.PDH_LOG_TYPE), hQuery: IntPtr, dwMaxSize: UInt32, szUserCaption: win32more.Foundation.PSTR, phLog: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhUpdateLogW(hLog: IntPtr, szUserString: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhUpdateLogA(hLog: IntPtr, szUserString: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhUpdateLogFileCatalog(hLog: IntPtr) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetLogFileSize(hLog: IntPtr, llSize: POINTER(Int64)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCloseLog(hLog: IntPtr, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSelectDataSourceW(hWndOwner: win32more.Foundation.HWND, dwFlags: win32more.System.Performance.PDH_SELECT_DATA_SOURCE_FLAGS, szDataSource: win32more.Foundation.PWSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSelectDataSourceA(hWndOwner: win32more.Foundation.HWND, dwFlags: win32more.System.Performance.PDH_SELECT_DATA_SOURCE_FLAGS, szDataSource: win32more.Foundation.PSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhIsRealTimeQuery(hQuery: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('pdh.dll')
def PdhSetQueryTimeRange(hQuery: IntPtr, pInfo: POINTER(win32more.System.Performance.PDH_TIME_INFO_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDataSourceTimeRangeW(szDataSource: win32more.Foundation.PWSTR, pdwNumEntries: POINTER(UInt32), pInfo: POINTER(win32more.System.Performance.PDH_TIME_INFO_head), pdwBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDataSourceTimeRangeA(szDataSource: win32more.Foundation.PSTR, pdwNumEntries: POINTER(UInt32), pInfo: POINTER(win32more.System.Performance.PDH_TIME_INFO_head), pdwBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCollectQueryDataEx(hQuery: IntPtr, dwIntervalTime: UInt32, hNewDataEvent: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhFormatFromRawValue(dwCounterType: UInt32, dwFormat: win32more.System.Performance.PDH_FMT, pTimeBase: POINTER(Int64), pRawValue1: POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head), pRawValue2: POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head), pFmtValue: POINTER(win32more.System.Performance.PDH_FMT_COUNTERVALUE_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetCounterTimeBase(hCounter: IntPtr, pTimeBase: POINTER(Int64)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhReadRawLogRecord(hLog: IntPtr, ftRecord: win32more.Foundation.FILETIME, pRawLogRecord: POINTER(win32more.System.Performance.PDH_RAW_LOG_RECORD_head), pdwBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSetDefaultRealTimeDataSource(dwDataSourceId: win32more.System.Performance.REAL_TIME_DATA_SOURCE_ID_FLAGS) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBindInputDataSourceW(phDataSource: POINTER(IntPtr), LogFileNameList: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBindInputDataSourceA(phDataSource: POINTER(IntPtr), LogFileNameList: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenQueryH(hDataSource: IntPtr, dwUserData: UIntPtr, phQuery: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumMachinesHW(hDataSource: IntPtr, mszMachineList: win32more.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumMachinesHA(hDataSource: IntPtr, mszMachineList: win32more.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectsHW(hDataSource: IntPtr, szMachineName: win32more.Foundation.PWSTR, mszObjectList: win32more.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: win32more.System.Performance.PERF_DETAIL, bRefresh: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectsHA(hDataSource: IntPtr, szMachineName: win32more.Foundation.PSTR, mszObjectList: win32more.Foundation.PSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: win32more.System.Performance.PERF_DETAIL, bRefresh: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectItemsHW(hDataSource: IntPtr, szMachineName: win32more.Foundation.PWSTR, szObjectName: win32more.Foundation.PWSTR, mszCounterList: win32more.Foundation.PWSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: win32more.Foundation.PWSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: win32more.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectItemsHA(hDataSource: IntPtr, szMachineName: win32more.Foundation.PSTR, szObjectName: win32more.Foundation.PSTR, mszCounterList: win32more.Foundation.PSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: win32more.Foundation.PSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: win32more.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandWildCardPathHW(hDataSource: IntPtr, szWildCardPath: win32more.Foundation.PWSTR, mszExpandedPathList: win32more.Foundation.PWSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandWildCardPathHA(hDataSource: IntPtr, szWildCardPath: win32more.Foundation.PSTR, mszExpandedPathList: win32more.Foundation.PSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDataSourceTimeRangeH(hDataSource: IntPtr, pdwNumEntries: POINTER(UInt32), pInfo: POINTER(win32more.System.Performance.PDH_TIME_INFO_head), pdwBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectHW(hDataSource: IntPtr, szMachineName: win32more.Foundation.PWSTR, szDefaultObjectName: win32more.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectHA(hDataSource: IntPtr, szMachineName: win32more.Foundation.PSTR, szDefaultObjectName: win32more.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterHW(hDataSource: IntPtr, szMachineName: win32more.Foundation.PWSTR, szObjectName: win32more.Foundation.PWSTR, szDefaultCounterName: win32more.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterHA(hDataSource: IntPtr, szMachineName: win32more.Foundation.PSTR, szObjectName: win32more.Foundation.PSTR, szDefaultCounterName: win32more.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBrowseCountersHW(pBrowseDlgData: POINTER(win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_HW_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBrowseCountersHA(pBrowseDlgData: POINTER(win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_HA_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhVerifySQLDBW(szDataSource: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhVerifySQLDBA(szDataSource: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCreateSQLTablesW(szDataSource: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCreateSQLTablesA(szDataSource: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumLogSetNamesW(szDataSource: win32more.Foundation.PWSTR, mszDataSetNameList: win32more.Foundation.PWSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumLogSetNamesA(szDataSource: win32more.Foundation.PSTR, mszDataSetNameList: win32more.Foundation.PSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetLogSetGUID(hLog: IntPtr, pGuid: POINTER(Guid), pRunId: POINTER(Int32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSetLogSetRunID(hLog: IntPtr, RunId: Int32) -> UInt32: ...
AppearPropPage = Guid('e49741e9-93a8-4ab1-8e-96-bf-44-82-28-2e-9c')
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
BootTraceSession = Guid('03837538-098b-11d8-94-14-50-50-54-50-30-30')
BootTraceSessionCollection = Guid('03837539-098b-11d8-94-14-50-50-54-50-30-30')
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
CounterItem = Guid('c4d2d8e0-d1dd-11ce-94-0f-00-80-29-00-43-48')
CounterItem2 = Guid('43196c62-c31f-4ce3-a0-2e-79-ef-e0-f6-a5-25')
@winfunctype_pointer
def CounterPathCallBack(param0: UIntPtr) -> Int32: ...
CounterPropPage = Guid('cf948561-ede8-11ce-94-1e-00-80-29-00-43-47')
Counters = Guid('b2b066d2-2aac-11cf-94-2f-00-80-29-00-43-47')
DataCollectorSet = Guid('03837521-098b-11d8-94-14-50-50-54-50-30-30')
DataCollectorSetCollection = Guid('03837525-098b-11d8-94-14-50-50-54-50-30-30')
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
class DICounterItem(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c08c4ff2-0e2e-11cf-94-2c-00-80-29-00-43-47')
class DILogFileItem(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('8d093ffc-f777-4917-82-d1-83-3f-bc-54-c5-8f')
DisplayTypeConstants = Int32
DisplayTypeConstants_sysmonLineGraph: DisplayTypeConstants = 1
DisplayTypeConstants_sysmonHistogram: DisplayTypeConstants = 2
DisplayTypeConstants_sysmonReport: DisplayTypeConstants = 3
DisplayTypeConstants_sysmonChartArea: DisplayTypeConstants = 4
DisplayTypeConstants_sysmonChartStackedArea: DisplayTypeConstants = 5
class DISystemMonitor(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('13d73d81-c32e-11cf-93-98-00-aa-00-a3-dd-ea')
class DISystemMonitorEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('84979930-4ab3-11cf-94-3a-00-80-29-00-43-47')
class DISystemMonitorInternal(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('194eb242-c32c-11cf-93-98-00-aa-00-a3-dd-ea')
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
GeneralPropPage = Guid('c3e5d3d2-1a03-11cf-94-2d-00-80-29-00-43-47')
GraphPropPage = Guid('c3e5d3d3-1a03-11cf-94-2d-00-80-29-00-43-47')
class IAlertDataCollector(c_void_p):
    extends: win32more.System.Performance.IDataCollector
    Guid = Guid('03837516-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(32)
    def get_AlertThresholds(alerts: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_AlertThresholds(alerts: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_EventLog(log: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_EventLog(log: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_SampleInterval(interval: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_SampleInterval(interval: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_Task(task: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_Task(task: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_TaskRunAsSelf(RunAsSelf: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_TaskRunAsSelf(RunAsSelf: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_TaskArguments(task: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def put_TaskArguments(task: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_TaskUserTextArguments(task: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_TaskUserTextArguments(task: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def get_TriggerDataCollectorSet(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def put_TriggerDataCollectorSet(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IApiTracingDataCollector(c_void_p):
    extends: win32more.System.Performance.IDataCollector
    Guid = Guid('0383751a-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(32)
    def get_LogApiNamesOnly(logapinames: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_LogApiNamesOnly(logapinames: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_LogApisRecursively(logrecursively: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_LogApisRecursively(logrecursively: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_ExePath(exepath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_ExePath(exepath: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_LogFilePath(logfilepath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_LogFilePath(logfilepath: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_IncludeModules(includemodules: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_IncludeModules(includemodules: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_IncludeApis(includeapis: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def put_IncludeApis(includeapis: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_ExcludeApis(excludeapis: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_ExcludeApis(excludeapis: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
class IConfigurationDataCollector(c_void_p):
    extends: win32more.System.Performance.IDataCollector
    Guid = Guid('03837514-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(32)
    def get_FileMaxCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_FileMaxCount(count: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_FileMaxRecursiveDepth(depth: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_FileMaxRecursiveDepth(depth: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_FileMaxTotalSize(size: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_FileMaxTotalSize(size: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_Files(Files: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_Files(Files: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_ManagementQueries(Queries: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_ManagementQueries(Queries: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_QueryNetworkAdapters(network: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def put_QueryNetworkAdapters(network: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_RegistryKeys(query: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_RegistryKeys(query: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def get_RegistryMaxRecursiveDepth(depth: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def put_RegistryMaxRecursiveDepth(depth: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_SystemStateFile(FileName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def put_SystemStateFile(FileName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ICounterItem(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('771a9520-ee28-11ce-94-1e-00-80-29-00-43-47')
    @commethod(3)
    def get_Value(pdblValue: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_Color(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_Color(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_Width(iWidth: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Width(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_LineStyle(iLineStyle: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_LineStyle(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_ScaleFactor(iScale: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_ScaleFactor(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Path(pstrValue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetValue(Value: POINTER(Double), Status: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetStatistics(Max: POINTER(Double), Min: POINTER(Double), Avg: POINTER(Double), Status: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class ICounterItem2(c_void_p):
    extends: win32more.System.Performance.ICounterItem
    Guid = Guid('eefcd4e1-ea1c-4435-b7-f4-e3-41-ba-03-b4-f9')
    @commethod(15)
    def put_Selected(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Selected(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Visible(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_Visible(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetDataAt(iIndex: Int32, iWhich: win32more.System.Performance.SysmonDataType, pVariant: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class ICounters(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('79167962-28fc-11cf-94-2f-00-80-29-00-43-47')
    @commethod(7)
    def get_Count(pLong: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(ppIunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(index: win32more.System.Com.VARIANT, ppI: POINTER(win32more.System.Performance.DICounterItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(pathname: win32more.Foundation.BSTR, ppI: POINTER(win32more.System.Performance.DICounterItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(index: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IDataCollector(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('038374ff-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_DataCollectorSet(group: POINTER(win32more.System.Performance.IDataCollectorSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_DataCollectorSet(group: win32more.System.Performance.IDataCollectorSet_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_DataCollectorType(type: POINTER(win32more.System.Performance.DataCollectorType)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_FileName(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_FileName(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_FileNameFormat(format: POINTER(win32more.System.Performance.AutoPathFormat)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_FileNameFormat(format: win32more.System.Performance.AutoPathFormat) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_FileNameFormatPattern(pattern: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_FileNameFormatPattern(pattern: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_LatestOutputLocation(path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_LatestOutputLocation(path: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_LogAppend(append: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_LogAppend(append: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_LogCircular(circular: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_LogCircular(circular: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_LogOverwrite(overwrite: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_LogOverwrite(overwrite: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_OutputLocation(path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Index(index: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_Index(index: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_Xml(Xml: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def SetXml(Xml: win32more.Foundation.BSTR, Validation: POINTER(win32more.System.Performance.IValueMap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def CreateOutputLocation(Latest: win32more.Foundation.VARIANT_BOOL, Location: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IDataCollectorCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('03837502-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_Count(retVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: win32more.System.Com.VARIANT, collector: POINTER(win32more.System.Performance.IDataCollector_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(retVal: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(collector: win32more.System.Performance.IDataCollector_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(collector: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Clear() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(collectors: win32more.System.Performance.IDataCollectorCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def CreateDataCollectorFromXml(bstrXml: win32more.Foundation.BSTR, pValidation: POINTER(win32more.System.Performance.IValueMap_head), pCollector: POINTER(win32more.System.Performance.IDataCollector_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def CreateDataCollector(Type: win32more.System.Performance.DataCollectorType, Collector: POINTER(win32more.System.Performance.IDataCollector_head)) -> win32more.Foundation.HRESULT: ...
class IDataCollectorSet(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('03837520-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_DataCollectors(collectors: POINTER(win32more.System.Performance.IDataCollectorCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Duration(seconds: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Duration(seconds: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(description: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Description(description: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_DescriptionUnresolved(Descr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_DisplayName(DisplayName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_DisplayName(DisplayName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_DisplayNameUnresolved(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Keywords(keywords: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Keywords(keywords: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_LatestOutputLocation(path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_LatestOutputLocation(path: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_OutputLocation(path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_RootPath(folder: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_RootPath(folder: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_Segment(segment: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_Segment(segment: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_SegmentMaxDuration(seconds: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_SegmentMaxDuration(seconds: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_SegmentMaxSize(size: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_SegmentMaxSize(size: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_SerialNumber(index: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_SerialNumber(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_Server(server: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_Status(status: POINTER(win32more.System.Performance.DataCollectorSetStatus)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_Subdirectory(folder: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_Subdirectory(folder: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_SubdirectoryFormat(format: POINTER(win32more.System.Performance.AutoPathFormat)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_SubdirectoryFormat(format: win32more.System.Performance.AutoPathFormat) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_SubdirectoryFormatPattern(pattern: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_SubdirectoryFormatPattern(pattern: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_Task(task: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_Task(task: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_TaskRunAsSelf(RunAsSelf: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def put_TaskRunAsSelf(RunAsSelf: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_TaskArguments(task: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_TaskArguments(task: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def get_TaskUserTextArguments(UserText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def put_TaskUserTextArguments(UserText: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_Schedules(ppSchedules: POINTER(win32more.System.Performance.IScheduleCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def get_SchedulesEnabled(enabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def put_SchedulesEnabled(enabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def get_UserAccount(user: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def get_Xml(xml: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def get_Security(pbstrSecurity: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def put_Security(bstrSecurity: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def get_StopOnCompletion(Stop: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def put_StopOnCompletion(Stop: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def get_DataManager(DataManager: POINTER(win32more.System.Performance.IDataManager_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def SetCredentials(user: win32more.Foundation.BSTR, password: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def Query(name: win32more.Foundation.BSTR, server: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def Commit(name: win32more.Foundation.BSTR, server: win32more.Foundation.BSTR, mode: win32more.System.Performance.CommitMode, validation: POINTER(win32more.System.Performance.IValueMap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def Start(Synchronous: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def Stop(Synchronous: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def SetXml(xml: win32more.Foundation.BSTR, validation: POINTER(win32more.System.Performance.IValueMap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def SetValue(key: win32more.Foundation.BSTR, value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def GetValue(key: win32more.Foundation.BSTR, value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IDataCollectorSetCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('03837524-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_Count(retVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: win32more.System.Com.VARIANT, set: POINTER(win32more.System.Performance.IDataCollectorSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(retVal: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(set: win32more.System.Performance.IDataCollectorSet_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(set: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Clear() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(sets: win32more.System.Performance.IDataCollectorSetCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetDataCollectorSets(server: win32more.Foundation.BSTR, filter: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IDataManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('03837541-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_Enabled(pfEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Enabled(fEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_CheckBeforeRunning(pfCheck: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_CheckBeforeRunning(fCheck: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_MinFreeDisk(MinFreeDisk: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_MinFreeDisk(MinFreeDisk: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_MaxSize(pulMaxSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_MaxSize(ulMaxSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_MaxFolderCount(pulMaxFolderCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_MaxFolderCount(ulMaxFolderCount: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_ResourcePolicy(pPolicy: POINTER(win32more.System.Performance.ResourcePolicy)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_ResourcePolicy(Policy: win32more.System.Performance.ResourcePolicy) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_FolderActions(Actions: POINTER(win32more.System.Performance.IFolderActionCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_ReportSchema(ReportSchema: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_ReportSchema(ReportSchema: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_ReportFileName(pbstrFilename: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_ReportFileName(pbstrFilename: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_RuleTargetFileName(Filename: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_RuleTargetFileName(Filename: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_EventsFileName(pbstrFilename: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_EventsFileName(pbstrFilename: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_Rules(pbstrXml: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_Rules(bstrXml: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def Run(Steps: win32more.System.Performance.DataManagerSteps, bstrFolder: win32more.Foundation.BSTR, Errors: POINTER(win32more.System.Performance.IValueMap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def Extract(CabFilename: win32more.Foundation.BSTR, DestinationPath: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFolderAction(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('03837543-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_Age(pulAge: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Age(ulAge: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Size(pulAge: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Size(ulAge: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Actions(Steps: POINTER(win32more.System.Performance.FolderActionSteps)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_Actions(Steps: win32more.System.Performance.FolderActionSteps) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_SendCabTo(pbstrDestination: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_SendCabTo(bstrDestination: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFolderActionCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('03837544-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_Count(Count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(Index: win32more.System.Com.VARIANT, Action: POINTER(win32more.System.Performance.IFolderAction_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(Enum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(Action: win32more.System.Performance.IFolderAction_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(Index: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Clear() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(Actions: win32more.System.Performance.IFolderActionCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def CreateFolderAction(FolderAction: POINTER(win32more.System.Performance.IFolderAction_head)) -> win32more.Foundation.HRESULT: ...
class ILogFileItem(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d6b518dd-05c7-418a-89-e6-4f-9c-e8-c6-84-1e')
    @commethod(3)
    def get_Path(pstrValue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ILogFiles(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('6a2a97e6-6851-41ea-87-ad-2a-82-25-33-58-65')
    @commethod(7)
    def get_Count(pLong: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(ppIunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(index: win32more.System.Com.VARIANT, ppI: POINTER(win32more.System.Performance.DILogFileItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(pathname: win32more.Foundation.BSTR, ppI: POINTER(win32more.System.Performance.DILogFileItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(index: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IPerformanceCounterDataCollector(c_void_p):
    extends: win32more.System.Performance.IDataCollector
    Guid = Guid('03837506-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(32)
    def get_DataSourceName(dsn: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_DataSourceName(dsn: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_PerformanceCounters(counters: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_PerformanceCounters(counters: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_LogFileFormat(format: POINTER(win32more.System.Performance.FileFormat)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_LogFileFormat(format: win32more.System.Performance.FileFormat) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_SampleInterval(interval: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_SampleInterval(interval: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_SegmentMaxRecords(records: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_SegmentMaxRecords(records: UInt32) -> win32more.Foundation.HRESULT: ...
class ISchedule(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('0383753a-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_StartDate(start: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_StartDate(start: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_EndDate(end: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_EndDate(end: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_StartTime(start: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_StartTime(start: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Days(days: POINTER(win32more.System.Performance.WeekDays)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Days(days: win32more.System.Performance.WeekDays) -> win32more.Foundation.HRESULT: ...
class IScheduleCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('0383753d-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_Count(retVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: win32more.System.Com.VARIANT, ppSchedule: POINTER(win32more.System.Performance.ISchedule_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ienum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(pSchedule: win32more.System.Performance.ISchedule_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(vSchedule: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Clear() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(pSchedules: win32more.System.Performance.IScheduleCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def CreateSchedule(Schedule: POINTER(win32more.System.Performance.ISchedule_head)) -> win32more.Foundation.HRESULT: ...
class ISystemMonitor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('194eb241-c32c-11cf-93-98-00-aa-00-a3-dd-ea')
    @commethod(3)
    def get_Appearance(iAppearance: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_Appearance(iAppearance: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_BackColor(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_BackColor(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_BorderStyle(iBorderStyle: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_BorderStyle(iBorderStyle: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_ForeColor(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_ForeColor(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Font(ppFont: POINTER(win32more.System.Ole.IFontDisp_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def putref_Font(pFont: win32more.System.Ole.IFontDisp_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Counters(ppICounters: POINTER(win32more.System.Performance.ICounters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_ShowVerticalGrid(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_ShowVerticalGrid(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_ShowHorizontalGrid(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_ShowHorizontalGrid(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_ShowLegend(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_ShowLegend(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_ShowScaleLabels(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_ShowScaleLabels(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_ShowValueBar(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_ShowValueBar(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_MaximumScale(iValue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_MaximumScale(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def put_MinimumScale(iValue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_MinimumScale(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_UpdateInterval(fValue: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_UpdateInterval(pfValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_DisplayType(eDisplayType: win32more.System.Performance.DisplayTypeConstants) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_DisplayType(peDisplayType: POINTER(win32more.System.Performance.DisplayTypeConstants)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def put_ManualUpdate(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_ManualUpdate(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_GraphTitle(bsTitle: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_GraphTitle(pbsTitle: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def put_YAxisLabel(bsTitle: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_YAxisLabel(pbsTitle: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def CollectSample() -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def UpdateGraph() -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def BrowseCounters() -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def DisplayProperties() -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def Counter(iIndex: Int32, ppICounter: POINTER(win32more.System.Performance.ICounterItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def AddCounter(bsPath: win32more.Foundation.BSTR, ppICounter: POINTER(win32more.System.Performance.ICounterItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def DeleteCounter(pCtr: win32more.System.Performance.ICounterItem_head) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def get_BackColorCtl(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def put_BackColorCtl(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def put_LogFileName(bsFileName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_LogFileName(bsFileName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def put_LogViewStart(StartTime: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def get_LogViewStart(StartTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def put_LogViewStop(StopTime: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def get_LogViewStop(StopTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def get_GridColor(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def put_GridColor(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def get_TimeBarColor(pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def put_TimeBarColor(Color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def get_Highlight(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def put_Highlight(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def get_ShowToolbar(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def put_ShowToolbar(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def Paste() -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def Copy() -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def put_ReadOnly(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def get_ReadOnly(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def put_ReportValueType(eReportValueType: win32more.System.Performance.ReportValueTypeConstants) -> win32more.Foundation.HRESULT: ...
    @commethod(67)
    def get_ReportValueType(peReportValueType: POINTER(win32more.System.Performance.ReportValueTypeConstants)) -> win32more.Foundation.HRESULT: ...
    @commethod(68)
    def put_MonitorDuplicateInstances(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(69)
    def get_MonitorDuplicateInstances(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(70)
    def put_DisplayFilter(iValue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(71)
    def get_DisplayFilter(piValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(72)
    def get_LogFiles(ppILogFiles: POINTER(win32more.System.Performance.ILogFiles_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(73)
    def put_DataSourceType(eDataSourceType: win32more.System.Performance.DataSourceTypeConstants) -> win32more.Foundation.HRESULT: ...
    @commethod(74)
    def get_DataSourceType(peDataSourceType: POINTER(win32more.System.Performance.DataSourceTypeConstants)) -> win32more.Foundation.HRESULT: ...
    @commethod(75)
    def put_SqlDsnName(bsSqlDsnName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(76)
    def get_SqlDsnName(bsSqlDsnName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(77)
    def put_SqlLogSetName(bsSqlLogSetName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(78)
    def get_SqlLogSetName(bsSqlLogSetName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ISystemMonitor2(c_void_p):
    extends: win32more.System.Performance.ISystemMonitor
    Guid = Guid('08e3206a-5fd2-4fde-a8-a5-8c-b3-b6-3d-26-77')
    @commethod(79)
    def put_EnableDigitGrouping(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(80)
    def get_EnableDigitGrouping(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(81)
    def put_EnableToolTips(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(82)
    def get_EnableToolTips(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(83)
    def put_ShowTimeAxisLabels(bState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(84)
    def get_ShowTimeAxisLabels(pbState: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(85)
    def put_ChartScroll(bScroll: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(86)
    def get_ChartScroll(pbScroll: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(87)
    def put_DataPointCount(iNewCount: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(88)
    def get_DataPointCount(piDataPointCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(89)
    def ScaleToFit(bSelectedCountersOnly: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(90)
    def SaveAs(bstrFileName: win32more.Foundation.BSTR, eSysmonFileType: win32more.System.Performance.SysmonFileType) -> win32more.Foundation.HRESULT: ...
    @commethod(91)
    def Relog(bstrFileName: win32more.Foundation.BSTR, eSysmonFileType: win32more.System.Performance.SysmonFileType, iFilter: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(92)
    def ClearData() -> win32more.Foundation.HRESULT: ...
    @commethod(93)
    def get_LogSourceStartTime(pDate: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(94)
    def get_LogSourceStopTime(pDate: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(95)
    def SetLogViewRange(StartTime: Double, StopTime: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(96)
    def GetLogViewRange(StartTime: POINTER(Double), StopTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(97)
    def BatchingLock(fLock: win32more.Foundation.VARIANT_BOOL, eBatchReason: win32more.System.Performance.SysmonBatchReason) -> win32more.Foundation.HRESULT: ...
    @commethod(98)
    def LoadSettings(bstrSettingFileName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ISystemMonitorEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ee660ea0-4abd-11cf-94-3a-00-80-29-00-43-47')
    @commethod(3)
    def OnCounterSelected(Index: Int32) -> Void: ...
    @commethod(4)
    def OnCounterAdded(Index: Int32) -> Void: ...
    @commethod(5)
    def OnCounterDeleted(Index: Int32) -> Void: ...
    @commethod(6)
    def OnSampleCollected() -> Void: ...
    @commethod(7)
    def OnDblClick(Index: Int32) -> Void: ...
class ITraceDataCollector(c_void_p):
    extends: win32more.System.Performance.IDataCollector
    Guid = Guid('0383750b-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(32)
    def get_BufferSize(size: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_BufferSize(size: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_BuffersLost(buffers: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_BuffersLost(buffers: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_BuffersWritten(buffers: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_BuffersWritten(buffers: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_ClockType(clock: POINTER(win32more.System.Performance.ClockType)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_ClockType(clock: win32more.System.Performance.ClockType) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_EventsLost(events: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_EventsLost(events: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_ExtendedModes(mode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def put_ExtendedModes(mode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_FlushTimer(seconds: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_FlushTimer(seconds: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def get_FreeBuffers(buffers: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def put_FreeBuffers(buffers: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_Guid(guid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def put_Guid(guid: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def get_IsKernelTrace(kernel: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def get_MaximumBuffers(buffers: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def put_MaximumBuffers(buffers: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def get_MinimumBuffers(buffers: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def put_MinimumBuffers(buffers: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def get_NumberOfBuffers(buffers: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def put_NumberOfBuffers(buffers: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def get_PreallocateFile(allocate: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def put_PreallocateFile(allocate: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def get_ProcessMode(process: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def put_ProcessMode(process: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def get_RealTimeBuffersLost(buffers: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def put_RealTimeBuffersLost(buffers: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def get_SessionId(id: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def put_SessionId(id: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def get_SessionName(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def put_SessionName(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(67)
    def get_SessionThreadId(tid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(68)
    def put_SessionThreadId(tid: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(69)
    def get_StreamMode(mode: POINTER(win32more.System.Performance.StreamMode)) -> win32more.Foundation.HRESULT: ...
    @commethod(70)
    def put_StreamMode(mode: win32more.System.Performance.StreamMode) -> win32more.Foundation.HRESULT: ...
    @commethod(71)
    def get_TraceDataProviders(providers: POINTER(win32more.System.Performance.ITraceDataProviderCollection_head)) -> win32more.Foundation.HRESULT: ...
class ITraceDataProvider(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('03837512-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_DisplayName(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_DisplayName(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Guid(guid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Guid(guid: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Level(ppLevel: POINTER(win32more.System.Performance.IValueMap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_KeywordsAny(ppKeywords: POINTER(win32more.System.Performance.IValueMap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_KeywordsAll(ppKeywords: POINTER(win32more.System.Performance.IValueMap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_Properties(ppProperties: POINTER(win32more.System.Performance.IValueMap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_FilterEnabled(FilterEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_FilterEnabled(FilterEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_FilterType(pulType: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_FilterType(ulType: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_FilterData(ppData: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_FilterData(pData: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Query(bstrName: win32more.Foundation.BSTR, bstrServer: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def Resolve(pFrom: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetSecurity(Sddl: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetSecurity(SecurityInfo: UInt32, Sddl: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetRegisteredProcesses(Processes: POINTER(win32more.System.Performance.IValueMap_head)) -> win32more.Foundation.HRESULT: ...
class ITraceDataProviderCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('03837510-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_Count(retVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: win32more.System.Com.VARIANT, ppProvider: POINTER(win32more.System.Performance.ITraceDataProvider_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(retVal: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(pProvider: win32more.System.Performance.ITraceDataProvider_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(vProvider: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Clear() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(providers: win32more.System.Performance.ITraceDataProviderCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def CreateTraceDataProvider(Provider: POINTER(win32more.System.Performance.ITraceDataProvider_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetTraceDataProviders(server: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetTraceDataProvidersByProcess(Server: win32more.Foundation.BSTR, Pid: UInt32) -> win32more.Foundation.HRESULT: ...
class IValueMap(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('03837534-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_Count(retVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: win32more.System.Com.VARIANT, value: POINTER(win32more.System.Performance.IValueMapItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(retVal: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(description: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Description(description: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Value(Value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Value(Value: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_ValueMapType(type: POINTER(win32more.System.Performance.ValueMapType)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_ValueMapType(type: win32more.System.Performance.ValueMapType) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Add(value: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Remove(value: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def Clear() -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def AddRange(map: win32more.System.Performance.IValueMap_head) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def CreateValueMapItem(Item: POINTER(win32more.System.Performance.IValueMapItem_head)) -> win32more.Foundation.HRESULT: ...
class IValueMapItem(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('03837533-098b-11d8-94-14-50-50-54-50-30-30')
    @commethod(7)
    def get_Description(description: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Description(description: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Enabled(enabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Enabled(enabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Key(key: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_Key(key: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Value(Value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Value(Value: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_ValueMapType(type: POINTER(win32more.System.Performance.ValueMapType)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_ValueMapType(type: win32more.System.Performance.ValueMapType) -> win32more.Foundation.HRESULT: ...
LegacyDataCollectorSet = Guid('03837526-098b-11d8-94-14-50-50-54-50-30-30')
LegacyDataCollectorSetCollection = Guid('03837527-098b-11d8-94-14-50-50-54-50-30-30')
LegacyTraceSession = Guid('03837528-098b-11d8-94-14-50-50-54-50-30-30')
LegacyTraceSessionCollection = Guid('03837529-098b-11d8-94-14-50-50-54-50-30-30')
LogFileItem = Guid('16ec5be8-df93-4237-94-e4-9e-e9-18-11-1d-71')
LogFiles = Guid('2735d9fd-f6b9-4f19-a5-d9-e2-d0-68-58-4b-c5')
class PDH_BROWSE_DLG_CONFIG_A(Structure):
    _bitfield: UInt32
    hWndOwner: win32more.Foundation.HWND
    szDataSource: win32more.Foundation.PSTR
    szReturnPathBuffer: win32more.Foundation.PSTR
    cchReturnPathLength: UInt32
    pCallBack: win32more.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: win32more.System.Performance.PERF_DETAIL
    szDialogBoxCaption: win32more.Foundation.PSTR
class PDH_BROWSE_DLG_CONFIG_HA(Structure):
    _bitfield: UInt32
    hWndOwner: win32more.Foundation.HWND
    hDataSource: IntPtr
    szReturnPathBuffer: win32more.Foundation.PSTR
    cchReturnPathLength: UInt32
    pCallBack: win32more.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: win32more.System.Performance.PERF_DETAIL
    szDialogBoxCaption: win32more.Foundation.PSTR
class PDH_BROWSE_DLG_CONFIG_HW(Structure):
    _bitfield: UInt32
    hWndOwner: win32more.Foundation.HWND
    hDataSource: IntPtr
    szReturnPathBuffer: win32more.Foundation.PWSTR
    cchReturnPathLength: UInt32
    pCallBack: win32more.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: win32more.System.Performance.PERF_DETAIL
    szDialogBoxCaption: win32more.Foundation.PWSTR
class PDH_BROWSE_DLG_CONFIG_W(Structure):
    _bitfield: UInt32
    hWndOwner: win32more.Foundation.HWND
    szDataSource: win32more.Foundation.PWSTR
    szReturnPathBuffer: win32more.Foundation.PWSTR
    cchReturnPathLength: UInt32
    pCallBack: win32more.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: win32more.System.Performance.PERF_DETAIL
    szDialogBoxCaption: win32more.Foundation.PWSTR
class PDH_COUNTER_INFO_A(Structure):
    dwLength: UInt32
    dwType: UInt32
    CVersion: UInt32
    CStatus: UInt32
    lScale: Int32
    lDefaultScale: Int32
    dwUserData: UIntPtr
    dwQueryUserData: UIntPtr
    szFullPath: win32more.Foundation.PSTR
    Anonymous: _Anonymous_e__Union
    szExplainText: win32more.Foundation.PSTR
    DataBuffer: UInt32 * 1
    class _Anonymous_e__Union(Union):
        DataItemPath: win32more.System.Performance.PDH_DATA_ITEM_PATH_ELEMENTS_A
        CounterPath: win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            szMachineName: win32more.Foundation.PSTR
            szObjectName: win32more.Foundation.PSTR
            szInstanceName: win32more.Foundation.PSTR
            szParentInstance: win32more.Foundation.PSTR
            dwInstanceIndex: UInt32
            szCounterName: win32more.Foundation.PSTR
class PDH_COUNTER_INFO_W(Structure):
    dwLength: UInt32
    dwType: UInt32
    CVersion: UInt32
    CStatus: UInt32
    lScale: Int32
    lDefaultScale: Int32
    dwUserData: UIntPtr
    dwQueryUserData: UIntPtr
    szFullPath: win32more.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    szExplainText: win32more.Foundation.PWSTR
    DataBuffer: UInt32 * 1
    class _Anonymous_e__Union(Union):
        DataItemPath: win32more.System.Performance.PDH_DATA_ITEM_PATH_ELEMENTS_W
        CounterPath: win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            szMachineName: win32more.Foundation.PWSTR
            szObjectName: win32more.Foundation.PWSTR
            szInstanceName: win32more.Foundation.PWSTR
            szParentInstance: win32more.Foundation.PWSTR
            dwInstanceIndex: UInt32
            szCounterName: win32more.Foundation.PWSTR
class PDH_COUNTER_PATH_ELEMENTS_A(Structure):
    szMachineName: win32more.Foundation.PSTR
    szObjectName: win32more.Foundation.PSTR
    szInstanceName: win32more.Foundation.PSTR
    szParentInstance: win32more.Foundation.PSTR
    dwInstanceIndex: UInt32
    szCounterName: win32more.Foundation.PSTR
class PDH_COUNTER_PATH_ELEMENTS_W(Structure):
    szMachineName: win32more.Foundation.PWSTR
    szObjectName: win32more.Foundation.PWSTR
    szInstanceName: win32more.Foundation.PWSTR
    szParentInstance: win32more.Foundation.PWSTR
    dwInstanceIndex: UInt32
    szCounterName: win32more.Foundation.PWSTR
class PDH_DATA_ITEM_PATH_ELEMENTS_A(Structure):
    szMachineName: win32more.Foundation.PSTR
    ObjectGUID: Guid
    dwItemId: UInt32
    szInstanceName: win32more.Foundation.PSTR
class PDH_DATA_ITEM_PATH_ELEMENTS_W(Structure):
    szMachineName: win32more.Foundation.PWSTR
    ObjectGUID: Guid
    dwItemId: UInt32
    szInstanceName: win32more.Foundation.PWSTR
PDH_DLL_VERSION = UInt32
PDH_CVERSION_WIN50: PDH_DLL_VERSION = 1280
PDH_VERSION: PDH_DLL_VERSION = 1283
PDH_FMT = UInt32
PDH_FMT_DOUBLE: PDH_FMT = 512
PDH_FMT_LARGE: PDH_FMT = 1024
PDH_FMT_LONG: PDH_FMT = 256
class PDH_FMT_COUNTERVALUE(Structure):
    CStatus: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        longValue: Int32
        doubleValue: Double
        largeValue: Int64
        AnsiStringValue: win32more.Foundation.PSTR
        WideStringValue: win32more.Foundation.PWSTR
class PDH_FMT_COUNTERVALUE_ITEM_A(Structure):
    szName: win32more.Foundation.PSTR
    FmtValue: win32more.System.Performance.PDH_FMT_COUNTERVALUE
class PDH_FMT_COUNTERVALUE_ITEM_W(Structure):
    szName: win32more.Foundation.PWSTR
    FmtValue: win32more.System.Performance.PDH_FMT_COUNTERVALUE
PDH_LOG = UInt32
PDH_LOG_READ_ACCESS: PDH_LOG = 65536
PDH_LOG_WRITE_ACCESS: PDH_LOG = 131072
PDH_LOG_UPDATE_ACCESS: PDH_LOG = 262144
class PDH_LOG_SERVICE_QUERY_INFO_A(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwLogQuota: UInt32
    szLogFileCaption: win32more.Foundation.PSTR
    szDefaultDir: win32more.Foundation.PSTR
    szBaseFileName: win32more.Foundation.PSTR
    dwFileType: UInt32
    dwReserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(Structure):
            PdlAutoNameInterval: UInt32
            PdlAutoNameUnits: UInt32
            PdlCommandFilename: win32more.Foundation.PSTR
            PdlCounterList: win32more.Foundation.PSTR
            PdlAutoNameFormat: UInt32
            PdlSampleInterval: UInt32
            PdlLogStartTime: win32more.Foundation.FILETIME
            PdlLogEndTime: win32more.Foundation.FILETIME
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
            TlLogFileName: win32more.Foundation.PSTR
class PDH_LOG_SERVICE_QUERY_INFO_W(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwLogQuota: UInt32
    szLogFileCaption: win32more.Foundation.PWSTR
    szDefaultDir: win32more.Foundation.PWSTR
    szBaseFileName: win32more.Foundation.PWSTR
    dwFileType: UInt32
    dwReserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(Structure):
            PdlAutoNameInterval: UInt32
            PdlAutoNameUnits: UInt32
            PdlCommandFilename: win32more.Foundation.PWSTR
            PdlCounterList: win32more.Foundation.PWSTR
            PdlAutoNameFormat: UInt32
            PdlSampleInterval: UInt32
            PdlLogStartTime: win32more.Foundation.FILETIME
            PdlLogEndTime: win32more.Foundation.FILETIME
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
            TlLogFileName: win32more.Foundation.PWSTR
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
class PDH_RAW_COUNTER(Structure):
    CStatus: UInt32
    TimeStamp: win32more.Foundation.FILETIME
    FirstValue: Int64
    SecondValue: Int64
    MultiCount: UInt32
class PDH_RAW_COUNTER_ITEM_A(Structure):
    szName: win32more.Foundation.PSTR
    RawValue: win32more.System.Performance.PDH_RAW_COUNTER
class PDH_RAW_COUNTER_ITEM_W(Structure):
    szName: win32more.Foundation.PWSTR
    RawValue: win32more.System.Performance.PDH_RAW_COUNTER
class PDH_RAW_LOG_RECORD(Structure):
    dwStructureSize: UInt32
    dwRecordType: win32more.System.Performance.PDH_LOG_TYPE
    dwItems: UInt32
    RawBytes: Byte * 1
PDH_SELECT_DATA_SOURCE_FLAGS = UInt32
PDH_FLAGS_FILE_BROWSER_ONLY: PDH_SELECT_DATA_SOURCE_FLAGS = 1
PDH_FLAGS_NONE: PDH_SELECT_DATA_SOURCE_FLAGS = 0
class PDH_STATISTICS(Structure):
    dwFormat: UInt32
    count: UInt32
    min: win32more.System.Performance.PDH_FMT_COUNTERVALUE
    max: win32more.System.Performance.PDH_FMT_COUNTERVALUE
    mean: win32more.System.Performance.PDH_FMT_COUNTERVALUE
class PDH_TIME_INFO(Structure):
    StartTime: Int64
    EndTime: Int64
    SampleCount: UInt32
PERF_COUNTER_AGGREGATE_FUNC = UInt32
PERF_AGGREGATE_UNDEFINED: PERF_COUNTER_AGGREGATE_FUNC = 0
PERF_AGGREGATE_TOTAL: PERF_COUNTER_AGGREGATE_FUNC = 1
PERF_AGGREGATE_AVG: PERF_COUNTER_AGGREGATE_FUNC = 2
PERF_AGGREGATE_MIN: PERF_COUNTER_AGGREGATE_FUNC = 3
class PERF_COUNTER_BLOCK(Structure):
    ByteLength: UInt32
class PERF_COUNTER_DATA(Structure):
    dwDataSize: UInt32
    dwSize: UInt32
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
class PERF_COUNTER_HEADER(Structure):
    dwStatus: UInt32
    dwType: win32more.System.Performance.PerfCounterDataType
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
    AggregateFunc: win32more.System.Performance.PERF_COUNTER_AGGREGATE_FUNC
    Reserved: UInt32
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
class PERF_DATA_BLOCK(Structure):
    Signature: Char * 4
    LittleEndian: UInt32
    Version: UInt32
    Revision: UInt32
    TotalByteLength: UInt32
    HeaderLength: UInt32
    NumObjectTypes: UInt32
    DefaultObject: Int32
    SystemTime: win32more.Foundation.SYSTEMTIME
    PerfTime: win32more.Foundation.LARGE_INTEGER
    PerfFreq: win32more.Foundation.LARGE_INTEGER
    PerfTime100nSec: win32more.Foundation.LARGE_INTEGER
    SystemNameLength: UInt32
    SystemNameOffset: UInt32
class PERF_DATA_HEADER(Structure):
    dwTotalSize: UInt32
    dwNumCounters: UInt32
    PerfTimeStamp: Int64
    PerfTime100NSec: Int64
    PerfFreq: Int64
    SystemTime: win32more.Foundation.SYSTEMTIME
PERF_DETAIL = UInt32
PERF_DETAIL_NOVICE: PERF_DETAIL = 100
PERF_DETAIL_ADVANCED: PERF_DETAIL = 200
PERF_DETAIL_EXPERT: PERF_DETAIL = 300
PERF_DETAIL_WIZARD: PERF_DETAIL = 400
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
def PERF_MEM_ALLOC(AllocSize: UIntPtr, pContext: c_void_p) -> c_void_p: ...
@winfunctype_pointer
def PERF_MEM_FREE(pBuffer: c_void_p, pContext: c_void_p) -> Void: ...
class PERF_MULTI_COUNTERS(Structure):
    dwSize: UInt32
    dwCounters: UInt32
class PERF_MULTI_INSTANCES(Structure):
    dwTotalSize: UInt32
    dwInstances: UInt32
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
    PerfTime: win32more.Foundation.LARGE_INTEGER
    PerfFreq: win32more.Foundation.LARGE_INTEGER
class PERF_PROVIDER_CONTEXT(Structure):
    ContextSize: UInt32
    Reserved: UInt32
    ControlCallback: win32more.System.Performance.PERFLIBREQUEST
    MemAllocRoutine: win32more.System.Performance.PERF_MEM_ALLOC
    MemFreeRoutine: win32more.System.Performance.PERF_MEM_FREE
    pMemContext: c_void_p
class PERF_STRING_BUFFER_HEADER(Structure):
    dwSize: UInt32
    dwCounters: UInt32
class PERF_STRING_COUNTER_HEADER(Structure):
    dwCounterId: UInt32
    dwOffset: UInt32
PerfCounterDataType = Int32
PERF_ERROR_RETURN: PerfCounterDataType = 0
PERF_SINGLE_COUNTER: PerfCounterDataType = 1
PERF_MULTIPLE_COUNTERS: PerfCounterDataType = 2
PERF_MULTIPLE_INSTANCES: PerfCounterDataType = 4
PERF_COUNTERSET: PerfCounterDataType = 6
@winfunctype_pointer
def PERFLIBREQUEST(RequestCode: UInt32, Buffer: c_void_p, BufferSize: UInt32) -> UInt32: ...
PerfProviderHandle = IntPtr
PerfQueryHandle = IntPtr
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
@winfunctype_pointer
def PLA_CABEXTRACT_CALLBACK(FileName: win32more.Foundation.PWSTR, Context: c_void_p) -> Void: ...
@winfunctype_pointer
def PM_CLOSE_PROC() -> UInt32: ...
@winfunctype_pointer
def PM_COLLECT_PROC(pValueName: win32more.Foundation.PWSTR, ppData: POINTER(c_void_p), pcbTotalBytes: POINTER(UInt32), pNumObjectTypes: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PM_OPEN_PROC(pContext: win32more.Foundation.PWSTR) -> UInt32: ...
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
ServerDataCollectorSet = Guid('03837531-098b-11d8-94-14-50-50-54-50-30-30')
ServerDataCollectorSetCollection = Guid('03837532-098b-11d8-94-14-50-50-54-50-30-30')
SourcePropPage = Guid('0cf32aa1-7571-11d0-93-c4-00-aa-00-a3-dd-ea')
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
SystemDataCollectorSet = Guid('03837546-098b-11d8-94-14-50-50-54-50-30-30')
SystemDataCollectorSetCollection = Guid('03837547-098b-11d8-94-14-50-50-54-50-30-30')
SystemMonitor = Guid('c4d2d8e0-d1dd-11ce-94-0f-00-80-29-00-43-47')
SystemMonitor2 = Guid('7f30578c-5f38-4612-ac-fe-6e-d0-4c-7b-7a-f8')
TraceDataProvider = Guid('03837513-098b-11d8-94-14-50-50-54-50-30-30')
TraceDataProviderCollection = Guid('03837511-098b-11d8-94-14-50-50-54-50-30-30')
TraceSession = Guid('0383751c-098b-11d8-94-14-50-50-54-50-30-30')
TraceSessionCollection = Guid('03837530-098b-11d8-94-14-50-50-54-50-30-30')
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
make_head(_module, '_ICounterItemUnion')
make_head(_module, '_ISystemMonitorUnion')
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
make_head(_module, 'PERF_COUNTER_BLOCK')
make_head(_module, 'PERF_COUNTER_DATA')
make_head(_module, 'PERF_COUNTER_DEFINITION')
make_head(_module, 'PERF_COUNTER_HEADER')
make_head(_module, 'PERF_COUNTER_IDENTIFIER')
make_head(_module, 'PERF_COUNTER_IDENTITY')
make_head(_module, 'PERF_COUNTER_INFO')
make_head(_module, 'PERF_COUNTER_REG_INFO')
make_head(_module, 'PERF_COUNTERSET_INFO')
make_head(_module, 'PERF_COUNTERSET_INSTANCE')
make_head(_module, 'PERF_COUNTERSET_REG_INFO')
make_head(_module, 'PERF_DATA_BLOCK')
make_head(_module, 'PERF_DATA_HEADER')
make_head(_module, 'PERF_INSTANCE_DEFINITION')
make_head(_module, 'PERF_INSTANCE_HEADER')
make_head(_module, 'PERF_MEM_ALLOC')
make_head(_module, 'PERF_MEM_FREE')
make_head(_module, 'PERF_MULTI_COUNTERS')
make_head(_module, 'PERF_MULTI_INSTANCES')
make_head(_module, 'PERF_OBJECT_TYPE')
make_head(_module, 'PERF_PROVIDER_CONTEXT')
make_head(_module, 'PERF_STRING_BUFFER_HEADER')
make_head(_module, 'PERF_STRING_COUNTER_HEADER')
make_head(_module, 'PERFLIBREQUEST')
make_head(_module, 'PLA_CABEXTRACT_CALLBACK')
make_head(_module, 'PM_CLOSE_PROC')
make_head(_module, 'PM_COLLECT_PROC')
make_head(_module, 'PM_OPEN_PROC')
__all__ = [
    "AppearPropPage",
    "AutoPathFormat",
    "AutoPathFormat_plaComputer",
    "AutoPathFormat_plaMonthDayHour",
    "AutoPathFormat_plaMonthDayHourMinute",
    "AutoPathFormat_plaNone",
    "AutoPathFormat_plaPattern",
    "AutoPathFormat_plaSerialNumber",
    "AutoPathFormat_plaYearDayOfYear",
    "AutoPathFormat_plaYearMonth",
    "AutoPathFormat_plaYearMonthDay",
    "AutoPathFormat_plaYearMonthDayHour",
    "BackupPerfRegistryToFileW",
    "BootTraceSession",
    "BootTraceSessionCollection",
    "ClockType",
    "ClockType_plaCycle",
    "ClockType_plaPerformance",
    "ClockType_plaSystem",
    "ClockType_plaTimeStamp",
    "CommitMode",
    "CommitMode_plaCreateNew",
    "CommitMode_plaCreateOrModify",
    "CommitMode_plaFlushTrace",
    "CommitMode_plaModify",
    "CommitMode_plaUpdateRunningInstance",
    "CommitMode_plaValidateOnly",
    "CounterItem",
    "CounterItem2",
    "CounterPathCallBack",
    "CounterPropPage",
    "Counters",
    "DATA_SOURCE_REGISTRY",
    "DATA_SOURCE_WBEM",
    "DICounterItem",
    "DIID_DICounterItem",
    "DIID_DILogFileItem",
    "DIID_DISystemMonitor",
    "DIID_DISystemMonitorEvents",
    "DIID_DISystemMonitorInternal",
    "DILogFileItem",
    "DISystemMonitor",
    "DISystemMonitorEvents",
    "DISystemMonitorInternal",
    "DataCollectorSet",
    "DataCollectorSetCollection",
    "DataCollectorSetStatus",
    "DataCollectorSetStatus_plaCompiling",
    "DataCollectorSetStatus_plaPending",
    "DataCollectorSetStatus_plaRunning",
    "DataCollectorSetStatus_plaStopped",
    "DataCollectorSetStatus_plaUndefined",
    "DataCollectorType",
    "DataCollectorType_plaAlert",
    "DataCollectorType_plaApiTrace",
    "DataCollectorType_plaConfiguration",
    "DataCollectorType_plaPerformanceCounter",
    "DataCollectorType_plaTrace",
    "DataManagerSteps",
    "DataManagerSteps_plaCreateHtml",
    "DataManagerSteps_plaCreateReport",
    "DataManagerSteps_plaFolderActions",
    "DataManagerSteps_plaResourceFreeing",
    "DataManagerSteps_plaRunRules",
    "DataSourceTypeConstants",
    "DataSourceTypeConstants_sysmonCurrentActivity",
    "DataSourceTypeConstants_sysmonLogFiles",
    "DataSourceTypeConstants_sysmonNullDataSource",
    "DataSourceTypeConstants_sysmonSqlLog",
    "DisplayTypeConstants",
    "DisplayTypeConstants_sysmonChartArea",
    "DisplayTypeConstants_sysmonChartStackedArea",
    "DisplayTypeConstants_sysmonHistogram",
    "DisplayTypeConstants_sysmonLineGraph",
    "DisplayTypeConstants_sysmonReport",
    "FileFormat",
    "FileFormat_plaBinary",
    "FileFormat_plaCommaSeparated",
    "FileFormat_plaSql",
    "FileFormat_plaTabSeparated",
    "FolderActionSteps",
    "FolderActionSteps_plaCreateCab",
    "FolderActionSteps_plaDeleteCab",
    "FolderActionSteps_plaDeleteData",
    "FolderActionSteps_plaDeleteReport",
    "FolderActionSteps_plaSendCab",
    "GeneralPropPage",
    "GraphPropPage",
    "H_WBEM_DATASOURCE",
    "IAlertDataCollector",
    "IApiTracingDataCollector",
    "IConfigurationDataCollector",
    "ICounterItem",
    "ICounterItem2",
    "ICounters",
    "IDataCollector",
    "IDataCollectorCollection",
    "IDataCollectorSet",
    "IDataCollectorSetCollection",
    "IDataManager",
    "IFolderAction",
    "IFolderActionCollection",
    "ILogFileItem",
    "ILogFiles",
    "IPerformanceCounterDataCollector",
    "ISchedule",
    "IScheduleCollection",
    "ISystemMonitor",
    "ISystemMonitor2",
    "ISystemMonitorEvents",
    "ITraceDataCollector",
    "ITraceDataProvider",
    "ITraceDataProviderCollection",
    "IValueMap",
    "IValueMapItem",
    "InstallPerfDllA",
    "InstallPerfDllW",
    "LIBID_SystemMonitor",
    "LegacyDataCollectorSet",
    "LegacyDataCollectorSetCollection",
    "LegacyTraceSession",
    "LegacyTraceSessionCollection",
    "LoadPerfCounterTextStringsA",
    "LoadPerfCounterTextStringsW",
    "LogFileItem",
    "LogFiles",
    "MAX_COUNTER_PATH",
    "MAX_PERF_OBJECTS_IN_QUERY_FUNCTION",
    "PDH_ACCESS_DENIED",
    "PDH_ASYNC_QUERY_TIMEOUT",
    "PDH_BINARY_LOG_CORRUPT",
    "PDH_BROWSE_DLG_CONFIG_A",
    "PDH_BROWSE_DLG_CONFIG_HA",
    "PDH_BROWSE_DLG_CONFIG_HW",
    "PDH_BROWSE_DLG_CONFIG_W",
    "PDH_CALC_NEGATIVE_DENOMINATOR",
    "PDH_CALC_NEGATIVE_TIMEBASE",
    "PDH_CALC_NEGATIVE_VALUE",
    "PDH_CANNOT_CONNECT_MACHINE",
    "PDH_CANNOT_CONNECT_WMI_SERVER",
    "PDH_CANNOT_READ_NAME_STRINGS",
    "PDH_CANNOT_SET_DEFAULT_REALTIME_DATASOURCE",
    "PDH_COUNTER_ALREADY_IN_QUERY",
    "PDH_COUNTER_INFO_A",
    "PDH_COUNTER_INFO_W",
    "PDH_COUNTER_PATH_ELEMENTS_A",
    "PDH_COUNTER_PATH_ELEMENTS_W",
    "PDH_CSTATUS_BAD_COUNTERNAME",
    "PDH_CSTATUS_INVALID_DATA",
    "PDH_CSTATUS_ITEM_NOT_VALIDATED",
    "PDH_CSTATUS_NEW_DATA",
    "PDH_CSTATUS_NO_COUNTER",
    "PDH_CSTATUS_NO_COUNTERNAME",
    "PDH_CSTATUS_NO_INSTANCE",
    "PDH_CSTATUS_NO_MACHINE",
    "PDH_CSTATUS_NO_OBJECT",
    "PDH_CSTATUS_VALID_DATA",
    "PDH_CVERSION_WIN50",
    "PDH_DATA_ITEM_PATH_ELEMENTS_A",
    "PDH_DATA_ITEM_PATH_ELEMENTS_W",
    "PDH_DATA_SOURCE_IS_LOG_FILE",
    "PDH_DATA_SOURCE_IS_REAL_TIME",
    "PDH_DIALOG_CANCELLED",
    "PDH_DLL_VERSION",
    "PDH_END_OF_LOG_FILE",
    "PDH_ENTRY_NOT_IN_LOG_FILE",
    "PDH_FILE_ALREADY_EXISTS",
    "PDH_FILE_NOT_FOUND",
    "PDH_FLAGS_FILE_BROWSER_ONLY",
    "PDH_FLAGS_NONE",
    "PDH_FMT",
    "PDH_FMT_COUNTERVALUE",
    "PDH_FMT_COUNTERVALUE_ITEM_A",
    "PDH_FMT_COUNTERVALUE_ITEM_W",
    "PDH_FMT_DOUBLE",
    "PDH_FMT_LARGE",
    "PDH_FMT_LONG",
    "PDH_FUNCTION_NOT_FOUND",
    "PDH_INCORRECT_APPEND_TIME",
    "PDH_INSUFFICIENT_BUFFER",
    "PDH_INVALID_ARGUMENT",
    "PDH_INVALID_BUFFER",
    "PDH_INVALID_DATA",
    "PDH_INVALID_DATASOURCE",
    "PDH_INVALID_HANDLE",
    "PDH_INVALID_INSTANCE",
    "PDH_INVALID_PATH",
    "PDH_INVALID_SQLDB",
    "PDH_INVALID_SQL_LOG_FORMAT",
    "PDH_LOG",
    "PDH_LOGSVC_NOT_OPENED",
    "PDH_LOGSVC_QUERY_NOT_FOUND",
    "PDH_LOG_FILE_CREATE_ERROR",
    "PDH_LOG_FILE_OPEN_ERROR",
    "PDH_LOG_FILE_TOO_SMALL",
    "PDH_LOG_READ_ACCESS",
    "PDH_LOG_SAMPLE_TOO_SMALL",
    "PDH_LOG_SERVICE_QUERY_INFO_A",
    "PDH_LOG_SERVICE_QUERY_INFO_W",
    "PDH_LOG_TYPE",
    "PDH_LOG_TYPE_BINARY",
    "PDH_LOG_TYPE_CSV",
    "PDH_LOG_TYPE_NOT_FOUND",
    "PDH_LOG_TYPE_PERFMON",
    "PDH_LOG_TYPE_RETIRED_BIN",
    "PDH_LOG_TYPE_SQL",
    "PDH_LOG_TYPE_TRACE_GENERIC",
    "PDH_LOG_TYPE_TRACE_KERNEL",
    "PDH_LOG_TYPE_TSV",
    "PDH_LOG_TYPE_UNDEFINED",
    "PDH_LOG_UPDATE_ACCESS",
    "PDH_LOG_WRITE_ACCESS",
    "PDH_MAX_COUNTER_NAME",
    "PDH_MAX_COUNTER_PATH",
    "PDH_MAX_DATASOURCE_PATH",
    "PDH_MAX_INSTANCE_NAME",
    "PDH_MAX_SCALE",
    "PDH_MEMORY_ALLOCATION_FAILURE",
    "PDH_MIN_SCALE",
    "PDH_MORE_DATA",
    "PDH_NOEXPANDCOUNTERS",
    "PDH_NOEXPANDINSTANCES",
    "PDH_NOT_IMPLEMENTED",
    "PDH_NO_COUNTERS",
    "PDH_NO_DATA",
    "PDH_NO_DIALOG_DATA",
    "PDH_NO_MORE_DATA",
    "PDH_OS_EARLIER_VERSION",
    "PDH_OS_LATER_VERSION",
    "PDH_PATH_FLAGS",
    "PDH_PATH_WBEM_INPUT",
    "PDH_PATH_WBEM_NONE",
    "PDH_PATH_WBEM_RESULT",
    "PDH_PLA_COLLECTION_ALREADY_RUNNING",
    "PDH_PLA_COLLECTION_NOT_FOUND",
    "PDH_PLA_ERROR_ALREADY_EXISTS",
    "PDH_PLA_ERROR_FILEPATH",
    "PDH_PLA_ERROR_NAME_TOO_LONG",
    "PDH_PLA_ERROR_NOSTART",
    "PDH_PLA_ERROR_SCHEDULE_ELAPSED",
    "PDH_PLA_ERROR_SCHEDULE_OVERLAP",
    "PDH_PLA_ERROR_TYPE_MISMATCH",
    "PDH_PLA_SERVICE_ERROR",
    "PDH_PLA_VALIDATION_ERROR",
    "PDH_PLA_VALIDATION_WARNING",
    "PDH_QUERY_PERF_DATA_TIMEOUT",
    "PDH_RAW_COUNTER",
    "PDH_RAW_COUNTER_ITEM_A",
    "PDH_RAW_COUNTER_ITEM_W",
    "PDH_RAW_LOG_RECORD",
    "PDH_REFRESHCOUNTERS",
    "PDH_RETRY",
    "PDH_SELECT_DATA_SOURCE_FLAGS",
    "PDH_SQL_ALLOCCON_FAILED",
    "PDH_SQL_ALLOC_FAILED",
    "PDH_SQL_ALTER_DETAIL_FAILED",
    "PDH_SQL_BIND_FAILED",
    "PDH_SQL_CONNECT_FAILED",
    "PDH_SQL_EXEC_DIRECT_FAILED",
    "PDH_SQL_FETCH_FAILED",
    "PDH_SQL_MORE_RESULTS_FAILED",
    "PDH_SQL_ROWCOUNT_FAILED",
    "PDH_STATISTICS",
    "PDH_STRING_NOT_FOUND",
    "PDH_TIME_INFO",
    "PDH_UNABLE_MAP_NAME_FILES",
    "PDH_UNABLE_READ_LOG_HEADER",
    "PDH_UNKNOWN_LOGSVC_COMMAND",
    "PDH_UNKNOWN_LOG_FORMAT",
    "PDH_UNMATCHED_APPEND_COUNTER",
    "PDH_VERSION",
    "PDH_WBEM_ERROR",
    "PERFLIBREQUEST",
    "PERF_ADD_COUNTER",
    "PERF_AGGREGATE_AVG",
    "PERF_AGGREGATE_INSTANCE",
    "PERF_AGGREGATE_MAX",
    "PERF_AGGREGATE_MIN",
    "PERF_AGGREGATE_TOTAL",
    "PERF_AGGREGATE_UNDEFINED",
    "PERF_ATTRIB_BY_REFERENCE",
    "PERF_ATTRIB_DISPLAY_AS_HEX",
    "PERF_ATTRIB_DISPLAY_AS_REAL",
    "PERF_ATTRIB_NO_DISPLAYABLE",
    "PERF_ATTRIB_NO_GROUP_SEPARATOR",
    "PERF_COLLECT_END",
    "PERF_COLLECT_START",
    "PERF_COUNTERSET",
    "PERF_COUNTERSET_FLAG_AGGREGATE",
    "PERF_COUNTERSET_FLAG_HISTORY",
    "PERF_COUNTERSET_FLAG_INSTANCE",
    "PERF_COUNTERSET_FLAG_MULTIPLE",
    "PERF_COUNTERSET_INFO",
    "PERF_COUNTERSET_INSTANCE",
    "PERF_COUNTERSET_MULTI_INSTANCES",
    "PERF_COUNTERSET_REG_INFO",
    "PERF_COUNTERSET_SINGLE_AGGREGATE",
    "PERF_COUNTERSET_SINGLE_INSTANCE",
    "PERF_COUNTER_AGGREGATE_FUNC",
    "PERF_COUNTER_BASE",
    "PERF_COUNTER_BLOCK",
    "PERF_COUNTER_DATA",
    "PERF_COUNTER_DEFINITION",
    "PERF_COUNTER_ELAPSED",
    "PERF_COUNTER_FRACTION",
    "PERF_COUNTER_HEADER",
    "PERF_COUNTER_HISTOGRAM",
    "PERF_COUNTER_HISTOGRAM_TYPE",
    "PERF_COUNTER_IDENTIFIER",
    "PERF_COUNTER_IDENTITY",
    "PERF_COUNTER_INFO",
    "PERF_COUNTER_PRECISION",
    "PERF_COUNTER_QUEUELEN",
    "PERF_COUNTER_RATE",
    "PERF_COUNTER_REG_INFO",
    "PERF_COUNTER_VALUE",
    "PERF_DATA_BLOCK",
    "PERF_DATA_HEADER",
    "PERF_DATA_REVISION",
    "PERF_DATA_VERSION",
    "PERF_DELTA_BASE",
    "PERF_DELTA_COUNTER",
    "PERF_DETAIL",
    "PERF_DETAIL_ADVANCED",
    "PERF_DETAIL_EXPERT",
    "PERF_DETAIL_NOVICE",
    "PERF_DETAIL_WIZARD",
    "PERF_DISPLAY_NOSHOW",
    "PERF_DISPLAY_NO_SUFFIX",
    "PERF_DISPLAY_PERCENT",
    "PERF_DISPLAY_PER_SEC",
    "PERF_DISPLAY_SECONDS",
    "PERF_ENUM_INSTANCES",
    "PERF_ERROR_RETURN",
    "PERF_FILTER",
    "PERF_INSTANCE_DEFINITION",
    "PERF_INSTANCE_HEADER",
    "PERF_INVERSE_COUNTER",
    "PERF_MAX_INSTANCE_NAME",
    "PERF_MEM_ALLOC",
    "PERF_MEM_FREE",
    "PERF_METADATA_MULTIPLE_INSTANCES",
    "PERF_METADATA_NO_INSTANCES",
    "PERF_MULTIPLE_COUNTERS",
    "PERF_MULTIPLE_INSTANCES",
    "PERF_MULTI_COUNTER",
    "PERF_MULTI_COUNTERS",
    "PERF_MULTI_INSTANCES",
    "PERF_NO_INSTANCES",
    "PERF_NO_UNIQUE_ID",
    "PERF_NUMBER_DECIMAL",
    "PERF_NUMBER_DEC_1000",
    "PERF_NUMBER_HEX",
    "PERF_OBJECT_TIMER",
    "PERF_OBJECT_TYPE",
    "PERF_PROVIDER_CONTEXT",
    "PERF_PROVIDER_DRIVER",
    "PERF_PROVIDER_KERNEL_MODE",
    "PERF_PROVIDER_USER_MODE",
    "PERF_REG_COUNTERSET_ENGLISH_NAME",
    "PERF_REG_COUNTERSET_HELP_STRING",
    "PERF_REG_COUNTERSET_NAME_STRING",
    "PERF_REG_COUNTERSET_STRUCT",
    "PERF_REG_COUNTER_ENGLISH_NAMES",
    "PERF_REG_COUNTER_HELP_STRINGS",
    "PERF_REG_COUNTER_NAME_STRINGS",
    "PERF_REG_COUNTER_STRUCT",
    "PERF_REG_PROVIDER_GUID",
    "PERF_REG_PROVIDER_NAME",
    "PERF_REMOVE_COUNTER",
    "PERF_SINGLE_COUNTER",
    "PERF_SIZE_DWORD",
    "PERF_SIZE_LARGE",
    "PERF_SIZE_VARIABLE_LEN",
    "PERF_SIZE_ZERO",
    "PERF_STRING_BUFFER_HEADER",
    "PERF_STRING_COUNTER_HEADER",
    "PERF_TEXT_ASCII",
    "PERF_TEXT_UNICODE",
    "PERF_TIMER_100NS",
    "PERF_TIMER_TICK",
    "PERF_TYPE_COUNTER",
    "PERF_TYPE_NUMBER",
    "PERF_TYPE_TEXT",
    "PERF_TYPE_ZERO",
    "PERF_WILDCARD_COUNTER",
    "PERF_WILDCARD_INSTANCE",
    "PLAL_ALERT_CMD_LINE_A_NAME",
    "PLAL_ALERT_CMD_LINE_C_NAME",
    "PLAL_ALERT_CMD_LINE_D_TIME",
    "PLAL_ALERT_CMD_LINE_L_VAL",
    "PLAL_ALERT_CMD_LINE_MASK",
    "PLAL_ALERT_CMD_LINE_M_VAL",
    "PLAL_ALERT_CMD_LINE_SINGLE",
    "PLAL_ALERT_CMD_LINE_U_TEXT",
    "PLA_CABEXTRACT_CALLBACK",
    "PLA_CAPABILITY_AUTOLOGGER",
    "PLA_CAPABILITY_LEGACY_SESSION",
    "PLA_CAPABILITY_LEGACY_SVC",
    "PLA_CAPABILITY_LOCAL",
    "PLA_CAPABILITY_V1_SESSION",
    "PLA_CAPABILITY_V1_SVC",
    "PLA_CAPABILITY_V1_SYSTEM",
    "PM_CLOSE_PROC",
    "PM_COLLECT_PROC",
    "PM_OPEN_PROC",
    "PdhAddCounterA",
    "PdhAddCounterW",
    "PdhAddEnglishCounterA",
    "PdhAddEnglishCounterW",
    "PdhBindInputDataSourceA",
    "PdhBindInputDataSourceW",
    "PdhBrowseCountersA",
    "PdhBrowseCountersHA",
    "PdhBrowseCountersHW",
    "PdhBrowseCountersW",
    "PdhCalculateCounterFromRawValue",
    "PdhCloseLog",
    "PdhCloseQuery",
    "PdhCollectQueryData",
    "PdhCollectQueryDataEx",
    "PdhCollectQueryDataWithTime",
    "PdhComputeCounterStatistics",
    "PdhConnectMachineA",
    "PdhConnectMachineW",
    "PdhCreateSQLTablesA",
    "PdhCreateSQLTablesW",
    "PdhEnumLogSetNamesA",
    "PdhEnumLogSetNamesW",
    "PdhEnumMachinesA",
    "PdhEnumMachinesHA",
    "PdhEnumMachinesHW",
    "PdhEnumMachinesW",
    "PdhEnumObjectItemsA",
    "PdhEnumObjectItemsHA",
    "PdhEnumObjectItemsHW",
    "PdhEnumObjectItemsW",
    "PdhEnumObjectsA",
    "PdhEnumObjectsHA",
    "PdhEnumObjectsHW",
    "PdhEnumObjectsW",
    "PdhExpandCounterPathA",
    "PdhExpandCounterPathW",
    "PdhExpandWildCardPathA",
    "PdhExpandWildCardPathHA",
    "PdhExpandWildCardPathHW",
    "PdhExpandWildCardPathW",
    "PdhFormatFromRawValue",
    "PdhGetCounterInfoA",
    "PdhGetCounterInfoW",
    "PdhGetCounterTimeBase",
    "PdhGetDataSourceTimeRangeA",
    "PdhGetDataSourceTimeRangeH",
    "PdhGetDataSourceTimeRangeW",
    "PdhGetDefaultPerfCounterA",
    "PdhGetDefaultPerfCounterHA",
    "PdhGetDefaultPerfCounterHW",
    "PdhGetDefaultPerfCounterW",
    "PdhGetDefaultPerfObjectA",
    "PdhGetDefaultPerfObjectHA",
    "PdhGetDefaultPerfObjectHW",
    "PdhGetDefaultPerfObjectW",
    "PdhGetDllVersion",
    "PdhGetFormattedCounterArrayA",
    "PdhGetFormattedCounterArrayW",
    "PdhGetFormattedCounterValue",
    "PdhGetLogFileSize",
    "PdhGetLogSetGUID",
    "PdhGetRawCounterArrayA",
    "PdhGetRawCounterArrayW",
    "PdhGetRawCounterValue",
    "PdhIsRealTimeQuery",
    "PdhLookupPerfIndexByNameA",
    "PdhLookupPerfIndexByNameW",
    "PdhLookupPerfNameByIndexA",
    "PdhLookupPerfNameByIndexW",
    "PdhMakeCounterPathA",
    "PdhMakeCounterPathW",
    "PdhOpenLogA",
    "PdhOpenLogW",
    "PdhOpenQueryA",
    "PdhOpenQueryH",
    "PdhOpenQueryW",
    "PdhParseCounterPathA",
    "PdhParseCounterPathW",
    "PdhParseInstanceNameA",
    "PdhParseInstanceNameW",
    "PdhReadRawLogRecord",
    "PdhRemoveCounter",
    "PdhSelectDataSourceA",
    "PdhSelectDataSourceW",
    "PdhSetCounterScaleFactor",
    "PdhSetDefaultRealTimeDataSource",
    "PdhSetLogSetRunID",
    "PdhSetQueryTimeRange",
    "PdhUpdateLogA",
    "PdhUpdateLogFileCatalog",
    "PdhUpdateLogW",
    "PdhValidatePathA",
    "PdhValidatePathExA",
    "PdhValidatePathExW",
    "PdhValidatePathW",
    "PdhVerifySQLDBA",
    "PdhVerifySQLDBW",
    "PerfAddCounters",
    "PerfCloseQueryHandle",
    "PerfCounterDataType",
    "PerfCreateInstance",
    "PerfDecrementULongCounterValue",
    "PerfDecrementULongLongCounterValue",
    "PerfDeleteCounters",
    "PerfDeleteInstance",
    "PerfEnumerateCounterSet",
    "PerfEnumerateCounterSetInstances",
    "PerfIncrementULongCounterValue",
    "PerfIncrementULongLongCounterValue",
    "PerfOpenQueryHandle",
    "PerfProviderHandle",
    "PerfQueryCounterData",
    "PerfQueryCounterInfo",
    "PerfQueryCounterSetRegistrationInfo",
    "PerfQueryHandle",
    "PerfQueryInstance",
    "PerfRegInfoType",
    "PerfSetCounterRefValue",
    "PerfSetCounterSetInfo",
    "PerfSetULongCounterValue",
    "PerfSetULongLongCounterValue",
    "PerfStartProvider",
    "PerfStartProviderEx",
    "PerfStopProvider",
    "QueryPerformanceCounter",
    "QueryPerformanceFrequency",
    "REAL_TIME_DATA_SOURCE_ID_FLAGS",
    "ReportValueTypeConstants",
    "ReportValueTypeConstants_sysmonAverage",
    "ReportValueTypeConstants_sysmonCurrentValue",
    "ReportValueTypeConstants_sysmonDefaultValue",
    "ReportValueTypeConstants_sysmonMaximum",
    "ReportValueTypeConstants_sysmonMinimum",
    "ResourcePolicy",
    "ResourcePolicy_plaDeleteLargest",
    "ResourcePolicy_plaDeleteOldest",
    "RestorePerfRegistryFromFileW",
    "S_PDH",
    "ServerDataCollectorSet",
    "ServerDataCollectorSetCollection",
    "SetServiceAsTrustedA",
    "SetServiceAsTrustedW",
    "SourcePropPage",
    "StreamMode",
    "StreamMode_plaBoth",
    "StreamMode_plaBuffering",
    "StreamMode_plaFile",
    "StreamMode_plaRealTime",
    "SysmonBatchReason",
    "SysmonBatchReason_sysmonBatchAddCounters",
    "SysmonBatchReason_sysmonBatchAddFiles",
    "SysmonBatchReason_sysmonBatchAddFilesAutoCounters",
    "SysmonBatchReason_sysmonBatchNone",
    "SysmonDataType",
    "SysmonDataType_sysmonDataAvg",
    "SysmonDataType_sysmonDataCount",
    "SysmonDataType_sysmonDataMax",
    "SysmonDataType_sysmonDataMin",
    "SysmonDataType_sysmonDataTime",
    "SysmonFileType",
    "SysmonFileType_sysmonFileBlg",
    "SysmonFileType_sysmonFileCsv",
    "SysmonFileType_sysmonFileGif",
    "SysmonFileType_sysmonFileHtml",
    "SysmonFileType_sysmonFileReport",
    "SysmonFileType_sysmonFileRetiredBlg",
    "SysmonFileType_sysmonFileTsv",
    "SystemDataCollectorSet",
    "SystemDataCollectorSetCollection",
    "SystemMonitor",
    "SystemMonitor2",
    "TraceDataProvider",
    "TraceDataProviderCollection",
    "TraceSession",
    "TraceSessionCollection",
    "UnloadPerfCounterTextStringsA",
    "UnloadPerfCounterTextStringsW",
    "UpdatePerfNameFilesA",
    "UpdatePerfNameFilesW",
    "ValueMapType",
    "ValueMapType_plaFlag",
    "ValueMapType_plaFlagArray",
    "ValueMapType_plaIndex",
    "ValueMapType_plaValidation",
    "WINPERF_LOG_DEBUG",
    "WINPERF_LOG_NONE",
    "WINPERF_LOG_USER",
    "WINPERF_LOG_VERBOSE",
    "WeekDays",
    "WeekDays_plaEveryday",
    "WeekDays_plaFriday",
    "WeekDays_plaMonday",
    "WeekDays_plaRunOnce",
    "WeekDays_plaSaturday",
    "WeekDays_plaSunday",
    "WeekDays_plaThursday",
    "WeekDays_plaTuesday",
    "WeekDays_plaWednesday",
    "_ICounterItemUnion",
    "_ISystemMonitorUnion",
]
