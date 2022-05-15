from win32more import *
import win32more.System.SettingsManagementInfrastructure
import win32more.Foundation
import win32more.System.Com

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.System.SettingsManagementInfrastructure, name, globals()[f"_define_{name}"]())
    return getattr(win32more.System.SettingsManagementInfrastructure, name)
def __dir__():
    return __all__
WCM_SETTINGS_ID_FLAG_REFERENCE = 0
WCM_SETTINGS_ID_FLAG_DEFINITION = 1
LINK_STORE_TO_ENGINE_INSTANCE = 1
LIMITED_VALIDATION_MODE = 1
WCM_E_INTERNALERROR = -2145255424
WCM_E_STATENODENOTFOUND = -2145255423
WCM_E_STATENODENOTALLOWED = -2145255422
WCM_E_ATTRIBUTENOTFOUND = -2145255421
WCM_E_ATTRIBUTENOTALLOWED = -2145255420
WCM_E_INVALIDVALUE = -2145255419
WCM_E_INVALIDVALUEFORMAT = -2145255418
WCM_E_TYPENOTSPECIFIED = -2145255417
WCM_E_INVALIDDATATYPE = -2145255416
WCM_E_NOTPOSITIONED = -2145255415
WCM_E_READONLYITEM = -2145255414
WCM_E_INVALIDPATH = -2145255413
WCM_E_WRONGESCAPESTRING = -2145255412
WCM_E_INVALIDVERSIONFORMAT = -2145255411
WCM_E_INVALIDLANGUAGEFORMAT = -2145255410
WCM_E_KEYNOTCHANGEABLE = -2145255409
WCM_E_EXPRESSIONNOTFOUND = -2145255408
WCM_E_SUBSTITUTIONNOTFOUND = -2145255407
WCM_E_USERALREADYREGISTERED = -2145255406
WCM_E_USERNOTFOUND = -2145255405
WCM_E_NAMESPACENOTFOUND = -2145255404
WCM_E_NAMESPACEALREADYREGISTERED = -2145255403
WCM_E_STORECORRUPTED = -2145255402
WCM_E_INVALIDEXPRESSIONSYNTAX = -2145255401
WCM_E_NOTIFICATIONNOTFOUND = -2145255400
WCM_E_CONFLICTINGASSERTION = -2145255399
WCM_E_ASSERTIONFAILED = -2145255398
WCM_E_DUPLICATENAME = -2145255397
WCM_E_INVALIDKEY = -2145255396
WCM_E_INVALIDSTREAM = -2145255395
WCM_E_HANDLERNOTFOUND = -2145255394
WCM_E_INVALIDHANDLERSYNTAX = -2145255393
WCM_E_VALIDATIONFAILED = -2145255392
WCM_E_RESTRICTIONFAILED = -2145255391
WCM_E_MANIFESTCOMPILATIONFAILED = -2145255390
WCM_E_CYCLICREFERENCE = -2145255389
WCM_E_MIXTYPEASSERTION = -2145255388
WCM_E_NOTSUPPORTEDFUNCTION = -2145255387
WCM_E_VALUETOOBIG = -2145255386
WCM_E_INVALIDATTRIBUTECOMBINATION = -2145255385
WCM_E_ABORTOPERATION = -2145255384
WCM_E_MISSINGCONFIGURATION = -2145255383
WCM_E_INVALIDPROCESSORFORMAT = -2145255382
WCM_E_SOURCEMANEMPTYVALUE = -2145255381
WCM_S_INTERNALERROR = 2232320
WCM_S_ATTRIBUTENOTFOUND = 2232321
WCM_S_LEGACYSETTINGWARNING = 2232322
WCM_S_INVALIDATTRIBUTECOMBINATION = 2232324
WCM_S_ATTRIBUTENOTALLOWED = 2232325
WCM_S_NAMESPACENOTFOUND = 2232326
WCM_E_UNKNOWNRESULT = -2145251325
SettingsEngine = Guid('9f7d7bb5-20b3-11da-81a5-0030f1642e3c')
WcmTargetMode = Int32
WcmTargetMode_OfflineMode = 1
WcmTargetMode_OnlineMode = 2
WcmNamespaceEnumerationFlags = Int32
WcmNamespaceEnumerationFlags_SharedEnumeration = 1
WcmNamespaceEnumerationFlags_UserEnumeration = 2
WcmNamespaceEnumerationFlags_AllEnumeration = 3
WcmDataType = Int32
WcmDataType_dataTypeByte = 1
WcmDataType_dataTypeSByte = 2
WcmDataType_dataTypeUInt16 = 3
WcmDataType_dataTypeInt16 = 4
WcmDataType_dataTypeUInt32 = 5
WcmDataType_dataTypeInt32 = 6
WcmDataType_dataTypeUInt64 = 7
WcmDataType_dataTypeInt64 = 8
WcmDataType_dataTypeBoolean = 11
WcmDataType_dataTypeString = 12
WcmDataType_dataTypeFlagArray = 32768
WcmSettingType = Int32
WcmSettingType_settingTypeScalar = 1
WcmSettingType_settingTypeComplex = 2
WcmSettingType_settingTypeList = 3
WcmRestrictionFacets = Int32
WcmRestrictionFacets_restrictionFacetMaxLength = 1
WcmRestrictionFacets_restrictionFacetEnumeration = 2
WcmRestrictionFacets_restrictionFacetMaxInclusive = 4
WcmRestrictionFacets_restrictionFacetMinInclusive = 8
WcmUserStatus = Int32
WcmUserStatus_UnknownStatus = 0
WcmUserStatus_UserRegistered = 1
WcmUserStatus_UserUnregistered = 2
WcmUserStatus_UserLoaded = 3
WcmUserStatus_UserUnloaded = 4
WcmNamespaceAccess = Int32
WcmNamespaceAccess_ReadOnlyAccess = 1
WcmNamespaceAccess_ReadWriteAccess = 2
def _define_IItemEnumerator_head():
    class IItemEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f7d7bb7-20b3-11da-81a5-0030f1642e3c')
    return IItemEnumerator
