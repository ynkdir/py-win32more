from win32more import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Search.Common
import win32more.UI.Shell.Common
import win32more.UI.Shell.PropertiesSystem

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
PKEY_PIDSTR_MAX = 10
def _define_PROPERTYKEY_head():
    class PROPERTYKEY(Structure):
        pass
    return PROPERTYKEY
def _define_PROPERTYKEY():
    PROPERTYKEY = win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head
    PROPERTYKEY._fields_ = [
        ("fmtid", Guid),
        ("pid", UInt32),
    ]
    return PROPERTYKEY
InMemoryPropertyStore = Guid('9a02e012-6303-4e1e-b9a1-630f802592c5')
InMemoryPropertyStoreMarshalByValue = Guid('d4ca0e2d-6da7-4b75-a97c-5f306f0eaedc')
PropertySystem = Guid('b8967f85-58ae-4f46-9fb2-5d7904798f4b')
def _define_IInitializeWithFile_head():
    class IInitializeWithFile(win32more.System.Com.IUnknown_head):
        Guid = Guid('b7d14566-0509-4cce-a71f-0a554233bd9b')
    return IInitializeWithFile
def _define_IInitializeWithFile():
    IInitializeWithFile = win32more.UI.Shell.PropertiesSystem.IInitializeWithFile_head
    IInitializeWithFile.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(3, 'Initialize', ((1, 'pszFilePath'),(1, 'grfMode'),)))
    return IInitializeWithFile
def _define_IInitializeWithStream_head():
    class IInitializeWithStream(win32more.System.Com.IUnknown_head):
        Guid = Guid('b824b49d-22ac-4161-ac8a-9916e8fa3f7f')
    return IInitializeWithStream
def _define_IInitializeWithStream():
    IInitializeWithStream = win32more.UI.Shell.PropertiesSystem.IInitializeWithStream_head
    IInitializeWithStream.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,UInt32, use_last_error=False)(3, 'Initialize', ((1, 'pstream'),(1, 'grfMode'),)))
    return IInitializeWithStream
def _define_IPropertyStore_head():
    class IPropertyStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('886d8eeb-8cf2-4446-8d02-cdba1dbdcf99')
    return IPropertyStore
def _define_IPropertyStore():
    IPropertyStore = win32more.UI.Shell.PropertiesSystem.IPropertyStore_head
    IPropertyStore.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'cProps'),)))
    IPropertyStore.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(4, 'GetAt', ((1, 'iProp'),(1, 'pkey'),)))
    IPropertyStore.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(5, 'GetValue', ((1, 'key'),(1, 'pv'),)))
    IPropertyStore.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(6, 'SetValue', ((1, 'key'),(1, 'propvar'),)))
    IPropertyStore.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Commit', ()))
    return IPropertyStore
def _define_INamedPropertyStore_head():
    class INamedPropertyStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('71604b0f-97b0-4764-8577-2f13e98a1422')
    return INamedPropertyStore
def _define_INamedPropertyStore():
    INamedPropertyStore = win32more.UI.Shell.PropertiesSystem.INamedPropertyStore_head
    INamedPropertyStore.GetNamedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(3, 'GetNamedValue', ((1, 'pszName'),(1, 'ppropvar'),)))
    INamedPropertyStore.SetNamedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(4, 'SetNamedValue', ((1, 'pszName'),(1, 'propvar'),)))
    INamedPropertyStore.GetNameCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetNameCount', ((1, 'pdwCount'),)))
    INamedPropertyStore.GetNameAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetNameAt', ((1, 'iProp'),(1, 'pbstrName'),)))
    return INamedPropertyStore
GETPROPERTYSTOREFLAGS = Int32
GPS_DEFAULT = 0
GPS_HANDLERPROPERTIESONLY = 1
GPS_READWRITE = 2
GPS_TEMPORARY = 4
GPS_FASTPROPERTIESONLY = 8
GPS_OPENSLOWITEM = 16
GPS_DELAYCREATION = 32
GPS_BESTEFFORT = 64
GPS_NO_OPLOCK = 128
GPS_PREFERQUERYPROPERTIES = 256
GPS_EXTRINSICPROPERTIES = 512
GPS_EXTRINSICPROPERTIESONLY = 1024
GPS_VOLATILEPROPERTIES = 2048
GPS_VOLATILEPROPERTIESONLY = 4096
GPS_MASK_VALID = 8191
def _define_IObjectWithPropertyKey_head():
    class IObjectWithPropertyKey(win32more.System.Com.IUnknown_head):
        Guid = Guid('fc0ca0a7-c316-4fd2-9031-3e628e6d4f23')
    return IObjectWithPropertyKey
def _define_IObjectWithPropertyKey():
    IObjectWithPropertyKey = win32more.UI.Shell.PropertiesSystem.IObjectWithPropertyKey_head
    IObjectWithPropertyKey.SetPropertyKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(3, 'SetPropertyKey', ((1, 'key'),)))
    IObjectWithPropertyKey.GetPropertyKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(4, 'GetPropertyKey', ((1, 'pkey'),)))
    return IObjectWithPropertyKey
PKA_FLAGS = Int32
PKA_SET = 0
PKA_APPEND = 1
PKA_DELETE = 2
def _define_IPropertyChange_head():
    class IPropertyChange(win32more.UI.Shell.PropertiesSystem.IObjectWithPropertyKey_head):
        Guid = Guid('f917bc8a-1bba-4478-a245-1bde03eb9431')
    return IPropertyChange
def _define_IPropertyChange():
    IPropertyChange = win32more.UI.Shell.PropertiesSystem.IPropertyChange_head
    IPropertyChange.ApplyToPropVariant = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(5, 'ApplyToPropVariant', ((1, 'propvarIn'),(1, 'ppropvarOut'),)))
    return IPropertyChange
def _define_IPropertyChangeArray_head():
    class IPropertyChangeArray(win32more.System.Com.IUnknown_head):
        Guid = Guid('380f5cad-1b5e-42f2-805d-637fd392d31e')
    return IPropertyChangeArray
def _define_IPropertyChangeArray():
    IPropertyChangeArray = win32more.UI.Shell.PropertiesSystem.IPropertyChangeArray_head
    IPropertyChangeArray.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pcOperations'),)))
    IPropertyChangeArray.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'GetAt', ((1, 'iIndex'),(1, 'riid'),(1, 'ppv'),)))
    IPropertyChangeArray.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Shell.PropertiesSystem.IPropertyChange_head, use_last_error=False)(5, 'InsertAt', ((1, 'iIndex'),(1, 'ppropChange'),)))
    IPropertyChangeArray.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyChange_head, use_last_error=False)(6, 'Append', ((1, 'ppropChange'),)))
    IPropertyChangeArray.AppendOrReplace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyChange_head, use_last_error=False)(7, 'AppendOrReplace', ((1, 'ppropChange'),)))
    IPropertyChangeArray.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'RemoveAt', ((1, 'iIndex'),)))
    IPropertyChangeArray.IsKeyInArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(9, 'IsKeyInArray', ((1, 'key'),)))
    return IPropertyChangeArray
def _define_IPropertyStoreCapabilities_head():
    class IPropertyStoreCapabilities(win32more.System.Com.IUnknown_head):
        Guid = Guid('c8e2d566-186e-4d49-bf41-6909ead56acc')
    return IPropertyStoreCapabilities
def _define_IPropertyStoreCapabilities():
    IPropertyStoreCapabilities = win32more.UI.Shell.PropertiesSystem.IPropertyStoreCapabilities_head
    IPropertyStoreCapabilities.IsPropertyWritable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(3, 'IsPropertyWritable', ((1, 'key'),)))
    return IPropertyStoreCapabilities
PSC_STATE = Int32
PSC_NORMAL = 0
PSC_NOTINSOURCE = 1
PSC_DIRTY = 2
PSC_READONLY = 3
def _define_IPropertyStoreCache_head():
    class IPropertyStoreCache(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head):
        Guid = Guid('3017056d-9a91-4e90-937d-746c72abbf4f')
    return IPropertyStoreCache
def _define_IPropertyStoreCache():
    IPropertyStoreCache = win32more.UI.Shell.PropertiesSystem.IPropertyStoreCache_head
    IPropertyStoreCache.GetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.UI.Shell.PropertiesSystem.PSC_STATE), use_last_error=False)(8, 'GetState', ((1, 'key'),(1, 'pstate'),)))
    IPropertyStoreCache.GetValueAndState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.UI.Shell.PropertiesSystem.PSC_STATE), use_last_error=False)(9, 'GetValueAndState', ((1, 'key'),(1, 'ppropvar'),(1, 'pstate'),)))
    IPropertyStoreCache.SetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.UI.Shell.PropertiesSystem.PSC_STATE, use_last_error=False)(10, 'SetState', ((1, 'key'),(1, 'state'),)))
    IPropertyStoreCache.SetValueAndState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PSC_STATE, use_last_error=False)(11, 'SetValueAndState', ((1, 'key'),(1, 'ppropvar'),(1, 'state'),)))
    return IPropertyStoreCache
PROPENUMTYPE = Int32
PET_DISCRETEVALUE = 0
PET_RANGEDVALUE = 1
PET_DEFAULTVALUE = 2
PET_ENDRANGE = 3
def _define_IPropertyEnumType_head():
    class IPropertyEnumType(win32more.System.Com.IUnknown_head):
        Guid = Guid('11e1fbf9-2d56-4a6b-8db3-7cd193a471f2')
    return IPropertyEnumType
def _define_IPropertyEnumType():
    IPropertyEnumType = win32more.UI.Shell.PropertiesSystem.IPropertyEnumType_head
    IPropertyEnumType.GetEnumType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPENUMTYPE), use_last_error=False)(3, 'GetEnumType', ((1, 'penumtype'),)))
    IPropertyEnumType.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(4, 'GetValue', ((1, 'ppropvar'),)))
    IPropertyEnumType.GetRangeMinValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(5, 'GetRangeMinValue', ((1, 'ppropvarMin'),)))
    IPropertyEnumType.GetRangeSetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(6, 'GetRangeSetValue', ((1, 'ppropvarSet'),)))
    IPropertyEnumType.GetDisplayText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetDisplayText', ((1, 'ppszDisplay'),)))
    return IPropertyEnumType
def _define_IPropertyEnumType2_head():
    class IPropertyEnumType2(win32more.UI.Shell.PropertiesSystem.IPropertyEnumType_head):
        Guid = Guid('9b6e051c-5ddd-4321-9070-fe2acb55e794')
    return IPropertyEnumType2
def _define_IPropertyEnumType2():
    IPropertyEnumType2 = win32more.UI.Shell.PropertiesSystem.IPropertyEnumType2_head
    IPropertyEnumType2.GetImageReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(8, 'GetImageReference', ((1, 'ppszImageRes'),)))
    return IPropertyEnumType2
def _define_IPropertyEnumTypeList_head():
    class IPropertyEnumTypeList(win32more.System.Com.IUnknown_head):
        Guid = Guid('a99400f4-3d84-4557-94ba-1242fb2cc9a6')
    return IPropertyEnumTypeList
