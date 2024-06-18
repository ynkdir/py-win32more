from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Data.Xml.MsXml
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.NetManagement
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Registry
class ACCESS_INFO_0(Structure):
    acc0_resource_name: win32more.Windows.Win32.Foundation.PWSTR
class ACCESS_INFO_1(Structure):
    acc1_resource_name: win32more.Windows.Win32.Foundation.PWSTR
    acc1_attr: UInt32
    acc1_count: UInt32
class ACCESS_INFO_1002(Structure):
    acc1002_attr: UInt32
class ACCESS_LIST(Structure):
    acl_ugname: win32more.Windows.Win32.Foundation.PWSTR
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
AF_OP_PRINT: win32more.Windows.Win32.NetworkManagement.NetManagement.AF_OP = 1
AF_OP_COMM: win32more.Windows.Win32.NetworkManagement.NetManagement.AF_OP = 2
AF_OP_SERVER: win32more.Windows.Win32.NetworkManagement.NetManagement.AF_OP = 4
AF_OP_ACCOUNTS: win32more.Windows.Win32.NetworkManagement.NetManagement.AF_OP = 8
class AT_ENUM(Structure):
    JobId: UInt32
    JobTime: UIntPtr
    DaysOfMonth: UInt32
    DaysOfWeek: Byte
    Flags: Byte
    Command: win32more.Windows.Win32.Foundation.PWSTR
class AT_INFO(Structure):
    JobTime: UIntPtr
    DaysOfMonth: UInt32
    DaysOfWeek: Byte
    Flags: Byte
    Command: win32more.Windows.Win32.Foundation.PWSTR