def _define_IItemEnumerator():
    IItemEnumerator = win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head
    IItemEnumerator.Current = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(3, 'Current', ((1, 'Item'),)))
    IItemEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'MoveNext', ((1, 'ItemValid'),)))
    IItemEnumerator.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    return IItemEnumerator
def _define_ISettingsIdentity_head():
    class ISettingsIdentity(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f7d7bb6-20b3-11da-81a5-0030f1642e3c')
    return ISettingsIdentity
def _define_ISettingsIdentity():
    ISettingsIdentity = win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head
    ISettingsIdentity.GetAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetAttribute', ((1, 'Reserved'),(1, 'Name'),(1, 'Value'),)))
    ISettingsIdentity.SetAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(4, 'SetAttribute', ((1, 'Reserved'),(1, 'Name'),(1, 'Value'),)))
    ISettingsIdentity.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetFlags', ((1, 'Flags'),)))
    ISettingsIdentity.SetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'SetFlags', ((1, 'Flags'),)))
    return ISettingsIdentity
def _define_ITargetInfo_head():
    class ITargetInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f7d7bb8-20b3-11da-81a5-0030f1642e3c')
    return ITargetInfo
def _define_ITargetInfo():
    ITargetInfo = win32more.System.SettingsManagementInfrastructure.ITargetInfo_head
    ITargetInfo.GetTargetMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.WcmTargetMode), use_last_error=False)(3, 'GetTargetMode', ((1, 'TargetMode'),)))
    ITargetInfo.SetTargetMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SettingsManagementInfrastructure.WcmTargetMode, use_last_error=False)(4, 'SetTargetMode', ((1, 'TargetMode'),)))
    ITargetInfo.GetTemporaryStoreLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'GetTemporaryStoreLocation', ((1, 'TemporaryStoreLocation'),)))
    ITargetInfo.SetTemporaryStoreLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'SetTemporaryStoreLocation', ((1, 'TemporaryStoreLocation'),)))
    ITargetInfo.GetTargetID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetTargetID', ((1, 'TargetID'),)))
    ITargetInfo.SetTargetID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(8, 'SetTargetID', ((1, 'TargetID'),)))
    ITargetInfo.GetTargetProcessorArchitecture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetTargetProcessorArchitecture', ((1, 'ProcessorArchitecture'),)))
    ITargetInfo.SetTargetProcessorArchitecture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(10, 'SetTargetProcessorArchitecture', ((1, 'ProcessorArchitecture'),)))
    ITargetInfo.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetProperty', ((1, 'Offline'),(1, 'Property'),(1, 'Value'),)))
    ITargetInfo.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(12, 'SetProperty', ((1, 'Offline'),(1, 'Property'),(1, 'Value'),)))
    ITargetInfo.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head), use_last_error=False)(13, 'GetEnumerator', ((1, 'Enumerator'),)))
    ITargetInfo.ExpandTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'ExpandTarget', ((1, 'Offline'),(1, 'Location'),(1, 'ExpandedLocation'),)))
    ITargetInfo.ExpandTargetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'ExpandTargetPath', ((1, 'Offline'),(1, 'Location'),(1, 'ExpandedLocation'),)))
    ITargetInfo.SetModulePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(16, 'SetModulePath', ((1, 'Module'),(1, 'Path'),)))
    ITargetInfo.LoadModule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HINSTANCE), use_last_error=False)(17, 'LoadModule', ((1, 'Module'),(1, 'ModuleHandle'),)))
    ITargetInfo.SetWow64Context = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_char_p_no, use_last_error=False)(18, 'SetWow64Context', ((1, 'InstallerModule'),(1, 'Wow64Context'),)))
    ITargetInfo.TranslateWow64 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'TranslateWow64', ((1, 'ClientArchitecture'),(1, 'Value'),(1, 'TranslatedValue'),)))
    ITargetInfo.SetSchemaHiveLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(20, 'SetSchemaHiveLocation', ((1, 'pwzHiveDir'),)))
    ITargetInfo.GetSchemaHiveLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'GetSchemaHiveLocation', ((1, 'pHiveLocation'),)))
    ITargetInfo.SetSchemaHiveMountName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(22, 'SetSchemaHiveMountName', ((1, 'pwzMountName'),)))
    ITargetInfo.GetSchemaHiveMountName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'GetSchemaHiveMountName', ((1, 'pMountName'),)))
    return ITargetInfo
