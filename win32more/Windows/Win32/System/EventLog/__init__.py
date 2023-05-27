from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.EventLog
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
EVT_VARIANT_TYPE_MASK: UInt32 = 127
EVT_VARIANT_TYPE_ARRAY: UInt32 = 128
EVT_READ_ACCESS: UInt32 = 1
EVT_WRITE_ACCESS: UInt32 = 2
EVT_CLEAR_ACCESS: UInt32 = 4
EVT_ALL_ACCESS: UInt32 = 7
@winfunctype('wevtapi.dll')
def EvtOpenSession(LoginClass: win32more.Windows.Win32.System.EventLog.EVT_LOGIN_CLASS, Login: VoidPtr, Timeout: UInt32, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtClose(Object: win32more.Windows.Win32.System.EventLog.EVT_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtCancel(Object: win32more.Windows.Win32.System.EventLog.EVT_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtGetExtendedStatus(BufferSize: UInt32, Buffer: win32more.Windows.Win32.Foundation.PWSTR, BufferUsed: POINTER(UInt32)) -> UInt32: ...
@winfunctype('wevtapi.dll')
def EvtQuery(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Path: win32more.Windows.Win32.Foundation.PWSTR, Query: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtNext(ResultSet: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, EventsSize: UInt32, Events: POINTER(IntPtr), Timeout: UInt32, Flags: UInt32, Returned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtSeek(ResultSet: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Position: Int64, Bookmark: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Timeout: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtSubscribe(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, SignalEvent: win32more.Windows.Win32.Foundation.HANDLE, ChannelPath: win32more.Windows.Win32.Foundation.PWSTR, Query: win32more.Windows.Win32.Foundation.PWSTR, Bookmark: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Context: VoidPtr, Callback: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_CALLBACK, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtCreateRenderContext(ValuePathsCount: UInt32, ValuePaths: POINTER(win32more.Windows.Win32.Foundation.PWSTR), Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtRender(Context: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Fragment: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Flags: UInt32, BufferSize: UInt32, Buffer: VoidPtr, BufferUsed: POINTER(UInt32), PropertyCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtFormatMessage(PublisherMetadata: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Event: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, MessageId: UInt32, ValueCount: UInt32, Values: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT_head), Flags: UInt32, BufferSize: UInt32, Buffer: win32more.Windows.Win32.Foundation.PWSTR, BufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtOpenLog(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Path: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtGetLogInfo(Log: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT_head), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtClearLog(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, ChannelPath: win32more.Windows.Win32.Foundation.PWSTR, TargetFilePath: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtExportLog(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Path: win32more.Windows.Win32.Foundation.PWSTR, Query: win32more.Windows.Win32.Foundation.PWSTR, TargetFilePath: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtArchiveExportedLog(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, LogFilePath: win32more.Windows.Win32.Foundation.PWSTR, Locale: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtOpenChannelEnum(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtNextChannelPath(ChannelEnum: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, ChannelPathBufferSize: UInt32, ChannelPathBuffer: win32more.Windows.Win32.Foundation.PWSTR, ChannelPathBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtOpenChannelConfig(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, ChannelPath: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtSaveChannelConfig(ChannelConfig: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtSetChannelConfigProperty(ChannelConfig: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID, Flags: UInt32, PropertyValue: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtGetChannelConfigProperty(ChannelConfig: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID, Flags: UInt32, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT_head), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtOpenPublisherEnum(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtNextPublisherId(PublisherEnum: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PublisherIdBufferSize: UInt32, PublisherIdBuffer: win32more.Windows.Win32.Foundation.PWSTR, PublisherIdBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtOpenPublisherMetadata(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PublisherId: win32more.Windows.Win32.Foundation.PWSTR, LogFilePath: win32more.Windows.Win32.Foundation.PWSTR, Locale: UInt32, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtGetPublisherMetadataProperty(PublisherMetadata: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID, Flags: UInt32, PublisherMetadataPropertyBufferSize: UInt32, PublisherMetadataPropertyBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT_head), PublisherMetadataPropertyBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtOpenEventMetadataEnum(PublisherMetadata: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtNextEventMetadata(EventMetadataEnum: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtGetEventMetadataProperty(EventMetadata: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID, Flags: UInt32, EventMetadataPropertyBufferSize: UInt32, EventMetadataPropertyBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT_head), EventMetadataPropertyBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtGetObjectArraySize(ObjectArray: IntPtr, ObjectArraySize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtGetObjectArrayProperty(ObjectArray: IntPtr, PropertyId: UInt32, ArrayIndex: UInt32, Flags: UInt32, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT_head), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtGetQueryInfo(QueryOrSubscription: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_QUERY_PROPERTY_ID, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT_head), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtCreateBookmark(BookmarkXml: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtUpdateBookmark(Bookmark: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Event: win32more.Windows.Win32.System.EventLog.EVT_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtGetEventInfo(Event: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_EVENT_PROPERTY_ID, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT_head), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ClearEventLogA(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, lpBackupFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ClearEventLogW(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, lpBackupFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def BackupEventLogA(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, lpBackupFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def BackupEventLogW(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, lpBackupFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CloseEventLog(hEventLog: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DeregisterEventSource(hEventLog: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def NotifyChangeEventLog(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetNumberOfEventLogRecords(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, NumberOfRecords: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetOldestEventLogRecord(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, OldestRecord: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OpenEventLogA(lpUNCServerName: win32more.Windows.Win32.Foundation.PSTR, lpSourceName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ADVAPI32.dll')
def OpenEventLogW(lpUNCServerName: win32more.Windows.Win32.Foundation.PWSTR, lpSourceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ADVAPI32.dll')
def RegisterEventSourceA(lpUNCServerName: win32more.Windows.Win32.Foundation.PSTR, lpSourceName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ADVAPI32.dll')
def RegisterEventSourceW(lpUNCServerName: win32more.Windows.Win32.Foundation.PWSTR, lpSourceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ADVAPI32.dll')
def OpenBackupEventLogA(lpUNCServerName: win32more.Windows.Win32.Foundation.PSTR, lpFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ADVAPI32.dll')
def OpenBackupEventLogW(lpUNCServerName: win32more.Windows.Win32.Foundation.PWSTR, lpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ADVAPI32.dll')
def ReadEventLogA(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, dwReadFlags: win32more.Windows.Win32.System.EventLog.READ_EVENT_LOG_READ_FLAGS, dwRecordOffset: UInt32, lpBuffer: VoidPtr, nNumberOfBytesToRead: UInt32, pnBytesRead: POINTER(UInt32), pnMinNumberOfBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ReadEventLogW(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, dwReadFlags: win32more.Windows.Win32.System.EventLog.READ_EVENT_LOG_READ_FLAGS, dwRecordOffset: UInt32, lpBuffer: VoidPtr, nNumberOfBytesToRead: UInt32, pnBytesRead: POINTER(UInt32), pnMinNumberOfBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ReportEventA(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, wType: win32more.Windows.Win32.System.EventLog.REPORT_EVENT_TYPE, wCategory: UInt16, dwEventID: UInt32, lpUserSid: win32more.Windows.Win32.Foundation.PSID, wNumStrings: UInt16, dwDataSize: UInt32, lpStrings: POINTER(win32more.Windows.Win32.Foundation.PSTR), lpRawData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ReportEventW(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, wType: win32more.Windows.Win32.System.EventLog.REPORT_EVENT_TYPE, wCategory: UInt16, dwEventID: UInt32, lpUserSid: win32more.Windows.Win32.Foundation.PSID, wNumStrings: UInt16, dwDataSize: UInt32, lpStrings: POINTER(win32more.Windows.Win32.Foundation.PWSTR), lpRawData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetEventLogInformation(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, dwInfoLevel: UInt32, lpBuffer: VoidPtr, cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class EVENTLOGRECORD(EasyCastStructure):
    Length: UInt32
    Reserved: UInt32
    RecordNumber: UInt32
    TimeGenerated: UInt32
    TimeWritten: UInt32
    EventID: UInt32
    EventType: win32more.Windows.Win32.System.EventLog.REPORT_EVENT_TYPE
    NumStrings: UInt16
    EventCategory: UInt16
    ReservedFlags: UInt16
    ClosingRecordNumber: UInt32
    StringOffset: UInt32
    UserSidLength: UInt32
    UserSidOffset: UInt32
    DataLength: UInt32
    DataOffset: UInt32
class EVENTLOG_FULL_INFORMATION(EasyCastStructure):
    dwFull: UInt32
class EVENTSFORLOGFILE(EasyCastStructure):
    ulSize: UInt32
    szLogicalLogFile: Char * 256
    ulNumRecords: UInt32
    pEventLogRecords: win32more.Windows.Win32.System.EventLog.EVENTLOGRECORD * 1
EVT_CHANNEL_CLOCK_TYPE = Int32
EVT_CHANNEL_CLOCK_TYPE_EvtChannelClockTypeSystemTime: EVT_CHANNEL_CLOCK_TYPE = 0
EVT_CHANNEL_CLOCK_TYPE_EvtChannelClockTypeQPC: EVT_CHANNEL_CLOCK_TYPE = 1
EVT_CHANNEL_CONFIG_PROPERTY_ID = Int32
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigEnabled: EVT_CHANNEL_CONFIG_PROPERTY_ID = 0
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigIsolation: EVT_CHANNEL_CONFIG_PROPERTY_ID = 1
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigType: EVT_CHANNEL_CONFIG_PROPERTY_ID = 2
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigOwningPublisher: EVT_CHANNEL_CONFIG_PROPERTY_ID = 3
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigClassicEventlog: EVT_CHANNEL_CONFIG_PROPERTY_ID = 4
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigAccess: EVT_CHANNEL_CONFIG_PROPERTY_ID = 5
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigRetention: EVT_CHANNEL_CONFIG_PROPERTY_ID = 6
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigAutoBackup: EVT_CHANNEL_CONFIG_PROPERTY_ID = 7
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigMaxSize: EVT_CHANNEL_CONFIG_PROPERTY_ID = 8
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigLogFilePath: EVT_CHANNEL_CONFIG_PROPERTY_ID = 9
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigLevel: EVT_CHANNEL_CONFIG_PROPERTY_ID = 10
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigKeywords: EVT_CHANNEL_CONFIG_PROPERTY_ID = 11
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigControlGuid: EVT_CHANNEL_CONFIG_PROPERTY_ID = 12
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigBufferSize: EVT_CHANNEL_CONFIG_PROPERTY_ID = 13
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigMinBuffers: EVT_CHANNEL_CONFIG_PROPERTY_ID = 14
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigMaxBuffers: EVT_CHANNEL_CONFIG_PROPERTY_ID = 15
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigLatency: EVT_CHANNEL_CONFIG_PROPERTY_ID = 16
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigClockType: EVT_CHANNEL_CONFIG_PROPERTY_ID = 17
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigSidType: EVT_CHANNEL_CONFIG_PROPERTY_ID = 18
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublisherList: EVT_CHANNEL_CONFIG_PROPERTY_ID = 19
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigFileMax: EVT_CHANNEL_CONFIG_PROPERTY_ID = 20
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigPropertyIdEND: EVT_CHANNEL_CONFIG_PROPERTY_ID = 21
EVT_CHANNEL_ISOLATION_TYPE = Int32
EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeApplication: EVT_CHANNEL_ISOLATION_TYPE = 0
EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeSystem: EVT_CHANNEL_ISOLATION_TYPE = 1
EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeCustom: EVT_CHANNEL_ISOLATION_TYPE = 2
EVT_CHANNEL_REFERENCE_FLAGS = UInt32
EVT_CHANNEL_REFERENCE_FLAGS_EvtChannelReferenceImported: EVT_CHANNEL_REFERENCE_FLAGS = 1
EVT_CHANNEL_SID_TYPE = Int32
EVT_CHANNEL_SID_TYPE_EvtChannelSidTypeNone: EVT_CHANNEL_SID_TYPE = 0
EVT_CHANNEL_SID_TYPE_EvtChannelSidTypePublishing: EVT_CHANNEL_SID_TYPE = 1
EVT_CHANNEL_TYPE = Int32
EVT_CHANNEL_TYPE_EvtChannelTypeAdmin: EVT_CHANNEL_TYPE = 0
EVT_CHANNEL_TYPE_EvtChannelTypeOperational: EVT_CHANNEL_TYPE = 1
EVT_CHANNEL_TYPE_EvtChannelTypeAnalytic: EVT_CHANNEL_TYPE = 2
EVT_CHANNEL_TYPE_EvtChannelTypeDebug: EVT_CHANNEL_TYPE = 3
EVT_EVENT_METADATA_PROPERTY_ID = Int32
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventID: EVT_EVENT_METADATA_PROPERTY_ID = 0
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventVersion: EVT_EVENT_METADATA_PROPERTY_ID = 1
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventChannel: EVT_EVENT_METADATA_PROPERTY_ID = 2
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventLevel: EVT_EVENT_METADATA_PROPERTY_ID = 3
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventOpcode: EVT_EVENT_METADATA_PROPERTY_ID = 4
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventTask: EVT_EVENT_METADATA_PROPERTY_ID = 5
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventKeyword: EVT_EVENT_METADATA_PROPERTY_ID = 6
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventMessageID: EVT_EVENT_METADATA_PROPERTY_ID = 7
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventTemplate: EVT_EVENT_METADATA_PROPERTY_ID = 8
EVT_EVENT_METADATA_PROPERTY_ID_EvtEventMetadataPropertyIdEND: EVT_EVENT_METADATA_PROPERTY_ID = 9
EVT_EVENT_PROPERTY_ID = Int32
EVT_EVENT_PROPERTY_ID_EvtEventQueryIDs: EVT_EVENT_PROPERTY_ID = 0
EVT_EVENT_PROPERTY_ID_EvtEventPath: EVT_EVENT_PROPERTY_ID = 1
EVT_EVENT_PROPERTY_ID_EvtEventPropertyIdEND: EVT_EVENT_PROPERTY_ID = 2
EVT_EXPORTLOG_FLAGS = UInt32
EVT_EXPORTLOG_FLAGS_EvtExportLogChannelPath: EVT_EXPORTLOG_FLAGS = 1
EVT_EXPORTLOG_FLAGS_EvtExportLogFilePath: EVT_EXPORTLOG_FLAGS = 2
EVT_EXPORTLOG_FLAGS_EvtExportLogTolerateQueryErrors: EVT_EXPORTLOG_FLAGS = 4096
EVT_EXPORTLOG_FLAGS_EvtExportLogOverwrite: EVT_EXPORTLOG_FLAGS = 8192
EVT_FORMAT_MESSAGE_FLAGS = UInt32
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageEvent: EVT_FORMAT_MESSAGE_FLAGS = 1
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageLevel: EVT_FORMAT_MESSAGE_FLAGS = 2
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageTask: EVT_FORMAT_MESSAGE_FLAGS = 3
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageOpcode: EVT_FORMAT_MESSAGE_FLAGS = 4
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageKeyword: EVT_FORMAT_MESSAGE_FLAGS = 5
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageChannel: EVT_FORMAT_MESSAGE_FLAGS = 6
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageProvider: EVT_FORMAT_MESSAGE_FLAGS = 7
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageId: EVT_FORMAT_MESSAGE_FLAGS = 8
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageXml: EVT_FORMAT_MESSAGE_FLAGS = 9
EVT_HANDLE = IntPtr
EVT_LOGIN_CLASS = Int32
EVT_LOGIN_CLASS_EvtRpcLogin: EVT_LOGIN_CLASS = 1
EVT_LOG_PROPERTY_ID = Int32
EVT_LOG_PROPERTY_ID_EvtLogCreationTime: EVT_LOG_PROPERTY_ID = 0
EVT_LOG_PROPERTY_ID_EvtLogLastAccessTime: EVT_LOG_PROPERTY_ID = 1
EVT_LOG_PROPERTY_ID_EvtLogLastWriteTime: EVT_LOG_PROPERTY_ID = 2
EVT_LOG_PROPERTY_ID_EvtLogFileSize: EVT_LOG_PROPERTY_ID = 3
EVT_LOG_PROPERTY_ID_EvtLogAttributes: EVT_LOG_PROPERTY_ID = 4
EVT_LOG_PROPERTY_ID_EvtLogNumberOfLogRecords: EVT_LOG_PROPERTY_ID = 5
EVT_LOG_PROPERTY_ID_EvtLogOldestRecordNumber: EVT_LOG_PROPERTY_ID = 6
EVT_LOG_PROPERTY_ID_EvtLogFull: EVT_LOG_PROPERTY_ID = 7
EVT_OPEN_LOG_FLAGS = UInt32
EVT_OPEN_LOG_FLAGS_EvtOpenChannelPath: EVT_OPEN_LOG_FLAGS = 1
EVT_OPEN_LOG_FLAGS_EvtOpenFilePath: EVT_OPEN_LOG_FLAGS = 2
EVT_PUBLISHER_METADATA_PROPERTY_ID = Int32
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPublisherGuid: EVT_PUBLISHER_METADATA_PROPERTY_ID = 0
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataResourceFilePath: EVT_PUBLISHER_METADATA_PROPERTY_ID = 1
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataParameterFilePath: EVT_PUBLISHER_METADATA_PROPERTY_ID = 2
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataMessageFilePath: EVT_PUBLISHER_METADATA_PROPERTY_ID = 3
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataHelpLink: EVT_PUBLISHER_METADATA_PROPERTY_ID = 4
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPublisherMessageID: EVT_PUBLISHER_METADATA_PROPERTY_ID = 5
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferences: EVT_PUBLISHER_METADATA_PROPERTY_ID = 6
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferencePath: EVT_PUBLISHER_METADATA_PROPERTY_ID = 7
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceIndex: EVT_PUBLISHER_METADATA_PROPERTY_ID = 8
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceID: EVT_PUBLISHER_METADATA_PROPERTY_ID = 9
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceFlags: EVT_PUBLISHER_METADATA_PROPERTY_ID = 10
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceMessageID: EVT_PUBLISHER_METADATA_PROPERTY_ID = 11
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevels: EVT_PUBLISHER_METADATA_PROPERTY_ID = 12
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelName: EVT_PUBLISHER_METADATA_PROPERTY_ID = 13
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelValue: EVT_PUBLISHER_METADATA_PROPERTY_ID = 14
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelMessageID: EVT_PUBLISHER_METADATA_PROPERTY_ID = 15
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTasks: EVT_PUBLISHER_METADATA_PROPERTY_ID = 16
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskName: EVT_PUBLISHER_METADATA_PROPERTY_ID = 17
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskEventGuid: EVT_PUBLISHER_METADATA_PROPERTY_ID = 18
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskValue: EVT_PUBLISHER_METADATA_PROPERTY_ID = 19
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskMessageID: EVT_PUBLISHER_METADATA_PROPERTY_ID = 20
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodes: EVT_PUBLISHER_METADATA_PROPERTY_ID = 21
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeName: EVT_PUBLISHER_METADATA_PROPERTY_ID = 22
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeValue: EVT_PUBLISHER_METADATA_PROPERTY_ID = 23
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeMessageID: EVT_PUBLISHER_METADATA_PROPERTY_ID = 24
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywords: EVT_PUBLISHER_METADATA_PROPERTY_ID = 25
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordName: EVT_PUBLISHER_METADATA_PROPERTY_ID = 26
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordValue: EVT_PUBLISHER_METADATA_PROPERTY_ID = 27
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordMessageID: EVT_PUBLISHER_METADATA_PROPERTY_ID = 28
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPropertyIdEND: EVT_PUBLISHER_METADATA_PROPERTY_ID = 29
EVT_QUERY_FLAGS = UInt32
EVT_QUERY_FLAGS_EvtQueryChannelPath: EVT_QUERY_FLAGS = 1
EVT_QUERY_FLAGS_EvtQueryFilePath: EVT_QUERY_FLAGS = 2
EVT_QUERY_FLAGS_EvtQueryForwardDirection: EVT_QUERY_FLAGS = 256
EVT_QUERY_FLAGS_EvtQueryReverseDirection: EVT_QUERY_FLAGS = 512
EVT_QUERY_FLAGS_EvtQueryTolerateQueryErrors: EVT_QUERY_FLAGS = 4096
EVT_QUERY_PROPERTY_ID = Int32
EVT_QUERY_PROPERTY_ID_EvtQueryNames: EVT_QUERY_PROPERTY_ID = 0
EVT_QUERY_PROPERTY_ID_EvtQueryStatuses: EVT_QUERY_PROPERTY_ID = 1
EVT_QUERY_PROPERTY_ID_EvtQueryPropertyIdEND: EVT_QUERY_PROPERTY_ID = 2
EVT_RENDER_CONTEXT_FLAGS = UInt32
EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextValues: EVT_RENDER_CONTEXT_FLAGS = 0
EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextSystem: EVT_RENDER_CONTEXT_FLAGS = 1
EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextUser: EVT_RENDER_CONTEXT_FLAGS = 2
EVT_RENDER_FLAGS = UInt32
EVT_RENDER_FLAGS_EvtRenderEventValues: EVT_RENDER_FLAGS = 0
EVT_RENDER_FLAGS_EvtRenderEventXml: EVT_RENDER_FLAGS = 1
EVT_RENDER_FLAGS_EvtRenderBookmark: EVT_RENDER_FLAGS = 2
class EVT_RPC_LOGIN(EasyCastStructure):
    Server: win32more.Windows.Win32.Foundation.PWSTR
    User: win32more.Windows.Win32.Foundation.PWSTR
    Domain: win32more.Windows.Win32.Foundation.PWSTR
    Password: win32more.Windows.Win32.Foundation.PWSTR
    Flags: UInt32
EVT_RPC_LOGIN_FLAGS = UInt32
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthDefault: EVT_RPC_LOGIN_FLAGS = 0
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthNegotiate: EVT_RPC_LOGIN_FLAGS = 1
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthKerberos: EVT_RPC_LOGIN_FLAGS = 2
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthNTLM: EVT_RPC_LOGIN_FLAGS = 3
EVT_SEEK_FLAGS = UInt32
EVT_SEEK_FLAGS_EvtSeekRelativeToFirst: EVT_SEEK_FLAGS = 1
EVT_SEEK_FLAGS_EvtSeekRelativeToLast: EVT_SEEK_FLAGS = 2
EVT_SEEK_FLAGS_EvtSeekRelativeToCurrent: EVT_SEEK_FLAGS = 3
EVT_SEEK_FLAGS_EvtSeekRelativeToBookmark: EVT_SEEK_FLAGS = 4
EVT_SEEK_FLAGS_EvtSeekOriginMask: EVT_SEEK_FLAGS = 7
EVT_SEEK_FLAGS_EvtSeekStrict: EVT_SEEK_FLAGS = 65536
@winfunctype_pointer
def EVT_SUBSCRIBE_CALLBACK(Action: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_NOTIFY_ACTION, UserContext: VoidPtr, Event: win32more.Windows.Win32.System.EventLog.EVT_HANDLE) -> UInt32: ...
EVT_SUBSCRIBE_FLAGS = UInt32
EVT_SUBSCRIBE_FLAGS_EvtSubscribeToFutureEvents: EVT_SUBSCRIBE_FLAGS = 1
EVT_SUBSCRIBE_FLAGS_EvtSubscribeStartAtOldestRecord: EVT_SUBSCRIBE_FLAGS = 2
EVT_SUBSCRIBE_FLAGS_EvtSubscribeStartAfterBookmark: EVT_SUBSCRIBE_FLAGS = 3
EVT_SUBSCRIBE_FLAGS_EvtSubscribeOriginMask: EVT_SUBSCRIBE_FLAGS = 3
EVT_SUBSCRIBE_FLAGS_EvtSubscribeTolerateQueryErrors: EVT_SUBSCRIBE_FLAGS = 4096
EVT_SUBSCRIBE_FLAGS_EvtSubscribeStrict: EVT_SUBSCRIBE_FLAGS = 65536
EVT_SUBSCRIBE_NOTIFY_ACTION = Int32
EVT_SUBSCRIBE_NOTIFY_ACTION_EvtSubscribeActionError: EVT_SUBSCRIBE_NOTIFY_ACTION = 0
EVT_SUBSCRIBE_NOTIFY_ACTION_EvtSubscribeActionDeliver: EVT_SUBSCRIBE_NOTIFY_ACTION = 1
EVT_SYSTEM_PROPERTY_ID = Int32
EVT_SYSTEM_PROPERTY_ID_EvtSystemProviderName: EVT_SYSTEM_PROPERTY_ID = 0
EVT_SYSTEM_PROPERTY_ID_EvtSystemProviderGuid: EVT_SYSTEM_PROPERTY_ID = 1
EVT_SYSTEM_PROPERTY_ID_EvtSystemEventID: EVT_SYSTEM_PROPERTY_ID = 2
EVT_SYSTEM_PROPERTY_ID_EvtSystemQualifiers: EVT_SYSTEM_PROPERTY_ID = 3
EVT_SYSTEM_PROPERTY_ID_EvtSystemLevel: EVT_SYSTEM_PROPERTY_ID = 4
EVT_SYSTEM_PROPERTY_ID_EvtSystemTask: EVT_SYSTEM_PROPERTY_ID = 5
EVT_SYSTEM_PROPERTY_ID_EvtSystemOpcode: EVT_SYSTEM_PROPERTY_ID = 6
EVT_SYSTEM_PROPERTY_ID_EvtSystemKeywords: EVT_SYSTEM_PROPERTY_ID = 7
EVT_SYSTEM_PROPERTY_ID_EvtSystemTimeCreated: EVT_SYSTEM_PROPERTY_ID = 8
EVT_SYSTEM_PROPERTY_ID_EvtSystemEventRecordId: EVT_SYSTEM_PROPERTY_ID = 9
EVT_SYSTEM_PROPERTY_ID_EvtSystemActivityID: EVT_SYSTEM_PROPERTY_ID = 10
EVT_SYSTEM_PROPERTY_ID_EvtSystemRelatedActivityID: EVT_SYSTEM_PROPERTY_ID = 11
EVT_SYSTEM_PROPERTY_ID_EvtSystemProcessID: EVT_SYSTEM_PROPERTY_ID = 12
EVT_SYSTEM_PROPERTY_ID_EvtSystemThreadID: EVT_SYSTEM_PROPERTY_ID = 13
EVT_SYSTEM_PROPERTY_ID_EvtSystemChannel: EVT_SYSTEM_PROPERTY_ID = 14
EVT_SYSTEM_PROPERTY_ID_EvtSystemComputer: EVT_SYSTEM_PROPERTY_ID = 15
EVT_SYSTEM_PROPERTY_ID_EvtSystemUserID: EVT_SYSTEM_PROPERTY_ID = 16
EVT_SYSTEM_PROPERTY_ID_EvtSystemVersion: EVT_SYSTEM_PROPERTY_ID = 17
EVT_SYSTEM_PROPERTY_ID_EvtSystemPropertyIdEND: EVT_SYSTEM_PROPERTY_ID = 18
class EVT_VARIANT(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    Count: UInt32
    Type: UInt32
    class _Anonymous_e__Union(EasyCastUnion):
        BooleanVal: win32more.Windows.Win32.Foundation.BOOL
        SByteVal: SByte
        Int16Val: Int16
        Int32Val: Int32
        Int64Val: Int64
        ByteVal: Byte
        UInt16Val: UInt16
        UInt32Val: UInt32
        UInt64Val: UInt64
        SingleVal: Single
        DoubleVal: Double
        FileTimeVal: UInt64
        SysTimeVal: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME_head)
        GuidVal: POINTER(Guid)
        StringVal: win32more.Windows.Win32.Foundation.PWSTR
        AnsiStringVal: win32more.Windows.Win32.Foundation.PSTR
        BinaryVal: POINTER(Byte)
        SidVal: win32more.Windows.Win32.Foundation.PSID
        SizeTVal: UIntPtr
        BooleanArr: POINTER(win32more.Windows.Win32.Foundation.BOOL)
        SByteArr: POINTER(SByte)
        Int16Arr: POINTER(Int16)
        Int32Arr: POINTER(Int32)
        Int64Arr: POINTER(Int64)
        ByteArr: POINTER(Byte)
        UInt16Arr: POINTER(UInt16)
        UInt32Arr: POINTER(UInt32)
        UInt64Arr: POINTER(UInt64)
        SingleArr: POINTER(Single)
        DoubleArr: POINTER(Double)
        FileTimeArr: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)
        SysTimeArr: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME_head)
        GuidArr: POINTER(Guid)
        StringArr: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
        AnsiStringArr: POINTER(win32more.Windows.Win32.Foundation.PSTR)
        SidArr: POINTER(win32more.Windows.Win32.Foundation.PSID)
        SizeTArr: POINTER(UIntPtr)
        EvtHandleVal: win32more.Windows.Win32.System.EventLog.EVT_HANDLE
        XmlVal: win32more.Windows.Win32.Foundation.PWSTR
        XmlValArr: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
EVT_VARIANT_TYPE = Int32
EVT_VARIANT_TYPE_EvtVarTypeNull: EVT_VARIANT_TYPE = 0
EVT_VARIANT_TYPE_EvtVarTypeString: EVT_VARIANT_TYPE = 1
EVT_VARIANT_TYPE_EvtVarTypeAnsiString: EVT_VARIANT_TYPE = 2
EVT_VARIANT_TYPE_EvtVarTypeSByte: EVT_VARIANT_TYPE = 3
EVT_VARIANT_TYPE_EvtVarTypeByte: EVT_VARIANT_TYPE = 4
EVT_VARIANT_TYPE_EvtVarTypeInt16: EVT_VARIANT_TYPE = 5
EVT_VARIANT_TYPE_EvtVarTypeUInt16: EVT_VARIANT_TYPE = 6
EVT_VARIANT_TYPE_EvtVarTypeInt32: EVT_VARIANT_TYPE = 7
EVT_VARIANT_TYPE_EvtVarTypeUInt32: EVT_VARIANT_TYPE = 8
EVT_VARIANT_TYPE_EvtVarTypeInt64: EVT_VARIANT_TYPE = 9
EVT_VARIANT_TYPE_EvtVarTypeUInt64: EVT_VARIANT_TYPE = 10
EVT_VARIANT_TYPE_EvtVarTypeSingle: EVT_VARIANT_TYPE = 11
EVT_VARIANT_TYPE_EvtVarTypeDouble: EVT_VARIANT_TYPE = 12
EVT_VARIANT_TYPE_EvtVarTypeBoolean: EVT_VARIANT_TYPE = 13
EVT_VARIANT_TYPE_EvtVarTypeBinary: EVT_VARIANT_TYPE = 14
EVT_VARIANT_TYPE_EvtVarTypeGuid: EVT_VARIANT_TYPE = 15
EVT_VARIANT_TYPE_EvtVarTypeSizeT: EVT_VARIANT_TYPE = 16
EVT_VARIANT_TYPE_EvtVarTypeFileTime: EVT_VARIANT_TYPE = 17
EVT_VARIANT_TYPE_EvtVarTypeSysTime: EVT_VARIANT_TYPE = 18
EVT_VARIANT_TYPE_EvtVarTypeSid: EVT_VARIANT_TYPE = 19
EVT_VARIANT_TYPE_EvtVarTypeHexInt32: EVT_VARIANT_TYPE = 20
EVT_VARIANT_TYPE_EvtVarTypeHexInt64: EVT_VARIANT_TYPE = 21
EVT_VARIANT_TYPE_EvtVarTypeEvtHandle: EVT_VARIANT_TYPE = 32
EVT_VARIANT_TYPE_EvtVarTypeEvtXml: EVT_VARIANT_TYPE = 35
READ_EVENT_LOG_READ_FLAGS = UInt32
EVENTLOG_SEEK_READ: READ_EVENT_LOG_READ_FLAGS = 2
EVENTLOG_SEQUENTIAL_READ: READ_EVENT_LOG_READ_FLAGS = 1
REPORT_EVENT_TYPE = UInt16
EVENTLOG_SUCCESS: REPORT_EVENT_TYPE = 0
EVENTLOG_AUDIT_FAILURE: REPORT_EVENT_TYPE = 16
EVENTLOG_AUDIT_SUCCESS: REPORT_EVENT_TYPE = 8
EVENTLOG_ERROR_TYPE: REPORT_EVENT_TYPE = 1
EVENTLOG_INFORMATION_TYPE: REPORT_EVENT_TYPE = 4
EVENTLOG_WARNING_TYPE: REPORT_EVENT_TYPE = 2
make_head(_module, 'EVENTLOGRECORD')
make_head(_module, 'EVENTLOG_FULL_INFORMATION')
make_head(_module, 'EVENTSFORLOGFILE')
make_head(_module, 'EVT_RPC_LOGIN')
make_head(_module, 'EVT_SUBSCRIBE_CALLBACK')
make_head(_module, 'EVT_VARIANT')
