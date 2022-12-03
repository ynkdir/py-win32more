from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
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
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
_PERSIST_SPROPSTORE_FLAGS = Int32
FPSPS_DEFAULT = 0
FPSPS_READONLY = 1
FPSPS_TREAT_NEW_VALUES_AS_DIRTY = 2
PKEY_PIDSTR_MAX = 10
def _define_PropVariantToWinRTPropertyValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Guid),POINTER(c_void_p))(('PropVariantToWinRTPropertyValue', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinRTPropertyValueToPropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('WinRTPropertyValueToPropVariant', windll['PROPSYS.dll']), ((1, 'punkPropertyValue'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSFormatForDisplay():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,win32more.Foundation.PWSTR,UInt32)(('PSFormatForDisplay', windll['PROPSYS.dll']), ((1, 'propkey'),(1, 'propvar'),(1, 'pdfFlags'),(1, 'pwszText'),(1, 'cchText'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSFormatForDisplayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,POINTER(win32more.Foundation.PWSTR))(('PSFormatForDisplayAlloc', windll['PROPSYS.dll']), ((1, 'key'),(1, 'propvar'),(1, 'pdff'),(1, 'ppszDisplay'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSFormatPropertyValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head,win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head,win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,POINTER(win32more.Foundation.PWSTR))(('PSFormatPropertyValue', windll['PROPSYS.dll']), ((1, 'pps'),(1, 'ppd'),(1, 'pdff'),(1, 'ppszDisplay'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetImageReferenceForValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.PWSTR))(('PSGetImageReferenceForValue', windll['PROPSYS.dll']), ((1, 'propkey'),(1, 'propvar'),(1, 'ppszImageRes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSStringFromPropertyKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Foundation.PWSTR,UInt32)(('PSStringFromPropertyKey', windll['PROPSYS.dll']), ((1, 'pkey'),(1, 'psz'),(1, 'cch'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyKeyFromString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(('PSPropertyKeyFromString', windll['PROPSYS.dll']), ((1, 'pszString'),(1, 'pkey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreateMemoryPropertyStore():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(('PSCreateMemoryPropertyStore', windll['PROPSYS.dll']), ((1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreateDelayedMultiplexPropertyStore():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,win32more.UI.Shell.PropertiesSystem.IDelayedPropertyStoreFactory_head,POINTER(UInt32),UInt32,POINTER(Guid),POINTER(c_void_p))(('PSCreateDelayedMultiplexPropertyStore', windll['PROPSYS.dll']), ((1, 'flags'),(1, 'pdpsf'),(1, 'rgStoreIds'),(1, 'cStores'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreateMultiplexPropertyStore():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head),UInt32,POINTER(Guid),POINTER(c_void_p))(('PSCreateMultiplexPropertyStore', windll['PROPSYS.dll']), ((1, 'prgpunkStores'),(1, 'cStores'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreatePropertyChangeArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.UI.Shell.PropertiesSystem.PKA_FLAGS),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(Guid),POINTER(c_void_p))(('PSCreatePropertyChangeArray', windll['PROPSYS.dll']), ((1, 'rgpropkey'),(1, 'rgflags'),(1, 'rgpropvar'),(1, 'cChanges'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreateSimplePropertyChange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.PKA_FLAGS,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Guid),POINTER(c_void_p))(('PSCreateSimplePropertyChange', windll['PROPSYS.dll']), ((1, 'flags'),(1, 'key'),(1, 'propvar'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyDescription():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Guid),POINTER(c_void_p))(('PSGetPropertyDescription', windll['PROPSYS.dll']), ((1, 'propkey'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyDescriptionByName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p))(('PSGetPropertyDescriptionByName', windll['PROPSYS.dll']), ((1, 'pszCanonicalName'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSLookupPropertyHandlerCLSID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid))(('PSLookupPropertyHandlerCLSID', windll['PROPSYS.dll']), ((1, 'pszFilePath'),(1, 'pclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetItemPropertyHandler():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL,POINTER(Guid),POINTER(c_void_p))(('PSGetItemPropertyHandler', windll['PROPSYS.dll']), ((1, 'punkItem'),(1, 'fReadWrite'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetItemPropertyHandlerWithCreateObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(('PSGetItemPropertyHandlerWithCreateObject', windll['PROPSYS.dll']), ((1, 'punkItem'),(1, 'fReadWrite'),(1, 'punkCreateObject'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head,win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('PSGetPropertyValue', windll['PROPSYS.dll']), ((1, 'pps'),(1, 'ppd'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSSetPropertyValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head,win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('PSSetPropertyValue', windll['PROPSYS.dll']), ((1, 'pps'),(1, 'ppd'),(1, 'propvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSRegisterPropertySchema():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('PSRegisterPropertySchema', windll['PROPSYS.dll']), ((1, 'pszPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSUnregisterPropertySchema():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('PSUnregisterPropertySchema', windll['PROPSYS.dll']), ((1, 'pszPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSRefreshPropertySchema():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('PSRefreshPropertySchema', windll['PROPSYS.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSEnumeratePropertyDescriptions():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER,POINTER(Guid),POINTER(c_void_p))(('PSEnumeratePropertyDescriptions', windll['PROPSYS.dll']), ((1, 'filterOn'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyKeyFromName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(('PSGetPropertyKeyFromName', windll['PROPSYS.dll']), ((1, 'pszName'),(1, 'ppropkey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetNameFromPropertyKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.PWSTR))(('PSGetNameFromPropertyKey', windll['PROPSYS.dll']), ((1, 'propkey'),(1, 'ppszCanonicalName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCoerceToCanonicalValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('PSCoerceToCanonicalValue', windll['PROPSYS.dll']), ((1, 'key'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyDescriptionListFromString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p))(('PSGetPropertyDescriptionListFromString', windll['PROPSYS.dll']), ((1, 'pszPropList'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreatePropertyStoreFromPropertySetStorage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertySetStorage_head,UInt32,POINTER(Guid),POINTER(c_void_p))(('PSCreatePropertyStoreFromPropertySetStorage', windll['PROPSYS.dll']), ((1, 'ppss'),(1, 'grfMode'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreatePropertyStoreFromObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(Guid),POINTER(c_void_p))(('PSCreatePropertyStoreFromObject', windll['PROPSYS.dll']), ((1, 'punk'),(1, 'grfMode'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSCreateAdapterFromPropertyStore():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head,POINTER(Guid),POINTER(c_void_p))(('PSCreateAdapterFromPropertyStore', windll['PROPSYS.dll']), ((1, 'pps'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertySystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(('PSGetPropertySystem', windll['PROPSYS.dll']), ((1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetPropertyFromPropertyStorage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head),UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('PSGetPropertyFromPropertyStorage', windll['PROPSYS.dll']), ((1, 'psps'),(1, 'cb'),(1, 'rpkey'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSGetNamedPropertyFromPropertyStorage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head),UInt32,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('PSGetNamedPropertyFromPropertyStorage', windll['PROPSYS.dll']), ((1, 'psps'),(1, 'cb'),(1, 'pszName'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.System.Com.VARENUM)(('PSPropertyBag_ReadType', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'var'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32)(('PSPropertyBag_ReadStr', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),(1, 'characterCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadStrAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('PSPropertyBag_ReadStrAlloc', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadBSTR():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BSTR))(('PSPropertyBag_ReadBSTR', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('PSPropertyBag_WriteStr', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteBSTR():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,win32more.Foundation.BSTR)(('PSPropertyBag_WriteBSTR', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadInt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Int32))(('PSPropertyBag_ReadInt', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteInt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,Int32)(('PSPropertyBag_WriteInt', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadSHORT():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Int16))(('PSPropertyBag_ReadSHORT', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteSHORT():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,Int16)(('PSPropertyBag_WriteSHORT', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadLONG():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Int32))(('PSPropertyBag_ReadLONG', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteLONG():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,Int32)(('PSPropertyBag_WriteLONG', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadDWORD():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(UInt32))(('PSPropertyBag_ReadDWORD', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteDWORD():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,UInt32)(('PSPropertyBag_WriteDWORD', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadBOOL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL))(('PSPropertyBag_ReadBOOL', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteBOOL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(('PSPropertyBag_WriteBOOL', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadPOINTL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.POINTL_head))(('PSPropertyBag_ReadPOINTL', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WritePOINTL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.POINTL_head))(('PSPropertyBag_WritePOINTL', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadPOINTS():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.POINTS_head))(('PSPropertyBag_ReadPOINTS', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WritePOINTS():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.POINTS_head))(('PSPropertyBag_WritePOINTS', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadRECTL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.RECTL_head))(('PSPropertyBag_ReadRECTL', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteRECTL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.RECTL_head))(('PSPropertyBag_WriteRECTL', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IStream_head))(('PSPropertyBag_ReadStream', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head)(('PSPropertyBag_WriteStream', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_Delete():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR)(('PSPropertyBag_Delete', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadULONGLONG():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(UInt64))(('PSPropertyBag_ReadULONGLONG', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteULONGLONG():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,UInt64)(('PSPropertyBag_WriteULONGLONG', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadUnknown():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p))(('PSPropertyBag_ReadUnknown', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteUnknown():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head)(('PSPropertyBag_WriteUnknown', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'punk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadGUID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Guid))(('PSPropertyBag_ReadGUID', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WriteGUID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(Guid))(('PSPropertyBag_WriteGUID', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_ReadPropertyKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(('PSPropertyBag_ReadPropertyKey', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PSPropertyBag_WritePropertyKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(('PSPropertyBag_WritePropertyKey', windll['PROPSYS.dll']), ((1, 'propBag'),(1, 'propName'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromResource():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromResource', windll['PROPSYS.dll']), ((1, 'hinst'),(1, 'id'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromBuffer', windll['PROPSYS.dll']), ((1, 'pv'),(1, 'cb'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromCLSID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromCLSID', windll['PROPSYS.dll']), ((1, 'clsid'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromGUIDAsString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromGUIDAsString', windll['PROPSYS.dll']), ((1, 'guid'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromFileTime', windll['PROPSYS.dll']), ((1, 'pftIn'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromPropVariantVectorElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromPropVariantVectorElem', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'iElem'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantVectorFromPropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantVectorFromPropVariant', windll['PROPSYS.dll']), ((1, 'propvarSingle'),(1, 'ppropvarVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromStrRet():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.Common.STRRET_head),POINTER(win32more.UI.Shell.Common.ITEMIDLIST_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromStrRet', windll['PROPSYS.dll']), ((1, 'pstrret'),(1, 'pidl'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromBooleanVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromBooleanVector', windll['PROPSYS.dll']), ((1, 'prgf'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromInt16Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromInt16Vector', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromUInt16Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromUInt16Vector', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromInt32Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromInt32Vector', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromUInt32Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromUInt32Vector', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromInt64Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromInt64Vector', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromUInt64Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromUInt64Vector', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromDoubleVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromDoubleVector', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromFileTimeVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromFileTimeVector', windll['PROPSYS.dll']), ((1, 'prgft'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromStringVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromStringVector', windll['PROPSYS.dll']), ((1, 'prgsz'),(1, 'cElems'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromStringAsVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromStringAsVector', windll['PROPSYS.dll']), ((1, 'psz'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBooleanWithDefault():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.Foundation.BOOL)(('PropVariantToBooleanWithDefault', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'fDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt16WithDefault():
    try:
        return WINFUNCTYPE(Int16,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),Int16)(('PropVariantToInt16WithDefault', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'iDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt16WithDefault():
    try:
        return WINFUNCTYPE(UInt16,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt16)(('PropVariantToUInt16WithDefault', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'uiDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt32WithDefault():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),Int32)(('PropVariantToInt32WithDefault', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'lDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt32WithDefault():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32)(('PropVariantToUInt32WithDefault', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'ulDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt64WithDefault():
    try:
        return WINFUNCTYPE(Int64,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),Int64)(('PropVariantToInt64WithDefault', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'llDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt64WithDefault():
    try:
        return WINFUNCTYPE(UInt64,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt64)(('PropVariantToUInt64WithDefault', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'ullDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToDoubleWithDefault():
    try:
        return WINFUNCTYPE(Double,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),Double)(('PropVariantToDoubleWithDefault', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'dblDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToStringWithDefault():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.Foundation.PWSTR)(('PropVariantToStringWithDefault', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'pszDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBoolean():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.BOOL))(('PropVariantToBoolean', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'pfRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt16():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int16))(('PropVariantToInt16', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'piRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt16():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt16))(('PropVariantToUInt16', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'puiRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt32():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int32))(('PropVariantToInt32', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'plRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt32():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32))(('PropVariantToUInt32', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'pulRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int64))(('PropVariantToInt64', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'pllRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt64))(('PropVariantToUInt64', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'pullRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToDouble():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Double))(('PropVariantToDouble', windll['PROPSYS.dll']), ((1, 'propvarIn'),(1, 'pdblRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),c_void_p,UInt32)(('PropVariantToBuffer', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pv'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.Foundation.PWSTR,UInt32)(('PropVariantToString', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'psz'),(1, 'cch'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToGUID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Guid))(('PropVariantToGUID', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pguid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToStringAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.PWSTR))(('PropVariantToStringAlloc', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'ppszOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBSTR():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.BSTR))(('PropVariantToBSTR', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToStrRet():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.UI.Shell.Common.STRRET_head))(('PropVariantToStrRet', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pstrret'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PSTIME_FLAGS,POINTER(win32more.Foundation.FILETIME_head))(('PropVariantToFileTime', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pstfOut'),(1, 'pftOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetElementCount():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('PropVariantGetElementCount', windll['PROPSYS.dll']), ((1, 'propvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBooleanVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.BOOL),UInt32,POINTER(UInt32))(('PropVariantToBooleanVector', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'prgf'),(1, 'crgf'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt16Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int16),UInt32,POINTER(UInt32))(('PropVariantToInt16Vector', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt16Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt16),UInt32,POINTER(UInt32))(('PropVariantToUInt16Vector', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt32Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int32),UInt32,POINTER(UInt32))(('PropVariantToInt32Vector', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt32Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32),UInt32,POINTER(UInt32))(('PropVariantToUInt32Vector', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt64Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Int64),UInt32,POINTER(UInt32))(('PropVariantToInt64Vector', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt64Vector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt64),UInt32,POINTER(UInt32))(('PropVariantToUInt64Vector', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToDoubleVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(Double),UInt32,POINTER(UInt32))(('PropVariantToDoubleVector', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToFileTimeVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.FILETIME_head),UInt32,POINTER(UInt32))(('PropVariantToFileTimeVector', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'prgft'),(1, 'crgft'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToStringVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(UInt32))(('PropVariantToStringVector', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'prgsz'),(1, 'crgsz'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToBooleanVectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(win32more.Foundation.BOOL)),POINTER(UInt32))(('PropVariantToBooleanVectorAlloc', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pprgf'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt16VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(Int16)),POINTER(UInt32))(('PropVariantToInt16VectorAlloc', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt16VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(UInt16)),POINTER(UInt32))(('PropVariantToUInt16VectorAlloc', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt32VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(Int32)),POINTER(UInt32))(('PropVariantToInt32VectorAlloc', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt32VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(UInt32)),POINTER(UInt32))(('PropVariantToUInt32VectorAlloc', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToInt64VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(Int64)),POINTER(UInt32))(('PropVariantToInt64VectorAlloc', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToUInt64VectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(UInt64)),POINTER(UInt32))(('PropVariantToUInt64VectorAlloc', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToDoubleVectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(Double)),POINTER(UInt32))(('PropVariantToDoubleVectorAlloc', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToFileTimeVectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(win32more.Foundation.FILETIME_head)),POINTER(UInt32))(('PropVariantToFileTimeVectorAlloc', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pprgft'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToStringVectorAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32))(('PropVariantToStringVectorAlloc', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'pprgsz'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetBooleanElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(win32more.Foundation.BOOL))(('PropVariantGetBooleanElem', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'iElem'),(1, 'pfVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetInt16Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(Int16))(('PropVariantGetInt16Elem', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetUInt16Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(UInt16))(('PropVariantGetUInt16Elem', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetInt32Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(Int32))(('PropVariantGetInt32Elem', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetUInt32Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(UInt32))(('PropVariantGetUInt32Elem', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetInt64Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(Int64))(('PropVariantGetInt64Elem', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetUInt64Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(UInt64))(('PropVariantGetUInt64Elem', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetDoubleElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(Double))(('PropVariantGetDoubleElem', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetFileTimeElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(win32more.Foundation.FILETIME_head))(('PropVariantGetFileTimeElem', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'iElem'),(1, 'pftVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetStringElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32,POINTER(win32more.Foundation.PWSTR))(('PropVariantGetStringElem', windll['PROPSYS.dll']), ((1, 'propvar'),(1, 'iElem'),(1, 'ppszVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClearPropVariantArray():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32)(('ClearPropVariantArray', windll['PROPSYS.dll']), ((1, 'rgPropVar'),(1, 'cVars'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantCompareEx():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPVAR_COMPARE_UNIT,win32more.UI.Shell.PropertiesSystem.PROPVAR_COMPARE_FLAGS)(('PropVariantCompareEx', windll['PROPSYS.dll']), ((1, 'propvar1'),(1, 'propvar2'),(1, 'unit'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantChangeType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPVAR_CHANGE_FLAGS,win32more.System.Com.VARENUM)(('PropVariantChangeType', windll['PROPSYS.dll']), ((1, 'ppropvarDest'),(1, 'propvarSrc'),(1, 'flags'),(1, 'vt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.VARIANT_head))(('PropVariantToVariant', windll['PROPSYS.dll']), ((1, 'pPropVar'),(1, 'pVar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToPropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('VariantToPropVariant', windll['PROPSYS.dll']), ((1, 'pVar'),(1, 'pPropVar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromResource():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromResource', windll['PROPSYS.dll']), ((1, 'hinst'),(1, 'id'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromBuffer', windll['PROPSYS.dll']), ((1, 'pv'),(1, 'cb'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromGUIDAsString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromGUIDAsString', windll['PROPSYS.dll']), ((1, 'guid'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromFileTime', windll['PROPSYS.dll']), ((1, 'pft'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromFileTimeArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromFileTimeArray', windll['PROPSYS.dll']), ((1, 'prgft'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromStrRet():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.Common.STRRET_head),POINTER(win32more.UI.Shell.Common.ITEMIDLIST_head),POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromStrRet', windll['PROPSYS.dll']), ((1, 'pstrret'),(1, 'pidl'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromVariantArrayElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromVariantArrayElem', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'iElem'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromBooleanArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromBooleanArray', windll['PROPSYS.dll']), ((1, 'prgf'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromInt16Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromInt16Array', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromUInt16Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromUInt16Array', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromInt32Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromInt32Array', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromUInt32Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromUInt32Array', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromInt64Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromInt64Array', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromUInt64Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromUInt64Array', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromDoubleArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromDoubleArray', windll['PROPSYS.dll']), ((1, 'prgn'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitVariantFromStringArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('InitVariantFromStringArray', windll['PROPSYS.dll']), ((1, 'prgsz'),(1, 'cElems'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToBooleanWithDefault():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BOOL)(('VariantToBooleanWithDefault', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'fDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt16WithDefault():
    try:
        return WINFUNCTYPE(Int16,POINTER(win32more.System.Com.VARIANT_head),Int16)(('VariantToInt16WithDefault', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'iDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt16WithDefault():
    try:
        return WINFUNCTYPE(UInt16,POINTER(win32more.System.Com.VARIANT_head),UInt16)(('VariantToUInt16WithDefault', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'uiDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt32WithDefault():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Com.VARIANT_head),Int32)(('VariantToInt32WithDefault', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'lDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt32WithDefault():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Com.VARIANT_head),UInt32)(('VariantToUInt32WithDefault', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'ulDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt64WithDefault():
    try:
        return WINFUNCTYPE(Int64,POINTER(win32more.System.Com.VARIANT_head),Int64)(('VariantToInt64WithDefault', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'llDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt64WithDefault():
    try:
        return WINFUNCTYPE(UInt64,POINTER(win32more.System.Com.VARIANT_head),UInt64)(('VariantToUInt64WithDefault', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'ullDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToDoubleWithDefault():
    try:
        return WINFUNCTYPE(Double,POINTER(win32more.System.Com.VARIANT_head),Double)(('VariantToDoubleWithDefault', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'dblDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToStringWithDefault():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.PWSTR)(('VariantToStringWithDefault', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'pszDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToBoolean():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.BOOL))(('VariantToBoolean', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'pfRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt16():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int16))(('VariantToInt16', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'piRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt16():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt16))(('VariantToUInt16', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'puiRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt32():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32))(('VariantToInt32', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'plRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt32():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt32))(('VariantToUInt32', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'pulRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int64))(('VariantToInt64', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'pllRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt64))(('VariantToUInt64', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'pullRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToDouble():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Double))(('VariantToDouble', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'pdblRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),c_void_p,UInt32)(('VariantToBuffer', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'pv'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToGUID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Guid))(('VariantToGUID', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'pguid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.PWSTR,UInt32)(('VariantToString', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'pszBuf'),(1, 'cchBuf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToStringAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.PWSTR))(('VariantToStringAlloc', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'ppszBuf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToDosDateTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt16),POINTER(UInt16))(('VariantToDosDateTime', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'pwDate'),(1, 'pwTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToStrRet():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.UI.Shell.Common.STRRET_head))(('VariantToStrRet', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'pstrret'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),win32more.UI.Shell.PropertiesSystem.PSTIME_FLAGS,POINTER(win32more.Foundation.FILETIME_head))(('VariantToFileTime', windll['PROPSYS.dll']), ((1, 'varIn'),(1, 'stfOut'),(1, 'pftOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetElementCount():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Com.VARIANT_head))(('VariantGetElementCount', windll['PROPSYS.dll']), ((1, 'varIn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToBooleanArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.BOOL),UInt32,POINTER(UInt32))(('VariantToBooleanArray', windll['PROPSYS.dll']), ((1, 'var'),(1, 'prgf'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt16Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int16),UInt32,POINTER(UInt32))(('VariantToInt16Array', windll['PROPSYS.dll']), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt16Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt16),UInt32,POINTER(UInt32))(('VariantToUInt16Array', windll['PROPSYS.dll']), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt32Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32),UInt32,POINTER(UInt32))(('VariantToInt32Array', windll['PROPSYS.dll']), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt32Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt32),UInt32,POINTER(UInt32))(('VariantToUInt32Array', windll['PROPSYS.dll']), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt64Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int64),UInt32,POINTER(UInt32))(('VariantToInt64Array', windll['PROPSYS.dll']), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt64Array():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt64),UInt32,POINTER(UInt32))(('VariantToUInt64Array', windll['PROPSYS.dll']), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToDoubleArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Double),UInt32,POINTER(UInt32))(('VariantToDoubleArray', windll['PROPSYS.dll']), ((1, 'var'),(1, 'prgn'),(1, 'crgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToStringArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(UInt32))(('VariantToStringArray', windll['PROPSYS.dll']), ((1, 'var'),(1, 'prgsz'),(1, 'crgsz'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToBooleanArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(win32more.Foundation.BOOL)),POINTER(UInt32))(('VariantToBooleanArrayAlloc', windll['PROPSYS.dll']), ((1, 'var'),(1, 'pprgf'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt16ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(Int16)),POINTER(UInt32))(('VariantToInt16ArrayAlloc', windll['PROPSYS.dll']), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt16ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(UInt16)),POINTER(UInt32))(('VariantToUInt16ArrayAlloc', windll['PROPSYS.dll']), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt32ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(Int32)),POINTER(UInt32))(('VariantToInt32ArrayAlloc', windll['PROPSYS.dll']), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt32ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(UInt32)),POINTER(UInt32))(('VariantToUInt32ArrayAlloc', windll['PROPSYS.dll']), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToInt64ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(Int64)),POINTER(UInt32))(('VariantToInt64ArrayAlloc', windll['PROPSYS.dll']), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToUInt64ArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(UInt64)),POINTER(UInt32))(('VariantToUInt64ArrayAlloc', windll['PROPSYS.dll']), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToDoubleArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(Double)),POINTER(UInt32))(('VariantToDoubleArrayAlloc', windll['PROPSYS.dll']), ((1, 'var'),(1, 'pprgn'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantToStringArrayAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32))(('VariantToStringArrayAlloc', windll['PROPSYS.dll']), ((1, 'var'),(1, 'pprgsz'),(1, 'pcElem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetBooleanElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(win32more.Foundation.BOOL))(('VariantGetBooleanElem', windll['PROPSYS.dll']), ((1, 'var'),(1, 'iElem'),(1, 'pfVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetInt16Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(Int16))(('VariantGetInt16Elem', windll['PROPSYS.dll']), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetUInt16Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(UInt16))(('VariantGetUInt16Elem', windll['PROPSYS.dll']), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetInt32Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(Int32))(('VariantGetInt32Elem', windll['PROPSYS.dll']), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetUInt32Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(UInt32))(('VariantGetUInt32Elem', windll['PROPSYS.dll']), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetInt64Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(Int64))(('VariantGetInt64Elem', windll['PROPSYS.dll']), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetUInt64Elem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(UInt64))(('VariantGetUInt64Elem', windll['PROPSYS.dll']), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetDoubleElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(Double))(('VariantGetDoubleElem', windll['PROPSYS.dll']), ((1, 'var'),(1, 'iElem'),(1, 'pnVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantGetStringElem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(win32more.Foundation.PWSTR))(('VariantGetStringElem', windll['PROPSYS.dll']), ((1, 'var'),(1, 'iElem'),(1, 'ppszVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClearVariantArray():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Com.VARIANT_head),UInt32)(('ClearVariantArray', windll['PROPSYS.dll']), ((1, 'pvars'),(1, 'cvars'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantCompare():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head))(('VariantCompare', windll['PROPSYS.dll']), ((1, 'var1'),(1, 'var2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHGetPropertyStoreFromIDList():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.Common.ITEMIDLIST_head),win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,POINTER(Guid),POINTER(c_void_p))(('SHGetPropertyStoreFromIDList', windll['SHELL32.dll']), ((1, 'pidl'),(1, 'flags'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHGetPropertyStoreFromParsingName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IBindCtx_head,win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,POINTER(Guid),POINTER(c_void_p))(('SHGetPropertyStoreFromParsingName', windll['SHELL32.dll']), ((1, 'pszPath'),(1, 'pbc'),(1, 'flags'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHAddDefaultPropertiesByExt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)(('SHAddDefaultPropertiesByExt', windll['SHELL32.dll']), ((1, 'pszExt'),(1, 'pPropStore'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PifMgr_OpenProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32)(('PifMgr_OpenProperties', windll['SHELL32.dll']), ((1, 'pszApp'),(1, 'pszPIF'),(1, 'hInf'),(1, 'flOpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PifMgr_GetProperties():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,c_void_p,Int32,UInt32)(('PifMgr_GetProperties', windll['SHELL32.dll']), ((1, 'hProps'),(1, 'pszGroup'),(1, 'lpProps'),(1, 'cbProps'),(1, 'flOpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PifMgr_SetProperties():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,c_void_p,Int32,UInt32)(('PifMgr_SetProperties', windll['SHELL32.dll']), ((1, 'hProps'),(1, 'pszGroup'),(1, 'lpProps'),(1, 'cbProps'),(1, 'flOpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PifMgr_CloseProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32)(('PifMgr_CloseProperties', windll['SHELL32.dll']), ((1, 'hProps'),(1, 'flOpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHPropStgCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertySetStorage_head,POINTER(Guid),POINTER(Guid),UInt32,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head),POINTER(UInt32))(('SHPropStgCreate', windll['SHELL32.dll']), ((1, 'psstg'),(1, 'fmtid'),(1, 'pclsid'),(1, 'grfFlags'),(1, 'grfMode'),(1, 'dwDisposition'),(1, 'ppstg'),(1, 'puCodePage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHPropStgReadMultiple():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyStorage_head,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPSPEC_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('SHPropStgReadMultiple', windll['SHELL32.dll']), ((1, 'pps'),(1, 'uCodePage'),(1, 'cpspec'),(1, 'rgpspec'),(1, 'rgvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHPropStgWriteMultiple():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyStorage_head,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPSPEC_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt32)(('SHPropStgWriteMultiple', windll['SHELL32.dll']), ((1, 'pps'),(1, 'puCodePage'),(1, 'cpspec'),(1, 'rgpspec'),(1, 'rgvar'),(1, 'propidNameFirst'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SHGetPropertyStoreForWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(('SHGetPropertyStoreForWindow', windll['SHELL32.dll']), ((1, 'hwnd'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
DRAWPROGRESSFLAGS = UInt32
DPF_NONE = 0
DPF_MARQUEE = 1
DPF_MARQUEE_COMPLETE = 2
DPF_ERROR = 4
DPF_WARNING = 8
DPF_STOPPED = 16
GETPROPERTYSTOREFLAGS = UInt32
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
def _define_ICreateObject_head():
    class ICreateObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('75121952-e0d0-43e5-93-80-1d-80-48-3a-cf-72')
    return ICreateObject
def _define_ICreateObject():
    ICreateObject = win32more.UI.Shell.PropertiesSystem.ICreateObject_head
    ICreateObject.CreateObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(3, 'CreateObject', ((1, 'clsid'),(1, 'pUnkOuter'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return ICreateObject
def _define_IDelayedPropertyStoreFactory_head():
    class IDelayedPropertyStoreFactory(win32more.UI.Shell.PropertiesSystem.IPropertyStoreFactory_head):
        Guid = Guid('40d4577f-e237-4bdb-bd-69-58-f0-89-43-1b-6a')
    return IDelayedPropertyStoreFactory
def _define_IDelayedPropertyStoreFactory():
    IDelayedPropertyStoreFactory = win32more.UI.Shell.PropertiesSystem.IDelayedPropertyStoreFactory_head
    IDelayedPropertyStoreFactory.GetDelayedPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,UInt32,POINTER(Guid),POINTER(c_void_p))(5, 'GetDelayedPropertyStore', ((1, 'flags'),(1, 'dwStoreId'),(1, 'riid'),(1, 'ppv'),)))
    win32more.UI.Shell.PropertiesSystem.IPropertyStoreFactory
    return IDelayedPropertyStoreFactory
def _define_IInitializeWithFile_head():
    class IInitializeWithFile(win32more.System.Com.IUnknown_head):
        Guid = Guid('b7d14566-0509-4cce-a7-1f-0a-55-42-33-bd-9b')
    return IInitializeWithFile
def _define_IInitializeWithFile():
    IInitializeWithFile = win32more.UI.Shell.PropertiesSystem.IInitializeWithFile_head
    IInitializeWithFile.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(3, 'Initialize', ((1, 'pszFilePath'),(1, 'grfMode'),)))
    win32more.System.Com.IUnknown
    return IInitializeWithFile
def _define_IInitializeWithStream_head():
    class IInitializeWithStream(win32more.System.Com.IUnknown_head):
        Guid = Guid('b824b49d-22ac-4161-ac-8a-99-16-e8-fa-3f-7f')
    return IInitializeWithStream
def _define_IInitializeWithStream():
    IInitializeWithStream = win32more.UI.Shell.PropertiesSystem.IInitializeWithStream_head
    IInitializeWithStream.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,UInt32)(3, 'Initialize', ((1, 'pstream'),(1, 'grfMode'),)))
    win32more.System.Com.IUnknown
    return IInitializeWithStream
def _define_INamedPropertyStore_head():
    class INamedPropertyStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('71604b0f-97b0-4764-85-77-2f-13-e9-8a-14-22')
    return INamedPropertyStore
def _define_INamedPropertyStore():
    INamedPropertyStore = win32more.UI.Shell.PropertiesSystem.INamedPropertyStore_head
    INamedPropertyStore.GetNamedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(3, 'GetNamedValue', ((1, 'pszName'),(1, 'ppropvar'),)))
    INamedPropertyStore.SetNamedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(4, 'SetNamedValue', ((1, 'pszName'),(1, 'propvar'),)))
    INamedPropertyStore.GetNameCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetNameCount', ((1, 'pdwCount'),)))
    INamedPropertyStore.GetNameAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR))(6, 'GetNameAt', ((1, 'iProp'),(1, 'pbstrName'),)))
    win32more.System.Com.IUnknown
    return INamedPropertyStore
InMemoryPropertyStore = Guid('9a02e012-6303-4e1e-b9-a1-63-0f-80-25-92-c5')
InMemoryPropertyStoreMarshalByValue = Guid('d4ca0e2d-6da7-4b75-a9-7c-5f-30-6f-0e-ae-dc')
def _define_IObjectWithPropertyKey_head():
    class IObjectWithPropertyKey(win32more.System.Com.IUnknown_head):
        Guid = Guid('fc0ca0a7-c316-4fd2-90-31-3e-62-8e-6d-4f-23')
    return IObjectWithPropertyKey
def _define_IObjectWithPropertyKey():
    IObjectWithPropertyKey = win32more.UI.Shell.PropertiesSystem.IObjectWithPropertyKey_head
    IObjectWithPropertyKey.SetPropertyKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(3, 'SetPropertyKey', ((1, 'key'),)))
    IObjectWithPropertyKey.GetPropertyKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(4, 'GetPropertyKey', ((1, 'pkey'),)))
    win32more.System.Com.IUnknown
    return IObjectWithPropertyKey
def _define_IPersistSerializedPropStorage_head():
    class IPersistSerializedPropStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('e318ad57-0aa0-450f-ac-a5-6f-ab-71-03-d9-17')
    return IPersistSerializedPropStorage
def _define_IPersistSerializedPropStorage():
    IPersistSerializedPropStorage = win32more.UI.Shell.PropertiesSystem.IPersistSerializedPropStorage_head
    IPersistSerializedPropStorage.SetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(3, 'SetFlags', ((1, 'flags'),)))
    IPersistSerializedPropStorage.SetPropertyStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head),UInt32)(4, 'SetPropertyStorage', ((1, 'psps'),(1, 'cb'),)))
    IPersistSerializedPropStorage.GetPropertyStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head)),POINTER(UInt32))(5, 'GetPropertyStorage', ((1, 'ppsps'),(1, 'pcb'),)))
    win32more.System.Com.IUnknown
    return IPersistSerializedPropStorage
def _define_IPersistSerializedPropStorage2_head():
    class IPersistSerializedPropStorage2(win32more.UI.Shell.PropertiesSystem.IPersistSerializedPropStorage_head):
        Guid = Guid('77effa68-4f98-4366-ba-72-57-3b-3d-88-05-71')
    return IPersistSerializedPropStorage2
def _define_IPersistSerializedPropStorage2():
    IPersistSerializedPropStorage2 = win32more.UI.Shell.PropertiesSystem.IPersistSerializedPropStorage2_head
    IPersistSerializedPropStorage2.GetPropertyStorageSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'GetPropertyStorageSize', ((1, 'pcb'),)))
    IPersistSerializedPropStorage2.GetPropertyStorageBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head),UInt32,POINTER(UInt32))(7, 'GetPropertyStorageBuffer', ((1, 'psps'),(1, 'cb'),(1, 'pcbWritten'),)))
    win32more.UI.Shell.PropertiesSystem.IPersistSerializedPropStorage
    return IPersistSerializedPropStorage2
def _define_IPropertyChange_head():
    class IPropertyChange(win32more.UI.Shell.PropertiesSystem.IObjectWithPropertyKey_head):
        Guid = Guid('f917bc8a-1bba-4478-a2-45-1b-de-03-eb-94-31')
    return IPropertyChange
def _define_IPropertyChange():
    IPropertyChange = win32more.UI.Shell.PropertiesSystem.IPropertyChange_head
    IPropertyChange.ApplyToPropVariant = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(5, 'ApplyToPropVariant', ((1, 'propvarIn'),(1, 'ppropvarOut'),)))
    win32more.UI.Shell.PropertiesSystem.IObjectWithPropertyKey
    return IPropertyChange
def _define_IPropertyChangeArray_head():
    class IPropertyChangeArray(win32more.System.Com.IUnknown_head):
        Guid = Guid('380f5cad-1b5e-42f2-80-5d-63-7f-d3-92-d3-1e')
    return IPropertyChangeArray
def _define_IPropertyChangeArray():
    IPropertyChangeArray = win32more.UI.Shell.PropertiesSystem.IPropertyChangeArray_head
    IPropertyChangeArray.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pcOperations'),)))
    IPropertyChangeArray.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p))(4, 'GetAt', ((1, 'iIndex'),(1, 'riid'),(1, 'ppv'),)))
    IPropertyChangeArray.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Shell.PropertiesSystem.IPropertyChange_head)(5, 'InsertAt', ((1, 'iIndex'),(1, 'ppropChange'),)))
    IPropertyChangeArray.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyChange_head)(6, 'Append', ((1, 'ppropChange'),)))
    IPropertyChangeArray.AppendOrReplace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyChange_head)(7, 'AppendOrReplace', ((1, 'ppropChange'),)))
    IPropertyChangeArray.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(8, 'RemoveAt', ((1, 'iIndex'),)))
    IPropertyChangeArray.IsKeyInArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(9, 'IsKeyInArray', ((1, 'key'),)))
    win32more.System.Com.IUnknown
    return IPropertyChangeArray
def _define_IPropertyDescription_head():
    class IPropertyDescription(win32more.System.Com.IUnknown_head):
        Guid = Guid('6f79d558-3e96-4549-a1-d1-7d-75-d2-28-88-14')
    return IPropertyDescription
def _define_IPropertyDescription():
    IPropertyDescription = win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head
    IPropertyDescription.GetPropertyKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(3, 'GetPropertyKey', ((1, 'pkey'),)))
    IPropertyDescription.GetCanonicalName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(4, 'GetCanonicalName', ((1, 'ppszName'),)))
    IPropertyDescription.GetPropertyType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16))(5, 'GetPropertyType', ((1, 'pvartype'),)))
    IPropertyDescription.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(6, 'GetDisplayName', ((1, 'ppszName'),)))
    IPropertyDescription.GetEditInvitation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'GetEditInvitation', ((1, 'ppszInvite'),)))
    IPropertyDescription.GetTypeFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_TYPE_FLAGS))(8, 'GetTypeFlags', ((1, 'mask'),(1, 'ppdtFlags'),)))
    IPropertyDescription.GetViewFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_VIEW_FLAGS))(9, 'GetViewFlags', ((1, 'ppdvFlags'),)))
    IPropertyDescription.GetDefaultColumnWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(10, 'GetDefaultColumnWidth', ((1, 'pcxChars'),)))
    IPropertyDescription.GetDisplayType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_DISPLAYTYPE))(11, 'GetDisplayType', ((1, 'pdisplaytype'),)))
    IPropertyDescription.GetColumnState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'GetColumnState', ((1, 'pcsFlags'),)))
    IPropertyDescription.GetGroupingRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_GROUPING_RANGE))(13, 'GetGroupingRange', ((1, 'pgr'),)))
    IPropertyDescription.GetRelativeDescriptionType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_RELATIVEDESCRIPTION_TYPE))(14, 'GetRelativeDescriptionType', ((1, 'prdt'),)))
    IPropertyDescription.GetRelativeDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(15, 'GetRelativeDescription', ((1, 'propvar1'),(1, 'propvar2'),(1, 'ppszDesc1'),(1, 'ppszDesc2'),)))
    IPropertyDescription.GetSortDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_SORTDESCRIPTION))(16, 'GetSortDescription', ((1, 'psd'),)))
    IPropertyDescription.GetSortDescriptionLabel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.Foundation.PWSTR))(17, 'GetSortDescriptionLabel', ((1, 'fDescending'),(1, 'ppszDescription'),)))
    IPropertyDescription.GetAggregationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_AGGREGATION_TYPE))(18, 'GetAggregationType', ((1, 'paggtype'),)))
    IPropertyDescription.GetConditionType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_CONDITION_TYPE),POINTER(win32more.System.Search.Common.CONDITION_OPERATION))(19, 'GetConditionType', ((1, 'pcontype'),(1, 'popDefault'),)))
    IPropertyDescription.GetEnumTypeList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(20, 'GetEnumTypeList', ((1, 'riid'),(1, 'ppv'),)))
    IPropertyDescription.CoerceToCanonicalValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(21, 'CoerceToCanonicalValue', ((1, 'ppropvar'),)))
    IPropertyDescription.FormatForDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,POINTER(win32more.Foundation.PWSTR))(22, 'FormatForDisplay', ((1, 'propvar'),(1, 'pdfFlags'),(1, 'ppszDisplay'),)))
    IPropertyDescription.IsValueCanonical = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(23, 'IsValueCanonical', ((1, 'propvar'),)))
    win32more.System.Com.IUnknown
    return IPropertyDescription
def _define_IPropertyDescription2_head():
    class IPropertyDescription2(win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head):
        Guid = Guid('57d2eded-5062-400e-b1-07-5d-ae-79-fe-57-a6')
    return IPropertyDescription2
def _define_IPropertyDescription2():
    IPropertyDescription2 = win32more.UI.Shell.PropertiesSystem.IPropertyDescription2_head
    IPropertyDescription2.GetImageReferenceForValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.Foundation.PWSTR))(24, 'GetImageReferenceForValue', ((1, 'propvar'),(1, 'ppszImageRes'),)))
    win32more.UI.Shell.PropertiesSystem.IPropertyDescription
    return IPropertyDescription2
def _define_IPropertyDescriptionAliasInfo_head():
    class IPropertyDescriptionAliasInfo(win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head):
        Guid = Guid('f67104fc-2af9-46fd-b3-2d-24-3c-14-04-f3-d1')
    return IPropertyDescriptionAliasInfo
def _define_IPropertyDescriptionAliasInfo():
    IPropertyDescriptionAliasInfo = win32more.UI.Shell.PropertiesSystem.IPropertyDescriptionAliasInfo_head
    IPropertyDescriptionAliasInfo.GetSortByAlias = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(24, 'GetSortByAlias', ((1, 'riid'),(1, 'ppv'),)))
    IPropertyDescriptionAliasInfo.GetAdditionalSortByAliases = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(25, 'GetAdditionalSortByAliases', ((1, 'riid'),(1, 'ppv'),)))
    win32more.UI.Shell.PropertiesSystem.IPropertyDescription
    return IPropertyDescriptionAliasInfo
def _define_IPropertyDescriptionList_head():
    class IPropertyDescriptionList(win32more.System.Com.IUnknown_head):
        Guid = Guid('1f9fc1d0-c39b-4b26-81-7f-01-19-67-d3-44-0e')
    return IPropertyDescriptionList
def _define_IPropertyDescriptionList():
    IPropertyDescriptionList = win32more.UI.Shell.PropertiesSystem.IPropertyDescriptionList_head
    IPropertyDescriptionList.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pcElem'),)))
    IPropertyDescriptionList.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p))(4, 'GetAt', ((1, 'iElem'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IPropertyDescriptionList
def _define_IPropertyDescriptionRelatedPropertyInfo_head():
    class IPropertyDescriptionRelatedPropertyInfo(win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head):
        Guid = Guid('507393f4-2a3d-4a60-b5-9e-d9-c7-57-16-c2-dd')
    return IPropertyDescriptionRelatedPropertyInfo
def _define_IPropertyDescriptionRelatedPropertyInfo():
    IPropertyDescriptionRelatedPropertyInfo = win32more.UI.Shell.PropertiesSystem.IPropertyDescriptionRelatedPropertyInfo_head
    IPropertyDescriptionRelatedPropertyInfo.GetRelatedProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p))(24, 'GetRelatedProperty', ((1, 'pszRelationshipName'),(1, 'riid'),(1, 'ppv'),)))
    win32more.UI.Shell.PropertiesSystem.IPropertyDescription
    return IPropertyDescriptionRelatedPropertyInfo
def _define_IPropertyDescriptionSearchInfo_head():
    class IPropertyDescriptionSearchInfo(win32more.UI.Shell.PropertiesSystem.IPropertyDescription_head):
        Guid = Guid('078f91bd-29a2-440f-92-4e-46-a2-91-52-45-20')
    return IPropertyDescriptionSearchInfo
def _define_IPropertyDescriptionSearchInfo():
    IPropertyDescriptionSearchInfo = win32more.UI.Shell.PropertiesSystem.IPropertyDescriptionSearchInfo_head
    IPropertyDescriptionSearchInfo.GetSearchInfoFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_SEARCHINFO_FLAGS))(24, 'GetSearchInfoFlags', ((1, 'ppdsiFlags'),)))
    IPropertyDescriptionSearchInfo.GetColumnIndexType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPDESC_COLUMNINDEX_TYPE))(25, 'GetColumnIndexType', ((1, 'ppdciType'),)))
    IPropertyDescriptionSearchInfo.GetProjectionString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(26, 'GetProjectionString', ((1, 'ppszProjection'),)))
    IPropertyDescriptionSearchInfo.GetMaxSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(27, 'GetMaxSize', ((1, 'pcbMaxSize'),)))
    win32more.UI.Shell.PropertiesSystem.IPropertyDescription
    return IPropertyDescriptionSearchInfo
