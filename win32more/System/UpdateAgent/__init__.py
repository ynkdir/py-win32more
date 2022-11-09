from win32more.base import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.UpdateAgent

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
LIBID_WUApiLib = 'b596cc9f-56e5-419e-a622-e01bb457431e'
UPDATE_LOCKDOWN_WEBSITE_ACCESS = 1
WU_S_SERVICE_STOP = 2359297
WU_S_SELFUPDATE = 2359298
WU_S_UPDATE_ERROR = 2359299
WU_S_MARKED_FOR_DISCONNECT = 2359300
WU_S_REBOOT_REQUIRED = 2359301
WU_S_ALREADY_INSTALLED = 2359302
WU_S_ALREADY_UNINSTALLED = 2359303
WU_S_ALREADY_DOWNLOADED = 2359304
WU_S_SOME_UPDATES_SKIPPED_ON_BATTERY = 2359305
WU_S_ALREADY_REVERTED = 2359306
WU_S_SEARCH_CRITERIA_NOT_SUPPORTED = 2359312
WU_S_UH_INSTALLSTILLPENDING = 2367509
WU_S_UH_DOWNLOAD_SIZE_CALCULATED = 2367510
WU_S_SIH_NOOP = 2379777
WU_S_DM_ALREADYDOWNLOADING = 2383873
WU_S_METADATA_SKIPPED_BY_ENFORCEMENTMODE = 2388225
WU_S_METADATA_IGNORED_SIGNATURE_VERIFICATION = 2388226
WU_S_SEARCH_LOAD_SHEDDING = 2392065
WU_E_NO_SERVICE = -2145124351
WU_E_MAX_CAPACITY_REACHED = -2145124350
WU_E_UNKNOWN_ID = -2145124349
WU_E_NOT_INITIALIZED = -2145124348
WU_E_RANGEOVERLAP = -2145124347
WU_E_TOOMANYRANGES = -2145124346
WU_E_INVALIDINDEX = -2145124345
WU_E_ITEMNOTFOUND = -2145124344
WU_E_OPERATIONINPROGRESS = -2145124343
WU_E_COULDNOTCANCEL = -2145124342
WU_E_CALL_CANCELLED = -2145124341
WU_E_NOOP = -2145124340
WU_E_XML_MISSINGDATA = -2145124339
WU_E_XML_INVALID = -2145124338
WU_E_CYCLE_DETECTED = -2145124337
WU_E_TOO_DEEP_RELATION = -2145124336
WU_E_INVALID_RELATIONSHIP = -2145124335
WU_E_REG_VALUE_INVALID = -2145124334
WU_E_DUPLICATE_ITEM = -2145124333
WU_E_INVALID_INSTALL_REQUESTED = -2145124332
WU_E_INSTALL_NOT_ALLOWED = -2145124330
WU_E_NOT_APPLICABLE = -2145124329
WU_E_NO_USERTOKEN = -2145124328
WU_E_EXCLUSIVE_INSTALL_CONFLICT = -2145124327
WU_E_POLICY_NOT_SET = -2145124326
WU_E_SELFUPDATE_IN_PROGRESS = -2145124325
WU_E_INVALID_UPDATE = -2145124323
WU_E_SERVICE_STOP = -2145124322
WU_E_NO_CONNECTION = -2145124321
WU_E_NO_INTERACTIVE_USER = -2145124320
WU_E_TIME_OUT = -2145124319
WU_E_ALL_UPDATES_FAILED = -2145124318
WU_E_EULAS_DECLINED = -2145124317
WU_E_NO_UPDATE = -2145124316
WU_E_USER_ACCESS_DISABLED = -2145124315
WU_E_INVALID_UPDATE_TYPE = -2145124314
WU_E_URL_TOO_LONG = -2145124313
WU_E_UNINSTALL_NOT_ALLOWED = -2145124312
WU_E_INVALID_PRODUCT_LICENSE = -2145124311
WU_E_MISSING_HANDLER = -2145124310
WU_E_LEGACYSERVER = -2145124309
WU_E_BIN_SOURCE_ABSENT = -2145124308
WU_E_SOURCE_ABSENT = -2145124307
WU_E_WU_DISABLED = -2145124306
WU_E_CALL_CANCELLED_BY_POLICY = -2145124305
WU_E_INVALID_PROXY_SERVER = -2145124304
WU_E_INVALID_FILE = -2145124303
WU_E_INVALID_CRITERIA = -2145124302
WU_E_EULA_UNAVAILABLE = -2145124301
WU_E_DOWNLOAD_FAILED = -2145124300
WU_E_UPDATE_NOT_PROCESSED = -2145124299
WU_E_INVALID_OPERATION = -2145124298
WU_E_NOT_SUPPORTED = -2145124297
WU_E_WINHTTP_INVALID_FILE = -2145124296
WU_E_TOO_MANY_RESYNC = -2145124295
WU_E_NO_SERVER_CORE_SUPPORT = -2145124288
WU_E_SYSPREP_IN_PROGRESS = -2145124287
WU_E_UNKNOWN_SERVICE = -2145124286
WU_E_NO_UI_SUPPORT = -2145124285
WU_E_PER_MACHINE_UPDATE_ACCESS_DENIED = -2145124284
WU_E_UNSUPPORTED_SEARCHSCOPE = -2145124283
WU_E_BAD_FILE_URL = -2145124282
WU_E_REVERT_NOT_ALLOWED = -2145124281
WU_E_INVALID_NOTIFICATION_INFO = -2145124280
WU_E_OUTOFRANGE = -2145124279
WU_E_SETUP_IN_PROGRESS = -2145124278
WU_E_ORPHANED_DOWNLOAD_JOB = -2145124277
WU_E_LOW_BATTERY = -2145124276
WU_E_INFRASTRUCTUREFILE_INVALID_FORMAT = -2145124275
WU_E_INFRASTRUCTUREFILE_REQUIRES_SSL = -2145124274
WU_E_IDLESHUTDOWN_OPCOUNT_DISCOVERY = -2145124273
WU_E_IDLESHUTDOWN_OPCOUNT_SEARCH = -2145124272
WU_E_IDLESHUTDOWN_OPCOUNT_DOWNLOAD = -2145124271
WU_E_IDLESHUTDOWN_OPCOUNT_INSTALL = -2145124270
WU_E_IDLESHUTDOWN_OPCOUNT_OTHER = -2145124269
WU_E_INTERACTIVE_CALL_CANCELLED = -2145124268
WU_E_AU_CALL_CANCELLED = -2145124267
WU_E_SYSTEM_UNSUPPORTED = -2145124266
WU_E_NO_SUCH_HANDLER_PLUGIN = -2145124265
WU_E_INVALID_SERIALIZATION_VERSION = -2145124264
WU_E_NETWORK_COST_EXCEEDS_POLICY = -2145124263
WU_E_CALL_CANCELLED_BY_HIDE = -2145124262
WU_E_CALL_CANCELLED_BY_INVALID = -2145124261
WU_E_INVALID_VOLUMEID = -2145124260
WU_E_UNRECOGNIZED_VOLUMEID = -2145124259
WU_E_EXTENDEDERROR_NOTSET = -2145124258
WU_E_EXTENDEDERROR_FAILED = -2145124257
WU_E_IDLESHUTDOWN_OPCOUNT_SERVICEREGISTRATION = -2145124256
WU_E_FILETRUST_SHA2SIGNATURE_MISSING = -2145124255
WU_E_UPDATE_NOT_APPROVED = -2145124254
WU_E_CALL_CANCELLED_BY_INTERACTIVE_SEARCH = -2145124253
WU_E_INSTALL_JOB_RESUME_NOT_ALLOWED = -2145124252
WU_E_INSTALL_JOB_NOT_SUSPENDED = -2145124251
WU_E_INSTALL_USERCONTEXT_ACCESSDENIED = -2145124250
WU_E_UNEXPECTED = -2145120257
WU_E_MSI_WRONG_VERSION = -2145120255
WU_E_MSI_NOT_CONFIGURED = -2145120254
WU_E_MSP_DISABLED = -2145120253
WU_E_MSI_WRONG_APP_CONTEXT = -2145120252
WU_E_MSI_NOT_PRESENT = -2145120251
WU_E_MSP_UNEXPECTED = -2145116161
WU_E_PT_SOAPCLIENT_BASE = -2145107968
WU_E_PT_SOAPCLIENT_INITIALIZE = -2145107967
WU_E_PT_SOAPCLIENT_OUTOFMEMORY = -2145107966
WU_E_PT_SOAPCLIENT_GENERATE = -2145107965
WU_E_PT_SOAPCLIENT_CONNECT = -2145107964
WU_E_PT_SOAPCLIENT_SEND = -2145107963
WU_E_PT_SOAPCLIENT_SERVER = -2145107962
WU_E_PT_SOAPCLIENT_SOAPFAULT = -2145107961
WU_E_PT_SOAPCLIENT_PARSEFAULT = -2145107960
WU_E_PT_SOAPCLIENT_READ = -2145107959
WU_E_PT_SOAPCLIENT_PARSE = -2145107958
WU_E_PT_SOAP_VERSION = -2145107957
WU_E_PT_SOAP_MUST_UNDERSTAND = -2145107956
WU_E_PT_SOAP_CLIENT = -2145107955
WU_E_PT_SOAP_SERVER = -2145107954
WU_E_PT_WMI_ERROR = -2145107953
WU_E_PT_EXCEEDED_MAX_SERVER_TRIPS = -2145107952
WU_E_PT_SUS_SERVER_NOT_SET = -2145107951
WU_E_PT_DOUBLE_INITIALIZATION = -2145107950
WU_E_PT_INVALID_COMPUTER_NAME = -2145107949
WU_E_PT_REFRESH_CACHE_REQUIRED = -2145107947
WU_E_PT_HTTP_STATUS_BAD_REQUEST = -2145107946
WU_E_PT_HTTP_STATUS_DENIED = -2145107945
WU_E_PT_HTTP_STATUS_FORBIDDEN = -2145107944
WU_E_PT_HTTP_STATUS_NOT_FOUND = -2145107943
WU_E_PT_HTTP_STATUS_BAD_METHOD = -2145107942
WU_E_PT_HTTP_STATUS_PROXY_AUTH_REQ = -2145107941
WU_E_PT_HTTP_STATUS_REQUEST_TIMEOUT = -2145107940
WU_E_PT_HTTP_STATUS_CONFLICT = -2145107939
WU_E_PT_HTTP_STATUS_GONE = -2145107938
WU_E_PT_HTTP_STATUS_SERVER_ERROR = -2145107937
WU_E_PT_HTTP_STATUS_NOT_SUPPORTED = -2145107936
WU_E_PT_HTTP_STATUS_BAD_GATEWAY = -2145107935
WU_E_PT_HTTP_STATUS_SERVICE_UNAVAIL = -2145107934
WU_E_PT_HTTP_STATUS_GATEWAY_TIMEOUT = -2145107933
WU_E_PT_HTTP_STATUS_VERSION_NOT_SUP = -2145107932
WU_E_PT_FILE_LOCATIONS_CHANGED = -2145107931
WU_E_PT_REGISTRATION_NOT_SUPPORTED = -2145107930
WU_E_PT_NO_AUTH_PLUGINS_REQUESTED = -2145107929
WU_E_PT_NO_AUTH_COOKIES_CREATED = -2145107928
WU_E_PT_INVALID_CONFIG_PROP = -2145107927
WU_E_PT_CONFIG_PROP_MISSING = -2145107926
WU_E_PT_HTTP_STATUS_NOT_MAPPED = -2145107925
WU_E_PT_WINHTTP_NAME_NOT_RESOLVED = -2145107924
WU_E_PT_LOAD_SHEDDING = -2145107923
WU_E_PT_SAME_REDIR_ID = -2145103827
WU_E_PT_NO_MANAGED_RECOVER = -2145103826
WU_E_PT_ECP_SUCCEEDED_WITH_ERRORS = -2145107921
WU_E_PT_ECP_INIT_FAILED = -2145107920
WU_E_PT_ECP_INVALID_FILE_FORMAT = -2145107919
WU_E_PT_ECP_INVALID_METADATA = -2145107918
WU_E_PT_ECP_FAILURE_TO_EXTRACT_DIGEST = -2145107917
WU_E_PT_ECP_FAILURE_TO_DECOMPRESS_CAB_FILE = -2145107916
WU_E_PT_ECP_FILE_LOCATION_ERROR = -2145107915
WU_E_PT_CATALOG_SYNC_REQUIRED = -2145123274
WU_E_PT_SECURITY_VERIFICATION_FAILURE = -2145123273
WU_E_PT_ENDPOINT_UNREACHABLE = -2145123272
WU_E_PT_INVALID_FORMAT = -2145123271
WU_E_PT_INVALID_URL = -2145123270
WU_E_PT_NWS_NOT_LOADED = -2145123269
WU_E_PT_PROXY_AUTH_SCHEME_NOT_SUPPORTED = -2145123268
WU_E_SERVICEPROP_NOTAVAIL = -2145123267
WU_E_PT_ENDPOINT_REFRESH_REQUIRED = -2145123266
WU_E_PT_ENDPOINTURL_NOTAVAIL = -2145123265
WU_E_PT_ENDPOINT_DISCONNECTED = -2145123264
WU_E_PT_INVALID_OPERATION = -2145123263
WU_E_PT_OBJECT_FAULTED = -2145123262
WU_E_PT_NUMERIC_OVERFLOW = -2145123261
WU_E_PT_OPERATION_ABORTED = -2145123260
WU_E_PT_OPERATION_ABANDONED = -2145123259
WU_E_PT_QUOTA_EXCEEDED = -2145123258
WU_E_PT_NO_TRANSLATION_AVAILABLE = -2145123257
WU_E_PT_ADDRESS_IN_USE = -2145123256
WU_E_PT_ADDRESS_NOT_AVAILABLE = -2145123255
WU_E_PT_OTHER = -2145123254
WU_E_PT_SECURITY_SYSTEM_FAILURE = -2145123253
WU_E_PT_UNEXPECTED = -2145103873
WU_E_REDIRECTOR_LOAD_XML = -2145103871
WU_E_REDIRECTOR_S_FALSE = -2145103870
WU_E_REDIRECTOR_ID_SMALLER = -2145103869
WU_E_REDIRECTOR_UNKNOWN_SERVICE = -2145103868
WU_E_REDIRECTOR_UNSUPPORTED_CONTENTTYPE = -2145103867
WU_E_REDIRECTOR_INVALID_RESPONSE = -2145103866
WU_E_REDIRECTOR_ATTRPROVIDER_EXCEEDED_MAX_NAMEVALUE = -2145103864
WU_E_REDIRECTOR_ATTRPROVIDER_INVALID_NAME = -2145103863
WU_E_REDIRECTOR_ATTRPROVIDER_INVALID_VALUE = -2145103862
WU_E_REDIRECTOR_SLS_GENERIC_ERROR = -2145103861
WU_E_REDIRECTOR_CONNECT_POLICY = -2145103860
WU_E_REDIRECTOR_ONLINE_DISALLOWED = -2145103859
WU_E_REDIRECTOR_UNEXPECTED = -2145103617
WU_E_SIH_VERIFY_DOWNLOAD_ENGINE = -2145103615
WU_E_SIH_VERIFY_DOWNLOAD_PAYLOAD = -2145103614
WU_E_SIH_VERIFY_STAGE_ENGINE = -2145103613
WU_E_SIH_VERIFY_STAGE_PAYLOAD = -2145103612
WU_E_SIH_ACTION_NOT_FOUND = -2145103611
WU_E_SIH_SLS_PARSE = -2145103610
WU_E_SIH_INVALIDHASH = -2145103609
WU_E_SIH_NO_ENGINE = -2145103608
WU_E_SIH_POST_REBOOT_INSTALL_FAILED = -2145103607
WU_E_SIH_POST_REBOOT_NO_CACHED_SLS_RESPONSE = -2145103606
WU_E_SIH_PARSE = -2145103605
WU_E_SIH_SECURITY = -2145103604
WU_E_SIH_PPL = -2145103603
WU_E_SIH_POLICY = -2145103602
WU_E_SIH_STDEXCEPTION = -2145103601
WU_E_SIH_NONSTDEXCEPTION = -2145103600
WU_E_SIH_ENGINE_EXCEPTION = -2145103599
WU_E_SIH_BLOCKED_FOR_PLATFORM = -2145103598
WU_E_SIH_ANOTHER_INSTANCE_RUNNING = -2145103597
WU_E_SIH_DNSRESILIENCY_OFF = -2145103596
WU_E_SIH_UNEXPECTED = -2145103361
WU_E_DRV_PRUNED = -2145075199
WU_E_DRV_NOPROP_OR_LEGACY = -2145075198
WU_E_DRV_REG_MISMATCH = -2145075197
WU_E_DRV_NO_METADATA = -2145075196
WU_E_DRV_MISSING_ATTRIBUTE = -2145075195
WU_E_DRV_SYNC_FAILED = -2145075194
WU_E_DRV_NO_PRINTER_CONTENT = -2145075193
WU_E_DRV_DEVICE_PROBLEM = -2145075192
WU_E_DRV_UNEXPECTED = -2145071105
WU_E_DS_SHUTDOWN = -2145091584
WU_E_DS_INUSE = -2145091583
WU_E_DS_INVALID = -2145091582
WU_E_DS_TABLEMISSING = -2145091581
WU_E_DS_TABLEINCORRECT = -2145091580
WU_E_DS_INVALIDTABLENAME = -2145091579
WU_E_DS_BADVERSION = -2145091578
WU_E_DS_NODATA = -2145091577
WU_E_DS_MISSINGDATA = -2145091576
WU_E_DS_MISSINGREF = -2145091575
WU_E_DS_UNKNOWNHANDLER = -2145091574
WU_E_DS_CANTDELETE = -2145091573
WU_E_DS_LOCKTIMEOUTEXPIRED = -2145091572
WU_E_DS_NOCATEGORIES = -2145091571
WU_E_DS_ROWEXISTS = -2145091570
WU_E_DS_STOREFILELOCKED = -2145091569
WU_E_DS_CANNOTREGISTER = -2145091568
WU_E_DS_UNABLETOSTART = -2145091567
WU_E_DS_DUPLICATEUPDATEID = -2145091565
WU_E_DS_UNKNOWNSERVICE = -2145091564
WU_E_DS_SERVICEEXPIRED = -2145091563
WU_E_DS_DECLINENOTALLOWED = -2145091562
WU_E_DS_TABLESESSIONMISMATCH = -2145091561
WU_E_DS_SESSIONLOCKMISMATCH = -2145091560
WU_E_DS_NEEDWINDOWSSERVICE = -2145091559
WU_E_DS_INVALIDOPERATION = -2145091558
WU_E_DS_SCHEMAMISMATCH = -2145091557
WU_E_DS_RESETREQUIRED = -2145091556
WU_E_DS_IMPERSONATED = -2145091555
WU_E_DS_DATANOTAVAILABLE = -2145091554
WU_E_DS_DATANOTLOADED = -2145091553
WU_E_DS_NODATA_NOSUCHREVISION = -2145091552
WU_E_DS_NODATA_NOSUCHUPDATE = -2145091551
WU_E_DS_NODATA_EULA = -2145091550
WU_E_DS_NODATA_SERVICE = -2145091549
WU_E_DS_NODATA_COOKIE = -2145091548
WU_E_DS_NODATA_TIMER = -2145091547
WU_E_DS_NODATA_CCR = -2145091546
WU_E_DS_NODATA_FILE = -2145091545
WU_E_DS_NODATA_DOWNLOADJOB = -2145091544
WU_E_DS_NODATA_TMI = -2145091543
WU_E_DS_UNEXPECTED = -2145087489
WU_E_INVENTORY_PARSEFAILED = -2145087487
WU_E_INVENTORY_GET_INVENTORY_TYPE_FAILED = -2145087486
WU_E_INVENTORY_RESULT_UPLOAD_FAILED = -2145087485
WU_E_INVENTORY_UNEXPECTED = -2145087484
WU_E_INVENTORY_WMI_ERROR = -2145087483
WU_E_AU_NOSERVICE = -2145083392
WU_E_AU_NONLEGACYSERVER = -2145083390
WU_E_AU_LEGACYCLIENTDISABLED = -2145083389
WU_E_AU_PAUSED = -2145083388
WU_E_AU_NO_REGISTERED_SERVICE = -2145083387
WU_E_AU_DETECT_SVCID_MISMATCH = -2145083386
WU_E_REBOOT_IN_PROGRESS = -2145083385
WU_E_AU_OOBE_IN_PROGRESS = -2145083384
WU_E_AU_UNEXPECTED = -2145079297
WU_E_UH_REMOTEUNAVAILABLE = -2145116160
WU_E_UH_LOCALONLY = -2145116159
WU_E_UH_UNKNOWNHANDLER = -2145116158
WU_E_UH_REMOTEALREADYACTIVE = -2145116157
WU_E_UH_DOESNOTSUPPORTACTION = -2145116156
WU_E_UH_WRONGHANDLER = -2145116155
WU_E_UH_INVALIDMETADATA = -2145116154
WU_E_UH_INSTALLERHUNG = -2145116153
WU_E_UH_OPERATIONCANCELLED = -2145116152
WU_E_UH_BADHANDLERXML = -2145116151
WU_E_UH_CANREQUIREINPUT = -2145116150
WU_E_UH_INSTALLERFAILURE = -2145116149
WU_E_UH_FALLBACKTOSELFCONTAINED = -2145116148
WU_E_UH_NEEDANOTHERDOWNLOAD = -2145116147
WU_E_UH_NOTIFYFAILURE = -2145116146
WU_E_UH_INCONSISTENT_FILE_NAMES = -2145116145
WU_E_UH_FALLBACKERROR = -2145116144
WU_E_UH_TOOMANYDOWNLOADREQUESTS = -2145116143
WU_E_UH_UNEXPECTEDCBSRESPONSE = -2145116142
WU_E_UH_BADCBSPACKAGEID = -2145116141
WU_E_UH_POSTREBOOTSTILLPENDING = -2145116140
WU_E_UH_POSTREBOOTRESULTUNKNOWN = -2145116139
WU_E_UH_POSTREBOOTUNEXPECTEDSTATE = -2145116138
WU_E_UH_NEW_SERVICING_STACK_REQUIRED = -2145116137
WU_E_UH_CALLED_BACK_FAILURE = -2145116136
WU_E_UH_CUSTOMINSTALLER_INVALID_SIGNATURE = -2145116135
WU_E_UH_UNSUPPORTED_INSTALLCONTEXT = -2145116134
WU_E_UH_INVALID_TARGETSESSION = -2145116133
WU_E_UH_DECRYPTFAILURE = -2145116132
WU_E_UH_HANDLER_DISABLEDUNTILREBOOT = -2145116131
WU_E_UH_APPX_NOT_PRESENT = -2145116130
WU_E_UH_NOTREADYTOCOMMIT = -2145116129
WU_E_UH_APPX_INVALID_PACKAGE_VOLUME = -2145116128
WU_E_UH_APPX_DEFAULT_PACKAGE_VOLUME_UNAVAILABLE = -2145116127
WU_E_UH_APPX_INSTALLED_PACKAGE_VOLUME_UNAVAILABLE = -2145116126
WU_E_UH_APPX_PACKAGE_FAMILY_NOT_FOUND = -2145116125
WU_E_UH_APPX_SYSTEM_VOLUME_NOT_FOUND = -2145116124
WU_E_UH_UNEXPECTED = -2145112065
WU_E_DM_URLNOTAVAILABLE = -2145099775
WU_E_DM_INCORRECTFILEHASH = -2145099774
WU_E_DM_UNKNOWNALGORITHM = -2145099773
WU_E_DM_NEEDDOWNLOADREQUEST = -2145099772
WU_E_DM_NONETWORK = -2145099771
WU_E_DM_WRONGBITSVERSION = -2145099770
WU_E_DM_NOTDOWNLOADED = -2145099769
WU_E_DM_FAILTOCONNECTTOBITS = -2145099768
WU_E_DM_BITSTRANSFERERROR = -2145099767
WU_E_DM_DOWNLOADLOCATIONCHANGED = -2145099766
WU_E_DM_CONTENTCHANGED = -2145099765
WU_E_DM_DOWNLOADLIMITEDBYUPDATESIZE = -2145099764
WU_E_DM_UNAUTHORIZED = -2145099762
WU_E_DM_BG_ERROR_TOKEN_REQUIRED = -2145099761
WU_E_DM_DOWNLOADSANDBOXNOTFOUND = -2145099760
WU_E_DM_DOWNLOADFILEPATHUNKNOWN = -2145099759
WU_E_DM_DOWNLOADFILEMISSING = -2145099758
WU_E_DM_UPDATEREMOVED = -2145099757
WU_E_DM_READRANGEFAILED = -2145099756
WU_E_DM_UNAUTHORIZED_NO_USER = -2145099754
WU_E_DM_UNAUTHORIZED_LOCAL_USER = -2145099753
WU_E_DM_UNAUTHORIZED_DOMAIN_USER = -2145099752
WU_E_DM_UNAUTHORIZED_MSA_USER = -2145099751
WU_E_DM_FALLINGBACKTOBITS = -2145099750
WU_E_DM_DOWNLOAD_VOLUME_CONFLICT = -2145099749
WU_E_DM_SANDBOX_HASH_MISMATCH = -2145099748
WU_E_DM_HARDRESERVEID_CONFLICT = -2145099747
WU_E_DM_DOSVC_REQUIRED = -2145099746
WU_E_DM_UNEXPECTED = -2145095681
WU_E_SETUP_INVALID_INFDATA = -2145071103
WU_E_SETUP_INVALID_IDENTDATA = -2145071102
WU_E_SETUP_ALREADY_INITIALIZED = -2145071101
WU_E_SETUP_NOT_INITIALIZED = -2145071100
WU_E_SETUP_SOURCE_VERSION_MISMATCH = -2145071099
WU_E_SETUP_TARGET_VERSION_GREATER = -2145071098
WU_E_SETUP_REGISTRATION_FAILED = -2145071097
WU_E_SELFUPDATE_SKIP_ON_FAILURE = -2145071096
WU_E_SETUP_SKIP_UPDATE = -2145071095
WU_E_SETUP_UNSUPPORTED_CONFIGURATION = -2145071094
WU_E_SETUP_BLOCKED_CONFIGURATION = -2145071093
WU_E_SETUP_REBOOT_TO_FIX = -2145071092
WU_E_SETUP_ALREADYRUNNING = -2145071091
WU_E_SETUP_REBOOTREQUIRED = -2145071090
WU_E_SETUP_HANDLER_EXEC_FAILURE = -2145071089
WU_E_SETUP_INVALID_REGISTRY_DATA = -2145071088
WU_E_SELFUPDATE_REQUIRED = -2145071087
WU_E_SELFUPDATE_REQUIRED_ADMIN = -2145071086
WU_E_SETUP_WRONG_SERVER_VERSION = -2145071085
WU_E_SETUP_DEFERRABLE_REBOOT_PENDING = -2145071084
WU_E_SETUP_NON_DEFERRABLE_REBOOT_PENDING = -2145071083
WU_E_SETUP_FAIL = -2145071082
WU_E_SETUP_UNEXPECTED = -2145067009
WU_E_EE_UNKNOWN_EXPRESSION = -2145067007
WU_E_EE_INVALID_EXPRESSION = -2145067006
WU_E_EE_MISSING_METADATA = -2145067005
WU_E_EE_INVALID_VERSION = -2145067004
WU_E_EE_NOT_INITIALIZED = -2145067003
WU_E_EE_INVALID_ATTRIBUTEDATA = -2145067002
WU_E_EE_CLUSTER_ERROR = -2145067001
WU_E_EE_UNEXPECTED = -2145062913
WU_E_INSTALLATION_RESULTS_UNKNOWN_VERSION = -2145112063
WU_E_INSTALLATION_RESULTS_INVALID_DATA = -2145112062
WU_E_INSTALLATION_RESULTS_NOT_FOUND = -2145112061
WU_E_TRAYICON_FAILURE = -2145112060
WU_E_NON_UI_MODE = -2145107971
WU_E_WUCLTUI_UNSUPPORTED_VERSION = -2145107970
WU_E_AUCLIENT_UNEXPECTED = -2145107969
WU_E_REPORTER_EVENTCACHECORRUPT = -2145062911
WU_E_REPORTER_EVENTNAMESPACEPARSEFAILED = -2145062910
WU_E_INVALID_EVENT = -2145062909
WU_E_SERVER_BUSY = -2145062908
WU_E_CALLBACK_COOKIE_NOT_FOUND = -2145062907
WU_E_REPORTER_UNEXPECTED = -2145058817
WU_E_OL_INVALID_SCANFILE = -2145095679
WU_E_OL_NEWCLIENT_REQUIRED = -2145095678
WU_E_INVALID_EVENT_PAYLOAD = -2145095677
WU_E_INVALID_EVENT_PAYLOADSIZE = -2145095676
WU_E_SERVICE_NOT_REGISTERED = -2145095675
WU_E_OL_UNEXPECTED = -2145091585
WU_E_METADATA_NOOP = -2145095424
WU_E_METADATA_CONFIG_INVALID_BINARY_ENCODING = -2145095423
WU_E_METADATA_FETCH_CONFIG = -2145095422
WU_E_METADATA_INVALID_PARAMETER = -2145095420
WU_E_METADATA_UNEXPECTED = -2145095419
WU_E_METADATA_NO_VERIFICATION_DATA = -2145095418
WU_E_METADATA_BAD_FRAGMENTSIGNING_CONFIG = -2145095417
WU_E_METADATA_FAILURE_PROCESSING_FRAGMENTSIGNING_CONFIG = -2145095416
WU_E_METADATA_XML_MISSING = -2145095392
WU_E_METADATA_XML_FRAGMENTSIGNING_MISSING = -2145095391
WU_E_METADATA_XML_MODE_MISSING = -2145095390
WU_E_METADATA_XML_MODE_INVALID = -2145095389
WU_E_METADATA_XML_VALIDITY_INVALID = -2145095388
WU_E_METADATA_XML_LEAFCERT_MISSING = -2145095387
WU_E_METADATA_XML_INTERMEDIATECERT_MISSING = -2145095386
WU_E_METADATA_XML_LEAFCERT_ID_MISSING = -2145095385
WU_E_METADATA_XML_BASE64CERDATA_MISSING = -2145095384
WU_E_METADATA_BAD_SIGNATURE = -2145095360
WU_E_METADATA_UNSUPPORTED_HASH_ALG = -2145095359
WU_E_METADATA_SIGNATURE_VERIFY_FAILED = -2145095358
WU_E_METADATATRUST_CERTIFICATECHAIN_VERIFICATION = -2145095344
WU_E_METADATATRUST_UNTRUSTED_CERTIFICATECHAIN = -2145095343
WU_E_METADATA_TIMESTAMP_TOKEN_MISSING = -2145095328
WU_E_METADATA_TIMESTAMP_TOKEN_VERIFICATION_FAILED = -2145095327
WU_E_METADATA_TIMESTAMP_TOKEN_UNTRUSTED = -2145095326
WU_E_METADATA_TIMESTAMP_TOKEN_VALIDITY_WINDOW = -2145095325
WU_E_METADATA_TIMESTAMP_TOKEN_SIGNATURE = -2145095324
WU_E_METADATA_TIMESTAMP_TOKEN_CERTCHAIN = -2145095323
WU_E_METADATA_TIMESTAMP_TOKEN_REFRESHONLINE = -2145095322
WU_E_METADATA_TIMESTAMP_TOKEN_ALL_BAD = -2145095321
WU_E_METADATA_TIMESTAMP_TOKEN_NODATA = -2145095320
WU_E_METADATA_TIMESTAMP_TOKEN_CACHELOOKUP = -2145095319
WU_E_METADATA_TIMESTAMP_TOKEN_VALIDITYWINDOW_UNEXPECTED = -2145095298
WU_E_METADATA_TIMESTAMP_TOKEN_UNEXPECTED = -2145095297
WU_E_METADATA_CERT_MISSING = -2145095296
WU_E_METADATA_LEAFCERT_BAD_TRANSPORT_ENCODING = -2145095295
WU_E_METADATA_INTCERT_BAD_TRANSPORT_ENCODING = -2145095294
WU_E_METADATA_CERT_UNTRUSTED = -2145095293
WU_E_WUTASK_INPROGRESS = -2145079295
WU_E_WUTASK_STATUS_DISABLED = -2145079294
WU_E_WUTASK_NOT_STARTED = -2145079293
WU_E_WUTASK_RETRY = -2145079292
WU_E_WUTASK_CANCELINSTALL_DISALLOWED = -2145079291
WU_E_UNKNOWN_HARDWARECAPABILITY = -2145079039
WU_E_BAD_XML_HARDWARECAPABILITY = -2145079038
WU_E_WMI_NOT_SUPPORTED = -2145079037
WU_E_UPDATE_MERGE_NOT_ALLOWED = -2145079036
WU_E_SKIPPED_UPDATE_INSTALLATION = -2145079035
WU_E_SLS_INVALID_REVISION = -2145078783
WU_E_FILETRUST_DUALSIGNATURE_RSA = -2145078527
WU_E_FILETRUST_DUALSIGNATURE_ECC = -2145078526
WU_E_TRUST_SUBJECT_NOT_TRUSTED = -2145078525
WU_E_TRUST_PROVIDER_UNKNOWN = -2145078524
StringCollection = Guid('72c97d74-7c3b-40ae-b77d-abdb22eba6fb')
UpdateSearcher = Guid('b699e5e8-67ff-4177-88b0-3684a3388bfb')
WebProxy = Guid('650503cf-9108-4ddc-a2ce-6c2341e1c582')
SystemInformation = Guid('c01b9ba0-bea7-41ba-b604-d0a36f469133')
WindowsUpdateAgentInfo = Guid('c2e88c2f-6f5b-4aaa-894b-55c847ad3a2d')
AutomaticUpdates = Guid('bfe18e9c-6d87-4450-b37c-e02f0b373803')
UpdateCollection = Guid('13639463-00db-4646-803d-528026140d88')
UpdateDownloader = Guid('5baf654a-5a07-4264-a255-9ff54c7151e7')
UpdateInstaller = Guid('d2e0fe7f-d23e-48e1-93c0-6fa8cc346474')
UpdateSession = Guid('4cb43d7f-7eee-4906-8698-60da1c38f2fe')
UpdateServiceManager = Guid('f8d253d9-89a4-4daa-87b6-1168369f0b21')
InstallationAgent = Guid('317e92fc-1679-46fd-a0b5-f08914dd8623')
AutomaticUpdatesNotificationLevel = Int32
AutomaticUpdatesNotificationLevel_aunlNotConfigured = 0
AutomaticUpdatesNotificationLevel_aunlDisabled = 1
AutomaticUpdatesNotificationLevel_aunlNotifyBeforeDownload = 2
AutomaticUpdatesNotificationLevel_aunlNotifyBeforeInstallation = 3
AutomaticUpdatesNotificationLevel_aunlScheduledInstallation = 4
AutomaticUpdatesScheduledInstallationDay = Int32
AutomaticUpdatesScheduledInstallationDay_ausidEveryDay = 0
AutomaticUpdatesScheduledInstallationDay_ausidEverySunday = 1
AutomaticUpdatesScheduledInstallationDay_ausidEveryMonday = 2
AutomaticUpdatesScheduledInstallationDay_ausidEveryTuesday = 3
AutomaticUpdatesScheduledInstallationDay_ausidEveryWednesday = 4
AutomaticUpdatesScheduledInstallationDay_ausidEveryThursday = 5
AutomaticUpdatesScheduledInstallationDay_ausidEveryFriday = 6
AutomaticUpdatesScheduledInstallationDay_ausidEverySaturday = 7
DownloadPhase = Int32
DownloadPhase_dphInitializing = 1
DownloadPhase_dphDownloading = 2
DownloadPhase_dphVerifying = 3
DownloadPriority = Int32
DownloadPriority_dpLow = 1
DownloadPriority_dpNormal = 2
DownloadPriority_dpHigh = 3
DownloadPriority_dpExtraHigh = 4
AutoSelectionMode = Int32
AutoSelectionMode_asLetWindowsUpdateDecide = 0
AutoSelectionMode_asAutoSelectIfDownloaded = 1
AutoSelectionMode_asNeverAutoSelect = 2
AutoSelectionMode_asAlwaysAutoSelect = 3
AutoDownloadMode = Int32
AutoDownloadMode_adLetWindowsUpdateDecide = 0
AutoDownloadMode_adNeverAutoDownload = 1
AutoDownloadMode_adAlwaysAutoDownload = 2
InstallationImpact = Int32
InstallationImpact_iiNormal = 0
InstallationImpact_iiMinor = 1
InstallationImpact_iiRequiresExclusiveHandling = 2
InstallationRebootBehavior = Int32
InstallationRebootBehavior_irbNeverReboots = 0
InstallationRebootBehavior_irbAlwaysRequiresReboot = 1
InstallationRebootBehavior_irbCanRequestReboot = 2
OperationResultCode = Int32
OperationResultCode_orcNotStarted = 0
OperationResultCode_orcInProgress = 1
OperationResultCode_orcSucceeded = 2
OperationResultCode_orcSucceededWithErrors = 3
OperationResultCode_orcFailed = 4
OperationResultCode_orcAborted = 5
ServerSelection = Int32
ServerSelection_ssDefault = 0
ServerSelection_ssManagedServer = 1
ServerSelection_ssWindowsUpdate = 2
ServerSelection_ssOthers = 3
UpdateType = Int32
UpdateType_utSoftware = 1
UpdateType_utDriver = 2
UpdateOperation = Int32
UpdateOperation_uoInstallation = 1
UpdateOperation_uoUninstallation = 2
DeploymentAction = Int32
DeploymentAction_daNone = 0
DeploymentAction_daInstallation = 1
DeploymentAction_daUninstallation = 2
DeploymentAction_daDetection = 3
DeploymentAction_daOptionalInstallation = 4
UpdateExceptionContext = Int32
UpdateExceptionContext_uecGeneral = 1
UpdateExceptionContext_uecWindowsDriver = 2
UpdateExceptionContext_uecWindowsInstaller = 3
UpdateExceptionContext_uecSearchIncomplete = 4
AutomaticUpdatesUserType = Int32
AutomaticUpdatesUserType_auutCurrentUser = 1
AutomaticUpdatesUserType_auutLocalAdministrator = 2
AutomaticUpdatesPermissionType = Int32
AutomaticUpdatesPermissionType_auptSetNotificationLevel = 1
AutomaticUpdatesPermissionType_auptDisableAutomaticUpdates = 2
AutomaticUpdatesPermissionType_auptSetIncludeRecommendedUpdates = 3
AutomaticUpdatesPermissionType_auptSetFeaturedUpdatesEnabled = 4
AutomaticUpdatesPermissionType_auptSetNonAdministratorsElevated = 5
UpdateServiceRegistrationState = Int32
UpdateServiceRegistrationState_usrsNotRegistered = 1
UpdateServiceRegistrationState_usrsRegistrationPending = 2
UpdateServiceRegistrationState_usrsRegistered = 3
SearchScope = Int32
SearchScope_searchScopeDefault = 0
SearchScope_searchScopeMachineOnly = 1
SearchScope_searchScopeCurrentUserOnly = 2
SearchScope_searchScopeMachineAndCurrentUser = 3
SearchScope_searchScopeMachineAndAllUsers = 4
SearchScope_searchScopeAllUsers = 5
def _define_IUpdateLockdown_head():
    class IUpdateLockdown(win32more.System.Com.IUnknown_head):
        Guid = Guid('a976c28d-75a1-42aa-94ae-8af8b872089a')
    return IUpdateLockdown
