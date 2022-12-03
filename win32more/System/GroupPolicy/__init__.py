from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security
import win32more.System.Com
import win32more.System.GroupPolicy
import win32more.System.Ole
import win32more.System.Registry
import win32more.System.Wmi
import win32more.UI.Controls
import win32more.UI.Shell
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
GPM_USE_PDC = 0
GPM_USE_ANYDC = 1
GPM_DONOTUSE_W2KDC = 2
GPM_DONOT_VALIDATEDC = 1
GPM_MIGRATIONTABLE_ONLY = 1
GPM_PROCESS_SECURITY = 2
RSOP_NO_COMPUTER = 65536
RSOP_NO_USER = 131072
RSOP_PLANNING_ASSUME_SLOW_LINK = 1
RSOP_PLANNING_ASSUME_LOOPBACK_MERGE = 2
RSOP_PLANNING_ASSUME_LOOPBACK_REPLACE = 4
RSOP_PLANNING_ASSUME_USER_WQLFILTER_TRUE = 8
RSOP_PLANNING_ASSUME_COMP_WQLFILTER_TRUE = 16
PI_NOUI = 1
PI_APPLYPOLICY = 2
PT_TEMPORARY = 1
PT_ROAMING = 2
PT_MANDATORY = 4
PT_ROAMING_PREEXISTING = 8
RP_FORCE = 1
RP_SYNC = 2
GPC_BLOCK_POLICY = 1
GPO_FLAG_DISABLE = 1
GPO_FLAG_FORCE = 2
GPO_LIST_FLAG_MACHINE = 1
GPO_LIST_FLAG_SITEONLY = 2
GPO_LIST_FLAG_NO_WMIFILTERS = 4
GPO_LIST_FLAG_NO_SECURITYFILTERS = 8
GP_DLLNAME = 'DllName'
GP_ENABLEASYNCHRONOUSPROCESSING = 'EnableAsynchronousProcessing'
GP_MAXNOGPOLISTCHANGESINTERVAL = 'MaxNoGPOListChangesInterval'
GP_NOBACKGROUNDPOLICY = 'NoBackgroundPolicy'
GP_NOGPOLISTCHANGES = 'NoGPOListChanges'
GP_NOMACHINEPOLICY = 'NoMachinePolicy'
GP_NOSLOWLINK = 'NoSlowLink'
GP_NOTIFYLINKTRANSITION = 'NotifyLinkTransition'
GP_NOUSERPOLICY = 'NoUserPolicy'
GP_PERUSERLOCALSETTINGS = 'PerUserLocalSettings'
GP_PROCESSGROUPPOLICY = 'ProcessGroupPolicy'
GP_REQUIRESSUCCESSFULREGISTRY = 'RequiresSuccessfulRegistry'
GPO_INFO_FLAG_MACHINE = 1
GPO_INFO_FLAG_BACKGROUND = 16
GPO_INFO_FLAG_SLOWLINK = 32
GPO_INFO_FLAG_VERBOSE = 64
GPO_INFO_FLAG_NOCHANGES = 128
GPO_INFO_FLAG_LINKTRANSITION = 256
GPO_INFO_FLAG_LOGRSOP_TRANSITION = 512
GPO_INFO_FLAG_FORCED_REFRESH = 1024
GPO_INFO_FLAG_SAFEMODE_BOOT = 2048
GPO_INFO_FLAG_ASYNC_FOREGROUND = 4096
FLAG_NO_GPO_FILTER = 2147483648
FLAG_NO_CSE_INVOKE = 1073741824
FLAG_ASSUME_SLOW_LINK = 536870912
FLAG_LOOPBACK_MERGE = 268435456
FLAG_LOOPBACK_REPLACE = 134217728
FLAG_ASSUME_USER_WQLFILTER_TRUE = 67108864
FLAG_ASSUME_COMP_WQLFILTER_TRUE = 33554432
FLAG_PLANNING_MODE = 16777216
FLAG_NO_USER = 1
FLAG_NO_COMPUTER = 2
FLAG_FORCE_CREATENAMESPACE = 4
RSOP_USER_ACCESS_DENIED = 1
RSOP_COMPUTER_ACCESS_DENIED = 2
RSOP_TEMPNAMESPACE_EXISTS = 4
LOCALSTATE_ASSIGNED = 1
LOCALSTATE_PUBLISHED = 2
LOCALSTATE_UNINSTALL_UNMANAGED = 4
LOCALSTATE_POLICYREMOVE_ORPHAN = 8
LOCALSTATE_POLICYREMOVE_UNINSTALL = 16
LOCALSTATE_ORPHANED = 32
LOCALSTATE_UNINSTALLED = 64
MANAGED_APPS_USERAPPLICATIONS = 1
MANAGED_APPS_FROMCATEGORY = 2
MANAGED_APPS_INFOLEVEL_DEFAULT = 65536
MANAGED_APPTYPE_WINDOWSINSTALLER = 1
MANAGED_APPTYPE_SETUPEXE = 2
MANAGED_APPTYPE_UNSUPPORTED = 3
def _define_CLSID_GPESnapIn():
    return Guid('8fc0b734-a0e1-11d1-a7-d3-00-00-f8-75-71-e3')
def _define_NODEID_Machine():
    return Guid('8fc0b737-a0e1-11d1-a7-d3-00-00-f8-75-71-e3')
def _define_NODEID_MachineSWSettings():
    return Guid('8fc0b73a-a0e1-11d1-a7-d3-00-00-f8-75-71-e3')
def _define_NODEID_User():
    return Guid('8fc0b738-a0e1-11d1-a7-d3-00-00-f8-75-71-e3')
def _define_NODEID_UserSWSettings():
    return Guid('8fc0b73c-a0e1-11d1-a7-d3-00-00-f8-75-71-e3')
def _define_CLSID_GroupPolicyObject():
    return Guid('ea502722-a23d-11d1-a7-d3-00-00-f8-75-71-e3')
def _define_CLSID_RSOPSnapIn():
    return Guid('6dc3804b-7212-458d-ad-b0-9a-07-e2-ae-1f-a2')
def _define_NODEID_RSOPMachine():
    return Guid('bd4c1a2e-0b7a-4a62-a6-b0-c0-57-75-39-c9-7e')
def _define_NODEID_RSOPMachineSWSettings():
    return Guid('6a76273e-eb8e-45db-94-c5-25-66-3a-5f-2c-1a')
def _define_NODEID_RSOPUser():
    return Guid('ab87364f-0cec-4cd8-9b-f8-89-8f-34-62-8f-b8')
def _define_NODEID_RSOPUserSWSettings():
    return Guid('e52c5ce3-fd27-4402-84-de-d9-a5-f2-85-89-10')
