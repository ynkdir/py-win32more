from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.WindowsSync
import win32more.UI.Shell.PropertiesSystem

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
SYNC_VERSION_FLAG_FROM_FEED = 1
SYNC_VERSION_FLAG_HAS_BY = 2
SYNC_SERIALIZE_REPLICA_KEY_MAP = 1
SYNC_FILTER_INFO_FLAG_ITEM_LIST = 1
SYNC_FILTER_INFO_FLAG_CHANGE_UNIT_LIST = 2
SYNC_FILTER_INFO_FLAG_CUSTOM = 4
SYNC_FILTER_INFO_COMBINED = 8
SYNC_CHANGE_FLAG_DELETED = 1
SYNC_CHANGE_FLAG_DOES_NOT_EXIST = 2
SYNC_CHANGE_FLAG_GHOST = 4
PKEY_PROVIDER_INSTANCEID = PROPERTYKEY(Fmtid='84179e61-60f6-4c1c-88ed-f1c531b32bda', Pid=2)
PKEY_PROVIDER_CLSID = PROPERTYKEY(Fmtid='84179e61-60f6-4c1c-88ed-f1c531b32bda', Pid=3)
PKEY_PROVIDER_CONFIGUI = PROPERTYKEY(Fmtid='84179e61-60f6-4c1c-88ed-f1c531b32bda', Pid=4)
PKEY_PROVIDER_CONTENTTYPE = PROPERTYKEY(Fmtid='84179e61-60f6-4c1c-88ed-f1c531b32bda', Pid=5)
PKEY_PROVIDER_CAPABILITIES = PROPERTYKEY(Fmtid='84179e61-60f6-4c1c-88ed-f1c531b32bda', Pid=6)
PKEY_PROVIDER_SUPPORTED_ARCHITECTURE = PROPERTYKEY(Fmtid='84179e61-60f6-4c1c-88ed-f1c531b32bda', Pid=7)
PKEY_PROVIDER_NAME = PROPERTYKEY(Fmtid='84179e61-60f6-4c1c-88ed-f1c531b32bda', Pid=8)
PKEY_PROVIDER_DESCRIPTION = PROPERTYKEY(Fmtid='84179e61-60f6-4c1c-88ed-f1c531b32bda', Pid=9)
PKEY_PROVIDER_TOOLTIPS = PROPERTYKEY(Fmtid='84179e61-60f6-4c1c-88ed-f1c531b32bda', Pid=10)
PKEY_PROVIDER_ICON = PROPERTYKEY(Fmtid='84179e61-60f6-4c1c-88ed-f1c531b32bda', Pid=11)
PKEY_CONFIGUI_INSTANCEID = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=2)
PKEY_CONFIGUI_CLSID = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=3)
PKEY_CONFIGUI_CONTENTTYPE = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=4)
PKEY_CONFIGUI_CAPABILITIES = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=5)
PKEY_CONFIGUI_SUPPORTED_ARCHITECTURE = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=6)
PKEY_CONFIGUI_IS_GLOBAL = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=7)
PKEY_CONFIGUI_NAME = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=8)
PKEY_CONFIGUI_DESCRIPTION = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=9)
PKEY_CONFIGUI_TOOLTIPS = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=10)
PKEY_CONFIGUI_ICON = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=11)
PKEY_CONFIGUI_MENUITEM_NOUI = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=12)
PKEY_CONFIGUI_MENUITEM = PROPERTYKEY(Fmtid='554b24ea-e8e3-45ba-9352-dfb561e171e4', Pid=13)
def _define_ID_PARAMETER_PAIR_head():
    class ID_PARAMETER_PAIR(Structure):
        pass
    return ID_PARAMETER_PAIR
def _define_ID_PARAMETER_PAIR():
    ID_PARAMETER_PAIR = win32more.System.WindowsSync.ID_PARAMETER_PAIR_head
    ID_PARAMETER_PAIR._fields_ = [
        ("fIsVariable", win32more.Foundation.BOOL),
        ("cbIdSize", UInt16),
    ]
    return ID_PARAMETER_PAIR
def _define_ID_PARAMETERS_head():
    class ID_PARAMETERS(Structure):
        pass
    return ID_PARAMETERS
def _define_ID_PARAMETERS():
    ID_PARAMETERS = win32more.System.WindowsSync.ID_PARAMETERS_head
    ID_PARAMETERS._fields_ = [
        ("dwSize", UInt32),
        ("replicaId", win32more.System.WindowsSync.ID_PARAMETER_PAIR),
        ("itemId", win32more.System.WindowsSync.ID_PARAMETER_PAIR),
        ("changeUnitId", win32more.System.WindowsSync.ID_PARAMETER_PAIR),
    ]
    return ID_PARAMETERS
def _define_SYNC_SESSION_STATISTICS_head():
    class SYNC_SESSION_STATISTICS(Structure):
        pass
    return SYNC_SESSION_STATISTICS
def _define_SYNC_SESSION_STATISTICS():
    SYNC_SESSION_STATISTICS = win32more.System.WindowsSync.SYNC_SESSION_STATISTICS_head
    SYNC_SESSION_STATISTICS._fields_ = [
        ("dwChangesApplied", UInt32),
        ("dwChangesFailed", UInt32),
    ]
    return SYNC_SESSION_STATISTICS
def _define_SYNC_VERSION_head():
    class SYNC_VERSION(Structure):
        pass
    return SYNC_VERSION
def _define_SYNC_VERSION():
    SYNC_VERSION = win32more.System.WindowsSync.SYNC_VERSION_head
    SYNC_VERSION._fields_ = [
        ("dwLastUpdatingReplicaKey", UInt32),
        ("ullTickCount", UInt64),
    ]
    return SYNC_VERSION
def _define_SYNC_RANGE_head():
    class SYNC_RANGE(Structure):
        pass
    return SYNC_RANGE
def _define_SYNC_RANGE():
    SYNC_RANGE = win32more.System.WindowsSync.SYNC_RANGE_head
    SYNC_RANGE._fields_ = [
        ("pbClosedLowerBound", c_char_p_no),
        ("pbClosedUpperBound", c_char_p_no),
    ]
    return SYNC_RANGE
def _define_SYNC_TIME_head():
    class SYNC_TIME(Structure):
        pass
    return SYNC_TIME
def _define_SYNC_TIME():
    SYNC_TIME = win32more.System.WindowsSync.SYNC_TIME_head
    SYNC_TIME._fields_ = [
        ("dwDate", UInt32),
        ("dwTime", UInt32),
    ]
    return SYNC_TIME
def _define_SYNC_FILTER_CHANGE_head():
    class SYNC_FILTER_CHANGE(Structure):
        pass
    return SYNC_FILTER_CHANGE
def _define_SYNC_FILTER_CHANGE():
    SYNC_FILTER_CHANGE = win32more.System.WindowsSync.SYNC_FILTER_CHANGE_head
    SYNC_FILTER_CHANGE._fields_ = [
        ("fMoveIn", win32more.Foundation.BOOL),
        ("moveVersion", win32more.System.WindowsSync.SYNC_VERSION),
    ]
    return SYNC_FILTER_CHANGE
SYNC_PROVIDER_ROLE = Int32
SPR_SOURCE = 0
SPR_DESTINATION = 1
CONFLICT_RESOLUTION_POLICY = Int32
CRP_NONE = 0
CRP_DESTINATION_PROVIDER_WINS = 1
CRP_SOURCE_PROVIDER_WINS = 2
CRP_LAST = 3
SYNC_PROGRESS_STAGE = Int32
SPS_CHANGE_DETECTION = 0
SPS_CHANGE_ENUMERATION = 1
SPS_CHANGE_APPLICATION = 2
SYNC_FULL_ENUMERATION_ACTION = Int32
SFEA_FULL_ENUMERATION = 0
SFEA_PARTIAL_SYNC = 1
SFEA_ABORT = 2
SYNC_RESOLVE_ACTION = Int32
SRA_DEFER = 0
SRA_ACCEPT_DESTINATION_PROVIDER = 1
SRA_ACCEPT_SOURCE_PROVIDER = 2
SRA_MERGE = 3
SRA_TRANSFER_AND_DEFER = 4
SRA_LAST = 5
SYNC_STATISTICS = Int32
SYNC_STATISTICS_RANGE_COUNT = 0
SYNC_SERIALIZATION_VERSION = Int32
SYNC_SERIALIZATION_VERSION_V1 = 1
SYNC_SERIALIZATION_VERSION_V2 = 4
SYNC_SERIALIZATION_VERSION_V3 = 5
FILTERING_TYPE = Int32
FT_CURRENT_ITEMS_ONLY = 0
FT_CURRENT_ITEMS_AND_VERSIONS_FOR_MOVED_OUT_ITEMS = 1
SYNC_CONSTRAINT_RESOLVE_ACTION = Int32
SCRA_DEFER = 0
SCRA_ACCEPT_DESTINATION_PROVIDER = 1
SCRA_ACCEPT_SOURCE_PROVIDER = 2
SCRA_TRANSFER_AND_DEFER = 3
SCRA_MERGE = 4
SCRA_RENAME_SOURCE = 5
SCRA_RENAME_DESTINATION = 6
CONSTRAINT_CONFLICT_REASON = Int32
CCR_OTHER = 0
CCR_COLLISION = 1
CCR_NOPARENT = 2
CCR_IDENTITY = 3
KNOWLEDGE_COOKIE_COMPARISON_RESULT = Int32
KCCR_COOKIE_KNOWLEDGE_EQUAL = 0
KCCR_COOKIE_KNOWLEDGE_CONTAINED = 1
KCCR_COOKIE_KNOWLEDGE_CONTAINS = 2
KCCR_COOKIE_KNOWLEDGE_NOT_COMPARABLE = 3
def _define_IClockVectorElement_head():
    class IClockVectorElement(win32more.System.Com.IUnknown_head):
        Guid = Guid('e71c4250-adf8-4a07-8fae-5669596909c1')
    return IClockVectorElement
def _define_IClockVectorElement():
    IClockVectorElement = win32more.System.WindowsSync.IClockVectorElement_head
    IClockVectorElement.GetReplicaKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetReplicaKey', ((1, 'pdwReplicaKey'),)))
    IClockVectorElement.GetTickCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(4, 'GetTickCount', ((1, 'pullTickCount'),)))
    win32more.System.Com.IUnknown
    return IClockVectorElement
def _define_IFeedClockVectorElement_head():
    class IFeedClockVectorElement(win32more.System.WindowsSync.IClockVectorElement_head):
        Guid = Guid('a40b46d2-e97b-4156-b6da-991f501b0f05')
    return IFeedClockVectorElement
def _define_IFeedClockVectorElement():
    IFeedClockVectorElement = win32more.System.WindowsSync.IFeedClockVectorElement_head
    IFeedClockVectorElement.GetSyncTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SYNC_TIME_head), use_last_error=False)(5, 'GetSyncTime', ((1, 'pSyncTime'),)))
    IFeedClockVectorElement.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no, use_last_error=False)(6, 'GetFlags', ((1, 'pbFlags'),)))
    win32more.System.WindowsSync.IClockVectorElement
    return IFeedClockVectorElement
def _define_IClockVector_head():
    class IClockVector(win32more.System.Com.IUnknown_head):
        Guid = Guid('14b2274a-8698-4cc6-9333-f89bd1d47bc4')
    return IClockVector
def _define_IClockVector():
    IClockVector = win32more.System.WindowsSync.IClockVector_head
    IClockVector.GetClockVectorElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'GetClockVectorElements', ((1, 'riid'),(1, 'ppiEnumClockVector'),)))
    IClockVector.GetClockVectorElementCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetClockVectorElementCount', ((1, 'pdwCount'),)))
    win32more.System.Com.IUnknown
    return IClockVector
def _define_IFeedClockVector_head():
    class IFeedClockVector(win32more.System.WindowsSync.IClockVector_head):
        Guid = Guid('8d1d98d1-9fb8-4ec9-a553-54dd924e0f67')
    return IFeedClockVector
def _define_IFeedClockVector():
    IFeedClockVector = win32more.System.WindowsSync.IFeedClockVector_head
    IFeedClockVector.GetUpdateCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetUpdateCount', ((1, 'pdwUpdateCount'),)))
    IFeedClockVector.IsNoConflictsSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'IsNoConflictsSpecified', ((1, 'pfIsNoConflictsSpecified'),)))
    win32more.System.WindowsSync.IClockVector
    return IFeedClockVector
def _define_IEnumClockVector_head():
    class IEnumClockVector(win32more.System.Com.IUnknown_head):
        Guid = Guid('525844db-2837-4799-9e80-81a66e02220c')
    return IEnumClockVector
def _define_IEnumClockVector():
    IEnumClockVector = win32more.System.WindowsSync.IEnumClockVector_head
    IEnumClockVector.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.IClockVectorElement_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cClockVectorElements'),(1, 'ppiClockVectorElements'),(1, 'pcFetched'),)))
    IEnumClockVector.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cSyncVersions'),)))
    IEnumClockVector.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumClockVector.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IEnumClockVector_head), use_last_error=False)(6, 'Clone', ((1, 'ppiEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumClockVector
def _define_IEnumFeedClockVector_head():
    class IEnumFeedClockVector(win32more.System.Com.IUnknown_head):
        Guid = Guid('550f763d-146a-48f6-abeb-6c88c7f70514')
    return IEnumFeedClockVector
def _define_IEnumFeedClockVector():
    IEnumFeedClockVector = win32more.System.WindowsSync.IEnumFeedClockVector_head
    IEnumFeedClockVector.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.IFeedClockVectorElement_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cClockVectorElements'),(1, 'ppiClockVectorElements'),(1, 'pcFetched'),)))
    IEnumFeedClockVector.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cSyncVersions'),)))
    IEnumFeedClockVector.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumFeedClockVector.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IEnumFeedClockVector_head), use_last_error=False)(6, 'Clone', ((1, 'ppiEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumFeedClockVector
def _define_ICoreFragment_head():
    class ICoreFragment(win32more.System.Com.IUnknown_head):
        Guid = Guid('613b2ab5-b304-47d9-9c31-ce6c54401a15')
    return ICoreFragment
def _define_ICoreFragment():
    ICoreFragment = win32more.System.WindowsSync.ICoreFragment_head
    ICoreFragment.NextColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'NextColumn', ((1, 'pChangeUnitId'),(1, 'pChangeUnitIdSize'),)))
    ICoreFragment.NextRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32),POINTER(win32more.System.WindowsSync.IClockVector_head), use_last_error=False)(4, 'NextRange', ((1, 'pItemId'),(1, 'pItemIdSize'),(1, 'piClockVector'),)))
    ICoreFragment.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    ICoreFragment.GetColumnCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetColumnCount', ((1, 'pColumnCount'),)))
    ICoreFragment.GetRangeCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetRangeCount', ((1, 'pRangeCount'),)))
    win32more.System.Com.IUnknown
    return ICoreFragment
