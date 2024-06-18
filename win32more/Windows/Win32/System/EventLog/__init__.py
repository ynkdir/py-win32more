from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.EventLog
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
def EvtFormatMessage(PublisherMetadata: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Event: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, MessageId: UInt32, ValueCount: UInt32, Values: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT), Flags: UInt32, BufferSize: UInt32, Buffer: win32more.Windows.Win32.Foundation.PWSTR, BufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtOpenLog(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Path: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtGetLogInfo(Log: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
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
def EvtSetChannelConfigProperty(ChannelConfig: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID, Flags: UInt32, PropertyValue: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtGetChannelConfigProperty(ChannelConfig: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID, Flags: UInt32, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtOpenPublisherEnum(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtNextPublisherId(PublisherEnum: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PublisherIdBufferSize: UInt32, PublisherIdBuffer: win32more.Windows.Win32.Foundation.PWSTR, PublisherIdBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtOpenPublisherMetadata(Session: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PublisherId: win32more.Windows.Win32.Foundation.PWSTR, LogFilePath: win32more.Windows.Win32.Foundation.PWSTR, Locale: UInt32, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtGetPublisherMetadataProperty(PublisherMetadata: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID, Flags: UInt32, PublisherMetadataPropertyBufferSize: UInt32, PublisherMetadataPropertyBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT), PublisherMetadataPropertyBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtOpenEventMetadataEnum(PublisherMetadata: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtNextEventMetadata(EventMetadataEnum: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Flags: UInt32) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtGetEventMetadataProperty(EventMetadata: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID, Flags: UInt32, EventMetadataPropertyBufferSize: UInt32, EventMetadataPropertyBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT), EventMetadataPropertyBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtGetObjectArraySize(ObjectArray: IntPtr, ObjectArraySize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtGetObjectArrayProperty(ObjectArray: IntPtr, PropertyId: UInt32, ArrayIndex: UInt32, Flags: UInt32, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtGetQueryInfo(QueryOrSubscription: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_QUERY_PROPERTY_ID, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtCreateBookmark(BookmarkXml: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.EventLog.EVT_HANDLE: ...
@winfunctype('wevtapi.dll')
def EvtUpdateBookmark(Bookmark: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, Event: win32more.Windows.Win32.System.EventLog.EVT_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wevtapi.dll')
def EvtGetEventInfo(Event: win32more.Windows.Win32.System.EventLog.EVT_HANDLE, PropertyId: win32more.Windows.Win32.System.EventLog.EVT_EVENT_PROPERTY_ID, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventLog.EVT_VARIANT), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ClearEventLogA(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, lpBackupFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ClearEventLogW(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, lpBackupFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
ClearEventLog = UnicodeAlias('ClearEventLogW')
@winfunctype('ADVAPI32.dll')
def BackupEventLogA(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, lpBackupFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def BackupEventLogW(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, lpBackupFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
BackupEventLog = UnicodeAlias('BackupEventLogW')
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
OpenEventLog = UnicodeAlias('OpenEventLogW')
@winfunctype('ADVAPI32.dll')
def RegisterEventSourceA(lpUNCServerName: win32more.Windows.Win32.Foundation.PSTR, lpSourceName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ADVAPI32.dll')
def RegisterEventSourceW(lpUNCServerName: win32more.Windows.Win32.Foundation.PWSTR, lpSourceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
RegisterEventSource = UnicodeAlias('RegisterEventSourceW')
@winfunctype('ADVAPI32.dll')
def OpenBackupEventLogA(lpUNCServerName: win32more.Windows.Win32.Foundation.PSTR, lpFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ADVAPI32.dll')
def OpenBackupEventLogW(lpUNCServerName: win32more.Windows.Win32.Foundation.PWSTR, lpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
OpenBackupEventLog = UnicodeAlias('OpenBackupEventLogW')
@winfunctype('ADVAPI32.dll')
def ReadEventLogA(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, dwReadFlags: win32more.Windows.Win32.System.EventLog.READ_EVENT_LOG_READ_FLAGS, dwRecordOffset: UInt32, lpBuffer: VoidPtr, nNumberOfBytesToRead: UInt32, pnBytesRead: POINTER(UInt32), pnMinNumberOfBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ReadEventLogW(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, dwReadFlags: win32more.Windows.Win32.System.EventLog.READ_EVENT_LOG_READ_FLAGS, dwRecordOffset: UInt32, lpBuffer: VoidPtr, nNumberOfBytesToRead: UInt32, pnBytesRead: POINTER(UInt32), pnMinNumberOfBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ReadEventLog = UnicodeAlias('ReadEventLogW')
@winfunctype('ADVAPI32.dll')
def ReportEventA(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, wType: win32more.Windows.Win32.System.EventLog.REPORT_EVENT_TYPE, wCategory: UInt16, dwEventID: UInt32, lpUserSid: win32more.Windows.Win32.Security.PSID, wNumStrings: UInt16, dwDataSize: UInt32, lpStrings: POINTER(win32more.Windows.Win32.Foundation.PSTR), lpRawData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ReportEventW(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, wType: win32more.Windows.Win32.System.EventLog.REPORT_EVENT_TYPE, wCategory: UInt16, dwEventID: UInt32, lpUserSid: win32more.Windows.Win32.Security.PSID, wNumStrings: UInt16, dwDataSize: UInt32, lpStrings: POINTER(win32more.Windows.Win32.Foundation.PWSTR), lpRawData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
ReportEvent = UnicodeAlias('ReportEventW')
@winfunctype('ADVAPI32.dll')
def GetEventLogInformation(hEventLog: win32more.Windows.Win32.Foundation.HANDLE, dwInfoLevel: UInt32, lpBuffer: VoidPtr, cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class EVENTLOGRECORD(Structure):
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
class EVENTLOG_FULL_INFORMATION(Structure):
    dwFull: UInt32
class EVENTSFORLOGFILE(Structure):
    ulSize: UInt32
    szLogicalLogFile: Char * 256
    ulNumRecords: UInt32
    pEventLogRecords: win32more.Windows.Win32.System.EventLog.EVENTLOGRECORD * 1
EVT_CHANNEL_CLOCK_TYPE = Int32
EvtChannelClockTypeSystemTime: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CLOCK_TYPE = 0
EvtChannelClockTypeQPC: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CLOCK_TYPE = 1
EVT_CHANNEL_CONFIG_PROPERTY_ID = Int32
EvtChannelConfigEnabled: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 0
EvtChannelConfigIsolation: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 1
EvtChannelConfigType: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 2
EvtChannelConfigOwningPublisher: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 3
EvtChannelConfigClassicEventlog: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 4
EvtChannelConfigAccess: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 5
EvtChannelLoggingConfigRetention: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 6
EvtChannelLoggingConfigAutoBackup: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 7
EvtChannelLoggingConfigMaxSize: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 8
EvtChannelLoggingConfigLogFilePath: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 9
EvtChannelPublishingConfigLevel: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 10
EvtChannelPublishingConfigKeywords: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 11
EvtChannelPublishingConfigControlGuid: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 12
EvtChannelPublishingConfigBufferSize: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 13
EvtChannelPublishingConfigMinBuffers: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 14
EvtChannelPublishingConfigMaxBuffers: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 15
EvtChannelPublishingConfigLatency: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 16
EvtChannelPublishingConfigClockType: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 17
EvtChannelPublishingConfigSidType: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 18
EvtChannelPublisherList: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 19
EvtChannelPublishingConfigFileMax: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 20
EvtChannelConfigPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 21
EVT_CHANNEL_ISOLATION_TYPE = Int32
EvtChannelIsolationTypeApplication: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_ISOLATION_TYPE = 0
EvtChannelIsolationTypeSystem: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_ISOLATION_TYPE = 1
EvtChannelIsolationTypeCustom: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_ISOLATION_TYPE = 2
EVT_CHANNEL_REFERENCE_FLAGS = UInt32
EvtChannelReferenceImported: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_REFERENCE_FLAGS = 1
EVT_CHANNEL_SID_TYPE = Int32
EvtChannelSidTypeNone: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_SID_TYPE = 0
EvtChannelSidTypePublishing: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_SID_TYPE = 1
EVT_CHANNEL_TYPE = Int32
EvtChannelTypeAdmin: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_TYPE = 0
EvtChannelTypeOperational: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_TYPE = 1
EvtChannelTypeAnalytic: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_TYPE = 2
EvtChannelTypeDebug: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_TYPE = 3
EVT_EVENT_METADATA_PROPERTY_ID = Int32
EventMetadataEventID: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 0
EventMetadataEventVersion: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 1
EventMetadataEventChannel: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 2
EventMetadataEventLevel: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 3
EventMetadataEventOpcode: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 4
EventMetadataEventTask: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 5
EventMetadataEventKeyword: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 6
EventMetadataEventMessageID: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 7
EventMetadataEventTemplate: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 8
EvtEventMetadataPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 9
EVT_EVENT_PROPERTY_ID = Int32
EvtEventQueryIDs: win32more.Windows.Win32.System.EventLog.EVT_EVENT_PROPERTY_ID = 0
EvtEventPath: win32more.Windows.Win32.System.EventLog.EVT_EVENT_PROPERTY_ID = 1
EvtEventPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_EVENT_PROPERTY_ID = 2
EVT_EXPORTLOG_FLAGS = UInt32
EvtExportLogChannelPath: win32more.Windows.Win32.System.EventLog.EVT_EXPORTLOG_FLAGS = 1
EvtExportLogFilePath: win32more.Windows.Win32.System.EventLog.EVT_EXPORTLOG_FLAGS = 2
EvtExportLogTolerateQueryErrors: win32more.Windows.Win32.System.EventLog.EVT_EXPORTLOG_FLAGS = 4096
EvtExportLogOverwrite: win32more.Windows.Win32.System.EventLog.EVT_EXPORTLOG_FLAGS = 8192
EVT_FORMAT_MESSAGE_FLAGS = UInt32
EvtFormatMessageEvent: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 1
EvtFormatMessageLevel: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 2
EvtFormatMessageTask: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 3
EvtFormatMessageOpcode: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 4
EvtFormatMessageKeyword: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 5
EvtFormatMessageChannel: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 6
EvtFormatMessageProvider: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 7
EvtFormatMessageId: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 8
EvtFormatMessageXml: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 9
EVT_HANDLE = IntPtr
EVT_LOGIN_CLASS = Int32
EvtRpcLogin: win32more.Windows.Win32.System.EventLog.EVT_LOGIN_CLASS = 1
EVT_LOG_PROPERTY_ID = Int32
EvtLogCreationTime: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 0
EvtLogLastAccessTime: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 1
EvtLogLastWriteTime: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 2
EvtLogFileSize: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 3
EvtLogAttributes: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 4
EvtLogNumberOfLogRecords: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 5
EvtLogOldestRecordNumber: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 6
EvtLogFull: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 7
EVT_OPEN_LOG_FLAGS = UInt32
EvtOpenChannelPath: win32more.Windows.Win32.System.EventLog.EVT_OPEN_LOG_FLAGS = 1
EvtOpenFilePath: win32more.Windows.Win32.System.EventLog.EVT_OPEN_LOG_FLAGS = 2
EVT_PUBLISHER_METADATA_PROPERTY_ID = Int32
EvtPublisherMetadataPublisherGuid: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 0
EvtPublisherMetadataResourceFilePath: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 1
EvtPublisherMetadataParameterFilePath: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 2
EvtPublisherMetadataMessageFilePath: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 3
EvtPublisherMetadataHelpLink: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 4
EvtPublisherMetadataPublisherMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 5
EvtPublisherMetadataChannelReferences: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 6
EvtPublisherMetadataChannelReferencePath: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 7
EvtPublisherMetadataChannelReferenceIndex: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 8
EvtPublisherMetadataChannelReferenceID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 9
EvtPublisherMetadataChannelReferenceFlags: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 10
EvtPublisherMetadataChannelReferenceMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 11
EvtPublisherMetadataLevels: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 12
EvtPublisherMetadataLevelName: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 13
EvtPublisherMetadataLevelValue: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 14
EvtPublisherMetadataLevelMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 15
EvtPublisherMetadataTasks: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 16
EvtPublisherMetadataTaskName: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 17
EvtPublisherMetadataTaskEventGuid: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 18
EvtPublisherMetadataTaskValue: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 19
EvtPublisherMetadataTaskMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 20
EvtPublisherMetadataOpcodes: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 21
EvtPublisherMetadataOpcodeName: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 22
EvtPublisherMetadataOpcodeValue: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 23
EvtPublisherMetadataOpcodeMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 24
EvtPublisherMetadataKeywords: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 25
EvtPublisherMetadataKeywordName: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 26
EvtPublisherMetadataKeywordValue: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 27
EvtPublisherMetadataKeywordMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 28
EvtPublisherMetadataPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 29
EVT_QUERY_FLAGS = UInt32
EvtQueryChannelPath: win32more.Windows.Win32.System.EventLog.EVT_QUERY_FLAGS = 1
EvtQueryFilePath: win32more.Windows.Win32.System.EventLog.EVT_QUERY_FLAGS = 2
EvtQueryForwardDirection: win32more.Windows.Win32.System.EventLog.EVT_QUERY_FLAGS = 256
EvtQueryReverseDirection: win32more.Windows.Win32.System.EventLog.EVT_QUERY_FLAGS = 512
EvtQueryTolerateQueryErrors: win32more.Windows.Win32.System.EventLog.EVT_QUERY_FLAGS = 4096
EVT_QUERY_PROPERTY_ID = Int32
EvtQueryNames: win32more.Windows.Win32.System.EventLog.EVT_QUERY_PROPERTY_ID = 0
EvtQueryStatuses: win32more.Windows.Win32.System.EventLog.EVT_QUERY_PROPERTY_ID = 1
EvtQueryPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_QUERY_PROPERTY_ID = 2
EVT_RENDER_CONTEXT_FLAGS = UInt32
EvtRenderContextValues: win32more.Windows.Win32.System.EventLog.EVT_RENDER_CONTEXT_FLAGS = 0
EvtRenderContextSystem: win32more.Windows.Win32.System.EventLog.EVT_RENDER_CONTEXT_FLAGS = 1
EvtRenderContextUser: win32more.Windows.Win32.System.EventLog.EVT_RENDER_CONTEXT_FLAGS = 2
EVT_RENDER_FLAGS = UInt32
EvtRenderEventValues: win32more.Windows.Win32.System.EventLog.EVT_RENDER_FLAGS = 0
EvtRenderEventXml: win32more.Windows.Win32.System.EventLog.EVT_RENDER_FLAGS = 1
EvtRenderBookmark: win32more.Windows.Win32.System.EventLog.EVT_RENDER_FLAGS = 2
class EVT_RPC_LOGIN(Structure):
    Server: win32more.Windows.Win32.Foundation.PWSTR
    User: win32more.Windows.Win32.Foundation.PWSTR
    Domain: win32more.Windows.Win32.Foundation.PWSTR
    Password: win32more.Windows.Win32.Foundation.PWSTR
    Flags: UInt32
EVT_RPC_LOGIN_FLAGS = UInt32
EvtRpcLoginAuthDefault: win32more.Windows.Win32.System.EventLog.EVT_RPC_LOGIN_FLAGS = 0
EvtRpcLoginAuthNegotiate: win32more.Windows.Win32.System.EventLog.EVT_RPC_LOGIN_FLAGS = 1
EvtRpcLoginAuthKerberos: win32more.Windows.Win32.System.EventLog.EVT_RPC_LOGIN_FLAGS = 2
EvtRpcLoginAuthNTLM: win32more.Windows.Win32.System.EventLog.EVT_RPC_LOGIN_FLAGS = 3
EVT_SEEK_FLAGS = UInt32
EvtSeekRelativeToFirst: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 1
EvtSeekRelativeToLast: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 2
EvtSeekRelativeToCurrent: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 3
EvtSeekRelativeToBookmark: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 4
EvtSeekOriginMask: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 7
EvtSeekStrict: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 65536
@winfunctype_pointer
def EVT_SUBSCRIBE_CALLBACK(Action: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_NOTIFY_ACTION, UserContext: VoidPtr, Event: win32more.Windows.Win32.System.EventLog.EVT_HANDLE) -> UInt32: ...
EVT_SUBSCRIBE_FLAGS = UInt32
EvtSubscribeToFutureEvents: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 1
EvtSubscribeStartAtOldestRecord: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 2
EvtSubscribeStartAfterBookmark: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 3
EvtSubscribeOriginMask: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 3
EvtSubscribeTolerateQueryErrors: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 4096
EvtSubscribeStrict: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 65536
EVT_SUBSCRIBE_NOTIFY_ACTION = Int32
EvtSubscribeActionError: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_NOTIFY_ACTION = 0
EvtSubscribeActionDeliver: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_NOTIFY_ACTION = 1
EVT_SYSTEM_PROPERTY_ID = Int32
EvtSystemProviderName: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 0
EvtSystemProviderGuid: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 1
EvtSystemEventID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 2
EvtSystemQualifiers: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 3
EvtSystemLevel: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 4
EvtSystemTask: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 5
EvtSystemOpcode: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 6
EvtSystemKeywords: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 7
EvtSystemTimeCreated: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 8
EvtSystemEventRecordId: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 9
EvtSystemActivityID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 10
EvtSystemRelatedActivityID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 11
EvtSystemProcessID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 12
EvtSystemThreadID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 13
EvtSystemChannel: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 14
EvtSystemComputer: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 15
EvtSystemUserID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 16
EvtSystemVersion: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 17
EvtSystemPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 18
class EVT_VARIANT(Structure):
    Anonymous: _Anonymous_e__Union
    Count: UInt32
    Type: UInt32
    class _Anonymous_e__Union(Union):
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
        SysTimeVal: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)
        GuidVal: POINTER(Guid)
        StringVal: win32more.Windows.Win32.Foundation.PWSTR
        AnsiStringVal: win32more.Windows.Win32.Foundation.PSTR
        BinaryVal: POINTER(Byte)
        SidVal: win32more.Windows.Win32.Security.PSID
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
        FileTimeArr: POINTER(win32more.Windows.Win32.Foundation.FILETIME)
        SysTimeArr: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)
        GuidArr: POINTER(Guid)
        StringArr: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
        AnsiStringArr: POINTER(win32more.Windows.Win32.Foundation.PSTR)
        SidArr: POINTER(win32more.Windows.Win32.Security.PSID)
        SizeTArr: POINTER(UIntPtr)
        EvtHandleVal: win32more.Windows.Win32.System.EventLog.EVT_HANDLE
        XmlVal: win32more.Windows.Win32.Foundation.PWSTR
        XmlValArr: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
EVT_VARIANT_TYPE = Int32
EvtVarTypeNull: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 0
EvtVarTypeString: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 1
EvtVarTypeAnsiString: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 2
EvtVarTypeSByte: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 3
EvtVarTypeByte: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 4
EvtVarTypeInt16: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 5
EvtVarTypeUInt16: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 6
EvtVarTypeInt32: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 7
EvtVarTypeUInt32: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 8
EvtVarTypeInt64: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 9
EvtVarTypeUInt64: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 10
EvtVarTypeSingle: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 11
EvtVarTypeDouble: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 12
EvtVarTypeBoolean: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 13
EvtVarTypeBinary: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 14
EvtVarTypeGuid: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 15
EvtVarTypeSizeT: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 16
EvtVarTypeFileTime: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 17
EvtVarTypeSysTime: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 18
EvtVarTypeSid: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 19
EvtVarTypeHexInt32: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 20
EvtVarTypeHexInt64: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 21
EvtVarTypeEvtHandle: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 32
EvtVarTypeEvtXml: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 35
READ_EVENT_LOG_READ_FLAGS = UInt32
EVENTLOG_SEEK_READ: win32more.Windows.Win32.System.EventLog.READ_EVENT_LOG_READ_FLAGS = 2
EVENTLOG_SEQUENTIAL_READ: win32more.Windows.Win32.System.EventLog.READ_EVENT_LOG_READ_FLAGS = 1
REPORT_EVENT_TYPE = UInt16
EVENTLOG_SUCCESS: win32more.Windows.Win32.System.EventLog.REPORT_EVENT_TYPE = 0
EVENTLOG_AUDIT_FAILURE: win32more.Windows.Win32.System.EventLog.REPORT_EVENT_TYPE = 16
EVENTLOG_AUDIT_SUCCESS: win32more.Windows.Win32.System.EventLog.REPORT_EVENT_TYPE = 8
EVENTLOG_ERROR_TYPE: win32more.Windows.Win32.System.EventLog.REPORT_EVENT_TYPE = 1
EVENTLOG_INFORMATION_TYPE: win32more.Windows.Win32.System.EventLog.REPORT_EVENT_TYPE = 4
EVENTLOG_WARNING_TYPE: win32more.Windows.Win32.System.EventLog.REPORT_EVENT_TYPE = 2


make_ready(__name__)