GPO_SECTION_ROOT = 0
GPO_SECTION_USER = 1
GPO_SECTION_MACHINE = 2
GPO_OPEN_LOAD_REGISTRY = 1
GPO_OPEN_READ_ONLY = 2
GPO_OPTION_DISABLE_USER = 1
GPO_OPTION_DISABLE_MACHINE = 2
RSOP_INFO_FLAG_DIAGNOSTIC_MODE = 1
GPO_BROWSE_DISABLENEW = 1
GPO_BROWSE_NOCOMPUTERS = 2
GPO_BROWSE_NODSGPOS = 4
GPO_BROWSE_OPENBUTTON = 8
GPO_BROWSE_INITTOALL = 16
GPO_BROWSE_NOUSERGPOS = 32
GPO_BROWSE_SENDAPPLYONEDIT = 64
def _define_RefreshPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL)(('RefreshPolicy', windll['USERENV.dll']), ((1, 'bMachine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RefreshPolicyEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL,UInt32)(('RefreshPolicyEx', windll['USERENV.dll']), ((1, 'bMachine'),(1, 'dwOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnterCriticalPolicySection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.BOOL)(('EnterCriticalPolicySection', windll['USERENV.dll']), ((1, 'bMachine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LeaveCriticalPolicySection():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('LeaveCriticalPolicySection', windll['USERENV.dll']), ((1, 'hSection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterGPNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL)(('RegisterGPNotification', windll['USERENV.dll']), ((1, 'hEvent'),(1, 'bMachine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterGPNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('UnregisterGPNotification', windll['USERENV.dll']), ((1, 'hEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGPOListA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,POINTER(POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTA_head)))(('GetGPOListA', windll['USERENV.dll']), ((1, 'hToken'),(1, 'lpName'),(1, 'lpHostName'),(1, 'lpComputerName'),(1, 'dwFlags'),(1, 'pGPOList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGPOListW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTW_head)))(('GetGPOListW', windll['USERENV.dll']), ((1, 'hToken'),(1, 'lpName'),(1, 'lpHostName'),(1, 'lpComputerName'),(1, 'dwFlags'),(1, 'pGPOList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeGPOListA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTA_head))(('FreeGPOListA', windll['USERENV.dll']), ((1, 'pGPOList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeGPOListW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTW_head))(('FreeGPOListW', windll['USERENV.dll']), ((1, 'pGPOList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAppliedGPOListA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSID,POINTER(Guid),POINTER(POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTA_head)))(('GetAppliedGPOListA', windll['USERENV.dll']), ((1, 'dwFlags'),(1, 'pMachineName'),(1, 'pSidUser'),(1, 'pGuidExtension'),(1, 'ppGPOList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAppliedGPOListW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PSID,POINTER(Guid),POINTER(POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTW_head)))(('GetAppliedGPOListW', windll['USERENV.dll']), ((1, 'dwFlags'),(1, 'pMachineName'),(1, 'pSidUser'),(1, 'pGuidExtension'),(1, 'ppGPOList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ProcessGroupPolicyCompleted():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),UIntPtr,UInt32)(('ProcessGroupPolicyCompleted', windll['USERENV.dll']), ((1, 'extensionId'),(1, 'pAsyncHandle'),(1, 'dwStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ProcessGroupPolicyCompletedEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),UIntPtr,UInt32,win32more.Foundation.HRESULT)(('ProcessGroupPolicyCompletedEx', windll['USERENV.dll']), ((1, 'extensionId'),(1, 'pAsyncHandle'),(1, 'dwStatus'),(1, 'RsopStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RsopAccessCheckByType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.PSECURITY_DESCRIPTOR,win32more.Foundation.PSID,c_void_p,UInt32,POINTER(win32more.Security.OBJECT_TYPE_LIST_head),UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),POINTER(win32more.Security.PRIVILEGE_SET_head),POINTER(UInt32),POINTER(UInt32),POINTER(Int32))(('RsopAccessCheckByType', windll['USERENV.dll']), ((1, 'pSecurityDescriptor'),(1, 'pPrincipalSelfSid'),(1, 'pRsopToken'),(1, 'dwDesiredAccessMask'),(1, 'pObjectTypeList'),(1, 'ObjectTypeListLength'),(1, 'pGenericMapping'),(1, 'pPrivilegeSet'),(1, 'pdwPrivilegeSetLength'),(1, 'pdwGrantedAccessMask'),(1, 'pbAccessStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RsopFileAccessCheck():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_void_p,UInt32,POINTER(UInt32),POINTER(Int32))(('RsopFileAccessCheck', windll['USERENV.dll']), ((1, 'pszFileName'),(1, 'pRsopToken'),(1, 'dwDesiredAccessMask'),(1, 'pdwGrantedAccessMask'),(1, 'pbAccessStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RsopSetPolicySettingStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Wmi.IWbemServices_head,win32more.System.Wmi.IWbemClassObject_head,UInt32,POINTER(win32more.System.GroupPolicy.POLICYSETTINGSTATUSINFO_head))(('RsopSetPolicySettingStatus', windll['USERENV.dll']), ((1, 'dwFlags'),(1, 'pServices'),(1, 'pSettingInstance'),(1, 'nInfo'),(1, 'pStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RsopResetPolicySettingStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Wmi.IWbemServices_head,win32more.System.Wmi.IWbemClassObject_head)(('RsopResetPolicySettingStatus', windll['USERENV.dll']), ((1, 'dwFlags'),(1, 'pServices'),(1, 'pSettingInstance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GenerateGPNotification():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32)(('GenerateGPNotification', windll['USERENV.dll']), ((1, 'bMachine'),(1, 'lpwszMgmtProduct'),(1, 'dwMgmtProductOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InstallApplication():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.GroupPolicy.INSTALLDATA_head))(('InstallApplication', windll['ADVAPI32.dll']), ((1, 'pInstallInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UninstallApplication():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32)(('UninstallApplication', windll['ADVAPI32.dll']), ((1, 'ProductCode'),(1, 'dwStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CommandLineFromMsiDescriptor():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('CommandLineFromMsiDescriptor', windll['ADVAPI32.dll']), ((1, 'Descriptor'),(1, 'CommandLine'),(1, 'CommandLineLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetManagedApplications():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),UInt32,UInt32,POINTER(UInt32),POINTER(POINTER(win32more.System.GroupPolicy.MANAGEDAPPLICATION_head)))(('GetManagedApplications', windll['ADVAPI32.dll']), ((1, 'pCategory'),(1, 'dwQueryFlags'),(1, 'dwInfoLevel'),(1, 'pdwApps'),(1, 'prgManagedApps'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLocalManagedApplications():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.BOOL,POINTER(UInt32),POINTER(POINTER(win32more.System.GroupPolicy.LOCALMANAGEDAPPLICATION_head)))(('GetLocalManagedApplications', windll['ADVAPI32.dll']), ((1, 'bUserApps'),(1, 'pdwApps'),(1, 'prgLocalApps'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLocalManagedApplicationData():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(('GetLocalManagedApplicationData', windll['ADVAPI32.dll']), ((1, 'ProductCode'),(1, 'DisplayName'),(1, 'SupportUrl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetManagedApplicationCategories():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.UI.Shell.APPCATEGORYINFOLIST_head))(('GetManagedApplicationCategories', windll['ADVAPI32.dll']), ((1, 'dwReserved'),(1, 'pAppCategory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateGPOLink():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(('CreateGPOLink', windll['GPEDIT.dll']), ((1, 'lpGPO'),(1, 'lpContainer'),(1, 'fHighPriority'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteGPOLink():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('DeleteGPOLink', windll['GPEDIT.dll']), ((1, 'lpGPO'),(1, 'lpContainer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteAllGPOLinks():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('DeleteAllGPOLinks', windll['GPEDIT.dll']), ((1, 'lpContainer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BrowseForGPO():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPOBROWSEINFO_head))(('BrowseForGPO', windll['GPEDIT.dll']), ((1, 'lpBrowseInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImportRSoPData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('ImportRSoPData', windll['GPEDIT.dll']), ((1, 'lpNameSpace'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExportRSoPData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('ExportRSoPData', windll['GPEDIT.dll']), ((1, 'lpNameSpace'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
APPSTATE = Int32
ABSENT = 0
ASSIGNED = 1
PUBLISHED = 2
CriticalPolicySectionHandle = IntPtr
GPM = Guid('f5694708-88fe-4b35-ba-bf-e5-61-62-d5-fb-c8')
GPMAsyncCancel = Guid('372796a9-76ec-479d-ad-6c-55-63-18-ed-5f-9d')
GPMBackup = Guid('ed1a54b8-5efa-482a-93-c0-8a-d8-6f-0d-68-c3')
GPMBackupCollection = Guid('eb8f035b-70db-4a9f-96-76-37-c2-59-94-e9-dc')
GPMBackupDir = Guid('fce4a59d-0f21-4afa-b8-59-e6-d0-c6-2c-d1-0c')
GPMBackupDirEx = Guid('e8c0988a-cf03-4c5b-8b-e2-2a-a9-ad-32-aa-da')
GPMBackupType = Int32
GPMBackupType_typeGPO = 0
GPMBackupType_typeStarterGPO = 1
GPMClientSideExtension = Guid('c1a2e70e-659c-4b1a-94-0b-f8-8b-0a-f9-c8-a4')
GPMConstants = Guid('3855e880-cd9e-4d0c-9e-af-15-79-28-3a-18-88')
GPMCSECollection = Guid('cf92b828-2d44-4b61-b1-0a-b3-27-af-d4-2d-a8')
GPMDestinationOption = Int32
GPMDestinationOption_opDestinationSameAsSource = 0
GPMDestinationOption_opDestinationNone = 1
GPMDestinationOption_opDestinationByRelativeName = 2
GPMDestinationOption_opDestinationSet = 3
GPMDomain = Guid('710901be-1050-4cb1-83-8a-c5-cf-f2-59-e1-83')
GPMEntryType = Int32
GPMEntryType_typeUser = 0
GPMEntryType_typeComputer = 1
GPMEntryType_typeLocalGroup = 2
GPMEntryType_typeGlobalGroup = 3
GPMEntryType_typeUniversalGroup = 4
GPMEntryType_typeUNCPath = 5
GPMEntryType_typeUnknown = 6
GPMGPO = Guid('d2ce2994-59b5-4064-b5-81-4d-68-48-6a-16-c4')
GPMGPOCollection = Guid('7a057325-832d-4de3-a4-1f-c7-80-43-6a-4e-09')
GPMGPOLink = Guid('c1df9880-5303-42c6-8a-3c-04-88-e1-bf-73-64')
GPMGPOLinksCollection = Guid('f6ed581a-49a5-47e2-b7-71-fd-8d-c0-2b-62-59')
GPMMapEntry = Guid('8c975253-5431-4471-b3-5d-06-26-c9-28-25-8a')
GPMMapEntryCollection = Guid('0cf75d5b-a3a1-4c55-b4-fe-9e-14-9c-41-f6-6d')
GPMMigrationTable = Guid('55af4043-2a06-4f72-ab-ef-63-1b-44-07-9c-76')
GPMPermission = Guid('5871a40a-e9c0-46ec-91-3e-94-4e-f9-22-5a-94')
GPMPermissionType = Int32
GPMPermissionType_permGPOApply = 65536
GPMPermissionType_permGPORead = 65792
GPMPermissionType_permGPOEdit = 65793
GPMPermissionType_permGPOEditSecurityAndDelete = 65794
GPMPermissionType_permGPOCustom = 65795
GPMPermissionType_permWMIFilterEdit = 131072
GPMPermissionType_permWMIFilterFullControl = 131073
GPMPermissionType_permWMIFilterCustom = 131074
GPMPermissionType_permSOMLink = 1835008
GPMPermissionType_permSOMLogging = 1573120
GPMPermissionType_permSOMPlanning = 1573376
GPMPermissionType_permSOMWMICreate = 1049344
GPMPermissionType_permSOMWMIFullControl = 1049345
GPMPermissionType_permSOMGPOCreate = 1049600
GPMPermissionType_permStarterGPORead = 197888
GPMPermissionType_permStarterGPOEdit = 197889
GPMPermissionType_permStarterGPOFullControl = 197890
GPMPermissionType_permStarterGPOCustom = 197891
GPMPermissionType_permSOMStarterGPOCreate = 1049856
GPMReportingOptions = Int32
GPMReportingOptions_opReportLegacy = 0
GPMReportingOptions_opReportComments = 1
GPMReportType = Int32
GPMReportType_repXML = 0
GPMReportType_repHTML = 1
GPMReportType_repInfraXML = 2
GPMReportType_repInfraRefreshXML = 3
GPMReportType_repClientHealthXML = 4
GPMReportType_repClientHealthRefreshXML = 5
GPMResult = Guid('92101ac0-9287-4206-a3-b2-4b-db-73-d2-25-f6')
GPMRSOP = Guid('489b0caf-9ec2-4eb7-91-f5-b6-f7-1d-43-da-8c')
GPMRSOPMode = Int32
GPMRSOPMode_rsopUnknown = 0
GPMRSOPMode_rsopPlanning = 1
GPMRSOPMode_rsopLogging = 2
GPMSearchCriteria = Guid('17aaca26-5ce0-44fa-8c-c0-52-59-e6-48-35-66')
GPMSearchOperation = Int32
GPMSearchOperation_opEquals = 0
GPMSearchOperation_opContains = 1
GPMSearchOperation_opNotContains = 2
GPMSearchOperation_opNotEquals = 3
GPMSearchProperty = Int32
GPMSearchProperty_gpoPermissions = 0
GPMSearchProperty_gpoEffectivePermissions = 1
GPMSearchProperty_gpoDisplayName = 2
GPMSearchProperty_gpoWMIFilter = 3
GPMSearchProperty_gpoID = 4
GPMSearchProperty_gpoComputerExtensions = 5
GPMSearchProperty_gpoUserExtensions = 6
GPMSearchProperty_somLinks = 7
GPMSearchProperty_gpoDomain = 8
GPMSearchProperty_backupMostRecent = 9
GPMSearchProperty_starterGPOPermissions = 10
GPMSearchProperty_starterGPOEffectivePermissions = 11
GPMSearchProperty_starterGPODisplayName = 12
GPMSearchProperty_starterGPOID = 13
GPMSearchProperty_starterGPODomain = 14
GPMSecurityInfo = Guid('547a5e8f-9162-4516-a4-df-9d-db-96-86-d8-46')
GPMSitesContainer = Guid('229f5c42-852c-4b30-94-5f-c5-22-be-9b-d3-86')
GPMSOM = Guid('32d93fac-450e-44cf-82-9c-8b-22-ff-6b-da-e1')
GPMSOMCollection = Guid('24c1f147-3720-4f5b-a9-c3-06-b4-e4-f9-31-d2')
GPMSOMType = Int32
GPMSOMType_somSite = 0
GPMSOMType_somDomain = 1
GPMSOMType_somOU = 2
GPMStarterGPOBackup = Guid('389e400a-d8ef-455b-a8-61-5f-9c-a3-4a-6a-02')
GPMStarterGPOBackupCollection = Guid('e75ea59d-1aeb-4cb5-a7-8a-28-1d-aa-58-24-06')
GPMStarterGPOCollection = Guid('82f8aa8b-49ba-43b2-95-6e-33-97-f9-b9-4c-3a')
GPMStarterGPOType = Int32
GPMStarterGPOType_typeSystem = 0
GPMStarterGPOType_typeCustom = 1
GPMStatusMessage = Guid('4b77cc94-d255-409b-bc-62-37-08-81-71-5a-19')
GPMStatusMsgCollection = Guid('2824e4be-4bcc-4cac-9e-60-0e-3e-d7-f1-24-96')
GPMTemplate = Guid('ecf1d454-71da-4e2f-a8-c0-81-85-46-59-11-d9')
GPMTrustee = Guid('c54a700d-19b6-4211-bc-b0-e8-e2-47-5e-47-1e')
GPMWMIFilter = Guid('626745d8-0dea-4062-bf-60-cf-c5-b1-ca-12-86')
GPMWMIFilterCollection = Guid('74dc6d28-e820-47d6-a0-b8-f0-8d-93-d7-fa-33')
GPO_LINK = Int32
GPO_LINK_GPLinkUnknown = 0
GPO_LINK_GPLinkMachine = 1
GPO_LINK_GPLinkSite = 2
GPO_LINK_GPLinkDomain = 3
GPO_LINK_GPLinkOrganizationalUnit = 4
def _define_GPOBROWSEINFO_head():
    class GPOBROWSEINFO(Structure):
        pass
    return GPOBROWSEINFO
def _define_GPOBROWSEINFO():
    GPOBROWSEINFO = win32more.System.GroupPolicy.GPOBROWSEINFO_head
    GPOBROWSEINFO._fields_ = [
        ('dwSize', UInt32),
        ('dwFlags', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('lpTitle', win32more.Foundation.PWSTR),
        ('lpInitialOU', win32more.Foundation.PWSTR),
        ('lpDSPath', win32more.Foundation.PWSTR),
        ('dwDSPathSize', UInt32),
        ('lpName', win32more.Foundation.PWSTR),
        ('dwNameSize', UInt32),
        ('gpoType', win32more.System.GroupPolicy.GROUP_POLICY_OBJECT_TYPE),
        ('gpoHint', win32more.System.GroupPolicy.GROUP_POLICY_HINT_TYPE),
    ]
    return GPOBROWSEINFO
GROUP_POLICY_HINT_TYPE = Int32
GROUP_POLICY_HINT_TYPE_GPHintUnknown = 0
GROUP_POLICY_HINT_TYPE_GPHintMachine = 1
GROUP_POLICY_HINT_TYPE_GPHintSite = 2
GROUP_POLICY_HINT_TYPE_GPHintDomain = 3
GROUP_POLICY_HINT_TYPE_GPHintOrganizationalUnit = 4
GROUP_POLICY_OBJECT_TYPE = Int32
GROUP_POLICY_OBJECT_TYPE_GPOTypeLocal = 0
GROUP_POLICY_OBJECT_TYPE_GPOTypeRemote = 1
GROUP_POLICY_OBJECT_TYPE_GPOTypeDS = 2
GROUP_POLICY_OBJECT_TYPE_GPOTypeLocalUser = 3
GROUP_POLICY_OBJECT_TYPE_GPOTypeLocalGroup = 4
def _define_GROUP_POLICY_OBJECTA_head():
    class GROUP_POLICY_OBJECTA(Structure):
        pass
    return GROUP_POLICY_OBJECTA
def _define_GROUP_POLICY_OBJECTA():
    GROUP_POLICY_OBJECTA = win32more.System.GroupPolicy.GROUP_POLICY_OBJECTA_head
    GROUP_POLICY_OBJECTA._fields_ = [
        ('dwOptions', UInt32),
        ('dwVersion', UInt32),
        ('lpDSPath', win32more.Foundation.PSTR),
        ('lpFileSysPath', win32more.Foundation.PSTR),
        ('lpDisplayName', win32more.Foundation.PSTR),
        ('szGPOName', win32more.Foundation.CHAR * 50),
        ('GPOLink', win32more.System.GroupPolicy.GPO_LINK),
        ('lParam', win32more.Foundation.LPARAM),
        ('pNext', POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTA_head)),
        ('pPrev', POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTA_head)),
        ('lpExtensions', win32more.Foundation.PSTR),
        ('lParam2', win32more.Foundation.LPARAM),
        ('lpLink', win32more.Foundation.PSTR),
    ]
    return GROUP_POLICY_OBJECTA
def _define_GROUP_POLICY_OBJECTW_head():
    class GROUP_POLICY_OBJECTW(Structure):
        pass
    return GROUP_POLICY_OBJECTW
def _define_GROUP_POLICY_OBJECTW():
    GROUP_POLICY_OBJECTW = win32more.System.GroupPolicy.GROUP_POLICY_OBJECTW_head
    GROUP_POLICY_OBJECTW._fields_ = [
        ('dwOptions', UInt32),
        ('dwVersion', UInt32),
        ('lpDSPath', win32more.Foundation.PWSTR),
        ('lpFileSysPath', win32more.Foundation.PWSTR),
        ('lpDisplayName', win32more.Foundation.PWSTR),
        ('szGPOName', Char * 50),
        ('GPOLink', win32more.System.GroupPolicy.GPO_LINK),
        ('lParam', win32more.Foundation.LPARAM),
        ('pNext', POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTW_head)),
        ('pPrev', POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTW_head)),
        ('lpExtensions', win32more.Foundation.PWSTR),
        ('lParam2', win32more.Foundation.LPARAM),
        ('lpLink', win32more.Foundation.PWSTR),
    ]
    return GROUP_POLICY_OBJECTW
def _define_IGPEInformation_head():
    class IGPEInformation(win32more.System.Com.IUnknown_head):
        Guid = Guid('8fc0b735-a0e1-11d1-a7-d3-00-00-f8-75-71-e3')
    return IGPEInformation
def _define_IGPEInformation():
    IGPEInformation = win32more.System.GroupPolicy.IGPEInformation_head
    IGPEInformation.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32)(3, 'GetName', ((1, 'pszName'),(1, 'cchMaxLength'),)))
    IGPEInformation.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32)(4, 'GetDisplayName', ((1, 'pszName'),(1, 'cchMaxLength'),)))
    IGPEInformation.GetRegistryKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Registry.HKEY))(5, 'GetRegistryKey', ((1, 'dwSection'),(1, 'hKey'),)))
    IGPEInformation.GetDSPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,Int32)(6, 'GetDSPath', ((1, 'dwSection'),(1, 'pszPath'),(1, 'cchMaxPath'),)))
    IGPEInformation.GetFileSysPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,Int32)(7, 'GetFileSysPath', ((1, 'dwSection'),(1, 'pszPath'),(1, 'cchMaxPath'),)))
    IGPEInformation.GetOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'GetOptions', ((1, 'dwOptions'),)))
    IGPEInformation.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECT_TYPE))(9, 'GetType', ((1, 'gpoType'),)))
    IGPEInformation.GetHint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GROUP_POLICY_HINT_TYPE))(10, 'GetHint', ((1, 'gpHint'),)))
    IGPEInformation.PolicyChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(Guid),POINTER(Guid))(11, 'PolicyChanged', ((1, 'bMachine'),(1, 'bAdd'),(1, 'pGuidExtension'),(1, 'pGuidSnapin'),)))
    win32more.System.Com.IUnknown
    return IGPEInformation
def _define_IGPM_head():
    class IGPM(win32more.System.Com.IDispatch_head):
        Guid = Guid('f5fae809-3bd6-4da9-a6-5e-17-66-5b-41-d7-63')
    return IGPM
def _define_IGPM():
    IGPM = win32more.System.GroupPolicy.IGPM_head
    IGPM.GetDomain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.GroupPolicy.IGPMDomain_head))(7, 'GetDomain', ((1, 'bstrDomain'),(1, 'bstrDomainController'),(1, 'lDCFlags'),(1, 'pIGPMDomain'),)))
    IGPM.GetBackupDir = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMBackupDir_head))(8, 'GetBackupDir', ((1, 'bstrBackupDir'),(1, 'pIGPMBackupDir'),)))
    IGPM.GetSitesContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.GroupPolicy.IGPMSitesContainer_head))(9, 'GetSitesContainer', ((1, 'bstrForest'),(1, 'bstrDomain'),(1, 'bstrDomainController'),(1, 'lDCFlags'),(1, 'ppIGPMSitesContainer'),)))
    IGPM.GetRSOP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMRSOPMode,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.GroupPolicy.IGPMRSOP_head))(10, 'GetRSOP', ((1, 'gpmRSoPMode'),(1, 'bstrNamespace'),(1, 'lFlags'),(1, 'ppIGPMRSOP'),)))
    IGPM.CreatePermission = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.GroupPolicy.GPMPermissionType,win32more.Foundation.VARIANT_BOOL,POINTER(win32more.System.GroupPolicy.IGPMPermission_head))(11, 'CreatePermission', ((1, 'bstrTrustee'),(1, 'perm'),(1, 'bInheritable'),(1, 'ppPerm'),)))
    IGPM.CreateSearchCriteria = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMSearchCriteria_head))(12, 'CreateSearchCriteria', ((1, 'ppIGPMSearchCriteria'),)))
    IGPM.CreateTrustee = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMTrustee_head))(13, 'CreateTrustee', ((1, 'bstrTrustee'),(1, 'ppIGPMTrustee'),)))
    IGPM.GetClientSideExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMCSECollection_head))(14, 'GetClientSideExtensions', ((1, 'ppIGPMCSECollection'),)))
    IGPM.GetConstants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMConstants_head))(15, 'GetConstants', ((1, 'ppIGPMConstants'),)))
    IGPM.GetMigrationTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMMigrationTable_head))(16, 'GetMigrationTable', ((1, 'bstrMigrationTablePath'),(1, 'ppMigrationTable'),)))
    IGPM.CreateMigrationTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMMigrationTable_head))(17, 'CreateMigrationTable', ((1, 'ppMigrationTable'),)))
    IGPM.InitializeReporting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(18, 'InitializeReporting', ((1, 'bstrAdmPath'),)))
    win32more.System.Com.IDispatch
    return IGPM