def _define_IPropertyEnumType_head():
    class IPropertyEnumType(win32more.System.Com.IUnknown_head):
        Guid = Guid('11e1fbf9-2d56-4a6b-8d-b3-7c-d1-93-a4-71-f2')
    return IPropertyEnumType
def _define_IPropertyEnumType():
    IPropertyEnumType = win32more.UI.Shell.PropertiesSystem.IPropertyEnumType_head
    IPropertyEnumType.GetEnumType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPENUMTYPE))(3, 'GetEnumType', ((1, 'penumtype'),)))
    IPropertyEnumType.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(4, 'GetValue', ((1, 'ppropvar'),)))
    IPropertyEnumType.GetRangeMinValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(5, 'GetRangeMinValue', ((1, 'ppropvarMin'),)))
    IPropertyEnumType.GetRangeSetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(6, 'GetRangeSetValue', ((1, 'ppropvarSet'),)))
    IPropertyEnumType.GetDisplayText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'GetDisplayText', ((1, 'ppszDisplay'),)))
    win32more.System.Com.IUnknown
    return IPropertyEnumType
def _define_IPropertyEnumType2_head():
    class IPropertyEnumType2(win32more.UI.Shell.PropertiesSystem.IPropertyEnumType_head):
        Guid = Guid('9b6e051c-5ddd-4321-90-70-fe-2a-cb-55-e7-94')
    return IPropertyEnumType2
