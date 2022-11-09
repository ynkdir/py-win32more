from win32more.base import *
import win32more.Foundation
import win32more.Networking.ActiveDirectory
import win32more.Networking.WinSock
import win32more.Security
import win32more.Security.Authentication.Identity
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Ole
import win32more.System.Registry
import win32more.UI.Controls
import win32more.UI.Shell
import win32more.UI.WindowsAndMessaging

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
WM_ADSPROP_NOTIFY_PAGEINIT = 2125
WM_ADSPROP_NOTIFY_PAGEHWND = 2126
WM_ADSPROP_NOTIFY_CHANGE = 2127
WM_ADSPROP_NOTIFY_APPLY = 2128
WM_ADSPROP_NOTIFY_SETFOCUS = 2129
WM_ADSPROP_NOTIFY_FOREGROUND = 2130
WM_ADSPROP_NOTIFY_EXIT = 2131
WM_ADSPROP_NOTIFY_ERROR = 2134
CLSID_CommonQuery = '83bc5ec0-6f2a-11d0-a1c4-00aa00c16e65'
QUERYFORM_CHANGESFORMLIST = 1
QUERYFORM_CHANGESOPTFORMLIST = 2
CQFF_NOGLOBALPAGES = 1
CQFF_ISOPTIONAL = 2
CQPM_INITIALIZE = 1
CQPM_RELEASE = 2
CQPM_ENABLE = 3
CQPM_GETPARAMETERS = 5
CQPM_CLEARFORM = 6
CQPM_PERSIST = 7
CQPM_HELP = 8
CQPM_SETDEFAULTPARAMETERS = 9
CQPM_HANDLERSPECIFIC = 268435456
OQWF_OKCANCEL = 1
OQWF_DEFAULTFORM = 2
OQWF_SINGLESELECT = 4
OQWF_LOADQUERY = 8
OQWF_REMOVESCOPES = 16
OQWF_REMOVEFORMS = 32
OQWF_ISSUEONOPEN = 64
OQWF_SHOWOPTIONAL = 128
OQWF_SAVEQUERYONOK = 512
OQWF_HIDEMENUS = 1024
OQWF_HIDESEARCHUI = 2048
OQWF_PARAMISPROPERTYBAG = 2147483648
CLSID_DsAdminCreateObj = 'e301a009-f901-11d2-82b9-00c04f68928b'
DSA_NEWOBJ_CTX_PRECOMMIT = 1
DSA_NEWOBJ_CTX_COMMIT = 2
DSA_NEWOBJ_CTX_POSTCOMMIT = 3
DSA_NEWOBJ_CTX_CLEANUP = 4
DSA_NOTIFY_DEL = 1
DSA_NOTIFY_REN = 2
DSA_NOTIFY_MOV = 4
DSA_NOTIFY_PROP = 8
DSA_NOTIFY_FLAG_ADDITIONAL_DATA = 2
DSA_NOTIFY_FLAG_FORCE_ADDITIONAL_DATA = 1
CLSID_MicrosoftDS = 'fe1290f0-cfbd-11cf-a330-00aa00c16e65'
CLSID_DsPropertyPages = '0d45d530-764b-11d0-a1ca-00aa00c16e65'
CLSID_DsDomainTreeBrowser = '1698790a-e2b4-11d0-b0b1-00c04fd8dca6'
CLSID_DsDisplaySpecifier = '1ab4a8c0-6a0b-11d2-ad49-00c04fa31a86'
CLSID_DsFolderProperties = '9e51e0d0-6e0f-11d2-9601-00c04fa31a86'
DSOBJECT_ISCONTAINER = 1
DSOBJECT_READONLYPAGES = 2147483648
DSPROVIDER_UNUSED_0 = 1
DSPROVIDER_UNUSED_1 = 2
DSPROVIDER_UNUSED_2 = 4
DSPROVIDER_UNUSED_3 = 8
DSPROVIDER_ADVANCED = 16
DSPROVIDER_AD_LDS = 32
DSDSOF_HASUSERANDSERVERINFO = 1
DSDSOF_SIMPLEAUTHENTICATE = 2
DSDSOF_DONTSIGNSEAL = 4
DSDSOF_DSAVAILABLE = 1073741824
DBDTF_RETURNFQDN = 1
DBDTF_RETURNMIXEDDOMAINS = 2
DBDTF_RETURNEXTERNAL = 4
DBDTF_RETURNINBOUND = 8
DBDTF_RETURNINOUTBOUND = 16
DSSSF_SIMPLEAUTHENTICATE = 1
DSSSF_DONTSIGNSEAL = 2
DSSSF_DSAVAILABLE = 2147483648
DSGIF_ISNORMAL = 0
DSGIF_ISOPEN = 1
DSGIF_ISDISABLED = 2
DSGIF_ISMASK = 15
DSGIF_GETDEFAULTICON = 16
DSGIF_DEFAULTISCONTAINER = 32
DSICCF_IGNORETREATASLEAF = 1
DSECAF_NOTLISTED = 1
DSCCIF_HASWIZARDDIALOG = 1
DSCCIF_HASWIZARDPRIMARYPAGE = 2
DSBI_NOBUTTONS = 1
DSBI_NOLINES = 2
DSBI_NOLINESATROOT = 4
DSBI_CHECKBOXES = 256
DSBI_NOROOT = 65536
DSBI_INCLUDEHIDDEN = 131072
DSBI_EXPANDONOPEN = 262144
DSBI_ENTIREDIRECTORY = 589824
DSBI_RETURN_FORMAT = 1048576
DSBI_HASCREDENTIALS = 2097152
DSBI_IGNORETREATASLEAF = 4194304
DSBI_SIMPLEAUTHENTICATE = 8388608
DSBI_RETURNOBJECTCLASS = 16777216
DSBI_DONTSIGNSEAL = 33554432
DSB_MAX_DISPLAYNAME_CHARS = 64
DSBF_STATE = 1
DSBF_ICONLOCATION = 2
DSBF_DISPLAYNAME = 4
DSBS_CHECKED = 1
DSBS_HIDDEN = 2
DSBS_ROOT = 4
DSBM_QUERYINSERTW = 100
DSBM_QUERYINSERTA = 101
DSBM_QUERYINSERT = 100
DSBM_CHANGEIMAGESTATE = 102
DSBM_HELP = 103
DSBM_CONTEXTMENU = 104
DSBID_BANNER = 256
DSBID_CONTAINERLIST = 257
DS_FORCE_REDISCOVERY = 1
DS_DIRECTORY_SERVICE_REQUIRED = 16
DS_DIRECTORY_SERVICE_PREFERRED = 32
DS_GC_SERVER_REQUIRED = 64
DS_PDC_REQUIRED = 128
DS_BACKGROUND_ONLY = 256
DS_IP_REQUIRED = 512
DS_KDC_REQUIRED = 1024
DS_TIMESERV_REQUIRED = 2048
DS_WRITABLE_REQUIRED = 4096
DS_GOOD_TIMESERV_PREFERRED = 8192
DS_AVOID_SELF = 16384
DS_ONLY_LDAP_NEEDED = 32768
DS_IS_FLAT_NAME = 65536
DS_IS_DNS_NAME = 131072
DS_TRY_NEXTCLOSEST_SITE = 262144
DS_DIRECTORY_SERVICE_6_REQUIRED = 524288
DS_WEB_SERVICE_REQUIRED = 1048576
DS_DIRECTORY_SERVICE_8_REQUIRED = 2097152
DS_DIRECTORY_SERVICE_9_REQUIRED = 4194304
DS_DIRECTORY_SERVICE_10_REQUIRED = 8388608
DS_KEY_LIST_SUPPORT_REQUIRED = 16777216
DS_RETURN_DNS_NAME = 1073741824
DS_RETURN_FLAT_NAME = 2147483648
DS_PDC_FLAG = 1
DS_GC_FLAG = 4
DS_LDAP_FLAG = 8
DS_DS_FLAG = 16
DS_KDC_FLAG = 32
DS_TIMESERV_FLAG = 64
DS_CLOSEST_FLAG = 128
DS_WRITABLE_FLAG = 256
DS_GOOD_TIMESERV_FLAG = 512
DS_NDNC_FLAG = 1024
DS_SELECT_SECRET_DOMAIN_6_FLAG = 2048
DS_FULL_SECRET_DOMAIN_6_FLAG = 4096
DS_WS_FLAG = 8192
DS_DS_8_FLAG = 16384
DS_DS_9_FLAG = 32768
DS_DS_10_FLAG = 65536
DS_KEY_LIST_FLAG = 131072
DS_PING_FLAGS = 1048575
DS_DNS_CONTROLLER_FLAG = 536870912
DS_DNS_DOMAIN_FLAG = 1073741824
DS_DNS_FOREST_FLAG = 2147483648
DS_DOMAIN_IN_FOREST = 1
DS_DOMAIN_DIRECT_OUTBOUND = 2
DS_DOMAIN_TREE_ROOT = 4
DS_DOMAIN_PRIMARY = 8
DS_DOMAIN_NATIVE_MODE = 16
DS_DOMAIN_DIRECT_INBOUND = 32
DS_GFTI_UPDATE_TDO = 1
DS_GFTI_VALID_FLAGS = 1
DS_ONLY_DO_SITE_NAME = 1
DS_NOTIFY_AFTER_SITE_RECORDS = 2
CLSID_DsQuery = '8a23e65e-31c2-11d0-891c-00a024ab2dbb'
CLSID_DsFindObjects = '83ee3fe1-57d9-11d0-b932-00a024ab2dbb'
CLSID_DsFindPeople = '83ee3fe2-57d9-11d0-b932-00a024ab2dbb'
CLSID_DsFindPrinter = 'b577f070-7ee2-11d0-913f-00aa00c16e65'
CLSID_DsFindComputer = '16006700-87ad-11d0-9140-00aa00c16e65'
CLSID_DsFindVolume = 'c1b3cbf1-886a-11d0-9140-00aa00c16e65'
CLSID_DsFindContainer = 'c1b3cbf2-886a-11d0-9140-00aa00c16e65'
CLSID_DsFindAdvanced = '83ee3fe3-57d9-11d0-b932-00a024ab2dbb'
CLSID_DsFindDomainController = '538c7b7e-d25e-11d0-9742-00a0c906af45'
CLSID_DsFindWriteableDomainController = '7cbef079-aa84-444b-bc70-68e41283eabc'
CLSID_DsFindFrsMembers = '94ce4b18-b3d3-11d1-b9b4-00c04fd8d5b0'
DSQPF_NOSAVE = 1
DSQPF_SAVELOCATION = 2
DSQPF_SHOWHIDDENOBJECTS = 4
DSQPF_ENABLEADMINFEATURES = 8
DSQPF_ENABLEADVANCEDFEATURES = 16
DSQPF_HASCREDENTIALS = 32
DSQPF_NOCHOOSECOLUMNS = 64
DSQPM_GETCLASSLIST = 268435456
DSQPM_HELPTOPICS = 268435457
DSROLE_PRIMARY_DS_RUNNING = 1
DSROLE_PRIMARY_DS_MIXED_MODE = 2
DSROLE_UPGRADE_IN_PROGRESS = 4
DSROLE_PRIMARY_DS_READONLY = 8
DSROLE_PRIMARY_DOMAIN_GUID_PRESENT = 16777216
ADS_ATTR_CLEAR = 1
ADS_ATTR_UPDATE = 2
ADS_ATTR_APPEND = 3
ADS_ATTR_DELETE = 4
ADS_EXT_MINEXTDISPID = 1
ADS_EXT_MAXEXTDISPID = 16777215
ADS_EXT_INITCREDENTIALS = 1
ADS_EXT_INITIALIZE_COMPLETE = 2
DS_BEHAVIOR_WIN2000 = 0
DS_BEHAVIOR_WIN2003_WITH_MIXED_DOMAINS = 1
DS_BEHAVIOR_WIN2003 = 2
DS_BEHAVIOR_WIN2008 = 3
DS_BEHAVIOR_WIN2008R2 = 4
DS_BEHAVIOR_WIN2012 = 5
DS_BEHAVIOR_WIN2012R2 = 6
DS_BEHAVIOR_WIN2016 = 7
DS_BEHAVIOR_LONGHORN = 3
DS_BEHAVIOR_WIN7 = 4
DS_BEHAVIOR_WIN8 = 5
DS_BEHAVIOR_WINBLUE = 6
DS_BEHAVIOR_WINTHRESHOLD = 7
ACTRL_DS_OPEN = 0
ACTRL_DS_CREATE_CHILD = 1
ACTRL_DS_DELETE_CHILD = 2
ACTRL_DS_LIST = 4
ACTRL_DS_SELF = 8
ACTRL_DS_READ_PROP = 16
ACTRL_DS_WRITE_PROP = 32
ACTRL_DS_DELETE_TREE = 64
ACTRL_DS_LIST_OBJECT = 128
ACTRL_DS_CONTROL_ACCESS = 256
NTDSAPI_BIND_ALLOW_DELEGATION = 1
NTDSAPI_BIND_FIND_BINDING = 2
NTDSAPI_BIND_FORCE_KERBEROS = 4
DS_REPSYNC_ASYNCHRONOUS_OPERATION = 1
DS_REPSYNC_WRITEABLE = 2
DS_REPSYNC_PERIODIC = 4
DS_REPSYNC_INTERSITE_MESSAGING = 8
DS_REPSYNC_FULL = 32
DS_REPSYNC_URGENT = 64
DS_REPSYNC_NO_DISCARD = 128
DS_REPSYNC_FORCE = 256
DS_REPSYNC_ADD_REFERENCE = 512
DS_REPSYNC_NEVER_COMPLETED = 1024
DS_REPSYNC_TWO_WAY = 2048
DS_REPSYNC_NEVER_NOTIFY = 4096
DS_REPSYNC_INITIAL = 8192
DS_REPSYNC_USE_COMPRESSION = 16384
DS_REPSYNC_ABANDONED = 32768
DS_REPSYNC_SELECT_SECRETS = 32768
DS_REPSYNC_INITIAL_IN_PROGRESS = 65536
DS_REPSYNC_PARTIAL_ATTRIBUTE_SET = 131072
DS_REPSYNC_REQUEUE = 262144
DS_REPSYNC_NOTIFICATION = 524288
DS_REPSYNC_ASYNCHRONOUS_REPLICA = 1048576
DS_REPSYNC_CRITICAL = 2097152
DS_REPSYNC_FULL_IN_PROGRESS = 4194304
DS_REPSYNC_PREEMPTED = 8388608
DS_REPSYNC_NONGC_RO_REPLICA = 16777216
DS_REPADD_ASYNCHRONOUS_OPERATION = 1
DS_REPADD_WRITEABLE = 2
DS_REPADD_INITIAL = 4
DS_REPADD_PERIODIC = 8
DS_REPADD_INTERSITE_MESSAGING = 16
DS_REPADD_ASYNCHRONOUS_REPLICA = 32
DS_REPADD_DISABLE_NOTIFICATION = 64
DS_REPADD_DISABLE_PERIODIC = 128
DS_REPADD_USE_COMPRESSION = 256
DS_REPADD_NEVER_NOTIFY = 512
DS_REPADD_TWO_WAY = 1024
DS_REPADD_CRITICAL = 2048
DS_REPADD_SELECT_SECRETS = 4096
DS_REPADD_NONGC_RO_REPLICA = 16777216
DS_REPDEL_ASYNCHRONOUS_OPERATION = 1
DS_REPDEL_WRITEABLE = 2
DS_REPDEL_INTERSITE_MESSAGING = 4
DS_REPDEL_IGNORE_ERRORS = 8
DS_REPDEL_LOCAL_ONLY = 16
DS_REPDEL_NO_SOURCE = 32
DS_REPDEL_REF_OK = 64
DS_REPMOD_ASYNCHRONOUS_OPERATION = 1
DS_REPMOD_WRITEABLE = 2
DS_REPMOD_UPDATE_FLAGS = 1
DS_REPMOD_UPDATE_INSTANCE = 2
DS_REPMOD_UPDATE_ADDRESS = 2
DS_REPMOD_UPDATE_SCHEDULE = 4
DS_REPMOD_UPDATE_RESULT = 8
DS_REPMOD_UPDATE_TRANSPORT = 16
DS_REPUPD_ASYNCHRONOUS_OPERATION = 1
DS_REPUPD_WRITEABLE = 2
DS_REPUPD_ADD_REFERENCE = 4
DS_REPUPD_DELETE_REFERENCE = 8
DS_REPUPD_REFERENCE_GCSPN = 16
DS_INSTANCETYPE_IS_NC_HEAD = 1
DS_INSTANCETYPE_NC_IS_WRITEABLE = 4
DS_INSTANCETYPE_NC_COMING = 16
DS_INSTANCETYPE_NC_GOING = 32
NTDSDSA_OPT_IS_GC = 1
NTDSDSA_OPT_DISABLE_INBOUND_REPL = 2
NTDSDSA_OPT_DISABLE_OUTBOUND_REPL = 4
NTDSDSA_OPT_DISABLE_NTDSCONN_XLATE = 8
NTDSDSA_OPT_DISABLE_SPN_REGISTRATION = 16
NTDSDSA_OPT_GENERATE_OWN_TOPO = 32
NTDSDSA_OPT_BLOCK_RPC = 64
NTDSCONN_OPT_IS_GENERATED = 1
NTDSCONN_OPT_TWOWAY_SYNC = 2
NTDSCONN_OPT_OVERRIDE_NOTIFY_DEFAULT = 4
NTDSCONN_OPT_USE_NOTIFY = 8
NTDSCONN_OPT_DISABLE_INTERSITE_COMPRESSION = 16
NTDSCONN_OPT_USER_OWNED_SCHEDULE = 32
NTDSCONN_OPT_RODC_TOPOLOGY = 64
NTDSCONN_KCC_NO_REASON = 0
NTDSCONN_KCC_GC_TOPOLOGY = 1
NTDSCONN_KCC_RING_TOPOLOGY = 2
NTDSCONN_KCC_MINIMIZE_HOPS_TOPOLOGY = 4
NTDSCONN_KCC_STALE_SERVERS_TOPOLOGY = 8
NTDSCONN_KCC_OSCILLATING_CONNECTION_TOPOLOGY = 16
NTDSCONN_KCC_INTERSITE_GC_TOPOLOGY = 32
NTDSCONN_KCC_INTERSITE_TOPOLOGY = 64
NTDSCONN_KCC_SERVER_FAILOVER_TOPOLOGY = 128
NTDSCONN_KCC_SITE_FAILOVER_TOPOLOGY = 256
NTDSCONN_KCC_REDUNDANT_SERVER_TOPOLOGY = 512
FRSCONN_PRIORITY_MASK = 1879048192
FRSCONN_MAX_PRIORITY = 8
NTDSCONN_OPT_IGNORE_SCHEDULE_MASK = 2147483648
NTDSSETTINGS_OPT_IS_AUTO_TOPOLOGY_DISABLED = 1
NTDSSETTINGS_OPT_IS_TOPL_CLEANUP_DISABLED = 2
NTDSSETTINGS_OPT_IS_TOPL_MIN_HOPS_DISABLED = 4
NTDSSETTINGS_OPT_IS_TOPL_DETECT_STALE_DISABLED = 8
NTDSSETTINGS_OPT_IS_INTER_SITE_AUTO_TOPOLOGY_DISABLED = 16
NTDSSETTINGS_OPT_IS_GROUP_CACHING_ENABLED = 32
NTDSSETTINGS_OPT_FORCE_KCC_WHISTLER_BEHAVIOR = 64
NTDSSETTINGS_OPT_FORCE_KCC_W2K_ELECTION = 128
NTDSSETTINGS_OPT_IS_RAND_BH_SELECTION_DISABLED = 256
NTDSSETTINGS_OPT_IS_SCHEDULE_HASHING_ENABLED = 512
NTDSSETTINGS_OPT_IS_REDUNDANT_SERVER_TOPOLOGY_ENABLED = 1024
NTDSSETTINGS_OPT_W2K3_IGNORE_SCHEDULES = 2048
NTDSSETTINGS_OPT_W2K3_BRIDGES_REQUIRED = 4096
NTDSSETTINGS_DEFAULT_SERVER_REDUNDANCY = 2
NTDSTRANSPORT_OPT_IGNORE_SCHEDULES = 1
NTDSTRANSPORT_OPT_BRIDGES_REQUIRED = 2
NTDSSITECONN_OPT_USE_NOTIFY = 1
NTDSSITECONN_OPT_TWOWAY_SYNC = 2
NTDSSITECONN_OPT_DISABLE_COMPRESSION = 4
NTDSSITELINK_OPT_USE_NOTIFY = 1
NTDSSITELINK_OPT_TWOWAY_SYNC = 2
NTDSSITELINK_OPT_DISABLE_COMPRESSION = 4
DS_REPSYNCALL_NO_OPTIONS = 0
DS_REPSYNCALL_ABORT_IF_SERVER_UNAVAILABLE = 1
DS_REPSYNCALL_SYNC_ADJACENT_SERVERS_ONLY = 2
DS_REPSYNCALL_ID_SERVERS_BY_DN = 4
DS_REPSYNCALL_DO_NOT_SYNC = 8
DS_REPSYNCALL_SKIP_INITIAL_CHECK = 16
DS_REPSYNCALL_PUSH_CHANGES_OUTWARD = 32
DS_REPSYNCALL_CROSS_SITE_BOUNDARIES = 64
DS_LIST_DSA_OBJECT_FOR_SERVER = 0
DS_LIST_DNS_HOST_NAME_FOR_SERVER = 1
DS_LIST_ACCOUNT_OBJECT_FOR_SERVER = 2
DS_ROLE_SCHEMA_OWNER = 0
DS_ROLE_DOMAIN_OWNER = 1
DS_ROLE_PDC_OWNER = 2
DS_ROLE_RID_OWNER = 3
DS_ROLE_INFRASTRUCTURE_OWNER = 4
DS_SCHEMA_GUID_NOT_FOUND = 0
DS_SCHEMA_GUID_ATTR = 1
DS_SCHEMA_GUID_ATTR_SET = 2
DS_SCHEMA_GUID_CLASS = 3
DS_SCHEMA_GUID_CONTROL_RIGHT = 4
DS_KCC_FLAG_ASYNC_OP = 1
DS_KCC_FLAG_DAMPED = 2
DS_EXIST_ADVISORY_MODE = 1
DS_REPL_INFO_FLAG_IMPROVE_LINKED_ATTRS = 1
DS_REPL_NBR_WRITEABLE = 16
DS_REPL_NBR_SYNC_ON_STARTUP = 32
DS_REPL_NBR_DO_SCHEDULED_SYNCS = 64
DS_REPL_NBR_USE_ASYNC_INTERSITE_TRANSPORT = 128
DS_REPL_NBR_TWO_WAY_SYNC = 512
DS_REPL_NBR_NONGC_RO_REPLICA = 1024
DS_REPL_NBR_RETURN_OBJECT_PARENTS = 2048
DS_REPL_NBR_SELECT_SECRETS = 4096
DS_REPL_NBR_FULL_SYNC_IN_PROGRESS = 65536
DS_REPL_NBR_FULL_SYNC_NEXT_PACKET = 131072
DS_REPL_NBR_GCSPN = 1048576
DS_REPL_NBR_NEVER_SYNCED = 2097152
DS_REPL_NBR_PREEMPTED = 16777216
DS_REPL_NBR_IGNORE_CHANGE_NOTIFICATIONS = 67108864
DS_REPL_NBR_DISABLE_SCHEDULED_SYNC = 134217728
DS_REPL_NBR_COMPRESS_CHANGES = 268435456
DS_REPL_NBR_NO_CHANGE_NOTIFICATIONS = 536870912
DS_REPL_NBR_PARTIAL_ATTRIBUTE_SET = 1073741824
ADAM_REPL_AUTHENTICATION_MODE_NEGOTIATE_PASS_THROUGH = 0
ADAM_REPL_AUTHENTICATION_MODE_NEGOTIATE = 1
ADAM_REPL_AUTHENTICATION_MODE_MUTUAL_AUTH_REQUIRED = 2
FLAG_FOREST_OPTIONAL_FEATURE = 1
FLAG_DOMAIN_OPTIONAL_FEATURE = 2
FLAG_DISABLABLE_OPTIONAL_FEATURE = 4
FLAG_SERVER_OPTIONAL_FEATURE = 8
DSOP_SCOPE_TYPE_TARGET_COMPUTER = 1
DSOP_SCOPE_TYPE_UPLEVEL_JOINED_DOMAIN = 2
DSOP_SCOPE_TYPE_DOWNLEVEL_JOINED_DOMAIN = 4
DSOP_SCOPE_TYPE_ENTERPRISE_DOMAIN = 8
DSOP_SCOPE_TYPE_GLOBAL_CATALOG = 16
DSOP_SCOPE_TYPE_EXTERNAL_UPLEVEL_DOMAIN = 32
DSOP_SCOPE_TYPE_EXTERNAL_DOWNLEVEL_DOMAIN = 64
DSOP_SCOPE_TYPE_WORKGROUP = 128
DSOP_SCOPE_TYPE_USER_ENTERED_UPLEVEL_SCOPE = 256
DSOP_SCOPE_TYPE_USER_ENTERED_DOWNLEVEL_SCOPE = 512
DSOP_SCOPE_FLAG_STARTING_SCOPE = 1
DSOP_SCOPE_FLAG_WANT_PROVIDER_WINNT = 2
DSOP_SCOPE_FLAG_WANT_PROVIDER_LDAP = 4
DSOP_SCOPE_FLAG_WANT_PROVIDER_GC = 8
DSOP_SCOPE_FLAG_WANT_SID_PATH = 16
DSOP_SCOPE_FLAG_WANT_DOWNLEVEL_BUILTIN_PATH = 32
DSOP_SCOPE_FLAG_DEFAULT_FILTER_USERS = 64
DSOP_SCOPE_FLAG_DEFAULT_FILTER_GROUPS = 128
DSOP_SCOPE_FLAG_DEFAULT_FILTER_COMPUTERS = 256
DSOP_SCOPE_FLAG_DEFAULT_FILTER_CONTACTS = 512
DSOP_SCOPE_FLAG_DEFAULT_FILTER_SERVICE_ACCOUNTS = 1024
DSOP_SCOPE_FLAG_DEFAULT_FILTER_PASSWORDSETTINGS_OBJECTS = 2048
DSOP_FILTER_INCLUDE_ADVANCED_VIEW = 1
DSOP_FILTER_USERS = 2
DSOP_FILTER_BUILTIN_GROUPS = 4
DSOP_FILTER_WELL_KNOWN_PRINCIPALS = 8
DSOP_FILTER_UNIVERSAL_GROUPS_DL = 16
DSOP_FILTER_UNIVERSAL_GROUPS_SE = 32
DSOP_FILTER_GLOBAL_GROUPS_DL = 64
DSOP_FILTER_GLOBAL_GROUPS_SE = 128
DSOP_FILTER_DOMAIN_LOCAL_GROUPS_DL = 256
DSOP_FILTER_DOMAIN_LOCAL_GROUPS_SE = 512
DSOP_FILTER_CONTACTS = 1024
DSOP_FILTER_COMPUTERS = 2048
DSOP_FILTER_SERVICE_ACCOUNTS = 4096
DSOP_FILTER_PASSWORDSETTINGS_OBJECTS = 8192
DSOP_DOWNLEVEL_FILTER_USERS = 2147483649
DSOP_DOWNLEVEL_FILTER_LOCAL_GROUPS = 2147483650
DSOP_DOWNLEVEL_FILTER_GLOBAL_GROUPS = 2147483652
DSOP_DOWNLEVEL_FILTER_COMPUTERS = 2147483656
DSOP_DOWNLEVEL_FILTER_WORLD = 2147483664
DSOP_DOWNLEVEL_FILTER_AUTHENTICATED_USER = 2147483680
DSOP_DOWNLEVEL_FILTER_ANONYMOUS = 2147483712
DSOP_DOWNLEVEL_FILTER_BATCH = 2147483776
DSOP_DOWNLEVEL_FILTER_CREATOR_OWNER = 2147483904
DSOP_DOWNLEVEL_FILTER_CREATOR_GROUP = 2147484160
DSOP_DOWNLEVEL_FILTER_DIALUP = 2147484672
DSOP_DOWNLEVEL_FILTER_INTERACTIVE = 2147485696
DSOP_DOWNLEVEL_FILTER_NETWORK = 2147487744
DSOP_DOWNLEVEL_FILTER_SERVICE = 2147491840
DSOP_DOWNLEVEL_FILTER_SYSTEM = 2147500032
DSOP_DOWNLEVEL_FILTER_EXCLUDE_BUILTIN_GROUPS = 2147516416
DSOP_DOWNLEVEL_FILTER_TERMINAL_SERVER = 2147549184
DSOP_DOWNLEVEL_FILTER_ALL_WELLKNOWN_SIDS = 2147614720
DSOP_DOWNLEVEL_FILTER_LOCAL_SERVICE = 2147745792
DSOP_DOWNLEVEL_FILTER_NETWORK_SERVICE = 2148007936
DSOP_DOWNLEVEL_FILTER_REMOTE_LOGON = 2148532224
DSOP_DOWNLEVEL_FILTER_INTERNET_USER = 2149580800
DSOP_DOWNLEVEL_FILTER_OWNER_RIGHTS = 2151677952
DSOP_DOWNLEVEL_FILTER_SERVICES = 2155872256
DSOP_DOWNLEVEL_FILTER_LOCAL_LOGON = 2164260864
DSOP_DOWNLEVEL_FILTER_THIS_ORG_CERT = 2181038080
DSOP_DOWNLEVEL_FILTER_IIS_APP_POOL = 2214592512
DSOP_DOWNLEVEL_FILTER_ALL_APP_PACKAGES = 2281701376
DSOP_DOWNLEVEL_FILTER_LOCAL_ACCOUNTS = 2415919104
DSOP_FLAG_MULTISELECT = 1
DSOP_FLAG_SKIP_TARGET_COMPUTER_DC_CHECK = 2
SCHEDULE_INTERVAL = 0
SCHEDULE_BANDWIDTH = 1
SCHEDULE_PRIORITY = 2
FACILITY_NTDSB = 2048
FACILITY_BACKUP = 2047
FACILITY_SYSTEM = 0
STATUS_SEVERITY_SUCCESS = 0
STATUS_SEVERITY_INFORMATIONAL = 1
STATUS_SEVERITY_WARNING = 2
STATUS_SEVERITY_ERROR = 3
CLSID_DsObjectPicker = '17d6ccd8-3b7b-11d2-b9e0-00c04fd8dbf7'
def _define_CQFORM_head():
    class CQFORM(Structure):
        pass
    return CQFORM
def _define_CQFORM():
    CQFORM = win32more.Networking.ActiveDirectory.CQFORM_head
    CQFORM._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("clsid", Guid),
        ("hIcon", win32more.UI.WindowsAndMessaging.HICON),
        ("pszTitle", win32more.Foundation.PWSTR),
    ]
    return CQFORM
def _define_LPCQADDFORMSPROC():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LPARAM,POINTER(win32more.Networking.ActiveDirectory.CQFORM_head), use_last_error=False)
def _define_LPCQADDPAGESPROC():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LPARAM,POINTER(Guid),POINTER(win32more.Networking.ActiveDirectory.CQPAGE_head), use_last_error=False)
def _define_LPCQPAGEPROC():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.CQPAGE_head),win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)
def _define_CQPAGE_head():
    class CQPAGE(Structure):
        pass
    return CQPAGE
def _define_CQPAGE():
    CQPAGE = win32more.Networking.ActiveDirectory.CQPAGE_head
    CQPAGE._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("pPageProc", win32more.Networking.ActiveDirectory.LPCQPAGEPROC),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("idPageName", Int32),
        ("idPageTemplate", Int32),
        ("pDlgProc", win32more.UI.WindowsAndMessaging.DLGPROC),
        ("lParam", win32more.Foundation.LPARAM),
    ]
    return CQPAGE
def _define_IQueryForm_head():
    class IQueryForm(win32more.System.Com.IUnknown_head):
        Guid = Guid('8cfcee30-39bd-11d0-b8d1-00a024ab2dbb')
    return IQueryForm
def _define_IQueryForm():
    IQueryForm = win32more.Networking.ActiveDirectory.IQueryForm_head
    IQueryForm.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Registry.HKEY, use_last_error=False)(3, 'Initialize', ((1, 'hkForm'),)))
    IQueryForm.AddForms = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.ActiveDirectory.LPCQADDFORMSPROC,win32more.Foundation.LPARAM, use_last_error=False)(4, 'AddForms', ((1, 'pAddFormsProc'),(1, 'lParam'),)))
    IQueryForm.AddPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.ActiveDirectory.LPCQADDPAGESPROC,win32more.Foundation.LPARAM, use_last_error=False)(5, 'AddPages', ((1, 'pAddPagesProc'),(1, 'lParam'),)))
    win32more.System.Com.IUnknown
    return IQueryForm
def _define_IPersistQuery_head():
    class IPersistQuery(win32more.System.Com.IPersist_head):
        Guid = Guid('1a3114b8-a62e-11d0-a6c5-00a0c906af45')
    return IPersistQuery
def _define_IPersistQuery():
    IPersistQuery = win32more.Networking.ActiveDirectory.IPersistQuery_head
    IPersistQuery.WriteString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(4, 'WriteString', ((1, 'pSection'),(1, 'pValueName'),(1, 'pValue'),)))
    IPersistQuery.ReadString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32, use_last_error=False)(5, 'ReadString', ((1, 'pSection'),(1, 'pValueName'),(1, 'pBuffer'),(1, 'cchBuffer'),)))
    IPersistQuery.WriteInt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32, use_last_error=False)(6, 'WriteInt', ((1, 'pSection'),(1, 'pValueName'),(1, 'value'),)))
    IPersistQuery.ReadInt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Int32), use_last_error=False)(7, 'ReadInt', ((1, 'pSection'),(1, 'pValueName'),(1, 'pValue'),)))
    IPersistQuery.WriteStruct = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32, use_last_error=False)(8, 'WriteStruct', ((1, 'pSection'),(1, 'pValueName'),(1, 'pStruct'),(1, 'cbStruct'),)))
    IPersistQuery.ReadStruct = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32, use_last_error=False)(9, 'ReadStruct', ((1, 'pSection'),(1, 'pValueName'),(1, 'pStruct'),(1, 'cbStruct'),)))
    IPersistQuery.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Clear', ()))
    win32more.System.Com.IPersist
    return IPersistQuery
def _define_OPENQUERYWINDOW_head():
    class OPENQUERYWINDOW(Structure):
        pass
    return OPENQUERYWINDOW
def _define_OPENQUERYWINDOW():
    OPENQUERYWINDOW = win32more.Networking.ActiveDirectory.OPENQUERYWINDOW_head
    class OPENQUERYWINDOW__Anonymous_e__Union(Union):
        pass
    OPENQUERYWINDOW__Anonymous_e__Union._fields_ = [
        ("pFormParameters", c_void_p),
        ("ppbFormParameters", win32more.System.Com.StructuredStorage.IPropertyBag_head),
    ]
    OPENQUERYWINDOW._anonymous_ = [
        'Anonymous',
    ]
    OPENQUERYWINDOW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("clsidHandler", Guid),
        ("pHandlerParameters", c_void_p),
        ("clsidDefaultForm", Guid),
        ("pPersistQuery", win32more.Networking.ActiveDirectory.IPersistQuery_head),
        ("Anonymous", OPENQUERYWINDOW__Anonymous_e__Union),
    ]
    return OPENQUERYWINDOW
def _define_ICommonQuery_head():
    class ICommonQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('ab50dec0-6f1d-11d0-a1c4-00aa00c16e65')
    return ICommonQuery
def _define_ICommonQuery():
    ICommonQuery = win32more.Networking.ActiveDirectory.ICommonQuery_head
    ICommonQuery.OpenQueryWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Networking.ActiveDirectory.OPENQUERYWINDOW_head),POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(3, 'OpenQueryWindow', ((1, 'hwndParent'),(1, 'pQueryWnd'),(1, 'ppDataObject'),)))
    win32more.System.Com.IUnknown
    return ICommonQuery
PropertyEntry = Guid('72d3edc2-a4c4-11d0-8533-00c04fd8d503')
PropertyValue = Guid('7b9e38b0-a97c-11d0-8534-00c04fd8d503')
AccessControlEntry = Guid('b75ac000-9bdd-11d0-852c-00c04fd8d503')
AccessControlList = Guid('b85ea052-9bdd-11d0-852c-00c04fd8d503')
SecurityDescriptor = Guid('b958f73c-9bdd-11d0-852c-00c04fd8d503')
LargeInteger = Guid('927971f5-0939-11d1-8be1-00c04fd8d503')
NameTranslate = Guid('274fae1f-3626-11d1-a3a4-00c04fb950dc')
CaseIgnoreList = Guid('15f88a55-4680-11d1-a3b4-00c04fb950dc')
FaxNumber = Guid('a5062215-4681-11d1-a3b4-00c04fb950dc')
NetAddress = Guid('b0b71247-4080-11d1-a3ac-00c04fb950dc')
OctetList = Guid('1241400f-4680-11d1-a3b4-00c04fb950dc')
Email = Guid('8f92a857-478e-11d1-a3b4-00c04fb950dc')
Path = Guid('b2538919-4080-11d1-a3ac-00c04fb950dc')
ReplicaPointer = Guid('f5d1badf-4080-11d1-a3ac-00c04fb950dc')
Timestamp = Guid('b2bed2eb-4080-11d1-a3ac-00c04fb950dc')
PostalAddress = Guid('0a75afcd-4680-11d1-a3b4-00c04fb950dc')
BackLink = Guid('fcbf906f-4080-11d1-a3ac-00c04fb950dc')
TypedName = Guid('b33143cb-4080-11d1-a3ac-00c04fb950dc')
Hold = Guid('b3ad3e13-4080-11d1-a3ac-00c04fb950dc')
Pathname = Guid('080d0d78-f421-11d0-a36e-00c04fb950dc')
ADSystemInfo = Guid('50b6327f-afd1-11d2-9cb9-0000f87a369e')
WinNTSystemInfo = Guid('66182ec4-afd1-11d2-9cb9-0000f87a369e')
DNWithBinary = Guid('7e99c0a3-f935-11d2-ba96-00c04fb6d0d1')
DNWithString = Guid('334857cc-f934-11d2-ba96-00c04fb6d0d1')
ADsSecurityUtility = Guid('f270c64a-ffb8-4ae4-85fe-3a75e5347966')
ADSTYPEENUM = Int32
ADSTYPE_INVALID = 0
ADSTYPE_DN_STRING = 1
ADSTYPE_CASE_EXACT_STRING = 2
ADSTYPE_CASE_IGNORE_STRING = 3
ADSTYPE_PRINTABLE_STRING = 4
ADSTYPE_NUMERIC_STRING = 5
ADSTYPE_BOOLEAN = 6
ADSTYPE_INTEGER = 7
ADSTYPE_OCTET_STRING = 8
ADSTYPE_UTC_TIME = 9
ADSTYPE_LARGE_INTEGER = 10
ADSTYPE_PROV_SPECIFIC = 11
ADSTYPE_OBJECT_CLASS = 12
ADSTYPE_CASEIGNORE_LIST = 13
ADSTYPE_OCTET_LIST = 14
ADSTYPE_PATH = 15
ADSTYPE_POSTALADDRESS = 16
ADSTYPE_TIMESTAMP = 17
ADSTYPE_BACKLINK = 18
ADSTYPE_TYPEDNAME = 19
ADSTYPE_HOLD = 20
ADSTYPE_NETADDRESS = 21
ADSTYPE_REPLICAPOINTER = 22
ADSTYPE_FAXNUMBER = 23
ADSTYPE_EMAIL = 24
ADSTYPE_NT_SECURITY_DESCRIPTOR = 25
ADSTYPE_UNKNOWN = 26
ADSTYPE_DN_WITH_BINARY = 27
ADSTYPE_DN_WITH_STRING = 28
def _define_ADS_OCTET_STRING_head():
    class ADS_OCTET_STRING(Structure):
        pass
    return ADS_OCTET_STRING
def _define_ADS_OCTET_STRING():
    ADS_OCTET_STRING = win32more.Networking.ActiveDirectory.ADS_OCTET_STRING_head
    ADS_OCTET_STRING._fields_ = [
        ("dwLength", UInt32),
        ("lpValue", c_char_p_no),
    ]
    return ADS_OCTET_STRING
def _define_ADS_NT_SECURITY_DESCRIPTOR_head():
    class ADS_NT_SECURITY_DESCRIPTOR(Structure):
        pass
    return ADS_NT_SECURITY_DESCRIPTOR
def _define_ADS_NT_SECURITY_DESCRIPTOR():
    ADS_NT_SECURITY_DESCRIPTOR = win32more.Networking.ActiveDirectory.ADS_NT_SECURITY_DESCRIPTOR_head
    ADS_NT_SECURITY_DESCRIPTOR._fields_ = [
        ("dwLength", UInt32),
        ("lpValue", c_char_p_no),
    ]
    return ADS_NT_SECURITY_DESCRIPTOR
def _define_ADS_PROV_SPECIFIC_head():
    class ADS_PROV_SPECIFIC(Structure):
        pass
    return ADS_PROV_SPECIFIC
def _define_ADS_PROV_SPECIFIC():
    ADS_PROV_SPECIFIC = win32more.Networking.ActiveDirectory.ADS_PROV_SPECIFIC_head
    ADS_PROV_SPECIFIC._fields_ = [
        ("dwLength", UInt32),
        ("lpValue", c_char_p_no),
    ]
    return ADS_PROV_SPECIFIC
def _define_ADS_CASEIGNORE_LIST_head():
    class ADS_CASEIGNORE_LIST(Structure):
        pass
    return ADS_CASEIGNORE_LIST
def _define_ADS_CASEIGNORE_LIST():
    ADS_CASEIGNORE_LIST = win32more.Networking.ActiveDirectory.ADS_CASEIGNORE_LIST_head
    ADS_CASEIGNORE_LIST._fields_ = [
        ("Next", POINTER(win32more.Networking.ActiveDirectory.ADS_CASEIGNORE_LIST_head)),
        ("String", win32more.Foundation.PWSTR),
    ]
    return ADS_CASEIGNORE_LIST
def _define_ADS_OCTET_LIST_head():
    class ADS_OCTET_LIST(Structure):
        pass
    return ADS_OCTET_LIST
def _define_ADS_OCTET_LIST():
    ADS_OCTET_LIST = win32more.Networking.ActiveDirectory.ADS_OCTET_LIST_head
    ADS_OCTET_LIST._fields_ = [
        ("Next", POINTER(win32more.Networking.ActiveDirectory.ADS_OCTET_LIST_head)),
        ("Length", UInt32),
        ("Data", c_char_p_no),
    ]
    return ADS_OCTET_LIST
def _define_ADS_PATH_head():
    class ADS_PATH(Structure):
        pass
    return ADS_PATH
def _define_ADS_PATH():
    ADS_PATH = win32more.Networking.ActiveDirectory.ADS_PATH_head
    ADS_PATH._fields_ = [
        ("Type", UInt32),
        ("VolumeName", win32more.Foundation.PWSTR),
        ("Path", win32more.Foundation.PWSTR),
    ]
    return ADS_PATH
def _define_ADS_POSTALADDRESS_head():
    class ADS_POSTALADDRESS(Structure):
        pass
    return ADS_POSTALADDRESS
def _define_ADS_POSTALADDRESS():
    ADS_POSTALADDRESS = win32more.Networking.ActiveDirectory.ADS_POSTALADDRESS_head
    ADS_POSTALADDRESS._fields_ = [
        ("PostalAddress", win32more.Foundation.PWSTR * 6),
    ]
    return ADS_POSTALADDRESS
def _define_ADS_TIMESTAMP_head():
    class ADS_TIMESTAMP(Structure):
        pass
    return ADS_TIMESTAMP
def _define_ADS_TIMESTAMP():
    ADS_TIMESTAMP = win32more.Networking.ActiveDirectory.ADS_TIMESTAMP_head
    ADS_TIMESTAMP._fields_ = [
        ("WholeSeconds", UInt32),
        ("EventID", UInt32),
    ]
    return ADS_TIMESTAMP
def _define_ADS_BACKLINK_head():
    class ADS_BACKLINK(Structure):
        pass
    return ADS_BACKLINK
def _define_ADS_BACKLINK():
    ADS_BACKLINK = win32more.Networking.ActiveDirectory.ADS_BACKLINK_head
    ADS_BACKLINK._fields_ = [
        ("RemoteID", UInt32),
        ("ObjectName", win32more.Foundation.PWSTR),
    ]
    return ADS_BACKLINK
def _define_ADS_TYPEDNAME_head():
    class ADS_TYPEDNAME(Structure):
        pass
    return ADS_TYPEDNAME
def _define_ADS_TYPEDNAME():
    ADS_TYPEDNAME = win32more.Networking.ActiveDirectory.ADS_TYPEDNAME_head
    ADS_TYPEDNAME._fields_ = [
        ("ObjectName", win32more.Foundation.PWSTR),
        ("Level", UInt32),
        ("Interval", UInt32),
    ]
    return ADS_TYPEDNAME
def _define_ADS_HOLD_head():
    class ADS_HOLD(Structure):
        pass
    return ADS_HOLD
def _define_ADS_HOLD():
    ADS_HOLD = win32more.Networking.ActiveDirectory.ADS_HOLD_head
    ADS_HOLD._fields_ = [
        ("ObjectName", win32more.Foundation.PWSTR),
        ("Amount", UInt32),
    ]
    return ADS_HOLD
def _define_ADS_NETADDRESS_head():
    class ADS_NETADDRESS(Structure):
        pass
    return ADS_NETADDRESS
def _define_ADS_NETADDRESS():
    ADS_NETADDRESS = win32more.Networking.ActiveDirectory.ADS_NETADDRESS_head
    ADS_NETADDRESS._fields_ = [
        ("AddressType", UInt32),
        ("AddressLength", UInt32),
        ("Address", c_char_p_no),
    ]
    return ADS_NETADDRESS
def _define_ADS_REPLICAPOINTER_head():
    class ADS_REPLICAPOINTER(Structure):
        pass
    return ADS_REPLICAPOINTER
def _define_ADS_REPLICAPOINTER():
    ADS_REPLICAPOINTER = win32more.Networking.ActiveDirectory.ADS_REPLICAPOINTER_head
    ADS_REPLICAPOINTER._fields_ = [
        ("ServerName", win32more.Foundation.PWSTR),
        ("ReplicaType", UInt32),
        ("ReplicaNumber", UInt32),
        ("Count", UInt32),
        ("ReplicaAddressHints", POINTER(win32more.Networking.ActiveDirectory.ADS_NETADDRESS_head)),
    ]
    return ADS_REPLICAPOINTER
def _define_ADS_FAXNUMBER_head():
    class ADS_FAXNUMBER(Structure):
        pass
    return ADS_FAXNUMBER
def _define_ADS_FAXNUMBER():
    ADS_FAXNUMBER = win32more.Networking.ActiveDirectory.ADS_FAXNUMBER_head
    ADS_FAXNUMBER._fields_ = [
        ("TelephoneNumber", win32more.Foundation.PWSTR),
        ("NumberOfBits", UInt32),
        ("Parameters", c_char_p_no),
    ]
    return ADS_FAXNUMBER
def _define_ADS_EMAIL_head():
    class ADS_EMAIL(Structure):
        pass
    return ADS_EMAIL
def _define_ADS_EMAIL():
    ADS_EMAIL = win32more.Networking.ActiveDirectory.ADS_EMAIL_head
    ADS_EMAIL._fields_ = [
        ("Address", win32more.Foundation.PWSTR),
        ("Type", UInt32),
    ]
    return ADS_EMAIL
def _define_ADS_DN_WITH_BINARY_head():
    class ADS_DN_WITH_BINARY(Structure):
        pass
    return ADS_DN_WITH_BINARY
def _define_ADS_DN_WITH_BINARY():
    ADS_DN_WITH_BINARY = win32more.Networking.ActiveDirectory.ADS_DN_WITH_BINARY_head
    ADS_DN_WITH_BINARY._fields_ = [
        ("dwLength", UInt32),
        ("lpBinaryValue", c_char_p_no),
        ("pszDNString", win32more.Foundation.PWSTR),
    ]
    return ADS_DN_WITH_BINARY
def _define_ADS_DN_WITH_STRING_head():
    class ADS_DN_WITH_STRING(Structure):
        pass
    return ADS_DN_WITH_STRING
def _define_ADS_DN_WITH_STRING():
    ADS_DN_WITH_STRING = win32more.Networking.ActiveDirectory.ADS_DN_WITH_STRING_head
    ADS_DN_WITH_STRING._fields_ = [
        ("pszStringValue", win32more.Foundation.PWSTR),
        ("pszDNString", win32more.Foundation.PWSTR),
    ]
    return ADS_DN_WITH_STRING
def _define_ADSVALUE_head():
    class ADSVALUE(Structure):
        pass
    return ADSVALUE
def _define_ADSVALUE():
    ADSVALUE = win32more.Networking.ActiveDirectory.ADSVALUE_head
    class ADSVALUE__Anonymous_e__Union(Union):
        pass
    ADSVALUE__Anonymous_e__Union._fields_ = [
        ("DNString", POINTER(UInt16)),
        ("CaseExactString", POINTER(UInt16)),
        ("CaseIgnoreString", POINTER(UInt16)),
        ("PrintableString", POINTER(UInt16)),
        ("NumericString", POINTER(UInt16)),
        ("Boolean", UInt32),
        ("Integer", UInt32),
        ("OctetString", win32more.Networking.ActiveDirectory.ADS_OCTET_STRING),
        ("UTCTime", win32more.Foundation.SYSTEMTIME),
        ("LargeInteger", win32more.Foundation.LARGE_INTEGER),
        ("ClassName", POINTER(UInt16)),
        ("ProviderSpecific", win32more.Networking.ActiveDirectory.ADS_PROV_SPECIFIC),
        ("pCaseIgnoreList", POINTER(win32more.Networking.ActiveDirectory.ADS_CASEIGNORE_LIST_head)),
        ("pOctetList", POINTER(win32more.Networking.ActiveDirectory.ADS_OCTET_LIST_head)),
        ("pPath", POINTER(win32more.Networking.ActiveDirectory.ADS_PATH_head)),
        ("pPostalAddress", POINTER(win32more.Networking.ActiveDirectory.ADS_POSTALADDRESS_head)),
        ("Timestamp", win32more.Networking.ActiveDirectory.ADS_TIMESTAMP),
        ("BackLink", win32more.Networking.ActiveDirectory.ADS_BACKLINK),
        ("pTypedName", POINTER(win32more.Networking.ActiveDirectory.ADS_TYPEDNAME_head)),
        ("Hold", win32more.Networking.ActiveDirectory.ADS_HOLD),
        ("pNetAddress", POINTER(win32more.Networking.ActiveDirectory.ADS_NETADDRESS_head)),
        ("pReplicaPointer", POINTER(win32more.Networking.ActiveDirectory.ADS_REPLICAPOINTER_head)),
        ("pFaxNumber", POINTER(win32more.Networking.ActiveDirectory.ADS_FAXNUMBER_head)),
        ("Email", win32more.Networking.ActiveDirectory.ADS_EMAIL),
        ("SecurityDescriptor", win32more.Networking.ActiveDirectory.ADS_NT_SECURITY_DESCRIPTOR),
        ("pDNWithBinary", POINTER(win32more.Networking.ActiveDirectory.ADS_DN_WITH_BINARY_head)),
        ("pDNWithString", POINTER(win32more.Networking.ActiveDirectory.ADS_DN_WITH_STRING_head)),
    ]
    ADSVALUE._anonymous_ = [
        'Anonymous',
    ]
    ADSVALUE._fields_ = [
        ("dwType", win32more.Networking.ActiveDirectory.ADSTYPEENUM),
        ("Anonymous", ADSVALUE__Anonymous_e__Union),
    ]
    return ADSVALUE
def _define_ADS_ATTR_INFO_head():
    class ADS_ATTR_INFO(Structure):
        pass
    return ADS_ATTR_INFO
def _define_ADS_ATTR_INFO():
    ADS_ATTR_INFO = win32more.Networking.ActiveDirectory.ADS_ATTR_INFO_head
    ADS_ATTR_INFO._fields_ = [
        ("pszAttrName", win32more.Foundation.PWSTR),
        ("dwControlCode", UInt32),
        ("dwADsType", win32more.Networking.ActiveDirectory.ADSTYPEENUM),
        ("pADsValues", POINTER(win32more.Networking.ActiveDirectory.ADSVALUE_head)),
        ("dwNumValues", UInt32),
    ]
    return ADS_ATTR_INFO
ADS_AUTHENTICATION_ENUM = UInt32
ADS_SECURE_AUTHENTICATION = 1
ADS_USE_ENCRYPTION = 2
ADS_USE_SSL = 2
ADS_READONLY_SERVER = 4
ADS_PROMPT_CREDENTIALS = 8
ADS_NO_AUTHENTICATION = 16
ADS_FAST_BIND = 32
ADS_USE_SIGNING = 64
ADS_USE_SEALING = 128
ADS_USE_DELEGATION = 256
ADS_SERVER_BIND = 512
ADS_NO_REFERRAL_CHASING = 1024
ADS_AUTH_RESERVED = 2147483648
def _define_ADS_OBJECT_INFO_head():
    class ADS_OBJECT_INFO(Structure):
        pass
    return ADS_OBJECT_INFO
def _define_ADS_OBJECT_INFO():
    ADS_OBJECT_INFO = win32more.Networking.ActiveDirectory.ADS_OBJECT_INFO_head
    ADS_OBJECT_INFO._fields_ = [
        ("pszRDN", win32more.Foundation.PWSTR),
        ("pszObjectDN", win32more.Foundation.PWSTR),
        ("pszParentDN", win32more.Foundation.PWSTR),
        ("pszSchemaDN", win32more.Foundation.PWSTR),
        ("pszClassName", win32more.Foundation.PWSTR),
    ]
    return ADS_OBJECT_INFO
ADS_STATUSENUM = Int32
ADS_STATUS_S_OK = 0
ADS_STATUS_INVALID_SEARCHPREF = 1
ADS_STATUS_INVALID_SEARCHPREFVALUE = 2
ADS_DEREFENUM = Int32
ADS_DEREF_NEVER = 0
ADS_DEREF_SEARCHING = 1
ADS_DEREF_FINDING = 2
ADS_DEREF_ALWAYS = 3
ADS_SCOPEENUM = Int32
ADS_SCOPE_BASE = 0
ADS_SCOPE_ONELEVEL = 1
ADS_SCOPE_SUBTREE = 2
ADS_PREFERENCES_ENUM = Int32
ADSIPROP_ASYNCHRONOUS = 0
ADSIPROP_DEREF_ALIASES = 1
ADSIPROP_SIZE_LIMIT = 2
ADSIPROP_TIME_LIMIT = 3
ADSIPROP_ATTRIBTYPES_ONLY = 4
ADSIPROP_SEARCH_SCOPE = 5
ADSIPROP_TIMEOUT = 6
ADSIPROP_PAGESIZE = 7
ADSIPROP_PAGED_TIME_LIMIT = 8
ADSIPROP_CHASE_REFERRALS = 9
ADSIPROP_SORT_ON = 10
ADSIPROP_CACHE_RESULTS = 11
ADSIPROP_ADSIFLAG = 12
ADSI_DIALECT_ENUM = Int32
ADSI_DIALECT_LDAP = 0
ADSI_DIALECT_SQL = 1
ADS_CHASE_REFERRALS_ENUM = Int32
ADS_CHASE_REFERRALS_NEVER = 0
ADS_CHASE_REFERRALS_SUBORDINATE = 32
ADS_CHASE_REFERRALS_EXTERNAL = 64
ADS_CHASE_REFERRALS_ALWAYS = 96
ADS_SEARCHPREF_ENUM = Int32
ADS_SEARCHPREF_ASYNCHRONOUS = 0
ADS_SEARCHPREF_DEREF_ALIASES = 1
ADS_SEARCHPREF_SIZE_LIMIT = 2
ADS_SEARCHPREF_TIME_LIMIT = 3
ADS_SEARCHPREF_ATTRIBTYPES_ONLY = 4
ADS_SEARCHPREF_SEARCH_SCOPE = 5
ADS_SEARCHPREF_TIMEOUT = 6
ADS_SEARCHPREF_PAGESIZE = 7
ADS_SEARCHPREF_PAGED_TIME_LIMIT = 8
ADS_SEARCHPREF_CHASE_REFERRALS = 9
ADS_SEARCHPREF_SORT_ON = 10
ADS_SEARCHPREF_CACHE_RESULTS = 11
ADS_SEARCHPREF_DIRSYNC = 12
ADS_SEARCHPREF_TOMBSTONE = 13
ADS_SEARCHPREF_VLV = 14
ADS_SEARCHPREF_ATTRIBUTE_QUERY = 15
ADS_SEARCHPREF_SECURITY_MASK = 16
ADS_SEARCHPREF_DIRSYNC_FLAG = 17
ADS_SEARCHPREF_EXTENDED_DN = 18
ADS_PASSWORD_ENCODING_ENUM = Int32
ADS_PASSWORD_ENCODE_REQUIRE_SSL = 0
ADS_PASSWORD_ENCODE_CLEAR = 1
def _define_ads_searchpref_info_head():
    class ads_searchpref_info(Structure):
        pass
    return ads_searchpref_info
def _define_ads_searchpref_info():
    ads_searchpref_info = win32more.Networking.ActiveDirectory.ads_searchpref_info_head
    ads_searchpref_info._fields_ = [
        ("dwSearchPref", win32more.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM),
        ("vValue", win32more.Networking.ActiveDirectory.ADSVALUE),
        ("dwStatus", win32more.Networking.ActiveDirectory.ADS_STATUSENUM),
    ]
    return ads_searchpref_info
def _define_ads_search_column_head():
    class ads_search_column(Structure):
        pass
    return ads_search_column
def _define_ads_search_column():
    ads_search_column = win32more.Networking.ActiveDirectory.ads_search_column_head
    ads_search_column._fields_ = [
        ("pszAttrName", win32more.Foundation.PWSTR),
        ("dwADsType", win32more.Networking.ActiveDirectory.ADSTYPEENUM),
        ("pADsValues", POINTER(win32more.Networking.ActiveDirectory.ADSVALUE_head)),
        ("dwNumValues", UInt32),
        ("hReserved", win32more.Foundation.HANDLE),
    ]
    return ads_search_column
def _define_ADS_ATTR_DEF_head():
    class ADS_ATTR_DEF(Structure):
        pass
    return ADS_ATTR_DEF
def _define_ADS_ATTR_DEF():
    ADS_ATTR_DEF = win32more.Networking.ActiveDirectory.ADS_ATTR_DEF_head
    ADS_ATTR_DEF._fields_ = [
        ("pszAttrName", win32more.Foundation.PWSTR),
        ("dwADsType", win32more.Networking.ActiveDirectory.ADSTYPEENUM),
        ("dwMinRange", UInt32),
        ("dwMaxRange", UInt32),
        ("fMultiValued", win32more.Foundation.BOOL),
    ]
    return ADS_ATTR_DEF
def _define_ADS_CLASS_DEF_head():
    class ADS_CLASS_DEF(Structure):
        pass
    return ADS_CLASS_DEF
def _define_ADS_CLASS_DEF():
    ADS_CLASS_DEF = win32more.Networking.ActiveDirectory.ADS_CLASS_DEF_head
    ADS_CLASS_DEF._fields_ = [
        ("pszClassName", win32more.Foundation.PWSTR),
        ("dwMandatoryAttrs", UInt32),
        ("ppszMandatoryAttrs", POINTER(win32more.Foundation.PWSTR)),
        ("optionalAttrs", UInt32),
        ("ppszOptionalAttrs", POINTER(POINTER(win32more.Foundation.PWSTR))),
        ("dwNamingAttrs", UInt32),
        ("ppszNamingAttrs", POINTER(POINTER(win32more.Foundation.PWSTR))),
        ("dwSuperClasses", UInt32),
        ("ppszSuperClasses", POINTER(POINTER(win32more.Foundation.PWSTR))),
        ("fIsContainer", win32more.Foundation.BOOL),
    ]
    return ADS_CLASS_DEF
def _define_ADS_SORTKEY_head():
    class ADS_SORTKEY(Structure):
        pass
    return ADS_SORTKEY
def _define_ADS_SORTKEY():
    ADS_SORTKEY = win32more.Networking.ActiveDirectory.ADS_SORTKEY_head
    ADS_SORTKEY._fields_ = [
        ("pszAttrType", win32more.Foundation.PWSTR),
        ("pszReserved", win32more.Foundation.PWSTR),
        ("fReverseorder", win32more.Foundation.BOOLEAN),
    ]
    return ADS_SORTKEY
def _define_ADS_VLV_head():
    class ADS_VLV(Structure):
        pass
    return ADS_VLV
def _define_ADS_VLV():
    ADS_VLV = win32more.Networking.ActiveDirectory.ADS_VLV_head
    ADS_VLV._fields_ = [
        ("dwBeforeCount", UInt32),
        ("dwAfterCount", UInt32),
        ("dwOffset", UInt32),
        ("dwContentCount", UInt32),
        ("pszTarget", win32more.Foundation.PWSTR),
        ("dwContextIDLength", UInt32),
        ("lpContextID", c_char_p_no),
    ]
    return ADS_VLV
ADS_PROPERTY_OPERATION_ENUM = Int32
ADS_PROPERTY_CLEAR = 1
ADS_PROPERTY_UPDATE = 2
ADS_PROPERTY_APPEND = 3
ADS_PROPERTY_DELETE = 4
ADS_SYSTEMFLAG_ENUM = Int32
ADS_SYSTEMFLAG_DISALLOW_DELETE = -2147483648
ADS_SYSTEMFLAG_CONFIG_ALLOW_RENAME = 1073741824
ADS_SYSTEMFLAG_CONFIG_ALLOW_MOVE = 536870912
ADS_SYSTEMFLAG_CONFIG_ALLOW_LIMITED_MOVE = 268435456
ADS_SYSTEMFLAG_DOMAIN_DISALLOW_RENAME = 134217728
ADS_SYSTEMFLAG_DOMAIN_DISALLOW_MOVE = 67108864
ADS_SYSTEMFLAG_CR_NTDS_NC = 1
ADS_SYSTEMFLAG_CR_NTDS_DOMAIN = 2
ADS_SYSTEMFLAG_ATTR_NOT_REPLICATED = 1
ADS_SYSTEMFLAG_ATTR_IS_CONSTRUCTED = 4
ADS_GROUP_TYPE_ENUM = Int32
ADS_GROUP_TYPE_GLOBAL_GROUP = 2
ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP = 4
ADS_GROUP_TYPE_LOCAL_GROUP = 4
ADS_GROUP_TYPE_UNIVERSAL_GROUP = 8
ADS_GROUP_TYPE_SECURITY_ENABLED = -2147483648
ADS_USER_FLAG_ENUM = Int32
ADS_UF_SCRIPT = 1
ADS_UF_ACCOUNTDISABLE = 2
ADS_UF_HOMEDIR_REQUIRED = 8
ADS_UF_LOCKOUT = 16
ADS_UF_PASSWD_NOTREQD = 32
ADS_UF_PASSWD_CANT_CHANGE = 64
ADS_UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED = 128
ADS_UF_TEMP_DUPLICATE_ACCOUNT = 256
ADS_UF_NORMAL_ACCOUNT = 512
ADS_UF_INTERDOMAIN_TRUST_ACCOUNT = 2048
ADS_UF_WORKSTATION_TRUST_ACCOUNT = 4096
ADS_UF_SERVER_TRUST_ACCOUNT = 8192
ADS_UF_DONT_EXPIRE_PASSWD = 65536
ADS_UF_MNS_LOGON_ACCOUNT = 131072
ADS_UF_SMARTCARD_REQUIRED = 262144
ADS_UF_TRUSTED_FOR_DELEGATION = 524288
ADS_UF_NOT_DELEGATED = 1048576
ADS_UF_USE_DES_KEY_ONLY = 2097152
ADS_UF_DONT_REQUIRE_PREAUTH = 4194304
ADS_UF_PASSWORD_EXPIRED = 8388608
ADS_UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION = 16777216
ADS_RIGHTS_ENUM = Int32
ADS_RIGHT_DELETE = 65536
ADS_RIGHT_READ_CONTROL = 131072
ADS_RIGHT_WRITE_DAC = 262144
ADS_RIGHT_WRITE_OWNER = 524288
ADS_RIGHT_SYNCHRONIZE = 1048576
ADS_RIGHT_ACCESS_SYSTEM_SECURITY = 16777216
ADS_RIGHT_GENERIC_READ = -2147483648
ADS_RIGHT_GENERIC_WRITE = 1073741824
ADS_RIGHT_GENERIC_EXECUTE = 536870912
ADS_RIGHT_GENERIC_ALL = 268435456
ADS_RIGHT_DS_CREATE_CHILD = 1
ADS_RIGHT_DS_DELETE_CHILD = 2
ADS_RIGHT_ACTRL_DS_LIST = 4
ADS_RIGHT_DS_SELF = 8
ADS_RIGHT_DS_READ_PROP = 16
ADS_RIGHT_DS_WRITE_PROP = 32
ADS_RIGHT_DS_DELETE_TREE = 64
ADS_RIGHT_DS_LIST_OBJECT = 128
ADS_RIGHT_DS_CONTROL_ACCESS = 256
ADS_ACETYPE_ENUM = Int32
ADS_ACETYPE_ACCESS_ALLOWED = 0
ADS_ACETYPE_ACCESS_DENIED = 1
ADS_ACETYPE_SYSTEM_AUDIT = 2
ADS_ACETYPE_ACCESS_ALLOWED_OBJECT = 5
ADS_ACETYPE_ACCESS_DENIED_OBJECT = 6
ADS_ACETYPE_SYSTEM_AUDIT_OBJECT = 7
ADS_ACETYPE_SYSTEM_ALARM_OBJECT = 8
ADS_ACETYPE_ACCESS_ALLOWED_CALLBACK = 9
ADS_ACETYPE_ACCESS_DENIED_CALLBACK = 10
ADS_ACETYPE_ACCESS_ALLOWED_CALLBACK_OBJECT = 11
ADS_ACETYPE_ACCESS_DENIED_CALLBACK_OBJECT = 12
ADS_ACETYPE_SYSTEM_AUDIT_CALLBACK = 13
ADS_ACETYPE_SYSTEM_ALARM_CALLBACK = 14
ADS_ACETYPE_SYSTEM_AUDIT_CALLBACK_OBJECT = 15
ADS_ACETYPE_SYSTEM_ALARM_CALLBACK_OBJECT = 16
ADS_ACEFLAG_ENUM = Int32
ADS_ACEFLAG_INHERIT_ACE = 2
ADS_ACEFLAG_NO_PROPAGATE_INHERIT_ACE = 4
ADS_ACEFLAG_INHERIT_ONLY_ACE = 8
ADS_ACEFLAG_INHERITED_ACE = 16
ADS_ACEFLAG_VALID_INHERIT_FLAGS = 31
ADS_ACEFLAG_SUCCESSFUL_ACCESS = 64
ADS_ACEFLAG_FAILED_ACCESS = 128
ADS_FLAGTYPE_ENUM = Int32
ADS_FLAG_OBJECT_TYPE_PRESENT = 1
ADS_FLAG_INHERITED_OBJECT_TYPE_PRESENT = 2
ADS_SD_CONTROL_ENUM = Int32
ADS_SD_CONTROL_SE_OWNER_DEFAULTED = 1
ADS_SD_CONTROL_SE_GROUP_DEFAULTED = 2
ADS_SD_CONTROL_SE_DACL_PRESENT = 4
ADS_SD_CONTROL_SE_DACL_DEFAULTED = 8
ADS_SD_CONTROL_SE_SACL_PRESENT = 16
ADS_SD_CONTROL_SE_SACL_DEFAULTED = 32
ADS_SD_CONTROL_SE_DACL_AUTO_INHERIT_REQ = 256
ADS_SD_CONTROL_SE_SACL_AUTO_INHERIT_REQ = 512
ADS_SD_CONTROL_SE_DACL_AUTO_INHERITED = 1024
ADS_SD_CONTROL_SE_SACL_AUTO_INHERITED = 2048
ADS_SD_CONTROL_SE_DACL_PROTECTED = 4096
ADS_SD_CONTROL_SE_SACL_PROTECTED = 8192
ADS_SD_CONTROL_SE_SELF_RELATIVE = 32768
ADS_SD_REVISION_ENUM = Int32
ADS_SD_REVISION_DS = 4
ADS_NAME_TYPE_ENUM = Int32
ADS_NAME_TYPE_1779 = 1
ADS_NAME_TYPE_CANONICAL = 2
ADS_NAME_TYPE_NT4 = 3
ADS_NAME_TYPE_DISPLAY = 4
ADS_NAME_TYPE_DOMAIN_SIMPLE = 5
ADS_NAME_TYPE_ENTERPRISE_SIMPLE = 6
ADS_NAME_TYPE_GUID = 7
ADS_NAME_TYPE_UNKNOWN = 8
ADS_NAME_TYPE_USER_PRINCIPAL_NAME = 9
ADS_NAME_TYPE_CANONICAL_EX = 10
ADS_NAME_TYPE_SERVICE_PRINCIPAL_NAME = 11
ADS_NAME_TYPE_SID_OR_SID_HISTORY_NAME = 12
ADS_NAME_INITTYPE_ENUM = Int32
ADS_NAME_INITTYPE_DOMAIN = 1
ADS_NAME_INITTYPE_SERVER = 2
ADS_NAME_INITTYPE_GC = 3
ADS_OPTION_ENUM = Int32
ADS_OPTION_SERVERNAME = 0
ADS_OPTION_REFERRALS = 1
ADS_OPTION_PAGE_SIZE = 2
ADS_OPTION_SECURITY_MASK = 3
ADS_OPTION_MUTUAL_AUTH_STATUS = 4
ADS_OPTION_QUOTA = 5
ADS_OPTION_PASSWORD_PORTNUMBER = 6
ADS_OPTION_PASSWORD_METHOD = 7
ADS_OPTION_ACCUMULATIVE_MODIFICATION = 8
ADS_OPTION_SKIP_SID_LOOKUP = 9
ADS_SECURITY_INFO_ENUM = Int32
ADS_SECURITY_INFO_OWNER = 1
ADS_SECURITY_INFO_GROUP = 2
ADS_SECURITY_INFO_DACL = 4
ADS_SECURITY_INFO_SACL = 8
ADS_SETTYPE_ENUM = Int32
ADS_SETTYPE_FULL = 1
ADS_SETTYPE_PROVIDER = 2
ADS_SETTYPE_SERVER = 3
ADS_SETTYPE_DN = 4
ADS_FORMAT_ENUM = Int32
ADS_FORMAT_WINDOWS = 1
ADS_FORMAT_WINDOWS_NO_SERVER = 2
ADS_FORMAT_WINDOWS_DN = 3
ADS_FORMAT_WINDOWS_PARENT = 4
ADS_FORMAT_X500 = 5
ADS_FORMAT_X500_NO_SERVER = 6
ADS_FORMAT_X500_DN = 7
ADS_FORMAT_X500_PARENT = 8
ADS_FORMAT_SERVER = 9
ADS_FORMAT_PROVIDER = 10
ADS_FORMAT_LEAF = 11
ADS_DISPLAY_ENUM = Int32
ADS_DISPLAY_FULL = 1
ADS_DISPLAY_VALUE_ONLY = 2
ADS_ESCAPE_MODE_ENUM = Int32
ADS_ESCAPEDMODE_DEFAULT = 1
ADS_ESCAPEDMODE_ON = 2
ADS_ESCAPEDMODE_OFF = 3
ADS_ESCAPEDMODE_OFF_EX = 4
ADS_PATHTYPE_ENUM = Int32
ADS_PATH_FILE = 1
ADS_PATH_FILESHARE = 2
ADS_PATH_REGISTRY = 3
ADS_SD_FORMAT_ENUM = Int32
ADS_SD_FORMAT_IID = 1
ADS_SD_FORMAT_RAW = 2
ADS_SD_FORMAT_HEXSTRING = 3
def _define_IADs_head():
    class IADs(win32more.System.Com.IDispatch_head):
        Guid = Guid('fd8256d0-fd15-11ce-abc4-02608c9e7553')
    return IADs
def _define_IADs():
    IADs = win32more.Networking.ActiveDirectory.IADs_head
    IADs.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'retval'),)))
    IADs.get_Class = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Class', ((1, 'retval'),)))
    IADs.get_GUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_GUID', ((1, 'retval'),)))
    IADs.get_ADsPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_ADsPath', ((1, 'retval'),)))
    IADs.get_Parent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_Parent', ((1, 'retval'),)))
    IADs.get_Schema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_Schema', ((1, 'retval'),)))
    IADs.GetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'GetInfo', ()))
    IADs.SetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'SetInfo', ()))
    IADs.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'Get', ((1, 'bstrName'),(1, 'pvProp'),)))
    IADs.Put = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(16, 'Put', ((1, 'bstrName'),(1, 'vProp'),)))
    IADs.GetEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(17, 'GetEx', ((1, 'bstrName'),(1, 'pvProp'),)))
    IADs.PutEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(18, 'PutEx', ((1, 'lnControlCode'),(1, 'bstrName'),(1, 'vProp'),)))
    IADs.GetInfoEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,Int32, use_last_error=False)(19, 'GetInfoEx', ((1, 'vProperties'),(1, 'lnReserved'),)))
    win32more.System.Com.IDispatch
    return IADs
def _define_IADsContainer_head():
    class IADsContainer(win32more.System.Com.IDispatch_head):
        Guid = Guid('001677d0-fd16-11ce-abc4-02608c9e7553')
    return IADsContainer
def _define_IADsContainer():
    IADsContainer = win32more.Networking.ActiveDirectory.IADsContainer_head
    IADsContainer.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'retval'),)))
    IADsContainer.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'retval'),)))
    IADsContainer.get_Filter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'get_Filter', ((1, 'pVar'),)))
    IADsContainer.put_Filter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(10, 'put_Filter', ((1, 'Var'),)))
    IADsContainer.get_Hints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'get_Hints', ((1, 'pvFilter'),)))
    IADsContainer.put_Hints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(12, 'put_Hints', ((1, 'vHints'),)))
    IADsContainer.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(13, 'GetObject', ((1, 'ClassName'),(1, 'RelativeName'),(1, 'ppObject'),)))
    IADsContainer.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(14, 'Create', ((1, 'ClassName'),(1, 'RelativeName'),(1, 'ppObject'),)))
    IADsContainer.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(15, 'Delete', ((1, 'bstrClassName'),(1, 'bstrRelativeName'),)))
    IADsContainer.CopyHere = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(16, 'CopyHere', ((1, 'SourceName'),(1, 'NewName'),(1, 'ppObject'),)))
    IADsContainer.MoveHere = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(17, 'MoveHere', ((1, 'SourceName'),(1, 'NewName'),(1, 'ppObject'),)))
    win32more.System.Com.IDispatch
    return IADsContainer
def _define_IADsCollection_head():
    class IADsCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('72b945e0-253b-11cf-a988-00aa006bc149')
    return IADsCollection
def _define_IADsCollection():
    IADsCollection = win32more.Networking.ActiveDirectory.IADsCollection_head
    IADsCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppEnumerator'),)))
    IADsCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(8, 'Add', ((1, 'bstrName'),(1, 'vItem'),)))
    IADsCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'Remove', ((1, 'bstrItemToBeRemoved'),)))
    IADsCollection.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'GetObject', ((1, 'bstrName'),(1, 'pvItem'),)))
    win32more.System.Com.IDispatch
    return IADsCollection
def _define_IADsMembers_head():
    class IADsMembers(win32more.System.Com.IDispatch_head):
        Guid = Guid('451a0030-72ec-11cf-b03b-00aa006e0975')
    return IADsMembers
def _define_IADsMembers():
    IADsMembers = win32more.Networking.ActiveDirectory.IADsMembers_head
    IADsMembers.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'plCount'),)))
    IADsMembers.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'ppEnumerator'),)))
    IADsMembers.get_Filter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'get_Filter', ((1, 'pvFilter'),)))
    IADsMembers.put_Filter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(10, 'put_Filter', ((1, 'pvFilter'),)))
    win32more.System.Com.IDispatch
    return IADsMembers
def _define_IADsPropertyList_head():
    class IADsPropertyList(win32more.System.Com.IDispatch_head):
        Guid = Guid('c6f602b6-8f69-11d0-8528-00c04fd8d503')
    return IADsPropertyList
def _define_IADsPropertyList():
    IADsPropertyList = win32more.Networking.ActiveDirectory.IADsPropertyList_head
    IADsPropertyList.get_PropertyCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_PropertyCount', ((1, 'plCount'),)))
    IADsPropertyList.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'Next', ((1, 'pVariant'),)))
    IADsPropertyList.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'Skip', ((1, 'cElements'),)))
    IADsPropertyList.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Reset', ()))
    IADsPropertyList.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'Item', ((1, 'varIndex'),(1, 'pVariant'),)))
    IADsPropertyList.GetPropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(12, 'GetPropertyItem', ((1, 'bstrName'),(1, 'lnADsType'),(1, 'pVariant'),)))
    IADsPropertyList.PutPropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(13, 'PutPropertyItem', ((1, 'varData'),)))
    IADsPropertyList.ResetPropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(14, 'ResetPropertyItem', ((1, 'varEntry'),)))
    IADsPropertyList.PurgePropertyList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'PurgePropertyList', ()))
    win32more.System.Com.IDispatch
    return IADsPropertyList
def _define_IADsPropertyEntry_head():
    class IADsPropertyEntry(win32more.System.Com.IDispatch_head):
        Guid = Guid('05792c8e-941f-11d0-8529-00c04fd8d503')
    return IADsPropertyEntry
def _define_IADsPropertyEntry():
    IADsPropertyEntry = win32more.Networking.ActiveDirectory.IADsPropertyEntry_head
    IADsPropertyEntry.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Clear', ()))
    IADsPropertyEntry.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Name', ((1, 'retval'),)))
    IADsPropertyEntry.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'put_Name', ((1, 'bstrName'),)))
    IADsPropertyEntry.get_ADsType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_ADsType', ((1, 'retval'),)))
    IADsPropertyEntry.put_ADsType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'put_ADsType', ((1, 'lnADsType'),)))
    IADsPropertyEntry.get_ControlCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_ControlCode', ((1, 'retval'),)))
    IADsPropertyEntry.put_ControlCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'put_ControlCode', ((1, 'lnControlCode'),)))
    IADsPropertyEntry.get_Values = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(14, 'get_Values', ((1, 'retval'),)))
    IADsPropertyEntry.put_Values = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(15, 'put_Values', ((1, 'vValues'),)))
    win32more.System.Com.IDispatch
    return IADsPropertyEntry
def _define_IADsPropertyValue_head():
    class IADsPropertyValue(win32more.System.Com.IDispatch_head):
        Guid = Guid('79fa9ad0-a97c-11d0-8534-00c04fd8d503')
    return IADsPropertyValue
def _define_IADsPropertyValue():
    IADsPropertyValue = win32more.Networking.ActiveDirectory.IADsPropertyValue_head
    IADsPropertyValue.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Clear', ()))
    IADsPropertyValue.get_ADsType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_ADsType', ((1, 'retval'),)))
    IADsPropertyValue.put_ADsType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'put_ADsType', ((1, 'lnADsType'),)))
    IADsPropertyValue.get_DNString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_DNString', ((1, 'retval'),)))
    IADsPropertyValue.put_DNString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'put_DNString', ((1, 'bstrDNString'),)))
    IADsPropertyValue.get_CaseExactString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_CaseExactString', ((1, 'retval'),)))
    IADsPropertyValue.put_CaseExactString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(13, 'put_CaseExactString', ((1, 'bstrCaseExactString'),)))
    IADsPropertyValue.get_CaseIgnoreString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_CaseIgnoreString', ((1, 'retval'),)))
    IADsPropertyValue.put_CaseIgnoreString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_CaseIgnoreString', ((1, 'bstrCaseIgnoreString'),)))
    IADsPropertyValue.get_PrintableString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_PrintableString', ((1, 'retval'),)))
    IADsPropertyValue.put_PrintableString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(17, 'put_PrintableString', ((1, 'bstrPrintableString'),)))
    IADsPropertyValue.get_NumericString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_NumericString', ((1, 'retval'),)))
    IADsPropertyValue.put_NumericString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(19, 'put_NumericString', ((1, 'bstrNumericString'),)))
    IADsPropertyValue.get_Boolean = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_Boolean', ((1, 'retval'),)))
    IADsPropertyValue.put_Boolean = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(21, 'put_Boolean', ((1, 'lnBoolean'),)))
    IADsPropertyValue.get_Integer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(22, 'get_Integer', ((1, 'retval'),)))
    IADsPropertyValue.put_Integer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(23, 'put_Integer', ((1, 'lnInteger'),)))
    IADsPropertyValue.get_OctetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(24, 'get_OctetString', ((1, 'retval'),)))
    IADsPropertyValue.put_OctetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(25, 'put_OctetString', ((1, 'vOctetString'),)))
    IADsPropertyValue.get_SecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(26, 'get_SecurityDescriptor', ((1, 'retval'),)))
    IADsPropertyValue.put_SecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(27, 'put_SecurityDescriptor', ((1, 'pSecurityDescriptor'),)))
    IADsPropertyValue.get_LargeInteger = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(28, 'get_LargeInteger', ((1, 'retval'),)))
    IADsPropertyValue.put_LargeInteger = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(29, 'put_LargeInteger', ((1, 'pLargeInteger'),)))
    IADsPropertyValue.get_UTCTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(30, 'get_UTCTime', ((1, 'retval'),)))
    IADsPropertyValue.put_UTCTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(31, 'put_UTCTime', ((1, 'daUTCTime'),)))
    win32more.System.Com.IDispatch
    return IADsPropertyValue
def _define_IADsPropertyValue2_head():
    class IADsPropertyValue2(win32more.System.Com.IDispatch_head):
        Guid = Guid('306e831c-5bc7-11d1-a3b8-00c04fb950dc')
    return IADsPropertyValue2
def _define_IADsPropertyValue2():
    IADsPropertyValue2 = win32more.Networking.ActiveDirectory.IADsPropertyValue2_head
    IADsPropertyValue2.GetObjectProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'GetObjectProperty', ((1, 'lnADsType'),(1, 'pvProp'),)))
    IADsPropertyValue2.PutObjectProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT, use_last_error=False)(8, 'PutObjectProperty', ((1, 'lnADsType'),(1, 'vProp'),)))
    win32more.System.Com.IDispatch
    return IADsPropertyValue2
def _define_IPrivateDispatch_head():
    class IPrivateDispatch(win32more.System.Com.IUnknown_head):
        Guid = Guid('86ab4bbe-65f6-11d1-8c13-00c04fd8d503')
    return IPrivateDispatch
def _define_IPrivateDispatch():
    IPrivateDispatch = win32more.Networking.ActiveDirectory.IPrivateDispatch_head
    IPrivateDispatch.ADSIInitializeDispatchManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'ADSIInitializeDispatchManager', ((1, 'dwExtensionId'),)))
    IPrivateDispatch.ADSIGetTypeInfoCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'ADSIGetTypeInfoCount', ((1, 'pctinfo'),)))
    IPrivateDispatch.ADSIGetTypeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.Com.ITypeInfo_head), use_last_error=False)(5, 'ADSIGetTypeInfo', ((1, 'itinfo'),(1, 'lcid'),(1, 'pptinfo'),)))
    IPrivateDispatch.ADSIGetIDsOfNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(POINTER(UInt16)),UInt32,UInt32,POINTER(Int32), use_last_error=False)(6, 'ADSIGetIDsOfNames', ((1, 'riid'),(1, 'rgszNames'),(1, 'cNames'),(1, 'lcid'),(1, 'rgdispid'),)))
    IPrivateDispatch.ADSIInvoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Guid),UInt32,UInt16,POINTER(win32more.System.Com.DISPPARAMS_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.EXCEPINFO_head),POINTER(UInt32), use_last_error=False)(7, 'ADSIInvoke', ((1, 'dispidMember'),(1, 'riid'),(1, 'lcid'),(1, 'wFlags'),(1, 'pdispparams'),(1, 'pvarResult'),(1, 'pexcepinfo'),(1, 'puArgErr'),)))
    win32more.System.Com.IUnknown
    return IPrivateDispatch
def _define_IPrivateUnknown_head():
    class IPrivateUnknown(win32more.System.Com.IUnknown_head):
        Guid = Guid('89126bab-6ead-11d1-8c18-00c04fd8d503')
    return IPrivateUnknown
def _define_IPrivateUnknown():
    IPrivateUnknown = win32more.Networking.ActiveDirectory.IPrivateUnknown_head
    IPrivateUnknown.ADSIInitializeObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32, use_last_error=False)(3, 'ADSIInitializeObject', ((1, 'lpszUserName'),(1, 'lpszPassword'),(1, 'lnReserved'),)))
    IPrivateUnknown.ADSIReleaseObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'ADSIReleaseObject', ()))
    win32more.System.Com.IUnknown
    return IPrivateUnknown
def _define_IADsExtension_head():
    class IADsExtension(win32more.System.Com.IUnknown_head):
        Guid = Guid('3d35553c-d2b0-11d1-b17b-0000f87593a0')
    return IADsExtension
def _define_IADsExtension():
    IADsExtension = win32more.Networking.ActiveDirectory.IADsExtension_head
    IADsExtension.Operate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(3, 'Operate', ((1, 'dwCode'),(1, 'varData1'),(1, 'varData2'),(1, 'varData3'),)))
    IADsExtension.PrivateGetIDsOfNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(POINTER(UInt16)),UInt32,UInt32,POINTER(Int32), use_last_error=False)(4, 'PrivateGetIDsOfNames', ((1, 'riid'),(1, 'rgszNames'),(1, 'cNames'),(1, 'lcid'),(1, 'rgDispid'),)))
    IADsExtension.PrivateInvoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Guid),UInt32,UInt16,POINTER(win32more.System.Com.DISPPARAMS_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.EXCEPINFO_head),POINTER(UInt32), use_last_error=False)(5, 'PrivateInvoke', ((1, 'dispidMember'),(1, 'riid'),(1, 'lcid'),(1, 'wFlags'),(1, 'pdispparams'),(1, 'pvarResult'),(1, 'pexcepinfo'),(1, 'puArgErr'),)))
    win32more.System.Com.IUnknown
    return IADsExtension
def _define_IADsDeleteOps_head():
    class IADsDeleteOps(win32more.System.Com.IDispatch_head):
        Guid = Guid('b2bd0902-8878-11d1-8c21-00c04fd8d503')
    return IADsDeleteOps
def _define_IADsDeleteOps():
    IADsDeleteOps = win32more.Networking.ActiveDirectory.IADsDeleteOps_head
    IADsDeleteOps.DeleteObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(7, 'DeleteObject', ((1, 'lnFlags'),)))
    win32more.System.Com.IDispatch
    return IADsDeleteOps
def _define_IADsNamespaces_head():
    class IADsNamespaces(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('28b96ba0-b330-11cf-a9ad-00aa006bc149')
    return IADsNamespaces
def _define_IADsNamespaces():
    IADsNamespaces = win32more.Networking.ActiveDirectory.IADsNamespaces_head
    IADsNamespaces.get_DefaultContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_DefaultContainer', ((1, 'retval'),)))
    IADsNamespaces.put_DefaultContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(21, 'put_DefaultContainer', ((1, 'bstrDefaultContainer'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsNamespaces
def _define_IADsClass_head():
    class IADsClass(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('c8f93dd0-4ae0-11cf-9e73-00aa004a5691')
    return IADsClass
def _define_IADsClass():
    IADsClass = win32more.Networking.ActiveDirectory.IADsClass_head
    IADsClass.get_PrimaryInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_PrimaryInterface', ((1, 'retval'),)))
    IADsClass.get_CLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_CLSID', ((1, 'retval'),)))
    IADsClass.put_CLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(22, 'put_CLSID', ((1, 'bstrCLSID'),)))
    IADsClass.get_OID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_OID', ((1, 'retval'),)))
    IADsClass.put_OID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(24, 'put_OID', ((1, 'bstrOID'),)))
    IADsClass.get_Abstract = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(25, 'get_Abstract', ((1, 'retval'),)))
    IADsClass.put_Abstract = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(26, 'put_Abstract', ((1, 'fAbstract'),)))
    IADsClass.get_Auxiliary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(27, 'get_Auxiliary', ((1, 'retval'),)))
    IADsClass.put_Auxiliary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(28, 'put_Auxiliary', ((1, 'fAuxiliary'),)))
    IADsClass.get_MandatoryProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(29, 'get_MandatoryProperties', ((1, 'retval'),)))
    IADsClass.put_MandatoryProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(30, 'put_MandatoryProperties', ((1, 'vMandatoryProperties'),)))
    IADsClass.get_OptionalProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(31, 'get_OptionalProperties', ((1, 'retval'),)))
    IADsClass.put_OptionalProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(32, 'put_OptionalProperties', ((1, 'vOptionalProperties'),)))
    IADsClass.get_NamingProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(33, 'get_NamingProperties', ((1, 'retval'),)))
    IADsClass.put_NamingProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(34, 'put_NamingProperties', ((1, 'vNamingProperties'),)))
    IADsClass.get_DerivedFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(35, 'get_DerivedFrom', ((1, 'retval'),)))
    IADsClass.put_DerivedFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(36, 'put_DerivedFrom', ((1, 'vDerivedFrom'),)))
    IADsClass.get_AuxDerivedFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(37, 'get_AuxDerivedFrom', ((1, 'retval'),)))
    IADsClass.put_AuxDerivedFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(38, 'put_AuxDerivedFrom', ((1, 'vAuxDerivedFrom'),)))
    IADsClass.get_PossibleSuperiors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(39, 'get_PossibleSuperiors', ((1, 'retval'),)))
    IADsClass.put_PossibleSuperiors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(40, 'put_PossibleSuperiors', ((1, 'vPossibleSuperiors'),)))
    IADsClass.get_Containment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(41, 'get_Containment', ((1, 'retval'),)))
    IADsClass.put_Containment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(42, 'put_Containment', ((1, 'vContainment'),)))
    IADsClass.get_Container = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(43, 'get_Container', ((1, 'retval'),)))
    IADsClass.put_Container = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(44, 'put_Container', ((1, 'fContainer'),)))
    IADsClass.get_HelpFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(45, 'get_HelpFileName', ((1, 'retval'),)))
    IADsClass.put_HelpFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(46, 'put_HelpFileName', ((1, 'bstrHelpFileName'),)))
    IADsClass.get_HelpFileContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(47, 'get_HelpFileContext', ((1, 'retval'),)))
    IADsClass.put_HelpFileContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(48, 'put_HelpFileContext', ((1, 'lnHelpFileContext'),)))
    IADsClass.Qualifiers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.IADsCollection_head), use_last_error=False)(49, 'Qualifiers', ((1, 'ppQualifiers'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsClass
def _define_IADsProperty_head():
    class IADsProperty(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('c8f93dd3-4ae0-11cf-9e73-00aa004a5691')
    return IADsProperty
def _define_IADsProperty():
    IADsProperty = win32more.Networking.ActiveDirectory.IADsProperty_head
    IADsProperty.get_OID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_OID', ((1, 'retval'),)))
    IADsProperty.put_OID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(21, 'put_OID', ((1, 'bstrOID'),)))
    IADsProperty.get_Syntax = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_Syntax', ((1, 'retval'),)))
    IADsProperty.put_Syntax = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_Syntax', ((1, 'bstrSyntax'),)))
    IADsProperty.get_MaxRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(24, 'get_MaxRange', ((1, 'retval'),)))
    IADsProperty.put_MaxRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(25, 'put_MaxRange', ((1, 'lnMaxRange'),)))
    IADsProperty.get_MinRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(26, 'get_MinRange', ((1, 'retval'),)))
    IADsProperty.put_MinRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(27, 'put_MinRange', ((1, 'lnMinRange'),)))
    IADsProperty.get_MultiValued = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(28, 'get_MultiValued', ((1, 'retval'),)))
    IADsProperty.put_MultiValued = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(29, 'put_MultiValued', ((1, 'fMultiValued'),)))
    IADsProperty.Qualifiers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.IADsCollection_head), use_last_error=False)(30, 'Qualifiers', ((1, 'ppQualifiers'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsProperty
def _define_IADsSyntax_head():
    class IADsSyntax(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('c8f93dd2-4ae0-11cf-9e73-00aa004a5691')
    return IADsSyntax
def _define_IADsSyntax():
    IADsSyntax = win32more.Networking.ActiveDirectory.IADsSyntax_head
    IADsSyntax.get_OleAutoDataType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_OleAutoDataType', ((1, 'retval'),)))
    IADsSyntax.put_OleAutoDataType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(21, 'put_OleAutoDataType', ((1, 'lnOleAutoDataType'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsSyntax
def _define_IADsLocality_head():
    class IADsLocality(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('a05e03a2-effe-11cf-8abc-00c04fd8d503')
    return IADsLocality
def _define_IADsLocality():
    IADsLocality = win32more.Networking.ActiveDirectory.IADsLocality_head
    IADsLocality.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_Description', ((1, 'retval'),)))
    IADsLocality.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(21, 'put_Description', ((1, 'bstrDescription'),)))
    IADsLocality.get_LocalityName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_LocalityName', ((1, 'retval'),)))
    IADsLocality.put_LocalityName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_LocalityName', ((1, 'bstrLocalityName'),)))
    IADsLocality.get_PostalAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_PostalAddress', ((1, 'retval'),)))
    IADsLocality.put_PostalAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_PostalAddress', ((1, 'bstrPostalAddress'),)))
    IADsLocality.get_SeeAlso = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(26, 'get_SeeAlso', ((1, 'retval'),)))
    IADsLocality.put_SeeAlso = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(27, 'put_SeeAlso', ((1, 'vSeeAlso'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsLocality
def _define_IADsO_head():
    class IADsO(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('a1cd2dc6-effe-11cf-8abc-00c04fd8d503')
    return IADsO
def _define_IADsO():
    IADsO = win32more.Networking.ActiveDirectory.IADsO_head
    IADsO.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_Description', ((1, 'retval'),)))
    IADsO.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(21, 'put_Description', ((1, 'bstrDescription'),)))
    IADsO.get_LocalityName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_LocalityName', ((1, 'retval'),)))
    IADsO.put_LocalityName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_LocalityName', ((1, 'bstrLocalityName'),)))
    IADsO.get_PostalAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_PostalAddress', ((1, 'retval'),)))
    IADsO.put_PostalAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_PostalAddress', ((1, 'bstrPostalAddress'),)))
    IADsO.get_TelephoneNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'get_TelephoneNumber', ((1, 'retval'),)))
    IADsO.put_TelephoneNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(27, 'put_TelephoneNumber', ((1, 'bstrTelephoneNumber'),)))
    IADsO.get_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(28, 'get_FaxNumber', ((1, 'retval'),)))
    IADsO.put_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(29, 'put_FaxNumber', ((1, 'bstrFaxNumber'),)))
    IADsO.get_SeeAlso = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(30, 'get_SeeAlso', ((1, 'retval'),)))
    IADsO.put_SeeAlso = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(31, 'put_SeeAlso', ((1, 'vSeeAlso'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsO
def _define_IADsOU_head():
    class IADsOU(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('a2f733b8-effe-11cf-8abc-00c04fd8d503')
    return IADsOU
def _define_IADsOU():
    IADsOU = win32more.Networking.ActiveDirectory.IADsOU_head
    IADsOU.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_Description', ((1, 'retval'),)))
    IADsOU.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(21, 'put_Description', ((1, 'bstrDescription'),)))
    IADsOU.get_LocalityName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_LocalityName', ((1, 'retval'),)))
    IADsOU.put_LocalityName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_LocalityName', ((1, 'bstrLocalityName'),)))
    IADsOU.get_PostalAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_PostalAddress', ((1, 'retval'),)))
    IADsOU.put_PostalAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_PostalAddress', ((1, 'bstrPostalAddress'),)))
    IADsOU.get_TelephoneNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'get_TelephoneNumber', ((1, 'retval'),)))
    IADsOU.put_TelephoneNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(27, 'put_TelephoneNumber', ((1, 'bstrTelephoneNumber'),)))
    IADsOU.get_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(28, 'get_FaxNumber', ((1, 'retval'),)))
    IADsOU.put_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(29, 'put_FaxNumber', ((1, 'bstrFaxNumber'),)))
    IADsOU.get_SeeAlso = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(30, 'get_SeeAlso', ((1, 'retval'),)))
    IADsOU.put_SeeAlso = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(31, 'put_SeeAlso', ((1, 'vSeeAlso'),)))
    IADsOU.get_BusinessCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(32, 'get_BusinessCategory', ((1, 'retval'),)))
    IADsOU.put_BusinessCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(33, 'put_BusinessCategory', ((1, 'bstrBusinessCategory'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsOU
def _define_IADsDomain_head():
    class IADsDomain(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('00e4c220-fd16-11ce-abc4-02608c9e7553')
    return IADsDomain
def _define_IADsDomain():
    IADsDomain = win32more.Networking.ActiveDirectory.IADsDomain_head
    IADsDomain.get_IsWorkgroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(20, 'get_IsWorkgroup', ((1, 'retval'),)))
    IADsDomain.get_MinPasswordLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'get_MinPasswordLength', ((1, 'retval'),)))
    IADsDomain.put_MinPasswordLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(22, 'put_MinPasswordLength', ((1, 'lnMinPasswordLength'),)))
    IADsDomain.get_MinPasswordAge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_MinPasswordAge', ((1, 'retval'),)))
    IADsDomain.put_MinPasswordAge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_MinPasswordAge', ((1, 'lnMinPasswordAge'),)))
    IADsDomain.get_MaxPasswordAge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'get_MaxPasswordAge', ((1, 'retval'),)))
    IADsDomain.put_MaxPasswordAge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(26, 'put_MaxPasswordAge', ((1, 'lnMaxPasswordAge'),)))
    IADsDomain.get_MaxBadPasswordsAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(27, 'get_MaxBadPasswordsAllowed', ((1, 'retval'),)))
    IADsDomain.put_MaxBadPasswordsAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(28, 'put_MaxBadPasswordsAllowed', ((1, 'lnMaxBadPasswordsAllowed'),)))
    IADsDomain.get_PasswordHistoryLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(29, 'get_PasswordHistoryLength', ((1, 'retval'),)))
    IADsDomain.put_PasswordHistoryLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(30, 'put_PasswordHistoryLength', ((1, 'lnPasswordHistoryLength'),)))
    IADsDomain.get_PasswordAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(31, 'get_PasswordAttributes', ((1, 'retval'),)))
    IADsDomain.put_PasswordAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(32, 'put_PasswordAttributes', ((1, 'lnPasswordAttributes'),)))
    IADsDomain.get_AutoUnlockInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(33, 'get_AutoUnlockInterval', ((1, 'retval'),)))
    IADsDomain.put_AutoUnlockInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(34, 'put_AutoUnlockInterval', ((1, 'lnAutoUnlockInterval'),)))
    IADsDomain.get_LockoutObservationInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(35, 'get_LockoutObservationInterval', ((1, 'retval'),)))
    IADsDomain.put_LockoutObservationInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(36, 'put_LockoutObservationInterval', ((1, 'lnLockoutObservationInterval'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsDomain
def _define_IADsComputer_head():
    class IADsComputer(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('efe3cc70-1d9f-11cf-b1f3-02608c9e7553')
    return IADsComputer
def _define_IADsComputer():
    IADsComputer = win32more.Networking.ActiveDirectory.IADsComputer_head
    IADsComputer.get_ComputerID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_ComputerID', ((1, 'retval'),)))
    IADsComputer.get_Site = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_Site', ((1, 'retval'),)))
    IADsComputer.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_Description', ((1, 'retval'),)))
    IADsComputer.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_Description', ((1, 'bstrDescription'),)))
    IADsComputer.get_Location = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_Location', ((1, 'retval'),)))
    IADsComputer.put_Location = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_Location', ((1, 'bstrLocation'),)))
    IADsComputer.get_PrimaryUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'get_PrimaryUser', ((1, 'retval'),)))
    IADsComputer.put_PrimaryUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(27, 'put_PrimaryUser', ((1, 'bstrPrimaryUser'),)))
    IADsComputer.get_Owner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(28, 'get_Owner', ((1, 'retval'),)))
    IADsComputer.put_Owner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(29, 'put_Owner', ((1, 'bstrOwner'),)))
    IADsComputer.get_Division = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(30, 'get_Division', ((1, 'retval'),)))
    IADsComputer.put_Division = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(31, 'put_Division', ((1, 'bstrDivision'),)))
    IADsComputer.get_Department = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(32, 'get_Department', ((1, 'retval'),)))
    IADsComputer.put_Department = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(33, 'put_Department', ((1, 'bstrDepartment'),)))
    IADsComputer.get_Role = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(34, 'get_Role', ((1, 'retval'),)))
    IADsComputer.put_Role = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(35, 'put_Role', ((1, 'bstrRole'),)))
    IADsComputer.get_OperatingSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'get_OperatingSystem', ((1, 'retval'),)))
    IADsComputer.put_OperatingSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'put_OperatingSystem', ((1, 'bstrOperatingSystem'),)))
    IADsComputer.get_OperatingSystemVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(38, 'get_OperatingSystemVersion', ((1, 'retval'),)))
    IADsComputer.put_OperatingSystemVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(39, 'put_OperatingSystemVersion', ((1, 'bstrOperatingSystemVersion'),)))
    IADsComputer.get_Model = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(40, 'get_Model', ((1, 'retval'),)))
    IADsComputer.put_Model = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(41, 'put_Model', ((1, 'bstrModel'),)))
    IADsComputer.get_Processor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(42, 'get_Processor', ((1, 'retval'),)))
    IADsComputer.put_Processor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(43, 'put_Processor', ((1, 'bstrProcessor'),)))
    IADsComputer.get_ProcessorCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(44, 'get_ProcessorCount', ((1, 'retval'),)))
    IADsComputer.put_ProcessorCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(45, 'put_ProcessorCount', ((1, 'bstrProcessorCount'),)))
    IADsComputer.get_MemorySize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(46, 'get_MemorySize', ((1, 'retval'),)))
    IADsComputer.put_MemorySize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(47, 'put_MemorySize', ((1, 'bstrMemorySize'),)))
    IADsComputer.get_StorageCapacity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(48, 'get_StorageCapacity', ((1, 'retval'),)))
    IADsComputer.put_StorageCapacity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(49, 'put_StorageCapacity', ((1, 'bstrStorageCapacity'),)))
    IADsComputer.get_NetAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(50, 'get_NetAddresses', ((1, 'retval'),)))
    IADsComputer.put_NetAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(51, 'put_NetAddresses', ((1, 'vNetAddresses'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsComputer
def _define_IADsComputerOperations_head():
    class IADsComputerOperations(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('ef497680-1d9f-11cf-b1f3-02608c9e7553')
    return IADsComputerOperations
def _define_IADsComputerOperations():
    IADsComputerOperations = win32more.Networking.ActiveDirectory.IADsComputerOperations_head
    IADsComputerOperations.Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(20, 'Status', ((1, 'ppObject'),)))
    IADsComputerOperations.Shutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(21, 'Shutdown', ((1, 'bReboot'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsComputerOperations
def _define_IADsGroup_head():
    class IADsGroup(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('27636b00-410f-11cf-b1ff-02608c9e7553')
    return IADsGroup
def _define_IADsGroup():
    IADsGroup = win32more.Networking.ActiveDirectory.IADsGroup_head
    IADsGroup.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_Description', ((1, 'retval'),)))
    IADsGroup.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(21, 'put_Description', ((1, 'bstrDescription'),)))
    IADsGroup.Members = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.IADsMembers_head), use_last_error=False)(22, 'Members', ((1, 'ppMembers'),)))
    IADsGroup.IsMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(23, 'IsMember', ((1, 'bstrMember'),(1, 'bMember'),)))
    IADsGroup.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(24, 'Add', ((1, 'bstrNewItem'),)))
    IADsGroup.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'Remove', ((1, 'bstrItemToBeRemoved'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsGroup
def _define_IADsUser_head():
    class IADsUser(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('3e37e320-17e2-11cf-abc4-02608c9e7553')
    return IADsUser
def _define_IADsUser():
    IADsUser = win32more.Networking.ActiveDirectory.IADsUser_head
    IADsUser.get_BadLoginAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_BadLoginAddress', ((1, 'retval'),)))
    IADsUser.get_BadLoginCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'get_BadLoginCount', ((1, 'retval'),)))
    IADsUser.get_LastLogin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(22, 'get_LastLogin', ((1, 'retval'),)))
    IADsUser.get_LastLogoff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(23, 'get_LastLogoff', ((1, 'retval'),)))
    IADsUser.get_LastFailedLogin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(24, 'get_LastFailedLogin', ((1, 'retval'),)))
    IADsUser.get_PasswordLastChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(25, 'get_PasswordLastChanged', ((1, 'retval'),)))
    IADsUser.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'get_Description', ((1, 'retval'),)))
    IADsUser.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(27, 'put_Description', ((1, 'bstrDescription'),)))
    IADsUser.get_Division = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(28, 'get_Division', ((1, 'retval'),)))
    IADsUser.put_Division = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(29, 'put_Division', ((1, 'bstrDivision'),)))
    IADsUser.get_Department = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(30, 'get_Department', ((1, 'retval'),)))
    IADsUser.put_Department = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(31, 'put_Department', ((1, 'bstrDepartment'),)))
    IADsUser.get_EmployeeID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(32, 'get_EmployeeID', ((1, 'retval'),)))
    IADsUser.put_EmployeeID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(33, 'put_EmployeeID', ((1, 'bstrEmployeeID'),)))
    IADsUser.get_FullName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(34, 'get_FullName', ((1, 'retval'),)))
    IADsUser.put_FullName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(35, 'put_FullName', ((1, 'bstrFullName'),)))
    IADsUser.get_FirstName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'get_FirstName', ((1, 'retval'),)))
    IADsUser.put_FirstName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'put_FirstName', ((1, 'bstrFirstName'),)))
    IADsUser.get_LastName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(38, 'get_LastName', ((1, 'retval'),)))
    IADsUser.put_LastName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(39, 'put_LastName', ((1, 'bstrLastName'),)))
    IADsUser.get_OtherName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(40, 'get_OtherName', ((1, 'retval'),)))
    IADsUser.put_OtherName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(41, 'put_OtherName', ((1, 'bstrOtherName'),)))
    IADsUser.get_NamePrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(42, 'get_NamePrefix', ((1, 'retval'),)))
    IADsUser.put_NamePrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(43, 'put_NamePrefix', ((1, 'bstrNamePrefix'),)))
    IADsUser.get_NameSuffix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(44, 'get_NameSuffix', ((1, 'retval'),)))
    IADsUser.put_NameSuffix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(45, 'put_NameSuffix', ((1, 'bstrNameSuffix'),)))
    IADsUser.get_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(46, 'get_Title', ((1, 'retval'),)))
    IADsUser.put_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(47, 'put_Title', ((1, 'bstrTitle'),)))
    IADsUser.get_Manager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(48, 'get_Manager', ((1, 'retval'),)))
    IADsUser.put_Manager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(49, 'put_Manager', ((1, 'bstrManager'),)))
    IADsUser.get_TelephoneHome = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(50, 'get_TelephoneHome', ((1, 'retval'),)))
    IADsUser.put_TelephoneHome = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(51, 'put_TelephoneHome', ((1, 'vTelephoneHome'),)))
    IADsUser.get_TelephoneMobile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(52, 'get_TelephoneMobile', ((1, 'retval'),)))
    IADsUser.put_TelephoneMobile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(53, 'put_TelephoneMobile', ((1, 'vTelephoneMobile'),)))
    IADsUser.get_TelephoneNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(54, 'get_TelephoneNumber', ((1, 'retval'),)))
    IADsUser.put_TelephoneNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(55, 'put_TelephoneNumber', ((1, 'vTelephoneNumber'),)))
    IADsUser.get_TelephonePager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(56, 'get_TelephonePager', ((1, 'retval'),)))
    IADsUser.put_TelephonePager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(57, 'put_TelephonePager', ((1, 'vTelephonePager'),)))
    IADsUser.get_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(58, 'get_FaxNumber', ((1, 'retval'),)))
    IADsUser.put_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(59, 'put_FaxNumber', ((1, 'vFaxNumber'),)))
    IADsUser.get_OfficeLocations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(60, 'get_OfficeLocations', ((1, 'retval'),)))
    IADsUser.put_OfficeLocations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(61, 'put_OfficeLocations', ((1, 'vOfficeLocations'),)))
    IADsUser.get_PostalAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(62, 'get_PostalAddresses', ((1, 'retval'),)))
    IADsUser.put_PostalAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(63, 'put_PostalAddresses', ((1, 'vPostalAddresses'),)))
    IADsUser.get_PostalCodes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(64, 'get_PostalCodes', ((1, 'retval'),)))
    IADsUser.put_PostalCodes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(65, 'put_PostalCodes', ((1, 'vPostalCodes'),)))
    IADsUser.get_SeeAlso = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(66, 'get_SeeAlso', ((1, 'retval'),)))
    IADsUser.put_SeeAlso = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(67, 'put_SeeAlso', ((1, 'vSeeAlso'),)))
    IADsUser.get_AccountDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(68, 'get_AccountDisabled', ((1, 'retval'),)))
    IADsUser.put_AccountDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(69, 'put_AccountDisabled', ((1, 'fAccountDisabled'),)))
    IADsUser.get_AccountExpirationDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(70, 'get_AccountExpirationDate', ((1, 'retval'),)))
    IADsUser.put_AccountExpirationDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(71, 'put_AccountExpirationDate', ((1, 'daAccountExpirationDate'),)))
    IADsUser.get_GraceLoginsAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(72, 'get_GraceLoginsAllowed', ((1, 'retval'),)))
    IADsUser.put_GraceLoginsAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(73, 'put_GraceLoginsAllowed', ((1, 'lnGraceLoginsAllowed'),)))
    IADsUser.get_GraceLoginsRemaining = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(74, 'get_GraceLoginsRemaining', ((1, 'retval'),)))
    IADsUser.put_GraceLoginsRemaining = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(75, 'put_GraceLoginsRemaining', ((1, 'lnGraceLoginsRemaining'),)))
    IADsUser.get_IsAccountLocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(76, 'get_IsAccountLocked', ((1, 'retval'),)))
    IADsUser.put_IsAccountLocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(77, 'put_IsAccountLocked', ((1, 'fIsAccountLocked'),)))
    IADsUser.get_LoginHours = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(78, 'get_LoginHours', ((1, 'retval'),)))
    IADsUser.put_LoginHours = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(79, 'put_LoginHours', ((1, 'vLoginHours'),)))
    IADsUser.get_LoginWorkstations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(80, 'get_LoginWorkstations', ((1, 'retval'),)))
    IADsUser.put_LoginWorkstations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(81, 'put_LoginWorkstations', ((1, 'vLoginWorkstations'),)))
    IADsUser.get_MaxLogins = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(82, 'get_MaxLogins', ((1, 'retval'),)))
    IADsUser.put_MaxLogins = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(83, 'put_MaxLogins', ((1, 'lnMaxLogins'),)))
    IADsUser.get_MaxStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(84, 'get_MaxStorage', ((1, 'retval'),)))
    IADsUser.put_MaxStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(85, 'put_MaxStorage', ((1, 'lnMaxStorage'),)))
    IADsUser.get_PasswordExpirationDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(86, 'get_PasswordExpirationDate', ((1, 'retval'),)))
    IADsUser.put_PasswordExpirationDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(87, 'put_PasswordExpirationDate', ((1, 'daPasswordExpirationDate'),)))
    IADsUser.get_PasswordMinimumLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(88, 'get_PasswordMinimumLength', ((1, 'retval'),)))
    IADsUser.put_PasswordMinimumLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(89, 'put_PasswordMinimumLength', ((1, 'lnPasswordMinimumLength'),)))
    IADsUser.get_PasswordRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(90, 'get_PasswordRequired', ((1, 'retval'),)))
    IADsUser.put_PasswordRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(91, 'put_PasswordRequired', ((1, 'fPasswordRequired'),)))
    IADsUser.get_RequireUniquePassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(92, 'get_RequireUniquePassword', ((1, 'retval'),)))
    IADsUser.put_RequireUniquePassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(93, 'put_RequireUniquePassword', ((1, 'fRequireUniquePassword'),)))
    IADsUser.get_EmailAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(94, 'get_EmailAddress', ((1, 'retval'),)))
    IADsUser.put_EmailAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(95, 'put_EmailAddress', ((1, 'bstrEmailAddress'),)))
    IADsUser.get_HomeDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(96, 'get_HomeDirectory', ((1, 'retval'),)))
    IADsUser.put_HomeDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(97, 'put_HomeDirectory', ((1, 'bstrHomeDirectory'),)))
    IADsUser.get_Languages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(98, 'get_Languages', ((1, 'retval'),)))
    IADsUser.put_Languages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(99, 'put_Languages', ((1, 'vLanguages'),)))
    IADsUser.get_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(100, 'get_Profile', ((1, 'retval'),)))
    IADsUser.put_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(101, 'put_Profile', ((1, 'bstrProfile'),)))
    IADsUser.get_LoginScript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(102, 'get_LoginScript', ((1, 'retval'),)))
    IADsUser.put_LoginScript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(103, 'put_LoginScript', ((1, 'bstrLoginScript'),)))
    IADsUser.get_Picture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(104, 'get_Picture', ((1, 'retval'),)))
    IADsUser.put_Picture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(105, 'put_Picture', ((1, 'vPicture'),)))
    IADsUser.get_HomePage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(106, 'get_HomePage', ((1, 'retval'),)))
    IADsUser.put_HomePage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(107, 'put_HomePage', ((1, 'bstrHomePage'),)))
    IADsUser.Groups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.IADsMembers_head), use_last_error=False)(108, 'Groups', ((1, 'ppGroups'),)))
    IADsUser.SetPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(109, 'SetPassword', ((1, 'NewPassword'),)))
    IADsUser.ChangePassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(110, 'ChangePassword', ((1, 'bstrOldPassword'),(1, 'bstrNewPassword'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsUser
def _define_IADsPrintQueue_head():
    class IADsPrintQueue(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('b15160d0-1226-11cf-a985-00aa006bc149')
    return IADsPrintQueue
def _define_IADsPrintQueue():
    IADsPrintQueue = win32more.Networking.ActiveDirectory.IADsPrintQueue_head
    IADsPrintQueue.get_PrinterPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_PrinterPath', ((1, 'retval'),)))
    IADsPrintQueue.put_PrinterPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(21, 'put_PrinterPath', ((1, 'bstrPrinterPath'),)))
    IADsPrintQueue.get_Model = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_Model', ((1, 'retval'),)))
    IADsPrintQueue.put_Model = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_Model', ((1, 'bstrModel'),)))
    IADsPrintQueue.get_Datatype = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_Datatype', ((1, 'retval'),)))
    IADsPrintQueue.put_Datatype = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_Datatype', ((1, 'bstrDatatype'),)))
    IADsPrintQueue.get_PrintProcessor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'get_PrintProcessor', ((1, 'retval'),)))
    IADsPrintQueue.put_PrintProcessor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(27, 'put_PrintProcessor', ((1, 'bstrPrintProcessor'),)))
    IADsPrintQueue.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(28, 'get_Description', ((1, 'retval'),)))
    IADsPrintQueue.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(29, 'put_Description', ((1, 'bstrDescription'),)))
    IADsPrintQueue.get_Location = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(30, 'get_Location', ((1, 'retval'),)))
    IADsPrintQueue.put_Location = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(31, 'put_Location', ((1, 'bstrLocation'),)))
    IADsPrintQueue.get_StartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(32, 'get_StartTime', ((1, 'retval'),)))
    IADsPrintQueue.put_StartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(33, 'put_StartTime', ((1, 'daStartTime'),)))
    IADsPrintQueue.get_UntilTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(34, 'get_UntilTime', ((1, 'retval'),)))
    IADsPrintQueue.put_UntilTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(35, 'put_UntilTime', ((1, 'daUntilTime'),)))
    IADsPrintQueue.get_DefaultJobPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(36, 'get_DefaultJobPriority', ((1, 'retval'),)))
    IADsPrintQueue.put_DefaultJobPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(37, 'put_DefaultJobPriority', ((1, 'lnDefaultJobPriority'),)))
    IADsPrintQueue.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(38, 'get_Priority', ((1, 'retval'),)))
    IADsPrintQueue.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(39, 'put_Priority', ((1, 'lnPriority'),)))
    IADsPrintQueue.get_BannerPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(40, 'get_BannerPage', ((1, 'retval'),)))
    IADsPrintQueue.put_BannerPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(41, 'put_BannerPage', ((1, 'bstrBannerPage'),)))
    IADsPrintQueue.get_PrintDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(42, 'get_PrintDevices', ((1, 'retval'),)))
    IADsPrintQueue.put_PrintDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(43, 'put_PrintDevices', ((1, 'vPrintDevices'),)))
    IADsPrintQueue.get_NetAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(44, 'get_NetAddresses', ((1, 'retval'),)))
    IADsPrintQueue.put_NetAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(45, 'put_NetAddresses', ((1, 'vNetAddresses'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsPrintQueue
def _define_IADsPrintQueueOperations_head():
    class IADsPrintQueueOperations(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('124be5c0-156e-11cf-a986-00aa006bc149')
    return IADsPrintQueueOperations
def _define_IADsPrintQueueOperations():
    IADsPrintQueueOperations = win32more.Networking.ActiveDirectory.IADsPrintQueueOperations_head
    IADsPrintQueueOperations.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_Status', ((1, 'retval'),)))
    IADsPrintQueueOperations.PrintJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.IADsCollection_head), use_last_error=False)(21, 'PrintJobs', ((1, 'pObject'),)))
    IADsPrintQueueOperations.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(22, 'Pause', ()))
    IADsPrintQueueOperations.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(23, 'Resume', ()))
    IADsPrintQueueOperations.Purge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(24, 'Purge', ()))
    win32more.Networking.ActiveDirectory.IADs
    return IADsPrintQueueOperations
def _define_IADsPrintJob_head():
    class IADsPrintJob(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('32fb6780-1ed0-11cf-a988-00aa006bc149')
    return IADsPrintJob
def _define_IADsPrintJob():
    IADsPrintJob = win32more.Networking.ActiveDirectory.IADsPrintJob_head
    IADsPrintJob.get_HostPrintQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_HostPrintQueue', ((1, 'retval'),)))
    IADsPrintJob.get_User = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_User', ((1, 'retval'),)))
    IADsPrintJob.get_UserPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_UserPath', ((1, 'retval'),)))
    IADsPrintJob.get_TimeSubmitted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(23, 'get_TimeSubmitted', ((1, 'retval'),)))
    IADsPrintJob.get_TotalPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(24, 'get_TotalPages', ((1, 'retval'),)))
    IADsPrintJob.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'get_Size', ((1, 'retval'),)))
    IADsPrintJob.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'get_Description', ((1, 'retval'),)))
    IADsPrintJob.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(27, 'put_Description', ((1, 'bstrDescription'),)))
    IADsPrintJob.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(28, 'get_Priority', ((1, 'retval'),)))
    IADsPrintJob.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(29, 'put_Priority', ((1, 'lnPriority'),)))
    IADsPrintJob.get_StartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(30, 'get_StartTime', ((1, 'retval'),)))
    IADsPrintJob.put_StartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(31, 'put_StartTime', ((1, 'daStartTime'),)))
    IADsPrintJob.get_UntilTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(32, 'get_UntilTime', ((1, 'retval'),)))
    IADsPrintJob.put_UntilTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(33, 'put_UntilTime', ((1, 'daUntilTime'),)))
    IADsPrintJob.get_Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(34, 'get_Notify', ((1, 'retval'),)))
    IADsPrintJob.put_Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(35, 'put_Notify', ((1, 'bstrNotify'),)))
    IADsPrintJob.get_NotifyPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'get_NotifyPath', ((1, 'retval'),)))
    IADsPrintJob.put_NotifyPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'put_NotifyPath', ((1, 'bstrNotifyPath'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsPrintJob
def _define_IADsPrintJobOperations_head():
    class IADsPrintJobOperations(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('9a52db30-1ecf-11cf-a988-00aa006bc149')
    return IADsPrintJobOperations
def _define_IADsPrintJobOperations():
    IADsPrintJobOperations = win32more.Networking.ActiveDirectory.IADsPrintJobOperations_head
    IADsPrintJobOperations.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_Status', ((1, 'retval'),)))
    IADsPrintJobOperations.get_TimeElapsed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'get_TimeElapsed', ((1, 'retval'),)))
    IADsPrintJobOperations.get_PagesPrinted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(22, 'get_PagesPrinted', ((1, 'retval'),)))
    IADsPrintJobOperations.get_Position = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_Position', ((1, 'retval'),)))
    IADsPrintJobOperations.put_Position = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_Position', ((1, 'lnPosition'),)))
    IADsPrintJobOperations.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(25, 'Pause', ()))
    IADsPrintJobOperations.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(26, 'Resume', ()))
    win32more.Networking.ActiveDirectory.IADs
    return IADsPrintJobOperations
def _define_IADsService_head():
    class IADsService(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('68af66e0-31ca-11cf-a98a-00aa006bc149')
    return IADsService
def _define_IADsService():
    IADsService = win32more.Networking.ActiveDirectory.IADsService_head
    IADsService.get_HostComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_HostComputer', ((1, 'retval'),)))
    IADsService.put_HostComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(21, 'put_HostComputer', ((1, 'bstrHostComputer'),)))
    IADsService.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_DisplayName', ((1, 'retval'),)))
    IADsService.put_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_DisplayName', ((1, 'bstrDisplayName'),)))
    IADsService.get_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_Version', ((1, 'retval'),)))
    IADsService.put_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_Version', ((1, 'bstrVersion'),)))
    IADsService.get_ServiceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(26, 'get_ServiceType', ((1, 'retval'),)))
    IADsService.put_ServiceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(27, 'put_ServiceType', ((1, 'lnServiceType'),)))
    IADsService.get_StartType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(28, 'get_StartType', ((1, 'retval'),)))
    IADsService.put_StartType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(29, 'put_StartType', ((1, 'lnStartType'),)))
    IADsService.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(30, 'get_Path', ((1, 'retval'),)))
    IADsService.put_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(31, 'put_Path', ((1, 'bstrPath'),)))
    IADsService.get_StartupParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(32, 'get_StartupParameters', ((1, 'retval'),)))
    IADsService.put_StartupParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(33, 'put_StartupParameters', ((1, 'bstrStartupParameters'),)))
    IADsService.get_ErrorControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(34, 'get_ErrorControl', ((1, 'retval'),)))
    IADsService.put_ErrorControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(35, 'put_ErrorControl', ((1, 'lnErrorControl'),)))
    IADsService.get_LoadOrderGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'get_LoadOrderGroup', ((1, 'retval'),)))
    IADsService.put_LoadOrderGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'put_LoadOrderGroup', ((1, 'bstrLoadOrderGroup'),)))
    IADsService.get_ServiceAccountName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(38, 'get_ServiceAccountName', ((1, 'retval'),)))
    IADsService.put_ServiceAccountName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(39, 'put_ServiceAccountName', ((1, 'bstrServiceAccountName'),)))
    IADsService.get_ServiceAccountPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(40, 'get_ServiceAccountPath', ((1, 'retval'),)))
    IADsService.put_ServiceAccountPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(41, 'put_ServiceAccountPath', ((1, 'bstrServiceAccountPath'),)))
    IADsService.get_Dependencies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(42, 'get_Dependencies', ((1, 'retval'),)))
    IADsService.put_Dependencies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(43, 'put_Dependencies', ((1, 'vDependencies'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsService
def _define_IADsServiceOperations_head():
    class IADsServiceOperations(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('5d7b33f0-31ca-11cf-a98a-00aa006bc149')
    return IADsServiceOperations
def _define_IADsServiceOperations():
    IADsServiceOperations = win32more.Networking.ActiveDirectory.IADsServiceOperations_head
    IADsServiceOperations.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_Status', ((1, 'retval'),)))
    IADsServiceOperations.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'Start', ()))
    IADsServiceOperations.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(22, 'Stop', ()))
    IADsServiceOperations.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(23, 'Pause', ()))
    IADsServiceOperations.Continue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(24, 'Continue', ()))
    IADsServiceOperations.SetPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'SetPassword', ((1, 'bstrNewPassword'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsServiceOperations
def _define_IADsFileService_head():
    class IADsFileService(win32more.Networking.ActiveDirectory.IADsService_head):
        Guid = Guid('a89d1900-31ca-11cf-a98a-00aa006bc149')
    return IADsFileService
def _define_IADsFileService():
    IADsFileService = win32more.Networking.ActiveDirectory.IADsFileService_head
    IADsFileService.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(44, 'get_Description', ((1, 'retval'),)))
    IADsFileService.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(45, 'put_Description', ((1, 'bstrDescription'),)))
    IADsFileService.get_MaxUserCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(46, 'get_MaxUserCount', ((1, 'retval'),)))
    IADsFileService.put_MaxUserCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(47, 'put_MaxUserCount', ((1, 'lnMaxUserCount'),)))
    win32more.Networking.ActiveDirectory.IADsService
    return IADsFileService
def _define_IADsFileServiceOperations_head():
    class IADsFileServiceOperations(win32more.Networking.ActiveDirectory.IADsServiceOperations_head):
        Guid = Guid('a02ded10-31ca-11cf-a98a-00aa006bc149')
    return IADsFileServiceOperations
def _define_IADsFileServiceOperations():
    IADsFileServiceOperations = win32more.Networking.ActiveDirectory.IADsFileServiceOperations_head
    IADsFileServiceOperations.Sessions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.IADsCollection_head), use_last_error=False)(26, 'Sessions', ((1, 'ppSessions'),)))
    IADsFileServiceOperations.Resources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.IADsCollection_head), use_last_error=False)(27, 'Resources', ((1, 'ppResources'),)))
    win32more.Networking.ActiveDirectory.IADsServiceOperations
    return IADsFileServiceOperations
def _define_IADsFileShare_head():
    class IADsFileShare(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('eb6dcaf0-4b83-11cf-a995-00aa006bc149')
    return IADsFileShare
def _define_IADsFileShare():
    IADsFileShare = win32more.Networking.ActiveDirectory.IADsFileShare_head
    IADsFileShare.get_CurrentUserCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_CurrentUserCount', ((1, 'retval'),)))
    IADsFileShare.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_Description', ((1, 'retval'),)))
    IADsFileShare.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(22, 'put_Description', ((1, 'bstrDescription'),)))
    IADsFileShare.get_HostComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_HostComputer', ((1, 'retval'),)))
    IADsFileShare.put_HostComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(24, 'put_HostComputer', ((1, 'bstrHostComputer'),)))
    IADsFileShare.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_Path', ((1, 'retval'),)))
    IADsFileShare.put_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(26, 'put_Path', ((1, 'bstrPath'),)))
    IADsFileShare.get_MaxUserCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(27, 'get_MaxUserCount', ((1, 'retval'),)))
    IADsFileShare.put_MaxUserCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(28, 'put_MaxUserCount', ((1, 'lnMaxUserCount'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsFileShare
def _define_IADsSession_head():
    class IADsSession(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('398b7da0-4aab-11cf-ae2c-00aa006ebfb9')
    return IADsSession
def _define_IADsSession():
    IADsSession = win32more.Networking.ActiveDirectory.IADsSession_head
    IADsSession.get_User = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_User', ((1, 'retval'),)))
    IADsSession.get_UserPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_UserPath', ((1, 'retval'),)))
    IADsSession.get_Computer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_Computer', ((1, 'retval'),)))
    IADsSession.get_ComputerPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_ComputerPath', ((1, 'retval'),)))
    IADsSession.get_ConnectTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(24, 'get_ConnectTime', ((1, 'retval'),)))
    IADsSession.get_IdleTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'get_IdleTime', ((1, 'retval'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsSession
def _define_IADsResource_head():
    class IADsResource(win32more.Networking.ActiveDirectory.IADs_head):
        Guid = Guid('34a05b20-4aab-11cf-ae2c-00aa006ebfb9')
    return IADsResource
def _define_IADsResource():
    IADsResource = win32more.Networking.ActiveDirectory.IADsResource_head
    IADsResource.get_User = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_User', ((1, 'retval'),)))
    IADsResource.get_UserPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_UserPath', ((1, 'retval'),)))
    IADsResource.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_Path', ((1, 'retval'),)))
    IADsResource.get_LockCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_LockCount', ((1, 'retval'),)))
    win32more.Networking.ActiveDirectory.IADs
    return IADsResource
def _define_IADsOpenDSObject_head():
    class IADsOpenDSObject(win32more.System.Com.IDispatch_head):
        Guid = Guid('ddf2891e-0f9c-11d0-8ad4-00c04fd8d503')
    return IADsOpenDSObject
def _define_IADsOpenDSObject():
    IADsOpenDSObject = win32more.Networking.ActiveDirectory.IADsOpenDSObject_head
    IADsOpenDSObject.OpenDSObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(7, 'OpenDSObject', ((1, 'lpszDNName'),(1, 'lpszUserName'),(1, 'lpszPassword'),(1, 'lnReserved'),(1, 'ppOleDsObj'),)))
    win32more.System.Com.IDispatch
    return IADsOpenDSObject
def _define_IDirectoryObject_head():
    class IDirectoryObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('e798de2c-22e4-11d0-84fe-00c04fd8d503')
    return IDirectoryObject
def _define_IDirectoryObject():
    IDirectoryObject = win32more.Networking.ActiveDirectory.IDirectoryObject_head
    IDirectoryObject.GetObjectInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Networking.ActiveDirectory.ADS_OBJECT_INFO_head)), use_last_error=False)(3, 'GetObjectInformation', ((1, 'ppObjInfo'),)))
    IDirectoryObject.GetObjectAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(POINTER(win32more.Networking.ActiveDirectory.ADS_ATTR_INFO_head)),POINTER(UInt32), use_last_error=False)(4, 'GetObjectAttributes', ((1, 'pAttributeNames'),(1, 'dwNumberAttributes'),(1, 'ppAttributeEntries'),(1, 'pdwNumAttributesReturned'),)))
    IDirectoryObject.SetObjectAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.ADS_ATTR_INFO_head),UInt32,POINTER(UInt32), use_last_error=False)(5, 'SetObjectAttributes', ((1, 'pAttributeEntries'),(1, 'dwNumAttributes'),(1, 'pdwNumAttributesModified'),)))
    IDirectoryObject.CreateDSObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Networking.ActiveDirectory.ADS_ATTR_INFO_head),UInt32,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(6, 'CreateDSObject', ((1, 'pszRDNName'),(1, 'pAttributeEntries'),(1, 'dwNumAttributes'),(1, 'ppObject'),)))
    IDirectoryObject.DeleteDSObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(7, 'DeleteDSObject', ((1, 'pszRDNName'),)))
    win32more.System.Com.IUnknown
    return IDirectoryObject
def _define_IDirectorySearch_head():
    class IDirectorySearch(win32more.System.Com.IUnknown_head):
        Guid = Guid('109ba8ec-92f0-11d0-a790-00c04fd8d5a8')
    return IDirectorySearch
def _define_IDirectorySearch():
    IDirectorySearch = win32more.Networking.ActiveDirectory.IDirectorySearch_head
    IDirectorySearch.SetSearchPreference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.ads_searchpref_info_head),UInt32, use_last_error=False)(3, 'SetSearchPreference', ((1, 'pSearchPrefs'),(1, 'dwNumPrefs'),)))
    IDirectorySearch.ExecuteSearch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(IntPtr), use_last_error=False)(4, 'ExecuteSearch', ((1, 'pszSearchFilter'),(1, 'pAttributeNames'),(1, 'dwNumberAttributes'),(1, 'phSearchResult'),)))
    IDirectorySearch.AbandonSearch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(5, 'AbandonSearch', ((1, 'phSearchResult'),)))
    IDirectorySearch.GetFirstRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(6, 'GetFirstRow', ((1, 'hSearchResult'),)))
    IDirectorySearch.GetNextRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(7, 'GetNextRow', ((1, 'hSearchResult'),)))
    IDirectorySearch.GetPreviousRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(8, 'GetPreviousRow', ((1, 'hSearchResult'),)))
    IDirectorySearch.GetNextColumnName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(9, 'GetNextColumnName', ((1, 'hSearchHandle'),(1, 'ppszColumnName'),)))
    IDirectorySearch.GetColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.Foundation.PWSTR,POINTER(win32more.Networking.ActiveDirectory.ads_search_column_head), use_last_error=False)(10, 'GetColumn', ((1, 'hSearchResult'),(1, 'szColumnName'),(1, 'pSearchColumn'),)))
    IDirectorySearch.FreeColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.ads_search_column_head), use_last_error=False)(11, 'FreeColumn', ((1, 'pSearchColumn'),)))
    IDirectorySearch.CloseSearchHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(12, 'CloseSearchHandle', ((1, 'hSearchResult'),)))
    win32more.System.Com.IUnknown
    return IDirectorySearch
def _define_IDirectorySchemaMgmt_head():
    class IDirectorySchemaMgmt(win32more.System.Com.IUnknown_head):
        Guid = Guid('75db3b9c-a4d8-11d0-a79c-00c04fd8d5a8')
    return IDirectorySchemaMgmt
def _define_IDirectorySchemaMgmt():
    IDirectorySchemaMgmt = win32more.Networking.ActiveDirectory.IDirectorySchemaMgmt_head
    IDirectorySchemaMgmt.EnumAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(POINTER(win32more.Networking.ActiveDirectory.ADS_ATTR_DEF_head)),POINTER(UInt32), use_last_error=False)(3, 'EnumAttributes', ((1, 'ppszAttrNames'),(1, 'dwNumAttributes'),(1, 'ppAttrDefinition'),(1, 'pdwNumAttributes'),)))
    IDirectorySchemaMgmt.CreateAttributeDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Networking.ActiveDirectory.ADS_ATTR_DEF_head), use_last_error=False)(4, 'CreateAttributeDefinition', ((1, 'pszAttributeName'),(1, 'pAttributeDefinition'),)))
    IDirectorySchemaMgmt.WriteAttributeDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Networking.ActiveDirectory.ADS_ATTR_DEF_head), use_last_error=False)(5, 'WriteAttributeDefinition', ((1, 'pszAttributeName'),(1, 'pAttributeDefinition'),)))
    IDirectorySchemaMgmt.DeleteAttributeDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'DeleteAttributeDefinition', ((1, 'pszAttributeName'),)))
    IDirectorySchemaMgmt.EnumClasses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(POINTER(win32more.Networking.ActiveDirectory.ADS_CLASS_DEF_head)),POINTER(UInt32), use_last_error=False)(7, 'EnumClasses', ((1, 'ppszClassNames'),(1, 'dwNumClasses'),(1, 'ppClassDefinition'),(1, 'pdwNumClasses'),)))
    IDirectorySchemaMgmt.WriteClassDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Networking.ActiveDirectory.ADS_CLASS_DEF_head), use_last_error=False)(8, 'WriteClassDefinition', ((1, 'pszClassName'),(1, 'pClassDefinition'),)))
    IDirectorySchemaMgmt.CreateClassDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Networking.ActiveDirectory.ADS_CLASS_DEF_head), use_last_error=False)(9, 'CreateClassDefinition', ((1, 'pszClassName'),(1, 'pClassDefinition'),)))
    IDirectorySchemaMgmt.DeleteClassDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(10, 'DeleteClassDefinition', ((1, 'pszClassName'),)))
    win32more.System.Com.IUnknown
    return IDirectorySchemaMgmt
def _define_IADsAggregatee_head():
    class IADsAggregatee(win32more.System.Com.IUnknown_head):
        Guid = Guid('1346ce8c-9039-11d0-8528-00c04fd8d503')
    return IADsAggregatee
def _define_IADsAggregatee():
    IADsAggregatee = win32more.Networking.ActiveDirectory.IADsAggregatee_head
    IADsAggregatee.ConnectAsAggregatee = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'ConnectAsAggregatee', ((1, 'pOuterUnknown'),)))
    IADsAggregatee.DisconnectAsAggregatee = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'DisconnectAsAggregatee', ()))
    IADsAggregatee.RelinquishInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(5, 'RelinquishInterface', ((1, 'riid'),)))
    IADsAggregatee.RestoreInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(6, 'RestoreInterface', ((1, 'riid'),)))
    win32more.System.Com.IUnknown
    return IADsAggregatee
def _define_IADsAggregator_head():
    class IADsAggregator(win32more.System.Com.IUnknown_head):
        Guid = Guid('52db5fb0-941f-11d0-8529-00c04fd8d503')
    return IADsAggregator
def _define_IADsAggregator():
    IADsAggregator = win32more.Networking.ActiveDirectory.IADsAggregator_head
    IADsAggregator.ConnectAsAggregator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'ConnectAsAggregator', ((1, 'pAggregatee'),)))
    IADsAggregator.DisconnectAsAggregator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'DisconnectAsAggregator', ()))
    win32more.System.Com.IUnknown
    return IADsAggregator
def _define_IADsAccessControlEntry_head():
    class IADsAccessControlEntry(win32more.System.Com.IDispatch_head):
        Guid = Guid('b4f3a14c-9bdd-11d0-852c-00c04fd8d503')
    return IADsAccessControlEntry
def _define_IADsAccessControlEntry():
    IADsAccessControlEntry = win32more.Networking.ActiveDirectory.IADsAccessControlEntry_head
    IADsAccessControlEntry.get_AccessMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_AccessMask', ((1, 'retval'),)))
    IADsAccessControlEntry.put_AccessMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_AccessMask', ((1, 'lnAccessMask'),)))
    IADsAccessControlEntry.get_AceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_AceType', ((1, 'retval'),)))
    IADsAccessControlEntry.put_AceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_AceType', ((1, 'lnAceType'),)))
    IADsAccessControlEntry.get_AceFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_AceFlags', ((1, 'retval'),)))
    IADsAccessControlEntry.put_AceFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'put_AceFlags', ((1, 'lnAceFlags'),)))
    IADsAccessControlEntry.get_Flags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_Flags', ((1, 'retval'),)))
    IADsAccessControlEntry.put_Flags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_Flags', ((1, 'lnFlags'),)))
    IADsAccessControlEntry.get_ObjectType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_ObjectType', ((1, 'retval'),)))
    IADsAccessControlEntry.put_ObjectType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_ObjectType', ((1, 'bstrObjectType'),)))
    IADsAccessControlEntry.get_InheritedObjectType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_InheritedObjectType', ((1, 'retval'),)))
    IADsAccessControlEntry.put_InheritedObjectType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_InheritedObjectType', ((1, 'bstrInheritedObjectType'),)))
    IADsAccessControlEntry.get_Trustee = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_Trustee', ((1, 'retval'),)))
    IADsAccessControlEntry.put_Trustee = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(20, 'put_Trustee', ((1, 'bstrTrustee'),)))
    win32more.System.Com.IDispatch
    return IADsAccessControlEntry
def _define_IADsAccessControlList_head():
    class IADsAccessControlList(win32more.System.Com.IDispatch_head):
        Guid = Guid('b7ee91cc-9bdd-11d0-852c-00c04fd8d503')
    return IADsAccessControlList
def _define_IADsAccessControlList():
    IADsAccessControlList = win32more.Networking.ActiveDirectory.IADsAccessControlList_head
    IADsAccessControlList.get_AclRevision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_AclRevision', ((1, 'retval'),)))
    IADsAccessControlList.put_AclRevision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_AclRevision', ((1, 'lnAclRevision'),)))
    IADsAccessControlList.get_AceCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_AceCount', ((1, 'retval'),)))
    IADsAccessControlList.put_AceCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_AceCount', ((1, 'lnAceCount'),)))
    IADsAccessControlList.AddAce = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(11, 'AddAce', ((1, 'pAccessControlEntry'),)))
    IADsAccessControlList.RemoveAce = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(12, 'RemoveAce', ((1, 'pAccessControlEntry'),)))
    IADsAccessControlList.CopyAccessList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(13, 'CopyAccessList', ((1, 'ppAccessControlList'),)))
    IADsAccessControlList.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(14, 'get__NewEnum', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IADsAccessControlList
def _define_IADsSecurityDescriptor_head():
    class IADsSecurityDescriptor(win32more.System.Com.IDispatch_head):
        Guid = Guid('b8c787ca-9bdd-11d0-852c-00c04fd8d503')
    return IADsSecurityDescriptor
def _define_IADsSecurityDescriptor():
    IADsSecurityDescriptor = win32more.Networking.ActiveDirectory.IADsSecurityDescriptor_head
    IADsSecurityDescriptor.get_Revision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Revision', ((1, 'retval'),)))
    IADsSecurityDescriptor.put_Revision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_Revision', ((1, 'lnRevision'),)))
    IADsSecurityDescriptor.get_Control = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Control', ((1, 'retval'),)))
    IADsSecurityDescriptor.put_Control = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_Control', ((1, 'lnControl'),)))
    IADsSecurityDescriptor.get_Owner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_Owner', ((1, 'retval'),)))
    IADsSecurityDescriptor.put_Owner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_Owner', ((1, 'bstrOwner'),)))
    IADsSecurityDescriptor.get_OwnerDefaulted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_OwnerDefaulted', ((1, 'retval'),)))
    IADsSecurityDescriptor.put_OwnerDefaulted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'put_OwnerDefaulted', ((1, 'fOwnerDefaulted'),)))
    IADsSecurityDescriptor.get_Group = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_Group', ((1, 'retval'),)))
    IADsSecurityDescriptor.put_Group = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_Group', ((1, 'bstrGroup'),)))
    IADsSecurityDescriptor.get_GroupDefaulted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_GroupDefaulted', ((1, 'retval'),)))
    IADsSecurityDescriptor.put_GroupDefaulted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(18, 'put_GroupDefaulted', ((1, 'fGroupDefaulted'),)))
    IADsSecurityDescriptor.get_DiscretionaryAcl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(19, 'get_DiscretionaryAcl', ((1, 'retval'),)))
    IADsSecurityDescriptor.put_DiscretionaryAcl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(20, 'put_DiscretionaryAcl', ((1, 'pDiscretionaryAcl'),)))
    IADsSecurityDescriptor.get_DaclDefaulted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(21, 'get_DaclDefaulted', ((1, 'retval'),)))
    IADsSecurityDescriptor.put_DaclDefaulted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(22, 'put_DaclDefaulted', ((1, 'fDaclDefaulted'),)))
    IADsSecurityDescriptor.get_SystemAcl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(23, 'get_SystemAcl', ((1, 'retval'),)))
    IADsSecurityDescriptor.put_SystemAcl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(24, 'put_SystemAcl', ((1, 'pSystemAcl'),)))
    IADsSecurityDescriptor.get_SaclDefaulted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(25, 'get_SaclDefaulted', ((1, 'retval'),)))
    IADsSecurityDescriptor.put_SaclDefaulted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(26, 'put_SaclDefaulted', ((1, 'fSaclDefaulted'),)))
    IADsSecurityDescriptor.CopySecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(27, 'CopySecurityDescriptor', ((1, 'ppSecurityDescriptor'),)))
    win32more.System.Com.IDispatch
    return IADsSecurityDescriptor
def _define_IADsLargeInteger_head():
    class IADsLargeInteger(win32more.System.Com.IDispatch_head):
        Guid = Guid('9068270b-0939-11d1-8be1-00c04fd8d503')
    return IADsLargeInteger
def _define_IADsLargeInteger():
    IADsLargeInteger = win32more.Networking.ActiveDirectory.IADsLargeInteger_head
    IADsLargeInteger.get_HighPart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_HighPart', ((1, 'retval'),)))
    IADsLargeInteger.put_HighPart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_HighPart', ((1, 'lnHighPart'),)))
    IADsLargeInteger.get_LowPart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_LowPart', ((1, 'retval'),)))
    IADsLargeInteger.put_LowPart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_LowPart', ((1, 'lnLowPart'),)))
    win32more.System.Com.IDispatch
    return IADsLargeInteger
def _define_IADsNameTranslate_head():
    class IADsNameTranslate(win32more.System.Com.IDispatch_head):
        Guid = Guid('b1b272a3-3625-11d1-a3a4-00c04fb950dc')
    return IADsNameTranslate
def _define_IADsNameTranslate():
    IADsNameTranslate = win32more.Networking.ActiveDirectory.IADsNameTranslate_head
    IADsNameTranslate.put_ChaseReferral = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(7, 'put_ChaseReferral', ((1, 'lnChaseReferral'),)))
    IADsNameTranslate.Init = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR, use_last_error=False)(8, 'Init', ((1, 'lnSetType'),(1, 'bstrADsPath'),)))
    IADsNameTranslate.InitEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(9, 'InitEx', ((1, 'lnSetType'),(1, 'bstrADsPath'),(1, 'bstrUserID'),(1, 'bstrDomain'),(1, 'bstrPassword'),)))
    IADsNameTranslate.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR, use_last_error=False)(10, 'Set', ((1, 'lnSetType'),(1, 'bstrADsPath'),)))
    IADsNameTranslate.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'Get', ((1, 'lnFormatType'),(1, 'pbstrADsPath'),)))
    IADsNameTranslate.SetEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT, use_last_error=False)(12, 'SetEx', ((1, 'lnFormatType'),(1, 'pvar'),)))
    IADsNameTranslate.GetEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'GetEx', ((1, 'lnFormatType'),(1, 'pvar'),)))
    win32more.System.Com.IDispatch
    return IADsNameTranslate
def _define_IADsCaseIgnoreList_head():
    class IADsCaseIgnoreList(win32more.System.Com.IDispatch_head):
        Guid = Guid('7b66b533-4680-11d1-a3b4-00c04fb950dc')
    return IADsCaseIgnoreList
def _define_IADsCaseIgnoreList():
    IADsCaseIgnoreList = win32more.Networking.ActiveDirectory.IADsCaseIgnoreList_head
    IADsCaseIgnoreList.get_CaseIgnoreList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_CaseIgnoreList', ((1, 'retval'),)))
    IADsCaseIgnoreList.put_CaseIgnoreList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_CaseIgnoreList', ((1, 'vCaseIgnoreList'),)))
    win32more.System.Com.IDispatch
    return IADsCaseIgnoreList
def _define_IADsFaxNumber_head():
    class IADsFaxNumber(win32more.System.Com.IDispatch_head):
        Guid = Guid('a910dea9-4680-11d1-a3b4-00c04fb950dc')
    return IADsFaxNumber
def _define_IADsFaxNumber():
    IADsFaxNumber = win32more.Networking.ActiveDirectory.IADsFaxNumber_head
    IADsFaxNumber.get_TelephoneNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_TelephoneNumber', ((1, 'retval'),)))
    IADsFaxNumber.put_TelephoneNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_TelephoneNumber', ((1, 'bstrTelephoneNumber'),)))
    IADsFaxNumber.get_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'get_Parameters', ((1, 'retval'),)))
    IADsFaxNumber.put_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(10, 'put_Parameters', ((1, 'vParameters'),)))
    win32more.System.Com.IDispatch
    return IADsFaxNumber
def _define_IADsNetAddress_head():
    class IADsNetAddress(win32more.System.Com.IDispatch_head):
        Guid = Guid('b21a50a9-4080-11d1-a3ac-00c04fb950dc')
    return IADsNetAddress
def _define_IADsNetAddress():
    IADsNetAddress = win32more.Networking.ActiveDirectory.IADsNetAddress_head
    IADsNetAddress.get_AddressType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_AddressType', ((1, 'retval'),)))
    IADsNetAddress.put_AddressType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_AddressType', ((1, 'lnAddressType'),)))
    IADsNetAddress.get_Address = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'get_Address', ((1, 'retval'),)))
    IADsNetAddress.put_Address = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(10, 'put_Address', ((1, 'vAddress'),)))
    win32more.System.Com.IDispatch
    return IADsNetAddress
def _define_IADsOctetList_head():
    class IADsOctetList(win32more.System.Com.IDispatch_head):
        Guid = Guid('7b28b80f-4680-11d1-a3b4-00c04fb950dc')
    return IADsOctetList
def _define_IADsOctetList():
    IADsOctetList = win32more.Networking.ActiveDirectory.IADsOctetList_head
    IADsOctetList.get_OctetList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_OctetList', ((1, 'retval'),)))
    IADsOctetList.put_OctetList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_OctetList', ((1, 'vOctetList'),)))
    win32more.System.Com.IDispatch
    return IADsOctetList
def _define_IADsEmail_head():
    class IADsEmail(win32more.System.Com.IDispatch_head):
        Guid = Guid('97af011a-478e-11d1-a3b4-00c04fb950dc')
    return IADsEmail
def _define_IADsEmail():
    IADsEmail = win32more.Networking.ActiveDirectory.IADsEmail_head
    IADsEmail.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Type', ((1, 'retval'),)))
    IADsEmail.put_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_Type', ((1, 'lnType'),)))
    IADsEmail.get_Address = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Address', ((1, 'retval'),)))
    IADsEmail.put_Address = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_Address', ((1, 'bstrAddress'),)))
    win32more.System.Com.IDispatch
    return IADsEmail
def _define_IADsPath_head():
    class IADsPath(win32more.System.Com.IDispatch_head):
        Guid = Guid('b287fcd5-4080-11d1-a3ac-00c04fb950dc')
    return IADsPath
def _define_IADsPath():
    IADsPath = win32more.Networking.ActiveDirectory.IADsPath_head
    IADsPath.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Type', ((1, 'retval'),)))
    IADsPath.put_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_Type', ((1, 'lnType'),)))
    IADsPath.get_VolumeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_VolumeName', ((1, 'retval'),)))
    IADsPath.put_VolumeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_VolumeName', ((1, 'bstrVolumeName'),)))
    IADsPath.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_Path', ((1, 'retval'),)))
    IADsPath.put_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_Path', ((1, 'bstrPath'),)))
    win32more.System.Com.IDispatch
    return IADsPath
def _define_IADsReplicaPointer_head():
    class IADsReplicaPointer(win32more.System.Com.IDispatch_head):
        Guid = Guid('f60fb803-4080-11d1-a3ac-00c04fb950dc')
    return IADsReplicaPointer
def _define_IADsReplicaPointer():
    IADsReplicaPointer = win32more.Networking.ActiveDirectory.IADsReplicaPointer_head
    IADsReplicaPointer.get_ServerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ServerName', ((1, 'retval'),)))
    IADsReplicaPointer.put_ServerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_ServerName', ((1, 'bstrServerName'),)))
    IADsReplicaPointer.get_ReplicaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_ReplicaType', ((1, 'retval'),)))
    IADsReplicaPointer.put_ReplicaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_ReplicaType', ((1, 'lnReplicaType'),)))
    IADsReplicaPointer.get_ReplicaNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_ReplicaNumber', ((1, 'retval'),)))
    IADsReplicaPointer.put_ReplicaNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'put_ReplicaNumber', ((1, 'lnReplicaNumber'),)))
    IADsReplicaPointer.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_Count', ((1, 'retval'),)))
    IADsReplicaPointer.put_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_Count', ((1, 'lnCount'),)))
    IADsReplicaPointer.get_ReplicaAddressHints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'get_ReplicaAddressHints', ((1, 'retval'),)))
    IADsReplicaPointer.put_ReplicaAddressHints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(16, 'put_ReplicaAddressHints', ((1, 'vReplicaAddressHints'),)))
    win32more.System.Com.IDispatch
    return IADsReplicaPointer
def _define_IADsAcl_head():
    class IADsAcl(win32more.System.Com.IDispatch_head):
        Guid = Guid('8452d3ab-0869-11d1-a377-00c04fb950dc')
    return IADsAcl
def _define_IADsAcl():
    IADsAcl = win32more.Networking.ActiveDirectory.IADsAcl_head
    IADsAcl.get_ProtectedAttrName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ProtectedAttrName', ((1, 'retval'),)))
    IADsAcl.put_ProtectedAttrName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_ProtectedAttrName', ((1, 'bstrProtectedAttrName'),)))
    IADsAcl.get_SubjectName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_SubjectName', ((1, 'retval'),)))
    IADsAcl.put_SubjectName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_SubjectName', ((1, 'bstrSubjectName'),)))
    IADsAcl.get_Privileges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_Privileges', ((1, 'retval'),)))
    IADsAcl.put_Privileges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'put_Privileges', ((1, 'lnPrivileges'),)))
    IADsAcl.CopyAcl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(13, 'CopyAcl', ((1, 'ppAcl'),)))
    win32more.System.Com.IDispatch
    return IADsAcl
def _define_IADsTimestamp_head():
    class IADsTimestamp(win32more.System.Com.IDispatch_head):
        Guid = Guid('b2f5a901-4080-11d1-a3ac-00c04fb950dc')
    return IADsTimestamp
def _define_IADsTimestamp():
    IADsTimestamp = win32more.Networking.ActiveDirectory.IADsTimestamp_head
    IADsTimestamp.get_WholeSeconds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_WholeSeconds', ((1, 'retval'),)))
    IADsTimestamp.put_WholeSeconds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_WholeSeconds', ((1, 'lnWholeSeconds'),)))
    IADsTimestamp.get_EventID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_EventID', ((1, 'retval'),)))
    IADsTimestamp.put_EventID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_EventID', ((1, 'lnEventID'),)))
    win32more.System.Com.IDispatch
    return IADsTimestamp
def _define_IADsPostalAddress_head():
    class IADsPostalAddress(win32more.System.Com.IDispatch_head):
        Guid = Guid('7adecf29-4680-11d1-a3b4-00c04fb950dc')
    return IADsPostalAddress
def _define_IADsPostalAddress():
    IADsPostalAddress = win32more.Networking.ActiveDirectory.IADsPostalAddress_head
    IADsPostalAddress.get_PostalAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_PostalAddress', ((1, 'retval'),)))
    IADsPostalAddress.put_PostalAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_PostalAddress', ((1, 'vPostalAddress'),)))
    win32more.System.Com.IDispatch
    return IADsPostalAddress
def _define_IADsBackLink_head():
    class IADsBackLink(win32more.System.Com.IDispatch_head):
        Guid = Guid('fd1302bd-4080-11d1-a3ac-00c04fb950dc')
    return IADsBackLink
def _define_IADsBackLink():
    IADsBackLink = win32more.Networking.ActiveDirectory.IADsBackLink_head
    IADsBackLink.get_RemoteID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_RemoteID', ((1, 'retval'),)))
    IADsBackLink.put_RemoteID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_RemoteID', ((1, 'lnRemoteID'),)))
    IADsBackLink.get_ObjectName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ObjectName', ((1, 'retval'),)))
    IADsBackLink.put_ObjectName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_ObjectName', ((1, 'bstrObjectName'),)))
    win32more.System.Com.IDispatch
    return IADsBackLink
def _define_IADsTypedName_head():
    class IADsTypedName(win32more.System.Com.IDispatch_head):
        Guid = Guid('b371a349-4080-11d1-a3ac-00c04fb950dc')
    return IADsTypedName
def _define_IADsTypedName():
    IADsTypedName = win32more.Networking.ActiveDirectory.IADsTypedName_head
    IADsTypedName.get_ObjectName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ObjectName', ((1, 'retval'),)))
    IADsTypedName.put_ObjectName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_ObjectName', ((1, 'bstrObjectName'),)))
    IADsTypedName.get_Level = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Level', ((1, 'retval'),)))
    IADsTypedName.put_Level = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_Level', ((1, 'lnLevel'),)))
    IADsTypedName.get_Interval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_Interval', ((1, 'retval'),)))
    IADsTypedName.put_Interval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'put_Interval', ((1, 'lnInterval'),)))
    win32more.System.Com.IDispatch
    return IADsTypedName
def _define_IADsHold_head():
    class IADsHold(win32more.System.Com.IDispatch_head):
        Guid = Guid('b3eb3b37-4080-11d1-a3ac-00c04fb950dc')
    return IADsHold
def _define_IADsHold():
    IADsHold = win32more.Networking.ActiveDirectory.IADsHold_head
    IADsHold.get_ObjectName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ObjectName', ((1, 'retval'),)))
    IADsHold.put_ObjectName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_ObjectName', ((1, 'bstrObjectName'),)))
    IADsHold.get_Amount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Amount', ((1, 'retval'),)))
    IADsHold.put_Amount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_Amount', ((1, 'lnAmount'),)))
    win32more.System.Com.IDispatch
    return IADsHold
def _define_IADsObjectOptions_head():
    class IADsObjectOptions(win32more.System.Com.IDispatch_head):
        Guid = Guid('46f14fda-232b-11d1-a808-00c04fd8d5a8')
    return IADsObjectOptions
def _define_IADsObjectOptions():
    IADsObjectOptions = win32more.Networking.ActiveDirectory.IADsObjectOptions_head
    IADsObjectOptions.GetOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'GetOption', ((1, 'lnOption'),(1, 'pvValue'),)))
    IADsObjectOptions.SetOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT, use_last_error=False)(8, 'SetOption', ((1, 'lnOption'),(1, 'vValue'),)))
    win32more.System.Com.IDispatch
    return IADsObjectOptions
def _define_IADsPathname_head():
    class IADsPathname(win32more.System.Com.IDispatch_head):
        Guid = Guid('d592aed4-f420-11d0-a36e-00c04fb950dc')
    return IADsPathname
def _define_IADsPathname():
    IADsPathname = win32more.Networking.ActiveDirectory.IADsPathname_head
    IADsPathname.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32, use_last_error=False)(7, 'Set', ((1, 'bstrADsPath'),(1, 'lnSetType'),)))
    IADsPathname.SetDisplayType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'SetDisplayType', ((1, 'lnDisplayType'),)))
    IADsPathname.Retrieve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'Retrieve', ((1, 'lnFormatType'),(1, 'pbstrADsPath'),)))
    IADsPathname.GetNumElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'GetNumElements', ((1, 'plnNumPathElements'),)))
    IADsPathname.GetElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetElement', ((1, 'lnElementIndex'),(1, 'pbstrElement'),)))
    IADsPathname.AddLeafElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'AddLeafElement', ((1, 'bstrLeafElement'),)))
    IADsPathname.RemoveLeafElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'RemoveLeafElement', ()))
    IADsPathname.CopyPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(14, 'CopyPath', ((1, 'ppAdsPath'),)))
    IADsPathname.GetEscapedElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'GetEscapedElement', ((1, 'lnReserved'),(1, 'bstrInStr'),(1, 'pbstrOutStr'),)))
    IADsPathname.get_EscapedMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_EscapedMode', ((1, 'retval'),)))
    IADsPathname.put_EscapedMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(17, 'put_EscapedMode', ((1, 'lnEscapedMode'),)))
    win32more.System.Com.IDispatch
    return IADsPathname
def _define_IADsADSystemInfo_head():
    class IADsADSystemInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('5bb11929-afd1-11d2-9cb9-0000f87a369e')
    return IADsADSystemInfo
def _define_IADsADSystemInfo():
    IADsADSystemInfo = win32more.Networking.ActiveDirectory.IADsADSystemInfo_head
    IADsADSystemInfo.get_UserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_UserName', ((1, 'retval'),)))
    IADsADSystemInfo.get_ComputerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ComputerName', ((1, 'retval'),)))
    IADsADSystemInfo.get_SiteName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_SiteName', ((1, 'retval'),)))
    IADsADSystemInfo.get_DomainShortName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_DomainShortName', ((1, 'retval'),)))
    IADsADSystemInfo.get_DomainDNSName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_DomainDNSName', ((1, 'retval'),)))
    IADsADSystemInfo.get_ForestDNSName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_ForestDNSName', ((1, 'retval'),)))
    IADsADSystemInfo.get_PDCRoleOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_PDCRoleOwner', ((1, 'retval'),)))
    IADsADSystemInfo.get_SchemaRoleOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_SchemaRoleOwner', ((1, 'retval'),)))
    IADsADSystemInfo.get_IsNativeMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_IsNativeMode', ((1, 'retval'),)))
    IADsADSystemInfo.GetAnyDCName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'GetAnyDCName', ((1, 'pszDCName'),)))
    IADsADSystemInfo.GetDCSiteName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'GetDCSiteName', ((1, 'szServer'),(1, 'pszSiteName'),)))
    IADsADSystemInfo.RefreshSchemaCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'RefreshSchemaCache', ()))
    IADsADSystemInfo.GetTrees = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(19, 'GetTrees', ((1, 'pvTrees'),)))
    win32more.System.Com.IDispatch
    return IADsADSystemInfo
def _define_IADsWinNTSystemInfo_head():
    class IADsWinNTSystemInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('6c6d65dc-afd1-11d2-9cb9-0000f87a369e')
    return IADsWinNTSystemInfo
def _define_IADsWinNTSystemInfo():
    IADsWinNTSystemInfo = win32more.Networking.ActiveDirectory.IADsWinNTSystemInfo_head
    IADsWinNTSystemInfo.get_UserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_UserName', ((1, 'retval'),)))
    IADsWinNTSystemInfo.get_ComputerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ComputerName', ((1, 'retval'),)))
    IADsWinNTSystemInfo.get_DomainName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_DomainName', ((1, 'retval'),)))
    IADsWinNTSystemInfo.get_PDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_PDC', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return IADsWinNTSystemInfo
def _define_IADsDNWithBinary_head():
    class IADsDNWithBinary(win32more.System.Com.IDispatch_head):
        Guid = Guid('7e99c0a2-f935-11d2-ba96-00c04fb6d0d1')
    return IADsDNWithBinary
def _define_IADsDNWithBinary():
    IADsDNWithBinary = win32more.Networking.ActiveDirectory.IADsDNWithBinary_head
    IADsDNWithBinary.get_BinaryValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_BinaryValue', ((1, 'retval'),)))
    IADsDNWithBinary.put_BinaryValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_BinaryValue', ((1, 'vBinaryValue'),)))
    IADsDNWithBinary.get_DNString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_DNString', ((1, 'retval'),)))
    IADsDNWithBinary.put_DNString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_DNString', ((1, 'bstrDNString'),)))
    win32more.System.Com.IDispatch
    return IADsDNWithBinary
def _define_IADsDNWithString_head():
    class IADsDNWithString(win32more.System.Com.IDispatch_head):
        Guid = Guid('370df02e-f934-11d2-ba96-00c04fb6d0d1')
    return IADsDNWithString
def _define_IADsDNWithString():
    IADsDNWithString = win32more.Networking.ActiveDirectory.IADsDNWithString_head
    IADsDNWithString.get_StringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_StringValue', ((1, 'retval'),)))
    IADsDNWithString.put_StringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_StringValue', ((1, 'bstrStringValue'),)))
    IADsDNWithString.get_DNString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_DNString', ((1, 'retval'),)))
    IADsDNWithString.put_DNString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_DNString', ((1, 'bstrDNString'),)))
    win32more.System.Com.IDispatch
    return IADsDNWithString
def _define_IADsSecurityUtility_head():
    class IADsSecurityUtility(win32more.System.Com.IDispatch_head):
        Guid = Guid('a63251b2-5f21-474b-ab52-4a8efad10895')
    return IADsSecurityUtility
def _define_IADsSecurityUtility():
    IADsSecurityUtility = win32more.Networking.ActiveDirectory.IADsSecurityUtility_head
    IADsSecurityUtility.GetSecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'GetSecurityDescriptor', ((1, 'varPath'),(1, 'lPathFormat'),(1, 'lFormat'),(1, 'pVariant'),)))
    IADsSecurityUtility.SetSecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,Int32,win32more.System.Com.VARIANT,Int32, use_last_error=False)(8, 'SetSecurityDescriptor', ((1, 'varPath'),(1, 'lPathFormat'),(1, 'varData'),(1, 'lDataFormat'),)))
    IADsSecurityUtility.ConvertSecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'ConvertSecurityDescriptor', ((1, 'varSD'),(1, 'lDataFormat'),(1, 'lOutFormat'),(1, 'pResult'),)))
    IADsSecurityUtility.get_SecurityMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_SecurityMask', ((1, 'retval'),)))
    IADsSecurityUtility.put_SecurityMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'put_SecurityMask', ((1, 'lnSecurityMask'),)))
    win32more.System.Com.IDispatch
    return IADsSecurityUtility
def _define_DSOBJECT_head():
    class DSOBJECT(Structure):
        pass
    return DSOBJECT
def _define_DSOBJECT():
    DSOBJECT = win32more.Networking.ActiveDirectory.DSOBJECT_head
    DSOBJECT._fields_ = [
        ("dwFlags", UInt32),
        ("dwProviderFlags", UInt32),
        ("offsetName", UInt32),
        ("offsetClass", UInt32),
    ]
    return DSOBJECT
def _define_DSOBJECTNAMES_head():
    class DSOBJECTNAMES(Structure):
        pass
    return DSOBJECTNAMES
def _define_DSOBJECTNAMES():
    DSOBJECTNAMES = win32more.Networking.ActiveDirectory.DSOBJECTNAMES_head
    DSOBJECTNAMES._fields_ = [
        ("clsidNamespace", Guid),
        ("cItems", UInt32),
        ("aObjects", win32more.Networking.ActiveDirectory.DSOBJECT * 0),
    ]
    return DSOBJECTNAMES
def _define_DSDISPLAYSPECOPTIONS_head():
    class DSDISPLAYSPECOPTIONS(Structure):
        pass
    return DSDISPLAYSPECOPTIONS
def _define_DSDISPLAYSPECOPTIONS():
    DSDISPLAYSPECOPTIONS = win32more.Networking.ActiveDirectory.DSDISPLAYSPECOPTIONS_head
    DSDISPLAYSPECOPTIONS._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("offsetAttribPrefix", UInt32),
        ("offsetUserName", UInt32),
        ("offsetPassword", UInt32),
        ("offsetServer", UInt32),
        ("offsetServerConfigPath", UInt32),
    ]
    return DSDISPLAYSPECOPTIONS
def _define_DSPROPERTYPAGEINFO_head():
    class DSPROPERTYPAGEINFO(Structure):
        pass
    return DSPROPERTYPAGEINFO
def _define_DSPROPERTYPAGEINFO():
    DSPROPERTYPAGEINFO = win32more.Networking.ActiveDirectory.DSPROPERTYPAGEINFO_head
    DSPROPERTYPAGEINFO._fields_ = [
        ("offsetString", UInt32),
    ]
    return DSPROPERTYPAGEINFO
def _define_DOMAINDESC_head():
    class DOMAINDESC(Structure):
        pass
    return DOMAINDESC
def _define_DOMAINDESC():
    DOMAINDESC = win32more.Networking.ActiveDirectory.DOMAINDESC_head
    DOMAINDESC._fields_ = [
        ("pszName", win32more.Foundation.PWSTR),
        ("pszPath", win32more.Foundation.PWSTR),
        ("pszNCName", win32more.Foundation.PWSTR),
        ("pszTrustParent", win32more.Foundation.PWSTR),
        ("pszObjectClass", win32more.Foundation.PWSTR),
        ("ulFlags", UInt32),
        ("fDownLevel", win32more.Foundation.BOOL),
        ("pdChildList", POINTER(win32more.Networking.ActiveDirectory.DOMAINDESC_head)),
        ("pdNextSibling", POINTER(win32more.Networking.ActiveDirectory.DOMAINDESC_head)),
    ]
    return DOMAINDESC
def _define_DOMAIN_TREE_head():
    class DOMAIN_TREE(Structure):
        pass
    return DOMAIN_TREE
def _define_DOMAIN_TREE():
    DOMAIN_TREE = win32more.Networking.ActiveDirectory.DOMAIN_TREE_head
    DOMAIN_TREE._fields_ = [
        ("dsSize", UInt32),
        ("dwCount", UInt32),
        ("aDomains", win32more.Networking.ActiveDirectory.DOMAINDESC * 0),
    ]
    return DOMAIN_TREE
def _define_IDsBrowseDomainTree_head():
    class IDsBrowseDomainTree(win32more.System.Com.IUnknown_head):
        Guid = Guid('7cabcf1e-78f5-11d2-960c-00c04fa31a86')
    return IDsBrowseDomainTree
def _define_IDsBrowseDomainTree():
    IDsBrowseDomainTree = win32more.Networking.ActiveDirectory.IDsBrowseDomainTree_head
    IDsBrowseDomainTree.BrowseTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.PWSTR),UInt32, use_last_error=False)(3, 'BrowseTo', ((1, 'hwndParent'),(1, 'ppszTargetPath'),(1, 'dwFlags'),)))
    IDsBrowseDomainTree.GetDomains = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Networking.ActiveDirectory.DOMAIN_TREE_head)),UInt32, use_last_error=False)(4, 'GetDomains', ((1, 'ppDomainTree'),(1, 'dwFlags'),)))
    IDsBrowseDomainTree.FreeDomains = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Networking.ActiveDirectory.DOMAIN_TREE_head)), use_last_error=False)(5, 'FreeDomains', ((1, 'ppDomainTree'),)))
    IDsBrowseDomainTree.FlushCachedDomains = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'FlushCachedDomains', ()))
    IDsBrowseDomainTree.SetComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(7, 'SetComputer', ((1, 'pszComputerName'),(1, 'pszUserName'),(1, 'pszPassword'),)))
    win32more.System.Com.IUnknown
    return IDsBrowseDomainTree
def _define_LPDSENUMATTRIBUTES():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LPARAM,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)
def _define_DSCLASSCREATIONINFO_head():
    class DSCLASSCREATIONINFO(Structure):
        pass
    return DSCLASSCREATIONINFO
def _define_DSCLASSCREATIONINFO():
    DSCLASSCREATIONINFO = win32more.Networking.ActiveDirectory.DSCLASSCREATIONINFO_head
    DSCLASSCREATIONINFO._fields_ = [
        ("dwFlags", UInt32),
        ("clsidWizardDialog", Guid),
        ("clsidWizardPrimaryPage", Guid),
        ("cWizardExtensions", UInt32),
        ("aWizardExtensions", Guid * 0),
    ]
    return DSCLASSCREATIONINFO
def _define_IDsDisplaySpecifier_head():
    class IDsDisplaySpecifier(win32more.System.Com.IUnknown_head):
        Guid = Guid('1ab4a8c0-6a0b-11d2-ad49-00c04fa31a86')
    return IDsDisplaySpecifier
def _define_IDsDisplaySpecifier():
    IDsDisplaySpecifier = win32more.Networking.ActiveDirectory.IDsDisplaySpecifier_head
    IDsDisplaySpecifier.SetServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(3, 'SetServer', ((1, 'pszServer'),(1, 'pszUserName'),(1, 'pszPassword'),(1, 'dwFlags'),)))
    IDsDisplaySpecifier.SetLanguageID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(4, 'SetLanguageID', ((1, 'langid'),)))
    IDsDisplaySpecifier.GetDisplaySpecifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(5, 'GetDisplaySpecifier', ((1, 'pszObjectClass'),(1, 'riid'),(1, 'ppv'),)))
    IDsDisplaySpecifier.GetIconLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(Char),Int32,POINTER(Int32), use_last_error=False)(6, 'GetIconLocation', ((1, 'pszObjectClass'),(1, 'dwFlags'),(1, 'pszBuffer'),(1, 'cchBuffer'),(1, 'presid'),)))
    IDsDisplaySpecifier.GetIcon = COMMETHOD(WINFUNCTYPE(win32more.UI.WindowsAndMessaging.HICON,win32more.Foundation.PWSTR,UInt32,Int32,Int32, use_last_error=False)(7, 'GetIcon', ((1, 'pszObjectClass'),(1, 'dwFlags'),(1, 'cxIcon'),(1, 'cyIcon'),)))
    IDsDisplaySpecifier.GetFriendlyClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Char),Int32, use_last_error=False)(8, 'GetFriendlyClassName', ((1, 'pszObjectClass'),(1, 'pszBuffer'),(1, 'cchBuffer'),)))
    IDsDisplaySpecifier.GetFriendlyAttributeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Char),UInt32, use_last_error=False)(9, 'GetFriendlyAttributeName', ((1, 'pszObjectClass'),(1, 'pszAttributeName'),(1, 'pszBuffer'),(1, 'cchBuffer'),)))
    IDsDisplaySpecifier.IsClassContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(10, 'IsClassContainer', ((1, 'pszObjectClass'),(1, 'pszADsPath'),(1, 'dwFlags'),)))
    IDsDisplaySpecifier.GetClassCreationInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.ActiveDirectory.DSCLASSCREATIONINFO_head)), use_last_error=False)(11, 'GetClassCreationInfo', ((1, 'pszObjectClass'),(1, 'ppdscci'),)))
    IDsDisplaySpecifier.EnumClassAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Networking.ActiveDirectory.LPDSENUMATTRIBUTES,win32more.Foundation.LPARAM, use_last_error=False)(12, 'EnumClassAttributes', ((1, 'pszObjectClass'),(1, 'pcbEnum'),(1, 'lParam'),)))
    IDsDisplaySpecifier.GetAttributeADsType = COMMETHOD(WINFUNCTYPE(win32more.Networking.ActiveDirectory.ADSTYPEENUM,win32more.Foundation.PWSTR, use_last_error=False)(13, 'GetAttributeADsType', ((1, 'pszAttributeName'),)))
    win32more.System.Com.IUnknown
    return IDsDisplaySpecifier
def _define_DSBROWSEINFOW_head():
    class DSBROWSEINFOW(Structure):
        pass
    return DSBROWSEINFOW
def _define_DSBROWSEINFOW():
    DSBROWSEINFOW = win32more.Networking.ActiveDirectory.DSBROWSEINFOW_head
    DSBROWSEINFOW._fields_ = [
        ("cbStruct", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("pszCaption", win32more.Foundation.PWSTR),
        ("pszTitle", win32more.Foundation.PWSTR),
        ("pszRoot", win32more.Foundation.PWSTR),
        ("pszPath", win32more.Foundation.PWSTR),
        ("cchPath", UInt32),
        ("dwFlags", UInt32),
        ("pfnCallback", win32more.UI.Shell.BFFCALLBACK),
        ("lParam", win32more.Foundation.LPARAM),
        ("dwReturnFormat", UInt32),
        ("pUserName", win32more.Foundation.PWSTR),
        ("pPassword", win32more.Foundation.PWSTR),
        ("pszObjectClass", win32more.Foundation.PWSTR),
        ("cchObjectClass", UInt32),
    ]
    return DSBROWSEINFOW
def _define_DSBROWSEINFOA_head():
    class DSBROWSEINFOA(Structure):
        pass
    return DSBROWSEINFOA
def _define_DSBROWSEINFOA():
    DSBROWSEINFOA = win32more.Networking.ActiveDirectory.DSBROWSEINFOA_head
    DSBROWSEINFOA._fields_ = [
        ("cbStruct", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("pszCaption", win32more.Foundation.PSTR),
        ("pszTitle", win32more.Foundation.PSTR),
        ("pszRoot", win32more.Foundation.PWSTR),
        ("pszPath", win32more.Foundation.PWSTR),
        ("cchPath", UInt32),
        ("dwFlags", UInt32),
        ("pfnCallback", win32more.UI.Shell.BFFCALLBACK),
        ("lParam", win32more.Foundation.LPARAM),
        ("dwReturnFormat", UInt32),
        ("pUserName", win32more.Foundation.PWSTR),
        ("pPassword", win32more.Foundation.PWSTR),
        ("pszObjectClass", win32more.Foundation.PWSTR),
        ("cchObjectClass", UInt32),
    ]
    return DSBROWSEINFOA
def _define_DSBITEMW_head():
    class DSBITEMW(Structure):
        pass
    return DSBITEMW
def _define_DSBITEMW():
    DSBITEMW = win32more.Networking.ActiveDirectory.DSBITEMW_head
    DSBITEMW._fields_ = [
        ("cbStruct", UInt32),
        ("pszADsPath", win32more.Foundation.PWSTR),
        ("pszClass", win32more.Foundation.PWSTR),
        ("dwMask", UInt32),
        ("dwState", UInt32),
        ("dwStateMask", UInt32),
        ("szDisplayName", Char * 64),
        ("szIconLocation", Char * 260),
        ("iIconResID", Int32),
    ]
    return DSBITEMW
def _define_DSBITEMA_head():
    class DSBITEMA(Structure):
        pass
    return DSBITEMA
def _define_DSBITEMA():
    DSBITEMA = win32more.Networking.ActiveDirectory.DSBITEMA_head
    DSBITEMA._fields_ = [
        ("cbStruct", UInt32),
        ("pszADsPath", win32more.Foundation.PWSTR),
        ("pszClass", win32more.Foundation.PWSTR),
        ("dwMask", UInt32),
        ("dwState", UInt32),
        ("dwStateMask", UInt32),
        ("szDisplayName", win32more.Foundation.CHAR * 64),
        ("szIconLocation", win32more.Foundation.CHAR * 260),
        ("iIconResID", Int32),
    ]
    return DSBITEMA
def _define_DSOP_UPLEVEL_FILTER_FLAGS_head():
    class DSOP_UPLEVEL_FILTER_FLAGS(Structure):
        pass
    return DSOP_UPLEVEL_FILTER_FLAGS
def _define_DSOP_UPLEVEL_FILTER_FLAGS():
    DSOP_UPLEVEL_FILTER_FLAGS = win32more.Networking.ActiveDirectory.DSOP_UPLEVEL_FILTER_FLAGS_head
    DSOP_UPLEVEL_FILTER_FLAGS._fields_ = [
        ("flBothModes", UInt32),
        ("flMixedModeOnly", UInt32),
        ("flNativeModeOnly", UInt32),
    ]
    return DSOP_UPLEVEL_FILTER_FLAGS
def _define_DSOP_FILTER_FLAGS_head():
    class DSOP_FILTER_FLAGS(Structure):
        pass
    return DSOP_FILTER_FLAGS
def _define_DSOP_FILTER_FLAGS():
    DSOP_FILTER_FLAGS = win32more.Networking.ActiveDirectory.DSOP_FILTER_FLAGS_head
    DSOP_FILTER_FLAGS._fields_ = [
        ("Uplevel", win32more.Networking.ActiveDirectory.DSOP_UPLEVEL_FILTER_FLAGS),
        ("flDownlevel", UInt32),
    ]
    return DSOP_FILTER_FLAGS
def _define_DSOP_SCOPE_INIT_INFO_head():
    class DSOP_SCOPE_INIT_INFO(Structure):
        pass
    return DSOP_SCOPE_INIT_INFO
def _define_DSOP_SCOPE_INIT_INFO():
    DSOP_SCOPE_INIT_INFO = win32more.Networking.ActiveDirectory.DSOP_SCOPE_INIT_INFO_head
    DSOP_SCOPE_INIT_INFO._fields_ = [
        ("cbSize", UInt32),
        ("flType", UInt32),
        ("flScope", UInt32),
        ("FilterFlags", win32more.Networking.ActiveDirectory.DSOP_FILTER_FLAGS),
        ("pwzDcName", win32more.Foundation.PWSTR),
        ("pwzADsPath", win32more.Foundation.PWSTR),
        ("hr", win32more.Foundation.HRESULT),
    ]
    return DSOP_SCOPE_INIT_INFO
def _define_DSOP_INIT_INFO_head():
    class DSOP_INIT_INFO(Structure):
        pass
    return DSOP_INIT_INFO
def _define_DSOP_INIT_INFO():
    DSOP_INIT_INFO = win32more.Networking.ActiveDirectory.DSOP_INIT_INFO_head
    DSOP_INIT_INFO._fields_ = [
        ("cbSize", UInt32),
        ("pwzTargetComputer", win32more.Foundation.PWSTR),
        ("cDsScopeInfos", UInt32),
        ("aDsScopeInfos", POINTER(win32more.Networking.ActiveDirectory.DSOP_SCOPE_INIT_INFO_head)),
        ("flOptions", UInt32),
        ("cAttributesToFetch", UInt32),
        ("apwzAttributeNames", POINTER(win32more.Foundation.PWSTR)),
    ]
    return DSOP_INIT_INFO
def _define_DS_SELECTION_head():
    class DS_SELECTION(Structure):
        pass
    return DS_SELECTION
def _define_DS_SELECTION():
    DS_SELECTION = win32more.Networking.ActiveDirectory.DS_SELECTION_head
    DS_SELECTION._fields_ = [
        ("pwzName", win32more.Foundation.PWSTR),
        ("pwzADsPath", win32more.Foundation.PWSTR),
        ("pwzClass", win32more.Foundation.PWSTR),
        ("pwzUPN", win32more.Foundation.PWSTR),
        ("pvarFetchedAttributes", POINTER(win32more.System.Com.VARIANT_head)),
        ("flScopeType", UInt32),
    ]
    return DS_SELECTION
def _define_DS_SELECTION_LIST_head():
    class DS_SELECTION_LIST(Structure):
        pass
    return DS_SELECTION_LIST
def _define_DS_SELECTION_LIST():
    DS_SELECTION_LIST = win32more.Networking.ActiveDirectory.DS_SELECTION_LIST_head
    DS_SELECTION_LIST._fields_ = [
        ("cItems", UInt32),
        ("cFetchedAttributes", UInt32),
        ("aDsSelection", win32more.Networking.ActiveDirectory.DS_SELECTION * 0),
    ]
    return DS_SELECTION_LIST
def _define_IDsObjectPicker_head():
    class IDsObjectPicker(win32more.System.Com.IUnknown_head):
        Guid = Guid('0c87e64e-3b7a-11d2-b9e0-00c04fd8dbf7')
    return IDsObjectPicker
def _define_IDsObjectPicker():
    IDsObjectPicker = win32more.Networking.ActiveDirectory.IDsObjectPicker_head
    IDsObjectPicker.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.DSOP_INIT_INFO_head), use_last_error=False)(3, 'Initialize', ((1, 'pInitInfo'),)))
    IDsObjectPicker.InvokeDialog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(4, 'InvokeDialog', ((1, 'hwndParent'),(1, 'ppdoSelections'),)))
    win32more.System.Com.IUnknown
    return IDsObjectPicker
def _define_IDsObjectPickerCredentials_head():
    class IDsObjectPickerCredentials(win32more.Networking.ActiveDirectory.IDsObjectPicker_head):
        Guid = Guid('e2d3ec9b-d041-445a-8f16-4748de8fb1cf')
    return IDsObjectPickerCredentials
def _define_IDsObjectPickerCredentials():
    IDsObjectPickerCredentials = win32more.Networking.ActiveDirectory.IDsObjectPickerCredentials_head
    IDsObjectPickerCredentials.SetCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetCredentials', ((1, 'szUserName'),(1, 'szPassword'),)))
    win32more.Networking.ActiveDirectory.IDsObjectPicker
    return IDsObjectPickerCredentials
def _define_DSQUERYINITPARAMS_head():
    class DSQUERYINITPARAMS(Structure):
        pass
    return DSQUERYINITPARAMS
def _define_DSQUERYINITPARAMS():
    DSQUERYINITPARAMS = win32more.Networking.ActiveDirectory.DSQUERYINITPARAMS_head
    DSQUERYINITPARAMS._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("pDefaultScope", win32more.Foundation.PWSTR),
        ("pDefaultSaveLocation", win32more.Foundation.PWSTR),
        ("pUserName", win32more.Foundation.PWSTR),
        ("pPassword", win32more.Foundation.PWSTR),
        ("pServer", win32more.Foundation.PWSTR),
    ]
    return DSQUERYINITPARAMS
def _define_DSCOLUMN_head():
    class DSCOLUMN(Structure):
        pass
    return DSCOLUMN
def _define_DSCOLUMN():
    DSCOLUMN = win32more.Networking.ActiveDirectory.DSCOLUMN_head
    DSCOLUMN._fields_ = [
        ("dwFlags", UInt32),
        ("fmt", Int32),
        ("cx", Int32),
        ("idsName", Int32),
        ("offsetProperty", Int32),
        ("dwReserved", UInt32),
    ]
    return DSCOLUMN
def _define_DSQUERYPARAMS_head():
    class DSQUERYPARAMS(Structure):
        pass
    return DSQUERYPARAMS
def _define_DSQUERYPARAMS():
    DSQUERYPARAMS = win32more.Networking.ActiveDirectory.DSQUERYPARAMS_head
    DSQUERYPARAMS._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("offsetQuery", Int32),
        ("iColumns", Int32),
        ("dwReserved", UInt32),
        ("aColumns", win32more.Networking.ActiveDirectory.DSCOLUMN * 0),
    ]
    return DSQUERYPARAMS
def _define_DSQUERYCLASSLIST_head():
    class DSQUERYCLASSLIST(Structure):
        pass
    return DSQUERYCLASSLIST
def _define_DSQUERYCLASSLIST():
    DSQUERYCLASSLIST = win32more.Networking.ActiveDirectory.DSQUERYCLASSLIST_head
    DSQUERYCLASSLIST._fields_ = [
        ("cbStruct", UInt32),
        ("cClasses", Int32),
        ("offsetClass", UInt32 * 0),
    ]
    return DSQUERYCLASSLIST
def _define_IDsAdminCreateObj_head():
    class IDsAdminCreateObj(win32more.System.Com.IUnknown_head):
        Guid = Guid('53554a38-f902-11d2-82b9-00c04f68928b')
    return IDsAdminCreateObj
def _define_IDsAdminCreateObj():
    IDsAdminCreateObj = win32more.Networking.ActiveDirectory.IDsAdminCreateObj_head
    IDsAdminCreateObj.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.ActiveDirectory.IADsContainer_head,win32more.Networking.ActiveDirectory.IADs_head,win32more.Foundation.PWSTR, use_last_error=False)(3, 'Initialize', ((1, 'pADsContainerObj'),(1, 'pADsCopySource'),(1, 'lpszClassName'),)))
    IDsAdminCreateObj.CreateModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Networking.ActiveDirectory.IADs_head), use_last_error=False)(4, 'CreateModal', ((1, 'hwndParent'),(1, 'ppADsObj'),)))
    win32more.System.Com.IUnknown
    return IDsAdminCreateObj
def _define_IDsAdminNewObj_head():
    class IDsAdminNewObj(win32more.System.Com.IUnknown_head):
        Guid = Guid('f2573587-e6fc-11d2-82af-00c04f68928b')
    return IDsAdminNewObj
def _define_IDsAdminNewObj():
    IDsAdminNewObj = win32more.Networking.ActiveDirectory.IDsAdminNewObj_head
    IDsAdminNewObj.SetButtons = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL, use_last_error=False)(3, 'SetButtons', ((1, 'nCurrIndex'),(1, 'bValid'),)))
    IDsAdminNewObj.GetPageCounts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32), use_last_error=False)(4, 'GetPageCounts', ((1, 'pnTotal'),(1, 'pnStartIndex'),)))
    win32more.System.Com.IUnknown
    return IDsAdminNewObj
def _define_IDsAdminNewObjPrimarySite_head():
    class IDsAdminNewObjPrimarySite(win32more.System.Com.IUnknown_head):
        Guid = Guid('be2b487e-f904-11d2-82b9-00c04f68928b')
    return IDsAdminNewObjPrimarySite
def _define_IDsAdminNewObjPrimarySite():
    IDsAdminNewObjPrimarySite = win32more.Networking.ActiveDirectory.IDsAdminNewObjPrimarySite_head
    IDsAdminNewObjPrimarySite.CreateNew = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'CreateNew', ((1, 'pszName'),)))
    IDsAdminNewObjPrimarySite.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Commit', ()))
    win32more.System.Com.IUnknown
    return IDsAdminNewObjPrimarySite
def _define_DSA_NEWOBJ_DISPINFO_head():
    class DSA_NEWOBJ_DISPINFO(Structure):
        pass
    return DSA_NEWOBJ_DISPINFO
def _define_DSA_NEWOBJ_DISPINFO():
    DSA_NEWOBJ_DISPINFO = win32more.Networking.ActiveDirectory.DSA_NEWOBJ_DISPINFO_head
    DSA_NEWOBJ_DISPINFO._fields_ = [
        ("dwSize", UInt32),
        ("hObjClassIcon", win32more.UI.WindowsAndMessaging.HICON),
        ("lpszWizTitle", win32more.Foundation.PWSTR),
        ("lpszContDisplayName", win32more.Foundation.PWSTR),
    ]
    return DSA_NEWOBJ_DISPINFO
def _define_IDsAdminNewObjExt_head():
    class IDsAdminNewObjExt(win32more.System.Com.IUnknown_head):
        Guid = Guid('6088eae2-e7bf-11d2-82af-00c04f68928b')
    return IDsAdminNewObjExt
def _define_IDsAdminNewObjExt():
    IDsAdminNewObjExt = win32more.Networking.ActiveDirectory.IDsAdminNewObjExt_head
    IDsAdminNewObjExt.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.ActiveDirectory.IADsContainer_head,win32more.Networking.ActiveDirectory.IADs_head,win32more.Foundation.PWSTR,win32more.Networking.ActiveDirectory.IDsAdminNewObj_head,POINTER(win32more.Networking.ActiveDirectory.DSA_NEWOBJ_DISPINFO_head), use_last_error=False)(3, 'Initialize', ((1, 'pADsContainerObj'),(1, 'pADsCopySource'),(1, 'lpszClassName'),(1, 'pDsAdminNewObj'),(1, 'pDispInfo'),)))
    IDsAdminNewObjExt.AddPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.LPFNSVADDPROPSHEETPAGE,win32more.Foundation.LPARAM, use_last_error=False)(4, 'AddPages', ((1, 'lpfnAddPage'),(1, 'lParam'),)))
    IDsAdminNewObjExt.SetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.ActiveDirectory.IADs_head, use_last_error=False)(5, 'SetObject', ((1, 'pADsObj'),)))
    IDsAdminNewObjExt.WriteData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32, use_last_error=False)(6, 'WriteData', ((1, 'hWnd'),(1, 'uContext'),)))
    IDsAdminNewObjExt.OnError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'OnError', ((1, 'hWnd'),(1, 'hr'),(1, 'uContext'),)))
    IDsAdminNewObjExt.GetSummaryInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetSummaryInfo', ((1, 'pBstrText'),)))
    win32more.System.Com.IUnknown
    return IDsAdminNewObjExt
def _define_IDsAdminNotifyHandler_head():
    class IDsAdminNotifyHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('e4a2b8b3-5a18-11d2-97c1-00a0c9a06d2d')
    return IDsAdminNotifyHandler
def _define_IDsAdminNotifyHandler():
    IDsAdminNotifyHandler = win32more.Networking.ActiveDirectory.IDsAdminNotifyHandler_head
    IDsAdminNotifyHandler.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,POINTER(UInt32), use_last_error=False)(3, 'Initialize', ((1, 'pExtraInfo'),(1, 'puEventFlags'),)))
    IDsAdminNotifyHandler.Begin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IDataObject_head,win32more.System.Com.IDataObject_head,POINTER(UInt32),POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'Begin', ((1, 'uEvent'),(1, 'pArg1'),(1, 'pArg2'),(1, 'puFlags'),(1, 'pBstr'),)))
    IDsAdminNotifyHandler.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(5, 'Notify', ((1, 'nItem'),(1, 'uFlags'),)))
    IDsAdminNotifyHandler.End = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'End', ()))
    win32more.System.Com.IUnknown
    return IDsAdminNotifyHandler
def _define_ADSPROPINITPARAMS_head():
    class ADSPROPINITPARAMS(Structure):
        pass
    return ADSPROPINITPARAMS
def _define_ADSPROPINITPARAMS():
    ADSPROPINITPARAMS = win32more.Networking.ActiveDirectory.ADSPROPINITPARAMS_head
    ADSPROPINITPARAMS._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("hr", win32more.Foundation.HRESULT),
        ("pDsObj", win32more.Networking.ActiveDirectory.IDirectoryObject_head),
        ("pwzCN", win32more.Foundation.PWSTR),
        ("pWritableAttrs", POINTER(win32more.Networking.ActiveDirectory.ADS_ATTR_INFO_head)),
    ]
    return ADSPROPINITPARAMS
def _define_ADSPROPERROR_head():
    class ADSPROPERROR(Structure):
        pass
    return ADSPROPERROR
def _define_ADSPROPERROR():
    ADSPROPERROR = win32more.Networking.ActiveDirectory.ADSPROPERROR_head
    ADSPROPERROR._fields_ = [
        ("hwndPage", win32more.Foundation.HWND),
        ("pszPageTitle", win32more.Foundation.PWSTR),
        ("pszObjPath", win32more.Foundation.PWSTR),
        ("pszObjClass", win32more.Foundation.PWSTR),
        ("hr", win32more.Foundation.HRESULT),
        ("pszError", win32more.Foundation.PWSTR),
    ]
    return ADSPROPERROR
def _define_SCHEDULE_HEADER_head():
    class SCHEDULE_HEADER(Structure):
        pass
    return SCHEDULE_HEADER
def _define_SCHEDULE_HEADER():
    SCHEDULE_HEADER = win32more.Networking.ActiveDirectory.SCHEDULE_HEADER_head
    SCHEDULE_HEADER._fields_ = [
        ("Type", UInt32),
        ("Offset", UInt32),
    ]
    return SCHEDULE_HEADER
def _define_SCHEDULE_head():
    class SCHEDULE(Structure):
        pass
    return SCHEDULE
def _define_SCHEDULE():
    SCHEDULE = win32more.Networking.ActiveDirectory.SCHEDULE_head
    SCHEDULE._fields_ = [
        ("Size", UInt32),
        ("Bandwidth", UInt32),
        ("NumberOfSchedules", UInt32),
        ("Schedules", win32more.Networking.ActiveDirectory.SCHEDULE_HEADER * 0),
    ]
    return SCHEDULE
DS_MANGLE_FOR = Int32
DS_MANGLE_UNKNOWN = 0
DS_MANGLE_OBJECT_RDN_FOR_DELETION = 1
DS_MANGLE_OBJECT_RDN_FOR_NAME_CONFLICT = 2
DS_NAME_FORMAT = Int32
DS_UNKNOWN_NAME = 0
DS_FQDN_1779_NAME = 1
DS_NT4_ACCOUNT_NAME = 2
DS_DISPLAY_NAME = 3
DS_UNIQUE_ID_NAME = 6
DS_CANONICAL_NAME = 7
DS_USER_PRINCIPAL_NAME = 8
DS_CANONICAL_NAME_EX = 9
DS_SERVICE_PRINCIPAL_NAME = 10
DS_SID_OR_SID_HISTORY_NAME = 11
DS_DNS_DOMAIN_NAME = 12
DS_NAME_FLAGS = Int32
DS_NAME_NO_FLAGS = 0
DS_NAME_FLAG_SYNTACTICAL_ONLY = 1
DS_NAME_FLAG_EVAL_AT_DC = 2
DS_NAME_FLAG_GCVERIFY = 4
DS_NAME_FLAG_TRUST_REFERRAL = 8
DS_NAME_ERROR = Int32
DS_NAME_NO_ERROR = 0
DS_NAME_ERROR_RESOLVING = 1
DS_NAME_ERROR_NOT_FOUND = 2
DS_NAME_ERROR_NOT_UNIQUE = 3
DS_NAME_ERROR_NO_MAPPING = 4
DS_NAME_ERROR_DOMAIN_ONLY = 5
DS_NAME_ERROR_NO_SYNTACTICAL_MAPPING = 6
DS_NAME_ERROR_TRUST_REFERRAL = 7
DS_SPN_NAME_TYPE = Int32
DS_SPN_DNS_HOST = 0
DS_SPN_DN_HOST = 1
DS_SPN_NB_HOST = 2
DS_SPN_DOMAIN = 3
DS_SPN_NB_DOMAIN = 4
DS_SPN_SERVICE = 5
DS_SPN_WRITE_OP = Int32
DS_SPN_ADD_SPN_OP = 0
DS_SPN_REPLACE_SPN_OP = 1
DS_SPN_DELETE_SPN_OP = 2
def _define_DS_NAME_RESULT_ITEMA_head():
    class DS_NAME_RESULT_ITEMA(Structure):
        pass
    return DS_NAME_RESULT_ITEMA
def _define_DS_NAME_RESULT_ITEMA():
    DS_NAME_RESULT_ITEMA = win32more.Networking.ActiveDirectory.DS_NAME_RESULT_ITEMA_head
    DS_NAME_RESULT_ITEMA._fields_ = [
        ("status", UInt32),
        ("pDomain", win32more.Foundation.PSTR),
        ("pName", win32more.Foundation.PSTR),
    ]
    return DS_NAME_RESULT_ITEMA
def _define_DS_NAME_RESULTA_head():
    class DS_NAME_RESULTA(Structure):
        pass
    return DS_NAME_RESULTA
def _define_DS_NAME_RESULTA():
    DS_NAME_RESULTA = win32more.Networking.ActiveDirectory.DS_NAME_RESULTA_head
    DS_NAME_RESULTA._fields_ = [
        ("cItems", UInt32),
        ("rItems", POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULT_ITEMA_head)),
    ]
    return DS_NAME_RESULTA
def _define_DS_NAME_RESULT_ITEMW_head():
    class DS_NAME_RESULT_ITEMW(Structure):
        pass
    return DS_NAME_RESULT_ITEMW
def _define_DS_NAME_RESULT_ITEMW():
    DS_NAME_RESULT_ITEMW = win32more.Networking.ActiveDirectory.DS_NAME_RESULT_ITEMW_head
    DS_NAME_RESULT_ITEMW._fields_ = [
        ("status", UInt32),
        ("pDomain", win32more.Foundation.PWSTR),
        ("pName", win32more.Foundation.PWSTR),
    ]
    return DS_NAME_RESULT_ITEMW
def _define_DS_NAME_RESULTW_head():
    class DS_NAME_RESULTW(Structure):
        pass
    return DS_NAME_RESULTW
def _define_DS_NAME_RESULTW():
    DS_NAME_RESULTW = win32more.Networking.ActiveDirectory.DS_NAME_RESULTW_head
    DS_NAME_RESULTW._fields_ = [
        ("cItems", UInt32),
        ("rItems", POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULT_ITEMW_head)),
    ]
    return DS_NAME_RESULTW
DS_REPSYNCALL_ERROR = Int32
DS_REPSYNCALL_WIN32_ERROR_CONTACTING_SERVER = 0
DS_REPSYNCALL_WIN32_ERROR_REPLICATING = 1
DS_REPSYNCALL_SERVER_UNREACHABLE = 2
DS_REPSYNCALL_EVENT = Int32
DS_REPSYNCALL_EVENT_ERROR = 0
DS_REPSYNCALL_EVENT_SYNC_STARTED = 1
DS_REPSYNCALL_EVENT_SYNC_COMPLETED = 2
DS_REPSYNCALL_EVENT_FINISHED = 3
def _define_DS_REPSYNCALL_SYNCA_head():
    class DS_REPSYNCALL_SYNCA(Structure):
        pass
    return DS_REPSYNCALL_SYNCA
def _define_DS_REPSYNCALL_SYNCA():
    DS_REPSYNCALL_SYNCA = win32more.Networking.ActiveDirectory.DS_REPSYNCALL_SYNCA_head
    DS_REPSYNCALL_SYNCA._fields_ = [
        ("pszSrcId", win32more.Foundation.PSTR),
        ("pszDstId", win32more.Foundation.PSTR),
        ("pszNC", win32more.Foundation.PSTR),
        ("pguidSrc", POINTER(Guid)),
        ("pguidDst", POINTER(Guid)),
    ]
    return DS_REPSYNCALL_SYNCA
def _define_DS_REPSYNCALL_SYNCW_head():
    class DS_REPSYNCALL_SYNCW(Structure):
        pass
    return DS_REPSYNCALL_SYNCW
def _define_DS_REPSYNCALL_SYNCW():
    DS_REPSYNCALL_SYNCW = win32more.Networking.ActiveDirectory.DS_REPSYNCALL_SYNCW_head
    DS_REPSYNCALL_SYNCW._fields_ = [
        ("pszSrcId", win32more.Foundation.PWSTR),
        ("pszDstId", win32more.Foundation.PWSTR),
        ("pszNC", win32more.Foundation.PWSTR),
        ("pguidSrc", POINTER(Guid)),
        ("pguidDst", POINTER(Guid)),
    ]
    return DS_REPSYNCALL_SYNCW
def _define_DS_REPSYNCALL_ERRINFOA_head():
    class DS_REPSYNCALL_ERRINFOA(Structure):
        pass
    return DS_REPSYNCALL_ERRINFOA
def _define_DS_REPSYNCALL_ERRINFOA():
    DS_REPSYNCALL_ERRINFOA = win32more.Networking.ActiveDirectory.DS_REPSYNCALL_ERRINFOA_head
    DS_REPSYNCALL_ERRINFOA._fields_ = [
        ("pszSvrId", win32more.Foundation.PSTR),
        ("error", win32more.Networking.ActiveDirectory.DS_REPSYNCALL_ERROR),
        ("dwWin32Err", UInt32),
        ("pszSrcId", win32more.Foundation.PSTR),
    ]
    return DS_REPSYNCALL_ERRINFOA
def _define_DS_REPSYNCALL_ERRINFOW_head():
    class DS_REPSYNCALL_ERRINFOW(Structure):
        pass
    return DS_REPSYNCALL_ERRINFOW
def _define_DS_REPSYNCALL_ERRINFOW():
    DS_REPSYNCALL_ERRINFOW = win32more.Networking.ActiveDirectory.DS_REPSYNCALL_ERRINFOW_head
    DS_REPSYNCALL_ERRINFOW._fields_ = [
        ("pszSvrId", win32more.Foundation.PWSTR),
        ("error", win32more.Networking.ActiveDirectory.DS_REPSYNCALL_ERROR),
        ("dwWin32Err", UInt32),
        ("pszSrcId", win32more.Foundation.PWSTR),
    ]
    return DS_REPSYNCALL_ERRINFOW
def _define_DS_REPSYNCALL_UPDATEA_head():
    class DS_REPSYNCALL_UPDATEA(Structure):
        pass
    return DS_REPSYNCALL_UPDATEA
def _define_DS_REPSYNCALL_UPDATEA():
    DS_REPSYNCALL_UPDATEA = win32more.Networking.ActiveDirectory.DS_REPSYNCALL_UPDATEA_head
    DS_REPSYNCALL_UPDATEA._fields_ = [
        ("event", win32more.Networking.ActiveDirectory.DS_REPSYNCALL_EVENT),
        ("pErrInfo", POINTER(win32more.Networking.ActiveDirectory.DS_REPSYNCALL_ERRINFOA_head)),
        ("pSync", POINTER(win32more.Networking.ActiveDirectory.DS_REPSYNCALL_SYNCA_head)),
    ]
    return DS_REPSYNCALL_UPDATEA
def _define_DS_REPSYNCALL_UPDATEW_head():
    class DS_REPSYNCALL_UPDATEW(Structure):
        pass
    return DS_REPSYNCALL_UPDATEW
def _define_DS_REPSYNCALL_UPDATEW():
    DS_REPSYNCALL_UPDATEW = win32more.Networking.ActiveDirectory.DS_REPSYNCALL_UPDATEW_head
    DS_REPSYNCALL_UPDATEW._fields_ = [
        ("event", win32more.Networking.ActiveDirectory.DS_REPSYNCALL_EVENT),
        ("pErrInfo", POINTER(win32more.Networking.ActiveDirectory.DS_REPSYNCALL_ERRINFOW_head)),
        ("pSync", POINTER(win32more.Networking.ActiveDirectory.DS_REPSYNCALL_SYNCW_head)),
    ]
    return DS_REPSYNCALL_UPDATEW
def _define_DS_SITE_COST_INFO_head():
    class DS_SITE_COST_INFO(Structure):
        pass
    return DS_SITE_COST_INFO
def _define_DS_SITE_COST_INFO():
    DS_SITE_COST_INFO = win32more.Networking.ActiveDirectory.DS_SITE_COST_INFO_head
    DS_SITE_COST_INFO._fields_ = [
        ("errorCode", UInt32),
        ("cost", UInt32),
    ]
    return DS_SITE_COST_INFO
def _define_DS_SCHEMA_GUID_MAPA_head():
    class DS_SCHEMA_GUID_MAPA(Structure):
        pass
    return DS_SCHEMA_GUID_MAPA
def _define_DS_SCHEMA_GUID_MAPA():
    DS_SCHEMA_GUID_MAPA = win32more.Networking.ActiveDirectory.DS_SCHEMA_GUID_MAPA_head
    DS_SCHEMA_GUID_MAPA._fields_ = [
        ("guid", Guid),
        ("guidType", UInt32),
        ("pName", win32more.Foundation.PSTR),
    ]
    return DS_SCHEMA_GUID_MAPA
def _define_DS_SCHEMA_GUID_MAPW_head():
    class DS_SCHEMA_GUID_MAPW(Structure):
        pass
    return DS_SCHEMA_GUID_MAPW
def _define_DS_SCHEMA_GUID_MAPW():
    DS_SCHEMA_GUID_MAPW = win32more.Networking.ActiveDirectory.DS_SCHEMA_GUID_MAPW_head
    DS_SCHEMA_GUID_MAPW._fields_ = [
        ("guid", Guid),
        ("guidType", UInt32),
        ("pName", win32more.Foundation.PWSTR),
    ]
    return DS_SCHEMA_GUID_MAPW
def _define_DS_DOMAIN_CONTROLLER_INFO_1A_head():
    class DS_DOMAIN_CONTROLLER_INFO_1A(Structure):
        pass
    return DS_DOMAIN_CONTROLLER_INFO_1A
def _define_DS_DOMAIN_CONTROLLER_INFO_1A():
    DS_DOMAIN_CONTROLLER_INFO_1A = win32more.Networking.ActiveDirectory.DS_DOMAIN_CONTROLLER_INFO_1A_head
    DS_DOMAIN_CONTROLLER_INFO_1A._fields_ = [
        ("NetbiosName", win32more.Foundation.PSTR),
        ("DnsHostName", win32more.Foundation.PSTR),
        ("SiteName", win32more.Foundation.PSTR),
        ("ComputerObjectName", win32more.Foundation.PSTR),
        ("ServerObjectName", win32more.Foundation.PSTR),
        ("fIsPdc", win32more.Foundation.BOOL),
        ("fDsEnabled", win32more.Foundation.BOOL),
    ]
    return DS_DOMAIN_CONTROLLER_INFO_1A
def _define_DS_DOMAIN_CONTROLLER_INFO_1W_head():
    class DS_DOMAIN_CONTROLLER_INFO_1W(Structure):
        pass
    return DS_DOMAIN_CONTROLLER_INFO_1W
def _define_DS_DOMAIN_CONTROLLER_INFO_1W():
    DS_DOMAIN_CONTROLLER_INFO_1W = win32more.Networking.ActiveDirectory.DS_DOMAIN_CONTROLLER_INFO_1W_head
    DS_DOMAIN_CONTROLLER_INFO_1W._fields_ = [
        ("NetbiosName", win32more.Foundation.PWSTR),
        ("DnsHostName", win32more.Foundation.PWSTR),
        ("SiteName", win32more.Foundation.PWSTR),
        ("ComputerObjectName", win32more.Foundation.PWSTR),
        ("ServerObjectName", win32more.Foundation.PWSTR),
        ("fIsPdc", win32more.Foundation.BOOL),
        ("fDsEnabled", win32more.Foundation.BOOL),
    ]
    return DS_DOMAIN_CONTROLLER_INFO_1W
def _define_DS_DOMAIN_CONTROLLER_INFO_2A_head():
    class DS_DOMAIN_CONTROLLER_INFO_2A(Structure):
        pass
    return DS_DOMAIN_CONTROLLER_INFO_2A
def _define_DS_DOMAIN_CONTROLLER_INFO_2A():
    DS_DOMAIN_CONTROLLER_INFO_2A = win32more.Networking.ActiveDirectory.DS_DOMAIN_CONTROLLER_INFO_2A_head
    DS_DOMAIN_CONTROLLER_INFO_2A._fields_ = [
        ("NetbiosName", win32more.Foundation.PSTR),
        ("DnsHostName", win32more.Foundation.PSTR),
        ("SiteName", win32more.Foundation.PSTR),
        ("SiteObjectName", win32more.Foundation.PSTR),
        ("ComputerObjectName", win32more.Foundation.PSTR),
        ("ServerObjectName", win32more.Foundation.PSTR),
        ("NtdsDsaObjectName", win32more.Foundation.PSTR),
        ("fIsPdc", win32more.Foundation.BOOL),
        ("fDsEnabled", win32more.Foundation.BOOL),
        ("fIsGc", win32more.Foundation.BOOL),
        ("SiteObjectGuid", Guid),
        ("ComputerObjectGuid", Guid),
        ("ServerObjectGuid", Guid),
        ("NtdsDsaObjectGuid", Guid),
    ]
    return DS_DOMAIN_CONTROLLER_INFO_2A
def _define_DS_DOMAIN_CONTROLLER_INFO_2W_head():
    class DS_DOMAIN_CONTROLLER_INFO_2W(Structure):
        pass
    return DS_DOMAIN_CONTROLLER_INFO_2W
def _define_DS_DOMAIN_CONTROLLER_INFO_2W():
    DS_DOMAIN_CONTROLLER_INFO_2W = win32more.Networking.ActiveDirectory.DS_DOMAIN_CONTROLLER_INFO_2W_head
    DS_DOMAIN_CONTROLLER_INFO_2W._fields_ = [
        ("NetbiosName", win32more.Foundation.PWSTR),
        ("DnsHostName", win32more.Foundation.PWSTR),
        ("SiteName", win32more.Foundation.PWSTR),
        ("SiteObjectName", win32more.Foundation.PWSTR),
        ("ComputerObjectName", win32more.Foundation.PWSTR),
        ("ServerObjectName", win32more.Foundation.PWSTR),
        ("NtdsDsaObjectName", win32more.Foundation.PWSTR),
        ("fIsPdc", win32more.Foundation.BOOL),
        ("fDsEnabled", win32more.Foundation.BOOL),
        ("fIsGc", win32more.Foundation.BOOL),
        ("SiteObjectGuid", Guid),
        ("ComputerObjectGuid", Guid),
        ("ServerObjectGuid", Guid),
        ("NtdsDsaObjectGuid", Guid),
    ]
    return DS_DOMAIN_CONTROLLER_INFO_2W
def _define_DS_DOMAIN_CONTROLLER_INFO_3A_head():
    class DS_DOMAIN_CONTROLLER_INFO_3A(Structure):
        pass
    return DS_DOMAIN_CONTROLLER_INFO_3A
def _define_DS_DOMAIN_CONTROLLER_INFO_3A():
    DS_DOMAIN_CONTROLLER_INFO_3A = win32more.Networking.ActiveDirectory.DS_DOMAIN_CONTROLLER_INFO_3A_head
    DS_DOMAIN_CONTROLLER_INFO_3A._fields_ = [
        ("NetbiosName", win32more.Foundation.PSTR),
        ("DnsHostName", win32more.Foundation.PSTR),
        ("SiteName", win32more.Foundation.PSTR),
        ("SiteObjectName", win32more.Foundation.PSTR),
        ("ComputerObjectName", win32more.Foundation.PSTR),
        ("ServerObjectName", win32more.Foundation.PSTR),
        ("NtdsDsaObjectName", win32more.Foundation.PSTR),
        ("fIsPdc", win32more.Foundation.BOOL),
        ("fDsEnabled", win32more.Foundation.BOOL),
        ("fIsGc", win32more.Foundation.BOOL),
        ("fIsRodc", win32more.Foundation.BOOL),
        ("SiteObjectGuid", Guid),
        ("ComputerObjectGuid", Guid),
        ("ServerObjectGuid", Guid),
        ("NtdsDsaObjectGuid", Guid),
    ]
    return DS_DOMAIN_CONTROLLER_INFO_3A
def _define_DS_DOMAIN_CONTROLLER_INFO_3W_head():
    class DS_DOMAIN_CONTROLLER_INFO_3W(Structure):
        pass
    return DS_DOMAIN_CONTROLLER_INFO_3W
def _define_DS_DOMAIN_CONTROLLER_INFO_3W():
    DS_DOMAIN_CONTROLLER_INFO_3W = win32more.Networking.ActiveDirectory.DS_DOMAIN_CONTROLLER_INFO_3W_head
    DS_DOMAIN_CONTROLLER_INFO_3W._fields_ = [
        ("NetbiosName", win32more.Foundation.PWSTR),
        ("DnsHostName", win32more.Foundation.PWSTR),
        ("SiteName", win32more.Foundation.PWSTR),
        ("SiteObjectName", win32more.Foundation.PWSTR),
        ("ComputerObjectName", win32more.Foundation.PWSTR),
        ("ServerObjectName", win32more.Foundation.PWSTR),
        ("NtdsDsaObjectName", win32more.Foundation.PWSTR),
        ("fIsPdc", win32more.Foundation.BOOL),
        ("fDsEnabled", win32more.Foundation.BOOL),
        ("fIsGc", win32more.Foundation.BOOL),
        ("fIsRodc", win32more.Foundation.BOOL),
        ("SiteObjectGuid", Guid),
        ("ComputerObjectGuid", Guid),
        ("ServerObjectGuid", Guid),
        ("NtdsDsaObjectGuid", Guid),
    ]
    return DS_DOMAIN_CONTROLLER_INFO_3W
DS_KCC_TASKID = Int32
DS_KCC_TASKID_UPDATE_TOPOLOGY = 0
DS_REPL_INFO_TYPE = Int32
DS_REPL_INFO_NEIGHBORS = 0
DS_REPL_INFO_CURSORS_FOR_NC = 1
DS_REPL_INFO_METADATA_FOR_OBJ = 2
DS_REPL_INFO_KCC_DSA_CONNECT_FAILURES = 3
DS_REPL_INFO_KCC_DSA_LINK_FAILURES = 4
DS_REPL_INFO_PENDING_OPS = 5
DS_REPL_INFO_METADATA_FOR_ATTR_VALUE = 6
DS_REPL_INFO_CURSORS_2_FOR_NC = 7
DS_REPL_INFO_CURSORS_3_FOR_NC = 8
DS_REPL_INFO_METADATA_2_FOR_OBJ = 9
DS_REPL_INFO_METADATA_2_FOR_ATTR_VALUE = 10
DS_REPL_INFO_METADATA_EXT_FOR_ATTR_VALUE = 11
DS_REPL_INFO_TYPE_MAX = 12
def _define_DS_REPL_NEIGHBORW_head():
    class DS_REPL_NEIGHBORW(Structure):
        pass
    return DS_REPL_NEIGHBORW
def _define_DS_REPL_NEIGHBORW():
    DS_REPL_NEIGHBORW = win32more.Networking.ActiveDirectory.DS_REPL_NEIGHBORW_head
    DS_REPL_NEIGHBORW._fields_ = [
        ("pszNamingContext", win32more.Foundation.PWSTR),
        ("pszSourceDsaDN", win32more.Foundation.PWSTR),
        ("pszSourceDsaAddress", win32more.Foundation.PWSTR),
        ("pszAsyncIntersiteTransportDN", win32more.Foundation.PWSTR),
        ("dwReplicaFlags", UInt32),
        ("dwReserved", UInt32),
        ("uuidNamingContextObjGuid", Guid),
        ("uuidSourceDsaObjGuid", Guid),
        ("uuidSourceDsaInvocationID", Guid),
        ("uuidAsyncIntersiteTransportObjGuid", Guid),
        ("usnLastObjChangeSynced", Int64),
        ("usnAttributeFilter", Int64),
        ("ftimeLastSyncSuccess", win32more.Foundation.FILETIME),
        ("ftimeLastSyncAttempt", win32more.Foundation.FILETIME),
        ("dwLastSyncResult", UInt32),
        ("cNumConsecutiveSyncFailures", UInt32),
    ]
    return DS_REPL_NEIGHBORW
def _define_DS_REPL_NEIGHBORW_BLOB_head():
    class DS_REPL_NEIGHBORW_BLOB(Structure):
        pass
    return DS_REPL_NEIGHBORW_BLOB
def _define_DS_REPL_NEIGHBORW_BLOB():
    DS_REPL_NEIGHBORW_BLOB = win32more.Networking.ActiveDirectory.DS_REPL_NEIGHBORW_BLOB_head
    DS_REPL_NEIGHBORW_BLOB._fields_ = [
        ("oszNamingContext", UInt32),
        ("oszSourceDsaDN", UInt32),
        ("oszSourceDsaAddress", UInt32),
        ("oszAsyncIntersiteTransportDN", UInt32),
        ("dwReplicaFlags", UInt32),
        ("dwReserved", UInt32),
        ("uuidNamingContextObjGuid", Guid),
        ("uuidSourceDsaObjGuid", Guid),
        ("uuidSourceDsaInvocationID", Guid),
        ("uuidAsyncIntersiteTransportObjGuid", Guid),
        ("usnLastObjChangeSynced", Int64),
        ("usnAttributeFilter", Int64),
        ("ftimeLastSyncSuccess", win32more.Foundation.FILETIME),
        ("ftimeLastSyncAttempt", win32more.Foundation.FILETIME),
        ("dwLastSyncResult", UInt32),
        ("cNumConsecutiveSyncFailures", UInt32),
    ]
    return DS_REPL_NEIGHBORW_BLOB
def _define_DS_REPL_NEIGHBORSW_head():
    class DS_REPL_NEIGHBORSW(Structure):
        pass
    return DS_REPL_NEIGHBORSW
def _define_DS_REPL_NEIGHBORSW():
    DS_REPL_NEIGHBORSW = win32more.Networking.ActiveDirectory.DS_REPL_NEIGHBORSW_head
    DS_REPL_NEIGHBORSW._fields_ = [
        ("cNumNeighbors", UInt32),
        ("dwReserved", UInt32),
        ("rgNeighbor", win32more.Networking.ActiveDirectory.DS_REPL_NEIGHBORW * 0),
    ]
    return DS_REPL_NEIGHBORSW
def _define_DS_REPL_CURSOR_head():
    class DS_REPL_CURSOR(Structure):
        pass
    return DS_REPL_CURSOR
def _define_DS_REPL_CURSOR():
    DS_REPL_CURSOR = win32more.Networking.ActiveDirectory.DS_REPL_CURSOR_head
    DS_REPL_CURSOR._fields_ = [
        ("uuidSourceDsaInvocationID", Guid),
        ("usnAttributeFilter", Int64),
    ]
    return DS_REPL_CURSOR
def _define_DS_REPL_CURSOR_2_head():
    class DS_REPL_CURSOR_2(Structure):
        pass
    return DS_REPL_CURSOR_2
def _define_DS_REPL_CURSOR_2():
    DS_REPL_CURSOR_2 = win32more.Networking.ActiveDirectory.DS_REPL_CURSOR_2_head
    DS_REPL_CURSOR_2._fields_ = [
        ("uuidSourceDsaInvocationID", Guid),
        ("usnAttributeFilter", Int64),
        ("ftimeLastSyncSuccess", win32more.Foundation.FILETIME),
    ]
    return DS_REPL_CURSOR_2
def _define_DS_REPL_CURSOR_3W_head():
    class DS_REPL_CURSOR_3W(Structure):
        pass
    return DS_REPL_CURSOR_3W
def _define_DS_REPL_CURSOR_3W():
    DS_REPL_CURSOR_3W = win32more.Networking.ActiveDirectory.DS_REPL_CURSOR_3W_head
    DS_REPL_CURSOR_3W._fields_ = [
        ("uuidSourceDsaInvocationID", Guid),
        ("usnAttributeFilter", Int64),
        ("ftimeLastSyncSuccess", win32more.Foundation.FILETIME),
        ("pszSourceDsaDN", win32more.Foundation.PWSTR),
    ]
    return DS_REPL_CURSOR_3W
def _define_DS_REPL_CURSOR_BLOB_head():
    class DS_REPL_CURSOR_BLOB(Structure):
        pass
    return DS_REPL_CURSOR_BLOB
def _define_DS_REPL_CURSOR_BLOB():
    DS_REPL_CURSOR_BLOB = win32more.Networking.ActiveDirectory.DS_REPL_CURSOR_BLOB_head
    DS_REPL_CURSOR_BLOB._fields_ = [
        ("uuidSourceDsaInvocationID", Guid),
        ("usnAttributeFilter", Int64),
        ("ftimeLastSyncSuccess", win32more.Foundation.FILETIME),
        ("oszSourceDsaDN", UInt32),
    ]
    return DS_REPL_CURSOR_BLOB
def _define_DS_REPL_CURSORS_head():
    class DS_REPL_CURSORS(Structure):
        pass
    return DS_REPL_CURSORS
def _define_DS_REPL_CURSORS():
    DS_REPL_CURSORS = win32more.Networking.ActiveDirectory.DS_REPL_CURSORS_head
    DS_REPL_CURSORS._fields_ = [
        ("cNumCursors", UInt32),
        ("dwReserved", UInt32),
        ("rgCursor", win32more.Networking.ActiveDirectory.DS_REPL_CURSOR * 0),
    ]
    return DS_REPL_CURSORS
def _define_DS_REPL_CURSORS_2_head():
    class DS_REPL_CURSORS_2(Structure):
        pass
    return DS_REPL_CURSORS_2
def _define_DS_REPL_CURSORS_2():
    DS_REPL_CURSORS_2 = win32more.Networking.ActiveDirectory.DS_REPL_CURSORS_2_head
    DS_REPL_CURSORS_2._fields_ = [
        ("cNumCursors", UInt32),
        ("dwEnumerationContext", UInt32),
        ("rgCursor", win32more.Networking.ActiveDirectory.DS_REPL_CURSOR_2 * 0),
    ]
    return DS_REPL_CURSORS_2
def _define_DS_REPL_CURSORS_3W_head():
    class DS_REPL_CURSORS_3W(Structure):
        pass
    return DS_REPL_CURSORS_3W
def _define_DS_REPL_CURSORS_3W():
    DS_REPL_CURSORS_3W = win32more.Networking.ActiveDirectory.DS_REPL_CURSORS_3W_head
    DS_REPL_CURSORS_3W._fields_ = [
        ("cNumCursors", UInt32),
        ("dwEnumerationContext", UInt32),
        ("rgCursor", win32more.Networking.ActiveDirectory.DS_REPL_CURSOR_3W * 0),
    ]
    return DS_REPL_CURSORS_3W
def _define_DS_REPL_ATTR_META_DATA_head():
    class DS_REPL_ATTR_META_DATA(Structure):
        pass
    return DS_REPL_ATTR_META_DATA
def _define_DS_REPL_ATTR_META_DATA():
    DS_REPL_ATTR_META_DATA = win32more.Networking.ActiveDirectory.DS_REPL_ATTR_META_DATA_head
    DS_REPL_ATTR_META_DATA._fields_ = [
        ("pszAttributeName", win32more.Foundation.PWSTR),
        ("dwVersion", UInt32),
        ("ftimeLastOriginatingChange", win32more.Foundation.FILETIME),
        ("uuidLastOriginatingDsaInvocationID", Guid),
        ("usnOriginatingChange", Int64),
        ("usnLocalChange", Int64),
    ]
    return DS_REPL_ATTR_META_DATA
def _define_DS_REPL_ATTR_META_DATA_2_head():
    class DS_REPL_ATTR_META_DATA_2(Structure):
        pass
    return DS_REPL_ATTR_META_DATA_2
def _define_DS_REPL_ATTR_META_DATA_2():
    DS_REPL_ATTR_META_DATA_2 = win32more.Networking.ActiveDirectory.DS_REPL_ATTR_META_DATA_2_head
    DS_REPL_ATTR_META_DATA_2._fields_ = [
        ("pszAttributeName", win32more.Foundation.PWSTR),
        ("dwVersion", UInt32),
        ("ftimeLastOriginatingChange", win32more.Foundation.FILETIME),
        ("uuidLastOriginatingDsaInvocationID", Guid),
        ("usnOriginatingChange", Int64),
        ("usnLocalChange", Int64),
        ("pszLastOriginatingDsaDN", win32more.Foundation.PWSTR),
    ]
    return DS_REPL_ATTR_META_DATA_2
def _define_DS_REPL_ATTR_META_DATA_BLOB_head():
    class DS_REPL_ATTR_META_DATA_BLOB(Structure):
        pass
    return DS_REPL_ATTR_META_DATA_BLOB
def _define_DS_REPL_ATTR_META_DATA_BLOB():
    DS_REPL_ATTR_META_DATA_BLOB = win32more.Networking.ActiveDirectory.DS_REPL_ATTR_META_DATA_BLOB_head
    DS_REPL_ATTR_META_DATA_BLOB._fields_ = [
        ("oszAttributeName", UInt32),
        ("dwVersion", UInt32),
        ("ftimeLastOriginatingChange", win32more.Foundation.FILETIME),
        ("uuidLastOriginatingDsaInvocationID", Guid),
        ("usnOriginatingChange", Int64),
        ("usnLocalChange", Int64),
        ("oszLastOriginatingDsaDN", UInt32),
    ]
    return DS_REPL_ATTR_META_DATA_BLOB
def _define_DS_REPL_OBJ_META_DATA_head():
    class DS_REPL_OBJ_META_DATA(Structure):
        pass
    return DS_REPL_OBJ_META_DATA
def _define_DS_REPL_OBJ_META_DATA():
    DS_REPL_OBJ_META_DATA = win32more.Networking.ActiveDirectory.DS_REPL_OBJ_META_DATA_head
    DS_REPL_OBJ_META_DATA._fields_ = [
        ("cNumEntries", UInt32),
        ("dwReserved", UInt32),
        ("rgMetaData", win32more.Networking.ActiveDirectory.DS_REPL_ATTR_META_DATA * 0),
    ]
    return DS_REPL_OBJ_META_DATA
def _define_DS_REPL_OBJ_META_DATA_2_head():
    class DS_REPL_OBJ_META_DATA_2(Structure):
        pass
    return DS_REPL_OBJ_META_DATA_2
def _define_DS_REPL_OBJ_META_DATA_2():
    DS_REPL_OBJ_META_DATA_2 = win32more.Networking.ActiveDirectory.DS_REPL_OBJ_META_DATA_2_head
    DS_REPL_OBJ_META_DATA_2._fields_ = [
        ("cNumEntries", UInt32),
        ("dwReserved", UInt32),
        ("rgMetaData", win32more.Networking.ActiveDirectory.DS_REPL_ATTR_META_DATA_2 * 0),
    ]
    return DS_REPL_OBJ_META_DATA_2
def _define_DS_REPL_KCC_DSA_FAILUREW_head():
    class DS_REPL_KCC_DSA_FAILUREW(Structure):
        pass
    return DS_REPL_KCC_DSA_FAILUREW
def _define_DS_REPL_KCC_DSA_FAILUREW():
    DS_REPL_KCC_DSA_FAILUREW = win32more.Networking.ActiveDirectory.DS_REPL_KCC_DSA_FAILUREW_head
    DS_REPL_KCC_DSA_FAILUREW._fields_ = [
        ("pszDsaDN", win32more.Foundation.PWSTR),
        ("uuidDsaObjGuid", Guid),
        ("ftimeFirstFailure", win32more.Foundation.FILETIME),
        ("cNumFailures", UInt32),
        ("dwLastResult", UInt32),
    ]
    return DS_REPL_KCC_DSA_FAILUREW
def _define_DS_REPL_KCC_DSA_FAILUREW_BLOB_head():
    class DS_REPL_KCC_DSA_FAILUREW_BLOB(Structure):
        pass
    return DS_REPL_KCC_DSA_FAILUREW_BLOB
def _define_DS_REPL_KCC_DSA_FAILUREW_BLOB():
    DS_REPL_KCC_DSA_FAILUREW_BLOB = win32more.Networking.ActiveDirectory.DS_REPL_KCC_DSA_FAILUREW_BLOB_head
    DS_REPL_KCC_DSA_FAILUREW_BLOB._fields_ = [
        ("oszDsaDN", UInt32),
        ("uuidDsaObjGuid", Guid),
        ("ftimeFirstFailure", win32more.Foundation.FILETIME),
        ("cNumFailures", UInt32),
        ("dwLastResult", UInt32),
    ]
    return DS_REPL_KCC_DSA_FAILUREW_BLOB
def _define_DS_REPL_KCC_DSA_FAILURESW_head():
    class DS_REPL_KCC_DSA_FAILURESW(Structure):
        pass
    return DS_REPL_KCC_DSA_FAILURESW
def _define_DS_REPL_KCC_DSA_FAILURESW():
    DS_REPL_KCC_DSA_FAILURESW = win32more.Networking.ActiveDirectory.DS_REPL_KCC_DSA_FAILURESW_head
    DS_REPL_KCC_DSA_FAILURESW._fields_ = [
        ("cNumEntries", UInt32),
        ("dwReserved", UInt32),
        ("rgDsaFailure", win32more.Networking.ActiveDirectory.DS_REPL_KCC_DSA_FAILUREW * 0),
    ]
    return DS_REPL_KCC_DSA_FAILURESW
DS_REPL_OP_TYPE = Int32
DS_REPL_OP_TYPE_SYNC = 0
DS_REPL_OP_TYPE_ADD = 1
DS_REPL_OP_TYPE_DELETE = 2
DS_REPL_OP_TYPE_MODIFY = 3
DS_REPL_OP_TYPE_UPDATE_REFS = 4
def _define_DS_REPL_OPW_head():
    class DS_REPL_OPW(Structure):
        pass
    return DS_REPL_OPW
def _define_DS_REPL_OPW():
    DS_REPL_OPW = win32more.Networking.ActiveDirectory.DS_REPL_OPW_head
    DS_REPL_OPW._fields_ = [
        ("ftimeEnqueued", win32more.Foundation.FILETIME),
        ("ulSerialNumber", UInt32),
        ("ulPriority", UInt32),
        ("OpType", win32more.Networking.ActiveDirectory.DS_REPL_OP_TYPE),
        ("ulOptions", UInt32),
        ("pszNamingContext", win32more.Foundation.PWSTR),
        ("pszDsaDN", win32more.Foundation.PWSTR),
        ("pszDsaAddress", win32more.Foundation.PWSTR),
        ("uuidNamingContextObjGuid", Guid),
        ("uuidDsaObjGuid", Guid),
    ]
    return DS_REPL_OPW
def _define_DS_REPL_OPW_BLOB_head():
    class DS_REPL_OPW_BLOB(Structure):
        pass
    return DS_REPL_OPW_BLOB
def _define_DS_REPL_OPW_BLOB():
    DS_REPL_OPW_BLOB = win32more.Networking.ActiveDirectory.DS_REPL_OPW_BLOB_head
    DS_REPL_OPW_BLOB._fields_ = [
        ("ftimeEnqueued", win32more.Foundation.FILETIME),
        ("ulSerialNumber", UInt32),
        ("ulPriority", UInt32),
        ("OpType", win32more.Networking.ActiveDirectory.DS_REPL_OP_TYPE),
        ("ulOptions", UInt32),
        ("oszNamingContext", UInt32),
        ("oszDsaDN", UInt32),
        ("oszDsaAddress", UInt32),
        ("uuidNamingContextObjGuid", Guid),
        ("uuidDsaObjGuid", Guid),
    ]
    return DS_REPL_OPW_BLOB
def _define_DS_REPL_PENDING_OPSW_head():
    class DS_REPL_PENDING_OPSW(Structure):
        pass
    return DS_REPL_PENDING_OPSW
def _define_DS_REPL_PENDING_OPSW():
    DS_REPL_PENDING_OPSW = win32more.Networking.ActiveDirectory.DS_REPL_PENDING_OPSW_head
    DS_REPL_PENDING_OPSW._fields_ = [
        ("ftimeCurrentOpStarted", win32more.Foundation.FILETIME),
        ("cNumPendingOps", UInt32),
        ("rgPendingOp", win32more.Networking.ActiveDirectory.DS_REPL_OPW * 0),
    ]
    return DS_REPL_PENDING_OPSW
def _define_DS_REPL_VALUE_META_DATA_head():
    class DS_REPL_VALUE_META_DATA(Structure):
        pass
    return DS_REPL_VALUE_META_DATA
def _define_DS_REPL_VALUE_META_DATA():
    DS_REPL_VALUE_META_DATA = win32more.Networking.ActiveDirectory.DS_REPL_VALUE_META_DATA_head
    DS_REPL_VALUE_META_DATA._fields_ = [
        ("pszAttributeName", win32more.Foundation.PWSTR),
        ("pszObjectDn", win32more.Foundation.PWSTR),
        ("cbData", UInt32),
        ("pbData", c_char_p_no),
        ("ftimeDeleted", win32more.Foundation.FILETIME),
        ("ftimeCreated", win32more.Foundation.FILETIME),
        ("dwVersion", UInt32),
        ("ftimeLastOriginatingChange", win32more.Foundation.FILETIME),
        ("uuidLastOriginatingDsaInvocationID", Guid),
        ("usnOriginatingChange", Int64),
        ("usnLocalChange", Int64),
    ]
    return DS_REPL_VALUE_META_DATA
def _define_DS_REPL_VALUE_META_DATA_2_head():
    class DS_REPL_VALUE_META_DATA_2(Structure):
        pass
    return DS_REPL_VALUE_META_DATA_2
def _define_DS_REPL_VALUE_META_DATA_2():
    DS_REPL_VALUE_META_DATA_2 = win32more.Networking.ActiveDirectory.DS_REPL_VALUE_META_DATA_2_head
    DS_REPL_VALUE_META_DATA_2._fields_ = [
        ("pszAttributeName", win32more.Foundation.PWSTR),
        ("pszObjectDn", win32more.Foundation.PWSTR),
        ("cbData", UInt32),
        ("pbData", c_char_p_no),
        ("ftimeDeleted", win32more.Foundation.FILETIME),
        ("ftimeCreated", win32more.Foundation.FILETIME),
        ("dwVersion", UInt32),
        ("ftimeLastOriginatingChange", win32more.Foundation.FILETIME),
        ("uuidLastOriginatingDsaInvocationID", Guid),
        ("usnOriginatingChange", Int64),
        ("usnLocalChange", Int64),
        ("pszLastOriginatingDsaDN", win32more.Foundation.PWSTR),
    ]
    return DS_REPL_VALUE_META_DATA_2
def _define_DS_REPL_VALUE_META_DATA_EXT_head():
    class DS_REPL_VALUE_META_DATA_EXT(Structure):
        pass
    return DS_REPL_VALUE_META_DATA_EXT
def _define_DS_REPL_VALUE_META_DATA_EXT():
    DS_REPL_VALUE_META_DATA_EXT = win32more.Networking.ActiveDirectory.DS_REPL_VALUE_META_DATA_EXT_head
    DS_REPL_VALUE_META_DATA_EXT._fields_ = [
        ("pszAttributeName", win32more.Foundation.PWSTR),
        ("pszObjectDn", win32more.Foundation.PWSTR),
        ("cbData", UInt32),
        ("pbData", c_char_p_no),
        ("ftimeDeleted", win32more.Foundation.FILETIME),
        ("ftimeCreated", win32more.Foundation.FILETIME),
        ("dwVersion", UInt32),
        ("ftimeLastOriginatingChange", win32more.Foundation.FILETIME),
        ("uuidLastOriginatingDsaInvocationID", Guid),
        ("usnOriginatingChange", Int64),
        ("usnLocalChange", Int64),
        ("pszLastOriginatingDsaDN", win32more.Foundation.PWSTR),
        ("dwUserIdentifier", UInt32),
        ("dwPriorLinkState", UInt32),
        ("dwCurrentLinkState", UInt32),
    ]
    return DS_REPL_VALUE_META_DATA_EXT
def _define_DS_REPL_VALUE_META_DATA_BLOB_head():
    class DS_REPL_VALUE_META_DATA_BLOB(Structure):
        pass
    return DS_REPL_VALUE_META_DATA_BLOB
def _define_DS_REPL_VALUE_META_DATA_BLOB():
    DS_REPL_VALUE_META_DATA_BLOB = win32more.Networking.ActiveDirectory.DS_REPL_VALUE_META_DATA_BLOB_head
    DS_REPL_VALUE_META_DATA_BLOB._fields_ = [
        ("oszAttributeName", UInt32),
        ("oszObjectDn", UInt32),
        ("cbData", UInt32),
        ("obData", UInt32),
        ("ftimeDeleted", win32more.Foundation.FILETIME),
        ("ftimeCreated", win32more.Foundation.FILETIME),
        ("dwVersion", UInt32),
        ("ftimeLastOriginatingChange", win32more.Foundation.FILETIME),
        ("uuidLastOriginatingDsaInvocationID", Guid),
        ("usnOriginatingChange", Int64),
        ("usnLocalChange", Int64),
        ("oszLastOriginatingDsaDN", UInt32),
    ]
    return DS_REPL_VALUE_META_DATA_BLOB
def _define_DS_REPL_VALUE_META_DATA_BLOB_EXT_head():
    class DS_REPL_VALUE_META_DATA_BLOB_EXT(Structure):
        pass
    return DS_REPL_VALUE_META_DATA_BLOB_EXT
def _define_DS_REPL_VALUE_META_DATA_BLOB_EXT():
    DS_REPL_VALUE_META_DATA_BLOB_EXT = win32more.Networking.ActiveDirectory.DS_REPL_VALUE_META_DATA_BLOB_EXT_head
    DS_REPL_VALUE_META_DATA_BLOB_EXT._fields_ = [
        ("oszAttributeName", UInt32),
        ("oszObjectDn", UInt32),
        ("cbData", UInt32),
        ("obData", UInt32),
        ("ftimeDeleted", win32more.Foundation.FILETIME),
        ("ftimeCreated", win32more.Foundation.FILETIME),
        ("dwVersion", UInt32),
        ("ftimeLastOriginatingChange", win32more.Foundation.FILETIME),
        ("uuidLastOriginatingDsaInvocationID", Guid),
        ("usnOriginatingChange", Int64),
        ("usnLocalChange", Int64),
        ("oszLastOriginatingDsaDN", UInt32),
        ("dwUserIdentifier", UInt32),
        ("dwPriorLinkState", UInt32),
        ("dwCurrentLinkState", UInt32),
    ]
    return DS_REPL_VALUE_META_DATA_BLOB_EXT
def _define_DS_REPL_ATTR_VALUE_META_DATA_head():
    class DS_REPL_ATTR_VALUE_META_DATA(Structure):
        pass
    return DS_REPL_ATTR_VALUE_META_DATA
def _define_DS_REPL_ATTR_VALUE_META_DATA():
    DS_REPL_ATTR_VALUE_META_DATA = win32more.Networking.ActiveDirectory.DS_REPL_ATTR_VALUE_META_DATA_head
    DS_REPL_ATTR_VALUE_META_DATA._fields_ = [
        ("cNumEntries", UInt32),
        ("dwEnumerationContext", UInt32),
        ("rgMetaData", win32more.Networking.ActiveDirectory.DS_REPL_VALUE_META_DATA * 0),
    ]
    return DS_REPL_ATTR_VALUE_META_DATA
def _define_DS_REPL_ATTR_VALUE_META_DATA_2_head():
    class DS_REPL_ATTR_VALUE_META_DATA_2(Structure):
        pass
    return DS_REPL_ATTR_VALUE_META_DATA_2
def _define_DS_REPL_ATTR_VALUE_META_DATA_2():
    DS_REPL_ATTR_VALUE_META_DATA_2 = win32more.Networking.ActiveDirectory.DS_REPL_ATTR_VALUE_META_DATA_2_head
    DS_REPL_ATTR_VALUE_META_DATA_2._fields_ = [
        ("cNumEntries", UInt32),
        ("dwEnumerationContext", UInt32),
        ("rgMetaData", win32more.Networking.ActiveDirectory.DS_REPL_VALUE_META_DATA_2 * 0),
    ]
    return DS_REPL_ATTR_VALUE_META_DATA_2
def _define_DS_REPL_ATTR_VALUE_META_DATA_EXT_head():
    class DS_REPL_ATTR_VALUE_META_DATA_EXT(Structure):
        pass
    return DS_REPL_ATTR_VALUE_META_DATA_EXT
def _define_DS_REPL_ATTR_VALUE_META_DATA_EXT():
    DS_REPL_ATTR_VALUE_META_DATA_EXT = win32more.Networking.ActiveDirectory.DS_REPL_ATTR_VALUE_META_DATA_EXT_head
    DS_REPL_ATTR_VALUE_META_DATA_EXT._fields_ = [
        ("cNumEntries", UInt32),
        ("dwEnumerationContext", UInt32),
        ("rgMetaData", win32more.Networking.ActiveDirectory.DS_REPL_VALUE_META_DATA_EXT * 0),
    ]
    return DS_REPL_ATTR_VALUE_META_DATA_EXT
def _define_DS_REPL_QUEUE_STATISTICSW_head():
    class DS_REPL_QUEUE_STATISTICSW(Structure):
        pass
    return DS_REPL_QUEUE_STATISTICSW
def _define_DS_REPL_QUEUE_STATISTICSW():
    DS_REPL_QUEUE_STATISTICSW = win32more.Networking.ActiveDirectory.DS_REPL_QUEUE_STATISTICSW_head
    DS_REPL_QUEUE_STATISTICSW._fields_ = [
        ("ftimeCurrentOpStarted", win32more.Foundation.FILETIME),
        ("cNumPendingOps", UInt32),
        ("ftimeOldestSync", win32more.Foundation.FILETIME),
        ("ftimeOldestAdd", win32more.Foundation.FILETIME),
        ("ftimeOldestMod", win32more.Foundation.FILETIME),
        ("ftimeOldestDel", win32more.Foundation.FILETIME),
        ("ftimeOldestUpdRefs", win32more.Foundation.FILETIME),
    ]
    return DS_REPL_QUEUE_STATISTICSW
DSROLE_MACHINE_ROLE = Int32
DsRole_RoleStandaloneWorkstation = 0
DsRole_RoleMemberWorkstation = 1
DsRole_RoleStandaloneServer = 2
DsRole_RoleMemberServer = 3
DsRole_RoleBackupDomainController = 4
DsRole_RolePrimaryDomainController = 5
DSROLE_SERVER_STATE = Int32
DSROLE_SERVER_STATE_DsRoleServerUnknown = 0
DSROLE_SERVER_STATE_DsRoleServerPrimary = 1
DSROLE_SERVER_STATE_DsRoleServerBackup = 2
DSROLE_PRIMARY_DOMAIN_INFO_LEVEL = Int32
DSROLE_PRIMARY_DOMAIN_INFO_LEVEL_DsRolePrimaryDomainInfoBasic = 1
DSROLE_PRIMARY_DOMAIN_INFO_LEVEL_DsRoleUpgradeStatus = 2
DSROLE_PRIMARY_DOMAIN_INFO_LEVEL_DsRoleOperationState = 3
def _define_DSROLE_PRIMARY_DOMAIN_INFO_BASIC_head():
    class DSROLE_PRIMARY_DOMAIN_INFO_BASIC(Structure):
        pass
    return DSROLE_PRIMARY_DOMAIN_INFO_BASIC
def _define_DSROLE_PRIMARY_DOMAIN_INFO_BASIC():
    DSROLE_PRIMARY_DOMAIN_INFO_BASIC = win32more.Networking.ActiveDirectory.DSROLE_PRIMARY_DOMAIN_INFO_BASIC_head
    DSROLE_PRIMARY_DOMAIN_INFO_BASIC._fields_ = [
        ("MachineRole", win32more.Networking.ActiveDirectory.DSROLE_MACHINE_ROLE),
        ("Flags", UInt32),
        ("DomainNameFlat", win32more.Foundation.PWSTR),
        ("DomainNameDns", win32more.Foundation.PWSTR),
        ("DomainForestName", win32more.Foundation.PWSTR),
        ("DomainGuid", Guid),
    ]
    return DSROLE_PRIMARY_DOMAIN_INFO_BASIC
def _define_DSROLE_UPGRADE_STATUS_INFO_head():
    class DSROLE_UPGRADE_STATUS_INFO(Structure):
        pass
    return DSROLE_UPGRADE_STATUS_INFO
def _define_DSROLE_UPGRADE_STATUS_INFO():
    DSROLE_UPGRADE_STATUS_INFO = win32more.Networking.ActiveDirectory.DSROLE_UPGRADE_STATUS_INFO_head
    DSROLE_UPGRADE_STATUS_INFO._fields_ = [
        ("OperationState", UInt32),
        ("PreviousServerState", win32more.Networking.ActiveDirectory.DSROLE_SERVER_STATE),
    ]
    return DSROLE_UPGRADE_STATUS_INFO
DSROLE_OPERATION_STATE = Int32
DSROLE_OPERATION_STATE_DsRoleOperationIdle = 0
DSROLE_OPERATION_STATE_DsRoleOperationActive = 1
DSROLE_OPERATION_STATE_DsRoleOperationNeedReboot = 2
def _define_DSROLE_OPERATION_STATE_INFO_head():
    class DSROLE_OPERATION_STATE_INFO(Structure):
        pass
    return DSROLE_OPERATION_STATE_INFO
def _define_DSROLE_OPERATION_STATE_INFO():
    DSROLE_OPERATION_STATE_INFO = win32more.Networking.ActiveDirectory.DSROLE_OPERATION_STATE_INFO_head
    DSROLE_OPERATION_STATE_INFO._fields_ = [
        ("OperationState", win32more.Networking.ActiveDirectory.DSROLE_OPERATION_STATE),
    ]
    return DSROLE_OPERATION_STATE_INFO
def _define_DOMAIN_CONTROLLER_INFOA_head():
    class DOMAIN_CONTROLLER_INFOA(Structure):
        pass
    return DOMAIN_CONTROLLER_INFOA
def _define_DOMAIN_CONTROLLER_INFOA():
    DOMAIN_CONTROLLER_INFOA = win32more.Networking.ActiveDirectory.DOMAIN_CONTROLLER_INFOA_head
    DOMAIN_CONTROLLER_INFOA._fields_ = [
        ("DomainControllerName", win32more.Foundation.PSTR),
        ("DomainControllerAddress", win32more.Foundation.PSTR),
        ("DomainControllerAddressType", UInt32),
        ("DomainGuid", Guid),
        ("DomainName", win32more.Foundation.PSTR),
        ("DnsForestName", win32more.Foundation.PSTR),
        ("Flags", UInt32),
        ("DcSiteName", win32more.Foundation.PSTR),
        ("ClientSiteName", win32more.Foundation.PSTR),
    ]
    return DOMAIN_CONTROLLER_INFOA
def _define_DOMAIN_CONTROLLER_INFOW_head():
    class DOMAIN_CONTROLLER_INFOW(Structure):
        pass
    return DOMAIN_CONTROLLER_INFOW
def _define_DOMAIN_CONTROLLER_INFOW():
    DOMAIN_CONTROLLER_INFOW = win32more.Networking.ActiveDirectory.DOMAIN_CONTROLLER_INFOW_head
    DOMAIN_CONTROLLER_INFOW._fields_ = [
        ("DomainControllerName", win32more.Foundation.PWSTR),
        ("DomainControllerAddress", win32more.Foundation.PWSTR),
        ("DomainControllerAddressType", UInt32),
        ("DomainGuid", Guid),
        ("DomainName", win32more.Foundation.PWSTR),
        ("DnsForestName", win32more.Foundation.PWSTR),
        ("Flags", UInt32),
        ("DcSiteName", win32more.Foundation.PWSTR),
        ("ClientSiteName", win32more.Foundation.PWSTR),
    ]
    return DOMAIN_CONTROLLER_INFOW
def _define_DS_DOMAIN_TRUSTSW_head():
    class DS_DOMAIN_TRUSTSW(Structure):
        pass
    return DS_DOMAIN_TRUSTSW
def _define_DS_DOMAIN_TRUSTSW():
    DS_DOMAIN_TRUSTSW = win32more.Networking.ActiveDirectory.DS_DOMAIN_TRUSTSW_head
    DS_DOMAIN_TRUSTSW._fields_ = [
        ("NetbiosDomainName", win32more.Foundation.PWSTR),
        ("DnsDomainName", win32more.Foundation.PWSTR),
        ("Flags", UInt32),
        ("ParentIndex", UInt32),
        ("TrustType", UInt32),
        ("TrustAttributes", UInt32),
        ("DomainSid", win32more.Foundation.PSID),
        ("DomainGuid", Guid),
    ]
    return DS_DOMAIN_TRUSTSW
def _define_DS_DOMAIN_TRUSTSA_head():
    class DS_DOMAIN_TRUSTSA(Structure):
        pass
    return DS_DOMAIN_TRUSTSA
def _define_DS_DOMAIN_TRUSTSA():
    DS_DOMAIN_TRUSTSA = win32more.Networking.ActiveDirectory.DS_DOMAIN_TRUSTSA_head
    DS_DOMAIN_TRUSTSA._fields_ = [
        ("NetbiosDomainName", win32more.Foundation.PSTR),
        ("DnsDomainName", win32more.Foundation.PSTR),
        ("Flags", UInt32),
        ("ParentIndex", UInt32),
        ("TrustType", UInt32),
        ("TrustAttributes", UInt32),
        ("DomainSid", win32more.Foundation.PSID),
        ("DomainGuid", Guid),
    ]
    return DS_DOMAIN_TRUSTSA
GetDcContextHandle = IntPtr
def _define_ADsGetObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("ADsGetObject", windll["ACTIVEDS"]), ((1, 'lpszPathName'),(1, 'riid'),(1, 'ppObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsBuildEnumerator():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.ActiveDirectory.IADsContainer_head,POINTER(win32more.System.Ole.IEnumVARIANT_head), use_last_error=False)(("ADsBuildEnumerator", windll["ACTIVEDS"]), ((1, 'pADsContainer'),(1, 'ppEnumVariant'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsFreeEnumerator():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IEnumVARIANT_head, use_last_error=False)(("ADsFreeEnumerator", windll["ACTIVEDS"]), ((1, 'pEnumVariant'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsEnumerateNext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IEnumVARIANT_head,UInt32,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt32), use_last_error=False)(("ADsEnumerateNext", windll["ACTIVEDS"]), ((1, 'pEnumVariant'),(1, 'cElements'),(1, 'pvar'),(1, 'pcElementsFetched'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsBuildVarArrayStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("ADsBuildVarArrayStr", windll["ACTIVEDS"]), ((1, 'lppPathNames'),(1, 'dwPathNames'),(1, 'pVar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsBuildVarArrayInt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("ADsBuildVarArrayInt", windll["ACTIVEDS"]), ((1, 'lpdwObjectTypes'),(1, 'dwObjectTypes'),(1, 'pVar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsOpenObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("ADsOpenObject", windll["ACTIVEDS"]), ((1, 'lpszPathName'),(1, 'lpszUserName'),(1, 'lpszPassword'),(1, 'dwReserved'),(1, 'riid'),(1, 'ppObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsGetLastError():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(Char),UInt32,POINTER(Char),UInt32, use_last_error=True)(("ADsGetLastError", windll["ACTIVEDS"]), ((1, 'lpError'),(1, 'lpErrorBuf'),(1, 'dwErrorBufLen'),(1, 'lpNameBuf'),(1, 'dwNameBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsSetLastError():
    try:
        return WINFUNCTYPE(Void,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("ADsSetLastError", windll["ACTIVEDS"]), ((1, 'dwErr'),(1, 'pszError'),(1, 'pszProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllocADsMem():
    try:
        return WINFUNCTYPE(c_void_p,UInt32, use_last_error=False)(("AllocADsMem", windll["ACTIVEDS"]), ((1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeADsMem():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p, use_last_error=False)(("FreeADsMem", windll["ACTIVEDS"]), ((1, 'pMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReallocADsMem():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,UInt32,UInt32, use_last_error=False)(("ReallocADsMem", windll["ACTIVEDS"]), ((1, 'pOldMem'),(1, 'cbOld'),(1, 'cbNew'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllocADsStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("AllocADsStr", windll["ACTIVEDS"]), ((1, 'pStr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeADsStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=False)(("FreeADsStr", windll["ACTIVEDS"]), ((1, 'pStr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReallocADsStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.PWSTR),win32more.Foundation.PWSTR, use_last_error=False)(("ReallocADsStr", windll["ACTIVEDS"]), ((1, 'ppStr'),(1, 'pStr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsEncodeBinaryData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("ADsEncodeBinaryData", windll["ACTIVEDS"]), ((1, 'pbSrcData'),(1, 'dwSrcLen'),(1, 'ppszDestData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsDecodeBinaryData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(("ADsDecodeBinaryData", windll["ACTIVEDS"]), ((1, 'szSrcData'),(1, 'ppbDestData'),(1, 'pdwDestLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantToAdsType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32,POINTER(POINTER(win32more.Networking.ActiveDirectory.ADSVALUE_head)),POINTER(UInt32), use_last_error=False)(("PropVariantToAdsType", windll["ACTIVEDS"]), ((1, 'pVariant'),(1, 'dwNumVariant'),(1, 'ppAdsValues'),(1, 'pdwNumValues'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AdsTypeToPropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.ActiveDirectory.ADSVALUE_head),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("AdsTypeToPropVariant", windll["ACTIVEDS"]), ((1, 'pAdsValues'),(1, 'dwNumValues'),(1, 'pVariant'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AdsFreeAdsValues():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.ActiveDirectory.ADSVALUE_head),UInt32, use_last_error=False)(("AdsFreeAdsValues", windll["ACTIVEDS"]), ((1, 'pAdsValues'),(1, 'dwNumValues'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BinarySDToSecurityDescriptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("BinarySDToSecurityDescriptor", windll["ACTIVEDS"]), ((1, 'pSecurityDescriptor'),(1, 'pVarsec'),(1, 'pszServerName'),(1, 'userName'),(1, 'passWord'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SecurityDescriptorToBinarySD():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),POINTER(UInt32),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("SecurityDescriptorToBinarySD", windll["ACTIVEDS"]), ((1, 'vVarSecDes'),(1, 'ppSecurityDescriptor'),(1, 'pdwSDLength'),(1, 'pszServerName'),(1, 'userName'),(1, 'passWord'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBrowseForContainerW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.ActiveDirectory.DSBROWSEINFOW_head), use_last_error=False)(("DsBrowseForContainerW", windll["dsuiext"]), ((1, 'pInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBrowseForContainer():
    return win32more.Networking.ActiveDirectory.DsBrowseForContainerW
def _define_DsBrowseForContainerA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.ActiveDirectory.DSBROWSEINFOA_head), use_last_error=False)(("DsBrowseForContainerA", windll["dsuiext"]), ((1, 'pInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetIcon():
    try:
        return WINFUNCTYPE(win32more.UI.WindowsAndMessaging.HICON,UInt32,win32more.Foundation.PWSTR,Int32,Int32, use_last_error=False)(("DsGetIcon", windll["dsuiext"]), ((1, 'dwFlags'),(1, 'pszObjectClass'),(1, 'cxImage'),(1, 'cyImage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetFriendlyClassName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Char),UInt32, use_last_error=False)(("DsGetFriendlyClassName", windll["dsuiext"]), ((1, 'pszObjectClass'),(1, 'pszBuffer'),(1, 'cchBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsPropCreateNotifyObj():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HWND), use_last_error=False)(("ADsPropCreateNotifyObj", windll["dsprop"]), ((1, 'pAppThdDataObj'),(1, 'pwzADsObjName'),(1, 'phNotifyObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsPropGetInitInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Networking.ActiveDirectory.ADSPROPINITPARAMS_head), use_last_error=False)(("ADsPropGetInitInfo", windll["dsprop"]), ((1, 'hNotifyObj'),(1, 'pInitParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsPropSetHwndWithTitle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.HWND,POINTER(SByte), use_last_error=False)(("ADsPropSetHwndWithTitle", windll["dsprop"]), ((1, 'hNotifyObj'),(1, 'hPage'),(1, 'ptzTitle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsPropSetHwnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.HWND, use_last_error=False)(("ADsPropSetHwnd", windll["dsprop"]), ((1, 'hNotifyObj'),(1, 'hPage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsPropCheckIfWritable():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Networking.ActiveDirectory.ADS_ATTR_INFO_head), use_last_error=False)(("ADsPropCheckIfWritable", windll["dsprop"]), ((1, 'pwzAttr'),(1, 'pWritableAttrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsPropSendErrorMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Networking.ActiveDirectory.ADSPROPERROR_head), use_last_error=False)(("ADsPropSendErrorMessage", windll["dsprop"]), ((1, 'hNotifyObj'),(1, 'pError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ADsPropShowErrorDialog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.HWND, use_last_error=False)(("ADsPropShowErrorDialog", windll["dsprop"]), ((1, 'hNotifyObj'),(1, 'hPage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsMakeSpnW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char), use_last_error=False)(("DsMakeSpnW", windll["DSPARSE"]), ((1, 'ServiceClass'),(1, 'ServiceName'),(1, 'InstanceName'),(1, 'InstancePort'),(1, 'Referrer'),(1, 'pcSpnLength'),(1, 'pszSpn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsMakeSpn():
    return win32more.Networking.ActiveDirectory.DsMakeSpnW
def _define_DsMakeSpnA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt16,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(Byte), use_last_error=False)(("DsMakeSpnA", windll["DSPARSE"]), ((1, 'ServiceClass'),(1, 'ServiceName'),(1, 'InstanceName'),(1, 'InstancePort'),(1, 'Referrer'),(1, 'pcSpnLength'),(1, 'pszSpn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsCrackSpnA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(Byte),POINTER(UInt32),POINTER(Byte),POINTER(UInt32),POINTER(Byte),POINTER(UInt16), use_last_error=False)(("DsCrackSpnA", windll["DSPARSE"]), ((1, 'pszSpn'),(1, 'pcServiceClass'),(1, 'ServiceClass'),(1, 'pcServiceName'),(1, 'ServiceName'),(1, 'pcInstanceName'),(1, 'InstanceName'),(1, 'pInstancePort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsCrackSpnW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt16), use_last_error=False)(("DsCrackSpnW", windll["DSPARSE"]), ((1, 'pszSpn'),(1, 'pcServiceClass'),(1, 'ServiceClass'),(1, 'pcServiceName'),(1, 'ServiceName'),(1, 'pcInstanceName'),(1, 'InstanceName'),(1, 'pInstancePort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsCrackSpn():
    return win32more.Networking.ActiveDirectory.DsCrackSpnW
def _define_DsQuoteRdnValueW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DsQuoteRdnValueW", windll["DSPARSE"]), ((1, 'cUnquotedRdnValueLength'),(1, 'psUnquotedRdnValue'),(1, 'pcQuotedRdnValueLength'),(1, 'psQuotedRdnValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsQuoteRdnValue():
    return win32more.Networking.ActiveDirectory.DsQuoteRdnValueW
def _define_DsQuoteRdnValueA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Byte),POINTER(UInt32),POINTER(Byte), use_last_error=False)(("DsQuoteRdnValueA", windll["DSPARSE"]), ((1, 'cUnquotedRdnValueLength'),(1, 'psUnquotedRdnValue'),(1, 'pcQuotedRdnValueLength'),(1, 'psQuotedRdnValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsUnquoteRdnValueW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DsUnquoteRdnValueW", windll["DSPARSE"]), ((1, 'cQuotedRdnValueLength'),(1, 'psQuotedRdnValue'),(1, 'pcUnquotedRdnValueLength'),(1, 'psUnquotedRdnValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsUnquoteRdnValue():
    return win32more.Networking.ActiveDirectory.DsUnquoteRdnValueW
def _define_DsUnquoteRdnValueA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Byte),POINTER(UInt32),POINTER(Byte), use_last_error=False)(("DsUnquoteRdnValueA", windll["DSPARSE"]), ((1, 'cQuotedRdnValueLength'),(1, 'psQuotedRdnValue'),(1, 'pcUnquotedRdnValueLength'),(1, 'psUnquotedRdnValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetRdnW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(("DsGetRdnW", windll["DSPARSE"]), ((1, 'ppDN'),(1, 'pcDN'),(1, 'ppKey'),(1, 'pcKey'),(1, 'ppVal'),(1, 'pcVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsCrackUnquotedMangledRdnW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Char),UInt32,POINTER(Guid),POINTER(win32more.Networking.ActiveDirectory.DS_MANGLE_FOR), use_last_error=False)(("DsCrackUnquotedMangledRdnW", windll["DSPARSE"]), ((1, 'pszRDN'),(1, 'cchRDN'),(1, 'pGuid'),(1, 'peDsMangleFor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsCrackUnquotedMangledRdn():
    return win32more.Networking.ActiveDirectory.DsCrackUnquotedMangledRdnW
def _define_DsCrackUnquotedMangledRdnA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Byte),UInt32,POINTER(Guid),POINTER(win32more.Networking.ActiveDirectory.DS_MANGLE_FOR), use_last_error=False)(("DsCrackUnquotedMangledRdnA", windll["DSPARSE"]), ((1, 'pszRDN'),(1, 'cchRDN'),(1, 'pGuid'),(1, 'peDsMangleFor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsIsMangledRdnValueW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Char),UInt32,win32more.Networking.ActiveDirectory.DS_MANGLE_FOR, use_last_error=False)(("DsIsMangledRdnValueW", windll["DSPARSE"]), ((1, 'pszRdn'),(1, 'cRdn'),(1, 'eDsMangleForDesired'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsIsMangledRdnValue():
    return win32more.Networking.ActiveDirectory.DsIsMangledRdnValueW
def _define_DsIsMangledRdnValueA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Byte),UInt32,win32more.Networking.ActiveDirectory.DS_MANGLE_FOR, use_last_error=False)(("DsIsMangledRdnValueA", windll["DSPARSE"]), ((1, 'pszRdn'),(1, 'cRdn'),(1, 'eDsMangleForDesired'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsIsMangledDnA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Networking.ActiveDirectory.DS_MANGLE_FOR, use_last_error=False)(("DsIsMangledDnA", windll["DSPARSE"]), ((1, 'pszDn'),(1, 'eDsMangleFor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsIsMangledDnW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Networking.ActiveDirectory.DS_MANGLE_FOR, use_last_error=False)(("DsIsMangledDnW", windll["DSPARSE"]), ((1, 'pszDn'),(1, 'eDsMangleFor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsIsMangledDn():
    return win32more.Networking.ActiveDirectory.DsIsMangledDnW
def _define_DsCrackSpn2A():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Byte),UInt32,POINTER(UInt32),POINTER(Byte),POINTER(UInt32),POINTER(Byte),POINTER(UInt32),POINTER(Byte),POINTER(UInt16), use_last_error=False)(("DsCrackSpn2A", windll["DSPARSE"]), ((1, 'pszSpn'),(1, 'cSpn'),(1, 'pcServiceClass'),(1, 'ServiceClass'),(1, 'pcServiceName'),(1, 'ServiceName'),(1, 'pcInstanceName'),(1, 'InstanceName'),(1, 'pInstancePort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsCrackSpn2W():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Char),UInt32,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt16), use_last_error=False)(("DsCrackSpn2W", windll["DSPARSE"]), ((1, 'pszSpn'),(1, 'cSpn'),(1, 'pcServiceClass'),(1, 'ServiceClass'),(1, 'pcServiceName'),(1, 'ServiceName'),(1, 'pcInstanceName'),(1, 'InstanceName'),(1, 'pInstancePort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsCrackSpn2():
    return win32more.Networking.ActiveDirectory.DsCrackSpn2W
def _define_DsCrackSpn3W():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt16),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DsCrackSpn3W", windll["DSPARSE"]), ((1, 'pszSpn'),(1, 'cSpn'),(1, 'pcHostName'),(1, 'HostName'),(1, 'pcInstanceName'),(1, 'InstanceName'),(1, 'pPortNumber'),(1, 'pcDomainName'),(1, 'DomainName'),(1, 'pcRealmName'),(1, 'RealmName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsCrackSpn4W():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DsCrackSpn4W", windll["DSPARSE"]), ((1, 'pszSpn'),(1, 'cSpn'),(1, 'pcHostName'),(1, 'HostName'),(1, 'pcInstanceName'),(1, 'InstanceName'),(1, 'pcPortName'),(1, 'PortName'),(1, 'pcDomainName'),(1, 'DomainName'),(1, 'pcRealmName'),(1, 'RealmName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindW", windll["NTDSAPI"]), ((1, 'DomainControllerName'),(1, 'DnsDomainName'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBind():
    return win32more.Networking.ActiveDirectory.DsBindW
def _define_DsBindA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindA", windll["NTDSAPI"]), ((1, 'DomainControllerName'),(1, 'DnsDomainName'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindWithCredW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindWithCredW", windll["NTDSAPI"]), ((1, 'DomainControllerName'),(1, 'DnsDomainName'),(1, 'AuthIdentity'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindWithCred():
    return win32more.Networking.ActiveDirectory.DsBindWithCredW
def _define_DsBindWithCredA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindWithCredA", windll["NTDSAPI"]), ((1, 'DomainControllerName'),(1, 'DnsDomainName'),(1, 'AuthIdentity'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindWithSpnW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindWithSpnW", windll["NTDSAPI"]), ((1, 'DomainControllerName'),(1, 'DnsDomainName'),(1, 'AuthIdentity'),(1, 'ServicePrincipalName'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindWithSpn():
    return win32more.Networking.ActiveDirectory.DsBindWithSpnW
def _define_DsBindWithSpnA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindWithSpnA", windll["NTDSAPI"]), ((1, 'DomainControllerName'),(1, 'DnsDomainName'),(1, 'AuthIdentity'),(1, 'ServicePrincipalName'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindWithSpnExW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindWithSpnExW", windll["NTDSAPI"]), ((1, 'DomainControllerName'),(1, 'DnsDomainName'),(1, 'AuthIdentity'),(1, 'ServicePrincipalName'),(1, 'BindFlags'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindWithSpnEx():
    return win32more.Networking.ActiveDirectory.DsBindWithSpnExW
def _define_DsBindWithSpnExA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindWithSpnExA", windll["NTDSAPI"]), ((1, 'DomainControllerName'),(1, 'DnsDomainName'),(1, 'AuthIdentity'),(1, 'ServicePrincipalName'),(1, 'BindFlags'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindByInstanceW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid),win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindByInstanceW", windll["NTDSAPI"]), ((1, 'ServerName'),(1, 'Annotation'),(1, 'InstanceGuid'),(1, 'DnsDomainName'),(1, 'AuthIdentity'),(1, 'ServicePrincipalName'),(1, 'BindFlags'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindByInstance():
    return win32more.Networking.ActiveDirectory.DsBindByInstanceW
def _define_DsBindByInstanceA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Guid),win32more.Foundation.PSTR,c_void_p,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindByInstanceA", windll["NTDSAPI"]), ((1, 'ServerName'),(1, 'Annotation'),(1, 'InstanceGuid'),(1, 'DnsDomainName'),(1, 'AuthIdentity'),(1, 'ServicePrincipalName'),(1, 'BindFlags'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindToISTGW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindToISTGW", windll["NTDSAPI"]), ((1, 'SiteName'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindToISTG():
    return win32more.Networking.ActiveDirectory.DsBindToISTGW
def _define_DsBindToISTGA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsBindToISTGA", windll["NTDSAPI"]), ((1, 'SiteName'),(1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsBindingSetTimeout():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("DsBindingSetTimeout", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'cTimeoutSecs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsUnBindW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsUnBindW", windll["NTDSAPI"]), ((1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsUnBind():
    return win32more.Networking.ActiveDirectory.DsUnBindW
def _define_DsUnBindA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("DsUnBindA", windll["NTDSAPI"]), ((1, 'phDS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsMakePasswordCredentialsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("DsMakePasswordCredentialsW", windll["NTDSAPI"]), ((1, 'User'),(1, 'Domain'),(1, 'Password'),(1, 'pAuthIdentity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsMakePasswordCredentials():
    return win32more.Networking.ActiveDirectory.DsMakePasswordCredentialsW
def _define_DsMakePasswordCredentialsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(c_void_p), use_last_error=False)(("DsMakePasswordCredentialsA", windll["NTDSAPI"]), ((1, 'User'),(1, 'Domain'),(1, 'Password'),(1, 'pAuthIdentity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsFreePasswordCredentials():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("DsFreePasswordCredentials", windll["NTDSAPI"]), ((1, 'AuthIdentity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsCrackNamesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.ActiveDirectory.DS_NAME_FLAGS,win32more.Networking.ActiveDirectory.DS_NAME_FORMAT,win32more.Networking.ActiveDirectory.DS_NAME_FORMAT,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTW_head)), use_last_error=False)(("DsCrackNamesW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'flags'),(1, 'formatOffered'),(1, 'formatDesired'),(1, 'cNames'),(1, 'rpNames'),(1, 'ppResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsCrackNames():
    return win32more.Networking.ActiveDirectory.DsCrackNamesW
def _define_DsCrackNamesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.ActiveDirectory.DS_NAME_FLAGS,win32more.Networking.ActiveDirectory.DS_NAME_FORMAT,win32more.Networking.ActiveDirectory.DS_NAME_FORMAT,UInt32,POINTER(win32more.Foundation.PSTR),POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTA_head)), use_last_error=False)(("DsCrackNamesA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'flags'),(1, 'formatOffered'),(1, 'formatDesired'),(1, 'cNames'),(1, 'rpNames'),(1, 'ppResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsFreeNameResultW():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTW_head), use_last_error=False)(("DsFreeNameResultW", windll["NTDSAPI"]), ((1, 'pResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsFreeNameResult():
    return win32more.Networking.ActiveDirectory.DsFreeNameResultW
def _define_DsFreeNameResultA():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTA_head), use_last_error=False)(("DsFreeNameResultA", windll["NTDSAPI"]), ((1, 'pResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetSpnA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Networking.ActiveDirectory.DS_SPN_NAME_TYPE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt16,UInt16,POINTER(win32more.Foundation.PSTR),POINTER(UInt16),POINTER(UInt32),POINTER(POINTER(win32more.Foundation.PSTR)), use_last_error=False)(("DsGetSpnA", windll["NTDSAPI"]), ((1, 'ServiceType'),(1, 'ServiceClass'),(1, 'ServiceName'),(1, 'InstancePort'),(1, 'cInstanceNames'),(1, 'pInstanceNames'),(1, 'pInstancePorts'),(1, 'pcSpn'),(1, 'prpszSpn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetSpnW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Networking.ActiveDirectory.DS_SPN_NAME_TYPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16,UInt16,POINTER(win32more.Foundation.PWSTR),POINTER(UInt16),POINTER(UInt32),POINTER(POINTER(win32more.Foundation.PWSTR)), use_last_error=False)(("DsGetSpnW", windll["NTDSAPI"]), ((1, 'ServiceType'),(1, 'ServiceClass'),(1, 'ServiceName'),(1, 'InstancePort'),(1, 'cInstanceNames'),(1, 'pInstanceNames'),(1, 'pInstancePorts'),(1, 'pcSpn'),(1, 'prpszSpn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetSpn():
    return win32more.Networking.ActiveDirectory.DsGetSpnW
def _define_DsFreeSpnArrayA():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(win32more.Foundation.PSTR), use_last_error=False)(("DsFreeSpnArrayA", windll["NTDSAPI"]), ((1, 'cSpn'),(1, 'rpszSpn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsFreeSpnArrayW():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("DsFreeSpnArrayW", windll["NTDSAPI"]), ((1, 'cSpn'),(1, 'rpszSpn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsFreeSpnArray():
    return win32more.Networking.ActiveDirectory.DsFreeSpnArrayW
def _define_DsWriteAccountSpnA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.ActiveDirectory.DS_SPN_WRITE_OP,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Foundation.PSTR), use_last_error=False)(("DsWriteAccountSpnA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'Operation'),(1, 'pszAccount'),(1, 'cSpn'),(1, 'rpszSpn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsWriteAccountSpnW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.ActiveDirectory.DS_SPN_WRITE_OP,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("DsWriteAccountSpnW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'Operation'),(1, 'pszAccount'),(1, 'cSpn'),(1, 'rpszSpn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsWriteAccountSpn():
    return win32more.Networking.ActiveDirectory.DsWriteAccountSpnW
def _define_DsClientMakeSpnForTargetServerW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char), use_last_error=False)(("DsClientMakeSpnForTargetServerW", windll["NTDSAPI"]), ((1, 'ServiceClass'),(1, 'ServiceName'),(1, 'pcSpnLength'),(1, 'pszSpn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsClientMakeSpnForTargetServer():
    return win32more.Networking.ActiveDirectory.DsClientMakeSpnForTargetServerW
def _define_DsClientMakeSpnForTargetServerA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(Byte), use_last_error=False)(("DsClientMakeSpnForTargetServerA", windll["NTDSAPI"]), ((1, 'ServiceClass'),(1, 'ServiceName'),(1, 'pcSpnLength'),(1, 'pszSpn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsServerRegisterSpnA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Networking.ActiveDirectory.DS_SPN_WRITE_OP,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("DsServerRegisterSpnA", windll["NTDSAPI"]), ((1, 'Operation'),(1, 'ServiceClass'),(1, 'UserObjectDN'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsServerRegisterSpnW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Networking.ActiveDirectory.DS_SPN_WRITE_OP,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DsServerRegisterSpnW", windll["NTDSAPI"]), ((1, 'Operation'),(1, 'ServiceClass'),(1, 'UserObjectDN'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsServerRegisterSpn():
    return win32more.Networking.ActiveDirectory.DsServerRegisterSpnW
def _define_DsReplicaSyncA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(Guid),UInt32, use_last_error=False)(("DsReplicaSyncA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'pUuidDsaSrc'),(1, 'Options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaSyncW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(Guid),UInt32, use_last_error=False)(("DsReplicaSyncW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'pUuidDsaSrc'),(1, 'Options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaSync():
    return win32more.Networking.ActiveDirectory.DsReplicaSyncW
def _define_DsReplicaAddA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.ActiveDirectory.SCHEDULE_head),UInt32, use_last_error=False)(("DsReplicaAddA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'SourceDsaDn'),(1, 'TransportDn'),(1, 'SourceDsaAddress'),(1, 'pSchedule'),(1, 'Options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaAddW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.ActiveDirectory.SCHEDULE_head),UInt32, use_last_error=False)(("DsReplicaAddW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'SourceDsaDn'),(1, 'TransportDn'),(1, 'SourceDsaAddress'),(1, 'pSchedule'),(1, 'Options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaAdd():
    return win32more.Networking.ActiveDirectory.DsReplicaAddW
def _define_DsReplicaDelA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("DsReplicaDelA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'DsaSrc'),(1, 'Options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaDelW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("DsReplicaDelW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'DsaSrc'),(1, 'Options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaDel():
    return win32more.Networking.ActiveDirectory.DsReplicaDelW
def _define_DsReplicaModifyA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(Guid),win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.ActiveDirectory.SCHEDULE_head),UInt32,UInt32,UInt32, use_last_error=False)(("DsReplicaModifyA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'pUuidSourceDsa'),(1, 'TransportDn'),(1, 'SourceDsaAddress'),(1, 'pSchedule'),(1, 'ReplicaFlags'),(1, 'ModifyFields'),(1, 'Options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaModifyW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(Guid),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.ActiveDirectory.SCHEDULE_head),UInt32,UInt32,UInt32, use_last_error=False)(("DsReplicaModifyW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'pUuidSourceDsa'),(1, 'TransportDn'),(1, 'SourceDsaAddress'),(1, 'pSchedule'),(1, 'ReplicaFlags'),(1, 'ModifyFields'),(1, 'Options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaModify():
    return win32more.Networking.ActiveDirectory.DsReplicaModifyW
def _define_DsReplicaUpdateRefsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Guid),UInt32, use_last_error=False)(("DsReplicaUpdateRefsA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'DsaDest'),(1, 'pUuidDsaDest'),(1, 'Options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaUpdateRefsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid),UInt32, use_last_error=False)(("DsReplicaUpdateRefsW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'DsaDest'),(1, 'pUuidDsaDest'),(1, 'Options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaUpdateRefs():
    return win32more.Networking.ActiveDirectory.DsReplicaUpdateRefsW
def _define_DsReplicaSyncAllA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,UInt32,IntPtr,c_void_p,POINTER(POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_REPSYNCALL_ERRINFOA_head))), use_last_error=False)(("DsReplicaSyncAllA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'pszNameContext'),(1, 'ulFlags'),(1, 'pFnCallBack'),(1, 'pCallbackData'),(1, 'pErrors'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaSyncAllW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,IntPtr,c_void_p,POINTER(POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_REPSYNCALL_ERRINFOW_head))), use_last_error=False)(("DsReplicaSyncAllW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'pszNameContext'),(1, 'ulFlags'),(1, 'pFnCallBack'),(1, 'pCallbackData'),(1, 'pErrors'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaSyncAll():
    return win32more.Networking.ActiveDirectory.DsReplicaSyncAllW
def _define_DsRemoveDsServerW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL),win32more.Foundation.BOOL, use_last_error=False)(("DsRemoveDsServerW", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'ServerDN'),(1, 'DomainDN'),(1, 'fLastDcInDomain'),(1, 'fCommit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsRemoveDsServer():
    return win32more.Networking.ActiveDirectory.DsRemoveDsServerW
def _define_DsRemoveDsServerA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Foundation.BOOL),win32more.Foundation.BOOL, use_last_error=False)(("DsRemoveDsServerA", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'ServerDN'),(1, 'DomainDN'),(1, 'fLastDcInDomain'),(1, 'fCommit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsRemoveDsDomainW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR, use_last_error=False)(("DsRemoveDsDomainW", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'DomainDN'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsRemoveDsDomain():
    return win32more.Networking.ActiveDirectory.DsRemoveDsDomainW
def _define_DsRemoveDsDomainA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR, use_last_error=False)(("DsRemoveDsDomainA", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'DomainDN'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListSitesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTA_head)), use_last_error=False)(("DsListSitesA", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'ppSites'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListSitesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTW_head)), use_last_error=False)(("DsListSitesW", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'ppSites'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListSites():
    return win32more.Networking.ActiveDirectory.DsListSitesW
def _define_DsListServersInSiteA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTA_head)), use_last_error=False)(("DsListServersInSiteA", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'site'),(1, 'ppServers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListServersInSiteW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTW_head)), use_last_error=False)(("DsListServersInSiteW", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'site'),(1, 'ppServers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListServersInSite():
    return win32more.Networking.ActiveDirectory.DsListServersInSiteW
def _define_DsListDomainsInSiteA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTA_head)), use_last_error=False)(("DsListDomainsInSiteA", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'site'),(1, 'ppDomains'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListDomainsInSiteW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTW_head)), use_last_error=False)(("DsListDomainsInSiteW", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'site'),(1, 'ppDomains'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListDomainsInSite():
    return win32more.Networking.ActiveDirectory.DsListDomainsInSiteW
def _define_DsListServersForDomainInSiteA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTA_head)), use_last_error=False)(("DsListServersForDomainInSiteA", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'domain'),(1, 'site'),(1, 'ppServers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListServersForDomainInSiteW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTW_head)), use_last_error=False)(("DsListServersForDomainInSiteW", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'domain'),(1, 'site'),(1, 'ppServers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListServersForDomainInSite():
    return win32more.Networking.ActiveDirectory.DsListServersForDomainInSiteW
def _define_DsListInfoForServerA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTA_head)), use_last_error=False)(("DsListInfoForServerA", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'server'),(1, 'ppInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListInfoForServerW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTW_head)), use_last_error=False)(("DsListInfoForServerW", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'server'),(1, 'ppInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListInfoForServer():
    return win32more.Networking.ActiveDirectory.DsListInfoForServerW
def _define_DsListRolesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTA_head)), use_last_error=False)(("DsListRolesA", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'ppRoles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListRolesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_NAME_RESULTW_head)), use_last_error=False)(("DsListRolesW", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'ppRoles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsListRoles():
    return win32more.Networking.ActiveDirectory.DsListRolesW
def _define_DsQuerySitesByCostW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,UInt32,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_SITE_COST_INFO_head)), use_last_error=False)(("DsQuerySitesByCostW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'pwszFromSite'),(1, 'rgwszToSites'),(1, 'cToSites'),(1, 'dwFlags'),(1, 'prgSiteInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsQuerySitesByCost():
    return win32more.Networking.ActiveDirectory.DsQuerySitesByCostW
def _define_DsQuerySitesByCostA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PSTR),UInt32,UInt32,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_SITE_COST_INFO_head)), use_last_error=False)(("DsQuerySitesByCostA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'pszFromSite'),(1, 'rgszToSites'),(1, 'cToSites'),(1, 'dwFlags'),(1, 'prgSiteInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsQuerySitesFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.ActiveDirectory.DS_SITE_COST_INFO_head), use_last_error=False)(("DsQuerySitesFree", windll["NTDSAPI"]), ((1, 'rgSiteInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsMapSchemaGuidsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(Guid),POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_SCHEMA_GUID_MAPA_head)), use_last_error=False)(("DsMapSchemaGuidsA", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'cGuids'),(1, 'rGuids'),(1, 'ppGuidMap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsFreeSchemaGuidMapA():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.ActiveDirectory.DS_SCHEMA_GUID_MAPA_head), use_last_error=False)(("DsFreeSchemaGuidMapA", windll["NTDSAPI"]), ((1, 'pGuidMap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsMapSchemaGuidsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(Guid),POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_SCHEMA_GUID_MAPW_head)), use_last_error=False)(("DsMapSchemaGuidsW", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'cGuids'),(1, 'rGuids'),(1, 'ppGuidMap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsMapSchemaGuids():
    return win32more.Networking.ActiveDirectory.DsMapSchemaGuidsW
def _define_DsFreeSchemaGuidMapW():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.ActiveDirectory.DS_SCHEMA_GUID_MAPW_head), use_last_error=False)(("DsFreeSchemaGuidMapW", windll["NTDSAPI"]), ((1, 'pGuidMap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsFreeSchemaGuidMap():
    return win32more.Networking.ActiveDirectory.DsFreeSchemaGuidMapW
def _define_DsGetDomainControllerInfoA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,UInt32,POINTER(UInt32),POINTER(c_void_p), use_last_error=False)(("DsGetDomainControllerInfoA", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'DomainName'),(1, 'InfoLevel'),(1, 'pcOut'),(1, 'ppInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDomainControllerInfoW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(c_void_p), use_last_error=False)(("DsGetDomainControllerInfoW", windll["NTDSAPI"]), ((1, 'hDs'),(1, 'DomainName'),(1, 'InfoLevel'),(1, 'pcOut'),(1, 'ppInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDomainControllerInfo():
    return win32more.Networking.ActiveDirectory.DsGetDomainControllerInfoW
def _define_DsFreeDomainControllerInfoA():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Void), use_last_error=False)(("DsFreeDomainControllerInfoA", windll["NTDSAPI"]), ((1, 'InfoLevel'),(1, 'cInfo'),(1, 'pInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsFreeDomainControllerInfoW():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Void), use_last_error=False)(("DsFreeDomainControllerInfoW", windll["NTDSAPI"]), ((1, 'InfoLevel'),(1, 'cInfo'),(1, 'pInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsFreeDomainControllerInfo():
    return win32more.Networking.ActiveDirectory.DsFreeDomainControllerInfoW
def _define_DsReplicaConsistencyCheck():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.ActiveDirectory.DS_KCC_TASKID,UInt32, use_last_error=False)(("DsReplicaConsistencyCheck", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'TaskID'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaVerifyObjectsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(Guid),UInt32, use_last_error=False)(("DsReplicaVerifyObjectsW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'pUuidDsaSrc'),(1, 'ulOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaVerifyObjects():
    return win32more.Networking.ActiveDirectory.DsReplicaVerifyObjectsW
def _define_DsReplicaVerifyObjectsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(Guid),UInt32, use_last_error=False)(("DsReplicaVerifyObjectsA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'NameContext'),(1, 'pUuidDsaSrc'),(1, 'ulOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaGetInfoW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.ActiveDirectory.DS_REPL_INFO_TYPE,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("DsReplicaGetInfoW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'InfoType'),(1, 'pszObject'),(1, 'puuidForSourceDsaObjGuid'),(1, 'ppInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaGetInfo2W():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.ActiveDirectory.DS_REPL_INFO_TYPE,win32more.Foundation.PWSTR,POINTER(Guid),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(c_void_p), use_last_error=False)(("DsReplicaGetInfo2W", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'InfoType'),(1, 'pszObject'),(1, 'puuidForSourceDsaObjGuid'),(1, 'pszAttributeName'),(1, 'pszValue'),(1, 'dwFlags'),(1, 'dwEnumerationContext'),(1, 'ppInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsReplicaFreeInfo():
    try:
        return WINFUNCTYPE(Void,win32more.Networking.ActiveDirectory.DS_REPL_INFO_TYPE,c_void_p, use_last_error=False)(("DsReplicaFreeInfo", windll["NTDSAPI"]), ((1, 'InfoType'),(1, 'pInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsAddSidHistoryW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DsAddSidHistoryW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'Flags'),(1, 'SrcDomain'),(1, 'SrcPrincipal'),(1, 'SrcDomainController'),(1, 'SrcDomainCreds'),(1, 'DstDomain'),(1, 'DstPrincipal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsAddSidHistory():
    return win32more.Networking.ActiveDirectory.DsAddSidHistoryW
def _define_DsAddSidHistoryA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("DsAddSidHistoryA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'Flags'),(1, 'SrcDomain'),(1, 'SrcPrincipal'),(1, 'SrcDomainController'),(1, 'SrcDomainCreds'),(1, 'DstDomain'),(1, 'DstPrincipal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsInheritSecurityIdentityW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DsInheritSecurityIdentityW", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'Flags'),(1, 'SrcPrincipal'),(1, 'DstPrincipal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsInheritSecurityIdentity():
    return win32more.Networking.ActiveDirectory.DsInheritSecurityIdentityW
def _define_DsInheritSecurityIdentityA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("DsInheritSecurityIdentityA", windll["NTDSAPI"]), ((1, 'hDS'),(1, 'Flags'),(1, 'SrcPrincipal'),(1, 'DstPrincipal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsRoleGetPrimaryDomainInformation():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Networking.ActiveDirectory.DSROLE_PRIMARY_DOMAIN_INFO_LEVEL,POINTER(c_char_p_no), use_last_error=False)(("DsRoleGetPrimaryDomainInformation", windll["NETAPI32"]), ((1, 'lpServer'),(1, 'InfoLevel'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsRoleFreeMemory():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("DsRoleFreeMemory", windll["NETAPI32"]), ((1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDcNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Guid),win32more.Foundation.PSTR,UInt32,POINTER(POINTER(win32more.Networking.ActiveDirectory.DOMAIN_CONTROLLER_INFOA_head)), use_last_error=False)(("DsGetDcNameA", windll["NETAPI32"]), ((1, 'ComputerName'),(1, 'DomainName'),(1, 'DomainGuid'),(1, 'SiteName'),(1, 'Flags'),(1, 'DomainControllerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDcNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.Networking.ActiveDirectory.DOMAIN_CONTROLLER_INFOW_head)), use_last_error=False)(("DsGetDcNameW", windll["NETAPI32"]), ((1, 'ComputerName'),(1, 'DomainName'),(1, 'DomainGuid'),(1, 'SiteName'),(1, 'Flags'),(1, 'DomainControllerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDcName():
    return win32more.Networking.ActiveDirectory.DsGetDcNameW
def _define_DsGetSiteNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PSTR), use_last_error=False)(("DsGetSiteNameA", windll["NETAPI32"]), ((1, 'ComputerName'),(1, 'SiteName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetSiteNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("DsGetSiteNameW", windll["NETAPI32"]), ((1, 'ComputerName'),(1, 'SiteName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetSiteName():
    return win32more.Networking.ActiveDirectory.DsGetSiteNameW
def _define_DsValidateSubnetNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("DsValidateSubnetNameW", windll["NETAPI32"]), ((1, 'SubnetName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsValidateSubnetName():
    return win32more.Networking.ActiveDirectory.DsValidateSubnetNameW
def _define_DsValidateSubnetNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("DsValidateSubnetNameA", windll["NETAPI32"]), ((1, 'SubnetName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsAddressToSiteNamesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Networking.WinSock.SOCKET_ADDRESS),POINTER(POINTER(win32more.Foundation.PWSTR)), use_last_error=False)(("DsAddressToSiteNamesW", windll["NETAPI32"]), ((1, 'ComputerName'),(1, 'EntryCount'),(1, 'SocketAddresses'),(1, 'SiteNames'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsAddressToSiteNames():
    return win32more.Networking.ActiveDirectory.DsAddressToSiteNamesW
def _define_DsAddressToSiteNamesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Networking.WinSock.SOCKET_ADDRESS),POINTER(POINTER(win32more.Foundation.PSTR)), use_last_error=False)(("DsAddressToSiteNamesA", windll["NETAPI32"]), ((1, 'ComputerName'),(1, 'EntryCount'),(1, 'SocketAddresses'),(1, 'SiteNames'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsAddressToSiteNamesExW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Networking.WinSock.SOCKET_ADDRESS),POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(POINTER(win32more.Foundation.PWSTR)), use_last_error=False)(("DsAddressToSiteNamesExW", windll["NETAPI32"]), ((1, 'ComputerName'),(1, 'EntryCount'),(1, 'SocketAddresses'),(1, 'SiteNames'),(1, 'SubnetNames'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsAddressToSiteNamesEx():
    return win32more.Networking.ActiveDirectory.DsAddressToSiteNamesExW
def _define_DsAddressToSiteNamesExA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Networking.WinSock.SOCKET_ADDRESS),POINTER(POINTER(win32more.Foundation.PSTR)),POINTER(POINTER(win32more.Foundation.PSTR)), use_last_error=False)(("DsAddressToSiteNamesExA", windll["NETAPI32"]), ((1, 'ComputerName'),(1, 'EntryCount'),(1, 'SocketAddresses'),(1, 'SiteNames'),(1, 'SubnetNames'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsEnumerateDomainTrustsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_DOMAIN_TRUSTSW_head)),POINTER(UInt32), use_last_error=False)(("DsEnumerateDomainTrustsW", windll["NETAPI32"]), ((1, 'ServerName'),(1, 'Flags'),(1, 'Domains'),(1, 'DomainCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsEnumerateDomainTrusts():
    return win32more.Networking.ActiveDirectory.DsEnumerateDomainTrustsW
def _define_DsEnumerateDomainTrustsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,POINTER(POINTER(win32more.Networking.ActiveDirectory.DS_DOMAIN_TRUSTSA_head)),POINTER(UInt32), use_last_error=False)(("DsEnumerateDomainTrustsA", windll["NETAPI32"]), ((1, 'ServerName'),(1, 'Flags'),(1, 'Domains'),(1, 'DomainCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetForestTrustInformationW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.Security.Authentication.Identity.LSA_FOREST_TRUST_INFORMATION_head)), use_last_error=False)(("DsGetForestTrustInformationW", windll["NETAPI32"]), ((1, 'ServerName'),(1, 'TrustedDomainName'),(1, 'Flags'),(1, 'ForestTrustInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsMergeForestTrustInformationW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Security.Authentication.Identity.LSA_FOREST_TRUST_INFORMATION_head),POINTER(win32more.Security.Authentication.Identity.LSA_FOREST_TRUST_INFORMATION_head),POINTER(POINTER(win32more.Security.Authentication.Identity.LSA_FOREST_TRUST_INFORMATION_head)), use_last_error=False)(("DsMergeForestTrustInformationW", windll["NETAPI32"]), ((1, 'DomainName'),(1, 'NewForestTrustInfo'),(1, 'OldForestTrustInfo'),(1, 'MergedForestTrustInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDcSiteCoverageW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(POINTER(win32more.Foundation.PWSTR)), use_last_error=False)(("DsGetDcSiteCoverageW", windll["NETAPI32"]), ((1, 'ServerName'),(1, 'EntryCount'),(1, 'SiteNames'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDcSiteCoverage():
    return win32more.Networking.ActiveDirectory.DsGetDcSiteCoverageW
def _define_DsGetDcSiteCoverageA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(POINTER(win32more.Foundation.PSTR)), use_last_error=False)(("DsGetDcSiteCoverageA", windll["NETAPI32"]), ((1, 'ServerName'),(1, 'EntryCount'),(1, 'SiteNames'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsDeregisterDnsHostRecordsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(Guid),win32more.Foundation.PWSTR, use_last_error=False)(("DsDeregisterDnsHostRecordsW", windll["NETAPI32"]), ((1, 'ServerName'),(1, 'DnsDomainName'),(1, 'DomainGuid'),(1, 'DsaGuid'),(1, 'DnsHostName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsDeregisterDnsHostRecords():
    return win32more.Networking.ActiveDirectory.DsDeregisterDnsHostRecordsW
def _define_DsDeregisterDnsHostRecordsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Guid),POINTER(Guid),win32more.Foundation.PSTR, use_last_error=False)(("DsDeregisterDnsHostRecordsA", windll["NETAPI32"]), ((1, 'ServerName'),(1, 'DnsDomainName'),(1, 'DomainGuid'),(1, 'DsaGuid'),(1, 'DnsHostName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDcOpenW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Networking.ActiveDirectory.GetDcContextHandle), use_last_error=False)(("DsGetDcOpenW", windll["NETAPI32"]), ((1, 'DnsName'),(1, 'OptionFlags'),(1, 'SiteName'),(1, 'DomainGuid'),(1, 'DnsForestName'),(1, 'DcFlags'),(1, 'RetGetDcContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDcOpen():
    return win32more.Networking.ActiveDirectory.DsGetDcOpenW
def _define_DsGetDcOpenA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(Guid),win32more.Foundation.PSTR,UInt32,POINTER(win32more.Networking.ActiveDirectory.GetDcContextHandle), use_last_error=False)(("DsGetDcOpenA", windll["NETAPI32"]), ((1, 'DnsName'),(1, 'OptionFlags'),(1, 'SiteName'),(1, 'DomainGuid'),(1, 'DnsForestName'),(1, 'DcFlags'),(1, 'RetGetDcContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDcNextW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(POINTER(win32more.Networking.WinSock.SOCKET_ADDRESS_head)),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("DsGetDcNextW", windll["NETAPI32"]), ((1, 'GetDcContextHandle'),(1, 'SockAddressCount'),(1, 'SockAddresses'),(1, 'DnsHostName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDcNext():
    return win32more.Networking.ActiveDirectory.DsGetDcNextW
def _define_DsGetDcNextA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(POINTER(win32more.Networking.WinSock.SOCKET_ADDRESS_head)),POINTER(win32more.Foundation.PSTR), use_last_error=False)(("DsGetDcNextA", windll["NETAPI32"]), ((1, 'GetDcContextHandle'),(1, 'SockAddressCount'),(1, 'SockAddresses'),(1, 'DnsHostName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DsGetDcCloseW():
    try:
        return WINFUNCTYPE(Void,win32more.Networking.ActiveDirectory.GetDcContextHandle, use_last_error=False)(("DsGetDcCloseW", windll["NETAPI32"]), ((1, 'GetDcContextHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WM_ADSPROP_NOTIFY_PAGEINIT",
    "WM_ADSPROP_NOTIFY_PAGEHWND",
    "WM_ADSPROP_NOTIFY_CHANGE",
    "WM_ADSPROP_NOTIFY_APPLY",
    "WM_ADSPROP_NOTIFY_SETFOCUS",
    "WM_ADSPROP_NOTIFY_FOREGROUND",
    "WM_ADSPROP_NOTIFY_EXIT",
    "WM_ADSPROP_NOTIFY_ERROR",
    "CLSID_CommonQuery",
    "QUERYFORM_CHANGESFORMLIST",
    "QUERYFORM_CHANGESOPTFORMLIST",
    "CQFF_NOGLOBALPAGES",
    "CQFF_ISOPTIONAL",
    "CQPM_INITIALIZE",
    "CQPM_RELEASE",
    "CQPM_ENABLE",
    "CQPM_GETPARAMETERS",
    "CQPM_CLEARFORM",
    "CQPM_PERSIST",
    "CQPM_HELP",
    "CQPM_SETDEFAULTPARAMETERS",
    "CQPM_HANDLERSPECIFIC",
    "OQWF_OKCANCEL",
    "OQWF_DEFAULTFORM",
    "OQWF_SINGLESELECT",
    "OQWF_LOADQUERY",
    "OQWF_REMOVESCOPES",
    "OQWF_REMOVEFORMS",
    "OQWF_ISSUEONOPEN",
    "OQWF_SHOWOPTIONAL",
    "OQWF_SAVEQUERYONOK",
    "OQWF_HIDEMENUS",
    "OQWF_HIDESEARCHUI",
    "OQWF_PARAMISPROPERTYBAG",
    "CLSID_DsAdminCreateObj",
    "DSA_NEWOBJ_CTX_PRECOMMIT",
    "DSA_NEWOBJ_CTX_COMMIT",
    "DSA_NEWOBJ_CTX_POSTCOMMIT",
    "DSA_NEWOBJ_CTX_CLEANUP",
    "DSA_NOTIFY_DEL",
    "DSA_NOTIFY_REN",
    "DSA_NOTIFY_MOV",
    "DSA_NOTIFY_PROP",
    "DSA_NOTIFY_FLAG_ADDITIONAL_DATA",
    "DSA_NOTIFY_FLAG_FORCE_ADDITIONAL_DATA",
    "CLSID_MicrosoftDS",
    "CLSID_DsPropertyPages",
    "CLSID_DsDomainTreeBrowser",
    "CLSID_DsDisplaySpecifier",
    "CLSID_DsFolderProperties",
    "DSOBJECT_ISCONTAINER",
    "DSOBJECT_READONLYPAGES",
    "DSPROVIDER_UNUSED_0",
    "DSPROVIDER_UNUSED_1",
    "DSPROVIDER_UNUSED_2",
    "DSPROVIDER_UNUSED_3",
    "DSPROVIDER_ADVANCED",
    "DSPROVIDER_AD_LDS",
    "DSDSOF_HASUSERANDSERVERINFO",
    "DSDSOF_SIMPLEAUTHENTICATE",
    "DSDSOF_DONTSIGNSEAL",
    "DSDSOF_DSAVAILABLE",
    "DBDTF_RETURNFQDN",
    "DBDTF_RETURNMIXEDDOMAINS",
    "DBDTF_RETURNEXTERNAL",
    "DBDTF_RETURNINBOUND",
    "DBDTF_RETURNINOUTBOUND",
    "DSSSF_SIMPLEAUTHENTICATE",
    "DSSSF_DONTSIGNSEAL",
    "DSSSF_DSAVAILABLE",
    "DSGIF_ISNORMAL",
    "DSGIF_ISOPEN",
    "DSGIF_ISDISABLED",
    "DSGIF_ISMASK",
    "DSGIF_GETDEFAULTICON",
    "DSGIF_DEFAULTISCONTAINER",
    "DSICCF_IGNORETREATASLEAF",
    "DSECAF_NOTLISTED",
    "DSCCIF_HASWIZARDDIALOG",
    "DSCCIF_HASWIZARDPRIMARYPAGE",
    "DSBI_NOBUTTONS",
    "DSBI_NOLINES",
    "DSBI_NOLINESATROOT",
    "DSBI_CHECKBOXES",
    "DSBI_NOROOT",
    "DSBI_INCLUDEHIDDEN",
    "DSBI_EXPANDONOPEN",
    "DSBI_ENTIREDIRECTORY",
    "DSBI_RETURN_FORMAT",
    "DSBI_HASCREDENTIALS",
    "DSBI_IGNORETREATASLEAF",
    "DSBI_SIMPLEAUTHENTICATE",
    "DSBI_RETURNOBJECTCLASS",
    "DSBI_DONTSIGNSEAL",
    "DSB_MAX_DISPLAYNAME_CHARS",
    "DSBF_STATE",
    "DSBF_ICONLOCATION",
    "DSBF_DISPLAYNAME",
    "DSBS_CHECKED",
    "DSBS_HIDDEN",
    "DSBS_ROOT",
    "DSBM_QUERYINSERTW",
    "DSBM_QUERYINSERTA",
    "DSBM_QUERYINSERT",
    "DSBM_CHANGEIMAGESTATE",
    "DSBM_HELP",
    "DSBM_CONTEXTMENU",
    "DSBID_BANNER",
    "DSBID_CONTAINERLIST",
    "DS_FORCE_REDISCOVERY",
    "DS_DIRECTORY_SERVICE_REQUIRED",
    "DS_DIRECTORY_SERVICE_PREFERRED",
    "DS_GC_SERVER_REQUIRED",
    "DS_PDC_REQUIRED",
    "DS_BACKGROUND_ONLY",
    "DS_IP_REQUIRED",
    "DS_KDC_REQUIRED",
    "DS_TIMESERV_REQUIRED",
    "DS_WRITABLE_REQUIRED",
    "DS_GOOD_TIMESERV_PREFERRED",
    "DS_AVOID_SELF",
    "DS_ONLY_LDAP_NEEDED",
    "DS_IS_FLAT_NAME",
    "DS_IS_DNS_NAME",
    "DS_TRY_NEXTCLOSEST_SITE",
    "DS_DIRECTORY_SERVICE_6_REQUIRED",
    "DS_WEB_SERVICE_REQUIRED",
    "DS_DIRECTORY_SERVICE_8_REQUIRED",
    "DS_DIRECTORY_SERVICE_9_REQUIRED",
    "DS_DIRECTORY_SERVICE_10_REQUIRED",
    "DS_KEY_LIST_SUPPORT_REQUIRED",
    "DS_RETURN_DNS_NAME",
    "DS_RETURN_FLAT_NAME",
    "DS_PDC_FLAG",
    "DS_GC_FLAG",
    "DS_LDAP_FLAG",
    "DS_DS_FLAG",
    "DS_KDC_FLAG",
    "DS_TIMESERV_FLAG",
    "DS_CLOSEST_FLAG",
    "DS_WRITABLE_FLAG",
    "DS_GOOD_TIMESERV_FLAG",
    "DS_NDNC_FLAG",
    "DS_SELECT_SECRET_DOMAIN_6_FLAG",
    "DS_FULL_SECRET_DOMAIN_6_FLAG",
    "DS_WS_FLAG",
    "DS_DS_8_FLAG",
    "DS_DS_9_FLAG",
    "DS_DS_10_FLAG",
    "DS_KEY_LIST_FLAG",
    "DS_PING_FLAGS",
    "DS_DNS_CONTROLLER_FLAG",
    "DS_DNS_DOMAIN_FLAG",
    "DS_DNS_FOREST_FLAG",
    "DS_DOMAIN_IN_FOREST",
    "DS_DOMAIN_DIRECT_OUTBOUND",
    "DS_DOMAIN_TREE_ROOT",
    "DS_DOMAIN_PRIMARY",
    "DS_DOMAIN_NATIVE_MODE",
    "DS_DOMAIN_DIRECT_INBOUND",
    "DS_GFTI_UPDATE_TDO",
    "DS_GFTI_VALID_FLAGS",
    "DS_ONLY_DO_SITE_NAME",
    "DS_NOTIFY_AFTER_SITE_RECORDS",
    "CLSID_DsQuery",
    "CLSID_DsFindObjects",
    "CLSID_DsFindPeople",
    "CLSID_DsFindPrinter",
    "CLSID_DsFindComputer",
    "CLSID_DsFindVolume",
    "CLSID_DsFindContainer",
    "CLSID_DsFindAdvanced",
    "CLSID_DsFindDomainController",
    "CLSID_DsFindWriteableDomainController",
    "CLSID_DsFindFrsMembers",
    "DSQPF_NOSAVE",
    "DSQPF_SAVELOCATION",
    "DSQPF_SHOWHIDDENOBJECTS",
    "DSQPF_ENABLEADMINFEATURES",
    "DSQPF_ENABLEADVANCEDFEATURES",
    "DSQPF_HASCREDENTIALS",
    "DSQPF_NOCHOOSECOLUMNS",
    "DSQPM_GETCLASSLIST",
    "DSQPM_HELPTOPICS",
    "DSROLE_PRIMARY_DS_RUNNING",
    "DSROLE_PRIMARY_DS_MIXED_MODE",
    "DSROLE_UPGRADE_IN_PROGRESS",
    "DSROLE_PRIMARY_DS_READONLY",
    "DSROLE_PRIMARY_DOMAIN_GUID_PRESENT",
    "ADS_ATTR_CLEAR",
    "ADS_ATTR_UPDATE",
    "ADS_ATTR_APPEND",
    "ADS_ATTR_DELETE",
    "ADS_EXT_MINEXTDISPID",
    "ADS_EXT_MAXEXTDISPID",
    "ADS_EXT_INITCREDENTIALS",
    "ADS_EXT_INITIALIZE_COMPLETE",
    "DS_BEHAVIOR_WIN2000",
    "DS_BEHAVIOR_WIN2003_WITH_MIXED_DOMAINS",
    "DS_BEHAVIOR_WIN2003",
    "DS_BEHAVIOR_WIN2008",
    "DS_BEHAVIOR_WIN2008R2",
    "DS_BEHAVIOR_WIN2012",
    "DS_BEHAVIOR_WIN2012R2",
    "DS_BEHAVIOR_WIN2016",
    "DS_BEHAVIOR_LONGHORN",
    "DS_BEHAVIOR_WIN7",
    "DS_BEHAVIOR_WIN8",
    "DS_BEHAVIOR_WINBLUE",
    "DS_BEHAVIOR_WINTHRESHOLD",
    "ACTRL_DS_OPEN",
    "ACTRL_DS_CREATE_CHILD",
    "ACTRL_DS_DELETE_CHILD",
    "ACTRL_DS_LIST",
    "ACTRL_DS_SELF",
    "ACTRL_DS_READ_PROP",
    "ACTRL_DS_WRITE_PROP",
    "ACTRL_DS_DELETE_TREE",
    "ACTRL_DS_LIST_OBJECT",
    "ACTRL_DS_CONTROL_ACCESS",
    "NTDSAPI_BIND_ALLOW_DELEGATION",
    "NTDSAPI_BIND_FIND_BINDING",
    "NTDSAPI_BIND_FORCE_KERBEROS",
    "DS_REPSYNC_ASYNCHRONOUS_OPERATION",
    "DS_REPSYNC_WRITEABLE",
    "DS_REPSYNC_PERIODIC",
    "DS_REPSYNC_INTERSITE_MESSAGING",
    "DS_REPSYNC_FULL",
    "DS_REPSYNC_URGENT",
    "DS_REPSYNC_NO_DISCARD",
    "DS_REPSYNC_FORCE",
    "DS_REPSYNC_ADD_REFERENCE",
    "DS_REPSYNC_NEVER_COMPLETED",
    "DS_REPSYNC_TWO_WAY",
    "DS_REPSYNC_NEVER_NOTIFY",
    "DS_REPSYNC_INITIAL",
    "DS_REPSYNC_USE_COMPRESSION",
    "DS_REPSYNC_ABANDONED",
    "DS_REPSYNC_SELECT_SECRETS",
    "DS_REPSYNC_INITIAL_IN_PROGRESS",
    "DS_REPSYNC_PARTIAL_ATTRIBUTE_SET",
    "DS_REPSYNC_REQUEUE",
    "DS_REPSYNC_NOTIFICATION",
    "DS_REPSYNC_ASYNCHRONOUS_REPLICA",
    "DS_REPSYNC_CRITICAL",
    "DS_REPSYNC_FULL_IN_PROGRESS",
    "DS_REPSYNC_PREEMPTED",
    "DS_REPSYNC_NONGC_RO_REPLICA",
    "DS_REPADD_ASYNCHRONOUS_OPERATION",
    "DS_REPADD_WRITEABLE",
    "DS_REPADD_INITIAL",
    "DS_REPADD_PERIODIC",
    "DS_REPADD_INTERSITE_MESSAGING",
    "DS_REPADD_ASYNCHRONOUS_REPLICA",
    "DS_REPADD_DISABLE_NOTIFICATION",
    "DS_REPADD_DISABLE_PERIODIC",
    "DS_REPADD_USE_COMPRESSION",
    "DS_REPADD_NEVER_NOTIFY",
    "DS_REPADD_TWO_WAY",
    "DS_REPADD_CRITICAL",
    "DS_REPADD_SELECT_SECRETS",
    "DS_REPADD_NONGC_RO_REPLICA",
    "DS_REPDEL_ASYNCHRONOUS_OPERATION",
    "DS_REPDEL_WRITEABLE",
    "DS_REPDEL_INTERSITE_MESSAGING",
    "DS_REPDEL_IGNORE_ERRORS",
    "DS_REPDEL_LOCAL_ONLY",
    "DS_REPDEL_NO_SOURCE",
    "DS_REPDEL_REF_OK",
    "DS_REPMOD_ASYNCHRONOUS_OPERATION",
    "DS_REPMOD_WRITEABLE",
    "DS_REPMOD_UPDATE_FLAGS",
    "DS_REPMOD_UPDATE_INSTANCE",
    "DS_REPMOD_UPDATE_ADDRESS",
    "DS_REPMOD_UPDATE_SCHEDULE",
    "DS_REPMOD_UPDATE_RESULT",
    "DS_REPMOD_UPDATE_TRANSPORT",
    "DS_REPUPD_ASYNCHRONOUS_OPERATION",
    "DS_REPUPD_WRITEABLE",
    "DS_REPUPD_ADD_REFERENCE",
    "DS_REPUPD_DELETE_REFERENCE",
    "DS_REPUPD_REFERENCE_GCSPN",
    "DS_INSTANCETYPE_IS_NC_HEAD",
    "DS_INSTANCETYPE_NC_IS_WRITEABLE",
    "DS_INSTANCETYPE_NC_COMING",
    "DS_INSTANCETYPE_NC_GOING",
    "NTDSDSA_OPT_IS_GC",
    "NTDSDSA_OPT_DISABLE_INBOUND_REPL",
    "NTDSDSA_OPT_DISABLE_OUTBOUND_REPL",
    "NTDSDSA_OPT_DISABLE_NTDSCONN_XLATE",
    "NTDSDSA_OPT_DISABLE_SPN_REGISTRATION",
    "NTDSDSA_OPT_GENERATE_OWN_TOPO",
    "NTDSDSA_OPT_BLOCK_RPC",
    "NTDSCONN_OPT_IS_GENERATED",
    "NTDSCONN_OPT_TWOWAY_SYNC",
    "NTDSCONN_OPT_OVERRIDE_NOTIFY_DEFAULT",
    "NTDSCONN_OPT_USE_NOTIFY",
    "NTDSCONN_OPT_DISABLE_INTERSITE_COMPRESSION",
    "NTDSCONN_OPT_USER_OWNED_SCHEDULE",
    "NTDSCONN_OPT_RODC_TOPOLOGY",
    "NTDSCONN_KCC_NO_REASON",
    "NTDSCONN_KCC_GC_TOPOLOGY",
    "NTDSCONN_KCC_RING_TOPOLOGY",
    "NTDSCONN_KCC_MINIMIZE_HOPS_TOPOLOGY",
    "NTDSCONN_KCC_STALE_SERVERS_TOPOLOGY",
    "NTDSCONN_KCC_OSCILLATING_CONNECTION_TOPOLOGY",
    "NTDSCONN_KCC_INTERSITE_GC_TOPOLOGY",
    "NTDSCONN_KCC_INTERSITE_TOPOLOGY",
    "NTDSCONN_KCC_SERVER_FAILOVER_TOPOLOGY",
    "NTDSCONN_KCC_SITE_FAILOVER_TOPOLOGY",
    "NTDSCONN_KCC_REDUNDANT_SERVER_TOPOLOGY",
    "FRSCONN_PRIORITY_MASK",
    "FRSCONN_MAX_PRIORITY",
    "NTDSCONN_OPT_IGNORE_SCHEDULE_MASK",
    "NTDSSETTINGS_OPT_IS_AUTO_TOPOLOGY_DISABLED",
    "NTDSSETTINGS_OPT_IS_TOPL_CLEANUP_DISABLED",
    "NTDSSETTINGS_OPT_IS_TOPL_MIN_HOPS_DISABLED",
    "NTDSSETTINGS_OPT_IS_TOPL_DETECT_STALE_DISABLED",
    "NTDSSETTINGS_OPT_IS_INTER_SITE_AUTO_TOPOLOGY_DISABLED",
    "NTDSSETTINGS_OPT_IS_GROUP_CACHING_ENABLED",
    "NTDSSETTINGS_OPT_FORCE_KCC_WHISTLER_BEHAVIOR",
    "NTDSSETTINGS_OPT_FORCE_KCC_W2K_ELECTION",
    "NTDSSETTINGS_OPT_IS_RAND_BH_SELECTION_DISABLED",
    "NTDSSETTINGS_OPT_IS_SCHEDULE_HASHING_ENABLED",
    "NTDSSETTINGS_OPT_IS_REDUNDANT_SERVER_TOPOLOGY_ENABLED",
    "NTDSSETTINGS_OPT_W2K3_IGNORE_SCHEDULES",
    "NTDSSETTINGS_OPT_W2K3_BRIDGES_REQUIRED",
    "NTDSSETTINGS_DEFAULT_SERVER_REDUNDANCY",
    "NTDSTRANSPORT_OPT_IGNORE_SCHEDULES",
    "NTDSTRANSPORT_OPT_BRIDGES_REQUIRED",
    "NTDSSITECONN_OPT_USE_NOTIFY",
    "NTDSSITECONN_OPT_TWOWAY_SYNC",
    "NTDSSITECONN_OPT_DISABLE_COMPRESSION",
    "NTDSSITELINK_OPT_USE_NOTIFY",
    "NTDSSITELINK_OPT_TWOWAY_SYNC",
    "NTDSSITELINK_OPT_DISABLE_COMPRESSION",
    "DS_REPSYNCALL_NO_OPTIONS",
    "DS_REPSYNCALL_ABORT_IF_SERVER_UNAVAILABLE",
    "DS_REPSYNCALL_SYNC_ADJACENT_SERVERS_ONLY",
    "DS_REPSYNCALL_ID_SERVERS_BY_DN",
    "DS_REPSYNCALL_DO_NOT_SYNC",
    "DS_REPSYNCALL_SKIP_INITIAL_CHECK",
    "DS_REPSYNCALL_PUSH_CHANGES_OUTWARD",
    "DS_REPSYNCALL_CROSS_SITE_BOUNDARIES",
    "DS_LIST_DSA_OBJECT_FOR_SERVER",
    "DS_LIST_DNS_HOST_NAME_FOR_SERVER",
    "DS_LIST_ACCOUNT_OBJECT_FOR_SERVER",
    "DS_ROLE_SCHEMA_OWNER",
    "DS_ROLE_DOMAIN_OWNER",
    "DS_ROLE_PDC_OWNER",
    "DS_ROLE_RID_OWNER",
    "DS_ROLE_INFRASTRUCTURE_OWNER",
    "DS_SCHEMA_GUID_NOT_FOUND",
    "DS_SCHEMA_GUID_ATTR",
    "DS_SCHEMA_GUID_ATTR_SET",
    "DS_SCHEMA_GUID_CLASS",
    "DS_SCHEMA_GUID_CONTROL_RIGHT",
    "DS_KCC_FLAG_ASYNC_OP",
    "DS_KCC_FLAG_DAMPED",
    "DS_EXIST_ADVISORY_MODE",
    "DS_REPL_INFO_FLAG_IMPROVE_LINKED_ATTRS",
    "DS_REPL_NBR_WRITEABLE",
    "DS_REPL_NBR_SYNC_ON_STARTUP",
    "DS_REPL_NBR_DO_SCHEDULED_SYNCS",
    "DS_REPL_NBR_USE_ASYNC_INTERSITE_TRANSPORT",
    "DS_REPL_NBR_TWO_WAY_SYNC",
    "DS_REPL_NBR_NONGC_RO_REPLICA",
    "DS_REPL_NBR_RETURN_OBJECT_PARENTS",
    "DS_REPL_NBR_SELECT_SECRETS",
    "DS_REPL_NBR_FULL_SYNC_IN_PROGRESS",
    "DS_REPL_NBR_FULL_SYNC_NEXT_PACKET",
    "DS_REPL_NBR_GCSPN",
    "DS_REPL_NBR_NEVER_SYNCED",
    "DS_REPL_NBR_PREEMPTED",
    "DS_REPL_NBR_IGNORE_CHANGE_NOTIFICATIONS",
    "DS_REPL_NBR_DISABLE_SCHEDULED_SYNC",
    "DS_REPL_NBR_COMPRESS_CHANGES",
    "DS_REPL_NBR_NO_CHANGE_NOTIFICATIONS",
    "DS_REPL_NBR_PARTIAL_ATTRIBUTE_SET",
    "ADAM_REPL_AUTHENTICATION_MODE_NEGOTIATE_PASS_THROUGH",
    "ADAM_REPL_AUTHENTICATION_MODE_NEGOTIATE",
    "ADAM_REPL_AUTHENTICATION_MODE_MUTUAL_AUTH_REQUIRED",
    "FLAG_FOREST_OPTIONAL_FEATURE",
    "FLAG_DOMAIN_OPTIONAL_FEATURE",
    "FLAG_DISABLABLE_OPTIONAL_FEATURE",
    "FLAG_SERVER_OPTIONAL_FEATURE",
    "DSOP_SCOPE_TYPE_TARGET_COMPUTER",
    "DSOP_SCOPE_TYPE_UPLEVEL_JOINED_DOMAIN",
    "DSOP_SCOPE_TYPE_DOWNLEVEL_JOINED_DOMAIN",
    "DSOP_SCOPE_TYPE_ENTERPRISE_DOMAIN",
    "DSOP_SCOPE_TYPE_GLOBAL_CATALOG",
    "DSOP_SCOPE_TYPE_EXTERNAL_UPLEVEL_DOMAIN",
    "DSOP_SCOPE_TYPE_EXTERNAL_DOWNLEVEL_DOMAIN",
    "DSOP_SCOPE_TYPE_WORKGROUP",
    "DSOP_SCOPE_TYPE_USER_ENTERED_UPLEVEL_SCOPE",
    "DSOP_SCOPE_TYPE_USER_ENTERED_DOWNLEVEL_SCOPE",
    "DSOP_SCOPE_FLAG_STARTING_SCOPE",
    "DSOP_SCOPE_FLAG_WANT_PROVIDER_WINNT",
    "DSOP_SCOPE_FLAG_WANT_PROVIDER_LDAP",
    "DSOP_SCOPE_FLAG_WANT_PROVIDER_GC",
    "DSOP_SCOPE_FLAG_WANT_SID_PATH",
    "DSOP_SCOPE_FLAG_WANT_DOWNLEVEL_BUILTIN_PATH",
    "DSOP_SCOPE_FLAG_DEFAULT_FILTER_USERS",
    "DSOP_SCOPE_FLAG_DEFAULT_FILTER_GROUPS",
    "DSOP_SCOPE_FLAG_DEFAULT_FILTER_COMPUTERS",
    "DSOP_SCOPE_FLAG_DEFAULT_FILTER_CONTACTS",
    "DSOP_SCOPE_FLAG_DEFAULT_FILTER_SERVICE_ACCOUNTS",
    "DSOP_SCOPE_FLAG_DEFAULT_FILTER_PASSWORDSETTINGS_OBJECTS",
    "DSOP_FILTER_INCLUDE_ADVANCED_VIEW",
    "DSOP_FILTER_USERS",
    "DSOP_FILTER_BUILTIN_GROUPS",
    "DSOP_FILTER_WELL_KNOWN_PRINCIPALS",
    "DSOP_FILTER_UNIVERSAL_GROUPS_DL",
    "DSOP_FILTER_UNIVERSAL_GROUPS_SE",
    "DSOP_FILTER_GLOBAL_GROUPS_DL",
    "DSOP_FILTER_GLOBAL_GROUPS_SE",
    "DSOP_FILTER_DOMAIN_LOCAL_GROUPS_DL",
    "DSOP_FILTER_DOMAIN_LOCAL_GROUPS_SE",
    "DSOP_FILTER_CONTACTS",
    "DSOP_FILTER_COMPUTERS",
    "DSOP_FILTER_SERVICE_ACCOUNTS",
    "DSOP_FILTER_PASSWORDSETTINGS_OBJECTS",
    "DSOP_DOWNLEVEL_FILTER_USERS",
    "DSOP_DOWNLEVEL_FILTER_LOCAL_GROUPS",
    "DSOP_DOWNLEVEL_FILTER_GLOBAL_GROUPS",
    "DSOP_DOWNLEVEL_FILTER_COMPUTERS",
    "DSOP_DOWNLEVEL_FILTER_WORLD",
    "DSOP_DOWNLEVEL_FILTER_AUTHENTICATED_USER",
    "DSOP_DOWNLEVEL_FILTER_ANONYMOUS",
    "DSOP_DOWNLEVEL_FILTER_BATCH",
    "DSOP_DOWNLEVEL_FILTER_CREATOR_OWNER",
    "DSOP_DOWNLEVEL_FILTER_CREATOR_GROUP",
    "DSOP_DOWNLEVEL_FILTER_DIALUP",
    "DSOP_DOWNLEVEL_FILTER_INTERACTIVE",
    "DSOP_DOWNLEVEL_FILTER_NETWORK",
    "DSOP_DOWNLEVEL_FILTER_SERVICE",
    "DSOP_DOWNLEVEL_FILTER_SYSTEM",
    "DSOP_DOWNLEVEL_FILTER_EXCLUDE_BUILTIN_GROUPS",
    "DSOP_DOWNLEVEL_FILTER_TERMINAL_SERVER",
    "DSOP_DOWNLEVEL_FILTER_ALL_WELLKNOWN_SIDS",
    "DSOP_DOWNLEVEL_FILTER_LOCAL_SERVICE",
    "DSOP_DOWNLEVEL_FILTER_NETWORK_SERVICE",
    "DSOP_DOWNLEVEL_FILTER_REMOTE_LOGON",
    "DSOP_DOWNLEVEL_FILTER_INTERNET_USER",
    "DSOP_DOWNLEVEL_FILTER_OWNER_RIGHTS",
    "DSOP_DOWNLEVEL_FILTER_SERVICES",
    "DSOP_DOWNLEVEL_FILTER_LOCAL_LOGON",
    "DSOP_DOWNLEVEL_FILTER_THIS_ORG_CERT",
    "DSOP_DOWNLEVEL_FILTER_IIS_APP_POOL",
    "DSOP_DOWNLEVEL_FILTER_ALL_APP_PACKAGES",
    "DSOP_DOWNLEVEL_FILTER_LOCAL_ACCOUNTS",
    "DSOP_FLAG_MULTISELECT",
    "DSOP_FLAG_SKIP_TARGET_COMPUTER_DC_CHECK",
    "SCHEDULE_INTERVAL",
    "SCHEDULE_BANDWIDTH",
    "SCHEDULE_PRIORITY",
    "FACILITY_NTDSB",
    "FACILITY_BACKUP",
    "FACILITY_SYSTEM",
    "STATUS_SEVERITY_SUCCESS",
    "STATUS_SEVERITY_INFORMATIONAL",
    "STATUS_SEVERITY_WARNING",
    "STATUS_SEVERITY_ERROR",
    "CLSID_DsObjectPicker",
    "CQFORM",
    "LPCQADDFORMSPROC",
    "LPCQADDPAGESPROC",
    "LPCQPAGEPROC",
    "CQPAGE",
    "IQueryForm",
    "IPersistQuery",
    "OPENQUERYWINDOW",
    "ICommonQuery",
    "PropertyEntry",
    "PropertyValue",
    "AccessControlEntry",
    "AccessControlList",
    "SecurityDescriptor",
    "LargeInteger",
    "NameTranslate",
    "CaseIgnoreList",
    "FaxNumber",
    "NetAddress",
    "OctetList",
    "Email",
    "Path",
    "ReplicaPointer",
    "Timestamp",
    "PostalAddress",
    "BackLink",
    "TypedName",
    "Hold",
    "Pathname",
    "ADSystemInfo",
    "WinNTSystemInfo",
    "DNWithBinary",
    "DNWithString",
    "ADsSecurityUtility",
    "ADSTYPEENUM",
    "ADSTYPE_INVALID",
    "ADSTYPE_DN_STRING",
    "ADSTYPE_CASE_EXACT_STRING",
    "ADSTYPE_CASE_IGNORE_STRING",
    "ADSTYPE_PRINTABLE_STRING",
    "ADSTYPE_NUMERIC_STRING",
    "ADSTYPE_BOOLEAN",
    "ADSTYPE_INTEGER",
    "ADSTYPE_OCTET_STRING",
    "ADSTYPE_UTC_TIME",
    "ADSTYPE_LARGE_INTEGER",
    "ADSTYPE_PROV_SPECIFIC",
    "ADSTYPE_OBJECT_CLASS",
    "ADSTYPE_CASEIGNORE_LIST",
    "ADSTYPE_OCTET_LIST",
    "ADSTYPE_PATH",
    "ADSTYPE_POSTALADDRESS",
    "ADSTYPE_TIMESTAMP",
    "ADSTYPE_BACKLINK",
    "ADSTYPE_TYPEDNAME",
    "ADSTYPE_HOLD",
    "ADSTYPE_NETADDRESS",
    "ADSTYPE_REPLICAPOINTER",
    "ADSTYPE_FAXNUMBER",
    "ADSTYPE_EMAIL",
    "ADSTYPE_NT_SECURITY_DESCRIPTOR",
    "ADSTYPE_UNKNOWN",
    "ADSTYPE_DN_WITH_BINARY",
    "ADSTYPE_DN_WITH_STRING",
    "ADS_OCTET_STRING",
    "ADS_NT_SECURITY_DESCRIPTOR",
    "ADS_PROV_SPECIFIC",
    "ADS_CASEIGNORE_LIST",
    "ADS_OCTET_LIST",
    "ADS_PATH",
    "ADS_POSTALADDRESS",
    "ADS_TIMESTAMP",
    "ADS_BACKLINK",
    "ADS_TYPEDNAME",
    "ADS_HOLD",
    "ADS_NETADDRESS",
    "ADS_REPLICAPOINTER",
    "ADS_FAXNUMBER",
    "ADS_EMAIL",
    "ADS_DN_WITH_BINARY",
    "ADS_DN_WITH_STRING",
    "ADSVALUE",
    "ADS_ATTR_INFO",
    "ADS_AUTHENTICATION_ENUM",
    "ADS_SECURE_AUTHENTICATION",
    "ADS_USE_ENCRYPTION",
    "ADS_USE_SSL",
    "ADS_READONLY_SERVER",
    "ADS_PROMPT_CREDENTIALS",
    "ADS_NO_AUTHENTICATION",
    "ADS_FAST_BIND",
    "ADS_USE_SIGNING",
    "ADS_USE_SEALING",
    "ADS_USE_DELEGATION",
    "ADS_SERVER_BIND",
    "ADS_NO_REFERRAL_CHASING",
    "ADS_AUTH_RESERVED",
    "ADS_OBJECT_INFO",
    "ADS_STATUSENUM",
    "ADS_STATUS_S_OK",
    "ADS_STATUS_INVALID_SEARCHPREF",
    "ADS_STATUS_INVALID_SEARCHPREFVALUE",
    "ADS_DEREFENUM",
    "ADS_DEREF_NEVER",
    "ADS_DEREF_SEARCHING",
    "ADS_DEREF_FINDING",
    "ADS_DEREF_ALWAYS",
    "ADS_SCOPEENUM",
    "ADS_SCOPE_BASE",
    "ADS_SCOPE_ONELEVEL",
    "ADS_SCOPE_SUBTREE",
    "ADS_PREFERENCES_ENUM",
    "ADSIPROP_ASYNCHRONOUS",
    "ADSIPROP_DEREF_ALIASES",
    "ADSIPROP_SIZE_LIMIT",
    "ADSIPROP_TIME_LIMIT",
    "ADSIPROP_ATTRIBTYPES_ONLY",
    "ADSIPROP_SEARCH_SCOPE",
    "ADSIPROP_TIMEOUT",
    "ADSIPROP_PAGESIZE",
    "ADSIPROP_PAGED_TIME_LIMIT",
    "ADSIPROP_CHASE_REFERRALS",
    "ADSIPROP_SORT_ON",
    "ADSIPROP_CACHE_RESULTS",
    "ADSIPROP_ADSIFLAG",
    "ADSI_DIALECT_ENUM",
    "ADSI_DIALECT_LDAP",
    "ADSI_DIALECT_SQL",
    "ADS_CHASE_REFERRALS_ENUM",
    "ADS_CHASE_REFERRALS_NEVER",
    "ADS_CHASE_REFERRALS_SUBORDINATE",
    "ADS_CHASE_REFERRALS_EXTERNAL",
    "ADS_CHASE_REFERRALS_ALWAYS",
    "ADS_SEARCHPREF_ENUM",
    "ADS_SEARCHPREF_ASYNCHRONOUS",
    "ADS_SEARCHPREF_DEREF_ALIASES",
    "ADS_SEARCHPREF_SIZE_LIMIT",
    "ADS_SEARCHPREF_TIME_LIMIT",
    "ADS_SEARCHPREF_ATTRIBTYPES_ONLY",
    "ADS_SEARCHPREF_SEARCH_SCOPE",
    "ADS_SEARCHPREF_TIMEOUT",
    "ADS_SEARCHPREF_PAGESIZE",
    "ADS_SEARCHPREF_PAGED_TIME_LIMIT",
    "ADS_SEARCHPREF_CHASE_REFERRALS",
    "ADS_SEARCHPREF_SORT_ON",
    "ADS_SEARCHPREF_CACHE_RESULTS",
    "ADS_SEARCHPREF_DIRSYNC",
    "ADS_SEARCHPREF_TOMBSTONE",
    "ADS_SEARCHPREF_VLV",
    "ADS_SEARCHPREF_ATTRIBUTE_QUERY",
    "ADS_SEARCHPREF_SECURITY_MASK",
    "ADS_SEARCHPREF_DIRSYNC_FLAG",
    "ADS_SEARCHPREF_EXTENDED_DN",
    "ADS_PASSWORD_ENCODING_ENUM",
    "ADS_PASSWORD_ENCODE_REQUIRE_SSL",
    "ADS_PASSWORD_ENCODE_CLEAR",
    "ads_searchpref_info",
    "ads_search_column",
    "ADS_ATTR_DEF",
    "ADS_CLASS_DEF",
    "ADS_SORTKEY",
    "ADS_VLV",
    "ADS_PROPERTY_OPERATION_ENUM",
    "ADS_PROPERTY_CLEAR",
    "ADS_PROPERTY_UPDATE",
    "ADS_PROPERTY_APPEND",
    "ADS_PROPERTY_DELETE",
    "ADS_SYSTEMFLAG_ENUM",
    "ADS_SYSTEMFLAG_DISALLOW_DELETE",
    "ADS_SYSTEMFLAG_CONFIG_ALLOW_RENAME",
    "ADS_SYSTEMFLAG_CONFIG_ALLOW_MOVE",
    "ADS_SYSTEMFLAG_CONFIG_ALLOW_LIMITED_MOVE",
    "ADS_SYSTEMFLAG_DOMAIN_DISALLOW_RENAME",
    "ADS_SYSTEMFLAG_DOMAIN_DISALLOW_MOVE",
    "ADS_SYSTEMFLAG_CR_NTDS_NC",
    "ADS_SYSTEMFLAG_CR_NTDS_DOMAIN",
    "ADS_SYSTEMFLAG_ATTR_NOT_REPLICATED",
    "ADS_SYSTEMFLAG_ATTR_IS_CONSTRUCTED",
    "ADS_GROUP_TYPE_ENUM",
    "ADS_GROUP_TYPE_GLOBAL_GROUP",
    "ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP",
    "ADS_GROUP_TYPE_LOCAL_GROUP",
    "ADS_GROUP_TYPE_UNIVERSAL_GROUP",
    "ADS_GROUP_TYPE_SECURITY_ENABLED",
    "ADS_USER_FLAG_ENUM",
    "ADS_UF_SCRIPT",
    "ADS_UF_ACCOUNTDISABLE",
    "ADS_UF_HOMEDIR_REQUIRED",
    "ADS_UF_LOCKOUT",
    "ADS_UF_PASSWD_NOTREQD",
    "ADS_UF_PASSWD_CANT_CHANGE",
    "ADS_UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED",
    "ADS_UF_TEMP_DUPLICATE_ACCOUNT",
    "ADS_UF_NORMAL_ACCOUNT",
    "ADS_UF_INTERDOMAIN_TRUST_ACCOUNT",
    "ADS_UF_WORKSTATION_TRUST_ACCOUNT",
    "ADS_UF_SERVER_TRUST_ACCOUNT",
    "ADS_UF_DONT_EXPIRE_PASSWD",
    "ADS_UF_MNS_LOGON_ACCOUNT",
    "ADS_UF_SMARTCARD_REQUIRED",
    "ADS_UF_TRUSTED_FOR_DELEGATION",
    "ADS_UF_NOT_DELEGATED",
    "ADS_UF_USE_DES_KEY_ONLY",
    "ADS_UF_DONT_REQUIRE_PREAUTH",
    "ADS_UF_PASSWORD_EXPIRED",
    "ADS_UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION",
    "ADS_RIGHTS_ENUM",
    "ADS_RIGHT_DELETE",
    "ADS_RIGHT_READ_CONTROL",
    "ADS_RIGHT_WRITE_DAC",
    "ADS_RIGHT_WRITE_OWNER",
    "ADS_RIGHT_SYNCHRONIZE",
    "ADS_RIGHT_ACCESS_SYSTEM_SECURITY",
    "ADS_RIGHT_GENERIC_READ",
    "ADS_RIGHT_GENERIC_WRITE",
    "ADS_RIGHT_GENERIC_EXECUTE",
    "ADS_RIGHT_GENERIC_ALL",
    "ADS_RIGHT_DS_CREATE_CHILD",
    "ADS_RIGHT_DS_DELETE_CHILD",
    "ADS_RIGHT_ACTRL_DS_LIST",
    "ADS_RIGHT_DS_SELF",
    "ADS_RIGHT_DS_READ_PROP",
    "ADS_RIGHT_DS_WRITE_PROP",
    "ADS_RIGHT_DS_DELETE_TREE",
    "ADS_RIGHT_DS_LIST_OBJECT",
    "ADS_RIGHT_DS_CONTROL_ACCESS",
    "ADS_ACETYPE_ENUM",
    "ADS_ACETYPE_ACCESS_ALLOWED",
    "ADS_ACETYPE_ACCESS_DENIED",
    "ADS_ACETYPE_SYSTEM_AUDIT",
    "ADS_ACETYPE_ACCESS_ALLOWED_OBJECT",
    "ADS_ACETYPE_ACCESS_DENIED_OBJECT",
    "ADS_ACETYPE_SYSTEM_AUDIT_OBJECT",
    "ADS_ACETYPE_SYSTEM_ALARM_OBJECT",
    "ADS_ACETYPE_ACCESS_ALLOWED_CALLBACK",
    "ADS_ACETYPE_ACCESS_DENIED_CALLBACK",
    "ADS_ACETYPE_ACCESS_ALLOWED_CALLBACK_OBJECT",
    "ADS_ACETYPE_ACCESS_DENIED_CALLBACK_OBJECT",
    "ADS_ACETYPE_SYSTEM_AUDIT_CALLBACK",
    "ADS_ACETYPE_SYSTEM_ALARM_CALLBACK",
    "ADS_ACETYPE_SYSTEM_AUDIT_CALLBACK_OBJECT",
    "ADS_ACETYPE_SYSTEM_ALARM_CALLBACK_OBJECT",
    "ADS_ACEFLAG_ENUM",
    "ADS_ACEFLAG_INHERIT_ACE",
    "ADS_ACEFLAG_NO_PROPAGATE_INHERIT_ACE",
    "ADS_ACEFLAG_INHERIT_ONLY_ACE",
    "ADS_ACEFLAG_INHERITED_ACE",
    "ADS_ACEFLAG_VALID_INHERIT_FLAGS",
    "ADS_ACEFLAG_SUCCESSFUL_ACCESS",
    "ADS_ACEFLAG_FAILED_ACCESS",
    "ADS_FLAGTYPE_ENUM",
    "ADS_FLAG_OBJECT_TYPE_PRESENT",
    "ADS_FLAG_INHERITED_OBJECT_TYPE_PRESENT",
    "ADS_SD_CONTROL_ENUM",
    "ADS_SD_CONTROL_SE_OWNER_DEFAULTED",
    "ADS_SD_CONTROL_SE_GROUP_DEFAULTED",
    "ADS_SD_CONTROL_SE_DACL_PRESENT",
    "ADS_SD_CONTROL_SE_DACL_DEFAULTED",
    "ADS_SD_CONTROL_SE_SACL_PRESENT",
    "ADS_SD_CONTROL_SE_SACL_DEFAULTED",
    "ADS_SD_CONTROL_SE_DACL_AUTO_INHERIT_REQ",
    "ADS_SD_CONTROL_SE_SACL_AUTO_INHERIT_REQ",
    "ADS_SD_CONTROL_SE_DACL_AUTO_INHERITED",
    "ADS_SD_CONTROL_SE_SACL_AUTO_INHERITED",
    "ADS_SD_CONTROL_SE_DACL_PROTECTED",
    "ADS_SD_CONTROL_SE_SACL_PROTECTED",
    "ADS_SD_CONTROL_SE_SELF_RELATIVE",
    "ADS_SD_REVISION_ENUM",
    "ADS_SD_REVISION_DS",
    "ADS_NAME_TYPE_ENUM",
    "ADS_NAME_TYPE_1779",
    "ADS_NAME_TYPE_CANONICAL",
    "ADS_NAME_TYPE_NT4",
    "ADS_NAME_TYPE_DISPLAY",
    "ADS_NAME_TYPE_DOMAIN_SIMPLE",
    "ADS_NAME_TYPE_ENTERPRISE_SIMPLE",
    "ADS_NAME_TYPE_GUID",
    "ADS_NAME_TYPE_UNKNOWN",
    "ADS_NAME_TYPE_USER_PRINCIPAL_NAME",
    "ADS_NAME_TYPE_CANONICAL_EX",
    "ADS_NAME_TYPE_SERVICE_PRINCIPAL_NAME",
    "ADS_NAME_TYPE_SID_OR_SID_HISTORY_NAME",
    "ADS_NAME_INITTYPE_ENUM",
    "ADS_NAME_INITTYPE_DOMAIN",
    "ADS_NAME_INITTYPE_SERVER",
    "ADS_NAME_INITTYPE_GC",
    "ADS_OPTION_ENUM",
    "ADS_OPTION_SERVERNAME",
    "ADS_OPTION_REFERRALS",
    "ADS_OPTION_PAGE_SIZE",
    "ADS_OPTION_SECURITY_MASK",
    "ADS_OPTION_MUTUAL_AUTH_STATUS",
    "ADS_OPTION_QUOTA",
    "ADS_OPTION_PASSWORD_PORTNUMBER",
    "ADS_OPTION_PASSWORD_METHOD",
    "ADS_OPTION_ACCUMULATIVE_MODIFICATION",
    "ADS_OPTION_SKIP_SID_LOOKUP",
    "ADS_SECURITY_INFO_ENUM",
    "ADS_SECURITY_INFO_OWNER",
    "ADS_SECURITY_INFO_GROUP",
    "ADS_SECURITY_INFO_DACL",
    "ADS_SECURITY_INFO_SACL",
    "ADS_SETTYPE_ENUM",
    "ADS_SETTYPE_FULL",
    "ADS_SETTYPE_PROVIDER",
    "ADS_SETTYPE_SERVER",
    "ADS_SETTYPE_DN",
    "ADS_FORMAT_ENUM",
    "ADS_FORMAT_WINDOWS",
    "ADS_FORMAT_WINDOWS_NO_SERVER",
    "ADS_FORMAT_WINDOWS_DN",
    "ADS_FORMAT_WINDOWS_PARENT",
    "ADS_FORMAT_X500",
    "ADS_FORMAT_X500_NO_SERVER",
    "ADS_FORMAT_X500_DN",
    "ADS_FORMAT_X500_PARENT",
    "ADS_FORMAT_SERVER",
    "ADS_FORMAT_PROVIDER",
    "ADS_FORMAT_LEAF",
    "ADS_DISPLAY_ENUM",
    "ADS_DISPLAY_FULL",
    "ADS_DISPLAY_VALUE_ONLY",
    "ADS_ESCAPE_MODE_ENUM",
    "ADS_ESCAPEDMODE_DEFAULT",
    "ADS_ESCAPEDMODE_ON",
    "ADS_ESCAPEDMODE_OFF",
    "ADS_ESCAPEDMODE_OFF_EX",
    "ADS_PATHTYPE_ENUM",
    "ADS_PATH_FILE",
    "ADS_PATH_FILESHARE",
    "ADS_PATH_REGISTRY",
    "ADS_SD_FORMAT_ENUM",
    "ADS_SD_FORMAT_IID",
    "ADS_SD_FORMAT_RAW",
    "ADS_SD_FORMAT_HEXSTRING",
    "IADs",
    "IADsContainer",
    "IADsCollection",
    "IADsMembers",
    "IADsPropertyList",
    "IADsPropertyEntry",
    "IADsPropertyValue",
    "IADsPropertyValue2",
    "IPrivateDispatch",
    "IPrivateUnknown",
    "IADsExtension",
    "IADsDeleteOps",
    "IADsNamespaces",
    "IADsClass",
    "IADsProperty",
    "IADsSyntax",
    "IADsLocality",
    "IADsO",
    "IADsOU",
    "IADsDomain",
    "IADsComputer",
    "IADsComputerOperations",
    "IADsGroup",
    "IADsUser",
    "IADsPrintQueue",
    "IADsPrintQueueOperations",
    "IADsPrintJob",
    "IADsPrintJobOperations",
    "IADsService",
    "IADsServiceOperations",
    "IADsFileService",
    "IADsFileServiceOperations",
    "IADsFileShare",
    "IADsSession",
    "IADsResource",
    "IADsOpenDSObject",
    "IDirectoryObject",
    "IDirectorySearch",
    "IDirectorySchemaMgmt",
    "IADsAggregatee",
    "IADsAggregator",
    "IADsAccessControlEntry",
    "IADsAccessControlList",
    "IADsSecurityDescriptor",
    "IADsLargeInteger",
    "IADsNameTranslate",
    "IADsCaseIgnoreList",
    "IADsFaxNumber",
    "IADsNetAddress",
    "IADsOctetList",
    "IADsEmail",
    "IADsPath",
    "IADsReplicaPointer",
    "IADsAcl",
    "IADsTimestamp",
    "IADsPostalAddress",
    "IADsBackLink",
    "IADsTypedName",
    "IADsHold",
    "IADsObjectOptions",
    "IADsPathname",
    "IADsADSystemInfo",
    "IADsWinNTSystemInfo",
    "IADsDNWithBinary",
    "IADsDNWithString",
    "IADsSecurityUtility",
    "DSOBJECT",
    "DSOBJECTNAMES",
    "DSDISPLAYSPECOPTIONS",
    "DSPROPERTYPAGEINFO",
    "DOMAINDESC",
    "DOMAIN_TREE",
    "IDsBrowseDomainTree",
    "LPDSENUMATTRIBUTES",
    "DSCLASSCREATIONINFO",
    "IDsDisplaySpecifier",
    "DSBROWSEINFOW",
    "DSBROWSEINFOA",
    "DSBITEMW",
    "DSBITEMA",
    "DSOP_UPLEVEL_FILTER_FLAGS",
    "DSOP_FILTER_FLAGS",
    "DSOP_SCOPE_INIT_INFO",
    "DSOP_INIT_INFO",
    "DS_SELECTION",
    "DS_SELECTION_LIST",
    "IDsObjectPicker",
    "IDsObjectPickerCredentials",
    "DSQUERYINITPARAMS",
    "DSCOLUMN",
    "DSQUERYPARAMS",
    "DSQUERYCLASSLIST",
    "IDsAdminCreateObj",
    "IDsAdminNewObj",
    "IDsAdminNewObjPrimarySite",
    "DSA_NEWOBJ_DISPINFO",
    "IDsAdminNewObjExt",
    "IDsAdminNotifyHandler",
    "ADSPROPINITPARAMS",
    "ADSPROPERROR",
    "SCHEDULE_HEADER",
    "SCHEDULE",
    "DS_MANGLE_FOR",
    "DS_MANGLE_UNKNOWN",
    "DS_MANGLE_OBJECT_RDN_FOR_DELETION",
    "DS_MANGLE_OBJECT_RDN_FOR_NAME_CONFLICT",
    "DS_NAME_FORMAT",
    "DS_UNKNOWN_NAME",
    "DS_FQDN_1779_NAME",
    "DS_NT4_ACCOUNT_NAME",
    "DS_DISPLAY_NAME",
    "DS_UNIQUE_ID_NAME",
    "DS_CANONICAL_NAME",
    "DS_USER_PRINCIPAL_NAME",
    "DS_CANONICAL_NAME_EX",
    "DS_SERVICE_PRINCIPAL_NAME",
    "DS_SID_OR_SID_HISTORY_NAME",
    "DS_DNS_DOMAIN_NAME",
    "DS_NAME_FLAGS",
    "DS_NAME_NO_FLAGS",
    "DS_NAME_FLAG_SYNTACTICAL_ONLY",
    "DS_NAME_FLAG_EVAL_AT_DC",
    "DS_NAME_FLAG_GCVERIFY",
    "DS_NAME_FLAG_TRUST_REFERRAL",
    "DS_NAME_ERROR",
    "DS_NAME_NO_ERROR",
    "DS_NAME_ERROR_RESOLVING",
    "DS_NAME_ERROR_NOT_FOUND",
    "DS_NAME_ERROR_NOT_UNIQUE",
    "DS_NAME_ERROR_NO_MAPPING",
    "DS_NAME_ERROR_DOMAIN_ONLY",
    "DS_NAME_ERROR_NO_SYNTACTICAL_MAPPING",
    "DS_NAME_ERROR_TRUST_REFERRAL",
    "DS_SPN_NAME_TYPE",
    "DS_SPN_DNS_HOST",
    "DS_SPN_DN_HOST",
    "DS_SPN_NB_HOST",
    "DS_SPN_DOMAIN",
    "DS_SPN_NB_DOMAIN",
    "DS_SPN_SERVICE",
    "DS_SPN_WRITE_OP",
    "DS_SPN_ADD_SPN_OP",
    "DS_SPN_REPLACE_SPN_OP",
    "DS_SPN_DELETE_SPN_OP",
    "DS_NAME_RESULT_ITEMA",
    "DS_NAME_RESULTA",
    "DS_NAME_RESULT_ITEMW",
    "DS_NAME_RESULTW",
    "DS_REPSYNCALL_ERROR",
    "DS_REPSYNCALL_WIN32_ERROR_CONTACTING_SERVER",
    "DS_REPSYNCALL_WIN32_ERROR_REPLICATING",
    "DS_REPSYNCALL_SERVER_UNREACHABLE",
    "DS_REPSYNCALL_EVENT",
    "DS_REPSYNCALL_EVENT_ERROR",
    "DS_REPSYNCALL_EVENT_SYNC_STARTED",
    "DS_REPSYNCALL_EVENT_SYNC_COMPLETED",
    "DS_REPSYNCALL_EVENT_FINISHED",
    "DS_REPSYNCALL_SYNCA",
    "DS_REPSYNCALL_SYNCW",
    "DS_REPSYNCALL_ERRINFOA",
    "DS_REPSYNCALL_ERRINFOW",
    "DS_REPSYNCALL_UPDATEA",
    "DS_REPSYNCALL_UPDATEW",
    "DS_SITE_COST_INFO",
    "DS_SCHEMA_GUID_MAPA",
    "DS_SCHEMA_GUID_MAPW",
    "DS_DOMAIN_CONTROLLER_INFO_1A",
    "DS_DOMAIN_CONTROLLER_INFO_1W",
    "DS_DOMAIN_CONTROLLER_INFO_2A",
    "DS_DOMAIN_CONTROLLER_INFO_2W",
    "DS_DOMAIN_CONTROLLER_INFO_3A",
    "DS_DOMAIN_CONTROLLER_INFO_3W",
    "DS_KCC_TASKID",
    "DS_KCC_TASKID_UPDATE_TOPOLOGY",
    "DS_REPL_INFO_TYPE",
    "DS_REPL_INFO_NEIGHBORS",
    "DS_REPL_INFO_CURSORS_FOR_NC",
    "DS_REPL_INFO_METADATA_FOR_OBJ",
    "DS_REPL_INFO_KCC_DSA_CONNECT_FAILURES",
    "DS_REPL_INFO_KCC_DSA_LINK_FAILURES",
    "DS_REPL_INFO_PENDING_OPS",
    "DS_REPL_INFO_METADATA_FOR_ATTR_VALUE",
    "DS_REPL_INFO_CURSORS_2_FOR_NC",
    "DS_REPL_INFO_CURSORS_3_FOR_NC",
    "DS_REPL_INFO_METADATA_2_FOR_OBJ",
    "DS_REPL_INFO_METADATA_2_FOR_ATTR_VALUE",
    "DS_REPL_INFO_METADATA_EXT_FOR_ATTR_VALUE",
    "DS_REPL_INFO_TYPE_MAX",
    "DS_REPL_NEIGHBORW",
    "DS_REPL_NEIGHBORW_BLOB",
    "DS_REPL_NEIGHBORSW",
    "DS_REPL_CURSOR",
    "DS_REPL_CURSOR_2",
    "DS_REPL_CURSOR_3W",
    "DS_REPL_CURSOR_BLOB",
    "DS_REPL_CURSORS",
    "DS_REPL_CURSORS_2",
    "DS_REPL_CURSORS_3W",
    "DS_REPL_ATTR_META_DATA",
    "DS_REPL_ATTR_META_DATA_2",
    "DS_REPL_ATTR_META_DATA_BLOB",
    "DS_REPL_OBJ_META_DATA",
    "DS_REPL_OBJ_META_DATA_2",
    "DS_REPL_KCC_DSA_FAILUREW",
    "DS_REPL_KCC_DSA_FAILUREW_BLOB",
    "DS_REPL_KCC_DSA_FAILURESW",
    "DS_REPL_OP_TYPE",
    "DS_REPL_OP_TYPE_SYNC",
    "DS_REPL_OP_TYPE_ADD",
    "DS_REPL_OP_TYPE_DELETE",
    "DS_REPL_OP_TYPE_MODIFY",
    "DS_REPL_OP_TYPE_UPDATE_REFS",
    "DS_REPL_OPW",
    "DS_REPL_OPW_BLOB",
    "DS_REPL_PENDING_OPSW",
    "DS_REPL_VALUE_META_DATA",
    "DS_REPL_VALUE_META_DATA_2",
    "DS_REPL_VALUE_META_DATA_EXT",
    "DS_REPL_VALUE_META_DATA_BLOB",
    "DS_REPL_VALUE_META_DATA_BLOB_EXT",
    "DS_REPL_ATTR_VALUE_META_DATA",
    "DS_REPL_ATTR_VALUE_META_DATA_2",
    "DS_REPL_ATTR_VALUE_META_DATA_EXT",
    "DS_REPL_QUEUE_STATISTICSW",
    "DSROLE_MACHINE_ROLE",
    "DsRole_RoleStandaloneWorkstation",
    "DsRole_RoleMemberWorkstation",
    "DsRole_RoleStandaloneServer",
    "DsRole_RoleMemberServer",
    "DsRole_RoleBackupDomainController",
    "DsRole_RolePrimaryDomainController",
    "DSROLE_SERVER_STATE",
    "DSROLE_SERVER_STATE_DsRoleServerUnknown",
    "DSROLE_SERVER_STATE_DsRoleServerPrimary",
    "DSROLE_SERVER_STATE_DsRoleServerBackup",
    "DSROLE_PRIMARY_DOMAIN_INFO_LEVEL",
    "DSROLE_PRIMARY_DOMAIN_INFO_LEVEL_DsRolePrimaryDomainInfoBasic",
    "DSROLE_PRIMARY_DOMAIN_INFO_LEVEL_DsRoleUpgradeStatus",
    "DSROLE_PRIMARY_DOMAIN_INFO_LEVEL_DsRoleOperationState",
    "DSROLE_PRIMARY_DOMAIN_INFO_BASIC",
    "DSROLE_UPGRADE_STATUS_INFO",
    "DSROLE_OPERATION_STATE",
    "DSROLE_OPERATION_STATE_DsRoleOperationIdle",
    "DSROLE_OPERATION_STATE_DsRoleOperationActive",
    "DSROLE_OPERATION_STATE_DsRoleOperationNeedReboot",
    "DSROLE_OPERATION_STATE_INFO",
    "DOMAIN_CONTROLLER_INFOA",
    "DOMAIN_CONTROLLER_INFOW",
    "DS_DOMAIN_TRUSTSW",
    "DS_DOMAIN_TRUSTSA",
    "GetDcContextHandle",
    "ADsGetObject",
    "ADsBuildEnumerator",
    "ADsFreeEnumerator",
    "ADsEnumerateNext",
    "ADsBuildVarArrayStr",
    "ADsBuildVarArrayInt",
    "ADsOpenObject",
    "ADsGetLastError",
    "ADsSetLastError",
    "AllocADsMem",
    "FreeADsMem",
    "ReallocADsMem",
    "AllocADsStr",
    "FreeADsStr",
    "ReallocADsStr",
    "ADsEncodeBinaryData",
    "ADsDecodeBinaryData",
    "PropVariantToAdsType",
    "AdsTypeToPropVariant",
    "AdsFreeAdsValues",
    "BinarySDToSecurityDescriptor",
    "SecurityDescriptorToBinarySD",
    "DsBrowseForContainerW",
    "DsBrowseForContainer",
    "DsBrowseForContainerA",
    "DsGetIcon",
    "DsGetFriendlyClassName",
    "ADsPropCreateNotifyObj",
    "ADsPropGetInitInfo",
    "ADsPropSetHwndWithTitle",
    "ADsPropSetHwnd",
    "ADsPropCheckIfWritable",
    "ADsPropSendErrorMessage",
    "ADsPropShowErrorDialog",
    "DsMakeSpnW",
    "DsMakeSpn",
    "DsMakeSpnA",
    "DsCrackSpnA",
    "DsCrackSpnW",
    "DsCrackSpn",
    "DsQuoteRdnValueW",
    "DsQuoteRdnValue",
    "DsQuoteRdnValueA",
    "DsUnquoteRdnValueW",
    "DsUnquoteRdnValue",
    "DsUnquoteRdnValueA",
    "DsGetRdnW",
    "DsCrackUnquotedMangledRdnW",
    "DsCrackUnquotedMangledRdn",
    "DsCrackUnquotedMangledRdnA",
    "DsIsMangledRdnValueW",
    "DsIsMangledRdnValue",
    "DsIsMangledRdnValueA",
    "DsIsMangledDnA",
    "DsIsMangledDnW",
    "DsIsMangledDn",
    "DsCrackSpn2A",
    "DsCrackSpn2W",
    "DsCrackSpn2",
    "DsCrackSpn3W",
    "DsCrackSpn4W",
    "DsBindW",
    "DsBind",
    "DsBindA",
    "DsBindWithCredW",
    "DsBindWithCred",
    "DsBindWithCredA",
    "DsBindWithSpnW",
    "DsBindWithSpn",
    "DsBindWithSpnA",
    "DsBindWithSpnExW",
    "DsBindWithSpnEx",
    "DsBindWithSpnExA",
    "DsBindByInstanceW",
    "DsBindByInstance",
    "DsBindByInstanceA",
    "DsBindToISTGW",
    "DsBindToISTG",
    "DsBindToISTGA",
    "DsBindingSetTimeout",
    "DsUnBindW",
    "DsUnBind",
    "DsUnBindA",
    "DsMakePasswordCredentialsW",
    "DsMakePasswordCredentials",
    "DsMakePasswordCredentialsA",
    "DsFreePasswordCredentials",
    "DsCrackNamesW",
    "DsCrackNames",
    "DsCrackNamesA",
    "DsFreeNameResultW",
    "DsFreeNameResult",
    "DsFreeNameResultA",
    "DsGetSpnA",
    "DsGetSpnW",
    "DsGetSpn",
    "DsFreeSpnArrayA",
    "DsFreeSpnArrayW",
    "DsFreeSpnArray",
    "DsWriteAccountSpnA",
    "DsWriteAccountSpnW",
    "DsWriteAccountSpn",
    "DsClientMakeSpnForTargetServerW",
    "DsClientMakeSpnForTargetServer",
    "DsClientMakeSpnForTargetServerA",
    "DsServerRegisterSpnA",
    "DsServerRegisterSpnW",
    "DsServerRegisterSpn",
    "DsReplicaSyncA",
    "DsReplicaSyncW",
    "DsReplicaSync",
    "DsReplicaAddA",
    "DsReplicaAddW",
    "DsReplicaAdd",
    "DsReplicaDelA",
    "DsReplicaDelW",
    "DsReplicaDel",
    "DsReplicaModifyA",
    "DsReplicaModifyW",
    "DsReplicaModify",
    "DsReplicaUpdateRefsA",
    "DsReplicaUpdateRefsW",
    "DsReplicaUpdateRefs",
    "DsReplicaSyncAllA",
    "DsReplicaSyncAllW",
    "DsReplicaSyncAll",
    "DsRemoveDsServerW",
    "DsRemoveDsServer",
    "DsRemoveDsServerA",
    "DsRemoveDsDomainW",
    "DsRemoveDsDomain",
    "DsRemoveDsDomainA",
    "DsListSitesA",
    "DsListSitesW",
    "DsListSites",
    "DsListServersInSiteA",
    "DsListServersInSiteW",
    "DsListServersInSite",
    "DsListDomainsInSiteA",
    "DsListDomainsInSiteW",
    "DsListDomainsInSite",
    "DsListServersForDomainInSiteA",
    "DsListServersForDomainInSiteW",
    "DsListServersForDomainInSite",
    "DsListInfoForServerA",
    "DsListInfoForServerW",
    "DsListInfoForServer",
    "DsListRolesA",
    "DsListRolesW",
    "DsListRoles",
    "DsQuerySitesByCostW",
    "DsQuerySitesByCost",
    "DsQuerySitesByCostA",
    "DsQuerySitesFree",
    "DsMapSchemaGuidsA",
    "DsFreeSchemaGuidMapA",
    "DsMapSchemaGuidsW",
    "DsMapSchemaGuids",
    "DsFreeSchemaGuidMapW",
    "DsFreeSchemaGuidMap",
    "DsGetDomainControllerInfoA",
    "DsGetDomainControllerInfoW",
    "DsGetDomainControllerInfo",
    "DsFreeDomainControllerInfoA",
    "DsFreeDomainControllerInfoW",
    "DsFreeDomainControllerInfo",
    "DsReplicaConsistencyCheck",
    "DsReplicaVerifyObjectsW",
    "DsReplicaVerifyObjects",
    "DsReplicaVerifyObjectsA",
    "DsReplicaGetInfoW",
    "DsReplicaGetInfo2W",
    "DsReplicaFreeInfo",
    "DsAddSidHistoryW",
    "DsAddSidHistory",
    "DsAddSidHistoryA",
    "DsInheritSecurityIdentityW",
    "DsInheritSecurityIdentity",
    "DsInheritSecurityIdentityA",
    "DsRoleGetPrimaryDomainInformation",
    "DsRoleFreeMemory",
    "DsGetDcNameA",
    "DsGetDcNameW",
    "DsGetDcName",
    "DsGetSiteNameA",
    "DsGetSiteNameW",
    "DsGetSiteName",
    "DsValidateSubnetNameW",
    "DsValidateSubnetName",
    "DsValidateSubnetNameA",
    "DsAddressToSiteNamesW",
    "DsAddressToSiteNames",
    "DsAddressToSiteNamesA",
    "DsAddressToSiteNamesExW",
    "DsAddressToSiteNamesEx",
    "DsAddressToSiteNamesExA",
    "DsEnumerateDomainTrustsW",
    "DsEnumerateDomainTrusts",
    "DsEnumerateDomainTrustsA",
    "DsGetForestTrustInformationW",
    "DsMergeForestTrustInformationW",
    "DsGetDcSiteCoverageW",
    "DsGetDcSiteCoverage",
    "DsGetDcSiteCoverageA",
    "DsDeregisterDnsHostRecordsW",
    "DsDeregisterDnsHostRecords",
    "DsDeregisterDnsHostRecordsA",
    "DsGetDcOpenW",
    "DsGetDcOpen",
    "DsGetDcOpenA",
    "DsGetDcNextW",
    "DsGetDcNext",
    "DsGetDcNextA",
    "DsGetDcCloseW",
]