def _define_IUpdateLockdown():
    IUpdateLockdown = win32more.System.UpdateAgent.IUpdateLockdown_head
    IUpdateLockdown.LockDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'LockDown', ((1, 'flags'),)))
    win32more.System.Com.IUnknown
    return IUpdateLockdown
def _define_IStringCollection_head():
    class IStringCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('eff90582-2ddc-480f-a06d-60f3fbc362c3')
    return IStringCollection
def _define_IStringCollection():
    IStringCollection = win32more.System.UpdateAgent.IStringCollection_head
    IStringCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Item', ((1, 'index'),(1, 'retval'),)))
    IStringCollection.put_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Item', ((1, 'index'),(1, 'value'),)))
    IStringCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'retval'),)))
    IStringCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Count', ((1, 'retval'),)))
    IStringCollection.get_ReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_ReadOnly', ((1, 'retval'),)))
    IStringCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(12, 'Add', ((1, 'value'),(1, 'retval'),)))
    IStringCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Clear', ()))
    IStringCollection.Copy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(14, 'Copy', ((1, 'retval'),)))
    IStringCollection.Insert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR, use_last_error=False)(15, 'Insert', ((1, 'index'),(1, 'value'),)))
    IStringCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'RemoveAt', ((1, 'index'),)))
    win32more.System.Com.IDispatch
    return IStringCollection