def _define_IPropertyEnumType2():
    IPropertyEnumType2 = win32more.UI.Shell.PropertiesSystem.IPropertyEnumType2_head
    IPropertyEnumType2.GetImageReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(8, 'GetImageReference', ((1, 'ppszImageRes'),)))
    win32more.UI.Shell.PropertiesSystem.IPropertyEnumType
    return IPropertyEnumType2
def _define_IPropertyEnumTypeList_head():
    class IPropertyEnumTypeList(win32more.System.Com.IUnknown_head):
        Guid = Guid('a99400f4-3d84-4557-94-ba-12-42-fb-2c-c9-a6')
    return IPropertyEnumTypeList
def _define_IPropertyEnumTypeList():
    IPropertyEnumTypeList = win32more.UI.Shell.PropertiesSystem.IPropertyEnumTypeList_head
    IPropertyEnumTypeList.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pctypes'),)))
    IPropertyEnumTypeList.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p))(4, 'GetAt', ((1, 'itype'),(1, 'riid'),(1, 'ppv'),)))
    IPropertyEnumTypeList.GetConditionAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p))(5, 'GetConditionAt', ((1, 'nIndex'),(1, 'riid'),(1, 'ppv'),)))
    IPropertyEnumTypeList.FindMatchingIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32))(6, 'FindMatchingIndex', ((1, 'propvarCmp'),(1, 'pnIndex'),)))
    win32more.System.Com.IUnknown
    return IPropertyEnumTypeList
