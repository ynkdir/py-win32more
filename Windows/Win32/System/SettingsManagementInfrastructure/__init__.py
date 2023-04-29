from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.SettingsManagementInfrastructure
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
class IItemEnumerator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9f7d7bb7-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def Current(self, Item: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MoveNext(self, ItemValid: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsContext(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9f7d7bbd-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def Serialize(self, pStream: Windows.Win32.System.Com.IStream_head, pTarget: Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deserialize(self, pStream: Windows.Win32.System.Com.IStream_head, pTarget: Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo_head, pppResults: POINTER(POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsResult_head)), pcResultCount: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetUserData(self, pUserData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUserData(self, pUserData: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNamespaces(self, ppNamespaceIds: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStoredSettings(self, pIdentity: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head, ppAddedSettings: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head), ppModifiedSettings: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head), ppDeletedSettings: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RevertSetting(self, pIdentity: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head, pwzSetting: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsEngine(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9f7d7bb9-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetNamespaces(self, Flags: Windows.Win32.System.SettingsManagementInfrastructure.WcmNamespaceEnumerationFlags, Reserved: c_void_p, Namespaces: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNamespace(self, SettingsID: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head, Access: Windows.Win32.System.SettingsManagementInfrastructure.WcmNamespaceAccess, Reserved: c_void_p, NamespaceItem: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsNamespace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorDescription(self, HResult: Int32, Message: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateSettingsIdentity(self, SettingsID: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStoreStatus(self, Reserved: c_void_p, Status: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmUserStatus)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def LoadStore(self, Flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnloadStore(self, Reserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterNamespace(self, SettingsID: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head, Stream: Windows.Win32.System.Com.IStream_head, PushSettings: Windows.Win32.Foundation.BOOL, Results: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnregisterNamespace(self, SettingsID: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head, RemoveSettings: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateTargetInfo(self, Target: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetTargetInfo(self, Target: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetTargetInfo(self, Target: Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateSettingsContext(self, Flags: UInt32, Reserved: c_void_p, SettingsContext: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetSettingsContext(self, SettingsContext: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ApplySettingsContext(self, SettingsContext: Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext_head, pppwzIdentities: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), pcIdentities: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetSettingsContext(self, SettingsContext: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsIdentity(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9f7d7bb6-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetAttribute(self, Reserved: c_void_p, Name: Windows.Win32.Foundation.PWSTR, Value: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAttribute(self, Reserved: c_void_p, Name: Windows.Win32.Foundation.PWSTR, Value: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFlags(self, Flags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetFlags(self, Flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsItem(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9f7d7bbb-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetName(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(self, Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(self, Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSettingType(self, Type: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmSettingType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDataType(self, Type: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetValueRaw(self, Data: POINTER(POINTER(Byte)), DataSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetValueRaw(self, DataType: Int32, Data: POINTER(Byte), DataSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def HasChild(self, ItemHasChild: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Children(self, Children: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetChild(self, Name: Windows.Win32.Foundation.PWSTR, Child: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSettingByPath(self, Path: Windows.Win32.Foundation.PWSTR, Setting: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateSettingByPath(self, Path: Windows.Win32.Foundation.PWSTR, Setting: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RemoveSettingByPath(self, Path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetListKeyInformation(self, KeyName: POINTER(Windows.Win32.Foundation.BSTR), DataType: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateListElement(self, KeyData: POINTER(Windows.Win32.System.Variant.VARIANT_head), Child: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveListElement(self, ElementName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Attributes(self, Attributes: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetAttribute(self, Name: Windows.Win32.Foundation.PWSTR, Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetPath(self, Path: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetRestrictionFacets(self, RestrictionFacets: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmRestrictionFacets)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetRestriction(self, RestrictionFacet: Windows.Win32.System.SettingsManagementInfrastructure.WcmRestrictionFacets, FacetData: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetKeyValue(self, Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsNamespace(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9f7d7bba-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetIdentity(self, SettingsID: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Settings(self, Settings: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Save(self, PushSettings: Windows.Win32.Foundation.BOOL, Result: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSettingByPath(self, Path: Windows.Win32.Foundation.PWSTR, Setting: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateSettingByPath(self, Path: Windows.Win32.Foundation.PWSTR, Setting: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveSettingByPath(self, Path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAttribute(self, Name: Windows.Win32.Foundation.PWSTR, Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISettingsResult(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9f7d7bbc-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetDescription(self, description: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetErrorCode(self, hrOut: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContextDescription(self, description: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLine(self, dwLine: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetColumn(self, dwColumn: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSource(self, file: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9f7d7bb8-20b3-11da-81-a5-00-30-f1-64-2e-3c')
    @commethod(3)
    def GetTargetMode(self, TargetMode: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.WcmTargetMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTargetMode(self, TargetMode: Windows.Win32.System.SettingsManagementInfrastructure.WcmTargetMode) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTemporaryStoreLocation(self, TemporaryStoreLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTemporaryStoreLocation(self, TemporaryStoreLocation: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTargetID(self, TargetID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetTargetID(self, TargetID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTargetProcessorArchitecture(self, ProcessorArchitecture: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetTargetProcessorArchitecture(self, ProcessorArchitecture: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProperty(self, Offline: Windows.Win32.Foundation.BOOL, Property: Windows.Win32.Foundation.PWSTR, Value: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetProperty(self, Offline: Windows.Win32.Foundation.BOOL, Property: Windows.Win32.Foundation.PWSTR, Value: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEnumerator(self, Enumerator: POINTER(Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ExpandTarget(self, Offline: Windows.Win32.Foundation.BOOL, Location: Windows.Win32.Foundation.PWSTR, ExpandedLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ExpandTargetPath(self, Offline: Windows.Win32.Foundation.BOOL, Location: Windows.Win32.Foundation.PWSTR, ExpandedLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetModulePath(self, Module: Windows.Win32.Foundation.PWSTR, Path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def LoadModule(self, Module: Windows.Win32.Foundation.PWSTR, ModuleHandle: POINTER(Windows.Win32.Foundation.HMODULE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetWow64Context(self, InstallerModule: Windows.Win32.Foundation.PWSTR, Wow64Context: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def TranslateWow64(self, ClientArchitecture: Windows.Win32.Foundation.PWSTR, Value: Windows.Win32.Foundation.PWSTR, TranslatedValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetSchemaHiveLocation(self, pwzHiveDir: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetSchemaHiveLocation(self, pHiveLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetSchemaHiveMountName(self, pwzMountName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetSchemaHiveMountName(self, pMountName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
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
