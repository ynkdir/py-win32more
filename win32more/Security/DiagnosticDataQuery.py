from win32more import *
import win32more.Security.DiagnosticDataQuery
import win32more.Foundation
import win32more.Security

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Security.DiagnosticDataQuery, name, eval(f"_define_{name}()"))
    return getattr(win32more.Security.DiagnosticDataQuery, name)
DdqAccessLevel = Int32
DdqAccessLevel_NoData = 0
DdqAccessLevel_CurrentUserData = 1
DdqAccessLevel_AllUserData = 2
def _define_DIAGNOSTIC_DATA_RECORD_head():
    class DIAGNOSTIC_DATA_RECORD(Structure):
        pass
    return DIAGNOSTIC_DATA_RECORD
def _define_DIAGNOSTIC_DATA_RECORD():
    DIAGNOSTIC_DATA_RECORD = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_RECORD_head
    DIAGNOSTIC_DATA_RECORD._fields_ = [
        ("rowId", Int64),
        ("timestamp", UInt64),
        ("eventKeywords", UInt64),
        ("fullEventName", win32more.Foundation.PWSTR),
        ("providerGroupGuid", win32more.Foundation.PWSTR),
        ("producerName", win32more.Foundation.PWSTR),
        ("privacyTags", POINTER(Int32)),
        ("privacyTagCount", UInt32),
        ("categoryIds", POINTER(Int32)),
        ("categoryIdCount", UInt32),
        ("isCoreData", win32more.Foundation.BOOL),
        ("extra1", win32more.Foundation.PWSTR),
        ("extra2", win32more.Foundation.PWSTR),
        ("extra3", win32more.Foundation.PWSTR),
    ]
    return DIAGNOSTIC_DATA_RECORD
def _define_DIAGNOSTIC_DATA_SEARCH_CRITERIA_head():
    class DIAGNOSTIC_DATA_SEARCH_CRITERIA(Structure):
        pass
    return DIAGNOSTIC_DATA_SEARCH_CRITERIA
def _define_DIAGNOSTIC_DATA_SEARCH_CRITERIA():
    DIAGNOSTIC_DATA_SEARCH_CRITERIA = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_SEARCH_CRITERIA_head
    DIAGNOSTIC_DATA_SEARCH_CRITERIA._fields_ = [
        ("producerNames", POINTER(win32more.Foundation.PWSTR)),
        ("producerNameCount", UInt32),
        ("textToMatch", win32more.Foundation.PWSTR),
        ("categoryIds", POINTER(Int32)),
        ("categoryIdCount", UInt32),
        ("privacyTags", POINTER(Int32)),
        ("privacyTagCount", UInt32),
        ("coreDataOnly", win32more.Foundation.BOOL),
    ]
    return DIAGNOSTIC_DATA_SEARCH_CRITERIA
def _define_DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION_head():
    class DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION(Structure):
        pass
    return DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION
def _define_DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION():
    DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION_head
    DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION._fields_ = [
        ("privacyTag", Int32),
        ("name", win32more.Foundation.PWSTR),
        ("description", win32more.Foundation.PWSTR),
    ]
    return DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION
def _define_DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION_head():
    class DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION(Structure):
        pass
    return DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION
def _define_DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION():
    DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION_head
    DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION._fields_ = [
        ("name", win32more.Foundation.PWSTR),
    ]
    return DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION
def _define_DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION_head():
    class DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION(Structure):
        pass
    return DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION
def _define_DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION():
    DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION_head
    DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION._fields_ = [
        ("id", Int32),
        ("name", win32more.Foundation.PWSTR),
    ]
    return DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION
def _define_DIAGNOSTIC_DATA_EVENT_TAG_STATS_head():
    class DIAGNOSTIC_DATA_EVENT_TAG_STATS(Structure):
        pass
    return DIAGNOSTIC_DATA_EVENT_TAG_STATS