def _define_IGPM2_head():
    class IGPM2(win32more.System.GroupPolicy.IGPM_head):
        Guid = Guid('00238f8a-3d86-41ac-8f-5e-06-a6-63-8a-63-4a')
    return IGPM2
def _define_IGPM2():
    IGPM2 = win32more.System.GroupPolicy.IGPM2_head
    IGPM2.GetBackupDirEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.GroupPolicy.GPMBackupType,POINTER(win32more.System.GroupPolicy.IGPMBackupDirEx_head))(19, 'GetBackupDirEx', ((1, 'bstrBackupDir'),(1, 'backupDirType'),(1, 'ppIGPMBackupDirEx'),)))
    IGPM2.InitializeReportingEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32)(20, 'InitializeReportingEx', ((1, 'bstrAdmPath'),(1, 'reportingOptions'),)))
    win32more.System.GroupPolicy.IGPM
    return IGPM2
def _define_IGPMAsyncCancel_head():
    class IGPMAsyncCancel(win32more.System.Com.IDispatch_head):
        Guid = Guid('ddc67754-be67-4541-81-66-f4-81-66-86-8c-9c')
    return IGPMAsyncCancel
def _define_IGPMAsyncCancel():
    IGPMAsyncCancel = win32more.System.GroupPolicy.IGPMAsyncCancel_head
    IGPMAsyncCancel.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Cancel', ()))
    win32more.System.Com.IDispatch
    return IGPMAsyncCancel
def _define_IGPMAsyncProgress_head():
    class IGPMAsyncProgress(win32more.System.Com.IDispatch_head):
        Guid = Guid('6aac29f8-5948-4324-bf-70-42-38-18-94-2d-bc')
    return IGPMAsyncProgress
def _define_IGPMAsyncProgress():
    IGPMAsyncProgress = win32more.System.GroupPolicy.IGPMAsyncProgress_head
    IGPMAsyncProgress.Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),win32more.System.GroupPolicy.IGPMStatusMsgCollection_head)(7, 'Status', ((1, 'lProgressNumerator'),(1, 'lProgressDenominator'),(1, 'hrStatus'),(1, 'pResult'),(1, 'ppIGPMStatusMsgCollection'),)))
    win32more.System.Com.IDispatch
    return IGPMAsyncProgress
def _define_IGPMBackup_head():
    class IGPMBackup(win32more.System.Com.IDispatch_head):
        Guid = Guid('d8a16a35-3b0d-416b-8d-02-4d-f6-f9-5a-71-19')
    return IGPMBackup
def _define_IGPMBackup():
    IGPMBackup = win32more.System.GroupPolicy.IGPMBackup_head
    IGPMBackup.get_ID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_ID', ((1, 'pVal'),)))
    IGPMBackup.get_GPOID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_GPOID', ((1, 'pVal'),)))
    IGPMBackup.get_GPODomain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_GPODomain', ((1, 'pVal'),)))
    IGPMBackup.get_GPODisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_GPODisplayName', ((1, 'pVal'),)))
    IGPMBackup.get_Timestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(11, 'get_Timestamp', ((1, 'pVal'),)))
    IGPMBackup.get_Comment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Comment', ((1, 'pVal'),)))
    IGPMBackup.get_BackupDir = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_BackupDir', ((1, 'pVal'),)))
    IGPMBackup.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'Delete', ()))
    IGPMBackup.GenerateReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMReportType,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(15, 'GenerateReport', ((1, 'gpmReportType'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMBackup.GenerateReportToFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMReportType,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMResult_head))(16, 'GenerateReportToFile', ((1, 'gpmReportType'),(1, 'bstrTargetFilePath'),(1, 'ppIGPMResult'),)))
    win32more.System.Com.IDispatch
    return IGPMBackup
def _define_IGPMBackupCollection_head():
    class IGPMBackupCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('c786fc0f-26d8-4bab-a7-45-39-ca-7e-80-0c-ac')
    return IGPMBackupCollection
def _define_IGPMBackupCollection():
    IGPMBackupCollection = win32more.System.GroupPolicy.IGPMBackupCollection_head
    IGPMBackupCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pVal'),)))
    IGPMBackupCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pVal'),)))
    IGPMBackupCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(9, 'get__NewEnum', ((1, 'ppIGPMBackup'),)))
    win32more.System.Com.IDispatch
    return IGPMBackupCollection
def _define_IGPMBackupDir_head():
    class IGPMBackupDir(win32more.System.Com.IDispatch_head):
        Guid = Guid('b1568bed-0a93-4acc-81-0f-af-e7-08-10-19-b9')
    return IGPMBackupDir
def _define_IGPMBackupDir():
    IGPMBackupDir = win32more.System.GroupPolicy.IGPMBackupDir_head
    IGPMBackupDir.get_BackupDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_BackupDirectory', ((1, 'pVal'),)))
    IGPMBackupDir.GetBackup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMBackup_head))(8, 'GetBackup', ((1, 'bstrID'),(1, 'ppBackup'),)))
    IGPMBackupDir.SearchBackups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMSearchCriteria_head,POINTER(win32more.System.GroupPolicy.IGPMBackupCollection_head))(9, 'SearchBackups', ((1, 'pIGPMSearchCriteria'),(1, 'ppIGPMBackupCollection'),)))
    win32more.System.Com.IDispatch
    return IGPMBackupDir
def _define_IGPMBackupDirEx_head():
    class IGPMBackupDirEx(win32more.System.Com.IDispatch_head):
        Guid = Guid('f8dc55ed-3ba0-4864-aa-d4-d3-65-18-9e-e1-d5')
    return IGPMBackupDirEx
def _define_IGPMBackupDirEx():
    IGPMBackupDirEx = win32more.System.GroupPolicy.IGPMBackupDirEx_head
    IGPMBackupDirEx.get_BackupDir = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_BackupDir', ((1, 'pbstrBackupDir'),)))
    IGPMBackupDirEx.get_BackupType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMBackupType))(8, 'get_BackupType', ((1, 'pgpmBackupType'),)))
    IGPMBackupDirEx.GetBackup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head))(9, 'GetBackup', ((1, 'bstrID'),(1, 'pvarBackup'),)))
    IGPMBackupDirEx.SearchBackups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMSearchCriteria_head,POINTER(win32more.System.Com.VARIANT_head))(10, 'SearchBackups', ((1, 'pIGPMSearchCriteria'),(1, 'pvarBackupCollection'),)))
    win32more.System.Com.IDispatch
    return IGPMBackupDirEx
def _define_IGPMClientSideExtension_head():
    class IGPMClientSideExtension(win32more.System.Com.IDispatch_head):
        Guid = Guid('69da7488-b8db-415e-92-66-90-1b-e4-d4-99-28')
    return IGPMClientSideExtension
def _define_IGPMClientSideExtension():
    IGPMClientSideExtension = win32more.System.GroupPolicy.IGPMClientSideExtension_head
    IGPMClientSideExtension.get_ID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_ID', ((1, 'pVal'),)))
    IGPMClientSideExtension.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_DisplayName', ((1, 'pVal'),)))
    IGPMClientSideExtension.IsUserEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'IsUserEnabled', ((1, 'pvbEnabled'),)))
    IGPMClientSideExtension.IsComputerEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(10, 'IsComputerEnabled', ((1, 'pvbEnabled'),)))
    win32more.System.Com.IDispatch
    return IGPMClientSideExtension
def _define_IGPMConstants_head():
    class IGPMConstants(win32more.System.Com.IDispatch_head):
        Guid = Guid('50ef73e6-d35c-4c8d-be-63-7e-a5-d2-aa-c5-c4')
    return IGPMConstants