def _define_ISettingsEngine_head():
    class ISettingsEngine(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f7d7bb9-20b3-11da-81a5-0030f1642e3c')
    return ISettingsEngine
def _define_ISettingsEngine():
    ISettingsEngine = win32more.System.SettingsManagementInfrastructure.ISettingsEngine_head
    ISettingsEngine.GetNamespaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SettingsManagementInfrastructure.WcmNamespaceEnumerationFlags,c_void_p,POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head), use_last_error=False)(3, 'GetNamespaces', ((1, 'Flags'),(1, 'Reserved'),(1, 'Namespaces'),)))
    ISettingsEngine.GetNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head,win32more.System.SettingsManagementInfrastructure.WcmNamespaceAccess,c_void_p,POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsNamespace_head), use_last_error=False)(4, 'GetNamespace', ((1, 'SettingsID'),(1, 'Access'),(1, 'Reserved'),(1, 'NamespaceItem'),)))
    ISettingsEngine.GetErrorDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'GetErrorDescription', ((1, 'HResult'),(1, 'Message'),)))
    ISettingsEngine.CreateSettingsIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head), use_last_error=False)(6, 'CreateSettingsIdentity', ((1, 'SettingsID'),)))
    ISettingsEngine.GetStoreStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.SettingsManagementInfrastructure.WcmUserStatus), use_last_error=False)(7, 'GetStoreStatus', ((1, 'Reserved'),(1, 'Status'),)))
    ISettingsEngine.LoadStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'LoadStore', ((1, 'Flags'),)))
    ISettingsEngine.UnloadStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(9, 'UnloadStore', ((1, 'Reserved'),)))
    ISettingsEngine.RegisterNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head,win32more.System.Com.IStream_head,win32more.Foundation.BOOL,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'RegisterNamespace', ((1, 'SettingsID'),(1, 'Stream'),(1, 'PushSettings'),(1, 'Results'),)))
    ISettingsEngine.UnregisterNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head,win32more.Foundation.BOOL, use_last_error=False)(11, 'UnregisterNamespace', ((1, 'SettingsID'),(1, 'RemoveSettings'),)))
    ISettingsEngine.CreateTargetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.ITargetInfo_head), use_last_error=False)(12, 'CreateTargetInfo', ((1, 'Target'),)))
    ISettingsEngine.GetTargetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.ITargetInfo_head), use_last_error=False)(13, 'GetTargetInfo', ((1, 'Target'),)))
    ISettingsEngine.SetTargetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SettingsManagementInfrastructure.ITargetInfo_head, use_last_error=False)(14, 'SetTargetInfo', ((1, 'Target'),)))
    ISettingsEngine.CreateSettingsContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsContext_head), use_last_error=False)(15, 'CreateSettingsContext', ((1, 'Flags'),(1, 'Reserved'),(1, 'SettingsContext'),)))
    ISettingsEngine.SetSettingsContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SettingsManagementInfrastructure.ISettingsContext_head, use_last_error=False)(16, 'SetSettingsContext', ((1, 'SettingsContext'),)))
    ISettingsEngine.ApplySettingsContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SettingsManagementInfrastructure.ISettingsContext_head,POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UIntPtr), use_last_error=False)(17, 'ApplySettingsContext', ((1, 'SettingsContext'),(1, 'pppwzIdentities'),(1, 'pcIdentities'),)))
    ISettingsEngine.GetSettingsContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsContext_head), use_last_error=False)(18, 'GetSettingsContext', ((1, 'SettingsContext'),)))
    return ISettingsEngine
