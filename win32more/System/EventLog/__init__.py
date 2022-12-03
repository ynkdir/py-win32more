from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.EventLog
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
EVT_VARIANT_TYPE_MASK = 127
EVT_VARIANT_TYPE_ARRAY = 128
EVT_READ_ACCESS = 1
EVT_WRITE_ACCESS = 2
EVT_CLEAR_ACCESS = 4
EVT_ALL_ACCESS = 7
def _define_EvtOpenSession():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_LOGIN_CLASS,c_void_p,UInt32,UInt32)(('EvtOpenSession', windll['wevtapi.dll']), ((1, 'LoginClass'),(1, 'Login'),(1, 'Timeout'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE)(('EvtClose', windll['wevtapi.dll']), ((1, 'Object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtCancel():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE)(('EvtCancel', windll['wevtapi.dll']), ((1, 'Object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtGetExtendedStatus():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('EvtGetExtendedStatus', windll['wevtapi.dll']), ((1, 'BufferSize'),(1, 'Buffer'),(1, 'BufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtQuery():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('EvtQuery', windll['wevtapi.dll']), ((1, 'Session'),(1, 'Path'),(1, 'Query'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtNext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,UInt32,POINTER(IntPtr),UInt32,UInt32,POINTER(UInt32))(('EvtNext', windll['wevtapi.dll']), ((1, 'ResultSet'),(1, 'EventsSize'),(1, 'Events'),(1, 'Timeout'),(1, 'Flags'),(1, 'Returned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtSeek():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,Int64,win32more.System.EventLog.EVT_HANDLE,UInt32,UInt32)(('EvtSeek', windll['wevtapi.dll']), ((1, 'ResultSet'),(1, 'Position'),(1, 'Bookmark'),(1, 'Timeout'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtSubscribe():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.EventLog.EVT_HANDLE,c_void_p,win32more.System.EventLog.EVT_SUBSCRIBE_CALLBACK,UInt32)(('EvtSubscribe', windll['wevtapi.dll']), ((1, 'Session'),(1, 'SignalEvent'),(1, 'ChannelPath'),(1, 'Query'),(1, 'Bookmark'),(1, 'Context'),(1, 'Callback'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtCreateRenderContext():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,UInt32,POINTER(win32more.Foundation.PWSTR),UInt32)(('EvtCreateRenderContext', windll['wevtapi.dll']), ((1, 'ValuePathsCount'),(1, 'ValuePaths'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtRender():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE,UInt32,UInt32,c_void_p,POINTER(UInt32),POINTER(UInt32))(('EvtRender', windll['wevtapi.dll']), ((1, 'Context'),(1, 'Fragment'),(1, 'Flags'),(1, 'BufferSize'),(1, 'Buffer'),(1, 'BufferUsed'),(1, 'PropertyCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtFormatMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE,UInt32,UInt32,POINTER(win32more.System.EventLog.EVT_VARIANT_head),UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('EvtFormatMessage', windll['wevtapi.dll']), ((1, 'PublisherMetadata'),(1, 'Event'),(1, 'MessageId'),(1, 'ValueCount'),(1, 'Values'),(1, 'Flags'),(1, 'BufferSize'),(1, 'Buffer'),(1, 'BufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtOpenLog():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE,win32more.Foundation.PWSTR,UInt32)(('EvtOpenLog', windll['wevtapi.dll']), ((1, 'Session'),(1, 'Path'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtGetLogInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_LOG_PROPERTY_ID,UInt32,POINTER(win32more.System.EventLog.EVT_VARIANT_head),POINTER(UInt32))(('EvtGetLogInfo', windll['wevtapi.dll']), ((1, 'Log'),(1, 'PropertyId'),(1, 'PropertyValueBufferSize'),(1, 'PropertyValueBuffer'),(1, 'PropertyValueBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtClearLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('EvtClearLog', windll['wevtapi.dll']), ((1, 'Session'),(1, 'ChannelPath'),(1, 'TargetFilePath'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtExportLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('EvtExportLog', windll['wevtapi.dll']), ((1, 'Session'),(1, 'Path'),(1, 'Query'),(1, 'TargetFilePath'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtArchiveExportedLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.Foundation.PWSTR,UInt32,UInt32)(('EvtArchiveExportedLog', windll['wevtapi.dll']), ((1, 'Session'),(1, 'LogFilePath'),(1, 'Locale'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtOpenChannelEnum():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE,UInt32)(('EvtOpenChannelEnum', windll['wevtapi.dll']), ((1, 'Session'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtNextChannelPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('EvtNextChannelPath', windll['wevtapi.dll']), ((1, 'ChannelEnum'),(1, 'ChannelPathBufferSize'),(1, 'ChannelPathBuffer'),(1, 'ChannelPathBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtOpenChannelConfig():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE,win32more.Foundation.PWSTR,UInt32)(('EvtOpenChannelConfig', windll['wevtapi.dll']), ((1, 'Session'),(1, 'ChannelPath'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtSaveChannelConfig():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,UInt32)(('EvtSaveChannelConfig', windll['wevtapi.dll']), ((1, 'ChannelConfig'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtSetChannelConfigProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID,UInt32,POINTER(win32more.System.EventLog.EVT_VARIANT_head))(('EvtSetChannelConfigProperty', windll['wevtapi.dll']), ((1, 'ChannelConfig'),(1, 'PropertyId'),(1, 'Flags'),(1, 'PropertyValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtGetChannelConfigProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_CHANNEL_CONFIG_PROPERTY_ID,UInt32,UInt32,POINTER(win32more.System.EventLog.EVT_VARIANT_head),POINTER(UInt32))(('EvtGetChannelConfigProperty', windll['wevtapi.dll']), ((1, 'ChannelConfig'),(1, 'PropertyId'),(1, 'Flags'),(1, 'PropertyValueBufferSize'),(1, 'PropertyValueBuffer'),(1, 'PropertyValueBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtOpenPublisherEnum():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE,UInt32)(('EvtOpenPublisherEnum', windll['wevtapi.dll']), ((1, 'Session'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtNextPublisherId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('EvtNextPublisherId', windll['wevtapi.dll']), ((1, 'PublisherEnum'),(1, 'PublisherIdBufferSize'),(1, 'PublisherIdBuffer'),(1, 'PublisherIdBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtOpenPublisherMetadata():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32)(('EvtOpenPublisherMetadata', windll['wevtapi.dll']), ((1, 'Session'),(1, 'PublisherId'),(1, 'LogFilePath'),(1, 'Locale'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtGetPublisherMetadataProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_PUBLISHER_METADATA_PROPERTY_ID,UInt32,UInt32,POINTER(win32more.System.EventLog.EVT_VARIANT_head),POINTER(UInt32))(('EvtGetPublisherMetadataProperty', windll['wevtapi.dll']), ((1, 'PublisherMetadata'),(1, 'PropertyId'),(1, 'Flags'),(1, 'PublisherMetadataPropertyBufferSize'),(1, 'PublisherMetadataPropertyBuffer'),(1, 'PublisherMetadataPropertyBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtOpenEventMetadataEnum():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE,UInt32)(('EvtOpenEventMetadataEnum', windll['wevtapi.dll']), ((1, 'PublisherMetadata'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtNextEventMetadata():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE,UInt32)(('EvtNextEventMetadata', windll['wevtapi.dll']), ((1, 'EventMetadataEnum'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtGetEventMetadataProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_EVENT_METADATA_PROPERTY_ID,UInt32,UInt32,POINTER(win32more.System.EventLog.EVT_VARIANT_head),POINTER(UInt32))(('EvtGetEventMetadataProperty', windll['wevtapi.dll']), ((1, 'EventMetadata'),(1, 'PropertyId'),(1, 'Flags'),(1, 'EventMetadataPropertyBufferSize'),(1, 'EventMetadataPropertyBuffer'),(1, 'EventMetadataPropertyBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtGetObjectArraySize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(UInt32))(('EvtGetObjectArraySize', windll['wevtapi.dll']), ((1, 'ObjectArray'),(1, 'ObjectArraySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtGetObjectArrayProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,UInt32,UInt32,UInt32,POINTER(win32more.System.EventLog.EVT_VARIANT_head),POINTER(UInt32))(('EvtGetObjectArrayProperty', windll['wevtapi.dll']), ((1, 'ObjectArray'),(1, 'PropertyId'),(1, 'ArrayIndex'),(1, 'Flags'),(1, 'PropertyValueBufferSize'),(1, 'PropertyValueBuffer'),(1, 'PropertyValueBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtGetQueryInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_QUERY_PROPERTY_ID,UInt32,POINTER(win32more.System.EventLog.EVT_VARIANT_head),POINTER(UInt32))(('EvtGetQueryInfo', windll['wevtapi.dll']), ((1, 'QueryOrSubscription'),(1, 'PropertyId'),(1, 'PropertyValueBufferSize'),(1, 'PropertyValueBuffer'),(1, 'PropertyValueBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtCreateBookmark():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EVT_HANDLE,win32more.Foundation.PWSTR)(('EvtCreateBookmark', windll['wevtapi.dll']), ((1, 'BookmarkXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtUpdateBookmark():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_HANDLE)(('EvtUpdateBookmark', windll['wevtapi.dll']), ((1, 'Bookmark'),(1, 'Event'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvtGetEventInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EVT_HANDLE,win32more.System.EventLog.EVT_EVENT_PROPERTY_ID,UInt32,POINTER(win32more.System.EventLog.EVT_VARIANT_head),POINTER(UInt32))(('EvtGetEventInfo', windll['wevtapi.dll']), ((1, 'Event'),(1, 'PropertyId'),(1, 'PropertyValueBufferSize'),(1, 'PropertyValueBuffer'),(1, 'PropertyValueBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClearEventLogA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventLogHandle,win32more.Foundation.PSTR)(('ClearEventLogA', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'lpBackupFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClearEventLogW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventLogHandle,win32more.Foundation.PWSTR)(('ClearEventLogW', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'lpBackupFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BackupEventLogA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventLogHandle,win32more.Foundation.PSTR)(('BackupEventLogA', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'lpBackupFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BackupEventLogW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventLogHandle,win32more.Foundation.PWSTR)(('BackupEventLogW', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'lpBackupFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseEventLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventLogHandle)(('CloseEventLog', windll['ADVAPI32.dll']), ((1, 'hEventLog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeregisterEventSource():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventSourceHandle)(('DeregisterEventSource', windll['ADVAPI32.dll']), ((1, 'hEventLog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyChangeEventLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventLogHandle,win32more.Foundation.HANDLE)(('NotifyChangeEventLog', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'hEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumberOfEventLogRecords():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventLogHandle,POINTER(UInt32))(('GetNumberOfEventLogRecords', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'NumberOfRecords'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOldestEventLogRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventLogHandle,POINTER(UInt32))(('GetOldestEventLogRecord', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'OldestRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenEventLogA():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EventLogHandle,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('OpenEventLogA', windll['ADVAPI32.dll']), ((1, 'lpUNCServerName'),(1, 'lpSourceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenEventLogW():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EventLogHandle,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('OpenEventLogW', windll['ADVAPI32.dll']), ((1, 'lpUNCServerName'),(1, 'lpSourceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterEventSourceA():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EventSourceHandle,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('RegisterEventSourceA', windll['ADVAPI32.dll']), ((1, 'lpUNCServerName'),(1, 'lpSourceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterEventSourceW():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EventSourceHandle,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('RegisterEventSourceW', windll['ADVAPI32.dll']), ((1, 'lpUNCServerName'),(1, 'lpSourceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenBackupEventLogA():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EventLogHandle,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('OpenBackupEventLogA', windll['ADVAPI32.dll']), ((1, 'lpUNCServerName'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenBackupEventLogW():
    try:
        return WINFUNCTYPE(win32more.System.EventLog.EventLogHandle,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('OpenBackupEventLogW', windll['ADVAPI32.dll']), ((1, 'lpUNCServerName'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadEventLogA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventLogHandle,win32more.System.EventLog.READ_EVENT_LOG_READ_FLAGS,UInt32,c_void_p,UInt32,POINTER(UInt32),POINTER(UInt32))(('ReadEventLogA', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'dwReadFlags'),(1, 'dwRecordOffset'),(1, 'lpBuffer'),(1, 'nNumberOfBytesToRead'),(1, 'pnBytesRead'),(1, 'pnMinNumberOfBytesNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadEventLogW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventLogHandle,win32more.System.EventLog.READ_EVENT_LOG_READ_FLAGS,UInt32,c_void_p,UInt32,POINTER(UInt32),POINTER(UInt32))(('ReadEventLogW', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'dwReadFlags'),(1, 'dwRecordOffset'),(1, 'lpBuffer'),(1, 'nNumberOfBytesToRead'),(1, 'pnBytesRead'),(1, 'pnMinNumberOfBytesNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportEventA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventSourceHandle,win32more.System.EventLog.REPORT_EVENT_TYPE,UInt16,UInt32,win32more.Foundation.PSID,UInt16,UInt32,POINTER(win32more.Foundation.PSTR),c_void_p)(('ReportEventA', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'wType'),(1, 'wCategory'),(1, 'dwEventID'),(1, 'lpUserSid'),(1, 'wNumStrings'),(1, 'dwDataSize'),(1, 'lpStrings'),(1, 'lpRawData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportEventW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventSourceHandle,win32more.System.EventLog.REPORT_EVENT_TYPE,UInt16,UInt32,win32more.Foundation.PSID,UInt16,UInt32,POINTER(win32more.Foundation.PWSTR),c_void_p)(('ReportEventW', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'wType'),(1, 'wCategory'),(1, 'dwEventID'),(1, 'lpUserSid'),(1, 'wNumStrings'),(1, 'dwDataSize'),(1, 'lpStrings'),(1, 'lpRawData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEventLogInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.EventLog.EventLogHandle,UInt32,c_void_p,UInt32,POINTER(UInt32))(('GetEventLogInformation', windll['ADVAPI32.dll']), ((1, 'hEventLog'),(1, 'dwInfoLevel'),(1, 'lpBuffer'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EVENTLOG_FULL_INFORMATION_head():
    class EVENTLOG_FULL_INFORMATION(Structure):
        pass
    return EVENTLOG_FULL_INFORMATION
def _define_EVENTLOG_FULL_INFORMATION():
    EVENTLOG_FULL_INFORMATION = win32more.System.EventLog.EVENTLOG_FULL_INFORMATION_head
    EVENTLOG_FULL_INFORMATION._fields_ = [
        ('dwFull', UInt32),
    ]
    return EVENTLOG_FULL_INFORMATION
EventLogHandle = IntPtr
def _define_EVENTLOGRECORD_head():
    class EVENTLOGRECORD(Structure):
        pass
    return EVENTLOGRECORD
def _define_EVENTLOGRECORD():
    EVENTLOGRECORD = win32more.System.EventLog.EVENTLOGRECORD_head
    EVENTLOGRECORD._fields_ = [
        ('Length', UInt32),
        ('Reserved', UInt32),
        ('RecordNumber', UInt32),
        ('TimeGenerated', UInt32),
        ('TimeWritten', UInt32),
        ('EventID', UInt32),
        ('EventType', win32more.System.EventLog.REPORT_EVENT_TYPE),
        ('NumStrings', UInt16),
        ('EventCategory', UInt16),
        ('ReservedFlags', UInt16),
        ('ClosingRecordNumber', UInt32),
        ('StringOffset', UInt32),
        ('UserSidLength', UInt32),
        ('UserSidOffset', UInt32),
        ('DataLength', UInt32),
        ('DataOffset', UInt32),
    ]
    return EVENTLOGRECORD
def _define_EVENTSFORLOGFILE_head():
    class EVENTSFORLOGFILE(Structure):
        pass
    return EVENTSFORLOGFILE
def _define_EVENTSFORLOGFILE():
    EVENTSFORLOGFILE = win32more.System.EventLog.EVENTSFORLOGFILE_head
    EVENTSFORLOGFILE._fields_ = [
        ('ulSize', UInt32),
        ('szLogicalLogFile', Char * 256),
        ('ulNumRecords', UInt32),
        ('pEventLogRecords', win32more.System.EventLog.EVENTLOGRECORD * 1),
    ]
    return EVENTSFORLOGFILE
EventSourceHandle = IntPtr
EVT_CHANNEL_CLOCK_TYPE = Int32
EVT_CHANNEL_CLOCK_TYPE_EvtChannelClockTypeSystemTime = 0
EVT_CHANNEL_CLOCK_TYPE_EvtChannelClockTypeQPC = 1
EVT_CHANNEL_CONFIG_PROPERTY_ID = Int32
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigEnabled = 0
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigIsolation = 1
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigType = 2
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigOwningPublisher = 3
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigClassicEventlog = 4
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigAccess = 5
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigRetention = 6
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigAutoBackup = 7
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigMaxSize = 8
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigLogFilePath = 9
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigLevel = 10
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigKeywords = 11
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigControlGuid = 12
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigBufferSize = 13
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigMinBuffers = 14
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigMaxBuffers = 15
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigLatency = 16
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigClockType = 17
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigSidType = 18
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublisherList = 19
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigFileMax = 20
EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigPropertyIdEND = 21
EVT_CHANNEL_ISOLATION_TYPE = Int32
EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeApplication = 0
EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeSystem = 1
EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeCustom = 2
EVT_CHANNEL_REFERENCE_FLAGS = UInt32
EVT_CHANNEL_REFERENCE_FLAGS_EvtChannelReferenceImported = 1
EVT_CHANNEL_SID_TYPE = Int32
EVT_CHANNEL_SID_TYPE_EvtChannelSidTypeNone = 0
EVT_CHANNEL_SID_TYPE_EvtChannelSidTypePublishing = 1
EVT_CHANNEL_TYPE = Int32
EVT_CHANNEL_TYPE_EvtChannelTypeAdmin = 0
EVT_CHANNEL_TYPE_EvtChannelTypeOperational = 1
EVT_CHANNEL_TYPE_EvtChannelTypeAnalytic = 2
EVT_CHANNEL_TYPE_EvtChannelTypeDebug = 3
EVT_EVENT_METADATA_PROPERTY_ID = Int32
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventID = 0
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventVersion = 1
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventChannel = 2
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventLevel = 3
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventOpcode = 4
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventTask = 5
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventKeyword = 6
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventMessageID = 7
EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventTemplate = 8
EVT_EVENT_METADATA_PROPERTY_ID_EvtEventMetadataPropertyIdEND = 9
EVT_EVENT_PROPERTY_ID = Int32
EVT_EVENT_PROPERTY_ID_EvtEventQueryIDs = 0
EVT_EVENT_PROPERTY_ID_EvtEventPath = 1
EVT_EVENT_PROPERTY_ID_EvtEventPropertyIdEND = 2
EVT_EXPORTLOG_FLAGS = UInt32
EVT_EXPORTLOG_FLAGS_EvtExportLogChannelPath = 1
EVT_EXPORTLOG_FLAGS_EvtExportLogFilePath = 2
EVT_EXPORTLOG_FLAGS_EvtExportLogTolerateQueryErrors = 4096
EVT_EXPORTLOG_FLAGS_EvtExportLogOverwrite = 8192
EVT_FORMAT_MESSAGE_FLAGS = UInt32
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageEvent = 1
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageLevel = 2
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageTask = 3
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageOpcode = 4
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageKeyword = 5
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageChannel = 6
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageProvider = 7
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageId = 8
EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageXml = 9
EVT_HANDLE = IntPtr
EVT_LOG_PROPERTY_ID = Int32
EVT_LOG_PROPERTY_ID_EvtLogCreationTime = 0
EVT_LOG_PROPERTY_ID_EvtLogLastAccessTime = 1
EVT_LOG_PROPERTY_ID_EvtLogLastWriteTime = 2
EVT_LOG_PROPERTY_ID_EvtLogFileSize = 3
EVT_LOG_PROPERTY_ID_EvtLogAttributes = 4
EVT_LOG_PROPERTY_ID_EvtLogNumberOfLogRecords = 5
EVT_LOG_PROPERTY_ID_EvtLogOldestRecordNumber = 6
EVT_LOG_PROPERTY_ID_EvtLogFull = 7
EVT_LOGIN_CLASS = Int32
EVT_LOGIN_CLASS_EvtRpcLogin = 1
EVT_OPEN_LOG_FLAGS = UInt32
EVT_OPEN_LOG_FLAGS_EvtOpenChannelPath = 1
EVT_OPEN_LOG_FLAGS_EvtOpenFilePath = 2
EVT_PUBLISHER_METADATA_PROPERTY_ID = Int32
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPublisherGuid = 0
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataResourceFilePath = 1
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataParameterFilePath = 2
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataMessageFilePath = 3
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataHelpLink = 4
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPublisherMessageID = 5
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferences = 6
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferencePath = 7
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceIndex = 8
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceID = 9
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceFlags = 10
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceMessageID = 11
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevels = 12
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelName = 13
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelValue = 14
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelMessageID = 15
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTasks = 16
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskName = 17
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskEventGuid = 18
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskValue = 19
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskMessageID = 20
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodes = 21
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeName = 22
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeValue = 23
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeMessageID = 24
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywords = 25
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordName = 26
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordValue = 27
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordMessageID = 28
EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPropertyIdEND = 29
EVT_QUERY_FLAGS = UInt32
EVT_QUERY_FLAGS_EvtQueryChannelPath = 1
EVT_QUERY_FLAGS_EvtQueryFilePath = 2
EVT_QUERY_FLAGS_EvtQueryForwardDirection = 256
EVT_QUERY_FLAGS_EvtQueryReverseDirection = 512
EVT_QUERY_FLAGS_EvtQueryTolerateQueryErrors = 4096
EVT_QUERY_PROPERTY_ID = Int32
EVT_QUERY_PROPERTY_ID_EvtQueryNames = 0
EVT_QUERY_PROPERTY_ID_EvtQueryStatuses = 1
EVT_QUERY_PROPERTY_ID_EvtQueryPropertyIdEND = 2
EVT_RENDER_CONTEXT_FLAGS = UInt32
EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextValues = 0
EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextSystem = 1
EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextUser = 2
EVT_RENDER_FLAGS = UInt32
EVT_RENDER_FLAGS_EvtRenderEventValues = 0
EVT_RENDER_FLAGS_EvtRenderEventXml = 1
EVT_RENDER_FLAGS_EvtRenderBookmark = 2
def _define_EVT_RPC_LOGIN_head():
    class EVT_RPC_LOGIN(Structure):
        pass
    return EVT_RPC_LOGIN
def _define_EVT_RPC_LOGIN():
    EVT_RPC_LOGIN = win32more.System.EventLog.EVT_RPC_LOGIN_head
    EVT_RPC_LOGIN._fields_ = [
        ('Server', win32more.Foundation.PWSTR),
        ('User', win32more.Foundation.PWSTR),
        ('Domain', win32more.Foundation.PWSTR),
        ('Password', win32more.Foundation.PWSTR),
        ('Flags', UInt32),
    ]
    return EVT_RPC_LOGIN
EVT_RPC_LOGIN_FLAGS = UInt32
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthDefault = 0
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthNegotiate = 1
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthKerberos = 2
EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthNTLM = 3
EVT_SEEK_FLAGS = UInt32
EVT_SEEK_FLAGS_EvtSeekRelativeToFirst = 1
EVT_SEEK_FLAGS_EvtSeekRelativeToLast = 2
EVT_SEEK_FLAGS_EvtSeekRelativeToCurrent = 3
EVT_SEEK_FLAGS_EvtSeekRelativeToBookmark = 4
EVT_SEEK_FLAGS_EvtSeekOriginMask = 7
EVT_SEEK_FLAGS_EvtSeekStrict = 65536
def _define_EVT_SUBSCRIBE_CALLBACK():
    return WINFUNCTYPE(UInt32,win32more.System.EventLog.EVT_SUBSCRIBE_NOTIFY_ACTION,c_void_p,win32more.System.EventLog.EVT_HANDLE)
EVT_SUBSCRIBE_FLAGS = UInt32
EVT_SUBSCRIBE_FLAGS_EvtSubscribeToFutureEvents = 1
EVT_SUBSCRIBE_FLAGS_EvtSubscribeStartAtOldestRecord = 2
EVT_SUBSCRIBE_FLAGS_EvtSubscribeStartAfterBookmark = 3
EVT_SUBSCRIBE_FLAGS_EvtSubscribeOriginMask = 3
EVT_SUBSCRIBE_FLAGS_EvtSubscribeTolerateQueryErrors = 4096
EVT_SUBSCRIBE_FLAGS_EvtSubscribeStrict = 65536
EVT_SUBSCRIBE_NOTIFY_ACTION = Int32
EVT_SUBSCRIBE_NOTIFY_ACTION_EvtSubscribeActionError = 0
EVT_SUBSCRIBE_NOTIFY_ACTION_EvtSubscribeActionDeliver = 1
EVT_SYSTEM_PROPERTY_ID = Int32
EVT_SYSTEM_PROPERTY_ID_EvtSystemProviderName = 0
EVT_SYSTEM_PROPERTY_ID_EvtSystemProviderGuid = 1
EVT_SYSTEM_PROPERTY_ID_EvtSystemEventID = 2
EVT_SYSTEM_PROPERTY_ID_EvtSystemQualifiers = 3
EVT_SYSTEM_PROPERTY_ID_EvtSystemLevel = 4
EVT_SYSTEM_PROPERTY_ID_EvtSystemTask = 5
EVT_SYSTEM_PROPERTY_ID_EvtSystemOpcode = 6
EVT_SYSTEM_PROPERTY_ID_EvtSystemKeywords = 7
EVT_SYSTEM_PROPERTY_ID_EvtSystemTimeCreated = 8
EVT_SYSTEM_PROPERTY_ID_EvtSystemEventRecordId = 9
EVT_SYSTEM_PROPERTY_ID_EvtSystemActivityID = 10
EVT_SYSTEM_PROPERTY_ID_EvtSystemRelatedActivityID = 11
EVT_SYSTEM_PROPERTY_ID_EvtSystemProcessID = 12
EVT_SYSTEM_PROPERTY_ID_EvtSystemThreadID = 13
EVT_SYSTEM_PROPERTY_ID_EvtSystemChannel = 14
EVT_SYSTEM_PROPERTY_ID_EvtSystemComputer = 15
EVT_SYSTEM_PROPERTY_ID_EvtSystemUserID = 16
EVT_SYSTEM_PROPERTY_ID_EvtSystemVersion = 17
EVT_SYSTEM_PROPERTY_ID_EvtSystemPropertyIdEND = 18
def _define_EVT_VARIANT_head():
    class EVT_VARIANT(Structure):
        pass
    return EVT_VARIANT
def _define_EVT_VARIANT():
    EVT_VARIANT = win32more.System.EventLog.EVT_VARIANT_head
    class EVT_VARIANT__Anonymous_e__Union(Union):
        pass
    EVT_VARIANT__Anonymous_e__Union._fields_ = [
        ('BooleanVal', win32more.Foundation.BOOL),
        ('SByteVal', SByte),
        ('Int16Val', Int16),
        ('Int32Val', Int32),
        ('Int64Val', Int64),
        ('ByteVal', Byte),
        ('UInt16Val', UInt16),
        ('UInt32Val', UInt32),
        ('UInt64Val', UInt64),
        ('SingleVal', Single),
        ('DoubleVal', Double),
        ('FileTimeVal', UInt64),
        ('SysTimeVal', POINTER(win32more.Foundation.SYSTEMTIME_head)),
        ('GuidVal', POINTER(Guid)),
        ('StringVal', win32more.Foundation.PWSTR),
        ('AnsiStringVal', win32more.Foundation.PSTR),
        ('BinaryVal', c_char_p_no),
        ('SidVal', win32more.Foundation.PSID),
        ('SizeTVal', UIntPtr),
        ('BooleanArr', POINTER(win32more.Foundation.BOOL)),
        ('SByteArr', POINTER(SByte)),
        ('Int16Arr', POINTER(Int16)),
        ('Int32Arr', POINTER(Int32)),
        ('Int64Arr', POINTER(Int64)),
        ('ByteArr', c_char_p_no),
        ('UInt16Arr', POINTER(UInt16)),
        ('UInt32Arr', POINTER(UInt32)),
        ('UInt64Arr', POINTER(UInt64)),
        ('SingleArr', POINTER(Single)),
        ('DoubleArr', POINTER(Double)),
        ('FileTimeArr', POINTER(win32more.Foundation.FILETIME_head)),
        ('SysTimeArr', POINTER(win32more.Foundation.SYSTEMTIME_head)),
        ('GuidArr', POINTER(Guid)),
        ('StringArr', POINTER(win32more.Foundation.PWSTR)),
        ('AnsiStringArr', POINTER(win32more.Foundation.PSTR)),
        ('SidArr', POINTER(win32more.Foundation.PSID)),
        ('SizeTArr', POINTER(UIntPtr)),
        ('EvtHandleVal', win32more.System.EventLog.EVT_HANDLE),
        ('XmlVal', win32more.Foundation.PWSTR),
        ('XmlValArr', POINTER(win32more.Foundation.PWSTR)),
    ]
    EVT_VARIANT._anonymous_ = [
        'Anonymous',
    ]
    EVT_VARIANT._fields_ = [
        ('Anonymous', EVT_VARIANT__Anonymous_e__Union),
        ('Count', UInt32),
        ('Type', UInt32),
    ]
    return EVT_VARIANT
EVT_VARIANT_TYPE = Int32
EVT_VARIANT_TYPE_EvtVarTypeNull = 0
EVT_VARIANT_TYPE_EvtVarTypeString = 1
EVT_VARIANT_TYPE_EvtVarTypeAnsiString = 2
EVT_VARIANT_TYPE_EvtVarTypeSByte = 3
EVT_VARIANT_TYPE_EvtVarTypeByte = 4
EVT_VARIANT_TYPE_EvtVarTypeInt16 = 5
EVT_VARIANT_TYPE_EvtVarTypeUInt16 = 6
EVT_VARIANT_TYPE_EvtVarTypeInt32 = 7
EVT_VARIANT_TYPE_EvtVarTypeUInt32 = 8
EVT_VARIANT_TYPE_EvtVarTypeInt64 = 9
EVT_VARIANT_TYPE_EvtVarTypeUInt64 = 10
EVT_VARIANT_TYPE_EvtVarTypeSingle = 11
EVT_VARIANT_TYPE_EvtVarTypeDouble = 12
EVT_VARIANT_TYPE_EvtVarTypeBoolean = 13
EVT_VARIANT_TYPE_EvtVarTypeBinary = 14
EVT_VARIANT_TYPE_EvtVarTypeGuid = 15
EVT_VARIANT_TYPE_EvtVarTypeSizeT = 16
EVT_VARIANT_TYPE_EvtVarTypeFileTime = 17
EVT_VARIANT_TYPE_EvtVarTypeSysTime = 18
EVT_VARIANT_TYPE_EvtVarTypeSid = 19
EVT_VARIANT_TYPE_EvtVarTypeHexInt32 = 20
EVT_VARIANT_TYPE_EvtVarTypeHexInt64 = 21
EVT_VARIANT_TYPE_EvtVarTypeEvtHandle = 32
EVT_VARIANT_TYPE_EvtVarTypeEvtXml = 35
READ_EVENT_LOG_READ_FLAGS = UInt32
EVENTLOG_SEEK_READ = 2
EVENTLOG_SEQUENTIAL_READ = 1
REPORT_EVENT_TYPE = UInt16
EVENTLOG_SUCCESS = 0
EVENTLOG_AUDIT_FAILURE = 16
EVENTLOG_AUDIT_SUCCESS = 8
EVENTLOG_ERROR_TYPE = 1
EVENTLOG_INFORMATION_TYPE = 4
EVENTLOG_WARNING_TYPE = 2
__all__ = [
    "BackupEventLogA",
    "BackupEventLogW",
    "ClearEventLogA",
    "ClearEventLogW",
    "CloseEventLog",
    "DeregisterEventSource",
    "EVENTLOGRECORD",
    "EVENTLOG_AUDIT_FAILURE",
    "EVENTLOG_AUDIT_SUCCESS",
    "EVENTLOG_ERROR_TYPE",
    "EVENTLOG_FULL_INFORMATION",
    "EVENTLOG_INFORMATION_TYPE",
    "EVENTLOG_SEEK_READ",
    "EVENTLOG_SEQUENTIAL_READ",
    "EVENTLOG_SUCCESS",
    "EVENTLOG_WARNING_TYPE",
    "EVENTSFORLOGFILE",
    "EVT_ALL_ACCESS",
    "EVT_CHANNEL_CLOCK_TYPE",
    "EVT_CHANNEL_CLOCK_TYPE_EvtChannelClockTypeQPC",
    "EVT_CHANNEL_CLOCK_TYPE_EvtChannelClockTypeSystemTime",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigAccess",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigClassicEventlog",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigEnabled",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigIsolation",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigOwningPublisher",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigPropertyIdEND",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelConfigType",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigAutoBackup",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigLogFilePath",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigMaxSize",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelLoggingConfigRetention",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublisherList",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigBufferSize",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigClockType",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigControlGuid",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigFileMax",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigKeywords",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigLatency",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigLevel",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigMaxBuffers",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigMinBuffers",
    "EVT_CHANNEL_CONFIG_PROPERTY_ID_EvtChannelPublishingConfigSidType",
    "EVT_CHANNEL_ISOLATION_TYPE",
    "EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeApplication",
    "EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeCustom",
    "EVT_CHANNEL_ISOLATION_TYPE_EvtChannelIsolationTypeSystem",
    "EVT_CHANNEL_REFERENCE_FLAGS",
    "EVT_CHANNEL_REFERENCE_FLAGS_EvtChannelReferenceImported",
    "EVT_CHANNEL_SID_TYPE",
    "EVT_CHANNEL_SID_TYPE_EvtChannelSidTypeNone",
    "EVT_CHANNEL_SID_TYPE_EvtChannelSidTypePublishing",
    "EVT_CHANNEL_TYPE",
    "EVT_CHANNEL_TYPE_EvtChannelTypeAdmin",
    "EVT_CHANNEL_TYPE_EvtChannelTypeAnalytic",
    "EVT_CHANNEL_TYPE_EvtChannelTypeDebug",
    "EVT_CHANNEL_TYPE_EvtChannelTypeOperational",
    "EVT_CLEAR_ACCESS",
    "EVT_EVENT_METADATA_PROPERTY_ID",
    "EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventChannel",
    "EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventID",
    "EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventKeyword",
    "EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventLevel",
    "EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventMessageID",
    "EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventOpcode",
    "EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventTask",
    "EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventTemplate",
    "EVT_EVENT_METADATA_PROPERTY_ID_EventMetadataEventVersion",
    "EVT_EVENT_METADATA_PROPERTY_ID_EvtEventMetadataPropertyIdEND",
    "EVT_EVENT_PROPERTY_ID",
    "EVT_EVENT_PROPERTY_ID_EvtEventPath",
    "EVT_EVENT_PROPERTY_ID_EvtEventPropertyIdEND",
    "EVT_EVENT_PROPERTY_ID_EvtEventQueryIDs",
    "EVT_EXPORTLOG_FLAGS",
    "EVT_EXPORTLOG_FLAGS_EvtExportLogChannelPath",
    "EVT_EXPORTLOG_FLAGS_EvtExportLogFilePath",
    "EVT_EXPORTLOG_FLAGS_EvtExportLogOverwrite",
    "EVT_EXPORTLOG_FLAGS_EvtExportLogTolerateQueryErrors",
    "EVT_FORMAT_MESSAGE_FLAGS",
    "EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageChannel",
    "EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageEvent",
    "EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageId",
    "EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageKeyword",
    "EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageLevel",
    "EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageOpcode",
    "EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageProvider",
    "EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageTask",
    "EVT_FORMAT_MESSAGE_FLAGS_EvtFormatMessageXml",
    "EVT_HANDLE",
    "EVT_LOGIN_CLASS",
    "EVT_LOGIN_CLASS_EvtRpcLogin",
    "EVT_LOG_PROPERTY_ID",
    "EVT_LOG_PROPERTY_ID_EvtLogAttributes",
    "EVT_LOG_PROPERTY_ID_EvtLogCreationTime",
    "EVT_LOG_PROPERTY_ID_EvtLogFileSize",
    "EVT_LOG_PROPERTY_ID_EvtLogFull",
    "EVT_LOG_PROPERTY_ID_EvtLogLastAccessTime",
    "EVT_LOG_PROPERTY_ID_EvtLogLastWriteTime",
    "EVT_LOG_PROPERTY_ID_EvtLogNumberOfLogRecords",
    "EVT_LOG_PROPERTY_ID_EvtLogOldestRecordNumber",
    "EVT_OPEN_LOG_FLAGS",
    "EVT_OPEN_LOG_FLAGS_EvtOpenChannelPath",
    "EVT_OPEN_LOG_FLAGS_EvtOpenFilePath",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceFlags",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceID",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceIndex",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferenceMessageID",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferencePath",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataChannelReferences",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataHelpLink",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordMessageID",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordName",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywordValue",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataKeywords",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelMessageID",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelName",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevelValue",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataLevels",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataMessageFilePath",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeMessageID",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeName",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodeValue",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataOpcodes",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataParameterFilePath",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPropertyIdEND",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPublisherGuid",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataPublisherMessageID",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataResourceFilePath",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskEventGuid",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskMessageID",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskName",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTaskValue",
    "EVT_PUBLISHER_METADATA_PROPERTY_ID_EvtPublisherMetadataTasks",
    "EVT_QUERY_FLAGS",
    "EVT_QUERY_FLAGS_EvtQueryChannelPath",
    "EVT_QUERY_FLAGS_EvtQueryFilePath",
    "EVT_QUERY_FLAGS_EvtQueryForwardDirection",
    "EVT_QUERY_FLAGS_EvtQueryReverseDirection",
    "EVT_QUERY_FLAGS_EvtQueryTolerateQueryErrors",
    "EVT_QUERY_PROPERTY_ID",
    "EVT_QUERY_PROPERTY_ID_EvtQueryNames",
    "EVT_QUERY_PROPERTY_ID_EvtQueryPropertyIdEND",
    "EVT_QUERY_PROPERTY_ID_EvtQueryStatuses",
    "EVT_READ_ACCESS",
    "EVT_RENDER_CONTEXT_FLAGS",
    "EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextSystem",
    "EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextUser",
    "EVT_RENDER_CONTEXT_FLAGS_EvtRenderContextValues",
    "EVT_RENDER_FLAGS",
    "EVT_RENDER_FLAGS_EvtRenderBookmark",
    "EVT_RENDER_FLAGS_EvtRenderEventValues",
    "EVT_RENDER_FLAGS_EvtRenderEventXml",
    "EVT_RPC_LOGIN",
    "EVT_RPC_LOGIN_FLAGS",
    "EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthDefault",
    "EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthKerberos",
    "EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthNTLM",
    "EVT_RPC_LOGIN_FLAGS_EvtRpcLoginAuthNegotiate",
    "EVT_SEEK_FLAGS",
    "EVT_SEEK_FLAGS_EvtSeekOriginMask",
    "EVT_SEEK_FLAGS_EvtSeekRelativeToBookmark",
    "EVT_SEEK_FLAGS_EvtSeekRelativeToCurrent",
    "EVT_SEEK_FLAGS_EvtSeekRelativeToFirst",
    "EVT_SEEK_FLAGS_EvtSeekRelativeToLast",
    "EVT_SEEK_FLAGS_EvtSeekStrict",
    "EVT_SUBSCRIBE_CALLBACK",
    "EVT_SUBSCRIBE_FLAGS",
    "EVT_SUBSCRIBE_FLAGS_EvtSubscribeOriginMask",
    "EVT_SUBSCRIBE_FLAGS_EvtSubscribeStartAfterBookmark",
    "EVT_SUBSCRIBE_FLAGS_EvtSubscribeStartAtOldestRecord",
    "EVT_SUBSCRIBE_FLAGS_EvtSubscribeStrict",
    "EVT_SUBSCRIBE_FLAGS_EvtSubscribeToFutureEvents",
    "EVT_SUBSCRIBE_FLAGS_EvtSubscribeTolerateQueryErrors",
    "EVT_SUBSCRIBE_NOTIFY_ACTION",
    "EVT_SUBSCRIBE_NOTIFY_ACTION_EvtSubscribeActionDeliver",
    "EVT_SUBSCRIBE_NOTIFY_ACTION_EvtSubscribeActionError",
    "EVT_SYSTEM_PROPERTY_ID",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemActivityID",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemChannel",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemComputer",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemEventID",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemEventRecordId",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemKeywords",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemLevel",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemOpcode",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemProcessID",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemPropertyIdEND",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemProviderGuid",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemProviderName",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemQualifiers",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemRelatedActivityID",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemTask",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemThreadID",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemTimeCreated",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemUserID",
    "EVT_SYSTEM_PROPERTY_ID_EvtSystemVersion",
    "EVT_VARIANT",
    "EVT_VARIANT_TYPE",
    "EVT_VARIANT_TYPE_ARRAY",
    "EVT_VARIANT_TYPE_EvtVarTypeAnsiString",
    "EVT_VARIANT_TYPE_EvtVarTypeBinary",
    "EVT_VARIANT_TYPE_EvtVarTypeBoolean",
    "EVT_VARIANT_TYPE_EvtVarTypeByte",
    "EVT_VARIANT_TYPE_EvtVarTypeDouble",
    "EVT_VARIANT_TYPE_EvtVarTypeEvtHandle",
    "EVT_VARIANT_TYPE_EvtVarTypeEvtXml",
    "EVT_VARIANT_TYPE_EvtVarTypeFileTime",
    "EVT_VARIANT_TYPE_EvtVarTypeGuid",
    "EVT_VARIANT_TYPE_EvtVarTypeHexInt32",
    "EVT_VARIANT_TYPE_EvtVarTypeHexInt64",
    "EVT_VARIANT_TYPE_EvtVarTypeInt16",
    "EVT_VARIANT_TYPE_EvtVarTypeInt32",
    "EVT_VARIANT_TYPE_EvtVarTypeInt64",
    "EVT_VARIANT_TYPE_EvtVarTypeNull",
    "EVT_VARIANT_TYPE_EvtVarTypeSByte",
    "EVT_VARIANT_TYPE_EvtVarTypeSid",
    "EVT_VARIANT_TYPE_EvtVarTypeSingle",
    "EVT_VARIANT_TYPE_EvtVarTypeSizeT",
    "EVT_VARIANT_TYPE_EvtVarTypeString",
    "EVT_VARIANT_TYPE_EvtVarTypeSysTime",
    "EVT_VARIANT_TYPE_EvtVarTypeUInt16",
    "EVT_VARIANT_TYPE_EvtVarTypeUInt32",
    "EVT_VARIANT_TYPE_EvtVarTypeUInt64",
    "EVT_VARIANT_TYPE_MASK",
    "EVT_WRITE_ACCESS",
    "EventLogHandle",
    "EventSourceHandle",
    "EvtArchiveExportedLog",
    "EvtCancel",
    "EvtClearLog",
    "EvtClose",
    "EvtCreateBookmark",
    "EvtCreateRenderContext",
    "EvtExportLog",
    "EvtFormatMessage",
    "EvtGetChannelConfigProperty",
    "EvtGetEventInfo",
    "EvtGetEventMetadataProperty",
    "EvtGetExtendedStatus",
    "EvtGetLogInfo",
    "EvtGetObjectArrayProperty",
    "EvtGetObjectArraySize",
    "EvtGetPublisherMetadataProperty",
    "EvtGetQueryInfo",
    "EvtNext",
    "EvtNextChannelPath",
    "EvtNextEventMetadata",
    "EvtNextPublisherId",
    "EvtOpenChannelConfig",
    "EvtOpenChannelEnum",
    "EvtOpenEventMetadataEnum",
    "EvtOpenLog",
    "EvtOpenPublisherEnum",
    "EvtOpenPublisherMetadata",
    "EvtOpenSession",
    "EvtQuery",
    "EvtRender",
    "EvtSaveChannelConfig",
    "EvtSeek",
    "EvtSetChannelConfigProperty",
    "EvtSubscribe",
    "EvtUpdateBookmark",
    "GetEventLogInformation",
    "GetNumberOfEventLogRecords",
    "GetOldestEventLogRecord",
    "NotifyChangeEventLog",
    "OpenBackupEventLogA",
    "OpenBackupEventLogW",
    "OpenEventLogA",
    "OpenEventLogW",
    "READ_EVENT_LOG_READ_FLAGS",
    "REPORT_EVENT_TYPE",
    "ReadEventLogA",
    "ReadEventLogW",
    "RegisterEventSourceA",
    "RegisterEventSourceW",
    "ReportEventA",
    "ReportEventW",
]