def _define_ICoreFragmentInspector_head():
    class ICoreFragmentInspector(win32more.System.Com.IUnknown_head):
        Guid = Guid('f7fcc5fd-ae26-4679-ba16-96aac583c134')
    return ICoreFragmentInspector
def _define_ICoreFragmentInspector():
    ICoreFragmentInspector = win32more.System.WindowsSync.ICoreFragmentInspector_head
    ICoreFragmentInspector.NextCoreFragments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.ICoreFragment_head),POINTER(UInt32), use_last_error=False)(3, 'NextCoreFragments', ((1, 'requestedCount'),(1, 'ppiCoreFragments'),(1, 'pFetchedCount'),)))
    ICoreFragmentInspector.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Reset', ()))
    win32more.System.Com.IUnknown
    return ICoreFragmentInspector
def _define_IRangeException_head():
    class IRangeException(win32more.System.Com.IUnknown_head):
        Guid = Guid('75ae8777-6848-49f7-956c-a3a92f5096e8')
    return IRangeException
def _define_IRangeException():
    IRangeException = win32more.System.WindowsSync.IRangeException_head
    IRangeException.GetClosedRangeStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'GetClosedRangeStart', ((1, 'pbClosedRangeStart'),(1, 'pcbIdSize'),)))
    IRangeException.GetClosedRangeEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(4, 'GetClosedRangeEnd', ((1, 'pbClosedRangeEnd'),(1, 'pcbIdSize'),)))
    IRangeException.GetClockVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(5, 'GetClockVector', ((1, 'riid'),(1, 'ppUnk'),)))
    win32more.System.Com.IUnknown
    return IRangeException
def _define_IEnumRangeExceptions_head():
    class IEnumRangeExceptions(win32more.System.Com.IUnknown_head):
        Guid = Guid('0944439f-ddb1-4176-b703-046ff22a2386')
    return IEnumRangeExceptions
def _define_IEnumRangeExceptions():
    IEnumRangeExceptions = win32more.System.WindowsSync.IEnumRangeExceptions_head
    IEnumRangeExceptions.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.IRangeException_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cExceptions'),(1, 'ppRangeException'),(1, 'pcFetched'),)))
    IEnumRangeExceptions.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cExceptions'),)))
    IEnumRangeExceptions.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumRangeExceptions.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IEnumRangeExceptions_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumRangeExceptions
def _define_ISingleItemException_head():
    class ISingleItemException(win32more.System.Com.IUnknown_head):
        Guid = Guid('892fb9b0-7c55-4a18-9316-fdf449569b64')
    return ISingleItemException
def _define_ISingleItemException():
    ISingleItemException = win32more.System.WindowsSync.ISingleItemException_head
    ISingleItemException.GetItemId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'GetItemId', ((1, 'pbItemId'),(1, 'pcbIdSize'),)))
    ISingleItemException.GetClockVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'GetClockVector', ((1, 'riid'),(1, 'ppUnk'),)))
    win32more.System.Com.IUnknown
    return ISingleItemException
def _define_IEnumSingleItemExceptions_head():
    class IEnumSingleItemExceptions(win32more.System.Com.IUnknown_head):
        Guid = Guid('e563381c-1b4d-4c66-9796-c86faccdcd40')
    return IEnumSingleItemExceptions
def _define_IEnumSingleItemExceptions():
    IEnumSingleItemExceptions = win32more.System.WindowsSync.IEnumSingleItemExceptions_head
    IEnumSingleItemExceptions.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.ISingleItemException_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cExceptions'),(1, 'ppSingleItemException'),(1, 'pcFetched'),)))
    IEnumSingleItemExceptions.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cExceptions'),)))
    IEnumSingleItemExceptions.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumSingleItemExceptions.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IEnumSingleItemExceptions_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumSingleItemExceptions
def _define_IChangeUnitException_head():
    class IChangeUnitException(win32more.System.Com.IUnknown_head):
        Guid = Guid('0cd7ee7c-fec0-4021-99ee-f0e5348f2a5f')
    return IChangeUnitException
def _define_IChangeUnitException():
    IChangeUnitException = win32more.System.WindowsSync.IChangeUnitException_head
    IChangeUnitException.GetItemId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'GetItemId', ((1, 'pbItemId'),(1, 'pcbIdSize'),)))
    IChangeUnitException.GetChangeUnitId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(4, 'GetChangeUnitId', ((1, 'pbChangeUnitId'),(1, 'pcbIdSize'),)))
    IChangeUnitException.GetClockVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(5, 'GetClockVector', ((1, 'riid'),(1, 'ppUnk'),)))
    win32more.System.Com.IUnknown
    return IChangeUnitException
def _define_IEnumChangeUnitExceptions_head():
    class IEnumChangeUnitExceptions(win32more.System.Com.IUnknown_head):
        Guid = Guid('3074e802-9319-4420-be21-1022e2e21da8')
    return IEnumChangeUnitExceptions
def _define_IEnumChangeUnitExceptions():
    IEnumChangeUnitExceptions = win32more.System.WindowsSync.IEnumChangeUnitExceptions_head
    IEnumChangeUnitExceptions.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.IChangeUnitException_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cExceptions'),(1, 'ppChangeUnitException'),(1, 'pcFetched'),)))
    IEnumChangeUnitExceptions.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cExceptions'),)))
    IEnumChangeUnitExceptions.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumChangeUnitExceptions.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IEnumChangeUnitExceptions_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumChangeUnitExceptions
def _define_IReplicaKeyMap_head():
    class IReplicaKeyMap(win32more.System.Com.IUnknown_head):
        Guid = Guid('2209f4fc-fd10-4ff0-84a8-f0a1982e440e')
    return IReplicaKeyMap
def _define_IReplicaKeyMap():
    IReplicaKeyMap = win32more.System.WindowsSync.IReplicaKeyMap_head
    IReplicaKeyMap.LookupReplicaKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'LookupReplicaKey', ((1, 'pbReplicaId'),(1, 'pdwReplicaKey'),)))
    IReplicaKeyMap.LookupReplicaId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(4, 'LookupReplicaId', ((1, 'dwReplicaKey'),(1, 'pbReplicaId'),(1, 'pcbIdSize'),)))
    IReplicaKeyMap.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(5, 'Serialize', ((1, 'pbReplicaKeyMap'),(1, 'pcbReplicaKeyMap'),)))
    win32more.System.Com.IUnknown
    return IReplicaKeyMap
def _define_IConstructReplicaKeyMap_head():
    class IConstructReplicaKeyMap(win32more.System.Com.IUnknown_head):
        Guid = Guid('ded10970-ec85-4115-b52c-4405845642a5')
    return IConstructReplicaKeyMap
def _define_IConstructReplicaKeyMap():
    IConstructReplicaKeyMap = win32more.System.WindowsSync.IConstructReplicaKeyMap_head
    IConstructReplicaKeyMap.FindOrAddReplica = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'FindOrAddReplica', ((1, 'pbReplicaId'),(1, 'pdwReplicaKey'),)))
    win32more.System.Com.IUnknown
    return IConstructReplicaKeyMap
def _define_ISyncKnowledge_head():
    class ISyncKnowledge(win32more.System.Com.IUnknown_head):
        Guid = Guid('615bbb53-c945-4203-bf4b-2cb65919a0aa')
    return ISyncKnowledge
def _define_ISyncKnowledge():
    ISyncKnowledge = win32more.System.WindowsSync.ISyncKnowledge_head
    ISyncKnowledge.GetOwnerReplicaId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'GetOwnerReplicaId', ((1, 'pbReplicaId'),(1, 'pcbIdSize'),)))
    ISyncKnowledge.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,c_char_p_no,POINTER(UInt32), use_last_error=False)(4, 'Serialize', ((1, 'fSerializeReplicaKeyMap'),(1, 'pbKnowledge'),(1, 'pcbKnowledge'),)))
    ISyncKnowledge.SetLocalTickCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(5, 'SetLocalTickCount', ((1, 'ullTickCount'),)))
    ISyncKnowledge.ContainsChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), use_last_error=False)(6, 'ContainsChange', ((1, 'pbVersionOwnerReplicaId'),(1, 'pgidItemId'),(1, 'pSyncVersion'),)))
    ISyncKnowledge.ContainsChangeUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), use_last_error=False)(7, 'ContainsChangeUnit', ((1, 'pbVersionOwnerReplicaId'),(1, 'pbItemId'),(1, 'pbChangeUnitId'),(1, 'pSyncVersion'),)))
    ISyncKnowledge.GetScopeVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(8, 'GetScopeVector', ((1, 'riid'),(1, 'ppUnk'),)))
    ISyncKnowledge.GetReplicaKeyMap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IReplicaKeyMap_head), use_last_error=False)(9, 'GetReplicaKeyMap', ((1, 'ppReplicaKeyMap'),)))
    ISyncKnowledge.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(10, 'Clone', ((1, 'ppClonedKnowledge'),)))
    ISyncKnowledge.ConvertVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head),c_char_p_no,POINTER(UInt32),POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), use_last_error=False)(11, 'ConvertVersion', ((1, 'pKnowledgeIn'),(1, 'pbCurrentOwnerId'),(1, 'pVersionIn'),(1, 'pbNewOwnerId'),(1, 'pcbIdSize'),(1, 'pVersionOut'),)))
    ISyncKnowledge.MapRemoteToLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(12, 'MapRemoteToLocal', ((1, 'pRemoteKnowledge'),(1, 'ppMappedKnowledge'),)))
    ISyncKnowledge.Union = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head, use_last_error=False)(13, 'Union', ((1, 'pKnowledge'),)))
    ISyncKnowledge.ProjectOntoItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(14, 'ProjectOntoItem', ((1, 'pbItemId'),(1, 'ppKnowledgeOut'),)))
    ISyncKnowledge.ProjectOntoChangeUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(15, 'ProjectOntoChangeUnit', ((1, 'pbItemId'),(1, 'pbChangeUnitId'),(1, 'ppKnowledgeOut'),)))
    ISyncKnowledge.ProjectOntoRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SYNC_RANGE_head),POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(16, 'ProjectOntoRange', ((1, 'psrngSyncRange'),(1, 'ppKnowledgeOut'),)))
    ISyncKnowledge.ExcludeItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no, use_last_error=False)(17, 'ExcludeItem', ((1, 'pbItemId'),)))
    ISyncKnowledge.ExcludeChangeUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no, use_last_error=False)(18, 'ExcludeChangeUnit', ((1, 'pbItemId'),(1, 'pbChangeUnitId'),)))
    ISyncKnowledge.ContainsKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head, use_last_error=False)(19, 'ContainsKnowledge', ((1, 'pKnowledge'),)))
    ISyncKnowledge.FindMinTickCountForReplica = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt64), use_last_error=False)(20, 'FindMinTickCountForReplica', ((1, 'pbReplicaId'),(1, 'pullReplicaTickCount'),)))
    ISyncKnowledge.GetRangeExceptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(21, 'GetRangeExceptions', ((1, 'riid'),(1, 'ppUnk'),)))
    ISyncKnowledge.GetSingleItemExceptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(22, 'GetSingleItemExceptions', ((1, 'riid'),(1, 'ppUnk'),)))
    ISyncKnowledge.GetChangeUnitExceptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(23, 'GetChangeUnitExceptions', ((1, 'riid'),(1, 'ppUnk'),)))
    ISyncKnowledge.FindClockVectorForItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(24, 'FindClockVectorForItem', ((1, 'pbItemId'),(1, 'riid'),(1, 'ppUnk'),)))
    ISyncKnowledge.FindClockVectorForChangeUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(25, 'FindClockVectorForChangeUnit', ((1, 'pbItemId'),(1, 'pbChangeUnitId'),(1, 'riid'),(1, 'ppUnk'),)))
    ISyncKnowledge.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(26, 'GetVersion', ((1, 'pdwVersion'),)))
    win32more.System.Com.IUnknown
    return ISyncKnowledge
def _define_IForgottenKnowledge_head():
    class IForgottenKnowledge(win32more.System.WindowsSync.ISyncKnowledge_head):
        Guid = Guid('456e0f96-6036-452b-9f9d-bcc4b4a85db2')
    return IForgottenKnowledge
def _define_IForgottenKnowledge():
    IForgottenKnowledge = win32more.System.WindowsSync.IForgottenKnowledge_head
    IForgottenKnowledge.ForgetToVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), use_last_error=False)(27, 'ForgetToVersion', ((1, 'pKnowledge'),(1, 'pVersion'),)))
    win32more.System.WindowsSync.ISyncKnowledge
    return IForgottenKnowledge
def _define_ISyncKnowledge2_head():
    class ISyncKnowledge2(win32more.System.WindowsSync.ISyncKnowledge_head):
        Guid = Guid('ed0addc0-3b4b-46a1-9a45-45661d2114c8')
    return ISyncKnowledge2
