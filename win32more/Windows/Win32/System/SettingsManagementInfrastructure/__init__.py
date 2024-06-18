from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.SettingsManagementInfrastructure
import win32more.Windows.Win32.System.Variant
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
WCM_E_INTERNALERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145255424
WCM_E_STATENODENOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = -2145255423
WCM_E_STATENODENOTALLOWED: win32more.Windows.Win32.Foundation.HRESULT = -2145255422
WCM_E_ATTRIBUTENOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = -2145255421
WCM_E_ATTRIBUTENOTALLOWED: win32more.Windows.Win32.Foundation.HRESULT = -2145255420
WCM_E_INVALIDVALUE: win32more.Windows.Win32.Foundation.HRESULT = -2145255419
WCM_E_INVALIDVALUEFORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2145255418
WCM_E_TYPENOTSPECIFIED: win32more.Windows.Win32.Foundation.HRESULT = -2145255417
WCM_E_INVALIDDATATYPE: win32more.Windows.Win32.Foundation.HRESULT = -2145255416
WCM_E_NOTPOSITIONED: win32more.Windows.Win32.Foundation.HRESULT = -2145255415
WCM_E_READONLYITEM: win32more.Windows.Win32.Foundation.HRESULT = -2145255414
WCM_E_INVALIDPATH: win32more.Windows.Win32.Foundation.HRESULT = -2145255413
WCM_E_WRONGESCAPESTRING: win32more.Windows.Win32.Foundation.HRESULT = -2145255412
WCM_E_INVALIDVERSIONFORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2145255411
WCM_E_INVALIDLANGUAGEFORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2145255410
WCM_E_KEYNOTCHANGEABLE: win32more.Windows.Win32.Foundation.HRESULT = -2145255409
WCM_E_EXPRESSIONNOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = -2145255408
WCM_E_SUBSTITUTIONNOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = -2145255407
WCM_E_USERALREADYREGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -2145255406
WCM_E_USERNOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = -2145255405
WCM_E_NAMESPACENOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = -2145255404
WCM_E_NAMESPACEALREADYREGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -2145255403
WCM_E_STORECORRUPTED: win32more.Windows.Win32.Foundation.HRESULT = -2145255402
WCM_E_INVALIDEXPRESSIONSYNTAX: win32more.Windows.Win32.Foundation.HRESULT = -2145255401
WCM_E_NOTIFICATIONNOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = -2145255400
WCM_E_CONFLICTINGASSERTION: win32more.Windows.Win32.Foundation.HRESULT = -2145255399
WCM_E_ASSERTIONFAILED: win32more.Windows.Win32.Foundation.HRESULT = -2145255398
WCM_E_DUPLICATENAME: win32more.Windows.Win32.Foundation.HRESULT = -2145255397
WCM_E_INVALIDKEY: win32more.Windows.Win32.Foundation.HRESULT = -2145255396
WCM_E_INVALIDSTREAM: win32more.Windows.Win32.Foundation.HRESULT = -2145255395
WCM_E_HANDLERNOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = -2145255394
WCM_E_INVALIDHANDLERSYNTAX: win32more.Windows.Win32.Foundation.HRESULT = -2145255393
WCM_E_VALIDATIONFAILED: win32more.Windows.Win32.Foundation.HRESULT = -2145255392
WCM_E_RESTRICTIONFAILED: win32more.Windows.Win32.Foundation.HRESULT = -2145255391
WCM_E_MANIFESTCOMPILATIONFAILED: win32more.Windows.Win32.Foundation.HRESULT = -2145255390
WCM_E_CYCLICREFERENCE: win32more.Windows.Win32.Foundation.HRESULT = -2145255389
WCM_E_MIXTYPEASSERTION: win32more.Windows.Win32.Foundation.HRESULT = -2145255388
WCM_E_NOTSUPPORTEDFUNCTION: win32more.Windows.Win32.Foundation.HRESULT = -2145255387
WCM_E_VALUETOOBIG: win32more.Windows.Win32.Foundation.HRESULT = -2145255386
WCM_E_INVALIDATTRIBUTECOMBINATION: win32more.Windows.Win32.Foundation.HRESULT = -2145255385
WCM_E_ABORTOPERATION: win32more.Windows.Win32.Foundation.HRESULT = -2145255384
WCM_E_MISSINGCONFIGURATION: win32more.Windows.Win32.Foundation.HRESULT = -2145255383
WCM_E_INVALIDPROCESSORFORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2145255382
WCM_E_SOURCEMANEMPTYVALUE: win32more.Windows.Win32.Foundation.HRESULT = -2145255381
WCM_S_INTERNALERROR: win32more.Windows.Win32.Foundation.HRESULT = 2232320
WCM_S_ATTRIBUTENOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = 2232321
WCM_S_LEGACYSETTINGWARNING: win32more.Windows.Win32.Foundation.HRESULT = 2232322
WCM_S_INVALIDATTRIBUTECOMBINATION: win32more.Windows.Win32.Foundation.HRESULT = 2232324
WCM_S_ATTRIBUTENOTALLOWED: win32more.Windows.Win32.Foundation.HRESULT = 2232325
WCM_S_NAMESPACENOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = 2232326
WCM_E_UNKNOWNRESULT: win32more.Windows.Win32.Foundation.HRESULT = -2145251325
class IItemEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f7d7bb7-20b3-11da-81a5-0030f1642e3c}')
    @commethod(3)
    def Current(self, Item: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MoveNext(self, ItemValid: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISettingsContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f7d7bbd-20b3-11da-81a5-0030f1642e3c}')
    @commethod(3)
    def Serialize(self, pStream: win32more.Windows.Win32.System.Com.IStream, pTarget: win32more.Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deserialize(self, pStream: win32more.Windows.Win32.System.Com.IStream, pTarget: win32more.Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo, pppResults: POINTER(POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsResult)), pcResultCount: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetUserData(self, pUserData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUserData(self, pUserData: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNamespaces(self, ppNamespaceIds: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStoredSettings(self, pIdentity: win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity, ppAddedSettings: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator), ppModifiedSettings: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator), ppDeletedSettings: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RevertSetting(self, pIdentity: win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity, pwzSetting: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISettingsEngine(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f7d7bb9-20b3-11da-81a5-0030f1642e3c}')
    @commethod(3)
    def GetNamespaces(self, Flags: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmNamespaceEnumerationFlags, Reserved: VoidPtr, Namespaces: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNamespace(self, SettingsID: win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity, Access: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmNamespaceAccess, Reserved: VoidPtr, NamespaceItem: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsNamespace)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorDescription(self, HResult: Int32, Message: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateSettingsIdentity(self, SettingsID: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStoreStatus(self, Reserved: VoidPtr, Status: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmUserStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def LoadStore(self, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnloadStore(self, Reserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterNamespace(self, SettingsID: win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity, Stream: win32more.Windows.Win32.System.Com.IStream, PushSettings: win32more.Windows.Win32.Foundation.BOOL, Results: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnregisterNamespace(self, SettingsID: win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity, RemoveSettings: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateTargetInfo(self, Target: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetTargetInfo(self, Target: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetTargetInfo(self, Target: win32more.Windows.Win32.System.SettingsManagementInfrastructure.ITargetInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateSettingsContext(self, Flags: UInt32, Reserved: VoidPtr, SettingsContext: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetSettingsContext(self, SettingsContext: win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ApplySettingsContext(self, SettingsContext: win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext, pppwzIdentities: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), pcIdentities: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetSettingsContext(self, SettingsContext: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISettingsIdentity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f7d7bb6-20b3-11da-81a5-0030f1642e3c}')
    @commethod(3)
    def GetAttribute(self, Reserved: VoidPtr, Name: win32more.Windows.Win32.Foundation.PWSTR, Value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAttribute(self, Reserved: VoidPtr, Name: win32more.Windows.Win32.Foundation.PWSTR, Value: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFlags(self, Flags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetFlags(self, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISettingsItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f7d7bbb-20b3-11da-81a5-0030f1642e3c}')
    @commethod(3)
    def GetName(self, Name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(self, Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(self, Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSettingType(self, Type: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmSettingType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDataType(self, Type: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetValueRaw(self, Data: POINTER(POINTER(Byte)), DataSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetValueRaw(self, DataType: Int32, Data: POINTER(Byte), DataSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def HasChild(self, ItemHasChild: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Children(self, Children: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetChild(self, Name: win32more.Windows.Win32.Foundation.PWSTR, Child: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSettingByPath(self, Path: win32more.Windows.Win32.Foundation.PWSTR, Setting: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateSettingByPath(self, Path: win32more.Windows.Win32.Foundation.PWSTR, Setting: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RemoveSettingByPath(self, Path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetListKeyInformation(self, KeyName: POINTER(win32more.Windows.Win32.Foundation.BSTR), DataType: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateListElement(self, KeyData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Child: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveListElement(self, ElementName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Attributes(self, Attributes: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetAttribute(self, Name: win32more.Windows.Win32.Foundation.PWSTR, Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetPath(self, Path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetRestrictionFacets(self, RestrictionFacets: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmRestrictionFacets)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetRestriction(self, RestrictionFacet: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmRestrictionFacets, FacetData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetKeyValue(self, Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISettingsNamespace(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f7d7bba-20b3-11da-81a5-0030f1642e3c}')
    @commethod(3)
    def GetIdentity(self, SettingsID: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsIdentity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Settings(self, Settings: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Save(self, PushSettings: win32more.Windows.Win32.Foundation.BOOL, Result: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSettingByPath(self, Path: win32more.Windows.Win32.Foundation.PWSTR, Setting: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateSettingByPath(self, Path: win32more.Windows.Win32.Foundation.PWSTR, Setting: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.ISettingsItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveSettingByPath(self, Path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAttribute(self, Name: win32more.Windows.Win32.Foundation.PWSTR, Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISettingsResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f7d7bbc-20b3-11da-81a5-0030f1642e3c}')
    @commethod(3)
    def GetDescription(self, description: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetErrorCode(self, hrOut: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContextDescription(self, description: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLine(self, dwLine: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetColumn(self, dwColumn: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSource(self, file: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITargetInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f7d7bb8-20b3-11da-81a5-0030f1642e3c}')
    @commethod(3)
    def GetTargetMode(self, TargetMode: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmTargetMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTargetMode(self, TargetMode: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmTargetMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTemporaryStoreLocation(self, TemporaryStoreLocation: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTemporaryStoreLocation(self, TemporaryStoreLocation: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTargetID(self, TargetID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetTargetID(self, TargetID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTargetProcessorArchitecture(self, ProcessorArchitecture: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetTargetProcessorArchitecture(self, ProcessorArchitecture: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProperty(self, Offline: win32more.Windows.Win32.Foundation.BOOL, Property: win32more.Windows.Win32.Foundation.PWSTR, Value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetProperty(self, Offline: win32more.Windows.Win32.Foundation.BOOL, Property: win32more.Windows.Win32.Foundation.PWSTR, Value: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEnumerator(self, Enumerator: POINTER(win32more.Windows.Win32.System.SettingsManagementInfrastructure.IItemEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ExpandTarget(self, Offline: win32more.Windows.Win32.Foundation.BOOL, Location: win32more.Windows.Win32.Foundation.PWSTR, ExpandedLocation: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ExpandTargetPath(self, Offline: win32more.Windows.Win32.Foundation.BOOL, Location: win32more.Windows.Win32.Foundation.PWSTR, ExpandedLocation: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetModulePath(self, Module: win32more.Windows.Win32.Foundation.PWSTR, Path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def LoadModule(self, Module: win32more.Windows.Win32.Foundation.PWSTR, ModuleHandle: POINTER(win32more.Windows.Win32.Foundation.HMODULE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetWow64Context(self, InstallerModule: win32more.Windows.Win32.Foundation.PWSTR, Wow64Context: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def TranslateWow64(self, ClientArchitecture: win32more.Windows.Win32.Foundation.PWSTR, Value: win32more.Windows.Win32.Foundation.PWSTR, TranslatedValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetSchemaHiveLocation(self, pwzHiveDir: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetSchemaHiveLocation(self, pHiveLocation: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetSchemaHiveMountName(self, pwzMountName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetSchemaHiveMountName(self, pMountName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SettingsEngine = Guid('{9f7d7bb5-20b3-11da-81a5-0030f1642e3c}')
WcmDataType = Int32
dataTypeByte: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType = 1
dataTypeSByte: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType = 2
dataTypeUInt16: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType = 3
dataTypeInt16: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType = 4
dataTypeUInt32: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType = 5
dataTypeInt32: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType = 6
dataTypeUInt64: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType = 7
dataTypeInt64: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType = 8
dataTypeBoolean: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType = 11
dataTypeString: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType = 12
dataTypeFlagArray: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmDataType = 32768
WcmNamespaceAccess = Int32
ReadOnlyAccess: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmNamespaceAccess = 1
ReadWriteAccess: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmNamespaceAccess = 2
WcmNamespaceEnumerationFlags = Int32
SharedEnumeration: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmNamespaceEnumerationFlags = 1
UserEnumeration: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmNamespaceEnumerationFlags = 2
AllEnumeration: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmNamespaceEnumerationFlags = 3
WcmRestrictionFacets = Int32
restrictionFacetMaxLength: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmRestrictionFacets = 1
restrictionFacetEnumeration: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmRestrictionFacets = 2
restrictionFacetMaxInclusive: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmRestrictionFacets = 4
restrictionFacetMinInclusive: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmRestrictionFacets = 8
WcmSettingType = Int32
settingTypeScalar: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmSettingType = 1
settingTypeComplex: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmSettingType = 2
settingTypeList: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmSettingType = 3
WcmTargetMode = Int32
OfflineMode: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmTargetMode = 1
OnlineMode: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmTargetMode = 2
WcmUserStatus = Int32
UnknownStatus: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmUserStatus = 0
UserRegistered: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmUserStatus = 1
UserUnregistered: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmUserStatus = 2
UserLoaded: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmUserStatus = 3
UserUnloaded: win32more.Windows.Win32.System.SettingsManagementInfrastructure.WcmUserStatus = 4


make_ready(__name__)
