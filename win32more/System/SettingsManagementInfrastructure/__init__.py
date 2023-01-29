from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.SettingsManagementInfrastructure
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
WCM_SETTINGS_ID_NAME: String = 'name'
WCM_SETTINGS_ID_VERSION: String = 'version'
WCM_SETTINGS_ID_LANGUAGE: String = 'language'
WCM_SETTINGS_ID_ARCHITECTURE: String = 'architecture'
WCM_SETTINGS_ID_TOKEN: String = 'token'
WCM_SETTINGS_ID_URI: String = 'uri'
WCM_SETTINGS_ID_VERSION_SCOPE: String = 'versionScope'
WCM_SETTINGS_ID_FLAG_REFERENCE: UInt32 = 0
WCM_SETTINGS_ID_FLAG_DEFINITION: UInt32 = 1
LINK_STORE_TO_ENGINE_INSTANCE: UInt32 = 1
LIMITED_VALIDATION_MODE: UInt32 = 1
WCM_E_INTERNALERROR: win32more.Foundation.HRESULT = -2145255424
WCM_E_STATENODENOTFOUND: win32more.Foundation.HRESULT = -2145255423
WCM_E_STATENODENOTALLOWED: win32more.Foundation.HRESULT = -2145255422
WCM_E_ATTRIBUTENOTFOUND: win32more.Foundation.HRESULT = -2145255421
WCM_E_ATTRIBUTENOTALLOWED: win32more.Foundation.HRESULT = -2145255420
WCM_E_INVALIDVALUE: win32more.Foundation.HRESULT = -2145255419
WCM_E_INVALIDVALUEFORMAT: win32more.Foundation.HRESULT = -2145255418
WCM_E_TYPENOTSPECIFIED: win32more.Foundation.HRESULT = -2145255417
WCM_E_INVALIDDATATYPE: win32more.Foundation.HRESULT = -2145255416
WCM_E_NOTPOSITIONED: win32more.Foundation.HRESULT = -2145255415
WCM_E_READONLYITEM: win32more.Foundation.HRESULT = -2145255414
WCM_E_INVALIDPATH: win32more.Foundation.HRESULT = -2145255413
WCM_E_WRONGESCAPESTRING: win32more.Foundation.HRESULT = -2145255412
WCM_E_INVALIDVERSIONFORMAT: win32more.Foundation.HRESULT = -2145255411
WCM_E_INVALIDLANGUAGEFORMAT: win32more.Foundation.HRESULT = -2145255410
WCM_E_KEYNOTCHANGEABLE: win32more.Foundation.HRESULT = -2145255409
WCM_E_EXPRESSIONNOTFOUND: win32more.Foundation.HRESULT = -2145255408
WCM_E_SUBSTITUTIONNOTFOUND: win32more.Foundation.HRESULT = -2145255407
WCM_E_USERALREADYREGISTERED: win32more.Foundation.HRESULT = -2145255406
WCM_E_USERNOTFOUND: win32more.Foundation.HRESULT = -2145255405
WCM_E_NAMESPACENOTFOUND: win32more.Foundation.HRESULT = -2145255404
WCM_E_NAMESPACEALREADYREGISTERED: win32more.Foundation.HRESULT = -2145255403
WCM_E_STORECORRUPTED: win32more.Foundation.HRESULT = -2145255402
WCM_E_INVALIDEXPRESSIONSYNTAX: win32more.Foundation.HRESULT = -2145255401
WCM_E_NOTIFICATIONNOTFOUND: win32more.Foundation.HRESULT = -2145255400
WCM_E_CONFLICTINGASSERTION: win32more.Foundation.HRESULT = -2145255399
WCM_E_ASSERTIONFAILED: win32more.Foundation.HRESULT = -2145255398
WCM_E_DUPLICATENAME: win32more.Foundation.HRESULT = -2145255397
WCM_E_INVALIDKEY: win32more.Foundation.HRESULT = -2145255396
WCM_E_INVALIDSTREAM: win32more.Foundation.HRESULT = -2145255395
WCM_E_HANDLERNOTFOUND: win32more.Foundation.HRESULT = -2145255394
WCM_E_INVALIDHANDLERSYNTAX: win32more.Foundation.HRESULT = -2145255393
WCM_E_VALIDATIONFAILED: win32more.Foundation.HRESULT = -2145255392
WCM_E_RESTRICTIONFAILED: win32more.Foundation.HRESULT = -2145255391
WCM_E_MANIFESTCOMPILATIONFAILED: win32more.Foundation.HRESULT = -2145255390
WCM_E_CYCLICREFERENCE: win32more.Foundation.HRESULT = -2145255389
WCM_E_MIXTYPEASSERTION: win32more.Foundation.HRESULT = -2145255388
WCM_E_NOTSUPPORTEDFUNCTION: win32more.Foundation.HRESULT = -2145255387
WCM_E_VALUETOOBIG: win32more.Foundation.HRESULT = -2145255386
WCM_E_INVALIDATTRIBUTECOMBINATION: win32more.Foundation.HRESULT = -2145255385
WCM_E_ABORTOPERATION: win32more.Foundation.HRESULT = -2145255384
WCM_E_MISSINGCONFIGURATION: win32more.Foundation.HRESULT = -2145255383
WCM_E_INVALIDPROCESSORFORMAT: win32more.Foundation.HRESULT = -2145255382
WCM_E_SOURCEMANEMPTYVALUE: win32more.Foundation.HRESULT = -2145255381
WCM_S_INTERNALERROR: win32more.Foundation.HRESULT = 2232320
WCM_S_ATTRIBUTENOTFOUND: win32more.Foundation.HRESULT = 2232321
WCM_S_LEGACYSETTINGWARNING: win32more.Foundation.HRESULT = 2232322
WCM_S_INVALIDATTRIBUTECOMBINATION: win32more.Foundation.HRESULT = 2232324
WCM_S_ATTRIBUTENOTALLOWED: win32more.Foundation.HRESULT = 2232325
WCM_S_NAMESPACENOTFOUND: win32more.Foundation.HRESULT = 2232326
WCM_E_UNKNOWNRESULT: win32more.Foundation.HRESULT = -2145251325
class IItemEnumerator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9f7d7bb7-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def Current(Item: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def MoveNext(ItemValid: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
class ISettingsContext(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9f7d7bbd-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def Serialize(pStream: win32more.System.Com.IStream_head, pTarget: win32more.System.SettingsManagementInfrastructure.ITargetInfo_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Deserialize(pStream: win32more.System.Com.IStream_head, pTarget: win32more.System.SettingsManagementInfrastructure.ITargetInfo_head, pppResults: POINTER(POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsResult_head)), pcResultCount: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetUserData(pUserData: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetUserData(pUserData: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetNamespaces(ppNamespaceIds: POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetStoredSettings(pIdentity: win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head, ppAddedSettings: POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head), ppModifiedSettings: POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head), ppDeletedSettings: POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def RevertSetting(pIdentity: win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head, pwzSetting: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class ISettingsEngine(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9f7d7bb9-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetNamespaces(Flags: win32more.System.SettingsManagementInfrastructure.WcmNamespaceEnumerationFlags, Reserved: c_void_p, Namespaces: POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetNamespace(SettingsID: win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head, Access: win32more.System.SettingsManagementInfrastructure.WcmNamespaceAccess, Reserved: c_void_p, NamespaceItem: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsNamespace_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorDescription(HResult: Int32, Message: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CreateSettingsIdentity(SettingsID: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetStoreStatus(Reserved: c_void_p, Status: POINTER(win32more.System.SettingsManagementInfrastructure.WcmUserStatus)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def LoadStore(Flags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def UnloadStore(Reserved: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterNamespace(SettingsID: win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head, Stream: win32more.System.Com.IStream_head, PushSettings: win32more.Foundation.BOOL, Results: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def UnregisterNamespace(SettingsID: win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head, RemoveSettings: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CreateTargetInfo(Target: POINTER(win32more.System.SettingsManagementInfrastructure.ITargetInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetTargetInfo(Target: POINTER(win32more.System.SettingsManagementInfrastructure.ITargetInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetTargetInfo(Target: win32more.System.SettingsManagementInfrastructure.ITargetInfo_head) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def CreateSettingsContext(Flags: UInt32, Reserved: c_void_p, SettingsContext: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsContext_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetSettingsContext(SettingsContext: win32more.System.SettingsManagementInfrastructure.ISettingsContext_head) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def ApplySettingsContext(SettingsContext: win32more.System.SettingsManagementInfrastructure.ISettingsContext_head, pppwzIdentities: POINTER(POINTER(win32more.Foundation.PWSTR)), pcIdentities: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetSettingsContext(SettingsContext: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsContext_head)) -> win32more.Foundation.HRESULT: ...
class ISettingsIdentity(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9f7d7bb6-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetAttribute(Reserved: c_void_p, Name: win32more.Foundation.PWSTR, Value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetAttribute(Reserved: c_void_p, Name: win32more.Foundation.PWSTR, Value: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFlags(Flags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetFlags(Flags: UInt32) -> win32more.Foundation.HRESULT: ...
class ISettingsItem(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9f7d7bbb-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetName(Name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(Value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(Value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSettingType(Type: POINTER(win32more.System.SettingsManagementInfrastructure.WcmSettingType)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDataType(Type: POINTER(win32more.System.SettingsManagementInfrastructure.WcmDataType)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetValueRaw(Data: POINTER(c_char_p_no), DataSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetValueRaw(DataType: Int32, Data: c_char_p_no, DataSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def HasChild(ItemHasChild: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Children(Children: POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetChild(Name: win32more.Foundation.PWSTR, Child: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetSettingByPath(Path: win32more.Foundation.PWSTR, Setting: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def CreateSettingByPath(Path: win32more.Foundation.PWSTR, Setting: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def RemoveSettingByPath(Path: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetListKeyInformation(KeyName: POINTER(win32more.Foundation.BSTR), DataType: POINTER(win32more.System.SettingsManagementInfrastructure.WcmDataType)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def CreateListElement(KeyData: POINTER(win32more.System.Com.VARIANT_head), Child: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveListElement(ElementName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def Attributes(Attributes: POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetAttribute(Name: win32more.Foundation.PWSTR, Value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetPath(Path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetRestrictionFacets(RestrictionFacets: POINTER(win32more.System.SettingsManagementInfrastructure.WcmRestrictionFacets)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetRestriction(RestrictionFacet: win32more.System.SettingsManagementInfrastructure.WcmRestrictionFacets, FacetData: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetKeyValue(Value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class ISettingsNamespace(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9f7d7bba-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetIdentity(SettingsID: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsIdentity_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Settings(Settings: POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Save(PushSettings: win32more.Foundation.BOOL, Result: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsResult_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSettingByPath(Path: win32more.Foundation.PWSTR, Setting: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CreateSettingByPath(Path: win32more.Foundation.PWSTR, Setting: POINTER(win32more.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveSettingByPath(Path: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetAttribute(Name: win32more.Foundation.PWSTR, Value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class ISettingsResult(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9f7d7bbc-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetDescription(description: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetErrorCode(hrOut: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetContextDescription(description: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetLine(dwLine: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetColumn(dwColumn: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSource(file: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ITargetInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9f7d7bb8-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetTargetMode(TargetMode: POINTER(win32more.System.SettingsManagementInfrastructure.WcmTargetMode)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetTargetMode(TargetMode: win32more.System.SettingsManagementInfrastructure.WcmTargetMode) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTemporaryStoreLocation(TemporaryStoreLocation: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetTemporaryStoreLocation(TemporaryStoreLocation: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTargetID(TargetID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetTargetID(TargetID: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTargetProcessorArchitecture(ProcessorArchitecture: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetTargetProcessorArchitecture(ProcessorArchitecture: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetProperty(Offline: win32more.Foundation.BOOL, Property: win32more.Foundation.PWSTR, Value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetProperty(Offline: win32more.Foundation.BOOL, Property: win32more.Foundation.PWSTR, Value: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetEnumerator(Enumerator: POINTER(win32more.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def ExpandTarget(Offline: win32more.Foundation.BOOL, Location: win32more.Foundation.PWSTR, ExpandedLocation: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ExpandTargetPath(Offline: win32more.Foundation.BOOL, Location: win32more.Foundation.PWSTR, ExpandedLocation: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetModulePath(Module: win32more.Foundation.PWSTR, Path: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def LoadModule(Module: win32more.Foundation.PWSTR, ModuleHandle: POINTER(win32more.Foundation.HINSTANCE)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetWow64Context(InstallerModule: win32more.Foundation.PWSTR, Wow64Context: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def TranslateWow64(ClientArchitecture: win32more.Foundation.PWSTR, Value: win32more.Foundation.PWSTR, TranslatedValue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetSchemaHiveLocation(pwzHiveDir: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetSchemaHiveLocation(pHiveLocation: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetSchemaHiveMountName(pwzMountName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetSchemaHiveMountName(pMountName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
SettingsEngine = Guid('9f7d7bb5-20b3-11da-81-a5-00-30-f1-64-2e-3c')
WcmDataType = Int32
WcmDataType_dataTypeByte: WcmDataType = 1
WcmDataType_dataTypeSByte: WcmDataType = 2
WcmDataType_dataTypeUInt16: WcmDataType = 3
WcmDataType_dataTypeInt16: WcmDataType = 4
WcmDataType_dataTypeUInt32: WcmDataType = 5
WcmDataType_dataTypeInt32: WcmDataType = 6
WcmDataType_dataTypeUInt64: WcmDataType = 7
WcmDataType_dataTypeInt64: WcmDataType = 8
WcmDataType_dataTypeBoolean: WcmDataType = 11
WcmDataType_dataTypeString: WcmDataType = 12
WcmDataType_dataTypeFlagArray: WcmDataType = 32768
WcmNamespaceAccess = Int32
WcmNamespaceAccess_ReadOnlyAccess: WcmNamespaceAccess = 1
WcmNamespaceAccess_ReadWriteAccess: WcmNamespaceAccess = 2
WcmNamespaceEnumerationFlags = Int32
WcmNamespaceEnumerationFlags_SharedEnumeration: WcmNamespaceEnumerationFlags = 1
WcmNamespaceEnumerationFlags_UserEnumeration: WcmNamespaceEnumerationFlags = 2
WcmNamespaceEnumerationFlags_AllEnumeration: WcmNamespaceEnumerationFlags = 3
WcmRestrictionFacets = Int32
WcmRestrictionFacets_restrictionFacetMaxLength: WcmRestrictionFacets = 1
WcmRestrictionFacets_restrictionFacetEnumeration: WcmRestrictionFacets = 2
WcmRestrictionFacets_restrictionFacetMaxInclusive: WcmRestrictionFacets = 4
WcmRestrictionFacets_restrictionFacetMinInclusive: WcmRestrictionFacets = 8
WcmSettingType = Int32
WcmSettingType_settingTypeScalar: WcmSettingType = 1
WcmSettingType_settingTypeComplex: WcmSettingType = 2
WcmSettingType_settingTypeList: WcmSettingType = 3
WcmTargetMode = Int32
WcmTargetMode_OfflineMode: WcmTargetMode = 1
WcmTargetMode_OnlineMode: WcmTargetMode = 2
WcmUserStatus = Int32
WcmUserStatus_UnknownStatus: WcmUserStatus = 0
WcmUserStatus_UserRegistered: WcmUserStatus = 1
WcmUserStatus_UserUnregistered: WcmUserStatus = 2
WcmUserStatus_UserLoaded: WcmUserStatus = 3
WcmUserStatus_UserUnloaded: WcmUserStatus = 4
make_head(_module, 'IItemEnumerator')
make_head(_module, 'ISettingsContext')
make_head(_module, 'ISettingsEngine')
make_head(_module, 'ISettingsIdentity')
make_head(_module, 'ISettingsItem')
make_head(_module, 'ISettingsNamespace')
make_head(_module, 'ISettingsResult')
make_head(_module, 'ITargetInfo')
__all__ = [
    "IItemEnumerator",
    "ISettingsContext",
    "ISettingsEngine",
    "ISettingsIdentity",
    "ISettingsItem",
    "ISettingsNamespace",
    "ISettingsResult",
    "ITargetInfo",
    "LIMITED_VALIDATION_MODE",
    "LINK_STORE_TO_ENGINE_INSTANCE",
    "SettingsEngine",
    "WCM_E_ABORTOPERATION",
    "WCM_E_ASSERTIONFAILED",
    "WCM_E_ATTRIBUTENOTALLOWED",
    "WCM_E_ATTRIBUTENOTFOUND",
    "WCM_E_CONFLICTINGASSERTION",
    "WCM_E_CYCLICREFERENCE",
    "WCM_E_DUPLICATENAME",
    "WCM_E_EXPRESSIONNOTFOUND",
    "WCM_E_HANDLERNOTFOUND",
    "WCM_E_INTERNALERROR",
    "WCM_E_INVALIDATTRIBUTECOMBINATION",
    "WCM_E_INVALIDDATATYPE",
    "WCM_E_INVALIDEXPRESSIONSYNTAX",
    "WCM_E_INVALIDHANDLERSYNTAX",
    "WCM_E_INVALIDKEY",
    "WCM_E_INVALIDLANGUAGEFORMAT",
    "WCM_E_INVALIDPATH",
    "WCM_E_INVALIDPROCESSORFORMAT",
    "WCM_E_INVALIDSTREAM",
    "WCM_E_INVALIDVALUE",
    "WCM_E_INVALIDVALUEFORMAT",
    "WCM_E_INVALIDVERSIONFORMAT",
    "WCM_E_KEYNOTCHANGEABLE",
    "WCM_E_MANIFESTCOMPILATIONFAILED",
    "WCM_E_MISSINGCONFIGURATION",
    "WCM_E_MIXTYPEASSERTION",
    "WCM_E_NAMESPACEALREADYREGISTERED",
    "WCM_E_NAMESPACENOTFOUND",
    "WCM_E_NOTIFICATIONNOTFOUND",
    "WCM_E_NOTPOSITIONED",
    "WCM_E_NOTSUPPORTEDFUNCTION",
    "WCM_E_READONLYITEM",
    "WCM_E_RESTRICTIONFAILED",
    "WCM_E_SOURCEMANEMPTYVALUE",
    "WCM_E_STATENODENOTALLOWED",
    "WCM_E_STATENODENOTFOUND",
    "WCM_E_STORECORRUPTED",
    "WCM_E_SUBSTITUTIONNOTFOUND",
    "WCM_E_TYPENOTSPECIFIED",
    "WCM_E_UNKNOWNRESULT",
    "WCM_E_USERALREADYREGISTERED",
    "WCM_E_USERNOTFOUND",
    "WCM_E_VALIDATIONFAILED",
    "WCM_E_VALUETOOBIG",
    "WCM_E_WRONGESCAPESTRING",
    "WCM_SETTINGS_ID_ARCHITECTURE",
    "WCM_SETTINGS_ID_FLAG_DEFINITION",
    "WCM_SETTINGS_ID_FLAG_REFERENCE",
    "WCM_SETTINGS_ID_LANGUAGE",
    "WCM_SETTINGS_ID_NAME",
    "WCM_SETTINGS_ID_TOKEN",
    "WCM_SETTINGS_ID_URI",
    "WCM_SETTINGS_ID_VERSION",
    "WCM_SETTINGS_ID_VERSION_SCOPE",
    "WCM_S_ATTRIBUTENOTALLOWED",
    "WCM_S_ATTRIBUTENOTFOUND",
    "WCM_S_INTERNALERROR",
    "WCM_S_INVALIDATTRIBUTECOMBINATION",
    "WCM_S_LEGACYSETTINGWARNING",
    "WCM_S_NAMESPACENOTFOUND",
    "WcmDataType",
    "WcmDataType_dataTypeBoolean",
    "WcmDataType_dataTypeByte",
    "WcmDataType_dataTypeFlagArray",
    "WcmDataType_dataTypeInt16",
    "WcmDataType_dataTypeInt32",
    "WcmDataType_dataTypeInt64",
    "WcmDataType_dataTypeSByte",
    "WcmDataType_dataTypeString",
    "WcmDataType_dataTypeUInt16",
    "WcmDataType_dataTypeUInt32",
    "WcmDataType_dataTypeUInt64",
    "WcmNamespaceAccess",
    "WcmNamespaceAccess_ReadOnlyAccess",
    "WcmNamespaceAccess_ReadWriteAccess",
    "WcmNamespaceEnumerationFlags",
    "WcmNamespaceEnumerationFlags_AllEnumeration",
    "WcmNamespaceEnumerationFlags_SharedEnumeration",
    "WcmNamespaceEnumerationFlags_UserEnumeration",
    "WcmRestrictionFacets",
    "WcmRestrictionFacets_restrictionFacetEnumeration",
    "WcmRestrictionFacets_restrictionFacetMaxInclusive",
    "WcmRestrictionFacets_restrictionFacetMaxLength",
    "WcmRestrictionFacets_restrictionFacetMinInclusive",
    "WcmSettingType",
    "WcmSettingType_settingTypeComplex",
    "WcmSettingType_settingTypeList",
    "WcmSettingType_settingTypeScalar",
    "WcmTargetMode",
    "WcmTargetMode_OfflineMode",
    "WcmTargetMode_OnlineMode",
    "WcmUserStatus",
    "WcmUserStatus_UnknownStatus",
    "WcmUserStatus_UserLoaded",
    "WcmUserStatus_UserRegistered",
    "WcmUserStatus_UserUnloaded",
    "WcmUserStatus_UserUnregistered",
]
_arch_optional = [
]