def _define_IWebProxy_head():
    class IWebProxy(win32more.System.Com.IDispatch_head):
        Guid = Guid('174c81fe-aecd-4dae-b8a0-2c6318dd86a8')
    return IWebProxy
def _define_IWebProxy():
    IWebProxy = win32more.System.UpdateAgent.IWebProxy_head
    IWebProxy.get_Address = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Address', ((1, 'retval'),)))
    IWebProxy.put_Address = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Address', ((1, 'value'),)))
    IWebProxy.get_BypassList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(9, 'get_BypassList', ((1, 'retval'),)))
    IWebProxy.put_BypassList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IStringCollection_head, use_last_error=False)(10, 'put_BypassList', ((1, 'value'),)))
    IWebProxy.get_BypassProxyOnLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_BypassProxyOnLocal', ((1, 'retval'),)))
    IWebProxy.put_BypassProxyOnLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(12, 'put_BypassProxyOnLocal', ((1, 'value'),)))
    IWebProxy.get_ReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_ReadOnly', ((1, 'retval'),)))
    IWebProxy.get_UserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_UserName', ((1, 'retval'),)))
    IWebProxy.put_UserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_UserName', ((1, 'value'),)))
    IWebProxy.SetPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'SetPassword', ((1, 'value'),)))
    IWebProxy.PromptForCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BSTR, use_last_error=False)(17, 'PromptForCredentials', ((1, 'parentWindow'),(1, 'title'),)))
    IWebProxy.PromptForCredentialsFromHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.BSTR, use_last_error=False)(18, 'PromptForCredentialsFromHwnd', ((1, 'parentWindow'),(1, 'title'),)))
    IWebProxy.get_AutoDetect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(19, 'get_AutoDetect', ((1, 'retval'),)))
    IWebProxy.put_AutoDetect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(20, 'put_AutoDetect', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IWebProxy
def _define_ISystemInformation_head():
    class ISystemInformation(win32more.System.Com.IDispatch_head):
        Guid = Guid('ade87bf7-7b56-4275-8fab-b9b0e591844b')
    return ISystemInformation
def _define_ISystemInformation():
    ISystemInformation = win32more.System.UpdateAgent.ISystemInformation_head
    ISystemInformation.get_OemHardwareSupportLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_OemHardwareSupportLink', ((1, 'retval'),)))
    ISystemInformation.get_RebootRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_RebootRequired', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return ISystemInformation
def _define_IWindowsUpdateAgentInfo_head():
    class IWindowsUpdateAgentInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('85713fa1-7796-4fa2-be3b-e2d6124dd373')
    return IWindowsUpdateAgentInfo
def _define_IWindowsUpdateAgentInfo():
    IWindowsUpdateAgentInfo = win32more.System.UpdateAgent.IWindowsUpdateAgentInfo_head
    IWindowsUpdateAgentInfo.GetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'GetInfo', ((1, 'varInfoIdentifier'),(1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IWindowsUpdateAgentInfo
def _define_IAutomaticUpdatesResults_head():
    class IAutomaticUpdatesResults(win32more.System.Com.IDispatch_head):
        Guid = Guid('e7a4d634-7942-4dd9-a111-82228ba33901')
    return IAutomaticUpdatesResults
def _define_IAutomaticUpdatesResults():
    IAutomaticUpdatesResults = win32more.System.UpdateAgent.IAutomaticUpdatesResults_head
    IAutomaticUpdatesResults.get_LastSearchSuccessDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_LastSearchSuccessDate', ((1, 'retval'),)))
    IAutomaticUpdatesResults.get_LastInstallationSuccessDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_LastInstallationSuccessDate', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IAutomaticUpdatesResults
def _define_IAutomaticUpdatesSettings_head():
    class IAutomaticUpdatesSettings(win32more.System.Com.IDispatch_head):
        Guid = Guid('2ee48f22-af3c-405f-8970-f71be12ee9a2')
    return IAutomaticUpdatesSettings
def _define_IAutomaticUpdatesSettings():
    IAutomaticUpdatesSettings = win32more.System.UpdateAgent.IAutomaticUpdatesSettings_head
    IAutomaticUpdatesSettings.get_NotificationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.AutomaticUpdatesNotificationLevel), use_last_error=False)(7, 'get_NotificationLevel', ((1, 'retval'),)))
    IAutomaticUpdatesSettings.put_NotificationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.AutomaticUpdatesNotificationLevel, use_last_error=False)(8, 'put_NotificationLevel', ((1, 'value'),)))
    IAutomaticUpdatesSettings.get_ReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_ReadOnly', ((1, 'retval'),)))
    IAutomaticUpdatesSettings.get_Required = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_Required', ((1, 'retval'),)))
    IAutomaticUpdatesSettings.get_ScheduledInstallationDay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.AutomaticUpdatesScheduledInstallationDay), use_last_error=False)(11, 'get_ScheduledInstallationDay', ((1, 'retval'),)))
    IAutomaticUpdatesSettings.put_ScheduledInstallationDay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.AutomaticUpdatesScheduledInstallationDay, use_last_error=False)(12, 'put_ScheduledInstallationDay', ((1, 'value'),)))
    IAutomaticUpdatesSettings.get_ScheduledInstallationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_ScheduledInstallationTime', ((1, 'retval'),)))
    IAutomaticUpdatesSettings.put_ScheduledInstallationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_ScheduledInstallationTime', ((1, 'value'),)))
    IAutomaticUpdatesSettings.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'Refresh', ()))
    IAutomaticUpdatesSettings.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Save', ()))
    win32more.System.Com.IDispatch
    return IAutomaticUpdatesSettings
def _define_IAutomaticUpdatesSettings2_head():
    class IAutomaticUpdatesSettings2(win32more.System.UpdateAgent.IAutomaticUpdatesSettings_head):
        Guid = Guid('6abc136a-c3ca-4384-8171-cb2b1e59b8dc')
    return IAutomaticUpdatesSettings2
def _define_IAutomaticUpdatesSettings2():
    IAutomaticUpdatesSettings2 = win32more.System.UpdateAgent.IAutomaticUpdatesSettings2_head
    IAutomaticUpdatesSettings2.get_IncludeRecommendedUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_IncludeRecommendedUpdates', ((1, 'retval'),)))
    IAutomaticUpdatesSettings2.put_IncludeRecommendedUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(18, 'put_IncludeRecommendedUpdates', ((1, 'value'),)))
    IAutomaticUpdatesSettings2.CheckPermission = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.AutomaticUpdatesUserType,win32more.System.UpdateAgent.AutomaticUpdatesPermissionType,POINTER(Int16), use_last_error=False)(19, 'CheckPermission', ((1, 'userType'),(1, 'permissionType'),(1, 'userHasPermission'),)))
    win32more.System.UpdateAgent.IAutomaticUpdatesSettings
    return IAutomaticUpdatesSettings2
def _define_IAutomaticUpdatesSettings3_head():
    class IAutomaticUpdatesSettings3(win32more.System.UpdateAgent.IAutomaticUpdatesSettings2_head):
        Guid = Guid('b587f5c3-f57e-485f-bbf5-0d181c5cd0dc')
    return IAutomaticUpdatesSettings3
def _define_IAutomaticUpdatesSettings3():
    IAutomaticUpdatesSettings3 = win32more.System.UpdateAgent.IAutomaticUpdatesSettings3_head
    IAutomaticUpdatesSettings3.get_NonAdministratorsElevated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(20, 'get_NonAdministratorsElevated', ((1, 'retval'),)))
    IAutomaticUpdatesSettings3.put_NonAdministratorsElevated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(21, 'put_NonAdministratorsElevated', ((1, 'value'),)))
    IAutomaticUpdatesSettings3.get_FeaturedUpdatesEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(22, 'get_FeaturedUpdatesEnabled', ((1, 'retval'),)))
    IAutomaticUpdatesSettings3.put_FeaturedUpdatesEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(23, 'put_FeaturedUpdatesEnabled', ((1, 'value'),)))
    win32more.System.UpdateAgent.IAutomaticUpdatesSettings2
    return IAutomaticUpdatesSettings3
def _define_IAutomaticUpdates_head():
    class IAutomaticUpdates(win32more.System.Com.IDispatch_head):
        Guid = Guid('673425bf-c082-4c7c-bdfd-569464b8e0ce')
    return IAutomaticUpdates
def _define_IAutomaticUpdates():
    IAutomaticUpdates = win32more.System.UpdateAgent.IAutomaticUpdates_head
    IAutomaticUpdates.DetectNow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'DetectNow', ()))
    IAutomaticUpdates.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Pause', ()))
    IAutomaticUpdates.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Resume', ()))
    IAutomaticUpdates.ShowSettingsDialog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'ShowSettingsDialog', ()))
    IAutomaticUpdates.get_Settings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IAutomaticUpdatesSettings_head), use_last_error=False)(11, 'get_Settings', ((1, 'retval'),)))
    IAutomaticUpdates.get_ServiceEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_ServiceEnabled', ((1, 'retval'),)))
    IAutomaticUpdates.EnableService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'EnableService', ()))
    win32more.System.Com.IDispatch
    return IAutomaticUpdates
def _define_IAutomaticUpdates2_head():
    class IAutomaticUpdates2(win32more.System.UpdateAgent.IAutomaticUpdates_head):
        Guid = Guid('4a2f5c31-cfd9-410e-b7fb-29a653973a0f')
    return IAutomaticUpdates2
def _define_IAutomaticUpdates2():
    IAutomaticUpdates2 = win32more.System.UpdateAgent.IAutomaticUpdates2_head
    IAutomaticUpdates2.get_Results = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IAutomaticUpdatesResults_head), use_last_error=False)(14, 'get_Results', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IAutomaticUpdates
    return IAutomaticUpdates2
def _define_IUpdateIdentity_head():
    class IUpdateIdentity(win32more.System.Com.IDispatch_head):
        Guid = Guid('46297823-9940-4c09-aed9-cd3ea6d05968')
    return IUpdateIdentity
def _define_IUpdateIdentity():
    IUpdateIdentity = win32more.System.UpdateAgent.IUpdateIdentity_head
    IUpdateIdentity.get_RevisionNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_RevisionNumber', ((1, 'retval'),)))
    IUpdateIdentity.get_UpdateID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_UpdateID', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateIdentity
def _define_IImageInformation_head():
    class IImageInformation(win32more.System.Com.IDispatch_head):
        Guid = Guid('7c907864-346c-4aeb-8f3f-57da289f969f')
    return IImageInformation
def _define_IImageInformation():
    IImageInformation = win32more.System.UpdateAgent.IImageInformation_head
    IImageInformation.get_AltText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_AltText', ((1, 'retval'),)))
    IImageInformation.get_Height = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Height', ((1, 'retval'),)))
    IImageInformation.get_Source = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Source', ((1, 'retval'),)))
    IImageInformation.get_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Width', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IImageInformation
def _define_ICategory_head():
    class ICategory(win32more.System.Com.IDispatch_head):
        Guid = Guid('81ddc1b8-9d35-47a6-b471-5b80f519223b')
    return ICategory
def _define_ICategory():
    ICategory = win32more.System.UpdateAgent.ICategory_head
    ICategory.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'retval'),)))
    ICategory.get_CategoryID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_CategoryID', ((1, 'retval'),)))
    ICategory.get_Children = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.ICategoryCollection_head), use_last_error=False)(9, 'get_Children', ((1, 'retval'),)))
    ICategory.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Description', ((1, 'retval'),)))
    ICategory.get_Image = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IImageInformation_head), use_last_error=False)(11, 'get_Image', ((1, 'retval'),)))
    ICategory.get_Order = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_Order', ((1, 'retval'),)))
    ICategory.get_Parent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.ICategory_head), use_last_error=False)(13, 'get_Parent', ((1, 'retval'),)))
    ICategory.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_Type', ((1, 'retval'),)))
    ICategory.get_Updates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateCollection_head), use_last_error=False)(15, 'get_Updates', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return ICategory
def _define_ICategoryCollection_head():
    class ICategoryCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('3a56bfb8-576c-43f7-9335-fe4838fd7e37')
    return ICategoryCollection
def _define_ICategoryCollection():
    ICategoryCollection = win32more.System.UpdateAgent.ICategoryCollection_head
    ICategoryCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.UpdateAgent.ICategory_head), use_last_error=False)(7, 'get_Item', ((1, 'index'),(1, 'retval'),)))
    ICategoryCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'retval'),)))
    ICategoryCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return ICategoryCollection
def _define_IInstallationBehavior_head():
    class IInstallationBehavior(win32more.System.Com.IDispatch_head):
        Guid = Guid('d9a59339-e245-4dbd-9686-4d5763e39624')
    return IInstallationBehavior
def _define_IInstallationBehavior():
    IInstallationBehavior = win32more.System.UpdateAgent.IInstallationBehavior_head
    IInstallationBehavior.get_CanRequestUserInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_CanRequestUserInput', ((1, 'retval'),)))
    IInstallationBehavior.get_Impact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.InstallationImpact), use_last_error=False)(8, 'get_Impact', ((1, 'retval'),)))
    IInstallationBehavior.get_RebootBehavior = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.InstallationRebootBehavior), use_last_error=False)(9, 'get_RebootBehavior', ((1, 'retval'),)))
    IInstallationBehavior.get_RequiresNetworkConnectivity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_RequiresNetworkConnectivity', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IInstallationBehavior
def _define_IUpdateDownloadContent_head():
    class IUpdateDownloadContent(win32more.System.Com.IDispatch_head):
        Guid = Guid('54a2cb2d-9a0c-48b6-8a50-9abb69ee2d02')
    return IUpdateDownloadContent
def _define_IUpdateDownloadContent():
    IUpdateDownloadContent = win32more.System.UpdateAgent.IUpdateDownloadContent_head
    IUpdateDownloadContent.get_DownloadUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_DownloadUrl', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateDownloadContent
def _define_IUpdateDownloadContent2_head():
    class IUpdateDownloadContent2(win32more.System.UpdateAgent.IUpdateDownloadContent_head):
        Guid = Guid('c97ad11b-f257-420b-9d9f-377f733f6f68')
    return IUpdateDownloadContent2
def _define_IUpdateDownloadContent2():
    IUpdateDownloadContent2 = win32more.System.UpdateAgent.IUpdateDownloadContent2_head
    IUpdateDownloadContent2.get_IsDeltaCompressedContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_IsDeltaCompressedContent', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IUpdateDownloadContent
    return IUpdateDownloadContent2
def _define_IUpdateDownloadContentCollection_head():
    class IUpdateDownloadContentCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('bc5513c8-b3b8-4bf7-a4d4-361c0d8c88ba')
    return IUpdateDownloadContentCollection
def _define_IUpdateDownloadContentCollection():
    IUpdateDownloadContentCollection = win32more.System.UpdateAgent.IUpdateDownloadContentCollection_head
    IUpdateDownloadContentCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.UpdateAgent.IUpdateDownloadContent_head), use_last_error=False)(7, 'get_Item', ((1, 'index'),(1, 'retval'),)))
    IUpdateDownloadContentCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'retval'),)))
    IUpdateDownloadContentCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateDownloadContentCollection
def _define_IUpdate_head():
    class IUpdate(win32more.System.Com.IDispatch_head):
        Guid = Guid('6a92b07a-d821-4682-b423-5c805022cc4d')
    return IUpdate
