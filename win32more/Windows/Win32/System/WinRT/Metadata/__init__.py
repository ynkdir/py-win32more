from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.Metadata
class ASSEMBLYMETADATA(Structure):
    usMajorVersion: UInt16
    usMinorVersion: UInt16
    usBuildNumber: UInt16
    usRevisionNumber: UInt16
    szLocale: win32more.Windows.Win32.Foundation.PWSTR
    cbLocale: UInt32
    rProcessor: POINTER(UInt32)
    ulProcessor: UInt32
    rOS: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.OSINFO)
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
COR_E_AMBIGUOUSMATCH: win32more.Windows.Win32.Foundation.HRESULT = -2147475171
COR_E_TARGETPARAMCOUNT: win32more.Windows.Win32.Foundation.HRESULT = -2147352562
COR_E_DIVIDEBYZERO: win32more.Windows.Win32.Foundation.HRESULT = -2147352558
COR_E_BADIMAGEFORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147024885
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
LIBID_ComPlusRuntime: Guid = Guid('{bed7f4ea-1a96-11d2-8f08-00a0c9a6186d}')
GUID_ExportedFromComPlus: Guid = Guid('{90883f05-3d28-11d2-8f17-00a0c9a6186d}')
GUID_ManagedName: Guid = Guid('{0f21f359-ab84-41e8-9a78-36d110e6d2f9}')
GUID_Function2Getter: Guid = Guid('{54fc8f55-38de-4703-9c4e-250351302b1c}')
CLSID_CorMetaDataDispenserRuntime: Guid = Guid('{1ec2de53-75cc-11d2-9775-00a0c9b4d50c}')
GUID_DispIdOverride: Guid = Guid('{cd2bc5c9-f452-4326-b714-f9c539d4da58}')
GUID_ForceIEnumerable: Guid = Guid('{b64784eb-d8d4-4d9b-9acd-0e30806426f7}')
GUID_PropGetCA: Guid = Guid('{2941ff83-88d8-4f73-b6a9-bdf8712d000d}')
GUID_PropPutCA: Guid = Guid('{29533527-3683-4364-abc0-db1add822fa2}')
CLSID_CLR_v1_MetaData: Guid = Guid('{005023ca-72b1-11d3-9fc4-00c04f79a0a3}')
CLSID_CLR_v2_MetaData: Guid = Guid('{efea471a-44fd-4862-9292-0c58d46e1f3a}')
MetaDataCheckDuplicatesFor: Guid = Guid('{30fe7be8-d7d9-11d2-9f80-00c04f79a0a3}')
MetaDataRefToDefCheck: Guid = Guid('{de3856f8-d7d9-11d2-9f80-00c04f79a0a3}')
MetaDataNotificationForTokenMovement: Guid = Guid('{e5d71a4c-d7da-11d2-9f80-00c04f79a0a3}')
MetaDataSetUpdate: Guid = Guid('{2eee315c-d7db-11d2-9f80-00c04f79a0a3}')
MetaDataImportOption: Guid = Guid('{79700f36-4aac-11d3-84c3-009027868cb1}')
MetaDataThreadSafetyOptions: Guid = Guid('{f7559806-f266-42ea-8c63-0adb45e8b234}')
MetaDataErrorIfEmitOutOfOrder: Guid = Guid('{1547872d-dc03-11d2-9420-0000f8083460}')
MetaDataGenerateTCEAdapters: Guid = Guid('{dcc9de90-4151-11d3-88d6-00902754c43a}')
MetaDataTypeLibImportNamespace: Guid = Guid('{f17ff889-5a63-11d3-9ff2-00c04ff7431a}')
MetaDataLinkerOptions: Guid = Guid('{47e099b6-ae7c-4797-8317-b48aa645b8f9}')
MetaDataRuntimeVersion: Guid = Guid('{47e099b7-ae7c-4797-8317-b48aa645b8f9}')
MetaDataMergerOptions: Guid = Guid('{132d3a6e-b35d-464e-951a-42efb9fb6601}')
MetaDataPreserveLocalRefs: Guid = Guid('{a55c0354-e91b-468b-8648-7cc31035d533}')
DESCR_GROUP_METHODDEF: Int32 = 0
DESCR_GROUP_METHODIMPL: Int32 = 1
CLSID_Cor: Guid = Guid('{bee00010-ee77-11d0-a015-00c04fbbb884}')
CLSID_CorMetaDataDispenser: Guid = Guid('{e5cb7a31-7512-11d2-89ce-0080c792e5d8}')
CLSID_CorMetaDataDispenserReg: Guid = Guid('{435755ff-7397-11d2-9771-00a0c9b4d50c}')
CLSID_CorMetaDataReg: Guid = Guid('{87f3a1f5-7397-11d2-9771-00a0c9b4d50c}')
SIGN_MASK_ONEBYTE: Int32 = -64
SIGN_MASK_TWOBYTE: Int32 = -8192
SIGN_MASK_FOURBYTE: Int32 = -268435456
@winfunctype('RoMetadata.dll')
def MetaDataGetDispenser(rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-0.dll')
def RoGetMetaDataFile(name: win32more.Windows.Win32.System.WinRT.HSTRING, metaDataDispenser: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataDispenserEx, metaDataFilePath: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING), metaDataImport: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataImport2), typeDefToken: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-0.dll')
def RoParseTypeName(typeName: win32more.Windows.Win32.System.WinRT.HSTRING, partsCount: POINTER(UInt32), typeNameParts: POINTER(POINTER(win32more.Windows.Win32.System.WinRT.HSTRING))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-0.dll')
def RoResolveNamespace(name: win32more.Windows.Win32.System.WinRT.HSTRING, windowsMetaDataDir: win32more.Windows.Win32.System.WinRT.HSTRING, packageGraphDirsCount: UInt32, packageGraphDirs: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING), metaDataFilePathsCount: POINTER(UInt32), metaDataFilePaths: POINTER(POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)), subNamespacesCount: POINTER(UInt32), subNamespaces: POINTER(POINTER(win32more.Windows.Win32.System.WinRT.HSTRING))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-1.dll')
def RoIsApiContractPresent(name: win32more.Windows.Win32.Foundation.PWSTR, majorVersion: UInt16, minorVersion: UInt16, present: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-1.dll')
def RoIsApiContractMajorVersionPresent(name: win32more.Windows.Win32.Foundation.PWSTR, majorVersion: UInt16, present: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-1.dll')
def RoCreateNonAgilePropertySet(ppPropertySet: POINTER(win32more.Windows.Foundation.Collections.IPropertySet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-ro-typeresolution-l1-1-1.dll')
def RoCreatePropertySetSerializer(ppPropertySetSerializer: POINTER(win32more.Windows.Storage.Streams.IPropertySetSerializer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll')
def RoGetParameterizedTypeInstanceIID(nameElementCount: UInt32, nameElements: POINTER(win32more.Windows.Win32.Foundation.PWSTR), metaDataLocator: win32more.Windows.Win32.System.WinRT.Metadata.IRoMetaDataLocator, iid: POINTER(Guid), pExtra: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.ROPARAMIIDHANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll')
def RoFreeParameterizedTypeExtra(extra: win32more.Windows.Win32.System.WinRT.Metadata.ROPARAMIIDHANDLE) -> Void: ...
@winfunctype('api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll')
def RoParameterizedTypeExtraGetTypeSignature(extra: win32more.Windows.Win32.System.WinRT.Metadata.ROPARAMIIDHANDLE) -> win32more.Windows.Win32.Foundation.PSTR: ...
COINITICOR = Int32
COINITCOR_DEFAULT: win32more.Windows.Win32.System.WinRT.Metadata.COINITICOR = 0
COINITIEE = Int32
COINITEE_DEFAULT: win32more.Windows.Win32.System.WinRT.Metadata.COINITIEE = 0
COINITEE_DLL: win32more.Windows.Win32.System.WinRT.Metadata.COINITIEE = 1
COINITEE_MAIN: win32more.Windows.Win32.System.WinRT.Metadata.COINITIEE = 2
class COR_FIELD_OFFSET(Structure):
    ridOfField: UInt32
    ulOffset: UInt32
class COR_NATIVE_LINK(Structure):
    m_linkType: Byte
    m_flags: Byte
    m_entryPoint: UInt32
    _pack_ = 1
class COR_SECATTR(Structure):
    tkCtor: UInt32
    pCustomAttribute: VoidPtr
    cbCustomAttribute: UInt32
COUNINITIEE = Int32
COUNINITEE_DEFAULT: win32more.Windows.Win32.System.WinRT.Metadata.COUNINITIEE = 0
COUNINITEE_DLL: win32more.Windows.Win32.System.WinRT.Metadata.COUNINITIEE = 1
class CVStruct(Structure):
    Major: Int16
    Minor: Int16
    Sub: Int16
    Build: Int16
CeeSectionAttr = Int64
sdNone: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionAttr = 0
sdReadOnly: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionAttr = 1073741888
sdReadWrite: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionAttr = 3221225536
sdExecute: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionAttr = 1610612768
class CeeSectionRelocExtra(Union):
    highAdj: UInt16
CeeSectionRelocType = Int32
srRelocAbsolute: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 0
srRelocHighLow: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 3
srRelocHighAdj: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 4
srRelocMapToken: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 5
srRelocRelative: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 6
srRelocFilePos: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 7
srRelocCodeRelative: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 8
srRelocIA64Imm64: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 9
srRelocDir64: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 10
srRelocIA64PcRel25: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 11
srRelocIA64PcRel64: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 12
srRelocAbsoluteTagged: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 13
srRelocSentinel: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 14
srNoBaseReloc: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 16384
srRelocPtr: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 32768
srRelocAbsolutePtr: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 32768
srRelocHighLowPtr: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 32771
srRelocRelativePtr: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 32774
srRelocIA64Imm64Ptr: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 32777
srRelocDir64Ptr: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType = 32778
CompilationRelaxationsEnum = Int32
CompilationRelaxations_NoStringInterning: win32more.Windows.Win32.System.WinRT.Metadata.CompilationRelaxationsEnum = 8
CorArgType = Int32
IMAGE_CEE_CS_END: win32more.Windows.Win32.System.WinRT.Metadata.CorArgType = 0
IMAGE_CEE_CS_VOID: win32more.Windows.Win32.System.WinRT.Metadata.CorArgType = 1
IMAGE_CEE_CS_I4: win32more.Windows.Win32.System.WinRT.Metadata.CorArgType = 2
IMAGE_CEE_CS_I8: win32more.Windows.Win32.System.WinRT.Metadata.CorArgType = 3
IMAGE_CEE_CS_R4: win32more.Windows.Win32.System.WinRT.Metadata.CorArgType = 4
IMAGE_CEE_CS_R8: win32more.Windows.Win32.System.WinRT.Metadata.CorArgType = 5
IMAGE_CEE_CS_PTR: win32more.Windows.Win32.System.WinRT.Metadata.CorArgType = 6
IMAGE_CEE_CS_OBJECT: win32more.Windows.Win32.System.WinRT.Metadata.CorArgType = 7
IMAGE_CEE_CS_STRUCT4: win32more.Windows.Win32.System.WinRT.Metadata.CorArgType = 8
IMAGE_CEE_CS_STRUCT32: win32more.Windows.Win32.System.WinRT.Metadata.CorArgType = 9
IMAGE_CEE_CS_BYVALUE: win32more.Windows.Win32.System.WinRT.Metadata.CorArgType = 10
CorAssemblyFlags = Int32
afPublicKey: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 1
afPA_None: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 0
afPA_MSIL: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 16
afPA_x86: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 32
afPA_IA64: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 48
afPA_AMD64: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 64
afPA_ARM: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 80
afPA_NoPlatform: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 112
afPA_Specified: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 128
afPA_Mask: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 112
afPA_FullMask: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 240
afPA_Shift: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 4
afEnableJITcompileTracking: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 32768
afDisableJITcompileOptimizer: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 16384
afRetargetable: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 256
afContentType_Default: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 0
afContentType_WindowsRuntime: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 512
afContentType_Mask: win32more.Windows.Win32.System.WinRT.Metadata.CorAssemblyFlags = 3584
CorAttributeTargets = Int32
catAssembly: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 1
catModule: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 2
catClass: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 4
catStruct: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 8
catEnum: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 16
catConstructor: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 32
catMethod: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 64
catProperty: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 128
catField: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 256
catEvent: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 512
catInterface: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 1024
catParameter: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 2048
catDelegate: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 4096
catGenericParameter: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 16384
catAll: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 24575
catClassMembers: win32more.Windows.Win32.System.WinRT.Metadata.CorAttributeTargets = 6140
CorCallingConvention = Int32
IMAGE_CEE_CS_CALLCONV_DEFAULT: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 0
IMAGE_CEE_CS_CALLCONV_VARARG: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 5
IMAGE_CEE_CS_CALLCONV_FIELD: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 6
IMAGE_CEE_CS_CALLCONV_LOCAL_SIG: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 7
IMAGE_CEE_CS_CALLCONV_PROPERTY: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 8
IMAGE_CEE_CS_CALLCONV_UNMGD: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 9
IMAGE_CEE_CS_CALLCONV_GENERICINST: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 10
IMAGE_CEE_CS_CALLCONV_NATIVEVARARG: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 11
IMAGE_CEE_CS_CALLCONV_MAX: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 12
IMAGE_CEE_CS_CALLCONV_MASK: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 15
IMAGE_CEE_CS_CALLCONV_HASTHIS: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 32
IMAGE_CEE_CS_CALLCONV_EXPLICITTHIS: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 64
IMAGE_CEE_CS_CALLCONV_GENERIC: win32more.Windows.Win32.System.WinRT.Metadata.CorCallingConvention = 16
CorCheckDuplicatesFor = Int32
MDDupAll: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = -1
MDDupENC: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = -1
MDNoDupChecks: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 0
MDDupTypeDef: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 1
MDDupInterfaceImpl: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 2
MDDupMethodDef: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 4
MDDupTypeRef: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 8
MDDupMemberRef: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 16
MDDupCustomAttribute: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 32
MDDupParamDef: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 64
MDDupPermission: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 128
MDDupProperty: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 256
MDDupEvent: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 512
MDDupFieldDef: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 1024
MDDupSignature: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 2048
MDDupModuleRef: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 4096
MDDupTypeSpec: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 8192
MDDupImplMap: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 16384
MDDupAssemblyRef: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 32768
MDDupFile: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 65536
MDDupExportedType: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 131072
MDDupManifestResource: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 262144
MDDupGenericParam: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 524288
MDDupMethodSpec: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 1048576
MDDupGenericParamConstraint: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 2097152
MDDupAssembly: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 268435456
MDDupDefault: win32more.Windows.Win32.System.WinRT.Metadata.CorCheckDuplicatesFor = 1058840
CorDeclSecurity = Int32
dclActionMask: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 31
dclActionNil: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 0
dclRequest: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 1
dclDemand: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 2
dclAssert: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 3
dclDeny: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 4
dclPermitOnly: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 5
dclLinktimeCheck: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 6
dclInheritanceCheck: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 7
dclRequestMinimum: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 8
dclRequestOptional: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 9
dclRequestRefuse: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 10
dclPrejitGrant: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 11
dclPrejitDenied: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 12
dclNonCasDemand: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 13
dclNonCasLinkDemand: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 14
dclNonCasInheritance: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 15
dclMaximumValue: win32more.Windows.Win32.System.WinRT.Metadata.CorDeclSecurity = 15
CorElementType = Byte
ELEMENT_TYPE_END: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 0
ELEMENT_TYPE_VOID: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 1
ELEMENT_TYPE_BOOLEAN: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 2
ELEMENT_TYPE_CHAR: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 3
ELEMENT_TYPE_I1: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 4
ELEMENT_TYPE_U1: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 5
ELEMENT_TYPE_I2: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 6
ELEMENT_TYPE_U2: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 7
ELEMENT_TYPE_I4: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 8
ELEMENT_TYPE_U4: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 9
ELEMENT_TYPE_I8: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 10
ELEMENT_TYPE_U8: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 11
ELEMENT_TYPE_R4: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 12
ELEMENT_TYPE_R8: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 13
ELEMENT_TYPE_STRING: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 14
ELEMENT_TYPE_PTR: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 15
ELEMENT_TYPE_BYREF: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 16
ELEMENT_TYPE_VALUETYPE: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 17
ELEMENT_TYPE_CLASS: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 18
ELEMENT_TYPE_VAR: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 19
ELEMENT_TYPE_ARRAY: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 20
ELEMENT_TYPE_GENERICINST: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 21
ELEMENT_TYPE_TYPEDBYREF: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 22
ELEMENT_TYPE_I: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 24
ELEMENT_TYPE_U: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 25
ELEMENT_TYPE_FNPTR: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 27
ELEMENT_TYPE_OBJECT: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 28
ELEMENT_TYPE_SZARRAY: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 29
ELEMENT_TYPE_MVAR: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 30
ELEMENT_TYPE_CMOD_REQD: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 31
ELEMENT_TYPE_CMOD_OPT: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 32
ELEMENT_TYPE_INTERNAL: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 33
ELEMENT_TYPE_MAX: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 34
ELEMENT_TYPE_MODIFIER: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 64
ELEMENT_TYPE_SENTINEL: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 65
ELEMENT_TYPE_PINNED: win32more.Windows.Win32.System.WinRT.Metadata.CorElementType = 69
CorErrorIfEmitOutOfOrder = Int32
MDErrorOutOfOrderDefault: win32more.Windows.Win32.System.WinRT.Metadata.CorErrorIfEmitOutOfOrder = 0
MDErrorOutOfOrderNone: win32more.Windows.Win32.System.WinRT.Metadata.CorErrorIfEmitOutOfOrder = 0
MDErrorOutOfOrderAll: win32more.Windows.Win32.System.WinRT.Metadata.CorErrorIfEmitOutOfOrder = -1
MDMethodOutOfOrder: win32more.Windows.Win32.System.WinRT.Metadata.CorErrorIfEmitOutOfOrder = 1
MDFieldOutOfOrder: win32more.Windows.Win32.System.WinRT.Metadata.CorErrorIfEmitOutOfOrder = 2
MDParamOutOfOrder: win32more.Windows.Win32.System.WinRT.Metadata.CorErrorIfEmitOutOfOrder = 4
MDPropertyOutOfOrder: win32more.Windows.Win32.System.WinRT.Metadata.CorErrorIfEmitOutOfOrder = 8
MDEventOutOfOrder: win32more.Windows.Win32.System.WinRT.Metadata.CorErrorIfEmitOutOfOrder = 16
CorEventAttr = Int32
evSpecialName: win32more.Windows.Win32.System.WinRT.Metadata.CorEventAttr = 512
evReservedMask: win32more.Windows.Win32.System.WinRT.Metadata.CorEventAttr = 1024
evRTSpecialName: win32more.Windows.Win32.System.WinRT.Metadata.CorEventAttr = 1024
CorExceptionFlag = Int32
COR_ILEXCEPTION_CLAUSE_NONE: win32more.Windows.Win32.System.WinRT.Metadata.CorExceptionFlag = 0
COR_ILEXCEPTION_CLAUSE_OFFSETLEN: win32more.Windows.Win32.System.WinRT.Metadata.CorExceptionFlag = 0
COR_ILEXCEPTION_CLAUSE_DEPRECATED: win32more.Windows.Win32.System.WinRT.Metadata.CorExceptionFlag = 0
COR_ILEXCEPTION_CLAUSE_FILTER: win32more.Windows.Win32.System.WinRT.Metadata.CorExceptionFlag = 1
COR_ILEXCEPTION_CLAUSE_FINALLY: win32more.Windows.Win32.System.WinRT.Metadata.CorExceptionFlag = 2
COR_ILEXCEPTION_CLAUSE_FAULT: win32more.Windows.Win32.System.WinRT.Metadata.CorExceptionFlag = 4
COR_ILEXCEPTION_CLAUSE_DUPLICATED: win32more.Windows.Win32.System.WinRT.Metadata.CorExceptionFlag = 8
CorFieldAttr = Int32
fdFieldAccessMask: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 7
fdPrivateScope: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 0
fdPrivate: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 1
fdFamANDAssem: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 2
fdAssembly: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 3
fdFamily: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 4
fdFamORAssem: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 5
fdPublic: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 6
fdStatic: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 16
fdInitOnly: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 32
fdLiteral: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 64
fdNotSerialized: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 128
fdSpecialName: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 512
fdPinvokeImpl: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 8192
fdReservedMask: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 38144
fdRTSpecialName: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 1024
fdHasFieldMarshal: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 4096
fdHasDefault: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 32768
fdHasFieldRVA: win32more.Windows.Win32.System.WinRT.Metadata.CorFieldAttr = 256
CorFileFlags = Int32
ffContainsMetaData: win32more.Windows.Win32.System.WinRT.Metadata.CorFileFlags = 0
ffContainsNoMetaData: win32more.Windows.Win32.System.WinRT.Metadata.CorFileFlags = 1
CorFileMapping = Int32
fmFlat: win32more.Windows.Win32.System.WinRT.Metadata.CorFileMapping = 0
fmExecutableImage: win32more.Windows.Win32.System.WinRT.Metadata.CorFileMapping = 1
CorGenericParamAttr = Int32
gpVarianceMask: win32more.Windows.Win32.System.WinRT.Metadata.CorGenericParamAttr = 3
gpNonVariant: win32more.Windows.Win32.System.WinRT.Metadata.CorGenericParamAttr = 0
gpCovariant: win32more.Windows.Win32.System.WinRT.Metadata.CorGenericParamAttr = 1
gpContravariant: win32more.Windows.Win32.System.WinRT.Metadata.CorGenericParamAttr = 2
gpSpecialConstraintMask: win32more.Windows.Win32.System.WinRT.Metadata.CorGenericParamAttr = 28
gpNoSpecialConstraint: win32more.Windows.Win32.System.WinRT.Metadata.CorGenericParamAttr = 0
gpReferenceTypeConstraint: win32more.Windows.Win32.System.WinRT.Metadata.CorGenericParamAttr = 4
gpNotNullableValueTypeConstraint: win32more.Windows.Win32.System.WinRT.Metadata.CorGenericParamAttr = 8
gpDefaultConstructorConstraint: win32more.Windows.Win32.System.WinRT.Metadata.CorGenericParamAttr = 16
CorILMethodFlags = Int32
CorILMethod_InitLocals: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodFlags = 16
CorILMethod_MoreSects: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodFlags = 8
CorILMethod_CompressedIL: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodFlags = 64
CorILMethod_FormatShift: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodFlags = 3
CorILMethod_FormatMask: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodFlags = 7
CorILMethod_TinyFormat: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodFlags = 2
CorILMethod_SmallFormat: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodFlags = 0
CorILMethod_FatFormat: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodFlags = 3
CorILMethod_TinyFormat1: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodFlags = 6
CorILMethodSect = Int32
CorILMethod_Sect_Reserved: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodSect = 0
CorILMethod_Sect_EHTable: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodSect = 1
CorILMethod_Sect_OptILTable: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodSect = 2
CorILMethod_Sect_KindMask: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodSect = 63
CorILMethod_Sect_FatFormat: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodSect = 64
CorILMethod_Sect_MoreSects: win32more.Windows.Win32.System.WinRT.Metadata.CorILMethodSect = 128
CorImportOptions = Int32
MDImportOptionDefault: win32more.Windows.Win32.System.WinRT.Metadata.CorImportOptions = 0
MDImportOptionAll: win32more.Windows.Win32.System.WinRT.Metadata.CorImportOptions = -1
MDImportOptionAllTypeDefs: win32more.Windows.Win32.System.WinRT.Metadata.CorImportOptions = 1
MDImportOptionAllMethodDefs: win32more.Windows.Win32.System.WinRT.Metadata.CorImportOptions = 2
MDImportOptionAllFieldDefs: win32more.Windows.Win32.System.WinRT.Metadata.CorImportOptions = 4
MDImportOptionAllProperties: win32more.Windows.Win32.System.WinRT.Metadata.CorImportOptions = 8
MDImportOptionAllEvents: win32more.Windows.Win32.System.WinRT.Metadata.CorImportOptions = 16
MDImportOptionAllCustomAttributes: win32more.Windows.Win32.System.WinRT.Metadata.CorImportOptions = 32
MDImportOptionAllExportedTypes: win32more.Windows.Win32.System.WinRT.Metadata.CorImportOptions = 64
CorLinkerOptions = Int32
MDAssembly: win32more.Windows.Win32.System.WinRT.Metadata.CorLinkerOptions = 0
MDNetModule: win32more.Windows.Win32.System.WinRT.Metadata.CorLinkerOptions = 1
CorLocalRefPreservation = Int32
MDPreserveLocalRefsNone: win32more.Windows.Win32.System.WinRT.Metadata.CorLocalRefPreservation = 0
MDPreserveLocalTypeRef: win32more.Windows.Win32.System.WinRT.Metadata.CorLocalRefPreservation = 1
MDPreserveLocalMemberRef: win32more.Windows.Win32.System.WinRT.Metadata.CorLocalRefPreservation = 2
CorManifestResourceFlags = Int32
mrVisibilityMask: win32more.Windows.Win32.System.WinRT.Metadata.CorManifestResourceFlags = 7
mrPublic: win32more.Windows.Win32.System.WinRT.Metadata.CorManifestResourceFlags = 1
mrPrivate: win32more.Windows.Win32.System.WinRT.Metadata.CorManifestResourceFlags = 2
CorMethodAttr = Int32
mdMemberAccessMask: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 7
mdPrivateScope: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 0
mdPrivate: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 1
mdFamANDAssem: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 2
mdAssem: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 3
mdFamily: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 4
mdFamORAssem: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 5
mdPublic: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 6
mdStatic: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 16
mdFinal: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 32
mdVirtual: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 64
mdHideBySig: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 128
mdVtableLayoutMask: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 256
mdReuseSlot: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 0
mdNewSlot: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 256
mdCheckAccessOnOverride: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 512
mdAbstract: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 1024
mdSpecialName: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 2048
mdPinvokeImpl: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 8192
mdUnmanagedExport: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 8
mdReservedMask: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 53248
mdRTSpecialName: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 4096
mdHasSecurity: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 16384
mdRequireSecObject: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodAttr = 32768
CorMethodImpl = Int32
miCodeTypeMask: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 3
miIL: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 0
miNative: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 1
miOPTIL: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 2
miRuntime: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 3
miManagedMask: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 4
miUnmanaged: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 4
miManaged: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 0
miForwardRef: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 16
miPreserveSig: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 128
miInternalCall: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 4096
miSynchronized: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 32
miNoInlining: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 8
miAggressiveInlining: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 256
miNoOptimization: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 64
miSecurityMitigations: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 1024
miUserMask: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 5628
miMaxMethodImplVal: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodImpl = 65535
CorMethodSemanticsAttr = Int32
msSetter: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodSemanticsAttr = 1
msGetter: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodSemanticsAttr = 2
msOther: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodSemanticsAttr = 4
msAddOn: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodSemanticsAttr = 8
msRemoveOn: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodSemanticsAttr = 16
msFire: win32more.Windows.Win32.System.WinRT.Metadata.CorMethodSemanticsAttr = 32
CorNativeLinkFlags = Int32
nlfNone: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeLinkFlags = 0
nlfLastError: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeLinkFlags = 1
nlfNoMangle: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeLinkFlags = 2
nlfMaxValue: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeLinkFlags = 3
CorNativeLinkType = Int32
nltNone: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeLinkType = 1
nltAnsi: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeLinkType = 2
nltUnicode: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeLinkType = 3
nltAuto: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeLinkType = 4
nltOle: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeLinkType = 5
nltMaxValue: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeLinkType = 7
CorNativeType = Int32
NATIVE_TYPE_END: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 0
NATIVE_TYPE_VOID: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 1
NATIVE_TYPE_BOOLEAN: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 2
NATIVE_TYPE_I1: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 3
NATIVE_TYPE_U1: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 4
NATIVE_TYPE_I2: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 5
NATIVE_TYPE_U2: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 6
NATIVE_TYPE_I4: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 7
NATIVE_TYPE_U4: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 8
NATIVE_TYPE_I8: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 9
NATIVE_TYPE_U8: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 10
NATIVE_TYPE_R4: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 11
NATIVE_TYPE_R8: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 12
NATIVE_TYPE_SYSCHAR: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 13
NATIVE_TYPE_VARIANT: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 14
NATIVE_TYPE_CURRENCY: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 15
NATIVE_TYPE_PTR: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 16
NATIVE_TYPE_DECIMAL: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 17
NATIVE_TYPE_DATE: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 18
NATIVE_TYPE_BSTR: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 19
NATIVE_TYPE_LPSTR: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 20
NATIVE_TYPE_LPWSTR: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 21
NATIVE_TYPE_LPTSTR: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 22
NATIVE_TYPE_FIXEDSYSSTRING: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 23
NATIVE_TYPE_OBJECTREF: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 24
NATIVE_TYPE_IUNKNOWN: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 25
NATIVE_TYPE_IDISPATCH: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 26
NATIVE_TYPE_STRUCT: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 27
NATIVE_TYPE_INTF: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 28
NATIVE_TYPE_SAFEARRAY: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 29
NATIVE_TYPE_FIXEDARRAY: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 30
NATIVE_TYPE_INT: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 31
NATIVE_TYPE_UINT: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 32
NATIVE_TYPE_NESTEDSTRUCT: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 33
NATIVE_TYPE_BYVALSTR: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 34
NATIVE_TYPE_ANSIBSTR: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 35
NATIVE_TYPE_TBSTR: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 36
NATIVE_TYPE_VARIANTBOOL: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 37
NATIVE_TYPE_FUNC: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 38
NATIVE_TYPE_ASANY: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 40
NATIVE_TYPE_ARRAY: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 42
NATIVE_TYPE_LPSTRUCT: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 43
NATIVE_TYPE_CUSTOMMARSHALER: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 44
NATIVE_TYPE_ERROR: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 45
NATIVE_TYPE_IINSPECTABLE: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 46
NATIVE_TYPE_HSTRING: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 47
NATIVE_TYPE_LPUTF8STR: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 48
NATIVE_TYPE_MAX: win32more.Windows.Win32.System.WinRT.Metadata.CorNativeType = 80
CorNotificationForTokenMovement = Int32
MDNotifyDefault: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 15
MDNotifyAll: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = -1
MDNotifyNone: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 0
MDNotifyMethodDef: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 1
MDNotifyMemberRef: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 2
MDNotifyFieldDef: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 4
MDNotifyTypeRef: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 8
MDNotifyTypeDef: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 16
MDNotifyParamDef: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 32
MDNotifyInterfaceImpl: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 64
MDNotifyProperty: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 128
MDNotifyEvent: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 256
MDNotifySignature: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 512
MDNotifyTypeSpec: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 1024
MDNotifyCustomAttribute: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 2048
MDNotifySecurityValue: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 4096
MDNotifyPermission: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 8192
MDNotifyModuleRef: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 16384
MDNotifyNameSpace: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 32768
MDNotifyAssemblyRef: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 16777216
MDNotifyFile: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 33554432
MDNotifyExportedType: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 67108864
MDNotifyResource: win32more.Windows.Win32.System.WinRT.Metadata.CorNotificationForTokenMovement = 134217728
CorOpenFlags = Int32
ofRead: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 0
ofWrite: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 1
ofReadWriteMask: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 1
ofCopyMemory: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 2
ofReadOnly: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 16
ofTakeOwnership: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 32
ofNoTypeLib: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 128
ofNoTransform: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 4096
ofCheckIntegrity: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 2048
ofReserved1: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 256
ofReserved2: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 512
ofReserved3: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = 1024
ofReserved: win32more.Windows.Win32.System.WinRT.Metadata.CorOpenFlags = -6336
CorPEKind = Int32
peNot: win32more.Windows.Win32.System.WinRT.Metadata.CorPEKind = 0
peILonly: win32more.Windows.Win32.System.WinRT.Metadata.CorPEKind = 1
pe32BitRequired: win32more.Windows.Win32.System.WinRT.Metadata.CorPEKind = 2
pe32Plus: win32more.Windows.Win32.System.WinRT.Metadata.CorPEKind = 4
pe32Unmanaged: win32more.Windows.Win32.System.WinRT.Metadata.CorPEKind = 8
pe32BitPreferred: win32more.Windows.Win32.System.WinRT.Metadata.CorPEKind = 16
CorParamAttr = Int32
pdIn: win32more.Windows.Win32.System.WinRT.Metadata.CorParamAttr = 1
pdOut: win32more.Windows.Win32.System.WinRT.Metadata.CorParamAttr = 2
pdOptional: win32more.Windows.Win32.System.WinRT.Metadata.CorParamAttr = 16
pdReservedMask: win32more.Windows.Win32.System.WinRT.Metadata.CorParamAttr = 61440
pdHasDefault: win32more.Windows.Win32.System.WinRT.Metadata.CorParamAttr = 4096
pdHasFieldMarshal: win32more.Windows.Win32.System.WinRT.Metadata.CorParamAttr = 8192
pdUnused: win32more.Windows.Win32.System.WinRT.Metadata.CorParamAttr = 53216
CorPinvokeMap = Int32
pmNoMangle: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 1
pmCharSetMask: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 6
pmCharSetNotSpec: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 0
pmCharSetAnsi: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 2
pmCharSetUnicode: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 4
pmCharSetAuto: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 6
pmBestFitUseAssem: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 0
pmBestFitEnabled: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 16
pmBestFitDisabled: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 32
pmBestFitMask: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 48
pmThrowOnUnmappableCharUseAssem: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 0
pmThrowOnUnmappableCharEnabled: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 4096
pmThrowOnUnmappableCharDisabled: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 8192
pmThrowOnUnmappableCharMask: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 12288
pmSupportsLastError: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 64
pmCallConvMask: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 1792
pmCallConvWinapi: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 256
pmCallConvCdecl: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 512
pmCallConvStdcall: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 768
pmCallConvThiscall: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 1024
pmCallConvFastcall: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 1280
pmMaxValue: win32more.Windows.Win32.System.WinRT.Metadata.CorPinvokeMap = 65535
CorPropertyAttr = Int32
prSpecialName: win32more.Windows.Win32.System.WinRT.Metadata.CorPropertyAttr = 512
prReservedMask: win32more.Windows.Win32.System.WinRT.Metadata.CorPropertyAttr = 62464
prRTSpecialName: win32more.Windows.Win32.System.WinRT.Metadata.CorPropertyAttr = 1024
prHasDefault: win32more.Windows.Win32.System.WinRT.Metadata.CorPropertyAttr = 4096
prUnused: win32more.Windows.Win32.System.WinRT.Metadata.CorPropertyAttr = 59903
CorRefToDefCheck = Int32
MDRefToDefDefault: win32more.Windows.Win32.System.WinRT.Metadata.CorRefToDefCheck = 3
MDRefToDefAll: win32more.Windows.Win32.System.WinRT.Metadata.CorRefToDefCheck = -1
MDRefToDefNone: win32more.Windows.Win32.System.WinRT.Metadata.CorRefToDefCheck = 0
MDTypeRefToDef: win32more.Windows.Win32.System.WinRT.Metadata.CorRefToDefCheck = 1
MDMemberRefToDef: win32more.Windows.Win32.System.WinRT.Metadata.CorRefToDefCheck = 2
CorRegFlags = Int32
regNoCopy: win32more.Windows.Win32.System.WinRT.Metadata.CorRegFlags = 1
regConfig: win32more.Windows.Win32.System.WinRT.Metadata.CorRegFlags = 2
regHasRefs: win32more.Windows.Win32.System.WinRT.Metadata.CorRegFlags = 4
CorSaveSize = Int32
cssAccurate: win32more.Windows.Win32.System.WinRT.Metadata.CorSaveSize = 0
cssQuick: win32more.Windows.Win32.System.WinRT.Metadata.CorSaveSize = 1
cssDiscardTransientCAs: win32more.Windows.Win32.System.WinRT.Metadata.CorSaveSize = 2
CorSerializationType = Int32
SERIALIZATION_TYPE_UNDEFINED: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 0
SERIALIZATION_TYPE_BOOLEAN: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 2
SERIALIZATION_TYPE_CHAR: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 3
SERIALIZATION_TYPE_I1: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 4
SERIALIZATION_TYPE_U1: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 5
SERIALIZATION_TYPE_I2: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 6
SERIALIZATION_TYPE_U2: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 7
SERIALIZATION_TYPE_I4: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 8
SERIALIZATION_TYPE_U4: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 9
SERIALIZATION_TYPE_I8: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 10
SERIALIZATION_TYPE_U8: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 11
SERIALIZATION_TYPE_R4: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 12
SERIALIZATION_TYPE_R8: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 13
SERIALIZATION_TYPE_STRING: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 14
SERIALIZATION_TYPE_SZARRAY: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 29
SERIALIZATION_TYPE_TYPE: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 80
SERIALIZATION_TYPE_TAGGED_OBJECT: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 81
SERIALIZATION_TYPE_FIELD: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 83
SERIALIZATION_TYPE_PROPERTY: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 84
SERIALIZATION_TYPE_ENUM: win32more.Windows.Win32.System.WinRT.Metadata.CorSerializationType = 85
CorSetENC = Int32
MDSetENCOn: win32more.Windows.Win32.System.WinRT.Metadata.CorSetENC = 1
MDSetENCOff: win32more.Windows.Win32.System.WinRT.Metadata.CorSetENC = 2
MDUpdateENC: win32more.Windows.Win32.System.WinRT.Metadata.CorSetENC = 1
MDUpdateFull: win32more.Windows.Win32.System.WinRT.Metadata.CorSetENC = 2
MDUpdateExtension: win32more.Windows.Win32.System.WinRT.Metadata.CorSetENC = 3
MDUpdateIncremental: win32more.Windows.Win32.System.WinRT.Metadata.CorSetENC = 4
MDUpdateDelta: win32more.Windows.Win32.System.WinRT.Metadata.CorSetENC = 5
MDUpdateMask: win32more.Windows.Win32.System.WinRT.Metadata.CorSetENC = 7
CorThreadSafetyOptions = Int32
MDThreadSafetyDefault: win32more.Windows.Win32.System.WinRT.Metadata.CorThreadSafetyOptions = 0
MDThreadSafetyOff: win32more.Windows.Win32.System.WinRT.Metadata.CorThreadSafetyOptions = 0
MDThreadSafetyOn: win32more.Windows.Win32.System.WinRT.Metadata.CorThreadSafetyOptions = 1
CorTokenType = Int32
mdtModule: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 0
mdtTypeRef: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 16777216
mdtTypeDef: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 33554432
mdtFieldDef: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 67108864
mdtMethodDef: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 100663296
mdtParamDef: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 134217728
mdtInterfaceImpl: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 150994944
mdtMemberRef: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 167772160
mdtCustomAttribute: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 201326592
mdtPermission: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 234881024
mdtSignature: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 285212672
mdtEvent: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 335544320
mdtProperty: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 385875968
mdtMethodImpl: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 419430400
mdtModuleRef: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 436207616
mdtTypeSpec: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 452984832
mdtAssembly: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 536870912
mdtAssemblyRef: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 587202560
mdtFile: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 637534208
mdtExportedType: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 654311424
mdtManifestResource: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 671088640
mdtGenericParam: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 704643072
mdtMethodSpec: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 721420288
mdtGenericParamConstraint: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 738197504
mdtString: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 1879048192
mdtName: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 1895825408
mdtBaseType: win32more.Windows.Win32.System.WinRT.Metadata.CorTokenType = 1912602624
CorTypeAttr = Int32
tdVisibilityMask: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 7
tdNotPublic: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 0
tdPublic: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 1
tdNestedPublic: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 2
tdNestedPrivate: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 3
tdNestedFamily: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 4
tdNestedAssembly: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 5
tdNestedFamANDAssem: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 6
tdNestedFamORAssem: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 7
tdLayoutMask: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 24
tdAutoLayout: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 0
tdSequentialLayout: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 8
tdExplicitLayout: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 16
tdClassSemanticsMask: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 32
tdClass: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 0
tdInterface: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 32
tdAbstract: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 128
tdSealed: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 256
tdSpecialName: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 1024
tdImport: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 4096
tdSerializable: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 8192
tdWindowsRuntime: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 16384
tdStringFormatMask: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 196608
tdAnsiClass: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 0
tdUnicodeClass: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 65536
tdAutoClass: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 131072
tdCustomFormatClass: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 196608
tdCustomFormatMask: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 12582912
tdBeforeFieldInit: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 1048576
tdForwarder: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 2097152
tdReservedMask: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 264192
tdRTSpecialName: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 2048
tdHasSecurity: win32more.Windows.Win32.System.WinRT.Metadata.CorTypeAttr = 262144
CorUnmanagedCallingConvention = Int32
IMAGE_CEE_UNMANAGED_CALLCONV_C: win32more.Windows.Win32.System.WinRT.Metadata.CorUnmanagedCallingConvention = 1
IMAGE_CEE_UNMANAGED_CALLCONV_STDCALL: win32more.Windows.Win32.System.WinRT.Metadata.CorUnmanagedCallingConvention = 2
IMAGE_CEE_UNMANAGED_CALLCONV_THISCALL: win32more.Windows.Win32.System.WinRT.Metadata.CorUnmanagedCallingConvention = 3
IMAGE_CEE_UNMANAGED_CALLCONV_FASTCALL: win32more.Windows.Win32.System.WinRT.Metadata.CorUnmanagedCallingConvention = 4
IMAGE_CEE_CS_CALLCONV_C: win32more.Windows.Win32.System.WinRT.Metadata.CorUnmanagedCallingConvention = 1
IMAGE_CEE_CS_CALLCONV_STDCALL: win32more.Windows.Win32.System.WinRT.Metadata.CorUnmanagedCallingConvention = 2
IMAGE_CEE_CS_CALLCONV_THISCALL: win32more.Windows.Win32.System.WinRT.Metadata.CorUnmanagedCallingConvention = 3
IMAGE_CEE_CS_CALLCONV_FASTCALL: win32more.Windows.Win32.System.WinRT.Metadata.CorUnmanagedCallingConvention = 4
CorValidatorModuleType = Int32
ValidatorModuleTypeInvalid: win32more.Windows.Win32.System.WinRT.Metadata.CorValidatorModuleType = 0
ValidatorModuleTypeMin: win32more.Windows.Win32.System.WinRT.Metadata.CorValidatorModuleType = 1
ValidatorModuleTypePE: win32more.Windows.Win32.System.WinRT.Metadata.CorValidatorModuleType = 1
ValidatorModuleTypeObj: win32more.Windows.Win32.System.WinRT.Metadata.CorValidatorModuleType = 2
ValidatorModuleTypeEnc: win32more.Windows.Win32.System.WinRT.Metadata.CorValidatorModuleType = 3
ValidatorModuleTypeIncr: win32more.Windows.Win32.System.WinRT.Metadata.CorValidatorModuleType = 4
ValidatorModuleTypeMax: win32more.Windows.Win32.System.WinRT.Metadata.CorValidatorModuleType = 4
class ICeeGen(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7ed1bdff-8e36-11d2-9c56-00a0c9b7cc45}')
    @commethod(3)
    def EmitString(self, lpString: win32more.Windows.Win32.Foundation.PWSTR, RVA: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetString(self, RVA: UInt32, lpString: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AllocateMethodBuffer(self, cchBuffer: UInt32, lpBuffer: POINTER(POINTER(Byte)), RVA: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMethodBuffer(self, RVA: UInt32, lpBuffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetIMapTokenIface(self, pIMapToken: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GenerateCeeFile(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetIlSection(self, section: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStringSection(self, section: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddSectionReloc(self, section: VoidPtr, offset: UInt32, relativeTo: VoidPtr, relocType: win32more.Windows.Win32.System.WinRT.Metadata.CeeSectionRelocType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSectionCreate(self, name: win32more.Windows.Win32.Foundation.PSTR, flags: UInt32, section: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSectionDataLen(self, section: VoidPtr, dataLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSectionBlock(self, section: VoidPtr, len: UInt32, align: UInt32, ppBytes: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def TruncateSection(self, section: VoidPtr, len: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GenerateCeeMemoryImage(self, ppImage: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ComputePointer(self, section: VoidPtr, RVA: UInt32, lpBuffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d0e80dd3-12d4-11d3-b39d-00c04ff81795}')
    @commethod(3)
    def MarkToken(self, tk: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMAGE_COR_ILMETHOD(Union):
    Tiny: win32more.Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_TINY
    Fat: win32more.Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_FAT
class IMAGE_COR_ILMETHOD_FAT(Structure):
    Flags: Annotated[UInt32, 12]
    Size: Annotated[UInt32, 4]
    MaxStack: Annotated[UInt32, 16]
    CodeSize: UInt32
    LocalVarSigTok: UInt32
class IMAGE_COR_ILMETHOD_SECT_EH(Union):
    Small: win32more.Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_EH_SMALL
    Fat: win32more.Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_EH_FAT
class IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT(Structure):
    Flags: win32more.Windows.Win32.System.WinRT.Metadata.CorExceptionFlag
    TryOffset: UInt32
    TryLength: UInt32
    HandlerOffset: UInt32
    HandlerLength: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ClassToken: UInt32
        FilterOffset: UInt32
if ARCH in 'X64,ARM64':
    class IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL(Structure):
        Flags: Annotated[UInt32, 16]
        TryOffset: Annotated[UInt32, 16]
        TryLength: Annotated[UInt32, 8]
        HandlerOffset: Annotated[UInt32, 16]
        HandlerLength: Annotated[UInt32, 8]
        Anonymous: _Anonymous_e__Union
        class _Anonymous_e__Union(Union):
            ClassToken: UInt32
            FilterOffset: UInt32
elif ARCH in 'X86':
    class IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL(Structure):
        Flags: Annotated[Int32, 16]
        TryOffset: Annotated[Int32, 16]
        TryLength: Annotated[UInt32, 8]
        HandlerOffset: Annotated[UInt32, 16]
        HandlerLength: Annotated[UInt32, 8]
        Anonymous: _Anonymous_e__Union
        class _Anonymous_e__Union(Union):
            ClassToken: UInt32
            FilterOffset: UInt32
class IMAGE_COR_ILMETHOD_SECT_EH_FAT(Structure):
    SectFat: win32more.Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_FAT
    Clauses: win32more.Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT * 1
class IMAGE_COR_ILMETHOD_SECT_EH_SMALL(Structure):
    SectSmall: win32more.Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_SMALL
    Reserved: UInt16
    Clauses: win32more.Windows.Win32.System.WinRT.Metadata.IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL * 1
class IMAGE_COR_ILMETHOD_SECT_FAT(Structure):
    Kind: Annotated[UInt32, 8]
    DataSize: Annotated[UInt32, 24]
class IMAGE_COR_ILMETHOD_SECT_SMALL(Structure):
    Kind: Byte
    DataSize: Byte
class IMAGE_COR_ILMETHOD_TINY(Structure):
    Flags_CodeSize: Byte
class IMAGE_COR_VTABLEFIXUP(Structure):
    RVA: UInt32
    Count: UInt16
    Type: UInt16
class IMapToken(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{06a3ea8b-0225-11d1-bf72-00c04fc31e12}')
    @commethod(3)
    def Map(self, tkImp: UInt32, tkEmit: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataAssemblyEmit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{211ef15b-5317-4438-b196-dec87b887693}')
    @commethod(3)
    def DefineAssembly(self, pbPublicKey: VoidPtr, cbPublicKey: UInt32, ulHashAlgId: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, pMetaData: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA), dwAssemblyFlags: UInt32, pma: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DefineAssemblyRef(self, pbPublicKeyOrToken: VoidPtr, cbPublicKeyOrToken: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, pMetaData: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA), pbHashValue: VoidPtr, cbHashValue: UInt32, dwAssemblyRefFlags: UInt32, pmdar: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DefineFile(self, szName: win32more.Windows.Win32.Foundation.PWSTR, pbHashValue: VoidPtr, cbHashValue: UInt32, dwFileFlags: UInt32, pmdf: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DefineExportedType(self, szName: win32more.Windows.Win32.Foundation.PWSTR, tkImplementation: UInt32, tkTypeDef: UInt32, dwExportedTypeFlags: UInt32, pmdct: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DefineManifestResource(self, szName: win32more.Windows.Win32.Foundation.PWSTR, tkImplementation: UInt32, dwOffset: UInt32, dwResourceFlags: UInt32, pmdmr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetAssemblyProps(self, pma: UInt32, pbPublicKey: VoidPtr, cbPublicKey: UInt32, ulHashAlgId: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, pMetaData: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA), dwAssemblyFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetAssemblyRefProps(self, ar: UInt32, pbPublicKeyOrToken: VoidPtr, cbPublicKeyOrToken: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, pMetaData: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA), pbHashValue: VoidPtr, cbHashValue: UInt32, dwAssemblyRefFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetFileProps(self, file: UInt32, pbHashValue: VoidPtr, cbHashValue: UInt32, dwFileFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetExportedTypeProps(self, ct: UInt32, tkImplementation: UInt32, tkTypeDef: UInt32, dwExportedTypeFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetManifestResourceProps(self, mr: UInt32, tkImplementation: UInt32, dwOffset: UInt32, dwResourceFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataAssemblyImport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ee62470b-e94b-424e-9b7c-2f00c9249f93}')
    @commethod(3)
    def GetAssemblyProps(self, mda: UInt32, ppbPublicKey: POINTER(VoidPtr), pcbPublicKey: POINTER(UInt32), pulHashAlgId: POINTER(UInt32), szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), pMetaData: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA), pdwAssemblyFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAssemblyRefProps(self, mdar: UInt32, ppbPublicKeyOrToken: POINTER(VoidPtr), pcbPublicKeyOrToken: POINTER(UInt32), szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), pMetaData: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA), ppbHashValue: POINTER(VoidPtr), pcbHashValue: POINTER(UInt32), pdwAssemblyRefFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileProps(self, mdf: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), ppbHashValue: POINTER(VoidPtr), pcbHashValue: POINTER(UInt32), pdwFileFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetExportedTypeProps(self, mdct: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), ptkImplementation: POINTER(UInt32), ptkTypeDef: POINTER(UInt32), pdwExportedTypeFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetManifestResourceProps(self, mdmr: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), ptkImplementation: POINTER(UInt32), pdwOffset: POINTER(UInt32), pdwResourceFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumAssemblyRefs(self, phEnum: POINTER(VoidPtr), rAssemblyRefs: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumFiles(self, phEnum: POINTER(VoidPtr), rFiles: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumExportedTypes(self, phEnum: POINTER(VoidPtr), rExportedTypes: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumManifestResources(self, phEnum: POINTER(VoidPtr), rManifestResources: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAssemblyFromScope(self, ptkAssembly: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def FindExportedTypeByName(self, szName: win32more.Windows.Win32.Foundation.PWSTR, mdtExportedType: UInt32, ptkExportedType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def FindManifestResourceByName(self, szName: win32more.Windows.Win32.Foundation.PWSTR, ptkManifestResource: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CloseEnum(self, hEnum: VoidPtr) -> Void: ...
    @commethod(16)
    def FindAssembliesByName(self, szAppBase: win32more.Windows.Win32.Foundation.PWSTR, szPrivateBin: win32more.Windows.Win32.Foundation.PWSTR, szAssemblyName: win32more.Windows.Win32.Foundation.PWSTR, ppIUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown), cMax: UInt32, pcAssemblies: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataDispenser(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{809c652e-7396-11d2-9771-00a0c9b4d50c}')
    @commethod(3)
    def DefineScope(self, rclsid: POINTER(Guid), dwCreateFlags: UInt32, riid: POINTER(Guid), ppIUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenScope(self, szScope: win32more.Windows.Win32.Foundation.PWSTR, dwOpenFlags: UInt32, riid: POINTER(Guid), ppIUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OpenScopeOnMemory(self, pData: VoidPtr, cbData: UInt32, dwOpenFlags: UInt32, riid: POINTER(Guid), ppIUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataDispenserEx(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataDispenser
    _iid_ = Guid('{31bcfce2-dafb-11d2-9f81-00c04f79a0a3}')
    @commethod(6)
    def SetOption(self, optionid: POINTER(Guid), value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOption(self, optionid: POINTER(Guid), pvalue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OpenScopeOnITypeInfo(self, pITI: win32more.Windows.Win32.System.Com.ITypeInfo, dwOpenFlags: UInt32, riid: POINTER(Guid), ppIUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCORSystemDirectory(self, szBuffer: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, pchBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FindAssembly(self, szAppBase: win32more.Windows.Win32.Foundation.PWSTR, szPrivateBin: win32more.Windows.Win32.Foundation.PWSTR, szGlobalBin: win32more.Windows.Win32.Foundation.PWSTR, szAssemblyName: win32more.Windows.Win32.Foundation.PWSTR, szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pcName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FindAssemblyModule(self, szAppBase: win32more.Windows.Win32.Foundation.PWSTR, szPrivateBin: win32more.Windows.Win32.Foundation.PWSTR, szGlobalBin: win32more.Windows.Win32.Foundation.PWSTR, szAssemblyName: win32more.Windows.Win32.Foundation.PWSTR, szModuleName: win32more.Windows.Win32.Foundation.PWSTR, szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pcName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataEmit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ba3fee4c-ecb9-4e41-83b7-183fa41cd859}')
    @commethod(3)
    def SetModuleProps(self, szName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Save(self, szFile: win32more.Windows.Win32.Foundation.PWSTR, dwSaveFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SaveToStream(self, pIStream: win32more.Windows.Win32.System.Com.IStream, dwSaveFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSaveSize(self, fSave: win32more.Windows.Win32.System.WinRT.Metadata.CorSaveSize, pdwSaveSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DefineTypeDef(self, szTypeDef: win32more.Windows.Win32.Foundation.PWSTR, dwTypeDefFlags: UInt32, tkExtends: UInt32, rtkImplements: POINTER(UInt32), ptd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DefineNestedType(self, szTypeDef: win32more.Windows.Win32.Foundation.PWSTR, dwTypeDefFlags: UInt32, tkExtends: UInt32, rtkImplements: POINTER(UInt32), tdEncloser: UInt32, ptd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetHandler(self, pUnk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DefineMethod(self, td: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, dwMethodFlags: UInt32, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, ulCodeRVA: UInt32, dwImplFlags: UInt32, pmd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DefineMethodImpl(self, td: UInt32, tkBody: UInt32, tkDecl: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DefineTypeRefByName(self, tkResolutionScope: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, ptr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DefineImportType(self, pAssemImport: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyImport, pbHashValue: VoidPtr, cbHashValue: UInt32, pImport: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataImport, tdImport: UInt32, pAssemEmit: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyEmit, ptr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def DefineMemberRef(self, tkImport: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def DefineImportMember(self, pAssemImport: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyImport, pbHashValue: VoidPtr, cbHashValue: UInt32, pImport: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataImport, mbMember: UInt32, pAssemEmit: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyEmit, tkParent: UInt32, pmr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DefineEvent(self, td: UInt32, szEvent: win32more.Windows.Win32.Foundation.PWSTR, dwEventFlags: UInt32, tkEventType: UInt32, mdAddOn: UInt32, mdRemoveOn: UInt32, mdFire: UInt32, rmdOtherMethods: POINTER(UInt32), pmdEvent: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetClassLayout(self, td: UInt32, dwPackSize: UInt32, rFieldOffsets: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.COR_FIELD_OFFSET), ulClassSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteClassLayout(self, td: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetFieldMarshal(self, tk: UInt32, pvNativeType: POINTER(Byte), cbNativeType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DeleteFieldMarshal(self, tk: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DefinePermissionSet(self, tk: UInt32, dwAction: UInt32, pvPermission: VoidPtr, cbPermission: UInt32, ppm: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetRVA(self, md: UInt32, ulRVA: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetTokenFromSig(self, pvSig: POINTER(Byte), cbSig: UInt32, pmsig: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def DefineModuleRef(self, szName: win32more.Windows.Win32.Foundation.PWSTR, pmur: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetParent(self, mr: UInt32, tk: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetTokenFromTypeSpec(self, pvSig: POINTER(Byte), cbSig: UInt32, ptypespec: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SaveToMemory(self, pbData: VoidPtr, cbData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def DefineUserString(self, szString: win32more.Windows.Win32.Foundation.PWSTR, cchString: UInt32, pstk: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DeleteToken(self, tkObj: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetMethodProps(self, md: UInt32, dwMethodFlags: UInt32, ulCodeRVA: UInt32, dwImplFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetTypeDefProps(self, td: UInt32, dwTypeDefFlags: UInt32, tkExtends: UInt32, rtkImplements: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetEventProps(self, ev: UInt32, dwEventFlags: UInt32, tkEventType: UInt32, mdAddOn: UInt32, mdRemoveOn: UInt32, mdFire: UInt32, rmdOtherMethods: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetPermissionSetProps(self, tk: UInt32, dwAction: UInt32, pvPermission: VoidPtr, cbPermission: UInt32, ppm: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def DefinePinvokeMap(self, tk: UInt32, dwMappingFlags: UInt32, szImportName: win32more.Windows.Win32.Foundation.PWSTR, mrImportDLL: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetPinvokeMap(self, tk: UInt32, dwMappingFlags: UInt32, szImportName: win32more.Windows.Win32.Foundation.PWSTR, mrImportDLL: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def DeletePinvokeMap(self, tk: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def DefineCustomAttribute(self, tkOwner: UInt32, tkCtor: UInt32, pCustomAttribute: VoidPtr, cbCustomAttribute: UInt32, pcv: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetCustomAttributeValue(self, pcv: UInt32, pCustomAttribute: VoidPtr, cbCustomAttribute: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def DefineField(self, td: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, dwFieldFlags: UInt32, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, dwCPlusTypeFlag: UInt32, pValue: VoidPtr, cchValue: UInt32, pmd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def DefineProperty(self, td: UInt32, szProperty: win32more.Windows.Win32.Foundation.PWSTR, dwPropFlags: UInt32, pvSig: POINTER(Byte), cbSig: UInt32, dwCPlusTypeFlag: UInt32, pValue: VoidPtr, cchValue: UInt32, mdSetter: UInt32, mdGetter: UInt32, rmdOtherMethods: POINTER(UInt32), pmdProp: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def DefineParam(self, md: UInt32, ulParamSeq: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, dwParamFlags: UInt32, dwCPlusTypeFlag: UInt32, pValue: VoidPtr, cchValue: UInt32, ppd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def SetFieldProps(self, fd: UInt32, dwFieldFlags: UInt32, dwCPlusTypeFlag: UInt32, pValue: VoidPtr, cchValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def SetPropertyProps(self, pr: UInt32, dwPropFlags: UInt32, dwCPlusTypeFlag: UInt32, pValue: VoidPtr, cchValue: UInt32, mdSetter: UInt32, mdGetter: UInt32, rmdOtherMethods: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def SetParamProps(self, pd: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, dwParamFlags: UInt32, dwCPlusTypeFlag: UInt32, pValue: VoidPtr, cchValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def DefineSecurityAttributeSet(self, tkObj: UInt32, rSecAttrs: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.COR_SECATTR), cSecAttrs: UInt32, pulErrorAttr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def ApplyEditAndContinue(self, pImport: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def TranslateSigWithScope(self, pAssemImport: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyImport, pbHashValue: VoidPtr, cbHashValue: UInt32, import_: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataImport, pbSigBlob: POINTER(Byte), cbSigBlob: UInt32, pAssemEmit: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataAssemblyEmit, emit: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataEmit, pvTranslatedSig: POINTER(Byte), cbTranslatedSigMax: UInt32, pcbTranslatedSig: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def SetMethodImplFlags(self, md: UInt32, dwImplFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def SetFieldRVA(self, fd: UInt32, ulRVA: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def Merge(self, pImport: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataImport, pHostMapToken: win32more.Windows.Win32.System.WinRT.Metadata.IMapToken, pHandler: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def MergeEnd(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataEmit2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataEmit
    _iid_ = Guid('{f5dd9950-f693-42e6-830e-7b833e8146a9}')
    @commethod(52)
    def DefineMethodSpec(self, tkParent: UInt32, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmi: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def GetDeltaSaveSize(self, fSave: win32more.Windows.Win32.System.WinRT.Metadata.CorSaveSize, pdwSaveSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SaveDelta(self, szFile: win32more.Windows.Win32.Foundation.PWSTR, dwSaveFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def SaveDeltaToStream(self, pIStream: win32more.Windows.Win32.System.Com.IStream, dwSaveFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def SaveDeltaToMemory(self, pbData: VoidPtr, cbData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def DefineGenericParam(self, tk: UInt32, ulParamSeq: UInt32, dwParamFlags: UInt32, szname: win32more.Windows.Win32.Foundation.PWSTR, reserved: UInt32, rtkConstraints: POINTER(UInt32), pgp: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def SetGenericParamProps(self, gp: UInt32, dwParamFlags: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, reserved: UInt32, rtkConstraints: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def ResetENCLog(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataError(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b81ff171-20f3-11d2-8dcc-00a0c9b09c19}')
    @commethod(3)
    def OnError(self, hrError: win32more.Windows.Win32.Foundation.HRESULT, token: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d0e80dd1-12d4-11d3-b39d-00c04ff81795}')
    @commethod(3)
    def UnmarkAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MarkToken(self, tk: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsTokenMarked(self, tk: UInt32, pIsMarked: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataImport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7dac8207-d3ae-4c75-9b67-92801a497d44}')
    @commethod(3)
    def CloseEnum(self, hEnum: VoidPtr) -> Void: ...
    @commethod(4)
    def CountEnum(self, hEnum: VoidPtr, pulCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ResetEnum(self, hEnum: VoidPtr, ulPos: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumTypeDefs(self, phEnum: POINTER(VoidPtr), rTypeDefs: POINTER(UInt32), cMax: UInt32, pcTypeDefs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumInterfaceImpls(self, phEnum: POINTER(VoidPtr), td: UInt32, rImpls: POINTER(UInt32), cMax: UInt32, pcImpls: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumTypeRefs(self, phEnum: POINTER(VoidPtr), rTypeRefs: POINTER(UInt32), cMax: UInt32, pcTypeRefs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def FindTypeDefByName(self, szTypeDef: win32more.Windows.Win32.Foundation.PWSTR, tkEnclosingClass: UInt32, ptd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetScopeProps(self, szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), pmvid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetModuleFromScope(self, pmd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetTypeDefProps(self, td: UInt32, szTypeDef: win32more.Windows.Win32.Foundation.PWSTR, cchTypeDef: UInt32, pchTypeDef: POINTER(UInt32), pdwTypeDefFlags: POINTER(UInt32), ptkExtends: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInterfaceImplProps(self, iiImpl: UInt32, pClass: POINTER(UInt32), ptkIface: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTypeRefProps(self, tr: UInt32, ptkResolutionScope: POINTER(UInt32), szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ResolveTypeRef(self, tr: UInt32, riid: POINTER(Guid), ppIScope: POINTER(win32more.Windows.Win32.System.Com.IUnknown), ptd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EnumMembers(self, phEnum: POINTER(VoidPtr), cl: UInt32, rMembers: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnumMembersWithName(self, phEnum: POINTER(VoidPtr), cl: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, rMembers: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumMethods(self, phEnum: POINTER(VoidPtr), cl: UInt32, rMethods: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EnumMethodsWithName(self, phEnum: POINTER(VoidPtr), cl: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, rMethods: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def EnumFields(self, phEnum: POINTER(VoidPtr), cl: UInt32, rFields: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EnumFieldsWithName(self, phEnum: POINTER(VoidPtr), cl: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, rFields: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def EnumParams(self, phEnum: POINTER(VoidPtr), mb: UInt32, rParams: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def EnumMemberRefs(self, phEnum: POINTER(VoidPtr), tkParent: UInt32, rMemberRefs: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def EnumMethodImpls(self, phEnum: POINTER(VoidPtr), td: UInt32, rMethodBody: POINTER(UInt32), rMethodDecl: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def EnumPermissionSets(self, phEnum: POINTER(VoidPtr), tk: UInt32, dwActions: UInt32, rPermission: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def FindMember(self, td: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def FindMethod(self, td: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def FindField(self, td: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def FindMemberRef(self, td: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, pvSigBlob: POINTER(Byte), cbSigBlob: UInt32, pmr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetMethodProps(self, mb: UInt32, pClass: POINTER(UInt32), szMethod: win32more.Windows.Win32.Foundation.PWSTR, cchMethod: UInt32, pchMethod: POINTER(UInt32), pdwAttr: POINTER(UInt32), ppvSigBlob: POINTER(POINTER(Byte)), pcbSigBlob: POINTER(UInt32), pulCodeRVA: POINTER(UInt32), pdwImplFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetMemberRefProps(self, mr: UInt32, ptk: POINTER(UInt32), szMember: win32more.Windows.Win32.Foundation.PWSTR, cchMember: UInt32, pchMember: POINTER(UInt32), ppvSigBlob: POINTER(POINTER(Byte)), pbSig: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def EnumProperties(self, phEnum: POINTER(VoidPtr), td: UInt32, rProperties: POINTER(UInt32), cMax: UInt32, pcProperties: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def EnumEvents(self, phEnum: POINTER(VoidPtr), td: UInt32, rEvents: POINTER(UInt32), cMax: UInt32, pcEvents: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetEventProps(self, ev: UInt32, pClass: POINTER(UInt32), szEvent: win32more.Windows.Win32.Foundation.PWSTR, cchEvent: UInt32, pchEvent: POINTER(UInt32), pdwEventFlags: POINTER(UInt32), ptkEventType: POINTER(UInt32), pmdAddOn: POINTER(UInt32), pmdRemoveOn: POINTER(UInt32), pmdFire: POINTER(UInt32), rmdOtherMethod: POINTER(UInt32), cMax: UInt32, pcOtherMethod: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def EnumMethodSemantics(self, phEnum: POINTER(VoidPtr), mb: UInt32, rEventProp: POINTER(UInt32), cMax: UInt32, pcEventProp: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetMethodSemantics(self, mb: UInt32, tkEventProp: UInt32, pdwSemanticsFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetClassLayout(self, td: UInt32, pdwPackSize: POINTER(UInt32), rFieldOffset: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.COR_FIELD_OFFSET), cMax: UInt32, pcFieldOffset: POINTER(UInt32), pulClassSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetFieldMarshal(self, tk: UInt32, ppvNativeType: POINTER(POINTER(Byte)), pcbNativeType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetRVA(self, tk: UInt32, pulCodeRVA: POINTER(UInt32), pdwImplFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetPermissionSetProps(self, pm: UInt32, pdwAction: POINTER(UInt32), ppvPermission: POINTER(VoidPtr), pcbPermission: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetSigFromToken(self, mdSig: UInt32, ppvSig: POINTER(POINTER(Byte)), pcbSig: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetModuleRefProps(self, mur: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def EnumModuleRefs(self, phEnum: POINTER(VoidPtr), rModuleRefs: POINTER(UInt32), cmax: UInt32, pcModuleRefs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetTypeSpecFromToken(self, typespec: UInt32, ppvSig: POINTER(POINTER(Byte)), pcbSig: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def GetNameFromToken(self, tk: UInt32, pszUtf8NamePtr: POINTER(POINTER(SByte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def EnumUnresolvedMethods(self, phEnum: POINTER(VoidPtr), rMethods: POINTER(UInt32), cMax: UInt32, pcTokens: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def GetUserString(self, stk: UInt32, szString: win32more.Windows.Win32.Foundation.PWSTR, cchString: UInt32, pchString: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetPinvokeMap(self, tk: UInt32, pdwMappingFlags: POINTER(UInt32), szImportName: win32more.Windows.Win32.Foundation.PWSTR, cchImportName: UInt32, pchImportName: POINTER(UInt32), pmrImportDLL: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def EnumSignatures(self, phEnum: POINTER(VoidPtr), rSignatures: POINTER(UInt32), cmax: UInt32, pcSignatures: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def EnumTypeSpecs(self, phEnum: POINTER(VoidPtr), rTypeSpecs: POINTER(UInt32), cmax: UInt32, pcTypeSpecs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def EnumUserStrings(self, phEnum: POINTER(VoidPtr), rStrings: POINTER(UInt32), cmax: UInt32, pcStrings: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def GetParamForMethodIndex(self, md: UInt32, ulParamSeq: UInt32, ppd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def EnumCustomAttributes(self, phEnum: POINTER(VoidPtr), tk: UInt32, tkType: UInt32, rCustomAttributes: POINTER(UInt32), cMax: UInt32, pcCustomAttributes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def GetCustomAttributeProps(self, cv: UInt32, ptkObj: POINTER(UInt32), ptkType: POINTER(UInt32), ppBlob: POINTER(VoidPtr), pcbSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def FindTypeRef(self, tkResolutionScope: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, ptr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def GetMemberProps(self, mb: UInt32, pClass: POINTER(UInt32), szMember: win32more.Windows.Win32.Foundation.PWSTR, cchMember: UInt32, pchMember: POINTER(UInt32), pdwAttr: POINTER(UInt32), ppvSigBlob: POINTER(POINTER(Byte)), pcbSigBlob: POINTER(UInt32), pulCodeRVA: POINTER(UInt32), pdwImplFlags: POINTER(UInt32), pdwCPlusTypeFlag: POINTER(UInt32), ppValue: POINTER(VoidPtr), pcchValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def GetFieldProps(self, mb: UInt32, pClass: POINTER(UInt32), szField: win32more.Windows.Win32.Foundation.PWSTR, cchField: UInt32, pchField: POINTER(UInt32), pdwAttr: POINTER(UInt32), ppvSigBlob: POINTER(POINTER(Byte)), pcbSigBlob: POINTER(UInt32), pdwCPlusTypeFlag: POINTER(UInt32), ppValue: POINTER(VoidPtr), pcchValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def GetPropertyProps(self, prop: UInt32, pClass: POINTER(UInt32), szProperty: win32more.Windows.Win32.Foundation.PWSTR, cchProperty: UInt32, pchProperty: POINTER(UInt32), pdwPropFlags: POINTER(UInt32), ppvSig: POINTER(POINTER(Byte)), pbSig: POINTER(UInt32), pdwCPlusTypeFlag: POINTER(UInt32), ppDefaultValue: POINTER(VoidPtr), pcchDefaultValue: POINTER(UInt32), pmdSetter: POINTER(UInt32), pmdGetter: POINTER(UInt32), rmdOtherMethod: POINTER(UInt32), cMax: UInt32, pcOtherMethod: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def GetParamProps(self, tk: UInt32, pmd: POINTER(UInt32), pulSequence: POINTER(UInt32), szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32), pdwAttr: POINTER(UInt32), pdwCPlusTypeFlag: POINTER(UInt32), ppValue: POINTER(VoidPtr), pcchValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def GetCustomAttributeByName(self, tkObj: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR, ppData: POINTER(VoidPtr), pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def IsValidToken(self, tk: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(62)
    def GetNestedClassProps(self, tdNestedClass: UInt32, ptdEnclosingClass: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def GetNativeCallConvFromSig(self, pvSig: VoidPtr, cbSig: UInt32, pCallConv: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def IsGlobal(self, pd: UInt32, pbGlobal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataImport2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataImport
    _iid_ = Guid('{fce5efa0-8bba-4f8e-a036-8f2022b08466}')
    @commethod(65)
    def EnumGenericParams(self, phEnum: POINTER(VoidPtr), tk: UInt32, rGenericParams: POINTER(UInt32), cMax: UInt32, pcGenericParams: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def GetGenericParamProps(self, gp: UInt32, pulParamSeq: POINTER(UInt32), pdwParamFlags: POINTER(UInt32), ptOwner: POINTER(UInt32), reserved: POINTER(UInt32), wzname: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def GetMethodSpecProps(self, mi: UInt32, tkParent: POINTER(UInt32), ppvSigBlob: POINTER(POINTER(Byte)), pcbSigBlob: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def EnumGenericParamConstraints(self, phEnum: POINTER(VoidPtr), tk: UInt32, rGenericParamConstraints: POINTER(UInt32), cMax: UInt32, pcGenericParamConstraints: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetGenericParamConstraintProps(self, gpc: UInt32, ptGenericParam: POINTER(UInt32), ptkConstraintType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def GetPEKind(self, pdwPEKind: POINTER(UInt32), pdwMAchine: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def GetVersionString(self, pwzBuf: win32more.Windows.Win32.Foundation.PWSTR, ccBufSize: UInt32, pccBufSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def EnumMethodSpecs(self, phEnum: POINTER(VoidPtr), tk: UInt32, rMethodSpecs: POINTER(UInt32), cMax: UInt32, pcMethodSpecs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7998ea64-7f95-48b8-86fc-17caf48bf5cb}')
    @commethod(3)
    def GetFileMapping(self, ppvData: POINTER(VoidPtr), pcbData: POINTER(UInt64), pdwMappingType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataTables(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d8f579ab-402d-4b8e-82d9-5d63b1065c68}')
    @commethod(3)
    def GetStringHeapSize(self, pcbStrings: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBlobHeapSize(self, pcbBlobs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetGuidHeapSize(self, pcbGuids: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUserStringHeapSize(self, pcbBlobs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNumTables(self, pcTables: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableIndex(self, token: UInt32, pixTbl: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableInfo(self, ixTbl: UInt32, pcbRow: POINTER(UInt32), pcRows: POINTER(UInt32), pcCols: POINTER(UInt32), piKey: POINTER(UInt32), ppName: POINTER(POINTER(SByte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetColumnInfo(self, ixTbl: UInt32, ixCol: UInt32, poCol: POINTER(UInt32), pcbCol: POINTER(UInt32), pType: POINTER(UInt32), ppName: POINTER(POINTER(SByte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCodedTokenInfo(self, ixCdTkn: UInt32, pcTokens: POINTER(UInt32), ppTokens: POINTER(POINTER(UInt32)), ppName: POINTER(POINTER(SByte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRow(self, ixTbl: UInt32, rid: UInt32, ppRow: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetColumn(self, ixTbl: UInt32, ixCol: UInt32, rid: UInt32, pVal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetString(self, ixString: UInt32, ppString: POINTER(POINTER(SByte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetBlob(self, ixBlob: UInt32, pcbData: POINTER(UInt32), ppData: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetGuid(self, ixGuid: UInt32, ppGUID: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetUserString(self, ixUserString: UInt32, pcbData: POINTER(UInt32), ppData: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetNextString(self, ixString: UInt32, pNext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetNextBlob(self, ixBlob: UInt32, pNext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetNextGuid(self, ixGuid: UInt32, pNext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetNextUserString(self, ixUserString: UInt32, pNext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataTables2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.Metadata.IMetaDataTables
    _iid_ = Guid('{badb5f70-58da-43a9-a1c6-d74819f19b15}')
    @commethod(22)
    def GetMetaDataStorage(self, ppvMd: POINTER(VoidPtr), pcbMd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMetaDataStreamInfo(self, ix: UInt32, ppchName: POINTER(POINTER(SByte)), ppv: POINTER(VoidPtr), pcb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataValidate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4709c9c6-81ff-11d3-9fc7-00c04f79a0a3}')
    @commethod(3)
    def ValidatorInit(self, dwModuleType: UInt32, pUnk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ValidateMetaData(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMetaDataWinMDImport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{969ea0c5-964e-411b-a807-b0f3c2dfcbd4}')
    @commethod(3)
    def GetUntransformedTypeRefProps(self, tr: UInt32, ptkResolutionScope: POINTER(UInt32), szName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, pchName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRoMetaDataLocator(ComPtr):
    extends: None
    @commethod(0)
    def Locate(self, nameElement: win32more.Windows.Win32.Foundation.PWSTR, metaDataDestination: win32more.Windows.Win32.System.WinRT.Metadata.IRoSimpleMetaDataBuilder) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRoSimpleMetaDataBuilder(ComPtr):
    extends: None
    @commethod(0)
    def SetWinRtInterface(self, iid: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(1)
    def SetDelegate(self, iid: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(2)
    def SetInterfaceGroupSimpleDefault(self, name: win32more.Windows.Win32.Foundation.PWSTR, defaultInterfaceName: win32more.Windows.Win32.Foundation.PWSTR, defaultInterfaceIID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(3)
    def SetInterfaceGroupParameterizedDefault(self, name: win32more.Windows.Win32.Foundation.PWSTR, elementCount: UInt32, defaultInterfaceNameElements: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetRuntimeClassSimpleDefault(self, name: win32more.Windows.Win32.Foundation.PWSTR, defaultInterfaceName: win32more.Windows.Win32.Foundation.PWSTR, defaultInterfaceIID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetRuntimeClassParameterizedDefault(self, name: win32more.Windows.Win32.Foundation.PWSTR, elementCount: UInt32, defaultInterfaceNameElements: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetStruct(self, name: win32more.Windows.Win32.Foundation.PWSTR, numFields: UInt32, fieldTypeNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetEnum(self, name: win32more.Windows.Win32.Foundation.PWSTR, baseType: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetParameterizedInterface(self, piid: Guid, numArgs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetParameterizedDelegate(self, piid: Guid, numArgs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LoadHintEnum = Int32
LoadDefault: win32more.Windows.Win32.System.WinRT.Metadata.LoadHintEnum = 0
LoadAlways: win32more.Windows.Win32.System.WinRT.Metadata.LoadHintEnum = 1
LoadSometimes: win32more.Windows.Win32.System.WinRT.Metadata.LoadHintEnum = 2
LoadNever: win32more.Windows.Win32.System.WinRT.Metadata.LoadHintEnum = 3
MergeFlags = Int32
MergeFlagsNone: win32more.Windows.Win32.System.WinRT.Metadata.MergeFlags = 0
MergeManifest: win32more.Windows.Win32.System.WinRT.Metadata.MergeFlags = 1
DropMemberRefCAs: win32more.Windows.Win32.System.WinRT.Metadata.MergeFlags = 2
NoDupCheck: win32more.Windows.Win32.System.WinRT.Metadata.MergeFlags = 4
MergeExportedTypes: win32more.Windows.Win32.System.WinRT.Metadata.MergeFlags = 8
NGenHintEnum = Int32
NGenDefault: win32more.Windows.Win32.System.WinRT.Metadata.NGenHintEnum = 0
NGenEager: win32more.Windows.Win32.System.WinRT.Metadata.NGenHintEnum = 1
NGenLazy: win32more.Windows.Win32.System.WinRT.Metadata.NGenHintEnum = 2
NGenNever: win32more.Windows.Win32.System.WinRT.Metadata.NGenHintEnum = 3
NativeTypeArrayFlags = Int32
ntaSizeParamIndexSpecified: win32more.Windows.Win32.System.WinRT.Metadata.NativeTypeArrayFlags = 1
ntaReserved: win32more.Windows.Win32.System.WinRT.Metadata.NativeTypeArrayFlags = 65534
class OSINFO(Structure):
    dwOSPlatformId: UInt32
    dwOSMajorVersion: UInt32
    dwOSMinorVersion: UInt32
ROPARAMIIDHANDLE = VoidPtr
ReplacesGeneralNumericDefines = Int32
IMAGE_DIRECTORY_ENTRY_COMHEADER: win32more.Windows.Win32.System.WinRT.Metadata.ReplacesGeneralNumericDefines = 14


make_ready(__name__)
