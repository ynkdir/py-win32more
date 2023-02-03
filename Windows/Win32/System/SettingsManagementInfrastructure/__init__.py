from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.SettingsManagementInfrastructure
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
WCM_E_INTERNALERROR: Windows.Win32.Foundation.HRESULT = -2145255424
WCM_E_STATENODENOTFOUND: Windows.Win32.Foundation.HRESULT = -2145255423
WCM_E_STATENODENOTALLOWED: Windows.Win32.Foundation.HRESULT = -2145255422
WCM_E_ATTRIBUTENOTFOUND: Windows.Win32.Foundation.HRESULT = -2145255421
WCM_E_ATTRIBUTENOTALLOWED: Windows.Win32.Foundation.HRESULT = -2145255420
WCM_E_INVALIDVALUE: Windows.Win32.Foundation.HRESULT = -2145255419
WCM_E_INVALIDVALUEFORMAT: Windows.Win32.Foundation.HRESULT = -2145255418
WCM_E_TYPENOTSPECIFIED: Windows.Win32.Foundation.HRESULT = -2145255417
WCM_E_INVALIDDATATYPE: Windows.Win32.Foundation.HRESULT = -2145255416
WCM_E_NOTPOSITIONED: Windows.Win32.Foundation.HRESULT = -2145255415
WCM_E_READONLYITEM: Windows.Win32.Foundation.HRESULT = -2145255414
WCM_E_INVALIDPATH: Windows.Win32.Foundation.HRESULT = -2145255413
WCM_E_WRONGESCAPESTRING: Windows.Win32.Foundation.HRESULT = -2145255412
WCM_E_INVALIDVERSIONFORMAT: Windows.Win32.Foundation.HRESULT = -2145255411
WCM_E_INVALIDLANGUAGEFORMAT: Windows.Win32.Foundation.HRESULT = -2145255410
WCM_E_KEYNOTCHANGEABLE: Windows.Win32.Foundation.HRESULT = -2145255409
WCM_E_EXPRESSIONNOTFOUND: Windows.Win32.Foundation.HRESULT = -2145255408
WCM_E_SUBSTITUTIONNOTFOUND: Windows.Win32.Foundation.HRESULT = -2145255407
WCM_E_USERALREADYREGISTERED: Windows.Win32.Foundation.HRESULT = -2145255406
WCM_E_USERNOTFOUND: Windows.Win32.Foundation.HRESULT = -2145255405
WCM_E_NAMESPACENOTFOUND: Windows.Win32.Foundation.HRESULT = -2145255404
WCM_E_NAMESPACEALREADYREGISTERED: Windows.Win32.Foundation.HRESULT = -2145255403
WCM_E_STORECORRUPTED: Windows.Win32.Foundation.HRESULT = -2145255402
WCM_E_INVALIDEXPRESSIONSYNTAX: Windows.Win32.Foundation.HRESULT = -2145255401
WCM_E_NOTIFICATIONNOTFOUND: Windows.Win32.Foundation.HRESULT = -2145255400
WCM_E_CONFLICTINGASSERTION: Windows.Win32.Foundation.HRESULT = -2145255399
WCM_E_ASSERTIONFAILED: Windows.Win32.Foundation.HRESULT = -2145255398
WCM_E_DUPLICATENAME: Windows.Win32.Foundation.HRESULT = -2145255397
WCM_E_INVALIDKEY: Windows.Win32.Foundation.HRESULT = -2145255396
WCM_E_INVALIDSTREAM: Windows.Win32.Foundation.HRESULT = -2145255395
WCM_E_HANDLERNOTFOUND: Windows.Win32.Foundation.HRESULT = -2145255394
WCM_E_INVALIDHANDLERSYNTAX: Windows.Win32.Foundation.HRESULT = -2145255393
WCM_E_VALIDATIONFAILED: Windows.Win32.Foundation.HRESULT = -2145255392
WCM_E_RESTRICTIONFAILED: Windows.Win32.Foundation.HRESULT = -2145255391
WCM_E_MANIFESTCOMPILATIONFAILED: Windows.Win32.Foundation.HRESULT = -2145255390
WCM_E_CYCLICREFERENCE: Windows.Win32.Foundation.HRESULT = -2145255389
WCM_E_MIXTYPEASSERTION: Windows.Win32.Foundation.HRESULT = -2145255388
WCM_E_NOTSUPPORTEDFUNCTION: Windows.Win32.Foundation.HRESULT = -2145255387
WCM_E_VALUETOOBIG: Windows.Win32.Foundation.HRESULT = -2145255386
WCM_E_INVALIDATTRIBUTECOMBINATION: Windows.Win32.Foundation.HRESULT = -2145255385
WCM_E_ABORTOPERATION: Windows.Win32.Foundation.HRESULT = -2145255384
WCM_E_MISSINGCONFIGURATION: Windows.Win32.Foundation.HRESULT = -2145255383
WCM_E_INVALIDPROCESSORFORMAT: Windows.Win32.Foundation.HRESULT = -2145255382
WCM_E_SOURCEMANEMPTYVALUE: Windows.Win32.Foundation.HRESULT = -2145255381
WCM_S_INTERNALERROR: Windows.Win32.Foundation.HRESULT = 2232320
WCM_S_ATTRIBUTENOTFOUND: Windows.Win32.Foundation.HRESULT = 2232321
WCM_S_LEGACYSETTINGWARNING: Windows.Win32.Foundation.HRESULT = 2232322
WCM_S_INVALIDATTRIBUTECOMBINATION: Windows.Win32.Foundation.HRESULT = 2232324
WCM_S_ATTRIBUTENOTALLOWED: Windows.Win32.Foundation.HRESULT = 2232325
WCM_S_NAMESPACENOTFOUND: Windows.Win32.Foundation.HRESULT = 2232326
WCM_E_UNKNOWNRESULT: Windows.Win32.Foundation.HRESULT = -2145251325
class IItemEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9f7d7bb7-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def Current(Item: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MoveNext(ItemValid: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9f7d7bbd-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def Serialize(pStream: Windows.Win32.System.Com.IStream_head, pTarget: Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deserialize(pStream: Windows.Win32.System.Com.IStream_head, pTarget: Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo_head, pppResults: POINTER(POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsResult_head)), pcResultCount: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetUserData(pUserData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUserData(pUserData: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNamespaces(ppNamespaceIds: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStoredSettings(pIdentity: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head, ppAddedSettings: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head), ppModifiedSettings: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head), ppDeletedSettings: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RevertSetting(pIdentity: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head, pwzSetting: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsEngine(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9f7d7bb9-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetNamespaces(Flags: Windows.Win32.System.SettingsManagementInfrastructure.WcmNamespaceEnumerationFlags, Reserved: c_void_p, Namespaces: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNamespace(SettingsID: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head, Access: Windows.Win32.System.SettingsManagementInfrastructure.WcmNamespaceAccess, Reserved: c_void_p, NamespaceItem: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsNamespace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorDescription(HResult: Int32, Message: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateSettingsIdentity(SettingsID: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStoreStatus(Reserved: c_void_p, Status: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmUserStatus)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def LoadStore(Flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnloadStore(Reserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterNamespace(SettingsID: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head, Stream: Windows.Win32.System.Com.IStream_head, PushSettings: Windows.Win32.Foundation.BOOL, Results: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnregisterNamespace(SettingsID: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head, RemoveSettings: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateTargetInfo(Target: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetTargetInfo(Target: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetTargetInfo(Target: Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateSettingsContext(Flags: UInt32, Reserved: c_void_p, SettingsContext: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetSettingsContext(SettingsContext: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ApplySettingsContext(SettingsContext: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext_head, pppwzIdentities: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), pcIdentities: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetSettingsContext(SettingsContext: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsIdentity(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9f7d7bb6-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetAttribute(Reserved: c_void_p, Name: Windows.Win32.Foundation.PWSTR, Value: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAttribute(Reserved: c_void_p, Name: Windows.Win32.Foundation.PWSTR, Value: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFlags(Flags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetFlags(Flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsItem(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9f7d7bbb-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetName(Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(Value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(Value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSettingType(Type: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmSettingType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDataType(Type: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetValueRaw(Data: POINTER(c_char_p_no), DataSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetValueRaw(DataType: Int32, Data: c_char_p_no, DataSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def HasChild(ItemHasChild: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Children(Children: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetChild(Name: Windows.Win32.Foundation.PWSTR, Child: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSettingByPath(Path: Windows.Win32.Foundation.PWSTR, Setting: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateSettingByPath(Path: Windows.Win32.Foundation.PWSTR, Setting: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RemoveSettingByPath(Path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetListKeyInformation(KeyName: POINTER(Windows.Win32.Foundation.BSTR), DataType: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateListElement(KeyData: POINTER(Windows.Win32.System.Com.VARIANT_head), Child: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveListElement(ElementName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Attributes(Attributes: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetAttribute(Name: Windows.Win32.Foundation.PWSTR, Value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetPath(Path: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetRestrictionFacets(RestrictionFacets: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmRestrictionFacets)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetRestriction(RestrictionFacet: Windows.Win32.System.SettingsManagementInfrastructure.WcmRestrictionFacets, FacetData: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetKeyValue(Value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsNamespace(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9f7d7bba-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetIdentity(SettingsID: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Settings(Settings: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Save(PushSettings: Windows.Win32.Foundation.BOOL, Result: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSettingByPath(Path: Windows.Win32.Foundation.PWSTR, Setting: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateSettingByPath(Path: Windows.Win32.Foundation.PWSTR, Setting: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveSettingByPath(Path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAttribute(Name: Windows.Win32.Foundation.PWSTR, Value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsResult(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9f7d7bbc-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetDescription(description: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetErrorCode(hrOut: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContextDescription(description: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLine(dwLine: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetColumn(dwColumn: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSource(file: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9f7d7bb8-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetTargetMode(TargetMode: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmTargetMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTargetMode(TargetMode: Windows.Win32.System.SettingsManagementInfrastructure.WcmTargetMode) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTemporaryStoreLocation(TemporaryStoreLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTemporaryStoreLocation(TemporaryStoreLocation: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTargetID(TargetID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetTargetID(TargetID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTargetProcessorArchitecture(ProcessorArchitecture: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetTargetProcessorArchitecture(ProcessorArchitecture: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProperty(Offline: Windows.Win32.Foundation.BOOL, Property: Windows.Win32.Foundation.PWSTR, Value: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetProperty(Offline: Windows.Win32.Foundation.BOOL, Property: Windows.Win32.Foundation.PWSTR, Value: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEnumerator(Enumerator: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ExpandTarget(Offline: Windows.Win32.Foundation.BOOL, Location: Windows.Win32.Foundation.PWSTR, ExpandedLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ExpandTargetPath(Offline: Windows.Win32.Foundation.BOOL, Location: Windows.Win32.Foundation.PWSTR, ExpandedLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetModulePath(Module: Windows.Win32.Foundation.PWSTR, Path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def LoadModule(Module: Windows.Win32.Foundation.PWSTR, ModuleHandle: POINTER(Windows.Win32.Foundation.HINSTANCE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetWow64Context(InstallerModule: Windows.Win32.Foundation.PWSTR, Wow64Context: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def TranslateWow64(ClientArchitecture: Windows.Win32.Foundation.PWSTR, Value: Windows.Win32.Foundation.PWSTR, TranslatedValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetSchemaHiveLocation(pwzHiveDir: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetSchemaHiveLocation(pHiveLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetSchemaHiveMountName(pwzMountName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetSchemaHiveMountName(pMountName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
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
