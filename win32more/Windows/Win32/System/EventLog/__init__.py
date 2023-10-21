from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
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
EVT_CHANNEL_CLOCK_TYPE_EvtChannelClockTypeSystemTime: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CLOCK_TYPE = 0
EVT_CHANNEL_CLOCK_TYPE_EvtChannelClockTypeQPC: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CLOCK_TYPE = 1
EVT_CHANNEL_CONFIG_PROPERTY_ID = Int32
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigEnabled: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 0
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigIsolation: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 1
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigType: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 2
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigOwningPublisher: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 3
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigClassicEventlog: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 4
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigAccess: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 5
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigRetention: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 6
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigAutoBackup: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 7
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigMaxSize: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 8
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigLogFilePath: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 9
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigLevel: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 10
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigKeywords: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 11
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigControlGuid: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 12
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigBufferSize: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 13
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigMinBuffers: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 14
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigMaxBuffers: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 15
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigLatency: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 16
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigClockType: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 17
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigSidType: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 18
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublisherList: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 19
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigFileMax: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 20
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID = 21
EVT_CHANNEL_ISOLATION_TYPE = Int32
EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeApplication: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_ISOLATION_TYPE = 0
EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeSystem: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_ISOLATION_TYPE = 1
EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeCustom: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_ISOLATION_TYPE = 2
EVT_CHANNEL_REFERENCE_FLAGS = UInt32
EVT_CHANNEL_REFERENCE_FLAGS_EvtChannelReferenceImported: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_REFERENCE_FLAGS = 1
EVT_CHANNEL_SID_TYPE = Int32
EVT_CHANNEL_SID_TYPE_EvtChannelSidTypeNone: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_SID_TYPE = 0
EVT_CHANNEL_SID_TYPE_EvtChannelSidTypePublishing: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_SID_TYPE = 1
EVT_CHANNEL_TYPE = Int32
EVT_CHANNEL_TYPE_EvtChannelTypeAdmin: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_TYPE = 0
EVT_CHANNEL_TYPE_EvtChannelTypeOperational: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_TYPE = 1
EVT_CHANNEL_TYPE_EvtChannelTypeAnalytic: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_TYPE = 2
EVT_CHANNEL_TYPE_EvtChannelTypeDebug: win32more.Windows.Win32.System.EventLog.EVT_CHANNEL_TYPE = 3
EVT_EVENT_METADATA_PROPERTY_ID = Int32
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventID: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 0
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventVersion: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 1
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventChannel: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 2
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventLevel: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 3
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventOpcode: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 4
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventTask: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 5
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventKeyword: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 6
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventMessageID: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 7
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventTemplate: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 8
EVT_EVENT_METADATA_PROPERTY_ID_EvtEventMetadataPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID = 9
EVT_EVENT_PROPERTY_ID = Int32
EVT_EVENT_PROPERTY_ID_EvtEventQueryIDs: win32more.Windows.Win32.System.EventLog.EVT_EVENT_PROPERTY_ID = 0
EVT_EVENT_PROPERTY_ID_EvtEventPath: win32more.Windows.Win32.System.EventLog.EVT_EVENT_PROPERTY_ID = 1
EVT_EVENT_PROPERTY_ID_EvtEventPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_EVENT_PROPERTY_ID = 2
EVT_EXPORTLOG_FLAGS = UInt32
EVT_EXPORTLOG_FLAGS_EvtExportLogChannelPath: win32more.Windows.Win32.System.EventLog.EVT_EXPORTLOG_FLAGS = 1
EVT_EXPORTLOG_FLAGS_EvtExportLogFilePath: win32more.Windows.Win32.System.EventLog.EVT_EXPORTLOG_FLAGS = 2
EVT_EXPORTLOG_FLAGS_EvtExportLogTolerateQueryErrors: win32more.Windows.Win32.System.EventLog.EVT_EXPORTLOG_FLAGS = 4096
EVT_EXPORTLOG_FLAGS_EvtExportLogOverwrite: win32more.Windows.Win32.System.EventLog.EVT_EXPORTLOG_FLAGS = 8192
EVT_FORMAT_MESSAGE_FLAGS = UInt32
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageEvent: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 1
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageLevel: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 2
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageTask: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 3
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageOpcode: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 4
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageKeyword: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 5
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageChannel: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 6
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageProvider: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 7
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageId: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 8
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageXml: win32more.Windows.Win32.System.EventLog.EVT_FORMAT_MESSAGE_FLAGS = 9
EVT_HANDLE = IntPtr
EVT_LOGIN_CLASS = Int32
EVT_LOGIN_CLASS_EvtRpcLogin: win32more.Windows.Win32.System.EventLog.EVT_LOGIN_CLASS = 1
EVT_LOG_PROPERTY_ID = Int32
EVT_LOG_PROPERTY_ID_EvtLogCreationTime: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 0
EVT_LOG_PROPERTY_ID_EvtLogLastAccessTime: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 1
EVT_LOG_PROPERTY_ID_EvtLogLastWriteTime: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 2
EVT_LOG_PROPERTY_ID_EvtLogFileSize: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 3
EVT_LOG_PROPERTY_ID_EvtLogAttributes: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 4
EVT_LOG_PROPERTY_ID_EvtLogNumberOfLogRecords: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 5
EVT_LOG_PROPERTY_ID_EvtLogOldestRecordNumber: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 6
EVT_LOG_PROPERTY_ID_EvtLogFull: win32more.Windows.Win32.System.EventLog.EVT_LOG_PROPERTY_ID = 7
EVT_OPEN_LOG_FLAGS = UInt32
EVT_OPEN_LOG_FLAGS_EvtOpenChannelPath: win32more.Windows.Win32.System.EventLog.EVT_OPEN_LOG_FLAGS = 1
EVT_OPEN_LOG_FLAGS_EvtOpenFilePath: win32more.Windows.Win32.System.EventLog.EVT_OPEN_LOG_FLAGS = 2
EVT_PUBLISHER_METADATA_PROPERTY_ID = Int32
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPublisherGuid: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 0
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataResourceFilePath: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 1
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataParameterFilePath: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 2
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataMessageFilePath: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 3
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataHelpLink: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 4
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPublisherMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 5
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferences: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 6
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferencePath: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 7
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceIndex: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 8
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 9
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceFlags: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 10
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 11
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevels: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 12
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelName: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 13
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelValue: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 14
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 15
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTasks: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 16
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskName: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 17
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskEventGuid: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 18
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskValue: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 19
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 20
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodes: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 21
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeName: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 22
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeValue: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 23
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 24
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywords: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 25
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordName: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 26
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordValue: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 27
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordMessageID: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 28
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID = 29
EVT_QUERY_FLAGS = UInt32
EVT_QUERY_FLAGS_EvtQueryChannelPath: win32more.Windows.Win32.System.EventLog.EVT_QUERY_FLAGS = 1
EVT_QUERY_FLAGS_EvtQueryFilePath: win32more.Windows.Win32.System.EventLog.EVT_QUERY_FLAGS = 2
EVT_QUERY_FLAGS_EvtQueryForwardDirection: win32more.Windows.Win32.System.EventLog.EVT_QUERY_FLAGS = 256
EVT_QUERY_FLAGS_EvtQueryReverseDirection: win32more.Windows.Win32.System.EventLog.EVT_QUERY_FLAGS = 512
EVT_QUERY_FLAGS_EvtQueryTolerateQueryErrors: win32more.Windows.Win32.System.EventLog.EVT_QUERY_FLAGS = 4096
EVT_QUERY_PROPERTY_ID = Int32
EVT_QUERY_PROPERTY_ID_EvtQueryNames: win32more.Windows.Win32.System.EventLog.EVT_QUERY_PROPERTY_ID = 0
EVT_QUERY_PROPERTY_ID_EvtQueryStatuses: win32more.Windows.Win32.System.EventLog.EVT_QUERY_PROPERTY_ID = 1
EVT_QUERY_PROPERTY_ID_EvtQueryPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_QUERY_PROPERTY_ID = 2
EVT_RENDER_CONTEXT_FLAGS = UInt32
EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextValues: win32more.Windows.Win32.System.EventLog.EVT_RENDER_CONTEXT_FLAGS = 0
EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextSystem: win32more.Windows.Win32.System.EventLog.EVT_RENDER_CONTEXT_FLAGS = 1
EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextUser: win32more.Windows.Win32.System.EventLog.EVT_RENDER_CONTEXT_FLAGS = 2
EVT_RENDER_FLAGS = UInt32
EVT_RENDER_FLAGS_EvtRenderEventValues: win32more.Windows.Win32.System.EventLog.EVT_RENDER_FLAGS = 0
EVT_RENDER_FLAGS_EvtRenderEventXml: win32more.Windows.Win32.System.EventLog.EVT_RENDER_FLAGS = 1
EVT_RENDER_FLAGS_EvtRenderBookmark: win32more.Windows.Win32.System.EventLog.EVT_RENDER_FLAGS = 2
class EVT_RPC_LOGIN(EasyCastStructure):
    Server: win32more.Windows.Win32.Foundation.PWSTR
    User: win32more.Windows.Win32.Foundation.PWSTR
    Domain: win32more.Windows.Win32.Foundation.PWSTR
    Password: win32more.Windows.Win32.Foundation.PWSTR
    Flags: UInt32
