from win32more.base import *
import win32more.Foundation
import win32more.Security.Authentication.Identity
import win32more.Security.Cryptography
import win32more.Security.Cryptography.Certificates
import win32more.System.Com

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
CA_DISP_INCOMPLETE = 0
CA_DISP_ERROR = 1
CA_DISP_REVOKED = 2
CA_DISP_VALID = 3
CA_DISP_INVALID = 4
CA_DISP_UNDER_SUBMISSION = 5
KRA_DISP_EXPIRED = 0
KRA_DISP_NOTFOUND = 1
KRA_DISP_REVOKED = 2
KRA_DISP_VALID = 3
KRA_DISP_INVALID = 4
KRA_DISP_UNTRUSTED = 5
KRA_DISP_NOTLOADED = 6
CA_ACCESS_MASKROLES = 255
CA_CRL_BASE = 1
CA_CRL_DELTA = 2
CA_CRL_REPUBLISH = 16
ICF_ALLOWFOREIGN = 65536
ICF_EXISTINGROW = 131072
IKF_OVERWRITE = 65536
CSBACKUP_TYPE_MASK = 3
CSRESTORE_TYPE_FULL = 1
CSRESTORE_TYPE_ONLINE = 2
CSRESTORE_TYPE_CATCHUP = 4
CSRESTORE_TYPE_MASK = 5
CSBACKUP_DISABLE_INCREMENTAL = 4294967295
CSBFT_DIRECTORY = 128
CSBFT_DATABASE_DIRECTORY = 64
CSBFT_LOG_DIRECTORY = 32
CSCONTROL_SHUTDOWN = 1
CSCONTROL_SUSPEND = 2
CSCONTROL_RESTART = 3
CAIF_DSENTRY = 1
CAIF_SHAREDFOLDERENTRY = 2
CAIF_REGISTRY = 4
CAIF_LOCAL = 8
CAIF_REGISTRYPARENT = 16
CR_IN_ENCODEANY = 255
CR_IN_ENCODEMASK = 255
CR_IN_FORMATANY = 0
CR_IN_PKCS10 = 256
CR_IN_KEYGEN = 512
CR_IN_PKCS7 = 768
CR_IN_CMC = 1024
CR_IN_CHALLENGERESPONSE = 1280
CR_IN_SIGNEDCERTIFICATETIMESTAMPLIST = 1536
CR_IN_FORMATMASK = 65280
CR_IN_SCEP = 65536
CR_IN_RPC = 131072
CR_IN_HTTP = 196608
CR_IN_FULLRESPONSE = 262144
CR_IN_CRLS = 524288
CR_IN_MACHINE = 1048576
CR_IN_ROBO = 2097152
CR_IN_CLIENTIDNONE = 4194304
CR_IN_CONNECTONLY = 8388608
CR_IN_RETURNCHALLENGE = 16777216
CR_IN_SCEPPOST = 33554432
CR_IN_CERTIFICATETRANSPARENCY = 67108864
CC_UIPICKCONFIGSKIPLOCALCA = 5
CR_DISP_REVOKED = 6
CR_OUT_BASE64REQUESTHEADER = 3
CR_OUT_HEX = 4
CR_OUT_HEXASCII = 5
CR_OUT_BASE64X509CRLHEADER = 9
CR_OUT_HEXADDR = 10
CR_OUT_HEXASCIIADDR = 11
CR_OUT_HEXRAW = 12
CR_OUT_ENCODEMASK = 255
CR_OUT_CHAIN = 256
CR_OUT_CRLS = 512
CR_OUT_NOCRLF = 1073741824
CR_OUT_NOCR = 2147483648
CR_GEMT_DEFAULT = 0
CR_GEMT_HRESULT_STRING = 1
CR_GEMT_HTTP_ERROR = 2
CR_PROP_NONE = 0
CR_PROP_FILEVERSION = 1
CR_PROP_PRODUCTVERSION = 2
CR_PROP_EXITCOUNT = 3
CR_PROP_EXITDESCRIPTION = 4
CR_PROP_POLICYDESCRIPTION = 5
CR_PROP_CANAME = 6
CR_PROP_SANITIZEDCANAME = 7
CR_PROP_SHAREDFOLDER = 8
CR_PROP_PARENTCA = 9
CR_PROP_CATYPE = 10
CR_PROP_CASIGCERTCOUNT = 11
CR_PROP_CASIGCERT = 12
CR_PROP_CASIGCERTCHAIN = 13
CR_PROP_CAXCHGCERTCOUNT = 14
CR_PROP_CAXCHGCERT = 15
CR_PROP_CAXCHGCERTCHAIN = 16
CR_PROP_BASECRL = 17
CR_PROP_DELTACRL = 18
CR_PROP_CACERTSTATE = 19
CR_PROP_CRLSTATE = 20
CR_PROP_CAPROPIDMAX = 21
CR_PROP_DNSNAME = 22
CR_PROP_ROLESEPARATIONENABLED = 23
CR_PROP_KRACERTUSEDCOUNT = 24
CR_PROP_KRACERTCOUNT = 25
CR_PROP_KRACERT = 26
CR_PROP_KRACERTSTATE = 27
CR_PROP_ADVANCEDSERVER = 28
CR_PROP_TEMPLATES = 29
CR_PROP_BASECRLPUBLISHSTATUS = 30
CR_PROP_DELTACRLPUBLISHSTATUS = 31
CR_PROP_CASIGCERTCRLCHAIN = 32
CR_PROP_CAXCHGCERTCRLCHAIN = 33
CR_PROP_CACERTSTATUSCODE = 34
CR_PROP_CAFORWARDCROSSCERT = 35
CR_PROP_CABACKWARDCROSSCERT = 36
CR_PROP_CAFORWARDCROSSCERTSTATE = 37
CR_PROP_CABACKWARDCROSSCERTSTATE = 38
CR_PROP_CACERTVERSION = 39
CR_PROP_SANITIZEDCASHORTNAME = 40
CR_PROP_CERTCDPURLS = 41
CR_PROP_CERTAIAURLS = 42
CR_PROP_CERTAIAOCSPURLS = 43
CR_PROP_LOCALENAME = 44
CR_PROP_SUBJECTTEMPLATE_OIDS = 45
CR_PROP_SCEPSERVERCERTS = 1000
CR_PROP_SCEPSERVERCAPABILITIES = 1001
CR_PROP_SCEPSERVERCERTSCHAIN = 1002
CR_PROP_SCEPMIN = 1000
CR_PROP_SCEPMAX = 1002
FR_PROP_CLAIMCHALLENGE = 22
EAN_NAMEOBJECTID = 2147483648
EANR_SUPPRESS_IA5CONVERSION = 2147483648
CERTENROLL_INDEX_BASE = 0
EXITEVENT_INVALID = 0
EXITEVENT_STARTUP = 128
EXITEVENT_CERTIMPORTED = 512
ENUMEXT_OBJECTID = 1
CMM_REFRESHONLY = 1
CMM_READONLY = 2
DBSESSIONCOUNTDEFAULT = 100
DBFLAGS_READONLY = 1
DBFLAGS_CREATEIFNEEDED = 2
DBFLAGS_CIRCULARLOGGING = 4
DBFLAGS_LAZYFLUSH = 8
DBFLAGS_MAXCACHESIZEX100 = 16
DBFLAGS_CHECKPOINTDEPTH60MB = 32
DBFLAGS_LOGBUFFERSLARGE = 64
DBFLAGS_LOGBUFFERSHUGE = 128
DBFLAGS_LOGFILESIZE16MB = 256
DBFLAGS_MULTITHREADTRANSACTIONS = 512
DBFLAGS_DISABLESNAPSHOTBACKUP = 1024
DBFLAGS_ENABLEVOLATILEREQUESTS = 2048
LDAPF_SSLENABLE = 1
LDAPF_SIGNDISABLE = 2
CSVER_MAJOR_WIN2K = 1
CSVER_MINOR_WIN2K = 1
CSVER_MAJOR_WHISTLER = 2
CSVER_MINOR_WHISTLER_BETA2 = 1
CSVER_MINOR_WHISTLER_BETA3 = 2
CSVER_MAJOR_LONGHORN = 3
CSVER_MINOR_LONGHORN_BETA1 = 1
CSVER_MAJOR_WIN7 = 4
CSVER_MINOR_WIN7 = 1
CSVER_MAJOR_WIN8 = 5
CSVER_MINOR_WIN8 = 1
CSVER_MAJOR_WINBLUE = 6
CSVER_MINOR_WINBLUE = 1
CSVER_MAJOR_THRESHOLD = 7
CSVER_MINOR_THRESHOLD = 1
CSVER_MAJOR = 7
CSVER_MINOR = 1
CCLOCKSKEWMINUTESDEFAULT = 10
CVIEWAGEMINUTESDEFAULT = 16
SETUP_SERVER_FLAG = 1
SETUP_CLIENT_FLAG = 2
SETUP_SUSPEND_FLAG = 4
SETUP_REQUEST_FLAG = 8
SETUP_ONLINE_FLAG = 16
SETUP_DENIED_FLAG = 32
SETUP_CREATEDB_FLAG = 64
SETUP_ATTEMPT_VROOT_CREATE = 128
SETUP_FORCECRL_FLAG = 256
SETUP_UPDATE_CAOBJECT_SVRTYPE = 512
SETUP_SERVER_UPGRADED_FLAG = 1024
SETUP_W2K_SECURITY_NOT_UPGRADED_FLAG = 2048
SETUP_SECURITY_CHANGED = 4096
SETUP_DCOM_SECURITY_UPDATED_FLAG = 8192
SETUP_SERVER_IS_UP_TO_DATE_FLAG = 16384
CRLF_DELTA_USE_OLDEST_UNEXPIRED_BASE = 1
CRLF_DELETE_EXPIRED_CRLS = 2
CRLF_CRLNUMBER_CRITICAL = 4
CRLF_REVCHECK_IGNORE_OFFLINE = 8
CRLF_IGNORE_INVALID_POLICIES = 16
CRLF_REBUILD_MODIFIED_SUBJECT_ONLY = 32
CRLF_SAVE_FAILED_CERTS = 64
CRLF_IGNORE_UNKNOWN_CMC_ATTRIBUTES = 128
CRLF_IGNORE_CROSS_CERT_TRUST_ERROR = 256
CRLF_PUBLISH_EXPIRED_CERT_CRLS = 512
CRLF_ENFORCE_ENROLLMENT_AGENT = 1024
CRLF_DISABLE_RDN_REORDER = 2048
CRLF_DISABLE_ROOT_CROSS_CERTS = 4096
CRLF_LOG_FULL_RESPONSE = 8192
CRLF_USE_XCHG_CERT_TEMPLATE = 16384
CRLF_USE_CROSS_CERT_TEMPLATE = 32768
CRLF_ALLOW_REQUEST_ATTRIBUTE_SUBJECT = 65536
CRLF_REVCHECK_IGNORE_NOREVCHECK = 131072
CRLF_PRESERVE_EXPIRED_CA_CERTS = 262144
CRLF_PRESERVE_REVOKED_CA_CERTS = 524288
CRLF_DISABLE_CHAIN_VERIFICATION = 1048576
CRLF_BUILD_ROOTCA_CRLENTRIES_BASEDONKEY = 2097152
KRAF_ENABLEFOREIGN = 1
KRAF_SAVEBADREQUESTKEY = 2
KRAF_ENABLEARCHIVEALL = 4
KRAF_DISABLEUSEDEFAULTPROVIDER = 8
IF_LOCKICERTREQUEST = 1
IF_NOREMOTEICERTREQUEST = 2
IF_NOLOCALICERTREQUEST = 4
IF_NORPCICERTREQUEST = 8
IF_NOREMOTEICERTADMIN = 16
IF_NOLOCALICERTADMIN = 32
IF_NOREMOTEICERTADMINBACKUP = 64
IF_NOLOCALICERTADMINBACKUP = 128
IF_NOSNAPSHOTBACKUP = 256
IF_ENFORCEENCRYPTICERTREQUEST = 512
IF_ENFORCEENCRYPTICERTADMIN = 1024
IF_ENABLEEXITKEYRETRIEVAL = 2048
IF_ENABLEADMINASAUDITOR = 4096
PROCFLG_NONE = 0
PROCFLG_ENFORCEGOODKEYS = 1
CSURL_SERVERPUBLISH = 1
CSURL_ADDTOCERTCDP = 2
CSURL_ADDTOFRESHESTCRL = 4
CSURL_ADDTOCRLCDP = 8
CSURL_PUBLISHRETRY = 16
CSURL_ADDTOCERTOCSP = 32
CSURL_SERVERPUBLISHDELTA = 64
CSURL_ADDTOIDP = 128
CAPATHLENGTH_INFINITE = 4294967295
REQDISP_PENDING = 0
REQDISP_ISSUE = 1
REQDISP_DENY = 2
REQDISP_USEREQUESTATTRIBUTE = 3
REQDISP_MASK = 255
REQDISP_PENDINGFIRST = 256
REQDISP_DEFAULT_ENTERPRISE = 1
REVEXT_CDPLDAPURL_OLD = 1
REVEXT_CDPHTTPURL_OLD = 2
REVEXT_CDPFTPURL_OLD = 4
REVEXT_CDPFILEURL_OLD = 8
REVEXT_CDPURLMASK_OLD = 255
REVEXT_CDPENABLE = 256
REVEXT_ASPENABLE = 512
REVEXT_DEFAULT_NODS = 256
REVEXT_DEFAULT_DS = 256
ISSCERT_LDAPURL_OLD = 1
ISSCERT_HTTPURL_OLD = 2
ISSCERT_FTPURL_OLD = 4
ISSCERT_FILEURL_OLD = 8
ISSCERT_URLMASK_OLD = 255
ISSCERT_ENABLE = 256
ISSCERT_DEFAULT_NODS = 256
ISSCERT_DEFAULT_DS = 256
EDITF_ENABLEREQUESTEXTENSIONS = 1
EDITF_REQUESTEXTENSIONLIST = 2
EDITF_DISABLEEXTENSIONLIST = 4
EDITF_ADDOLDKEYUSAGE = 8
EDITF_ADDOLDCERTTYPE = 16
EDITF_ATTRIBUTEENDDATE = 32
EDITF_BASICCONSTRAINTSCRITICAL = 64
EDITF_BASICCONSTRAINTSCA = 128
EDITF_ENABLEAKIKEYID = 256
EDITF_ATTRIBUTECA = 512
EDITF_IGNOREREQUESTERGROUP = 1024
EDITF_ENABLEAKIISSUERNAME = 2048
EDITF_ENABLEAKIISSUERSERIAL = 4096
EDITF_ENABLEAKICRITICAL = 8192
EDITF_SERVERUPGRADED = 16384
EDITF_ATTRIBUTEEKU = 32768
EDITF_ENABLEDEFAULTSMIME = 65536
EDITF_EMAILOPTIONAL = 131072
EDITF_ATTRIBUTESUBJECTALTNAME2 = 262144
EDITF_ENABLELDAPREFERRALS = 524288
EDITF_ENABLECHASECLIENTDC = 1048576
EDITF_AUDITCERTTEMPLATELOAD = 2097152
EDITF_DISABLEOLDOSCNUPN = 4194304
EDITF_DISABLELDAPPACKAGELIST = 8388608
EDITF_ENABLEUPNMAP = 16777216
EDITF_ENABLEOCSPREVNOCHECK = 33554432
EDITF_ENABLERENEWONBEHALFOF = 67108864
EDITF_ENABLEKEYENCIPHERMENTCACERT = 134217728
EXITPUB_FILE = 1
EXITPUB_ACTIVEDIRECTORY = 2
EXITPUB_REMOVEOLDCERTS = 16
EXITPUB_DEFAULT_ENTERPRISE = 2
EXITPUB_DEFAULT_STANDALONE = 1
TP_MACHINEPOLICY = 1
KR_ENABLE_MACHINE = 1
KR_ENABLE_USER = 2
EXTENSION_CRITICAL_FLAG = 1
EXTENSION_DISABLE_FLAG = 2
EXTENSION_DELETE_FLAG = 4
EXTENSION_POLICY_MASK = 65535
EXTENSION_ORIGIN_REQUEST = 65536
EXTENSION_ORIGIN_POLICY = 131072
EXTENSION_ORIGIN_ADMIN = 196608
EXTENSION_ORIGIN_SERVER = 262144
EXTENSION_ORIGIN_RENEWALCERT = 327680
EXTENSION_ORIGIN_IMPORTEDCERT = 393216
EXTENSION_ORIGIN_PKCS7 = 458752
EXTENSION_ORIGIN_CMC = 524288
EXTENSION_ORIGIN_CACERT = 589824
EXTENSION_ORIGIN_MASK = 983040
CPF_BASE = 1
CPF_DELTA = 2
CPF_COMPLETE = 4
CPF_SHADOW = 8
CPF_CASTORE_ERROR = 16
CPF_BADURL_ERROR = 32
CPF_MANUAL = 64
CPF_SIGNATURE_ERROR = 128
CPF_LDAP_ERROR = 256
CPF_FILE_ERROR = 512
CPF_FTP_ERROR = 1024
CPF_HTTP_ERROR = 2048
CPF_POSTPONED_BASE_LDAP_ERROR = 4096
CPF_POSTPONED_BASE_FILE_ERROR = 8192
PROPTYPE_MASK = 255
PROPCALLER_SERVER = 256
PROPCALLER_POLICY = 512
PROPCALLER_EXIT = 768
PROPCALLER_ADMIN = 1024
PROPCALLER_REQUEST = 1280
PROPCALLER_MASK = 3840
PROPFLAGS_INDEXED = 65536
CR_FLG_FORCETELETEX = 1
CR_FLG_RENEWAL = 2
CR_FLG_FORCEUTF8 = 4
CR_FLG_CAXCHGCERT = 8
CR_FLG_ENROLLONBEHALFOF = 16
CR_FLG_SUBJECTUNMODIFIED = 32
CR_FLG_VALIDENCRYPTEDKEYHASH = 64
CR_FLG_CACROSSCERT = 128
CR_FLG_ENFORCEUTF8 = 256
CR_FLG_DEFINEDCACERT = 512
CR_FLG_CHALLENGEPENDING = 1024
CR_FLG_CHALLENGESATISFIED = 2048
CR_FLG_TRUSTONUSE = 4096
CR_FLG_TRUSTEKCERT = 8192
CR_FLG_TRUSTEKKEY = 16384
CR_FLG_PUBLISHERROR = 2147483648
DB_DISP_ACTIVE = 8
DB_DISP_PENDING = 9
DB_DISP_QUEUE_MAX = 9
DB_DISP_FOREIGN = 12
DB_DISP_CA_CERT = 15
DB_DISP_CA_CERT_CHAIN = 16
DB_DISP_KRA_CERT = 17
DB_DISP_LOG_MIN = 20
DB_DISP_ISSUED = 20
DB_DISP_REVOKED = 21
DB_DISP_LOG_FAILED_MIN = 30
DB_DISP_ERROR = 30
DB_DISP_DENIED = 31
VR_PENDING = 0
VR_INSTANT_OK = 1
VR_INSTANT_BAD = 2
CV_OUT_HEXRAW = 12
CV_OUT_ENCODEMASK = 255
CV_OUT_NOCRLF = 1073741824
CV_OUT_NOCR = 2147483648
CVR_SEEK_NONE = 0
CVR_SEEK_MASK = 255
CVR_SEEK_NODELTA = 4096
CVR_SORT_NONE = 0
CVR_SORT_ASCEND = 1
CVR_SORT_DESCEND = 2
CV_COLUMN_EXTENSION_DEFAULT = -4
CV_COLUMN_ATTRIBUTE_DEFAULT = -5
CV_COLUMN_CRL_DEFAULT = -6
CV_COLUMN_LOG_REVOKED_DEFAULT = -7
CVRC_TABLE_MASK = 61440
CVRC_TABLE_SHIFT = 12
CRYPT_ENUM_ALL_PROVIDERS = 1
XEPR_ENUM_FIRST = -1
XEPR_DATE = 5
XEPR_TEMPLATENAME = 6
XEPR_VERSION = 7
XEPR_V1TEMPLATENAME = 9
XEPR_V2TEMPLATEOID = 16
XEKL_KEYSIZE_DEFAULT = 4
XECP_STRING_PROPERTY = 1
XECI_DISABLE = 0
XECI_XENROLL = 1
XECI_AUTOENROLL = 2
XECI_REQWIZARD = 3
XECI_CERTREQ = 4
wszCMM_PROP_NAME = 'Name'
wszCMM_PROP_DESCRIPTION = 'Description'
wszCMM_PROP_COPYRIGHT = 'Copyright'
wszCMM_PROP_FILEVER = 'File Version'
wszCMM_PROP_PRODUCTVER = 'Product Version'
wszCMM_PROP_DISPLAY_HWND = 'HWND'
wszCMM_PROP_ISMULTITHREADED = 'IsMultiThreaded'
CERT_VIEW_COLUMN_INDEX = Int32
CV_COLUMN_LOG_DEFAULT = -2
CV_COLUMN_LOG_FAILED_DEFAULT = -3
CV_COLUMN_QUEUE_DEFAULT = -1
CERT_DELETE_ROW_FLAGS = UInt32
CDR_EXPIRED = 1
CDR_REQUEST_LAST_CHANGED = 2
FULL_RESPONSE_PROPERTY_ID = UInt32
FR_PROP_NONE = 0
FR_PROP_FULLRESPONSE = 1
FR_PROP_STATUSINFOCOUNT = 2
FR_PROP_BODYPARTSTRING = 3
FR_PROP_STATUS = 4
FR_PROP_STATUSSTRING = 5
FR_PROP_OTHERINFOCHOICE = 6
FR_PROP_FAILINFO = 7
FR_PROP_PENDINFOTOKEN = 8
FR_PROP_PENDINFOTIME = 9
FR_PROP_ISSUEDCERTIFICATEHASH = 10
FR_PROP_ISSUEDCERTIFICATE = 11
FR_PROP_ISSUEDCERTIFICATECHAIN = 12
FR_PROP_ISSUEDCERTIFICATECRLCHAIN = 13
FR_PROP_ENCRYPTEDKEYHASH = 14
FR_PROP_FULLRESPONSENOPKCS7 = 15
FR_PROP_CAEXCHANGECERTIFICATEHASH = 16
FR_PROP_CAEXCHANGECERTIFICATE = 17
FR_PROP_CAEXCHANGECERTIFICATECHAIN = 18
FR_PROP_CAEXCHANGECERTIFICATECRLCHAIN = 19
FR_PROP_ATTESTATIONCHALLENGE = 20
FR_PROP_ATTESTATIONPROVIDERNAME = 21
CVRC_COLUMN = UInt32
CVRC_COLUMN_SCHEMA = 0
CVRC_COLUMN_RESULT = 1
CVRC_COLUMN_VALUE = 2
CVRC_COLUMN_MASK = 4095
CERT_IMPORT_FLAGS = UInt32
CR_IN_BASE64HEADER = 0
CR_IN_BASE64 = 1
CR_IN_BINARY = 2
CERT_GET_CONFIG_FLAGS = UInt32
CC_DEFAULTCONFIG = 0
CC_FIRSTCONFIG = 2
CC_LOCALACTIVECONFIG = 4
CC_LOCALCONFIG = 3
CC_UIPICKCONFIG = 1
CC_UIPICKCONFIGSKIPLOCALCA_ = 5
ENUM_CERT_COLUMN_VALUE_FLAGS = UInt32
CV_OUT_BASE64 = 1
CV_OUT_BASE64HEADER = 0
CV_OUT_BASE64REQUESTHEADER = 3
CV_OUT_BASE64X509CRLHEADER = 9
CV_OUT_BINARY = 2
CV_OUT_HEX = 4
CV_OUT_HEXADDR = 10
CV_OUT_HEXASCII = 5
CV_OUT_HEXASCIIADDR = 11
PENDING_REQUEST_DESIRED_PROPERTY = UInt32
XEPR_CADNS = 1
XEPR_CAFRIENDLYNAME = 3
XEPR_CANAME = 2
XEPR_HASH = 8
XEPR_REQUESTID = 4
CERTADMIN_GET_ROLES_FLAGS = UInt32
CA_ACCESS_ADMIN = 1
CA_ACCESS_AUDITOR = 4
CA_ACCESS_ENROLL = 512
CA_ACCESS_OFFICER = 2
CA_ACCESS_OPERATOR = 8
CA_ACCESS_READ = 256
CR_DISP = UInt32
CR_DISP_DENIED = 2
CR_DISP_ERROR = 1
CR_DISP_INCOMPLETE = 0
CR_DISP_ISSUED = 3
CR_DISP_ISSUED_OUT_OF_BAND = 4
CR_DISP_UNDER_SUBMISSION = 5
XEKL_KEYSIZE = UInt32
XEKL_KEYSIZE_MIN = 1
XEKL_KEYSIZE_MAX = 2
XEKL_KEYSIZE_INC = 3
CERT_CREATE_REQUEST_FLAGS = UInt32
XECR_CMC = 3
XECR_PKCS10_V1_5 = 4
XECR_PKCS10_V2_0 = 1
XECR_PKCS7 = 2
CERT_EXIT_EVENT_MASK = UInt32
EXITEVENT_CERTDENIED = 4
EXITEVENT_CERTISSUED = 1
EXITEVENT_CERTPENDING = 2
EXITEVENT_CERTRETRIEVEPENDING = 16
EXITEVENT_CERTREVOKED = 8
EXITEVENT_CRLISSUED = 32
EXITEVENT_SHUTDOWN = 64
ADDED_CERT_TYPE = UInt32
XECT_EXTENSION_V1 = 1
XECT_EXTENSION_V2 = 2
CVRC_TABLE = UInt32
CVRC_TABLE_ATTRIBUTES = 16384
CVRC_TABLE_CRL = 20480
CVRC_TABLE_EXTENSIONS = 12288
CVRC_TABLE_REQCERT = 0
CERT_PROPERTY_TYPE = UInt32
PROPTYPE_BINARY = 3
PROPTYPE_DATE = 2
PROPTYPE_LONG = 1
PROPTYPE_STRING = 4
CERT_ALT_NAME = UInt32
CERT_ALT_NAME_RFC822_NAME = 2
CERT_ALT_NAME_DNS_NAME = 3
CERT_ALT_NAME_URL = 7
CERT_ALT_NAME_REGISTERED_ID = 9
CERT_ALT_NAME_DIRECTORY_NAME = 5
CERT_ALT_NAME_IP_ADDRESS = 8
CERT_ALT_NAME_OTHER_NAME = 1
CSBACKUP_TYPE = UInt32
CSBACKUP_TYPE_FULL = 1
CSBACKUP_TYPE_LOGS_ONLY = 2
XEKL_KEYSPEC = UInt32
XEKL_KEYSPEC_KEYX = 1
XEKL_KEYSPEC_SIG = 2
CERT_REQUEST_OUT_TYPE = UInt32
CR_OUT_BASE64HEADER = 0
CR_OUT_BASE64 = 1
CR_OUT_BINARY = 2
CERT_VIEW_SEEK_OPERATOR_FLAGS = UInt32
CVR_SEEK_EQ = 1
CVR_SEEK_LE = 4
CVR_SEEK_LT = 2
CVR_SEEK_GE = 8
CVR_SEEK_GT = 16
CCertAdmin = Guid('37eabaf0-7fb6-11d0-8817-00a0c903b83c')
CCertView = Guid('a12d0f7a-1e84-11d1-9bd6-00c04fb683fa')
OCSPPropertyCollection = Guid('f935a528-ba8a-4dd9-ba79-f283275cb2de')
OCSPAdmin = Guid('d3f73511-92c9-47cb-8ff2-8d891a7c4de4')
def _define_IEnumCERTVIEWCOLUMN_head():
    class IEnumCERTVIEWCOLUMN(win32more.System.Com.IDispatch_head):
        Guid = Guid('9c735be2-57a5-11d1-9bdb-00c04fb683fa')
    return IEnumCERTVIEWCOLUMN
def _define_IEnumCERTVIEWCOLUMN():
    IEnumCERTVIEWCOLUMN = win32more.Security.Cryptography.Certificates.IEnumCERTVIEWCOLUMN_head
    IEnumCERTVIEWCOLUMN.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'Next', ((1, 'pIndex'),)))
    IEnumCERTVIEWCOLUMN.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetName', ((1, 'pstrOut'),)))
    IEnumCERTVIEWCOLUMN.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetDisplayName', ((1, 'pstrOut'),)))
    IEnumCERTVIEWCOLUMN.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'GetType', ((1, 'pType'),)))
    IEnumCERTVIEWCOLUMN.IsIndexed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'IsIndexed', ((1, 'pIndexed'),)))
    IEnumCERTVIEWCOLUMN.GetMaxLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'GetMaxLength', ((1, 'pMaxLength'),)))
    IEnumCERTVIEWCOLUMN.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ENUM_CERT_COLUMN_VALUE_FLAGS,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'GetValue', ((1, 'Flags'),(1, 'pvarValue'),)))
    IEnumCERTVIEWCOLUMN.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'Skip', ((1, 'celt'),)))
    IEnumCERTVIEWCOLUMN.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'Reset', ()))
    IEnumCERTVIEWCOLUMN.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IEnumCERTVIEWCOLUMN_head), use_last_error=False)(16, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IDispatch
    return IEnumCERTVIEWCOLUMN
def _define_IEnumCERTVIEWATTRIBUTE_head():
    class IEnumCERTVIEWATTRIBUTE(win32more.System.Com.IDispatch_head):
        Guid = Guid('e77db656-7653-11d1-9bde-00c04fb683fa')
    return IEnumCERTVIEWATTRIBUTE
def _define_IEnumCERTVIEWATTRIBUTE():
    IEnumCERTVIEWATTRIBUTE = win32more.Security.Cryptography.Certificates.IEnumCERTVIEWATTRIBUTE_head
    IEnumCERTVIEWATTRIBUTE.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'Next', ((1, 'pIndex'),)))
    IEnumCERTVIEWATTRIBUTE.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetName', ((1, 'pstrOut'),)))
    IEnumCERTVIEWATTRIBUTE.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetValue', ((1, 'pstrOut'),)))
    IEnumCERTVIEWATTRIBUTE.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'Skip', ((1, 'celt'),)))
    IEnumCERTVIEWATTRIBUTE.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Reset', ()))
    IEnumCERTVIEWATTRIBUTE.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IEnumCERTVIEWATTRIBUTE_head), use_last_error=False)(12, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IDispatch
    return IEnumCERTVIEWATTRIBUTE
def _define_IEnumCERTVIEWEXTENSION_head():
    class IEnumCERTVIEWEXTENSION(win32more.System.Com.IDispatch_head):
        Guid = Guid('e7dd1466-7653-11d1-9bde-00c04fb683fa')
    return IEnumCERTVIEWEXTENSION
def _define_IEnumCERTVIEWEXTENSION():
    IEnumCERTVIEWEXTENSION = win32more.Security.Cryptography.Certificates.IEnumCERTVIEWEXTENSION_head
    IEnumCERTVIEWEXTENSION.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'Next', ((1, 'pIndex'),)))
    IEnumCERTVIEWEXTENSION.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetName', ((1, 'pstrOut'),)))
    IEnumCERTVIEWEXTENSION.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'GetFlags', ((1, 'pFlags'),)))
    IEnumCERTVIEWEXTENSION.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CERT_PROPERTY_TYPE,win32more.Security.Cryptography.Certificates.ENUM_CERT_COLUMN_VALUE_FLAGS,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'GetValue', ((1, 'Type'),(1, 'Flags'),(1, 'pvarValue'),)))
    IEnumCERTVIEWEXTENSION.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Skip', ((1, 'celt'),)))
    IEnumCERTVIEWEXTENSION.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Reset', ()))
    IEnumCERTVIEWEXTENSION.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IEnumCERTVIEWEXTENSION_head), use_last_error=False)(13, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IDispatch
    return IEnumCERTVIEWEXTENSION
def _define_IEnumCERTVIEWROW_head():
    class IEnumCERTVIEWROW(win32more.System.Com.IDispatch_head):
        Guid = Guid('d1157f4c-5af2-11d1-9bdc-00c04fb683fa')
    return IEnumCERTVIEWROW
def _define_IEnumCERTVIEWROW():
    IEnumCERTVIEWROW = win32more.Security.Cryptography.Certificates.IEnumCERTVIEWROW_head
    IEnumCERTVIEWROW.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'Next', ((1, 'pIndex'),)))
    IEnumCERTVIEWROW.EnumCertViewColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IEnumCERTVIEWCOLUMN_head), use_last_error=False)(8, 'EnumCertViewColumn', ((1, 'ppenum'),)))
    IEnumCERTVIEWROW.EnumCertViewAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.IEnumCERTVIEWATTRIBUTE_head), use_last_error=False)(9, 'EnumCertViewAttribute', ((1, 'Flags'),(1, 'ppenum'),)))
    IEnumCERTVIEWROW.EnumCertViewExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.IEnumCERTVIEWEXTENSION_head), use_last_error=False)(10, 'EnumCertViewExtension', ((1, 'Flags'),(1, 'ppenum'),)))
    IEnumCERTVIEWROW.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Skip', ((1, 'celt'),)))
    IEnumCERTVIEWROW.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Reset', ()))
    IEnumCERTVIEWROW.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IEnumCERTVIEWROW_head), use_last_error=False)(13, 'Clone', ((1, 'ppenum'),)))
    IEnumCERTVIEWROW.GetMaxIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'GetMaxIndex', ((1, 'pIndex'),)))
    win32more.System.Com.IDispatch
    return IEnumCERTVIEWROW
def _define_ICertView_head():
    class ICertView(win32more.System.Com.IDispatch_head):
        Guid = Guid('c3fac344-1e84-11d1-9bd6-00c04fb683fa')
    return ICertView
def _define_ICertView():
    ICertView = win32more.Security.Cryptography.Certificates.ICertView_head
    ICertView.OpenConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'OpenConnection', ((1, 'strConfig'),)))
    ICertView.EnumCertViewColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CVRC_COLUMN,POINTER(win32more.Security.Cryptography.Certificates.IEnumCERTVIEWCOLUMN_head), use_last_error=False)(8, 'EnumCertViewColumn', ((1, 'fResultColumn'),(1, 'ppenum'),)))
    ICertView.GetColumnCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CVRC_COLUMN,POINTER(Int32), use_last_error=False)(9, 'GetColumnCount', ((1, 'fResultColumn'),(1, 'pcColumn'),)))
    ICertView.GetColumnIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CVRC_COLUMN,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(10, 'GetColumnIndex', ((1, 'fResultColumn'),(1, 'strColumnName'),(1, 'pColumnIndex'),)))
    ICertView.SetResultColumnCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'SetResultColumnCount', ((1, 'cResultColumn'),)))
    ICertView.SetResultColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'SetResultColumn', ((1, 'ColumnIndex'),)))
    ICertView.SetRestriction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CERT_VIEW_COLUMN_INDEX,win32more.Security.Cryptography.Certificates.CERT_VIEW_SEEK_OPERATOR_FLAGS,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'SetRestriction', ((1, 'ColumnIndex'),(1, 'SeekOperator'),(1, 'SortOrder'),(1, 'pvarValue'),)))
    ICertView.OpenView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IEnumCERTVIEWROW_head), use_last_error=False)(14, 'OpenView', ((1, 'ppenum'),)))
    win32more.System.Com.IDispatch
    return ICertView
def _define_ICertView2_head():
    class ICertView2(win32more.Security.Cryptography.Certificates.ICertView_head):
        Guid = Guid('d594b282-8851-4b61-9c66-3edadf848863')
    return ICertView2
def _define_ICertView2():
    ICertView2 = win32more.Security.Cryptography.Certificates.ICertView2_head
    ICertView2.SetTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CVRC_TABLE, use_last_error=False)(15, 'SetTable', ((1, 'Table'),)))
    win32more.Security.Cryptography.Certificates.ICertView
    return ICertView2
def _define_ICertAdmin_head():
    class ICertAdmin(win32more.System.Com.IDispatch_head):
        Guid = Guid('34df6950-7fb6-11d0-8817-00a0c903b83c')
    return ICertAdmin
def _define_ICertAdmin():
    ICertAdmin = win32more.Security.Cryptography.Certificates.ICertAdmin_head
    ICertAdmin.IsValidCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(7, 'IsValidCertificate', ((1, 'strConfig'),(1, 'strSerialNumber'),(1, 'pDisposition'),)))
    ICertAdmin.GetRevocationReason = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'GetRevocationReason', ((1, 'pReason'),)))
    ICertAdmin.RevokeCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,Double, use_last_error=False)(9, 'RevokeCertificate', ((1, 'strConfig'),(1, 'strSerialNumber'),(1, 'Reason'),(1, 'Date'),)))
    ICertAdmin.SetRequestAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR, use_last_error=False)(10, 'SetRequestAttributes', ((1, 'strConfig'),(1, 'RequestId'),(1, 'strAttributes'),)))
    ICertAdmin.SetCertificateExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.CERT_PROPERTY_TYPE,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'SetCertificateExtension', ((1, 'strConfig'),(1, 'RequestId'),(1, 'strExtensionName'),(1, 'Type'),(1, 'Flags'),(1, 'pvarValue'),)))
    ICertAdmin.DenyRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32, use_last_error=False)(12, 'DenyRequest', ((1, 'strConfig'),(1, 'RequestId'),)))
    ICertAdmin.ResubmitRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(Int32), use_last_error=False)(13, 'ResubmitRequest', ((1, 'strConfig'),(1, 'RequestId'),(1, 'pDisposition'),)))
    ICertAdmin.PublishCRL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Double, use_last_error=False)(14, 'PublishCRL', ((1, 'strConfig'),(1, 'Date'),)))
    ICertAdmin.GetCRL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'GetCRL', ((1, 'strConfig'),(1, 'Flags'),(1, 'pstrCRL'),)))
    ICertAdmin.ImportCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.CERT_IMPORT_FLAGS,POINTER(Int32), use_last_error=False)(16, 'ImportCertificate', ((1, 'strConfig'),(1, 'strCertificate'),(1, 'Flags'),(1, 'pRequestId'),)))
    win32more.System.Com.IDispatch
    return ICertAdmin
def _define_ICertAdmin2_head():
    class ICertAdmin2(win32more.Security.Cryptography.Certificates.ICertAdmin_head):
        Guid = Guid('f7c3ac41-b8ce-4fb4-aa58-3d1dc0e36b39')
    return ICertAdmin2
def _define_ICertAdmin2():
    ICertAdmin2 = win32more.Security.Cryptography.Certificates.ICertAdmin2_head
    ICertAdmin2.PublishCRLs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Double,Int32, use_last_error=False)(17, 'PublishCRLs', ((1, 'strConfig'),(1, 'Date'),(1, 'CRLFlags'),)))
    ICertAdmin2.GetCAProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(18, 'GetCAProperty', ((1, 'strConfig'),(1, 'PropId'),(1, 'PropIndex'),(1, 'PropType'),(1, 'Flags'),(1, 'pvarPropertyValue'),)))
    ICertAdmin2.SetCAProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,win32more.Security.Cryptography.Certificates.CERT_PROPERTY_TYPE,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(19, 'SetCAProperty', ((1, 'strConfig'),(1, 'PropId'),(1, 'PropIndex'),(1, 'PropType'),(1, 'pvarPropertyValue'),)))
    ICertAdmin2.GetCAPropertyFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(Int32), use_last_error=False)(20, 'GetCAPropertyFlags', ((1, 'strConfig'),(1, 'PropId'),(1, 'pPropFlags'),)))
    ICertAdmin2.GetCAPropertyDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'GetCAPropertyDisplayName', ((1, 'strConfig'),(1, 'PropId'),(1, 'pstrDisplayName'),)))
    ICertAdmin2.GetArchivedKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'GetArchivedKey', ((1, 'strConfig'),(1, 'RequestId'),(1, 'Flags'),(1, 'pstrArchivedKey'),)))
    ICertAdmin2.GetConfigEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(23, 'GetConfigEntry', ((1, 'strConfig'),(1, 'strNodePath'),(1, 'strEntryName'),(1, 'pvarEntry'),)))
    ICertAdmin2.SetConfigEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(24, 'SetConfigEntry', ((1, 'strConfig'),(1, 'strNodePath'),(1, 'strEntryName'),(1, 'pvarEntry'),)))
    ICertAdmin2.ImportKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.CERT_IMPORT_FLAGS,win32more.Foundation.BSTR, use_last_error=False)(25, 'ImportKey', ((1, 'strConfig'),(1, 'RequestId'),(1, 'strCertHash'),(1, 'Flags'),(1, 'strKey'),)))
    ICertAdmin2.GetMyRoles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Cryptography.Certificates.CERTADMIN_GET_ROLES_FLAGS), use_last_error=False)(26, 'GetMyRoles', ((1, 'strConfig'),(1, 'pRoles'),)))
    ICertAdmin2.DeleteRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.CERT_DELETE_ROW_FLAGS,Double,win32more.Security.Cryptography.Certificates.CVRC_TABLE,Int32,POINTER(Int32), use_last_error=False)(27, 'DeleteRow', ((1, 'strConfig'),(1, 'Flags'),(1, 'Date'),(1, 'Table'),(1, 'RowId'),(1, 'pcDeleted'),)))
    win32more.Security.Cryptography.Certificates.ICertAdmin
    return ICertAdmin2
def _define_IOCSPProperty_head():
    class IOCSPProperty(win32more.System.Com.IDispatch_head):
        Guid = Guid('66fb7839-5f04-4c25-ad18-9ff1a8376ee0')
    return IOCSPProperty
def _define_IOCSPProperty():
    IOCSPProperty = win32more.Security.Cryptography.Certificates.IOCSPProperty_head
    IOCSPProperty.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'pVal'),)))
    IOCSPProperty.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_Value', ((1, 'pVal'),)))
    IOCSPProperty.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(9, 'put_Value', ((1, 'newVal'),)))
    IOCSPProperty.get_Modified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_Modified', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IOCSPProperty
def _define_IOCSPPropertyCollection_head():
    class IOCSPPropertyCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('2597c18d-54e6-4b74-9fa9-a6bfda99cbbe')
    return IOCSPPropertyCollection
def _define_IOCSPPropertyCollection():
    IOCSPPropertyCollection = win32more.Security.Cryptography.Certificates.IOCSPPropertyCollection_head
    IOCSPPropertyCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppVal'),)))
    IOCSPPropertyCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_Item', ((1, 'Index'),(1, 'pVal'),)))
    IOCSPPropertyCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'pVal'),)))
    IOCSPPropertyCollection.get_ItemByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'get_ItemByName', ((1, 'bstrPropName'),(1, 'pVal'),)))
    IOCSPPropertyCollection.CreateProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Security.Cryptography.Certificates.IOCSPProperty_head), use_last_error=False)(11, 'CreateProperty', ((1, 'bstrPropName'),(1, 'pVarPropValue'),(1, 'ppVal'),)))
    IOCSPPropertyCollection.DeleteProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'DeleteProperty', ((1, 'bstrPropName'),)))
    IOCSPPropertyCollection.InitializeFromProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'InitializeFromProperties', ((1, 'pVarProperties'),)))
    IOCSPPropertyCollection.GetAllProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(14, 'GetAllProperties', ((1, 'pVarProperties'),)))
    win32more.System.Com.IDispatch
    return IOCSPPropertyCollection
def _define_IOCSPCAConfiguration_head():
    class IOCSPCAConfiguration(win32more.System.Com.IDispatch_head):
        Guid = Guid('aec92b40-3d46-433f-87d1-b84d5c1e790d')
    return IOCSPCAConfiguration
def _define_IOCSPCAConfiguration():
    IOCSPCAConfiguration = win32more.Security.Cryptography.Certificates.IOCSPCAConfiguration_head
    IOCSPCAConfiguration.get_Identifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Identifier', ((1, 'pVal'),)))
    IOCSPCAConfiguration.get_CACertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_CACertificate', ((1, 'pVal'),)))
    IOCSPCAConfiguration.get_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_HashAlgorithm', ((1, 'pVal'),)))
    IOCSPCAConfiguration.put_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_HashAlgorithm', ((1, 'newVal'),)))
    IOCSPCAConfiguration.get_SigningFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'get_SigningFlags', ((1, 'pVal'),)))
    IOCSPCAConfiguration.put_SigningFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(12, 'put_SigningFlags', ((1, 'newVal'),)))
    IOCSPCAConfiguration.get_SigningCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'get_SigningCertificate', ((1, 'pVal'),)))
    IOCSPCAConfiguration.put_SigningCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(14, 'put_SigningCertificate', ((1, 'newVal'),)))
    IOCSPCAConfiguration.get_ReminderDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(15, 'get_ReminderDuration', ((1, 'pVal'),)))
    IOCSPCAConfiguration.put_ReminderDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(16, 'put_ReminderDuration', ((1, 'newVal'),)))
    IOCSPCAConfiguration.get_ErrorCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(17, 'get_ErrorCode', ((1, 'pVal'),)))
    IOCSPCAConfiguration.get_CSPName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_CSPName', ((1, 'pVal'),)))
    IOCSPCAConfiguration.get_KeySpec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(19, 'get_KeySpec', ((1, 'pVal'),)))
    IOCSPCAConfiguration.get_ProviderCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_ProviderCLSID', ((1, 'pVal'),)))
    IOCSPCAConfiguration.put_ProviderCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(21, 'put_ProviderCLSID', ((1, 'newVal'),)))
    IOCSPCAConfiguration.get_ProviderProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(22, 'get_ProviderProperties', ((1, 'pVal'),)))
    IOCSPCAConfiguration.put_ProviderProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(23, 'put_ProviderProperties', ((1, 'newVal'),)))
    IOCSPCAConfiguration.get_Modified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(24, 'get_Modified', ((1, 'pVal'),)))
    IOCSPCAConfiguration.get_LocalRevocationInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(25, 'get_LocalRevocationInformation', ((1, 'pVal'),)))
    IOCSPCAConfiguration.put_LocalRevocationInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(26, 'put_LocalRevocationInformation', ((1, 'newVal'),)))
    IOCSPCAConfiguration.get_SigningCertificateTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(27, 'get_SigningCertificateTemplate', ((1, 'pVal'),)))
    IOCSPCAConfiguration.put_SigningCertificateTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(28, 'put_SigningCertificateTemplate', ((1, 'newVal'),)))
    IOCSPCAConfiguration.get_CAConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(29, 'get_CAConfig', ((1, 'pVal'),)))
    IOCSPCAConfiguration.put_CAConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(30, 'put_CAConfig', ((1, 'newVal'),)))
    win32more.System.Com.IDispatch
    return IOCSPCAConfiguration
def _define_IOCSPCAConfigurationCollection_head():
    class IOCSPCAConfigurationCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('2bebea0b-5ece-4f28-a91c-86b4bb20f0d3')
    return IOCSPCAConfigurationCollection
def _define_IOCSPCAConfigurationCollection():
    IOCSPCAConfigurationCollection = win32more.Security.Cryptography.Certificates.IOCSPCAConfigurationCollection_head
    IOCSPCAConfigurationCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pVal'),)))
    IOCSPCAConfigurationCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_Item', ((1, 'Index'),(1, 'pVal'),)))
    IOCSPCAConfigurationCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'pVal'),)))
    IOCSPCAConfigurationCollection.get_ItemByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'get_ItemByName', ((1, 'bstrIdentifier'),(1, 'pVal'),)))
    IOCSPCAConfigurationCollection.CreateCAConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Cryptography.Certificates.IOCSPCAConfiguration_head), use_last_error=False)(11, 'CreateCAConfiguration', ((1, 'bstrIdentifier'),(1, 'varCACert'),(1, 'ppVal'),)))
    IOCSPCAConfigurationCollection.DeleteCAConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'DeleteCAConfiguration', ((1, 'bstrIdentifier'),)))
    win32more.System.Com.IDispatch
    return IOCSPCAConfigurationCollection
def _define_IOCSPAdmin_head():
    class IOCSPAdmin(win32more.System.Com.IDispatch_head):
        Guid = Guid('322e830d-67db-4fe9-9577-4596d9f09294')
    return IOCSPAdmin
def _define_IOCSPAdmin():
    IOCSPAdmin = win32more.Security.Cryptography.Certificates.IOCSPAdmin_head
    IOCSPAdmin.get_OCSPServiceProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IOCSPPropertyCollection_head), use_last_error=False)(7, 'get_OCSPServiceProperties', ((1, 'ppVal'),)))
    IOCSPAdmin.get_OCSPCAConfigurationCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IOCSPCAConfigurationCollection_head), use_last_error=False)(8, 'get_OCSPCAConfigurationCollection', ((1, 'pVal'),)))
    IOCSPAdmin.GetConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16, use_last_error=False)(9, 'GetConfiguration', ((1, 'bstrServerName'),(1, 'bForce'),)))
    IOCSPAdmin.SetConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16, use_last_error=False)(10, 'SetConfiguration', ((1, 'bstrServerName'),(1, 'bForce'),)))
    IOCSPAdmin.GetMyRoles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(11, 'GetMyRoles', ((1, 'bstrServerName'),(1, 'pRoles'),)))
    IOCSPAdmin.Ping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'Ping', ((1, 'bstrServerName'),)))
    IOCSPAdmin.SetSecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(13, 'SetSecurity', ((1, 'bstrServerName'),(1, 'bstrVal'),)))
    IOCSPAdmin.GetSecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'GetSecurity', ((1, 'bstrServerName'),(1, 'pVal'),)))
    IOCSPAdmin.GetSigningCertificates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'GetSigningCertificates', ((1, 'bstrServerName'),(1, 'pCACertVar'),(1, 'pVal'),)))
    IOCSPAdmin.GetHashAlgorithms = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(16, 'GetHashAlgorithms', ((1, 'bstrServerName'),(1, 'bstrCAId'),(1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IOCSPAdmin
OCSPSigningFlag = Int32
OCSP_SF_SILENT = 1
OCSP_SF_USE_CACERT = 2
OCSP_SF_ALLOW_SIGNINGCERT_AUTORENEWAL = 4
OCSP_SF_FORCE_SIGNINGCERT_ISSUER_ISCA = 8
OCSP_SF_AUTODISCOVER_SIGNINGCERT = 16
OCSP_SF_MANUAL_ASSIGN_SIGNINGCERT = 32
OCSP_SF_RESPONDER_ID_KEYHASH = 64
OCSP_SF_RESPONDER_ID_NAME = 128
OCSP_SF_ALLOW_NONCE_EXTENSION = 256
OCSP_SF_ALLOW_SIGNINGCERT_AUTOENROLLMENT = 512
OCSPRequestFlag = Int32
OCSP_RF_REJECT_SIGNED_REQUESTS = 1
def _define_CSEDB_RSTMAPW_head():
    class CSEDB_RSTMAPW(Structure):
        pass
    return CSEDB_RSTMAPW
def _define_CSEDB_RSTMAPW():
    CSEDB_RSTMAPW = win32more.Security.Cryptography.Certificates.CSEDB_RSTMAPW_head
    CSEDB_RSTMAPW._fields_ = [
        ("pwszDatabaseName", win32more.Foundation.PWSTR),
        ("pwszNewDatabaseName", win32more.Foundation.PWSTR),
    ]
    return CSEDB_RSTMAPW
def _define_FNCERTSRVISSERVERONLINEW():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)
def _define_FNCERTSRVBACKUPGETDYNAMICFILELISTW():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(POINTER(UInt16)),POINTER(UInt32), use_last_error=False)
def _define_FNCERTSRVBACKUPPREPAREW():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(c_void_p), use_last_error=False)
def _define_FNCERTSRVBACKUPGETDATABASENAMESW():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(POINTER(UInt16)),POINTER(UInt32), use_last_error=False)
def _define_FNCERTSRVBACKUPOPENFILEW():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.LARGE_INTEGER_head), use_last_error=False)
def _define_FNCERTSRVBACKUPREAD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)
def _define_FNCERTSRVBACKUPCLOSE():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)
def _define_FNCERTSRVBACKUPGETBACKUPLOGSW():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(POINTER(UInt16)),POINTER(UInt32), use_last_error=False)
def _define_FNCERTSRVBACKUPTRUNCATELOGS():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)
def _define_FNCERTSRVBACKUPEND():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)
def _define_FNCERTSRVBACKUPFREE():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_FNCERTSRVRESTOREGETDATABASELOCATIONSW():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(POINTER(UInt16)),POINTER(UInt32), use_last_error=False)
def _define_FNCERTSRVRESTOREPREPAREW():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(c_void_p), use_last_error=False)
def _define_FNCERTSRVRESTOREREGISTERW():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.Certificates.CSEDB_RSTMAPW_head),Int32,win32more.Foundation.PWSTR,UInt32,UInt32, use_last_error=False)
def _define_FNCERTSRVRESTOREREGISTERCOMPLETE():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.HRESULT, use_last_error=False)
def _define_FNCERTSRVRESTOREEND():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)
def _define_FNCERTSRVSERVERCONTROLW():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)
CCertGetConfig = Guid('c6cc49b0-ce17-11d0-8833-00a0c903b83c')
CCertConfig = Guid('372fce38-4324-11d0-8810-00a0c903b83c')
CCertRequest = Guid('98aff3f0-5524-11d0-8812-00a0c903b83c')
CCertServerPolicy = Guid('aa000926-ffbe-11cf-8800-00a0c903b83c')
CCertServerExit = Guid('4c4a5e40-732c-11d0-8816-00a0c903b83c')
def _define_ICertServerPolicy_head():
    class ICertServerPolicy(win32more.System.Com.IDispatch_head):
        Guid = Guid('aa000922-ffbe-11cf-8800-00a0c903b83c')
    return ICertServerPolicy
def _define_ICertServerPolicy():
    ICertServerPolicy = win32more.Security.Cryptography.Certificates.ICertServerPolicy_head
    ICertServerPolicy.SetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(7, 'SetContext', ((1, 'Context'),)))
    ICertServerPolicy.GetRequestProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'GetRequestProperty', ((1, 'strPropertyName'),(1, 'PropertyType'),(1, 'pvarPropertyValue'),)))
    ICertServerPolicy.GetRequestAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetRequestAttribute', ((1, 'strAttributeName'),(1, 'pstrAttributeValue'),)))
    ICertServerPolicy.GetCertificateProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.CERT_PROPERTY_TYPE,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'GetCertificateProperty', ((1, 'strPropertyName'),(1, 'PropertyType'),(1, 'pvarPropertyValue'),)))
    ICertServerPolicy.SetCertificateProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'SetCertificateProperty', ((1, 'strPropertyName'),(1, 'PropertyType'),(1, 'pvarPropertyValue'),)))
    ICertServerPolicy.GetCertificateExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.CERT_PROPERTY_TYPE,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(12, 'GetCertificateExtension', ((1, 'strExtensionName'),(1, 'Type'),(1, 'pvarValue'),)))
    ICertServerPolicy.GetCertificateExtensionFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'GetCertificateExtensionFlags', ((1, 'pExtFlags'),)))
    ICertServerPolicy.SetCertificateExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(14, 'SetCertificateExtension', ((1, 'strExtensionName'),(1, 'Type'),(1, 'ExtFlags'),(1, 'pvarValue'),)))
    ICertServerPolicy.EnumerateExtensionsSetup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(15, 'EnumerateExtensionsSetup', ((1, 'Flags'),)))
    ICertServerPolicy.EnumerateExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'EnumerateExtensions', ((1, 'pstrExtensionName'),)))
    ICertServerPolicy.EnumerateExtensionsClose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'EnumerateExtensionsClose', ()))
    ICertServerPolicy.EnumerateAttributesSetup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'EnumerateAttributesSetup', ((1, 'Flags'),)))
    ICertServerPolicy.EnumerateAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'EnumerateAttributes', ((1, 'pstrAttributeName'),)))
    ICertServerPolicy.EnumerateAttributesClose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(20, 'EnumerateAttributesClose', ()))
    win32more.System.Com.IDispatch
    return ICertServerPolicy
def _define_ICertServerExit_head():
    class ICertServerExit(win32more.System.Com.IDispatch_head):
        Guid = Guid('4ba9eb90-732c-11d0-8816-00a0c903b83c')
    return ICertServerExit
def _define_ICertServerExit():
    ICertServerExit = win32more.Security.Cryptography.Certificates.ICertServerExit_head
    ICertServerExit.SetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(7, 'SetContext', ((1, 'Context'),)))
    ICertServerExit.GetRequestProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'GetRequestProperty', ((1, 'strPropertyName'),(1, 'PropertyType'),(1, 'pvarPropertyValue'),)))
    ICertServerExit.GetRequestAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetRequestAttribute', ((1, 'strAttributeName'),(1, 'pstrAttributeValue'),)))
    ICertServerExit.GetCertificateProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'GetCertificateProperty', ((1, 'strPropertyName'),(1, 'PropertyType'),(1, 'pvarPropertyValue'),)))
    ICertServerExit.GetCertificateExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'GetCertificateExtension', ((1, 'strExtensionName'),(1, 'Type'),(1, 'pvarValue'),)))
    ICertServerExit.GetCertificateExtensionFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'GetCertificateExtensionFlags', ((1, 'pExtFlags'),)))
    ICertServerExit.EnumerateExtensionsSetup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'EnumerateExtensionsSetup', ((1, 'Flags'),)))
    ICertServerExit.EnumerateExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'EnumerateExtensions', ((1, 'pstrExtensionName'),)))
    ICertServerExit.EnumerateExtensionsClose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'EnumerateExtensionsClose', ()))
    ICertServerExit.EnumerateAttributesSetup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'EnumerateAttributesSetup', ((1, 'Flags'),)))
    ICertServerExit.EnumerateAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'EnumerateAttributes', ((1, 'pstrAttributeName'),)))
    ICertServerExit.EnumerateAttributesClose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'EnumerateAttributesClose', ()))
    win32more.System.Com.IDispatch
    return ICertServerExit
def _define_ICertGetConfig_head():
    class ICertGetConfig(win32more.System.Com.IDispatch_head):
        Guid = Guid('c7ea09c0-ce17-11d0-8833-00a0c903b83c')
    return ICertGetConfig
def _define_ICertGetConfig():
    ICertGetConfig = win32more.Security.Cryptography.Certificates.ICertGetConfig_head
    ICertGetConfig.GetConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CERT_GET_CONFIG_FLAGS,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetConfig', ((1, 'Flags'),(1, 'pstrOut'),)))
    win32more.System.Com.IDispatch
    return ICertGetConfig
def _define_ICertConfig_head():
    class ICertConfig(win32more.System.Com.IDispatch_head):
        Guid = Guid('372fce34-4324-11d0-8810-00a0c903b83c')
    return ICertConfig
def _define_ICertConfig():
    ICertConfig = win32more.Security.Cryptography.Certificates.ICertConfig_head
    ICertConfig.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(7, 'Reset', ((1, 'Index'),(1, 'pCount'),)))
    ICertConfig.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'Next', ((1, 'pIndex'),)))
    ICertConfig.GetField = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetField', ((1, 'strFieldName'),(1, 'pstrOut'),)))
    ICertConfig.GetConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetConfig', ((1, 'Flags'),(1, 'pstrOut'),)))
    win32more.System.Com.IDispatch
    return ICertConfig
def _define_ICertConfig2_head():
    class ICertConfig2(win32more.Security.Cryptography.Certificates.ICertConfig_head):
        Guid = Guid('7a18edde-7e78-4163-8ded-78e2c9cee924')
    return ICertConfig2
def _define_ICertConfig2():
    ICertConfig2 = win32more.Security.Cryptography.Certificates.ICertConfig2_head
    ICertConfig2.SetSharedFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'SetSharedFolder', ((1, 'strSharedFolder'),)))
    win32more.Security.Cryptography.Certificates.ICertConfig
    return ICertConfig2
def _define_ICertRequest_head():
    class ICertRequest(win32more.System.Com.IDispatch_head):
        Guid = Guid('014e4840-5523-11d0-8812-00a0c903b83c')
    return ICertRequest
def _define_ICertRequest():
    ICertRequest = win32more.Security.Cryptography.Certificates.ICertRequest_head
    ICertRequest.Submit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(7, 'Submit', ((1, 'Flags'),(1, 'strRequest'),(1, 'strAttributes'),(1, 'strConfig'),(1, 'pDisposition'),)))
    ICertRequest.RetrievePending = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(8, 'RetrievePending', ((1, 'RequestId'),(1, 'strConfig'),(1, 'pDisposition'),)))
    ICertRequest.GetLastStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'GetLastStatus', ((1, 'pStatus'),)))
    ICertRequest.GetRequestId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'GetRequestId', ((1, 'pRequestId'),)))
    ICertRequest.GetDispositionMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetDispositionMessage', ((1, 'pstrDispositionMessage'),)))
    ICertRequest.GetCACertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'GetCACertificate', ((1, 'fExchangeCertificate'),(1, 'strConfig'),(1, 'Flags'),(1, 'pstrCertificate'),)))
    ICertRequest.GetCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'GetCertificate', ((1, 'Flags'),(1, 'pstrCertificate'),)))
    win32more.System.Com.IDispatch
    return ICertRequest
def _define_ICertRequest2_head():
    class ICertRequest2(win32more.Security.Cryptography.Certificates.ICertRequest_head):
        Guid = Guid('a4772988-4a85-4fa9-824e-b5cf5c16405a')
    return ICertRequest2
def _define_ICertRequest2():
    ICertRequest2 = win32more.Security.Cryptography.Certificates.ICertRequest2_head
    ICertRequest2.GetIssuedCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,POINTER(win32more.Security.Cryptography.Certificates.CR_DISP), use_last_error=False)(14, 'GetIssuedCertificate', ((1, 'strConfig'),(1, 'RequestId'),(1, 'strSerialNumber'),(1, 'pDisposition'),)))
    ICertRequest2.GetErrorMessageText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'GetErrorMessageText', ((1, 'hrMessage'),(1, 'Flags'),(1, 'pstrErrorMessageText'),)))
    ICertRequest2.GetCAProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(16, 'GetCAProperty', ((1, 'strConfig'),(1, 'PropId'),(1, 'PropIndex'),(1, 'PropType'),(1, 'Flags'),(1, 'pvarPropertyValue'),)))
    ICertRequest2.GetCAPropertyFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(Int32), use_last_error=False)(17, 'GetCAPropertyFlags', ((1, 'strConfig'),(1, 'PropId'),(1, 'pPropFlags'),)))
    ICertRequest2.GetCAPropertyDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'GetCAPropertyDisplayName', ((1, 'strConfig'),(1, 'PropId'),(1, 'pstrDisplayName'),)))
    ICertRequest2.GetFullResponseProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.FULL_RESPONSE_PROPERTY_ID,Int32,win32more.Security.Cryptography.Certificates.CERT_PROPERTY_TYPE,win32more.Security.Cryptography.Certificates.CERT_REQUEST_OUT_TYPE,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(19, 'GetFullResponseProperty', ((1, 'PropId'),(1, 'PropIndex'),(1, 'PropType'),(1, 'Flags'),(1, 'pvarPropertyValue'),)))
    win32more.Security.Cryptography.Certificates.ICertRequest
    return ICertRequest2
X509EnrollmentAuthFlags = Int32
X509EnrollmentAuthFlags_X509AuthNone = 0
X509EnrollmentAuthFlags_X509AuthAnonymous = 1
X509EnrollmentAuthFlags_X509AuthKerberos = 2
X509EnrollmentAuthFlags_X509AuthUsername = 4
X509EnrollmentAuthFlags_X509AuthCertificate = 8
def _define_ICertRequest3_head():
    class ICertRequest3(win32more.Security.Cryptography.Certificates.ICertRequest2_head):
        Guid = Guid('afc8f92b-33a2-4861-bf36-2933b7cd67b3')
    return ICertRequest3
def _define_ICertRequest3():
    ICertRequest3 = win32more.Security.Cryptography.Certificates.ICertRequest3_head
    ICertRequest3.SetCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(20, 'SetCredential', ((1, 'hWnd'),(1, 'AuthType'),(1, 'strCredential'),(1, 'strPassword'),)))
    ICertRequest3.GetRequestIdString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'GetRequestIdString', ((1, 'pstrRequestId'),)))
    ICertRequest3.GetIssuedCertificate2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Security.Cryptography.Certificates.CR_DISP), use_last_error=False)(22, 'GetIssuedCertificate2', ((1, 'strConfig'),(1, 'strRequestId'),(1, 'strSerialNumber'),(1, 'pDisposition'),)))
    ICertRequest3.GetRefreshPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(23, 'GetRefreshPolicy', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.ICertRequest2
    return ICertRequest3
CCertEncodeStringArray = Guid('19a76fe0-7494-11d0-8816-00a0c903b83c')
CCertEncodeLongArray = Guid('4e0680a0-a0a2-11d0-8821-00a0c903b83c')
CCertEncodeDateArray = Guid('301f77b0-a470-11d0-8821-00a0c903b83c')
CCertEncodeCRLDistInfo = Guid('01fa60a0-bbff-11d0-8825-00a0c903b83c')
CCertEncodeAltName = Guid('1cfc4cda-1271-11d1-9bd4-00c04fb683fa')
CCertEncodeBitString = Guid('6d6b3cd8-1278-11d1-9bd4-00c04fb683fa')
CObjectId = Guid('884e2000-217d-11da-b2a4-000e7bbb2b09')
CObjectIds = Guid('884e2001-217d-11da-b2a4-000e7bbb2b09')
CBinaryConverter = Guid('884e2002-217d-11da-b2a4-000e7bbb2b09')
CX500DistinguishedName = Guid('884e2003-217d-11da-b2a4-000e7bbb2b09')
CCspInformation = Guid('884e2007-217d-11da-b2a4-000e7bbb2b09')
CCspInformations = Guid('884e2008-217d-11da-b2a4-000e7bbb2b09')
CCspStatus = Guid('884e2009-217d-11da-b2a4-000e7bbb2b09')
CX509PublicKey = Guid('884e200b-217d-11da-b2a4-000e7bbb2b09')
CX509PrivateKey = Guid('884e200c-217d-11da-b2a4-000e7bbb2b09')
CX509EndorsementKey = Guid('11a25a1d-b9a3-4edd-af83-3b59adbed361')
CX509Extension = Guid('884e200d-217d-11da-b2a4-000e7bbb2b09')
CX509Extensions = Guid('884e200e-217d-11da-b2a4-000e7bbb2b09')
CX509ExtensionKeyUsage = Guid('884e200f-217d-11da-b2a4-000e7bbb2b09')
CX509ExtensionEnhancedKeyUsage = Guid('884e2010-217d-11da-b2a4-000e7bbb2b09')
CX509ExtensionTemplateName = Guid('884e2011-217d-11da-b2a4-000e7bbb2b09')
CX509ExtensionTemplate = Guid('884e2012-217d-11da-b2a4-000e7bbb2b09')
CAlternativeName = Guid('884e2013-217d-11da-b2a4-000e7bbb2b09')
CAlternativeNames = Guid('884e2014-217d-11da-b2a4-000e7bbb2b09')
CX509ExtensionAlternativeNames = Guid('884e2015-217d-11da-b2a4-000e7bbb2b09')
CX509ExtensionBasicConstraints = Guid('884e2016-217d-11da-b2a4-000e7bbb2b09')
CX509ExtensionSubjectKeyIdentifier = Guid('884e2017-217d-11da-b2a4-000e7bbb2b09')
CX509ExtensionAuthorityKeyIdentifier = Guid('884e2018-217d-11da-b2a4-000e7bbb2b09')
CSmimeCapability = Guid('884e2019-217d-11da-b2a4-000e7bbb2b09')
CSmimeCapabilities = Guid('884e201a-217d-11da-b2a4-000e7bbb2b09')
CX509ExtensionSmimeCapabilities = Guid('884e201b-217d-11da-b2a4-000e7bbb2b09')
CPolicyQualifier = Guid('884e201c-217d-11da-b2a4-000e7bbb2b09')
CPolicyQualifiers = Guid('884e201d-217d-11da-b2a4-000e7bbb2b09')
CCertificatePolicy = Guid('884e201e-217d-11da-b2a4-000e7bbb2b09')
CCertificatePolicies = Guid('884e201f-217d-11da-b2a4-000e7bbb2b09')
CX509ExtensionCertificatePolicies = Guid('884e2020-217d-11da-b2a4-000e7bbb2b09')
CX509ExtensionMSApplicationPolicies = Guid('884e2021-217d-11da-b2a4-000e7bbb2b09')
CX509Attribute = Guid('884e2022-217d-11da-b2a4-000e7bbb2b09')
CX509Attributes = Guid('884e2023-217d-11da-b2a4-000e7bbb2b09')
CX509AttributeExtensions = Guid('884e2024-217d-11da-b2a4-000e7bbb2b09')
CX509AttributeClientId = Guid('884e2025-217d-11da-b2a4-000e7bbb2b09')
CX509AttributeRenewalCertificate = Guid('884e2026-217d-11da-b2a4-000e7bbb2b09')
CX509AttributeArchiveKey = Guid('884e2027-217d-11da-b2a4-000e7bbb2b09')
CX509AttributeArchiveKeyHash = Guid('884e2028-217d-11da-b2a4-000e7bbb2b09')
CX509AttributeOSVersion = Guid('884e202a-217d-11da-b2a4-000e7bbb2b09')
CX509AttributeCspProvider = Guid('884e202b-217d-11da-b2a4-000e7bbb2b09')
CCryptAttribute = Guid('884e202c-217d-11da-b2a4-000e7bbb2b09')
CCryptAttributes = Guid('884e202d-217d-11da-b2a4-000e7bbb2b09')
CCertProperty = Guid('884e202e-217d-11da-b2a4-000e7bbb2b09')
CCertProperties = Guid('884e202f-217d-11da-b2a4-000e7bbb2b09')
CCertPropertyFriendlyName = Guid('884e2030-217d-11da-b2a4-000e7bbb2b09')
CCertPropertyDescription = Guid('884e2031-217d-11da-b2a4-000e7bbb2b09')
CCertPropertyAutoEnroll = Guid('884e2032-217d-11da-b2a4-000e7bbb2b09')
CCertPropertyRequestOriginator = Guid('884e2033-217d-11da-b2a4-000e7bbb2b09')
CCertPropertySHA1Hash = Guid('884e2034-217d-11da-b2a4-000e7bbb2b09')
CCertPropertyKeyProvInfo = Guid('884e2036-217d-11da-b2a4-000e7bbb2b09')
CCertPropertyArchived = Guid('884e2037-217d-11da-b2a4-000e7bbb2b09')
CCertPropertyBackedUp = Guid('884e2038-217d-11da-b2a4-000e7bbb2b09')
CCertPropertyEnrollment = Guid('884e2039-217d-11da-b2a4-000e7bbb2b09')
CCertPropertyRenewal = Guid('884e203a-217d-11da-b2a4-000e7bbb2b09')
CCertPropertyArchivedKeyHash = Guid('884e203b-217d-11da-b2a4-000e7bbb2b09')
CCertPropertyEnrollmentPolicyServer = Guid('884e204c-217d-11da-b2a4-000e7bbb2b09')
CSignerCertificate = Guid('884e203d-217d-11da-b2a4-000e7bbb2b09')
CX509NameValuePair = Guid('884e203f-217d-11da-b2a4-000e7bbb2b09')
CCertificateAttestationChallenge = Guid('1362ada1-eb60-456a-b6e1-118050db741b')
CX509CertificateRequestPkcs10 = Guid('884e2042-217d-11da-b2a4-000e7bbb2b09')
CX509CertificateRequestCertificate = Guid('884e2043-217d-11da-b2a4-000e7bbb2b09')
CX509CertificateRequestPkcs7 = Guid('884e2044-217d-11da-b2a4-000e7bbb2b09')
CX509CertificateRequestCmc = Guid('884e2045-217d-11da-b2a4-000e7bbb2b09')
CX509Enrollment = Guid('884e2046-217d-11da-b2a4-000e7bbb2b09')
CX509EnrollmentWebClassFactory = Guid('884e2049-217d-11da-b2a4-000e7bbb2b09')
CX509EnrollmentHelper = Guid('884e2050-217d-11da-b2a4-000e7bbb2b09')
CX509MachineEnrollmentFactory = Guid('884e2051-217d-11da-b2a4-000e7bbb2b09')
CX509EnrollmentPolicyActiveDirectory = Guid('91f39027-217f-11da-b2a4-000e7bbb2b09')
CX509EnrollmentPolicyWebService = Guid('91f39028-217f-11da-b2a4-000e7bbb2b09')
CX509PolicyServerListManager = Guid('91f39029-217f-11da-b2a4-000e7bbb2b09')
CX509PolicyServerUrl = Guid('91f3902a-217f-11da-b2a4-000e7bbb2b09')
CX509CertificateTemplateADWritable = Guid('8336e323-2e6a-4a04-937c-548f681839b3')
CX509CertificateRevocationListEntry = Guid('884e205e-217d-11da-b2a4-000e7bbb2b09')
CX509CertificateRevocationListEntries = Guid('884e205f-217d-11da-b2a4-000e7bbb2b09')
CX509CertificateRevocationList = Guid('884e2060-217d-11da-b2a4-000e7bbb2b09')
CX509SCEPEnrollment = Guid('884e2061-217d-11da-b2a4-000e7bbb2b09')
CX509SCEPEnrollmentHelper = Guid('884e2062-217d-11da-b2a4-000e7bbb2b09')
def _define_ICertManageModule_head():
    class ICertManageModule(win32more.System.Com.IDispatch_head):
        Guid = Guid('e7d7ad42-bd3d-11d1-9a4d-00c04fc297eb')
    return ICertManageModule
def _define_ICertManageModule():
    ICertManageModule = win32more.Security.Cryptography.Certificates.ICertManageModule_head
    ICertManageModule.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'GetProperty', ((1, 'strConfig'),(1, 'strStorageLocation'),(1, 'strPropertyName'),(1, 'Flags'),(1, 'pvarProperty'),)))
    ICertManageModule.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'SetProperty', ((1, 'strConfig'),(1, 'strStorageLocation'),(1, 'strPropertyName'),(1, 'Flags'),(1, 'pvarProperty'),)))
    ICertManageModule.Configure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32, use_last_error=False)(9, 'Configure', ((1, 'strConfig'),(1, 'strStorageLocation'),(1, 'Flags'),)))
    win32more.System.Com.IDispatch
    return ICertManageModule
def _define_CERTTRANSBLOB_head():
    class CERTTRANSBLOB(Structure):
        pass
    return CERTTRANSBLOB
def _define_CERTTRANSBLOB():
    CERTTRANSBLOB = win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head
    CERTTRANSBLOB._fields_ = [
        ("cb", UInt32),
        ("pb", c_char_p_no),
    ]
    return CERTTRANSBLOB
def _define_CERTVIEWRESTRICTION_head():
    class CERTVIEWRESTRICTION(Structure):
        pass
    return CERTVIEWRESTRICTION
def _define_CERTVIEWRESTRICTION():
    CERTVIEWRESTRICTION = win32more.Security.Cryptography.Certificates.CERTVIEWRESTRICTION_head
    CERTVIEWRESTRICTION._fields_ = [
        ("ColumnIndex", UInt32),
        ("SeekOperator", Int32),
        ("SortOrder", Int32),
        ("pbValue", c_char_p_no),
        ("cbValue", UInt32),
    ]
    return CERTVIEWRESTRICTION
def _define_ICertPolicy_head():
    class ICertPolicy(win32more.System.Com.IDispatch_head):
        Guid = Guid('38bb5a00-7636-11d0-b413-00a0c91bbf8c')
    return ICertPolicy
def _define_ICertPolicy():
    ICertPolicy = win32more.Security.Cryptography.Certificates.ICertPolicy_head
    ICertPolicy.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'Initialize', ((1, 'strConfig'),)))
    ICertPolicy.VerifyRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,Int32,POINTER(Int32), use_last_error=False)(8, 'VerifyRequest', ((1, 'strConfig'),(1, 'Context'),(1, 'bNewRequest'),(1, 'Flags'),(1, 'pDisposition'),)))
    ICertPolicy.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetDescription', ((1, 'pstrDescription'),)))
    ICertPolicy.ShutDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'ShutDown', ()))
    win32more.System.Com.IDispatch
    return ICertPolicy
def _define_ICertPolicy2_head():
    class ICertPolicy2(win32more.Security.Cryptography.Certificates.ICertPolicy_head):
        Guid = Guid('3db4910e-8001-4bf1-aa1b-f43a808317a0')
    return ICertPolicy2
def _define_ICertPolicy2():
    ICertPolicy2 = win32more.Security.Cryptography.Certificates.ICertPolicy2_head
    ICertPolicy2.GetManageModule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICertManageModule_head), use_last_error=False)(11, 'GetManageModule', ((1, 'ppManageModule'),)))
    win32more.Security.Cryptography.Certificates.ICertPolicy
    return ICertPolicy2
X509SCEPMessageType = Int32
X509SCEPMessageType_SCEPMessageUnknown = -1
X509SCEPMessageType_SCEPMessageCertResponse = 3
X509SCEPMessageType_SCEPMessagePKCSRequest = 19
X509SCEPMessageType_SCEPMessageGetCertInitial = 20
X509SCEPMessageType_SCEPMessageGetCert = 21
X509SCEPMessageType_SCEPMessageGetCRL = 22
X509SCEPMessageType_SCEPMessageClaimChallengeAnswer = 41
X509SCEPDisposition = Int32
X509SCEPDisposition_SCEPDispositionUnknown = -1
X509SCEPDisposition_SCEPDispositionSuccess = 0
X509SCEPDisposition_SCEPDispositionFailure = 2
X509SCEPDisposition_SCEPDispositionPending = 3
X509SCEPDisposition_SCEPDispositionPendingChallenge = 11
X509SCEPFailInfo = Int32
X509SCEPFailInfo_SCEPFailUnknown = -1
X509SCEPFailInfo_SCEPFailBadAlgorithm = 0
X509SCEPFailInfo_SCEPFailBadMessageCheck = 1
X509SCEPFailInfo_SCEPFailBadRequest = 2
X509SCEPFailInfo_SCEPFailBadTime = 3
X509SCEPFailInfo_SCEPFailBadCertId = 4
def _define_INDESPolicy_head():
    class INDESPolicy(win32more.System.Com.IUnknown_head):
        Guid = Guid('13ca515d-431d-46cc-8c2e-1da269bbd625')
    return INDESPolicy
def _define_INDESPolicy():
    INDESPolicy = win32more.Security.Cryptography.Certificates.INDESPolicy_head
    INDESPolicy.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Initialize', ()))
    INDESPolicy.Uninitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Uninitialize', ()))
    INDESPolicy.GenerateChallenge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GenerateChallenge', ((1, 'pwszTemplate'),(1, 'pwszParams'),(1, 'ppwszResponse'),)))
    INDESPolicy.VerifyRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head),POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'VerifyRequest', ((1, 'pctbRequest'),(1, 'pctbSigningCertEncoded'),(1, 'pwszTemplate'),(1, 'pwszTransactionId'),(1, 'pfVerified'),)))
    INDESPolicy.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Security.Cryptography.Certificates.X509SCEPDisposition,Int32,POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head), use_last_error=False)(7, 'Notify', ((1, 'pwszChallenge'),(1, 'pwszTransactionId'),(1, 'disposition'),(1, 'lastHResult'),(1, 'pctbIssuedCertEncoded'),)))
    win32more.System.Com.IUnknown
    return INDESPolicy
CERTENROLL_OBJECTID = Int32
XCN_OID_NONE = 0
XCN_OID_RSA = 1
XCN_OID_PKCS = 2
XCN_OID_RSA_HASH = 3
XCN_OID_RSA_ENCRYPT = 4
XCN_OID_PKCS_1 = 5
XCN_OID_PKCS_2 = 6
XCN_OID_PKCS_3 = 7
XCN_OID_PKCS_4 = 8
XCN_OID_PKCS_5 = 9
XCN_OID_PKCS_6 = 10
XCN_OID_PKCS_7 = 11
XCN_OID_PKCS_8 = 12
XCN_OID_PKCS_9 = 13
XCN_OID_PKCS_10 = 14
XCN_OID_PKCS_12 = 15
XCN_OID_RSA_RSA = 16
XCN_OID_RSA_MD2RSA = 17
XCN_OID_RSA_MD4RSA = 18
XCN_OID_RSA_MD5RSA = 19
XCN_OID_RSA_SHA1RSA = 20
XCN_OID_RSA_SETOAEP_RSA = 21
XCN_OID_RSA_DH = 22
XCN_OID_RSA_data = 23
XCN_OID_RSA_signedData = 24
XCN_OID_RSA_envelopedData = 25
XCN_OID_RSA_signEnvData = 26
XCN_OID_RSA_digestedData = 27
XCN_OID_RSA_hashedData = 28
XCN_OID_RSA_encryptedData = 29
XCN_OID_RSA_emailAddr = 30
XCN_OID_RSA_unstructName = 31
XCN_OID_RSA_contentType = 32
XCN_OID_RSA_messageDigest = 33
XCN_OID_RSA_signingTime = 34
XCN_OID_RSA_counterSign = 35
XCN_OID_RSA_challengePwd = 36
XCN_OID_RSA_unstructAddr = 37
XCN_OID_RSA_extCertAttrs = 38
XCN_OID_RSA_certExtensions = 39
XCN_OID_RSA_SMIMECapabilities = 40
XCN_OID_RSA_preferSignedData = 41
XCN_OID_RSA_SMIMEalg = 42
XCN_OID_RSA_SMIMEalgESDH = 43
XCN_OID_RSA_SMIMEalgCMS3DESwrap = 44
XCN_OID_RSA_SMIMEalgCMSRC2wrap = 45
XCN_OID_RSA_MD2 = 46
XCN_OID_RSA_MD4 = 47
XCN_OID_RSA_MD5 = 48
XCN_OID_RSA_RC2CBC = 49
XCN_OID_RSA_RC4 = 50
XCN_OID_RSA_DES_EDE3_CBC = 51
XCN_OID_RSA_RC5_CBCPad = 52
XCN_OID_ANSI_X942 = 53
XCN_OID_ANSI_X942_DH = 54
XCN_OID_X957 = 55
XCN_OID_X957_DSA = 56
XCN_OID_X957_SHA1DSA = 57
XCN_OID_DS = 58
XCN_OID_DSALG = 59
XCN_OID_DSALG_CRPT = 60
XCN_OID_DSALG_HASH = 61
XCN_OID_DSALG_SIGN = 62
XCN_OID_DSALG_RSA = 63
XCN_OID_OIW = 64
XCN_OID_OIWSEC = 65
XCN_OID_OIWSEC_md4RSA = 66
XCN_OID_OIWSEC_md5RSA = 67
XCN_OID_OIWSEC_md4RSA2 = 68
XCN_OID_OIWSEC_desECB = 69
XCN_OID_OIWSEC_desCBC = 70
XCN_OID_OIWSEC_desOFB = 71
XCN_OID_OIWSEC_desCFB = 72
XCN_OID_OIWSEC_desMAC = 73
XCN_OID_OIWSEC_rsaSign = 74
XCN_OID_OIWSEC_dsa = 75
XCN_OID_OIWSEC_shaDSA = 76
XCN_OID_OIWSEC_mdc2RSA = 77
XCN_OID_OIWSEC_shaRSA = 78
XCN_OID_OIWSEC_dhCommMod = 79
XCN_OID_OIWSEC_desEDE = 80
XCN_OID_OIWSEC_sha = 81
XCN_OID_OIWSEC_mdc2 = 82
XCN_OID_OIWSEC_dsaComm = 83
XCN_OID_OIWSEC_dsaCommSHA = 84
XCN_OID_OIWSEC_rsaXchg = 85
XCN_OID_OIWSEC_keyHashSeal = 86
XCN_OID_OIWSEC_md2RSASign = 87
XCN_OID_OIWSEC_md5RSASign = 88
XCN_OID_OIWSEC_sha1 = 89
XCN_OID_OIWSEC_dsaSHA1 = 90
XCN_OID_OIWSEC_dsaCommSHA1 = 91
XCN_OID_OIWSEC_sha1RSASign = 92
XCN_OID_OIWDIR = 93
XCN_OID_OIWDIR_CRPT = 94
XCN_OID_OIWDIR_HASH = 95
XCN_OID_OIWDIR_SIGN = 96
XCN_OID_OIWDIR_md2 = 97
XCN_OID_OIWDIR_md2RSA = 98
XCN_OID_INFOSEC = 99
XCN_OID_INFOSEC_sdnsSignature = 100
XCN_OID_INFOSEC_mosaicSignature = 101
XCN_OID_INFOSEC_sdnsConfidentiality = 102
XCN_OID_INFOSEC_mosaicConfidentiality = 103
XCN_OID_INFOSEC_sdnsIntegrity = 104
XCN_OID_INFOSEC_mosaicIntegrity = 105
XCN_OID_INFOSEC_sdnsTokenProtection = 106
XCN_OID_INFOSEC_mosaicTokenProtection = 107
XCN_OID_INFOSEC_sdnsKeyManagement = 108
XCN_OID_INFOSEC_mosaicKeyManagement = 109
XCN_OID_INFOSEC_sdnsKMandSig = 110
XCN_OID_INFOSEC_mosaicKMandSig = 111
XCN_OID_INFOSEC_SuiteASignature = 112
XCN_OID_INFOSEC_SuiteAConfidentiality = 113
XCN_OID_INFOSEC_SuiteAIntegrity = 114
XCN_OID_INFOSEC_SuiteATokenProtection = 115
XCN_OID_INFOSEC_SuiteAKeyManagement = 116
XCN_OID_INFOSEC_SuiteAKMandSig = 117
XCN_OID_INFOSEC_mosaicUpdatedSig = 118
XCN_OID_INFOSEC_mosaicKMandUpdSig = 119
XCN_OID_INFOSEC_mosaicUpdatedInteg = 120
XCN_OID_COMMON_NAME = 121
XCN_OID_SUR_NAME = 122
XCN_OID_DEVICE_SERIAL_NUMBER = 123
XCN_OID_COUNTRY_NAME = 124
XCN_OID_LOCALITY_NAME = 125
XCN_OID_STATE_OR_PROVINCE_NAME = 126
XCN_OID_STREET_ADDRESS = 127
XCN_OID_ORGANIZATION_NAME = 128
XCN_OID_ORGANIZATIONAL_UNIT_NAME = 129
XCN_OID_TITLE = 130
XCN_OID_DESCRIPTION = 131
XCN_OID_SEARCH_GUIDE = 132
XCN_OID_BUSINESS_CATEGORY = 133
XCN_OID_POSTAL_ADDRESS = 134
XCN_OID_POSTAL_CODE = 135
XCN_OID_POST_OFFICE_BOX = 136
XCN_OID_PHYSICAL_DELIVERY_OFFICE_NAME = 137
XCN_OID_TELEPHONE_NUMBER = 138
XCN_OID_TELEX_NUMBER = 139
XCN_OID_TELETEXT_TERMINAL_IDENTIFIER = 140
XCN_OID_FACSIMILE_TELEPHONE_NUMBER = 141
XCN_OID_X21_ADDRESS = 142
XCN_OID_INTERNATIONAL_ISDN_NUMBER = 143
XCN_OID_REGISTERED_ADDRESS = 144
XCN_OID_DESTINATION_INDICATOR = 145
XCN_OID_PREFERRED_DELIVERY_METHOD = 146
XCN_OID_PRESENTATION_ADDRESS = 147
XCN_OID_SUPPORTED_APPLICATION_CONTEXT = 148
XCN_OID_MEMBER = 149
XCN_OID_OWNER = 150
XCN_OID_ROLE_OCCUPANT = 151
XCN_OID_SEE_ALSO = 152
XCN_OID_USER_PASSWORD = 153
XCN_OID_USER_CERTIFICATE = 154
XCN_OID_CA_CERTIFICATE = 155
XCN_OID_AUTHORITY_REVOCATION_LIST = 156
XCN_OID_CERTIFICATE_REVOCATION_LIST = 157
XCN_OID_CROSS_CERTIFICATE_PAIR = 158
XCN_OID_GIVEN_NAME = 159
XCN_OID_INITIALS = 160
XCN_OID_DN_QUALIFIER = 161
XCN_OID_DOMAIN_COMPONENT = 162
XCN_OID_PKCS_12_FRIENDLY_NAME_ATTR = 163
XCN_OID_PKCS_12_LOCAL_KEY_ID = 164
XCN_OID_PKCS_12_KEY_PROVIDER_NAME_ATTR = 165
XCN_OID_LOCAL_MACHINE_KEYSET = 166
XCN_OID_PKCS_12_EXTENDED_ATTRIBUTES = 167
XCN_OID_KEYID_RDN = 168
XCN_OID_AUTHORITY_KEY_IDENTIFIER = 169
XCN_OID_KEY_ATTRIBUTES = 170
XCN_OID_CERT_POLICIES_95 = 171
XCN_OID_KEY_USAGE_RESTRICTION = 172
XCN_OID_SUBJECT_ALT_NAME = 173
XCN_OID_ISSUER_ALT_NAME = 174
XCN_OID_BASIC_CONSTRAINTS = 175
XCN_OID_KEY_USAGE = 176
XCN_OID_PRIVATEKEY_USAGE_PERIOD = 177
XCN_OID_BASIC_CONSTRAINTS2 = 178
XCN_OID_CERT_POLICIES = 179
XCN_OID_ANY_CERT_POLICY = 180
XCN_OID_AUTHORITY_KEY_IDENTIFIER2 = 181
XCN_OID_SUBJECT_KEY_IDENTIFIER = 182
XCN_OID_SUBJECT_ALT_NAME2 = 183
XCN_OID_ISSUER_ALT_NAME2 = 184
XCN_OID_CRL_REASON_CODE = 185
XCN_OID_REASON_CODE_HOLD = 186
XCN_OID_CRL_DIST_POINTS = 187
XCN_OID_ENHANCED_KEY_USAGE = 188
XCN_OID_CRL_NUMBER = 189
XCN_OID_DELTA_CRL_INDICATOR = 190
XCN_OID_ISSUING_DIST_POINT = 191
XCN_OID_FRESHEST_CRL = 192
XCN_OID_NAME_CONSTRAINTS = 193
XCN_OID_POLICY_MAPPINGS = 194
XCN_OID_LEGACY_POLICY_MAPPINGS = 195
XCN_OID_POLICY_CONSTRAINTS = 196
XCN_OID_RENEWAL_CERTIFICATE = 197
XCN_OID_ENROLLMENT_NAME_VALUE_PAIR = 198
XCN_OID_ENROLLMENT_CSP_PROVIDER = 199
XCN_OID_OS_VERSION = 200
XCN_OID_ENROLLMENT_AGENT = 201
XCN_OID_PKIX = 202
XCN_OID_PKIX_PE = 203
XCN_OID_AUTHORITY_INFO_ACCESS = 204
XCN_OID_BIOMETRIC_EXT = 205
XCN_OID_LOGOTYPE_EXT = 206
XCN_OID_CERT_EXTENSIONS = 207
XCN_OID_NEXT_UPDATE_LOCATION = 208
XCN_OID_REMOVE_CERTIFICATE = 209
XCN_OID_CROSS_CERT_DIST_POINTS = 210
XCN_OID_CTL = 211
XCN_OID_SORTED_CTL = 212
XCN_OID_SERIALIZED = 213
XCN_OID_NT_PRINCIPAL_NAME = 214
XCN_OID_PRODUCT_UPDATE = 215
XCN_OID_ANY_APPLICATION_POLICY = 216
XCN_OID_AUTO_ENROLL_CTL_USAGE = 217
XCN_OID_ENROLL_CERTTYPE_EXTENSION = 218
XCN_OID_CERT_MANIFOLD = 219
XCN_OID_CERTSRV_CA_VERSION = 220
XCN_OID_CERTSRV_PREVIOUS_CERT_HASH = 221
XCN_OID_CRL_VIRTUAL_BASE = 222
XCN_OID_CRL_NEXT_PUBLISH = 223
XCN_OID_KP_CA_EXCHANGE = 224
XCN_OID_KP_KEY_RECOVERY_AGENT = 225
XCN_OID_CERTIFICATE_TEMPLATE = 226
XCN_OID_ENTERPRISE_OID_ROOT = 227
XCN_OID_RDN_DUMMY_SIGNER = 228
XCN_OID_APPLICATION_CERT_POLICIES = 229
XCN_OID_APPLICATION_POLICY_MAPPINGS = 230
XCN_OID_APPLICATION_POLICY_CONSTRAINTS = 231
XCN_OID_ARCHIVED_KEY_ATTR = 232
XCN_OID_CRL_SELF_CDP = 233
XCN_OID_REQUIRE_CERT_CHAIN_POLICY = 234
XCN_OID_ARCHIVED_KEY_CERT_HASH = 235
XCN_OID_ISSUED_CERT_HASH = 236
XCN_OID_DS_EMAIL_REPLICATION = 237
XCN_OID_REQUEST_CLIENT_INFO = 238
XCN_OID_ENCRYPTED_KEY_HASH = 239
XCN_OID_CERTSRV_CROSSCA_VERSION = 240
XCN_OID_NTDS_REPLICATION = 241
XCN_OID_SUBJECT_DIR_ATTRS = 242
XCN_OID_PKIX_KP = 243
XCN_OID_PKIX_KP_SERVER_AUTH = 244
XCN_OID_PKIX_KP_CLIENT_AUTH = 245
XCN_OID_PKIX_KP_CODE_SIGNING = 246
XCN_OID_PKIX_KP_EMAIL_PROTECTION = 247
XCN_OID_PKIX_KP_IPSEC_END_SYSTEM = 248
XCN_OID_PKIX_KP_IPSEC_TUNNEL = 249
XCN_OID_PKIX_KP_IPSEC_USER = 250
XCN_OID_PKIX_KP_TIMESTAMP_SIGNING = 251
XCN_OID_PKIX_KP_OCSP_SIGNING = 252
XCN_OID_PKIX_OCSP_NOCHECK = 253
XCN_OID_IPSEC_KP_IKE_INTERMEDIATE = 254
XCN_OID_KP_CTL_USAGE_SIGNING = 255
XCN_OID_KP_TIME_STAMP_SIGNING = 256
XCN_OID_SERVER_GATED_CRYPTO = 257
XCN_OID_SGC_NETSCAPE = 258
XCN_OID_KP_EFS = 259
XCN_OID_EFS_RECOVERY = 260
XCN_OID_WHQL_CRYPTO = 261
XCN_OID_NT5_CRYPTO = 262
XCN_OID_OEM_WHQL_CRYPTO = 263
XCN_OID_EMBEDDED_NT_CRYPTO = 264
XCN_OID_ROOT_LIST_SIGNER = 265
XCN_OID_KP_QUALIFIED_SUBORDINATION = 266
XCN_OID_KP_KEY_RECOVERY = 267
XCN_OID_KP_DOCUMENT_SIGNING = 268
XCN_OID_KP_LIFETIME_SIGNING = 269
XCN_OID_KP_MOBILE_DEVICE_SOFTWARE = 270
XCN_OID_KP_SMART_DISPLAY = 271
XCN_OID_KP_CSP_SIGNATURE = 272
XCN_OID_DRM = 273
XCN_OID_DRM_INDIVIDUALIZATION = 274
XCN_OID_LICENSES = 275
XCN_OID_LICENSE_SERVER = 276
XCN_OID_KP_SMARTCARD_LOGON = 277
XCN_OID_YESNO_TRUST_ATTR = 278
XCN_OID_PKIX_POLICY_QUALIFIER_CPS = 279
XCN_OID_PKIX_POLICY_QUALIFIER_USERNOTICE = 280
XCN_OID_CERT_POLICIES_95_QUALIFIER1 = 281
XCN_OID_PKIX_ACC_DESCR = 282
XCN_OID_PKIX_OCSP = 283
XCN_OID_PKIX_CA_ISSUERS = 284
XCN_OID_VERISIGN_PRIVATE_6_9 = 285
XCN_OID_VERISIGN_ONSITE_JURISDICTION_HASH = 286
XCN_OID_VERISIGN_BITSTRING_6_13 = 287
XCN_OID_VERISIGN_ISS_STRONG_CRYPTO = 288
XCN_OID_NETSCAPE = 289
XCN_OID_NETSCAPE_CERT_EXTENSION = 290
XCN_OID_NETSCAPE_CERT_TYPE = 291
XCN_OID_NETSCAPE_BASE_URL = 292
XCN_OID_NETSCAPE_REVOCATION_URL = 293
XCN_OID_NETSCAPE_CA_REVOCATION_URL = 294
XCN_OID_NETSCAPE_CERT_RENEWAL_URL = 295
XCN_OID_NETSCAPE_CA_POLICY_URL = 296
XCN_OID_NETSCAPE_SSL_SERVER_NAME = 297
XCN_OID_NETSCAPE_COMMENT = 298
XCN_OID_NETSCAPE_DATA_TYPE = 299
XCN_OID_NETSCAPE_CERT_SEQUENCE = 300
XCN_OID_CT_PKI_DATA = 301
XCN_OID_CT_PKI_RESPONSE = 302
XCN_OID_PKIX_NO_SIGNATURE = 303
XCN_OID_CMC = 304
XCN_OID_CMC_STATUS_INFO = 305
XCN_OID_CMC_IDENTIFICATION = 306
XCN_OID_CMC_IDENTITY_PROOF = 307
XCN_OID_CMC_DATA_RETURN = 308
XCN_OID_CMC_TRANSACTION_ID = 309
XCN_OID_CMC_SENDER_NONCE = 310
XCN_OID_CMC_RECIPIENT_NONCE = 311
XCN_OID_CMC_ADD_EXTENSIONS = 312
XCN_OID_CMC_ENCRYPTED_POP = 313
XCN_OID_CMC_DECRYPTED_POP = 314
XCN_OID_CMC_LRA_POP_WITNESS = 315
XCN_OID_CMC_GET_CERT = 316
XCN_OID_CMC_GET_CRL = 317
XCN_OID_CMC_REVOKE_REQUEST = 318
XCN_OID_CMC_REG_INFO = 319
XCN_OID_CMC_RESPONSE_INFO = 320
XCN_OID_CMC_QUERY_PENDING = 321
XCN_OID_CMC_ID_POP_LINK_RANDOM = 322
XCN_OID_CMC_ID_POP_LINK_WITNESS = 323
XCN_OID_CMC_ID_CONFIRM_CERT_ACCEPTANCE = 324
XCN_OID_CMC_ADD_ATTRIBUTES = 325
XCN_OID_LOYALTY_OTHER_LOGOTYPE = 326
XCN_OID_BACKGROUND_OTHER_LOGOTYPE = 327
XCN_OID_PKIX_OCSP_BASIC_SIGNED_RESPONSE = 328
XCN_OID_PKCS_7_DATA = 329
XCN_OID_PKCS_7_SIGNED = 330
XCN_OID_PKCS_7_ENVELOPED = 331
XCN_OID_PKCS_7_SIGNEDANDENVELOPED = 332
XCN_OID_PKCS_7_DIGESTED = 333
XCN_OID_PKCS_7_ENCRYPTED = 334
XCN_OID_PKCS_9_CONTENT_TYPE = 335
XCN_OID_PKCS_9_MESSAGE_DIGEST = 336
XCN_OID_CERT_PROP_ID_PREFIX = 337
XCN_OID_CERT_KEY_IDENTIFIER_PROP_ID = 338
XCN_OID_CERT_ISSUER_SERIAL_NUMBER_MD5_HASH_PROP_ID = 339
XCN_OID_CERT_SUBJECT_NAME_MD5_HASH_PROP_ID = 340
XCN_OID_CERT_MD5_HASH_PROP_ID = 341
XCN_OID_RSA_SHA256RSA = 342
XCN_OID_RSA_SHA384RSA = 343
XCN_OID_RSA_SHA512RSA = 344
XCN_OID_NIST_sha256 = 345
XCN_OID_NIST_sha384 = 346
XCN_OID_NIST_sha512 = 347
XCN_OID_RSA_MGF1 = 348
XCN_OID_ECC_PUBLIC_KEY = 349
XCN_OID_ECDSA_SHA1 = 350
XCN_OID_ECDSA_SPECIFIED = 351
XCN_OID_ANY_ENHANCED_KEY_USAGE = 352
XCN_OID_RSA_SSA_PSS = 353
XCN_OID_ATTR_SUPPORTED_ALGORITHMS = 355
XCN_OID_ATTR_TPM_SECURITY_ASSERTIONS = 356
XCN_OID_ATTR_TPM_SPECIFICATION = 357
XCN_OID_CERT_DISALLOWED_FILETIME_PROP_ID = 358
XCN_OID_CERT_SIGNATURE_HASH_PROP_ID = 359
XCN_OID_CERT_STRONG_KEY_OS_1 = 360
XCN_OID_CERT_STRONG_KEY_OS_CURRENT = 361
XCN_OID_CERT_STRONG_KEY_OS_PREFIX = 362
XCN_OID_CERT_STRONG_SIGN_OS_1 = 363
XCN_OID_CERT_STRONG_SIGN_OS_CURRENT = 364
XCN_OID_CERT_STRONG_SIGN_OS_PREFIX = 365
XCN_OID_DH_SINGLE_PASS_STDDH_SHA1_KDF = 366
XCN_OID_DH_SINGLE_PASS_STDDH_SHA256_KDF = 367
XCN_OID_DH_SINGLE_PASS_STDDH_SHA384_KDF = 368
XCN_OID_DISALLOWED_HASH = 369
XCN_OID_DISALLOWED_LIST = 370
XCN_OID_ECC_CURVE_P256 = 371
XCN_OID_ECC_CURVE_P384 = 372
XCN_OID_ECC_CURVE_P521 = 373
XCN_OID_ECDSA_SHA256 = 374
XCN_OID_ECDSA_SHA384 = 375
XCN_OID_ECDSA_SHA512 = 376
XCN_OID_ENROLL_CAXCHGCERT_HASH = 377
XCN_OID_ENROLL_EK_INFO = 378
XCN_OID_ENROLL_EKPUB_CHALLENGE = 379
XCN_OID_ENROLL_EKVERIFYCERT = 380
XCN_OID_ENROLL_EKVERIFYCREDS = 381
XCN_OID_ENROLL_EKVERIFYKEY = 382
XCN_OID_EV_RDN_COUNTRY = 383
XCN_OID_EV_RDN_LOCALE = 384
XCN_OID_EV_RDN_STATE_OR_PROVINCE = 385
XCN_OID_INHIBIT_ANY_POLICY = 386
XCN_OID_INTERNATIONALIZED_EMAIL_ADDRESS = 387
XCN_OID_KP_KERNEL_MODE_CODE_SIGNING = 388
XCN_OID_KP_KERNEL_MODE_HAL_EXTENSION_SIGNING = 389
XCN_OID_KP_KERNEL_MODE_TRUSTED_BOOT_SIGNING = 390
XCN_OID_KP_TPM_AIK_CERTIFICATE = 391
XCN_OID_KP_TPM_EK_CERTIFICATE = 392
XCN_OID_KP_TPM_PLATFORM_CERTIFICATE = 393
XCN_OID_NIST_AES128_CBC = 394
XCN_OID_NIST_AES128_WRAP = 395
XCN_OID_NIST_AES192_CBC = 396
XCN_OID_NIST_AES192_WRAP = 397
XCN_OID_NIST_AES256_CBC = 398
XCN_OID_NIST_AES256_WRAP = 399
XCN_OID_PKCS_12_PbeIds = 400
XCN_OID_PKCS_12_pbeWithSHA1And128BitRC2 = 401
XCN_OID_PKCS_12_pbeWithSHA1And128BitRC4 = 402
XCN_OID_PKCS_12_pbeWithSHA1And2KeyTripleDES = 403
XCN_OID_PKCS_12_pbeWithSHA1And3KeyTripleDES = 404
XCN_OID_PKCS_12_pbeWithSHA1And40BitRC2 = 405
XCN_OID_PKCS_12_pbeWithSHA1And40BitRC4 = 406
XCN_OID_PKCS_12_PROTECTED_PASSWORD_SECRET_BAG_TYPE_ID = 407
XCN_OID_PKINIT_KP_KDC = 408
XCN_OID_PKIX_CA_REPOSITORY = 409
XCN_OID_PKIX_OCSP_NONCE = 410
XCN_OID_PKIX_TIME_STAMPING = 411
XCN_OID_QC_EU_COMPLIANCE = 412
XCN_OID_QC_SSCD = 413
XCN_OID_QC_STATEMENTS_EXT = 414
XCN_OID_RDN_TPM_MANUFACTURER = 415
XCN_OID_RDN_TPM_MODEL = 416
XCN_OID_RDN_TPM_VERSION = 417
XCN_OID_REVOKED_LIST_SIGNER = 418
XCN_OID_RFC3161_counterSign = 419
XCN_OID_ROOT_PROGRAM_AUTO_UPDATE_CA_REVOCATION = 420
XCN_OID_ROOT_PROGRAM_AUTO_UPDATE_END_REVOCATION = 421
XCN_OID_ROOT_PROGRAM_FLAGS = 422
XCN_OID_ROOT_PROGRAM_NO_OCSP_FAILOVER_TO_CRL = 423
XCN_OID_RSA_PSPECIFIED = 424
XCN_OID_RSAES_OAEP = 425
XCN_OID_SUBJECT_INFO_ACCESS = 426
XCN_OID_TIMESTAMP_TOKEN = 427
XCN_OID_ENROLL_SCEP_ERROR = 428
XCN_OIDVerisign_MessageType = 429
XCN_OIDVerisign_PkiStatus = 430
XCN_OIDVerisign_FailInfo = 431
XCN_OIDVerisign_SenderNonce = 432
XCN_OIDVerisign_RecipientNonce = 433
XCN_OIDVerisign_TransactionID = 434
XCN_OID_ENROLL_ATTESTATION_CHALLENGE = 435
XCN_OID_ENROLL_ATTESTATION_STATEMENT = 436
XCN_OID_ENROLL_ENCRYPTION_ALGORITHM = 437
XCN_OID_ENROLL_KSP_NAME = 438
WebSecurityLevel = Int32
WebSecurityLevel_LevelUnsafe = 0
WebSecurityLevel_LevelSafe = 1
EncodingType = Int32
XCN_CRYPT_STRING_BASE64HEADER = 0
XCN_CRYPT_STRING_BASE64 = 1
XCN_CRYPT_STRING_BINARY = 2
XCN_CRYPT_STRING_BASE64REQUESTHEADER = 3
XCN_CRYPT_STRING_HEX = 4
XCN_CRYPT_STRING_HEXASCII = 5
XCN_CRYPT_STRING_BASE64_ANY = 6
XCN_CRYPT_STRING_ANY = 7
XCN_CRYPT_STRING_HEX_ANY = 8
XCN_CRYPT_STRING_BASE64X509CRLHEADER = 9
XCN_CRYPT_STRING_HEXADDR = 10
XCN_CRYPT_STRING_HEXASCIIADDR = 11
XCN_CRYPT_STRING_HEXRAW = 12
XCN_CRYPT_STRING_BASE64URI = 13
XCN_CRYPT_STRING_ENCODEMASK = 255
XCN_CRYPT_STRING_CHAIN = 256
XCN_CRYPT_STRING_TEXT = 512
XCN_CRYPT_STRING_PERCENTESCAPE = 134217728
XCN_CRYPT_STRING_HASHDATA = 268435456
XCN_CRYPT_STRING_STRICT = 536870912
XCN_CRYPT_STRING_NOCRLF = 1073741824
XCN_CRYPT_STRING_NOCR = -2147483648
PFXExportOptions = Int32
PFXExportOptions_PFXExportEEOnly = 0
PFXExportOptions_PFXExportChainNoRoot = 1
PFXExportOptions_PFXExportChainWithRoot = 2
ObjectIdGroupId = Int32
XCN_CRYPT_ANY_GROUP_ID = 0
XCN_CRYPT_HASH_ALG_OID_GROUP_ID = 1
XCN_CRYPT_ENCRYPT_ALG_OID_GROUP_ID = 2
XCN_CRYPT_PUBKEY_ALG_OID_GROUP_ID = 3
XCN_CRYPT_SIGN_ALG_OID_GROUP_ID = 4
XCN_CRYPT_RDN_ATTR_OID_GROUP_ID = 5
XCN_CRYPT_EXT_OR_ATTR_OID_GROUP_ID = 6
XCN_CRYPT_ENHKEY_USAGE_OID_GROUP_ID = 7
XCN_CRYPT_POLICY_OID_GROUP_ID = 8
XCN_CRYPT_TEMPLATE_OID_GROUP_ID = 9
XCN_CRYPT_KDF_OID_GROUP_ID = 10
XCN_CRYPT_LAST_OID_GROUP_ID = 10
XCN_CRYPT_FIRST_ALG_OID_GROUP_ID = 1
XCN_CRYPT_LAST_ALG_OID_GROUP_ID = 4
XCN_CRYPT_GROUP_ID_MASK = 65535
XCN_CRYPT_OID_PREFER_CNG_ALGID_FLAG = 1073741824
XCN_CRYPT_OID_DISABLE_SEARCH_DS_FLAG = -2147483648
XCN_CRYPT_OID_INFO_OID_GROUP_BIT_LEN_MASK = 268369920
XCN_CRYPT_OID_INFO_OID_GROUP_BIT_LEN_SHIFT = 16
XCN_CRYPT_KEY_LENGTH_MASK = 268369920
ObjectIdPublicKeyFlags = Int32
XCN_CRYPT_OID_INFO_PUBKEY_ANY = 0
XCN_CRYPT_OID_INFO_PUBKEY_SIGN_KEY_FLAG = -2147483648
XCN_CRYPT_OID_INFO_PUBKEY_ENCRYPT_KEY_FLAG = 1073741824
AlgorithmFlags = Int32
AlgorithmFlags_AlgorithmFlagsNone = 0
AlgorithmFlags_AlgorithmFlagsWrap = 1
def _define_IObjectId_head():
    class IObjectId(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab300-217d-11da-b2a4-000e7bbb2b09')
    return IObjectId
def _define_IObjectId():
    IObjectId = win32more.Security.Cryptography.Certificates.IObjectId_head
    IObjectId.InitializeFromName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CERTENROLL_OBJECTID, use_last_error=False)(7, 'InitializeFromName', ((1, 'Name'),)))
    IObjectId.InitializeFromValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'InitializeFromValue', ((1, 'strValue'),)))
    IObjectId.InitializeFromAlgorithmName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ObjectIdGroupId,win32more.Security.Cryptography.Certificates.ObjectIdPublicKeyFlags,win32more.Security.Cryptography.Certificates.AlgorithmFlags,win32more.Foundation.BSTR, use_last_error=False)(9, 'InitializeFromAlgorithmName', ((1, 'GroupId'),(1, 'KeyFlags'),(1, 'AlgFlags'),(1, 'strAlgorithmName'),)))
    IObjectId.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.CERTENROLL_OBJECTID), use_last_error=False)(10, 'get_Name', ((1, 'pValue'),)))
    IObjectId.get_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_FriendlyName', ((1, 'pValue'),)))
    IObjectId.put_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_FriendlyName', ((1, 'Value'),)))
    IObjectId.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_Value', ((1, 'pValue'),)))
    IObjectId.GetAlgorithmName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ObjectIdGroupId,win32more.Security.Cryptography.Certificates.ObjectIdPublicKeyFlags,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'GetAlgorithmName', ((1, 'GroupId'),(1, 'KeyFlags'),(1, 'pstrAlgorithmName'),)))
    win32more.System.Com.IDispatch
    return IObjectId
def _define_IObjectIds_head():
    class IObjectIds(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab301-217d-11da-b2a4-000e7bbb2b09')
    return IObjectIds
def _define_IObjectIds():
    IObjectIds = win32more.Security.Cryptography.Certificates.IObjectIds_head
    IObjectIds.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    IObjectIds.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    IObjectIds.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    IObjectIds.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    IObjectIds.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    IObjectIds.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    IObjectIds.AddRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectIds_head, use_last_error=False)(13, 'AddRange', ((1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IObjectIds
def _define_IBinaryConverter_head():
    class IBinaryConverter(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab302-217d-11da-b2a4-000e7bbb2b09')
    return IBinaryConverter
def _define_IBinaryConverter():
    IBinaryConverter = win32more.Security.Cryptography.Certificates.IBinaryConverter_head
    IBinaryConverter.StringToString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'StringToString', ((1, 'strEncodedIn'),(1, 'EncodingIn'),(1, 'Encoding'),(1, 'pstrEncoded'),)))
    IBinaryConverter.VariantByteArrayToString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'VariantByteArrayToString', ((1, 'pvarByteArray'),(1, 'Encoding'),(1, 'pstrEncoded'),)))
    IBinaryConverter.StringToVariantByteArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'StringToVariantByteArray', ((1, 'strEncoded'),(1, 'Encoding'),(1, 'pvarByteArray'),)))
    win32more.System.Com.IDispatch
    return IBinaryConverter
def _define_IBinaryConverter2_head():
    class IBinaryConverter2(win32more.Security.Cryptography.Certificates.IBinaryConverter_head):
        Guid = Guid('8d7928b4-4e17-428d-9a17-728df00d1b2b')
    return IBinaryConverter2
def _define_IBinaryConverter2():
    IBinaryConverter2 = win32more.Security.Cryptography.Certificates.IBinaryConverter2_head
    IBinaryConverter2.StringArrayToVariantArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'StringArrayToVariantArray', ((1, 'pvarStringArray'),(1, 'pvarVariantArray'),)))
    IBinaryConverter2.VariantArrayToStringArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'VariantArrayToStringArray', ((1, 'pvarVariantArray'),(1, 'pvarStringArray'),)))
    win32more.Security.Cryptography.Certificates.IBinaryConverter
    return IBinaryConverter2
X500NameFlags = Int32
XCN_CERT_NAME_STR_NONE = 0
XCN_CERT_SIMPLE_NAME_STR = 1
XCN_CERT_OID_NAME_STR = 2
XCN_CERT_X500_NAME_STR = 3
XCN_CERT_XML_NAME_STR = 4
XCN_CERT_NAME_STR_SEMICOLON_FLAG = 1073741824
XCN_CERT_NAME_STR_NO_PLUS_FLAG = 536870912
XCN_CERT_NAME_STR_NO_QUOTING_FLAG = 268435456
XCN_CERT_NAME_STR_CRLF_FLAG = 134217728
XCN_CERT_NAME_STR_COMMA_FLAG = 67108864
XCN_CERT_NAME_STR_REVERSE_FLAG = 33554432
XCN_CERT_NAME_STR_FORWARD_FLAG = 16777216
XCN_CERT_NAME_STR_AMBIGUOUS_SEPARATOR_FLAGS = 1275068416
XCN_CERT_NAME_STR_DISABLE_IE4_UTF8_FLAG = 65536
XCN_CERT_NAME_STR_ENABLE_T61_UNICODE_FLAG = 131072
XCN_CERT_NAME_STR_ENABLE_UTF8_UNICODE_FLAG = 262144
XCN_CERT_NAME_STR_FORCE_UTF8_DIR_STR_FLAG = 524288
XCN_CERT_NAME_STR_DISABLE_UTF8_DIR_STR_FLAG = 1048576
XCN_CERT_NAME_STR_ENABLE_PUNYCODE_FLAG = 2097152
XCN_CERT_NAME_STR_DS_ESCAPED = 8388608
def _define_IX500DistinguishedName_head():
    class IX500DistinguishedName(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab303-217d-11da-b2a4-000e7bbb2b09')
    return IX500DistinguishedName
def _define_IX500DistinguishedName():
    IX500DistinguishedName = win32more.Security.Cryptography.Certificates.IX500DistinguishedName_head
    IX500DistinguishedName.Decode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Security.Cryptography.Certificates.X500NameFlags, use_last_error=False)(7, 'Decode', ((1, 'strEncodedName'),(1, 'Encoding'),(1, 'NameFlags'),)))
    IX500DistinguishedName.Encode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.X500NameFlags, use_last_error=False)(8, 'Encode', ((1, 'strName'),(1, 'NameFlags'),)))
    IX500DistinguishedName.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Name', ((1, 'pValue'),)))
    IX500DistinguishedName.get_EncodedName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_EncodedName', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX500DistinguishedName
X509CertificateEnrollmentContext = Int32
X509CertificateEnrollmentContext_ContextNone = 0
X509CertificateEnrollmentContext_ContextUser = 1
X509CertificateEnrollmentContext_ContextMachine = 2
X509CertificateEnrollmentContext_ContextAdministratorForceMachine = 3
EnrollmentEnrollStatus = Int32
EnrollmentEnrollStatus_Enrolled = 1
EnrollmentEnrollStatus_EnrollPended = 2
EnrollmentEnrollStatus_EnrollUIDeferredEnrollmentRequired = 4
EnrollmentEnrollStatus_EnrollError = 16
EnrollmentEnrollStatus_EnrollUnknown = 32
EnrollmentEnrollStatus_EnrollSkipped = 64
EnrollmentEnrollStatus_EnrollDenied = 256
EnrollmentSelectionStatus = Int32
EnrollmentSelectionStatus_SelectedNo = 0
EnrollmentSelectionStatus_SelectedYes = 1
EnrollmentDisplayStatus = Int32
EnrollmentDisplayStatus_DisplayNo = 0
EnrollmentDisplayStatus_DisplayYes = 1
def _define_IX509EnrollmentStatus_head():
    class IX509EnrollmentStatus(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab304-217d-11da-b2a4-000e7bbb2b09')
    return IX509EnrollmentStatus
def _define_IX509EnrollmentStatus():
    IX509EnrollmentStatus = win32more.Security.Cryptography.Certificates.IX509EnrollmentStatus_head
    IX509EnrollmentStatus.AppendText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'AppendText', ((1, 'strText'),)))
    IX509EnrollmentStatus.get_Text = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Text', ((1, 'pValue'),)))
    IX509EnrollmentStatus.put_Text = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'put_Text', ((1, 'Value'),)))
    IX509EnrollmentStatus.get_Selected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.EnrollmentSelectionStatus), use_last_error=False)(10, 'get_Selected', ((1, 'pValue'),)))
    IX509EnrollmentStatus.put_Selected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EnrollmentSelectionStatus, use_last_error=False)(11, 'put_Selected', ((1, 'Value'),)))
    IX509EnrollmentStatus.get_Display = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.EnrollmentDisplayStatus), use_last_error=False)(12, 'get_Display', ((1, 'pValue'),)))
    IX509EnrollmentStatus.put_Display = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EnrollmentDisplayStatus, use_last_error=False)(13, 'put_Display', ((1, 'Value'),)))
    IX509EnrollmentStatus.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.EnrollmentEnrollStatus), use_last_error=False)(14, 'get_Status', ((1, 'pValue'),)))
    IX509EnrollmentStatus.put_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EnrollmentEnrollStatus, use_last_error=False)(15, 'put_Status', ((1, 'Value'),)))
    IX509EnrollmentStatus.get_Error = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(16, 'get_Error', ((1, 'pValue'),)))
    IX509EnrollmentStatus.put_Error = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(17, 'put_Error', ((1, 'Value'),)))
    IX509EnrollmentStatus.get_ErrorText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_ErrorText', ((1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX509EnrollmentStatus
X509ProviderType = Int32
XCN_PROV_NONE = 0
XCN_PROV_RSA_FULL = 1
XCN_PROV_RSA_SIG = 2
XCN_PROV_DSS = 3
XCN_PROV_FORTEZZA = 4
XCN_PROV_MS_EXCHANGE = 5
XCN_PROV_SSL = 6
XCN_PROV_RSA_SCHANNEL = 12
XCN_PROV_DSS_DH = 13
XCN_PROV_EC_ECDSA_SIG = 14
XCN_PROV_EC_ECNRA_SIG = 15
XCN_PROV_EC_ECDSA_FULL = 16
XCN_PROV_EC_ECNRA_FULL = 17
XCN_PROV_DH_SCHANNEL = 18
XCN_PROV_SPYRUS_LYNKS = 20
XCN_PROV_RNG = 21
XCN_PROV_INTEL_SEC = 22
XCN_PROV_REPLACE_OWF = 23
XCN_PROV_RSA_AES = 24
AlgorithmType = Int32
XCN_BCRYPT_UNKNOWN_INTERFACE = 0
XCN_BCRYPT_CIPHER_INTERFACE = 1
XCN_BCRYPT_HASH_INTERFACE = 2
XCN_BCRYPT_ASYMMETRIC_ENCRYPTION_INTERFACE = 3
XCN_BCRYPT_SIGNATURE_INTERFACE = 5
XCN_BCRYPT_SECRET_AGREEMENT_INTERFACE = 4
XCN_BCRYPT_RNG_INTERFACE = 6
XCN_BCRYPT_KEY_DERIVATION_INTERFACE = 7
AlgorithmOperationFlags = Int32
XCN_NCRYPT_NO_OPERATION = 0
XCN_NCRYPT_CIPHER_OPERATION = 1
XCN_NCRYPT_HASH_OPERATION = 2
XCN_NCRYPT_ASYMMETRIC_ENCRYPTION_OPERATION = 4
XCN_NCRYPT_SECRET_AGREEMENT_OPERATION = 8
XCN_NCRYPT_SIGNATURE_OPERATION = 16
XCN_NCRYPT_RNG_OPERATION = 32
XCN_NCRYPT_KEY_DERIVATION_OPERATION = 64
XCN_NCRYPT_ANY_ASYMMETRIC_OPERATION = 28
XCN_NCRYPT_PREFER_SIGNATURE_ONLY_OPERATION = 2097152
XCN_NCRYPT_PREFER_NON_SIGNATURE_OPERATION = 4194304
XCN_NCRYPT_EXACT_MATCH_OPERATION = 8388608
XCN_NCRYPT_PREFERENCE_MASK_OPERATION = 14680064
def _define_ICspAlgorithm_head():
    class ICspAlgorithm(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab305-217d-11da-b2a4-000e7bbb2b09')
    return ICspAlgorithm
def _define_ICspAlgorithm():
    ICspAlgorithm = win32more.Security.Cryptography.Certificates.ICspAlgorithm_head
    ICspAlgorithm.GetAlgorithmOid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Security.Cryptography.Certificates.AlgorithmFlags,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(7, 'GetAlgorithmOid', ((1, 'Length'),(1, 'AlgFlags'),(1, 'ppValue'),)))
    ICspAlgorithm.get_DefaultLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_DefaultLength', ((1, 'pValue'),)))
    ICspAlgorithm.get_IncrementLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_IncrementLength', ((1, 'pValue'),)))
    ICspAlgorithm.get_LongName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_LongName', ((1, 'pValue'),)))
    ICspAlgorithm.get_Valid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_Valid', ((1, 'pValue'),)))
    ICspAlgorithm.get_MaxLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_MaxLength', ((1, 'pValue'),)))
    ICspAlgorithm.get_MinLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_MinLength', ((1, 'pValue'),)))
    ICspAlgorithm.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_Name', ((1, 'pValue'),)))
    ICspAlgorithm.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.AlgorithmType), use_last_error=False)(15, 'get_Type', ((1, 'pValue'),)))
    ICspAlgorithm.get_Operations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.AlgorithmOperationFlags), use_last_error=False)(16, 'get_Operations', ((1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return ICspAlgorithm
def _define_ICspAlgorithms_head():
    class ICspAlgorithms(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab306-217d-11da-b2a4-000e7bbb2b09')
    return ICspAlgorithms
def _define_ICspAlgorithms():
    ICspAlgorithms = win32more.Security.Cryptography.Certificates.ICspAlgorithms_head
    ICspAlgorithms.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.ICspAlgorithm_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    ICspAlgorithms.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    ICspAlgorithms.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    ICspAlgorithms.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICspAlgorithm_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    ICspAlgorithms.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    ICspAlgorithms.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    ICspAlgorithms.get_ItemByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Cryptography.Certificates.ICspAlgorithm_head), use_last_error=False)(13, 'get_ItemByName', ((1, 'strName'),(1, 'ppValue'),)))
    ICspAlgorithms.get_IndexByObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head,POINTER(Int32), use_last_error=False)(14, 'get_IndexByObjectId', ((1, 'pObjectId'),(1, 'pIndex'),)))
    win32more.System.Com.IDispatch
    return ICspAlgorithms
X509KeySpec = Int32
XCN_AT_NONE = 0
XCN_AT_KEYEXCHANGE = 1
XCN_AT_SIGNATURE = 2
def _define_ICspInformation_head():
    class ICspInformation(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab307-217d-11da-b2a4-000e7bbb2b09')
    return ICspInformation
def _define_ICspInformation():
    ICspInformation = win32more.Security.Cryptography.Certificates.ICspInformation_head
    ICspInformation.InitializeFromName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'InitializeFromName', ((1, 'strName'),)))
    ICspInformation.InitializeFromType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509ProviderType,win32more.Security.Cryptography.Certificates.IObjectId_head,Int16, use_last_error=False)(8, 'InitializeFromType', ((1, 'Type'),(1, 'pAlgorithm'),(1, 'MachineContext'),)))
    ICspInformation.get_CspAlgorithms = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICspAlgorithms_head), use_last_error=False)(9, 'get_CspAlgorithms', ((1, 'ppValue'),)))
    ICspInformation.get_HasHardwareRandomNumberGenerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_HasHardwareRandomNumberGenerator', ((1, 'pValue'),)))
    ICspInformation.get_IsHardwareDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_IsHardwareDevice', ((1, 'pValue'),)))
    ICspInformation.get_IsRemovable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_IsRemovable', ((1, 'pValue'),)))
    ICspInformation.get_IsSoftwareDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_IsSoftwareDevice', ((1, 'pValue'),)))
    ICspInformation.get_Valid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(14, 'get_Valid', ((1, 'pValue'),)))
    ICspInformation.get_MaxKeyContainerNameLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_MaxKeyContainerNameLength', ((1, 'pValue'),)))
    ICspInformation.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_Name', ((1, 'pValue'),)))
    ICspInformation.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509ProviderType), use_last_error=False)(17, 'get_Type', ((1, 'pValue'),)))
    ICspInformation.get_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(18, 'get_Version', ((1, 'pValue'),)))
    ICspInformation.get_KeySpec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509KeySpec), use_last_error=False)(19, 'get_KeySpec', ((1, 'pValue'),)))
    ICspInformation.get_IsSmartCard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(20, 'get_IsSmartCard', ((1, 'pValue'),)))
    ICspInformation.GetDefaultSecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'GetDefaultSecurityDescriptor', ((1, 'MachineContext'),(1, 'pValue'),)))
    ICspInformation.get_LegacyCsp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(22, 'get_LegacyCsp', ((1, 'pValue'),)))
    ICspInformation.GetCspStatusFromOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head,win32more.Security.Cryptography.Certificates.AlgorithmOperationFlags,POINTER(win32more.Security.Cryptography.Certificates.ICspStatus_head), use_last_error=False)(23, 'GetCspStatusFromOperations', ((1, 'pAlgorithm'),(1, 'Operations'),(1, 'ppValue'),)))
    win32more.System.Com.IDispatch
    return ICspInformation
def _define_ICspInformations_head():
    class ICspInformations(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab308-217d-11da-b2a4-000e7bbb2b09')
    return ICspInformations
def _define_ICspInformations():
    ICspInformations = win32more.Security.Cryptography.Certificates.ICspInformations_head
    ICspInformations.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.ICspInformation_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    ICspInformations.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    ICspInformations.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    ICspInformations.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICspInformation_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    ICspInformations.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    ICspInformations.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    ICspInformations.AddAvailableCsps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'AddAvailableCsps', ()))
    ICspInformations.get_ItemByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Cryptography.Certificates.ICspInformation_head), use_last_error=False)(14, 'get_ItemByName', ((1, 'strName'),(1, 'ppCspInformation'),)))
    ICspInformations.GetCspStatusFromProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.X509KeySpec,POINTER(win32more.Security.Cryptography.Certificates.ICspStatus_head), use_last_error=False)(15, 'GetCspStatusFromProviderName', ((1, 'strProviderName'),(1, 'LegacyKeySpec'),(1, 'ppValue'),)))
    ICspInformations.GetCspStatusesFromOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.AlgorithmOperationFlags,win32more.Security.Cryptography.Certificates.ICspInformation_head,POINTER(win32more.Security.Cryptography.Certificates.ICspStatuses_head), use_last_error=False)(16, 'GetCspStatusesFromOperations', ((1, 'Operations'),(1, 'pCspInformation'),(1, 'ppValue'),)))
    ICspInformations.GetEncryptionCspAlgorithms = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICspInformation_head,POINTER(win32more.Security.Cryptography.Certificates.ICspAlgorithms_head), use_last_error=False)(17, 'GetEncryptionCspAlgorithms', ((1, 'pCspInformation'),(1, 'ppValue'),)))
    ICspInformations.GetHashAlgorithms = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICspInformation_head,POINTER(win32more.Security.Cryptography.Certificates.IObjectIds_head), use_last_error=False)(18, 'GetHashAlgorithms', ((1, 'pCspInformation'),(1, 'ppValue'),)))
    win32more.System.Com.IDispatch
    return ICspInformations
def _define_ICspStatus_head():
    class ICspStatus(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab309-217d-11da-b2a4-000e7bbb2b09')
    return ICspStatus
def _define_ICspStatus():
    ICspStatus = win32more.Security.Cryptography.Certificates.ICspStatus_head
    ICspStatus.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICspInformation_head,win32more.Security.Cryptography.Certificates.ICspAlgorithm_head, use_last_error=False)(7, 'Initialize', ((1, 'pCsp'),(1, 'pAlgorithm'),)))
    ICspStatus.get_Ordinal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Ordinal', ((1, 'pValue'),)))
    ICspStatus.put_Ordinal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'put_Ordinal', ((1, 'Value'),)))
    ICspStatus.get_CspAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICspAlgorithm_head), use_last_error=False)(10, 'get_CspAlgorithm', ((1, 'ppValue'),)))
    ICspStatus.get_CspInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICspInformation_head), use_last_error=False)(11, 'get_CspInformation', ((1, 'ppValue'),)))
    ICspStatus.get_EnrollmentStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509EnrollmentStatus_head), use_last_error=False)(12, 'get_EnrollmentStatus', ((1, 'ppValue'),)))
    ICspStatus.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_DisplayName', ((1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return ICspStatus
def _define_ICspStatuses_head():
    class ICspStatuses(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab30a-217d-11da-b2a4-000e7bbb2b09')
    return ICspStatuses
def _define_ICspStatuses():
    ICspStatuses = win32more.Security.Cryptography.Certificates.ICspStatuses_head
    ICspStatuses.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.ICspStatus_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    ICspStatuses.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    ICspStatuses.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    ICspStatuses.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICspStatus_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    ICspStatuses.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    ICspStatuses.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    ICspStatuses.get_ItemByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Security.Cryptography.Certificates.ICspStatus_head), use_last_error=False)(13, 'get_ItemByName', ((1, 'strCspName'),(1, 'strAlgorithmName'),(1, 'ppValue'),)))
    ICspStatuses.get_ItemByOrdinal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.ICspStatus_head), use_last_error=False)(14, 'get_ItemByOrdinal', ((1, 'Ordinal'),(1, 'ppValue'),)))
    ICspStatuses.get_ItemByOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.AlgorithmOperationFlags,POINTER(win32more.Security.Cryptography.Certificates.ICspStatus_head), use_last_error=False)(15, 'get_ItemByOperations', ((1, 'strCspName'),(1, 'strAlgorithmName'),(1, 'Operations'),(1, 'ppValue'),)))
    ICspStatuses.get_ItemByProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICspStatus_head,POINTER(win32more.Security.Cryptography.Certificates.ICspStatus_head), use_last_error=False)(16, 'get_ItemByProvider', ((1, 'pCspStatus'),(1, 'ppValue'),)))
    win32more.System.Com.IDispatch
    return ICspStatuses
KeyIdentifierHashAlgorithm = Int32
KeyIdentifierHashAlgorithm_SKIHashDefault = 0
KeyIdentifierHashAlgorithm_SKIHashSha1 = 1
KeyIdentifierHashAlgorithm_SKIHashCapiSha1 = 2
KeyIdentifierHashAlgorithm_SKIHashSha256 = 3
KeyIdentifierHashAlgorithm_SKIHashHPKP = 5
def _define_IX509PublicKey_head():
    class IX509PublicKey(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab30b-217d-11da-b2a4-000e7bbb2b09')
    return IX509PublicKey
def _define_IX509PublicKey():
    IX509PublicKey = win32more.Security.Cryptography.Certificates.IX509PublicKey_head
    IX509PublicKey.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(7, 'Initialize', ((1, 'pObjectId'),(1, 'strEncodedKey'),(1, 'strEncodedParameters'),(1, 'Encoding'),)))
    IX509PublicKey.InitializeFromEncodedPublicKeyInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(8, 'InitializeFromEncodedPublicKeyInfo', ((1, 'strEncodedPublicKeyInfo'),(1, 'Encoding'),)))
    IX509PublicKey.get_Algorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(9, 'get_Algorithm', ((1, 'ppValue'),)))
    IX509PublicKey.get_Length = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Length', ((1, 'pValue'),)))
    IX509PublicKey.get_EncodedKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_EncodedKey', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509PublicKey.get_EncodedParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_EncodedParameters', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509PublicKey.ComputeKeyIdentifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.KeyIdentifierHashAlgorithm,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'ComputeKeyIdentifier', ((1, 'Algorithm'),(1, 'Encoding'),(1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX509PublicKey
X509PrivateKeyExportFlags = Int32
XCN_NCRYPT_ALLOW_EXPORT_NONE = 0
XCN_NCRYPT_ALLOW_EXPORT_FLAG = 1
XCN_NCRYPT_ALLOW_PLAINTEXT_EXPORT_FLAG = 2
XCN_NCRYPT_ALLOW_ARCHIVING_FLAG = 4
XCN_NCRYPT_ALLOW_PLAINTEXT_ARCHIVING_FLAG = 8
X509PrivateKeyUsageFlags = Int32
XCN_NCRYPT_ALLOW_USAGES_NONE = 0
XCN_NCRYPT_ALLOW_DECRYPT_FLAG = 1
XCN_NCRYPT_ALLOW_SIGNING_FLAG = 2
XCN_NCRYPT_ALLOW_KEY_AGREEMENT_FLAG = 4
XCN_NCRYPT_ALLOW_KEY_IMPORT_FLAG = 8
XCN_NCRYPT_ALLOW_ALL_USAGES = 16777215
X509PrivateKeyProtection = Int32
XCN_NCRYPT_UI_NO_PROTECTION_FLAG = 0
XCN_NCRYPT_UI_PROTECT_KEY_FLAG = 1
XCN_NCRYPT_UI_FORCE_HIGH_PROTECTION_FLAG = 2
XCN_NCRYPT_UI_FINGERPRINT_PROTECTION_FLAG = 4
XCN_NCRYPT_UI_APPCONTAINER_ACCESS_MEDIUM_FLAG = 8
X509PrivateKeyVerify = Int32
X509PrivateKeyVerify_VerifyNone = 0
X509PrivateKeyVerify_VerifySilent = 1
X509PrivateKeyVerify_VerifySmartCardNone = 2
X509PrivateKeyVerify_VerifySmartCardSilent = 3
X509PrivateKeyVerify_VerifyAllowUI = 4
def _define_IX509PrivateKey_head():
    class IX509PrivateKey(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab30c-217d-11da-b2a4-000e7bbb2b09')
    return IX509PrivateKey
def _define_IX509PrivateKey():
    IX509PrivateKey = win32more.Security.Cryptography.Certificates.IX509PrivateKey_head
    IX509PrivateKey.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Open', ()))
    IX509PrivateKey.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Create', ()))
    IX509PrivateKey.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Close', ()))
    IX509PrivateKey.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Delete', ()))
    IX509PrivateKey.Verify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509PrivateKeyVerify, use_last_error=False)(11, 'Verify', ((1, 'VerifyType'),)))
    IX509PrivateKey.Import = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(12, 'Import', ((1, 'strExportType'),(1, 'strEncodedKey'),(1, 'Encoding'),)))
    IX509PrivateKey.Export = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'Export', ((1, 'strExportType'),(1, 'Encoding'),(1, 'pstrEncodedKey'),)))
    IX509PrivateKey.ExportPublicKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509PublicKey_head), use_last_error=False)(14, 'ExportPublicKey', ((1, 'ppPublicKey'),)))
    IX509PrivateKey.get_ContainerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_ContainerName', ((1, 'pValue'),)))
    IX509PrivateKey.put_ContainerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_ContainerName', ((1, 'Value'),)))
    IX509PrivateKey.get_ContainerNamePrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_ContainerNamePrefix', ((1, 'pValue'),)))
    IX509PrivateKey.put_ContainerNamePrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_ContainerNamePrefix', ((1, 'Value'),)))
    IX509PrivateKey.get_ReaderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_ReaderName', ((1, 'pValue'),)))
    IX509PrivateKey.put_ReaderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(20, 'put_ReaderName', ((1, 'Value'),)))
    IX509PrivateKey.get_CspInformations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICspInformations_head), use_last_error=False)(21, 'get_CspInformations', ((1, 'ppValue'),)))
    IX509PrivateKey.put_CspInformations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICspInformations_head, use_last_error=False)(22, 'put_CspInformations', ((1, 'pValue'),)))
    IX509PrivateKey.get_CspStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICspStatus_head), use_last_error=False)(23, 'get_CspStatus', ((1, 'ppValue'),)))
    IX509PrivateKey.put_CspStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICspStatus_head, use_last_error=False)(24, 'put_CspStatus', ((1, 'pValue'),)))
    IX509PrivateKey.get_ProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_ProviderName', ((1, 'pValue'),)))
    IX509PrivateKey.put_ProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(26, 'put_ProviderName', ((1, 'Value'),)))
    IX509PrivateKey.get_ProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509ProviderType), use_last_error=False)(27, 'get_ProviderType', ((1, 'pValue'),)))
    IX509PrivateKey.put_ProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509ProviderType, use_last_error=False)(28, 'put_ProviderType', ((1, 'Value'),)))
    IX509PrivateKey.get_LegacyCsp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(29, 'get_LegacyCsp', ((1, 'pValue'),)))
    IX509PrivateKey.put_LegacyCsp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(30, 'put_LegacyCsp', ((1, 'Value'),)))
    IX509PrivateKey.get_Algorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(31, 'get_Algorithm', ((1, 'ppValue'),)))
    IX509PrivateKey.put_Algorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head, use_last_error=False)(32, 'put_Algorithm', ((1, 'pValue'),)))
    IX509PrivateKey.get_KeySpec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509KeySpec), use_last_error=False)(33, 'get_KeySpec', ((1, 'pValue'),)))
    IX509PrivateKey.put_KeySpec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509KeySpec, use_last_error=False)(34, 'put_KeySpec', ((1, 'Value'),)))
    IX509PrivateKey.get_Length = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(35, 'get_Length', ((1, 'pValue'),)))
    IX509PrivateKey.put_Length = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(36, 'put_Length', ((1, 'Value'),)))
    IX509PrivateKey.get_ExportPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509PrivateKeyExportFlags), use_last_error=False)(37, 'get_ExportPolicy', ((1, 'pValue'),)))
    IX509PrivateKey.put_ExportPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509PrivateKeyExportFlags, use_last_error=False)(38, 'put_ExportPolicy', ((1, 'Value'),)))
    IX509PrivateKey.get_KeyUsage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509PrivateKeyUsageFlags), use_last_error=False)(39, 'get_KeyUsage', ((1, 'pValue'),)))
    IX509PrivateKey.put_KeyUsage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509PrivateKeyUsageFlags, use_last_error=False)(40, 'put_KeyUsage', ((1, 'Value'),)))
    IX509PrivateKey.get_KeyProtection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509PrivateKeyProtection), use_last_error=False)(41, 'get_KeyProtection', ((1, 'pValue'),)))
    IX509PrivateKey.put_KeyProtection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509PrivateKeyProtection, use_last_error=False)(42, 'put_KeyProtection', ((1, 'Value'),)))
    IX509PrivateKey.get_MachineContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(43, 'get_MachineContext', ((1, 'pValue'),)))
    IX509PrivateKey.put_MachineContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(44, 'put_MachineContext', ((1, 'Value'),)))
    IX509PrivateKey.get_SecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(45, 'get_SecurityDescriptor', ((1, 'pValue'),)))
    IX509PrivateKey.put_SecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(46, 'put_SecurityDescriptor', ((1, 'Value'),)))
    IX509PrivateKey.get_Certificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(47, 'get_Certificate', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509PrivateKey.put_Certificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(48, 'put_Certificate', ((1, 'Encoding'),(1, 'Value'),)))
    IX509PrivateKey.get_UniqueContainerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(49, 'get_UniqueContainerName', ((1, 'pValue'),)))
    IX509PrivateKey.get_Opened = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(50, 'get_Opened', ((1, 'pValue'),)))
    IX509PrivateKey.get_DefaultContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(51, 'get_DefaultContainer', ((1, 'pValue'),)))
    IX509PrivateKey.get_Existing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(52, 'get_Existing', ((1, 'pValue'),)))
    IX509PrivateKey.put_Existing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(53, 'put_Existing', ((1, 'Value'),)))
    IX509PrivateKey.get_Silent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(54, 'get_Silent', ((1, 'pValue'),)))
    IX509PrivateKey.put_Silent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(55, 'put_Silent', ((1, 'Value'),)))
    IX509PrivateKey.get_ParentWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(56, 'get_ParentWindow', ((1, 'pValue'),)))
    IX509PrivateKey.put_ParentWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(57, 'put_ParentWindow', ((1, 'Value'),)))
    IX509PrivateKey.get_UIContextMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(58, 'get_UIContextMessage', ((1, 'pValue'),)))
    IX509PrivateKey.put_UIContextMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(59, 'put_UIContextMessage', ((1, 'Value'),)))
    IX509PrivateKey.put_Pin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(60, 'put_Pin', ((1, 'Value'),)))
    IX509PrivateKey.get_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(61, 'get_FriendlyName', ((1, 'pValue'),)))
    IX509PrivateKey.put_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(62, 'put_FriendlyName', ((1, 'Value'),)))
    IX509PrivateKey.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(63, 'get_Description', ((1, 'pValue'),)))
    IX509PrivateKey.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(64, 'put_Description', ((1, 'Value'),)))
    win32more.System.Com.IDispatch
    return IX509PrivateKey
X509HardwareKeyUsageFlags = Int32
XCN_NCRYPT_PCP_NONE = 0
XCN_NCRYPT_TPM12_PROVIDER = 65536
XCN_NCRYPT_PCP_SIGNATURE_KEY = 1
XCN_NCRYPT_PCP_ENCRYPTION_KEY = 2
XCN_NCRYPT_PCP_GENERIC_KEY = 3
XCN_NCRYPT_PCP_STORAGE_KEY = 4
XCN_NCRYPT_PCP_IDENTITY_KEY = 8
X509KeyParametersExportType = Int32
XCN_CRYPT_OID_USE_CURVE_NONE = 0
XCN_CRYPT_OID_USE_CURVE_NAME_FOR_ENCODE_FLAG = 536870912
XCN_CRYPT_OID_USE_CURVE_PARAMETERS_FOR_ENCODE_FLAG = 268435456
def _define_IX509PrivateKey2_head():
    class IX509PrivateKey2(win32more.Security.Cryptography.Certificates.IX509PrivateKey_head):
        Guid = Guid('728ab362-217d-11da-b2a4-000e7bbb2b09')
    return IX509PrivateKey2
def _define_IX509PrivateKey2():
    IX509PrivateKey2 = win32more.Security.Cryptography.Certificates.IX509PrivateKey2_head
    IX509PrivateKey2.get_HardwareKeyUsage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509HardwareKeyUsageFlags), use_last_error=False)(65, 'get_HardwareKeyUsage', ((1, 'pValue'),)))
    IX509PrivateKey2.put_HardwareKeyUsage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509HardwareKeyUsageFlags, use_last_error=False)(66, 'put_HardwareKeyUsage', ((1, 'Value'),)))
    IX509PrivateKey2.get_AlternateStorageLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(67, 'get_AlternateStorageLocation', ((1, 'pValue'),)))
    IX509PrivateKey2.put_AlternateStorageLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(68, 'put_AlternateStorageLocation', ((1, 'Value'),)))
    IX509PrivateKey2.get_AlgorithmName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(69, 'get_AlgorithmName', ((1, 'pValue'),)))
    IX509PrivateKey2.put_AlgorithmName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(70, 'put_AlgorithmName', ((1, 'Value'),)))
    IX509PrivateKey2.get_AlgorithmParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(71, 'get_AlgorithmParameters', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509PrivateKey2.put_AlgorithmParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(72, 'put_AlgorithmParameters', ((1, 'Encoding'),(1, 'Value'),)))
    IX509PrivateKey2.get_ParametersExportType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509KeyParametersExportType), use_last_error=False)(73, 'get_ParametersExportType', ((1, 'pValue'),)))
    IX509PrivateKey2.put_ParametersExportType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509KeyParametersExportType, use_last_error=False)(74, 'put_ParametersExportType', ((1, 'Value'),)))
    win32more.Security.Cryptography.Certificates.IX509PrivateKey
    return IX509PrivateKey2
def _define_IX509EndorsementKey_head():
    class IX509EndorsementKey(win32more.System.Com.IDispatch_head):
        Guid = Guid('b11cd855-f4c4-4fc6-b710-4422237f09e9')
    return IX509EndorsementKey
def _define_IX509EndorsementKey():
    IX509EndorsementKey = win32more.Security.Cryptography.Certificates.IX509EndorsementKey_head
    IX509EndorsementKey.get_ProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ProviderName', ((1, 'pValue'),)))
    IX509EndorsementKey.put_ProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_ProviderName', ((1, 'Value'),)))
    IX509EndorsementKey.get_Length = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Length', ((1, 'pValue'),)))
    IX509EndorsementKey.get_Opened = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_Opened', ((1, 'pValue'),)))
    IX509EndorsementKey.AddCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(11, 'AddCertificate', ((1, 'Encoding'),(1, 'strCertificate'),)))
    IX509EndorsementKey.RemoveCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(12, 'RemoveCertificate', ((1, 'Encoding'),(1, 'strCertificate'),)))
    IX509EndorsementKey.GetCertificateByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,Int32,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'GetCertificateByIndex', ((1, 'ManufacturerOnly'),(1, 'dwIndex'),(1, 'Encoding'),(1, 'pValue'),)))
    IX509EndorsementKey.GetCertificateCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Int32), use_last_error=False)(14, 'GetCertificateCount', ((1, 'ManufacturerOnly'),(1, 'pCount'),)))
    IX509EndorsementKey.ExportPublicKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509PublicKey_head), use_last_error=False)(15, 'ExportPublicKey', ((1, 'ppPublicKey'),)))
    IX509EndorsementKey.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Open', ()))
    IX509EndorsementKey.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'Close', ()))
    win32more.System.Com.IDispatch
    return IX509EndorsementKey
def _define_IX509Extension_head():
    class IX509Extension(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab30d-217d-11da-b2a4-000e7bbb2b09')
    return IX509Extension
def _define_IX509Extension():
    IX509Extension = win32more.Security.Cryptography.Certificates.IX509Extension_head
    IX509Extension.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(7, 'Initialize', ((1, 'pObjectId'),(1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509Extension.get_ObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(8, 'get_ObjectId', ((1, 'ppValue'),)))
    IX509Extension.get_RawData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_RawData', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509Extension.get_Critical = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_Critical', ((1, 'pValue'),)))
    IX509Extension.put_Critical = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(11, 'put_Critical', ((1, 'Value'),)))
    win32more.System.Com.IDispatch
    return IX509Extension
def _define_IX509Extensions_head():
    class IX509Extensions(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab30e-217d-11da-b2a4-000e7bbb2b09')
    return IX509Extensions
def _define_IX509Extensions():
    IX509Extensions = win32more.Security.Cryptography.Certificates.IX509Extensions_head
    IX509Extensions.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.IX509Extension_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    IX509Extensions.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    IX509Extensions.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    IX509Extensions.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509Extension_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    IX509Extensions.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    IX509Extensions.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    IX509Extensions.get_IndexByObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head,POINTER(Int32), use_last_error=False)(13, 'get_IndexByObjectId', ((1, 'pObjectId'),(1, 'pIndex'),)))
    IX509Extensions.AddRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509Extensions_head, use_last_error=False)(14, 'AddRange', ((1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX509Extensions
X509KeyUsageFlags = Int32
XCN_CERT_NO_KEY_USAGE = 0
XCN_CERT_DIGITAL_SIGNATURE_KEY_USAGE = 128
XCN_CERT_NON_REPUDIATION_KEY_USAGE = 64
XCN_CERT_KEY_ENCIPHERMENT_KEY_USAGE = 32
XCN_CERT_DATA_ENCIPHERMENT_KEY_USAGE = 16
XCN_CERT_KEY_AGREEMENT_KEY_USAGE = 8
XCN_CERT_KEY_CERT_SIGN_KEY_USAGE = 4
XCN_CERT_OFFLINE_CRL_SIGN_KEY_USAGE = 2
XCN_CERT_CRL_SIGN_KEY_USAGE = 2
XCN_CERT_ENCIPHER_ONLY_KEY_USAGE = 1
XCN_CERT_DECIPHER_ONLY_KEY_USAGE = 32768
def _define_IX509ExtensionKeyUsage_head():
    class IX509ExtensionKeyUsage(win32more.Security.Cryptography.Certificates.IX509Extension_head):
        Guid = Guid('728ab30f-217d-11da-b2a4-000e7bbb2b09')
    return IX509ExtensionKeyUsage
def _define_IX509ExtensionKeyUsage():
    IX509ExtensionKeyUsage = win32more.Security.Cryptography.Certificates.IX509ExtensionKeyUsage_head
    IX509ExtensionKeyUsage.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509KeyUsageFlags, use_last_error=False)(12, 'InitializeEncode', ((1, 'UsageFlags'),)))
    IX509ExtensionKeyUsage.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509ExtensionKeyUsage.get_KeyUsage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509KeyUsageFlags), use_last_error=False)(14, 'get_KeyUsage', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Extension
    return IX509ExtensionKeyUsage
def _define_IX509ExtensionEnhancedKeyUsage_head():
    class IX509ExtensionEnhancedKeyUsage(win32more.Security.Cryptography.Certificates.IX509Extension_head):
        Guid = Guid('728ab310-217d-11da-b2a4-000e7bbb2b09')
    return IX509ExtensionEnhancedKeyUsage
def _define_IX509ExtensionEnhancedKeyUsage():
    IX509ExtensionEnhancedKeyUsage = win32more.Security.Cryptography.Certificates.IX509ExtensionEnhancedKeyUsage_head
    IX509ExtensionEnhancedKeyUsage.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectIds_head, use_last_error=False)(12, 'InitializeEncode', ((1, 'pValue'),)))
    IX509ExtensionEnhancedKeyUsage.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509ExtensionEnhancedKeyUsage.get_EnhancedKeyUsage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectIds_head), use_last_error=False)(14, 'get_EnhancedKeyUsage', ((1, 'ppValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Extension
    return IX509ExtensionEnhancedKeyUsage
def _define_IX509ExtensionTemplateName_head():
    class IX509ExtensionTemplateName(win32more.Security.Cryptography.Certificates.IX509Extension_head):
        Guid = Guid('728ab311-217d-11da-b2a4-000e7bbb2b09')
    return IX509ExtensionTemplateName
def _define_IX509ExtensionTemplateName():
    IX509ExtensionTemplateName = win32more.Security.Cryptography.Certificates.IX509ExtensionTemplateName_head
    IX509ExtensionTemplateName.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'InitializeEncode', ((1, 'strTemplateName'),)))
    IX509ExtensionTemplateName.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509ExtensionTemplateName.get_TemplateName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_TemplateName', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Extension
    return IX509ExtensionTemplateName
def _define_IX509ExtensionTemplate_head():
    class IX509ExtensionTemplate(win32more.Security.Cryptography.Certificates.IX509Extension_head):
        Guid = Guid('728ab312-217d-11da-b2a4-000e7bbb2b09')
    return IX509ExtensionTemplate
def _define_IX509ExtensionTemplate():
    IX509ExtensionTemplate = win32more.Security.Cryptography.Certificates.IX509ExtensionTemplate_head
    IX509ExtensionTemplate.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head,Int32,Int32, use_last_error=False)(12, 'InitializeEncode', ((1, 'pTemplateOid'),(1, 'MajorVersion'),(1, 'MinorVersion'),)))
    IX509ExtensionTemplate.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509ExtensionTemplate.get_TemplateOid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(14, 'get_TemplateOid', ((1, 'ppValue'),)))
    IX509ExtensionTemplate.get_MajorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_MajorVersion', ((1, 'pValue'),)))
    IX509ExtensionTemplate.get_MinorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_MinorVersion', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Extension
    return IX509ExtensionTemplate
AlternativeNameType = Int32
XCN_CERT_ALT_NAME_UNKNOWN = 0
XCN_CERT_ALT_NAME_OTHER_NAME = 1
XCN_CERT_ALT_NAME_RFC822_NAME = 2
XCN_CERT_ALT_NAME_DNS_NAME = 3
XCN_CERT_ALT_NAME_X400_ADDRESS = 4
XCN_CERT_ALT_NAME_DIRECTORY_NAME = 5
XCN_CERT_ALT_NAME_EDI_PARTY_NAME = 6
XCN_CERT_ALT_NAME_URL = 7
XCN_CERT_ALT_NAME_IP_ADDRESS = 8
XCN_CERT_ALT_NAME_REGISTERED_ID = 9
XCN_CERT_ALT_NAME_GUID = 10
XCN_CERT_ALT_NAME_USER_PRINCIPLE_NAME = 11
def _define_IAlternativeName_head():
    class IAlternativeName(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab313-217d-11da-b2a4-000e7bbb2b09')
    return IAlternativeName
def _define_IAlternativeName():
    IAlternativeName = win32more.Security.Cryptography.Certificates.IAlternativeName_head
    IAlternativeName.InitializeFromString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.AlternativeNameType,win32more.Foundation.BSTR, use_last_error=False)(7, 'InitializeFromString', ((1, 'Type'),(1, 'strValue'),)))
    IAlternativeName.InitializeFromRawData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.AlternativeNameType,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(8, 'InitializeFromRawData', ((1, 'Type'),(1, 'Encoding'),(1, 'strRawData'),)))
    IAlternativeName.InitializeFromOtherName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR,Int16, use_last_error=False)(9, 'InitializeFromOtherName', ((1, 'pObjectId'),(1, 'Encoding'),(1, 'strRawData'),(1, 'ToBeWrapped'),)))
    IAlternativeName.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.AlternativeNameType), use_last_error=False)(10, 'get_Type', ((1, 'pValue'),)))
    IAlternativeName.get_StrValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_StrValue', ((1, 'pValue'),)))
    IAlternativeName.get_ObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(12, 'get_ObjectId', ((1, 'ppValue'),)))
    IAlternativeName.get_RawData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_RawData', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IAlternativeName
def _define_IAlternativeNames_head():
    class IAlternativeNames(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab314-217d-11da-b2a4-000e7bbb2b09')
    return IAlternativeNames
def _define_IAlternativeNames():
    IAlternativeNames = win32more.Security.Cryptography.Certificates.IAlternativeNames_head
    IAlternativeNames.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.IAlternativeName_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    IAlternativeNames.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    IAlternativeNames.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    IAlternativeNames.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IAlternativeName_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    IAlternativeNames.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    IAlternativeNames.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    win32more.System.Com.IDispatch
    return IAlternativeNames
def _define_IX509ExtensionAlternativeNames_head():
    class IX509ExtensionAlternativeNames(win32more.Security.Cryptography.Certificates.IX509Extension_head):
        Guid = Guid('728ab315-217d-11da-b2a4-000e7bbb2b09')
    return IX509ExtensionAlternativeNames
def _define_IX509ExtensionAlternativeNames():
    IX509ExtensionAlternativeNames = win32more.Security.Cryptography.Certificates.IX509ExtensionAlternativeNames_head
    IX509ExtensionAlternativeNames.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IAlternativeNames_head, use_last_error=False)(12, 'InitializeEncode', ((1, 'pValue'),)))
    IX509ExtensionAlternativeNames.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509ExtensionAlternativeNames.get_AlternativeNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IAlternativeNames_head), use_last_error=False)(14, 'get_AlternativeNames', ((1, 'ppValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Extension
    return IX509ExtensionAlternativeNames
def _define_IX509ExtensionBasicConstraints_head():
    class IX509ExtensionBasicConstraints(win32more.Security.Cryptography.Certificates.IX509Extension_head):
        Guid = Guid('728ab316-217d-11da-b2a4-000e7bbb2b09')
    return IX509ExtensionBasicConstraints
def _define_IX509ExtensionBasicConstraints():
    IX509ExtensionBasicConstraints = win32more.Security.Cryptography.Certificates.IX509ExtensionBasicConstraints_head
    IX509ExtensionBasicConstraints.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,Int32, use_last_error=False)(12, 'InitializeEncode', ((1, 'IsCA'),(1, 'PathLenConstraint'),)))
    IX509ExtensionBasicConstraints.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509ExtensionBasicConstraints.get_IsCA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(14, 'get_IsCA', ((1, 'pValue'),)))
    IX509ExtensionBasicConstraints.get_PathLenConstraint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_PathLenConstraint', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Extension
    return IX509ExtensionBasicConstraints
def _define_IX509ExtensionSubjectKeyIdentifier_head():
    class IX509ExtensionSubjectKeyIdentifier(win32more.Security.Cryptography.Certificates.IX509Extension_head):
        Guid = Guid('728ab317-217d-11da-b2a4-000e7bbb2b09')
    return IX509ExtensionSubjectKeyIdentifier
def _define_IX509ExtensionSubjectKeyIdentifier():
    IX509ExtensionSubjectKeyIdentifier = win32more.Security.Cryptography.Certificates.IX509ExtensionSubjectKeyIdentifier_head
    IX509ExtensionSubjectKeyIdentifier.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(12, 'InitializeEncode', ((1, 'Encoding'),(1, 'strKeyIdentifier'),)))
    IX509ExtensionSubjectKeyIdentifier.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509ExtensionSubjectKeyIdentifier.get_SubjectKeyIdentifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_SubjectKeyIdentifier', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Extension
    return IX509ExtensionSubjectKeyIdentifier
def _define_IX509ExtensionAuthorityKeyIdentifier_head():
    class IX509ExtensionAuthorityKeyIdentifier(win32more.Security.Cryptography.Certificates.IX509Extension_head):
        Guid = Guid('728ab318-217d-11da-b2a4-000e7bbb2b09')
    return IX509ExtensionAuthorityKeyIdentifier
def _define_IX509ExtensionAuthorityKeyIdentifier():
    IX509ExtensionAuthorityKeyIdentifier = win32more.Security.Cryptography.Certificates.IX509ExtensionAuthorityKeyIdentifier_head
    IX509ExtensionAuthorityKeyIdentifier.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(12, 'InitializeEncode', ((1, 'Encoding'),(1, 'strKeyIdentifier'),)))
    IX509ExtensionAuthorityKeyIdentifier.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509ExtensionAuthorityKeyIdentifier.get_AuthorityKeyIdentifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_AuthorityKeyIdentifier', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Extension
    return IX509ExtensionAuthorityKeyIdentifier
def _define_ISmimeCapability_head():
    class ISmimeCapability(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab319-217d-11da-b2a4-000e7bbb2b09')
    return ISmimeCapability
def _define_ISmimeCapability():
    ISmimeCapability = win32more.Security.Cryptography.Certificates.ISmimeCapability_head
    ISmimeCapability.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head,Int32, use_last_error=False)(7, 'Initialize', ((1, 'pObjectId'),(1, 'BitCount'),)))
    ISmimeCapability.get_ObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(8, 'get_ObjectId', ((1, 'ppValue'),)))
    ISmimeCapability.get_BitCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_BitCount', ((1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return ISmimeCapability
def _define_ISmimeCapabilities_head():
    class ISmimeCapabilities(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab31a-217d-11da-b2a4-000e7bbb2b09')
    return ISmimeCapabilities
def _define_ISmimeCapabilities():
    ISmimeCapabilities = win32more.Security.Cryptography.Certificates.ISmimeCapabilities_head
    ISmimeCapabilities.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.ISmimeCapability_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    ISmimeCapabilities.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    ISmimeCapabilities.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    ISmimeCapabilities.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ISmimeCapability_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    ISmimeCapabilities.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    ISmimeCapabilities.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    ISmimeCapabilities.AddFromCsp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICspInformation_head, use_last_error=False)(13, 'AddFromCsp', ((1, 'pValue'),)))
    ISmimeCapabilities.AddAvailableSmimeCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'AddAvailableSmimeCapabilities', ((1, 'MachineContext'),)))
    win32more.System.Com.IDispatch
    return ISmimeCapabilities
def _define_IX509ExtensionSmimeCapabilities_head():
    class IX509ExtensionSmimeCapabilities(win32more.Security.Cryptography.Certificates.IX509Extension_head):
        Guid = Guid('728ab31b-217d-11da-b2a4-000e7bbb2b09')
    return IX509ExtensionSmimeCapabilities
def _define_IX509ExtensionSmimeCapabilities():
    IX509ExtensionSmimeCapabilities = win32more.Security.Cryptography.Certificates.IX509ExtensionSmimeCapabilities_head
    IX509ExtensionSmimeCapabilities.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ISmimeCapabilities_head, use_last_error=False)(12, 'InitializeEncode', ((1, 'pValue'),)))
    IX509ExtensionSmimeCapabilities.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509ExtensionSmimeCapabilities.get_SmimeCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ISmimeCapabilities_head), use_last_error=False)(14, 'get_SmimeCapabilities', ((1, 'ppValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Extension
    return IX509ExtensionSmimeCapabilities
PolicyQualifierType = Int32
PolicyQualifierType_PolicyQualifierTypeUnknown = 0
PolicyQualifierType_PolicyQualifierTypeUrl = 1
PolicyQualifierType_PolicyQualifierTypeUserNotice = 2
PolicyQualifierType_PolicyQualifierTypeFlags = 3
def _define_IPolicyQualifier_head():
    class IPolicyQualifier(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab31c-217d-11da-b2a4-000e7bbb2b09')
    return IPolicyQualifier
def _define_IPolicyQualifier():
    IPolicyQualifier = win32more.Security.Cryptography.Certificates.IPolicyQualifier_head
    IPolicyQualifier.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.PolicyQualifierType, use_last_error=False)(7, 'InitializeEncode', ((1, 'strQualifier'),(1, 'Type'),)))
    IPolicyQualifier.get_ObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(8, 'get_ObjectId', ((1, 'ppValue'),)))
    IPolicyQualifier.get_Qualifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Qualifier', ((1, 'pValue'),)))
    IPolicyQualifier.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.PolicyQualifierType), use_last_error=False)(10, 'get_Type', ((1, 'pValue'),)))
    IPolicyQualifier.get_RawData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_RawData', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IPolicyQualifier
def _define_IPolicyQualifiers_head():
    class IPolicyQualifiers(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab31d-217d-11da-b2a4-000e7bbb2b09')
    return IPolicyQualifiers
def _define_IPolicyQualifiers():
    IPolicyQualifiers = win32more.Security.Cryptography.Certificates.IPolicyQualifiers_head
    IPolicyQualifiers.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.IPolicyQualifier_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    IPolicyQualifiers.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    IPolicyQualifiers.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    IPolicyQualifiers.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IPolicyQualifier_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    IPolicyQualifiers.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    IPolicyQualifiers.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    win32more.System.Com.IDispatch
    return IPolicyQualifiers
def _define_ICertificatePolicy_head():
    class ICertificatePolicy(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab31e-217d-11da-b2a4-000e7bbb2b09')
    return ICertificatePolicy
def _define_ICertificatePolicy():
    ICertificatePolicy = win32more.Security.Cryptography.Certificates.ICertificatePolicy_head
    ICertificatePolicy.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head, use_last_error=False)(7, 'Initialize', ((1, 'pValue'),)))
    ICertificatePolicy.get_ObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(8, 'get_ObjectId', ((1, 'ppValue'),)))
    ICertificatePolicy.get_PolicyQualifiers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IPolicyQualifiers_head), use_last_error=False)(9, 'get_PolicyQualifiers', ((1, 'ppValue'),)))
    win32more.System.Com.IDispatch
    return ICertificatePolicy
def _define_ICertificatePolicies_head():
    class ICertificatePolicies(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab31f-217d-11da-b2a4-000e7bbb2b09')
    return ICertificatePolicies
def _define_ICertificatePolicies():
    ICertificatePolicies = win32more.Security.Cryptography.Certificates.ICertificatePolicies_head
    ICertificatePolicies.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.ICertificatePolicy_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    ICertificatePolicies.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    ICertificatePolicies.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    ICertificatePolicies.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICertificatePolicy_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    ICertificatePolicies.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    ICertificatePolicies.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    win32more.System.Com.IDispatch
    return ICertificatePolicies
def _define_IX509ExtensionCertificatePolicies_head():
    class IX509ExtensionCertificatePolicies(win32more.Security.Cryptography.Certificates.IX509Extension_head):
        Guid = Guid('728ab320-217d-11da-b2a4-000e7bbb2b09')
    return IX509ExtensionCertificatePolicies
def _define_IX509ExtensionCertificatePolicies():
    IX509ExtensionCertificatePolicies = win32more.Security.Cryptography.Certificates.IX509ExtensionCertificatePolicies_head
    IX509ExtensionCertificatePolicies.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICertificatePolicies_head, use_last_error=False)(12, 'InitializeEncode', ((1, 'pValue'),)))
    IX509ExtensionCertificatePolicies.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509ExtensionCertificatePolicies.get_Policies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICertificatePolicies_head), use_last_error=False)(14, 'get_Policies', ((1, 'ppValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Extension
    return IX509ExtensionCertificatePolicies
def _define_IX509ExtensionMSApplicationPolicies_head():
    class IX509ExtensionMSApplicationPolicies(win32more.Security.Cryptography.Certificates.IX509Extension_head):
        Guid = Guid('728ab321-217d-11da-b2a4-000e7bbb2b09')
    return IX509ExtensionMSApplicationPolicies
def _define_IX509ExtensionMSApplicationPolicies():
    IX509ExtensionMSApplicationPolicies = win32more.Security.Cryptography.Certificates.IX509ExtensionMSApplicationPolicies_head
    IX509ExtensionMSApplicationPolicies.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICertificatePolicies_head, use_last_error=False)(12, 'InitializeEncode', ((1, 'pValue'),)))
    IX509ExtensionMSApplicationPolicies.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509ExtensionMSApplicationPolicies.get_Policies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICertificatePolicies_head), use_last_error=False)(14, 'get_Policies', ((1, 'ppValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Extension
    return IX509ExtensionMSApplicationPolicies
def _define_IX509Attribute_head():
    class IX509Attribute(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab322-217d-11da-b2a4-000e7bbb2b09')
    return IX509Attribute
def _define_IX509Attribute():
    IX509Attribute = win32more.Security.Cryptography.Certificates.IX509Attribute_head
    IX509Attribute.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(7, 'Initialize', ((1, 'pObjectId'),(1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509Attribute.get_ObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(8, 'get_ObjectId', ((1, 'ppValue'),)))
    IX509Attribute.get_RawData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_RawData', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX509Attribute
def _define_IX509Attributes_head():
    class IX509Attributes(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab323-217d-11da-b2a4-000e7bbb2b09')
    return IX509Attributes
def _define_IX509Attributes():
    IX509Attributes = win32more.Security.Cryptography.Certificates.IX509Attributes_head
    IX509Attributes.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.IX509Attribute_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    IX509Attributes.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    IX509Attributes.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    IX509Attributes.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509Attribute_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    IX509Attributes.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    IX509Attributes.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    win32more.System.Com.IDispatch
    return IX509Attributes
def _define_IX509AttributeExtensions_head():
    class IX509AttributeExtensions(win32more.Security.Cryptography.Certificates.IX509Attribute_head):
        Guid = Guid('728ab324-217d-11da-b2a4-000e7bbb2b09')
    return IX509AttributeExtensions
def _define_IX509AttributeExtensions():
    IX509AttributeExtensions = win32more.Security.Cryptography.Certificates.IX509AttributeExtensions_head
    IX509AttributeExtensions.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509Extensions_head, use_last_error=False)(10, 'InitializeEncode', ((1, 'pExtensions'),)))
    IX509AttributeExtensions.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(11, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509AttributeExtensions.get_X509Extensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509Extensions_head), use_last_error=False)(12, 'get_X509Extensions', ((1, 'ppValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Attribute
    return IX509AttributeExtensions
RequestClientInfoClientId = Int32
RequestClientInfoClientId_ClientIdNone = 0
RequestClientInfoClientId_ClientIdXEnroll2003 = 1
RequestClientInfoClientId_ClientIdAutoEnroll2003 = 2
RequestClientInfoClientId_ClientIdWizard2003 = 3
RequestClientInfoClientId_ClientIdCertReq2003 = 4
RequestClientInfoClientId_ClientIdDefaultRequest = 5
RequestClientInfoClientId_ClientIdAutoEnroll = 6
RequestClientInfoClientId_ClientIdRequestWizard = 7
RequestClientInfoClientId_ClientIdEOBO = 8
RequestClientInfoClientId_ClientIdCertReq = 9
RequestClientInfoClientId_ClientIdTest = 10
RequestClientInfoClientId_ClientIdWinRT = 11
RequestClientInfoClientId_ClientIdUserStart = 1000
def _define_IX509AttributeClientId_head():
    class IX509AttributeClientId(win32more.Security.Cryptography.Certificates.IX509Attribute_head):
        Guid = Guid('728ab325-217d-11da-b2a4-000e7bbb2b09')
    return IX509AttributeClientId
def _define_IX509AttributeClientId():
    IX509AttributeClientId = win32more.Security.Cryptography.Certificates.IX509AttributeClientId_head
    IX509AttributeClientId.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.RequestClientInfoClientId,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(10, 'InitializeEncode', ((1, 'ClientId'),(1, 'strMachineDnsName'),(1, 'strUserSamName'),(1, 'strProcessName'),)))
    IX509AttributeClientId.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(11, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509AttributeClientId.get_ClientId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.RequestClientInfoClientId), use_last_error=False)(12, 'get_ClientId', ((1, 'pValue'),)))
    IX509AttributeClientId.get_MachineDnsName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_MachineDnsName', ((1, 'pValue'),)))
    IX509AttributeClientId.get_UserSamName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_UserSamName', ((1, 'pValue'),)))
    IX509AttributeClientId.get_ProcessName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_ProcessName', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Attribute
    return IX509AttributeClientId
def _define_IX509AttributeRenewalCertificate_head():
    class IX509AttributeRenewalCertificate(win32more.Security.Cryptography.Certificates.IX509Attribute_head):
        Guid = Guid('728ab326-217d-11da-b2a4-000e7bbb2b09')
    return IX509AttributeRenewalCertificate
def _define_IX509AttributeRenewalCertificate():
    IX509AttributeRenewalCertificate = win32more.Security.Cryptography.Certificates.IX509AttributeRenewalCertificate_head
    IX509AttributeRenewalCertificate.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(10, 'InitializeEncode', ((1, 'Encoding'),(1, 'strCert'),)))
    IX509AttributeRenewalCertificate.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(11, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509AttributeRenewalCertificate.get_RenewalCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_RenewalCertificate', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Attribute
    return IX509AttributeRenewalCertificate
def _define_IX509AttributeArchiveKey_head():
    class IX509AttributeArchiveKey(win32more.Security.Cryptography.Certificates.IX509Attribute_head):
        Guid = Guid('728ab327-217d-11da-b2a4-000e7bbb2b09')
    return IX509AttributeArchiveKey
def _define_IX509AttributeArchiveKey():
    IX509AttributeArchiveKey = win32more.Security.Cryptography.Certificates.IX509AttributeArchiveKey_head
    IX509AttributeArchiveKey.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509PrivateKey_head,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.IObjectId_head,Int32, use_last_error=False)(10, 'InitializeEncode', ((1, 'pKey'),(1, 'Encoding'),(1, 'strCAXCert'),(1, 'pAlgorithm'),(1, 'EncryptionStrength'),)))
    IX509AttributeArchiveKey.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(11, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509AttributeArchiveKey.get_EncryptedKeyBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_EncryptedKeyBlob', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509AttributeArchiveKey.get_EncryptionAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(13, 'get_EncryptionAlgorithm', ((1, 'ppValue'),)))
    IX509AttributeArchiveKey.get_EncryptionStrength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'get_EncryptionStrength', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Attribute
    return IX509AttributeArchiveKey
def _define_IX509AttributeArchiveKeyHash_head():
    class IX509AttributeArchiveKeyHash(win32more.Security.Cryptography.Certificates.IX509Attribute_head):
        Guid = Guid('728ab328-217d-11da-b2a4-000e7bbb2b09')
    return IX509AttributeArchiveKeyHash
def _define_IX509AttributeArchiveKeyHash():
    IX509AttributeArchiveKeyHash = win32more.Security.Cryptography.Certificates.IX509AttributeArchiveKeyHash_head
    IX509AttributeArchiveKeyHash.InitializeEncodeFromEncryptedKeyBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(10, 'InitializeEncodeFromEncryptedKeyBlob', ((1, 'Encoding'),(1, 'strEncryptedKeyBlob'),)))
    IX509AttributeArchiveKeyHash.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(11, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509AttributeArchiveKeyHash.get_EncryptedKeyHashBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_EncryptedKeyHashBlob', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Attribute
    return IX509AttributeArchiveKeyHash
def _define_IX509AttributeOSVersion_head():
    class IX509AttributeOSVersion(win32more.Security.Cryptography.Certificates.IX509Attribute_head):
        Guid = Guid('728ab32a-217d-11da-b2a4-000e7bbb2b09')
    return IX509AttributeOSVersion
def _define_IX509AttributeOSVersion():
    IX509AttributeOSVersion = win32more.Security.Cryptography.Certificates.IX509AttributeOSVersion_head
    IX509AttributeOSVersion.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'InitializeEncode', ((1, 'strOSVersion'),)))
    IX509AttributeOSVersion.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(11, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509AttributeOSVersion.get_OSVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_OSVersion', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Attribute
    return IX509AttributeOSVersion
def _define_IX509AttributeCspProvider_head():
    class IX509AttributeCspProvider(win32more.Security.Cryptography.Certificates.IX509Attribute_head):
        Guid = Guid('728ab32b-217d-11da-b2a4-000e7bbb2b09')
    return IX509AttributeCspProvider
def _define_IX509AttributeCspProvider():
    IX509AttributeCspProvider = win32more.Security.Cryptography.Certificates.IX509AttributeCspProvider_head
    IX509AttributeCspProvider.InitializeEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509KeySpec,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(10, 'InitializeEncode', ((1, 'KeySpec'),(1, 'strProviderName'),(1, 'Encoding'),(1, 'strSignature'),)))
    IX509AttributeCspProvider.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(11, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    IX509AttributeCspProvider.get_KeySpec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509KeySpec), use_last_error=False)(12, 'get_KeySpec', ((1, 'pValue'),)))
    IX509AttributeCspProvider.get_ProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_ProviderName', ((1, 'pValue'),)))
    IX509AttributeCspProvider.get_Signature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_Signature', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Attribute
    return IX509AttributeCspProvider
def _define_ICryptAttribute_head():
    class ICryptAttribute(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab32c-217d-11da-b2a4-000e7bbb2b09')
    return ICryptAttribute
def _define_ICryptAttribute():
    ICryptAttribute = win32more.Security.Cryptography.Certificates.ICryptAttribute_head
    ICryptAttribute.InitializeFromObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head, use_last_error=False)(7, 'InitializeFromObjectId', ((1, 'pObjectId'),)))
    ICryptAttribute.InitializeFromValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509Attributes_head, use_last_error=False)(8, 'InitializeFromValues', ((1, 'pAttributes'),)))
    ICryptAttribute.get_ObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(9, 'get_ObjectId', ((1, 'ppValue'),)))
    ICryptAttribute.get_Values = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509Attributes_head), use_last_error=False)(10, 'get_Values', ((1, 'ppValue'),)))
    win32more.System.Com.IDispatch
    return ICryptAttribute
def _define_ICryptAttributes_head():
    class ICryptAttributes(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab32d-217d-11da-b2a4-000e7bbb2b09')
    return ICryptAttributes
def _define_ICryptAttributes():
    ICryptAttributes = win32more.Security.Cryptography.Certificates.ICryptAttributes_head
    ICryptAttributes.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.ICryptAttribute_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    ICryptAttributes.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    ICryptAttributes.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    ICryptAttributes.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICryptAttribute_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    ICryptAttributes.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    ICryptAttributes.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    ICryptAttributes.get_IndexByObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head,POINTER(Int32), use_last_error=False)(13, 'get_IndexByObjectId', ((1, 'pObjectId'),(1, 'pIndex'),)))
    ICryptAttributes.AddRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICryptAttributes_head, use_last_error=False)(14, 'AddRange', ((1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return ICryptAttributes
CERTENROLL_PROPERTYID = Int32
XCN_PROPERTYID_NONE = 0
XCN_CERT_KEY_PROV_HANDLE_PROP_ID = 1
XCN_CERT_KEY_PROV_INFO_PROP_ID = 2
XCN_CERT_SHA1_HASH_PROP_ID = 3
XCN_CERT_MD5_HASH_PROP_ID = 4
XCN_CERT_HASH_PROP_ID = 3
XCN_CERT_KEY_CONTEXT_PROP_ID = 5
XCN_CERT_KEY_SPEC_PROP_ID = 6
XCN_CERT_IE30_RESERVED_PROP_ID = 7
XCN_CERT_PUBKEY_HASH_RESERVED_PROP_ID = 8
XCN_CERT_ENHKEY_USAGE_PROP_ID = 9
XCN_CERT_CTL_USAGE_PROP_ID = 9
XCN_CERT_NEXT_UPDATE_LOCATION_PROP_ID = 10
XCN_CERT_FRIENDLY_NAME_PROP_ID = 11
XCN_CERT_PVK_FILE_PROP_ID = 12
XCN_CERT_DESCRIPTION_PROP_ID = 13
XCN_CERT_ACCESS_STATE_PROP_ID = 14
XCN_CERT_SIGNATURE_HASH_PROP_ID = 15
XCN_CERT_SMART_CARD_DATA_PROP_ID = 16
XCN_CERT_EFS_PROP_ID = 17
XCN_CERT_FORTEZZA_DATA_PROP_ID = 18
XCN_CERT_ARCHIVED_PROP_ID = 19
XCN_CERT_KEY_IDENTIFIER_PROP_ID = 20
XCN_CERT_AUTO_ENROLL_PROP_ID = 21
XCN_CERT_PUBKEY_ALG_PARA_PROP_ID = 22
XCN_CERT_CROSS_CERT_DIST_POINTS_PROP_ID = 23
XCN_CERT_ISSUER_PUBLIC_KEY_MD5_HASH_PROP_ID = 24
XCN_CERT_SUBJECT_PUBLIC_KEY_MD5_HASH_PROP_ID = 25
XCN_CERT_ENROLLMENT_PROP_ID = 26
XCN_CERT_DATE_STAMP_PROP_ID = 27
XCN_CERT_ISSUER_SERIAL_NUMBER_MD5_HASH_PROP_ID = 28
XCN_CERT_SUBJECT_NAME_MD5_HASH_PROP_ID = 29
XCN_CERT_EXTENDED_ERROR_INFO_PROP_ID = 30
XCN_CERT_RENEWAL_PROP_ID = 64
XCN_CERT_ARCHIVED_KEY_HASH_PROP_ID = 65
XCN_CERT_AUTO_ENROLL_RETRY_PROP_ID = 66
XCN_CERT_AIA_URL_RETRIEVED_PROP_ID = 67
XCN_CERT_AUTHORITY_INFO_ACCESS_PROP_ID = 68
XCN_CERT_BACKED_UP_PROP_ID = 69
XCN_CERT_OCSP_RESPONSE_PROP_ID = 70
XCN_CERT_REQUEST_ORIGINATOR_PROP_ID = 71
XCN_CERT_SOURCE_LOCATION_PROP_ID = 72
XCN_CERT_SOURCE_URL_PROP_ID = 73
XCN_CERT_NEW_KEY_PROP_ID = 74
XCN_CERT_OCSP_CACHE_PREFIX_PROP_ID = 75
XCN_CERT_SMART_CARD_ROOT_INFO_PROP_ID = 76
XCN_CERT_NO_AUTO_EXPIRE_CHECK_PROP_ID = 77
XCN_CERT_NCRYPT_KEY_HANDLE_PROP_ID = 78
XCN_CERT_HCRYPTPROV_OR_NCRYPT_KEY_HANDLE_PROP_ID = 79
XCN_CERT_SUBJECT_INFO_ACCESS_PROP_ID = 80
XCN_CERT_CA_OCSP_AUTHORITY_INFO_ACCESS_PROP_ID = 81
XCN_CERT_CA_DISABLE_CRL_PROP_ID = 82
XCN_CERT_ROOT_PROGRAM_CERT_POLICIES_PROP_ID = 83
XCN_CERT_ROOT_PROGRAM_NAME_CONSTRAINTS_PROP_ID = 84
XCN_CERT_SUBJECT_OCSP_AUTHORITY_INFO_ACCESS_PROP_ID = 85
XCN_CERT_SUBJECT_DISABLE_CRL_PROP_ID = 86
XCN_CERT_CEP_PROP_ID = 87
XCN_CERT_SIGN_HASH_CNG_ALG_PROP_ID = 89
XCN_CERT_SCARD_PIN_ID_PROP_ID = 90
XCN_CERT_SCARD_PIN_INFO_PROP_ID = 91
XCN_CERT_SUBJECT_PUB_KEY_BIT_LENGTH_PROP_ID = 92
XCN_CERT_PUB_KEY_CNG_ALG_BIT_LENGTH_PROP_ID = 93
XCN_CERT_ISSUER_PUB_KEY_BIT_LENGTH_PROP_ID = 94
XCN_CERT_ISSUER_CHAIN_SIGN_HASH_CNG_ALG_PROP_ID = 95
XCN_CERT_ISSUER_CHAIN_PUB_KEY_CNG_ALG_BIT_LENGTH_PROP_ID = 96
XCN_CERT_NO_EXPIRE_NOTIFICATION_PROP_ID = 97
XCN_CERT_AUTH_ROOT_SHA256_HASH_PROP_ID = 98
XCN_CERT_NCRYPT_KEY_HANDLE_TRANSFER_PROP_ID = 99
XCN_CERT_HCRYPTPROV_TRANSFER_PROP_ID = 100
XCN_CERT_SMART_CARD_READER_PROP_ID = 101
XCN_CERT_SEND_AS_TRUSTED_ISSUER_PROP_ID = 102
XCN_CERT_KEY_REPAIR_ATTEMPTED_PROP_ID = 103
XCN_CERT_DISALLOWED_FILETIME_PROP_ID = 104
XCN_CERT_ROOT_PROGRAM_CHAIN_POLICIES_PROP_ID = 105
XCN_CERT_SMART_CARD_READER_NON_REMOVABLE_PROP_ID = 106
XCN_CERT_SHA256_HASH_PROP_ID = 107
XCN_CERT_SCEP_SERVER_CERTS_PROP_ID = 108
XCN_CERT_SCEP_RA_SIGNATURE_CERT_PROP_ID = 109
XCN_CERT_SCEP_RA_ENCRYPTION_CERT_PROP_ID = 110
XCN_CERT_SCEP_CA_CERT_PROP_ID = 111
XCN_CERT_SCEP_SIGNER_CERT_PROP_ID = 112
XCN_CERT_SCEP_NONCE_PROP_ID = 113
XCN_CERT_SCEP_ENCRYPT_HASH_CNG_ALG_PROP_ID = 114
XCN_CERT_SCEP_FLAGS_PROP_ID = 115
XCN_CERT_SCEP_GUID_PROP_ID = 116
XCN_CERT_SERIALIZABLE_KEY_CONTEXT_PROP_ID = 117
XCN_CERT_ISOLATED_KEY_PROP_ID = 118
XCN_CERT_SERIAL_CHAIN_PROP_ID = 119
XCN_CERT_KEY_CLASSIFICATION_PROP_ID = 120
XCN_CERT_DISALLOWED_ENHKEY_USAGE_PROP_ID = 122
XCN_CERT_NONCOMPLIANT_ROOT_URL_PROP_ID = 123
XCN_CERT_PIN_SHA256_HASH_PROP_ID = 124
XCN_CERT_CLR_DELETE_KEY_PROP_ID = 125
XCN_CERT_NOT_BEFORE_FILETIME_PROP_ID = 126
XCN_CERT_CERT_NOT_BEFORE_ENHKEY_USAGE_PROP_ID = 127
XCN_CERT_FIRST_RESERVED_PROP_ID = 128
XCN_CERT_LAST_RESERVED_PROP_ID = 32767
XCN_CERT_FIRST_USER_PROP_ID = 32768
XCN_CERT_LAST_USER_PROP_ID = 65535
XCN_CERT_STORE_LOCALIZED_NAME_PROP_ID = 4096
def _define_ICertProperty_head():
    class ICertProperty(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab32e-217d-11da-b2a4-000e7bbb2b09')
    return ICertProperty
def _define_ICertProperty():
    ICertProperty = win32more.Security.Cryptography.Certificates.ICertProperty_head
    ICertProperty.InitializeFromCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(7, 'InitializeFromCertificate', ((1, 'MachineContext'),(1, 'Encoding'),(1, 'strCertificate'),)))
    ICertProperty.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(8, 'InitializeDecode', ((1, 'Encoding'),(1, 'strEncodedData'),)))
    ICertProperty.get_PropertyId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.CERTENROLL_PROPERTYID), use_last_error=False)(9, 'get_PropertyId', ((1, 'pValue'),)))
    ICertProperty.put_PropertyId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CERTENROLL_PROPERTYID, use_last_error=False)(10, 'put_PropertyId', ((1, 'Value'),)))
    ICertProperty.get_RawData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_RawData', ((1, 'Encoding'),(1, 'pValue'),)))
    ICertProperty.RemoveFromCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(12, 'RemoveFromCertificate', ((1, 'MachineContext'),(1, 'Encoding'),(1, 'strCertificate'),)))
    ICertProperty.SetValueOnCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'SetValueOnCertificate', ((1, 'MachineContext'),(1, 'Encoding'),(1, 'strCertificate'),)))
    win32more.System.Com.IDispatch
    return ICertProperty
def _define_ICertProperties_head():
    class ICertProperties(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab32f-217d-11da-b2a4-000e7bbb2b09')
    return ICertProperties
def _define_ICertProperties():
    ICertProperties = win32more.Security.Cryptography.Certificates.ICertProperties_head
    ICertProperties.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.ICertProperty_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    ICertProperties.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    ICertProperties.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    ICertProperties.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICertProperty_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    ICertProperties.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    ICertProperties.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    ICertProperties.InitializeFromCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(13, 'InitializeFromCertificate', ((1, 'MachineContext'),(1, 'Encoding'),(1, 'strCertificate'),)))
    win32more.System.Com.IDispatch
    return ICertProperties
def _define_ICertPropertyFriendlyName_head():
    class ICertPropertyFriendlyName(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab330-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertyFriendlyName
def _define_ICertPropertyFriendlyName():
    ICertPropertyFriendlyName = win32more.Security.Cryptography.Certificates.ICertPropertyFriendlyName_head
    ICertPropertyFriendlyName.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'Initialize', ((1, 'strFriendlyName'),)))
    ICertPropertyFriendlyName.get_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_FriendlyName', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertyFriendlyName
def _define_ICertPropertyDescription_head():
    class ICertPropertyDescription(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab331-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertyDescription
def _define_ICertPropertyDescription():
    ICertPropertyDescription = win32more.Security.Cryptography.Certificates.ICertPropertyDescription_head
    ICertPropertyDescription.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'Initialize', ((1, 'strDescription'),)))
    ICertPropertyDescription.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_Description', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertyDescription
def _define_ICertPropertyAutoEnroll_head():
    class ICertPropertyAutoEnroll(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab332-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertyAutoEnroll
def _define_ICertPropertyAutoEnroll():
    ICertPropertyAutoEnroll = win32more.Security.Cryptography.Certificates.ICertPropertyAutoEnroll_head
    ICertPropertyAutoEnroll.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'Initialize', ((1, 'strTemplateName'),)))
    ICertPropertyAutoEnroll.get_TemplateName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_TemplateName', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertyAutoEnroll
def _define_ICertPropertyRequestOriginator_head():
    class ICertPropertyRequestOriginator(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab333-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertyRequestOriginator
def _define_ICertPropertyRequestOriginator():
    ICertPropertyRequestOriginator = win32more.Security.Cryptography.Certificates.ICertPropertyRequestOriginator_head
    ICertPropertyRequestOriginator.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'Initialize', ((1, 'strRequestOriginator'),)))
    ICertPropertyRequestOriginator.InitializeFromLocalRequestOriginator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'InitializeFromLocalRequestOriginator', ()))
    ICertPropertyRequestOriginator.get_RequestOriginator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_RequestOriginator', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertyRequestOriginator
def _define_ICertPropertySHA1Hash_head():
    class ICertPropertySHA1Hash(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab334-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertySHA1Hash
def _define_ICertPropertySHA1Hash():
    ICertPropertySHA1Hash = win32more.Security.Cryptography.Certificates.ICertPropertySHA1Hash_head
    ICertPropertySHA1Hash.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(14, 'Initialize', ((1, 'Encoding'),(1, 'strRenewalValue'),)))
    ICertPropertySHA1Hash.get_SHA1Hash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_SHA1Hash', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertySHA1Hash
def _define_ICertPropertyKeyProvInfo_head():
    class ICertPropertyKeyProvInfo(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab336-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertyKeyProvInfo
def _define_ICertPropertyKeyProvInfo():
    ICertPropertyKeyProvInfo = win32more.Security.Cryptography.Certificates.ICertPropertyKeyProvInfo_head
    ICertPropertyKeyProvInfo.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509PrivateKey_head, use_last_error=False)(14, 'Initialize', ((1, 'pValue'),)))
    ICertPropertyKeyProvInfo.get_PrivateKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509PrivateKey_head), use_last_error=False)(15, 'get_PrivateKey', ((1, 'ppValue'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertyKeyProvInfo
def _define_ICertPropertyArchived_head():
    class ICertPropertyArchived(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab337-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertyArchived
def _define_ICertPropertyArchived():
    ICertPropertyArchived = win32more.Security.Cryptography.Certificates.ICertPropertyArchived_head
    ICertPropertyArchived.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'Initialize', ((1, 'ArchivedValue'),)))
    ICertPropertyArchived.get_Archived = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_Archived', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertyArchived
def _define_ICertPropertyBackedUp_head():
    class ICertPropertyBackedUp(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab338-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertyBackedUp
def _define_ICertPropertyBackedUp():
    ICertPropertyBackedUp = win32more.Security.Cryptography.Certificates.ICertPropertyBackedUp_head
    ICertPropertyBackedUp.InitializeFromCurrentTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'InitializeFromCurrentTime', ((1, 'BackedUpValue'),)))
    ICertPropertyBackedUp.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,Double, use_last_error=False)(15, 'Initialize', ((1, 'BackedUpValue'),(1, 'Date'),)))
    ICertPropertyBackedUp.get_BackedUpValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_BackedUpValue', ((1, 'pValue'),)))
    ICertPropertyBackedUp.get_BackedUpTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(17, 'get_BackedUpTime', ((1, 'pDate'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertyBackedUp
def _define_ICertPropertyEnrollment_head():
    class ICertPropertyEnrollment(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab339-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertyEnrollment
def _define_ICertPropertyEnrollment():
    ICertPropertyEnrollment = win32more.Security.Cryptography.Certificates.ICertPropertyEnrollment_head
    ICertPropertyEnrollment.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(14, 'Initialize', ((1, 'RequestId'),(1, 'strCADnsName'),(1, 'strCAName'),(1, 'strFriendlyName'),)))
    ICertPropertyEnrollment.get_RequestId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_RequestId', ((1, 'pValue'),)))
    ICertPropertyEnrollment.get_CADnsName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_CADnsName', ((1, 'pValue'),)))
    ICertPropertyEnrollment.get_CAName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_CAName', ((1, 'pValue'),)))
    ICertPropertyEnrollment.get_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_FriendlyName', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertyEnrollment
def _define_ICertPropertyRenewal_head():
    class ICertPropertyRenewal(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab33a-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertyRenewal
def _define_ICertPropertyRenewal():
    ICertPropertyRenewal = win32more.Security.Cryptography.Certificates.ICertPropertyRenewal_head
    ICertPropertyRenewal.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(14, 'Initialize', ((1, 'Encoding'),(1, 'strRenewalValue'),)))
    ICertPropertyRenewal.InitializeFromCertificateHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(15, 'InitializeFromCertificateHash', ((1, 'MachineContext'),(1, 'Encoding'),(1, 'strCertificate'),)))
    ICertPropertyRenewal.get_Renewal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_Renewal', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertyRenewal
def _define_ICertPropertyArchivedKeyHash_head():
    class ICertPropertyArchivedKeyHash(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab33b-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertyArchivedKeyHash
def _define_ICertPropertyArchivedKeyHash():
    ICertPropertyArchivedKeyHash = win32more.Security.Cryptography.Certificates.ICertPropertyArchivedKeyHash_head
    ICertPropertyArchivedKeyHash.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(14, 'Initialize', ((1, 'Encoding'),(1, 'strArchivedKeyHashValue'),)))
    ICertPropertyArchivedKeyHash.get_ArchivedKeyHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_ArchivedKeyHash', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertyArchivedKeyHash
EnrollmentPolicyServerPropertyFlags = Int32
EnrollmentPolicyServerPropertyFlags_DefaultNone = 0
EnrollmentPolicyServerPropertyFlags_DefaultPolicyServer = 1
PolicyServerUrlFlags = Int32
PolicyServerUrlFlags_PsfNone = 0
PolicyServerUrlFlags_PsfLocationGroupPolicy = 1
PolicyServerUrlFlags_PsfLocationRegistry = 2
PolicyServerUrlFlags_PsfUseClientId = 4
PolicyServerUrlFlags_PsfAutoEnrollmentEnabled = 16
PolicyServerUrlFlags_PsfAllowUnTrustedCA = 32
def _define_ICertPropertyEnrollmentPolicyServer_head():
    class ICertPropertyEnrollmentPolicyServer(win32more.Security.Cryptography.Certificates.ICertProperty_head):
        Guid = Guid('728ab34a-217d-11da-b2a4-000e7bbb2b09')
    return ICertPropertyEnrollmentPolicyServer
def _define_ICertPropertyEnrollmentPolicyServer():
    ICertPropertyEnrollmentPolicyServer = win32more.Security.Cryptography.Certificates.ICertPropertyEnrollmentPolicyServer_head
    ICertPropertyEnrollmentPolicyServer.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EnrollmentPolicyServerPropertyFlags,win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags,win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags,win32more.Security.Cryptography.Certificates.PolicyServerUrlFlags,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(14, 'Initialize', ((1, 'PropertyFlags'),(1, 'AuthFlags'),(1, 'EnrollmentServerAuthFlags'),(1, 'UrlFlags'),(1, 'strRequestId'),(1, 'strUrl'),(1, 'strId'),(1, 'strEnrollmentServerUrl'),)))
    ICertPropertyEnrollmentPolicyServer.GetPolicyServerUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'GetPolicyServerUrl', ((1, 'pValue'),)))
    ICertPropertyEnrollmentPolicyServer.GetPolicyServerId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'GetPolicyServerId', ((1, 'pValue'),)))
    ICertPropertyEnrollmentPolicyServer.GetEnrollmentServerUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'GetEnrollmentServerUrl', ((1, 'pValue'),)))
    ICertPropertyEnrollmentPolicyServer.GetRequestIdString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'GetRequestIdString', ((1, 'pValue'),)))
    ICertPropertyEnrollmentPolicyServer.GetPropertyFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.EnrollmentPolicyServerPropertyFlags), use_last_error=False)(19, 'GetPropertyFlags', ((1, 'pValue'),)))
    ICertPropertyEnrollmentPolicyServer.GetUrlFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.PolicyServerUrlFlags), use_last_error=False)(20, 'GetUrlFlags', ((1, 'pValue'),)))
    ICertPropertyEnrollmentPolicyServer.GetAuthentication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags), use_last_error=False)(21, 'GetAuthentication', ((1, 'pValue'),)))
    ICertPropertyEnrollmentPolicyServer.GetEnrollmentServerAuthentication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags), use_last_error=False)(22, 'GetEnrollmentServerAuthentication', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.ICertProperty
    return ICertPropertyEnrollmentPolicyServer
def _define_IX509SignatureInformation_head():
    class IX509SignatureInformation(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab33c-217d-11da-b2a4-000e7bbb2b09')
    return IX509SignatureInformation
def _define_IX509SignatureInformation():
    IX509SignatureInformation = win32more.Security.Cryptography.Certificates.IX509SignatureInformation_head
    IX509SignatureInformation.get_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(7, 'get_HashAlgorithm', ((1, 'ppValue'),)))
    IX509SignatureInformation.put_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head, use_last_error=False)(8, 'put_HashAlgorithm', ((1, 'pValue'),)))
    IX509SignatureInformation.get_PublicKeyAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(9, 'get_PublicKeyAlgorithm', ((1, 'ppValue'),)))
    IX509SignatureInformation.put_PublicKeyAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head, use_last_error=False)(10, 'put_PublicKeyAlgorithm', ((1, 'pValue'),)))
    IX509SignatureInformation.get_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_Parameters', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509SignatureInformation.put_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_Parameters', ((1, 'Encoding'),(1, 'Value'),)))
    IX509SignatureInformation.get_AlternateSignatureAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_AlternateSignatureAlgorithm', ((1, 'pValue'),)))
    IX509SignatureInformation.put_AlternateSignatureAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'put_AlternateSignatureAlgorithm', ((1, 'Value'),)))
    IX509SignatureInformation.get_AlternateSignatureAlgorithmSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_AlternateSignatureAlgorithmSet', ((1, 'pValue'),)))
    IX509SignatureInformation.get_NullSigned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_NullSigned', ((1, 'pValue'),)))
    IX509SignatureInformation.put_NullSigned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(17, 'put_NullSigned', ((1, 'Value'),)))
    IX509SignatureInformation.GetSignatureAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,Int16,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(18, 'GetSignatureAlgorithm', ((1, 'Pkcs7Signature'),(1, 'SignatureKey'),(1, 'ppValue'),)))
    IX509SignatureInformation.SetDefaultValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(19, 'SetDefaultValues', ()))
    win32more.System.Com.IDispatch
    return IX509SignatureInformation
def _define_ISignerCertificate_head():
    class ISignerCertificate(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab33d-217d-11da-b2a4-000e7bbb2b09')
    return ISignerCertificate
def _define_ISignerCertificate():
    ISignerCertificate = win32more.Security.Cryptography.Certificates.ISignerCertificate_head
    ISignerCertificate.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Security.Cryptography.Certificates.X509PrivateKeyVerify,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(7, 'Initialize', ((1, 'MachineContext'),(1, 'VerifyType'),(1, 'Encoding'),(1, 'strCertificate'),)))
    ISignerCertificate.get_Certificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Certificate', ((1, 'Encoding'),(1, 'pValue'),)))
    ISignerCertificate.get_PrivateKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509PrivateKey_head), use_last_error=False)(9, 'get_PrivateKey', ((1, 'ppValue'),)))
    ISignerCertificate.get_Silent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_Silent', ((1, 'pValue'),)))
    ISignerCertificate.put_Silent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(11, 'put_Silent', ((1, 'Value'),)))
    ISignerCertificate.get_ParentWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_ParentWindow', ((1, 'pValue'),)))
    ISignerCertificate.put_ParentWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'put_ParentWindow', ((1, 'Value'),)))
    ISignerCertificate.get_UIContextMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_UIContextMessage', ((1, 'pValue'),)))
    ISignerCertificate.put_UIContextMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_UIContextMessage', ((1, 'Value'),)))
    ISignerCertificate.put_Pin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_Pin', ((1, 'Value'),)))
    ISignerCertificate.get_SignatureInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509SignatureInformation_head), use_last_error=False)(17, 'get_SignatureInformation', ((1, 'ppValue'),)))
    win32more.System.Com.IDispatch
    return ISignerCertificate
def _define_ISignerCertificates_head():
    class ISignerCertificates(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab33e-217d-11da-b2a4-000e7bbb2b09')
    return ISignerCertificates
def _define_ISignerCertificates():
    ISignerCertificates = win32more.Security.Cryptography.Certificates.ISignerCertificates_head
    ISignerCertificates.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.ISignerCertificate_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    ISignerCertificates.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    ISignerCertificates.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    ISignerCertificates.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ISignerCertificate_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    ISignerCertificates.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    ISignerCertificates.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    ISignerCertificates.Find = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ISignerCertificate_head,POINTER(Int32), use_last_error=False)(13, 'Find', ((1, 'pSignerCert'),(1, 'piSignerCert'),)))
    win32more.System.Com.IDispatch
    return ISignerCertificates
def _define_IX509NameValuePair_head():
    class IX509NameValuePair(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab33f-217d-11da-b2a4-000e7bbb2b09')
    return IX509NameValuePair
def _define_IX509NameValuePair():
    IX509NameValuePair = win32more.Security.Cryptography.Certificates.IX509NameValuePair_head
    IX509NameValuePair.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(7, 'Initialize', ((1, 'strName'),(1, 'strValue'),)))
    IX509NameValuePair.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Value', ((1, 'pValue'),)))
    IX509NameValuePair.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Name', ((1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX509NameValuePair
def _define_IX509NameValuePairs_head():
    class IX509NameValuePairs(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab340-217d-11da-b2a4-000e7bbb2b09')
    return IX509NameValuePairs
def _define_IX509NameValuePairs():
    IX509NameValuePairs = win32more.Security.Cryptography.Certificates.IX509NameValuePairs_head
    IX509NameValuePairs.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.IX509NameValuePair_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    IX509NameValuePairs.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    IX509NameValuePairs.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    IX509NameValuePairs.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509NameValuePair_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    IX509NameValuePairs.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    IX509NameValuePairs.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    win32more.System.Com.IDispatch
    return IX509NameValuePairs
EnrollmentTemplateProperty = Int32
EnrollmentTemplateProperty_TemplatePropCommonName = 1
EnrollmentTemplateProperty_TemplatePropFriendlyName = 2
EnrollmentTemplateProperty_TemplatePropEKUs = 3
EnrollmentTemplateProperty_TemplatePropCryptoProviders = 4
EnrollmentTemplateProperty_TemplatePropMajorRevision = 5
EnrollmentTemplateProperty_TemplatePropDescription = 6
EnrollmentTemplateProperty_TemplatePropKeySpec = 7
EnrollmentTemplateProperty_TemplatePropSchemaVersion = 8
EnrollmentTemplateProperty_TemplatePropMinorRevision = 9
EnrollmentTemplateProperty_TemplatePropRASignatureCount = 10
EnrollmentTemplateProperty_TemplatePropMinimumKeySize = 11
EnrollmentTemplateProperty_TemplatePropOID = 12
EnrollmentTemplateProperty_TemplatePropSupersede = 13
EnrollmentTemplateProperty_TemplatePropRACertificatePolicies = 14
EnrollmentTemplateProperty_TemplatePropRAEKUs = 15
EnrollmentTemplateProperty_TemplatePropCertificatePolicies = 16
EnrollmentTemplateProperty_TemplatePropV1ApplicationPolicy = 17
EnrollmentTemplateProperty_TemplatePropAsymmetricAlgorithm = 18
EnrollmentTemplateProperty_TemplatePropKeySecurityDescriptor = 19
EnrollmentTemplateProperty_TemplatePropSymmetricAlgorithm = 20
EnrollmentTemplateProperty_TemplatePropSymmetricKeyLength = 21
EnrollmentTemplateProperty_TemplatePropHashAlgorithm = 22
EnrollmentTemplateProperty_TemplatePropKeyUsage = 23
EnrollmentTemplateProperty_TemplatePropEnrollmentFlags = 24
EnrollmentTemplateProperty_TemplatePropSubjectNameFlags = 25
EnrollmentTemplateProperty_TemplatePropPrivateKeyFlags = 26
EnrollmentTemplateProperty_TemplatePropGeneralFlags = 27
EnrollmentTemplateProperty_TemplatePropSecurityDescriptor = 28
EnrollmentTemplateProperty_TemplatePropExtensions = 29
EnrollmentTemplateProperty_TemplatePropValidityPeriod = 30
EnrollmentTemplateProperty_TemplatePropRenewalPeriod = 31
def _define_IX509CertificateTemplate_head():
    class IX509CertificateTemplate(win32more.System.Com.IDispatch_head):
        Guid = Guid('54244a13-555a-4e22-896d-1b0e52f76406')
    return IX509CertificateTemplate
def _define_IX509CertificateTemplate():
    IX509CertificateTemplate = win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head
    IX509CertificateTemplate.get_Property = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EnrollmentTemplateProperty,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Property', ((1, 'property'),(1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX509CertificateTemplate
def _define_IX509CertificateTemplates_head():
    class IX509CertificateTemplates(win32more.System.Com.IDispatch_head):
        Guid = Guid('13b79003-2181-11da-b2a4-000e7bbb2b09')
    return IX509CertificateTemplates
def _define_IX509CertificateTemplates():
    IX509CertificateTemplates = win32more.Security.Cryptography.Certificates.IX509CertificateTemplates_head
    IX509CertificateTemplates.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    IX509CertificateTemplates.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    IX509CertificateTemplates.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    IX509CertificateTemplates.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    IX509CertificateTemplates.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    IX509CertificateTemplates.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    IX509CertificateTemplates.get_ItemByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head), use_last_error=False)(13, 'get_ItemByName', ((1, 'bstrName'),(1, 'ppValue'),)))
    IX509CertificateTemplates.get_ItemByOid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head), use_last_error=False)(14, 'get_ItemByOid', ((1, 'pOid'),(1, 'ppValue'),)))
    win32more.System.Com.IDispatch
    return IX509CertificateTemplates
CommitTemplateFlags = Int32
CommitTemplateFlags_CommitFlagSaveTemplateGenerateOID = 1
CommitTemplateFlags_CommitFlagSaveTemplateUseCurrentOID = 2
CommitTemplateFlags_CommitFlagSaveTemplateOverwrite = 3
CommitTemplateFlags_CommitFlagDeleteTemplate = 4
def _define_IX509CertificateTemplateWritable_head():
    class IX509CertificateTemplateWritable(win32more.System.Com.IDispatch_head):
        Guid = Guid('f49466a7-395a-4e9e-b6e7-32b331600dc0')
    return IX509CertificateTemplateWritable
def _define_IX509CertificateTemplateWritable():
    IX509CertificateTemplateWritable = win32more.Security.Cryptography.Certificates.IX509CertificateTemplateWritable_head
    IX509CertificateTemplateWritable.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head, use_last_error=False)(7, 'Initialize', ((1, 'pValue'),)))
    IX509CertificateTemplateWritable.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CommitTemplateFlags,win32more.Foundation.BSTR, use_last_error=False)(8, 'Commit', ((1, 'commitFlags'),(1, 'strServerContext'),)))
    IX509CertificateTemplateWritable.get_Property = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EnrollmentTemplateProperty,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'get_Property', ((1, 'property'),(1, 'pValue'),)))
    IX509CertificateTemplateWritable.put_Property = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EnrollmentTemplateProperty,win32more.System.Com.VARIANT, use_last_error=False)(10, 'put_Property', ((1, 'property'),(1, 'value'),)))
    IX509CertificateTemplateWritable.get_Template = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head), use_last_error=False)(11, 'get_Template', ((1, 'ppValue'),)))
    win32more.System.Com.IDispatch
    return IX509CertificateTemplateWritable
EnrollmentCAProperty = Int32
EnrollmentCAProperty_CAPropCommonName = 1
EnrollmentCAProperty_CAPropDistinguishedName = 2
EnrollmentCAProperty_CAPropSanitizedName = 3
EnrollmentCAProperty_CAPropSanitizedShortName = 4
EnrollmentCAProperty_CAPropDNSName = 5
EnrollmentCAProperty_CAPropCertificateTypes = 6
EnrollmentCAProperty_CAPropCertificate = 7
EnrollmentCAProperty_CAPropDescription = 8
EnrollmentCAProperty_CAPropWebServers = 9
EnrollmentCAProperty_CAPropSiteName = 10
EnrollmentCAProperty_CAPropSecurity = 11
EnrollmentCAProperty_CAPropRenewalOnly = 12
def _define_ICertificationAuthority_head():
    class ICertificationAuthority(win32more.System.Com.IDispatch_head):
        Guid = Guid('835d1f61-1e95-4bc8-b4d3-976c42b968f7')
    return ICertificationAuthority
def _define_ICertificationAuthority():
    ICertificationAuthority = win32more.Security.Cryptography.Certificates.ICertificationAuthority_head
    ICertificationAuthority.get_Property = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EnrollmentCAProperty,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Property', ((1, 'property'),(1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return ICertificationAuthority
def _define_ICertificationAuthorities_head():
    class ICertificationAuthorities(win32more.System.Com.IDispatch_head):
        Guid = Guid('13b79005-2181-11da-b2a4-000e7bbb2b09')
    return ICertificationAuthorities
def _define_ICertificationAuthorities():
    ICertificationAuthorities = win32more.Security.Cryptography.Certificates.ICertificationAuthorities_head
    ICertificationAuthorities.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.ICertificationAuthority_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    ICertificationAuthorities.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    ICertificationAuthorities.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    ICertificationAuthorities.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICertificationAuthority_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    ICertificationAuthorities.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    ICertificationAuthorities.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    ICertificationAuthorities.ComputeSiteCosts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'ComputeSiteCosts', ()))
    ICertificationAuthorities.get_ItemByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Cryptography.Certificates.ICertificationAuthority_head), use_last_error=False)(14, 'get_ItemByName', ((1, 'strName'),(1, 'ppValue'),)))
    win32more.System.Com.IDispatch
    return ICertificationAuthorities
X509EnrollmentPolicyLoadOption = Int32
X509EnrollmentPolicyLoadOption_LoadOptionDefault = 0
X509EnrollmentPolicyLoadOption_LoadOptionCacheOnly = 1
X509EnrollmentPolicyLoadOption_LoadOptionReload = 2
X509EnrollmentPolicyLoadOption_LoadOptionRegisterForADChanges = 4
EnrollmentPolicyFlags = Int32
EnrollmentPolicyFlags_DisableGroupPolicyList = 2
EnrollmentPolicyFlags_DisableUserServerList = 4
PolicyServerUrlPropertyID = Int32
PolicyServerUrlPropertyID_PsPolicyID = 0
PolicyServerUrlPropertyID_PsFriendlyName = 1
X509EnrollmentPolicyExportFlags = Int32
X509EnrollmentPolicyExportFlags_ExportTemplates = 1
X509EnrollmentPolicyExportFlags_ExportOIDs = 2
X509EnrollmentPolicyExportFlags_ExportCAs = 4
def _define_IX509EnrollmentPolicyServer_head():
    class IX509EnrollmentPolicyServer(win32more.System.Com.IDispatch_head):
        Guid = Guid('13b79026-2181-11da-b2a4-000e7bbb2b09')
    return IX509EnrollmentPolicyServer
def _define_IX509EnrollmentPolicyServer():
    IX509EnrollmentPolicyServer = win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head
    IX509EnrollmentPolicyServer.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags,Int16,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext, use_last_error=False)(7, 'Initialize', ((1, 'bstrPolicyServerUrl'),(1, 'bstrPolicyServerId'),(1, 'authFlags'),(1, 'fIsUnTrusted'),(1, 'context'),)))
    IX509EnrollmentPolicyServer.LoadPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509EnrollmentPolicyLoadOption, use_last_error=False)(8, 'LoadPolicy', ((1, 'option'),)))
    IX509EnrollmentPolicyServer.GetTemplates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateTemplates_head), use_last_error=False)(9, 'GetTemplates', ((1, 'pTemplates'),)))
    IX509EnrollmentPolicyServer.GetCAsForTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head,POINTER(win32more.Security.Cryptography.Certificates.ICertificationAuthorities_head), use_last_error=False)(10, 'GetCAsForTemplate', ((1, 'pTemplate'),(1, 'ppCAs'),)))
    IX509EnrollmentPolicyServer.GetCAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICertificationAuthorities_head), use_last_error=False)(11, 'GetCAs', ((1, 'ppCAs'),)))
    IX509EnrollmentPolicyServer.Validate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Validate', ()))
    IX509EnrollmentPolicyServer.GetCustomOids = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectIds_head), use_last_error=False)(13, 'GetCustomOids', ((1, 'ppObjectIds'),)))
    IX509EnrollmentPolicyServer.GetNextUpdateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(14, 'GetNextUpdateTime', ((1, 'pDate'),)))
    IX509EnrollmentPolicyServer.GetLastUpdateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(15, 'GetLastUpdateTime', ((1, 'pDate'),)))
    IX509EnrollmentPolicyServer.GetPolicyServerUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'GetPolicyServerUrl', ((1, 'pValue'),)))
    IX509EnrollmentPolicyServer.GetPolicyServerId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'GetPolicyServerId', ((1, 'pValue'),)))
    IX509EnrollmentPolicyServer.GetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'GetFriendlyName', ((1, 'pValue'),)))
    IX509EnrollmentPolicyServer.GetIsDefaultCEP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(19, 'GetIsDefaultCEP', ((1, 'pValue'),)))
    IX509EnrollmentPolicyServer.GetUseClientId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(20, 'GetUseClientId', ((1, 'pValue'),)))
    IX509EnrollmentPolicyServer.GetAllowUnTrustedCA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(21, 'GetAllowUnTrustedCA', ((1, 'pValue'),)))
    IX509EnrollmentPolicyServer.GetCachePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'GetCachePath', ((1, 'pValue'),)))
    IX509EnrollmentPolicyServer.GetCacheDir = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'GetCacheDir', ((1, 'pValue'),)))
    IX509EnrollmentPolicyServer.GetAuthFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags), use_last_error=False)(24, 'GetAuthFlags', ((1, 'pValue'),)))
    IX509EnrollmentPolicyServer.SetCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(25, 'SetCredential', ((1, 'hWndParent'),(1, 'flag'),(1, 'strCredential'),(1, 'strPassword'),)))
    IX509EnrollmentPolicyServer.QueryChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(26, 'QueryChanges', ((1, 'pValue'),)))
    IX509EnrollmentPolicyServer.InitializeImport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(27, 'InitializeImport', ((1, 'val'),)))
    IX509EnrollmentPolicyServer.Export = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509EnrollmentPolicyExportFlags,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(28, 'Export', ((1, 'exportFlags'),(1, 'pVal'),)))
    IX509EnrollmentPolicyServer.get_Cost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(29, 'get_Cost', ((1, 'pValue'),)))
    IX509EnrollmentPolicyServer.put_Cost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(30, 'put_Cost', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IX509EnrollmentPolicyServer
def _define_IX509PolicyServerUrl_head():
    class IX509PolicyServerUrl(win32more.System.Com.IDispatch_head):
        Guid = Guid('884e204a-217d-11da-b2a4-000e7bbb2b09')
    return IX509PolicyServerUrl
def _define_IX509PolicyServerUrl():
    IX509PolicyServerUrl = win32more.Security.Cryptography.Certificates.IX509PolicyServerUrl_head
    IX509PolicyServerUrl.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext, use_last_error=False)(7, 'Initialize', ((1, 'context'),)))
    IX509PolicyServerUrl.get_Url = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Url', ((1, 'ppValue'),)))
    IX509PolicyServerUrl.put_Url = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'put_Url', ((1, 'pValue'),)))
    IX509PolicyServerUrl.get_Default = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_Default', ((1, 'pValue'),)))
    IX509PolicyServerUrl.put_Default = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(11, 'put_Default', ((1, 'value'),)))
    IX509PolicyServerUrl.get_Flags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.PolicyServerUrlFlags), use_last_error=False)(12, 'get_Flags', ((1, 'pValue'),)))
    IX509PolicyServerUrl.put_Flags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.PolicyServerUrlFlags, use_last_error=False)(13, 'put_Flags', ((1, 'Flags'),)))
    IX509PolicyServerUrl.get_AuthFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags), use_last_error=False)(14, 'get_AuthFlags', ((1, 'pValue'),)))
    IX509PolicyServerUrl.put_AuthFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags, use_last_error=False)(15, 'put_AuthFlags', ((1, 'Flags'),)))
    IX509PolicyServerUrl.get_Cost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(16, 'get_Cost', ((1, 'pValue'),)))
    IX509PolicyServerUrl.put_Cost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(17, 'put_Cost', ((1, 'value'),)))
    IX509PolicyServerUrl.GetStringProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.PolicyServerUrlPropertyID,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'GetStringProperty', ((1, 'propertyId'),(1, 'ppValue'),)))
    IX509PolicyServerUrl.SetStringProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.PolicyServerUrlPropertyID,win32more.Foundation.BSTR, use_last_error=False)(19, 'SetStringProperty', ((1, 'propertyId'),(1, 'pValue'),)))
    IX509PolicyServerUrl.UpdateRegistry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext, use_last_error=False)(20, 'UpdateRegistry', ((1, 'context'),)))
    IX509PolicyServerUrl.RemoveFromRegistry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext, use_last_error=False)(21, 'RemoveFromRegistry', ((1, 'context'),)))
    win32more.System.Com.IDispatch
    return IX509PolicyServerUrl
def _define_IX509PolicyServerListManager_head():
    class IX509PolicyServerListManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('884e204b-217d-11da-b2a4-000e7bbb2b09')
    return IX509PolicyServerListManager
def _define_IX509PolicyServerListManager():
    IX509PolicyServerListManager = win32more.Security.Cryptography.Certificates.IX509PolicyServerListManager_head
    IX509PolicyServerListManager.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.IX509PolicyServerUrl_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    IX509PolicyServerListManager.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    IX509PolicyServerListManager.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    IX509PolicyServerListManager.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509PolicyServerUrl_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    IX509PolicyServerListManager.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    IX509PolicyServerListManager.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    IX509PolicyServerListManager.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Security.Cryptography.Certificates.PolicyServerUrlFlags, use_last_error=False)(13, 'Initialize', ((1, 'context'),(1, 'Flags'),)))
    win32more.System.Com.IDispatch
    return IX509PolicyServerListManager
X509RequestType = Int32
X509RequestType_TypeAny = 0
X509RequestType_TypePkcs10 = 1
X509RequestType_TypePkcs7 = 2
X509RequestType_TypeCmc = 3
X509RequestType_TypeCertificate = 4
X509RequestInheritOptions = Int32
X509RequestInheritOptions_InheritDefault = 0
X509RequestInheritOptions_InheritNewDefaultKey = 1
X509RequestInheritOptions_InheritNewSimilarKey = 2
X509RequestInheritOptions_InheritPrivateKey = 3
X509RequestInheritOptions_InheritPublicKey = 4
X509RequestInheritOptions_InheritKeyMask = 15
X509RequestInheritOptions_InheritNone = 16
X509RequestInheritOptions_InheritRenewalCertificateFlag = 32
X509RequestInheritOptions_InheritTemplateFlag = 64
X509RequestInheritOptions_InheritSubjectFlag = 128
X509RequestInheritOptions_InheritExtensionsFlag = 256
X509RequestInheritOptions_InheritSubjectAltNameFlag = 512
X509RequestInheritOptions_InheritValidityPeriodFlag = 1024
X509RequestInheritOptions_InheritReserved80000000 = -2147483648
InnerRequestLevel = Int32
InnerRequestLevel_LevelInnermost = 0
InnerRequestLevel_LevelNext = 1
def _define_IX509CertificateRequest_head():
    class IX509CertificateRequest(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab341-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRequest
def _define_IX509CertificateRequest():
    IX509CertificateRequest = win32more.Security.Cryptography.Certificates.IX509CertificateRequest_head
    IX509CertificateRequest.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext, use_last_error=False)(7, 'Initialize', ((1, 'Context'),)))
    IX509CertificateRequest.Encode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Encode', ()))
    IX509CertificateRequest.ResetForEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'ResetForEncode', ()))
    IX509CertificateRequest.GetInnerRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.InnerRequestLevel,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateRequest_head), use_last_error=False)(10, 'GetInnerRequest', ((1, 'Level'),(1, 'ppValue'),)))
    IX509CertificateRequest.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509RequestType), use_last_error=False)(11, 'get_Type', ((1, 'pValue'),)))
    IX509CertificateRequest.get_EnrollmentContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext), use_last_error=False)(12, 'get_EnrollmentContext', ((1, 'pValue'),)))
    IX509CertificateRequest.get_Silent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_Silent', ((1, 'pValue'),)))
    IX509CertificateRequest.put_Silent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'put_Silent', ((1, 'Value'),)))
    IX509CertificateRequest.get_ParentWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_ParentWindow', ((1, 'pValue'),)))
    IX509CertificateRequest.put_ParentWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_ParentWindow', ((1, 'Value'),)))
    IX509CertificateRequest.get_UIContextMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_UIContextMessage', ((1, 'pValue'),)))
    IX509CertificateRequest.put_UIContextMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_UIContextMessage', ((1, 'Value'),)))
    IX509CertificateRequest.get_SuppressDefaults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(19, 'get_SuppressDefaults', ((1, 'pValue'),)))
    IX509CertificateRequest.put_SuppressDefaults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(20, 'put_SuppressDefaults', ((1, 'Value'),)))
    IX509CertificateRequest.get_RenewalCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_RenewalCertificate', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRequest.put_RenewalCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(22, 'put_RenewalCertificate', ((1, 'Encoding'),(1, 'Value'),)))
    IX509CertificateRequest.get_ClientId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.RequestClientInfoClientId), use_last_error=False)(23, 'get_ClientId', ((1, 'pValue'),)))
    IX509CertificateRequest.put_ClientId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.RequestClientInfoClientId, use_last_error=False)(24, 'put_ClientId', ((1, 'Value'),)))
    IX509CertificateRequest.get_CspInformations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICspInformations_head), use_last_error=False)(25, 'get_CspInformations', ((1, 'ppValue'),)))
    IX509CertificateRequest.put_CspInformations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ICspInformations_head, use_last_error=False)(26, 'put_CspInformations', ((1, 'pValue'),)))
    IX509CertificateRequest.get_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(27, 'get_HashAlgorithm', ((1, 'ppValue'),)))
    IX509CertificateRequest.put_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head, use_last_error=False)(28, 'put_HashAlgorithm', ((1, 'pValue'),)))
    IX509CertificateRequest.get_AlternateSignatureAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(29, 'get_AlternateSignatureAlgorithm', ((1, 'pValue'),)))
    IX509CertificateRequest.put_AlternateSignatureAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(30, 'put_AlternateSignatureAlgorithm', ((1, 'Value'),)))
    IX509CertificateRequest.get_RawData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(31, 'get_RawData', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX509CertificateRequest
Pkcs10AllowedSignatureTypes = Int32
Pkcs10AllowedSignatureTypes_AllowedKeySignature = 1
Pkcs10AllowedSignatureTypes_AllowedNullSignature = 2
def _define_IX509CertificateRequestPkcs10_head():
    class IX509CertificateRequestPkcs10(win32more.Security.Cryptography.Certificates.IX509CertificateRequest_head):
        Guid = Guid('728ab342-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRequestPkcs10
def _define_IX509CertificateRequestPkcs10():
    IX509CertificateRequestPkcs10 = win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10_head
    IX509CertificateRequestPkcs10.InitializeFromTemplateName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Foundation.BSTR, use_last_error=False)(32, 'InitializeFromTemplateName', ((1, 'Context'),(1, 'strTemplateName'),)))
    IX509CertificateRequestPkcs10.InitializeFromPrivateKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Security.Cryptography.Certificates.IX509PrivateKey_head,win32more.Foundation.BSTR, use_last_error=False)(33, 'InitializeFromPrivateKey', ((1, 'Context'),(1, 'pPrivateKey'),(1, 'strTemplateName'),)))
    IX509CertificateRequestPkcs10.InitializeFromPublicKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Security.Cryptography.Certificates.IX509PublicKey_head,win32more.Foundation.BSTR, use_last_error=False)(34, 'InitializeFromPublicKey', ((1, 'Context'),(1, 'pPublicKey'),(1, 'strTemplateName'),)))
    IX509CertificateRequestPkcs10.InitializeFromCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Security.Cryptography.Certificates.X509RequestInheritOptions, use_last_error=False)(35, 'InitializeFromCertificate', ((1, 'Context'),(1, 'strCertificate'),(1, 'Encoding'),(1, 'InheritOptions'),)))
    IX509CertificateRequestPkcs10.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(36, 'InitializeDecode', ((1, 'strEncodedData'),(1, 'Encoding'),)))
    IX509CertificateRequestPkcs10.CheckSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.Pkcs10AllowedSignatureTypes, use_last_error=False)(37, 'CheckSignature', ((1, 'AllowedSignatureTypes'),)))
    IX509CertificateRequestPkcs10.IsSmartCard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(38, 'IsSmartCard', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10.get_TemplateObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(39, 'get_TemplateObjectId', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs10.get_PublicKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509PublicKey_head), use_last_error=False)(40, 'get_PublicKey', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs10.get_PrivateKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509PrivateKey_head), use_last_error=False)(41, 'get_PrivateKey', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs10.get_NullSigned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(42, 'get_NullSigned', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10.get_ReuseKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(43, 'get_ReuseKey', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10.get_OldCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(44, 'get_OldCertificate', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRequestPkcs10.get_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX500DistinguishedName_head), use_last_error=False)(45, 'get_Subject', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs10.put_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX500DistinguishedName_head, use_last_error=False)(46, 'put_Subject', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10.get_CspStatuses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICspStatuses_head), use_last_error=False)(47, 'get_CspStatuses', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs10.get_SmimeCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(48, 'get_SmimeCapabilities', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10.put_SmimeCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(49, 'put_SmimeCapabilities', ((1, 'Value'),)))
    IX509CertificateRequestPkcs10.get_SignatureInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509SignatureInformation_head), use_last_error=False)(50, 'get_SignatureInformation', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs10.get_KeyContainerNamePrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(51, 'get_KeyContainerNamePrefix', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10.put_KeyContainerNamePrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(52, 'put_KeyContainerNamePrefix', ((1, 'Value'),)))
    IX509CertificateRequestPkcs10.get_CryptAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICryptAttributes_head), use_last_error=False)(53, 'get_CryptAttributes', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs10.get_X509Extensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509Extensions_head), use_last_error=False)(54, 'get_X509Extensions', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs10.get_CriticalExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectIds_head), use_last_error=False)(55, 'get_CriticalExtensions', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs10.get_SuppressOids = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectIds_head), use_last_error=False)(56, 'get_SuppressOids', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs10.get_RawDataToBeSigned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(57, 'get_RawDataToBeSigned', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRequestPkcs10.get_Signature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(58, 'get_Signature', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRequestPkcs10.GetCspStatuses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509KeySpec,POINTER(win32more.Security.Cryptography.Certificates.ICspStatuses_head), use_last_error=False)(59, 'GetCspStatuses', ((1, 'KeySpec'),(1, 'ppCspStatuses'),)))
    win32more.Security.Cryptography.Certificates.IX509CertificateRequest
    return IX509CertificateRequestPkcs10
def _define_IX509CertificateRequestPkcs10V2_head():
    class IX509CertificateRequestPkcs10V2(win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10_head):
        Guid = Guid('728ab35b-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRequestPkcs10V2
def _define_IX509CertificateRequestPkcs10V2():
    IX509CertificateRequestPkcs10V2 = win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10V2_head
    IX509CertificateRequestPkcs10V2.InitializeFromTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head, use_last_error=False)(60, 'InitializeFromTemplate', ((1, 'context'),(1, 'pPolicyServer'),(1, 'pTemplate'),)))
    IX509CertificateRequestPkcs10V2.InitializeFromPrivateKeyTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Security.Cryptography.Certificates.IX509PrivateKey_head,win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head, use_last_error=False)(61, 'InitializeFromPrivateKeyTemplate', ((1, 'Context'),(1, 'pPrivateKey'),(1, 'pPolicyServer'),(1, 'pTemplate'),)))
    IX509CertificateRequestPkcs10V2.InitializeFromPublicKeyTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Security.Cryptography.Certificates.IX509PublicKey_head,win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head, use_last_error=False)(62, 'InitializeFromPublicKeyTemplate', ((1, 'Context'),(1, 'pPublicKey'),(1, 'pPolicyServer'),(1, 'pTemplate'),)))
    IX509CertificateRequestPkcs10V2.get_PolicyServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head), use_last_error=False)(63, 'get_PolicyServer', ((1, 'ppPolicyServer'),)))
    IX509CertificateRequestPkcs10V2.get_Template = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head), use_last_error=False)(64, 'get_Template', ((1, 'ppTemplate'),)))
    win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10
    return IX509CertificateRequestPkcs10V2
def _define_IX509CertificateRequestPkcs10V3_head():
    class IX509CertificateRequestPkcs10V3(win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10V2_head):
        Guid = Guid('54ea9942-3d66-4530-b76e-7c9170d3ec52')
    return IX509CertificateRequestPkcs10V3
def _define_IX509CertificateRequestPkcs10V3():
    IX509CertificateRequestPkcs10V3 = win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10V3_head
    IX509CertificateRequestPkcs10V3.get_AttestPrivateKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(65, 'get_AttestPrivateKey', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10V3.put_AttestPrivateKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(66, 'put_AttestPrivateKey', ((1, 'Value'),)))
    IX509CertificateRequestPkcs10V3.get_AttestationEncryptionCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(67, 'get_AttestationEncryptionCertificate', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRequestPkcs10V3.put_AttestationEncryptionCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(68, 'put_AttestationEncryptionCertificate', ((1, 'Encoding'),(1, 'Value'),)))
    IX509CertificateRequestPkcs10V3.get_EncryptionAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(69, 'get_EncryptionAlgorithm', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs10V3.put_EncryptionAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head, use_last_error=False)(70, 'put_EncryptionAlgorithm', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10V3.get_EncryptionStrength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(71, 'get_EncryptionStrength', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10V3.put_EncryptionStrength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(72, 'put_EncryptionStrength', ((1, 'Value'),)))
    IX509CertificateRequestPkcs10V3.get_ChallengePassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(73, 'get_ChallengePassword', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10V3.put_ChallengePassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(74, 'put_ChallengePassword', ((1, 'Value'),)))
    IX509CertificateRequestPkcs10V3.get_NameValuePairs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509NameValuePairs_head), use_last_error=False)(75, 'get_NameValuePairs', ((1, 'ppValue'),)))
    win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10V2
    return IX509CertificateRequestPkcs10V3
KeyAttestationClaimType = Int32
XCN_NCRYPT_CLAIM_NONE = 0
XCN_NCRYPT_CLAIM_AUTHORITY_AND_SUBJECT = 3
XCN_NCRYPT_CLAIM_AUTHORITY_ONLY = 1
XCN_NCRYPT_CLAIM_SUBJECT_ONLY = 2
XCN_NCRYPT_CLAIM_UNKNOWN = 4096
def _define_IX509CertificateRequestPkcs10V4_head():
    class IX509CertificateRequestPkcs10V4(win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10V3_head):
        Guid = Guid('728ab363-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRequestPkcs10V4
def _define_IX509CertificateRequestPkcs10V4():
    IX509CertificateRequestPkcs10V4 = win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10V4_head
    IX509CertificateRequestPkcs10V4.get_ClaimType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.KeyAttestationClaimType), use_last_error=False)(76, 'get_ClaimType', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10V4.put_ClaimType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.KeyAttestationClaimType, use_last_error=False)(77, 'put_ClaimType', ((1, 'Value'),)))
    IX509CertificateRequestPkcs10V4.get_AttestPrivateKeyPreferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(78, 'get_AttestPrivateKeyPreferred', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs10V4.put_AttestPrivateKeyPreferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(79, 'put_AttestPrivateKeyPreferred', ((1, 'Value'),)))
    win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10V3
    return IX509CertificateRequestPkcs10V4
def _define_IX509CertificateRequestCertificate_head():
    class IX509CertificateRequestCertificate(win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10_head):
        Guid = Guid('728ab343-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRequestCertificate
def _define_IX509CertificateRequestCertificate():
    IX509CertificateRequestCertificate = win32more.Security.Cryptography.Certificates.IX509CertificateRequestCertificate_head
    IX509CertificateRequestCertificate.CheckPublicKeySignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509PublicKey_head, use_last_error=False)(60, 'CheckPublicKeySignature', ((1, 'pPublicKey'),)))
    IX509CertificateRequestCertificate.get_Issuer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX500DistinguishedName_head), use_last_error=False)(61, 'get_Issuer', ((1, 'ppValue'),)))
    IX509CertificateRequestCertificate.put_Issuer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX500DistinguishedName_head, use_last_error=False)(62, 'put_Issuer', ((1, 'pValue'),)))
    IX509CertificateRequestCertificate.get_NotBefore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(63, 'get_NotBefore', ((1, 'pValue'),)))
    IX509CertificateRequestCertificate.put_NotBefore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(64, 'put_NotBefore', ((1, 'Value'),)))
    IX509CertificateRequestCertificate.get_NotAfter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(65, 'get_NotAfter', ((1, 'pValue'),)))
    IX509CertificateRequestCertificate.put_NotAfter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(66, 'put_NotAfter', ((1, 'Value'),)))
    IX509CertificateRequestCertificate.get_SerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(67, 'get_SerialNumber', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRequestCertificate.put_SerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(68, 'put_SerialNumber', ((1, 'Encoding'),(1, 'Value'),)))
    IX509CertificateRequestCertificate.get_SignerCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ISignerCertificate_head), use_last_error=False)(69, 'get_SignerCertificate', ((1, 'ppValue'),)))
    IX509CertificateRequestCertificate.put_SignerCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ISignerCertificate_head, use_last_error=False)(70, 'put_SignerCertificate', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10
    return IX509CertificateRequestCertificate
def _define_IX509CertificateRequestCertificate2_head():
    class IX509CertificateRequestCertificate2(win32more.Security.Cryptography.Certificates.IX509CertificateRequestCertificate_head):
        Guid = Guid('728ab35a-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRequestCertificate2
def _define_IX509CertificateRequestCertificate2():
    IX509CertificateRequestCertificate2 = win32more.Security.Cryptography.Certificates.IX509CertificateRequestCertificate2_head
    IX509CertificateRequestCertificate2.InitializeFromTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head, use_last_error=False)(71, 'InitializeFromTemplate', ((1, 'context'),(1, 'pPolicyServer'),(1, 'pTemplate'),)))
    IX509CertificateRequestCertificate2.InitializeFromPrivateKeyTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Security.Cryptography.Certificates.IX509PrivateKey_head,win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head, use_last_error=False)(72, 'InitializeFromPrivateKeyTemplate', ((1, 'Context'),(1, 'pPrivateKey'),(1, 'pPolicyServer'),(1, 'pTemplate'),)))
    IX509CertificateRequestCertificate2.get_PolicyServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head), use_last_error=False)(73, 'get_PolicyServer', ((1, 'ppPolicyServer'),)))
    IX509CertificateRequestCertificate2.get_Template = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head), use_last_error=False)(74, 'get_Template', ((1, 'ppTemplate'),)))
    win32more.Security.Cryptography.Certificates.IX509CertificateRequestCertificate
    return IX509CertificateRequestCertificate2
def _define_IX509CertificateRequestPkcs7_head():
    class IX509CertificateRequestPkcs7(win32more.Security.Cryptography.Certificates.IX509CertificateRequest_head):
        Guid = Guid('728ab344-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRequestPkcs7
def _define_IX509CertificateRequestPkcs7():
    IX509CertificateRequestPkcs7 = win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs7_head
    IX509CertificateRequestPkcs7.InitializeFromTemplateName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Foundation.BSTR, use_last_error=False)(32, 'InitializeFromTemplateName', ((1, 'Context'),(1, 'strTemplateName'),)))
    IX509CertificateRequestPkcs7.InitializeFromCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,Int16,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Security.Cryptography.Certificates.X509RequestInheritOptions, use_last_error=False)(33, 'InitializeFromCertificate', ((1, 'Context'),(1, 'RenewalRequest'),(1, 'strCertificate'),(1, 'Encoding'),(1, 'InheritOptions'),)))
    IX509CertificateRequestPkcs7.InitializeFromInnerRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509CertificateRequest_head, use_last_error=False)(34, 'InitializeFromInnerRequest', ((1, 'pInnerRequest'),)))
    IX509CertificateRequestPkcs7.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(35, 'InitializeDecode', ((1, 'strEncodedData'),(1, 'Encoding'),)))
    IX509CertificateRequestPkcs7.get_RequesterName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'get_RequesterName', ((1, 'pValue'),)))
    IX509CertificateRequestPkcs7.put_RequesterName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'put_RequesterName', ((1, 'Value'),)))
    IX509CertificateRequestPkcs7.get_SignerCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ISignerCertificate_head), use_last_error=False)(38, 'get_SignerCertificate', ((1, 'ppValue'),)))
    IX509CertificateRequestPkcs7.put_SignerCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ISignerCertificate_head, use_last_error=False)(39, 'put_SignerCertificate', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509CertificateRequest
    return IX509CertificateRequestPkcs7
def _define_IX509CertificateRequestPkcs7V2_head():
    class IX509CertificateRequestPkcs7V2(win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs7_head):
        Guid = Guid('728ab35c-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRequestPkcs7V2
def _define_IX509CertificateRequestPkcs7V2():
    IX509CertificateRequestPkcs7V2 = win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs7V2_head
    IX509CertificateRequestPkcs7V2.InitializeFromTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head, use_last_error=False)(40, 'InitializeFromTemplate', ((1, 'context'),(1, 'pPolicyServer'),(1, 'pTemplate'),)))
    IX509CertificateRequestPkcs7V2.get_PolicyServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head), use_last_error=False)(41, 'get_PolicyServer', ((1, 'ppPolicyServer'),)))
    IX509CertificateRequestPkcs7V2.get_Template = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head), use_last_error=False)(42, 'get_Template', ((1, 'ppTemplate'),)))
    IX509CertificateRequestPkcs7V2.CheckCertificateSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(43, 'CheckCertificateSignature', ((1, 'ValidateCertificateChain'),)))
    win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs7
    return IX509CertificateRequestPkcs7V2
def _define_IX509CertificateRequestCmc_head():
    class IX509CertificateRequestCmc(win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs7_head):
        Guid = Guid('728ab345-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRequestCmc
def _define_IX509CertificateRequestCmc():
    IX509CertificateRequestCmc = win32more.Security.Cryptography.Certificates.IX509CertificateRequestCmc_head
    IX509CertificateRequestCmc.InitializeFromInnerRequestTemplateName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509CertificateRequest_head,win32more.Foundation.BSTR, use_last_error=False)(40, 'InitializeFromInnerRequestTemplateName', ((1, 'pInnerRequest'),(1, 'strTemplateName'),)))
    IX509CertificateRequestCmc.get_TemplateObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(41, 'get_TemplateObjectId', ((1, 'ppValue'),)))
    IX509CertificateRequestCmc.get_NullSigned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(42, 'get_NullSigned', ((1, 'pValue'),)))
    IX509CertificateRequestCmc.get_CryptAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICryptAttributes_head), use_last_error=False)(43, 'get_CryptAttributes', ((1, 'ppValue'),)))
    IX509CertificateRequestCmc.get_NameValuePairs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509NameValuePairs_head), use_last_error=False)(44, 'get_NameValuePairs', ((1, 'ppValue'),)))
    IX509CertificateRequestCmc.get_X509Extensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509Extensions_head), use_last_error=False)(45, 'get_X509Extensions', ((1, 'ppValue'),)))
    IX509CertificateRequestCmc.get_CriticalExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectIds_head), use_last_error=False)(46, 'get_CriticalExtensions', ((1, 'ppValue'),)))
    IX509CertificateRequestCmc.get_SuppressOids = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectIds_head), use_last_error=False)(47, 'get_SuppressOids', ((1, 'ppValue'),)))
    IX509CertificateRequestCmc.get_TransactionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(48, 'get_TransactionId', ((1, 'pValue'),)))
    IX509CertificateRequestCmc.put_TransactionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(49, 'put_TransactionId', ((1, 'Value'),)))
    IX509CertificateRequestCmc.get_SenderNonce = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(50, 'get_SenderNonce', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRequestCmc.put_SenderNonce = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(51, 'put_SenderNonce', ((1, 'Encoding'),(1, 'Value'),)))
    IX509CertificateRequestCmc.get_SignatureInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509SignatureInformation_head), use_last_error=False)(52, 'get_SignatureInformation', ((1, 'ppValue'),)))
    IX509CertificateRequestCmc.get_ArchivePrivateKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(53, 'get_ArchivePrivateKey', ((1, 'pValue'),)))
    IX509CertificateRequestCmc.put_ArchivePrivateKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(54, 'put_ArchivePrivateKey', ((1, 'Value'),)))
    IX509CertificateRequestCmc.get_KeyArchivalCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(55, 'get_KeyArchivalCertificate', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRequestCmc.put_KeyArchivalCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(56, 'put_KeyArchivalCertificate', ((1, 'Encoding'),(1, 'Value'),)))
    IX509CertificateRequestCmc.get_EncryptionAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(57, 'get_EncryptionAlgorithm', ((1, 'ppValue'),)))
    IX509CertificateRequestCmc.put_EncryptionAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head, use_last_error=False)(58, 'put_EncryptionAlgorithm', ((1, 'pValue'),)))
    IX509CertificateRequestCmc.get_EncryptionStrength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(59, 'get_EncryptionStrength', ((1, 'pValue'),)))
    IX509CertificateRequestCmc.put_EncryptionStrength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(60, 'put_EncryptionStrength', ((1, 'Value'),)))
    IX509CertificateRequestCmc.get_EncryptedKeyHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(61, 'get_EncryptedKeyHash', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRequestCmc.get_SignerCertificates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ISignerCertificates_head), use_last_error=False)(62, 'get_SignerCertificates', ((1, 'ppValue'),)))
    win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs7
    return IX509CertificateRequestCmc
def _define_IX509CertificateRequestCmc2_head():
    class IX509CertificateRequestCmc2(win32more.Security.Cryptography.Certificates.IX509CertificateRequestCmc_head):
        Guid = Guid('728ab35d-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRequestCmc2
def _define_IX509CertificateRequestCmc2():
    IX509CertificateRequestCmc2 = win32more.Security.Cryptography.Certificates.IX509CertificateRequestCmc2_head
    IX509CertificateRequestCmc2.InitializeFromTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head, use_last_error=False)(63, 'InitializeFromTemplate', ((1, 'context'),(1, 'pPolicyServer'),(1, 'pTemplate'),)))
    IX509CertificateRequestCmc2.InitializeFromInnerRequestTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509CertificateRequest_head,win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head, use_last_error=False)(64, 'InitializeFromInnerRequestTemplate', ((1, 'pInnerRequest'),(1, 'pPolicyServer'),(1, 'pTemplate'),)))
    IX509CertificateRequestCmc2.get_PolicyServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head), use_last_error=False)(65, 'get_PolicyServer', ((1, 'ppPolicyServer'),)))
    IX509CertificateRequestCmc2.get_Template = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head), use_last_error=False)(66, 'get_Template', ((1, 'ppTemplate'),)))
    IX509CertificateRequestCmc2.CheckSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.Pkcs10AllowedSignatureTypes, use_last_error=False)(67, 'CheckSignature', ((1, 'AllowedSignatureTypes'),)))
    IX509CertificateRequestCmc2.CheckCertificateSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ISignerCertificate_head,Int16, use_last_error=False)(68, 'CheckCertificateSignature', ((1, 'pSignerCertificate'),(1, 'ValidateCertificateChain'),)))
    win32more.Security.Cryptography.Certificates.IX509CertificateRequestCmc
    return IX509CertificateRequestCmc2
InstallResponseRestrictionFlags = Int32
InstallResponseRestrictionFlags_AllowNone = 0
InstallResponseRestrictionFlags_AllowNoOutstandingRequest = 1
InstallResponseRestrictionFlags_AllowUntrustedCertificate = 2
InstallResponseRestrictionFlags_AllowUntrustedRoot = 4
def _define_IX509Enrollment_head():
    class IX509Enrollment(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab346-217d-11da-b2a4-000e7bbb2b09')
    return IX509Enrollment
def _define_IX509Enrollment():
    IX509Enrollment = win32more.Security.Cryptography.Certificates.IX509Enrollment_head
    IX509Enrollment.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext, use_last_error=False)(7, 'Initialize', ((1, 'Context'),)))
    IX509Enrollment.InitializeFromTemplateName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Foundation.BSTR, use_last_error=False)(8, 'InitializeFromTemplateName', ((1, 'Context'),(1, 'strTemplateName'),)))
    IX509Enrollment.InitializeFromRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509CertificateRequest_head, use_last_error=False)(9, 'InitializeFromRequest', ((1, 'pRequest'),)))
    IX509Enrollment.CreateRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'CreateRequest', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509Enrollment.Enroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Enroll', ()))
    IX509Enrollment.InstallResponse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.InstallResponseRestrictionFlags,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(12, 'InstallResponse', ((1, 'Restrictions'),(1, 'strResponse'),(1, 'Encoding'),(1, 'strPassword'),)))
    IX509Enrollment.CreatePFX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.PFXExportOptions,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'CreatePFX', ((1, 'strPassword'),(1, 'ExportOptions'),(1, 'Encoding'),(1, 'pValue'),)))
    IX509Enrollment.get_Request = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateRequest_head), use_last_error=False)(14, 'get_Request', ((1, 'pValue'),)))
    IX509Enrollment.get_Silent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_Silent', ((1, 'pValue'),)))
    IX509Enrollment.put_Silent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(16, 'put_Silent', ((1, 'Value'),)))
    IX509Enrollment.get_ParentWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_ParentWindow', ((1, 'pValue'),)))
    IX509Enrollment.put_ParentWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_ParentWindow', ((1, 'Value'),)))
    IX509Enrollment.get_NameValuePairs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509NameValuePairs_head), use_last_error=False)(19, 'get_NameValuePairs', ((1, 'ppValue'),)))
    IX509Enrollment.get_EnrollmentContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext), use_last_error=False)(20, 'get_EnrollmentContext', ((1, 'pValue'),)))
    IX509Enrollment.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509EnrollmentStatus_head), use_last_error=False)(21, 'get_Status', ((1, 'ppValue'),)))
    IX509Enrollment.get_Certificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_Certificate', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509Enrollment.get_Response = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_Response', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509Enrollment.get_CertificateFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_CertificateFriendlyName', ((1, 'pValue'),)))
    IX509Enrollment.put_CertificateFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_CertificateFriendlyName', ((1, 'strValue'),)))
    IX509Enrollment.get_CertificateDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'get_CertificateDescription', ((1, 'pValue'),)))
    IX509Enrollment.put_CertificateDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(27, 'put_CertificateDescription', ((1, 'strValue'),)))
    IX509Enrollment.get_RequestId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(28, 'get_RequestId', ((1, 'pValue'),)))
    IX509Enrollment.get_CAConfigString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(29, 'get_CAConfigString', ((1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX509Enrollment
def _define_IX509Enrollment2_head():
    class IX509Enrollment2(win32more.Security.Cryptography.Certificates.IX509Enrollment_head):
        Guid = Guid('728ab350-217d-11da-b2a4-000e7bbb2b09')
    return IX509Enrollment2
def _define_IX509Enrollment2():
    IX509Enrollment2 = win32more.Security.Cryptography.Certificates.IX509Enrollment2_head
    IX509Enrollment2.InitializeFromTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head,win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head, use_last_error=False)(30, 'InitializeFromTemplate', ((1, 'context'),(1, 'pPolicyServer'),(1, 'pTemplate'),)))
    IX509Enrollment2.InstallResponse2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.InstallResponseRestrictionFlags,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.PolicyServerUrlFlags,win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags, use_last_error=False)(31, 'InstallResponse2', ((1, 'Restrictions'),(1, 'strResponse'),(1, 'Encoding'),(1, 'strPassword'),(1, 'strEnrollmentPolicyServerUrl'),(1, 'strEnrollmentPolicyServerID'),(1, 'EnrollmentPolicyServerFlags'),(1, 'authFlags'),)))
    IX509Enrollment2.get_PolicyServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509EnrollmentPolicyServer_head), use_last_error=False)(32, 'get_PolicyServer', ((1, 'ppPolicyServer'),)))
    IX509Enrollment2.get_Template = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateTemplate_head), use_last_error=False)(33, 'get_Template', ((1, 'ppTemplate'),)))
    IX509Enrollment2.get_RequestIdString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(34, 'get_RequestIdString', ((1, 'pValue'),)))
    win32more.Security.Cryptography.Certificates.IX509Enrollment
    return IX509Enrollment2
WebEnrollmentFlags = Int32
WebEnrollmentFlags_EnrollPrompt = 1
def _define_IX509EnrollmentHelper_head():
    class IX509EnrollmentHelper(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab351-217d-11da-b2a4-000e7bbb2b09')
    return IX509EnrollmentHelper
def _define_IX509EnrollmentHelper():
    IX509EnrollmentHelper = win32more.Security.Cryptography.Certificates.IX509EnrollmentHelper_head
    IX509EnrollmentHelper.AddPolicyServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.PolicyServerUrlFlags,win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(7, 'AddPolicyServer', ((1, 'strEnrollmentPolicyServerURI'),(1, 'strEnrollmentPolicyID'),(1, 'EnrollmentPolicyServerFlags'),(1, 'authFlags'),(1, 'strCredential'),(1, 'strPassword'),)))
    IX509EnrollmentHelper.AddEnrollmentServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.X509EnrollmentAuthFlags,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(8, 'AddEnrollmentServer', ((1, 'strEnrollmentServerURI'),(1, 'authFlags'),(1, 'strCredential'),(1, 'strPassword'),)))
    IX509EnrollmentHelper.Enroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Security.Cryptography.Certificates.WebEnrollmentFlags,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'Enroll', ((1, 'strEnrollmentPolicyServerURI'),(1, 'strTemplateName'),(1, 'Encoding'),(1, 'enrollFlags'),(1, 'pstrCertificate'),)))
    IX509EnrollmentHelper.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext, use_last_error=False)(10, 'Initialize', ((1, 'Context'),)))
    win32more.System.Com.IDispatch
    return IX509EnrollmentHelper
def _define_IX509EnrollmentWebClassFactory_head():
    class IX509EnrollmentWebClassFactory(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab349-217d-11da-b2a4-000e7bbb2b09')
    return IX509EnrollmentWebClassFactory
def _define_IX509EnrollmentWebClassFactory():
    IX509EnrollmentWebClassFactory = win32more.Security.Cryptography.Certificates.IX509EnrollmentWebClassFactory_head
    IX509EnrollmentWebClassFactory.CreateObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'CreateObject', ((1, 'strProgID'),(1, 'ppIUnknown'),)))
    win32more.System.Com.IDispatch
    return IX509EnrollmentWebClassFactory
def _define_IX509MachineEnrollmentFactory_head():
    class IX509MachineEnrollmentFactory(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab352-217d-11da-b2a4-000e7bbb2b09')
    return IX509MachineEnrollmentFactory
def _define_IX509MachineEnrollmentFactory():
    IX509MachineEnrollmentFactory = win32more.Security.Cryptography.Certificates.IX509MachineEnrollmentFactory_head
    IX509MachineEnrollmentFactory.CreateObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Cryptography.Certificates.IX509EnrollmentHelper_head), use_last_error=False)(7, 'CreateObject', ((1, 'strProgID'),(1, 'ppIHelper'),)))
    win32more.System.Com.IDispatch
    return IX509MachineEnrollmentFactory
CRLRevocationReason = Int32
XCN_CRL_REASON_UNSPECIFIED = 0
XCN_CRL_REASON_KEY_COMPROMISE = 1
XCN_CRL_REASON_CA_COMPROMISE = 2
XCN_CRL_REASON_AFFILIATION_CHANGED = 3
XCN_CRL_REASON_SUPERSEDED = 4
XCN_CRL_REASON_CESSATION_OF_OPERATION = 5
XCN_CRL_REASON_CERTIFICATE_HOLD = 6
XCN_CRL_REASON_REMOVE_FROM_CRL = 8
XCN_CRL_REASON_PRIVILEGE_WITHDRAWN = 9
XCN_CRL_REASON_AA_COMPROMISE = 10
def _define_IX509CertificateRevocationListEntry_head():
    class IX509CertificateRevocationListEntry(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab35e-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRevocationListEntry
def _define_IX509CertificateRevocationListEntry():
    IX509CertificateRevocationListEntry = win32more.Security.Cryptography.Certificates.IX509CertificateRevocationListEntry_head
    IX509CertificateRevocationListEntry.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR,Double, use_last_error=False)(7, 'Initialize', ((1, 'Encoding'),(1, 'SerialNumber'),(1, 'RevocationDate'),)))
    IX509CertificateRevocationListEntry.get_SerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_SerialNumber', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRevocationListEntry.get_RevocationDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(9, 'get_RevocationDate', ((1, 'pValue'),)))
    IX509CertificateRevocationListEntry.get_RevocationReason = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.CRLRevocationReason), use_last_error=False)(10, 'get_RevocationReason', ((1, 'pValue'),)))
    IX509CertificateRevocationListEntry.put_RevocationReason = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CRLRevocationReason, use_last_error=False)(11, 'put_RevocationReason', ((1, 'Value'),)))
    IX509CertificateRevocationListEntry.get_X509Extensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509Extensions_head), use_last_error=False)(12, 'get_X509Extensions', ((1, 'ppValue'),)))
    IX509CertificateRevocationListEntry.get_CriticalExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectIds_head), use_last_error=False)(13, 'get_CriticalExtensions', ((1, 'ppValue'),)))
    win32more.System.Com.IDispatch
    return IX509CertificateRevocationListEntry
def _define_IX509CertificateRevocationListEntries_head():
    class IX509CertificateRevocationListEntries(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab35f-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRevocationListEntries
def _define_IX509CertificateRevocationListEntries():
    IX509CertificateRevocationListEntries = win32more.Security.Cryptography.Certificates.IX509CertificateRevocationListEntries_head
    IX509CertificateRevocationListEntries.get_ItemByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateRevocationListEntry_head), use_last_error=False)(7, 'get_ItemByIndex', ((1, 'Index'),(1, 'pVal'),)))
    IX509CertificateRevocationListEntries.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    IX509CertificateRevocationListEntries.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'pVal'),)))
    IX509CertificateRevocationListEntries.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509CertificateRevocationListEntry_head, use_last_error=False)(10, 'Add', ((1, 'pVal'),)))
    IX509CertificateRevocationListEntries.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    IX509CertificateRevocationListEntries.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    IX509CertificateRevocationListEntries.get_IndexBySerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(13, 'get_IndexBySerialNumber', ((1, 'Encoding'),(1, 'SerialNumber'),(1, 'pIndex'),)))
    IX509CertificateRevocationListEntries.AddRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509CertificateRevocationListEntries_head, use_last_error=False)(14, 'AddRange', ((1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX509CertificateRevocationListEntries
def _define_IX509CertificateRevocationList_head():
    class IX509CertificateRevocationList(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab360-217d-11da-b2a4-000e7bbb2b09')
    return IX509CertificateRevocationList
def _define_IX509CertificateRevocationList():
    IX509CertificateRevocationList = win32more.Security.Cryptography.Certificates.IX509CertificateRevocationList_head
    IX509CertificateRevocationList.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Initialize', ()))
    IX509CertificateRevocationList.InitializeDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(8, 'InitializeDecode', ((1, 'strEncodedData'),(1, 'Encoding'),)))
    IX509CertificateRevocationList.Encode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Encode', ()))
    IX509CertificateRevocationList.ResetForEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'ResetForEncode', ()))
    IX509CertificateRevocationList.CheckPublicKeySignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509PublicKey_head, use_last_error=False)(11, 'CheckPublicKeySignature', ((1, 'pPublicKey'),)))
    IX509CertificateRevocationList.CheckSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'CheckSignature', ()))
    IX509CertificateRevocationList.get_Issuer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX500DistinguishedName_head), use_last_error=False)(13, 'get_Issuer', ((1, 'ppValue'),)))
    IX509CertificateRevocationList.put_Issuer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX500DistinguishedName_head, use_last_error=False)(14, 'put_Issuer', ((1, 'pValue'),)))
    IX509CertificateRevocationList.get_ThisUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(15, 'get_ThisUpdate', ((1, 'pValue'),)))
    IX509CertificateRevocationList.put_ThisUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(16, 'put_ThisUpdate', ((1, 'Value'),)))
    IX509CertificateRevocationList.get_NextUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(17, 'get_NextUpdate', ((1, 'pValue'),)))
    IX509CertificateRevocationList.put_NextUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(18, 'put_NextUpdate', ((1, 'Value'),)))
    IX509CertificateRevocationList.get_X509CRLEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateRevocationListEntries_head), use_last_error=False)(19, 'get_X509CRLEntries', ((1, 'ppValue'),)))
    IX509CertificateRevocationList.get_X509Extensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509Extensions_head), use_last_error=False)(20, 'get_X509Extensions', ((1, 'ppValue'),)))
    IX509CertificateRevocationList.get_CriticalExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectIds_head), use_last_error=False)(21, 'get_CriticalExtensions', ((1, 'ppValue'),)))
    IX509CertificateRevocationList.get_SignerCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ISignerCertificate_head), use_last_error=False)(22, 'get_SignerCertificate', ((1, 'ppValue'),)))
    IX509CertificateRevocationList.put_SignerCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ISignerCertificate_head, use_last_error=False)(23, 'put_SignerCertificate', ((1, 'pValue'),)))
    IX509CertificateRevocationList.get_CRLNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_CRLNumber', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRevocationList.put_CRLNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_CRLNumber', ((1, 'Encoding'),(1, 'Value'),)))
    IX509CertificateRevocationList.get_CAVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(26, 'get_CAVersion', ((1, 'pValue'),)))
    IX509CertificateRevocationList.put_CAVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(27, 'put_CAVersion', ((1, 'pValue'),)))
    IX509CertificateRevocationList.get_BaseCRL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(28, 'get_BaseCRL', ((1, 'pValue'),)))
    IX509CertificateRevocationList.get_NullSigned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(29, 'get_NullSigned', ((1, 'pValue'),)))
    IX509CertificateRevocationList.get_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IObjectId_head), use_last_error=False)(30, 'get_HashAlgorithm', ((1, 'ppValue'),)))
    IX509CertificateRevocationList.put_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IObjectId_head, use_last_error=False)(31, 'put_HashAlgorithm', ((1, 'pValue'),)))
    IX509CertificateRevocationList.get_AlternateSignatureAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(32, 'get_AlternateSignatureAlgorithm', ((1, 'pValue'),)))
    IX509CertificateRevocationList.put_AlternateSignatureAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(33, 'put_AlternateSignatureAlgorithm', ((1, 'Value'),)))
    IX509CertificateRevocationList.get_SignatureInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509SignatureInformation_head), use_last_error=False)(34, 'get_SignatureInformation', ((1, 'ppValue'),)))
    IX509CertificateRevocationList.get_RawData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(35, 'get_RawData', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRevocationList.get_RawDataToBeSigned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'get_RawDataToBeSigned', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509CertificateRevocationList.get_Signature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(37, 'get_Signature', ((1, 'Encoding'),(1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX509CertificateRevocationList
def _define_ICertificateAttestationChallenge_head():
    class ICertificateAttestationChallenge(win32more.System.Com.IDispatch_head):
        Guid = Guid('6f175a7c-4a3a-40ae-9dba-592fd6bbf9b8')
    return ICertificateAttestationChallenge
def _define_ICertificateAttestationChallenge():
    ICertificateAttestationChallenge = win32more.Security.Cryptography.Certificates.ICertificateAttestationChallenge_head
    ICertificateAttestationChallenge.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(7, 'Initialize', ((1, 'Encoding'),(1, 'strPendingFullCmcResponseWithChallenge'),)))
    ICertificateAttestationChallenge.DecryptChallenge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'DecryptChallenge', ((1, 'Encoding'),(1, 'pstrEnvelopedPkcs7ReencryptedToCA'),)))
    ICertificateAttestationChallenge.get_RequestID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_RequestID', ((1, 'pstrRequestID'),)))
    win32more.System.Com.IDispatch
    return ICertificateAttestationChallenge
def _define_ICertificateAttestationChallenge2_head():
    class ICertificateAttestationChallenge2(win32more.Security.Cryptography.Certificates.ICertificateAttestationChallenge_head):
        Guid = Guid('4631334d-e266-47d6-bd79-be53cb2e2753')
    return ICertificateAttestationChallenge2
def _define_ICertificateAttestationChallenge2():
    ICertificateAttestationChallenge2 = win32more.Security.Cryptography.Certificates.ICertificateAttestationChallenge2_head
    ICertificateAttestationChallenge2.put_KeyContainerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_KeyContainerName', ((1, 'Value'),)))
    ICertificateAttestationChallenge2.put_KeyBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(11, 'put_KeyBlob', ((1, 'Encoding'),(1, 'Value'),)))
    win32more.Security.Cryptography.Certificates.ICertificateAttestationChallenge
    return ICertificateAttestationChallenge2
def _define_IX509SCEPEnrollment_head():
    class IX509SCEPEnrollment(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab361-217d-11da-b2a4-000e7bbb2b09')
    return IX509SCEPEnrollment
def _define_IX509SCEPEnrollment():
    IX509SCEPEnrollment = win32more.Security.Cryptography.Certificates.IX509SCEPEnrollment_head
    IX509SCEPEnrollment.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10_head,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(7, 'Initialize', ((1, 'pRequest'),(1, 'strThumbprint'),(1, 'ThumprintEncoding'),(1, 'strServerCertificates'),(1, 'Encoding'),)))
    IX509SCEPEnrollment.InitializeForPending = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext, use_last_error=False)(8, 'InitializeForPending', ((1, 'Context'),)))
    IX509SCEPEnrollment.CreateRequestMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'CreateRequestMessage', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509SCEPEnrollment.CreateRetrievePendingMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'CreateRetrievePendingMessage', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509SCEPEnrollment.CreateRetrieveCertificateMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'CreateRetrieveCertificateMessage', ((1, 'Context'),(1, 'strIssuer'),(1, 'IssuerEncoding'),(1, 'strSerialNumber'),(1, 'SerialNumberEncoding'),(1, 'Encoding'),(1, 'pValue'),)))
    IX509SCEPEnrollment.ProcessResponseMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Security.Cryptography.Certificates.X509SCEPDisposition), use_last_error=False)(12, 'ProcessResponseMessage', ((1, 'strResponse'),(1, 'Encoding'),(1, 'pDisposition'),)))
    IX509SCEPEnrollment.put_ServerCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(13, 'put_ServerCapabilities', ((1, 'Value'),)))
    IX509SCEPEnrollment.get_FailInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.X509SCEPFailInfo), use_last_error=False)(14, 'get_FailInfo', ((1, 'pValue'),)))
    IX509SCEPEnrollment.get_SignerCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ISignerCertificate_head), use_last_error=False)(15, 'get_SignerCertificate', ((1, 'ppValue'),)))
    IX509SCEPEnrollment.put_SignerCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ISignerCertificate_head, use_last_error=False)(16, 'put_SignerCertificate', ((1, 'pValue'),)))
    IX509SCEPEnrollment.get_OldCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ISignerCertificate_head), use_last_error=False)(17, 'get_OldCertificate', ((1, 'ppValue'),)))
    IX509SCEPEnrollment.put_OldCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ISignerCertificate_head, use_last_error=False)(18, 'put_OldCertificate', ((1, 'pValue'),)))
    IX509SCEPEnrollment.get_TransactionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_TransactionId', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509SCEPEnrollment.put_TransactionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Foundation.BSTR, use_last_error=False)(20, 'put_TransactionId', ((1, 'Encoding'),(1, 'Value'),)))
    IX509SCEPEnrollment.get_Request = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10_head), use_last_error=False)(21, 'get_Request', ((1, 'ppValue'),)))
    IX509SCEPEnrollment.get_CertificateFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_CertificateFriendlyName', ((1, 'pValue'),)))
    IX509SCEPEnrollment.put_CertificateFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_CertificateFriendlyName', ((1, 'Value'),)))
    IX509SCEPEnrollment.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509EnrollmentStatus_head), use_last_error=False)(24, 'get_Status', ((1, 'ppValue'),)))
    IX509SCEPEnrollment.get_Certificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_Certificate', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509SCEPEnrollment.get_Silent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(26, 'get_Silent', ((1, 'pValue'),)))
    IX509SCEPEnrollment.put_Silent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(27, 'put_Silent', ((1, 'Value'),)))
    IX509SCEPEnrollment.DeleteRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(28, 'DeleteRequest', ()))
    win32more.System.Com.IDispatch
    return IX509SCEPEnrollment
X509SCEPProcessMessageFlags = Int32
X509SCEPProcessMessageFlags_SCEPProcessDefault = 0
X509SCEPProcessMessageFlags_SCEPProcessSkipCertInstall = 1
DelayRetryAction = Int32
DelayRetryAction_DelayRetryUnknown = 0
DelayRetryAction_DelayRetryNone = 1
DelayRetryAction_DelayRetryShort = 2
DelayRetryAction_DelayRetryLong = 3
DelayRetryAction_DelayRetrySuccess = 4
DelayRetryAction_DelayRetryPastSuccess = 5
def _define_IX509SCEPEnrollment2_head():
    class IX509SCEPEnrollment2(win32more.Security.Cryptography.Certificates.IX509SCEPEnrollment_head):
        Guid = Guid('728ab364-217d-11da-b2a4-000e7bbb2b09')
    return IX509SCEPEnrollment2
def _define_IX509SCEPEnrollment2():
    IX509SCEPEnrollment2 = win32more.Security.Cryptography.Certificates.IX509SCEPEnrollment2_head
    IX509SCEPEnrollment2.CreateChallengeAnswerMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(29, 'CreateChallengeAnswerMessage', ((1, 'Encoding'),(1, 'pValue'),)))
    IX509SCEPEnrollment2.ProcessResponseMessage2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509SCEPProcessMessageFlags,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Security.Cryptography.Certificates.X509SCEPDisposition), use_last_error=False)(30, 'ProcessResponseMessage2', ((1, 'Flags'),(1, 'strResponse'),(1, 'Encoding'),(1, 'pDisposition'),)))
    IX509SCEPEnrollment2.get_ResultMessageText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(31, 'get_ResultMessageText', ((1, 'pValue'),)))
    IX509SCEPEnrollment2.get_DelayRetry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.DelayRetryAction), use_last_error=False)(32, 'get_DelayRetry', ((1, 'pValue'),)))
    IX509SCEPEnrollment2.get_ActivityId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(33, 'get_ActivityId', ((1, 'pValue'),)))
    IX509SCEPEnrollment2.put_ActivityId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(34, 'put_ActivityId', ((1, 'Value'),)))
    win32more.Security.Cryptography.Certificates.IX509SCEPEnrollment
    return IX509SCEPEnrollment2
def _define_IX509SCEPEnrollmentHelper_head():
    class IX509SCEPEnrollmentHelper(win32more.System.Com.IDispatch_head):
        Guid = Guid('728ab365-217d-11da-b2a4-000e7bbb2b09')
    return IX509SCEPEnrollmentHelper
def _define_IX509SCEPEnrollmentHelper():
    IX509SCEPEnrollmentHelper = win32more.Security.Cryptography.Certificates.IX509SCEPEnrollmentHelper_head
    IX509SCEPEnrollmentHelper.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.IX509CertificateRequestPkcs10_head,win32more.Foundation.BSTR, use_last_error=False)(7, 'Initialize', ((1, 'strServerUrl'),(1, 'strRequestHeaders'),(1, 'pRequest'),(1, 'strCACertificateThumbprint'),)))
    IX509SCEPEnrollmentHelper.InitializeForPending = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.X509CertificateEnrollmentContext,win32more.Foundation.BSTR, use_last_error=False)(8, 'InitializeForPending', ((1, 'strServerUrl'),(1, 'strRequestHeaders'),(1, 'Context'),(1, 'strTransactionId'),)))
    IX509SCEPEnrollmentHelper.Enroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509SCEPProcessMessageFlags,POINTER(win32more.Security.Cryptography.Certificates.X509SCEPDisposition), use_last_error=False)(9, 'Enroll', ((1, 'ProcessFlags'),(1, 'pDisposition'),)))
    IX509SCEPEnrollmentHelper.FetchPending = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.X509SCEPProcessMessageFlags,POINTER(win32more.Security.Cryptography.Certificates.X509SCEPDisposition), use_last_error=False)(10, 'FetchPending', ((1, 'ProcessFlags'),(1, 'pDisposition'),)))
    IX509SCEPEnrollmentHelper.get_X509SCEPEnrollment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.IX509SCEPEnrollment_head), use_last_error=False)(11, 'get_X509SCEPEnrollment', ((1, 'ppValue'),)))
    IX509SCEPEnrollmentHelper.get_ResultMessageText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_ResultMessageText', ((1, 'pValue'),)))
    win32more.System.Com.IDispatch
    return IX509SCEPEnrollmentHelper
X509CertificateTemplateGeneralFlag = Int32
X509CertificateTemplateGeneralFlag_GeneralMachineType = 64
X509CertificateTemplateGeneralFlag_GeneralCA = 128
X509CertificateTemplateGeneralFlag_GeneralCrossCA = 2048
X509CertificateTemplateGeneralFlag_GeneralDefault = 65536
X509CertificateTemplateGeneralFlag_GeneralModified = 131072
X509CertificateTemplateGeneralFlag_GeneralDonotPersist = 4096
X509CertificateTemplateEnrollmentFlag = Int32
X509CertificateTemplateEnrollmentFlag_EnrollmentIncludeSymmetricAlgorithms = 1
X509CertificateTemplateEnrollmentFlag_EnrollmentPendAllRequests = 2
X509CertificateTemplateEnrollmentFlag_EnrollmentPublishToKRAContainer = 4
X509CertificateTemplateEnrollmentFlag_EnrollmentPublishToDS = 8
X509CertificateTemplateEnrollmentFlag_EnrollmentAutoEnrollmentCheckUserDSCertificate = 16
X509CertificateTemplateEnrollmentFlag_EnrollmentAutoEnrollment = 32
X509CertificateTemplateEnrollmentFlag_EnrollmentDomainAuthenticationNotRequired = 128
X509CertificateTemplateEnrollmentFlag_EnrollmentPreviousApprovalValidateReenrollment = 64
X509CertificateTemplateEnrollmentFlag_EnrollmentUserInteractionRequired = 256
X509CertificateTemplateEnrollmentFlag_EnrollmentAddTemplateName = 512
X509CertificateTemplateEnrollmentFlag_EnrollmentRemoveInvalidCertificateFromPersonalStore = 1024
X509CertificateTemplateEnrollmentFlag_EnrollmentAllowEnrollOnBehalfOf = 2048
X509CertificateTemplateEnrollmentFlag_EnrollmentAddOCSPNoCheck = 4096
X509CertificateTemplateEnrollmentFlag_EnrollmentReuseKeyOnFullSmartCard = 8192
X509CertificateTemplateEnrollmentFlag_EnrollmentNoRevocationInfoInCerts = 16384
X509CertificateTemplateEnrollmentFlag_EnrollmentIncludeBasicConstraintsForEECerts = 32768
X509CertificateTemplateEnrollmentFlag_EnrollmentPreviousApprovalKeyBasedValidateReenrollment = 65536
X509CertificateTemplateEnrollmentFlag_EnrollmentCertificateIssuancePoliciesFromRequest = 131072
X509CertificateTemplateEnrollmentFlag_EnrollmentSkipAutoRenewal = 262144
X509CertificateTemplateSubjectNameFlag = Int32
X509CertificateTemplateSubjectNameFlag_SubjectNameEnrolleeSupplies = 1
X509CertificateTemplateSubjectNameFlag_SubjectNameRequireDirectoryPath = -2147483648
X509CertificateTemplateSubjectNameFlag_SubjectNameRequireCommonName = 1073741824
X509CertificateTemplateSubjectNameFlag_SubjectNameRequireEmail = 536870912
X509CertificateTemplateSubjectNameFlag_SubjectNameRequireDNS = 268435456
X509CertificateTemplateSubjectNameFlag_SubjectNameAndAlternativeNameOldCertSupplies = 8
X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameEnrolleeSupplies = 65536
X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireDirectoryGUID = 16777216
X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireUPN = 33554432
X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireEmail = 67108864
X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireSPN = 8388608
X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireDNS = 134217728
X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireDomainDNS = 4194304
X509CertificateTemplatePrivateKeyFlag = Int32
X509CertificateTemplatePrivateKeyFlag_PrivateKeyRequireArchival = 1
X509CertificateTemplatePrivateKeyFlag_PrivateKeyExportable = 16
X509CertificateTemplatePrivateKeyFlag_PrivateKeyRequireStrongKeyProtection = 32
X509CertificateTemplatePrivateKeyFlag_PrivateKeyRequireAlternateSignatureAlgorithm = 64
X509CertificateTemplatePrivateKeyFlag_PrivateKeyRequireSameKeyRenewal = 128
X509CertificateTemplatePrivateKeyFlag_PrivateKeyUseLegacyProvider = 256
X509CertificateTemplatePrivateKeyFlag_PrivateKeyEKTrustOnUse = 512
X509CertificateTemplatePrivateKeyFlag_PrivateKeyEKValidateCert = 1024
X509CertificateTemplatePrivateKeyFlag_PrivateKeyEKValidateKey = 2048
X509CertificateTemplatePrivateKeyFlag_PrivateKeyAttestNone = 0
X509CertificateTemplatePrivateKeyFlag_PrivateKeyAttestPreferred = 4096
X509CertificateTemplatePrivateKeyFlag_PrivateKeyAttestRequired = 8192
X509CertificateTemplatePrivateKeyFlag_PrivateKeyAttestMask = 12288
X509CertificateTemplatePrivateKeyFlag_PrivateKeyAttestWithoutPolicy = 16384
X509CertificateTemplatePrivateKeyFlag_PrivateKeyServerVersionMask = 983040
X509CertificateTemplatePrivateKeyFlag_PrivateKeyServerVersionShift = 16
X509CertificateTemplatePrivateKeyFlag_PrivateKeyHelloKspKey = 1048576
X509CertificateTemplatePrivateKeyFlag_PrivateKeyHelloLogonKey = 2097152
X509CertificateTemplatePrivateKeyFlag_PrivateKeyClientVersionMask = 251658240
X509CertificateTemplatePrivateKeyFlag_PrivateKeyClientVersionShift = 24
ImportPFXFlags = Int32
ImportPFXFlags_ImportNone = 0
ImportPFXFlags_ImportMachineContext = 1
ImportPFXFlags_ImportForceOverwrite = 2
ImportPFXFlags_ImportSilent = 4
ImportPFXFlags_ImportSaveProperties = 8
ImportPFXFlags_ImportExportable = 16
ImportPFXFlags_ImportExportableEncrypted = 32
ImportPFXFlags_ImportNoUserProtected = 64
ImportPFXFlags_ImportUserProtected = 128
ImportPFXFlags_ImportUserProtectedHigh = 256
ImportPFXFlags_ImportInstallCertificate = 512
ImportPFXFlags_ImportInstallChain = 1024
ImportPFXFlags_ImportInstallChainAndRoot = 2048
def _define_FNIMPORTPFXTOPROVIDER():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,c_char_p_no,UInt32,win32more.Security.Cryptography.Certificates.ImportPFXFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head))), use_last_error=False)
def _define_FNIMPORTPFXTOPROVIDERFREEDATA():
    return CFUNCTYPE(Void,UInt32,POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)), use_last_error=False)
def _define_ICertEncodeStringArray_head():
    class ICertEncodeStringArray(win32more.System.Com.IDispatch_head):
        Guid = Guid('12a88820-7494-11d0-8816-00a0c903b83c')
    return ICertEncodeStringArray
def _define_ICertEncodeStringArray():
    ICertEncodeStringArray = win32more.Security.Cryptography.Certificates.ICertEncodeStringArray_head
    ICertEncodeStringArray.Decode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'Decode', ((1, 'strBinary'),)))
    ICertEncodeStringArray.GetStringType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'GetStringType', ((1, 'pStringType'),)))
    ICertEncodeStringArray.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'GetCount', ((1, 'pCount'),)))
    ICertEncodeStringArray.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetValue', ((1, 'Index'),(1, 'pstr'),)))
    ICertEncodeStringArray.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Security.Cryptography.CERT_RDN_ATTR_VALUE_TYPE, use_last_error=False)(11, 'Reset', ((1, 'Count'),(1, 'StringType'),)))
    ICertEncodeStringArray.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR, use_last_error=False)(12, 'SetValue', ((1, 'Index'),(1, 'str'),)))
    ICertEncodeStringArray.Encode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'Encode', ((1, 'pstrBinary'),)))
    win32more.System.Com.IDispatch
    return ICertEncodeStringArray
def _define_ICertEncodeStringArray2_head():
    class ICertEncodeStringArray2(win32more.Security.Cryptography.Certificates.ICertEncodeStringArray_head):
        Guid = Guid('9c680d93-9b7d-4e95-9018-4ffe10ba5ada')
    return ICertEncodeStringArray2
def _define_ICertEncodeStringArray2():
    ICertEncodeStringArray2 = win32more.Security.Cryptography.Certificates.ICertEncodeStringArray2_head
    ICertEncodeStringArray2.DecodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(14, 'DecodeBlob', ((1, 'strEncodedData'),(1, 'Encoding'),)))
    ICertEncodeStringArray2.EncodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'EncodeBlob', ((1, 'Encoding'),(1, 'pstrEncodedData'),)))
    win32more.Security.Cryptography.Certificates.ICertEncodeStringArray
    return ICertEncodeStringArray2
def _define_ICertEncodeLongArray_head():
    class ICertEncodeLongArray(win32more.System.Com.IDispatch_head):
        Guid = Guid('15e2f230-a0a2-11d0-8821-00a0c903b83c')
    return ICertEncodeLongArray
def _define_ICertEncodeLongArray():
    ICertEncodeLongArray = win32more.Security.Cryptography.Certificates.ICertEncodeLongArray_head
    ICertEncodeLongArray.Decode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'Decode', ((1, 'strBinary'),)))
    ICertEncodeLongArray.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'GetCount', ((1, 'pCount'),)))
    ICertEncodeLongArray.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(9, 'GetValue', ((1, 'Index'),(1, 'pValue'),)))
    ICertEncodeLongArray.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'Reset', ((1, 'Count'),)))
    ICertEncodeLongArray.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(11, 'SetValue', ((1, 'Index'),(1, 'Value'),)))
    ICertEncodeLongArray.Encode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'Encode', ((1, 'pstrBinary'),)))
    win32more.System.Com.IDispatch
    return ICertEncodeLongArray
def _define_ICertEncodeLongArray2_head():
    class ICertEncodeLongArray2(win32more.Security.Cryptography.Certificates.ICertEncodeLongArray_head):
        Guid = Guid('4efde84a-bd9b-4fc2-a108-c347d478840f')
    return ICertEncodeLongArray2
def _define_ICertEncodeLongArray2():
    ICertEncodeLongArray2 = win32more.Security.Cryptography.Certificates.ICertEncodeLongArray2_head
    ICertEncodeLongArray2.DecodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(13, 'DecodeBlob', ((1, 'strEncodedData'),(1, 'Encoding'),)))
    ICertEncodeLongArray2.EncodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'EncodeBlob', ((1, 'Encoding'),(1, 'pstrEncodedData'),)))
    win32more.Security.Cryptography.Certificates.ICertEncodeLongArray
    return ICertEncodeLongArray2
def _define_ICertEncodeDateArray_head():
    class ICertEncodeDateArray(win32more.System.Com.IDispatch_head):
        Guid = Guid('2f9469a0-a470-11d0-8821-00a0c903b83c')
    return ICertEncodeDateArray
def _define_ICertEncodeDateArray():
    ICertEncodeDateArray = win32more.Security.Cryptography.Certificates.ICertEncodeDateArray_head
    ICertEncodeDateArray.Decode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'Decode', ((1, 'strBinary'),)))
    ICertEncodeDateArray.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'GetCount', ((1, 'pCount'),)))
    ICertEncodeDateArray.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Double), use_last_error=False)(9, 'GetValue', ((1, 'Index'),(1, 'pValue'),)))
    ICertEncodeDateArray.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'Reset', ((1, 'Count'),)))
    ICertEncodeDateArray.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Double, use_last_error=False)(11, 'SetValue', ((1, 'Index'),(1, 'Value'),)))
    ICertEncodeDateArray.Encode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'Encode', ((1, 'pstrBinary'),)))
    win32more.System.Com.IDispatch
    return ICertEncodeDateArray
def _define_ICertEncodeDateArray2_head():
    class ICertEncodeDateArray2(win32more.Security.Cryptography.Certificates.ICertEncodeDateArray_head):
        Guid = Guid('99a4edb5-2b8e-448d-bf95-bba8d7789dc8')
    return ICertEncodeDateArray2
def _define_ICertEncodeDateArray2():
    ICertEncodeDateArray2 = win32more.Security.Cryptography.Certificates.ICertEncodeDateArray2_head
    ICertEncodeDateArray2.DecodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(13, 'DecodeBlob', ((1, 'strEncodedData'),(1, 'Encoding'),)))
    ICertEncodeDateArray2.EncodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'EncodeBlob', ((1, 'Encoding'),(1, 'pstrEncodedData'),)))
    win32more.Security.Cryptography.Certificates.ICertEncodeDateArray
    return ICertEncodeDateArray2
def _define_ICertEncodeCRLDistInfo_head():
    class ICertEncodeCRLDistInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('01958640-bbff-11d0-8825-00a0c903b83c')
    return ICertEncodeCRLDistInfo
def _define_ICertEncodeCRLDistInfo():
    ICertEncodeCRLDistInfo = win32more.Security.Cryptography.Certificates.ICertEncodeCRLDistInfo_head
    ICertEncodeCRLDistInfo.Decode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'Decode', ((1, 'strBinary'),)))
    ICertEncodeCRLDistInfo.GetDistPointCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'GetDistPointCount', ((1, 'pDistPointCount'),)))
    ICertEncodeCRLDistInfo.GetNameCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(9, 'GetNameCount', ((1, 'DistPointIndex'),(1, 'pNameCount'),)))
    ICertEncodeCRLDistInfo.GetNameChoice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Int32), use_last_error=False)(10, 'GetNameChoice', ((1, 'DistPointIndex'),(1, 'NameIndex'),(1, 'pNameChoice'),)))
    ICertEncodeCRLDistInfo.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetName', ((1, 'DistPointIndex'),(1, 'NameIndex'),(1, 'pstrName'),)))
    ICertEncodeCRLDistInfo.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'Reset', ((1, 'DistPointCount'),)))
    ICertEncodeCRLDistInfo.SetNameCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(13, 'SetNameCount', ((1, 'DistPointIndex'),(1, 'NameCount'),)))
    ICertEncodeCRLDistInfo.SetNameEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Security.Cryptography.Certificates.CERT_ALT_NAME,win32more.Foundation.BSTR, use_last_error=False)(14, 'SetNameEntry', ((1, 'DistPointIndex'),(1, 'NameIndex'),(1, 'NameChoice'),(1, 'strName'),)))
    ICertEncodeCRLDistInfo.Encode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'Encode', ((1, 'pstrBinary'),)))
    win32more.System.Com.IDispatch
    return ICertEncodeCRLDistInfo
def _define_ICertEncodeCRLDistInfo2_head():
    class ICertEncodeCRLDistInfo2(win32more.Security.Cryptography.Certificates.ICertEncodeCRLDistInfo_head):
        Guid = Guid('b4275d4b-3e30-446f-ad36-09d03120b078')
    return ICertEncodeCRLDistInfo2
def _define_ICertEncodeCRLDistInfo2():
    ICertEncodeCRLDistInfo2 = win32more.Security.Cryptography.Certificates.ICertEncodeCRLDistInfo2_head
    ICertEncodeCRLDistInfo2.DecodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(16, 'DecodeBlob', ((1, 'strEncodedData'),(1, 'Encoding'),)))
    ICertEncodeCRLDistInfo2.EncodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'EncodeBlob', ((1, 'Encoding'),(1, 'pstrEncodedData'),)))
    win32more.Security.Cryptography.Certificates.ICertEncodeCRLDistInfo
    return ICertEncodeCRLDistInfo2
def _define_ICertEncodeAltName_head():
    class ICertEncodeAltName(win32more.System.Com.IDispatch_head):
        Guid = Guid('1c9a8c70-1271-11d1-9bd4-00c04fb683fa')
    return ICertEncodeAltName
def _define_ICertEncodeAltName():
    ICertEncodeAltName = win32more.Security.Cryptography.Certificates.ICertEncodeAltName_head
    ICertEncodeAltName.Decode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'Decode', ((1, 'strBinary'),)))
    ICertEncodeAltName.GetNameCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'GetNameCount', ((1, 'pNameCount'),)))
    ICertEncodeAltName.GetNameChoice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(9, 'GetNameChoice', ((1, 'NameIndex'),(1, 'pNameChoice'),)))
    ICertEncodeAltName.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetName', ((1, 'NameIndex'),(1, 'pstrName'),)))
    ICertEncodeAltName.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Reset', ((1, 'NameCount'),)))
    ICertEncodeAltName.SetNameEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Security.Cryptography.Certificates.CERT_ALT_NAME,win32more.Foundation.BSTR, use_last_error=False)(12, 'SetNameEntry', ((1, 'NameIndex'),(1, 'NameChoice'),(1, 'strName'),)))
    ICertEncodeAltName.Encode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'Encode', ((1, 'pstrBinary'),)))
    win32more.System.Com.IDispatch
    return ICertEncodeAltName
def _define_ICertEncodeAltName2_head():
    class ICertEncodeAltName2(win32more.Security.Cryptography.Certificates.ICertEncodeAltName_head):
        Guid = Guid('f67fe177-5ef1-4535-b4ce-29df15e2e0c3')
    return ICertEncodeAltName2
def _define_ICertEncodeAltName2():
    ICertEncodeAltName2 = win32more.Security.Cryptography.Certificates.ICertEncodeAltName2_head
    ICertEncodeAltName2.DecodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(14, 'DecodeBlob', ((1, 'strEncodedData'),(1, 'Encoding'),)))
    ICertEncodeAltName2.EncodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'EncodeBlob', ((1, 'Encoding'),(1, 'pstrEncodedData'),)))
    ICertEncodeAltName2.GetNameBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'GetNameBlob', ((1, 'NameIndex'),(1, 'Encoding'),(1, 'pstrName'),)))
    ICertEncodeAltName2.SetNameEntryBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(17, 'SetNameEntryBlob', ((1, 'NameIndex'),(1, 'NameChoice'),(1, 'strName'),(1, 'Encoding'),)))
    win32more.Security.Cryptography.Certificates.ICertEncodeAltName
    return ICertEncodeAltName2
def _define_ICertEncodeBitString_head():
    class ICertEncodeBitString(win32more.System.Com.IDispatch_head):
        Guid = Guid('6db525be-1278-11d1-9bd4-00c04fb683fa')
    return ICertEncodeBitString
def _define_ICertEncodeBitString():
    ICertEncodeBitString = win32more.Security.Cryptography.Certificates.ICertEncodeBitString_head
    ICertEncodeBitString.Decode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'Decode', ((1, 'strBinary'),)))
    ICertEncodeBitString.GetBitCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'GetBitCount', ((1, 'pBitCount'),)))
    ICertEncodeBitString.GetBitString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetBitString', ((1, 'pstrBitString'),)))
    ICertEncodeBitString.Encode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'Encode', ((1, 'BitCount'),(1, 'strBitString'),(1, 'pstrBinary'),)))
    win32more.System.Com.IDispatch
    return ICertEncodeBitString
def _define_ICertEncodeBitString2_head():
    class ICertEncodeBitString2(win32more.Security.Cryptography.Certificates.ICertEncodeBitString_head):
        Guid = Guid('e070d6e7-23ef-4dd2-8242-ebd9c928cb30')
    return ICertEncodeBitString2
def _define_ICertEncodeBitString2():
    ICertEncodeBitString2 = win32more.Security.Cryptography.Certificates.ICertEncodeBitString2_head
    ICertEncodeBitString2.DecodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType, use_last_error=False)(11, 'DecodeBlob', ((1, 'strEncodedData'),(1, 'Encoding'),)))
    ICertEncodeBitString2.EncodeBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Security.Cryptography.Certificates.EncodingType,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'EncodeBlob', ((1, 'BitCount'),(1, 'strBitString'),(1, 'EncodingIn'),(1, 'Encoding'),(1, 'pstrEncodedData'),)))
    ICertEncodeBitString2.GetBitStringBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.EncodingType,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'GetBitStringBlob', ((1, 'Encoding'),(1, 'pstrBitString'),)))
    win32more.Security.Cryptography.Certificates.ICertEncodeBitString
    return ICertEncodeBitString2
def _define_ICertExit_head():
    class ICertExit(win32more.System.Com.IDispatch_head):
        Guid = Guid('e19ae1a0-7364-11d0-8816-00a0c903b83c')
    return ICertExit
def _define_ICertExit():
    ICertExit = win32more.Security.Cryptography.Certificates.ICertExit_head
    ICertExit.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Cryptography.Certificates.CERT_EXIT_EVENT_MASK), use_last_error=False)(7, 'Initialize', ((1, 'strConfig'),(1, 'pEventMask'),)))
    ICertExit.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(8, 'Notify', ((1, 'ExitEvent'),(1, 'Context'),)))
    ICertExit.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetDescription', ((1, 'pstrDescription'),)))
    win32more.System.Com.IDispatch
    return ICertExit
def _define_ICertExit2_head():
    class ICertExit2(win32more.Security.Cryptography.Certificates.ICertExit_head):
        Guid = Guid('0abf484b-d049-464d-a7ed-552e7529b0ff')
    return ICertExit2
def _define_ICertExit2():
    ICertExit2 = win32more.Security.Cryptography.Certificates.ICertExit2_head
    ICertExit2.GetManageModule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.Certificates.ICertManageModule_head), use_last_error=False)(10, 'GetManageModule', ((1, 'ppManageModule'),)))
    win32more.Security.Cryptography.Certificates.ICertExit
    return ICertExit2
ENUM_CATYPES = Int32
ENUM_ENTERPRISE_ROOTCA = 0
ENUM_ENTERPRISE_SUBCA = 1
ENUM_STANDALONE_ROOTCA = 3
ENUM_STANDALONE_SUBCA = 4
ENUM_UNKNOWN_CA = 5
def _define_CAINFO_head():
    class CAINFO(Structure):
        pass
    return CAINFO
def _define_CAINFO():
    CAINFO = win32more.Security.Cryptography.Certificates.CAINFO_head
    CAINFO._fields_ = [
        ("cbSize", UInt32),
        ("CAType", win32more.Security.Cryptography.Certificates.ENUM_CATYPES),
        ("cCASignatureCerts", UInt32),
        ("cCAExchangeCerts", UInt32),
        ("cExitModules", UInt32),
        ("lPropIdMax", Int32),
        ("lRoleSeparationEnabled", Int32),
        ("cKRACertUsedCount", UInt32),
        ("cKRACertCount", UInt32),
        ("fAdvancedServer", UInt32),
    ]
    return CAINFO
CEnroll2 = Guid('127698e4-e730-4e5c-a2b1-21490a70c8a1')
CEnroll = Guid('43f8f289-7a20-11d0-8f06-00c04fc295e1')
def _define_ICEnroll_head():
    class ICEnroll(win32more.System.Com.IDispatch_head):
        Guid = Guid('43f8f288-7a20-11d0-8f06-00c04fc295e1')
    return ICEnroll
def _define_ICEnroll():
    ICEnroll = win32more.Security.Cryptography.Certificates.ICEnroll_head
    ICEnroll.createFilePKCS10 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(7, 'createFilePKCS10', ((1, 'DNName'),(1, 'Usage'),(1, 'wszPKCS10FileName'),)))
    ICEnroll.acceptFilePKCS7 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'acceptFilePKCS7', ((1, 'wszPKCS7FileName'),)))
    ICEnroll.createPKCS10 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'createPKCS10', ((1, 'DNName'),(1, 'Usage'),(1, 'pPKCS10'),)))
    ICEnroll.acceptPKCS7 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'acceptPKCS7', ((1, 'PKCS7'),)))
    ICEnroll.getCertFromPKCS7 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'getCertFromPKCS7', ((1, 'wszPKCS7'),(1, 'pbstrCert'),)))
    ICEnroll.enumProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'enumProviders', ((1, 'dwIndex'),(1, 'dwFlags'),(1, 'pbstrProvName'),)))
    ICEnroll.enumContainers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'enumContainers', ((1, 'dwIndex'),(1, 'pbstr'),)))
    ICEnroll.freeRequestInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'freeRequestInfo', ((1, 'PKCS7OrPKCS10'),)))
    ICEnroll.get_MyStoreName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_MyStoreName', ((1, 'pbstrName'),)))
    ICEnroll.put_MyStoreName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_MyStoreName', ((1, 'bstrName'),)))
    ICEnroll.get_MyStoreType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_MyStoreType', ((1, 'pbstrType'),)))
    ICEnroll.put_MyStoreType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_MyStoreType', ((1, 'bstrType'),)))
    ICEnroll.get_MyStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_MyStoreFlags', ((1, 'pdwFlags'),)))
    ICEnroll.put_MyStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'put_MyStoreFlags', ((1, 'dwFlags'),)))
    ICEnroll.get_CAStoreName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_CAStoreName', ((1, 'pbstrName'),)))
    ICEnroll.put_CAStoreName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(22, 'put_CAStoreName', ((1, 'bstrName'),)))
    ICEnroll.get_CAStoreType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_CAStoreType', ((1, 'pbstrType'),)))
    ICEnroll.put_CAStoreType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(24, 'put_CAStoreType', ((1, 'bstrType'),)))
    ICEnroll.get_CAStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'get_CAStoreFlags', ((1, 'pdwFlags'),)))
    ICEnroll.put_CAStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(26, 'put_CAStoreFlags', ((1, 'dwFlags'),)))
    ICEnroll.get_RootStoreName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(27, 'get_RootStoreName', ((1, 'pbstrName'),)))
    ICEnroll.put_RootStoreName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(28, 'put_RootStoreName', ((1, 'bstrName'),)))
    ICEnroll.get_RootStoreType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(29, 'get_RootStoreType', ((1, 'pbstrType'),)))
    ICEnroll.put_RootStoreType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(30, 'put_RootStoreType', ((1, 'bstrType'),)))
    ICEnroll.get_RootStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(31, 'get_RootStoreFlags', ((1, 'pdwFlags'),)))
    ICEnroll.put_RootStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(32, 'put_RootStoreFlags', ((1, 'dwFlags'),)))
    ICEnroll.get_RequestStoreName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(33, 'get_RequestStoreName', ((1, 'pbstrName'),)))
    ICEnroll.put_RequestStoreName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(34, 'put_RequestStoreName', ((1, 'bstrName'),)))
    ICEnroll.get_RequestStoreType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(35, 'get_RequestStoreType', ((1, 'pbstrType'),)))
    ICEnroll.put_RequestStoreType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(36, 'put_RequestStoreType', ((1, 'bstrType'),)))
    ICEnroll.get_RequestStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(37, 'get_RequestStoreFlags', ((1, 'pdwFlags'),)))
    ICEnroll.put_RequestStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(38, 'put_RequestStoreFlags', ((1, 'dwFlags'),)))
    ICEnroll.get_ContainerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(39, 'get_ContainerName', ((1, 'pbstrContainer'),)))
    ICEnroll.put_ContainerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(40, 'put_ContainerName', ((1, 'bstrContainer'),)))
    ICEnroll.get_ProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(41, 'get_ProviderName', ((1, 'pbstrProvider'),)))
    ICEnroll.put_ProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(42, 'put_ProviderName', ((1, 'bstrProvider'),)))
    ICEnroll.get_ProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(43, 'get_ProviderType', ((1, 'pdwType'),)))
    ICEnroll.put_ProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(44, 'put_ProviderType', ((1, 'dwType'),)))
    ICEnroll.get_KeySpec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(45, 'get_KeySpec', ((1, 'pdw'),)))
    ICEnroll.put_KeySpec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(46, 'put_KeySpec', ((1, 'dw'),)))
    ICEnroll.get_ProviderFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(47, 'get_ProviderFlags', ((1, 'pdwFlags'),)))
    ICEnroll.put_ProviderFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(48, 'put_ProviderFlags', ((1, 'dwFlags'),)))
    ICEnroll.get_UseExistingKeySet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(49, 'get_UseExistingKeySet', ((1, 'fUseExistingKeys'),)))
    ICEnroll.put_UseExistingKeySet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(50, 'put_UseExistingKeySet', ((1, 'fUseExistingKeys'),)))
    ICEnroll.get_GenKeyFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(51, 'get_GenKeyFlags', ((1, 'pdwFlags'),)))
    ICEnroll.put_GenKeyFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(52, 'put_GenKeyFlags', ((1, 'dwFlags'),)))
    ICEnroll.get_DeleteRequestCert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(53, 'get_DeleteRequestCert', ((1, 'fDelete'),)))
    ICEnroll.put_DeleteRequestCert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(54, 'put_DeleteRequestCert', ((1, 'fDelete'),)))
    ICEnroll.get_WriteCertToCSP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(55, 'get_WriteCertToCSP', ((1, 'fBool'),)))
    ICEnroll.put_WriteCertToCSP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(56, 'put_WriteCertToCSP', ((1, 'fBool'),)))
    ICEnroll.get_SPCFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(57, 'get_SPCFileName', ((1, 'pbstr'),)))
    ICEnroll.put_SPCFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(58, 'put_SPCFileName', ((1, 'bstr'),)))
    ICEnroll.get_PVKFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(59, 'get_PVKFileName', ((1, 'pbstr'),)))
    ICEnroll.put_PVKFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(60, 'put_PVKFileName', ((1, 'bstr'),)))
    ICEnroll.get_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(61, 'get_HashAlgorithm', ((1, 'pbstr'),)))
    ICEnroll.put_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(62, 'put_HashAlgorithm', ((1, 'bstr'),)))
    win32more.System.Com.IDispatch
    return ICEnroll
def _define_ICEnroll2_head():
    class ICEnroll2(win32more.Security.Cryptography.Certificates.ICEnroll_head):
        Guid = Guid('704ca730-c90b-11d1-9bec-00c04fc295e1')
    return ICEnroll2
def _define_ICEnroll2():
    ICEnroll2 = win32more.Security.Cryptography.Certificates.ICEnroll2_head
    ICEnroll2.addCertTypeToRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(63, 'addCertTypeToRequest', ((1, 'CertType'),)))
    ICEnroll2.addNameValuePairToSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(64, 'addNameValuePairToSignature', ((1, 'Name'),(1, 'Value'),)))
    ICEnroll2.get_WriteCertToUserDS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(65, 'get_WriteCertToUserDS', ((1, 'fBool'),)))
    ICEnroll2.put_WriteCertToUserDS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(66, 'put_WriteCertToUserDS', ((1, 'fBool'),)))
    ICEnroll2.get_EnableT61DNEncoding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(67, 'get_EnableT61DNEncoding', ((1, 'fBool'),)))
    ICEnroll2.put_EnableT61DNEncoding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(68, 'put_EnableT61DNEncoding', ((1, 'fBool'),)))
    win32more.Security.Cryptography.Certificates.ICEnroll
    return ICEnroll2
def _define_ICEnroll3_head():
    class ICEnroll3(win32more.Security.Cryptography.Certificates.ICEnroll2_head):
        Guid = Guid('c28c2d95-b7de-11d2-a421-00c04f79fe8e')
    return ICEnroll3
def _define_ICEnroll3():
    ICEnroll3 = win32more.Security.Cryptography.Certificates.ICEnroll3_head
    ICEnroll3.InstallPKCS7 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(69, 'InstallPKCS7', ((1, 'PKCS7'),)))
    ICEnroll3.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(70, 'Reset', ()))
    ICEnroll3.GetSupportedKeySpec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(71, 'GetSupportedKeySpec', ((1, 'pdwKeySpec'),)))
    ICEnroll3.GetKeyLen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(Int32), use_last_error=False)(72, 'GetKeyLen', ((1, 'fMin'),(1, 'fExchange'),(1, 'pdwKeySize'),)))
    ICEnroll3.EnumAlgs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Int32), use_last_error=False)(73, 'EnumAlgs', ((1, 'dwIndex'),(1, 'algClass'),(1, 'pdwAlgID'),)))
    ICEnroll3.GetAlgName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(74, 'GetAlgName', ((1, 'algID'),(1, 'pbstr'),)))
    ICEnroll3.put_ReuseHardwareKeyIfUnableToGenNew = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(75, 'put_ReuseHardwareKeyIfUnableToGenNew', ((1, 'fReuseHardwareKeyIfUnableToGenNew'),)))
    ICEnroll3.get_ReuseHardwareKeyIfUnableToGenNew = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(76, 'get_ReuseHardwareKeyIfUnableToGenNew', ((1, 'fReuseHardwareKeyIfUnableToGenNew'),)))
    ICEnroll3.put_HashAlgID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(77, 'put_HashAlgID', ((1, 'hashAlgID'),)))
    ICEnroll3.get_HashAlgID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(78, 'get_HashAlgID', ((1, 'hashAlgID'),)))
    ICEnroll3.put_LimitExchangeKeyToEncipherment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(79, 'put_LimitExchangeKeyToEncipherment', ((1, 'fLimitExchangeKeyToEncipherment'),)))
    ICEnroll3.get_LimitExchangeKeyToEncipherment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(80, 'get_LimitExchangeKeyToEncipherment', ((1, 'fLimitExchangeKeyToEncipherment'),)))
    ICEnroll3.put_EnableSMIMECapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(81, 'put_EnableSMIMECapabilities', ((1, 'fEnableSMIMECapabilities'),)))
    ICEnroll3.get_EnableSMIMECapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(82, 'get_EnableSMIMECapabilities', ((1, 'fEnableSMIMECapabilities'),)))
    win32more.Security.Cryptography.Certificates.ICEnroll2
    return ICEnroll3
def _define_ICEnroll4_head():
    class ICEnroll4(win32more.Security.Cryptography.Certificates.ICEnroll3_head):
        Guid = Guid('c1f1188a-2eb5-4a80-841b-7e729a356d90')
    return ICEnroll4
def _define_ICEnroll4():
    ICEnroll4 = win32more.Security.Cryptography.Certificates.ICEnroll4_head
    ICEnroll4.put_PrivateKeyArchiveCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(83, 'put_PrivateKeyArchiveCertificate', ((1, 'bstrCert'),)))
    ICEnroll4.get_PrivateKeyArchiveCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(84, 'get_PrivateKeyArchiveCertificate', ((1, 'pbstrCert'),)))
    ICEnroll4.put_ThumbPrint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(85, 'put_ThumbPrint', ((1, 'bstrThumbPrint'),)))
    ICEnroll4.get_ThumbPrint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(86, 'get_ThumbPrint', ((1, 'pbstrThumbPrint'),)))
    ICEnroll4.binaryToString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(87, 'binaryToString', ((1, 'Flags'),(1, 'strBinary'),(1, 'pstrEncoded'),)))
    ICEnroll4.stringToBinary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(88, 'stringToBinary', ((1, 'Flags'),(1, 'strEncoded'),(1, 'pstrBinary'),)))
    ICEnroll4.addExtensionToRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(89, 'addExtensionToRequest', ((1, 'Flags'),(1, 'strName'),(1, 'strValue'),)))
    ICEnroll4.addAttributeToRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(90, 'addAttributeToRequest', ((1, 'Flags'),(1, 'strName'),(1, 'strValue'),)))
    ICEnroll4.addNameValuePairToRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(91, 'addNameValuePairToRequest', ((1, 'Flags'),(1, 'strName'),(1, 'strValue'),)))
    ICEnroll4.resetExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(92, 'resetExtensions', ()))
    ICEnroll4.resetAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(93, 'resetAttributes', ()))
    ICEnroll4.createRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CERT_CREATE_REQUEST_FLAGS,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(94, 'createRequest', ((1, 'Flags'),(1, 'strDNName'),(1, 'Usage'),(1, 'pstrRequest'),)))
    ICEnroll4.createFileRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CERT_CREATE_REQUEST_FLAGS,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(95, 'createFileRequest', ((1, 'Flags'),(1, 'strDNName'),(1, 'strUsage'),(1, 'strRequestFileName'),)))
    ICEnroll4.acceptResponse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(96, 'acceptResponse', ((1, 'strResponse'),)))
    ICEnroll4.acceptFileResponse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(97, 'acceptFileResponse', ((1, 'strResponseFileName'),)))
    ICEnroll4.getCertFromResponse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(98, 'getCertFromResponse', ((1, 'strResponse'),(1, 'pstrCert'),)))
    ICEnroll4.getCertFromFileResponse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(99, 'getCertFromFileResponse', ((1, 'strResponseFileName'),(1, 'pstrCert'),)))
    ICEnroll4.createPFX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(100, 'createPFX', ((1, 'strPassword'),(1, 'pstrPFX'),)))
    ICEnroll4.createFilePFX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(101, 'createFilePFX', ((1, 'strPassword'),(1, 'strPFXFileName'),)))
    ICEnroll4.setPendingRequestInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(102, 'setPendingRequestInfo', ((1, 'lRequestID'),(1, 'strCADNS'),(1, 'strCAName'),(1, 'strFriendlyName'),)))
    ICEnroll4.enumPendingRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Security.Cryptography.Certificates.PENDING_REQUEST_DESIRED_PROPERTY,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(103, 'enumPendingRequest', ((1, 'lIndex'),(1, 'lDesiredProperty'),(1, 'pvarProperty'),)))
    ICEnroll4.removePendingRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(104, 'removePendingRequest', ((1, 'strThumbprint'),)))
    ICEnroll4.GetKeyLenEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.XEKL_KEYSIZE,win32more.Security.Cryptography.Certificates.XEKL_KEYSPEC,POINTER(Int32), use_last_error=False)(105, 'GetKeyLenEx', ((1, 'lSizeSpec'),(1, 'lKeySpec'),(1, 'pdwKeySize'),)))
    ICEnroll4.InstallPKCS7Ex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(106, 'InstallPKCS7Ex', ((1, 'PKCS7'),(1, 'plCertInstalled'),)))
    ICEnroll4.addCertTypeToRequestEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ADDED_CERT_TYPE,win32more.Foundation.BSTR,Int32,win32more.Foundation.BOOL,Int32, use_last_error=False)(107, 'addCertTypeToRequestEx', ((1, 'lType'),(1, 'bstrOIDOrName'),(1, 'lMajorVersion'),(1, 'fMinorVersion'),(1, 'lMinorVersion'),)))
    ICEnroll4.getProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(108, 'getProviderType', ((1, 'strProvName'),(1, 'plProvType'),)))
    ICEnroll4.put_SignerCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(109, 'put_SignerCertificate', ((1, 'bstrCert'),)))
    ICEnroll4.put_ClientId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(110, 'put_ClientId', ((1, 'lClientId'),)))
    ICEnroll4.get_ClientId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(111, 'get_ClientId', ((1, 'plClientId'),)))
    ICEnroll4.addBlobPropertyToCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.BSTR, use_last_error=False)(112, 'addBlobPropertyToCertificate', ((1, 'lPropertyId'),(1, 'lReserved'),(1, 'bstrProperty'),)))
    ICEnroll4.resetBlobProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(113, 'resetBlobProperties', ()))
    ICEnroll4.put_IncludeSubjectKeyID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(114, 'put_IncludeSubjectKeyID', ((1, 'fInclude'),)))
    ICEnroll4.get_IncludeSubjectKeyID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(115, 'get_IncludeSubjectKeyID', ((1, 'pfInclude'),)))
    win32more.Security.Cryptography.Certificates.ICEnroll3
    return ICEnroll4
def _define_IEnroll_head():
    class IEnroll(win32more.System.Com.IUnknown_head):
        Guid = Guid('acaa7838-4585-11d1-ab57-00c04fc295e1')
    return IEnroll
def _define_IEnroll():
    IEnroll = win32more.Security.Cryptography.Certificates.IEnroll_head
    IEnroll.createFilePKCS10WStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'createFilePKCS10WStr', ((1, 'DNName'),(1, 'Usage'),(1, 'wszPKCS10FileName'),)))
    IEnroll.acceptFilePKCS7WStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'acceptFilePKCS7WStr', ((1, 'wszPKCS7FileName'),)))
    IEnroll.createPKCS10WStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(5, 'createPKCS10WStr', ((1, 'DNName'),(1, 'Usage'),(1, 'pPkcs10Blob'),)))
    IEnroll.acceptPKCS7Blob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(6, 'acceptPKCS7Blob', ((1, 'pBlobPKCS7'),)))
    IEnroll.getCertContextFromPKCS7 = COMMETHOD(WINFUNCTYPE(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(7, 'getCertContextFromPKCS7', ((1, 'pBlobPKCS7'),)))
    IEnroll.getMyStore = COMMETHOD(WINFUNCTYPE(c_void_p, use_last_error=False)(8, 'getMyStore', ()))
    IEnroll.getCAStore = COMMETHOD(WINFUNCTYPE(c_void_p, use_last_error=False)(9, 'getCAStore', ()))
    IEnroll.getROOTHStore = COMMETHOD(WINFUNCTYPE(c_void_p, use_last_error=False)(10, 'getROOTHStore', ()))
    IEnroll.enumProvidersWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(11, 'enumProvidersWStr', ((1, 'dwIndex'),(1, 'dwFlags'),(1, 'pbstrProvName'),)))
    IEnroll.enumContainersWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(12, 'enumContainersWStr', ((1, 'dwIndex'),(1, 'pbstr'),)))
    IEnroll.freeRequestInfoBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.CRYPTOAPI_BLOB, use_last_error=False)(13, 'freeRequestInfoBlob', ((1, 'pkcs7OrPkcs10'),)))
    IEnroll.get_MyStoreNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(14, 'get_MyStoreNameWStr', ((1, 'szwName'),)))
    IEnroll.put_MyStoreNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(15, 'put_MyStoreNameWStr', ((1, 'szwName'),)))
    IEnroll.get_MyStoreTypeWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(16, 'get_MyStoreTypeWStr', ((1, 'szwType'),)))
    IEnroll.put_MyStoreTypeWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(17, 'put_MyStoreTypeWStr', ((1, 'szwType'),)))
    IEnroll.get_MyStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(18, 'get_MyStoreFlags', ((1, 'pdwFlags'),)))
    IEnroll.put_MyStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(19, 'put_MyStoreFlags', ((1, 'dwFlags'),)))
    IEnroll.get_CAStoreNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(20, 'get_CAStoreNameWStr', ((1, 'szwName'),)))
    IEnroll.put_CAStoreNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(21, 'put_CAStoreNameWStr', ((1, 'szwName'),)))
    IEnroll.get_CAStoreTypeWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(22, 'get_CAStoreTypeWStr', ((1, 'szwType'),)))
    IEnroll.put_CAStoreTypeWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(23, 'put_CAStoreTypeWStr', ((1, 'szwType'),)))
    IEnroll.get_CAStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(24, 'get_CAStoreFlags', ((1, 'pdwFlags'),)))
    IEnroll.put_CAStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(25, 'put_CAStoreFlags', ((1, 'dwFlags'),)))
    IEnroll.get_RootStoreNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(26, 'get_RootStoreNameWStr', ((1, 'szwName'),)))
    IEnroll.put_RootStoreNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(27, 'put_RootStoreNameWStr', ((1, 'szwName'),)))
    IEnroll.get_RootStoreTypeWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(28, 'get_RootStoreTypeWStr', ((1, 'szwType'),)))
    IEnroll.put_RootStoreTypeWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(29, 'put_RootStoreTypeWStr', ((1, 'szwType'),)))
    IEnroll.get_RootStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(30, 'get_RootStoreFlags', ((1, 'pdwFlags'),)))
    IEnroll.put_RootStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(31, 'put_RootStoreFlags', ((1, 'dwFlags'),)))
    IEnroll.get_RequestStoreNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(32, 'get_RequestStoreNameWStr', ((1, 'szwName'),)))
    IEnroll.put_RequestStoreNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(33, 'put_RequestStoreNameWStr', ((1, 'szwName'),)))
    IEnroll.get_RequestStoreTypeWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(34, 'get_RequestStoreTypeWStr', ((1, 'szwType'),)))
    IEnroll.put_RequestStoreTypeWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(35, 'put_RequestStoreTypeWStr', ((1, 'szwType'),)))
    IEnroll.get_RequestStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(36, 'get_RequestStoreFlags', ((1, 'pdwFlags'),)))
    IEnroll.put_RequestStoreFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(37, 'put_RequestStoreFlags', ((1, 'dwFlags'),)))
    IEnroll.get_ContainerNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(38, 'get_ContainerNameWStr', ((1, 'szwContainer'),)))
    IEnroll.put_ContainerNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(39, 'put_ContainerNameWStr', ((1, 'szwContainer'),)))
    IEnroll.get_ProviderNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(40, 'get_ProviderNameWStr', ((1, 'szwProvider'),)))
    IEnroll.put_ProviderNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(41, 'put_ProviderNameWStr', ((1, 'szwProvider'),)))
    IEnroll.get_ProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(42, 'get_ProviderType', ((1, 'pdwType'),)))
    IEnroll.put_ProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(43, 'put_ProviderType', ((1, 'dwType'),)))
    IEnroll.get_KeySpec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(44, 'get_KeySpec', ((1, 'pdw'),)))
    IEnroll.put_KeySpec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(45, 'put_KeySpec', ((1, 'dw'),)))
    IEnroll.get_ProviderFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(46, 'get_ProviderFlags', ((1, 'pdwFlags'),)))
    IEnroll.put_ProviderFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(47, 'put_ProviderFlags', ((1, 'dwFlags'),)))
    IEnroll.get_UseExistingKeySet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(48, 'get_UseExistingKeySet', ((1, 'fUseExistingKeys'),)))
    IEnroll.put_UseExistingKeySet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(49, 'put_UseExistingKeySet', ((1, 'fUseExistingKeys'),)))
    IEnroll.get_GenKeyFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(50, 'get_GenKeyFlags', ((1, 'pdwFlags'),)))
    IEnroll.put_GenKeyFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(51, 'put_GenKeyFlags', ((1, 'dwFlags'),)))
    IEnroll.get_DeleteRequestCert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(52, 'get_DeleteRequestCert', ((1, 'fDelete'),)))
    IEnroll.put_DeleteRequestCert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(53, 'put_DeleteRequestCert', ((1, 'fDelete'),)))
    IEnroll.get_WriteCertToUserDS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(54, 'get_WriteCertToUserDS', ((1, 'fBool'),)))
    IEnroll.put_WriteCertToUserDS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(55, 'put_WriteCertToUserDS', ((1, 'fBool'),)))
    IEnroll.get_EnableT61DNEncoding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(56, 'get_EnableT61DNEncoding', ((1, 'fBool'),)))
    IEnroll.put_EnableT61DNEncoding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(57, 'put_EnableT61DNEncoding', ((1, 'fBool'),)))
    IEnroll.get_WriteCertToCSP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(58, 'get_WriteCertToCSP', ((1, 'fBool'),)))
    IEnroll.put_WriteCertToCSP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(59, 'put_WriteCertToCSP', ((1, 'fBool'),)))
    IEnroll.get_SPCFileNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(60, 'get_SPCFileNameWStr', ((1, 'szw'),)))
    IEnroll.put_SPCFileNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(61, 'put_SPCFileNameWStr', ((1, 'szw'),)))
    IEnroll.get_PVKFileNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(62, 'get_PVKFileNameWStr', ((1, 'szw'),)))
    IEnroll.put_PVKFileNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(63, 'put_PVKFileNameWStr', ((1, 'szw'),)))
    IEnroll.get_HashAlgorithmWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(64, 'get_HashAlgorithmWStr', ((1, 'szw'),)))
    IEnroll.put_HashAlgorithmWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(65, 'put_HashAlgorithmWStr', ((1, 'szw'),)))
    IEnroll.get_RenewalCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)), use_last_error=False)(66, 'get_RenewalCertificate', ((1, 'ppCertContext'),)))
    IEnroll.put_RenewalCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), use_last_error=False)(67, 'put_RenewalCertificate', ((1, 'pCertContext'),)))
    IEnroll.AddCertTypeToRequestWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(68, 'AddCertTypeToRequestWStr', ((1, 'szw'),)))
    IEnroll.AddNameValuePairToSignatureWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(69, 'AddNameValuePairToSignatureWStr', ((1, 'Name'),(1, 'Value'),)))
    IEnroll.AddExtensionsToRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_EXTENSIONS_head), use_last_error=False)(70, 'AddExtensionsToRequest', ((1, 'pCertExtensions'),)))
    IEnroll.AddAuthenticatedAttributesToPKCS7Request = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CRYPT_ATTRIBUTES_head), use_last_error=False)(71, 'AddAuthenticatedAttributesToPKCS7Request', ((1, 'pAttributes'),)))
    IEnroll.CreatePKCS7RequestFromRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head),POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(72, 'CreatePKCS7RequestFromRequest', ((1, 'pRequest'),(1, 'pSigningCertContext'),(1, 'pPkcs7Blob'),)))
    win32more.System.Com.IUnknown
    return IEnroll
def _define_IEnroll2_head():
    class IEnroll2(win32more.Security.Cryptography.Certificates.IEnroll_head):
        Guid = Guid('c080e199-b7df-11d2-a421-00c04f79fe8e')
    return IEnroll2
def _define_IEnroll2():
    IEnroll2 = win32more.Security.Cryptography.Certificates.IEnroll2_head
    IEnroll2.InstallPKCS7Blob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(73, 'InstallPKCS7Blob', ((1, 'pBlobPKCS7'),)))
    IEnroll2.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(74, 'Reset', ()))
    IEnroll2.GetSupportedKeySpec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(75, 'GetSupportedKeySpec', ((1, 'pdwKeySpec'),)))
    IEnroll2.GetKeyLen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(Int32), use_last_error=False)(76, 'GetKeyLen', ((1, 'fMin'),(1, 'fExchange'),(1, 'pdwKeySize'),)))
    IEnroll2.EnumAlgs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Int32), use_last_error=False)(77, 'EnumAlgs', ((1, 'dwIndex'),(1, 'algClass'),(1, 'pdwAlgID'),)))
    IEnroll2.GetAlgNameWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(78, 'GetAlgNameWStr', ((1, 'algID'),(1, 'ppwsz'),)))
    IEnroll2.put_ReuseHardwareKeyIfUnableToGenNew = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(79, 'put_ReuseHardwareKeyIfUnableToGenNew', ((1, 'fReuseHardwareKeyIfUnableToGenNew'),)))
    IEnroll2.get_ReuseHardwareKeyIfUnableToGenNew = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(80, 'get_ReuseHardwareKeyIfUnableToGenNew', ((1, 'fReuseHardwareKeyIfUnableToGenNew'),)))
    IEnroll2.put_HashAlgID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(81, 'put_HashAlgID', ((1, 'hashAlgID'),)))
    IEnroll2.get_HashAlgID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(82, 'get_HashAlgID', ((1, 'hashAlgID'),)))
    IEnroll2.SetHStoreMy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(83, 'SetHStoreMy', ((1, 'hStore'),)))
    IEnroll2.SetHStoreCA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(84, 'SetHStoreCA', ((1, 'hStore'),)))
    IEnroll2.SetHStoreROOT = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(85, 'SetHStoreROOT', ((1, 'hStore'),)))
    IEnroll2.SetHStoreRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(86, 'SetHStoreRequest', ((1, 'hStore'),)))
    IEnroll2.put_LimitExchangeKeyToEncipherment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(87, 'put_LimitExchangeKeyToEncipherment', ((1, 'fLimitExchangeKeyToEncipherment'),)))
    IEnroll2.get_LimitExchangeKeyToEncipherment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(88, 'get_LimitExchangeKeyToEncipherment', ((1, 'fLimitExchangeKeyToEncipherment'),)))
    IEnroll2.put_EnableSMIMECapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(89, 'put_EnableSMIMECapabilities', ((1, 'fEnableSMIMECapabilities'),)))
    IEnroll2.get_EnableSMIMECapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(90, 'get_EnableSMIMECapabilities', ((1, 'fEnableSMIMECapabilities'),)))
    win32more.Security.Cryptography.Certificates.IEnroll
    return IEnroll2
def _define_IEnroll4_head():
    class IEnroll4(win32more.Security.Cryptography.Certificates.IEnroll2_head):
        Guid = Guid('f8053fe5-78f4-448f-a0db-41d61b73446b')
    return IEnroll4
def _define_IEnroll4():
    IEnroll4 = win32more.Security.Cryptography.Certificates.IEnroll4_head
    IEnroll4.put_ThumbPrintWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.CRYPTOAPI_BLOB, use_last_error=False)(91, 'put_ThumbPrintWStr', ((1, 'thumbPrintBlob'),)))
    IEnroll4.get_ThumbPrintWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(92, 'get_ThumbPrintWStr', ((1, 'thumbPrintBlob'),)))
    IEnroll4.SetPrivateKeyArchiveCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), use_last_error=False)(93, 'SetPrivateKeyArchiveCertificate', ((1, 'pPrivateKeyArchiveCert'),)))
    IEnroll4.GetPrivateKeyArchiveCertificate = COMMETHOD(WINFUNCTYPE(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), use_last_error=False)(94, 'GetPrivateKeyArchiveCertificate', ()))
    IEnroll4.binaryBlobToString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(95, 'binaryBlobToString', ((1, 'Flags'),(1, 'pblobBinary'),(1, 'ppwszString'),)))
    IEnroll4.stringToBinaryBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head),POINTER(Int32),POINTER(Int32), use_last_error=False)(96, 'stringToBinaryBlob', ((1, 'Flags'),(1, 'pwszString'),(1, 'pblobBinary'),(1, 'pdwSkip'),(1, 'pdwFlags'),)))
    IEnroll4.addExtensionToRequestWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(97, 'addExtensionToRequestWStr', ((1, 'Flags'),(1, 'pwszName'),(1, 'pblobValue'),)))
    IEnroll4.addAttributeToRequestWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(98, 'addAttributeToRequestWStr', ((1, 'Flags'),(1, 'pwszName'),(1, 'pblobValue'),)))
    IEnroll4.addNameValuePairToRequestWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(99, 'addNameValuePairToRequestWStr', ((1, 'Flags'),(1, 'pwszName'),(1, 'pwszValue'),)))
    IEnroll4.resetExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(100, 'resetExtensions', ()))
    IEnroll4.resetAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(101, 'resetAttributes', ()))
    IEnroll4.createRequestWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CERT_CREATE_REQUEST_FLAGS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(102, 'createRequestWStr', ((1, 'Flags'),(1, 'pwszDNName'),(1, 'pwszUsage'),(1, 'pblobRequest'),)))
    IEnroll4.createFileRequestWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.CERT_CREATE_REQUEST_FLAGS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(103, 'createFileRequestWStr', ((1, 'Flags'),(1, 'pwszDNName'),(1, 'pwszUsage'),(1, 'pwszRequestFileName'),)))
    IEnroll4.acceptResponseBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(104, 'acceptResponseBlob', ((1, 'pblobResponse'),)))
    IEnroll4.acceptFileResponseWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(105, 'acceptFileResponseWStr', ((1, 'pwszResponseFileName'),)))
    IEnroll4.getCertContextFromResponseBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head),POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)), use_last_error=False)(106, 'getCertContextFromResponseBlob', ((1, 'pblobResponse'),(1, 'ppCertContext'),)))
    IEnroll4.getCertContextFromFileResponseWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)), use_last_error=False)(107, 'getCertContextFromFileResponseWStr', ((1, 'pwszResponseFileName'),(1, 'ppCertContext'),)))
    IEnroll4.createPFXWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(108, 'createPFXWStr', ((1, 'pwszPassword'),(1, 'pblobPFX'),)))
    IEnroll4.createFilePFXWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(109, 'createFilePFXWStr', ((1, 'pwszPassword'),(1, 'pwszPFXFileName'),)))
    IEnroll4.setPendingRequestInfoWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(110, 'setPendingRequestInfoWStr', ((1, 'lRequestID'),(1, 'pwszCADNS'),(1, 'pwszCAName'),(1, 'pwszFriendlyName'),)))
    IEnroll4.enumPendingRequestWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Security.Cryptography.Certificates.PENDING_REQUEST_DESIRED_PROPERTY,c_void_p, use_last_error=False)(111, 'enumPendingRequestWStr', ((1, 'lIndex'),(1, 'lDesiredProperty'),(1, 'ppProperty'),)))
    IEnroll4.removePendingRequestWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.CRYPTOAPI_BLOB, use_last_error=False)(112, 'removePendingRequestWStr', ((1, 'thumbPrintBlob'),)))
    IEnroll4.GetKeyLenEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.XEKL_KEYSIZE,win32more.Security.Cryptography.Certificates.XEKL_KEYSPEC,POINTER(Int32), use_last_error=False)(113, 'GetKeyLenEx', ((1, 'lSizeSpec'),(1, 'lKeySpec'),(1, 'pdwKeySize'),)))
    IEnroll4.InstallPKCS7BlobEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head),POINTER(Int32), use_last_error=False)(114, 'InstallPKCS7BlobEx', ((1, 'pBlobPKCS7'),(1, 'plCertInstalled'),)))
    IEnroll4.AddCertTypeToRequestWStrEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Cryptography.Certificates.ADDED_CERT_TYPE,win32more.Foundation.PWSTR,Int32,win32more.Foundation.BOOL,Int32, use_last_error=False)(115, 'AddCertTypeToRequestWStrEx', ((1, 'lType'),(1, 'pwszOIDOrName'),(1, 'lMajorVersion'),(1, 'fMinorVersion'),(1, 'lMinorVersion'),)))
    IEnroll4.getProviderTypeWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Int32), use_last_error=False)(116, 'getProviderTypeWStr', ((1, 'pwszProvName'),(1, 'plProvType'),)))
    IEnroll4.addBlobPropertyToCertificateWStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head), use_last_error=False)(117, 'addBlobPropertyToCertificateWStr', ((1, 'lPropertyId'),(1, 'lReserved'),(1, 'pBlobProperty'),)))
    IEnroll4.SetSignerCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), use_last_error=False)(118, 'SetSignerCertificate', ((1, 'pSignerCert'),)))
    IEnroll4.put_ClientId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(119, 'put_ClientId', ((1, 'lClientId'),)))
    IEnroll4.get_ClientId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(120, 'get_ClientId', ((1, 'plClientId'),)))
    IEnroll4.put_IncludeSubjectKeyID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(121, 'put_IncludeSubjectKeyID', ((1, 'fInclude'),)))
    IEnroll4.get_IncludeSubjectKeyID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(122, 'get_IncludeSubjectKeyID', ((1, 'pfInclude'),)))
    win32more.Security.Cryptography.Certificates.IEnroll2
    return IEnroll4
def _define_ICertRequestD_head():
    class ICertRequestD(win32more.System.Com.IUnknown_head):
        Guid = Guid('d99e6e70-fc88-11d0-b498-00a0c90312f3')
    return ICertRequestD
def _define_ICertRequestD():
    ICertRequestD = win32more.Security.Cryptography.Certificates.ICertRequestD_head
    ICertRequestD.Request = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head),POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head),POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head),POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head), use_last_error=False)(3, 'Request', ((1, 'dwFlags'),(1, 'pwszAuthority'),(1, 'pdwRequestId'),(1, 'pdwDisposition'),(1, 'pwszAttributes'),(1, 'pctbRequest'),(1, 'pctbCertChain'),(1, 'pctbEncodedCert'),(1, 'pctbDispositionMessage'),)))
    ICertRequestD.GetCACert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head), use_last_error=False)(4, 'GetCACert', ((1, 'fchain'),(1, 'pwszAuthority'),(1, 'pctbOut'),)))
    ICertRequestD.Ping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'Ping', ((1, 'pwszAuthority'),)))
    win32more.System.Com.IUnknown
    return ICertRequestD
def _define_ICertRequestD2_head():
    class ICertRequestD2(win32more.Security.Cryptography.Certificates.ICertRequestD_head):
        Guid = Guid('5422fd3a-d4b8-4cef-a12e-e87d4ca22e90')
    return ICertRequestD2
def _define_ICertRequestD2():
    ICertRequestD2 = win32more.Security.Cryptography.Certificates.ICertRequestD2_head
    ICertRequestD2.Request2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head),POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head),POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head),POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head), use_last_error=False)(6, 'Request2', ((1, 'pwszAuthority'),(1, 'dwFlags'),(1, 'pwszSerialNumber'),(1, 'pdwRequestId'),(1, 'pdwDisposition'),(1, 'pwszAttributes'),(1, 'pctbRequest'),(1, 'pctbFullResponse'),(1, 'pctbEncodedCert'),(1, 'pctbDispositionMessage'),)))
    ICertRequestD2.GetCAProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,Int32,Int32,POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head), use_last_error=False)(7, 'GetCAProperty', ((1, 'pwszAuthority'),(1, 'PropId'),(1, 'PropIndex'),(1, 'PropType'),(1, 'pctbPropertyValue'),)))
    ICertRequestD2.GetCAPropertyInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Int32),POINTER(win32more.Security.Cryptography.Certificates.CERTTRANSBLOB_head), use_last_error=False)(8, 'GetCAPropertyInfo', ((1, 'pwszAuthority'),(1, 'pcProperty'),(1, 'pctbPropInfo'),)))
    ICertRequestD2.Ping2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(9, 'Ping2', ((1, 'pwszAuthority'),)))
    win32more.Security.Cryptography.Certificates.ICertRequestD
    return ICertRequestD2
def _define_CertSrvIsServerOnlineW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("CertSrvIsServerOnlineW", windll["certadm"]), ((1, 'pwszServerName'),(1, 'pfServerOnline'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvBackupGetDynamicFileListW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(("CertSrvBackupGetDynamicFileListW", windll["certadm"]), ((1, 'hbc'),(1, 'ppwszzFileList'),(1, 'pcbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvBackupPrepareW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Security.Cryptography.Certificates.CSBACKUP_TYPE,POINTER(c_void_p), use_last_error=False)(("CertSrvBackupPrepareW", windll["certadm"]), ((1, 'pwszServerName'),(1, 'grbitJet'),(1, 'dwBackupFlags'),(1, 'phbc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvBackupGetDatabaseNamesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(("CertSrvBackupGetDatabaseNamesW", windll["certadm"]), ((1, 'hbc'),(1, 'ppwszzAttachmentInformation'),(1, 'pcbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvBackupOpenFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.LARGE_INTEGER_head), use_last_error=False)(("CertSrvBackupOpenFileW", windll["certadm"]), ((1, 'hbc'),(1, 'pwszAttachmentName'),(1, 'cbReadHintSize'),(1, 'pliFileSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvBackupRead():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("CertSrvBackupRead", windll["certadm"]), ((1, 'hbc'),(1, 'pvBuffer'),(1, 'cbBuffer'),(1, 'pcbRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvBackupClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("CertSrvBackupClose", windll["certadm"]), ((1, 'hbc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvBackupGetBackupLogsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(("CertSrvBackupGetBackupLogsW", windll["certadm"]), ((1, 'hbc'),(1, 'ppwszzBackupLogFiles'),(1, 'pcbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvBackupTruncateLogs():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("CertSrvBackupTruncateLogs", windll["certadm"]), ((1, 'hbc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvBackupEnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("CertSrvBackupEnd", windll["certadm"]), ((1, 'hbc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvBackupFree():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("CertSrvBackupFree", windll["certadm"]), ((1, 'pv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvRestoreGetDatabaseLocationsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(("CertSrvRestoreGetDatabaseLocationsW", windll["certadm"]), ((1, 'hbc'),(1, 'ppwszzDatabaseLocationList'),(1, 'pcbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvRestorePrepareW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(c_void_p), use_last_error=False)(("CertSrvRestorePrepareW", windll["certadm"]), ((1, 'pwszServerName'),(1, 'dwRestoreFlags'),(1, 'phbc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvRestoreRegisterW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.Certificates.CSEDB_RSTMAPW_head),Int32,win32more.Foundation.PWSTR,UInt32,UInt32, use_last_error=False)(("CertSrvRestoreRegisterW", windll["certadm"]), ((1, 'hbc'),(1, 'pwszCheckPointFilePath'),(1, 'pwszLogPath'),(1, 'rgrstmap'),(1, 'crstmap'),(1, 'pwszBackupLogPath'),(1, 'genLow'),(1, 'genHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvRestoreRegisterThroughFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.Certificates.CSEDB_RSTMAPW_head),Int32,win32more.Foundation.PWSTR,UInt32,UInt32, use_last_error=False)(("CertSrvRestoreRegisterThroughFile", windll["certadm"]), ((1, 'hbc'),(1, 'pwszCheckPointFilePath'),(1, 'pwszLogPath'),(1, 'rgrstmap'),(1, 'crstmap'),(1, 'pwszBackupLogPath'),(1, 'genLow'),(1, 'genHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvRestoreRegisterComplete():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.HRESULT, use_last_error=False)(("CertSrvRestoreRegisterComplete", windll["certadm"]), ((1, 'hbc'),(1, 'hrRestoreState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvRestoreEnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("CertSrvRestoreEnd", windll["certadm"]), ((1, 'hbc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSrvServerControlW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(("CertSrvServerControlW", windll["certadm"]), ((1, 'pwszServerName'),(1, 'dwControlFlags'),(1, 'pcbOut'),(1, 'ppbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PstGetTrustAnchors():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Foundation.UNICODE_STRING_head),UInt32,POINTER(win32more.Security.Cryptography.CERT_SELECT_CRITERIA),POINTER(POINTER(win32more.Security.Authentication.Identity.SecPkgContext_IssuerListInfoEx_head)), use_last_error=False)(("PstGetTrustAnchors", windll["certpoleng"]), ((1, 'pTargetName'),(1, 'cCriteria'),(1, 'rgpCriteria'),(1, 'ppTrustedIssuers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PstGetTrustAnchorsEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Foundation.UNICODE_STRING_head),UInt32,POINTER(win32more.Security.Cryptography.CERT_SELECT_CRITERIA),POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(POINTER(win32more.Security.Authentication.Identity.SecPkgContext_IssuerListInfoEx_head)), use_last_error=False)(("PstGetTrustAnchorsEx", windll["certpoleng"]), ((1, 'pTargetName'),(1, 'cCriteria'),(1, 'rgpCriteria'),(1, 'pCertContext'),(1, 'ppTrustedIssuers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PstGetCertificateChain():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(win32more.Security.Authentication.Identity.SecPkgContext_IssuerListInfoEx_head),POINTER(POINTER(win32more.Security.Cryptography.CERT_CHAIN_CONTEXT_head)), use_last_error=False)(("PstGetCertificateChain", windll["certpoleng"]), ((1, 'pCert'),(1, 'pTrustedIssuers'),(1, 'ppCertChainContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PstGetCertificates():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Foundation.UNICODE_STRING_head),UInt32,POINTER(win32more.Security.Cryptography.CERT_SELECT_CRITERIA),win32more.Foundation.BOOL,POINTER(UInt32),POINTER(POINTER(POINTER(win32more.Security.Cryptography.CERT_CHAIN_CONTEXT_head))), use_last_error=False)(("PstGetCertificates", windll["certpoleng"]), ((1, 'pTargetName'),(1, 'cCriteria'),(1, 'rgpCriteria'),(1, 'bIsClient'),(1, 'pdwCertChainContextCount'),(1, 'ppCertChainContexts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PstAcquirePrivateKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), use_last_error=False)(("PstAcquirePrivateKey", windll["certpoleng"]), ((1, 'pCert'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PstValidate():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Foundation.UNICODE_STRING_head),win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.CERT_USAGE_MATCH_head),POINTER(c_void_p),POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(Guid), use_last_error=False)(("PstValidate", windll["certpoleng"]), ((1, 'pTargetName'),(1, 'bIsClient'),(1, 'pRequestedIssuancePolicy'),(1, 'phAdditionalCertStore'),(1, 'pCert'),(1, 'pProvGUID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PstMapCertificate():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(win32more.Security.Authentication.Identity.LSA_TOKEN_INFORMATION_TYPE),POINTER(c_void_p), use_last_error=False)(("PstMapCertificate", windll["certpoleng"]), ((1, 'pCert'),(1, 'pTokenInformationType'),(1, 'ppTokenInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PstGetUserNameForCertificate():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(win32more.Foundation.UNICODE_STRING_head), use_last_error=False)(("PstGetUserNameForCertificate", windll["certpoleng"]), ((1, 'pCertContext'),(1, 'UserName'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CA_DISP_INCOMPLETE",
    "CA_DISP_ERROR",
    "CA_DISP_REVOKED",
    "CA_DISP_VALID",
    "CA_DISP_INVALID",
    "CA_DISP_UNDER_SUBMISSION",
    "KRA_DISP_EXPIRED",
    "KRA_DISP_NOTFOUND",
    "KRA_DISP_REVOKED",
    "KRA_DISP_VALID",
    "KRA_DISP_INVALID",
    "KRA_DISP_UNTRUSTED",
    "KRA_DISP_NOTLOADED",
    "CA_ACCESS_MASKROLES",
    "CA_CRL_BASE",
    "CA_CRL_DELTA",
    "CA_CRL_REPUBLISH",
    "ICF_ALLOWFOREIGN",
    "ICF_EXISTINGROW",
    "IKF_OVERWRITE",
    "CSBACKUP_TYPE_MASK",
    "CSRESTORE_TYPE_FULL",
    "CSRESTORE_TYPE_ONLINE",
    "CSRESTORE_TYPE_CATCHUP",
    "CSRESTORE_TYPE_MASK",
    "CSBACKUP_DISABLE_INCREMENTAL",
    "CSBFT_DIRECTORY",
    "CSBFT_DATABASE_DIRECTORY",
    "CSBFT_LOG_DIRECTORY",
    "CSCONTROL_SHUTDOWN",
    "CSCONTROL_SUSPEND",
    "CSCONTROL_RESTART",
    "CAIF_DSENTRY",
    "CAIF_SHAREDFOLDERENTRY",
    "CAIF_REGISTRY",
    "CAIF_LOCAL",
    "CAIF_REGISTRYPARENT",
    "CR_IN_ENCODEANY",
    "CR_IN_ENCODEMASK",
    "CR_IN_FORMATANY",
    "CR_IN_PKCS10",
    "CR_IN_KEYGEN",
    "CR_IN_PKCS7",
    "CR_IN_CMC",
    "CR_IN_CHALLENGERESPONSE",
    "CR_IN_SIGNEDCERTIFICATETIMESTAMPLIST",
    "CR_IN_FORMATMASK",
    "CR_IN_SCEP",
    "CR_IN_RPC",
    "CR_IN_HTTP",
    "CR_IN_FULLRESPONSE",
    "CR_IN_CRLS",
    "CR_IN_MACHINE",
    "CR_IN_ROBO",
    "CR_IN_CLIENTIDNONE",
    "CR_IN_CONNECTONLY",
    "CR_IN_RETURNCHALLENGE",
    "CR_IN_SCEPPOST",
    "CR_IN_CERTIFICATETRANSPARENCY",
    "CC_UIPICKCONFIGSKIPLOCALCA",
    "CR_DISP_REVOKED",
    "CR_OUT_BASE64REQUESTHEADER",
    "CR_OUT_HEX",
    "CR_OUT_HEXASCII",
    "CR_OUT_BASE64X509CRLHEADER",
    "CR_OUT_HEXADDR",
    "CR_OUT_HEXASCIIADDR",
    "CR_OUT_HEXRAW",
    "CR_OUT_ENCODEMASK",
    "CR_OUT_CHAIN",
    "CR_OUT_CRLS",
    "CR_OUT_NOCRLF",
    "CR_OUT_NOCR",
    "CR_GEMT_DEFAULT",
    "CR_GEMT_HRESULT_STRING",
    "CR_GEMT_HTTP_ERROR",
    "CR_PROP_NONE",
    "CR_PROP_FILEVERSION",
    "CR_PROP_PRODUCTVERSION",
    "CR_PROP_EXITCOUNT",
    "CR_PROP_EXITDESCRIPTION",
    "CR_PROP_POLICYDESCRIPTION",
    "CR_PROP_CANAME",
    "CR_PROP_SANITIZEDCANAME",
    "CR_PROP_SHAREDFOLDER",
    "CR_PROP_PARENTCA",
    "CR_PROP_CATYPE",
    "CR_PROP_CASIGCERTCOUNT",
    "CR_PROP_CASIGCERT",
    "CR_PROP_CASIGCERTCHAIN",
    "CR_PROP_CAXCHGCERTCOUNT",
    "CR_PROP_CAXCHGCERT",
    "CR_PROP_CAXCHGCERTCHAIN",
    "CR_PROP_BASECRL",
    "CR_PROP_DELTACRL",
    "CR_PROP_CACERTSTATE",
    "CR_PROP_CRLSTATE",
    "CR_PROP_CAPROPIDMAX",
    "CR_PROP_DNSNAME",
    "CR_PROP_ROLESEPARATIONENABLED",
    "CR_PROP_KRACERTUSEDCOUNT",
    "CR_PROP_KRACERTCOUNT",
    "CR_PROP_KRACERT",
    "CR_PROP_KRACERTSTATE",
    "CR_PROP_ADVANCEDSERVER",
    "CR_PROP_TEMPLATES",
    "CR_PROP_BASECRLPUBLISHSTATUS",
    "CR_PROP_DELTACRLPUBLISHSTATUS",
    "CR_PROP_CASIGCERTCRLCHAIN",
    "CR_PROP_CAXCHGCERTCRLCHAIN",
    "CR_PROP_CACERTSTATUSCODE",
    "CR_PROP_CAFORWARDCROSSCERT",
    "CR_PROP_CABACKWARDCROSSCERT",
    "CR_PROP_CAFORWARDCROSSCERTSTATE",
    "CR_PROP_CABACKWARDCROSSCERTSTATE",
    "CR_PROP_CACERTVERSION",
    "CR_PROP_SANITIZEDCASHORTNAME",
    "CR_PROP_CERTCDPURLS",
    "CR_PROP_CERTAIAURLS",
    "CR_PROP_CERTAIAOCSPURLS",
    "CR_PROP_LOCALENAME",
    "CR_PROP_SUBJECTTEMPLATE_OIDS",
    "CR_PROP_SCEPSERVERCERTS",
    "CR_PROP_SCEPSERVERCAPABILITIES",
    "CR_PROP_SCEPSERVERCERTSCHAIN",
    "CR_PROP_SCEPMIN",
    "CR_PROP_SCEPMAX",
    "FR_PROP_CLAIMCHALLENGE",
    "EAN_NAMEOBJECTID",
    "EANR_SUPPRESS_IA5CONVERSION",
    "CERTENROLL_INDEX_BASE",
    "EXITEVENT_INVALID",
    "EXITEVENT_STARTUP",
    "EXITEVENT_CERTIMPORTED",
    "ENUMEXT_OBJECTID",
    "CMM_REFRESHONLY",
    "CMM_READONLY",
    "DBSESSIONCOUNTDEFAULT",
    "DBFLAGS_READONLY",
    "DBFLAGS_CREATEIFNEEDED",
    "DBFLAGS_CIRCULARLOGGING",
    "DBFLAGS_LAZYFLUSH",
    "DBFLAGS_MAXCACHESIZEX100",
    "DBFLAGS_CHECKPOINTDEPTH60MB",
    "DBFLAGS_LOGBUFFERSLARGE",
    "DBFLAGS_LOGBUFFERSHUGE",
    "DBFLAGS_LOGFILESIZE16MB",
    "DBFLAGS_MULTITHREADTRANSACTIONS",
    "DBFLAGS_DISABLESNAPSHOTBACKUP",
    "DBFLAGS_ENABLEVOLATILEREQUESTS",
    "LDAPF_SSLENABLE",
    "LDAPF_SIGNDISABLE",
    "CSVER_MAJOR_WIN2K",
    "CSVER_MINOR_WIN2K",
    "CSVER_MAJOR_WHISTLER",
    "CSVER_MINOR_WHISTLER_BETA2",
    "CSVER_MINOR_WHISTLER_BETA3",
    "CSVER_MAJOR_LONGHORN",
    "CSVER_MINOR_LONGHORN_BETA1",
    "CSVER_MAJOR_WIN7",
    "CSVER_MINOR_WIN7",
    "CSVER_MAJOR_WIN8",
    "CSVER_MINOR_WIN8",
    "CSVER_MAJOR_WINBLUE",
    "CSVER_MINOR_WINBLUE",
    "CSVER_MAJOR_THRESHOLD",
    "CSVER_MINOR_THRESHOLD",
    "CSVER_MAJOR",
    "CSVER_MINOR",
    "CCLOCKSKEWMINUTESDEFAULT",
    "CVIEWAGEMINUTESDEFAULT",
    "SETUP_SERVER_FLAG",
    "SETUP_CLIENT_FLAG",
    "SETUP_SUSPEND_FLAG",
    "SETUP_REQUEST_FLAG",
    "SETUP_ONLINE_FLAG",
    "SETUP_DENIED_FLAG",
    "SETUP_CREATEDB_FLAG",
    "SETUP_ATTEMPT_VROOT_CREATE",
    "SETUP_FORCECRL_FLAG",
    "SETUP_UPDATE_CAOBJECT_SVRTYPE",
    "SETUP_SERVER_UPGRADED_FLAG",
    "SETUP_W2K_SECURITY_NOT_UPGRADED_FLAG",
    "SETUP_SECURITY_CHANGED",
    "SETUP_DCOM_SECURITY_UPDATED_FLAG",
    "SETUP_SERVER_IS_UP_TO_DATE_FLAG",
    "CRLF_DELTA_USE_OLDEST_UNEXPIRED_BASE",
    "CRLF_DELETE_EXPIRED_CRLS",
    "CRLF_CRLNUMBER_CRITICAL",
    "CRLF_REVCHECK_IGNORE_OFFLINE",
    "CRLF_IGNORE_INVALID_POLICIES",
    "CRLF_REBUILD_MODIFIED_SUBJECT_ONLY",
    "CRLF_SAVE_FAILED_CERTS",
    "CRLF_IGNORE_UNKNOWN_CMC_ATTRIBUTES",
    "CRLF_IGNORE_CROSS_CERT_TRUST_ERROR",
    "CRLF_PUBLISH_EXPIRED_CERT_CRLS",
    "CRLF_ENFORCE_ENROLLMENT_AGENT",
    "CRLF_DISABLE_RDN_REORDER",
    "CRLF_DISABLE_ROOT_CROSS_CERTS",
    "CRLF_LOG_FULL_RESPONSE",
    "CRLF_USE_XCHG_CERT_TEMPLATE",
    "CRLF_USE_CROSS_CERT_TEMPLATE",
    "CRLF_ALLOW_REQUEST_ATTRIBUTE_SUBJECT",
    "CRLF_REVCHECK_IGNORE_NOREVCHECK",
    "CRLF_PRESERVE_EXPIRED_CA_CERTS",
    "CRLF_PRESERVE_REVOKED_CA_CERTS",
    "CRLF_DISABLE_CHAIN_VERIFICATION",
    "CRLF_BUILD_ROOTCA_CRLENTRIES_BASEDONKEY",
    "KRAF_ENABLEFOREIGN",
    "KRAF_SAVEBADREQUESTKEY",
    "KRAF_ENABLEARCHIVEALL",
    "KRAF_DISABLEUSEDEFAULTPROVIDER",
    "IF_LOCKICERTREQUEST",
    "IF_NOREMOTEICERTREQUEST",
    "IF_NOLOCALICERTREQUEST",
    "IF_NORPCICERTREQUEST",
    "IF_NOREMOTEICERTADMIN",
    "IF_NOLOCALICERTADMIN",
    "IF_NOREMOTEICERTADMINBACKUP",
    "IF_NOLOCALICERTADMINBACKUP",
    "IF_NOSNAPSHOTBACKUP",
    "IF_ENFORCEENCRYPTICERTREQUEST",
    "IF_ENFORCEENCRYPTICERTADMIN",
    "IF_ENABLEEXITKEYRETRIEVAL",
    "IF_ENABLEADMINASAUDITOR",
    "PROCFLG_NONE",
    "PROCFLG_ENFORCEGOODKEYS",
    "CSURL_SERVERPUBLISH",
    "CSURL_ADDTOCERTCDP",
    "CSURL_ADDTOFRESHESTCRL",
    "CSURL_ADDTOCRLCDP",
    "CSURL_PUBLISHRETRY",
    "CSURL_ADDTOCERTOCSP",
    "CSURL_SERVERPUBLISHDELTA",
    "CSURL_ADDTOIDP",
    "CAPATHLENGTH_INFINITE",
    "REQDISP_PENDING",
    "REQDISP_ISSUE",
    "REQDISP_DENY",
    "REQDISP_USEREQUESTATTRIBUTE",
    "REQDISP_MASK",
    "REQDISP_PENDINGFIRST",
    "REQDISP_DEFAULT_ENTERPRISE",
    "REVEXT_CDPLDAPURL_OLD",
    "REVEXT_CDPHTTPURL_OLD",
    "REVEXT_CDPFTPURL_OLD",
    "REVEXT_CDPFILEURL_OLD",
    "REVEXT_CDPURLMASK_OLD",
    "REVEXT_CDPENABLE",
    "REVEXT_ASPENABLE",
    "REVEXT_DEFAULT_NODS",
    "REVEXT_DEFAULT_DS",
    "ISSCERT_LDAPURL_OLD",
    "ISSCERT_HTTPURL_OLD",
    "ISSCERT_FTPURL_OLD",
    "ISSCERT_FILEURL_OLD",
    "ISSCERT_URLMASK_OLD",
    "ISSCERT_ENABLE",
    "ISSCERT_DEFAULT_NODS",
    "ISSCERT_DEFAULT_DS",
    "EDITF_ENABLEREQUESTEXTENSIONS",
    "EDITF_REQUESTEXTENSIONLIST",
    "EDITF_DISABLEEXTENSIONLIST",
    "EDITF_ADDOLDKEYUSAGE",
    "EDITF_ADDOLDCERTTYPE",
    "EDITF_ATTRIBUTEENDDATE",
    "EDITF_BASICCONSTRAINTSCRITICAL",
    "EDITF_BASICCONSTRAINTSCA",
    "EDITF_ENABLEAKIKEYID",
    "EDITF_ATTRIBUTECA",
    "EDITF_IGNOREREQUESTERGROUP",
    "EDITF_ENABLEAKIISSUERNAME",
    "EDITF_ENABLEAKIISSUERSERIAL",
    "EDITF_ENABLEAKICRITICAL",
    "EDITF_SERVERUPGRADED",
    "EDITF_ATTRIBUTEEKU",
    "EDITF_ENABLEDEFAULTSMIME",
    "EDITF_EMAILOPTIONAL",
    "EDITF_ATTRIBUTESUBJECTALTNAME2",
    "EDITF_ENABLELDAPREFERRALS",
    "EDITF_ENABLECHASECLIENTDC",
    "EDITF_AUDITCERTTEMPLATELOAD",
    "EDITF_DISABLEOLDOSCNUPN",
    "EDITF_DISABLELDAPPACKAGELIST",
    "EDITF_ENABLEUPNMAP",
    "EDITF_ENABLEOCSPREVNOCHECK",
    "EDITF_ENABLERENEWONBEHALFOF",
    "EDITF_ENABLEKEYENCIPHERMENTCACERT",
    "EXITPUB_FILE",
    "EXITPUB_ACTIVEDIRECTORY",
    "EXITPUB_REMOVEOLDCERTS",
    "EXITPUB_DEFAULT_ENTERPRISE",
    "EXITPUB_DEFAULT_STANDALONE",
    "TP_MACHINEPOLICY",
    "KR_ENABLE_MACHINE",
    "KR_ENABLE_USER",
    "EXTENSION_CRITICAL_FLAG",
    "EXTENSION_DISABLE_FLAG",
    "EXTENSION_DELETE_FLAG",
    "EXTENSION_POLICY_MASK",
    "EXTENSION_ORIGIN_REQUEST",
    "EXTENSION_ORIGIN_POLICY",
    "EXTENSION_ORIGIN_ADMIN",
    "EXTENSION_ORIGIN_SERVER",
    "EXTENSION_ORIGIN_RENEWALCERT",
    "EXTENSION_ORIGIN_IMPORTEDCERT",
    "EXTENSION_ORIGIN_PKCS7",
    "EXTENSION_ORIGIN_CMC",
    "EXTENSION_ORIGIN_CACERT",
    "EXTENSION_ORIGIN_MASK",
    "CPF_BASE",
    "CPF_DELTA",
    "CPF_COMPLETE",
    "CPF_SHADOW",
    "CPF_CASTORE_ERROR",
    "CPF_BADURL_ERROR",
    "CPF_MANUAL",
    "CPF_SIGNATURE_ERROR",
    "CPF_LDAP_ERROR",
    "CPF_FILE_ERROR",
    "CPF_FTP_ERROR",
    "CPF_HTTP_ERROR",
    "CPF_POSTPONED_BASE_LDAP_ERROR",
    "CPF_POSTPONED_BASE_FILE_ERROR",
    "PROPTYPE_MASK",
    "PROPCALLER_SERVER",
    "PROPCALLER_POLICY",
    "PROPCALLER_EXIT",
    "PROPCALLER_ADMIN",
    "PROPCALLER_REQUEST",
    "PROPCALLER_MASK",
    "PROPFLAGS_INDEXED",
    "CR_FLG_FORCETELETEX",
    "CR_FLG_RENEWAL",
    "CR_FLG_FORCEUTF8",
    "CR_FLG_CAXCHGCERT",
    "CR_FLG_ENROLLONBEHALFOF",
    "CR_FLG_SUBJECTUNMODIFIED",
    "CR_FLG_VALIDENCRYPTEDKEYHASH",
    "CR_FLG_CACROSSCERT",
    "CR_FLG_ENFORCEUTF8",
    "CR_FLG_DEFINEDCACERT",
    "CR_FLG_CHALLENGEPENDING",
    "CR_FLG_CHALLENGESATISFIED",
    "CR_FLG_TRUSTONUSE",
    "CR_FLG_TRUSTEKCERT",
    "CR_FLG_TRUSTEKKEY",
    "CR_FLG_PUBLISHERROR",
    "DB_DISP_ACTIVE",
    "DB_DISP_PENDING",
    "DB_DISP_QUEUE_MAX",
    "DB_DISP_FOREIGN",
    "DB_DISP_CA_CERT",
    "DB_DISP_CA_CERT_CHAIN",
    "DB_DISP_KRA_CERT",
    "DB_DISP_LOG_MIN",
    "DB_DISP_ISSUED",
    "DB_DISP_REVOKED",
    "DB_DISP_LOG_FAILED_MIN",
    "DB_DISP_ERROR",
    "DB_DISP_DENIED",
    "VR_PENDING",
    "VR_INSTANT_OK",
    "VR_INSTANT_BAD",
    "CV_OUT_HEXRAW",
    "CV_OUT_ENCODEMASK",
    "CV_OUT_NOCRLF",
    "CV_OUT_NOCR",
    "CVR_SEEK_NONE",
    "CVR_SEEK_MASK",
    "CVR_SEEK_NODELTA",
    "CVR_SORT_NONE",
    "CVR_SORT_ASCEND",
    "CVR_SORT_DESCEND",
    "CV_COLUMN_EXTENSION_DEFAULT",
    "CV_COLUMN_ATTRIBUTE_DEFAULT",
    "CV_COLUMN_CRL_DEFAULT",
    "CV_COLUMN_LOG_REVOKED_DEFAULT",
    "CVRC_TABLE_MASK",
    "CVRC_TABLE_SHIFT",
    "CRYPT_ENUM_ALL_PROVIDERS",
    "XEPR_ENUM_FIRST",
    "XEPR_DATE",
    "XEPR_TEMPLATENAME",
    "XEPR_VERSION",
    "XEPR_V1TEMPLATENAME",
    "XEPR_V2TEMPLATEOID",
    "XEKL_KEYSIZE_DEFAULT",
    "XECP_STRING_PROPERTY",
    "XECI_DISABLE",
    "XECI_XENROLL",
    "XECI_AUTOENROLL",
    "XECI_REQWIZARD",
    "XECI_CERTREQ",
    "wszCMM_PROP_NAME",
    "wszCMM_PROP_DESCRIPTION",
    "wszCMM_PROP_COPYRIGHT",
    "wszCMM_PROP_FILEVER",
    "wszCMM_PROP_PRODUCTVER",
    "wszCMM_PROP_DISPLAY_HWND",
    "wszCMM_PROP_ISMULTITHREADED",
    "CERT_VIEW_COLUMN_INDEX",
    "CV_COLUMN_LOG_DEFAULT",
    "CV_COLUMN_LOG_FAILED_DEFAULT",
    "CV_COLUMN_QUEUE_DEFAULT",
    "CERT_DELETE_ROW_FLAGS",
    "CDR_EXPIRED",
    "CDR_REQUEST_LAST_CHANGED",
    "FULL_RESPONSE_PROPERTY_ID",
    "FR_PROP_NONE",
    "FR_PROP_FULLRESPONSE",
    "FR_PROP_STATUSINFOCOUNT",
    "FR_PROP_BODYPARTSTRING",
    "FR_PROP_STATUS",
    "FR_PROP_STATUSSTRING",
    "FR_PROP_OTHERINFOCHOICE",
    "FR_PROP_FAILINFO",
    "FR_PROP_PENDINFOTOKEN",
    "FR_PROP_PENDINFOTIME",
    "FR_PROP_ISSUEDCERTIFICATEHASH",
    "FR_PROP_ISSUEDCERTIFICATE",
    "FR_PROP_ISSUEDCERTIFICATECHAIN",
    "FR_PROP_ISSUEDCERTIFICATECRLCHAIN",
    "FR_PROP_ENCRYPTEDKEYHASH",
    "FR_PROP_FULLRESPONSENOPKCS7",
    "FR_PROP_CAEXCHANGECERTIFICATEHASH",
    "FR_PROP_CAEXCHANGECERTIFICATE",
    "FR_PROP_CAEXCHANGECERTIFICATECHAIN",
    "FR_PROP_CAEXCHANGECERTIFICATECRLCHAIN",
    "FR_PROP_ATTESTATIONCHALLENGE",
    "FR_PROP_ATTESTATIONPROVIDERNAME",
    "CVRC_COLUMN",
    "CVRC_COLUMN_SCHEMA",
    "CVRC_COLUMN_RESULT",
    "CVRC_COLUMN_VALUE",
    "CVRC_COLUMN_MASK",
    "CERT_IMPORT_FLAGS",
    "CR_IN_BASE64HEADER",
    "CR_IN_BASE64",
    "CR_IN_BINARY",
    "CERT_GET_CONFIG_FLAGS",
    "CC_DEFAULTCONFIG",
    "CC_FIRSTCONFIG",
    "CC_LOCALACTIVECONFIG",
    "CC_LOCALCONFIG",
    "CC_UIPICKCONFIG",
    "CC_UIPICKCONFIGSKIPLOCALCA_",
    "ENUM_CERT_COLUMN_VALUE_FLAGS",
    "CV_OUT_BASE64",
    "CV_OUT_BASE64HEADER",
    "CV_OUT_BASE64REQUESTHEADER",
    "CV_OUT_BASE64X509CRLHEADER",
    "CV_OUT_BINARY",
    "CV_OUT_HEX",
    "CV_OUT_HEXADDR",
    "CV_OUT_HEXASCII",
    "CV_OUT_HEXASCIIADDR",
    "PENDING_REQUEST_DESIRED_PROPERTY",
    "XEPR_CADNS",
    "XEPR_CAFRIENDLYNAME",
    "XEPR_CANAME",
    "XEPR_HASH",
    "XEPR_REQUESTID",
    "CERTADMIN_GET_ROLES_FLAGS",
    "CA_ACCESS_ADMIN",
    "CA_ACCESS_AUDITOR",
    "CA_ACCESS_ENROLL",
    "CA_ACCESS_OFFICER",
    "CA_ACCESS_OPERATOR",
    "CA_ACCESS_READ",
    "CR_DISP",
    "CR_DISP_DENIED",
    "CR_DISP_ERROR",
    "CR_DISP_INCOMPLETE",
    "CR_DISP_ISSUED",
    "CR_DISP_ISSUED_OUT_OF_BAND",
    "CR_DISP_UNDER_SUBMISSION",
    "XEKL_KEYSIZE",
    "XEKL_KEYSIZE_MIN",
    "XEKL_KEYSIZE_MAX",
    "XEKL_KEYSIZE_INC",
    "CERT_CREATE_REQUEST_FLAGS",
    "XECR_CMC",
    "XECR_PKCS10_V1_5",
    "XECR_PKCS10_V2_0",
    "XECR_PKCS7",
    "CERT_EXIT_EVENT_MASK",
    "EXITEVENT_CERTDENIED",
    "EXITEVENT_CERTISSUED",
    "EXITEVENT_CERTPENDING",
    "EXITEVENT_CERTRETRIEVEPENDING",
    "EXITEVENT_CERTREVOKED",
    "EXITEVENT_CRLISSUED",
    "EXITEVENT_SHUTDOWN",
    "ADDED_CERT_TYPE",
    "XECT_EXTENSION_V1",
    "XECT_EXTENSION_V2",
    "CVRC_TABLE",
    "CVRC_TABLE_ATTRIBUTES",
    "CVRC_TABLE_CRL",
    "CVRC_TABLE_EXTENSIONS",
    "CVRC_TABLE_REQCERT",
    "CERT_PROPERTY_TYPE",
    "PROPTYPE_BINARY",
    "PROPTYPE_DATE",
    "PROPTYPE_LONG",
    "PROPTYPE_STRING",
    "CERT_ALT_NAME",
    "CERT_ALT_NAME_RFC822_NAME",
    "CERT_ALT_NAME_DNS_NAME",
    "CERT_ALT_NAME_URL",
    "CERT_ALT_NAME_REGISTERED_ID",
    "CERT_ALT_NAME_DIRECTORY_NAME",
    "CERT_ALT_NAME_IP_ADDRESS",
    "CERT_ALT_NAME_OTHER_NAME",
    "CSBACKUP_TYPE",
    "CSBACKUP_TYPE_FULL",
    "CSBACKUP_TYPE_LOGS_ONLY",
    "XEKL_KEYSPEC",
    "XEKL_KEYSPEC_KEYX",
    "XEKL_KEYSPEC_SIG",
    "CERT_REQUEST_OUT_TYPE",
    "CR_OUT_BASE64HEADER",
    "CR_OUT_BASE64",
    "CR_OUT_BINARY",
    "CERT_VIEW_SEEK_OPERATOR_FLAGS",
    "CVR_SEEK_EQ",
    "CVR_SEEK_LE",
    "CVR_SEEK_LT",
    "CVR_SEEK_GE",
    "CVR_SEEK_GT",
    "CCertAdmin",
    "CCertView",
    "OCSPPropertyCollection",
    "OCSPAdmin",
    "IEnumCERTVIEWCOLUMN",
    "IEnumCERTVIEWATTRIBUTE",
    "IEnumCERTVIEWEXTENSION",
    "IEnumCERTVIEWROW",
    "ICertView",
    "ICertView2",
    "ICertAdmin",
    "ICertAdmin2",
    "IOCSPProperty",
    "IOCSPPropertyCollection",
    "IOCSPCAConfiguration",
    "IOCSPCAConfigurationCollection",
    "IOCSPAdmin",
    "OCSPSigningFlag",
    "OCSP_SF_SILENT",
    "OCSP_SF_USE_CACERT",
    "OCSP_SF_ALLOW_SIGNINGCERT_AUTORENEWAL",
    "OCSP_SF_FORCE_SIGNINGCERT_ISSUER_ISCA",
    "OCSP_SF_AUTODISCOVER_SIGNINGCERT",
    "OCSP_SF_MANUAL_ASSIGN_SIGNINGCERT",
    "OCSP_SF_RESPONDER_ID_KEYHASH",
    "OCSP_SF_RESPONDER_ID_NAME",
    "OCSP_SF_ALLOW_NONCE_EXTENSION",
    "OCSP_SF_ALLOW_SIGNINGCERT_AUTOENROLLMENT",
    "OCSPRequestFlag",
    "OCSP_RF_REJECT_SIGNED_REQUESTS",
    "CSEDB_RSTMAPW",
    "FNCERTSRVISSERVERONLINEW",
    "FNCERTSRVBACKUPGETDYNAMICFILELISTW",
    "FNCERTSRVBACKUPPREPAREW",
    "FNCERTSRVBACKUPGETDATABASENAMESW",
    "FNCERTSRVBACKUPOPENFILEW",
    "FNCERTSRVBACKUPREAD",
    "FNCERTSRVBACKUPCLOSE",
    "FNCERTSRVBACKUPGETBACKUPLOGSW",
    "FNCERTSRVBACKUPTRUNCATELOGS",
    "FNCERTSRVBACKUPEND",
    "FNCERTSRVBACKUPFREE",
    "FNCERTSRVRESTOREGETDATABASELOCATIONSW",
    "FNCERTSRVRESTOREPREPAREW",
    "FNCERTSRVRESTOREREGISTERW",
    "FNCERTSRVRESTOREREGISTERCOMPLETE",
    "FNCERTSRVRESTOREEND",
    "FNCERTSRVSERVERCONTROLW",
    "CCertGetConfig",
    "CCertConfig",
    "CCertRequest",
    "CCertServerPolicy",
    "CCertServerExit",
    "ICertServerPolicy",
    "ICertServerExit",
    "ICertGetConfig",
    "ICertConfig",
    "ICertConfig2",
    "ICertRequest",
    "ICertRequest2",
    "X509EnrollmentAuthFlags",
    "X509EnrollmentAuthFlags_X509AuthNone",
    "X509EnrollmentAuthFlags_X509AuthAnonymous",
    "X509EnrollmentAuthFlags_X509AuthKerberos",
    "X509EnrollmentAuthFlags_X509AuthUsername",
    "X509EnrollmentAuthFlags_X509AuthCertificate",
    "ICertRequest3",
    "CCertEncodeStringArray",
    "CCertEncodeLongArray",
    "CCertEncodeDateArray",
    "CCertEncodeCRLDistInfo",
    "CCertEncodeAltName",
    "CCertEncodeBitString",
    "CObjectId",
    "CObjectIds",
    "CBinaryConverter",
    "CX500DistinguishedName",
    "CCspInformation",
    "CCspInformations",
    "CCspStatus",
    "CX509PublicKey",
    "CX509PrivateKey",
    "CX509EndorsementKey",
    "CX509Extension",
    "CX509Extensions",
    "CX509ExtensionKeyUsage",
    "CX509ExtensionEnhancedKeyUsage",
    "CX509ExtensionTemplateName",
    "CX509ExtensionTemplate",
    "CAlternativeName",
    "CAlternativeNames",
    "CX509ExtensionAlternativeNames",
    "CX509ExtensionBasicConstraints",
    "CX509ExtensionSubjectKeyIdentifier",
    "CX509ExtensionAuthorityKeyIdentifier",
    "CSmimeCapability",
    "CSmimeCapabilities",
    "CX509ExtensionSmimeCapabilities",
    "CPolicyQualifier",
    "CPolicyQualifiers",
    "CCertificatePolicy",
    "CCertificatePolicies",
    "CX509ExtensionCertificatePolicies",
    "CX509ExtensionMSApplicationPolicies",
    "CX509Attribute",
    "CX509Attributes",
    "CX509AttributeExtensions",
    "CX509AttributeClientId",
    "CX509AttributeRenewalCertificate",
    "CX509AttributeArchiveKey",
    "CX509AttributeArchiveKeyHash",
    "CX509AttributeOSVersion",
    "CX509AttributeCspProvider",
    "CCryptAttribute",
    "CCryptAttributes",
    "CCertProperty",
    "CCertProperties",
    "CCertPropertyFriendlyName",
    "CCertPropertyDescription",
    "CCertPropertyAutoEnroll",
    "CCertPropertyRequestOriginator",
    "CCertPropertySHA1Hash",
    "CCertPropertyKeyProvInfo",
    "CCertPropertyArchived",
    "CCertPropertyBackedUp",
    "CCertPropertyEnrollment",
    "CCertPropertyRenewal",
    "CCertPropertyArchivedKeyHash",
    "CCertPropertyEnrollmentPolicyServer",
    "CSignerCertificate",
    "CX509NameValuePair",
    "CCertificateAttestationChallenge",
    "CX509CertificateRequestPkcs10",
    "CX509CertificateRequestCertificate",
    "CX509CertificateRequestPkcs7",
    "CX509CertificateRequestCmc",
    "CX509Enrollment",
    "CX509EnrollmentWebClassFactory",
    "CX509EnrollmentHelper",
    "CX509MachineEnrollmentFactory",
    "CX509EnrollmentPolicyActiveDirectory",
    "CX509EnrollmentPolicyWebService",
    "CX509PolicyServerListManager",
    "CX509PolicyServerUrl",
    "CX509CertificateTemplateADWritable",
    "CX509CertificateRevocationListEntry",
    "CX509CertificateRevocationListEntries",
    "CX509CertificateRevocationList",
    "CX509SCEPEnrollment",
    "CX509SCEPEnrollmentHelper",
    "ICertManageModule",
    "CERTTRANSBLOB",
    "CERTVIEWRESTRICTION",
    "ICertPolicy",
    "ICertPolicy2",
    "X509SCEPMessageType",
    "X509SCEPMessageType_SCEPMessageUnknown",
    "X509SCEPMessageType_SCEPMessageCertResponse",
    "X509SCEPMessageType_SCEPMessagePKCSRequest",
    "X509SCEPMessageType_SCEPMessageGetCertInitial",
    "X509SCEPMessageType_SCEPMessageGetCert",
    "X509SCEPMessageType_SCEPMessageGetCRL",
    "X509SCEPMessageType_SCEPMessageClaimChallengeAnswer",
    "X509SCEPDisposition",
    "X509SCEPDisposition_SCEPDispositionUnknown",
    "X509SCEPDisposition_SCEPDispositionSuccess",
    "X509SCEPDisposition_SCEPDispositionFailure",
    "X509SCEPDisposition_SCEPDispositionPending",
    "X509SCEPDisposition_SCEPDispositionPendingChallenge",
    "X509SCEPFailInfo",
    "X509SCEPFailInfo_SCEPFailUnknown",
    "X509SCEPFailInfo_SCEPFailBadAlgorithm",
    "X509SCEPFailInfo_SCEPFailBadMessageCheck",
    "X509SCEPFailInfo_SCEPFailBadRequest",
    "X509SCEPFailInfo_SCEPFailBadTime",
    "X509SCEPFailInfo_SCEPFailBadCertId",
    "INDESPolicy",
    "CERTENROLL_OBJECTID",
    "XCN_OID_NONE",
    "XCN_OID_RSA",
    "XCN_OID_PKCS",
    "XCN_OID_RSA_HASH",
    "XCN_OID_RSA_ENCRYPT",
    "XCN_OID_PKCS_1",
    "XCN_OID_PKCS_2",
    "XCN_OID_PKCS_3",
    "XCN_OID_PKCS_4",
    "XCN_OID_PKCS_5",
    "XCN_OID_PKCS_6",
    "XCN_OID_PKCS_7",
    "XCN_OID_PKCS_8",
    "XCN_OID_PKCS_9",
    "XCN_OID_PKCS_10",
    "XCN_OID_PKCS_12",
    "XCN_OID_RSA_RSA",
    "XCN_OID_RSA_MD2RSA",
    "XCN_OID_RSA_MD4RSA",
    "XCN_OID_RSA_MD5RSA",
    "XCN_OID_RSA_SHA1RSA",
    "XCN_OID_RSA_SETOAEP_RSA",
    "XCN_OID_RSA_DH",
    "XCN_OID_RSA_data",
    "XCN_OID_RSA_signedData",
    "XCN_OID_RSA_envelopedData",
    "XCN_OID_RSA_signEnvData",
    "XCN_OID_RSA_digestedData",
    "XCN_OID_RSA_hashedData",
    "XCN_OID_RSA_encryptedData",
    "XCN_OID_RSA_emailAddr",
    "XCN_OID_RSA_unstructName",
    "XCN_OID_RSA_contentType",
    "XCN_OID_RSA_messageDigest",
    "XCN_OID_RSA_signingTime",
    "XCN_OID_RSA_counterSign",
    "XCN_OID_RSA_challengePwd",
    "XCN_OID_RSA_unstructAddr",
    "XCN_OID_RSA_extCertAttrs",
    "XCN_OID_RSA_certExtensions",
    "XCN_OID_RSA_SMIMECapabilities",
    "XCN_OID_RSA_preferSignedData",
    "XCN_OID_RSA_SMIMEalg",
    "XCN_OID_RSA_SMIMEalgESDH",
    "XCN_OID_RSA_SMIMEalgCMS3DESwrap",
    "XCN_OID_RSA_SMIMEalgCMSRC2wrap",
    "XCN_OID_RSA_MD2",
    "XCN_OID_RSA_MD4",
    "XCN_OID_RSA_MD5",
    "XCN_OID_RSA_RC2CBC",
    "XCN_OID_RSA_RC4",
    "XCN_OID_RSA_DES_EDE3_CBC",
    "XCN_OID_RSA_RC5_CBCPad",
    "XCN_OID_ANSI_X942",
    "XCN_OID_ANSI_X942_DH",
    "XCN_OID_X957",
    "XCN_OID_X957_DSA",
    "XCN_OID_X957_SHA1DSA",
    "XCN_OID_DS",
    "XCN_OID_DSALG",
    "XCN_OID_DSALG_CRPT",
    "XCN_OID_DSALG_HASH",
    "XCN_OID_DSALG_SIGN",
    "XCN_OID_DSALG_RSA",
    "XCN_OID_OIW",
    "XCN_OID_OIWSEC",
    "XCN_OID_OIWSEC_md4RSA",
    "XCN_OID_OIWSEC_md5RSA",
    "XCN_OID_OIWSEC_md4RSA2",
    "XCN_OID_OIWSEC_desECB",
    "XCN_OID_OIWSEC_desCBC",
    "XCN_OID_OIWSEC_desOFB",
    "XCN_OID_OIWSEC_desCFB",
    "XCN_OID_OIWSEC_desMAC",
    "XCN_OID_OIWSEC_rsaSign",
    "XCN_OID_OIWSEC_dsa",
    "XCN_OID_OIWSEC_shaDSA",
    "XCN_OID_OIWSEC_mdc2RSA",
    "XCN_OID_OIWSEC_shaRSA",
    "XCN_OID_OIWSEC_dhCommMod",
    "XCN_OID_OIWSEC_desEDE",
    "XCN_OID_OIWSEC_sha",
    "XCN_OID_OIWSEC_mdc2",
    "XCN_OID_OIWSEC_dsaComm",
    "XCN_OID_OIWSEC_dsaCommSHA",
    "XCN_OID_OIWSEC_rsaXchg",
    "XCN_OID_OIWSEC_keyHashSeal",
    "XCN_OID_OIWSEC_md2RSASign",
    "XCN_OID_OIWSEC_md5RSASign",
    "XCN_OID_OIWSEC_sha1",
    "XCN_OID_OIWSEC_dsaSHA1",
    "XCN_OID_OIWSEC_dsaCommSHA1",
    "XCN_OID_OIWSEC_sha1RSASign",
    "XCN_OID_OIWDIR",
    "XCN_OID_OIWDIR_CRPT",
    "XCN_OID_OIWDIR_HASH",
    "XCN_OID_OIWDIR_SIGN",
    "XCN_OID_OIWDIR_md2",
    "XCN_OID_OIWDIR_md2RSA",
    "XCN_OID_INFOSEC",
    "XCN_OID_INFOSEC_sdnsSignature",
    "XCN_OID_INFOSEC_mosaicSignature",
    "XCN_OID_INFOSEC_sdnsConfidentiality",
    "XCN_OID_INFOSEC_mosaicConfidentiality",
    "XCN_OID_INFOSEC_sdnsIntegrity",
    "XCN_OID_INFOSEC_mosaicIntegrity",
    "XCN_OID_INFOSEC_sdnsTokenProtection",
    "XCN_OID_INFOSEC_mosaicTokenProtection",
    "XCN_OID_INFOSEC_sdnsKeyManagement",
    "XCN_OID_INFOSEC_mosaicKeyManagement",
    "XCN_OID_INFOSEC_sdnsKMandSig",
    "XCN_OID_INFOSEC_mosaicKMandSig",
    "XCN_OID_INFOSEC_SuiteASignature",
    "XCN_OID_INFOSEC_SuiteAConfidentiality",
    "XCN_OID_INFOSEC_SuiteAIntegrity",
    "XCN_OID_INFOSEC_SuiteATokenProtection",
    "XCN_OID_INFOSEC_SuiteAKeyManagement",
    "XCN_OID_INFOSEC_SuiteAKMandSig",
    "XCN_OID_INFOSEC_mosaicUpdatedSig",
    "XCN_OID_INFOSEC_mosaicKMandUpdSig",
    "XCN_OID_INFOSEC_mosaicUpdatedInteg",
    "XCN_OID_COMMON_NAME",
    "XCN_OID_SUR_NAME",
    "XCN_OID_DEVICE_SERIAL_NUMBER",
    "XCN_OID_COUNTRY_NAME",
    "XCN_OID_LOCALITY_NAME",
    "XCN_OID_STATE_OR_PROVINCE_NAME",
    "XCN_OID_STREET_ADDRESS",
    "XCN_OID_ORGANIZATION_NAME",
    "XCN_OID_ORGANIZATIONAL_UNIT_NAME",
    "XCN_OID_TITLE",
    "XCN_OID_DESCRIPTION",
    "XCN_OID_SEARCH_GUIDE",
    "XCN_OID_BUSINESS_CATEGORY",
    "XCN_OID_POSTAL_ADDRESS",
    "XCN_OID_POSTAL_CODE",
    "XCN_OID_POST_OFFICE_BOX",
    "XCN_OID_PHYSICAL_DELIVERY_OFFICE_NAME",
    "XCN_OID_TELEPHONE_NUMBER",
    "XCN_OID_TELEX_NUMBER",
    "XCN_OID_TELETEXT_TERMINAL_IDENTIFIER",
    "XCN_OID_FACSIMILE_TELEPHONE_NUMBER",
    "XCN_OID_X21_ADDRESS",
    "XCN_OID_INTERNATIONAL_ISDN_NUMBER",
    "XCN_OID_REGISTERED_ADDRESS",
    "XCN_OID_DESTINATION_INDICATOR",
    "XCN_OID_PREFERRED_DELIVERY_METHOD",
    "XCN_OID_PRESENTATION_ADDRESS",
    "XCN_OID_SUPPORTED_APPLICATION_CONTEXT",
    "XCN_OID_MEMBER",
    "XCN_OID_OWNER",
    "XCN_OID_ROLE_OCCUPANT",
    "XCN_OID_SEE_ALSO",
    "XCN_OID_USER_PASSWORD",
    "XCN_OID_USER_CERTIFICATE",
    "XCN_OID_CA_CERTIFICATE",
    "XCN_OID_AUTHORITY_REVOCATION_LIST",
    "XCN_OID_CERTIFICATE_REVOCATION_LIST",
    "XCN_OID_CROSS_CERTIFICATE_PAIR",
    "XCN_OID_GIVEN_NAME",
    "XCN_OID_INITIALS",
    "XCN_OID_DN_QUALIFIER",
    "XCN_OID_DOMAIN_COMPONENT",
    "XCN_OID_PKCS_12_FRIENDLY_NAME_ATTR",
    "XCN_OID_PKCS_12_LOCAL_KEY_ID",
    "XCN_OID_PKCS_12_KEY_PROVIDER_NAME_ATTR",
    "XCN_OID_LOCAL_MACHINE_KEYSET",
    "XCN_OID_PKCS_12_EXTENDED_ATTRIBUTES",
    "XCN_OID_KEYID_RDN",
    "XCN_OID_AUTHORITY_KEY_IDENTIFIER",
    "XCN_OID_KEY_ATTRIBUTES",
    "XCN_OID_CERT_POLICIES_95",
    "XCN_OID_KEY_USAGE_RESTRICTION",
    "XCN_OID_SUBJECT_ALT_NAME",
    "XCN_OID_ISSUER_ALT_NAME",
    "XCN_OID_BASIC_CONSTRAINTS",
    "XCN_OID_KEY_USAGE",
    "XCN_OID_PRIVATEKEY_USAGE_PERIOD",
    "XCN_OID_BASIC_CONSTRAINTS2",
    "XCN_OID_CERT_POLICIES",
    "XCN_OID_ANY_CERT_POLICY",
    "XCN_OID_AUTHORITY_KEY_IDENTIFIER2",
    "XCN_OID_SUBJECT_KEY_IDENTIFIER",
    "XCN_OID_SUBJECT_ALT_NAME2",
    "XCN_OID_ISSUER_ALT_NAME2",
    "XCN_OID_CRL_REASON_CODE",
    "XCN_OID_REASON_CODE_HOLD",
    "XCN_OID_CRL_DIST_POINTS",
    "XCN_OID_ENHANCED_KEY_USAGE",
    "XCN_OID_CRL_NUMBER",
    "XCN_OID_DELTA_CRL_INDICATOR",
    "XCN_OID_ISSUING_DIST_POINT",
    "XCN_OID_FRESHEST_CRL",
    "XCN_OID_NAME_CONSTRAINTS",
    "XCN_OID_POLICY_MAPPINGS",
    "XCN_OID_LEGACY_POLICY_MAPPINGS",
    "XCN_OID_POLICY_CONSTRAINTS",
    "XCN_OID_RENEWAL_CERTIFICATE",
    "XCN_OID_ENROLLMENT_NAME_VALUE_PAIR",
    "XCN_OID_ENROLLMENT_CSP_PROVIDER",
    "XCN_OID_OS_VERSION",
    "XCN_OID_ENROLLMENT_AGENT",
    "XCN_OID_PKIX",
    "XCN_OID_PKIX_PE",
    "XCN_OID_AUTHORITY_INFO_ACCESS",
    "XCN_OID_BIOMETRIC_EXT",
    "XCN_OID_LOGOTYPE_EXT",
    "XCN_OID_CERT_EXTENSIONS",
    "XCN_OID_NEXT_UPDATE_LOCATION",
    "XCN_OID_REMOVE_CERTIFICATE",
    "XCN_OID_CROSS_CERT_DIST_POINTS",
    "XCN_OID_CTL",
    "XCN_OID_SORTED_CTL",
    "XCN_OID_SERIALIZED",
    "XCN_OID_NT_PRINCIPAL_NAME",
    "XCN_OID_PRODUCT_UPDATE",
    "XCN_OID_ANY_APPLICATION_POLICY",
    "XCN_OID_AUTO_ENROLL_CTL_USAGE",
    "XCN_OID_ENROLL_CERTTYPE_EXTENSION",
    "XCN_OID_CERT_MANIFOLD",
    "XCN_OID_CERTSRV_CA_VERSION",
    "XCN_OID_CERTSRV_PREVIOUS_CERT_HASH",
    "XCN_OID_CRL_VIRTUAL_BASE",
    "XCN_OID_CRL_NEXT_PUBLISH",
    "XCN_OID_KP_CA_EXCHANGE",
    "XCN_OID_KP_KEY_RECOVERY_AGENT",
    "XCN_OID_CERTIFICATE_TEMPLATE",
    "XCN_OID_ENTERPRISE_OID_ROOT",
    "XCN_OID_RDN_DUMMY_SIGNER",
    "XCN_OID_APPLICATION_CERT_POLICIES",
    "XCN_OID_APPLICATION_POLICY_MAPPINGS",
    "XCN_OID_APPLICATION_POLICY_CONSTRAINTS",
    "XCN_OID_ARCHIVED_KEY_ATTR",
    "XCN_OID_CRL_SELF_CDP",
    "XCN_OID_REQUIRE_CERT_CHAIN_POLICY",
    "XCN_OID_ARCHIVED_KEY_CERT_HASH",
    "XCN_OID_ISSUED_CERT_HASH",
    "XCN_OID_DS_EMAIL_REPLICATION",
    "XCN_OID_REQUEST_CLIENT_INFO",
    "XCN_OID_ENCRYPTED_KEY_HASH",
    "XCN_OID_CERTSRV_CROSSCA_VERSION",
    "XCN_OID_NTDS_REPLICATION",
    "XCN_OID_SUBJECT_DIR_ATTRS",
    "XCN_OID_PKIX_KP",
    "XCN_OID_PKIX_KP_SERVER_AUTH",
    "XCN_OID_PKIX_KP_CLIENT_AUTH",
    "XCN_OID_PKIX_KP_CODE_SIGNING",
    "XCN_OID_PKIX_KP_EMAIL_PROTECTION",
    "XCN_OID_PKIX_KP_IPSEC_END_SYSTEM",
    "XCN_OID_PKIX_KP_IPSEC_TUNNEL",
    "XCN_OID_PKIX_KP_IPSEC_USER",
    "XCN_OID_PKIX_KP_TIMESTAMP_SIGNING",
    "XCN_OID_PKIX_KP_OCSP_SIGNING",
    "XCN_OID_PKIX_OCSP_NOCHECK",
    "XCN_OID_IPSEC_KP_IKE_INTERMEDIATE",
    "XCN_OID_KP_CTL_USAGE_SIGNING",
    "XCN_OID_KP_TIME_STAMP_SIGNING",
    "XCN_OID_SERVER_GATED_CRYPTO",
    "XCN_OID_SGC_NETSCAPE",
    "XCN_OID_KP_EFS",
    "XCN_OID_EFS_RECOVERY",
    "XCN_OID_WHQL_CRYPTO",
    "XCN_OID_NT5_CRYPTO",
    "XCN_OID_OEM_WHQL_CRYPTO",
    "XCN_OID_EMBEDDED_NT_CRYPTO",
    "XCN_OID_ROOT_LIST_SIGNER",
    "XCN_OID_KP_QUALIFIED_SUBORDINATION",
    "XCN_OID_KP_KEY_RECOVERY",
    "XCN_OID_KP_DOCUMENT_SIGNING",
    "XCN_OID_KP_LIFETIME_SIGNING",
    "XCN_OID_KP_MOBILE_DEVICE_SOFTWARE",
    "XCN_OID_KP_SMART_DISPLAY",
    "XCN_OID_KP_CSP_SIGNATURE",
    "XCN_OID_DRM",
    "XCN_OID_DRM_INDIVIDUALIZATION",
    "XCN_OID_LICENSES",
    "XCN_OID_LICENSE_SERVER",
    "XCN_OID_KP_SMARTCARD_LOGON",
    "XCN_OID_YESNO_TRUST_ATTR",
    "XCN_OID_PKIX_POLICY_QUALIFIER_CPS",
    "XCN_OID_PKIX_POLICY_QUALIFIER_USERNOTICE",
    "XCN_OID_CERT_POLICIES_95_QUALIFIER1",
    "XCN_OID_PKIX_ACC_DESCR",
    "XCN_OID_PKIX_OCSP",
    "XCN_OID_PKIX_CA_ISSUERS",
    "XCN_OID_VERISIGN_PRIVATE_6_9",
    "XCN_OID_VERISIGN_ONSITE_JURISDICTION_HASH",
    "XCN_OID_VERISIGN_BITSTRING_6_13",
    "XCN_OID_VERISIGN_ISS_STRONG_CRYPTO",
    "XCN_OID_NETSCAPE",
    "XCN_OID_NETSCAPE_CERT_EXTENSION",
    "XCN_OID_NETSCAPE_CERT_TYPE",
    "XCN_OID_NETSCAPE_BASE_URL",
    "XCN_OID_NETSCAPE_REVOCATION_URL",
    "XCN_OID_NETSCAPE_CA_REVOCATION_URL",
    "XCN_OID_NETSCAPE_CERT_RENEWAL_URL",
    "XCN_OID_NETSCAPE_CA_POLICY_URL",
    "XCN_OID_NETSCAPE_SSL_SERVER_NAME",
    "XCN_OID_NETSCAPE_COMMENT",
    "XCN_OID_NETSCAPE_DATA_TYPE",
    "XCN_OID_NETSCAPE_CERT_SEQUENCE",
    "XCN_OID_CT_PKI_DATA",
    "XCN_OID_CT_PKI_RESPONSE",
    "XCN_OID_PKIX_NO_SIGNATURE",
    "XCN_OID_CMC",
    "XCN_OID_CMC_STATUS_INFO",
    "XCN_OID_CMC_IDENTIFICATION",
    "XCN_OID_CMC_IDENTITY_PROOF",
    "XCN_OID_CMC_DATA_RETURN",
    "XCN_OID_CMC_TRANSACTION_ID",
    "XCN_OID_CMC_SENDER_NONCE",
    "XCN_OID_CMC_RECIPIENT_NONCE",
    "XCN_OID_CMC_ADD_EXTENSIONS",
    "XCN_OID_CMC_ENCRYPTED_POP",
    "XCN_OID_CMC_DECRYPTED_POP",
    "XCN_OID_CMC_LRA_POP_WITNESS",
    "XCN_OID_CMC_GET_CERT",
    "XCN_OID_CMC_GET_CRL",
    "XCN_OID_CMC_REVOKE_REQUEST",
    "XCN_OID_CMC_REG_INFO",
    "XCN_OID_CMC_RESPONSE_INFO",
    "XCN_OID_CMC_QUERY_PENDING",
    "XCN_OID_CMC_ID_POP_LINK_RANDOM",
    "XCN_OID_CMC_ID_POP_LINK_WITNESS",
    "XCN_OID_CMC_ID_CONFIRM_CERT_ACCEPTANCE",
    "XCN_OID_CMC_ADD_ATTRIBUTES",
    "XCN_OID_LOYALTY_OTHER_LOGOTYPE",
    "XCN_OID_BACKGROUND_OTHER_LOGOTYPE",
    "XCN_OID_PKIX_OCSP_BASIC_SIGNED_RESPONSE",
    "XCN_OID_PKCS_7_DATA",
    "XCN_OID_PKCS_7_SIGNED",
    "XCN_OID_PKCS_7_ENVELOPED",
    "XCN_OID_PKCS_7_SIGNEDANDENVELOPED",
    "XCN_OID_PKCS_7_DIGESTED",
    "XCN_OID_PKCS_7_ENCRYPTED",
    "XCN_OID_PKCS_9_CONTENT_TYPE",
    "XCN_OID_PKCS_9_MESSAGE_DIGEST",
    "XCN_OID_CERT_PROP_ID_PREFIX",
    "XCN_OID_CERT_KEY_IDENTIFIER_PROP_ID",
    "XCN_OID_CERT_ISSUER_SERIAL_NUMBER_MD5_HASH_PROP_ID",
    "XCN_OID_CERT_SUBJECT_NAME_MD5_HASH_PROP_ID",
    "XCN_OID_CERT_MD5_HASH_PROP_ID",
    "XCN_OID_RSA_SHA256RSA",
    "XCN_OID_RSA_SHA384RSA",
    "XCN_OID_RSA_SHA512RSA",
    "XCN_OID_NIST_sha256",
    "XCN_OID_NIST_sha384",
    "XCN_OID_NIST_sha512",
    "XCN_OID_RSA_MGF1",
    "XCN_OID_ECC_PUBLIC_KEY",
    "XCN_OID_ECDSA_SHA1",
    "XCN_OID_ECDSA_SPECIFIED",
    "XCN_OID_ANY_ENHANCED_KEY_USAGE",
    "XCN_OID_RSA_SSA_PSS",
    "XCN_OID_ATTR_SUPPORTED_ALGORITHMS",
    "XCN_OID_ATTR_TPM_SECURITY_ASSERTIONS",
    "XCN_OID_ATTR_TPM_SPECIFICATION",
    "XCN_OID_CERT_DISALLOWED_FILETIME_PROP_ID",
    "XCN_OID_CERT_SIGNATURE_HASH_PROP_ID",
    "XCN_OID_CERT_STRONG_KEY_OS_1",
    "XCN_OID_CERT_STRONG_KEY_OS_CURRENT",
    "XCN_OID_CERT_STRONG_KEY_OS_PREFIX",
    "XCN_OID_CERT_STRONG_SIGN_OS_1",
    "XCN_OID_CERT_STRONG_SIGN_OS_CURRENT",
    "XCN_OID_CERT_STRONG_SIGN_OS_PREFIX",
    "XCN_OID_DH_SINGLE_PASS_STDDH_SHA1_KDF",
    "XCN_OID_DH_SINGLE_PASS_STDDH_SHA256_KDF",
    "XCN_OID_DH_SINGLE_PASS_STDDH_SHA384_KDF",
    "XCN_OID_DISALLOWED_HASH",
    "XCN_OID_DISALLOWED_LIST",
    "XCN_OID_ECC_CURVE_P256",
    "XCN_OID_ECC_CURVE_P384",
    "XCN_OID_ECC_CURVE_P521",
    "XCN_OID_ECDSA_SHA256",
    "XCN_OID_ECDSA_SHA384",
    "XCN_OID_ECDSA_SHA512",
    "XCN_OID_ENROLL_CAXCHGCERT_HASH",
    "XCN_OID_ENROLL_EK_INFO",
    "XCN_OID_ENROLL_EKPUB_CHALLENGE",
    "XCN_OID_ENROLL_EKVERIFYCERT",
    "XCN_OID_ENROLL_EKVERIFYCREDS",
    "XCN_OID_ENROLL_EKVERIFYKEY",
    "XCN_OID_EV_RDN_COUNTRY",
    "XCN_OID_EV_RDN_LOCALE",
    "XCN_OID_EV_RDN_STATE_OR_PROVINCE",
    "XCN_OID_INHIBIT_ANY_POLICY",
    "XCN_OID_INTERNATIONALIZED_EMAIL_ADDRESS",
    "XCN_OID_KP_KERNEL_MODE_CODE_SIGNING",
    "XCN_OID_KP_KERNEL_MODE_HAL_EXTENSION_SIGNING",
    "XCN_OID_KP_KERNEL_MODE_TRUSTED_BOOT_SIGNING",
    "XCN_OID_KP_TPM_AIK_CERTIFICATE",
    "XCN_OID_KP_TPM_EK_CERTIFICATE",
    "XCN_OID_KP_TPM_PLATFORM_CERTIFICATE",
    "XCN_OID_NIST_AES128_CBC",
    "XCN_OID_NIST_AES128_WRAP",
    "XCN_OID_NIST_AES192_CBC",
    "XCN_OID_NIST_AES192_WRAP",
    "XCN_OID_NIST_AES256_CBC",
    "XCN_OID_NIST_AES256_WRAP",
    "XCN_OID_PKCS_12_PbeIds",
    "XCN_OID_PKCS_12_pbeWithSHA1And128BitRC2",
    "XCN_OID_PKCS_12_pbeWithSHA1And128BitRC4",
    "XCN_OID_PKCS_12_pbeWithSHA1And2KeyTripleDES",
    "XCN_OID_PKCS_12_pbeWithSHA1And3KeyTripleDES",
    "XCN_OID_PKCS_12_pbeWithSHA1And40BitRC2",
    "XCN_OID_PKCS_12_pbeWithSHA1And40BitRC4",
    "XCN_OID_PKCS_12_PROTECTED_PASSWORD_SECRET_BAG_TYPE_ID",
    "XCN_OID_PKINIT_KP_KDC",
    "XCN_OID_PKIX_CA_REPOSITORY",
    "XCN_OID_PKIX_OCSP_NONCE",
    "XCN_OID_PKIX_TIME_STAMPING",
    "XCN_OID_QC_EU_COMPLIANCE",
    "XCN_OID_QC_SSCD",
    "XCN_OID_QC_STATEMENTS_EXT",
    "XCN_OID_RDN_TPM_MANUFACTURER",
    "XCN_OID_RDN_TPM_MODEL",
    "XCN_OID_RDN_TPM_VERSION",
    "XCN_OID_REVOKED_LIST_SIGNER",
    "XCN_OID_RFC3161_counterSign",
    "XCN_OID_ROOT_PROGRAM_AUTO_UPDATE_CA_REVOCATION",
    "XCN_OID_ROOT_PROGRAM_AUTO_UPDATE_END_REVOCATION",
    "XCN_OID_ROOT_PROGRAM_FLAGS",
    "XCN_OID_ROOT_PROGRAM_NO_OCSP_FAILOVER_TO_CRL",
    "XCN_OID_RSA_PSPECIFIED",
    "XCN_OID_RSAES_OAEP",
    "XCN_OID_SUBJECT_INFO_ACCESS",
    "XCN_OID_TIMESTAMP_TOKEN",
    "XCN_OID_ENROLL_SCEP_ERROR",
    "XCN_OIDVerisign_MessageType",
    "XCN_OIDVerisign_PkiStatus",
    "XCN_OIDVerisign_FailInfo",
    "XCN_OIDVerisign_SenderNonce",
    "XCN_OIDVerisign_RecipientNonce",
    "XCN_OIDVerisign_TransactionID",
    "XCN_OID_ENROLL_ATTESTATION_CHALLENGE",
    "XCN_OID_ENROLL_ATTESTATION_STATEMENT",
    "XCN_OID_ENROLL_ENCRYPTION_ALGORITHM",
    "XCN_OID_ENROLL_KSP_NAME",
    "WebSecurityLevel",
    "WebSecurityLevel_LevelUnsafe",
    "WebSecurityLevel_LevelSafe",
    "EncodingType",
    "XCN_CRYPT_STRING_BASE64HEADER",
    "XCN_CRYPT_STRING_BASE64",
    "XCN_CRYPT_STRING_BINARY",
    "XCN_CRYPT_STRING_BASE64REQUESTHEADER",
    "XCN_CRYPT_STRING_HEX",
    "XCN_CRYPT_STRING_HEXASCII",
    "XCN_CRYPT_STRING_BASE64_ANY",
    "XCN_CRYPT_STRING_ANY",
    "XCN_CRYPT_STRING_HEX_ANY",
    "XCN_CRYPT_STRING_BASE64X509CRLHEADER",
    "XCN_CRYPT_STRING_HEXADDR",
    "XCN_CRYPT_STRING_HEXASCIIADDR",
    "XCN_CRYPT_STRING_HEXRAW",
    "XCN_CRYPT_STRING_BASE64URI",
    "XCN_CRYPT_STRING_ENCODEMASK",
    "XCN_CRYPT_STRING_CHAIN",
    "XCN_CRYPT_STRING_TEXT",
    "XCN_CRYPT_STRING_PERCENTESCAPE",
    "XCN_CRYPT_STRING_HASHDATA",
    "XCN_CRYPT_STRING_STRICT",
    "XCN_CRYPT_STRING_NOCRLF",
    "XCN_CRYPT_STRING_NOCR",
    "PFXExportOptions",
    "PFXExportOptions_PFXExportEEOnly",
    "PFXExportOptions_PFXExportChainNoRoot",
    "PFXExportOptions_PFXExportChainWithRoot",
    "ObjectIdGroupId",
    "XCN_CRYPT_ANY_GROUP_ID",
    "XCN_CRYPT_HASH_ALG_OID_GROUP_ID",
    "XCN_CRYPT_ENCRYPT_ALG_OID_GROUP_ID",
    "XCN_CRYPT_PUBKEY_ALG_OID_GROUP_ID",
    "XCN_CRYPT_SIGN_ALG_OID_GROUP_ID",
    "XCN_CRYPT_RDN_ATTR_OID_GROUP_ID",
    "XCN_CRYPT_EXT_OR_ATTR_OID_GROUP_ID",
    "XCN_CRYPT_ENHKEY_USAGE_OID_GROUP_ID",
    "XCN_CRYPT_POLICY_OID_GROUP_ID",
    "XCN_CRYPT_TEMPLATE_OID_GROUP_ID",
    "XCN_CRYPT_KDF_OID_GROUP_ID",
    "XCN_CRYPT_LAST_OID_GROUP_ID",
    "XCN_CRYPT_FIRST_ALG_OID_GROUP_ID",
    "XCN_CRYPT_LAST_ALG_OID_GROUP_ID",
    "XCN_CRYPT_GROUP_ID_MASK",
    "XCN_CRYPT_OID_PREFER_CNG_ALGID_FLAG",
    "XCN_CRYPT_OID_DISABLE_SEARCH_DS_FLAG",
    "XCN_CRYPT_OID_INFO_OID_GROUP_BIT_LEN_MASK",
    "XCN_CRYPT_OID_INFO_OID_GROUP_BIT_LEN_SHIFT",
    "XCN_CRYPT_KEY_LENGTH_MASK",
    "ObjectIdPublicKeyFlags",
    "XCN_CRYPT_OID_INFO_PUBKEY_ANY",
    "XCN_CRYPT_OID_INFO_PUBKEY_SIGN_KEY_FLAG",
    "XCN_CRYPT_OID_INFO_PUBKEY_ENCRYPT_KEY_FLAG",
    "AlgorithmFlags",
    "AlgorithmFlags_AlgorithmFlagsNone",
    "AlgorithmFlags_AlgorithmFlagsWrap",
    "IObjectId",
    "IObjectIds",
    "IBinaryConverter",
    "IBinaryConverter2",
    "X500NameFlags",
    "XCN_CERT_NAME_STR_NONE",
    "XCN_CERT_SIMPLE_NAME_STR",
    "XCN_CERT_OID_NAME_STR",
    "XCN_CERT_X500_NAME_STR",
    "XCN_CERT_XML_NAME_STR",
    "XCN_CERT_NAME_STR_SEMICOLON_FLAG",
    "XCN_CERT_NAME_STR_NO_PLUS_FLAG",
    "XCN_CERT_NAME_STR_NO_QUOTING_FLAG",
    "XCN_CERT_NAME_STR_CRLF_FLAG",
    "XCN_CERT_NAME_STR_COMMA_FLAG",
    "XCN_CERT_NAME_STR_REVERSE_FLAG",
    "XCN_CERT_NAME_STR_FORWARD_FLAG",
    "XCN_CERT_NAME_STR_AMBIGUOUS_SEPARATOR_FLAGS",
    "XCN_CERT_NAME_STR_DISABLE_IE4_UTF8_FLAG",
    "XCN_CERT_NAME_STR_ENABLE_T61_UNICODE_FLAG",
    "XCN_CERT_NAME_STR_ENABLE_UTF8_UNICODE_FLAG",
    "XCN_CERT_NAME_STR_FORCE_UTF8_DIR_STR_FLAG",
    "XCN_CERT_NAME_STR_DISABLE_UTF8_DIR_STR_FLAG",
    "XCN_CERT_NAME_STR_ENABLE_PUNYCODE_FLAG",
    "XCN_CERT_NAME_STR_DS_ESCAPED",
    "IX500DistinguishedName",
    "X509CertificateEnrollmentContext",
    "X509CertificateEnrollmentContext_ContextNone",
    "X509CertificateEnrollmentContext_ContextUser",
    "X509CertificateEnrollmentContext_ContextMachine",
    "X509CertificateEnrollmentContext_ContextAdministratorForceMachine",
    "EnrollmentEnrollStatus",
    "EnrollmentEnrollStatus_Enrolled",
    "EnrollmentEnrollStatus_EnrollPended",
    "EnrollmentEnrollStatus_EnrollUIDeferredEnrollmentRequired",
    "EnrollmentEnrollStatus_EnrollError",
    "EnrollmentEnrollStatus_EnrollUnknown",
    "EnrollmentEnrollStatus_EnrollSkipped",
    "EnrollmentEnrollStatus_EnrollDenied",
    "EnrollmentSelectionStatus",
    "EnrollmentSelectionStatus_SelectedNo",
    "EnrollmentSelectionStatus_SelectedYes",
    "EnrollmentDisplayStatus",
    "EnrollmentDisplayStatus_DisplayNo",
    "EnrollmentDisplayStatus_DisplayYes",
    "IX509EnrollmentStatus",
    "X509ProviderType",
    "XCN_PROV_NONE",
    "XCN_PROV_RSA_FULL",
    "XCN_PROV_RSA_SIG",
    "XCN_PROV_DSS",
    "XCN_PROV_FORTEZZA",
    "XCN_PROV_MS_EXCHANGE",
    "XCN_PROV_SSL",
    "XCN_PROV_RSA_SCHANNEL",
    "XCN_PROV_DSS_DH",
    "XCN_PROV_EC_ECDSA_SIG",
    "XCN_PROV_EC_ECNRA_SIG",
    "XCN_PROV_EC_ECDSA_FULL",
    "XCN_PROV_EC_ECNRA_FULL",
    "XCN_PROV_DH_SCHANNEL",
    "XCN_PROV_SPYRUS_LYNKS",
    "XCN_PROV_RNG",
    "XCN_PROV_INTEL_SEC",
    "XCN_PROV_REPLACE_OWF",
    "XCN_PROV_RSA_AES",
    "AlgorithmType",
    "XCN_BCRYPT_UNKNOWN_INTERFACE",
    "XCN_BCRYPT_CIPHER_INTERFACE",
    "XCN_BCRYPT_HASH_INTERFACE",
    "XCN_BCRYPT_ASYMMETRIC_ENCRYPTION_INTERFACE",
    "XCN_BCRYPT_SIGNATURE_INTERFACE",
    "XCN_BCRYPT_SECRET_AGREEMENT_INTERFACE",
    "XCN_BCRYPT_RNG_INTERFACE",
    "XCN_BCRYPT_KEY_DERIVATION_INTERFACE",
    "AlgorithmOperationFlags",
    "XCN_NCRYPT_NO_OPERATION",
    "XCN_NCRYPT_CIPHER_OPERATION",
    "XCN_NCRYPT_HASH_OPERATION",
    "XCN_NCRYPT_ASYMMETRIC_ENCRYPTION_OPERATION",
    "XCN_NCRYPT_SECRET_AGREEMENT_OPERATION",
    "XCN_NCRYPT_SIGNATURE_OPERATION",
    "XCN_NCRYPT_RNG_OPERATION",
    "XCN_NCRYPT_KEY_DERIVATION_OPERATION",
    "XCN_NCRYPT_ANY_ASYMMETRIC_OPERATION",
    "XCN_NCRYPT_PREFER_SIGNATURE_ONLY_OPERATION",
    "XCN_NCRYPT_PREFER_NON_SIGNATURE_OPERATION",
    "XCN_NCRYPT_EXACT_MATCH_OPERATION",
    "XCN_NCRYPT_PREFERENCE_MASK_OPERATION",
    "ICspAlgorithm",
    "ICspAlgorithms",
    "X509KeySpec",
    "XCN_AT_NONE",
    "XCN_AT_KEYEXCHANGE",
    "XCN_AT_SIGNATURE",
    "ICspInformation",
    "ICspInformations",
    "ICspStatus",
    "ICspStatuses",
    "KeyIdentifierHashAlgorithm",
    "KeyIdentifierHashAlgorithm_SKIHashDefault",
    "KeyIdentifierHashAlgorithm_SKIHashSha1",
    "KeyIdentifierHashAlgorithm_SKIHashCapiSha1",
    "KeyIdentifierHashAlgorithm_SKIHashSha256",
    "KeyIdentifierHashAlgorithm_SKIHashHPKP",
    "IX509PublicKey",
    "X509PrivateKeyExportFlags",
    "XCN_NCRYPT_ALLOW_EXPORT_NONE",
    "XCN_NCRYPT_ALLOW_EXPORT_FLAG",
    "XCN_NCRYPT_ALLOW_PLAINTEXT_EXPORT_FLAG",
    "XCN_NCRYPT_ALLOW_ARCHIVING_FLAG",
    "XCN_NCRYPT_ALLOW_PLAINTEXT_ARCHIVING_FLAG",
    "X509PrivateKeyUsageFlags",
    "XCN_NCRYPT_ALLOW_USAGES_NONE",
    "XCN_NCRYPT_ALLOW_DECRYPT_FLAG",
    "XCN_NCRYPT_ALLOW_SIGNING_FLAG",
    "XCN_NCRYPT_ALLOW_KEY_AGREEMENT_FLAG",
    "XCN_NCRYPT_ALLOW_KEY_IMPORT_FLAG",
    "XCN_NCRYPT_ALLOW_ALL_USAGES",
    "X509PrivateKeyProtection",
    "XCN_NCRYPT_UI_NO_PROTECTION_FLAG",
    "XCN_NCRYPT_UI_PROTECT_KEY_FLAG",
    "XCN_NCRYPT_UI_FORCE_HIGH_PROTECTION_FLAG",
    "XCN_NCRYPT_UI_FINGERPRINT_PROTECTION_FLAG",
    "XCN_NCRYPT_UI_APPCONTAINER_ACCESS_MEDIUM_FLAG",
    "X509PrivateKeyVerify",
    "X509PrivateKeyVerify_VerifyNone",
    "X509PrivateKeyVerify_VerifySilent",
    "X509PrivateKeyVerify_VerifySmartCardNone",
    "X509PrivateKeyVerify_VerifySmartCardSilent",
    "X509PrivateKeyVerify_VerifyAllowUI",
    "IX509PrivateKey",
    "X509HardwareKeyUsageFlags",
    "XCN_NCRYPT_PCP_NONE",
    "XCN_NCRYPT_TPM12_PROVIDER",
    "XCN_NCRYPT_PCP_SIGNATURE_KEY",
    "XCN_NCRYPT_PCP_ENCRYPTION_KEY",
    "XCN_NCRYPT_PCP_GENERIC_KEY",
    "XCN_NCRYPT_PCP_STORAGE_KEY",
    "XCN_NCRYPT_PCP_IDENTITY_KEY",
    "X509KeyParametersExportType",
    "XCN_CRYPT_OID_USE_CURVE_NONE",
    "XCN_CRYPT_OID_USE_CURVE_NAME_FOR_ENCODE_FLAG",
    "XCN_CRYPT_OID_USE_CURVE_PARAMETERS_FOR_ENCODE_FLAG",
    "IX509PrivateKey2",
    "IX509EndorsementKey",
    "IX509Extension",
    "IX509Extensions",
    "X509KeyUsageFlags",
    "XCN_CERT_NO_KEY_USAGE",
    "XCN_CERT_DIGITAL_SIGNATURE_KEY_USAGE",
    "XCN_CERT_NON_REPUDIATION_KEY_USAGE",
    "XCN_CERT_KEY_ENCIPHERMENT_KEY_USAGE",
    "XCN_CERT_DATA_ENCIPHERMENT_KEY_USAGE",
    "XCN_CERT_KEY_AGREEMENT_KEY_USAGE",
    "XCN_CERT_KEY_CERT_SIGN_KEY_USAGE",
    "XCN_CERT_OFFLINE_CRL_SIGN_KEY_USAGE",
    "XCN_CERT_CRL_SIGN_KEY_USAGE",
    "XCN_CERT_ENCIPHER_ONLY_KEY_USAGE",
    "XCN_CERT_DECIPHER_ONLY_KEY_USAGE",
    "IX509ExtensionKeyUsage",
    "IX509ExtensionEnhancedKeyUsage",
    "IX509ExtensionTemplateName",
    "IX509ExtensionTemplate",
    "AlternativeNameType",
    "XCN_CERT_ALT_NAME_UNKNOWN",
    "XCN_CERT_ALT_NAME_OTHER_NAME",
    "XCN_CERT_ALT_NAME_RFC822_NAME",
    "XCN_CERT_ALT_NAME_DNS_NAME",
    "XCN_CERT_ALT_NAME_X400_ADDRESS",
    "XCN_CERT_ALT_NAME_DIRECTORY_NAME",
    "XCN_CERT_ALT_NAME_EDI_PARTY_NAME",
    "XCN_CERT_ALT_NAME_URL",
    "XCN_CERT_ALT_NAME_IP_ADDRESS",
    "XCN_CERT_ALT_NAME_REGISTERED_ID",
    "XCN_CERT_ALT_NAME_GUID",
    "XCN_CERT_ALT_NAME_USER_PRINCIPLE_NAME",
    "IAlternativeName",
    "IAlternativeNames",
    "IX509ExtensionAlternativeNames",
    "IX509ExtensionBasicConstraints",
    "IX509ExtensionSubjectKeyIdentifier",
    "IX509ExtensionAuthorityKeyIdentifier",
    "ISmimeCapability",
    "ISmimeCapabilities",
    "IX509ExtensionSmimeCapabilities",
    "PolicyQualifierType",
    "PolicyQualifierType_PolicyQualifierTypeUnknown",
    "PolicyQualifierType_PolicyQualifierTypeUrl",
    "PolicyQualifierType_PolicyQualifierTypeUserNotice",
    "PolicyQualifierType_PolicyQualifierTypeFlags",
    "IPolicyQualifier",
    "IPolicyQualifiers",
    "ICertificatePolicy",
    "ICertificatePolicies",
    "IX509ExtensionCertificatePolicies",
    "IX509ExtensionMSApplicationPolicies",
    "IX509Attribute",
    "IX509Attributes",
    "IX509AttributeExtensions",
    "RequestClientInfoClientId",
    "RequestClientInfoClientId_ClientIdNone",
    "RequestClientInfoClientId_ClientIdXEnroll2003",
    "RequestClientInfoClientId_ClientIdAutoEnroll2003",
    "RequestClientInfoClientId_ClientIdWizard2003",
    "RequestClientInfoClientId_ClientIdCertReq2003",
    "RequestClientInfoClientId_ClientIdDefaultRequest",
    "RequestClientInfoClientId_ClientIdAutoEnroll",
    "RequestClientInfoClientId_ClientIdRequestWizard",
    "RequestClientInfoClientId_ClientIdEOBO",
    "RequestClientInfoClientId_ClientIdCertReq",
    "RequestClientInfoClientId_ClientIdTest",
    "RequestClientInfoClientId_ClientIdWinRT",
    "RequestClientInfoClientId_ClientIdUserStart",
    "IX509AttributeClientId",
    "IX509AttributeRenewalCertificate",
    "IX509AttributeArchiveKey",
    "IX509AttributeArchiveKeyHash",
    "IX509AttributeOSVersion",
    "IX509AttributeCspProvider",
    "ICryptAttribute",
    "ICryptAttributes",
    "CERTENROLL_PROPERTYID",
    "XCN_PROPERTYID_NONE",
    "XCN_CERT_KEY_PROV_HANDLE_PROP_ID",
    "XCN_CERT_KEY_PROV_INFO_PROP_ID",
    "XCN_CERT_SHA1_HASH_PROP_ID",
    "XCN_CERT_MD5_HASH_PROP_ID",
    "XCN_CERT_HASH_PROP_ID",
    "XCN_CERT_KEY_CONTEXT_PROP_ID",
    "XCN_CERT_KEY_SPEC_PROP_ID",
    "XCN_CERT_IE30_RESERVED_PROP_ID",
    "XCN_CERT_PUBKEY_HASH_RESERVED_PROP_ID",
    "XCN_CERT_ENHKEY_USAGE_PROP_ID",
    "XCN_CERT_CTL_USAGE_PROP_ID",
    "XCN_CERT_NEXT_UPDATE_LOCATION_PROP_ID",
    "XCN_CERT_FRIENDLY_NAME_PROP_ID",
    "XCN_CERT_PVK_FILE_PROP_ID",
    "XCN_CERT_DESCRIPTION_PROP_ID",
    "XCN_CERT_ACCESS_STATE_PROP_ID",
    "XCN_CERT_SIGNATURE_HASH_PROP_ID",
    "XCN_CERT_SMART_CARD_DATA_PROP_ID",
    "XCN_CERT_EFS_PROP_ID",
    "XCN_CERT_FORTEZZA_DATA_PROP_ID",
    "XCN_CERT_ARCHIVED_PROP_ID",
    "XCN_CERT_KEY_IDENTIFIER_PROP_ID",
    "XCN_CERT_AUTO_ENROLL_PROP_ID",
    "XCN_CERT_PUBKEY_ALG_PARA_PROP_ID",
    "XCN_CERT_CROSS_CERT_DIST_POINTS_PROP_ID",
    "XCN_CERT_ISSUER_PUBLIC_KEY_MD5_HASH_PROP_ID",
    "XCN_CERT_SUBJECT_PUBLIC_KEY_MD5_HASH_PROP_ID",
    "XCN_CERT_ENROLLMENT_PROP_ID",
    "XCN_CERT_DATE_STAMP_PROP_ID",
    "XCN_CERT_ISSUER_SERIAL_NUMBER_MD5_HASH_PROP_ID",
    "XCN_CERT_SUBJECT_NAME_MD5_HASH_PROP_ID",
    "XCN_CERT_EXTENDED_ERROR_INFO_PROP_ID",
    "XCN_CERT_RENEWAL_PROP_ID",
    "XCN_CERT_ARCHIVED_KEY_HASH_PROP_ID",
    "XCN_CERT_AUTO_ENROLL_RETRY_PROP_ID",
    "XCN_CERT_AIA_URL_RETRIEVED_PROP_ID",
    "XCN_CERT_AUTHORITY_INFO_ACCESS_PROP_ID",
    "XCN_CERT_BACKED_UP_PROP_ID",
    "XCN_CERT_OCSP_RESPONSE_PROP_ID",
    "XCN_CERT_REQUEST_ORIGINATOR_PROP_ID",
    "XCN_CERT_SOURCE_LOCATION_PROP_ID",
    "XCN_CERT_SOURCE_URL_PROP_ID",
    "XCN_CERT_NEW_KEY_PROP_ID",
    "XCN_CERT_OCSP_CACHE_PREFIX_PROP_ID",
    "XCN_CERT_SMART_CARD_ROOT_INFO_PROP_ID",
    "XCN_CERT_NO_AUTO_EXPIRE_CHECK_PROP_ID",
    "XCN_CERT_NCRYPT_KEY_HANDLE_PROP_ID",
    "XCN_CERT_HCRYPTPROV_OR_NCRYPT_KEY_HANDLE_PROP_ID",
    "XCN_CERT_SUBJECT_INFO_ACCESS_PROP_ID",
    "XCN_CERT_CA_OCSP_AUTHORITY_INFO_ACCESS_PROP_ID",
    "XCN_CERT_CA_DISABLE_CRL_PROP_ID",
    "XCN_CERT_ROOT_PROGRAM_CERT_POLICIES_PROP_ID",
    "XCN_CERT_ROOT_PROGRAM_NAME_CONSTRAINTS_PROP_ID",
    "XCN_CERT_SUBJECT_OCSP_AUTHORITY_INFO_ACCESS_PROP_ID",
    "XCN_CERT_SUBJECT_DISABLE_CRL_PROP_ID",
    "XCN_CERT_CEP_PROP_ID",
    "XCN_CERT_SIGN_HASH_CNG_ALG_PROP_ID",
    "XCN_CERT_SCARD_PIN_ID_PROP_ID",
    "XCN_CERT_SCARD_PIN_INFO_PROP_ID",
    "XCN_CERT_SUBJECT_PUB_KEY_BIT_LENGTH_PROP_ID",
    "XCN_CERT_PUB_KEY_CNG_ALG_BIT_LENGTH_PROP_ID",
    "XCN_CERT_ISSUER_PUB_KEY_BIT_LENGTH_PROP_ID",
    "XCN_CERT_ISSUER_CHAIN_SIGN_HASH_CNG_ALG_PROP_ID",
    "XCN_CERT_ISSUER_CHAIN_PUB_KEY_CNG_ALG_BIT_LENGTH_PROP_ID",
    "XCN_CERT_NO_EXPIRE_NOTIFICATION_PROP_ID",
    "XCN_CERT_AUTH_ROOT_SHA256_HASH_PROP_ID",
    "XCN_CERT_NCRYPT_KEY_HANDLE_TRANSFER_PROP_ID",
    "XCN_CERT_HCRYPTPROV_TRANSFER_PROP_ID",
    "XCN_CERT_SMART_CARD_READER_PROP_ID",
    "XCN_CERT_SEND_AS_TRUSTED_ISSUER_PROP_ID",
    "XCN_CERT_KEY_REPAIR_ATTEMPTED_PROP_ID",
    "XCN_CERT_DISALLOWED_FILETIME_PROP_ID",
    "XCN_CERT_ROOT_PROGRAM_CHAIN_POLICIES_PROP_ID",
    "XCN_CERT_SMART_CARD_READER_NON_REMOVABLE_PROP_ID",
    "XCN_CERT_SHA256_HASH_PROP_ID",
    "XCN_CERT_SCEP_SERVER_CERTS_PROP_ID",
    "XCN_CERT_SCEP_RA_SIGNATURE_CERT_PROP_ID",
    "XCN_CERT_SCEP_RA_ENCRYPTION_CERT_PROP_ID",
    "XCN_CERT_SCEP_CA_CERT_PROP_ID",
    "XCN_CERT_SCEP_SIGNER_CERT_PROP_ID",
    "XCN_CERT_SCEP_NONCE_PROP_ID",
    "XCN_CERT_SCEP_ENCRYPT_HASH_CNG_ALG_PROP_ID",
    "XCN_CERT_SCEP_FLAGS_PROP_ID",
    "XCN_CERT_SCEP_GUID_PROP_ID",
    "XCN_CERT_SERIALIZABLE_KEY_CONTEXT_PROP_ID",
    "XCN_CERT_ISOLATED_KEY_PROP_ID",
    "XCN_CERT_SERIAL_CHAIN_PROP_ID",
    "XCN_CERT_KEY_CLASSIFICATION_PROP_ID",
    "XCN_CERT_DISALLOWED_ENHKEY_USAGE_PROP_ID",
    "XCN_CERT_NONCOMPLIANT_ROOT_URL_PROP_ID",
    "XCN_CERT_PIN_SHA256_HASH_PROP_ID",
    "XCN_CERT_CLR_DELETE_KEY_PROP_ID",
    "XCN_CERT_NOT_BEFORE_FILETIME_PROP_ID",
    "XCN_CERT_CERT_NOT_BEFORE_ENHKEY_USAGE_PROP_ID",
    "XCN_CERT_FIRST_RESERVED_PROP_ID",
    "XCN_CERT_LAST_RESERVED_PROP_ID",
    "XCN_CERT_FIRST_USER_PROP_ID",
    "XCN_CERT_LAST_USER_PROP_ID",
    "XCN_CERT_STORE_LOCALIZED_NAME_PROP_ID",
    "ICertProperty",
    "ICertProperties",
    "ICertPropertyFriendlyName",
    "ICertPropertyDescription",
    "ICertPropertyAutoEnroll",
    "ICertPropertyRequestOriginator",
    "ICertPropertySHA1Hash",
    "ICertPropertyKeyProvInfo",
    "ICertPropertyArchived",
    "ICertPropertyBackedUp",
    "ICertPropertyEnrollment",
    "ICertPropertyRenewal",
    "ICertPropertyArchivedKeyHash",
    "EnrollmentPolicyServerPropertyFlags",
    "EnrollmentPolicyServerPropertyFlags_DefaultNone",
    "EnrollmentPolicyServerPropertyFlags_DefaultPolicyServer",
    "PolicyServerUrlFlags",
    "PolicyServerUrlFlags_PsfNone",
    "PolicyServerUrlFlags_PsfLocationGroupPolicy",
    "PolicyServerUrlFlags_PsfLocationRegistry",
    "PolicyServerUrlFlags_PsfUseClientId",
    "PolicyServerUrlFlags_PsfAutoEnrollmentEnabled",
    "PolicyServerUrlFlags_PsfAllowUnTrustedCA",
    "ICertPropertyEnrollmentPolicyServer",
    "IX509SignatureInformation",
    "ISignerCertificate",
    "ISignerCertificates",
    "IX509NameValuePair",
    "IX509NameValuePairs",
    "EnrollmentTemplateProperty",
    "EnrollmentTemplateProperty_TemplatePropCommonName",
    "EnrollmentTemplateProperty_TemplatePropFriendlyName",
    "EnrollmentTemplateProperty_TemplatePropEKUs",
    "EnrollmentTemplateProperty_TemplatePropCryptoProviders",
    "EnrollmentTemplateProperty_TemplatePropMajorRevision",
    "EnrollmentTemplateProperty_TemplatePropDescription",
    "EnrollmentTemplateProperty_TemplatePropKeySpec",
    "EnrollmentTemplateProperty_TemplatePropSchemaVersion",
    "EnrollmentTemplateProperty_TemplatePropMinorRevision",
    "EnrollmentTemplateProperty_TemplatePropRASignatureCount",
    "EnrollmentTemplateProperty_TemplatePropMinimumKeySize",
    "EnrollmentTemplateProperty_TemplatePropOID",
    "EnrollmentTemplateProperty_TemplatePropSupersede",
    "EnrollmentTemplateProperty_TemplatePropRACertificatePolicies",
    "EnrollmentTemplateProperty_TemplatePropRAEKUs",
    "EnrollmentTemplateProperty_TemplatePropCertificatePolicies",
    "EnrollmentTemplateProperty_TemplatePropV1ApplicationPolicy",
    "EnrollmentTemplateProperty_TemplatePropAsymmetricAlgorithm",
    "EnrollmentTemplateProperty_TemplatePropKeySecurityDescriptor",
    "EnrollmentTemplateProperty_TemplatePropSymmetricAlgorithm",
    "EnrollmentTemplateProperty_TemplatePropSymmetricKeyLength",
    "EnrollmentTemplateProperty_TemplatePropHashAlgorithm",
    "EnrollmentTemplateProperty_TemplatePropKeyUsage",
    "EnrollmentTemplateProperty_TemplatePropEnrollmentFlags",
    "EnrollmentTemplateProperty_TemplatePropSubjectNameFlags",
    "EnrollmentTemplateProperty_TemplatePropPrivateKeyFlags",
    "EnrollmentTemplateProperty_TemplatePropGeneralFlags",
    "EnrollmentTemplateProperty_TemplatePropSecurityDescriptor",
    "EnrollmentTemplateProperty_TemplatePropExtensions",
    "EnrollmentTemplateProperty_TemplatePropValidityPeriod",
    "EnrollmentTemplateProperty_TemplatePropRenewalPeriod",
    "IX509CertificateTemplate",
    "IX509CertificateTemplates",
    "CommitTemplateFlags",
    "CommitTemplateFlags_CommitFlagSaveTemplateGenerateOID",
    "CommitTemplateFlags_CommitFlagSaveTemplateUseCurrentOID",
    "CommitTemplateFlags_CommitFlagSaveTemplateOverwrite",
    "CommitTemplateFlags_CommitFlagDeleteTemplate",
    "IX509CertificateTemplateWritable",
    "EnrollmentCAProperty",
    "EnrollmentCAProperty_CAPropCommonName",
    "EnrollmentCAProperty_CAPropDistinguishedName",
    "EnrollmentCAProperty_CAPropSanitizedName",
    "EnrollmentCAProperty_CAPropSanitizedShortName",
    "EnrollmentCAProperty_CAPropDNSName",
    "EnrollmentCAProperty_CAPropCertificateTypes",
    "EnrollmentCAProperty_CAPropCertificate",
    "EnrollmentCAProperty_CAPropDescription",
    "EnrollmentCAProperty_CAPropWebServers",
    "EnrollmentCAProperty_CAPropSiteName",
    "EnrollmentCAProperty_CAPropSecurity",
    "EnrollmentCAProperty_CAPropRenewalOnly",
    "ICertificationAuthority",
    "ICertificationAuthorities",
    "X509EnrollmentPolicyLoadOption",
    "X509EnrollmentPolicyLoadOption_LoadOptionDefault",
    "X509EnrollmentPolicyLoadOption_LoadOptionCacheOnly",
    "X509EnrollmentPolicyLoadOption_LoadOptionReload",
    "X509EnrollmentPolicyLoadOption_LoadOptionRegisterForADChanges",
    "EnrollmentPolicyFlags",
    "EnrollmentPolicyFlags_DisableGroupPolicyList",
    "EnrollmentPolicyFlags_DisableUserServerList",
    "PolicyServerUrlPropertyID",
    "PolicyServerUrlPropertyID_PsPolicyID",
    "PolicyServerUrlPropertyID_PsFriendlyName",
    "X509EnrollmentPolicyExportFlags",
    "X509EnrollmentPolicyExportFlags_ExportTemplates",
    "X509EnrollmentPolicyExportFlags_ExportOIDs",
    "X509EnrollmentPolicyExportFlags_ExportCAs",
    "IX509EnrollmentPolicyServer",
    "IX509PolicyServerUrl",
    "IX509PolicyServerListManager",
    "X509RequestType",
    "X509RequestType_TypeAny",
    "X509RequestType_TypePkcs10",
    "X509RequestType_TypePkcs7",
    "X509RequestType_TypeCmc",
    "X509RequestType_TypeCertificate",
    "X509RequestInheritOptions",
    "X509RequestInheritOptions_InheritDefault",
    "X509RequestInheritOptions_InheritNewDefaultKey",
    "X509RequestInheritOptions_InheritNewSimilarKey",
    "X509RequestInheritOptions_InheritPrivateKey",
    "X509RequestInheritOptions_InheritPublicKey",
    "X509RequestInheritOptions_InheritKeyMask",
    "X509RequestInheritOptions_InheritNone",
    "X509RequestInheritOptions_InheritRenewalCertificateFlag",
    "X509RequestInheritOptions_InheritTemplateFlag",
    "X509RequestInheritOptions_InheritSubjectFlag",
    "X509RequestInheritOptions_InheritExtensionsFlag",
    "X509RequestInheritOptions_InheritSubjectAltNameFlag",
    "X509RequestInheritOptions_InheritValidityPeriodFlag",
    "X509RequestInheritOptions_InheritReserved80000000",
    "InnerRequestLevel",
    "InnerRequestLevel_LevelInnermost",
    "InnerRequestLevel_LevelNext",
    "IX509CertificateRequest",
    "Pkcs10AllowedSignatureTypes",
    "Pkcs10AllowedSignatureTypes_AllowedKeySignature",
    "Pkcs10AllowedSignatureTypes_AllowedNullSignature",
    "IX509CertificateRequestPkcs10",
    "IX509CertificateRequestPkcs10V2",
    "IX509CertificateRequestPkcs10V3",
    "KeyAttestationClaimType",
    "XCN_NCRYPT_CLAIM_NONE",
    "XCN_NCRYPT_CLAIM_AUTHORITY_AND_SUBJECT",
    "XCN_NCRYPT_CLAIM_AUTHORITY_ONLY",
    "XCN_NCRYPT_CLAIM_SUBJECT_ONLY",
    "XCN_NCRYPT_CLAIM_UNKNOWN",
    "IX509CertificateRequestPkcs10V4",
    "IX509CertificateRequestCertificate",
    "IX509CertificateRequestCertificate2",
    "IX509CertificateRequestPkcs7",
    "IX509CertificateRequestPkcs7V2",
    "IX509CertificateRequestCmc",
    "IX509CertificateRequestCmc2",
    "InstallResponseRestrictionFlags",
    "InstallResponseRestrictionFlags_AllowNone",
    "InstallResponseRestrictionFlags_AllowNoOutstandingRequest",
    "InstallResponseRestrictionFlags_AllowUntrustedCertificate",
    "InstallResponseRestrictionFlags_AllowUntrustedRoot",
    "IX509Enrollment",
    "IX509Enrollment2",
    "WebEnrollmentFlags",
    "WebEnrollmentFlags_EnrollPrompt",
    "IX509EnrollmentHelper",
    "IX509EnrollmentWebClassFactory",
    "IX509MachineEnrollmentFactory",
    "CRLRevocationReason",
    "XCN_CRL_REASON_UNSPECIFIED",
    "XCN_CRL_REASON_KEY_COMPROMISE",
    "XCN_CRL_REASON_CA_COMPROMISE",
    "XCN_CRL_REASON_AFFILIATION_CHANGED",
    "XCN_CRL_REASON_SUPERSEDED",
    "XCN_CRL_REASON_CESSATION_OF_OPERATION",
    "XCN_CRL_REASON_CERTIFICATE_HOLD",
    "XCN_CRL_REASON_REMOVE_FROM_CRL",
    "XCN_CRL_REASON_PRIVILEGE_WITHDRAWN",
    "XCN_CRL_REASON_AA_COMPROMISE",
    "IX509CertificateRevocationListEntry",
    "IX509CertificateRevocationListEntries",
    "IX509CertificateRevocationList",
    "ICertificateAttestationChallenge",
    "ICertificateAttestationChallenge2",
    "IX509SCEPEnrollment",
    "X509SCEPProcessMessageFlags",
    "X509SCEPProcessMessageFlags_SCEPProcessDefault",
    "X509SCEPProcessMessageFlags_SCEPProcessSkipCertInstall",
    "DelayRetryAction",
    "DelayRetryAction_DelayRetryUnknown",
    "DelayRetryAction_DelayRetryNone",
    "DelayRetryAction_DelayRetryShort",
    "DelayRetryAction_DelayRetryLong",
    "DelayRetryAction_DelayRetrySuccess",
    "DelayRetryAction_DelayRetryPastSuccess",
    "IX509SCEPEnrollment2",
    "IX509SCEPEnrollmentHelper",
    "X509CertificateTemplateGeneralFlag",
    "X509CertificateTemplateGeneralFlag_GeneralMachineType",
    "X509CertificateTemplateGeneralFlag_GeneralCA",
    "X509CertificateTemplateGeneralFlag_GeneralCrossCA",
    "X509CertificateTemplateGeneralFlag_GeneralDefault",
    "X509CertificateTemplateGeneralFlag_GeneralModified",
    "X509CertificateTemplateGeneralFlag_GeneralDonotPersist",
    "X509CertificateTemplateEnrollmentFlag",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentIncludeSymmetricAlgorithms",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentPendAllRequests",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentPublishToKRAContainer",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentPublishToDS",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentAutoEnrollmentCheckUserDSCertificate",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentAutoEnrollment",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentDomainAuthenticationNotRequired",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentPreviousApprovalValidateReenrollment",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentUserInteractionRequired",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentAddTemplateName",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentRemoveInvalidCertificateFromPersonalStore",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentAllowEnrollOnBehalfOf",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentAddOCSPNoCheck",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentReuseKeyOnFullSmartCard",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentNoRevocationInfoInCerts",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentIncludeBasicConstraintsForEECerts",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentPreviousApprovalKeyBasedValidateReenrollment",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentCertificateIssuancePoliciesFromRequest",
    "X509CertificateTemplateEnrollmentFlag_EnrollmentSkipAutoRenewal",
    "X509CertificateTemplateSubjectNameFlag",
    "X509CertificateTemplateSubjectNameFlag_SubjectNameEnrolleeSupplies",
    "X509CertificateTemplateSubjectNameFlag_SubjectNameRequireDirectoryPath",
    "X509CertificateTemplateSubjectNameFlag_SubjectNameRequireCommonName",
    "X509CertificateTemplateSubjectNameFlag_SubjectNameRequireEmail",
    "X509CertificateTemplateSubjectNameFlag_SubjectNameRequireDNS",
    "X509CertificateTemplateSubjectNameFlag_SubjectNameAndAlternativeNameOldCertSupplies",
    "X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameEnrolleeSupplies",
    "X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireDirectoryGUID",
    "X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireUPN",
    "X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireEmail",
    "X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireSPN",
    "X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireDNS",
    "X509CertificateTemplateSubjectNameFlag_SubjectAlternativeNameRequireDomainDNS",
    "X509CertificateTemplatePrivateKeyFlag",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyRequireArchival",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyExportable",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyRequireStrongKeyProtection",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyRequireAlternateSignatureAlgorithm",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyRequireSameKeyRenewal",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyUseLegacyProvider",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyEKTrustOnUse",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyEKValidateCert",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyEKValidateKey",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyAttestNone",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyAttestPreferred",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyAttestRequired",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyAttestMask",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyAttestWithoutPolicy",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyServerVersionMask",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyServerVersionShift",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyHelloKspKey",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyHelloLogonKey",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyClientVersionMask",
    "X509CertificateTemplatePrivateKeyFlag_PrivateKeyClientVersionShift",
    "ImportPFXFlags",
    "ImportPFXFlags_ImportNone",
    "ImportPFXFlags_ImportMachineContext",
    "ImportPFXFlags_ImportForceOverwrite",
    "ImportPFXFlags_ImportSilent",
    "ImportPFXFlags_ImportSaveProperties",
    "ImportPFXFlags_ImportExportable",
    "ImportPFXFlags_ImportExportableEncrypted",
    "ImportPFXFlags_ImportNoUserProtected",
    "ImportPFXFlags_ImportUserProtected",
    "ImportPFXFlags_ImportUserProtectedHigh",
    "ImportPFXFlags_ImportInstallCertificate",
    "ImportPFXFlags_ImportInstallChain",
    "ImportPFXFlags_ImportInstallChainAndRoot",
    "FNIMPORTPFXTOPROVIDER",
    "FNIMPORTPFXTOPROVIDERFREEDATA",
    "ICertEncodeStringArray",
    "ICertEncodeStringArray2",
    "ICertEncodeLongArray",
    "ICertEncodeLongArray2",
    "ICertEncodeDateArray",
    "ICertEncodeDateArray2",
    "ICertEncodeCRLDistInfo",
    "ICertEncodeCRLDistInfo2",
    "ICertEncodeAltName",
    "ICertEncodeAltName2",
    "ICertEncodeBitString",
    "ICertEncodeBitString2",
    "ICertExit",
    "ICertExit2",
    "ENUM_CATYPES",
    "ENUM_ENTERPRISE_ROOTCA",
    "ENUM_ENTERPRISE_SUBCA",
    "ENUM_STANDALONE_ROOTCA",
    "ENUM_STANDALONE_SUBCA",
    "ENUM_UNKNOWN_CA",
    "CAINFO",
    "CEnroll2",
    "CEnroll",
    "ICEnroll",
    "ICEnroll2",
    "ICEnroll3",
    "ICEnroll4",
    "IEnroll",
    "IEnroll2",
    "IEnroll4",
    "ICertRequestD",
    "ICertRequestD2",
    "CertSrvIsServerOnlineW",
    "CertSrvBackupGetDynamicFileListW",
    "CertSrvBackupPrepareW",
    "CertSrvBackupGetDatabaseNamesW",
    "CertSrvBackupOpenFileW",
    "CertSrvBackupRead",
    "CertSrvBackupClose",
    "CertSrvBackupGetBackupLogsW",
    "CertSrvBackupTruncateLogs",
    "CertSrvBackupEnd",
    "CertSrvBackupFree",
    "CertSrvRestoreGetDatabaseLocationsW",
    "CertSrvRestorePrepareW",
    "CertSrvRestoreRegisterW",
    "CertSrvRestoreRegisterThroughFile",
    "CertSrvRestoreRegisterComplete",
    "CertSrvRestoreEnd",
    "CertSrvServerControlW",
    "PstGetTrustAnchors",
    "PstGetTrustAnchorsEx",
    "PstGetCertificateChain",
    "PstGetCertificates",
    "PstAcquirePrivateKey",
    "PstValidate",
    "PstMapCertificate",
    "PstGetUserNameForCertificate",
]