def _define_IGPMConstants():
    IGPMConstants = win32more.System.GroupPolicy.IGPMConstants_head
    IGPMConstants.get_PermGPOApply = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(7, 'get_PermGPOApply', ((1, 'pVal'),)))
    IGPMConstants.get_PermGPORead = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(8, 'get_PermGPORead', ((1, 'pVal'),)))
    IGPMConstants.get_PermGPOEdit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(9, 'get_PermGPOEdit', ((1, 'pVal'),)))
    IGPMConstants.get_PermGPOEditSecurityAndDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(10, 'get_PermGPOEditSecurityAndDelete', ((1, 'pVal'),)))
    IGPMConstants.get_PermGPOCustom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(11, 'get_PermGPOCustom', ((1, 'pVal'),)))
    IGPMConstants.get_PermWMIFilterEdit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(12, 'get_PermWMIFilterEdit', ((1, 'pVal'),)))
    IGPMConstants.get_PermWMIFilterFullControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(13, 'get_PermWMIFilterFullControl', ((1, 'pVal'),)))
    IGPMConstants.get_PermWMIFilterCustom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(14, 'get_PermWMIFilterCustom', ((1, 'pVal'),)))
    IGPMConstants.get_PermSOMLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(15, 'get_PermSOMLink', ((1, 'pVal'),)))
    IGPMConstants.get_PermSOMLogging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(16, 'get_PermSOMLogging', ((1, 'pVal'),)))
    IGPMConstants.get_PermSOMPlanning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(17, 'get_PermSOMPlanning', ((1, 'pVal'),)))
    IGPMConstants.get_PermSOMGPOCreate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(18, 'get_PermSOMGPOCreate', ((1, 'pVal'),)))
    IGPMConstants.get_PermSOMWMICreate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(19, 'get_PermSOMWMICreate', ((1, 'pVal'),)))
    IGPMConstants.get_PermSOMWMIFullControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(20, 'get_PermSOMWMIFullControl', ((1, 'pVal'),)))
    IGPMConstants.get_SearchPropertyGPOPermissions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(21, 'get_SearchPropertyGPOPermissions', ((1, 'pVal'),)))
    IGPMConstants.get_SearchPropertyGPOEffectivePermissions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(22, 'get_SearchPropertyGPOEffectivePermissions', ((1, 'pVal'),)))
    IGPMConstants.get_SearchPropertyGPODisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(23, 'get_SearchPropertyGPODisplayName', ((1, 'pVal'),)))
    IGPMConstants.get_SearchPropertyGPOWMIFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(24, 'get_SearchPropertyGPOWMIFilter', ((1, 'pVal'),)))
    IGPMConstants.get_SearchPropertyGPOID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(25, 'get_SearchPropertyGPOID', ((1, 'pVal'),)))
    IGPMConstants.get_SearchPropertyGPOComputerExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(26, 'get_SearchPropertyGPOComputerExtensions', ((1, 'pVal'),)))
    IGPMConstants.get_SearchPropertyGPOUserExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(27, 'get_SearchPropertyGPOUserExtensions', ((1, 'pVal'),)))
    IGPMConstants.get_SearchPropertySOMLinks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(28, 'get_SearchPropertySOMLinks', ((1, 'pVal'),)))
    IGPMConstants.get_SearchPropertyGPODomain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(29, 'get_SearchPropertyGPODomain', ((1, 'pVal'),)))
    IGPMConstants.get_SearchPropertyBackupMostRecent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(30, 'get_SearchPropertyBackupMostRecent', ((1, 'pVal'),)))
    IGPMConstants.get_SearchOpEquals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchOperation))(31, 'get_SearchOpEquals', ((1, 'pVal'),)))
    IGPMConstants.get_SearchOpContains = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchOperation))(32, 'get_SearchOpContains', ((1, 'pVal'),)))
    IGPMConstants.get_SearchOpNotContains = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchOperation))(33, 'get_SearchOpNotContains', ((1, 'pVal'),)))
    IGPMConstants.get_SearchOpNotEquals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchOperation))(34, 'get_SearchOpNotEquals', ((1, 'pVal'),)))
    IGPMConstants.get_UsePDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(35, 'get_UsePDC', ((1, 'pVal'),)))
    IGPMConstants.get_UseAnyDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(36, 'get_UseAnyDC', ((1, 'pVal'),)))
    IGPMConstants.get_DoNotUseW2KDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(37, 'get_DoNotUseW2KDC', ((1, 'pVal'),)))
    IGPMConstants.get_SOMSite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSOMType))(38, 'get_SOMSite', ((1, 'pVal'),)))
    IGPMConstants.get_SOMDomain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSOMType))(39, 'get_SOMDomain', ((1, 'pVal'),)))
    IGPMConstants.get_SOMOU = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSOMType))(40, 'get_SOMOU', ((1, 'pVal'),)))
    IGPMConstants.get_SecurityFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL,POINTER(Int32))(41, 'get_SecurityFlags', ((1, 'vbOwner'),(1, 'vbGroup'),(1, 'vbDACL'),(1, 'vbSACL'),(1, 'pVal'),)))
    IGPMConstants.get_DoNotValidateDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(42, 'get_DoNotValidateDC', ((1, 'pVal'),)))
    IGPMConstants.get_ReportHTML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMReportType))(43, 'get_ReportHTML', ((1, 'pVal'),)))
    IGPMConstants.get_ReportXML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMReportType))(44, 'get_ReportXML', ((1, 'pVal'),)))
    IGPMConstants.get_RSOPModeUnknown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMRSOPMode))(45, 'get_RSOPModeUnknown', ((1, 'pVal'),)))
    IGPMConstants.get_RSOPModePlanning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMRSOPMode))(46, 'get_RSOPModePlanning', ((1, 'pVal'),)))
    IGPMConstants.get_RSOPModeLogging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMRSOPMode))(47, 'get_RSOPModeLogging', ((1, 'pVal'),)))
    IGPMConstants.get_EntryTypeUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMEntryType))(48, 'get_EntryTypeUser', ((1, 'pVal'),)))
    IGPMConstants.get_EntryTypeComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMEntryType))(49, 'get_EntryTypeComputer', ((1, 'pVal'),)))
    IGPMConstants.get_EntryTypeLocalGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMEntryType))(50, 'get_EntryTypeLocalGroup', ((1, 'pVal'),)))
    IGPMConstants.get_EntryTypeGlobalGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMEntryType))(51, 'get_EntryTypeGlobalGroup', ((1, 'pVal'),)))
    IGPMConstants.get_EntryTypeUniversalGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMEntryType))(52, 'get_EntryTypeUniversalGroup', ((1, 'pVal'),)))
    IGPMConstants.get_EntryTypeUNCPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMEntryType))(53, 'get_EntryTypeUNCPath', ((1, 'pVal'),)))
    IGPMConstants.get_EntryTypeUnknown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMEntryType))(54, 'get_EntryTypeUnknown', ((1, 'pVal'),)))
    IGPMConstants.get_DestinationOptionSameAsSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMDestinationOption))(55, 'get_DestinationOptionSameAsSource', ((1, 'pVal'),)))
    IGPMConstants.get_DestinationOptionNone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMDestinationOption))(56, 'get_DestinationOptionNone', ((1, 'pVal'),)))
    IGPMConstants.get_DestinationOptionByRelativeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMDestinationOption))(57, 'get_DestinationOptionByRelativeName', ((1, 'pVal'),)))
    IGPMConstants.get_DestinationOptionSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMDestinationOption))(58, 'get_DestinationOptionSet', ((1, 'pVal'),)))
    IGPMConstants.get_MigrationTableOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(59, 'get_MigrationTableOnly', ((1, 'pVal'),)))
    IGPMConstants.get_ProcessSecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(60, 'get_ProcessSecurity', ((1, 'pVal'),)))
    IGPMConstants.get_RsopLoggingNoComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(61, 'get_RsopLoggingNoComputer', ((1, 'pVal'),)))
    IGPMConstants.get_RsopLoggingNoUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(62, 'get_RsopLoggingNoUser', ((1, 'pVal'),)))
    IGPMConstants.get_RsopPlanningAssumeSlowLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(63, 'get_RsopPlanningAssumeSlowLink', ((1, 'pVal'),)))
    IGPMConstants.get_RsopPlanningLoopbackOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL,POINTER(Int32))(64, 'get_RsopPlanningLoopbackOption', ((1, 'vbMerge'),(1, 'pVal'),)))
    IGPMConstants.get_RsopPlanningAssumeUserWQLFilterTrue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(65, 'get_RsopPlanningAssumeUserWQLFilterTrue', ((1, 'pVal'),)))
    IGPMConstants.get_RsopPlanningAssumeCompWQLFilterTrue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(66, 'get_RsopPlanningAssumeCompWQLFilterTrue', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IGPMConstants
def _define_IGPMConstants2_head():
    class IGPMConstants2(win32more.System.GroupPolicy.IGPMConstants_head):
        Guid = Guid('05ae21b0-ac09-4032-a2-6f-9e-7d-a7-86-dc-19')
    return IGPMConstants2
def _define_IGPMConstants2():
    IGPMConstants2 = win32more.System.GroupPolicy.IGPMConstants2_head
    IGPMConstants2.get_BackupTypeGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMBackupType))(67, 'get_BackupTypeGPO', ((1, 'pVal'),)))
    IGPMConstants2.get_BackupTypeStarterGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMBackupType))(68, 'get_BackupTypeStarterGPO', ((1, 'pVal'),)))
    IGPMConstants2.get_StarterGPOTypeSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMStarterGPOType))(69, 'get_StarterGPOTypeSystem', ((1, 'pVal'),)))
    IGPMConstants2.get_StarterGPOTypeCustom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMStarterGPOType))(70, 'get_StarterGPOTypeCustom', ((1, 'pVal'),)))
    IGPMConstants2.get_SearchPropertyStarterGPOPermissions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(71, 'get_SearchPropertyStarterGPOPermissions', ((1, 'pVal'),)))
    IGPMConstants2.get_SearchPropertyStarterGPOEffectivePermissions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(72, 'get_SearchPropertyStarterGPOEffectivePermissions', ((1, 'pVal'),)))
    IGPMConstants2.get_SearchPropertyStarterGPODisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(73, 'get_SearchPropertyStarterGPODisplayName', ((1, 'pVal'),)))
    IGPMConstants2.get_SearchPropertyStarterGPOID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(74, 'get_SearchPropertyStarterGPOID', ((1, 'pVal'),)))
    IGPMConstants2.get_SearchPropertyStarterGPODomain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSearchProperty))(75, 'get_SearchPropertyStarterGPODomain', ((1, 'pVal'),)))
    IGPMConstants2.get_PermStarterGPORead = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(76, 'get_PermStarterGPORead', ((1, 'pVal'),)))
    IGPMConstants2.get_PermStarterGPOEdit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(77, 'get_PermStarterGPOEdit', ((1, 'pVal'),)))
    IGPMConstants2.get_PermStarterGPOFullControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(78, 'get_PermStarterGPOFullControl', ((1, 'pVal'),)))
    IGPMConstants2.get_PermStarterGPOCustom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(79, 'get_PermStarterGPOCustom', ((1, 'pVal'),)))
    IGPMConstants2.get_ReportLegacy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMReportingOptions))(80, 'get_ReportLegacy', ((1, 'pVal'),)))
    IGPMConstants2.get_ReportComments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMReportingOptions))(81, 'get_ReportComments', ((1, 'pVal'),)))
    win32more.System.GroupPolicy.IGPMConstants
    return IGPMConstants2
def _define_IGPMCSECollection_head():
    class IGPMCSECollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('2e52a97d-0a4a-4a6f-85-db-20-16-22-45-5d-a0')
    return IGPMCSECollection
def _define_IGPMCSECollection():
    IGPMCSECollection = win32more.System.GroupPolicy.IGPMCSECollection_head
    IGPMCSECollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pVal'),)))
    IGPMCSECollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pVal'),)))
    IGPMCSECollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(9, 'get__NewEnum', ((1, 'ppIGPMCSEs'),)))
    win32more.System.Com.IDispatch
    return IGPMCSECollection
def _define_IGPMDomain_head():
    class IGPMDomain(win32more.System.Com.IDispatch_head):
        Guid = Guid('6b21cc14-5a00-4f44-a7-38-fe-ec-8a-94-c7-e3')
    return IGPMDomain
def _define_IGPMDomain():
    IGPMDomain = win32more.System.GroupPolicy.IGPMDomain_head
    IGPMDomain.get_DomainController = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_DomainController', ((1, 'pVal'),)))
    IGPMDomain.get_Domain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Domain', ((1, 'pVal'),)))
    IGPMDomain.CreateGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMGPO_head))(9, 'CreateGPO', ((1, 'ppNewGPO'),)))
    IGPMDomain.GetGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMGPO_head))(10, 'GetGPO', ((1, 'bstrGuid'),(1, 'ppGPO'),)))
    IGPMDomain.SearchGPOs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMSearchCriteria_head,POINTER(win32more.System.GroupPolicy.IGPMGPOCollection_head))(11, 'SearchGPOs', ((1, 'pIGPMSearchCriteria'),(1, 'ppIGPMGPOCollection'),)))
    IGPMDomain.RestoreGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMBackup_head,Int32,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(12, 'RestoreGPO', ((1, 'pIGPMBackup'),(1, 'lDCFlags'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMDomain.GetSOM = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMSOM_head))(13, 'GetSOM', ((1, 'bstrPath'),(1, 'ppSOM'),)))
    IGPMDomain.SearchSOMs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMSearchCriteria_head,POINTER(win32more.System.GroupPolicy.IGPMSOMCollection_head))(14, 'SearchSOMs', ((1, 'pIGPMSearchCriteria'),(1, 'ppIGPMSOMCollection'),)))
    IGPMDomain.GetWMIFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMWMIFilter_head))(15, 'GetWMIFilter', ((1, 'bstrPath'),(1, 'ppWMIFilter'),)))
    IGPMDomain.SearchWMIFilters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMSearchCriteria_head,POINTER(win32more.System.GroupPolicy.IGPMWMIFilterCollection_head))(16, 'SearchWMIFilters', ((1, 'pIGPMSearchCriteria'),(1, 'ppIGPMWMIFilterCollection'),)))
    win32more.System.Com.IDispatch
    return IGPMDomain
def _define_IGPMDomain2_head():
    class IGPMDomain2(win32more.System.GroupPolicy.IGPMDomain_head):
        Guid = Guid('7ca6bb8b-f1eb-490a-93-8d-3c-4e-51-c7-68-e6')
    return IGPMDomain2
def _define_IGPMDomain2():
    IGPMDomain2 = win32more.System.GroupPolicy.IGPMDomain2_head
    IGPMDomain2.CreateStarterGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMStarterGPO_head))(17, 'CreateStarterGPO', ((1, 'ppnewTemplate'),)))
    IGPMDomain2.CreateGPOFromStarterGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMStarterGPO_head,POINTER(win32more.System.GroupPolicy.IGPMGPO_head))(18, 'CreateGPOFromStarterGPO', ((1, 'pGPOTemplate'),(1, 'ppnewGPO'),)))
    IGPMDomain2.GetStarterGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMStarterGPO_head))(19, 'GetStarterGPO', ((1, 'bstrGuid'),(1, 'ppTemplate'),)))
    IGPMDomain2.SearchStarterGPOs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMSearchCriteria_head,POINTER(win32more.System.GroupPolicy.IGPMStarterGPOCollection_head))(20, 'SearchStarterGPOs', ((1, 'pIGPMSearchCriteria'),(1, 'ppIGPMTemplateCollection'),)))
    IGPMDomain2.LoadStarterGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(21, 'LoadStarterGPO', ((1, 'bstrLoadFile'),(1, 'bOverwrite'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMDomain2.RestoreStarterGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMStarterGPOBackup_head,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(22, 'RestoreStarterGPO', ((1, 'pIGPMTmplBackup'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    win32more.System.GroupPolicy.IGPMDomain
    return IGPMDomain2
def _define_IGPMDomain3_head():
    class IGPMDomain3(win32more.System.GroupPolicy.IGPMDomain2_head):
        Guid = Guid('0077fdfe-88c7-4acf-a1-1d-d1-0a-7c-31-0a-03')
    return IGPMDomain3
def _define_IGPMDomain3():
    IGPMDomain3 = win32more.System.GroupPolicy.IGPMDomain3_head
    IGPMDomain3.GenerateReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMReportType,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(23, 'GenerateReport', ((1, 'gpmReportType'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMDomain3.get_InfrastructureDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(24, 'get_InfrastructureDC', ((1, 'pVal'),)))
    IGPMDomain3.put_InfrastructureDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(25, 'put_InfrastructureDC', ((1, 'newVal'),)))
    IGPMDomain3.put_InfrastructureFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(26, 'put_InfrastructureFlags', ((1, 'dwFlags'),)))
    win32more.System.GroupPolicy.IGPMDomain2
    return IGPMDomain3
def _define_IGPMGPO_head():
    class IGPMGPO(win32more.System.Com.IDispatch_head):
        Guid = Guid('58cc4352-1ca3-48e5-98-64-1d-a4-d6-e0-d6-0f')
    return IGPMGPO
def _define_IGPMGPO():
    IGPMGPO = win32more.System.GroupPolicy.IGPMGPO_head
    IGPMGPO.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_DisplayName', ((1, 'pVal'),)))
    IGPMGPO.put_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_DisplayName', ((1, 'newVal'),)))
    IGPMGPO.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Path', ((1, 'pVal'),)))
    IGPMGPO.get_ID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_ID', ((1, 'pVal'),)))
    IGPMGPO.get_DomainName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_DomainName', ((1, 'pVal'),)))
    IGPMGPO.get_CreationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(12, 'get_CreationTime', ((1, 'pDate'),)))
    IGPMGPO.get_ModificationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(13, 'get_ModificationTime', ((1, 'pDate'),)))
    IGPMGPO.get_UserDSVersionNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(14, 'get_UserDSVersionNumber', ((1, 'pVal'),)))
    IGPMGPO.get_ComputerDSVersionNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_ComputerDSVersionNumber', ((1, 'pVal'),)))
    IGPMGPO.get_UserSysvolVersionNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_UserSysvolVersionNumber', ((1, 'pVal'),)))
    IGPMGPO.get_ComputerSysvolVersionNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(17, 'get_ComputerSysvolVersionNumber', ((1, 'pVal'),)))
    IGPMGPO.GetWMIFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMWMIFilter_head))(18, 'GetWMIFilter', ((1, 'ppIGPMWMIFilter'),)))
    IGPMGPO.SetWMIFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMWMIFilter_head)(19, 'SetWMIFilter', ((1, 'pIGPMWMIFilter'),)))
    IGPMGPO.SetUserEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(20, 'SetUserEnabled', ((1, 'vbEnabled'),)))
    IGPMGPO.SetComputerEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(21, 'SetComputerEnabled', ((1, 'vbEnabled'),)))
    IGPMGPO.IsUserEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(22, 'IsUserEnabled', ((1, 'pvbEnabled'),)))
    IGPMGPO.IsComputerEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(23, 'IsComputerEnabled', ((1, 'pvbEnabled'),)))
    IGPMGPO.GetSecurityInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMSecurityInfo_head))(24, 'GetSecurityInfo', ((1, 'ppSecurityInfo'),)))
    IGPMGPO.SetSecurityInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMSecurityInfo_head)(25, 'SetSecurityInfo', ((1, 'pSecurityInfo'),)))
    IGPMGPO.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(26, 'Delete', ()))
    IGPMGPO.Backup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(27, 'Backup', ((1, 'bstrBackupDir'),(1, 'bstrComment'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMGPO.Import = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.GroupPolicy.IGPMBackup_head,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(28, 'Import', ((1, 'lFlags'),(1, 'pIGPMBackup'),(1, 'pvarMigrationTable'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMGPO.GenerateReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMReportType,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(29, 'GenerateReport', ((1, 'gpmReportType'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMGPO.GenerateReportToFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMReportType,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMResult_head))(30, 'GenerateReportToFile', ((1, 'gpmReportType'),(1, 'bstrTargetFilePath'),(1, 'ppIGPMResult'),)))
    IGPMGPO.CopyTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.GroupPolicy.IGPMDomain_head,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(31, 'CopyTo', ((1, 'lFlags'),(1, 'pIGPMDomain'),(1, 'pvarNewDisplayName'),(1, 'pvarMigrationTable'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMGPO.SetSecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.IDispatch_head)(32, 'SetSecurityDescriptor', ((1, 'lFlags'),(1, 'pSD'),)))
    IGPMGPO.GetSecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.IDispatch_head))(33, 'GetSecurityDescriptor', ((1, 'lFlags'),(1, 'ppSD'),)))
    IGPMGPO.IsACLConsistent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(34, 'IsACLConsistent', ((1, 'pvbConsistent'),)))
    IGPMGPO.MakeACLConsistent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(35, 'MakeACLConsistent', ()))
    win32more.System.Com.IDispatch
    return IGPMGPO
def _define_IGPMGPO2_head():
    class IGPMGPO2(win32more.System.GroupPolicy.IGPMGPO_head):
        Guid = Guid('8a66a210-b78b-4d99-88-e2-c3-06-a8-17-c9-25')
    return IGPMGPO2
def _define_IGPMGPO2():
    IGPMGPO2 = win32more.System.GroupPolicy.IGPMGPO2_head
    IGPMGPO2.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(36, 'get_Description', ((1, 'pVal'),)))
    IGPMGPO2.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(37, 'put_Description', ((1, 'newVal'),)))
    win32more.System.GroupPolicy.IGPMGPO
    return IGPMGPO2