def _define_IPropertyStore_head():
    class IPropertyStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('886d8eeb-8cf2-4446-8d-02-cd-ba-1d-bd-cf-99')
    return IPropertyStore
def _define_IPropertyStore():
    IPropertyStore = win32more.UI.Shell.PropertiesSystem.IPropertyStore_head
    IPropertyStore.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'cProps'),)))
    IPropertyStore.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(4, 'GetAt', ((1, 'iProp'),(1, 'pkey'),)))
    IPropertyStore.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(5, 'GetValue', ((1, 'key'),(1, 'pv'),)))
    IPropertyStore.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(6, 'SetValue', ((1, 'key'),(1, 'propvar'),)))
    IPropertyStore.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Commit', ()))
    win32more.System.Com.IUnknown
    return IPropertyStore
def _define_IPropertyStoreCache_head():
    class IPropertyStoreCache(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head):
        Guid = Guid('3017056d-9a91-4e90-93-7d-74-6c-72-ab-bf-4f')
    return IPropertyStoreCache
def _define_IPropertyStoreCache():
    IPropertyStoreCache = win32more.UI.Shell.PropertiesSystem.IPropertyStoreCache_head
    IPropertyStoreCache.GetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.UI.Shell.PropertiesSystem.PSC_STATE))(8, 'GetState', ((1, 'key'),(1, 'pstate'),)))
    IPropertyStoreCache.GetValueAndState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.UI.Shell.PropertiesSystem.PSC_STATE))(9, 'GetValueAndState', ((1, 'key'),(1, 'ppropvar'),(1, 'pstate'),)))
    IPropertyStoreCache.SetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.UI.Shell.PropertiesSystem.PSC_STATE)(10, 'SetState', ((1, 'key'),(1, 'state'),)))
    IPropertyStoreCache.SetValueAndState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PSC_STATE)(11, 'SetValueAndState', ((1, 'key'),(1, 'ppropvar'),(1, 'state'),)))
    win32more.UI.Shell.PropertiesSystem.IPropertyStore
    return IPropertyStoreCache