def _define_IUpdate():
    IUpdate = win32more.System.UpdateAgent.IUpdate_head
    IUpdate.get_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Title', ((1, 'retval'),)))
    IUpdate.get_AutoSelectOnWebSites = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_AutoSelectOnWebSites', ((1, 'retval'),)))
    IUpdate.get_BundledUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateCollection_head), use_last_error=False)(9, 'get_BundledUpdates', ((1, 'retval'),)))
    IUpdate.get_CanRequireSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_CanRequireSource', ((1, 'retval'),)))
    IUpdate.get_Categories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.ICategoryCollection_head), use_last_error=False)(11, 'get_Categories', ((1, 'retval'),)))
    IUpdate.get_Deadline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(12, 'get_Deadline', ((1, 'retval'),)))
    IUpdate.get_DeltaCompressedContentAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_DeltaCompressedContentAvailable', ((1, 'retval'),)))
    IUpdate.get_DeltaCompressedContentPreferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(14, 'get_DeltaCompressedContentPreferred', ((1, 'retval'),)))
    IUpdate.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_Description', ((1, 'retval'),)))
    IUpdate.get_EulaAccepted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_EulaAccepted', ((1, 'retval'),)))
    IUpdate.get_EulaText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_EulaText', ((1, 'retval'),)))
    IUpdate.get_HandlerID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_HandlerID', ((1, 'retval'),)))
    IUpdate.get_Identity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateIdentity_head), use_last_error=False)(19, 'get_Identity', ((1, 'retval'),)))
    IUpdate.get_Image = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IImageInformation_head), use_last_error=False)(20, 'get_Image', ((1, 'retval'),)))
    IUpdate.get_InstallationBehavior = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IInstallationBehavior_head), use_last_error=False)(21, 'get_InstallationBehavior', ((1, 'retval'),)))
    IUpdate.get_IsBeta = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(22, 'get_IsBeta', ((1, 'retval'),)))
    IUpdate.get_IsDownloaded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(23, 'get_IsDownloaded', ((1, 'retval'),)))
    IUpdate.get_IsHidden = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(24, 'get_IsHidden', ((1, 'retval'),)))
    IUpdate.put_IsHidden = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(25, 'put_IsHidden', ((1, 'value'),)))
    IUpdate.get_IsInstalled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(26, 'get_IsInstalled', ((1, 'retval'),)))
    IUpdate.get_IsMandatory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(27, 'get_IsMandatory', ((1, 'retval'),)))
    IUpdate.get_IsUninstallable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(28, 'get_IsUninstallable', ((1, 'retval'),)))
    IUpdate.get_Languages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(29, 'get_Languages', ((1, 'retval'),)))
    IUpdate.get_LastDeploymentChangeTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(30, 'get_LastDeploymentChangeTime', ((1, 'retval'),)))
    IUpdate.get_MaxDownloadSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(31, 'get_MaxDownloadSize', ((1, 'retval'),)))
    IUpdate.get_MinDownloadSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(32, 'get_MinDownloadSize', ((1, 'retval'),)))
    IUpdate.get_MoreInfoUrls = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(33, 'get_MoreInfoUrls', ((1, 'retval'),)))
    IUpdate.get_MsrcSeverity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(34, 'get_MsrcSeverity', ((1, 'retval'),)))
    IUpdate.get_RecommendedCpuSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(35, 'get_RecommendedCpuSpeed', ((1, 'retval'),)))
    IUpdate.get_RecommendedHardDiskSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(36, 'get_RecommendedHardDiskSpace', ((1, 'retval'),)))
    IUpdate.get_RecommendedMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(37, 'get_RecommendedMemory', ((1, 'retval'),)))
    IUpdate.get_ReleaseNotes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(38, 'get_ReleaseNotes', ((1, 'retval'),)))
    IUpdate.get_SecurityBulletinIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(39, 'get_SecurityBulletinIDs', ((1, 'retval'),)))
    IUpdate.get_SupersededUpdateIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(40, 'get_SupersededUpdateIDs', ((1, 'retval'),)))
    IUpdate.get_SupportUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(41, 'get_SupportUrl', ((1, 'retval'),)))
    IUpdate.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.UpdateType), use_last_error=False)(42, 'get_Type', ((1, 'retval'),)))
    IUpdate.get_UninstallationNotes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(43, 'get_UninstallationNotes', ((1, 'retval'),)))
    IUpdate.get_UninstallationBehavior = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IInstallationBehavior_head), use_last_error=False)(44, 'get_UninstallationBehavior', ((1, 'retval'),)))
    IUpdate.get_UninstallationSteps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(45, 'get_UninstallationSteps', ((1, 'retval'),)))
    IUpdate.get_KBArticleIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(46, 'get_KBArticleIDs', ((1, 'retval'),)))
    IUpdate.AcceptEula = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(47, 'AcceptEula', ()))
    IUpdate.get_DeploymentAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.DeploymentAction), use_last_error=False)(48, 'get_DeploymentAction', ((1, 'retval'),)))
    IUpdate.CopyFromCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16, use_last_error=False)(49, 'CopyFromCache', ((1, 'path'),(1, 'toExtractCabFiles'),)))
    IUpdate.get_DownloadPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.DownloadPriority), use_last_error=False)(50, 'get_DownloadPriority', ((1, 'retval'),)))
    IUpdate.get_DownloadContents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateDownloadContentCollection_head), use_last_error=False)(51, 'get_DownloadContents', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdate
def _define_IWindowsDriverUpdate_head():
    class IWindowsDriverUpdate(win32more.System.UpdateAgent.IUpdate_head):
        Guid = Guid('b383cd1a-5ce9-4504-9f63-764b1236f191')
    return IWindowsDriverUpdate
def _define_IWindowsDriverUpdate():
    IWindowsDriverUpdate = win32more.System.UpdateAgent.IWindowsDriverUpdate_head
    IWindowsDriverUpdate.get_DriverClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(52, 'get_DriverClass', ((1, 'retval'),)))
    IWindowsDriverUpdate.get_DriverHardwareID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(53, 'get_DriverHardwareID', ((1, 'retval'),)))
    IWindowsDriverUpdate.get_DriverManufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(54, 'get_DriverManufacturer', ((1, 'retval'),)))
    IWindowsDriverUpdate.get_DriverModel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(55, 'get_DriverModel', ((1, 'retval'),)))
    IWindowsDriverUpdate.get_DriverProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(56, 'get_DriverProvider', ((1, 'retval'),)))
    IWindowsDriverUpdate.get_DriverVerDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(57, 'get_DriverVerDate', ((1, 'retval'),)))
    IWindowsDriverUpdate.get_DeviceProblemNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(58, 'get_DeviceProblemNumber', ((1, 'retval'),)))
    IWindowsDriverUpdate.get_DeviceStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(59, 'get_DeviceStatus', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IUpdate
    return IWindowsDriverUpdate
def _define_IUpdate2_head():
    class IUpdate2(win32more.System.UpdateAgent.IUpdate_head):
        Guid = Guid('144fe9b0-d23d-4a8b-8634-fb4457533b7a')
    return IUpdate2
def _define_IUpdate2():
    IUpdate2 = win32more.System.UpdateAgent.IUpdate2_head
    IUpdate2.get_RebootRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(52, 'get_RebootRequired', ((1, 'retval'),)))
    IUpdate2.get_IsPresent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(53, 'get_IsPresent', ((1, 'retval'),)))
    IUpdate2.get_CveIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(54, 'get_CveIDs', ((1, 'retval'),)))
    IUpdate2.CopyToCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IStringCollection_head, use_last_error=False)(55, 'CopyToCache', ((1, 'pFiles'),)))
    win32more.System.UpdateAgent.IUpdate
    return IUpdate2
def _define_IUpdate3_head():
    class IUpdate3(win32more.System.UpdateAgent.IUpdate2_head):
        Guid = Guid('112eda6b-95b3-476f-9d90-aee82c6b8181')
    return IUpdate3
def _define_IUpdate3():
    IUpdate3 = win32more.System.UpdateAgent.IUpdate3_head
    IUpdate3.get_BrowseOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(56, 'get_BrowseOnly', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IUpdate2
    return IUpdate3
def _define_IUpdate4_head():
    class IUpdate4(win32more.System.UpdateAgent.IUpdate3_head):
        Guid = Guid('27e94b0d-5139-49a2-9a61-93522dc54652')
    return IUpdate4
def _define_IUpdate4():
    IUpdate4 = win32more.System.UpdateAgent.IUpdate4_head
    IUpdate4.get_PerUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(57, 'get_PerUser', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IUpdate3
    return IUpdate4
def _define_IUpdate5_head():
    class IUpdate5(win32more.System.UpdateAgent.IUpdate4_head):
        Guid = Guid('c1c2f21a-d2f4-4902-b5c6-8a081c19a890')
    return IUpdate5
def _define_IUpdate5():
    IUpdate5 = win32more.System.UpdateAgent.IUpdate5_head
    IUpdate5.get_AutoSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.AutoSelectionMode), use_last_error=False)(58, 'get_AutoSelection', ((1, 'retval'),)))
    IUpdate5.get_AutoDownload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.AutoDownloadMode), use_last_error=False)(59, 'get_AutoDownload', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IUpdate4
    return IUpdate5
def _define_IWindowsDriverUpdate2_head():
    class IWindowsDriverUpdate2(win32more.System.UpdateAgent.IWindowsDriverUpdate_head):
        Guid = Guid('615c4269-7a48-43bd-96b7-bf6ca27d6c3e')
    return IWindowsDriverUpdate2
def _define_IWindowsDriverUpdate2():
    IWindowsDriverUpdate2 = win32more.System.UpdateAgent.IWindowsDriverUpdate2_head
    IWindowsDriverUpdate2.get_RebootRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(60, 'get_RebootRequired', ((1, 'retval'),)))
    IWindowsDriverUpdate2.get_IsPresent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(61, 'get_IsPresent', ((1, 'retval'),)))
    IWindowsDriverUpdate2.get_CveIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(62, 'get_CveIDs', ((1, 'retval'),)))
    IWindowsDriverUpdate2.CopyToCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IStringCollection_head, use_last_error=False)(63, 'CopyToCache', ((1, 'pFiles'),)))
    win32more.System.UpdateAgent.IWindowsDriverUpdate
    return IWindowsDriverUpdate2
def _define_IWindowsDriverUpdate3_head():
    class IWindowsDriverUpdate3(win32more.System.UpdateAgent.IWindowsDriverUpdate2_head):
        Guid = Guid('49ebd502-4a96-41bd-9e3e-4c5057f4250c')
    return IWindowsDriverUpdate3
def _define_IWindowsDriverUpdate3():
    IWindowsDriverUpdate3 = win32more.System.UpdateAgent.IWindowsDriverUpdate3_head
    IWindowsDriverUpdate3.get_BrowseOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(64, 'get_BrowseOnly', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IWindowsDriverUpdate2
    return IWindowsDriverUpdate3
def _define_IWindowsDriverUpdateEntry_head():
    class IWindowsDriverUpdateEntry(win32more.System.Com.IDispatch_head):
        Guid = Guid('ed8bfe40-a60b-42ea-9652-817dfcfa23ec')
    return IWindowsDriverUpdateEntry
def _define_IWindowsDriverUpdateEntry():
    IWindowsDriverUpdateEntry = win32more.System.UpdateAgent.IWindowsDriverUpdateEntry_head
    IWindowsDriverUpdateEntry.get_DriverClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_DriverClass', ((1, 'retval'),)))
    IWindowsDriverUpdateEntry.get_DriverHardwareID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_DriverHardwareID', ((1, 'retval'),)))
    IWindowsDriverUpdateEntry.get_DriverManufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_DriverManufacturer', ((1, 'retval'),)))
    IWindowsDriverUpdateEntry.get_DriverModel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_DriverModel', ((1, 'retval'),)))
    IWindowsDriverUpdateEntry.get_DriverProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_DriverProvider', ((1, 'retval'),)))
    IWindowsDriverUpdateEntry.get_DriverVerDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(12, 'get_DriverVerDate', ((1, 'retval'),)))
    IWindowsDriverUpdateEntry.get_DeviceProblemNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_DeviceProblemNumber', ((1, 'retval'),)))
    IWindowsDriverUpdateEntry.get_DeviceStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'get_DeviceStatus', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IWindowsDriverUpdateEntry
def _define_IWindowsDriverUpdateEntryCollection_head():
    class IWindowsDriverUpdateEntryCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('0d521700-a372-4bef-828b-3d00c10adebd')
    return IWindowsDriverUpdateEntryCollection
def _define_IWindowsDriverUpdateEntryCollection():
    IWindowsDriverUpdateEntryCollection = win32more.System.UpdateAgent.IWindowsDriverUpdateEntryCollection_head
    IWindowsDriverUpdateEntryCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.UpdateAgent.IWindowsDriverUpdateEntry_head), use_last_error=False)(7, 'get_Item', ((1, 'index'),(1, 'retval'),)))
    IWindowsDriverUpdateEntryCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'retval'),)))
    IWindowsDriverUpdateEntryCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IWindowsDriverUpdateEntryCollection
def _define_IWindowsDriverUpdate4_head():
    class IWindowsDriverUpdate4(win32more.System.UpdateAgent.IWindowsDriverUpdate3_head):
        Guid = Guid('004c6a2b-0c19-4c69-9f5c-a269b2560db9')
    return IWindowsDriverUpdate4
def _define_IWindowsDriverUpdate4():
    IWindowsDriverUpdate4 = win32more.System.UpdateAgent.IWindowsDriverUpdate4_head
    IWindowsDriverUpdate4.get_WindowsDriverUpdateEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IWindowsDriverUpdateEntryCollection_head), use_last_error=False)(65, 'get_WindowsDriverUpdateEntries', ((1, 'retval'),)))
    IWindowsDriverUpdate4.get_PerUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(66, 'get_PerUser', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IWindowsDriverUpdate3
    return IWindowsDriverUpdate4
def _define_IWindowsDriverUpdate5_head():
    class IWindowsDriverUpdate5(win32more.System.UpdateAgent.IWindowsDriverUpdate4_head):
        Guid = Guid('70cf5c82-8642-42bb-9dbc-0cfd263c6c4f')
    return IWindowsDriverUpdate5
def _define_IWindowsDriverUpdate5():
    IWindowsDriverUpdate5 = win32more.System.UpdateAgent.IWindowsDriverUpdate5_head
    IWindowsDriverUpdate5.get_AutoSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.AutoSelectionMode), use_last_error=False)(67, 'get_AutoSelection', ((1, 'retval'),)))
    IWindowsDriverUpdate5.get_AutoDownload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.AutoDownloadMode), use_last_error=False)(68, 'get_AutoDownload', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IWindowsDriverUpdate4
    return IWindowsDriverUpdate5
def _define_IUpdateCollection_head():
    class IUpdateCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('07f7438c-7709-4ca5-b518-91279288134e')
    return IUpdateCollection
def _define_IUpdateCollection():
    IUpdateCollection = win32more.System.UpdateAgent.IUpdateCollection_head
    IUpdateCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.UpdateAgent.IUpdate_head), use_last_error=False)(7, 'get_Item', ((1, 'index'),(1, 'retval'),)))
    IUpdateCollection.put_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.UpdateAgent.IUpdate_head, use_last_error=False)(8, 'put_Item', ((1, 'index'),(1, 'value'),)))
    IUpdateCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'retval'),)))
    IUpdateCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Count', ((1, 'retval'),)))
    IUpdateCollection.get_ReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_ReadOnly', ((1, 'retval'),)))
    IUpdateCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IUpdate_head,POINTER(Int32), use_last_error=False)(12, 'Add', ((1, 'value'),(1, 'retval'),)))
    IUpdateCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Clear', ()))
    IUpdateCollection.Copy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateCollection_head), use_last_error=False)(14, 'Copy', ((1, 'retval'),)))
    IUpdateCollection.Insert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.UpdateAgent.IUpdate_head, use_last_error=False)(15, 'Insert', ((1, 'index'),(1, 'value'),)))
    IUpdateCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'RemoveAt', ((1, 'index'),)))
    win32more.System.Com.IDispatch
    return IUpdateCollection
def _define_IUpdateException_head():
    class IUpdateException(win32more.System.Com.IDispatch_head):
        Guid = Guid('a376dd5e-09d4-427f-af7c-fed5b6e1c1d6')
    return IUpdateException
def _define_IUpdateException():
    IUpdateException = win32more.System.UpdateAgent.IUpdateException_head
    IUpdateException.get_Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Message', ((1, 'retval'),)))
    IUpdateException.get_HResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_HResult', ((1, 'retval'),)))
    IUpdateException.get_Context = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.UpdateExceptionContext), use_last_error=False)(9, 'get_Context', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateException
def _define_IInvalidProductLicenseException_head():
    class IInvalidProductLicenseException(win32more.System.UpdateAgent.IUpdateException_head):
        Guid = Guid('a37d00f5-7bb0-4953-b414-f9e98326f2e8')
    return IInvalidProductLicenseException
def _define_IInvalidProductLicenseException():
    IInvalidProductLicenseException = win32more.System.UpdateAgent.IInvalidProductLicenseException_head
    IInvalidProductLicenseException.get_Product = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Product', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IUpdateException
    return IInvalidProductLicenseException
def _define_IUpdateExceptionCollection_head():
    class IUpdateExceptionCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('503626a3-8e14-4729-9355-0fe664bd2321')
    return IUpdateExceptionCollection
def _define_IUpdateExceptionCollection():
    IUpdateExceptionCollection = win32more.System.UpdateAgent.IUpdateExceptionCollection_head
    IUpdateExceptionCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.UpdateAgent.IUpdateException_head), use_last_error=False)(7, 'get_Item', ((1, 'index'),(1, 'retval'),)))
    IUpdateExceptionCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'retval'),)))
    IUpdateExceptionCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateExceptionCollection
def _define_ISearchResult_head():
    class ISearchResult(win32more.System.Com.IDispatch_head):
        Guid = Guid('d40cff62-e08c-4498-941a-01e25f0fd33c')
    return ISearchResult
def _define_ISearchResult():
    ISearchResult = win32more.System.UpdateAgent.ISearchResult_head
    ISearchResult.get_ResultCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.OperationResultCode), use_last_error=False)(7, 'get_ResultCode', ((1, 'retval'),)))
    ISearchResult.get_RootCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.ICategoryCollection_head), use_last_error=False)(8, 'get_RootCategories', ((1, 'retval'),)))
    ISearchResult.get_Updates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateCollection_head), use_last_error=False)(9, 'get_Updates', ((1, 'retval'),)))
    ISearchResult.get_Warnings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateExceptionCollection_head), use_last_error=False)(10, 'get_Warnings', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return ISearchResult
def _define_ISearchJob_head():
    class ISearchJob(win32more.System.Com.IDispatch_head):
        Guid = Guid('7366ea16-7a1a-4ea2-b042-973d3e9cd99b')
    return ISearchJob
def _define_ISearchJob():
    ISearchJob = win32more.System.UpdateAgent.ISearchJob_head
    ISearchJob.get_AsyncState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_AsyncState', ((1, 'retval'),)))
    ISearchJob.get_IsCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_IsCompleted', ((1, 'retval'),)))
    ISearchJob.CleanUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'CleanUp', ()))
    ISearchJob.RequestAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'RequestAbort', ()))
    win32more.System.Com.IDispatch
    return ISearchJob
def _define_ISearchCompletedCallbackArgs_head():
    class ISearchCompletedCallbackArgs(win32more.System.Com.IDispatch_head):
        Guid = Guid('a700a634-2850-4c47-938a-9e4b6e5af9a6')
    return ISearchCompletedCallbackArgs
def _define_ISearchCompletedCallbackArgs():
    ISearchCompletedCallbackArgs = win32more.System.UpdateAgent.ISearchCompletedCallbackArgs_head
    win32more.System.Com.IDispatch
    return ISearchCompletedCallbackArgs
def _define_ISearchCompletedCallback_head():
    class ISearchCompletedCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('88aee058-d4b0-4725-a2f1-814a67ae964c')
    return ISearchCompletedCallback
