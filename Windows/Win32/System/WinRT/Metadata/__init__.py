from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT
import Windows.Win32.System.WinRT.Metadata
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ASSEMBLYMETADATA(EasyCastStructure):
    usMajorVersion: UInt16
    usMinorVersion: UInt16
    usBuildNumber: UInt16
    usRevisionNumber: UInt16
    szLocale: Windows.Win32.Foundation.PWSTR
    cbLocale: UInt32
    rProcessor: POINTER(UInt32)
    ulProcessor: UInt32
    rOS: POINTER(Windows.Win32.System.WinRT.Metadata.OSINFO_head)
    ulOS: UInt32
INVALID_CONNECTION_ID: UInt32 = 0
INVALID_TASK_ID: UInt32 = 0
MAX_CONNECTION_NAME: UInt32 = 260
MAIN_CLR_MODULE_NAME_W: String = 'coreclr'
MAIN_CLR_MODULE_NAME_A: String = 'coreclr'
MSCOREE_SHIM_W: String = 'mscoree.dll'
MSCOREE_SHIM_A: String = 'mscoree.dll'
COR_NATIVE_LINK_CUSTOM_VALUE: String = 'COMPLUS_NativeLink'
COR_NATIVE_LINK_CUSTOM_VALUE_ANSI: String = 'COMPLUS_NativeLink'
COR_NATIVE_LINK_CUSTOM_VALUE_CC: UInt32 = 18
COR_BASE_SECURITY_ATTRIBUTE_CLASS: String = 'System.Security.Permissions.SecurityAttribute'
COR_BASE_SECURITY_ATTRIBUTE_CLASS_ANSI: String = 'System.Security.Permissions.SecurityAttribute'
COR_SUPPRESS_UNMANAGED_CODE_CHECK_ATTRIBUTE: String = 'System.Security.SuppressUnmanagedCodeSecurityAttribute'
COR_SUPPRESS_UNMANAGED_CODE_CHECK_ATTRIBUTE_ANSI: String = 'System.Security.SuppressUnmanagedCodeSecurityAttribute'
COR_UNVER_CODE_ATTRIBUTE: String = 'System.Security.UnverifiableCodeAttribute'
COR_UNVER_CODE_ATTRIBUTE_ANSI: String = 'System.Security.UnverifiableCodeAttribute'
COR_REQUIRES_SECOBJ_ATTRIBUTE: String = 'System.Security.DynamicSecurityMethodAttribute'
COR_REQUIRES_SECOBJ_ATTRIBUTE_ANSI: String = 'System.Security.DynamicSecurityMethodAttribute'
COR_COMPILERSERVICE_DISCARDABLEATTRIBUTE: String = 'System.Runtime.CompilerServices.DiscardableAttribute'
COR_COMPILERSERVICE_DISCARDABLEATTRIBUTE_ASNI: String = 'System.Runtime.CompilerServices.DiscardableAttribute'
COR_E_UNAUTHORIZEDACCESS: Int32 = -2147024891
COR_E_ARGUMENT: Int32 = -2147024809
COR_E_INVALIDCAST: Int32 = -2147467262
COR_E_OUTOFMEMORY: Int32 = -2147024882
COR_E_NULLREFERENCE: Int32 = -2147467261
COR_E_AMBIGUOUSMATCH: Windows.Win32.Foundation.HRESULT = -2147475171
COR_E_TARGETPARAMCOUNT: Windows.Win32.Foundation.HRESULT = -2147352562
COR_E_DIVIDEBYZERO: Windows.Win32.Foundation.HRESULT = -2147352558
COR_E_BADIMAGEFORMAT: Windows.Win32.Foundation.HRESULT = -2147024885
FRAMEWORK_REGISTRY_KEY: String = 'Software\\Microsoft\\.NETFramework'
FRAMEWORK_REGISTRY_KEY_W: String = 'Software\\Microsoft\\.NETFramework'
USER_FRAMEWORK_REGISTRY_KEY: String = 'Software\\Microsoft\\.NETFramework64'
USER_FRAMEWORK_REGISTRY_KEY_W: String = 'Software\\Microsoft\\.NETFramework64'
COR_CTOR_METHOD_NAME: String = '.ctor'
COR_CTOR_METHOD_NAME_W: String = '.ctor'
COR_CCTOR_METHOD_NAME: String = '.cctor'
COR_CCTOR_METHOD_NAME_W: String = '.cctor'
COR_ENUM_FIELD_NAME: String = 'value__'
COR_ENUM_FIELD_NAME_W: String = 'value__'
COR_DELETED_NAME_A: String = '_Deleted'
COR_DELETED_NAME_W: String = '_Deleted'
COR_VTABLEGAP_NAME_A: String = '_VtblGap'
COR_VTABLEGAP_NAME_W: String = '_VtblGap'
INTEROP_DISPID_TYPE_W: String = 'System.Runtime.InteropServices.DispIdAttribute'
INTEROP_DISPID_TYPE: String = 'System.Runtime.InteropServices.DispIdAttribute'
INTEROP_INTERFACETYPE_TYPE_W: String = 'System.Runtime.InteropServices.InterfaceTypeAttribute'
INTEROP_INTERFACETYPE_TYPE: String = 'System.Runtime.InteropServices.InterfaceTypeAttribute'
INTEROP_CLASSINTERFACE_TYPE_W: String = 'System.Runtime.InteropServices.ClassInterfaceAttribute'
INTEROP_CLASSINTERFACE_TYPE: String = 'System.Runtime.InteropServices.ClassInterfaceAttribute'
INTEROP_COMVISIBLE_TYPE_W: String = 'System.Runtime.InteropServices.ComVisibleAttribute'
INTEROP_COMVISIBLE_TYPE: String = 'System.Runtime.InteropServices.ComVisibleAttribute'
INTEROP_COMREGISTERFUNCTION_TYPE_W: String = 'System.Runtime.InteropServices.ComRegisterFunctionAttribute'
INTEROP_COMREGISTERFUNCTION_TYPE: String = 'System.Runtime.InteropServices.ComRegisterFunctionAttribute'
INTEROP_COMUNREGISTERFUNCTION_TYPE_W: String = 'System.Runtime.InteropServices.ComUnregisterFunctionAttribute'
INTEROP_COMUNREGISTERFUNCTION_TYPE: String = 'System.Runtime.InteropServices.ComUnregisterFunctionAttribute'
INTEROP_IMPORTEDFROMTYPELIB_TYPE_W: String = 'System.Runtime.InteropServices.ImportedFromTypeLibAttribute'
INTEROP_IMPORTEDFROMTYPELIB_TYPE: String = 'System.Runtime.InteropServices.ImportedFromTypeLibAttribute'
INTEROP_PRIMARYINTEROPASSEMBLY_TYPE_W: String = 'System.Runtime.InteropServices.PrimaryInteropAssemblyAttribute'
INTEROP_PRIMARYINTEROPASSEMBLY_TYPE: String = 'System.Runtime.InteropServices.PrimaryInteropAssemblyAttribute'
INTEROP_IDISPATCHIMPL_TYPE_W: String = 'System.Runtime.InteropServices.IDispatchImplAttribute'
INTEROP_IDISPATCHIMPL_TYPE: String = 'System.Runtime.InteropServices.IDispatchImplAttribute'
INTEROP_COMSOURCEINTERFACES_TYPE_W: String = 'System.Runtime.InteropServices.ComSourceInterfacesAttribute'
INTEROP_COMSOURCEINTERFACES_TYPE: String = 'System.Runtime.InteropServices.ComSourceInterfacesAttribute'
INTEROP_COMDEFAULTINTERFACE_TYPE_W: String = 'System.Runtime.InteropServices.ComDefaultInterfaceAttribute'
INTEROP_COMDEFAULTINTERFACE_TYPE: String = 'System.Runtime.InteropServices.ComDefaultInterfaceAttribute'
INTEROP_COMCONVERSIONLOSS_TYPE_W: String = 'System.Runtime.InteropServices.ComConversionLossAttribute'
INTEROP_COMCONVERSIONLOSS_TYPE: String = 'System.Runtime.InteropServices.ComConversionLossAttribute'
INTEROP_BESTFITMAPPING_TYPE_W: String = 'System.Runtime.InteropServices.BestFitMappingAttribute'
INTEROP_BESTFITMAPPING_TYPE: String = 'System.Runtime.InteropServices.BestFitMappingAttribute'
INTEROP_TYPELIBTYPE_TYPE_W: String = 'System.Runtime.InteropServices.TypeLibTypeAttribute'
INTEROP_TYPELIBTYPE_TYPE: String = 'System.Runtime.InteropServices.TypeLibTypeAttribute'
INTEROP_TYPELIBFUNC_TYPE_W: String = 'System.Runtime.InteropServices.TypeLibFuncAttribute'
INTEROP_TYPELIBFUNC_TYPE: String = 'System.Runtime.InteropServices.TypeLibFuncAttribute'
INTEROP_TYPELIBVAR_TYPE_W: String = 'System.Runtime.InteropServices.TypeLibVarAttribute'
INTEROP_TYPELIBVAR_TYPE: String = 'System.Runtime.InteropServices.TypeLibVarAttribute'
INTEROP_MARSHALAS_TYPE_W: String = 'System.Runtime.InteropServices.MarshalAsAttribute'
INTEROP_MARSHALAS_TYPE: String = 'System.Runtime.InteropServices.MarshalAsAttribute'
INTEROP_COMIMPORT_TYPE_W: String = 'System.Runtime.InteropServices.ComImportAttribute'
INTEROP_COMIMPORT_TYPE: String = 'System.Runtime.InteropServices.ComImportAttribute'
INTEROP_GUID_TYPE_W: String = 'System.Runtime.InteropServices.GuidAttribute'
INTEROP_GUID_TYPE: String = 'System.Runtime.InteropServices.GuidAttribute'
INTEROP_DEFAULTMEMBER_TYPE_W: String = 'System.Reflection.DefaultMemberAttribute'
INTEROP_DEFAULTMEMBER_TYPE: String = 'System.Reflection.DefaultMemberAttribute'
INTEROP_COMEMULATE_TYPE_W: String = 'System.Runtime.InteropServices.ComEmulateAttribute'
INTEROP_COMEMULATE_TYPE: String = 'System.Runtime.InteropServices.ComEmulateAttribute'
INTEROP_PRESERVESIG_TYPE_W: String = 'System.Runtime.InteropServices.PreserveSigAttribure'
INTEROP_PRESERVESIG_TYPE: String = 'System.Runtime.InteropServices.PreserveSigAttribure'
INTEROP_IN_TYPE_W: String = 'System.Runtime.InteropServices.InAttribute'
INTEROP_IN_TYPE: String = 'System.Runtime.InteropServices.InAttribute'
INTEROP_OUT_TYPE_W: String = 'System.Runtime.InteropServices.OutAttribute'
INTEROP_OUT_TYPE: String = 'System.Runtime.InteropServices.OutAttribute'
INTEROP_COMALIASNAME_TYPE_W: String = 'System.Runtime.InteropServices.ComAliasNameAttribute'
INTEROP_COMALIASNAME_TYPE: String = 'System.Runtime.InteropServices.ComAliasNameAttribute'
INTEROP_PARAMARRAY_TYPE_W: String = 'System.ParamArrayAttribute'
INTEROP_PARAMARRAY_TYPE: String = 'System.ParamArrayAttribute'
INTEROP_LCIDCONVERSION_TYPE_W: String = 'System.Runtime.InteropServices.LCIDConversionAttribute'
INTEROP_LCIDCONVERSION_TYPE: String = 'System.Runtime.InteropServices.LCIDConversionAttribute'
INTEROP_COMSUBSTITUTABLEINTERFACE_TYPE_W: String = 'System.Runtime.InteropServices.ComSubstitutableInterfaceAttribute'
INTEROP_COMSUBSTITUTABLEINTERFACE_TYPE: String = 'System.Runtime.InteropServices.ComSubstitutableInterfaceAttribute'
INTEROP_DECIMALVALUE_TYPE_W: String = 'System.Runtime.CompilerServices.DecimalConstantAttribute'
INTEROP_DECIMALVALUE_TYPE: String = 'System.Runtime.CompilerServices.DecimalConstantAttribute'
INTEROP_DATETIMEVALUE_TYPE_W: String = 'System.Runtime.CompilerServices.DateTimeConstantAttribute'
INTEROP_DATETIMEVALUE_TYPE: String = 'System.Runtime.CompilerServices.DateTimeConstantAttribute'
INTEROP_IUNKNOWNVALUE_TYPE_W: String = 'System.Runtime.CompilerServices.IUnknownConstantAttribute'
INTEROP_IUNKNOWNVALUE_TYPE: String = 'System.Runtime.CompilerServices.IUnknownConstantAttribute'
INTEROP_IDISPATCHVALUE_TYPE_W: String = 'System.Runtime.CompilerServices.IDispatchConstantAttribute'
INTEROP_IDISPATCHVALUE_TYPE: String = 'System.Runtime.CompilerServices.IDispatchConstantAttribute'
INTEROP_AUTOPROXY_TYPE_W: String = 'System.Runtime.InteropServices.AutomationProxyAttribute'
INTEROP_AUTOPROXY_TYPE: String = 'System.Runtime.InteropServices.AutomationProxyAttribute'
INTEROP_TYPELIBIMPORTCLASS_TYPE_W: String = 'System.Runtime.InteropServices.TypeLibImportClassAttribute'
INTEROP_TYPELIBIMPORTCLASS_TYPE: String = 'System.Runtime.InteropServices.TypeLibImportClassAttribute'
INTEROP_TYPELIBVERSION_TYPE_W: String = 'System.Runtime.InteropServices.TypeLibVersionAttribute'
INTEROP_TYPELIBVERSION_TYPE: String = 'System.Runtime.InteropServices.TypeLibVersionAttribute'
INTEROP_COMCOMPATIBLEVERSION_TYPE_W: String = 'System.Runtime.InteropServices.ComCompatibleVersionAttribute'
INTEROP_COMCOMPATIBLEVERSION_TYPE: String = 'System.Runtime.InteropServices.ComCompatibleVersionAttribute'
INTEROP_COMEVENTINTERFACE_TYPE_W: String = 'System.Runtime.InteropServices.ComEventInterfaceAttribute'
INTEROP_COMEVENTINTERFACE_TYPE: String = 'System.Runtime.InteropServices.ComEventInterfaceAttribute'
INTEROP_COCLASS_TYPE_W: String = 'System.Runtime.InteropServices.CoClassAttribute'
INTEROP_COCLASS_TYPE: String = 'System.Runtime.InteropServices.CoClassAttribute'
INTEROP_SERIALIZABLE_TYPE_W: String = 'System.SerializableAttribute'
INTEROP_SERIALIZABLE_TYPE: String = 'System.SerializableAttribute'
INTEROP_SETWIN32CONTEXTINIDISPATCHATTRIBUTE_TYPE_W: String = 'System.Runtime.InteropServices.SetWin32ContextInIDispatchAttribute'
INTEROP_SETWIN32CONTEXTINIDISPATCHATTRIBUTE_TYPE: String = 'System.Runtime.InteropServices.SetWin32ContextInIDispatchAttribute'
FORWARD_INTEROP_STUB_METHOD_TYPE_W: String = 'System.Runtime.InteropServices.ManagedToNativeComInteropStubAttribute'
FORWARD_INTEROP_STUB_METHOD_TYPE: String = 'System.Runtime.InteropServices.ManagedToNativeComInteropStubAttribute'
FRIEND_ASSEMBLY_TYPE_W: String = 'System.Runtime.CompilerServices.InternalsVisibleToAttribute'
FRIEND_ASSEMBLY_TYPE: String = 'System.Runtime.CompilerServices.InternalsVisibleToAttribute'
FRIEND_ACCESS_ALLOWED_ATTRIBUTE_TYPE_W: String = 'System.Runtime.CompilerServices.FriendAccessAllowedAttribute'
FRIEND_ACCESS_ALLOWED_ATTRIBUTE_TYPE: String = 'System.Runtime.CompilerServices.FriendAccessAllowedAttribute'
SUBJECT_ASSEMBLY_TYPE_W: String = 'System.Runtime.CompilerServices.IgnoresAccessChecksToAttribute'
SUBJECT_ASSEMBLY_TYPE: String = 'System.Runtime.CompilerServices.IgnoresAccessChecksToAttribute'
DISABLED_PRIVATE_REFLECTION_TYPE_W: String = 'System.Runtime.CompilerServices.DisablePrivateReflectionAttribute'
DISABLED_PRIVATE_REFLECTION_TYPE: String = 'System.Runtime.CompilerServices.DisablePrivateReflectionAttribute'
DEFAULTDOMAIN_STA_TYPE_W: String = 'System.STAThreadAttribute'
DEFAULTDOMAIN_STA_TYPE: String = 'System.STAThreadAttribute'
DEFAULTDOMAIN_MTA_TYPE_W: String = 'System.MTAThreadAttribute'
DEFAULTDOMAIN_MTA_TYPE: String = 'System.MTAThreadAttribute'
DEFAULTDOMAIN_LOADEROPTIMIZATION_TYPE_W: String = 'System.LoaderOptimizationAttribute'
DEFAULTDOMAIN_LOADEROPTIMIZATION_TYPE: String = 'System.LoaderOptimizationAttribute'
NONVERSIONABLE_TYPE_W: String = 'System.Runtime.Versioning.NonVersionableAttribute'
NONVERSIONABLE_TYPE: String = 'System.Runtime.Versioning.NonVersionableAttribute'
COMPILATIONRELAXATIONS_TYPE_W: String = 'System.Runtime.CompilerServices.CompilationRelaxationsAttribute'
COMPILATIONRELAXATIONS_TYPE: String = 'System.Runtime.CompilerServices.CompilationRelaxationsAttribute'
RUNTIMECOMPATIBILITY_TYPE_W: String = 'System.Runtime.CompilerServices.RuntimeCompatibilityAttribute'
RUNTIMECOMPATIBILITY_TYPE: String = 'System.Runtime.CompilerServices.RuntimeCompatibilityAttribute'
DEFAULTDEPENDENCY_TYPE_W: String = 'System.Runtime.CompilerServices.DefaultDependencyAttribute'
DEFAULTDEPENDENCY_TYPE: String = 'System.Runtime.CompilerServices.DefaultDependencyAttribute'
DEPENDENCY_TYPE_W: String = 'System.Runtime.CompilerServices.DependencyAttribute'
DEPENDENCY_TYPE: String = 'System.Runtime.CompilerServices.DependencyAttribute'
TARGET_FRAMEWORK_TYPE_W: String = 'System.Runtime.Versioning.TargetFrameworkAttribute'
TARGET_FRAMEWORK_TYPE: String = 'System.Runtime.Versioning.TargetFrameworkAttribute'
ASSEMBLY_METADATA_TYPE_W: String = 'System.Reflection.AssemblyMetadataAttribute'
ASSEMBLY_METADATA_TYPE: String = 'System.Reflection.AssemblyMetadataAttribute'
CMOD_CALLCONV_NAMESPACE_OLD: String = 'System.Runtime.InteropServices'
CMOD_CALLCONV_NAMESPACE: String = 'System.Runtime.CompilerServices'
CMOD_CALLCONV_NAME_CDECL: String = 'CallConvCdecl'
CMOD_CALLCONV_NAME_STDCALL: String = 'CallConvStdcall'
CMOD_CALLCONV_NAME_THISCALL: String = 'CallConvThiscall'
CMOD_CALLCONV_NAME_FASTCALL: String = 'CallConvFastcall'
LIBID_ComPlusRuntime: Guid = Guid('bed7f4ea-1a96-11d2-8f-08-00-a0-c9-a6-18-6d')
GUID_ExportedFromComPlus: Guid = Guid('90883f05-3d28-11d2-8f-17-00-a0-c9-a6-18-6d')
GUID_ManagedName: Guid = Guid('0f21f359-ab84-41e8-9a-78-36-d1-10-e6-d2-f9')
GUID_Function2Getter: Guid = Guid('54fc8f55-38de-4703-9c-4e-25-03-51-30-2b-1c')
CLSID_CorMetaDataDispenserRuntime: Guid = Guid('1ec2de53-75cc-11d2-97-75-00-a0-c9-b4-d5-0c')
GUID_DispIdOverride: Guid = Guid('cd2bc5c9-f452-4326-b7-14-f9-c5-39-d4-da-58')
GUID_ForceIEnumerable: Guid = Guid('b64784eb-d8d4-4d9b-9a-cd-0e-30-80-64-26-f7')
GUID_PropGetCA: Guid = Guid('2941ff83-88d8-4f73-b6-a9-bd-f8-71-2d-00-0d')
GUID_PropPutCA: Guid = Guid('29533527-3683-4364-ab-c0-db-1a-dd-82-2f-a2')
CLSID_CLR_v1_MetaData: Guid = Guid('005023ca-72b1-11d3-9f-c4-00-c0-4f-79-a0-a3')
CLSID_CLR_v2_MetaData: Guid = Guid('efea471a-44fd-4862-92-92-0c-58-d4-6e-1f-3a')
MetaDataCheckDuplicatesFor: Guid = Guid('30fe7be8-d7d9-11d2-9f-80-00-c0-4f-79-a0-a3')
MetaDataRefToDefCheck: Guid = Guid('de3856f8-d7d9-11d2-9f-80-00-c0-4f-79-a0-a3')
MetaDataNotificationForTokenMovement: Guid = Guid('e5d71a4c-d7da-11d2-9f-80-00-c0-4f-79-a0-a3')
MetaDataSetUpdate: Guid = Guid('2eee315c-d7db-11d2-9f-80-00-c0-4f-79-a0-a3')
MetaDataImportOption: Guid = Guid('79700f36-4aac-11d3-84-c3-00-90-27-86-8c-b1')
MetaDataThreadSafetyOptions: Guid = Guid('f7559806-f266-42ea-8c-63-0a-db-45-e8-b2-34')
MetaDataErrorIfEmitOutOfOrder: Guid = Guid('1547872d-dc03-11d2-94-20-00-00-f8-08-34-60')
MetaDataGenerateTCEAdapters: Guid = Guid('dcc9de90-4151-11d3-88-d6-00-90-27-54-c4-3a')
MetaDataTypeLibImportNamespace: Guid = Guid('f17ff889-5a63-11d3-9f-f2-00-c0-4f-f7-43-1a')
MetaDataLinkerOptions: Guid = Guid('47e099b6-ae7c-4797-83-17-b4-8a-a6-45-b8-f9')
MetaDataRuntimeVersion: Guid = Guid('47e099b7-ae7c-4797-83-17-b4-8a-a6-45-b8-f9')
MetaDataMergerOptions: Guid = Guid('132d3a6e-b35d-464e-95-1a-42-ef-b9-fb-66-01')
MetaDataPreserveLocalRefs: Guid = Guid('a55c0354-e91b-468b-86-48-7c-c3-10-35-d5-33')
DESCR_GROUP_METHODDEF: Int32 = 0
DESCR_GROUP_METHODIMPL: Int32 = 1
CLSID_Cor: Guid = Guid('bee00010-ee77-11d0-a0-15-00-c0-4f-bb-b8-84')
CLSID_CorMetaDataDispenser: Guid = Guid('e5cb7a31-7512-11d2-89-ce-00-80-c7-92-e5-d8')
CLSID_CorMetaDataDispenserReg: Guid = Guid('435755ff-7397-11d2-97-71-00-a0-c9-b4-d5-0c')
CLSID_CorMetaDataReg: Guid = Guid('87f3a1f5-7397-11d2-97-71-00-a0-c9-b4-d5-0c')
SIGN_MASK_ONEBYTE: Int32 = -64
SIGN_MASK_TWOBYTE: Int32 = -8192
SIGN_MASK_FOURBYTE: Int32 = -268435456
@winfunctype('RoMetadata.dll')
def MetaDataGetDispenser(rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-0.dll')
def RoGetMetaDataFile(name: Windows.Win32.System.WinRT.HSTRING, metaDataDispenser: Windows.Win32.System.WinRT.Metadata.IMetaDataDispenserEx_head, metaDataFilePath: POINTER(Windows.Win32.System.WinRT.HSTRING), metaDataImport: POINTER(Windows.Win32.System.WinRT.Metadata.IMetaDataImport2_head), typeDefToken: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-0.dll')
def RoParseTypeName(typeName: Windows.Win32.System.WinRT.HSTRING, partsCount: POINTER(UInt32), typeNameParts: POINTER(POINTER(Windows.Win32.System.WinRT.HSTRING))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-0.dll')
def RoResolveNamespace(name: Windows.Win32.System.WinRT.HSTRING, windowsMetaDataDir: Windows.Win32.System.WinRT.HSTRING, packageGraphDirsCount: UInt32, packageGraphDirs: POINTER(Windows.Win32.System.WinRT.HSTRING), metaDataFilePathsCount: POINTER(UInt32), metaDataFilePaths: POINTER(POINTER(Windows.Win32.System.WinRT.HSTRING)), subNamespacesCount: POINTER(UInt32), subNamespaces: POINTER(POINTER(Windows.Win32.System.WinRT.HSTRING))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-1.dll')
def RoIsApiContractPresent(name: Windows.Win32.Foundation.PWSTR, majorVersion: UInt16, minorVersion: UInt16, present: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-1.dll')
def RoIsApiContractMajorVersionPresent(name: Windows.Win32.Foundation.PWSTR, majorVersion: UInt16, present: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-1.dll')
def RoCreateNonAgilePropertySet(ppPropertySet: POINTER(MissingType)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-1.dll')
def RoCreatePropertySetSerializer(ppPropertySetSerializer: POINTER(MissingType)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll')
def RoGetParameterizedTypeInstanceIID(nameElementCount: UInt32, nameElements: POINTER(Windows.Win32.Foundation.PWSTR), metaDataLocator: Windows.Win32.System.WinRT.Metadata.IRoMetaDataLocator_head, iid: POINTER(Guid), pExtra: POINTER(Windows.Win32.System.WinRT.ROPARAMIIDHANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll')
def RoFreeParameterizedTypeExtra(extra: Windows.Win32.System.WinRT.ROPARAMIIDHANDLE) -> Void: ...
@winfunctype('api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll')
def RoParameterizedTypeExtraGetTypeSignature(extra: Windows.Win32.System.WinRT.ROPARAMIIDHANDLE) -> Windows.Win32.Foundation.PSTR: ...
COINITICOR = Int32
COINITCOR_DEFAULT: COINITICOR = 0
COINITIEE = Int32
COINITEE_DEFAULT: COINITIEE = 0
COINITEE_DLL: COINITIEE = 1
COINITEE_MAIN: COINITIEE = 2
class COR_FIELD_OFFSET(EasyCastStructure):
    ridOfField: UInt32
    ulOffset: UInt32
class COR_NATIVE_LINK(EasyCastStructure):
    m_linkType: Byte
    m_flags: Byte
    m_entryPoint: UInt32
    _pack_ = 1
class COR_SECATTR(EasyCastStructure):
    tkCtor: UInt32
    pCustomAttribute: c_void_p
    cbCustomAttribute: UInt32
COUNINITIEE = Int32
COUNINITEE_DEFAULT: COUNINITIEE = 0
COUNINITEE_DLL: COUNINITIEE = 1
class CVStruct(EasyCastStructure):
    Major: Int16
    Minor: Int16
    Sub: Int16
    Build: Int16
CeeSectionAttr = Int64
CeeSectionAttr_sdNone: CeeSectionAttr = 0
CeeSectionAttr_sdReadOnly: CeeSectionAttr = 1073741888
CeeSectionAttr_sdReadWrite: CeeSectionAttr = 3221225536
CeeSectionAttr_sdExecute: CeeSectionAttr = 1610612768
class CeeSectionRelocExtra(EasyCastUnion):
    highAdj: UInt16
CeeSectionRelocType = Int32
CeeSectionRelocType_srRelocAbsolute: CeeSectionRelocType = 0
CeeSectionRelocType_srRelocHighLow: CeeSectionRelocType = 3
CeeSectionRelocType_srRelocHighAdj: CeeSectionRelocType = 4
CeeSectionRelocType_srRelocMapToken: CeeSectionRelocType = 5
CeeSectionRelocType_srRelocRelative: CeeSectionRelocType = 6
CeeSectionRelocType_srRelocFilePos: CeeSectionRelocType = 7
CeeSectionRelocType_srRelocCodeRelative: CeeSectionRelocType = 8
CeeSectionRelocType_srRelocIA64Imm64: CeeSectionRelocType = 9
CeeSectionRelocType_srRelocDir64: CeeSectionRelocType = 10
CeeSectionRelocType_srRelocIA64PcRel25: CeeSectionRelocType = 11
CeeSectionRelocType_srRelocIA64PcRel64: CeeSectionRelocType = 12
CeeSectionRelocType_srRelocAbsoluteTagged: CeeSectionRelocType = 13
CeeSectionRelocType_srRelocSentinel: CeeSectionRelocType = 14
CeeSectionRelocType_srNoBaseReloc: CeeSectionRelocType = 16384
CeeSectionRelocType_srRelocPtr: CeeSectionRelocType = 32768
CeeSectionRelocType_srRelocAbsolutePtr: CeeSectionRelocType = 32768
CeeSectionRelocType_srRelocHighLowPtr: CeeSectionRelocType = 32771
CeeSectionRelocType_srRelocRelativePtr: CeeSectionRelocType = 32774
CeeSectionRelocType_srRelocIA64Imm64Ptr: CeeSectionRelocType = 32777
CeeSectionRelocType_srRelocDir64Ptr: CeeSectionRelocType = 32778
CompilationRelaxationsEnum = Int32
CompilationRelaxations_NoStringInterning: CompilationRelaxationsEnum = 8
CorArgType = Int32
IMAGE_CEE_CS_END: CorArgType = 0
IMAGE_CEE_CS_VOID: CorArgType = 1
IMAGE_CEE_CS_I4: CorArgType = 2
IMAGE_CEE_CS_I8: CorArgType = 3
IMAGE_CEE_CS_R4: CorArgType = 4
IMAGE_CEE_CS_R8: CorArgType = 5
IMAGE_CEE_CS_PTR: CorArgType = 6
IMAGE_CEE_CS_OBJECT: CorArgType = 7
IMAGE_CEE_CS_STRUCT4: CorArgType = 8
IMAGE_CEE_CS_STRUCT32: CorArgType = 9
IMAGE_CEE_CS_BYVALUE: CorArgType = 10
CorAssemblyFlags = Int32
CorAssemblyFlags_afPublicKey: CorAssemblyFlags = 1
CorAssemblyFlags_afPA_None: CorAssemblyFlags = 0
CorAssemblyFlags_afPA_MSIL: CorAssemblyFlags = 16
CorAssemblyFlags_afPA_x86: CorAssemblyFlags = 32
CorAssemblyFlags_afPA_IA64: CorAssemblyFlags = 48
CorAssemblyFlags_afPA_AMD64: CorAssemblyFlags = 64
CorAssemblyFlags_afPA_ARM: CorAssemblyFlags = 80
CorAssemblyFlags_afPA_NoPlatform: CorAssemblyFlags = 112
CorAssemblyFlags_afPA_Specified: CorAssemblyFlags = 128
CorAssemblyFlags_afPA_Mask: CorAssemblyFlags = 112
CorAssemblyFlags_afPA_FullMask: CorAssemblyFlags = 240
CorAssemblyFlags_afPA_Shift: CorAssemblyFlags = 4
CorAssemblyFlags_afEnableJITcompileTracking: CorAssemblyFlags = 32768
CorAssemblyFlags_afDisableJITcompileOptimizer: CorAssemblyFlags = 16384
CorAssemblyFlags_afRetargetable: CorAssemblyFlags = 256
CorAssemblyFlags_afContentType_Default: CorAssemblyFlags = 0
CorAssemblyFlags_afContentType_WindowsRuntime: CorAssemblyFlags = 512
CorAssemblyFlags_afContentType_Mask: CorAssemblyFlags = 3584
CorAttributeTargets = Int32
CorAttributeTargets_catAssembly: CorAttributeTargets = 1
CorAttributeTargets_catModule: CorAttributeTargets = 2
CorAttributeTargets_catClass: CorAttributeTargets = 4
CorAttributeTargets_catStruct: CorAttributeTargets = 8
CorAttributeTargets_catEnum: CorAttributeTargets = 16
CorAttributeTargets_catConstructor: CorAttributeTargets = 32
CorAttributeTargets_catMethod: CorAttributeTargets = 64
CorAttributeTargets_catProperty: CorAttributeTargets = 128
CorAttributeTargets_catField: CorAttributeTargets = 256
CorAttributeTargets_catEvent: CorAttributeTargets = 512
CorAttributeTargets_catInterface: CorAttributeTargets = 1024
CorAttributeTargets_catParameter: CorAttributeTargets = 2048
CorAttributeTargets_catDelegate: CorAttributeTargets = 4096
CorAttributeTargets_catGenericParameter: CorAttributeTargets = 16384
CorAttributeTargets_catAll: CorAttributeTargets = 24575
CorAttributeTargets_catClassMembers: CorAttributeTargets = 6140
CorCallingConvention = Int32
IMAGE_CEE_CS_CALLCONV_DEFAULT: CorCallingConvention = 0
IMAGE_CEE_CS_CALLCONV_VARARG: CorCallingConvention = 5
IMAGE_CEE_CS_CALLCONV_FIELD: CorCallingConvention = 6
IMAGE_CEE_CS_CALLCONV_LOCAL_SIG: CorCallingConvention = 7
IMAGE_CEE_CS_CALLCONV_PROPERTY: CorCallingConvention = 8
IMAGE_CEE_CS_CALLCONV_UNMGD: CorCallingConvention = 9
IMAGE_CEE_CS_CALLCONV_GENERICINST: CorCallingConvention = 10
IMAGE_CEE_CS_CALLCONV_NATIVEVARARG: CorCallingConvention = 11
IMAGE_CEE_CS_CALLCONV_MAX: CorCallingConvention = 12
IMAGE_CEE_CS_CALLCONV_MASK: CorCallingConvention = 15
IMAGE_CEE_CS_CALLCONV_HASTHIS: CorCallingConvention = 32
IMAGE_CEE_CS_CALLCONV_EXPLICITTHIS: CorCallingConvention = 64
IMAGE_CEE_CS_CALLCONV_GENERIC: CorCallingConvention = 16
CorCheckDuplicatesFor = Int32
CorCheckDuplicatesFor_MDDupAll: CorCheckDuplicatesFor = -1
CorCheckDuplicatesFor_MDDupENC: CorCheckDuplicatesFor = -1
CorCheckDuplicatesFor_MDNoDupChecks: CorCheckDuplicatesFor = 0
CorCheckDuplicatesFor_MDDupTypeDef: CorCheckDuplicatesFor = 1
CorCheckDuplicatesFor_MDDupInterfaceImpl: CorCheckDuplicatesFor = 2
CorCheckDuplicatesFor_MDDupMethodDef: CorCheckDuplicatesFor = 4
CorCheckDuplicatesFor_MDDupTypeRef: CorCheckDuplicatesFor = 8
CorCheckDuplicatesFor_MDDupMemberRef: CorCheckDuplicatesFor = 16
CorCheckDuplicatesFor_MDDupCustomAttribute: CorCheckDuplicatesFor = 32
CorCheckDuplicatesFor_MDDupParamDef: CorCheckDuplicatesFor = 64
CorCheckDuplicatesFor_MDDupPermission: CorCheckDuplicatesFor = 128
CorCheckDuplicatesFor_MDDupProperty: CorCheckDuplicatesFor = 256
CorCheckDuplicatesFor_MDDupEvent: CorCheckDuplicatesFor = 512
CorCheckDuplicatesFor_MDDupFieldDef: CorCheckDuplicatesFor = 1024
CorCheckDuplicatesFor_MDDupSignature: CorCheckDuplicatesFor = 2048
CorCheckDuplicatesFor_MDDupModuleRef: CorCheckDuplicatesFor = 4096
CorCheckDuplicatesFor_MDDupTypeSpec: CorCheckDuplicatesFor = 8192
CorCheckDuplicatesFor_MDDupImplMap: CorCheckDuplicatesFor = 16384
CorCheckDuplicatesFor_MDDupAssemblyRef: CorCheckDuplicatesFor = 32768
CorCheckDuplicatesFor_MDDupFile: CorCheckDuplicatesFor = 65536
CorCheckDuplicatesFor_MDDupExportedType: CorCheckDuplicatesFor = 131072
CorCheckDuplicatesFor_MDDupManifestResource: CorCheckDuplicatesFor = 262144
CorCheckDuplicatesFor_MDDupGenericParam: CorCheckDuplicatesFor = 524288
CorCheckDuplicatesFor_MDDupMethodSpec: CorCheckDuplicatesFor = 1048576
CorCheckDuplicatesFor_MDDupGenericParamConstraint: CorCheckDuplicatesFor = 2097152
CorCheckDuplicatesFor_MDDupAssembly: CorCheckDuplicatesFor = 268435456
CorCheckDuplicatesFor_MDDupDefault: CorCheckDuplicatesFor = 1058840
CorDeclSecurity = Int32
CorDeclSecurity_dclActionMask: CorDeclSecurity = 31
CorDeclSecurity_dclActionNil: CorDeclSecurity = 0
CorDeclSecurity_dclRequest: CorDeclSecurity = 1
CorDeclSecurity_dclDemand: CorDeclSecurity = 2
CorDeclSecurity_dclAssert: CorDeclSecurity = 3
CorDeclSecurity_dclDeny: CorDeclSecurity = 4
CorDeclSecurity_dclPermitOnly: CorDeclSecurity = 5
CorDeclSecurity_dclLinktimeCheck: CorDeclSecurity = 6
CorDeclSecurity_dclInheritanceCheck: CorDeclSecurity = 7
CorDeclSecurity_dclRequestMinimum: CorDeclSecurity = 8
CorDeclSecurity_dclRequestOptional: CorDeclSecurity = 9
CorDeclSecurity_dclRequestRefuse: CorDeclSecurity = 10
CorDeclSecurity_dclPrejitGrant: CorDeclSecurity = 11
CorDeclSecurity_dclPrejitDenied: CorDeclSecurity = 12
CorDeclSecurity_dclNonCasDemand: CorDeclSecurity = 13
CorDeclSecurity_dclNonCasLinkDemand: CorDeclSecurity = 14
CorDeclSecurity_dclNonCasInheritance: CorDeclSecurity = 15
CorDeclSecurity_dclMaximumValue: CorDeclSecurity = 15
CorElementType = Int32
ELEMENT_TYPE_END: CorElementType = 0
ELEMENT_TYPE_VOID: CorElementType = 1
ELEMENT_TYPE_BOOLEAN: CorElementType = 2
ELEMENT_TYPE_CHAR: CorElementType = 3
ELEMENT_TYPE_I1: CorElementType = 4
ELEMENT_TYPE_U1: CorElementType = 5
ELEMENT_TYPE_I2: CorElementType = 6
ELEMENT_TYPE_U2: CorElementType = 7
ELEMENT_TYPE_I4: CorElementType = 8
ELEMENT_TYPE_U4: CorElementType = 9
ELEMENT_TYPE_I8: CorElementType = 10
ELEMENT_TYPE_U8: CorElementType = 11
ELEMENT_TYPE_R4: CorElementType = 12
ELEMENT_TYPE_R8: CorElementType = 13
ELEMENT_TYPE_STRING: CorElementType = 14
ELEMENT_TYPE_PTR: CorElementType = 15
ELEMENT_TYPE_BYREF: CorElementType = 16
ELEMENT_TYPE_VALUETYPE: CorElementType = 17
ELEMENT_TYPE_CLASS: CorElementType = 18
ELEMENT_TYPE_VAR: CorElementType = 19
ELEMENT_TYPE_ARRAY: CorElementType = 20
ELEMENT_TYPE_GENERICINST: CorElementType = 21
ELEMENT_TYPE_TYPEDBYREF: CorElementType = 22
ELEMENT_TYPE_I: CorElementType = 24
ELEMENT_TYPE_U: CorElementType = 25
ELEMENT_TYPE_FNPTR: CorElementType = 27
ELEMENT_TYPE_OBJECT: CorElementType = 28
ELEMENT_TYPE_SZARRAY: CorElementType = 29
ELEMENT_TYPE_MVAR: CorElementType = 30
ELEMENT_TYPE_CMOD_REQD: CorElementType = 31
ELEMENT_TYPE_CMOD_OPT: CorElementType = 32
ELEMENT_TYPE_INTERNAL: CorElementType = 33
ELEMENT_TYPE_MAX: CorElementType = 34
ELEMENT_TYPE_MODIFIER: CorElementType = 64
ELEMENT_TYPE_SENTINEL: CorElementType = 65
ELEMENT_TYPE_PINNED: CorElementType = 69
CorErrorIfEmitOutOfOrder = Int32
CorErrorIfEmitOutOfOrder_MDErrorOutOfOrderDefault: CorErrorIfEmitOutOfOrder = 0
CorErrorIfEmitOutOfOrder_MDErrorOutOfOrderNone: CorErrorIfEmitOutOfOrder = 0
CorErrorIfEmitOutOfOrder_MDErrorOutOfOrderAll: CorErrorIfEmitOutOfOrder = -1
CorErrorIfEmitOutOfOrder_MDMethodOutOfOrder: CorErrorIfEmitOutOfOrder = 1
CorErrorIfEmitOutOfOrder_MDFieldOutOfOrder: CorErrorIfEmitOutOfOrder = 2
CorErrorIfEmitOutOfOrder_MDParamOutOfOrder: CorErrorIfEmitOutOfOrder = 4
CorErrorIfEmitOutOfOrder_MDPropertyOutOfOrder: CorErrorIfEmitOutOfOrder = 8
CorErrorIfEmitOutOfOrder_MDEventOutOfOrder: CorErrorIfEmitOutOfOrder = 16
CorEventAttr = Int32
CorEventAttr_evSpecialName: CorEventAttr = 512
CorEventAttr_evReservedMask: CorEventAttr = 1024
CorEventAttr_evRTSpecialName: CorEventAttr = 1024
CorExceptionFlag = Int32
COR_ILEXCEPTION_CLAUSE_NONE: CorExceptionFlag = 0
COR_ILEXCEPTION_CLAUSE_OFFSETLEN: CorExceptionFlag = 0
COR_ILEXCEPTION_CLAUSE_DEPRECATED: CorExceptionFlag = 0
COR_ILEXCEPTION_CLAUSE_FILTER: CorExceptionFlag = 1
COR_ILEXCEPTION_CLAUSE_FINALLY: CorExceptionFlag = 2
COR_ILEXCEPTION_CLAUSE_FAULT: CorExceptionFlag = 4
COR_ILEXCEPTION_CLAUSE_DUPLICATED: CorExceptionFlag = 8
CorFieldAttr = Int32
CorFieldAttr_fdFieldAccessMask: CorFieldAttr = 7
CorFieldAttr_fdPrivateScope: CorFieldAttr = 0
CorFieldAttr_fdPrivate: CorFieldAttr = 1
CorFieldAttr_fdFamANDAssem: CorFieldAttr = 2
CorFieldAttr_fdAssembly: CorFieldAttr = 3
CorFieldAttr_fdFamily: CorFieldAttr = 4
CorFieldAttr_fdFamORAssem: CorFieldAttr = 5
CorFieldAttr_fdPublic: CorFieldAttr = 6
CorFieldAttr_fdStatic: CorFieldAttr = 16
CorFieldAttr_fdInitOnly: CorFieldAttr = 32
CorFieldAttr_fdLiteral: CorFieldAttr = 64
CorFieldAttr_fdNotSerialized: CorFieldAttr = 128
CorFieldAttr_fdSpecialName: CorFieldAttr = 512
CorFieldAttr_fdPinvokeImpl: CorFieldAttr = 8192
CorFieldAttr_fdReservedMask: CorFieldAttr = 38144
CorFieldAttr_fdRTSpecialName: CorFieldAttr = 1024
CorFieldAttr_fdHasFieldMarshal: CorFieldAttr = 4096
CorFieldAttr_fdHasDefault: CorFieldAttr = 32768
CorFieldAttr_fdHasFieldRVA: CorFieldAttr = 256
CorFileFlags = Int32
CorFileFlags_ffContainsMetaData: CorFileFlags = 0
CorFileFlags_ffContainsNoMetaData: CorFileFlags = 1
CorFileMapping = Int32
CorFileMapping_fmFlat: CorFileMapping = 0
CorFileMapping_fmExecutableImage: CorFileMapping = 1
CorGenericParamAttr = Int32
CorGenericParamAttr_gpVarianceMask: CorGenericParamAttr = 3
CorGenericParamAttr_gpNonVariant: CorGenericParamAttr = 0
CorGenericParamAttr_gpCovariant: CorGenericParamAttr = 1
CorGenericParamAttr_gpContravariant: CorGenericParamAttr = 2
CorGenericParamAttr_gpSpecialConstraintMask: CorGenericParamAttr = 28
CorGenericParamAttr_gpNoSpecialConstraint: CorGenericParamAttr = 0
CorGenericParamAttr_gpReferenceTypeConstraint: CorGenericParamAttr = 4
CorGenericParamAttr_gpNotNullableValueTypeConstraint: CorGenericParamAttr = 8
CorGenericParamAttr_gpDefaultConstructorConstraint: CorGenericParamAttr = 16
CorILMethodFlags = Int32
CorILMethod_InitLocals: CorILMethodFlags = 16
CorILMethod_MoreSects: CorILMethodFlags = 8
CorILMethod_CompressedIL: CorILMethodFlags = 64
CorILMethod_FormatShift: CorILMethodFlags = 3
CorILMethod_FormatMask: CorILMethodFlags = 7
CorILMethod_TinyFormat: CorILMethodFlags = 2
CorILMethod_SmallFormat: CorILMethodFlags = 0
CorILMethod_FatFormat: CorILMethodFlags = 3
CorILMethod_TinyFormat1: CorILMethodFlags = 6
CorILMethodSect = Int32
CorILMethod_Sect_Reserved: CorILMethodSect = 0
CorILMethod_Sect_EHTable: CorILMethodSect = 1
CorILMethod_Sect_OptILTable: CorILMethodSect = 2
CorILMethod_Sect_KindMask: CorILMethodSect = 63
CorILMethod_Sect_FatFormat: CorILMethodSect = 64
CorILMethod_Sect_MoreSects: CorILMethodSect = 128
CorImportOptions = Int32
CorImportOptions_MDImportOptionDefault: CorImportOptions = 0
CorImportOptions_MDImportOptionAll: CorImportOptions = -1
CorImportOptions_MDImportOptionAllTypeDefs: CorImportOptions = 1
CorImportOptions_MDImportOptionAllMethodDefs: CorImportOptions = 2
CorImportOptions_MDImportOptionAllFieldDefs: CorImportOptions = 4
CorImportOptions_MDImportOptionAllProperties: CorImportOptions = 8
CorImportOptions_MDImportOptionAllEvents: CorImportOptions = 16
CorImportOptions_MDImportOptionAllCustomAttributes: CorImportOptions = 32
CorImportOptions_MDImportOptionAllExportedTypes: CorImportOptions = 64
CorLinkerOptions = Int32
CorLinkerOptions_MDAssembly: CorLinkerOptions = 0
CorLinkerOptions_MDNetModule: CorLinkerOptions = 1
CorLocalRefPreservation = Int32
CorLocalRefPreservation_MDPreserveLocalRefsNone: CorLocalRefPreservation = 0
CorLocalRefPreservation_MDPreserveLocalTypeRef: CorLocalRefPreservation = 1
CorLocalRefPreservation_MDPreserveLocalMemberRef: CorLocalRefPreservation = 2
CorManifestResourceFlags = Int32
CorManifestResourceFlags_mrVisibilityMask: CorManifestResourceFlags = 7
CorManifestResourceFlags_mrPublic: CorManifestResourceFlags = 1
CorManifestResourceFlags_mrPrivate: CorManifestResourceFlags = 2
CorMethodAttr = Int32
CorMethodAttr_mdMemberAccessMask: CorMethodAttr = 7
CorMethodAttr_mdPrivateScope: CorMethodAttr = 0
CorMethodAttr_mdPrivate: CorMethodAttr = 1
CorMethodAttr_mdFamANDAssem: CorMethodAttr = 2
CorMethodAttr_mdAssem: CorMethodAttr = 3
CorMethodAttr_mdFamily: CorMethodAttr = 4
CorMethodAttr_mdFamORAssem: CorMethodAttr = 5
CorMethodAttr_mdPublic: CorMethodAttr = 6
CorMethodAttr_mdStatic: CorMethodAttr = 16
CorMethodAttr_mdFinal: CorMethodAttr = 32
CorMethodAttr_mdVirtual: CorMethodAttr = 64
CorMethodAttr_mdHideBySig: CorMethodAttr = 128
CorMethodAttr_mdVtableLayoutMask: CorMethodAttr = 256
CorMethodAttr_mdReuseSlot: CorMethodAttr = 0
CorMethodAttr_mdNewSlot: CorMethodAttr = 256
CorMethodAttr_mdCheckAccessOnOverride: CorMethodAttr = 512
CorMethodAttr_mdAbstract: CorMethodAttr = 1024
CorMethodAttr_mdSpecialName: CorMethodAttr = 2048
CorMethodAttr_mdPinvokeImpl: CorMethodAttr = 8192
CorMethodAttr_mdUnmanagedExport: CorMethodAttr = 8
CorMethodAttr_mdReservedMask: CorMethodAttr = 53248
CorMethodAttr_mdRTSpecialName: CorMethodAttr = 4096
CorMethodAttr_mdHasSecurity: CorMethodAttr = 16384
CorMethodAttr_mdRequireSecObject: CorMethodAttr = 32768
CorMethodImpl = Int32
CorMethodImpl_miCodeTypeMask: CorMethodImpl = 3
CorMethodImpl_miIL: CorMethodImpl = 0
CorMethodImpl_miNative: CorMethodImpl = 1
CorMethodImpl_miOPTIL: CorMethodImpl = 2
CorMethodImpl_miRuntime: CorMethodImpl = 3
CorMethodImpl_miManagedMask: CorMethodImpl = 4
CorMethodImpl_miUnmanaged: CorMethodImpl = 4
CorMethodImpl_miManaged: CorMethodImpl = 0
CorMethodImpl_miForwardRef: CorMethodImpl = 16
CorMethodImpl_miPreserveSig: CorMethodImpl = 128
CorMethodImpl_miInternalCall: CorMethodImpl = 4096
CorMethodImpl_miSynchronized: CorMethodImpl = 32
CorMethodImpl_miNoInlining: CorMethodImpl = 8
CorMethodImpl_miAggressiveInlining: CorMethodImpl = 256
CorMethodImpl_miNoOptimization: CorMethodImpl = 64
CorMethodImpl_miSecurityMitigations: CorMethodImpl = 1024
CorMethodImpl_miUserMask: CorMethodImpl = 5628
CorMethodImpl_miMaxMethodImplVal: CorMethodImpl = 65535
CorMethodSemanticsAttr = Int32
CorMethodSemanticsAttr_msSetter: CorMethodSemanticsAttr = 1
CorMethodSemanticsAttr_msGetter: CorMethodSemanticsAttr = 2
CorMethodSemanticsAttr_msOther: CorMethodSemanticsAttr = 4
CorMethodSemanticsAttr_msAddOn: CorMethodSemanticsAttr = 8
CorMethodSemanticsAttr_msRemoveOn: CorMethodSemanticsAttr = 16
CorMethodSemanticsAttr_msFire: CorMethodSemanticsAttr = 32
CorNativeLinkFlags = Int32
CorNativeLinkFlags_nlfNone: CorNativeLinkFlags = 0
CorNativeLinkFlags_nlfLastError: CorNativeLinkFlags = 1
CorNativeLinkFlags_nlfNoMangle: CorNativeLinkFlags = 2
CorNativeLinkFlags_nlfMaxValue: CorNativeLinkFlags = 3
CorNativeLinkType = Int32
CorNativeLinkType_nltNone: CorNativeLinkType = 1
CorNativeLinkType_nltAnsi: CorNativeLinkType = 2
CorNativeLinkType_nltUnicode: CorNativeLinkType = 3
CorNativeLinkType_nltAuto: CorNativeLinkType = 4
CorNativeLinkType_nltOle: CorNativeLinkType = 5
CorNativeLinkType_nltMaxValue: CorNativeLinkType = 7
CorNativeType = Int32
NATIVE_TYPE_END: CorNativeType = 0
NATIVE_TYPE_VOID: CorNativeType = 1
NATIVE_TYPE_BOOLEAN: CorNativeType = 2
NATIVE_TYPE_I1: CorNativeType = 3
NATIVE_TYPE_U1: CorNativeType = 4
NATIVE_TYPE_I2: CorNativeType = 5
NATIVE_TYPE_U2: CorNativeType = 6
NATIVE_TYPE_I4: CorNativeType = 7
NATIVE_TYPE_U4: CorNativeType = 8
NATIVE_TYPE_I8: CorNativeType = 9
NATIVE_TYPE_U8: CorNativeType = 10
NATIVE_TYPE_R4: CorNativeType = 11
NATIVE_TYPE_R8: CorNativeType = 12
NATIVE_TYPE_SYSCHAR: CorNativeType = 13
NATIVE_TYPE_VARIANT: CorNativeType = 14
NATIVE_TYPE_CURRENCY: CorNativeType = 15
NATIVE_TYPE_PTR: CorNativeType = 16
NATIVE_TYPE_DECIMAL: CorNativeType = 17
NATIVE_TYPE_DATE: CorNativeType = 18
NATIVE_TYPE_BSTR: CorNativeType = 19
NATIVE_TYPE_LPSTR: CorNativeType = 20
NATIVE_TYPE_LPWSTR: CorNativeType = 21
NATIVE_TYPE_LPTSTR: CorNativeType = 22
NATIVE_TYPE_FIXEDSYSSTRING: CorNativeType = 23
NATIVE_TYPE_OBJECTREF: CorNativeType = 24
NATIVE_TYPE_IUNKNOWN: CorNativeType = 25
NATIVE_TYPE_IDISPATCH: CorNativeType = 26
NATIVE_TYPE_STRUCT: CorNativeType = 27
NATIVE_TYPE_INTF: CorNativeType = 28
NATIVE_TYPE_SAFEARRAY: CorNativeType = 29
NATIVE_TYPE_FIXEDARRAY: CorNativeType = 30
NATIVE_TYPE_INT: CorNativeType = 31
NATIVE_TYPE_UINT: CorNativeType = 32
NATIVE_TYPE_NESTEDSTRUCT: CorNativeType = 33
NATIVE_TYPE_BYVALSTR: CorNativeType = 34
NATIVE_TYPE_ANSIBSTR: CorNativeType = 35
NATIVE_TYPE_TBSTR: CorNativeType = 36
NATIVE_TYPE_VARIANTBOOL: CorNativeType = 37
NATIVE_TYPE_FUNC: CorNativeType = 38
NATIVE_TYPE_ASANY: CorNativeType = 40
NATIVE_TYPE_ARRAY: CorNativeType = 42
NATIVE_TYPE_LPSTRUCT: CorNativeType = 43
NATIVE_TYPE_CUSTOMMARSHALER: CorNativeType = 44
NATIVE_TYPE_ERROR: CorNativeType = 45
NATIVE_TYPE_IINSPECTABLE: CorNativeType = 46
NATIVE_TYPE_HSTRING: CorNativeType = 47
NATIVE_TYPE_LPUTF8STR: CorNativeType = 48
NATIVE_TYPE_MAX: CorNativeType = 80
CorNotificationForTokenMovement = Int32
CorNotificationForTokenMovement_MDNotifyDefault: CorNotificationForTokenMovement = 15
CorNotificationForTokenMovement_MDNotifyAll: CorNotificationForTokenMovement = -1
CorNotificationForTokenMovement_MDNotifyNone: CorNotificationForTokenMovement = 0
CorNotificationForTokenMovement_MDNotifyMethodDef: CorNotificationForTokenMovement = 1
CorNotificationForTokenMovement_MDNotifyMemberRef: CorNotificationForTokenMovement = 2
CorNotificationForTokenMovement_MDNotifyFieldDef: CorNotificationForTokenMovement = 4
CorNotificationForTokenMovement_MDNotifyTypeRef: CorNotificationForTokenMovement = 8
CorNotificationForTokenMovement_MDNotifyTypeDef: CorNotificationForTokenMovement = 16
CorNotificationForTokenMovement_MDNotifyParamDef: CorNotificationForTokenMovement = 32
CorNotificationForTokenMovement_MDNotifyInterfaceImpl: CorNotificationForTokenMovement = 64
CorNotificationForTokenMovement_MDNotifyProperty: CorNotificationForTokenMovement = 128
CorNotificationForTokenMovement_MDNotifyEvent: CorNotificationForTokenMovement = 256
CorNotificationForTokenMovement_MDNotifySignature: CorNotificationForTokenMovement = 512
CorNotificationForTokenMovement_MDNotifyTypeSpec: CorNotificationForTokenMovement = 1024
CorNotificationForTokenMovement_MDNotifyCustomAttribute: CorNotificationForTokenMovement = 2048
CorNotificationForTokenMovement_MDNotifySecurityValue: CorNotificationForTokenMovement = 4096
CorNotificationForTokenMovement_MDNotifyPermission: CorNotificationForTokenMovement = 8192
CorNotificationForTokenMovement_MDNotifyModuleRef: CorNotificationForTokenMovement = 16384
CorNotificationForTokenMovement_MDNotifyNameSpace: CorNotificationForTokenMovement = 32768
CorNotificationForTokenMovement_MDNotifyAssemblyRef: CorNotificationForTokenMovement = 16777216
CorNotificationForTokenMovement_MDNotifyFile: CorNotificationForTokenMovement = 33554432
CorNotificationForTokenMovement_MDNotifyExportedType: CorNotificationForTokenMovement = 67108864
CorNotificationForTokenMovement_MDNotifyResource: CorNotificationForTokenMovement = 134217728
CorOpenFlags = Int32
CorOpenFlags_ofRead: CorOpenFlags = 0
CorOpenFlags_ofWrite: CorOpenFlags = 1
CorOpenFlags_ofReadWriteMask: CorOpenFlags = 1
CorOpenFlags_ofCopyMemory: CorOpenFlags = 2
CorOpenFlags_ofReadOnly: CorOpenFlags = 16
CorOpenFlags_ofTakeOwnership: CorOpenFlags = 32
CorOpenFlags_ofNoTypeLib: CorOpenFlags = 128
CorOpenFlags_ofNoTransform: CorOpenFlags = 4096
CorOpenFlags_ofCheckIntegrity: CorOpenFlags = 2048
CorOpenFlags_ofReserved1: CorOpenFlags = 256
CorOpenFlags_ofReserved2: CorOpenFlags = 512
CorOpenFlags_ofReserved3: CorOpenFlags = 1024
CorOpenFlags_ofReserved: CorOpenFlags = -6336
CorPEKind = Int32
CorPEKind_peNot: CorPEKind = 0
CorPEKind_peILonly: CorPEKind = 1
CorPEKind_pe32BitRequired: CorPEKind = 2
CorPEKind_pe32Plus: CorPEKind = 4
CorPEKind_pe32Unmanaged: CorPEKind = 8
CorPEKind_pe32BitPreferred: CorPEKind = 16
CorParamAttr = Int32
CorParamAttr_pdIn: CorParamAttr = 1
CorParamAttr_pdOut: CorParamAttr = 2
CorParamAttr_pdOptional: CorParamAttr = 16
CorParamAttr_pdReservedMask: CorParamAttr = 61440
CorParamAttr_pdHasDefault: CorParamAttr = 4096
CorParamAttr_pdHasFieldMarshal: CorParamAttr = 8192
CorParamAttr_pdUnused: CorParamAttr = 53216
CorPinvokeMap = Int32
CorPinvokeMap_pmNoMangle: CorPinvokeMap = 1
CorPinvokeMap_pmCharSetMask: CorPinvokeMap = 6
CorPinvokeMap_pmCharSetNotSpec: CorPinvokeMap = 0
CorPinvokeMap_pmCharSetAnsi: CorPinvokeMap = 2
CorPinvokeMap_pmCharSetUnicode: CorPinvokeMap = 4
CorPinvokeMap_pmCharSetAuto: CorPinvokeMap = 6
CorPinvokeMap_pmBestFitUseAssem: CorPinvokeMap = 0
CorPinvokeMap_pmBestFitEnabled: CorPinvokeMap = 16
CorPinvokeMap_pmBestFitDisabled: CorPinvokeMap = 32
CorPinvokeMap_pmBestFitMask: CorPinvokeMap = 48
CorPinvokeMap_pmThrowOnUnmappableCharUseAssem: CorPinvokeMap = 0
CorPinvokeMap_pmThrowOnUnmappableCharEnabled: CorPinvokeMap = 4096
CorPinvokeMap_pmThrowOnUnmappableCharDisabled: CorPinvokeMap = 8192
CorPinvokeMap_pmThrowOnUnmappableCharMask: CorPinvokeMap = 12288
CorPinvokeMap_pmSupportsLastError: CorPinvokeMap = 64
CorPinvokeMap_pmCallConvMask: CorPinvokeMap = 1792
CorPinvokeMap_pmCallConvWinapi: CorPinvokeMap = 256
CorPinvokeMap_pmCallConvCdecl: CorPinvokeMap = 512
CorPinvokeMap_pmCallConvStdcall: CorPinvokeMap = 768
CorPinvokeMap_pmCallConvThiscall: CorPinvokeMap = 1024
CorPinvokeMap_pmCallConvFastcall: CorPinvokeMap = 1280
CorPinvokeMap_pmMaxValue: CorPinvokeMap = 65535
CorPropertyAttr = Int32
CorPropertyAttr_prSpecialName: CorPropertyAttr = 512
CorPropertyAttr_prReservedMask: CorPropertyAttr = 62464
CorPropertyAttr_prRTSpecialName: CorPropertyAttr = 1024
CorPropertyAttr_prHasDefault: CorPropertyAttr = 4096
CorPropertyAttr_prUnused: CorPropertyAttr = 59903
CorRefToDefCheck = Int32
CorRefToDefCheck_MDRefToDefDefault: CorRefToDefCheck = 3
CorRefToDefCheck_MDRefToDefAll: CorRefToDefCheck = -1
CorRefToDefCheck_MDRefToDefNone: CorRefToDefCheck = 0
CorRefToDefCheck_MDTypeRefToDef: CorRefToDefCheck = 1
CorRefToDefCheck_MDMemberRefToDef: CorRefToDefCheck = 2
CorRegFlags = Int32
CorRegFlags_regNoCopy: CorRegFlags = 1
CorRegFlags_regConfig: CorRegFlags = 2
CorRegFlags_regHasRefs: CorRegFlags = 4
CorSaveSize = Int32
CorSaveSize_cssAccurate: CorSaveSize = 0
CorSaveSize_cssQuick: CorSaveSize = 1
CorSaveSize_cssDiscardTransientCAs: CorSaveSize = 2
CorSerializationType = Int32
SERIALIZATION_TYPE_UNDEFINED: CorSerializationType = 0
SERIALIZATION_TYPE_BOOLEAN: CorSerializationType = 2
SERIALIZATION_TYPE_CHAR: CorSerializationType = 3
SERIALIZATION_TYPE_I1: CorSerializationType = 4
SERIALIZATION_TYPE_U1: CorSerializationType = 5
SERIALIZATION_TYPE_I2: CorSerializationType = 6
SERIALIZATION_TYPE_U2: CorSerializationType = 7
SERIALIZATION_TYPE_I4: CorSerializationType = 8
SERIALIZATION_TYPE_U4: CorSerializationType = 9
SERIALIZATION_TYPE_I8: CorSerializationType = 10
SERIALIZATION_TYPE_U8: CorSerializationType = 11
SERIALIZATION_TYPE_R4: CorSerializationType = 12
SERIALIZATION_TYPE_R8: CorSerializationType = 13
SERIALIZATION_TYPE_STRING: CorSerializationType = 14
SERIALIZATION_TYPE_SZARRAY: CorSerializationType = 29
SERIALIZATION_TYPE_TYPE: CorSerializationType = 80
SERIALIZATION_TYPE_TAGGED_OBJECT: CorSerializationType = 81
SERIALIZATION_TYPE_FIELD: CorSerializationType = 83
SERIALIZATION_TYPE_PROPERTY: CorSerializationType = 84
SERIALIZATION_TYPE_ENUM: CorSerializationType = 85
CorSetENC = Int32
CorSetENC_MDSetENCOn: CorSetENC = 1
CorSetENC_MDSetENCOff: CorSetENC = 2
CorSetENC_MDUpdateENC: CorSetENC = 1
CorSetENC_MDUpdateFull: CorSetENC = 2
CorSetENC_MDUpdateExtension: CorSetENC = 3
CorSetENC_MDUpdateIncremental: CorSetENC = 4
CorSetENC_MDUpdateDelta: CorSetENC = 5
CorSetENC_MDUpdateMask: CorSetENC = 7
CorThreadSafetyOptions = Int32
CorThreadSafetyOptions_MDThreadSafetyDefault: CorThreadSafetyOptions = 0
CorThreadSafetyOptions_MDThreadSafetyOff: CorThreadSafetyOptions = 0
CorThreadSafetyOptions_MDThreadSafetyOn: CorThreadSafetyOptions = 1
CorTokenType = Int32
CorTokenType_mdtModule: CorTokenType = 0
CorTokenType_mdtTypeRef: CorTokenType = 16777216
CorTokenType_mdtTypeDef: CorTokenType = 33554432
CorTokenType_mdtFieldDef: CorTokenType = 67108864
CorTokenType_mdtMethodDef: CorTokenType = 100663296
CorTokenType_mdtParamDef: CorTokenType = 134217728
CorTokenType_mdtInterfaceImpl: CorTokenType = 150994944
CorTokenType_mdtMemberRef: CorTokenType = 167772160
CorTokenType_mdtCustomAttribute: CorTokenType = 201326592
CorTokenType_mdtPermission: CorTokenType = 234881024
CorTokenType_mdtSignature: CorTokenType = 285212672
CorTokenType_mdtEvent: CorTokenType = 335544320
CorTokenType_mdtProperty: CorTokenType = 385875968
CorTokenType_mdtMethodImpl: CorTokenType = 419430400
CorTokenType_mdtModuleRef: CorTokenType = 436207616
CorTokenType_mdtTypeSpec: CorTokenType = 452984832
CorTokenType_mdtAssembly: CorTokenType = 536870912
CorTokenType_mdtAssemblyRef: CorTokenType = 587202560
CorTokenType_mdtFile: CorTokenType = 637534208
CorTokenType_mdtExportedType: CorTokenType = 654311424
CorTokenType_mdtManifestResource: CorTokenType = 671088640
CorTokenType_mdtGenericParam: CorTokenType = 704643072
CorTokenType_mdtMethodSpec: CorTokenType = 721420288
CorTokenType_mdtGenericParamConstraint: CorTokenType = 738197504
CorTokenType_mdtString: CorTokenType = 1879048192
CorTokenType_mdtName: CorTokenType = 1895825408
CorTokenType_mdtBaseType: CorTokenType = 1912602624
CorTypeAttr = Int32
CorTypeAttr_tdVisibilityMask: CorTypeAttr = 7
CorTypeAttr_tdNotPublic: CorTypeAttr = 0
CorTypeAttr_tdPublic: CorTypeAttr = 1
CorTypeAttr_tdNestedPublic: CorTypeAttr = 2
CorTypeAttr_tdNestedPrivate: CorTypeAttr = 3
CorTypeAttr_tdNestedFamily: CorTypeAttr = 4
CorTypeAttr_tdNestedAssembly: CorTypeAttr = 5
CorTypeAttr_tdNestedFamANDAssem: CorTypeAttr = 6
CorTypeAttr_tdNestedFamORAssem: CorTypeAttr = 7
CorTypeAttr_tdLayoutMask: CorTypeAttr = 24
CorTypeAttr_tdAutoLayout: CorTypeAttr = 0
CorTypeAttr_tdSequentialLayout: CorTypeAttr = 8
CorTypeAttr_tdExplicitLayout: CorTypeAttr = 16
CorTypeAttr_tdClassSemanticsMask: CorTypeAttr = 32
CorTypeAttr_tdClass: CorTypeAttr = 0
CorTypeAttr_tdInterface: CorTypeAttr = 32
CorTypeAttr_tdAbstract: CorTypeAttr = 128
CorTypeAttr_tdSealed: CorTypeAttr = 256
CorTypeAttr_tdSpecialName: CorTypeAttr = 1024
CorTypeAttr_tdImport: CorTypeAttr = 4096
CorTypeAttr_tdSerializable: CorTypeAttr = 8192
CorTypeAttr_tdWindowsRuntime: CorTypeAttr = 16384
CorTypeAttr_tdStringFormatMask: CorTypeAttr = 196608
CorTypeAttr_tdAnsiClass: CorTypeAttr = 0
CorTypeAttr_tdUnicodeClass: CorTypeAttr = 65536
CorTypeAttr_tdAutoClass: CorTypeAttr = 131072
CorTypeAttr_tdCustomFormatClass: CorTypeAttr = 196608
CorTypeAttr_tdCustomFormatMask: CorTypeAttr = 12582912
CorTypeAttr_tdBeforeFieldInit: CorTypeAttr = 1048576
CorTypeAttr_tdForwarder: CorTypeAttr = 2097152
CorTypeAttr_tdReservedMask: CorTypeAttr = 264192
CorTypeAttr_tdRTSpecialName: CorTypeAttr = 2048
CorTypeAttr_tdHasSecurity: CorTypeAttr = 262144
CorUnmanagedCallingConvention = Int32
IMAGE_CEE_UNMANAGED_CALLCONV_C: CorUnmanagedCallingConvention = 1
IMAGE_CEE_UNMANAGED_CALLCONV_STDCALL: CorUnmanagedCallingConvention = 2
IMAGE_CEE_UNMANAGED_CALLCONV_THISCALL: CorUnmanagedCallingConvention = 3
IMAGE_CEE_UNMANAGED_CALLCONV_FASTCALL: CorUnmanagedCallingConvention = 4
IMAGE_CEE_CS_CALLCONV_C: CorUnmanagedCallingConvention = 1
IMAGE_CEE_CS_CALLCONV_STDCALL: CorUnmanagedCallingConvention = 2
IMAGE_CEE_CS_CALLCONV_THISCALL: CorUnmanagedCallingConvention = 3
IMAGE_CEE_CS_CALLCONV_FASTCALL: CorUnmanagedCallingConvention = 4
CorValidatorModuleType = Int32
CorValidatorModuleType_ValidatorModuleTypeInvalid: CorValidatorModuleType = 0
CorValidatorModuleType_ValidatorModuleTypeMin: CorValidatorModuleType = 1
CorValidatorModuleType_ValidatorModuleTypePE: CorValidatorModuleType = 1
CorValidatorModuleType_ValidatorModuleTypeObj: CorValidatorModuleType = 2
CorValidatorModuleType_ValidatorModuleTypeEnc: CorValidatorModuleType = 3
CorValidatorModuleType_ValidatorModuleTypeIncr: CorValidatorModuleType = 4
CorValidatorModuleType_ValidatorModuleTypeMax: CorValidatorModuleType = 4
class ICeeGen(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7ed1bdff-8e36-11d2-9c-56-00-a0-c9-b7-cc-45')
    @commethod(3)
    def EmitString(self, lpString: Windows.Win32.Foundation.PWSTR, RVA: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetString(self, RVA: UInt32, lpString: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AllocateMethodBuffer(self, cchBuffer: UInt32, lpBuffer: POINTER(POINTER(Byte)), RVA: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMethodBuffer(self, RVA: UInt32, lpBuffer: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetIMapTokenIface(self, pIMapToken: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GenerateCeeFile(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetIlSection(self, section: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStringSection(self, section: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddSectionReloc(self, section: c_void_p, offset: UInt32, relativeTo: c_void_p, relocType: Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSectionCreate(self, name: Windows.Win32.Foundation.PSTR, flags: UInt32, section: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSectionDataLen(self, section: c_void_p, dataLen: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSectionBlock(self, section: c_void_p, len: UInt32, align: UInt32, ppBytes: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def TruncateSection(self, section: c_void_p, len: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GenerateCeeMemoryImage(self, ppImage: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ComputePointer(self, section: c_void_p, RVA: UInt32, lpBuffer: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class IHostFilter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d0e80dd3-12d4-11d3-b3-9d-00-c0-4f-f8-17-95')
    @commethod(3)
    def MarkToken(self, tk: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMAGE_COR_ILMETHOD(EasyCastUnion):
    Tiny: Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_TINY
    Fat: Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_FAT
class IMAGE_COR_ILMETHOD_FAT(EasyCastStructure):
    _bitfield: UInt32
    CodeSize: UInt32
    LocalVarSigTok: UInt32
class IMAGE_COR_ILMETHOD_SECT_EH(EasyCastUnion):
    Small: Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_EH_SMALL
    Fat: Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_EH_FAT
class IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT(EasyCastStructure):
    Flags: Windows.Win32.System.WinRT.Metadata.CorExceptionFlag
    TryOffset: UInt32
    TryLength: UInt32
    HandlerOffset: UInt32
    HandlerLength: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        ClassToken: UInt32
        FilterOffset: UInt32
if ARCH in 'X64,ARM64':
    class IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL(EasyCastStructure):
        _bitfield1: UInt32
        _bitfield2: UInt32
        Anonymous: _Anonymous_e__Union
        class _Anonymous_e__Union(EasyCastUnion):
            ClassToken: UInt32
            FilterOffset: UInt32
if ARCH in 'X86':
    class IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL(EasyCastStructure):
        _bitfield1: Int32
        _bitfield2: UInt32
        Anonymous: _Anonymous_e__Union
        class _Anonymous_e__Union(EasyCastUnion):
            ClassToken: UInt32
            FilterOffset: UInt32
class IMAGE_COR_ILMETHOD_SECT_EH_FAT(EasyCastStructure):
    SectFat: Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_FAT
    Clauses: Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT * 1
class IMAGE_COR_ILMETHOD_SECT_EH_SMALL(EasyCastStructure):
    SectSmall: Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_SMALL
    Reserved: UInt16
    Clauses: Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL * 1
class IMAGE_COR_ILMETHOD_SECT_FAT(EasyCastStructure):
    _bitfield: UInt32
class IMAGE_COR_ILMETHOD_SECT_SMALL(EasyCastStructure):
    Kind: Byte
    DataSize: Byte
class IMAGE_COR_ILMETHOD_TINY(EasyCastStructure):
    Flags_CodeSize: Byte
class IMAGE_COR_VTABLEFIXUP(EasyCastStructure):
    RVA: UInt32
    Count: UInt16
    Type: UInt16
class IMapToken(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('06a3ea8b-0225-11d1-bf-72-00-c0-4f-c3-1e-12')
    @commethod(3)
    def Map(self, tkImp: UInt32, tkEmit: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataAssemblyEmit(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('211ef15b-5317-4438-b1-96-de-c8-7b-88-76-93')
    @commethod(3)
    def DefineAssembly(self, pbPublicKey: c_void_p, cbPublicKey: UInt32, ulHashAlgId: UInt32, szName: Windows.Win32.Foundation.PWSTR, pMetaData: POINTER(Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA_head), dwAssemblyFlags: UInt32, pma: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DefineAssemblyRef(self, pbPublicKeyOrToken: c_void_p, cbPublicKeyOrToken: UInt32, szName: Windows.Win32.Foundation.PWSTR, pMetaData: POINTER(Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA_head), pbHashValue: c_void_p, cbHashValue: UInt32, dwAssemblyRefFlags: UInt32, pmdar: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DefineFile(self, szName: Windows.Win32.Foundation.PWSTR, pbHashValue: c_void_p, cbHashValue: UInt32, dwFileFlags: UInt32, pmdf: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DefineExportedType(self, szName: Windows.Win32.Foundation.PWSTR, tkImplementation: UInt32, tkTypeDef: UInt32, dwExportedTypeFlags: UInt32, pmdct: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DefineManifestResource(self, szName: Windows.Win32.Foundation.PWSTR, tkImplementation: UInt32, dwOffset: UInt32, dwResourceFlags: UInt32, pmdmr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetAssemblyProps(self, pma: UInt32, pbPublicKey: c_void_p, cbPublicKey: UInt32, ulHashAlgId: UInt32, szName: Windows.Win32.Foundation.PWSTR, pMetaData: POINTER(Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA_head), dwAssemblyFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetAssemblyRefProps(self, ar: UInt32, pbPublicKeyOrToken: c_void_p, cbPublicKeyOrToken: UInt32, szName: Windows.Win32.Foundation.PWSTR, pMetaData: POINTER(Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA_head), pbHashValue: c_void_p, cbHashValue: UInt32, dwAssemblyRefFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetFileProps(self, file: UInt32, pbHashValue: c_void_p, cbHashValue: UInt32, dwFileFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetExportedTypeProps(self, ct: UInt32, tkImplementation: UInt32, tkTypeDef: UInt32, dwExportedTypeFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetManifestResourceProps(self, mr: UInt32, tkImplementation: UInt32, dwOffset: UInt32, dwResourceFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataAssemblyImport(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ee62470b-e94b-424e-9b-7c-2f-00-c9-24-9f-93')
    @commethod(3)
    def GetAssemblyProps(self, mda: UInt32, ppbPublicKey: POINTER(c_void_p), pcbPublicKey: POINTER(UInt32), pulHashAlgId: POINTER(UInt32), szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), pMetaData: POINTER(Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA_head), pdwAssemblyFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAssemblyRefProps(self, mdar: UInt32, ppbPublicKeyOrToken: POINTER(c_void_p), pcbPublicKeyOrToken: POINTER(UInt32), szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), pMetaData: POINTER(Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA_head), ppbHashValue: POINTER(c_void_p), pcbHashValue: POINTER(UInt32), pdwAssemblyRefFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileProps(self, mdf: UInt32, szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), ppbHashValue: POINTER(c_void_p), pcbHashValue: POINTER(UInt32), pdwFileFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetExportedTypeProps(self, mdct: UInt32, szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), ptkImplementation: POINTER(UInt32), ptkTypeDef: POINTER(UInt32), pdwExportedTypeFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetManifestResourceProps(self, mdmr: UInt32, szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), ptkImplementation: POINTER(UInt32), pdwOffset: POINTER(UInt32), pdwResourceFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumAssemblyRefs(self, phEnum: POINTER(c_void_p), rAssemblyRefs: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumFiles(self, phEnum: POINTER(c_void_p), rFiles: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumExportedTypes(self, phEnum: POINTER(c_void_p), rExportedTypes: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumManifestResources(self, phEnum: POINTER(c_void_p), rManifestResources: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAssemblyFromScope(self, ptkAssembly: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def FindExportedTypeByName(self, szName: Windows.Win32.Foundation.PWSTR, mdtExportedType: UInt32, ptkExportedType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def FindManifestResourceByName(self, szName: Windows.Win32.Foundation.PWSTR, ptkManifestResource: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CloseEnum(self, hEnum: c_void_p) -> Void: ...
    @commethod(16)
    def FindAssembliesByName(self, szAppBase: Windows.Win32.Foundation.PWSTR, szPrivateBin: Windows.Win32.Foundation.PWSTR, szAssemblyName: Windows.Win32.Foundation.PWSTR, ppIUnk: POINTER(Windows.Win32.System.Com.IUnknown_head), cMax: UInt32, pcAssemblies: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataDispenser(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('809c652e-7396-11d2-97-71-00-a0-c9-b4-d5-0c')
    @commethod(3)
    def DefineScope(self, rclsid: POINTER(Guid), dwCreateFlags: UInt32, riid: POINTER(Guid), ppIUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenScope(self, szScope: Windows.Win32.Foundation.PWSTR, dwOpenFlags: UInt32, riid: POINTER(Guid), ppIUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OpenScopeOnMemory(self, pData: c_void_p, cbData: UInt32, dwOpenFlags: UInt32, riid: POINTER(Guid), ppIUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataDispenserEx(c_void_p):
    extends: Windows.Win32.System.WinRT.Metadata.IMetaDataDispenser
    Guid = Guid('31bcfce2-dafb-11d2-9f-81-00-c0-4f-79-a0-a3')
    @commethod(6)
    def SetOption(self, optionid: POINTER(Guid), value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOption(self, optionid: POINTER(Guid), pvalue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OpenScopeOnITypeInfo(self, pITI: Windows.Win32.System.Com.ITypeInfo_head, dwOpenFlags: UInt32, riid: POINTER(Guid), ppIUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCORSystemDirectory(self, szBuffer: Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, pchBuffer: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FindAssembly(self, szAppBase: Windows.Win32.Foundation.PWSTR, szPrivateBin: Windows.Win32.Foundation.PWSTR, szGlobalBin: Windows.Win32.Foundation.PWSTR, szAssemblyName: Windows.Win32.Foundation.PWSTR, szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pcName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FindAssemblyModule(self, szAppBase: Windows.Win32.Foundation.PWSTR, szPrivateBin: Windows.Win32.Foundation.PWSTR, szGlobalBin: Windows.Win32.Foundation.PWSTR, szAssemblyName: Windows.Win32.Foundation.PWSTR, szModuleName: Windows.Win32.Foundation.PWSTR, szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pcName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataEmit(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ba3fee4c-ecb9-4e41-83-b7-18-3f-a4-1c-d8-59')
    @commethod(3)
    def SetModuleProps(self, szName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Save(self, szFile: Windows.Win32.Foundation.PWSTR, dwSaveFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SaveToStream(self, pIStream: Windows.Win32.System.Com.IStream_head, dwSaveFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSaveSize(self, fSave: Windows.Win32.System.WinRT.Metadata.CorSaveSize, pdwSaveSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DefineTypeDef(self, szTypeDef: Windows.Win32.Foundation.PWSTR, dwTypeDefFlags: UInt32, tkExtends: UInt32, rtkImplements: POINTER(UInt32), ptd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DefineNestedType(self, szTypeDef: Windows.Win32.Foundation.PWSTR, dwTypeDefFlags: UInt32, tkExtends: UInt32, rtkImplements: POINTER(UInt32), tdEncloser: UInt32, ptd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetHandler(self, pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DefineMethod(self, td: UInt32, szName: Windows.Win32.Foundation.PWSTR, dwMethodFlags: UInt32, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, ulCodeRVA: UInt32, dwImplFlags: UInt32, pmd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DefineMethodImpl(self, td: UInt32, tkBody: UInt32, tkDecl: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DefineTypeRefByName(self, tkResolutionScope: UInt32, szName: Windows.Win32.Foundation.PWSTR, ptr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DefineImportType(self, pAssemImport: Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyImport_head, pbHashValue: c_void_p, cbHashValue: UInt32, pImport: Windows.Win32.System.WinRT.Metadata.IMetaDataImport_head, tdImport: UInt32, pAssemEmit: Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyEmit_head, ptr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def DefineMemberRef(self, tkImport: UInt32, szName: Windows.Win32.Foundation.PWSTR, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def DefineImportMember(self, pAssemImport: Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyImport_head, pbHashValue: c_void_p, cbHashValue: UInt32, pImport: Windows.Win32.System.WinRT.Metadata.IMetaDataImport_head, mbMember: UInt32, pAssemEmit: Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyEmit_head, tkParent: UInt32, pmr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DefineEvent(self, td: UInt32, szEvent: Windows.Win32.Foundation.PWSTR, dwEventFlags: UInt32, tkEventType: UInt32, mdAddOn: UInt32, mdRemoveOn: UInt32, mdFire: UInt32, rmdOtherMethods: POINTER(UInt32), pmdEvent: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetClassLayout(self, td: UInt32, dwPackSize: UInt32, rFieldOffsets: POINTER(Windows.Win32.System.WinRT.Metadata.COR_FIELD_OFFSET_head), ulClassSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteClassLayout(self, td: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetFieldMarshal(self, tk: UInt32, pvNativeType: POINTER(Byte), cbNativeType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DeleteFieldMarshal(self, tk: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DefinePermissionSet(self, tk: UInt32, dwAction: UInt32, pvPermission: c_void_p, cbPermission: UInt32, ppm: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetRVA(self, md: UInt32, ulRVA: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetTokenFromSig(self, pvSig: POINTER(Byte), cbSig: UInt32, pmsig: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def DefineModuleRef(self, szName: Windows.Win32.Foundation.PWSTR, pmur: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetParent(self, mr: UInt32, tk: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetTokenFromTypeSpec(self, pvSig: POINTER(Byte), cbSig: UInt32, ptypespec: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SaveToMemory(self, pbData: c_void_p, cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def DefineUserString(self, szString: Windows.Win32.Foundation.PWSTR, cchString: UInt32, pstk: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DeleteToken(self, tkObj: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetMethodProps(self, md: UInt32, dwMethodFlags: UInt32, ulCodeRVA: UInt32, dwImplFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetTypeDefProps(self, td: UInt32, dwTypeDefFlags: UInt32, tkExtends: UInt32, rtkImplements: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetEventProps(self, ev: UInt32, dwEventFlags: UInt32, tkEventType: UInt32, mdAddOn: UInt32, mdRemoveOn: UInt32, mdFire: UInt32, rmdOtherMethods: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetPermissionSetProps(self, tk: UInt32, dwAction: UInt32, pvPermission: c_void_p, cbPermission: UInt32, ppm: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def DefinePinvokeMap(self, tk: UInt32, dwMappingFlags: UInt32, szImportName: Windows.Win32.Foundation.PWSTR, mrImportDLL: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetPinvokeMap(self, tk: UInt32, dwMappingFlags: UInt32, szImportName: Windows.Win32.Foundation.PWSTR, mrImportDLL: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def DeletePinvokeMap(self, tk: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def DefineCustomAttribute(self, tkOwner: UInt32, tkCtor: UInt32, pCustomAttribute: c_void_p, cbCustomAttribute: UInt32, pcv: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetCustomAttributeValue(self, pcv: UInt32, pCustomAttribute: c_void_p, cbCustomAttribute: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def DefineField(self, td: UInt32, szName: Windows.Win32.Foundation.PWSTR, dwFieldFlags: UInt32, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, dwCPlusTypeFlag: UInt32, pValue: c_void_p, cchValue: UInt32, pmd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def DefineProperty(self, td: UInt32, szProperty: Windows.Win32.Foundation.PWSTR, dwPropFlags: UInt32, pvSig: POINTER(Byte), cbSig: UInt32, dwCPlusTypeFlag: UInt32, pValue: c_void_p, cchValue: UInt32, mdSetter: UInt32, mdGetter: UInt32, rmdOtherMethods: POINTER(UInt32), pmdProp: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def DefineParam(self, md: UInt32, ulParamSeq: UInt32, szName: Windows.Win32.Foundation.PWSTR, dwParamFlags: UInt32, dwCPlusTypeFlag: UInt32, pValue: c_void_p, cchValue: UInt32, ppd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def SetFieldProps(self, fd: UInt32, dwFieldFlags: UInt32, dwCPlusTypeFlag: UInt32, pValue: c_void_p, cchValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def SetPropertyProps(self, pr: UInt32, dwPropFlags: UInt32, dwCPlusTypeFlag: UInt32, pValue: c_void_p, cchValue: UInt32, mdSetter: UInt32, mdGetter: UInt32, rmdOtherMethods: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def SetParamProps(self, pd: UInt32, szName: Windows.Win32.Foundation.PWSTR, dwParamFlags: UInt32, dwCPlusTypeFlag: UInt32, pValue: c_void_p, cchValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def DefineSecurityAttributeSet(self, tkObj: UInt32, rSecAttrs: POINTER(Windows.Win32.System.WinRT.Metadata.COR_SECATTR_head), cSecAttrs: UInt32, pulErrorAttr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def ApplyEditAndContinue(self, pImport: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def TranslateSigWithScope(self, pAssemImport: Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyImport_head, pbHashValue: c_void_p, cbHashValue: UInt32, import_: Windows.Win32.System.WinRT.Metadata.IMetaDataImport_head, pbSigBlob: POINTER(Byte), cbSigBlob: UInt32, pAssemEmit: Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyEmit_head, emit: Windows.Win32.System.WinRT.Metadata.IMetaDataEmit_head, pvTranslatedSig: POINTER(Byte), cbTranslatedSigMax: UInt32, pcbTranslatedSig: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def SetMethodImplFlags(self, md: UInt32, dwImplFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def SetFieldRVA(self, fd: UInt32, ulRVA: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def Merge(self, pImport: Windows.Win32.System.WinRT.Metadata.IMetaDataImport_head, pHostMapToken: Windows.Win32.System.WinRT.Metadata.IMapToken_head, pHandler: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def MergeEnd(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataEmit2(c_void_p):
    extends: Windows.Win32.System.WinRT.Metadata.IMetaDataEmit
    Guid = Guid('f5dd9950-f693-42e6-83-0e-7b-83-3e-81-46-a9')
    @commethod(52)
    def DefineMethodSpec(self, tkParent: UInt32, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmi: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def GetDeltaSaveSize(self, fSave: Windows.Win32.System.WinRT.Metadata.CorSaveSize, pdwSaveSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SaveDelta(self, szFile: Windows.Win32.Foundation.PWSTR, dwSaveFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def SaveDeltaToStream(self, pIStream: Windows.Win32.System.Com.IStream_head, dwSaveFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def SaveDeltaToMemory(self, pbData: c_void_p, cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def DefineGenericParam(self, tk: UInt32, ulParamSeq: UInt32, dwParamFlags: UInt32, szname: Windows.Win32.Foundation.PWSTR, reserved: UInt32, rtkConstraints: POINTER(UInt32), pgp: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def SetGenericParamProps(self, gp: UInt32, dwParamFlags: UInt32, szName: Windows.Win32.Foundation.PWSTR, reserved: UInt32, rtkConstraints: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def ResetENCLog(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataError(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b81ff171-20f3-11d2-8d-cc-00-a0-c9-b0-9c-19')
    @commethod(3)
    def OnError(self, hrError: Windows.Win32.Foundation.HRESULT, token: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataFilter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d0e80dd1-12d4-11d3-b3-9d-00-c0-4f-f8-17-95')
    @commethod(3)
    def UnmarkAll(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MarkToken(self, tk: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsTokenMarked(self, tk: UInt32, pIsMarked: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataImport(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7dac8207-d3ae-4c75-9b-67-92-80-1a-49-7d-44')
    @commethod(3)
    def CloseEnum(self, hEnum: c_void_p) -> Void: ...
    @commethod(4)
    def CountEnum(self, hEnum: c_void_p, pulCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ResetEnum(self, hEnum: c_void_p, ulPos: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumTypeDefs(self, phEnum: POINTER(c_void_p), rTypeDefs: POINTER(UInt32), cMax: UInt32, pcTypeDefs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumInterfaceImpls(self, phEnum: POINTER(c_void_p), td: UInt32, rImpls: POINTER(UInt32), cMax: UInt32, pcImpls: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumTypeRefs(self, phEnum: POINTER(c_void_p), rTypeRefs: POINTER(UInt32), cMax: UInt32, pcTypeRefs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def FindTypeDefByName(self, szTypeDef: Windows.Win32.Foundation.PWSTR, tkEnclosingClass: UInt32, ptd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetScopeProps(self, szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), pmvid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetModuleFromScope(self, pmd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetTypeDefProps(self, td: UInt32, szTypeDef: Windows.Win32.Foundation.PWSTR, cchTypeDef: UInt32, pchTypeDef: POINTER(UInt32), pdwTypeDefFlags: POINTER(UInt32), ptkExtends: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInterfaceImplProps(self, iiImpl: UInt32, pClass: POINTER(UInt32), ptkIface: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTypeRefProps(self, tr: UInt32, ptkResolutionScope: POINTER(UInt32), szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ResolveTypeRef(self, tr: UInt32, riid: POINTER(Guid), ppIScope: POINTER(Windows.Win32.System.Com.IUnknown_head), ptd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EnumMembers(self, phEnum: POINTER(c_void_p), cl: UInt32, rMembers: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnumMembersWithName(self, phEnum: POINTER(c_void_p), cl: UInt32, szName: Windows.Win32.Foundation.PWSTR, rMembers: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumMethods(self, phEnum: POINTER(c_void_p), cl: UInt32, rMethods: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EnumMethodsWithName(self, phEnum: POINTER(c_void_p), cl: UInt32, szName: Windows.Win32.Foundation.PWSTR, rMethods: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def EnumFields(self, phEnum: POINTER(c_void_p), cl: UInt32, rFields: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EnumFieldsWithName(self, phEnum: POINTER(c_void_p), cl: UInt32, szName: Windows.Win32.Foundation.PWSTR, rFields: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def EnumParams(self, phEnum: POINTER(c_void_p), mb: UInt32, rParams: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def EnumMemberRefs(self, phEnum: POINTER(c_void_p), tkParent: UInt32, rMemberRefs: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def EnumMethodImpls(self, phEnum: POINTER(c_void_p), td: UInt32, rMethodBody: POINTER(UInt32), rMethodDecl: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def EnumPermissionSets(self, phEnum: POINTER(c_void_p), tk: UInt32, dwActions: UInt32, rPermission: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def FindMember(self, td: UInt32, szName: Windows.Win32.Foundation.PWSTR, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmb: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def FindMethod(self, td: UInt32, szName: Windows.Win32.Foundation.PWSTR, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmb: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def FindField(self, td: UInt32, szName: Windows.Win32.Foundation.PWSTR, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmb: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def FindMemberRef(self, td: UInt32, szName: Windows.Win32.Foundation.PWSTR, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetMethodProps(self, mb: UInt32, pClass: POINTER(UInt32), szMethod: Windows.Win32.Foundation.PWSTR, cchMethod: UInt32, pchMethod: POINTER(UInt32), pdwAttr: POINTER(UInt32), ppvSigBlob: POINTER(POINTER(Byte)), pcbSigBlob: POINTER(UInt32), pulCodeRVA: POINTER(UInt32), pdwImplFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetMemberRefProps(self, mr: UInt32, ptk: POINTER(UInt32), szMember: Windows.Win32.Foundation.PWSTR, cchMember: UInt32, pchMember: POINTER(UInt32), ppvSigBlob: POINTER(POINTER(Byte)), pbSig: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def EnumProperties(self, phEnum: POINTER(c_void_p), td: UInt32, rProperties: POINTER(UInt32), cMax: UInt32, pcProperties: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def EnumEvents(self, phEnum: POINTER(c_void_p), td: UInt32, rEvents: POINTER(UInt32), cMax: UInt32, pcEvents: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetEventProps(self, ev: UInt32, pClass: POINTER(UInt32), szEvent: Windows.Win32.Foundation.PWSTR, cchEvent: UInt32, pchEvent: POINTER(UInt32), pdwEventFlags: POINTER(UInt32), ptkEventType: POINTER(UInt32), pmdAddOn: POINTER(UInt32), pmdRemoveOn: POINTER(UInt32), pmdFire: POINTER(UInt32), rmdOtherMethod: POINTER(UInt32), cMax: UInt32, pcOtherMethod: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def EnumMethodSemantics(self, phEnum: POINTER(c_void_p), mb: UInt32, rEventProp: POINTER(UInt32), cMax: UInt32, pcEventProp: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetMethodSemantics(self, mb: UInt32, tkEventProp: UInt32, pdwSemanticsFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetClassLayout(self, td: UInt32, pdwPackSize: POINTER(UInt32), rFieldOffset: POINTER(Windows.Win32.System.WinRT.Metadata.COR_FIELD_OFFSET_head), cMax: UInt32, pcFieldOffset: POINTER(UInt32), pulClassSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetFieldMarshal(self, tk: UInt32, ppvNativeType: POINTER(POINTER(Byte)), pcbNativeType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetRVA(self, tk: UInt32, pulCodeRVA: POINTER(UInt32), pdwImplFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetPermissionSetProps(self, pm: UInt32, pdwAction: POINTER(UInt32), ppvPermission: POINTER(c_void_p), pcbPermission: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetSigFromToken(self, mdSig: UInt32, ppvSig: POINTER(POINTER(Byte)), pcbSig: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetModuleRefProps(self, mur: UInt32, szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def EnumModuleRefs(self, phEnum: POINTER(c_void_p), rModuleRefs: POINTER(UInt32), cmax: UInt32, pcModuleRefs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetTypeSpecFromToken(self, typespec: UInt32, ppvSig: POINTER(POINTER(Byte)), pcbSig: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def GetNameFromToken(self, tk: UInt32, pszUtf8NamePtr: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def EnumUnresolvedMethods(self, phEnum: POINTER(c_void_p), rMethods: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def GetUserString(self, stk: UInt32, szString: Windows.Win32.Foundation.PWSTR, cchString: UInt32, pchString: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetPinvokeMap(self, tk: UInt32, pdwMappingFlags: POINTER(UInt32), szImportName: Windows.Win32.Foundation.PWSTR, cchImportName: UInt32, pchImportName: POINTER(UInt32), pmrImportDLL: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def EnumSignatures(self, phEnum: POINTER(c_void_p), rSignatures: POINTER(UInt32), cmax: UInt32, pcSignatures: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def EnumTypeSpecs(self, phEnum: POINTER(c_void_p), rTypeSpecs: POINTER(UInt32), cmax: UInt32, pcTypeSpecs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def EnumUserStrings(self, phEnum: POINTER(c_void_p), rStrings: POINTER(UInt32), cmax: UInt32, pcStrings: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def GetParamForMethodIndex(self, md: UInt32, ulParamSeq: UInt32, ppd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def EnumCustomAttributes(self, phEnum: POINTER(c_void_p), tk: UInt32, tkType: UInt32, rCustomAttributes: POINTER(UInt32), cMax: UInt32, pcCustomAttributes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def GetCustomAttributeProps(self, cv: UInt32, ptkObj: POINTER(UInt32), ptkType: POINTER(UInt32), ppBlob: POINTER(c_void_p), pcbSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def FindTypeRef(self, tkResolutionScope: UInt32, szName: Windows.Win32.Foundation.PWSTR, ptr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def GetMemberProps(self, mb: UInt32, pClass: POINTER(UInt32), szMember: Windows.Win32.Foundation.PWSTR, cchMember: UInt32, pchMember: POINTER(UInt32), pdwAttr: POINTER(UInt32), ppvSigBlob: POINTER(POINTER(Byte)), pcbSigBlob: POINTER(UInt32), pulCodeRVA: POINTER(UInt32), pdwImplFlags: POINTER(UInt32), pdwCPlusTypeFlag: POINTER(UInt32), ppValue: POINTER(c_void_p), pcchValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def GetFieldProps(self, mb: UInt32, pClass: POINTER(UInt32), szField: Windows.Win32.Foundation.PWSTR, cchField: UInt32, pchField: POINTER(UInt32), pdwAttr: POINTER(UInt32), ppvSigBlob: POINTER(POINTER(Byte)), pcbSigBlob: POINTER(UInt32), pdwCPlusTypeFlag: POINTER(UInt32), ppValue: POINTER(c_void_p), pcchValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def GetPropertyProps(self, prop: UInt32, pClass: POINTER(UInt32), szProperty: Windows.Win32.Foundation.PWSTR, cchProperty: UInt32, pchProperty: POINTER(UInt32), pdwPropFlags: POINTER(UInt32), ppvSig: POINTER(POINTER(Byte)), pbSig: POINTER(UInt32), pdwCPlusTypeFlag: POINTER(UInt32), ppDefaultValue: POINTER(c_void_p), pcchDefaultValue: POINTER(UInt32), pmdSetter: POINTER(UInt32), pmdGetter: POINTER(UInt32), rmdOtherMethod: POINTER(UInt32), cMax: UInt32, pcOtherMethod: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def GetParamProps(self, tk: UInt32, pmd: POINTER(UInt32), pulSequence: POINTER(UInt32), szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), pdwAttr: POINTER(UInt32), pdwCPlusTypeFlag: POINTER(UInt32), ppValue: POINTER(c_void_p), pcchValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def GetCustomAttributeByName(self, tkObj: UInt32, szName: Windows.Win32.Foundation.PWSTR, ppData: POINTER(c_void_p), pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def IsValidToken(self, tk: UInt32) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(62)
    def GetNestedClassProps(self, tdNestedClass: UInt32, ptdEnclosingClass: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def GetNativeCallConvFromSig(self, pvSig: c_void_p, cbSig: UInt32, pCallConv: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def IsGlobal(self, pd: UInt32, pbGlobal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataImport2(c_void_p):
    extends: Windows.Win32.System.WinRT.Metadata.IMetaDataImport
    Guid = Guid('fce5efa0-8bba-4f8e-a0-36-8f-20-22-b0-84-66')
    @commethod(65)
    def EnumGenericParams(self, phEnum: POINTER(c_void_p), tk: UInt32, rGenericParams: POINTER(UInt32), cMax: UInt32, pcGenericParams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def GetGenericParamProps(self, gp: UInt32, pulParamSeq: POINTER(UInt32), pdwParamFlags: POINTER(UInt32), ptOwner: POINTER(UInt32), reserved: POINTER(UInt32), wzname: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def GetMethodSpecProps(self, mi: UInt32, tkParent: POINTER(UInt32), ppvSigBlob: POINTER(POINTER(Byte)), pcbSigBlob: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def EnumGenericParamConstraints(self, phEnum: POINTER(c_void_p), tk: UInt32, rGenericParamConstraints: POINTER(UInt32), cMax: UInt32, pcGenericParamConstraints: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetGenericParamConstraintProps(self, gpc: UInt32, ptGenericParam: POINTER(UInt32), ptkConstraintType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def GetPEKind(self, pdwPEKind: POINTER(UInt32), pdwMAchine: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def GetVersionString(self, pwzBuf: Windows.Win32.Foundation.PWSTR, ccBufSize: UInt32, pccBufSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def EnumMethodSpecs(self, phEnum: POINTER(c_void_p), tk: UInt32, rMethodSpecs: POINTER(UInt32), cMax: UInt32, pcMethodSpecs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7998ea64-7f95-48b8-86-fc-17-ca-f4-8b-f5-cb')
    @commethod(3)
    def GetFileMapping(self, ppvData: POINTER(c_void_p), pcbData: POINTER(UInt64), pdwMappingType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataTables(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d8f579ab-402d-4b8e-82-d9-5d-63-b1-06-5c-68')
    @commethod(3)
    def GetStringHeapSize(self, pcbStrings: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBlobHeapSize(self, pcbBlobs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetGuidHeapSize(self, pcbGuids: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUserStringHeapSize(self, pcbBlobs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNumTables(self, pcTables: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableIndex(self, token: UInt32, pixTbl: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableInfo(self, ixTbl: UInt32, pcbRow: POINTER(UInt32), pcRows: POINTER(UInt32), pcCols: POINTER(UInt32), piKey: POINTER(UInt32), ppName: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetColumnInfo(self, ixTbl: UInt32, ixCol: UInt32, poCol: POINTER(UInt32), pcbCol: POINTER(UInt32), pType: POINTER(UInt32), ppName: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCodedTokenInfo(self, ixCdTkn: UInt32, pcTokens: POINTER(UInt32), ppTokens: POINTER(POINTER(UInt32)), ppName: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRow(self, ixTbl: UInt32, rid: UInt32, ppRow: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetColumn(self, ixTbl: UInt32, ixCol: UInt32, rid: UInt32, pVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetString(self, ixString: UInt32, ppString: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetBlob(self, ixBlob: UInt32, pcbData: POINTER(UInt32), ppData: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetGuid(self, ixGuid: UInt32, ppGUID: POINTER(POINTER(Guid))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetUserString(self, ixUserString: UInt32, pcbData: POINTER(UInt32), ppData: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetNextString(self, ixString: UInt32, pNext: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetNextBlob(self, ixBlob: UInt32, pNext: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetNextGuid(self, ixGuid: UInt32, pNext: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetNextUserString(self, ixUserString: UInt32, pNext: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataTables2(c_void_p):
    extends: Windows.Win32.System.WinRT.Metadata.IMetaDataTables
    Guid = Guid('badb5f70-58da-43a9-a1-c6-d7-48-19-f1-9b-15')
    @commethod(22)
    def GetMetaDataStorage(self, ppvMd: POINTER(c_void_p), pcbMd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMetaDataStreamInfo(self, ix: UInt32, ppchName: POINTER(POINTER(SByte)), ppv: POINTER(c_void_p), pcb: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataValidate(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4709c9c6-81ff-11d3-9f-c7-00-c0-4f-79-a0-a3')
    @commethod(3)
    def ValidatorInit(self, dwModuleType: UInt32, pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ValidateMetaData(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMetaDataWinMDImport(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('969ea0c5-964e-411b-a8-07-b0-f3-c2-df-cb-d4')
    @commethod(3)
    def GetUntransformedTypeRefProps(self, tr: UInt32, ptkResolutionScope: POINTER(UInt32), szName: Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRoMetaDataLocator(c_void_p):
    extends: None
    @commethod(0)
    def Locate(self, nameElement: Windows.Win32.Foundation.PWSTR, metaDataDestination: Windows.Win32.System.WinRT.Metadata.IRoSimpleMetaDataBuilder_head) -> Windows.Win32.Foundation.HRESULT: ...
class IRoSimpleMetaDataBuilder(c_void_p):
    extends: None
    @commethod(0)
    def SetWinRtInterface(self, iid: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(1)
    def SetDelegate(self, iid: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(2)
    def SetInterfaceGroupSimpleDefault(self, name: Windows.Win32.Foundation.PWSTR, defaultInterfaceName: Windows.Win32.Foundation.PWSTR, defaultInterfaceIID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(3)
    def SetInterfaceGroupParameterizedDefault(self, name: Windows.Win32.Foundation.PWSTR, elementCount: UInt32, defaultInterfaceNameElements: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetRuntimeClassSimpleDefault(self, name: Windows.Win32.Foundation.PWSTR, defaultInterfaceName: Windows.Win32.Foundation.PWSTR, defaultInterfaceIID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetRuntimeClassParameterizedDefault(self, name: Windows.Win32.Foundation.PWSTR, elementCount: UInt32, defaultInterfaceNameElements: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetStruct(self, name: Windows.Win32.Foundation.PWSTR, numFields: UInt32, fieldTypeNames: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetEnum(self, name: Windows.Win32.Foundation.PWSTR, baseType: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetParameterizedInterface(self, piid: Guid, numArgs: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetParameterizedDelegate(self, piid: Guid, numArgs: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
LoadHintEnum = Int32
LoadHintEnum_LoadDefault: LoadHintEnum = 0
LoadHintEnum_LoadAlways: LoadHintEnum = 1
LoadHintEnum_LoadSometimes: LoadHintEnum = 2
LoadHintEnum_LoadNever: LoadHintEnum = 3
MergeFlags = Int32
MergeFlags_MergeFlagsNone: MergeFlags = 0
MergeFlags_MergeManifest: MergeFlags = 1
MergeFlags_DropMemberRefCAs: MergeFlags = 2
MergeFlags_NoDupCheck: MergeFlags = 4
MergeFlags_MergeExportedTypes: MergeFlags = 8
NGenHintEnum = Int32
NGenHintEnum_NGenDefault: NGenHintEnum = 0
NGenHintEnum_NGenEager: NGenHintEnum = 1
NGenHintEnum_NGenLazy: NGenHintEnum = 2
NGenHintEnum_NGenNever: NGenHintEnum = 3
NativeTypeArrayFlags = Int32
NativeTypeArrayFlags_ntaSizeParamIndexSpecified: NativeTypeArrayFlags = 1
NativeTypeArrayFlags_ntaReserved: NativeTypeArrayFlags = 65534
class OSINFO(EasyCastStructure):
    dwOSPlatformId: UInt32
    dwOSMajorVersion: UInt32
    dwOSMinorVersion: UInt32
ReplacesGeneralNumericDefines = Int32
IMAGE_DIRECTORY_ENTRY_COMHEADER: ReplacesGeneralNumericDefines = 14
make_head(_module, 'ASSEMBLYMETADATA')
make_head(_module, 'COR_FIELD_OFFSET')
make_head(_module, 'COR_NATIVE_LINK')
make_head(_module, 'COR_SECATTR')
make_head(_module, 'CVStruct')
make_head(_module, 'CeeSectionRelocExtra')
make_head(_module, 'ICeeGen')
make_head(_module, 'IHostFilter')
make_head(_module, 'IMAGE_COR_ILMETHOD')
make_head(_module, 'IMAGE_COR_ILMETHOD_FAT')
make_head(_module, 'IMAGE_COR_ILMETHOD_SECT_EH')
make_head(_module, 'IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT')
if ARCH in 'X64,ARM64':
    make_head(_module, 'IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL')
if ARCH in 'X86':
    make_head(_module, 'IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL')
make_head(_module, 'IMAGE_COR_ILMETHOD_SECT_EH_FAT')
make_head(_module, 'IMAGE_COR_ILMETHOD_SECT_EH_SMALL')
make_head(_module, 'IMAGE_COR_ILMETHOD_SECT_FAT')
make_head(_module, 'IMAGE_COR_ILMETHOD_SECT_SMALL')
make_head(_module, 'IMAGE_COR_ILMETHOD_TINY')
make_head(_module, 'IMAGE_COR_VTABLEFIXUP')
make_head(_module, 'IMapToken')
make_head(_module, 'IMetaDataAssemblyEmit')
make_head(_module, 'IMetaDataAssemblyImport')
make_head(_module, 'IMetaDataDispenser')
make_head(_module, 'IMetaDataDispenserEx')
make_head(_module, 'IMetaDataEmit')
make_head(_module, 'IMetaDataEmit2')
make_head(_module, 'IMetaDataError')
make_head(_module, 'IMetaDataFilter')
make_head(_module, 'IMetaDataImport')
make_head(_module, 'IMetaDataImport2')
make_head(_module, 'IMetaDataInfo')
make_head(_module, 'IMetaDataTables')
make_head(_module, 'IMetaDataTables2')
make_head(_module, 'IMetaDataValidate')
make_head(_module, 'IMetaDataWinMDImport')
make_head(_module, 'IRoMetaDataLocator')
make_head(_module, 'IRoSimpleMetaDataBuilder')
make_head(_module, 'OSINFO')