def _define_ISyncKnowledge2():
    ISyncKnowledge2 = win32more.System.WindowsSync.ISyncKnowledge2_head
    ISyncKnowledge2.GetIdParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ID_PARAMETERS_head), use_last_error=False)(27, 'GetIdParameters', ((1, 'pIdParameters'),)))
    ISyncKnowledge2.ProjectOntoColumnSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),UInt32,POINTER(win32more.System.WindowsSync.ISyncKnowledge2_head), use_last_error=False)(28, 'ProjectOntoColumnSet', ((1, 'ppColumns'),(1, 'count'),(1, 'ppiKnowledgeOut'),)))
    ISyncKnowledge2.SerializeWithOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.SYNC_SERIALIZATION_VERSION,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(29, 'SerializeWithOptions', ((1, 'targetFormatVersion'),(1, 'dwFlags'),(1, 'pbBuffer'),(1, 'pdwSerializedSize'),)))
    ISyncKnowledge2.GetLowestUncontainedId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge2_head,c_char_p_no,POINTER(UInt32), use_last_error=False)(30, 'GetLowestUncontainedId', ((1, 'piSyncKnowledge'),(1, 'pbItemId'),(1, 'pcbItemIdSize'),)))
    ISyncKnowledge2.GetInspector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(31, 'GetInspector', ((1, 'riid'),(1, 'ppiInspector'),)))
    ISyncKnowledge2.GetMinimumSupportedVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SYNC_SERIALIZATION_VERSION), use_last_error=False)(32, 'GetMinimumSupportedVersion', ((1, 'pVersion'),)))
    ISyncKnowledge2.GetStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.SYNC_STATISTICS,POINTER(UInt32), use_last_error=False)(33, 'GetStatistics', ((1, 'which'),(1, 'pValue'),)))
    ISyncKnowledge2.ContainsKnowledgeForItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,c_char_p_no, use_last_error=False)(34, 'ContainsKnowledgeForItem', ((1, 'pKnowledge'),(1, 'pbItemId'),)))
    ISyncKnowledge2.ContainsKnowledgeForChangeUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,c_char_p_no,c_char_p_no, use_last_error=False)(35, 'ContainsKnowledgeForChangeUnit', ((1, 'pKnowledge'),(1, 'pbItemId'),(1, 'pbChangeUnitId'),)))
    ISyncKnowledge2.ProjectOntoKnowledgeWithPrerequisite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.System.WindowsSync.ISyncKnowledge_head,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(36, 'ProjectOntoKnowledgeWithPrerequisite', ((1, 'pPrerequisiteKnowledge'),(1, 'pTemplateKnowledge'),(1, 'ppProjectedKnowledge'),)))
    ISyncKnowledge2.Complement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(37, 'Complement', ((1, 'pSyncKnowledge'),(1, 'ppComplementedKnowledge'),)))
    ISyncKnowledge2.IntersectsWithKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head, use_last_error=False)(38, 'IntersectsWithKnowledge', ((1, 'pSyncKnowledge'),)))
    ISyncKnowledge2.GetKnowledgeCookie = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(39, 'GetKnowledgeCookie', ((1, 'ppKnowledgeCookie'),)))
    ISyncKnowledge2.CompareToKnowledgeCookie = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.WindowsSync.KNOWLEDGE_COOKIE_COMPARISON_RESULT), use_last_error=False)(40, 'CompareToKnowledgeCookie', ((1, 'pKnowledgeCookie'),(1, 'pResult'),)))
    win32more.System.WindowsSync.ISyncKnowledge
    return ISyncKnowledge2
def _define_IRecoverableErrorData_head():
    class IRecoverableErrorData(win32more.System.Com.IUnknown_head):
        Guid = Guid('b37c4a0a-4b7d-4c2d-9711-3b00d119b1c8')
    return IRecoverableErrorData
def _define_IRecoverableErrorData():
    IRecoverableErrorData = win32more.System.WindowsSync.IRecoverableErrorData_head
    IRecoverableErrorData.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'Initialize', ((1, 'pcszItemDisplayName'),(1, 'pcszErrorDescription'),)))
    IRecoverableErrorData.GetItemDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(4, 'GetItemDisplayName', ((1, 'pszItemDisplayName'),(1, 'pcchItemDisplayName'),)))
    IRecoverableErrorData.GetErrorDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(5, 'GetErrorDescription', ((1, 'pszErrorDescription'),(1, 'pcchErrorDescription'),)))
    win32more.System.Com.IUnknown
    return IRecoverableErrorData
def _define_IRecoverableError_head():
    class IRecoverableError(win32more.System.Com.IUnknown_head):
        Guid = Guid('0f5625e8-0a7b-45ee-9637-1ce13645909e')
    return IRecoverableError
def _define_IRecoverableError():
    IRecoverableError = win32more.System.WindowsSync.IRecoverableError_head
    IRecoverableError.GetStage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SYNC_PROGRESS_STAGE), use_last_error=False)(3, 'GetStage', ((1, 'pStage'),)))
    IRecoverableError.GetProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SYNC_PROVIDER_ROLE), use_last_error=False)(4, 'GetProvider', ((1, 'pProviderRole'),)))
    IRecoverableError.GetChangeWithRecoverableError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncChange_head), use_last_error=False)(5, 'GetChangeWithRecoverableError', ((1, 'ppChangeWithRecoverableError'),)))
    IRecoverableError.GetRecoverableErrorDataForChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT),POINTER(win32more.System.WindowsSync.IRecoverableErrorData_head), use_last_error=False)(6, 'GetRecoverableErrorDataForChange', ((1, 'phrError'),(1, 'ppErrorData'),)))
    IRecoverableError.GetRecoverableErrorDataForChangeUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncChangeUnit_head,POINTER(win32more.Foundation.HRESULT),POINTER(win32more.System.WindowsSync.IRecoverableErrorData_head), use_last_error=False)(7, 'GetRecoverableErrorDataForChangeUnit', ((1, 'pChangeUnit'),(1, 'phrError'),(1, 'ppErrorData'),)))
    win32more.System.Com.IUnknown
    return IRecoverableError
def _define_IChangeConflict_head():
    class IChangeConflict(win32more.System.Com.IUnknown_head):
        Guid = Guid('014ebf97-9f20-4f7a-bdd4-25979c77c002')
    return IChangeConflict
def _define_IChangeConflict():
    IChangeConflict = win32more.System.WindowsSync.IChangeConflict_head
    IChangeConflict.GetDestinationProviderConflictingChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncChange_head), use_last_error=False)(3, 'GetDestinationProviderConflictingChange', ((1, 'ppConflictingChange'),)))
    IChangeConflict.GetSourceProviderConflictingChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncChange_head), use_last_error=False)(4, 'GetSourceProviderConflictingChange', ((1, 'ppConflictingChange'),)))
    IChangeConflict.GetDestinationProviderConflictingData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(5, 'GetDestinationProviderConflictingData', ((1, 'ppConflictingData'),)))
    IChangeConflict.GetSourceProviderConflictingData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(6, 'GetSourceProviderConflictingData', ((1, 'ppConflictingData'),)))
    IChangeConflict.GetResolveActionForChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SYNC_RESOLVE_ACTION), use_last_error=False)(7, 'GetResolveActionForChange', ((1, 'pResolveAction'),)))
    IChangeConflict.SetResolveActionForChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.SYNC_RESOLVE_ACTION, use_last_error=False)(8, 'SetResolveActionForChange', ((1, 'resolveAction'),)))
    IChangeConflict.GetResolveActionForChangeUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncChangeUnit_head,POINTER(win32more.System.WindowsSync.SYNC_RESOLVE_ACTION), use_last_error=False)(9, 'GetResolveActionForChangeUnit', ((1, 'pChangeUnit'),(1, 'pResolveAction'),)))
    IChangeConflict.SetResolveActionForChangeUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncChangeUnit_head,win32more.System.WindowsSync.SYNC_RESOLVE_ACTION, use_last_error=False)(10, 'SetResolveActionForChangeUnit', ((1, 'pChangeUnit'),(1, 'resolveAction'),)))
    win32more.System.Com.IUnknown
    return IChangeConflict
def _define_IConstraintConflict_head():
    class IConstraintConflict(win32more.System.Com.IUnknown_head):
        Guid = Guid('00d2302e-1cf8-4835-b85f-b7ca4f799e0a')
    return IConstraintConflict
def _define_IConstraintConflict():
    IConstraintConflict = win32more.System.WindowsSync.IConstraintConflict_head
    IConstraintConflict.GetDestinationProviderConflictingChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncChange_head), use_last_error=False)(3, 'GetDestinationProviderConflictingChange', ((1, 'ppConflictingChange'),)))
    IConstraintConflict.GetSourceProviderConflictingChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncChange_head), use_last_error=False)(4, 'GetSourceProviderConflictingChange', ((1, 'ppConflictingChange'),)))
    IConstraintConflict.GetDestinationProviderOriginalChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncChange_head), use_last_error=False)(5, 'GetDestinationProviderOriginalChange', ((1, 'ppOriginalChange'),)))
    IConstraintConflict.GetDestinationProviderConflictingData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(6, 'GetDestinationProviderConflictingData', ((1, 'ppConflictingData'),)))
    IConstraintConflict.GetSourceProviderConflictingData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'GetSourceProviderConflictingData', ((1, 'ppConflictingData'),)))
    IConstraintConflict.GetDestinationProviderOriginalData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'GetDestinationProviderOriginalData', ((1, 'ppOriginalData'),)))
    IConstraintConflict.GetConstraintResolveActionForChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION), use_last_error=False)(9, 'GetConstraintResolveActionForChange', ((1, 'pConstraintResolveAction'),)))
    IConstraintConflict.SetConstraintResolveActionForChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION, use_last_error=False)(10, 'SetConstraintResolveActionForChange', ((1, 'constraintResolveAction'),)))
    IConstraintConflict.GetConstraintResolveActionForChangeUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncChangeUnit_head,POINTER(win32more.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION), use_last_error=False)(11, 'GetConstraintResolveActionForChangeUnit', ((1, 'pChangeUnit'),(1, 'pConstraintResolveAction'),)))
    IConstraintConflict.SetConstraintResolveActionForChangeUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncChangeUnit_head,win32more.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION, use_last_error=False)(12, 'SetConstraintResolveActionForChangeUnit', ((1, 'pChangeUnit'),(1, 'constraintResolveAction'),)))
    IConstraintConflict.GetConstraintConflictReason = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.CONSTRAINT_CONFLICT_REASON), use_last_error=False)(13, 'GetConstraintConflictReason', ((1, 'pConstraintConflictReason'),)))
    IConstraintConflict.IsTemporary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'IsTemporary', ()))
    win32more.System.Com.IUnknown
    return IConstraintConflict
def _define_ISyncCallback_head():
    class ISyncCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('0599797f-5ed9-485c-ae36-0c5d1bf2e7a5')
    return ISyncCallback
def _define_ISyncCallback():
    ISyncCallback = win32more.System.WindowsSync.ISyncCallback_head
    ISyncCallback.OnProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.SYNC_PROVIDER_ROLE,win32more.System.WindowsSync.SYNC_PROGRESS_STAGE,UInt32,UInt32, use_last_error=False)(3, 'OnProgress', ((1, 'provider'),(1, 'syncStage'),(1, 'dwCompletedWork'),(1, 'dwTotalWork'),)))
    ISyncCallback.OnChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncChange_head, use_last_error=False)(4, 'OnChange', ((1, 'pSyncChange'),)))
    ISyncCallback.OnConflict = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.IChangeConflict_head, use_last_error=False)(5, 'OnConflict', ((1, 'pConflict'),)))
    ISyncCallback.OnFullEnumerationNeeded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SYNC_FULL_ENUMERATION_ACTION), use_last_error=False)(6, 'OnFullEnumerationNeeded', ((1, 'pFullEnumerationAction'),)))
    ISyncCallback.OnRecoverableError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.IRecoverableError_head, use_last_error=False)(7, 'OnRecoverableError', ((1, 'pRecoverableError'),)))
    win32more.System.Com.IUnknown
    return ISyncCallback
def _define_ISyncCallback2_head():
    class ISyncCallback2(win32more.System.WindowsSync.ISyncCallback_head):
        Guid = Guid('47ce84af-7442-4ead-8630-12015e030ad7')
    return ISyncCallback2
def _define_ISyncCallback2():
    ISyncCallback2 = win32more.System.WindowsSync.ISyncCallback2_head
    ISyncCallback2.OnChangeApplied = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(8, 'OnChangeApplied', ((1, 'dwChangesApplied'),(1, 'dwChangesFailed'),)))
    ISyncCallback2.OnChangeFailed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(9, 'OnChangeFailed', ((1, 'dwChangesApplied'),(1, 'dwChangesFailed'),)))
    win32more.System.WindowsSync.ISyncCallback
    return ISyncCallback2
def _define_ISyncConstraintCallback_head():
    class ISyncConstraintCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('8af3843e-75b3-438c-bb51-6f020d70d3cb')
    return ISyncConstraintCallback
def _define_ISyncConstraintCallback():
    ISyncConstraintCallback = win32more.System.WindowsSync.ISyncConstraintCallback_head
    ISyncConstraintCallback.OnConstraintConflict = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.IConstraintConflict_head, use_last_error=False)(3, 'OnConstraintConflict', ((1, 'pConflict'),)))
    win32more.System.Com.IUnknown
    return ISyncConstraintCallback
def _define_ISyncProvider_head():
    class ISyncProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('8f657056-2bce-4a17-8c68-c7bb7898b56f')
    return ISyncProvider
def _define_ISyncProvider():
    ISyncProvider = win32more.System.WindowsSync.ISyncProvider_head
    ISyncProvider.GetIdParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ID_PARAMETERS_head), use_last_error=False)(3, 'GetIdParameters', ((1, 'pIdParameters'),)))
    win32more.System.Com.IUnknown
    return ISyncProvider
def _define_ISyncSessionState_head():
    class ISyncSessionState(win32more.System.Com.IUnknown_head):
        Guid = Guid('b8a940fe-9f01-483b-9434-c37d361225d9')
    return ISyncSessionState
def _define_ISyncSessionState():
    ISyncSessionState = win32more.System.WindowsSync.ISyncSessionState_head
    ISyncSessionState.IsCanceled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'IsCanceled', ((1, 'pfIsCanceled'),)))
    ISyncSessionState.GetInfoForChangeApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(4, 'GetInfoForChangeApplication', ((1, 'pbChangeApplierInfo'),(1, 'pcbChangeApplierInfo'),)))
    ISyncSessionState.LoadInfoFromChangeApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32, use_last_error=False)(5, 'LoadInfoFromChangeApplication', ((1, 'pbChangeApplierInfo'),(1, 'cbChangeApplierInfo'),)))
    ISyncSessionState.GetForgottenKnowledgeRecoveryRangeStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(6, 'GetForgottenKnowledgeRecoveryRangeStart', ((1, 'pbRangeStart'),(1, 'pcbRangeStart'),)))
    ISyncSessionState.GetForgottenKnowledgeRecoveryRangeEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(7, 'GetForgottenKnowledgeRecoveryRangeEnd', ((1, 'pbRangeEnd'),(1, 'pcbRangeEnd'),)))
    ISyncSessionState.SetForgottenKnowledgeRecoveryRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SYNC_RANGE_head), use_last_error=False)(8, 'SetForgottenKnowledgeRecoveryRange', ((1, 'pRange'),)))
    ISyncSessionState.OnProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.SYNC_PROVIDER_ROLE,win32more.System.WindowsSync.SYNC_PROGRESS_STAGE,UInt32,UInt32, use_last_error=False)(9, 'OnProgress', ((1, 'provider'),(1, 'syncStage'),(1, 'dwCompletedWork'),(1, 'dwTotalWork'),)))
    win32more.System.Com.IUnknown
    return ISyncSessionState
