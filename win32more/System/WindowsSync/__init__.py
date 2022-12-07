from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.WindowsSync
import win32more.UI.Shell.PropertiesSystem
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
SYNC_VERSION_FLAG_FROM_FEED: UInt32 = 1
SYNC_VERSION_FLAG_HAS_BY: UInt32 = 2
SYNC_SERIALIZE_REPLICA_KEY_MAP: UInt32 = 1
SYNC_FILTER_INFO_FLAG_ITEM_LIST: UInt32 = 1
SYNC_FILTER_INFO_FLAG_CHANGE_UNIT_LIST: UInt32 = 2
SYNC_FILTER_INFO_FLAG_CUSTOM: UInt32 = 4
SYNC_FILTER_INFO_COMBINED: UInt32 = 8
SYNC_CHANGE_FLAG_DELETED: UInt32 = 1
SYNC_CHANGE_FLAG_DOES_NOT_EXIST: UInt32 = 2
SYNC_CHANGE_FLAG_GHOST: UInt32 = 4
def PKEY_PROVIDER_INSTANCEID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('84179e61-60f6-4c1c-88-ed-f1-c5-31-b3-2b-da'), pid=2)
def PKEY_PROVIDER_CLSID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('84179e61-60f6-4c1c-88-ed-f1-c5-31-b3-2b-da'), pid=3)
def PKEY_PROVIDER_CONFIGUI():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('84179e61-60f6-4c1c-88-ed-f1-c5-31-b3-2b-da'), pid=4)
def PKEY_PROVIDER_CONTENTTYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('84179e61-60f6-4c1c-88-ed-f1-c5-31-b3-2b-da'), pid=5)
def PKEY_PROVIDER_CAPABILITIES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('84179e61-60f6-4c1c-88-ed-f1-c5-31-b3-2b-da'), pid=6)
def PKEY_PROVIDER_SUPPORTED_ARCHITECTURE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('84179e61-60f6-4c1c-88-ed-f1-c5-31-b3-2b-da'), pid=7)
def PKEY_PROVIDER_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('84179e61-60f6-4c1c-88-ed-f1-c5-31-b3-2b-da'), pid=8)
def PKEY_PROVIDER_DESCRIPTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('84179e61-60f6-4c1c-88-ed-f1-c5-31-b3-2b-da'), pid=9)
def PKEY_PROVIDER_TOOLTIPS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('84179e61-60f6-4c1c-88-ed-f1-c5-31-b3-2b-da'), pid=10)
def PKEY_PROVIDER_ICON():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('84179e61-60f6-4c1c-88-ed-f1-c5-31-b3-2b-da'), pid=11)
def PKEY_CONFIGUI_INSTANCEID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=2)
def PKEY_CONFIGUI_CLSID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=3)
def PKEY_CONFIGUI_CONTENTTYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=4)
def PKEY_CONFIGUI_CAPABILITIES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=5)
def PKEY_CONFIGUI_SUPPORTED_ARCHITECTURE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=6)
def PKEY_CONFIGUI_IS_GLOBAL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=7)
def PKEY_CONFIGUI_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=8)
def PKEY_CONFIGUI_DESCRIPTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=9)
def PKEY_CONFIGUI_TOOLTIPS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=10)
def PKEY_CONFIGUI_ICON():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=11)
def PKEY_CONFIGUI_MENUITEM_NOUI():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=12)
def PKEY_CONFIGUI_MENUITEM():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('554b24ea-e8e3-45ba-93-52-df-b5-61-e1-71-e4'), pid=13)
CONFLICT_RESOLUTION_POLICY = Int32
CRP_NONE: CONFLICT_RESOLUTION_POLICY = 0
CRP_DESTINATION_PROVIDER_WINS: CONFLICT_RESOLUTION_POLICY = 1
CRP_SOURCE_PROVIDER_WINS: CONFLICT_RESOLUTION_POLICY = 2
CRP_LAST: CONFLICT_RESOLUTION_POLICY = 3
CONSTRAINT_CONFLICT_REASON = Int32
CCR_OTHER: CONSTRAINT_CONFLICT_REASON = 0
CCR_COLLISION: CONSTRAINT_CONFLICT_REASON = 1
CCR_NOPARENT: CONSTRAINT_CONFLICT_REASON = 2
CCR_IDENTITY: CONSTRAINT_CONFLICT_REASON = 3
FILTER_COMBINATION_TYPE = Int32
FCT_INTERSECTION: FILTER_COMBINATION_TYPE = 0
FILTERING_TYPE = Int32
FT_CURRENT_ITEMS_ONLY: FILTERING_TYPE = 0
FT_CURRENT_ITEMS_AND_VERSIONS_FOR_MOVED_OUT_ITEMS: FILTERING_TYPE = 1
class IAsynchronousDataRetriever(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9fc7e470-61ea-4a88-9b-e4-df-56-a2-7c-fe-f2')
    @commethod(3)
    def GetIdParameters(pIdParameters: POINTER(win32more.System.WindowsSync.ID_PARAMETERS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterCallback(pDataRetrieverCallback: win32more.System.WindowsSync.IDataRetrieverCallback_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RevokeCallback(pDataRetrieverCallback: win32more.System.WindowsSync.IDataRetrieverCallback_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def LoadChangeData(pLoadChangeContext: win32more.System.WindowsSync.ILoadChangeContext_head) -> win32more.Foundation.HRESULT: ...
class IChangeConflict(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('014ebf97-9f20-4f7a-bd-d4-25-97-9c-77-c0-02')
    @commethod(3)
    def GetDestinationProviderConflictingChange(ppConflictingChange: POINTER(win32more.System.WindowsSync.ISyncChange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceProviderConflictingChange(ppConflictingChange: POINTER(win32more.System.WindowsSync.ISyncChange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDestinationProviderConflictingData(ppConflictingData: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSourceProviderConflictingData(ppConflictingData: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetResolveActionForChange(pResolveAction: POINTER(win32more.System.WindowsSync.SYNC_RESOLVE_ACTION)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetResolveActionForChange(resolveAction: win32more.System.WindowsSync.SYNC_RESOLVE_ACTION) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetResolveActionForChangeUnit(pChangeUnit: win32more.System.WindowsSync.ISyncChangeUnit_head, pResolveAction: POINTER(win32more.System.WindowsSync.SYNC_RESOLVE_ACTION)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetResolveActionForChangeUnit(pChangeUnit: win32more.System.WindowsSync.ISyncChangeUnit_head, resolveAction: win32more.System.WindowsSync.SYNC_RESOLVE_ACTION) -> win32more.Foundation.HRESULT: ...
class IChangeUnitException(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0cd7ee7c-fec0-4021-99-ee-f0-e5-34-8f-2a-5f')
    @commethod(3)
    def GetItemId(pbItemId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetChangeUnitId(pbChangeUnitId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetClockVector(riid: POINTER(Guid), ppUnk: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IChangeUnitListFilterInfo(c_void_p):
    extends: win32more.System.WindowsSync.ISyncFilterInfo
    Guid = Guid('f2837671-0bdf-43fa-b5-02-23-23-75-fb-50-c2')
    @commethod(4)
    def Initialize(ppbChangeUnitIds: POINTER(c_char_p_no), dwChangeUnitCount: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeUnitIdCount(pdwChangeUnitIdCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetChangeUnitId(dwChangeUnitIdIndex: UInt32, pbChangeUnitId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IClockVector(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('14b2274a-8698-4cc6-93-33-f8-9b-d1-d4-7b-c4')
    @commethod(3)
    def GetClockVectorElements(riid: POINTER(Guid), ppiEnumClockVector: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetClockVectorElementCount(pdwCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IClockVectorElement(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e71c4250-adf8-4a07-8f-ae-56-69-59-69-09-c1')
    @commethod(3)
    def GetReplicaKey(pdwReplicaKey: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTickCount(pullTickCount: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
class ICombinedFilterInfo(c_void_p):
    extends: win32more.System.WindowsSync.ISyncFilterInfo
    Guid = Guid('11f9de71-2818-4779-b2-ac-42-d4-50-56-5f-45')
    @commethod(4)
    def GetFilterCount(pdwFilterCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFilterInfo(dwFilterIndex: UInt32, ppIFilterInfo: POINTER(win32more.System.WindowsSync.ISyncFilterInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetFilterCombinationType(pFilterCombinationType: POINTER(win32more.System.WindowsSync.FILTER_COMBINATION_TYPE)) -> win32more.Foundation.HRESULT: ...
class IConstraintConflict(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00d2302e-1cf8-4835-b8-5f-b7-ca-4f-79-9e-0a')
    @commethod(3)
    def GetDestinationProviderConflictingChange(ppConflictingChange: POINTER(win32more.System.WindowsSync.ISyncChange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceProviderConflictingChange(ppConflictingChange: POINTER(win32more.System.WindowsSync.ISyncChange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDestinationProviderOriginalChange(ppOriginalChange: POINTER(win32more.System.WindowsSync.ISyncChange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDestinationProviderConflictingData(ppConflictingData: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSourceProviderConflictingData(ppConflictingData: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetDestinationProviderOriginalData(ppOriginalData: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetConstraintResolveActionForChange(pConstraintResolveAction: POINTER(win32more.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetConstraintResolveActionForChange(constraintResolveAction: win32more.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetConstraintResolveActionForChangeUnit(pChangeUnit: win32more.System.WindowsSync.ISyncChangeUnit_head, pConstraintResolveAction: POINTER(win32more.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetConstraintResolveActionForChangeUnit(pChangeUnit: win32more.System.WindowsSync.ISyncChangeUnit_head, constraintResolveAction: win32more.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetConstraintConflictReason(pConstraintConflictReason: POINTER(win32more.System.WindowsSync.CONSTRAINT_CONFLICT_REASON)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def IsTemporary() -> win32more.Foundation.HRESULT: ...
class IConstructReplicaKeyMap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ded10970-ec85-4115-b5-2c-44-05-84-56-42-a5')
    @commethod(3)
    def FindOrAddReplica(pbReplicaId: c_char_p_no, pdwReplicaKey: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ICoreFragment(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('613b2ab5-b304-47d9-9c-31-ce-6c-54-40-1a-15')
    @commethod(3)
    def NextColumn(pChangeUnitId: c_char_p_no, pChangeUnitIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def NextRange(pItemId: c_char_p_no, pItemIdSize: POINTER(UInt32), piClockVector: POINTER(win32more.System.WindowsSync.IClockVector_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumnCount(pColumnCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRangeCount(pRangeCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ICoreFragmentInspector(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f7fcc5fd-ae26-4679-ba-16-96-aa-c5-83-c1-34')
    @commethod(3)
    def NextCoreFragments(requestedCount: UInt32, ppiCoreFragments: POINTER(win32more.System.WindowsSync.ICoreFragment_head), pFetchedCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Reset() -> win32more.Foundation.HRESULT: ...
class ICustomFilterInfo(c_void_p):
    extends: win32more.System.WindowsSync.ISyncFilterInfo
    Guid = Guid('1d335dff-6f88-4e4d-91-a8-a3-f3-51-cf-d4-73')
    @commethod(4)
    def GetSyncFilter(pISyncFilter: POINTER(win32more.System.WindowsSync.ISyncFilter_head)) -> win32more.Foundation.HRESULT: ...
class ID_PARAMETER_PAIR(Structure):
    fIsVariable: win32more.Foundation.BOOL
    cbIdSize: UInt16
class ID_PARAMETERS(Structure):
    dwSize: UInt32
    replicaId: win32more.System.WindowsSync.ID_PARAMETER_PAIR
    itemId: win32more.System.WindowsSync.ID_PARAMETER_PAIR
    changeUnitId: win32more.System.WindowsSync.ID_PARAMETER_PAIR
class IDataRetrieverCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('71b4863b-f969-4676-bb-c3-3d-9f-dc-3f-b2-c7')
    @commethod(3)
    def LoadChangeDataComplete(pUnkData: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LoadChangeDataError(hrError: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
class IEnumChangeUnitExceptions(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3074e802-9319-4420-be-21-10-22-e2-e2-1d-a8')
    @commethod(3)
    def Next(cExceptions: UInt32, ppChangeUnitException: POINTER(win32more.System.WindowsSync.IChangeUnitException_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cExceptions: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.WindowsSync.IEnumChangeUnitExceptions_head)) -> win32more.Foundation.HRESULT: ...
class IEnumClockVector(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('525844db-2837-4799-9e-80-81-a6-6e-02-22-0c')
    @commethod(3)
    def Next(cClockVectorElements: UInt32, ppiClockVectorElements: POINTER(win32more.System.WindowsSync.IClockVectorElement_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cSyncVersions: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppiEnum: POINTER(win32more.System.WindowsSync.IEnumClockVector_head)) -> win32more.Foundation.HRESULT: ...
class IEnumFeedClockVector(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('550f763d-146a-48f6-ab-eb-6c-88-c7-f7-05-14')
    @commethod(3)
    def Next(cClockVectorElements: UInt32, ppiClockVectorElements: POINTER(win32more.System.WindowsSync.IFeedClockVectorElement_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cSyncVersions: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppiEnum: POINTER(win32more.System.WindowsSync.IEnumFeedClockVector_head)) -> win32more.Foundation.HRESULT: ...
class IEnumItemIds(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('43aa3f61-4b2e-4b60-83-df-b1-10-d3-e1-48-f1')
    @commethod(3)
    def Next(pbItemId: c_char_p_no, pcbItemIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IEnumRangeExceptions(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0944439f-ddb1-4176-b7-03-04-6f-f2-2a-23-86')
    @commethod(3)
    def Next(cExceptions: UInt32, ppRangeException: POINTER(win32more.System.WindowsSync.IRangeException_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cExceptions: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.WindowsSync.IEnumRangeExceptions_head)) -> win32more.Foundation.HRESULT: ...
class IEnumSingleItemExceptions(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e563381c-1b4d-4c66-97-96-c8-6f-ac-cd-cd-40')
    @commethod(3)
    def Next(cExceptions: UInt32, ppSingleItemException: POINTER(win32more.System.WindowsSync.ISingleItemException_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cExceptions: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.WindowsSync.IEnumSingleItemExceptions_head)) -> win32more.Foundation.HRESULT: ...
class IEnumSyncChanges(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5f86be4a-5e78-4e32-ac-1c-c2-4f-d2-23-ef-85')
    @commethod(3)
    def Next(cChanges: UInt32, ppChange: POINTER(win32more.System.WindowsSync.ISyncChange_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cChanges: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.WindowsSync.IEnumSyncChanges_head)) -> win32more.Foundation.HRESULT: ...
class IEnumSyncChangeUnits(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('346b35f1-8703-4c6d-ab-1a-4d-bc-a2-cf-f9-7f')
    @commethod(3)
    def Next(cChanges: UInt32, ppChangeUnit: POINTER(win32more.System.WindowsSync.ISyncChangeUnit_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cChanges: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.WindowsSync.IEnumSyncChangeUnits_head)) -> win32more.Foundation.HRESULT: ...
class IEnumSyncProviderConfigUIInfos(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f6be2602-17c6-4658-a2-d7-68-ed-33-30-f6-41')
    @commethod(3)
    def Next(cFactories: UInt32, ppSyncProviderConfigUIInfo: POINTER(win32more.System.WindowsSync.ISyncProviderConfigUIInfo_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cFactories: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.WindowsSync.IEnumSyncProviderConfigUIInfos_head)) -> win32more.Foundation.HRESULT: ...
class IEnumSyncProviderInfos(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a04ba850-5eb1-460d-a9-73-39-3f-cb-60-8a-11')
    @commethod(3)
    def Next(cInstances: UInt32, ppSyncProviderInfo: POINTER(win32more.System.WindowsSync.ISyncProviderInfo_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cInstances: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.WindowsSync.IEnumSyncProviderInfos_head)) -> win32more.Foundation.HRESULT: ...
class IFeedClockVector(c_void_p):
    extends: win32more.System.WindowsSync.IClockVector
    Guid = Guid('8d1d98d1-9fb8-4ec9-a5-53-54-dd-92-4e-0f-67')
    @commethod(5)
    def GetUpdateCount(pdwUpdateCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def IsNoConflictsSpecified(pfIsNoConflictsSpecified: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IFeedClockVectorElement(c_void_p):
    extends: win32more.System.WindowsSync.IClockVectorElement
    Guid = Guid('a40b46d2-e97b-4156-b6-da-99-1f-50-1b-0f-05')
    @commethod(5)
    def GetSyncTime(pSyncTime: POINTER(win32more.System.WindowsSync.SYNC_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetFlags(pbFlags: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IFilterKeyMap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ca169652-07c6-4708-a3-da-6e-4e-ba-8d-22-97')
    @commethod(3)
    def GetCount(pdwCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddFilter(pISyncFilter: win32more.System.WindowsSync.ISyncFilter_head, pdwFilterKey: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFilter(dwFilterKey: UInt32, ppISyncFilter: POINTER(win32more.System.WindowsSync.ISyncFilter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Serialize(pbFilterKeyMap: c_char_p_no, pcbFilterKeyMap: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IFilterRequestCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('82df8873-6360-463a-a8-a1-ed-e5-e1-a1-59-4d')
    @commethod(3)
    def RequestFilter(pFilter: win32more.System.Com.IUnknown_head, filteringType: win32more.System.WindowsSync.FILTERING_TYPE) -> win32more.Foundation.HRESULT: ...
class IFilterTrackingProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('743383c0-fc4e-45ba-ad-81-d9-d8-4c-7a-24-f8')
    @commethod(3)
    def SpecifyTrackedFilters(pCallback: win32more.System.WindowsSync.IFilterTrackingRequestCallback_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddTrackedFilter(pFilter: win32more.System.WindowsSync.ISyncFilter_head) -> win32more.Foundation.HRESULT: ...
class IFilterTrackingRequestCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('713ca7bb-c858-4674-b4-b6-11-22-43-65-87-a9')
    @commethod(3)
    def RequestTrackedFilter(pFilter: win32more.System.WindowsSync.ISyncFilter_head) -> win32more.Foundation.HRESULT: ...
class IFilterTrackingSyncChangeBuilder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('295024a0-70da-4c58-88-3c-ce-2a-fb-30-8d-0b')
    @commethod(3)
    def AddFilterChange(dwFilterKey: UInt32, pFilterChange: POINTER(win32more.System.WindowsSync.SYNC_FILTER_CHANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetAllChangeUnitsPresentFlag() -> win32more.Foundation.HRESULT: ...
class IForgottenKnowledge(c_void_p):
    extends: win32more.System.WindowsSync.ISyncKnowledge
    Guid = Guid('456e0f96-6036-452b-9f-9d-bc-c4-b4-a8-5d-b2')
    @commethod(27)
    def ForgetToVersion(pKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head)) -> win32more.Foundation.HRESULT: ...
class IKnowledgeSyncProvider(c_void_p):
    extends: win32more.System.WindowsSync.ISyncProvider
    Guid = Guid('43434a49-8da4-47f2-81-72-ad-7b-8b-02-49-78')
    @commethod(4)
    def BeginSession(role: win32more.System.WindowsSync.SYNC_PROVIDER_ROLE, pSessionState: win32more.System.WindowsSync.ISyncSessionState_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSyncBatchParameters(ppSyncKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head), pdwRequestedBatchSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetChangeBatch(dwBatchSize: UInt32, pSyncKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, ppSyncChangeBatch: POINTER(win32more.System.WindowsSync.ISyncChangeBatch_head), ppUnkDataRetriever: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetFullEnumerationChangeBatch(dwBatchSize: UInt32, pbLowerEnumerationBound: c_char_p_no, pSyncKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, ppSyncChangeBatch: POINTER(win32more.System.WindowsSync.ISyncFullEnumerationChangeBatch_head), ppUnkDataRetriever: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ProcessChangeBatch(resolutionPolicy: win32more.System.WindowsSync.CONFLICT_RESOLUTION_POLICY, pSourceChangeBatch: win32more.System.WindowsSync.ISyncChangeBatch_head, pUnkDataRetriever: win32more.System.Com.IUnknown_head, pCallback: win32more.System.WindowsSync.ISyncCallback_head, pSyncSessionStatistics: POINTER(win32more.System.WindowsSync.SYNC_SESSION_STATISTICS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def ProcessFullEnumerationChangeBatch(resolutionPolicy: win32more.System.WindowsSync.CONFLICT_RESOLUTION_POLICY, pSourceChangeBatch: win32more.System.WindowsSync.ISyncFullEnumerationChangeBatch_head, pUnkDataRetriever: win32more.System.Com.IUnknown_head, pCallback: win32more.System.WindowsSync.ISyncCallback_head, pSyncSessionStatistics: POINTER(win32more.System.WindowsSync.SYNC_SESSION_STATISTICS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def EndSession(pSessionState: win32more.System.WindowsSync.ISyncSessionState_head) -> win32more.Foundation.HRESULT: ...
class ILoadChangeContext(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('44a4aaca-ec39-46d5-b5-c9-d6-33-c0-ee-67-e2')
    @commethod(3)
    def GetSyncChange(ppSyncChange: POINTER(win32more.System.WindowsSync.ISyncChange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetRecoverableErrorOnChange(hrError: win32more.Foundation.HRESULT, pErrorData: win32more.System.WindowsSync.IRecoverableErrorData_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetRecoverableErrorOnChangeUnit(hrError: win32more.Foundation.HRESULT, pChangeUnit: win32more.System.WindowsSync.ISyncChangeUnit_head, pErrorData: win32more.System.WindowsSync.IRecoverableErrorData_head) -> win32more.Foundation.HRESULT: ...
class IProviderConverter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('809b7276-98cf-4957-93-a5-0e-bd-d3-dd-df-fd')
    @commethod(3)
    def Initialize(pISyncProvider: win32more.System.WindowsSync.ISyncProvider_head) -> win32more.Foundation.HRESULT: ...
class IRangeException(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('75ae8777-6848-49f7-95-6c-a3-a9-2f-50-96-e8')
    @commethod(3)
    def GetClosedRangeStart(pbClosedRangeStart: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetClosedRangeEnd(pbClosedRangeEnd: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetClockVector(riid: POINTER(Guid), ppUnk: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IRecoverableError(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0f5625e8-0a7b-45ee-96-37-1c-e1-36-45-90-9e')
    @commethod(3)
    def GetStage(pStage: POINTER(win32more.System.WindowsSync.SYNC_PROGRESS_STAGE)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetProvider(pProviderRole: POINTER(win32more.System.WindowsSync.SYNC_PROVIDER_ROLE)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeWithRecoverableError(ppChangeWithRecoverableError: POINTER(win32more.System.WindowsSync.ISyncChange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecoverableErrorDataForChange(phrError: POINTER(win32more.Foundation.HRESULT), ppErrorData: POINTER(win32more.System.WindowsSync.IRecoverableErrorData_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecoverableErrorDataForChangeUnit(pChangeUnit: win32more.System.WindowsSync.ISyncChangeUnit_head, phrError: POINTER(win32more.Foundation.HRESULT), ppErrorData: POINTER(win32more.System.WindowsSync.IRecoverableErrorData_head)) -> win32more.Foundation.HRESULT: ...
class IRecoverableErrorData(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b37c4a0a-4b7d-4c2d-97-11-3b-00-d1-19-b1-c8')
    @commethod(3)
    def Initialize(pcszItemDisplayName: win32more.Foundation.PWSTR, pcszErrorDescription: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetItemDisplayName(pszItemDisplayName: win32more.Foundation.PWSTR, pcchItemDisplayName: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorDescription(pszErrorDescription: win32more.Foundation.PWSTR, pcchErrorDescription: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IRegisteredSyncProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('913bcf76-47c1-40b5-a8-96-5e-8a-9c-41-4c-14')
    @commethod(3)
    def Init(pguidInstanceId: POINTER(Guid), pguidContentType: POINTER(Guid), pContextPropertyStore: win32more.UI.Shell.PropertiesSystem.IPropertyStore_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetInstanceId(pguidInstanceId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
class IReplicaKeyMap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2209f4fc-fd10-4ff0-84-a8-f0-a1-98-2e-44-0e')
    @commethod(3)
    def LookupReplicaKey(pbReplicaId: c_char_p_no, pdwReplicaKey: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LookupReplicaId(dwReplicaKey: UInt32, pbReplicaId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Serialize(pbReplicaKeyMap: c_char_p_no, pcbReplicaKeyMap: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IRequestFilteredSync(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2e020184-6d18-46a7-a3-2a-da-4a-eb-06-69-6c')
    @commethod(3)
    def SpecifyFilter(pCallback: win32more.System.WindowsSync.IFilterRequestCallback_head) -> win32more.Foundation.HRESULT: ...
class ISingleItemException(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('892fb9b0-7c55-4a18-93-16-fd-f4-49-56-9b-64')
    @commethod(3)
    def GetItemId(pbItemId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetClockVector(riid: POINTER(Guid), ppUnk: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class ISupportFilteredSync(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3d128ded-d555-4e0d-bf-4b-fb-21-3a-8a-93-02')
    @commethod(3)
    def AddFilter(pFilter: win32more.System.Com.IUnknown_head, filteringType: win32more.System.WindowsSync.FILTERING_TYPE) -> win32more.Foundation.HRESULT: ...
class ISupportLastWriteTime(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('eadf816f-d0bd-43ca-8f-40-5a-cd-c6-c0-6f-7a')
    @commethod(3)
    def GetItemChangeTime(pbItemId: c_char_p_no, pullTimestamp: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetChangeUnitChangeTime(pbItemId: c_char_p_no, pbChangeUnitId: c_char_p_no, pullTimestamp: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
class ISyncCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0599797f-5ed9-485c-ae-36-0c-5d-1b-f2-e7-a5')
    @commethod(3)
    def OnProgress(provider: win32more.System.WindowsSync.SYNC_PROVIDER_ROLE, syncStage: win32more.System.WindowsSync.SYNC_PROGRESS_STAGE, dwCompletedWork: UInt32, dwTotalWork: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnChange(pSyncChange: win32more.System.WindowsSync.ISyncChange_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnConflict(pConflict: win32more.System.WindowsSync.IChangeConflict_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnFullEnumerationNeeded(pFullEnumerationAction: POINTER(win32more.System.WindowsSync.SYNC_FULL_ENUMERATION_ACTION)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnRecoverableError(pRecoverableError: win32more.System.WindowsSync.IRecoverableError_head) -> win32more.Foundation.HRESULT: ...
class ISyncCallback2(c_void_p):
    extends: win32more.System.WindowsSync.ISyncCallback
    Guid = Guid('47ce84af-7442-4ead-86-30-12-01-5e-03-0a-d7')
    @commethod(8)
    def OnChangeApplied(dwChangesApplied: UInt32, dwChangesFailed: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnChangeFailed(dwChangesApplied: UInt32, dwChangesFailed: UInt32) -> win32more.Foundation.HRESULT: ...
class ISyncChange(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a1952beb-0f6b-4711-b1-36-01-da-85-b9-68-a6')
    @commethod(3)
    def GetOwnerReplicaId(pbReplicaId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetRootItemId(pbRootItemId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeVersion(pbCurrentReplicaId: c_char_p_no, pVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCreationVersion(pbCurrentReplicaId: c_char_p_no, pVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetFlags(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetWorkEstimate(pdwWork: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetChangeUnits(ppEnum: POINTER(win32more.System.WindowsSync.IEnumSyncChangeUnits_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetMadeWithKnowledge(ppMadeWithKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetLearnedKnowledge(ppLearnedKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetWorkEstimate(dwWork: UInt32) -> win32more.Foundation.HRESULT: ...
class ISyncChangeBatch(c_void_p):
    extends: win32more.System.WindowsSync.ISyncChangeBatchBase
    Guid = Guid('70c64dee-380f-4c2e-8f-70-31-c5-5b-d5-f9-b3')
    @commethod(17)
    def BeginUnorderedGroup() -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def EndUnorderedGroup(pMadeWithKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, fAllChangesForKnowledge: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def AddLoggedConflict(pbOwnerReplicaId: c_char_p_no, pbItemId: c_char_p_no, pChangeVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), pCreationVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), dwFlags: UInt32, dwWorkForChange: UInt32, pConflictKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, ppChangeBuilder: POINTER(win32more.System.WindowsSync.ISyncChangeBuilder_head)) -> win32more.Foundation.HRESULT: ...
class ISyncChangeBatch2(c_void_p):
    extends: win32more.System.WindowsSync.ISyncChangeBatch
    Guid = Guid('225f4a33-f5ee-4cc7-b0-39-67-a2-62-b4-b2-ac')
    @commethod(20)
    def AddMergeTombstoneMetadataToGroup(pbOwnerReplicaId: c_char_p_no, pbWinnerItemId: c_char_p_no, pbItemId: c_char_p_no, pChangeVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), pCreationVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), dwWorkForChange: UInt32, ppChangeBuilder: POINTER(win32more.System.WindowsSync.ISyncChangeBuilder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def AddMergeTombstoneLoggedConflict(pbOwnerReplicaId: c_char_p_no, pbWinnerItemId: c_char_p_no, pbItemId: c_char_p_no, pChangeVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), pCreationVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), dwWorkForChange: UInt32, pConflictKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, ppChangeBuilder: POINTER(win32more.System.WindowsSync.ISyncChangeBuilder_head)) -> win32more.Foundation.HRESULT: ...
class ISyncChangeBatchAdvanced(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0f1a4995-cbc8-421d-b5-50-5d-0b-eb-f3-e9-a5')
    @commethod(3)
    def GetFilterInfo(ppFilterInfo: POINTER(win32more.System.WindowsSync.ISyncFilterInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ConvertFullEnumerationChangeBatchToRegularChangeBatch(ppChangeBatch: POINTER(win32more.System.WindowsSync.ISyncChangeBatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetUpperBoundItemId(pbItemId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetBatchLevelKnowledgeShouldBeApplied(pfBatchKnowledgeShouldBeApplied: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ISyncChangeBatchBase(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('52f6e694-6a71-4494-a1-84-a8-31-1b-f5-d2-27')
    @commethod(3)
    def GetChangeEnumerator(ppEnum: POINTER(win32more.System.WindowsSync.IEnumSyncChanges_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetIsLastBatch(pfLastBatch: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetWorkEstimateForBatch(pdwWorkForBatch: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRemainingWorkEstimateForSession(pdwRemainingWorkForSession: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def BeginOrderedGroup(pbLowerBound: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def EndOrderedGroup(pbUpperBound: c_char_p_no, pMadeWithKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AddItemMetadataToGroup(pbOwnerReplicaId: c_char_p_no, pbItemId: c_char_p_no, pChangeVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), pCreationVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), dwFlags: UInt32, dwWorkForChange: UInt32, ppChangeBuilder: POINTER(win32more.System.WindowsSync.ISyncChangeBuilder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetLearnedKnowledge(ppLearnedKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetPrerequisiteKnowledge(ppPrerequisteKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetSourceForgottenKnowledge(ppSourceForgottenKnowledge: POINTER(win32more.System.WindowsSync.IForgottenKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetLastBatch() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetWorkEstimateForBatch(dwWorkForBatch: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetRemainingWorkEstimateForSession(dwRemainingWorkForSession: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Serialize(pbChangeBatch: c_char_p_no, pcbChangeBatch: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ISyncChangeBatchBase2(c_void_p):
    extends: win32more.System.WindowsSync.ISyncChangeBatchBase
    Guid = Guid('6fdb596a-d755-4584-bd-0c-c0-c2-3a-54-8f-bf')
    @commethod(17)
    def SerializeWithOptions(targetFormatVersion: win32more.System.WindowsSync.SYNC_SERIALIZATION_VERSION, dwFlags: UInt32, pbBuffer: c_char_p_no, pdwSerializedSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ISyncChangeBatchWithFilterKeyMap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('de247002-566d-459a-a6-ed-a5-aa-b3-45-9f-b7')
    @commethod(3)
    def GetFilterKeyMap(ppIFilterKeyMap: POINTER(win32more.System.WindowsSync.IFilterKeyMap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetFilterKeyMap(pIFilterKeyMap: win32more.System.WindowsSync.IFilterKeyMap_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetFilterForgottenKnowledge(dwFilterKey: UInt32, pFilterForgottenKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetFilteredReplicaLearnedKnowledge(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: win32more.System.WindowsSync.IEnumItemIds_head, ppLearnedForgottenKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetLearnedFilterForgottenKnowledge(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: win32more.System.WindowsSync.IEnumItemIds_head, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetFilteredReplicaLearnedForgottenKnowledge(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: win32more.System.WindowsSync.IEnumItemIds_head, ppLearnedForgottenKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetFilteredReplicaLearnedForgottenKnowledgeAfterRecoveryComplete(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: win32more.System.WindowsSync.IEnumItemIds_head, ppLearnedForgottenKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetLearnedFilterForgottenKnowledgeAfterRecoveryComplete(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: win32more.System.WindowsSync.IEnumItemIds_head, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
class ISyncChangeBatchWithPrerequisite(c_void_p):
    extends: win32more.System.WindowsSync.ISyncChangeBatchBase
    Guid = Guid('097f13be-5b92-4048-b3-f2-7b-42-a2-51-5e-07')
    @commethod(17)
    def SetPrerequisiteKnowledge(pPrerequisiteKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetLearnedKnowledgeWithPrerequisite(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, ppLearnedWithPrerequisiteKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetLearnedForgottenKnowledge(ppLearnedForgottenKnowledge: POINTER(win32more.System.WindowsSync.IForgottenKnowledge_head)) -> win32more.Foundation.HRESULT: ...
class ISyncChangeBuilder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56f14771-8677-484f-a1-70-e3-86-e4-18-a6-76')
    @commethod(3)
    def AddChangeUnitMetadata(pbChangeUnitId: c_char_p_no, pChangeUnitVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head)) -> win32more.Foundation.HRESULT: ...
class ISyncChangeUnit(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('60edd8ca-7341-4bb7-95-ce-fa-b6-39-4b-51-cb')
    @commethod(3)
    def GetItemChange(ppSyncChange: POINTER(win32more.System.WindowsSync.ISyncChange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetChangeUnitId(pbChangeUnitId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeUnitVersion(pbCurrentReplicaId: c_char_p_no, pVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head)) -> win32more.Foundation.HRESULT: ...
class ISyncChangeWithFilterKeyMap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bfe1ef00-e87d-42fd-a4-e9-24-2d-70-41-4a-ef')
    @commethod(3)
    def GetFilterCount(pdwFilterCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetFilterChange(dwFilterKey: UInt32, pFilterChange: POINTER(win32more.System.WindowsSync.SYNC_FILTER_CHANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAllChangeUnitsPresentFlag(pfAllChangeUnitsPresent: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetFilterForgottenKnowledge(dwFilterKey: UInt32, ppIFilterForgottenKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetFilteredReplicaLearnedKnowledge(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: win32more.System.WindowsSync.IEnumItemIds_head, ppLearnedKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetLearnedFilterForgottenKnowledge(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: win32more.System.WindowsSync.IEnumItemIds_head, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetFilteredReplicaLearnedForgottenKnowledge(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: win32more.System.WindowsSync.IEnumItemIds_head, ppLearnedForgottenKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetFilteredReplicaLearnedForgottenKnowledgeAfterRecoveryComplete(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: win32more.System.WindowsSync.IEnumItemIds_head, ppLearnedForgottenKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetLearnedFilterForgottenKnowledgeAfterRecoveryComplete(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: win32more.System.WindowsSync.IEnumItemIds_head, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
class ISyncChangeWithPrerequisite(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9e38382f-1589-48c3-92-e4-05-ec-dc-b4-f3-f7')
    @commethod(3)
    def GetPrerequisiteKnowledge(ppPrerequisiteKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLearnedKnowledgeWithPrerequisite(pDestinationKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, ppLearnedKnowledgeWithPrerequisite: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
class ISyncConstraintCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8af3843e-75b3-438c-bb-51-6f-02-0d-70-d3-cb')
    @commethod(3)
    def OnConstraintConflict(pConflict: win32more.System.WindowsSync.IConstraintConflict_head) -> win32more.Foundation.HRESULT: ...
class ISyncDataConverter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('435d4861-68d5-44aa-a0-f9-72-a0-b0-0e-f9-cf')
    @commethod(3)
    def ConvertDataRetrieverFromProviderFormat(pUnkDataRetrieverIn: win32more.System.Com.IUnknown_head, pEnumSyncChanges: win32more.System.WindowsSync.IEnumSyncChanges_head, ppUnkDataOut: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ConvertDataRetrieverToProviderFormat(pUnkDataRetrieverIn: win32more.System.Com.IUnknown_head, pEnumSyncChanges: win32more.System.WindowsSync.IEnumSyncChanges_head, ppUnkDataOut: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ConvertDataFromProviderFormat(pDataContext: win32more.System.WindowsSync.ILoadChangeContext_head, pUnkDataIn: win32more.System.Com.IUnknown_head, ppUnkDataOut: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ConvertDataToProviderFormat(pDataContext: win32more.System.WindowsSync.ILoadChangeContext_head, pUnkDataOut: win32more.System.Com.IUnknown_head, ppUnkDataout: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ISyncFilter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('087a3f15-0fcb-44c1-96-39-53-c1-4e-2b-55-06')
    @commethod(3)
    def IsIdentical(pSyncFilter: win32more.System.WindowsSync.ISyncFilter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Serialize(pbSyncFilter: c_char_p_no, pcbSyncFilter: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ISyncFilterDeserializer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b45b7a72-e5c7-46be-9c-82-77-b8-b1-5d-ab-8a')
    @commethod(3)
    def DeserializeSyncFilter(pbSyncFilter: c_char_p_no, dwCbSyncFilter: UInt32, ppISyncFilter: POINTER(win32more.System.WindowsSync.ISyncFilter_head)) -> win32more.Foundation.HRESULT: ...
class ISyncFilterInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('794eaaf8-3f2e-47e6-97-28-17-e6-fc-f9-4c-b7')
    @commethod(3)
    def Serialize(pbBuffer: c_char_p_no, pcbBuffer: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ISyncFilterInfo2(c_void_p):
    extends: win32more.System.WindowsSync.ISyncFilterInfo
    Guid = Guid('19b394ba-e3d0-468c-93-4d-32-19-68-b2-ab-34')
    @commethod(4)
    def GetFlags(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ISyncFullEnumerationChange(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9785e0bd-bdff-40c4-98-c5-b3-4b-2f-19-91-b3')
    @commethod(3)
    def GetLearnedKnowledgeAfterRecoveryComplete(ppLearnedKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLearnedForgottenKnowledge(ppLearnedForgottenKnowledge: POINTER(win32more.System.WindowsSync.IForgottenKnowledge_head)) -> win32more.Foundation.HRESULT: ...
class ISyncFullEnumerationChangeBatch(c_void_p):
    extends: win32more.System.WindowsSync.ISyncChangeBatchBase
    Guid = Guid('ef64197d-4f44-4ea2-b3-55-45-24-71-3e-3b-ed')
    @commethod(17)
    def GetLearnedKnowledgeAfterRecoveryComplete(ppLearnedKnowledgeAfterRecoveryComplete: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetClosedLowerBoundItemId(pbClosedLowerBoundItemId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetClosedUpperBoundItemId(pbClosedUpperBoundItemId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ISyncFullEnumerationChangeBatch2(c_void_p):
    extends: win32more.System.WindowsSync.ISyncFullEnumerationChangeBatch
    Guid = Guid('e06449f4-a205-4b65-97-24-01-b2-21-01-ee-c1')
    @commethod(20)
    def AddMergeTombstoneMetadataToGroup(pbOwnerReplicaId: c_char_p_no, pbWinnerItemId: c_char_p_no, pbItemId: c_char_p_no, pChangeVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), pCreationVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), dwWorkForChange: UInt32, ppChangeBuilder: POINTER(win32more.System.WindowsSync.ISyncChangeBuilder_head)) -> win32more.Foundation.HRESULT: ...
class ISynchronousDataRetriever(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9b22f2a9-a4cd-4648-9d-8e-3a-51-0d-4d-a0-4b')
    @commethod(3)
    def GetIdParameters(pIdParameters: POINTER(win32more.System.WindowsSync.ID_PARAMETERS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LoadChangeData(pLoadChangeContext: win32more.System.WindowsSync.ILoadChangeContext_head, ppUnkData: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ISyncKnowledge(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('615bbb53-c945-4203-bf-4b-2c-b6-59-19-a0-aa')
    @commethod(3)
    def GetOwnerReplicaId(pbReplicaId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Serialize(fSerializeReplicaKeyMap: win32more.Foundation.BOOL, pbKnowledge: c_char_p_no, pcbKnowledge: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetLocalTickCount(ullTickCount: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ContainsChange(pbVersionOwnerReplicaId: c_char_p_no, pgidItemId: c_char_p_no, pSyncVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ContainsChangeUnit(pbVersionOwnerReplicaId: c_char_p_no, pbItemId: c_char_p_no, pbChangeUnitId: c_char_p_no, pSyncVersion: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetScopeVector(riid: POINTER(Guid), ppUnk: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetReplicaKeyMap(ppReplicaKeyMap: POINTER(win32more.System.WindowsSync.IReplicaKeyMap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Clone(ppClonedKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ConvertVersion(pKnowledgeIn: win32more.System.WindowsSync.ISyncKnowledge_head, pbCurrentOwnerId: c_char_p_no, pVersionIn: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head), pbNewOwnerId: c_char_p_no, pcbIdSize: POINTER(UInt32), pVersionOut: POINTER(win32more.System.WindowsSync.SYNC_VERSION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def MapRemoteToLocal(pRemoteKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, ppMappedKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Union(pKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def ProjectOntoItem(pbItemId: c_char_p_no, ppKnowledgeOut: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ProjectOntoChangeUnit(pbItemId: c_char_p_no, pbChangeUnitId: c_char_p_no, ppKnowledgeOut: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def ProjectOntoRange(psrngSyncRange: POINTER(win32more.System.WindowsSync.SYNC_RANGE_head), ppKnowledgeOut: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def ExcludeItem(pbItemId: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def ExcludeChangeUnit(pbItemId: c_char_p_no, pbChangeUnitId: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def ContainsKnowledge(pKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def FindMinTickCountForReplica(pbReplicaId: c_char_p_no, pullReplicaTickCount: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetRangeExceptions(riid: POINTER(Guid), ppUnk: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetSingleItemExceptions(riid: POINTER(Guid), ppUnk: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetChangeUnitExceptions(riid: POINTER(Guid), ppUnk: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def FindClockVectorForItem(pbItemId: c_char_p_no, riid: POINTER(Guid), ppUnk: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def FindClockVectorForChangeUnit(pbItemId: c_char_p_no, pbChangeUnitId: c_char_p_no, riid: POINTER(Guid), ppUnk: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetVersion(pdwVersion: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ISyncKnowledge2(c_void_p):
    extends: win32more.System.WindowsSync.ISyncKnowledge
    Guid = Guid('ed0addc0-3b4b-46a1-9a-45-45-66-1d-21-14-c8')
    @commethod(27)
    def GetIdParameters(pIdParameters: POINTER(win32more.System.WindowsSync.ID_PARAMETERS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def ProjectOntoColumnSet(ppColumns: POINTER(c_char_p_no), count: UInt32, ppiKnowledgeOut: POINTER(win32more.System.WindowsSync.ISyncKnowledge2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def SerializeWithOptions(targetFormatVersion: win32more.System.WindowsSync.SYNC_SERIALIZATION_VERSION, dwFlags: UInt32, pbBuffer: c_char_p_no, pdwSerializedSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def GetLowestUncontainedId(piSyncKnowledge: win32more.System.WindowsSync.ISyncKnowledge2_head, pbItemId: c_char_p_no, pcbItemIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetInspector(riid: POINTER(Guid), ppiInspector: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetMinimumSupportedVersion(pVersion: POINTER(win32more.System.WindowsSync.SYNC_SERIALIZATION_VERSION)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetStatistics(which: win32more.System.WindowsSync.SYNC_STATISTICS, pValue: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def ContainsKnowledgeForItem(pKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pbItemId: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def ContainsKnowledgeForChangeUnit(pKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pbItemId: c_char_p_no, pbChangeUnitId: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def ProjectOntoKnowledgeWithPrerequisite(pPrerequisiteKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, pTemplateKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, ppProjectedKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def Complement(pSyncKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head, ppComplementedKnowledge: POINTER(win32more.System.WindowsSync.ISyncKnowledge_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def IntersectsWithKnowledge(pSyncKnowledge: win32more.System.WindowsSync.ISyncKnowledge_head) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def GetKnowledgeCookie(ppKnowledgeCookie: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def CompareToKnowledgeCookie(pKnowledgeCookie: win32more.System.Com.IUnknown_head, pResult: POINTER(win32more.System.WindowsSync.KNOWLEDGE_COOKIE_COMPARISON_RESULT)) -> win32more.Foundation.HRESULT: ...
class ISyncMergeTombstoneChange(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6ec62597-0903-484c-ad-61-36-d6-e9-38-f4-7b')
    @commethod(3)
    def GetWinnerItemId(pbWinnerItemId: c_char_p_no, pcbIdSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ISyncProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8f657056-2bce-4a17-8c-68-c7-bb-78-98-b5-6f')
    @commethod(3)
    def GetIdParameters(pIdParameters: POINTER(win32more.System.WindowsSync.ID_PARAMETERS_head)) -> win32more.Foundation.HRESULT: ...
class ISyncProviderConfigUI(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7b0705f6-cbcd-4071-ab-05-3b-dc-36-4d-4a-0c')
    @commethod(3)
    def Init(pguidInstanceId: POINTER(Guid), pguidContentType: POINTER(Guid), pConfigurationProperties: win32more.UI.Shell.PropertiesSystem.IPropertyStore_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetRegisteredProperties(ppConfigUIProperties: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateAndRegisterNewSyncProvider(hwndParent: win32more.Foundation.HWND, pUnkContext: win32more.System.Com.IUnknown_head, ppProviderInfo: POINTER(win32more.System.WindowsSync.ISyncProviderInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ModifySyncProvider(hwndParent: win32more.Foundation.HWND, pUnkContext: win32more.System.Com.IUnknown_head, pProviderInfo: win32more.System.WindowsSync.ISyncProviderInfo_head) -> win32more.Foundation.HRESULT: ...
class ISyncProviderConfigUIInfo(c_void_p):
    extends: win32more.UI.Shell.PropertiesSystem.IPropertyStore
    Guid = Guid('214141ae-33d7-4d8d-8e-37-f2-27-e8-80-ce-50')
    @commethod(8)
    def GetSyncProviderConfigUI(dwClsContext: UInt32, ppSyncProviderConfigUI: POINTER(win32more.System.WindowsSync.ISyncProviderConfigUI_head)) -> win32more.Foundation.HRESULT: ...
class ISyncProviderInfo(c_void_p):
    extends: win32more.UI.Shell.PropertiesSystem.IPropertyStore
    Guid = Guid('1ee135de-88a4-4504-b0-d0-f7-92-0d-7e-5b-a6')
    @commethod(8)
    def GetSyncProvider(dwClsContext: UInt32, ppSyncProvider: POINTER(win32more.System.WindowsSync.IRegisteredSyncProvider_head)) -> win32more.Foundation.HRESULT: ...
class ISyncProviderRegistration(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('cb45953b-7624-47bc-a4-72-eb-8c-ac-6b-22-2e')
    @commethod(3)
    def CreateSyncProviderConfigUIRegistrationInstance(pConfigUIConfig: POINTER(win32more.System.WindowsSync.SyncProviderConfigUIConfiguration_head), ppConfigUIInfo: POINTER(win32more.System.WindowsSync.ISyncProviderConfigUIInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterSyncProviderConfigUI(pguidInstanceId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumerateSyncProviderConfigUIs(pguidContentType: POINTER(Guid), dwSupportedArchitecture: UInt32, ppEnumSyncProviderConfigUIInfos: POINTER(win32more.System.WindowsSync.IEnumSyncProviderConfigUIInfos_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CreateSyncProviderRegistrationInstance(pProviderConfiguration: POINTER(win32more.System.WindowsSync.SyncProviderConfiguration_head), ppProviderInfo: POINTER(win32more.System.WindowsSync.ISyncProviderInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterSyncProvider(pguidInstanceId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSyncProviderConfigUIInfoforProvider(pguidProviderInstanceId: POINTER(Guid), ppProviderConfigUIInfo: POINTER(win32more.System.WindowsSync.ISyncProviderConfigUIInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EnumerateSyncProviders(pguidContentType: POINTER(Guid), dwStateFlagsToFilterMask: UInt32, dwStateFlagsToFilter: UInt32, refProviderClsId: POINTER(Guid), dwSupportedArchitecture: UInt32, ppEnumSyncProviderInfos: POINTER(win32more.System.WindowsSync.IEnumSyncProviderInfos_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetSyncProviderInfo(pguidInstanceId: POINTER(Guid), ppProviderInfo: POINTER(win32more.System.WindowsSync.ISyncProviderInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetSyncProviderFromInstanceId(pguidInstanceId: POINTER(Guid), dwClsContext: UInt32, ppSyncProvider: POINTER(win32more.System.WindowsSync.IRegisteredSyncProvider_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetSyncProviderConfigUIInfo(pguidInstanceId: POINTER(Guid), ppConfigUIInfo: POINTER(win32more.System.WindowsSync.ISyncProviderConfigUIInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetSyncProviderConfigUIFromInstanceId(pguidInstanceId: POINTER(Guid), dwClsContext: UInt32, ppConfigUI: POINTER(win32more.System.WindowsSync.ISyncProviderConfigUI_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetSyncProviderState(pguidInstanceId: POINTER(Guid), pdwStateFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetSyncProviderState(pguidInstanceId: POINTER(Guid), dwStateFlagsMask: UInt32, dwStateFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterForEvent(phEvent: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def RevokeEvent(hEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetChange(hEvent: win32more.Foundation.HANDLE, ppChange: POINTER(win32more.System.WindowsSync.ISyncRegistrationChange_head)) -> win32more.Foundation.HRESULT: ...
class ISyncRegistrationChange(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('eea0d9ae-6b29-43b4-9e-70-e3-ae-33-bb-2c-3b')
    @commethod(3)
    def GetEvent(psreEvent: POINTER(win32more.System.WindowsSync.SYNC_REGISTRATION_EVENT)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetInstanceId(pguidInstanceId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class ISyncSessionExtendedErrorInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('326c6810-790a-409b-b7-41-69-99-38-87-61-eb')
    @commethod(3)
    def GetSyncProviderWithError(ppProviderWithError: POINTER(win32more.System.WindowsSync.ISyncProvider_head)) -> win32more.Foundation.HRESULT: ...
class ISyncSessionState(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b8a940fe-9f01-483b-94-34-c3-7d-36-12-25-d9')
    @commethod(3)
    def IsCanceled(pfIsCanceled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetInfoForChangeApplication(pbChangeApplierInfo: c_char_p_no, pcbChangeApplierInfo: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def LoadInfoFromChangeApplication(pbChangeApplierInfo: c_char_p_no, cbChangeApplierInfo: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetForgottenKnowledgeRecoveryRangeStart(pbRangeStart: c_char_p_no, pcbRangeStart: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetForgottenKnowledgeRecoveryRangeEnd(pbRangeEnd: c_char_p_no, pcbRangeEnd: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetForgottenKnowledgeRecoveryRange(pRange: POINTER(win32more.System.WindowsSync.SYNC_RANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnProgress(provider: win32more.System.WindowsSync.SYNC_PROVIDER_ROLE, syncStage: win32more.System.WindowsSync.SYNC_PROGRESS_STAGE, dwCompletedWork: UInt32, dwTotalWork: UInt32) -> win32more.Foundation.HRESULT: ...
class ISyncSessionState2(c_void_p):
    extends: win32more.System.WindowsSync.ISyncSessionState
    Guid = Guid('9e37cfa3-9e38-4c61-9c-a3-ff-e8-10-b4-5c-a2')
    @commethod(10)
    def SetProviderWithError(fSelf: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetSessionErrorStatus(phrSessionError: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
KNOWLEDGE_COOKIE_COMPARISON_RESULT = Int32
KCCR_COOKIE_KNOWLEDGE_EQUAL: KNOWLEDGE_COOKIE_COMPARISON_RESULT = 0
KCCR_COOKIE_KNOWLEDGE_CONTAINED: KNOWLEDGE_COOKIE_COMPARISON_RESULT = 1
KCCR_COOKIE_KNOWLEDGE_CONTAINS: KNOWLEDGE_COOKIE_COMPARISON_RESULT = 2
KCCR_COOKIE_KNOWLEDGE_NOT_COMPARABLE: KNOWLEDGE_COOKIE_COMPARISON_RESULT = 3
SYNC_CONSTRAINT_RESOLVE_ACTION = Int32
SCRA_DEFER: SYNC_CONSTRAINT_RESOLVE_ACTION = 0
SCRA_ACCEPT_DESTINATION_PROVIDER: SYNC_CONSTRAINT_RESOLVE_ACTION = 1
SCRA_ACCEPT_SOURCE_PROVIDER: SYNC_CONSTRAINT_RESOLVE_ACTION = 2
SCRA_TRANSFER_AND_DEFER: SYNC_CONSTRAINT_RESOLVE_ACTION = 3
SCRA_MERGE: SYNC_CONSTRAINT_RESOLVE_ACTION = 4
SCRA_RENAME_SOURCE: SYNC_CONSTRAINT_RESOLVE_ACTION = 5
SCRA_RENAME_DESTINATION: SYNC_CONSTRAINT_RESOLVE_ACTION = 6
class SYNC_FILTER_CHANGE(Structure):
    fMoveIn: win32more.Foundation.BOOL
    moveVersion: win32more.System.WindowsSync.SYNC_VERSION
SYNC_FULL_ENUMERATION_ACTION = Int32
SFEA_FULL_ENUMERATION: SYNC_FULL_ENUMERATION_ACTION = 0
SFEA_PARTIAL_SYNC: SYNC_FULL_ENUMERATION_ACTION = 1
SFEA_ABORT: SYNC_FULL_ENUMERATION_ACTION = 2
SYNC_PROGRESS_STAGE = Int32
SPS_CHANGE_DETECTION: SYNC_PROGRESS_STAGE = 0
SPS_CHANGE_ENUMERATION: SYNC_PROGRESS_STAGE = 1
SPS_CHANGE_APPLICATION: SYNC_PROGRESS_STAGE = 2
SYNC_PROVIDER_ROLE = Int32
SPR_SOURCE: SYNC_PROVIDER_ROLE = 0
SPR_DESTINATION: SYNC_PROVIDER_ROLE = 1
class SYNC_RANGE(Structure):
    pbClosedLowerBound: c_char_p_no
    pbClosedUpperBound: c_char_p_no
SYNC_REGISTRATION_EVENT = Int32
SRE_PROVIDER_ADDED: SYNC_REGISTRATION_EVENT = 0
SRE_PROVIDER_REMOVED: SYNC_REGISTRATION_EVENT = 1
SRE_PROVIDER_UPDATED: SYNC_REGISTRATION_EVENT = 2
SRE_PROVIDER_STATE_CHANGED: SYNC_REGISTRATION_EVENT = 3
SRE_CONFIGUI_ADDED: SYNC_REGISTRATION_EVENT = 4
SRE_CONFIGUI_REMOVED: SYNC_REGISTRATION_EVENT = 5
SRE_CONFIGUI_UPDATED: SYNC_REGISTRATION_EVENT = 6
SYNC_RESOLVE_ACTION = Int32
SRA_DEFER: SYNC_RESOLVE_ACTION = 0
SRA_ACCEPT_DESTINATION_PROVIDER: SYNC_RESOLVE_ACTION = 1
SRA_ACCEPT_SOURCE_PROVIDER: SYNC_RESOLVE_ACTION = 2
SRA_MERGE: SYNC_RESOLVE_ACTION = 3
SRA_TRANSFER_AND_DEFER: SYNC_RESOLVE_ACTION = 4
SRA_LAST: SYNC_RESOLVE_ACTION = 5
SYNC_SERIALIZATION_VERSION = Int32
SYNC_SERIALIZATION_VERSION_V1: SYNC_SERIALIZATION_VERSION = 1
SYNC_SERIALIZATION_VERSION_V2: SYNC_SERIALIZATION_VERSION = 4
SYNC_SERIALIZATION_VERSION_V3: SYNC_SERIALIZATION_VERSION = 5
class SYNC_SESSION_STATISTICS(Structure):
    dwChangesApplied: UInt32
    dwChangesFailed: UInt32
SYNC_STATISTICS = Int32
SYNC_STATISTICS_RANGE_COUNT: SYNC_STATISTICS = 0
class SYNC_TIME(Structure):
    dwDate: UInt32
    dwTime: UInt32
class SYNC_VERSION(Structure):
    dwLastUpdatingReplicaKey: UInt32
    ullTickCount: UInt64
class SyncProviderConfigUIConfiguration(Structure):
    dwVersion: UInt32
    guidInstanceId: Guid
    clsidConfigUI: Guid
    guidContentType: Guid
    dwCapabilities: UInt32
    dwSupportedArchitecture: UInt32
    fIsGlobal: win32more.Foundation.BOOL
class SyncProviderConfiguration(Structure):
    dwVersion: UInt32
    guidInstanceId: Guid
    clsidProvider: Guid
    guidConfigUIInstanceId: Guid
    guidContentType: Guid
    dwCapabilities: UInt32
    dwSupportedArchitecture: UInt32
SyncProviderRegistration = Guid('f82b4ef1-93a9-4dde-80-15-f7-95-0a-1a-6e-31')
make_head(_module, 'PKEY_PROVIDER_INSTANCEID')
make_head(_module, 'PKEY_PROVIDER_CLSID')
make_head(_module, 'PKEY_PROVIDER_CONFIGUI')
make_head(_module, 'PKEY_PROVIDER_CONTENTTYPE')
make_head(_module, 'PKEY_PROVIDER_CAPABILITIES')
make_head(_module, 'PKEY_PROVIDER_SUPPORTED_ARCHITECTURE')
make_head(_module, 'PKEY_PROVIDER_NAME')
make_head(_module, 'PKEY_PROVIDER_DESCRIPTION')
make_head(_module, 'PKEY_PROVIDER_TOOLTIPS')
make_head(_module, 'PKEY_PROVIDER_ICON')
make_head(_module, 'PKEY_CONFIGUI_INSTANCEID')
make_head(_module, 'PKEY_CONFIGUI_CLSID')
make_head(_module, 'PKEY_CONFIGUI_CONTENTTYPE')
make_head(_module, 'PKEY_CONFIGUI_CAPABILITIES')
make_head(_module, 'PKEY_CONFIGUI_SUPPORTED_ARCHITECTURE')
make_head(_module, 'PKEY_CONFIGUI_IS_GLOBAL')
make_head(_module, 'PKEY_CONFIGUI_NAME')
make_head(_module, 'PKEY_CONFIGUI_DESCRIPTION')
make_head(_module, 'PKEY_CONFIGUI_TOOLTIPS')
make_head(_module, 'PKEY_CONFIGUI_ICON')
make_head(_module, 'PKEY_CONFIGUI_MENUITEM_NOUI')
make_head(_module, 'PKEY_CONFIGUI_MENUITEM')
make_head(_module, 'IAsynchronousDataRetriever')
make_head(_module, 'IChangeConflict')
make_head(_module, 'IChangeUnitException')
make_head(_module, 'IChangeUnitListFilterInfo')
make_head(_module, 'IClockVector')
make_head(_module, 'IClockVectorElement')
make_head(_module, 'ICombinedFilterInfo')
make_head(_module, 'IConstraintConflict')
make_head(_module, 'IConstructReplicaKeyMap')
make_head(_module, 'ICoreFragment')
make_head(_module, 'ICoreFragmentInspector')
make_head(_module, 'ICustomFilterInfo')
make_head(_module, 'ID_PARAMETER_PAIR')
make_head(_module, 'ID_PARAMETERS')
make_head(_module, 'IDataRetrieverCallback')
make_head(_module, 'IEnumChangeUnitExceptions')
make_head(_module, 'IEnumClockVector')
make_head(_module, 'IEnumFeedClockVector')
make_head(_module, 'IEnumItemIds')
make_head(_module, 'IEnumRangeExceptions')
make_head(_module, 'IEnumSingleItemExceptions')
make_head(_module, 'IEnumSyncChanges')
make_head(_module, 'IEnumSyncChangeUnits')
make_head(_module, 'IEnumSyncProviderConfigUIInfos')
make_head(_module, 'IEnumSyncProviderInfos')
make_head(_module, 'IFeedClockVector')
make_head(_module, 'IFeedClockVectorElement')
make_head(_module, 'IFilterKeyMap')
make_head(_module, 'IFilterRequestCallback')
make_head(_module, 'IFilterTrackingProvider')
make_head(_module, 'IFilterTrackingRequestCallback')
make_head(_module, 'IFilterTrackingSyncChangeBuilder')
make_head(_module, 'IForgottenKnowledge')
make_head(_module, 'IKnowledgeSyncProvider')
make_head(_module, 'ILoadChangeContext')
make_head(_module, 'IProviderConverter')
make_head(_module, 'IRangeException')
make_head(_module, 'IRecoverableError')
make_head(_module, 'IRecoverableErrorData')
make_head(_module, 'IRegisteredSyncProvider')
make_head(_module, 'IReplicaKeyMap')
make_head(_module, 'IRequestFilteredSync')
make_head(_module, 'ISingleItemException')
make_head(_module, 'ISupportFilteredSync')
make_head(_module, 'ISupportLastWriteTime')
make_head(_module, 'ISyncCallback')
make_head(_module, 'ISyncCallback2')
make_head(_module, 'ISyncChange')
make_head(_module, 'ISyncChangeBatch')
make_head(_module, 'ISyncChangeBatch2')
make_head(_module, 'ISyncChangeBatchAdvanced')
make_head(_module, 'ISyncChangeBatchBase')
make_head(_module, 'ISyncChangeBatchBase2')
make_head(_module, 'ISyncChangeBatchWithFilterKeyMap')
make_head(_module, 'ISyncChangeBatchWithPrerequisite')
make_head(_module, 'ISyncChangeBuilder')
make_head(_module, 'ISyncChangeUnit')
make_head(_module, 'ISyncChangeWithFilterKeyMap')
make_head(_module, 'ISyncChangeWithPrerequisite')
make_head(_module, 'ISyncConstraintCallback')
make_head(_module, 'ISyncDataConverter')
make_head(_module, 'ISyncFilter')
make_head(_module, 'ISyncFilterDeserializer')
make_head(_module, 'ISyncFilterInfo')
make_head(_module, 'ISyncFilterInfo2')
make_head(_module, 'ISyncFullEnumerationChange')
make_head(_module, 'ISyncFullEnumerationChangeBatch')
make_head(_module, 'ISyncFullEnumerationChangeBatch2')
make_head(_module, 'ISynchronousDataRetriever')
make_head(_module, 'ISyncKnowledge')
make_head(_module, 'ISyncKnowledge2')
make_head(_module, 'ISyncMergeTombstoneChange')
make_head(_module, 'ISyncProvider')
make_head(_module, 'ISyncProviderConfigUI')
make_head(_module, 'ISyncProviderConfigUIInfo')
make_head(_module, 'ISyncProviderInfo')
make_head(_module, 'ISyncProviderRegistration')
make_head(_module, 'ISyncRegistrationChange')
make_head(_module, 'ISyncSessionExtendedErrorInfo')
make_head(_module, 'ISyncSessionState')
make_head(_module, 'ISyncSessionState2')
make_head(_module, 'SYNC_FILTER_CHANGE')
make_head(_module, 'SYNC_RANGE')
make_head(_module, 'SYNC_SESSION_STATISTICS')
make_head(_module, 'SYNC_TIME')
make_head(_module, 'SYNC_VERSION')
make_head(_module, 'SyncProviderConfigUIConfiguration')
make_head(_module, 'SyncProviderConfiguration')
__all__ = [
    "CCR_COLLISION",
    "CCR_IDENTITY",
    "CCR_NOPARENT",
    "CCR_OTHER",
    "CONFLICT_RESOLUTION_POLICY",
    "CONSTRAINT_CONFLICT_REASON",
    "CRP_DESTINATION_PROVIDER_WINS",
    "CRP_LAST",
    "CRP_NONE",
    "CRP_SOURCE_PROVIDER_WINS",
    "FCT_INTERSECTION",
    "FILTERING_TYPE",
    "FILTER_COMBINATION_TYPE",
    "FT_CURRENT_ITEMS_AND_VERSIONS_FOR_MOVED_OUT_ITEMS",
    "FT_CURRENT_ITEMS_ONLY",
    "IAsynchronousDataRetriever",
    "IChangeConflict",
    "IChangeUnitException",
    "IChangeUnitListFilterInfo",
    "IClockVector",
    "IClockVectorElement",
    "ICombinedFilterInfo",
    "IConstraintConflict",
    "IConstructReplicaKeyMap",
    "ICoreFragment",
    "ICoreFragmentInspector",
    "ICustomFilterInfo",
    "ID_PARAMETERS",
    "ID_PARAMETER_PAIR",
    "IDataRetrieverCallback",
    "IEnumChangeUnitExceptions",
    "IEnumClockVector",
    "IEnumFeedClockVector",
    "IEnumItemIds",
    "IEnumRangeExceptions",
    "IEnumSingleItemExceptions",
    "IEnumSyncChangeUnits",
    "IEnumSyncChanges",
    "IEnumSyncProviderConfigUIInfos",
    "IEnumSyncProviderInfos",
    "IFeedClockVector",
    "IFeedClockVectorElement",
    "IFilterKeyMap",
    "IFilterRequestCallback",
    "IFilterTrackingProvider",
    "IFilterTrackingRequestCallback",
    "IFilterTrackingSyncChangeBuilder",
    "IForgottenKnowledge",
    "IKnowledgeSyncProvider",
    "ILoadChangeContext",
    "IProviderConverter",
    "IRangeException",
    "IRecoverableError",
    "IRecoverableErrorData",
    "IRegisteredSyncProvider",
    "IReplicaKeyMap",
    "IRequestFilteredSync",
    "ISingleItemException",
    "ISupportFilteredSync",
    "ISupportLastWriteTime",
    "ISyncCallback",
    "ISyncCallback2",
    "ISyncChange",
    "ISyncChangeBatch",
    "ISyncChangeBatch2",
    "ISyncChangeBatchAdvanced",
    "ISyncChangeBatchBase",
    "ISyncChangeBatchBase2",
    "ISyncChangeBatchWithFilterKeyMap",
    "ISyncChangeBatchWithPrerequisite",
    "ISyncChangeBuilder",
    "ISyncChangeUnit",
    "ISyncChangeWithFilterKeyMap",
    "ISyncChangeWithPrerequisite",
    "ISyncConstraintCallback",
    "ISyncDataConverter",
    "ISyncFilter",
    "ISyncFilterDeserializer",
    "ISyncFilterInfo",
    "ISyncFilterInfo2",
    "ISyncFullEnumerationChange",
    "ISyncFullEnumerationChangeBatch",
    "ISyncFullEnumerationChangeBatch2",
    "ISyncKnowledge",
    "ISyncKnowledge2",
    "ISyncMergeTombstoneChange",
    "ISyncProvider",
    "ISyncProviderConfigUI",
    "ISyncProviderConfigUIInfo",
    "ISyncProviderInfo",
    "ISyncProviderRegistration",
    "ISyncRegistrationChange",
    "ISyncSessionExtendedErrorInfo",
    "ISyncSessionState",
    "ISyncSessionState2",
    "ISynchronousDataRetriever",
    "KCCR_COOKIE_KNOWLEDGE_CONTAINED",
    "KCCR_COOKIE_KNOWLEDGE_CONTAINS",
    "KCCR_COOKIE_KNOWLEDGE_EQUAL",
    "KCCR_COOKIE_KNOWLEDGE_NOT_COMPARABLE",
    "KNOWLEDGE_COOKIE_COMPARISON_RESULT",
    "PKEY_CONFIGUI_CAPABILITIES",
    "PKEY_CONFIGUI_CLSID",
    "PKEY_CONFIGUI_CONTENTTYPE",
    "PKEY_CONFIGUI_DESCRIPTION",
    "PKEY_CONFIGUI_ICON",
    "PKEY_CONFIGUI_INSTANCEID",
    "PKEY_CONFIGUI_IS_GLOBAL",
    "PKEY_CONFIGUI_MENUITEM",
    "PKEY_CONFIGUI_MENUITEM_NOUI",
    "PKEY_CONFIGUI_NAME",
    "PKEY_CONFIGUI_SUPPORTED_ARCHITECTURE",
    "PKEY_CONFIGUI_TOOLTIPS",
    "PKEY_PROVIDER_CAPABILITIES",
    "PKEY_PROVIDER_CLSID",
    "PKEY_PROVIDER_CONFIGUI",
    "PKEY_PROVIDER_CONTENTTYPE",
    "PKEY_PROVIDER_DESCRIPTION",
    "PKEY_PROVIDER_ICON",
    "PKEY_PROVIDER_INSTANCEID",
    "PKEY_PROVIDER_NAME",
    "PKEY_PROVIDER_SUPPORTED_ARCHITECTURE",
    "PKEY_PROVIDER_TOOLTIPS",
    "SCRA_ACCEPT_DESTINATION_PROVIDER",
    "SCRA_ACCEPT_SOURCE_PROVIDER",
    "SCRA_DEFER",
    "SCRA_MERGE",
    "SCRA_RENAME_DESTINATION",
    "SCRA_RENAME_SOURCE",
    "SCRA_TRANSFER_AND_DEFER",
    "SFEA_ABORT",
    "SFEA_FULL_ENUMERATION",
    "SFEA_PARTIAL_SYNC",
    "SPR_DESTINATION",
    "SPR_SOURCE",
    "SPS_CHANGE_APPLICATION",
    "SPS_CHANGE_DETECTION",
    "SPS_CHANGE_ENUMERATION",
    "SRA_ACCEPT_DESTINATION_PROVIDER",
    "SRA_ACCEPT_SOURCE_PROVIDER",
    "SRA_DEFER",
    "SRA_LAST",
    "SRA_MERGE",
    "SRA_TRANSFER_AND_DEFER",
    "SRE_CONFIGUI_ADDED",
    "SRE_CONFIGUI_REMOVED",
    "SRE_CONFIGUI_UPDATED",
    "SRE_PROVIDER_ADDED",
    "SRE_PROVIDER_REMOVED",
    "SRE_PROVIDER_STATE_CHANGED",
    "SRE_PROVIDER_UPDATED",
    "SYNC_CHANGE_FLAG_DELETED",
    "SYNC_CHANGE_FLAG_DOES_NOT_EXIST",
    "SYNC_CHANGE_FLAG_GHOST",
    "SYNC_CONSTRAINT_RESOLVE_ACTION",
    "SYNC_FILTER_CHANGE",
    "SYNC_FILTER_INFO_COMBINED",
    "SYNC_FILTER_INFO_FLAG_CHANGE_UNIT_LIST",
    "SYNC_FILTER_INFO_FLAG_CUSTOM",
    "SYNC_FILTER_INFO_FLAG_ITEM_LIST",
    "SYNC_FULL_ENUMERATION_ACTION",
    "SYNC_PROGRESS_STAGE",
    "SYNC_PROVIDER_ROLE",
    "SYNC_RANGE",
    "SYNC_REGISTRATION_EVENT",
    "SYNC_RESOLVE_ACTION",
    "SYNC_SERIALIZATION_VERSION",
    "SYNC_SERIALIZATION_VERSION_V1",
    "SYNC_SERIALIZATION_VERSION_V2",
    "SYNC_SERIALIZATION_VERSION_V3",
    "SYNC_SERIALIZE_REPLICA_KEY_MAP",
    "SYNC_SESSION_STATISTICS",
    "SYNC_STATISTICS",
    "SYNC_STATISTICS_RANGE_COUNT",
    "SYNC_TIME",
    "SYNC_VERSION",
    "SYNC_VERSION_FLAG_FROM_FEED",
    "SYNC_VERSION_FLAG_HAS_BY",
    "SyncProviderConfigUIConfiguration",
    "SyncProviderConfiguration",
    "SyncProviderRegistration",
]
