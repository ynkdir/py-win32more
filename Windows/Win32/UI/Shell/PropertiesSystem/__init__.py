from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.Search.Common
import Windows.Win32.System.Variant
import Windows.Win32.UI.Shell.Common
import Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
PKEY_PIDSTR_MAX: UInt32 = 10
@winfunctype('PROPSYS.dll')
def PSFormatForDisplay(propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pdfFlags: Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, pwszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSFormatForDisplayAlloc(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pdff: Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSFormatPropertyValue(pps: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, ppd: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription_head, pdff: Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetImageReferenceForValue(propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppszImageRes: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSStringFromPropertyKey(pkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), psz: Windows.Win32.Foundation.PWSTR, cch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyKeyFromString(pszString: Windows.Win32.Foundation.PWSTR, pkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateMemoryPropertyStore(riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateDelayedMultiplexPropertyStore(flags: Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, pdpsf: Windows.Win32.UI.Shell.PropertiesSystem.IDelayedPropertyStoreFactory_head, rgStoreIds: POINTER(UInt32), cStores: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateMultiplexPropertyStore(prgpunkStores: POINTER(Windows.Win32.System.Com.IUnknown_head), cStores: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreatePropertyChangeArray(rgpropkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), rgflags: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PKA_FLAGS), rgpropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), cChanges: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateSimplePropertyChange(flags: Windows.Win32.UI.Shell.PropertiesSystem.PKA_FLAGS, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyDescription(propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyDescriptionByName(pszCanonicalName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSLookupPropertyHandlerCLSID(pszFilePath: Windows.Win32.Foundation.PWSTR, pclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetItemPropertyHandler(punkItem: Windows.Win32.System.Com.IUnknown_head, fReadWrite: Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetItemPropertyHandlerWithCreateObject(punkItem: Windows.Win32.System.Com.IUnknown_head, fReadWrite: Windows.Win32.Foundation.BOOL, punkCreateObject: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyValue(pps: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, ppd: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription_head, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSSetPropertyValue(pps: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, ppd: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription_head, propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSRegisterPropertySchema(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSUnregisterPropertySchema(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSRefreshPropertySchema() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSEnumeratePropertyDescriptions(filterOn: Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyKeyFromName(pszName: Windows.Win32.Foundation.PWSTR, ppropkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetNameFromPropertyKey(propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppszCanonicalName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCoerceToCanonicalValue(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyDescriptionListFromString(pszPropList: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreatePropertyStoreFromPropertySetStorage(ppss: Windows.Win32.System.Com.StructuredStorage.IPropertySetStorage_head, grfMode: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreatePropertyStoreFromObject(punk: Windows.Win32.System.Com.IUnknown_head, grfMode: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateAdapterFromPropertyStore(pps: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertySystem(riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyFromPropertyStorage(psps: Windows.Win32.UI.Shell.PropertiesSystem.PCUSERIALIZEDPROPSTORAGE, cb: UInt32, rpkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetNamedPropertyFromPropertyStorage(psps: Windows.Win32.UI.Shell.PropertiesSystem.PCUSERIALIZEDPROPSTORAGE, cb: UInt32, pszName: Windows.Win32.Foundation.PWSTR, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadType(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, var: POINTER(Windows.Win32.System.Variant.VARIANT_head), type: Windows.Win32.System.Variant.VARENUM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadStr(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: Windows.Win32.Foundation.PWSTR, characterCount: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadStrAlloc(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadBSTR(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteStr(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteBSTR(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadInt(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteInt(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadSHORT(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteSHORT(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: Int16) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadLONG(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteLONG(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadDWORD(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteDWORD(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadBOOL(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteBOOL(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadPOINTL(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.POINTL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WritePOINTL(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.POINTL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadPOINTS(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.POINTS_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WritePOINTS(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.POINTS_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadRECTL(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.RECTL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteRECTL(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.RECTL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadStream(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteStream(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_Delete(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadULONGLONG(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteULONGLONG(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadUnknown(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteUnknown(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadGUID(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteGUID(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadPropertyKey(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WritePropertyKey(propBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, propName: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetPropertyStoreFromIDList(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), flags: Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetPropertyStoreFromParsingName(pszPath: Windows.Win32.Foundation.PWSTR, pbc: Windows.Win32.System.Com.IBindCtx_head, flags: Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHAddDefaultPropertiesByExt(pszExt: Windows.Win32.Foundation.PWSTR, pPropStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def PifMgr_OpenProperties(pszApp: Windows.Win32.Foundation.PWSTR, pszPIF: Windows.Win32.Foundation.PWSTR, hInf: UInt32, flOpt: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('SHELL32.dll')
def PifMgr_GetProperties(hProps: Windows.Win32.Foundation.HANDLE, pszGroup: Windows.Win32.Foundation.PSTR, lpProps: VoidPtr, cbProps: Int32, flOpt: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def PifMgr_SetProperties(hProps: Windows.Win32.Foundation.HANDLE, pszGroup: Windows.Win32.Foundation.PSTR, lpProps: VoidPtr, cbProps: Int32, flOpt: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def PifMgr_CloseProperties(hProps: Windows.Win32.Foundation.HANDLE, flOpt: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('SHELL32.dll')
def SHPropStgCreate(psstg: Windows.Win32.System.Com.StructuredStorage.IPropertySetStorage_head, fmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, grfMode: UInt32, dwDisposition: UInt32, ppstg: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head), puCodePage: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHPropStgReadMultiple(pps: Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head, uCodePage: UInt32, cpspec: UInt32, rgpspec: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPSPEC_head), rgvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHPropStgWriteMultiple(pps: Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head, puCodePage: POINTER(UInt32), cpspec: UInt32, rgpspec: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPSPEC_head), rgvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), propidNameFirst: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetPropertyStoreForWindow(hwnd: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
GETPROPERTYSTOREFLAGS = Int32
GPS_DEFAULT: GETPROPERTYSTOREFLAGS = 0
GPS_HANDLERPROPERTIESONLY: GETPROPERTYSTOREFLAGS = 1
GPS_READWRITE: GETPROPERTYSTOREFLAGS = 2
GPS_TEMPORARY: GETPROPERTYSTOREFLAGS = 4
GPS_FASTPROPERTIESONLY: GETPROPERTYSTOREFLAGS = 8
GPS_OPENSLOWITEM: GETPROPERTYSTOREFLAGS = 16
GPS_DELAYCREATION: GETPROPERTYSTOREFLAGS = 32
GPS_BESTEFFORT: GETPROPERTYSTOREFLAGS = 64
GPS_NO_OPLOCK: GETPROPERTYSTOREFLAGS = 128
GPS_PREFERQUERYPROPERTIES: GETPROPERTYSTOREFLAGS = 256
GPS_EXTRINSICPROPERTIES: GETPROPERTYSTOREFLAGS = 512
GPS_EXTRINSICPROPERTIESONLY: GETPROPERTYSTOREFLAGS = 1024
GPS_VOLATILEPROPERTIES: GETPROPERTYSTOREFLAGS = 2048
GPS_VOLATILEPROPERTIESONLY: GETPROPERTYSTOREFLAGS = 4096
GPS_MASK_VALID: GETPROPERTYSTOREFLAGS = 8191
class ICreateObject(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75121952-e0d0-43e5-9380-1d80483acf72}')
    @commethod(3)
    def CreateObject(self, clsid: POINTER(Guid), pUnkOuter: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IDelayedPropertyStoreFactory(ComPtr):
    extends: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStoreFactory
    _iid_ = Guid('{40d4577f-e237-4bdb-bd69-58f089431b6a}')
    @commethod(5)
    def GetDelayedPropertyStore(self, flags: Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, dwStoreId: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithFile(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b7d14566-0509-4cce-a71f-0a554233bd9b}')
    @commethod(3)
    def Initialize(self, pszFilePath: Windows.Win32.Foundation.PWSTR, grfMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithStream(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b824b49d-22ac-4161-ac8a-9916e8fa3f7f}')
    @commethod(3)
    def Initialize(self, pstream: Windows.Win32.System.Com.IStream_head, grfMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class INamedPropertyStore(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71604b0f-97b0-4764-8577-2f13e98a1422}')
    @commethod(3)
    def GetNamedValue(self, pszName: Windows.Win32.Foundation.PWSTR, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetNamedValue(self, pszName: Windows.Win32.Foundation.PWSTR, propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNameCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNameAt(self, iProp: UInt32, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectWithPropertyKey(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc0ca0a7-c316-4fd2-9031-3e628e6d4f23}')
    @commethod(3)
    def SetPropertyKey(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyKey(self, pkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistSerializedPropStorage(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e318ad57-0aa0-450f-aca5-6fab7103d917}')
    @commethod(3)
    def SetFlags(self, flags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPropertyStorage(self, psps: Windows.Win32.UI.Shell.PropertiesSystem.PCUSERIALIZEDPROPSTORAGE, cb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyStorage(self, ppsps: POINTER(POINTER(Windows.Win32.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE)), pcb: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistSerializedPropStorage2(ComPtr):
    extends: Windows.Win32.UI.Shell.PropertiesSystem.IPersistSerializedPropStorage
    _iid_ = Guid('{77effa68-4f98-4366-ba72-573b3d880571}')
    @commethod(6)
    def GetPropertyStorageSize(self, pcb: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPropertyStorageBuffer(self, psps: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE), cb: UInt32, pcbWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyChange(ComPtr):
    extends: Windows.Win32.UI.Shell.PropertiesSystem.IObjectWithPropertyKey
    _iid_ = Guid('{f917bc8a-1bba-4478-a245-1bde03eb9431}')
    @commethod(5)
    def ApplyToPropVariant(self, propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppropvarOut: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyChangeArray(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{380f5cad-1b5e-42f2-805d-637fd392d31e}')
    @commethod(3)
    def GetCount(self, pcOperations: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, iIndex: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(self, iIndex: UInt32, ppropChange: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyChange_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Append(self, ppropChange: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyChange_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AppendOrReplace(self, ppropChange: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyChange_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveAt(self, iIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsKeyInArray(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescription(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6f79d558-3e96-4549-a1d1-7d75d2288814}')
    @commethod(3)
    def GetPropertyKey(self, pkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCanonicalName(self, ppszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyType(self, pvartype: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDisplayName(self, ppszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEditInvitation(self, ppszInvite: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTypeFlags(self, mask: Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS, ppdtFlags: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetViewFlags(self, ppdvFlags: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDefaultColumnWidth(self, pcxChars: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDisplayType(self, pdisplaytype: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_DISPLAYTYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetColumnState(self, pcsFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetGroupingRange(self, pgr: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRelativeDescriptionType(self, prdt: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRelativeDescription(self, propvar1: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), propvar2: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppszDesc1: POINTER(Windows.Win32.Foundation.PWSTR), ppszDesc2: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSortDescription(self, psd: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SORTDESCRIPTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetSortDescriptionLabel(self, fDescending: Windows.Win32.Foundation.BOOL, ppszDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetAggregationType(self, paggtype: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetConditionType(self, pcontype: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_CONDITION_TYPE), popDefault: POINTER(Windows.Win32.System.Search.Common.CONDITION_OPERATION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetEnumTypeList(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CoerceToCanonicalValue(self, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def FormatForDisplay(self, propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pdfFlags: Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def IsValueCanonical(self, propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescription2(ComPtr):
    extends: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription
    _iid_ = Guid('{57d2eded-5062-400e-b107-5dae79fe57a6}')
    @commethod(24)
    def GetImageReferenceForValue(self, propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppszImageRes: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescriptionAliasInfo(ComPtr):
    extends: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription
    _iid_ = Guid('{f67104fc-2af9-46fd-b32d-243c1404f3d1}')
    @commethod(24)
    def GetSortByAlias(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetAdditionalSortByAliases(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescriptionList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1f9fc1d0-c39b-4b26-817f-011967d3440e}')
    @commethod(3)
    def GetCount(self, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, iElem: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescriptionRelatedPropertyInfo(ComPtr):
    extends: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription
    _iid_ = Guid('{507393f4-2a3d-4a60-b59e-d9c75716c2dd}')
    @commethod(24)
    def GetRelatedProperty(self, pszRelationshipName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescriptionSearchInfo(ComPtr):
    extends: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription
    _iid_ = Guid('{078f91bd-29a2-440f-924e-46a291524520}')
    @commethod(24)
    def GetSearchInfoFlags(self, ppdsiFlags: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SEARCHINFO_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetColumnIndexType(self, ppdciType: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_COLUMNINDEX_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetProjectionString(self, ppszProjection: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetMaxSize(self, pcbMaxSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyEnumType(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11e1fbf9-2d56-4a6b-8db3-7cd193a471f2}')
    @commethod(3)
    def GetEnumType(self, penumtype: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPENUMTYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(self, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRangeMinValue(self, ppropvarMin: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRangeSetValue(self, ppropvarSet: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDisplayText(self, ppszDisplay: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyEnumType2(ComPtr):
    extends: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyEnumType
    _iid_ = Guid('{9b6e051c-5ddd-4321-9070-fe2acb55e794}')
    @commethod(8)
    def GetImageReference(self, ppszImageRes: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyEnumTypeList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a99400f4-3d84-4557-94ba-1242fb2cc9a6}')
    @commethod(3)
    def GetCount(self, pctypes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, itype: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetConditionAt(self, nIndex: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindMatchingIndex(self, propvarCmp: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pnIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyStore(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{886d8eeb-8cf2-4446-8d02-cdba1dbdcf99}')
    @commethod(3)
    def GetCount(self, cProps: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, iProp: UInt32, pkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pv: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Commit(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyStoreCache(ComPtr):
    extends: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    _iid_ = Guid('{3017056d-9a91-4e90-937d-746c72abbf4f}')
    @commethod(8)
    def GetState(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pstate: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetValueAndState(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pstate: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetState(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), state: Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetValueAndState(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), state: Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyStoreCapabilities(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8e2d566-186e-4d49-bf41-6909ead56acc}')
    @commethod(3)
    def IsPropertyWritable(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyStoreFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bc110b6d-57e8-4148-a9c6-91015ab2f3a5}')
    @commethod(3)
    def GetPropertyStore(self, flags: Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, pUnkFactory: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyStoreForKeys(self, rgKeys: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), cKeys: UInt32, flags: Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertySystem(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ca724e8a-c3e6-442b-88a4-6fb0db8035a3}')
    @commethod(3)
    def GetPropertyDescription(self, propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyDescriptionByName(self, pszCanonicalName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyDescriptionListFromString(self, pszPropList: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumeratePropertyDescriptions(self, filterOn: Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FormatForDisplay(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pdff: Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, pszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FormatForDisplayAlloc(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pdff: Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterPropertySchema(self, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnregisterPropertySchema(self, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RefreshPropertySchema(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertySystemChangeNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fa955fd9-38be-4879-a6ce-824cf52d609f}')
    @commethod(3)
    def SchemaRefreshed(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyUI(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{757a7d9f-919a-4118-99d7-dbb208c8cc66}')
    @commethod(3)
    def ParsePropertyName(self, pszName: Windows.Win32.Foundation.PWSTR, pfmtid: POINTER(Guid), ppid: POINTER(UInt32), pchEaten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCannonicalName(self, fmtid: POINTER(Guid), pid: UInt32, pwszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDisplayName(self, fmtid: POINTER(Guid), pid: UInt32, flags: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_NAME_FLAGS, pwszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyDescription(self, fmtid: POINTER(Guid), pid: UInt32, pwszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDefaultWidth(self, fmtid: POINTER(Guid), pid: UInt32, pcxChars: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFlags(self, fmtid: POINTER(Guid), pid: UInt32, pflags: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def FormatForDisplay(self, fmtid: POINTER(Guid), pid: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), puiff: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FORMAT_FLAGS, pwszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetHelpInfo(self, fmtid: POINTER(Guid), pid: UInt32, pwszHelpFile: Windows.Win32.Foundation.PWSTR, cch: UInt32, puHelpID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
InMemoryPropertyStore = Guid('{9a02e012-6303-4e1e-b9a1-630f802592c5}')
InMemoryPropertyStoreMarshalByValue = Guid('{d4ca0e2d-6da7-4b75-a97c-5f306f0eaedc}')
PCUSERIALIZEDPROPSTORAGE = IntPtr
PDOPSTATUS = Int32
PDOPS_RUNNING: PDOPSTATUS = 1
PDOPS_PAUSED: PDOPSTATUS = 2
PDOPS_CANCELLED: PDOPSTATUS = 3
PDOPS_STOPPED: PDOPSTATUS = 4
PDOPS_ERRORS: PDOPSTATUS = 5
PKA_FLAGS = Int32
PKA_SET: PKA_FLAGS = 0
PKA_APPEND: PKA_FLAGS = 1
PKA_DELETE: PKA_FLAGS = 2
PLACEHOLDER_STATES = Int32
PS_NONE: PLACEHOLDER_STATES = 0
PS_MARKED_FOR_OFFLINE_AVAILABILITY: PLACEHOLDER_STATES = 1
PS_FULL_PRIMARY_STREAM_AVAILABLE: PLACEHOLDER_STATES = 2
PS_CREATE_FILE_ACCESSIBLE: PLACEHOLDER_STATES = 4
PS_CLOUDFILE_PLACEHOLDER: PLACEHOLDER_STATES = 8
PS_DEFAULT: PLACEHOLDER_STATES = 7
PS_ALL: PLACEHOLDER_STATES = 15
PROPDESC_AGGREGATION_TYPE = Int32
PDAT_DEFAULT: PROPDESC_AGGREGATION_TYPE = 0
PDAT_FIRST: PROPDESC_AGGREGATION_TYPE = 1
PDAT_SUM: PROPDESC_AGGREGATION_TYPE = 2
PDAT_AVERAGE: PROPDESC_AGGREGATION_TYPE = 3
PDAT_DATERANGE: PROPDESC_AGGREGATION_TYPE = 4
PDAT_UNION: PROPDESC_AGGREGATION_TYPE = 5
PDAT_MAX: PROPDESC_AGGREGATION_TYPE = 6
PDAT_MIN: PROPDESC_AGGREGATION_TYPE = 7
PROPDESC_COLUMNINDEX_TYPE = Int32
PDCIT_NONE: PROPDESC_COLUMNINDEX_TYPE = 0
PDCIT_ONDISK: PROPDESC_COLUMNINDEX_TYPE = 1
PDCIT_INMEMORY: PROPDESC_COLUMNINDEX_TYPE = 2
PDCIT_ONDEMAND: PROPDESC_COLUMNINDEX_TYPE = 3
PDCIT_ONDISKALL: PROPDESC_COLUMNINDEX_TYPE = 4
PDCIT_ONDISKVECTOR: PROPDESC_COLUMNINDEX_TYPE = 5
PROPDESC_CONDITION_TYPE = Int32
PDCOT_NONE: PROPDESC_CONDITION_TYPE = 0
PDCOT_STRING: PROPDESC_CONDITION_TYPE = 1
PDCOT_SIZE: PROPDESC_CONDITION_TYPE = 2
PDCOT_DATETIME: PROPDESC_CONDITION_TYPE = 3
PDCOT_BOOLEAN: PROPDESC_CONDITION_TYPE = 4
PDCOT_NUMBER: PROPDESC_CONDITION_TYPE = 5
PROPDESC_DISPLAYTYPE = Int32
PDDT_STRING: PROPDESC_DISPLAYTYPE = 0
PDDT_NUMBER: PROPDESC_DISPLAYTYPE = 1
PDDT_BOOLEAN: PROPDESC_DISPLAYTYPE = 2
PDDT_DATETIME: PROPDESC_DISPLAYTYPE = 3
PDDT_ENUMERATED: PROPDESC_DISPLAYTYPE = 4
PROPDESC_ENUMFILTER = Int32
PDEF_ALL: PROPDESC_ENUMFILTER = 0
PDEF_SYSTEM: PROPDESC_ENUMFILTER = 1
PDEF_NONSYSTEM: PROPDESC_ENUMFILTER = 2
PDEF_VIEWABLE: PROPDESC_ENUMFILTER = 3
PDEF_QUERYABLE: PROPDESC_ENUMFILTER = 4
PDEF_INFULLTEXTQUERY: PROPDESC_ENUMFILTER = 5
PDEF_COLUMN: PROPDESC_ENUMFILTER = 6
PROPDESC_FORMAT_FLAGS = Int32
PDFF_DEFAULT: PROPDESC_FORMAT_FLAGS = 0
PDFF_PREFIXNAME: PROPDESC_FORMAT_FLAGS = 1
PDFF_FILENAME: PROPDESC_FORMAT_FLAGS = 2
PDFF_ALWAYSKB: PROPDESC_FORMAT_FLAGS = 4
PDFF_RESERVED_RIGHTTOLEFT: PROPDESC_FORMAT_FLAGS = 8
PDFF_SHORTTIME: PROPDESC_FORMAT_FLAGS = 16
PDFF_LONGTIME: PROPDESC_FORMAT_FLAGS = 32
PDFF_HIDETIME: PROPDESC_FORMAT_FLAGS = 64
PDFF_SHORTDATE: PROPDESC_FORMAT_FLAGS = 128
PDFF_LONGDATE: PROPDESC_FORMAT_FLAGS = 256
PDFF_HIDEDATE: PROPDESC_FORMAT_FLAGS = 512
PDFF_RELATIVEDATE: PROPDESC_FORMAT_FLAGS = 1024
PDFF_USEEDITINVITATION: PROPDESC_FORMAT_FLAGS = 2048
PDFF_READONLY: PROPDESC_FORMAT_FLAGS = 4096
PDFF_NOAUTOREADINGORDER: PROPDESC_FORMAT_FLAGS = 8192
PROPDESC_GROUPING_RANGE = Int32
PDGR_DISCRETE: PROPDESC_GROUPING_RANGE = 0
PDGR_ALPHANUMERIC: PROPDESC_GROUPING_RANGE = 1
PDGR_SIZE: PROPDESC_GROUPING_RANGE = 2
PDGR_DYNAMIC: PROPDESC_GROUPING_RANGE = 3
PDGR_DATE: PROPDESC_GROUPING_RANGE = 4
PDGR_PERCENT: PROPDESC_GROUPING_RANGE = 5
PDGR_ENUMERATED: PROPDESC_GROUPING_RANGE = 6
PROPDESC_RELATIVEDESCRIPTION_TYPE = Int32
PDRDT_GENERAL: PROPDESC_RELATIVEDESCRIPTION_TYPE = 0
PDRDT_DATE: PROPDESC_RELATIVEDESCRIPTION_TYPE = 1
PDRDT_SIZE: PROPDESC_RELATIVEDESCRIPTION_TYPE = 2
PDRDT_COUNT: PROPDESC_RELATIVEDESCRIPTION_TYPE = 3
PDRDT_REVISION: PROPDESC_RELATIVEDESCRIPTION_TYPE = 4
PDRDT_LENGTH: PROPDESC_RELATIVEDESCRIPTION_TYPE = 5
PDRDT_DURATION: PROPDESC_RELATIVEDESCRIPTION_TYPE = 6
PDRDT_SPEED: PROPDESC_RELATIVEDESCRIPTION_TYPE = 7
PDRDT_RATE: PROPDESC_RELATIVEDESCRIPTION_TYPE = 8
PDRDT_RATING: PROPDESC_RELATIVEDESCRIPTION_TYPE = 9
PDRDT_PRIORITY: PROPDESC_RELATIVEDESCRIPTION_TYPE = 10
PROPDESC_SEARCHINFO_FLAGS = Int32
PDSIF_DEFAULT: PROPDESC_SEARCHINFO_FLAGS = 0
PDSIF_ININVERTEDINDEX: PROPDESC_SEARCHINFO_FLAGS = 1
PDSIF_ISCOLUMN: PROPDESC_SEARCHINFO_FLAGS = 2
PDSIF_ISCOLUMNSPARSE: PROPDESC_SEARCHINFO_FLAGS = 4
PDSIF_ALWAYSINCLUDE: PROPDESC_SEARCHINFO_FLAGS = 8
PDSIF_USEFORTYPEAHEAD: PROPDESC_SEARCHINFO_FLAGS = 16
PROPDESC_SORTDESCRIPTION = Int32
PDSD_GENERAL: PROPDESC_SORTDESCRIPTION = 0
PDSD_A_Z: PROPDESC_SORTDESCRIPTION = 1
PDSD_LOWEST_HIGHEST: PROPDESC_SORTDESCRIPTION = 2
PDSD_SMALLEST_BIGGEST: PROPDESC_SORTDESCRIPTION = 3
PDSD_OLDEST_NEWEST: PROPDESC_SORTDESCRIPTION = 4
PROPDESC_TYPE_FLAGS = UInt32
PDTF_DEFAULT: PROPDESC_TYPE_FLAGS = 0
PDTF_MULTIPLEVALUES: PROPDESC_TYPE_FLAGS = 1
PDTF_ISINNATE: PROPDESC_TYPE_FLAGS = 2
PDTF_ISGROUP: PROPDESC_TYPE_FLAGS = 4
PDTF_CANGROUPBY: PROPDESC_TYPE_FLAGS = 8
PDTF_CANSTACKBY: PROPDESC_TYPE_FLAGS = 16
PDTF_ISTREEPROPERTY: PROPDESC_TYPE_FLAGS = 32
PDTF_INCLUDEINFULLTEXTQUERY: PROPDESC_TYPE_FLAGS = 64
PDTF_ISVIEWABLE: PROPDESC_TYPE_FLAGS = 128
PDTF_ISQUERYABLE: PROPDESC_TYPE_FLAGS = 256
PDTF_CANBEPURGED: PROPDESC_TYPE_FLAGS = 512
PDTF_SEARCHRAWVALUE: PROPDESC_TYPE_FLAGS = 1024
PDTF_DONTCOERCEEMPTYSTRINGS: PROPDESC_TYPE_FLAGS = 2048
PDTF_ALWAYSINSUPPLEMENTALSTORE: PROPDESC_TYPE_FLAGS = 4096
PDTF_ISSYSTEMPROPERTY: PROPDESC_TYPE_FLAGS = 2147483648
PDTF_MASK_ALL: PROPDESC_TYPE_FLAGS = 2147491839
PROPDESC_VIEW_FLAGS = Int32
PDVF_DEFAULT: PROPDESC_VIEW_FLAGS = 0
PDVF_CENTERALIGN: PROPDESC_VIEW_FLAGS = 1
PDVF_RIGHTALIGN: PROPDESC_VIEW_FLAGS = 2
PDVF_BEGINNEWGROUP: PROPDESC_VIEW_FLAGS = 4
PDVF_FILLAREA: PROPDESC_VIEW_FLAGS = 8
PDVF_SORTDESCENDING: PROPDESC_VIEW_FLAGS = 16
PDVF_SHOWONLYIFPRESENT: PROPDESC_VIEW_FLAGS = 32
PDVF_SHOWBYDEFAULT: PROPDESC_VIEW_FLAGS = 64
PDVF_SHOWINPRIMARYLIST: PROPDESC_VIEW_FLAGS = 128
PDVF_SHOWINSECONDARYLIST: PROPDESC_VIEW_FLAGS = 256
PDVF_HIDELABEL: PROPDESC_VIEW_FLAGS = 512
PDVF_HIDDEN: PROPDESC_VIEW_FLAGS = 2048
PDVF_CANWRAP: PROPDESC_VIEW_FLAGS = 4096
PDVF_MASK_ALL: PROPDESC_VIEW_FLAGS = 7167
PROPENUMTYPE = Int32
PET_DISCRETEVALUE: PROPENUMTYPE = 0
PET_RANGEDVALUE: PROPENUMTYPE = 1
PET_DEFAULTVALUE: PROPENUMTYPE = 2
PET_ENDRANGE: PROPENUMTYPE = 3
class PROPERTYKEY(EasyCastStructure):
    fmtid: Guid
    pid: UInt32
PROPERTYUI_FLAGS = Int32
PUIF_DEFAULT: PROPERTYUI_FLAGS = 0
PUIF_RIGHTALIGN: PROPERTYUI_FLAGS = 1
PUIF_NOLABELININFOTIP: PROPERTYUI_FLAGS = 2
PROPERTYUI_FORMAT_FLAGS = Int32
PUIFFDF_DEFAULT: PROPERTYUI_FORMAT_FLAGS = 0
PUIFFDF_RIGHTTOLEFT: PROPERTYUI_FORMAT_FLAGS = 1
PUIFFDF_SHORTFORMAT: PROPERTYUI_FORMAT_FLAGS = 2
PUIFFDF_NOTIME: PROPERTYUI_FORMAT_FLAGS = 4
PUIFFDF_FRIENDLYDATE: PROPERTYUI_FORMAT_FLAGS = 8
PROPERTYUI_NAME_FLAGS = Int32
PUIFNF_DEFAULT: PROPERTYUI_NAME_FLAGS = 0
PUIFNF_MNEMONIC: PROPERTYUI_NAME_FLAGS = 1
class PROPPRG(EasyCastStructure):
    flPrg: UInt16
    flPrgInit: UInt16
    achTitle: Windows.Win32.Foundation.CHAR * 30
    achCmdLine: Windows.Win32.Foundation.CHAR * 128
    achWorkDir: Windows.Win32.Foundation.CHAR * 64
    wHotKey: UInt16
    achIconFile: Windows.Win32.Foundation.CHAR * 80
    wIconIndex: UInt16
    dwEnhModeFlags: UInt32
    dwRealModeFlags: UInt32
    achOtherFile: Windows.Win32.Foundation.CHAR * 80
    achPIFFile: Windows.Win32.Foundation.CHAR * 260
    _pack_ = 1
PSC_STATE = Int32
PSC_NORMAL: PSC_STATE = 0
PSC_NOTINSOURCE: PSC_STATE = 1
PSC_DIRTY: PSC_STATE = 2
PSC_READONLY: PSC_STATE = 3
PropertySystem = Guid('{b8967f85-58ae-4f46-9fb2-5d7904798f4b}')
SERIALIZEDPROPSTORAGE = IntPtr
SYNC_ENGINE_STATE_FLAGS = Int32
SESF_NONE: SYNC_ENGINE_STATE_FLAGS = 0
SESF_SERVICE_QUOTA_NEARING_LIMIT: SYNC_ENGINE_STATE_FLAGS = 1
SESF_SERVICE_QUOTA_EXCEEDED_LIMIT: SYNC_ENGINE_STATE_FLAGS = 2
SESF_AUTHENTICATION_ERROR: SYNC_ENGINE_STATE_FLAGS = 4
SESF_PAUSED_DUE_TO_METERED_NETWORK: SYNC_ENGINE_STATE_FLAGS = 8
SESF_PAUSED_DUE_TO_DISK_SPACE_FULL: SYNC_ENGINE_STATE_FLAGS = 16
SESF_PAUSED_DUE_TO_CLIENT_POLICY: SYNC_ENGINE_STATE_FLAGS = 32
SESF_PAUSED_DUE_TO_SERVICE_POLICY: SYNC_ENGINE_STATE_FLAGS = 64
SESF_SERVICE_UNAVAILABLE: SYNC_ENGINE_STATE_FLAGS = 128
SESF_PAUSED_DUE_TO_USER_REQUEST: SYNC_ENGINE_STATE_FLAGS = 256
SESF_ALL_FLAGS: SYNC_ENGINE_STATE_FLAGS = 511
SYNC_TRANSFER_STATUS = Int32
STS_NONE: SYNC_TRANSFER_STATUS = 0
STS_NEEDSUPLOAD: SYNC_TRANSFER_STATUS = 1
STS_NEEDSDOWNLOAD: SYNC_TRANSFER_STATUS = 2
STS_TRANSFERRING: SYNC_TRANSFER_STATUS = 4
STS_PAUSED: SYNC_TRANSFER_STATUS = 8
STS_HASERROR: SYNC_TRANSFER_STATUS = 16
STS_FETCHING_METADATA: SYNC_TRANSFER_STATUS = 32
STS_USER_REQUESTED_REFRESH: SYNC_TRANSFER_STATUS = 64
STS_HASWARNING: SYNC_TRANSFER_STATUS = 128
STS_EXCLUDED: SYNC_TRANSFER_STATUS = 256
STS_INCOMPLETE: SYNC_TRANSFER_STATUS = 512
STS_PLACEHOLDER_IFEMPTY: SYNC_TRANSFER_STATUS = 1024
_PERSIST_SPROPSTORE_FLAGS = Int32
FPSPS_DEFAULT: _PERSIST_SPROPSTORE_FLAGS = 0
FPSPS_READONLY: _PERSIST_SPROPSTORE_FLAGS = 1
FPSPS_TREAT_NEW_VALUES_AS_DIRTY: _PERSIST_SPROPSTORE_FLAGS = 2
make_head(_module, 'ICreateObject')
make_head(_module, 'IDelayedPropertyStoreFactory')
make_head(_module, 'IInitializeWithFile')
make_head(_module, 'IInitializeWithStream')
make_head(_module, 'INamedPropertyStore')
make_head(_module, 'IObjectWithPropertyKey')
make_head(_module, 'IPersistSerializedPropStorage')
make_head(_module, 'IPersistSerializedPropStorage2')
make_head(_module, 'IPropertyChange')
make_head(_module, 'IPropertyChangeArray')
make_head(_module, 'IPropertyDescription')
make_head(_module, 'IPropertyDescription2')
make_head(_module, 'IPropertyDescriptionAliasInfo')
make_head(_module, 'IPropertyDescriptionList')
make_head(_module, 'IPropertyDescriptionRelatedPropertyInfo')
make_head(_module, 'IPropertyDescriptionSearchInfo')
make_head(_module, 'IPropertyEnumType')
make_head(_module, 'IPropertyEnumType2')
make_head(_module, 'IPropertyEnumTypeList')
make_head(_module, 'IPropertyStore')
make_head(_module, 'IPropertyStoreCache')
make_head(_module, 'IPropertyStoreCapabilities')
make_head(_module, 'IPropertyStoreFactory')
make_head(_module, 'IPropertySystem')
make_head(_module, 'IPropertySystemChangeNotify')
make_head(_module, 'IPropertyUI')
make_head(_module, 'PROPERTYKEY')
make_head(_module, 'PROPPRG')
