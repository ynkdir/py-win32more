from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Search.Common
import win32more.UI.Shell.Common
import win32more.UI.Shell.PropertiesSystem
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
PKEY_PIDSTR_MAX: UInt32 = 10
@winfunctype('PROPSYS.dll')
def PropVariantToWinRTPropertyValue(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def WinRTPropertyValueToPropVariant(punkPropertyValue: win32more.System.Com.IUnknown_head, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSFormatForDisplay(propkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pdfFlags: win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, pwszText: win32more.Foundation.PWSTR, cchText: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSFormatForDisplayAlloc(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pdff: win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSFormatPropertyValue(pps: win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, ppd: win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head, pdff: win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetImageReferenceForValue(propkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), ppszImageRes: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSStringFromPropertyKey(pkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), psz: win32more.Foundation.PWSTR, cch: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyKeyFromString(pszString: win32more.Foundation.PWSTR, pkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateMemoryPropertyStore(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateDelayedMultiplexPropertyStore(flags: win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, pdpsf: win32more.UI.Shell.PropertiesSystem.IDelayedPropertyStoreFactory_head, rgStoreIds: POINTER(UInt32), cStores: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateMultiplexPropertyStore(prgpunkStores: POINTER(win32more.System.Com.IUnknown_head), cStores: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreatePropertyChangeArray(rgpropkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), rgflags: POINTER(win32more.UI.Shell.PropertiesSystem.PKA_FLAGS), rgpropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), cChanges: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateSimplePropertyChange(flags: win32more.UI.Shell.PropertiesSystem.PKA_FLAGS, key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyDescription(propkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyDescriptionByName(pszCanonicalName: win32more.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSLookupPropertyHandlerCLSID(pszFilePath: win32more.Foundation.PWSTR, pclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetItemPropertyHandler(punkItem: win32more.System.Com.IUnknown_head, fReadWrite: win32more.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetItemPropertyHandlerWithCreateObject(punkItem: win32more.System.Com.IUnknown_head, fReadWrite: win32more.Foundation.BOOL, punkCreateObject: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyValue(pps: win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, ppd: win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSSetPropertyValue(pps: win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, ppd: win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head, propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSRegisterPropertySchema(pszPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSUnregisterPropertySchema(pszPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSRefreshPropertySchema() -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSEnumeratePropertyDescriptions(filterOn: win32more.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyKeyFromName(pszName: win32more.Foundation.PWSTR, ppropkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetNameFromPropertyKey(propkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppszCanonicalName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCoerceToCanonicalValue(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyDescriptionListFromString(pszPropList: win32more.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreatePropertyStoreFromPropertySetStorage(ppss: win32more.System.Com.StructuredStorage.IPropertySetStorage_head, grfMode: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreatePropertyStoreFromObject(punk: win32more.System.Com.IUnknown_head, grfMode: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSCreateAdapterFromPropertyStore(pps: win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertySystem(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetPropertyFromPropertyStorage(psps: POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head), cb: UInt32, rpkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSGetNamedPropertyFromPropertyStorage(psps: POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head), cb: UInt32, pszName: win32more.Foundation.PWSTR, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadType(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, var: POINTER(win32more.System.Com.VARIANT_head), type: win32more.System.Com.VARENUM) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadStr(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: win32more.Foundation.PWSTR, characterCount: Int32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadStrAlloc(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadBSTR(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteStr(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteBSTR(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadInt(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteInt(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: Int32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadSHORT(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteSHORT(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: Int16) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadLONG(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteLONG(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: Int32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadDWORD(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteDWORD(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadBOOL(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteBOOL(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadPOINTL(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.Foundation.POINTL_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WritePOINTL(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.Foundation.POINTL_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadPOINTS(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.Foundation.POINTS_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WritePOINTS(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.Foundation.POINTS_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadRECTL(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.Foundation.RECTL_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteRECTL(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.Foundation.RECTL_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadStream(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteStream(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_Delete(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadULONGLONG(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteULONGLONG(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: UInt64) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadUnknown(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteUnknown(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadGUID(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WriteGUID(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_ReadPropertyKey(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PSPropertyBag_WritePropertyKey(propBag: win32more.System.Com.StructuredStorage.IPropertyBag_head, propName: win32more.Foundation.PWSTR, value: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromResource(hinst: win32more.Foundation.HINSTANCE, id: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromBuffer(pv: c_void_p, cb: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromCLSID(clsid: POINTER(Guid), ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromGUIDAsString(guid: POINTER(Guid), ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromFileTime(pftIn: POINTER(win32more.Foundation.FILETIME_head), ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromPropVariantVectorElem(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantVectorFromPropVariant(propvarSingle: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), ppropvarVector: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromStrRet(pstrret: POINTER(win32more.UI.Shell.Common.STRRET_head), pidl: POINTER(win32more.UI.Shell.Common.ITEMIDLIST_head), ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromBooleanVector(prgf: POINTER(win32more.Foundation.BOOL), cElems: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt16Vector(prgn: POINTER(Int16), cElems: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt16Vector(prgn: POINTER(UInt16), cElems: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt32Vector(prgn: POINTER(Int32), cElems: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt32Vector(prgn: POINTER(UInt32), cElems: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt64Vector(prgn: POINTER(Int64), cElems: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt64Vector(prgn: POINTER(UInt64), cElems: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromDoubleVector(prgn: POINTER(Double), cElems: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromFileTimeVector(prgft: POINTER(win32more.Foundation.FILETIME_head), cElems: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromStringVector(prgsz: POINTER(win32more.Foundation.PWSTR), cElems: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromStringAsVector(psz: win32more.Foundation.PWSTR, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanWithDefault(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), fDefault: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16WithDefault(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iDefault: Int16) -> Int16: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16WithDefault(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), uiDefault: UInt16) -> UInt16: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32WithDefault(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), lDefault: Int32) -> Int32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32WithDefault(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), ulDefault: UInt32) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64WithDefault(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), llDefault: Int64) -> Int64: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64WithDefault(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), ullDefault: UInt64) -> UInt64: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleWithDefault(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), dblDefault: Double) -> Double: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringWithDefault(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pszDefault: win32more.Foundation.PWSTR) -> win32more.Foundation.PWSTR: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBoolean(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pfRet: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), piRet: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), puiRet: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), plRet: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pulRet: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pllRet: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pullRet: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDouble(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pdblRet: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBuffer(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pv: c_void_p, cb: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToString(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), psz: win32more.Foundation.PWSTR, cch: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToGUID(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringAlloc(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), ppszOut: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBSTR(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pbstrOut: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStrRet(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pstrret: POINTER(win32more.UI.Shell.Common.STRRET_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTime(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pstfOut: win32more.UI.Shell.PropertiesSystem.PSTIME_FLAGS, pftOut: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetElementCount(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanVector(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), prgf: POINTER(win32more.Foundation.BOOL), crgf: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16Vector(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Int16), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16Vector(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(UInt16), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32Vector(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Int32), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32Vector(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(UInt32), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64Vector(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Int64), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64Vector(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(UInt64), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleVector(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Double), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTimeVector(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), prgft: POINTER(win32more.Foundation.FILETIME_head), crgft: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringVector(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), prgsz: POINTER(win32more.Foundation.PWSTR), crgsz: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanVectorAlloc(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pprgf: POINTER(POINTER(win32more.Foundation.BOOL)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16VectorAlloc(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Int16)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16VectorAlloc(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(UInt16)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32VectorAlloc(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Int32)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32VectorAlloc(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(UInt32)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64VectorAlloc(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Int64)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64VectorAlloc(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(UInt64)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleVectorAlloc(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Double)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTimeVectorAlloc(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pprgft: POINTER(POINTER(win32more.Foundation.FILETIME_head)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringVectorAlloc(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pprgsz: POINTER(POINTER(win32more.Foundation.PWSTR)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetBooleanElem(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt16Elem(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt16Elem(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt32Elem(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt32Elem(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt64Elem(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt64Elem(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetDoubleElem(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetFileTimeElem(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pftVal: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetStringElem(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, ppszVal: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def ClearPropVariantArray(rgPropVar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), cVars: UInt32) -> Void: ...
@winfunctype('PROPSYS.dll')
def PropVariantCompareEx(propvar1: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), propvar2: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), unit: win32more.UI.Shell.PropertiesSystem.PROPVAR_COMPARE_UNIT, flags: win32more.UI.Shell.PropertiesSystem.PROPVAR_COMPARE_FLAGS) -> Int32: ...
@winfunctype('PROPSYS.dll')
def PropVariantChangeType(ppropvarDest: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), propvarSrc: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), flags: win32more.UI.Shell.PropertiesSystem.PROPVAR_CHANGE_FLAGS, vt: win32more.System.Com.VARENUM) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToVariant(pPropVar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pVar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToPropVariant(pVar: POINTER(win32more.System.Com.VARIANT_head), pPropVar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromResource(hinst: win32more.Foundation.HINSTANCE, id: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromBuffer(pv: c_void_p, cb: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromGUIDAsString(guid: POINTER(Guid), pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromFileTime(pft: POINTER(win32more.Foundation.FILETIME_head), pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromFileTimeArray(prgft: POINTER(win32more.Foundation.FILETIME_head), cElems: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromStrRet(pstrret: POINTER(win32more.UI.Shell.Common.STRRET_head), pidl: POINTER(win32more.UI.Shell.Common.ITEMIDLIST_head), pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromVariantArrayElem(varIn: POINTER(win32more.System.Com.VARIANT_head), iElem: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromBooleanArray(prgf: POINTER(win32more.Foundation.BOOL), cElems: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromInt16Array(prgn: POINTER(Int16), cElems: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromUInt16Array(prgn: POINTER(UInt16), cElems: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromInt32Array(prgn: POINTER(Int32), cElems: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromUInt32Array(prgn: POINTER(UInt32), cElems: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromInt64Array(prgn: POINTER(Int64), cElems: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromUInt64Array(prgn: POINTER(UInt64), cElems: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromDoubleArray(prgn: POINTER(Double), cElems: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromStringArray(prgsz: POINTER(win32more.Foundation.PWSTR), cElems: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToBooleanWithDefault(varIn: POINTER(win32more.System.Com.VARIANT_head), fDefault: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16WithDefault(varIn: POINTER(win32more.System.Com.VARIANT_head), iDefault: Int16) -> Int16: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16WithDefault(varIn: POINTER(win32more.System.Com.VARIANT_head), uiDefault: UInt16) -> UInt16: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32WithDefault(varIn: POINTER(win32more.System.Com.VARIANT_head), lDefault: Int32) -> Int32: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32WithDefault(varIn: POINTER(win32more.System.Com.VARIANT_head), ulDefault: UInt32) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64WithDefault(varIn: POINTER(win32more.System.Com.VARIANT_head), llDefault: Int64) -> Int64: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64WithDefault(varIn: POINTER(win32more.System.Com.VARIANT_head), ullDefault: UInt64) -> UInt64: ...
@winfunctype('PROPSYS.dll')
def VariantToDoubleWithDefault(varIn: POINTER(win32more.System.Com.VARIANT_head), dblDefault: Double) -> Double: ...
@winfunctype('PROPSYS.dll')
def VariantToStringWithDefault(varIn: POINTER(win32more.System.Com.VARIANT_head), pszDefault: win32more.Foundation.PWSTR) -> win32more.Foundation.PWSTR: ...
@winfunctype('PROPSYS.dll')
def VariantToBoolean(varIn: POINTER(win32more.System.Com.VARIANT_head), pfRet: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16(varIn: POINTER(win32more.System.Com.VARIANT_head), piRet: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16(varIn: POINTER(win32more.System.Com.VARIANT_head), puiRet: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32(varIn: POINTER(win32more.System.Com.VARIANT_head), plRet: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32(varIn: POINTER(win32more.System.Com.VARIANT_head), pulRet: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64(varIn: POINTER(win32more.System.Com.VARIANT_head), pllRet: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64(varIn: POINTER(win32more.System.Com.VARIANT_head), pullRet: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDouble(varIn: POINTER(win32more.System.Com.VARIANT_head), pdblRet: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToBuffer(varIn: POINTER(win32more.System.Com.VARIANT_head), pv: c_void_p, cb: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToGUID(varIn: POINTER(win32more.System.Com.VARIANT_head), pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToString(varIn: POINTER(win32more.System.Com.VARIANT_head), pszBuf: win32more.Foundation.PWSTR, cchBuf: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToStringAlloc(varIn: POINTER(win32more.System.Com.VARIANT_head), ppszBuf: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDosDateTime(varIn: POINTER(win32more.System.Com.VARIANT_head), pwDate: POINTER(UInt16), pwTime: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToStrRet(varIn: POINTER(win32more.System.Com.VARIANT_head), pstrret: POINTER(win32more.UI.Shell.Common.STRRET_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToFileTime(varIn: POINTER(win32more.System.Com.VARIANT_head), stfOut: win32more.UI.Shell.PropertiesSystem.PSTIME_FLAGS, pftOut: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetElementCount(varIn: POINTER(win32more.System.Com.VARIANT_head)) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def VariantToBooleanArray(var: POINTER(win32more.System.Com.VARIANT_head), prgf: POINTER(win32more.Foundation.BOOL), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16Array(var: POINTER(win32more.System.Com.VARIANT_head), prgn: POINTER(Int16), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16Array(var: POINTER(win32more.System.Com.VARIANT_head), prgn: POINTER(UInt16), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32Array(var: POINTER(win32more.System.Com.VARIANT_head), prgn: POINTER(Int32), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32Array(var: POINTER(win32more.System.Com.VARIANT_head), prgn: POINTER(UInt32), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64Array(var: POINTER(win32more.System.Com.VARIANT_head), prgn: POINTER(Int64), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64Array(var: POINTER(win32more.System.Com.VARIANT_head), prgn: POINTER(UInt64), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDoubleArray(var: POINTER(win32more.System.Com.VARIANT_head), prgn: POINTER(Double), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToStringArray(var: POINTER(win32more.System.Com.VARIANT_head), prgsz: POINTER(win32more.Foundation.PWSTR), crgsz: UInt32, pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToBooleanArrayAlloc(var: POINTER(win32more.System.Com.VARIANT_head), pprgf: POINTER(POINTER(win32more.Foundation.BOOL)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16ArrayAlloc(var: POINTER(win32more.System.Com.VARIANT_head), pprgn: POINTER(POINTER(Int16)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16ArrayAlloc(var: POINTER(win32more.System.Com.VARIANT_head), pprgn: POINTER(POINTER(UInt16)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32ArrayAlloc(var: POINTER(win32more.System.Com.VARIANT_head), pprgn: POINTER(POINTER(Int32)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32ArrayAlloc(var: POINTER(win32more.System.Com.VARIANT_head), pprgn: POINTER(POINTER(UInt32)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64ArrayAlloc(var: POINTER(win32more.System.Com.VARIANT_head), pprgn: POINTER(POINTER(Int64)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64ArrayAlloc(var: POINTER(win32more.System.Com.VARIANT_head), pprgn: POINTER(POINTER(UInt64)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDoubleArrayAlloc(var: POINTER(win32more.System.Com.VARIANT_head), pprgn: POINTER(POINTER(Double)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToStringArrayAlloc(var: POINTER(win32more.System.Com.VARIANT_head), pprgsz: POINTER(POINTER(win32more.Foundation.PWSTR)), pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetBooleanElem(var: POINTER(win32more.System.Com.VARIANT_head), iElem: UInt32, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetInt16Elem(var: POINTER(win32more.System.Com.VARIANT_head), iElem: UInt32, pnVal: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetUInt16Elem(var: POINTER(win32more.System.Com.VARIANT_head), iElem: UInt32, pnVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetInt32Elem(var: POINTER(win32more.System.Com.VARIANT_head), iElem: UInt32, pnVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetUInt32Elem(var: POINTER(win32more.System.Com.VARIANT_head), iElem: UInt32, pnVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetInt64Elem(var: POINTER(win32more.System.Com.VARIANT_head), iElem: UInt32, pnVal: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetUInt64Elem(var: POINTER(win32more.System.Com.VARIANT_head), iElem: UInt32, pnVal: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetDoubleElem(var: POINTER(win32more.System.Com.VARIANT_head), iElem: UInt32, pnVal: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetStringElem(var: POINTER(win32more.System.Com.VARIANT_head), iElem: UInt32, ppszVal: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def ClearVariantArray(pvars: POINTER(win32more.System.Com.VARIANT_head), cvars: UInt32) -> Void: ...
@winfunctype('PROPSYS.dll')
def VariantCompare(var1: POINTER(win32more.System.Com.VARIANT_head), var2: POINTER(win32more.System.Com.VARIANT_head)) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHGetPropertyStoreFromIDList(pidl: POINTER(win32more.UI.Shell.Common.ITEMIDLIST_head), flags: win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetPropertyStoreFromParsingName(pszPath: win32more.Foundation.PWSTR, pbc: win32more.System.Com.IBindCtx_head, flags: win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHAddDefaultPropertiesByExt(pszExt: win32more.Foundation.PWSTR, pPropStore: win32more.UI.Shell.PropertiesSystem.IPropertyStore_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def PifMgr_OpenProperties(pszApp: win32more.Foundation.PWSTR, pszPIF: win32more.Foundation.PWSTR, hInf: UInt32, flOpt: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('SHELL32.dll')
def PifMgr_GetProperties(hProps: win32more.Foundation.HANDLE, pszGroup: win32more.Foundation.PSTR, lpProps: c_void_p, cbProps: Int32, flOpt: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def PifMgr_SetProperties(hProps: win32more.Foundation.HANDLE, pszGroup: win32more.Foundation.PSTR, lpProps: c_void_p, cbProps: Int32, flOpt: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def PifMgr_CloseProperties(hProps: win32more.Foundation.HANDLE, flOpt: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('SHELL32.dll')
def SHPropStgCreate(psstg: win32more.System.Com.StructuredStorage.IPropertySetStorage_head, fmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, grfMode: UInt32, dwDisposition: UInt32, ppstg: POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head), puCodePage: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHPropStgReadMultiple(pps: win32more.System.Com.StructuredStorage.IPropertyStorage_head, uCodePage: UInt32, cpspec: UInt32, rgpspec: POINTER(win32more.System.Com.StructuredStorage.PROPSPEC_head), rgvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHPropStgWriteMultiple(pps: win32more.System.Com.StructuredStorage.IPropertyStorage_head, puCodePage: POINTER(UInt32), cpspec: UInt32, rgpspec: POINTER(win32more.System.Com.StructuredStorage.PROPSPEC_head), rgvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), propidNameFirst: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetPropertyStoreForWindow(hwnd: win32more.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
DRAWPROGRESSFLAGS = UInt32
DPF_NONE: DRAWPROGRESSFLAGS = 0
DPF_MARQUEE: DRAWPROGRESSFLAGS = 1
DPF_MARQUEE_COMPLETE: DRAWPROGRESSFLAGS = 2
DPF_ERROR: DRAWPROGRESSFLAGS = 4
DPF_WARNING: DRAWPROGRESSFLAGS = 8
DPF_STOPPED: DRAWPROGRESSFLAGS = 16
GETPROPERTYSTOREFLAGS = UInt32
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
class ICreateObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('75121952-e0d0-43e5-93-80-1d-80-48-3a-cf-72')
    @commethod(3)
    def CreateObject(clsid: POINTER(Guid), pUnkOuter: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IDelayedPropertyStoreFactory(c_void_p):
    extends: win32more.UI.Shell.PropertiesSystem.IPropertyStoreFactory
    Guid = Guid('40d4577f-e237-4bdb-bd-69-58-f0-89-43-1b-6a')
    @commethod(5)
    def GetDelayedPropertyStore(flags: win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, dwStoreId: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IInitializeWithFile(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b7d14566-0509-4cce-a7-1f-0a-55-42-33-bd-9b')
    @commethod(3)
    def Initialize(pszFilePath: win32more.Foundation.PWSTR, grfMode: UInt32) -> win32more.Foundation.HRESULT: ...
class IInitializeWithStream(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b824b49d-22ac-4161-ac-8a-99-16-e8-fa-3f-7f')
    @commethod(3)
    def Initialize(pstream: win32more.System.Com.IStream_head, grfMode: UInt32) -> win32more.Foundation.HRESULT: ...
class INamedPropertyStore(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('71604b0f-97b0-4764-85-77-2f-13-e9-8a-14-22')
    @commethod(3)
    def GetNamedValue(pszName: win32more.Foundation.PWSTR, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetNamedValue(pszName: win32more.Foundation.PWSTR, propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetNameCount(pdwCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetNameAt(iProp: UInt32, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IObjectWithPropertyKey(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fc0ca0a7-c316-4fd2-90-31-3e-62-8e-6d-4f-23')
    @commethod(3)
    def SetPropertyKey(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyKey(pkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
class IPersistSerializedPropStorage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e318ad57-0aa0-450f-ac-a5-6f-ab-71-03-d9-17')
    @commethod(3)
    def SetFlags(flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetPropertyStorage(psps: POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head), cb: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyStorage(ppsps: POINTER(POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head)), pcb: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IPersistSerializedPropStorage2(c_void_p):
    extends: win32more.UI.Shell.PropertiesSystem.IPersistSerializedPropStorage
    Guid = Guid('77effa68-4f98-4366-ba-72-57-3b-3d-88-05-71')
    @commethod(6)
    def GetPropertyStorageSize(pcb: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetPropertyStorageBuffer(psps: POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head), cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IPropertyChange(c_void_p):
    extends: win32more.UI.Shell.PropertiesSystem.IObjectWithPropertyKey
    Guid = Guid('f917bc8a-1bba-4478-a2-45-1b-de-03-eb-94-31')
    @commethod(5)
    def ApplyToPropVariant(propvarIn: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), ppropvarOut: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IPropertyChangeArray(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('380f5cad-1b5e-42f2-80-5d-63-7f-d3-92-d3-1e')
    @commethod(3)
    def GetCount(pcOperations: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(iIndex: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(iIndex: UInt32, ppropChange: win32more.UI.Shell.PropertiesSystem.IPropertyChange_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Append(ppropChange: win32more.UI.Shell.PropertiesSystem.IPropertyChange_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def AppendOrReplace(ppropChange: win32more.UI.Shell.PropertiesSystem.IPropertyChange_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveAt(iIndex: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def IsKeyInArray(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
class IPropertyDescription(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6f79d558-3e96-4549-a1-d1-7d-75-d2-28-88-14')
    @commethod(3)
    def GetPropertyKey(pkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCanonicalName(ppszName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyType(pvartype: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDisplayName(ppszName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetEditInvitation(ppszInvite: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTypeFlags(mask: win32more.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS, ppdtFlags: POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetViewFlags(ppdvFlags: POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetDefaultColumnWidth(pcxChars: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetDisplayType(pdisplaytype: POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_DISPLAYTYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetColumnState(pcsFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetGroupingRange(pgr: POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRelativeDescriptionType(prdt: POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetRelativeDescription(propvar1: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), propvar2: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), ppszDesc1: POINTER(win32more.Foundation.PWSTR), ppszDesc2: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetSortDescription(psd: POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_SORTDESCRIPTION)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetSortDescriptionLabel(fDescending: win32more.Foundation.BOOL, ppszDescription: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetAggregationType(paggtype: POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetConditionType(pcontype: POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_CONDITION_TYPE), popDefault: POINTER(win32more.System.Search.Common.CONDITION_OPERATION)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetEnumTypeList(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def CoerceToCanonicalValue(ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def FormatForDisplay(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pdfFlags: win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def IsValueCanonical(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IPropertyDescription2(c_void_p):
    extends: win32more.UI.Shell.PropertiesSystem.IPropertyDescription
    Guid = Guid('57d2eded-5062-400e-b1-07-5d-ae-79-fe-57-a6')
    @commethod(24)
    def GetImageReferenceForValue(propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), ppszImageRes: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IPropertyDescriptionAliasInfo(c_void_p):
    extends: win32more.UI.Shell.PropertiesSystem.IPropertyDescription
    Guid = Guid('f67104fc-2af9-46fd-b3-2d-24-3c-14-04-f3-d1')
    @commethod(24)
    def GetSortByAlias(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetAdditionalSortByAliases(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IPropertyDescriptionList(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1f9fc1d0-c39b-4b26-81-7f-01-19-67-d3-44-0e')
    @commethod(3)
    def GetCount(pcElem: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(iElem: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IPropertyDescriptionRelatedPropertyInfo(c_void_p):
    extends: win32more.UI.Shell.PropertiesSystem.IPropertyDescription
    Guid = Guid('507393f4-2a3d-4a60-b5-9e-d9-c7-57-16-c2-dd')
    @commethod(24)
    def GetRelatedProperty(pszRelationshipName: win32more.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IPropertyDescriptionSearchInfo(c_void_p):
    extends: win32more.UI.Shell.PropertiesSystem.IPropertyDescription
    Guid = Guid('078f91bd-29a2-440f-92-4e-46-a2-91-52-45-20')
    @commethod(24)
    def GetSearchInfoFlags(ppdsiFlags: POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_SEARCHINFO_FLAGS)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetColumnIndexType(ppdciType: POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_COLUMNINDEX_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetProjectionString(ppszProjection: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def GetMaxSize(pcbMaxSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IPropertyEnumType(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('11e1fbf9-2d56-4a6b-8d-b3-7c-d1-93-a4-71-f2')
    @commethod(3)
    def GetEnumType(penumtype: POINTER(win32more.UI.Shell.PropertiesSystem.PROPENUMTYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetRangeMinValue(ppropvarMin: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRangeSetValue(ppropvarSet: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDisplayText(ppszDisplay: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IPropertyEnumType2(c_void_p):
    extends: win32more.UI.Shell.PropertiesSystem.IPropertyEnumType
    Guid = Guid('9b6e051c-5ddd-4321-90-70-fe-2a-cb-55-e7-94')
    @commethod(8)
    def GetImageReference(ppszImageRes: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IPropertyEnumTypeList(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a99400f4-3d84-4557-94-ba-12-42-fb-2c-c9-a6')
    @commethod(3)
    def GetCount(pctypes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(itype: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetConditionAt(nIndex: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def FindMatchingIndex(propvarCmp: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pnIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IPropertyStore(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('886d8eeb-8cf2-4446-8d-02-cd-ba-1d-bd-cf-99')
    @commethod(3)
    def GetCount(cProps: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(iProp: UInt32, pkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetValue(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pv: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetValue(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Commit() -> win32more.Foundation.HRESULT: ...
class IPropertyStoreCache(c_void_p):
    extends: win32more.UI.Shell.PropertiesSystem.IPropertyStore
    Guid = Guid('3017056d-9a91-4e90-93-7d-74-6c-72-ab-bf-4f')
    @commethod(8)
    def GetState(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pstate: POINTER(win32more.UI.Shell.PropertiesSystem.PSC_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetValueAndState(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pstate: POINTER(win32more.UI.Shell.PropertiesSystem.PSC_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetState(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), state: win32more.UI.Shell.PropertiesSystem.PSC_STATE) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetValueAndState(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), state: win32more.UI.Shell.PropertiesSystem.PSC_STATE) -> win32more.Foundation.HRESULT: ...
class IPropertyStoreCapabilities(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c8e2d566-186e-4d49-bf-41-69-09-ea-d5-6a-cc')
    @commethod(3)
    def IsPropertyWritable(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
class IPropertyStoreFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bc110b6d-57e8-4148-a9-c6-91-01-5a-b2-f3-a5')
    @commethod(3)
    def GetPropertyStore(flags: win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, pUnkFactory: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyStoreForKeys(rgKeys: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), cKeys: UInt32, flags: win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IPropertySystem(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ca724e8a-c3e6-442b-88-a4-6f-b0-db-80-35-a3')
    @commethod(3)
    def GetPropertyDescription(propkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyDescriptionByName(pszCanonicalName: win32more.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyDescriptionListFromString(pszPropList: win32more.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumeratePropertyDescriptions(filterOn: win32more.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def FormatForDisplay(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pdff: win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, pszText: win32more.Foundation.PWSTR, cchText: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def FormatForDisplayAlloc(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pdff: win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS, ppszDisplay: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterPropertySchema(pszPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def UnregisterPropertySchema(pszPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RefreshPropertySchema() -> win32more.Foundation.HRESULT: ...
class IPropertySystemChangeNotify(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fa955fd9-38be-4879-a6-ce-82-4c-f5-2d-60-9f')
    @commethod(3)
    def SchemaRefreshed() -> win32more.Foundation.HRESULT: ...
class IPropertyUI(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('757a7d9f-919a-4118-99-d7-db-b2-08-c8-cc-66')
    @commethod(3)
    def ParsePropertyName(pszName: win32more.Foundation.PWSTR, pfmtid: POINTER(Guid), ppid: POINTER(UInt32), pchEaten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCannonicalName(fmtid: POINTER(Guid), pid: UInt32, pwszText: win32more.Foundation.PWSTR, cchText: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDisplayName(fmtid: POINTER(Guid), pid: UInt32, flags: win32more.UI.Shell.PropertiesSystem.PROPERTYUI_NAME_FLAGS, pwszText: win32more.Foundation.PWSTR, cchText: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyDescription(fmtid: POINTER(Guid), pid: UInt32, pwszText: win32more.Foundation.PWSTR, cchText: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDefaultWidth(fmtid: POINTER(Guid), pid: UInt32, pcxChars: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetFlags(fmtid: POINTER(Guid), pid: UInt32, pflags: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYUI_FLAGS)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def FormatForDisplay(fmtid: POINTER(Guid), pid: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), puiff: win32more.UI.Shell.PropertiesSystem.PROPERTYUI_FORMAT_FLAGS, pwszText: win32more.Foundation.PWSTR, cchText: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetHelpInfo(fmtid: POINTER(Guid), pid: UInt32, pwszHelpFile: win32more.Foundation.PWSTR, cch: UInt32, puHelpID: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
InMemoryPropertyStore = Guid('9a02e012-6303-4e1e-b9-a1-63-0f-80-25-92-c5')
InMemoryPropertyStoreMarshalByValue = Guid('d4ca0e2d-6da7-4b75-a9-7c-5f-30-6f-0e-ae-dc')
PDOPSTATUS = Int32
PDOPS_RUNNING: PDOPSTATUS = 1
PDOPS_PAUSED: PDOPSTATUS = 2
PDOPS_CANCELLED: PDOPSTATUS = 3
PDOPS_STOPPED: PDOPSTATUS = 4
PDOPS_ERRORS: PDOPSTATUS = 5
PKA_FLAGS = UInt32
PKA_SET: PKA_FLAGS = 0
PKA_APPEND: PKA_FLAGS = 1
PKA_DELETE: PKA_FLAGS = 2
PLACEHOLDER_STATES = UInt32
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
PROPDESC_FORMAT_FLAGS = UInt32
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
PROPDESC_SEARCHINFO_FLAGS = UInt32
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
PROPDESC_VIEW_FLAGS = UInt32
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
class PROPERTYKEY(Structure):
    fmtid: Guid
    pid: UInt32
PROPERTYUI_FLAGS = UInt32
PUIF_DEFAULT: PROPERTYUI_FLAGS = 0
PUIF_RIGHTALIGN: PROPERTYUI_FLAGS = 1
PUIF_NOLABELININFOTIP: PROPERTYUI_FLAGS = 2
PROPERTYUI_FORMAT_FLAGS = UInt32
PUIFFDF_DEFAULT: PROPERTYUI_FORMAT_FLAGS = 0
PUIFFDF_RIGHTTOLEFT: PROPERTYUI_FORMAT_FLAGS = 1
PUIFFDF_SHORTFORMAT: PROPERTYUI_FORMAT_FLAGS = 2
PUIFFDF_NOTIME: PROPERTYUI_FORMAT_FLAGS = 4
PUIFFDF_FRIENDLYDATE: PROPERTYUI_FORMAT_FLAGS = 8
PROPERTYUI_NAME_FLAGS = UInt32
PUIFNF_DEFAULT: PROPERTYUI_NAME_FLAGS = 0
PUIFNF_MNEMONIC: PROPERTYUI_NAME_FLAGS = 1
class PROPPRG(Structure):
    flPrg: UInt16
    flPrgInit: UInt16
    achTitle: win32more.Foundation.CHAR * 30
    achCmdLine: win32more.Foundation.CHAR * 128
    achWorkDir: win32more.Foundation.CHAR * 64
    wHotKey: UInt16
    achIconFile: win32more.Foundation.CHAR * 80
    wIconIndex: UInt16
    dwEnhModeFlags: UInt32
    dwRealModeFlags: UInt32
    achOtherFile: win32more.Foundation.CHAR * 80
    achPIFFile: win32more.Foundation.CHAR * 260
    _pack_ = 1
PROPVAR_CHANGE_FLAGS = UInt32
PVCHF_DEFAULT: PROPVAR_CHANGE_FLAGS = 0
PVCHF_NOVALUEPROP: PROPVAR_CHANGE_FLAGS = 1
PVCHF_ALPHABOOL: PROPVAR_CHANGE_FLAGS = 2
PVCHF_NOUSEROVERRIDE: PROPVAR_CHANGE_FLAGS = 4
PVCHF_LOCALBOOL: PROPVAR_CHANGE_FLAGS = 8
PVCHF_NOHEXSTRING: PROPVAR_CHANGE_FLAGS = 16
PROPVAR_COMPARE_FLAGS = UInt32
PVCF_DEFAULT: PROPVAR_COMPARE_FLAGS = 0
PVCF_TREATEMPTYASGREATERTHAN: PROPVAR_COMPARE_FLAGS = 1
PVCF_USESTRCMP: PROPVAR_COMPARE_FLAGS = 2
PVCF_USESTRCMPC: PROPVAR_COMPARE_FLAGS = 4
PVCF_USESTRCMPI: PROPVAR_COMPARE_FLAGS = 8
PVCF_USESTRCMPIC: PROPVAR_COMPARE_FLAGS = 16
PVCF_DIGITSASNUMBERS_CASESENSITIVE: PROPVAR_COMPARE_FLAGS = 32
PROPVAR_COMPARE_UNIT = Int32
PVCU_DEFAULT: PROPVAR_COMPARE_UNIT = 0
PVCU_SECOND: PROPVAR_COMPARE_UNIT = 1
PVCU_MINUTE: PROPVAR_COMPARE_UNIT = 2
PVCU_HOUR: PROPVAR_COMPARE_UNIT = 3
PVCU_DAY: PROPVAR_COMPARE_UNIT = 4
PVCU_MONTH: PROPVAR_COMPARE_UNIT = 5
PVCU_YEAR: PROPVAR_COMPARE_UNIT = 6
PSC_STATE = Int32
PSC_NORMAL: PSC_STATE = 0
PSC_NOTINSOURCE: PSC_STATE = 1
PSC_DIRTY: PSC_STATE = 2
PSC_READONLY: PSC_STATE = 3
PSTIME_FLAGS = UInt32
PSTF_UTC: PSTIME_FLAGS = 0
PSTF_LOCAL: PSTIME_FLAGS = 1
PropertySystem = Guid('b8967f85-58ae-4f46-9f-b2-5d-79-04-79-8f-4b')
class SERIALIZEDPROPSTORAGE(Structure):
    pass
SYNC_ENGINE_STATE_FLAGS = UInt32
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
SYNC_TRANSFER_STATUS = UInt32
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
make_head(_module, 'SERIALIZEDPROPSTORAGE')
__all__ = [
    "ClearPropVariantArray",
    "ClearVariantArray",
    "DPF_ERROR",
    "DPF_MARQUEE",
    "DPF_MARQUEE_COMPLETE",
    "DPF_NONE",
    "DPF_STOPPED",
    "DPF_WARNING",
    "DRAWPROGRESSFLAGS",
    "FPSPS_DEFAULT",
    "FPSPS_READONLY",
    "FPSPS_TREAT_NEW_VALUES_AS_DIRTY",
    "GETPROPERTYSTOREFLAGS",
    "GPS_BESTEFFORT",
    "GPS_DEFAULT",
    "GPS_DELAYCREATION",
    "GPS_EXTRINSICPROPERTIES",
    "GPS_EXTRINSICPROPERTIESONLY",
    "GPS_FASTPROPERTIESONLY",
    "GPS_HANDLERPROPERTIESONLY",
    "GPS_MASK_VALID",
    "GPS_NO_OPLOCK",
    "GPS_OPENSLOWITEM",
    "GPS_PREFERQUERYPROPERTIES",
    "GPS_READWRITE",
    "GPS_TEMPORARY",
    "GPS_VOLATILEPROPERTIES",
    "GPS_VOLATILEPROPERTIESONLY",
    "ICreateObject",
    "IDelayedPropertyStoreFactory",
    "IInitializeWithFile",
    "IInitializeWithStream",
    "INamedPropertyStore",
    "IObjectWithPropertyKey",
    "IPersistSerializedPropStorage",
    "IPersistSerializedPropStorage2",
    "IPropertyChange",
    "IPropertyChangeArray",
    "IPropertyDescription",
    "IPropertyDescription2",
    "IPropertyDescriptionAliasInfo",
    "IPropertyDescriptionList",
    "IPropertyDescriptionRelatedPropertyInfo",
    "IPropertyDescriptionSearchInfo",
    "IPropertyEnumType",
    "IPropertyEnumType2",
    "IPropertyEnumTypeList",
    "IPropertyStore",
    "IPropertyStoreCache",
    "IPropertyStoreCapabilities",
    "IPropertyStoreFactory",
    "IPropertySystem",
    "IPropertySystemChangeNotify",
    "IPropertyUI",
    "InMemoryPropertyStore",
    "InMemoryPropertyStoreMarshalByValue",
    "InitPropVariantFromBooleanVector",
    "InitPropVariantFromBuffer",
    "InitPropVariantFromCLSID",
    "InitPropVariantFromDoubleVector",
    "InitPropVariantFromFileTime",
    "InitPropVariantFromFileTimeVector",
    "InitPropVariantFromGUIDAsString",
    "InitPropVariantFromInt16Vector",
    "InitPropVariantFromInt32Vector",
    "InitPropVariantFromInt64Vector",
    "InitPropVariantFromPropVariantVectorElem",
    "InitPropVariantFromResource",
    "InitPropVariantFromStrRet",
    "InitPropVariantFromStringAsVector",
    "InitPropVariantFromStringVector",
    "InitPropVariantFromUInt16Vector",
    "InitPropVariantFromUInt32Vector",
    "InitPropVariantFromUInt64Vector",
    "InitPropVariantVectorFromPropVariant",
    "InitVariantFromBooleanArray",
    "InitVariantFromBuffer",
    "InitVariantFromDoubleArray",
    "InitVariantFromFileTime",
    "InitVariantFromFileTimeArray",
    "InitVariantFromGUIDAsString",
    "InitVariantFromInt16Array",
    "InitVariantFromInt32Array",
    "InitVariantFromInt64Array",
    "InitVariantFromResource",
    "InitVariantFromStrRet",
    "InitVariantFromStringArray",
    "InitVariantFromUInt16Array",
    "InitVariantFromUInt32Array",
    "InitVariantFromUInt64Array",
    "InitVariantFromVariantArrayElem",
    "PDAT_AVERAGE",
    "PDAT_DATERANGE",
    "PDAT_DEFAULT",
    "PDAT_FIRST",
    "PDAT_MAX",
    "PDAT_MIN",
    "PDAT_SUM",
    "PDAT_UNION",
    "PDCIT_INMEMORY",
    "PDCIT_NONE",
    "PDCIT_ONDEMAND",
    "PDCIT_ONDISK",
    "PDCIT_ONDISKALL",
    "PDCIT_ONDISKVECTOR",
    "PDCOT_BOOLEAN",
    "PDCOT_DATETIME",
    "PDCOT_NONE",
    "PDCOT_NUMBER",
    "PDCOT_SIZE",
    "PDCOT_STRING",
    "PDDT_BOOLEAN",
    "PDDT_DATETIME",
    "PDDT_ENUMERATED",
    "PDDT_NUMBER",
    "PDDT_STRING",
    "PDEF_ALL",
    "PDEF_COLUMN",
    "PDEF_INFULLTEXTQUERY",
    "PDEF_NONSYSTEM",
    "PDEF_QUERYABLE",
    "PDEF_SYSTEM",
    "PDEF_VIEWABLE",
    "PDFF_ALWAYSKB",
    "PDFF_DEFAULT",
    "PDFF_FILENAME",
    "PDFF_HIDEDATE",
    "PDFF_HIDETIME",
    "PDFF_LONGDATE",
    "PDFF_LONGTIME",
    "PDFF_NOAUTOREADINGORDER",
    "PDFF_PREFIXNAME",
    "PDFF_READONLY",
    "PDFF_RELATIVEDATE",
    "PDFF_RESERVED_RIGHTTOLEFT",
    "PDFF_SHORTDATE",
    "PDFF_SHORTTIME",
    "PDFF_USEEDITINVITATION",
    "PDGR_ALPHANUMERIC",
    "PDGR_DATE",
    "PDGR_DISCRETE",
    "PDGR_DYNAMIC",
    "PDGR_ENUMERATED",
    "PDGR_PERCENT",
    "PDGR_SIZE",
    "PDOPSTATUS",
    "PDOPS_CANCELLED",
    "PDOPS_ERRORS",
    "PDOPS_PAUSED",
    "PDOPS_RUNNING",
    "PDOPS_STOPPED",
    "PDRDT_COUNT",
    "PDRDT_DATE",
    "PDRDT_DURATION",
    "PDRDT_GENERAL",
    "PDRDT_LENGTH",
    "PDRDT_PRIORITY",
    "PDRDT_RATE",
    "PDRDT_RATING",
    "PDRDT_REVISION",
    "PDRDT_SIZE",
    "PDRDT_SPEED",
    "PDSD_A_Z",
    "PDSD_GENERAL",
    "PDSD_LOWEST_HIGHEST",
    "PDSD_OLDEST_NEWEST",
    "PDSD_SMALLEST_BIGGEST",
    "PDSIF_ALWAYSINCLUDE",
    "PDSIF_DEFAULT",
    "PDSIF_ININVERTEDINDEX",
    "PDSIF_ISCOLUMN",
    "PDSIF_ISCOLUMNSPARSE",
    "PDSIF_USEFORTYPEAHEAD",
    "PDTF_ALWAYSINSUPPLEMENTALSTORE",
    "PDTF_CANBEPURGED",
    "PDTF_CANGROUPBY",
    "PDTF_CANSTACKBY",
    "PDTF_DEFAULT",
    "PDTF_DONTCOERCEEMPTYSTRINGS",
    "PDTF_INCLUDEINFULLTEXTQUERY",
    "PDTF_ISGROUP",
    "PDTF_ISINNATE",
    "PDTF_ISQUERYABLE",
    "PDTF_ISSYSTEMPROPERTY",
    "PDTF_ISTREEPROPERTY",
    "PDTF_ISVIEWABLE",
    "PDTF_MASK_ALL",
    "PDTF_MULTIPLEVALUES",
    "PDTF_SEARCHRAWVALUE",
    "PDVF_BEGINNEWGROUP",
    "PDVF_CANWRAP",
    "PDVF_CENTERALIGN",
    "PDVF_DEFAULT",
    "PDVF_FILLAREA",
    "PDVF_HIDDEN",
    "PDVF_HIDELABEL",
    "PDVF_MASK_ALL",
    "PDVF_RIGHTALIGN",
    "PDVF_SHOWBYDEFAULT",
    "PDVF_SHOWINPRIMARYLIST",
    "PDVF_SHOWINSECONDARYLIST",
    "PDVF_SHOWONLYIFPRESENT",
    "PDVF_SORTDESCENDING",
    "PET_DEFAULTVALUE",
    "PET_DISCRETEVALUE",
    "PET_ENDRANGE",
    "PET_RANGEDVALUE",
    "PKA_APPEND",
    "PKA_DELETE",
    "PKA_FLAGS",
    "PKA_SET",
    "PKEY_PIDSTR_MAX",
    "PLACEHOLDER_STATES",
    "PROPDESC_AGGREGATION_TYPE",
    "PROPDESC_COLUMNINDEX_TYPE",
    "PROPDESC_CONDITION_TYPE",
    "PROPDESC_DISPLAYTYPE",
    "PROPDESC_ENUMFILTER",
    "PROPDESC_FORMAT_FLAGS",
    "PROPDESC_GROUPING_RANGE",
    "PROPDESC_RELATIVEDESCRIPTION_TYPE",
    "PROPDESC_SEARCHINFO_FLAGS",
    "PROPDESC_SORTDESCRIPTION",
    "PROPDESC_TYPE_FLAGS",
    "PROPDESC_VIEW_FLAGS",
    "PROPENUMTYPE",
    "PROPERTYKEY",
    "PROPERTYUI_FLAGS",
    "PROPERTYUI_FORMAT_FLAGS",
    "PROPERTYUI_NAME_FLAGS",
    "PROPPRG",
    "PROPVAR_CHANGE_FLAGS",
    "PROPVAR_COMPARE_FLAGS",
    "PROPVAR_COMPARE_UNIT",
    "PSC_DIRTY",
    "PSC_NORMAL",
    "PSC_NOTINSOURCE",
    "PSC_READONLY",
    "PSC_STATE",
    "PSCoerceToCanonicalValue",
    "PSCreateAdapterFromPropertyStore",
    "PSCreateDelayedMultiplexPropertyStore",
    "PSCreateMemoryPropertyStore",
    "PSCreateMultiplexPropertyStore",
    "PSCreatePropertyChangeArray",
    "PSCreatePropertyStoreFromObject",
    "PSCreatePropertyStoreFromPropertySetStorage",
    "PSCreateSimplePropertyChange",
    "PSEnumeratePropertyDescriptions",
    "PSFormatForDisplay",
    "PSFormatForDisplayAlloc",
    "PSFormatPropertyValue",
    "PSGetImageReferenceForValue",
    "PSGetItemPropertyHandler",
    "PSGetItemPropertyHandlerWithCreateObject",
    "PSGetNameFromPropertyKey",
    "PSGetNamedPropertyFromPropertyStorage",
    "PSGetPropertyDescription",
    "PSGetPropertyDescriptionByName",
    "PSGetPropertyDescriptionListFromString",
    "PSGetPropertyFromPropertyStorage",
    "PSGetPropertyKeyFromName",
    "PSGetPropertySystem",
    "PSGetPropertyValue",
    "PSLookupPropertyHandlerCLSID",
    "PSPropertyBag_Delete",
    "PSPropertyBag_ReadBOOL",
    "PSPropertyBag_ReadBSTR",
    "PSPropertyBag_ReadDWORD",
    "PSPropertyBag_ReadGUID",
    "PSPropertyBag_ReadInt",
    "PSPropertyBag_ReadLONG",
    "PSPropertyBag_ReadPOINTL",
    "PSPropertyBag_ReadPOINTS",
    "PSPropertyBag_ReadPropertyKey",
    "PSPropertyBag_ReadRECTL",
    "PSPropertyBag_ReadSHORT",
    "PSPropertyBag_ReadStr",
    "PSPropertyBag_ReadStrAlloc",
    "PSPropertyBag_ReadStream",
    "PSPropertyBag_ReadType",
    "PSPropertyBag_ReadULONGLONG",
    "PSPropertyBag_ReadUnknown",
    "PSPropertyBag_WriteBOOL",
    "PSPropertyBag_WriteBSTR",
    "PSPropertyBag_WriteDWORD",
    "PSPropertyBag_WriteGUID",
    "PSPropertyBag_WriteInt",
    "PSPropertyBag_WriteLONG",
    "PSPropertyBag_WritePOINTL",
    "PSPropertyBag_WritePOINTS",
    "PSPropertyBag_WritePropertyKey",
    "PSPropertyBag_WriteRECTL",
    "PSPropertyBag_WriteSHORT",
    "PSPropertyBag_WriteStr",
    "PSPropertyBag_WriteStream",
    "PSPropertyBag_WriteULONGLONG",
    "PSPropertyBag_WriteUnknown",
    "PSPropertyKeyFromString",
    "PSRefreshPropertySchema",
    "PSRegisterPropertySchema",
    "PSSetPropertyValue",
    "PSStringFromPropertyKey",
    "PSTF_LOCAL",
    "PSTF_UTC",
    "PSTIME_FLAGS",
    "PSUnregisterPropertySchema",
    "PS_ALL",
    "PS_CLOUDFILE_PLACEHOLDER",
    "PS_CREATE_FILE_ACCESSIBLE",
    "PS_DEFAULT",
    "PS_FULL_PRIMARY_STREAM_AVAILABLE",
    "PS_MARKED_FOR_OFFLINE_AVAILABILITY",
    "PS_NONE",
    "PUIFFDF_DEFAULT",
    "PUIFFDF_FRIENDLYDATE",
    "PUIFFDF_NOTIME",
    "PUIFFDF_RIGHTTOLEFT",
    "PUIFFDF_SHORTFORMAT",
    "PUIFNF_DEFAULT",
    "PUIFNF_MNEMONIC",
    "PUIF_DEFAULT",
    "PUIF_NOLABELININFOTIP",
    "PUIF_RIGHTALIGN",
    "PVCF_DEFAULT",
    "PVCF_DIGITSASNUMBERS_CASESENSITIVE",
    "PVCF_TREATEMPTYASGREATERTHAN",
    "PVCF_USESTRCMP",
    "PVCF_USESTRCMPC",
    "PVCF_USESTRCMPI",
    "PVCF_USESTRCMPIC",
    "PVCHF_ALPHABOOL",
    "PVCHF_DEFAULT",
    "PVCHF_LOCALBOOL",
    "PVCHF_NOHEXSTRING",
    "PVCHF_NOUSEROVERRIDE",
    "PVCHF_NOVALUEPROP",
    "PVCU_DAY",
    "PVCU_DEFAULT",
    "PVCU_HOUR",
    "PVCU_MINUTE",
    "PVCU_MONTH",
    "PVCU_SECOND",
    "PVCU_YEAR",
    "PifMgr_CloseProperties",
    "PifMgr_GetProperties",
    "PifMgr_OpenProperties",
    "PifMgr_SetProperties",
    "PropVariantChangeType",
    "PropVariantCompareEx",
    "PropVariantGetBooleanElem",
    "PropVariantGetDoubleElem",
    "PropVariantGetElementCount",
    "PropVariantGetFileTimeElem",
    "PropVariantGetInt16Elem",
    "PropVariantGetInt32Elem",
    "PropVariantGetInt64Elem",
    "PropVariantGetStringElem",
    "PropVariantGetUInt16Elem",
    "PropVariantGetUInt32Elem",
    "PropVariantGetUInt64Elem",
    "PropVariantToBSTR",
    "PropVariantToBoolean",
    "PropVariantToBooleanVector",
    "PropVariantToBooleanVectorAlloc",
    "PropVariantToBooleanWithDefault",
    "PropVariantToBuffer",
    "PropVariantToDouble",
    "PropVariantToDoubleVector",
    "PropVariantToDoubleVectorAlloc",
    "PropVariantToDoubleWithDefault",
    "PropVariantToFileTime",
    "PropVariantToFileTimeVector",
    "PropVariantToFileTimeVectorAlloc",
    "PropVariantToGUID",
    "PropVariantToInt16",
    "PropVariantToInt16Vector",
    "PropVariantToInt16VectorAlloc",
    "PropVariantToInt16WithDefault",
    "PropVariantToInt32",
    "PropVariantToInt32Vector",
    "PropVariantToInt32VectorAlloc",
    "PropVariantToInt32WithDefault",
    "PropVariantToInt64",
    "PropVariantToInt64Vector",
    "PropVariantToInt64VectorAlloc",
    "PropVariantToInt64WithDefault",
    "PropVariantToStrRet",
    "PropVariantToString",
    "PropVariantToStringAlloc",
    "PropVariantToStringVector",
    "PropVariantToStringVectorAlloc",
    "PropVariantToStringWithDefault",
    "PropVariantToUInt16",
    "PropVariantToUInt16Vector",
    "PropVariantToUInt16VectorAlloc",
    "PropVariantToUInt16WithDefault",
    "PropVariantToUInt32",
    "PropVariantToUInt32Vector",
    "PropVariantToUInt32VectorAlloc",
    "PropVariantToUInt32WithDefault",
    "PropVariantToUInt64",
    "PropVariantToUInt64Vector",
    "PropVariantToUInt64VectorAlloc",
    "PropVariantToUInt64WithDefault",
    "PropVariantToVariant",
    "PropVariantToWinRTPropertyValue",
    "PropertySystem",
    "SERIALIZEDPROPSTORAGE",
    "SESF_ALL_FLAGS",
    "SESF_AUTHENTICATION_ERROR",
    "SESF_NONE",
    "SESF_PAUSED_DUE_TO_CLIENT_POLICY",
    "SESF_PAUSED_DUE_TO_DISK_SPACE_FULL",
    "SESF_PAUSED_DUE_TO_METERED_NETWORK",
    "SESF_PAUSED_DUE_TO_SERVICE_POLICY",
    "SESF_PAUSED_DUE_TO_USER_REQUEST",
    "SESF_SERVICE_QUOTA_EXCEEDED_LIMIT",
    "SESF_SERVICE_QUOTA_NEARING_LIMIT",
    "SESF_SERVICE_UNAVAILABLE",
    "SHAddDefaultPropertiesByExt",
    "SHGetPropertyStoreForWindow",
    "SHGetPropertyStoreFromIDList",
    "SHGetPropertyStoreFromParsingName",
    "SHPropStgCreate",
    "SHPropStgReadMultiple",
    "SHPropStgWriteMultiple",
    "STS_EXCLUDED",
    "STS_FETCHING_METADATA",
    "STS_HASERROR",
    "STS_HASWARNING",
    "STS_INCOMPLETE",
    "STS_NEEDSDOWNLOAD",
    "STS_NEEDSUPLOAD",
    "STS_NONE",
    "STS_PAUSED",
    "STS_PLACEHOLDER_IFEMPTY",
    "STS_TRANSFERRING",
    "STS_USER_REQUESTED_REFRESH",
    "SYNC_ENGINE_STATE_FLAGS",
    "SYNC_TRANSFER_STATUS",
    "VariantCompare",
    "VariantGetBooleanElem",
    "VariantGetDoubleElem",
    "VariantGetElementCount",
    "VariantGetInt16Elem",
    "VariantGetInt32Elem",
    "VariantGetInt64Elem",
    "VariantGetStringElem",
    "VariantGetUInt16Elem",
    "VariantGetUInt32Elem",
    "VariantGetUInt64Elem",
    "VariantToBoolean",
    "VariantToBooleanArray",
    "VariantToBooleanArrayAlloc",
    "VariantToBooleanWithDefault",
    "VariantToBuffer",
    "VariantToDosDateTime",
    "VariantToDouble",
    "VariantToDoubleArray",
    "VariantToDoubleArrayAlloc",
    "VariantToDoubleWithDefault",
    "VariantToFileTime",
    "VariantToGUID",
    "VariantToInt16",
    "VariantToInt16Array",
    "VariantToInt16ArrayAlloc",
    "VariantToInt16WithDefault",
    "VariantToInt32",
    "VariantToInt32Array",
    "VariantToInt32ArrayAlloc",
    "VariantToInt32WithDefault",
    "VariantToInt64",
    "VariantToInt64Array",
    "VariantToInt64ArrayAlloc",
    "VariantToInt64WithDefault",
    "VariantToPropVariant",
    "VariantToStrRet",
    "VariantToString",
    "VariantToStringAlloc",
    "VariantToStringArray",
    "VariantToStringArrayAlloc",
    "VariantToStringWithDefault",
    "VariantToUInt16",
    "VariantToUInt16Array",
    "VariantToUInt16ArrayAlloc",
    "VariantToUInt16WithDefault",
    "VariantToUInt32",
    "VariantToUInt32Array",
    "VariantToUInt32ArrayAlloc",
    "VariantToUInt32WithDefault",
    "VariantToUInt64",
    "VariantToUInt64Array",
    "VariantToUInt64ArrayAlloc",
    "VariantToUInt64WithDefault",
    "WinRTPropertyValueToPropVariant",
    "_PERSIST_SPROPSTORE_FLAGS",
]
_arch_optional = [
]
