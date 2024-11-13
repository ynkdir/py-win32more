from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Search.Common
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.Shell.Common
import win32more.Windows.Win32.UI.Shell.PropertiesSystem
PKEY_PIDSTR_MAX: UInt32 = 10
@winfunctype('PROPSYS.dll')
def PSFormatForDisplay(propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pdfFlags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, pwszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSFormatForDisplayAlloc(key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pdff: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSFormatPropertyValue(pps: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore, ppd: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription, pdff: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetImageReferenceForValue(propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), ppszImageRes: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSStringFromPropertyKey(pkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), psz: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyKeyFromString(pszString: win32more.Windows.Win32.Foundation.PWSTR, pkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateMemoryPropertyStore(riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateDelayedMultiplexPropertyStore(flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, pdpsf: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IDelayedPropertyStoreFactory, rgStoreIds: POINTER(UInt32), cStores: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateMultiplexPropertyStore(prgpunkStores: POINTER(win32more.Windows.Win32.System.Com.IUnknown), cStores: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreatePropertyChangeArray(rgpropkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), rgflags: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PKA_FLAGS), rgpropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), cChanges: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateSimplePropertyChange(flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PKA_FLAGS, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyDescription(propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyDescriptionByName(pszCanonicalName: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSLookupPropertyHandlerCLSID(pszFilePath: win32more.Windows.Win32.Foundation.PWSTR, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetItemPropertyHandler(punkItem: win32more.Windows.Win32.System.Com.IUnknown, fReadWrite: win32more.Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetItemPropertyHandlerWithCreateObject(punkItem: win32more.Windows.Win32.System.Com.IUnknown, fReadWrite: win32more.Windows.Win32.Foundation.BOOL, punkCreateObject: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyValue(pps: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore, ppd: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSSetPropertyValue(pps: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore, ppd: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription, propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSRegisterPropertySchema(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSUnregisterPropertySchema(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSRefreshPropertySchema() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSEnumeratePropertyDescriptions(filterOn: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyKeyFromName(pszName: win32more.Windows.Win32.Foundation.PWSTR, ppropkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetNameFromPropertyKey(propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppszCanonicalName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCoerceToCanonicalValue(key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyDescriptionListFromString(pszPropList: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreatePropertyStoreFromPropertySetStorage(ppss: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertySetStorage, grfMode: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreatePropertyStoreFromObject(punk: win32more.Windows.Win32.System.Com.IUnknown, grfMode: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateAdapterFromPropertyStore(pps: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertySystem(riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyFromPropertyStorage(psps: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PCUSERIALIZEDPROPSTORAGE, cb: UInt32, rpkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetNamedPropertyFromPropertyStorage(psps: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PCUSERIALIZEDPROPSTORAGE, cb: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadType(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), type: win32more.Windows.Win32.System.Variant.VARENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadStr(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: win32more.Windows.Win32.Foundation.PWSTR, characterCount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadStrAlloc(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadBSTR(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteStr(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteBSTR(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadInt(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteInt(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadSHORT(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteSHORT(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: Int16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadLONG(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteLONG(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadDWORD(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteDWORD(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadBOOL(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteBOOL(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadPOINTL(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.POINTL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WritePOINTL(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.POINTL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadPOINTS(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.POINTS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WritePOINTS(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.POINTS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadRECTL(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.RECTL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteRECTL(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.RECTL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadStream(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteStream(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_Delete(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadULONGLONG(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteULONGLONG(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadUnknown(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteUnknown(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadGUID(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteGUID(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadPropertyKey(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WritePropertyKey(propBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, propName: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetPropertyStoreFromIDList(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetPropertyStoreFromParsingName(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pbc: win32more.Windows.Win32.System.Com.IBindCtx, flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHAddDefaultPropertiesByExt(pszExt: win32more.Windows.Win32.Foundation.PWSTR, pPropStore: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def PifMgr_OpenProperties(pszApp: win32more.Windows.Win32.Foundation.PWSTR, pszPIF: win32more.Windows.Win32.Foundation.PWSTR, hInf: UInt32, flOpt: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('SHELL32.dll')
def PifMgr_GetProperties(hProps: win32more.Windows.Win32.Foundation.HANDLE, pszGroup: win32more.Windows.Win32.Foundation.PSTR, lpProps: VoidPtr, cbProps: Int32, flOpt: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def PifMgr_SetProperties(hProps: win32more.Windows.Win32.Foundation.HANDLE, pszGroup: win32more.Windows.Win32.Foundation.PSTR, lpProps: VoidPtr, cbProps: Int32, flOpt: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def PifMgr_CloseProperties(hProps: win32more.Windows.Win32.Foundation.HANDLE, flOpt: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('SHELL32.dll')
def SHPropStgCreate(psstg: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertySetStorage, fmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, grfMode: UInt32, dwDisposition: UInt32, ppstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage), puCodePage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHPropStgReadMultiple(pps: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage, uCodePage: UInt32, cpspec: UInt32, rgpspec: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC), rgvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHPropStgWriteMultiple(pps: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage, puCodePage: POINTER(UInt32), cpspec: UInt32, rgpspec: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC), rgvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), propidNameFirst: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetPropertyStoreForWindow(hwnd: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
GETPROPERTYSTOREFLAGS = Int32
GPS_DEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 0
GPS_HANDLERPROPERTIESONLY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 1
GPS_READWRITE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 2
GPS_TEMPORARY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 4
GPS_FASTPROPERTIESONLY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 8
GPS_OPENSLOWITEM: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 16
GPS_DELAYCREATION: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 32
GPS_BESTEFFORT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 64
GPS_NO_OPLOCK: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 128
GPS_PREFERQUERYPROPERTIES: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 256
GPS_EXTRINSICPROPERTIES: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 512
GPS_EXTRINSICPROPERTIESONLY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 1024
GPS_VOLATILEPROPERTIES: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 2048
GPS_VOLATILEPROPERTIESONLY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 4096
GPS_MASK_VALID: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS = 8191
class ICreateObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75121952-e0d0-43e5-9380-1d80483acf72}')
    @commethod(3)
    def CreateObject(self, clsid: POINTER(Guid), pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDelayedPropertyStoreFactory(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStoreFactory
    _iid_ = Guid('{40d4577f-e237-4bdb-bd69-58f089431b6a}')
    @commethod(5)
    def GetDelayedPropertyStore(self, flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, dwStoreId: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithFile(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b7d14566-0509-4cce-a71f-0a554233bd9b}')
    @commethod(3)
    def Initialize(self, pszFilePath: win32more.Windows.Win32.Foundation.PWSTR, grfMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b824b49d-22ac-4161-ac8a-9916e8fa3f7f}')
    @commethod(3)
    def Initialize(self, pstream: win32more.Windows.Win32.System.Com.IStream, grfMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INamedPropertyStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71604b0f-97b0-4764-8577-2f13e98a1422}')
    @commethod(3)
    def GetNamedValue(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetNamedValue(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNameCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNameAt(self, iProp: UInt32, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectWithPropertyKey(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc0ca0a7-c316-4fd2-9031-3e628e6d4f23}')
    @commethod(3)
    def SetPropertyKey(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyKey(self, pkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistSerializedPropStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e318ad57-0aa0-450f-aca5-6fab7103d917}')
    @commethod(3)
    def SetFlags(self, flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPropertyStorage(self, psps: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PCUSERIALIZEDPROPSTORAGE, cb: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyStorage(self, ppsps: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE)), pcb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistSerializedPropStorage2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPersistSerializedPropStorage
    _iid_ = Guid('{77effa68-4f98-4366-ba72-573b3d880571}')
    @commethod(6)
    def GetPropertyStorageSize(self, pcb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPropertyStorageBuffer(self, psps: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE), cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyChange(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IObjectWithPropertyKey
    _iid_ = Guid('{f917bc8a-1bba-4478-a245-1bde03eb9431}')
    @commethod(5)
    def ApplyToPropVariant(self, propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), ppropvarOut: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyChangeArray(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{380f5cad-1b5e-42f2-805d-637fd392d31e}')
    @commethod(3)
    def GetCount(self, pcOperations: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, iIndex: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(self, iIndex: UInt32, ppropChange: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyChange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Append(self, ppropChange: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyChange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AppendOrReplace(self, ppropChange: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyChange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveAt(self, iIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsKeyInArray(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescription(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6f79d558-3e96-4549-a1d1-7d75d2288814}')
    @commethod(3)
    def GetPropertyKey(self, pkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCanonicalName(self, ppszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyType(self, pvartype: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDisplayName(self, ppszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEditInvitation(self, ppszInvite: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTypeFlags(self, mask: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS, ppdtFlags: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetViewFlags(self, ppdvFlags: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDefaultColumnWidth(self, pcxChars: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDisplayType(self, pdisplaytype: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_DISPLAYTYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetColumnState(self, pcsFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetGroupingRange(self, pgr: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRelativeDescriptionType(self, prdt: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRelativeDescription(self, propvar1: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), propvar2: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), ppszDesc1: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppszDesc2: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSortDescription(self, psd: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SORTDESCRIPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetSortDescriptionLabel(self, fDescending: win32more.Windows.Win32.Foundation.BOOL, ppszDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetAggregationType(self, paggtype: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetConditionType(self, pcontype: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_CONDITION_TYPE), popDefault: POINTER(win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetEnumTypeList(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CoerceToCanonicalValue(self, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def FormatForDisplay(self, propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pdfFlags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def IsValueCanonical(self, propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescription2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription
    _iid_ = Guid('{57d2eded-5062-400e-b107-5dae79fe57a6}')
    @commethod(24)
    def GetImageReferenceForValue(self, propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), ppszImageRes: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescriptionAliasInfo(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription
    _iid_ = Guid('{f67104fc-2af9-46fd-b32d-243c1404f3d1}')
    @commethod(24)
    def GetSortByAlias(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetAdditionalSortByAliases(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescriptionList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1f9fc1d0-c39b-4b26-817f-011967d3440e}')
    @commethod(3)
    def GetCount(self, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, iElem: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescriptionRelatedPropertyInfo(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription
    _iid_ = Guid('{507393f4-2a3d-4a60-b59e-d9c75716c2dd}')
    @commethod(24)
    def GetRelatedProperty(self, pszRelationshipName: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyDescriptionSearchInfo(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescription
    _iid_ = Guid('{078f91bd-29a2-440f-924e-46a291524520}')
    @commethod(24)
    def GetSearchInfoFlags(self, ppdsiFlags: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SEARCHINFO_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetColumnIndexType(self, ppdciType: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_COLUMNINDEX_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetProjectionString(self, ppszProjection: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetMaxSize(self, pcbMaxSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyEnumType(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11e1fbf9-2d56-4a6b-8db3-7cd193a471f2}')
    @commethod(3)
    def GetEnumType(self, penumtype: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPENUMTYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(self, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRangeMinValue(self, ppropvarMin: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRangeSetValue(self, ppropvarSet: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDisplayText(self, ppszDisplay: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyEnumType2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyEnumType
    _iid_ = Guid('{9b6e051c-5ddd-4321-9070-fe2acb55e794}')
    @commethod(8)
    def GetImageReference(self, ppszImageRes: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyEnumTypeList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a99400f4-3d84-4557-94ba-1242fb2cc9a6}')
    @commethod(3)
    def GetCount(self, pctypes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, itype: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetConditionAt(self, nIndex: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindMatchingIndex(self, propvarCmp: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pnIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{886d8eeb-8cf2-4446-8d02-cdba1dbdcf99}')
    @commethod(3)
    def GetCount(self, cProps: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, iProp: UInt32, pkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pv: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyStoreCache(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    _iid_ = Guid('{3017056d-9a91-4e90-937d-746c72abbf4f}')
    @commethod(8)
    def GetState(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pstate: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetValueAndState(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pstate: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetState(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), state: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetValueAndState(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), state: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyStoreCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8e2d566-186e-4d49-bf41-6909ead56acc}')
    @commethod(3)
    def IsPropertyWritable(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyStoreFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bc110b6d-57e8-4148-a9c6-91015ab2f3a5}')
    @commethod(3)
    def GetPropertyStore(self, flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, pUnkFactory: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyStoreForKeys(self, rgKeys: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), cKeys: UInt32, flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertySystem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ca724e8a-c3e6-442b-88a4-6fb0db8035a3}')
    @commethod(3)
    def GetPropertyDescription(self, propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyDescriptionByName(self, pszCanonicalName: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyDescriptionListFromString(self, pszPropList: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumeratePropertyDescriptions(self, filterOn: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FormatForDisplay(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pdff: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, pszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FormatForDisplayAlloc(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pdff: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterPropertySchema(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnregisterPropertySchema(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RefreshPropertySchema(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertySystemChangeNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fa955fd9-38be-4879-a6ce-824cf52d609f}')
    @commethod(3)
    def SchemaRefreshed(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyUI(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{757a7d9f-919a-4118-99d7-dbb208c8cc66}')
    @commethod(3)
    def ParsePropertyName(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, pfmtid: POINTER(Guid), ppid: POINTER(UInt32), pchEaten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCannonicalName(self, fmtid: POINTER(Guid), pid: UInt32, pwszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDisplayName(self, fmtid: POINTER(Guid), pid: UInt32, flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_NAME_FLAGS, pwszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyDescription(self, fmtid: POINTER(Guid), pid: UInt32, pwszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDefaultWidth(self, fmtid: POINTER(Guid), pid: UInt32, pcxChars: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFlags(self, fmtid: POINTER(Guid), pid: UInt32, pflags: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def FormatForDisplay(self, fmtid: POINTER(Guid), pid: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), puiff: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FORMAT_FLAGS, pwszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetHelpInfo(self, fmtid: POINTER(Guid), pid: UInt32, pwszHelpFile: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, puHelpID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
InMemoryPropertyStore = Guid('{9a02e012-6303-4e1e-b9a1-630f802592c5}')
InMemoryPropertyStoreMarshalByValue = Guid('{d4ca0e2d-6da7-4b75-a97c-5f306f0eaedc}')
PCUSERIALIZEDPROPSTORAGE = IntPtr
PDOPSTATUS = Int32
PDOPS_RUNNING: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PDOPSTATUS = 1
PDOPS_PAUSED: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PDOPSTATUS = 2
PDOPS_CANCELLED: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PDOPSTATUS = 3
PDOPS_STOPPED: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PDOPSTATUS = 4
PDOPS_ERRORS: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PDOPSTATUS = 5
PKA_FLAGS = Int32
PKA_SET: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PKA_FLAGS = 0
PKA_APPEND: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PKA_FLAGS = 1
PKA_DELETE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PKA_FLAGS = 2
PLACEHOLDER_STATES = Int32
PS_NONE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PLACEHOLDER_STATES = 0
PS_MARKED_FOR_OFFLINE_AVAILABILITY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PLACEHOLDER_STATES = 1
PS_FULL_PRIMARY_STREAM_AVAILABLE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PLACEHOLDER_STATES = 2
PS_CREATE_FILE_ACCESSIBLE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PLACEHOLDER_STATES = 4
PS_CLOUDFILE_PLACEHOLDER: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PLACEHOLDER_STATES = 8
PS_DEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PLACEHOLDER_STATES = 7
PS_ALL: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PLACEHOLDER_STATES = 15
PROPDESC_AGGREGATION_TYPE = Int32
PDAT_DEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE = 0
PDAT_FIRST: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE = 1
PDAT_SUM: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE = 2
PDAT_AVERAGE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE = 3
PDAT_DATERANGE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE = 4
PDAT_UNION: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE = 5
PDAT_MAX: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE = 6
PDAT_MIN: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE = 7
PROPDESC_COLUMNINDEX_TYPE = Int32
PDCIT_NONE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_COLUMNINDEX_TYPE = 0
PDCIT_ONDISK: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_COLUMNINDEX_TYPE = 1
PDCIT_INMEMORY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_COLUMNINDEX_TYPE = 2
PDCIT_ONDEMAND: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_COLUMNINDEX_TYPE = 3
PDCIT_ONDISKALL: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_COLUMNINDEX_TYPE = 4
PDCIT_ONDISKVECTOR: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_COLUMNINDEX_TYPE = 5
PROPDESC_CONDITION_TYPE = Int32
PDCOT_NONE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_CONDITION_TYPE = 0
PDCOT_STRING: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_CONDITION_TYPE = 1
PDCOT_SIZE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_CONDITION_TYPE = 2
PDCOT_DATETIME: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_CONDITION_TYPE = 3
PDCOT_BOOLEAN: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_CONDITION_TYPE = 4
PDCOT_NUMBER: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_CONDITION_TYPE = 5
PROPDESC_DISPLAYTYPE = Int32
PDDT_STRING: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_DISPLAYTYPE = 0
PDDT_NUMBER: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_DISPLAYTYPE = 1
PDDT_BOOLEAN: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_DISPLAYTYPE = 2
PDDT_DATETIME: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_DISPLAYTYPE = 3
PDDT_ENUMERATED: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_DISPLAYTYPE = 4
PROPDESC_ENUMFILTER = Int32
PDEF_ALL: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER = 0
PDEF_SYSTEM: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER = 1
PDEF_NONSYSTEM: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER = 2
PDEF_VIEWABLE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER = 3
PDEF_QUERYABLE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER = 4
PDEF_INFULLTEXTQUERY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER = 5
PDEF_COLUMN: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER = 6
PROPDESC_FORMAT_FLAGS = Int32
PDFF_DEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 0
PDFF_PREFIXNAME: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 1
PDFF_FILENAME: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 2
PDFF_ALWAYSKB: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 4
PDFF_RESERVED_RIGHTTOLEFT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 8
PDFF_SHORTTIME: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 16
PDFF_LONGTIME: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 32
PDFF_HIDETIME: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 64
PDFF_SHORTDATE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 128
PDFF_LONGDATE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 256
PDFF_HIDEDATE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 512
PDFF_RELATIVEDATE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 1024
PDFF_USEEDITINVITATION: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 2048
PDFF_READONLY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 4096
PDFF_NOAUTOREADINGORDER: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS = 8192
PROPDESC_GROUPING_RANGE = Int32
PDGR_DISCRETE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE = 0
PDGR_ALPHANUMERIC: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE = 1
PDGR_SIZE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE = 2
PDGR_DYNAMIC: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE = 3
PDGR_DATE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE = 4
PDGR_PERCENT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE = 5
PDGR_ENUMERATED: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE = 6
PROPDESC_RELATIVEDESCRIPTION_TYPE = Int32
PDRDT_GENERAL: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE = 0
PDRDT_DATE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE = 1
PDRDT_SIZE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE = 2
PDRDT_COUNT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE = 3
PDRDT_REVISION: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE = 4
PDRDT_LENGTH: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE = 5
PDRDT_DURATION: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE = 6
PDRDT_SPEED: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE = 7
PDRDT_RATE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE = 8
PDRDT_RATING: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE = 9
PDRDT_PRIORITY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE = 10
PROPDESC_SEARCHINFO_FLAGS = Int32
PDSIF_DEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SEARCHINFO_FLAGS = 0
PDSIF_ININVERTEDINDEX: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SEARCHINFO_FLAGS = 1
PDSIF_ISCOLUMN: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SEARCHINFO_FLAGS = 2
PDSIF_ISCOLUMNSPARSE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SEARCHINFO_FLAGS = 4
PDSIF_ALWAYSINCLUDE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SEARCHINFO_FLAGS = 8
PDSIF_USEFORTYPEAHEAD: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SEARCHINFO_FLAGS = 16
PROPDESC_SORTDESCRIPTION = Int32
PDSD_GENERAL: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SORTDESCRIPTION = 0
PDSD_A_Z: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SORTDESCRIPTION = 1
PDSD_LOWEST_HIGHEST: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SORTDESCRIPTION = 2
PDSD_SMALLEST_BIGGEST: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SORTDESCRIPTION = 3
PDSD_OLDEST_NEWEST: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_SORTDESCRIPTION = 4
PROPDESC_TYPE_FLAGS = UInt32
PDTF_DEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 0
PDTF_MULTIPLEVALUES: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 1
PDTF_ISINNATE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 2
PDTF_ISGROUP: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 4
PDTF_CANGROUPBY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 8
PDTF_CANSTACKBY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 16
PDTF_ISTREEPROPERTY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 32
PDTF_INCLUDEINFULLTEXTQUERY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 64
PDTF_ISVIEWABLE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 128
PDTF_ISQUERYABLE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 256
PDTF_CANBEPURGED: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 512
PDTF_SEARCHRAWVALUE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 1024
PDTF_DONTCOERCEEMPTYSTRINGS: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 2048
PDTF_ALWAYSINSUPPLEMENTALSTORE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 4096
PDTF_ISSYSTEMPROPERTY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 2147483648
PDTF_MASK_ALL: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS = 2147491839
PROPDESC_VIEW_FLAGS = Int32
PDVF_DEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 0
PDVF_CENTERALIGN: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 1
PDVF_RIGHTALIGN: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 2
PDVF_BEGINNEWGROUP: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 4
PDVF_FILLAREA: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 8
PDVF_SORTDESCENDING: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 16
PDVF_SHOWONLYIFPRESENT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 32
PDVF_SHOWBYDEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 64
PDVF_SHOWINPRIMARYLIST: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 128
PDVF_SHOWINSECONDARYLIST: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 256
PDVF_HIDELABEL: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 512
PDVF_HIDDEN: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 2048
PDVF_CANWRAP: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 4096
PDVF_MASK_ALL: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS = 7167
PROPENUMTYPE = Int32
PET_DISCRETEVALUE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPENUMTYPE = 0
PET_RANGEDVALUE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPENUMTYPE = 1
PET_DEFAULTVALUE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPENUMTYPE = 2
PET_ENDRANGE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPENUMTYPE = 3
PROPERTYUI_FLAGS = Int32
PUIF_DEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FLAGS = 0
PUIF_RIGHTALIGN: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FLAGS = 1
PUIF_NOLABELININFOTIP: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FLAGS = 2
PROPERTYUI_FORMAT_FLAGS = Int32
PUIFFDF_DEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FORMAT_FLAGS = 0
PUIFFDF_RIGHTTOLEFT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FORMAT_FLAGS = 1
PUIFFDF_SHORTFORMAT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FORMAT_FLAGS = 2
PUIFFDF_NOTIME: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FORMAT_FLAGS = 4
PUIFFDF_FRIENDLYDATE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_FORMAT_FLAGS = 8
PROPERTYUI_NAME_FLAGS = Int32
PUIFNF_DEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_NAME_FLAGS = 0
PUIFNF_MNEMONIC: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYUI_NAME_FLAGS = 1
class PROPPRG(Structure):
    flPrg: UInt16
    flPrgInit: UInt16
    achTitle: win32more.Windows.Win32.Foundation.CHAR * 30
    achCmdLine: win32more.Windows.Win32.Foundation.CHAR * 128
    achWorkDir: win32more.Windows.Win32.Foundation.CHAR * 64
    wHotKey: UInt16
    achIconFile: win32more.Windows.Win32.Foundation.CHAR * 80
    wIconIndex: UInt16
    dwEnhModeFlags: UInt32
    dwRealModeFlags: UInt32
    achOtherFile: win32more.Windows.Win32.Foundation.CHAR * 80
    achPIFFile: win32more.Windows.Win32.Foundation.CHAR * 260
    _pack_ = 1
PSC_STATE = Int32
PSC_NORMAL: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE = 0
PSC_NOTINSOURCE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE = 1
PSC_DIRTY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE = 2
PSC_READONLY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.PSC_STATE = 3
PropertySystem = Guid('{b8967f85-58ae-4f46-9fb2-5d7904798f4b}')
SERIALIZEDPROPSTORAGE = IntPtr
SYNC_ENGINE_STATE_FLAGS = Int32
SESF_NONE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_ENGINE_STATE_FLAGS = 0
SESF_SERVICE_QUOTA_NEARING_LIMIT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_ENGINE_STATE_FLAGS = 1
SESF_SERVICE_QUOTA_EXCEEDED_LIMIT: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_ENGINE_STATE_FLAGS = 2
SESF_AUTHENTICATION_ERROR: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_ENGINE_STATE_FLAGS = 4
SESF_PAUSED_DUE_TO_METERED_NETWORK: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_ENGINE_STATE_FLAGS = 8
SESF_PAUSED_DUE_TO_DISK_SPACE_FULL: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_ENGINE_STATE_FLAGS = 16
SESF_PAUSED_DUE_TO_CLIENT_POLICY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_ENGINE_STATE_FLAGS = 32
SESF_PAUSED_DUE_TO_SERVICE_POLICY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_ENGINE_STATE_FLAGS = 64
SESF_SERVICE_UNAVAILABLE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_ENGINE_STATE_FLAGS = 128
SESF_PAUSED_DUE_TO_USER_REQUEST: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_ENGINE_STATE_FLAGS = 256
SESF_ALL_FLAGS: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_ENGINE_STATE_FLAGS = 511
SYNC_TRANSFER_STATUS = Int32
STS_NONE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 0
STS_NEEDSUPLOAD: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 1
STS_NEEDSDOWNLOAD: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 2
STS_TRANSFERRING: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 4
STS_PAUSED: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 8
STS_HASERROR: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 16
STS_FETCHING_METADATA: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 32
STS_USER_REQUESTED_REFRESH: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 64
STS_HASWARNING: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 128
STS_EXCLUDED: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 256
STS_INCOMPLETE: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 512
STS_PLACEHOLDER_IFEMPTY: win32more.Windows.Win32.UI.Shell.PropertiesSystem.SYNC_TRANSFER_STATUS = 1024
_PERSIST_SPROPSTORE_FLAGS = Int32
FPSPS_DEFAULT: win32more.Windows.Win32.UI.Shell.PropertiesSystem._PERSIST_SPROPSTORE_FLAGS = 0
FPSPS_READONLY: win32more.Windows.Win32.UI.Shell.PropertiesSystem._PERSIST_SPROPSTORE_FLAGS = 1
FPSPS_TREAT_NEW_VALUES_AS_DIRTY: win32more.Windows.Win32.UI.Shell.PropertiesSystem._PERSIST_SPROPSTORE_FLAGS = 2


make_ready(__name__)