def _define_ISyncSessionExtendedErrorInfo_head():
    class ISyncSessionExtendedErrorInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('326c6810-790a-409b-b741-6999388761eb')
    return ISyncSessionExtendedErrorInfo
def _define_ISyncSessionExtendedErrorInfo():
    ISyncSessionExtendedErrorInfo = win32more.System.WindowsSync.ISyncSessionExtendedErrorInfo_head
    ISyncSessionExtendedErrorInfo.GetSyncProviderWithError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncProvider_head), use_last_error=False)(3, 'GetSyncProviderWithError', ((1, 'ppProviderWithError'),)))
    win32more.System.Com.IUnknown
    return ISyncSessionExtendedErrorInfo
def _define_ISyncSessionState2_head():
    class ISyncSessionState2(win32more.System.WindowsSync.ISyncSessionState_head):
        Guid = Guid('9e37cfa3-9e38-4c61-9ca3-ffe810b45ca2')
    return ISyncSessionState2
def _define_ISyncSessionState2():
    ISyncSessionState2 = win32more.System.WindowsSync.ISyncSessionState2_head
    ISyncSessionState2.SetProviderWithError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(10, 'SetProviderWithError', ((1, 'fSelf'),)))
    ISyncSessionState2.GetSessionErrorStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(11, 'GetSessionErrorStatus', ((1, 'phrSessionError'),)))
    win32more.System.WindowsSync.ISyncSessionState
    return ISyncSessionState2
def _define_ISyncFilterInfo_head():
    class ISyncFilterInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('794eaaf8-3f2e-47e6-9728-17e6fcf94cb7')
    return ISyncFilterInfo
def _define_ISyncFilterInfo():
    ISyncFilterInfo = win32more.System.WindowsSync.ISyncFilterInfo_head
    ISyncFilterInfo.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'Serialize', ((1, 'pbBuffer'),(1, 'pcbBuffer'),)))
    win32more.System.Com.IUnknown
    return ISyncFilterInfo
def _define_ISyncFilterInfo2_head():
    class ISyncFilterInfo2(win32more.System.WindowsSync.ISyncFilterInfo_head):
        Guid = Guid('19b394ba-e3d0-468c-934d-321968b2ab34')
    return ISyncFilterInfo2
def _define_ISyncFilterInfo2():
    ISyncFilterInfo2 = win32more.System.WindowsSync.ISyncFilterInfo2_head
    ISyncFilterInfo2.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetFlags', ((1, 'pdwFlags'),)))
    win32more.System.WindowsSync.ISyncFilterInfo
    return ISyncFilterInfo2
def _define_IChangeUnitListFilterInfo_head():
    class IChangeUnitListFilterInfo(win32more.System.WindowsSync.ISyncFilterInfo_head):
        Guid = Guid('f2837671-0bdf-43fa-b502-232375fb50c2')
    return IChangeUnitListFilterInfo
def _define_IChangeUnitListFilterInfo():
    IChangeUnitListFilterInfo = win32more.System.WindowsSync.IChangeUnitListFilterInfo_head
    IChangeUnitListFilterInfo.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),UInt32, use_last_error=False)(4, 'Initialize', ((1, 'ppbChangeUnitIds'),(1, 'dwChangeUnitCount'),)))
    IChangeUnitListFilterInfo.GetChangeUnitIdCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetChangeUnitIdCount', ((1, 'pdwChangeUnitIdCount'),)))
    IChangeUnitListFilterInfo.GetChangeUnitId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(6, 'GetChangeUnitId', ((1, 'dwChangeUnitIdIndex'),(1, 'pbChangeUnitId'),(1, 'pcbIdSize'),)))
    win32more.System.WindowsSync.ISyncFilterInfo
    return IChangeUnitListFilterInfo
def _define_ISyncFilter_head():
    class ISyncFilter(win32more.System.Com.IUnknown_head):
        Guid = Guid('087a3f15-0fcb-44c1-9639-53c14e2b5506')
    return ISyncFilter
def _define_ISyncFilter():
    ISyncFilter = win32more.System.WindowsSync.ISyncFilter_head
    ISyncFilter.IsIdentical = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncFilter_head, use_last_error=False)(3, 'IsIdentical', ((1, 'pSyncFilter'),)))
    ISyncFilter.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(4, 'Serialize', ((1, 'pbSyncFilter'),(1, 'pcbSyncFilter'),)))
    win32more.System.Com.IUnknown
    return ISyncFilter
def _define_ISyncFilterDeserializer_head():
    class ISyncFilterDeserializer(win32more.System.Com.IUnknown_head):
        Guid = Guid('b45b7a72-e5c7-46be-9c82-77b8b15dab8a')
    return ISyncFilterDeserializer
def _define_ISyncFilterDeserializer():
    ISyncFilterDeserializer = win32more.System.WindowsSync.ISyncFilterDeserializer_head
    ISyncFilterDeserializer.DeserializeSyncFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(win32more.System.WindowsSync.ISyncFilter_head), use_last_error=False)(3, 'DeserializeSyncFilter', ((1, 'pbSyncFilter'),(1, 'dwCbSyncFilter'),(1, 'ppISyncFilter'),)))
    win32more.System.Com.IUnknown
    return ISyncFilterDeserializer
def _define_ICustomFilterInfo_head():
    class ICustomFilterInfo(win32more.System.WindowsSync.ISyncFilterInfo_head):
        Guid = Guid('1d335dff-6f88-4e4d-91a8-a3f351cfd473')
    return ICustomFilterInfo
def _define_ICustomFilterInfo():
    ICustomFilterInfo = win32more.System.WindowsSync.ICustomFilterInfo_head
    ICustomFilterInfo.GetSyncFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncFilter_head), use_last_error=False)(4, 'GetSyncFilter', ((1, 'pISyncFilter'),)))
    win32more.System.WindowsSync.ISyncFilterInfo
    return ICustomFilterInfo
FILTER_COMBINATION_TYPE = Int32
FCT_INTERSECTION = 0
def _define_ICombinedFilterInfo_head():
    class ICombinedFilterInfo(win32more.System.WindowsSync.ISyncFilterInfo_head):
        Guid = Guid('11f9de71-2818-4779-b2ac-42d450565f45')
    return ICombinedFilterInfo
def _define_ICombinedFilterInfo():
    ICombinedFilterInfo = win32more.System.WindowsSync.ICombinedFilterInfo_head
    ICombinedFilterInfo.GetFilterCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetFilterCount', ((1, 'pdwFilterCount'),)))
    ICombinedFilterInfo.GetFilterInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.ISyncFilterInfo_head), use_last_error=False)(5, 'GetFilterInfo', ((1, 'dwFilterIndex'),(1, 'ppIFilterInfo'),)))
    ICombinedFilterInfo.GetFilterCombinationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.FILTER_COMBINATION_TYPE), use_last_error=False)(6, 'GetFilterCombinationType', ((1, 'pFilterCombinationType'),)))
    win32more.System.WindowsSync.ISyncFilterInfo
    return ICombinedFilterInfo
def _define_IEnumSyncChanges_head():
    class IEnumSyncChanges(win32more.System.Com.IUnknown_head):
        Guid = Guid('5f86be4a-5e78-4e32-ac1c-c24fd223ef85')
    return IEnumSyncChanges
def _define_IEnumSyncChanges():
    IEnumSyncChanges = win32more.System.WindowsSync.IEnumSyncChanges_head
    IEnumSyncChanges.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.ISyncChange_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cChanges'),(1, 'ppChange'),(1, 'pcFetched'),)))
    IEnumSyncChanges.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cChanges'),)))
    IEnumSyncChanges.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumSyncChanges.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IEnumSyncChanges_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumSyncChanges
def _define_ISyncChangeBuilder_head():
    class ISyncChangeBuilder(win32more.System.Com.IUnknown_head):
        Guid = Guid('56f14771-8677-484f-a170-e386e418a676')
    return ISyncChangeBuilder
def _define_ISyncChangeBuilder():
    ISyncChangeBuilder = win32more.System.WindowsSync.ISyncChangeBuilder_head
    ISyncChangeBuilder.AddChangeUnitMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), use_last_error=False)(3, 'AddChangeUnitMetadata', ((1, 'pbChangeUnitId'),(1, 'pChangeUnitVersion'),)))
    win32more.System.Com.IUnknown
    return ISyncChangeBuilder
def _define_IFilterTrackingSyncChangeBuilder_head():
    class IFilterTrackingSyncChangeBuilder(win32more.System.Com.IUnknown_head):
        Guid = Guid('295024a0-70da-4c58-883c-ce2afb308d0b')
    return IFilterTrackingSyncChangeBuilder
def _define_IFilterTrackingSyncChangeBuilder():
    IFilterTrackingSyncChangeBuilder = win32more.System.WindowsSync.IFilterTrackingSyncChangeBuilder_head
    IFilterTrackingSyncChangeBuilder.AddFilterChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.SYNC_FILTER_CHANGE_head), use_last_error=False)(3, 'AddFilterChange', ((1, 'dwFilterKey'),(1, 'pFilterChange'),)))
    IFilterTrackingSyncChangeBuilder.SetAllChangeUnitsPresentFlag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'SetAllChangeUnitsPresentFlag', ()))
    win32more.System.Com.IUnknown
    return IFilterTrackingSyncChangeBuilder
def _define_ISyncChangeBatchBase_head():
    class ISyncChangeBatchBase(win32more.System.Com.IUnknown_head):
        Guid = Guid('52f6e694-6a71-4494-a184-a8311bf5d227')
    return ISyncChangeBatchBase
def _define_ISyncChangeBatchBase():
    ISyncChangeBatchBase = win32more.System.WindowsSync.ISyncChangeBatchBase_head
    ISyncChangeBatchBase.GetChangeEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IEnumSyncChanges_head), use_last_error=False)(3, 'GetChangeEnumerator', ((1, 'ppEnum'),)))
    ISyncChangeBatchBase.GetIsLastBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetIsLastBatch', ((1, 'pfLastBatch'),)))
    ISyncChangeBatchBase.GetWorkEstimateForBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetWorkEstimateForBatch', ((1, 'pdwWorkForBatch'),)))
    ISyncChangeBatchBase.GetRemainingWorkEstimateForSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetRemainingWorkEstimateForSession', ((1, 'pdwRemainingWorkForSession'),)))
    ISyncChangeBatchBase.BeginOrderedGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no, use_last_error=False)(7, 'BeginOrderedGroup', ((1, 'pbLowerBound'),)))
    ISyncChangeBatchBase.EndOrderedGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,win32more.System.WindowsSync.ISyncKnowledge_head, use_last_error=False)(8, 'EndOrderedGroup', ((1, 'pbUpperBound'),(1, 'pMadeWithKnowledge'),)))
    ISyncChangeBatchBase.AddItemMetadataToGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head),POINTER(win32more.System.WindowsSync.SYNC_VERSION_head),UInt32,UInt32,POINTER(win32more.System.WindowsSync.ISyncChangeBuilder_head), use_last_error=False)(9, 'AddItemMetadataToGroup', ((1, 'pbOwnerReplicaId'),(1, 'pbItemId'),(1, 'pChangeVersion'),(1, 'pCreationVersion'),(1, 'dwFlags'),(1, 'dwWorkForChange'),(1, 'ppChangeBuilder'),)))
    ISyncChangeBatchBase.GetLearnedKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(10, 'GetLearnedKnowledge', ((1, 'ppLearnedKnowledge'),)))
    ISyncChangeBatchBase.GetPrerequisiteKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(11, 'GetPrerequisiteKnowledge', ((1, 'ppPrerequisteKnowledge'),)))
    ISyncChangeBatchBase.GetSourceForgottenKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IForgottenKnowledge_head), use_last_error=False)(12, 'GetSourceForgottenKnowledge', ((1, 'ppSourceForgottenKnowledge'),)))
    ISyncChangeBatchBase.SetLastBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'SetLastBatch', ()))
    ISyncChangeBatchBase.SetWorkEstimateForBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(14, 'SetWorkEstimateForBatch', ((1, 'dwWorkForBatch'),)))
    ISyncChangeBatchBase.SetRemainingWorkEstimateForSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(15, 'SetRemainingWorkEstimateForSession', ((1, 'dwRemainingWorkForSession'),)))
    ISyncChangeBatchBase.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(16, 'Serialize', ((1, 'pbChangeBatch'),(1, 'pcbChangeBatch'),)))
    win32more.System.Com.IUnknown
    return ISyncChangeBatchBase
def _define_ISyncChangeBatch_head():
    class ISyncChangeBatch(win32more.System.WindowsSync.ISyncChangeBatchBase_head):
        Guid = Guid('70c64dee-380f-4c2e-8f70-31c55bd5f9b3')
    return ISyncChangeBatch
def _define_ISyncChangeBatch():
    ISyncChangeBatch = win32more.System.WindowsSync.ISyncChangeBatch_head
    ISyncChangeBatch.BeginUnorderedGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'BeginUnorderedGroup', ()))
    ISyncChangeBatch.EndUnorderedGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.Foundation.BOOL, use_last_error=False)(18, 'EndUnorderedGroup', ((1, 'pMadeWithKnowledge'),(1, 'fAllChangesForKnowledge'),)))
    ISyncChangeBatch.AddLoggedConflict = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head),POINTER(win32more.System.WindowsSync.SYNC_VERSION_head),UInt32,UInt32,win32more.System.WindowsSync.ISyncKnowledge_head,POINTER(win32more.System.WindowsSync.ISyncChangeBuilder_head), use_last_error=False)(19, 'AddLoggedConflict', ((1, 'pbOwnerReplicaId'),(1, 'pbItemId'),(1, 'pChangeVersion'),(1, 'pCreationVersion'),(1, 'dwFlags'),(1, 'dwWorkForChange'),(1, 'pConflictKnowledge'),(1, 'ppChangeBuilder'),)))
    win32more.System.WindowsSync.ISyncChangeBatchBase
    return ISyncChangeBatch