def _define_IPropertyEnumTypeList():
    IPropertyEnumTypeList = win32more.UI.Shell.PropertiesSystem.IPropertyEnumTypeList_head
    IPropertyEnumTypeList.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pctypes'),)))
    IPropertyEnumTypeList.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'GetAt', ((1, 'itype'),(1, 'riid'),(1, 'ppv'),)))
    IPropertyEnumTypeList.GetConditionAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(5, 'GetConditionAt', ((1, 'nIndex'),(1, 'riid'),(1, 'ppv'),)))
    IPropertyEnumTypeList.FindMatchingIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32), use_last_error=False)(6, 'FindMatchingIndex', ((1, 'propvarCmp'),(1, 'pnIndex'),)))
    return IPropertyEnumTypeList
PROPDESC_TYPE_FLAGS = Int32
PDTF_DEFAULT = 0
PDTF_MULTIPLEVALUES = 1
PDTF_ISINNATE = 2
PDTF_ISGROUP = 4
PDTF_CANGROUPBY = 8
PDTF_CANSTACKBY = 16
PDTF_ISTREEPROPERTY = 32
PDTF_INCLUDEINFULLTEXTQUERY = 64
PDTF_ISVIEWABLE = 128
PDTF_ISQUERYABLE = 256
PDTF_CANBEPURGED = 512
PDTF_SEARCHRAWVALUE = 1024
PDTF_DONTCOERCEEMPTYSTRINGS = 2048
PDTF_ALWAYSINSUPPLEMENTALSTORE = 4096
PDTF_ISSYSTEMPROPERTY = -2147483648
PDTF_MASK_ALL = -2147475457
PROPDESC_VIEW_FLAGS = Int32
PDVF_DEFAULT = 0
PDVF_CENTERALIGN = 1
PDVF_RIGHTALIGN = 2
PDVF_BEGINNEWGROUP = 4
PDVF_FILLAREA = 8
PDVF_SORTDESCENDING = 16
PDVF_SHOWONLYIFPRESENT = 32
PDVF_SHOWBYDEFAULT = 64
PDVF_SHOWINPRIMARYLIST = 128
PDVF_SHOWINSECONDARYLIST = 256
PDVF_HIDELABEL = 512
PDVF_HIDDEN = 2048
PDVF_CANWRAP = 4096
PDVF_MASK_ALL = 7167
PROPDESC_DISPLAYTYPE = Int32
PDDT_STRING = 0
PDDT_NUMBER = 1
PDDT_BOOLEAN = 2
PDDT_DATETIME = 3
PDDT_ENUMERATED = 4
PROPDESC_GROUPING_RANGE = Int32
PDGR_DISCRETE = 0
PDGR_ALPHANUMERIC = 1
PDGR_SIZE = 2
PDGR_DYNAMIC = 3
PDGR_DATE = 4
PDGR_PERCENT = 5
PDGR_ENUMERATED = 6
PROPDESC_FORMAT_FLAGS = Int32
PDFF_DEFAULT = 0
PDFF_PREFIXNAME = 1
PDFF_FILENAME = 2
PDFF_ALWAYSKB = 4
PDFF_RESERVED_RIGHTTOLEFT = 8
PDFF_SHORTTIME = 16
PDFF_LONGTIME = 32
PDFF_HIDETIME = 64
PDFF_SHORTDATE = 128
PDFF_LONGDATE = 256
PDFF_HIDEDATE = 512
PDFF_RELATIVEDATE = 1024
PDFF_USEEDITINVITATION = 2048
PDFF_READONLY = 4096
PDFF_NOAUTOREADINGORDER = 8192
PROPDESC_SORTDESCRIPTION = Int32
PDSD_GENERAL = 0
PDSD_A_Z = 1
PDSD_LOWEST_HIGHEST = 2
PDSD_SMALLEST_BIGGEST = 3
PDSD_OLDEST_NEWEST = 4
PROPDESC_RELATIVEDESCRIPTION_TYPE = Int32
PDRDT_GENERAL = 0
PDRDT_DATE = 1
PDRDT_SIZE = 2
PDRDT_COUNT = 3
PDRDT_REVISION = 4
PDRDT_LENGTH = 5
PDRDT_DURATION = 6
PDRDT_SPEED = 7
PDRDT_RATE = 8
PDRDT_RATING = 9
PDRDT_PRIORITY = 10
PROPDESC_AGGREGATION_TYPE = Int32
PDAT_DEFAULT = 0
PDAT_FIRST = 1
PDAT_SUM = 2
PDAT_AVERAGE = 3
PDAT_DATERANGE = 4
PDAT_UNION = 5
PDAT_MAX = 6
PDAT_MIN = 7
PROPDESC_CONDITION_TYPE = Int32
PDCOT_NONE = 0
PDCOT_STRING = 1
PDCOT_SIZE = 2
PDCOT_DATETIME = 3
PDCOT_BOOLEAN = 4
PDCOT_NUMBER = 5
def _define_IPropertyDescription_head():
    class IPropertyDescription(win32more.System.Com.IUnknown_head):
        Guid = Guid('6f79d558-3e96-4549-a1d1-7d75d2288814')
    return IPropertyDescription
def _define_IPropertyDescription():
    IPropertyDescription = win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head
    IPropertyDescription.GetPropertyKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(3, 'GetPropertyKey', ((1, 'pkey'),)))
    IPropertyDescription.GetCanonicalName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetCanonicalName', ((1, 'ppszName'),)))
    IPropertyDescription.GetPropertyType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(5, 'GetPropertyType', ((1, 'pvartype'),)))
    IPropertyDescription.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetDisplayName', ((1, 'ppszName'),)))
    IPropertyDescription.GetEditInvitation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetEditInvitation', ((1, 'ppszInvite'),)))
    IPropertyDescription.GetTypeFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS), use_last_error=False)(8, 'GetTypeFlags', ((1, 'mask'),(1, 'ppdtFlags'),)))
    IPropertyDescription.GetViewFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS), use_last_error=False)(9, 'GetViewFlags', ((1, 'ppdvFlags'),)))
    IPropertyDescription.GetDefaultColumnWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetDefaultColumnWidth', ((1, 'pcxChars'),)))
    IPropertyDescription.GetDisplayType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_DISPLAYTYPE), use_last_error=False)(11, 'GetDisplayType', ((1, 'pdisplaytype'),)))
    IPropertyDescription.GetColumnState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'GetColumnState', ((1, 'pcsFlags'),)))
    IPropertyDescription.GetGroupingRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE), use_last_error=False)(13, 'GetGroupingRange', ((1, 'pgr'),)))
    IPropertyDescription.GetRelativeDescriptionType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE), use_last_error=False)(14, 'GetRelativeDescriptionType', ((1, 'prdt'),)))
    IPropertyDescription.GetRelativeDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(15, 'GetRelativeDescription', ((1, 'propvar1'),(1, 'propvar2'),(1, 'ppszDesc1'),(1, 'ppszDesc2'),)))
    IPropertyDescription.GetSortDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_SORTDESCRIPTION), use_last_error=False)(16, 'GetSortDescription', ((1, 'psd'),)))
    IPropertyDescription.GetSortDescriptionLabel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(17, 'GetSortDescriptionLabel', ((1, 'fDescending'),(1, 'ppszDescription'),)))
    IPropertyDescription.GetAggregationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE), use_last_error=False)(18, 'GetAggregationType', ((1, 'paggtype'),)))
    IPropertyDescription.GetConditionType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_CONDITION_TYPE),POINTER(win32more.System.Search.Common.CONDITION_OPERATION), use_last_error=False)(19, 'GetConditionType', ((1, 'pcontype'),(1, 'popDefault'),)))
    IPropertyDescription.GetEnumTypeList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(20, 'GetEnumTypeList', ((1, 'riid'),(1, 'ppv'),)))
    IPropertyDescription.CoerceToCanonicalValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(21, 'CoerceToCanonicalValue', ((1, 'ppropvar'),)))
    IPropertyDescription.FormatForDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(22, 'FormatForDisplay', ((1, 'propvar'),(1, 'pdfFlags'),(1, 'ppszDisplay'),)))
    IPropertyDescription.IsValueCanonical = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(23, 'IsValueCanonical', ((1, 'propvar'),)))
    return IPropertyDescription
def _define_IPropertyDescription2_head():
    class IPropertyDescription2(win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head):
        Guid = Guid('57d2eded-5062-400e-b107-5dae79fe57a6')
    return IPropertyDescription2
def _define_IPropertyDescription2():
    IPropertyDescription2 = win32more.UI.Shell.PropertiesSystem.IPropertyDescription2_head
    IPropertyDescription2.GetImageReferenceForValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(24, 'GetImageReferenceForValue', ((1, 'propvar'),(1, 'ppszImageRes'),)))
    return IPropertyDescription2
def _define_IPropertyDescriptionAliasInfo_head():
    class IPropertyDescriptionAliasInfo(win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head):
        Guid = Guid('f67104fc-2af9-46fd-b32d-243c1404f3d1')
    return IPropertyDescriptionAliasInfo
def _define_IPropertyDescriptionAliasInfo():
    IPropertyDescriptionAliasInfo = win32more.UI.Shell.PropertiesSystem.IPropertyDescriptionAliasInfo_head
    IPropertyDescriptionAliasInfo.GetSortByAlias = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(24, 'GetSortByAlias', ((1, 'riid'),(1, 'ppv'),)))
    IPropertyDescriptionAliasInfo.GetAdditionalSortByAliases = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(25, 'GetAdditionalSortByAliases', ((1, 'riid'),(1, 'ppv'),)))
    return IPropertyDescriptionAliasInfo
PROPDESC_SEARCHINFO_FLAGS = Int32
PDSIF_DEFAULT = 0
PDSIF_ININVERTEDINDEX = 1
PDSIF_ISCOLUMN = 2
PDSIF_ISCOLUMNSPARSE = 4
PDSIF_ALWAYSINCLUDE = 8
PDSIF_USEFORTYPEAHEAD = 16
PROPDESC_COLUMNINDEX_TYPE = Int32
PDCIT_NONE = 0
PDCIT_ONDISK = 1
PDCIT_INMEMORY = 2
PDCIT_ONDEMAND = 3
PDCIT_ONDISKALL = 4
PDCIT_ONDISKVECTOR = 5
def _define_IPropertyDescriptionSearchInfo_head():
    class IPropertyDescriptionSearchInfo(win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head):
        Guid = Guid('078f91bd-29a2-440f-924e-46a291524520')
    return IPropertyDescriptionSearchInfo
def _define_IPropertyDescriptionSearchInfo():
    IPropertyDescriptionSearchInfo = win32more.UI.Shell.PropertiesSystem.IPropertyDescriptionSearchInfo_head
    IPropertyDescriptionSearchInfo.GetSearchInfoFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_SEARCHINFO_FLAGS), use_last_error=False)(24, 'GetSearchInfoFlags', ((1, 'ppdsiFlags'),)))
    IPropertyDescriptionSearchInfo.GetColumnIndexType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_COLUMNINDEX_TYPE), use_last_error=False)(25, 'GetColumnIndexType', ((1, 'ppdciType'),)))
    IPropertyDescriptionSearchInfo.GetProjectionString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(26, 'GetProjectionString', ((1, 'ppszProjection'),)))
    IPropertyDescriptionSearchInfo.GetMaxSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(27, 'GetMaxSize', ((1, 'pcbMaxSize'),)))
    return IPropertyDescriptionSearchInfo