class AUDIT_ENTRY(Structure):
    ae_len: UInt32
    ae_reserved: UInt32
    ae_time: UInt32
    ae_type: UInt32
    ae_data_offset: UInt32
    ae_data_size: UInt32
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
NERR_CannotUpdateAadHostName: UInt32 = 2728
NERR_DuplicateHostName: UInt32 = 2729
NERR_HostNameTooLong: UInt32 = 2730
NERR_TooManyHostNames: UInt32 = 2731
NERR_AccountReuseBlockedByPolicy: UInt32 = 2732
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
ServiceAccountPasswordGUID: Guid = Guid('{262e99c9-6160-4871-acec-4e61736b6f21}')
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
NETLOG_PassThruFilterError_Summary_AdminOverride: UInt32 = 5832
NETLOG_PassThruFilterError_Summary_Blocked: UInt32 = 5833
NETLOG_PassThruFilterError_Request_AdminOverride: UInt32 = 5834
NETLOG_PassThruFilterError_Request_Blocked: UInt32 = 5835
NETLOG_NetlogonRpcBacklogLimitSet: UInt32 = 5836
NETLOG_NetlogonRpcBacklogLimitFailure: UInt32 = 5837
NETLOG_NetlogonRpcSigningClient: UInt32 = 5838
NETLOG_NetlogonRpcSigningTrust: UInt32 = 5839
NETLOG_NetlogonRc4Allowed: UInt32 = 5840
NETLOG_NetlogonRc4Denied: UInt32 = 5841
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
NETCFG_E_ALREADY_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2147180512
NETCFG_E_NOT_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2147180511
NETCFG_E_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2147180510
NETCFG_E_NO_WRITE_LOCK: win32more.Windows.Win32.Foundation.HRESULT = -2147180508
NETCFG_E_NEED_REBOOT: win32more.Windows.Win32.Foundation.HRESULT = -2147180507
NETCFG_E_ACTIVE_RAS_CONNECTIONS: win32more.Windows.Win32.Foundation.HRESULT = -2147180506
NETCFG_E_ADAPTER_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147180505
NETCFG_E_COMPONENT_REMOVED_PENDING_REBOOT: win32more.Windows.Win32.Foundation.HRESULT = -2147180504
NETCFG_E_MAX_FILTER_LIMIT: win32more.Windows.Win32.Foundation.HRESULT = -2147180503
NETCFG_E_VMSWITCH_ACTIVE_OVER_ADAPTER: win32more.Windows.Win32.Foundation.HRESULT = -2147180502
NETCFG_E_DUPLICATE_INSTANCEID: win32more.Windows.Win32.Foundation.HRESULT = -2147180501
NETCFG_S_REBOOT: win32more.Windows.Win32.Foundation.HRESULT = 303136
NETCFG_S_DISABLE_QUERY: win32more.Windows.Win32.Foundation.HRESULT = 303138
NETCFG_S_STILL_REFERENCED: win32more.Windows.Win32.Foundation.HRESULT = 303139
NETCFG_S_CAUSED_SETUP_CHANGE: win32more.Windows.Win32.Foundation.HRESULT = 303140
NETCFG_S_COMMIT_NOW: win32more.Windows.Win32.Foundation.HRESULT = 303141
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
ALIGN_SHIFT: UInt32 = 7
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
def NetUserAdd(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, filter: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_USER_ENUM_FILTER_FLAGS, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserSetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserDel(servername: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserGetGroups(servername: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserSetGroups(servername: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), num_entries: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserGetLocalGroups(servername: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, flags: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserModalsGet(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserModalsSet(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUserChangePassword(domainname: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR, oldpassword: win32more.Windows.Win32.Foundation.PWSTR, newpassword: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupAdd(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupAddUser(servername: win32more.Windows.Win32.Foundation.PWSTR, GroupName: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupSetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupDel(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupDelUser(servername: win32more.Windows.Win32.Foundation.PWSTR, GroupName: win32more.Windows.Win32.Foundation.PWSTR, Username: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupGetUsers(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), ResumeHandle: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGroupSetUsers(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), totalentries: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupAdd(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupAddMember(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR, membersid: win32more.Windows.Win32.Security.PSID) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupSetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupDel(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupDelMember(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR, membersid: win32more.Windows.Win32.Security.PSID) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupGetMembers(servername: win32more.Windows.Win32.Foundation.PWSTR, localgroupname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupSetMembers(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), totalentries: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupAddMembers(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), totalentries: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetLocalGroupDelMembers(servername: win32more.Windows.Win32.Foundation.PWSTR, groupname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), totalentries: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetQueryDisplayInformation(ServerName: win32more.Windows.Win32.Foundation.PWSTR, Level: UInt32, Index: UInt32, EntriesRequested: UInt32, PreferredMaximumLength: UInt32, ReturnedEntryCount: POINTER(UInt32), SortedBuffer: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGetDisplayInformationIndex(ServerName: win32more.Windows.Win32.Foundation.PWSTR, Level: UInt32, Prefix: win32more.Windows.Win32.Foundation.PWSTR, Index: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessAdd(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, BasePath: win32more.Windows.Win32.Foundation.PWSTR, Recursive: UInt32, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, resource: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessSetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, resource: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessDel(servername: win32more.Windows.Win32.Foundation.PWSTR, resource: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAccessGetUserPerms(servername: win32more.Windows.Win32.Foundation.PWSTR, UGname: win32more.Windows.Win32.Foundation.PWSTR, resource: win32more.Windows.Win32.Foundation.PWSTR, Perms: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetValidatePasswordPolicy(ServerName: win32more.Windows.Win32.Foundation.PWSTR, Qualifier: VoidPtr, ValidationType: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_TYPE, InputArg: VoidPtr, OutputArg: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetValidatePasswordPolicyFree(OutputArg: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGetDCName(ServerName: win32more.Windows.Win32.Foundation.PWSTR, DomainName: win32more.Windows.Win32.Foundation.PWSTR, Buffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGetAnyDCName(ServerName: win32more.Windows.Win32.Foundation.PWSTR, DomainName: win32more.Windows.Win32.Foundation.PWSTR, Buffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def I_NetLogonControl2(ServerName: win32more.Windows.Win32.Foundation.PWSTR, FunctionCode: UInt32, QueryLevel: UInt32, Data: POINTER(Byte), Buffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAddServiceAccount(ServerName: win32more.Windows.Win32.Foundation.PWSTR, AccountName: win32more.Windows.Win32.Foundation.PWSTR, Password: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('NETAPI32.dll')
def NetRemoveServiceAccount(ServerName: win32more.Windows.Win32.Foundation.PWSTR, AccountName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('NETAPI32.dll')
def NetEnumerateServiceAccounts(ServerName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32, AccountsCount: POINTER(UInt32), Accounts: POINTER(POINTER(POINTER(UInt16)))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('NETAPI32.dll')
def NetIsServiceAccount(ServerName: win32more.Windows.Win32.Foundation.PWSTR, AccountName: win32more.Windows.Win32.Foundation.PWSTR, IsService: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('NETAPI32.dll')
def NetQueryServiceAccount(ServerName: win32more.Windows.Win32.Foundation.PWSTR, AccountName: win32more.Windows.Win32.Foundation.PWSTR, InfoLevel: UInt32, Buffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('NETAPI32.dll')
def NetAlertRaise(AlertType: win32more.Windows.Win32.Foundation.PWSTR, Buffer: VoidPtr, BufferSize: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAlertRaiseEx(AlertType: win32more.Windows.Win32.Foundation.PWSTR, VariableInfo: VoidPtr, VariableInfoSize: UInt32, ServiceName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetMessageNameAdd(servername: win32more.Windows.Win32.Foundation.PWSTR, msgname: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetMessageNameEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetMessageNameGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, msgname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetMessageNameDel(servername: win32more.Windows.Win32.Foundation.PWSTR, msgname: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetMessageBufferSend(servername: win32more.Windows.Win32.Foundation.PWSTR, msgname: win32more.Windows.Win32.Foundation.PWSTR, fromname: win32more.Windows.Win32.Foundation.PWSTR, buf: POINTER(Byte), buflen: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRemoteTOD(UncServerName: win32more.Windows.Win32.Foundation.PWSTR, BufferPtr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRemoteComputerSupports(UncServerName: win32more.Windows.Win32.Foundation.PWSTR, OptionsWanted: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS, OptionsSupported: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplSetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirAdd(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirDel(servername: win32more.Windows.Win32.Foundation.PWSTR, dirname: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, dirname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirSetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, dirname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirLock(servername: win32more.Windows.Win32.Foundation.PWSTR, dirname: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplExportDirUnlock(servername: win32more.Windows.Win32.Foundation.PWSTR, dirname: win32more.Windows.Win32.Foundation.PWSTR, unlockforce: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirAdd(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirDel(servername: win32more.Windows.Win32.Foundation.PWSTR, dirname: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, dirname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirLock(servername: win32more.Windows.Win32.Foundation.PWSTR, dirname: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetReplImportDirUnlock(servername: win32more.Windows.Win32.Foundation.PWSTR, dirname: win32more.Windows.Win32.Foundation.PWSTR, unlockforce: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), servertype: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE, domain: win32more.Windows.Win32.Foundation.PWSTR, resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerSetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), ParmError: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerDiskEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerComputerNameAdd(ServerName: win32more.Windows.Win32.Foundation.PWSTR, EmulatedDomainName: win32more.Windows.Win32.Foundation.PWSTR, EmulatedServerName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerComputerNameDel(ServerName: win32more.Windows.Win32.Foundation.PWSTR, EmulatedServerName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerTransportAdd(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(Byte)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerTransportAddEx(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(Byte)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerTransportDel(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(Byte)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerTransportEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServiceControl(servername: win32more.Windows.Win32.Foundation.PWSTR, service: win32more.Windows.Win32.Foundation.PWSTR, opcode: UInt32, arg: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServiceEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServiceGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, service: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServiceInstall(servername: win32more.Windows.Win32.Foundation.PWSTR, service: win32more.Windows.Win32.Foundation.PWSTR, argc: UInt32, argv: POINTER(win32more.Windows.Win32.Foundation.PWSTR), bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUseAdd(servername: POINTER(SByte), LevelFlags: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUseDel(UncServerName: win32more.Windows.Win32.Foundation.PWSTR, UseName: win32more.Windows.Win32.Foundation.PWSTR, ForceLevelFlags: win32more.Windows.Win32.NetworkManagement.NetManagement.FORCE_LEVEL_FLAGS) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUseEnum(UncServerName: win32more.Windows.Win32.Foundation.PWSTR, LevelFlags: UInt32, BufPtr: POINTER(POINTER(Byte)), PreferedMaximumSize: UInt32, EntriesRead: POINTER(UInt32), TotalEntries: POINTER(UInt32), ResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUseGetInfo(UncServerName: win32more.Windows.Win32.Foundation.PWSTR, UseName: win32more.Windows.Win32.Foundation.PWSTR, LevelFlags: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaSetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buffer: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaUserGetInfo(reserved: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaUserSetInfo(reserved: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaUserEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaTransportAdd(servername: POINTER(SByte), level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaTransportDel(servername: win32more.Windows.Win32.Foundation.PWSTR, transportname: win32more.Windows.Win32.Foundation.PWSTR, ucond: win32more.Windows.Win32.NetworkManagement.NetManagement.FORCE_LEVEL_FLAGS) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetWkstaTransportEnum(servername: POINTER(SByte), level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetApiBufferAllocate(ByteCount: UInt32, Buffer: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetApiBufferFree(Buffer: VoidPtr) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetApiBufferReallocate(OldBuffer: VoidPtr, NewByteCount: UInt32, NewBuffer: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetApiBufferSize(Buffer: VoidPtr, ByteCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetErrorLogClear(UncServerName: win32more.Windows.Win32.Foundation.PWSTR, BackupFile: win32more.Windows.Win32.Foundation.PWSTR, Reserved: POINTER(Byte)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetErrorLogRead(UncServerName: win32more.Windows.Win32.Foundation.PWSTR, Reserved1: win32more.Windows.Win32.Foundation.PWSTR, ErrorLogHandle: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.HLOG), Offset: UInt32, Reserved2: POINTER(UInt32), Reserved3: UInt32, OffsetFlag: UInt32, BufPtr: POINTER(POINTER(Byte)), PrefMaxSize: UInt32, BytesRead: POINTER(UInt32), TotalAvailable: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetErrorLogWrite(Reserved1: POINTER(Byte), Code: UInt32, Component: win32more.Windows.Win32.Foundation.PWSTR, Buffer: POINTER(Byte), NumBytes: UInt32, MsgBuf: POINTER(Byte), StrCount: UInt32, Reserved2: POINTER(Byte)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetConfigGet(server: win32more.Windows.Win32.Foundation.PWSTR, component: win32more.Windows.Win32.Foundation.PWSTR, parameter: win32more.Windows.Win32.Foundation.PWSTR, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetConfigGetAll(server: win32more.Windows.Win32.Foundation.PWSTR, component: win32more.Windows.Win32.Foundation.PWSTR, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetConfigSet(server: win32more.Windows.Win32.Foundation.PWSTR, reserved1: win32more.Windows.Win32.Foundation.PWSTR, component: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, reserved2: UInt32, buf: POINTER(Byte), reserved3: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAuditClear(server: win32more.Windows.Win32.Foundation.PWSTR, backupfile: win32more.Windows.Win32.Foundation.PWSTR, service: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAuditRead(server: win32more.Windows.Win32.Foundation.PWSTR, service: win32more.Windows.Win32.Foundation.PWSTR, auditloghandle: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.HLOG), offset: UInt32, reserved1: POINTER(UInt32), reserved2: UInt32, offsetflag: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, bytesread: POINTER(UInt32), totalavailable: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAuditWrite(type: UInt32, buf: POINTER(Byte), numbytes: UInt32, service: win32more.Windows.Win32.Foundation.PWSTR, reserved: POINTER(Byte)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetJoinDomain(lpServer: win32more.Windows.Win32.Foundation.PWSTR, lpDomain: win32more.Windows.Win32.Foundation.PWSTR, lpMachineAccountOU: win32more.Windows.Win32.Foundation.PWSTR, lpAccount: win32more.Windows.Win32.Foundation.PWSTR, lpPassword: win32more.Windows.Win32.Foundation.PWSTR, fJoinOptions: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetUnjoinDomain(lpServer: win32more.Windows.Win32.Foundation.PWSTR, lpAccount: win32more.Windows.Win32.Foundation.PWSTR, lpPassword: win32more.Windows.Win32.Foundation.PWSTR, fUnjoinOptions: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRenameMachineInDomain(lpServer: win32more.Windows.Win32.Foundation.PWSTR, lpNewMachineName: win32more.Windows.Win32.Foundation.PWSTR, lpAccount: win32more.Windows.Win32.Foundation.PWSTR, lpPassword: win32more.Windows.Win32.Foundation.PWSTR, fRenameOptions: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetValidateName(lpServer: win32more.Windows.Win32.Foundation.PWSTR, lpName: win32more.Windows.Win32.Foundation.PWSTR, lpAccount: win32more.Windows.Win32.Foundation.PWSTR, lpPassword: win32more.Windows.Win32.Foundation.PWSTR, NameType: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_NAME_TYPE) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGetJoinableOUs(lpServer: win32more.Windows.Win32.Foundation.PWSTR, lpDomain: win32more.Windows.Win32.Foundation.PWSTR, lpAccount: win32more.Windows.Win32.Foundation.PWSTR, lpPassword: win32more.Windows.Win32.Foundation.PWSTR, OUCount: POINTER(UInt32), OUs: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetAddAlternateComputerName(Server: win32more.Windows.Win32.Foundation.PWSTR, AlternateName: win32more.Windows.Win32.Foundation.PWSTR, DomainAccount: win32more.Windows.Win32.Foundation.PWSTR, DomainAccountPassword: win32more.Windows.Win32.Foundation.PWSTR, Reserved: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRemoveAlternateComputerName(Server: win32more.Windows.Win32.Foundation.PWSTR, AlternateName: win32more.Windows.Win32.Foundation.PWSTR, DomainAccount: win32more.Windows.Win32.Foundation.PWSTR, DomainAccountPassword: win32more.Windows.Win32.Foundation.PWSTR, Reserved: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetSetPrimaryComputerName(Server: win32more.Windows.Win32.Foundation.PWSTR, PrimaryName: win32more.Windows.Win32.Foundation.PWSTR, DomainAccount: win32more.Windows.Win32.Foundation.PWSTR, DomainAccountPassword: win32more.Windows.Win32.Foundation.PWSTR, Reserved: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetEnumerateComputerNames(Server: win32more.Windows.Win32.Foundation.PWSTR, NameType: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_COMPUTER_NAME_TYPE, Reserved: UInt32, EntryCount: POINTER(UInt32), ComputerNames: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetProvisionComputerAccount(lpDomain: win32more.Windows.Win32.Foundation.PWSTR, lpMachineName: win32more.Windows.Win32.Foundation.PWSTR, lpMachineAccountOU: win32more.Windows.Win32.Foundation.PWSTR, lpDcName: win32more.Windows.Win32.Foundation.PWSTR, dwOptions: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_PROVISION, pProvisionBinData: POINTER(POINTER(Byte)), pdwProvisionBinDataSize: POINTER(UInt32), pProvisionTextData: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRequestOfflineDomainJoin(pProvisionBinData: POINTER(Byte), cbProvisionBinDataSize: UInt32, dwOptions: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_REQUEST_PROVISION_OPTIONS, lpWindowsPath: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetCreateProvisioningPackage(pProvisioningParams: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_PROVISIONING_PARAMS), ppPackageBinData: POINTER(POINTER(Byte)), pdwPackageBinDataSize: POINTER(UInt32), ppPackageTextData: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetRequestProvisioningPackageInstall(pPackageBinData: POINTER(Byte), dwPackageBinDataSize: UInt32, dwProvisionOptions: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_REQUEST_PROVISION_OPTIONS, lpWindowsPath: win32more.Windows.Win32.Foundation.PWSTR, pvReserved: VoidPtr) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetGetAadJoinInformation(pcszTenantId: win32more.Windows.Win32.Foundation.PWSTR, ppJoinInfo: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.DSREG_JOIN_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NETAPI32.dll')
def NetFreeAadJoinInformation(pJoinInfo: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.DSREG_JOIN_INFO)) -> Void: ...
@winfunctype('NETAPI32.dll')
def NetGetJoinInformation(lpServer: win32more.Windows.Win32.Foundation.PWSTR, lpNameBuffer: POINTER(win32more.Windows.Win32.Foundation.PWSTR), BufferType: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_JOIN_STATUS)) -> UInt32: ...
@winfunctype('mstask.dll')
def GetNetScheduleAccountInformation(pwszServerName: win32more.Windows.Win32.Foundation.PWSTR, ccAccount: UInt32, wszAccount: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mstask.dll')
def SetNetScheduleAccountInformation(pwszServerName: win32more.Windows.Win32.Foundation.PWSTR, pwszAccount: win32more.Windows.Win32.Foundation.PWSTR, pwszPassword: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NETAPI32.dll')
def NetScheduleJobAdd(Servername: win32more.Windows.Win32.Foundation.PWSTR, Buffer: POINTER(Byte), JobId: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetScheduleJobDel(Servername: win32more.Windows.Win32.Foundation.PWSTR, MinJobId: UInt32, MaxJobId: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetScheduleJobEnum(Servername: win32more.Windows.Win32.Foundation.PWSTR, PointerToBuffer: POINTER(POINTER(Byte)), PrefferedMaximumLength: UInt32, EntriesRead: POINTER(UInt32), TotalEntries: POINTER(UInt32), ResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetScheduleJobGetInfo(Servername: win32more.Windows.Win32.Foundation.PWSTR, JobId: UInt32, PointerToBuffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceRegisterExA(lpszCallerName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceDeregisterA(dwTraceID: UInt32) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceDeregisterExA(dwTraceID: UInt32, dwFlags: UInt32) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceGetConsoleA(dwTraceID: UInt32, lphConsole: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@cfunctype('rtutils.dll', variadic=True)
def TracePrintfA(dwTraceID: UInt32, lpszFormat: win32more.Windows.Win32.Foundation.PSTR, *__arglist) -> UInt32: ...
@cfunctype('rtutils.dll', variadic=True)
def TracePrintfExA(dwTraceID: UInt32, dwFlags: UInt32, lpszFormat: win32more.Windows.Win32.Foundation.PSTR, *__arglist) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceVprintfExA(dwTraceID: UInt32, dwFlags: UInt32, lpszFormat: win32more.Windows.Win32.Foundation.PSTR, arglist: POINTER(SByte)) -> UInt32: ...
@winfunctype('rtutils.dll')
def TracePutsExA(dwTraceID: UInt32, dwFlags: UInt32, lpszString: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceDumpExA(dwTraceID: UInt32, dwFlags: UInt32, lpbBytes: POINTER(Byte), dwByteCount: UInt32, dwGroupSize: UInt32, bAddressPrefix: win32more.Windows.Win32.Foundation.BOOL, lpszPrefix: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('rtutils.dll')
def TraceRegisterExW(lpszCallerName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> UInt32: ...
TraceRegisterEx = UnicodeAlias('TraceRegisterExW')
@winfunctype('rtutils.dll')
def TraceDeregisterW(dwTraceID: UInt32) -> UInt32: ...
TraceDeregister = UnicodeAlias('TraceDeregisterW')
@winfunctype('rtutils.dll')
def TraceDeregisterExW(dwTraceID: UInt32, dwFlags: UInt32) -> UInt32: ...
TraceDeregisterEx = UnicodeAlias('TraceDeregisterExW')
@winfunctype('rtutils.dll')
def TraceGetConsoleW(dwTraceID: UInt32, lphConsole: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
TraceGetConsole = UnicodeAlias('TraceGetConsoleW')
@cfunctype('rtutils.dll', variadic=True)
def TracePrintfW(dwTraceID: UInt32, lpszFormat: win32more.Windows.Win32.Foundation.PWSTR, *__arglist) -> UInt32: ...
TracePrintf = UnicodeAlias('TracePrintfW')
@cfunctype('rtutils.dll', variadic=True)
def TracePrintfExW(dwTraceID: UInt32, dwFlags: UInt32, lpszFormat: win32more.Windows.Win32.Foundation.PWSTR, *__arglist) -> UInt32: ...
TracePrintfEx = UnicodeAlias('TracePrintfExW')
@winfunctype('rtutils.dll')
def TraceVprintfExW(dwTraceID: UInt32, dwFlags: UInt32, lpszFormat: win32more.Windows.Win32.Foundation.PWSTR, arglist: POINTER(SByte)) -> UInt32: ...
TraceVprintfEx = UnicodeAlias('TraceVprintfExW')
@winfunctype('rtutils.dll')
def TracePutsExW(dwTraceID: UInt32, dwFlags: UInt32, lpszString: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
TracePutsEx = UnicodeAlias('TracePutsExW')
@winfunctype('rtutils.dll')
def TraceDumpExW(dwTraceID: UInt32, dwFlags: UInt32, lpbBytes: POINTER(Byte), dwByteCount: UInt32, dwGroupSize: UInt32, bAddressPrefix: win32more.Windows.Win32.Foundation.BOOL, lpszPrefix: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
TraceDumpEx = UnicodeAlias('TraceDumpExW')
@winfunctype('rtutils.dll')
def LogErrorA(dwMessageId: UInt32, cNumberOfSubStrings: UInt32, plpwsSubStrings: POINTER(win32more.Windows.Win32.Foundation.PSTR), dwErrorCode: UInt32) -> Void: ...
@winfunctype('rtutils.dll')
def LogEventA(wEventType: UInt32, dwMessageId: UInt32, cNumberOfSubStrings: UInt32, plpwsSubStrings: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> Void: ...
@winfunctype('rtutils.dll')
def LogErrorW(dwMessageId: UInt32, cNumberOfSubStrings: UInt32, plpwsSubStrings: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwErrorCode: UInt32) -> Void: ...
LogError = UnicodeAlias('LogErrorW')
@winfunctype('rtutils.dll')
def LogEventW(wEventType: UInt32, dwMessageId: UInt32, cNumberOfSubStrings: UInt32, plpwsSubStrings: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> Void: ...
LogEvent = UnicodeAlias('LogEventW')
@winfunctype('rtutils.dll')
def RouterLogRegisterA(lpszSource: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('rtutils.dll')
def RouterLogDeregisterA(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventA(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Windows.Win32.Foundation.PSTR), dwErrorCode: UInt32) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventDataA(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Windows.Win32.Foundation.PSTR), dwDataBytes: UInt32, lpDataBytes: POINTER(Byte)) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventStringA(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Windows.Win32.Foundation.PSTR), dwErrorCode: UInt32, dwErrorIndex: UInt32) -> Void: ...
@cfunctype('rtutils.dll', variadic=True)
def RouterLogEventExA(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE, dwEventType: UInt32, dwErrorCode: UInt32, dwMessageId: UInt32, ptszFormat: win32more.Windows.Win32.Foundation.PSTR, *__arglist) -> Void: ...
@winfunctype('rtutils.dll')
def RouterLogEventValistExA(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE, dwEventType: UInt32, dwErrorCode: UInt32, dwMessageId: UInt32, ptszFormat: win32more.Windows.Win32.Foundation.PSTR, arglist: POINTER(SByte)) -> Void: ...
@winfunctype('rtutils.dll')
def RouterGetErrorStringA(dwErrorCode: UInt32, lplpszErrorString: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@winfunctype('rtutils.dll')
def RouterLogRegisterW(lpszSource: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
RouterLogRegister = UnicodeAlias('RouterLogRegisterW')
@winfunctype('rtutils.dll')
def RouterLogDeregisterW(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
RouterLogDeregister = UnicodeAlias('RouterLogDeregisterW')
@winfunctype('rtutils.dll')
def RouterLogEventW(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwErrorCode: UInt32) -> Void: ...
RouterLogEvent = UnicodeAlias('RouterLogEventW')
@winfunctype('rtutils.dll')
def RouterLogEventDataW(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwDataBytes: UInt32, lpDataBytes: POINTER(Byte)) -> Void: ...
RouterLogEventData = UnicodeAlias('RouterLogEventDataW')
@winfunctype('rtutils.dll')
def RouterLogEventStringW(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE, dwEventType: UInt32, dwMessageId: UInt32, dwSubStringCount: UInt32, plpszSubStringArray: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwErrorCode: UInt32, dwErrorIndex: UInt32) -> Void: ...
RouterLogEventString = UnicodeAlias('RouterLogEventStringW')
@cfunctype('rtutils.dll', variadic=True)
def RouterLogEventExW(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE, dwEventType: UInt32, dwErrorCode: UInt32, dwMessageId: UInt32, ptszFormat: win32more.Windows.Win32.Foundation.PWSTR, *__arglist) -> Void: ...
RouterLogEventEx = UnicodeAlias('RouterLogEventExW')
@winfunctype('rtutils.dll')
def RouterLogEventValistExW(hLogHandle: win32more.Windows.Win32.Foundation.HANDLE, dwEventType: UInt32, dwErrorCode: UInt32, dwMessageId: UInt32, ptszFormat: win32more.Windows.Win32.Foundation.PWSTR, arglist: POINTER(SByte)) -> Void: ...
RouterLogEventValistEx = UnicodeAlias('RouterLogEventValistExW')
@winfunctype('rtutils.dll')
def RouterGetErrorStringW(dwErrorCode: UInt32, lplpwszErrorString: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
RouterGetErrorString = UnicodeAlias('RouterGetErrorStringW')
@winfunctype('rtutils.dll')
def RouterAssert(pszFailedAssertion: win32more.Windows.Win32.Foundation.PSTR, pszFileName: win32more.Windows.Win32.Foundation.PSTR, dwLineNumber: UInt32, pszMessage: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('rtutils.dll')
def MprSetupProtocolEnum(dwTransportId: UInt32, lplpBuffer: POINTER(POINTER(Byte)), lpdwEntriesRead: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rtutils.dll')
def MprSetupProtocolFree(lpBuffer: VoidPtr) -> UInt32: ...
BIND_FLAGS1 = Int32
NCN_ADD: win32more.Windows.Win32.NetworkManagement.NetManagement.BIND_FLAGS1 = 1
NCN_REMOVE: win32more.Windows.Win32.NetworkManagement.NetManagement.BIND_FLAGS1 = 2
NCN_UPDATE: win32more.Windows.Win32.NetworkManagement.NetManagement.BIND_FLAGS1 = 4
NCN_ENABLE: win32more.Windows.Win32.NetworkManagement.NetManagement.BIND_FLAGS1 = 16
NCN_DISABLE: win32more.Windows.Win32.NetworkManagement.NetManagement.BIND_FLAGS1 = 32
NCN_BINDING_PATH: win32more.Windows.Win32.NetworkManagement.NetManagement.BIND_FLAGS1 = 256
NCN_PROPERTYCHANGE: win32more.Windows.Win32.NetworkManagement.NetManagement.BIND_FLAGS1 = 512
NCN_NET: win32more.Windows.Win32.NetworkManagement.NetManagement.BIND_FLAGS1 = 65536
NCN_NETTRANS: win32more.Windows.Win32.NetworkManagement.NetManagement.BIND_FLAGS1 = 131072
NCN_NETCLIENT: win32more.Windows.Win32.NetworkManagement.NetManagement.BIND_FLAGS1 = 262144
NCN_NETSERVICE: win32more.Windows.Win32.NetworkManagement.NetManagement.BIND_FLAGS1 = 524288
COMPONENT_CHARACTERISTICS = Int32
NCF_VIRTUAL: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 1
NCF_SOFTWARE_ENUMERATED: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 2
NCF_PHYSICAL: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 4
NCF_HIDDEN: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 8
NCF_NO_SERVICE: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 16
NCF_NOT_USER_REMOVABLE: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 32
NCF_MULTIPORT_INSTANCED_ADAPTER: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 64
NCF_HAS_UI: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 128
NCF_SINGLE_INSTANCE: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 256
NCF_FILTER: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 1024
NCF_DONTEXPOSELOWER: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 4096
NCF_HIDE_BINDING: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 8192
NCF_NDIS_PROTOCOL: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 16384
NCF_FIXED_BINDING: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 131072
NCF_LW_FILTER: win32more.Windows.Win32.NetworkManagement.NetManagement.COMPONENT_CHARACTERISTICS = 262144
class CONFIG_INFO_0(Structure):
    cfgi0_key: win32more.Windows.Win32.Foundation.PWSTR
    cfgi0_data: win32more.Windows.Win32.Foundation.PWSTR
DEFAULT_PAGES = Int32
DPP_ADVANCED: win32more.Windows.Win32.NetworkManagement.NetManagement.DEFAULT_PAGES = 1
class DSREG_JOIN_INFO(Structure):
    joinType: win32more.Windows.Win32.NetworkManagement.NetManagement.DSREG_JOIN_TYPE
    pJoinCertificate: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
    pszDeviceId: win32more.Windows.Win32.Foundation.PWSTR
    pszIdpDomain: win32more.Windows.Win32.Foundation.PWSTR
    pszTenantId: win32more.Windows.Win32.Foundation.PWSTR
    pszJoinUserEmail: win32more.Windows.Win32.Foundation.PWSTR
    pszTenantDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    pszMdmEnrollmentUrl: win32more.Windows.Win32.Foundation.PWSTR
    pszMdmTermsOfUseUrl: win32more.Windows.Win32.Foundation.PWSTR
    pszMdmComplianceUrl: win32more.Windows.Win32.Foundation.PWSTR
    pszUserSettingSyncUrl: win32more.Windows.Win32.Foundation.PWSTR
    pUserInfo: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.DSREG_USER_INFO)
DSREG_JOIN_TYPE = Int32
DSREG_UNKNOWN_JOIN: win32more.Windows.Win32.NetworkManagement.NetManagement.DSREG_JOIN_TYPE = 0
DSREG_DEVICE_JOIN: win32more.Windows.Win32.NetworkManagement.NetManagement.DSREG_JOIN_TYPE = 1
DSREG_WORKPLACE_JOIN: win32more.Windows.Win32.NetworkManagement.NetManagement.DSREG_JOIN_TYPE = 2
class DSREG_USER_INFO(Structure):
    pszUserEmail: win32more.Windows.Win32.Foundation.PWSTR
    pszUserKeyId: win32more.Windows.Win32.Foundation.PWSTR
    pszUserKeyName: win32more.Windows.Win32.Foundation.PWSTR
ENUM_BINDING_PATHS_FLAGS = Int32
EBP_ABOVE: win32more.Windows.Win32.NetworkManagement.NetManagement.ENUM_BINDING_PATHS_FLAGS = 1
EBP_BELOW: win32more.Windows.Win32.NetworkManagement.NetManagement.ENUM_BINDING_PATHS_FLAGS = 2
class ERRLOG_OTHER_INFO(Structure):
    alrter_errcode: UInt32
    alrter_offset: UInt32
class ERROR_LOG(Structure):
    el_len: UInt32
    el_reserved: UInt32
    el_time: UInt32
    el_error: UInt32
    el_name: win32more.Windows.Win32.Foundation.PWSTR
    el_text: win32more.Windows.Win32.Foundation.PWSTR
    el_data: POINTER(Byte)
    el_data_size: UInt32
    el_nstrings: UInt32
class FLAT_STRING(Structure):
    MaximumLength: Int16
    Length: Int16
    Buffer: win32more.Windows.Win32.Foundation.CHAR * 1
FORCE_LEVEL_FLAGS = UInt32
USE_NOFORCE: win32more.Windows.Win32.NetworkManagement.NetManagement.FORCE_LEVEL_FLAGS = 0
USE_FORCE: win32more.Windows.Win32.NetworkManagement.NetManagement.FORCE_LEVEL_FLAGS = 1
USE_LOTS_OF_FORCE: win32more.Windows.Win32.NetworkManagement.NetManagement.FORCE_LEVEL_FLAGS = 2
class GROUP_INFO_0(Structure):
    grpi0_name: win32more.Windows.Win32.Foundation.PWSTR
class GROUP_INFO_1(Structure):
    grpi1_name: win32more.Windows.Win32.Foundation.PWSTR
    grpi1_comment: win32more.Windows.Win32.Foundation.PWSTR
class GROUP_INFO_1002(Structure):
    grpi1002_comment: win32more.Windows.Win32.Foundation.PWSTR
class GROUP_INFO_1005(Structure):
    grpi1005_attributes: UInt32
class GROUP_INFO_2(Structure):
    grpi2_name: win32more.Windows.Win32.Foundation.PWSTR
    grpi2_comment: win32more.Windows.Win32.Foundation.PWSTR
    grpi2_group_id: UInt32
    grpi2_attributes: UInt32
class GROUP_INFO_3(Structure):
    grpi3_name: win32more.Windows.Win32.Foundation.PWSTR
    grpi3_comment: win32more.Windows.Win32.Foundation.PWSTR
    grpi3_group_sid: win32more.Windows.Win32.Security.PSID
    grpi3_attributes: UInt32
class GROUP_USERS_INFO_0(Structure):
    grui0_name: win32more.Windows.Win32.Foundation.PWSTR
class GROUP_USERS_INFO_1(Structure):
    grui1_name: win32more.Windows.Win32.Foundation.PWSTR
    grui1_attributes: UInt32
class HARDWARE_ADDRESS(Structure):
    Address: Byte * 6
class HLOG(Structure):
    time: UInt32
    last_flags: UInt32
    offset: UInt32
    rec_offset: UInt32
class IEnumNetCfgBindingInterface(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae90-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingInterface), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.IEnumNetCfgBindingInterface)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumNetCfgBindingPath(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae91-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingPath), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.IEnumNetCfgBindingPath)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumNetCfgComponent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae92-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.IEnumNetCfgComponent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfg(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae93-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def Initialize(self, pvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uninitialize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Apply(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumComponents(self, pguidClass: POINTER(Guid), ppenumComponent: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.IEnumNetCfgComponent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindComponent(self, pszwInfId: win32more.Windows.Win32.Foundation.PWSTR, pComponent: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def QueryNetCfgClass(self, pguidClass: POINTER(Guid), riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgBindingInterface(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae94-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def GetName(self, ppszwInterfaceName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUpperComponent(self, ppnccItem: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLowerComponent(self, ppnccItem: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgBindingPath(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae96-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def IsSamePathAs(self, pPath: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingPath) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsSubPathOf(self, pPath: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingPath) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsEnabled(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Enable(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPathToken(self, ppszwPathToken: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOwner(self, ppComponent: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDepth(self, pcInterfaces: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumBindingInterfaces(self, ppenumInterface: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.IEnumNetCfgBindingInterface)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgClass(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae97-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def FindComponent(self, pszwInfId: win32more.Windows.Win32.Foundation.PWSTR, ppnccItem: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumComponents(self, ppenumComponent: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.IEnumNetCfgComponent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgClassSetup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae9d-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def SelectAndInstall(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, pOboToken: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.OBO_TOKEN), ppnccItem: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Install(self, pszwInfId: win32more.Windows.Win32.Foundation.PWSTR, pOboToken: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.OBO_TOKEN), dwSetupFlags: UInt32, dwUpgradeFromBuildNo: UInt32, pszwAnswerFile: win32more.Windows.Win32.Foundation.PWSTR, pszwAnswerSections: win32more.Windows.Win32.Foundation.PWSTR, ppnccItem: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeInstall(self, pComponent: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent, pOboToken: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.OBO_TOKEN), pmszwRefs: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgClassSetup2(ComPtr):
    extends: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgClassSetup
    _iid_ = Guid('{c0e8aea0-306e-11d1-aacf-00805fc1270e}')
    @commethod(6)
    def UpdateNonEnumeratedComponent(self, pIComp: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent, dwSetupFlags: UInt32, dwUpgradeFromBuildNo: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgComponent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae99-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def GetDisplayName(self, ppszwDisplayName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDisplayName(self, pszwDisplayName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHelpText(self, pszwHelpText: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetId(self, ppszwId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCharacteristics(self, pdwCharacteristics: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetInstanceGuid(self, pGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPnpDevNodeId(self, ppszwDevNodeId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetClassGuid(self, pGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBindName(self, ppszwBindName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDeviceStatus(self, pulStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OpenParamKey(self, phkey: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RaisePropertyUi(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, punkContext: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgComponentBindings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae9e-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def BindTo(self, pnccItem: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnbindFrom(self, pnccItem: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SupportsBindingInterface(self, dwFlags: UInt32, pszwInterfaceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsBoundTo(self, pnccItem: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsBindableTo(self, pnccItem: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumBindingPaths(self, dwFlags: UInt32, ppIEnum: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.IEnumNetCfgBindingPath)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MoveBefore(self, pncbItemSrc: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingPath, pncbItemDest: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingPath) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def MoveAfter(self, pncbItemSrc: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingPath, pncbItemDest: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingPath) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgComponentControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{932238df-bea1-11d0-9298-00c04fc99dcf}')
    @commethod(3)
    def Initialize(self, pIComp: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent, pINetCfg: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfg, fInstalling: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ApplyRegistryChanges(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ApplyPnpChanges(self, pICallback: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgPnpReconfigCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CancelChanges(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgComponentNotifyBinding(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{932238e1-bea1-11d0-9298-00c04fc99dcf}')
    @commethod(3)
    def QueryBindingPath(self, dwChangeFlag: UInt32, pIPath: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingPath) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyBindingPath(self, dwChangeFlag: UInt32, pIPath: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingPath) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgComponentNotifyGlobal(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{932238e2-bea1-11d0-9298-00c04fc99dcf}')
    @commethod(3)
    def GetSupportedNotifications(self, dwNotifications: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SysQueryBindingPath(self, dwChangeFlag: UInt32, pIPath: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingPath) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SysNotifyBindingPath(self, dwChangeFlag: UInt32, pIPath: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgBindingPath) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SysNotifyComponent(self, dwChangeFlag: UInt32, pIComp: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgComponentPropertyUi(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{932238e0-bea1-11d0-9298-00c04fc99dcf}')
    @commethod(3)
    def QueryPropertyUi(self, pUnkReserved: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetContext(self, pUnkReserved: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MergePropPages(self, pdwDefPages: POINTER(UInt32), pahpspPrivate: POINTER(POINTER(Byte)), pcPages: POINTER(UInt32), hwndParent: win32more.Windows.Win32.Foundation.HWND, pszStartPage: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ValidateProperties(self, hwndSheet: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ApplyProperties(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CancelProperties(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgComponentSetup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{932238e3-bea1-11d0-9298-00c04fc99dcf}')
    @commethod(3)
    def Install(self, dwSetupFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Upgrade(self, dwSetupFlags: UInt32, dwUpgradeFomBuildNo: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReadAnswerFile(self, pszwAnswerFile: win32more.Windows.Win32.Foundation.PWSTR, pszwAnswerSections: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Removing(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgComponentSysPrep(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae9a-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def SaveAdapterParameters(self, pncsp: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgSysPrep, pszwAnswerSections: win32more.Windows.Win32.Foundation.PWSTR, pAdapterInstanceGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RestoreAdapterParameters(self, pszwAnswerFile: win32more.Windows.Win32.Foundation.PWSTR, pszwAnswerSection: win32more.Windows.Win32.Foundation.PWSTR, pAdapterInstanceGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgComponentUpperEdge(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{932238e4-bea1-11d0-9298-00c04fc99dcf}')
    @commethod(3)
    def GetInterfaceIdsForAdapter(self, pAdapter: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent, pdwNumInterfaces: POINTER(UInt32), ppguidInterfaceIds: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddInterfacesToAdapter(self, pAdapter: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent, dwNumInterfaces: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveInterfacesFromAdapter(self, pAdapter: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent, dwNumInterfaces: UInt32, pguidInterfaceIds: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgLock(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae9f-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def AcquireWriteLock(self, cmsTimeout: UInt32, pszwClientDescription: win32more.Windows.Win32.Foundation.PWSTR, ppszwClientDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseWriteLock(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsWriteLocked(self, ppszwClientDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgPnpReconfigCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8d84bd35-e227-11d2-b700-00a0c98a6a85}')
    @commethod(3)
    def SendPnpReconfig(self, Layer: win32more.Windows.Win32.NetworkManagement.NetManagement.NCPNP_RECONFIG_LAYER, pszwUpper: win32more.Windows.Win32.Foundation.PWSTR, pszwLower: win32more.Windows.Win32.Foundation.PWSTR, pvData: VoidPtr, dwSizeOfData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetCfgSysPrep(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0e8ae98-306e-11d1-aacf-00805fc1270e}')
    @commethod(3)
    def HrSetupSetFirstDword(self, pwszSection: win32more.Windows.Win32.Foundation.PWSTR, pwszKey: win32more.Windows.Win32.Foundation.PWSTR, dwValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HrSetupSetFirstString(self, pwszSection: win32more.Windows.Win32.Foundation.PWSTR, pwszKey: win32more.Windows.Win32.Foundation.PWSTR, pwszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HrSetupSetFirstStringAsBool(self, pwszSection: win32more.Windows.Win32.Foundation.PWSTR, pwszKey: win32more.Windows.Win32.Foundation.PWSTR, fValue: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def HrSetupSetFirstMultiSzField(self, pwszSection: win32more.Windows.Win32.Foundation.PWSTR, pwszKey: win32more.Windows.Win32.Foundation.PWSTR, pmszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetLanConnectionUiInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c08956a6-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(3)
    def GetDeviceGuid(self, pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetRasConnectionIpUiInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{faedcf58-31fe-11d1-aad2-00805fc1270e}')
    @commethod(3)
    def GetUiInfo(self, pInfo: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_IPUI)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProvisioningDomain(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c96fbd50-24dd-11d8-89fb-00904b2ea9c6}')
    @commethod(3)
    def Add(self, pszwPathToFolder: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Query(self, pszwDomain: win32more.Windows.Win32.Foundation.PWSTR, pszwLanguage: win32more.Windows.Win32.Foundation.PWSTR, pszwXPathQuery: win32more.Windows.Win32.Foundation.PWSTR, Nodes: POINTER(win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMNodeList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProvisioningProfileWireless(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c96fbd51-24dd-11d8-89fb-00904b2ea9c6}')
    @commethod(3)
    def CreateProfile(self, bstrXMLWirelessConfigProfile: win32more.Windows.Win32.Foundation.BSTR, bstrXMLConnectionConfigProfile: win32more.Windows.Win32.Foundation.BSTR, pAdapterInstanceGuid: POINTER(Guid), pulStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class LOCALGROUP_INFO_0(Structure):
    lgrpi0_name: win32more.Windows.Win32.Foundation.PWSTR
class LOCALGROUP_INFO_1(Structure):
    lgrpi1_name: win32more.Windows.Win32.Foundation.PWSTR
    lgrpi1_comment: win32more.Windows.Win32.Foundation.PWSTR
class LOCALGROUP_INFO_1002(Structure):
    lgrpi1002_comment: win32more.Windows.Win32.Foundation.PWSTR
class LOCALGROUP_MEMBERS_INFO_0(Structure):
    lgrmi0_sid: win32more.Windows.Win32.Security.PSID
class LOCALGROUP_MEMBERS_INFO_1(Structure):
    lgrmi1_sid: win32more.Windows.Win32.Security.PSID
    lgrmi1_sidusage: win32more.Windows.Win32.Security.SID_NAME_USE
    lgrmi1_name: win32more.Windows.Win32.Foundation.PWSTR
class LOCALGROUP_MEMBERS_INFO_2(Structure):
    lgrmi2_sid: win32more.Windows.Win32.Security.PSID
    lgrmi2_sidusage: win32more.Windows.Win32.Security.SID_NAME_USE
    lgrmi2_domainandname: win32more.Windows.Win32.Foundation.PWSTR
class LOCALGROUP_MEMBERS_INFO_3(Structure):
    lgrmi3_domainandname: win32more.Windows.Win32.Foundation.PWSTR
class LOCALGROUP_USERS_INFO_0(Structure):
    lgrui0_name: win32more.Windows.Win32.Foundation.PWSTR
class MPR_PROTOCOL_0(Structure):
    dwProtocolId: UInt32
    wszProtocol: Char * 41
    wszDLLName: Char * 49
class MSA_INFO_0(Structure):
    State: win32more.Windows.Win32.NetworkManagement.NetManagement.MSA_INFO_STATE
MSA_INFO_LEVEL = Int32
MsaInfoLevel0: win32more.Windows.Win32.NetworkManagement.NetManagement.MSA_INFO_LEVEL = 0
MsaInfoLevelMax: win32more.Windows.Win32.NetworkManagement.NetManagement.MSA_INFO_LEVEL = 1
MSA_INFO_STATE = Int32
MsaInfoNotExist: win32more.Windows.Win32.NetworkManagement.NetManagement.MSA_INFO_STATE = 1
MsaInfoNotService: win32more.Windows.Win32.NetworkManagement.NetManagement.MSA_INFO_STATE = 2
MsaInfoCannotInstall: win32more.Windows.Win32.NetworkManagement.NetManagement.MSA_INFO_STATE = 3
MsaInfoCanInstall: win32more.Windows.Win32.NetworkManagement.NetManagement.MSA_INFO_STATE = 4
MsaInfoInstalled: win32more.Windows.Win32.NetworkManagement.NetManagement.MSA_INFO_STATE = 5
class MSG_INFO_0(Structure):
    msgi0_name: win32more.Windows.Win32.Foundation.PWSTR
class MSG_INFO_1(Structure):
    msgi1_name: win32more.Windows.Win32.Foundation.PWSTR
    msgi1_forward_flag: UInt32
    msgi1_forward: win32more.Windows.Win32.Foundation.PWSTR
NCPNP_RECONFIG_LAYER = Int32
NCRL_NDIS: win32more.Windows.Win32.NetworkManagement.NetManagement.NCPNP_RECONFIG_LAYER = 1
NCRL_TDI: win32more.Windows.Win32.NetworkManagement.NetManagement.NCPNP_RECONFIG_LAYER = 2
NCRP_FLAGS = Int32
NCRP_QUERY_PROPERTY_UI: win32more.Windows.Win32.NetworkManagement.NetManagement.NCRP_FLAGS = 1
NCRP_SHOW_PROPERTY_UI: win32more.Windows.Win32.NetworkManagement.NetManagement.NCRP_FLAGS = 2
class NETLOGON_INFO_1(Structure):
    netlog1_flags: UInt32
    netlog1_pdc_connection_status: UInt32
class NETLOGON_INFO_2(Structure):
    netlog2_flags: UInt32
    netlog2_pdc_connection_status: UInt32
    netlog2_trusted_dc_name: win32more.Windows.Win32.Foundation.PWSTR
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
    netlog4_trusted_dc_name: win32more.Windows.Win32.Foundation.PWSTR
    netlog4_trusted_domain_name: win32more.Windows.Win32.Foundation.PWSTR
NETSETUP_JOIN_STATUS = Int32
NetSetupUnknownStatus: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_JOIN_STATUS = 0
NetSetupUnjoined: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_JOIN_STATUS = 1
NetSetupWorkgroupName: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_JOIN_STATUS = 2
NetSetupDomainName: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_JOIN_STATUS = 3
NETSETUP_NAME_TYPE = Int32
NetSetupUnknown: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_NAME_TYPE = 0
NetSetupMachine: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_NAME_TYPE = 1
NetSetupWorkgroup: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_NAME_TYPE = 2
NetSetupDomain: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_NAME_TYPE = 3
NetSetupNonExistentDomain: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_NAME_TYPE = 4
NetSetupDnsMachine: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_NAME_TYPE = 5
NETSETUP_PROVISION = UInt32
NETSETUP_PROVISION_DOWNLEVEL_PRIV_SUPPORT: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_PROVISION = 1
NETSETUP_PROVISION_REUSE_ACCOUNT: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_PROVISION = 2
NETSETUP_PROVISION_USE_DEFAULT_PASSWORD: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_PROVISION = 4
NETSETUP_PROVISION_SKIP_ACCOUNT_SEARCH: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_PROVISION = 8
NETSETUP_PROVISION_ROOT_CA_CERTS: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_PROVISION = 16
class NETSETUP_PROVISIONING_PARAMS(Structure):
    dwVersion: UInt32
    lpDomain: win32more.Windows.Win32.Foundation.PWSTR
    lpHostName: win32more.Windows.Win32.Foundation.PWSTR
    lpMachineAccountOU: win32more.Windows.Win32.Foundation.PWSTR
    lpDcName: win32more.Windows.Win32.Foundation.PWSTR
    dwProvisionOptions: win32more.Windows.Win32.NetworkManagement.NetManagement.NETSETUP_PROVISION
    aCertTemplateNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    cCertTemplateNames: UInt32
    aMachinePolicyNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    cMachinePolicyNames: UInt32
    aMachinePolicyPaths: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    cMachinePolicyPaths: UInt32
    lpNetbiosName: win32more.Windows.Win32.Foundation.PWSTR
    lpSiteName: win32more.Windows.Win32.Foundation.PWSTR
    lpPrimaryDNSDomain: win32more.Windows.Win32.Foundation.PWSTR
NETWORK_INSTALL_TIME = Int32
NSF_PRIMARYINSTALL: win32more.Windows.Win32.NetworkManagement.NetManagement.NETWORK_INSTALL_TIME = 1
NSF_POSTSYSINSTALL: win32more.Windows.Win32.NetworkManagement.NetManagement.NETWORK_INSTALL_TIME = 2
class NETWORK_NAME(Structure):
    Name: win32more.Windows.Win32.NetworkManagement.NetManagement.FLAT_STRING
NETWORK_UPGRADE_TYPE = Int32
NSF_WIN16_UPGRADE: win32more.Windows.Win32.NetworkManagement.NetManagement.NETWORK_UPGRADE_TYPE = 16
NSF_WIN95_UPGRADE: win32more.Windows.Win32.NetworkManagement.NetManagement.NETWORK_UPGRADE_TYPE = 32
NSF_WINNT_WKS_UPGRADE: win32more.Windows.Win32.NetworkManagement.NetManagement.NETWORK_UPGRADE_TYPE = 64
NSF_WINNT_SVR_UPGRADE: win32more.Windows.Win32.NetworkManagement.NetManagement.NETWORK_UPGRADE_TYPE = 128
NSF_WINNT_SBS_UPGRADE: win32more.Windows.Win32.NetworkManagement.NetManagement.NETWORK_UPGRADE_TYPE = 256
NSF_COMPONENT_UPDATE: win32more.Windows.Win32.NetworkManagement.NetManagement.NETWORK_UPGRADE_TYPE = 512
NET_COMPUTER_NAME_TYPE = Int32
NetPrimaryComputerName: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_COMPUTER_NAME_TYPE = 0
NetAlternateComputerNames: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_COMPUTER_NAME_TYPE = 1
NetAllComputerNames: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_COMPUTER_NAME_TYPE = 2
NetComputerNameTypeMax: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_COMPUTER_NAME_TYPE = 3
class NET_DISPLAY_GROUP(Structure):
    grpi3_name: win32more.Windows.Win32.Foundation.PWSTR
    grpi3_comment: win32more.Windows.Win32.Foundation.PWSTR
    grpi3_group_id: UInt32
    grpi3_attributes: UInt32
    grpi3_next_index: UInt32
class NET_DISPLAY_MACHINE(Structure):
    usri2_name: win32more.Windows.Win32.Foundation.PWSTR
    usri2_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri2_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri2_user_id: UInt32
    usri2_next_index: UInt32
class NET_DISPLAY_USER(Structure):
    usri1_name: win32more.Windows.Win32.Foundation.PWSTR
    usri1_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri1_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri1_full_name: win32more.Windows.Win32.Foundation.PWSTR
    usri1_user_id: UInt32
    usri1_next_index: UInt32
NET_JOIN_DOMAIN_JOIN_OPTIONS = UInt32
NETSETUP_JOIN_DOMAIN: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 1
NETSETUP_ACCT_CREATE: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 2
NETSETUP_WIN9X_UPGRADE: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 16
NETSETUP_DOMAIN_JOIN_IF_JOINED: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 32
NETSETUP_JOIN_UNSECURE: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 64
NETSETUP_MACHINE_PWD_PASSED: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 128
NETSETUP_DEFER_SPN_SET: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 256
NETSETUP_JOIN_DC_ACCOUNT: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 512
NETSETUP_JOIN_WITH_NEW_NAME: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 1024
NETSETUP_JOIN_READONLY: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 2048
NETSETUP_AMBIGUOUS_DC: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 4096
NETSETUP_NO_NETLOGON_CACHE: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 8192
NETSETUP_DONT_CONTROL_SERVICES: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 16384
NETSETUP_SET_MACHINE_NAME: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 32768
NETSETUP_FORCE_SPN_SET: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 65536
NETSETUP_NO_ACCT_REUSE: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 131072
NETSETUP_IGNORE_UNSUPPORTED_FLAGS: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_JOIN_DOMAIN_JOIN_OPTIONS = 268435456
NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = UInt32
SUPPORTS_REMOTE_ADMIN_PROTOCOL: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = 2
SUPPORTS_RPC: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = 4
SUPPORTS_SAM_PROTOCOL: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = 8
SUPPORTS_UNICODE: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = 16
SUPPORTS_LOCAL: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_REMOTE_COMPUTER_SUPPORTS_OPTIONS = 32
NET_REQUEST_PROVISION_OPTIONS = UInt32
NETSETUP_PROVISION_ONLINE_CALLER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_REQUEST_PROVISION_OPTIONS = 1073741824
NET_SERVER_TYPE = UInt32
SV_TYPE_WORKSTATION: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 1
SV_TYPE_SERVER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 2
SV_TYPE_SQLSERVER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 4
SV_TYPE_DOMAIN_CTRL: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 8
SV_TYPE_DOMAIN_BAKCTRL: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 16
SV_TYPE_TIME_SOURCE: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 32
SV_TYPE_AFP: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 64
SV_TYPE_NOVELL: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 128
SV_TYPE_DOMAIN_MEMBER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 256
SV_TYPE_PRINTQ_SERVER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 512
SV_TYPE_DIALIN_SERVER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 1024
SV_TYPE_XENIX_SERVER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 2048
SV_TYPE_SERVER_UNIX: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 2048
SV_TYPE_NT: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 4096
SV_TYPE_WFW: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 8192
SV_TYPE_SERVER_MFPN: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 16384
SV_TYPE_SERVER_NT: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 32768
SV_TYPE_POTENTIAL_BROWSER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 65536
SV_TYPE_BACKUP_BROWSER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 131072
SV_TYPE_MASTER_BROWSER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 262144
SV_TYPE_DOMAIN_MASTER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 524288
SV_TYPE_SERVER_OSF: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 1048576
SV_TYPE_SERVER_VMS: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 2097152
SV_TYPE_WINDOWS: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 4194304
SV_TYPE_DFS: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 8388608
SV_TYPE_CLUSTER_NT: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 16777216
SV_TYPE_TERMINALSERVER: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 33554432
SV_TYPE_CLUSTER_VS_NT: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 67108864
SV_TYPE_DCE: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 268435456
SV_TYPE_ALTERNATE_XPORT: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 536870912
SV_TYPE_LOCAL_LIST_ONLY: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 1073741824
SV_TYPE_DOMAIN_ENUM: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 2147483648
SV_TYPE_ALL: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE = 4294967295
NET_USER_ENUM_FILTER_FLAGS = UInt32
FILTER_TEMP_DUPLICATE_ACCOUNT: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_USER_ENUM_FILTER_FLAGS = 1
FILTER_NORMAL_ACCOUNT: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_USER_ENUM_FILTER_FLAGS = 2
FILTER_INTERDOMAIN_TRUST_ACCOUNT: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_USER_ENUM_FILTER_FLAGS = 8
FILTER_WORKSTATION_TRUST_ACCOUNT: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_USER_ENUM_FILTER_FLAGS = 16
FILTER_SERVER_TRUST_ACCOUNT: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_USER_ENUM_FILTER_FLAGS = 32
class NET_VALIDATE_AUTHENTICATION_INPUT_ARG(Structure):
    InputPersistedFields: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS
    PasswordMatched: win32more.Windows.Win32.Foundation.BOOLEAN
class NET_VALIDATE_OUTPUT_ARG(Structure):
    ChangedPersistedFields: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS
    ValidationStatus: UInt32
class NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG(Structure):
    InputPersistedFields: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS
    ClearPassword: win32more.Windows.Win32.Foundation.PWSTR
    UserAccountName: win32more.Windows.Win32.Foundation.PWSTR
    HashedPassword: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_HASH
    PasswordMatch: win32more.Windows.Win32.Foundation.BOOLEAN
class NET_VALIDATE_PASSWORD_HASH(Structure):
    Length: UInt32
    Hash: POINTER(Byte)
class NET_VALIDATE_PASSWORD_RESET_INPUT_ARG(Structure):
    InputPersistedFields: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_VALIDATE_PERSISTED_FIELDS
    ClearPassword: win32more.Windows.Win32.Foundation.PWSTR
    UserAccountName: win32more.Windows.Win32.Foundation.PWSTR
    HashedPassword: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_HASH
    PasswordMustChangeAtNextLogon: win32more.Windows.Win32.Foundation.BOOLEAN
    ClearLockout: win32more.Windows.Win32.Foundation.BOOLEAN
NET_VALIDATE_PASSWORD_TYPE = Int32
NetValidateAuthentication: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_TYPE = 1
NetValidatePasswordChange: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_TYPE = 2
NetValidatePasswordReset: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_TYPE = 3
class NET_VALIDATE_PERSISTED_FIELDS(Structure):
    PresentFields: UInt32
    PasswordLastSet: win32more.Windows.Win32.Foundation.FILETIME
    BadPasswordTime: win32more.Windows.Win32.Foundation.FILETIME
    LockoutTime: win32more.Windows.Win32.Foundation.FILETIME
    BadPasswordCount: UInt32
    PasswordHistoryLength: UInt32
    PasswordHistory: POINTER(win32more.Windows.Win32.NetworkManagement.NetManagement.NET_VALIDATE_PASSWORD_HASH)
NetProvisioning = Guid('{2aa2b5fe-b846-4d07-810c-b21ee45320e3}')
class OBO_TOKEN(Structure):
    Type: win32more.Windows.Win32.NetworkManagement.NetManagement.OBO_TOKEN_TYPE
    pncc: win32more.Windows.Win32.NetworkManagement.NetManagement.INetCfgComponent
    pszwManufacturer: win32more.Windows.Win32.Foundation.PWSTR
    pszwProduct: win32more.Windows.Win32.Foundation.PWSTR
    pszwDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    fRegistered: win32more.Windows.Win32.Foundation.BOOL
OBO_TOKEN_TYPE = Int32
OBO_USER: win32more.Windows.Win32.NetworkManagement.NetManagement.OBO_TOKEN_TYPE = 1
OBO_COMPONENT: win32more.Windows.Win32.NetworkManagement.NetManagement.OBO_TOKEN_TYPE = 2
OBO_SOFTWARE: win32more.Windows.Win32.NetworkManagement.NetManagement.OBO_TOKEN_TYPE = 3
class PRINT_OTHER_INFO(Structure):
    alrtpr_jobid: UInt32
    alrtpr_status: UInt32
    alrtpr_submitted: UInt32
    alrtpr_size: UInt32
class RASCON_IPUI(Structure):
    guidConnection: Guid
    fIPv6Cfg: win32more.Windows.Win32.Foundation.BOOL
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
RCUIF_VPN: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 1
RCUIF_DEMAND_DIAL: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 2
RCUIF_NOT_ADMIN: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 4
RCUIF_USE_IPv4_STATICADDRESS: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 8
RCUIF_USE_IPv4_NAME_SERVERS: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 16
RCUIF_USE_IPv4_REMOTE_GATEWAY: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 32
RCUIF_USE_IPv4_EXPLICIT_METRIC: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 64
RCUIF_USE_HEADER_COMPRESSION: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 128
RCUIF_USE_DISABLE_REGISTER_DNS: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 256
RCUIF_USE_PRIVATE_DNS_SUFFIX: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 512
RCUIF_ENABLE_NBT: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 1024
RCUIF_USE_IPv6_STATICADDRESS: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 2048
RCUIF_USE_IPv6_NAME_SERVERS: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 4096
RCUIF_USE_IPv6_REMOTE_GATEWAY: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 8192
RCUIF_USE_IPv6_EXPLICIT_METRIC: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 16384
RCUIF_DISABLE_CLASS_BASED_ROUTE: win32more.Windows.Win32.NetworkManagement.NetManagement.RASCON_UIINFO_FLAGS = 32768
class REPL_EDIR_INFO_0(Structure):
    rped0_dirname: win32more.Windows.Win32.Foundation.PWSTR
class REPL_EDIR_INFO_1(Structure):
    rped1_dirname: win32more.Windows.Win32.Foundation.PWSTR
    rped1_integrity: UInt32
    rped1_extent: UInt32
class REPL_EDIR_INFO_1000(Structure):
    rped1000_integrity: UInt32
class REPL_EDIR_INFO_1001(Structure):
    rped1001_extent: UInt32
class REPL_EDIR_INFO_2(Structure):
    rped2_dirname: win32more.Windows.Win32.Foundation.PWSTR
    rped2_integrity: UInt32
    rped2_extent: UInt32
    rped2_lockcount: UInt32
    rped2_locktime: UInt32
class REPL_IDIR_INFO_0(Structure):
    rpid0_dirname: win32more.Windows.Win32.Foundation.PWSTR
class REPL_IDIR_INFO_1(Structure):
    rpid1_dirname: win32more.Windows.Win32.Foundation.PWSTR
    rpid1_state: UInt32
    rpid1_mastername: win32more.Windows.Win32.Foundation.PWSTR
    rpid1_last_update_time: UInt32
    rpid1_lockcount: UInt32
    rpid1_locktime: UInt32
class REPL_INFO_0(Structure):
    rp0_role: UInt32
    rp0_exportpath: win32more.Windows.Win32.Foundation.PWSTR
    rp0_exportlist: win32more.Windows.Win32.Foundation.PWSTR
    rp0_importpath: win32more.Windows.Win32.Foundation.PWSTR
    rp0_importlist: win32more.Windows.Win32.Foundation.PWSTR
    rp0_logonusername: win32more.Windows.Win32.Foundation.PWSTR
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
    TocEntry: win32more.Windows.Win32.NetworkManagement.NetManagement.RTR_TOC_ENTRY * 1
class RTR_TOC_ENTRY(Structure):
    InfoType: UInt32
    InfoSize: UInt32
    Count: UInt32
    Offset: UInt32
class SERVER_INFO_100(Structure):
    sv100_platform_id: UInt32
    sv100_name: win32more.Windows.Win32.Foundation.PWSTR
class SERVER_INFO_1005(Structure):
    sv1005_comment: win32more.Windows.Win32.Foundation.PWSTR
class SERVER_INFO_101(Structure):
    sv101_platform_id: UInt32
    sv101_name: win32more.Windows.Win32.Foundation.PWSTR
    sv101_version_major: UInt32
    sv101_version_minor: UInt32
    sv101_type: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE
    sv101_comment: win32more.Windows.Win32.Foundation.PWSTR
class SERVER_INFO_1010(Structure):
    sv1010_disc: Int32
class SERVER_INFO_1016(Structure):
    sv1016_hidden: win32more.Windows.Win32.NetworkManagement.NetManagement.SERVER_INFO_HIDDEN
class SERVER_INFO_1017(Structure):
    sv1017_announce: UInt32
class SERVER_INFO_1018(Structure):
    sv1018_anndelta: UInt32
class SERVER_INFO_102(Structure):
    sv102_platform_id: UInt32
    sv102_name: win32more.Windows.Win32.Foundation.PWSTR
    sv102_version_major: UInt32
    sv102_version_minor: UInt32
    sv102_type: win32more.Windows.Win32.NetworkManagement.NetManagement.NET_SERVER_TYPE
    sv102_comment: win32more.Windows.Win32.Foundation.PWSTR
    sv102_users: UInt32
    sv102_disc: Int32
    sv102_hidden: win32more.Windows.Win32.NetworkManagement.NetManagement.SERVER_INFO_HIDDEN
    sv102_announce: UInt32
    sv102_anndelta: UInt32
    sv102_licenses: UInt32
    sv102_userpath: win32more.Windows.Win32.Foundation.PWSTR
class SERVER_INFO_103(Structure):
    sv103_platform_id: UInt32
    sv103_name: win32more.Windows.Win32.Foundation.PWSTR
    sv103_version_major: UInt32
    sv103_version_minor: UInt32
    sv103_type: UInt32
    sv103_comment: win32more.Windows.Win32.Foundation.PWSTR
    sv103_users: UInt32
    sv103_disc: Int32
    sv103_hidden: win32more.Windows.Win32.Foundation.BOOL
    sv103_announce: UInt32
    sv103_anndelta: UInt32
    sv103_licenses: UInt32
    sv103_userpath: win32more.Windows.Win32.Foundation.PWSTR
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
    sv1514_enablesoftcompat: win32more.Windows.Win32.Foundation.BOOL
class SERVER_INFO_1515(Structure):
    sv1515_enableforcedlogoff: win32more.Windows.Win32.Foundation.BOOL
class SERVER_INFO_1516(Structure):
    sv1516_timesource: win32more.Windows.Win32.Foundation.BOOL
class SERVER_INFO_1518(Structure):
    sv1518_lmannounce: win32more.Windows.Win32.Foundation.BOOL
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
    sv1536_enableoplocks: win32more.Windows.Win32.Foundation.BOOL
class SERVER_INFO_1537(Structure):
    sv1537_enableoplockforceclose: win32more.Windows.Win32.Foundation.BOOL
class SERVER_INFO_1538(Structure):
    sv1538_enablefcbopens: win32more.Windows.Win32.Foundation.BOOL
class SERVER_INFO_1539(Structure):
    sv1539_enableraw: win32more.Windows.Win32.Foundation.BOOL
class SERVER_INFO_1540(Structure):
    sv1540_enablesharednetdrives: win32more.Windows.Win32.Foundation.BOOL
class SERVER_INFO_1541(Structure):
    sv1541_minfreeconnections: win32more.Windows.Win32.Foundation.BOOL
class SERVER_INFO_1542(Structure):
    sv1542_maxfreeconnections: win32more.Windows.Win32.Foundation.BOOL
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
    sv1566_removeduplicatesearches: win32more.Windows.Win32.Foundation.BOOL
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
    sv1585_sendsfrompreferredprocessor: win32more.Windows.Win32.Foundation.BOOL
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
    sv1598_enforcekerberosreauthentication: win32more.Windows.Win32.Foundation.BOOLEAN
class SERVER_INFO_1600(Structure):
    sv1598_disabledos: win32more.Windows.Win32.Foundation.BOOLEAN
class SERVER_INFO_1601(Structure):
    sv1598_lowdiskspaceminimum: UInt32
class SERVER_INFO_1602(Structure):
    sv_1598_disablestrictnamechecking: win32more.Windows.Win32.Foundation.BOOL
class SERVER_INFO_402(Structure):
    sv402_ulist_mtime: UInt32
    sv402_glist_mtime: UInt32
    sv402_alist_mtime: UInt32
    sv402_alerts: win32more.Windows.Win32.Foundation.PWSTR
    sv402_security: win32more.Windows.Win32.NetworkManagement.NetManagement.SERVER_INFO_SECURITY
    sv402_numadmin: UInt32
    sv402_lanmask: UInt32
    sv402_guestacct: win32more.Windows.Win32.Foundation.PWSTR
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
    sv402_srvheuristics: win32more.Windows.Win32.Foundation.PWSTR
class SERVER_INFO_403(Structure):
    sv403_ulist_mtime: UInt32
    sv403_glist_mtime: UInt32
    sv403_alist_mtime: UInt32
    sv403_alerts: win32more.Windows.Win32.Foundation.PWSTR
    sv403_security: win32more.Windows.Win32.NetworkManagement.NetManagement.SERVER_INFO_SECURITY
    sv403_numadmin: UInt32
    sv403_lanmask: UInt32
    sv403_guestacct: win32more.Windows.Win32.Foundation.PWSTR
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
    sv403_srvheuristics: win32more.Windows.Win32.Foundation.PWSTR
    sv403_auditedevents: UInt32
    sv403_autoprofile: UInt32
    sv403_autopath: win32more.Windows.Win32.Foundation.PWSTR
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
    sv502_enablesoftcompat: win32more.Windows.Win32.Foundation.BOOL
    sv502_enableforcedlogoff: win32more.Windows.Win32.Foundation.BOOL
    sv502_timesource: win32more.Windows.Win32.Foundation.BOOL
    sv502_acceptdownlevelapis: win32more.Windows.Win32.Foundation.BOOL
    sv502_lmannounce: win32more.Windows.Win32.Foundation.BOOL
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
    sv503_enablesoftcompat: win32more.Windows.Win32.Foundation.BOOL
    sv503_enableforcedlogoff: win32more.Windows.Win32.Foundation.BOOL
    sv503_timesource: win32more.Windows.Win32.Foundation.BOOL
    sv503_acceptdownlevelapis: win32more.Windows.Win32.Foundation.BOOL
    sv503_lmannounce: win32more.Windows.Win32.Foundation.BOOL
    sv503_domain: win32more.Windows.Win32.Foundation.PWSTR
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
    sv503_enableoplocks: win32more.Windows.Win32.Foundation.BOOL
    sv503_enableoplockforceclose: win32more.Windows.Win32.Foundation.BOOL
    sv503_enablefcbopens: win32more.Windows.Win32.Foundation.BOOL
    sv503_enableraw: win32more.Windows.Win32.Foundation.BOOL
    sv503_enablesharednetdrives: win32more.Windows.Win32.Foundation.BOOL
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
    sv598_restrictnullsessaccess: win32more.Windows.Win32.Foundation.BOOL
    sv598_enablewfw311directipx: win32more.Windows.Win32.Foundation.BOOL
    sv598_queuesamplesecs: UInt32
    sv598_balancecount: UInt32
    sv598_preferredaffinity: UInt32
    sv598_maxfreerfcbs: UInt32
    sv598_maxfreemfcbs: UInt32
    sv598_maxfreelfcbs: UInt32
    sv598_maxfreepagedpoolchunks: UInt32
    sv598_minpagedpoolchunksize: UInt32
    sv598_maxpagedpoolchunksize: UInt32
    sv598_sendsfrompreferredprocessor: win32more.Windows.Win32.Foundation.BOOL
    sv598_cacheddirectorylimit: UInt32
    sv598_maxcopylength: UInt32
    sv598_enablecompression: win32more.Windows.Win32.Foundation.BOOL
    sv598_autosharewks: win32more.Windows.Win32.Foundation.BOOL
    sv598_autoshareserver: win32more.Windows.Win32.Foundation.BOOL
    sv598_enablesecuritysignature: win32more.Windows.Win32.Foundation.BOOL
    sv598_requiresecuritysignature: win32more.Windows.Win32.Foundation.BOOL
    sv598_minclientbuffersize: UInt32
    sv598_serverguid: Guid
    sv598_ConnectionNoSessionsTimeout: UInt32
    sv598_IdleThreadTimeOut: UInt32
    sv598_enableW9xsecuritysignature: win32more.Windows.Win32.Foundation.BOOL
    sv598_enforcekerberosreauthentication: win32more.Windows.Win32.Foundation.BOOL
    sv598_disabledos: win32more.Windows.Win32.Foundation.BOOL
    sv598_lowdiskspaceminimum: UInt32
    sv598_disablestrictnamechecking: win32more.Windows.Win32.Foundation.BOOL
    sv598_enableauthenticateusersharing: win32more.Windows.Win32.Foundation.BOOL
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
    sv599_enablesoftcompat: win32more.Windows.Win32.Foundation.BOOL
    sv599_enableforcedlogoff: win32more.Windows.Win32.Foundation.BOOL
    sv599_timesource: win32more.Windows.Win32.Foundation.BOOL
    sv599_acceptdownlevelapis: win32more.Windows.Win32.Foundation.BOOL
    sv599_lmannounce: win32more.Windows.Win32.Foundation.BOOL
    sv599_domain: win32more.Windows.Win32.Foundation.PWSTR
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
    sv599_enableoplocks: win32more.Windows.Win32.Foundation.BOOL
    sv599_enableoplockforceclose: win32more.Windows.Win32.Foundation.BOOL
    sv599_enablefcbopens: win32more.Windows.Win32.Foundation.BOOL
    sv599_enableraw: win32more.Windows.Win32.Foundation.BOOL
    sv599_enablesharednetdrives: win32more.Windows.Win32.Foundation.BOOL
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
SERVER_INFO_HIDDEN = Int32
SV_VISIBLE: win32more.Windows.Win32.NetworkManagement.NetManagement.SERVER_INFO_HIDDEN = 0
SV_HIDDEN: win32more.Windows.Win32.NetworkManagement.NetManagement.SERVER_INFO_HIDDEN = 1
SERVER_INFO_SECURITY = UInt32
SV_SHARESECURITY: win32more.Windows.Win32.NetworkManagement.NetManagement.SERVER_INFO_SECURITY = 0
SV_USERSECURITY: win32more.Windows.Win32.NetworkManagement.NetManagement.SERVER_INFO_SECURITY = 1
class SERVER_TRANSPORT_INFO_0(Structure):
    svti0_numberofvcs: UInt32
    svti0_transportname: win32more.Windows.Win32.Foundation.PWSTR
    svti0_transportaddress: POINTER(Byte)
    svti0_transportaddresslength: UInt32
    svti0_networkaddress: win32more.Windows.Win32.Foundation.PWSTR
class SERVER_TRANSPORT_INFO_1(Structure):
    svti1_numberofvcs: UInt32
    svti1_transportname: win32more.Windows.Win32.Foundation.PWSTR
    svti1_transportaddress: POINTER(Byte)
    svti1_transportaddresslength: UInt32
    svti1_networkaddress: win32more.Windows.Win32.Foundation.PWSTR
    svti1_domain: win32more.Windows.Win32.Foundation.PWSTR
class SERVER_TRANSPORT_INFO_2(Structure):
    svti2_numberofvcs: UInt32
    svti2_transportname: win32more.Windows.Win32.Foundation.PWSTR
    svti2_transportaddress: POINTER(Byte)
    svti2_transportaddresslength: UInt32
    svti2_networkaddress: win32more.Windows.Win32.Foundation.PWSTR
    svti2_domain: win32more.Windows.Win32.Foundation.PWSTR
    svti2_flags: UInt32
class SERVER_TRANSPORT_INFO_3(Structure):
    svti3_numberofvcs: UInt32
    svti3_transportname: win32more.Windows.Win32.Foundation.PWSTR
    svti3_transportaddress: POINTER(Byte)
    svti3_transportaddresslength: UInt32
    svti3_networkaddress: win32more.Windows.Win32.Foundation.PWSTR
    svti3_domain: win32more.Windows.Win32.Foundation.PWSTR
    svti3_flags: UInt32
    svti3_passwordlength: UInt32
    svti3_password: Byte * 256
class SERVICE_INFO_0(Structure):
    svci0_name: win32more.Windows.Win32.Foundation.PWSTR
class SERVICE_INFO_1(Structure):
    svci1_name: win32more.Windows.Win32.Foundation.PWSTR
    svci1_status: UInt32
    svci1_code: UInt32
    svci1_pid: UInt32
class SERVICE_INFO_2(Structure):
    svci2_name: win32more.Windows.Win32.Foundation.PWSTR
    svci2_status: UInt32
    svci2_code: UInt32
    svci2_pid: UInt32
    svci2_text: win32more.Windows.Win32.Foundation.PWSTR
    svci2_specific_error: UInt32
    svci2_display_name: win32more.Windows.Win32.Foundation.PWSTR
class SMB_COMPRESSION_INFO(Structure):
    Switch: win32more.Windows.Win32.Foundation.BOOLEAN
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
NCF_LOWER: win32more.Windows.Win32.NetworkManagement.NetManagement.SUPPORTS_BINDING_INTERFACE_FLAGS = 1
NCF_UPPER: win32more.Windows.Win32.NetworkManagement.NetManagement.SUPPORTS_BINDING_INTERFACE_FLAGS = 2
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
    Type: win32more.Windows.Win32.NetworkManagement.NetManagement.TRANSPORT_TYPE
    SkipCertificateCheck: win32more.Windows.Win32.Foundation.BOOLEAN
TRANSPORT_TYPE = Int32
UseTransportType_None: win32more.Windows.Win32.NetworkManagement.NetManagement.TRANSPORT_TYPE = 0
UseTransportType_Wsk: win32more.Windows.Win32.NetworkManagement.NetManagement.TRANSPORT_TYPE = 1
UseTransportType_Quic: win32more.Windows.Win32.NetworkManagement.NetManagement.TRANSPORT_TYPE = 2
USER_ACCOUNT_FLAGS = UInt32
UF_SCRIPT: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 1
UF_ACCOUNTDISABLE: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 2
UF_HOMEDIR_REQUIRED: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 8
UF_PASSWD_NOTREQD: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 32
UF_PASSWD_CANT_CHANGE: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 64
UF_LOCKOUT: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 16
UF_DONT_EXPIRE_PASSWD: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 65536
UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 128
UF_NOT_DELEGATED: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 1048576
UF_SMARTCARD_REQUIRED: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 262144
UF_USE_DES_KEY_ONLY: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 2097152
UF_DONT_REQUIRE_PREAUTH: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 4194304
UF_TRUSTED_FOR_DELEGATION: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 524288
UF_PASSWORD_EXPIRED: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 8388608
UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS = 16777216
class USER_INFO_0(Structure):
    usri0_name: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1(Structure):
    usri1_name: win32more.Windows.Win32.Foundation.PWSTR
    usri1_password: win32more.Windows.Win32.Foundation.PWSTR
    usri1_password_age: UInt32
    usri1_priv: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_PRIV
    usri1_home_dir: win32more.Windows.Win32.Foundation.PWSTR
    usri1_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri1_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri1_script_path: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_10(Structure):
    usri10_name: win32more.Windows.Win32.Foundation.PWSTR
    usri10_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri10_usr_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri10_full_name: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1003(Structure):
    usri1003_password: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1005(Structure):
    usri1005_priv: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_PRIV
class USER_INFO_1006(Structure):
    usri1006_home_dir: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1007(Structure):
    usri1007_comment: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1008(Structure):
    usri1008_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
class USER_INFO_1009(Structure):
    usri1009_script_path: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1010(Structure):
    usri1010_auth_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.AF_OP
class USER_INFO_1011(Structure):
    usri1011_full_name: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1012(Structure):
    usri1012_usr_comment: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1013(Structure):
    usri1013_parms: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1014(Structure):
    usri1014_workstations: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1017(Structure):
    usri1017_acct_expires: UInt32
class USER_INFO_1018(Structure):
    usri1018_max_storage: UInt32
class USER_INFO_1020(Structure):
    usri1020_units_per_week: UInt32
    usri1020_logon_hours: POINTER(Byte)
class USER_INFO_1023(Structure):
    usri1023_logon_server: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1024(Structure):
    usri1024_country_code: UInt32
class USER_INFO_1025(Structure):
    usri1025_code_page: UInt32
class USER_INFO_1051(Structure):
    usri1051_primary_group_id: UInt32
class USER_INFO_1052(Structure):
    usri1052_profile: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_1053(Structure):
    usri1053_home_dir_drive: win32more.Windows.Win32.Foundation.PWSTR
class USER_INFO_11(Structure):
    usri11_name: win32more.Windows.Win32.Foundation.PWSTR
    usri11_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri11_usr_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri11_full_name: win32more.Windows.Win32.Foundation.PWSTR
    usri11_priv: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_PRIV
    usri11_auth_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.AF_OP
    usri11_password_age: UInt32
    usri11_home_dir: win32more.Windows.Win32.Foundation.PWSTR
    usri11_parms: win32more.Windows.Win32.Foundation.PWSTR
    usri11_last_logon: UInt32
    usri11_last_logoff: UInt32
    usri11_bad_pw_count: UInt32
    usri11_num_logons: UInt32
    usri11_logon_server: win32more.Windows.Win32.Foundation.PWSTR
    usri11_country_code: UInt32
    usri11_workstations: win32more.Windows.Win32.Foundation.PWSTR
    usri11_max_storage: UInt32
    usri11_units_per_week: UInt32
    usri11_logon_hours: POINTER(Byte)
    usri11_code_page: UInt32
class USER_INFO_2(Structure):
    usri2_name: win32more.Windows.Win32.Foundation.PWSTR
    usri2_password: win32more.Windows.Win32.Foundation.PWSTR
    usri2_password_age: UInt32
    usri2_priv: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_PRIV
    usri2_home_dir: win32more.Windows.Win32.Foundation.PWSTR
    usri2_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri2_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri2_script_path: win32more.Windows.Win32.Foundation.PWSTR
    usri2_auth_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.AF_OP
    usri2_full_name: win32more.Windows.Win32.Foundation.PWSTR
    usri2_usr_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri2_parms: win32more.Windows.Win32.Foundation.PWSTR
    usri2_workstations: win32more.Windows.Win32.Foundation.PWSTR
    usri2_last_logon: UInt32
    usri2_last_logoff: UInt32
    usri2_acct_expires: UInt32
    usri2_max_storage: UInt32
    usri2_units_per_week: UInt32
    usri2_logon_hours: POINTER(Byte)
    usri2_bad_pw_count: UInt32
    usri2_num_logons: UInt32
    usri2_logon_server: win32more.Windows.Win32.Foundation.PWSTR
    usri2_country_code: UInt32
    usri2_code_page: UInt32
class USER_INFO_20(Structure):
    usri20_name: win32more.Windows.Win32.Foundation.PWSTR
    usri20_full_name: win32more.Windows.Win32.Foundation.PWSTR
    usri20_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri20_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri20_user_id: UInt32
class USER_INFO_21(Structure):
    usri21_password: Byte * 16
class USER_INFO_22(Structure):
    usri22_name: win32more.Windows.Win32.Foundation.PWSTR
    usri22_password: Byte * 16
    usri22_password_age: UInt32
    usri22_priv: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_PRIV
    usri22_home_dir: win32more.Windows.Win32.Foundation.PWSTR
    usri22_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri22_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri22_script_path: win32more.Windows.Win32.Foundation.PWSTR
    usri22_auth_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.AF_OP
    usri22_full_name: win32more.Windows.Win32.Foundation.PWSTR
    usri22_usr_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri22_parms: win32more.Windows.Win32.Foundation.PWSTR
    usri22_workstations: win32more.Windows.Win32.Foundation.PWSTR
    usri22_last_logon: UInt32
    usri22_last_logoff: UInt32
    usri22_acct_expires: UInt32
    usri22_max_storage: UInt32
    usri22_units_per_week: UInt32
    usri22_logon_hours: POINTER(Byte)
    usri22_bad_pw_count: UInt32
    usri22_num_logons: UInt32
    usri22_logon_server: win32more.Windows.Win32.Foundation.PWSTR
    usri22_country_code: UInt32
    usri22_code_page: UInt32
class USER_INFO_23(Structure):
    usri23_name: win32more.Windows.Win32.Foundation.PWSTR
    usri23_full_name: win32more.Windows.Win32.Foundation.PWSTR
    usri23_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri23_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri23_user_sid: win32more.Windows.Win32.Security.PSID
class USER_INFO_24(Structure):
    usri24_internet_identity: win32more.Windows.Win32.Foundation.BOOL
    usri24_flags: UInt32
    usri24_internet_provider_name: win32more.Windows.Win32.Foundation.PWSTR
    usri24_internet_principal_name: win32more.Windows.Win32.Foundation.PWSTR
    usri24_user_sid: win32more.Windows.Win32.Security.PSID
class USER_INFO_3(Structure):
    usri3_name: win32more.Windows.Win32.Foundation.PWSTR
    usri3_password: win32more.Windows.Win32.Foundation.PWSTR
    usri3_password_age: UInt32
    usri3_priv: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_PRIV
    usri3_home_dir: win32more.Windows.Win32.Foundation.PWSTR
    usri3_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri3_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri3_script_path: win32more.Windows.Win32.Foundation.PWSTR
    usri3_auth_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.AF_OP
    usri3_full_name: win32more.Windows.Win32.Foundation.PWSTR
    usri3_usr_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri3_parms: win32more.Windows.Win32.Foundation.PWSTR
    usri3_workstations: win32more.Windows.Win32.Foundation.PWSTR
    usri3_last_logon: UInt32
    usri3_last_logoff: UInt32
    usri3_acct_expires: UInt32
    usri3_max_storage: UInt32
    usri3_units_per_week: UInt32
    usri3_logon_hours: POINTER(Byte)
    usri3_bad_pw_count: UInt32
    usri3_num_logons: UInt32
    usri3_logon_server: win32more.Windows.Win32.Foundation.PWSTR
    usri3_country_code: UInt32
    usri3_code_page: UInt32
    usri3_user_id: UInt32
    usri3_primary_group_id: UInt32
    usri3_profile: win32more.Windows.Win32.Foundation.PWSTR
    usri3_home_dir_drive: win32more.Windows.Win32.Foundation.PWSTR
    usri3_password_expired: UInt32
class USER_INFO_4(Structure):
    usri4_name: win32more.Windows.Win32.Foundation.PWSTR
    usri4_password: win32more.Windows.Win32.Foundation.PWSTR
    usri4_password_age: UInt32
    usri4_priv: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_PRIV
    usri4_home_dir: win32more.Windows.Win32.Foundation.PWSTR
    usri4_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri4_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_ACCOUNT_FLAGS
    usri4_script_path: win32more.Windows.Win32.Foundation.PWSTR
    usri4_auth_flags: win32more.Windows.Win32.NetworkManagement.NetManagement.AF_OP
    usri4_full_name: win32more.Windows.Win32.Foundation.PWSTR
    usri4_usr_comment: win32more.Windows.Win32.Foundation.PWSTR
    usri4_parms: win32more.Windows.Win32.Foundation.PWSTR
    usri4_workstations: win32more.Windows.Win32.Foundation.PWSTR
    usri4_last_logon: UInt32
    usri4_last_logoff: UInt32
    usri4_acct_expires: UInt32
    usri4_max_storage: UInt32
    usri4_units_per_week: UInt32
    usri4_logon_hours: POINTER(Byte)
    usri4_bad_pw_count: UInt32
    usri4_num_logons: UInt32
    usri4_logon_server: win32more.Windows.Win32.Foundation.PWSTR
    usri4_country_code: UInt32
    usri4_code_page: UInt32
    usri4_user_sid: win32more.Windows.Win32.Security.PSID
    usri4_primary_group_id: UInt32
    usri4_profile: win32more.Windows.Win32.Foundation.PWSTR
    usri4_home_dir_drive: win32more.Windows.Win32.Foundation.PWSTR
    usri4_password_expired: UInt32
class USER_MODALS_INFO_0(Structure):
    usrmod0_min_passwd_len: UInt32
    usrmod0_max_passwd_age: UInt32
    usrmod0_min_passwd_age: UInt32
    usrmod0_force_logoff: UInt32
    usrmod0_password_hist_len: UInt32
class USER_MODALS_INFO_1(Structure):
    usrmod1_role: UInt32
    usrmod1_primary: win32more.Windows.Win32.Foundation.PWSTR
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
    usrmod1006_role: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_MODALS_ROLES
class USER_MODALS_INFO_1007(Structure):
    usrmod1007_primary: win32more.Windows.Win32.Foundation.PWSTR
class USER_MODALS_INFO_2(Structure):
    usrmod2_domain_name: win32more.Windows.Win32.Foundation.PWSTR
    usrmod2_domain_id: win32more.Windows.Win32.Security.PSID
class USER_MODALS_INFO_3(Structure):
    usrmod3_lockout_duration: UInt32
    usrmod3_lockout_observation_window: UInt32
    usrmod3_lockout_threshold: UInt32
USER_MODALS_ROLES = UInt32
UAS_ROLE_STANDALONE: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_MODALS_ROLES = 0
UAS_ROLE_MEMBER: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_MODALS_ROLES = 1
UAS_ROLE_BACKUP: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_MODALS_ROLES = 2
UAS_ROLE_PRIMARY: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_MODALS_ROLES = 3
class USER_OTHER_INFO(Structure):
    alrtus_errcode: UInt32
    alrtus_numstrings: UInt32
USER_PRIV = UInt32
USER_PRIV_GUEST: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_PRIV = 0
USER_PRIV_USER: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_PRIV = 1
USER_PRIV_ADMIN: win32more.Windows.Win32.NetworkManagement.NetManagement.USER_PRIV = 2
class USE_INFO_0(Structure):
    ui0_local: win32more.Windows.Win32.Foundation.PWSTR
    ui0_remote: win32more.Windows.Win32.Foundation.PWSTR
class USE_INFO_1(Structure):
    ui1_local: win32more.Windows.Win32.Foundation.PWSTR
    ui1_remote: win32more.Windows.Win32.Foundation.PWSTR
    ui1_password: win32more.Windows.Win32.Foundation.PWSTR
    ui1_status: UInt32
    ui1_asg_type: win32more.Windows.Win32.NetworkManagement.NetManagement.USE_INFO_ASG_TYPE
    ui1_refcount: UInt32
    ui1_usecount: UInt32
class USE_INFO_2(Structure):
    ui2_local: win32more.Windows.Win32.Foundation.PWSTR
    ui2_remote: win32more.Windows.Win32.Foundation.PWSTR
    ui2_password: win32more.Windows.Win32.Foundation.PWSTR
    ui2_status: UInt32
    ui2_asg_type: win32more.Windows.Win32.NetworkManagement.NetManagement.USE_INFO_ASG_TYPE
    ui2_refcount: UInt32
    ui2_usecount: UInt32
    ui2_username: win32more.Windows.Win32.Foundation.PWSTR
    ui2_domainname: win32more.Windows.Win32.Foundation.PWSTR
class USE_INFO_3(Structure):
    ui3_ui2: win32more.Windows.Win32.NetworkManagement.NetManagement.USE_INFO_2
    ui3_flags: UInt32
class USE_INFO_4(Structure):
    ui4_ui3: win32more.Windows.Win32.NetworkManagement.NetManagement.USE_INFO_3
    ui4_auth_identity_length: UInt32
    ui4_auth_identity: POINTER(Byte)
class USE_INFO_5(Structure):
    ui4_ui3: win32more.Windows.Win32.NetworkManagement.NetManagement.USE_INFO_3
    ui4_auth_identity_length: UInt32
    ui4_auth_identity: POINTER(Byte)
    ui5_security_descriptor_length: UInt32
    ui5_security_descriptor: POINTER(Byte)
    ui5_use_options_length: UInt32
    ui5_use_options: POINTER(Byte)
USE_INFO_ASG_TYPE = UInt32
USE_WILDCARD: win32more.Windows.Win32.NetworkManagement.NetManagement.USE_INFO_ASG_TYPE = 4294967295
USE_DISKDEV: win32more.Windows.Win32.NetworkManagement.NetManagement.USE_INFO_ASG_TYPE = 0
USE_SPOOLDEV: win32more.Windows.Win32.NetworkManagement.NetManagement.USE_INFO_ASG_TYPE = 1
USE_IPC: win32more.Windows.Win32.NetworkManagement.NetManagement.USE_INFO_ASG_TYPE = 3
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
    pInfo: VoidPtr
    Length: UIntPtr
class USE_OPTION_TRANSPORT_PARAMETERS(Structure):
    Tag: UInt32
    Length: UInt16
    Reserved: UInt16
class WKSTA_INFO_100(Structure):
    wki100_platform_id: UInt32
    wki100_computername: win32more.Windows.Win32.Foundation.PWSTR
    wki100_langroup: win32more.Windows.Win32.Foundation.PWSTR
    wki100_ver_major: UInt32
    wki100_ver_minor: UInt32
class WKSTA_INFO_101(Structure):
    wki101_platform_id: UInt32
    wki101_computername: win32more.Windows.Win32.Foundation.PWSTR
    wki101_langroup: win32more.Windows.Win32.Foundation.PWSTR
    wki101_ver_major: UInt32
    wki101_ver_minor: UInt32
    wki101_lanroot: win32more.Windows.Win32.Foundation.PWSTR
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
    wki102_computername: win32more.Windows.Win32.Foundation.PWSTR
    wki102_langroup: win32more.Windows.Win32.Foundation.PWSTR
    wki102_ver_major: UInt32
    wki102_ver_minor: UInt32
    wki102_lanroot: win32more.Windows.Win32.Foundation.PWSTR
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
    wki1048_use_opportunistic_locking: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1049(Structure):
    wki1049_use_unlock_behind: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1050(Structure):
    wki1050_use_close_behind: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1051(Structure):
    wki1051_buf_named_pipes: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1052(Structure):
    wki1052_use_lock_read_unlock: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1053(Structure):
    wki1053_utilize_nt_caching: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1054(Structure):
    wki1054_use_raw_read: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1055(Structure):
    wki1055_use_raw_write: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1056(Structure):
    wki1056_use_write_raw_data: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1057(Structure):
    wki1057_use_encryption: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1058(Structure):
    wki1058_buf_files_deny_write: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1059(Structure):
    wki1059_buf_read_only_files: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1060(Structure):
    wki1060_force_core_create_mode: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_INFO_1061(Structure):
    wki1061_use_512_byte_max_transfer: win32more.Windows.Win32.Foundation.BOOL
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
    wki302_wrk_heuristics: win32more.Windows.Win32.Foundation.PWSTR
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
    wki402_wrk_heuristics: win32more.Windows.Win32.Foundation.PWSTR
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
    wki502_log_election_packets: win32more.Windows.Win32.Foundation.BOOL
    wki502_use_opportunistic_locking: win32more.Windows.Win32.Foundation.BOOL
    wki502_use_unlock_behind: win32more.Windows.Win32.Foundation.BOOL
    wki502_use_close_behind: win32more.Windows.Win32.Foundation.BOOL
    wki502_buf_named_pipes: win32more.Windows.Win32.Foundation.BOOL
    wki502_use_lock_read_unlock: win32more.Windows.Win32.Foundation.BOOL
    wki502_utilize_nt_caching: win32more.Windows.Win32.Foundation.BOOL
    wki502_use_raw_read: win32more.Windows.Win32.Foundation.BOOL
    wki502_use_raw_write: win32more.Windows.Win32.Foundation.BOOL
    wki502_use_write_raw_data: win32more.Windows.Win32.Foundation.BOOL
    wki502_use_encryption: win32more.Windows.Win32.Foundation.BOOL
    wki502_buf_files_deny_write: win32more.Windows.Win32.Foundation.BOOL
    wki502_buf_read_only_files: win32more.Windows.Win32.Foundation.BOOL
    wki502_force_core_create_mode: win32more.Windows.Win32.Foundation.BOOL
    wki502_use_512_byte_max_transfer: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_TRANSPORT_INFO_0(Structure):
    wkti0_quality_of_service: UInt32
    wkti0_number_of_vcs: UInt32
    wkti0_transport_name: win32more.Windows.Win32.Foundation.PWSTR
    wkti0_transport_address: win32more.Windows.Win32.Foundation.PWSTR
    wkti0_wan_ish: win32more.Windows.Win32.Foundation.BOOL
class WKSTA_USER_INFO_0(Structure):
    wkui0_username: win32more.Windows.Win32.Foundation.PWSTR
class WKSTA_USER_INFO_1(Structure):
    wkui1_username: win32more.Windows.Win32.Foundation.PWSTR
    wkui1_logon_domain: win32more.Windows.Win32.Foundation.PWSTR
    wkui1_oth_domains: win32more.Windows.Win32.Foundation.PWSTR
    wkui1_logon_server: win32more.Windows.Win32.Foundation.PWSTR
class WKSTA_USER_INFO_1101(Structure):
    wkui1101_oth_domains: win32more.Windows.Win32.Foundation.PWSTR
@winfunctype_pointer
def WORKERFUNCTION(param0: VoidPtr) -> Void: ...


make_ready(__name__)