def _define_IPropertyStoreCapabilities_head():
    class IPropertyStoreCapabilities(win32more.System.Com.IUnknown_head):
        Guid = Guid('c8e2d566-186e-4d49-bf-41-69-09-ea-d5-6a-cc')
    return IPropertyStoreCapabilities
def _define_IPropertyStoreCapabilities():
    IPropertyStoreCapabilities = win32more.UI.Shell.PropertiesSystem.IPropertyStoreCapabilities_head
    IPropertyStoreCapabilities.IsPropertyWritable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(3, 'IsPropertyWritable', ((1, 'key'),)))
    win32more.System.Com.IUnknown
    return IPropertyStoreCapabilities
def _define_IPropertyStoreFactory_head():
    class IPropertyStoreFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('bc110b6d-57e8-4148-a9-c6-91-01-5a-b2-f3-a5')
    return IPropertyStoreFactory
def _define_IPropertyStoreFactory():
    IPropertyStoreFactory = win32more.UI.Shell.PropertiesSystem.IPropertyStoreFactory_head
    IPropertyStoreFactory.GetPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(3, 'GetPropertyStore', ((1, 'flags'),(1, 'pUnkFactory'),(1, 'riid'),(1, 'ppv'),)))
    IPropertyStoreFactory.GetPropertyStoreForKeys = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32,win32more.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS,POINTER(Guid),POINTER(c_void_p))(4, 'GetPropertyStoreForKeys', ((1, 'rgKeys'),(1, 'cKeys'),(1, 'flags'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IPropertyStoreFactory
def _define_IPropertySystem_head():
    class IPropertySystem(win32more.System.Com.IUnknown_head):
        Guid = Guid('ca724e8a-c3e6-442b-88-a4-6f-b0-db-80-35-a3')
    return IPropertySystem
def _define_IPropertySystem():
    IPropertySystem = win32more.UI.Shell.PropertiesSystem.IPropertySystem_head
    IPropertySystem.GetPropertyDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Guid),POINTER(c_void_p))(3, 'GetPropertyDescription', ((1, 'propkey'),(1, 'riid'),(1, 'ppv'),)))
    IPropertySystem.GetPropertyDescriptionByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p))(4, 'GetPropertyDescriptionByName', ((1, 'pszCanonicalName'),(1, 'riid'),(1, 'ppv'),)))
    IPropertySystem.GetPropertyDescriptionListFromString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p))(5, 'GetPropertyDescriptionListFromString', ((1, 'pszPropList'),(1, 'riid'),(1, 'ppv'),)))
    IPropertySystem.EnumeratePropertyDescriptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.PROPDESC_ENUMFILTER,POINTER(Guid),POINTER(c_void_p))(6, 'EnumeratePropertyDescriptions', ((1, 'filterOn'),(1, 'riid'),(1, 'ppv'),)))
    IPropertySystem.FormatForDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,win32more.Foundation.PWSTR,UInt32)(7, 'FormatForDisplay', ((1, 'key'),(1, 'propvar'),(1, 'pdff'),(1, 'pszText'),(1, 'cchText'),)))
    IPropertySystem.FormatForDisplayAlloc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPDESC_FORMAT_FLAGS,POINTER(win32more.Foundation.PWSTR))(8, 'FormatForDisplayAlloc', ((1, 'key'),(1, 'propvar'),(1, 'pdff'),(1, 'ppszDisplay'),)))
    IPropertySystem.RegisterPropertySchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(9, 'RegisterPropertySchema', ((1, 'pszPath'),)))
    IPropertySystem.UnregisterPropertySchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(10, 'UnregisterPropertySchema', ((1, 'pszPath'),)))
    IPropertySystem.RefreshPropertySchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'RefreshPropertySchema', ()))
    win32more.System.Com.IUnknown
    return IPropertySystem