def _define_IGPMGPO3_head():
    class IGPMGPO3(win32more.System.GroupPolicy.IGPMGPO2_head):
        Guid = Guid('7cf123a1-f94a-4112-bf-ae-6a-a1-db-9c-b2-48')
    return IGPMGPO3
def _define_IGPMGPO3():
    IGPMGPO3 = win32more.System.GroupPolicy.IGPMGPO3_head
    IGPMGPO3.get_InfrastructureDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(38, 'get_InfrastructureDC', ((1, 'pVal'),)))
    IGPMGPO3.put_InfrastructureDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(39, 'put_InfrastructureDC', ((1, 'newVal'),)))
    IGPMGPO3.put_InfrastructureFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(40, 'put_InfrastructureFlags', ((1, 'dwFlags'),)))
    win32more.System.GroupPolicy.IGPMGPO2
    return IGPMGPO3
def _define_IGPMGPOCollection_head():
    class IGPMGPOCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('f0f0d5cf-70ca-4c39-9e-29-b6-42-f8-72-6c-01')
    return IGPMGPOCollection
def _define_IGPMGPOCollection():
    IGPMGPOCollection = win32more.System.GroupPolicy.IGPMGPOCollection_head
    IGPMGPOCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pVal'),)))
    IGPMGPOCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pVal'),)))
    IGPMGPOCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(9, 'get__NewEnum', ((1, 'ppIGPMGPOs'),)))
    win32more.System.Com.IDispatch
    return IGPMGPOCollection
def _define_IGPMGPOLink_head():
    class IGPMGPOLink(win32more.System.Com.IDispatch_head):
        Guid = Guid('434b99bd-5de7-478a-80-9c-c2-51-72-1d-f7-0c')
    return IGPMGPOLink
def _define_IGPMGPOLink():
    IGPMGPOLink = win32more.System.GroupPolicy.IGPMGPOLink_head
    IGPMGPOLink.get_GPOID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_GPOID', ((1, 'pVal'),)))
    IGPMGPOLink.get_GPODomain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_GPODomain', ((1, 'pVal'),)))
    IGPMGPOLink.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_Enabled', ((1, 'pVal'),)))
    IGPMGPOLink.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(10, 'put_Enabled', ((1, 'newVal'),)))
    IGPMGPOLink.get_Enforced = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_Enforced', ((1, 'pVal'),)))
    IGPMGPOLink.put_Enforced = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(12, 'put_Enforced', ((1, 'newVal'),)))
    IGPMGPOLink.get_SOMLinkOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_SOMLinkOrder', ((1, 'lVal'),)))
    IGPMGPOLink.get_SOM = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMSOM_head))(14, 'get_SOM', ((1, 'ppIGPMSOM'),)))
    IGPMGPOLink.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'Delete', ()))
    win32more.System.Com.IDispatch
    return IGPMGPOLink
def _define_IGPMGPOLinksCollection_head():
    class IGPMGPOLinksCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('189d7b68-16bd-4d0d-a2-ec-2e-6a-a2-28-8c-7f')
    return IGPMGPOLinksCollection
def _define_IGPMGPOLinksCollection():
    IGPMGPOLinksCollection = win32more.System.GroupPolicy.IGPMGPOLinksCollection_head
    IGPMGPOLinksCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pVal'),)))
    IGPMGPOLinksCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pVal'),)))
    IGPMGPOLinksCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(9, 'get__NewEnum', ((1, 'ppIGPMLinks'),)))
    win32more.System.Com.IDispatch
    return IGPMGPOLinksCollection
def _define_IGPMMapEntry_head():
    class IGPMMapEntry(win32more.System.Com.IDispatch_head):
        Guid = Guid('8e79ad06-2381-4444-be-4c-ff-69-3e-6e-6f-2b')
    return IGPMMapEntry
def _define_IGPMMapEntry():
    IGPMMapEntry = win32more.System.GroupPolicy.IGPMMapEntry_head
    IGPMMapEntry.get_Source = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Source', ((1, 'pbstrSource'),)))
    IGPMMapEntry.get_Destination = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Destination', ((1, 'pbstrDestination'),)))
    IGPMMapEntry.get_DestinationOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMDestinationOption))(9, 'get_DestinationOption', ((1, 'pgpmDestOption'),)))
    IGPMMapEntry.get_EntryType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMEntryType))(10, 'get_EntryType', ((1, 'pgpmEntryType'),)))
    win32more.System.Com.IDispatch
    return IGPMMapEntry
def _define_IGPMMapEntryCollection_head():
    class IGPMMapEntryCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('bb0bf49b-e53f-443f-b8-07-8b-e2-2b-fb-6d-42')
    return IGPMMapEntryCollection
def _define_IGPMMapEntryCollection():
    IGPMMapEntryCollection = win32more.System.GroupPolicy.IGPMMapEntryCollection_head
    IGPMMapEntryCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pVal'),)))
    IGPMMapEntryCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pVal'),)))
    IGPMMapEntryCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(9, 'get__NewEnum', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IGPMMapEntryCollection
def _define_IGPMMigrationTable_head():
    class IGPMMigrationTable(win32more.System.Com.IDispatch_head):
        Guid = Guid('48f823b1-efaf-470b-b6-ed-40-d1-4e-e1-a4-ec')
    return IGPMMigrationTable
def _define_IGPMMigrationTable():
    IGPMMigrationTable = win32more.System.GroupPolicy.IGPMMigrationTable_head
    IGPMMigrationTable.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(7, 'Save', ((1, 'bstrMigrationTablePath'),)))
    IGPMMigrationTable.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT)(8, 'Add', ((1, 'lFlags'),(1, 'var'),)))
    IGPMMigrationTable.AddEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.GroupPolicy.GPMEntryType,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMMapEntry_head))(9, 'AddEntry', ((1, 'bstrSource'),(1, 'gpmEntryType'),(1, 'pvarDestination'),(1, 'ppEntry'),)))
    IGPMMigrationTable.GetEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMMapEntry_head))(10, 'GetEntry', ((1, 'bstrSource'),(1, 'ppEntry'),)))
    IGPMMigrationTable.DeleteEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'DeleteEntry', ((1, 'bstrSource'),)))
    IGPMMigrationTable.UpdateDestination = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMMapEntry_head))(12, 'UpdateDestination', ((1, 'bstrSource'),(1, 'pvarDestination'),(1, 'ppEntry'),)))
    IGPMMigrationTable.Validate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMResult_head))(13, 'Validate', ((1, 'ppResult'),)))
    IGPMMigrationTable.GetEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMMapEntryCollection_head))(14, 'GetEntries', ((1, 'ppEntries'),)))
    win32more.System.Com.IDispatch
    return IGPMMigrationTable
def _define_IGPMPermission_head():
    class IGPMPermission(win32more.System.Com.IDispatch_head):
        Guid = Guid('35ebca40-e1a1-4a02-89-05-d7-94-16-fb-46-4a')
    return IGPMPermission
def _define_IGPMPermission():
    IGPMPermission = win32more.System.GroupPolicy.IGPMPermission_head
    IGPMPermission.get_Inherited = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_Inherited', ((1, 'pVal'),)))
    IGPMPermission.get_Inheritable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(8, 'get_Inheritable', ((1, 'pVal'),)))
    IGPMPermission.get_Denied = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_Denied', ((1, 'pVal'),)))
    IGPMPermission.get_Permission = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMPermissionType))(10, 'get_Permission', ((1, 'pVal'),)))
    IGPMPermission.get_Trustee = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMTrustee_head))(11, 'get_Trustee', ((1, 'ppIGPMTrustee'),)))
    win32more.System.Com.IDispatch
    return IGPMPermission
def _define_IGPMResult_head():
    class IGPMResult(win32more.System.Com.IDispatch_head):
        Guid = Guid('86dff7e9-f76f-42ab-95-70-ce-bc-6b-e8-a5-2d')
    return IGPMResult
def _define_IGPMResult():
    IGPMResult = win32more.System.GroupPolicy.IGPMResult_head
    IGPMResult.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMStatusMsgCollection_head))(7, 'get_Status', ((1, 'ppIGPMStatusMsgCollection'),)))
    IGPMResult.get_Result = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Result', ((1, 'pvarResult'),)))
    IGPMResult.OverallStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'OverallStatus', ()))
    win32more.System.Com.IDispatch
    return IGPMResult
def _define_IGPMRSOP_head():
    class IGPMRSOP(win32more.System.Com.IDispatch_head):
        Guid = Guid('49ed785a-3237-4ff2-b1-f0-fd-f5-a8-d5-a1-ee')
    return IGPMRSOP
def _define_IGPMRSOP():
    IGPMRSOP = win32more.System.GroupPolicy.IGPMRSOP_head
    IGPMRSOP.get_Mode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMRSOPMode))(7, 'get_Mode', ((1, 'pVal'),)))
    IGPMRSOP.get_Namespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Namespace', ((1, 'bstrVal'),)))
    IGPMRSOP.put_LoggingComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'put_LoggingComputer', ((1, 'bstrVal'),)))
    IGPMRSOP.get_LoggingComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_LoggingComputer', ((1, 'bstrVal'),)))
    IGPMRSOP.put_LoggingUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'put_LoggingUser', ((1, 'bstrVal'),)))
    IGPMRSOP.get_LoggingUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_LoggingUser', ((1, 'bstrVal'),)))
    IGPMRSOP.put_LoggingFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(13, 'put_LoggingFlags', ((1, 'lVal'),)))
    IGPMRSOP.get_LoggingFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(14, 'get_LoggingFlags', ((1, 'lVal'),)))
    IGPMRSOP.put_PlanningFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(15, 'put_PlanningFlags', ((1, 'lVal'),)))
    IGPMRSOP.get_PlanningFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_PlanningFlags', ((1, 'lVal'),)))
    IGPMRSOP.put_PlanningDomainController = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(17, 'put_PlanningDomainController', ((1, 'bstrVal'),)))
    IGPMRSOP.get_PlanningDomainController = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_PlanningDomainController', ((1, 'bstrVal'),)))
    IGPMRSOP.put_PlanningSiteName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(19, 'put_PlanningSiteName', ((1, 'bstrVal'),)))
    IGPMRSOP.get_PlanningSiteName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_PlanningSiteName', ((1, 'bstrVal'),)))
    IGPMRSOP.put_PlanningUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_PlanningUser', ((1, 'bstrVal'),)))
    IGPMRSOP.get_PlanningUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_PlanningUser', ((1, 'bstrVal'),)))
    IGPMRSOP.put_PlanningUserSOM = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'put_PlanningUserSOM', ((1, 'bstrVal'),)))
    IGPMRSOP.get_PlanningUserSOM = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(24, 'get_PlanningUserSOM', ((1, 'bstrVal'),)))
    IGPMRSOP.put_PlanningUserWMIFilters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(25, 'put_PlanningUserWMIFilters', ((1, 'varVal'),)))
    IGPMRSOP.get_PlanningUserWMIFilters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(26, 'get_PlanningUserWMIFilters', ((1, 'varVal'),)))
    IGPMRSOP.put_PlanningUserSecurityGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(27, 'put_PlanningUserSecurityGroups', ((1, 'varVal'),)))
    IGPMRSOP.get_PlanningUserSecurityGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(28, 'get_PlanningUserSecurityGroups', ((1, 'varVal'),)))
    IGPMRSOP.put_PlanningComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(29, 'put_PlanningComputer', ((1, 'bstrVal'),)))
    IGPMRSOP.get_PlanningComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(30, 'get_PlanningComputer', ((1, 'bstrVal'),)))
    IGPMRSOP.put_PlanningComputerSOM = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(31, 'put_PlanningComputerSOM', ((1, 'bstrVal'),)))
    IGPMRSOP.get_PlanningComputerSOM = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(32, 'get_PlanningComputerSOM', ((1, 'bstrVal'),)))
    IGPMRSOP.put_PlanningComputerWMIFilters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(33, 'put_PlanningComputerWMIFilters', ((1, 'varVal'),)))
    IGPMRSOP.get_PlanningComputerWMIFilters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(34, 'get_PlanningComputerWMIFilters', ((1, 'varVal'),)))
    IGPMRSOP.put_PlanningComputerSecurityGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(35, 'put_PlanningComputerSecurityGroups', ((1, 'varVal'),)))
    IGPMRSOP.get_PlanningComputerSecurityGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(36, 'get_PlanningComputerSecurityGroups', ((1, 'varVal'),)))
    IGPMRSOP.LoggingEnumerateUsers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(37, 'LoggingEnumerateUsers', ((1, 'varVal'),)))
    IGPMRSOP.CreateQueryResults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(38, 'CreateQueryResults', ()))
    IGPMRSOP.ReleaseQueryResults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(39, 'ReleaseQueryResults', ()))
    IGPMRSOP.GenerateReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMReportType,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(40, 'GenerateReport', ((1, 'gpmReportType'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMRSOP.GenerateReportToFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMReportType,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMResult_head))(41, 'GenerateReportToFile', ((1, 'gpmReportType'),(1, 'bstrTargetFilePath'),(1, 'ppIGPMResult'),)))
    win32more.System.Com.IDispatch
    return IGPMRSOP