def _define_IPropertyDescriptionRelatedPropertyInfo_head():
    class IPropertyDescriptionRelatedPropertyInfo(win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head):
        Guid = Guid('507393f4-2a3d-4a60-b59e-d9c75716c2dd')
    return IPropertyDescriptionRelatedPropertyInfo
def _define_IPropertyDescriptionRelatedPropertyInfo():
    IPropertyDescriptionRelatedPropertyInfo = win32more.UI.Shell.PropertiesSystem.IPropertyDescriptionRelatedPropertyInfo_head
    IPropertyDescriptionRelatedPropertyInfo.GetRelatedProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(24, 'GetRelatedProperty', ((1, 'pszRelationshipName'),(1, 'riid'),(1, 'ppv'),)))
    return IPropertyDescriptionRelatedPropertyInfo
PROPDESC_ENUMFILTER = Int32
PDEF_ALL = 0
PDEF_SYSTEM = 1
PDEF_NONSYSTEM = 2
PDEF_VIEWABLE = 3
PDEF_QUERYABLE = 4
PDEF_INFULLTEXTQUERY = 5
PDEF_COLUMN = 6
def _define_IPropertySystem_head():
    class IPropertySystem(win32more.System.Com.IUnknown_head):
        Guid = Guid('ca724e8a-c3e6-442b-88a4-6fb0db8035a3')
    return IPropertySystem
def _define_IPropertySystem():
    IPropertySystem = win32more.UI.Shell.PropertiesSystem.IPropertySystem_head
    IPropertySystem.GetPropertyDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'GetPropertyDescription', ((1, 'propkey'),(1, 'riid'),(1, 'ppv'),)))
    IPropertySystem.GetPropertyDescriptionByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'GetPropertyDescriptionByName', ((1, 'pszCanonicalName'),(1, 'riid'),(1, 'ppv'),)))
    IPropertySystem.GetPropertyDescriptionListFromString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(5, 'GetPropertyDescriptionListFromString', ((1, 'pszPropList'),(1, 'riid'),(1, 'ppv'),)))
    IPropertySystem.EnumeratePropertyDescriptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'EnumeratePropertyDescriptions', ((1, 'filterOn'),(1, 'riid'),(1, 'ppv'),)))
    IPropertySystem.FormatForDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,POINTER(Char),UInt32, use_last_error=False)(7, 'FormatForDisplay', ((1, 'key'),(1, 'propvar'),(1, 'pdff'),(1, 'pszText'),(1, 'cchText'),)))
    IPropertySystem.FormatForDisplayAlloc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(8, 'FormatForDisplayAlloc', ((1, 'key'),(1, 'propvar'),(1, 'pdff'),(1, 'ppszDisplay'),)))
    IPropertySystem.RegisterPropertySchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(9, 'RegisterPropertySchema', ((1, 'pszPath'),)))
    IPropertySystem.UnregisterPropertySchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(10, 'UnregisterPropertySchema', ((1, 'pszPath'),)))
    IPropertySystem.RefreshPropertySchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'RefreshPropertySchema', ()))
    return IPropertySystem
def _define_IPropertyDescriptionList_head():
    class IPropertyDescriptionList(win32more.System.Com.IUnknown_head):
        Guid = Guid('1f9fc1d0-c39b-4b26-817f-011967d3440e')
    return IPropertyDescriptionList
def _define_IPropertyDescriptionList():
    IPropertyDescriptionList = win32more.UI.Shell.PropertiesSystem.IPropertyDescriptionList_head
    IPropertyDescriptionList.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pcElem'),)))
    IPropertyDescriptionList.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'GetAt', ((1, 'iElem'),(1, 'riid'),(1, 'ppv'),)))
    return IPropertyDescriptionList
def _define_IPropertyStoreFactory_head():
    class IPropertyStoreFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('bc110b6d-57e8-4148-a9c6-91015ab2f3a5')
    return IPropertyStoreFactory
def _define_IPropertyStoreFactory():
    IPropertyStoreFactory = win32more.UI.Shell.PropertiesSystem.IPropertyStoreFactory_head
    IPropertyStoreFactory.GetPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'GetPropertyStore', ((1, 'flags'),(1, 'pUnkFactory'),(1, 'riid'),(1, 'ppv'),)))
    IPropertyStoreFactory.GetPropertyStoreForKeys = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32,win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'GetPropertyStoreForKeys', ((1, 'rgKeys'),(1, 'cKeys'),(1, 'flags'),(1, 'riid'),(1, 'ppv'),)))
    return IPropertyStoreFactory
def _define_IDelayedPropertyStoreFactory_head():
    class IDelayedPropertyStoreFactory(win32more.UI.Shell.PropertiesSystem.IPropertyStoreFactory_head):
        Guid = Guid('40d4577f-e237-4bdb-bd69-58f089431b6a')
    return IDelayedPropertyStoreFactory
def _define_IDelayedPropertyStoreFactory():
    IDelayedPropertyStoreFactory = win32more.UI.Shell.PropertiesSystem.IDelayedPropertyStoreFactory_head
    IDelayedPropertyStoreFactory.GetDelayedPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(5, 'GetDelayedPropertyStore', ((1, 'flags'),(1, 'dwStoreId'),(1, 'riid'),(1, 'ppv'),)))
    return IDelayedPropertyStoreFactory
_PERSIST_SPROPSTORE_FLAGS = Int32
FPSPS_DEFAULT = 0
FPSPS_READONLY = 1
FPSPS_TREAT_NEW_VALUES_AS_DIRTY = 2
def _define_SERIALIZEDPROPSTORAGE_head():
    class SERIALIZEDPROPSTORAGE(Structure):
        pass
    return SERIALIZEDPROPSTORAGE
def _define_SERIALIZEDPROPSTORAGE():
    SERIALIZEDPROPSTORAGE = win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head
    return SERIALIZEDPROPSTORAGE
def _define_IPersistSerializedPropStorage_head():
    class IPersistSerializedPropStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('e318ad57-0aa0-450f-aca5-6fab7103d917')
    return IPersistSerializedPropStorage
def _define_IPersistSerializedPropStorage():
    IPersistSerializedPropStorage = win32more.UI.Shell.PropertiesSystem.IPersistSerializedPropStorage_head
    IPersistSerializedPropStorage.SetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'SetFlags', ((1, 'flags'),)))
    IPersistSerializedPropStorage.SetPropertyStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head),UInt32, use_last_error=False)(4, 'SetPropertyStorage', ((1, 'psps'),(1, 'cb'),)))
    IPersistSerializedPropStorage.GetPropertyStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head)),POINTER(UInt32), use_last_error=False)(5, 'GetPropertyStorage', ((1, 'ppsps'),(1, 'pcb'),)))
    return IPersistSerializedPropStorage
def _define_IPersistSerializedPropStorage2_head():
    class IPersistSerializedPropStorage2(win32more.UI.Shell.PropertiesSystem.IPersistSerializedPropStorage_head):
        Guid = Guid('77effa68-4f98-4366-ba72-573b3d880571')
    return IPersistSerializedPropStorage2
def _define_IPersistSerializedPropStorage2():
    IPersistSerializedPropStorage2 = win32more.UI.Shell.PropertiesSystem.IPersistSerializedPropStorage2_head
    IPersistSerializedPropStorage2.GetPropertyStorageSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetPropertyStorageSize', ((1, 'pcb'),)))
    IPersistSerializedPropStorage2.GetPropertyStorageBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head),UInt32,POINTER(UInt32), use_last_error=False)(7, 'GetPropertyStorageBuffer', ((1, 'psps'),(1, 'cb'),(1, 'pcbWritten'),)))
    return IPersistSerializedPropStorage2
def _define_IPropertySystemChangeNotify_head():
    class IPropertySystemChangeNotify(win32more.System.Com.IUnknown_head):
        Guid = Guid('fa955fd9-38be-4879-a6ce-824cf52d609f')
    return IPropertySystemChangeNotify
def _define_IPropertySystemChangeNotify():
    IPropertySystemChangeNotify = win32more.UI.Shell.PropertiesSystem.IPropertySystemChangeNotify_head
    IPropertySystemChangeNotify.SchemaRefreshed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'SchemaRefreshed', ()))
    return IPropertySystemChangeNotify
def _define_ICreateObject_head():
    class ICreateObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('75121952-e0d0-43e5-9380-1d80483acf72')
    return ICreateObject
def _define_ICreateObject():
    ICreateObject = win32more.UI.Shell.PropertiesSystem.ICreateObject_head
    ICreateObject.CreateObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CreateObject', ((1, 'clsid'),(1, 'pUnkOuter'),(1, 'riid'),(1, 'ppv'),)))
    return ICreateObject
PSTIME_FLAGS = Int32
PSTF_UTC = 0
PSTF_LOCAL = 1
PROPVAR_COMPARE_UNIT = Int32
PVCU_DEFAULT = 0
PVCU_SECOND = 1
PVCU_MINUTE = 2
PVCU_HOUR = 3
PVCU_DAY = 4
PVCU_MONTH = 5
PVCU_YEAR = 6
PROPVAR_COMPARE_FLAGS = Int32
PVCF_DEFAULT = 0
PVCF_TREATEMPTYASGREATERTHAN = 1
PVCF_USESTRCMP = 2
PVCF_USESTRCMPC = 4
PVCF_USESTRCMPI = 8
PVCF_USESTRCMPIC = 16
PVCF_DIGITSASNUMBERS_CASESENSITIVE = 32
PROPVAR_CHANGE_FLAGS = Int32
PVCHF_DEFAULT = 0
PVCHF_NOVALUEPROP = 1
PVCHF_ALPHABOOL = 2
PVCHF_NOUSEROVERRIDE = 4
PVCHF_LOCALBOOL = 8
PVCHF_NOHEXSTRING = 16
DRAWPROGRESSFLAGS = Int32
DPF_NONE = 0
DPF_MARQUEE = 1
DPF_MARQUEE_COMPLETE = 2
DPF_ERROR = 4
DPF_WARNING = 8
DPF_STOPPED = 16
SYNC_TRANSFER_STATUS = Int32
STS_NONE = 0
STS_NEEDSUPLOAD = 1
STS_NEEDSDOWNLOAD = 2
STS_TRANSFERRING = 4
STS_PAUSED = 8
STS_HASERROR = 16
STS_FETCHING_METADATA = 32
STS_USER_REQUESTED_REFRESH = 64
STS_HASWARNING = 128
STS_EXCLUDED = 256
STS_INCOMPLETE = 512
STS_PLACEHOLDER_IFEMPTY = 1024
PLACEHOLDER_STATES = Int32
PS_NONE = 0
PS_MARKED_FOR_OFFLINE_AVAILABILITY = 1
PS_FULL_PRIMARY_STREAM_AVAILABLE = 2
PS_CREATE_FILE_ACCESSIBLE = 4
PS_CLOUDFILE_PLACEHOLDER = 8
PS_DEFAULT = 7
PS_ALL = 15
PROPERTYUI_NAME_FLAGS = Int32
PUIFNF_DEFAULT = 0
PUIFNF_MNEMONIC = 1
PROPERTYUI_FLAGS = Int32
PUIF_DEFAULT = 0
PUIF_RIGHTALIGN = 1
PUIF_NOLABELININFOTIP = 2
PROPERTYUI_FORMAT_FLAGS = Int32
PUIFFDF_DEFAULT = 0
PUIFFDF_RIGHTTOLEFT = 1
PUIFFDF_SHORTFORMAT = 2
PUIFFDF_NOTIME = 4
PUIFFDF_FRIENDLYDATE = 8
def _define_IPropertyUI_head():
    class IPropertyUI(win32more.System.Com.IUnknown_head):
        Guid = Guid('757a7d9f-919a-4118-99d7-dbb208c8cc66')
    return IPropertyUI