def _define_IPropertySystemChangeNotify_head():
    class IPropertySystemChangeNotify(win32more.System.Com.IUnknown_head):
        Guid = Guid('fa955fd9-38be-4879-a6-ce-82-4c-f5-2d-60-9f')
    return IPropertySystemChangeNotify
def _define_IPropertySystemChangeNotify():
    IPropertySystemChangeNotify = win32more.UI.Shell.PropertiesSystem.IPropertySystemChangeNotify_head
    IPropertySystemChangeNotify.SchemaRefreshed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'SchemaRefreshed', ()))
    win32more.System.Com.IUnknown
    return IPropertySystemChangeNotify
def _define_IPropertyUI_head():
    class IPropertyUI(win32more.System.Com.IUnknown_head):
        Guid = Guid('757a7d9f-919a-4118-99-d7-db-b2-08-c8-cc-66')
    return IPropertyUI
def _define_IPropertyUI():
    IPropertyUI = win32more.UI.Shell.PropertiesSystem.IPropertyUI_head
    IPropertyUI.ParsePropertyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(UInt32),POINTER(UInt32))(3, 'ParsePropertyName', ((1, 'pszName'),(1, 'pfmtid'),(1, 'ppid'),(1, 'pchEaten'),)))
    IPropertyUI.GetCannonicalName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,win32more.Foundation.PWSTR,UInt32)(4, 'GetCannonicalName', ((1, 'fmtid'),(1, 'pid'),(1, 'pwszText'),(1, 'cchText'),)))
    IPropertyUI.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,win32more.UI.Shell.PropertiesSystem.PROPERTYUI_NAME_FLAGS,win32more.Foundation.PWSTR,UInt32)(5, 'GetDisplayName', ((1, 'fmtid'),(1, 'pid'),(1, 'flags'),(1, 'pwszText'),(1, 'cchText'),)))
    IPropertyUI.GetPropertyDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,win32more.Foundation.PWSTR,UInt32)(6, 'GetPropertyDescription', ((1, 'fmtid'),(1, 'pid'),(1, 'pwszText'),(1, 'cchText'),)))
    IPropertyUI.GetDefaultWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(UInt32))(7, 'GetDefaultWidth', ((1, 'fmtid'),(1, 'pid'),(1, 'pcxChars'),)))
    IPropertyUI.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYUI_FLAGS))(8, 'GetFlags', ((1, 'fmtid'),(1, 'pid'),(1, 'pflags'),)))
    IPropertyUI.FormatForDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Shell.PropertiesSystem.PROPERTYUI_FORMAT_FLAGS,win32more.Foundation.PWSTR,UInt32)(9, 'FormatForDisplay', ((1, 'fmtid'),(1, 'pid'),(1, 'ppropvar'),(1, 'puiff'),(1, 'pwszText'),(1, 'cchText'),)))
    IPropertyUI.GetHelpInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(10, 'GetHelpInfo', ((1, 'fmtid'),(1, 'pid'),(1, 'pwszHelpFile'),(1, 'cch'),(1, 'puHelpID'),)))
    win32more.System.Com.IUnknown
    return IPropertyUI
