from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Data.Xml.MsXml
import win32more.Foundation
import win32more.NetworkManagement.NetManagement
import win32more.Security
import win32more.Security.Cryptography
import win32more.System.Com
import win32more.System.Registry
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
def _define_ACCESS_INFO_0_head():
    class ACCESS_INFO_0(Structure):
        pass
    return ACCESS_INFO_0
def _define_ACCESS_INFO_0():
    ACCESS_INFO_0 = win32more.NetworkManagement.NetManagement.ACCESS_INFO_0_head
    ACCESS_INFO_0._fields_ = [
        ('acc0_resource_name', win32more.Foundation.PWSTR),
    ]
    return ACCESS_INFO_0
def _define_ACCESS_INFO_1_head():
    class ACCESS_INFO_1(Structure):
        pass
    return ACCESS_INFO_1
def _define_ACCESS_INFO_1():
    ACCESS_INFO_1 = win32more.NetworkManagement.NetManagement.ACCESS_INFO_1_head
    ACCESS_INFO_1._fields_ = [
        ('acc1_resource_name', win32more.Foundation.PWSTR),
        ('acc1_attr', UInt32),
        ('acc1_count', UInt32),
    ]
    return ACCESS_INFO_1
def _define_ACCESS_INFO_1002_head():
    class ACCESS_INFO_1002(Structure):
        pass
    return ACCESS_INFO_1002
def _define_ACCESS_INFO_1002():
    ACCESS_INFO_1002 = win32more.NetworkManagement.NetManagement.ACCESS_INFO_1002_head
    ACCESS_INFO_1002._fields_ = [
        ('acc1002_attr', UInt32),
    ]
    return ACCESS_INFO_1002
def _define_ACCESS_LIST_head():
    class ACCESS_LIST(Structure):
        pass
    return ACCESS_LIST
def _define_ACCESS_LIST():
    ACCESS_LIST = win32more.NetworkManagement.NetManagement.ACCESS_LIST_head
    ACCESS_LIST._fields_ = [
        ('acl_ugname', win32more.Foundation.PWSTR),
        ('acl_access', UInt32),
    ]
    return ACCESS_LIST
def _define_ADMIN_OTHER_INFO_head():
    class ADMIN_OTHER_INFO(Structure):
        pass
    return ADMIN_OTHER_INFO
def _define_ADMIN_OTHER_INFO():
    ADMIN_OTHER_INFO = win32more.NetworkManagement.NetManagement.ADMIN_OTHER_INFO_head
    ADMIN_OTHER_INFO._fields_ = [
        ('alrtad_errcode', UInt32),
        ('alrtad_numstrings', UInt32),
    ]
    return ADMIN_OTHER_INFO
def _define_AE_ACCLIM_head():
    class AE_ACCLIM(Structure):
        pass
    return AE_ACCLIM
def _define_AE_ACCLIM():
    AE_ACCLIM = win32more.NetworkManagement.NetManagement.AE_ACCLIM_head
    AE_ACCLIM._fields_ = [
        ('ae_al_compname', UInt32),
        ('ae_al_username', UInt32),
        ('ae_al_resname', UInt32),
        ('ae_al_limit', UInt32),
    ]
    return AE_ACCLIM
def _define_AE_ACLMOD_head():
    class AE_ACLMOD(Structure):
        pass
    return AE_ACLMOD
def _define_AE_ACLMOD():
    AE_ACLMOD = win32more.NetworkManagement.NetManagement.AE_ACLMOD_head
    AE_ACLMOD._fields_ = [
        ('ae_am_compname', UInt32),
        ('ae_am_username', UInt32),
        ('ae_am_resname', UInt32),
        ('ae_am_action', UInt32),
        ('ae_am_datalen', UInt32),
    ]
    return AE_ACLMOD
def _define_AE_CLOSEFILE_head():
    class AE_CLOSEFILE(Structure):
        pass
    return AE_CLOSEFILE
def _define_AE_CLOSEFILE():
    AE_CLOSEFILE = win32more.NetworkManagement.NetManagement.AE_CLOSEFILE_head
    AE_CLOSEFILE._fields_ = [
        ('ae_cf_compname', UInt32),
        ('ae_cf_username', UInt32),
        ('ae_cf_resname', UInt32),
        ('ae_cf_fileid', UInt32),
        ('ae_cf_duration', UInt32),
        ('ae_cf_reason', UInt32),
    ]
    return AE_CLOSEFILE
def _define_AE_CONNREJ_head():
    class AE_CONNREJ(Structure):
        pass
    return AE_CONNREJ
def _define_AE_CONNREJ():
    AE_CONNREJ = win32more.NetworkManagement.NetManagement.AE_CONNREJ_head
    AE_CONNREJ._fields_ = [
        ('ae_cr_compname', UInt32),
        ('ae_cr_username', UInt32),
        ('ae_cr_netname', UInt32),
        ('ae_cr_reason', UInt32),
    ]
    return AE_CONNREJ
def _define_AE_CONNSTART_head():
    class AE_CONNSTART(Structure):
        pass
    return AE_CONNSTART
def _define_AE_CONNSTART():
    AE_CONNSTART = win32more.NetworkManagement.NetManagement.AE_CONNSTART_head
    AE_CONNSTART._fields_ = [
        ('ae_ct_compname', UInt32),
        ('ae_ct_username', UInt32),
        ('ae_ct_netname', UInt32),
        ('ae_ct_connid', UInt32),
    ]
    return AE_CONNSTART
def _define_AE_CONNSTOP_head():
    class AE_CONNSTOP(Structure):
        pass
    return AE_CONNSTOP
def _define_AE_CONNSTOP():
    AE_CONNSTOP = win32more.NetworkManagement.NetManagement.AE_CONNSTOP_head
    AE_CONNSTOP._fields_ = [
        ('ae_cp_compname', UInt32),
        ('ae_cp_username', UInt32),
        ('ae_cp_netname', UInt32),
        ('ae_cp_connid', UInt32),
        ('ae_cp_reason', UInt32),
    ]
    return AE_CONNSTOP
def _define_AE_GENERIC_head():
    class AE_GENERIC(Structure):
        pass
    return AE_GENERIC
def _define_AE_GENERIC():
    AE_GENERIC = win32more.NetworkManagement.NetManagement.AE_GENERIC_head
    AE_GENERIC._fields_ = [
        ('ae_ge_msgfile', UInt32),
        ('ae_ge_msgnum', UInt32),
        ('ae_ge_params', UInt32),
        ('ae_ge_param1', UInt32),
        ('ae_ge_param2', UInt32),
        ('ae_ge_param3', UInt32),
        ('ae_ge_param4', UInt32),
        ('ae_ge_param5', UInt32),
        ('ae_ge_param6', UInt32),
        ('ae_ge_param7', UInt32),
        ('ae_ge_param8', UInt32),
        ('ae_ge_param9', UInt32),
    ]
    return AE_GENERIC
def _define_AE_LOCKOUT_head():
    class AE_LOCKOUT(Structure):
        pass
    return AE_LOCKOUT
def _define_AE_LOCKOUT():
    AE_LOCKOUT = win32more.NetworkManagement.NetManagement.AE_LOCKOUT_head
    AE_LOCKOUT._fields_ = [
        ('ae_lk_compname', UInt32),
        ('ae_lk_username', UInt32),
        ('ae_lk_action', UInt32),
        ('ae_lk_bad_pw_count', UInt32),
    ]
    return AE_LOCKOUT
def _define_AE_NETLOGOFF_head():
    class AE_NETLOGOFF(Structure):
        pass
    return AE_NETLOGOFF
def _define_AE_NETLOGOFF():
    AE_NETLOGOFF = win32more.NetworkManagement.NetManagement.AE_NETLOGOFF_head
    AE_NETLOGOFF._fields_ = [
        ('ae_nf_compname', UInt32),
        ('ae_nf_username', UInt32),
        ('ae_nf_reserved1', UInt32),
        ('ae_nf_reserved2', UInt32),
    ]
    return AE_NETLOGOFF
def _define_AE_NETLOGON_head():
    class AE_NETLOGON(Structure):
        pass
    return AE_NETLOGON
def _define_AE_NETLOGON():
    AE_NETLOGON = win32more.NetworkManagement.NetManagement.AE_NETLOGON_head
    AE_NETLOGON._fields_ = [
        ('ae_no_compname', UInt32),
        ('ae_no_username', UInt32),
        ('ae_no_privilege', UInt32),
        ('ae_no_authflags', UInt32),
    ]
    return AE_NETLOGON
def _define_AE_RESACCESS_head():
    class AE_RESACCESS(Structure):
        pass
    return AE_RESACCESS
def _define_AE_RESACCESS():
    AE_RESACCESS = win32more.NetworkManagement.NetManagement.AE_RESACCESS_head
    AE_RESACCESS._fields_ = [
        ('ae_ra_compname', UInt32),
        ('ae_ra_username', UInt32),
        ('ae_ra_resname', UInt32),
        ('ae_ra_operation', UInt32),
        ('ae_ra_returncode', UInt32),
        ('ae_ra_restype', UInt32),
        ('ae_ra_fileid', UInt32),
    ]
    return AE_RESACCESS
def _define_AE_RESACCESSREJ_head():
    class AE_RESACCESSREJ(Structure):
        pass
    return AE_RESACCESSREJ
def _define_AE_RESACCESSREJ():
    AE_RESACCESSREJ = win32more.NetworkManagement.NetManagement.AE_RESACCESSREJ_head
    AE_RESACCESSREJ._fields_ = [
        ('ae_rr_compname', UInt32),
        ('ae_rr_username', UInt32),
        ('ae_rr_resname', UInt32),
        ('ae_rr_operation', UInt32),
    ]
    return AE_RESACCESSREJ
def _define_AE_SERVICESTAT_head():
    class AE_SERVICESTAT(Structure):
        pass
    return AE_SERVICESTAT
def _define_AE_SERVICESTAT():
    AE_SERVICESTAT = win32more.NetworkManagement.NetManagement.AE_SERVICESTAT_head
    AE_SERVICESTAT._fields_ = [
        ('ae_ss_compname', UInt32),
        ('ae_ss_username', UInt32),
        ('ae_ss_svcname', UInt32),
        ('ae_ss_status', UInt32),
        ('ae_ss_code', UInt32),
        ('ae_ss_text', UInt32),
        ('ae_ss_returnval', UInt32),
    ]
    return AE_SERVICESTAT
def _define_AE_SESSLOGOFF_head():
    class AE_SESSLOGOFF(Structure):
        pass
    return AE_SESSLOGOFF
def _define_AE_SESSLOGOFF():
    AE_SESSLOGOFF = win32more.NetworkManagement.NetManagement.AE_SESSLOGOFF_head
    AE_SESSLOGOFF._fields_ = [
        ('ae_sf_compname', UInt32),
        ('ae_sf_username', UInt32),
        ('ae_sf_reason', UInt32),
    ]
    return AE_SESSLOGOFF
def _define_AE_SESSLOGON_head():
    class AE_SESSLOGON(Structure):
        pass
    return AE_SESSLOGON
def _define_AE_SESSLOGON():
    AE_SESSLOGON = win32more.NetworkManagement.NetManagement.AE_SESSLOGON_head
    AE_SESSLOGON._fields_ = [
        ('ae_so_compname', UInt32),
        ('ae_so_username', UInt32),
        ('ae_so_privilege', UInt32),
    ]
    return AE_SESSLOGON
def _define_AE_SESSPWERR_head():
    class AE_SESSPWERR(Structure):
        pass
    return AE_SESSPWERR
def _define_AE_SESSPWERR():
    AE_SESSPWERR = win32more.NetworkManagement.NetManagement.AE_SESSPWERR_head
    AE_SESSPWERR._fields_ = [
        ('ae_sp_compname', UInt32),
        ('ae_sp_username', UInt32),
    ]
    return AE_SESSPWERR
def _define_AE_SRVSTATUS_head():
    class AE_SRVSTATUS(Structure):
        pass
    return AE_SRVSTATUS
def _define_AE_SRVSTATUS():
    AE_SRVSTATUS = win32more.NetworkManagement.NetManagement.AE_SRVSTATUS_head
    AE_SRVSTATUS._fields_ = [
        ('ae_sv_status', UInt32),
    ]
    return AE_SRVSTATUS
def _define_AE_UASMOD_head():
    class AE_UASMOD(Structure):
        pass
    return AE_UASMOD
def _define_AE_UASMOD():
    AE_UASMOD = win32more.NetworkManagement.NetManagement.AE_UASMOD_head
    AE_UASMOD._fields_ = [
        ('ae_um_compname', UInt32),
        ('ae_um_username', UInt32),
        ('ae_um_resname', UInt32),
        ('ae_um_rectype', UInt32),
        ('ae_um_action', UInt32),
        ('ae_um_datalen', UInt32),
    ]
    return AE_UASMOD
AF_OP = UInt32
AF_OP_PRINT = 1
AF_OP_COMM = 2
AF_OP_SERVER = 4
AF_OP_ACCOUNTS = 8
NERR_BASE = 2100
NERR_PasswordExpired = 2242
CNLEN = 15
LM20_CNLEN = 15
DNLEN = 15
LM20_DNLEN = 15
UNCLEN = 17
LM20_UNCLEN = 17
LM20_NNLEN = 12
SNLEN = 80
LM20_SNLEN = 15
STXTLEN = 256
LM20_STXTLEN = 63
PATHLEN = 256
LM20_PATHLEN = 256
DEVLEN = 80
LM20_DEVLEN = 8
EVLEN = 16
UNLEN = 256
LM20_UNLEN = 20
GNLEN = 256
LM20_GNLEN = 20
PWLEN = 256
LM20_PWLEN = 14
SHPWLEN = 8
CLTYPE_LEN = 12
MAXCOMMENTSZ = 256
LM20_MAXCOMMENTSZ = 48
QNLEN = 80
LM20_QNLEN = 12
ALERTSZ = 128
NETBIOS_NAME_LEN = 16
MAX_PREFERRED_LENGTH = 4294967295
CRYPT_KEY_LEN = 7
CRYPT_TXT_LEN = 8
ENCRYPTED_PWLEN = 16
SESSION_PWLEN = 24
SESSION_CRYPT_KLEN = 21
PARMNUM_ALL = 0
PARM_ERROR_UNKNOWN = 4294967295
PARM_ERROR_NONE = 0
PARMNUM_BASE_INFOLEVEL = 1000
MESSAGE_FILENAME = 'NETMSG'
OS2MSG_FILENAME = 'BASE'
HELP_MSG_FILENAME = 'NETH'
BACKUP_MSG_FILENAME = 'BAK.MSG'
PLATFORM_ID_DOS = 300
PLATFORM_ID_OS2 = 400
PLATFORM_ID_NT = 500
PLATFORM_ID_OSF = 600
PLATFORM_ID_VMS = 700
MIN_LANMAN_MESSAGE_ID = 2100
MAX_LANMAN_MESSAGE_ID = 5899
NERR_Success = 0
NERR_NetNotStarted = 2102
NERR_UnknownServer = 2103
NERR_ShareMem = 2104
NERR_NoNetworkResource = 2105
NERR_RemoteOnly = 2106
NERR_DevNotRedirected = 2107
NERR_ServerNotStarted = 2114
NERR_ItemNotFound = 2115
NERR_UnknownDevDir = 2116
NERR_RedirectedPath = 2117
NERR_DuplicateShare = 2118
NERR_NoRoom = 2119
NERR_TooManyItems = 2121
NERR_InvalidMaxUsers = 2122
NERR_BufTooSmall = 2123
NERR_RemoteErr = 2127
NERR_LanmanIniError = 2131
NERR_NetworkError = 2136
NERR_WkstaInconsistentState = 2137
NERR_WkstaNotStarted = 2138
NERR_BrowserNotStarted = 2139
NERR_InternalError = 2140
NERR_BadTransactConfig = 2141
NERR_InvalidAPI = 2142
NERR_BadEventName = 2143
NERR_DupNameReboot = 2144
NERR_CfgCompNotFound = 2146
NERR_CfgParamNotFound = 2147
NERR_LineTooLong = 2149
NERR_QNotFound = 2150
NERR_JobNotFound = 2151
NERR_DestNotFound = 2152
NERR_DestExists = 2153
NERR_QExists = 2154
NERR_QNoRoom = 2155
NERR_JobNoRoom = 2156
NERR_DestNoRoom = 2157
NERR_DestIdle = 2158
NERR_DestInvalidOp = 2159
NERR_ProcNoRespond = 2160
NERR_SpoolerNotLoaded = 2161
NERR_DestInvalidState = 2162
NERR_QInvalidState = 2163
NERR_JobInvalidState = 2164
NERR_SpoolNoMemory = 2165
NERR_DriverNotFound = 2166
NERR_DataTypeInvalid = 2167
NERR_ProcNotFound = 2168
NERR_ServiceTableLocked = 2180
NERR_ServiceTableFull = 2181
NERR_ServiceInstalled = 2182
NERR_ServiceEntryLocked = 2183
NERR_ServiceNotInstalled = 2184
NERR_BadServiceName = 2185
NERR_ServiceCtlTimeout = 2186
NERR_ServiceCtlBusy = 2187
NERR_BadServiceProgName = 2188
NERR_ServiceNotCtrl = 2189
NERR_ServiceKillProc = 2190
NERR_ServiceCtlNotValid = 2191
NERR_NotInDispatchTbl = 2192
NERR_BadControlRecv = 2193
NERR_ServiceNotStarting = 2194
NERR_AlreadyLoggedOn = 2200
NERR_NotLoggedOn = 2201
NERR_BadUsername = 2202
NERR_BadPassword = 2203
NERR_UnableToAddName_W = 2204
NERR_UnableToAddName_F = 2205
NERR_UnableToDelName_W = 2206
NERR_UnableToDelName_F = 2207
NERR_LogonsPaused = 2209
NERR_LogonServerConflict = 2210
NERR_LogonNoUserPath = 2211
NERR_LogonScriptError = 2212
NERR_StandaloneLogon = 2214
NERR_LogonServerNotFound = 2215
NERR_LogonDomainExists = 2216
NERR_NonValidatedLogon = 2217
NERR_ACFNotFound = 2219
NERR_GroupNotFound = 2220
NERR_UserNotFound = 2221
NERR_ResourceNotFound = 2222
NERR_GroupExists = 2223
NERR_UserExists = 2224
NERR_ResourceExists = 2225
NERR_NotPrimary = 2226
NERR_ACFNotLoaded = 2227
NERR_ACFNoRoom = 2228
NERR_ACFFileIOFail = 2229
NERR_ACFTooManyLists = 2230
NERR_UserLogon = 2231
NERR_ACFNoParent = 2232
NERR_CanNotGrowSegment = 2233
NERR_SpeGroupOp = 2234
NERR_NotInCache = 2235
NERR_UserInGroup = 2236
NERR_UserNotInGroup = 2237
NERR_AccountUndefined = 2238
NERR_AccountExpired = 2239
NERR_InvalidWorkstation = 2240
NERR_InvalidLogonHours = 2241
NERR_PasswordCantChange = 2243
NERR_PasswordHistConflict = 2244
NERR_PasswordTooShort = 2245
NERR_PasswordTooRecent = 2246
NERR_InvalidDatabase = 2247
NERR_DatabaseUpToDate = 2248
NERR_SyncRequired = 2249
NERR_UseNotFound = 2250
NERR_BadAsgType = 2251
NERR_DeviceIsShared = 2252
NERR_SameAsComputerName = 2253
NERR_NoComputerName = 2270
NERR_MsgAlreadyStarted = 2271
NERR_MsgInitFailed = 2272
NERR_NameNotFound = 2273
NERR_AlreadyForwarded = 2274
NERR_AddForwarded = 2275
NERR_AlreadyExists = 2276
NERR_TooManyNames = 2277
NERR_DelComputerName = 2278
NERR_LocalForward = 2279
NERR_GrpMsgProcessor = 2280
NERR_PausedRemote = 2281
NERR_BadReceive = 2282
NERR_NameInUse = 2283
NERR_MsgNotStarted = 2284
NERR_NotLocalName = 2285
NERR_NoForwardName = 2286
NERR_RemoteFull = 2287
NERR_NameNotForwarded = 2288
NERR_TruncatedBroadcast = 2289
NERR_InvalidDevice = 2294
NERR_WriteFault = 2295
NERR_DuplicateName = 2297
NERR_DeleteLater = 2298
NERR_IncompleteDel = 2299
NERR_MultipleNets = 2300
NERR_NetNameNotFound = 2310
NERR_DeviceNotShared = 2311
NERR_ClientNameNotFound = 2312
NERR_FileIdNotFound = 2314
NERR_ExecFailure = 2315
NERR_TmpFile = 2316
NERR_TooMuchData = 2317
NERR_DeviceShareConflict = 2318
NERR_BrowserTableIncomplete = 2319
NERR_NotLocalDomain = 2320
NERR_IsDfsShare = 2321
NERR_DevInvalidOpCode = 2331
NERR_DevNotFound = 2332
NERR_DevNotOpen = 2333
NERR_BadQueueDevString = 2334
NERR_BadQueuePriority = 2335
NERR_NoCommDevs = 2337
NERR_QueueNotFound = 2338
NERR_BadDevString = 2340
NERR_BadDev = 2341
NERR_InUseBySpooler = 2342
NERR_CommDevInUse = 2343
NERR_InvalidComputer = 2351
NERR_MaxLenExceeded = 2354
NERR_BadComponent = 2356
NERR_CantType = 2357
NERR_TooManyEntries = 2362
NERR_ProfileFileTooBig = 2370
NERR_ProfileOffset = 2371
NERR_ProfileCleanup = 2372
NERR_ProfileUnknownCmd = 2373
NERR_ProfileLoadErr = 2374
NERR_ProfileSaveErr = 2375
NERR_LogOverflow = 2377
NERR_LogFileChanged = 2378
NERR_LogFileCorrupt = 2379
NERR_SourceIsDir = 2380
NERR_BadSource = 2381
NERR_BadDest = 2382
NERR_DifferentServers = 2383
NERR_RunSrvPaused = 2385
NERR_ErrCommRunSrv = 2389
NERR_ErrorExecingGhost = 2391
NERR_ShareNotFound = 2392
NERR_InvalidLana = 2400
NERR_OpenFiles = 2401
NERR_ActiveConns = 2402
NERR_BadPasswordCore = 2403
NERR_DevInUse = 2404
NERR_LocalDrive = 2405
NERR_AlertExists = 2430
NERR_TooManyAlerts = 2431
NERR_NoSuchAlert = 2432
NERR_BadRecipient = 2433
NERR_AcctLimitExceeded = 2434
NERR_InvalidLogSeek = 2440
NERR_BadUasConfig = 2450
NERR_InvalidUASOp = 2451
NERR_LastAdmin = 2452
NERR_DCNotFound = 2453
NERR_LogonTrackingError = 2454
NERR_NetlogonNotStarted = 2455
NERR_CanNotGrowUASFile = 2456
NERR_TimeDiffAtDC = 2457
NERR_PasswordMismatch = 2458
NERR_NoSuchServer = 2460
NERR_NoSuchSession = 2461
NERR_NoSuchConnection = 2462
NERR_TooManyServers = 2463
NERR_TooManySessions = 2464
NERR_TooManyConnections = 2465
NERR_TooManyFiles = 2466
NERR_NoAlternateServers = 2467
NERR_TryDownLevel = 2470
NERR_UPSDriverNotStarted = 2480
NERR_UPSInvalidConfig = 2481
NERR_UPSInvalidCommPort = 2482
NERR_UPSSignalAsserted = 2483
NERR_UPSShutdownFailed = 2484
NERR_BadDosRetCode = 2500
NERR_ProgNeedsExtraMem = 2501
NERR_BadDosFunction = 2502
NERR_RemoteBootFailed = 2503
NERR_BadFileCheckSum = 2504
NERR_NoRplBootSystem = 2505
NERR_RplLoadrNetBiosErr = 2506
NERR_RplLoadrDiskErr = 2507
NERR_ImageParamErr = 2508
NERR_TooManyImageParams = 2509
NERR_NonDosFloppyUsed = 2510
NERR_RplBootRestart = 2511
NERR_RplSrvrCallFailed = 2512
NERR_CantConnectRplSrvr = 2513
NERR_CantOpenImageFile = 2514
NERR_CallingRplSrvr = 2515
NERR_StartingRplBoot = 2516
NERR_RplBootServiceTerm = 2517
NERR_RplBootStartFailed = 2518
NERR_RPL_CONNECTED = 2519
NERR_BrowserConfiguredToNotRun = 2550
NERR_RplNoAdaptersStarted = 2610
NERR_RplBadRegistry = 2611
NERR_RplBadDatabase = 2612
NERR_RplRplfilesShare = 2613
NERR_RplNotRplServer = 2614
NERR_RplCannotEnum = 2615
NERR_RplWkstaInfoCorrupted = 2616
NERR_RplWkstaNotFound = 2617
NERR_RplWkstaNameUnavailable = 2618
NERR_RplProfileInfoCorrupted = 2619
NERR_RplProfileNotFound = 2620
NERR_RplProfileNameUnavailable = 2621
NERR_RplProfileNotEmpty = 2622
NERR_RplConfigInfoCorrupted = 2623
NERR_RplConfigNotFound = 2624
NERR_RplAdapterInfoCorrupted = 2625
NERR_RplInternal = 2626
NERR_RplVendorInfoCorrupted = 2627
NERR_RplBootInfoCorrupted = 2628
NERR_RplWkstaNeedsUserAcct = 2629
NERR_RplNeedsRPLUSERAcct = 2630
NERR_RplBootNotFound = 2631
NERR_RplIncompatibleProfile = 2632
NERR_RplAdapterNameUnavailable = 2633
NERR_RplConfigNotEmpty = 2634
NERR_RplBootInUse = 2635
NERR_RplBackupDatabase = 2636
NERR_RplAdapterNotFound = 2637
NERR_RplVendorNotFound = 2638
NERR_RplVendorNameUnavailable = 2639
NERR_RplBootNameUnavailable = 2640
NERR_RplConfigNameUnavailable = 2641
NERR_DfsInternalCorruption = 2660
NERR_DfsVolumeDataCorrupt = 2661
NERR_DfsNoSuchVolume = 2662
NERR_DfsVolumeAlreadyExists = 2663
NERR_DfsAlreadyShared = 2664
NERR_DfsNoSuchShare = 2665
NERR_DfsNotALeafVolume = 2666
NERR_DfsLeafVolume = 2667
NERR_DfsVolumeHasMultipleServers = 2668
NERR_DfsCantCreateJunctionPoint = 2669
NERR_DfsServerNotDfsAware = 2670
NERR_DfsBadRenamePath = 2671
NERR_DfsVolumeIsOffline = 2672
NERR_DfsNoSuchServer = 2673
NERR_DfsCyclicalName = 2674
NERR_DfsNotSupportedInServerDfs = 2675
NERR_DfsDuplicateService = 2676
NERR_DfsCantRemoveLastServerShare = 2677
NERR_DfsVolumeIsInterDfs = 2678
NERR_DfsInconsistent = 2679
NERR_DfsServerUpgraded = 2680
NERR_DfsDataIsIdentical = 2681
NERR_DfsCantRemoveDfsRoot = 2682
NERR_DfsChildOrParentInDfs = 2683
NERR_DfsInternalError = 2690
NERR_SetupAlreadyJoined = 2691
NERR_SetupNotJoined = 2692
NERR_SetupDomainController = 2693
NERR_DefaultJoinRequired = 2694
NERR_InvalidWorkgroupName = 2695
NERR_NameUsesIncompatibleCodePage = 2696
NERR_ComputerAccountNotFound = 2697
NERR_PersonalSku = 2698
NERR_SetupCheckDNSConfig = 2699
NERR_AlreadyCloudDomainJoined = 2700
NERR_PasswordMustChange = 2701
NERR_AccountLockedOut = 2702
NERR_PasswordTooLong = 2703
NERR_PasswordNotComplexEnough = 2704
NERR_PasswordFilterError = 2705
NERR_NoOfflineJoinInfo = 2709
NERR_BadOfflineJoinInfo = 2710
NERR_CantCreateJoinInfo = 2711
NERR_BadDomainJoinInfo = 2712
NERR_JoinPerformedMustRestart = 2713
NERR_NoJoinPending = 2714
NERR_ValuesNotSet = 2715
NERR_CantVerifyHostname = 2716
NERR_CantLoadOfflineHive = 2717
NERR_ConnectionInsecure = 2718
NERR_ProvisioningBlobUnsupported = 2719
NERR_DS8DCRequired = 2720
NERR_LDAPCapableDCRequired = 2721
NERR_DS8DCNotFound = 2722
NERR_TargetVersionUnsupported = 2723
NERR_InvalidMachineNameForJoin = 2724
NERR_DS9DCNotFound = 2725
NERR_PlainTextSecretsRequired = 2726
NERR_CannotUnjoinAadDomain = 2727
MAX_NERR = 2999
UF_TEMP_DUPLICATE_ACCOUNT = 256
UF_NORMAL_ACCOUNT = 512
UF_INTERDOMAIN_TRUST_ACCOUNT = 2048
UF_WORKSTATION_TRUST_ACCOUNT = 4096
UF_SERVER_TRUST_ACCOUNT = 8192
UF_MNS_LOGON_ACCOUNT = 131072
UF_NO_AUTH_DATA_REQUIRED = 33554432
UF_PARTIAL_SECRETS_ACCOUNT = 67108864
UF_USE_AES_KEYS = 134217728
LG_INCLUDE_INDIRECT = 1
USER_NAME_PARMNUM = 1
USER_PASSWORD_PARMNUM = 3
USER_PASSWORD_AGE_PARMNUM = 4
USER_PRIV_PARMNUM = 5
USER_HOME_DIR_PARMNUM = 6
USER_COMMENT_PARMNUM = 7
USER_FLAGS_PARMNUM = 8
USER_SCRIPT_PATH_PARMNUM = 9
USER_AUTH_FLAGS_PARMNUM = 10
USER_FULL_NAME_PARMNUM = 11
USER_USR_COMMENT_PARMNUM = 12
USER_PARMS_PARMNUM = 13
USER_WORKSTATIONS_PARMNUM = 14
USER_LAST_LOGON_PARMNUM = 15
USER_LAST_LOGOFF_PARMNUM = 16
USER_ACCT_EXPIRES_PARMNUM = 17
USER_MAX_STORAGE_PARMNUM = 18
USER_UNITS_PER_WEEK_PARMNUM = 19
USER_LOGON_HOURS_PARMNUM = 20
USER_PAD_PW_COUNT_PARMNUM = 21
USER_NUM_LOGONS_PARMNUM = 22
USER_LOGON_SERVER_PARMNUM = 23
USER_COUNTRY_CODE_PARMNUM = 24
USER_CODE_PAGE_PARMNUM = 25
USER_PRIMARY_GROUP_PARMNUM = 51
USER_PROFILE = 52
USER_PROFILE_PARMNUM = 52
USER_HOME_DIR_DRIVE_PARMNUM = 53
NULL_USERSETINFO_PASSWD = '              '
UNITS_PER_DAY = 24
USER_PRIV_MASK = 3
MAX_PASSWD_LEN = 256
DEF_MIN_PWLEN = 6
DEF_PWUNIQUENESS = 5
DEF_MAX_PWHIST = 8
DEF_MAX_BADPW = 0
VALIDATED_LOGON = 0
PASSWORD_EXPIRED = 2
NON_VALIDATED_LOGON = 3
VALID_LOGOFF = 1
MODALS_MIN_PASSWD_LEN_PARMNUM = 1
MODALS_MAX_PASSWD_AGE_PARMNUM = 2
MODALS_MIN_PASSWD_AGE_PARMNUM = 3
MODALS_FORCE_LOGOFF_PARMNUM = 4
MODALS_PASSWD_HIST_LEN_PARMNUM = 5
MODALS_ROLE_PARMNUM = 6
MODALS_PRIMARY_PARMNUM = 7
MODALS_DOMAIN_NAME_PARMNUM = 8
MODALS_DOMAIN_ID_PARMNUM = 9
MODALS_LOCKOUT_DURATION_PARMNUM = 10
MODALS_LOCKOUT_OBSERVATION_WINDOW_PARMNUM = 11
MODALS_LOCKOUT_THRESHOLD_PARMNUM = 12
GROUPIDMASK = 32768
GROUP_SPECIALGRP_USERS = 'USERS'
GROUP_SPECIALGRP_ADMINS = 'ADMINS'
GROUP_SPECIALGRP_GUESTS = 'GUESTS'
GROUP_SPECIALGRP_LOCAL = 'LOCAL'
GROUP_ALL_PARMNUM = 0
GROUP_NAME_PARMNUM = 1
GROUP_COMMENT_PARMNUM = 2
GROUP_ATTRIBUTES_PARMNUM = 3
LOCALGROUP_NAME_PARMNUM = 1
LOCALGROUP_COMMENT_PARMNUM = 2
MAXPERMENTRIES = 64
ACCESS_NONE = 0
ACCESS_GROUP = 32768
ACCESS_AUDIT = 1
ACCESS_SUCCESS_OPEN = 16
ACCESS_SUCCESS_WRITE = 32
ACCESS_SUCCESS_DELETE = 64
ACCESS_SUCCESS_ACL = 128
ACCESS_SUCCESS_MASK = 240
ACCESS_FAIL_OPEN = 256
ACCESS_FAIL_WRITE = 512
ACCESS_FAIL_DELETE = 1024
ACCESS_FAIL_ACL = 2048
ACCESS_FAIL_MASK = 3840
ACCESS_FAIL_SHIFT = 4
ACCESS_RESOURCE_NAME_PARMNUM = 1
ACCESS_ATTR_PARMNUM = 2
ACCESS_COUNT_PARMNUM = 3
ACCESS_ACCESS_LIST_PARMNUM = 4
ACCESS_LETTERS = 'RWCXDAP         '
NET_VALIDATE_PASSWORD_LAST_SET = 1
NET_VALIDATE_BAD_PASSWORD_TIME = 2
NET_VALIDATE_LOCKOUT_TIME = 4
NET_VALIDATE_BAD_PASSWORD_COUNT = 8
NET_VALIDATE_PASSWORD_HISTORY_LENGTH = 16
NET_VALIDATE_PASSWORD_HISTORY = 32
NETLOGON_CONTROL_QUERY = 1
NETLOGON_CONTROL_REPLICATE = 2
NETLOGON_CONTROL_SYNCHRONIZE = 3
NETLOGON_CONTROL_PDC_REPLICATE = 4
NETLOGON_CONTROL_REDISCOVER = 5
NETLOGON_CONTROL_TC_QUERY = 6
NETLOGON_CONTROL_TRANSPORT_NOTIFY = 7
NETLOGON_CONTROL_FIND_USER = 8
NETLOGON_CONTROL_CHANGE_PASSWORD = 9
NETLOGON_CONTROL_TC_VERIFY = 10
NETLOGON_CONTROL_FORCE_DNS_REG = 11
NETLOGON_CONTROL_QUERY_DNS_REG = 12
NETLOGON_CONTROL_QUERY_ENC_TYPES = 13
NETLOGON_CONTROL_UNLOAD_NETLOGON_DLL = 65531
NETLOGON_CONTROL_BACKUP_CHANGE_LOG = 65532
NETLOGON_CONTROL_TRUNCATE_LOG = 65533
NETLOGON_CONTROL_SET_DBFLAG = 65534
NETLOGON_CONTROL_BREAKPOINT = 65535
NETLOGON_REPLICATION_NEEDED = 1
NETLOGON_REPLICATION_IN_PROGRESS = 2
NETLOGON_FULL_SYNC_REPLICATION = 4
NETLOGON_REDO_NEEDED = 8
NETLOGON_HAS_IP = 16
NETLOGON_HAS_TIMESERV = 32
NETLOGON_DNS_UPDATE_FAILURE = 64
NETLOGON_VERIFY_STATUS_RETURNED = 128
SERVICE_ACCOUNT_PASSWORD = '_SA_{262E99C9-6160-4871-ACEC-4E61736B6F21}'
SERVICE_ACCOUNT_SECRET_PREFIX = '_SC_{262E99C9-6160-4871-ACEC-4E61736B6F21}_'
def _define_ServiceAccountPasswordGUID():
    return Guid('262e99c9-6160-4871-ac-ec-4e-61-73-6b-6f-21')
SERVICE_ACCOUNT_FLAG_LINK_TO_HOST_ONLY = 1
SERVICE_ACCOUNT_FLAG_ADD_AGAINST_RODC = 2
SERVICE_ACCOUNT_FLAG_UNLINK_FROM_HOST_ONLY = 1
SERVICE_ACCOUNT_FLAG_REMOVE_OFFLINE = 2
ALERTER_MAILSLOT = '\\\\.\\MAILSLOT\\Alerter'
ALERT_PRINT_EVENT = 'PRINTING'
ALERT_MESSAGE_EVENT = 'MESSAGE'
ALERT_ERRORLOG_EVENT = 'ERRORLOG'
ALERT_ADMIN_EVENT = 'ADMIN'
ALERT_USER_EVENT = 'USER'
PRJOB_QSTATUS = 3
PRJOB_DEVSTATUS = 508
PRJOB_COMPLETE = 4
PRJOB_INTERV = 8
PRJOB_ERROR = 16
PRJOB_DESTOFFLINE = 32
PRJOB_DESTPAUSED = 64
PRJOB_NOTIFY = 128
PRJOB_DESTNOPAPER = 256
PRJOB_DELETED = 32768
PRJOB_QS_QUEUED = 0
PRJOB_QS_PAUSED = 1
PRJOB_QS_SPOOLING = 2
PRJOB_QS_PRINTING = 3
JOB_RUN_PERIODICALLY = 1
JOB_EXEC_ERROR = 2
JOB_RUNS_TODAY = 4
JOB_ADD_CURRENT_DATE = 8
JOB_NONINTERACTIVE = 16
LOGFLAGS_FORWARD = 0
LOGFLAGS_BACKWARD = 1
LOGFLAGS_SEEK = 2
ACTION_LOCKOUT = 0
ACTION_ADMINUNLOCK = 1
AE_SRVSTATUS_CONSTANT = 0
AE_SESSLOGON_CONSTANT = 1
AE_SESSLOGOFF_CONSTANT = 2
AE_SESSPWERR_CONSTANT = 3
AE_CONNSTART_CONSTANT = 4
AE_CONNSTOP_CONSTANT = 5
AE_CONNREJ_CONSTANT = 6
AE_RESACCESS_CONSTANT = 7
AE_RESACCESSREJ_CONSTANT = 8
AE_CLOSEFILE_CONSTANT = 9
AE_SERVICESTAT_CONSTANT = 11
AE_ACLMOD_CONSTANT = 12
AE_UASMOD_CONSTANT = 13
AE_NETLOGON_CONSTANT = 14
AE_NETLOGOFF_CONSTANT = 15
AE_NETLOGDENIED = 16
AE_ACCLIMITEXCD = 17
AE_RESACCESS2 = 18
AE_ACLMODFAIL = 19
AE_LOCKOUT_CONSTANT = 20
AE_GENERIC_TYPE = 21
AE_SRVSTART = 0
AE_SRVPAUSED = 1
AE_SRVCONT = 2
AE_SRVSTOP = 3
AE_GUEST = 0
AE_USER = 1
AE_ADMIN = 2
AE_NORMAL = 0
AE_USERLIMIT = 0
AE_GENERAL = 0
AE_ERROR = 1
AE_SESSDIS = 1
AE_BADPW = 1
AE_AUTODIS = 2
AE_UNSHARE = 2
AE_ADMINPRIVREQD = 2
AE_ADMINDIS = 3
AE_NOACCESSPERM = 3
AE_ACCRESTRICT = 4
AE_NORMAL_CLOSE = 0
AE_SES_CLOSE = 1
AE_ADMIN_CLOSE = 2
AE_LIM_UNKNOWN = 0
AE_LIM_LOGONHOURS = 1
AE_LIM_EXPIRED = 2
AE_LIM_INVAL_WKSTA = 3
AE_LIM_DISABLED = 4
AE_LIM_DELETED = 5
AE_MOD = 0
AE_DELETE = 1
AE_ADD = 2
AE_UAS_USER = 0
AE_UAS_GROUP = 1
AE_UAS_MODALS = 2
SVAUD_SERVICE = 1
SVAUD_GOODSESSLOGON = 6
SVAUD_BADSESSLOGON = 24
SVAUD_GOODNETLOGON = 96
SVAUD_BADNETLOGON = 384
SVAUD_GOODUSE = 1536
SVAUD_BADUSE = 6144
SVAUD_USERLIST = 8192
SVAUD_PERMISSIONS = 16384
SVAUD_RESOURCE = 32768
SVAUD_LOGONLIM = 65536
AA_AUDIT_ALL = 1
AA_A_OWNER = 4
AA_CLOSE = 8
AA_S_OPEN = 16
AA_S_WRITE = 32
AA_S_CREATE = 32
AA_S_DELETE = 64
AA_S_ACL = 128
AA_F_OPEN = 256
AA_F_WRITE = 512
AA_F_CREATE = 512
AA_F_DELETE = 1024
AA_F_ACL = 2048
AA_A_OPEN = 4096
AA_A_WRITE = 8192
AA_A_CREATE = 8192
AA_A_DELETE = 16384
AA_A_ACL = 32768
ERRLOG_BASE = 3100
NELOG_Internal_Error = 3100
NELOG_Resource_Shortage = 3101
NELOG_Unable_To_Lock_Segment = 3102
NELOG_Unable_To_Unlock_Segment = 3103
NELOG_Uninstall_Service = 3104
NELOG_Init_Exec_Fail = 3105
NELOG_Ncb_Error = 3106
NELOG_Net_Not_Started = 3107
NELOG_Ioctl_Error = 3108
NELOG_System_Semaphore = 3109
NELOG_Init_OpenCreate_Err = 3110
NELOG_NetBios = 3111
NELOG_SMB_Illegal = 3112
NELOG_Service_Fail = 3113
NELOG_Entries_Lost = 3114
NELOG_Init_Seg_Overflow = 3120
NELOG_Srv_No_Mem_Grow = 3121
NELOG_Access_File_Bad = 3122
NELOG_Srvnet_Not_Started = 3123
NELOG_Init_Chardev_Err = 3124
NELOG_Remote_API = 3125
NELOG_Ncb_TooManyErr = 3126
NELOG_Mailslot_err = 3127
NELOG_ReleaseMem_Alert = 3128
NELOG_AT_cannot_write = 3129
NELOG_Cant_Make_Msg_File = 3130
NELOG_Exec_Netservr_NoMem = 3131
NELOG_Server_Lock_Failure = 3132
NELOG_Msg_Shutdown = 3140
NELOG_Msg_Sem_Shutdown = 3141
NELOG_Msg_Log_Err = 3150
NELOG_VIO_POPUP_ERR = 3151
NELOG_Msg_Unexpected_SMB_Type = 3152
NELOG_Wksta_Infoseg = 3160
NELOG_Wksta_Compname = 3161
NELOG_Wksta_BiosThreadFailure = 3162
NELOG_Wksta_IniSeg = 3163
NELOG_Wksta_HostTab_Full = 3164
NELOG_Wksta_Bad_Mailslot_SMB = 3165
NELOG_Wksta_UASInit = 3166
NELOG_Wksta_SSIRelogon = 3167
NELOG_Build_Name = 3170
NELOG_Name_Expansion = 3171
NELOG_Message_Send = 3172
NELOG_Mail_Slt_Err = 3173
NELOG_AT_cannot_read = 3174
NELOG_AT_sched_err = 3175
NELOG_AT_schedule_file_created = 3176
NELOG_Srvnet_NB_Open = 3177
NELOG_AT_Exec_Err = 3178
NELOG_Lazy_Write_Err = 3180
NELOG_HotFix = 3181
NELOG_HardErr_From_Server = 3182
NELOG_LocalSecFail1 = 3183
NELOG_LocalSecFail2 = 3184
NELOG_LocalSecFail3 = 3185
NELOG_LocalSecGeneralFail = 3186
NELOG_NetWkSta_Internal_Error = 3190
NELOG_NetWkSta_No_Resource = 3191
NELOG_NetWkSta_SMB_Err = 3192
NELOG_NetWkSta_VC_Err = 3193
NELOG_NetWkSta_Stuck_VC_Err = 3194
NELOG_NetWkSta_NCB_Err = 3195
NELOG_NetWkSta_Write_Behind_Err = 3196
NELOG_NetWkSta_Reset_Err = 3197
NELOG_NetWkSta_Too_Many = 3198
NELOG_Srv_Thread_Failure = 3204
NELOG_Srv_Close_Failure = 3205
NELOG_ReplUserCurDir = 3206
NELOG_ReplCannotMasterDir = 3207
NELOG_ReplUpdateError = 3208
NELOG_ReplLostMaster = 3209
NELOG_NetlogonAuthDCFail = 3210
NELOG_ReplLogonFailed = 3211
NELOG_ReplNetErr = 3212
NELOG_ReplMaxFiles = 3213
NELOG_ReplMaxTreeDepth = 3214
NELOG_ReplBadMsg = 3215
NELOG_ReplSysErr = 3216
NELOG_ReplUserLoged = 3217
NELOG_ReplBadImport = 3218
NELOG_ReplBadExport = 3219
NELOG_ReplSignalFileErr = 3220
NELOG_DiskFT = 3221
NELOG_ReplAccessDenied = 3222
NELOG_NetlogonFailedPrimary = 3223
NELOG_NetlogonPasswdSetFailed = 3224
NELOG_NetlogonTrackingError = 3225
NELOG_NetlogonSyncError = 3226
NELOG_NetlogonRequireSignOrSealError = 3227
NELOG_UPS_PowerOut = 3230
NELOG_UPS_Shutdown = 3231
NELOG_UPS_CmdFileError = 3232
NELOG_UPS_CannotOpenDriver = 3233
NELOG_UPS_PowerBack = 3234
NELOG_UPS_CmdFileConfig = 3235
NELOG_UPS_CmdFileExec = 3236
NELOG_Missing_Parameter = 3250
NELOG_Invalid_Config_Line = 3251
NELOG_Invalid_Config_File = 3252
NELOG_File_Changed = 3253
NELOG_Files_Dont_Fit = 3254
NELOG_Wrong_DLL_Version = 3255
NELOG_Error_in_DLL = 3256
NELOG_System_Error = 3257
NELOG_FT_ErrLog_Too_Large = 3258
NELOG_FT_Update_In_Progress = 3259
NELOG_Joined_Domain = 3260
NELOG_Joined_Workgroup = 3261
NELOG_OEM_Code = 3299
ERRLOG2_BASE = 5700
NELOG_NetlogonSSIInitError = 5700
NELOG_NetlogonFailedToUpdateTrustList = 5701
NELOG_NetlogonFailedToAddRpcInterface = 5702
NELOG_NetlogonFailedToReadMailslot = 5703
NELOG_NetlogonFailedToRegisterSC = 5704
NELOG_NetlogonChangeLogCorrupt = 5705
NELOG_NetlogonFailedToCreateShare = 5706
NELOG_NetlogonDownLevelLogonFailed = 5707
NELOG_NetlogonDownLevelLogoffFailed = 5708
NELOG_NetlogonNTLogonFailed = 5709
NELOG_NetlogonNTLogoffFailed = 5710
NELOG_NetlogonPartialSyncCallSuccess = 5711
NELOG_NetlogonPartialSyncCallFailed = 5712
NELOG_NetlogonFullSyncCallSuccess = 5713
NELOG_NetlogonFullSyncCallFailed = 5714
NELOG_NetlogonPartialSyncSuccess = 5715
NELOG_NetlogonPartialSyncFailed = 5716
NELOG_NetlogonFullSyncSuccess = 5717
NELOG_NetlogonFullSyncFailed = 5718
NELOG_NetlogonAuthNoDomainController = 5719
NELOG_NetlogonAuthNoTrustLsaSecret = 5720
NELOG_NetlogonAuthNoTrustSamAccount = 5721
NELOG_NetlogonServerAuthFailed = 5722
NELOG_NetlogonServerAuthNoTrustSamAccount = 5723
NELOG_FailedToRegisterSC = 5724
NELOG_FailedToSetServiceStatus = 5725
NELOG_FailedToGetComputerName = 5726
NELOG_DriverNotLoaded = 5727
NELOG_NoTranportLoaded = 5728
NELOG_NetlogonFailedDomainDelta = 5729
NELOG_NetlogonFailedGlobalGroupDelta = 5730
NELOG_NetlogonFailedLocalGroupDelta = 5731
NELOG_NetlogonFailedUserDelta = 5732
NELOG_NetlogonFailedPolicyDelta = 5733
NELOG_NetlogonFailedTrustedDomainDelta = 5734
NELOG_NetlogonFailedAccountDelta = 5735
NELOG_NetlogonFailedSecretDelta = 5736
NELOG_NetlogonSystemError = 5737
NELOG_NetlogonDuplicateMachineAccounts = 5738
NELOG_NetlogonTooManyGlobalGroups = 5739
NELOG_NetlogonBrowserDriver = 5740
NELOG_NetlogonAddNameFailure = 5741
NELOG_RplMessages = 5742
NELOG_RplXnsBoot = 5743
NELOG_RplSystem = 5744
NELOG_RplWkstaTimeout = 5745
NELOG_RplWkstaFileOpen = 5746
NELOG_RplWkstaFileRead = 5747
NELOG_RplWkstaMemory = 5748
NELOG_RplWkstaFileChecksum = 5749
NELOG_RplWkstaFileLineCount = 5750
NELOG_RplWkstaBbcFile = 5751
NELOG_RplWkstaFileSize = 5752
NELOG_RplWkstaInternal = 5753
NELOG_RplWkstaWrongVersion = 5754
NELOG_RplWkstaNetwork = 5755
NELOG_RplAdapterResource = 5756
NELOG_RplFileCopy = 5757
NELOG_RplFileDelete = 5758
NELOG_RplFilePerms = 5759
NELOG_RplCheckConfigs = 5760
NELOG_RplCreateProfiles = 5761
NELOG_RplRegistry = 5762
NELOG_RplReplaceRPLDISK = 5763
NELOG_RplCheckSecurity = 5764
NELOG_RplBackupDatabase = 5765
NELOG_RplInitDatabase = 5766
NELOG_RplRestoreDatabaseFailure = 5767
NELOG_RplRestoreDatabaseSuccess = 5768
NELOG_RplInitRestoredDatabase = 5769
NELOG_NetlogonSessionTypeWrong = 5770
NELOG_RplUpgradeDBTo40 = 5771
NELOG_NetlogonLanmanBdcsNotAllowed = 5772
NELOG_NetlogonNoDynamicDns = 5773
NELOG_NetlogonDynamicDnsRegisterFailure = 5774
NELOG_NetlogonDynamicDnsDeregisterFailure = 5775
NELOG_NetlogonFailedFileCreate = 5776
NELOG_NetlogonGetSubnetToSite = 5777
NELOG_NetlogonNoSiteForClient = 5778
NELOG_NetlogonBadSiteName = 5779
NELOG_NetlogonBadSubnetName = 5780
NELOG_NetlogonDynamicDnsServerFailure = 5781
NELOG_NetlogonDynamicDnsFailure = 5782
NELOG_NetlogonRpcCallCancelled = 5783
NELOG_NetlogonDcSiteCovered = 5784
NELOG_NetlogonDcSiteNotCovered = 5785
NELOG_NetlogonGcSiteCovered = 5786
NELOG_NetlogonGcSiteNotCovered = 5787
NELOG_NetlogonFailedSpnUpdate = 5788
NELOG_NetlogonFailedDnsHostNameUpdate = 5789
NELOG_NetlogonAuthNoUplevelDomainController = 5790
NELOG_NetlogonAuthDomainDowngraded = 5791
NELOG_NetlogonNdncSiteCovered = 5792
NELOG_NetlogonNdncSiteNotCovered = 5793
NELOG_NetlogonDcOldSiteCovered = 5794
NELOG_NetlogonDcSiteNotCoveredAuto = 5795
NELOG_NetlogonGcOldSiteCovered = 5796
NELOG_NetlogonGcSiteNotCoveredAuto = 5797
NELOG_NetlogonNdncOldSiteCovered = 5798
NELOG_NetlogonNdncSiteNotCoveredAuto = 5799
NELOG_NetlogonSpnMultipleSamAccountNames = 5800
NELOG_NetlogonSpnCrackNamesFailure = 5801
NELOG_NetlogonNoAddressToSiteMapping = 5802
NELOG_NetlogonInvalidGenericParameterValue = 5803
NELOG_NetlogonInvalidDwordParameterValue = 5804
NELOG_NetlogonServerAuthFailedNoAccount = 5805
NELOG_NetlogonNoDynamicDnsManual = 5806
NELOG_NetlogonNoSiteForClients = 5807
NELOG_NetlogonDnsDeregAborted = 5808
NELOG_NetlogonRpcPortRequestFailure = 5809
NELOG_NetlogonPartialSiteMappingForClients = 5810
NELOG_NetlogonRemoteDynamicDnsRegisterFailure = 5811
NELOG_NetlogonRemoteDynamicDnsDeregisterFailure = 5812
NELOG_NetlogonRejectedRemoteDynamicDnsRegister = 5813
NELOG_NetlogonRejectedRemoteDynamicDnsDeregister = 5814
NELOG_NetlogonRemoteDynamicDnsUpdateRequestFailure = 5815
NELOG_NetlogonUserValidationReqInitialTimeOut = 5816
NELOG_NetlogonUserValidationReqRecurringTimeOut = 5817
NELOG_NetlogonUserValidationReqWaitInitialWarning = 5818
NELOG_NetlogonUserValidationReqWaitRecurringWarning = 5819
NELOG_NetlogonFailedToAddAuthzRpcInterface = 5820
NELOG_NetLogonFailedToInitializeAuthzRm = 5821
NELOG_NetLogonFailedToInitializeRPCSD = 5822
NELOG_NetlogonMachinePasswdSetSucceeded = 5823
NELOG_NetlogonMsaPasswdSetSucceeded = 5824
NELOG_NetlogonDnsHostNameLowerCasingFailed = 5825
NETLOG_NetlogonNonWindowsSupportsSecureRpc = 5826
NETLOG_NetlogonUnsecureRpcClient = 5827
NETLOG_NetlogonUnsecureRpcTrust = 5828
NETLOG_NetlogonUnsecuredRpcMachineTemporarilyAllowed = 5829
NETLOG_NetlogonUnsecureRpcMachineAllowedBySsdl = 5830
NETLOG_NetlogonUnsecureRpcTrustAllowedBySsdl = 5831
NETSETUP_ACCT_DELETE = 4
NETSETUP_DNS_NAME_CHANGES_ONLY = 4096
NETSETUP_INSTALL_INVOCATION = 262144
NETSETUP_ALT_SAMACCOUNTNAME = 131072
NET_IGNORE_UNSUPPORTED_FLAGS = 1
NETSETUP_PROVISION_PERSISTENTSITE = 32
NETSETUP_PROVISION_CHECK_PWD_ONLY = 2147483648
NETSETUP_PROVISIONING_PARAMS_WIN8_VERSION = 1
NETSETUP_PROVISIONING_PARAMS_CURRENT_VERSION = 2
MSGNAME_NOT_FORWARDED = 0
MSGNAME_FORWARDED_TO = 4
MSGNAME_FORWARDED_FROM = 16
SUPPORTS_ANY = -1
NO_PERMISSION_REQUIRED = 1
ALLOCATE_RESPONSE = 2
USE_SPECIFIC_TRANSPORT = 2147483648
SV_PLATFORM_ID_OS2 = 400
SV_PLATFORM_ID_NT = 500
MAJOR_VERSION_MASK = 15
SV_NODISC = -1
SV_PLATFORM_ID_PARMNUM = 101
SV_NAME_PARMNUM = 102
SV_VERSION_MAJOR_PARMNUM = 103
SV_VERSION_MINOR_PARMNUM = 104
SV_TYPE_PARMNUM = 105
SV_COMMENT_PARMNUM = 5
SV_USERS_PARMNUM = 107
SV_DISC_PARMNUM = 10
SV_HIDDEN_PARMNUM = 16
SV_ANNOUNCE_PARMNUM = 17
SV_ANNDELTA_PARMNUM = 18
SV_USERPATH_PARMNUM = 112
SV_ULIST_MTIME_PARMNUM = 401
SV_GLIST_MTIME_PARMNUM = 402
SV_ALIST_MTIME_PARMNUM = 403
SV_ALERTS_PARMNUM = 11
SV_SECURITY_PARMNUM = 405
SV_NUMADMIN_PARMNUM = 406
SV_LANMASK_PARMNUM = 407
SV_GUESTACC_PARMNUM = 408
SV_CHDEVQ_PARMNUM = 410
SV_CHDEVJOBS_PARMNUM = 411
SV_CONNECTIONS_PARMNUM = 412
SV_SHARES_PARMNUM = 413
SV_OPENFILES_PARMNUM = 414
SV_SESSREQS_PARMNUM = 417
SV_ACTIVELOCKS_PARMNUM = 419
SV_NUMREQBUF_PARMNUM = 420
SV_NUMBIGBUF_PARMNUM = 422
SV_NUMFILETASKS_PARMNUM = 423
SV_ALERTSCHED_PARMNUM = 37
SV_ERRORALERT_PARMNUM = 38
SV_LOGONALERT_PARMNUM = 39
SV_ACCESSALERT_PARMNUM = 40
SV_DISKALERT_PARMNUM = 41
SV_NETIOALERT_PARMNUM = 42
SV_MAXAUDITSZ_PARMNUM = 43
SV_SRVHEURISTICS_PARMNUM = 431
SV_SESSOPENS_PARMNUM = 501
SV_SESSVCS_PARMNUM = 502
SV_OPENSEARCH_PARMNUM = 503
SV_SIZREQBUF_PARMNUM = 504
SV_INITWORKITEMS_PARMNUM = 505
SV_MAXWORKITEMS_PARMNUM = 506
SV_RAWWORKITEMS_PARMNUM = 507
SV_IRPSTACKSIZE_PARMNUM = 508
SV_MAXRAWBUFLEN_PARMNUM = 509
SV_SESSUSERS_PARMNUM = 510
SV_SESSCONNS_PARMNUM = 511
SV_MAXNONPAGEDMEMORYUSAGE_PARMNUM = 512
SV_MAXPAGEDMEMORYUSAGE_PARMNUM = 513
SV_ENABLESOFTCOMPAT_PARMNUM = 514
SV_ENABLEFORCEDLOGOFF_PARMNUM = 515
SV_TIMESOURCE_PARMNUM = 516
SV_ACCEPTDOWNLEVELAPIS_PARMNUM = 517
SV_LMANNOUNCE_PARMNUM = 518
SV_DOMAIN_PARMNUM = 519
SV_MAXCOPYREADLEN_PARMNUM = 520
SV_MAXCOPYWRITELEN_PARMNUM = 521
SV_MINKEEPSEARCH_PARMNUM = 522
SV_MAXKEEPSEARCH_PARMNUM = 523
SV_MINKEEPCOMPLSEARCH_PARMNUM = 524
SV_MAXKEEPCOMPLSEARCH_PARMNUM = 525
SV_THREADCOUNTADD_PARMNUM = 526
SV_NUMBLOCKTHREADS_PARMNUM = 527
SV_SCAVTIMEOUT_PARMNUM = 528
SV_MINRCVQUEUE_PARMNUM = 529
SV_MINFREEWORKITEMS_PARMNUM = 530
SV_XACTMEMSIZE_PARMNUM = 531
SV_THREADPRIORITY_PARMNUM = 532
SV_MAXMPXCT_PARMNUM = 533
SV_OPLOCKBREAKWAIT_PARMNUM = 534
SV_OPLOCKBREAKRESPONSEWAIT_PARMNUM = 535
SV_ENABLEOPLOCKS_PARMNUM = 536
SV_ENABLEOPLOCKFORCECLOSE_PARMNUM = 537
SV_ENABLEFCBOPENS_PARMNUM = 538
SV_ENABLERAW_PARMNUM = 539
SV_ENABLESHAREDNETDRIVES_PARMNUM = 540
SV_MINFREECONNECTIONS_PARMNUM = 541
SV_MAXFREECONNECTIONS_PARMNUM = 542
SV_INITSESSTABLE_PARMNUM = 543
SV_INITCONNTABLE_PARMNUM = 544
SV_INITFILETABLE_PARMNUM = 545
SV_INITSEARCHTABLE_PARMNUM = 546
SV_ALERTSCHEDULE_PARMNUM = 547
SV_ERRORTHRESHOLD_PARMNUM = 548
SV_NETWORKERRORTHRESHOLD_PARMNUM = 549
SV_DISKSPACETHRESHOLD_PARMNUM = 550
SV_MAXLINKDELAY_PARMNUM = 552
SV_MINLINKTHROUGHPUT_PARMNUM = 553
SV_LINKINFOVALIDTIME_PARMNUM = 554
SV_SCAVQOSINFOUPDATETIME_PARMNUM = 555
SV_MAXWORKITEMIDLETIME_PARMNUM = 556
SV_MAXRAWWORKITEMS_PARMNUM = 557
SV_PRODUCTTYPE_PARMNUM = 560
SV_SERVERSIZE_PARMNUM = 561
SV_CONNECTIONLESSAUTODISC_PARMNUM = 562
SV_SHARINGVIOLATIONRETRIES_PARMNUM = 563
SV_SHARINGVIOLATIONDELAY_PARMNUM = 564
SV_MAXGLOBALOPENSEARCH_PARMNUM = 565
SV_REMOVEDUPLICATESEARCHES_PARMNUM = 566
SV_LOCKVIOLATIONRETRIES_PARMNUM = 567
SV_LOCKVIOLATIONOFFSET_PARMNUM = 568
SV_LOCKVIOLATIONDELAY_PARMNUM = 569
SV_MDLREADSWITCHOVER_PARMNUM = 570
SV_CACHEDOPENLIMIT_PARMNUM = 571
SV_CRITICALTHREADS_PARMNUM = 572
SV_RESTRICTNULLSESSACCESS_PARMNUM = 573
SV_ENABLEWFW311DIRECTIPX_PARMNUM = 574
SV_OTHERQUEUEAFFINITY_PARMNUM = 575
SV_QUEUESAMPLESECS_PARMNUM = 576
SV_BALANCECOUNT_PARMNUM = 577
SV_PREFERREDAFFINITY_PARMNUM = 578
SV_MAXFREERFCBS_PARMNUM = 579
SV_MAXFREEMFCBS_PARMNUM = 580
SV_MAXFREELFCBS_PARMNUM = 581
SV_MAXFREEPAGEDPOOLCHUNKS_PARMNUM = 582
SV_MINPAGEDPOOLCHUNKSIZE_PARMNUM = 583
SV_MAXPAGEDPOOLCHUNKSIZE_PARMNUM = 584
SV_SENDSFROMPREFERREDPROCESSOR_PARMNUM = 585
SV_MAXTHREADSPERQUEUE_PARMNUM = 586
SV_CACHEDDIRECTORYLIMIT_PARMNUM = 587
SV_MAXCOPYLENGTH_PARMNUM = 588
SV_ENABLECOMPRESSION_PARMNUM = 590
SV_AUTOSHAREWKS_PARMNUM = 591
SV_AUTOSHARESERVER_PARMNUM = 592
SV_ENABLESECURITYSIGNATURE_PARMNUM = 593
SV_REQUIRESECURITYSIGNATURE_PARMNUM = 594
SV_MINCLIENTBUFFERSIZE_PARMNUM = 595
SV_CONNECTIONNOSESSIONSTIMEOUT_PARMNUM = 596
SV_IDLETHREADTIMEOUT_PARMNUM = 597
SV_ENABLEW9XSECURITYSIGNATURE_PARMNUM = 598
SV_ENFORCEKERBEROSREAUTHENTICATION_PARMNUM = 599
SV_DISABLEDOS_PARMNUM = 600
SV_LOWDISKSPACEMINIMUM_PARMNUM = 601
SV_DISABLESTRICTNAMECHECKING_PARMNUM = 602
SV_ENABLEAUTHENTICATEUSERSHARING_PARMNUM = 603
SVI1_NUM_ELEMENTS = 5
SVI2_NUM_ELEMENTS = 40
SVI3_NUM_ELEMENTS = 44
SV_MAX_CMD_LEN = 256
SW_AUTOPROF_LOAD_MASK = 1
SW_AUTOPROF_SAVE_MASK = 2
SV_MAX_SRV_HEUR_LEN = 32
SV_USERS_PER_LICENSE = 5
SVTI2_REMAP_PIPE_NAMES = 2
SVTI2_SCOPED_NAME = 4
SVTI2_CLUSTER_NAME = 8
SVTI2_CLUSTER_DNN_NAME = 16
SVTI2_UNICODE_TRANSPORT_ADDRESS = 32
SVTI2_RESERVED1 = 4096
SVTI2_RESERVED2 = 8192
SVTI2_RESERVED3 = 16384
SRV_SUPPORT_HASH_GENERATION = 1
SRV_HASH_GENERATION_ACTIVE = 2
SERVICE_INSTALL_STATE = 3
SERVICE_UNINSTALLED = 0
SERVICE_INSTALL_PENDING = 1
SERVICE_UNINSTALL_PENDING = 2
SERVICE_INSTALLED = 3
SERVICE_PAUSE_STATE = 12
LM20_SERVICE_ACTIVE = 0
LM20_SERVICE_CONTINUE_PENDING = 4
LM20_SERVICE_PAUSE_PENDING = 8
LM20_SERVICE_PAUSED = 12
SERVICE_NOT_UNINSTALLABLE = 0
SERVICE_UNINSTALLABLE = 16
SERVICE_NOT_PAUSABLE = 0
SERVICE_PAUSABLE = 32
SERVICE_REDIR_PAUSED = 1792
SERVICE_REDIR_DISK_PAUSED = 256
SERVICE_REDIR_PRINT_PAUSED = 512
SERVICE_REDIR_COMM_PAUSED = 1024
SERVICE_DOS_ENCRYPTION = 'ENCRYPT'
SERVICE_CTRL_INTERROGATE = 0
SERVICE_CTRL_PAUSE = 1
SERVICE_CTRL_CONTINUE = 2
SERVICE_CTRL_UNINSTALL = 3
SERVICE_CTRL_REDIR_DISK = 1
SERVICE_CTRL_REDIR_PRINT = 2
SERVICE_CTRL_REDIR_COMM = 4
SERVICE_IP_NO_HINT = 0
SERVICE_CCP_NO_HINT = 0
SERVICE_IP_QUERY_HINT = 65536
SERVICE_CCP_QUERY_HINT = 65536
SERVICE_IP_CHKPT_NUM = 255
SERVICE_CCP_CHKPT_NUM = 255
SERVICE_IP_WAIT_TIME = 65280
SERVICE_CCP_WAIT_TIME = 65280
SERVICE_IP_WAITTIME_SHIFT = 8
SERVICE_NTIP_WAITTIME_SHIFT = 12
UPPER_HINT_MASK = 65280
LOWER_HINT_MASK = 255
UPPER_GET_HINT_MASK = 267386880
LOWER_GET_HINT_MASK = 65280
SERVICE_NT_MAXTIME = 65535
SERVICE_RESRV_MASK = 131071
SERVICE_MAXTIME = 255
SERVICE_BASE = 3050
SERVICE_UIC_NORMAL = 0
SERVICE_UIC_BADPARMVAL = 3051
SERVICE_UIC_MISSPARM = 3052
SERVICE_UIC_UNKPARM = 3053
SERVICE_UIC_RESOURCE = 3054
SERVICE_UIC_CONFIG = 3055
SERVICE_UIC_SYSTEM = 3056
SERVICE_UIC_INTERNAL = 3057
SERVICE_UIC_AMBIGPARM = 3058
SERVICE_UIC_DUPPARM = 3059
SERVICE_UIC_KILL = 3060
SERVICE_UIC_EXEC = 3061
SERVICE_UIC_SUBSERV = 3062
SERVICE_UIC_CONFLPARM = 3063
SERVICE_UIC_FILE = 3064
SERVICE_UIC_M_NULL = 0
SERVICE_UIC_M_MEMORY = 3070
SERVICE_UIC_M_DISK = 3071
SERVICE_UIC_M_THREADS = 3072
SERVICE_UIC_M_PROCESSES = 3073
SERVICE_UIC_M_SECURITY = 3074
SERVICE_UIC_M_LANROOT = 3075
SERVICE_UIC_M_REDIR = 3076
SERVICE_UIC_M_SERVER = 3077
SERVICE_UIC_M_SEC_FILE_ERR = 3078
SERVICE_UIC_M_FILES = 3079
SERVICE_UIC_M_LOGS = 3080
SERVICE_UIC_M_LANGROUP = 3081
SERVICE_UIC_M_MSGNAME = 3082
SERVICE_UIC_M_ANNOUNCE = 3083
SERVICE_UIC_M_UAS = 3084
SERVICE_UIC_M_SERVER_SEC_ERR = 3085
SERVICE_UIC_M_WKSTA = 3087
SERVICE_UIC_M_ERRLOG = 3088
SERVICE_UIC_M_FILE_UW = 3089
SERVICE_UIC_M_ADDPAK = 3090
SERVICE_UIC_M_LAZY = 3091
SERVICE_UIC_M_UAS_MACHINE_ACCT = 3092
SERVICE_UIC_M_UAS_SERVERS_NMEMB = 3093
SERVICE_UIC_M_UAS_SERVERS_NOGRP = 3094
SERVICE_UIC_M_UAS_INVALID_ROLE = 3095
SERVICE_UIC_M_NETLOGON_NO_DC = 3096
SERVICE_UIC_M_NETLOGON_DC_CFLCT = 3097
SERVICE_UIC_M_NETLOGON_AUTH = 3098
SERVICE_UIC_M_UAS_PROLOG = 3099
SERVICE2_BASE = 5600
SERVICE_UIC_M_NETLOGON_MPATH = 5600
SERVICE_UIC_M_LSA_MACHINE_ACCT = 5601
SERVICE_UIC_M_DATABASE_ERROR = 5602
USE_FLAG_GLOBAL_MAPPING = 65536
USE_LOCAL_PARMNUM = 1
USE_REMOTE_PARMNUM = 2
USE_PASSWORD_PARMNUM = 3
USE_ASGTYPE_PARMNUM = 4
USE_USERNAME_PARMNUM = 5
USE_DOMAINNAME_PARMNUM = 6
USE_FLAGS_PARMNUM = 7
USE_AUTHIDENTITY_PARMNUM = 8
USE_SD_PARMNUM = 9
USE_OPTIONS_PARMNUM = 10
USE_OK = 0
USE_PAUSED = 1
USE_SESSLOST = 2
USE_DISCONN = 2
USE_NETERR = 3
USE_CONN = 4
USE_RECONN = 5
USE_CHARDEV = 2
CREATE_NO_CONNECT = 1
CREATE_BYPASS_CSC = 2
CREATE_CRED_RESET = 4
USE_DEFAULT_CREDENTIALS = 4
CREATE_REQUIRE_CONNECTION_INTEGRITY = 8
CREATE_REQUIRE_CONNECTION_PRIVACY = 16
CREATE_PERSIST_MAPPING = 32
CREATE_WRITE_THROUGH_SEMANTICS = 64
CREATE_GLOBAL_MAPPING = 256
WKSTA_PLATFORM_ID_PARMNUM = 100
WKSTA_COMPUTERNAME_PARMNUM = 1
WKSTA_LANGROUP_PARMNUM = 2
WKSTA_VER_MAJOR_PARMNUM = 4
WKSTA_VER_MINOR_PARMNUM = 5
WKSTA_LOGGED_ON_USERS_PARMNUM = 6
WKSTA_LANROOT_PARMNUM = 7
WKSTA_LOGON_DOMAIN_PARMNUM = 8
WKSTA_LOGON_SERVER_PARMNUM = 9
WKSTA_CHARWAIT_PARMNUM = 10
WKSTA_CHARTIME_PARMNUM = 11
WKSTA_CHARCOUNT_PARMNUM = 12
WKSTA_KEEPCONN_PARMNUM = 13
WKSTA_KEEPSEARCH_PARMNUM = 14
WKSTA_MAXCMDS_PARMNUM = 15
WKSTA_NUMWORKBUF_PARMNUM = 16
WKSTA_MAXWRKCACHE_PARMNUM = 17
WKSTA_SESSTIMEOUT_PARMNUM = 18
WKSTA_SIZERROR_PARMNUM = 19
WKSTA_NUMALERTS_PARMNUM = 20
WKSTA_NUMSERVICES_PARMNUM = 21
WKSTA_NUMCHARBUF_PARMNUM = 22
WKSTA_SIZCHARBUF_PARMNUM = 23
WKSTA_ERRLOGSZ_PARMNUM = 27
WKSTA_PRINTBUFTIME_PARMNUM = 28
WKSTA_SIZWORKBUF_PARMNUM = 29
WKSTA_MAILSLOTS_PARMNUM = 30
WKSTA_NUMDGRAMBUF_PARMNUM = 31
WKSTA_WRKHEURISTICS_PARMNUM = 32
WKSTA_MAXTHREADS_PARMNUM = 33
WKSTA_LOCKQUOTA_PARMNUM = 41
WKSTA_LOCKINCREMENT_PARMNUM = 42
WKSTA_LOCKMAXIMUM_PARMNUM = 43
WKSTA_PIPEINCREMENT_PARMNUM = 44
WKSTA_PIPEMAXIMUM_PARMNUM = 45
WKSTA_DORMANTFILELIMIT_PARMNUM = 46
WKSTA_CACHEFILETIMEOUT_PARMNUM = 47
WKSTA_USEOPPORTUNISTICLOCKING_PARMNUM = 48
WKSTA_USEUNLOCKBEHIND_PARMNUM = 49
WKSTA_USECLOSEBEHIND_PARMNUM = 50
WKSTA_BUFFERNAMEDPIPES_PARMNUM = 51
WKSTA_USELOCKANDREADANDUNLOCK_PARMNUM = 52
WKSTA_UTILIZENTCACHING_PARMNUM = 53
WKSTA_USERAWREAD_PARMNUM = 54
WKSTA_USERAWWRITE_PARMNUM = 55
WKSTA_USEWRITERAWWITHDATA_PARMNUM = 56
WKSTA_USEENCRYPTION_PARMNUM = 57
WKSTA_BUFFILESWITHDENYWRITE_PARMNUM = 58
WKSTA_BUFFERREADONLYFILES_PARMNUM = 59
WKSTA_FORCECORECREATEMODE_PARMNUM = 60
WKSTA_USE512BYTESMAXTRANSFER_PARMNUM = 61
WKSTA_READAHEADTHRUPUT_PARMNUM = 62
WKSTA_OTH_DOMAINS_PARMNUM = 101
TRANSPORT_QUALITYOFSERVICE_PARMNUM = 201
TRANSPORT_NAME_PARMNUM = 202
EVENT_SRV_SERVICE_FAILED = -1073739824
EVENT_SRV_RESOURCE_SHORTAGE = -1073739823
EVENT_SRV_CANT_CREATE_DEVICE = -1073739822
EVENT_SRV_CANT_CREATE_PROCESS = -1073739821
EVENT_SRV_CANT_CREATE_THREAD = -1073739820
EVENT_SRV_UNEXPECTED_DISC = -1073739819
EVENT_SRV_INVALID_REQUEST = -1073739818
EVENT_SRV_CANT_OPEN_NPFS = -1073739817
EVENT_SRV_CANT_GROW_TABLE = -2147481639
EVENT_SRV_CANT_START_SCAVENGER = -1073739814
EVENT_SRV_IRP_STACK_SIZE = -1073739813
EVENT_SRV_NETWORK_ERROR = -2147481636
EVENT_SRV_DISK_FULL = -2147481635
EVENT_SRV_NO_VIRTUAL_MEMORY = -1073739808
EVENT_SRV_NONPAGED_POOL_LIMIT = -1073739807
EVENT_SRV_PAGED_POOL_LIMIT = -1073739806
EVENT_SRV_NO_NONPAGED_POOL = -1073739805
EVENT_SRV_NO_PAGED_POOL = -1073739804
EVENT_SRV_NO_WORK_ITEM = -2147481627
EVENT_SRV_NO_FREE_CONNECTIONS = -2147481626
EVENT_SRV_NO_FREE_RAW_WORK_ITEM = -2147481625
EVENT_SRV_NO_BLOCKING_IO = -2147481624
EVENT_SRV_DOS_ATTACK_DETECTED = -2147481623
EVENT_SRV_TOO_MANY_DOS = -2147481622
EVENT_SRV_OUT_OF_WORK_ITEM_DOS = -2147481621
EVENT_SRV_KEY_NOT_FOUND = -1073739323
EVENT_SRV_KEY_NOT_CREATED = -1073739322
EVENT_SRV_NO_TRANSPORTS_BOUND = -1073739321
EVENT_SRV_CANT_BIND_TO_TRANSPORT = -2147481144
EVENT_SRV_CANT_BIND_DUP_NAME = -1073739319
EVENT_SRV_INVALID_REGISTRY_VALUE = -2147481142
EVENT_SRV_INVALID_SD = -2147481141
EVENT_SRV_CANT_LOAD_DRIVER = -2147481140
EVENT_SRV_CANT_UNLOAD_DRIVER = -2147481139
EVENT_SRV_CANT_MAP_ERROR = -2147481138
EVENT_SRV_CANT_RECREATE_SHARE = -2147481137
EVENT_SRV_CANT_CHANGE_DOMAIN_NAME = -2147481136
EVENT_SRV_TXF_INIT_FAILED = -2147481135
EVENT_RDR_RESOURCE_SHORTAGE = -2147480647
EVENT_RDR_CANT_CREATE_DEVICE = -2147480646
EVENT_RDR_CANT_CREATE_THREAD = -2147480645
EVENT_RDR_CANT_SET_THREAD = -2147480644
EVENT_RDR_INVALID_REPLY = -2147480643
EVENT_RDR_INVALID_SMB = -2147480642
EVENT_RDR_INVALID_LOCK_REPLY = -2147480641
EVENT_RDR_FAILED_UNLOCK = -2147480639
EVENT_RDR_CLOSE_BEHIND = -2147480637
EVENT_RDR_UNEXPECTED_ERROR = -2147480636
EVENT_RDR_TIMEOUT = -2147480635
EVENT_RDR_INVALID_OPLOCK = -2147480634
EVENT_RDR_CONNECTION_REFERENCE = -2147480633
EVENT_RDR_SERVER_REFERENCE = -2147480632
EVENT_RDR_SMB_REFERENCE = -2147480631
EVENT_RDR_ENCRYPT = -2147480630
EVENT_RDR_CONNECTION = -2147480629
EVENT_RDR_MAXCMDS = -2147480627
EVENT_RDR_OPLOCK_SMB = -2147480626
EVENT_RDR_DISPOSITION = -2147480625
EVENT_RDR_CONTEXTS = -2147480624
EVENT_RDR_WRITE_BEHIND_FLUSH_FAILED = -2147480623
EVENT_RDR_AT_THREAD_MAX = -2147480622
EVENT_RDR_CANT_READ_REGISTRY = -2147480621
EVENT_RDR_TIMEZONE_BIAS_TOO_LARGE = -2147480620
EVENT_RDR_PRIMARY_TRANSPORT_CONNECT_FAILED = -2147480619
EVENT_RDR_DELAYED_SET_ATTRIBUTES_FAILED = -2147480618
EVENT_RDR_DELETEONCLOSE_FAILED = -2147480617
EVENT_RDR_CANT_BIND_TRANSPORT = -2147480616
EVENT_RDR_CANT_REGISTER_ADDRESS = -2147480615
EVENT_RDR_CANT_GET_SECURITY_CONTEXT = -2147480614
EVENT_RDR_CANT_BUILD_SMB_HEADER = -2147480613
EVENT_RDR_SECURITY_SIGNATURE_MISMATCH = -2147480612
EVENT_TCPIP6_STARTED = 1073744924
EVENT_STREAMS_STRLOG = -1073737824
EVENT_STREAMS_ALLOCB_FAILURE = -2147479647
EVENT_STREAMS_ALLOCB_FAILURE_CNT = -2147479646
EVENT_STREAMS_ESBALLOC_FAILURE = -2147479645
EVENT_STREAMS_ESBALLOC_FAILURE_CNT = -2147479644
EVENT_TCPIP_CREATE_DEVICE_FAILED = -1073737724
EVENT_TCPIP_NO_RESOURCES_FOR_INIT = -1073737723
EVENT_TCPIP_TOO_MANY_NETS = -1073737639
EVENT_TCPIP_NO_MASK = -1073737638
EVENT_TCPIP_INVALID_ADDRESS = -1073737637
EVENT_TCPIP_INVALID_MASK = -1073737636
EVENT_TCPIP_NO_ADAPTER_RESOURCES = -1073737635
EVENT_TCPIP_DHCP_INIT_FAILED = -2147479458
EVENT_TCPIP_ADAPTER_REG_FAILURE = -1073737633
EVENT_TCPIP_INVALID_DEFAULT_GATEWAY = -2147479456
EVENT_TCPIP_NO_ADDRESS_LIST = -1073737631
EVENT_TCPIP_NO_MASK_LIST = -1073737630
EVENT_TCPIP_NO_BINDINGS = -1073737629
EVENT_TCPIP_IP_INIT_FAILED = -1073737628
EVENT_TCPIP_TOO_MANY_GATEWAYS = -2147479451
EVENT_TCPIP_ADDRESS_CONFLICT1 = -1073737626
EVENT_TCPIP_ADDRESS_CONFLICT2 = -1073737625
EVENT_TCPIP_NTE_CONTEXT_LIST_FAILURE = -1073737624
EVENT_TCPIP_MEDIA_CONNECT = 1073746025
EVENT_TCPIP_MEDIA_DISCONNECT = 1073746026
EVENT_TCPIP_IPV4_UNINSTALLED = 1073746027
EVENT_TCPIP_AUTOCONFIGURED_ADDRESS_LIMIT_REACHED = -2147479444
EVENT_TCPIP_AUTOCONFIGURED_ROUTE_LIMIT_REACHED = -2147479443
EVENT_TCPIP_OUT_OF_ORDER_FRAGMENTS_EXCEEDED = -2147479442
EVENT_TCPIP_INTERFACE_BIND_FAILURE = -1073737617
EVENT_TCPIP_TCP_INIT_FAILED = -1073737599
EVENT_TCPIP_TCP_CONNECT_LIMIT_REACHED = -2147479422
EVENT_TCPIP_TCP_TIME_WAIT_COLLISION = -2147479421
EVENT_TCPIP_TCP_WSD_WS_RESTRICTED = -2147479420
EVENT_TCPIP_TCP_MPP_ATTACKS_DETECTED = -2147479419
EVENT_TCPIP_TCP_CONNECTIONS_PERF_IMPACTED = -2147479418
EVENT_TCPIP_TCP_GLOBAL_EPHEMERAL_PORT_SPACE_EXHAUSTED = -2147479417
EVENT_TCPIP_UDP_LIMIT_REACHED = -2147479383
EVENT_TCPIP_UDP_GLOBAL_EPHEMERAL_PORT_SPACE_EXHAUSTED = -2147479382
EVENT_TCPIP_PCF_MULTICAST_OID_ISSUE = -2147479358
EVENT_TCPIP_PCF_MISSING_CAPABILITY = -2147479357
EVENT_TCPIP_PCF_SET_FILTER_FAILURE = -2147479356
EVENT_TCPIP_PCF_NO_ARP_FILTER = -2147479355
EVENT_TCPIP_PCF_CLEAR_FILTER_FAILURE = -1073737530
EVENT_NBT_CREATE_DRIVER = -1073737524
EVENT_NBT_OPEN_REG_PARAMS = -1073737523
EVENT_NBT_NO_BACKUP_WINS = -2147479346
EVENT_NBT_NO_WINS = -2147479345
EVENT_NBT_BAD_BACKUP_WINS_ADDR = -2147479344
EVENT_NBT_BAD_PRIMARY_WINS_ADDR = -2147479343
EVENT_NBT_NAME_SERVER_ADDRS = -1073737518
EVENT_NBT_CREATE_ADDRESS = -1073737517
EVENT_NBT_CREATE_CONNECTION = -1073737516
EVENT_NBT_NON_OS_INIT = -1073737515
EVENT_NBT_TIMERS = -1073737514
EVENT_NBT_CREATE_DEVICE = -1073737513
EVENT_NBT_NO_DEVICES = -2147479336
EVENT_NBT_OPEN_REG_LINKAGE = -1073737511
EVENT_NBT_READ_BIND = -1073737510
EVENT_NBT_READ_EXPORT = -1073737509
EVENT_NBT_OPEN_REG_NAMESERVER = -2147479332
EVENT_SCOPE_LABEL_TOO_LONG = -2147479331
EVENT_SCOPE_TOO_LONG = -2147479330
EVENT_NBT_DUPLICATE_NAME = -1073737505
EVENT_NBT_NAME_RELEASE = -1073737504
EVENT_NBT_DUPLICATE_NAME_ERROR = -1073737503
EVENT_NBT_NO_RESOURCES = -1073737502
EVENT_NDIS_RESOURCE_CONFLICT = -1073736824
EVENT_NDIS_OUT_OF_RESOURCE = -1073736823
EVENT_NDIS_HARDWARE_FAILURE = -1073736822
EVENT_NDIS_ADAPTER_NOT_FOUND = -1073736821
EVENT_NDIS_INTERRUPT_CONNECT = -1073736820
EVENT_NDIS_DRIVER_FAILURE = -1073736819
EVENT_NDIS_BAD_VERSION = -1073736818
EVENT_NDIS_TIMEOUT = -2147478641
EVENT_NDIS_NETWORK_ADDRESS = -1073736816
EVENT_NDIS_UNSUPPORTED_CONFIGURATION = -1073736815
EVENT_NDIS_INVALID_VALUE_FROM_ADAPTER = -1073736814
EVENT_NDIS_MISSING_CONFIGURATION_PARAMETER = -1073736813
EVENT_NDIS_BAD_IO_BASE_ADDRESS = -1073736812
EVENT_NDIS_RECEIVE_SPACE_SMALL = 1073746837
EVENT_NDIS_ADAPTER_DISABLED = -2147478634
EVENT_NDIS_IO_PORT_CONFLICT = -2147478633
EVENT_NDIS_PORT_OR_DMA_CONFLICT = -2147478632
EVENT_NDIS_MEMORY_CONFLICT = -2147478631
EVENT_NDIS_INTERRUPT_CONFLICT = -2147478630
EVENT_NDIS_DMA_CONFLICT = -2147478629
EVENT_NDIS_INVALID_DOWNLOAD_FILE_ERROR = -1073736804
EVENT_NDIS_MAXRECEIVES_ERROR = -2147478627
EVENT_NDIS_MAXTRANSMITS_ERROR = -2147478626
EVENT_NDIS_MAXFRAMESIZE_ERROR = -2147478625
EVENT_NDIS_MAXINTERNALBUFS_ERROR = -2147478624
EVENT_NDIS_MAXMULTICAST_ERROR = -2147478623
EVENT_NDIS_PRODUCTID_ERROR = -2147478622
EVENT_NDIS_LOBE_FAILUE_ERROR = -2147478621
EVENT_NDIS_SIGNAL_LOSS_ERROR = -2147478620
EVENT_NDIS_REMOVE_RECEIVED_ERROR = -2147478619
EVENT_NDIS_TOKEN_RING_CORRECTION = 1073746854
EVENT_NDIS_ADAPTER_CHECK_ERROR = -1073736793
EVENT_NDIS_RESET_FAILURE_ERROR = -2147478616
EVENT_NDIS_CABLE_DISCONNECTED_ERROR = -2147478615
EVENT_NDIS_RESET_FAILURE_CORRECTION = -2147478614
EVENT_EventlogStarted = -2147477643
EVENT_EventlogStopped = -2147477642
EVENT_EventlogAbnormalShutdown = -2147477640
EVENT_EventLogProductInfo = -2147477639
EVENT_ComputerNameChange = -2147477637
EVENT_DNSDomainNameChange = -2147477636
EVENT_EventlogUptime = -2147477635
EVENT_UP_DRIVER_ON_MP = -1073735724
EVENT_SERVICE_START_FAILED = -1073734824
EVENT_SERVICE_START_FAILED_II = -1073734823
EVENT_SERVICE_START_FAILED_GROUP = -1073734822
EVENT_SERVICE_START_FAILED_NONE = -1073734821
EVENT_CALL_TO_FUNCTION_FAILED = -1073734819
EVENT_CALL_TO_FUNCTION_FAILED_II = -1073734818
EVENT_REVERTED_TO_LASTKNOWNGOOD = -1073734817
EVENT_BAD_ACCOUNT_NAME = -1073734816
EVENT_CONNECTION_TIMEOUT = -1073734815
EVENT_READFILE_TIMEOUT = -1073734814
EVENT_TRANSACT_TIMEOUT = -1073734813
EVENT_TRANSACT_INVALID = -1073734812
EVENT_FIRST_LOGON_FAILED = -1073734811
EVENT_SECOND_LOGON_FAILED = -1073734810
EVENT_INVALID_DRIVER_DEPENDENCY = -1073734809
EVENT_BAD_SERVICE_STATE = -1073734808
EVENT_CIRCULAR_DEPENDENCY_DEMAND = -1073734807
EVENT_CIRCULAR_DEPENDENCY_AUTO = -1073734806
EVENT_DEPEND_ON_LATER_SERVICE = -1073734805
EVENT_DEPEND_ON_LATER_GROUP = -1073734804
EVENT_SEVERE_SERVICE_FAILED = -1073734803
EVENT_SERVICE_START_HUNG = -1073734802
EVENT_SERVICE_EXIT_FAILED = -1073734801
EVENT_SERVICE_EXIT_FAILED_SPECIFIC = -1073734800
EVENT_SERVICE_START_AT_BOOT_FAILED = -1073734799
EVENT_BOOT_SYSTEM_DRIVERS_FAILED = -1073734798
EVENT_RUNNING_LASTKNOWNGOOD = -1073734797
EVENT_TAKE_OWNERSHIP = -1073734796
TITLE_SC_MESSAGE_BOX = -1073734795
EVENT_SERVICE_NOT_INTERACTIVE = -1073734794
EVENT_SERVICE_CRASH = -1073734793
EVENT_SERVICE_RECOVERY_FAILED = -1073734792
EVENT_SERVICE_SCESRV_FAILED = -1073734791
EVENT_SERVICE_CRASH_NO_ACTION = -1073734790
EVENT_SERVICE_CONTROL_SUCCESS = 1073748859
EVENT_SERVICE_STATUS_SUCCESS = 1073748860
EVENT_SERVICE_CONFIG_BACKOUT_FAILED = -1073734787
EVENT_FIRST_LOGON_FAILED_II = -1073734786
EVENT_SERVICE_DIFFERENT_PID_CONNECTED = -2147476609
EVENT_SERVICE_START_TYPE_CHANGED = 1073748864
EVENT_SERVICE_LOGON_TYPE_NOT_GRANTED = -1073734783
EVENT_SERVICE_STOP_SUCCESS_WITH_REASON = 1073748866
EVENT_SERVICE_SHUTDOWN_FAILED = -1073734781
EVENT_COMMAND_NOT_INTERACTIVE = -1073733924
EVENT_COMMAND_START_FAILED = -1073733923
EVENT_BOWSER_OTHER_MASTER_ON_NET = -1073733821
EVENT_BOWSER_PROMOTED_WHILE_ALREADY_MASTER = -2147475644
EVENT_BOWSER_NON_MASTER_MASTER_ANNOUNCE = -2147475643
EVENT_BOWSER_ILLEGAL_DATAGRAM = -2147475642
EVENT_BROWSER_STATUS_BITS_UPDATE_FAILED = -1073733817
EVENT_BROWSER_ROLE_CHANGE_FAILED = -1073733816
EVENT_BROWSER_MASTER_PROMOTION_FAILED = -1073733815
EVENT_BOWSER_NAME_CONVERSION_FAILED = -1073733814
EVENT_BROWSER_OTHERDOMAIN_ADD_FAILED = -1073733813
EVENT_BOWSER_ELECTION_RECEIVED = 8012
EVENT_BOWSER_ELECTION_SENT_GETBLIST_FAILED = 1073749837
EVENT_BOWSER_ELECTION_SENT_FIND_MASTER_FAILED = 1073749838
EVENT_BROWSER_ELECTION_SENT_LANMAN_NT_STARTED = 1073749839
EVENT_BOWSER_ILLEGAL_DATAGRAM_THRESHOLD = -1073733808
EVENT_BROWSER_DEPENDANT_SERVICE_FAILED = -1073733807
EVENT_BROWSER_MASTER_PROMOTION_FAILED_STOPPING = -1073733805
EVENT_BROWSER_MASTER_PROMOTION_FAILED_NO_MASTER = -1073733804
EVENT_BROWSER_SERVER_LIST_FAILED = -2147475627
EVENT_BROWSER_DOMAIN_LIST_FAILED = -2147475626
EVENT_BROWSER_ILLEGAL_CONFIG = -2147475625
EVENT_BOWSER_OLD_BACKUP_FOUND = 1073749848
EVENT_BROWSER_SERVER_LIST_RETRIEVED = 8025
EVENT_BROWSER_DOMAIN_LIST_RETRIEVED = 8026
EVENT_BOWSER_PDC_LOST_ELECTION = 1073749851
EVENT_BOWSER_NON_PDC_WON_ELECTION = 1073749852
EVENT_BOWSER_CANT_READ_REGISTRY = 1073749853
EVENT_BOWSER_MAILSLOT_DATAGRAM_THRESHOLD_EXCEEDED = 1073749854
EVENT_BOWSER_GETBROWSERLIST_THRESHOLD_EXCEEDED = 1073749855
EVENT_BROWSER_BACKUP_STOPPED = -1073733792
EVENT_BROWSER_ELECTION_SENT_LANMAN_NT_STOPPED = 1073749857
EVENT_BROWSER_GETBLIST_RECEIVED_NOT_MASTER = -1073733790
EVENT_BROWSER_ELECTION_SENT_ROLE_CHANGED = 1073749859
EVENT_BROWSER_NOT_STARTED_IPX_CONFIG_MISMATCH = -1073733788
NWSAP_EVENT_KEY_NOT_FOUND = -1073733324
NWSAP_EVENT_WSASTARTUP_FAILED = -1073733323
NWSAP_EVENT_SOCKET_FAILED = -1073733322
NWSAP_EVENT_SETOPTBCAST_FAILED = -1073733321
NWSAP_EVENT_BIND_FAILED = -1073733320
NWSAP_EVENT_GETSOCKNAME_FAILED = -1073733319
NWSAP_EVENT_OPTEXTENDEDADDR_FAILED = -1073733318
NWSAP_EVENT_OPTBCASTINADDR_FAILED = -1073733317
NWSAP_EVENT_CARDMALLOC_FAILED = -1073733316
NWSAP_EVENT_NOCARDS = -1073733315
NWSAP_EVENT_THREADEVENT_FAIL = -1073733314
NWSAP_EVENT_RECVSEM_FAIL = -1073733313
NWSAP_EVENT_SENDEVENT_FAIL = -1073733312
NWSAP_EVENT_STARTRECEIVE_ERROR = -1073733311
NWSAP_EVENT_STARTWORKER_ERROR = -1073733310
NWSAP_EVENT_TABLE_MALLOC_FAILED = -1073733309
NWSAP_EVENT_HASHTABLE_MALLOC_FAILED = -1073733308
NWSAP_EVENT_STARTLPCWORKER_ERROR = -1073733307
NWSAP_EVENT_CREATELPCPORT_ERROR = -1073733306
NWSAP_EVENT_CREATELPCEVENT_ERROR = -1073733305
NWSAP_EVENT_LPCLISTENMEMORY_ERROR = -1073733304
NWSAP_EVENT_LPCHANDLEMEMORY_ERROR = -1073733303
NWSAP_EVENT_BADWANFILTER_VALUE = -1073733302
NWSAP_EVENT_CARDLISTEVENT_FAIL = -1073733301
NWSAP_EVENT_SDMDEVENT_FAIL = -1073733300
NWSAP_EVENT_INVALID_FILTERNAME = -2147475123
NWSAP_EVENT_WANSEM_FAIL = -1073733298
NWSAP_EVENT_WANSOCKET_FAILED = -1073733297
NWSAP_EVENT_WANBIND_FAILED = -1073733296
NWSAP_EVENT_STARTWANWORKER_ERROR = -1073733295
NWSAP_EVENT_STARTWANCHECK_ERROR = -1073733294
NWSAP_EVENT_OPTMAXADAPTERNUM_ERROR = -1073733293
NWSAP_EVENT_WANHANDLEMEMORY_ERROR = -1073733292
NWSAP_EVENT_WANEVENT_ERROR = -1073733291
EVENT_TRANSPORT_RESOURCE_POOL = -2147474647
EVENT_TRANSPORT_RESOURCE_LIMIT = -2147474646
EVENT_TRANSPORT_RESOURCE_SPECIFIC = -2147474645
EVENT_TRANSPORT_REGISTER_FAILED = -1073732820
EVENT_TRANSPORT_BINDING_FAILED = -1073732819
EVENT_TRANSPORT_ADAPTER_NOT_FOUND = -1073732818
EVENT_TRANSPORT_SET_OID_FAILED = -1073732817
EVENT_TRANSPORT_QUERY_OID_FAILED = -1073732816
EVENT_TRANSPORT_TRANSFER_DATA = 1073750833
EVENT_TRANSPORT_TOO_MANY_LINKS = 1073750834
EVENT_TRANSPORT_BAD_PROTOCOL = 1073750835
EVENT_IPX_NEW_DEFAULT_TYPE = 1073751325
EVENT_IPX_SAP_ANNOUNCE = -2147474146
EVENT_IPX_ILLEGAL_CONFIG = -2147474145
EVENT_IPX_INTERNAL_NET_INVALID = -1073732320
EVENT_IPX_NO_FRAME_TYPES = -1073732319
EVENT_IPX_CREATE_DEVICE = -1073732318
EVENT_IPX_NO_ADAPTERS = -1073732317
EVENT_RPCSS_CREATEPROCESS_FAILURE = -1073731824
EVENT_RPCSS_RUNAS_CREATEPROCESS_FAILURE = -1073731823
EVENT_RPCSS_LAUNCH_ACCESS_DENIED = -1073731822
EVENT_RPCSS_DEFAULT_LAUNCH_ACCESS_DENIED = -1073731821
EVENT_RPCSS_RUNAS_CANT_LOGIN = -1073731820
EVENT_RPCSS_START_SERVICE_FAILURE = -1073731819
EVENT_RPCSS_REMOTE_SIDE_ERROR = -1073731818
EVENT_RPCSS_ACTIVATION_ERROR = -1073731817
EVENT_RPCSS_REMOTE_SIDE_ERROR_WITH_FILE = -1073731816
EVENT_RPCSS_REMOTE_SIDE_UNAVAILABLE = -1073731815
EVENT_RPCSS_SERVER_START_TIMEOUT = -1073731814
EVENT_RPCSS_SERVER_NOT_RESPONDING = -1073731813
EVENT_DCOM_ASSERTION_FAILURE = -1073731812
EVENT_DCOM_INVALID_ENDPOINT_DATA = -1073731811
EVENT_DCOM_COMPLUS_DISABLED = -1073731810
EVENT_RPCSS_STOP_SERVICE_FAILURE = -1073731795
EVENT_RPCSS_CREATEDEBUGGERPROCESS_FAILURE = -1073731794
EVENT_DNS_CACHE_START_FAILURE_NO_DLL = -1073730824
EVENT_DNS_CACHE_START_FAILURE_NO_ENTRY = -1073730823
EVENT_DNS_CACHE_START_FAILURE_NO_CONTROL = -1073730822
EVENT_DNS_CACHE_START_FAILURE_NO_DONE_EVENT = -1073730821
EVENT_DNS_CACHE_START_FAILURE_NO_RPC = -1073730820
EVENT_DNS_CACHE_START_FAILURE_NO_SHUTDOWN_NOTIFY = -1073730819
EVENT_DNS_CACHE_START_FAILURE_NO_UPDATE = -1073730818
EVENT_DNS_CACHE_START_FAILURE_LOW_MEMORY = -1073730817
EVENT_DNS_CACHE_NETWORK_PERF_WARNING = -2147472598
EVENT_DNS_CACHE_UNABLE_TO_REACH_SERVER_WARNING = -2147472597
EVENT_DNSAPI_REGISTRATION_FAILED_TIMEOUT = -2147472498
EVENT_DNSAPI_REGISTRATION_FAILED_SERVERFAIL = -2147472497
EVENT_DNSAPI_REGISTRATION_FAILED_NOTSUPP = -2147472496
EVENT_DNSAPI_REGISTRATION_FAILED_REFUSED = -2147472495
EVENT_DNSAPI_REGISTRATION_FAILED_SECURITY = -2147472494
EVENT_DNSAPI_REGISTRATION_FAILED_OTHER = -2147472493
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_TIMEOUT = -2147472492
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_SERVERFAIL = -2147472491
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_NOTSUPP = -2147472490
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_REFUSED = -2147472489
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_SECURITY = -2147472488
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_OTHER = -2147472487
EVENT_DNSAPI_REGISTRATION_FAILED_TIMEOUT_PRIMARY_DN = -2147472486
EVENT_DNSAPI_REGISTRATION_FAILED_SERVERFAIL_PRIMARY_DN = -2147472485
EVENT_DNSAPI_REGISTRATION_FAILED_NOTSUPP_PRIMARY_DN = -2147472484
EVENT_DNSAPI_REGISTRATION_FAILED_REFUSED_PRIMARY_DN = -2147472483
EVENT_DNSAPI_REGISTRATION_FAILED_SECURITY_PRIMARY_DN = -2147472482
EVENT_DNSAPI_REGISTRATION_FAILED_OTHER_PRIMARY_DN = -2147472481
EVENT_DNSAPI_DEREGISTRATION_FAILED_TIMEOUT = -2147472468
EVENT_DNSAPI_DEREGISTRATION_FAILED_SERVERFAIL = -2147472467
EVENT_DNSAPI_DEREGISTRATION_FAILED_NOTSUPP = -2147472466
EVENT_DNSAPI_DEREGISTRATION_FAILED_REFUSED = -2147472465
EVENT_DNSAPI_DEREGISTRATION_FAILED_SECURITY = -2147472464
EVENT_DNSAPI_DEREGISTRATION_FAILED_OTHER = -2147472463
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_TIMEOUT = -2147472462
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_SERVERFAIL = -2147472461
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_NOTSUPP = -2147472460
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_REFUSED = -2147472459
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_SECURITY = -2147472458
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_OTHER = -2147472457
EVENT_DNSAPI_DEREGISTRATION_FAILED_TIMEOUT_PRIMARY_DN = -2147472456
EVENT_DNSAPI_DEREGISTRATION_FAILED_SERVERFAIL_PRIMARY_DN = -2147472455
EVENT_DNSAPI_DEREGISTRATION_FAILED_NOTSUPP_PRIMARY_DN = -2147472454
EVENT_DNSAPI_DEREGISTRATION_FAILED_REFUSED_PRIMARY_DN = -2147472453
EVENT_DNSAPI_DEREGISTRATION_FAILED_SECURITY_PRIMARY_DN = -2147472452
EVENT_DNSAPI_DEREGISTRATION_FAILED_OTHER_PRIMARY_DN = -2147472451
EVENT_DNSAPI_REGISTERED_ADAPTER = 1073753024
EVENT_DNSAPI_REGISTERED_PTR = 1073753025
EVENT_DNSAPI_REGISTERED_ADAPTER_PRIMARY_DN = 1073753026
EVENT_TRK_INTERNAL_ERROR = -1073729324
EVENT_TRK_SERVICE_START_SUCCESS = 1073754325
EVENT_TRK_SERVICE_START_FAILURE = -1073729322
EVENT_TRK_SERVICE_CORRUPT_LOG = -1073729321
EVENT_TRK_SERVICE_VOL_QUOTA_EXCEEDED = -2147471144
EVENT_TRK_SERVICE_VOLUME_CREATE = 1073754329
EVENT_TRK_SERVICE_VOLUME_CLAIM = 1073754330
EVENT_TRK_SERVICE_DUPLICATE_VOLIDS = 1073754331
EVENT_TRK_SERVICE_MOVE_QUOTA_EXCEEDED = -2147471140
EVENT_FRS_ERROR = -1073728324
EVENT_FRS_STARTING = 1073755325
EVENT_FRS_STOPPING = 1073755326
EVENT_FRS_STOPPED = 1073755327
EVENT_FRS_STOPPED_FORCE = -1073728320
EVENT_FRS_STOPPED_ASSERT = -1073728319
EVENT_FRS_ASSERT = -1073728318
EVENT_FRS_VOLUME_NOT_SUPPORTED = -1073728317
EVENT_FRS_LONG_JOIN = -2147470140
EVENT_FRS_LONG_JOIN_DONE = -2147470139
EVENT_FRS_CANNOT_COMMUNICATE = -1073728314
EVENT_FRS_DATABASE_SPACE = -1073728313
EVENT_FRS_DISK_WRITE_CACHE_ENABLED = -2147470136
EVENT_FRS_JET_1414 = -1073728311
EVENT_FRS_SYSVOL_NOT_READY = -2147470134
EVENT_FRS_SYSVOL_NOT_READY_PRIMARY = -2147470133
EVENT_FRS_SYSVOL_READY = 1073755340
EVENT_FRS_ACCESS_CHECKS_DISABLED = -2147470131
EVENT_FRS_ACCESS_CHECKS_FAILED_USER = -2147470130
EVENT_FRS_ACCESS_CHECKS_FAILED_UNKNOWN = -1073728305
EVENT_FRS_MOVED_PREEXISTING = -2147470128
EVENT_FRS_CANNOT_START_BACKUP_RESTORE_IN_PROGRESS = -1073728303
EVENT_FRS_STAGING_AREA_FULL = -2147470126
EVENT_FRS_HUGE_FILE = -2147470125
EVENT_FRS_CANNOT_CREATE_UUID = -1073728300
EVENT_FRS_NO_DNS_ATTRIBUTE = -2147470123
EVENT_FRS_NO_SID = -1073728298
NTFRSPRF_OPEN_RPC_BINDING_ERROR_SET = -1073728297
NTFRSPRF_OPEN_RPC_BINDING_ERROR_CONN = -1073728296
NTFRSPRF_OPEN_RPC_CALL_ERROR_SET = -1073728295
NTFRSPRF_OPEN_RPC_CALL_ERROR_CONN = -1073728294
NTFRSPRF_COLLECT_RPC_BINDING_ERROR_SET = -1073728293
NTFRSPRF_COLLECT_RPC_BINDING_ERROR_CONN = -1073728292
NTFRSPRF_COLLECT_RPC_CALL_ERROR_SET = -1073728291
NTFRSPRF_COLLECT_RPC_CALL_ERROR_CONN = -1073728290
NTFRSPRF_VIRTUALALLOC_ERROR_SET = -1073728289
NTFRSPRF_VIRTUALALLOC_ERROR_CONN = -1073728288
NTFRSPRF_REGISTRY_ERROR_SET = -1073728287
NTFRSPRF_REGISTRY_ERROR_CONN = -1073728286
EVENT_FRS_ROOT_NOT_VALID = -1073728285
EVENT_FRS_STAGE_NOT_VALID = -1073728284
EVENT_FRS_OVERLAPS_LOGGING = -1073728283
EVENT_FRS_OVERLAPS_WORKING = -1073728282
EVENT_FRS_OVERLAPS_STAGE = -1073728281
EVENT_FRS_OVERLAPS_ROOT = -1073728280
EVENT_FRS_OVERLAPS_OTHER_STAGE = -1073728279
EVENT_FRS_PREPARE_ROOT_FAILED = -1073728278
EVENT_FRS_BAD_REG_DATA = -2147470101
EVENT_FRS_JOIN_FAIL_TIME_SKEW = -1073728276
EVENT_FRS_RMTCO_TIME_SKEW = -1073728275
EVENT_FRS_CANT_OPEN_STAGE = -1073728274
EVENT_FRS_CANT_OPEN_PREINSTALL = -1073728273
EVENT_FRS_REPLICA_SET_CREATE_FAIL = -1073728272
EVENT_FRS_REPLICA_SET_CREATE_OK = 1073755377
EVENT_FRS_REPLICA_SET_CXTIONS = 1073755378
EVENT_FRS_IN_ERROR_STATE = -1073728269
EVENT_FRS_REPLICA_NO_ROOT_CHANGE = -1073728268
EVENT_FRS_DUPLICATE_IN_CXTION_SYSVOL = -1073728267
EVENT_FRS_DUPLICATE_IN_CXTION = -1073728266
EVENT_FRS_ROOT_HAS_MOVED = -1073728265
EVENT_FRS_ERROR_REPLICA_SET_DELETED = -2147470088
EVENT_FRS_REPLICA_IN_JRNL_WRAP_ERROR = -1073728263
EVENT_FRS_DS_POLL_ERROR_SUMMARY = -2147470086
EVENT_PS_GPC_REGISTER_FAILED = -1073727824
EVENT_PS_NO_RESOURCES_FOR_INIT = -1073727823
EVENT_PS_REGISTER_PROTOCOL_FAILED = -1073727822
EVENT_PS_REGISTER_MINIPORT_FAILED = -1073727821
EVENT_PS_BAD_BESTEFFORT_LIMIT = -2147469548
EVENT_PS_QUERY_OID_GEN_MAXIMUM_FRAME_SIZE = -1073727723
EVENT_PS_QUERY_OID_GEN_MAXIMUM_TOTAL_SIZE = -1073727722
EVENT_PS_QUERY_OID_GEN_LINK_SPEED = -1073727721
EVENT_PS_BINDING_FAILED = -1073727720
EVENT_PS_MISSING_ADAPTER_REGISTRY_DATA = -1073727719
EVENT_PS_REGISTER_ADDRESS_FAMILY_FAILED = -1073727718
EVENT_PS_INIT_DEVICE_FAILED = -1073727717
EVENT_PS_WMI_INSTANCE_NAME_FAILED = -1073727716
EVENT_PS_WAN_LIMITED_BESTEFFORT = -2147469539
EVENT_PS_RESOURCE_POOL = -1073727714
EVENT_PS_ADMISSIONCONTROL_OVERFLOW = -2147469537
EVENT_PS_NETWORK_ADDRESS_FAIL = -1073727712
EXTRA_EXIT_POINT = -1073727524
MISSING_EXIT_POINT = -1073727523
MISSING_VOLUME = -1073727522
EXTRA_VOLUME = -1073727521
EXTRA_EXIT_POINT_DELETED = -1073727520
EXTRA_EXIT_POINT_NOT_DELETED = -1073727519
MISSING_EXIT_POINT_CREATED = -1073727518
MISSING_EXIT_POINT_NOT_CREATED = -1073727517
MISSING_VOLUME_CREATED = -1073727516
MISSING_VOLUME_NOT_CREATED = -1073727515
EXTRA_VOLUME_DELETED = -1073727514
EXTRA_VOLUME_NOT_DELETED = -1073727513
COULD_NOT_VERIFY_VOLUMES = -1073727512
KNOWLEDGE_INCONSISTENCY_DETECTED = -1073727511
PREFIX_MISMATCH = -1073727510
PREFIX_MISMATCH_FIXED = -1073727509
PREFIX_MISMATCH_NOT_FIXED = -1073727508
MACHINE_UNJOINED = -1073727507
DFS_REFERRAL_REQUEST = 1073756142
NOT_A_DFS_PATH = 1073756224
LM_REDIR_FAILURE = 1073756225
DFS_CONNECTION_FAILURE = 1073756226
DFS_REFERRAL_FAILURE = 1073756227
DFS_REFERRAL_SUCCESS = 1073756228
DFS_MAX_DNR_ATTEMPTS = 1073756229
DFS_SPECIAL_REFERRAL_FAILURE = 1073756230
DFS_OPEN_FAILURE = 1073756231
NET_DFS_ENUM = 1073756324
NET_DFS_ENUMEX = 1073756325
DFS_ERROR_CREATE_REPARSEPOINT_FAILURE = -1073727321
DFS_ERROR_UNSUPPORTED_FILESYSTEM = -1073727320
DFS_ERROR_OVERLAPPING_DIRECTORIES = -1073727319
DFS_INFO_ACTIVEDIRECTORY_ONLINE = 1073756332
DFS_ERROR_TOO_MANY_ERRORS = -1073727315
DFS_ERROR_WINSOCKINIT_FAILED = -1073727314
DFS_ERROR_SECURITYINIT_FAILED = -1073727313
DFS_ERROR_THREADINIT_FAILED = -1073727312
DFS_ERROR_SITECACHEINIT_FAILED = -1073727311
DFS_ERROR_ROOTSYNCINIT_FAILED = -1073727310
DFS_ERROR_CREATEEVENT_FAILED = -1073727309
DFS_ERROR_COMPUTERINFO_FAILED = -1073727308
DFS_ERROR_CLUSTERINFO_FAILED = -1073727307
DFS_ERROR_DCINFO_FAILED = -1073727306
DFS_ERROR_PREFIXTABLE_FAILED = -1073727305
DFS_ERROR_HANDLENAMESPACE_FAILED = -1073727304
DFS_ERROR_REGISTERSTORE_FAILED = -1073727303
DFS_ERROR_REFLECTIONENGINE_FAILED = -1073727302
DFS_ERROR_ACTIVEDIRECTORY_OFFLINE = -1073727301
DFS_ERROR_SITESUPPOR_FAILED = -1073727300
DFS_ERROR_DSCONNECT_FAILED = -2147469122
DFS_INFO_DS_RECONNECTED = 1073756353
DFS_ERROR_NO_DFS_DATA = -1073727294
DFS_INFO_FINISH_INIT = 1073756355
DFS_INFO_RECONNECT_DATA = 1073756356
DFS_INFO_FINISH_BUILDING_NAMESPACE = 1073756357
DFS_ERROR_ON_ROOT = -2147469114
DFS_ERROR_MUTLIPLE_ROOTS_NOT_SUPPORTED = -1073727289
DFS_WARN_DOMAIN_REFERRAL_OVERFLOW = -2147469112
DFS_INFO_DOMAIN_REFERRAL_MIN_OVERFLOW = 1073756361
DFS_WARN_INCOMPLETE_MOVE = -2147469110
DFS_ERROR_RESYNCHRONIZE_FAILED = -1073727285
DFS_ERROR_REMOVE_LINK_FAILED = -1073727284
DFS_WARN_METADATA_LINK_TYPE_INCORRECT = -2147469107
DFS_WARN_METADATA_LINK_INFO_INVALID = -2147469106
DFS_ERROR_TARGET_LIST_INCORRECT = -1073727281
DFS_ERROR_LINKS_OVERLAP = -1073727280
DFS_ERROR_LINK_OVERLAP = -1073727279
DFS_ERROR_CREATE_REPARSEPOINT_SUCCESS = 1073756370
DFS_ERROR_DUPLICATE_LINK = -1073727277
DFS_ERROR_TRUSTED_DOMAIN_INFO_FAILED = -1073727276
DFS_INFO_TRUSTED_DOMAIN_INFO_SUCCESS = 1073756373
DFS_ERROR_CROSS_FOREST_TRUST_INFO_FAILED = -1073727274
DFS_INFO_CROSS_FOREST_TRUST_INFO_SUCCESS = 1073756375
DFS_INIT_SUCCESS = 1073756376
DFS_ROOT_SHARE_ACQUIRE_FAILED = -2147469095
DFS_ROOT_SHARE_ACQUIRE_SUCCESS = 1073756378
EVENT_BRIDGE_PROTOCOL_REGISTER_FAILED = -1073727224
EVENT_BRIDGE_MINIPROT_DEVNAME_MISSING = -1073727223
EVENT_BRIDGE_MINIPORT_REGISTER_FAILED = -1073727222
EVENT_BRIDGE_DEVICE_CREATION_FAILED = -1073727221
EVENT_BRIDGE_NO_BRIDGE_MAC_ADDR = -1073727220
EVENT_BRIDGE_MINIPORT_INIT_FAILED = -1073727219
EVENT_BRIDGE_ETHERNET_NOT_OFFERED = -1073727218
EVENT_BRIDGE_THREAD_CREATION_FAILED = -1073727217
EVENT_BRIDGE_THREAD_REF_FAILED = -1073727216
EVENT_BRIDGE_PACKET_POOL_CREATION_FAILED = -1073727215
EVENT_BRIDGE_BUFFER_POOL_CREATION_FAILED = -1073727214
EVENT_BRIDGE_INIT_MALLOC_FAILED = -1073727213
EVENT_BRIDGE_ADAPTER_LINK_SPEED_QUERY_FAILED = -1073727124
EVENT_BRIDGE_ADAPTER_MAC_ADDR_QUERY_FAILED = -1073727123
EVENT_BRIDGE_ADAPTER_FILTER_FAILED = -1073727122
EVENT_BRIDGE_ADAPTER_NAME_QUERY_FAILED = -1073727121
EVENT_BRIDGE_ADAPTER_BIND_FAILED = -1073727120
EVENT_DAV_REDIR_DELAYED_WRITE_FAILED = -2147468848
EVENT_WEBCLIENT_CLOSE_PUT_FAILED = -2147468747
EVENT_WEBCLIENT_CLOSE_DELETE_FAILED = -2147468746
EVENT_WEBCLIENT_CLOSE_PROPPATCH_FAILED = -2147468745
EVENT_WEBCLIENT_SETINFO_PROPPATCH_FAILED = -2147468744
EVENT_WSK_OWNINGTHREAD_PARAMETER_IGNORED = -1073725824
EVENT_WINSOCK_TDI_FILTER_DETECTED = -2147467647
EVENT_WINSOCK_CLOSESOCKET_STUCK = -2147467646
EVENT_EQOS_INFO_MACHINE_POLICY_REFRESH_NO_CHANGE = 1073758324
EVENT_EQOS_INFO_MACHINE_POLICY_REFRESH_WITH_CHANGE = 1073758325
EVENT_EQOS_INFO_USER_POLICY_REFRESH_NO_CHANGE = 1073758326
EVENT_EQOS_INFO_USER_POLICY_REFRESH_WITH_CHANGE = 1073758327
EVENT_EQOS_INFO_TCP_AUTOTUNING_NOT_CONFIGURED = 1073758328
EVENT_EQOS_INFO_TCP_AUTOTUNING_OFF = 1073758329
EVENT_EQOS_INFO_TCP_AUTOTUNING_HIGHLY_RESTRICTED = 1073758330
EVENT_EQOS_INFO_TCP_AUTOTUNING_RESTRICTED = 1073758331
EVENT_EQOS_INFO_TCP_AUTOTUNING_NORMAL = 1073758332
EVENT_EQOS_INFO_APP_MARKING_NOT_CONFIGURED = 1073758333
EVENT_EQOS_INFO_APP_MARKING_IGNORED = 1073758334
EVENT_EQOS_INFO_APP_MARKING_ALLOWED = 1073758335
EVENT_EQOS_INFO_LOCAL_SETTING_DONT_USE_NLA = 1073758336
EVENT_EQOS_URL_QOS_APPLICATION_CONFLICT = 1073758337
EVENT_EQOS_WARNING_TEST_1 = -2147467048
EVENT_EQOS_WARNING_TEST_2 = -2147467047
EVENT_EQOS_WARNING_MACHINE_POLICY_VERSION = -2147467046
EVENT_EQOS_WARNING_USER_POLICY_VERSION = -2147467045
EVENT_EQOS_WARNING_MACHINE_POLICY_PROFILE_NOT_SPECIFIED = -2147467044
EVENT_EQOS_WARNING_USER_POLICY_PROFILE_NOT_SPECIFIED = -2147467043
EVENT_EQOS_WARNING_MACHINE_POLICY_QUOTA_EXCEEDED = -2147467042
EVENT_EQOS_WARNING_USER_POLICY_QUOTA_EXCEEDED = -2147467041
EVENT_EQOS_WARNING_MACHINE_POLICY_CONFLICT = -2147467040
EVENT_EQOS_WARNING_USER_POLICY_CONFLICT = -2147467039
EVENT_EQOS_WARNING_MACHINE_POLICY_NO_FULLPATH_APPNAME = -2147467038
EVENT_EQOS_WARNING_USER_POLICY_NO_FULLPATH_APPNAME = -2147467037
EVENT_EQOS_ERROR_MACHINE_POLICY_REFERESH = -1073725124
EVENT_EQOS_ERROR_USER_POLICY_REFERESH = -1073725123
EVENT_EQOS_ERROR_OPENING_MACHINE_POLICY_ROOT_KEY = -1073725122
EVENT_EQOS_ERROR_OPENING_USER_POLICY_ROOT_KEY = -1073725121
EVENT_EQOS_ERROR_MACHINE_POLICY_KEYNAME_TOO_LONG = -1073725120
EVENT_EQOS_ERROR_USER_POLICY_KEYNAME_TOO_LONG = -1073725119
EVENT_EQOS_ERROR_MACHINE_POLICY_KEYNAME_SIZE_ZERO = -1073725118
EVENT_EQOS_ERROR_USER_POLICY_KEYNAME_SIZE_ZERO = -1073725117
EVENT_EQOS_ERROR_OPENING_MACHINE_POLICY_SUBKEY = -1073725116
EVENT_EQOS_ERROR_OPENING_USER_POLICY_SUBKEY = -1073725115
EVENT_EQOS_ERROR_PROCESSING_MACHINE_POLICY_FIELD = -1073725114
EVENT_EQOS_ERROR_PROCESSING_USER_POLICY_FIELD = -1073725113
EVENT_EQOS_ERROR_SETTING_TCP_AUTOTUNING = -1073725112
EVENT_EQOS_ERROR_SETTING_APP_MARKING = -1073725111
EVENT_WINNAT_SESSION_LIMIT_REACHED = -2147466648
HARDWARE_ADDRESS_LENGTH = 6
NETMAN_VARTYPE_ULONG = 0
NETMAN_VARTYPE_HARDWARE_ADDRESS = 1
NETMAN_VARTYPE_STRING = 2
REPL_ROLE_EXPORT = 1
REPL_ROLE_IMPORT = 2
REPL_ROLE_BOTH = 3
REPL_INTERVAL_INFOLEVEL = 1000
REPL_PULSE_INFOLEVEL = 1001
REPL_GUARDTIME_INFOLEVEL = 1002
REPL_RANDOM_INFOLEVEL = 1003
REPL_INTEGRITY_FILE = 1
REPL_INTEGRITY_TREE = 2
REPL_EXTENT_FILE = 1
REPL_EXTENT_TREE = 2
REPL_EXPORT_INTEGRITY_INFOLEVEL = 1000
REPL_EXPORT_EXTENT_INFOLEVEL = 1001
REPL_UNLOCK_NOFORCE = 0
REPL_UNLOCK_FORCE = 1
REPL_STATE_OK = 0
REPL_STATE_NO_MASTER = 1
REPL_STATE_NO_SYNC = 2
REPL_STATE_NEVER_REPLICATED = 3
SERVICE_WORKSTATION = 'LanmanWorkstation'
SERVICE_LM20_WORKSTATION = 'WORKSTATION'
WORKSTATION_DISPLAY_NAME = 'Workstation'
SERVICE_SERVER = 'LanmanServer'
SERVICE_LM20_SERVER = 'SERVER'
SERVER_DISPLAY_NAME = 'Server'
SERVICE_BROWSER = 'BROWSER'
SERVICE_LM20_BROWSER = 'BROWSER'
SERVICE_MESSENGER = 'MESSENGER'
SERVICE_LM20_MESSENGER = 'MESSENGER'
SERVICE_NETRUN = 'NETRUN'
SERVICE_LM20_NETRUN = 'NETRUN'
SERVICE_SPOOLER = 'SPOOLER'
SERVICE_LM20_SPOOLER = 'SPOOLER'
SERVICE_ALERTER = 'ALERTER'
SERVICE_LM20_ALERTER = 'ALERTER'
SERVICE_NETLOGON = 'NETLOGON'
SERVICE_LM20_NETLOGON = 'NETLOGON'
SERVICE_NETPOPUP = 'NETPOPUP'
SERVICE_LM20_NETPOPUP = 'NETPOPUP'
SERVICE_SQLSERVER = 'SQLSERVER'
SERVICE_LM20_SQLSERVER = 'SQLSERVER'
SERVICE_REPL = 'REPLICATOR'
SERVICE_LM20_REPL = 'REPLICATOR'
SERVICE_RIPL = 'REMOTEBOOT'
SERVICE_LM20_RIPL = 'REMOTEBOOT'
SERVICE_TIMESOURCE = 'TIMESOURCE'
SERVICE_LM20_TIMESOURCE = 'TIMESOURCE'
SERVICE_AFP = 'AFP'
SERVICE_LM20_AFP = 'AFP'
SERVICE_UPS = 'UPS'
SERVICE_LM20_UPS = 'UPS'
SERVICE_XACTSRV = 'XACTSRV'
SERVICE_LM20_XACTSRV = 'XACTSRV'
SERVICE_TCPIP = 'TCPIP'
SERVICE_LM20_TCPIP = 'TCPIP'
SERVICE_NBT = 'NBT'
SERVICE_LM20_NBT = 'NBT'
SERVICE_LMHOSTS = 'LMHOSTS'
SERVICE_LM20_LMHOSTS = 'LMHOSTS'
SERVICE_TELNET = 'Telnet'
SERVICE_LM20_TELNET = 'Telnet'
SERVICE_SCHEDULE = 'Schedule'
SERVICE_LM20_SCHEDULE = 'Schedule'
SERVICE_NTLMSSP = 'NtLmSsp'
SERVICE_DHCP = 'DHCP'
SERVICE_LM20_DHCP = 'DHCP'
SERVICE_NWSAP = 'NwSapAgent'
SERVICE_LM20_NWSAP = 'NwSapAgent'
NWSAP_DISPLAY_NAME = 'NW Sap Agent'
SERVICE_NWCS = 'NWCWorkstation'
SERVICE_DNS_CACHE = 'DnsCache'
SERVICE_W32TIME = 'w32time'
SERVCE_LM20_W32TIME = 'w32time'
SERVICE_KDC = 'kdc'
SERVICE_LM20_KDC = 'kdc'
SERVICE_RPCLOCATOR = 'RPCLOCATOR'
SERVICE_LM20_RPCLOCATOR = 'RPCLOCATOR'
SERVICE_TRKSVR = 'TrkSvr'
SERVICE_LM20_TRKSVR = 'TrkSvr'
SERVICE_TRKWKS = 'TrkWks'
SERVICE_LM20_TRKWKS = 'TrkWks'
SERVICE_NTFRS = 'NtFrs'
SERVICE_LM20_NTFRS = 'NtFrs'
SERVICE_ISMSERV = 'IsmServ'
SERVICE_LM20_ISMSERV = 'IsmServ'
SERVICE_NTDS = 'NTDS'
SERVICE_LM20_NTDS = 'NTDS'
SERVICE_ADWS = 'ADWS'
SERVICE_DSROLE = 'DsRoleSvc'
SERVICE_LM20_DSROLE = 'DsRoleSvc'
NETCFG_E_ALREADY_INITIALIZED = -2147180512
NETCFG_E_NOT_INITIALIZED = -2147180511
NETCFG_E_IN_USE = -2147180510
NETCFG_E_NO_WRITE_LOCK = -2147180508
NETCFG_E_NEED_REBOOT = -2147180507
NETCFG_E_ACTIVE_RAS_CONNECTIONS = -2147180506
NETCFG_E_ADAPTER_NOT_FOUND = -2147180505
NETCFG_E_COMPONENT_REMOVED_PENDING_REBOOT = -2147180504
NETCFG_E_MAX_FILTER_LIMIT = -2147180503
NETCFG_E_VMSWITCH_ACTIVE_OVER_ADAPTER = -2147180502
NETCFG_E_DUPLICATE_INSTANCEID = -2147180501
NETCFG_S_REBOOT = 303136
NETCFG_S_DISABLE_QUERY = 303138
NETCFG_S_STILL_REFERENCED = 303139
NETCFG_S_CAUSED_SETUP_CHANGE = 303140
NETCFG_S_COMMIT_NOW = 303141
NETCFG_CLIENT_CID_MS_MSClient = 'ms_msclient'
NETCFG_SERVICE_CID_MS_SERVER = 'ms_server'
NETCFG_SERVICE_CID_MS_NETBIOS = 'ms_netbios'
NETCFG_SERVICE_CID_MS_PSCHED = 'ms_pschedpc'
NETCFG_SERVICE_CID_MS_WLBS = 'ms_wlbs'
NETCFG_TRANS_CID_MS_APPLETALK = 'ms_appletalk'
NETCFG_TRANS_CID_MS_NETBEUI = 'ms_netbeui'
NETCFG_TRANS_CID_MS_NETMON = 'ms_netmon'
NETCFG_TRANS_CID_MS_NWIPX = 'ms_nwipx'
NETCFG_TRANS_CID_MS_NWSPX = 'ms_nwspx'
NETCFG_TRANS_CID_MS_TCPIP = 'ms_tcpip'
WZC_PROFILE_SUCCESS = 0
WZC_PROFILE_XML_ERROR_NO_VERSION = 1
WZC_PROFILE_XML_ERROR_BAD_VERSION = 2
WZC_PROFILE_XML_ERROR_UNSUPPORTED_VERSION = 3
WZC_PROFILE_XML_ERROR_SSID_NOT_FOUND = 4
WZC_PROFILE_XML_ERROR_BAD_SSID = 5
WZC_PROFILE_XML_ERROR_CONNECTION_TYPE = 6
WZC_PROFILE_XML_ERROR_AUTHENTICATION = 7
WZC_PROFILE_XML_ERROR_ENCRYPTION = 8
WZC_PROFILE_XML_ERROR_KEY_PROVIDED_AUTOMATICALLY = 9
WZC_PROFILE_XML_ERROR_1X_ENABLED = 10
WZC_PROFILE_XML_ERROR_EAP_METHOD = 11
WZC_PROFILE_XML_ERROR_BAD_KEY_INDEX = 12
WZC_PROFILE_XML_ERROR_KEY_INDEX_RANGE = 13
WZC_PROFILE_XML_ERROR_BAD_NETWORK_KEY = 14
WZC_PROFILE_CONFIG_ERROR_INVALID_AUTH_FOR_CONNECTION_TYPE = 15
WZC_PROFILE_CONFIG_ERROR_INVALID_ENCRYPTION_FOR_AUTHMODE = 16
WZC_PROFILE_CONFIG_ERROR_KEY_REQUIRED = 17
WZC_PROFILE_CONFIG_ERROR_KEY_INDEX_REQUIRED = 18
WZC_PROFILE_CONFIG_ERROR_KEY_INDEX_NOT_APPLICABLE = 19
WZC_PROFILE_CONFIG_ERROR_1X_NOT_ALLOWED = 20
WZC_PROFILE_CONFIG_ERROR_1X_NOT_ALLOWED_KEY_REQUIRED = 21
WZC_PROFILE_CONFIG_ERROR_1X_NOT_ENABLED_KEY_PROVIDED = 22
WZC_PROFILE_CONFIG_ERROR_EAP_METHOD_REQUIRED = 23
WZC_PROFILE_CONFIG_ERROR_EAP_METHOD_NOT_APPLICABLE = 24
WZC_PROFILE_CONFIG_ERROR_WPA_NOT_SUPPORTED = 25
WZC_PROFILE_CONFIG_ERROR_WPA_ENCRYPTION_NOT_SUPPORTED = 26
WZC_PROFILE_SET_ERROR_DUPLICATE_NETWORK = 27
WZC_PROFILE_SET_ERROR_MEMORY_ALLOCATION = 28
WZC_PROFILE_SET_ERROR_READING_1X_CONFIG = 29
WZC_PROFILE_SET_ERROR_WRITING_1X_CONFIG = 30
WZC_PROFILE_SET_ERROR_WRITING_WZC_CFG = 31
WZC_PROFILE_API_ERROR_NOT_SUPPORTED = 32
WZC_PROFILE_API_ERROR_FAILED_TO_LOAD_XML = 33
WZC_PROFILE_API_ERROR_FAILED_TO_LOAD_SCHEMA = 34
WZC_PROFILE_API_ERROR_XML_VALIDATION_FAILED = 35
WZC_PROFILE_API_ERROR_INTERNAL = 36
RF_ROUTING = 1
RF_ROUTINGV6 = 2
RF_DEMAND_UPDATE_ROUTES = 4
RF_ADD_ALL_INTERFACES = 16
RF_MULTICAST = 32
RF_POWER = 64
MS_ROUTER_VERSION = 1536
ROUTING_DOMAIN_INFO_REVISION_1 = 1
INTERFACE_INFO_REVISION_1 = 1
IR_PROMISCUOUS = 0
IR_PROMISCUOUS_MULTICAST = 1
PROTO_IP_MSDP = 9
PROTO_IP_IGMP = 10
PROTO_IP_BGMP = 11
PROTO_IP_VRRP = 112
PROTO_IP_BOOTP = 9999
PROTO_IPV6_DHCP = 999
PROTO_IP_DNS_PROXY = 10003
PROTO_IP_DHCP_ALLOCATOR = 10004
PROTO_IP_NAT = 10005
PROTO_IP_DIFFSERV = 10008
PROTO_IP_MGM = 10009
PROTO_IP_ALG = 10010
PROTO_IP_H323 = 10011
PROTO_IP_FTP = 10012
PROTO_IP_DTP = 10013
PROTO_TYPE_UCAST = 0
PROTO_TYPE_MCAST = 1
PROTO_TYPE_MS0 = 2
PROTO_TYPE_MS1 = 3
PROTO_VENDOR_MS0 = 0
PROTO_VENDOR_MS1 = 311
PROTO_VENDOR_MS2 = 16383
IPX_PROTOCOL_BASE = 131071
IPX_PROTOCOL_RIP = 131072
RIS_INTERFACE_ADDRESS_CHANGE = 0
RIS_INTERFACE_ENABLED = 1
RIS_INTERFACE_DISABLED = 2
RIS_INTERFACE_MEDIA_PRESENT = 3
RIS_INTERFACE_MEDIA_ABSENT = 4
MRINFO_TUNNEL_FLAG = 1
MRINFO_PIM_FLAG = 4
MRINFO_DOWN_FLAG = 16
MRINFO_DISABLED_FLAG = 32
MRINFO_QUERIER_FLAG = 64
MRINFO_LEAF_FLAG = 128
MFE_NO_ERROR = 0
MFE_REACHED_CORE = 1
MFE_OIF_PRUNED = 5
MFE_PRUNED_UPSTREAM = 4
MFE_OLD_ROUTER = 11
MFE_NOT_FORWARDING = 2
MFE_WRONG_IF = 3
MFE_BOUNDARY_REACHED = 6
MFE_NO_MULTICAST = 7
MFE_IIF = 8
MFE_NO_ROUTE = 9
MFE_NOT_LAST_HOP = 10
MFE_PROHIBITED = 12
MFE_NO_SPACE = 13
REGISTER_PROTOCOL_ENTRY_POINT_STRING = 'RegisterProtocol'
ALIGN_SIZE = 8
RTR_INFO_BLOCK_VERSION = 1
TRACE_USE_FILE = 1
TRACE_USE_CONSOLE = 2
TRACE_NO_SYNCH = 4
TRACE_NO_STDINFO = 1
TRACE_USE_MASK = 2
TRACE_USE_MSEC = 4
TRACE_USE_DATE = 8
INVALID_TRACEID = 4294967295
RTUTILS_MAX_PROTOCOL_NAME_LEN = 40
RTUTILS_MAX_PROTOCOL_DLL_LEN = 48
MAX_PROTOCOL_NAME_LEN = 40
MAX_PROTOCOL_DLL_LEN = 48
def _define_NetUserAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetUserAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUserEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.NetworkManagement.NetManagement.NET_USER_ENUM_FILTER_FLAGS,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetUserEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'filter'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUserGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetUserGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'username'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUserSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetUserSetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'username'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUserDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetUserDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'username'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUserGetGroups():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32))(('NetUserGetGroups', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'username'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUserSetGroups():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,UInt32)(('NetUserSetGroups', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'username'),(1, 'level'),(1, 'buf'),(1, 'num_entries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUserGetLocalGroups():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32))(('NetUserGetLocalGroups', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'username'),(1, 'level'),(1, 'flags'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUserModalsGet():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetUserModalsGet', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUserModalsSet():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetUserModalsSet', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUserChangePassword():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetUserChangePassword', windll['NETAPI32.dll']), ((1, 'domainname'),(1, 'username'),(1, 'oldpassword'),(1, 'newpassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGroupAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetGroupAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGroupAddUser():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetGroupAddUser', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'GroupName'),(1, 'username'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGroupEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UIntPtr))(('NetGroupEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGroupGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetGroupGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGroupSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetGroupSetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGroupDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetGroupDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGroupDelUser():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetGroupDelUser', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'GroupName'),(1, 'Username'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGroupGetUsers():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UIntPtr))(('NetGroupGetUsers', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'ResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGroupSetUsers():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,UInt32)(('NetGroupSetUsers', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),(1, 'level'),(1, 'buf'),(1, 'totalentries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetLocalGroupAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetLocalGroupAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetLocalGroupAddMember():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PSID)(('NetLocalGroupAddMember', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),(1, 'membersid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetLocalGroupEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UIntPtr))(('NetLocalGroupEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resumehandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetLocalGroupGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetLocalGroupGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetLocalGroupSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetLocalGroupSetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetLocalGroupDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetLocalGroupDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetLocalGroupDelMember():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PSID)(('NetLocalGroupDelMember', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),(1, 'membersid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetLocalGroupGetMembers():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UIntPtr))(('NetLocalGroupGetMembers', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'localgroupname'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resumehandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetLocalGroupSetMembers():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,UInt32)(('NetLocalGroupSetMembers', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),(1, 'level'),(1, 'buf'),(1, 'totalentries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetLocalGroupAddMembers():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,UInt32)(('NetLocalGroupAddMembers', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),(1, 'level'),(1, 'buf'),(1, 'totalentries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetLocalGroupDelMembers():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,UInt32)(('NetLocalGroupDelMembers', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'groupname'),(1, 'level'),(1, 'buf'),(1, 'totalentries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetQueryDisplayInformation():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(c_void_p))(('NetQueryDisplayInformation', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'Level'),(1, 'Index'),(1, 'EntriesRequested'),(1, 'PreferredMaximumLength'),(1, 'ReturnedEntryCount'),(1, 'SortedBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGetDisplayInformationIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('NetGetDisplayInformationIndex', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'Level'),(1, 'Prefix'),(1, 'Index'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAccessAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetAccessAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAccessEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetAccessEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'BasePath'),(1, 'Recursive'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAccessGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetAccessGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'resource'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAccessSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetAccessSetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'resource'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAccessDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetAccessDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'resource'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAccessGetUserPerms():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('NetAccessGetUserPerms', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'UGname'),(1, 'resource'),(1, 'Perms'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetValidatePasswordPolicy():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,c_void_p,win32more.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_TYPE,c_void_p,POINTER(c_void_p))(('NetValidatePasswordPolicy', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'Qualifier'),(1, 'ValidationType'),(1, 'InputArg'),(1, 'OutputArg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetValidatePasswordPolicyFree():
    try:
        return WINFUNCTYPE(UInt32,POINTER(c_void_p))(('NetValidatePasswordPolicyFree', windll['NETAPI32.dll']), ((1, 'OutputArg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGetDCName():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(c_char_p_no))(('NetGetDCName', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'DomainName'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGetAnyDCName():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(c_char_p_no))(('NetGetAnyDCName', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'DomainName'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_NetLogonControl2():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,c_char_p_no,POINTER(c_char_p_no))(('I_NetLogonControl2', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'FunctionCode'),(1, 'QueryLevel'),(1, 'Data'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAddServiceAccount():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('NetAddServiceAccount', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'AccountName'),(1, 'Password'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetRemoveServiceAccount():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('NetRemoveServiceAccount', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'AccountName'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetEnumerateServiceAccounts():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(POINTER(POINTER(UInt16))))(('NetEnumerateServiceAccounts', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'Flags'),(1, 'AccountsCount'),(1, 'Accounts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetIsServiceAccount():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL))(('NetIsServiceAccount', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'AccountName'),(1, 'IsService'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetQueryServiceAccount():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetQueryServiceAccount', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'AccountName'),(1, 'InfoLevel'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAlertRaise():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,c_void_p,UInt32)(('NetAlertRaise', windll['NETAPI32.dll']), ((1, 'AlertType'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAlertRaiseEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,c_void_p,UInt32,win32more.Foundation.PWSTR)(('NetAlertRaiseEx', windll['NETAPI32.dll']), ((1, 'AlertType'),(1, 'VariableInfo'),(1, 'VariableInfoSize'),(1, 'ServiceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetMessageNameAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetMessageNameAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'msgname'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetMessageNameEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetMessageNameEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetMessageNameGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetMessageNameGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'msgname'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetMessageNameDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetMessageNameDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'msgname'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetMessageBufferSend():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,UInt32)(('NetMessageBufferSend', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'msgname'),(1, 'fromname'),(1, 'buf'),(1, 'buflen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetRemoteTOD():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(c_char_p_no))(('NetRemoteTOD', windll['NETAPI32.dll']), ((1, 'UncServerName'),(1, 'BufferPtr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetRemoteComputerSupports():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.NetManagement.NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS,POINTER(UInt32))(('NetRemoteComputerSupports', windll['NETAPI32.dll']), ((1, 'UncServerName'),(1, 'OptionsWanted'),(1, 'OptionsSupported'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetReplGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetReplSetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplExportDirAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetReplExportDirAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplExportDirDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetReplExportDirDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'dirname'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplExportDirEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetReplExportDirEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resumehandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplExportDirGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetReplExportDirGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'dirname'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplExportDirSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetReplExportDirSetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'dirname'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplExportDirLock():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetReplExportDirLock', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'dirname'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplExportDirUnlock():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('NetReplExportDirUnlock', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'dirname'),(1, 'unlockforce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplImportDirAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetReplImportDirAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplImportDirDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetReplImportDirDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'dirname'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplImportDirEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetReplImportDirEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resumehandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplImportDirGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetReplImportDirGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'dirname'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplImportDirLock():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetReplImportDirLock', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'dirname'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetReplImportDirUnlock():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('NetReplImportDirUnlock', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'dirname'),(1, 'unlockforce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),win32more.NetworkManagement.NetManagement.NET_SERVER_TYPE,win32more.Foundation.PWSTR,POINTER(UInt32))(('NetServerEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'servertype'),(1, 'domain'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetServerGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetServerSetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),(1, 'ParmError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerDiskEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetServerDiskEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerComputerNameAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetServerComputerNameAdd', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'EmulatedDomainName'),(1, 'EmulatedServerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerComputerNameDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetServerComputerNameDel', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'EmulatedServerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerTransportAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no)(('NetServerTransportAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerTransportAddEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no)(('NetServerTransportAddEx', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerTransportDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no)(('NetServerTransportDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerTransportEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetServerTransportEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServiceControl():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(c_char_p_no))(('NetServiceControl', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'service'),(1, 'opcode'),(1, 'arg'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServiceEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetServiceEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServiceGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetServiceGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'service'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServiceInstall():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(c_char_p_no))(('NetServiceInstall', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'service'),(1, 'argc'),(1, 'argv'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUseAdd():
    try:
        return WINFUNCTYPE(UInt32,POINTER(SByte),UInt32,c_char_p_no,POINTER(UInt32))(('NetUseAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'LevelFlags'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUseDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.NetworkManagement.NetManagement.FORCE_LEVEL_FLAGS)(('NetUseDel', windll['NETAPI32.dll']), ((1, 'UncServerName'),(1, 'UseName'),(1, 'ForceLevelFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUseEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetUseEnum', windll['NETAPI32.dll']), ((1, 'UncServerName'),(1, 'LevelFlags'),(1, 'BufPtr'),(1, 'PreferedMaximumSize'),(1, 'EntriesRead'),(1, 'TotalEntries'),(1, 'ResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUseGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetUseGetInfo', windll['NETAPI32.dll']), ((1, 'UncServerName'),(1, 'UseName'),(1, 'LevelFlags'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetWkstaGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetWkstaGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetWkstaSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetWkstaSetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buffer'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetWkstaUserGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetWkstaUserGetInfo', windll['NETAPI32.dll']), ((1, 'reserved'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetWkstaUserSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetWkstaUserSetInfo', windll['NETAPI32.dll']), ((1, 'reserved'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetWkstaUserEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetWkstaUserEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resumehandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetWkstaTransportAdd():
    try:
        return WINFUNCTYPE(UInt32,POINTER(SByte),UInt32,c_char_p_no,POINTER(UInt32))(('NetWkstaTransportAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetWkstaTransportDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.NetworkManagement.NetManagement.FORCE_LEVEL_FLAGS)(('NetWkstaTransportDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'transportname'),(1, 'ucond'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetWkstaTransportEnum():
    try:
        return WINFUNCTYPE(UInt32,POINTER(SByte),UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetWkstaTransportEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetApiBufferAllocate():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(c_void_p))(('NetApiBufferAllocate', windll['NETAPI32.dll']), ((1, 'ByteCount'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetApiBufferFree():
    try:
        return WINFUNCTYPE(UInt32,c_void_p)(('NetApiBufferFree', windll['NETAPI32.dll']), ((1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetApiBufferReallocate():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,POINTER(c_void_p))(('NetApiBufferReallocate', windll['NETAPI32.dll']), ((1, 'OldBuffer'),(1, 'NewByteCount'),(1, 'NewBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetApiBufferSize():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(UInt32))(('NetApiBufferSize', windll['NETAPI32.dll']), ((1, 'Buffer'),(1, 'ByteCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetErrorLogClear():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no)(('NetErrorLogClear', windll['NETAPI32.dll']), ((1, 'UncServerName'),(1, 'BackupFile'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetErrorLogRead():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.NetManagement.HLOG_head),UInt32,POINTER(UInt32),UInt32,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32))(('NetErrorLogRead', windll['NETAPI32.dll']), ((1, 'UncServerName'),(1, 'Reserved1'),(1, 'ErrorLogHandle'),(1, 'Offset'),(1, 'Reserved2'),(1, 'Reserved3'),(1, 'OffsetFlag'),(1, 'BufPtr'),(1, 'PrefMaxSize'),(1, 'BytesRead'),(1, 'TotalAvailable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetErrorLogWrite():
    try:
        return WINFUNCTYPE(UInt32,c_char_p_no,UInt32,win32more.Foundation.PWSTR,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no)(('NetErrorLogWrite', windll['NETAPI32.dll']), ((1, 'Reserved1'),(1, 'Code'),(1, 'Component'),(1, 'Buffer'),(1, 'NumBytes'),(1, 'MsgBuf'),(1, 'StrCount'),(1, 'Reserved2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetConfigGet():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(c_char_p_no))(('NetConfigGet', windll['NETAPI32.dll']), ((1, 'server'),(1, 'component'),(1, 'parameter'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetConfigGetAll():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(c_char_p_no))(('NetConfigGetAll', windll['NETAPI32.dll']), ((1, 'server'),(1, 'component'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetConfigSet():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,c_char_p_no,UInt32)(('NetConfigSet', windll['NETAPI32.dll']), ((1, 'server'),(1, 'reserved1'),(1, 'component'),(1, 'level'),(1, 'reserved2'),(1, 'buf'),(1, 'reserved3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAuditClear():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetAuditClear', windll['NETAPI32.dll']), ((1, 'server'),(1, 'backupfile'),(1, 'service'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAuditRead():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.NetManagement.HLOG_head),UInt32,POINTER(UInt32),UInt32,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32))(('NetAuditRead', windll['NETAPI32.dll']), ((1, 'server'),(1, 'service'),(1, 'auditloghandle'),(1, 'offset'),(1, 'reserved1'),(1, 'reserved2'),(1, 'offsetflag'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'bytesread'),(1, 'totalavailable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAuditWrite():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_char_p_no,UInt32,win32more.Foundation.PWSTR,c_char_p_no)(('NetAuditWrite', windll['NETAPI32.dll']), ((1, 'type'),(1, 'buf'),(1, 'numbytes'),(1, 'service'),(1, 'reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetJoinDomain():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS)(('NetJoinDomain', windll['NETAPI32.dll']), ((1, 'lpServer'),(1, 'lpDomain'),(1, 'lpMachineAccountOU'),(1, 'lpAccount'),(1, 'lpPassword'),(1, 'fJoinOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetUnjoinDomain():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('NetUnjoinDomain', windll['NETAPI32.dll']), ((1, 'lpServer'),(1, 'lpAccount'),(1, 'lpPassword'),(1, 'fUnjoinOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetRenameMachineInDomain():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('NetRenameMachineInDomain', windll['NETAPI32.dll']), ((1, 'lpServer'),(1, 'lpNewMachineName'),(1, 'lpAccount'),(1, 'lpPassword'),(1, 'fRenameOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetValidateName():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.NetworkManagement.NetManagement.NETSETUP_NAME_TYPE)(('NetValidateName', windll['NETAPI32.dll']), ((1, 'lpServer'),(1, 'lpName'),(1, 'lpAccount'),(1, 'lpPassword'),(1, 'NameType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGetJoinableOUs():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(POINTER(win32more.Foundation.PWSTR)))(('NetGetJoinableOUs', windll['NETAPI32.dll']), ((1, 'lpServer'),(1, 'lpDomain'),(1, 'lpAccount'),(1, 'lpPassword'),(1, 'OUCount'),(1, 'OUs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetAddAlternateComputerName():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('NetAddAlternateComputerName', windll['NETAPI32.dll']), ((1, 'Server'),(1, 'AlternateName'),(1, 'DomainAccount'),(1, 'DomainAccountPassword'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetRemoveAlternateComputerName():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('NetRemoveAlternateComputerName', windll['NETAPI32.dll']), ((1, 'Server'),(1, 'AlternateName'),(1, 'DomainAccount'),(1, 'DomainAccountPassword'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetSetPrimaryComputerName():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('NetSetPrimaryComputerName', windll['NETAPI32.dll']), ((1, 'Server'),(1, 'PrimaryName'),(1, 'DomainAccount'),(1, 'DomainAccountPassword'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetEnumerateComputerNames():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.NetManagement.NET_COMPUTER_NAME_TYPE,UInt32,POINTER(UInt32),POINTER(POINTER(win32more.Foundation.PWSTR)))(('NetEnumerateComputerNames', windll['NETAPI32.dll']), ((1, 'Server'),(1, 'NameType'),(1, 'Reserved'),(1, 'EntryCount'),(1, 'ComputerNames'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetProvisionComputerAccount():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.NetworkManagement.NetManagement.NETSETUP_PROVISION,POINTER(c_char_p_no),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(('NetProvisionComputerAccount', windll['NETAPI32.dll']), ((1, 'lpDomain'),(1, 'lpMachineName'),(1, 'lpMachineAccountOU'),(1, 'lpDcName'),(1, 'dwOptions'),(1, 'pProvisionBinData'),(1, 'pdwProvisionBinDataSize'),(1, 'pProvisionTextData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetRequestOfflineDomainJoin():
    try:
        return WINFUNCTYPE(UInt32,c_char_p_no,UInt32,win32more.NetworkManagement.NetManagement.NET_REQUEST_PROVISION_OPTIONS,win32more.Foundation.PWSTR)(('NetRequestOfflineDomainJoin', windll['NETAPI32.dll']), ((1, 'pProvisionBinData'),(1, 'cbProvisionBinDataSize'),(1, 'dwOptions'),(1, 'lpWindowsPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetCreateProvisioningPackage():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.NetManagement.NETSETUP_PROVISIONING_PARAMS_head),POINTER(c_char_p_no),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(('NetCreateProvisioningPackage', windll['NETAPI32.dll']), ((1, 'pProvisioningParams'),(1, 'ppPackageBinData'),(1, 'pdwPackageBinDataSize'),(1, 'ppPackageTextData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetRequestProvisioningPackageInstall():
    try:
        return WINFUNCTYPE(UInt32,c_char_p_no,UInt32,win32more.NetworkManagement.NetManagement.NET_REQUEST_PROVISION_OPTIONS,win32more.Foundation.PWSTR,c_void_p)(('NetRequestProvisioningPackageInstall', windll['NETAPI32.dll']), ((1, 'pPackageBinData'),(1, 'dwPackageBinDataSize'),(1, 'dwProvisionOptions'),(1, 'lpWindowsPath'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGetAadJoinInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.NetManagement.DSREG_JOIN_INFO_head)))(('NetGetAadJoinInformation', windll['NETAPI32.dll']), ((1, 'pcszTenantId'),(1, 'ppJoinInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetFreeAadJoinInformation():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.NetManagement.DSREG_JOIN_INFO_head))(('NetFreeAadJoinInformation', windll['NETAPI32.dll']), ((1, 'pJoinInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetGetJoinInformation():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.NetworkManagement.NetManagement.NETSETUP_JOIN_STATUS))(('NetGetJoinInformation', windll['NETAPI32.dll']), ((1, 'lpServer'),(1, 'lpNameBuffer'),(1, 'BufferType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNetScheduleAccountInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR)(('GetNetScheduleAccountInformation', windll['mstask.dll']), ((1, 'pwszServerName'),(1, 'ccAccount'),(1, 'wszAccount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetNetScheduleAccountInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('SetNetScheduleAccountInformation', windll['mstask.dll']), ((1, 'pwszServerName'),(1, 'pwszAccount'),(1, 'pwszPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetScheduleJobAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,c_char_p_no,POINTER(UInt32))(('NetScheduleJobAdd', windll['NETAPI32.dll']), ((1, 'Servername'),(1, 'Buffer'),(1, 'JobId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetScheduleJobDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32)(('NetScheduleJobDel', windll['NETAPI32.dll']), ((1, 'Servername'),(1, 'MinJobId'),(1, 'MaxJobId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetScheduleJobEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetScheduleJobEnum', windll['NETAPI32.dll']), ((1, 'Servername'),(1, 'PointerToBuffer'),(1, 'PrefferedMaximumLength'),(1, 'EntriesRead'),(1, 'TotalEntries'),(1, 'ResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetScheduleJobGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetScheduleJobGetInfo', windll['NETAPI32.dll']), ((1, 'Servername'),(1, 'JobId'),(1, 'PointerToBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceRegisterExA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32)(('TraceRegisterExA', windll['rtutils.dll']), ((1, 'lpszCallerName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceDeregisterA():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('TraceDeregisterA', windll['rtutils.dll']), ((1, 'dwTraceID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceDeregisterExA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32)(('TraceDeregisterExA', windll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceGetConsoleA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Foundation.HANDLE))(('TraceGetConsoleA', windll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'lphConsole'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TracePrintfA():
    try:
        return CFUNCTYPE(UInt32,UInt32,win32more.Foundation.PSTR)(('TracePrintfA', cdll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'lpszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TracePrintfExA():
    try:
        return CFUNCTYPE(UInt32,UInt32,UInt32,win32more.Foundation.PSTR)(('TracePrintfExA', cdll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'dwFlags'),(1, 'lpszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceVprintfExA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.Foundation.PSTR,POINTER(SByte))(('TraceVprintfExA', windll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'dwFlags'),(1, 'lpszFormat'),(1, 'arglist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TracePutsExA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.Foundation.PSTR)(('TracePutsExA', windll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'dwFlags'),(1, 'lpszString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceDumpExA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,c_char_p_no,UInt32,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('TraceDumpExA', windll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'dwFlags'),(1, 'lpbBytes'),(1, 'dwByteCount'),(1, 'dwGroupSize'),(1, 'bAddressPrefix'),(1, 'lpszPrefix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceRegisterExW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32)(('TraceRegisterExW', windll['rtutils.dll']), ((1, 'lpszCallerName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceDeregisterW():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('TraceDeregisterW', windll['rtutils.dll']), ((1, 'dwTraceID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceDeregisterExW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32)(('TraceDeregisterExW', windll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceGetConsoleW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Foundation.HANDLE))(('TraceGetConsoleW', windll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'lphConsole'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TracePrintfW():
    try:
        return CFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR)(('TracePrintfW', cdll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'lpszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TracePrintfExW():
    try:
        return CFUNCTYPE(UInt32,UInt32,UInt32,win32more.Foundation.PWSTR)(('TracePrintfExW', cdll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'dwFlags'),(1, 'lpszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceVprintfExW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(SByte))(('TraceVprintfExW', windll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'dwFlags'),(1, 'lpszFormat'),(1, 'arglist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TracePutsExW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.Foundation.PWSTR)(('TracePutsExW', windll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'dwFlags'),(1, 'lpszString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceDumpExW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,c_char_p_no,UInt32,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('TraceDumpExW', windll['rtutils.dll']), ((1, 'dwTraceID'),(1, 'dwFlags'),(1, 'lpbBytes'),(1, 'dwByteCount'),(1, 'dwGroupSize'),(1, 'bAddressPrefix'),(1, 'lpszPrefix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogErrorA():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Foundation.PSTR),UInt32)(('LogErrorA', windll['rtutils.dll']), ((1, 'dwMessageId'),(1, 'cNumberOfSubStrings'),(1, 'plpwsSubStrings'),(1, 'dwErrorCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogEventA():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.PSTR))(('LogEventA', windll['rtutils.dll']), ((1, 'wEventType'),(1, 'dwMessageId'),(1, 'cNumberOfSubStrings'),(1, 'plpwsSubStrings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogErrorW():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Foundation.PWSTR),UInt32)(('LogErrorW', windll['rtutils.dll']), ((1, 'dwMessageId'),(1, 'cNumberOfSubStrings'),(1, 'plpwsSubStrings'),(1, 'dwErrorCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogEventW():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.PWSTR))(('LogEventW', windll['rtutils.dll']), ((1, 'wEventType'),(1, 'dwMessageId'),(1, 'cNumberOfSubStrings'),(1, 'plpwsSubStrings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogRegisterA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR)(('RouterLogRegisterA', windll['rtutils.dll']), ((1, 'lpszSource'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogDeregisterA():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE)(('RouterLogDeregisterA', windll['rtutils.dll']), ((1, 'hLogHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogEventA():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.PSTR),UInt32)(('RouterLogEventA', windll['rtutils.dll']), ((1, 'hLogHandle'),(1, 'dwEventType'),(1, 'dwMessageId'),(1, 'dwSubStringCount'),(1, 'plpszSubStringArray'),(1, 'dwErrorCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogEventDataA():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.PSTR),UInt32,c_char_p_no)(('RouterLogEventDataA', windll['rtutils.dll']), ((1, 'hLogHandle'),(1, 'dwEventType'),(1, 'dwMessageId'),(1, 'dwSubStringCount'),(1, 'plpszSubStringArray'),(1, 'dwDataBytes'),(1, 'lpDataBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogEventStringA():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.PSTR),UInt32,UInt32)(('RouterLogEventStringA', windll['rtutils.dll']), ((1, 'hLogHandle'),(1, 'dwEventType'),(1, 'dwMessageId'),(1, 'dwSubStringCount'),(1, 'plpszSubStringArray'),(1, 'dwErrorCode'),(1, 'dwErrorIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogEventExA():
    try:
        return CFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,win32more.Foundation.PSTR)(('RouterLogEventExA', cdll['rtutils.dll']), ((1, 'hLogHandle'),(1, 'dwEventType'),(1, 'dwErrorCode'),(1, 'dwMessageId'),(1, 'ptszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogEventValistExA():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,win32more.Foundation.PSTR,POINTER(SByte))(('RouterLogEventValistExA', windll['rtutils.dll']), ((1, 'hLogHandle'),(1, 'dwEventType'),(1, 'dwErrorCode'),(1, 'dwMessageId'),(1, 'ptszFormat'),(1, 'arglist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterGetErrorStringA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Foundation.PSTR))(('RouterGetErrorStringA', windll['rtutils.dll']), ((1, 'dwErrorCode'),(1, 'lplpszErrorString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogRegisterW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR)(('RouterLogRegisterW', windll['rtutils.dll']), ((1, 'lpszSource'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogDeregisterW():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE)(('RouterLogDeregisterW', windll['rtutils.dll']), ((1, 'hLogHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogEventW():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.PWSTR),UInt32)(('RouterLogEventW', windll['rtutils.dll']), ((1, 'hLogHandle'),(1, 'dwEventType'),(1, 'dwMessageId'),(1, 'dwSubStringCount'),(1, 'plpszSubStringArray'),(1, 'dwErrorCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogEventDataW():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.PWSTR),UInt32,c_char_p_no)(('RouterLogEventDataW', windll['rtutils.dll']), ((1, 'hLogHandle'),(1, 'dwEventType'),(1, 'dwMessageId'),(1, 'dwSubStringCount'),(1, 'plpszSubStringArray'),(1, 'dwDataBytes'),(1, 'lpDataBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogEventStringW():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.PWSTR),UInt32,UInt32)(('RouterLogEventStringW', windll['rtutils.dll']), ((1, 'hLogHandle'),(1, 'dwEventType'),(1, 'dwMessageId'),(1, 'dwSubStringCount'),(1, 'plpszSubStringArray'),(1, 'dwErrorCode'),(1, 'dwErrorIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogEventExW():
    try:
        return CFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,win32more.Foundation.PWSTR)(('RouterLogEventExW', cdll['rtutils.dll']), ((1, 'hLogHandle'),(1, 'dwEventType'),(1, 'dwErrorCode'),(1, 'dwMessageId'),(1, 'ptszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterLogEventValistExW():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(SByte))(('RouterLogEventValistExW', windll['rtutils.dll']), ((1, 'hLogHandle'),(1, 'dwEventType'),(1, 'dwErrorCode'),(1, 'dwMessageId'),(1, 'ptszFormat'),(1, 'arglist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterGetErrorStringW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Foundation.PWSTR))(('RouterGetErrorStringW', windll['rtutils.dll']), ((1, 'dwErrorCode'),(1, 'lplpwszErrorString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RouterAssert():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR)(('RouterAssert', windll['rtutils.dll']), ((1, 'pszFailedAssertion'),(1, 'pszFileName'),(1, 'dwLineNumber'),(1, 'pszMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprSetupProtocolEnum():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(c_char_p_no),POINTER(UInt32))(('MprSetupProtocolEnum', windll['rtutils.dll']), ((1, 'dwTransportId'),(1, 'lplpBuffer'),(1, 'lpdwEntriesRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprSetupProtocolFree():
    try:
        return WINFUNCTYPE(UInt32,c_void_p)(('MprSetupProtocolFree', windll['rtutils.dll']), ((1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AT_ENUM_head():
    class AT_ENUM(Structure):
        pass
    return AT_ENUM
def _define_AT_ENUM():
    AT_ENUM = win32more.NetworkManagement.NetManagement.AT_ENUM_head
    AT_ENUM._fields_ = [
        ('JobId', UInt32),
        ('JobTime', UIntPtr),
        ('DaysOfMonth', UInt32),
        ('DaysOfWeek', Byte),
        ('Flags', Byte),
        ('Command', win32more.Foundation.PWSTR),
    ]
    return AT_ENUM
def _define_AT_INFO_head():
    class AT_INFO(Structure):
        pass
    return AT_INFO
def _define_AT_INFO():
    AT_INFO = win32more.NetworkManagement.NetManagement.AT_INFO_head
    AT_INFO._fields_ = [
        ('JobTime', UIntPtr),
        ('DaysOfMonth', UInt32),
        ('DaysOfWeek', Byte),
        ('Flags', Byte),
        ('Command', win32more.Foundation.PWSTR),
    ]
    return AT_INFO
def _define_AUDIT_ENTRY_head():
    class AUDIT_ENTRY(Structure):
        pass
    return AUDIT_ENTRY
def _define_AUDIT_ENTRY():
    AUDIT_ENTRY = win32more.NetworkManagement.NetManagement.AUDIT_ENTRY_head
    AUDIT_ENTRY._fields_ = [
        ('ae_len', UInt32),
        ('ae_reserved', UInt32),
        ('ae_time', UInt32),
        ('ae_type', UInt32),
        ('ae_data_offset', UInt32),
        ('ae_data_size', UInt32),
    ]
    return AUDIT_ENTRY
BIND_FLAGS1 = Int32
NCN_ADD = 1
NCN_REMOVE = 2
NCN_UPDATE = 4
NCN_ENABLE = 16
NCN_DISABLE = 32
NCN_BINDING_PATH = 256
NCN_PROPERTYCHANGE = 512
NCN_NET = 65536
NCN_NETTRANS = 131072
NCN_NETCLIENT = 262144
NCN_NETSERVICE = 524288
COMPONENT_CHARACTERISTICS = Int32
NCF_VIRTUAL = 1
NCF_SOFTWARE_ENUMERATED = 2
NCF_PHYSICAL = 4
NCF_HIDDEN = 8
NCF_NO_SERVICE = 16
NCF_NOT_USER_REMOVABLE = 32
NCF_MULTIPORT_INSTANCED_ADAPTER = 64
NCF_HAS_UI = 128
NCF_SINGLE_INSTANCE = 256
NCF_FILTER = 1024
NCF_DONTEXPOSELOWER = 4096
NCF_HIDE_BINDING = 8192
NCF_NDIS_PROTOCOL = 16384
NCF_FIXED_BINDING = 131072
NCF_LW_FILTER = 262144
def _define_CONFIG_INFO_0_head():
    class CONFIG_INFO_0(Structure):
        pass
    return CONFIG_INFO_0
def _define_CONFIG_INFO_0():
    CONFIG_INFO_0 = win32more.NetworkManagement.NetManagement.CONFIG_INFO_0_head
    CONFIG_INFO_0._fields_ = [
        ('cfgi0_key', win32more.Foundation.PWSTR),
        ('cfgi0_data', win32more.Foundation.PWSTR),
    ]
    return CONFIG_INFO_0
DEFAULT_PAGES = Int32
DPP_ADVANCED = 1
def _define_DSREG_JOIN_INFO_head():
    class DSREG_JOIN_INFO(Structure):
        pass
    return DSREG_JOIN_INFO
def _define_DSREG_JOIN_INFO():
    DSREG_JOIN_INFO = win32more.NetworkManagement.NetManagement.DSREG_JOIN_INFO_head
    DSREG_JOIN_INFO._fields_ = [
        ('joinType', win32more.NetworkManagement.NetManagement.DSREG_JOIN_TYPE),
        ('pJoinCertificate', POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ('pszDeviceId', win32more.Foundation.PWSTR),
        ('pszIdpDomain', win32more.Foundation.PWSTR),
        ('pszTenantId', win32more.Foundation.PWSTR),
        ('pszJoinUserEmail', win32more.Foundation.PWSTR),
        ('pszTenantDisplayName', win32more.Foundation.PWSTR),
        ('pszMdmEnrollmentUrl', win32more.Foundation.PWSTR),
        ('pszMdmTermsOfUseUrl', win32more.Foundation.PWSTR),
        ('pszMdmComplianceUrl', win32more.Foundation.PWSTR),
        ('pszUserSettingSyncUrl', win32more.Foundation.PWSTR),
        ('pUserInfo', POINTER(win32more.NetworkManagement.NetManagement.DSREG_USER_INFO_head)),
    ]
    return DSREG_JOIN_INFO
DSREG_JOIN_TYPE = Int32
DSREG_UNKNOWN_JOIN = 0
DSREG_DEVICE_JOIN = 1
DSREG_WORKPLACE_JOIN = 2
def _define_DSREG_USER_INFO_head():
    class DSREG_USER_INFO(Structure):
        pass
    return DSREG_USER_INFO
def _define_DSREG_USER_INFO():
    DSREG_USER_INFO = win32more.NetworkManagement.NetManagement.DSREG_USER_INFO_head
    DSREG_USER_INFO._fields_ = [
        ('pszUserEmail', win32more.Foundation.PWSTR),
        ('pszUserKeyId', win32more.Foundation.PWSTR),
        ('pszUserKeyName', win32more.Foundation.PWSTR),
    ]
    return DSREG_USER_INFO
ENUM_BINDING_PATHS_FLAGS = Int32
EBP_ABOVE = 1
EBP_BELOW = 2
def _define_ERRLOG_OTHER_INFO_head():
    class ERRLOG_OTHER_INFO(Structure):
        pass
    return ERRLOG_OTHER_INFO
def _define_ERRLOG_OTHER_INFO():
    ERRLOG_OTHER_INFO = win32more.NetworkManagement.NetManagement.ERRLOG_OTHER_INFO_head
    ERRLOG_OTHER_INFO._fields_ = [
        ('alrter_errcode', UInt32),
        ('alrter_offset', UInt32),
    ]
    return ERRLOG_OTHER_INFO
def _define_ERROR_LOG_head():
    class ERROR_LOG(Structure):
        pass
    return ERROR_LOG
def _define_ERROR_LOG():
    ERROR_LOG = win32more.NetworkManagement.NetManagement.ERROR_LOG_head
    ERROR_LOG._fields_ = [
        ('el_len', UInt32),
        ('el_reserved', UInt32),
        ('el_time', UInt32),
        ('el_error', UInt32),
        ('el_name', win32more.Foundation.PWSTR),
        ('el_text', win32more.Foundation.PWSTR),
        ('el_data', c_char_p_no),
        ('el_data_size', UInt32),
        ('el_nstrings', UInt32),
    ]
    return ERROR_LOG
def _define_FLAT_STRING_head():
    class FLAT_STRING(Structure):
        pass
    return FLAT_STRING
def _define_FLAT_STRING():
    FLAT_STRING = win32more.NetworkManagement.NetManagement.FLAT_STRING_head
    FLAT_STRING._fields_ = [
        ('MaximumLength', Int16),
        ('Length', Int16),
        ('Buffer', win32more.Foundation.CHAR * 1),
    ]
    return FLAT_STRING
FORCE_LEVEL_FLAGS = UInt32
USE_NOFORCE = 0
USE_FORCE = 1
USE_LOTS_OF_FORCE = 2
def _define_GROUP_INFO_0_head():
    class GROUP_INFO_0(Structure):
        pass
    return GROUP_INFO_0
def _define_GROUP_INFO_0():
    GROUP_INFO_0 = win32more.NetworkManagement.NetManagement.GROUP_INFO_0_head
    GROUP_INFO_0._fields_ = [
        ('grpi0_name', win32more.Foundation.PWSTR),
    ]
    return GROUP_INFO_0
def _define_GROUP_INFO_1_head():
    class GROUP_INFO_1(Structure):
        pass
    return GROUP_INFO_1
def _define_GROUP_INFO_1():
    GROUP_INFO_1 = win32more.NetworkManagement.NetManagement.GROUP_INFO_1_head
    GROUP_INFO_1._fields_ = [
        ('grpi1_name', win32more.Foundation.PWSTR),
        ('grpi1_comment', win32more.Foundation.PWSTR),
    ]
    return GROUP_INFO_1
def _define_GROUP_INFO_1002_head():
    class GROUP_INFO_1002(Structure):
        pass
    return GROUP_INFO_1002
def _define_GROUP_INFO_1002():
    GROUP_INFO_1002 = win32more.NetworkManagement.NetManagement.GROUP_INFO_1002_head
    GROUP_INFO_1002._fields_ = [
        ('grpi1002_comment', win32more.Foundation.PWSTR),
    ]
    return GROUP_INFO_1002
def _define_GROUP_INFO_1005_head():
    class GROUP_INFO_1005(Structure):
        pass
    return GROUP_INFO_1005
def _define_GROUP_INFO_1005():
    GROUP_INFO_1005 = win32more.NetworkManagement.NetManagement.GROUP_INFO_1005_head
    GROUP_INFO_1005._fields_ = [
        ('grpi1005_attributes', UInt32),
    ]
    return GROUP_INFO_1005
def _define_GROUP_INFO_2_head():
    class GROUP_INFO_2(Structure):
        pass
    return GROUP_INFO_2
def _define_GROUP_INFO_2():
    GROUP_INFO_2 = win32more.NetworkManagement.NetManagement.GROUP_INFO_2_head
    GROUP_INFO_2._fields_ = [
        ('grpi2_name', win32more.Foundation.PWSTR),
        ('grpi2_comment', win32more.Foundation.PWSTR),
        ('grpi2_group_id', UInt32),
        ('grpi2_attributes', UInt32),
    ]
    return GROUP_INFO_2
def _define_GROUP_INFO_3_head():
    class GROUP_INFO_3(Structure):
        pass
    return GROUP_INFO_3
def _define_GROUP_INFO_3():
    GROUP_INFO_3 = win32more.NetworkManagement.NetManagement.GROUP_INFO_3_head
    GROUP_INFO_3._fields_ = [
        ('grpi3_name', win32more.Foundation.PWSTR),
        ('grpi3_comment', win32more.Foundation.PWSTR),
        ('grpi3_group_sid', win32more.Foundation.PSID),
        ('grpi3_attributes', UInt32),
    ]
    return GROUP_INFO_3
def _define_GROUP_USERS_INFO_0_head():
    class GROUP_USERS_INFO_0(Structure):
        pass
    return GROUP_USERS_INFO_0
def _define_GROUP_USERS_INFO_0():
    GROUP_USERS_INFO_0 = win32more.NetworkManagement.NetManagement.GROUP_USERS_INFO_0_head
    GROUP_USERS_INFO_0._fields_ = [
        ('grui0_name', win32more.Foundation.PWSTR),
    ]
    return GROUP_USERS_INFO_0
def _define_GROUP_USERS_INFO_1_head():
    class GROUP_USERS_INFO_1(Structure):
        pass
    return GROUP_USERS_INFO_1
def _define_GROUP_USERS_INFO_1():
    GROUP_USERS_INFO_1 = win32more.NetworkManagement.NetManagement.GROUP_USERS_INFO_1_head
    GROUP_USERS_INFO_1._fields_ = [
        ('grui1_name', win32more.Foundation.PWSTR),
        ('grui1_attributes', UInt32),
    ]
    return GROUP_USERS_INFO_1
def _define_HARDWARE_ADDRESS_head():
    class HARDWARE_ADDRESS(Structure):
        pass
    return HARDWARE_ADDRESS
def _define_HARDWARE_ADDRESS():
    HARDWARE_ADDRESS = win32more.NetworkManagement.NetManagement.HARDWARE_ADDRESS_head
    HARDWARE_ADDRESS._fields_ = [
        ('Address', Byte * 6),
    ]
    return HARDWARE_ADDRESS
def _define_HLOG_head():
    class HLOG(Structure):
        pass
    return HLOG
def _define_HLOG():
    HLOG = win32more.NetworkManagement.NetManagement.HLOG_head
    HLOG._fields_ = [
        ('time', UInt32),
        ('last_flags', UInt32),
        ('offset', UInt32),
        ('rec_offset', UInt32),
    ]
    return HLOG
def _define_IEnumNetCfgBindingInterface_head():
    class IEnumNetCfgBindingInterface(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae90-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return IEnumNetCfgBindingInterface
def _define_IEnumNetCfgBindingInterface():
    IEnumNetCfgBindingInterface = win32more.NetworkManagement.NetManagement.IEnumNetCfgBindingInterface_head
    IEnumNetCfgBindingInterface.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.NetworkManagement.NetManagement.INetCfgBindingInterface_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumNetCfgBindingInterface.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetCfgBindingInterface.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumNetCfgBindingInterface.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgBindingInterface_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumNetCfgBindingInterface
def _define_IEnumNetCfgBindingPath_head():
    class IEnumNetCfgBindingPath(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae91-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return IEnumNetCfgBindingPath
def _define_IEnumNetCfgBindingPath():
    IEnumNetCfgBindingPath = win32more.NetworkManagement.NetManagement.IEnumNetCfgBindingPath_head
    IEnumNetCfgBindingPath.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumNetCfgBindingPath.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetCfgBindingPath.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumNetCfgBindingPath.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgBindingPath_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumNetCfgBindingPath
def _define_IEnumNetCfgComponent_head():
    class IEnumNetCfgComponent(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae92-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return IEnumNetCfgComponent
def _define_IEnumNetCfgComponent():
    IEnumNetCfgComponent = win32more.NetworkManagement.NetManagement.IEnumNetCfgComponent_head
    IEnumNetCfgComponent.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumNetCfgComponent.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetCfgComponent.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumNetCfgComponent.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgComponent_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumNetCfgComponent
def _define_INetCfg_head():
    class INetCfg(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae93-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return INetCfg
def _define_INetCfg():
    INetCfg = win32more.NetworkManagement.NetManagement.INetCfg_head
    INetCfg.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(3, 'Initialize', ((1, 'pvReserved'),)))
    INetCfg.Uninitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Uninitialize', ()))
    INetCfg.Apply = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Apply', ()))
    INetCfg.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Cancel', ()))
    INetCfg.EnumComponents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgComponent_head))(7, 'EnumComponents', ((1, 'pguidClass'),(1, 'ppenumComponent'),)))
    INetCfg.FindComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head))(8, 'FindComponent', ((1, 'pszwInfId'),(1, 'pComponent'),)))
    INetCfg.QueryNetCfgClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(c_void_p))(9, 'QueryNetCfgClass', ((1, 'pguidClass'),(1, 'riid'),(1, 'ppvObject'),)))
    win32more.System.Com.IUnknown
    return INetCfg
def _define_INetCfgBindingInterface_head():
    class INetCfgBindingInterface(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae94-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return INetCfgBindingInterface
def _define_INetCfgBindingInterface():
    INetCfgBindingInterface = win32more.NetworkManagement.NetManagement.INetCfgBindingInterface_head
    INetCfgBindingInterface.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(3, 'GetName', ((1, 'ppszwInterfaceName'),)))
    INetCfgBindingInterface.GetUpperComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head))(4, 'GetUpperComponent', ((1, 'ppnccItem'),)))
    INetCfgBindingInterface.GetLowerComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head))(5, 'GetLowerComponent', ((1, 'ppnccItem'),)))
    win32more.System.Com.IUnknown
    return INetCfgBindingInterface
def _define_INetCfgBindingPath_head():
    class INetCfgBindingPath(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae96-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return INetCfgBindingPath
def _define_INetCfgBindingPath():
    INetCfgBindingPath = win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head
    INetCfgBindingPath.IsSamePathAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head)(3, 'IsSamePathAs', ((1, 'pPath'),)))
    INetCfgBindingPath.IsSubPathOf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head)(4, 'IsSubPathOf', ((1, 'pPath'),)))
    INetCfgBindingPath.IsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'IsEnabled', ()))
    INetCfgBindingPath.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(6, 'Enable', ((1, 'fEnable'),)))
    INetCfgBindingPath.GetPathToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'GetPathToken', ((1, 'ppszwPathToken'),)))
    INetCfgBindingPath.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head))(8, 'GetOwner', ((1, 'ppComponent'),)))
    INetCfgBindingPath.GetDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'GetDepth', ((1, 'pcInterfaces'),)))
    INetCfgBindingPath.EnumBindingInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgBindingInterface_head))(10, 'EnumBindingInterfaces', ((1, 'ppenumInterface'),)))
    win32more.System.Com.IUnknown
    return INetCfgBindingPath
def _define_INetCfgClass_head():
    class INetCfgClass(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae97-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return INetCfgClass
def _define_INetCfgClass():
    INetCfgClass = win32more.NetworkManagement.NetManagement.INetCfgClass_head
    INetCfgClass.FindComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head))(3, 'FindComponent', ((1, 'pszwInfId'),(1, 'ppnccItem'),)))
    INetCfgClass.EnumComponents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgComponent_head))(4, 'EnumComponents', ((1, 'ppenumComponent'),)))
    win32more.System.Com.IUnknown
    return INetCfgClass
def _define_INetCfgClassSetup_head():
    class INetCfgClassSetup(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae9d-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return INetCfgClassSetup
def _define_INetCfgClassSetup():
    INetCfgClassSetup = win32more.NetworkManagement.NetManagement.INetCfgClassSetup_head
    INetCfgClassSetup.SelectAndInstall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.NetManagement.OBO_TOKEN_head),POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head))(3, 'SelectAndInstall', ((1, 'hwndParent'),(1, 'pOboToken'),(1, 'ppnccItem'),)))
    INetCfgClassSetup.Install = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.NetManagement.OBO_TOKEN_head),UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head))(4, 'Install', ((1, 'pszwInfId'),(1, 'pOboToken'),(1, 'dwSetupFlags'),(1, 'dwUpgradeFromBuildNo'),(1, 'pszwAnswerFile'),(1, 'pszwAnswerSections'),(1, 'ppnccItem'),)))
    INetCfgClassSetup.DeInstall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgComponent_head,POINTER(win32more.NetworkManagement.NetManagement.OBO_TOKEN_head),POINTER(win32more.Foundation.PWSTR))(5, 'DeInstall', ((1, 'pComponent'),(1, 'pOboToken'),(1, 'pmszwRefs'),)))
    win32more.System.Com.IUnknown
    return INetCfgClassSetup
def _define_INetCfgClassSetup2_head():
    class INetCfgClassSetup2(win32more.NetworkManagement.NetManagement.INetCfgClassSetup_head):
        Guid = Guid('c0e8aea0-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return INetCfgClassSetup2
def _define_INetCfgClassSetup2():
    INetCfgClassSetup2 = win32more.NetworkManagement.NetManagement.INetCfgClassSetup2_head
    INetCfgClassSetup2.UpdateNonEnumeratedComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgComponent_head,UInt32,UInt32)(6, 'UpdateNonEnumeratedComponent', ((1, 'pIComp'),(1, 'dwSetupFlags'),(1, 'dwUpgradeFromBuildNo'),)))
    win32more.NetworkManagement.NetManagement.INetCfgClassSetup
    return INetCfgClassSetup2
def _define_INetCfgComponent_head():
    class INetCfgComponent(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae99-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return INetCfgComponent
def _define_INetCfgComponent():
    INetCfgComponent = win32more.NetworkManagement.NetManagement.INetCfgComponent_head
    INetCfgComponent.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(3, 'GetDisplayName', ((1, 'ppszwDisplayName'),)))
    INetCfgComponent.SetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(4, 'SetDisplayName', ((1, 'pszwDisplayName'),)))
    INetCfgComponent.GetHelpText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(5, 'GetHelpText', ((1, 'pszwHelpText'),)))
    INetCfgComponent.GetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(6, 'GetId', ((1, 'ppszwId'),)))
    INetCfgComponent.GetCharacteristics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(7, 'GetCharacteristics', ((1, 'pdwCharacteristics'),)))
    INetCfgComponent.GetInstanceGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(8, 'GetInstanceGuid', ((1, 'pGuid'),)))
    INetCfgComponent.GetPnpDevNodeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(9, 'GetPnpDevNodeId', ((1, 'ppszwDevNodeId'),)))
    INetCfgComponent.GetClassGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(10, 'GetClassGuid', ((1, 'pGuid'),)))
    INetCfgComponent.GetBindName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(11, 'GetBindName', ((1, 'ppszwBindName'),)))
    INetCfgComponent.GetDeviceStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'GetDeviceStatus', ((1, 'pulStatus'),)))
    INetCfgComponent.OpenParamKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Registry.HKEY))(13, 'OpenParamKey', ((1, 'phkey'),)))
    INetCfgComponent.RaisePropertyUi = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.System.Com.IUnknown_head)(14, 'RaisePropertyUi', ((1, 'hwndParent'),(1, 'dwFlags'),(1, 'punkContext'),)))
    win32more.System.Com.IUnknown
    return INetCfgComponent
def _define_INetCfgComponentBindings_head():
    class INetCfgComponentBindings(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae9e-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return INetCfgComponentBindings
def _define_INetCfgComponentBindings():
    INetCfgComponentBindings = win32more.NetworkManagement.NetManagement.INetCfgComponentBindings_head
    INetCfgComponentBindings.BindTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgComponent_head)(3, 'BindTo', ((1, 'pnccItem'),)))
    INetCfgComponentBindings.UnbindFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgComponent_head)(4, 'UnbindFrom', ((1, 'pnccItem'),)))
    INetCfgComponentBindings.SupportsBindingInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR)(5, 'SupportsBindingInterface', ((1, 'dwFlags'),(1, 'pszwInterfaceName'),)))
    INetCfgComponentBindings.IsBoundTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgComponent_head)(6, 'IsBoundTo', ((1, 'pnccItem'),)))
    INetCfgComponentBindings.IsBindableTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgComponent_head)(7, 'IsBindableTo', ((1, 'pnccItem'),)))
    INetCfgComponentBindings.EnumBindingPaths = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgBindingPath_head))(8, 'EnumBindingPaths', ((1, 'dwFlags'),(1, 'ppIEnum'),)))
    INetCfgComponentBindings.MoveBefore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head,win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head)(9, 'MoveBefore', ((1, 'pncbItemSrc'),(1, 'pncbItemDest'),)))
    INetCfgComponentBindings.MoveAfter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head,win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head)(10, 'MoveAfter', ((1, 'pncbItemSrc'),(1, 'pncbItemDest'),)))
    win32more.System.Com.IUnknown
    return INetCfgComponentBindings
def _define_INetCfgComponentControl_head():
    class INetCfgComponentControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('932238df-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    return INetCfgComponentControl
def _define_INetCfgComponentControl():
    INetCfgComponentControl = win32more.NetworkManagement.NetManagement.INetCfgComponentControl_head
    INetCfgComponentControl.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgComponent_head,win32more.NetworkManagement.NetManagement.INetCfg_head,win32more.Foundation.BOOL)(3, 'Initialize', ((1, 'pIComp'),(1, 'pINetCfg'),(1, 'fInstalling'),)))
    INetCfgComponentControl.ApplyRegistryChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'ApplyRegistryChanges', ()))
    INetCfgComponentControl.ApplyPnpChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgPnpReconfigCallback_head)(5, 'ApplyPnpChanges', ((1, 'pICallback'),)))
    INetCfgComponentControl.CancelChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'CancelChanges', ()))
    win32more.System.Com.IUnknown
    return INetCfgComponentControl
def _define_INetCfgComponentNotifyBinding_head():
    class INetCfgComponentNotifyBinding(win32more.System.Com.IUnknown_head):
        Guid = Guid('932238e1-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    return INetCfgComponentNotifyBinding
def _define_INetCfgComponentNotifyBinding():
    INetCfgComponentNotifyBinding = win32more.NetworkManagement.NetManagement.INetCfgComponentNotifyBinding_head
    INetCfgComponentNotifyBinding.QueryBindingPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head)(3, 'QueryBindingPath', ((1, 'dwChangeFlag'),(1, 'pIPath'),)))
    INetCfgComponentNotifyBinding.NotifyBindingPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head)(4, 'NotifyBindingPath', ((1, 'dwChangeFlag'),(1, 'pIPath'),)))
    win32more.System.Com.IUnknown
    return INetCfgComponentNotifyBinding
def _define_INetCfgComponentNotifyGlobal_head():
    class INetCfgComponentNotifyGlobal(win32more.System.Com.IUnknown_head):
        Guid = Guid('932238e2-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    return INetCfgComponentNotifyGlobal
def _define_INetCfgComponentNotifyGlobal():
    INetCfgComponentNotifyGlobal = win32more.NetworkManagement.NetManagement.INetCfgComponentNotifyGlobal_head
    INetCfgComponentNotifyGlobal.GetSupportedNotifications = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetSupportedNotifications', ((1, 'dwNotifications'),)))
    INetCfgComponentNotifyGlobal.SysQueryBindingPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head)(4, 'SysQueryBindingPath', ((1, 'dwChangeFlag'),(1, 'pIPath'),)))
    INetCfgComponentNotifyGlobal.SysNotifyBindingPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head)(5, 'SysNotifyBindingPath', ((1, 'dwChangeFlag'),(1, 'pIPath'),)))
    INetCfgComponentNotifyGlobal.SysNotifyComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.NetworkManagement.NetManagement.INetCfgComponent_head)(6, 'SysNotifyComponent', ((1, 'dwChangeFlag'),(1, 'pIComp'),)))
    win32more.System.Com.IUnknown
    return INetCfgComponentNotifyGlobal
def _define_INetCfgComponentPropertyUi_head():
    class INetCfgComponentPropertyUi(win32more.System.Com.IUnknown_head):
        Guid = Guid('932238e0-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    return INetCfgComponentPropertyUi
def _define_INetCfgComponentPropertyUi():
    INetCfgComponentPropertyUi = win32more.NetworkManagement.NetManagement.INetCfgComponentPropertyUi_head
    INetCfgComponentPropertyUi.QueryPropertyUi = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(3, 'QueryPropertyUi', ((1, 'pUnkReserved'),)))
    INetCfgComponentPropertyUi.SetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(4, 'SetContext', ((1, 'pUnkReserved'),)))
    INetCfgComponentPropertyUi.MergePropPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(c_char_p_no),POINTER(UInt32),win32more.Foundation.HWND,POINTER(win32more.Foundation.PWSTR))(5, 'MergePropPages', ((1, 'pdwDefPages'),(1, 'pahpspPrivate'),(1, 'pcPages'),(1, 'hwndParent'),(1, 'pszStartPage'),)))
    INetCfgComponentPropertyUi.ValidateProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND)(6, 'ValidateProperties', ((1, 'hwndSheet'),)))
    INetCfgComponentPropertyUi.ApplyProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'ApplyProperties', ()))
    INetCfgComponentPropertyUi.CancelProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'CancelProperties', ()))
    win32more.System.Com.IUnknown
    return INetCfgComponentPropertyUi
def _define_INetCfgComponentSetup_head():
    class INetCfgComponentSetup(win32more.System.Com.IUnknown_head):
        Guid = Guid('932238e3-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    return INetCfgComponentSetup
def _define_INetCfgComponentSetup():
    INetCfgComponentSetup = win32more.NetworkManagement.NetManagement.INetCfgComponentSetup_head
    INetCfgComponentSetup.Install = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'Install', ((1, 'dwSetupFlags'),)))
    INetCfgComponentSetup.Upgrade = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(4, 'Upgrade', ((1, 'dwSetupFlags'),(1, 'dwUpgradeFomBuildNo'),)))
    INetCfgComponentSetup.ReadAnswerFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(5, 'ReadAnswerFile', ((1, 'pszwAnswerFile'),(1, 'pszwAnswerSections'),)))
    INetCfgComponentSetup.Removing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Removing', ()))
    win32more.System.Com.IUnknown
    return INetCfgComponentSetup
def _define_INetCfgComponentSysPrep_head():
    class INetCfgComponentSysPrep(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae9a-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return INetCfgComponentSysPrep
def _define_INetCfgComponentSysPrep():
    INetCfgComponentSysPrep = win32more.NetworkManagement.NetManagement.INetCfgComponentSysPrep_head
    INetCfgComponentSysPrep.SaveAdapterParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgSysPrep_head,win32more.Foundation.PWSTR,POINTER(Guid))(3, 'SaveAdapterParameters', ((1, 'pncsp'),(1, 'pszwAnswerSections'),(1, 'pAdapterInstanceGuid'),)))
    INetCfgComponentSysPrep.RestoreAdapterParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid))(4, 'RestoreAdapterParameters', ((1, 'pszwAnswerFile'),(1, 'pszwAnswerSection'),(1, 'pAdapterInstanceGuid'),)))
    win32more.System.Com.IUnknown
    return INetCfgComponentSysPrep
def _define_INetCfgComponentUpperEdge_head():
    class INetCfgComponentUpperEdge(win32more.System.Com.IUnknown_head):
        Guid = Guid('932238e4-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    return INetCfgComponentUpperEdge
def _define_INetCfgComponentUpperEdge():
    INetCfgComponentUpperEdge = win32more.NetworkManagement.NetManagement.INetCfgComponentUpperEdge_head
    INetCfgComponentUpperEdge.GetInterfaceIdsForAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgComponent_head,POINTER(UInt32),POINTER(POINTER(Guid)))(3, 'GetInterfaceIdsForAdapter', ((1, 'pAdapter'),(1, 'pdwNumInterfaces'),(1, 'ppguidInterfaceIds'),)))
    INetCfgComponentUpperEdge.AddInterfacesToAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgComponent_head,UInt32)(4, 'AddInterfacesToAdapter', ((1, 'pAdapter'),(1, 'dwNumInterfaces'),)))
    INetCfgComponentUpperEdge.RemoveInterfacesFromAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.INetCfgComponent_head,UInt32,POINTER(Guid))(5, 'RemoveInterfacesFromAdapter', ((1, 'pAdapter'),(1, 'dwNumInterfaces'),(1, 'pguidInterfaceIds'),)))
    win32more.System.Com.IUnknown
    return INetCfgComponentUpperEdge
def _define_INetCfgLock_head():
    class INetCfgLock(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae9f-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return INetCfgLock
def _define_INetCfgLock():
    INetCfgLock = win32more.NetworkManagement.NetManagement.INetCfgLock_head
    INetCfgLock.AcquireWriteLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(3, 'AcquireWriteLock', ((1, 'cmsTimeout'),(1, 'pszwClientDescription'),(1, 'ppszwClientDescription'),)))
    INetCfgLock.ReleaseWriteLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'ReleaseWriteLock', ()))
    INetCfgLock.IsWriteLocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(5, 'IsWriteLocked', ((1, 'ppszwClientDescription'),)))
    win32more.System.Com.IUnknown
    return INetCfgLock
def _define_INetCfgPnpReconfigCallback_head():
    class INetCfgPnpReconfigCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('8d84bd35-e227-11d2-b7-00-00-a0-c9-8a-6a-85')
    return INetCfgPnpReconfigCallback
def _define_INetCfgPnpReconfigCallback():
    INetCfgPnpReconfigCallback = win32more.NetworkManagement.NetManagement.INetCfgPnpReconfigCallback_head
    INetCfgPnpReconfigCallback.SendPnpReconfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetManagement.NCPNP_RECONFIG_LAYER,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32)(3, 'SendPnpReconfig', ((1, 'Layer'),(1, 'pszwUpper'),(1, 'pszwLower'),(1, 'pvData'),(1, 'dwSizeOfData'),)))
    win32more.System.Com.IUnknown
    return INetCfgPnpReconfigCallback
def _define_INetCfgSysPrep_head():
    class INetCfgSysPrep(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0e8ae98-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    return INetCfgSysPrep
def _define_INetCfgSysPrep():
    INetCfgSysPrep = win32more.NetworkManagement.NetManagement.INetCfgSysPrep_head
    INetCfgSysPrep.HrSetupSetFirstDword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(3, 'HrSetupSetFirstDword', ((1, 'pwszSection'),(1, 'pwszKey'),(1, 'dwValue'),)))
    INetCfgSysPrep.HrSetupSetFirstString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(4, 'HrSetupSetFirstString', ((1, 'pwszSection'),(1, 'pwszKey'),(1, 'pwszValue'),)))
    INetCfgSysPrep.HrSetupSetFirstStringAsBool = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(5, 'HrSetupSetFirstStringAsBool', ((1, 'pwszSection'),(1, 'pwszKey'),(1, 'fValue'),)))
    INetCfgSysPrep.HrSetupSetFirstMultiSzField = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(6, 'HrSetupSetFirstMultiSzField', ((1, 'pwszSection'),(1, 'pwszKey'),(1, 'pmszValue'),)))
    win32more.System.Com.IUnknown
    return INetCfgSysPrep
def _define_INetLanConnectionUiInfo_head():
    class INetLanConnectionUiInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956a6-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return INetLanConnectionUiInfo
def _define_INetLanConnectionUiInfo():
    INetLanConnectionUiInfo = win32more.NetworkManagement.NetManagement.INetLanConnectionUiInfo_head
    INetLanConnectionUiInfo.GetDeviceGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetDeviceGuid', ((1, 'pguid'),)))
    win32more.System.Com.IUnknown
    return INetLanConnectionUiInfo
def _define_INetRasConnectionIpUiInfo_head():
    class INetRasConnectionIpUiInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('faedcf58-31fe-11d1-aa-d2-00-80-5f-c1-27-0e')
    return INetRasConnectionIpUiInfo
def _define_INetRasConnectionIpUiInfo():
    INetRasConnectionIpUiInfo = win32more.NetworkManagement.NetManagement.INetRasConnectionIpUiInfo_head
    INetRasConnectionIpUiInfo.GetUiInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.NetManagement.RASCON_IPUI_head))(3, 'GetUiInfo', ((1, 'pInfo'),)))
    win32more.System.Com.IUnknown
    return INetRasConnectionIpUiInfo
def _define_IProvisioningDomain_head():
    class IProvisioningDomain(win32more.System.Com.IUnknown_head):
        Guid = Guid('c96fbd50-24dd-11d8-89-fb-00-90-4b-2e-a9-c6')
    return IProvisioningDomain
def _define_IProvisioningDomain():
    IProvisioningDomain = win32more.NetworkManagement.NetManagement.IProvisioningDomain_head
    IProvisioningDomain.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'Add', ((1, 'pszwPathToFolder'),)))
    IProvisioningDomain.Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Data.Xml.MsXml.IXMLDOMNodeList_head))(4, 'Query', ((1, 'pszwDomain'),(1, 'pszwLanguage'),(1, 'pszwXPathQuery'),(1, 'Nodes'),)))
    win32more.System.Com.IUnknown
    return IProvisioningDomain
def _define_IProvisioningProfileWireless_head():
    class IProvisioningProfileWireless(win32more.System.Com.IUnknown_head):
        Guid = Guid('c96fbd51-24dd-11d8-89-fb-00-90-4b-2e-a9-c6')
    return IProvisioningProfileWireless
def _define_IProvisioningProfileWireless():
    IProvisioningProfileWireless = win32more.NetworkManagement.NetManagement.IProvisioningProfileWireless_head
    IProvisioningProfileWireless.CreateProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Guid),POINTER(UInt32))(3, 'CreateProfile', ((1, 'bstrXMLWirelessConfigProfile'),(1, 'bstrXMLConnectionConfigProfile'),(1, 'pAdapterInstanceGuid'),(1, 'pulStatus'),)))
    win32more.System.Com.IUnknown
    return IProvisioningProfileWireless
def _define_LOCALGROUP_INFO_0_head():
    class LOCALGROUP_INFO_0(Structure):
        pass
    return LOCALGROUP_INFO_0
def _define_LOCALGROUP_INFO_0():
    LOCALGROUP_INFO_0 = win32more.NetworkManagement.NetManagement.LOCALGROUP_INFO_0_head
    LOCALGROUP_INFO_0._fields_ = [
        ('lgrpi0_name', win32more.Foundation.PWSTR),
    ]
    return LOCALGROUP_INFO_0
def _define_LOCALGROUP_INFO_1_head():
    class LOCALGROUP_INFO_1(Structure):
        pass
    return LOCALGROUP_INFO_1
def _define_LOCALGROUP_INFO_1():
    LOCALGROUP_INFO_1 = win32more.NetworkManagement.NetManagement.LOCALGROUP_INFO_1_head
    LOCALGROUP_INFO_1._fields_ = [
        ('lgrpi1_name', win32more.Foundation.PWSTR),
        ('lgrpi1_comment', win32more.Foundation.PWSTR),
    ]
    return LOCALGROUP_INFO_1
def _define_LOCALGROUP_INFO_1002_head():
    class LOCALGROUP_INFO_1002(Structure):
        pass
    return LOCALGROUP_INFO_1002
def _define_LOCALGROUP_INFO_1002():
    LOCALGROUP_INFO_1002 = win32more.NetworkManagement.NetManagement.LOCALGROUP_INFO_1002_head
    LOCALGROUP_INFO_1002._fields_ = [
        ('lgrpi1002_comment', win32more.Foundation.PWSTR),
    ]
    return LOCALGROUP_INFO_1002
def _define_LOCALGROUP_MEMBERS_INFO_0_head():
    class LOCALGROUP_MEMBERS_INFO_0(Structure):
        pass
    return LOCALGROUP_MEMBERS_INFO_0
def _define_LOCALGROUP_MEMBERS_INFO_0():
    LOCALGROUP_MEMBERS_INFO_0 = win32more.NetworkManagement.NetManagement.LOCALGROUP_MEMBERS_INFO_0_head
    LOCALGROUP_MEMBERS_INFO_0._fields_ = [
        ('lgrmi0_sid', win32more.Foundation.PSID),
    ]
    return LOCALGROUP_MEMBERS_INFO_0
def _define_LOCALGROUP_MEMBERS_INFO_1_head():
    class LOCALGROUP_MEMBERS_INFO_1(Structure):
        pass
    return LOCALGROUP_MEMBERS_INFO_1
def _define_LOCALGROUP_MEMBERS_INFO_1():
    LOCALGROUP_MEMBERS_INFO_1 = win32more.NetworkManagement.NetManagement.LOCALGROUP_MEMBERS_INFO_1_head
    LOCALGROUP_MEMBERS_INFO_1._fields_ = [
        ('lgrmi1_sid', win32more.Foundation.PSID),
        ('lgrmi1_sidusage', win32more.Security.SID_NAME_USE),
        ('lgrmi1_name', win32more.Foundation.PWSTR),
    ]
    return LOCALGROUP_MEMBERS_INFO_1
def _define_LOCALGROUP_MEMBERS_INFO_2_head():
    class LOCALGROUP_MEMBERS_INFO_2(Structure):
        pass
    return LOCALGROUP_MEMBERS_INFO_2
def _define_LOCALGROUP_MEMBERS_INFO_2():
    LOCALGROUP_MEMBERS_INFO_2 = win32more.NetworkManagement.NetManagement.LOCALGROUP_MEMBERS_INFO_2_head
    LOCALGROUP_MEMBERS_INFO_2._fields_ = [
        ('lgrmi2_sid', win32more.Foundation.PSID),
        ('lgrmi2_sidusage', win32more.Security.SID_NAME_USE),
        ('lgrmi2_domainandname', win32more.Foundation.PWSTR),
    ]
    return LOCALGROUP_MEMBERS_INFO_2
def _define_LOCALGROUP_MEMBERS_INFO_3_head():
    class LOCALGROUP_MEMBERS_INFO_3(Structure):
        pass
    return LOCALGROUP_MEMBERS_INFO_3
def _define_LOCALGROUP_MEMBERS_INFO_3():
    LOCALGROUP_MEMBERS_INFO_3 = win32more.NetworkManagement.NetManagement.LOCALGROUP_MEMBERS_INFO_3_head
    LOCALGROUP_MEMBERS_INFO_3._fields_ = [
        ('lgrmi3_domainandname', win32more.Foundation.PWSTR),
    ]
    return LOCALGROUP_MEMBERS_INFO_3
def _define_LOCALGROUP_USERS_INFO_0_head():
    class LOCALGROUP_USERS_INFO_0(Structure):
        pass
    return LOCALGROUP_USERS_INFO_0
def _define_LOCALGROUP_USERS_INFO_0():
    LOCALGROUP_USERS_INFO_0 = win32more.NetworkManagement.NetManagement.LOCALGROUP_USERS_INFO_0_head
    LOCALGROUP_USERS_INFO_0._fields_ = [
        ('lgrui0_name', win32more.Foundation.PWSTR),
    ]
    return LOCALGROUP_USERS_INFO_0
def _define_MPR_PROTOCOL_0_head():
    class MPR_PROTOCOL_0(Structure):
        pass
    return MPR_PROTOCOL_0
def _define_MPR_PROTOCOL_0():
    MPR_PROTOCOL_0 = win32more.NetworkManagement.NetManagement.MPR_PROTOCOL_0_head
    MPR_PROTOCOL_0._fields_ = [
        ('dwProtocolId', UInt32),
        ('wszProtocol', Char * 41),
        ('wszDLLName', Char * 49),
    ]
    return MPR_PROTOCOL_0
def _define_MSA_INFO_0_head():
    class MSA_INFO_0(Structure):
        pass
    return MSA_INFO_0
def _define_MSA_INFO_0():
    MSA_INFO_0 = win32more.NetworkManagement.NetManagement.MSA_INFO_0_head
    MSA_INFO_0._fields_ = [
        ('State', win32more.NetworkManagement.NetManagement.MSA_INFO_STATE),
    ]
    return MSA_INFO_0
MSA_INFO_LEVEL = Int32
MSA_INFO_LEVEL_MsaInfoLevel0 = 0
MSA_INFO_LEVEL_MsaInfoLevelMax = 1
MSA_INFO_STATE = Int32
MSA_INFO_STATE_MsaInfoNotExist = 1
MSA_INFO_STATE_MsaInfoNotService = 2
MSA_INFO_STATE_MsaInfoCannotInstall = 3
MSA_INFO_STATE_MsaInfoCanInstall = 4
MSA_INFO_STATE_MsaInfoInstalled = 5
def _define_MSG_INFO_0_head():
    class MSG_INFO_0(Structure):
        pass
    return MSG_INFO_0
def _define_MSG_INFO_0():
    MSG_INFO_0 = win32more.NetworkManagement.NetManagement.MSG_INFO_0_head
    MSG_INFO_0._fields_ = [
        ('msgi0_name', win32more.Foundation.PWSTR),
    ]
    return MSG_INFO_0
def _define_MSG_INFO_1_head():
    class MSG_INFO_1(Structure):
        pass
    return MSG_INFO_1
def _define_MSG_INFO_1():
    MSG_INFO_1 = win32more.NetworkManagement.NetManagement.MSG_INFO_1_head
    MSG_INFO_1._fields_ = [
        ('msgi1_name', win32more.Foundation.PWSTR),
        ('msgi1_forward_flag', UInt32),
        ('msgi1_forward', win32more.Foundation.PWSTR),
    ]
    return MSG_INFO_1
NCPNP_RECONFIG_LAYER = Int32
NCRL_NDIS = 1
NCRL_TDI = 2
NCRP_FLAGS = Int32
NCRP_QUERY_PROPERTY_UI = 1
NCRP_SHOW_PROPERTY_UI = 2
NET_COMPUTER_NAME_TYPE = Int32
NET_COMPUTER_NAME_TYPE_NetPrimaryComputerName = 0
NET_COMPUTER_NAME_TYPE_NetAlternateComputerNames = 1
NET_COMPUTER_NAME_TYPE_NetAllComputerNames = 2
NET_COMPUTER_NAME_TYPE_NetComputerNameTypeMax = 3
def _define_NET_DISPLAY_GROUP_head():
    class NET_DISPLAY_GROUP(Structure):
        pass
    return NET_DISPLAY_GROUP
def _define_NET_DISPLAY_GROUP():
    NET_DISPLAY_GROUP = win32more.NetworkManagement.NetManagement.NET_DISPLAY_GROUP_head
    NET_DISPLAY_GROUP._fields_ = [
        ('grpi3_name', win32more.Foundation.PWSTR),
        ('grpi3_comment', win32more.Foundation.PWSTR),
        ('grpi3_group_id', UInt32),
        ('grpi3_attributes', UInt32),
        ('grpi3_next_index', UInt32),
    ]
    return NET_DISPLAY_GROUP
def _define_NET_DISPLAY_MACHINE_head():
    class NET_DISPLAY_MACHINE(Structure):
        pass
    return NET_DISPLAY_MACHINE
def _define_NET_DISPLAY_MACHINE():
    NET_DISPLAY_MACHINE = win32more.NetworkManagement.NetManagement.NET_DISPLAY_MACHINE_head
    NET_DISPLAY_MACHINE._fields_ = [
        ('usri2_name', win32more.Foundation.PWSTR),
        ('usri2_comment', win32more.Foundation.PWSTR),
        ('usri2_flags', win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS),
        ('usri2_user_id', UInt32),
        ('usri2_next_index', UInt32),
    ]
    return NET_DISPLAY_MACHINE
def _define_NET_DISPLAY_USER_head():
    class NET_DISPLAY_USER(Structure):
        pass
    return NET_DISPLAY_USER
def _define_NET_DISPLAY_USER():
    NET_DISPLAY_USER = win32more.NetworkManagement.NetManagement.NET_DISPLAY_USER_head
    NET_DISPLAY_USER._fields_ = [
        ('usri1_name', win32more.Foundation.PWSTR),
        ('usri1_comment', win32more.Foundation.PWSTR),
        ('usri1_flags', win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS),
        ('usri1_full_name', win32more.Foundation.PWSTR),
        ('usri1_user_id', UInt32),
        ('usri1_next_index', UInt32),
    ]
    return NET_DISPLAY_USER
NET_JOIN_DOMAIN_JOIN_OPTIONS = UInt32
NETSETUP_JOIN_DOMAIN = 1
NETSETUP_ACCT_CREATE = 2
NETSETUP_WIN9X_UPGRADE = 16
NETSETUP_DOMAIN_JOIN_IF_JOINED = 32
NETSETUP_JOIN_UNSECURE = 64
NETSETUP_MACHINE_PWD_PASSED = 128
NETSETUP_DEFER_SPN_SET = 256
NETSETUP_JOIN_DC_ACCOUNT = 512
NETSETUP_JOIN_WITH_NEW_NAME = 1024
NETSETUP_JOIN_READONLY = 2048
NETSETUP_AMBIGUOUS_DC = 4096
NETSETUP_NO_NETLOGON_CACHE = 8192
NETSETUP_DONT_CONTROL_SERVICES = 16384
NETSETUP_SET_MACHINE_NAME = 32768
NETSETUP_FORCE_SPN_SET = 65536
NETSETUP_NO_ACCT_REUSE = 131072
NETSETUP_IGNORE_UNSUPPORTED_FLAGS = 268435456
NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = Int32
SUPPORTS_REMOTE_ADMIN_PROTOCOL = 2
SUPPORTS_RPC = 4
SUPPORTS_SAM_PROTOCOL = 8
SUPPORTS_UNICODE = 16
SUPPORTS_LOCAL = 32
NET_REQUEST_PROVISION_OPTIONS = UInt32
NETSETUP_PROVISION_ONLINE_CALLER = 1073741824
NET_SERVER_TYPE = UInt32
SV_TYPE_WORKSTATION = 1
SV_TYPE_SERVER = 2
SV_TYPE_SQLSERVER = 4
SV_TYPE_DOMAIN_CTRL = 8
SV_TYPE_DOMAIN_BAKCTRL = 16
SV_TYPE_TIME_SOURCE = 32
SV_TYPE_AFP = 64
SV_TYPE_NOVELL = 128
SV_TYPE_DOMAIN_MEMBER = 256
SV_TYPE_PRINTQ_SERVER = 512
SV_TYPE_DIALIN_SERVER = 1024
SV_TYPE_XENIX_SERVER = 2048
SV_TYPE_SERVER_UNIX = 2048
SV_TYPE_NT = 4096
SV_TYPE_WFW = 8192
SV_TYPE_SERVER_MFPN = 16384
SV_TYPE_SERVER_NT = 32768
SV_TYPE_POTENTIAL_BROWSER = 65536
SV_TYPE_BACKUP_BROWSER = 131072
SV_TYPE_MASTER_BROWSER = 262144
SV_TYPE_DOMAIN_MASTER = 524288
SV_TYPE_SERVER_OSF = 1048576
SV_TYPE_SERVER_VMS = 2097152
SV_TYPE_WINDOWS = 4194304
SV_TYPE_DFS = 8388608
SV_TYPE_CLUSTER_NT = 16777216
SV_TYPE_TERMINALSERVER = 33554432
SV_TYPE_CLUSTER_VS_NT = 67108864
SV_TYPE_DCE = 268435456
SV_TYPE_ALTERNATE_XPORT = 536870912
SV_TYPE_LOCAL_LIST_ONLY = 1073741824
SV_TYPE_DOMAIN_ENUM = 2147483648
SV_TYPE_ALL = 4294967295
NET_USER_ENUM_FILTER_FLAGS = UInt32
FILTER_TEMP_DUPLICATE_ACCOUNT = 1
FILTER_NORMAL_ACCOUNT = 2
FILTER_INTERDOMAIN_TRUST_ACCOUNT = 8
FILTER_WORKSTATION_TRUST_ACCOUNT = 16
FILTER_SERVER_TRUST_ACCOUNT = 32
def _define_NET_VALIDATE_AUTHENTICATION_INPUT_ARG_head():
    class NET_VALIDATE_AUTHENTICATION_INPUT_ARG(Structure):
        pass
    return NET_VALIDATE_AUTHENTICATION_INPUT_ARG
def _define_NET_VALIDATE_AUTHENTICATION_INPUT_ARG():
    NET_VALIDATE_AUTHENTICATION_INPUT_ARG = win32more.NetworkManagement.NetManagement.NET_VALIDATE_AUTHENTICATION_INPUT_ARG_head
    NET_VALIDATE_AUTHENTICATION_INPUT_ARG._fields_ = [
        ('InputPersistedFields', win32more.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS),
        ('PasswordMatched', win32more.Foundation.BOOLEAN),
    ]
    return NET_VALIDATE_AUTHENTICATION_INPUT_ARG
def _define_NET_VALIDATE_OUTPUT_ARG_head():
    class NET_VALIDATE_OUTPUT_ARG(Structure):
        pass
    return NET_VALIDATE_OUTPUT_ARG
def _define_NET_VALIDATE_OUTPUT_ARG():
    NET_VALIDATE_OUTPUT_ARG = win32more.NetworkManagement.NetManagement.NET_VALIDATE_OUTPUT_ARG_head
    NET_VALIDATE_OUTPUT_ARG._fields_ = [
        ('ChangedPersistedFields', win32more.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS),
        ('ValidationStatus', UInt32),
    ]
    return NET_VALIDATE_OUTPUT_ARG
def _define_NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG_head():
    class NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG(Structure):
        pass
    return NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG
def _define_NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG():
    NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG = win32more.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG_head
    NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG._fields_ = [
        ('InputPersistedFields', win32more.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS),
        ('ClearPassword', win32more.Foundation.PWSTR),
        ('UserAccountName', win32more.Foundation.PWSTR),
        ('HashedPassword', win32more.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_HASH),
        ('PasswordMatch', win32more.Foundation.BOOLEAN),
    ]
    return NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG
def _define_NET_VALIDATE_PASSWORD_HASH_head():
    class NET_VALIDATE_PASSWORD_HASH(Structure):
        pass
    return NET_VALIDATE_PASSWORD_HASH
def _define_NET_VALIDATE_PASSWORD_HASH():
    NET_VALIDATE_PASSWORD_HASH = win32more.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_HASH_head
    NET_VALIDATE_PASSWORD_HASH._fields_ = [
        ('Length', UInt32),
        ('Hash', c_char_p_no),
    ]
    return NET_VALIDATE_PASSWORD_HASH
def _define_NET_VALIDATE_PASSWORD_RESET_INPUT_ARG_head():
    class NET_VALIDATE_PASSWORD_RESET_INPUT_ARG(Structure):
        pass
    return NET_VALIDATE_PASSWORD_RESET_INPUT_ARG
def _define_NET_VALIDATE_PASSWORD_RESET_INPUT_ARG():
    NET_VALIDATE_PASSWORD_RESET_INPUT_ARG = win32more.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_RESET_INPUT_ARG_head
    NET_VALIDATE_PASSWORD_RESET_INPUT_ARG._fields_ = [
        ('InputPersistedFields', win32more.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS),
        ('ClearPassword', win32more.Foundation.PWSTR),
        ('UserAccountName', win32more.Foundation.PWSTR),
        ('HashedPassword', win32more.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_HASH),
        ('PasswordMustChangeAtNextLogon', win32more.Foundation.BOOLEAN),
        ('ClearLockout', win32more.Foundation.BOOLEAN),
    ]
    return NET_VALIDATE_PASSWORD_RESET_INPUT_ARG
NET_VALIDATE_PASSWORD_TYPE = Int32
NET_VALIDATE_PASSWORD_TYPE_NetValidateAuthentication = 1
NET_VALIDATE_PASSWORD_TYPE_NetValidatePasswordChange = 2
NET_VALIDATE_PASSWORD_TYPE_NetValidatePasswordReset = 3
def _define_NET_VALIDATE_PERSISTED_FIELDS_head():
    class NET_VALIDATE_PERSISTED_FIELDS(Structure):
        pass
    return NET_VALIDATE_PERSISTED_FIELDS
def _define_NET_VALIDATE_PERSISTED_FIELDS():
    NET_VALIDATE_PERSISTED_FIELDS = win32more.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS_head
    NET_VALIDATE_PERSISTED_FIELDS._fields_ = [
        ('PresentFields', UInt32),
        ('PasswordLastSet', win32more.Foundation.FILETIME),
        ('BadPasswordTime', win32more.Foundation.FILETIME),
        ('LockoutTime', win32more.Foundation.FILETIME),
        ('BadPasswordCount', UInt32),
        ('PasswordHistoryLength', UInt32),
        ('PasswordHistory', POINTER(win32more.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_HASH_head)),
    ]
    return NET_VALIDATE_PERSISTED_FIELDS
def _define_NETLOGON_INFO_1_head():
    class NETLOGON_INFO_1(Structure):
        pass
    return NETLOGON_INFO_1
def _define_NETLOGON_INFO_1():
    NETLOGON_INFO_1 = win32more.NetworkManagement.NetManagement.NETLOGON_INFO_1_head
    NETLOGON_INFO_1._fields_ = [
        ('netlog1_flags', UInt32),
        ('netlog1_pdc_connection_status', UInt32),
    ]
    return NETLOGON_INFO_1
def _define_NETLOGON_INFO_2_head():
    class NETLOGON_INFO_2(Structure):
        pass
    return NETLOGON_INFO_2
def _define_NETLOGON_INFO_2():
    NETLOGON_INFO_2 = win32more.NetworkManagement.NetManagement.NETLOGON_INFO_2_head
    NETLOGON_INFO_2._fields_ = [
        ('netlog2_flags', UInt32),
        ('netlog2_pdc_connection_status', UInt32),
        ('netlog2_trusted_dc_name', win32more.Foundation.PWSTR),
        ('netlog2_tc_connection_status', UInt32),
    ]
    return NETLOGON_INFO_2
def _define_NETLOGON_INFO_3_head():
    class NETLOGON_INFO_3(Structure):
        pass
    return NETLOGON_INFO_3
def _define_NETLOGON_INFO_3():
    NETLOGON_INFO_3 = win32more.NetworkManagement.NetManagement.NETLOGON_INFO_3_head
    NETLOGON_INFO_3._fields_ = [
        ('netlog3_flags', UInt32),
        ('netlog3_logon_attempts', UInt32),
        ('netlog3_reserved1', UInt32),
        ('netlog3_reserved2', UInt32),
        ('netlog3_reserved3', UInt32),
        ('netlog3_reserved4', UInt32),
        ('netlog3_reserved5', UInt32),
    ]
    return NETLOGON_INFO_3
def _define_NETLOGON_INFO_4_head():
    class NETLOGON_INFO_4(Structure):
        pass
    return NETLOGON_INFO_4
def _define_NETLOGON_INFO_4():
    NETLOGON_INFO_4 = win32more.NetworkManagement.NetManagement.NETLOGON_INFO_4_head
    NETLOGON_INFO_4._fields_ = [
        ('netlog4_trusted_dc_name', win32more.Foundation.PWSTR),
        ('netlog4_trusted_domain_name', win32more.Foundation.PWSTR),
    ]
    return NETLOGON_INFO_4
NetProvisioning = Guid('2aa2b5fe-b846-4d07-81-0c-b2-1e-e4-53-20-e3')
NETSETUP_JOIN_STATUS = Int32
NETSETUP_JOIN_STATUS_NetSetupUnknownStatus = 0
NETSETUP_JOIN_STATUS_NetSetupUnjoined = 1
NETSETUP_JOIN_STATUS_NetSetupWorkgroupName = 2
NETSETUP_JOIN_STATUS_NetSetupDomainName = 3
NETSETUP_NAME_TYPE = Int32
NETSETUP_NAME_TYPE_NetSetupUnknown = 0
NETSETUP_NAME_TYPE_NetSetupMachine = 1
NETSETUP_NAME_TYPE_NetSetupWorkgroup = 2
NETSETUP_NAME_TYPE_NetSetupDomain = 3
NETSETUP_NAME_TYPE_NetSetupNonExistentDomain = 4
NETSETUP_NAME_TYPE_NetSetupDnsMachine = 5
NETSETUP_PROVISION = UInt32
NETSETUP_PROVISION_DOWNLEVEL_PRIV_SUPPORT = 1
NETSETUP_PROVISION_REUSE_ACCOUNT = 2
NETSETUP_PROVISION_USE_DEFAULT_PASSWORD = 4
NETSETUP_PROVISION_SKIP_ACCOUNT_SEARCH = 8
NETSETUP_PROVISION_ROOT_CA_CERTS = 16
def _define_NETSETUP_PROVISIONING_PARAMS_head():
    class NETSETUP_PROVISIONING_PARAMS(Structure):
        pass
    return NETSETUP_PROVISIONING_PARAMS
def _define_NETSETUP_PROVISIONING_PARAMS():
    NETSETUP_PROVISIONING_PARAMS = win32more.NetworkManagement.NetManagement.NETSETUP_PROVISIONING_PARAMS_head
    NETSETUP_PROVISIONING_PARAMS._fields_ = [
        ('dwVersion', UInt32),
        ('lpDomain', win32more.Foundation.PWSTR),
        ('lpHostName', win32more.Foundation.PWSTR),
        ('lpMachineAccountOU', win32more.Foundation.PWSTR),
        ('lpDcName', win32more.Foundation.PWSTR),
        ('dwProvisionOptions', win32more.NetworkManagement.NetManagement.NETSETUP_PROVISION),
        ('aCertTemplateNames', POINTER(win32more.Foundation.PWSTR)),
        ('cCertTemplateNames', UInt32),
        ('aMachinePolicyNames', POINTER(win32more.Foundation.PWSTR)),
        ('cMachinePolicyNames', UInt32),
        ('aMachinePolicyPaths', POINTER(win32more.Foundation.PWSTR)),
        ('cMachinePolicyPaths', UInt32),
        ('lpNetbiosName', win32more.Foundation.PWSTR),
        ('lpSiteName', win32more.Foundation.PWSTR),
        ('lpPrimaryDNSDomain', win32more.Foundation.PWSTR),
    ]
    return NETSETUP_PROVISIONING_PARAMS
NETWORK_INSTALL_TIME = Int32
NSF_PRIMARYINSTALL = 1
NSF_POSTSYSINSTALL = 2
def _define_NETWORK_NAME_head():
    class NETWORK_NAME(Structure):
        pass
    return NETWORK_NAME
def _define_NETWORK_NAME():
    NETWORK_NAME = win32more.NetworkManagement.NetManagement.NETWORK_NAME_head
    NETWORK_NAME._fields_ = [
        ('Name', win32more.NetworkManagement.NetManagement.FLAT_STRING),
    ]
    return NETWORK_NAME
NETWORK_UPGRADE_TYPE = Int32
NSF_WIN16_UPGRADE = 16
NSF_WIN95_UPGRADE = 32
NSF_WINNT_WKS_UPGRADE = 64
NSF_WINNT_SVR_UPGRADE = 128
NSF_WINNT_SBS_UPGRADE = 256
NSF_COMPONENT_UPDATE = 512
def _define_OBO_TOKEN_head():
    class OBO_TOKEN(Structure):
        pass
    return OBO_TOKEN
def _define_OBO_TOKEN():
    OBO_TOKEN = win32more.NetworkManagement.NetManagement.OBO_TOKEN_head
    OBO_TOKEN._fields_ = [
        ('Type', win32more.NetworkManagement.NetManagement.OBO_TOKEN_TYPE),
        ('pncc', win32more.NetworkManagement.NetManagement.INetCfgComponent_head),
        ('pszwManufacturer', win32more.Foundation.PWSTR),
        ('pszwProduct', win32more.Foundation.PWSTR),
        ('pszwDisplayName', win32more.Foundation.PWSTR),
        ('fRegistered', win32more.Foundation.BOOL),
    ]
    return OBO_TOKEN
OBO_TOKEN_TYPE = Int32
OBO_USER = 1
OBO_COMPONENT = 2
OBO_SOFTWARE = 3
def _define_PRINT_OTHER_INFO_head():
    class PRINT_OTHER_INFO(Structure):
        pass
    return PRINT_OTHER_INFO
def _define_PRINT_OTHER_INFO():
    PRINT_OTHER_INFO = win32more.NetworkManagement.NetManagement.PRINT_OTHER_INFO_head
    PRINT_OTHER_INFO._fields_ = [
        ('alrtpr_jobid', UInt32),
        ('alrtpr_status', UInt32),
        ('alrtpr_submitted', UInt32),
        ('alrtpr_size', UInt32),
    ]
    return PRINT_OTHER_INFO
def _define_RASCON_IPUI_head():
    class RASCON_IPUI(Structure):
        pass
    return RASCON_IPUI
def _define_RASCON_IPUI():
    RASCON_IPUI = win32more.NetworkManagement.NetManagement.RASCON_IPUI_head
    RASCON_IPUI._fields_ = [
        ('guidConnection', Guid),
        ('fIPv6Cfg', win32more.Foundation.BOOL),
        ('dwFlags', UInt32),
        ('pszwIpAddr', Char * 16),
        ('pszwDnsAddr', Char * 16),
        ('pszwDns2Addr', Char * 16),
        ('pszwWinsAddr', Char * 16),
        ('pszwWins2Addr', Char * 16),
        ('pszwDnsSuffix', Char * 256),
        ('pszwIpv6Addr', Char * 65),
        ('dwIpv6PrefixLength', UInt32),
        ('pszwIpv6DnsAddr', Char * 65),
        ('pszwIpv6Dns2Addr', Char * 65),
        ('dwIPv4InfMetric', UInt32),
        ('dwIPv6InfMetric', UInt32),
    ]
    return RASCON_IPUI
RASCON_UIINFO_FLAGS = Int32
RCUIF_VPN = 1
RCUIF_DEMAND_DIAL = 2
RCUIF_NOT_ADMIN = 4
RCUIF_USE_IPv4_STATICADDRESS = 8
RCUIF_USE_IPv4_NAME_SERVERS = 16
RCUIF_USE_IPv4_REMOTE_GATEWAY = 32
RCUIF_USE_IPv4_EXPLICIT_METRIC = 64
RCUIF_USE_HEADER_COMPRESSION = 128
RCUIF_USE_DISABLE_REGISTER_DNS = 256
RCUIF_USE_PRIVATE_DNS_SUFFIX = 512
RCUIF_ENABLE_NBT = 1024
RCUIF_USE_IPv6_STATICADDRESS = 2048
RCUIF_USE_IPv6_NAME_SERVERS = 4096
RCUIF_USE_IPv6_REMOTE_GATEWAY = 8192
RCUIF_USE_IPv6_EXPLICIT_METRIC = 16384
RCUIF_DISABLE_CLASS_BASED_ROUTE = 32768
def _define_REPL_EDIR_INFO_0_head():
    class REPL_EDIR_INFO_0(Structure):
        pass
    return REPL_EDIR_INFO_0
def _define_REPL_EDIR_INFO_0():
    REPL_EDIR_INFO_0 = win32more.NetworkManagement.NetManagement.REPL_EDIR_INFO_0_head
    REPL_EDIR_INFO_0._fields_ = [
        ('rped0_dirname', win32more.Foundation.PWSTR),
    ]
    return REPL_EDIR_INFO_0
def _define_REPL_EDIR_INFO_1_head():
    class REPL_EDIR_INFO_1(Structure):
        pass
    return REPL_EDIR_INFO_1
def _define_REPL_EDIR_INFO_1():
    REPL_EDIR_INFO_1 = win32more.NetworkManagement.NetManagement.REPL_EDIR_INFO_1_head
    REPL_EDIR_INFO_1._fields_ = [
        ('rped1_dirname', win32more.Foundation.PWSTR),
        ('rped1_integrity', UInt32),
        ('rped1_extent', UInt32),
    ]
    return REPL_EDIR_INFO_1
def _define_REPL_EDIR_INFO_1000_head():
    class REPL_EDIR_INFO_1000(Structure):
        pass
    return REPL_EDIR_INFO_1000
def _define_REPL_EDIR_INFO_1000():
    REPL_EDIR_INFO_1000 = win32more.NetworkManagement.NetManagement.REPL_EDIR_INFO_1000_head
    REPL_EDIR_INFO_1000._fields_ = [
        ('rped1000_integrity', UInt32),
    ]
    return REPL_EDIR_INFO_1000
def _define_REPL_EDIR_INFO_1001_head():
    class REPL_EDIR_INFO_1001(Structure):
        pass
    return REPL_EDIR_INFO_1001
def _define_REPL_EDIR_INFO_1001():
    REPL_EDIR_INFO_1001 = win32more.NetworkManagement.NetManagement.REPL_EDIR_INFO_1001_head
    REPL_EDIR_INFO_1001._fields_ = [
        ('rped1001_extent', UInt32),
    ]
    return REPL_EDIR_INFO_1001
def _define_REPL_EDIR_INFO_2_head():
    class REPL_EDIR_INFO_2(Structure):
        pass
    return REPL_EDIR_INFO_2
def _define_REPL_EDIR_INFO_2():
    REPL_EDIR_INFO_2 = win32more.NetworkManagement.NetManagement.REPL_EDIR_INFO_2_head
    REPL_EDIR_INFO_2._fields_ = [
        ('rped2_dirname', win32more.Foundation.PWSTR),
        ('rped2_integrity', UInt32),
        ('rped2_extent', UInt32),
        ('rped2_lockcount', UInt32),
        ('rped2_locktime', UInt32),
    ]
    return REPL_EDIR_INFO_2
def _define_REPL_IDIR_INFO_0_head():
    class REPL_IDIR_INFO_0(Structure):
        pass
    return REPL_IDIR_INFO_0
def _define_REPL_IDIR_INFO_0():
    REPL_IDIR_INFO_0 = win32more.NetworkManagement.NetManagement.REPL_IDIR_INFO_0_head
    REPL_IDIR_INFO_0._fields_ = [
        ('rpid0_dirname', win32more.Foundation.PWSTR),
    ]
    return REPL_IDIR_INFO_0
def _define_REPL_IDIR_INFO_1_head():
    class REPL_IDIR_INFO_1(Structure):
        pass
    return REPL_IDIR_INFO_1
def _define_REPL_IDIR_INFO_1():
    REPL_IDIR_INFO_1 = win32more.NetworkManagement.NetManagement.REPL_IDIR_INFO_1_head
    REPL_IDIR_INFO_1._fields_ = [
        ('rpid1_dirname', win32more.Foundation.PWSTR),
        ('rpid1_state', UInt32),
        ('rpid1_mastername', win32more.Foundation.PWSTR),
        ('rpid1_last_update_time', UInt32),
        ('rpid1_lockcount', UInt32),
        ('rpid1_locktime', UInt32),
    ]
    return REPL_IDIR_INFO_1
def _define_REPL_INFO_0_head():
    class REPL_INFO_0(Structure):
        pass
    return REPL_INFO_0
def _define_REPL_INFO_0():
    REPL_INFO_0 = win32more.NetworkManagement.NetManagement.REPL_INFO_0_head
    REPL_INFO_0._fields_ = [
        ('rp0_role', UInt32),
        ('rp0_exportpath', win32more.Foundation.PWSTR),
        ('rp0_exportlist', win32more.Foundation.PWSTR),
        ('rp0_importpath', win32more.Foundation.PWSTR),
        ('rp0_importlist', win32more.Foundation.PWSTR),
        ('rp0_logonusername', win32more.Foundation.PWSTR),
        ('rp0_interval', UInt32),
        ('rp0_pulse', UInt32),
        ('rp0_guardtime', UInt32),
        ('rp0_random', UInt32),
    ]
    return REPL_INFO_0
def _define_REPL_INFO_1000_head():
    class REPL_INFO_1000(Structure):
        pass
    return REPL_INFO_1000
def _define_REPL_INFO_1000():
    REPL_INFO_1000 = win32more.NetworkManagement.NetManagement.REPL_INFO_1000_head
    REPL_INFO_1000._fields_ = [
        ('rp1000_interval', UInt32),
    ]
    return REPL_INFO_1000
def _define_REPL_INFO_1001_head():
    class REPL_INFO_1001(Structure):
        pass
    return REPL_INFO_1001
def _define_REPL_INFO_1001():
    REPL_INFO_1001 = win32more.NetworkManagement.NetManagement.REPL_INFO_1001_head
    REPL_INFO_1001._fields_ = [
        ('rp1001_pulse', UInt32),
    ]
    return REPL_INFO_1001
def _define_REPL_INFO_1002_head():
    class REPL_INFO_1002(Structure):
        pass
    return REPL_INFO_1002
def _define_REPL_INFO_1002():
    REPL_INFO_1002 = win32more.NetworkManagement.NetManagement.REPL_INFO_1002_head
    REPL_INFO_1002._fields_ = [
        ('rp1002_guardtime', UInt32),
    ]
    return REPL_INFO_1002
def _define_REPL_INFO_1003_head():
    class REPL_INFO_1003(Structure):
        pass
    return REPL_INFO_1003
def _define_REPL_INFO_1003():
    REPL_INFO_1003 = win32more.NetworkManagement.NetManagement.REPL_INFO_1003_head
    REPL_INFO_1003._fields_ = [
        ('rp1003_random', UInt32),
    ]
    return REPL_INFO_1003
def _define_RTR_INFO_BLOCK_HEADER_head():
    class RTR_INFO_BLOCK_HEADER(Structure):
        pass
    return RTR_INFO_BLOCK_HEADER
def _define_RTR_INFO_BLOCK_HEADER():
    RTR_INFO_BLOCK_HEADER = win32more.NetworkManagement.NetManagement.RTR_INFO_BLOCK_HEADER_head
    RTR_INFO_BLOCK_HEADER._fields_ = [
        ('Version', UInt32),
        ('Size', UInt32),
        ('TocEntriesCount', UInt32),
        ('TocEntry', win32more.NetworkManagement.NetManagement.RTR_TOC_ENTRY * 1),
    ]
    return RTR_INFO_BLOCK_HEADER
def _define_RTR_TOC_ENTRY_head():
    class RTR_TOC_ENTRY(Structure):
        pass
    return RTR_TOC_ENTRY
def _define_RTR_TOC_ENTRY():
    RTR_TOC_ENTRY = win32more.NetworkManagement.NetManagement.RTR_TOC_ENTRY_head
    RTR_TOC_ENTRY._fields_ = [
        ('InfoType', UInt32),
        ('InfoSize', UInt32),
        ('Count', UInt32),
        ('Offset', UInt32),
    ]
    return RTR_TOC_ENTRY
def _define_SERVER_INFO_100_head():
    class SERVER_INFO_100(Structure):
        pass
    return SERVER_INFO_100
def _define_SERVER_INFO_100():
    SERVER_INFO_100 = win32more.NetworkManagement.NetManagement.SERVER_INFO_100_head
    SERVER_INFO_100._fields_ = [
        ('sv100_platform_id', UInt32),
        ('sv100_name', win32more.Foundation.PWSTR),
    ]
    return SERVER_INFO_100
def _define_SERVER_INFO_1005_head():
    class SERVER_INFO_1005(Structure):
        pass
    return SERVER_INFO_1005
def _define_SERVER_INFO_1005():
    SERVER_INFO_1005 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1005_head
    SERVER_INFO_1005._fields_ = [
        ('sv1005_comment', win32more.Foundation.PWSTR),
    ]
    return SERVER_INFO_1005
def _define_SERVER_INFO_101_head():
    class SERVER_INFO_101(Structure):
        pass
    return SERVER_INFO_101
def _define_SERVER_INFO_101():
    SERVER_INFO_101 = win32more.NetworkManagement.NetManagement.SERVER_INFO_101_head
    SERVER_INFO_101._fields_ = [
        ('sv101_platform_id', UInt32),
        ('sv101_name', win32more.Foundation.PWSTR),
        ('sv101_version_major', UInt32),
        ('sv101_version_minor', UInt32),
        ('sv101_type', win32more.NetworkManagement.NetManagement.NET_SERVER_TYPE),
        ('sv101_comment', win32more.Foundation.PWSTR),
    ]
    return SERVER_INFO_101
def _define_SERVER_INFO_1010_head():
    class SERVER_INFO_1010(Structure):
        pass
    return SERVER_INFO_1010
def _define_SERVER_INFO_1010():
    SERVER_INFO_1010 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1010_head
    SERVER_INFO_1010._fields_ = [
        ('sv1010_disc', Int32),
    ]
    return SERVER_INFO_1010
def _define_SERVER_INFO_1016_head():
    class SERVER_INFO_1016(Structure):
        pass
    return SERVER_INFO_1016
def _define_SERVER_INFO_1016():
    SERVER_INFO_1016 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1016_head
    SERVER_INFO_1016._fields_ = [
        ('sv1016_hidden', win32more.NetworkManagement.NetManagement.SERVER_INFO_HIDDEN),
    ]
    return SERVER_INFO_1016
def _define_SERVER_INFO_1017_head():
    class SERVER_INFO_1017(Structure):
        pass
    return SERVER_INFO_1017
def _define_SERVER_INFO_1017():
    SERVER_INFO_1017 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1017_head
    SERVER_INFO_1017._fields_ = [
        ('sv1017_announce', UInt32),
    ]
    return SERVER_INFO_1017
def _define_SERVER_INFO_1018_head():
    class SERVER_INFO_1018(Structure):
        pass
    return SERVER_INFO_1018
def _define_SERVER_INFO_1018():
    SERVER_INFO_1018 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1018_head
    SERVER_INFO_1018._fields_ = [
        ('sv1018_anndelta', UInt32),
    ]
    return SERVER_INFO_1018
def _define_SERVER_INFO_102_head():
    class SERVER_INFO_102(Structure):
        pass
    return SERVER_INFO_102
def _define_SERVER_INFO_102():
    SERVER_INFO_102 = win32more.NetworkManagement.NetManagement.SERVER_INFO_102_head
    SERVER_INFO_102._fields_ = [
        ('sv102_platform_id', UInt32),
        ('sv102_name', win32more.Foundation.PWSTR),
        ('sv102_version_major', UInt32),
        ('sv102_version_minor', UInt32),
        ('sv102_type', win32more.NetworkManagement.NetManagement.NET_SERVER_TYPE),
        ('sv102_comment', win32more.Foundation.PWSTR),
        ('sv102_users', UInt32),
        ('sv102_disc', Int32),
        ('sv102_hidden', win32more.NetworkManagement.NetManagement.SERVER_INFO_HIDDEN),
        ('sv102_announce', UInt32),
        ('sv102_anndelta', UInt32),
        ('sv102_licenses', UInt32),
        ('sv102_userpath', win32more.Foundation.PWSTR),
    ]
    return SERVER_INFO_102
def _define_SERVER_INFO_103_head():
    class SERVER_INFO_103(Structure):
        pass
    return SERVER_INFO_103
def _define_SERVER_INFO_103():
    SERVER_INFO_103 = win32more.NetworkManagement.NetManagement.SERVER_INFO_103_head
    SERVER_INFO_103._fields_ = [
        ('sv103_platform_id', UInt32),
        ('sv103_name', win32more.Foundation.PWSTR),
        ('sv103_version_major', UInt32),
        ('sv103_version_minor', UInt32),
        ('sv103_type', UInt32),
        ('sv103_comment', win32more.Foundation.PWSTR),
        ('sv103_users', UInt32),
        ('sv103_disc', Int32),
        ('sv103_hidden', win32more.Foundation.BOOL),
        ('sv103_announce', UInt32),
        ('sv103_anndelta', UInt32),
        ('sv103_licenses', UInt32),
        ('sv103_userpath', win32more.Foundation.PWSTR),
        ('sv103_capabilities', UInt32),
    ]
    return SERVER_INFO_103
def _define_SERVER_INFO_1107_head():
    class SERVER_INFO_1107(Structure):
        pass
    return SERVER_INFO_1107
def _define_SERVER_INFO_1107():
    SERVER_INFO_1107 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1107_head
    SERVER_INFO_1107._fields_ = [
        ('sv1107_users', UInt32),
    ]
    return SERVER_INFO_1107
def _define_SERVER_INFO_1501_head():
    class SERVER_INFO_1501(Structure):
        pass
    return SERVER_INFO_1501
def _define_SERVER_INFO_1501():
    SERVER_INFO_1501 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1501_head
    SERVER_INFO_1501._fields_ = [
        ('sv1501_sessopens', UInt32),
    ]
    return SERVER_INFO_1501
def _define_SERVER_INFO_1502_head():
    class SERVER_INFO_1502(Structure):
        pass
    return SERVER_INFO_1502
def _define_SERVER_INFO_1502():
    SERVER_INFO_1502 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1502_head
    SERVER_INFO_1502._fields_ = [
        ('sv1502_sessvcs', UInt32),
    ]
    return SERVER_INFO_1502
def _define_SERVER_INFO_1503_head():
    class SERVER_INFO_1503(Structure):
        pass
    return SERVER_INFO_1503
def _define_SERVER_INFO_1503():
    SERVER_INFO_1503 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1503_head
    SERVER_INFO_1503._fields_ = [
        ('sv1503_opensearch', UInt32),
    ]
    return SERVER_INFO_1503
def _define_SERVER_INFO_1506_head():
    class SERVER_INFO_1506(Structure):
        pass
    return SERVER_INFO_1506
def _define_SERVER_INFO_1506():
    SERVER_INFO_1506 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1506_head
    SERVER_INFO_1506._fields_ = [
        ('sv1506_maxworkitems', UInt32),
    ]
    return SERVER_INFO_1506
def _define_SERVER_INFO_1509_head():
    class SERVER_INFO_1509(Structure):
        pass
    return SERVER_INFO_1509
def _define_SERVER_INFO_1509():
    SERVER_INFO_1509 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1509_head
    SERVER_INFO_1509._fields_ = [
        ('sv1509_maxrawbuflen', UInt32),
    ]
    return SERVER_INFO_1509
def _define_SERVER_INFO_1510_head():
    class SERVER_INFO_1510(Structure):
        pass
    return SERVER_INFO_1510
def _define_SERVER_INFO_1510():
    SERVER_INFO_1510 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1510_head
    SERVER_INFO_1510._fields_ = [
        ('sv1510_sessusers', UInt32),
    ]
    return SERVER_INFO_1510
def _define_SERVER_INFO_1511_head():
    class SERVER_INFO_1511(Structure):
        pass
    return SERVER_INFO_1511
def _define_SERVER_INFO_1511():
    SERVER_INFO_1511 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1511_head
    SERVER_INFO_1511._fields_ = [
        ('sv1511_sessconns', UInt32),
    ]
    return SERVER_INFO_1511
def _define_SERVER_INFO_1512_head():
    class SERVER_INFO_1512(Structure):
        pass
    return SERVER_INFO_1512
def _define_SERVER_INFO_1512():
    SERVER_INFO_1512 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1512_head
    SERVER_INFO_1512._fields_ = [
        ('sv1512_maxnonpagedmemoryusage', UInt32),
    ]
    return SERVER_INFO_1512
def _define_SERVER_INFO_1513_head():
    class SERVER_INFO_1513(Structure):
        pass
    return SERVER_INFO_1513
def _define_SERVER_INFO_1513():
    SERVER_INFO_1513 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1513_head
    SERVER_INFO_1513._fields_ = [
        ('sv1513_maxpagedmemoryusage', UInt32),
    ]
    return SERVER_INFO_1513
def _define_SERVER_INFO_1514_head():
    class SERVER_INFO_1514(Structure):
        pass
    return SERVER_INFO_1514
def _define_SERVER_INFO_1514():
    SERVER_INFO_1514 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1514_head
    SERVER_INFO_1514._fields_ = [
        ('sv1514_enablesoftcompat', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1514
def _define_SERVER_INFO_1515_head():
    class SERVER_INFO_1515(Structure):
        pass
    return SERVER_INFO_1515
def _define_SERVER_INFO_1515():
    SERVER_INFO_1515 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1515_head
    SERVER_INFO_1515._fields_ = [
        ('sv1515_enableforcedlogoff', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1515
def _define_SERVER_INFO_1516_head():
    class SERVER_INFO_1516(Structure):
        pass
    return SERVER_INFO_1516
def _define_SERVER_INFO_1516():
    SERVER_INFO_1516 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1516_head
    SERVER_INFO_1516._fields_ = [
        ('sv1516_timesource', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1516
def _define_SERVER_INFO_1518_head():
    class SERVER_INFO_1518(Structure):
        pass
    return SERVER_INFO_1518
def _define_SERVER_INFO_1518():
    SERVER_INFO_1518 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1518_head
    SERVER_INFO_1518._fields_ = [
        ('sv1518_lmannounce', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1518
def _define_SERVER_INFO_1520_head():
    class SERVER_INFO_1520(Structure):
        pass
    return SERVER_INFO_1520
def _define_SERVER_INFO_1520():
    SERVER_INFO_1520 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1520_head
    SERVER_INFO_1520._fields_ = [
        ('sv1520_maxcopyreadlen', UInt32),
    ]
    return SERVER_INFO_1520
def _define_SERVER_INFO_1521_head():
    class SERVER_INFO_1521(Structure):
        pass
    return SERVER_INFO_1521
def _define_SERVER_INFO_1521():
    SERVER_INFO_1521 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1521_head
    SERVER_INFO_1521._fields_ = [
        ('sv1521_maxcopywritelen', UInt32),
    ]
    return SERVER_INFO_1521
def _define_SERVER_INFO_1522_head():
    class SERVER_INFO_1522(Structure):
        pass
    return SERVER_INFO_1522
def _define_SERVER_INFO_1522():
    SERVER_INFO_1522 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1522_head
    SERVER_INFO_1522._fields_ = [
        ('sv1522_minkeepsearch', UInt32),
    ]
    return SERVER_INFO_1522
def _define_SERVER_INFO_1523_head():
    class SERVER_INFO_1523(Structure):
        pass
    return SERVER_INFO_1523
def _define_SERVER_INFO_1523():
    SERVER_INFO_1523 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1523_head
    SERVER_INFO_1523._fields_ = [
        ('sv1523_maxkeepsearch', UInt32),
    ]
    return SERVER_INFO_1523
def _define_SERVER_INFO_1524_head():
    class SERVER_INFO_1524(Structure):
        pass
    return SERVER_INFO_1524
def _define_SERVER_INFO_1524():
    SERVER_INFO_1524 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1524_head
    SERVER_INFO_1524._fields_ = [
        ('sv1524_minkeepcomplsearch', UInt32),
    ]
    return SERVER_INFO_1524
def _define_SERVER_INFO_1525_head():
    class SERVER_INFO_1525(Structure):
        pass
    return SERVER_INFO_1525
def _define_SERVER_INFO_1525():
    SERVER_INFO_1525 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1525_head
    SERVER_INFO_1525._fields_ = [
        ('sv1525_maxkeepcomplsearch', UInt32),
    ]
    return SERVER_INFO_1525
def _define_SERVER_INFO_1528_head():
    class SERVER_INFO_1528(Structure):
        pass
    return SERVER_INFO_1528
def _define_SERVER_INFO_1528():
    SERVER_INFO_1528 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1528_head
    SERVER_INFO_1528._fields_ = [
        ('sv1528_scavtimeout', UInt32),
    ]
    return SERVER_INFO_1528
def _define_SERVER_INFO_1529_head():
    class SERVER_INFO_1529(Structure):
        pass
    return SERVER_INFO_1529
def _define_SERVER_INFO_1529():
    SERVER_INFO_1529 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1529_head
    SERVER_INFO_1529._fields_ = [
        ('sv1529_minrcvqueue', UInt32),
    ]
    return SERVER_INFO_1529
def _define_SERVER_INFO_1530_head():
    class SERVER_INFO_1530(Structure):
        pass
    return SERVER_INFO_1530
def _define_SERVER_INFO_1530():
    SERVER_INFO_1530 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1530_head
    SERVER_INFO_1530._fields_ = [
        ('sv1530_minfreeworkitems', UInt32),
    ]
    return SERVER_INFO_1530
def _define_SERVER_INFO_1533_head():
    class SERVER_INFO_1533(Structure):
        pass
    return SERVER_INFO_1533
def _define_SERVER_INFO_1533():
    SERVER_INFO_1533 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1533_head
    SERVER_INFO_1533._fields_ = [
        ('sv1533_maxmpxct', UInt32),
    ]
    return SERVER_INFO_1533
def _define_SERVER_INFO_1534_head():
    class SERVER_INFO_1534(Structure):
        pass
    return SERVER_INFO_1534
def _define_SERVER_INFO_1534():
    SERVER_INFO_1534 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1534_head
    SERVER_INFO_1534._fields_ = [
        ('sv1534_oplockbreakwait', UInt32),
    ]
    return SERVER_INFO_1534
def _define_SERVER_INFO_1535_head():
    class SERVER_INFO_1535(Structure):
        pass
    return SERVER_INFO_1535
def _define_SERVER_INFO_1535():
    SERVER_INFO_1535 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1535_head
    SERVER_INFO_1535._fields_ = [
        ('sv1535_oplockbreakresponsewait', UInt32),
    ]
    return SERVER_INFO_1535
def _define_SERVER_INFO_1536_head():
    class SERVER_INFO_1536(Structure):
        pass
    return SERVER_INFO_1536
def _define_SERVER_INFO_1536():
    SERVER_INFO_1536 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1536_head
    SERVER_INFO_1536._fields_ = [
        ('sv1536_enableoplocks', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1536
def _define_SERVER_INFO_1537_head():
    class SERVER_INFO_1537(Structure):
        pass
    return SERVER_INFO_1537
def _define_SERVER_INFO_1537():
    SERVER_INFO_1537 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1537_head
    SERVER_INFO_1537._fields_ = [
        ('sv1537_enableoplockforceclose', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1537
def _define_SERVER_INFO_1538_head():
    class SERVER_INFO_1538(Structure):
        pass
    return SERVER_INFO_1538
def _define_SERVER_INFO_1538():
    SERVER_INFO_1538 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1538_head
    SERVER_INFO_1538._fields_ = [
        ('sv1538_enablefcbopens', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1538
def _define_SERVER_INFO_1539_head():
    class SERVER_INFO_1539(Structure):
        pass
    return SERVER_INFO_1539
def _define_SERVER_INFO_1539():
    SERVER_INFO_1539 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1539_head
    SERVER_INFO_1539._fields_ = [
        ('sv1539_enableraw', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1539
def _define_SERVER_INFO_1540_head():
    class SERVER_INFO_1540(Structure):
        pass
    return SERVER_INFO_1540
def _define_SERVER_INFO_1540():
    SERVER_INFO_1540 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1540_head
    SERVER_INFO_1540._fields_ = [
        ('sv1540_enablesharednetdrives', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1540
def _define_SERVER_INFO_1541_head():
    class SERVER_INFO_1541(Structure):
        pass
    return SERVER_INFO_1541
def _define_SERVER_INFO_1541():
    SERVER_INFO_1541 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1541_head
    SERVER_INFO_1541._fields_ = [
        ('sv1541_minfreeconnections', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1541
def _define_SERVER_INFO_1542_head():
    class SERVER_INFO_1542(Structure):
        pass
    return SERVER_INFO_1542
def _define_SERVER_INFO_1542():
    SERVER_INFO_1542 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1542_head
    SERVER_INFO_1542._fields_ = [
        ('sv1542_maxfreeconnections', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1542
def _define_SERVER_INFO_1543_head():
    class SERVER_INFO_1543(Structure):
        pass
    return SERVER_INFO_1543
def _define_SERVER_INFO_1543():
    SERVER_INFO_1543 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1543_head
    SERVER_INFO_1543._fields_ = [
        ('sv1543_initsesstable', UInt32),
    ]
    return SERVER_INFO_1543
def _define_SERVER_INFO_1544_head():
    class SERVER_INFO_1544(Structure):
        pass
    return SERVER_INFO_1544
def _define_SERVER_INFO_1544():
    SERVER_INFO_1544 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1544_head
    SERVER_INFO_1544._fields_ = [
        ('sv1544_initconntable', UInt32),
    ]
    return SERVER_INFO_1544
def _define_SERVER_INFO_1545_head():
    class SERVER_INFO_1545(Structure):
        pass
    return SERVER_INFO_1545
def _define_SERVER_INFO_1545():
    SERVER_INFO_1545 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1545_head
    SERVER_INFO_1545._fields_ = [
        ('sv1545_initfiletable', UInt32),
    ]
    return SERVER_INFO_1545
def _define_SERVER_INFO_1546_head():
    class SERVER_INFO_1546(Structure):
        pass
    return SERVER_INFO_1546
def _define_SERVER_INFO_1546():
    SERVER_INFO_1546 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1546_head
    SERVER_INFO_1546._fields_ = [
        ('sv1546_initsearchtable', UInt32),
    ]
    return SERVER_INFO_1546
def _define_SERVER_INFO_1547_head():
    class SERVER_INFO_1547(Structure):
        pass
    return SERVER_INFO_1547
def _define_SERVER_INFO_1547():
    SERVER_INFO_1547 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1547_head
    SERVER_INFO_1547._fields_ = [
        ('sv1547_alertschedule', UInt32),
    ]
    return SERVER_INFO_1547
def _define_SERVER_INFO_1548_head():
    class SERVER_INFO_1548(Structure):
        pass
    return SERVER_INFO_1548
def _define_SERVER_INFO_1548():
    SERVER_INFO_1548 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1548_head
    SERVER_INFO_1548._fields_ = [
        ('sv1548_errorthreshold', UInt32),
    ]
    return SERVER_INFO_1548
def _define_SERVER_INFO_1549_head():
    class SERVER_INFO_1549(Structure):
        pass
    return SERVER_INFO_1549
def _define_SERVER_INFO_1549():
    SERVER_INFO_1549 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1549_head
    SERVER_INFO_1549._fields_ = [
        ('sv1549_networkerrorthreshold', UInt32),
    ]
    return SERVER_INFO_1549
def _define_SERVER_INFO_1550_head():
    class SERVER_INFO_1550(Structure):
        pass
    return SERVER_INFO_1550
def _define_SERVER_INFO_1550():
    SERVER_INFO_1550 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1550_head
    SERVER_INFO_1550._fields_ = [
        ('sv1550_diskspacethreshold', UInt32),
    ]
    return SERVER_INFO_1550
def _define_SERVER_INFO_1552_head():
    class SERVER_INFO_1552(Structure):
        pass
    return SERVER_INFO_1552
def _define_SERVER_INFO_1552():
    SERVER_INFO_1552 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1552_head
    SERVER_INFO_1552._fields_ = [
        ('sv1552_maxlinkdelay', UInt32),
    ]
    return SERVER_INFO_1552
def _define_SERVER_INFO_1553_head():
    class SERVER_INFO_1553(Structure):
        pass
    return SERVER_INFO_1553
def _define_SERVER_INFO_1553():
    SERVER_INFO_1553 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1553_head
    SERVER_INFO_1553._fields_ = [
        ('sv1553_minlinkthroughput', UInt32),
    ]
    return SERVER_INFO_1553
def _define_SERVER_INFO_1554_head():
    class SERVER_INFO_1554(Structure):
        pass
    return SERVER_INFO_1554
def _define_SERVER_INFO_1554():
    SERVER_INFO_1554 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1554_head
    SERVER_INFO_1554._fields_ = [
        ('sv1554_linkinfovalidtime', UInt32),
    ]
    return SERVER_INFO_1554
def _define_SERVER_INFO_1555_head():
    class SERVER_INFO_1555(Structure):
        pass
    return SERVER_INFO_1555
def _define_SERVER_INFO_1555():
    SERVER_INFO_1555 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1555_head
    SERVER_INFO_1555._fields_ = [
        ('sv1555_scavqosinfoupdatetime', UInt32),
    ]
    return SERVER_INFO_1555
def _define_SERVER_INFO_1556_head():
    class SERVER_INFO_1556(Structure):
        pass
    return SERVER_INFO_1556
def _define_SERVER_INFO_1556():
    SERVER_INFO_1556 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1556_head
    SERVER_INFO_1556._fields_ = [
        ('sv1556_maxworkitemidletime', UInt32),
    ]
    return SERVER_INFO_1556
def _define_SERVER_INFO_1557_head():
    class SERVER_INFO_1557(Structure):
        pass
    return SERVER_INFO_1557
def _define_SERVER_INFO_1557():
    SERVER_INFO_1557 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1557_head
    SERVER_INFO_1557._fields_ = [
        ('sv1557_maxrawworkitems', UInt32),
    ]
    return SERVER_INFO_1557
def _define_SERVER_INFO_1560_head():
    class SERVER_INFO_1560(Structure):
        pass
    return SERVER_INFO_1560
def _define_SERVER_INFO_1560():
    SERVER_INFO_1560 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1560_head
    SERVER_INFO_1560._fields_ = [
        ('sv1560_producttype', UInt32),
    ]
    return SERVER_INFO_1560
def _define_SERVER_INFO_1561_head():
    class SERVER_INFO_1561(Structure):
        pass
    return SERVER_INFO_1561
def _define_SERVER_INFO_1561():
    SERVER_INFO_1561 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1561_head
    SERVER_INFO_1561._fields_ = [
        ('sv1561_serversize', UInt32),
    ]
    return SERVER_INFO_1561
def _define_SERVER_INFO_1562_head():
    class SERVER_INFO_1562(Structure):
        pass
    return SERVER_INFO_1562
def _define_SERVER_INFO_1562():
    SERVER_INFO_1562 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1562_head
    SERVER_INFO_1562._fields_ = [
        ('sv1562_connectionlessautodisc', UInt32),
    ]
    return SERVER_INFO_1562
def _define_SERVER_INFO_1563_head():
    class SERVER_INFO_1563(Structure):
        pass
    return SERVER_INFO_1563
def _define_SERVER_INFO_1563():
    SERVER_INFO_1563 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1563_head
    SERVER_INFO_1563._fields_ = [
        ('sv1563_sharingviolationretries', UInt32),
    ]
    return SERVER_INFO_1563
def _define_SERVER_INFO_1564_head():
    class SERVER_INFO_1564(Structure):
        pass
    return SERVER_INFO_1564
def _define_SERVER_INFO_1564():
    SERVER_INFO_1564 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1564_head
    SERVER_INFO_1564._fields_ = [
        ('sv1564_sharingviolationdelay', UInt32),
    ]
    return SERVER_INFO_1564
def _define_SERVER_INFO_1565_head():
    class SERVER_INFO_1565(Structure):
        pass
    return SERVER_INFO_1565
def _define_SERVER_INFO_1565():
    SERVER_INFO_1565 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1565_head
    SERVER_INFO_1565._fields_ = [
        ('sv1565_maxglobalopensearch', UInt32),
    ]
    return SERVER_INFO_1565
def _define_SERVER_INFO_1566_head():
    class SERVER_INFO_1566(Structure):
        pass
    return SERVER_INFO_1566
def _define_SERVER_INFO_1566():
    SERVER_INFO_1566 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1566_head
    SERVER_INFO_1566._fields_ = [
        ('sv1566_removeduplicatesearches', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1566
def _define_SERVER_INFO_1567_head():
    class SERVER_INFO_1567(Structure):
        pass
    return SERVER_INFO_1567
def _define_SERVER_INFO_1567():
    SERVER_INFO_1567 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1567_head
    SERVER_INFO_1567._fields_ = [
        ('sv1567_lockviolationretries', UInt32),
    ]
    return SERVER_INFO_1567
def _define_SERVER_INFO_1568_head():
    class SERVER_INFO_1568(Structure):
        pass
    return SERVER_INFO_1568
def _define_SERVER_INFO_1568():
    SERVER_INFO_1568 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1568_head
    SERVER_INFO_1568._fields_ = [
        ('sv1568_lockviolationoffset', UInt32),
    ]
    return SERVER_INFO_1568
def _define_SERVER_INFO_1569_head():
    class SERVER_INFO_1569(Structure):
        pass
    return SERVER_INFO_1569
def _define_SERVER_INFO_1569():
    SERVER_INFO_1569 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1569_head
    SERVER_INFO_1569._fields_ = [
        ('sv1569_lockviolationdelay', UInt32),
    ]
    return SERVER_INFO_1569
def _define_SERVER_INFO_1570_head():
    class SERVER_INFO_1570(Structure):
        pass
    return SERVER_INFO_1570
def _define_SERVER_INFO_1570():
    SERVER_INFO_1570 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1570_head
    SERVER_INFO_1570._fields_ = [
        ('sv1570_mdlreadswitchover', UInt32),
    ]
    return SERVER_INFO_1570
def _define_SERVER_INFO_1571_head():
    class SERVER_INFO_1571(Structure):
        pass
    return SERVER_INFO_1571
def _define_SERVER_INFO_1571():
    SERVER_INFO_1571 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1571_head
    SERVER_INFO_1571._fields_ = [
        ('sv1571_cachedopenlimit', UInt32),
    ]
    return SERVER_INFO_1571
def _define_SERVER_INFO_1572_head():
    class SERVER_INFO_1572(Structure):
        pass
    return SERVER_INFO_1572
def _define_SERVER_INFO_1572():
    SERVER_INFO_1572 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1572_head
    SERVER_INFO_1572._fields_ = [
        ('sv1572_criticalthreads', UInt32),
    ]
    return SERVER_INFO_1572
def _define_SERVER_INFO_1573_head():
    class SERVER_INFO_1573(Structure):
        pass
    return SERVER_INFO_1573
def _define_SERVER_INFO_1573():
    SERVER_INFO_1573 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1573_head
    SERVER_INFO_1573._fields_ = [
        ('sv1573_restrictnullsessaccess', UInt32),
    ]
    return SERVER_INFO_1573
def _define_SERVER_INFO_1574_head():
    class SERVER_INFO_1574(Structure):
        pass
    return SERVER_INFO_1574
def _define_SERVER_INFO_1574():
    SERVER_INFO_1574 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1574_head
    SERVER_INFO_1574._fields_ = [
        ('sv1574_enablewfw311directipx', UInt32),
    ]
    return SERVER_INFO_1574
def _define_SERVER_INFO_1575_head():
    class SERVER_INFO_1575(Structure):
        pass
    return SERVER_INFO_1575
def _define_SERVER_INFO_1575():
    SERVER_INFO_1575 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1575_head
    SERVER_INFO_1575._fields_ = [
        ('sv1575_otherqueueaffinity', UInt32),
    ]
    return SERVER_INFO_1575
def _define_SERVER_INFO_1576_head():
    class SERVER_INFO_1576(Structure):
        pass
    return SERVER_INFO_1576
def _define_SERVER_INFO_1576():
    SERVER_INFO_1576 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1576_head
    SERVER_INFO_1576._fields_ = [
        ('sv1576_queuesamplesecs', UInt32),
    ]
    return SERVER_INFO_1576
def _define_SERVER_INFO_1577_head():
    class SERVER_INFO_1577(Structure):
        pass
    return SERVER_INFO_1577
def _define_SERVER_INFO_1577():
    SERVER_INFO_1577 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1577_head
    SERVER_INFO_1577._fields_ = [
        ('sv1577_balancecount', UInt32),
    ]
    return SERVER_INFO_1577
def _define_SERVER_INFO_1578_head():
    class SERVER_INFO_1578(Structure):
        pass
    return SERVER_INFO_1578
def _define_SERVER_INFO_1578():
    SERVER_INFO_1578 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1578_head
    SERVER_INFO_1578._fields_ = [
        ('sv1578_preferredaffinity', UInt32),
    ]
    return SERVER_INFO_1578
def _define_SERVER_INFO_1579_head():
    class SERVER_INFO_1579(Structure):
        pass
    return SERVER_INFO_1579
def _define_SERVER_INFO_1579():
    SERVER_INFO_1579 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1579_head
    SERVER_INFO_1579._fields_ = [
        ('sv1579_maxfreerfcbs', UInt32),
    ]
    return SERVER_INFO_1579
def _define_SERVER_INFO_1580_head():
    class SERVER_INFO_1580(Structure):
        pass
    return SERVER_INFO_1580
def _define_SERVER_INFO_1580():
    SERVER_INFO_1580 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1580_head
    SERVER_INFO_1580._fields_ = [
        ('sv1580_maxfreemfcbs', UInt32),
    ]
    return SERVER_INFO_1580
def _define_SERVER_INFO_1581_head():
    class SERVER_INFO_1581(Structure):
        pass
    return SERVER_INFO_1581
def _define_SERVER_INFO_1581():
    SERVER_INFO_1581 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1581_head
    SERVER_INFO_1581._fields_ = [
        ('sv1581_maxfreemlcbs', UInt32),
    ]
    return SERVER_INFO_1581
def _define_SERVER_INFO_1582_head():
    class SERVER_INFO_1582(Structure):
        pass
    return SERVER_INFO_1582
def _define_SERVER_INFO_1582():
    SERVER_INFO_1582 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1582_head
    SERVER_INFO_1582._fields_ = [
        ('sv1582_maxfreepagedpoolchunks', UInt32),
    ]
    return SERVER_INFO_1582
def _define_SERVER_INFO_1583_head():
    class SERVER_INFO_1583(Structure):
        pass
    return SERVER_INFO_1583
def _define_SERVER_INFO_1583():
    SERVER_INFO_1583 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1583_head
    SERVER_INFO_1583._fields_ = [
        ('sv1583_minpagedpoolchunksize', UInt32),
    ]
    return SERVER_INFO_1583
def _define_SERVER_INFO_1584_head():
    class SERVER_INFO_1584(Structure):
        pass
    return SERVER_INFO_1584
def _define_SERVER_INFO_1584():
    SERVER_INFO_1584 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1584_head
    SERVER_INFO_1584._fields_ = [
        ('sv1584_maxpagedpoolchunksize', UInt32),
    ]
    return SERVER_INFO_1584
def _define_SERVER_INFO_1585_head():
    class SERVER_INFO_1585(Structure):
        pass
    return SERVER_INFO_1585
def _define_SERVER_INFO_1585():
    SERVER_INFO_1585 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1585_head
    SERVER_INFO_1585._fields_ = [
        ('sv1585_sendsfrompreferredprocessor', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1585
def _define_SERVER_INFO_1586_head():
    class SERVER_INFO_1586(Structure):
        pass
    return SERVER_INFO_1586
def _define_SERVER_INFO_1586():
    SERVER_INFO_1586 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1586_head
    SERVER_INFO_1586._fields_ = [
        ('sv1586_maxthreadsperqueue', UInt32),
    ]
    return SERVER_INFO_1586
def _define_SERVER_INFO_1587_head():
    class SERVER_INFO_1587(Structure):
        pass
    return SERVER_INFO_1587
def _define_SERVER_INFO_1587():
    SERVER_INFO_1587 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1587_head
    SERVER_INFO_1587._fields_ = [
        ('sv1587_cacheddirectorylimit', UInt32),
    ]
    return SERVER_INFO_1587
def _define_SERVER_INFO_1588_head():
    class SERVER_INFO_1588(Structure):
        pass
    return SERVER_INFO_1588
def _define_SERVER_INFO_1588():
    SERVER_INFO_1588 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1588_head
    SERVER_INFO_1588._fields_ = [
        ('sv1588_maxcopylength', UInt32),
    ]
    return SERVER_INFO_1588
def _define_SERVER_INFO_1590_head():
    class SERVER_INFO_1590(Structure):
        pass
    return SERVER_INFO_1590
def _define_SERVER_INFO_1590():
    SERVER_INFO_1590 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1590_head
    SERVER_INFO_1590._fields_ = [
        ('sv1590_enablecompression', UInt32),
    ]
    return SERVER_INFO_1590
def _define_SERVER_INFO_1591_head():
    class SERVER_INFO_1591(Structure):
        pass
    return SERVER_INFO_1591
def _define_SERVER_INFO_1591():
    SERVER_INFO_1591 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1591_head
    SERVER_INFO_1591._fields_ = [
        ('sv1591_autosharewks', UInt32),
    ]
    return SERVER_INFO_1591
def _define_SERVER_INFO_1592_head():
    class SERVER_INFO_1592(Structure):
        pass
    return SERVER_INFO_1592
def _define_SERVER_INFO_1592():
    SERVER_INFO_1592 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1592_head
    SERVER_INFO_1592._fields_ = [
        ('sv1592_autosharewks', UInt32),
    ]
    return SERVER_INFO_1592
def _define_SERVER_INFO_1593_head():
    class SERVER_INFO_1593(Structure):
        pass
    return SERVER_INFO_1593
def _define_SERVER_INFO_1593():
    SERVER_INFO_1593 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1593_head
    SERVER_INFO_1593._fields_ = [
        ('sv1593_enablesecuritysignature', UInt32),
    ]
    return SERVER_INFO_1593
def _define_SERVER_INFO_1594_head():
    class SERVER_INFO_1594(Structure):
        pass
    return SERVER_INFO_1594
def _define_SERVER_INFO_1594():
    SERVER_INFO_1594 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1594_head
    SERVER_INFO_1594._fields_ = [
        ('sv1594_requiresecuritysignature', UInt32),
    ]
    return SERVER_INFO_1594
def _define_SERVER_INFO_1595_head():
    class SERVER_INFO_1595(Structure):
        pass
    return SERVER_INFO_1595
def _define_SERVER_INFO_1595():
    SERVER_INFO_1595 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1595_head
    SERVER_INFO_1595._fields_ = [
        ('sv1595_minclientbuffersize', UInt32),
    ]
    return SERVER_INFO_1595
def _define_SERVER_INFO_1596_head():
    class SERVER_INFO_1596(Structure):
        pass
    return SERVER_INFO_1596
def _define_SERVER_INFO_1596():
    SERVER_INFO_1596 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1596_head
    SERVER_INFO_1596._fields_ = [
        ('sv1596_ConnectionNoSessionsTimeout', UInt32),
    ]
    return SERVER_INFO_1596
def _define_SERVER_INFO_1597_head():
    class SERVER_INFO_1597(Structure):
        pass
    return SERVER_INFO_1597
def _define_SERVER_INFO_1597():
    SERVER_INFO_1597 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1597_head
    SERVER_INFO_1597._fields_ = [
        ('sv1597_IdleThreadTimeOut', UInt32),
    ]
    return SERVER_INFO_1597
def _define_SERVER_INFO_1598_head():
    class SERVER_INFO_1598(Structure):
        pass
    return SERVER_INFO_1598
def _define_SERVER_INFO_1598():
    SERVER_INFO_1598 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1598_head
    SERVER_INFO_1598._fields_ = [
        ('sv1598_enableW9xsecuritysignature', UInt32),
    ]
    return SERVER_INFO_1598
def _define_SERVER_INFO_1599_head():
    class SERVER_INFO_1599(Structure):
        pass
    return SERVER_INFO_1599
def _define_SERVER_INFO_1599():
    SERVER_INFO_1599 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1599_head
    SERVER_INFO_1599._fields_ = [
        ('sv1598_enforcekerberosreauthentication', win32more.Foundation.BOOLEAN),
    ]
    return SERVER_INFO_1599
def _define_SERVER_INFO_1600_head():
    class SERVER_INFO_1600(Structure):
        pass
    return SERVER_INFO_1600
def _define_SERVER_INFO_1600():
    SERVER_INFO_1600 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1600_head
    SERVER_INFO_1600._fields_ = [
        ('sv1598_disabledos', win32more.Foundation.BOOLEAN),
    ]
    return SERVER_INFO_1600
def _define_SERVER_INFO_1601_head():
    class SERVER_INFO_1601(Structure):
        pass
    return SERVER_INFO_1601
def _define_SERVER_INFO_1601():
    SERVER_INFO_1601 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1601_head
    SERVER_INFO_1601._fields_ = [
        ('sv1598_lowdiskspaceminimum', UInt32),
    ]
    return SERVER_INFO_1601
def _define_SERVER_INFO_1602_head():
    class SERVER_INFO_1602(Structure):
        pass
    return SERVER_INFO_1602
def _define_SERVER_INFO_1602():
    SERVER_INFO_1602 = win32more.NetworkManagement.NetManagement.SERVER_INFO_1602_head
    SERVER_INFO_1602._fields_ = [
        ('sv_1598_disablestrictnamechecking', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_1602
def _define_SERVER_INFO_402_head():
    class SERVER_INFO_402(Structure):
        pass
    return SERVER_INFO_402
def _define_SERVER_INFO_402():
    SERVER_INFO_402 = win32more.NetworkManagement.NetManagement.SERVER_INFO_402_head
    SERVER_INFO_402._fields_ = [
        ('sv402_ulist_mtime', UInt32),
        ('sv402_glist_mtime', UInt32),
        ('sv402_alist_mtime', UInt32),
        ('sv402_alerts', win32more.Foundation.PWSTR),
        ('sv402_security', win32more.NetworkManagement.NetManagement.SERVER_INFO_SECURITY),
        ('sv402_numadmin', UInt32),
        ('sv402_lanmask', UInt32),
        ('sv402_guestacct', win32more.Foundation.PWSTR),
        ('sv402_chdevs', UInt32),
        ('sv402_chdevq', UInt32),
        ('sv402_chdevjobs', UInt32),
        ('sv402_connections', UInt32),
        ('sv402_shares', UInt32),
        ('sv402_openfiles', UInt32),
        ('sv402_sessopens', UInt32),
        ('sv402_sessvcs', UInt32),
        ('sv402_sessreqs', UInt32),
        ('sv402_opensearch', UInt32),
        ('sv402_activelocks', UInt32),
        ('sv402_numreqbuf', UInt32),
        ('sv402_sizreqbuf', UInt32),
        ('sv402_numbigbuf', UInt32),
        ('sv402_numfiletasks', UInt32),
        ('sv402_alertsched', UInt32),
        ('sv402_erroralert', UInt32),
        ('sv402_logonalert', UInt32),
        ('sv402_accessalert', UInt32),
        ('sv402_diskalert', UInt32),
        ('sv402_netioalert', UInt32),
        ('sv402_maxauditsz', UInt32),
        ('sv402_srvheuristics', win32more.Foundation.PWSTR),
    ]
    return SERVER_INFO_402
def _define_SERVER_INFO_403_head():
    class SERVER_INFO_403(Structure):
        pass
    return SERVER_INFO_403
def _define_SERVER_INFO_403():
    SERVER_INFO_403 = win32more.NetworkManagement.NetManagement.SERVER_INFO_403_head
    SERVER_INFO_403._fields_ = [
        ('sv403_ulist_mtime', UInt32),
        ('sv403_glist_mtime', UInt32),
        ('sv403_alist_mtime', UInt32),
        ('sv403_alerts', win32more.Foundation.PWSTR),
        ('sv403_security', win32more.NetworkManagement.NetManagement.SERVER_INFO_SECURITY),
        ('sv403_numadmin', UInt32),
        ('sv403_lanmask', UInt32),
        ('sv403_guestacct', win32more.Foundation.PWSTR),
        ('sv403_chdevs', UInt32),
        ('sv403_chdevq', UInt32),
        ('sv403_chdevjobs', UInt32),
        ('sv403_connections', UInt32),
        ('sv403_shares', UInt32),
        ('sv403_openfiles', UInt32),
        ('sv403_sessopens', UInt32),
        ('sv403_sessvcs', UInt32),
        ('sv403_sessreqs', UInt32),
        ('sv403_opensearch', UInt32),
        ('sv403_activelocks', UInt32),
        ('sv403_numreqbuf', UInt32),
        ('sv403_sizreqbuf', UInt32),
        ('sv403_numbigbuf', UInt32),
        ('sv403_numfiletasks', UInt32),
        ('sv403_alertsched', UInt32),
        ('sv403_erroralert', UInt32),
        ('sv403_logonalert', UInt32),
        ('sv403_accessalert', UInt32),
        ('sv403_diskalert', UInt32),
        ('sv403_netioalert', UInt32),
        ('sv403_maxauditsz', UInt32),
        ('sv403_srvheuristics', win32more.Foundation.PWSTR),
        ('sv403_auditedevents', UInt32),
        ('sv403_autoprofile', UInt32),
        ('sv403_autopath', win32more.Foundation.PWSTR),
    ]
    return SERVER_INFO_403
def _define_SERVER_INFO_502_head():
    class SERVER_INFO_502(Structure):
        pass
    return SERVER_INFO_502
def _define_SERVER_INFO_502():
    SERVER_INFO_502 = win32more.NetworkManagement.NetManagement.SERVER_INFO_502_head
    SERVER_INFO_502._fields_ = [
        ('sv502_sessopens', UInt32),
        ('sv502_sessvcs', UInt32),
        ('sv502_opensearch', UInt32),
        ('sv502_sizreqbuf', UInt32),
        ('sv502_initworkitems', UInt32),
        ('sv502_maxworkitems', UInt32),
        ('sv502_rawworkitems', UInt32),
        ('sv502_irpstacksize', UInt32),
        ('sv502_maxrawbuflen', UInt32),
        ('sv502_sessusers', UInt32),
        ('sv502_sessconns', UInt32),
        ('sv502_maxpagedmemoryusage', UInt32),
        ('sv502_maxnonpagedmemoryusage', UInt32),
        ('sv502_enablesoftcompat', win32more.Foundation.BOOL),
        ('sv502_enableforcedlogoff', win32more.Foundation.BOOL),
        ('sv502_timesource', win32more.Foundation.BOOL),
        ('sv502_acceptdownlevelapis', win32more.Foundation.BOOL),
        ('sv502_lmannounce', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_502
def _define_SERVER_INFO_503_head():
    class SERVER_INFO_503(Structure):
        pass
    return SERVER_INFO_503
def _define_SERVER_INFO_503():
    SERVER_INFO_503 = win32more.NetworkManagement.NetManagement.SERVER_INFO_503_head
    SERVER_INFO_503._fields_ = [
        ('sv503_sessopens', UInt32),
        ('sv503_sessvcs', UInt32),
        ('sv503_opensearch', UInt32),
        ('sv503_sizreqbuf', UInt32),
        ('sv503_initworkitems', UInt32),
        ('sv503_maxworkitems', UInt32),
        ('sv503_rawworkitems', UInt32),
        ('sv503_irpstacksize', UInt32),
        ('sv503_maxrawbuflen', UInt32),
        ('sv503_sessusers', UInt32),
        ('sv503_sessconns', UInt32),
        ('sv503_maxpagedmemoryusage', UInt32),
        ('sv503_maxnonpagedmemoryusage', UInt32),
        ('sv503_enablesoftcompat', win32more.Foundation.BOOL),
        ('sv503_enableforcedlogoff', win32more.Foundation.BOOL),
        ('sv503_timesource', win32more.Foundation.BOOL),
        ('sv503_acceptdownlevelapis', win32more.Foundation.BOOL),
        ('sv503_lmannounce', win32more.Foundation.BOOL),
        ('sv503_domain', win32more.Foundation.PWSTR),
        ('sv503_maxcopyreadlen', UInt32),
        ('sv503_maxcopywritelen', UInt32),
        ('sv503_minkeepsearch', UInt32),
        ('sv503_maxkeepsearch', UInt32),
        ('sv503_minkeepcomplsearch', UInt32),
        ('sv503_maxkeepcomplsearch', UInt32),
        ('sv503_threadcountadd', UInt32),
        ('sv503_numblockthreads', UInt32),
        ('sv503_scavtimeout', UInt32),
        ('sv503_minrcvqueue', UInt32),
        ('sv503_minfreeworkitems', UInt32),
        ('sv503_xactmemsize', UInt32),
        ('sv503_threadpriority', UInt32),
        ('sv503_maxmpxct', UInt32),
        ('sv503_oplockbreakwait', UInt32),
        ('sv503_oplockbreakresponsewait', UInt32),
        ('sv503_enableoplocks', win32more.Foundation.BOOL),
        ('sv503_enableoplockforceclose', win32more.Foundation.BOOL),
        ('sv503_enablefcbopens', win32more.Foundation.BOOL),
        ('sv503_enableraw', win32more.Foundation.BOOL),
        ('sv503_enablesharednetdrives', win32more.Foundation.BOOL),
        ('sv503_minfreeconnections', UInt32),
        ('sv503_maxfreeconnections', UInt32),
    ]
    return SERVER_INFO_503
def _define_SERVER_INFO_598_head():
    class SERVER_INFO_598(Structure):
        pass
    return SERVER_INFO_598
def _define_SERVER_INFO_598():
    SERVER_INFO_598 = win32more.NetworkManagement.NetManagement.SERVER_INFO_598_head
    SERVER_INFO_598._fields_ = [
        ('sv598_maxrawworkitems', UInt32),
        ('sv598_maxthreadsperqueue', UInt32),
        ('sv598_producttype', UInt32),
        ('sv598_serversize', UInt32),
        ('sv598_connectionlessautodisc', UInt32),
        ('sv598_sharingviolationretries', UInt32),
        ('sv598_sharingviolationdelay', UInt32),
        ('sv598_maxglobalopensearch', UInt32),
        ('sv598_removeduplicatesearches', UInt32),
        ('sv598_lockviolationoffset', UInt32),
        ('sv598_lockviolationdelay', UInt32),
        ('sv598_mdlreadswitchover', UInt32),
        ('sv598_cachedopenlimit', UInt32),
        ('sv598_otherqueueaffinity', UInt32),
        ('sv598_restrictnullsessaccess', win32more.Foundation.BOOL),
        ('sv598_enablewfw311directipx', win32more.Foundation.BOOL),
        ('sv598_queuesamplesecs', UInt32),
        ('sv598_balancecount', UInt32),
        ('sv598_preferredaffinity', UInt32),
        ('sv598_maxfreerfcbs', UInt32),
        ('sv598_maxfreemfcbs', UInt32),
        ('sv598_maxfreelfcbs', UInt32),
        ('sv598_maxfreepagedpoolchunks', UInt32),
        ('sv598_minpagedpoolchunksize', UInt32),
        ('sv598_maxpagedpoolchunksize', UInt32),
        ('sv598_sendsfrompreferredprocessor', win32more.Foundation.BOOL),
        ('sv598_cacheddirectorylimit', UInt32),
        ('sv598_maxcopylength', UInt32),
        ('sv598_enablecompression', win32more.Foundation.BOOL),
        ('sv598_autosharewks', win32more.Foundation.BOOL),
        ('sv598_autoshareserver', win32more.Foundation.BOOL),
        ('sv598_enablesecuritysignature', win32more.Foundation.BOOL),
        ('sv598_requiresecuritysignature', win32more.Foundation.BOOL),
        ('sv598_minclientbuffersize', UInt32),
        ('sv598_serverguid', Guid),
        ('sv598_ConnectionNoSessionsTimeout', UInt32),
        ('sv598_IdleThreadTimeOut', UInt32),
        ('sv598_enableW9xsecuritysignature', win32more.Foundation.BOOL),
        ('sv598_enforcekerberosreauthentication', win32more.Foundation.BOOL),
        ('sv598_disabledos', win32more.Foundation.BOOL),
        ('sv598_lowdiskspaceminimum', UInt32),
        ('sv598_disablestrictnamechecking', win32more.Foundation.BOOL),
        ('sv598_enableauthenticateusersharing', win32more.Foundation.BOOL),
    ]
    return SERVER_INFO_598
def _define_SERVER_INFO_599_head():
    class SERVER_INFO_599(Structure):
        pass
    return SERVER_INFO_599
def _define_SERVER_INFO_599():
    SERVER_INFO_599 = win32more.NetworkManagement.NetManagement.SERVER_INFO_599_head
    SERVER_INFO_599._fields_ = [
        ('sv599_sessopens', UInt32),
        ('sv599_sessvcs', UInt32),
        ('sv599_opensearch', UInt32),
        ('sv599_sizreqbuf', UInt32),
        ('sv599_initworkitems', UInt32),
        ('sv599_maxworkitems', UInt32),
        ('sv599_rawworkitems', UInt32),
        ('sv599_irpstacksize', UInt32),
        ('sv599_maxrawbuflen', UInt32),
        ('sv599_sessusers', UInt32),
        ('sv599_sessconns', UInt32),
        ('sv599_maxpagedmemoryusage', UInt32),
        ('sv599_maxnonpagedmemoryusage', UInt32),
        ('sv599_enablesoftcompat', win32more.Foundation.BOOL),
        ('sv599_enableforcedlogoff', win32more.Foundation.BOOL),
        ('sv599_timesource', win32more.Foundation.BOOL),
        ('sv599_acceptdownlevelapis', win32more.Foundation.BOOL),
        ('sv599_lmannounce', win32more.Foundation.BOOL),
        ('sv599_domain', win32more.Foundation.PWSTR),
        ('sv599_maxcopyreadlen', UInt32),
        ('sv599_maxcopywritelen', UInt32),
        ('sv599_minkeepsearch', UInt32),
        ('sv599_maxkeepsearch', UInt32),
        ('sv599_minkeepcomplsearch', UInt32),
        ('sv599_maxkeepcomplsearch', UInt32),
        ('sv599_threadcountadd', UInt32),
        ('sv599_numblockthreads', UInt32),
        ('sv599_scavtimeout', UInt32),
        ('sv599_minrcvqueue', UInt32),
        ('sv599_minfreeworkitems', UInt32),
        ('sv599_xactmemsize', UInt32),
        ('sv599_threadpriority', UInt32),
        ('sv599_maxmpxct', UInt32),
        ('sv599_oplockbreakwait', UInt32),
        ('sv599_oplockbreakresponsewait', UInt32),
        ('sv599_enableoplocks', win32more.Foundation.BOOL),
        ('sv599_enableoplockforceclose', win32more.Foundation.BOOL),
        ('sv599_enablefcbopens', win32more.Foundation.BOOL),
        ('sv599_enableraw', win32more.Foundation.BOOL),
        ('sv599_enablesharednetdrives', win32more.Foundation.BOOL),
        ('sv599_minfreeconnections', UInt32),
        ('sv599_maxfreeconnections', UInt32),
        ('sv599_initsesstable', UInt32),
        ('sv599_initconntable', UInt32),
        ('sv599_initfiletable', UInt32),
        ('sv599_initsearchtable', UInt32),
        ('sv599_alertschedule', UInt32),
        ('sv599_errorthreshold', UInt32),
        ('sv599_networkerrorthreshold', UInt32),
        ('sv599_diskspacethreshold', UInt32),
        ('sv599_reserved', UInt32),
        ('sv599_maxlinkdelay', UInt32),
        ('sv599_minlinkthroughput', UInt32),
        ('sv599_linkinfovalidtime', UInt32),
        ('sv599_scavqosinfoupdatetime', UInt32),
        ('sv599_maxworkitemidletime', UInt32),
    ]
    return SERVER_INFO_599
SERVER_INFO_HIDDEN = UInt32
SV_VISIBLE = 0
SV_HIDDEN = 1
SERVER_INFO_SECURITY = UInt32
SV_SHARESECURITY = 0
SV_USERSECURITY = 1
def _define_SERVER_TRANSPORT_INFO_0_head():
    class SERVER_TRANSPORT_INFO_0(Structure):
        pass
    return SERVER_TRANSPORT_INFO_0
def _define_SERVER_TRANSPORT_INFO_0():
    SERVER_TRANSPORT_INFO_0 = win32more.NetworkManagement.NetManagement.SERVER_TRANSPORT_INFO_0_head
    SERVER_TRANSPORT_INFO_0._fields_ = [
        ('svti0_numberofvcs', UInt32),
        ('svti0_transportname', win32more.Foundation.PWSTR),
        ('svti0_transportaddress', c_char_p_no),
        ('svti0_transportaddresslength', UInt32),
        ('svti0_networkaddress', win32more.Foundation.PWSTR),
    ]
    return SERVER_TRANSPORT_INFO_0
def _define_SERVER_TRANSPORT_INFO_1_head():
    class SERVER_TRANSPORT_INFO_1(Structure):
        pass
    return SERVER_TRANSPORT_INFO_1
def _define_SERVER_TRANSPORT_INFO_1():
    SERVER_TRANSPORT_INFO_1 = win32more.NetworkManagement.NetManagement.SERVER_TRANSPORT_INFO_1_head
    SERVER_TRANSPORT_INFO_1._fields_ = [
        ('svti1_numberofvcs', UInt32),
        ('svti1_transportname', win32more.Foundation.PWSTR),
        ('svti1_transportaddress', c_char_p_no),
        ('svti1_transportaddresslength', UInt32),
        ('svti1_networkaddress', win32more.Foundation.PWSTR),
        ('svti1_domain', win32more.Foundation.PWSTR),
    ]
    return SERVER_TRANSPORT_INFO_1
def _define_SERVER_TRANSPORT_INFO_2_head():
    class SERVER_TRANSPORT_INFO_2(Structure):
        pass
    return SERVER_TRANSPORT_INFO_2
def _define_SERVER_TRANSPORT_INFO_2():
    SERVER_TRANSPORT_INFO_2 = win32more.NetworkManagement.NetManagement.SERVER_TRANSPORT_INFO_2_head
    SERVER_TRANSPORT_INFO_2._fields_ = [
        ('svti2_numberofvcs', UInt32),
        ('svti2_transportname', win32more.Foundation.PWSTR),
        ('svti2_transportaddress', c_char_p_no),
        ('svti2_transportaddresslength', UInt32),
        ('svti2_networkaddress', win32more.Foundation.PWSTR),
        ('svti2_domain', win32more.Foundation.PWSTR),
        ('svti2_flags', UInt32),
    ]
    return SERVER_TRANSPORT_INFO_2
def _define_SERVER_TRANSPORT_INFO_3_head():
    class SERVER_TRANSPORT_INFO_3(Structure):
        pass
    return SERVER_TRANSPORT_INFO_3
def _define_SERVER_TRANSPORT_INFO_3():
    SERVER_TRANSPORT_INFO_3 = win32more.NetworkManagement.NetManagement.SERVER_TRANSPORT_INFO_3_head
    SERVER_TRANSPORT_INFO_3._fields_ = [
        ('svti3_numberofvcs', UInt32),
        ('svti3_transportname', win32more.Foundation.PWSTR),
        ('svti3_transportaddress', c_char_p_no),
        ('svti3_transportaddresslength', UInt32),
        ('svti3_networkaddress', win32more.Foundation.PWSTR),
        ('svti3_domain', win32more.Foundation.PWSTR),
        ('svti3_flags', UInt32),
        ('svti3_passwordlength', UInt32),
        ('svti3_password', Byte * 256),
    ]
    return SERVER_TRANSPORT_INFO_3
def _define_SERVICE_INFO_0_head():
    class SERVICE_INFO_0(Structure):
        pass
    return SERVICE_INFO_0
def _define_SERVICE_INFO_0():
    SERVICE_INFO_0 = win32more.NetworkManagement.NetManagement.SERVICE_INFO_0_head
    SERVICE_INFO_0._fields_ = [
        ('svci0_name', win32more.Foundation.PWSTR),
    ]
    return SERVICE_INFO_0
def _define_SERVICE_INFO_1_head():
    class SERVICE_INFO_1(Structure):
        pass
    return SERVICE_INFO_1
def _define_SERVICE_INFO_1():
    SERVICE_INFO_1 = win32more.NetworkManagement.NetManagement.SERVICE_INFO_1_head
    SERVICE_INFO_1._fields_ = [
        ('svci1_name', win32more.Foundation.PWSTR),
        ('svci1_status', UInt32),
        ('svci1_code', UInt32),
        ('svci1_pid', UInt32),
    ]
    return SERVICE_INFO_1
def _define_SERVICE_INFO_2_head():
    class SERVICE_INFO_2(Structure):
        pass
    return SERVICE_INFO_2
def _define_SERVICE_INFO_2():
    SERVICE_INFO_2 = win32more.NetworkManagement.NetManagement.SERVICE_INFO_2_head
    SERVICE_INFO_2._fields_ = [
        ('svci2_name', win32more.Foundation.PWSTR),
        ('svci2_status', UInt32),
        ('svci2_code', UInt32),
        ('svci2_pid', UInt32),
        ('svci2_text', win32more.Foundation.PWSTR),
        ('svci2_specific_error', UInt32),
        ('svci2_display_name', win32more.Foundation.PWSTR),
    ]
    return SERVICE_INFO_2
def _define_SMB_COMPRESSION_INFO_head():
    class SMB_COMPRESSION_INFO(Structure):
        pass
    return SMB_COMPRESSION_INFO
def _define_SMB_COMPRESSION_INFO():
    SMB_COMPRESSION_INFO = win32more.NetworkManagement.NetManagement.SMB_COMPRESSION_INFO_head
    SMB_COMPRESSION_INFO._fields_ = [
        ('Switch', win32more.Foundation.BOOLEAN),
        ('Reserved1', Byte),
        ('Reserved2', UInt16),
        ('Reserved3', UInt32),
    ]
    return SMB_COMPRESSION_INFO
def _define_SMB_TREE_CONNECT_PARAMETERS_head():
    class SMB_TREE_CONNECT_PARAMETERS(Structure):
        pass
    return SMB_TREE_CONNECT_PARAMETERS
def _define_SMB_TREE_CONNECT_PARAMETERS():
    SMB_TREE_CONNECT_PARAMETERS = win32more.NetworkManagement.NetManagement.SMB_TREE_CONNECT_PARAMETERS_head
    SMB_TREE_CONNECT_PARAMETERS._fields_ = [
        ('EABufferOffset', UInt32),
        ('EABufferLen', UInt32),
        ('CreateOptions', UInt32),
        ('TreeConnectAttributes', UInt32),
    ]
    return SMB_TREE_CONNECT_PARAMETERS
def _define_SMB_USE_OPTION_COMPRESSION_PARAMETERS_head():
    class SMB_USE_OPTION_COMPRESSION_PARAMETERS(Structure):
        pass
    return SMB_USE_OPTION_COMPRESSION_PARAMETERS
def _define_SMB_USE_OPTION_COMPRESSION_PARAMETERS():
    SMB_USE_OPTION_COMPRESSION_PARAMETERS = win32more.NetworkManagement.NetManagement.SMB_USE_OPTION_COMPRESSION_PARAMETERS_head
    SMB_USE_OPTION_COMPRESSION_PARAMETERS._fields_ = [
        ('Tag', UInt32),
        ('Length', UInt16),
        ('Reserved', UInt16),
    ]
    return SMB_USE_OPTION_COMPRESSION_PARAMETERS
def _define_STD_ALERT_head():
    class STD_ALERT(Structure):
        pass
    return STD_ALERT
def _define_STD_ALERT():
    STD_ALERT = win32more.NetworkManagement.NetManagement.STD_ALERT_head
    STD_ALERT._fields_ = [
        ('alrt_timestamp', UInt32),
        ('alrt_eventname', Char * 17),
        ('alrt_servicename', Char * 81),
    ]
    return STD_ALERT
SUPPORTS_BINDING_INTERFACE_FLAGS = Int32
NCF_LOWER = 1
NCF_UPPER = 2
def _define_TIME_OF_DAY_INFO_head():
    class TIME_OF_DAY_INFO(Structure):
        pass
    return TIME_OF_DAY_INFO
def _define_TIME_OF_DAY_INFO():
    TIME_OF_DAY_INFO = win32more.NetworkManagement.NetManagement.TIME_OF_DAY_INFO_head
    TIME_OF_DAY_INFO._fields_ = [
        ('tod_elapsedt', UInt32),
        ('tod_msecs', UInt32),
        ('tod_hours', UInt32),
        ('tod_mins', UInt32),
        ('tod_secs', UInt32),
        ('tod_hunds', UInt32),
        ('tod_timezone', Int32),
        ('tod_tinterval', UInt32),
        ('tod_day', UInt32),
        ('tod_month', UInt32),
        ('tod_year', UInt32),
        ('tod_weekday', UInt32),
    ]
    return TIME_OF_DAY_INFO
def _define_TRANSPORT_INFO_head():
    class TRANSPORT_INFO(Structure):
        pass
    return TRANSPORT_INFO
def _define_TRANSPORT_INFO():
    TRANSPORT_INFO = win32more.NetworkManagement.NetManagement.TRANSPORT_INFO_head
    TRANSPORT_INFO._fields_ = [
        ('Type', win32more.NetworkManagement.NetManagement.TRANSPORT_TYPE),
        ('SkipCertificateCheck', win32more.Foundation.BOOLEAN),
    ]
    return TRANSPORT_INFO
TRANSPORT_TYPE = Int32
UseTransportType_None = 0
UseTransportType_Wsk = 1
UseTransportType_Quic = 2
def _define_USE_INFO_0_head():
    class USE_INFO_0(Structure):
        pass
    return USE_INFO_0
def _define_USE_INFO_0():
    USE_INFO_0 = win32more.NetworkManagement.NetManagement.USE_INFO_0_head
    USE_INFO_0._fields_ = [
        ('ui0_local', win32more.Foundation.PWSTR),
        ('ui0_remote', win32more.Foundation.PWSTR),
    ]
    return USE_INFO_0
def _define_USE_INFO_1_head():
    class USE_INFO_1(Structure):
        pass
    return USE_INFO_1
def _define_USE_INFO_1():
    USE_INFO_1 = win32more.NetworkManagement.NetManagement.USE_INFO_1_head
    USE_INFO_1._fields_ = [
        ('ui1_local', win32more.Foundation.PWSTR),
        ('ui1_remote', win32more.Foundation.PWSTR),
        ('ui1_password', win32more.Foundation.PWSTR),
        ('ui1_status', UInt32),
        ('ui1_asg_type', win32more.NetworkManagement.NetManagement.USE_INFO_ASG_TYPE),
        ('ui1_refcount', UInt32),
        ('ui1_usecount', UInt32),
    ]
    return USE_INFO_1
def _define_USE_INFO_2_head():
    class USE_INFO_2(Structure):
        pass
    return USE_INFO_2
def _define_USE_INFO_2():
    USE_INFO_2 = win32more.NetworkManagement.NetManagement.USE_INFO_2_head
    USE_INFO_2._fields_ = [
        ('ui2_local', win32more.Foundation.PWSTR),
        ('ui2_remote', win32more.Foundation.PWSTR),
        ('ui2_password', win32more.Foundation.PWSTR),
        ('ui2_status', UInt32),
        ('ui2_asg_type', win32more.NetworkManagement.NetManagement.USE_INFO_ASG_TYPE),
        ('ui2_refcount', UInt32),
        ('ui2_usecount', UInt32),
        ('ui2_username', win32more.Foundation.PWSTR),
        ('ui2_domainname', win32more.Foundation.PWSTR),
    ]
    return USE_INFO_2
def _define_USE_INFO_3_head():
    class USE_INFO_3(Structure):
        pass
    return USE_INFO_3
def _define_USE_INFO_3():
    USE_INFO_3 = win32more.NetworkManagement.NetManagement.USE_INFO_3_head
    USE_INFO_3._fields_ = [
        ('ui3_ui2', win32more.NetworkManagement.NetManagement.USE_INFO_2),
        ('ui3_flags', UInt32),
    ]
    return USE_INFO_3
def _define_USE_INFO_4_head():
    class USE_INFO_4(Structure):
        pass
    return USE_INFO_4
def _define_USE_INFO_4():
    USE_INFO_4 = win32more.NetworkManagement.NetManagement.USE_INFO_4_head
    USE_INFO_4._fields_ = [
        ('ui4_ui3', win32more.NetworkManagement.NetManagement.USE_INFO_3),
        ('ui4_auth_identity_length', UInt32),
        ('ui4_auth_identity', c_char_p_no),
    ]
    return USE_INFO_4
def _define_USE_INFO_5_head():
    class USE_INFO_5(Structure):
        pass
    return USE_INFO_5
def _define_USE_INFO_5():
    USE_INFO_5 = win32more.NetworkManagement.NetManagement.USE_INFO_5_head
    USE_INFO_5._fields_ = [
        ('ui4_ui3', win32more.NetworkManagement.NetManagement.USE_INFO_3),
        ('ui4_auth_identity_length', UInt32),
        ('ui4_auth_identity', c_char_p_no),
        ('ui5_security_descriptor_length', UInt32),
        ('ui5_security_descriptor', c_char_p_no),
        ('ui5_use_options_length', UInt32),
        ('ui5_use_options', c_char_p_no),
    ]
    return USE_INFO_5
USE_INFO_ASG_TYPE = UInt32
USE_WILDCARD = 4294967295
USE_DISKDEV = 0
USE_SPOOLDEV = 1
USE_IPC = 3
def _define_USE_OPTION_DEFERRED_CONNECTION_PARAMETERS_head():
    class USE_OPTION_DEFERRED_CONNECTION_PARAMETERS(Structure):
        pass
    return USE_OPTION_DEFERRED_CONNECTION_PARAMETERS
def _define_USE_OPTION_DEFERRED_CONNECTION_PARAMETERS():
    USE_OPTION_DEFERRED_CONNECTION_PARAMETERS = win32more.NetworkManagement.NetManagement.USE_OPTION_DEFERRED_CONNECTION_PARAMETERS_head
    USE_OPTION_DEFERRED_CONNECTION_PARAMETERS._fields_ = [
        ('Tag', UInt32),
        ('Length', UInt16),
        ('Reserved', UInt16),
    ]
    return USE_OPTION_DEFERRED_CONNECTION_PARAMETERS
def _define_USE_OPTION_GENERIC_head():
    class USE_OPTION_GENERIC(Structure):
        pass
    return USE_OPTION_GENERIC
def _define_USE_OPTION_GENERIC():
    USE_OPTION_GENERIC = win32more.NetworkManagement.NetManagement.USE_OPTION_GENERIC_head
    USE_OPTION_GENERIC._fields_ = [
        ('Tag', UInt32),
        ('Length', UInt16),
        ('Reserved', UInt16),
    ]
    return USE_OPTION_GENERIC
def _define_USE_OPTION_PROPERTIES_head():
    class USE_OPTION_PROPERTIES(Structure):
        pass
    return USE_OPTION_PROPERTIES
def _define_USE_OPTION_PROPERTIES():
    USE_OPTION_PROPERTIES = win32more.NetworkManagement.NetManagement.USE_OPTION_PROPERTIES_head
    USE_OPTION_PROPERTIES._fields_ = [
        ('Tag', UInt32),
        ('pInfo', c_void_p),
        ('Length', UIntPtr),
    ]
    return USE_OPTION_PROPERTIES
def _define_USE_OPTION_TRANSPORT_PARAMETERS_head():
    class USE_OPTION_TRANSPORT_PARAMETERS(Structure):
        pass
    return USE_OPTION_TRANSPORT_PARAMETERS
def _define_USE_OPTION_TRANSPORT_PARAMETERS():
    USE_OPTION_TRANSPORT_PARAMETERS = win32more.NetworkManagement.NetManagement.USE_OPTION_TRANSPORT_PARAMETERS_head
    USE_OPTION_TRANSPORT_PARAMETERS._fields_ = [
        ('Tag', UInt32),
        ('Length', UInt16),
        ('Reserved', UInt16),
    ]
    return USE_OPTION_TRANSPORT_PARAMETERS
USER_ACCOUNT_FLAGS = UInt32
UF_SCRIPT = 1
UF_ACCOUNTDISABLE = 2
UF_HOMEDIR_REQUIRED = 8
UF_PASSWD_NOTREQD = 32
UF_PASSWD_CANT_CHANGE = 64
UF_LOCKOUT = 16
UF_DONT_EXPIRE_PASSWD = 65536
UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED = 128
UF_NOT_DELEGATED = 1048576
UF_SMARTCARD_REQUIRED = 262144
UF_USE_DES_KEY_ONLY = 2097152
UF_DONT_REQUIRE_PREAUTH = 4194304
UF_TRUSTED_FOR_DELEGATION = 524288
UF_PASSWORD_EXPIRED = 8388608
UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION = 16777216
def _define_USER_INFO_0_head():
    class USER_INFO_0(Structure):
        pass
    return USER_INFO_0
def _define_USER_INFO_0():
    USER_INFO_0 = win32more.NetworkManagement.NetManagement.USER_INFO_0_head
    USER_INFO_0._fields_ = [
        ('usri0_name', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_0
def _define_USER_INFO_1_head():
    class USER_INFO_1(Structure):
        pass
    return USER_INFO_1
def _define_USER_INFO_1():
    USER_INFO_1 = win32more.NetworkManagement.NetManagement.USER_INFO_1_head
    USER_INFO_1._fields_ = [
        ('usri1_name', win32more.Foundation.PWSTR),
        ('usri1_password', win32more.Foundation.PWSTR),
        ('usri1_password_age', UInt32),
        ('usri1_priv', win32more.NetworkManagement.NetManagement.USER_PRIV),
        ('usri1_home_dir', win32more.Foundation.PWSTR),
        ('usri1_comment', win32more.Foundation.PWSTR),
        ('usri1_flags', win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS),
        ('usri1_script_path', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1
def _define_USER_INFO_10_head():
    class USER_INFO_10(Structure):
        pass
    return USER_INFO_10
def _define_USER_INFO_10():
    USER_INFO_10 = win32more.NetworkManagement.NetManagement.USER_INFO_10_head
    USER_INFO_10._fields_ = [
        ('usri10_name', win32more.Foundation.PWSTR),
        ('usri10_comment', win32more.Foundation.PWSTR),
        ('usri10_usr_comment', win32more.Foundation.PWSTR),
        ('usri10_full_name', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_10
def _define_USER_INFO_1003_head():
    class USER_INFO_1003(Structure):
        pass
    return USER_INFO_1003
def _define_USER_INFO_1003():
    USER_INFO_1003 = win32more.NetworkManagement.NetManagement.USER_INFO_1003_head
    USER_INFO_1003._fields_ = [
        ('usri1003_password', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1003
def _define_USER_INFO_1005_head():
    class USER_INFO_1005(Structure):
        pass
    return USER_INFO_1005
def _define_USER_INFO_1005():
    USER_INFO_1005 = win32more.NetworkManagement.NetManagement.USER_INFO_1005_head
    USER_INFO_1005._fields_ = [
        ('usri1005_priv', win32more.NetworkManagement.NetManagement.USER_PRIV),
    ]
    return USER_INFO_1005
def _define_USER_INFO_1006_head():
    class USER_INFO_1006(Structure):
        pass
    return USER_INFO_1006
def _define_USER_INFO_1006():
    USER_INFO_1006 = win32more.NetworkManagement.NetManagement.USER_INFO_1006_head
    USER_INFO_1006._fields_ = [
        ('usri1006_home_dir', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1006
def _define_USER_INFO_1007_head():
    class USER_INFO_1007(Structure):
        pass
    return USER_INFO_1007
def _define_USER_INFO_1007():
    USER_INFO_1007 = win32more.NetworkManagement.NetManagement.USER_INFO_1007_head
    USER_INFO_1007._fields_ = [
        ('usri1007_comment', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1007
def _define_USER_INFO_1008_head():
    class USER_INFO_1008(Structure):
        pass
    return USER_INFO_1008
def _define_USER_INFO_1008():
    USER_INFO_1008 = win32more.NetworkManagement.NetManagement.USER_INFO_1008_head
    USER_INFO_1008._fields_ = [
        ('usri1008_flags', win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS),
    ]
    return USER_INFO_1008
def _define_USER_INFO_1009_head():
    class USER_INFO_1009(Structure):
        pass
    return USER_INFO_1009
def _define_USER_INFO_1009():
    USER_INFO_1009 = win32more.NetworkManagement.NetManagement.USER_INFO_1009_head
    USER_INFO_1009._fields_ = [
        ('usri1009_script_path', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1009
def _define_USER_INFO_1010_head():
    class USER_INFO_1010(Structure):
        pass
    return USER_INFO_1010
def _define_USER_INFO_1010():
    USER_INFO_1010 = win32more.NetworkManagement.NetManagement.USER_INFO_1010_head
    USER_INFO_1010._fields_ = [
        ('usri1010_auth_flags', win32more.NetworkManagement.NetManagement.AF_OP),
    ]
    return USER_INFO_1010
def _define_USER_INFO_1011_head():
    class USER_INFO_1011(Structure):
        pass
    return USER_INFO_1011
def _define_USER_INFO_1011():
    USER_INFO_1011 = win32more.NetworkManagement.NetManagement.USER_INFO_1011_head
    USER_INFO_1011._fields_ = [
        ('usri1011_full_name', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1011
def _define_USER_INFO_1012_head():
    class USER_INFO_1012(Structure):
        pass
    return USER_INFO_1012
def _define_USER_INFO_1012():
    USER_INFO_1012 = win32more.NetworkManagement.NetManagement.USER_INFO_1012_head
    USER_INFO_1012._fields_ = [
        ('usri1012_usr_comment', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1012
def _define_USER_INFO_1013_head():
    class USER_INFO_1013(Structure):
        pass
    return USER_INFO_1013
def _define_USER_INFO_1013():
    USER_INFO_1013 = win32more.NetworkManagement.NetManagement.USER_INFO_1013_head
    USER_INFO_1013._fields_ = [
        ('usri1013_parms', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1013
def _define_USER_INFO_1014_head():
    class USER_INFO_1014(Structure):
        pass
    return USER_INFO_1014
def _define_USER_INFO_1014():
    USER_INFO_1014 = win32more.NetworkManagement.NetManagement.USER_INFO_1014_head
    USER_INFO_1014._fields_ = [
        ('usri1014_workstations', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1014
def _define_USER_INFO_1017_head():
    class USER_INFO_1017(Structure):
        pass
    return USER_INFO_1017
def _define_USER_INFO_1017():
    USER_INFO_1017 = win32more.NetworkManagement.NetManagement.USER_INFO_1017_head
    USER_INFO_1017._fields_ = [
        ('usri1017_acct_expires', UInt32),
    ]
    return USER_INFO_1017
def _define_USER_INFO_1018_head():
    class USER_INFO_1018(Structure):
        pass
    return USER_INFO_1018
def _define_USER_INFO_1018():
    USER_INFO_1018 = win32more.NetworkManagement.NetManagement.USER_INFO_1018_head
    USER_INFO_1018._fields_ = [
        ('usri1018_max_storage', UInt32),
    ]
    return USER_INFO_1018
def _define_USER_INFO_1020_head():
    class USER_INFO_1020(Structure):
        pass
    return USER_INFO_1020
def _define_USER_INFO_1020():
    USER_INFO_1020 = win32more.NetworkManagement.NetManagement.USER_INFO_1020_head
    USER_INFO_1020._fields_ = [
        ('usri1020_units_per_week', UInt32),
        ('usri1020_logon_hours', c_char_p_no),
    ]
    return USER_INFO_1020
def _define_USER_INFO_1023_head():
    class USER_INFO_1023(Structure):
        pass
    return USER_INFO_1023
def _define_USER_INFO_1023():
    USER_INFO_1023 = win32more.NetworkManagement.NetManagement.USER_INFO_1023_head
    USER_INFO_1023._fields_ = [
        ('usri1023_logon_server', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1023
def _define_USER_INFO_1024_head():
    class USER_INFO_1024(Structure):
        pass
    return USER_INFO_1024
def _define_USER_INFO_1024():
    USER_INFO_1024 = win32more.NetworkManagement.NetManagement.USER_INFO_1024_head
    USER_INFO_1024._fields_ = [
        ('usri1024_country_code', UInt32),
    ]
    return USER_INFO_1024
def _define_USER_INFO_1025_head():
    class USER_INFO_1025(Structure):
        pass
    return USER_INFO_1025
def _define_USER_INFO_1025():
    USER_INFO_1025 = win32more.NetworkManagement.NetManagement.USER_INFO_1025_head
    USER_INFO_1025._fields_ = [
        ('usri1025_code_page', UInt32),
    ]
    return USER_INFO_1025
def _define_USER_INFO_1051_head():
    class USER_INFO_1051(Structure):
        pass
    return USER_INFO_1051
def _define_USER_INFO_1051():
    USER_INFO_1051 = win32more.NetworkManagement.NetManagement.USER_INFO_1051_head
    USER_INFO_1051._fields_ = [
        ('usri1051_primary_group_id', UInt32),
    ]
    return USER_INFO_1051
def _define_USER_INFO_1052_head():
    class USER_INFO_1052(Structure):
        pass
    return USER_INFO_1052
def _define_USER_INFO_1052():
    USER_INFO_1052 = win32more.NetworkManagement.NetManagement.USER_INFO_1052_head
    USER_INFO_1052._fields_ = [
        ('usri1052_profile', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1052
def _define_USER_INFO_1053_head():
    class USER_INFO_1053(Structure):
        pass
    return USER_INFO_1053
def _define_USER_INFO_1053():
    USER_INFO_1053 = win32more.NetworkManagement.NetManagement.USER_INFO_1053_head
    USER_INFO_1053._fields_ = [
        ('usri1053_home_dir_drive', win32more.Foundation.PWSTR),
    ]
    return USER_INFO_1053
def _define_USER_INFO_11_head():
    class USER_INFO_11(Structure):
        pass
    return USER_INFO_11
def _define_USER_INFO_11():
    USER_INFO_11 = win32more.NetworkManagement.NetManagement.USER_INFO_11_head
    USER_INFO_11._fields_ = [
        ('usri11_name', win32more.Foundation.PWSTR),
        ('usri11_comment', win32more.Foundation.PWSTR),
        ('usri11_usr_comment', win32more.Foundation.PWSTR),
        ('usri11_full_name', win32more.Foundation.PWSTR),
        ('usri11_priv', win32more.NetworkManagement.NetManagement.USER_PRIV),
        ('usri11_auth_flags', win32more.NetworkManagement.NetManagement.AF_OP),
        ('usri11_password_age', UInt32),
        ('usri11_home_dir', win32more.Foundation.PWSTR),
        ('usri11_parms', win32more.Foundation.PWSTR),
        ('usri11_last_logon', UInt32),
        ('usri11_last_logoff', UInt32),
        ('usri11_bad_pw_count', UInt32),
        ('usri11_num_logons', UInt32),
        ('usri11_logon_server', win32more.Foundation.PWSTR),
        ('usri11_country_code', UInt32),
        ('usri11_workstations', win32more.Foundation.PWSTR),
        ('usri11_max_storage', UInt32),
        ('usri11_units_per_week', UInt32),
        ('usri11_logon_hours', c_char_p_no),
        ('usri11_code_page', UInt32),
    ]
    return USER_INFO_11
def _define_USER_INFO_2_head():
    class USER_INFO_2(Structure):
        pass
    return USER_INFO_2
def _define_USER_INFO_2():
    USER_INFO_2 = win32more.NetworkManagement.NetManagement.USER_INFO_2_head
    USER_INFO_2._fields_ = [
        ('usri2_name', win32more.Foundation.PWSTR),
        ('usri2_password', win32more.Foundation.PWSTR),
        ('usri2_password_age', UInt32),
        ('usri2_priv', win32more.NetworkManagement.NetManagement.USER_PRIV),
        ('usri2_home_dir', win32more.Foundation.PWSTR),
        ('usri2_comment', win32more.Foundation.PWSTR),
        ('usri2_flags', win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS),
        ('usri2_script_path', win32more.Foundation.PWSTR),
        ('usri2_auth_flags', win32more.NetworkManagement.NetManagement.AF_OP),
        ('usri2_full_name', win32more.Foundation.PWSTR),
        ('usri2_usr_comment', win32more.Foundation.PWSTR),
        ('usri2_parms', win32more.Foundation.PWSTR),
        ('usri2_workstations', win32more.Foundation.PWSTR),
        ('usri2_last_logon', UInt32),
        ('usri2_last_logoff', UInt32),
        ('usri2_acct_expires', UInt32),
        ('usri2_max_storage', UInt32),
        ('usri2_units_per_week', UInt32),
        ('usri2_logon_hours', c_char_p_no),
        ('usri2_bad_pw_count', UInt32),
        ('usri2_num_logons', UInt32),
        ('usri2_logon_server', win32more.Foundation.PWSTR),
        ('usri2_country_code', UInt32),
        ('usri2_code_page', UInt32),
    ]
    return USER_INFO_2
def _define_USER_INFO_20_head():
    class USER_INFO_20(Structure):
        pass
    return USER_INFO_20
def _define_USER_INFO_20():
    USER_INFO_20 = win32more.NetworkManagement.NetManagement.USER_INFO_20_head
    USER_INFO_20._fields_ = [
        ('usri20_name', win32more.Foundation.PWSTR),
        ('usri20_full_name', win32more.Foundation.PWSTR),
        ('usri20_comment', win32more.Foundation.PWSTR),
        ('usri20_flags', win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS),
        ('usri20_user_id', UInt32),
    ]
    return USER_INFO_20
def _define_USER_INFO_21_head():
    class USER_INFO_21(Structure):
        pass
    return USER_INFO_21
def _define_USER_INFO_21():
    USER_INFO_21 = win32more.NetworkManagement.NetManagement.USER_INFO_21_head
    USER_INFO_21._fields_ = [
        ('usri21_password', Byte * 16),
    ]
    return USER_INFO_21
def _define_USER_INFO_22_head():
    class USER_INFO_22(Structure):
        pass
    return USER_INFO_22
def _define_USER_INFO_22():
    USER_INFO_22 = win32more.NetworkManagement.NetManagement.USER_INFO_22_head
    USER_INFO_22._fields_ = [
        ('usri22_name', win32more.Foundation.PWSTR),
        ('usri22_password', Byte * 16),
        ('usri22_password_age', UInt32),
        ('usri22_priv', win32more.NetworkManagement.NetManagement.USER_PRIV),
        ('usri22_home_dir', win32more.Foundation.PWSTR),
        ('usri22_comment', win32more.Foundation.PWSTR),
        ('usri22_flags', win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS),
        ('usri22_script_path', win32more.Foundation.PWSTR),
        ('usri22_auth_flags', win32more.NetworkManagement.NetManagement.AF_OP),
        ('usri22_full_name', win32more.Foundation.PWSTR),
        ('usri22_usr_comment', win32more.Foundation.PWSTR),
        ('usri22_parms', win32more.Foundation.PWSTR),
        ('usri22_workstations', win32more.Foundation.PWSTR),
        ('usri22_last_logon', UInt32),
        ('usri22_last_logoff', UInt32),
        ('usri22_acct_expires', UInt32),
        ('usri22_max_storage', UInt32),
        ('usri22_units_per_week', UInt32),
        ('usri22_logon_hours', c_char_p_no),
        ('usri22_bad_pw_count', UInt32),
        ('usri22_num_logons', UInt32),
        ('usri22_logon_server', win32more.Foundation.PWSTR),
        ('usri22_country_code', UInt32),
        ('usri22_code_page', UInt32),
    ]
    return USER_INFO_22
def _define_USER_INFO_23_head():
    class USER_INFO_23(Structure):
        pass
    return USER_INFO_23
def _define_USER_INFO_23():
    USER_INFO_23 = win32more.NetworkManagement.NetManagement.USER_INFO_23_head
    USER_INFO_23._fields_ = [
        ('usri23_name', win32more.Foundation.PWSTR),
        ('usri23_full_name', win32more.Foundation.PWSTR),
        ('usri23_comment', win32more.Foundation.PWSTR),
        ('usri23_flags', win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS),
        ('usri23_user_sid', win32more.Foundation.PSID),
    ]
    return USER_INFO_23
def _define_USER_INFO_24_head():
    class USER_INFO_24(Structure):
        pass
    return USER_INFO_24
def _define_USER_INFO_24():
    USER_INFO_24 = win32more.NetworkManagement.NetManagement.USER_INFO_24_head
    USER_INFO_24._fields_ = [
        ('usri24_internet_identity', win32more.Foundation.BOOL),
        ('usri24_flags', UInt32),
        ('usri24_internet_provider_name', win32more.Foundation.PWSTR),
        ('usri24_internet_principal_name', win32more.Foundation.PWSTR),
        ('usri24_user_sid', win32more.Foundation.PSID),
    ]
    return USER_INFO_24
def _define_USER_INFO_3_head():
    class USER_INFO_3(Structure):
        pass
    return USER_INFO_3
def _define_USER_INFO_3():
    USER_INFO_3 = win32more.NetworkManagement.NetManagement.USER_INFO_3_head
    USER_INFO_3._fields_ = [
        ('usri3_name', win32more.Foundation.PWSTR),
        ('usri3_password', win32more.Foundation.PWSTR),
        ('usri3_password_age', UInt32),
        ('usri3_priv', win32more.NetworkManagement.NetManagement.USER_PRIV),
        ('usri3_home_dir', win32more.Foundation.PWSTR),
        ('usri3_comment', win32more.Foundation.PWSTR),
        ('usri3_flags', win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS),
        ('usri3_script_path', win32more.Foundation.PWSTR),
        ('usri3_auth_flags', win32more.NetworkManagement.NetManagement.AF_OP),
        ('usri3_full_name', win32more.Foundation.PWSTR),
        ('usri3_usr_comment', win32more.Foundation.PWSTR),
        ('usri3_parms', win32more.Foundation.PWSTR),
        ('usri3_workstations', win32more.Foundation.PWSTR),
        ('usri3_last_logon', UInt32),
        ('usri3_last_logoff', UInt32),
        ('usri3_acct_expires', UInt32),
        ('usri3_max_storage', UInt32),
        ('usri3_units_per_week', UInt32),
        ('usri3_logon_hours', c_char_p_no),
        ('usri3_bad_pw_count', UInt32),
        ('usri3_num_logons', UInt32),
        ('usri3_logon_server', win32more.Foundation.PWSTR),
        ('usri3_country_code', UInt32),
        ('usri3_code_page', UInt32),
        ('usri3_user_id', UInt32),
        ('usri3_primary_group_id', UInt32),
        ('usri3_profile', win32more.Foundation.PWSTR),
        ('usri3_home_dir_drive', win32more.Foundation.PWSTR),
        ('usri3_password_expired', UInt32),
    ]
    return USER_INFO_3
def _define_USER_INFO_4_head():
    class USER_INFO_4(Structure):
        pass
    return USER_INFO_4
def _define_USER_INFO_4():
    USER_INFO_4 = win32more.NetworkManagement.NetManagement.USER_INFO_4_head
    USER_INFO_4._fields_ = [
        ('usri4_name', win32more.Foundation.PWSTR),
        ('usri4_password', win32more.Foundation.PWSTR),
        ('usri4_password_age', UInt32),
        ('usri4_priv', win32more.NetworkManagement.NetManagement.USER_PRIV),
        ('usri4_home_dir', win32more.Foundation.PWSTR),
        ('usri4_comment', win32more.Foundation.PWSTR),
        ('usri4_flags', win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS),
        ('usri4_script_path', win32more.Foundation.PWSTR),
        ('usri4_auth_flags', win32more.NetworkManagement.NetManagement.AF_OP),
        ('usri4_full_name', win32more.Foundation.PWSTR),
        ('usri4_usr_comment', win32more.Foundation.PWSTR),
        ('usri4_parms', win32more.Foundation.PWSTR),
        ('usri4_workstations', win32more.Foundation.PWSTR),
        ('usri4_last_logon', UInt32),
        ('usri4_last_logoff', UInt32),
        ('usri4_acct_expires', UInt32),
        ('usri4_max_storage', UInt32),
        ('usri4_units_per_week', UInt32),
        ('usri4_logon_hours', c_char_p_no),
        ('usri4_bad_pw_count', UInt32),
        ('usri4_num_logons', UInt32),
        ('usri4_logon_server', win32more.Foundation.PWSTR),
        ('usri4_country_code', UInt32),
        ('usri4_code_page', UInt32),
        ('usri4_user_sid', win32more.Foundation.PSID),
        ('usri4_primary_group_id', UInt32),
        ('usri4_profile', win32more.Foundation.PWSTR),
        ('usri4_home_dir_drive', win32more.Foundation.PWSTR),
        ('usri4_password_expired', UInt32),
    ]
    return USER_INFO_4
def _define_USER_MODALS_INFO_0_head():
    class USER_MODALS_INFO_0(Structure):
        pass
    return USER_MODALS_INFO_0
def _define_USER_MODALS_INFO_0():
    USER_MODALS_INFO_0 = win32more.NetworkManagement.NetManagement.USER_MODALS_INFO_0_head
    USER_MODALS_INFO_0._fields_ = [
        ('usrmod0_min_passwd_len', UInt32),
        ('usrmod0_max_passwd_age', UInt32),
        ('usrmod0_min_passwd_age', UInt32),
        ('usrmod0_force_logoff', UInt32),
        ('usrmod0_password_hist_len', UInt32),
    ]
    return USER_MODALS_INFO_0
def _define_USER_MODALS_INFO_1_head():
    class USER_MODALS_INFO_1(Structure):
        pass
    return USER_MODALS_INFO_1
def _define_USER_MODALS_INFO_1():
    USER_MODALS_INFO_1 = win32more.NetworkManagement.NetManagement.USER_MODALS_INFO_1_head
    USER_MODALS_INFO_1._fields_ = [
        ('usrmod1_role', UInt32),
        ('usrmod1_primary', win32more.Foundation.PWSTR),
    ]
    return USER_MODALS_INFO_1
def _define_USER_MODALS_INFO_1001_head():
    class USER_MODALS_INFO_1001(Structure):
        pass
    return USER_MODALS_INFO_1001
def _define_USER_MODALS_INFO_1001():
    USER_MODALS_INFO_1001 = win32more.NetworkManagement.NetManagement.USER_MODALS_INFO_1001_head
    USER_MODALS_INFO_1001._fields_ = [
        ('usrmod1001_min_passwd_len', UInt32),
    ]
    return USER_MODALS_INFO_1001
def _define_USER_MODALS_INFO_1002_head():
    class USER_MODALS_INFO_1002(Structure):
        pass
    return USER_MODALS_INFO_1002
def _define_USER_MODALS_INFO_1002():
    USER_MODALS_INFO_1002 = win32more.NetworkManagement.NetManagement.USER_MODALS_INFO_1002_head
    USER_MODALS_INFO_1002._fields_ = [
        ('usrmod1002_max_passwd_age', UInt32),
    ]
    return USER_MODALS_INFO_1002
def _define_USER_MODALS_INFO_1003_head():
    class USER_MODALS_INFO_1003(Structure):
        pass
    return USER_MODALS_INFO_1003
def _define_USER_MODALS_INFO_1003():
    USER_MODALS_INFO_1003 = win32more.NetworkManagement.NetManagement.USER_MODALS_INFO_1003_head
    USER_MODALS_INFO_1003._fields_ = [
        ('usrmod1003_min_passwd_age', UInt32),
    ]
    return USER_MODALS_INFO_1003
def _define_USER_MODALS_INFO_1004_head():
    class USER_MODALS_INFO_1004(Structure):
        pass
    return USER_MODALS_INFO_1004
def _define_USER_MODALS_INFO_1004():
    USER_MODALS_INFO_1004 = win32more.NetworkManagement.NetManagement.USER_MODALS_INFO_1004_head
    USER_MODALS_INFO_1004._fields_ = [
        ('usrmod1004_force_logoff', UInt32),
    ]
    return USER_MODALS_INFO_1004
def _define_USER_MODALS_INFO_1005_head():
    class USER_MODALS_INFO_1005(Structure):
        pass
    return USER_MODALS_INFO_1005
def _define_USER_MODALS_INFO_1005():
    USER_MODALS_INFO_1005 = win32more.NetworkManagement.NetManagement.USER_MODALS_INFO_1005_head
    USER_MODALS_INFO_1005._fields_ = [
        ('usrmod1005_password_hist_len', UInt32),
    ]
    return USER_MODALS_INFO_1005
def _define_USER_MODALS_INFO_1006_head():
    class USER_MODALS_INFO_1006(Structure):
        pass
    return USER_MODALS_INFO_1006
def _define_USER_MODALS_INFO_1006():
    USER_MODALS_INFO_1006 = win32more.NetworkManagement.NetManagement.USER_MODALS_INFO_1006_head
    USER_MODALS_INFO_1006._fields_ = [
        ('usrmod1006_role', win32more.NetworkManagement.NetManagement.USER_MODALS_ROLES),
    ]
    return USER_MODALS_INFO_1006
def _define_USER_MODALS_INFO_1007_head():
    class USER_MODALS_INFO_1007(Structure):
        pass
    return USER_MODALS_INFO_1007
def _define_USER_MODALS_INFO_1007():
    USER_MODALS_INFO_1007 = win32more.NetworkManagement.NetManagement.USER_MODALS_INFO_1007_head
    USER_MODALS_INFO_1007._fields_ = [
        ('usrmod1007_primary', win32more.Foundation.PWSTR),
    ]
    return USER_MODALS_INFO_1007
def _define_USER_MODALS_INFO_2_head():
    class USER_MODALS_INFO_2(Structure):
        pass
    return USER_MODALS_INFO_2
def _define_USER_MODALS_INFO_2():
    USER_MODALS_INFO_2 = win32more.NetworkManagement.NetManagement.USER_MODALS_INFO_2_head
    USER_MODALS_INFO_2._fields_ = [
        ('usrmod2_domain_name', win32more.Foundation.PWSTR),
        ('usrmod2_domain_id', win32more.Foundation.PSID),
    ]
    return USER_MODALS_INFO_2
def _define_USER_MODALS_INFO_3_head():
    class USER_MODALS_INFO_3(Structure):
        pass
    return USER_MODALS_INFO_3
def _define_USER_MODALS_INFO_3():
    USER_MODALS_INFO_3 = win32more.NetworkManagement.NetManagement.USER_MODALS_INFO_3_head
    USER_MODALS_INFO_3._fields_ = [
        ('usrmod3_lockout_duration', UInt32),
        ('usrmod3_lockout_observation_window', UInt32),
        ('usrmod3_lockout_threshold', UInt32),
    ]
    return USER_MODALS_INFO_3
USER_MODALS_ROLES = UInt32
UAS_ROLE_STANDALONE = 0
UAS_ROLE_MEMBER = 1
UAS_ROLE_BACKUP = 2
UAS_ROLE_PRIMARY = 3
def _define_USER_OTHER_INFO_head():
    class USER_OTHER_INFO(Structure):
        pass
    return USER_OTHER_INFO
def _define_USER_OTHER_INFO():
    USER_OTHER_INFO = win32more.NetworkManagement.NetManagement.USER_OTHER_INFO_head
    USER_OTHER_INFO._fields_ = [
        ('alrtus_errcode', UInt32),
        ('alrtus_numstrings', UInt32),
    ]
    return USER_OTHER_INFO
USER_PRIV = UInt32
USER_PRIV_GUEST = 0
USER_PRIV_USER = 1
USER_PRIV_ADMIN = 2
def _define_WKSTA_INFO_100_head():
    class WKSTA_INFO_100(Structure):
        pass
    return WKSTA_INFO_100
def _define_WKSTA_INFO_100():
    WKSTA_INFO_100 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_100_head
    WKSTA_INFO_100._fields_ = [
        ('wki100_platform_id', UInt32),
        ('wki100_computername', win32more.Foundation.PWSTR),
        ('wki100_langroup', win32more.Foundation.PWSTR),
        ('wki100_ver_major', UInt32),
        ('wki100_ver_minor', UInt32),
    ]
    return WKSTA_INFO_100
def _define_WKSTA_INFO_101_head():
    class WKSTA_INFO_101(Structure):
        pass
    return WKSTA_INFO_101
def _define_WKSTA_INFO_101():
    WKSTA_INFO_101 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_101_head
    WKSTA_INFO_101._fields_ = [
        ('wki101_platform_id', UInt32),
        ('wki101_computername', win32more.Foundation.PWSTR),
        ('wki101_langroup', win32more.Foundation.PWSTR),
        ('wki101_ver_major', UInt32),
        ('wki101_ver_minor', UInt32),
        ('wki101_lanroot', win32more.Foundation.PWSTR),
    ]
    return WKSTA_INFO_101
def _define_WKSTA_INFO_1010_head():
    class WKSTA_INFO_1010(Structure):
        pass
    return WKSTA_INFO_1010
def _define_WKSTA_INFO_1010():
    WKSTA_INFO_1010 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1010_head
    WKSTA_INFO_1010._fields_ = [
        ('wki1010_char_wait', UInt32),
    ]
    return WKSTA_INFO_1010
def _define_WKSTA_INFO_1011_head():
    class WKSTA_INFO_1011(Structure):
        pass
    return WKSTA_INFO_1011
def _define_WKSTA_INFO_1011():
    WKSTA_INFO_1011 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1011_head
    WKSTA_INFO_1011._fields_ = [
        ('wki1011_collection_time', UInt32),
    ]
    return WKSTA_INFO_1011
def _define_WKSTA_INFO_1012_head():
    class WKSTA_INFO_1012(Structure):
        pass
    return WKSTA_INFO_1012
def _define_WKSTA_INFO_1012():
    WKSTA_INFO_1012 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1012_head
    WKSTA_INFO_1012._fields_ = [
        ('wki1012_maximum_collection_count', UInt32),
    ]
    return WKSTA_INFO_1012
def _define_WKSTA_INFO_1013_head():
    class WKSTA_INFO_1013(Structure):
        pass
    return WKSTA_INFO_1013
def _define_WKSTA_INFO_1013():
    WKSTA_INFO_1013 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1013_head
    WKSTA_INFO_1013._fields_ = [
        ('wki1013_keep_conn', UInt32),
    ]
    return WKSTA_INFO_1013
def _define_WKSTA_INFO_1018_head():
    class WKSTA_INFO_1018(Structure):
        pass
    return WKSTA_INFO_1018
def _define_WKSTA_INFO_1018():
    WKSTA_INFO_1018 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1018_head
    WKSTA_INFO_1018._fields_ = [
        ('wki1018_sess_timeout', UInt32),
    ]
    return WKSTA_INFO_1018
def _define_WKSTA_INFO_102_head():
    class WKSTA_INFO_102(Structure):
        pass
    return WKSTA_INFO_102
def _define_WKSTA_INFO_102():
    WKSTA_INFO_102 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_102_head
    WKSTA_INFO_102._fields_ = [
        ('wki102_platform_id', UInt32),
        ('wki102_computername', win32more.Foundation.PWSTR),
        ('wki102_langroup', win32more.Foundation.PWSTR),
        ('wki102_ver_major', UInt32),
        ('wki102_ver_minor', UInt32),
        ('wki102_lanroot', win32more.Foundation.PWSTR),
        ('wki102_logged_on_users', UInt32),
    ]
    return WKSTA_INFO_102
def _define_WKSTA_INFO_1023_head():
    class WKSTA_INFO_1023(Structure):
        pass
    return WKSTA_INFO_1023
def _define_WKSTA_INFO_1023():
    WKSTA_INFO_1023 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1023_head
    WKSTA_INFO_1023._fields_ = [
        ('wki1023_siz_char_buf', UInt32),
    ]
    return WKSTA_INFO_1023
def _define_WKSTA_INFO_1027_head():
    class WKSTA_INFO_1027(Structure):
        pass
    return WKSTA_INFO_1027
def _define_WKSTA_INFO_1027():
    WKSTA_INFO_1027 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1027_head
    WKSTA_INFO_1027._fields_ = [
        ('wki1027_errlog_sz', UInt32),
    ]
    return WKSTA_INFO_1027
def _define_WKSTA_INFO_1028_head():
    class WKSTA_INFO_1028(Structure):
        pass
    return WKSTA_INFO_1028
def _define_WKSTA_INFO_1028():
    WKSTA_INFO_1028 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1028_head
    WKSTA_INFO_1028._fields_ = [
        ('wki1028_print_buf_time', UInt32),
    ]
    return WKSTA_INFO_1028
def _define_WKSTA_INFO_1032_head():
    class WKSTA_INFO_1032(Structure):
        pass
    return WKSTA_INFO_1032
def _define_WKSTA_INFO_1032():
    WKSTA_INFO_1032 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1032_head
    WKSTA_INFO_1032._fields_ = [
        ('wki1032_wrk_heuristics', UInt32),
    ]
    return WKSTA_INFO_1032
def _define_WKSTA_INFO_1033_head():
    class WKSTA_INFO_1033(Structure):
        pass
    return WKSTA_INFO_1033
def _define_WKSTA_INFO_1033():
    WKSTA_INFO_1033 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1033_head
    WKSTA_INFO_1033._fields_ = [
        ('wki1033_max_threads', UInt32),
    ]
    return WKSTA_INFO_1033
def _define_WKSTA_INFO_1041_head():
    class WKSTA_INFO_1041(Structure):
        pass
    return WKSTA_INFO_1041
def _define_WKSTA_INFO_1041():
    WKSTA_INFO_1041 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1041_head
    WKSTA_INFO_1041._fields_ = [
        ('wki1041_lock_quota', UInt32),
    ]
    return WKSTA_INFO_1041
def _define_WKSTA_INFO_1042_head():
    class WKSTA_INFO_1042(Structure):
        pass
    return WKSTA_INFO_1042
def _define_WKSTA_INFO_1042():
    WKSTA_INFO_1042 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1042_head
    WKSTA_INFO_1042._fields_ = [
        ('wki1042_lock_increment', UInt32),
    ]
    return WKSTA_INFO_1042
def _define_WKSTA_INFO_1043_head():
    class WKSTA_INFO_1043(Structure):
        pass
    return WKSTA_INFO_1043
def _define_WKSTA_INFO_1043():
    WKSTA_INFO_1043 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1043_head
    WKSTA_INFO_1043._fields_ = [
        ('wki1043_lock_maximum', UInt32),
    ]
    return WKSTA_INFO_1043
def _define_WKSTA_INFO_1044_head():
    class WKSTA_INFO_1044(Structure):
        pass
    return WKSTA_INFO_1044
def _define_WKSTA_INFO_1044():
    WKSTA_INFO_1044 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1044_head
    WKSTA_INFO_1044._fields_ = [
        ('wki1044_pipe_increment', UInt32),
    ]
    return WKSTA_INFO_1044
def _define_WKSTA_INFO_1045_head():
    class WKSTA_INFO_1045(Structure):
        pass
    return WKSTA_INFO_1045
def _define_WKSTA_INFO_1045():
    WKSTA_INFO_1045 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1045_head
    WKSTA_INFO_1045._fields_ = [
        ('wki1045_pipe_maximum', UInt32),
    ]
    return WKSTA_INFO_1045
def _define_WKSTA_INFO_1046_head():
    class WKSTA_INFO_1046(Structure):
        pass
    return WKSTA_INFO_1046
def _define_WKSTA_INFO_1046():
    WKSTA_INFO_1046 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1046_head
    WKSTA_INFO_1046._fields_ = [
        ('wki1046_dormant_file_limit', UInt32),
    ]
    return WKSTA_INFO_1046
def _define_WKSTA_INFO_1047_head():
    class WKSTA_INFO_1047(Structure):
        pass
    return WKSTA_INFO_1047
def _define_WKSTA_INFO_1047():
    WKSTA_INFO_1047 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1047_head
    WKSTA_INFO_1047._fields_ = [
        ('wki1047_cache_file_timeout', UInt32),
    ]
    return WKSTA_INFO_1047
def _define_WKSTA_INFO_1048_head():
    class WKSTA_INFO_1048(Structure):
        pass
    return WKSTA_INFO_1048
def _define_WKSTA_INFO_1048():
    WKSTA_INFO_1048 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1048_head
    WKSTA_INFO_1048._fields_ = [
        ('wki1048_use_opportunistic_locking', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1048
def _define_WKSTA_INFO_1049_head():
    class WKSTA_INFO_1049(Structure):
        pass
    return WKSTA_INFO_1049
def _define_WKSTA_INFO_1049():
    WKSTA_INFO_1049 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1049_head
    WKSTA_INFO_1049._fields_ = [
        ('wki1049_use_unlock_behind', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1049
def _define_WKSTA_INFO_1050_head():
    class WKSTA_INFO_1050(Structure):
        pass
    return WKSTA_INFO_1050
def _define_WKSTA_INFO_1050():
    WKSTA_INFO_1050 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1050_head
    WKSTA_INFO_1050._fields_ = [
        ('wki1050_use_close_behind', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1050
def _define_WKSTA_INFO_1051_head():
    class WKSTA_INFO_1051(Structure):
        pass
    return WKSTA_INFO_1051
def _define_WKSTA_INFO_1051():
    WKSTA_INFO_1051 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1051_head
    WKSTA_INFO_1051._fields_ = [
        ('wki1051_buf_named_pipes', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1051
def _define_WKSTA_INFO_1052_head():
    class WKSTA_INFO_1052(Structure):
        pass
    return WKSTA_INFO_1052
def _define_WKSTA_INFO_1052():
    WKSTA_INFO_1052 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1052_head
    WKSTA_INFO_1052._fields_ = [
        ('wki1052_use_lock_read_unlock', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1052
def _define_WKSTA_INFO_1053_head():
    class WKSTA_INFO_1053(Structure):
        pass
    return WKSTA_INFO_1053
def _define_WKSTA_INFO_1053():
    WKSTA_INFO_1053 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1053_head
    WKSTA_INFO_1053._fields_ = [
        ('wki1053_utilize_nt_caching', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1053
def _define_WKSTA_INFO_1054_head():
    class WKSTA_INFO_1054(Structure):
        pass
    return WKSTA_INFO_1054
def _define_WKSTA_INFO_1054():
    WKSTA_INFO_1054 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1054_head
    WKSTA_INFO_1054._fields_ = [
        ('wki1054_use_raw_read', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1054
def _define_WKSTA_INFO_1055_head():
    class WKSTA_INFO_1055(Structure):
        pass
    return WKSTA_INFO_1055
def _define_WKSTA_INFO_1055():
    WKSTA_INFO_1055 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1055_head
    WKSTA_INFO_1055._fields_ = [
        ('wki1055_use_raw_write', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1055
def _define_WKSTA_INFO_1056_head():
    class WKSTA_INFO_1056(Structure):
        pass
    return WKSTA_INFO_1056
def _define_WKSTA_INFO_1056():
    WKSTA_INFO_1056 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1056_head
    WKSTA_INFO_1056._fields_ = [
        ('wki1056_use_write_raw_data', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1056
def _define_WKSTA_INFO_1057_head():
    class WKSTA_INFO_1057(Structure):
        pass
    return WKSTA_INFO_1057
def _define_WKSTA_INFO_1057():
    WKSTA_INFO_1057 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1057_head
    WKSTA_INFO_1057._fields_ = [
        ('wki1057_use_encryption', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1057
def _define_WKSTA_INFO_1058_head():
    class WKSTA_INFO_1058(Structure):
        pass
    return WKSTA_INFO_1058
def _define_WKSTA_INFO_1058():
    WKSTA_INFO_1058 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1058_head
    WKSTA_INFO_1058._fields_ = [
        ('wki1058_buf_files_deny_write', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1058
def _define_WKSTA_INFO_1059_head():
    class WKSTA_INFO_1059(Structure):
        pass
    return WKSTA_INFO_1059
def _define_WKSTA_INFO_1059():
    WKSTA_INFO_1059 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1059_head
    WKSTA_INFO_1059._fields_ = [
        ('wki1059_buf_read_only_files', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1059
def _define_WKSTA_INFO_1060_head():
    class WKSTA_INFO_1060(Structure):
        pass
    return WKSTA_INFO_1060
def _define_WKSTA_INFO_1060():
    WKSTA_INFO_1060 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1060_head
    WKSTA_INFO_1060._fields_ = [
        ('wki1060_force_core_create_mode', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1060
def _define_WKSTA_INFO_1061_head():
    class WKSTA_INFO_1061(Structure):
        pass
    return WKSTA_INFO_1061
def _define_WKSTA_INFO_1061():
    WKSTA_INFO_1061 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1061_head
    WKSTA_INFO_1061._fields_ = [
        ('wki1061_use_512_byte_max_transfer', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_1061
def _define_WKSTA_INFO_1062_head():
    class WKSTA_INFO_1062(Structure):
        pass
    return WKSTA_INFO_1062
def _define_WKSTA_INFO_1062():
    WKSTA_INFO_1062 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_1062_head
    WKSTA_INFO_1062._fields_ = [
        ('wki1062_read_ahead_throughput', UInt32),
    ]
    return WKSTA_INFO_1062
def _define_WKSTA_INFO_302_head():
    class WKSTA_INFO_302(Structure):
        pass
    return WKSTA_INFO_302
def _define_WKSTA_INFO_302():
    WKSTA_INFO_302 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_302_head
    WKSTA_INFO_302._fields_ = [
        ('wki302_char_wait', UInt32),
        ('wki302_collection_time', UInt32),
        ('wki302_maximum_collection_count', UInt32),
        ('wki302_keep_conn', UInt32),
        ('wki302_keep_search', UInt32),
        ('wki302_max_cmds', UInt32),
        ('wki302_num_work_buf', UInt32),
        ('wki302_siz_work_buf', UInt32),
        ('wki302_max_wrk_cache', UInt32),
        ('wki302_sess_timeout', UInt32),
        ('wki302_siz_error', UInt32),
        ('wki302_num_alerts', UInt32),
        ('wki302_num_services', UInt32),
        ('wki302_errlog_sz', UInt32),
        ('wki302_print_buf_time', UInt32),
        ('wki302_num_char_buf', UInt32),
        ('wki302_siz_char_buf', UInt32),
        ('wki302_wrk_heuristics', win32more.Foundation.PWSTR),
        ('wki302_mailslots', UInt32),
        ('wki302_num_dgram_buf', UInt32),
    ]
    return WKSTA_INFO_302
def _define_WKSTA_INFO_402_head():
    class WKSTA_INFO_402(Structure):
        pass
    return WKSTA_INFO_402
def _define_WKSTA_INFO_402():
    WKSTA_INFO_402 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_402_head
    WKSTA_INFO_402._fields_ = [
        ('wki402_char_wait', UInt32),
        ('wki402_collection_time', UInt32),
        ('wki402_maximum_collection_count', UInt32),
        ('wki402_keep_conn', UInt32),
        ('wki402_keep_search', UInt32),
        ('wki402_max_cmds', UInt32),
        ('wki402_num_work_buf', UInt32),
        ('wki402_siz_work_buf', UInt32),
        ('wki402_max_wrk_cache', UInt32),
        ('wki402_sess_timeout', UInt32),
        ('wki402_siz_error', UInt32),
        ('wki402_num_alerts', UInt32),
        ('wki402_num_services', UInt32),
        ('wki402_errlog_sz', UInt32),
        ('wki402_print_buf_time', UInt32),
        ('wki402_num_char_buf', UInt32),
        ('wki402_siz_char_buf', UInt32),
        ('wki402_wrk_heuristics', win32more.Foundation.PWSTR),
        ('wki402_mailslots', UInt32),
        ('wki402_num_dgram_buf', UInt32),
        ('wki402_max_threads', UInt32),
    ]
    return WKSTA_INFO_402
def _define_WKSTA_INFO_502_head():
    class WKSTA_INFO_502(Structure):
        pass
    return WKSTA_INFO_502
def _define_WKSTA_INFO_502():
    WKSTA_INFO_502 = win32more.NetworkManagement.NetManagement.WKSTA_INFO_502_head
    WKSTA_INFO_502._fields_ = [
        ('wki502_char_wait', UInt32),
        ('wki502_collection_time', UInt32),
        ('wki502_maximum_collection_count', UInt32),
        ('wki502_keep_conn', UInt32),
        ('wki502_max_cmds', UInt32),
        ('wki502_sess_timeout', UInt32),
        ('wki502_siz_char_buf', UInt32),
        ('wki502_max_threads', UInt32),
        ('wki502_lock_quota', UInt32),
        ('wki502_lock_increment', UInt32),
        ('wki502_lock_maximum', UInt32),
        ('wki502_pipe_increment', UInt32),
        ('wki502_pipe_maximum', UInt32),
        ('wki502_cache_file_timeout', UInt32),
        ('wki502_dormant_file_limit', UInt32),
        ('wki502_read_ahead_throughput', UInt32),
        ('wki502_num_mailslot_buffers', UInt32),
        ('wki502_num_srv_announce_buffers', UInt32),
        ('wki502_max_illegal_datagram_events', UInt32),
        ('wki502_illegal_datagram_event_reset_frequency', UInt32),
        ('wki502_log_election_packets', win32more.Foundation.BOOL),
        ('wki502_use_opportunistic_locking', win32more.Foundation.BOOL),
        ('wki502_use_unlock_behind', win32more.Foundation.BOOL),
        ('wki502_use_close_behind', win32more.Foundation.BOOL),
        ('wki502_buf_named_pipes', win32more.Foundation.BOOL),
        ('wki502_use_lock_read_unlock', win32more.Foundation.BOOL),
        ('wki502_utilize_nt_caching', win32more.Foundation.BOOL),
        ('wki502_use_raw_read', win32more.Foundation.BOOL),
        ('wki502_use_raw_write', win32more.Foundation.BOOL),
        ('wki502_use_write_raw_data', win32more.Foundation.BOOL),
        ('wki502_use_encryption', win32more.Foundation.BOOL),
        ('wki502_buf_files_deny_write', win32more.Foundation.BOOL),
        ('wki502_buf_read_only_files', win32more.Foundation.BOOL),
        ('wki502_force_core_create_mode', win32more.Foundation.BOOL),
        ('wki502_use_512_byte_max_transfer', win32more.Foundation.BOOL),
    ]
    return WKSTA_INFO_502
def _define_WKSTA_TRANSPORT_INFO_0_head():
    class WKSTA_TRANSPORT_INFO_0(Structure):
        pass
    return WKSTA_TRANSPORT_INFO_0
def _define_WKSTA_TRANSPORT_INFO_0():
    WKSTA_TRANSPORT_INFO_0 = win32more.NetworkManagement.NetManagement.WKSTA_TRANSPORT_INFO_0_head
    WKSTA_TRANSPORT_INFO_0._fields_ = [
        ('wkti0_quality_of_service', UInt32),
        ('wkti0_number_of_vcs', UInt32),
        ('wkti0_transport_name', win32more.Foundation.PWSTR),
        ('wkti0_transport_address', win32more.Foundation.PWSTR),
        ('wkti0_wan_ish', win32more.Foundation.BOOL),
    ]
    return WKSTA_TRANSPORT_INFO_0
def _define_WKSTA_USER_INFO_0_head():
    class WKSTA_USER_INFO_0(Structure):
        pass
    return WKSTA_USER_INFO_0
def _define_WKSTA_USER_INFO_0():
    WKSTA_USER_INFO_0 = win32more.NetworkManagement.NetManagement.WKSTA_USER_INFO_0_head
    WKSTA_USER_INFO_0._fields_ = [
        ('wkui0_username', win32more.Foundation.PWSTR),
    ]
    return WKSTA_USER_INFO_0
def _define_WKSTA_USER_INFO_1_head():
    class WKSTA_USER_INFO_1(Structure):
        pass
    return WKSTA_USER_INFO_1
def _define_WKSTA_USER_INFO_1():
    WKSTA_USER_INFO_1 = win32more.NetworkManagement.NetManagement.WKSTA_USER_INFO_1_head
    WKSTA_USER_INFO_1._fields_ = [
        ('wkui1_username', win32more.Foundation.PWSTR),
        ('wkui1_logon_domain', win32more.Foundation.PWSTR),
        ('wkui1_oth_domains', win32more.Foundation.PWSTR),
        ('wkui1_logon_server', win32more.Foundation.PWSTR),
    ]
    return WKSTA_USER_INFO_1
def _define_WKSTA_USER_INFO_1101_head():
    class WKSTA_USER_INFO_1101(Structure):
        pass
    return WKSTA_USER_INFO_1101
def _define_WKSTA_USER_INFO_1101():
    WKSTA_USER_INFO_1101 = win32more.NetworkManagement.NetManagement.WKSTA_USER_INFO_1101_head
    WKSTA_USER_INFO_1101._fields_ = [
        ('wkui1101_oth_domains', win32more.Foundation.PWSTR),
    ]
    return WKSTA_USER_INFO_1101
def _define_WORKERFUNCTION():
    return WINFUNCTYPE(Void,c_void_p)
__all__ = [
    "AA_AUDIT_ALL",
    "AA_A_ACL",
    "AA_A_CREATE",
    "AA_A_DELETE",
    "AA_A_OPEN",
    "AA_A_OWNER",
    "AA_A_WRITE",
    "AA_CLOSE",
    "AA_F_ACL",
    "AA_F_CREATE",
    "AA_F_DELETE",
    "AA_F_OPEN",
    "AA_F_WRITE",
    "AA_S_ACL",
    "AA_S_CREATE",
    "AA_S_DELETE",
    "AA_S_OPEN",
    "AA_S_WRITE",
    "ACCESS_ACCESS_LIST_PARMNUM",
    "ACCESS_ATTR_PARMNUM",
    "ACCESS_AUDIT",
    "ACCESS_COUNT_PARMNUM",
    "ACCESS_FAIL_ACL",
    "ACCESS_FAIL_DELETE",
    "ACCESS_FAIL_MASK",
    "ACCESS_FAIL_OPEN",
    "ACCESS_FAIL_SHIFT",
    "ACCESS_FAIL_WRITE",
    "ACCESS_GROUP",
    "ACCESS_INFO_0",
    "ACCESS_INFO_1",
    "ACCESS_INFO_1002",
    "ACCESS_LETTERS",
    "ACCESS_LIST",
    "ACCESS_NONE",
    "ACCESS_RESOURCE_NAME_PARMNUM",
    "ACCESS_SUCCESS_ACL",
    "ACCESS_SUCCESS_DELETE",
    "ACCESS_SUCCESS_MASK",
    "ACCESS_SUCCESS_OPEN",
    "ACCESS_SUCCESS_WRITE",
    "ACTION_ADMINUNLOCK",
    "ACTION_LOCKOUT",
    "ADMIN_OTHER_INFO",
    "AE_ACCLIM",
    "AE_ACCLIMITEXCD",
    "AE_ACCRESTRICT",
    "AE_ACLMOD",
    "AE_ACLMODFAIL",
    "AE_ACLMOD_CONSTANT",
    "AE_ADD",
    "AE_ADMIN",
    "AE_ADMINDIS",
    "AE_ADMINPRIVREQD",
    "AE_ADMIN_CLOSE",
    "AE_AUTODIS",
    "AE_BADPW",
    "AE_CLOSEFILE",
    "AE_CLOSEFILE_CONSTANT",
    "AE_CONNREJ",
    "AE_CONNREJ_CONSTANT",
    "AE_CONNSTART",
    "AE_CONNSTART_CONSTANT",
    "AE_CONNSTOP",
    "AE_CONNSTOP_CONSTANT",
    "AE_DELETE",
    "AE_ERROR",
    "AE_GENERAL",
    "AE_GENERIC",
    "AE_GENERIC_TYPE",
    "AE_GUEST",
    "AE_LIM_DELETED",
    "AE_LIM_DISABLED",
    "AE_LIM_EXPIRED",
    "AE_LIM_INVAL_WKSTA",
    "AE_LIM_LOGONHOURS",
    "AE_LIM_UNKNOWN",
    "AE_LOCKOUT",
    "AE_LOCKOUT_CONSTANT",
    "AE_MOD",
    "AE_NETLOGDENIED",
    "AE_NETLOGOFF",
    "AE_NETLOGOFF_CONSTANT",
    "AE_NETLOGON",
    "AE_NETLOGON_CONSTANT",
    "AE_NOACCESSPERM",
    "AE_NORMAL",
    "AE_NORMAL_CLOSE",
    "AE_RESACCESS",
    "AE_RESACCESS2",
    "AE_RESACCESSREJ",
    "AE_RESACCESSREJ_CONSTANT",
    "AE_RESACCESS_CONSTANT",
    "AE_SERVICESTAT",
    "AE_SERVICESTAT_CONSTANT",
    "AE_SESSDIS",
    "AE_SESSLOGOFF",
    "AE_SESSLOGOFF_CONSTANT",
    "AE_SESSLOGON",
    "AE_SESSLOGON_CONSTANT",
    "AE_SESSPWERR",
    "AE_SESSPWERR_CONSTANT",
    "AE_SES_CLOSE",
    "AE_SRVCONT",
    "AE_SRVPAUSED",
    "AE_SRVSTART",
    "AE_SRVSTATUS",
    "AE_SRVSTATUS_CONSTANT",
    "AE_SRVSTOP",
    "AE_UASMOD",
    "AE_UASMOD_CONSTANT",
    "AE_UAS_GROUP",
    "AE_UAS_MODALS",
    "AE_UAS_USER",
    "AE_UNSHARE",
    "AE_USER",
    "AE_USERLIMIT",
    "AF_OP",
    "AF_OP_ACCOUNTS",
    "AF_OP_COMM",
    "AF_OP_PRINT",
    "AF_OP_SERVER",
    "ALERTER_MAILSLOT",
    "ALERTSZ",
    "ALERT_ADMIN_EVENT",
    "ALERT_ERRORLOG_EVENT",
    "ALERT_MESSAGE_EVENT",
    "ALERT_PRINT_EVENT",
    "ALERT_USER_EVENT",
    "ALIGN_SIZE",
    "ALLOCATE_RESPONSE",
    "AT_ENUM",
    "AT_INFO",
    "AUDIT_ENTRY",
    "BACKUP_MSG_FILENAME",
    "BIND_FLAGS1",
    "CLTYPE_LEN",
    "CNLEN",
    "COMPONENT_CHARACTERISTICS",
    "CONFIG_INFO_0",
    "COULD_NOT_VERIFY_VOLUMES",
    "CREATE_BYPASS_CSC",
    "CREATE_CRED_RESET",
    "CREATE_GLOBAL_MAPPING",
    "CREATE_NO_CONNECT",
    "CREATE_PERSIST_MAPPING",
    "CREATE_REQUIRE_CONNECTION_INTEGRITY",
    "CREATE_REQUIRE_CONNECTION_PRIVACY",
    "CREATE_WRITE_THROUGH_SEMANTICS",
    "CRYPT_KEY_LEN",
    "CRYPT_TXT_LEN",
    "DEFAULT_PAGES",
    "DEF_MAX_BADPW",
    "DEF_MAX_PWHIST",
    "DEF_MIN_PWLEN",
    "DEF_PWUNIQUENESS",
    "DEVLEN",
    "DFS_CONNECTION_FAILURE",
    "DFS_ERROR_ACTIVEDIRECTORY_OFFLINE",
    "DFS_ERROR_CLUSTERINFO_FAILED",
    "DFS_ERROR_COMPUTERINFO_FAILED",
    "DFS_ERROR_CREATEEVENT_FAILED",
    "DFS_ERROR_CREATE_REPARSEPOINT_FAILURE",
    "DFS_ERROR_CREATE_REPARSEPOINT_SUCCESS",
    "DFS_ERROR_CROSS_FOREST_TRUST_INFO_FAILED",
    "DFS_ERROR_DCINFO_FAILED",
    "DFS_ERROR_DSCONNECT_FAILED",
    "DFS_ERROR_DUPLICATE_LINK",
    "DFS_ERROR_HANDLENAMESPACE_FAILED",
    "DFS_ERROR_LINKS_OVERLAP",
    "DFS_ERROR_LINK_OVERLAP",
    "DFS_ERROR_MUTLIPLE_ROOTS_NOT_SUPPORTED",
    "DFS_ERROR_NO_DFS_DATA",
    "DFS_ERROR_ON_ROOT",
    "DFS_ERROR_OVERLAPPING_DIRECTORIES",
    "DFS_ERROR_PREFIXTABLE_FAILED",
    "DFS_ERROR_REFLECTIONENGINE_FAILED",
    "DFS_ERROR_REGISTERSTORE_FAILED",
    "DFS_ERROR_REMOVE_LINK_FAILED",
    "DFS_ERROR_RESYNCHRONIZE_FAILED",
    "DFS_ERROR_ROOTSYNCINIT_FAILED",
    "DFS_ERROR_SECURITYINIT_FAILED",
    "DFS_ERROR_SITECACHEINIT_FAILED",
    "DFS_ERROR_SITESUPPOR_FAILED",
    "DFS_ERROR_TARGET_LIST_INCORRECT",
    "DFS_ERROR_THREADINIT_FAILED",
    "DFS_ERROR_TOO_MANY_ERRORS",
    "DFS_ERROR_TRUSTED_DOMAIN_INFO_FAILED",
    "DFS_ERROR_UNSUPPORTED_FILESYSTEM",
    "DFS_ERROR_WINSOCKINIT_FAILED",
    "DFS_INFO_ACTIVEDIRECTORY_ONLINE",
    "DFS_INFO_CROSS_FOREST_TRUST_INFO_SUCCESS",
    "DFS_INFO_DOMAIN_REFERRAL_MIN_OVERFLOW",
    "DFS_INFO_DS_RECONNECTED",
    "DFS_INFO_FINISH_BUILDING_NAMESPACE",
    "DFS_INFO_FINISH_INIT",
    "DFS_INFO_RECONNECT_DATA",
    "DFS_INFO_TRUSTED_DOMAIN_INFO_SUCCESS",
    "DFS_INIT_SUCCESS",
    "DFS_MAX_DNR_ATTEMPTS",
    "DFS_OPEN_FAILURE",
    "DFS_REFERRAL_FAILURE",
    "DFS_REFERRAL_REQUEST",
    "DFS_REFERRAL_SUCCESS",
    "DFS_ROOT_SHARE_ACQUIRE_FAILED",
    "DFS_ROOT_SHARE_ACQUIRE_SUCCESS",
    "DFS_SPECIAL_REFERRAL_FAILURE",
    "DFS_WARN_DOMAIN_REFERRAL_OVERFLOW",
    "DFS_WARN_INCOMPLETE_MOVE",
    "DFS_WARN_METADATA_LINK_INFO_INVALID",
    "DFS_WARN_METADATA_LINK_TYPE_INCORRECT",
    "DNLEN",
    "DPP_ADVANCED",
    "DSREG_DEVICE_JOIN",
    "DSREG_JOIN_INFO",
    "DSREG_JOIN_TYPE",
    "DSREG_UNKNOWN_JOIN",
    "DSREG_USER_INFO",
    "DSREG_WORKPLACE_JOIN",
    "EBP_ABOVE",
    "EBP_BELOW",
    "ENCRYPTED_PWLEN",
    "ENUM_BINDING_PATHS_FLAGS",
    "ERRLOG2_BASE",
    "ERRLOG_BASE",
    "ERRLOG_OTHER_INFO",
    "ERROR_LOG",
    "EVENT_BAD_ACCOUNT_NAME",
    "EVENT_BAD_SERVICE_STATE",
    "EVENT_BOOT_SYSTEM_DRIVERS_FAILED",
    "EVENT_BOWSER_CANT_READ_REGISTRY",
    "EVENT_BOWSER_ELECTION_RECEIVED",
    "EVENT_BOWSER_ELECTION_SENT_FIND_MASTER_FAILED",
    "EVENT_BOWSER_ELECTION_SENT_GETBLIST_FAILED",
    "EVENT_BOWSER_GETBROWSERLIST_THRESHOLD_EXCEEDED",
    "EVENT_BOWSER_ILLEGAL_DATAGRAM",
    "EVENT_BOWSER_ILLEGAL_DATAGRAM_THRESHOLD",
    "EVENT_BOWSER_MAILSLOT_DATAGRAM_THRESHOLD_EXCEEDED",
    "EVENT_BOWSER_NAME_CONVERSION_FAILED",
    "EVENT_BOWSER_NON_MASTER_MASTER_ANNOUNCE",
    "EVENT_BOWSER_NON_PDC_WON_ELECTION",
    "EVENT_BOWSER_OLD_BACKUP_FOUND",
    "EVENT_BOWSER_OTHER_MASTER_ON_NET",
    "EVENT_BOWSER_PDC_LOST_ELECTION",
    "EVENT_BOWSER_PROMOTED_WHILE_ALREADY_MASTER",
    "EVENT_BRIDGE_ADAPTER_BIND_FAILED",
    "EVENT_BRIDGE_ADAPTER_FILTER_FAILED",
    "EVENT_BRIDGE_ADAPTER_LINK_SPEED_QUERY_FAILED",
    "EVENT_BRIDGE_ADAPTER_MAC_ADDR_QUERY_FAILED",
    "EVENT_BRIDGE_ADAPTER_NAME_QUERY_FAILED",
    "EVENT_BRIDGE_BUFFER_POOL_CREATION_FAILED",
    "EVENT_BRIDGE_DEVICE_CREATION_FAILED",
    "EVENT_BRIDGE_ETHERNET_NOT_OFFERED",
    "EVENT_BRIDGE_INIT_MALLOC_FAILED",
    "EVENT_BRIDGE_MINIPORT_INIT_FAILED",
    "EVENT_BRIDGE_MINIPORT_REGISTER_FAILED",
    "EVENT_BRIDGE_MINIPROT_DEVNAME_MISSING",
    "EVENT_BRIDGE_NO_BRIDGE_MAC_ADDR",
    "EVENT_BRIDGE_PACKET_POOL_CREATION_FAILED",
    "EVENT_BRIDGE_PROTOCOL_REGISTER_FAILED",
    "EVENT_BRIDGE_THREAD_CREATION_FAILED",
    "EVENT_BRIDGE_THREAD_REF_FAILED",
    "EVENT_BROWSER_BACKUP_STOPPED",
    "EVENT_BROWSER_DEPENDANT_SERVICE_FAILED",
    "EVENT_BROWSER_DOMAIN_LIST_FAILED",
    "EVENT_BROWSER_DOMAIN_LIST_RETRIEVED",
    "EVENT_BROWSER_ELECTION_SENT_LANMAN_NT_STARTED",
    "EVENT_BROWSER_ELECTION_SENT_LANMAN_NT_STOPPED",
    "EVENT_BROWSER_ELECTION_SENT_ROLE_CHANGED",
    "EVENT_BROWSER_GETBLIST_RECEIVED_NOT_MASTER",
    "EVENT_BROWSER_ILLEGAL_CONFIG",
    "EVENT_BROWSER_MASTER_PROMOTION_FAILED",
    "EVENT_BROWSER_MASTER_PROMOTION_FAILED_NO_MASTER",
    "EVENT_BROWSER_MASTER_PROMOTION_FAILED_STOPPING",
    "EVENT_BROWSER_NOT_STARTED_IPX_CONFIG_MISMATCH",
    "EVENT_BROWSER_OTHERDOMAIN_ADD_FAILED",
    "EVENT_BROWSER_ROLE_CHANGE_FAILED",
    "EVENT_BROWSER_SERVER_LIST_FAILED",
    "EVENT_BROWSER_SERVER_LIST_RETRIEVED",
    "EVENT_BROWSER_STATUS_BITS_UPDATE_FAILED",
    "EVENT_CALL_TO_FUNCTION_FAILED",
    "EVENT_CALL_TO_FUNCTION_FAILED_II",
    "EVENT_CIRCULAR_DEPENDENCY_AUTO",
    "EVENT_CIRCULAR_DEPENDENCY_DEMAND",
    "EVENT_COMMAND_NOT_INTERACTIVE",
    "EVENT_COMMAND_START_FAILED",
    "EVENT_CONNECTION_TIMEOUT",
    "EVENT_ComputerNameChange",
    "EVENT_DAV_REDIR_DELAYED_WRITE_FAILED",
    "EVENT_DCOM_ASSERTION_FAILURE",
    "EVENT_DCOM_COMPLUS_DISABLED",
    "EVENT_DCOM_INVALID_ENDPOINT_DATA",
    "EVENT_DEPEND_ON_LATER_GROUP",
    "EVENT_DEPEND_ON_LATER_SERVICE",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_NOTSUPP",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_NOTSUPP_PRIMARY_DN",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_OTHER",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_OTHER_PRIMARY_DN",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_REFUSED",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_REFUSED_PRIMARY_DN",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_SECURITY",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_SECURITY_PRIMARY_DN",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_SERVERFAIL",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_SERVERFAIL_PRIMARY_DN",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_TIMEOUT",
    "EVENT_DNSAPI_DEREGISTRATION_FAILED_TIMEOUT_PRIMARY_DN",
    "EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_NOTSUPP",
    "EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_OTHER",
    "EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_REFUSED",
    "EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_SECURITY",
    "EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_SERVERFAIL",
    "EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_TIMEOUT",
    "EVENT_DNSAPI_PTR_REGISTRATION_FAILED_NOTSUPP",
    "EVENT_DNSAPI_PTR_REGISTRATION_FAILED_OTHER",
    "EVENT_DNSAPI_PTR_REGISTRATION_FAILED_REFUSED",
    "EVENT_DNSAPI_PTR_REGISTRATION_FAILED_SECURITY",
    "EVENT_DNSAPI_PTR_REGISTRATION_FAILED_SERVERFAIL",
    "EVENT_DNSAPI_PTR_REGISTRATION_FAILED_TIMEOUT",
    "EVENT_DNSAPI_REGISTERED_ADAPTER",
    "EVENT_DNSAPI_REGISTERED_ADAPTER_PRIMARY_DN",
    "EVENT_DNSAPI_REGISTERED_PTR",
    "EVENT_DNSAPI_REGISTRATION_FAILED_NOTSUPP",
    "EVENT_DNSAPI_REGISTRATION_FAILED_NOTSUPP_PRIMARY_DN",
    "EVENT_DNSAPI_REGISTRATION_FAILED_OTHER",
    "EVENT_DNSAPI_REGISTRATION_FAILED_OTHER_PRIMARY_DN",
    "EVENT_DNSAPI_REGISTRATION_FAILED_REFUSED",
    "EVENT_DNSAPI_REGISTRATION_FAILED_REFUSED_PRIMARY_DN",
    "EVENT_DNSAPI_REGISTRATION_FAILED_SECURITY",
    "EVENT_DNSAPI_REGISTRATION_FAILED_SECURITY_PRIMARY_DN",
    "EVENT_DNSAPI_REGISTRATION_FAILED_SERVERFAIL",
    "EVENT_DNSAPI_REGISTRATION_FAILED_SERVERFAIL_PRIMARY_DN",
    "EVENT_DNSAPI_REGISTRATION_FAILED_TIMEOUT",
    "EVENT_DNSAPI_REGISTRATION_FAILED_TIMEOUT_PRIMARY_DN",
    "EVENT_DNSDomainNameChange",
    "EVENT_DNS_CACHE_NETWORK_PERF_WARNING",
    "EVENT_DNS_CACHE_START_FAILURE_LOW_MEMORY",
    "EVENT_DNS_CACHE_START_FAILURE_NO_CONTROL",
    "EVENT_DNS_CACHE_START_FAILURE_NO_DLL",
    "EVENT_DNS_CACHE_START_FAILURE_NO_DONE_EVENT",
    "EVENT_DNS_CACHE_START_FAILURE_NO_ENTRY",
    "EVENT_DNS_CACHE_START_FAILURE_NO_RPC",
    "EVENT_DNS_CACHE_START_FAILURE_NO_SHUTDOWN_NOTIFY",
    "EVENT_DNS_CACHE_START_FAILURE_NO_UPDATE",
    "EVENT_DNS_CACHE_UNABLE_TO_REACH_SERVER_WARNING",
    "EVENT_EQOS_ERROR_MACHINE_POLICY_KEYNAME_SIZE_ZERO",
    "EVENT_EQOS_ERROR_MACHINE_POLICY_KEYNAME_TOO_LONG",
    "EVENT_EQOS_ERROR_MACHINE_POLICY_REFERESH",
    "EVENT_EQOS_ERROR_OPENING_MACHINE_POLICY_ROOT_KEY",
    "EVENT_EQOS_ERROR_OPENING_MACHINE_POLICY_SUBKEY",
    "EVENT_EQOS_ERROR_OPENING_USER_POLICY_ROOT_KEY",
    "EVENT_EQOS_ERROR_OPENING_USER_POLICY_SUBKEY",
    "EVENT_EQOS_ERROR_PROCESSING_MACHINE_POLICY_FIELD",
    "EVENT_EQOS_ERROR_PROCESSING_USER_POLICY_FIELD",
    "EVENT_EQOS_ERROR_SETTING_APP_MARKING",
    "EVENT_EQOS_ERROR_SETTING_TCP_AUTOTUNING",
    "EVENT_EQOS_ERROR_USER_POLICY_KEYNAME_SIZE_ZERO",
    "EVENT_EQOS_ERROR_USER_POLICY_KEYNAME_TOO_LONG",
    "EVENT_EQOS_ERROR_USER_POLICY_REFERESH",
    "EVENT_EQOS_INFO_APP_MARKING_ALLOWED",
    "EVENT_EQOS_INFO_APP_MARKING_IGNORED",
    "EVENT_EQOS_INFO_APP_MARKING_NOT_CONFIGURED",
    "EVENT_EQOS_INFO_LOCAL_SETTING_DONT_USE_NLA",
    "EVENT_EQOS_INFO_MACHINE_POLICY_REFRESH_NO_CHANGE",
    "EVENT_EQOS_INFO_MACHINE_POLICY_REFRESH_WITH_CHANGE",
    "EVENT_EQOS_INFO_TCP_AUTOTUNING_HIGHLY_RESTRICTED",
    "EVENT_EQOS_INFO_TCP_AUTOTUNING_NORMAL",
    "EVENT_EQOS_INFO_TCP_AUTOTUNING_NOT_CONFIGURED",
    "EVENT_EQOS_INFO_TCP_AUTOTUNING_OFF",
    "EVENT_EQOS_INFO_TCP_AUTOTUNING_RESTRICTED",
    "EVENT_EQOS_INFO_USER_POLICY_REFRESH_NO_CHANGE",
    "EVENT_EQOS_INFO_USER_POLICY_REFRESH_WITH_CHANGE",
    "EVENT_EQOS_URL_QOS_APPLICATION_CONFLICT",
    "EVENT_EQOS_WARNING_MACHINE_POLICY_CONFLICT",
    "EVENT_EQOS_WARNING_MACHINE_POLICY_NO_FULLPATH_APPNAME",
    "EVENT_EQOS_WARNING_MACHINE_POLICY_PROFILE_NOT_SPECIFIED",
    "EVENT_EQOS_WARNING_MACHINE_POLICY_QUOTA_EXCEEDED",
    "EVENT_EQOS_WARNING_MACHINE_POLICY_VERSION",
    "EVENT_EQOS_WARNING_TEST_1",
    "EVENT_EQOS_WARNING_TEST_2",
    "EVENT_EQOS_WARNING_USER_POLICY_CONFLICT",
    "EVENT_EQOS_WARNING_USER_POLICY_NO_FULLPATH_APPNAME",
    "EVENT_EQOS_WARNING_USER_POLICY_PROFILE_NOT_SPECIFIED",
    "EVENT_EQOS_WARNING_USER_POLICY_QUOTA_EXCEEDED",
    "EVENT_EQOS_WARNING_USER_POLICY_VERSION",
    "EVENT_EventLogProductInfo",
    "EVENT_EventlogAbnormalShutdown",
    "EVENT_EventlogStarted",
    "EVENT_EventlogStopped",
    "EVENT_EventlogUptime",
    "EVENT_FIRST_LOGON_FAILED",
    "EVENT_FIRST_LOGON_FAILED_II",
    "EVENT_FRS_ACCESS_CHECKS_DISABLED",
    "EVENT_FRS_ACCESS_CHECKS_FAILED_UNKNOWN",
    "EVENT_FRS_ACCESS_CHECKS_FAILED_USER",
    "EVENT_FRS_ASSERT",
    "EVENT_FRS_BAD_REG_DATA",
    "EVENT_FRS_CANNOT_COMMUNICATE",
    "EVENT_FRS_CANNOT_CREATE_UUID",
    "EVENT_FRS_CANNOT_START_BACKUP_RESTORE_IN_PROGRESS",
    "EVENT_FRS_CANT_OPEN_PREINSTALL",
    "EVENT_FRS_CANT_OPEN_STAGE",
    "EVENT_FRS_DATABASE_SPACE",
    "EVENT_FRS_DISK_WRITE_CACHE_ENABLED",
    "EVENT_FRS_DS_POLL_ERROR_SUMMARY",
    "EVENT_FRS_DUPLICATE_IN_CXTION",
    "EVENT_FRS_DUPLICATE_IN_CXTION_SYSVOL",
    "EVENT_FRS_ERROR",
    "EVENT_FRS_ERROR_REPLICA_SET_DELETED",
    "EVENT_FRS_HUGE_FILE",
    "EVENT_FRS_IN_ERROR_STATE",
    "EVENT_FRS_JET_1414",
    "EVENT_FRS_JOIN_FAIL_TIME_SKEW",
    "EVENT_FRS_LONG_JOIN",
    "EVENT_FRS_LONG_JOIN_DONE",
    "EVENT_FRS_MOVED_PREEXISTING",
    "EVENT_FRS_NO_DNS_ATTRIBUTE",
    "EVENT_FRS_NO_SID",
    "EVENT_FRS_OVERLAPS_LOGGING",
    "EVENT_FRS_OVERLAPS_OTHER_STAGE",
    "EVENT_FRS_OVERLAPS_ROOT",
    "EVENT_FRS_OVERLAPS_STAGE",
    "EVENT_FRS_OVERLAPS_WORKING",
    "EVENT_FRS_PREPARE_ROOT_FAILED",
    "EVENT_FRS_REPLICA_IN_JRNL_WRAP_ERROR",
    "EVENT_FRS_REPLICA_NO_ROOT_CHANGE",
    "EVENT_FRS_REPLICA_SET_CREATE_FAIL",
    "EVENT_FRS_REPLICA_SET_CREATE_OK",
    "EVENT_FRS_REPLICA_SET_CXTIONS",
    "EVENT_FRS_RMTCO_TIME_SKEW",
    "EVENT_FRS_ROOT_HAS_MOVED",
    "EVENT_FRS_ROOT_NOT_VALID",
    "EVENT_FRS_STAGE_NOT_VALID",
    "EVENT_FRS_STAGING_AREA_FULL",
    "EVENT_FRS_STARTING",
    "EVENT_FRS_STOPPED",
    "EVENT_FRS_STOPPED_ASSERT",
    "EVENT_FRS_STOPPED_FORCE",
    "EVENT_FRS_STOPPING",
    "EVENT_FRS_SYSVOL_NOT_READY",
    "EVENT_FRS_SYSVOL_NOT_READY_PRIMARY",
    "EVENT_FRS_SYSVOL_READY",
    "EVENT_FRS_VOLUME_NOT_SUPPORTED",
    "EVENT_INVALID_DRIVER_DEPENDENCY",
    "EVENT_IPX_CREATE_DEVICE",
    "EVENT_IPX_ILLEGAL_CONFIG",
    "EVENT_IPX_INTERNAL_NET_INVALID",
    "EVENT_IPX_NEW_DEFAULT_TYPE",
    "EVENT_IPX_NO_ADAPTERS",
    "EVENT_IPX_NO_FRAME_TYPES",
    "EVENT_IPX_SAP_ANNOUNCE",
    "EVENT_NBT_BAD_BACKUP_WINS_ADDR",
    "EVENT_NBT_BAD_PRIMARY_WINS_ADDR",
    "EVENT_NBT_CREATE_ADDRESS",
    "EVENT_NBT_CREATE_CONNECTION",
    "EVENT_NBT_CREATE_DEVICE",
    "EVENT_NBT_CREATE_DRIVER",
    "EVENT_NBT_DUPLICATE_NAME",
    "EVENT_NBT_DUPLICATE_NAME_ERROR",
    "EVENT_NBT_NAME_RELEASE",
    "EVENT_NBT_NAME_SERVER_ADDRS",
    "EVENT_NBT_NON_OS_INIT",
    "EVENT_NBT_NO_BACKUP_WINS",
    "EVENT_NBT_NO_DEVICES",
    "EVENT_NBT_NO_RESOURCES",
    "EVENT_NBT_NO_WINS",
    "EVENT_NBT_OPEN_REG_LINKAGE",
    "EVENT_NBT_OPEN_REG_NAMESERVER",
    "EVENT_NBT_OPEN_REG_PARAMS",
    "EVENT_NBT_READ_BIND",
    "EVENT_NBT_READ_EXPORT",
    "EVENT_NBT_TIMERS",
    "EVENT_NDIS_ADAPTER_CHECK_ERROR",
    "EVENT_NDIS_ADAPTER_DISABLED",
    "EVENT_NDIS_ADAPTER_NOT_FOUND",
    "EVENT_NDIS_BAD_IO_BASE_ADDRESS",
    "EVENT_NDIS_BAD_VERSION",
    "EVENT_NDIS_CABLE_DISCONNECTED_ERROR",
    "EVENT_NDIS_DMA_CONFLICT",
    "EVENT_NDIS_DRIVER_FAILURE",
    "EVENT_NDIS_HARDWARE_FAILURE",
    "EVENT_NDIS_INTERRUPT_CONFLICT",
    "EVENT_NDIS_INTERRUPT_CONNECT",
    "EVENT_NDIS_INVALID_DOWNLOAD_FILE_ERROR",
    "EVENT_NDIS_INVALID_VALUE_FROM_ADAPTER",
    "EVENT_NDIS_IO_PORT_CONFLICT",
    "EVENT_NDIS_LOBE_FAILUE_ERROR",
    "EVENT_NDIS_MAXFRAMESIZE_ERROR",
    "EVENT_NDIS_MAXINTERNALBUFS_ERROR",
    "EVENT_NDIS_MAXMULTICAST_ERROR",
    "EVENT_NDIS_MAXRECEIVES_ERROR",
    "EVENT_NDIS_MAXTRANSMITS_ERROR",
    "EVENT_NDIS_MEMORY_CONFLICT",
    "EVENT_NDIS_MISSING_CONFIGURATION_PARAMETER",
    "EVENT_NDIS_NETWORK_ADDRESS",
    "EVENT_NDIS_OUT_OF_RESOURCE",
    "EVENT_NDIS_PORT_OR_DMA_CONFLICT",
    "EVENT_NDIS_PRODUCTID_ERROR",
    "EVENT_NDIS_RECEIVE_SPACE_SMALL",
    "EVENT_NDIS_REMOVE_RECEIVED_ERROR",
    "EVENT_NDIS_RESET_FAILURE_CORRECTION",
    "EVENT_NDIS_RESET_FAILURE_ERROR",
    "EVENT_NDIS_RESOURCE_CONFLICT",
    "EVENT_NDIS_SIGNAL_LOSS_ERROR",
    "EVENT_NDIS_TIMEOUT",
    "EVENT_NDIS_TOKEN_RING_CORRECTION",
    "EVENT_NDIS_UNSUPPORTED_CONFIGURATION",
    "EVENT_PS_ADMISSIONCONTROL_OVERFLOW",
    "EVENT_PS_BAD_BESTEFFORT_LIMIT",
    "EVENT_PS_BINDING_FAILED",
    "EVENT_PS_GPC_REGISTER_FAILED",
    "EVENT_PS_INIT_DEVICE_FAILED",
    "EVENT_PS_MISSING_ADAPTER_REGISTRY_DATA",
    "EVENT_PS_NETWORK_ADDRESS_FAIL",
    "EVENT_PS_NO_RESOURCES_FOR_INIT",
    "EVENT_PS_QUERY_OID_GEN_LINK_SPEED",
    "EVENT_PS_QUERY_OID_GEN_MAXIMUM_FRAME_SIZE",
    "EVENT_PS_QUERY_OID_GEN_MAXIMUM_TOTAL_SIZE",
    "EVENT_PS_REGISTER_ADDRESS_FAMILY_FAILED",
    "EVENT_PS_REGISTER_MINIPORT_FAILED",
    "EVENT_PS_REGISTER_PROTOCOL_FAILED",
    "EVENT_PS_RESOURCE_POOL",
    "EVENT_PS_WAN_LIMITED_BESTEFFORT",
    "EVENT_PS_WMI_INSTANCE_NAME_FAILED",
    "EVENT_RDR_AT_THREAD_MAX",
    "EVENT_RDR_CANT_BIND_TRANSPORT",
    "EVENT_RDR_CANT_BUILD_SMB_HEADER",
    "EVENT_RDR_CANT_CREATE_DEVICE",
    "EVENT_RDR_CANT_CREATE_THREAD",
    "EVENT_RDR_CANT_GET_SECURITY_CONTEXT",
    "EVENT_RDR_CANT_READ_REGISTRY",
    "EVENT_RDR_CANT_REGISTER_ADDRESS",
    "EVENT_RDR_CANT_SET_THREAD",
    "EVENT_RDR_CLOSE_BEHIND",
    "EVENT_RDR_CONNECTION",
    "EVENT_RDR_CONNECTION_REFERENCE",
    "EVENT_RDR_CONTEXTS",
    "EVENT_RDR_DELAYED_SET_ATTRIBUTES_FAILED",
    "EVENT_RDR_DELETEONCLOSE_FAILED",
    "EVENT_RDR_DISPOSITION",
    "EVENT_RDR_ENCRYPT",
    "EVENT_RDR_FAILED_UNLOCK",
    "EVENT_RDR_INVALID_LOCK_REPLY",
    "EVENT_RDR_INVALID_OPLOCK",
    "EVENT_RDR_INVALID_REPLY",
    "EVENT_RDR_INVALID_SMB",
    "EVENT_RDR_MAXCMDS",
    "EVENT_RDR_OPLOCK_SMB",
    "EVENT_RDR_PRIMARY_TRANSPORT_CONNECT_FAILED",
    "EVENT_RDR_RESOURCE_SHORTAGE",
    "EVENT_RDR_SECURITY_SIGNATURE_MISMATCH",
    "EVENT_RDR_SERVER_REFERENCE",
    "EVENT_RDR_SMB_REFERENCE",
    "EVENT_RDR_TIMEOUT",
    "EVENT_RDR_TIMEZONE_BIAS_TOO_LARGE",
    "EVENT_RDR_UNEXPECTED_ERROR",
    "EVENT_RDR_WRITE_BEHIND_FLUSH_FAILED",
    "EVENT_READFILE_TIMEOUT",
    "EVENT_REVERTED_TO_LASTKNOWNGOOD",
    "EVENT_RPCSS_ACTIVATION_ERROR",
    "EVENT_RPCSS_CREATEDEBUGGERPROCESS_FAILURE",
    "EVENT_RPCSS_CREATEPROCESS_FAILURE",
    "EVENT_RPCSS_DEFAULT_LAUNCH_ACCESS_DENIED",
    "EVENT_RPCSS_LAUNCH_ACCESS_DENIED",
    "EVENT_RPCSS_REMOTE_SIDE_ERROR",
    "EVENT_RPCSS_REMOTE_SIDE_ERROR_WITH_FILE",
    "EVENT_RPCSS_REMOTE_SIDE_UNAVAILABLE",
    "EVENT_RPCSS_RUNAS_CANT_LOGIN",
    "EVENT_RPCSS_RUNAS_CREATEPROCESS_FAILURE",
    "EVENT_RPCSS_SERVER_NOT_RESPONDING",
    "EVENT_RPCSS_SERVER_START_TIMEOUT",
    "EVENT_RPCSS_START_SERVICE_FAILURE",
    "EVENT_RPCSS_STOP_SERVICE_FAILURE",
    "EVENT_RUNNING_LASTKNOWNGOOD",
    "EVENT_SCOPE_LABEL_TOO_LONG",
    "EVENT_SCOPE_TOO_LONG",
    "EVENT_SECOND_LOGON_FAILED",
    "EVENT_SERVICE_CONFIG_BACKOUT_FAILED",
    "EVENT_SERVICE_CONTROL_SUCCESS",
    "EVENT_SERVICE_CRASH",
    "EVENT_SERVICE_CRASH_NO_ACTION",
    "EVENT_SERVICE_DIFFERENT_PID_CONNECTED",
    "EVENT_SERVICE_EXIT_FAILED",
    "EVENT_SERVICE_EXIT_FAILED_SPECIFIC",
    "EVENT_SERVICE_LOGON_TYPE_NOT_GRANTED",
    "EVENT_SERVICE_NOT_INTERACTIVE",
    "EVENT_SERVICE_RECOVERY_FAILED",
    "EVENT_SERVICE_SCESRV_FAILED",
    "EVENT_SERVICE_SHUTDOWN_FAILED",
    "EVENT_SERVICE_START_AT_BOOT_FAILED",
    "EVENT_SERVICE_START_FAILED",
    "EVENT_SERVICE_START_FAILED_GROUP",
    "EVENT_SERVICE_START_FAILED_II",
    "EVENT_SERVICE_START_FAILED_NONE",
    "EVENT_SERVICE_START_HUNG",
    "EVENT_SERVICE_START_TYPE_CHANGED",
    "EVENT_SERVICE_STATUS_SUCCESS",
    "EVENT_SERVICE_STOP_SUCCESS_WITH_REASON",
    "EVENT_SEVERE_SERVICE_FAILED",
    "EVENT_SRV_CANT_BIND_DUP_NAME",
    "EVENT_SRV_CANT_BIND_TO_TRANSPORT",
    "EVENT_SRV_CANT_CHANGE_DOMAIN_NAME",
    "EVENT_SRV_CANT_CREATE_DEVICE",
    "EVENT_SRV_CANT_CREATE_PROCESS",
    "EVENT_SRV_CANT_CREATE_THREAD",
    "EVENT_SRV_CANT_GROW_TABLE",
    "EVENT_SRV_CANT_LOAD_DRIVER",
    "EVENT_SRV_CANT_MAP_ERROR",
    "EVENT_SRV_CANT_OPEN_NPFS",
    "EVENT_SRV_CANT_RECREATE_SHARE",
    "EVENT_SRV_CANT_START_SCAVENGER",
    "EVENT_SRV_CANT_UNLOAD_DRIVER",
    "EVENT_SRV_DISK_FULL",
    "EVENT_SRV_DOS_ATTACK_DETECTED",
    "EVENT_SRV_INVALID_REGISTRY_VALUE",
    "EVENT_SRV_INVALID_REQUEST",
    "EVENT_SRV_INVALID_SD",
    "EVENT_SRV_IRP_STACK_SIZE",
    "EVENT_SRV_KEY_NOT_CREATED",
    "EVENT_SRV_KEY_NOT_FOUND",
    "EVENT_SRV_NETWORK_ERROR",
    "EVENT_SRV_NONPAGED_POOL_LIMIT",
    "EVENT_SRV_NO_BLOCKING_IO",
    "EVENT_SRV_NO_FREE_CONNECTIONS",
    "EVENT_SRV_NO_FREE_RAW_WORK_ITEM",
    "EVENT_SRV_NO_NONPAGED_POOL",
    "EVENT_SRV_NO_PAGED_POOL",
    "EVENT_SRV_NO_TRANSPORTS_BOUND",
    "EVENT_SRV_NO_VIRTUAL_MEMORY",
    "EVENT_SRV_NO_WORK_ITEM",
    "EVENT_SRV_OUT_OF_WORK_ITEM_DOS",
    "EVENT_SRV_PAGED_POOL_LIMIT",
    "EVENT_SRV_RESOURCE_SHORTAGE",
    "EVENT_SRV_SERVICE_FAILED",
    "EVENT_SRV_TOO_MANY_DOS",
    "EVENT_SRV_TXF_INIT_FAILED",
    "EVENT_SRV_UNEXPECTED_DISC",
    "EVENT_STREAMS_ALLOCB_FAILURE",
    "EVENT_STREAMS_ALLOCB_FAILURE_CNT",
    "EVENT_STREAMS_ESBALLOC_FAILURE",
    "EVENT_STREAMS_ESBALLOC_FAILURE_CNT",
    "EVENT_STREAMS_STRLOG",
    "EVENT_TAKE_OWNERSHIP",
    "EVENT_TCPIP6_STARTED",
    "EVENT_TCPIP_ADAPTER_REG_FAILURE",
    "EVENT_TCPIP_ADDRESS_CONFLICT1",
    "EVENT_TCPIP_ADDRESS_CONFLICT2",
    "EVENT_TCPIP_AUTOCONFIGURED_ADDRESS_LIMIT_REACHED",
    "EVENT_TCPIP_AUTOCONFIGURED_ROUTE_LIMIT_REACHED",
    "EVENT_TCPIP_CREATE_DEVICE_FAILED",
    "EVENT_TCPIP_DHCP_INIT_FAILED",
    "EVENT_TCPIP_INTERFACE_BIND_FAILURE",
    "EVENT_TCPIP_INVALID_ADDRESS",
    "EVENT_TCPIP_INVALID_DEFAULT_GATEWAY",
    "EVENT_TCPIP_INVALID_MASK",
    "EVENT_TCPIP_IPV4_UNINSTALLED",
    "EVENT_TCPIP_IP_INIT_FAILED",
    "EVENT_TCPIP_MEDIA_CONNECT",
    "EVENT_TCPIP_MEDIA_DISCONNECT",
    "EVENT_TCPIP_NO_ADAPTER_RESOURCES",
    "EVENT_TCPIP_NO_ADDRESS_LIST",
    "EVENT_TCPIP_NO_BINDINGS",
    "EVENT_TCPIP_NO_MASK",
    "EVENT_TCPIP_NO_MASK_LIST",
    "EVENT_TCPIP_NO_RESOURCES_FOR_INIT",
    "EVENT_TCPIP_NTE_CONTEXT_LIST_FAILURE",
    "EVENT_TCPIP_OUT_OF_ORDER_FRAGMENTS_EXCEEDED",
    "EVENT_TCPIP_PCF_CLEAR_FILTER_FAILURE",
    "EVENT_TCPIP_PCF_MISSING_CAPABILITY",
    "EVENT_TCPIP_PCF_MULTICAST_OID_ISSUE",
    "EVENT_TCPIP_PCF_NO_ARP_FILTER",
    "EVENT_TCPIP_PCF_SET_FILTER_FAILURE",
    "EVENT_TCPIP_TCP_CONNECTIONS_PERF_IMPACTED",
    "EVENT_TCPIP_TCP_CONNECT_LIMIT_REACHED",
    "EVENT_TCPIP_TCP_GLOBAL_EPHEMERAL_PORT_SPACE_EXHAUSTED",
    "EVENT_TCPIP_TCP_INIT_FAILED",
    "EVENT_TCPIP_TCP_MPP_ATTACKS_DETECTED",
    "EVENT_TCPIP_TCP_TIME_WAIT_COLLISION",
    "EVENT_TCPIP_TCP_WSD_WS_RESTRICTED",
    "EVENT_TCPIP_TOO_MANY_GATEWAYS",
    "EVENT_TCPIP_TOO_MANY_NETS",
    "EVENT_TCPIP_UDP_GLOBAL_EPHEMERAL_PORT_SPACE_EXHAUSTED",
    "EVENT_TCPIP_UDP_LIMIT_REACHED",
    "EVENT_TRANSACT_INVALID",
    "EVENT_TRANSACT_TIMEOUT",
    "EVENT_TRANSPORT_ADAPTER_NOT_FOUND",
    "EVENT_TRANSPORT_BAD_PROTOCOL",
    "EVENT_TRANSPORT_BINDING_FAILED",
    "EVENT_TRANSPORT_QUERY_OID_FAILED",
    "EVENT_TRANSPORT_REGISTER_FAILED",
    "EVENT_TRANSPORT_RESOURCE_LIMIT",
    "EVENT_TRANSPORT_RESOURCE_POOL",
    "EVENT_TRANSPORT_RESOURCE_SPECIFIC",
    "EVENT_TRANSPORT_SET_OID_FAILED",
    "EVENT_TRANSPORT_TOO_MANY_LINKS",
    "EVENT_TRANSPORT_TRANSFER_DATA",
    "EVENT_TRK_INTERNAL_ERROR",
    "EVENT_TRK_SERVICE_CORRUPT_LOG",
    "EVENT_TRK_SERVICE_DUPLICATE_VOLIDS",
    "EVENT_TRK_SERVICE_MOVE_QUOTA_EXCEEDED",
    "EVENT_TRK_SERVICE_START_FAILURE",
    "EVENT_TRK_SERVICE_START_SUCCESS",
    "EVENT_TRK_SERVICE_VOLUME_CLAIM",
    "EVENT_TRK_SERVICE_VOLUME_CREATE",
    "EVENT_TRK_SERVICE_VOL_QUOTA_EXCEEDED",
    "EVENT_UP_DRIVER_ON_MP",
    "EVENT_WEBCLIENT_CLOSE_DELETE_FAILED",
    "EVENT_WEBCLIENT_CLOSE_PROPPATCH_FAILED",
    "EVENT_WEBCLIENT_CLOSE_PUT_FAILED",
    "EVENT_WEBCLIENT_SETINFO_PROPPATCH_FAILED",
    "EVENT_WINNAT_SESSION_LIMIT_REACHED",
    "EVENT_WINSOCK_CLOSESOCKET_STUCK",
    "EVENT_WINSOCK_TDI_FILTER_DETECTED",
    "EVENT_WSK_OWNINGTHREAD_PARAMETER_IGNORED",
    "EVLEN",
    "EXTRA_EXIT_POINT",
    "EXTRA_EXIT_POINT_DELETED",
    "EXTRA_EXIT_POINT_NOT_DELETED",
    "EXTRA_VOLUME",
    "EXTRA_VOLUME_DELETED",
    "EXTRA_VOLUME_NOT_DELETED",
    "FILTER_INTERDOMAIN_TRUST_ACCOUNT",
    "FILTER_NORMAL_ACCOUNT",
    "FILTER_SERVER_TRUST_ACCOUNT",
    "FILTER_TEMP_DUPLICATE_ACCOUNT",
    "FILTER_WORKSTATION_TRUST_ACCOUNT",
    "FLAT_STRING",
    "FORCE_LEVEL_FLAGS",
    "GNLEN",
    "GROUPIDMASK",
    "GROUP_ALL_PARMNUM",
    "GROUP_ATTRIBUTES_PARMNUM",
    "GROUP_COMMENT_PARMNUM",
    "GROUP_INFO_0",
    "GROUP_INFO_1",
    "GROUP_INFO_1002",
    "GROUP_INFO_1005",
    "GROUP_INFO_2",
    "GROUP_INFO_3",
    "GROUP_NAME_PARMNUM",
    "GROUP_SPECIALGRP_ADMINS",
    "GROUP_SPECIALGRP_GUESTS",
    "GROUP_SPECIALGRP_LOCAL",
    "GROUP_SPECIALGRP_USERS",
    "GROUP_USERS_INFO_0",
    "GROUP_USERS_INFO_1",
    "GetNetScheduleAccountInformation",
    "HARDWARE_ADDRESS",
    "HARDWARE_ADDRESS_LENGTH",
    "HELP_MSG_FILENAME",
    "HLOG",
    "IEnumNetCfgBindingInterface",
    "IEnumNetCfgBindingPath",
    "IEnumNetCfgComponent",
    "INTERFACE_INFO_REVISION_1",
    "INVALID_TRACEID",
    "INetCfg",
    "INetCfgBindingInterface",
    "INetCfgBindingPath",
    "INetCfgClass",
    "INetCfgClassSetup",
    "INetCfgClassSetup2",
    "INetCfgComponent",
    "INetCfgComponentBindings",
    "INetCfgComponentControl",
    "INetCfgComponentNotifyBinding",
    "INetCfgComponentNotifyGlobal",
    "INetCfgComponentPropertyUi",
    "INetCfgComponentSetup",
    "INetCfgComponentSysPrep",
    "INetCfgComponentUpperEdge",
    "INetCfgLock",
    "INetCfgPnpReconfigCallback",
    "INetCfgSysPrep",
    "INetLanConnectionUiInfo",
    "INetRasConnectionIpUiInfo",
    "IPX_PROTOCOL_BASE",
    "IPX_PROTOCOL_RIP",
    "IProvisioningDomain",
    "IProvisioningProfileWireless",
    "IR_PROMISCUOUS",
    "IR_PROMISCUOUS_MULTICAST",
    "I_NetLogonControl2",
    "JOB_ADD_CURRENT_DATE",
    "JOB_EXEC_ERROR",
    "JOB_NONINTERACTIVE",
    "JOB_RUNS_TODAY",
    "JOB_RUN_PERIODICALLY",
    "KNOWLEDGE_INCONSISTENCY_DETECTED",
    "LG_INCLUDE_INDIRECT",
    "LM20_CNLEN",
    "LM20_DEVLEN",
    "LM20_DNLEN",
    "LM20_GNLEN",
    "LM20_MAXCOMMENTSZ",
    "LM20_NNLEN",
    "LM20_PATHLEN",
    "LM20_PWLEN",
    "LM20_QNLEN",
    "LM20_SERVICE_ACTIVE",
    "LM20_SERVICE_CONTINUE_PENDING",
    "LM20_SERVICE_PAUSED",
    "LM20_SERVICE_PAUSE_PENDING",
    "LM20_SNLEN",
    "LM20_STXTLEN",
    "LM20_UNCLEN",
    "LM20_UNLEN",
    "LM_REDIR_FAILURE",
    "LOCALGROUP_COMMENT_PARMNUM",
    "LOCALGROUP_INFO_0",
    "LOCALGROUP_INFO_1",
    "LOCALGROUP_INFO_1002",
    "LOCALGROUP_MEMBERS_INFO_0",
    "LOCALGROUP_MEMBERS_INFO_1",
    "LOCALGROUP_MEMBERS_INFO_2",
    "LOCALGROUP_MEMBERS_INFO_3",
    "LOCALGROUP_NAME_PARMNUM",
    "LOCALGROUP_USERS_INFO_0",
    "LOGFLAGS_BACKWARD",
    "LOGFLAGS_FORWARD",
    "LOGFLAGS_SEEK",
    "LOWER_GET_HINT_MASK",
    "LOWER_HINT_MASK",
    "LogErrorA",
    "LogErrorW",
    "LogEventA",
    "LogEventW",
    "MACHINE_UNJOINED",
    "MAJOR_VERSION_MASK",
    "MAXCOMMENTSZ",
    "MAXPERMENTRIES",
    "MAX_LANMAN_MESSAGE_ID",
    "MAX_NERR",
    "MAX_PASSWD_LEN",
    "MAX_PREFERRED_LENGTH",
    "MAX_PROTOCOL_DLL_LEN",
    "MAX_PROTOCOL_NAME_LEN",
    "MESSAGE_FILENAME",
    "MFE_BOUNDARY_REACHED",
    "MFE_IIF",
    "MFE_NOT_FORWARDING",
    "MFE_NOT_LAST_HOP",
    "MFE_NO_ERROR",
    "MFE_NO_MULTICAST",
    "MFE_NO_ROUTE",
    "MFE_NO_SPACE",
    "MFE_OIF_PRUNED",
    "MFE_OLD_ROUTER",
    "MFE_PROHIBITED",
    "MFE_PRUNED_UPSTREAM",
    "MFE_REACHED_CORE",
    "MFE_WRONG_IF",
    "MIN_LANMAN_MESSAGE_ID",
    "MISSING_EXIT_POINT",
    "MISSING_EXIT_POINT_CREATED",
    "MISSING_EXIT_POINT_NOT_CREATED",
    "MISSING_VOLUME",
    "MISSING_VOLUME_CREATED",
    "MISSING_VOLUME_NOT_CREATED",
    "MODALS_DOMAIN_ID_PARMNUM",
    "MODALS_DOMAIN_NAME_PARMNUM",
    "MODALS_FORCE_LOGOFF_PARMNUM",
    "MODALS_LOCKOUT_DURATION_PARMNUM",
    "MODALS_LOCKOUT_OBSERVATION_WINDOW_PARMNUM",
    "MODALS_LOCKOUT_THRESHOLD_PARMNUM",
    "MODALS_MAX_PASSWD_AGE_PARMNUM",
    "MODALS_MIN_PASSWD_AGE_PARMNUM",
    "MODALS_MIN_PASSWD_LEN_PARMNUM",
    "MODALS_PASSWD_HIST_LEN_PARMNUM",
    "MODALS_PRIMARY_PARMNUM",
    "MODALS_ROLE_PARMNUM",
    "MPR_PROTOCOL_0",
    "MRINFO_DISABLED_FLAG",
    "MRINFO_DOWN_FLAG",
    "MRINFO_LEAF_FLAG",
    "MRINFO_PIM_FLAG",
    "MRINFO_QUERIER_FLAG",
    "MRINFO_TUNNEL_FLAG",
    "MSA_INFO_0",
    "MSA_INFO_LEVEL",
    "MSA_INFO_LEVEL_MsaInfoLevel0",
    "MSA_INFO_LEVEL_MsaInfoLevelMax",
    "MSA_INFO_STATE",
    "MSA_INFO_STATE_MsaInfoCanInstall",
    "MSA_INFO_STATE_MsaInfoCannotInstall",
    "MSA_INFO_STATE_MsaInfoInstalled",
    "MSA_INFO_STATE_MsaInfoNotExist",
    "MSA_INFO_STATE_MsaInfoNotService",
    "MSGNAME_FORWARDED_FROM",
    "MSGNAME_FORWARDED_TO",
    "MSGNAME_NOT_FORWARDED",
    "MSG_INFO_0",
    "MSG_INFO_1",
    "MS_ROUTER_VERSION",
    "MprSetupProtocolEnum",
    "MprSetupProtocolFree",
    "NCF_DONTEXPOSELOWER",
    "NCF_FILTER",
    "NCF_FIXED_BINDING",
    "NCF_HAS_UI",
    "NCF_HIDDEN",
    "NCF_HIDE_BINDING",
    "NCF_LOWER",
    "NCF_LW_FILTER",
    "NCF_MULTIPORT_INSTANCED_ADAPTER",
    "NCF_NDIS_PROTOCOL",
    "NCF_NOT_USER_REMOVABLE",
    "NCF_NO_SERVICE",
    "NCF_PHYSICAL",
    "NCF_SINGLE_INSTANCE",
    "NCF_SOFTWARE_ENUMERATED",
    "NCF_UPPER",
    "NCF_VIRTUAL",
    "NCN_ADD",
    "NCN_BINDING_PATH",
    "NCN_DISABLE",
    "NCN_ENABLE",
    "NCN_NET",
    "NCN_NETCLIENT",
    "NCN_NETSERVICE",
    "NCN_NETTRANS",
    "NCN_PROPERTYCHANGE",
    "NCN_REMOVE",
    "NCN_UPDATE",
    "NCPNP_RECONFIG_LAYER",
    "NCRL_NDIS",
    "NCRL_TDI",
    "NCRP_FLAGS",
    "NCRP_QUERY_PROPERTY_UI",
    "NCRP_SHOW_PROPERTY_UI",
    "NELOG_AT_Exec_Err",
    "NELOG_AT_cannot_read",
    "NELOG_AT_cannot_write",
    "NELOG_AT_sched_err",
    "NELOG_AT_schedule_file_created",
    "NELOG_Access_File_Bad",
    "NELOG_Build_Name",
    "NELOG_Cant_Make_Msg_File",
    "NELOG_DiskFT",
    "NELOG_DriverNotLoaded",
    "NELOG_Entries_Lost",
    "NELOG_Error_in_DLL",
    "NELOG_Exec_Netservr_NoMem",
    "NELOG_FT_ErrLog_Too_Large",
    "NELOG_FT_Update_In_Progress",
    "NELOG_FailedToGetComputerName",
    "NELOG_FailedToRegisterSC",
    "NELOG_FailedToSetServiceStatus",
    "NELOG_File_Changed",
    "NELOG_Files_Dont_Fit",
    "NELOG_HardErr_From_Server",
    "NELOG_HotFix",
    "NELOG_Init_Chardev_Err",
    "NELOG_Init_Exec_Fail",
    "NELOG_Init_OpenCreate_Err",
    "NELOG_Init_Seg_Overflow",
    "NELOG_Internal_Error",
    "NELOG_Invalid_Config_File",
    "NELOG_Invalid_Config_Line",
    "NELOG_Ioctl_Error",
    "NELOG_Joined_Domain",
    "NELOG_Joined_Workgroup",
    "NELOG_Lazy_Write_Err",
    "NELOG_LocalSecFail1",
    "NELOG_LocalSecFail2",
    "NELOG_LocalSecFail3",
    "NELOG_LocalSecGeneralFail",
    "NELOG_Mail_Slt_Err",
    "NELOG_Mailslot_err",
    "NELOG_Message_Send",
    "NELOG_Missing_Parameter",
    "NELOG_Msg_Log_Err",
    "NELOG_Msg_Sem_Shutdown",
    "NELOG_Msg_Shutdown",
    "NELOG_Msg_Unexpected_SMB_Type",
    "NELOG_Name_Expansion",
    "NELOG_Ncb_Error",
    "NELOG_Ncb_TooManyErr",
    "NELOG_NetBios",
    "NELOG_NetLogonFailedToInitializeAuthzRm",
    "NELOG_NetLogonFailedToInitializeRPCSD",
    "NELOG_NetWkSta_Internal_Error",
    "NELOG_NetWkSta_NCB_Err",
    "NELOG_NetWkSta_No_Resource",
    "NELOG_NetWkSta_Reset_Err",
    "NELOG_NetWkSta_SMB_Err",
    "NELOG_NetWkSta_Stuck_VC_Err",
    "NELOG_NetWkSta_Too_Many",
    "NELOG_NetWkSta_VC_Err",
    "NELOG_NetWkSta_Write_Behind_Err",
    "NELOG_Net_Not_Started",
    "NELOG_NetlogonAddNameFailure",
    "NELOG_NetlogonAuthDCFail",
    "NELOG_NetlogonAuthDomainDowngraded",
    "NELOG_NetlogonAuthNoDomainController",
    "NELOG_NetlogonAuthNoTrustLsaSecret",
    "NELOG_NetlogonAuthNoTrustSamAccount",
    "NELOG_NetlogonAuthNoUplevelDomainController",
    "NELOG_NetlogonBadSiteName",
    "NELOG_NetlogonBadSubnetName",
    "NELOG_NetlogonBrowserDriver",
    "NELOG_NetlogonChangeLogCorrupt",
    "NELOG_NetlogonDcOldSiteCovered",
    "NELOG_NetlogonDcSiteCovered",
    "NELOG_NetlogonDcSiteNotCovered",
    "NELOG_NetlogonDcSiteNotCoveredAuto",
    "NELOG_NetlogonDnsDeregAborted",
    "NELOG_NetlogonDnsHostNameLowerCasingFailed",
    "NELOG_NetlogonDownLevelLogoffFailed",
    "NELOG_NetlogonDownLevelLogonFailed",
    "NELOG_NetlogonDuplicateMachineAccounts",
    "NELOG_NetlogonDynamicDnsDeregisterFailure",
    "NELOG_NetlogonDynamicDnsFailure",
    "NELOG_NetlogonDynamicDnsRegisterFailure",
    "NELOG_NetlogonDynamicDnsServerFailure",
    "NELOG_NetlogonFailedAccountDelta",
    "NELOG_NetlogonFailedDnsHostNameUpdate",
    "NELOG_NetlogonFailedDomainDelta",
    "NELOG_NetlogonFailedFileCreate",
    "NELOG_NetlogonFailedGlobalGroupDelta",
    "NELOG_NetlogonFailedLocalGroupDelta",
    "NELOG_NetlogonFailedPolicyDelta",
    "NELOG_NetlogonFailedPrimary",
    "NELOG_NetlogonFailedSecretDelta",
    "NELOG_NetlogonFailedSpnUpdate",
    "NELOG_NetlogonFailedToAddAuthzRpcInterface",
    "NELOG_NetlogonFailedToAddRpcInterface",
    "NELOG_NetlogonFailedToCreateShare",
    "NELOG_NetlogonFailedToReadMailslot",
    "NELOG_NetlogonFailedToRegisterSC",
    "NELOG_NetlogonFailedToUpdateTrustList",
    "NELOG_NetlogonFailedTrustedDomainDelta",
    "NELOG_NetlogonFailedUserDelta",
    "NELOG_NetlogonFullSyncCallFailed",
    "NELOG_NetlogonFullSyncCallSuccess",
    "NELOG_NetlogonFullSyncFailed",
    "NELOG_NetlogonFullSyncSuccess",
    "NELOG_NetlogonGcOldSiteCovered",
    "NELOG_NetlogonGcSiteCovered",
    "NELOG_NetlogonGcSiteNotCovered",
    "NELOG_NetlogonGcSiteNotCoveredAuto",
    "NELOG_NetlogonGetSubnetToSite",
    "NELOG_NetlogonInvalidDwordParameterValue",
    "NELOG_NetlogonInvalidGenericParameterValue",
    "NELOG_NetlogonLanmanBdcsNotAllowed",
    "NELOG_NetlogonMachinePasswdSetSucceeded",
    "NELOG_NetlogonMsaPasswdSetSucceeded",
    "NELOG_NetlogonNTLogoffFailed",
    "NELOG_NetlogonNTLogonFailed",
    "NELOG_NetlogonNdncOldSiteCovered",
    "NELOG_NetlogonNdncSiteCovered",
    "NELOG_NetlogonNdncSiteNotCovered",
    "NELOG_NetlogonNdncSiteNotCoveredAuto",
    "NELOG_NetlogonNoAddressToSiteMapping",
    "NELOG_NetlogonNoDynamicDns",
    "NELOG_NetlogonNoDynamicDnsManual",
    "NELOG_NetlogonNoSiteForClient",
    "NELOG_NetlogonNoSiteForClients",
    "NELOG_NetlogonPartialSiteMappingForClients",
    "NELOG_NetlogonPartialSyncCallFailed",
    "NELOG_NetlogonPartialSyncCallSuccess",
    "NELOG_NetlogonPartialSyncFailed",
    "NELOG_NetlogonPartialSyncSuccess",
    "NELOG_NetlogonPasswdSetFailed",
    "NELOG_NetlogonRejectedRemoteDynamicDnsDeregister",
    "NELOG_NetlogonRejectedRemoteDynamicDnsRegister",
    "NELOG_NetlogonRemoteDynamicDnsDeregisterFailure",
    "NELOG_NetlogonRemoteDynamicDnsRegisterFailure",
    "NELOG_NetlogonRemoteDynamicDnsUpdateRequestFailure",
    "NELOG_NetlogonRequireSignOrSealError",
    "NELOG_NetlogonRpcCallCancelled",
    "NELOG_NetlogonRpcPortRequestFailure",
    "NELOG_NetlogonSSIInitError",
    "NELOG_NetlogonServerAuthFailed",
    "NELOG_NetlogonServerAuthFailedNoAccount",
    "NELOG_NetlogonServerAuthNoTrustSamAccount",
    "NELOG_NetlogonSessionTypeWrong",
    "NELOG_NetlogonSpnCrackNamesFailure",
    "NELOG_NetlogonSpnMultipleSamAccountNames",
    "NELOG_NetlogonSyncError",
    "NELOG_NetlogonSystemError",
    "NELOG_NetlogonTooManyGlobalGroups",
    "NELOG_NetlogonTrackingError",
    "NELOG_NetlogonUserValidationReqInitialTimeOut",
    "NELOG_NetlogonUserValidationReqRecurringTimeOut",
    "NELOG_NetlogonUserValidationReqWaitInitialWarning",
    "NELOG_NetlogonUserValidationReqWaitRecurringWarning",
    "NELOG_NoTranportLoaded",
    "NELOG_OEM_Code",
    "NELOG_ReleaseMem_Alert",
    "NELOG_Remote_API",
    "NELOG_ReplAccessDenied",
    "NELOG_ReplBadExport",
    "NELOG_ReplBadImport",
    "NELOG_ReplBadMsg",
    "NELOG_ReplCannotMasterDir",
    "NELOG_ReplLogonFailed",
    "NELOG_ReplLostMaster",
    "NELOG_ReplMaxFiles",
    "NELOG_ReplMaxTreeDepth",
    "NELOG_ReplNetErr",
    "NELOG_ReplSignalFileErr",
    "NELOG_ReplSysErr",
    "NELOG_ReplUpdateError",
    "NELOG_ReplUserCurDir",
    "NELOG_ReplUserLoged",
    "NELOG_Resource_Shortage",
    "NELOG_RplAdapterResource",
    "NELOG_RplBackupDatabase",
    "NELOG_RplCheckConfigs",
    "NELOG_RplCheckSecurity",
    "NELOG_RplCreateProfiles",
    "NELOG_RplFileCopy",
    "NELOG_RplFileDelete",
    "NELOG_RplFilePerms",
    "NELOG_RplInitDatabase",
    "NELOG_RplInitRestoredDatabase",
    "NELOG_RplMessages",
    "NELOG_RplRegistry",
    "NELOG_RplReplaceRPLDISK",
    "NELOG_RplRestoreDatabaseFailure",
    "NELOG_RplRestoreDatabaseSuccess",
    "NELOG_RplSystem",
    "NELOG_RplUpgradeDBTo40",
    "NELOG_RplWkstaBbcFile",
    "NELOG_RplWkstaFileChecksum",
    "NELOG_RplWkstaFileLineCount",
    "NELOG_RplWkstaFileOpen",
    "NELOG_RplWkstaFileRead",
    "NELOG_RplWkstaFileSize",
    "NELOG_RplWkstaInternal",
    "NELOG_RplWkstaMemory",
    "NELOG_RplWkstaNetwork",
    "NELOG_RplWkstaTimeout",
    "NELOG_RplWkstaWrongVersion",
    "NELOG_RplXnsBoot",
    "NELOG_SMB_Illegal",
    "NELOG_Server_Lock_Failure",
    "NELOG_Service_Fail",
    "NELOG_Srv_Close_Failure",
    "NELOG_Srv_No_Mem_Grow",
    "NELOG_Srv_Thread_Failure",
    "NELOG_Srvnet_NB_Open",
    "NELOG_Srvnet_Not_Started",
    "NELOG_System_Error",
    "NELOG_System_Semaphore",
    "NELOG_UPS_CannotOpenDriver",
    "NELOG_UPS_CmdFileConfig",
    "NELOG_UPS_CmdFileError",
    "NELOG_UPS_CmdFileExec",
    "NELOG_UPS_PowerBack",
    "NELOG_UPS_PowerOut",
    "NELOG_UPS_Shutdown",
    "NELOG_Unable_To_Lock_Segment",
    "NELOG_Unable_To_Unlock_Segment",
    "NELOG_Uninstall_Service",
    "NELOG_VIO_POPUP_ERR",
    "NELOG_Wksta_Bad_Mailslot_SMB",
    "NELOG_Wksta_BiosThreadFailure",
    "NELOG_Wksta_Compname",
    "NELOG_Wksta_HostTab_Full",
    "NELOG_Wksta_Infoseg",
    "NELOG_Wksta_IniSeg",
    "NELOG_Wksta_SSIRelogon",
    "NELOG_Wksta_UASInit",
    "NELOG_Wrong_DLL_Version",
    "NERR_ACFFileIOFail",
    "NERR_ACFNoParent",
    "NERR_ACFNoRoom",
    "NERR_ACFNotFound",
    "NERR_ACFNotLoaded",
    "NERR_ACFTooManyLists",
    "NERR_AccountExpired",
    "NERR_AccountLockedOut",
    "NERR_AccountUndefined",
    "NERR_AcctLimitExceeded",
    "NERR_ActiveConns",
    "NERR_AddForwarded",
    "NERR_AlertExists",
    "NERR_AlreadyCloudDomainJoined",
    "NERR_AlreadyExists",
    "NERR_AlreadyForwarded",
    "NERR_AlreadyLoggedOn",
    "NERR_BASE",
    "NERR_BadAsgType",
    "NERR_BadComponent",
    "NERR_BadControlRecv",
    "NERR_BadDest",
    "NERR_BadDev",
    "NERR_BadDevString",
    "NERR_BadDomainJoinInfo",
    "NERR_BadDosFunction",
    "NERR_BadDosRetCode",
    "NERR_BadEventName",
    "NERR_BadFileCheckSum",
    "NERR_BadOfflineJoinInfo",
    "NERR_BadPassword",
    "NERR_BadPasswordCore",
    "NERR_BadQueueDevString",
    "NERR_BadQueuePriority",
    "NERR_BadReceive",
    "NERR_BadRecipient",
    "NERR_BadServiceName",
    "NERR_BadServiceProgName",
    "NERR_BadSource",
    "NERR_BadTransactConfig",
    "NERR_BadUasConfig",
    "NERR_BadUsername",
    "NERR_BrowserConfiguredToNotRun",
    "NERR_BrowserNotStarted",
    "NERR_BrowserTableIncomplete",
    "NERR_BufTooSmall",
    "NERR_CallingRplSrvr",
    "NERR_CanNotGrowSegment",
    "NERR_CanNotGrowUASFile",
    "NERR_CannotUnjoinAadDomain",
    "NERR_CantConnectRplSrvr",
    "NERR_CantCreateJoinInfo",
    "NERR_CantLoadOfflineHive",
    "NERR_CantOpenImageFile",
    "NERR_CantType",
    "NERR_CantVerifyHostname",
    "NERR_CfgCompNotFound",
    "NERR_CfgParamNotFound",
    "NERR_ClientNameNotFound",
    "NERR_CommDevInUse",
    "NERR_ComputerAccountNotFound",
    "NERR_ConnectionInsecure",
    "NERR_DCNotFound",
    "NERR_DS8DCNotFound",
    "NERR_DS8DCRequired",
    "NERR_DS9DCNotFound",
    "NERR_DataTypeInvalid",
    "NERR_DatabaseUpToDate",
    "NERR_DefaultJoinRequired",
    "NERR_DelComputerName",
    "NERR_DeleteLater",
    "NERR_DestExists",
    "NERR_DestIdle",
    "NERR_DestInvalidOp",
    "NERR_DestInvalidState",
    "NERR_DestNoRoom",
    "NERR_DestNotFound",
    "NERR_DevInUse",
    "NERR_DevInvalidOpCode",
    "NERR_DevNotFound",
    "NERR_DevNotOpen",
    "NERR_DevNotRedirected",
    "NERR_DeviceIsShared",
    "NERR_DeviceNotShared",
    "NERR_DeviceShareConflict",
    "NERR_DfsAlreadyShared",
    "NERR_DfsBadRenamePath",
    "NERR_DfsCantCreateJunctionPoint",
    "NERR_DfsCantRemoveDfsRoot",
    "NERR_DfsCantRemoveLastServerShare",
    "NERR_DfsChildOrParentInDfs",
    "NERR_DfsCyclicalName",
    "NERR_DfsDataIsIdentical",
    "NERR_DfsDuplicateService",
    "NERR_DfsInconsistent",
    "NERR_DfsInternalCorruption",
    "NERR_DfsInternalError",
    "NERR_DfsLeafVolume",
    "NERR_DfsNoSuchServer",
    "NERR_DfsNoSuchShare",
    "NERR_DfsNoSuchVolume",
    "NERR_DfsNotALeafVolume",
    "NERR_DfsNotSupportedInServerDfs",
    "NERR_DfsServerNotDfsAware",
    "NERR_DfsServerUpgraded",
    "NERR_DfsVolumeAlreadyExists",
    "NERR_DfsVolumeDataCorrupt",
    "NERR_DfsVolumeHasMultipleServers",
    "NERR_DfsVolumeIsInterDfs",
    "NERR_DfsVolumeIsOffline",
    "NERR_DifferentServers",
    "NERR_DriverNotFound",
    "NERR_DupNameReboot",
    "NERR_DuplicateName",
    "NERR_DuplicateShare",
    "NERR_ErrCommRunSrv",
    "NERR_ErrorExecingGhost",
    "NERR_ExecFailure",
    "NERR_FileIdNotFound",
    "NERR_GroupExists",
    "NERR_GroupNotFound",
    "NERR_GrpMsgProcessor",
    "NERR_ImageParamErr",
    "NERR_InUseBySpooler",
    "NERR_IncompleteDel",
    "NERR_InternalError",
    "NERR_InvalidAPI",
    "NERR_InvalidComputer",
    "NERR_InvalidDatabase",
    "NERR_InvalidDevice",
    "NERR_InvalidLana",
    "NERR_InvalidLogSeek",
    "NERR_InvalidLogonHours",
    "NERR_InvalidMachineNameForJoin",
    "NERR_InvalidMaxUsers",
    "NERR_InvalidUASOp",
    "NERR_InvalidWorkgroupName",
    "NERR_InvalidWorkstation",
    "NERR_IsDfsShare",
    "NERR_ItemNotFound",
    "NERR_JobInvalidState",
    "NERR_JobNoRoom",
    "NERR_JobNotFound",
    "NERR_JoinPerformedMustRestart",
    "NERR_LDAPCapableDCRequired",
    "NERR_LanmanIniError",
    "NERR_LastAdmin",
    "NERR_LineTooLong",
    "NERR_LocalDrive",
    "NERR_LocalForward",
    "NERR_LogFileChanged",
    "NERR_LogFileCorrupt",
    "NERR_LogOverflow",
    "NERR_LogonDomainExists",
    "NERR_LogonNoUserPath",
    "NERR_LogonScriptError",
    "NERR_LogonServerConflict",
    "NERR_LogonServerNotFound",
    "NERR_LogonTrackingError",
    "NERR_LogonsPaused",
    "NERR_MaxLenExceeded",
    "NERR_MsgAlreadyStarted",
    "NERR_MsgInitFailed",
    "NERR_MsgNotStarted",
    "NERR_MultipleNets",
    "NERR_NameInUse",
    "NERR_NameNotForwarded",
    "NERR_NameNotFound",
    "NERR_NameUsesIncompatibleCodePage",
    "NERR_NetNameNotFound",
    "NERR_NetNotStarted",
    "NERR_NetlogonNotStarted",
    "NERR_NetworkError",
    "NERR_NoAlternateServers",
    "NERR_NoCommDevs",
    "NERR_NoComputerName",
    "NERR_NoForwardName",
    "NERR_NoJoinPending",
    "NERR_NoNetworkResource",
    "NERR_NoOfflineJoinInfo",
    "NERR_NoRoom",
    "NERR_NoRplBootSystem",
    "NERR_NoSuchAlert",
    "NERR_NoSuchConnection",
    "NERR_NoSuchServer",
    "NERR_NoSuchSession",
    "NERR_NonDosFloppyUsed",
    "NERR_NonValidatedLogon",
    "NERR_NotInCache",
    "NERR_NotInDispatchTbl",
    "NERR_NotLocalDomain",
    "NERR_NotLocalName",
    "NERR_NotLoggedOn",
    "NERR_NotPrimary",
    "NERR_OpenFiles",
    "NERR_PasswordCantChange",
    "NERR_PasswordExpired",
    "NERR_PasswordFilterError",
    "NERR_PasswordHistConflict",
    "NERR_PasswordMismatch",
    "NERR_PasswordMustChange",
    "NERR_PasswordNotComplexEnough",
    "NERR_PasswordTooLong",
    "NERR_PasswordTooRecent",
    "NERR_PasswordTooShort",
    "NERR_PausedRemote",
    "NERR_PersonalSku",
    "NERR_PlainTextSecretsRequired",
    "NERR_ProcNoRespond",
    "NERR_ProcNotFound",
    "NERR_ProfileCleanup",
    "NERR_ProfileFileTooBig",
    "NERR_ProfileLoadErr",
    "NERR_ProfileOffset",
    "NERR_ProfileSaveErr",
    "NERR_ProfileUnknownCmd",
    "NERR_ProgNeedsExtraMem",
    "NERR_ProvisioningBlobUnsupported",
    "NERR_QExists",
    "NERR_QInvalidState",
    "NERR_QNoRoom",
    "NERR_QNotFound",
    "NERR_QueueNotFound",
    "NERR_RPL_CONNECTED",
    "NERR_RedirectedPath",
    "NERR_RemoteBootFailed",
    "NERR_RemoteErr",
    "NERR_RemoteFull",
    "NERR_RemoteOnly",
    "NERR_ResourceExists",
    "NERR_ResourceNotFound",
    "NERR_RplAdapterInfoCorrupted",
    "NERR_RplAdapterNameUnavailable",
    "NERR_RplAdapterNotFound",
    "NERR_RplBackupDatabase",
    "NERR_RplBadDatabase",
    "NERR_RplBadRegistry",
    "NERR_RplBootInUse",
    "NERR_RplBootInfoCorrupted",
    "NERR_RplBootNameUnavailable",
    "NERR_RplBootNotFound",
    "NERR_RplBootRestart",
    "NERR_RplBootServiceTerm",
    "NERR_RplBootStartFailed",
    "NERR_RplCannotEnum",
    "NERR_RplConfigInfoCorrupted",
    "NERR_RplConfigNameUnavailable",
    "NERR_RplConfigNotEmpty",
    "NERR_RplConfigNotFound",
    "NERR_RplIncompatibleProfile",
    "NERR_RplInternal",
    "NERR_RplLoadrDiskErr",
    "NERR_RplLoadrNetBiosErr",
    "NERR_RplNeedsRPLUSERAcct",
    "NERR_RplNoAdaptersStarted",
    "NERR_RplNotRplServer",
    "NERR_RplProfileInfoCorrupted",
    "NERR_RplProfileNameUnavailable",
    "NERR_RplProfileNotEmpty",
    "NERR_RplProfileNotFound",
    "NERR_RplRplfilesShare",
    "NERR_RplSrvrCallFailed",
    "NERR_RplVendorInfoCorrupted",
    "NERR_RplVendorNameUnavailable",
    "NERR_RplVendorNotFound",
    "NERR_RplWkstaInfoCorrupted",
    "NERR_RplWkstaNameUnavailable",
    "NERR_RplWkstaNeedsUserAcct",
    "NERR_RplWkstaNotFound",
    "NERR_RunSrvPaused",
    "NERR_SameAsComputerName",
    "NERR_ServerNotStarted",
    "NERR_ServiceCtlBusy",
    "NERR_ServiceCtlNotValid",
    "NERR_ServiceCtlTimeout",
    "NERR_ServiceEntryLocked",
    "NERR_ServiceInstalled",
    "NERR_ServiceKillProc",
    "NERR_ServiceNotCtrl",
    "NERR_ServiceNotInstalled",
    "NERR_ServiceNotStarting",
    "NERR_ServiceTableFull",
    "NERR_ServiceTableLocked",
    "NERR_SetupAlreadyJoined",
    "NERR_SetupCheckDNSConfig",
    "NERR_SetupDomainController",
    "NERR_SetupNotJoined",
    "NERR_ShareMem",
    "NERR_ShareNotFound",
    "NERR_SourceIsDir",
    "NERR_SpeGroupOp",
    "NERR_SpoolNoMemory",
    "NERR_SpoolerNotLoaded",
    "NERR_StandaloneLogon",
    "NERR_StartingRplBoot",
    "NERR_Success",
    "NERR_SyncRequired",
    "NERR_TargetVersionUnsupported",
    "NERR_TimeDiffAtDC",
    "NERR_TmpFile",
    "NERR_TooManyAlerts",
    "NERR_TooManyConnections",
    "NERR_TooManyEntries",
    "NERR_TooManyFiles",
    "NERR_TooManyImageParams",
    "NERR_TooManyItems",
    "NERR_TooManyNames",
    "NERR_TooManyServers",
    "NERR_TooManySessions",
    "NERR_TooMuchData",
    "NERR_TruncatedBroadcast",
    "NERR_TryDownLevel",
    "NERR_UPSDriverNotStarted",
    "NERR_UPSInvalidCommPort",
    "NERR_UPSInvalidConfig",
    "NERR_UPSShutdownFailed",
    "NERR_UPSSignalAsserted",
    "NERR_UnableToAddName_F",
    "NERR_UnableToAddName_W",
    "NERR_UnableToDelName_F",
    "NERR_UnableToDelName_W",
    "NERR_UnknownDevDir",
    "NERR_UnknownServer",
    "NERR_UseNotFound",
    "NERR_UserExists",
    "NERR_UserInGroup",
    "NERR_UserLogon",
    "NERR_UserNotFound",
    "NERR_UserNotInGroup",
    "NERR_ValuesNotSet",
    "NERR_WkstaInconsistentState",
    "NERR_WkstaNotStarted",
    "NERR_WriteFault",
    "NETBIOS_NAME_LEN",
    "NETCFG_CLIENT_CID_MS_MSClient",
    "NETCFG_E_ACTIVE_RAS_CONNECTIONS",
    "NETCFG_E_ADAPTER_NOT_FOUND",
    "NETCFG_E_ALREADY_INITIALIZED",
    "NETCFG_E_COMPONENT_REMOVED_PENDING_REBOOT",
    "NETCFG_E_DUPLICATE_INSTANCEID",
    "NETCFG_E_IN_USE",
    "NETCFG_E_MAX_FILTER_LIMIT",
    "NETCFG_E_NEED_REBOOT",
    "NETCFG_E_NOT_INITIALIZED",
    "NETCFG_E_NO_WRITE_LOCK",
    "NETCFG_E_VMSWITCH_ACTIVE_OVER_ADAPTER",
    "NETCFG_SERVICE_CID_MS_NETBIOS",
    "NETCFG_SERVICE_CID_MS_PSCHED",
    "NETCFG_SERVICE_CID_MS_SERVER",
    "NETCFG_SERVICE_CID_MS_WLBS",
    "NETCFG_S_CAUSED_SETUP_CHANGE",
    "NETCFG_S_COMMIT_NOW",
    "NETCFG_S_DISABLE_QUERY",
    "NETCFG_S_REBOOT",
    "NETCFG_S_STILL_REFERENCED",
    "NETCFG_TRANS_CID_MS_APPLETALK",
    "NETCFG_TRANS_CID_MS_NETBEUI",
    "NETCFG_TRANS_CID_MS_NETMON",
    "NETCFG_TRANS_CID_MS_NWIPX",
    "NETCFG_TRANS_CID_MS_NWSPX",
    "NETCFG_TRANS_CID_MS_TCPIP",
    "NETLOGON_CONTROL_BACKUP_CHANGE_LOG",
    "NETLOGON_CONTROL_BREAKPOINT",
    "NETLOGON_CONTROL_CHANGE_PASSWORD",
    "NETLOGON_CONTROL_FIND_USER",
    "NETLOGON_CONTROL_FORCE_DNS_REG",
    "NETLOGON_CONTROL_PDC_REPLICATE",
    "NETLOGON_CONTROL_QUERY",
    "NETLOGON_CONTROL_QUERY_DNS_REG",
    "NETLOGON_CONTROL_QUERY_ENC_TYPES",
    "NETLOGON_CONTROL_REDISCOVER",
    "NETLOGON_CONTROL_REPLICATE",
    "NETLOGON_CONTROL_SET_DBFLAG",
    "NETLOGON_CONTROL_SYNCHRONIZE",
    "NETLOGON_CONTROL_TC_QUERY",
    "NETLOGON_CONTROL_TC_VERIFY",
    "NETLOGON_CONTROL_TRANSPORT_NOTIFY",
    "NETLOGON_CONTROL_TRUNCATE_LOG",
    "NETLOGON_CONTROL_UNLOAD_NETLOGON_DLL",
    "NETLOGON_DNS_UPDATE_FAILURE",
    "NETLOGON_FULL_SYNC_REPLICATION",
    "NETLOGON_HAS_IP",
    "NETLOGON_HAS_TIMESERV",
    "NETLOGON_INFO_1",
    "NETLOGON_INFO_2",
    "NETLOGON_INFO_3",
    "NETLOGON_INFO_4",
    "NETLOGON_REDO_NEEDED",
    "NETLOGON_REPLICATION_IN_PROGRESS",
    "NETLOGON_REPLICATION_NEEDED",
    "NETLOGON_VERIFY_STATUS_RETURNED",
    "NETLOG_NetlogonNonWindowsSupportsSecureRpc",
    "NETLOG_NetlogonUnsecureRpcClient",
    "NETLOG_NetlogonUnsecureRpcMachineAllowedBySsdl",
    "NETLOG_NetlogonUnsecureRpcTrust",
    "NETLOG_NetlogonUnsecureRpcTrustAllowedBySsdl",
    "NETLOG_NetlogonUnsecuredRpcMachineTemporarilyAllowed",
    "NETMAN_VARTYPE_HARDWARE_ADDRESS",
    "NETMAN_VARTYPE_STRING",
    "NETMAN_VARTYPE_ULONG",
    "NETSETUP_ACCT_CREATE",
    "NETSETUP_ACCT_DELETE",
    "NETSETUP_ALT_SAMACCOUNTNAME",
    "NETSETUP_AMBIGUOUS_DC",
    "NETSETUP_DEFER_SPN_SET",
    "NETSETUP_DNS_NAME_CHANGES_ONLY",
    "NETSETUP_DOMAIN_JOIN_IF_JOINED",
    "NETSETUP_DONT_CONTROL_SERVICES",
    "NETSETUP_FORCE_SPN_SET",
    "NETSETUP_IGNORE_UNSUPPORTED_FLAGS",
    "NETSETUP_INSTALL_INVOCATION",
    "NETSETUP_JOIN_DC_ACCOUNT",
    "NETSETUP_JOIN_DOMAIN",
    "NETSETUP_JOIN_READONLY",
    "NETSETUP_JOIN_STATUS",
    "NETSETUP_JOIN_STATUS_NetSetupDomainName",
    "NETSETUP_JOIN_STATUS_NetSetupUnjoined",
    "NETSETUP_JOIN_STATUS_NetSetupUnknownStatus",
    "NETSETUP_JOIN_STATUS_NetSetupWorkgroupName",
    "NETSETUP_JOIN_UNSECURE",
    "NETSETUP_JOIN_WITH_NEW_NAME",
    "NETSETUP_MACHINE_PWD_PASSED",
    "NETSETUP_NAME_TYPE",
    "NETSETUP_NAME_TYPE_NetSetupDnsMachine",
    "NETSETUP_NAME_TYPE_NetSetupDomain",
    "NETSETUP_NAME_TYPE_NetSetupMachine",
    "NETSETUP_NAME_TYPE_NetSetupNonExistentDomain",
    "NETSETUP_NAME_TYPE_NetSetupUnknown",
    "NETSETUP_NAME_TYPE_NetSetupWorkgroup",
    "NETSETUP_NO_ACCT_REUSE",
    "NETSETUP_NO_NETLOGON_CACHE",
    "NETSETUP_PROVISION",
    "NETSETUP_PROVISIONING_PARAMS",
    "NETSETUP_PROVISIONING_PARAMS_CURRENT_VERSION",
    "NETSETUP_PROVISIONING_PARAMS_WIN8_VERSION",
    "NETSETUP_PROVISION_CHECK_PWD_ONLY",
    "NETSETUP_PROVISION_DOWNLEVEL_PRIV_SUPPORT",
    "NETSETUP_PROVISION_ONLINE_CALLER",
    "NETSETUP_PROVISION_PERSISTENTSITE",
    "NETSETUP_PROVISION_REUSE_ACCOUNT",
    "NETSETUP_PROVISION_ROOT_CA_CERTS",
    "NETSETUP_PROVISION_SKIP_ACCOUNT_SEARCH",
    "NETSETUP_PROVISION_USE_DEFAULT_PASSWORD",
    "NETSETUP_SET_MACHINE_NAME",
    "NETSETUP_WIN9X_UPGRADE",
    "NETWORK_INSTALL_TIME",
    "NETWORK_NAME",
    "NETWORK_UPGRADE_TYPE",
    "NET_COMPUTER_NAME_TYPE",
    "NET_COMPUTER_NAME_TYPE_NetAllComputerNames",
    "NET_COMPUTER_NAME_TYPE_NetAlternateComputerNames",
    "NET_COMPUTER_NAME_TYPE_NetComputerNameTypeMax",
    "NET_COMPUTER_NAME_TYPE_NetPrimaryComputerName",
    "NET_DFS_ENUM",
    "NET_DFS_ENUMEX",
    "NET_DISPLAY_GROUP",
    "NET_DISPLAY_MACHINE",
    "NET_DISPLAY_USER",
    "NET_IGNORE_UNSUPPORTED_FLAGS",
    "NET_JOIN_DOMAIN_JOIN_OPTIONS",
    "NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS",
    "NET_REQUEST_PROVISION_OPTIONS",
    "NET_SERVER_TYPE",
    "NET_USER_ENUM_FILTER_FLAGS",
    "NET_VALIDATE_AUTHENTICATION_INPUT_ARG",
    "NET_VALIDATE_BAD_PASSWORD_COUNT",
    "NET_VALIDATE_BAD_PASSWORD_TIME",
    "NET_VALIDATE_LOCKOUT_TIME",
    "NET_VALIDATE_OUTPUT_ARG",
    "NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG",
    "NET_VALIDATE_PASSWORD_HASH",
    "NET_VALIDATE_PASSWORD_HISTORY",
    "NET_VALIDATE_PASSWORD_HISTORY_LENGTH",
    "NET_VALIDATE_PASSWORD_LAST_SET",
    "NET_VALIDATE_PASSWORD_RESET_INPUT_ARG",
    "NET_VALIDATE_PASSWORD_TYPE",
    "NET_VALIDATE_PASSWORD_TYPE_NetValidateAuthentication",
    "NET_VALIDATE_PASSWORD_TYPE_NetValidatePasswordChange",
    "NET_VALIDATE_PASSWORD_TYPE_NetValidatePasswordReset",
    "NET_VALIDATE_PERSISTED_FIELDS",
    "NON_VALIDATED_LOGON",
    "NOT_A_DFS_PATH",
    "NO_PERMISSION_REQUIRED",
    "NSF_COMPONENT_UPDATE",
    "NSF_POSTSYSINSTALL",
    "NSF_PRIMARYINSTALL",
    "NSF_WIN16_UPGRADE",
    "NSF_WIN95_UPGRADE",
    "NSF_WINNT_SBS_UPGRADE",
    "NSF_WINNT_SVR_UPGRADE",
    "NSF_WINNT_WKS_UPGRADE",
    "NTFRSPRF_COLLECT_RPC_BINDING_ERROR_CONN",
    "NTFRSPRF_COLLECT_RPC_BINDING_ERROR_SET",
    "NTFRSPRF_COLLECT_RPC_CALL_ERROR_CONN",
    "NTFRSPRF_COLLECT_RPC_CALL_ERROR_SET",
    "NTFRSPRF_OPEN_RPC_BINDING_ERROR_CONN",
    "NTFRSPRF_OPEN_RPC_BINDING_ERROR_SET",
    "NTFRSPRF_OPEN_RPC_CALL_ERROR_CONN",
    "NTFRSPRF_OPEN_RPC_CALL_ERROR_SET",
    "NTFRSPRF_REGISTRY_ERROR_CONN",
    "NTFRSPRF_REGISTRY_ERROR_SET",
    "NTFRSPRF_VIRTUALALLOC_ERROR_CONN",
    "NTFRSPRF_VIRTUALALLOC_ERROR_SET",
    "NULL_USERSETINFO_PASSWD",
    "NWSAP_DISPLAY_NAME",
    "NWSAP_EVENT_BADWANFILTER_VALUE",
    "NWSAP_EVENT_BIND_FAILED",
    "NWSAP_EVENT_CARDLISTEVENT_FAIL",
    "NWSAP_EVENT_CARDMALLOC_FAILED",
    "NWSAP_EVENT_CREATELPCEVENT_ERROR",
    "NWSAP_EVENT_CREATELPCPORT_ERROR",
    "NWSAP_EVENT_GETSOCKNAME_FAILED",
    "NWSAP_EVENT_HASHTABLE_MALLOC_FAILED",
    "NWSAP_EVENT_INVALID_FILTERNAME",
    "NWSAP_EVENT_KEY_NOT_FOUND",
    "NWSAP_EVENT_LPCHANDLEMEMORY_ERROR",
    "NWSAP_EVENT_LPCLISTENMEMORY_ERROR",
    "NWSAP_EVENT_NOCARDS",
    "NWSAP_EVENT_OPTBCASTINADDR_FAILED",
    "NWSAP_EVENT_OPTEXTENDEDADDR_FAILED",
    "NWSAP_EVENT_OPTMAXADAPTERNUM_ERROR",
    "NWSAP_EVENT_RECVSEM_FAIL",
    "NWSAP_EVENT_SDMDEVENT_FAIL",
    "NWSAP_EVENT_SENDEVENT_FAIL",
    "NWSAP_EVENT_SETOPTBCAST_FAILED",
    "NWSAP_EVENT_SOCKET_FAILED",
    "NWSAP_EVENT_STARTLPCWORKER_ERROR",
    "NWSAP_EVENT_STARTRECEIVE_ERROR",
    "NWSAP_EVENT_STARTWANCHECK_ERROR",
    "NWSAP_EVENT_STARTWANWORKER_ERROR",
    "NWSAP_EVENT_STARTWORKER_ERROR",
    "NWSAP_EVENT_TABLE_MALLOC_FAILED",
    "NWSAP_EVENT_THREADEVENT_FAIL",
    "NWSAP_EVENT_WANBIND_FAILED",
    "NWSAP_EVENT_WANEVENT_ERROR",
    "NWSAP_EVENT_WANHANDLEMEMORY_ERROR",
    "NWSAP_EVENT_WANSEM_FAIL",
    "NWSAP_EVENT_WANSOCKET_FAILED",
    "NWSAP_EVENT_WSASTARTUP_FAILED",
    "NetAccessAdd",
    "NetAccessDel",
    "NetAccessEnum",
    "NetAccessGetInfo",
    "NetAccessGetUserPerms",
    "NetAccessSetInfo",
    "NetAddAlternateComputerName",
    "NetAddServiceAccount",
    "NetAlertRaise",
    "NetAlertRaiseEx",
    "NetApiBufferAllocate",
    "NetApiBufferFree",
    "NetApiBufferReallocate",
    "NetApiBufferSize",
    "NetAuditClear",
    "NetAuditRead",
    "NetAuditWrite",
    "NetConfigGet",
    "NetConfigGetAll",
    "NetConfigSet",
    "NetCreateProvisioningPackage",
    "NetEnumerateComputerNames",
    "NetEnumerateServiceAccounts",
    "NetErrorLogClear",
    "NetErrorLogRead",
    "NetErrorLogWrite",
    "NetFreeAadJoinInformation",
    "NetGetAadJoinInformation",
    "NetGetAnyDCName",
    "NetGetDCName",
    "NetGetDisplayInformationIndex",
    "NetGetJoinInformation",
    "NetGetJoinableOUs",
    "NetGroupAdd",
    "NetGroupAddUser",
    "NetGroupDel",
    "NetGroupDelUser",
    "NetGroupEnum",
    "NetGroupGetInfo",
    "NetGroupGetUsers",
    "NetGroupSetInfo",
    "NetGroupSetUsers",
    "NetIsServiceAccount",
    "NetJoinDomain",
    "NetLocalGroupAdd",
    "NetLocalGroupAddMember",
    "NetLocalGroupAddMembers",
    "NetLocalGroupDel",
    "NetLocalGroupDelMember",
    "NetLocalGroupDelMembers",
    "NetLocalGroupEnum",
    "NetLocalGroupGetInfo",
    "NetLocalGroupGetMembers",
    "NetLocalGroupSetInfo",
    "NetLocalGroupSetMembers",
    "NetMessageBufferSend",
    "NetMessageNameAdd",
    "NetMessageNameDel",
    "NetMessageNameEnum",
    "NetMessageNameGetInfo",
    "NetProvisionComputerAccount",
    "NetProvisioning",
    "NetQueryDisplayInformation",
    "NetQueryServiceAccount",
    "NetRemoteComputerSupports",
    "NetRemoteTOD",
    "NetRemoveAlternateComputerName",
    "NetRemoveServiceAccount",
    "NetRenameMachineInDomain",
    "NetReplExportDirAdd",
    "NetReplExportDirDel",
    "NetReplExportDirEnum",
    "NetReplExportDirGetInfo",
    "NetReplExportDirLock",
    "NetReplExportDirSetInfo",
    "NetReplExportDirUnlock",
    "NetReplGetInfo",
    "NetReplImportDirAdd",
    "NetReplImportDirDel",
    "NetReplImportDirEnum",
    "NetReplImportDirGetInfo",
    "NetReplImportDirLock",
    "NetReplImportDirUnlock",
    "NetReplSetInfo",
    "NetRequestOfflineDomainJoin",
    "NetRequestProvisioningPackageInstall",
    "NetScheduleJobAdd",
    "NetScheduleJobDel",
    "NetScheduleJobEnum",
    "NetScheduleJobGetInfo",
    "NetServerComputerNameAdd",
    "NetServerComputerNameDel",
    "NetServerDiskEnum",
    "NetServerEnum",
    "NetServerGetInfo",
    "NetServerSetInfo",
    "NetServerTransportAdd",
    "NetServerTransportAddEx",
    "NetServerTransportDel",
    "NetServerTransportEnum",
    "NetServiceControl",
    "NetServiceEnum",
    "NetServiceGetInfo",
    "NetServiceInstall",
    "NetSetPrimaryComputerName",
    "NetUnjoinDomain",
    "NetUseAdd",
    "NetUseDel",
    "NetUseEnum",
    "NetUseGetInfo",
    "NetUserAdd",
    "NetUserChangePassword",
    "NetUserDel",
    "NetUserEnum",
    "NetUserGetGroups",
    "NetUserGetInfo",
    "NetUserGetLocalGroups",
    "NetUserModalsGet",
    "NetUserModalsSet",
    "NetUserSetGroups",
    "NetUserSetInfo",
    "NetValidateName",
    "NetValidatePasswordPolicy",
    "NetValidatePasswordPolicyFree",
    "NetWkstaGetInfo",
    "NetWkstaSetInfo",
    "NetWkstaTransportAdd",
    "NetWkstaTransportDel",
    "NetWkstaTransportEnum",
    "NetWkstaUserEnum",
    "NetWkstaUserGetInfo",
    "NetWkstaUserSetInfo",
    "OBO_COMPONENT",
    "OBO_SOFTWARE",
    "OBO_TOKEN",
    "OBO_TOKEN_TYPE",
    "OBO_USER",
    "OS2MSG_FILENAME",
    "PARMNUM_ALL",
    "PARMNUM_BASE_INFOLEVEL",
    "PARM_ERROR_NONE",
    "PARM_ERROR_UNKNOWN",
    "PASSWORD_EXPIRED",
    "PATHLEN",
    "PLATFORM_ID_DOS",
    "PLATFORM_ID_NT",
    "PLATFORM_ID_OS2",
    "PLATFORM_ID_OSF",
    "PLATFORM_ID_VMS",
    "PREFIX_MISMATCH",
    "PREFIX_MISMATCH_FIXED",
    "PREFIX_MISMATCH_NOT_FIXED",
    "PRINT_OTHER_INFO",
    "PRJOB_COMPLETE",
    "PRJOB_DELETED",
    "PRJOB_DESTNOPAPER",
    "PRJOB_DESTOFFLINE",
    "PRJOB_DESTPAUSED",
    "PRJOB_DEVSTATUS",
    "PRJOB_ERROR",
    "PRJOB_INTERV",
    "PRJOB_NOTIFY",
    "PRJOB_QSTATUS",
    "PRJOB_QS_PAUSED",
    "PRJOB_QS_PRINTING",
    "PRJOB_QS_QUEUED",
    "PRJOB_QS_SPOOLING",
    "PROTO_IPV6_DHCP",
    "PROTO_IP_ALG",
    "PROTO_IP_BGMP",
    "PROTO_IP_BOOTP",
    "PROTO_IP_DHCP_ALLOCATOR",
    "PROTO_IP_DIFFSERV",
    "PROTO_IP_DNS_PROXY",
    "PROTO_IP_DTP",
    "PROTO_IP_FTP",
    "PROTO_IP_H323",
    "PROTO_IP_IGMP",
    "PROTO_IP_MGM",
    "PROTO_IP_MSDP",
    "PROTO_IP_NAT",
    "PROTO_IP_VRRP",
    "PROTO_TYPE_MCAST",
    "PROTO_TYPE_MS0",
    "PROTO_TYPE_MS1",
    "PROTO_TYPE_UCAST",
    "PROTO_VENDOR_MS0",
    "PROTO_VENDOR_MS1",
    "PROTO_VENDOR_MS2",
    "PWLEN",
    "QNLEN",
    "RASCON_IPUI",
    "RASCON_UIINFO_FLAGS",
    "RCUIF_DEMAND_DIAL",
    "RCUIF_DISABLE_CLASS_BASED_ROUTE",
    "RCUIF_ENABLE_NBT",
    "RCUIF_NOT_ADMIN",
    "RCUIF_USE_DISABLE_REGISTER_DNS",
    "RCUIF_USE_HEADER_COMPRESSION",
    "RCUIF_USE_IPv4_EXPLICIT_METRIC",
    "RCUIF_USE_IPv4_NAME_SERVERS",
    "RCUIF_USE_IPv4_REMOTE_GATEWAY",
    "RCUIF_USE_IPv4_STATICADDRESS",
    "RCUIF_USE_IPv6_EXPLICIT_METRIC",
    "RCUIF_USE_IPv6_NAME_SERVERS",
    "RCUIF_USE_IPv6_REMOTE_GATEWAY",
    "RCUIF_USE_IPv6_STATICADDRESS",
    "RCUIF_USE_PRIVATE_DNS_SUFFIX",
    "RCUIF_VPN",
    "REGISTER_PROTOCOL_ENTRY_POINT_STRING",
    "REPL_EDIR_INFO_0",
    "REPL_EDIR_INFO_1",
    "REPL_EDIR_INFO_1000",
    "REPL_EDIR_INFO_1001",
    "REPL_EDIR_INFO_2",
    "REPL_EXPORT_EXTENT_INFOLEVEL",
    "REPL_EXPORT_INTEGRITY_INFOLEVEL",
    "REPL_EXTENT_FILE",
    "REPL_EXTENT_TREE",
    "REPL_GUARDTIME_INFOLEVEL",
    "REPL_IDIR_INFO_0",
    "REPL_IDIR_INFO_1",
    "REPL_INFO_0",
    "REPL_INFO_1000",
    "REPL_INFO_1001",
    "REPL_INFO_1002",
    "REPL_INFO_1003",
    "REPL_INTEGRITY_FILE",
    "REPL_INTEGRITY_TREE",
    "REPL_INTERVAL_INFOLEVEL",
    "REPL_PULSE_INFOLEVEL",
    "REPL_RANDOM_INFOLEVEL",
    "REPL_ROLE_BOTH",
    "REPL_ROLE_EXPORT",
    "REPL_ROLE_IMPORT",
    "REPL_STATE_NEVER_REPLICATED",
    "REPL_STATE_NO_MASTER",
    "REPL_STATE_NO_SYNC",
    "REPL_STATE_OK",
    "REPL_UNLOCK_FORCE",
    "REPL_UNLOCK_NOFORCE",
    "RF_ADD_ALL_INTERFACES",
    "RF_DEMAND_UPDATE_ROUTES",
    "RF_MULTICAST",
    "RF_POWER",
    "RF_ROUTING",
    "RF_ROUTINGV6",
    "RIS_INTERFACE_ADDRESS_CHANGE",
    "RIS_INTERFACE_DISABLED",
    "RIS_INTERFACE_ENABLED",
    "RIS_INTERFACE_MEDIA_ABSENT",
    "RIS_INTERFACE_MEDIA_PRESENT",
    "ROUTING_DOMAIN_INFO_REVISION_1",
    "RTR_INFO_BLOCK_HEADER",
    "RTR_INFO_BLOCK_VERSION",
    "RTR_TOC_ENTRY",
    "RTUTILS_MAX_PROTOCOL_DLL_LEN",
    "RTUTILS_MAX_PROTOCOL_NAME_LEN",
    "RouterAssert",
    "RouterGetErrorStringA",
    "RouterGetErrorStringW",
    "RouterLogDeregisterA",
    "RouterLogDeregisterW",
    "RouterLogEventA",
    "RouterLogEventDataA",
    "RouterLogEventDataW",
    "RouterLogEventExA",
    "RouterLogEventExW",
    "RouterLogEventStringA",
    "RouterLogEventStringW",
    "RouterLogEventValistExA",
    "RouterLogEventValistExW",
    "RouterLogEventW",
    "RouterLogRegisterA",
    "RouterLogRegisterW",
    "SERVCE_LM20_W32TIME",
    "SERVER_DISPLAY_NAME",
    "SERVER_INFO_100",
    "SERVER_INFO_1005",
    "SERVER_INFO_101",
    "SERVER_INFO_1010",
    "SERVER_INFO_1016",
    "SERVER_INFO_1017",
    "SERVER_INFO_1018",
    "SERVER_INFO_102",
    "SERVER_INFO_103",
    "SERVER_INFO_1107",
    "SERVER_INFO_1501",
    "SERVER_INFO_1502",
    "SERVER_INFO_1503",
    "SERVER_INFO_1506",
    "SERVER_INFO_1509",
    "SERVER_INFO_1510",
    "SERVER_INFO_1511",
    "SERVER_INFO_1512",
    "SERVER_INFO_1513",
    "SERVER_INFO_1514",
    "SERVER_INFO_1515",
    "SERVER_INFO_1516",
    "SERVER_INFO_1518",
    "SERVER_INFO_1520",
    "SERVER_INFO_1521",
    "SERVER_INFO_1522",
    "SERVER_INFO_1523",
    "SERVER_INFO_1524",
    "SERVER_INFO_1525",
    "SERVER_INFO_1528",
    "SERVER_INFO_1529",
    "SERVER_INFO_1530",
    "SERVER_INFO_1533",
    "SERVER_INFO_1534",
    "SERVER_INFO_1535",
    "SERVER_INFO_1536",
    "SERVER_INFO_1537",
    "SERVER_INFO_1538",
    "SERVER_INFO_1539",
    "SERVER_INFO_1540",
    "SERVER_INFO_1541",
    "SERVER_INFO_1542",
    "SERVER_INFO_1543",
    "SERVER_INFO_1544",
    "SERVER_INFO_1545",
    "SERVER_INFO_1546",
    "SERVER_INFO_1547",
    "SERVER_INFO_1548",
    "SERVER_INFO_1549",
    "SERVER_INFO_1550",
    "SERVER_INFO_1552",
    "SERVER_INFO_1553",
    "SERVER_INFO_1554",
    "SERVER_INFO_1555",
    "SERVER_INFO_1556",
    "SERVER_INFO_1557",
    "SERVER_INFO_1560",
    "SERVER_INFO_1561",
    "SERVER_INFO_1562",
    "SERVER_INFO_1563",
    "SERVER_INFO_1564",
    "SERVER_INFO_1565",
    "SERVER_INFO_1566",
    "SERVER_INFO_1567",
    "SERVER_INFO_1568",
    "SERVER_INFO_1569",
    "SERVER_INFO_1570",
    "SERVER_INFO_1571",
    "SERVER_INFO_1572",
    "SERVER_INFO_1573",
    "SERVER_INFO_1574",
    "SERVER_INFO_1575",
    "SERVER_INFO_1576",
    "SERVER_INFO_1577",
    "SERVER_INFO_1578",
    "SERVER_INFO_1579",
    "SERVER_INFO_1580",
    "SERVER_INFO_1581",
    "SERVER_INFO_1582",
    "SERVER_INFO_1583",
    "SERVER_INFO_1584",
    "SERVER_INFO_1585",
    "SERVER_INFO_1586",
    "SERVER_INFO_1587",
    "SERVER_INFO_1588",
    "SERVER_INFO_1590",
    "SERVER_INFO_1591",
    "SERVER_INFO_1592",
    "SERVER_INFO_1593",
    "SERVER_INFO_1594",
    "SERVER_INFO_1595",
    "SERVER_INFO_1596",
    "SERVER_INFO_1597",
    "SERVER_INFO_1598",
    "SERVER_INFO_1599",
    "SERVER_INFO_1600",
    "SERVER_INFO_1601",
    "SERVER_INFO_1602",
    "SERVER_INFO_402",
    "SERVER_INFO_403",
    "SERVER_INFO_502",
    "SERVER_INFO_503",
    "SERVER_INFO_598",
    "SERVER_INFO_599",
    "SERVER_INFO_HIDDEN",
    "SERVER_INFO_SECURITY",
    "SERVER_TRANSPORT_INFO_0",
    "SERVER_TRANSPORT_INFO_1",
    "SERVER_TRANSPORT_INFO_2",
    "SERVER_TRANSPORT_INFO_3",
    "SERVICE2_BASE",
    "SERVICE_ACCOUNT_FLAG_ADD_AGAINST_RODC",
    "SERVICE_ACCOUNT_FLAG_LINK_TO_HOST_ONLY",
    "SERVICE_ACCOUNT_FLAG_REMOVE_OFFLINE",
    "SERVICE_ACCOUNT_FLAG_UNLINK_FROM_HOST_ONLY",
    "SERVICE_ACCOUNT_PASSWORD",
    "SERVICE_ACCOUNT_SECRET_PREFIX",
    "SERVICE_ADWS",
    "SERVICE_AFP",
    "SERVICE_ALERTER",
    "SERVICE_BASE",
    "SERVICE_BROWSER",
    "SERVICE_CCP_CHKPT_NUM",
    "SERVICE_CCP_NO_HINT",
    "SERVICE_CCP_QUERY_HINT",
    "SERVICE_CCP_WAIT_TIME",
    "SERVICE_CTRL_CONTINUE",
    "SERVICE_CTRL_INTERROGATE",
    "SERVICE_CTRL_PAUSE",
    "SERVICE_CTRL_REDIR_COMM",
    "SERVICE_CTRL_REDIR_DISK",
    "SERVICE_CTRL_REDIR_PRINT",
    "SERVICE_CTRL_UNINSTALL",
    "SERVICE_DHCP",
    "SERVICE_DNS_CACHE",
    "SERVICE_DOS_ENCRYPTION",
    "SERVICE_DSROLE",
    "SERVICE_INFO_0",
    "SERVICE_INFO_1",
    "SERVICE_INFO_2",
    "SERVICE_INSTALLED",
    "SERVICE_INSTALL_PENDING",
    "SERVICE_INSTALL_STATE",
    "SERVICE_IP_CHKPT_NUM",
    "SERVICE_IP_NO_HINT",
    "SERVICE_IP_QUERY_HINT",
    "SERVICE_IP_WAITTIME_SHIFT",
    "SERVICE_IP_WAIT_TIME",
    "SERVICE_ISMSERV",
    "SERVICE_KDC",
    "SERVICE_LM20_AFP",
    "SERVICE_LM20_ALERTER",
    "SERVICE_LM20_BROWSER",
    "SERVICE_LM20_DHCP",
    "SERVICE_LM20_DSROLE",
    "SERVICE_LM20_ISMSERV",
    "SERVICE_LM20_KDC",
    "SERVICE_LM20_LMHOSTS",
    "SERVICE_LM20_MESSENGER",
    "SERVICE_LM20_NBT",
    "SERVICE_LM20_NETLOGON",
    "SERVICE_LM20_NETPOPUP",
    "SERVICE_LM20_NETRUN",
    "SERVICE_LM20_NTDS",
    "SERVICE_LM20_NTFRS",
    "SERVICE_LM20_NWSAP",
    "SERVICE_LM20_REPL",
    "SERVICE_LM20_RIPL",
    "SERVICE_LM20_RPCLOCATOR",
    "SERVICE_LM20_SCHEDULE",
    "SERVICE_LM20_SERVER",
    "SERVICE_LM20_SPOOLER",
    "SERVICE_LM20_SQLSERVER",
    "SERVICE_LM20_TCPIP",
    "SERVICE_LM20_TELNET",
    "SERVICE_LM20_TIMESOURCE",
    "SERVICE_LM20_TRKSVR",
    "SERVICE_LM20_TRKWKS",
    "SERVICE_LM20_UPS",
    "SERVICE_LM20_WORKSTATION",
    "SERVICE_LM20_XACTSRV",
    "SERVICE_LMHOSTS",
    "SERVICE_MAXTIME",
    "SERVICE_MESSENGER",
    "SERVICE_NBT",
    "SERVICE_NETLOGON",
    "SERVICE_NETPOPUP",
    "SERVICE_NETRUN",
    "SERVICE_NOT_PAUSABLE",
    "SERVICE_NOT_UNINSTALLABLE",
    "SERVICE_NTDS",
    "SERVICE_NTFRS",
    "SERVICE_NTIP_WAITTIME_SHIFT",
    "SERVICE_NTLMSSP",
    "SERVICE_NT_MAXTIME",
    "SERVICE_NWCS",
    "SERVICE_NWSAP",
    "SERVICE_PAUSABLE",
    "SERVICE_PAUSE_STATE",
    "SERVICE_REDIR_COMM_PAUSED",
    "SERVICE_REDIR_DISK_PAUSED",
    "SERVICE_REDIR_PAUSED",
    "SERVICE_REDIR_PRINT_PAUSED",
    "SERVICE_REPL",
    "SERVICE_RESRV_MASK",
    "SERVICE_RIPL",
    "SERVICE_RPCLOCATOR",
    "SERVICE_SCHEDULE",
    "SERVICE_SERVER",
    "SERVICE_SPOOLER",
    "SERVICE_SQLSERVER",
    "SERVICE_TCPIP",
    "SERVICE_TELNET",
    "SERVICE_TIMESOURCE",
    "SERVICE_TRKSVR",
    "SERVICE_TRKWKS",
    "SERVICE_UIC_AMBIGPARM",
    "SERVICE_UIC_BADPARMVAL",
    "SERVICE_UIC_CONFIG",
    "SERVICE_UIC_CONFLPARM",
    "SERVICE_UIC_DUPPARM",
    "SERVICE_UIC_EXEC",
    "SERVICE_UIC_FILE",
    "SERVICE_UIC_INTERNAL",
    "SERVICE_UIC_KILL",
    "SERVICE_UIC_MISSPARM",
    "SERVICE_UIC_M_ADDPAK",
    "SERVICE_UIC_M_ANNOUNCE",
    "SERVICE_UIC_M_DATABASE_ERROR",
    "SERVICE_UIC_M_DISK",
    "SERVICE_UIC_M_ERRLOG",
    "SERVICE_UIC_M_FILES",
    "SERVICE_UIC_M_FILE_UW",
    "SERVICE_UIC_M_LANGROUP",
    "SERVICE_UIC_M_LANROOT",
    "SERVICE_UIC_M_LAZY",
    "SERVICE_UIC_M_LOGS",
    "SERVICE_UIC_M_LSA_MACHINE_ACCT",
    "SERVICE_UIC_M_MEMORY",
    "SERVICE_UIC_M_MSGNAME",
    "SERVICE_UIC_M_NETLOGON_AUTH",
    "SERVICE_UIC_M_NETLOGON_DC_CFLCT",
    "SERVICE_UIC_M_NETLOGON_MPATH",
    "SERVICE_UIC_M_NETLOGON_NO_DC",
    "SERVICE_UIC_M_NULL",
    "SERVICE_UIC_M_PROCESSES",
    "SERVICE_UIC_M_REDIR",
    "SERVICE_UIC_M_SECURITY",
    "SERVICE_UIC_M_SEC_FILE_ERR",
    "SERVICE_UIC_M_SERVER",
    "SERVICE_UIC_M_SERVER_SEC_ERR",
    "SERVICE_UIC_M_THREADS",
    "SERVICE_UIC_M_UAS",
    "SERVICE_UIC_M_UAS_INVALID_ROLE",
    "SERVICE_UIC_M_UAS_MACHINE_ACCT",
    "SERVICE_UIC_M_UAS_PROLOG",
    "SERVICE_UIC_M_UAS_SERVERS_NMEMB",
    "SERVICE_UIC_M_UAS_SERVERS_NOGRP",
    "SERVICE_UIC_M_WKSTA",
    "SERVICE_UIC_NORMAL",
    "SERVICE_UIC_RESOURCE",
    "SERVICE_UIC_SUBSERV",
    "SERVICE_UIC_SYSTEM",
    "SERVICE_UIC_UNKPARM",
    "SERVICE_UNINSTALLABLE",
    "SERVICE_UNINSTALLED",
    "SERVICE_UNINSTALL_PENDING",
    "SERVICE_UPS",
    "SERVICE_W32TIME",
    "SERVICE_WORKSTATION",
    "SERVICE_XACTSRV",
    "SESSION_CRYPT_KLEN",
    "SESSION_PWLEN",
    "SHPWLEN",
    "SMB_COMPRESSION_INFO",
    "SMB_TREE_CONNECT_PARAMETERS",
    "SMB_USE_OPTION_COMPRESSION_PARAMETERS",
    "SNLEN",
    "SRV_HASH_GENERATION_ACTIVE",
    "SRV_SUPPORT_HASH_GENERATION",
    "STD_ALERT",
    "STXTLEN",
    "SUPPORTS_ANY",
    "SUPPORTS_BINDING_INTERFACE_FLAGS",
    "SUPPORTS_LOCAL",
    "SUPPORTS_REMOTE_ADMIN_PROTOCOL",
    "SUPPORTS_RPC",
    "SUPPORTS_SAM_PROTOCOL",
    "SUPPORTS_UNICODE",
    "SVAUD_BADNETLOGON",
    "SVAUD_BADSESSLOGON",
    "SVAUD_BADUSE",
    "SVAUD_GOODNETLOGON",
    "SVAUD_GOODSESSLOGON",
    "SVAUD_GOODUSE",
    "SVAUD_LOGONLIM",
    "SVAUD_PERMISSIONS",
    "SVAUD_RESOURCE",
    "SVAUD_SERVICE",
    "SVAUD_USERLIST",
    "SVI1_NUM_ELEMENTS",
    "SVI2_NUM_ELEMENTS",
    "SVI3_NUM_ELEMENTS",
    "SVTI2_CLUSTER_DNN_NAME",
    "SVTI2_CLUSTER_NAME",
    "SVTI2_REMAP_PIPE_NAMES",
    "SVTI2_RESERVED1",
    "SVTI2_RESERVED2",
    "SVTI2_RESERVED3",
    "SVTI2_SCOPED_NAME",
    "SVTI2_UNICODE_TRANSPORT_ADDRESS",
    "SV_ACCEPTDOWNLEVELAPIS_PARMNUM",
    "SV_ACCESSALERT_PARMNUM",
    "SV_ACTIVELOCKS_PARMNUM",
    "SV_ALERTSCHEDULE_PARMNUM",
    "SV_ALERTSCHED_PARMNUM",
    "SV_ALERTS_PARMNUM",
    "SV_ALIST_MTIME_PARMNUM",
    "SV_ANNDELTA_PARMNUM",
    "SV_ANNOUNCE_PARMNUM",
    "SV_AUTOSHARESERVER_PARMNUM",
    "SV_AUTOSHAREWKS_PARMNUM",
    "SV_BALANCECOUNT_PARMNUM",
    "SV_CACHEDDIRECTORYLIMIT_PARMNUM",
    "SV_CACHEDOPENLIMIT_PARMNUM",
    "SV_CHDEVJOBS_PARMNUM",
    "SV_CHDEVQ_PARMNUM",
    "SV_COMMENT_PARMNUM",
    "SV_CONNECTIONLESSAUTODISC_PARMNUM",
    "SV_CONNECTIONNOSESSIONSTIMEOUT_PARMNUM",
    "SV_CONNECTIONS_PARMNUM",
    "SV_CRITICALTHREADS_PARMNUM",
    "SV_DISABLEDOS_PARMNUM",
    "SV_DISABLESTRICTNAMECHECKING_PARMNUM",
    "SV_DISC_PARMNUM",
    "SV_DISKALERT_PARMNUM",
    "SV_DISKSPACETHRESHOLD_PARMNUM",
    "SV_DOMAIN_PARMNUM",
    "SV_ENABLEAUTHENTICATEUSERSHARING_PARMNUM",
    "SV_ENABLECOMPRESSION_PARMNUM",
    "SV_ENABLEFCBOPENS_PARMNUM",
    "SV_ENABLEFORCEDLOGOFF_PARMNUM",
    "SV_ENABLEOPLOCKFORCECLOSE_PARMNUM",
    "SV_ENABLEOPLOCKS_PARMNUM",
    "SV_ENABLERAW_PARMNUM",
    "SV_ENABLESECURITYSIGNATURE_PARMNUM",
    "SV_ENABLESHAREDNETDRIVES_PARMNUM",
    "SV_ENABLESOFTCOMPAT_PARMNUM",
    "SV_ENABLEW9XSECURITYSIGNATURE_PARMNUM",
    "SV_ENABLEWFW311DIRECTIPX_PARMNUM",
    "SV_ENFORCEKERBEROSREAUTHENTICATION_PARMNUM",
    "SV_ERRORALERT_PARMNUM",
    "SV_ERRORTHRESHOLD_PARMNUM",
    "SV_GLIST_MTIME_PARMNUM",
    "SV_GUESTACC_PARMNUM",
    "SV_HIDDEN",
    "SV_HIDDEN_PARMNUM",
    "SV_IDLETHREADTIMEOUT_PARMNUM",
    "SV_INITCONNTABLE_PARMNUM",
    "SV_INITFILETABLE_PARMNUM",
    "SV_INITSEARCHTABLE_PARMNUM",
    "SV_INITSESSTABLE_PARMNUM",
    "SV_INITWORKITEMS_PARMNUM",
    "SV_IRPSTACKSIZE_PARMNUM",
    "SV_LANMASK_PARMNUM",
    "SV_LINKINFOVALIDTIME_PARMNUM",
    "SV_LMANNOUNCE_PARMNUM",
    "SV_LOCKVIOLATIONDELAY_PARMNUM",
    "SV_LOCKVIOLATIONOFFSET_PARMNUM",
    "SV_LOCKVIOLATIONRETRIES_PARMNUM",
    "SV_LOGONALERT_PARMNUM",
    "SV_LOWDISKSPACEMINIMUM_PARMNUM",
    "SV_MAXAUDITSZ_PARMNUM",
    "SV_MAXCOPYLENGTH_PARMNUM",
    "SV_MAXCOPYREADLEN_PARMNUM",
    "SV_MAXCOPYWRITELEN_PARMNUM",
    "SV_MAXFREECONNECTIONS_PARMNUM",
    "SV_MAXFREELFCBS_PARMNUM",
    "SV_MAXFREEMFCBS_PARMNUM",
    "SV_MAXFREEPAGEDPOOLCHUNKS_PARMNUM",
    "SV_MAXFREERFCBS_PARMNUM",
    "SV_MAXGLOBALOPENSEARCH_PARMNUM",
    "SV_MAXKEEPCOMPLSEARCH_PARMNUM",
    "SV_MAXKEEPSEARCH_PARMNUM",
    "SV_MAXLINKDELAY_PARMNUM",
    "SV_MAXMPXCT_PARMNUM",
    "SV_MAXNONPAGEDMEMORYUSAGE_PARMNUM",
    "SV_MAXPAGEDMEMORYUSAGE_PARMNUM",
    "SV_MAXPAGEDPOOLCHUNKSIZE_PARMNUM",
    "SV_MAXRAWBUFLEN_PARMNUM",
    "SV_MAXRAWWORKITEMS_PARMNUM",
    "SV_MAXTHREADSPERQUEUE_PARMNUM",
    "SV_MAXWORKITEMIDLETIME_PARMNUM",
    "SV_MAXWORKITEMS_PARMNUM",
    "SV_MAX_CMD_LEN",
    "SV_MAX_SRV_HEUR_LEN",
    "SV_MDLREADSWITCHOVER_PARMNUM",
    "SV_MINCLIENTBUFFERSIZE_PARMNUM",
    "SV_MINFREECONNECTIONS_PARMNUM",
    "SV_MINFREEWORKITEMS_PARMNUM",
    "SV_MINKEEPCOMPLSEARCH_PARMNUM",
    "SV_MINKEEPSEARCH_PARMNUM",
    "SV_MINLINKTHROUGHPUT_PARMNUM",
    "SV_MINPAGEDPOOLCHUNKSIZE_PARMNUM",
    "SV_MINRCVQUEUE_PARMNUM",
    "SV_NAME_PARMNUM",
    "SV_NETIOALERT_PARMNUM",
    "SV_NETWORKERRORTHRESHOLD_PARMNUM",
    "SV_NODISC",
    "SV_NUMADMIN_PARMNUM",
    "SV_NUMBIGBUF_PARMNUM",
    "SV_NUMBLOCKTHREADS_PARMNUM",
    "SV_NUMFILETASKS_PARMNUM",
    "SV_NUMREQBUF_PARMNUM",
    "SV_OPENFILES_PARMNUM",
    "SV_OPENSEARCH_PARMNUM",
    "SV_OPLOCKBREAKRESPONSEWAIT_PARMNUM",
    "SV_OPLOCKBREAKWAIT_PARMNUM",
    "SV_OTHERQUEUEAFFINITY_PARMNUM",
    "SV_PLATFORM_ID_NT",
    "SV_PLATFORM_ID_OS2",
    "SV_PLATFORM_ID_PARMNUM",
    "SV_PREFERREDAFFINITY_PARMNUM",
    "SV_PRODUCTTYPE_PARMNUM",
    "SV_QUEUESAMPLESECS_PARMNUM",
    "SV_RAWWORKITEMS_PARMNUM",
    "SV_REMOVEDUPLICATESEARCHES_PARMNUM",
    "SV_REQUIRESECURITYSIGNATURE_PARMNUM",
    "SV_RESTRICTNULLSESSACCESS_PARMNUM",
    "SV_SCAVQOSINFOUPDATETIME_PARMNUM",
    "SV_SCAVTIMEOUT_PARMNUM",
    "SV_SECURITY_PARMNUM",
    "SV_SENDSFROMPREFERREDPROCESSOR_PARMNUM",
    "SV_SERVERSIZE_PARMNUM",
    "SV_SESSCONNS_PARMNUM",
    "SV_SESSOPENS_PARMNUM",
    "SV_SESSREQS_PARMNUM",
    "SV_SESSUSERS_PARMNUM",
    "SV_SESSVCS_PARMNUM",
    "SV_SHARESECURITY",
    "SV_SHARES_PARMNUM",
    "SV_SHARINGVIOLATIONDELAY_PARMNUM",
    "SV_SHARINGVIOLATIONRETRIES_PARMNUM",
    "SV_SIZREQBUF_PARMNUM",
    "SV_SRVHEURISTICS_PARMNUM",
    "SV_THREADCOUNTADD_PARMNUM",
    "SV_THREADPRIORITY_PARMNUM",
    "SV_TIMESOURCE_PARMNUM",
    "SV_TYPE_AFP",
    "SV_TYPE_ALL",
    "SV_TYPE_ALTERNATE_XPORT",
    "SV_TYPE_BACKUP_BROWSER",
    "SV_TYPE_CLUSTER_NT",
    "SV_TYPE_CLUSTER_VS_NT",
    "SV_TYPE_DCE",
    "SV_TYPE_DFS",
    "SV_TYPE_DIALIN_SERVER",
    "SV_TYPE_DOMAIN_BAKCTRL",
    "SV_TYPE_DOMAIN_CTRL",
    "SV_TYPE_DOMAIN_ENUM",
    "SV_TYPE_DOMAIN_MASTER",
    "SV_TYPE_DOMAIN_MEMBER",
    "SV_TYPE_LOCAL_LIST_ONLY",
    "SV_TYPE_MASTER_BROWSER",
    "SV_TYPE_NOVELL",
    "SV_TYPE_NT",
    "SV_TYPE_PARMNUM",
    "SV_TYPE_POTENTIAL_BROWSER",
    "SV_TYPE_PRINTQ_SERVER",
    "SV_TYPE_SERVER",
    "SV_TYPE_SERVER_MFPN",
    "SV_TYPE_SERVER_NT",
    "SV_TYPE_SERVER_OSF",
    "SV_TYPE_SERVER_UNIX",
    "SV_TYPE_SERVER_VMS",
    "SV_TYPE_SQLSERVER",
    "SV_TYPE_TERMINALSERVER",
    "SV_TYPE_TIME_SOURCE",
    "SV_TYPE_WFW",
    "SV_TYPE_WINDOWS",
    "SV_TYPE_WORKSTATION",
    "SV_TYPE_XENIX_SERVER",
    "SV_ULIST_MTIME_PARMNUM",
    "SV_USERPATH_PARMNUM",
    "SV_USERSECURITY",
    "SV_USERS_PARMNUM",
    "SV_USERS_PER_LICENSE",
    "SV_VERSION_MAJOR_PARMNUM",
    "SV_VERSION_MINOR_PARMNUM",
    "SV_VISIBLE",
    "SV_XACTMEMSIZE_PARMNUM",
    "SW_AUTOPROF_LOAD_MASK",
    "SW_AUTOPROF_SAVE_MASK",
    "ServiceAccountPasswordGUID",
    "SetNetScheduleAccountInformation",
    "TIME_OF_DAY_INFO",
    "TITLE_SC_MESSAGE_BOX",
    "TRACE_NO_STDINFO",
    "TRACE_NO_SYNCH",
    "TRACE_USE_CONSOLE",
    "TRACE_USE_DATE",
    "TRACE_USE_FILE",
    "TRACE_USE_MASK",
    "TRACE_USE_MSEC",
    "TRANSPORT_INFO",
    "TRANSPORT_NAME_PARMNUM",
    "TRANSPORT_QUALITYOFSERVICE_PARMNUM",
    "TRANSPORT_TYPE",
    "TraceDeregisterA",
    "TraceDeregisterExA",
    "TraceDeregisterExW",
    "TraceDeregisterW",
    "TraceDumpExA",
    "TraceDumpExW",
    "TraceGetConsoleA",
    "TraceGetConsoleW",
    "TracePrintfA",
    "TracePrintfExA",
    "TracePrintfExW",
    "TracePrintfW",
    "TracePutsExA",
    "TracePutsExW",
    "TraceRegisterExA",
    "TraceRegisterExW",
    "TraceVprintfExA",
    "TraceVprintfExW",
    "UAS_ROLE_BACKUP",
    "UAS_ROLE_MEMBER",
    "UAS_ROLE_PRIMARY",
    "UAS_ROLE_STANDALONE",
    "UF_ACCOUNTDISABLE",
    "UF_DONT_EXPIRE_PASSWD",
    "UF_DONT_REQUIRE_PREAUTH",
    "UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED",
    "UF_HOMEDIR_REQUIRED",
    "UF_INTERDOMAIN_TRUST_ACCOUNT",
    "UF_LOCKOUT",
    "UF_MNS_LOGON_ACCOUNT",
    "UF_NORMAL_ACCOUNT",
    "UF_NOT_DELEGATED",
    "UF_NO_AUTH_DATA_REQUIRED",
    "UF_PARTIAL_SECRETS_ACCOUNT",
    "UF_PASSWD_CANT_CHANGE",
    "UF_PASSWD_NOTREQD",
    "UF_PASSWORD_EXPIRED",
    "UF_SCRIPT",
    "UF_SERVER_TRUST_ACCOUNT",
    "UF_SMARTCARD_REQUIRED",
    "UF_TEMP_DUPLICATE_ACCOUNT",
    "UF_TRUSTED_FOR_DELEGATION",
    "UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION",
    "UF_USE_AES_KEYS",
    "UF_USE_DES_KEY_ONLY",
    "UF_WORKSTATION_TRUST_ACCOUNT",
    "UNCLEN",
    "UNITS_PER_DAY",
    "UNLEN",
    "UPPER_GET_HINT_MASK",
    "UPPER_HINT_MASK",
    "USER_ACCOUNT_FLAGS",
    "USER_ACCT_EXPIRES_PARMNUM",
    "USER_AUTH_FLAGS_PARMNUM",
    "USER_CODE_PAGE_PARMNUM",
    "USER_COMMENT_PARMNUM",
    "USER_COUNTRY_CODE_PARMNUM",
    "USER_FLAGS_PARMNUM",
    "USER_FULL_NAME_PARMNUM",
    "USER_HOME_DIR_DRIVE_PARMNUM",
    "USER_HOME_DIR_PARMNUM",
    "USER_INFO_0",
    "USER_INFO_1",
    "USER_INFO_10",
    "USER_INFO_1003",
    "USER_INFO_1005",
    "USER_INFO_1006",
    "USER_INFO_1007",
    "USER_INFO_1008",
    "USER_INFO_1009",
    "USER_INFO_1010",
    "USER_INFO_1011",
    "USER_INFO_1012",
    "USER_INFO_1013",
    "USER_INFO_1014",
    "USER_INFO_1017",
    "USER_INFO_1018",
    "USER_INFO_1020",
    "USER_INFO_1023",
    "USER_INFO_1024",
    "USER_INFO_1025",
    "USER_INFO_1051",
    "USER_INFO_1052",
    "USER_INFO_1053",
    "USER_INFO_11",
    "USER_INFO_2",
    "USER_INFO_20",
    "USER_INFO_21",
    "USER_INFO_22",
    "USER_INFO_23",
    "USER_INFO_24",
    "USER_INFO_3",
    "USER_INFO_4",
    "USER_LAST_LOGOFF_PARMNUM",
    "USER_LAST_LOGON_PARMNUM",
    "USER_LOGON_HOURS_PARMNUM",
    "USER_LOGON_SERVER_PARMNUM",
    "USER_MAX_STORAGE_PARMNUM",
    "USER_MODALS_INFO_0",
    "USER_MODALS_INFO_1",
    "USER_MODALS_INFO_1001",
    "USER_MODALS_INFO_1002",
    "USER_MODALS_INFO_1003",
    "USER_MODALS_INFO_1004",
    "USER_MODALS_INFO_1005",
    "USER_MODALS_INFO_1006",
    "USER_MODALS_INFO_1007",
    "USER_MODALS_INFO_2",
    "USER_MODALS_INFO_3",
    "USER_MODALS_ROLES",
    "USER_NAME_PARMNUM",
    "USER_NUM_LOGONS_PARMNUM",
    "USER_OTHER_INFO",
    "USER_PAD_PW_COUNT_PARMNUM",
    "USER_PARMS_PARMNUM",
    "USER_PASSWORD_AGE_PARMNUM",
    "USER_PASSWORD_PARMNUM",
    "USER_PRIMARY_GROUP_PARMNUM",
    "USER_PRIV",
    "USER_PRIV_ADMIN",
    "USER_PRIV_GUEST",
    "USER_PRIV_MASK",
    "USER_PRIV_PARMNUM",
    "USER_PRIV_USER",
    "USER_PROFILE",
    "USER_PROFILE_PARMNUM",
    "USER_SCRIPT_PATH_PARMNUM",
    "USER_UNITS_PER_WEEK_PARMNUM",
    "USER_USR_COMMENT_PARMNUM",
    "USER_WORKSTATIONS_PARMNUM",
    "USE_ASGTYPE_PARMNUM",
    "USE_AUTHIDENTITY_PARMNUM",
    "USE_CHARDEV",
    "USE_CONN",
    "USE_DEFAULT_CREDENTIALS",
    "USE_DISCONN",
    "USE_DISKDEV",
    "USE_DOMAINNAME_PARMNUM",
    "USE_FLAGS_PARMNUM",
    "USE_FLAG_GLOBAL_MAPPING",
    "USE_FORCE",
    "USE_INFO_0",
    "USE_INFO_1",
    "USE_INFO_2",
    "USE_INFO_3",
    "USE_INFO_4",
    "USE_INFO_5",
    "USE_INFO_ASG_TYPE",
    "USE_IPC",
    "USE_LOCAL_PARMNUM",
    "USE_LOTS_OF_FORCE",
    "USE_NETERR",
    "USE_NOFORCE",
    "USE_OK",
    "USE_OPTIONS_PARMNUM",
    "USE_OPTION_DEFERRED_CONNECTION_PARAMETERS",
    "USE_OPTION_GENERIC",
    "USE_OPTION_PROPERTIES",
    "USE_OPTION_TRANSPORT_PARAMETERS",
    "USE_PASSWORD_PARMNUM",
    "USE_PAUSED",
    "USE_RECONN",
    "USE_REMOTE_PARMNUM",
    "USE_SD_PARMNUM",
    "USE_SESSLOST",
    "USE_SPECIFIC_TRANSPORT",
    "USE_SPOOLDEV",
    "USE_USERNAME_PARMNUM",
    "USE_WILDCARD",
    "UseTransportType_None",
    "UseTransportType_Quic",
    "UseTransportType_Wsk",
    "VALIDATED_LOGON",
    "VALID_LOGOFF",
    "WKSTA_BUFFERNAMEDPIPES_PARMNUM",
    "WKSTA_BUFFERREADONLYFILES_PARMNUM",
    "WKSTA_BUFFILESWITHDENYWRITE_PARMNUM",
    "WKSTA_CACHEFILETIMEOUT_PARMNUM",
    "WKSTA_CHARCOUNT_PARMNUM",
    "WKSTA_CHARTIME_PARMNUM",
    "WKSTA_CHARWAIT_PARMNUM",
    "WKSTA_COMPUTERNAME_PARMNUM",
    "WKSTA_DORMANTFILELIMIT_PARMNUM",
    "WKSTA_ERRLOGSZ_PARMNUM",
    "WKSTA_FORCECORECREATEMODE_PARMNUM",
    "WKSTA_INFO_100",
    "WKSTA_INFO_101",
    "WKSTA_INFO_1010",
    "WKSTA_INFO_1011",
    "WKSTA_INFO_1012",
    "WKSTA_INFO_1013",
    "WKSTA_INFO_1018",
    "WKSTA_INFO_102",
    "WKSTA_INFO_1023",
    "WKSTA_INFO_1027",
    "WKSTA_INFO_1028",
    "WKSTA_INFO_1032",
    "WKSTA_INFO_1033",
    "WKSTA_INFO_1041",
    "WKSTA_INFO_1042",
    "WKSTA_INFO_1043",
    "WKSTA_INFO_1044",
    "WKSTA_INFO_1045",
    "WKSTA_INFO_1046",
    "WKSTA_INFO_1047",
    "WKSTA_INFO_1048",
    "WKSTA_INFO_1049",
    "WKSTA_INFO_1050",
    "WKSTA_INFO_1051",
    "WKSTA_INFO_1052",
    "WKSTA_INFO_1053",
    "WKSTA_INFO_1054",
    "WKSTA_INFO_1055",
    "WKSTA_INFO_1056",
    "WKSTA_INFO_1057",
    "WKSTA_INFO_1058",
    "WKSTA_INFO_1059",
    "WKSTA_INFO_1060",
    "WKSTA_INFO_1061",
    "WKSTA_INFO_1062",
    "WKSTA_INFO_302",
    "WKSTA_INFO_402",
    "WKSTA_INFO_502",
    "WKSTA_KEEPCONN_PARMNUM",
    "WKSTA_KEEPSEARCH_PARMNUM",
    "WKSTA_LANGROUP_PARMNUM",
    "WKSTA_LANROOT_PARMNUM",
    "WKSTA_LOCKINCREMENT_PARMNUM",
    "WKSTA_LOCKMAXIMUM_PARMNUM",
    "WKSTA_LOCKQUOTA_PARMNUM",
    "WKSTA_LOGGED_ON_USERS_PARMNUM",
    "WKSTA_LOGON_DOMAIN_PARMNUM",
    "WKSTA_LOGON_SERVER_PARMNUM",
    "WKSTA_MAILSLOTS_PARMNUM",
    "WKSTA_MAXCMDS_PARMNUM",
    "WKSTA_MAXTHREADS_PARMNUM",
    "WKSTA_MAXWRKCACHE_PARMNUM",
    "WKSTA_NUMALERTS_PARMNUM",
    "WKSTA_NUMCHARBUF_PARMNUM",
    "WKSTA_NUMDGRAMBUF_PARMNUM",
    "WKSTA_NUMSERVICES_PARMNUM",
    "WKSTA_NUMWORKBUF_PARMNUM",
    "WKSTA_OTH_DOMAINS_PARMNUM",
    "WKSTA_PIPEINCREMENT_PARMNUM",
    "WKSTA_PIPEMAXIMUM_PARMNUM",
    "WKSTA_PLATFORM_ID_PARMNUM",
    "WKSTA_PRINTBUFTIME_PARMNUM",
    "WKSTA_READAHEADTHRUPUT_PARMNUM",
    "WKSTA_SESSTIMEOUT_PARMNUM",
    "WKSTA_SIZCHARBUF_PARMNUM",
    "WKSTA_SIZERROR_PARMNUM",
    "WKSTA_SIZWORKBUF_PARMNUM",
    "WKSTA_TRANSPORT_INFO_0",
    "WKSTA_USE512BYTESMAXTRANSFER_PARMNUM",
    "WKSTA_USECLOSEBEHIND_PARMNUM",
    "WKSTA_USEENCRYPTION_PARMNUM",
    "WKSTA_USELOCKANDREADANDUNLOCK_PARMNUM",
    "WKSTA_USEOPPORTUNISTICLOCKING_PARMNUM",
    "WKSTA_USERAWREAD_PARMNUM",
    "WKSTA_USERAWWRITE_PARMNUM",
    "WKSTA_USER_INFO_0",
    "WKSTA_USER_INFO_1",
    "WKSTA_USER_INFO_1101",
    "WKSTA_USEUNLOCKBEHIND_PARMNUM",
    "WKSTA_USEWRITERAWWITHDATA_PARMNUM",
    "WKSTA_UTILIZENTCACHING_PARMNUM",
    "WKSTA_VER_MAJOR_PARMNUM",
    "WKSTA_VER_MINOR_PARMNUM",
    "WKSTA_WRKHEURISTICS_PARMNUM",
    "WORKERFUNCTION",
    "WORKSTATION_DISPLAY_NAME",
    "WZC_PROFILE_API_ERROR_FAILED_TO_LOAD_SCHEMA",
    "WZC_PROFILE_API_ERROR_FAILED_TO_LOAD_XML",
    "WZC_PROFILE_API_ERROR_INTERNAL",
    "WZC_PROFILE_API_ERROR_NOT_SUPPORTED",
    "WZC_PROFILE_API_ERROR_XML_VALIDATION_FAILED",
    "WZC_PROFILE_CONFIG_ERROR_1X_NOT_ALLOWED",
    "WZC_PROFILE_CONFIG_ERROR_1X_NOT_ALLOWED_KEY_REQUIRED",
    "WZC_PROFILE_CONFIG_ERROR_1X_NOT_ENABLED_KEY_PROVIDED",
    "WZC_PROFILE_CONFIG_ERROR_EAP_METHOD_NOT_APPLICABLE",
    "WZC_PROFILE_CONFIG_ERROR_EAP_METHOD_REQUIRED",
    "WZC_PROFILE_CONFIG_ERROR_INVALID_AUTH_FOR_CONNECTION_TYPE",
    "WZC_PROFILE_CONFIG_ERROR_INVALID_ENCRYPTION_FOR_AUTHMODE",
    "WZC_PROFILE_CONFIG_ERROR_KEY_INDEX_NOT_APPLICABLE",
    "WZC_PROFILE_CONFIG_ERROR_KEY_INDEX_REQUIRED",
    "WZC_PROFILE_CONFIG_ERROR_KEY_REQUIRED",
    "WZC_PROFILE_CONFIG_ERROR_WPA_ENCRYPTION_NOT_SUPPORTED",
    "WZC_PROFILE_CONFIG_ERROR_WPA_NOT_SUPPORTED",
    "WZC_PROFILE_SET_ERROR_DUPLICATE_NETWORK",
    "WZC_PROFILE_SET_ERROR_MEMORY_ALLOCATION",
    "WZC_PROFILE_SET_ERROR_READING_1X_CONFIG",
    "WZC_PROFILE_SET_ERROR_WRITING_1X_CONFIG",
    "WZC_PROFILE_SET_ERROR_WRITING_WZC_CFG",
    "WZC_PROFILE_SUCCESS",
    "WZC_PROFILE_XML_ERROR_1X_ENABLED",
    "WZC_PROFILE_XML_ERROR_AUTHENTICATION",
    "WZC_PROFILE_XML_ERROR_BAD_KEY_INDEX",
    "WZC_PROFILE_XML_ERROR_BAD_NETWORK_KEY",
    "WZC_PROFILE_XML_ERROR_BAD_SSID",
    "WZC_PROFILE_XML_ERROR_BAD_VERSION",
    "WZC_PROFILE_XML_ERROR_CONNECTION_TYPE",
    "WZC_PROFILE_XML_ERROR_EAP_METHOD",
    "WZC_PROFILE_XML_ERROR_ENCRYPTION",
    "WZC_PROFILE_XML_ERROR_KEY_INDEX_RANGE",
    "WZC_PROFILE_XML_ERROR_KEY_PROVIDED_AUTOMATICALLY",
    "WZC_PROFILE_XML_ERROR_NO_VERSION",
    "WZC_PROFILE_XML_ERROR_SSID_NOT_FOUND",
    "WZC_PROFILE_XML_ERROR_UNSUPPORTED_VERSION",
]