def _define_IPropertyUI():
    IPropertyUI = win32more.UI.Shell.PropertiesSystem.IPropertyUI_head
    IPropertyUI.ParsePropertyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(3, 'ParsePropertyName', ((1, 'pszName'),(1, 'pfmtid'),(1, 'ppid'),(1, 'pchEaten'),)))
    IPropertyUI.GetCannonicalName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Char),UInt32, use_last_error=False)(4, 'GetCannonicalName', ((1, 'fmtid'),(1, 'pid'),(1, 'pwszText'),(1, 'cchText'),)))
    IPropertyUI.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,win32more.UI.Shell.PropertiesSystem.PROPERTYUI_NAME_FLAGS,POINTER(Char),UInt32, use_last_error=False)(5, 'GetDisplayName', ((1, 'fmtid'),(1, 'pid'),(1, 'flags'),(1, 'pwszText'),(1, 'cchText'),)))
    IPropertyUI.GetPropertyDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Char),UInt32, use_last_error=False)(6, 'GetPropertyDescription', ((1, 'fmtid'),(1, 'pid'),(1, 'pwszText'),(1, 'cchText'),)))
    IPropertyUI.GetDefaultWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(UInt32), use_last_error=False)(7, 'GetDefaultWidth', ((1, 'fmtid'),(1, 'pid'),(1, 'pcxChars'),)))
    IPropertyUI.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYUI_FLAGS), use_last_error=False)(8, 'GetFlags', ((1, 'fmtid'),(1, 'pid'),(1, 'pflags'),)))
    IPropertyUI.FormatForDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPERTYUI_FORMAT_FLAGS,POINTER(Char),UInt32, use_last_error=False)(9, 'FormatForDisplay', ((1, 'fmtid'),(1, 'pid'),(1, 'ppropvar'),(1, 'puiff'),(1, 'pwszText'),(1, 'cchText'),)))
    IPropertyUI.GetHelpInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Char),UInt32,POINTER(UInt32), use_last_error=False)(10, 'GetHelpInfo', ((1, 'fmtid'),(1, 'pid'),(1, 'pwszHelpFile'),(1, 'cch'),(1, 'puHelpID'),)))
    return IPropertyUI
PDOPSTATUS = Int32
PDOPS_RUNNING = 1
PDOPS_PAUSED = 2
PDOPS_CANCELLED = 3
PDOPS_STOPPED = 4
PDOPS_ERRORS = 5
SYNC_ENGINE_STATE_FLAGS = Int32
SESF_NONE = 0
SESF_SERVICE_QUOTA_NEARING_LIMIT = 1
SESF_SERVICE_QUOTA_EXCEEDED_LIMIT = 2
SESF_AUTHENTICATION_ERROR = 4
SESF_PAUSED_DUE_TO_METERED_NETWORK = 8
SESF_PAUSED_DUE_TO_DISK_SPACE_FULL = 16
SESF_PAUSED_DUE_TO_CLIENT_POLICY = 32
SESF_PAUSED_DUE_TO_SERVICE_POLICY = 64
SESF_SERVICE_UNAVAILABLE = 128
SESF_PAUSED_DUE_TO_USER_REQUEST = 256
SESF_ALL_FLAGS = 511
def _define_PROPPRG_head():
    class PROPPRG(Structure):
        pass
    return PROPPRG
def _define_PROPPRG():
    PROPPRG = win32more.UI.Shell.PropertiesSystem.PROPPRG_head
    PROPPRG._pack_ = 1
    PROPPRG._fields_ = [
        ("flPrg", UInt16),
        ("flPrgInit", UInt16),
        ("achTitle", win32more.Foundation.CHAR * 30),
        ("achCmdLine", win32more.Foundation.CHAR * 128),
        ("achWorkDir", win32more.Foundation.CHAR * 64),
        ("wHotKey", UInt16),
        ("achIconFile", win32more.Foundation.CHAR * 80),
        ("wIconIndex", UInt16),
        ("dwEnhModeFlags", UInt32),
        ("dwRealModeFlags", UInt32),
        ("achOtherFile", win32more.Foundation.CHAR * 80),
        ("achPIFFile", win32more.Foundation.CHAR * 260),
    ]
    return PROPPRG
def _define_PropVariantToWinRTPropertyValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PropVariantToWinRTPropertyValue", windll["PROPSYS"]), ((1, 'propvar'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinRTPropertyValueToPropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("WinRTPropertyValueToPropVariant", windll["PROPSYS"]), ((1, 'punkPropertyValue'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSFormatForDisplay():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,POINTER(Char),UInt32, use_last_error=False)(("PSFormatForDisplay", windll["PROPSYS"]), ((1, 'propkey'),(1, 'propvar'),(1, 'pdfFlags'),(1, 'pwszText'),(1, 'cchText'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSFormatForDisplayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PSFormatForDisplayAlloc", windll["PROPSYS"]), ((1, 'key'),(1, 'propvar'),(1, 'pdff'),(1, 'ppszDisplay'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSFormatPropertyValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head,win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head,win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PSFormatPropertyValue", windll["PROPSYS"]), ((1, 'pps'),(1, 'ppd'),(1, 'pdff'),(1, 'ppszDisplay'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetImageReferenceForValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PSGetImageReferenceForValue", windll["PROPSYS"]), ((1, 'propkey'),(1, 'propvar'),(1, 'ppszImageRes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSStringFromPropertyKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Char),UInt32, use_last_error=False)(("PSStringFromPropertyKey", windll["PROPSYS"]), ((1, 'pkey'),(1, 'psz'),(1, 'cch'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyKeyFromString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(("PSPropertyKeyFromString", windll["PROPSYS"]), ((1, 'pszString'),(1, 'pkey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreateMemoryPropertyStore():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSCreateMemoryPropertyStore", windll["PROPSYS"]), ((1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreateDelayedMultiplexPropertyStore():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,win32more.UI.Shell.PropertiesSystem.IDelayedPropertyStoreFactory_head,POINTER(UInt32),UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSCreateDelayedMultiplexPropertyStore", windll["PROPSYS"]), ((1, 'flags'),(1, 'pdpsf'),(1, 'rgStoreIds'),(1, 'cStores'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreateMultiplexPropertyStore():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head),UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSCreateMultiplexPropertyStore", windll["PROPSYS"]), ((1, 'prgpunkStores'),(1, 'cStores'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreatePropertyChangeArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY),POINTER(win32more.UI.Shell.PropertiesSystem.PKA_FLAGS),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT),UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSCreatePropertyChangeArray", windll["PROPSYS"]), ((1, 'rgpropkey'),(1, 'rgflags'),(1, 'rgpropvar'),(1, 'cChanges'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreateSimplePropertyChange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.PKA_FLAGS,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSCreateSimplePropertyChange", windll["PROPSYS"]), ((1, 'flags'),(1, 'key'),(1, 'propvar'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyDescription():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSGetPropertyDescription", windll["PROPSYS"]), ((1, 'propkey'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyDescriptionByName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSGetPropertyDescriptionByName", windll["PROPSYS"]), ((1, 'pszCanonicalName'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSLookupPropertyHandlerCLSID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(("PSLookupPropertyHandlerCLSID", windll["PROPSYS"]), ((1, 'pszFilePath'),(1, 'pclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetItemPropertyHandler():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSGetItemPropertyHandler", windll["PROPSYS"]), ((1, 'punkItem'),(1, 'fReadWrite'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetItemPropertyHandlerWithCreateObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSGetItemPropertyHandlerWithCreateObject", windll["PROPSYS"]), ((1, 'punkItem'),(1, 'fReadWrite'),(1, 'punkCreateObject'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head,win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("PSGetPropertyValue", windll["PROPSYS"]), ((1, 'pps'),(1, 'ppd'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSSetPropertyValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head,win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("PSSetPropertyValue", windll["PROPSYS"]), ((1, 'pps'),(1, 'ppd'),(1, 'propvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSRegisterPropertySchema():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("PSRegisterPropertySchema", windll["PROPSYS"]), ((1, 'pszPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSUnregisterPropertySchema():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("PSUnregisterPropertySchema", windll["PROPSYS"]), ((1, 'pszPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSRefreshPropertySchema():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("PSRefreshPropertySchema", windll["PROPSYS"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSEnumeratePropertyDescriptions():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSEnumeratePropertyDescriptions", windll["PROPSYS"]), ((1, 'filterOn'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyKeyFromName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(("PSGetPropertyKeyFromName", windll["PROPSYS"]), ((1, 'pszName'),(1, 'ppropkey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetNameFromPropertyKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PSGetNameFromPropertyKey", windll["PROPSYS"]), ((1, 'propkey'),(1, 'ppszCanonicalName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCoerceToCanonicalValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("PSCoerceToCanonicalValue", windll["PROPSYS"]), ((1, 'key'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyDescriptionListFromString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSGetPropertyDescriptionListFromString", windll["PROPSYS"]), ((1, 'pszPropList'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreatePropertyStoreFromPropertySetStorage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertySetStorage_head,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSCreatePropertyStoreFromPropertySetStorage", windll["PROPSYS"]), ((1, 'ppss'),(1, 'grfMode'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreatePropertyStoreFromObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSCreatePropertyStoreFromObject", windll["PROPSYS"]), ((1, 'punk'),(1, 'grfMode'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreateAdapterFromPropertyStore():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSCreateAdapterFromPropertyStore", windll["PROPSYS"]), ((1, 'pps'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertySystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSGetPropertySystem", windll["PROPSYS"]), ((1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyFromPropertyStorage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head),UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("PSGetPropertyFromPropertyStorage", windll["PROPSYS"]), ((1, 'psps'),(1, 'cb'),(1, 'rpkey'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetNamedPropertyFromPropertyStorage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head),UInt32,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("PSGetNamedPropertyFromPropertyStorage", windll["PROPSYS"]), ((1, 'psps'),(1, 'cb'),(1, 'pszName'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head),UInt16, use_last_error=False)(("PSPropertyBag_ReadType", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'var'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Char),Int32, use_last_error=False)(("PSPropertyBag_ReadStr", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),(1, 'characterCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadStrAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PSPropertyBag_ReadStrAlloc", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadBSTR():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("PSPropertyBag_ReadBSTR", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("PSPropertyBag_WriteStr", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteBSTR():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,win32more.Foundation.BSTR, use_last_error=False)(("PSPropertyBag_WriteBSTR", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadInt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Int32), use_last_error=False)(("PSPropertyBag_ReadInt", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteInt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,Int32, use_last_error=False)(("PSPropertyBag_WriteInt", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadSHORT():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Int16), use_last_error=False)(("PSPropertyBag_ReadSHORT", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteSHORT():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,Int16, use_last_error=False)(("PSPropertyBag_WriteSHORT", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadLONG():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Int32), use_last_error=False)(("PSPropertyBag_ReadLONG", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteLONG():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,Int32, use_last_error=False)(("PSPropertyBag_WriteLONG", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadDWORD():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PSPropertyBag_ReadDWORD", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteDWORD():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("PSPropertyBag_WriteDWORD", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadBOOL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("PSPropertyBag_ReadBOOL", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteBOOL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("PSPropertyBag_WriteBOOL", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadPOINTL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.POINTL_head), use_last_error=False)(("PSPropertyBag_ReadPOINTL", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WritePOINTL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.POINTL_head), use_last_error=False)(("PSPropertyBag_WritePOINTL", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadPOINTS():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.POINTS_head), use_last_error=False)(("PSPropertyBag_ReadPOINTS", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WritePOINTS():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.POINTS_head), use_last_error=False)(("PSPropertyBag_WritePOINTS", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadRECTL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.RECTL_head), use_last_error=False)(("PSPropertyBag_ReadRECTL", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteRECTL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.RECTL_head), use_last_error=False)(("PSPropertyBag_WriteRECTL", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(("PSPropertyBag_ReadStream", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head, use_last_error=False)(("PSPropertyBag_WriteStream", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_Delete():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR, use_last_error=False)(("PSPropertyBag_Delete", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadULONGLONG():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(UInt64), use_last_error=False)(("PSPropertyBag_ReadULONGLONG", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteULONGLONG():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,UInt64, use_last_error=False)(("PSPropertyBag_WriteULONGLONG", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadUnknown():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PSPropertyBag_ReadUnknown", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteUnknown():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head, use_last_error=False)(("PSPropertyBag_WriteUnknown", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'punk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadGUID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(("PSPropertyBag_ReadGUID", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteGUID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(("PSPropertyBag_WriteGUID", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadPropertyKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(("PSPropertyBag_ReadPropertyKey", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WritePropertyKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(("PSPropertyBag_WritePropertyKey", windll["PROPSYS"]), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromResource():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromResource", windll["PROPSYS"]), ((1, 'hinst'),(1, 'id'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromBuffer", windll["PROPSYS"]), ((1, 'pv'),(1, 'cb'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromCLSID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromCLSID", windll["PROPSYS"]), ((1, 'clsid'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromGUIDAsString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromGUIDAsString", windll["PROPSYS"]), ((1, 'guid'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromFileTime", windll["PROPSYS"]), ((1, 'pftIn'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromPropVariantVectorElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromPropVariantVectorElem", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'iElem'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantVectorFromPropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantVectorFromPropVariant", windll["PROPSYS"]), ((1, 'propvarSingle'),(1, 'ppropvarVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromStrRet():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.Common.STRRET_head),POINTER(win32more.UI.Shell.Common.ITEMIDLIST_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromStrRet", windll["PROPSYS"]), ((1, 'pstrret'),(1, 'pidl'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromBooleanVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromBooleanVector", windll["PROPSYS"]), ((1, 'prgf'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromInt16Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromInt16Vector", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromUInt16Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromUInt16Vector", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromInt32Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromInt32Vector", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromUInt32Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromUInt32Vector", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromInt64Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromInt64Vector", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromUInt64Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromUInt64Vector", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromDoubleVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromDoubleVector", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromFileTimeVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromFileTimeVector", windll["PROPSYS"]), ((1, 'prgft'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromStringVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromStringVector", windll["PROPSYS"]), ((1, 'prgsz'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromStringAsVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromStringAsVector", windll["PROPSYS"]), ((1, 'psz'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBooleanWithDefault():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.Foundation.BOOL, use_last_error=False)(("PropVariantToBooleanWithDefault", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'fDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt16WithDefault():
    try:
        return WINFUNCTYPE(Int16,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),Int16, use_last_error=False)(("PropVariantToInt16WithDefault", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'iDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt16WithDefault():
    try:
        return WINFUNCTYPE(UInt16,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt16, use_last_error=False)(("PropVariantToUInt16WithDefault", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'uiDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt32WithDefault():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),Int32, use_last_error=False)(("PropVariantToInt32WithDefault", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'lDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt32WithDefault():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32, use_last_error=False)(("PropVariantToUInt32WithDefault", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'ulDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt64WithDefault():
    try:
        return WINFUNCTYPE(Int64,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),Int64, use_last_error=False)(("PropVariantToInt64WithDefault", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'llDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt64WithDefault():
    try:
        return WINFUNCTYPE(UInt64,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt64, use_last_error=False)(("PropVariantToUInt64WithDefault", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'ullDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToDoubleWithDefault():
    try:
        return WINFUNCTYPE(Double,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),Double, use_last_error=False)(("PropVariantToDoubleWithDefault", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'dblDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToStringWithDefault():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.Foundation.PWSTR, use_last_error=False)(("PropVariantToStringWithDefault", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'pszDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBoolean():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(("PropVariantToBoolean", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'pfRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt16():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int16), use_last_error=False)(("PropVariantToInt16", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'piRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt16():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt16), use_last_error=False)(("PropVariantToUInt16", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'puiRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt32():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int32), use_last_error=False)(("PropVariantToInt32", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'plRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt32():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32), use_last_error=False)(("PropVariantToUInt32", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'pulRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int64), use_last_error=False)(("PropVariantToInt64", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'pllRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt64), use_last_error=False)(("PropVariantToUInt64", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'pullRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToDouble():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Double), use_last_error=False)(("PropVariantToDouble", windll["PROPSYS"]), ((1, 'propvarIn'),(1, 'pdblRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),c_void_p,UInt32, use_last_error=False)(("PropVariantToBuffer", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pv'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Char),UInt32, use_last_error=False)(("PropVariantToString", windll["PROPSYS"]), ((1, 'propvar'),(1, 'psz'),(1, 'cch'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToGUID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Guid), use_last_error=False)(("PropVariantToGUID", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pguid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToStringAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PropVariantToStringAlloc", windll["PROPSYS"]), ((1, 'propvar'),(1, 'ppszOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBSTR():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.BSTR), use_last_error=False)(("PropVariantToBSTR", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToStrRet():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.UI.Shell.Common.STRRET_head), use_last_error=False)(("PropVariantToStrRet", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pstrret'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PSTIME_FLAGS,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("PropVariantToFileTime", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pstfOut'),(1, 'pftOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetElementCount():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("PropVariantGetElementCount", windll["PROPSYS"]), ((1, 'propvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBooleanVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.BOOL),UInt32,POINTER(UInt32), use_last_error=False)(("PropVariantToBooleanVector", windll["PROPSYS"]), ((1, 'propvar'),(1, 'prgf'),(1, 'crgf'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt16Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int16),UInt32,POINTER(UInt32), use_last_error=False)(("PropVariantToInt16Vector", windll["PROPSYS"]), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt16Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt16),UInt32,POINTER(UInt32), use_last_error=False)(("PropVariantToUInt16Vector", windll["PROPSYS"]), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt32Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int32),UInt32,POINTER(UInt32), use_last_error=False)(("PropVariantToInt32Vector", windll["PROPSYS"]), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt32Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32),UInt32,POINTER(UInt32), use_last_error=False)(("PropVariantToUInt32Vector", windll["PROPSYS"]), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt64Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int64),UInt32,POINTER(UInt32), use_last_error=False)(("PropVariantToInt64Vector", windll["PROPSYS"]), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt64Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt64),UInt32,POINTER(UInt32), use_last_error=False)(("PropVariantToUInt64Vector", windll["PROPSYS"]), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToDoubleVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Double),UInt32,POINTER(UInt32), use_last_error=False)(("PropVariantToDoubleVector", windll["PROPSYS"]), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToFileTimeVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.FILETIME),UInt32,POINTER(UInt32), use_last_error=False)(("PropVariantToFileTimeVector", windll["PROPSYS"]), ((1, 'propvar'),(1, 'prgft'),(1, 'crgft'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToStringVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(UInt32), use_last_error=False)(("PropVariantToStringVector", windll["PROPSYS"]), ((1, 'propvar'),(1, 'prgsz'),(1, 'crgsz'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBooleanVectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(win32more.Foundation.BOOL)),POINTER(UInt32), use_last_error=False)(("PropVariantToBooleanVectorAlloc", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pprgf'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt16VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(Int16)),POINTER(UInt32), use_last_error=False)(("PropVariantToInt16VectorAlloc", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt16VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(UInt16)),POINTER(UInt32), use_last_error=False)(("PropVariantToUInt16VectorAlloc", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt32VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(Int32)),POINTER(UInt32), use_last_error=False)(("PropVariantToInt32VectorAlloc", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt32VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(UInt32)),POINTER(UInt32), use_last_error=False)(("PropVariantToUInt32VectorAlloc", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt64VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(Int64)),POINTER(UInt32), use_last_error=False)(("PropVariantToInt64VectorAlloc", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt64VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(UInt64)),POINTER(UInt32), use_last_error=False)(("PropVariantToUInt64VectorAlloc", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToDoubleVectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(Double)),POINTER(UInt32), use_last_error=False)(("PropVariantToDoubleVectorAlloc", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToFileTimeVectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(win32more.Foundation.FILETIME_head)),POINTER(UInt32), use_last_error=False)(("PropVariantToFileTimeVectorAlloc", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pprgft'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToStringVectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32), use_last_error=False)(("PropVariantToStringVectorAlloc", windll["PROPSYS"]), ((1, 'propvar'),(1, 'pprgsz'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetBooleanElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("PropVariantGetBooleanElem", windll["PROPSYS"]), ((1, 'propvar'),(1, 'iElem'),(1, 'pfVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetInt16Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(Int16), use_last_error=False)(("PropVariantGetInt16Elem", windll["PROPSYS"]), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetUInt16Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(UInt16), use_last_error=False)(("PropVariantGetUInt16Elem", windll["PROPSYS"]), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetInt32Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(Int32), use_last_error=False)(("PropVariantGetInt32Elem", windll["PROPSYS"]), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetUInt32Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(UInt32), use_last_error=False)(("PropVariantGetUInt32Elem", windll["PROPSYS"]), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetInt64Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(Int64), use_last_error=False)(("PropVariantGetInt64Elem", windll["PROPSYS"]), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetUInt64Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(UInt64), use_last_error=False)(("PropVariantGetUInt64Elem", windll["PROPSYS"]), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetDoubleElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(Double), use_last_error=False)(("PropVariantGetDoubleElem", windll["PROPSYS"]), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetFileTimeElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("PropVariantGetFileTimeElem", windll["PROPSYS"]), ((1, 'propvar'),(1, 'iElem'),(1, 'pftVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetStringElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PropVariantGetStringElem", windll["PROPSYS"]), ((1, 'propvar'),(1, 'iElem'),(1, 'ppszVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClearPropVariantArray():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT),UInt32, use_last_error=False)(("ClearPropVariantArray", windll["PROPSYS"]), ((1, 'rgPropVar'),(1, 'cVars'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantCompareEx():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPVAR_COMPARE_UNIT,win32more.UI.Shell.PropertiesSystem.PROPVAR_COMPARE_FLAGS, use_last_error=False)(("PropVariantCompareEx", windll["PROPSYS"]), ((1, 'propvar1'),(1, 'propvar2'),(1, 'unit'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantChangeType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPVAR_CHANGE_FLAGS,UInt16, use_last_error=False)(("PropVariantChangeType", windll["PROPSYS"]), ((1, 'ppropvarDest'),(1, 'propvarSrc'),(1, 'flags'),(1, 'vt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("PropVariantToVariant", windll["PROPSYS"]), ((1, 'pPropVar'),(1, 'pVar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToPropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("VariantToPropVariant", windll["PROPSYS"]), ((1, 'pVar'),(1, 'pPropVar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromResource():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromResource", windll["PROPSYS"]), ((1, 'hinst'),(1, 'id'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromBuffer", windll["PROPSYS"]), ((1, 'pv'),(1, 'cb'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromGUIDAsString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromGUIDAsString", windll["PROPSYS"]), ((1, 'guid'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromFileTime", windll["PROPSYS"]), ((1, 'pft'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromFileTimeArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromFileTimeArray", windll["PROPSYS"]), ((1, 'prgft'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromStrRet():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.Common.STRRET_head),POINTER(win32more.UI.Shell.Common.ITEMIDLIST_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromStrRet", windll["PROPSYS"]), ((1, 'pstrret'),(1, 'pidl'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromVariantArrayElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromVariantArrayElem", windll["PROPSYS"]), ((1, 'varIn'),(1, 'iElem'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromBooleanArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromBooleanArray", windll["PROPSYS"]), ((1, 'prgf'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromInt16Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromInt16Array", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromUInt16Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromUInt16Array", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromInt32Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromInt32Array", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromUInt32Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromUInt32Array", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromInt64Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromInt64Array", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromUInt64Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromUInt64Array", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromDoubleArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromDoubleArray", windll["PROPSYS"]), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromStringArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("InitVariantFromStringArray", windll["PROPSYS"]), ((1, 'prgsz'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToBooleanWithDefault():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BOOL, use_last_error=False)(("VariantToBooleanWithDefault", windll["PROPSYS"]), ((1, 'varIn'),(1, 'fDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt16WithDefault():
    try:
        return WINFUNCTYPE(Int16,POINTER(win32more.System.Com.VARIANT_head),Int16, use_last_error=False)(("VariantToInt16WithDefault", windll["PROPSYS"]), ((1, 'varIn'),(1, 'iDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt16WithDefault():
    try:
        return WINFUNCTYPE(UInt16,POINTER(win32more.System.Com.VARIANT_head),UInt16, use_last_error=False)(("VariantToUInt16WithDefault", windll["PROPSYS"]), ((1, 'varIn'),(1, 'uiDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt32WithDefault():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Com.VARIANT_head),Int32, use_last_error=False)(("VariantToInt32WithDefault", windll["PROPSYS"]), ((1, 'varIn'),(1, 'lDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt32WithDefault():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Com.VARIANT_head),UInt32, use_last_error=False)(("VariantToUInt32WithDefault", windll["PROPSYS"]), ((1, 'varIn'),(1, 'ulDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt64WithDefault():
    try:
        return WINFUNCTYPE(Int64,POINTER(win32more.System.Com.VARIANT_head),Int64, use_last_error=False)(("VariantToInt64WithDefault", windll["PROPSYS"]), ((1, 'varIn'),(1, 'llDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt64WithDefault():
    try:
        return WINFUNCTYPE(UInt64,POINTER(win32more.System.Com.VARIANT_head),UInt64, use_last_error=False)(("VariantToUInt64WithDefault", windll["PROPSYS"]), ((1, 'varIn'),(1, 'ullDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToDoubleWithDefault():
    try:
        return WINFUNCTYPE(Double,POINTER(win32more.System.Com.VARIANT_head),Double, use_last_error=False)(("VariantToDoubleWithDefault", windll["PROPSYS"]), ((1, 'varIn'),(1, 'dblDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToStringWithDefault():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.PWSTR, use_last_error=False)(("VariantToStringWithDefault", windll["PROPSYS"]), ((1, 'varIn'),(1, 'pszDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToBoolean():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(("VariantToBoolean", windll["PROPSYS"]), ((1, 'varIn'),(1, 'pfRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt16():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int16), use_last_error=False)(("VariantToInt16", windll["PROPSYS"]), ((1, 'varIn'),(1, 'piRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt16():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt16), use_last_error=False)(("VariantToUInt16", windll["PROPSYS"]), ((1, 'varIn'),(1, 'puiRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt32():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32), use_last_error=False)(("VariantToInt32", windll["PROPSYS"]), ((1, 'varIn'),(1, 'plRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt32():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt32), use_last_error=False)(("VariantToUInt32", windll["PROPSYS"]), ((1, 'varIn'),(1, 'pulRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int64), use_last_error=False)(("VariantToInt64", windll["PROPSYS"]), ((1, 'varIn'),(1, 'pllRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt64), use_last_error=False)(("VariantToUInt64", windll["PROPSYS"]), ((1, 'varIn'),(1, 'pullRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToDouble():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Double), use_last_error=False)(("VariantToDouble", windll["PROPSYS"]), ((1, 'varIn'),(1, 'pdblRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),c_void_p,UInt32, use_last_error=False)(("VariantToBuffer", windll["PROPSYS"]), ((1, 'varIn'),(1, 'pv'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToGUID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Guid), use_last_error=False)(("VariantToGUID", windll["PROPSYS"]), ((1, 'varIn'),(1, 'pguid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Char),UInt32, use_last_error=False)(("VariantToString", windll["PROPSYS"]), ((1, 'varIn'),(1, 'pszBuf'),(1, 'cchBuf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToStringAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("VariantToStringAlloc", windll["PROPSYS"]), ((1, 'varIn'),(1, 'ppszBuf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToDosDateTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt16),POINTER(UInt16), use_last_error=False)(("VariantToDosDateTime", windll["PROPSYS"]), ((1, 'varIn'),(1, 'pwDate'),(1, 'pwTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToStrRet():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.UI.Shell.Common.STRRET_head), use_last_error=False)(("VariantToStrRet", windll["PROPSYS"]), ((1, 'varIn'),(1, 'pstrret'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),win32more.UI.Shell.PropertiesSystem.PSTIME_FLAGS,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("VariantToFileTime", windll["PROPSYS"]), ((1, 'varIn'),(1, 'stfOut'),(1, 'pftOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetElementCount():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VariantGetElementCount", windll["PROPSYS"]), ((1, 'varIn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToBooleanArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.BOOL),UInt32,POINTER(UInt32), use_last_error=False)(("VariantToBooleanArray", windll["PROPSYS"]), ((1, 'var'),(1, 'prgf'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt16Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int16),UInt32,POINTER(UInt32), use_last_error=False)(("VariantToInt16Array", windll["PROPSYS"]), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt16Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt16),UInt32,POINTER(UInt32), use_last_error=False)(("VariantToUInt16Array", windll["PROPSYS"]), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt32Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32),UInt32,POINTER(UInt32), use_last_error=False)(("VariantToInt32Array", windll["PROPSYS"]), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt32Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt32),UInt32,POINTER(UInt32), use_last_error=False)(("VariantToUInt32Array", windll["PROPSYS"]), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt64Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int64),UInt32,POINTER(UInt32), use_last_error=False)(("VariantToInt64Array", windll["PROPSYS"]), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt64Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt64),UInt32,POINTER(UInt32), use_last_error=False)(("VariantToUInt64Array", windll["PROPSYS"]), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToDoubleArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Double),UInt32,POINTER(UInt32), use_last_error=False)(("VariantToDoubleArray", windll["PROPSYS"]), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToStringArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(UInt32), use_last_error=False)(("VariantToStringArray", windll["PROPSYS"]), ((1, 'var'),(1, 'prgsz'),(1, 'crgsz'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToBooleanArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(win32more.Foundation.BOOL)),POINTER(UInt32), use_last_error=False)(("VariantToBooleanArrayAlloc", windll["PROPSYS"]), ((1, 'var'),(1, 'pprgf'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt16ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(Int16)),POINTER(UInt32), use_last_error=False)(("VariantToInt16ArrayAlloc", windll["PROPSYS"]), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt16ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(UInt16)),POINTER(UInt32), use_last_error=False)(("VariantToUInt16ArrayAlloc", windll["PROPSYS"]), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt32ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(Int32)),POINTER(UInt32), use_last_error=False)(("VariantToInt32ArrayAlloc", windll["PROPSYS"]), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt32ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(UInt32)),POINTER(UInt32), use_last_error=False)(("VariantToUInt32ArrayAlloc", windll["PROPSYS"]), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt64ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(Int64)),POINTER(UInt32), use_last_error=False)(("VariantToInt64ArrayAlloc", windll["PROPSYS"]), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt64ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(UInt64)),POINTER(UInt32), use_last_error=False)(("VariantToUInt64ArrayAlloc", windll["PROPSYS"]), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToDoubleArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(Double)),POINTER(UInt32), use_last_error=False)(("VariantToDoubleArrayAlloc", windll["PROPSYS"]), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToStringArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32), use_last_error=False)(("VariantToStringArrayAlloc", windll["PROPSYS"]), ((1, 'var'),(1, 'pprgsz'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetBooleanElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("VariantGetBooleanElem", windll["PROPSYS"]), ((1, 'var'),(1, 'iElem'),(1, 'pfVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetInt16Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(Int16), use_last_error=False)(("VariantGetInt16Elem", windll["PROPSYS"]), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetUInt16Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(UInt16), use_last_error=False)(("VariantGetUInt16Elem", windll["PROPSYS"]), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetInt32Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(Int32), use_last_error=False)(("VariantGetInt32Elem", windll["PROPSYS"]), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetUInt32Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(UInt32), use_last_error=False)(("VariantGetUInt32Elem", windll["PROPSYS"]), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetInt64Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(Int64), use_last_error=False)(("VariantGetInt64Elem", windll["PROPSYS"]), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetUInt64Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(UInt64), use_last_error=False)(("VariantGetUInt64Elem", windll["PROPSYS"]), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetDoubleElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(Double), use_last_error=False)(("VariantGetDoubleElem", windll["PROPSYS"]), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetStringElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("VariantGetStringElem", windll["PROPSYS"]), ((1, 'var'),(1, 'iElem'),(1, 'ppszVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClearVariantArray():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Com.VARIANT),UInt32, use_last_error=False)(("ClearVariantArray", windll["PROPSYS"]), ((1, 'pvars'),(1, 'cvars'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantCompare():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VariantCompare", windll["PROPSYS"]), ((1, 'var1'),(1, 'var2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHGetPropertyStoreFromIDList():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.Common.ITEMIDLIST_head),win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("SHGetPropertyStoreFromIDList", windll["SHELL32"]), ((1, 'pidl'),(1, 'flags'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHGetPropertyStoreFromParsingName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IBindCtx_head,win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("SHGetPropertyStoreFromParsingName", windll["SHELL32"]), ((1, 'pszPath'),(1, 'pbc'),(1, 'flags'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHAddDefaultPropertiesByExt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, use_last_error=False)(("SHAddDefaultPropertiesByExt", windll["SHELL32"]), ((1, 'pszExt'),(1, 'pPropStore'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PifMgr_OpenProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32, use_last_error=False)(("PifMgr_OpenProperties", windll["SHELL32"]), ((1, 'pszApp'),(1, 'pszPIF'),(1, 'hInf'),(1, 'flOpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PifMgr_GetProperties():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,c_void_p,Int32,UInt32, use_last_error=False)(("PifMgr_GetProperties", windll["SHELL32"]), ((1, 'hProps'),(1, 'pszGroup'),(1, 'lpProps'),(1, 'cbProps'),(1, 'flOpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PifMgr_SetProperties():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,c_void_p,Int32,UInt32, use_last_error=False)(("PifMgr_SetProperties", windll["SHELL32"]), ((1, 'hProps'),(1, 'pszGroup'),(1, 'lpProps'),(1, 'cbProps'),(1, 'flOpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PifMgr_CloseProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("PifMgr_CloseProperties", windll["SHELL32"]), ((1, 'hProps'),(1, 'flOpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHPropStgCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertySetStorage_head,POINTER(Guid),POINTER(Guid),UInt32,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head),POINTER(UInt32), use_last_error=False)(("SHPropStgCreate", windll["SHELL32"]), ((1, 'psstg'),(1, 'fmtid'),(1, 'pclsid'),(1, 'grfFlags'),(1, 'grfMode'),(1, 'dwDisposition'),(1, 'ppstg'),(1, 'puCodePage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHPropStgReadMultiple():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyStorage_head,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPSPEC),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("SHPropStgReadMultiple", windll["SHELL32"]), ((1, 'pps'),(1, 'uCodePage'),(1, 'cpspec'),(1, 'rgpspec'),(1, 'rgvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHPropStgWriteMultiple():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyStorage_head,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPSPEC),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT),UInt32, use_last_error=False)(("SHPropStgWriteMultiple", windll["SHELL32"]), ((1, 'pps'),(1, 'puCodePage'),(1, 'cpspec'),(1, 'rgpspec'),(1, 'rgvar'),(1, 'propidNameFirst'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHGetPropertyStoreForWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("SHGetPropertyStoreForWindow", windll["SHELL32"]), ((1, 'hwnd'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "PKEY_PIDSTR_MAX",
    "PROPERTYKEY",
    "InMemoryPropertyStore",
    "InMemoryPropertyStoreMarshalByValue",
    "PropertySystem",
    "IInitializeWithFile",
    "IInitializeWithStream",
    "IPropertyStore",
    "INamedPropertyStore",
    "GETPROPERTYSTOREFLAGS",
    "GPS_DEFAULT",
    "GPS_HANDLERPROPERTIESONLY",
    "GPS_READWRITE",
    "GPS_TEMPORARY",
    "GPS_FASTPROPERTIESONLY",
    "GPS_OPENSLOWITEM",
    "GPS_DELAYCREATION",
    "GPS_BESTEFFORT",
    "GPS_NO_OPLOCK",
    "GPS_PREFERQUERYPROPERTIES",
    "GPS_EXTRINSICPROPERTIES",
    "GPS_EXTRINSICPROPERTIESONLY",
    "GPS_VOLATILEPROPERTIES",
    "GPS_VOLATILEPROPERTIESONLY",
    "GPS_MASK_VALID",
    "IObjectWithPropertyKey",
    "PKA_FLAGS",
    "PKA_SET",
    "PKA_APPEND",
    "PKA_DELETE",
    "IPropertyChange",
    "IPropertyChangeArray",
    "IPropertyStoreCapabilities",
    "PSC_STATE",
    "PSC_NORMAL",
    "PSC_NOTINSOURCE",
    "PSC_DIRTY",
    "PSC_READONLY",
    "IPropertyStoreCache",
    "PROPENUMTYPE",
    "PET_DISCRETEVALUE",
    "PET_RANGEDVALUE",
    "PET_DEFAULTVALUE",
    "PET_ENDRANGE",
    "IPropertyEnumType",
    "IPropertyEnumType2",
    "IPropertyEnumTypeList",
    "PROPDESC_TYPE_FLAGS",
    "PDTF_DEFAULT",
    "PDTF_MULTIPLEVALUES",
    "PDTF_ISINNATE",
    "PDTF_ISGROUP",
    "PDTF_CANGROUPBY",
    "PDTF_CANSTACKBY",
    "PDTF_ISTREEPROPERTY",
    "PDTF_INCLUDEINFULLTEXTQUERY",
    "PDTF_ISVIEWABLE",
    "PDTF_ISQUERYABLE",
    "PDTF_CANBEPURGED",
    "PDTF_SEARCHRAWVALUE",
    "PDTF_DONTCOERCEEMPTYSTRINGS",
    "PDTF_ALWAYSINSUPPLEMENTALSTORE",
    "PDTF_ISSYSTEMPROPERTY",
    "PDTF_MASK_ALL",
    "PROPDESC_VIEW_FLAGS",
    "PDVF_DEFAULT",
    "PDVF_CENTERALIGN",
    "PDVF_RIGHTALIGN",
    "PDVF_BEGINNEWGROUP",
    "PDVF_FILLAREA",
    "PDVF_SORTDESCENDING",
    "PDVF_SHOWONLYIFPRESENT",
    "PDVF_SHOWBYDEFAULT",
    "PDVF_SHOWINPRIMARYLIST",
    "PDVF_SHOWINSECONDARYLIST",
    "PDVF_HIDELABEL",
    "PDVF_HIDDEN",
    "PDVF_CANWRAP",
    "PDVF_MASK_ALL",
    "PROPDESC_DISPLAYTYPE",
    "PDDT_STRING",
    "PDDT_NUMBER",
    "PDDT_BOOLEAN",
    "PDDT_DATETIME",
    "PDDT_ENUMERATED",
    "PROPDESC_GROUPING_RANGE",
    "PDGR_DISCRETE",
    "PDGR_ALPHANUMERIC",
    "PDGR_SIZE",
    "PDGR_DYNAMIC",
    "PDGR_DATE",
    "PDGR_PERCENT",
    "PDGR_ENUMERATED",
    "PROPDESC_FORMAT_FLAGS",
    "PDFF_DEFAULT",
    "PDFF_PREFIXNAME",
    "PDFF_FILENAME",
    "PDFF_ALWAYSKB",
    "PDFF_RESERVED_RIGHTTOLEFT",
    "PDFF_SHORTTIME",
    "PDFF_LONGTIME",
    "PDFF_HIDETIME",
    "PDFF_SHORTDATE",
    "PDFF_LONGDATE",
    "PDFF_HIDEDATE",
    "PDFF_RELATIVEDATE",
    "PDFF_USEEDITINVITATION",
    "PDFF_READONLY",
    "PDFF_NOAUTOREADINGORDER",
    "PROPDESC_SORTDESCRIPTION",
    "PDSD_GENERAL",
    "PDSD_A_Z",
    "PDSD_LOWEST_HIGHEST",
    "PDSD_SMALLEST_BIGGEST",
    "PDSD_OLDEST_NEWEST",
    "PROPDESC_RELATIVEDESCRIPTION_TYPE",
    "PDRDT_GENERAL",
    "PDRDT_DATE",
    "PDRDT_SIZE",
    "PDRDT_COUNT",
    "PDRDT_REVISION",
    "PDRDT_LENGTH",
    "PDRDT_DURATION",
    "PDRDT_SPEED",
    "PDRDT_RATE",
    "PDRDT_RATING",
    "PDRDT_PRIORITY",
    "PROPDESC_AGGREGATION_TYPE",
    "PDAT_DEFAULT",
    "PDAT_FIRST",
    "PDAT_SUM",
    "PDAT_AVERAGE",
    "PDAT_DATERANGE",
    "PDAT_UNION",
    "PDAT_MAX",
    "PDAT_MIN",
    "PROPDESC_CONDITION_TYPE",
    "PDCOT_NONE",
    "PDCOT_STRING",
    "PDCOT_SIZE",
    "PDCOT_DATETIME",
    "PDCOT_BOOLEAN",
    "PDCOT_NUMBER",
    "IPropertyDescription",
    "IPropertyDescription2",
    "IPropertyDescriptionAliasInfo",
    "PROPDESC_SEARCHINFO_FLAGS",
    "PDSIF_DEFAULT",
    "PDSIF_ININVERTEDINDEX",
    "PDSIF_ISCOLUMN",
    "PDSIF_ISCOLUMNSPARSE",
    "PDSIF_ALWAYSINCLUDE",
    "PDSIF_USEFORTYPEAHEAD",
    "PROPDESC_COLUMNINDEX_TYPE",
    "PDCIT_NONE",
    "PDCIT_ONDISK",
    "PDCIT_INMEMORY",
    "PDCIT_ONDEMAND",
    "PDCIT_ONDISKALL",
    "PDCIT_ONDISKVECTOR",
    "IPropertyDescriptionSearchInfo",
    "IPropertyDescriptionRelatedPropertyInfo",
    "PROPDESC_ENUMFILTER",
    "PDEF_ALL",
    "PDEF_SYSTEM",
    "PDEF_NONSYSTEM",
    "PDEF_VIEWABLE",
    "PDEF_QUERYABLE",
    "PDEF_INFULLTEXTQUERY",
    "PDEF_COLUMN",
    "IPropertySystem",
    "IPropertyDescriptionList",
    "IPropertyStoreFactory",
    "IDelayedPropertyStoreFactory",
    "_PERSIST_SPROPSTORE_FLAGS",
    "FPSPS_DEFAULT",
    "FPSPS_READONLY",
    "FPSPS_TREAT_NEW_VALUES_AS_DIRTY",
    "SERIALIZEDPROPSTORAGE",
    "IPersistSerializedPropStorage",
    "IPersistSerializedPropStorage2",
    "IPropertySystemChangeNotify",
    "ICreateObject",
    "PSTIME_FLAGS",
    "PSTF_UTC",
    "PSTF_LOCAL",
    "PROPVAR_COMPARE_UNIT",
    "PVCU_DEFAULT",
    "PVCU_SECOND",
    "PVCU_MINUTE",
    "PVCU_HOUR",
    "PVCU_DAY",
    "PVCU_MONTH",
    "PVCU_YEAR",
    "PROPVAR_COMPARE_FLAGS",
    "PVCF_DEFAULT",
    "PVCF_TREATEMPTYASGREATERTHAN",
    "PVCF_USESTRCMP",
    "PVCF_USESTRCMPC",
    "PVCF_USESTRCMPI",
    "PVCF_USESTRCMPIC",
    "PVCF_DIGITSASNUMBERS_CASESENSITIVE",
    "PROPVAR_CHANGE_FLAGS",
    "PVCHF_DEFAULT",
    "PVCHF_NOVALUEPROP",
    "PVCHF_ALPHABOOL",
    "PVCHF_NOUSEROVERRIDE",
    "PVCHF_LOCALBOOL",
    "PVCHF_NOHEXSTRING",
    "DRAWPROGRESSFLAGS",
    "DPF_NONE",
    "DPF_MARQUEE",
    "DPF_MARQUEE_COMPLETE",
    "DPF_ERROR",
    "DPF_WARNING",
    "DPF_STOPPED",
    "SYNC_TRANSFER_STATUS",
    "STS_NONE",
    "STS_NEEDSUPLOAD",
    "STS_NEEDSDOWNLOAD",
    "STS_TRANSFERRING",
    "STS_PAUSED",
    "STS_HASERROR",
    "STS_FETCHING_METADATA",
    "STS_USER_REQUESTED_REFRESH",
    "STS_HASWARNING",
    "STS_EXCLUDED",
    "STS_INCOMPLETE",
    "STS_PLACEHOLDER_IFEMPTY",
    "PLACEHOLDER_STATES",
    "PS_NONE",
    "PS_MARKED_FOR_OFFLINE_AVAILABILITY",
    "PS_FULL_PRIMARY_STREAM_AVAILABLE",
    "PS_CREATE_FILE_ACCESSIBLE",
    "PS_CLOUDFILE_PLACEHOLDER",
    "PS_DEFAULT",
    "PS_ALL",
    "PROPERTYUI_NAME_FLAGS",
    "PUIFNF_DEFAULT",
    "PUIFNF_MNEMONIC",
    "PROPERTYUI_FLAGS",
    "PUIF_DEFAULT",
    "PUIF_RIGHTALIGN",
    "PUIF_NOLABELININFOTIP",
    "PROPERTYUI_FORMAT_FLAGS",
    "PUIFFDF_DEFAULT",
    "PUIFFDF_RIGHTTOLEFT",
    "PUIFFDF_SHORTFORMAT",
    "PUIFFDF_NOTIME",
    "PUIFFDF_FRIENDLYDATE",
    "IPropertyUI",
    "PDOPSTATUS",
    "PDOPS_RUNNING",
    "PDOPS_PAUSED",
    "PDOPS_CANCELLED",
    "PDOPS_STOPPED",
    "PDOPS_ERRORS",
    "SYNC_ENGINE_STATE_FLAGS",
    "SESF_NONE",
    "SESF_SERVICE_QUOTA_NEARING_LIMIT",
    "SESF_SERVICE_QUOTA_EXCEEDED_LIMIT",
    "SESF_AUTHENTICATION_ERROR",
    "SESF_PAUSED_DUE_TO_METERED_NETWORK",
    "SESF_PAUSED_DUE_TO_DISK_SPACE_FULL",
    "SESF_PAUSED_DUE_TO_CLIENT_POLICY",
    "SESF_PAUSED_DUE_TO_SERVICE_POLICY",
    "SESF_SERVICE_UNAVAILABLE",
    "SESF_PAUSED_DUE_TO_USER_REQUEST",
    "SESF_ALL_FLAGS",
    "PROPPRG",
    "PropVariantToWinRTPropertyValue",
    "WinRTPropertyValueToPropVariant",
    "PSFormatForDisplay",
    "PSFormatForDisplayAlloc",
    "PSFormatPropertyValue",
    "PSGetImageReferenceForValue",
    "PSStringFromPropertyKey",
    "PSPropertyKeyFromString",
    "PSCreateMemoryPropertyStore",
    "PSCreateDelayedMultiplexPropertyStore",
    "PSCreateMultiplexPropertyStore",
    "PSCreatePropertyChangeArray",
    "PSCreateSimplePropertyChange",
    "PSGetPropertyDescription",
    "PSGetPropertyDescriptionByName",
    "PSLookupPropertyHandlerCLSID",
    "PSGetItemPropertyHandler",
    "PSGetItemPropertyHandlerWithCreateObject",
    "PSGetPropertyValue",
    "PSSetPropertyValue",
    "PSRegisterPropertySchema",
    "PSUnregisterPropertySchema",
    "PSRefreshPropertySchema",
    "PSEnumeratePropertyDescriptions",
    "PSGetPropertyKeyFromName",
    "PSGetNameFromPropertyKey",
    "PSCoerceToCanonicalValue",
    "PSGetPropertyDescriptionListFromString",
    "PSCreatePropertyStoreFromPropertySetStorage",
    "PSCreatePropertyStoreFromObject",
    "PSCreateAdapterFromPropertyStore",
    "PSGetPropertySystem",
    "PSGetPropertyFromPropertyStorage",
    "PSGetNamedPropertyFromPropertyStorage",
    "PSPropertyBag_ReadType",
    "PSPropertyBag_ReadStr",
    "PSPropertyBag_ReadStrAlloc",
    "PSPropertyBag_ReadBSTR",
    "PSPropertyBag_WriteStr",
    "PSPropertyBag_WriteBSTR",
    "PSPropertyBag_ReadInt",
    "PSPropertyBag_WriteInt",
    "PSPropertyBag_ReadSHORT",
    "PSPropertyBag_WriteSHORT",
    "PSPropertyBag_ReadLONG",
    "PSPropertyBag_WriteLONG",
    "PSPropertyBag_ReadDWORD",
    "PSPropertyBag_WriteDWORD",
    "PSPropertyBag_ReadBOOL",
    "PSPropertyBag_WriteBOOL",
    "PSPropertyBag_ReadPOINTL",
    "PSPropertyBag_WritePOINTL",
    "PSPropertyBag_ReadPOINTS",
    "PSPropertyBag_WritePOINTS",
    "PSPropertyBag_ReadRECTL",
    "PSPropertyBag_WriteRECTL",
    "PSPropertyBag_ReadStream",
    "PSPropertyBag_WriteStream",
    "PSPropertyBag_Delete",
    "PSPropertyBag_ReadULONGLONG",
    "PSPropertyBag_WriteULONGLONG",
    "PSPropertyBag_ReadUnknown",
    "PSPropertyBag_WriteUnknown",
    "PSPropertyBag_ReadGUID",
    "PSPropertyBag_WriteGUID",
    "PSPropertyBag_ReadPropertyKey",
    "PSPropertyBag_WritePropertyKey",
    "InitPropVariantFromResource",
    "InitPropVariantFromBuffer",
    "InitPropVariantFromCLSID",
    "InitPropVariantFromGUIDAsString",
    "InitPropVariantFromFileTime",
    "InitPropVariantFromPropVariantVectorElem",
    "InitPropVariantVectorFromPropVariant",
    "InitPropVariantFromStrRet",
    "InitPropVariantFromBooleanVector",
    "InitPropVariantFromInt16Vector",
    "InitPropVariantFromUInt16Vector",
    "InitPropVariantFromInt32Vector",
    "InitPropVariantFromUInt32Vector",
    "InitPropVariantFromInt64Vector",
    "InitPropVariantFromUInt64Vector",
    "InitPropVariantFromDoubleVector",
    "InitPropVariantFromFileTimeVector",
    "InitPropVariantFromStringVector",
    "InitPropVariantFromStringAsVector",
    "PropVariantToBooleanWithDefault",
    "PropVariantToInt16WithDefault",
    "PropVariantToUInt16WithDefault",
    "PropVariantToInt32WithDefault",
    "PropVariantToUInt32WithDefault",
    "PropVariantToInt64WithDefault",
    "PropVariantToUInt64WithDefault",
    "PropVariantToDoubleWithDefault",
    "PropVariantToStringWithDefault",
    "PropVariantToBoolean",
    "PropVariantToInt16",
    "PropVariantToUInt16",
    "PropVariantToInt32",
    "PropVariantToUInt32",
    "PropVariantToInt64",
    "PropVariantToUInt64",
    "PropVariantToDouble",
    "PropVariantToBuffer",
    "PropVariantToString",
    "PropVariantToGUID",
    "PropVariantToStringAlloc",
    "PropVariantToBSTR",
    "PropVariantToStrRet",
    "PropVariantToFileTime",
    "PropVariantGetElementCount",
    "PropVariantToBooleanVector",
    "PropVariantToInt16Vector",
    "PropVariantToUInt16Vector",
    "PropVariantToInt32Vector",
    "PropVariantToUInt32Vector",
    "PropVariantToInt64Vector",
    "PropVariantToUInt64Vector",
    "PropVariantToDoubleVector",
    "PropVariantToFileTimeVector",
    "PropVariantToStringVector",
    "PropVariantToBooleanVectorAlloc",
    "PropVariantToInt16VectorAlloc",
    "PropVariantToUInt16VectorAlloc",
    "PropVariantToInt32VectorAlloc",
    "PropVariantToUInt32VectorAlloc",
    "PropVariantToInt64VectorAlloc",
    "PropVariantToUInt64VectorAlloc",
    "PropVariantToDoubleVectorAlloc",
    "PropVariantToFileTimeVectorAlloc",
    "PropVariantToStringVectorAlloc",
    "PropVariantGetBooleanElem",
    "PropVariantGetInt16Elem",
    "PropVariantGetUInt16Elem",
    "PropVariantGetInt32Elem",
    "PropVariantGetUInt32Elem",
    "PropVariantGetInt64Elem",
    "PropVariantGetUInt64Elem",
    "PropVariantGetDoubleElem",
    "PropVariantGetFileTimeElem",
    "PropVariantGetStringElem",
    "ClearPropVariantArray",
    "PropVariantCompareEx",
    "PropVariantChangeType",
    "PropVariantToVariant",
    "VariantToPropVariant",
    "InitVariantFromResource",
    "InitVariantFromBuffer",
    "InitVariantFromGUIDAsString",
    "InitVariantFromFileTime",
    "InitVariantFromFileTimeArray",
    "InitVariantFromStrRet",
    "InitVariantFromVariantArrayElem",
    "InitVariantFromBooleanArray",
    "InitVariantFromInt16Array",
    "InitVariantFromUInt16Array",
    "InitVariantFromInt32Array",
    "InitVariantFromUInt32Array",
    "InitVariantFromInt64Array",
    "InitVariantFromUInt64Array",
    "InitVariantFromDoubleArray",
    "InitVariantFromStringArray",
    "VariantToBooleanWithDefault",
    "VariantToInt16WithDefault",
    "VariantToUInt16WithDefault",
    "VariantToInt32WithDefault",
    "VariantToUInt32WithDefault",
    "VariantToInt64WithDefault",
    "VariantToUInt64WithDefault",
    "VariantToDoubleWithDefault",
    "VariantToStringWithDefault",
    "VariantToBoolean",
    "VariantToInt16",
    "VariantToUInt16",
    "VariantToInt32",
    "VariantToUInt32",
    "VariantToInt64",
    "VariantToUInt64",
    "VariantToDouble",
    "VariantToBuffer",
    "VariantToGUID",
    "VariantToString",
    "VariantToStringAlloc",
    "VariantToDosDateTime",
    "VariantToStrRet",
    "VariantToFileTime",
    "VariantGetElementCount",
    "VariantToBooleanArray",
    "VariantToInt16Array",
    "VariantToUInt16Array",
    "VariantToInt32Array",
    "VariantToUInt32Array",
    "VariantToInt64Array",
    "VariantToUInt64Array",
    "VariantToDoubleArray",
    "VariantToStringArray",
    "VariantToBooleanArrayAlloc",
    "VariantToInt16ArrayAlloc",
    "VariantToUInt16ArrayAlloc",
    "VariantToInt32ArrayAlloc",
    "VariantToUInt32ArrayAlloc",
    "VariantToInt64ArrayAlloc",
    "VariantToUInt64ArrayAlloc",
    "VariantToDoubleArrayAlloc",
    "VariantToStringArrayAlloc",
    "VariantGetBooleanElem",
    "VariantGetInt16Elem",
    "VariantGetUInt16Elem",
    "VariantGetInt32Elem",
    "VariantGetUInt32Elem",
    "VariantGetInt64Elem",
    "VariantGetUInt64Elem",
    "VariantGetDoubleElem",
    "VariantGetStringElem",
    "ClearVariantArray",
    "VariantCompare",
    "SHGetPropertyStoreFromIDList",
    "SHGetPropertyStoreFromParsingName",
    "SHAddDefaultPropertiesByExt",
    "PifMgr_OpenProperties",
    "PifMgr_GetProperties",
    "PifMgr_SetProperties",
    "PifMgr_CloseProperties",
    "SHPropStgCreate",
    "SHPropStgReadMultiple",
    "SHPropStgWriteMultiple",
    "SHGetPropertyStoreForWindow",
]