def _define_IGPMSearchCriteria_head():
    class IGPMSearchCriteria(win32more.System.Com.IDispatch_head):
        Guid = Guid('d6f11c42-829b-48d4-83-f5-36-15-b6-7d-fc-22')
    return IGPMSearchCriteria
def _define_IGPMSearchCriteria():
    IGPMSearchCriteria = win32more.System.GroupPolicy.IGPMSearchCriteria_head
    IGPMSearchCriteria.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMSearchProperty,win32more.System.GroupPolicy.GPMSearchOperation,win32more.System.Com.VARIANT)(7, 'Add', ((1, 'searchProperty'),(1, 'searchOperation'),(1, 'varValue'),)))
    win32more.System.Com.IDispatch
    return IGPMSearchCriteria
def _define_IGPMSecurityInfo_head():
    class IGPMSecurityInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('b6c31ed4-1c93-4d3e-ae-84-eb-6d-61-16-1b-60')
    return IGPMSecurityInfo
def _define_IGPMSecurityInfo():
    IGPMSecurityInfo = win32more.System.GroupPolicy.IGPMSecurityInfo_head
    IGPMSecurityInfo.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pVal'),)))
    IGPMSecurityInfo.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pVal'),)))
    IGPMSecurityInfo.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(9, 'get__NewEnum', ((1, 'ppEnum'),)))
    IGPMSecurityInfo.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMPermission_head)(10, 'Add', ((1, 'pPerm'),)))
    IGPMSecurityInfo.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMPermission_head)(11, 'Remove', ((1, 'pPerm'),)))
    IGPMSecurityInfo.RemoveTrustee = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'RemoveTrustee', ((1, 'bstrTrustee'),)))
    win32more.System.Com.IDispatch
    return IGPMSecurityInfo
def _define_IGPMSitesContainer_head():
    class IGPMSitesContainer(win32more.System.Com.IDispatch_head):
        Guid = Guid('4725a899-2782-4d27-a6-bb-d4-99-24-6f-fd-72')
    return IGPMSitesContainer
def _define_IGPMSitesContainer():
    IGPMSitesContainer = win32more.System.GroupPolicy.IGPMSitesContainer_head
    IGPMSitesContainer.get_DomainController = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_DomainController', ((1, 'pVal'),)))
    IGPMSitesContainer.get_Domain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Domain', ((1, 'pVal'),)))
    IGPMSitesContainer.get_Forest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Forest', ((1, 'pVal'),)))
    IGPMSitesContainer.GetSite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMSOM_head))(10, 'GetSite', ((1, 'bstrSiteName'),(1, 'ppSOM'),)))
    IGPMSitesContainer.SearchSites = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMSearchCriteria_head,POINTER(win32more.System.GroupPolicy.IGPMSOMCollection_head))(11, 'SearchSites', ((1, 'pIGPMSearchCriteria'),(1, 'ppIGPMSOMCollection'),)))
    win32more.System.Com.IDispatch
    return IGPMSitesContainer
def _define_IGPMSOM_head():
    class IGPMSOM(win32more.System.Com.IDispatch_head):
        Guid = Guid('c0a7f09e-05a1-4f0c-81-58-9e-5c-33-68-4f-6b')
    return IGPMSOM
def _define_IGPMSOM():
    IGPMSOM = win32more.System.GroupPolicy.IGPMSOM_head
    IGPMSOM.get_GPOInheritanceBlocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_GPOInheritanceBlocked', ((1, 'pVal'),)))
    IGPMSOM.put_GPOInheritanceBlocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(8, 'put_GPOInheritanceBlocked', ((1, 'newVal'),)))
    IGPMSOM.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Name', ((1, 'pVal'),)))
    IGPMSOM.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_Path', ((1, 'pVal'),)))
    IGPMSOM.CreateGPOLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.GroupPolicy.IGPMGPO_head,POINTER(win32more.System.GroupPolicy.IGPMGPOLink_head))(11, 'CreateGPOLink', ((1, 'lLinkPos'),(1, 'pGPO'),(1, 'ppNewGPOLink'),)))
    IGPMSOM.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMSOMType))(12, 'get_Type', ((1, 'pVal'),)))
    IGPMSOM.GetGPOLinks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMGPOLinksCollection_head))(13, 'GetGPOLinks', ((1, 'ppGPOLinks'),)))
    IGPMSOM.GetInheritedGPOLinks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMGPOLinksCollection_head))(14, 'GetInheritedGPOLinks', ((1, 'ppGPOLinks'),)))
    IGPMSOM.GetSecurityInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMSecurityInfo_head))(15, 'GetSecurityInfo', ((1, 'ppSecurityInfo'),)))
    IGPMSOM.SetSecurityInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMSecurityInfo_head)(16, 'SetSecurityInfo', ((1, 'pSecurityInfo'),)))
    win32more.System.Com.IDispatch
    return IGPMSOM
def _define_IGPMSOMCollection_head():
    class IGPMSOMCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('adc1688e-00e4-4495-ab-ba-be-d2-00-df-0c-ab')
    return IGPMSOMCollection
def _define_IGPMSOMCollection():
    IGPMSOMCollection = win32more.System.GroupPolicy.IGPMSOMCollection_head
    IGPMSOMCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pVal'),)))
    IGPMSOMCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pVal'),)))
    IGPMSOMCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(9, 'get__NewEnum', ((1, 'ppIGPMSOM'),)))
    win32more.System.Com.IDispatch
    return IGPMSOMCollection
def _define_IGPMStarterGPO_head():
    class IGPMStarterGPO(win32more.System.Com.IDispatch_head):
        Guid = Guid('dfc3f61b-8880-4490-93-37-d2-9c-7b-a8-c2-f0')
    return IGPMStarterGPO
def _define_IGPMStarterGPO():
    IGPMStarterGPO = win32more.System.GroupPolicy.IGPMStarterGPO_head
    IGPMStarterGPO.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_DisplayName', ((1, 'pVal'),)))
    IGPMStarterGPO.put_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_DisplayName', ((1, 'newVal'),)))
    IGPMStarterGPO.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Description', ((1, 'pVal'),)))
    IGPMStarterGPO.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_Description', ((1, 'newVal'),)))
    IGPMStarterGPO.get_Author = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_Author', ((1, 'pVal'),)))
    IGPMStarterGPO.get_Product = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Product', ((1, 'pVal'),)))
    IGPMStarterGPO.get_CreationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(13, 'get_CreationTime', ((1, 'pVal'),)))
    IGPMStarterGPO.get_ID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_ID', ((1, 'pVal'),)))
    IGPMStarterGPO.get_ModifiedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(15, 'get_ModifiedTime', ((1, 'pVal'),)))
    IGPMStarterGPO.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMStarterGPOType))(16, 'get_Type', ((1, 'pVal'),)))
    IGPMStarterGPO.get_ComputerVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16))(17, 'get_ComputerVersion', ((1, 'pVal'),)))
    IGPMStarterGPO.get_UserVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16))(18, 'get_UserVersion', ((1, 'pVal'),)))
    IGPMStarterGPO.get_StarterGPOVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_StarterGPOVersion', ((1, 'pVal'),)))
    IGPMStarterGPO.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(20, 'Delete', ()))
    IGPMStarterGPO.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(21, 'Save', ((1, 'bstrSaveFile'),(1, 'bOverwrite'),(1, 'bSaveAsSystem'),(1, 'bstrLanguage'),(1, 'bstrAuthor'),(1, 'bstrProduct'),(1, 'bstrUniqueID'),(1, 'bstrVersion'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMStarterGPO.Backup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(22, 'Backup', ((1, 'bstrBackupDir'),(1, 'bstrComment'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMStarterGPO.CopyTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(23, 'CopyTo', ((1, 'pvarNewDisplayName'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMStarterGPO.GenerateReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMReportType,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(24, 'GenerateReport', ((1, 'gpmReportType'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMStarterGPO.GenerateReportToFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMReportType,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMResult_head))(25, 'GenerateReportToFile', ((1, 'gpmReportType'),(1, 'bstrTargetFilePath'),(1, 'ppIGPMResult'),)))
    IGPMStarterGPO.GetSecurityInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMSecurityInfo_head))(26, 'GetSecurityInfo', ((1, 'ppSecurityInfo'),)))
    IGPMStarterGPO.SetSecurityInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMSecurityInfo_head)(27, 'SetSecurityInfo', ((1, 'pSecurityInfo'),)))
    win32more.System.Com.IDispatch
    return IGPMStarterGPO
def _define_IGPMStarterGPOBackup_head():
    class IGPMStarterGPOBackup(win32more.System.Com.IDispatch_head):
        Guid = Guid('51d98eda-a87e-43dd-b8-0a-0b-66-ef-19-38-d6')
    return IGPMStarterGPOBackup
def _define_IGPMStarterGPOBackup():
    IGPMStarterGPOBackup = win32more.System.GroupPolicy.IGPMStarterGPOBackup_head
    IGPMStarterGPOBackup.get_BackupDir = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_BackupDir', ((1, 'pbstrBackupDir'),)))
    IGPMStarterGPOBackup.get_Comment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Comment', ((1, 'pbstrComment'),)))
    IGPMStarterGPOBackup.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_DisplayName', ((1, 'pbstrDisplayName'),)))
    IGPMStarterGPOBackup.get_Domain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_Domain', ((1, 'pbstrTemplateDomain'),)))
    IGPMStarterGPOBackup.get_StarterGPOID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_StarterGPOID', ((1, 'pbstrTemplateID'),)))
    IGPMStarterGPOBackup.get_ID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_ID', ((1, 'pbstrID'),)))
    IGPMStarterGPOBackup.get_Timestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(13, 'get_Timestamp', ((1, 'pTimestamp'),)))
    IGPMStarterGPOBackup.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GPMStarterGPOType))(14, 'get_Type', ((1, 'pType'),)))
    IGPMStarterGPOBackup.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'Delete', ()))
    IGPMStarterGPOBackup.GenerateReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMReportType,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.GroupPolicy.IGPMResult_head))(16, 'GenerateReport', ((1, 'gpmReportType'),(1, 'pvarGPMProgress'),(1, 'pvarGPMCancel'),(1, 'ppIGPMResult'),)))
    IGPMStarterGPOBackup.GenerateReportToFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.GPMReportType,win32more.Foundation.BSTR,POINTER(win32more.System.GroupPolicy.IGPMResult_head))(17, 'GenerateReportToFile', ((1, 'gpmReportType'),(1, 'bstrTargetFilePath'),(1, 'ppIGPMResult'),)))
    win32more.System.Com.IDispatch
    return IGPMStarterGPOBackup
def _define_IGPMStarterGPOBackupCollection_head():
    class IGPMStarterGPOBackupCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('c998031d-add0-4bb5-8d-ea-29-85-05-d8-42-3b')
    return IGPMStarterGPOBackupCollection
def _define_IGPMStarterGPOBackupCollection():
    IGPMStarterGPOBackupCollection = win32more.System.GroupPolicy.IGPMStarterGPOBackupCollection_head
    IGPMStarterGPOBackupCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pVal'),)))
    IGPMStarterGPOBackupCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pVal'),)))
    IGPMStarterGPOBackupCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(9, 'get__NewEnum', ((1, 'ppIGPMTmplBackup'),)))
    win32more.System.Com.IDispatch
    return IGPMStarterGPOBackupCollection
def _define_IGPMStarterGPOCollection_head():
    class IGPMStarterGPOCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('2e522729-2219-44ad-93-3a-64-df-d6-50-c4-23')
    return IGPMStarterGPOCollection
def _define_IGPMStarterGPOCollection():
    IGPMStarterGPOCollection = win32more.System.GroupPolicy.IGPMStarterGPOCollection_head
    IGPMStarterGPOCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pVal'),)))
    IGPMStarterGPOCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pVal'),)))
    IGPMStarterGPOCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(9, 'get__NewEnum', ((1, 'ppIGPMTemplates'),)))
    win32more.System.Com.IDispatch
    return IGPMStarterGPOCollection
def _define_IGPMStatusMessage_head():
    class IGPMStatusMessage(win32more.System.Com.IDispatch_head):
        Guid = Guid('8496c22f-f3de-4a1f-8f-58-60-3c-aa-a9-3d-7b')
    return IGPMStatusMessage
def _define_IGPMStatusMessage():
    IGPMStatusMessage = win32more.System.GroupPolicy.IGPMStatusMessage_head
    IGPMStatusMessage.get_ObjectPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_ObjectPath', ((1, 'pVal'),)))
    IGPMStatusMessage.ErrorCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'ErrorCode', ()))
    IGPMStatusMessage.get_ExtensionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_ExtensionName', ((1, 'pVal'),)))
    IGPMStatusMessage.get_SettingsName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_SettingsName', ((1, 'pVal'),)))
    IGPMStatusMessage.OperationCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'OperationCode', ()))
    IGPMStatusMessage.get_Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Message', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IGPMStatusMessage
def _define_IGPMStatusMsgCollection_head():
    class IGPMStatusMsgCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('9b6e1af0-1a92-40f3-a5-9d-f3-6a-c1-f7-28-b7')
    return IGPMStatusMsgCollection