def _define_ISyncFullEnumerationChangeBatch_head():
    class ISyncFullEnumerationChangeBatch(win32more.System.WindowsSync.ISyncChangeBatchBase_head):
        Guid = Guid('ef64197d-4f44-4ea2-b355-4524713e3bed')
    return ISyncFullEnumerationChangeBatch
def _define_ISyncFullEnumerationChangeBatch():
    ISyncFullEnumerationChangeBatch = win32more.System.WindowsSync.ISyncFullEnumerationChangeBatch_head
    ISyncFullEnumerationChangeBatch.GetLearnedKnowledgeAfterRecoveryComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(17, 'GetLearnedKnowledgeAfterRecoveryComplete', ((1, 'ppLearnedKnowledgeAfterRecoveryComplete'),)))
    ISyncFullEnumerationChangeBatch.GetClosedLowerBoundItemId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(18, 'GetClosedLowerBoundItemId', ((1, 'pbClosedLowerBoundItemId'),(1, 'pcbIdSize'),)))
    ISyncFullEnumerationChangeBatch.GetClosedUpperBoundItemId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(19, 'GetClosedUpperBoundItemId', ((1, 'pbClosedUpperBoundItemId'),(1, 'pcbIdSize'),)))
    win32more.System.WindowsSync.ISyncChangeBatchBase
    return ISyncFullEnumerationChangeBatch
def _define_ISyncChangeBatchWithPrerequisite_head():
    class ISyncChangeBatchWithPrerequisite(win32more.System.WindowsSync.ISyncChangeBatchBase_head):
        Guid = Guid('097f13be-5b92-4048-b3f2-7b42a2515e07')
    return ISyncChangeBatchWithPrerequisite
def _define_ISyncChangeBatchWithPrerequisite():
    ISyncChangeBatchWithPrerequisite = win32more.System.WindowsSync.ISyncChangeBatchWithPrerequisite_head
    ISyncChangeBatchWithPrerequisite.SetPrerequisiteKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head, use_last_error=False)(17, 'SetPrerequisiteKnowledge', ((1, 'pPrerequisiteKnowledge'),)))
    ISyncChangeBatchWithPrerequisite.GetLearnedKnowledgeWithPrerequisite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(18, 'GetLearnedKnowledgeWithPrerequisite', ((1, 'pDestinationKnowledge'),(1, 'ppLearnedWithPrerequisiteKnowledge'),)))
    ISyncChangeBatchWithPrerequisite.GetLearnedForgottenKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IForgottenKnowledge_head), use_last_error=False)(19, 'GetLearnedForgottenKnowledge', ((1, 'ppLearnedForgottenKnowledge'),)))
    win32more.System.WindowsSync.ISyncChangeBatchBase
    return ISyncChangeBatchWithPrerequisite
def _define_ISyncChangeBatchBase2_head():
    class ISyncChangeBatchBase2(win32more.System.WindowsSync.ISyncChangeBatchBase_head):
        Guid = Guid('6fdb596a-d755-4584-bd0c-c0c23a548fbf')
    return ISyncChangeBatchBase2
def _define_ISyncChangeBatchBase2():
    ISyncChangeBatchBase2 = win32more.System.WindowsSync.ISyncChangeBatchBase2_head
    ISyncChangeBatchBase2.SerializeWithOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.SYNC_SERIALIZATION_VERSION,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(17, 'SerializeWithOptions', ((1, 'targetFormatVersion'),(1, 'dwFlags'),(1, 'pbBuffer'),(1, 'pdwSerializedSize'),)))
    win32more.System.WindowsSync.ISyncChangeBatchBase
    return ISyncChangeBatchBase2
def _define_ISyncChangeBatchAdvanced_head():
    class ISyncChangeBatchAdvanced(win32more.System.Com.IUnknown_head):
        Guid = Guid('0f1a4995-cbc8-421d-b550-5d0bebf3e9a5')
    return ISyncChangeBatchAdvanced
def _define_ISyncChangeBatchAdvanced():
    ISyncChangeBatchAdvanced = win32more.System.WindowsSync.ISyncChangeBatchAdvanced_head
    ISyncChangeBatchAdvanced.GetFilterInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncFilterInfo_head), use_last_error=False)(3, 'GetFilterInfo', ((1, 'ppFilterInfo'),)))
    ISyncChangeBatchAdvanced.ConvertFullEnumerationChangeBatchToRegularChangeBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncChangeBatch_head), use_last_error=False)(4, 'ConvertFullEnumerationChangeBatchToRegularChangeBatch', ((1, 'ppChangeBatch'),)))
    ISyncChangeBatchAdvanced.GetUpperBoundItemId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(5, 'GetUpperBoundItemId', ((1, 'pbItemId'),(1, 'pcbIdSize'),)))
    ISyncChangeBatchAdvanced.GetBatchLevelKnowledgeShouldBeApplied = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'GetBatchLevelKnowledgeShouldBeApplied', ((1, 'pfBatchKnowledgeShouldBeApplied'),)))
    win32more.System.Com.IUnknown
    return ISyncChangeBatchAdvanced
def _define_ISyncChangeBatch2_head():
    class ISyncChangeBatch2(win32more.System.WindowsSync.ISyncChangeBatch_head):
        Guid = Guid('225f4a33-f5ee-4cc7-b039-67a262b4b2ac')
    return ISyncChangeBatch2
def _define_ISyncChangeBatch2():
    ISyncChangeBatch2 = win32more.System.WindowsSync.ISyncChangeBatch2_head
    ISyncChangeBatch2.AddMergeTombstoneMetadataToGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head),POINTER(win32more.System.WindowsSync.SYNC_VERSION_head),UInt32,POINTER(win32more.System.WindowsSync.ISyncChangeBuilder_head), use_last_error=False)(20, 'AddMergeTombstoneMetadataToGroup', ((1, 'pbOwnerReplicaId'),(1, 'pbWinnerItemId'),(1, 'pbItemId'),(1, 'pChangeVersion'),(1, 'pCreationVersion'),(1, 'dwWorkForChange'),(1, 'ppChangeBuilder'),)))
    ISyncChangeBatch2.AddMergeTombstoneLoggedConflict = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head),POINTER(win32more.System.WindowsSync.SYNC_VERSION_head),UInt32,win32more.System.WindowsSync.ISyncKnowledge_head,POINTER(win32more.System.WindowsSync.ISyncChangeBuilder_head), use_last_error=False)(21, 'AddMergeTombstoneLoggedConflict', ((1, 'pbOwnerReplicaId'),(1, 'pbWinnerItemId'),(1, 'pbItemId'),(1, 'pChangeVersion'),(1, 'pCreationVersion'),(1, 'dwWorkForChange'),(1, 'pConflictKnowledge'),(1, 'ppChangeBuilder'),)))
    win32more.System.WindowsSync.ISyncChangeBatch
    return ISyncChangeBatch2
def _define_ISyncFullEnumerationChangeBatch2_head():
    class ISyncFullEnumerationChangeBatch2(win32more.System.WindowsSync.ISyncFullEnumerationChangeBatch_head):
        Guid = Guid('e06449f4-a205-4b65-9724-01b22101eec1')
    return ISyncFullEnumerationChangeBatch2
def _define_ISyncFullEnumerationChangeBatch2():
    ISyncFullEnumerationChangeBatch2 = win32more.System.WindowsSync.ISyncFullEnumerationChangeBatch2_head
    ISyncFullEnumerationChangeBatch2.AddMergeTombstoneMetadataToGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head),POINTER(win32more.System.WindowsSync.SYNC_VERSION_head),UInt32,POINTER(win32more.System.WindowsSync.ISyncChangeBuilder_head), use_last_error=False)(20, 'AddMergeTombstoneMetadataToGroup', ((1, 'pbOwnerReplicaId'),(1, 'pbWinnerItemId'),(1, 'pbItemId'),(1, 'pChangeVersion'),(1, 'pCreationVersion'),(1, 'dwWorkForChange'),(1, 'ppChangeBuilder'),)))
    win32more.System.WindowsSync.ISyncFullEnumerationChangeBatch
    return ISyncFullEnumerationChangeBatch2
def _define_IKnowledgeSyncProvider_head():
    class IKnowledgeSyncProvider(win32more.System.WindowsSync.ISyncProvider_head):
        Guid = Guid('43434a49-8da4-47f2-8172-ad7b8b024978')
    return IKnowledgeSyncProvider
def _define_IKnowledgeSyncProvider():
    IKnowledgeSyncProvider = win32more.System.WindowsSync.IKnowledgeSyncProvider_head
    IKnowledgeSyncProvider.BeginSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.SYNC_PROVIDER_ROLE,win32more.System.WindowsSync.ISyncSessionState_head, use_last_error=False)(4, 'BeginSession', ((1, 'role'),(1, 'pSessionState'),)))
    IKnowledgeSyncProvider.GetSyncBatchParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head),POINTER(UInt32), use_last_error=False)(5, 'GetSyncBatchParameters', ((1, 'ppSyncKnowledge'),(1, 'pdwRequestedBatchSize'),)))
    IKnowledgeSyncProvider.GetChangeBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.WindowsSync.ISyncKnowledge_head,POINTER(win32more.System.WindowsSync.ISyncChangeBatch_head),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(6, 'GetChangeBatch', ((1, 'dwBatchSize'),(1, 'pSyncKnowledge'),(1, 'ppSyncChangeBatch'),(1, 'ppUnkDataRetriever'),)))
    IKnowledgeSyncProvider.GetFullEnumerationChangeBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,win32more.System.WindowsSync.ISyncKnowledge_head,POINTER(win32more.System.WindowsSync.ISyncFullEnumerationChangeBatch_head),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'GetFullEnumerationChangeBatch', ((1, 'dwBatchSize'),(1, 'pbLowerEnumerationBound'),(1, 'pSyncKnowledge'),(1, 'ppSyncChangeBatch'),(1, 'ppUnkDataRetriever'),)))
    IKnowledgeSyncProvider.ProcessChangeBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.CONFLICT_RESOLUTION_POLICY,win32more.System.WindowsSync.ISyncChangeBatch_head,win32more.System.Com.IUnknown_head,win32more.System.WindowsSync.ISyncCallback_head,POINTER(win32more.System.WindowsSync.SYNC_SESSION_STATISTICS_head), use_last_error=False)(8, 'ProcessChangeBatch', ((1, 'resolutionPolicy'),(1, 'pSourceChangeBatch'),(1, 'pUnkDataRetriever'),(1, 'pCallback'),(1, 'pSyncSessionStatistics'),)))
    IKnowledgeSyncProvider.ProcessFullEnumerationChangeBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.CONFLICT_RESOLUTION_POLICY,win32more.System.WindowsSync.ISyncFullEnumerationChangeBatch_head,win32more.System.Com.IUnknown_head,win32more.System.WindowsSync.ISyncCallback_head,POINTER(win32more.System.WindowsSync.SYNC_SESSION_STATISTICS_head), use_last_error=False)(9, 'ProcessFullEnumerationChangeBatch', ((1, 'resolutionPolicy'),(1, 'pSourceChangeBatch'),(1, 'pUnkDataRetriever'),(1, 'pCallback'),(1, 'pSyncSessionStatistics'),)))
    IKnowledgeSyncProvider.EndSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncSessionState_head, use_last_error=False)(10, 'EndSession', ((1, 'pSessionState'),)))
    win32more.System.WindowsSync.ISyncProvider
    return IKnowledgeSyncProvider
def _define_ISyncChangeUnit_head():
    class ISyncChangeUnit(win32more.System.Com.IUnknown_head):
        Guid = Guid('60edd8ca-7341-4bb7-95ce-fab6394b51cb')
    return ISyncChangeUnit
def _define_ISyncChangeUnit():
    ISyncChangeUnit = win32more.System.WindowsSync.ISyncChangeUnit_head
    ISyncChangeUnit.GetItemChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncChange_head), use_last_error=False)(3, 'GetItemChange', ((1, 'ppSyncChange'),)))
    ISyncChangeUnit.GetChangeUnitId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(4, 'GetChangeUnitId', ((1, 'pbChangeUnitId'),(1, 'pcbIdSize'),)))
    ISyncChangeUnit.GetChangeUnitVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), use_last_error=False)(5, 'GetChangeUnitVersion', ((1, 'pbCurrentReplicaId'),(1, 'pVersion'),)))
    win32more.System.Com.IUnknown
    return ISyncChangeUnit
def _define_IEnumSyncChangeUnits_head():
    class IEnumSyncChangeUnits(win32more.System.Com.IUnknown_head):
        Guid = Guid('346b35f1-8703-4c6d-ab1a-4dbca2cff97f')
    return IEnumSyncChangeUnits
def _define_IEnumSyncChangeUnits():
    IEnumSyncChangeUnits = win32more.System.WindowsSync.IEnumSyncChangeUnits_head
    IEnumSyncChangeUnits.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.ISyncChangeUnit_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cChanges'),(1, 'ppChangeUnit'),(1, 'pcFetched'),)))
    IEnumSyncChangeUnits.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cChanges'),)))
    IEnumSyncChangeUnits.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumSyncChangeUnits.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IEnumSyncChangeUnits_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumSyncChangeUnits
def _define_ISyncChange_head():
    class ISyncChange(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1952beb-0f6b-4711-b136-01da85b968a6')
    return ISyncChange
def _define_ISyncChange():
    ISyncChange = win32more.System.WindowsSync.ISyncChange_head
    ISyncChange.GetOwnerReplicaId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'GetOwnerReplicaId', ((1, 'pbReplicaId'),(1, 'pcbIdSize'),)))
    ISyncChange.GetRootItemId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(4, 'GetRootItemId', ((1, 'pbRootItemId'),(1, 'pcbIdSize'),)))
    ISyncChange.GetChangeVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), use_last_error=False)(5, 'GetChangeVersion', ((1, 'pbCurrentReplicaId'),(1, 'pVersion'),)))
    ISyncChange.GetCreationVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), use_last_error=False)(6, 'GetCreationVersion', ((1, 'pbCurrentReplicaId'),(1, 'pVersion'),)))
    ISyncChange.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetFlags', ((1, 'pdwFlags'),)))
    ISyncChange.GetWorkEstimate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetWorkEstimate', ((1, 'pdwWork'),)))
    ISyncChange.GetChangeUnits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IEnumSyncChangeUnits_head), use_last_error=False)(9, 'GetChangeUnits', ((1, 'ppEnum'),)))
    ISyncChange.GetMadeWithKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(10, 'GetMadeWithKnowledge', ((1, 'ppMadeWithKnowledge'),)))
    ISyncChange.GetLearnedKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(11, 'GetLearnedKnowledge', ((1, 'ppLearnedKnowledge'),)))
    ISyncChange.SetWorkEstimate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(12, 'SetWorkEstimate', ((1, 'dwWork'),)))
    win32more.System.Com.IUnknown
    return ISyncChange