def _define_ISearchCompletedCallback():
    ISearchCompletedCallback = win32more.System.UpdateAgent.ISearchCompletedCallback_head
    ISearchCompletedCallback.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.ISearchJob_head,win32more.System.UpdateAgent.ISearchCompletedCallbackArgs_head, use_last_error=False)(3, 'Invoke', ((1, 'searchJob'),(1, 'callbackArgs'),)))
    win32more.System.Com.IUnknown
    return ISearchCompletedCallback
def _define_IUpdateHistoryEntry_head():
    class IUpdateHistoryEntry(win32more.System.Com.IDispatch_head):
        Guid = Guid('be56a644-af0e-4e0e-a311-c1d8e695cbff')
    return IUpdateHistoryEntry
def _define_IUpdateHistoryEntry():
    IUpdateHistoryEntry = win32more.System.UpdateAgent.IUpdateHistoryEntry_head
    IUpdateHistoryEntry.get_Operation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.UpdateOperation), use_last_error=False)(7, 'get_Operation', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_ResultCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.OperationResultCode), use_last_error=False)(8, 'get_ResultCode', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_HResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_HResult', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_Date = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(10, 'get_Date', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_UpdateIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateIdentity_head), use_last_error=False)(11, 'get_UpdateIdentity', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_Title', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_Description', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_UnmappedResultCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'get_UnmappedResultCode', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_ClientApplicationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_ClientApplicationID', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_ServerSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.ServerSelection), use_last_error=False)(16, 'get_ServerSelection', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_ServiceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_ServiceID', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_UninstallationSteps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(18, 'get_UninstallationSteps', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_UninstallationNotes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_UninstallationNotes', ((1, 'retval'),)))
    IUpdateHistoryEntry.get_SupportUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_SupportUrl', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateHistoryEntry
def _define_IUpdateHistoryEntry2_head():
    class IUpdateHistoryEntry2(win32more.System.UpdateAgent.IUpdateHistoryEntry_head):
        Guid = Guid('c2bfb780-4539-4132-ab8c-0a8772013ab6')
    return IUpdateHistoryEntry2
def _define_IUpdateHistoryEntry2():
    IUpdateHistoryEntry2 = win32more.System.UpdateAgent.IUpdateHistoryEntry2_head
    IUpdateHistoryEntry2.get_Categories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.ICategoryCollection_head), use_last_error=False)(21, 'get_Categories', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IUpdateHistoryEntry
    return IUpdateHistoryEntry2
def _define_IUpdateHistoryEntryCollection_head():
    class IUpdateHistoryEntryCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('a7f04f3c-a290-435b-aadf-a116c3357a5c')
    return IUpdateHistoryEntryCollection
def _define_IUpdateHistoryEntryCollection():
    IUpdateHistoryEntryCollection = win32more.System.UpdateAgent.IUpdateHistoryEntryCollection_head
    IUpdateHistoryEntryCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.UpdateAgent.IUpdateHistoryEntry_head), use_last_error=False)(7, 'get_Item', ((1, 'index'),(1, 'retval'),)))
    IUpdateHistoryEntryCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'retval'),)))
    IUpdateHistoryEntryCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateHistoryEntryCollection
def _define_IUpdateSearcher_head():
    class IUpdateSearcher(win32more.System.Com.IDispatch_head):
        Guid = Guid('8f45abf1-f9ae-4b95-a933-f0f66e5056ea')
    return IUpdateSearcher
def _define_IUpdateSearcher():
    IUpdateSearcher = win32more.System.UpdateAgent.IUpdateSearcher_head
    IUpdateSearcher.get_CanAutomaticallyUpgradeService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_CanAutomaticallyUpgradeService', ((1, 'retval'),)))
    IUpdateSearcher.put_CanAutomaticallyUpgradeService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(8, 'put_CanAutomaticallyUpgradeService', ((1, 'value'),)))
    IUpdateSearcher.get_ClientApplicationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ClientApplicationID', ((1, 'retval'),)))
    IUpdateSearcher.put_ClientApplicationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_ClientApplicationID', ((1, 'value'),)))
    IUpdateSearcher.get_IncludePotentiallySupersededUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_IncludePotentiallySupersededUpdates', ((1, 'retval'),)))
    IUpdateSearcher.put_IncludePotentiallySupersededUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(12, 'put_IncludePotentiallySupersededUpdates', ((1, 'value'),)))
    IUpdateSearcher.get_ServerSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.ServerSelection), use_last_error=False)(13, 'get_ServerSelection', ((1, 'retval'),)))
    IUpdateSearcher.put_ServerSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.ServerSelection, use_last_error=False)(14, 'put_ServerSelection', ((1, 'value'),)))
    IUpdateSearcher.BeginSearch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IUnknown_head,win32more.System.Com.VARIANT,POINTER(win32more.System.UpdateAgent.ISearchJob_head), use_last_error=False)(15, 'BeginSearch', ((1, 'criteria'),(1, 'onCompleted'),(1, 'state'),(1, 'retval'),)))
    IUpdateSearcher.EndSearch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.ISearchJob_head,POINTER(win32more.System.UpdateAgent.ISearchResult_head), use_last_error=False)(16, 'EndSearch', ((1, 'searchJob'),(1, 'retval'),)))
    IUpdateSearcher.EscapeString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'EscapeString', ((1, 'unescaped'),(1, 'retval'),)))
    IUpdateSearcher.QueryHistory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.UpdateAgent.IUpdateHistoryEntryCollection_head), use_last_error=False)(18, 'QueryHistory', ((1, 'startIndex'),(1, 'count'),(1, 'retval'),)))
    IUpdateSearcher.Search = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.UpdateAgent.ISearchResult_head), use_last_error=False)(19, 'Search', ((1, 'criteria'),(1, 'retval'),)))
    IUpdateSearcher.get_Online = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(20, 'get_Online', ((1, 'retval'),)))
    IUpdateSearcher.put_Online = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(21, 'put_Online', ((1, 'value'),)))
    IUpdateSearcher.GetTotalHistoryCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(22, 'GetTotalHistoryCount', ((1, 'retval'),)))
    IUpdateSearcher.get_ServiceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_ServiceID', ((1, 'retval'),)))
    IUpdateSearcher.put_ServiceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(24, 'put_ServiceID', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IUpdateSearcher
def _define_IUpdateSearcher2_head():
    class IUpdateSearcher2(win32more.System.UpdateAgent.IUpdateSearcher_head):
        Guid = Guid('4cbdcb2d-1589-4beb-bd1c-3e582ff0add0')
    return IUpdateSearcher2
def _define_IUpdateSearcher2():
    IUpdateSearcher2 = win32more.System.UpdateAgent.IUpdateSearcher2_head
    IUpdateSearcher2.get_IgnoreDownloadPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(25, 'get_IgnoreDownloadPriority', ((1, 'retval'),)))
    IUpdateSearcher2.put_IgnoreDownloadPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(26, 'put_IgnoreDownloadPriority', ((1, 'value'),)))
    win32more.System.UpdateAgent.IUpdateSearcher
    return IUpdateSearcher2
def _define_IUpdateSearcher3_head():
    class IUpdateSearcher3(win32more.System.UpdateAgent.IUpdateSearcher2_head):
        Guid = Guid('04c6895d-eaf2-4034-97f3-311de9be413a')
    return IUpdateSearcher3
def _define_IUpdateSearcher3():
    IUpdateSearcher3 = win32more.System.UpdateAgent.IUpdateSearcher3_head
    IUpdateSearcher3.get_SearchScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.SearchScope), use_last_error=False)(27, 'get_SearchScope', ((1, 'retval'),)))
    IUpdateSearcher3.put_SearchScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.SearchScope, use_last_error=False)(28, 'put_SearchScope', ((1, 'value'),)))
    win32more.System.UpdateAgent.IUpdateSearcher2
    return IUpdateSearcher3
def _define_IUpdateDownloadResult_head():
    class IUpdateDownloadResult(win32more.System.Com.IDispatch_head):
        Guid = Guid('bf99af76-b575-42ad-8aa4-33cbb5477af1')
    return IUpdateDownloadResult
def _define_IUpdateDownloadResult():
    IUpdateDownloadResult = win32more.System.UpdateAgent.IUpdateDownloadResult_head
    IUpdateDownloadResult.get_HResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_HResult', ((1, 'retval'),)))
    IUpdateDownloadResult.get_ResultCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.OperationResultCode), use_last_error=False)(8, 'get_ResultCode', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateDownloadResult
def _define_IDownloadResult_head():
    class IDownloadResult(win32more.System.Com.IDispatch_head):
        Guid = Guid('daa4fdd0-4727-4dbe-a1e7-745dca317144')
    return IDownloadResult
def _define_IDownloadResult():
    IDownloadResult = win32more.System.UpdateAgent.IDownloadResult_head
    IDownloadResult.get_HResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_HResult', ((1, 'retval'),)))
    IDownloadResult.get_ResultCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.OperationResultCode), use_last_error=False)(8, 'get_ResultCode', ((1, 'retval'),)))
    IDownloadResult.GetUpdateResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.UpdateAgent.IUpdateDownloadResult_head), use_last_error=False)(9, 'GetUpdateResult', ((1, 'updateIndex'),(1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IDownloadResult
def _define_IDownloadProgress_head():
    class IDownloadProgress(win32more.System.Com.IDispatch_head):
        Guid = Guid('d31a5bac-f719-4178-9dbb-5e2cb47fd18a')
    return IDownloadProgress
def _define_IDownloadProgress():
    IDownloadProgress = win32more.System.UpdateAgent.IDownloadProgress_head
    IDownloadProgress.get_CurrentUpdateBytesDownloaded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(7, 'get_CurrentUpdateBytesDownloaded', ((1, 'retval'),)))
    IDownloadProgress.get_CurrentUpdateBytesToDownload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(8, 'get_CurrentUpdateBytesToDownload', ((1, 'retval'),)))
    IDownloadProgress.get_CurrentUpdateIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_CurrentUpdateIndex', ((1, 'retval'),)))
    IDownloadProgress.get_PercentComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_PercentComplete', ((1, 'retval'),)))
    IDownloadProgress.get_TotalBytesDownloaded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(11, 'get_TotalBytesDownloaded', ((1, 'retval'),)))
    IDownloadProgress.get_TotalBytesToDownload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(12, 'get_TotalBytesToDownload', ((1, 'retval'),)))
    IDownloadProgress.GetUpdateResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.UpdateAgent.IUpdateDownloadResult_head), use_last_error=False)(13, 'GetUpdateResult', ((1, 'updateIndex'),(1, 'retval'),)))
    IDownloadProgress.get_CurrentUpdateDownloadPhase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.DownloadPhase), use_last_error=False)(14, 'get_CurrentUpdateDownloadPhase', ((1, 'retval'),)))
    IDownloadProgress.get_CurrentUpdatePercentComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_CurrentUpdatePercentComplete', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IDownloadProgress
def _define_IDownloadJob_head():
    class IDownloadJob(win32more.System.Com.IDispatch_head):
        Guid = Guid('c574de85-7358-43f6-aae8-8697e62d8ba7')
    return IDownloadJob
def _define_IDownloadJob():
    IDownloadJob = win32more.System.UpdateAgent.IDownloadJob_head
    IDownloadJob.get_AsyncState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_AsyncState', ((1, 'retval'),)))
    IDownloadJob.get_IsCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_IsCompleted', ((1, 'retval'),)))
    IDownloadJob.get_Updates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateCollection_head), use_last_error=False)(9, 'get_Updates', ((1, 'retval'),)))
    IDownloadJob.CleanUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'CleanUp', ()))
    IDownloadJob.GetProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IDownloadProgress_head), use_last_error=False)(11, 'GetProgress', ((1, 'retval'),)))
    IDownloadJob.RequestAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'RequestAbort', ()))
    win32more.System.Com.IDispatch
    return IDownloadJob
def _define_IDownloadCompletedCallbackArgs_head():
    class IDownloadCompletedCallbackArgs(win32more.System.Com.IDispatch_head):
        Guid = Guid('fa565b23-498c-47a0-979d-e7d5b1813360')
    return IDownloadCompletedCallbackArgs
def _define_IDownloadCompletedCallbackArgs():
    IDownloadCompletedCallbackArgs = win32more.System.UpdateAgent.IDownloadCompletedCallbackArgs_head
    win32more.System.Com.IDispatch
    return IDownloadCompletedCallbackArgs
def _define_IDownloadCompletedCallback_head():
    class IDownloadCompletedCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('77254866-9f5b-4c8e-b9e2-c77a8530d64b')
    return IDownloadCompletedCallback
def _define_IDownloadCompletedCallback():
    IDownloadCompletedCallback = win32more.System.UpdateAgent.IDownloadCompletedCallback_head
    IDownloadCompletedCallback.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IDownloadJob_head,win32more.System.UpdateAgent.IDownloadCompletedCallbackArgs_head, use_last_error=False)(3, 'Invoke', ((1, 'downloadJob'),(1, 'callbackArgs'),)))
    win32more.System.Com.IUnknown
    return IDownloadCompletedCallback
def _define_IDownloadProgressChangedCallbackArgs_head():
    class IDownloadProgressChangedCallbackArgs(win32more.System.Com.IDispatch_head):
        Guid = Guid('324ff2c6-4981-4b04-9412-57481745ab24')
    return IDownloadProgressChangedCallbackArgs
def _define_IDownloadProgressChangedCallbackArgs():
    IDownloadProgressChangedCallbackArgs = win32more.System.UpdateAgent.IDownloadProgressChangedCallbackArgs_head
    IDownloadProgressChangedCallbackArgs.get_Progress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IDownloadProgress_head), use_last_error=False)(7, 'get_Progress', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IDownloadProgressChangedCallbackArgs
def _define_IDownloadProgressChangedCallback_head():
    class IDownloadProgressChangedCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('8c3f1cdd-6173-4591-aebd-a56a53ca77c1')
    return IDownloadProgressChangedCallback
def _define_IDownloadProgressChangedCallback():
    IDownloadProgressChangedCallback = win32more.System.UpdateAgent.IDownloadProgressChangedCallback_head
    IDownloadProgressChangedCallback.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IDownloadJob_head,win32more.System.UpdateAgent.IDownloadProgressChangedCallbackArgs_head, use_last_error=False)(3, 'Invoke', ((1, 'downloadJob'),(1, 'callbackArgs'),)))
    win32more.System.Com.IUnknown
    return IDownloadProgressChangedCallback
def _define_IUpdateDownloader_head():
    class IUpdateDownloader(win32more.System.Com.IDispatch_head):
        Guid = Guid('68f1c6f9-7ecc-4666-a464-247fe12496c3')
    return IUpdateDownloader
def _define_IUpdateDownloader():
    IUpdateDownloader = win32more.System.UpdateAgent.IUpdateDownloader_head
    IUpdateDownloader.get_ClientApplicationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ClientApplicationID', ((1, 'retval'),)))
    IUpdateDownloader.put_ClientApplicationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_ClientApplicationID', ((1, 'value'),)))
    IUpdateDownloader.get_IsForced = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_IsForced', ((1, 'retval'),)))
    IUpdateDownloader.put_IsForced = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(10, 'put_IsForced', ((1, 'value'),)))
    IUpdateDownloader.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.DownloadPriority), use_last_error=False)(11, 'get_Priority', ((1, 'retval'),)))
    IUpdateDownloader.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.DownloadPriority, use_last_error=False)(12, 'put_Priority', ((1, 'value'),)))
    IUpdateDownloader.get_Updates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateCollection_head), use_last_error=False)(13, 'get_Updates', ((1, 'retval'),)))
    IUpdateDownloader.put_Updates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IUpdateCollection_head, use_last_error=False)(14, 'put_Updates', ((1, 'value'),)))
    IUpdateDownloader.BeginDownload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,win32more.System.Com.VARIANT,POINTER(win32more.System.UpdateAgent.IDownloadJob_head), use_last_error=False)(15, 'BeginDownload', ((1, 'onProgressChanged'),(1, 'onCompleted'),(1, 'state'),(1, 'retval'),)))
    IUpdateDownloader.Download = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IDownloadResult_head), use_last_error=False)(16, 'Download', ((1, 'retval'),)))
    IUpdateDownloader.EndDownload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IDownloadJob_head,POINTER(win32more.System.UpdateAgent.IDownloadResult_head), use_last_error=False)(17, 'EndDownload', ((1, 'value'),(1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateDownloader
def _define_IUpdateInstallationResult_head():
    class IUpdateInstallationResult(win32more.System.Com.IDispatch_head):
        Guid = Guid('d940f0f8-3cbb-4fd0-993f-471e7f2328ad')
    return IUpdateInstallationResult
def _define_IUpdateInstallationResult():
    IUpdateInstallationResult = win32more.System.UpdateAgent.IUpdateInstallationResult_head
    IUpdateInstallationResult.get_HResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_HResult', ((1, 'retval'),)))
    IUpdateInstallationResult.get_RebootRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_RebootRequired', ((1, 'retval'),)))
    IUpdateInstallationResult.get_ResultCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.OperationResultCode), use_last_error=False)(9, 'get_ResultCode', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateInstallationResult
def _define_IInstallationResult_head():
    class IInstallationResult(win32more.System.Com.IDispatch_head):
        Guid = Guid('a43c56d6-7451-48d4-af96-b6cd2d0d9b7a')
    return IInstallationResult
def _define_IInstallationResult():
    IInstallationResult = win32more.System.UpdateAgent.IInstallationResult_head
    IInstallationResult.get_HResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_HResult', ((1, 'retval'),)))
    IInstallationResult.get_RebootRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_RebootRequired', ((1, 'retval'),)))
    IInstallationResult.get_ResultCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.OperationResultCode), use_last_error=False)(9, 'get_ResultCode', ((1, 'retval'),)))
    IInstallationResult.GetUpdateResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.UpdateAgent.IUpdateInstallationResult_head), use_last_error=False)(10, 'GetUpdateResult', ((1, 'updateIndex'),(1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IInstallationResult
def _define_IInstallationProgress_head():
    class IInstallationProgress(win32more.System.Com.IDispatch_head):
        Guid = Guid('345c8244-43a3-4e32-a368-65f073b76f36')
    return IInstallationProgress
def _define_IInstallationProgress():
    IInstallationProgress = win32more.System.UpdateAgent.IInstallationProgress_head
    IInstallationProgress.get_CurrentUpdateIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_CurrentUpdateIndex', ((1, 'retval'),)))
    IInstallationProgress.get_CurrentUpdatePercentComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_CurrentUpdatePercentComplete', ((1, 'retval'),)))
    IInstallationProgress.get_PercentComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_PercentComplete', ((1, 'retval'),)))
    IInstallationProgress.GetUpdateResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.UpdateAgent.IUpdateInstallationResult_head), use_last_error=False)(10, 'GetUpdateResult', ((1, 'updateIndex'),(1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IInstallationProgress
def _define_IInstallationJob_head():
    class IInstallationJob(win32more.System.Com.IDispatch_head):
        Guid = Guid('5c209f0b-bad5-432a-9556-4699bed2638a')
    return IInstallationJob
def _define_IInstallationJob():
    IInstallationJob = win32more.System.UpdateAgent.IInstallationJob_head
    IInstallationJob.get_AsyncState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_AsyncState', ((1, 'retval'),)))
    IInstallationJob.get_IsCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_IsCompleted', ((1, 'retval'),)))
    IInstallationJob.get_Updates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateCollection_head), use_last_error=False)(9, 'get_Updates', ((1, 'retval'),)))
    IInstallationJob.CleanUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'CleanUp', ()))
    IInstallationJob.GetProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IInstallationProgress_head), use_last_error=False)(11, 'GetProgress', ((1, 'retval'),)))
    IInstallationJob.RequestAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'RequestAbort', ()))
    win32more.System.Com.IDispatch
    return IInstallationJob