EVT_RPC_LOGIN_FLAGS = UInt32
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthDefault: win32more.Windows.Win32.System.EventLog.EVT_RPC_LOGIN_FLAGS = 0
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthNegotiate: win32more.Windows.Win32.System.EventLog.EVT_RPC_LOGIN_FLAGS = 1
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthKerberos: win32more.Windows.Win32.System.EventLog.EVT_RPC_LOGIN_FLAGS = 2
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthNTLM: win32more.Windows.Win32.System.EventLog.EVT_RPC_LOGIN_FLAGS = 3
EVT_SEEK_FLAGS = UInt32
EVT_SEEK_FLAGS_EvtSeekRelativeToFirst: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 1
EVT_SEEK_FLAGS_EvtSeekRelativeToLast: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 2
EVT_SEEK_FLAGS_EvtSeekRelativeToCurrent: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 3
EVT_SEEK_FLAGS_EvtSeekRelativeToBookmark: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 4
EVT_SEEK_FLAGS_EvtSeekOriginMask: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 7
EVT_SEEK_FLAGS_EvtSeekStrict: win32more.Windows.Win32.System.EventLog.EVT_SEEK_FLAGS = 65536
@winfunctype_pointer
def EVT_SUBSCRIBE_CALLBACK(Action: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_NOTIFY_ACTION, UserContext: VoidPtr, Event: win32more.Windows.Win32.System.EventLog.EVT_HANDLE) -> UInt32: ...
EVT_SUBSCRIBE_FLAGS = UInt32
EVT_SUBSCRIBE_FLAGS_EvtSubscribeToFutureEvents: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 1
EVT_SUBSCRIBE_FLAGS_EvtSubscribeStartAtOldestRecord: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 2
EVT_SUBSCRIBE_FLAGS_EvtSubscribeStartAfterBookmark: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 3
EVT_SUBSCRIBE_FLAGS_EvtSubscribeOriginMask: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 3
EVT_SUBSCRIBE_FLAGS_EvtSubscribeTolerateQueryErrors: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 4096
EVT_SUBSCRIBE_FLAGS_EvtSubscribeStrict: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_FLAGS = 65536
EVT_SUBSCRIBE_NOTIFY_ACTION = Int32
EVT_SUBSCRIBE_NOTIFY_ACTION_EvtSubscribeActionError: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_NOTIFY_ACTION = 0
EVT_SUBSCRIBE_NOTIFY_ACTION_EvtSubscribeActionDeliver: win32more.Windows.Win32.System.EventLog.EVT_SUBSCRIBE_NOTIFY_ACTION = 1
EVT_SYSTEM_PROPERTY_ID = Int32
EVT_SYSTEM_PROPERTY_ID_EvtSystemProviderName: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 0
EVT_SYSTEM_PROPERTY_ID_EvtSystemProviderGuid: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 1
EVT_SYSTEM_PROPERTY_ID_EvtSystemEventID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 2
EVT_SYSTEM_PROPERTY_ID_EvtSystemQualifiers: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 3
EVT_SYSTEM_PROPERTY_ID_EvtSystemLevel: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 4
EVT_SYSTEM_PROPERTY_ID_EvtSystemTask: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 5
EVT_SYSTEM_PROPERTY_ID_EvtSystemOpcode: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 6
EVT_SYSTEM_PROPERTY_ID_EvtSystemKeywords: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 7
EVT_SYSTEM_PROPERTY_ID_EvtSystemTimeCreated: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 8
EVT_SYSTEM_PROPERTY_ID_EvtSystemEventRecordId: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 9
EVT_SYSTEM_PROPERTY_ID_EvtSystemActivityID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 10
EVT_SYSTEM_PROPERTY_ID_EvtSystemRelatedActivityID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 11
EVT_SYSTEM_PROPERTY_ID_EvtSystemProcessID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 12
EVT_SYSTEM_PROPERTY_ID_EvtSystemThreadID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 13
EVT_SYSTEM_PROPERTY_ID_EvtSystemChannel: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 14
EVT_SYSTEM_PROPERTY_ID_EvtSystemComputer: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 15
EVT_SYSTEM_PROPERTY_ID_EvtSystemUserID: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 16
EVT_SYSTEM_PROPERTY_ID_EvtSystemVersion: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 17
EVT_SYSTEM_PROPERTY_ID_EvtSystemPropertyIdEND: win32more.Windows.Win32.System.EventLog.EVT_SYSTEM_PROPERTY_ID = 18
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
        SysTimeVal: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)
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
        FileTimeArr: POINTER(win32more.Windows.Win32.Foundation.FILETIME)
        SysTimeArr: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)
        GuidArr: POINTER(Guid)
        StringArr: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
        AnsiStringArr: POINTER(win32more.Windows.Win32.Foundation.PSTR)
        SidArr: POINTER(win32more.Windows.Win32.Foundation.PSID)
        SizeTArr: POINTER(UIntPtr)
        EvtHandleVal: win32more.Windows.Win32.System.EventLog.EVT_HANDLE
        XmlVal: win32more.Windows.Win32.Foundation.PWSTR
        XmlValArr: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