def _define_ISyncChangeWithPrerequisite_head():
    class ISyncChangeWithPrerequisite(win32more.System.Com.IUnknown_head):
        Guid = Guid('9e38382f-1589-48c3-92e4-05ecdcb4f3f7')
    return ISyncChangeWithPrerequisite
def _define_ISyncChangeWithPrerequisite():
    ISyncChangeWithPrerequisite = win32more.System.WindowsSync.ISyncChangeWithPrerequisite_head
    ISyncChangeWithPrerequisite.GetPrerequisiteKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(3, 'GetPrerequisiteKnowledge', ((1, 'ppPrerequisiteKnowledge'),)))
    ISyncChangeWithPrerequisite.GetLearnedKnowledgeWithPrerequisite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(4, 'GetLearnedKnowledgeWithPrerequisite', ((1, 'pDestinationKnowledge'),(1, 'ppLearnedKnowledgeWithPrerequisite'),)))
    win32more.System.Com.IUnknown
    return ISyncChangeWithPrerequisite
def _define_ISyncFullEnumerationChange_head():
    class ISyncFullEnumerationChange(win32more.System.Com.IUnknown_head):
        Guid = Guid('9785e0bd-bdff-40c4-98c5-b34b2f1991b3')
    return ISyncFullEnumerationChange
def _define_ISyncFullEnumerationChange():
    ISyncFullEnumerationChange = win32more.System.WindowsSync.ISyncFullEnumerationChange_head
    ISyncFullEnumerationChange.GetLearnedKnowledgeAfterRecoveryComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(3, 'GetLearnedKnowledgeAfterRecoveryComplete', ((1, 'ppLearnedKnowledge'),)))
    ISyncFullEnumerationChange.GetLearnedForgottenKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IForgottenKnowledge_head), use_last_error=False)(4, 'GetLearnedForgottenKnowledge', ((1, 'ppLearnedForgottenKnowledge'),)))
    win32more.System.Com.IUnknown
    return ISyncFullEnumerationChange
def _define_ISyncMergeTombstoneChange_head():
    class ISyncMergeTombstoneChange(win32more.System.Com.IUnknown_head):
        Guid = Guid('6ec62597-0903-484c-ad61-36d6e938f47b')
    return ISyncMergeTombstoneChange
def _define_ISyncMergeTombstoneChange():
    ISyncMergeTombstoneChange = win32more.System.WindowsSync.ISyncMergeTombstoneChange_head
    ISyncMergeTombstoneChange.GetWinnerItemId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'GetWinnerItemId', ((1, 'pbWinnerItemId'),(1, 'pcbIdSize'),)))
    win32more.System.Com.IUnknown
    return ISyncMergeTombstoneChange
def _define_IEnumItemIds_head():
    class IEnumItemIds(win32more.System.Com.IUnknown_head):
        Guid = Guid('43aa3f61-4b2e-4b60-83df-b110d3e148f1')
    return IEnumItemIds
def _define_IEnumItemIds():
    IEnumItemIds = win32more.System.WindowsSync.IEnumItemIds_head
    IEnumItemIds.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'pbItemId'),(1, 'pcbItemIdSize'),)))
    win32more.System.Com.IUnknown
    return IEnumItemIds
def _define_IFilterKeyMap_head():
    class IFilterKeyMap(win32more.System.Com.IUnknown_head):
        Guid = Guid('ca169652-07c6-4708-a3da-6e4eba8d2297')
    return IFilterKeyMap
def _define_IFilterKeyMap():
    IFilterKeyMap = win32more.System.WindowsSync.IFilterKeyMap_head
    IFilterKeyMap.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pdwCount'),)))
    IFilterKeyMap.AddFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncFilter_head,POINTER(UInt32), use_last_error=False)(4, 'AddFilter', ((1, 'pISyncFilter'),(1, 'pdwFilterKey'),)))
    IFilterKeyMap.GetFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.ISyncFilter_head), use_last_error=False)(5, 'GetFilter', ((1, 'dwFilterKey'),(1, 'ppISyncFilter'),)))
    IFilterKeyMap.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(6, 'Serialize', ((1, 'pbFilterKeyMap'),(1, 'pcbFilterKeyMap'),)))
    win32more.System.Com.IUnknown
    return IFilterKeyMap
def _define_ISyncChangeWithFilterKeyMap_head():
    class ISyncChangeWithFilterKeyMap(win32more.System.Com.IUnknown_head):
        Guid = Guid('bfe1ef00-e87d-42fd-a4e9-242d70414aef')
    return ISyncChangeWithFilterKeyMap
def _define_ISyncChangeWithFilterKeyMap():
    ISyncChangeWithFilterKeyMap = win32more.System.WindowsSync.ISyncChangeWithFilterKeyMap_head
    ISyncChangeWithFilterKeyMap.GetFilterCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetFilterCount', ((1, 'pdwFilterCount'),)))
    ISyncChangeWithFilterKeyMap.GetFilterChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.SYNC_FILTER_CHANGE_head), use_last_error=False)(4, 'GetFilterChange', ((1, 'dwFilterKey'),(1, 'pFilterChange'),)))
    ISyncChangeWithFilterKeyMap.GetAllChangeUnitsPresentFlag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'GetAllChangeUnitsPresentFlag', ((1, 'pfAllChangeUnitsPresent'),)))
    ISyncChangeWithFilterKeyMap.GetFilterForgottenKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(6, 'GetFilterForgottenKnowledge', ((1, 'dwFilterKey'),(1, 'ppIFilterForgottenKnowledge'),)))
    ISyncChangeWithFilterKeyMap.GetFilteredReplicaLearnedKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.System.WindowsSync.IEnumItemIds_head,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(7, 'GetFilteredReplicaLearnedKnowledge', ((1, 'pDestinationKnowledge'),(1, 'pNewMoveins'),(1, 'ppLearnedKnowledge'),)))
    ISyncChangeWithFilterKeyMap.GetLearnedFilterForgottenKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.System.WindowsSync.IEnumItemIds_head,UInt32,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(8, 'GetLearnedFilterForgottenKnowledge', ((1, 'pDestinationKnowledge'),(1, 'pNewMoveins'),(1, 'dwFilterKey'),(1, 'ppLearnedFilterForgottenKnowledge'),)))
    ISyncChangeWithFilterKeyMap.GetFilteredReplicaLearnedForgottenKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.System.WindowsSync.IEnumItemIds_head,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(9, 'GetFilteredReplicaLearnedForgottenKnowledge', ((1, 'pDestinationKnowledge'),(1, 'pNewMoveins'),(1, 'ppLearnedForgottenKnowledge'),)))
    ISyncChangeWithFilterKeyMap.GetFilteredReplicaLearnedForgottenKnowledgeAfterRecoveryComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.System.WindowsSync.IEnumItemIds_head,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(10, 'GetFilteredReplicaLearnedForgottenKnowledgeAfterRecoveryComplete', ((1, 'pDestinationKnowledge'),(1, 'pNewMoveins'),(1, 'ppLearnedForgottenKnowledge'),)))
    ISyncChangeWithFilterKeyMap.GetLearnedFilterForgottenKnowledgeAfterRecoveryComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.System.WindowsSync.IEnumItemIds_head,UInt32,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(11, 'GetLearnedFilterForgottenKnowledgeAfterRecoveryComplete', ((1, 'pDestinationKnowledge'),(1, 'pNewMoveins'),(1, 'dwFilterKey'),(1, 'ppLearnedFilterForgottenKnowledge'),)))
    win32more.System.Com.IUnknown
    return ISyncChangeWithFilterKeyMap
def _define_ISyncChangeBatchWithFilterKeyMap_head():
    class ISyncChangeBatchWithFilterKeyMap(win32more.System.Com.IUnknown_head):
        Guid = Guid('de247002-566d-459a-a6ed-a5aab3459fb7')
    return ISyncChangeBatchWithFilterKeyMap
def _define_ISyncChangeBatchWithFilterKeyMap():
    ISyncChangeBatchWithFilterKeyMap = win32more.System.WindowsSync.ISyncChangeBatchWithFilterKeyMap_head
    ISyncChangeBatchWithFilterKeyMap.GetFilterKeyMap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IFilterKeyMap_head), use_last_error=False)(3, 'GetFilterKeyMap', ((1, 'ppIFilterKeyMap'),)))
    ISyncChangeBatchWithFilterKeyMap.SetFilterKeyMap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.IFilterKeyMap_head, use_last_error=False)(4, 'SetFilterKeyMap', ((1, 'pIFilterKeyMap'),)))
    ISyncChangeBatchWithFilterKeyMap.SetFilterForgottenKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.WindowsSync.ISyncKnowledge_head, use_last_error=False)(5, 'SetFilterForgottenKnowledge', ((1, 'dwFilterKey'),(1, 'pFilterForgottenKnowledge'),)))
    ISyncChangeBatchWithFilterKeyMap.GetFilteredReplicaLearnedKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.System.WindowsSync.IEnumItemIds_head,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(6, 'GetFilteredReplicaLearnedKnowledge', ((1, 'pDestinationKnowledge'),(1, 'pNewMoveins'),(1, 'ppLearnedForgottenKnowledge'),)))
    ISyncChangeBatchWithFilterKeyMap.GetLearnedFilterForgottenKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.System.WindowsSync.IEnumItemIds_head,UInt32,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(7, 'GetLearnedFilterForgottenKnowledge', ((1, 'pDestinationKnowledge'),(1, 'pNewMoveins'),(1, 'dwFilterKey'),(1, 'ppLearnedFilterForgottenKnowledge'),)))
    ISyncChangeBatchWithFilterKeyMap.GetFilteredReplicaLearnedForgottenKnowledge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.System.WindowsSync.IEnumItemIds_head,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(8, 'GetFilteredReplicaLearnedForgottenKnowledge', ((1, 'pDestinationKnowledge'),(1, 'pNewMoveins'),(1, 'ppLearnedForgottenKnowledge'),)))
    ISyncChangeBatchWithFilterKeyMap.GetFilteredReplicaLearnedForgottenKnowledgeAfterRecoveryComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.System.WindowsSync.IEnumItemIds_head,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(9, 'GetFilteredReplicaLearnedForgottenKnowledgeAfterRecoveryComplete', ((1, 'pDestinationKnowledge'),(1, 'pNewMoveins'),(1, 'ppLearnedForgottenKnowledge'),)))
    ISyncChangeBatchWithFilterKeyMap.GetLearnedFilterForgottenKnowledgeAfterRecoveryComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncKnowledge_head,win32more.System.WindowsSync.IEnumItemIds_head,UInt32,POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), use_last_error=False)(10, 'GetLearnedFilterForgottenKnowledgeAfterRecoveryComplete', ((1, 'pDestinationKnowledge'),(1, 'pNewMoveins'),(1, 'dwFilterKey'),(1, 'ppLearnedFilterForgottenKnowledge'),)))
    win32more.System.Com.IUnknown
    return ISyncChangeBatchWithFilterKeyMap
def _define_IDataRetrieverCallback_head():
    class IDataRetrieverCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('71b4863b-f969-4676-bbc3-3d9fdc3fb2c7')
    return IDataRetrieverCallback
def _define_IDataRetrieverCallback():
    IDataRetrieverCallback = win32more.System.WindowsSync.IDataRetrieverCallback_head
    IDataRetrieverCallback.LoadChangeDataComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'LoadChangeDataComplete', ((1, 'pUnkData'),)))
    IDataRetrieverCallback.LoadChangeDataError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(4, 'LoadChangeDataError', ((1, 'hrError'),)))
    win32more.System.Com.IUnknown
    return IDataRetrieverCallback
def _define_ILoadChangeContext_head():
    class ILoadChangeContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('44a4aaca-ec39-46d5-b5c9-d633c0ee67e2')
    return ILoadChangeContext
def _define_ILoadChangeContext():
    ILoadChangeContext = win32more.System.WindowsSync.ILoadChangeContext_head
    ILoadChangeContext.GetSyncChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ISyncChange_head), use_last_error=False)(3, 'GetSyncChange', ((1, 'ppSyncChange'),)))
    ILoadChangeContext.SetRecoverableErrorOnChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.System.WindowsSync.IRecoverableErrorData_head, use_last_error=False)(4, 'SetRecoverableErrorOnChange', ((1, 'hrError'),(1, 'pErrorData'),)))
    ILoadChangeContext.SetRecoverableErrorOnChangeUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncChangeUnit_head,win32more.System.WindowsSync.IRecoverableErrorData_head, use_last_error=False)(5, 'SetRecoverableErrorOnChangeUnit', ((1, 'hrError'),(1, 'pChangeUnit'),(1, 'pErrorData'),)))
    win32more.System.Com.IUnknown
    return ILoadChangeContext
def _define_ISynchronousDataRetriever_head():
    class ISynchronousDataRetriever(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b22f2a9-a4cd-4648-9d8e-3a510d4da04b')
    return ISynchronousDataRetriever
def _define_ISynchronousDataRetriever():
    ISynchronousDataRetriever = win32more.System.WindowsSync.ISynchronousDataRetriever_head
    ISynchronousDataRetriever.GetIdParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ID_PARAMETERS_head), use_last_error=False)(3, 'GetIdParameters', ((1, 'pIdParameters'),)))
    ISynchronousDataRetriever.LoadChangeData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ILoadChangeContext_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(4, 'LoadChangeData', ((1, 'pLoadChangeContext'),(1, 'ppUnkData'),)))
    win32more.System.Com.IUnknown
    return ISynchronousDataRetriever
def _define_IAsynchronousDataRetriever_head():
    class IAsynchronousDataRetriever(win32more.System.Com.IUnknown_head):
        Guid = Guid('9fc7e470-61ea-4a88-9be4-df56a27cfef2')
    return IAsynchronousDataRetriever