PDOPSTATUS = Int32
PDOPS_RUNNING = 1
PDOPS_PAUSED = 2
PDOPS_CANCELLED = 3
PDOPS_STOPPED = 4
PDOPS_ERRORS = 5
PKA_FLAGS = UInt32
PKA_SET = 0
PKA_APPEND = 1
PKA_DELETE = 2
PLACEHOLDER_STATES = UInt32
PS_NONE = 0
PS_MARKED_FOR_OFFLINE_AVAILABILITY = 1
PS_FULL_PRIMARY_STREAM_AVAILABLE = 2
PS_CREATE_FILE_ACCESSIBLE = 4
PS_CLOUDFILE_PLACEHOLDER = 8
PS_DEFAULT = 7
PS_ALL = 15
PROPDESC_AGGREGATION_TYPE = Int32
PDAT_DEFAULT = 0
PDAT_FIRST = 1
PDAT_SUM = 2
PDAT_AVERAGE = 3
PDAT_DATERANGE = 4
PDAT_UNION = 5
PDAT_MAX = 6
PDAT_MIN = 7
PROPDESC_COLUMNINDEX_TYPE = Int32
PDCIT_NONE = 0
PDCIT_ONDISK = 1
PDCIT_INMEMORY = 2
PDCIT_ONDEMAND = 3
PDCIT_ONDISKALL = 4
PDCIT_ONDISKVECTOR = 5
PROPDESC_CONDITION_TYPE = Int32
PDCOT_NONE = 0
PDCOT_STRING = 1
PDCOT_SIZE = 2
PDCOT_DATETIME = 3
PDCOT_BOOLEAN = 4
PDCOT_NUMBER = 5
PROPDESC_DISPLAYTYPE = Int32
PDDT_STRING = 0
PDDT_NUMBER = 1
PDDT_BOOLEAN = 2
PDDT_DATETIME = 3
PDDT_ENUMERATED = 4
PROPDESC_ENUMFILTER = Int32
PDEF_ALL = 0
PDEF_SYSTEM = 1
PDEF_NONSYSTEM = 2
PDEF_VIEWABLE = 3
PDEF_QUERYABLE = 4
PDEF_INFULLTEXTQUERY = 5
PDEF_COLUMN = 6
PROPDESC_FORMAT_FLAGS = UInt32
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
PROPDESC_GROUPING_RANGE = Int32
PDGR_DISCRETE = 0
PDGR_ALPHANUMERIC = 1
PDGR_SIZE = 2
PDGR_DYNAMIC = 3
PDGR_DATE = 4
PDGR_PERCENT = 5
PDGR_ENUMERATED = 6
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
PROPDESC_SEARCHINFO_FLAGS = UInt32
PDSIF_DEFAULT = 0
PDSIF_ININVERTEDINDEX = 1
PDSIF_ISCOLUMN = 2
PDSIF_ISCOLUMNSPARSE = 4
PDSIF_ALWAYSINCLUDE = 8
PDSIF_USEFORTYPEAHEAD = 16
PROPDESC_SORTDESCRIPTION = Int32
PDSD_GENERAL = 0
PDSD_A_Z = 1
PDSD_LOWEST_HIGHEST = 2
PDSD_SMALLEST_BIGGEST = 3
PDSD_OLDEST_NEWEST = 4
PROPDESC_TYPE_FLAGS = UInt32
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
PDTF_ISSYSTEMPROPERTY = 2147483648
PDTF_MASK_ALL = 2147491839
PROPDESC_VIEW_FLAGS = UInt32
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
PROPENUMTYPE = Int32
PET_DISCRETEVALUE = 0
PET_RANGEDVALUE = 1
PET_DEFAULTVALUE = 2
PET_ENDRANGE = 3
def _define_PROPERTYKEY_head():
    class PROPERTYKEY(Structure):
        pass
    return PROPERTYKEY