def _define_IInstallationCompletedCallbackArgs_head():
    class IInstallationCompletedCallbackArgs(win32more.System.Com.IDispatch_head):
        Guid = Guid('250e2106-8efb-4705-9653-ef13c581b6a1')
    return IInstallationCompletedCallbackArgs
def _define_IInstallationCompletedCallbackArgs():
    IInstallationCompletedCallbackArgs = win32more.System.UpdateAgent.IInstallationCompletedCallbackArgs_head
    win32more.System.Com.IDispatch
    return IInstallationCompletedCallbackArgs
def _define_IInstallationCompletedCallback_head():
    class IInstallationCompletedCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('45f4f6f3-d602-4f98-9a8a-3efa152ad2d3')
    return IInstallationCompletedCallback
def _define_IInstallationCompletedCallback():
    IInstallationCompletedCallback = win32more.System.UpdateAgent.IInstallationCompletedCallback_head
    IInstallationCompletedCallback.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IInstallationJob_head,win32more.System.UpdateAgent.IInstallationCompletedCallbackArgs_head, use_last_error=False)(3, 'Invoke', ((1, 'installationJob'),(1, 'callbackArgs'),)))
    win32more.System.Com.IUnknown
    return IInstallationCompletedCallback
def _define_IInstallationProgressChangedCallbackArgs_head():
    class IInstallationProgressChangedCallbackArgs(win32more.System.Com.IDispatch_head):
        Guid = Guid('e4f14e1e-689d-4218-a0b9-bc189c484a01')
    return IInstallationProgressChangedCallbackArgs
def _define_IInstallationProgressChangedCallbackArgs():
    IInstallationProgressChangedCallbackArgs = win32more.System.UpdateAgent.IInstallationProgressChangedCallbackArgs_head
    IInstallationProgressChangedCallbackArgs.get_Progress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IInstallationProgress_head), use_last_error=False)(7, 'get_Progress', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IInstallationProgressChangedCallbackArgs
def _define_IInstallationProgressChangedCallback_head():
    class IInstallationProgressChangedCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('e01402d5-f8da-43ba-a012-38894bd048f1')
    return IInstallationProgressChangedCallback
def _define_IInstallationProgressChangedCallback():
    IInstallationProgressChangedCallback = win32more.System.UpdateAgent.IInstallationProgressChangedCallback_head
    IInstallationProgressChangedCallback.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IInstallationJob_head,win32more.System.UpdateAgent.IInstallationProgressChangedCallbackArgs_head, use_last_error=False)(3, 'Invoke', ((1, 'installationJob'),(1, 'callbackArgs'),)))
    win32more.System.Com.IUnknown
    return IInstallationProgressChangedCallback
def _define_IUpdateInstaller_head():
    class IUpdateInstaller(win32more.System.Com.IDispatch_head):
        Guid = Guid('7b929c68-ccdc-4226-96b1-8724600b54c2')
    return IUpdateInstaller
def _define_IUpdateInstaller():
    IUpdateInstaller = win32more.System.UpdateAgent.IUpdateInstaller_head
    IUpdateInstaller.get_ClientApplicationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ClientApplicationID', ((1, 'retval'),)))
    IUpdateInstaller.put_ClientApplicationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_ClientApplicationID', ((1, 'value'),)))
    IUpdateInstaller.get_IsForced = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_IsForced', ((1, 'retval'),)))
    IUpdateInstaller.put_IsForced = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(10, 'put_IsForced', ((1, 'value'),)))
    IUpdateInstaller.get_ParentHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(11, 'get_ParentHwnd', ((1, 'retval'),)))
    IUpdateInstaller.put_ParentHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(12, 'put_ParentHwnd', ((1, 'value'),)))
    IUpdateInstaller.put_ParentWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(13, 'put_ParentWindow', ((1, 'value'),)))
    IUpdateInstaller.get_ParentWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(14, 'get_ParentWindow', ((1, 'retval'),)))
    IUpdateInstaller.get_Updates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateCollection_head), use_last_error=False)(15, 'get_Updates', ((1, 'retval'),)))
    IUpdateInstaller.put_Updates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IUpdateCollection_head, use_last_error=False)(16, 'put_Updates', ((1, 'value'),)))
    IUpdateInstaller.BeginInstall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,win32more.System.Com.VARIANT,POINTER(win32more.System.UpdateAgent.IInstallationJob_head), use_last_error=False)(17, 'BeginInstall', ((1, 'onProgressChanged'),(1, 'onCompleted'),(1, 'state'),(1, 'retval'),)))
    IUpdateInstaller.BeginUninstall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,win32more.System.Com.VARIANT,POINTER(win32more.System.UpdateAgent.IInstallationJob_head), use_last_error=False)(18, 'BeginUninstall', ((1, 'onProgressChanged'),(1, 'onCompleted'),(1, 'state'),(1, 'retval'),)))
    IUpdateInstaller.EndInstall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IInstallationJob_head,POINTER(win32more.System.UpdateAgent.IInstallationResult_head), use_last_error=False)(19, 'EndInstall', ((1, 'value'),(1, 'retval'),)))
    IUpdateInstaller.EndUninstall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IInstallationJob_head,POINTER(win32more.System.UpdateAgent.IInstallationResult_head), use_last_error=False)(20, 'EndUninstall', ((1, 'value'),(1, 'retval'),)))
    IUpdateInstaller.Install = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IInstallationResult_head), use_last_error=False)(21, 'Install', ((1, 'retval'),)))
    IUpdateInstaller.RunWizard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.UpdateAgent.IInstallationResult_head), use_last_error=False)(22, 'RunWizard', ((1, 'dialogTitle'),(1, 'retval'),)))
    IUpdateInstaller.get_IsBusy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(23, 'get_IsBusy', ((1, 'retval'),)))
    IUpdateInstaller.Uninstall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IInstallationResult_head), use_last_error=False)(24, 'Uninstall', ((1, 'retval'),)))
    IUpdateInstaller.get_AllowSourcePrompts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(25, 'get_AllowSourcePrompts', ((1, 'retval'),)))
    IUpdateInstaller.put_AllowSourcePrompts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(26, 'put_AllowSourcePrompts', ((1, 'value'),)))
    IUpdateInstaller.get_RebootRequiredBeforeInstallation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(27, 'get_RebootRequiredBeforeInstallation', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateInstaller
def _define_IUpdateInstaller2_head():
    class IUpdateInstaller2(win32more.System.UpdateAgent.IUpdateInstaller_head):
        Guid = Guid('3442d4fe-224d-4cee-98cf-30e0c4d229e6')
    return IUpdateInstaller2
def _define_IUpdateInstaller2():
    IUpdateInstaller2 = win32more.System.UpdateAgent.IUpdateInstaller2_head
    IUpdateInstaller2.get_ForceQuiet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(28, 'get_ForceQuiet', ((1, 'retval'),)))
    IUpdateInstaller2.put_ForceQuiet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(29, 'put_ForceQuiet', ((1, 'value'),)))
    win32more.System.UpdateAgent.IUpdateInstaller
    return IUpdateInstaller2
def _define_IUpdateInstaller3_head():
    class IUpdateInstaller3(win32more.System.UpdateAgent.IUpdateInstaller2_head):
        Guid = Guid('16d11c35-099a-48d0-8338-5fae64047f8e')
    return IUpdateInstaller3
def _define_IUpdateInstaller3():
    IUpdateInstaller3 = win32more.System.UpdateAgent.IUpdateInstaller3_head
    IUpdateInstaller3.get_AttemptCloseAppsIfNecessary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(30, 'get_AttemptCloseAppsIfNecessary', ((1, 'retval'),)))
    IUpdateInstaller3.put_AttemptCloseAppsIfNecessary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(31, 'put_AttemptCloseAppsIfNecessary', ((1, 'value'),)))
    win32more.System.UpdateAgent.IUpdateInstaller2
    return IUpdateInstaller3
def _define_IUpdateInstaller4_head():
    class IUpdateInstaller4(win32more.System.UpdateAgent.IUpdateInstaller3_head):
        Guid = Guid('ef8208ea-2304-492d-9109-23813b0958e1')
    return IUpdateInstaller4
def _define_IUpdateInstaller4():
    IUpdateInstaller4 = win32more.System.UpdateAgent.IUpdateInstaller4_head
    IUpdateInstaller4.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(32, 'Commit', ((1, 'dwFlags'),)))
    win32more.System.UpdateAgent.IUpdateInstaller3
    return IUpdateInstaller4
def _define_IUpdateSession_head():
    class IUpdateSession(win32more.System.Com.IDispatch_head):
        Guid = Guid('816858a4-260d-4260-933a-2585f1abc76b')
    return IUpdateSession
def _define_IUpdateSession():
    IUpdateSession = win32more.System.UpdateAgent.IUpdateSession_head
    IUpdateSession.get_ClientApplicationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ClientApplicationID', ((1, 'retval'),)))
    IUpdateSession.put_ClientApplicationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_ClientApplicationID', ((1, 'value'),)))
    IUpdateSession.get_ReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_ReadOnly', ((1, 'retval'),)))
    IUpdateSession.get_WebProxy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IWebProxy_head), use_last_error=False)(10, 'get_WebProxy', ((1, 'retval'),)))
    IUpdateSession.put_WebProxy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.UpdateAgent.IWebProxy_head, use_last_error=False)(11, 'put_WebProxy', ((1, 'value'),)))
    IUpdateSession.CreateUpdateSearcher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateSearcher_head), use_last_error=False)(12, 'CreateUpdateSearcher', ((1, 'retval'),)))
    IUpdateSession.CreateUpdateDownloader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateDownloader_head), use_last_error=False)(13, 'CreateUpdateDownloader', ((1, 'retval'),)))
    IUpdateSession.CreateUpdateInstaller = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateInstaller_head), use_last_error=False)(14, 'CreateUpdateInstaller', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateSession
def _define_IUpdateSession2_head():
    class IUpdateSession2(win32more.System.UpdateAgent.IUpdateSession_head):
        Guid = Guid('91caf7b0-eb23-49ed-9937-c52d817f46f7')
    return IUpdateSession2
def _define_IUpdateSession2():
    IUpdateSession2 = win32more.System.UpdateAgent.IUpdateSession2_head
    IUpdateSession2.get_UserLocale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(15, 'get_UserLocale', ((1, 'retval'),)))
    IUpdateSession2.put_UserLocale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(16, 'put_UserLocale', ((1, 'lcid'),)))
    win32more.System.UpdateAgent.IUpdateSession
    return IUpdateSession2
def _define_IUpdateSession3_head():
    class IUpdateSession3(win32more.System.UpdateAgent.IUpdateSession2_head):
        Guid = Guid('918efd1e-b5d8-4c90-8540-aeb9bdc56f9d')
    return IUpdateSession3
def _define_IUpdateSession3():
    IUpdateSession3 = win32more.System.UpdateAgent.IUpdateSession3_head
    IUpdateSession3.CreateUpdateServiceManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateServiceManager2_head), use_last_error=False)(17, 'CreateUpdateServiceManager', ((1, 'retval'),)))
    IUpdateSession3.QueryHistory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,POINTER(win32more.System.UpdateAgent.IUpdateHistoryEntryCollection_head), use_last_error=False)(18, 'QueryHistory', ((1, 'criteria'),(1, 'startIndex'),(1, 'count'),(1, 'retval'),)))
    win32more.System.UpdateAgent.IUpdateSession2
    return IUpdateSession3
def _define_IUpdateService_head():
    class IUpdateService(win32more.System.Com.IDispatch_head):
        Guid = Guid('76b3b17e-aed6-4da5-85f0-83587f81abe3')
    return IUpdateService
def _define_IUpdateService():
    IUpdateService = win32more.System.UpdateAgent.IUpdateService_head
    IUpdateService.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'retval'),)))
    IUpdateService.get_ContentValidationCert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_ContentValidationCert', ((1, 'retval'),)))
    IUpdateService.get_ExpirationDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(9, 'get_ExpirationDate', ((1, 'retval'),)))
    IUpdateService.get_IsManaged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_IsManaged', ((1, 'retval'),)))
    IUpdateService.get_IsRegisteredWithAU = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_IsRegisteredWithAU', ((1, 'retval'),)))
    IUpdateService.get_IssueDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(12, 'get_IssueDate', ((1, 'retval'),)))
    IUpdateService.get_OffersWindowsUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_OffersWindowsUpdates', ((1, 'retval'),)))
    IUpdateService.get_RedirectUrls = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IStringCollection_head), use_last_error=False)(14, 'get_RedirectUrls', ((1, 'retval'),)))
    IUpdateService.get_ServiceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_ServiceID', ((1, 'retval'),)))
    IUpdateService.get_IsScanPackageService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_IsScanPackageService', ((1, 'retval'),)))
    IUpdateService.get_CanRegisterWithAU = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_CanRegisterWithAU', ((1, 'retval'),)))
    IUpdateService.get_ServiceUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_ServiceUrl', ((1, 'retval'),)))
    IUpdateService.get_SetupPrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_SetupPrefix', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateService
def _define_IUpdateService2_head():
    class IUpdateService2(win32more.System.UpdateAgent.IUpdateService_head):
        Guid = Guid('1518b460-6518-4172-940f-c75883b24ceb')
    return IUpdateService2
def _define_IUpdateService2():
    IUpdateService2 = win32more.System.UpdateAgent.IUpdateService2_head
    IUpdateService2.get_IsDefaultAUService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(20, 'get_IsDefaultAUService', ((1, 'retval'),)))
    win32more.System.UpdateAgent.IUpdateService
    return IUpdateService2
def _define_IUpdateServiceCollection_head():
    class IUpdateServiceCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('9b0353aa-0e52-44ff-b8b0-1f7fa0437f88')
    return IUpdateServiceCollection
def _define_IUpdateServiceCollection():
    IUpdateServiceCollection = win32more.System.UpdateAgent.IUpdateServiceCollection_head
    IUpdateServiceCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.UpdateAgent.IUpdateService_head), use_last_error=False)(7, 'get_Item', ((1, 'index'),(1, 'retval'),)))
    IUpdateServiceCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'retval'),)))
    IUpdateServiceCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateServiceCollection
def _define_IUpdateServiceRegistration_head():
    class IUpdateServiceRegistration(win32more.System.Com.IDispatch_head):
        Guid = Guid('dde02280-12b3-4e0b-937b-6747f6acb286')
    return IUpdateServiceRegistration
def _define_IUpdateServiceRegistration():
    IUpdateServiceRegistration = win32more.System.UpdateAgent.IUpdateServiceRegistration_head
    IUpdateServiceRegistration.get_RegistrationState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.UpdateServiceRegistrationState), use_last_error=False)(7, 'get_RegistrationState', ((1, 'retval'),)))
    IUpdateServiceRegistration.get_ServiceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ServiceID', ((1, 'retval'),)))
    IUpdateServiceRegistration.get_IsPendingRegistrationWithAU = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_IsPendingRegistrationWithAU', ((1, 'retval'),)))
    IUpdateServiceRegistration.get_Service = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateService2_head), use_last_error=False)(10, 'get_Service', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IUpdateServiceRegistration
def _define_IUpdateServiceManager_head():
    class IUpdateServiceManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('23857e3c-02ba-44a3-9423-b1c900805f37')
    return IUpdateServiceManager
def _define_IUpdateServiceManager():
    IUpdateServiceManager = win32more.System.UpdateAgent.IUpdateServiceManager_head
    IUpdateServiceManager.get_Services = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAgent.IUpdateServiceCollection_head), use_last_error=False)(7, 'get_Services', ((1, 'retval'),)))
    IUpdateServiceManager.AddService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.UpdateAgent.IUpdateService_head), use_last_error=False)(8, 'AddService', ((1, 'serviceID'),(1, 'authorizationCabPath'),(1, 'retval'),)))
    IUpdateServiceManager.RegisterServiceWithAU = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'RegisterServiceWithAU', ((1, 'serviceID'),)))
    IUpdateServiceManager.RemoveService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'RemoveService', ((1, 'serviceID'),)))
    IUpdateServiceManager.UnregisterServiceWithAU = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'UnregisterServiceWithAU', ((1, 'serviceID'),)))
    IUpdateServiceManager.AddScanPackageService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.UpdateAgent.IUpdateService_head), use_last_error=False)(12, 'AddScanPackageService', ((1, 'serviceName'),(1, 'scanFileLocation'),(1, 'flags'),(1, 'ppService'),)))
    IUpdateServiceManager.SetOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(13, 'SetOption', ((1, 'optionName'),(1, 'optionValue'),)))
    win32more.System.Com.IDispatch
    return IUpdateServiceManager
def _define_IUpdateServiceManager2_head():
    class IUpdateServiceManager2(win32more.System.UpdateAgent.IUpdateServiceManager_head):
        Guid = Guid('0bb8531d-7e8d-424f-986c-a0b8f60a3e7b')
    return IUpdateServiceManager2
def _define_IUpdateServiceManager2():
    IUpdateServiceManager2 = win32more.System.UpdateAgent.IUpdateServiceManager2_head
    IUpdateServiceManager2.get_ClientApplicationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_ClientApplicationID', ((1, 'retval'),)))
    IUpdateServiceManager2.put_ClientApplicationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_ClientApplicationID', ((1, 'value'),)))
    IUpdateServiceManager2.QueryServiceRegistration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.UpdateAgent.IUpdateServiceRegistration_head), use_last_error=False)(16, 'QueryServiceRegistration', ((1, 'serviceID'),(1, 'retval'),)))
    IUpdateServiceManager2.AddService2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,POINTER(win32more.System.UpdateAgent.IUpdateServiceRegistration_head), use_last_error=False)(17, 'AddService2', ((1, 'serviceID'),(1, 'flags'),(1, 'authorizationCabPath'),(1, 'retval'),)))
    win32more.System.UpdateAgent.IUpdateServiceManager
    return IUpdateServiceManager2
def _define_IInstallationAgent_head():
    class IInstallationAgent(win32more.System.Com.IDispatch_head):
        Guid = Guid('925cbc18-a2ea-4648-bf1c-ec8badcfe20a')
    return IInstallationAgent
def _define_IInstallationAgent():
    IInstallationAgent = win32more.System.UpdateAgent.IInstallationAgent_head
    IInstallationAgent.RecordInstallationResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.UpdateAgent.IStringCollection_head, use_last_error=False)(7, 'RecordInstallationResult', ((1, 'installationResultCookie'),(1, 'hresult'),(1, 'extendedReportingData'),)))
    win32more.System.Com.IDispatch
    return IInstallationAgent