def _define_IAsynchronousDataRetriever():
    IAsynchronousDataRetriever = win32more.System.WindowsSync.IAsynchronousDataRetriever_head
    IAsynchronousDataRetriever.GetIdParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.ID_PARAMETERS_head), use_last_error=False)(3, 'GetIdParameters', ((1, 'pIdParameters'),)))
    IAsynchronousDataRetriever.RegisterCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.IDataRetrieverCallback_head, use_last_error=False)(4, 'RegisterCallback', ((1, 'pDataRetrieverCallback'),)))
    IAsynchronousDataRetriever.RevokeCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.IDataRetrieverCallback_head, use_last_error=False)(5, 'RevokeCallback', ((1, 'pDataRetrieverCallback'),)))
    IAsynchronousDataRetriever.LoadChangeData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ILoadChangeContext_head, use_last_error=False)(6, 'LoadChangeData', ((1, 'pLoadChangeContext'),)))
    win32more.System.Com.IUnknown
    return IAsynchronousDataRetriever
def _define_IFilterRequestCallback_head():
    class IFilterRequestCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('82df8873-6360-463a-a8a1-ede5e1a1594d')
    return IFilterRequestCallback
def _define_IFilterRequestCallback():
    IFilterRequestCallback = win32more.System.WindowsSync.IFilterRequestCallback_head
    IFilterRequestCallback.RequestFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.WindowsSync.FILTERING_TYPE, use_last_error=False)(3, 'RequestFilter', ((1, 'pFilter'),(1, 'filteringType'),)))
    win32more.System.Com.IUnknown
    return IFilterRequestCallback
def _define_IRequestFilteredSync_head():
    class IRequestFilteredSync(win32more.System.Com.IUnknown_head):
        Guid = Guid('2e020184-6d18-46a7-a32a-da4aeb06696c')
    return IRequestFilteredSync
def _define_IRequestFilteredSync():
    IRequestFilteredSync = win32more.System.WindowsSync.IRequestFilteredSync_head
    IRequestFilteredSync.SpecifyFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.IFilterRequestCallback_head, use_last_error=False)(3, 'SpecifyFilter', ((1, 'pCallback'),)))
    win32more.System.Com.IUnknown
    return IRequestFilteredSync
def _define_ISupportFilteredSync_head():
    class ISupportFilteredSync(win32more.System.Com.IUnknown_head):
        Guid = Guid('3d128ded-d555-4e0d-bf4b-fb213a8a9302')
    return ISupportFilteredSync
def _define_ISupportFilteredSync():
    ISupportFilteredSync = win32more.System.WindowsSync.ISupportFilteredSync_head
    ISupportFilteredSync.AddFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.WindowsSync.FILTERING_TYPE, use_last_error=False)(3, 'AddFilter', ((1, 'pFilter'),(1, 'filteringType'),)))
    win32more.System.Com.IUnknown
    return ISupportFilteredSync
def _define_IFilterTrackingRequestCallback_head():
    class IFilterTrackingRequestCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('713ca7bb-c858-4674-b4b6-1122436587a9')
    return IFilterTrackingRequestCallback
def _define_IFilterTrackingRequestCallback():
    IFilterTrackingRequestCallback = win32more.System.WindowsSync.IFilterTrackingRequestCallback_head
    IFilterTrackingRequestCallback.RequestTrackedFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncFilter_head, use_last_error=False)(3, 'RequestTrackedFilter', ((1, 'pFilter'),)))
    win32more.System.Com.IUnknown
    return IFilterTrackingRequestCallback
def _define_IFilterTrackingProvider_head():
    class IFilterTrackingProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('743383c0-fc4e-45ba-ad81-d9d84c7a24f8')
    return IFilterTrackingProvider
def _define_IFilterTrackingProvider():
    IFilterTrackingProvider = win32more.System.WindowsSync.IFilterTrackingProvider_head
    IFilterTrackingProvider.SpecifyTrackedFilters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.IFilterTrackingRequestCallback_head, use_last_error=False)(3, 'SpecifyTrackedFilters', ((1, 'pCallback'),)))
    IFilterTrackingProvider.AddTrackedFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncFilter_head, use_last_error=False)(4, 'AddTrackedFilter', ((1, 'pFilter'),)))
    win32more.System.Com.IUnknown
    return IFilterTrackingProvider
def _define_ISupportLastWriteTime_head():
    class ISupportLastWriteTime(win32more.System.Com.IUnknown_head):
        Guid = Guid('eadf816f-d0bd-43ca-8f40-5acdc6c06f7a')
    return ISupportLastWriteTime
def _define_ISupportLastWriteTime():
    ISupportLastWriteTime = win32more.System.WindowsSync.ISupportLastWriteTime_head
    ISupportLastWriteTime.GetItemChangeTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt64), use_last_error=False)(3, 'GetItemChangeTime', ((1, 'pbItemId'),(1, 'pullTimestamp'),)))
    ISupportLastWriteTime.GetChangeUnitChangeTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no,POINTER(UInt64), use_last_error=False)(4, 'GetChangeUnitChangeTime', ((1, 'pbItemId'),(1, 'pbChangeUnitId'),(1, 'pullTimestamp'),)))
    win32more.System.Com.IUnknown
    return ISupportLastWriteTime
def _define_IProviderConverter_head():
    class IProviderConverter(win32more.System.Com.IUnknown_head):
        Guid = Guid('809b7276-98cf-4957-93a5-0ebdd3dddffd')
    return IProviderConverter
def _define_IProviderConverter():
    IProviderConverter = win32more.System.WindowsSync.IProviderConverter_head
    IProviderConverter.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ISyncProvider_head, use_last_error=False)(3, 'Initialize', ((1, 'pISyncProvider'),)))
    win32more.System.Com.IUnknown
    return IProviderConverter
def _define_ISyncDataConverter_head():
    class ISyncDataConverter(win32more.System.Com.IUnknown_head):
        Guid = Guid('435d4861-68d5-44aa-a0f9-72a0b00ef9cf')
    return ISyncDataConverter
def _define_ISyncDataConverter():
    ISyncDataConverter = win32more.System.WindowsSync.ISyncDataConverter_head
    ISyncDataConverter.ConvertDataRetrieverFromProviderFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.WindowsSync.IEnumSyncChanges_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'ConvertDataRetrieverFromProviderFormat', ((1, 'pUnkDataRetrieverIn'),(1, 'pEnumSyncChanges'),(1, 'ppUnkDataOut'),)))
    ISyncDataConverter.ConvertDataRetrieverToProviderFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.WindowsSync.IEnumSyncChanges_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(4, 'ConvertDataRetrieverToProviderFormat', ((1, 'pUnkDataRetrieverIn'),(1, 'pEnumSyncChanges'),(1, 'ppUnkDataOut'),)))
    ISyncDataConverter.ConvertDataFromProviderFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ILoadChangeContext_head,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(5, 'ConvertDataFromProviderFormat', ((1, 'pDataContext'),(1, 'pUnkDataIn'),(1, 'ppUnkDataOut'),)))
    ISyncDataConverter.ConvertDataToProviderFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsSync.ILoadChangeContext_head,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(6, 'ConvertDataToProviderFormat', ((1, 'pDataContext'),(1, 'pUnkDataOut'),(1, 'ppUnkDataout'),)))
    win32more.System.Com.IUnknown
    return ISyncDataConverter
SyncProviderRegistration = Guid('f82b4ef1-93a9-4dde-8015-f7950a1a6e31')
def _define_SyncProviderConfiguration_head():
    class SyncProviderConfiguration(Structure):
        pass
    return SyncProviderConfiguration
def _define_SyncProviderConfiguration():
    SyncProviderConfiguration = win32more.System.WindowsSync.SyncProviderConfiguration_head
    SyncProviderConfiguration._fields_ = [
        ("dwVersion", UInt32),
        ("guidInstanceId", Guid),
        ("clsidProvider", Guid),
        ("guidConfigUIInstanceId", Guid),
        ("guidContentType", Guid),
        ("dwCapabilities", UInt32),
        ("dwSupportedArchitecture", UInt32),
    ]
    return SyncProviderConfiguration
def _define_SyncProviderConfigUIConfiguration_head():
    class SyncProviderConfigUIConfiguration(Structure):
        pass
    return SyncProviderConfigUIConfiguration
def _define_SyncProviderConfigUIConfiguration():
    SyncProviderConfigUIConfiguration = win32more.System.WindowsSync.SyncProviderConfigUIConfiguration_head
    SyncProviderConfigUIConfiguration._fields_ = [
        ("dwVersion", UInt32),
        ("guidInstanceId", Guid),
        ("clsidConfigUI", Guid),
        ("guidContentType", Guid),
        ("dwCapabilities", UInt32),
        ("dwSupportedArchitecture", UInt32),
        ("fIsGlobal", win32more.Foundation.BOOL),
    ]
    return SyncProviderConfigUIConfiguration
def _define_ISyncProviderRegistration_head():
    class ISyncProviderRegistration(win32more.System.Com.IUnknown_head):
        Guid = Guid('cb45953b-7624-47bc-a472-eb8cac6b222e')
    return ISyncProviderRegistration
def _define_ISyncProviderRegistration():
    ISyncProviderRegistration = win32more.System.WindowsSync.ISyncProviderRegistration_head
    ISyncProviderRegistration.CreateSyncProviderConfigUIRegistrationInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SyncProviderConfigUIConfiguration_head),POINTER(win32more.System.WindowsSync.ISyncProviderConfigUIInfo_head), use_last_error=False)(3, 'CreateSyncProviderConfigUIRegistrationInstance', ((1, 'pConfigUIConfig'),(1, 'ppConfigUIInfo'),)))
    ISyncProviderRegistration.UnregisterSyncProviderConfigUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'UnregisterSyncProviderConfigUI', ((1, 'pguidInstanceId'),)))
    ISyncProviderRegistration.EnumerateSyncProviderConfigUIs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.System.WindowsSync.IEnumSyncProviderConfigUIInfos_head), use_last_error=False)(5, 'EnumerateSyncProviderConfigUIs', ((1, 'pguidContentType'),(1, 'dwSupportedArchitecture'),(1, 'ppEnumSyncProviderConfigUIInfos'),)))
    ISyncProviderRegistration.CreateSyncProviderRegistrationInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SyncProviderConfiguration_head),POINTER(win32more.System.WindowsSync.ISyncProviderInfo_head), use_last_error=False)(6, 'CreateSyncProviderRegistrationInstance', ((1, 'pProviderConfiguration'),(1, 'ppProviderInfo'),)))
    ISyncProviderRegistration.UnregisterSyncProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(7, 'UnregisterSyncProvider', ((1, 'pguidInstanceId'),)))
    ISyncProviderRegistration.GetSyncProviderConfigUIInfoforProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.WindowsSync.ISyncProviderConfigUIInfo_head), use_last_error=False)(8, 'GetSyncProviderConfigUIInfoforProvider', ((1, 'pguidProviderInstanceId'),(1, 'ppProviderConfigUIInfo'),)))
    ISyncProviderRegistration.EnumerateSyncProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,UInt32,POINTER(Guid),UInt32,POINTER(win32more.System.WindowsSync.IEnumSyncProviderInfos_head), use_last_error=False)(9, 'EnumerateSyncProviders', ((1, 'pguidContentType'),(1, 'dwStateFlagsToFilterMask'),(1, 'dwStateFlagsToFilter'),(1, 'refProviderClsId'),(1, 'dwSupportedArchitecture'),(1, 'ppEnumSyncProviderInfos'),)))
    ISyncProviderRegistration.GetSyncProviderInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.WindowsSync.ISyncProviderInfo_head), use_last_error=False)(10, 'GetSyncProviderInfo', ((1, 'pguidInstanceId'),(1, 'ppProviderInfo'),)))
    ISyncProviderRegistration.GetSyncProviderFromInstanceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.System.WindowsSync.IRegisteredSyncProvider_head), use_last_error=False)(11, 'GetSyncProviderFromInstanceId', ((1, 'pguidInstanceId'),(1, 'dwClsContext'),(1, 'ppSyncProvider'),)))
    ISyncProviderRegistration.GetSyncProviderConfigUIInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.WindowsSync.ISyncProviderConfigUIInfo_head), use_last_error=False)(12, 'GetSyncProviderConfigUIInfo', ((1, 'pguidInstanceId'),(1, 'ppConfigUIInfo'),)))
    ISyncProviderRegistration.GetSyncProviderConfigUIFromInstanceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.System.WindowsSync.ISyncProviderConfigUI_head), use_last_error=False)(13, 'GetSyncProviderConfigUIFromInstanceId', ((1, 'pguidInstanceId'),(1, 'dwClsContext'),(1, 'ppConfigUI'),)))
    ISyncProviderRegistration.GetSyncProviderState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32), use_last_error=False)(14, 'GetSyncProviderState', ((1, 'pguidInstanceId'),(1, 'pdwStateFlags'),)))
    ISyncProviderRegistration.SetSyncProviderState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,UInt32, use_last_error=False)(15, 'SetSyncProviderState', ((1, 'pguidInstanceId'),(1, 'dwStateFlagsMask'),(1, 'dwStateFlags'),)))
    ISyncProviderRegistration.RegisterForEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(16, 'RegisterForEvent', ((1, 'phEvent'),)))
    ISyncProviderRegistration.RevokeEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(17, 'RevokeEvent', ((1, 'hEvent'),)))
    ISyncProviderRegistration.GetChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.System.WindowsSync.ISyncRegistrationChange_head), use_last_error=False)(18, 'GetChange', ((1, 'hEvent'),(1, 'ppChange'),)))
    win32more.System.Com.IUnknown
    return ISyncProviderRegistration
def _define_IEnumSyncProviderConfigUIInfos_head():
    class IEnumSyncProviderConfigUIInfos(win32more.System.Com.IUnknown_head):
        Guid = Guid('f6be2602-17c6-4658-a2d7-68ed3330f641')
    return IEnumSyncProviderConfigUIInfos
def _define_IEnumSyncProviderConfigUIInfos():
    IEnumSyncProviderConfigUIInfos = win32more.System.WindowsSync.IEnumSyncProviderConfigUIInfos_head
    IEnumSyncProviderConfigUIInfos.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.ISyncProviderConfigUIInfo_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cFactories'),(1, 'ppSyncProviderConfigUIInfo'),(1, 'pcFetched'),)))
    IEnumSyncProviderConfigUIInfos.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cFactories'),)))
    IEnumSyncProviderConfigUIInfos.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumSyncProviderConfigUIInfos.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IEnumSyncProviderConfigUIInfos_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumSyncProviderConfigUIInfos
def _define_IEnumSyncProviderInfos_head():
    class IEnumSyncProviderInfos(win32more.System.Com.IUnknown_head):
        Guid = Guid('a04ba850-5eb1-460d-a973-393fcb608a11')
    return IEnumSyncProviderInfos
def _define_IEnumSyncProviderInfos():
    IEnumSyncProviderInfos = win32more.System.WindowsSync.IEnumSyncProviderInfos_head
    IEnumSyncProviderInfos.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.ISyncProviderInfo_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cInstances'),(1, 'ppSyncProviderInfo'),(1, 'pcFetched'),)))
    IEnumSyncProviderInfos.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cInstances'),)))
    IEnumSyncProviderInfos.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumSyncProviderInfos.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.IEnumSyncProviderInfos_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumSyncProviderInfos
def _define_ISyncProviderInfo_head():
    class ISyncProviderInfo(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head):
        Guid = Guid('1ee135de-88a4-4504-b0d0-f7920d7e5ba6')
    return ISyncProviderInfo
def _define_ISyncProviderInfo():
    ISyncProviderInfo = win32more.System.WindowsSync.ISyncProviderInfo_head
    ISyncProviderInfo.GetSyncProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.IRegisteredSyncProvider_head), use_last_error=False)(8, 'GetSyncProvider', ((1, 'dwClsContext'),(1, 'ppSyncProvider'),)))
    win32more.UI.Shell.PropertiesSystem.IPropertyStore
    return ISyncProviderInfo
def _define_ISyncProviderConfigUIInfo_head():
    class ISyncProviderConfigUIInfo(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head):
        Guid = Guid('214141ae-33d7-4d8d-8e37-f227e880ce50')
    return ISyncProviderConfigUIInfo
def _define_ISyncProviderConfigUIInfo():
    ISyncProviderConfigUIInfo = win32more.System.WindowsSync.ISyncProviderConfigUIInfo_head
    ISyncProviderConfigUIInfo.GetSyncProviderConfigUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.WindowsSync.ISyncProviderConfigUI_head), use_last_error=False)(8, 'GetSyncProviderConfigUI', ((1, 'dwClsContext'),(1, 'ppSyncProviderConfigUI'),)))
    win32more.UI.Shell.PropertiesSystem.IPropertyStore
    return ISyncProviderConfigUIInfo
def _define_ISyncProviderConfigUI_head():
    class ISyncProviderConfigUI(win32more.System.Com.IUnknown_head):
        Guid = Guid('7b0705f6-cbcd-4071-ab05-3bdc364d4a0c')
    return ISyncProviderConfigUI
def _define_ISyncProviderConfigUI():
    ISyncProviderConfigUI = win32more.System.WindowsSync.ISyncProviderConfigUI_head
    ISyncProviderConfigUI.Init = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, use_last_error=False)(3, 'Init', ((1, 'pguidInstanceId'),(1, 'pguidContentType'),(1, 'pConfigurationProperties'),)))
    ISyncProviderConfigUI.GetRegisteredProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(4, 'GetRegisteredProperties', ((1, 'ppConfigUIProperties'),)))
    ISyncProviderConfigUI.CreateAndRegisterNewSyncProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.Com.IUnknown_head,POINTER(win32more.System.WindowsSync.ISyncProviderInfo_head), use_last_error=False)(5, 'CreateAndRegisterNewSyncProvider', ((1, 'hwndParent'),(1, 'pUnkContext'),(1, 'ppProviderInfo'),)))
    ISyncProviderConfigUI.ModifySyncProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.Com.IUnknown_head,win32more.System.WindowsSync.ISyncProviderInfo_head, use_last_error=False)(6, 'ModifySyncProvider', ((1, 'hwndParent'),(1, 'pUnkContext'),(1, 'pProviderInfo'),)))
    win32more.System.Com.IUnknown
    return ISyncProviderConfigUI
def _define_IRegisteredSyncProvider_head():
    class IRegisteredSyncProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('913bcf76-47c1-40b5-a896-5e8a9c414c14')
    return IRegisteredSyncProvider
def _define_IRegisteredSyncProvider():
    IRegisteredSyncProvider = win32more.System.WindowsSync.IRegisteredSyncProvider_head
    IRegisteredSyncProvider.Init = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, use_last_error=False)(3, 'Init', ((1, 'pguidInstanceId'),(1, 'pguidContentType'),(1, 'pContextPropertyStore'),)))
    IRegisteredSyncProvider.GetInstanceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'GetInstanceId', ((1, 'pguidInstanceId'),)))
    IRegisteredSyncProvider.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    win32more.System.Com.IUnknown
    return IRegisteredSyncProvider
SYNC_REGISTRATION_EVENT = Int32
SRE_PROVIDER_ADDED = 0
SRE_PROVIDER_REMOVED = 1
SRE_PROVIDER_UPDATED = 2
SRE_PROVIDER_STATE_CHANGED = 3
SRE_CONFIGUI_ADDED = 4
SRE_CONFIGUI_REMOVED = 5
SRE_CONFIGUI_UPDATED = 6
def _define_ISyncRegistrationChange_head():
    class ISyncRegistrationChange(win32more.System.Com.IUnknown_head):
        Guid = Guid('eea0d9ae-6b29-43b4-9e70-e3ae33bb2c3b')
    return ISyncRegistrationChange
def _define_ISyncRegistrationChange():
    ISyncRegistrationChange = win32more.System.WindowsSync.ISyncRegistrationChange_head
    ISyncRegistrationChange.GetEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsSync.SYNC_REGISTRATION_EVENT), use_last_error=False)(3, 'GetEvent', ((1, 'psreEvent'),)))
    ISyncRegistrationChange.GetInstanceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'GetInstanceId', ((1, 'pguidInstanceId'),)))
    win32more.System.Com.IUnknown
    return ISyncRegistrationChange
__all__ = [
    "SYNC_VERSION_FLAG_FROM_FEED",
    "SYNC_VERSION_FLAG_HAS_BY",
    "SYNC_SERIALIZE_REPLICA_KEY_MAP",
    "SYNC_FILTER_INFO_FLAG_ITEM_LIST",
    "SYNC_FILTER_INFO_FLAG_CHANGE_UNIT_LIST",
    "SYNC_FILTER_INFO_FLAG_CUSTOM",
    "SYNC_FILTER_INFO_COMBINED",
    "SYNC_CHANGE_FLAG_DELETED",
    "SYNC_CHANGE_FLAG_DOES_NOT_EXIST",
    "SYNC_CHANGE_FLAG_GHOST",
    "PKEY_PROVIDER_INSTANCEID",
    "PKEY_PROVIDER_CLSID",
    "PKEY_PROVIDER_CONFIGUI",
    "PKEY_PROVIDER_CONTENTTYPE",
    "PKEY_PROVIDER_CAPABILITIES",
    "PKEY_PROVIDER_SUPPORTED_ARCHITECTURE",
    "PKEY_PROVIDER_NAME",
    "PKEY_PROVIDER_DESCRIPTION",
    "PKEY_PROVIDER_TOOLTIPS",
    "PKEY_PROVIDER_ICON",
    "PKEY_CONFIGUI_INSTANCEID",
    "PKEY_CONFIGUI_CLSID",
    "PKEY_CONFIGUI_CONTENTTYPE",
    "PKEY_CONFIGUI_CAPABILITIES",
    "PKEY_CONFIGUI_SUPPORTED_ARCHITECTURE",
    "PKEY_CONFIGUI_IS_GLOBAL",
    "PKEY_CONFIGUI_NAME",
    "PKEY_CONFIGUI_DESCRIPTION",
    "PKEY_CONFIGUI_TOOLTIPS",
    "PKEY_CONFIGUI_ICON",
    "PKEY_CONFIGUI_MENUITEM_NOUI",
    "PKEY_CONFIGUI_MENUITEM",
    "ID_PARAMETER_PAIR",
    "ID_PARAMETERS",
    "SYNC_SESSION_STATISTICS",
    "SYNC_VERSION",
    "SYNC_RANGE",
    "SYNC_TIME",
    "SYNC_FILTER_CHANGE",
    "SYNC_PROVIDER_ROLE",
    "SPR_SOURCE",
    "SPR_DESTINATION",
    "CONFLICT_RESOLUTION_POLICY",
    "CRP_NONE",
    "CRP_DESTINATION_PROVIDER_WINS",
    "CRP_SOURCE_PROVIDER_WINS",
    "CRP_LAST",
    "SYNC_PROGRESS_STAGE",
    "SPS_CHANGE_DETECTION",
    "SPS_CHANGE_ENUMERATION",
    "SPS_CHANGE_APPLICATION",
    "SYNC_FULL_ENUMERATION_ACTION",
    "SFEA_FULL_ENUMERATION",
    "SFEA_PARTIAL_SYNC",
    "SFEA_ABORT",
    "SYNC_RESOLVE_ACTION",
    "SRA_DEFER",
    "SRA_ACCEPT_DESTINATION_PROVIDER",
    "SRA_ACCEPT_SOURCE_PROVIDER",
    "SRA_MERGE",
    "SRA_TRANSFER_AND_DEFER",
    "SRA_LAST",
    "SYNC_STATISTICS",
    "SYNC_STATISTICS_RANGE_COUNT",
    "SYNC_SERIALIZATION_VERSION",
    "SYNC_SERIALIZATION_VERSION_V1",
    "SYNC_SERIALIZATION_VERSION_V2",
    "SYNC_SERIALIZATION_VERSION_V3",
    "FILTERING_TYPE",
    "FT_CURRENT_ITEMS_ONLY",
    "FT_CURRENT_ITEMS_AND_VERSIONS_FOR_MOVED_OUT_ITEMS",
    "SYNC_CONSTRAINT_RESOLVE_ACTION",
    "SCRA_DEFER",
    "SCRA_ACCEPT_DESTINATION_PROVIDER",
    "SCRA_ACCEPT_SOURCE_PROVIDER",
    "SCRA_TRANSFER_AND_DEFER",
    "SCRA_MERGE",
    "SCRA_RENAME_SOURCE",
    "SCRA_RENAME_DESTINATION",
    "CONSTRAINT_CONFLICT_REASON",
    "CCR_OTHER",
    "CCR_COLLISION",
    "CCR_NOPARENT",
    "CCR_IDENTITY",
    "KNOWLEDGE_COOKIE_COMPARISON_RESULT",
    "KCCR_COOKIE_KNOWLEDGE_EQUAL",
    "KCCR_COOKIE_KNOWLEDGE_CONTAINED",
    "KCCR_COOKIE_KNOWLEDGE_CONTAINS",
    "KCCR_COOKIE_KNOWLEDGE_NOT_COMPARABLE",
    "IClockVectorElement",
    "IFeedClockVectorElement",
    "IClockVector",
    "IFeedClockVector",
    "IEnumClockVector",
    "IEnumFeedClockVector",
    "ICoreFragment",
    "ICoreFragmentInspector",
    "IRangeException",
    "IEnumRangeExceptions",
    "ISingleItemException",
    "IEnumSingleItemExceptions",
    "IChangeUnitException",
    "IEnumChangeUnitExceptions",
    "IReplicaKeyMap",
    "IConstructReplicaKeyMap",
    "ISyncKnowledge",
    "IForgottenKnowledge",
    "ISyncKnowledge2",
    "IRecoverableErrorData",
    "IRecoverableError",
    "IChangeConflict",
    "IConstraintConflict",
    "ISyncCallback",
    "ISyncCallback2",
    "ISyncConstraintCallback",
    "ISyncProvider",
    "ISyncSessionState",
    "ISyncSessionExtendedErrorInfo",
    "ISyncSessionState2",
    "ISyncFilterInfo",
    "ISyncFilterInfo2",
    "IChangeUnitListFilterInfo",
    "ISyncFilter",
    "ISyncFilterDeserializer",
    "ICustomFilterInfo",
    "FILTER_COMBINATION_TYPE",
    "FCT_INTERSECTION",
    "ICombinedFilterInfo",
    "IEnumSyncChanges",
    "ISyncChangeBuilder",
    "IFilterTrackingSyncChangeBuilder",
    "ISyncChangeBatchBase",
    "ISyncChangeBatch",
    "ISyncFullEnumerationChangeBatch",
    "ISyncChangeBatchWithPrerequisite",
    "ISyncChangeBatchBase2",
    "ISyncChangeBatchAdvanced",
    "ISyncChangeBatch2",
    "ISyncFullEnumerationChangeBatch2",
    "IKnowledgeSyncProvider",
    "ISyncChangeUnit",
    "IEnumSyncChangeUnits",
    "ISyncChange",
    "ISyncChangeWithPrerequisite",
    "ISyncFullEnumerationChange",
    "ISyncMergeTombstoneChange",
    "IEnumItemIds",
    "IFilterKeyMap",
    "ISyncChangeWithFilterKeyMap",
    "ISyncChangeBatchWithFilterKeyMap",
    "IDataRetrieverCallback",
    "ILoadChangeContext",
    "ISynchronousDataRetriever",
    "IAsynchronousDataRetriever",
    "IFilterRequestCallback",
    "IRequestFilteredSync",
    "ISupportFilteredSync",
    "IFilterTrackingRequestCallback",
    "IFilterTrackingProvider",
    "ISupportLastWriteTime",
    "IProviderConverter",
    "ISyncDataConverter",
    "SyncProviderRegistration",
    "SyncProviderConfiguration",
    "SyncProviderConfigUIConfiguration",
    "ISyncProviderRegistration",
    "IEnumSyncProviderConfigUIInfos",
    "IEnumSyncProviderInfos",
    "ISyncProviderInfo",
    "ISyncProviderConfigUIInfo",
    "ISyncProviderConfigUI",
    "IRegisteredSyncProvider",
    "SYNC_REGISTRATION_EVENT",
    "SRE_PROVIDER_ADDED",
    "SRE_PROVIDER_REMOVED",
    "SRE_PROVIDER_UPDATED",
    "SRE_PROVIDER_STATE_CHANGED",
    "SRE_CONFIGUI_ADDED",
    "SRE_CONFIGUI_REMOVED",
    "SRE_CONFIGUI_UPDATED",
    "ISyncRegistrationChange",
]