EVT_VARIANT_TYPE = Int32
EVT_VARIANT_TYPE_EvtVarTypeNull: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 0
EVT_VARIANT_TYPE_EvtVarTypeString: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 1
EVT_VARIANT_TYPE_EvtVarTypeAnsiString: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 2
EVT_VARIANT_TYPE_EvtVarTypeSByte: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 3
EVT_VARIANT_TYPE_EvtVarTypeByte: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 4
EVT_VARIANT_TYPE_EvtVarTypeInt16: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 5
EVT_VARIANT_TYPE_EvtVarTypeUInt16: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 6
EVT_VARIANT_TYPE_EvtVarTypeInt32: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 7
EVT_VARIANT_TYPE_EvtVarTypeUInt32: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 8
EVT_VARIANT_TYPE_EvtVarTypeInt64: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 9
EVT_VARIANT_TYPE_EvtVarTypeUInt64: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 10
EVT_VARIANT_TYPE_EvtVarTypeSingle: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 11
EVT_VARIANT_TYPE_EvtVarTypeDouble: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 12
EVT_VARIANT_TYPE_EvtVarTypeBoolean: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 13
EVT_VARIANT_TYPE_EvtVarTypeBinary: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 14
EVT_VARIANT_TYPE_EvtVarTypeGuid: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 15
EVT_VARIANT_TYPE_EvtVarTypeSizeT: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 16
EVT_VARIANT_TYPE_EvtVarTypeFileTime: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 17
EVT_VARIANT_TYPE_EvtVarTypeSysTime: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 18
EVT_VARIANT_TYPE_EvtVarTypeSid: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 19
EVT_VARIANT_TYPE_EvtVarTypeHexInt32: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 20
EVT_VARIANT_TYPE_EvtVarTypeHexInt64: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 21
EVT_VARIANT_TYPE_EvtVarTypeEvtHandle: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 32
EVT_VARIANT_TYPE_EvtVarTypeEvtXml: win32more.Windows.Win32.System.EventLog.EVT_VARIANT_TYPE = 35
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