def _define_ISettingsItem_head():
    class ISettingsItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f7d7bbb-20b3-11da-81a5-0030f1642e3c')
    return ISettingsItem
def _define_ISettingsItem():
    ISettingsItem = win32more.System.SettingsManagementInfrastructure.ISettingsItem_head
    ISettingsItem.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetName', ((1, 'Name'),)))
    ISettingsItem.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'GetValue', ((1, 'Value'),)))
    ISettingsItem.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(5, 'SetValue', ((1, 'Value'),)))
    ISettingsItem.GetSettingType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.WcmSettingType), use_last_error=False)(6, 'GetSettingType', ((1, 'Type'),)))
    ISettingsItem.GetDataType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.WcmDataType), use_last_error=False)(7, 'GetDataType', ((1, 'Type'),)))
    ISettingsItem.GetValueRaw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(8, 'GetValueRaw', ((1, 'Data'),(1, 'DataSize'),)))
    ISettingsItem.SetValueRaw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Byte),UInt32, use_last_error=False)(9, 'SetValueRaw', ((1, 'DataType'),(1, 'Data'),(1, 'DataSize'),)))
    ISettingsItem.HasChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'HasChild', ((1, 'ItemHasChild'),)))
    ISettingsItem.Children = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head), use_last_error=False)(11, 'Children', ((1, 'Children'),)))
    ISettingsItem.GetChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head), use_last_error=False)(12, 'GetChild', ((1, 'Name'),(1, 'Child'),)))
    ISettingsItem.GetSettingByPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head), use_last_error=False)(13, 'GetSettingByPath', ((1, 'Path'),(1, 'Setting'),)))
    ISettingsItem.CreateSettingByPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head), use_last_error=False)(14, 'CreateSettingByPath', ((1, 'Path'),(1, 'Setting'),)))
    ISettingsItem.RemoveSettingByPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(15, 'RemoveSettingByPath', ((1, 'Path'),)))
    ISettingsItem.GetListKeyInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),POINTER(win32more.System.SettingsManagementInfrastructure.WcmDataType), use_last_error=False)(16, 'GetListKeyInformation', ((1, 'KeyName'),(1, 'DataType'),)))
    ISettingsItem.CreateListElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head), use_last_error=False)(17, 'CreateListElement', ((1, 'KeyData'),(1, 'Child'),)))
    ISettingsItem.RemoveListElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(18, 'RemoveListElement', ((1, 'ElementName'),)))
    ISettingsItem.Attributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head), use_last_error=False)(19, 'Attributes', ((1, 'Attributes'),)))
    ISettingsItem.GetAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(20, 'GetAttribute', ((1, 'Name'),(1, 'Value'),)))
    ISettingsItem.GetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'GetPath', ((1, 'Path'),)))
    ISettingsItem.GetRestrictionFacets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.WcmRestrictionFacets), use_last_error=False)(22, 'GetRestrictionFacets', ((1, 'RestrictionFacets'),)))
    ISettingsItem.GetRestriction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SettingsManagementInfrastructure.WcmRestrictionFacets,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(23, 'GetRestriction', ((1, 'RestrictionFacet'),(1, 'FacetData'),)))
    ISettingsItem.GetKeyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(24, 'GetKeyValue', ((1, 'Value'),)))
    return ISettingsItem
