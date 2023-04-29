from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Security.DiagnosticDataQuery
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('DiagnosticDataQuery.dll')
def DdqCreateSession(accessLevel: Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel, hSession: POINTER(Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqCloseSession(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetSessionAccessLevel(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, accessLevel: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticDataAccessLevelAllowed(accessLevel: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordStats(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, searchCriteria: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_SEARCH_CRITERIA_head), recordCount: POINTER(UInt32), minRowId: POINTER(Int64), maxRowId: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordPayload(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, rowId: Int64, payload: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordLocaleTags(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, locale: Windows.Win32.Foundation.PWSTR, hTagDescription: POINTER(Windows.Win32.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordLocaleTags(hTagDescription: Windows.Win32.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordLocaleTagAtIndex(hTagDescription: Windows.Win32.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION, index: UInt32, tagDescription: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordLocaleTagCount(hTagDescription: Windows.Win32.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION, tagDescriptionCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducers(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, hProducerDescription: POINTER(Windows.Win32.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordProducers(hProducerDescription: Windows.Win32.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducerAtIndex(hProducerDescription: Windows.Win32.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION, index: UInt32, producerDescription: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducerCount(hProducerDescription: Windows.Win32.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION, producerDescriptionCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducerCategories(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, producerName: Windows.Win32.Foundation.PWSTR, hCategoryDescription: POINTER(Windows.Win32.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordProducerCategories(hCategoryDescription: Windows.Win32.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordCategoryAtIndex(hCategoryDescription: Windows.Win32.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION, index: UInt32, categoryDescription: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordCategoryCount(hCategoryDescription: Windows.Win32.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION, categoryDescriptionCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqIsDiagnosticRecordSampledIn(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, providerGroup: POINTER(Guid), providerId: POINTER(Guid), providerName: Windows.Win32.Foundation.PWSTR, eventId: POINTER(UInt32), eventName: Windows.Win32.Foundation.PWSTR, eventVersion: POINTER(UInt32), eventKeywords: POINTER(UInt64), isSampledIn: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordPage(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, searchCriteria: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_SEARCH_CRITERIA_head), offset: UInt32, pageRecordCount: UInt32, baseRowId: Int64, hRecord: POINTER(Windows.Win32.Security.HDIAGNOSTIC_RECORD)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordPage(hRecord: Windows.Win32.Security.HDIAGNOSTIC_RECORD) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordAtIndex(hRecord: Windows.Win32.Security.HDIAGNOSTIC_RECORD, index: UInt32, record: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_RECORD_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordCount(hRecord: Windows.Win32.Security.HDIAGNOSTIC_RECORD, recordCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReportStoreReportCount(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, reportStoreType: UInt32, reportCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqCancelDiagnosticRecordOperation(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReport(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, reportStoreType: UInt32, hReport: POINTER(Windows.Win32.Security.HDIAGNOSTIC_REPORT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticReport(hReport: Windows.Win32.Security.HDIAGNOSTIC_REPORT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReportAtIndex(hReport: Windows.Win32.Security.HDIAGNOSTIC_REPORT, index: UInt32, report: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReportCount(hReport: Windows.Win32.Security.HDIAGNOSTIC_REPORT, reportCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqExtractDiagnosticReport(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, reportStoreType: UInt32, reportKey: Windows.Win32.Foundation.PWSTR, destinationPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordTagDistribution(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, producerNames: POINTER(Windows.Win32.Foundation.PWSTR), producerNameCount: UInt32, tagStats: POINTER(POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TAG_STATS_head)), statCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordBinaryDistribution(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, producerNames: POINTER(Windows.Win32.Foundation.PWSTR), producerNameCount: UInt32, topNBinaries: UInt32, binaryStats: POINTER(POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_BINARY_STATS_head)), statCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordSummary(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, producerNames: POINTER(Windows.Win32.Foundation.PWSTR), producerNameCount: UInt32, generalStats: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_GENERAL_STATS_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqSetTranscriptConfiguration(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, desiredConfig: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetTranscriptConfiguration(hSession: Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, currentConfig: POINTER(Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
class DIAGNOSTIC_DATA_EVENT_BINARY_STATS(EasyCastStructure):
    moduleName: Windows.Win32.Foundation.PWSTR
    friendlyModuleName: Windows.Win32.Foundation.PWSTR
    eventCount: UInt32
    uploadSizeBytes: UInt64
class DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION(EasyCastStructure):
    id: Int32
    name: Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION(EasyCastStructure):
    name: Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION(EasyCastStructure):
    privacyTag: Int32
    name: Windows.Win32.Foundation.PWSTR
    description: Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_EVENT_TAG_STATS(EasyCastStructure):
    privacyTag: Int32
    eventCount: UInt32
class DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION(EasyCastStructure):
    hoursOfHistoryToKeep: UInt32
    maxStoreMegabytes: UInt32
    requestedMaxStoreMegabytes: UInt32
class DIAGNOSTIC_DATA_GENERAL_STATS(EasyCastStructure):
    optInLevel: UInt32
    transcriptSizeBytes: UInt64
    oldestEventTimestamp: UInt64
    totalEventCountLast24Hours: UInt32
    averageDailyEvents: Single
class DIAGNOSTIC_DATA_RECORD(EasyCastStructure):
    rowId: Int64
    timestamp: UInt64
    eventKeywords: UInt64
    fullEventName: Windows.Win32.Foundation.PWSTR
    providerGroupGuid: Windows.Win32.Foundation.PWSTR
    producerName: Windows.Win32.Foundation.PWSTR
    privacyTags: POINTER(Int32)
    privacyTagCount: UInt32
    categoryIds: POINTER(Int32)
    categoryIdCount: UInt32
    isCoreData: Windows.Win32.Foundation.BOOL
    extra1: Windows.Win32.Foundation.PWSTR
    extra2: Windows.Win32.Foundation.PWSTR
    extra3: Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_SEARCH_CRITERIA(EasyCastStructure):
    producerNames: POINTER(Windows.Win32.Foundation.PWSTR)
    producerNameCount: UInt32
    textToMatch: Windows.Win32.Foundation.PWSTR
    categoryIds: POINTER(Int32)
    categoryIdCount: UInt32
    privacyTags: POINTER(Int32)
    privacyTagCount: UInt32
    coreDataOnly: Windows.Win32.Foundation.BOOL
class DIAGNOSTIC_REPORT_DATA(EasyCastStructure):
    signature: Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_SIGNATURE
    bucketId: Guid
    reportId: Guid
    creationTime: Windows.Win32.Foundation.FILETIME
    sizeInBytes: UInt64
    cabId: Windows.Win32.Foundation.PWSTR
    reportStatus: UInt32
    reportIntegratorId: Guid
    fileNames: POINTER(Windows.Win32.Foundation.PWSTR)
    fileCount: UInt32
    friendlyEventName: Windows.Win32.Foundation.PWSTR
    applicationName: Windows.Win32.Foundation.PWSTR
    applicationPath: Windows.Win32.Foundation.PWSTR
    description: Windows.Win32.Foundation.PWSTR
    bucketIdString: Windows.Win32.Foundation.PWSTR
    legacyBucketId: UInt64
    reportKey: Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_REPORT_PARAMETER(EasyCastStructure):
    name: Char * 129
    value: Char * 260
class DIAGNOSTIC_REPORT_SIGNATURE(EasyCastStructure):
    eventName: Char * 65
    parameters: Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_PARAMETER * 10
DdqAccessLevel = Int32
DdqAccessLevel_NoData: DdqAccessLevel = 0
DdqAccessLevel_CurrentUserData: DdqAccessLevel = 1
DdqAccessLevel_AllUserData: DdqAccessLevel = 2
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_BINARY_STATS')
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION')
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION')
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION')
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_TAG_STATS')
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION')
make_head(_module, 'DIAGNOSTIC_DATA_GENERAL_STATS')
make_head(_module, 'DIAGNOSTIC_DATA_RECORD')
make_head(_module, 'DIAGNOSTIC_DATA_SEARCH_CRITERIA')
make_head(_module, 'DIAGNOSTIC_REPORT_DATA')
make_head(_module, 'DIAGNOSTIC_REPORT_PARAMETER')
make_head(_module, 'DIAGNOSTIC_REPORT_SIGNATURE')
