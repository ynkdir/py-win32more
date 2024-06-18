from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.DiagnosticDataQuery
@winfunctype('DiagnosticDataQuery.dll')
def DdqCreateSession(accessLevel: win32more.Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel, hSession: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqCloseSession(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetSessionAccessLevel(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, accessLevel: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticDataAccessLevelAllowed(accessLevel: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordStats(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, searchCriteria: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_SEARCH_CRITERIA), recordCount: POINTER(UInt32), minRowId: POINTER(Int64), maxRowId: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordPayload(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, rowId: Int64, payload: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordLocaleTags(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, locale: win32more.Windows.Win32.Foundation.PWSTR, hTagDescription: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordLocaleTags(hTagDescription: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordLocaleTagAtIndex(hTagDescription: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION, index: UInt32, tagDescription: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordLocaleTagCount(hTagDescription: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION, tagDescriptionCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducers(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, hProducerDescription: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordProducers(hProducerDescription: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducerAtIndex(hProducerDescription: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION, index: UInt32, producerDescription: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducerCount(hProducerDescription: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION, producerDescriptionCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducerCategories(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, producerName: win32more.Windows.Win32.Foundation.PWSTR, hCategoryDescription: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordProducerCategories(hCategoryDescription: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordCategoryAtIndex(hCategoryDescription: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION, index: UInt32, categoryDescription: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordCategoryCount(hCategoryDescription: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION, categoryDescriptionCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqIsDiagnosticRecordSampledIn(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, providerGroup: POINTER(Guid), providerId: POINTER(Guid), providerName: win32more.Windows.Win32.Foundation.PWSTR, eventId: POINTER(UInt32), eventName: win32more.Windows.Win32.Foundation.PWSTR, eventVersion: POINTER(UInt32), eventKeywords: POINTER(UInt64), isSampledIn: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordPage(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, searchCriteria: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_SEARCH_CRITERIA), offset: UInt32, pageRecordCount: UInt32, baseRowId: Int64, hRecord: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_RECORD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordPage(hRecord: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_RECORD) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordAtIndex(hRecord: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_RECORD, index: UInt32, record: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_RECORD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordCount(hRecord: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_RECORD, recordCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReportStoreReportCount(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, reportStoreType: UInt32, reportCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqCancelDiagnosticRecordOperation(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReport(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, reportStoreType: UInt32, hReport: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_REPORT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticReport(hReport: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_REPORT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReportAtIndex(hReport: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_REPORT, index: UInt32, report: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReportCount(hReport: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_REPORT, reportCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqExtractDiagnosticReport(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, reportStoreType: UInt32, reportKey: win32more.Windows.Win32.Foundation.PWSTR, destinationPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordTagDistribution(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, producerNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), producerNameCount: UInt32, tagStats: POINTER(POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TAG_STATS)), statCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordBinaryDistribution(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, producerNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), producerNameCount: UInt32, topNBinaries: UInt32, binaryStats: POINTER(POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_BINARY_STATS)), statCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordSummary(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, producerNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), producerNameCount: UInt32, generalStats: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_GENERAL_STATS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqSetTranscriptConfiguration(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, desiredConfig: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetTranscriptConfiguration(hSession: win32more.Windows.Win32.Security.DiagnosticDataQuery.HDIAGNOSTIC_DATA_QUERY_SESSION, currentConfig: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DIAGNOSTIC_DATA_EVENT_BINARY_STATS(Structure):
    moduleName: win32more.Windows.Win32.Foundation.PWSTR
    friendlyModuleName: win32more.Windows.Win32.Foundation.PWSTR
    eventCount: UInt32
    uploadSizeBytes: UInt64
class DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION(Structure):
    id: Int32
    name: win32more.Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION(Structure):
    name: win32more.Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION(Structure):
    privacyTag: Int32
    name: win32more.Windows.Win32.Foundation.PWSTR
    description: win32more.Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_EVENT_TAG_STATS(Structure):
    privacyTag: Int32
    eventCount: UInt32
class DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION(Structure):
    hoursOfHistoryToKeep: UInt32
    maxStoreMegabytes: UInt32
    requestedMaxStoreMegabytes: UInt32
class DIAGNOSTIC_DATA_GENERAL_STATS(Structure):
    optInLevel: UInt32
    transcriptSizeBytes: UInt64
    oldestEventTimestamp: UInt64
    totalEventCountLast24Hours: UInt32
    averageDailyEvents: Single
class DIAGNOSTIC_DATA_RECORD(Structure):
    rowId: Int64
    timestamp: UInt64
    eventKeywords: UInt64
    fullEventName: win32more.Windows.Win32.Foundation.PWSTR
    providerGroupGuid: win32more.Windows.Win32.Foundation.PWSTR
    producerName: win32more.Windows.Win32.Foundation.PWSTR
    privacyTags: POINTER(Int32)
    privacyTagCount: UInt32
    categoryIds: POINTER(Int32)
    categoryIdCount: UInt32
    isCoreData: win32more.Windows.Win32.Foundation.BOOL
    extra1: win32more.Windows.Win32.Foundation.PWSTR
    extra2: win32more.Windows.Win32.Foundation.PWSTR
    extra3: win32more.Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_SEARCH_CRITERIA(Structure):
    producerNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    producerNameCount: UInt32
    textToMatch: win32more.Windows.Win32.Foundation.PWSTR
    categoryIds: POINTER(Int32)
    categoryIdCount: UInt32
    privacyTags: POINTER(Int32)
    privacyTagCount: UInt32
    coreDataOnly: win32more.Windows.Win32.Foundation.BOOL
class DIAGNOSTIC_REPORT_DATA(Structure):
    signature: win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_SIGNATURE
    bucketId: Guid
    reportId: Guid
    creationTime: win32more.Windows.Win32.Foundation.FILETIME
    sizeInBytes: UInt64
    cabId: win32more.Windows.Win32.Foundation.PWSTR
    reportStatus: UInt32
    reportIntegratorId: Guid
    fileNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    fileCount: UInt32
    friendlyEventName: win32more.Windows.Win32.Foundation.PWSTR
    applicationName: win32more.Windows.Win32.Foundation.PWSTR
    applicationPath: win32more.Windows.Win32.Foundation.PWSTR
    description: win32more.Windows.Win32.Foundation.PWSTR
    bucketIdString: win32more.Windows.Win32.Foundation.PWSTR
    legacyBucketId: UInt64
    reportKey: win32more.Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_REPORT_PARAMETER(Structure):
    name: Char * 129
    value: Char * 260
class DIAGNOSTIC_REPORT_SIGNATURE(Structure):
    eventName: Char * 65
    parameters: win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_PARAMETER * 10
DdqAccessLevel = Int32
NoData: win32more.Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel = 0
CurrentUserData: win32more.Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel = 1
AllUserData: win32more.Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel = 2
HDIAGNOSTIC_DATA_QUERY_SESSION = VoidPtr
HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION = VoidPtr
HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION = VoidPtr
HDIAGNOSTIC_EVENT_TAG_DESCRIPTION = VoidPtr
HDIAGNOSTIC_RECORD = VoidPtr
HDIAGNOSTIC_REPORT = VoidPtr


make_ready(__name__)