def _define_ISettingsNamespace_head():
    class ISettingsNamespace(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f7d7bba-20b3-11da-81a5-0030f1642e3c')
    return ISettingsNamespace
def _define_ISettingsNamespace():
    ISettingsNamespace = win32more.System.SettingsManagementInfrastructure.ISettingsNamespace_head
    ISettingsNamespace.GetIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head), use_last_error=False)(3, 'GetIdentity', ((1, 'SettingsID'),)))
    ISettingsNamespace.Settings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head), use_last_error=False)(4, 'Settings', ((1, 'Settings'),)))
    ISettingsNamespace.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsResult_head), use_last_error=False)(5, 'Save', ((1, 'PushSettings'),(1, 'Result'),)))
    ISettingsNamespace.GetSettingByPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head), use_last_error=False)(6, 'GetSettingByPath', ((1, 'Path'),(1, 'Setting'),)))
    ISettingsNamespace.CreateSettingByPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head), use_last_error=False)(7, 'CreateSettingByPath', ((1, 'Path'),(1, 'Setting'),)))
    ISettingsNamespace.RemoveSettingByPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(8, 'RemoveSettingByPath', ((1, 'Path'),)))
    ISettingsNamespace.GetAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'GetAttribute', ((1, 'Name'),(1, 'Value'),)))
    return ISettingsNamespace
def _define_ISettingsResult_head():
    class ISettingsResult(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f7d7bbc-20b3-11da-81a5-0030f1642e3c')
    return ISettingsResult
def _define_ISettingsResult():
    ISettingsResult = win32more.System.SettingsManagementInfrastructure.ISettingsResult_head
    ISettingsResult.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetDescription', ((1, 'description'),)))
    ISettingsResult.GetErrorCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(4, 'GetErrorCode', ((1, 'hrOut'),)))
    ISettingsResult.GetContextDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'GetContextDescription', ((1, 'description'),)))
    ISettingsResult.GetLine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetLine', ((1, 'dwLine'),)))
    ISettingsResult.GetColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetColumn', ((1, 'dwColumn'),)))
    ISettingsResult.GetSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetSource', ((1, 'file'),)))
    return ISettingsResult
def _define_ISettingsContext_head():
    class ISettingsContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f7d7bbd-20b3-11da-81a5-0030f1642e3c')
    return ISettingsContext
def _define_ISettingsContext():
    ISettingsContext = win32more.System.SettingsManagementInfrastructure.ISettingsContext_head
    ISettingsContext.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.SettingsManagementInfrastructure.ITargetInfo_head, use_last_error=False)(3, 'Serialize', ((1, 'pStream'),(1, 'pTarget'),)))
    ISettingsContext.Deserialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.SettingsManagementInfrastructure.ITargetInfo_head,POINTER(POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsResult_head)),POINTER(UIntPtr), use_last_error=False)(4, 'Deserialize', ((1, 'pStream'),(1, 'pTarget'),(1, 'pppResults'),(1, 'pcResultCount'),)))
    ISettingsContext.SetUserData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(5, 'SetUserData', ((1, 'pUserData'),)))
    ISettingsContext.GetUserData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p), use_last_error=False)(6, 'GetUserData', ((1, 'pUserData'),)))
    ISettingsContext.GetNamespaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head), use_last_error=False)(7, 'GetNamespaces', ((1, 'ppNamespaceIds'),)))
    ISettingsContext.GetStoredSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head,POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head),POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head),POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head), use_last_error=False)(8, 'GetStoredSettings', ((1, 'pIdentity'),(1, 'ppAddedSettings'),(1, 'ppModifiedSettings'),(1, 'ppDeletedSettings'),)))
    ISettingsContext.RevertSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head,win32more.Foundation.PWSTR, use_last_error=False)(9, 'RevertSetting', ((1, 'pIdentity'),(1, 'pwzSetting'),)))
    return ISettingsContext
