from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.System.Com
import Windows.Win32.System.GroupPolicy
import Windows.Win32.System.Ole
import Windows.Win32.System.Registry
import Windows.Win32.System.Variant
import Windows.Win32.System.Wmi
import Windows.Win32.UI.Controls
import Windows.Win32.UI.Shell
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
APPSTATE = Int32
ABSENT: APPSTATE = 0
ASSIGNED: APPSTATE = 1
PUBLISHED: APPSTATE = 2
GPM_USE_PDC: UInt32 = 0
GPM_USE_ANYDC: UInt32 = 1
GPM_DONOTUSE_W2KDC: UInt32 = 2
GPM_DONOT_VALIDATEDC: UInt32 = 1
GPM_MIGRATIONTABLE_ONLY: UInt32 = 1
GPM_PROCESS_SECURITY: UInt32 = 2
RSOP_NO_COMPUTER: UInt32 = 65536
RSOP_NO_USER: UInt32 = 131072
RSOP_PLANNING_ASSUME_SLOW_LINK: UInt32 = 1
RSOP_PLANNING_ASSUME_LOOPBACK_MERGE: UInt32 = 2
RSOP_PLANNING_ASSUME_LOOPBACK_REPLACE: UInt32 = 4
RSOP_PLANNING_ASSUME_USER_WQLFILTER_TRUE: UInt32 = 8
RSOP_PLANNING_ASSUME_COMP_WQLFILTER_TRUE: UInt32 = 16
PI_NOUI: UInt32 = 1
PI_APPLYPOLICY: UInt32 = 2
PT_TEMPORARY: UInt32 = 1
PT_ROAMING: UInt32 = 2
PT_MANDATORY: UInt32 = 4
PT_ROAMING_PREEXISTING: UInt32 = 8
RP_FORCE: UInt32 = 1
RP_SYNC: UInt32 = 2
GPC_BLOCK_POLICY: UInt32 = 1
GPO_FLAG_DISABLE: UInt32 = 1
GPO_FLAG_FORCE: UInt32 = 2
GPO_LIST_FLAG_MACHINE: UInt32 = 1
GPO_LIST_FLAG_SITEONLY: UInt32 = 2
GPO_LIST_FLAG_NO_WMIFILTERS: UInt32 = 4
GPO_LIST_FLAG_NO_SECURITYFILTERS: UInt32 = 8
GP_DLLNAME: String = 'DllName'
GP_ENABLEASYNCHRONOUSPROCESSING: String = 'EnableAsynchronousProcessing'
GP_MAXNOGPOLISTCHANGESINTERVAL: String = 'MaxNoGPOListChangesInterval'
GP_NOBACKGROUNDPOLICY: String = 'NoBackgroundPolicy'
GP_NOGPOLISTCHANGES: String = 'NoGPOListChanges'
GP_NOMACHINEPOLICY: String = 'NoMachinePolicy'
GP_NOSLOWLINK: String = 'NoSlowLink'
GP_NOTIFYLINKTRANSITION: String = 'NotifyLinkTransition'
GP_NOUSERPOLICY: String = 'NoUserPolicy'
GP_PERUSERLOCALSETTINGS: String = 'PerUserLocalSettings'
GP_PROCESSGROUPPOLICY: String = 'ProcessGroupPolicy'
GP_REQUIRESSUCCESSFULREGISTRY: String = 'RequiresSuccessfulRegistry'
GPO_INFO_FLAG_MACHINE: UInt32 = 1
GPO_INFO_FLAG_BACKGROUND: UInt32 = 16
GPO_INFO_FLAG_SLOWLINK: UInt32 = 32
GPO_INFO_FLAG_VERBOSE: UInt32 = 64
GPO_INFO_FLAG_NOCHANGES: UInt32 = 128
GPO_INFO_FLAG_LINKTRANSITION: UInt32 = 256
GPO_INFO_FLAG_LOGRSOP_TRANSITION: UInt32 = 512
GPO_INFO_FLAG_FORCED_REFRESH: UInt32 = 1024
GPO_INFO_FLAG_SAFEMODE_BOOT: UInt32 = 2048
GPO_INFO_FLAG_ASYNC_FOREGROUND: UInt32 = 4096
FLAG_NO_GPO_FILTER: UInt32 = 2147483648
FLAG_NO_CSE_INVOKE: UInt32 = 1073741824
FLAG_ASSUME_SLOW_LINK: UInt32 = 536870912
FLAG_LOOPBACK_MERGE: UInt32 = 268435456
FLAG_LOOPBACK_REPLACE: UInt32 = 134217728
FLAG_ASSUME_USER_WQLFILTER_TRUE: UInt32 = 67108864
FLAG_ASSUME_COMP_WQLFILTER_TRUE: UInt32 = 33554432
FLAG_PLANNING_MODE: UInt32 = 16777216
FLAG_NO_USER: UInt32 = 1
FLAG_NO_COMPUTER: UInt32 = 2
FLAG_FORCE_CREATENAMESPACE: UInt32 = 4
RSOP_USER_ACCESS_DENIED: UInt32 = 1
RSOP_COMPUTER_ACCESS_DENIED: UInt32 = 2
RSOP_TEMPNAMESPACE_EXISTS: UInt32 = 4
LOCALSTATE_ASSIGNED: UInt32 = 1
LOCALSTATE_PUBLISHED: UInt32 = 2
LOCALSTATE_UNINSTALL_UNMANAGED: UInt32 = 4
LOCALSTATE_POLICYREMOVE_ORPHAN: UInt32 = 8
LOCALSTATE_POLICYREMOVE_UNINSTALL: UInt32 = 16
LOCALSTATE_ORPHANED: UInt32 = 32
LOCALSTATE_UNINSTALLED: UInt32 = 64
MANAGED_APPS_USERAPPLICATIONS: UInt32 = 1
MANAGED_APPS_FROMCATEGORY: UInt32 = 2
MANAGED_APPS_INFOLEVEL_DEFAULT: UInt32 = 65536
MANAGED_APPTYPE_WINDOWSINSTALLER: UInt32 = 1
MANAGED_APPTYPE_SETUPEXE: UInt32 = 2
MANAGED_APPTYPE_UNSUPPORTED: UInt32 = 3
CLSID_GPESnapIn: Guid = Guid('{8fc0b734-a0e1-11d1-a7d3-0000f87571e3}')
NODEID_Machine: Guid = Guid('{8fc0b737-a0e1-11d1-a7d3-0000f87571e3}')
NODEID_MachineSWSettings: Guid = Guid('{8fc0b73a-a0e1-11d1-a7d3-0000f87571e3}')
NODEID_User: Guid = Guid('{8fc0b738-a0e1-11d1-a7d3-0000f87571e3}')
NODEID_UserSWSettings: Guid = Guid('{8fc0b73c-a0e1-11d1-a7d3-0000f87571e3}')
CLSID_GroupPolicyObject: Guid = Guid('{ea502722-a23d-11d1-a7d3-0000f87571e3}')
CLSID_RSOPSnapIn: Guid = Guid('{6dc3804b-7212-458d-adb0-9a07e2ae1fa2}')
NODEID_RSOPMachine: Guid = Guid('{bd4c1a2e-0b7a-4a62-a6b0-c0577539c97e}')
NODEID_RSOPMachineSWSettings: Guid = Guid('{6a76273e-eb8e-45db-94c5-25663a5f2c1a}')
NODEID_RSOPUser: Guid = Guid('{ab87364f-0cec-4cd8-9bf8-898f34628fb8}')
NODEID_RSOPUserSWSettings: Guid = Guid('{e52c5ce3-fd27-4402-84de-d9a5f2858910}')
GPO_SECTION_ROOT: UInt32 = 0
GPO_SECTION_USER: UInt32 = 1
GPO_SECTION_MACHINE: UInt32 = 2
GPO_OPEN_LOAD_REGISTRY: UInt32 = 1
GPO_OPEN_READ_ONLY: UInt32 = 2
GPO_OPTION_DISABLE_USER: UInt32 = 1
GPO_OPTION_DISABLE_MACHINE: UInt32 = 2
RSOP_INFO_FLAG_DIAGNOSTIC_MODE: UInt32 = 1
GPO_BROWSE_DISABLENEW: UInt32 = 1
GPO_BROWSE_NOCOMPUTERS: UInt32 = 2
GPO_BROWSE_NODSGPOS: UInt32 = 4
GPO_BROWSE_OPENBUTTON: UInt32 = 8
GPO_BROWSE_INITTOALL: UInt32 = 16
GPO_BROWSE_NOUSERGPOS: UInt32 = 32
GPO_BROWSE_SENDAPPLYONEDIT: UInt32 = 64
@winfunctype('USERENV.dll')
def RefreshPolicy(bMachine: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def RefreshPolicyEx(bMachine: Windows.Win32.Foundation.BOOL, dwOptions: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def EnterCriticalPolicySection(bMachine: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('USERENV.dll')
def LeaveCriticalPolicySection(hSection: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def RegisterGPNotification(hEvent: Windows.Win32.Foundation.HANDLE, bMachine: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def UnregisterGPNotification(hEvent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetGPOListA(hToken: Windows.Win32.Foundation.HANDLE, lpName: Windows.Win32.Foundation.PSTR, lpHostName: Windows.Win32.Foundation.PSTR, lpComputerName: Windows.Win32.Foundation.PSTR, dwFlags: UInt32, pGPOList: POINTER(POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetGPOListW(hToken: Windows.Win32.Foundation.HANDLE, lpName: Windows.Win32.Foundation.PWSTR, lpHostName: Windows.Win32.Foundation.PWSTR, lpComputerName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pGPOList: POINTER(POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def FreeGPOListA(pGPOList: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def FreeGPOListW(pGPOList: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetAppliedGPOListA(dwFlags: UInt32, pMachineName: Windows.Win32.Foundation.PSTR, pSidUser: Windows.Win32.Foundation.PSID, pGuidExtension: POINTER(Guid), ppGPOList: POINTER(POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTA_head))) -> UInt32: ...
@winfunctype('USERENV.dll')
def GetAppliedGPOListW(dwFlags: UInt32, pMachineName: Windows.Win32.Foundation.PWSTR, pSidUser: Windows.Win32.Foundation.PSID, pGuidExtension: POINTER(Guid), ppGPOList: POINTER(POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTW_head))) -> UInt32: ...
@winfunctype('USERENV.dll')
def ProcessGroupPolicyCompleted(extensionId: POINTER(Guid), pAsyncHandle: UIntPtr, dwStatus: UInt32) -> UInt32: ...
@winfunctype('USERENV.dll')
def ProcessGroupPolicyCompletedEx(extensionId: POINTER(Guid), pAsyncHandle: UIntPtr, dwStatus: UInt32, RsopStatus: Windows.Win32.Foundation.HRESULT) -> UInt32: ...
@winfunctype('USERENV.dll')
def RsopAccessCheckByType(pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, pPrincipalSelfSid: Windows.Win32.Foundation.PSID, pRsopToken: c_void_p, dwDesiredAccessMask: UInt32, pObjectTypeList: POINTER(Windows.Win32.Security.OBJECT_TYPE_LIST_head), ObjectTypeListLength: UInt32, pGenericMapping: POINTER(Windows.Win32.Security.GENERIC_MAPPING_head), pPrivilegeSet: POINTER(Windows.Win32.Security.PRIVILEGE_SET_head), pdwPrivilegeSetLength: POINTER(UInt32), pdwGrantedAccessMask: POINTER(UInt32), pbAccessStatus: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def RsopFileAccessCheck(pszFileName: Windows.Win32.Foundation.PWSTR, pRsopToken: c_void_p, dwDesiredAccessMask: UInt32, pdwGrantedAccessMask: POINTER(UInt32), pbAccessStatus: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def RsopSetPolicySettingStatus(dwFlags: UInt32, pServices: Windows.Win32.System.Wmi.IWbemServices_head, pSettingInstance: Windows.Win32.System.Wmi.IWbemClassObject_head, nInfo: UInt32, pStatus: POINTER(Windows.Win32.System.GroupPolicy.POLICYSETTINGSTATUSINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def RsopResetPolicySettingStatus(dwFlags: UInt32, pServices: Windows.Win32.System.Wmi.IWbemServices_head, pSettingInstance: Windows.Win32.System.Wmi.IWbemClassObject_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def GenerateGPNotification(bMachine: Windows.Win32.Foundation.BOOL, lpwszMgmtProduct: Windows.Win32.Foundation.PWSTR, dwMgmtProductOptions: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def InstallApplication(pInstallInfo: POINTER(Windows.Win32.System.GroupPolicy.INSTALLDATA_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def UninstallApplication(ProductCode: Windows.Win32.Foundation.PWSTR, dwStatus: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def CommandLineFromMsiDescriptor(Descriptor: Windows.Win32.Foundation.PWSTR, CommandLine: Windows.Win32.Foundation.PWSTR, CommandLineLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetManagedApplications(pCategory: POINTER(Guid), dwQueryFlags: UInt32, dwInfoLevel: UInt32, pdwApps: POINTER(UInt32), prgManagedApps: POINTER(POINTER(Windows.Win32.System.GroupPolicy.MANAGEDAPPLICATION_head))) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetLocalManagedApplications(bUserApps: Windows.Win32.Foundation.BOOL, pdwApps: POINTER(UInt32), prgLocalApps: POINTER(POINTER(Windows.Win32.System.GroupPolicy.LOCALMANAGEDAPPLICATION_head))) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetLocalManagedApplicationData(ProductCode: Windows.Win32.Foundation.PWSTR, DisplayName: POINTER(Windows.Win32.Foundation.PWSTR), SupportUrl: POINTER(Windows.Win32.Foundation.PWSTR)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def GetManagedApplicationCategories(dwReserved: UInt32, pAppCategory: POINTER(Windows.Win32.UI.Shell.APPCATEGORYINFOLIST_head)) -> UInt32: ...
@winfunctype('GPEDIT.dll')
def CreateGPOLink(lpGPO: Windows.Win32.Foundation.PWSTR, lpContainer: Windows.Win32.Foundation.PWSTR, fHighPriority: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('GPEDIT.dll')
def DeleteGPOLink(lpGPO: Windows.Win32.Foundation.PWSTR, lpContainer: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('GPEDIT.dll')
def DeleteAllGPOLinks(lpContainer: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('GPEDIT.dll')
def BrowseForGPO(lpBrowseInfo: POINTER(Windows.Win32.System.GroupPolicy.GPOBROWSEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('GPEDIT.dll')
def ImportRSoPData(lpNameSpace: Windows.Win32.Foundation.PWSTR, lpFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('GPEDIT.dll')
def ExportRSoPData(lpNameSpace: Windows.Win32.Foundation.PWSTR, lpFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class CriticalPolicySectionHandle(EasyCastStructure):
    Value: IntPtr
GPM = Guid('{f5694708-88fe-4b35-babf-e56162d5fbc8}')
GPMAsyncCancel = Guid('{372796a9-76ec-479d-ad6c-556318ed5f9d}')
GPMBackup = Guid('{ed1a54b8-5efa-482a-93c0-8ad86f0d68c3}')
GPMBackupCollection = Guid('{eb8f035b-70db-4a9f-9676-37c25994e9dc}')
GPMBackupDir = Guid('{fce4a59d-0f21-4afa-b859-e6d0c62cd10c}')
GPMBackupDirEx = Guid('{e8c0988a-cf03-4c5b-8be2-2aa9ad32aada}')
GPMBackupType = Int32
GPMBackupType_typeGPO: GPMBackupType = 0
GPMBackupType_typeStarterGPO: GPMBackupType = 1
GPMCSECollection = Guid('{cf92b828-2d44-4b61-b10a-b327afd42da8}')
GPMClientSideExtension = Guid('{c1a2e70e-659c-4b1a-940b-f88b0af9c8a4}')
GPMConstants = Guid('{3855e880-cd9e-4d0c-9eaf-1579283a1888}')
GPMDestinationOption = Int32
GPMDestinationOption_opDestinationSameAsSource: GPMDestinationOption = 0
GPMDestinationOption_opDestinationNone: GPMDestinationOption = 1
GPMDestinationOption_opDestinationByRelativeName: GPMDestinationOption = 2
GPMDestinationOption_opDestinationSet: GPMDestinationOption = 3
GPMDomain = Guid('{710901be-1050-4cb1-838a-c5cff259e183}')
GPMEntryType = Int32
GPMEntryType_typeUser: GPMEntryType = 0
GPMEntryType_typeComputer: GPMEntryType = 1
GPMEntryType_typeLocalGroup: GPMEntryType = 2
GPMEntryType_typeGlobalGroup: GPMEntryType = 3
GPMEntryType_typeUniversalGroup: GPMEntryType = 4
GPMEntryType_typeUNCPath: GPMEntryType = 5
GPMEntryType_typeUnknown: GPMEntryType = 6
GPMGPO = Guid('{d2ce2994-59b5-4064-b581-4d68486a16c4}')
GPMGPOCollection = Guid('{7a057325-832d-4de3-a41f-c780436a4e09}')
GPMGPOLink = Guid('{c1df9880-5303-42c6-8a3c-0488e1bf7364}')
GPMGPOLinksCollection = Guid('{f6ed581a-49a5-47e2-b771-fd8dc02b6259}')
GPMMapEntry = Guid('{8c975253-5431-4471-b35d-0626c928258a}')
GPMMapEntryCollection = Guid('{0cf75d5b-a3a1-4c55-b4fe-9e149c41f66d}')
GPMMigrationTable = Guid('{55af4043-2a06-4f72-abef-631b44079c76}')
GPMPermission = Guid('{5871a40a-e9c0-46ec-913e-944ef9225a94}')
GPMPermissionType = Int32
GPMPermissionType_permGPOApply: GPMPermissionType = 65536
GPMPermissionType_permGPORead: GPMPermissionType = 65792
GPMPermissionType_permGPOEdit: GPMPermissionType = 65793
GPMPermissionType_permGPOEditSecurityAndDelete: GPMPermissionType = 65794
GPMPermissionType_permGPOCustom: GPMPermissionType = 65795
GPMPermissionType_permWMIFilterEdit: GPMPermissionType = 131072
GPMPermissionType_permWMIFilterFullControl: GPMPermissionType = 131073
GPMPermissionType_permWMIFilterCustom: GPMPermissionType = 131074
GPMPermissionType_permSOMLink: GPMPermissionType = 1835008
GPMPermissionType_permSOMLogging: GPMPermissionType = 1573120
GPMPermissionType_permSOMPlanning: GPMPermissionType = 1573376
GPMPermissionType_permSOMWMICreate: GPMPermissionType = 1049344
GPMPermissionType_permSOMWMIFullControl: GPMPermissionType = 1049345
GPMPermissionType_permSOMGPOCreate: GPMPermissionType = 1049600
GPMPermissionType_permStarterGPORead: GPMPermissionType = 197888
GPMPermissionType_permStarterGPOEdit: GPMPermissionType = 197889
GPMPermissionType_permStarterGPOFullControl: GPMPermissionType = 197890
GPMPermissionType_permStarterGPOCustom: GPMPermissionType = 197891
GPMPermissionType_permSOMStarterGPOCreate: GPMPermissionType = 1049856
GPMRSOP = Guid('{489b0caf-9ec2-4eb7-91f5-b6f71d43da8c}')
GPMRSOPMode = Int32
GPMRSOPMode_rsopUnknown: GPMRSOPMode = 0
GPMRSOPMode_rsopPlanning: GPMRSOPMode = 1
GPMRSOPMode_rsopLogging: GPMRSOPMode = 2
GPMReportType = Int32
GPMReportType_repXML: GPMReportType = 0
GPMReportType_repHTML: GPMReportType = 1
GPMReportType_repInfraXML: GPMReportType = 2
GPMReportType_repInfraRefreshXML: GPMReportType = 3
GPMReportType_repClientHealthXML: GPMReportType = 4
GPMReportType_repClientHealthRefreshXML: GPMReportType = 5
GPMReportingOptions = Int32
GPMReportingOptions_opReportLegacy: GPMReportingOptions = 0
GPMReportingOptions_opReportComments: GPMReportingOptions = 1
GPMResult = Guid('{92101ac0-9287-4206-a3b2-4bdb73d225f6}')
GPMSOM = Guid('{32d93fac-450e-44cf-829c-8b22ff6bdae1}')
GPMSOMCollection = Guid('{24c1f147-3720-4f5b-a9c3-06b4e4f931d2}')
GPMSOMType = Int32
GPMSOMType_somSite: GPMSOMType = 0
GPMSOMType_somDomain: GPMSOMType = 1
GPMSOMType_somOU: GPMSOMType = 2
GPMSearchCriteria = Guid('{17aaca26-5ce0-44fa-8cc0-5259e6483566}')
GPMSearchOperation = Int32
GPMSearchOperation_opEquals: GPMSearchOperation = 0
GPMSearchOperation_opContains: GPMSearchOperation = 1
GPMSearchOperation_opNotContains: GPMSearchOperation = 2
GPMSearchOperation_opNotEquals: GPMSearchOperation = 3
GPMSearchProperty = Int32
GPMSearchProperty_gpoPermissions: GPMSearchProperty = 0
GPMSearchProperty_gpoEffectivePermissions: GPMSearchProperty = 1
GPMSearchProperty_gpoDisplayName: GPMSearchProperty = 2
GPMSearchProperty_gpoWMIFilter: GPMSearchProperty = 3
GPMSearchProperty_gpoID: GPMSearchProperty = 4
GPMSearchProperty_gpoComputerExtensions: GPMSearchProperty = 5
GPMSearchProperty_gpoUserExtensions: GPMSearchProperty = 6
GPMSearchProperty_somLinks: GPMSearchProperty = 7
GPMSearchProperty_gpoDomain: GPMSearchProperty = 8
GPMSearchProperty_backupMostRecent: GPMSearchProperty = 9
GPMSearchProperty_starterGPOPermissions: GPMSearchProperty = 10
GPMSearchProperty_starterGPOEffectivePermissions: GPMSearchProperty = 11
GPMSearchProperty_starterGPODisplayName: GPMSearchProperty = 12
GPMSearchProperty_starterGPOID: GPMSearchProperty = 13
GPMSearchProperty_starterGPODomain: GPMSearchProperty = 14
GPMSecurityInfo = Guid('{547a5e8f-9162-4516-a4df-9ddb9686d846}')
GPMSitesContainer = Guid('{229f5c42-852c-4b30-945f-c522be9bd386}')
GPMStarterGPOBackup = Guid('{389e400a-d8ef-455b-a861-5f9ca34a6a02}')
GPMStarterGPOBackupCollection = Guid('{e75ea59d-1aeb-4cb5-a78a-281daa582406}')
GPMStarterGPOCollection = Guid('{82f8aa8b-49ba-43b2-956e-3397f9b94c3a}')
GPMStarterGPOType = Int32
GPMStarterGPOType_typeSystem: GPMStarterGPOType = 0
GPMStarterGPOType_typeCustom: GPMStarterGPOType = 1
GPMStatusMessage = Guid('{4b77cc94-d255-409b-bc62-370881715a19}')
GPMStatusMsgCollection = Guid('{2824e4be-4bcc-4cac-9e60-0e3ed7f12496}')
GPMTemplate = Guid('{ecf1d454-71da-4e2f-a8c0-8185465911d9}')
GPMTrustee = Guid('{c54a700d-19b6-4211-bcb0-e8e2475e471e}')
GPMWMIFilter = Guid('{626745d8-0dea-4062-bf60-cfc5b1ca1286}')
GPMWMIFilterCollection = Guid('{74dc6d28-e820-47d6-a0b8-f08d93d7fa33}')
class GPOBROWSEINFO(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    lpTitle: Windows.Win32.Foundation.PWSTR
    lpInitialOU: Windows.Win32.Foundation.PWSTR
    lpDSPath: Windows.Win32.Foundation.PWSTR
    dwDSPathSize: UInt32
    lpName: Windows.Win32.Foundation.PWSTR
    dwNameSize: UInt32
    gpoType: Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECT_TYPE
    gpoHint: Windows.Win32.System.GroupPolicy.GROUP_POLICY_HINT_TYPE
GPO_LINK = Int32
GPO_LINK_GPLinkUnknown: GPO_LINK = 0
GPO_LINK_GPLinkMachine: GPO_LINK = 1
GPO_LINK_GPLinkSite: GPO_LINK = 2
GPO_LINK_GPLinkDomain: GPO_LINK = 3
GPO_LINK_GPLinkOrganizationalUnit: GPO_LINK = 4
GROUP_POLICY_HINT_TYPE = Int32
GROUP_POLICY_HINT_TYPE_GPHintUnknown: GROUP_POLICY_HINT_TYPE = 0
GROUP_POLICY_HINT_TYPE_GPHintMachine: GROUP_POLICY_HINT_TYPE = 1
GROUP_POLICY_HINT_TYPE_GPHintSite: GROUP_POLICY_HINT_TYPE = 2
GROUP_POLICY_HINT_TYPE_GPHintDomain: GROUP_POLICY_HINT_TYPE = 3
GROUP_POLICY_HINT_TYPE_GPHintOrganizationalUnit: GROUP_POLICY_HINT_TYPE = 4
class GROUP_POLICY_OBJECTA(EasyCastStructure):
    dwOptions: UInt32
    dwVersion: UInt32
    lpDSPath: Windows.Win32.Foundation.PSTR
    lpFileSysPath: Windows.Win32.Foundation.PSTR
    lpDisplayName: Windows.Win32.Foundation.PSTR
    szGPOName: Windows.Win32.Foundation.CHAR * 50
    GPOLink: Windows.Win32.System.GroupPolicy.GPO_LINK
    lParam: Windows.Win32.Foundation.LPARAM
    pNext: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTA_head)
    pPrev: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTA_head)
    lpExtensions: Windows.Win32.Foundation.PSTR
    lParam2: Windows.Win32.Foundation.LPARAM
    lpLink: Windows.Win32.Foundation.PSTR
class GROUP_POLICY_OBJECTW(EasyCastStructure):
    dwOptions: UInt32
    dwVersion: UInt32
    lpDSPath: Windows.Win32.Foundation.PWSTR
    lpFileSysPath: Windows.Win32.Foundation.PWSTR
    lpDisplayName: Windows.Win32.Foundation.PWSTR
    szGPOName: Char * 50
    GPOLink: Windows.Win32.System.GroupPolicy.GPO_LINK
    lParam: Windows.Win32.Foundation.LPARAM
    pNext: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTW_head)
    pPrev: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTW_head)
    lpExtensions: Windows.Win32.Foundation.PWSTR
    lParam2: Windows.Win32.Foundation.LPARAM
    lpLink: Windows.Win32.Foundation.PWSTR
GROUP_POLICY_OBJECT_TYPE = Int32
GROUP_POLICY_OBJECT_TYPE_GPOTypeLocal: GROUP_POLICY_OBJECT_TYPE = 0
GROUP_POLICY_OBJECT_TYPE_GPOTypeRemote: GROUP_POLICY_OBJECT_TYPE = 1
GROUP_POLICY_OBJECT_TYPE_GPOTypeDS: GROUP_POLICY_OBJECT_TYPE = 2
GROUP_POLICY_OBJECT_TYPE_GPOTypeLocalUser: GROUP_POLICY_OBJECT_TYPE = 3
GROUP_POLICY_OBJECT_TYPE_GPOTypeLocalGroup: GROUP_POLICY_OBJECT_TYPE = 4
class IGPEInformation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8fc0b735-a0e1-11d1-a7d3-0000f87571e3}')
    @commethod(3)
    def GetName(self, pszName: Windows.Win32.Foundation.PWSTR, cchMaxLength: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDisplayName(self, pszName: Windows.Win32.Foundation.PWSTR, cchMaxLength: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRegistryKey(self, dwSection: UInt32, hKey: POINTER(Windows.Win32.System.Registry.HKEY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDSPath(self, dwSection: UInt32, pszPath: Windows.Win32.Foundation.PWSTR, cchMaxPath: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFileSysPath(self, dwSection: UInt32, pszPath: Windows.Win32.Foundation.PWSTR, cchMaxPath: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOptions(self, dwOptions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetType(self, gpoType: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetHint(self, gpHint: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_HINT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def PolicyChanged(self, bMachine: Windows.Win32.Foundation.BOOL, bAdd: Windows.Win32.Foundation.BOOL, pGuidExtension: POINTER(Guid), pGuidSnapin: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPM(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f5fae809-3bd6-4da9-a65e-17665b41d763}')
    @commethod(7)
    def GetDomain(self, bstrDomain: Windows.Win32.Foundation.BSTR, bstrDomainController: Windows.Win32.Foundation.BSTR, lDCFlags: Int32, pIGPMDomain: POINTER(Windows.Win32.System.GroupPolicy.IGPMDomain_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBackupDir(self, bstrBackupDir: Windows.Win32.Foundation.BSTR, pIGPMBackupDir: POINTER(Windows.Win32.System.GroupPolicy.IGPMBackupDir_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSitesContainer(self, bstrForest: Windows.Win32.Foundation.BSTR, bstrDomain: Windows.Win32.Foundation.BSTR, bstrDomainController: Windows.Win32.Foundation.BSTR, lDCFlags: Int32, ppIGPMSitesContainer: POINTER(Windows.Win32.System.GroupPolicy.IGPMSitesContainer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRSOP(self, gpmRSoPMode: Windows.Win32.System.GroupPolicy.GPMRSOPMode, bstrNamespace: Windows.Win32.Foundation.BSTR, lFlags: Int32, ppIGPMRSOP: POINTER(Windows.Win32.System.GroupPolicy.IGPMRSOP_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreatePermission(self, bstrTrustee: Windows.Win32.Foundation.BSTR, perm: Windows.Win32.System.GroupPolicy.GPMPermissionType, bInheritable: Windows.Win32.Foundation.VARIANT_BOOL, ppPerm: POINTER(Windows.Win32.System.GroupPolicy.IGPMPermission_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateSearchCriteria(self, ppIGPMSearchCriteria: POINTER(Windows.Win32.System.GroupPolicy.IGPMSearchCriteria_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateTrustee(self, bstrTrustee: Windows.Win32.Foundation.BSTR, ppIGPMTrustee: POINTER(Windows.Win32.System.GroupPolicy.IGPMTrustee_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetClientSideExtensions(self, ppIGPMCSECollection: POINTER(Windows.Win32.System.GroupPolicy.IGPMCSECollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetConstants(self, ppIGPMConstants: POINTER(Windows.Win32.System.GroupPolicy.IGPMConstants_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetMigrationTable(self, bstrMigrationTablePath: Windows.Win32.Foundation.BSTR, ppMigrationTable: POINTER(Windows.Win32.System.GroupPolicy.IGPMMigrationTable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateMigrationTable(self, ppMigrationTable: POINTER(Windows.Win32.System.GroupPolicy.IGPMMigrationTable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def InitializeReporting(self, bstrAdmPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IGPM2(ComPtr):
    extends: Windows.Win32.System.GroupPolicy.IGPM
    _iid_ = Guid('{00238f8a-3d86-41ac-8f5e-06a6638a634a}')
    @commethod(19)
    def GetBackupDirEx(self, bstrBackupDir: Windows.Win32.Foundation.BSTR, backupDirType: Windows.Win32.System.GroupPolicy.GPMBackupType, ppIGPMBackupDirEx: POINTER(Windows.Win32.System.GroupPolicy.IGPMBackupDirEx_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def InitializeReportingEx(self, bstrAdmPath: Windows.Win32.Foundation.BSTR, reportingOptions: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMAsyncCancel(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ddc67754-be67-4541-8166-f48166868c9c}')
    @commethod(7)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMAsyncProgress(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6aac29f8-5948-4324-bf70-423818942dbc}')
    @commethod(7)
    def Status(self, lProgressNumerator: Int32, lProgressDenominator: Int32, hrStatus: Windows.Win32.Foundation.HRESULT, pResult: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMStatusMsgCollection: Windows.Win32.System.GroupPolicy.IGPMStatusMsgCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMBackup(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d8a16a35-3b0d-416b-8d02-4df6f95a7119}')
    @commethod(7)
    def get_ID(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GPOID(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_GPODomain(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_GPODisplayName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Timestamp(self, pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Comment(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_BackupDir(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GenerateReport(self, gpmReportType: Windows.Win32.System.GroupPolicy.GPMReportType, pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GenerateReportToFile(self, gpmReportType: Windows.Win32.System.GroupPolicy.GPMReportType, bstrTargetFilePath: Windows.Win32.Foundation.BSTR, ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMBackupCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c786fc0f-26d8-4bab-a745-39ca7e800cac}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppIGPMBackup: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMBackupDir(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b1568bed-0a93-4acc-810f-afe7081019b9}')
    @commethod(7)
    def get_BackupDirectory(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBackup(self, bstrID: Windows.Win32.Foundation.BSTR, ppBackup: POINTER(Windows.Win32.System.GroupPolicy.IGPMBackup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SearchBackups(self, pIGPMSearchCriteria: Windows.Win32.System.GroupPolicy.IGPMSearchCriteria_head, ppIGPMBackupCollection: POINTER(Windows.Win32.System.GroupPolicy.IGPMBackupCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMBackupDirEx(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f8dc55ed-3ba0-4864-aad4-d365189ee1d5}')
    @commethod(7)
    def get_BackupDir(self, pbstrBackupDir: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_BackupType(self, pgpmBackupType: POINTER(Windows.Win32.System.GroupPolicy.GPMBackupType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetBackup(self, bstrID: Windows.Win32.Foundation.BSTR, pvarBackup: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SearchBackups(self, pIGPMSearchCriteria: Windows.Win32.System.GroupPolicy.IGPMSearchCriteria_head, pvarBackupCollection: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMCSECollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2e52a97d-0a4a-4a6f-85db-201622455da0}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppIGPMCSEs: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMClientSideExtension(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{69da7488-b8db-415e-9266-901be4d49928}')
    @commethod(7)
    def get_ID(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DisplayName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsUserEnabled(self, pvbEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsComputerEnabled(self, pvbEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMConstants(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{50ef73e6-d35c-4c8d-be63-7ea5d2aac5c4}')
    @commethod(7)
    def get_PermGPOApply(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_PermGPORead(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PermGPOEdit(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PermGPOEditSecurityAndDelete(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PermGPOCustom(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_PermWMIFilterEdit(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_PermWMIFilterFullControl(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_PermWMIFilterCustom(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_PermSOMLink(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_PermSOMLogging(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_PermSOMPlanning(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_PermSOMGPOCreate(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_PermSOMWMICreate(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_PermSOMWMIFullControl(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_SearchPropertyGPOPermissions(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_SearchPropertyGPOEffectivePermissions(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_SearchPropertyGPODisplayName(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_SearchPropertyGPOWMIFilter(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_SearchPropertyGPOID(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_SearchPropertyGPOComputerExtensions(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_SearchPropertyGPOUserExtensions(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_SearchPropertySOMLinks(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_SearchPropertyGPODomain(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_SearchPropertyBackupMostRecent(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_SearchOpEquals(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchOperation)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_SearchOpContains(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchOperation)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_SearchOpNotContains(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchOperation)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_SearchOpNotEquals(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchOperation)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_UsePDC(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_UseAnyDC(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_DoNotUseW2KDC(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_SOMSite(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSOMType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_SOMDomain(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSOMType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_SOMOU(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSOMType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_SecurityFlags(self, vbOwner: Windows.Win32.Foundation.VARIANT_BOOL, vbGroup: Windows.Win32.Foundation.VARIANT_BOOL, vbDACL: Windows.Win32.Foundation.VARIANT_BOOL, vbSACL: Windows.Win32.Foundation.VARIANT_BOOL, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_DoNotValidateDC(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_ReportHTML(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMReportType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_ReportXML(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMReportType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_RSOPModeUnknown(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMRSOPMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_RSOPModePlanning(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMRSOPMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_RSOPModeLogging(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMRSOPMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_EntryTypeUser(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMEntryType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_EntryTypeComputer(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMEntryType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_EntryTypeLocalGroup(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMEntryType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_EntryTypeGlobalGroup(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMEntryType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_EntryTypeUniversalGroup(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMEntryType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_EntryTypeUNCPath(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMEntryType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def get_EntryTypeUnknown(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMEntryType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_DestinationOptionSameAsSource(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMDestinationOption)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def get_DestinationOptionNone(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMDestinationOption)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_DestinationOptionByRelativeName(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMDestinationOption)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def get_DestinationOptionSet(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMDestinationOption)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_MigrationTableOnly(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def get_ProcessSecurity(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def get_RsopLoggingNoComputer(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def get_RsopLoggingNoUser(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def get_RsopPlanningAssumeSlowLink(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def get_RsopPlanningLoopbackOption(self, vbMerge: Windows.Win32.Foundation.VARIANT_BOOL, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_RsopPlanningAssumeUserWQLFilterTrue(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def get_RsopPlanningAssumeCompWQLFilterTrue(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMConstants2(ComPtr):
    extends: Windows.Win32.System.GroupPolicy.IGPMConstants
    _iid_ = Guid('{05ae21b0-ac09-4032-a26f-9e7da786dc19}')
    @commethod(67)
    def get_BackupTypeGPO(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMBackupType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def get_BackupTypeStarterGPO(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMBackupType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_StarterGPOTypeSystem(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMStarterGPOType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def get_StarterGPOTypeCustom(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMStarterGPOType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def get_SearchPropertyStarterGPOPermissions(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def get_SearchPropertyStarterGPOEffectivePermissions(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def get_SearchPropertyStarterGPODisplayName(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def get_SearchPropertyStarterGPOID(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def get_SearchPropertyStarterGPODomain(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSearchProperty)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def get_PermStarterGPORead(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def get_PermStarterGPOEdit(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def get_PermStarterGPOFullControl(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def get_PermStarterGPOCustom(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def get_ReportLegacy(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMReportingOptions)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def get_ReportComments(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMReportingOptions)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMDomain(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6b21cc14-5a00-4f44-a738-feec8a94c7e3}')
    @commethod(7)
    def get_DomainController(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Domain(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateGPO(self, ppNewGPO: POINTER(Windows.Win32.System.GroupPolicy.IGPMGPO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetGPO(self, bstrGuid: Windows.Win32.Foundation.BSTR, ppGPO: POINTER(Windows.Win32.System.GroupPolicy.IGPMGPO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SearchGPOs(self, pIGPMSearchCriteria: Windows.Win32.System.GroupPolicy.IGPMSearchCriteria_head, ppIGPMGPOCollection: POINTER(Windows.Win32.System.GroupPolicy.IGPMGPOCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RestoreGPO(self, pIGPMBackup: Windows.Win32.System.GroupPolicy.IGPMBackup_head, lDCFlags: Int32, pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSOM(self, bstrPath: Windows.Win32.Foundation.BSTR, ppSOM: POINTER(Windows.Win32.System.GroupPolicy.IGPMSOM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SearchSOMs(self, pIGPMSearchCriteria: Windows.Win32.System.GroupPolicy.IGPMSearchCriteria_head, ppIGPMSOMCollection: POINTER(Windows.Win32.System.GroupPolicy.IGPMSOMCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetWMIFilter(self, bstrPath: Windows.Win32.Foundation.BSTR, ppWMIFilter: POINTER(Windows.Win32.System.GroupPolicy.IGPMWMIFilter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SearchWMIFilters(self, pIGPMSearchCriteria: Windows.Win32.System.GroupPolicy.IGPMSearchCriteria_head, ppIGPMWMIFilterCollection: POINTER(Windows.Win32.System.GroupPolicy.IGPMWMIFilterCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMDomain2(ComPtr):
    extends: Windows.Win32.System.GroupPolicy.IGPMDomain
    _iid_ = Guid('{7ca6bb8b-f1eb-490a-938d-3c4e51c768e6}')
    @commethod(17)
    def CreateStarterGPO(self, ppnewTemplate: POINTER(Windows.Win32.System.GroupPolicy.IGPMStarterGPO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateGPOFromStarterGPO(self, pGPOTemplate: Windows.Win32.System.GroupPolicy.IGPMStarterGPO_head, ppnewGPO: POINTER(Windows.Win32.System.GroupPolicy.IGPMGPO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetStarterGPO(self, bstrGuid: Windows.Win32.Foundation.BSTR, ppTemplate: POINTER(Windows.Win32.System.GroupPolicy.IGPMStarterGPO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SearchStarterGPOs(self, pIGPMSearchCriteria: Windows.Win32.System.GroupPolicy.IGPMSearchCriteria_head, ppIGPMTemplateCollection: POINTER(Windows.Win32.System.GroupPolicy.IGPMStarterGPOCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def LoadStarterGPO(self, bstrLoadFile: Windows.Win32.Foundation.BSTR, bOverwrite: Windows.Win32.Foundation.VARIANT_BOOL, pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def RestoreStarterGPO(self, pIGPMTmplBackup: Windows.Win32.System.GroupPolicy.IGPMStarterGPOBackup_head, pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMDomain3(ComPtr):
    extends: Windows.Win32.System.GroupPolicy.IGPMDomain2
    _iid_ = Guid('{0077fdfe-88c7-4acf-a11d-d10a7c310a03}')
    @commethod(23)
    def GenerateReport(self, gpmReportType: Windows.Win32.System.GroupPolicy.GPMReportType, pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_InfrastructureDC(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_InfrastructureDC(self, newVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_InfrastructureFlags(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMGPO(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{58cc4352-1ca3-48e5-9864-1da4d6e0d60f}')
    @commethod(7)
    def get_DisplayName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_DisplayName(self, newVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Path(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ID(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DomainName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CreationTime(self, pDate: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ModificationTime(self, pDate: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_UserDSVersionNumber(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ComputerDSVersionNumber(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_UserSysvolVersionNumber(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ComputerSysvolVersionNumber(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetWMIFilter(self, ppIGPMWMIFilter: POINTER(Windows.Win32.System.GroupPolicy.IGPMWMIFilter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetWMIFilter(self, pIGPMWMIFilter: Windows.Win32.System.GroupPolicy.IGPMWMIFilter_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetUserEnabled(self, vbEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetComputerEnabled(self, vbEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def IsUserEnabled(self, pvbEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def IsComputerEnabled(self, pvbEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetSecurityInfo(self, ppSecurityInfo: POINTER(Windows.Win32.System.GroupPolicy.IGPMSecurityInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetSecurityInfo(self, pSecurityInfo: Windows.Win32.System.GroupPolicy.IGPMSecurityInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Backup(self, bstrBackupDir: Windows.Win32.Foundation.BSTR, bstrComment: Windows.Win32.Foundation.BSTR, pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def Import(self, lFlags: Int32, pIGPMBackup: Windows.Win32.System.GroupPolicy.IGPMBackup_head, pvarMigrationTable: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GenerateReport(self, gpmReportType: Windows.Win32.System.GroupPolicy.GPMReportType, pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GenerateReportToFile(self, gpmReportType: Windows.Win32.System.GroupPolicy.GPMReportType, bstrTargetFilePath: Windows.Win32.Foundation.BSTR, ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CopyTo(self, lFlags: Int32, pIGPMDomain: Windows.Win32.System.GroupPolicy.IGPMDomain_head, pvarNewDisplayName: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarMigrationTable: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetSecurityDescriptor(self, lFlags: Int32, pSD: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetSecurityDescriptor(self, lFlags: Int32, ppSD: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def IsACLConsistent(self, pvbConsistent: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def MakeACLConsistent(self) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMGPO2(ComPtr):
    extends: Windows.Win32.System.GroupPolicy.IGPMGPO
    _iid_ = Guid('{8a66a210-b78b-4d99-88e2-c306a817c925}')
    @commethod(36)
    def get_Description(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_Description(self, newVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMGPO3(ComPtr):
    extends: Windows.Win32.System.GroupPolicy.IGPMGPO2
    _iid_ = Guid('{7cf123a1-f94a-4112-bfae-6aa1db9cb248}')
    @commethod(38)
    def get_InfrastructureDC(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_InfrastructureDC(self, newVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_InfrastructureFlags(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMGPOCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f0f0d5cf-70ca-4c39-9e29-b642f8726c01}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppIGPMGPOs: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMGPOLink(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{434b99bd-5de7-478a-809c-c251721df70c}')
    @commethod(7)
    def get_GPOID(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GPODomain(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Enabled(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Enabled(self, newVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Enforced(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Enforced(self, newVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_SOMLinkOrder(self, lVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_SOM(self, ppIGPMSOM: POINTER(Windows.Win32.System.GroupPolicy.IGPMSOM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMGPOLinksCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{189d7b68-16bd-4d0d-a2ec-2e6aa2288c7f}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppIGPMLinks: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMMapEntry(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8e79ad06-2381-4444-be4c-ff693e6e6f2b}')
    @commethod(7)
    def get_Source(self, pbstrSource: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Destination(self, pbstrDestination: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DestinationOption(self, pgpmDestOption: POINTER(Windows.Win32.System.GroupPolicy.GPMDestinationOption)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_EntryType(self, pgpmEntryType: POINTER(Windows.Win32.System.GroupPolicy.GPMEntryType)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMMapEntryCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bb0bf49b-e53f-443f-b807-8be22bfb6d42}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, pVal: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMMigrationTable(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{48f823b1-efaf-470b-b6ed-40d14ee1a4ec}')
    @commethod(7)
    def Save(self, bstrMigrationTablePath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Add(self, lFlags: Int32, var: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddEntry(self, bstrSource: Windows.Win32.Foundation.BSTR, gpmEntryType: Windows.Win32.System.GroupPolicy.GPMEntryType, pvarDestination: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppEntry: POINTER(Windows.Win32.System.GroupPolicy.IGPMMapEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetEntry(self, bstrSource: Windows.Win32.Foundation.BSTR, ppEntry: POINTER(Windows.Win32.System.GroupPolicy.IGPMMapEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DeleteEntry(self, bstrSource: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UpdateDestination(self, bstrSource: Windows.Win32.Foundation.BSTR, pvarDestination: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppEntry: POINTER(Windows.Win32.System.GroupPolicy.IGPMMapEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Validate(self, ppResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetEntries(self, ppEntries: POINTER(Windows.Win32.System.GroupPolicy.IGPMMapEntryCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMPermission(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{35ebca40-e1a1-4a02-8905-d79416fb464a}')
    @commethod(7)
    def get_Inherited(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Inheritable(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Denied(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Permission(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMPermissionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Trustee(self, ppIGPMTrustee: POINTER(Windows.Win32.System.GroupPolicy.IGPMTrustee_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMRSOP(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{49ed785a-3237-4ff2-b1f0-fdf5a8d5a1ee}')
    @commethod(7)
    def get_Mode(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMRSOPMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Namespace(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_LoggingComputer(self, bstrVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_LoggingComputer(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_LoggingUser(self, bstrVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_LoggingUser(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_LoggingFlags(self, lVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_LoggingFlags(self, lVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_PlanningFlags(self, lVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_PlanningFlags(self, lVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_PlanningDomainController(self, bstrVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_PlanningDomainController(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_PlanningSiteName(self, bstrVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_PlanningSiteName(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_PlanningUser(self, bstrVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_PlanningUser(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_PlanningUserSOM(self, bstrVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_PlanningUserSOM(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_PlanningUserWMIFilters(self, varVal: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_PlanningUserWMIFilters(self, varVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_PlanningUserSecurityGroups(self, varVal: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_PlanningUserSecurityGroups(self, varVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_PlanningComputer(self, bstrVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_PlanningComputer(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_PlanningComputerSOM(self, bstrVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_PlanningComputerSOM(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_PlanningComputerWMIFilters(self, varVal: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_PlanningComputerWMIFilters(self, varVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_PlanningComputerSecurityGroups(self, varVal: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_PlanningComputerSecurityGroups(self, varVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def LoggingEnumerateUsers(self, varVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def CreateQueryResults(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def ReleaseQueryResults(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GenerateReport(self, gpmReportType: Windows.Win32.System.GroupPolicy.GPMReportType, pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GenerateReportToFile(self, gpmReportType: Windows.Win32.System.GroupPolicy.GPMReportType, bstrTargetFilePath: Windows.Win32.Foundation.BSTR, ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMResult(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{86dff7e9-f76f-42ab-9570-cebc6be8a52d}')
    @commethod(7)
    def get_Status(self, ppIGPMStatusMsgCollection: POINTER(Windows.Win32.System.GroupPolicy.IGPMStatusMsgCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Result(self, pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OverallStatus(self) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMSOM(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c0a7f09e-05a1-4f0c-8158-9e5c33684f6b}')
    @commethod(7)
    def get_GPOInheritanceBlocked(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_GPOInheritanceBlocked(self, newVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Path(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateGPOLink(self, lLinkPos: Int32, pGPO: Windows.Win32.System.GroupPolicy.IGPMGPO_head, ppNewGPOLink: POINTER(Windows.Win32.System.GroupPolicy.IGPMGPOLink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Type(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMSOMType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetGPOLinks(self, ppGPOLinks: POINTER(Windows.Win32.System.GroupPolicy.IGPMGPOLinksCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetInheritedGPOLinks(self, ppGPOLinks: POINTER(Windows.Win32.System.GroupPolicy.IGPMGPOLinksCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetSecurityInfo(self, ppSecurityInfo: POINTER(Windows.Win32.System.GroupPolicy.IGPMSecurityInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetSecurityInfo(self, pSecurityInfo: Windows.Win32.System.GroupPolicy.IGPMSecurityInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMSOMCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{adc1688e-00e4-4495-abba-bed200df0cab}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppIGPMSOM: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMSearchCriteria(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d6f11c42-829b-48d4-83f5-3615b67dfc22}')
    @commethod(7)
    def Add(self, searchProperty: Windows.Win32.System.GroupPolicy.GPMSearchProperty, searchOperation: Windows.Win32.System.GroupPolicy.GPMSearchOperation, varValue: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMSecurityInfo(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b6c31ed4-1c93-4d3e-ae84-eb6d61161b60}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnum: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pPerm: Windows.Win32.System.GroupPolicy.IGPMPermission_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, pPerm: Windows.Win32.System.GroupPolicy.IGPMPermission_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveTrustee(self, bstrTrustee: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMSitesContainer(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4725a899-2782-4d27-a6bb-d499246ffd72}')
    @commethod(7)
    def get_DomainController(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Domain(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Forest(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSite(self, bstrSiteName: Windows.Win32.Foundation.BSTR, ppSOM: POINTER(Windows.Win32.System.GroupPolicy.IGPMSOM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SearchSites(self, pIGPMSearchCriteria: Windows.Win32.System.GroupPolicy.IGPMSearchCriteria_head, ppIGPMSOMCollection: POINTER(Windows.Win32.System.GroupPolicy.IGPMSOMCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMStarterGPO(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dfc3f61b-8880-4490-9337-d29c7ba8c2f0}')
    @commethod(7)
    def get_DisplayName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_DisplayName(self, newVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, newVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Author(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Product(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CreationTime(self, pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ID(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ModifiedTime(self, pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Type(self, pVal: POINTER(Windows.Win32.System.GroupPolicy.GPMStarterGPOType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ComputerVersion(self, pVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_UserVersion(self, pVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_StarterGPOVersion(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Save(self, bstrSaveFile: Windows.Win32.Foundation.BSTR, bOverwrite: Windows.Win32.Foundation.VARIANT_BOOL, bSaveAsSystem: Windows.Win32.Foundation.VARIANT_BOOL, bstrLanguage: POINTER(Windows.Win32.System.Variant.VARIANT_head), bstrAuthor: POINTER(Windows.Win32.System.Variant.VARIANT_head), bstrProduct: POINTER(Windows.Win32.System.Variant.VARIANT_head), bstrUniqueID: POINTER(Windows.Win32.System.Variant.VARIANT_head), bstrVersion: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Backup(self, bstrBackupDir: Windows.Win32.Foundation.BSTR, bstrComment: Windows.Win32.Foundation.BSTR, pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CopyTo(self, pvarNewDisplayName: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GenerateReport(self, gpmReportType: Windows.Win32.System.GroupPolicy.GPMReportType, pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GenerateReportToFile(self, gpmReportType: Windows.Win32.System.GroupPolicy.GPMReportType, bstrTargetFilePath: Windows.Win32.Foundation.BSTR, ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetSecurityInfo(self, ppSecurityInfo: POINTER(Windows.Win32.System.GroupPolicy.IGPMSecurityInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetSecurityInfo(self, pSecurityInfo: Windows.Win32.System.GroupPolicy.IGPMSecurityInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMStarterGPOBackup(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{51d98eda-a87e-43dd-b80a-0b66ef1938d6}')
    @commethod(7)
    def get_BackupDir(self, pbstrBackupDir: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Comment(self, pbstrComment: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DisplayName(self, pbstrDisplayName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Domain(self, pbstrTemplateDomain: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_StarterGPOID(self, pbstrTemplateID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ID(self, pbstrID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Timestamp(self, pTimestamp: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Type(self, pType: POINTER(Windows.Win32.System.GroupPolicy.GPMStarterGPOType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GenerateReport(self, gpmReportType: Windows.Win32.System.GroupPolicy.GPMReportType, pvarGPMProgress: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarGPMCancel: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GenerateReportToFile(self, gpmReportType: Windows.Win32.System.GroupPolicy.GPMReportType, bstrTargetFilePath: Windows.Win32.Foundation.BSTR, ppIGPMResult: POINTER(Windows.Win32.System.GroupPolicy.IGPMResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMStarterGPOBackupCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c998031d-add0-4bb5-8dea-298505d8423b}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppIGPMTmplBackup: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMStarterGPOCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2e522729-2219-44ad-933a-64dfd650c423}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppIGPMTemplates: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMStatusMessage(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8496c22f-f3de-4a1f-8f58-603caaa93d7b}')
    @commethod(7)
    def get_ObjectPath(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ErrorCode(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ExtensionName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_SettingsName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OperationCode(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Message(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMStatusMsgCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9b6e1af0-1a92-40f3-a59d-f36ac1f728b7}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, pVal: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMTrustee(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3b466da8-c1a4-4b2a-999a-befcdd56cefb}')
    @commethod(7)
    def get_TrusteeSid(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_TrusteeName(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TrusteeDomain(self, bstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_TrusteeDSPath(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_TrusteeType(self, lVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMWMIFilter(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ef2ff9b4-3c27-459a-b979-038305cec75d}')
    @commethod(7)
    def get_Path(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, newVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, newVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Description(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetQueryList(self, pQryList: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSecurityInfo(self, ppSecurityInfo: POINTER(Windows.Win32.System.GroupPolicy.IGPMSecurityInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSecurityInfo(self, pSecurityInfo: Windows.Win32.System.GroupPolicy.IGPMSecurityInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
class IGPMWMIFilterCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{5782d582-1a36-4661-8a94-c3c32551945b}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, pVal: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGroupPolicyObject(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ea502723-a23d-11d1-a7d3-0000f87571e3}')
    @commethod(3)
    def New(self, pszDomainName: Windows.Win32.Foundation.PWSTR, pszDisplayName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenDSGPO(self, pszPath: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OpenLocalMachineGPO(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OpenRemoteMachineGPO(self, pszComputerName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Save(self, bMachine: Windows.Win32.Foundation.BOOL, bAdd: Windows.Win32.Foundation.BOOL, pGuidExtension: POINTER(Guid), pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetName(self, pszName: Windows.Win32.Foundation.PWSTR, cchMaxLength: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDisplayName(self, pszName: Windows.Win32.Foundation.PWSTR, cchMaxLength: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDisplayName(self, pszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPath(self, pszPath: Windows.Win32.Foundation.PWSTR, cchMaxLength: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDSPath(self, dwSection: UInt32, pszPath: Windows.Win32.Foundation.PWSTR, cchMaxPath: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetFileSysPath(self, dwSection: UInt32, pszPath: Windows.Win32.Foundation.PWSTR, cchMaxPath: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRegistryKey(self, dwSection: UInt32, hKey: POINTER(Windows.Win32.System.Registry.HKEY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetOptions(self, dwOptions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetOptions(self, dwOptions: UInt32, dwMask: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetType(self, gpoType: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetMachineName(self, pszName: Windows.Win32.Foundation.PWSTR, cchMaxLength: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetPropertySheetPages(self, hPages: POINTER(POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE)), uPageCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class INSTALLDATA(EasyCastStructure):
    Type: Windows.Win32.System.GroupPolicy.INSTALLSPECTYPE
    Spec: Windows.Win32.System.GroupPolicy.INSTALLSPEC
class INSTALLSPEC(EasyCastUnion):
    AppName: _AppName_e__Struct
    FileExt: Windows.Win32.Foundation.PWSTR
    ProgId: Windows.Win32.Foundation.PWSTR
    COMClass: _COMClass_e__Struct
    class _AppName_e__Struct(EasyCastStructure):
        Name: Windows.Win32.Foundation.PWSTR
        GPOId: Guid
    class _COMClass_e__Struct(EasyCastStructure):
        Clsid: Guid
        ClsCtx: UInt32
INSTALLSPECTYPE = Int32
APPNAME: INSTALLSPECTYPE = 1
FILEEXT: INSTALLSPECTYPE = 2
PROGID: INSTALLSPECTYPE = 3
COMCLASS: INSTALLSPECTYPE = 4
class IRSOPInformation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9a5a81b5-d9c7-49ef-9d11-ddf50968c48d}')
    @commethod(3)
    def GetNamespace(self, dwSection: UInt32, pszName: Windows.Win32.Foundation.PWSTR, cchMaxLength: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEventLogEntryText(self, pszEventSource: Windows.Win32.Foundation.PWSTR, pszEventLogName: Windows.Win32.Foundation.PWSTR, pszEventTime: Windows.Win32.Foundation.PWSTR, dwEventID: UInt32, ppszText: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class LOCALMANAGEDAPPLICATION(EasyCastStructure):
    pszDeploymentName: Windows.Win32.Foundation.PWSTR
    pszPolicyName: Windows.Win32.Foundation.PWSTR
    pszProductId: Windows.Win32.Foundation.PWSTR
    dwState: UInt32
class MANAGEDAPPLICATION(EasyCastStructure):
    pszPackageName: Windows.Win32.Foundation.PWSTR
    pszPublisher: Windows.Win32.Foundation.PWSTR
    dwVersionHi: UInt32
    dwVersionLo: UInt32
    dwRevision: UInt32
    GpoId: Guid
    pszPolicyName: Windows.Win32.Foundation.PWSTR
    ProductId: Guid
    Language: UInt16
    pszOwner: Windows.Win32.Foundation.PWSTR
    pszCompany: Windows.Win32.Foundation.PWSTR
    pszComments: Windows.Win32.Foundation.PWSTR
    pszContact: Windows.Win32.Foundation.PWSTR
    pszSupportUrl: Windows.Win32.Foundation.PWSTR
    dwPathType: UInt32
    bInstalled: Windows.Win32.Foundation.BOOL
@winfunctype_pointer
def PFNGENERATEGROUPPOLICY(dwFlags: UInt32, pbAbort: POINTER(Windows.Win32.Foundation.BOOL), pwszSite: Windows.Win32.Foundation.PWSTR, pComputerTarget: POINTER(Windows.Win32.System.GroupPolicy.RSOP_TARGET_head), pUserTarget: POINTER(Windows.Win32.System.GroupPolicy.RSOP_TARGET_head)) -> UInt32: ...
@winfunctype_pointer
def PFNPROCESSGROUPPOLICY(dwFlags: UInt32, hToken: Windows.Win32.Foundation.HANDLE, hKeyRoot: Windows.Win32.System.Registry.HKEY, pDeletedGPOList: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTA_head), pChangedGPOList: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTA_head), pHandle: UIntPtr, pbAbort: POINTER(Windows.Win32.Foundation.BOOL), pStatusCallback: Windows.Win32.System.GroupPolicy.PFNSTATUSMESSAGECALLBACK) -> UInt32: ...
@winfunctype_pointer
def PFNPROCESSGROUPPOLICYEX(dwFlags: UInt32, hToken: Windows.Win32.Foundation.HANDLE, hKeyRoot: Windows.Win32.System.Registry.HKEY, pDeletedGPOList: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTA_head), pChangedGPOList: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTA_head), pHandle: UIntPtr, pbAbort: POINTER(Windows.Win32.Foundation.BOOL), pStatusCallback: Windows.Win32.System.GroupPolicy.PFNSTATUSMESSAGECALLBACK, pWbemServices: Windows.Win32.System.Wmi.IWbemServices_head, pRsopStatus: POINTER(Windows.Win32.Foundation.HRESULT)) -> UInt32: ...
@winfunctype_pointer
def PFNSTATUSMESSAGECALLBACK(bVerbose: Windows.Win32.Foundation.BOOL, lpMessage: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
class POLICYSETTINGSTATUSINFO(EasyCastStructure):
    szKey: Windows.Win32.Foundation.PWSTR
    szEventSource: Windows.Win32.Foundation.PWSTR
    szEventLogName: Windows.Win32.Foundation.PWSTR
    dwEventID: UInt32
    dwErrorCode: UInt32
    status: Windows.Win32.System.GroupPolicy.SETTINGSTATUS
    timeLogged: Windows.Win32.Foundation.SYSTEMTIME
class RSOP_TARGET(EasyCastStructure):
    pwszAccountName: Windows.Win32.Foundation.PWSTR
    pwszNewSOM: Windows.Win32.Foundation.PWSTR
    psaSecurityGroups: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)
    pRsopToken: c_void_p
    pGPOList: POINTER(Windows.Win32.System.GroupPolicy.GROUP_POLICY_OBJECTA_head)
    pWbemServices: Windows.Win32.System.Wmi.IWbemServices_head
SETTINGSTATUS = Int32
SETTINGSTATUS_RSOPUnspecified: SETTINGSTATUS = 0
SETTINGSTATUS_RSOPApplied: SETTINGSTATUS = 1
SETTINGSTATUS_RSOPIgnored: SETTINGSTATUS = 2
SETTINGSTATUS_RSOPFailed: SETTINGSTATUS = 3
SETTINGSTATUS_RSOPSubsettingFailed: SETTINGSTATUS = 4
make_head(_module, 'CriticalPolicySectionHandle')
make_head(_module, 'GPOBROWSEINFO')
make_head(_module, 'GROUP_POLICY_OBJECTA')
make_head(_module, 'GROUP_POLICY_OBJECTW')
make_head(_module, 'IGPEInformation')
make_head(_module, 'IGPM')
make_head(_module, 'IGPM2')
make_head(_module, 'IGPMAsyncCancel')
make_head(_module, 'IGPMAsyncProgress')
make_head(_module, 'IGPMBackup')
make_head(_module, 'IGPMBackupCollection')
make_head(_module, 'IGPMBackupDir')
make_head(_module, 'IGPMBackupDirEx')
make_head(_module, 'IGPMCSECollection')
make_head(_module, 'IGPMClientSideExtension')
make_head(_module, 'IGPMConstants')
make_head(_module, 'IGPMConstants2')
make_head(_module, 'IGPMDomain')
make_head(_module, 'IGPMDomain2')
make_head(_module, 'IGPMDomain3')
make_head(_module, 'IGPMGPO')
make_head(_module, 'IGPMGPO2')
make_head(_module, 'IGPMGPO3')
make_head(_module, 'IGPMGPOCollection')
make_head(_module, 'IGPMGPOLink')
make_head(_module, 'IGPMGPOLinksCollection')
make_head(_module, 'IGPMMapEntry')
make_head(_module, 'IGPMMapEntryCollection')
make_head(_module, 'IGPMMigrationTable')
make_head(_module, 'IGPMPermission')
make_head(_module, 'IGPMRSOP')
make_head(_module, 'IGPMResult')
make_head(_module, 'IGPMSOM')
make_head(_module, 'IGPMSOMCollection')
make_head(_module, 'IGPMSearchCriteria')
make_head(_module, 'IGPMSecurityInfo')
make_head(_module, 'IGPMSitesContainer')
make_head(_module, 'IGPMStarterGPO')
make_head(_module, 'IGPMStarterGPOBackup')
make_head(_module, 'IGPMStarterGPOBackupCollection')
make_head(_module, 'IGPMStarterGPOCollection')
make_head(_module, 'IGPMStatusMessage')
make_head(_module, 'IGPMStatusMsgCollection')
make_head(_module, 'IGPMTrustee')
make_head(_module, 'IGPMWMIFilter')
make_head(_module, 'IGPMWMIFilterCollection')
make_head(_module, 'IGroupPolicyObject')
make_head(_module, 'INSTALLDATA')
make_head(_module, 'INSTALLSPEC')
make_head(_module, 'IRSOPInformation')
make_head(_module, 'LOCALMANAGEDAPPLICATION')
make_head(_module, 'MANAGEDAPPLICATION')
make_head(_module, 'PFNGENERATEGROUPPOLICY')
make_head(_module, 'PFNPROCESSGROUPPOLICY')
make_head(_module, 'PFNPROCESSGROUPPOLICYEX')
make_head(_module, 'PFNSTATUSMESSAGECALLBACK')
make_head(_module, 'POLICYSETTINGSTATUSINFO')
make_head(_module, 'RSOP_TARGET')