def _define_IGPMStatusMsgCollection():
    IGPMStatusMsgCollection = win32more.System.GroupPolicy.IGPMStatusMsgCollection_head
    IGPMStatusMsgCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pVal'),)))
    IGPMStatusMsgCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pVal'),)))
    IGPMStatusMsgCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(9, 'get__NewEnum', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IGPMStatusMsgCollection
def _define_IGPMTrustee_head():
    class IGPMTrustee(win32more.System.Com.IDispatch_head):
        Guid = Guid('3b466da8-c1a4-4b2a-99-9a-be-fc-dd-56-ce-fb')
    return IGPMTrustee
def _define_IGPMTrustee():
    IGPMTrustee = win32more.System.GroupPolicy.IGPMTrustee_head
    IGPMTrustee.get_TrusteeSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_TrusteeSid', ((1, 'bstrVal'),)))
    IGPMTrustee.get_TrusteeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_TrusteeName', ((1, 'bstrVal'),)))
    IGPMTrustee.get_TrusteeDomain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_TrusteeDomain', ((1, 'bstrVal'),)))
    IGPMTrustee.get_TrusteeDSPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_TrusteeDSPath', ((1, 'pVal'),)))
    IGPMTrustee.get_TrusteeType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_TrusteeType', ((1, 'lVal'),)))
    win32more.System.Com.IDispatch
    return IGPMTrustee
def _define_IGPMWMIFilter_head():
    class IGPMWMIFilter(win32more.System.Com.IDispatch_head):
        Guid = Guid('ef2ff9b4-3c27-459a-b9-79-03-83-05-ce-c7-5d')
    return IGPMWMIFilter
def _define_IGPMWMIFilter():
    IGPMWMIFilter = win32more.System.GroupPolicy.IGPMWMIFilter_head
    IGPMWMIFilter.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Path', ((1, 'pVal'),)))
    IGPMWMIFilter.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Name', ((1, 'newVal'),)))
    IGPMWMIFilter.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Name', ((1, 'pVal'),)))
    IGPMWMIFilter.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_Description', ((1, 'newVal'),)))
    IGPMWMIFilter.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_Description', ((1, 'pVal'),)))
    IGPMWMIFilter.GetQueryList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(12, 'GetQueryList', ((1, 'pQryList'),)))
    IGPMWMIFilter.GetSecurityInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.IGPMSecurityInfo_head))(13, 'GetSecurityInfo', ((1, 'ppSecurityInfo'),)))
    IGPMWMIFilter.SetSecurityInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.GroupPolicy.IGPMSecurityInfo_head)(14, 'SetSecurityInfo', ((1, 'pSecurityInfo'),)))
    win32more.System.Com.IDispatch
    return IGPMWMIFilter
def _define_IGPMWMIFilterCollection_head():
    class IGPMWMIFilterCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('5782d582-1a36-4661-8a-94-c3-c3-25-51-94-5b')
    return IGPMWMIFilterCollection
def _define_IGPMWMIFilterCollection():
    IGPMWMIFilterCollection = win32more.System.GroupPolicy.IGPMWMIFilterCollection_head
    IGPMWMIFilterCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pVal'),)))
    IGPMWMIFilterCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pVal'),)))
    IGPMWMIFilterCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(9, 'get__NewEnum', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IGPMWMIFilterCollection
def _define_IGroupPolicyObject_head():
    class IGroupPolicyObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea502723-a23d-11d1-a7-d3-00-00-f8-75-71-e3')
    return IGroupPolicyObject
def _define_IGroupPolicyObject():
    IGroupPolicyObject = win32more.System.GroupPolicy.IGroupPolicyObject_head
    IGroupPolicyObject.New = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(3, 'New', ((1, 'pszDomainName'),(1, 'pszDisplayName'),(1, 'dwFlags'),)))
    IGroupPolicyObject.OpenDSGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(4, 'OpenDSGPO', ((1, 'pszPath'),(1, 'dwFlags'),)))
    IGroupPolicyObject.OpenLocalMachineGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'OpenLocalMachineGPO', ((1, 'dwFlags'),)))
    IGroupPolicyObject.OpenRemoteMachineGPO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(6, 'OpenRemoteMachineGPO', ((1, 'pszComputerName'),(1, 'dwFlags'),)))
    IGroupPolicyObject.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(Guid),POINTER(Guid))(7, 'Save', ((1, 'bMachine'),(1, 'bAdd'),(1, 'pGuidExtension'),(1, 'pGuid'),)))
    IGroupPolicyObject.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Delete', ()))
    IGroupPolicyObject.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32)(9, 'GetName', ((1, 'pszName'),(1, 'cchMaxLength'),)))
    IGroupPolicyObject.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32)(10, 'GetDisplayName', ((1, 'pszName'),(1, 'cchMaxLength'),)))
    IGroupPolicyObject.SetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(11, 'SetDisplayName', ((1, 'pszName'),)))
    IGroupPolicyObject.GetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32)(12, 'GetPath', ((1, 'pszPath'),(1, 'cchMaxLength'),)))
    IGroupPolicyObject.GetDSPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,Int32)(13, 'GetDSPath', ((1, 'dwSection'),(1, 'pszPath'),(1, 'cchMaxPath'),)))
    IGroupPolicyObject.GetFileSysPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,Int32)(14, 'GetFileSysPath', ((1, 'dwSection'),(1, 'pszPath'),(1, 'cchMaxPath'),)))
    IGroupPolicyObject.GetRegistryKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Registry.HKEY))(15, 'GetRegistryKey', ((1, 'dwSection'),(1, 'hKey'),)))
    IGroupPolicyObject.GetOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(16, 'GetOptions', ((1, 'dwOptions'),)))
    IGroupPolicyObject.SetOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(17, 'SetOptions', ((1, 'dwOptions'),(1, 'dwMask'),)))
    IGroupPolicyObject.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECT_TYPE))(18, 'GetType', ((1, 'gpoType'),)))
    IGroupPolicyObject.GetMachineName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32)(19, 'GetMachineName', ((1, 'pszName'),(1, 'cchMaxLength'),)))
    IGroupPolicyObject.GetPropertySheetPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Controls.HPROPSHEETPAGE)),POINTER(UInt32))(20, 'GetPropertySheetPages', ((1, 'hPages'),(1, 'uPageCount'),)))
    win32more.System.Com.IUnknown
    return IGroupPolicyObject
def _define_INSTALLDATA_head():
    class INSTALLDATA(Structure):
        pass
    return INSTALLDATA
def _define_INSTALLDATA():
    INSTALLDATA = win32more.System.GroupPolicy.INSTALLDATA_head
    INSTALLDATA._fields_ = [
        ('Type', win32more.System.GroupPolicy.INSTALLSPECTYPE),
        ('Spec', win32more.System.GroupPolicy.INSTALLSPEC),
    ]
    return INSTALLDATA
def _define_INSTALLSPEC_head():
    class INSTALLSPEC(Union):
        pass
    return INSTALLSPEC
def _define_INSTALLSPEC():
    INSTALLSPEC = win32more.System.GroupPolicy.INSTALLSPEC_head
    class INSTALLSPEC__AppName_e__Struct(Structure):
        pass
    INSTALLSPEC__AppName_e__Struct._fields_ = [
        ('Name', win32more.Foundation.PWSTR),
        ('GPOId', Guid),
    ]
    class INSTALLSPEC__COMClass_e__Struct(Structure):
        pass
    INSTALLSPEC__COMClass_e__Struct._fields_ = [
        ('Clsid', Guid),
        ('ClsCtx', UInt32),
    ]
    INSTALLSPEC._fields_ = [
        ('AppName', INSTALLSPEC__AppName_e__Struct),
        ('FileExt', win32more.Foundation.PWSTR),
        ('ProgId', win32more.Foundation.PWSTR),
        ('COMClass', INSTALLSPEC__COMClass_e__Struct),
    ]
    return INSTALLSPEC
INSTALLSPECTYPE = Int32
APPNAME = 1
FILEEXT = 2
PROGID = 3
COMCLASS = 4
def _define_IRSOPInformation_head():
    class IRSOPInformation(win32more.System.Com.IUnknown_head):
        Guid = Guid('9a5a81b5-d9c7-49ef-9d-11-dd-f5-09-68-c4-8d')
    return IRSOPInformation
def _define_IRSOPInformation():
    IRSOPInformation = win32more.System.GroupPolicy.IRSOPInformation_head
    IRSOPInformation.GetNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,Int32)(3, 'GetNamespace', ((1, 'dwSection'),(1, 'pszName'),(1, 'cchMaxLength'),)))
    IRSOPInformation.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetFlags', ((1, 'pdwFlags'),)))
    IRSOPInformation.GetEventLogEntryText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR))(5, 'GetEventLogEntryText', ((1, 'pszEventSource'),(1, 'pszEventLogName'),(1, 'pszEventTime'),(1, 'dwEventID'),(1, 'ppszText'),)))
    win32more.System.Com.IUnknown
    return IRSOPInformation
def _define_LOCALMANAGEDAPPLICATION_head():
    class LOCALMANAGEDAPPLICATION(Structure):
        pass
    return LOCALMANAGEDAPPLICATION
def _define_LOCALMANAGEDAPPLICATION():
    LOCALMANAGEDAPPLICATION = win32more.System.GroupPolicy.LOCALMANAGEDAPPLICATION_head
    LOCALMANAGEDAPPLICATION._fields_ = [
        ('pszDeploymentName', win32more.Foundation.PWSTR),
        ('pszPolicyName', win32more.Foundation.PWSTR),
        ('pszProductId', win32more.Foundation.PWSTR),
        ('dwState', UInt32),
    ]
    return LOCALMANAGEDAPPLICATION
def _define_MANAGEDAPPLICATION_head():
    class MANAGEDAPPLICATION(Structure):
        pass
    return MANAGEDAPPLICATION
def _define_MANAGEDAPPLICATION():
    MANAGEDAPPLICATION = win32more.System.GroupPolicy.MANAGEDAPPLICATION_head
    MANAGEDAPPLICATION._fields_ = [
        ('pszPackageName', win32more.Foundation.PWSTR),
        ('pszPublisher', win32more.Foundation.PWSTR),
        ('dwVersionHi', UInt32),
        ('dwVersionLo', UInt32),
        ('dwRevision', UInt32),
        ('GpoId', Guid),
        ('pszPolicyName', win32more.Foundation.PWSTR),
        ('ProductId', Guid),
        ('Language', UInt16),
        ('pszOwner', win32more.Foundation.PWSTR),
        ('pszCompany', win32more.Foundation.PWSTR),
        ('pszComments', win32more.Foundation.PWSTR),
        ('pszContact', win32more.Foundation.PWSTR),
        ('pszSupportUrl', win32more.Foundation.PWSTR),
        ('dwPathType', UInt32),
        ('bInstalled', win32more.Foundation.BOOL),
    ]
    return MANAGEDAPPLICATION
def _define_PFNGENERATEGROUPPOLICY():
    return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Foundation.BOOL),win32more.Foundation.PWSTR,POINTER(win32more.System.GroupPolicy.RSOP_TARGET_head),POINTER(win32more.System.GroupPolicy.RSOP_TARGET_head))
def _define_PFNPROCESSGROUPPOLICY():
    return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.HANDLE,win32more.System.Registry.HKEY,POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTA_head),POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTA_head),UIntPtr,POINTER(win32more.Foundation.BOOL),win32more.System.GroupPolicy.PFNSTATUSMESSAGECALLBACK)
def _define_PFNPROCESSGROUPPOLICYEX():
    return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.HANDLE,win32more.System.Registry.HKEY,POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTA_head),POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTA_head),UIntPtr,POINTER(win32more.Foundation.BOOL),win32more.System.GroupPolicy.PFNSTATUSMESSAGECALLBACK,win32more.System.Wmi.IWbemServices_head,POINTER(win32more.Foundation.HRESULT))
def _define_PFNSTATUSMESSAGECALLBACK():
    return WINFUNCTYPE(UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR)
def _define_POLICYSETTINGSTATUSINFO_head():
    class POLICYSETTINGSTATUSINFO(Structure):
        pass
    return POLICYSETTINGSTATUSINFO
def _define_POLICYSETTINGSTATUSINFO():
    POLICYSETTINGSTATUSINFO = win32more.System.GroupPolicy.POLICYSETTINGSTATUSINFO_head
    POLICYSETTINGSTATUSINFO._fields_ = [
        ('szKey', win32more.Foundation.PWSTR),
        ('szEventSource', win32more.Foundation.PWSTR),
        ('szEventLogName', win32more.Foundation.PWSTR),
        ('dwEventID', UInt32),
        ('dwErrorCode', UInt32),
        ('status', win32more.System.GroupPolicy.SETTINGSTATUS),
        ('timeLogged', win32more.Foundation.SYSTEMTIME),
    ]
    return POLICYSETTINGSTATUSINFO
def _define_RSOP_TARGET_head():
    class RSOP_TARGET(Structure):
        pass
    return RSOP_TARGET
def _define_RSOP_TARGET():
    RSOP_TARGET = win32more.System.GroupPolicy.RSOP_TARGET_head
    RSOP_TARGET._fields_ = [
        ('pwszAccountName', win32more.Foundation.PWSTR),
        ('pwszNewSOM', win32more.Foundation.PWSTR),
        ('psaSecurityGroups', POINTER(win32more.System.Com.SAFEARRAY_head)),
        ('pRsopToken', c_void_p),
        ('pGPOList', POINTER(win32more.System.GroupPolicy.GROUP_POLICY_OBJECTA_head)),
        ('pWbemServices', win32more.System.Wmi.IWbemServices_head),
    ]
    return RSOP_TARGET