def _define_DIAGNOSTIC_DATA_EVENT_TAG_STATS():
    DIAGNOSTIC_DATA_EVENT_TAG_STATS = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TAG_STATS_head
    DIAGNOSTIC_DATA_EVENT_TAG_STATS._fields_ = [
        ("privacyTag", Int32),
        ("eventCount", UInt32),
    ]
    return DIAGNOSTIC_DATA_EVENT_TAG_STATS
def _define_DIAGNOSTIC_DATA_EVENT_BINARY_STATS_head():
    class DIAGNOSTIC_DATA_EVENT_BINARY_STATS(Structure):
        pass
    return DIAGNOSTIC_DATA_EVENT_BINARY_STATS
def _define_DIAGNOSTIC_DATA_EVENT_BINARY_STATS():
    DIAGNOSTIC_DATA_EVENT_BINARY_STATS = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_BINARY_STATS_head
    DIAGNOSTIC_DATA_EVENT_BINARY_STATS._fields_ = [
        ("moduleName", win32more.Foundation.PWSTR),
        ("friendlyModuleName", win32more.Foundation.PWSTR),
        ("eventCount", UInt32),
        ("uploadSizeBytes", UInt64),
    ]
    return DIAGNOSTIC_DATA_EVENT_BINARY_STATS
def _define_DIAGNOSTIC_DATA_GENERAL_STATS_head():
    class DIAGNOSTIC_DATA_GENERAL_STATS(Structure):
        pass
    return DIAGNOSTIC_DATA_GENERAL_STATS
def _define_DIAGNOSTIC_DATA_GENERAL_STATS():
    DIAGNOSTIC_DATA_GENERAL_STATS = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_GENERAL_STATS_head
    DIAGNOSTIC_DATA_GENERAL_STATS._fields_ = [
        ("optInLevel", UInt32),
        ("transcriptSizeBytes", UInt64),
        ("oldestEventTimestamp", UInt64),
        ("totalEventCountLast24Hours", UInt32),
        ("averageDailyEvents", Single),
    ]
    return DIAGNOSTIC_DATA_GENERAL_STATS
def _define_DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION_head():
    class DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION(Structure):
        pass
    return DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION
def _define_DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION():
    DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION_head
    DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION._fields_ = [
        ("hoursOfHistoryToKeep", UInt32),
        ("maxStoreMegabytes", UInt32),
        ("requestedMaxStoreMegabytes", UInt32),
    ]
    return DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION
def _define_DIAGNOSTIC_REPORT_PARAMETER_head():
    class DIAGNOSTIC_REPORT_PARAMETER(Structure):
        pass
    return DIAGNOSTIC_REPORT_PARAMETER
def _define_DIAGNOSTIC_REPORT_PARAMETER():
    DIAGNOSTIC_REPORT_PARAMETER = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_PARAMETER_head
    DIAGNOSTIC_REPORT_PARAMETER._fields_ = [
        ("name", Char * 129),
        ("value", Char * 260),
    ]
    return DIAGNOSTIC_REPORT_PARAMETER
def _define_DIAGNOSTIC_REPORT_SIGNATURE_head():
    class DIAGNOSTIC_REPORT_SIGNATURE(Structure):
        pass
    return DIAGNOSTIC_REPORT_SIGNATURE
def _define_DIAGNOSTIC_REPORT_SIGNATURE():
    DIAGNOSTIC_REPORT_SIGNATURE = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_SIGNATURE_head
    DIAGNOSTIC_REPORT_SIGNATURE._fields_ = [
        ("eventName", Char * 65),
        ("parameters", win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_PARAMETER * 10),
    ]
    return DIAGNOSTIC_REPORT_SIGNATURE
def _define_DIAGNOSTIC_REPORT_DATA_head():
    class DIAGNOSTIC_REPORT_DATA(Structure):
        pass
    return DIAGNOSTIC_REPORT_DATA
