from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
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
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class ACCESS_INFO_0(Structure):
    acc0_resource_name: win32more.Foundation.PWSTR
class ACCESS_INFO_1(Structure):
    acc1_resource_name: win32more.Foundation.PWSTR
    acc1_attr: UInt32
    acc1_count: UInt32
class ACCESS_INFO_1002(Structure):
    acc1002_attr: UInt32
class ACCESS_LIST(Structure):
    acl_ugname: win32more.Foundation.PWSTR
    acl_access: UInt32
class ADMIN_OTHER_INFO(Structure):
    alrtad_errcode: UInt32
    alrtad_numstrings: UInt32
class AE_ACCLIM(Structure):
    ae_al_compname: UInt32
    ae_al_username: UInt32
    ae_al_resname: UInt32
    ae_al_limit: UInt32
class AE_ACLMOD(Structure):
    ae_am_compname: UInt32
    ae_am_username: UInt32
    ae_am_resname: UInt32
    ae_am_action: UInt32
    ae_am_datalen: UInt32
class AE_CLOSEFILE(Structure):
    ae_cf_compname: UInt32
    ae_cf_username: UInt32
    ae_cf_resname: UInt32
    ae_cf_fileid: UInt32
    ae_cf_duration: UInt32
    ae_cf_reason: UInt32
class AE_CONNREJ(Structure):
    ae_cr_compname: UInt32
    ae_cr_username: UInt32
    ae_cr_netname: UInt32
    ae_cr_reason: UInt32
class AE_CONNSTART(Structure):
    ae_ct_compname: UInt32
    ae_ct_username: UInt32
    ae_ct_netname: UInt32
    ae_ct_connid: UInt32
class AE_CONNSTOP(Structure):
    ae_cp_compname: UInt32
    ae_cp_username: UInt32
    ae_cp_netname: UInt32
    ae_cp_connid: UInt32
    ae_cp_reason: UInt32
class AE_GENERIC(Structure):
    ae_ge_msgfile: UInt32
    ae_ge_msgnum: UInt32
    ae_ge_params: UInt32
    ae_ge_param1: UInt32
    ae_ge_param2: UInt32
    ae_ge_param3: UInt32
    ae_ge_param4: UInt32
    ae_ge_param5: UInt32
    ae_ge_param6: UInt32
    ae_ge_param7: UInt32
    ae_ge_param8: UInt32
    ae_ge_param9: UInt32
class AE_LOCKOUT(Structure):
    ae_lk_compname: UInt32
    ae_lk_username: UInt32
    ae_lk_action: UInt32
    ae_lk_bad_pw_count: UInt32
class AE_NETLOGOFF(Structure):
    ae_nf_compname: UInt32
    ae_nf_username: UInt32
    ae_nf_reserved1: UInt32
    ae_nf_reserved2: UInt32
class AE_NETLOGON(Structure):
    ae_no_compname: UInt32
    ae_no_username: UInt32
    ae_no_privilege: UInt32
    ae_no_authflags: UInt32
class AE_RESACCESS(Structure):
    ae_ra_compname: UInt32
    ae_ra_username: UInt32
    ae_ra_resname: UInt32
    ae_ra_operation: UInt32
    ae_ra_returncode: UInt32
    ae_ra_restype: UInt32
    ae_ra_fileid: UInt32
class AE_RESACCESSREJ(Structure):
    ae_rr_compname: UInt32
    ae_rr_username: UInt32
    ae_rr_resname: UInt32
    ae_rr_operation: UInt32
class AE_SERVICESTAT(Structure):
    ae_ss_compname: UInt32
    ae_ss_username: UInt32
    ae_ss_svcname: UInt32
    ae_ss_status: UInt32
    ae_ss_code: UInt32
    ae_ss_text: UInt32
    ae_ss_returnval: UInt32
class AE_SESSLOGOFF(Structure):
    ae_sf_compname: UInt32
    ae_sf_username: UInt32
    ae_sf_reason: UInt32
class AE_SESSLOGON(Structure):
    ae_so_compname: UInt32
    ae_so_username: UInt32
    ae_so_privilege: UInt32
class AE_SESSPWERR(Structure):
    ae_sp_compname: UInt32
    ae_sp_username: UInt32
class AE_SRVSTATUS(Structure):
    ae_sv_status: UInt32
class AE_UASMOD(Structure):
    ae_um_compname: UInt32
    ae_um_username: UInt32
    ae_um_resname: UInt32
    ae_um_rectype: UInt32
    ae_um_action: UInt32
    ae_um_datalen: UInt32