SETTINGSTATUS = Int32
SETTINGSTATUS_RSOPUnspecified = 0
SETTINGSTATUS_RSOPApplied = 1
SETTINGSTATUS_RSOPIgnored = 2
SETTINGSTATUS_RSOPFailed = 3
SETTINGSTATUS_RSOPSubsettingFailed = 4
__all__ = [
    "ABSENT",
    "APPNAME",
    "APPSTATE",
    "ASSIGNED",
    "BrowseForGPO",
    "CLSID_GPESnapIn",
    "CLSID_GroupPolicyObject",
    "CLSID_RSOPSnapIn",
    "COMCLASS",
    "CommandLineFromMsiDescriptor",
    "CreateGPOLink",
    "CriticalPolicySectionHandle",
    "DeleteAllGPOLinks",
    "DeleteGPOLink",
    "EnterCriticalPolicySection",
    "ExportRSoPData",
    "FILEEXT",
    "FLAG_ASSUME_COMP_WQLFILTER_TRUE",
    "FLAG_ASSUME_SLOW_LINK",
    "FLAG_ASSUME_USER_WQLFILTER_TRUE",
    "FLAG_FORCE_CREATENAMESPACE",
    "FLAG_LOOPBACK_MERGE",
    "FLAG_LOOPBACK_REPLACE",
    "FLAG_NO_COMPUTER",
    "FLAG_NO_CSE_INVOKE",
    "FLAG_NO_GPO_FILTER",
    "FLAG_NO_USER",
    "FLAG_PLANNING_MODE",
    "FreeGPOListA",
    "FreeGPOListW",
    "GPC_BLOCK_POLICY",
    "GPM",
    "GPMAsyncCancel",
    "GPMBackup",
    "GPMBackupCollection",
    "GPMBackupDir",
    "GPMBackupDirEx",
    "GPMBackupType",
    "GPMBackupType_typeGPO",
    "GPMBackupType_typeStarterGPO",
    "GPMCSECollection",
    "GPMClientSideExtension",
    "GPMConstants",
    "GPMDestinationOption",
    "GPMDestinationOption_opDestinationByRelativeName",
    "GPMDestinationOption_opDestinationNone",
    "GPMDestinationOption_opDestinationSameAsSource",
    "GPMDestinationOption_opDestinationSet",
    "GPMDomain",
    "GPMEntryType",
    "GPMEntryType_typeComputer",
    "GPMEntryType_typeGlobalGroup",
    "GPMEntryType_typeLocalGroup",
    "GPMEntryType_typeUNCPath",
    "GPMEntryType_typeUniversalGroup",
    "GPMEntryType_typeUnknown",
    "GPMEntryType_typeUser",
    "GPMGPO",
    "GPMGPOCollection",
    "GPMGPOLink",
    "GPMGPOLinksCollection",
    "GPMMapEntry",
    "GPMMapEntryCollection",
    "GPMMigrationTable",
    "GPMPermission",
    "GPMPermissionType",
    "GPMPermissionType_permGPOApply",
    "GPMPermissionType_permGPOCustom",
    "GPMPermissionType_permGPOEdit",
    "GPMPermissionType_permGPOEditSecurityAndDelete",
    "GPMPermissionType_permGPORead",
    "GPMPermissionType_permSOMGPOCreate",
    "GPMPermissionType_permSOMLink",
    "GPMPermissionType_permSOMLogging",
    "GPMPermissionType_permSOMPlanning",
    "GPMPermissionType_permSOMStarterGPOCreate",
    "GPMPermissionType_permSOMWMICreate",
    "GPMPermissionType_permSOMWMIFullControl",
    "GPMPermissionType_permStarterGPOCustom",
    "GPMPermissionType_permStarterGPOEdit",
    "GPMPermissionType_permStarterGPOFullControl",
    "GPMPermissionType_permStarterGPORead",
    "GPMPermissionType_permWMIFilterCustom",
    "GPMPermissionType_permWMIFilterEdit",
    "GPMPermissionType_permWMIFilterFullControl",
    "GPMRSOP",
    "GPMRSOPMode",
    "GPMRSOPMode_rsopLogging",
    "GPMRSOPMode_rsopPlanning",
    "GPMRSOPMode_rsopUnknown",
    "GPMReportType",
    "GPMReportType_repClientHealthRefreshXML",
    "GPMReportType_repClientHealthXML",
    "GPMReportType_repHTML",
    "GPMReportType_repInfraRefreshXML",
    "GPMReportType_repInfraXML",
    "GPMReportType_repXML",
    "GPMReportingOptions",
    "GPMReportingOptions_opReportComments",
    "GPMReportingOptions_opReportLegacy",
    "GPMResult",
    "GPMSOM",
    "GPMSOMCollection",
    "GPMSOMType",
    "GPMSOMType_somDomain",
    "GPMSOMType_somOU",
    "GPMSOMType_somSite",
    "GPMSearchCriteria",
    "GPMSearchOperation",
    "GPMSearchOperation_opContains",
    "GPMSearchOperation_opEquals",
    "GPMSearchOperation_opNotContains",
    "GPMSearchOperation_opNotEquals",
    "GPMSearchProperty",
    "GPMSearchProperty_backupMostRecent",
    "GPMSearchProperty_gpoComputerExtensions",
    "GPMSearchProperty_gpoDisplayName",
    "GPMSearchProperty_gpoDomain",
    "GPMSearchProperty_gpoEffectivePermissions",
    "GPMSearchProperty_gpoID",
    "GPMSearchProperty_gpoPermissions",
    "GPMSearchProperty_gpoUserExtensions",
    "GPMSearchProperty_gpoWMIFilter",
    "GPMSearchProperty_somLinks",
    "GPMSearchProperty_starterGPODisplayName",
    "GPMSearchProperty_starterGPODomain",
    "GPMSearchProperty_starterGPOEffectivePermissions",
    "GPMSearchProperty_starterGPOID",
    "GPMSearchProperty_starterGPOPermissions",
    "GPMSecurityInfo",
    "GPMSitesContainer",
    "GPMStarterGPOBackup",
    "GPMStarterGPOBackupCollection",
    "GPMStarterGPOCollection",
    "GPMStarterGPOType",
    "GPMStarterGPOType_typeCustom",
    "GPMStarterGPOType_typeSystem",
    "GPMStatusMessage",
    "GPMStatusMsgCollection",
    "GPMTemplate",
    "GPMTrustee",
    "GPMWMIFilter",
    "GPMWMIFilterCollection",
    "GPM_DONOTUSE_W2KDC",
    "GPM_DONOT_VALIDATEDC",
    "GPM_MIGRATIONTABLE_ONLY",
    "GPM_PROCESS_SECURITY",
    "GPM_USE_ANYDC",
    "GPM_USE_PDC",
    "GPOBROWSEINFO",
    "GPO_BROWSE_DISABLENEW",
    "GPO_BROWSE_INITTOALL",
    "GPO_BROWSE_NOCOMPUTERS",
    "GPO_BROWSE_NODSGPOS",
    "GPO_BROWSE_NOUSERGPOS",
    "GPO_BROWSE_OPENBUTTON",
    "GPO_BROWSE_SENDAPPLYONEDIT",
    "GPO_FLAG_DISABLE",
    "GPO_FLAG_FORCE",
    "GPO_INFO_FLAG_ASYNC_FOREGROUND",
    "GPO_INFO_FLAG_BACKGROUND",
    "GPO_INFO_FLAG_FORCED_REFRESH",
    "GPO_INFO_FLAG_LINKTRANSITION",
    "GPO_INFO_FLAG_LOGRSOP_TRANSITION",
    "GPO_INFO_FLAG_MACHINE",
    "GPO_INFO_FLAG_NOCHANGES",
    "GPO_INFO_FLAG_SAFEMODE_BOOT",
    "GPO_INFO_FLAG_SLOWLINK",
    "GPO_INFO_FLAG_VERBOSE",
    "GPO_LINK",
    "GPO_LINK_GPLinkDomain",
    "GPO_LINK_GPLinkMachine",
    "GPO_LINK_GPLinkOrganizationalUnit",
    "GPO_LINK_GPLinkSite",
    "GPO_LINK_GPLinkUnknown",
    "GPO_LIST_FLAG_MACHINE",
    "GPO_LIST_FLAG_NO_SECURITYFILTERS",
    "GPO_LIST_FLAG_NO_WMIFILTERS",
    "GPO_LIST_FLAG_SITEONLY",
    "GPO_OPEN_LOAD_REGISTRY",
    "GPO_OPEN_READ_ONLY",
    "GPO_OPTION_DISABLE_MACHINE",
    "GPO_OPTION_DISABLE_USER",
    "GPO_SECTION_MACHINE",
    "GPO_SECTION_ROOT",
    "GPO_SECTION_USER",
    "GP_DLLNAME",
    "GP_ENABLEASYNCHRONOUSPROCESSING",
    "GP_MAXNOGPOLISTCHANGESINTERVAL",
    "GP_NOBACKGROUNDPOLICY",
    "GP_NOGPOLISTCHANGES",
    "GP_NOMACHINEPOLICY",
    "GP_NOSLOWLINK",
    "GP_NOTIFYLINKTRANSITION",
    "GP_NOUSERPOLICY",
    "GP_PERUSERLOCALSETTINGS",
    "GP_PROCESSGROUPPOLICY",
    "GP_REQUIRESSUCCESSFULREGISTRY",
    "GROUP_POLICY_HINT_TYPE",
    "GROUP_POLICY_HINT_TYPE_GPHintDomain",
    "GROUP_POLICY_HINT_TYPE_GPHintMachine",
    "GROUP_POLICY_HINT_TYPE_GPHintOrganizationalUnit",
    "GROUP_POLICY_HINT_TYPE_GPHintSite",
    "GROUP_POLICY_HINT_TYPE_GPHintUnknown",
    "GROUP_POLICY_OBJECTA",
    "GROUP_POLICY_OBJECTW",
    "GROUP_POLICY_OBJECT_TYPE",
    "GROUP_POLICY_OBJECT_TYPE_GPOTypeDS",
    "GROUP_POLICY_OBJECT_TYPE_GPOTypeLocal",
    "GROUP_POLICY_OBJECT_TYPE_GPOTypeLocalGroup",
    "GROUP_POLICY_OBJECT_TYPE_GPOTypeLocalUser",
    "GROUP_POLICY_OBJECT_TYPE_GPOTypeRemote",
    "GenerateGPNotification",
    "GetAppliedGPOListA",
    "GetAppliedGPOListW",
    "GetGPOListA",
    "GetGPOListW",
    "GetLocalManagedApplicationData",
    "GetLocalManagedApplications",
    "GetManagedApplicationCategories",
    "GetManagedApplications",
    "IGPEInformation",
    "IGPM",
    "IGPM2",
    "IGPMAsyncCancel",
    "IGPMAsyncProgress",
    "IGPMBackup",
    "IGPMBackupCollection",
    "IGPMBackupDir",
    "IGPMBackupDirEx",
    "IGPMCSECollection",
    "IGPMClientSideExtension",
    "IGPMConstants",
    "IGPMConstants2",
    "IGPMDomain",
    "IGPMDomain2",
    "IGPMDomain3",
    "IGPMGPO",
    "IGPMGPO2",
    "IGPMGPO3",
    "IGPMGPOCollection",
    "IGPMGPOLink",
    "IGPMGPOLinksCollection",
    "IGPMMapEntry",
    "IGPMMapEntryCollection",
    "IGPMMigrationTable",
    "IGPMPermission",
    "IGPMRSOP",
    "IGPMResult",
    "IGPMSOM",
    "IGPMSOMCollection",
    "IGPMSearchCriteria",
    "IGPMSecurityInfo",
    "IGPMSitesContainer",
    "IGPMStarterGPO",
    "IGPMStarterGPOBackup",
    "IGPMStarterGPOBackupCollection",
    "IGPMStarterGPOCollection",
    "IGPMStatusMessage",
    "IGPMStatusMsgCollection",
    "IGPMTrustee",
    "IGPMWMIFilter",
    "IGPMWMIFilterCollection",
    "IGroupPolicyObject",
    "INSTALLDATA",
    "INSTALLSPEC",
    "INSTALLSPECTYPE",
    "IRSOPInformation",
    "ImportRSoPData",
    "InstallApplication",
    "LOCALMANAGEDAPPLICATION",
    "LOCALSTATE_ASSIGNED",
    "LOCALSTATE_ORPHANED",
    "LOCALSTATE_POLICYREMOVE_ORPHAN",
    "LOCALSTATE_POLICYREMOVE_UNINSTALL",
    "LOCALSTATE_PUBLISHED",
    "LOCALSTATE_UNINSTALLED",
    "LOCALSTATE_UNINSTALL_UNMANAGED",
    "LeaveCriticalPolicySection",
    "MANAGEDAPPLICATION",
    "MANAGED_APPS_FROMCATEGORY",
    "MANAGED_APPS_INFOLEVEL_DEFAULT",
    "MANAGED_APPS_USERAPPLICATIONS",
    "MANAGED_APPTYPE_SETUPEXE",
    "MANAGED_APPTYPE_UNSUPPORTED",
    "MANAGED_APPTYPE_WINDOWSINSTALLER",
    "NODEID_Machine",
    "NODEID_MachineSWSettings",
    "NODEID_RSOPMachine",
    "NODEID_RSOPMachineSWSettings",
    "NODEID_RSOPUser",
    "NODEID_RSOPUserSWSettings",
    "NODEID_User",
    "NODEID_UserSWSettings",
    "PFNGENERATEGROUPPOLICY",
    "PFNPROCESSGROUPPOLICY",
    "PFNPROCESSGROUPPOLICYEX",
    "PFNSTATUSMESSAGECALLBACK",
    "PI_APPLYPOLICY",
    "PI_NOUI",
    "POLICYSETTINGSTATUSINFO",
    "PROGID",
    "PT_MANDATORY",
    "PT_ROAMING",
    "PT_ROAMING_PREEXISTING",
    "PT_TEMPORARY",
    "PUBLISHED",
    "ProcessGroupPolicyCompleted",
    "ProcessGroupPolicyCompletedEx",
    "RP_FORCE",
    "RP_SYNC",
    "RSOP_COMPUTER_ACCESS_DENIED",
    "RSOP_INFO_FLAG_DIAGNOSTIC_MODE",
    "RSOP_NO_COMPUTER",
    "RSOP_NO_USER",
    "RSOP_PLANNING_ASSUME_COMP_WQLFILTER_TRUE",
    "RSOP_PLANNING_ASSUME_LOOPBACK_MERGE",
    "RSOP_PLANNING_ASSUME_LOOPBACK_REPLACE",
    "RSOP_PLANNING_ASSUME_SLOW_LINK",
    "RSOP_PLANNING_ASSUME_USER_WQLFILTER_TRUE",
    "RSOP_TARGET",
    "RSOP_TEMPNAMESPACE_EXISTS",
    "RSOP_USER_ACCESS_DENIED",
    "RefreshPolicy",
    "RefreshPolicyEx",
    "RegisterGPNotification",
    "RsopAccessCheckByType",
    "RsopFileAccessCheck",
    "RsopResetPolicySettingStatus",
    "RsopSetPolicySettingStatus",
    "SETTINGSTATUS",
    "SETTINGSTATUS_RSOPApplied",
    "SETTINGSTATUS_RSOPFailed",
    "SETTINGSTATUS_RSOPIgnored",
    "SETTINGSTATUS_RSOPSubsettingFailed",
    "SETTINGSTATUS_RSOPUnspecified",
    "UninstallApplication",
    "UnregisterGPNotification",
]