def _define_DIAGNOSTIC_REPORT_DATA():
    DIAGNOSTIC_REPORT_DATA = win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_DATA_head
    DIAGNOSTIC_REPORT_DATA._fields_ = [
        ("signature", win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_SIGNATURE),
        ("bucketId", Guid),
        ("reportId", Guid),
        ("creationTime", win32more.Foundation.FILETIME),
        ("sizeInBytes", UInt64),
        ("cabId", win32more.Foundation.PWSTR),
        ("reportStatus", UInt32),
        ("reportIntegratorId", Guid),
        ("fileNames", POINTER(win32more.Foundation.PWSTR)),
        ("fileCount", UInt32),
        ("friendlyEventName", win32more.Foundation.PWSTR),
        ("applicationName", win32more.Foundation.PWSTR),
        ("applicationPath", win32more.Foundation.PWSTR),
        ("description", win32more.Foundation.PWSTR),
        ("bucketIdString", win32more.Foundation.PWSTR),
        ("legacyBucketId", UInt64),
        ("reportKey", win32more.Foundation.PWSTR),
    ]
    return DIAGNOSTIC_REPORT_DATA
def _define_DdqCreateSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.DiagnosticDataQuery.DdqAccessLevel,POINTER(win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION), use_last_error=False)(("DdqCreateSession", windll["DiagnosticDataQuery"]), ((1, 'accessLevel'),(1, 'hSession'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqCloseSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, use_last_error=False)(("DdqCloseSession", windll["DiagnosticDataQuery"]), ((1, 'hSession'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetSessionAccessLevel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,POINTER(win32more.Security.DiagnosticDataQuery.DdqAccessLevel), use_last_error=False)(("DdqGetSessionAccessLevel", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'accessLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticDataAccessLevelAllowed():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.DiagnosticDataQuery.DdqAccessLevel), use_last_error=False)(("DdqGetDiagnosticDataAccessLevelAllowed", windll["DiagnosticDataQuery"]), ((1, 'accessLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordStats():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_SEARCH_CRITERIA_head),POINTER(UInt32),POINTER(Int64),POINTER(Int64), use_last_error=False)(("DdqGetDiagnosticRecordStats", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'searchCriteria'),(1, 'recordCount'),(1, 'minRowId'),(1, 'maxRowId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordPayload():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,Int64,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("DdqGetDiagnosticRecordPayload", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'rowId'),(1, 'payload'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordLocaleTags():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,win32more.Foundation.PWSTR,POINTER(win32more.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION), use_last_error=False)(("DdqGetDiagnosticRecordLocaleTags", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'locale'),(1, 'hTagDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqFreeDiagnosticRecordLocaleTags():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION, use_last_error=False)(("DdqFreeDiagnosticRecordLocaleTags", windll["DiagnosticDataQuery"]), ((1, 'hTagDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordLocaleTagAtIndex():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION,UInt32,POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION_head), use_last_error=False)(("DdqGetDiagnosticRecordLocaleTagAtIndex", windll["DiagnosticDataQuery"]), ((1, 'hTagDescription'),(1, 'index'),(1, 'tagDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordLocaleTagCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION,POINTER(UInt32), use_last_error=False)(("DdqGetDiagnosticRecordLocaleTagCount", windll["DiagnosticDataQuery"]), ((1, 'hTagDescription'),(1, 'tagDescriptionCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordProducers():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,POINTER(win32more.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION), use_last_error=False)(("DdqGetDiagnosticRecordProducers", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'hProducerDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqFreeDiagnosticRecordProducers():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION, use_last_error=False)(("DdqFreeDiagnosticRecordProducers", windll["DiagnosticDataQuery"]), ((1, 'hProducerDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordProducerAtIndex():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION,UInt32,POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION_head), use_last_error=False)(("DdqGetDiagnosticRecordProducerAtIndex", windll["DiagnosticDataQuery"]), ((1, 'hProducerDescription'),(1, 'index'),(1, 'producerDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordProducerCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION,POINTER(UInt32), use_last_error=False)(("DdqGetDiagnosticRecordProducerCount", windll["DiagnosticDataQuery"]), ((1, 'hProducerDescription'),(1, 'producerDescriptionCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordProducerCategories():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,win32more.Foundation.PWSTR,POINTER(win32more.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION), use_last_error=False)(("DdqGetDiagnosticRecordProducerCategories", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'producerName'),(1, 'hCategoryDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqFreeDiagnosticRecordProducerCategories():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION, use_last_error=False)(("DdqFreeDiagnosticRecordProducerCategories", windll["DiagnosticDataQuery"]), ((1, 'hCategoryDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordCategoryAtIndex():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION,UInt32,POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION_head), use_last_error=False)(("DdqGetDiagnosticRecordCategoryAtIndex", windll["DiagnosticDataQuery"]), ((1, 'hCategoryDescription'),(1, 'index'),(1, 'categoryDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordCategoryCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION,POINTER(UInt32), use_last_error=False)(("DdqGetDiagnosticRecordCategoryCount", windll["DiagnosticDataQuery"]), ((1, 'hCategoryDescription'),(1, 'categoryDescriptionCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqIsDiagnosticRecordSampledIn():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,POINTER(Guid),POINTER(Guid),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt64),POINTER(win32more.Foundation.BOOL), use_last_error=False)(("DdqIsDiagnosticRecordSampledIn", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'providerGroup'),(1, 'providerId'),(1, 'providerName'),(1, 'eventId'),(1, 'eventName'),(1, 'eventVersion'),(1, 'eventKeywords'),(1, 'isSampledIn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordPage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_SEARCH_CRITERIA_head),UInt32,UInt32,Int64,POINTER(win32more.Security.HDIAGNOSTIC_RECORD), use_last_error=False)(("DdqGetDiagnosticRecordPage", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'searchCriteria'),(1, 'offset'),(1, 'pageRecordCount'),(1, 'baseRowId'),(1, 'hRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqFreeDiagnosticRecordPage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_RECORD, use_last_error=False)(("DdqFreeDiagnosticRecordPage", windll["DiagnosticDataQuery"]), ((1, 'hRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordAtIndex():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_RECORD,UInt32,POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_RECORD_head), use_last_error=False)(("DdqGetDiagnosticRecordAtIndex", windll["DiagnosticDataQuery"]), ((1, 'hRecord'),(1, 'index'),(1, 'record'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_RECORD,POINTER(UInt32), use_last_error=False)(("DdqGetDiagnosticRecordCount", windll["DiagnosticDataQuery"]), ((1, 'hRecord'),(1, 'recordCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticReportStoreReportCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,UInt32,POINTER(UInt32), use_last_error=False)(("DdqGetDiagnosticReportStoreReportCount", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'reportStoreType'),(1, 'reportCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqCancelDiagnosticRecordOperation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, use_last_error=False)(("DdqCancelDiagnosticRecordOperation", windll["DiagnosticDataQuery"]), ((1, 'hSession'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticReport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,UInt32,POINTER(win32more.Security.HDIAGNOSTIC_REPORT), use_last_error=False)(("DdqGetDiagnosticReport", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'reportStoreType'),(1, 'hReport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqFreeDiagnosticReport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_REPORT, use_last_error=False)(("DdqFreeDiagnosticReport", windll["DiagnosticDataQuery"]), ((1, 'hReport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticReportAtIndex():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_REPORT,UInt32,POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_DATA_head), use_last_error=False)(("DdqGetDiagnosticReportAtIndex", windll["DiagnosticDataQuery"]), ((1, 'hReport'),(1, 'index'),(1, 'report'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticReportCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_REPORT,POINTER(UInt32), use_last_error=False)(("DdqGetDiagnosticReportCount", windll["DiagnosticDataQuery"]), ((1, 'hReport'),(1, 'reportCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqExtractDiagnosticReport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DdqExtractDiagnosticReport", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'reportStoreType'),(1, 'reportKey'),(1, 'destinationPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordTagDistribution():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TAG_STATS_head)),POINTER(UInt32), use_last_error=False)(("DdqGetDiagnosticRecordTagDistribution", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'producerNames'),(1, 'producerNameCount'),(1, 'tagStats'),(1, 'statCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordBinaryDistribution():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,POINTER(win32more.Foundation.PWSTR),UInt32,UInt32,POINTER(POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_BINARY_STATS_head)),POINTER(UInt32), use_last_error=False)(("DdqGetDiagnosticRecordBinaryDistribution", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'producerNames'),(1, 'producerNameCount'),(1, 'topNBinaries'),(1, 'binaryStats'),(1, 'statCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetDiagnosticRecordSummary():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_GENERAL_STATS_head), use_last_error=False)(("DdqGetDiagnosticRecordSummary", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'producerNames'),(1, 'producerNameCount'),(1, 'generalStats'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqSetTranscriptConfiguration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION_head), use_last_error=False)(("DdqSetTranscriptConfiguration", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'desiredConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdqGetTranscriptConfiguration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.HDIAGNOSTIC_DATA_QUERY_SESSION,POINTER(win32more.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION_head), use_last_error=False)(("DdqGetTranscriptConfiguration", windll["DiagnosticDataQuery"]), ((1, 'hSession'),(1, 'currentConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DdqAccessLevel",
    "DdqAccessLevel_NoData",
    "DdqAccessLevel_CurrentUserData",
    "DdqAccessLevel_AllUserData",
    "DIAGNOSTIC_DATA_RECORD",
    "DIAGNOSTIC_DATA_SEARCH_CRITERIA",
    "DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION",
    "DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION",
    "DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION",
    "DIAGNOSTIC_DATA_EVENT_TAG_STATS",
    "DIAGNOSTIC_DATA_EVENT_BINARY_STATS",
    "DIAGNOSTIC_DATA_GENERAL_STATS",
    "DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION",
    "DIAGNOSTIC_REPORT_PARAMETER",
    "DIAGNOSTIC_REPORT_SIGNATURE",
    "DIAGNOSTIC_REPORT_DATA",
    "DdqCreateSession",
    "DdqCloseSession",
    "DdqGetSessionAccessLevel",
    "DdqGetDiagnosticDataAccessLevelAllowed",
    "DdqGetDiagnosticRecordStats",
    "DdqGetDiagnosticRecordPayload",
    "DdqGetDiagnosticRecordLocaleTags",
    "DdqFreeDiagnosticRecordLocaleTags",
    "DdqGetDiagnosticRecordLocaleTagAtIndex",
    "DdqGetDiagnosticRecordLocaleTagCount",
    "DdqGetDiagnosticRecordProducers",
    "DdqFreeDiagnosticRecordProducers",
    "DdqGetDiagnosticRecordProducerAtIndex",
    "DdqGetDiagnosticRecordProducerCount",
    "DdqGetDiagnosticRecordProducerCategories",
    "DdqFreeDiagnosticRecordProducerCategories",
    "DdqGetDiagnosticRecordCategoryAtIndex",
    "DdqGetDiagnosticRecordCategoryCount",
    "DdqIsDiagnosticRecordSampledIn",
    "DdqGetDiagnosticRecordPage",
    "DdqFreeDiagnosticRecordPage",
    "DdqGetDiagnosticRecordAtIndex",
    "DdqGetDiagnosticRecordCount",
    "DdqGetDiagnosticReportStoreReportCount",
    "DdqCancelDiagnosticRecordOperation",
    "DdqGetDiagnosticReport",
    "DdqFreeDiagnosticReport",
    "DdqGetDiagnosticReportAtIndex",
    "DdqGetDiagnosticReportCount",
    "DdqExtractDiagnosticReport",
    "DdqGetDiagnosticRecordTagDistribution",
    "DdqGetDiagnosticRecordBinaryDistribution",
    "DdqGetDiagnosticRecordSummary",
    "DdqSetTranscriptConfiguration",
    "DdqGetTranscriptConfiguration",
]