UpdateLockdownOption = Int32
UpdateLockdownOption_uloForWebsiteAccess = 1
AddServiceFlag = Int32
AddServiceFlag_asfAllowPendingRegistration = 1
AddServiceFlag_asfAllowOnlineRegistration = 2
AddServiceFlag_asfRegisterServiceWithAU = 4
UpdateServiceOption = Int32
UpdateServiceOption_usoNonVolatileService = 1
__all__ = [
    "LIBID_WUApiLib",
    "UPDATE_LOCKDOWN_WEBSITE_ACCESS",
    "WU_S_SERVICE_STOP",
    "WU_S_SELFUPDATE",
    "WU_S_UPDATE_ERROR",
    "WU_S_MARKED_FOR_DISCONNECT",
    "WU_S_REBOOT_REQUIRED",
    "WU_S_ALREADY_INSTALLED",
    "WU_S_ALREADY_UNINSTALLED",
    "WU_S_ALREADY_DOWNLOADED",
    "WU_S_SOME_UPDATES_SKIPPED_ON_BATTERY",
    "WU_S_ALREADY_REVERTED",
    "WU_S_SEARCH_CRITERIA_NOT_SUPPORTED",
    "WU_S_UH_INSTALLSTILLPENDING",
    "WU_S_UH_DOWNLOAD_SIZE_CALCULATED",
    "WU_S_SIH_NOOP",
    "WU_S_DM_ALREADYDOWNLOADING",
    "WU_S_METADATA_SKIPPED_BY_ENFORCEMENTMODE",
    "WU_S_METADATA_IGNORED_SIGNATURE_VERIFICATION",
    "WU_S_SEARCH_LOAD_SHEDDING",
    "WU_E_NO_SERVICE",
    "WU_E_MAX_CAPACITY_REACHED",
    "WU_E_UNKNOWN_ID",
    "WU_E_NOT_INITIALIZED",
    "WU_E_RANGEOVERLAP",
    "WU_E_TOOMANYRANGES",
    "WU_E_INVALIDINDEX",
    "WU_E_ITEMNOTFOUND",
    "WU_E_OPERATIONINPROGRESS",
    "WU_E_COULDNOTCANCEL",
    "WU_E_CALL_CANCELLED",
    "WU_E_NOOP",
    "WU_E_XML_MISSINGDATA",
    "WU_E_XML_INVALID",
    "WU_E_CYCLE_DETECTED",
    "WU_E_TOO_DEEP_RELATION",
    "WU_E_INVALID_RELATIONSHIP",
    "WU_E_REG_VALUE_INVALID",
    "WU_E_DUPLICATE_ITEM",
    "WU_E_INVALID_INSTALL_REQUESTED",
    "WU_E_INSTALL_NOT_ALLOWED",
    "WU_E_NOT_APPLICABLE",
    "WU_E_NO_USERTOKEN",
    "WU_E_EXCLUSIVE_INSTALL_CONFLICT",
    "WU_E_POLICY_NOT_SET",
    "WU_E_SELFUPDATE_IN_PROGRESS",
    "WU_E_INVALID_UPDATE",
    "WU_E_SERVICE_STOP",
    "WU_E_NO_CONNECTION",
    "WU_E_NO_INTERACTIVE_USER",
    "WU_E_TIME_OUT",
    "WU_E_ALL_UPDATES_FAILED",
    "WU_E_EULAS_DECLINED",
    "WU_E_NO_UPDATE",
    "WU_E_USER_ACCESS_DISABLED",
    "WU_E_INVALID_UPDATE_TYPE",
    "WU_E_URL_TOO_LONG",
    "WU_E_UNINSTALL_NOT_ALLOWED",
    "WU_E_INVALID_PRODUCT_LICENSE",
    "WU_E_MISSING_HANDLER",
    "WU_E_LEGACYSERVER",
    "WU_E_BIN_SOURCE_ABSENT",
    "WU_E_SOURCE_ABSENT",
    "WU_E_WU_DISABLED",
    "WU_E_CALL_CANCELLED_BY_POLICY",
    "WU_E_INVALID_PROXY_SERVER",
    "WU_E_INVALID_FILE",
    "WU_E_INVALID_CRITERIA",
    "WU_E_EULA_UNAVAILABLE",
    "WU_E_DOWNLOAD_FAILED",
    "WU_E_UPDATE_NOT_PROCESSED",
    "WU_E_INVALID_OPERATION",
    "WU_E_NOT_SUPPORTED",
    "WU_E_WINHTTP_INVALID_FILE",
    "WU_E_TOO_MANY_RESYNC",
    "WU_E_NO_SERVER_CORE_SUPPORT",
    "WU_E_SYSPREP_IN_PROGRESS",
    "WU_E_UNKNOWN_SERVICE",
    "WU_E_NO_UI_SUPPORT",
    "WU_E_PER_MACHINE_UPDATE_ACCESS_DENIED",
    "WU_E_UNSUPPORTED_SEARCHSCOPE",
    "WU_E_BAD_FILE_URL",
    "WU_E_REVERT_NOT_ALLOWED",
    "WU_E_INVALID_NOTIFICATION_INFO",
    "WU_E_OUTOFRANGE",
    "WU_E_SETUP_IN_PROGRESS",
    "WU_E_ORPHANED_DOWNLOAD_JOB",
    "WU_E_LOW_BATTERY",
    "WU_E_INFRASTRUCTUREFILE_INVALID_FORMAT",
    "WU_E_INFRASTRUCTUREFILE_REQUIRES_SSL",
    "WU_E_IDLESHUTDOWN_OPCOUNT_DISCOVERY",
    "WU_E_IDLESHUTDOWN_OPCOUNT_SEARCH",
    "WU_E_IDLESHUTDOWN_OPCOUNT_DOWNLOAD",
    "WU_E_IDLESHUTDOWN_OPCOUNT_INSTALL",
    "WU_E_IDLESHUTDOWN_OPCOUNT_OTHER",
    "WU_E_INTERACTIVE_CALL_CANCELLED",
    "WU_E_AU_CALL_CANCELLED",
    "WU_E_SYSTEM_UNSUPPORTED",
    "WU_E_NO_SUCH_HANDLER_PLUGIN",
    "WU_E_INVALID_SERIALIZATION_VERSION",
    "WU_E_NETWORK_COST_EXCEEDS_POLICY",
    "WU_E_CALL_CANCELLED_BY_HIDE",
    "WU_E_CALL_CANCELLED_BY_INVALID",
    "WU_E_INVALID_VOLUMEID",
    "WU_E_UNRECOGNIZED_VOLUMEID",
    "WU_E_EXTENDEDERROR_NOTSET",
    "WU_E_EXTENDEDERROR_FAILED",
    "WU_E_IDLESHUTDOWN_OPCOUNT_SERVICEREGISTRATION",
    "WU_E_FILETRUST_SHA2SIGNATURE_MISSING",
    "WU_E_UPDATE_NOT_APPROVED",
    "WU_E_CALL_CANCELLED_BY_INTERACTIVE_SEARCH",
    "WU_E_INSTALL_JOB_RESUME_NOT_ALLOWED",
    "WU_E_INSTALL_JOB_NOT_SUSPENDED",
    "WU_E_INSTALL_USERCONTEXT_ACCESSDENIED",
    "WU_E_UNEXPECTED",
    "WU_E_MSI_WRONG_VERSION",
    "WU_E_MSI_NOT_CONFIGURED",
    "WU_E_MSP_DISABLED",
    "WU_E_MSI_WRONG_APP_CONTEXT",
    "WU_E_MSI_NOT_PRESENT",
    "WU_E_MSP_UNEXPECTED",
    "WU_E_PT_SOAPCLIENT_BASE",
    "WU_E_PT_SOAPCLIENT_INITIALIZE",
    "WU_E_PT_SOAPCLIENT_OUTOFMEMORY",
    "WU_E_PT_SOAPCLIENT_GENERATE",
    "WU_E_PT_SOAPCLIENT_CONNECT",
    "WU_E_PT_SOAPCLIENT_SEND",
    "WU_E_PT_SOAPCLIENT_SERVER",
    "WU_E_PT_SOAPCLIENT_SOAPFAULT",
    "WU_E_PT_SOAPCLIENT_PARSEFAULT",
    "WU_E_PT_SOAPCLIENT_READ",
    "WU_E_PT_SOAPCLIENT_PARSE",
    "WU_E_PT_SOAP_VERSION",
    "WU_E_PT_SOAP_MUST_UNDERSTAND",
    "WU_E_PT_SOAP_CLIENT",
    "WU_E_PT_SOAP_SERVER",
    "WU_E_PT_WMI_ERROR",
    "WU_E_PT_EXCEEDED_MAX_SERVER_TRIPS",
    "WU_E_PT_SUS_SERVER_NOT_SET",
    "WU_E_PT_DOUBLE_INITIALIZATION",
    "WU_E_PT_INVALID_COMPUTER_NAME",
    "WU_E_PT_REFRESH_CACHE_REQUIRED",
    "WU_E_PT_HTTP_STATUS_BAD_REQUEST",
    "WU_E_PT_HTTP_STATUS_DENIED",
    "WU_E_PT_HTTP_STATUS_FORBIDDEN",
    "WU_E_PT_HTTP_STATUS_NOT_FOUND",
    "WU_E_PT_HTTP_STATUS_BAD_METHOD",
    "WU_E_PT_HTTP_STATUS_PROXY_AUTH_REQ",
    "WU_E_PT_HTTP_STATUS_REQUEST_TIMEOUT",
    "WU_E_PT_HTTP_STATUS_CONFLICT",
    "WU_E_PT_HTTP_STATUS_GONE",
    "WU_E_PT_HTTP_STATUS_SERVER_ERROR",
    "WU_E_PT_HTTP_STATUS_NOT_SUPPORTED",
    "WU_E_PT_HTTP_STATUS_BAD_GATEWAY",
    "WU_E_PT_HTTP_STATUS_SERVICE_UNAVAIL",
    "WU_E_PT_HTTP_STATUS_GATEWAY_TIMEOUT",
    "WU_E_PT_HTTP_STATUS_VERSION_NOT_SUP",
    "WU_E_PT_FILE_LOCATIONS_CHANGED",
    "WU_E_PT_REGISTRATION_NOT_SUPPORTED",
    "WU_E_PT_NO_AUTH_PLUGINS_REQUESTED",
    "WU_E_PT_NO_AUTH_COOKIES_CREATED",
    "WU_E_PT_INVALID_CONFIG_PROP",
    "WU_E_PT_CONFIG_PROP_MISSING",
    "WU_E_PT_HTTP_STATUS_NOT_MAPPED",
    "WU_E_PT_WINHTTP_NAME_NOT_RESOLVED",
    "WU_E_PT_LOAD_SHEDDING",
    "WU_E_PT_SAME_REDIR_ID",
    "WU_E_PT_NO_MANAGED_RECOVER",
    "WU_E_PT_ECP_SUCCEEDED_WITH_ERRORS",
    "WU_E_PT_ECP_INIT_FAILED",
    "WU_E_PT_ECP_INVALID_FILE_FORMAT",
    "WU_E_PT_ECP_INVALID_METADATA",
    "WU_E_PT_ECP_FAILURE_TO_EXTRACT_DIGEST",
    "WU_E_PT_ECP_FAILURE_TO_DECOMPRESS_CAB_FILE",
    "WU_E_PT_ECP_FILE_LOCATION_ERROR",
    "WU_E_PT_CATALOG_SYNC_REQUIRED",
    "WU_E_PT_SECURITY_VERIFICATION_FAILURE",
    "WU_E_PT_ENDPOINT_UNREACHABLE",
    "WU_E_PT_INVALID_FORMAT",
    "WU_E_PT_INVALID_URL",
    "WU_E_PT_NWS_NOT_LOADED",
    "WU_E_PT_PROXY_AUTH_SCHEME_NOT_SUPPORTED",
    "WU_E_SERVICEPROP_NOTAVAIL",
    "WU_E_PT_ENDPOINT_REFRESH_REQUIRED",
    "WU_E_PT_ENDPOINTURL_NOTAVAIL",
    "WU_E_PT_ENDPOINT_DISCONNECTED",
    "WU_E_PT_INVALID_OPERATION",
    "WU_E_PT_OBJECT_FAULTED",
    "WU_E_PT_NUMERIC_OVERFLOW",
    "WU_E_PT_OPERATION_ABORTED",
    "WU_E_PT_OPERATION_ABANDONED",
    "WU_E_PT_QUOTA_EXCEEDED",
    "WU_E_PT_NO_TRANSLATION_AVAILABLE",
    "WU_E_PT_ADDRESS_IN_USE",
    "WU_E_PT_ADDRESS_NOT_AVAILABLE",
    "WU_E_PT_OTHER",
    "WU_E_PT_SECURITY_SYSTEM_FAILURE",
    "WU_E_PT_UNEXPECTED",
    "WU_E_REDIRECTOR_LOAD_XML",
    "WU_E_REDIRECTOR_S_FALSE",
    "WU_E_REDIRECTOR_ID_SMALLER",
    "WU_E_REDIRECTOR_UNKNOWN_SERVICE",
    "WU_E_REDIRECTOR_UNSUPPORTED_CONTENTTYPE",
    "WU_E_REDIRECTOR_INVALID_RESPONSE",
    "WU_E_REDIRECTOR_ATTRPROVIDER_EXCEEDED_MAX_NAMEVALUE",
    "WU_E_REDIRECTOR_ATTRPROVIDER_INVALID_NAME",
    "WU_E_REDIRECTOR_ATTRPROVIDER_INVALID_VALUE",
    "WU_E_REDIRECTOR_SLS_GENERIC_ERROR",
    "WU_E_REDIRECTOR_CONNECT_POLICY",
    "WU_E_REDIRECTOR_ONLINE_DISALLOWED",
    "WU_E_REDIRECTOR_UNEXPECTED",
    "WU_E_SIH_VERIFY_DOWNLOAD_ENGINE",
    "WU_E_SIH_VERIFY_DOWNLOAD_PAYLOAD",
    "WU_E_SIH_VERIFY_STAGE_ENGINE",
    "WU_E_SIH_VERIFY_STAGE_PAYLOAD",
    "WU_E_SIH_ACTION_NOT_FOUND",
    "WU_E_SIH_SLS_PARSE",
    "WU_E_SIH_INVALIDHASH",
    "WU_E_SIH_NO_ENGINE",
    "WU_E_SIH_POST_REBOOT_INSTALL_FAILED",
    "WU_E_SIH_POST_REBOOT_NO_CACHED_SLS_RESPONSE",
    "WU_E_SIH_PARSE",
    "WU_E_SIH_SECURITY",
    "WU_E_SIH_PPL",
    "WU_E_SIH_POLICY",
    "WU_E_SIH_STDEXCEPTION",
    "WU_E_SIH_NONSTDEXCEPTION",
    "WU_E_SIH_ENGINE_EXCEPTION",
    "WU_E_SIH_BLOCKED_FOR_PLATFORM",
    "WU_E_SIH_ANOTHER_INSTANCE_RUNNING",
    "WU_E_SIH_DNSRESILIENCY_OFF",
    "WU_E_SIH_UNEXPECTED",
    "WU_E_DRV_PRUNED",
    "WU_E_DRV_NOPROP_OR_LEGACY",
    "WU_E_DRV_REG_MISMATCH",
    "WU_E_DRV_NO_METADATA",
    "WU_E_DRV_MISSING_ATTRIBUTE",
    "WU_E_DRV_SYNC_FAILED",
    "WU_E_DRV_NO_PRINTER_CONTENT",
    "WU_E_DRV_DEVICE_PROBLEM",
    "WU_E_DRV_UNEXPECTED",
    "WU_E_DS_SHUTDOWN",
    "WU_E_DS_INUSE",
    "WU_E_DS_INVALID",
    "WU_E_DS_TABLEMISSING",
    "WU_E_DS_TABLEINCORRECT",
    "WU_E_DS_INVALIDTABLENAME",
    "WU_E_DS_BADVERSION",
    "WU_E_DS_NODATA",
    "WU_E_DS_MISSINGDATA",
    "WU_E_DS_MISSINGREF",
    "WU_E_DS_UNKNOWNHANDLER",
    "WU_E_DS_CANTDELETE",
    "WU_E_DS_LOCKTIMEOUTEXPIRED",
    "WU_E_DS_NOCATEGORIES",
    "WU_E_DS_ROWEXISTS",
    "WU_E_DS_STOREFILELOCKED",
    "WU_E_DS_CANNOTREGISTER",
    "WU_E_DS_UNABLETOSTART",
    "WU_E_DS_DUPLICATEUPDATEID",
    "WU_E_DS_UNKNOWNSERVICE",
    "WU_E_DS_SERVICEEXPIRED",
    "WU_E_DS_DECLINENOTALLOWED",
    "WU_E_DS_TABLESESSIONMISMATCH",
    "WU_E_DS_SESSIONLOCKMISMATCH",
    "WU_E_DS_NEEDWINDOWSSERVICE",
    "WU_E_DS_INVALIDOPERATION",
    "WU_E_DS_SCHEMAMISMATCH",
    "WU_E_DS_RESETREQUIRED",
    "WU_E_DS_IMPERSONATED",
    "WU_E_DS_DATANOTAVAILABLE",
    "WU_E_DS_DATANOTLOADED",
    "WU_E_DS_NODATA_NOSUCHREVISION",
    "WU_E_DS_NODATA_NOSUCHUPDATE",
    "WU_E_DS_NODATA_EULA",
    "WU_E_DS_NODATA_SERVICE",
    "WU_E_DS_NODATA_COOKIE",
    "WU_E_DS_NODATA_TIMER",
    "WU_E_DS_NODATA_CCR",
    "WU_E_DS_NODATA_FILE",
    "WU_E_DS_NODATA_DOWNLOADJOB",
    "WU_E_DS_NODATA_TMI",
    "WU_E_DS_UNEXPECTED",
    "WU_E_INVENTORY_PARSEFAILED",
    "WU_E_INVENTORY_GET_INVENTORY_TYPE_FAILED",
    "WU_E_INVENTORY_RESULT_UPLOAD_FAILED",
    "WU_E_INVENTORY_UNEXPECTED",
    "WU_E_INVENTORY_WMI_ERROR",
    "WU_E_AU_NOSERVICE",
    "WU_E_AU_NONLEGACYSERVER",
    "WU_E_AU_LEGACYCLIENTDISABLED",
    "WU_E_AU_PAUSED",
    "WU_E_AU_NO_REGISTERED_SERVICE",
    "WU_E_AU_DETECT_SVCID_MISMATCH",
    "WU_E_REBOOT_IN_PROGRESS",
    "WU_E_AU_OOBE_IN_PROGRESS",
    "WU_E_AU_UNEXPECTED",
    "WU_E_UH_REMOTEUNAVAILABLE",
    "WU_E_UH_LOCALONLY",
    "WU_E_UH_UNKNOWNHANDLER",
    "WU_E_UH_REMOTEALREADYACTIVE",
    "WU_E_UH_DOESNOTSUPPORTACTION",
    "WU_E_UH_WRONGHANDLER",
    "WU_E_UH_INVALIDMETADATA",
    "WU_E_UH_INSTALLERHUNG",
    "WU_E_UH_OPERATIONCANCELLED",
    "WU_E_UH_BADHANDLERXML",
    "WU_E_UH_CANREQUIREINPUT",
    "WU_E_UH_INSTALLERFAILURE",
    "WU_E_UH_FALLBACKTOSELFCONTAINED",
    "WU_E_UH_NEEDANOTHERDOWNLOAD",
    "WU_E_UH_NOTIFYFAILURE",
    "WU_E_UH_INCONSISTENT_FILE_NAMES",
    "WU_E_UH_FALLBACKERROR",
    "WU_E_UH_TOOMANYDOWNLOADREQUESTS",
    "WU_E_UH_UNEXPECTEDCBSRESPONSE",
    "WU_E_UH_BADCBSPACKAGEID",
    "WU_E_UH_POSTREBOOTSTILLPENDING",
    "WU_E_UH_POSTREBOOTRESULTUNKNOWN",
    "WU_E_UH_POSTREBOOTUNEXPECTEDSTATE",
    "WU_E_UH_NEW_SERVICING_STACK_REQUIRED",
    "WU_E_UH_CALLED_BACK_FAILURE",
    "WU_E_UH_CUSTOMINSTALLER_INVALID_SIGNATURE",
    "WU_E_UH_UNSUPPORTED_INSTALLCONTEXT",
    "WU_E_UH_INVALID_TARGETSESSION",
    "WU_E_UH_DECRYPTFAILURE",
    "WU_E_UH_HANDLER_DISABLEDUNTILREBOOT",
    "WU_E_UH_APPX_NOT_PRESENT",
    "WU_E_UH_NOTREADYTOCOMMIT",
    "WU_E_UH_APPX_INVALID_PACKAGE_VOLUME",
    "WU_E_UH_APPX_DEFAULT_PACKAGE_VOLUME_UNAVAILABLE",
    "WU_E_UH_APPX_INSTALLED_PACKAGE_VOLUME_UNAVAILABLE",
    "WU_E_UH_APPX_PACKAGE_FAMILY_NOT_FOUND",
    "WU_E_UH_APPX_SYSTEM_VOLUME_NOT_FOUND",
    "WU_E_UH_UNEXPECTED",
    "WU_E_DM_URLNOTAVAILABLE",
    "WU_E_DM_INCORRECTFILEHASH",
    "WU_E_DM_UNKNOWNALGORITHM",
    "WU_E_DM_NEEDDOWNLOADREQUEST",
    "WU_E_DM_NONETWORK",
    "WU_E_DM_WRONGBITSVERSION",
    "WU_E_DM_NOTDOWNLOADED",
    "WU_E_DM_FAILTOCONNECTTOBITS",
    "WU_E_DM_BITSTRANSFERERROR",
    "WU_E_DM_DOWNLOADLOCATIONCHANGED",
    "WU_E_DM_CONTENTCHANGED",
    "WU_E_DM_DOWNLOADLIMITEDBYUPDATESIZE",
    "WU_E_DM_UNAUTHORIZED",
    "WU_E_DM_BG_ERROR_TOKEN_REQUIRED",
    "WU_E_DM_DOWNLOADSANDBOXNOTFOUND",
    "WU_E_DM_DOWNLOADFILEPATHUNKNOWN",
    "WU_E_DM_DOWNLOADFILEMISSING",
    "WU_E_DM_UPDATEREMOVED",
    "WU_E_DM_READRANGEFAILED",
    "WU_E_DM_UNAUTHORIZED_NO_USER",
    "WU_E_DM_UNAUTHORIZED_LOCAL_USER",
    "WU_E_DM_UNAUTHORIZED_DOMAIN_USER",
    "WU_E_DM_UNAUTHORIZED_MSA_USER",
    "WU_E_DM_FALLINGBACKTOBITS",
    "WU_E_DM_DOWNLOAD_VOLUME_CONFLICT",
    "WU_E_DM_SANDBOX_HASH_MISMATCH",
    "WU_E_DM_HARDRESERVEID_CONFLICT",
    "WU_E_DM_DOSVC_REQUIRED",
    "WU_E_DM_UNEXPECTED",
    "WU_E_SETUP_INVALID_INFDATA",
    "WU_E_SETUP_INVALID_IDENTDATA",
    "WU_E_SETUP_ALREADY_INITIALIZED",
    "WU_E_SETUP_NOT_INITIALIZED",
    "WU_E_SETUP_SOURCE_VERSION_MISMATCH",
    "WU_E_SETUP_TARGET_VERSION_GREATER",
    "WU_E_SETUP_REGISTRATION_FAILED",
    "WU_E_SELFUPDATE_SKIP_ON_FAILURE",
    "WU_E_SETUP_SKIP_UPDATE",
    "WU_E_SETUP_UNSUPPORTED_CONFIGURATION",
    "WU_E_SETUP_BLOCKED_CONFIGURATION",
    "WU_E_SETUP_REBOOT_TO_FIX",
    "WU_E_SETUP_ALREADYRUNNING",
    "WU_E_SETUP_REBOOTREQUIRED",
    "WU_E_SETUP_HANDLER_EXEC_FAILURE",
    "WU_E_SETUP_INVALID_REGISTRY_DATA",
    "WU_E_SELFUPDATE_REQUIRED",
    "WU_E_SELFUPDATE_REQUIRED_ADMIN",
    "WU_E_SETUP_WRONG_SERVER_VERSION",
    "WU_E_SETUP_DEFERRABLE_REBOOT_PENDING",
    "WU_E_SETUP_NON_DEFERRABLE_REBOOT_PENDING",
    "WU_E_SETUP_FAIL",
    "WU_E_SETUP_UNEXPECTED",
    "WU_E_EE_UNKNOWN_EXPRESSION",
    "WU_E_EE_INVALID_EXPRESSION",
    "WU_E_EE_MISSING_METADATA",
    "WU_E_EE_INVALID_VERSION",
    "WU_E_EE_NOT_INITIALIZED",
    "WU_E_EE_INVALID_ATTRIBUTEDATA",
    "WU_E_EE_CLUSTER_ERROR",
    "WU_E_EE_UNEXPECTED",
    "WU_E_INSTALLATION_RESULTS_UNKNOWN_VERSION",
    "WU_E_INSTALLATION_RESULTS_INVALID_DATA",
    "WU_E_INSTALLATION_RESULTS_NOT_FOUND",
    "WU_E_TRAYICON_FAILURE",
    "WU_E_NON_UI_MODE",
    "WU_E_WUCLTUI_UNSUPPORTED_VERSION",
    "WU_E_AUCLIENT_UNEXPECTED",
    "WU_E_REPORTER_EVENTCACHECORRUPT",
    "WU_E_REPORTER_EVENTNAMESPACEPARSEFAILED",
    "WU_E_INVALID_EVENT",
    "WU_E_SERVER_BUSY",
    "WU_E_CALLBACK_COOKIE_NOT_FOUND",
    "WU_E_REPORTER_UNEXPECTED",
    "WU_E_OL_INVALID_SCANFILE",
    "WU_E_OL_NEWCLIENT_REQUIRED",
    "WU_E_INVALID_EVENT_PAYLOAD",
    "WU_E_INVALID_EVENT_PAYLOADSIZE",
    "WU_E_SERVICE_NOT_REGISTERED",
    "WU_E_OL_UNEXPECTED",
    "WU_E_METADATA_NOOP",
    "WU_E_METADATA_CONFIG_INVALID_BINARY_ENCODING",
    "WU_E_METADATA_FETCH_CONFIG",
    "WU_E_METADATA_INVALID_PARAMETER",
    "WU_E_METADATA_UNEXPECTED",
    "WU_E_METADATA_NO_VERIFICATION_DATA",
    "WU_E_METADATA_BAD_FRAGMENTSIGNING_CONFIG",
    "WU_E_METADATA_FAILURE_PROCESSING_FRAGMENTSIGNING_CONFIG",
    "WU_E_METADATA_XML_MISSING",
    "WU_E_METADATA_XML_FRAGMENTSIGNING_MISSING",
    "WU_E_METADATA_XML_MODE_MISSING",
    "WU_E_METADATA_XML_MODE_INVALID",
    "WU_E_METADATA_XML_VALIDITY_INVALID",
    "WU_E_METADATA_XML_LEAFCERT_MISSING",
    "WU_E_METADATA_XML_INTERMEDIATECERT_MISSING",
    "WU_E_METADATA_XML_LEAFCERT_ID_MISSING",
    "WU_E_METADATA_XML_BASE64CERDATA_MISSING",
    "WU_E_METADATA_BAD_SIGNATURE",
    "WU_E_METADATA_UNSUPPORTED_HASH_ALG",
    "WU_E_METADATA_SIGNATURE_VERIFY_FAILED",
    "WU_E_METADATATRUST_CERTIFICATECHAIN_VERIFICATION",
    "WU_E_METADATATRUST_UNTRUSTED_CERTIFICATECHAIN",
    "WU_E_METADATA_TIMESTAMP_TOKEN_MISSING",
    "WU_E_METADATA_TIMESTAMP_TOKEN_VERIFICATION_FAILED",
    "WU_E_METADATA_TIMESTAMP_TOKEN_UNTRUSTED",
    "WU_E_METADATA_TIMESTAMP_TOKEN_VALIDITY_WINDOW",
    "WU_E_METADATA_TIMESTAMP_TOKEN_SIGNATURE",
    "WU_E_METADATA_TIMESTAMP_TOKEN_CERTCHAIN",
    "WU_E_METADATA_TIMESTAMP_TOKEN_REFRESHONLINE",
    "WU_E_METADATA_TIMESTAMP_TOKEN_ALL_BAD",
    "WU_E_METADATA_TIMESTAMP_TOKEN_NODATA",
    "WU_E_METADATA_TIMESTAMP_TOKEN_CACHELOOKUP",
    "WU_E_METADATA_TIMESTAMP_TOKEN_VALIDITYWINDOW_UNEXPECTED",
    "WU_E_METADATA_TIMESTAMP_TOKEN_UNEXPECTED",
    "WU_E_METADATA_CERT_MISSING",
    "WU_E_METADATA_LEAFCERT_BAD_TRANSPORT_ENCODING",
    "WU_E_METADATA_INTCERT_BAD_TRANSPORT_ENCODING",
    "WU_E_METADATA_CERT_UNTRUSTED",
    "WU_E_WUTASK_INPROGRESS",
    "WU_E_WUTASK_STATUS_DISABLED",
    "WU_E_WUTASK_NOT_STARTED",
    "WU_E_WUTASK_RETRY",
    "WU_E_WUTASK_CANCELINSTALL_DISALLOWED",
    "WU_E_UNKNOWN_HARDWARECAPABILITY",
    "WU_E_BAD_XML_HARDWARECAPABILITY",
    "WU_E_WMI_NOT_SUPPORTED",
    "WU_E_UPDATE_MERGE_NOT_ALLOWED",
    "WU_E_SKIPPED_UPDATE_INSTALLATION",
    "WU_E_SLS_INVALID_REVISION",
    "WU_E_FILETRUST_DUALSIGNATURE_RSA",
    "WU_E_FILETRUST_DUALSIGNATURE_ECC",
    "WU_E_TRUST_SUBJECT_NOT_TRUSTED",
    "WU_E_TRUST_PROVIDER_UNKNOWN",
    "StringCollection",
    "UpdateSearcher",
    "WebProxy",
    "SystemInformation",
    "WindowsUpdateAgentInfo",
    "AutomaticUpdates",
    "UpdateCollection",
    "UpdateDownloader",
    "UpdateInstaller",
    "UpdateSession",
    "UpdateServiceManager",
    "InstallationAgent",
    "AutomaticUpdatesNotificationLevel",
    "AutomaticUpdatesNotificationLevel_aunlNotConfigured",
    "AutomaticUpdatesNotificationLevel_aunlDisabled",
    "AutomaticUpdatesNotificationLevel_aunlNotifyBeforeDownload",
    "AutomaticUpdatesNotificationLevel_aunlNotifyBeforeInstallation",
    "AutomaticUpdatesNotificationLevel_aunlScheduledInstallation",
    "AutomaticUpdatesScheduledInstallationDay",
    "AutomaticUpdatesScheduledInstallationDay_ausidEveryDay",
    "AutomaticUpdatesScheduledInstallationDay_ausidEverySunday",
    "AutomaticUpdatesScheduledInstallationDay_ausidEveryMonday",
    "AutomaticUpdatesScheduledInstallationDay_ausidEveryTuesday",
    "AutomaticUpdatesScheduledInstallationDay_ausidEveryWednesday",
    "AutomaticUpdatesScheduledInstallationDay_ausidEveryThursday",
    "AutomaticUpdatesScheduledInstallationDay_ausidEveryFriday",
    "AutomaticUpdatesScheduledInstallationDay_ausidEverySaturday",
    "DownloadPhase",
    "DownloadPhase_dphInitializing",
    "DownloadPhase_dphDownloading",
    "DownloadPhase_dphVerifying",
    "DownloadPriority",
    "DownloadPriority_dpLow",
    "DownloadPriority_dpNormal",
    "DownloadPriority_dpHigh",
    "DownloadPriority_dpExtraHigh",
    "AutoSelectionMode",
    "AutoSelectionMode_asLetWindowsUpdateDecide",
    "AutoSelectionMode_asAutoSelectIfDownloaded",
    "AutoSelectionMode_asNeverAutoSelect",
    "AutoSelectionMode_asAlwaysAutoSelect",
    "AutoDownloadMode",
    "AutoDownloadMode_adLetWindowsUpdateDecide",
    "AutoDownloadMode_adNeverAutoDownload",
    "AutoDownloadMode_adAlwaysAutoDownload",
    "InstallationImpact",
    "InstallationImpact_iiNormal",
    "InstallationImpact_iiMinor",
    "InstallationImpact_iiRequiresExclusiveHandling",
    "InstallationRebootBehavior",
    "InstallationRebootBehavior_irbNeverReboots",
    "InstallationRebootBehavior_irbAlwaysRequiresReboot",
    "InstallationRebootBehavior_irbCanRequestReboot",
    "OperationResultCode",
    "OperationResultCode_orcNotStarted",
    "OperationResultCode_orcInProgress",
    "OperationResultCode_orcSucceeded",
    "OperationResultCode_orcSucceededWithErrors",
    "OperationResultCode_orcFailed",
    "OperationResultCode_orcAborted",
    "ServerSelection",
    "ServerSelection_ssDefault",
    "ServerSelection_ssManagedServer",
    "ServerSelection_ssWindowsUpdate",
    "ServerSelection_ssOthers",
    "UpdateType",
    "UpdateType_utSoftware",
    "UpdateType_utDriver",
    "UpdateOperation",
    "UpdateOperation_uoInstallation",
    "UpdateOperation_uoUninstallation",
    "DeploymentAction",
    "DeploymentAction_daNone",
    "DeploymentAction_daInstallation",
    "DeploymentAction_daUninstallation",
    "DeploymentAction_daDetection",
    "DeploymentAction_daOptionalInstallation",
    "UpdateExceptionContext",
    "UpdateExceptionContext_uecGeneral",
    "UpdateExceptionContext_uecWindowsDriver",
    "UpdateExceptionContext_uecWindowsInstaller",
    "UpdateExceptionContext_uecSearchIncomplete",
    "AutomaticUpdatesUserType",
    "AutomaticUpdatesUserType_auutCurrentUser",
    "AutomaticUpdatesUserType_auutLocalAdministrator",
    "AutomaticUpdatesPermissionType",
    "AutomaticUpdatesPermissionType_auptSetNotificationLevel",
    "AutomaticUpdatesPermissionType_auptDisableAutomaticUpdates",
    "AutomaticUpdatesPermissionType_auptSetIncludeRecommendedUpdates",
    "AutomaticUpdatesPermissionType_auptSetFeaturedUpdatesEnabled",
    "AutomaticUpdatesPermissionType_auptSetNonAdministratorsElevated",
    "UpdateServiceRegistrationState",
    "UpdateServiceRegistrationState_usrsNotRegistered",
    "UpdateServiceRegistrationState_usrsRegistrationPending",
    "UpdateServiceRegistrationState_usrsRegistered",
    "SearchScope",
    "SearchScope_searchScopeDefault",
    "SearchScope_searchScopeMachineOnly",
    "SearchScope_searchScopeCurrentUserOnly",
    "SearchScope_searchScopeMachineAndCurrentUser",
    "SearchScope_searchScopeMachineAndAllUsers",
    "SearchScope_searchScopeAllUsers",
    "IUpdateLockdown",
    "IStringCollection",
    "IWebProxy",
    "ISystemInformation",
    "IWindowsUpdateAgentInfo",
    "IAutomaticUpdatesResults",
    "IAutomaticUpdatesSettings",
    "IAutomaticUpdatesSettings2",
    "IAutomaticUpdatesSettings3",
    "IAutomaticUpdates",
    "IAutomaticUpdates2",
    "IUpdateIdentity",
    "IImageInformation",
    "ICategory",
    "ICategoryCollection",
    "IInstallationBehavior",
    "IUpdateDownloadContent",
    "IUpdateDownloadContent2",
    "IUpdateDownloadContentCollection",
    "IUpdate",
    "IWindowsDriverUpdate",
    "IUpdate2",
    "IUpdate3",
    "IUpdate4",
    "IUpdate5",
    "IWindowsDriverUpdate2",
    "IWindowsDriverUpdate3",
    "IWindowsDriverUpdateEntry",
    "IWindowsDriverUpdateEntryCollection",
    "IWindowsDriverUpdate4",
    "IWindowsDriverUpdate5",
    "IUpdateCollection",
    "IUpdateException",
    "IInvalidProductLicenseException",
    "IUpdateExceptionCollection",
    "ISearchResult",
    "ISearchJob",
    "ISearchCompletedCallbackArgs",
    "ISearchCompletedCallback",
    "IUpdateHistoryEntry",
    "IUpdateHistoryEntry2",
    "IUpdateHistoryEntryCollection",
    "IUpdateSearcher",
    "IUpdateSearcher2",
    "IUpdateSearcher3",
    "IUpdateDownloadResult",
    "IDownloadResult",
    "IDownloadProgress",
    "IDownloadJob",
    "IDownloadCompletedCallbackArgs",
    "IDownloadCompletedCallback",
    "IDownloadProgressChangedCallbackArgs",
    "IDownloadProgressChangedCallback",
    "IUpdateDownloader",
    "IUpdateInstallationResult",
    "IInstallationResult",
    "IInstallationProgress",
    "IInstallationJob",
    "IInstallationCompletedCallbackArgs",
    "IInstallationCompletedCallback",
    "IInstallationProgressChangedCallbackArgs",
    "IInstallationProgressChangedCallback",
    "IUpdateInstaller",
    "IUpdateInstaller2",
    "IUpdateInstaller3",
    "IUpdateInstaller4",
    "IUpdateSession",
    "IUpdateSession2",
    "IUpdateSession3",
    "IUpdateService",
    "IUpdateService2",
    "IUpdateServiceCollection",
    "IUpdateServiceRegistration",
    "IUpdateServiceManager",
    "IUpdateServiceManager2",
    "IInstallationAgent",
    "UpdateLockdownOption",
    "UpdateLockdownOption_uloForWebsiteAccess",
    "AddServiceFlag",
    "AddServiceFlag_asfAllowPendingRegistration",
    "AddServiceFlag_asfAllowOnlineRegistration",
    "AddServiceFlag_asfRegisterServiceWithAU",
    "UpdateServiceOption",
    "UpdateServiceOption_usoNonVolatileService",
]