def _define_PROPERTYKEY():
    PROPERTYKEY = win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head
    PROPERTYKEY._fields_ = [
        ('fmtid', Guid),
        ('pid', UInt32),
    ]
    return PROPERTYKEY
PropertySystem = Guid('b8967f85-58ae-4f46-9f-b2-5d-79-04-79-8f-4b')
PROPERTYUI_FLAGS = UInt32
PUIF_DEFAULT = 0
PUIF_RIGHTALIGN = 1
PUIF_NOLABELININFOTIP = 2
PROPERTYUI_FORMAT_FLAGS = UInt32
PUIFFDF_DEFAULT = 0
PUIFFDF_RIGHTTOLEFT = 1
PUIFFDF_SHORTFORMAT = 2
PUIFFDF_NOTIME = 4
PUIFFDF_FRIENDLYDATE = 8
PROPERTYUI_NAME_FLAGS = UInt32
PUIFNF_DEFAULT = 0
PUIFNF_MNEMONIC = 1
def _define_PROPPRG_head():
    class PROPPRG(Structure):
        pass
    return PROPPRG
def _define_PROPPRG():
    PROPPRG = win32more.UI.Shell.PropertiesSystem.PROPPRG_head
    PROPPRG._pack_ = 1
    PROPPRG._fields_ = [
        ('flPrg', UInt16),
        ('flPrgInit', UInt16),
        ('achTitle', win32more.Foundation.CHAR * 30),
        ('achCmdLine', win32more.Foundation.CHAR * 128),
        ('achWorkDir', win32more.Foundation.CHAR * 64),
        ('wHotKey', UInt16),
        ('achIconFile', win32more.Foundation.CHAR * 80),
        ('wIconIndex', UInt16),
        ('dwEnhModeFlags', UInt32),
        ('dwRealModeFlags', UInt32),
        ('achOtherFile', win32more.Foundation.CHAR * 80),
        ('achPIFFile', win32more.Foundation.CHAR * 260),
    ]
    return PROPPRG
PROPVAR_CHANGE_FLAGS = UInt32
PVCHF_DEFAULT = 0
PVCHF_NOVALUEPROP = 1
PVCHF_ALPHABOOL = 2
PVCHF_NOUSEROVERRIDE = 4
PVCHF_LOCALBOOL = 8
PVCHF_NOHEXSTRING = 16
PROPVAR_COMPARE_FLAGS = UInt32
PVCF_DEFAULT = 0
PVCF_TREATEMPTYASGREATERTHAN = 1
PVCF_USESTRCMP = 2
PVCF_USESTRCMPC = 4
PVCF_USESTRCMPI = 8
PVCF_USESTRCMPIC = 16
PVCF_DIGITSASNUMBERS_CASESENSITIVE = 32
PROPVAR_COMPARE_UNIT = Int32
PVCU_DEFAULT = 0
PVCU_SECOND = 1
PVCU_MINUTE = 2
PVCU_HOUR = 3
PVCU_DAY = 4
PVCU_MONTH = 5
PVCU_YEAR = 6
PSC_STATE = Int32
PSC_NORMAL = 0
PSC_NOTINSOURCE = 1
PSC_DIRTY = 2
PSC_READONLY = 3
PSTIME_FLAGS = UInt32
PSTF_UTC = 0
PSTF_LOCAL = 1
def _define_SERIALIZEDPROPSTORAGE_head():
    class SERIALIZEDPROPSTORAGE(Structure):
        pass
    return SERIALIZEDPROPSTORAGE
def _define_SERIALIZEDPROPSTORAGE():
    SERIALIZEDPROPSTORAGE = win32more.UI.Shell.PropertiesSystem.SERIALIZEDPROPSTORAGE_head
    return SERIALIZEDPROPSTORAGE
SYNC_ENGINE_STATE_FLAGS = UInt32
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
SYNC_TRANSFER_STATUS = UInt32
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