AF_OP = UInt32
AF_OP_PRINT: AF_OP = 1
AF_OP_COMM: AF_OP = 2
AF_OP_SERVER: AF_OP = 4
AF_OP_ACCOUNTS: AF_OP = 8
NERR_BASE: UInt32 = 2100
NERR_PasswordExpired: UInt32 = 2242
CNLEN: UInt32 = 15
LM20_CNLEN: UInt32 = 15
DNLEN: UInt32 = 15
LM20_DNLEN: UInt32 = 15
UNCLEN: UInt32 = 17
LM20_UNCLEN: UInt32 = 17
LM20_NNLEN: UInt32 = 12
SNLEN: UInt32 = 80
LM20_SNLEN: UInt32 = 15
STXTLEN: UInt32 = 256
LM20_STXTLEN: UInt32 = 63
PATHLEN: UInt32 = 256
LM20_PATHLEN: UInt32 = 256
DEVLEN: UInt32 = 80
LM20_DEVLEN: UInt32 = 8
EVLEN: UInt32 = 16
UNLEN: UInt32 = 256
LM20_UNLEN: UInt32 = 20
GNLEN: UInt32 = 256
LM20_GNLEN: UInt32 = 20
PWLEN: UInt32 = 256
LM20_PWLEN: UInt32 = 14
SHPWLEN: UInt32 = 8
CLTYPE_LEN: UInt32 = 12
MAXCOMMENTSZ: UInt32 = 256
LM20_MAXCOMMENTSZ: UInt32 = 48
QNLEN: UInt32 = 80
LM20_QNLEN: UInt32 = 12
ALERTSZ: UInt32 = 128
NETBIOS_NAME_LEN: UInt32 = 16
MAX_PREFERRED_LENGTH: UInt32 = 4294967295
CRYPT_KEY_LEN: UInt32 = 7
CRYPT_TXT_LEN: UInt32 = 8
ENCRYPTED_PWLEN: UInt32 = 16
SESSION_PWLEN: UInt32 = 24
SESSION_CRYPT_KLEN: UInt32 = 21
PARMNUM_ALL: UInt32 = 0
PARM_ERROR_UNKNOWN: UInt32 = 4294967295
PARM_ERROR_NONE: UInt32 = 0
PARMNUM_BASE_INFOLEVEL: UInt32 = 1000
MESSAGE_FILENAME: String = 'NETMSG'
OS2MSG_FILENAME: String = 'BASE'
HELP_MSG_FILENAME: String = 'NETH'
BACKUP_MSG_FILENAME: String = 'BAK.MSG'
PLATFORM_ID_DOS: UInt32 = 300
PLATFORM_ID_OS2: UInt32 = 400
PLATFORM_ID_NT: UInt32 = 500
PLATFORM_ID_OSF: UInt32 = 600
PLATFORM_ID_VMS: UInt32 = 700
MIN_LANMAN_MESSAGE_ID: UInt32 = 2100
MAX_LANMAN_MESSAGE_ID: UInt32 = 5899
NERR_Success: UInt32 = 0
NERR_NetNotStarted: UInt32 = 2102
NERR_UnknownServer: UInt32 = 2103
NERR_ShareMem: UInt32 = 2104
NERR_NoNetworkResource: UInt32 = 2105
NERR_RemoteOnly: UInt32 = 2106
NERR_DevNotRedirected: UInt32 = 2107
NERR_ServerNotStarted: UInt32 = 2114
NERR_ItemNotFound: UInt32 = 2115
NERR_UnknownDevDir: UInt32 = 2116
NERR_RedirectedPath: UInt32 = 2117
NERR_DuplicateShare: UInt32 = 2118
NERR_NoRoom: UInt32 = 2119
NERR_TooManyItems: UInt32 = 2121
NERR_InvalidMaxUsers: UInt32 = 2122
NERR_BufTooSmall: UInt32 = 2123
NERR_RemoteErr: UInt32 = 2127
NERR_LanmanIniError: UInt32 = 2131
NERR_NetworkError: UInt32 = 2136
NERR_WkstaInconsistentState: UInt32 = 2137
NERR_WkstaNotStarted: UInt32 = 2138
NERR_BrowserNotStarted: UInt32 = 2139
NERR_InternalError: UInt32 = 2140
NERR_BadTransactConfig: UInt32 = 2141
NERR_InvalidAPI: UInt32 = 2142
NERR_BadEventName: UInt32 = 2143
NERR_DupNameReboot: UInt32 = 2144
NERR_CfgCompNotFound: UInt32 = 2146
NERR_CfgParamNotFound: UInt32 = 2147
NERR_LineTooLong: UInt32 = 2149
NERR_QNotFound: UInt32 = 2150
NERR_JobNotFound: UInt32 = 2151
NERR_DestNotFound: UInt32 = 2152
NERR_DestExists: UInt32 = 2153
NERR_QExists: UInt32 = 2154
NERR_QNoRoom: UInt32 = 2155
NERR_JobNoRoom: UInt32 = 2156
NERR_DestNoRoom: UInt32 = 2157
NERR_DestIdle: UInt32 = 2158
NERR_DestInvalidOp: UInt32 = 2159
NERR_ProcNoRespond: UInt32 = 2160
NERR_SpoolerNotLoaded: UInt32 = 2161
NERR_DestInvalidState: UInt32 = 2162
NERR_QInvalidState: UInt32 = 2163
NERR_JobInvalidState: UInt32 = 2164
NERR_SpoolNoMemory: UInt32 = 2165
NERR_DriverNotFound: UInt32 = 2166
NERR_DataTypeInvalid: UInt32 = 2167
NERR_ProcNotFound: UInt32 = 2168
NERR_ServiceTableLocked: UInt32 = 2180
NERR_ServiceTableFull: UInt32 = 2181
NERR_ServiceInstalled: UInt32 = 2182
NERR_ServiceEntryLocked: UInt32 = 2183
NERR_ServiceNotInstalled: UInt32 = 2184
NERR_BadServiceName: UInt32 = 2185
NERR_ServiceCtlTimeout: UInt32 = 2186
NERR_ServiceCtlBusy: UInt32 = 2187
NERR_BadServiceProgName: UInt32 = 2188
NERR_ServiceNotCtrl: UInt32 = 2189
NERR_ServiceKillProc: UInt32 = 2190
NERR_ServiceCtlNotValid: UInt32 = 2191
NERR_NotInDispatchTbl: UInt32 = 2192
NERR_BadControlRecv: UInt32 = 2193
NERR_ServiceNotStarting: UInt32 = 2194
NERR_AlreadyLoggedOn: UInt32 = 2200
NERR_NotLoggedOn: UInt32 = 2201
NERR_BadUsername: UInt32 = 2202
NERR_BadPassword: UInt32 = 2203
NERR_UnableToAddName_W: UInt32 = 2204
NERR_UnableToAddName_F: UInt32 = 2205
NERR_UnableToDelName_W: UInt32 = 2206
NERR_UnableToDelName_F: UInt32 = 2207
NERR_LogonsPaused: UInt32 = 2209
NERR_LogonServerConflict: UInt32 = 2210
NERR_LogonNoUserPath: UInt32 = 2211
NERR_LogonScriptError: UInt32 = 2212
NERR_StandaloneLogon: UInt32 = 2214
NERR_LogonServerNotFound: UInt32 = 2215
NERR_LogonDomainExists: UInt32 = 2216
NERR_NonValidatedLogon: UInt32 = 2217
NERR_ACFNotFound: UInt32 = 2219
NERR_GroupNotFound: UInt32 = 2220
NERR_UserNotFound: UInt32 = 2221
NERR_ResourceNotFound: UInt32 = 2222
NERR_GroupExists: UInt32 = 2223
NERR_UserExists: UInt32 = 2224
NERR_ResourceExists: UInt32 = 2225
NERR_NotPrimary: UInt32 = 2226
NERR_ACFNotLoaded: UInt32 = 2227
NERR_ACFNoRoom: UInt32 = 2228
NERR_ACFFileIOFail: UInt32 = 2229
NERR_ACFTooManyLists: UInt32 = 2230
NERR_UserLogon: UInt32 = 2231
NERR_ACFNoParent: UInt32 = 2232
NERR_CanNotGrowSegment: UInt32 = 2233
NERR_SpeGroupOp: UInt32 = 2234
NERR_NotInCache: UInt32 = 2235
NERR_UserInGroup: UInt32 = 2236
NERR_UserNotInGroup: UInt32 = 2237
NERR_AccountUndefined: UInt32 = 2238
NERR_AccountExpired: UInt32 = 2239
NERR_InvalidWorkstation: UInt32 = 2240
NERR_InvalidLogonHours: UInt32 = 2241
NERR_PasswordCantChange: UInt32 = 2243
NERR_PasswordHistConflict: UInt32 = 2244
NERR_PasswordTooShort: UInt32 = 2245
NERR_PasswordTooRecent: UInt32 = 2246
NERR_InvalidDatabase: UInt32 = 2247
NERR_DatabaseUpToDate: UInt32 = 2248
NERR_SyncRequired: UInt32 = 2249
NERR_UseNotFound: UInt32 = 2250
NERR_BadAsgType: UInt32 = 2251
NERR_DeviceIsShared: UInt32 = 2252
NERR_SameAsComputerName: UInt32 = 2253
NERR_NoComputerName: UInt32 = 2270
NERR_MsgAlreadyStarted: UInt32 = 2271
NERR_MsgInitFailed: UInt32 = 2272
NERR_NameNotFound: UInt32 = 2273
NERR_AlreadyForwarded: UInt32 = 2274
NERR_AddForwarded: UInt32 = 2275
NERR_AlreadyExists: UInt32 = 2276
NERR_TooManyNames: UInt32 = 2277
NERR_DelComputerName: UInt32 = 2278
NERR_LocalForward: UInt32 = 2279
NERR_GrpMsgProcessor: UInt32 = 2280
NERR_PausedRemote: UInt32 = 2281
NERR_BadReceive: UInt32 = 2282
NERR_NameInUse: UInt32 = 2283
NERR_MsgNotStarted: UInt32 = 2284
NERR_NotLocalName: UInt32 = 2285
NERR_NoForwardName: UInt32 = 2286
NERR_RemoteFull: UInt32 = 2287
NERR_NameNotForwarded: UInt32 = 2288
NERR_TruncatedBroadcast: UInt32 = 2289
NERR_InvalidDevice: UInt32 = 2294
NERR_WriteFault: UInt32 = 2295
NERR_DuplicateName: UInt32 = 2297
NERR_DeleteLater: UInt32 = 2298
NERR_IncompleteDel: UInt32 = 2299
NERR_MultipleNets: UInt32 = 2300
NERR_NetNameNotFound: UInt32 = 2310
NERR_DeviceNotShared: UInt32 = 2311
NERR_ClientNameNotFound: UInt32 = 2312
NERR_FileIdNotFound: UInt32 = 2314
NERR_ExecFailure: UInt32 = 2315
NERR_TmpFile: UInt32 = 2316
NERR_TooMuchData: UInt32 = 2317
NERR_DeviceShareConflict: UInt32 = 2318
NERR_BrowserTableIncomplete: UInt32 = 2319
NERR_NotLocalDomain: UInt32 = 2320
NERR_IsDfsShare: UInt32 = 2321
NERR_DevInvalidOpCode: UInt32 = 2331
NERR_DevNotFound: UInt32 = 2332
NERR_DevNotOpen: UInt32 = 2333
NERR_BadQueueDevString: UInt32 = 2334
NERR_BadQueuePriority: UInt32 = 2335
NERR_NoCommDevs: UInt32 = 2337
NERR_QueueNotFound: UInt32 = 2338
NERR_BadDevString: UInt32 = 2340
NERR_BadDev: UInt32 = 2341
NERR_InUseBySpooler: UInt32 = 2342
NERR_CommDevInUse: UInt32 = 2343
NERR_InvalidComputer: UInt32 = 2351
NERR_MaxLenExceeded: UInt32 = 2354
NERR_BadComponent: UInt32 = 2356
NERR_CantType: UInt32 = 2357
NERR_TooManyEntries: UInt32 = 2362
NERR_ProfileFileTooBig: UInt32 = 2370
NERR_ProfileOffset: UInt32 = 2371
NERR_ProfileCleanup: UInt32 = 2372
NERR_ProfileUnknownCmd: UInt32 = 2373
NERR_ProfileLoadErr: UInt32 = 2374
NERR_ProfileSaveErr: UInt32 = 2375
NERR_LogOverflow: UInt32 = 2377
NERR_LogFileChanged: UInt32 = 2378
NERR_LogFileCorrupt: UInt32 = 2379
NERR_SourceIsDir: UInt32 = 2380
NERR_BadSource: UInt32 = 2381
NERR_BadDest: UInt32 = 2382
NERR_DifferentServers: UInt32 = 2383
NERR_RunSrvPaused: UInt32 = 2385
NERR_ErrCommRunSrv: UInt32 = 2389
NERR_ErrorExecingGhost: UInt32 = 2391
NERR_ShareNotFound: UInt32 = 2392
NERR_InvalidLana: UInt32 = 2400
NERR_OpenFiles: UInt32 = 2401
NERR_ActiveConns: UInt32 = 2402
NERR_BadPasswordCore: UInt32 = 2403
NERR_DevInUse: UInt32 = 2404
NERR_LocalDrive: UInt32 = 2405
NERR_AlertExists: UInt32 = 2430
NERR_TooManyAlerts: UInt32 = 2431
NERR_NoSuchAlert: UInt32 = 2432
NERR_BadRecipient: UInt32 = 2433
NERR_AcctLimitExceeded: UInt32 = 2434
NERR_InvalidLogSeek: UInt32 = 2440
NERR_BadUasConfig: UInt32 = 2450
NERR_InvalidUASOp: UInt32 = 2451
NERR_LastAdmin: UInt32 = 2452
NERR_DCNotFound: UInt32 = 2453
NERR_LogonTrackingError: UInt32 = 2454
NERR_NetlogonNotStarted: UInt32 = 2455
NERR_CanNotGrowUASFile: UInt32 = 2456
NERR_TimeDiffAtDC: UInt32 = 2457
NERR_PasswordMismatch: UInt32 = 2458
NERR_NoSuchServer: UInt32 = 2460
NERR_NoSuchSession: UInt32 = 2461
NERR_NoSuchConnection: UInt32 = 2462
NERR_TooManyServers: UInt32 = 2463
NERR_TooManySessions: UInt32 = 2464
NERR_TooManyConnections: UInt32 = 2465
NERR_TooManyFiles: UInt32 = 2466
NERR_NoAlternateServers: UInt32 = 2467
NERR_TryDownLevel: UInt32 = 2470
NERR_UPSDriverNotStarted: UInt32 = 2480
NERR_UPSInvalidConfig: UInt32 = 2481
NERR_UPSInvalidCommPort: UInt32 = 2482
NERR_UPSSignalAsserted: UInt32 = 2483
NERR_UPSShutdownFailed: UInt32 = 2484
NERR_BadDosRetCode: UInt32 = 2500
NERR_ProgNeedsExtraMem: UInt32 = 2501
NERR_BadDosFunction: UInt32 = 2502
NERR_RemoteBootFailed: UInt32 = 2503
NERR_BadFileCheckSum: UInt32 = 2504
NERR_NoRplBootSystem: UInt32 = 2505
NERR_RplLoadrNetBiosErr: UInt32 = 2506
NERR_RplLoadrDiskErr: UInt32 = 2507
NERR_ImageParamErr: UInt32 = 2508
NERR_TooManyImageParams: UInt32 = 2509
NERR_NonDosFloppyUsed: UInt32 = 2510
NERR_RplBootRestart: UInt32 = 2511
NERR_RplSrvrCallFailed: UInt32 = 2512
NERR_CantConnectRplSrvr: UInt32 = 2513
NERR_CantOpenImageFile: UInt32 = 2514
NERR_CallingRplSrvr: UInt32 = 2515
NERR_StartingRplBoot: UInt32 = 2516
NERR_RplBootServiceTerm: UInt32 = 2517
NERR_RplBootStartFailed: UInt32 = 2518
NERR_RPL_CONNECTED: UInt32 = 2519
NERR_BrowserConfiguredToNotRun: UInt32 = 2550
NERR_RplNoAdaptersStarted: UInt32 = 2610
NERR_RplBadRegistry: UInt32 = 2611
NERR_RplBadDatabase: UInt32 = 2612
NERR_RplRplfilesShare: UInt32 = 2613
NERR_RplNotRplServer: UInt32 = 2614
NERR_RplCannotEnum: UInt32 = 2615
NERR_RplWkstaInfoCorrupted: UInt32 = 2616
NERR_RplWkstaNotFound: UInt32 = 2617
NERR_RplWkstaNameUnavailable: UInt32 = 2618
NERR_RplProfileInfoCorrupted: UInt32 = 2619
NERR_RplProfileNotFound: UInt32 = 2620
NERR_RplProfileNameUnavailable: UInt32 = 2621
NERR_RplProfileNotEmpty: UInt32 = 2622
NERR_RplConfigInfoCorrupted: UInt32 = 2623
NERR_RplConfigNotFound: UInt32 = 2624
NERR_RplAdapterInfoCorrupted: UInt32 = 2625
NERR_RplInternal: UInt32 = 2626
NERR_RplVendorInfoCorrupted: UInt32 = 2627
NERR_RplBootInfoCorrupted: UInt32 = 2628
NERR_RplWkstaNeedsUserAcct: UInt32 = 2629
NERR_RplNeedsRPLUSERAcct: UInt32 = 2630
NERR_RplBootNotFound: UInt32 = 2631
NERR_RplIncompatibleProfile: UInt32 = 2632
NERR_RplAdapterNameUnavailable: UInt32 = 2633
NERR_RplConfigNotEmpty: UInt32 = 2634
NERR_RplBootInUse: UInt32 = 2635
NERR_RplBackupDatabase: UInt32 = 2636
NERR_RplAdapterNotFound: UInt32 = 2637
NERR_RplVendorNotFound: UInt32 = 2638
NERR_RplVendorNameUnavailable: UInt32 = 2639
NERR_RplBootNameUnavailable: UInt32 = 2640
NERR_RplConfigNameUnavailable: UInt32 = 2641
NERR_DfsInternalCorruption: UInt32 = 2660
NERR_DfsVolumeDataCorrupt: UInt32 = 2661
NERR_DfsNoSuchVolume: UInt32 = 2662
NERR_DfsVolumeAlreadyExists: UInt32 = 2663
NERR_DfsAlreadyShared: UInt32 = 2664
NERR_DfsNoSuchShare: UInt32 = 2665
NERR_DfsNotALeafVolume: UInt32 = 2666
NERR_DfsLeafVolume: UInt32 = 2667
NERR_DfsVolumeHasMultipleServers: UInt32 = 2668
NERR_DfsCantCreateJunctionPoint: UInt32 = 2669
NERR_DfsServerNotDfsAware: UInt32 = 2670
NERR_DfsBadRenamePath: UInt32 = 2671
NERR_DfsVolumeIsOffline: UInt32 = 2672
NERR_DfsNoSuchServer: UInt32 = 2673
NERR_DfsCyclicalName: UInt32 = 2674
NERR_DfsNotSupportedInServerDfs: UInt32 = 2675
NERR_DfsDuplicateService: UInt32 = 2676
NERR_DfsCantRemoveLastServerShare: UInt32 = 2677
NERR_DfsVolumeIsInterDfs: UInt32 = 2678
NERR_DfsInconsistent: UInt32 = 2679
NERR_DfsServerUpgraded: UInt32 = 2680
NERR_DfsDataIsIdentical: UInt32 = 2681
NERR_DfsCantRemoveDfsRoot: UInt32 = 2682
NERR_DfsChildOrParentInDfs: UInt32 = 2683
NERR_DfsInternalError: UInt32 = 2690
NERR_SetupAlreadyJoined: UInt32 = 2691
NERR_SetupNotJoined: UInt32 = 2692
NERR_SetupDomainController: UInt32 = 2693
NERR_DefaultJoinRequired: UInt32 = 2694
NERR_InvalidWorkgroupName: UInt32 = 2695
NERR_NameUsesIncompatibleCodePage: UInt32 = 2696
NERR_ComputerAccountNotFound: UInt32 = 2697
NERR_PersonalSku: UInt32 = 2698
NERR_SetupCheckDNSConfig: UInt32 = 2699
NERR_AlreadyCloudDomainJoined: UInt32 = 2700
NERR_PasswordMustChange: UInt32 = 2701
NERR_AccountLockedOut: UInt32 = 2702
NERR_PasswordTooLong: UInt32 = 2703
NERR_PasswordNotComplexEnough: UInt32 = 2704
NERR_PasswordFilterError: UInt32 = 2705
NERR_NoOfflineJoinInfo: UInt32 = 2709
NERR_BadOfflineJoinInfo: UInt32 = 2710
NERR_CantCreateJoinInfo: UInt32 = 2711
NERR_BadDomainJoinInfo: UInt32 = 2712
NERR_JoinPerformedMustRestart: UInt32 = 2713
NERR_NoJoinPending: UInt32 = 2714
NERR_ValuesNotSet: UInt32 = 2715
NERR_CantVerifyHostname: UInt32 = 2716
NERR_CantLoadOfflineHive: UInt32 = 2717
NERR_ConnectionInsecure: UInt32 = 2718
NERR_ProvisioningBlobUnsupported: UInt32 = 2719
NERR_DS8DCRequired: UInt32 = 2720
NERR_LDAPCapableDCRequired: UInt32 = 2721
NERR_DS8DCNotFound: UInt32 = 2722
NERR_TargetVersionUnsupported: UInt32 = 2723
NERR_InvalidMachineNameForJoin: UInt32 = 2724
NERR_DS9DCNotFound: UInt32 = 2725
NERR_PlainTextSecretsRequired: UInt32 = 2726
NERR_CannotUnjoinAadDomain: UInt32 = 2727
MAX_NERR: UInt32 = 2999
UF_TEMP_DUPLICATE_ACCOUNT: UInt32 = 256
UF_NORMAL_ACCOUNT: UInt32 = 512
UF_INTERDOMAIN_TRUST_ACCOUNT: UInt32 = 2048
UF_WORKSTATION_TRUST_ACCOUNT: UInt32 = 4096
UF_SERVER_TRUST_ACCOUNT: UInt32 = 8192
UF_MNS_LOGON_ACCOUNT: UInt32 = 131072
UF_NO_AUTH_DATA_REQUIRED: UInt32 = 33554432
UF_PARTIAL_SECRETS_ACCOUNT: UInt32 = 67108864
UF_USE_AES_KEYS: UInt32 = 134217728
LG_INCLUDE_INDIRECT: UInt32 = 1
USER_NAME_PARMNUM: UInt32 = 1
USER_PASSWORD_PARMNUM: UInt32 = 3
USER_PASSWORD_AGE_PARMNUM: UInt32 = 4
USER_PRIV_PARMNUM: UInt32 = 5
USER_HOME_DIR_PARMNUM: UInt32 = 6
USER_COMMENT_PARMNUM: UInt32 = 7
USER_FLAGS_PARMNUM: UInt32 = 8
USER_SCRIPT_PATH_PARMNUM: UInt32 = 9
USER_AUTH_FLAGS_PARMNUM: UInt32 = 10
USER_FULL_NAME_PARMNUM: UInt32 = 11
USER_USR_COMMENT_PARMNUM: UInt32 = 12
USER_PARMS_PARMNUM: UInt32 = 13
USER_WORKSTATIONS_PARMNUM: UInt32 = 14
USER_LAST_LOGON_PARMNUM: UInt32 = 15
USER_LAST_LOGOFF_PARMNUM: UInt32 = 16
USER_ACCT_EXPIRES_PARMNUM: UInt32 = 17
USER_MAX_STORAGE_PARMNUM: UInt32 = 18
USER_UNITS_PER_WEEK_PARMNUM: UInt32 = 19
USER_LOGON_HOURS_PARMNUM: UInt32 = 20
USER_PAD_PW_COUNT_PARMNUM: UInt32 = 21
USER_NUM_LOGONS_PARMNUM: UInt32 = 22
USER_LOGON_SERVER_PARMNUM: UInt32 = 23
USER_COUNTRY_CODE_PARMNUM: UInt32 = 24
USER_CODE_PAGE_PARMNUM: UInt32 = 25
USER_PRIMARY_GROUP_PARMNUM: UInt32 = 51
USER_PROFILE: UInt32 = 52
USER_PROFILE_PARMNUM: UInt32 = 52
USER_HOME_DIR_DRIVE_PARMNUM: UInt32 = 53
NULL_USERSETINFO_PASSWD: String = '              '
UNITS_PER_DAY: UInt32 = 24
USER_PRIV_MASK: UInt32 = 3
MAX_PASSWD_LEN: UInt32 = 256
DEF_MIN_PWLEN: UInt32 = 6
DEF_PWUNIQUENESS: UInt32 = 5
DEF_MAX_PWHIST: UInt32 = 8
DEF_MAX_BADPW: UInt32 = 0
VALIDATED_LOGON: UInt32 = 0
PASSWORD_EXPIRED: UInt32 = 2
NON_VALIDATED_LOGON: UInt32 = 3
VALID_LOGOFF: UInt32 = 1
MODALS_MIN_PASSWD_LEN_PARMNUM: UInt32 = 1
MODALS_MAX_PASSWD_AGE_PARMNUM: UInt32 = 2
MODALS_MIN_PASSWD_AGE_PARMNUM: UInt32 = 3
MODALS_FORCE_LOGOFF_PARMNUM: UInt32 = 4
MODALS_PASSWD_HIST_LEN_PARMNUM: UInt32 = 5
MODALS_ROLE_PARMNUM: UInt32 = 6
MODALS_PRIMARY_PARMNUM: UInt32 = 7
MODALS_DOMAIN_NAME_PARMNUM: UInt32 = 8
MODALS_DOMAIN_ID_PARMNUM: UInt32 = 9
MODALS_LOCKOUT_DURATION_PARMNUM: UInt32 = 10
MODALS_LOCKOUT_OBSERVATION_WINDOW_PARMNUM: UInt32 = 11
MODALS_LOCKOUT_THRESHOLD_PARMNUM: UInt32 = 12
GROUPIDMASK: UInt32 = 32768
GROUP_SPECIALGRP_USERS: String = 'USERS'
GROUP_SPECIALGRP_ADMINS: String = 'ADMINS'
GROUP_SPECIALGRP_GUESTS: String = 'GUESTS'
GROUP_SPECIALGRP_LOCAL: String = 'LOCAL'
GROUP_ALL_PARMNUM: UInt32 = 0
GROUP_NAME_PARMNUM: UInt32 = 1
GROUP_COMMENT_PARMNUM: UInt32 = 2
GROUP_ATTRIBUTES_PARMNUM: UInt32 = 3
LOCALGROUP_NAME_PARMNUM: UInt32 = 1
LOCALGROUP_COMMENT_PARMNUM: UInt32 = 2
MAXPERMENTRIES: UInt32 = 64
ACCESS_NONE: UInt32 = 0
ACCESS_GROUP: UInt32 = 32768
ACCESS_AUDIT: UInt32 = 1
ACCESS_SUCCESS_OPEN: UInt32 = 16
ACCESS_SUCCESS_WRITE: UInt32 = 32
ACCESS_SUCCESS_DELETE: UInt32 = 64
ACCESS_SUCCESS_ACL: UInt32 = 128
ACCESS_SUCCESS_MASK: UInt32 = 240
ACCESS_FAIL_OPEN: UInt32 = 256
ACCESS_FAIL_WRITE: UInt32 = 512
ACCESS_FAIL_DELETE: UInt32 = 1024
ACCESS_FAIL_ACL: UInt32 = 2048
ACCESS_FAIL_MASK: UInt32 = 3840
ACCESS_FAIL_SHIFT: UInt32 = 4
ACCESS_RESOURCE_NAME_PARMNUM: UInt32 = 1
ACCESS_ATTR_PARMNUM: UInt32 = 2
ACCESS_COUNT_PARMNUM: UInt32 = 3
ACCESS_ACCESS_LIST_PARMNUM: UInt32 = 4
ACCESS_LETTERS: String = 'RWCXDAP         '
NET_VALIDATE_PASSWORD_LAST_SET: UInt32 = 1
NET_VALIDATE_BAD_PASSWORD_TIME: UInt32 = 2
NET_VALIDATE_LOCKOUT_TIME: UInt32 = 4
NET_VALIDATE_BAD_PASSWORD_COUNT: UInt32 = 8
NET_VALIDATE_PASSWORD_HISTORY_LENGTH: UInt32 = 16
NET_VALIDATE_PASSWORD_HISTORY: UInt32 = 32
NETLOGON_CONTROL_QUERY: UInt32 = 1
NETLOGON_CONTROL_REPLICATE: UInt32 = 2
NETLOGON_CONTROL_SYNCHRONIZE: UInt32 = 3
NETLOGON_CONTROL_PDC_REPLICATE: UInt32 = 4
NETLOGON_CONTROL_REDISCOVER: UInt32 = 5
NETLOGON_CONTROL_TC_QUERY: UInt32 = 6
NETLOGON_CONTROL_TRANSPORT_NOTIFY: UInt32 = 7
NETLOGON_CONTROL_FIND_USER: UInt32 = 8
NETLOGON_CONTROL_CHANGE_PASSWORD: UInt32 = 9
NETLOGON_CONTROL_TC_VERIFY: UInt32 = 10
NETLOGON_CONTROL_FORCE_DNS_REG: UInt32 = 11
NETLOGON_CONTROL_QUERY_DNS_REG: UInt32 = 12
NETLOGON_CONTROL_QUERY_ENC_TYPES: UInt32 = 13
NETLOGON_CONTROL_UNLOAD_NETLOGON_DLL: UInt32 = 65531
NETLOGON_CONTROL_BACKUP_CHANGE_LOG: UInt32 = 65532
NETLOGON_CONTROL_TRUNCATE_LOG: UInt32 = 65533
NETLOGON_CONTROL_SET_DBFLAG: UInt32 = 65534
NETLOGON_CONTROL_BREAKPOINT: UInt32 = 65535
NETLOGON_REPLICATION_NEEDED: UInt32 = 1
NETLOGON_REPLICATION_IN_PROGRESS: UInt32 = 2
NETLOGON_FULL_SYNC_REPLICATION: UInt32 = 4
NETLOGON_REDO_NEEDED: UInt32 = 8
NETLOGON_HAS_IP: UInt32 = 16
NETLOGON_HAS_TIMESERV: UInt32 = 32
NETLOGON_DNS_UPDATE_FAILURE: UInt32 = 64
NETLOGON_VERIFY_STATUS_RETURNED: UInt32 = 128
SERVICE_ACCOUNT_PASSWORD: String = '_SA_{262E99C9-6160-4871-ACEC-4E61736B6F21}'
SERVICE_ACCOUNT_SECRET_PREFIX: String = '_SC_{262E99C9-6160-4871-ACEC-4E61736B6F21}_'
ServiceAccountPasswordGUID: Guid = Guid('262e99c9-6160-4871-ac-ec-4e-61-73-6b-6f-21')
SERVICE_ACCOUNT_FLAG_LINK_TO_HOST_ONLY: Int32 = 1
SERVICE_ACCOUNT_FLAG_ADD_AGAINST_RODC: Int32 = 2
SERVICE_ACCOUNT_FLAG_UNLINK_FROM_HOST_ONLY: Int32 = 1
SERVICE_ACCOUNT_FLAG_REMOVE_OFFLINE: Int32 = 2
ALERTER_MAILSLOT: String = '\\\\.\\MAILSLOT\\Alerter'
ALERT_PRINT_EVENT: String = 'PRINTING'
ALERT_MESSAGE_EVENT: String = 'MESSAGE'
ALERT_ERRORLOG_EVENT: String = 'ERRORLOG'
ALERT_ADMIN_EVENT: String = 'ADMIN'
ALERT_USER_EVENT: String = 'USER'
PRJOB_QSTATUS: UInt32 = 3
PRJOB_DEVSTATUS: UInt32 = 508
PRJOB_COMPLETE: UInt32 = 4
PRJOB_INTERV: UInt32 = 8
PRJOB_ERROR: UInt32 = 16
PRJOB_DESTOFFLINE: UInt32 = 32
PRJOB_DESTPAUSED: UInt32 = 64
PRJOB_NOTIFY: UInt32 = 128
PRJOB_DESTNOPAPER: UInt32 = 256
PRJOB_DELETED: UInt32 = 32768
PRJOB_QS_QUEUED: UInt32 = 0
PRJOB_QS_PAUSED: UInt32 = 1
PRJOB_QS_SPOOLING: UInt32 = 2
PRJOB_QS_PRINTING: UInt32 = 3
JOB_RUN_PERIODICALLY: UInt32 = 1
JOB_EXEC_ERROR: UInt32 = 2
JOB_RUNS_TODAY: UInt32 = 4
JOB_ADD_CURRENT_DATE: UInt32 = 8
JOB_NONINTERACTIVE: UInt32 = 16
LOGFLAGS_FORWARD: UInt32 = 0
LOGFLAGS_BACKWARD: UInt32 = 1
LOGFLAGS_SEEK: UInt32 = 2
ACTION_LOCKOUT: UInt32 = 0
ACTION_ADMINUNLOCK: UInt32 = 1
AE_SRVSTATUS_CONSTANT: UInt32 = 0
AE_SESSLOGON_CONSTANT: UInt32 = 1
AE_SESSLOGOFF_CONSTANT: UInt32 = 2
AE_SESSPWERR_CONSTANT: UInt32 = 3
AE_CONNSTART_CONSTANT: UInt32 = 4
AE_CONNSTOP_CONSTANT: UInt32 = 5
AE_CONNREJ_CONSTANT: UInt32 = 6
AE_RESACCESS_CONSTANT: UInt32 = 7
AE_RESACCESSREJ_CONSTANT: UInt32 = 8
AE_CLOSEFILE_CONSTANT: UInt32 = 9
AE_SERVICESTAT_CONSTANT: UInt32 = 11
AE_ACLMOD_CONSTANT: UInt32 = 12
AE_UASMOD_CONSTANT: UInt32 = 13
AE_NETLOGON_CONSTANT: UInt32 = 14
AE_NETLOGOFF_CONSTANT: UInt32 = 15
AE_NETLOGDENIED: UInt32 = 16
AE_ACCLIMITEXCD: UInt32 = 17
AE_RESACCESS2: UInt32 = 18
AE_ACLMODFAIL: UInt32 = 19
AE_LOCKOUT_CONSTANT: UInt32 = 20
AE_GENERIC_TYPE: UInt32 = 21
AE_SRVSTART: UInt32 = 0
AE_SRVPAUSED: UInt32 = 1
AE_SRVCONT: UInt32 = 2
AE_SRVSTOP: UInt32 = 3
AE_GUEST: UInt32 = 0
AE_USER: UInt32 = 1
AE_ADMIN: UInt32 = 2
AE_NORMAL: UInt32 = 0
AE_USERLIMIT: UInt32 = 0
AE_GENERAL: UInt32 = 0
AE_ERROR: UInt32 = 1
AE_SESSDIS: UInt32 = 1
AE_BADPW: UInt32 = 1
AE_AUTODIS: UInt32 = 2
AE_UNSHARE: UInt32 = 2
AE_ADMINPRIVREQD: UInt32 = 2
AE_ADMINDIS: UInt32 = 3
AE_NOACCESSPERM: UInt32 = 3
AE_ACCRESTRICT: UInt32 = 4
AE_NORMAL_CLOSE: UInt32 = 0
AE_SES_CLOSE: UInt32 = 1
AE_ADMIN_CLOSE: UInt32 = 2
AE_LIM_UNKNOWN: UInt32 = 0
AE_LIM_LOGONHOURS: UInt32 = 1
AE_LIM_EXPIRED: UInt32 = 2
AE_LIM_INVAL_WKSTA: UInt32 = 3
AE_LIM_DISABLED: UInt32 = 4
AE_LIM_DELETED: UInt32 = 5
AE_MOD: UInt32 = 0
AE_DELETE: UInt32 = 1
AE_ADD: UInt32 = 2
AE_UAS_USER: UInt32 = 0
AE_UAS_GROUP: UInt32 = 1
AE_UAS_MODALS: UInt32 = 2
SVAUD_SERVICE: UInt32 = 1
SVAUD_GOODSESSLOGON: UInt32 = 6
SVAUD_BADSESSLOGON: UInt32 = 24
SVAUD_GOODNETLOGON: UInt32 = 96
SVAUD_BADNETLOGON: UInt32 = 384
SVAUD_GOODUSE: UInt32 = 1536
SVAUD_BADUSE: UInt32 = 6144
SVAUD_USERLIST: UInt32 = 8192
SVAUD_PERMISSIONS: UInt32 = 16384
SVAUD_RESOURCE: UInt32 = 32768
SVAUD_LOGONLIM: UInt32 = 65536
AA_AUDIT_ALL: UInt32 = 1
AA_A_OWNER: UInt32 = 4
AA_CLOSE: UInt32 = 8
AA_S_OPEN: UInt32 = 16
AA_S_WRITE: UInt32 = 32
AA_S_CREATE: UInt32 = 32
AA_S_DELETE: UInt32 = 64
AA_S_ACL: UInt32 = 128
AA_F_OPEN: UInt32 = 256
AA_F_WRITE: UInt32 = 512
AA_F_CREATE: UInt32 = 512
AA_F_DELETE: UInt32 = 1024
AA_F_ACL: UInt32 = 2048
AA_A_OPEN: UInt32 = 4096
AA_A_WRITE: UInt32 = 8192
AA_A_CREATE: UInt32 = 8192
AA_A_DELETE: UInt32 = 16384
AA_A_ACL: UInt32 = 32768
ERRLOG_BASE: UInt32 = 3100
NELOG_Internal_Error: UInt32 = 3100
NELOG_Resource_Shortage: UInt32 = 3101
NELOG_Unable_To_Lock_Segment: UInt32 = 3102
NELOG_Unable_To_Unlock_Segment: UInt32 = 3103
NELOG_Uninstall_Service: UInt32 = 3104
NELOG_Init_Exec_Fail: UInt32 = 3105
NELOG_Ncb_Error: UInt32 = 3106
NELOG_Net_Not_Started: UInt32 = 3107
NELOG_Ioctl_Error: UInt32 = 3108
NELOG_System_Semaphore: UInt32 = 3109
NELOG_Init_OpenCreate_Err: UInt32 = 3110
NELOG_NetBios: UInt32 = 3111
NELOG_SMB_Illegal: UInt32 = 3112
NELOG_Service_Fail: UInt32 = 3113
NELOG_Entries_Lost: UInt32 = 3114
NELOG_Init_Seg_Overflow: UInt32 = 3120
NELOG_Srv_No_Mem_Grow: UInt32 = 3121
NELOG_Access_File_Bad: UInt32 = 3122
NELOG_Srvnet_Not_Started: UInt32 = 3123
NELOG_Init_Chardev_Err: UInt32 = 3124
NELOG_Remote_API: UInt32 = 3125
NELOG_Ncb_TooManyErr: UInt32 = 3126
NELOG_Mailslot_err: UInt32 = 3127
NELOG_ReleaseMem_Alert: UInt32 = 3128
NELOG_AT_cannot_write: UInt32 = 3129
NELOG_Cant_Make_Msg_File: UInt32 = 3130
NELOG_Exec_Netservr_NoMem: UInt32 = 3131
NELOG_Server_Lock_Failure: UInt32 = 3132
NELOG_Msg_Shutdown: UInt32 = 3140
NELOG_Msg_Sem_Shutdown: UInt32 = 3141
NELOG_Msg_Log_Err: UInt32 = 3150
NELOG_VIO_POPUP_ERR: UInt32 = 3151
NELOG_Msg_Unexpected_SMB_Type: UInt32 = 3152
NELOG_Wksta_Infoseg: UInt32 = 3160
NELOG_Wksta_Compname: UInt32 = 3161
NELOG_Wksta_BiosThreadFailure: UInt32 = 3162
NELOG_Wksta_IniSeg: UInt32 = 3163
NELOG_Wksta_HostTab_Full: UInt32 = 3164
NELOG_Wksta_Bad_Mailslot_SMB: UInt32 = 3165
NELOG_Wksta_UASInit: UInt32 = 3166
NELOG_Wksta_SSIRelogon: UInt32 = 3167
NELOG_Build_Name: UInt32 = 3170
NELOG_Name_Expansion: UInt32 = 3171
NELOG_Message_Send: UInt32 = 3172
NELOG_Mail_Slt_Err: UInt32 = 3173
NELOG_AT_cannot_read: UInt32 = 3174
NELOG_AT_sched_err: UInt32 = 3175
NELOG_AT_schedule_file_created: UInt32 = 3176
NELOG_Srvnet_NB_Open: UInt32 = 3177
NELOG_AT_Exec_Err: UInt32 = 3178
NELOG_Lazy_Write_Err: UInt32 = 3180
NELOG_HotFix: UInt32 = 3181
NELOG_HardErr_From_Server: UInt32 = 3182
NELOG_LocalSecFail1: UInt32 = 3183
NELOG_LocalSecFail2: UInt32 = 3184
NELOG_LocalSecFail3: UInt32 = 3185
NELOG_LocalSecGeneralFail: UInt32 = 3186
NELOG_NetWkSta_Internal_Error: UInt32 = 3190
NELOG_NetWkSta_No_Resource: UInt32 = 3191
NELOG_NetWkSta_SMB_Err: UInt32 = 3192
NELOG_NetWkSta_VC_Err: UInt32 = 3193
NELOG_NetWkSta_Stuck_VC_Err: UInt32 = 3194
NELOG_NetWkSta_NCB_Err: UInt32 = 3195
NELOG_NetWkSta_Write_Behind_Err: UInt32 = 3196
NELOG_NetWkSta_Reset_Err: UInt32 = 3197
NELOG_NetWkSta_Too_Many: UInt32 = 3198
NELOG_Srv_Thread_Failure: UInt32 = 3204
NELOG_Srv_Close_Failure: UInt32 = 3205
NELOG_ReplUserCurDir: UInt32 = 3206
NELOG_ReplCannotMasterDir: UInt32 = 3207
NELOG_ReplUpdateError: UInt32 = 3208
NELOG_ReplLostMaster: UInt32 = 3209
NELOG_NetlogonAuthDCFail: UInt32 = 3210
NELOG_ReplLogonFailed: UInt32 = 3211
NELOG_ReplNetErr: UInt32 = 3212
NELOG_ReplMaxFiles: UInt32 = 3213
NELOG_ReplMaxTreeDepth: UInt32 = 3214
NELOG_ReplBadMsg: UInt32 = 3215
NELOG_ReplSysErr: UInt32 = 3216
NELOG_ReplUserLoged: UInt32 = 3217
NELOG_ReplBadImport: UInt32 = 3218
NELOG_ReplBadExport: UInt32 = 3219
NELOG_ReplSignalFileErr: UInt32 = 3220
NELOG_DiskFT: UInt32 = 3221
NELOG_ReplAccessDenied: UInt32 = 3222
NELOG_NetlogonFailedPrimary: UInt32 = 3223
NELOG_NetlogonPasswdSetFailed: UInt32 = 3224
NELOG_NetlogonTrackingError: UInt32 = 3225
NELOG_NetlogonSyncError: UInt32 = 3226
NELOG_NetlogonRequireSignOrSealError: UInt32 = 3227
NELOG_UPS_PowerOut: UInt32 = 3230
NELOG_UPS_Shutdown: UInt32 = 3231
NELOG_UPS_CmdFileError: UInt32 = 3232
NELOG_UPS_CannotOpenDriver: UInt32 = 3233
NELOG_UPS_PowerBack: UInt32 = 3234
NELOG_UPS_CmdFileConfig: UInt32 = 3235
NELOG_UPS_CmdFileExec: UInt32 = 3236
NELOG_Missing_Parameter: UInt32 = 3250
NELOG_Invalid_Config_Line: UInt32 = 3251
NELOG_Invalid_Config_File: UInt32 = 3252
NELOG_File_Changed: UInt32 = 3253
NELOG_Files_Dont_Fit: UInt32 = 3254
NELOG_Wrong_DLL_Version: UInt32 = 3255
NELOG_Error_in_DLL: UInt32 = 3256
NELOG_System_Error: UInt32 = 3257
NELOG_FT_ErrLog_Too_Large: UInt32 = 3258
NELOG_FT_Update_In_Progress: UInt32 = 3259
NELOG_Joined_Domain: UInt32 = 3260
NELOG_Joined_Workgroup: UInt32 = 3261
NELOG_OEM_Code: UInt32 = 3299
ERRLOG2_BASE: UInt32 = 5700
NELOG_NetlogonSSIInitError: UInt32 = 5700
NELOG_NetlogonFailedToUpdateTrustList: UInt32 = 5701
NELOG_NetlogonFailedToAddRpcInterface: UInt32 = 5702
NELOG_NetlogonFailedToReadMailslot: UInt32 = 5703
NELOG_NetlogonFailedToRegisterSC: UInt32 = 5704
NELOG_NetlogonChangeLogCorrupt: UInt32 = 5705
NELOG_NetlogonFailedToCreateShare: UInt32 = 5706
NELOG_NetlogonDownLevelLogonFailed: UInt32 = 5707
NELOG_NetlogonDownLevelLogoffFailed: UInt32 = 5708
NELOG_NetlogonNTLogonFailed: UInt32 = 5709
NELOG_NetlogonNTLogoffFailed: UInt32 = 5710
NELOG_NetlogonPartialSyncCallSuccess: UInt32 = 5711
NELOG_NetlogonPartialSyncCallFailed: UInt32 = 5712
NELOG_NetlogonFullSyncCallSuccess: UInt32 = 5713
NELOG_NetlogonFullSyncCallFailed: UInt32 = 5714
NELOG_NetlogonPartialSyncSuccess: UInt32 = 5715
NELOG_NetlogonPartialSyncFailed: UInt32 = 5716
NELOG_NetlogonFullSyncSuccess: UInt32 = 5717
NELOG_NetlogonFullSyncFailed: UInt32 = 5718
NELOG_NetlogonAuthNoDomainController: UInt32 = 5719
NELOG_NetlogonAuthNoTrustLsaSecret: UInt32 = 5720
NELOG_NetlogonAuthNoTrustSamAccount: UInt32 = 5721
NELOG_NetlogonServerAuthFailed: UInt32 = 5722
NELOG_NetlogonServerAuthNoTrustSamAccount: UInt32 = 5723
NELOG_FailedToRegisterSC: UInt32 = 5724
NELOG_FailedToSetServiceStatus: UInt32 = 5725
NELOG_FailedToGetComputerName: UInt32 = 5726
NELOG_DriverNotLoaded: UInt32 = 5727
NELOG_NoTranportLoaded: UInt32 = 5728
NELOG_NetlogonFailedDomainDelta: UInt32 = 5729
NELOG_NetlogonFailedGlobalGroupDelta: UInt32 = 5730
NELOG_NetlogonFailedLocalGroupDelta: UInt32 = 5731
NELOG_NetlogonFailedUserDelta: UInt32 = 5732
NELOG_NetlogonFailedPolicyDelta: UInt32 = 5733
NELOG_NetlogonFailedTrustedDomainDelta: UInt32 = 5734
NELOG_NetlogonFailedAccountDelta: UInt32 = 5735
NELOG_NetlogonFailedSecretDelta: UInt32 = 5736
NELOG_NetlogonSystemError: UInt32 = 5737
NELOG_NetlogonDuplicateMachineAccounts: UInt32 = 5738
NELOG_NetlogonTooManyGlobalGroups: UInt32 = 5739
NELOG_NetlogonBrowserDriver: UInt32 = 5740
NELOG_NetlogonAddNameFailure: UInt32 = 5741
NELOG_RplMessages: UInt32 = 5742
NELOG_RplXnsBoot: UInt32 = 5743
NELOG_RplSystem: UInt32 = 5744
NELOG_RplWkstaTimeout: UInt32 = 5745
NELOG_RplWkstaFileOpen: UInt32 = 5746
NELOG_RplWkstaFileRead: UInt32 = 5747
NELOG_RplWkstaMemory: UInt32 = 5748
NELOG_RplWkstaFileChecksum: UInt32 = 5749
NELOG_RplWkstaFileLineCount: UInt32 = 5750
NELOG_RplWkstaBbcFile: UInt32 = 5751
NELOG_RplWkstaFileSize: UInt32 = 5752
NELOG_RplWkstaInternal: UInt32 = 5753
NELOG_RplWkstaWrongVersion: UInt32 = 5754
NELOG_RplWkstaNetwork: UInt32 = 5755
NELOG_RplAdapterResource: UInt32 = 5756
NELOG_RplFileCopy: UInt32 = 5757
NELOG_RplFileDelete: UInt32 = 5758
NELOG_RplFilePerms: UInt32 = 5759
NELOG_RplCheckConfigs: UInt32 = 5760
NELOG_RplCreateProfiles: UInt32 = 5761
NELOG_RplRegistry: UInt32 = 5762
NELOG_RplReplaceRPLDISK: UInt32 = 5763
NELOG_RplCheckSecurity: UInt32 = 5764
NELOG_RplBackupDatabase: UInt32 = 5765
NELOG_RplInitDatabase: UInt32 = 5766
NELOG_RplRestoreDatabaseFailure: UInt32 = 5767
NELOG_RplRestoreDatabaseSuccess: UInt32 = 5768
NELOG_RplInitRestoredDatabase: UInt32 = 5769
NELOG_NetlogonSessionTypeWrong: UInt32 = 5770
NELOG_RplUpgradeDBTo40: UInt32 = 5771
NELOG_NetlogonLanmanBdcsNotAllowed: UInt32 = 5772
NELOG_NetlogonNoDynamicDns: UInt32 = 5773
NELOG_NetlogonDynamicDnsRegisterFailure: UInt32 = 5774
NELOG_NetlogonDynamicDnsDeregisterFailure: UInt32 = 5775
NELOG_NetlogonFailedFileCreate: UInt32 = 5776
NELOG_NetlogonGetSubnetToSite: UInt32 = 5777
NELOG_NetlogonNoSiteForClient: UInt32 = 5778
NELOG_NetlogonBadSiteName: UInt32 = 5779
NELOG_NetlogonBadSubnetName: UInt32 = 5780
NELOG_NetlogonDynamicDnsServerFailure: UInt32 = 5781
NELOG_NetlogonDynamicDnsFailure: UInt32 = 5782
NELOG_NetlogonRpcCallCancelled: UInt32 = 5783
NELOG_NetlogonDcSiteCovered: UInt32 = 5784
NELOG_NetlogonDcSiteNotCovered: UInt32 = 5785
NELOG_NetlogonGcSiteCovered: UInt32 = 5786
NELOG_NetlogonGcSiteNotCovered: UInt32 = 5787
NELOG_NetlogonFailedSpnUpdate: UInt32 = 5788
NELOG_NetlogonFailedDnsHostNameUpdate: UInt32 = 5789
NELOG_NetlogonAuthNoUplevelDomainController: UInt32 = 5790
NELOG_NetlogonAuthDomainDowngraded: UInt32 = 5791
NELOG_NetlogonNdncSiteCovered: UInt32 = 5792
NELOG_NetlogonNdncSiteNotCovered: UInt32 = 5793
NELOG_NetlogonDcOldSiteCovered: UInt32 = 5794
NELOG_NetlogonDcSiteNotCoveredAuto: UInt32 = 5795
NELOG_NetlogonGcOldSiteCovered: UInt32 = 5796
NELOG_NetlogonGcSiteNotCoveredAuto: UInt32 = 5797
NELOG_NetlogonNdncOldSiteCovered: UInt32 = 5798
NELOG_NetlogonNdncSiteNotCoveredAuto: UInt32 = 5799
NELOG_NetlogonSpnMultipleSamAccountNames: UInt32 = 5800
NELOG_NetlogonSpnCrackNamesFailure: UInt32 = 5801
NELOG_NetlogonNoAddressToSiteMapping: UInt32 = 5802
NELOG_NetlogonInvalidGenericParameterValue: UInt32 = 5803
NELOG_NetlogonInvalidDwordParameterValue: UInt32 = 5804
NELOG_NetlogonServerAuthFailedNoAccount: UInt32 = 5805
NELOG_NetlogonNoDynamicDnsManual: UInt32 = 5806
NELOG_NetlogonNoSiteForClients: UInt32 = 5807
NELOG_NetlogonDnsDeregAborted: UInt32 = 5808
NELOG_NetlogonRpcPortRequestFailure: UInt32 = 5809
NELOG_NetlogonPartialSiteMappingForClients: UInt32 = 5810
NELOG_NetlogonRemoteDynamicDnsRegisterFailure: UInt32 = 5811
NELOG_NetlogonRemoteDynamicDnsDeregisterFailure: UInt32 = 5812
NELOG_NetlogonRejectedRemoteDynamicDnsRegister: UInt32 = 5813
NELOG_NetlogonRejectedRemoteDynamicDnsDeregister: UInt32 = 5814
NELOG_NetlogonRemoteDynamicDnsUpdateRequestFailure: UInt32 = 5815
NELOG_NetlogonUserValidationReqInitialTimeOut: UInt32 = 5816
NELOG_NetlogonUserValidationReqRecurringTimeOut: UInt32 = 5817
NELOG_NetlogonUserValidationReqWaitInitialWarning: UInt32 = 5818
NELOG_NetlogonUserValidationReqWaitRecurringWarning: UInt32 = 5819
NELOG_NetlogonFailedToAddAuthzRpcInterface: UInt32 = 5820
NELOG_NetLogonFailedToInitializeAuthzRm: UInt32 = 5821
NELOG_NetLogonFailedToInitializeRPCSD: UInt32 = 5822
NELOG_NetlogonMachinePasswdSetSucceeded: UInt32 = 5823
NELOG_NetlogonMsaPasswdSetSucceeded: UInt32 = 5824
NELOG_NetlogonDnsHostNameLowerCasingFailed: UInt32 = 5825
NETLOG_NetlogonNonWindowsSupportsSecureRpc: UInt32 = 5826
NETLOG_NetlogonUnsecureRpcClient: UInt32 = 5827
NETLOG_NetlogonUnsecureRpcTrust: UInt32 = 5828
NETLOG_NetlogonUnsecuredRpcMachineTemporarilyAllowed: UInt32 = 5829
NETLOG_NetlogonUnsecureRpcMachineAllowedBySsdl: UInt32 = 5830
NETLOG_NetlogonUnsecureRpcTrustAllowedBySsdl: UInt32 = 5831
NETSETUP_ACCT_DELETE: UInt32 = 4
NETSETUP_DNS_NAME_CHANGES_ONLY: UInt32 = 4096
NETSETUP_INSTALL_INVOCATION: UInt32 = 262144
NETSETUP_ALT_SAMACCOUNTNAME: UInt32 = 131072
NET_IGNORE_UNSUPPORTED_FLAGS: UInt32 = 1
NETSETUP_PROVISION_PERSISTENTSITE: UInt32 = 32
NETSETUP_PROVISION_CHECK_PWD_ONLY: UInt32 = 2147483648
NETSETUP_PROVISIONING_PARAMS_WIN8_VERSION: UInt32 = 1
NETSETUP_PROVISIONING_PARAMS_CURRENT_VERSION: UInt32 = 2
MSGNAME_NOT_FORWARDED: UInt32 = 0
MSGNAME_FORWARDED_TO: UInt32 = 4
MSGNAME_FORWARDED_FROM: UInt32 = 16
SUPPORTS_ANY: Int32 = -1
NO_PERMISSION_REQUIRED: UInt32 = 1
ALLOCATE_RESPONSE: UInt32 = 2
USE_SPECIFIC_TRANSPORT: UInt32 = 2147483648
SV_PLATFORM_ID_OS2: UInt32 = 400
SV_PLATFORM_ID_NT: UInt32 = 500
MAJOR_VERSION_MASK: UInt32 = 15
SV_NODISC: Int32 = -1
SV_PLATFORM_ID_PARMNUM: UInt32 = 101
SV_NAME_PARMNUM: UInt32 = 102
SV_VERSION_MAJOR_PARMNUM: UInt32 = 103
SV_VERSION_MINOR_PARMNUM: UInt32 = 104
SV_TYPE_PARMNUM: UInt32 = 105
SV_COMMENT_PARMNUM: UInt32 = 5
SV_USERS_PARMNUM: UInt32 = 107
SV_DISC_PARMNUM: UInt32 = 10
SV_HIDDEN_PARMNUM: UInt32 = 16
SV_ANNOUNCE_PARMNUM: UInt32 = 17
SV_ANNDELTA_PARMNUM: UInt32 = 18
SV_USERPATH_PARMNUM: UInt32 = 112
SV_ULIST_MTIME_PARMNUM: UInt32 = 401
SV_GLIST_MTIME_PARMNUM: UInt32 = 402
SV_ALIST_MTIME_PARMNUM: UInt32 = 403
SV_ALERTS_PARMNUM: UInt32 = 11
SV_SECURITY_PARMNUM: UInt32 = 405
SV_NUMADMIN_PARMNUM: UInt32 = 406
SV_LANMASK_PARMNUM: UInt32 = 407
SV_GUESTACC_PARMNUM: UInt32 = 408
SV_CHDEVQ_PARMNUM: UInt32 = 410
SV_CHDEVJOBS_PARMNUM: UInt32 = 411
SV_CONNECTIONS_PARMNUM: UInt32 = 412
SV_SHARES_PARMNUM: UInt32 = 413
SV_OPENFILES_PARMNUM: UInt32 = 414
SV_SESSREQS_PARMNUM: UInt32 = 417
SV_ACTIVELOCKS_PARMNUM: UInt32 = 419
SV_NUMREQBUF_PARMNUM: UInt32 = 420
SV_NUMBIGBUF_PARMNUM: UInt32 = 422
SV_NUMFILETASKS_PARMNUM: UInt32 = 423
SV_ALERTSCHED_PARMNUM: UInt32 = 37
SV_ERRORALERT_PARMNUM: UInt32 = 38
SV_LOGONALERT_PARMNUM: UInt32 = 39
SV_ACCESSALERT_PARMNUM: UInt32 = 40
SV_DISKALERT_PARMNUM: UInt32 = 41
SV_NETIOALERT_PARMNUM: UInt32 = 42
SV_MAXAUDITSZ_PARMNUM: UInt32 = 43
SV_SRVHEURISTICS_PARMNUM: UInt32 = 431
SV_SESSOPENS_PARMNUM: UInt32 = 501
SV_SESSVCS_PARMNUM: UInt32 = 502
SV_OPENSEARCH_PARMNUM: UInt32 = 503
SV_SIZREQBUF_PARMNUM: UInt32 = 504
SV_INITWORKITEMS_PARMNUM: UInt32 = 505
SV_MAXWORKITEMS_PARMNUM: UInt32 = 506
SV_RAWWORKITEMS_PARMNUM: UInt32 = 507
SV_IRPSTACKSIZE_PARMNUM: UInt32 = 508
SV_MAXRAWBUFLEN_PARMNUM: UInt32 = 509
SV_SESSUSERS_PARMNUM: UInt32 = 510
SV_SESSCONNS_PARMNUM: UInt32 = 511
SV_MAXNONPAGEDMEMORYUSAGE_PARMNUM: UInt32 = 512
SV_MAXPAGEDMEMORYUSAGE_PARMNUM: UInt32 = 513
SV_ENABLESOFTCOMPAT_PARMNUM: UInt32 = 514
SV_ENABLEFORCEDLOGOFF_PARMNUM: UInt32 = 515
SV_TIMESOURCE_PARMNUM: UInt32 = 516
SV_ACCEPTDOWNLEVELAPIS_PARMNUM: UInt32 = 517
SV_LMANNOUNCE_PARMNUM: UInt32 = 518
SV_DOMAIN_PARMNUM: UInt32 = 519
SV_MAXCOPYREADLEN_PARMNUM: UInt32 = 520
SV_MAXCOPYWRITELEN_PARMNUM: UInt32 = 521
SV_MINKEEPSEARCH_PARMNUM: UInt32 = 522
SV_MAXKEEPSEARCH_PARMNUM: UInt32 = 523
SV_MINKEEPCOMPLSEARCH_PARMNUM: UInt32 = 524
SV_MAXKEEPCOMPLSEARCH_PARMNUM: UInt32 = 525
SV_THREADCOUNTADD_PARMNUM: UInt32 = 526
SV_NUMBLOCKTHREADS_PARMNUM: UInt32 = 527
SV_SCAVTIMEOUT_PARMNUM: UInt32 = 528
SV_MINRCVQUEUE_PARMNUM: UInt32 = 529
SV_MINFREEWORKITEMS_PARMNUM: UInt32 = 530
SV_XACTMEMSIZE_PARMNUM: UInt32 = 531
SV_THREADPRIORITY_PARMNUM: UInt32 = 532
SV_MAXMPXCT_PARMNUM: UInt32 = 533
SV_OPLOCKBREAKWAIT_PARMNUM: UInt32 = 534
SV_OPLOCKBREAKRESPONSEWAIT_PARMNUM: UInt32 = 535
SV_ENABLEOPLOCKS_PARMNUM: UInt32 = 536
SV_ENABLEOPLOCKFORCECLOSE_PARMNUM: UInt32 = 537
SV_ENABLEFCBOPENS_PARMNUM: UInt32 = 538
SV_ENABLERAW_PARMNUM: UInt32 = 539
SV_ENABLESHAREDNETDRIVES_PARMNUM: UInt32 = 540
SV_MINFREECONNECTIONS_PARMNUM: UInt32 = 541
SV_MAXFREECONNECTIONS_PARMNUM: UInt32 = 542
SV_INITSESSTABLE_PARMNUM: UInt32 = 543
SV_INITCONNTABLE_PARMNUM: UInt32 = 544
SV_INITFILETABLE_PARMNUM: UInt32 = 545
SV_INITSEARCHTABLE_PARMNUM: UInt32 = 546
SV_ALERTSCHEDULE_PARMNUM: UInt32 = 547
SV_ERRORTHRESHOLD_PARMNUM: UInt32 = 548
SV_NETWORKERRORTHRESHOLD_PARMNUM: UInt32 = 549
SV_DISKSPACETHRESHOLD_PARMNUM: UInt32 = 550
SV_MAXLINKDELAY_PARMNUM: UInt32 = 552
SV_MINLINKTHROUGHPUT_PARMNUM: UInt32 = 553
SV_LINKINFOVALIDTIME_PARMNUM: UInt32 = 554
SV_SCAVQOSINFOUPDATETIME_PARMNUM: UInt32 = 555
SV_MAXWORKITEMIDLETIME_PARMNUM: UInt32 = 556
SV_MAXRAWWORKITEMS_PARMNUM: UInt32 = 557
SV_PRODUCTTYPE_PARMNUM: UInt32 = 560
SV_SERVERSIZE_PARMNUM: UInt32 = 561
SV_CONNECTIONLESSAUTODISC_PARMNUM: UInt32 = 562
SV_SHARINGVIOLATIONRETRIES_PARMNUM: UInt32 = 563
SV_SHARINGVIOLATIONDELAY_PARMNUM: UInt32 = 564
SV_MAXGLOBALOPENSEARCH_PARMNUM: UInt32 = 565
SV_REMOVEDUPLICATESEARCHES_PARMNUM: UInt32 = 566
SV_LOCKVIOLATIONRETRIES_PARMNUM: UInt32 = 567
SV_LOCKVIOLATIONOFFSET_PARMNUM: UInt32 = 568
SV_LOCKVIOLATIONDELAY_PARMNUM: UInt32 = 569
SV_MDLREADSWITCHOVER_PARMNUM: UInt32 = 570
SV_CACHEDOPENLIMIT_PARMNUM: UInt32 = 571
SV_CRITICALTHREADS_PARMNUM: UInt32 = 572
SV_RESTRICTNULLSESSACCESS_PARMNUM: UInt32 = 573
SV_ENABLEWFW311DIRECTIPX_PARMNUM: UInt32 = 574
SV_OTHERQUEUEAFFINITY_PARMNUM: UInt32 = 575
SV_QUEUESAMPLESECS_PARMNUM: UInt32 = 576
SV_BALANCECOUNT_PARMNUM: UInt32 = 577
SV_PREFERREDAFFINITY_PARMNUM: UInt32 = 578
SV_MAXFREERFCBS_PARMNUM: UInt32 = 579
SV_MAXFREEMFCBS_PARMNUM: UInt32 = 580
SV_MAXFREELFCBS_PARMNUM: UInt32 = 581
SV_MAXFREEPAGEDPOOLCHUNKS_PARMNUM: UInt32 = 582
SV_MINPAGEDPOOLCHUNKSIZE_PARMNUM: UInt32 = 583
SV_MAXPAGEDPOOLCHUNKSIZE_PARMNUM: UInt32 = 584
SV_SENDSFROMPREFERREDPROCESSOR_PARMNUM: UInt32 = 585
SV_MAXTHREADSPERQUEUE_PARMNUM: UInt32 = 586
SV_CACHEDDIRECTORYLIMIT_PARMNUM: UInt32 = 587
SV_MAXCOPYLENGTH_PARMNUM: UInt32 = 588
SV_ENABLECOMPRESSION_PARMNUM: UInt32 = 590
SV_AUTOSHAREWKS_PARMNUM: UInt32 = 591
SV_AUTOSHARESERVER_PARMNUM: UInt32 = 592
SV_ENABLESECURITYSIGNATURE_PARMNUM: UInt32 = 593
SV_REQUIRESECURITYSIGNATURE_PARMNUM: UInt32 = 594
SV_MINCLIENTBUFFERSIZE_PARMNUM: UInt32 = 595
SV_CONNECTIONNOSESSIONSTIMEOUT_PARMNUM: UInt32 = 596
SV_IDLETHREADTIMEOUT_PARMNUM: UInt32 = 597
SV_ENABLEW9XSECURITYSIGNATURE_PARMNUM: UInt32 = 598
SV_ENFORCEKERBEROSREAUTHENTICATION_PARMNUM: UInt32 = 599
SV_DISABLEDOS_PARMNUM: UInt32 = 600
SV_LOWDISKSPACEMINIMUM_PARMNUM: UInt32 = 601
SV_DISABLESTRICTNAMECHECKING_PARMNUM: UInt32 = 602
SV_ENABLEAUTHENTICATEUSERSHARING_PARMNUM: UInt32 = 603
SVI1_NUM_ELEMENTS: UInt32 = 5
SVI2_NUM_ELEMENTS: UInt32 = 40
SVI3_NUM_ELEMENTS: UInt32 = 44
SV_MAX_CMD_LEN: UInt32 = 256
SW_AUTOPROF_LOAD_MASK: UInt32 = 1
SW_AUTOPROF_SAVE_MASK: UInt32 = 2
SV_MAX_SRV_HEUR_LEN: UInt32 = 32
SV_USERS_PER_LICENSE: UInt32 = 5
SVTI2_REMAP_PIPE_NAMES: UInt32 = 2
SVTI2_SCOPED_NAME: UInt32 = 4
SVTI2_CLUSTER_NAME: UInt32 = 8
SVTI2_CLUSTER_DNN_NAME: UInt32 = 16
SVTI2_UNICODE_TRANSPORT_ADDRESS: UInt32 = 32
SVTI2_RESERVED1: UInt32 = 4096
SVTI2_RESERVED2: UInt32 = 8192
SVTI2_RESERVED3: UInt32 = 16384
SRV_SUPPORT_HASH_GENERATION: UInt32 = 1
SRV_HASH_GENERATION_ACTIVE: UInt32 = 2
SERVICE_INSTALL_STATE: UInt32 = 3
SERVICE_UNINSTALLED: UInt32 = 0
SERVICE_INSTALL_PENDING: UInt32 = 1
SERVICE_UNINSTALL_PENDING: UInt32 = 2
SERVICE_INSTALLED: UInt32 = 3
SERVICE_PAUSE_STATE: UInt32 = 12
LM20_SERVICE_ACTIVE: UInt32 = 0
LM20_SERVICE_CONTINUE_PENDING: UInt32 = 4
LM20_SERVICE_PAUSE_PENDING: UInt32 = 8
LM20_SERVICE_PAUSED: UInt32 = 12
SERVICE_NOT_UNINSTALLABLE: UInt32 = 0
SERVICE_UNINSTALLABLE: UInt32 = 16
SERVICE_NOT_PAUSABLE: UInt32 = 0
SERVICE_PAUSABLE: UInt32 = 32
SERVICE_REDIR_PAUSED: UInt32 = 1792
SERVICE_REDIR_DISK_PAUSED: UInt32 = 256
SERVICE_REDIR_PRINT_PAUSED: UInt32 = 512
SERVICE_REDIR_COMM_PAUSED: UInt32 = 1024
SERVICE_DOS_ENCRYPTION: String = 'ENCRYPT'
SERVICE_CTRL_INTERROGATE: UInt32 = 0
SERVICE_CTRL_PAUSE: UInt32 = 1
SERVICE_CTRL_CONTINUE: UInt32 = 2
SERVICE_CTRL_UNINSTALL: UInt32 = 3
SERVICE_CTRL_REDIR_DISK: UInt32 = 1
SERVICE_CTRL_REDIR_PRINT: UInt32 = 2
SERVICE_CTRL_REDIR_COMM: UInt32 = 4
SERVICE_IP_NO_HINT: UInt32 = 0
SERVICE_CCP_NO_HINT: UInt32 = 0
SERVICE_IP_QUERY_HINT: UInt32 = 65536
SERVICE_CCP_QUERY_HINT: UInt32 = 65536
SERVICE_IP_CHKPT_NUM: UInt32 = 255
SERVICE_CCP_CHKPT_NUM: UInt32 = 255
SERVICE_IP_WAIT_TIME: UInt32 = 65280
SERVICE_CCP_WAIT_TIME: UInt32 = 65280
SERVICE_IP_WAITTIME_SHIFT: UInt32 = 8
SERVICE_NTIP_WAITTIME_SHIFT: UInt32 = 12
UPPER_HINT_MASK: UInt32 = 65280
LOWER_HINT_MASK: UInt32 = 255
UPPER_GET_HINT_MASK: UInt32 = 267386880
LOWER_GET_HINT_MASK: UInt32 = 65280
SERVICE_NT_MAXTIME: UInt32 = 65535
SERVICE_RESRV_MASK: UInt32 = 131071
SERVICE_MAXTIME: UInt32 = 255
SERVICE_BASE: UInt32 = 3050
SERVICE_UIC_NORMAL: UInt32 = 0
SERVICE_UIC_BADPARMVAL: UInt32 = 3051
SERVICE_UIC_MISSPARM: UInt32 = 3052
SERVICE_UIC_UNKPARM: UInt32 = 3053
SERVICE_UIC_RESOURCE: UInt32 = 3054
SERVICE_UIC_CONFIG: UInt32 = 3055
SERVICE_UIC_SYSTEM: UInt32 = 3056
SERVICE_UIC_INTERNAL: UInt32 = 3057
SERVICE_UIC_AMBIGPARM: UInt32 = 3058
SERVICE_UIC_DUPPARM: UInt32 = 3059
SERVICE_UIC_KILL: UInt32 = 3060
SERVICE_UIC_EXEC: UInt32 = 3061
SERVICE_UIC_SUBSERV: UInt32 = 3062
SERVICE_UIC_CONFLPARM: UInt32 = 3063
SERVICE_UIC_FILE: UInt32 = 3064
SERVICE_UIC_M_NULL: UInt32 = 0
SERVICE_UIC_M_MEMORY: UInt32 = 3070
SERVICE_UIC_M_DISK: UInt32 = 3071
SERVICE_UIC_M_THREADS: UInt32 = 3072
SERVICE_UIC_M_PROCESSES: UInt32 = 3073
SERVICE_UIC_M_SECURITY: UInt32 = 3074
SERVICE_UIC_M_LANROOT: UInt32 = 3075
SERVICE_UIC_M_REDIR: UInt32 = 3076
SERVICE_UIC_M_SERVER: UInt32 = 3077
SERVICE_UIC_M_SEC_FILE_ERR: UInt32 = 3078
SERVICE_UIC_M_FILES: UInt32 = 3079
SERVICE_UIC_M_LOGS: UInt32 = 3080
SERVICE_UIC_M_LANGROUP: UInt32 = 3081
SERVICE_UIC_M_MSGNAME: UInt32 = 3082
SERVICE_UIC_M_ANNOUNCE: UInt32 = 3083
SERVICE_UIC_M_UAS: UInt32 = 3084
SERVICE_UIC_M_SERVER_SEC_ERR: UInt32 = 3085
SERVICE_UIC_M_WKSTA: UInt32 = 3087
SERVICE_UIC_M_ERRLOG: UInt32 = 3088
SERVICE_UIC_M_FILE_UW: UInt32 = 3089
SERVICE_UIC_M_ADDPAK: UInt32 = 3090
SERVICE_UIC_M_LAZY: UInt32 = 3091
SERVICE_UIC_M_UAS_MACHINE_ACCT: UInt32 = 3092
SERVICE_UIC_M_UAS_SERVERS_NMEMB: UInt32 = 3093
SERVICE_UIC_M_UAS_SERVERS_NOGRP: UInt32 = 3094
SERVICE_UIC_M_UAS_INVALID_ROLE: UInt32 = 3095
SERVICE_UIC_M_NETLOGON_NO_DC: UInt32 = 3096
SERVICE_UIC_M_NETLOGON_DC_CFLCT: UInt32 = 3097
SERVICE_UIC_M_NETLOGON_AUTH: UInt32 = 3098
SERVICE_UIC_M_UAS_PROLOG: UInt32 = 3099
SERVICE2_BASE: UInt32 = 5600
SERVICE_UIC_M_NETLOGON_MPATH: UInt32 = 5600
SERVICE_UIC_M_LSA_MACHINE_ACCT: UInt32 = 5601
SERVICE_UIC_M_DATABASE_ERROR: UInt32 = 5602
USE_FLAG_GLOBAL_MAPPING: UInt32 = 65536
USE_LOCAL_PARMNUM: UInt32 = 1
USE_REMOTE_PARMNUM: UInt32 = 2
USE_PASSWORD_PARMNUM: UInt32 = 3
USE_ASGTYPE_PARMNUM: UInt32 = 4
USE_USERNAME_PARMNUM: UInt32 = 5
USE_DOMAINNAME_PARMNUM: UInt32 = 6
USE_FLAGS_PARMNUM: UInt32 = 7
USE_AUTHIDENTITY_PARMNUM: UInt32 = 8
USE_SD_PARMNUM: UInt32 = 9
USE_OPTIONS_PARMNUM: UInt32 = 10
USE_OK: UInt32 = 0
USE_PAUSED: UInt32 = 1
USE_SESSLOST: UInt32 = 2
USE_DISCONN: UInt32 = 2
USE_NETERR: UInt32 = 3
USE_CONN: UInt32 = 4
USE_RECONN: UInt32 = 5
USE_CHARDEV: UInt32 = 2
CREATE_NO_CONNECT: UInt32 = 1
CREATE_BYPASS_CSC: UInt32 = 2
CREATE_CRED_RESET: UInt32 = 4
USE_DEFAULT_CREDENTIALS: UInt32 = 4
CREATE_REQUIRE_CONNECTION_INTEGRITY: UInt32 = 8
CREATE_REQUIRE_CONNECTION_PRIVACY: UInt32 = 16
CREATE_PERSIST_MAPPING: UInt32 = 32
CREATE_WRITE_THROUGH_SEMANTICS: UInt32 = 64
CREATE_GLOBAL_MAPPING: UInt32 = 256
WKSTA_PLATFORM_ID_PARMNUM: UInt32 = 100
WKSTA_COMPUTERNAME_PARMNUM: UInt32 = 1
WKSTA_LANGROUP_PARMNUM: UInt32 = 2
WKSTA_VER_MAJOR_PARMNUM: UInt32 = 4
WKSTA_VER_MINOR_PARMNUM: UInt32 = 5
WKSTA_LOGGED_ON_USERS_PARMNUM: UInt32 = 6
WKSTA_LANROOT_PARMNUM: UInt32 = 7
WKSTA_LOGON_DOMAIN_PARMNUM: UInt32 = 8
WKSTA_LOGON_SERVER_PARMNUM: UInt32 = 9
WKSTA_CHARWAIT_PARMNUM: UInt32 = 10
WKSTA_CHARTIME_PARMNUM: UInt32 = 11
WKSTA_CHARCOUNT_PARMNUM: UInt32 = 12
WKSTA_KEEPCONN_PARMNUM: UInt32 = 13
WKSTA_KEEPSEARCH_PARMNUM: UInt32 = 14
WKSTA_MAXCMDS_PARMNUM: UInt32 = 15
WKSTA_NUMWORKBUF_PARMNUM: UInt32 = 16
WKSTA_MAXWRKCACHE_PARMNUM: UInt32 = 17
WKSTA_SESSTIMEOUT_PARMNUM: UInt32 = 18
WKSTA_SIZERROR_PARMNUM: UInt32 = 19
WKSTA_NUMALERTS_PARMNUM: UInt32 = 20
WKSTA_NUMSERVICES_PARMNUM: UInt32 = 21
WKSTA_NUMCHARBUF_PARMNUM: UInt32 = 22
WKSTA_SIZCHARBUF_PARMNUM: UInt32 = 23
WKSTA_ERRLOGSZ_PARMNUM: UInt32 = 27
WKSTA_PRINTBUFTIME_PARMNUM: UInt32 = 28
WKSTA_SIZWORKBUF_PARMNUM: UInt32 = 29
WKSTA_MAILSLOTS_PARMNUM: UInt32 = 30
WKSTA_NUMDGRAMBUF_PARMNUM: UInt32 = 31
WKSTA_WRKHEURISTICS_PARMNUM: UInt32 = 32
WKSTA_MAXTHREADS_PARMNUM: UInt32 = 33
WKSTA_LOCKQUOTA_PARMNUM: UInt32 = 41
WKSTA_LOCKINCREMENT_PARMNUM: UInt32 = 42
WKSTA_LOCKMAXIMUM_PARMNUM: UInt32 = 43
WKSTA_PIPEINCREMENT_PARMNUM: UInt32 = 44
WKSTA_PIPEMAXIMUM_PARMNUM: UInt32 = 45
WKSTA_DORMANTFILELIMIT_PARMNUM: UInt32 = 46
WKSTA_CACHEFILETIMEOUT_PARMNUM: UInt32 = 47
WKSTA_USEOPPORTUNISTICLOCKING_PARMNUM: UInt32 = 48
WKSTA_USEUNLOCKBEHIND_PARMNUM: UInt32 = 49
WKSTA_USECLOSEBEHIND_PARMNUM: UInt32 = 50
WKSTA_BUFFERNAMEDPIPES_PARMNUM: UInt32 = 51
WKSTA_USELOCKANDREADANDUNLOCK_PARMNUM: UInt32 = 52
WKSTA_UTILIZENTCACHING_PARMNUM: UInt32 = 53
WKSTA_USERAWREAD_PARMNUM: UInt32 = 54
WKSTA_USERAWWRITE_PARMNUM: UInt32 = 55
WKSTA_USEWRITERAWWITHDATA_PARMNUM: UInt32 = 56
WKSTA_USEENCRYPTION_PARMNUM: UInt32 = 57
WKSTA_BUFFILESWITHDENYWRITE_PARMNUM: UInt32 = 58
WKSTA_BUFFERREADONLYFILES_PARMNUM: UInt32 = 59
WKSTA_FORCECORECREATEMODE_PARMNUM: UInt32 = 60
WKSTA_USE512BYTESMAXTRANSFER_PARMNUM: UInt32 = 61
WKSTA_READAHEADTHRUPUT_PARMNUM: UInt32 = 62
WKSTA_OTH_DOMAINS_PARMNUM: UInt32 = 101
TRANSPORT_QUALITYOFSERVICE_PARMNUM: UInt32 = 201
TRANSPORT_NAME_PARMNUM: UInt32 = 202
EVENT_SRV_SERVICE_FAILED: Int32 = -1073739824
EVENT_SRV_RESOURCE_SHORTAGE: Int32 = -1073739823
EVENT_SRV_CANT_CREATE_DEVICE: Int32 = -1073739822
EVENT_SRV_CANT_CREATE_PROCESS: Int32 = -1073739821
EVENT_SRV_CANT_CREATE_THREAD: Int32 = -1073739820
EVENT_SRV_UNEXPECTED_DISC: Int32 = -1073739819
EVENT_SRV_INVALID_REQUEST: Int32 = -1073739818
EVENT_SRV_CANT_OPEN_NPFS: Int32 = -1073739817
EVENT_SRV_CANT_GROW_TABLE: Int32 = -2147481639
EVENT_SRV_CANT_START_SCAVENGER: Int32 = -1073739814
EVENT_SRV_IRP_STACK_SIZE: Int32 = -1073739813
EVENT_SRV_NETWORK_ERROR: Int32 = -2147481636
EVENT_SRV_DISK_FULL: Int32 = -2147481635
EVENT_SRV_NO_VIRTUAL_MEMORY: Int32 = -1073739808
EVENT_SRV_NONPAGED_POOL_LIMIT: Int32 = -1073739807
EVENT_SRV_PAGED_POOL_LIMIT: Int32 = -1073739806
EVENT_SRV_NO_NONPAGED_POOL: Int32 = -1073739805
EVENT_SRV_NO_PAGED_POOL: Int32 = -1073739804
EVENT_SRV_NO_WORK_ITEM: Int32 = -2147481627
EVENT_SRV_NO_FREE_CONNECTIONS: Int32 = -2147481626
EVENT_SRV_NO_FREE_RAW_WORK_ITEM: Int32 = -2147481625
EVENT_SRV_NO_BLOCKING_IO: Int32 = -2147481624
EVENT_SRV_DOS_ATTACK_DETECTED: Int32 = -2147481623
EVENT_SRV_TOO_MANY_DOS: Int32 = -2147481622
EVENT_SRV_OUT_OF_WORK_ITEM_DOS: Int32 = -2147481621
EVENT_SRV_KEY_NOT_FOUND: Int32 = -1073739323
EVENT_SRV_KEY_NOT_CREATED: Int32 = -1073739322
EVENT_SRV_NO_TRANSPORTS_BOUND: Int32 = -1073739321
EVENT_SRV_CANT_BIND_TO_TRANSPORT: Int32 = -2147481144
EVENT_SRV_CANT_BIND_DUP_NAME: Int32 = -1073739319
EVENT_SRV_INVALID_REGISTRY_VALUE: Int32 = -2147481142
EVENT_SRV_INVALID_SD: Int32 = -2147481141
EVENT_SRV_CANT_LOAD_DRIVER: Int32 = -2147481140
EVENT_SRV_CANT_UNLOAD_DRIVER: Int32 = -2147481139
EVENT_SRV_CANT_MAP_ERROR: Int32 = -2147481138
EVENT_SRV_CANT_RECREATE_SHARE: Int32 = -2147481137
EVENT_SRV_CANT_CHANGE_DOMAIN_NAME: Int32 = -2147481136
EVENT_SRV_TXF_INIT_FAILED: Int32 = -2147481135
EVENT_RDR_RESOURCE_SHORTAGE: Int32 = -2147480647
EVENT_RDR_CANT_CREATE_DEVICE: Int32 = -2147480646
EVENT_RDR_CANT_CREATE_THREAD: Int32 = -2147480645
EVENT_RDR_CANT_SET_THREAD: Int32 = -2147480644
EVENT_RDR_INVALID_REPLY: Int32 = -2147480643
EVENT_RDR_INVALID_SMB: Int32 = -2147480642
EVENT_RDR_INVALID_LOCK_REPLY: Int32 = -2147480641
EVENT_RDR_FAILED_UNLOCK: Int32 = -2147480639
EVENT_RDR_CLOSE_BEHIND: Int32 = -2147480637
EVENT_RDR_UNEXPECTED_ERROR: Int32 = -2147480636
EVENT_RDR_TIMEOUT: Int32 = -2147480635
EVENT_RDR_INVALID_OPLOCK: Int32 = -2147480634
EVENT_RDR_CONNECTION_REFERENCE: Int32 = -2147480633
EVENT_RDR_SERVER_REFERENCE: Int32 = -2147480632
EVENT_RDR_SMB_REFERENCE: Int32 = -2147480631
EVENT_RDR_ENCRYPT: Int32 = -2147480630
EVENT_RDR_CONNECTION: Int32 = -2147480629
EVENT_RDR_MAXCMDS: Int32 = -2147480627
EVENT_RDR_OPLOCK_SMB: Int32 = -2147480626
EVENT_RDR_DISPOSITION: Int32 = -2147480625
EVENT_RDR_CONTEXTS: Int32 = -2147480624
EVENT_RDR_WRITE_BEHIND_FLUSH_FAILED: Int32 = -2147480623
EVENT_RDR_AT_THREAD_MAX: Int32 = -2147480622
EVENT_RDR_CANT_READ_REGISTRY: Int32 = -2147480621
EVENT_RDR_TIMEZONE_BIAS_TOO_LARGE: Int32 = -2147480620
EVENT_RDR_PRIMARY_TRANSPORT_CONNECT_FAILED: Int32 = -2147480619
EVENT_RDR_DELAYED_SET_ATTRIBUTES_FAILED: Int32 = -2147480618
EVENT_RDR_DELETEONCLOSE_FAILED: Int32 = -2147480617
EVENT_RDR_CANT_BIND_TRANSPORT: Int32 = -2147480616
EVENT_RDR_CANT_REGISTER_ADDRESS: Int32 = -2147480615
EVENT_RDR_CANT_GET_SECURITY_CONTEXT: Int32 = -2147480614
EVENT_RDR_CANT_BUILD_SMB_HEADER: Int32 = -2147480613
EVENT_RDR_SECURITY_SIGNATURE_MISMATCH: Int32 = -2147480612
EVENT_TCPIP6_STARTED: Int32 = 1073744924
EVENT_STREAMS_STRLOG: Int32 = -1073737824
EVENT_STREAMS_ALLOCB_FAILURE: Int32 = -2147479647
EVENT_STREAMS_ALLOCB_FAILURE_CNT: Int32 = -2147479646
EVENT_STREAMS_ESBALLOC_FAILURE: Int32 = -2147479645
EVENT_STREAMS_ESBALLOC_FAILURE_CNT: Int32 = -2147479644
EVENT_TCPIP_CREATE_DEVICE_FAILED: Int32 = -1073737724
EVENT_TCPIP_NO_RESOURCES_FOR_INIT: Int32 = -1073737723
EVENT_TCPIP_TOO_MANY_NETS: Int32 = -1073737639
EVENT_TCPIP_NO_MASK: Int32 = -1073737638
EVENT_TCPIP_INVALID_ADDRESS: Int32 = -1073737637
EVENT_TCPIP_INVALID_MASK: Int32 = -1073737636
EVENT_TCPIP_NO_ADAPTER_RESOURCES: Int32 = -1073737635
EVENT_TCPIP_DHCP_INIT_FAILED: Int32 = -2147479458
EVENT_TCPIP_ADAPTER_REG_FAILURE: Int32 = -1073737633
EVENT_TCPIP_INVALID_DEFAULT_GATEWAY: Int32 = -2147479456
EVENT_TCPIP_NO_ADDRESS_LIST: Int32 = -1073737631
EVENT_TCPIP_NO_MASK_LIST: Int32 = -1073737630
EVENT_TCPIP_NO_BINDINGS: Int32 = -1073737629
EVENT_TCPIP_IP_INIT_FAILED: Int32 = -1073737628
EVENT_TCPIP_TOO_MANY_GATEWAYS: Int32 = -2147479451
EVENT_TCPIP_ADDRESS_CONFLICT1: Int32 = -1073737626
EVENT_TCPIP_ADDRESS_CONFLICT2: Int32 = -1073737625
EVENT_TCPIP_NTE_CONTEXT_LIST_FAILURE: Int32 = -1073737624
EVENT_TCPIP_MEDIA_CONNECT: Int32 = 1073746025
EVENT_TCPIP_MEDIA_DISCONNECT: Int32 = 1073746026
EVENT_TCPIP_IPV4_UNINSTALLED: Int32 = 1073746027
EVENT_TCPIP_AUTOCONFIGURED_ADDRESS_LIMIT_REACHED: Int32 = -2147479444
EVENT_TCPIP_AUTOCONFIGURED_ROUTE_LIMIT_REACHED: Int32 = -2147479443
EVENT_TCPIP_OUT_OF_ORDER_FRAGMENTS_EXCEEDED: Int32 = -2147479442
EVENT_TCPIP_INTERFACE_BIND_FAILURE: Int32 = -1073737617
EVENT_TCPIP_TCP_INIT_FAILED: Int32 = -1073737599
EVENT_TCPIP_TCP_CONNECT_LIMIT_REACHED: Int32 = -2147479422
EVENT_TCPIP_TCP_TIME_WAIT_COLLISION: Int32 = -2147479421
EVENT_TCPIP_TCP_WSD_WS_RESTRICTED: Int32 = -2147479420
EVENT_TCPIP_TCP_MPP_ATTACKS_DETECTED: Int32 = -2147479419
EVENT_TCPIP_TCP_CONNECTIONS_PERF_IMPACTED: Int32 = -2147479418
EVENT_TCPIP_TCP_GLOBAL_EPHEMERAL_PORT_SPACE_EXHAUSTED: Int32 = -2147479417
EVENT_TCPIP_UDP_LIMIT_REACHED: Int32 = -2147479383
EVENT_TCPIP_UDP_GLOBAL_EPHEMERAL_PORT_SPACE_EXHAUSTED: Int32 = -2147479382
EVENT_TCPIP_PCF_MULTICAST_OID_ISSUE: Int32 = -2147479358
EVENT_TCPIP_PCF_MISSING_CAPABILITY: Int32 = -2147479357
EVENT_TCPIP_PCF_SET_FILTER_FAILURE: Int32 = -2147479356
EVENT_TCPIP_PCF_NO_ARP_FILTER: Int32 = -2147479355
EVENT_TCPIP_PCF_CLEAR_FILTER_FAILURE: Int32 = -1073737530
EVENT_NBT_CREATE_DRIVER: Int32 = -1073737524
EVENT_NBT_OPEN_REG_PARAMS: Int32 = -1073737523
EVENT_NBT_NO_BACKUP_WINS: Int32 = -2147479346
EVENT_NBT_NO_WINS: Int32 = -2147479345
EVENT_NBT_BAD_BACKUP_WINS_ADDR: Int32 = -2147479344
EVENT_NBT_BAD_PRIMARY_WINS_ADDR: Int32 = -2147479343
EVENT_NBT_NAME_SERVER_ADDRS: Int32 = -1073737518
EVENT_NBT_CREATE_ADDRESS: Int32 = -1073737517
EVENT_NBT_CREATE_CONNECTION: Int32 = -1073737516
EVENT_NBT_NON_OS_INIT: Int32 = -1073737515
EVENT_NBT_TIMERS: Int32 = -1073737514
EVENT_NBT_CREATE_DEVICE: Int32 = -1073737513
EVENT_NBT_NO_DEVICES: Int32 = -2147479336
EVENT_NBT_OPEN_REG_LINKAGE: Int32 = -1073737511
EVENT_NBT_READ_BIND: Int32 = -1073737510
EVENT_NBT_READ_EXPORT: Int32 = -1073737509
EVENT_NBT_OPEN_REG_NAMESERVER: Int32 = -2147479332
EVENT_SCOPE_LABEL_TOO_LONG: Int32 = -2147479331
EVENT_SCOPE_TOO_LONG: Int32 = -2147479330
EVENT_NBT_DUPLICATE_NAME: Int32 = -1073737505
EVENT_NBT_NAME_RELEASE: Int32 = -1073737504
EVENT_NBT_DUPLICATE_NAME_ERROR: Int32 = -1073737503
EVENT_NBT_NO_RESOURCES: Int32 = -1073737502
EVENT_NDIS_RESOURCE_CONFLICT: Int32 = -1073736824
EVENT_NDIS_OUT_OF_RESOURCE: Int32 = -1073736823
EVENT_NDIS_HARDWARE_FAILURE: Int32 = -1073736822
EVENT_NDIS_ADAPTER_NOT_FOUND: Int32 = -1073736821
EVENT_NDIS_INTERRUPT_CONNECT: Int32 = -1073736820
EVENT_NDIS_DRIVER_FAILURE: Int32 = -1073736819
EVENT_NDIS_BAD_VERSION: Int32 = -1073736818
EVENT_NDIS_TIMEOUT: Int32 = -2147478641
EVENT_NDIS_NETWORK_ADDRESS: Int32 = -1073736816
EVENT_NDIS_UNSUPPORTED_CONFIGURATION: Int32 = -1073736815
EVENT_NDIS_INVALID_VALUE_FROM_ADAPTER: Int32 = -1073736814
EVENT_NDIS_MISSING_CONFIGURATION_PARAMETER: Int32 = -1073736813
EVENT_NDIS_BAD_IO_BASE_ADDRESS: Int32 = -1073736812
EVENT_NDIS_RECEIVE_SPACE_SMALL: Int32 = 1073746837
EVENT_NDIS_ADAPTER_DISABLED: Int32 = -2147478634
EVENT_NDIS_IO_PORT_CONFLICT: Int32 = -2147478633
EVENT_NDIS_PORT_OR_DMA_CONFLICT: Int32 = -2147478632
EVENT_NDIS_MEMORY_CONFLICT: Int32 = -2147478631
EVENT_NDIS_INTERRUPT_CONFLICT: Int32 = -2147478630
EVENT_NDIS_DMA_CONFLICT: Int32 = -2147478629
EVENT_NDIS_INVALID_DOWNLOAD_FILE_ERROR: Int32 = -1073736804
EVENT_NDIS_MAXRECEIVES_ERROR: Int32 = -2147478627
EVENT_NDIS_MAXTRANSMITS_ERROR: Int32 = -2147478626
EVENT_NDIS_MAXFRAMESIZE_ERROR: Int32 = -2147478625
EVENT_NDIS_MAXINTERNALBUFS_ERROR: Int32 = -2147478624
EVENT_NDIS_MAXMULTICAST_ERROR: Int32 = -2147478623
EVENT_NDIS_PRODUCTID_ERROR: Int32 = -2147478622
EVENT_NDIS_LOBE_FAILUE_ERROR: Int32 = -2147478621
EVENT_NDIS_SIGNAL_LOSS_ERROR: Int32 = -2147478620
EVENT_NDIS_REMOVE_RECEIVED_ERROR: Int32 = -2147478619
EVENT_NDIS_TOKEN_RING_CORRECTION: Int32 = 1073746854
EVENT_NDIS_ADAPTER_CHECK_ERROR: Int32 = -1073736793
EVENT_NDIS_RESET_FAILURE_ERROR: Int32 = -2147478616
EVENT_NDIS_CABLE_DISCONNECTED_ERROR: Int32 = -2147478615
EVENT_NDIS_RESET_FAILURE_CORRECTION: Int32 = -2147478614
EVENT_EventlogStarted: Int32 = -2147477643
EVENT_EventlogStopped: Int32 = -2147477642
EVENT_EventlogAbnormalShutdown: Int32 = -2147477640
EVENT_EventLogProductInfo: Int32 = -2147477639
EVENT_ComputerNameChange: Int32 = -2147477637
EVENT_DNSDomainNameChange: Int32 = -2147477636
EVENT_EventlogUptime: Int32 = -2147477635
EVENT_UP_DRIVER_ON_MP: Int32 = -1073735724
EVENT_SERVICE_START_FAILED: Int32 = -1073734824
EVENT_SERVICE_START_FAILED_II: Int32 = -1073734823
EVENT_SERVICE_START_FAILED_GROUP: Int32 = -1073734822
EVENT_SERVICE_START_FAILED_NONE: Int32 = -1073734821
EVENT_CALL_TO_FUNCTION_FAILED: Int32 = -1073734819
EVENT_CALL_TO_FUNCTION_FAILED_II: Int32 = -1073734818
EVENT_REVERTED_TO_LASTKNOWNGOOD: Int32 = -1073734817
EVENT_BAD_ACCOUNT_NAME: Int32 = -1073734816
EVENT_CONNECTION_TIMEOUT: Int32 = -1073734815
EVENT_READFILE_TIMEOUT: Int32 = -1073734814
EVENT_TRANSACT_TIMEOUT: Int32 = -1073734813
EVENT_TRANSACT_INVALID: Int32 = -1073734812
EVENT_FIRST_LOGON_FAILED: Int32 = -1073734811
EVENT_SECOND_LOGON_FAILED: Int32 = -1073734810
EVENT_INVALID_DRIVER_DEPENDENCY: Int32 = -1073734809
EVENT_BAD_SERVICE_STATE: Int32 = -1073734808
EVENT_CIRCULAR_DEPENDENCY_DEMAND: Int32 = -1073734807
EVENT_CIRCULAR_DEPENDENCY_AUTO: Int32 = -1073734806
EVENT_DEPEND_ON_LATER_SERVICE: Int32 = -1073734805
EVENT_DEPEND_ON_LATER_GROUP: Int32 = -1073734804
EVENT_SEVERE_SERVICE_FAILED: Int32 = -1073734803
EVENT_SERVICE_START_HUNG: Int32 = -1073734802
EVENT_SERVICE_EXIT_FAILED: Int32 = -1073734801
EVENT_SERVICE_EXIT_FAILED_SPECIFIC: Int32 = -1073734800
EVENT_SERVICE_START_AT_BOOT_FAILED: Int32 = -1073734799
EVENT_BOOT_SYSTEM_DRIVERS_FAILED: Int32 = -1073734798
EVENT_RUNNING_LASTKNOWNGOOD: Int32 = -1073734797
EVENT_TAKE_OWNERSHIP: Int32 = -1073734796
TITLE_SC_MESSAGE_BOX: Int32 = -1073734795
EVENT_SERVICE_NOT_INTERACTIVE: Int32 = -1073734794
EVENT_SERVICE_CRASH: Int32 = -1073734793
EVENT_SERVICE_RECOVERY_FAILED: Int32 = -1073734792
EVENT_SERVICE_SCESRV_FAILED: Int32 = -1073734791
EVENT_SERVICE_CRASH_NO_ACTION: Int32 = -1073734790
EVENT_SERVICE_CONTROL_SUCCESS: Int32 = 1073748859
EVENT_SERVICE_STATUS_SUCCESS: Int32 = 1073748860
EVENT_SERVICE_CONFIG_BACKOUT_FAILED: Int32 = -1073734787
EVENT_FIRST_LOGON_FAILED_II: Int32 = -1073734786
EVENT_SERVICE_DIFFERENT_PID_CONNECTED: Int32 = -2147476609
EVENT_SERVICE_START_TYPE_CHANGED: Int32 = 1073748864
EVENT_SERVICE_LOGON_TYPE_NOT_GRANTED: Int32 = -1073734783
EVENT_SERVICE_STOP_SUCCESS_WITH_REASON: Int32 = 1073748866
EVENT_SERVICE_SHUTDOWN_FAILED: Int32 = -1073734781
EVENT_COMMAND_NOT_INTERACTIVE: Int32 = -1073733924
EVENT_COMMAND_START_FAILED: Int32 = -1073733923
EVENT_BOWSER_OTHER_MASTER_ON_NET: Int32 = -1073733821
EVENT_BOWSER_PROMOTED_WHILE_ALREADY_MASTER: Int32 = -2147475644
EVENT_BOWSER_NON_MASTER_MASTER_ANNOUNCE: Int32 = -2147475643
EVENT_BOWSER_ILLEGAL_DATAGRAM: Int32 = -2147475642
EVENT_BROWSER_STATUS_BITS_UPDATE_FAILED: Int32 = -1073733817
EVENT_BROWSER_ROLE_CHANGE_FAILED: Int32 = -1073733816
EVENT_BROWSER_MASTER_PROMOTION_FAILED: Int32 = -1073733815
EVENT_BOWSER_NAME_CONVERSION_FAILED: Int32 = -1073733814
EVENT_BROWSER_OTHERDOMAIN_ADD_FAILED: Int32 = -1073733813
EVENT_BOWSER_ELECTION_RECEIVED: Int32 = 8012
EVENT_BOWSER_ELECTION_SENT_GETBLIST_FAILED: Int32 = 1073749837
EVENT_BOWSER_ELECTION_SENT_FIND_MASTER_FAILED: Int32 = 1073749838
EVENT_BROWSER_ELECTION_SENT_LANMAN_NT_STARTED: Int32 = 1073749839
EVENT_BOWSER_ILLEGAL_DATAGRAM_THRESHOLD: Int32 = -1073733808
EVENT_BROWSER_DEPENDANT_SERVICE_FAILED: Int32 = -1073733807
EVENT_BROWSER_MASTER_PROMOTION_FAILED_STOPPING: Int32 = -1073733805
EVENT_BROWSER_MASTER_PROMOTION_FAILED_NO_MASTER: Int32 = -1073733804
EVENT_BROWSER_SERVER_LIST_FAILED: Int32 = -2147475627
EVENT_BROWSER_DOMAIN_LIST_FAILED: Int32 = -2147475626
EVENT_BROWSER_ILLEGAL_CONFIG: Int32 = -2147475625
EVENT_BOWSER_OLD_BACKUP_FOUND: Int32 = 1073749848
EVENT_BROWSER_SERVER_LIST_RETRIEVED: Int32 = 8025
EVENT_BROWSER_DOMAIN_LIST_RETRIEVED: Int32 = 8026
EVENT_BOWSER_PDC_LOST_ELECTION: Int32 = 1073749851
EVENT_BOWSER_NON_PDC_WON_ELECTION: Int32 = 1073749852
EVENT_BOWSER_CANT_READ_REGISTRY: Int32 = 1073749853
EVENT_BOWSER_MAILSLOT_DATAGRAM_THRESHOLD_EXCEEDED: Int32 = 1073749854
EVENT_BOWSER_GETBROWSERLIST_THRESHOLD_EXCEEDED: Int32 = 1073749855
EVENT_BROWSER_BACKUP_STOPPED: Int32 = -1073733792
EVENT_BROWSER_ELECTION_SENT_LANMAN_NT_STOPPED: Int32 = 1073749857
EVENT_BROWSER_GETBLIST_RECEIVED_NOT_MASTER: Int32 = -1073733790
EVENT_BROWSER_ELECTION_SENT_ROLE_CHANGED: Int32 = 1073749859
EVENT_BROWSER_NOT_STARTED_IPX_CONFIG_MISMATCH: Int32 = -1073733788
NWSAP_EVENT_KEY_NOT_FOUND: Int32 = -1073733324
NWSAP_EVENT_WSASTARTUP_FAILED: Int32 = -1073733323
NWSAP_EVENT_SOCKET_FAILED: Int32 = -1073733322
NWSAP_EVENT_SETOPTBCAST_FAILED: Int32 = -1073733321
NWSAP_EVENT_BIND_FAILED: Int32 = -1073733320
NWSAP_EVENT_GETSOCKNAME_FAILED: Int32 = -1073733319
NWSAP_EVENT_OPTEXTENDEDADDR_FAILED: Int32 = -1073733318
NWSAP_EVENT_OPTBCASTINADDR_FAILED: Int32 = -1073733317
NWSAP_EVENT_CARDMALLOC_FAILED: Int32 = -1073733316
NWSAP_EVENT_NOCARDS: Int32 = -1073733315
NWSAP_EVENT_THREADEVENT_FAIL: Int32 = -1073733314
NWSAP_EVENT_RECVSEM_FAIL: Int32 = -1073733313
NWSAP_EVENT_SENDEVENT_FAIL: Int32 = -1073733312
NWSAP_EVENT_STARTRECEIVE_ERROR: Int32 = -1073733311
NWSAP_EVENT_STARTWORKER_ERROR: Int32 = -1073733310
NWSAP_EVENT_TABLE_MALLOC_FAILED: Int32 = -1073733309
NWSAP_EVENT_HASHTABLE_MALLOC_FAILED: Int32 = -1073733308
NWSAP_EVENT_STARTLPCWORKER_ERROR: Int32 = -1073733307
NWSAP_EVENT_CREATELPCPORT_ERROR: Int32 = -1073733306
NWSAP_EVENT_CREATELPCEVENT_ERROR: Int32 = -1073733305
NWSAP_EVENT_LPCLISTENMEMORY_ERROR: Int32 = -1073733304
NWSAP_EVENT_LPCHANDLEMEMORY_ERROR: Int32 = -1073733303
NWSAP_EVENT_BADWANFILTER_VALUE: Int32 = -1073733302
NWSAP_EVENT_CARDLISTEVENT_FAIL: Int32 = -1073733301
NWSAP_EVENT_SDMDEVENT_FAIL: Int32 = -1073733300
NWSAP_EVENT_INVALID_FILTERNAME: Int32 = -2147475123
NWSAP_EVENT_WANSEM_FAIL: Int32 = -1073733298
NWSAP_EVENT_WANSOCKET_FAILED: Int32 = -1073733297
NWSAP_EVENT_WANBIND_FAILED: Int32 = -1073733296
NWSAP_EVENT_STARTWANWORKER_ERROR: Int32 = -1073733295
NWSAP_EVENT_STARTWANCHECK_ERROR: Int32 = -1073733294
NWSAP_EVENT_OPTMAXADAPTERNUM_ERROR: Int32 = -1073733293
NWSAP_EVENT_WANHANDLEMEMORY_ERROR: Int32 = -1073733292
NWSAP_EVENT_WANEVENT_ERROR: Int32 = -1073733291
EVENT_TRANSPORT_RESOURCE_POOL: Int32 = -2147474647
EVENT_TRANSPORT_RESOURCE_LIMIT: Int32 = -2147474646
EVENT_TRANSPORT_RESOURCE_SPECIFIC: Int32 = -2147474645
EVENT_TRANSPORT_REGISTER_FAILED: Int32 = -1073732820
EVENT_TRANSPORT_BINDING_FAILED: Int32 = -1073732819
EVENT_TRANSPORT_ADAPTER_NOT_FOUND: Int32 = -1073732818
EVENT_TRANSPORT_SET_OID_FAILED: Int32 = -1073732817
EVENT_TRANSPORT_QUERY_OID_FAILED: Int32 = -1073732816
EVENT_TRANSPORT_TRANSFER_DATA: Int32 = 1073750833
EVENT_TRANSPORT_TOO_MANY_LINKS: Int32 = 1073750834
EVENT_TRANSPORT_BAD_PROTOCOL: Int32 = 1073750835
EVENT_IPX_NEW_DEFAULT_TYPE: Int32 = 1073751325
EVENT_IPX_SAP_ANNOUNCE: Int32 = -2147474146
EVENT_IPX_ILLEGAL_CONFIG: Int32 = -2147474145
EVENT_IPX_INTERNAL_NET_INVALID: Int32 = -1073732320
EVENT_IPX_NO_FRAME_TYPES: Int32 = -1073732319
EVENT_IPX_CREATE_DEVICE: Int32 = -1073732318
EVENT_IPX_NO_ADAPTERS: Int32 = -1073732317
EVENT_RPCSS_CREATEPROCESS_FAILURE: Int32 = -1073731824
EVENT_RPCSS_RUNAS_CREATEPROCESS_FAILURE: Int32 = -1073731823
EVENT_RPCSS_LAUNCH_ACCESS_DENIED: Int32 = -1073731822
EVENT_RPCSS_DEFAULT_LAUNCH_ACCESS_DENIED: Int32 = -1073731821
EVENT_RPCSS_RUNAS_CANT_LOGIN: Int32 = -1073731820
EVENT_RPCSS_START_SERVICE_FAILURE: Int32 = -1073731819
EVENT_RPCSS_REMOTE_SIDE_ERROR: Int32 = -1073731818
EVENT_RPCSS_ACTIVATION_ERROR: Int32 = -1073731817
EVENT_RPCSS_REMOTE_SIDE_ERROR_WITH_FILE: Int32 = -1073731816
EVENT_RPCSS_REMOTE_SIDE_UNAVAILABLE: Int32 = -1073731815
EVENT_RPCSS_SERVER_START_TIMEOUT: Int32 = -1073731814
EVENT_RPCSS_SERVER_NOT_RESPONDING: Int32 = -1073731813
EVENT_DCOM_ASSERTION_FAILURE: Int32 = -1073731812
EVENT_DCOM_INVALID_ENDPOINT_DATA: Int32 = -1073731811
EVENT_DCOM_COMPLUS_DISABLED: Int32 = -1073731810
EVENT_RPCSS_STOP_SERVICE_FAILURE: Int32 = -1073731795
EVENT_RPCSS_CREATEDEBUGGERPROCESS_FAILURE: Int32 = -1073731794
EVENT_DNS_CACHE_START_FAILURE_NO_DLL: Int32 = -1073730824
EVENT_DNS_CACHE_START_FAILURE_NO_ENTRY: Int32 = -1073730823
EVENT_DNS_CACHE_START_FAILURE_NO_CONTROL: Int32 = -1073730822
EVENT_DNS_CACHE_START_FAILURE_NO_DONE_EVENT: Int32 = -1073730821
EVENT_DNS_CACHE_START_FAILURE_NO_RPC: Int32 = -1073730820
EVENT_DNS_CACHE_START_FAILURE_NO_SHUTDOWN_NOTIFY: Int32 = -1073730819
EVENT_DNS_CACHE_START_FAILURE_NO_UPDATE: Int32 = -1073730818
EVENT_DNS_CACHE_START_FAILURE_LOW_MEMORY: Int32 = -1073730817
EVENT_DNS_CACHE_NETWORK_PERF_WARNING: Int32 = -2147472598
EVENT_DNS_CACHE_UNABLE_TO_REACH_SERVER_WARNING: Int32 = -2147472597
EVENT_DNSAPI_REGISTRATION_FAILED_TIMEOUT: Int32 = -2147472498
EVENT_DNSAPI_REGISTRATION_FAILED_SERVERFAIL: Int32 = -2147472497
EVENT_DNSAPI_REGISTRATION_FAILED_NOTSUPP: Int32 = -2147472496
EVENT_DNSAPI_REGISTRATION_FAILED_REFUSED: Int32 = -2147472495
EVENT_DNSAPI_REGISTRATION_FAILED_SECURITY: Int32 = -2147472494
EVENT_DNSAPI_REGISTRATION_FAILED_OTHER: Int32 = -2147472493
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_TIMEOUT: Int32 = -2147472492
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_SERVERFAIL: Int32 = -2147472491
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_NOTSUPP: Int32 = -2147472490
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_REFUSED: Int32 = -2147472489
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_SECURITY: Int32 = -2147472488
EVENT_DNSAPI_PTR_REGISTRATION_FAILED_OTHER: Int32 = -2147472487
EVENT_DNSAPI_REGISTRATION_FAILED_TIMEOUT_PRIMARY_DN: Int32 = -2147472486
EVENT_DNSAPI_REGISTRATION_FAILED_SERVERFAIL_PRIMARY_DN: Int32 = -2147472485
EVENT_DNSAPI_REGISTRATION_FAILED_NOTSUPP_PRIMARY_DN: Int32 = -2147472484
EVENT_DNSAPI_REGISTRATION_FAILED_REFUSED_PRIMARY_DN: Int32 = -2147472483
EVENT_DNSAPI_REGISTRATION_FAILED_SECURITY_PRIMARY_DN: Int32 = -2147472482
EVENT_DNSAPI_REGISTRATION_FAILED_OTHER_PRIMARY_DN: Int32 = -2147472481
EVENT_DNSAPI_DEREGISTRATION_FAILED_TIMEOUT: Int32 = -2147472468
EVENT_DNSAPI_DEREGISTRATION_FAILED_SERVERFAIL: Int32 = -2147472467
EVENT_DNSAPI_DEREGISTRATION_FAILED_NOTSUPP: Int32 = -2147472466
EVENT_DNSAPI_DEREGISTRATION_FAILED_REFUSED: Int32 = -2147472465
EVENT_DNSAPI_DEREGISTRATION_FAILED_SECURITY: Int32 = -2147472464
EVENT_DNSAPI_DEREGISTRATION_FAILED_OTHER: Int32 = -2147472463
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_TIMEOUT: Int32 = -2147472462
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_SERVERFAIL: Int32 = -2147472461
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_NOTSUPP: Int32 = -2147472460
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_REFUSED: Int32 = -2147472459
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_SECURITY: Int32 = -2147472458
EVENT_DNSAPI_PTR_DEREGISTRATION_FAILED_OTHER: Int32 = -2147472457
EVENT_DNSAPI_DEREGISTRATION_FAILED_TIMEOUT_PRIMARY_DN: Int32 = -2147472456
EVENT_DNSAPI_DEREGISTRATION_FAILED_SERVERFAIL_PRIMARY_DN: Int32 = -2147472455
EVENT_DNSAPI_DEREGISTRATION_FAILED_NOTSUPP_PRIMARY_DN: Int32 = -2147472454
EVENT_DNSAPI_DEREGISTRATION_FAILED_REFUSED_PRIMARY_DN: Int32 = -2147472453
EVENT_DNSAPI_DEREGISTRATION_FAILED_SECURITY_PRIMARY_DN: Int32 = -2147472452
EVENT_DNSAPI_DEREGISTRATION_FAILED_OTHER_PRIMARY_DN: Int32 = -2147472451
EVENT_DNSAPI_REGISTERED_ADAPTER: Int32 = 1073753024
EVENT_DNSAPI_REGISTERED_PTR: Int32 = 1073753025
EVENT_DNSAPI_REGISTERED_ADAPTER_PRIMARY_DN: Int32 = 1073753026
EVENT_TRK_INTERNAL_ERROR: Int32 = -1073729324
EVENT_TRK_SERVICE_START_SUCCESS: Int32 = 1073754325
EVENT_TRK_SERVICE_START_FAILURE: Int32 = -1073729322
EVENT_TRK_SERVICE_CORRUPT_LOG: Int32 = -1073729321
EVENT_TRK_SERVICE_VOL_QUOTA_EXCEEDED: Int32 = -2147471144
EVENT_TRK_SERVICE_VOLUME_CREATE: Int32 = 1073754329
EVENT_TRK_SERVICE_VOLUME_CLAIM: Int32 = 1073754330
EVENT_TRK_SERVICE_DUPLICATE_VOLIDS: Int32 = 1073754331
EVENT_TRK_SERVICE_MOVE_QUOTA_EXCEEDED: Int32 = -2147471140
EVENT_FRS_ERROR: Int32 = -1073728324
EVENT_FRS_STARTING: Int32 = 1073755325
EVENT_FRS_STOPPING: Int32 = 1073755326
EVENT_FRS_STOPPED: Int32 = 1073755327
EVENT_FRS_STOPPED_FORCE: Int32 = -1073728320
EVENT_FRS_STOPPED_ASSERT: Int32 = -1073728319
EVENT_FRS_ASSERT: Int32 = -1073728318
EVENT_FRS_VOLUME_NOT_SUPPORTED: Int32 = -1073728317
EVENT_FRS_LONG_JOIN: Int32 = -2147470140
EVENT_FRS_LONG_JOIN_DONE: Int32 = -2147470139
EVENT_FRS_CANNOT_COMMUNICATE: Int32 = -1073728314
EVENT_FRS_DATABASE_SPACE: Int32 = -1073728313
EVENT_FRS_DISK_WRITE_CACHE_ENABLED: Int32 = -2147470136
EVENT_FRS_JET_1414: Int32 = -1073728311
EVENT_FRS_SYSVOL_NOT_READY: Int32 = -2147470134
EVENT_FRS_SYSVOL_NOT_READY_PRIMARY: Int32 = -2147470133
EVENT_FRS_SYSVOL_READY: Int32 = 1073755340
EVENT_FRS_ACCESS_CHECKS_DISABLED: Int32 = -2147470131
EVENT_FRS_ACCESS_CHECKS_FAILED_USER: Int32 = -2147470130
EVENT_FRS_ACCESS_CHECKS_FAILED_UNKNOWN: Int32 = -1073728305
EVENT_FRS_MOVED_PREEXISTING: Int32 = -2147470128
EVENT_FRS_CANNOT_START_BACKUP_RESTORE_IN_PROGRESS: Int32 = -1073728303
EVENT_FRS_STAGING_AREA_FULL: Int32 = -2147470126
EVENT_FRS_HUGE_FILE: Int32 = -2147470125
EVENT_FRS_CANNOT_CREATE_UUID: Int32 = -1073728300
EVENT_FRS_NO_DNS_ATTRIBUTE: Int32 = -2147470123
EVENT_FRS_NO_SID: Int32 = -1073728298
NTFRSPRF_OPEN_RPC_BINDING_ERROR_SET: Int32 = -1073728297
NTFRSPRF_OPEN_RPC_BINDING_ERROR_CONN: Int32 = -1073728296
NTFRSPRF_OPEN_RPC_CALL_ERROR_SET: Int32 = -1073728295
NTFRSPRF_OPEN_RPC_CALL_ERROR_CONN: Int32 = -1073728294
NTFRSPRF_COLLECT_RPC_BINDING_ERROR_SET: Int32 = -1073728293
NTFRSPRF_COLLECT_RPC_BINDING_ERROR_CONN: Int32 = -1073728292
NTFRSPRF_COLLECT_RPC_CALL_ERROR_SET: Int32 = -1073728291
NTFRSPRF_COLLECT_RPC_CALL_ERROR_CONN: Int32 = -1073728290
NTFRSPRF_VIRTUALALLOC_ERROR_SET: Int32 = -1073728289
NTFRSPRF_VIRTUALALLOC_ERROR_CONN: Int32 = -1073728288
NTFRSPRF_REGISTRY_ERROR_SET: Int32 = -1073728287
NTFRSPRF_REGISTRY_ERROR_CONN: Int32 = -1073728286
EVENT_FRS_ROOT_NOT_VALID: Int32 = -1073728285
EVENT_FRS_STAGE_NOT_VALID: Int32 = -1073728284
EVENT_FRS_OVERLAPS_LOGGING: Int32 = -1073728283
EVENT_FRS_OVERLAPS_WORKING: Int32 = -1073728282
EVENT_FRS_OVERLAPS_STAGE: Int32 = -1073728281
EVENT_FRS_OVERLAPS_ROOT: Int32 = -1073728280
EVENT_FRS_OVERLAPS_OTHER_STAGE: Int32 = -1073728279
EVENT_FRS_PREPARE_ROOT_FAILED: Int32 = -1073728278
EVENT_FRS_BAD_REG_DATA: Int32 = -2147470101
EVENT_FRS_JOIN_FAIL_TIME_SKEW: Int32 = -1073728276
EVENT_FRS_RMTCO_TIME_SKEW: Int32 = -1073728275
EVENT_FRS_CANT_OPEN_STAGE: Int32 = -1073728274
EVENT_FRS_CANT_OPEN_PREINSTALL: Int32 = -1073728273
EVENT_FRS_REPLICA_SET_CREATE_FAIL: Int32 = -1073728272
EVENT_FRS_REPLICA_SET_CREATE_OK: Int32 = 1073755377
EVENT_FRS_REPLICA_SET_CXTIONS: Int32 = 1073755378
EVENT_FRS_IN_ERROR_STATE: Int32 = -1073728269
EVENT_FRS_REPLICA_NO_ROOT_CHANGE: Int32 = -1073728268
EVENT_FRS_DUPLICATE_IN_CXTION_SYSVOL: Int32 = -1073728267
EVENT_FRS_DUPLICATE_IN_CXTION: Int32 = -1073728266
EVENT_FRS_ROOT_HAS_MOVED: Int32 = -1073728265
EVENT_FRS_ERROR_REPLICA_SET_DELETED: Int32 = -2147470088
EVENT_FRS_REPLICA_IN_JRNL_WRAP_ERROR: Int32 = -1073728263
EVENT_FRS_DS_POLL_ERROR_SUMMARY: Int32 = -2147470086
EVENT_PS_GPC_REGISTER_FAILED: Int32 = -1073727824
EVENT_PS_NO_RESOURCES_FOR_INIT: Int32 = -1073727823
EVENT_PS_REGISTER_PROTOCOL_FAILED: Int32 = -1073727822
EVENT_PS_REGISTER_MINIPORT_FAILED: Int32 = -1073727821
EVENT_PS_BAD_BESTEFFORT_LIMIT: Int32 = -2147469548
EVENT_PS_QUERY_OID_GEN_MAXIMUM_FRAME_SIZE: Int32 = -1073727723
EVENT_PS_QUERY_OID_GEN_MAXIMUM_TOTAL_SIZE: Int32 = -1073727722
EVENT_PS_QUERY_OID_GEN_LINK_SPEED: Int32 = -1073727721
EVENT_PS_BINDING_FAILED: Int32 = -1073727720
EVENT_PS_MISSING_ADAPTER_REGISTRY_DATA: Int32 = -1073727719
EVENT_PS_REGISTER_ADDRESS_FAMILY_FAILED: Int32 = -1073727718
EVENT_PS_INIT_DEVICE_FAILED: Int32 = -1073727717
EVENT_PS_WMI_INSTANCE_NAME_FAILED: Int32 = -1073727716
EVENT_PS_WAN_LIMITED_BESTEFFORT: Int32 = -2147469539
EVENT_PS_RESOURCE_POOL: Int32 = -1073727714
EVENT_PS_ADMISSIONCONTROL_OVERFLOW: Int32 = -2147469537
EVENT_PS_NETWORK_ADDRESS_FAIL: Int32 = -1073727712
EXTRA_EXIT_POINT: Int32 = -1073727524
MISSING_EXIT_POINT: Int32 = -1073727523
MISSING_VOLUME: Int32 = -1073727522
EXTRA_VOLUME: Int32 = -1073727521
EXTRA_EXIT_POINT_DELETED: Int32 = -1073727520
EXTRA_EXIT_POINT_NOT_DELETED: Int32 = -1073727519
MISSING_EXIT_POINT_CREATED: Int32 = -1073727518
MISSING_EXIT_POINT_NOT_CREATED: Int32 = -1073727517
MISSING_VOLUME_CREATED: Int32 = -1073727516
MISSING_VOLUME_NOT_CREATED: Int32 = -1073727515
EXTRA_VOLUME_DELETED: Int32 = -1073727514
EXTRA_VOLUME_NOT_DELETED: Int32 = -1073727513
COULD_NOT_VERIFY_VOLUMES: Int32 = -1073727512
KNOWLEDGE_INCONSISTENCY_DETECTED: Int32 = -1073727511
PREFIX_MISMATCH: Int32 = -1073727510
PREFIX_MISMATCH_FIXED: Int32 = -1073727509
PREFIX_MISMATCH_NOT_FIXED: Int32 = -1073727508
MACHINE_UNJOINED: Int32 = -1073727507
DFS_REFERRAL_REQUEST: Int32 = 1073756142
NOT_A_DFS_PATH: Int32 = 1073756224
LM_REDIR_FAILURE: Int32 = 1073756225
DFS_CONNECTION_FAILURE: Int32 = 1073756226
DFS_REFERRAL_FAILURE: Int32 = 1073756227
DFS_REFERRAL_SUCCESS: Int32 = 1073756228
DFS_MAX_DNR_ATTEMPTS: Int32 = 1073756229
DFS_SPECIAL_REFERRAL_FAILURE: Int32 = 1073756230
DFS_OPEN_FAILURE: Int32 = 1073756231
NET_DFS_ENUM: Int32 = 1073756324
NET_DFS_ENUMEX: Int32 = 1073756325
DFS_ERROR_CREATE_REPARSEPOINT_FAILURE: Int32 = -1073727321
DFS_ERROR_UNSUPPORTED_FILESYSTEM: Int32 = -1073727320
DFS_ERROR_OVERLAPPING_DIRECTORIES: Int32 = -1073727319
DFS_INFO_ACTIVEDIRECTORY_ONLINE: Int32 = 1073756332
DFS_ERROR_TOO_MANY_ERRORS: Int32 = -1073727315
DFS_ERROR_WINSOCKINIT_FAILED: Int32 = -1073727314
DFS_ERROR_SECURITYINIT_FAILED: Int32 = -1073727313
DFS_ERROR_THREADINIT_FAILED: Int32 = -1073727312
DFS_ERROR_SITECACHEINIT_FAILED: Int32 = -1073727311
DFS_ERROR_ROOTSYNCINIT_FAILED: Int32 = -1073727310
DFS_ERROR_CREATEEVENT_FAILED: Int32 = -1073727309
DFS_ERROR_COMPUTERINFO_FAILED: Int32 = -1073727308
DFS_ERROR_CLUSTERINFO_FAILED: Int32 = -1073727307
DFS_ERROR_DCINFO_FAILED: Int32 = -1073727306
DFS_ERROR_PREFIXTABLE_FAILED: Int32 = -1073727305
DFS_ERROR_HANDLENAMESPACE_FAILED: Int32 = -1073727304
DFS_ERROR_REGISTERSTORE_FAILED: Int32 = -1073727303
DFS_ERROR_REFLECTIONENGINE_FAILED: Int32 = -1073727302
DFS_ERROR_ACTIVEDIRECTORY_OFFLINE: Int32 = -1073727301
DFS_ERROR_SITESUPPOR_FAILED: Int32 = -1073727300
DFS_ERROR_DSCONNECT_FAILED: Int32 = -2147469122
DFS_INFO_DS_RECONNECTED: Int32 = 1073756353
DFS_ERROR_NO_DFS_DATA: Int32 = -1073727294
DFS_INFO_FINISH_INIT: Int32 = 1073756355
DFS_INFO_RECONNECT_DATA: Int32 = 1073756356
DFS_INFO_FINISH_BUILDING_NAMESPACE: Int32 = 1073756357
DFS_ERROR_ON_ROOT: Int32 = -2147469114
DFS_ERROR_MUTLIPLE_ROOTS_NOT_SUPPORTED: Int32 = -1073727289
DFS_WARN_DOMAIN_REFERRAL_OVERFLOW: Int32 = -2147469112
DFS_INFO_DOMAIN_REFERRAL_MIN_OVERFLOW: Int32 = 1073756361
DFS_WARN_INCOMPLETE_MOVE: Int32 = -2147469110
DFS_ERROR_RESYNCHRONIZE_FAILED: Int32 = -1073727285
DFS_ERROR_REMOVE_LINK_FAILED: Int32 = -1073727284
DFS_WARN_METADATA_LINK_TYPE_INCORRECT: Int32 = -2147469107
DFS_WARN_METADATA_LINK_INFO_INVALID: Int32 = -2147469106
DFS_ERROR_TARGET_LIST_INCORRECT: Int32 = -1073727281
DFS_ERROR_LINKS_OVERLAP: Int32 = -1073727280
DFS_ERROR_LINK_OVERLAP: Int32 = -1073727279
DFS_ERROR_CREATE_REPARSEPOINT_SUCCESS: Int32 = 1073756370
DFS_ERROR_DUPLICATE_LINK: Int32 = -1073727277
DFS_ERROR_TRUSTED_DOMAIN_INFO_FAILED: Int32 = -1073727276
DFS_INFO_TRUSTED_DOMAIN_INFO_SUCCESS: Int32 = 1073756373
DFS_ERROR_CROSS_FOREST_TRUST_INFO_FAILED: Int32 = -1073727274
DFS_INFO_CROSS_FOREST_TRUST_INFO_SUCCESS: Int32 = 1073756375
DFS_INIT_SUCCESS: Int32 = 1073756376
DFS_ROOT_SHARE_ACQUIRE_FAILED: Int32 = -2147469095
DFS_ROOT_SHARE_ACQUIRE_SUCCESS: Int32 = 1073756378
EVENT_BRIDGE_PROTOCOL_REGISTER_FAILED: Int32 = -1073727224
EVENT_BRIDGE_MINIPROT_DEVNAME_MISSING: Int32 = -1073727223
EVENT_BRIDGE_MINIPORT_REGISTER_FAILED: Int32 = -1073727222
EVENT_BRIDGE_DEVICE_CREATION_FAILED: Int32 = -1073727221
EVENT_BRIDGE_NO_BRIDGE_MAC_ADDR: Int32 = -1073727220
EVENT_BRIDGE_MINIPORT_INIT_FAILED: Int32 = -1073727219
EVENT_BRIDGE_ETHERNET_NOT_OFFERED: Int32 = -1073727218
EVENT_BRIDGE_THREAD_CREATION_FAILED: Int32 = -1073727217
EVENT_BRIDGE_THREAD_REF_FAILED: Int32 = -1073727216
EVENT_BRIDGE_PACKET_POOL_CREATION_FAILED: Int32 = -1073727215
EVENT_BRIDGE_BUFFER_POOL_CREATION_FAILED: Int32 = -1073727214
EVENT_BRIDGE_INIT_MALLOC_FAILED: Int32 = -1073727213
EVENT_BRIDGE_ADAPTER_LINK_SPEED_QUERY_FAILED: Int32 = -1073727124
EVENT_BRIDGE_ADAPTER_MAC_ADDR_QUERY_FAILED: Int32 = -1073727123
EVENT_BRIDGE_ADAPTER_FILTER_FAILED: Int32 = -1073727122
EVENT_BRIDGE_ADAPTER_NAME_QUERY_FAILED: Int32 = -1073727121
EVENT_BRIDGE_ADAPTER_BIND_FAILED: Int32 = -1073727120
EVENT_DAV_REDIR_DELAYED_WRITE_FAILED: Int32 = -2147468848
EVENT_WEBCLIENT_CLOSE_PUT_FAILED: Int32 = -2147468747
EVENT_WEBCLIENT_CLOSE_DELETE_FAILED: Int32 = -2147468746
EVENT_WEBCLIENT_CLOSE_PROPPATCH_FAILED: Int32 = -2147468745
EVENT_WEBCLIENT_SETINFO_PROPPATCH_FAILED: Int32 = -2147468744
EVENT_WSK_OWNINGTHREAD_PARAMETER_IGNORED: Int32 = -1073725824
EVENT_WINSOCK_TDI_FILTER_DETECTED: Int32 = -2147467647
EVENT_WINSOCK_CLOSESOCKET_STUCK: Int32 = -2147467646
EVENT_EQOS_INFO_MACHINE_POLICY_REFRESH_NO_CHANGE: Int32 = 1073758324
EVENT_EQOS_INFO_MACHINE_POLICY_REFRESH_WITH_CHANGE: Int32 = 1073758325
EVENT_EQOS_INFO_USER_POLICY_REFRESH_NO_CHANGE: Int32 = 1073758326
EVENT_EQOS_INFO_USER_POLICY_REFRESH_WITH_CHANGE: Int32 = 1073758327
EVENT_EQOS_INFO_TCP_AUTOTUNING_NOT_CONFIGURED: Int32 = 1073758328
EVENT_EQOS_INFO_TCP_AUTOTUNING_OFF: Int32 = 1073758329
EVENT_EQOS_INFO_TCP_AUTOTUNING_HIGHLY_RESTRICTED: Int32 = 1073758330
EVENT_EQOS_INFO_TCP_AUTOTUNING_RESTRICTED: Int32 = 1073758331
EVENT_EQOS_INFO_TCP_AUTOTUNING_NORMAL: Int32 = 1073758332
EVENT_EQOS_INFO_APP_MARKING_NOT_CONFIGURED: Int32 = 1073758333
EVENT_EQOS_INFO_APP_MARKING_IGNORED: Int32 = 1073758334
EVENT_EQOS_INFO_APP_MARKING_ALLOWED: Int32 = 1073758335
EVENT_EQOS_INFO_LOCAL_SETTING_DONT_USE_NLA: Int32 = 1073758336
EVENT_EQOS_URL_QOS_APPLICATION_CONFLICT: Int32 = 1073758337
EVENT_EQOS_WARNING_TEST_1: Int32 = -2147467048
EVENT_EQOS_WARNING_TEST_2: Int32 = -2147467047
EVENT_EQOS_WARNING_MACHINE_POLICY_VERSION: Int32 = -2147467046
EVENT_EQOS_WARNING_USER_POLICY_VERSION: Int32 = -2147467045
EVENT_EQOS_WARNING_MACHINE_POLICY_PROFILE_NOT_SPECIFIED: Int32 = -2147467044
EVENT_EQOS_WARNING_USER_POLICY_PROFILE_NOT_SPECIFIED: Int32 = -2147467043
EVENT_EQOS_WARNING_MACHINE_POLICY_QUOTA_EXCEEDED: Int32 = -2147467042
EVENT_EQOS_WARNING_USER_POLICY_QUOTA_EXCEEDED: Int32 = -2147467041
EVENT_EQOS_WARNING_MACHINE_POLICY_CONFLICT: Int32 = -2147467040
EVENT_EQOS_WARNING_USER_POLICY_CONFLICT: Int32 = -2147467039
EVENT_EQOS_WARNING_MACHINE_POLICY_NO_FULLPATH_APPNAME: Int32 = -2147467038
EVENT_EQOS_WARNING_USER_POLICY_NO_FULLPATH_APPNAME: Int32 = -2147467037
EVENT_EQOS_ERROR_MACHINE_POLICY_REFERESH: Int32 = -1073725124
EVENT_EQOS_ERROR_USER_POLICY_REFERESH: Int32 = -1073725123
EVENT_EQOS_ERROR_OPENING_MACHINE_POLICY_ROOT_KEY: Int32 = -1073725122
EVENT_EQOS_ERROR_OPENING_USER_POLICY_ROOT_KEY: Int32 = -1073725121
EVENT_EQOS_ERROR_MACHINE_POLICY_KEYNAME_TOO_LONG: Int32 = -1073725120
EVENT_EQOS_ERROR_USER_POLICY_KEYNAME_TOO_LONG: Int32 = -1073725119
EVENT_EQOS_ERROR_MACHINE_POLICY_KEYNAME_SIZE_ZERO: Int32 = -1073725118
EVENT_EQOS_ERROR_USER_POLICY_KEYNAME_SIZE_ZERO: Int32 = -1073725117
EVENT_EQOS_ERROR_OPENING_MACHINE_POLICY_SUBKEY: Int32 = -1073725116
EVENT_EQOS_ERROR_OPENING_USER_POLICY_SUBKEY: Int32 = -1073725115
EVENT_EQOS_ERROR_PROCESSING_MACHINE_POLICY_FIELD: Int32 = -1073725114
EVENT_EQOS_ERROR_PROCESSING_USER_POLICY_FIELD: Int32 = -1073725113
EVENT_EQOS_ERROR_SETTING_TCP_AUTOTUNING: Int32 = -1073725112
EVENT_EQOS_ERROR_SETTING_APP_MARKING: Int32 = -1073725111
EVENT_WINNAT_SESSION_LIMIT_REACHED: Int32 = -2147466648
HARDWARE_ADDRESS_LENGTH: UInt32 = 6
NETMAN_VARTYPE_ULONG: UInt32 = 0
NETMAN_VARTYPE_HARDWARE_ADDRESS: UInt32 = 1
NETMAN_VARTYPE_STRING: UInt32 = 2
REPL_ROLE_EXPORT: UInt32 = 1
REPL_ROLE_IMPORT: UInt32 = 2
REPL_ROLE_BOTH: UInt32 = 3
REPL_INTERVAL_INFOLEVEL: UInt32 = 1000
REPL_PULSE_INFOLEVEL: UInt32 = 1001
REPL_GUARDTIME_INFOLEVEL: UInt32 = 1002
REPL_RANDOM_INFOLEVEL: UInt32 = 1003
REPL_INTEGRITY_FILE: UInt32 = 1
REPL_INTEGRITY_TREE: UInt32 = 2
REPL_EXTENT_FILE: UInt32 = 1
REPL_EXTENT_TREE: UInt32 = 2
REPL_EXPORT_INTEGRITY_INFOLEVEL: UInt32 = 1000
REPL_EXPORT_EXTENT_INFOLEVEL: UInt32 = 1001
REPL_UNLOCK_NOFORCE: UInt32 = 0
REPL_UNLOCK_FORCE: UInt32 = 1
REPL_STATE_OK: UInt32 = 0
REPL_STATE_NO_MASTER: UInt32 = 1
REPL_STATE_NO_SYNC: UInt32 = 2
REPL_STATE_NEVER_REPLICATED: UInt32 = 3
SERVICE_WORKSTATION: String = 'LanmanWorkstation'
SERVICE_LM20_WORKSTATION: String = 'WORKSTATION'
WORKSTATION_DISPLAY_NAME: String = 'Workstation'
SERVICE_SERVER: String = 'LanmanServer'
SERVICE_LM20_SERVER: String = 'SERVER'
SERVER_DISPLAY_NAME: String = 'Server'
SERVICE_BROWSER: String = 'BROWSER'
SERVICE_LM20_BROWSER: String = 'BROWSER'
SERVICE_MESSENGER: String = 'MESSENGER'
SERVICE_LM20_MESSENGER: String = 'MESSENGER'
SERVICE_NETRUN: String = 'NETRUN'
SERVICE_LM20_NETRUN: String = 'NETRUN'
SERVICE_SPOOLER: String = 'SPOOLER'
SERVICE_LM20_SPOOLER: String = 'SPOOLER'
SERVICE_ALERTER: String = 'ALERTER'
SERVICE_LM20_ALERTER: String = 'ALERTER'
SERVICE_NETLOGON: String = 'NETLOGON'
SERVICE_LM20_NETLOGON: String = 'NETLOGON'
SERVICE_NETPOPUP: String = 'NETPOPUP'
SERVICE_LM20_NETPOPUP: String = 'NETPOPUP'
SERVICE_SQLSERVER: String = 'SQLSERVER'
SERVICE_LM20_SQLSERVER: String = 'SQLSERVER'
SERVICE_REPL: String = 'REPLICATOR'
SERVICE_LM20_REPL: String = 'REPLICATOR'
SERVICE_RIPL: String = 'REMOTEBOOT'
SERVICE_LM20_RIPL: String = 'REMOTEBOOT'
SERVICE_TIMESOURCE: String = 'TIMESOURCE'
SERVICE_LM20_TIMESOURCE: String = 'TIMESOURCE'
SERVICE_AFP: String = 'AFP'
SERVICE_LM20_AFP: String = 'AFP'
SERVICE_UPS: String = 'UPS'
SERVICE_LM20_UPS: String = 'UPS'
SERVICE_XACTSRV: String = 'XACTSRV'
SERVICE_LM20_XACTSRV: String = 'XACTSRV'
SERVICE_TCPIP: String = 'TCPIP'
SERVICE_LM20_TCPIP: String = 'TCPIP'
SERVICE_NBT: String = 'NBT'
SERVICE_LM20_NBT: String = 'NBT'
SERVICE_LMHOSTS: String = 'LMHOSTS'
SERVICE_LM20_LMHOSTS: String = 'LMHOSTS'
SERVICE_TELNET: String = 'Telnet'
SERVICE_LM20_TELNET: String = 'Telnet'
SERVICE_SCHEDULE: String = 'Schedule'
SERVICE_LM20_SCHEDULE: String = 'Schedule'
SERVICE_NTLMSSP: String = 'NtLmSsp'
SERVICE_DHCP: String = 'DHCP'
SERVICE_LM20_DHCP: String = 'DHCP'
SERVICE_NWSAP: String = 'NwSapAgent'
SERVICE_LM20_NWSAP: String = 'NwSapAgent'
NWSAP_DISPLAY_NAME: String = 'NW Sap Agent'
SERVICE_NWCS: String = 'NWCWorkstation'
SERVICE_DNS_CACHE: String = 'DnsCache'
SERVICE_W32TIME: String = 'w32time'
SERVCE_LM20_W32TIME: String = 'w32time'
SERVICE_KDC: String = 'kdc'
SERVICE_LM20_KDC: String = 'kdc'
SERVICE_RPCLOCATOR: String = 'RPCLOCATOR'
SERVICE_LM20_RPCLOCATOR: String = 'RPCLOCATOR'
SERVICE_TRKSVR: String = 'TrkSvr'
SERVICE_LM20_TRKSVR: String = 'TrkSvr'
SERVICE_TRKWKS: String = 'TrkWks'
SERVICE_LM20_TRKWKS: String = 'TrkWks'
SERVICE_NTFRS: String = 'NtFrs'
SERVICE_LM20_NTFRS: String = 'NtFrs'
SERVICE_ISMSERV: String = 'IsmServ'
SERVICE_LM20_ISMSERV: String = 'IsmServ'
SERVICE_NTDS: String = 'NTDS'
SERVICE_LM20_NTDS: String = 'NTDS'
SERVICE_ADWS: String = 'ADWS'
SERVICE_DSROLE: String = 'DsRoleSvc'
SERVICE_LM20_DSROLE: String = 'DsRoleSvc'
NETCFG_E_ALREADY_INITIALIZED: win32more.Foundation.HRESULT = -2147180512
NETCFG_E_NOT_INITIALIZED: win32more.Foundation.HRESULT = -2147180511
NETCFG_E_IN_USE: win32more.Foundation.HRESULT = -2147180510
NETCFG_E_NO_WRITE_LOCK: win32more.Foundation.HRESULT = -2147180508
NETCFG_E_NEED_REBOOT: win32more.Foundation.HRESULT = -2147180507
NETCFG_E_ACTIVE_RAS_CONNECTIONS: win32more.Foundation.HRESULT = -2147180506
NETCFG_E_ADAPTER_NOT_FOUND: win32more.Foundation.HRESULT = -2147180505
NETCFG_E_COMPONENT_REMOVED_PENDING_REBOOT: win32more.Foundation.HRESULT = -2147180504
NETCFG_E_MAX_FILTER_LIMIT: win32more.Foundation.HRESULT = -2147180503
NETCFG_E_VMSWITCH_ACTIVE_OVER_ADAPTER: win32more.Foundation.HRESULT = -2147180502
NETCFG_E_DUPLICATE_INSTANCEID: win32more.Foundation.HRESULT = -2147180501
NETCFG_S_REBOOT: win32more.Foundation.HRESULT = 303136
NETCFG_S_DISABLE_QUERY: win32more.Foundation.HRESULT = 303138
NETCFG_S_STILL_REFERENCED: win32more.Foundation.HRESULT = 303139
NETCFG_S_CAUSED_SETUP_CHANGE: win32more.Foundation.HRESULT = 303140
NETCFG_S_COMMIT_NOW: win32more.Foundation.HRESULT = 303141
NETCFG_CLIENT_CID_MS_MSClient: String = 'ms_msclient'
NETCFG_SERVICE_CID_MS_SERVER: String = 'ms_server'
NETCFG_SERVICE_CID_MS_NETBIOS: String = 'ms_netbios'
NETCFG_SERVICE_CID_MS_PSCHED: String = 'ms_pschedpc'
NETCFG_SERVICE_CID_MS_WLBS: String = 'ms_wlbs'
NETCFG_TRANS_CID_MS_APPLETALK: String = 'ms_appletalk'
NETCFG_TRANS_CID_MS_NETBEUI: String = 'ms_netbeui'
NETCFG_TRANS_CID_MS_NETMON: String = 'ms_netmon'
NETCFG_TRANS_CID_MS_NWIPX: String = 'ms_nwipx'
NETCFG_TRANS_CID_MS_NWSPX: String = 'ms_nwspx'
NETCFG_TRANS_CID_MS_TCPIP: String = 'ms_tcpip'
WZC_PROFILE_SUCCESS: UInt32 = 0
WZC_PROFILE_XML_ERROR_NO_VERSION: UInt32 = 1
WZC_PROFILE_XML_ERROR_BAD_VERSION: UInt32 = 2
WZC_PROFILE_XML_ERROR_UNSUPPORTED_VERSION: UInt32 = 3
WZC_PROFILE_XML_ERROR_SSID_NOT_FOUND: UInt32 = 4
WZC_PROFILE_XML_ERROR_BAD_SSID: UInt32 = 5
WZC_PROFILE_XML_ERROR_CONNECTION_TYPE: UInt32 = 6
WZC_PROFILE_XML_ERROR_AUTHENTICATION: UInt32 = 7
WZC_PROFILE_XML_ERROR_ENCRYPTION: UInt32 = 8
WZC_PROFILE_XML_ERROR_KEY_PROVIDED_AUTOMATICALLY: UInt32 = 9
WZC_PROFILE_XML_ERROR_1X_ENABLED: UInt32 = 10
WZC_PROFILE_XML_ERROR_EAP_METHOD: UInt32 = 11
WZC_PROFILE_XML_ERROR_BAD_KEY_INDEX: UInt32 = 12
WZC_PROFILE_XML_ERROR_KEY_INDEX_RANGE: UInt32 = 13
WZC_PROFILE_XML_ERROR_BAD_NETWORK_KEY: UInt32 = 14
WZC_PROFILE_CONFIG_ERROR_INVALID_AUTH_FOR_CONNECTION_TYPE: UInt32 = 15
WZC_PROFILE_CONFIG_ERROR_INVALID_ENCRYPTION_FOR_AUTHMODE: UInt32 = 16
WZC_PROFILE_CONFIG_ERROR_KEY_REQUIRED: UInt32 = 17
WZC_PROFILE_CONFIG_ERROR_KEY_INDEX_REQUIRED: UInt32 = 18
WZC_PROFILE_CONFIG_ERROR_KEY_INDEX_NOT_APPLICABLE: UInt32 = 19
WZC_PROFILE_CONFIG_ERROR_1X_NOT_ALLOWED: UInt32 = 20
WZC_PROFILE_CONFIG_ERROR_1X_NOT_ALLOWED_KEY_REQUIRED: UInt32 = 21
WZC_PROFILE_CONFIG_ERROR_1X_NOT_ENABLED_KEY_PROVIDED: UInt32 = 22
WZC_PROFILE_CONFIG_ERROR_EAP_METHOD_REQUIRED: UInt32 = 23
WZC_PROFILE_CONFIG_ERROR_EAP_METHOD_NOT_APPLICABLE: UInt32 = 24
WZC_PROFILE_CONFIG_ERROR_WPA_NOT_SUPPORTED: UInt32 = 25
WZC_PROFILE_CONFIG_ERROR_WPA_ENCRYPTION_NOT_SUPPORTED: UInt32 = 26
WZC_PROFILE_SET_ERROR_DUPLICATE_NETWORK: UInt32 = 27
WZC_PROFILE_SET_ERROR_MEMORY_ALLOCATION: UInt32 = 28
WZC_PROFILE_SET_ERROR_READING_1X_CONFIG: UInt32 = 29
WZC_PROFILE_SET_ERROR_WRITING_1X_CONFIG: UInt32 = 30
WZC_PROFILE_SET_ERROR_WRITING_WZC_CFG: UInt32 = 31
WZC_PROFILE_API_ERROR_NOT_SUPPORTED: UInt32 = 32
WZC_PROFILE_API_ERROR_FAILED_TO_LOAD_XML: UInt32 = 33
WZC_PROFILE_API_ERROR_FAILED_TO_LOAD_SCHEMA: UInt32 = 34
WZC_PROFILE_API_ERROR_XML_VALIDATION_FAILED: UInt32 = 35
WZC_PROFILE_API_ERROR_INTERNAL: UInt32 = 36
RF_ROUTING: UInt32 = 1
RF_ROUTINGV6: UInt32 = 2
RF_DEMAND_UPDATE_ROUTES: UInt32 = 4
RF_ADD_ALL_INTERFACES: UInt32 = 16
RF_MULTICAST: UInt32 = 32
RF_POWER: UInt32 = 64
MS_ROUTER_VERSION: UInt32 = 1536
ROUTING_DOMAIN_INFO_REVISION_1: UInt32 = 1
INTERFACE_INFO_REVISION_1: UInt32 = 1
IR_PROMISCUOUS: UInt32 = 0
IR_PROMISCUOUS_MULTICAST: UInt32 = 1
PROTO_IP_MSDP: UInt32 = 9
PROTO_IP_IGMP: UInt32 = 10
PROTO_IP_BGMP: UInt32 = 11
PROTO_IP_VRRP: UInt32 = 112
PROTO_IP_BOOTP: UInt32 = 9999
PROTO_IPV6_DHCP: UInt32 = 999
PROTO_IP_DNS_PROXY: UInt32 = 10003
PROTO_IP_DHCP_ALLOCATOR: UInt32 = 10004
PROTO_IP_NAT: UInt32 = 10005
PROTO_IP_DIFFSERV: UInt32 = 10008
PROTO_IP_MGM: UInt32 = 10009
PROTO_IP_ALG: UInt32 = 10010
PROTO_IP_H323: UInt32 = 10011
PROTO_IP_FTP: UInt32 = 10012
PROTO_IP_DTP: UInt32 = 10013
PROTO_TYPE_UCAST: UInt32 = 0
PROTO_TYPE_MCAST: UInt32 = 1
PROTO_TYPE_MS0: UInt32 = 2
PROTO_TYPE_MS1: UInt32 = 3
PROTO_VENDOR_MS0: UInt32 = 0
PROTO_VENDOR_MS1: UInt32 = 311
PROTO_VENDOR_MS2: UInt32 = 16383
IPX_PROTOCOL_BASE: UInt32 = 131071
IPX_PROTOCOL_RIP: UInt32 = 131072
RIS_INTERFACE_ADDRESS_CHANGE: UInt32 = 0
RIS_INTERFACE_ENABLED: UInt32 = 1
RIS_INTERFACE_DISABLED: UInt32 = 2
RIS_INTERFACE_MEDIA_PRESENT: UInt32 = 3
RIS_INTERFACE_MEDIA_ABSENT: UInt32 = 4
MRINFO_TUNNEL_FLAG: UInt32 = 1
MRINFO_PIM_FLAG: UInt32 = 4
MRINFO_DOWN_FLAG: UInt32 = 16
MRINFO_DISABLED_FLAG: UInt32 = 32
MRINFO_QUERIER_FLAG: UInt32 = 64
MRINFO_LEAF_FLAG: UInt32 = 128
MFE_NO_ERROR: UInt32 = 0
MFE_REACHED_CORE: UInt32 = 1
MFE_OIF_PRUNED: UInt32 = 5
MFE_PRUNED_UPSTREAM: UInt32 = 4
MFE_OLD_ROUTER: UInt32 = 11
MFE_NOT_FORWARDING: UInt32 = 2
MFE_WRONG_IF: UInt32 = 3
MFE_BOUNDARY_REACHED: UInt32 = 6
MFE_NO_MULTICAST: UInt32 = 7
MFE_IIF: UInt32 = 8
MFE_NO_ROUTE: UInt32 = 9
MFE_NOT_LAST_HOP: UInt32 = 10
MFE_PROHIBITED: UInt32 = 12
MFE_NO_SPACE: UInt32 = 13
REGISTER_PROTOCOL_ENTRY_POINT_STRING: String = 'RegisterProtocol'
ALIGN_SIZE: UInt32 = 8
RTR_INFO_BLOCK_VERSION: UInt32 = 1
TRACE_USE_FILE: UInt32 = 1
TRACE_USE_CONSOLE: UInt32 = 2
TRACE_NO_SYNCH: UInt32 = 4
TRACE_NO_STDINFO: UInt32 = 1
TRACE_USE_MASK: UInt32 = 2
TRACE_USE_MSEC: UInt32 = 4
TRACE_USE_DATE: UInt32 = 8
INVALID_TRACEID: UInt32 = 4294967295
RTUTILS_MAX_PROTOCOL_NAME_LEN: UInt32 = 40
RTUTILS_MAX_PROTOCOL_DLL_LEN: UInt32 = 48
MAX_PROTOCOL_NAME_LEN: UInt32 = 40
MAX_PROTOCOL_DLL_LEN: UInt32 = 48
@winfunctype('NETAPI32.dll')
def NetUserAdd(servername: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserEnum(servername: win32more.Foundation.PWSTR, level: UInt32, filter: win32more.NetworkManagement.NetManagement.NET_USER_ENUM_FILTER_FLAGS, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserGetInfo(servername: win32more.Foundation.PWSTR, username: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserSetInfo(servername: win32more.Foundation.PWSTR, username: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserDel(servername: win32more.Foundation.PWSTR, username: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserGetGroups(servername: win32more.Foundation.PWSTR, username: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserSetGroups(servername: win32more.Foundation.PWSTR, username: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, num_entries: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserGetLocalGroups(servername: win32more.Foundation.PWSTR, username: win32more.Foundation.PWSTR, level: UInt32, flags: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserModalsGet(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserModalsSet(servername: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserChangePassword(domainname: win32more.Foundation.PWSTR, username: win32more.Foundation.PWSTR, oldpassword: win32more.Foundation.PWSTR, newpassword: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupAdd(servername: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupAddUser(servername: win32more.Foundation.PWSTR, GroupName: win32more.Foundation.PWSTR, username: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupEnum(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupGetInfo(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupSetInfo(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupDel(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupDelUser(servername: win32more.Foundation.PWSTR, GroupName: win32more.Foundation.PWSTR, Username: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupGetUsers(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), ResumeHandle: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupSetUsers(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, totalentries: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupAdd(servername: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupAddMember(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR, membersid: win32more.Foundation.PSID) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupEnum(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupGetInfo(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupSetInfo(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupDel(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupDelMember(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR, membersid: win32more.Foundation.PSID) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupGetMembers(servername: win32more.Foundation.PWSTR, localgroupname: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupSetMembers(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, totalentries: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupAddMembers(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, totalentries: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupDelMembers(servername: win32more.Foundation.PWSTR, groupname: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, totalentries: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetQueryDisplayInformation(ServerName: win32more.Foundation.PWSTR, Level: UInt32, Index: UInt32, EntriesRequested: UInt32, PreferredMaximumLength: UInt32, ReturnedEntryCount: POINTER(UInt32), SortedBuffer: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGetDisplayInformationIndex(ServerName: win32more.Foundation.PWSTR, Level: UInt32, Prefix: win32more.Foundation.PWSTR, Index: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessAdd(servername: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessEnum(servername: win32more.Foundation.PWSTR, BasePath: win32more.Foundation.PWSTR, Recursive: UInt32, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessGetInfo(servername: win32more.Foundation.PWSTR, resource: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessSetInfo(servername: win32more.Foundation.PWSTR, resource: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessDel(servername: win32more.Foundation.PWSTR, resource: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessGetUserPerms(servername: win32more.Foundation.PWSTR, UGname: win32more.Foundation.PWSTR, resource: win32more.Foundation.PWSTR, Perms: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetValidatePasswordPolicy(ServerName: win32more.Foundation.PWSTR, Qualifier: c_void_p, ValidationType: win32more.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_TYPE, InputArg: c_void_p, OutputArg: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetValidatePasswordPolicyFree(OutputArg: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGetDCName(ServerName: win32more.Foundation.PWSTR, DomainName: win32more.Foundation.PWSTR, Buffer: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGetAnyDCName(ServerName: win32more.Foundation.PWSTR, DomainName: win32more.Foundation.PWSTR, Buffer: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def I_NetLogonControl2(ServerName: win32more.Foundation.PWSTR, FunctionCode: UInt32, QueryLevel: UInt32, Data: c_char_p_no, Buffer: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAddServiceAccount(ServerName: win32more.Foundation.PWSTR, AccountName: win32more.Foundation.PWSTR, Password: win32more.Foundation.PWSTR, Flags: UInt32) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('NETAPI32.dll')
def NetRemoveServiceAccount(ServerName: win32more.Foundation.PWSTR, AccountName: win32more.Foundation.PWSTR, Flags: UInt32) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('NETAPI32.dll')
def NetEnumerateServiceAccounts(ServerName: win32more.Foundation.PWSTR, Flags: UInt32, AccountsCount: POINTER(UInt32), Accounts: POINTER(POINTER(POINTER(UInt16)))) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('NETAPI32.dll')
def NetIsServiceAccount(ServerName: win32more.Foundation.PWSTR, AccountName: win32more.Foundation.PWSTR, IsService: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('NETAPI32.dll')
def NetQueryServiceAccount(ServerName: win32more.Foundation.PWSTR, AccountName: win32more.Foundation.PWSTR, InfoLevel: UInt32, Buffer: POINTER(c_char_p_no)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('NETAPI32.dll')
def NetAlertRaise(AlertType: win32more.Foundation.PWSTR, Buffer: c_void_p, BufferSize: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAlertRaiseEx(AlertType: win32more.Foundation.PWSTR, VariableInfo: c_void_p, VariableInfoSize: UInt32, ServiceName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetMessageNameAdd(servername: win32more.Foundation.PWSTR, msgname: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetMessageNameEnum(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetMessageNameGetInfo(servername: win32more.Foundation.PWSTR, msgname: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetMessageNameDel(servername: win32more.Foundation.PWSTR, msgname: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetMessageBufferSend(servername: win32more.Foundation.PWSTR, msgname: win32more.Foundation.PWSTR, fromname: win32more.Foundation.PWSTR, buf: c_char_p_no, buflen: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRemoteTOD(UncServerName: win32more.Foundation.PWSTR, BufferPtr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRemoteComputerSupports(UncServerName: win32more.Foundation.PWSTR, OptionsWanted: win32more.NetworkManagement.NetManagement.NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS, OptionsSupported: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplGetInfo(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplSetInfo(servername: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirAdd(servername: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirDel(servername: win32more.Foundation.PWSTR, dirname: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirEnum(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirGetInfo(servername: win32more.Foundation.PWSTR, dirname: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirSetInfo(servername: win32more.Foundation.PWSTR, dirname: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirLock(servername: win32more.Foundation.PWSTR, dirname: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirUnlock(servername: win32more.Foundation.PWSTR, dirname: win32more.Foundation.PWSTR, unlockforce: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirAdd(servername: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirDel(servername: win32more.Foundation.PWSTR, dirname: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirEnum(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirGetInfo(servername: win32more.Foundation.PWSTR, dirname: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirLock(servername: win32more.Foundation.PWSTR, dirname: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirUnlock(servername: win32more.Foundation.PWSTR, dirname: win32more.Foundation.PWSTR, unlockforce: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerEnum(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), servertype: win32more.NetworkManagement.NetManagement.NET_SERVER_TYPE, domain: win32more.Foundation.PWSTR, resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerGetInfo(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerSetInfo(servername: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, ParmError: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerDiskEnum(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerComputerNameAdd(ServerName: win32more.Foundation.PWSTR, EmulatedDomainName: win32more.Foundation.PWSTR, EmulatedServerName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerComputerNameDel(ServerName: win32more.Foundation.PWSTR, EmulatedServerName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerTransportAdd(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: c_char_p_no) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerTransportAddEx(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: c_char_p_no) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerTransportDel(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: c_char_p_no) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerTransportEnum(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServiceControl(servername: win32more.Foundation.PWSTR, service: win32more.Foundation.PWSTR, opcode: UInt32, arg: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServiceEnum(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServiceGetInfo(servername: win32more.Foundation.PWSTR, service: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServiceInstall(servername: win32more.Foundation.PWSTR, service: win32more.Foundation.PWSTR, argc: UInt32, argv: POINTER(win32more.Foundation.PWSTR), bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUseAdd(servername: POINTER(SByte), LevelFlags: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUseDel(UncServerName: win32more.Foundation.PWSTR, UseName: win32more.Foundation.PWSTR, ForceLevelFlags: win32more.NetworkManagement.NetManagement.FORCE_LEVEL_FLAGS) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUseEnum(UncServerName: win32more.Foundation.PWSTR, LevelFlags: UInt32, BufPtr: POINTER(c_char_p_no), PreferedMaximumSize: UInt32, EntriesRead: POINTER(UInt32), TotalEntries: POINTER(UInt32), ResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUseGetInfo(UncServerName: win32more.Foundation.PWSTR, UseName: win32more.Foundation.PWSTR, LevelFlags: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaGetInfo(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaSetInfo(servername: win32more.Foundation.PWSTR, level: UInt32, buffer: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaUserGetInfo(reserved: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaUserSetInfo(reserved: win32more.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaUserEnum(servername: win32more.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaTransportAdd(servername: POINTER(SByte), level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaTransportDel(servername: win32more.Foundation.PWSTR, transportname: win32more.Foundation.PWSTR, ucond: win32more.NetworkManagement.NetManagement.FORCE_LEVEL_FLAGS) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaTransportEnum(servername: POINTER(SByte), level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetApiBufferAllocate(ByteCount: UInt32, Buffer: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetApiBufferFree(Buffer: c_void_p) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetApiBufferReallocate(OldBuffer: c_void_p, NewByteCount: UInt32, NewBuffer: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetApiBufferSize(Buffer: c_void_p, ByteCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetErrorLogClear(UncServerName: win32more.Foundation.PWSTR, BackupFile: win32more.Foundation.PWSTR, Reserved: c_char_p_no) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetErrorLogRead(UncServerName: win32more.Foundation.PWSTR, Reserved1: win32more.Foundation.PWSTR, ErrorLogHandle: POINTER(win32more.NetworkManagement.NetManagement.HLOG_head), Offset: UInt32, Reserved2: POINTER(UInt32), Reserved3: UInt32, OffsetFlag: UInt32, BufPtr: POINTER(c_char_p_no), PrefMaxSize: UInt32, BytesRead: POINTER(UInt32), TotalAvailable: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetErrorLogWrite(Reserved1: c_char_p_no, Code: UInt32, Component: win32more.Foundation.PWSTR, Buffer: c_char_p_no, NumBytes: UInt32, MsgBuf: c_char_p_no, StrCount: UInt32, Reserved2: c_char_p_no) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetConfigGet(server: win32more.Foundation.PWSTR, component: win32more.Foundation.PWSTR, parameter: win32more.Foundation.PWSTR, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetConfigGetAll(server: win32more.Foundation.PWSTR, component: win32more.Foundation.PWSTR, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetConfigSet(server: win32more.Foundation.PWSTR, reserved1: win32more.Foundation.PWSTR, component: win32more.Foundation.PWSTR, level: UInt32, reserved2: UInt32, buf: c_char_p_no, reserved3: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAuditClear(server: win32more.Foundation.PWSTR, backupfile: win32more.Foundation.PWSTR, service: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAuditRead(server: win32more.Foundation.PWSTR, service: win32more.Foundation.PWSTR, auditloghandle: POINTER(win32more.NetworkManagement.NetManagement.HLOG_head), offset: UInt32, reserved1: POINTER(UInt32), reserved2: UInt32, offsetflag: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, bytesread: POINTER(UInt32), totalavailable: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAuditWrite(type: UInt32, buf: c_char_p_no, numbytes: UInt32, service: win32more.Foundation.PWSTR, reserved: c_char_p_no) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetJoinDomain(lpServer: win32more.Foundation.PWSTR, lpDomain: win32more.Foundation.PWSTR, lpMachineAccountOU: win32more.Foundation.PWSTR, lpAccount: win32more.Foundation.PWSTR, lpPassword: win32more.Foundation.PWSTR, fJoinOptions: win32more.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUnjoinDomain(lpServer: win32more.Foundation.PWSTR, lpAccount: win32more.Foundation.PWSTR, lpPassword: win32more.Foundation.PWSTR, fUnjoinOptions: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRenameMachineInDomain(lpServer: win32more.Foundation.PWSTR, lpNewMachineName: win32more.Foundation.PWSTR, lpAccount: win32more.Foundation.PWSTR, lpPassword: win32more.Foundation.PWSTR, fRenameOptions: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetValidateName(lpServer: win32more.Foundation.PWSTR, lpName: win32more.Foundation.PWSTR, lpAccount: win32more.Foundation.PWSTR, lpPassword: win32more.Foundation.PWSTR, NameType: win32more.NetworkManagement.NetManagement.NETSETUP_NAME_TYPE) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGetJoinableOUs(lpServer: win32more.Foundation.PWSTR, lpDomain: win32more.Foundation.PWSTR, lpAccount: win32more.Foundation.PWSTR, lpPassword: win32more.Foundation.PWSTR, OUCount: POINTER(UInt32), OUs: POINTER(POINTER(win32more.Foundation.PWSTR))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAddAlternateComputerName(Server: win32more.Foundation.PWSTR, AlternateName: win32more.Foundation.PWSTR, DomainAccount: win32more.Foundation.PWSTR, DomainAccountPassword: win32more.Foundation.PWSTR, Reserved: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRemoveAlternateComputerName(Server: win32more.Foundation.PWSTR, AlternateName: win32more.Foundation.PWSTR, DomainAccount: win32more.Foundation.PWSTR, DomainAccountPassword: win32more.Foundation.PWSTR, Reserved: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetSetPrimaryComputerName(Server: win32more.Foundation.PWSTR, PrimaryName: win32more.Foundation.PWSTR, DomainAccount: win32more.Foundation.PWSTR, DomainAccountPassword: win32more.Foundation.PWSTR, Reserved: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetEnumerateComputerNames(Server: win32more.Foundation.PWSTR, NameType: win32more.NetworkManagement.NetManagement.NET_COMPUTER_NAME_TYPE, Reserved: UInt32, EntryCount: POINTER(UInt32), ComputerNames: POINTER(POINTER(win32more.Foundation.PWSTR))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetProvisionComputerAccount(lpDomain: win32more.Foundation.PWSTR, lpMachineName: win32more.Foundation.PWSTR, lpMachineAccountOU: win32more.Foundation.PWSTR, lpDcName: win32more.Foundation.PWSTR, dwOptions: win32more.NetworkManagement.NetManagement.NETSETUP_PROVISION, pProvisionBinData: POINTER(c_char_p_no), pdwProvisionBinDataSize: POINTER(UInt32), pProvisionTextData: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRequestOfflineDomainJoin(pProvisionBinData: c_char_p_no, cbProvisionBinDataSize: UInt32, dwOptions: win32more.NetworkManagement.NetManagement.NET_REQUEST_PROVISION_OPTIONS, lpWindowsPath: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetCreateProvisioningPackage(pProvisioningParams: POINTER(win32more.NetworkManagement.NetManagement.NETSETUP_PROVISIONING_PARAMS_head), ppPackageBinData: POINTER(c_char_p_no), pdwPackageBinDataSize: POINTER(UInt32), ppPackageTextData: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRequestProvisioningPackageInstall(pPackageBinData: c_char_p_no, dwPackageBinDataSize: UInt32, dwProvisionOptions: win32more.NetworkManagement.NetManagement.NET_REQUEST_PROVISION_OPTIONS, lpWindowsPath: win32more.Foundation.PWSTR, pvReserved: c_void_p) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGetAadJoinInformation(pcszTenantId: win32more.Foundation.PWSTR, ppJoinInfo: POINTER(POINTER(win32more.NetworkManagement.NetManagement.DSREG_JOIN_INFO_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('NETAPI32.dll')
def NetFreeAadJoinInformation(pJoinInfo: POINTER(win32more.NetworkManagement.NetManagement.DSREG_JOIN_INFO_head)) -> Void: ...
@winfunctype('NETAPI32.dll')
def NetGetJoinInformation(lpServer: win32more.Foundation.PWSTR, lpNameBuffer: POINTER(win32more.Foundation.PWSTR), BufferType: POINTER(win32more.NetworkManagement.NetManagement.NETSETUP_JOIN_STATUS)) -> UInt32: ...
@winfunctype('mstask.dll')
def GetNetScheduleAccountInformation(pwszServerName: win32more.Foundation.PWSTR, ccAccount: UInt32, wszAccount: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('mstask.dll')
def SetNetScheduleAccountInformation(pwszServerName: win32more.Foundation.PWSTR, pwszAccount: win32more.Foundation.PWSTR, pwszPassword: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('NETAPI32.dll')
def NetScheduleJobAdd(Servername: win32more.Foundation.PWSTR, Buffer: c_char_p_no, JobId: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetScheduleJobDel(Servername: win32more.Foundation.PWSTR, MinJobId: UInt32, MaxJobId: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetScheduleJobEnum(Servername: win32more.Foundation.PWSTR, PointerToBuffer: POINTER(c_char_p_no), PrefferedMaximumLength: UInt32, EntriesRead: POINTER(UInt32), TotalEntries: POINTER(UInt32), ResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetScheduleJobGetInfo(Servername: win32more.Foundation.PWSTR, JobId: UInt32, PointerToBuffer: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceRegisterExA(lpszCallerName: win32more.Foundation.PSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceDeregisterA(dwTraceID: UInt32) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceDeregisterExA(dwTraceID: UInt32, dwFlags: UInt32) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceGetConsoleA(dwTraceID: UInt32, lphConsole: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@cfunctype('rtutils.dll')
def TracePrintfA(dwTraceID: UInt32, lpszFormat: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('rtutils.dll')
def TracePrintfExA(dwTraceID: UInt32, dwFlags: UInt32, lpszFormat: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceVprintfExA(dwTraceID: UInt32, dwFlags: UInt32, lpszFormat: win32more.Foundation.PSTR, arglist: POINTER(SByte)) -> UInt32: ...
@winfunctype('rtutils.dll')
def TracePutsExA(dwTraceID: UInt32, dwFlags: UInt32, lpszString: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceDumpExA(dwTraceID: UInt32, dwFlags: UInt32, lpbBytes: c_char_p_no, dwByteCount: UInt32, dwGroupSize: UInt32, bAddressPrefix: win32more.Foundation.BOOL, lpszPrefix: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceRegisterExW(lpszCallerName: win32more.Foundation.PWSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceDeregisterW(dwTraceID: UInt32) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceDeregisterExW(dwTraceID: UInt32, dwFlags: UInt32) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceGetConsoleW(dwTraceID: UInt32, lphConsole: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@cfunctype('rtutils.dll')
def TracePrintfW(dwTraceID: UInt32, lpszFormat: win32more.Foundation.PWSTR) -> UInt32: ...
@cfunctype('rtutils.dll')
def TracePrintfExW(dwTraceID: UInt32, dwFlags: UInt32, lpszFormat: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceVprintfExW(dwTraceID: UInt32, dwFlags: UInt32, lpszFormat: win32more.Foundation.PWSTR, arglist: POINTER(SByte)) -> UInt32: ...
@winfunctype('rtutils.dll')
def TracePutsExW(dwTraceID: UInt32, dwFlags: UInt32, lpszString: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceDumpExW(dwTraceID: UInt32, dwFlags: UInt32, lpbBytes: c_char_p_no, dwByteCount: UInt32, dwGroupSize: UInt32, bAddressPrefix: win32more.Foundation.BOOL, lpszPrefix: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('rtutils.dll')
def LogErrorA(dwMessageId: UInt32, cNumberOfSubStrings: UInt32, plpwsSubStrings: POINTER(win32more.Foundation.PSTR), dwErrorCode: UInt32) -> Void: ...
@winfunctype('rtutils.dll')
def LogEventA(wEventType: UInt32, dwMessageId: UInt32, cNumberOfSubStrings: UInt32, plpwsSubStrings: POINTER(win32more.Foundation.PSTR)) -> Void: ...
@winfunctype('rtutils.dll')
def LogErrorW(dwMessageId: UInt32, cNumberOfSubStrings: UInt32, plpwsSubStrings: POINTER(win32more.Foundation.PWSTR), dwErrorCode: UInt32) -> Void: ...
@winfunctype('rtutils.dll')
def LogEventW(wEventType: UInt32, dwMessageId: UInt32, cNumberOfSubStrings: UInt32, plpwsSubStrings: POINTER(win32more.Foundation.PWSTR)) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogRegisterA(lpszSource: win32more.Foundation.PSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('rtutils.dll')
def RouterLogDeregisterA(hLogHandle: win32more.Foundation.HANDLE) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventA(hLogHandle: win32more.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Foundation.PSTR), dwErrorCode: UInt32) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventDataA(hLogHandle: win32more.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Foundation.PSTR), dwDataBytes: UInt32, lpDataBytes: c_char_p_no) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventStringA(hLogHandle: win32more.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Foundation.PSTR), dwErrorCode: UInt32, dwErrorIndex: UInt32) -> Void: ...
@cfunctype('rtutils.dll')
def RouterLogEventExA(hLogHandle: win32more.Foundation.HANDLE, dwEventType: UInt32, dwErrorCode: UInt32, dwMessageId: UInt32, ptszFormat: win32more.Foundation.PSTR) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventValistExA(hLogHandle: win32more.Foundation.HANDLE, dwEventType: UInt32, dwErrorCode: UInt32, dwMessageId: UInt32, ptszFormat: win32more.Foundation.PSTR, arglist: POINTER(SByte)) -> Void: ...
@winfunctype('rtutils.dll')
def RouterGetErrorStringA(dwErrorCode: UInt32, lplpszErrorString: POINTER(win32more.Foundation.PSTR)) -> UInt32: ...
@winfunctype('rtutils.dll')
def RouterLogRegisterW(lpszSource: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('rtutils.dll')
def RouterLogDeregisterW(hLogHandle: win32more.Foundation.HANDLE) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventW(hLogHandle: win32more.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Foundation.PWSTR), dwErrorCode: UInt32) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventDataW(hLogHandle: win32more.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Foundation.PWSTR), dwDataBytes: UInt32, lpDataBytes: c_char_p_no) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventStringW(hLogHandle: win32more.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Foundation.PWSTR), dwErrorCode: UInt32, dwErrorIndex: UInt32) -> Void: ...
@cfunctype('rtutils.dll')
def RouterLogEventExW(hLogHandle: win32more.Foundation.HANDLE, dwEventType: UInt32, dwErrorCode: UInt32, dwMessageId: UInt32, ptszFormat: win32more.Foundation.PWSTR) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventValistExW(hLogHandle: win32more.Foundation.HANDLE, dwEventType: UInt32, dwErrorCode: UInt32, dwMessageId: UInt32, ptszFormat: win32more.Foundation.PWSTR, arglist: POINTER(SByte)) -> Void: ...
@winfunctype('rtutils.dll')
def RouterGetErrorStringW(dwErrorCode: UInt32, lplpwszErrorString: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('rtutils.dll')
def RouterAssert(pszFailedAssertion: win32more.Foundation.PSTR, pszFileName: win32more.Foundation.PSTR, dwLineNumber: UInt32, pszMessage: win32more.Foundation.PSTR) -> Void: ...
@winfunctype('rtutils.dll')
def MprSetupProtocolEnum(dwTransportId: UInt32, lplpBuffer: POINTER(c_char_p_no), lpdwEntriesRead: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rtutils.dll')
def MprSetupProtocolFree(lpBuffer: c_void_p) -> UInt32: ...
class AT_ENUM(Structure):
    JobId: UInt32
    JobTime: UIntPtr
    DaysOfMonth: UInt32
    DaysOfWeek: Byte
    Flags: Byte
    Command: win32more.Foundation.PWSTR
class AT_INFO(Structure):
    JobTime: UIntPtr
    DaysOfMonth: UInt32
    DaysOfWeek: Byte
    Flags: Byte
    Command: win32more.Foundation.PWSTR
class AUDIT_ENTRY(Structure):
    ae_len: UInt32
    ae_reserved: UInt32
    ae_time: UInt32
    ae_type: UInt32
    ae_data_offset: UInt32
    ae_data_size: UInt32
BIND_FLAGS1 = Int32
NCN_ADD: BIND_FLAGS1 = 1
NCN_REMOVE: BIND_FLAGS1 = 2
NCN_UPDATE: BIND_FLAGS1 = 4
NCN_ENABLE: BIND_FLAGS1 = 16
NCN_DISABLE: BIND_FLAGS1 = 32
NCN_BINDING_PATH: BIND_FLAGS1 = 256
NCN_PROPERTYCHANGE: BIND_FLAGS1 = 512
NCN_NET: BIND_FLAGS1 = 65536
NCN_NETTRANS: BIND_FLAGS1 = 131072
NCN_NETCLIENT: BIND_FLAGS1 = 262144
NCN_NETSERVICE: BIND_FLAGS1 = 524288
COMPONENT_CHARACTERISTICS = Int32
NCF_VIRTUAL: COMPONENT_CHARACTERISTICS = 1
NCF_SOFTWARE_ENUMERATED: COMPONENT_CHARACTERISTICS = 2
NCF_PHYSICAL: COMPONENT_CHARACTERISTICS = 4
NCF_HIDDEN: COMPONENT_CHARACTERISTICS = 8
NCF_NO_SERVICE: COMPONENT_CHARACTERISTICS = 16
NCF_NOT_USER_REMOVABLE: COMPONENT_CHARACTERISTICS = 32
NCF_MULTIPORT_INSTANCED_ADAPTER: COMPONENT_CHARACTERISTICS = 64
NCF_HAS_UI: COMPONENT_CHARACTERISTICS = 128
NCF_SINGLE_INSTANCE: COMPONENT_CHARACTERISTICS = 256
NCF_FILTER: COMPONENT_CHARACTERISTICS = 1024
NCF_DONTEXPOSELOWER: COMPONENT_CHARACTERISTICS = 4096
NCF_HIDE_BINDING: COMPONENT_CHARACTERISTICS = 8192
NCF_NDIS_PROTOCOL: COMPONENT_CHARACTERISTICS = 16384
NCF_FIXED_BINDING: COMPONENT_CHARACTERISTICS = 131072
NCF_LW_FILTER: COMPONENT_CHARACTERISTICS = 262144
class CONFIG_INFO_0(Structure):
    cfgi0_key: win32more.Foundation.PWSTR
    cfgi0_data: win32more.Foundation.PWSTR
DEFAULT_PAGES = Int32
DPP_ADVANCED: DEFAULT_PAGES = 1
class DSREG_JOIN_INFO(Structure):
    joinType: win32more.NetworkManagement.NetManagement.DSREG_JOIN_TYPE
    pJoinCertificate: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
    pszDeviceId: win32more.Foundation.PWSTR
    pszIdpDomain: win32more.Foundation.PWSTR
    pszTenantId: win32more.Foundation.PWSTR
    pszJoinUserEmail: win32more.Foundation.PWSTR
    pszTenantDisplayName: win32more.Foundation.PWSTR
    pszMdmEnrollmentUrl: win32more.Foundation.PWSTR
    pszMdmTermsOfUseUrl: win32more.Foundation.PWSTR
    pszMdmComplianceUrl: win32more.Foundation.PWSTR
    pszUserSettingSyncUrl: win32more.Foundation.PWSTR
    pUserInfo: POINTER(win32more.NetworkManagement.NetManagement.DSREG_USER_INFO_head)
DSREG_JOIN_TYPE = Int32
DSREG_UNKNOWN_JOIN: DSREG_JOIN_TYPE = 0
DSREG_DEVICE_JOIN: DSREG_JOIN_TYPE = 1
DSREG_WORKPLACE_JOIN: DSREG_JOIN_TYPE = 2
class DSREG_USER_INFO(Structure):
    pszUserEmail: win32more.Foundation.PWSTR
    pszUserKeyId: win32more.Foundation.PWSTR
    pszUserKeyName: win32more.Foundation.PWSTR
ENUM_BINDING_PATHS_FLAGS = Int32
EBP_ABOVE: ENUM_BINDING_PATHS_FLAGS = 1
EBP_BELOW: ENUM_BINDING_PATHS_FLAGS = 2
class ERRLOG_OTHER_INFO(Structure):
    alrter_errcode: UInt32
    alrter_offset: UInt32
class ERROR_LOG(Structure):
    el_len: UInt32
    el_reserved: UInt32
    el_time: UInt32
    el_error: UInt32
    el_name: win32more.Foundation.PWSTR
    el_text: win32more.Foundation.PWSTR
    el_data: c_char_p_no
    el_data_size: UInt32
    el_nstrings: UInt32
class FLAT_STRING(Structure):
    MaximumLength: Int16
    Length: Int16
    Buffer: win32more.Foundation.CHAR * 1
FORCE_LEVEL_FLAGS = UInt32
USE_NOFORCE: FORCE_LEVEL_FLAGS = 0
USE_FORCE: FORCE_LEVEL_FLAGS = 1
USE_LOTS_OF_FORCE: FORCE_LEVEL_FLAGS = 2
class GROUP_INFO_0(Structure):
    grpi0_name: win32more.Foundation.PWSTR
class GROUP_INFO_1(Structure):
    grpi1_name: win32more.Foundation.PWSTR
    grpi1_comment: win32more.Foundation.PWSTR
class GROUP_INFO_1002(Structure):
    grpi1002_comment: win32more.Foundation.PWSTR
class GROUP_INFO_1005(Structure):
    grpi1005_attributes: UInt32
class GROUP_INFO_2(Structure):
    grpi2_name: win32more.Foundation.PWSTR
    grpi2_comment: win32more.Foundation.PWSTR
    grpi2_group_id: UInt32
    grpi2_attributes: UInt32
class GROUP_INFO_3(Structure):
    grpi3_name: win32more.Foundation.PWSTR
    grpi3_comment: win32more.Foundation.PWSTR
    grpi3_group_sid: win32more.Foundation.PSID
    grpi3_attributes: UInt32
class GROUP_USERS_INFO_0(Structure):
    grui0_name: win32more.Foundation.PWSTR
class GROUP_USERS_INFO_1(Structure):
    grui1_name: win32more.Foundation.PWSTR
    grui1_attributes: UInt32
class HARDWARE_ADDRESS(Structure):
    Address: Byte * 6
class HLOG(Structure):
    time: UInt32
    last_flags: UInt32
    offset: UInt32
    rec_offset: UInt32
class IEnumNetCfgBindingInterface(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae90-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.NetworkManagement.NetManagement.INetCfgBindingInterface_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgBindingInterface_head)) -> win32more.Foundation.HRESULT: ...
class IEnumNetCfgBindingPath(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae91-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgBindingPath_head)) -> win32more.Foundation.HRESULT: ...
class IEnumNetCfgComponent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae92-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgComponent_head)) -> win32more.Foundation.HRESULT: ...
class INetCfg(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae93-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def Initialize(pvReserved: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Uninitialize() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Apply() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Cancel() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def EnumComponents(pguidClass: POINTER(Guid), ppenumComponent: POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgComponent_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def FindComponent(pszwInfId: win32more.Foundation.PWSTR, pComponent: POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def QueryNetCfgClass(pguidClass: POINTER(Guid), riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class INetCfgBindingInterface(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae94-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def GetName(ppszwInterfaceName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetUpperComponent(ppnccItem: POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetLowerComponent(ppnccItem: POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head)) -> win32more.Foundation.HRESULT: ...
class INetCfgBindingPath(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae96-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def IsSamePathAs(pPath: win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def IsSubPathOf(pPath: win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsEnabled() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Enable(fEnable: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetPathToken(ppszwPathToken: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetOwner(ppComponent: POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDepth(pcInterfaces: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def EnumBindingInterfaces(ppenumInterface: POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgBindingInterface_head)) -> win32more.Foundation.HRESULT: ...
class INetCfgClass(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae97-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def FindComponent(pszwInfId: win32more.Foundation.PWSTR, ppnccItem: POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnumComponents(ppenumComponent: POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgComponent_head)) -> win32more.Foundation.HRESULT: ...
class INetCfgClassSetup(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae9d-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def SelectAndInstall(hwndParent: win32more.Foundation.HWND, pOboToken: POINTER(win32more.NetworkManagement.NetManagement.OBO_TOKEN_head), ppnccItem: POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Install(pszwInfId: win32more.Foundation.PWSTR, pOboToken: POINTER(win32more.NetworkManagement.NetManagement.OBO_TOKEN_head), dwSetupFlags: UInt32, dwUpgradeFromBuildNo: UInt32, pszwAnswerFile: win32more.Foundation.PWSTR, pszwAnswerSections: win32more.Foundation.PWSTR, ppnccItem: POINTER(win32more.NetworkManagement.NetManagement.INetCfgComponent_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def DeInstall(pComponent: win32more.NetworkManagement.NetManagement.INetCfgComponent_head, pOboToken: POINTER(win32more.NetworkManagement.NetManagement.OBO_TOKEN_head), pmszwRefs: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class INetCfgClassSetup2(c_void_p):
    extends: win32more.NetworkManagement.NetManagement.INetCfgClassSetup
    Guid = Guid('c0e8aea0-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(6)
    def UpdateNonEnumeratedComponent(pIComp: win32more.NetworkManagement.NetManagement.INetCfgComponent_head, dwSetupFlags: UInt32, dwUpgradeFromBuildNo: UInt32) -> win32more.Foundation.HRESULT: ...
class INetCfgComponent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae99-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def GetDisplayName(ppszwDisplayName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetDisplayName(pszwDisplayName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetHelpText(pszwHelpText: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetId(ppszwId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCharacteristics(pdwCharacteristics: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetInstanceGuid(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetPnpDevNodeId(ppszwDevNodeId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetClassGuid(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetBindName(ppszwBindName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetDeviceStatus(pulStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def OpenParamKey(phkey: POINTER(win32more.System.Registry.HKEY)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def RaisePropertyUi(hwndParent: win32more.Foundation.HWND, dwFlags: UInt32, punkContext: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class INetCfgComponentBindings(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae9e-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def BindTo(pnccItem: win32more.NetworkManagement.NetManagement.INetCfgComponent_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnbindFrom(pnccItem: win32more.NetworkManagement.NetManagement.INetCfgComponent_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SupportsBindingInterface(dwFlags: UInt32, pszwInterfaceName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def IsBoundTo(pnccItem: win32more.NetworkManagement.NetManagement.INetCfgComponent_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def IsBindableTo(pnccItem: win32more.NetworkManagement.NetManagement.INetCfgComponent_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def EnumBindingPaths(dwFlags: UInt32, ppIEnum: POINTER(win32more.NetworkManagement.NetManagement.IEnumNetCfgBindingPath_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def MoveBefore(pncbItemSrc: win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head, pncbItemDest: win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def MoveAfter(pncbItemSrc: win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head, pncbItemDest: win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head) -> win32more.Foundation.HRESULT: ...
class INetCfgComponentControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('932238df-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    @commethod(3)
    def Initialize(pIComp: win32more.NetworkManagement.NetManagement.INetCfgComponent_head, pINetCfg: win32more.NetworkManagement.NetManagement.INetCfg_head, fInstalling: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ApplyRegistryChanges() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ApplyPnpChanges(pICallback: win32more.NetworkManagement.NetManagement.INetCfgPnpReconfigCallback_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CancelChanges() -> win32more.Foundation.HRESULT: ...
class INetCfgComponentNotifyBinding(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('932238e1-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    @commethod(3)
    def QueryBindingPath(dwChangeFlag: UInt32, pIPath: win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyBindingPath(dwChangeFlag: UInt32, pIPath: win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head) -> win32more.Foundation.HRESULT: ...
class INetCfgComponentNotifyGlobal(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('932238e2-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    @commethod(3)
    def GetSupportedNotifications(dwNotifications: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SysQueryBindingPath(dwChangeFlag: UInt32, pIPath: win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SysNotifyBindingPath(dwChangeFlag: UInt32, pIPath: win32more.NetworkManagement.NetManagement.INetCfgBindingPath_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SysNotifyComponent(dwChangeFlag: UInt32, pIComp: win32more.NetworkManagement.NetManagement.INetCfgComponent_head) -> win32more.Foundation.HRESULT: ...
class INetCfgComponentPropertyUi(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('932238e0-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    @commethod(3)
    def QueryPropertyUi(pUnkReserved: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetContext(pUnkReserved: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def MergePropPages(pdwDefPages: POINTER(UInt32), pahpspPrivate: POINTER(c_char_p_no), pcPages: POINTER(UInt32), hwndParent: win32more.Foundation.HWND, pszStartPage: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ValidateProperties(hwndSheet: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ApplyProperties() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CancelProperties() -> win32more.Foundation.HRESULT: ...
class INetCfgComponentSetup(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('932238e3-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    @commethod(3)
    def Install(dwSetupFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Upgrade(dwSetupFlags: UInt32, dwUpgradeFomBuildNo: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ReadAnswerFile(pszwAnswerFile: win32more.Foundation.PWSTR, pszwAnswerSections: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Removing() -> win32more.Foundation.HRESULT: ...
class INetCfgComponentSysPrep(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae9a-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def SaveAdapterParameters(pncsp: win32more.NetworkManagement.NetManagement.INetCfgSysPrep_head, pszwAnswerSections: win32more.Foundation.PWSTR, pAdapterInstanceGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RestoreAdapterParameters(pszwAnswerFile: win32more.Foundation.PWSTR, pszwAnswerSection: win32more.Foundation.PWSTR, pAdapterInstanceGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class INetCfgComponentUpperEdge(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('932238e4-bea1-11d0-92-98-00-c0-4f-c9-9d-cf')
    @commethod(3)
    def GetInterfaceIdsForAdapter(pAdapter: win32more.NetworkManagement.NetManagement.INetCfgComponent_head, pdwNumInterfaces: POINTER(UInt32), ppguidInterfaceIds: POINTER(POINTER(Guid))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddInterfacesToAdapter(pAdapter: win32more.NetworkManagement.NetManagement.INetCfgComponent_head, dwNumInterfaces: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveInterfacesFromAdapter(pAdapter: win32more.NetworkManagement.NetManagement.INetCfgComponent_head, dwNumInterfaces: UInt32, pguidInterfaceIds: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class INetCfgLock(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae9f-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def AcquireWriteLock(cmsTimeout: UInt32, pszwClientDescription: win32more.Foundation.PWSTR, ppszwClientDescription: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseWriteLock() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsWriteLocked(ppszwClientDescription: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class INetCfgPnpReconfigCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8d84bd35-e227-11d2-b7-00-00-a0-c9-8a-6a-85')
    @commethod(3)
    def SendPnpReconfig(Layer: win32more.NetworkManagement.NetManagement.NCPNP_RECONFIG_LAYER, pszwUpper: win32more.Foundation.PWSTR, pszwLower: win32more.Foundation.PWSTR, pvData: c_void_p, dwSizeOfData: UInt32) -> win32more.Foundation.HRESULT: ...
class INetCfgSysPrep(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0e8ae98-306e-11d1-aa-cf-00-80-5f-c1-27-0e')
    @commethod(3)
    def HrSetupSetFirstDword(pwszSection: win32more.Foundation.PWSTR, pwszKey: win32more.Foundation.PWSTR, dwValue: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def HrSetupSetFirstString(pwszSection: win32more.Foundation.PWSTR, pwszKey: win32more.Foundation.PWSTR, pwszValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def HrSetupSetFirstStringAsBool(pwszSection: win32more.Foundation.PWSTR, pwszKey: win32more.Foundation.PWSTR, fValue: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def HrSetupSetFirstMultiSzField(pwszSection: win32more.Foundation.PWSTR, pwszKey: win32more.Foundation.PWSTR, pmszValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class INetLanConnectionUiInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c08956a6-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(3)
    def GetDeviceGuid(pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class INetRasConnectionIpUiInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('faedcf58-31fe-11d1-aa-d2-00-80-5f-c1-27-0e')
    @commethod(3)
    def GetUiInfo(pInfo: POINTER(win32more.NetworkManagement.NetManagement.RASCON_IPUI_head)) -> win32more.Foundation.HRESULT: ...
class IProvisioningDomain(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c96fbd50-24dd-11d8-89-fb-00-90-4b-2e-a9-c6')
    @commethod(3)
    def Add(pszwPathToFolder: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Query(pszwDomain: win32more.Foundation.PWSTR, pszwLanguage: win32more.Foundation.PWSTR, pszwXPathQuery: win32more.Foundation.PWSTR, Nodes: POINTER(win32more.Data.Xml.MsXml.IXMLDOMNodeList_head)) -> win32more.Foundation.HRESULT: ...
class IProvisioningProfileWireless(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c96fbd51-24dd-11d8-89-fb-00-90-4b-2e-a9-c6')
    @commethod(3)
    def CreateProfile(bstrXMLWirelessConfigProfile: win32more.Foundation.BSTR, bstrXMLConnectionConfigProfile: win32more.Foundation.BSTR, pAdapterInstanceGuid: POINTER(Guid), pulStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class LOCALGROUP_INFO_0(Structure):
    lgrpi0_name: win32more.Foundation.PWSTR
class LOCALGROUP_INFO_1(Structure):
    lgrpi1_name: win32more.Foundation.PWSTR
    lgrpi1_comment: win32more.Foundation.PWSTR
class LOCALGROUP_INFO_1002(Structure):
    lgrpi1002_comment: win32more.Foundation.PWSTR
class LOCALGROUP_MEMBERS_INFO_0(Structure):
    lgrmi0_sid: win32more.Foundation.PSID
class LOCALGROUP_MEMBERS_INFO_1(Structure):
    lgrmi1_sid: win32more.Foundation.PSID
    lgrmi1_sidusage: win32more.Security.SID_NAME_USE
    lgrmi1_name: win32more.Foundation.PWSTR
class LOCALGROUP_MEMBERS_INFO_2(Structure):
    lgrmi2_sid: win32more.Foundation.PSID
    lgrmi2_sidusage: win32more.Security.SID_NAME_USE
    lgrmi2_domainandname: win32more.Foundation.PWSTR
class LOCALGROUP_MEMBERS_INFO_3(Structure):
    lgrmi3_domainandname: win32more.Foundation.PWSTR
class LOCALGROUP_USERS_INFO_0(Structure):
    lgrui0_name: win32more.Foundation.PWSTR
class MPR_PROTOCOL_0(Structure):
    dwProtocolId: UInt32
    wszProtocol: Char * 41
    wszDLLName: Char * 49
class MSA_INFO_0(Structure):
    State: win32more.NetworkManagement.NetManagement.MSA_INFO_STATE
MSA_INFO_LEVEL = Int32
MSA_INFO_LEVEL_MsaInfoLevel0: MSA_INFO_LEVEL = 0
MSA_INFO_LEVEL_MsaInfoLevelMax: MSA_INFO_LEVEL = 1
MSA_INFO_STATE = Int32
MSA_INFO_STATE_MsaInfoNotExist: MSA_INFO_STATE = 1
MSA_INFO_STATE_MsaInfoNotService: MSA_INFO_STATE = 2
MSA_INFO_STATE_MsaInfoCannotInstall: MSA_INFO_STATE = 3
MSA_INFO_STATE_MsaInfoCanInstall: MSA_INFO_STATE = 4
MSA_INFO_STATE_MsaInfoInstalled: MSA_INFO_STATE = 5
class MSG_INFO_0(Structure):
    msgi0_name: win32more.Foundation.PWSTR
class MSG_INFO_1(Structure):
    msgi1_name: win32more.Foundation.PWSTR
    msgi1_forward_flag: UInt32
    msgi1_forward: win32more.Foundation.PWSTR
NCPNP_RECONFIG_LAYER = Int32
NCRL_NDIS: NCPNP_RECONFIG_LAYER = 1
NCRL_TDI: NCPNP_RECONFIG_LAYER = 2
NCRP_FLAGS = Int32
NCRP_QUERY_PROPERTY_UI: NCRP_FLAGS = 1
NCRP_SHOW_PROPERTY_UI: NCRP_FLAGS = 2
NET_COMPUTER_NAME_TYPE = Int32
NET_COMPUTER_NAME_TYPE_NetPrimaryComputerName: NET_COMPUTER_NAME_TYPE = 0
NET_COMPUTER_NAME_TYPE_NetAlternateComputerNames: NET_COMPUTER_NAME_TYPE = 1
NET_COMPUTER_NAME_TYPE_NetAllComputerNames: NET_COMPUTER_NAME_TYPE = 2
NET_COMPUTER_NAME_TYPE_NetComputerNameTypeMax: NET_COMPUTER_NAME_TYPE = 3
class NET_DISPLAY_GROUP(Structure):
    grpi3_name: win32more.Foundation.PWSTR
    grpi3_comment: win32more.Foundation.PWSTR
    grpi3_group_id: UInt32
    grpi3_attributes: UInt32
    grpi3_next_index: UInt32
class NET_DISPLAY_MACHINE(Structure):
    usri2_name: win32more.Foundation.PWSTR
    usri2_comment: win32more.Foundation.PWSTR
    usri2_flags: win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri2_user_id: UInt32
    usri2_next_index: UInt32
class NET_DISPLAY_USER(Structure):
    usri1_name: win32more.Foundation.PWSTR
    usri1_comment: win32more.Foundation.PWSTR
    usri1_flags: win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri1_full_name: win32more.Foundation.PWSTR
    usri1_user_id: UInt32
    usri1_next_index: UInt32
NET_JOIN_DOMAIN_JOIN_OPTIONS = UInt32
NETSETUP_JOIN_DOMAIN: NET_JOIN_DOMAIN_JOIN_OPTIONS = 1
NETSETUP_ACCT_CREATE: NET_JOIN_DOMAIN_JOIN_OPTIONS = 2
NETSETUP_WIN9X_UPGRADE: NET_JOIN_DOMAIN_JOIN_OPTIONS = 16
NETSETUP_DOMAIN_JOIN_IF_JOINED: NET_JOIN_DOMAIN_JOIN_OPTIONS = 32
NETSETUP_JOIN_UNSECURE: NET_JOIN_DOMAIN_JOIN_OPTIONS = 64
NETSETUP_MACHINE_PWD_PASSED: NET_JOIN_DOMAIN_JOIN_OPTIONS = 128
NETSETUP_DEFER_SPN_SET: NET_JOIN_DOMAIN_JOIN_OPTIONS = 256
NETSETUP_JOIN_DC_ACCOUNT: NET_JOIN_DOMAIN_JOIN_OPTIONS = 512
NETSETUP_JOIN_WITH_NEW_NAME: NET_JOIN_DOMAIN_JOIN_OPTIONS = 1024
NETSETUP_JOIN_READONLY: NET_JOIN_DOMAIN_JOIN_OPTIONS = 2048
NETSETUP_AMBIGUOUS_DC: NET_JOIN_DOMAIN_JOIN_OPTIONS = 4096
NETSETUP_NO_NETLOGON_CACHE: NET_JOIN_DOMAIN_JOIN_OPTIONS = 8192
NETSETUP_DONT_CONTROL_SERVICES: NET_JOIN_DOMAIN_JOIN_OPTIONS = 16384
NETSETUP_SET_MACHINE_NAME: NET_JOIN_DOMAIN_JOIN_OPTIONS = 32768
NETSETUP_FORCE_SPN_SET: NET_JOIN_DOMAIN_JOIN_OPTIONS = 65536
NETSETUP_NO_ACCT_REUSE: NET_JOIN_DOMAIN_JOIN_OPTIONS = 131072
NETSETUP_IGNORE_UNSUPPORTED_FLAGS: NET_JOIN_DOMAIN_JOIN_OPTIONS = 268435456
NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = Int32
SUPPORTS_REMOTE_ADMIN_PROTOCOL: NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = 2
SUPPORTS_RPC: NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = 4
SUPPORTS_SAM_PROTOCOL: NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = 8
SUPPORTS_UNICODE: NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = 16
SUPPORTS_LOCAL: NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = 32
NET_REQUEST_PROVISION_OPTIONS = UInt32
NETSETUP_PROVISION_ONLINE_CALLER: NET_REQUEST_PROVISION_OPTIONS = 1073741824
NET_SERVER_TYPE = UInt32
SV_TYPE_WORKSTATION: NET_SERVER_TYPE = 1
SV_TYPE_SERVER: NET_SERVER_TYPE = 2
SV_TYPE_SQLSERVER: NET_SERVER_TYPE = 4
SV_TYPE_DOMAIN_CTRL: NET_SERVER_TYPE = 8
SV_TYPE_DOMAIN_BAKCTRL: NET_SERVER_TYPE = 16
SV_TYPE_TIME_SOURCE: NET_SERVER_TYPE = 32
SV_TYPE_AFP: NET_SERVER_TYPE = 64
SV_TYPE_NOVELL: NET_SERVER_TYPE = 128
SV_TYPE_DOMAIN_MEMBER: NET_SERVER_TYPE = 256
SV_TYPE_PRINTQ_SERVER: NET_SERVER_TYPE = 512
SV_TYPE_DIALIN_SERVER: NET_SERVER_TYPE = 1024
SV_TYPE_XENIX_SERVER: NET_SERVER_TYPE = 2048
SV_TYPE_SERVER_UNIX: NET_SERVER_TYPE = 2048
SV_TYPE_NT: NET_SERVER_TYPE = 4096
SV_TYPE_WFW: NET_SERVER_TYPE = 8192
SV_TYPE_SERVER_MFPN: NET_SERVER_TYPE = 16384
SV_TYPE_SERVER_NT: NET_SERVER_TYPE = 32768
SV_TYPE_POTENTIAL_BROWSER: NET_SERVER_TYPE = 65536
SV_TYPE_BACKUP_BROWSER: NET_SERVER_TYPE = 131072
SV_TYPE_MASTER_BROWSER: NET_SERVER_TYPE = 262144
SV_TYPE_DOMAIN_MASTER: NET_SERVER_TYPE = 524288
SV_TYPE_SERVER_OSF: NET_SERVER_TYPE = 1048576
SV_TYPE_SERVER_VMS: NET_SERVER_TYPE = 2097152
SV_TYPE_WINDOWS: NET_SERVER_TYPE = 4194304
SV_TYPE_DFS: NET_SERVER_TYPE = 8388608
SV_TYPE_CLUSTER_NT: NET_SERVER_TYPE = 16777216
SV_TYPE_TERMINALSERVER: NET_SERVER_TYPE = 33554432
SV_TYPE_CLUSTER_VS_NT: NET_SERVER_TYPE = 67108864
SV_TYPE_DCE: NET_SERVER_TYPE = 268435456
SV_TYPE_ALTERNATE_XPORT: NET_SERVER_TYPE = 536870912
SV_TYPE_LOCAL_LIST_ONLY: NET_SERVER_TYPE = 1073741824
SV_TYPE_DOMAIN_ENUM: NET_SERVER_TYPE = 2147483648
SV_TYPE_ALL: NET_SERVER_TYPE = 4294967295
NET_USER_ENUM_FILTER_FLAGS = UInt32
FILTER_TEMP_DUPLICATE_ACCOUNT: NET_USER_ENUM_FILTER_FLAGS = 1
FILTER_NORMAL_ACCOUNT: NET_USER_ENUM_FILTER_FLAGS = 2
FILTER_INTERDOMAIN_TRUST_ACCOUNT: NET_USER_ENUM_FILTER_FLAGS = 8
FILTER_WORKSTATION_TRUST_ACCOUNT: NET_USER_ENUM_FILTER_FLAGS = 16
FILTER_SERVER_TRUST_ACCOUNT: NET_USER_ENUM_FILTER_FLAGS = 32
class NET_VALIDATE_AUTHENTICATION_INPUT_ARG(Structure):
    InputPersistedFields: win32more.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS
    PasswordMatched: win32more.Foundation.BOOLEAN
class NET_VALIDATE_OUTPUT_ARG(Structure):
    ChangedPersistedFields: win32more.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS
    ValidationStatus: UInt32
class NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG(Structure):
    InputPersistedFields: win32more.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS
    ClearPassword: win32more.Foundation.PWSTR
    UserAccountName: win32more.Foundation.PWSTR
    HashedPassword: win32more.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_HASH
    PasswordMatch: win32more.Foundation.BOOLEAN
class NET_VALIDATE_PASSWORD_HASH(Structure):
    Length: UInt32
    Hash: c_char_p_no
class NET_VALIDATE_PASSWORD_RESET_INPUT_ARG(Structure):
    InputPersistedFields: win32more.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS
    ClearPassword: win32more.Foundation.PWSTR
    UserAccountName: win32more.Foundation.PWSTR
    HashedPassword: win32more.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_HASH
    PasswordMustChangeAtNextLogon: win32more.Foundation.BOOLEAN
    ClearLockout: win32more.Foundation.BOOLEAN
NET_VALIDATE_PASSWORD_TYPE = Int32
NET_VALIDATE_PASSWORD_TYPE_NetValidateAuthentication: NET_VALIDATE_PASSWORD_TYPE = 1
NET_VALIDATE_PASSWORD_TYPE_NetValidatePasswordChange: NET_VALIDATE_PASSWORD_TYPE = 2
NET_VALIDATE_PASSWORD_TYPE_NetValidatePasswordReset: NET_VALIDATE_PASSWORD_TYPE = 3
class NET_VALIDATE_PERSISTED_FIELDS(Structure):
    PresentFields: UInt32
    PasswordLastSet: win32more.Foundation.FILETIME
    BadPasswordTime: win32more.Foundation.FILETIME
    LockoutTime: win32more.Foundation.FILETIME
    BadPasswordCount: UInt32
    PasswordHistoryLength: UInt32
    PasswordHistory: POINTER(win32more.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_HASH_head)
class NETLOGON_INFO_1(Structure):
    netlog1_flags: UInt32
    netlog1_pdc_connection_status: UInt32
class NETLOGON_INFO_2(Structure):
    netlog2_flags: UInt32
    netlog2_pdc_connection_status: UInt32
    netlog2_trusted_dc_name: win32more.Foundation.PWSTR
    netlog2_tc_connection_status: UInt32
class NETLOGON_INFO_3(Structure):
    netlog3_flags: UInt32
    netlog3_logon_attempts: UInt32
    netlog3_reserved1: UInt32
    netlog3_reserved2: UInt32
    netlog3_reserved3: UInt32
    netlog3_reserved4: UInt32
    netlog3_reserved5: UInt32
class NETLOGON_INFO_4(Structure):
    netlog4_trusted_dc_name: win32more.Foundation.PWSTR
    netlog4_trusted_domain_name: win32more.Foundation.PWSTR
NetProvisioning = Guid('2aa2b5fe-b846-4d07-81-0c-b2-1e-e4-53-20-e3')
NETSETUP_JOIN_STATUS = Int32
NETSETUP_JOIN_STATUS_NetSetupUnknownStatus: NETSETUP_JOIN_STATUS = 0
NETSETUP_JOIN_STATUS_NetSetupUnjoined: NETSETUP_JOIN_STATUS = 1
NETSETUP_JOIN_STATUS_NetSetupWorkgroupName: NETSETUP_JOIN_STATUS = 2
NETSETUP_JOIN_STATUS_NetSetupDomainName: NETSETUP_JOIN_STATUS = 3
NETSETUP_NAME_TYPE = Int32
NETSETUP_NAME_TYPE_NetSetupUnknown: NETSETUP_NAME_TYPE = 0
NETSETUP_NAME_TYPE_NetSetupMachine: NETSETUP_NAME_TYPE = 1
NETSETUP_NAME_TYPE_NetSetupWorkgroup: NETSETUP_NAME_TYPE = 2
NETSETUP_NAME_TYPE_NetSetupDomain: NETSETUP_NAME_TYPE = 3
NETSETUP_NAME_TYPE_NetSetupNonExistentDomain: NETSETUP_NAME_TYPE = 4
NETSETUP_NAME_TYPE_NetSetupDnsMachine: NETSETUP_NAME_TYPE = 5
NETSETUP_PROVISION = UInt32
NETSETUP_PROVISION_DOWNLEVEL_PRIV_SUPPORT: NETSETUP_PROVISION = 1
NETSETUP_PROVISION_REUSE_ACCOUNT: NETSETUP_PROVISION = 2
NETSETUP_PROVISION_USE_DEFAULT_PASSWORD: NETSETUP_PROVISION = 4
NETSETUP_PROVISION_SKIP_ACCOUNT_SEARCH: NETSETUP_PROVISION = 8
NETSETUP_PROVISION_ROOT_CA_CERTS: NETSETUP_PROVISION = 16
class NETSETUP_PROVISIONING_PARAMS(Structure):
    dwVersion: UInt32
    lpDomain: win32more.Foundation.PWSTR
    lpHostName: win32more.Foundation.PWSTR
    lpMachineAccountOU: win32more.Foundation.PWSTR
    lpDcName: win32more.Foundation.PWSTR
    dwProvisionOptions: win32more.NetworkManagement.NetManagement.NETSETUP_PROVISION
    aCertTemplateNames: POINTER(win32more.Foundation.PWSTR)
    cCertTemplateNames: UInt32
    aMachinePolicyNames: POINTER(win32more.Foundation.PWSTR)
    cMachinePolicyNames: UInt32
    aMachinePolicyPaths: POINTER(win32more.Foundation.PWSTR)
    cMachinePolicyPaths: UInt32
    lpNetbiosName: win32more.Foundation.PWSTR
    lpSiteName: win32more.Foundation.PWSTR
    lpPrimaryDNSDomain: win32more.Foundation.PWSTR
NETWORK_INSTALL_TIME = Int32
NSF_PRIMARYINSTALL: NETWORK_INSTALL_TIME = 1
NSF_POSTSYSINSTALL: NETWORK_INSTALL_TIME = 2
class NETWORK_NAME(Structure):
    Name: win32more.NetworkManagement.NetManagement.FLAT_STRING
NETWORK_UPGRADE_TYPE = Int32
NSF_WIN16_UPGRADE: NETWORK_UPGRADE_TYPE = 16
NSF_WIN95_UPGRADE: NETWORK_UPGRADE_TYPE = 32
NSF_WINNT_WKS_UPGRADE: NETWORK_UPGRADE_TYPE = 64
NSF_WINNT_SVR_UPGRADE: NETWORK_UPGRADE_TYPE = 128
NSF_WINNT_SBS_UPGRADE: NETWORK_UPGRADE_TYPE = 256
NSF_COMPONENT_UPDATE: NETWORK_UPGRADE_TYPE = 512
class OBO_TOKEN(Structure):
    Type: win32more.NetworkManagement.NetManagement.OBO_TOKEN_TYPE
    pncc: win32more.NetworkManagement.NetManagement.INetCfgComponent_head
    pszwManufacturer: win32more.Foundation.PWSTR
    pszwProduct: win32more.Foundation.PWSTR
    pszwDisplayName: win32more.Foundation.PWSTR
    fRegistered: win32more.Foundation.BOOL
OBO_TOKEN_TYPE = Int32
OBO_USER: OBO_TOKEN_TYPE = 1
OBO_COMPONENT: OBO_TOKEN_TYPE = 2
OBO_SOFTWARE: OBO_TOKEN_TYPE = 3
class PRINT_OTHER_INFO(Structure):
    alrtpr_jobid: UInt32
    alrtpr_status: UInt32
    alrtpr_submitted: UInt32
    alrtpr_size: UInt32
class RASCON_IPUI(Structure):
    guidConnection: Guid
    fIPv6Cfg: win32more.Foundation.BOOL
    dwFlags: UInt32
    pszwIpAddr: Char * 16
    pszwDnsAddr: Char * 16
    pszwDns2Addr: Char * 16
    pszwWinsAddr: Char * 16
    pszwWins2Addr: Char * 16
    pszwDnsSuffix: Char * 256
    pszwIpv6Addr: Char * 65
    dwIpv6PrefixLength: UInt32
    pszwIpv6DnsAddr: Char * 65
    pszwIpv6Dns2Addr: Char * 65
    dwIPv4InfMetric: UInt32
    dwIPv6InfMetric: UInt32
RASCON_UIINFO_FLAGS = Int32
RCUIF_VPN: RASCON_UIINFO_FLAGS = 1
RCUIF_DEMAND_DIAL: RASCON_UIINFO_FLAGS = 2
RCUIF_NOT_ADMIN: RASCON_UIINFO_FLAGS = 4
RCUIF_USE_IPv4_STATICADDRESS: RASCON_UIINFO_FLAGS = 8
RCUIF_USE_IPv4_NAME_SERVERS: RASCON_UIINFO_FLAGS = 16
RCUIF_USE_IPv4_REMOTE_GATEWAY: RASCON_UIINFO_FLAGS = 32
RCUIF_USE_IPv4_EXPLICIT_METRIC: RASCON_UIINFO_FLAGS = 64
RCUIF_USE_HEADER_COMPRESSION: RASCON_UIINFO_FLAGS = 128
RCUIF_USE_DISABLE_REGISTER_DNS: RASCON_UIINFO_FLAGS = 256
RCUIF_USE_PRIVATE_DNS_SUFFIX: RASCON_UIINFO_FLAGS = 512
RCUIF_ENABLE_NBT: RASCON_UIINFO_FLAGS = 1024
RCUIF_USE_IPv6_STATICADDRESS: RASCON_UIINFO_FLAGS = 2048
RCUIF_USE_IPv6_NAME_SERVERS: RASCON_UIINFO_FLAGS = 4096
RCUIF_USE_IPv6_REMOTE_GATEWAY: RASCON_UIINFO_FLAGS = 8192
RCUIF_USE_IPv6_EXPLICIT_METRIC: RASCON_UIINFO_FLAGS = 16384
RCUIF_DISABLE_CLASS_BASED_ROUTE: RASCON_UIINFO_FLAGS = 32768
class REPL_EDIR_INFO_0(Structure):
    rped0_dirname: win32more.Foundation.PWSTR
class REPL_EDIR_INFO_1(Structure):
    rped1_dirname: win32more.Foundation.PWSTR
    rped1_integrity: UInt32
    rped1_extent: UInt32
class REPL_EDIR_INFO_1000(Structure):
    rped1000_integrity: UInt32
class REPL_EDIR_INFO_1001(Structure):
    rped1001_extent: UInt32
class REPL_EDIR_INFO_2(Structure):
    rped2_dirname: win32more.Foundation.PWSTR
    rped2_integrity: UInt32
    rped2_extent: UInt32
    rped2_lockcount: UInt32
    rped2_locktime: UInt32
class REPL_IDIR_INFO_0(Structure):
    rpid0_dirname: win32more.Foundation.PWSTR
class REPL_IDIR_INFO_1(Structure):
    rpid1_dirname: win32more.Foundation.PWSTR
    rpid1_state: UInt32
    rpid1_mastername: win32more.Foundation.PWSTR
    rpid1_last_update_time: UInt32
    rpid1_lockcount: UInt32
    rpid1_locktime: UInt32
class REPL_INFO_0(Structure):
    rp0_role: UInt32
    rp0_exportpath: win32more.Foundation.PWSTR
    rp0_exportlist: win32more.Foundation.PWSTR
    rp0_importpath: win32more.Foundation.PWSTR
    rp0_importlist: win32more.Foundation.PWSTR
    rp0_logonusername: win32more.Foundation.PWSTR
    rp0_interval: UInt32
    rp0_pulse: UInt32
    rp0_guardtime: UInt32
    rp0_random: UInt32
class REPL_INFO_1000(Structure):
    rp1000_interval: UInt32
class REPL_INFO_1001(Structure):
    rp1001_pulse: UInt32
class REPL_INFO_1002(Structure):
    rp1002_guardtime: UInt32
class REPL_INFO_1003(Structure):
    rp1003_random: UInt32
class RTR_INFO_BLOCK_HEADER(Structure):
    Version: UInt32
    Size: UInt32
    TocEntriesCount: UInt32
    TocEntry: win32more.NetworkManagement.NetManagement.RTR_TOC_ENTRY * 1
class RTR_TOC_ENTRY(Structure):
    InfoType: UInt32
    InfoSize: UInt32
    Count: UInt32
    Offset: UInt32
class SERVER_INFO_100(Structure):
    sv100_platform_id: UInt32
    sv100_name: win32more.Foundation.PWSTR
class SERVER_INFO_1005(Structure):
    sv1005_comment: win32more.Foundation.PWSTR
class SERVER_INFO_101(Structure):
    sv101_platform_id: UInt32
    sv101_name: win32more.Foundation.PWSTR
    sv101_version_major: UInt32
    sv101_version_minor: UInt32
    sv101_type: win32more.NetworkManagement.NetManagement.NET_SERVER_TYPE
    sv101_comment: win32more.Foundation.PWSTR
class SERVER_INFO_1010(Structure):
    sv1010_disc: Int32
class SERVER_INFO_1016(Structure):
    sv1016_hidden: win32more.NetworkManagement.NetManagement.SERVER_INFO_HIDDEN
class SERVER_INFO_1017(Structure):
    sv1017_announce: UInt32
class SERVER_INFO_1018(Structure):
    sv1018_anndelta: UInt32
class SERVER_INFO_102(Structure):
    sv102_platform_id: UInt32
    sv102_name: win32more.Foundation.PWSTR
    sv102_version_major: UInt32
    sv102_version_minor: UInt32
    sv102_type: win32more.NetworkManagement.NetManagement.NET_SERVER_TYPE
    sv102_comment: win32more.Foundation.PWSTR
    sv102_users: UInt32
    sv102_disc: Int32
    sv102_hidden: win32more.NetworkManagement.NetManagement.SERVER_INFO_HIDDEN
    sv102_announce: UInt32
    sv102_anndelta: UInt32
    sv102_licenses: UInt32
    sv102_userpath: win32more.Foundation.PWSTR
class SERVER_INFO_103(Structure):
    sv103_platform_id: UInt32
    sv103_name: win32more.Foundation.PWSTR
    sv103_version_major: UInt32
    sv103_version_minor: UInt32
    sv103_type: UInt32
    sv103_comment: win32more.Foundation.PWSTR
    sv103_users: UInt32
    sv103_disc: Int32
    sv103_hidden: win32more.Foundation.BOOL
    sv103_announce: UInt32
    sv103_anndelta: UInt32
    sv103_licenses: UInt32
    sv103_userpath: win32more.Foundation.PWSTR
    sv103_capabilities: UInt32
class SERVER_INFO_1107(Structure):
    sv1107_users: UInt32
class SERVER_INFO_1501(Structure):
    sv1501_sessopens: UInt32
class SERVER_INFO_1502(Structure):
    sv1502_sessvcs: UInt32
class SERVER_INFO_1503(Structure):
    sv1503_opensearch: UInt32
class SERVER_INFO_1506(Structure):
    sv1506_maxworkitems: UInt32
class SERVER_INFO_1509(Structure):
    sv1509_maxrawbuflen: UInt32
class SERVER_INFO_1510(Structure):
    sv1510_sessusers: UInt32
class SERVER_INFO_1511(Structure):
    sv1511_sessconns: UInt32
class SERVER_INFO_1512(Structure):
    sv1512_maxnonpagedmemoryusage: UInt32
class SERVER_INFO_1513(Structure):
    sv1513_maxpagedmemoryusage: UInt32
class SERVER_INFO_1514(Structure):
    sv1514_enablesoftcompat: win32more.Foundation.BOOL
class SERVER_INFO_1515(Structure):
    sv1515_enableforcedlogoff: win32more.Foundation.BOOL
class SERVER_INFO_1516(Structure):
    sv1516_timesource: win32more.Foundation.BOOL
class SERVER_INFO_1518(Structure):
    sv1518_lmannounce: win32more.Foundation.BOOL
class SERVER_INFO_1520(Structure):
    sv1520_maxcopyreadlen: UInt32
class SERVER_INFO_1521(Structure):
    sv1521_maxcopywritelen: UInt32
class SERVER_INFO_1522(Structure):
    sv1522_minkeepsearch: UInt32
class SERVER_INFO_1523(Structure):
    sv1523_maxkeepsearch: UInt32
class SERVER_INFO_1524(Structure):
    sv1524_minkeepcomplsearch: UInt32
class SERVER_INFO_1525(Structure):
    sv1525_maxkeepcomplsearch: UInt32
class SERVER_INFO_1528(Structure):
    sv1528_scavtimeout: UInt32
class SERVER_INFO_1529(Structure):
    sv1529_minrcvqueue: UInt32
class SERVER_INFO_1530(Structure):
    sv1530_minfreeworkitems: UInt32
class SERVER_INFO_1533(Structure):
    sv1533_maxmpxct: UInt32
class SERVER_INFO_1534(Structure):
    sv1534_oplockbreakwait: UInt32
class SERVER_INFO_1535(Structure):
    sv1535_oplockbreakresponsewait: UInt32
class SERVER_INFO_1536(Structure):
    sv1536_enableoplocks: win32more.Foundation.BOOL
class SERVER_INFO_1537(Structure):
    sv1537_enableoplockforceclose: win32more.Foundation.BOOL
class SERVER_INFO_1538(Structure):
    sv1538_enablefcbopens: win32more.Foundation.BOOL
class SERVER_INFO_1539(Structure):
    sv1539_enableraw: win32more.Foundation.BOOL
class SERVER_INFO_1540(Structure):
    sv1540_enablesharednetdrives: win32more.Foundation.BOOL
class SERVER_INFO_1541(Structure):
    sv1541_minfreeconnections: win32more.Foundation.BOOL
class SERVER_INFO_1542(Structure):
    sv1542_maxfreeconnections: win32more.Foundation.BOOL
class SERVER_INFO_1543(Structure):
    sv1543_initsesstable: UInt32
class SERVER_INFO_1544(Structure):
    sv1544_initconntable: UInt32
class SERVER_INFO_1545(Structure):
    sv1545_initfiletable: UInt32
class SERVER_INFO_1546(Structure):
    sv1546_initsearchtable: UInt32
class SERVER_INFO_1547(Structure):
    sv1547_alertschedule: UInt32
class SERVER_INFO_1548(Structure):
    sv1548_errorthreshold: UInt32
class SERVER_INFO_1549(Structure):
    sv1549_networkerrorthreshold: UInt32
class SERVER_INFO_1550(Structure):
    sv1550_diskspacethreshold: UInt32
class SERVER_INFO_1552(Structure):
    sv1552_maxlinkdelay: UInt32
class SERVER_INFO_1553(Structure):
    sv1553_minlinkthroughput: UInt32
class SERVER_INFO_1554(Structure):
    sv1554_linkinfovalidtime: UInt32
class SERVER_INFO_1555(Structure):
    sv1555_scavqosinfoupdatetime: UInt32
class SERVER_INFO_1556(Structure):
    sv1556_maxworkitemidletime: UInt32
class SERVER_INFO_1557(Structure):
    sv1557_maxrawworkitems: UInt32
class SERVER_INFO_1560(Structure):
    sv1560_producttype: UInt32
class SERVER_INFO_1561(Structure):
    sv1561_serversize: UInt32
class SERVER_INFO_1562(Structure):
    sv1562_connectionlessautodisc: UInt32
class SERVER_INFO_1563(Structure):
    sv1563_sharingviolationretries: UInt32
class SERVER_INFO_1564(Structure):
    sv1564_sharingviolationdelay: UInt32
class SERVER_INFO_1565(Structure):
    sv1565_maxglobalopensearch: UInt32
class SERVER_INFO_1566(Structure):
    sv1566_removeduplicatesearches: win32more.Foundation.BOOL
class SERVER_INFO_1567(Structure):
    sv1567_lockviolationretries: UInt32
class SERVER_INFO_1568(Structure):
    sv1568_lockviolationoffset: UInt32
class SERVER_INFO_1569(Structure):
    sv1569_lockviolationdelay: UInt32
class SERVER_INFO_1570(Structure):
    sv1570_mdlreadswitchover: UInt32
class SERVER_INFO_1571(Structure):
    sv1571_cachedopenlimit: UInt32
class SERVER_INFO_1572(Structure):
    sv1572_criticalthreads: UInt32
class SERVER_INFO_1573(Structure):
    sv1573_restrictnullsessaccess: UInt32
class SERVER_INFO_1574(Structure):
    sv1574_enablewfw311directipx: UInt32
class SERVER_INFO_1575(Structure):
    sv1575_otherqueueaffinity: UInt32
class SERVER_INFO_1576(Structure):
    sv1576_queuesamplesecs: UInt32
class SERVER_INFO_1577(Structure):
    sv1577_balancecount: UInt32
class SERVER_INFO_1578(Structure):
    sv1578_preferredaffinity: UInt32
class SERVER_INFO_1579(Structure):
    sv1579_maxfreerfcbs: UInt32
class SERVER_INFO_1580(Structure):
    sv1580_maxfreemfcbs: UInt32
class SERVER_INFO_1581(Structure):
    sv1581_maxfreemlcbs: UInt32
class SERVER_INFO_1582(Structure):
    sv1582_maxfreepagedpoolchunks: UInt32
class SERVER_INFO_1583(Structure):
    sv1583_minpagedpoolchunksize: UInt32
class SERVER_INFO_1584(Structure):
    sv1584_maxpagedpoolchunksize: UInt32
class SERVER_INFO_1585(Structure):
    sv1585_sendsfrompreferredprocessor: win32more.Foundation.BOOL
class SERVER_INFO_1586(Structure):
    sv1586_maxthreadsperqueue: UInt32
class SERVER_INFO_1587(Structure):
    sv1587_cacheddirectorylimit: UInt32
class SERVER_INFO_1588(Structure):
    sv1588_maxcopylength: UInt32
class SERVER_INFO_1590(Structure):
    sv1590_enablecompression: UInt32
class SERVER_INFO_1591(Structure):
    sv1591_autosharewks: UInt32
class SERVER_INFO_1592(Structure):
    sv1592_autosharewks: UInt32
class SERVER_INFO_1593(Structure):
    sv1593_enablesecuritysignature: UInt32
class SERVER_INFO_1594(Structure):
    sv1594_requiresecuritysignature: UInt32
class SERVER_INFO_1595(Structure):
    sv1595_minclientbuffersize: UInt32
class SERVER_INFO_1596(Structure):
    sv1596_ConnectionNoSessionsTimeout: UInt32
class SERVER_INFO_1597(Structure):
    sv1597_IdleThreadTimeOut: UInt32
class SERVER_INFO_1598(Structure):
    sv1598_enableW9xsecuritysignature: UInt32
class SERVER_INFO_1599(Structure):
    sv1598_enforcekerberosreauthentication: win32more.Foundation.BOOLEAN
class SERVER_INFO_1600(Structure):
    sv1598_disabledos: win32more.Foundation.BOOLEAN
class SERVER_INFO_1601(Structure):
    sv1598_lowdiskspaceminimum: UInt32
class SERVER_INFO_1602(Structure):
    sv_1598_disablestrictnamechecking: win32more.Foundation.BOOL
class SERVER_INFO_402(Structure):
    sv402_ulist_mtime: UInt32
    sv402_glist_mtime: UInt32
    sv402_alist_mtime: UInt32
    sv402_alerts: win32more.Foundation.PWSTR
    sv402_security: win32more.NetworkManagement.NetManagement.SERVER_INFO_SECURITY
    sv402_numadmin: UInt32
    sv402_lanmask: UInt32
    sv402_guestacct: win32more.Foundation.PWSTR
    sv402_chdevs: UInt32
    sv402_chdevq: UInt32
    sv402_chdevjobs: UInt32
    sv402_connections: UInt32
    sv402_shares: UInt32
    sv402_openfiles: UInt32
    sv402_sessopens: UInt32
    sv402_sessvcs: UInt32
    sv402_sessreqs: UInt32
    sv402_opensearch: UInt32
    sv402_activelocks: UInt32
    sv402_numreqbuf: UInt32
    sv402_sizreqbuf: UInt32
    sv402_numbigbuf: UInt32
    sv402_numfiletasks: UInt32
    sv402_alertsched: UInt32
    sv402_erroralert: UInt32
    sv402_logonalert: UInt32
    sv402_accessalert: UInt32
    sv402_diskalert: UInt32
    sv402_netioalert: UInt32
    sv402_maxauditsz: UInt32
    sv402_srvheuristics: win32more.Foundation.PWSTR
class SERVER_INFO_403(Structure):
    sv403_ulist_mtime: UInt32
    sv403_glist_mtime: UInt32
    sv403_alist_mtime: UInt32
    sv403_alerts: win32more.Foundation.PWSTR
    sv403_security: win32more.NetworkManagement.NetManagement.SERVER_INFO_SECURITY
    sv403_numadmin: UInt32
    sv403_lanmask: UInt32
    sv403_guestacct: win32more.Foundation.PWSTR
    sv403_chdevs: UInt32
    sv403_chdevq: UInt32
    sv403_chdevjobs: UInt32
    sv403_connections: UInt32
    sv403_shares: UInt32
    sv403_openfiles: UInt32
    sv403_sessopens: UInt32
    sv403_sessvcs: UInt32
    sv403_sessreqs: UInt32
    sv403_opensearch: UInt32
    sv403_activelocks: UInt32
    sv403_numreqbuf: UInt32
    sv403_sizreqbuf: UInt32
    sv403_numbigbuf: UInt32
    sv403_numfiletasks: UInt32
    sv403_alertsched: UInt32
    sv403_erroralert: UInt32
    sv403_logonalert: UInt32
    sv403_accessalert: UInt32
    sv403_diskalert: UInt32
    sv403_netioalert: UInt32
    sv403_maxauditsz: UInt32
    sv403_srvheuristics: win32more.Foundation.PWSTR
    sv403_auditedevents: UInt32
    sv403_autoprofile: UInt32
    sv403_autopath: win32more.Foundation.PWSTR
class SERVER_INFO_502(Structure):
    sv502_sessopens: UInt32
    sv502_sessvcs: UInt32
    sv502_opensearch: UInt32
    sv502_sizreqbuf: UInt32
    sv502_initworkitems: UInt32
    sv502_maxworkitems: UInt32
    sv502_rawworkitems: UInt32
    sv502_irpstacksize: UInt32
    sv502_maxrawbuflen: UInt32
    sv502_sessusers: UInt32
    sv502_sessconns: UInt32
    sv502_maxpagedmemoryusage: UInt32
    sv502_maxnonpagedmemoryusage: UInt32
    sv502_enablesoftcompat: win32more.Foundation.BOOL
    sv502_enableforcedlogoff: win32more.Foundation.BOOL
    sv502_timesource: win32more.Foundation.BOOL
    sv502_acceptdownlevelapis: win32more.Foundation.BOOL
    sv502_lmannounce: win32more.Foundation.BOOL
class SERVER_INFO_503(Structure):
    sv503_sessopens: UInt32
    sv503_sessvcs: UInt32
    sv503_opensearch: UInt32
    sv503_sizreqbuf: UInt32
    sv503_initworkitems: UInt32
    sv503_maxworkitems: UInt32
    sv503_rawworkitems: UInt32
    sv503_irpstacksize: UInt32
    sv503_maxrawbuflen: UInt32
    sv503_sessusers: UInt32
    sv503_sessconns: UInt32
    sv503_maxpagedmemoryusage: UInt32
    sv503_maxnonpagedmemoryusage: UInt32
    sv503_enablesoftcompat: win32more.Foundation.BOOL
    sv503_enableforcedlogoff: win32more.Foundation.BOOL
    sv503_timesource: win32more.Foundation.BOOL
    sv503_acceptdownlevelapis: win32more.Foundation.BOOL
    sv503_lmannounce: win32more.Foundation.BOOL
    sv503_domain: win32more.Foundation.PWSTR
    sv503_maxcopyreadlen: UInt32
    sv503_maxcopywritelen: UInt32
    sv503_minkeepsearch: UInt32
    sv503_maxkeepsearch: UInt32
    sv503_minkeepcomplsearch: UInt32
    sv503_maxkeepcomplsearch: UInt32
    sv503_threadcountadd: UInt32
    sv503_numblockthreads: UInt32
    sv503_scavtimeout: UInt32
    sv503_minrcvqueue: UInt32
    sv503_minfreeworkitems: UInt32
    sv503_xactmemsize: UInt32
    sv503_threadpriority: UInt32
    sv503_maxmpxct: UInt32
    sv503_oplockbreakwait: UInt32
    sv503_oplockbreakresponsewait: UInt32
    sv503_enableoplocks: win32more.Foundation.BOOL
    sv503_enableoplockforceclose: win32more.Foundation.BOOL
    sv503_enablefcbopens: win32more.Foundation.BOOL
    sv503_enableraw: win32more.Foundation.BOOL
    sv503_enablesharednetdrives: win32more.Foundation.BOOL
    sv503_minfreeconnections: UInt32
    sv503_maxfreeconnections: UInt32
class SERVER_INFO_598(Structure):
    sv598_maxrawworkitems: UInt32
    sv598_maxthreadsperqueue: UInt32
    sv598_producttype: UInt32
    sv598_serversize: UInt32
    sv598_connectionlessautodisc: UInt32
    sv598_sharingviolationretries: UInt32
    sv598_sharingviolationdelay: UInt32
    sv598_maxglobalopensearch: UInt32
    sv598_removeduplicatesearches: UInt32
    sv598_lockviolationoffset: UInt32
    sv598_lockviolationdelay: UInt32
    sv598_mdlreadswitchover: UInt32
    sv598_cachedopenlimit: UInt32
    sv598_otherqueueaffinity: UInt32
    sv598_restrictnullsessaccess: win32more.Foundation.BOOL
    sv598_enablewfw311directipx: win32more.Foundation.BOOL
    sv598_queuesamplesecs: UInt32
    sv598_balancecount: UInt32
    sv598_preferredaffinity: UInt32
    sv598_maxfreerfcbs: UInt32
    sv598_maxfreemfcbs: UInt32
    sv598_maxfreelfcbs: UInt32
    sv598_maxfreepagedpoolchunks: UInt32
    sv598_minpagedpoolchunksize: UInt32
    sv598_maxpagedpoolchunksize: UInt32
    sv598_sendsfrompreferredprocessor: win32more.Foundation.BOOL
    sv598_cacheddirectorylimit: UInt32
    sv598_maxcopylength: UInt32
    sv598_enablecompression: win32more.Foundation.BOOL
    sv598_autosharewks: win32more.Foundation.BOOL
    sv598_autoshareserver: win32more.Foundation.BOOL
    sv598_enablesecuritysignature: win32more.Foundation.BOOL
    sv598_requiresecuritysignature: win32more.Foundation.BOOL
    sv598_minclientbuffersize: UInt32
    sv598_serverguid: Guid
    sv598_ConnectionNoSessionsTimeout: UInt32
    sv598_IdleThreadTimeOut: UInt32
    sv598_enableW9xsecuritysignature: win32more.Foundation.BOOL
    sv598_enforcekerberosreauthentication: win32more.Foundation.BOOL
    sv598_disabledos: win32more.Foundation.BOOL
    sv598_lowdiskspaceminimum: UInt32
    sv598_disablestrictnamechecking: win32more.Foundation.BOOL
    sv598_enableauthenticateusersharing: win32more.Foundation.BOOL
class SERVER_INFO_599(Structure):
    sv599_sessopens: UInt32
    sv599_sessvcs: UInt32
    sv599_opensearch: UInt32
    sv599_sizreqbuf: UInt32
    sv599_initworkitems: UInt32
    sv599_maxworkitems: UInt32
    sv599_rawworkitems: UInt32
    sv599_irpstacksize: UInt32
    sv599_maxrawbuflen: UInt32
    sv599_sessusers: UInt32
    sv599_sessconns: UInt32
    sv599_maxpagedmemoryusage: UInt32
    sv599_maxnonpagedmemoryusage: UInt32
    sv599_enablesoftcompat: win32more.Foundation.BOOL
    sv599_enableforcedlogoff: win32more.Foundation.BOOL
    sv599_timesource: win32more.Foundation.BOOL
    sv599_acceptdownlevelapis: win32more.Foundation.BOOL
    sv599_lmannounce: win32more.Foundation.BOOL
    sv599_domain: win32more.Foundation.PWSTR
    sv599_maxcopyreadlen: UInt32
    sv599_maxcopywritelen: UInt32
    sv599_minkeepsearch: UInt32
    sv599_maxkeepsearch: UInt32
    sv599_minkeepcomplsearch: UInt32
    sv599_maxkeepcomplsearch: UInt32
    sv599_threadcountadd: UInt32
    sv599_numblockthreads: UInt32
    sv599_scavtimeout: UInt32
    sv599_minrcvqueue: UInt32
    sv599_minfreeworkitems: UInt32
    sv599_xactmemsize: UInt32
    sv599_threadpriority: UInt32
    sv599_maxmpxct: UInt32
    sv599_oplockbreakwait: UInt32
    sv599_oplockbreakresponsewait: UInt32
    sv599_enableoplocks: win32more.Foundation.BOOL
    sv599_enableoplockforceclose: win32more.Foundation.BOOL
    sv599_enablefcbopens: win32more.Foundation.BOOL
    sv599_enableraw: win32more.Foundation.BOOL
    sv599_enablesharednetdrives: win32more.Foundation.BOOL
    sv599_minfreeconnections: UInt32
    sv599_maxfreeconnections: UInt32
    sv599_initsesstable: UInt32
    sv599_initconntable: UInt32
    sv599_initfiletable: UInt32
    sv599_initsearchtable: UInt32
    sv599_alertschedule: UInt32
    sv599_errorthreshold: UInt32
    sv599_networkerrorthreshold: UInt32
    sv599_diskspacethreshold: UInt32
    sv599_reserved: UInt32
    sv599_maxlinkdelay: UInt32
    sv599_minlinkthroughput: UInt32
    sv599_linkinfovalidtime: UInt32
    sv599_scavqosinfoupdatetime: UInt32
    sv599_maxworkitemidletime: UInt32
SERVER_INFO_HIDDEN = UInt32
SV_VISIBLE: SERVER_INFO_HIDDEN = 0
SV_HIDDEN: SERVER_INFO_HIDDEN = 1
SERVER_INFO_SECURITY = UInt32
SV_SHARESECURITY: SERVER_INFO_SECURITY = 0
SV_USERSECURITY: SERVER_INFO_SECURITY = 1
class SERVER_TRANSPORT_INFO_0(Structure):
    svti0_numberofvcs: UInt32
    svti0_transportname: win32more.Foundation.PWSTR
    svti0_transportaddress: c_char_p_no
    svti0_transportaddresslength: UInt32
    svti0_networkaddress: win32more.Foundation.PWSTR
class SERVER_TRANSPORT_INFO_1(Structure):
    svti1_numberofvcs: UInt32
    svti1_transportname: win32more.Foundation.PWSTR
    svti1_transportaddress: c_char_p_no
    svti1_transportaddresslength: UInt32
    svti1_networkaddress: win32more.Foundation.PWSTR
    svti1_domain: win32more.Foundation.PWSTR
class SERVER_TRANSPORT_INFO_2(Structure):
    svti2_numberofvcs: UInt32
    svti2_transportname: win32more.Foundation.PWSTR
    svti2_transportaddress: c_char_p_no
    svti2_transportaddresslength: UInt32
    svti2_networkaddress: win32more.Foundation.PWSTR
    svti2_domain: win32more.Foundation.PWSTR
    svti2_flags: UInt32
class SERVER_TRANSPORT_INFO_3(Structure):
    svti3_numberofvcs: UInt32
    svti3_transportname: win32more.Foundation.PWSTR
    svti3_transportaddress: c_char_p_no
    svti3_transportaddresslength: UInt32
    svti3_networkaddress: win32more.Foundation.PWSTR
    svti3_domain: win32more.Foundation.PWSTR
    svti3_flags: UInt32
    svti3_passwordlength: UInt32
    svti3_password: Byte * 256
class SERVICE_INFO_0(Structure):
    svci0_name: win32more.Foundation.PWSTR
class SERVICE_INFO_1(Structure):
    svci1_name: win32more.Foundation.PWSTR
    svci1_status: UInt32
    svci1_code: UInt32
    svci1_pid: UInt32
class SERVICE_INFO_2(Structure):
    svci2_name: win32more.Foundation.PWSTR
    svci2_status: UInt32
    svci2_code: UInt32
    svci2_pid: UInt32
    svci2_text: win32more.Foundation.PWSTR
    svci2_specific_error: UInt32
    svci2_display_name: win32more.Foundation.PWSTR
class SMB_COMPRESSION_INFO(Structure):
    Switch: win32more.Foundation.BOOLEAN
    Reserved1: Byte
    Reserved2: UInt16
    Reserved3: UInt32
class SMB_TREE_CONNECT_PARAMETERS(Structure):
    EABufferOffset: UInt32
    EABufferLen: UInt32
    CreateOptions: UInt32
    TreeConnectAttributes: UInt32
class SMB_USE_OPTION_COMPRESSION_PARAMETERS(Structure):
    Tag: UInt32
    Length: UInt16
    Reserved: UInt16
class STD_ALERT(Structure):
    alrt_timestamp: UInt32
    alrt_eventname: Char * 17
    alrt_servicename: Char * 81
SUPPORTS_BINDING_INTERFACE_FLAGS = Int32
NCF_LOWER: SUPPORTS_BINDING_INTERFACE_FLAGS = 1
NCF_UPPER: SUPPORTS_BINDING_INTERFACE_FLAGS = 2
class TIME_OF_DAY_INFO(Structure):
    tod_elapsedt: UInt32
    tod_msecs: UInt32
    tod_hours: UInt32
    tod_mins: UInt32
    tod_secs: UInt32
    tod_hunds: UInt32
    tod_timezone: Int32
    tod_tinterval: UInt32
    tod_day: UInt32
    tod_month: UInt32
    tod_year: UInt32
    tod_weekday: UInt32
class TRANSPORT_INFO(Structure):
    Type: win32more.NetworkManagement.NetManagement.TRANSPORT_TYPE
    SkipCertificateCheck: win32more.Foundation.BOOLEAN
TRANSPORT_TYPE = Int32
UseTransportType_None: TRANSPORT_TYPE = 0
UseTransportType_Wsk: TRANSPORT_TYPE = 1
UseTransportType_Quic: TRANSPORT_TYPE = 2
class USE_INFO_0(Structure):
    ui0_local: win32more.Foundation.PWSTR
    ui0_remote: win32more.Foundation.PWSTR
class USE_INFO_1(Structure):
    ui1_local: win32more.Foundation.PWSTR
    ui1_remote: win32more.Foundation.PWSTR
    ui1_password: win32more.Foundation.PWSTR
    ui1_status: UInt32
    ui1_asg_type: win32more.NetworkManagement.NetManagement.USE_INFO_ASG_TYPE
    ui1_refcount: UInt32
    ui1_usecount: UInt32
class USE_INFO_2(Structure):
    ui2_local: win32more.Foundation.PWSTR
    ui2_remote: win32more.Foundation.PWSTR
    ui2_password: win32more.Foundation.PWSTR
    ui2_status: UInt32
    ui2_asg_type: win32more.NetworkManagement.NetManagement.USE_INFO_ASG_TYPE
    ui2_refcount: UInt32
    ui2_usecount: UInt32
    ui2_username: win32more.Foundation.PWSTR
    ui2_domainname: win32more.Foundation.PWSTR
class USE_INFO_3(Structure):
    ui3_ui2: win32more.NetworkManagement.NetManagement.USE_INFO_2
    ui3_flags: UInt32
class USE_INFO_4(Structure):
    ui4_ui3: win32more.NetworkManagement.NetManagement.USE_INFO_3
    ui4_auth_identity_length: UInt32
    ui4_auth_identity: c_char_p_no
class USE_INFO_5(Structure):
    ui4_ui3: win32more.NetworkManagement.NetManagement.USE_INFO_3
    ui4_auth_identity_length: UInt32
    ui4_auth_identity: c_char_p_no
    ui5_security_descriptor_length: UInt32
    ui5_security_descriptor: c_char_p_no
    ui5_use_options_length: UInt32
    ui5_use_options: c_char_p_no
USE_INFO_ASG_TYPE = UInt32
USE_WILDCARD: USE_INFO_ASG_TYPE = 4294967295
USE_DISKDEV: USE_INFO_ASG_TYPE = 0
USE_SPOOLDEV: USE_INFO_ASG_TYPE = 1
USE_IPC: USE_INFO_ASG_TYPE = 3
class USE_OPTION_DEFERRED_CONNECTION_PARAMETERS(Structure):
    Tag: UInt32
    Length: UInt16
    Reserved: UInt16
class USE_OPTION_GENERIC(Structure):
    Tag: UInt32
    Length: UInt16
    Reserved: UInt16
class USE_OPTION_PROPERTIES(Structure):
    Tag: UInt32
    pInfo: c_void_p
    Length: UIntPtr
class USE_OPTION_TRANSPORT_PARAMETERS(Structure):
    Tag: UInt32
    Length: UInt16
    Reserved: UInt16
USER_ACCOUNT_FLAGS = UInt32
UF_SCRIPT: USER_ACCOUNT_FLAGS = 1
UF_ACCOUNTDISABLE: USER_ACCOUNT_FLAGS = 2
UF_HOMEDIR_REQUIRED: USER_ACCOUNT_FLAGS = 8
UF_PASSWD_NOTREQD: USER_ACCOUNT_FLAGS = 32
UF_PASSWD_CANT_CHANGE: USER_ACCOUNT_FLAGS = 64
UF_LOCKOUT: USER_ACCOUNT_FLAGS = 16
UF_DONT_EXPIRE_PASSWD: USER_ACCOUNT_FLAGS = 65536
UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED: USER_ACCOUNT_FLAGS = 128
UF_NOT_DELEGATED: USER_ACCOUNT_FLAGS = 1048576
UF_SMARTCARD_REQUIRED: USER_ACCOUNT_FLAGS = 262144
UF_USE_DES_KEY_ONLY: USER_ACCOUNT_FLAGS = 2097152
UF_DONT_REQUIRE_PREAUTH: USER_ACCOUNT_FLAGS = 4194304
UF_TRUSTED_FOR_DELEGATION: USER_ACCOUNT_FLAGS = 524288
UF_PASSWORD_EXPIRED: USER_ACCOUNT_FLAGS = 8388608
UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION: USER_ACCOUNT_FLAGS = 16777216
class USER_INFO_0(Structure):
    usri0_name: win32more.Foundation.PWSTR
class USER_INFO_1(Structure):
    usri1_name: win32more.Foundation.PWSTR
    usri1_password: win32more.Foundation.PWSTR
    usri1_password_age: UInt32
    usri1_priv: win32more.NetworkManagement.NetManagement.USER_PRIV
    usri1_home_dir: win32more.Foundation.PWSTR
    usri1_comment: win32more.Foundation.PWSTR
    usri1_flags: win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri1_script_path: win32more.Foundation.PWSTR
class USER_INFO_10(Structure):
    usri10_name: win32more.Foundation.PWSTR
    usri10_comment: win32more.Foundation.PWSTR
    usri10_usr_comment: win32more.Foundation.PWSTR
    usri10_full_name: win32more.Foundation.PWSTR
class USER_INFO_1003(Structure):
    usri1003_password: win32more.Foundation.PWSTR
class USER_INFO_1005(Structure):
    usri1005_priv: win32more.NetworkManagement.NetManagement.USER_PRIV
class USER_INFO_1006(Structure):
    usri1006_home_dir: win32more.Foundation.PWSTR
class USER_INFO_1007(Structure):
    usri1007_comment: win32more.Foundation.PWSTR
class USER_INFO_1008(Structure):
    usri1008_flags: win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
class USER_INFO_1009(Structure):
    usri1009_script_path: win32more.Foundation.PWSTR
class USER_INFO_1010(Structure):
    usri1010_auth_flags: win32more.NetworkManagement.NetManagement.AF_OP
class USER_INFO_1011(Structure):
    usri1011_full_name: win32more.Foundation.PWSTR
class USER_INFO_1012(Structure):
    usri1012_usr_comment: win32more.Foundation.PWSTR
class USER_INFO_1013(Structure):
    usri1013_parms: win32more.Foundation.PWSTR
class USER_INFO_1014(Structure):
    usri1014_workstations: win32more.Foundation.PWSTR
class USER_INFO_1017(Structure):
    usri1017_acct_expires: UInt32
class USER_INFO_1018(Structure):
    usri1018_max_storage: UInt32
class USER_INFO_1020(Structure):
    usri1020_units_per_week: UInt32
    usri1020_logon_hours: c_char_p_no
class USER_INFO_1023(Structure):
    usri1023_logon_server: win32more.Foundation.PWSTR
class USER_INFO_1024(Structure):
    usri1024_country_code: UInt32
class USER_INFO_1025(Structure):
    usri1025_code_page: UInt32
class USER_INFO_1051(Structure):
    usri1051_primary_group_id: UInt32
class USER_INFO_1052(Structure):
    usri1052_profile: win32more.Foundation.PWSTR
class USER_INFO_1053(Structure):
    usri1053_home_dir_drive: win32more.Foundation.PWSTR
class USER_INFO_11(Structure):
    usri11_name: win32more.Foundation.PWSTR
    usri11_comment: win32more.Foundation.PWSTR
    usri11_usr_comment: win32more.Foundation.PWSTR
    usri11_full_name: win32more.Foundation.PWSTR
    usri11_priv: win32more.NetworkManagement.NetManagement.USER_PRIV
    usri11_auth_flags: win32more.NetworkManagement.NetManagement.AF_OP
    usri11_password_age: UInt32
    usri11_home_dir: win32more.Foundation.PWSTR
    usri11_parms: win32more.Foundation.PWSTR
    usri11_last_logon: UInt32
    usri11_last_logoff: UInt32
    usri11_bad_pw_count: UInt32
    usri11_num_logons: UInt32
    usri11_logon_server: win32more.Foundation.PWSTR
    usri11_country_code: UInt32
    usri11_workstations: win32more.Foundation.PWSTR
    usri11_max_storage: UInt32
    usri11_units_per_week: UInt32
    usri11_logon_hours: c_char_p_no
    usri11_code_page: UInt32
class USER_INFO_2(Structure):
    usri2_name: win32more.Foundation.PWSTR
    usri2_password: win32more.Foundation.PWSTR
    usri2_password_age: UInt32
    usri2_priv: win32more.NetworkManagement.NetManagement.USER_PRIV
    usri2_home_dir: win32more.Foundation.PWSTR
    usri2_comment: win32more.Foundation.PWSTR
    usri2_flags: win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri2_script_path: win32more.Foundation.PWSTR
    usri2_auth_flags: win32more.NetworkManagement.NetManagement.AF_OP
    usri2_full_name: win32more.Foundation.PWSTR
    usri2_usr_comment: win32more.Foundation.PWSTR
    usri2_parms: win32more.Foundation.PWSTR
    usri2_workstations: win32more.Foundation.PWSTR
    usri2_last_logon: UInt32
    usri2_last_logoff: UInt32
    usri2_acct_expires: UInt32
    usri2_max_storage: UInt32
    usri2_units_per_week: UInt32
    usri2_logon_hours: c_char_p_no
    usri2_bad_pw_count: UInt32
    usri2_num_logons: UInt32
    usri2_logon_server: win32more.Foundation.PWSTR
    usri2_country_code: UInt32
    usri2_code_page: UInt32
class USER_INFO_20(Structure):
    usri20_name: win32more.Foundation.PWSTR
    usri20_full_name: win32more.Foundation.PWSTR
    usri20_comment: win32more.Foundation.PWSTR
    usri20_flags: win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri20_user_id: UInt32
class USER_INFO_21(Structure):
    usri21_password: Byte * 16
class USER_INFO_22(Structure):
    usri22_name: win32more.Foundation.PWSTR
    usri22_password: Byte * 16
    usri22_password_age: UInt32
    usri22_priv: win32more.NetworkManagement.NetManagement.USER_PRIV
    usri22_home_dir: win32more.Foundation.PWSTR
    usri22_comment: win32more.Foundation.PWSTR
    usri22_flags: win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri22_script_path: win32more.Foundation.PWSTR
    usri22_auth_flags: win32more.NetworkManagement.NetManagement.AF_OP
    usri22_full_name: win32more.Foundation.PWSTR
    usri22_usr_comment: win32more.Foundation.PWSTR
    usri22_parms: win32more.Foundation.PWSTR
    usri22_workstations: win32more.Foundation.PWSTR
    usri22_last_logon: UInt32
    usri22_last_logoff: UInt32
    usri22_acct_expires: UInt32
    usri22_max_storage: UInt32
    usri22_units_per_week: UInt32
    usri22_logon_hours: c_char_p_no
    usri22_bad_pw_count: UInt32
    usri22_num_logons: UInt32
    usri22_logon_server: win32more.Foundation.PWSTR
    usri22_country_code: UInt32
    usri22_code_page: UInt32
class USER_INFO_23(Structure):
    usri23_name: win32more.Foundation.PWSTR
    usri23_full_name: win32more.Foundation.PWSTR
    usri23_comment: win32more.Foundation.PWSTR
    usri23_flags: win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri23_user_sid: win32more.Foundation.PSID
class USER_INFO_24(Structure):
    usri24_internet_identity: win32more.Foundation.BOOL
    usri24_flags: UInt32
    usri24_internet_provider_name: win32more.Foundation.PWSTR
    usri24_internet_principal_name: win32more.Foundation.PWSTR
    usri24_user_sid: win32more.Foundation.PSID
class USER_INFO_3(Structure):
    usri3_name: win32more.Foundation.PWSTR
    usri3_password: win32more.Foundation.PWSTR
    usri3_password_age: UInt32
    usri3_priv: win32more.NetworkManagement.NetManagement.USER_PRIV
    usri3_home_dir: win32more.Foundation.PWSTR
    usri3_comment: win32more.Foundation.PWSTR
    usri3_flags: win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri3_script_path: win32more.Foundation.PWSTR
    usri3_auth_flags: win32more.NetworkManagement.NetManagement.AF_OP
    usri3_full_name: win32more.Foundation.PWSTR
    usri3_usr_comment: win32more.Foundation.PWSTR
    usri3_parms: win32more.Foundation.PWSTR
    usri3_workstations: win32more.Foundation.PWSTR
    usri3_last_logon: UInt32
    usri3_last_logoff: UInt32
    usri3_acct_expires: UInt32
    usri3_max_storage: UInt32
    usri3_units_per_week: UInt32
    usri3_logon_hours: c_char_p_no
    usri3_bad_pw_count: UInt32
    usri3_num_logons: UInt32
    usri3_logon_server: win32more.Foundation.PWSTR
    usri3_country_code: UInt32
    usri3_code_page: UInt32
    usri3_user_id: UInt32
    usri3_primary_group_id: UInt32
    usri3_profile: win32more.Foundation.PWSTR
    usri3_home_dir_drive: win32more.Foundation.PWSTR
    usri3_password_expired: UInt32
class USER_INFO_4(Structure):
    usri4_name: win32more.Foundation.PWSTR
    usri4_password: win32more.Foundation.PWSTR
    usri4_password_age: UInt32
    usri4_priv: win32more.NetworkManagement.NetManagement.USER_PRIV
    usri4_home_dir: win32more.Foundation.PWSTR
    usri4_comment: win32more.Foundation.PWSTR
    usri4_flags: win32more.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri4_script_path: win32more.Foundation.PWSTR
    usri4_auth_flags: win32more.NetworkManagement.NetManagement.AF_OP
    usri4_full_name: win32more.Foundation.PWSTR
    usri4_usr_comment: win32more.Foundation.PWSTR
    usri4_parms: win32more.Foundation.PWSTR
    usri4_workstations: win32more.Foundation.PWSTR
    usri4_last_logon: UInt32
    usri4_last_logoff: UInt32
    usri4_acct_expires: UInt32
    usri4_max_storage: UInt32
    usri4_units_per_week: UInt32
    usri4_logon_hours: c_char_p_no
    usri4_bad_pw_count: UInt32
    usri4_num_logons: UInt32
    usri4_logon_server: win32more.Foundation.PWSTR
    usri4_country_code: UInt32
    usri4_code_page: UInt32
    usri4_user_sid: win32more.Foundation.PSID
    usri4_primary_group_id: UInt32
    usri4_profile: win32more.Foundation.PWSTR
    usri4_home_dir_drive: win32more.Foundation.PWSTR
    usri4_password_expired: UInt32
class USER_MODALS_INFO_0(Structure):
    usrmod0_min_passwd_len: UInt32
    usrmod0_max_passwd_age: UInt32
    usrmod0_min_passwd_age: UInt32
    usrmod0_force_logoff: UInt32
    usrmod0_password_hist_len: UInt32
class USER_MODALS_INFO_1(Structure):
    usrmod1_role: UInt32
    usrmod1_primary: win32more.Foundation.PWSTR
class USER_MODALS_INFO_1001(Structure):
    usrmod1001_min_passwd_len: UInt32
class USER_MODALS_INFO_1002(Structure):
    usrmod1002_max_passwd_age: UInt32
class USER_MODALS_INFO_1003(Structure):
    usrmod1003_min_passwd_age: UInt32
class USER_MODALS_INFO_1004(Structure):
    usrmod1004_force_logoff: UInt32
class USER_MODALS_INFO_1005(Structure):
    usrmod1005_password_hist_len: UInt32
class USER_MODALS_INFO_1006(Structure):
    usrmod1006_role: win32more.NetworkManagement.NetManagement.USER_MODALS_ROLES
class USER_MODALS_INFO_1007(Structure):
    usrmod1007_primary: win32more.Foundation.PWSTR
class USER_MODALS_INFO_2(Structure):
    usrmod2_domain_name: win32more.Foundation.PWSTR
    usrmod2_domain_id: win32more.Foundation.PSID
class USER_MODALS_INFO_3(Structure):
    usrmod3_lockout_duration: UInt32
    usrmod3_lockout_observation_window: UInt32
    usrmod3_lockout_threshold: UInt32
USER_MODALS_ROLES = UInt32
UAS_ROLE_STANDALONE: USER_MODALS_ROLES = 0
UAS_ROLE_MEMBER: USER_MODALS_ROLES = 1
UAS_ROLE_BACKUP: USER_MODALS_ROLES = 2
UAS_ROLE_PRIMARY: USER_MODALS_ROLES = 3
class USER_OTHER_INFO(Structure):
    alrtus_errcode: UInt32
    alrtus_numstrings: UInt32
USER_PRIV = UInt32
USER_PRIV_GUEST: USER_PRIV = 0
USER_PRIV_USER: USER_PRIV = 1
USER_PRIV_ADMIN: USER_PRIV = 2
class WKSTA_INFO_100(Structure):
    wki100_platform_id: UInt32
    wki100_computername: win32more.Foundation.PWSTR
    wki100_langroup: win32more.Foundation.PWSTR
    wki100_ver_major: UInt32
    wki100_ver_minor: UInt32
class WKSTA_INFO_101(Structure):
    wki101_platform_id: UInt32
    wki101_computername: win32more.Foundation.PWSTR
    wki101_langroup: win32more.Foundation.PWSTR
    wki101_ver_major: UInt32
    wki101_ver_minor: UInt32
    wki101_lanroot: win32more.Foundation.PWSTR
class WKSTA_INFO_1010(Structure):
    wki1010_char_wait: UInt32
class WKSTA_INFO_1011(Structure):
    wki1011_collection_time: UInt32
class WKSTA_INFO_1012(Structure):
    wki1012_maximum_collection_count: UInt32
class WKSTA_INFO_1013(Structure):
    wki1013_keep_conn: UInt32
class WKSTA_INFO_1018(Structure):
    wki1018_sess_timeout: UInt32
class WKSTA_INFO_102(Structure):
    wki102_platform_id: UInt32
    wki102_computername: win32more.Foundation.PWSTR
    wki102_langroup: win32more.Foundation.PWSTR
    wki102_ver_major: UInt32
    wki102_ver_minor: UInt32
    wki102_lanroot: win32more.Foundation.PWSTR
    wki102_logged_on_users: UInt32
class WKSTA_INFO_1023(Structure):
    wki1023_siz_char_buf: UInt32
class WKSTA_INFO_1027(Structure):
    wki1027_errlog_sz: UInt32
class WKSTA_INFO_1028(Structure):
    wki1028_print_buf_time: UInt32
class WKSTA_INFO_1032(Structure):
    wki1032_wrk_heuristics: UInt32
class WKSTA_INFO_1033(Structure):
    wki1033_max_threads: UInt32
class WKSTA_INFO_1041(Structure):
    wki1041_lock_quota: UInt32
class WKSTA_INFO_1042(Structure):
    wki1042_lock_increment: UInt32
class WKSTA_INFO_1043(Structure):
    wki1043_lock_maximum: UInt32
class WKSTA_INFO_1044(Structure):
    wki1044_pipe_increment: UInt32
class WKSTA_INFO_1045(Structure):
    wki1045_pipe_maximum: UInt32
class WKSTA_INFO_1046(Structure):
    wki1046_dormant_file_limit: UInt32
class WKSTA_INFO_1047(Structure):
    wki1047_cache_file_timeout: UInt32
class WKSTA_INFO_1048(Structure):
    wki1048_use_opportunistic_locking: win32more.Foundation.BOOL
class WKSTA_INFO_1049(Structure):
    wki1049_use_unlock_behind: win32more.Foundation.BOOL
class WKSTA_INFO_1050(Structure):
    wki1050_use_close_behind: win32more.Foundation.BOOL
class WKSTA_INFO_1051(Structure):
    wki1051_buf_named_pipes: win32more.Foundation.BOOL
class WKSTA_INFO_1052(Structure):
    wki1052_use_lock_read_unlock: win32more.Foundation.BOOL
class WKSTA_INFO_1053(Structure):
    wki1053_utilize_nt_caching: win32more.Foundation.BOOL
class WKSTA_INFO_1054(Structure):
    wki1054_use_raw_read: win32more.Foundation.BOOL
class WKSTA_INFO_1055(Structure):
    wki1055_use_raw_write: win32more.Foundation.BOOL
class WKSTA_INFO_1056(Structure):
    wki1056_use_write_raw_data: win32more.Foundation.BOOL
class WKSTA_INFO_1057(Structure):
    wki1057_use_encryption: win32more.Foundation.BOOL
class WKSTA_INFO_1058(Structure):
    wki1058_buf_files_deny_write: win32more.Foundation.BOOL
class WKSTA_INFO_1059(Structure):
    wki1059_buf_read_only_files: win32more.Foundation.BOOL
class WKSTA_INFO_1060(Structure):
    wki1060_force_core_create_mode: win32more.Foundation.BOOL
class WKSTA_INFO_1061(Structure):
    wki1061_use_512_byte_max_transfer: win32more.Foundation.BOOL
class WKSTA_INFO_1062(Structure):
    wki1062_read_ahead_throughput: UInt32
class WKSTA_INFO_302(Structure):
    wki302_char_wait: UInt32
    wki302_collection_time: UInt32
    wki302_maximum_collection_count: UInt32
    wki302_keep_conn: UInt32
    wki302_keep_search: UInt32
    wki302_max_cmds: UInt32
    wki302_num_work_buf: UInt32
    wki302_siz_work_buf: UInt32
    wki302_max_wrk_cache: UInt32
    wki302_sess_timeout: UInt32
    wki302_siz_error: UInt32
    wki302_num_alerts: UInt32
    wki302_num_services: UInt32
    wki302_errlog_sz: UInt32
    wki302_print_buf_time: UInt32
    wki302_num_char_buf: UInt32
    wki302_siz_char_buf: UInt32
    wki302_wrk_heuristics: win32more.Foundation.PWSTR
    wki302_mailslots: UInt32
    wki302_num_dgram_buf: UInt32
class WKSTA_INFO_402(Structure):
    wki402_char_wait: UInt32
    wki402_collection_time: UInt32
    wki402_maximum_collection_count: UInt32
    wki402_keep_conn: UInt32
    wki402_keep_search: UInt32
    wki402_max_cmds: UInt32
    wki402_num_work_buf: UInt32
    wki402_siz_work_buf: UInt32
    wki402_max_wrk_cache: UInt32
    wki402_sess_timeout: UInt32
    wki402_siz_error: UInt32
    wki402_num_alerts: UInt32
    wki402_num_services: UInt32
    wki402_errlog_sz: UInt32
    wki402_print_buf_time: UInt32
    wki402_num_char_buf: UInt32
    wki402_siz_char_buf: UInt32
    wki402_wrk_heuristics: win32more.Foundation.PWSTR
    wki402_mailslots: UInt32
    wki402_num_dgram_buf: UInt32
    wki402_max_threads: UInt32
class WKSTA_INFO_502(Structure):
    wki502_char_wait: UInt32
    wki502_collection_time: UInt32
    wki502_maximum_collection_count: UInt32
    wki502_keep_conn: UInt32
    wki502_max_cmds: UInt32
    wki502_sess_timeout: UInt32
    wki502_siz_char_buf: UInt32
    wki502_max_threads: UInt32
    wki502_lock_quota: UInt32
    wki502_lock_increment: UInt32
    wki502_lock_maximum: UInt32
    wki502_pipe_increment: UInt32
    wki502_pipe_maximum: UInt32
    wki502_cache_file_timeout: UInt32
    wki502_dormant_file_limit: UInt32
    wki502_read_ahead_throughput: UInt32
    wki502_num_mailslot_buffers: UInt32
    wki502_num_srv_announce_buffers: UInt32
    wki502_max_illegal_datagram_events: UInt32
    wki502_illegal_datagram_event_reset_frequency: UInt32
    wki502_log_election_packets: win32more.Foundation.BOOL
    wki502_use_opportunistic_locking: win32more.Foundation.BOOL
    wki502_use_unlock_behind: win32more.Foundation.BOOL
    wki502_use_close_behind: win32more.Foundation.BOOL
    wki502_buf_named_pipes: win32more.Foundation.BOOL
    wki502_use_lock_read_unlock: win32more.Foundation.BOOL
    wki502_utilize_nt_caching: win32more.Foundation.BOOL
    wki502_use_raw_read: win32more.Foundation.BOOL
    wki502_use_raw_write: win32more.Foundation.BOOL
    wki502_use_write_raw_data: win32more.Foundation.BOOL
    wki502_use_encryption: win32more.Foundation.BOOL
    wki502_buf_files_deny_write: win32more.Foundation.BOOL
    wki502_buf_read_only_files: win32more.Foundation.BOOL
    wki502_force_core_create_mode: win32more.Foundation.BOOL
    wki502_use_512_byte_max_transfer: win32more.Foundation.BOOL
class WKSTA_TRANSPORT_INFO_0(Structure):
    wkti0_quality_of_service: UInt32
    wkti0_number_of_vcs: UInt32
    wkti0_transport_name: win32more.Foundation.PWSTR
    wkti0_transport_address: win32more.Foundation.PWSTR
    wkti0_wan_ish: win32more.Foundation.BOOL
class WKSTA_USER_INFO_0(Structure):
    wkui0_username: win32more.Foundation.PWSTR
class WKSTA_USER_INFO_1(Structure):
    wkui1_username: win32more.Foundation.PWSTR
    wkui1_logon_domain: win32more.Foundation.PWSTR
    wkui1_oth_domains: win32more.Foundation.PWSTR
    wkui1_logon_server: win32more.Foundation.PWSTR
class WKSTA_USER_INFO_1101(Structure):
    wkui1101_oth_domains: win32more.Foundation.PWSTR
@winfunctype_pointer
def WORKERFUNCTION(param0: c_void_p) -> Void: ...
make_head(_module, 'ACCESS_INFO_0')
make_head(_module, 'ACCESS_INFO_1')
make_head(_module, 'ACCESS_INFO_1002')
make_head(_module, 'ACCESS_LIST')
make_head(_module, 'ADMIN_OTHER_INFO')
make_head(_module, 'AE_ACCLIM')
make_head(_module, 'AE_ACLMOD')
make_head(_module, 'AE_CLOSEFILE')
make_head(_module, 'AE_CONNREJ')
make_head(_module, 'AE_CONNSTART')
make_head(_module, 'AE_CONNSTOP')
make_head(_module, 'AE_GENERIC')
make_head(_module, 'AE_LOCKOUT')
make_head(_module, 'AE_NETLOGOFF')
make_head(_module, 'AE_NETLOGON')
make_head(_module, 'AE_RESACCESS')
make_head(_module, 'AE_RESACCESSREJ')
make_head(_module, 'AE_SERVICESTAT')
make_head(_module, 'AE_SESSLOGOFF')
make_head(_module, 'AE_SESSLOGON')
make_head(_module, 'AE_SESSPWERR')
make_head(_module, 'AE_SRVSTATUS')
make_head(_module, 'AE_UASMOD')
make_head(_module, 'AT_ENUM')
make_head(_module, 'AT_INFO')
make_head(_module, 'AUDIT_ENTRY')
make_head(_module, 'CONFIG_INFO_0')
make_head(_module, 'DSREG_JOIN_INFO')
make_head(_module, 'DSREG_USER_INFO')
make_head(_module, 'ERRLOG_OTHER_INFO')
make_head(_module, 'ERROR_LOG')
make_head(_module, 'FLAT_STRING')
make_head(_module, 'GROUP_INFO_0')
make_head(_module, 'GROUP_INFO_1')
make_head(_module, 'GROUP_INFO_1002')
make_head(_module, 'GROUP_INFO_1005')
make_head(_module, 'GROUP_INFO_2')
make_head(_module, 'GROUP_INFO_3')
make_head(_module, 'GROUP_USERS_INFO_0')
make_head(_module, 'GROUP_USERS_INFO_1')
make_head(_module, 'HARDWARE_ADDRESS')
make_head(_module, 'HLOG')
make_head(_module, 'IEnumNetCfgBindingInterface')
make_head(_module, 'IEnumNetCfgBindingPath')
make_head(_module, 'IEnumNetCfgComponent')
make_head(_module, 'INetCfg')
make_head(_module, 'INetCfgBindingInterface')
make_head(_module, 'INetCfgBindingPath')
make_head(_module, 'INetCfgClass')
make_head(_module, 'INetCfgClassSetup')
make_head(_module, 'INetCfgClassSetup2')
make_head(_module, 'INetCfgComponent')
make_head(_module, 'INetCfgComponentBindings')
make_head(_module, 'INetCfgComponentControl')
make_head(_module, 'INetCfgComponentNotifyBinding')
make_head(_module, 'INetCfgComponentNotifyGlobal')
make_head(_module, 'INetCfgComponentPropertyUi')
make_head(_module, 'INetCfgComponentSetup')
make_head(_module, 'INetCfgComponentSysPrep')
make_head(_module, 'INetCfgComponentUpperEdge')
make_head(_module, 'INetCfgLock')
make_head(_module, 'INetCfgPnpReconfigCallback')
make_head(_module, 'INetCfgSysPrep')
make_head(_module, 'INetLanConnectionUiInfo')
make_head(_module, 'INetRasConnectionIpUiInfo')
make_head(_module, 'IProvisioningDomain')
make_head(_module, 'IProvisioningProfileWireless')
make_head(_module, 'LOCALGROUP_INFO_0')
make_head(_module, 'LOCALGROUP_INFO_1')
make_head(_module, 'LOCALGROUP_INFO_1002')
make_head(_module, 'LOCALGROUP_MEMBERS_INFO_0')
make_head(_module, 'LOCALGROUP_MEMBERS_INFO_1')
make_head(_module, 'LOCALGROUP_MEMBERS_INFO_2')
make_head(_module, 'LOCALGROUP_MEMBERS_INFO_3')
make_head(_module, 'LOCALGROUP_USERS_INFO_0')
make_head(_module, 'MPR_PROTOCOL_0')
make_head(_module, 'MSA_INFO_0')
make_head(_module, 'MSG_INFO_0')
make_head(_module, 'MSG_INFO_1')
make_head(_module, 'NET_DISPLAY_GROUP')
make_head(_module, 'NET_DISPLAY_MACHINE')
make_head(_module, 'NET_DISPLAY_USER')
make_head(_module, 'NET_VALIDATE_AUTHENTICATION_INPUT_ARG')
make_head(_module, 'NET_VALIDATE_OUTPUT_ARG')
make_head(_module, 'NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG')
make_head(_module, 'NET_VALIDATE_PASSWORD_HASH')
make_head(_module, 'NET_VALIDATE_PASSWORD_RESET_INPUT_ARG')
make_head(_module, 'NET_VALIDATE_PERSISTED_FIELDS')
make_head(_module, 'NETLOGON_INFO_1')
make_head(_module, 'NETLOGON_INFO_2')
make_head(_module, 'NETLOGON_INFO_3')
make_head(_module, 'NETLOGON_INFO_4')
make_head(_module, 'NETSETUP_PROVISIONING_PARAMS')
make_head(_module, 'NETWORK_NAME')
make_head(_module, 'OBO_TOKEN')
make_head(_module, 'PRINT_OTHER_INFO')
make_head(_module, 'RASCON_IPUI')
make_head(_module, 'REPL_EDIR_INFO_0')
make_head(_module, 'REPL_EDIR_INFO_1')
make_head(_module, 'REPL_EDIR_INFO_1000')
make_head(_module, 'REPL_EDIR_INFO_1001')
make_head(_module, 'REPL_EDIR_INFO_2')
make_head(_module, 'REPL_IDIR_INFO_0')
make_head(_module, 'REPL_IDIR_INFO_1')
make_head(_module, 'REPL_INFO_0')
make_head(_module, 'REPL_INFO_1000')
make_head(_module, 'REPL_INFO_1001')
make_head(_module, 'REPL_INFO_1002')
make_head(_module, 'REPL_INFO_1003')
make_head(_module, 'RTR_INFO_BLOCK_HEADER')
make_head(_module, 'RTR_TOC_ENTRY')
make_head(_module, 'SERVER_INFO_100')
make_head(_module, 'SERVER_INFO_1005')
make_head(_module, 'SERVER_INFO_101')
make_head(_module, 'SERVER_INFO_1010')
make_head(_module, 'SERVER_INFO_1016')
make_head(_module, 'SERVER_INFO_1017')
make_head(_module, 'SERVER_INFO_1018')
make_head(_module, 'SERVER_INFO_102')
make_head(_module, 'SERVER_INFO_103')
make_head(_module, 'SERVER_INFO_1107')
make_head(_module, 'SERVER_INFO_1501')
make_head(_module, 'SERVER_INFO_1502')
make_head(_module, 'SERVER_INFO_1503')
make_head(_module, 'SERVER_INFO_1506')
make_head(_module, 'SERVER_INFO_1509')
make_head(_module, 'SERVER_INFO_1510')
make_head(_module, 'SERVER_INFO_1511')
make_head(_module, 'SERVER_INFO_1512')
make_head(_module, 'SERVER_INFO_1513')
make_head(_module, 'SERVER_INFO_1514')
make_head(_module, 'SERVER_INFO_1515')
make_head(_module, 'SERVER_INFO_1516')
make_head(_module, 'SERVER_INFO_1518')
make_head(_module, 'SERVER_INFO_1520')
make_head(_module, 'SERVER_INFO_1521')
make_head(_module, 'SERVER_INFO_1522')
make_head(_module, 'SERVER_INFO_1523')
make_head(_module, 'SERVER_INFO_1524')
make_head(_module, 'SERVER_INFO_1525')
make_head(_module, 'SERVER_INFO_1528')
make_head(_module, 'SERVER_INFO_1529')
make_head(_module, 'SERVER_INFO_1530')
make_head(_module, 'SERVER_INFO_1533')
make_head(_module, 'SERVER_INFO_1534')
make_head(_module, 'SERVER_INFO_1535')
make_head(_module, 'SERVER_INFO_1536')
make_head(_module, 'SERVER_INFO_1537')
make_head(_module, 'SERVER_INFO_1538')
make_head(_module, 'SERVER_INFO_1539')
make_head(_module, 'SERVER_INFO_1540')
make_head(_module, 'SERVER_INFO_1541')
make_head(_module, 'SERVER_INFO_1542')
make_head(_module, 'SERVER_INFO_1543')
make_head(_module, 'SERVER_INFO_1544')
make_head(_module, 'SERVER_INFO_1545')
make_head(_module, 'SERVER_INFO_1546')
make_head(_module, 'SERVER_INFO_1547')
make_head(_module, 'SERVER_INFO_1548')
make_head(_module, 'SERVER_INFO_1549')
make_head(_module, 'SERVER_INFO_1550')
make_head(_module, 'SERVER_INFO_1552')
make_head(_module, 'SERVER_INFO_1553')
make_head(_module, 'SERVER_INFO_1554')
make_head(_module, 'SERVER_INFO_1555')
make_head(_module, 'SERVER_INFO_1556')
make_head(_module, 'SERVER_INFO_1557')
make_head(_module, 'SERVER_INFO_1560')
make_head(_module, 'SERVER_INFO_1561')
make_head(_module, 'SERVER_INFO_1562')
make_head(_module, 'SERVER_INFO_1563')
make_head(_module, 'SERVER_INFO_1564')
make_head(_module, 'SERVER_INFO_1565')
make_head(_module, 'SERVER_INFO_1566')
make_head(_module, 'SERVER_INFO_1567')
make_head(_module, 'SERVER_INFO_1568')
make_head(_module, 'SERVER_INFO_1569')
make_head(_module, 'SERVER_INFO_1570')
make_head(_module, 'SERVER_INFO_1571')
make_head(_module, 'SERVER_INFO_1572')
make_head(_module, 'SERVER_INFO_1573')
make_head(_module, 'SERVER_INFO_1574')
make_head(_module, 'SERVER_INFO_1575')
make_head(_module, 'SERVER_INFO_1576')
make_head(_module, 'SERVER_INFO_1577')
make_head(_module, 'SERVER_INFO_1578')
make_head(_module, 'SERVER_INFO_1579')
make_head(_module, 'SERVER_INFO_1580')
make_head(_module, 'SERVER_INFO_1581')
make_head(_module, 'SERVER_INFO_1582')
make_head(_module, 'SERVER_INFO_1583')
make_head(_module, 'SERVER_INFO_1584')
make_head(_module, 'SERVER_INFO_1585')
make_head(_module, 'SERVER_INFO_1586')
make_head(_module, 'SERVER_INFO_1587')
make_head(_module, 'SERVER_INFO_1588')
make_head(_module, 'SERVER_INFO_1590')
make_head(_module, 'SERVER_INFO_1591')
make_head(_module, 'SERVER_INFO_1592')
make_head(_module, 'SERVER_INFO_1593')
make_head(_module, 'SERVER_INFO_1594')
make_head(_module, 'SERVER_INFO_1595')
make_head(_module, 'SERVER_INFO_1596')
make_head(_module, 'SERVER_INFO_1597')
make_head(_module, 'SERVER_INFO_1598')
make_head(_module, 'SERVER_INFO_1599')
make_head(_module, 'SERVER_INFO_1600')
make_head(_module, 'SERVER_INFO_1601')
make_head(_module, 'SERVER_INFO_1602')
make_head(_module, 'SERVER_INFO_402')
make_head(_module, 'SERVER_INFO_403')
make_head(_module, 'SERVER_INFO_502')
make_head(_module, 'SERVER_INFO_503')
make_head(_module, 'SERVER_INFO_598')
make_head(_module, 'SERVER_INFO_599')
make_head(_module, 'SERVER_TRANSPORT_INFO_0')
make_head(_module, 'SERVER_TRANSPORT_INFO_1')
make_head(_module, 'SERVER_TRANSPORT_INFO_2')
make_head(_module, 'SERVER_TRANSPORT_INFO_3')
make_head(_module, 'SERVICE_INFO_0')
make_head(_module, 'SERVICE_INFO_1')
make_head(_module, 'SERVICE_INFO_2')
make_head(_module, 'SMB_COMPRESSION_INFO')
make_head(_module, 'SMB_TREE_CONNECT_PARAMETERS')
make_head(_module, 'SMB_USE_OPTION_COMPRESSION_PARAMETERS')
make_head(_module, 'STD_ALERT')
make_head(_module, 'TIME_OF_DAY_INFO')
make_head(_module, 'TRANSPORT_INFO')
make_head(_module, 'USE_INFO_0')
make_head(_module, 'USE_INFO_1')
make_head(_module, 'USE_INFO_2')
make_head(_module, 'USE_INFO_3')
make_head(_module, 'USE_INFO_4')
make_head(_module, 'USE_INFO_5')
make_head(_module, 'USE_OPTION_DEFERRED_CONNECTION_PARAMETERS')
make_head(_module, 'USE_OPTION_GENERIC')
make_head(_module, 'USE_OPTION_PROPERTIES')
make_head(_module, 'USE_OPTION_TRANSPORT_PARAMETERS')
make_head(_module, 'USER_INFO_0')
make_head(_module, 'USER_INFO_1')
make_head(_module, 'USER_INFO_10')
make_head(_module, 'USER_INFO_1003')
make_head(_module, 'USER_INFO_1005')
make_head(_module, 'USER_INFO_1006')
make_head(_module, 'USER_INFO_1007')
make_head(_module, 'USER_INFO_1008')
make_head(_module, 'USER_INFO_1009')
make_head(_module, 'USER_INFO_1010')
make_head(_module, 'USER_INFO_1011')
make_head(_module, 'USER_INFO_1012')
make_head(_module, 'USER_INFO_1013')
make_head(_module, 'USER_INFO_1014')
make_head(_module, 'USER_INFO_1017')
make_head(_module, 'USER_INFO_1018')
make_head(_module, 'USER_INFO_1020')
make_head(_module, 'USER_INFO_1023')
make_head(_module, 'USER_INFO_1024')
make_head(_module, 'USER_INFO_1025')
make_head(_module, 'USER_INFO_1051')
make_head(_module, 'USER_INFO_1052')
make_head(_module, 'USER_INFO_1053')
make_head(_module, 'USER_INFO_11')
make_head(_module, 'USER_INFO_2')
make_head(_module, 'USER_INFO_20')
make_head(_module, 'USER_INFO_21')
make_head(_module, 'USER_INFO_22')
make_head(_module, 'USER_INFO_23')
make_head(_module, 'USER_INFO_24')
make_head(_module, 'USER_INFO_3')
make_head(_module, 'USER_INFO_4')
make_head(_module, 'USER_MODALS_INFO_0')
make_head(_module, 'USER_MODALS_INFO_1')
make_head(_module, 'USER_MODALS_INFO_1001')
make_head(_module, 'USER_MODALS_INFO_1002')
make_head(_module, 'USER_MODALS_INFO_1003')
make_head(_module, 'USER_MODALS_INFO_1004')
make_head(_module, 'USER_MODALS_INFO_1005')
make_head(_module, 'USER_MODALS_INFO_1006')
make_head(_module, 'USER_MODALS_INFO_1007')
make_head(_module, 'USER_MODALS_INFO_2')
make_head(_module, 'USER_MODALS_INFO_3')
make_head(_module, 'USER_OTHER_INFO')
make_head(_module, 'WKSTA_INFO_100')
make_head(_module, 'WKSTA_INFO_101')
make_head(_module, 'WKSTA_INFO_1010')
make_head(_module, 'WKSTA_INFO_1011')
make_head(_module, 'WKSTA_INFO_1012')
make_head(_module, 'WKSTA_INFO_1013')
make_head(_module, 'WKSTA_INFO_1018')
make_head(_module, 'WKSTA_INFO_102')
make_head(_module, 'WKSTA_INFO_1023')
make_head(_module, 'WKSTA_INFO_1027')
make_head(_module, 'WKSTA_INFO_1028')
make_head(_module, 'WKSTA_INFO_1032')
make_head(_module, 'WKSTA_INFO_1033')
make_head(_module, 'WKSTA_INFO_1041')
make_head(_module, 'WKSTA_INFO_1042')
make_head(_module, 'WKSTA_INFO_1043')
make_head(_module, 'WKSTA_INFO_1044')
make_head(_module, 'WKSTA_INFO_1045')
make_head(_module, 'WKSTA_INFO_1046')
make_head(_module, 'WKSTA_INFO_1047')
make_head(_module, 'WKSTA_INFO_1048')
make_head(_module, 'WKSTA_INFO_1049')
make_head(_module, 'WKSTA_INFO_1050')
make_head(_module, 'WKSTA_INFO_1051')
make_head(_module, 'WKSTA_INFO_1052')
make_head(_module, 'WKSTA_INFO_1053')
make_head(_module, 'WKSTA_INFO_1054')
make_head(_module, 'WKSTA_INFO_1055')
make_head(_module, 'WKSTA_INFO_1056')
make_head(_module, 'WKSTA_INFO_1057')
make_head(_module, 'WKSTA_INFO_1058')
make_head(_module, 'WKSTA_INFO_1059')
make_head(_module, 'WKSTA_INFO_1060')
make_head(_module, 'WKSTA_INFO_1061')
make_head(_module, 'WKSTA_INFO_1062')
make_head(_module, 'WKSTA_INFO_302')
make_head(_module, 'WKSTA_INFO_402')
make_head(_module, 'WKSTA_INFO_502')
make_head(_module, 'WKSTA_TRANSPORT_INFO_0')
make_head(_module, 'WKSTA_USER_INFO_0')
make_head(_module, 'WKSTA_USER_INFO_1')
make_head(_module, 'WKSTA_USER_INFO_1101')
make_head(_module, 'WORKERFUNCTION')
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