__all__ = [
    "WCM_SETTINGS_ID_FLAG_REFERENCE",
    "WCM_SETTINGS_ID_FLAG_DEFINITION",
    "LINK_STORE_TO_ENGINE_INSTANCE",
    "LIMITED_VALIDATION_MODE",
    "WCM_E_INTERNALERROR",
    "WCM_E_STATENODENOTFOUND",
    "WCM_E_STATENODENOTALLOWED",
    "WCM_E_ATTRIBUTENOTFOUND",
    "WCM_E_ATTRIBUTENOTALLOWED",
    "WCM_E_INVALIDVALUE",
    "WCM_E_INVALIDVALUEFORMAT",
    "WCM_E_TYPENOTSPECIFIED",
    "WCM_E_INVALIDDATATYPE",
    "WCM_E_NOTPOSITIONED",
    "WCM_E_READONLYITEM",
    "WCM_E_INVALIDPATH",
    "WCM_E_WRONGESCAPESTRING",
    "WCM_E_INVALIDVERSIONFORMAT",
    "WCM_E_INVALIDLANGUAGEFORMAT",
    "WCM_E_KEYNOTCHANGEABLE",
    "WCM_E_EXPRESSIONNOTFOUND",
    "WCM_E_SUBSTITUTIONNOTFOUND",
    "WCM_E_USERALREADYREGISTERED",
    "WCM_E_USERNOTFOUND",
    "WCM_E_NAMESPACENOTFOUND",
    "WCM_E_NAMESPACEALREADYREGISTERED",
    "WCM_E_STORECORRUPTED",
    "WCM_E_INVALIDEXPRESSIONSYNTAX",
    "WCM_E_NOTIFICATIONNOTFOUND",
    "WCM_E_CONFLICTINGASSERTION",
    "WCM_E_ASSERTIONFAILED",
    "WCM_E_DUPLICATENAME",
    "WCM_E_INVALIDKEY",
    "WCM_E_INVALIDSTREAM",
    "WCM_E_HANDLERNOTFOUND",
    "WCM_E_INVALIDHANDLERSYNTAX",
    "WCM_E_VALIDATIONFAILED",
    "WCM_E_RESTRICTIONFAILED",
    "WCM_E_MANIFESTCOMPILATIONFAILED",
    "WCM_E_CYCLICREFERENCE",
    "WCM_E_MIXTYPEASSERTION",
    "WCM_E_NOTSUPPORTEDFUNCTION",
    "WCM_E_VALUETOOBIG",
    "WCM_E_INVALIDATTRIBUTECOMBINATION",
    "WCM_E_ABORTOPERATION",
    "WCM_E_MISSINGCONFIGURATION",
    "WCM_E_INVALIDPROCESSORFORMAT",
    "WCM_E_SOURCEMANEMPTYVALUE",
    "WCM_S_INTERNALERROR",
    "WCM_S_ATTRIBUTENOTFOUND",
    "WCM_S_LEGACYSETTINGWARNING",
    "WCM_S_INVALIDATTRIBUTECOMBINATION",
    "WCM_S_ATTRIBUTENOTALLOWED",
    "WCM_S_NAMESPACENOTFOUND",
    "WCM_E_UNKNOWNRESULT",
    "SettingsEngine",
    "WcmTargetMode",
    "WcmTargetMode_OfflineMode",
    "WcmTargetMode_OnlineMode",
    "WcmNamespaceEnumerationFlags",
    "WcmNamespaceEnumerationFlags_SharedEnumeration",
    "WcmNamespaceEnumerationFlags_UserEnumeration",
    "WcmNamespaceEnumerationFlags_AllEnumeration",
    "WcmDataType",
    "WcmDataType_dataTypeByte",
    "WcmDataType_dataTypeSByte",
    "WcmDataType_dataTypeUInt16",
    "WcmDataType_dataTypeInt16",
    "WcmDataType_dataTypeUInt32",
    "WcmDataType_dataTypeInt32",
    "WcmDataType_dataTypeUInt64",
    "WcmDataType_dataTypeInt64",
    "WcmDataType_dataTypeBoolean",
    "WcmDataType_dataTypeString",
    "WcmDataType_dataTypeFlagArray",
    "WcmSettingType",
    "WcmSettingType_settingTypeScalar",
    "WcmSettingType_settingTypeComplex",
    "WcmSettingType_settingTypeList",
    "WcmRestrictionFacets",
    "WcmRestrictionFacets_restrictionFacetMaxLength",
    "WcmRestrictionFacets_restrictionFacetEnumeration",
    "WcmRestrictionFacets_restrictionFacetMaxInclusive",
    "WcmRestrictionFacets_restrictionFacetMinInclusive",
    "WcmUserStatus",
    "WcmUserStatus_UnknownStatus",
    "WcmUserStatus_UserRegistered",
    "WcmUserStatus_UserUnregistered",
    "WcmUserStatus_UserLoaded",
    "WcmUserStatus_UserUnloaded",
    "WcmNamespaceAccess",
    "WcmNamespaceAccess_ReadOnlyAccess",
    "WcmNamespaceAccess_ReadWriteAccess",
    "IItemEnumerator",
    "ISettingsIdentity",
    "ITargetInfo",
    "ISettingsEngine",
    "ISettingsItem",
    "ISettingsNamespace",
    "ISettingsResult",
    "ISettingsContext",
]
