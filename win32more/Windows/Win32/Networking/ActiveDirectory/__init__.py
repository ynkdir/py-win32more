from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.ActiveDirectory
import win32more.Windows.Win32.Networking.WinSock
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.Authentication.Identity
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.Registry
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.Controls
import win32more.Windows.Win32.UI.Shell
import win32more.Windows.Win32.UI.WindowsAndMessaging
ADSI_DIALECT_ENUM = Int32
ADSI_DIALECT_LDAP: win32more.Windows.Win32.Networking.ActiveDirectory.ADSI_DIALECT_ENUM = 0
ADSI_DIALECT_SQL: win32more.Windows.Win32.Networking.ActiveDirectory.ADSI_DIALECT_ENUM = 1
class ADSPROPERROR(Structure):
    hwndPage: win32more.Windows.Win32.Foundation.HWND
    pszPageTitle: win32more.Windows.Win32.Foundation.PWSTR
    pszObjPath: win32more.Windows.Win32.Foundation.PWSTR
    pszObjClass: win32more.Windows.Win32.Foundation.PWSTR
    hr: win32more.Windows.Win32.Foundation.HRESULT
    pszError: win32more.Windows.Win32.Foundation.PWSTR
class ADSPROPINITPARAMS(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    hr: win32more.Windows.Win32.Foundation.HRESULT
    pDsObj: win32more.Windows.Win32.Networking.ActiveDirectory.IDirectoryObject
    pwzCN: win32more.Windows.Win32.Foundation.PWSTR
    pWritableAttrs: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ATTR_INFO)
ADSTYPE = Int32
ADSTYPE_INVALID: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 0
ADSTYPE_DN_STRING: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 1
ADSTYPE_CASE_EXACT_STRING: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 2
ADSTYPE_CASE_IGNORE_STRING: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 3
ADSTYPE_PRINTABLE_STRING: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 4
ADSTYPE_NUMERIC_STRING: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 5
ADSTYPE_BOOLEAN: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 6
ADSTYPE_INTEGER: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 7
ADSTYPE_OCTET_STRING: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 8
ADSTYPE_UTC_TIME: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 9
ADSTYPE_LARGE_INTEGER: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 10
ADSTYPE_PROV_SPECIFIC: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 11
ADSTYPE_OBJECT_CLASS: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 12
ADSTYPE_CASEIGNORE_LIST: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 13
ADSTYPE_OCTET_LIST: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 14
ADSTYPE_PATH: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 15
ADSTYPE_POSTALADDRESS: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 16
ADSTYPE_TIMESTAMP: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 17
ADSTYPE_BACKLINK: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 18
ADSTYPE_TYPEDNAME: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 19
ADSTYPE_HOLD: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 20
ADSTYPE_NETADDRESS: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 21
ADSTYPE_REPLICAPOINTER: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 22
ADSTYPE_FAXNUMBER: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 23
ADSTYPE_EMAIL: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 24
ADSTYPE_NT_SECURITY_DESCRIPTOR: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 25
ADSTYPE_UNKNOWN: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 26
ADSTYPE_DN_WITH_BINARY: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 27
ADSTYPE_DN_WITH_STRING: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE = 28
class ADSVALUE(Structure):
    dwType: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        DNString: POINTER(UInt16)
        CaseExactString: POINTER(UInt16)
        CaseIgnoreString: POINTER(UInt16)
        PrintableString: POINTER(UInt16)
        NumericString: POINTER(UInt16)
        Boolean: UInt32
        Integer: UInt32
        OctetString: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OCTET_STRING
        UTCTime: win32more.Windows.Win32.Foundation.SYSTEMTIME
        LargeInteger: Int64
        ClassName: POINTER(UInt16)
        ProviderSpecific: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PROV_SPECIFIC
        pCaseIgnoreList: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_CASEIGNORE_LIST)
        pOctetList: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OCTET_LIST)
        pPath: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PATH)
        pPostalAddress: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_POSTALADDRESS)
        Timestamp: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_TIMESTAMP
        BackLink: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_BACKLINK
        pTypedName: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_TYPEDNAME)
        Hold: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_HOLD
        pNetAddress: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NETADDRESS)
        pReplicaPointer: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_REPLICAPOINTER)
        pFaxNumber: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FAXNUMBER)
        Email: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_EMAIL
        SecurityDescriptor: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NT_SECURITY_DESCRIPTOR
        pDNWithBinary: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_DN_WITH_BINARY)
        pDNWithString: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_DN_WITH_STRING)
ADS_ACEFLAG_ENUM = Int32
ADS_ACEFLAG_INHERIT_ACE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACEFLAG_ENUM = 2
ADS_ACEFLAG_NO_PROPAGATE_INHERIT_ACE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACEFLAG_ENUM = 4
ADS_ACEFLAG_INHERIT_ONLY_ACE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACEFLAG_ENUM = 8
ADS_ACEFLAG_INHERITED_ACE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACEFLAG_ENUM = 16
ADS_ACEFLAG_VALID_INHERIT_FLAGS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACEFLAG_ENUM = 31
ADS_ACEFLAG_SUCCESSFUL_ACCESS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACEFLAG_ENUM = 64
ADS_ACEFLAG_FAILED_ACCESS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACEFLAG_ENUM = 128
ADS_ACETYPE_ENUM = Int32
ADS_ACETYPE_ACCESS_ALLOWED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 0
ADS_ACETYPE_ACCESS_DENIED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 1
ADS_ACETYPE_SYSTEM_AUDIT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 2
ADS_ACETYPE_ACCESS_ALLOWED_OBJECT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 5
ADS_ACETYPE_ACCESS_DENIED_OBJECT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 6
ADS_ACETYPE_SYSTEM_AUDIT_OBJECT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 7
ADS_ACETYPE_SYSTEM_ALARM_OBJECT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 8
ADS_ACETYPE_ACCESS_ALLOWED_CALLBACK: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 9
ADS_ACETYPE_ACCESS_DENIED_CALLBACK: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 10
ADS_ACETYPE_ACCESS_ALLOWED_CALLBACK_OBJECT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 11
ADS_ACETYPE_ACCESS_DENIED_CALLBACK_OBJECT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 12
ADS_ACETYPE_SYSTEM_AUDIT_CALLBACK: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 13
ADS_ACETYPE_SYSTEM_ALARM_CALLBACK: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 14
ADS_ACETYPE_SYSTEM_AUDIT_CALLBACK_OBJECT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 15
ADS_ACETYPE_SYSTEM_ALARM_CALLBACK_OBJECT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ACETYPE_ENUM = 16
class ADS_ATTR_DEF(Structure):
    pszAttrName: win32more.Windows.Win32.Foundation.PWSTR
    dwADsType: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE
    dwMinRange: UInt32
    dwMaxRange: UInt32
    fMultiValued: win32more.Windows.Win32.Foundation.BOOL
class ADS_ATTR_INFO(Structure):
    pszAttrName: win32more.Windows.Win32.Foundation.PWSTR
    dwControlCode: UInt32
    dwADsType: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE
    pADsValues: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADSVALUE)
    dwNumValues: UInt32
ADS_AUTHENTICATION_ENUM = UInt32
ADS_SECURE_AUTHENTICATION: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 1
ADS_USE_ENCRYPTION: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 2
ADS_USE_SSL: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 2
ADS_READONLY_SERVER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 4
ADS_PROMPT_CREDENTIALS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 8
ADS_NO_AUTHENTICATION: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 16
ADS_FAST_BIND: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 32
ADS_USE_SIGNING: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 64
ADS_USE_SEALING: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 128
ADS_USE_DELEGATION: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 256
ADS_SERVER_BIND: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 512
ADS_NO_REFERRAL_CHASING: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 1024
ADS_AUTH_RESERVED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM = 2147483648
class ADS_BACKLINK(Structure):
    RemoteID: UInt32
    ObjectName: win32more.Windows.Win32.Foundation.PWSTR
class ADS_CASEIGNORE_LIST(Structure):
    Next: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_CASEIGNORE_LIST)
    String: win32more.Windows.Win32.Foundation.PWSTR
ADS_CHASE_REFERRALS_ENUM = Int32
ADS_CHASE_REFERRALS_NEVER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_CHASE_REFERRALS_ENUM = 0
ADS_CHASE_REFERRALS_SUBORDINATE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_CHASE_REFERRALS_ENUM = 32
ADS_CHASE_REFERRALS_EXTERNAL: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_CHASE_REFERRALS_ENUM = 64
ADS_CHASE_REFERRALS_ALWAYS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_CHASE_REFERRALS_ENUM = 96
class ADS_CLASS_DEF(Structure):
    pszClassName: win32more.Windows.Win32.Foundation.PWSTR
    dwMandatoryAttrs: UInt32
    ppszMandatoryAttrs: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    optionalAttrs: UInt32
    ppszOptionalAttrs: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))
    dwNamingAttrs: UInt32
    ppszNamingAttrs: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))
    dwSuperClasses: UInt32
    ppszSuperClasses: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))
    fIsContainer: win32more.Windows.Win32.Foundation.BOOL
ADS_DEREFENUM = Int32
ADS_DEREF_NEVER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_DEREFENUM = 0
ADS_DEREF_SEARCHING: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_DEREFENUM = 1
ADS_DEREF_FINDING: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_DEREFENUM = 2
ADS_DEREF_ALWAYS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_DEREFENUM = 3
ADS_DISPLAY_ENUM = Int32
ADS_DISPLAY_FULL: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_DISPLAY_ENUM = 1
ADS_DISPLAY_VALUE_ONLY: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_DISPLAY_ENUM = 2
class ADS_DN_WITH_BINARY(Structure):
    dwLength: UInt32
    lpBinaryValue: POINTER(Byte)
    pszDNString: win32more.Windows.Win32.Foundation.PWSTR
class ADS_DN_WITH_STRING(Structure):
    pszStringValue: win32more.Windows.Win32.Foundation.PWSTR
    pszDNString: win32more.Windows.Win32.Foundation.PWSTR
class ADS_EMAIL(Structure):
    Address: win32more.Windows.Win32.Foundation.PWSTR
    Type: UInt32
ADS_ESCAPE_MODE_ENUM = Int32
ADS_ESCAPEDMODE_DEFAULT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ESCAPE_MODE_ENUM = 1
ADS_ESCAPEDMODE_ON: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ESCAPE_MODE_ENUM = 2
ADS_ESCAPEDMODE_OFF: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ESCAPE_MODE_ENUM = 3
ADS_ESCAPEDMODE_OFF_EX: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ESCAPE_MODE_ENUM = 4
class ADS_FAXNUMBER(Structure):
    TelephoneNumber: win32more.Windows.Win32.Foundation.PWSTR
    NumberOfBits: UInt32
    Parameters: POINTER(Byte)
ADS_FLAGTYPE_ENUM = Int32
ADS_FLAG_OBJECT_TYPE_PRESENT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FLAGTYPE_ENUM = 1
ADS_FLAG_INHERITED_OBJECT_TYPE_PRESENT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FLAGTYPE_ENUM = 2
ADS_FORMAT_ENUM = Int32
ADS_FORMAT_WINDOWS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FORMAT_ENUM = 1
ADS_FORMAT_WINDOWS_NO_SERVER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FORMAT_ENUM = 2
ADS_FORMAT_WINDOWS_DN: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FORMAT_ENUM = 3
ADS_FORMAT_WINDOWS_PARENT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FORMAT_ENUM = 4
ADS_FORMAT_X500: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FORMAT_ENUM = 5
ADS_FORMAT_X500_NO_SERVER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FORMAT_ENUM = 6
ADS_FORMAT_X500_DN: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FORMAT_ENUM = 7
ADS_FORMAT_X500_PARENT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FORMAT_ENUM = 8
ADS_FORMAT_SERVER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FORMAT_ENUM = 9
ADS_FORMAT_PROVIDER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FORMAT_ENUM = 10
ADS_FORMAT_LEAF: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_FORMAT_ENUM = 11
ADS_GROUP_TYPE_ENUM = Int32
ADS_GROUP_TYPE_GLOBAL_GROUP: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_GROUP_TYPE_ENUM = 2
ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_GROUP_TYPE_ENUM = 4
ADS_GROUP_TYPE_LOCAL_GROUP: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_GROUP_TYPE_ENUM = 4
ADS_GROUP_TYPE_UNIVERSAL_GROUP: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_GROUP_TYPE_ENUM = 8
ADS_GROUP_TYPE_SECURITY_ENABLED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_GROUP_TYPE_ENUM = -2147483648
class ADS_HOLD(Structure):
    ObjectName: win32more.Windows.Win32.Foundation.PWSTR
    Amount: UInt32
ADS_NAME_INITTYPE_ENUM = Int32
ADS_NAME_INITTYPE_DOMAIN: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_INITTYPE_ENUM = 1
ADS_NAME_INITTYPE_SERVER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_INITTYPE_ENUM = 2
ADS_NAME_INITTYPE_GC: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_INITTYPE_ENUM = 3
ADS_NAME_TYPE_ENUM = Int32
ADS_NAME_TYPE_1779: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 1
ADS_NAME_TYPE_CANONICAL: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 2
ADS_NAME_TYPE_NT4: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 3
ADS_NAME_TYPE_DISPLAY: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 4
ADS_NAME_TYPE_DOMAIN_SIMPLE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 5
ADS_NAME_TYPE_ENTERPRISE_SIMPLE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 6
ADS_NAME_TYPE_GUID: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 7
ADS_NAME_TYPE_UNKNOWN: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 8
ADS_NAME_TYPE_USER_PRINCIPAL_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 9
ADS_NAME_TYPE_CANONICAL_EX: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 10
ADS_NAME_TYPE_SERVICE_PRINCIPAL_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 11
ADS_NAME_TYPE_SID_OR_SID_HISTORY_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NAME_TYPE_ENUM = 12
class ADS_NETADDRESS(Structure):
    AddressType: UInt32
    AddressLength: UInt32
    Address: POINTER(Byte)
class ADS_NT_SECURITY_DESCRIPTOR(Structure):
    dwLength: UInt32
    lpValue: POINTER(Byte)
class ADS_OBJECT_INFO(Structure):
    pszRDN: win32more.Windows.Win32.Foundation.PWSTR
    pszObjectDN: win32more.Windows.Win32.Foundation.PWSTR
    pszParentDN: win32more.Windows.Win32.Foundation.PWSTR
    pszSchemaDN: win32more.Windows.Win32.Foundation.PWSTR
    pszClassName: win32more.Windows.Win32.Foundation.PWSTR
class ADS_OCTET_LIST(Structure):
    Next: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OCTET_LIST)
    Length: UInt32
    Data: POINTER(Byte)
class ADS_OCTET_STRING(Structure):
    dwLength: UInt32
    lpValue: POINTER(Byte)
ADS_OPTION_ENUM = Int32
ADS_OPTION_SERVERNAME: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OPTION_ENUM = 0
ADS_OPTION_REFERRALS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OPTION_ENUM = 1
ADS_OPTION_PAGE_SIZE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OPTION_ENUM = 2
ADS_OPTION_SECURITY_MASK: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OPTION_ENUM = 3
ADS_OPTION_MUTUAL_AUTH_STATUS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OPTION_ENUM = 4
ADS_OPTION_QUOTA: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OPTION_ENUM = 5
ADS_OPTION_PASSWORD_PORTNUMBER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OPTION_ENUM = 6
ADS_OPTION_PASSWORD_METHOD: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OPTION_ENUM = 7
ADS_OPTION_ACCUMULATIVE_MODIFICATION: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OPTION_ENUM = 8
ADS_OPTION_SKIP_SID_LOOKUP: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OPTION_ENUM = 9
ADS_PASSWORD_ENCODING_ENUM = Int32
ADS_PASSWORD_ENCODE_REQUIRE_SSL: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PASSWORD_ENCODING_ENUM = 0
ADS_PASSWORD_ENCODE_CLEAR: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PASSWORD_ENCODING_ENUM = 1
class ADS_PATH(Structure):
    Type: UInt32
    VolumeName: win32more.Windows.Win32.Foundation.PWSTR
    Path: win32more.Windows.Win32.Foundation.PWSTR
ADS_PATHTYPE_ENUM = Int32
ADS_PATH_FILE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PATHTYPE_ENUM = 1
ADS_PATH_FILESHARE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PATHTYPE_ENUM = 2
ADS_PATH_REGISTRY: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PATHTYPE_ENUM = 3
class ADS_POSTALADDRESS(Structure):
    PostalAddress: win32more.Windows.Win32.Foundation.PWSTR * 6
ADS_PREFERENCES_ENUM = Int32
ADSIPROP_ASYNCHRONOUS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 0
ADSIPROP_DEREF_ALIASES: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 1
ADSIPROP_SIZE_LIMIT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 2
ADSIPROP_TIME_LIMIT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 3
ADSIPROP_ATTRIBTYPES_ONLY: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 4
ADSIPROP_SEARCH_SCOPE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 5
ADSIPROP_TIMEOUT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 6
ADSIPROP_PAGESIZE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 7
ADSIPROP_PAGED_TIME_LIMIT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 8
ADSIPROP_CHASE_REFERRALS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 9
ADSIPROP_SORT_ON: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 10
ADSIPROP_CACHE_RESULTS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 11
ADSIPROP_ADSIFLAG: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PREFERENCES_ENUM = 12
ADS_PROPERTY_OPERATION_ENUM = Int32
ADS_PROPERTY_CLEAR: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PROPERTY_OPERATION_ENUM = 1
ADS_PROPERTY_UPDATE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PROPERTY_OPERATION_ENUM = 2
ADS_PROPERTY_APPEND: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PROPERTY_OPERATION_ENUM = 3
ADS_PROPERTY_DELETE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_PROPERTY_OPERATION_ENUM = 4
class ADS_PROV_SPECIFIC(Structure):
    dwLength: UInt32
    lpValue: POINTER(Byte)
class ADS_REPLICAPOINTER(Structure):
    ServerName: win32more.Windows.Win32.Foundation.PWSTR
    ReplicaType: UInt32
    ReplicaNumber: UInt32
    Count: UInt32
    ReplicaAddressHints: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_NETADDRESS)
ADS_RIGHTS_ENUM = Int32
ADS_RIGHT_DELETE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 65536
ADS_RIGHT_READ_CONTROL: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 131072
ADS_RIGHT_WRITE_DAC: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 262144
ADS_RIGHT_WRITE_OWNER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 524288
ADS_RIGHT_SYNCHRONIZE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 1048576
ADS_RIGHT_ACCESS_SYSTEM_SECURITY: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 16777216
ADS_RIGHT_GENERIC_READ: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = -2147483648
ADS_RIGHT_GENERIC_WRITE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 1073741824
ADS_RIGHT_GENERIC_EXECUTE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 536870912
ADS_RIGHT_GENERIC_ALL: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 268435456
ADS_RIGHT_DS_CREATE_CHILD: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 1
ADS_RIGHT_DS_DELETE_CHILD: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 2
ADS_RIGHT_ACTRL_DS_LIST: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 4
ADS_RIGHT_DS_SELF: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 8
ADS_RIGHT_DS_READ_PROP: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 16
ADS_RIGHT_DS_WRITE_PROP: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 32
ADS_RIGHT_DS_DELETE_TREE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 64
ADS_RIGHT_DS_LIST_OBJECT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 128
ADS_RIGHT_DS_CONTROL_ACCESS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_RIGHTS_ENUM = 256
ADS_SCOPEENUM = Int32
ADS_SCOPE_BASE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SCOPEENUM = 0
ADS_SCOPE_ONELEVEL: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SCOPEENUM = 1
ADS_SCOPE_SUBTREE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SCOPEENUM = 2
ADS_SD_CONTROL_ENUM = Int32
ADS_SD_CONTROL_SE_OWNER_DEFAULTED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 1
ADS_SD_CONTROL_SE_GROUP_DEFAULTED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 2
ADS_SD_CONTROL_SE_DACL_PRESENT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 4
ADS_SD_CONTROL_SE_DACL_DEFAULTED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 8
ADS_SD_CONTROL_SE_SACL_PRESENT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 16
ADS_SD_CONTROL_SE_SACL_DEFAULTED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 32
ADS_SD_CONTROL_SE_DACL_AUTO_INHERIT_REQ: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 256
ADS_SD_CONTROL_SE_SACL_AUTO_INHERIT_REQ: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 512
ADS_SD_CONTROL_SE_DACL_AUTO_INHERITED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 1024
ADS_SD_CONTROL_SE_SACL_AUTO_INHERITED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 2048
ADS_SD_CONTROL_SE_DACL_PROTECTED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 4096
ADS_SD_CONTROL_SE_SACL_PROTECTED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 8192
ADS_SD_CONTROL_SE_SELF_RELATIVE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_CONTROL_ENUM = 32768
ADS_SD_FORMAT_ENUM = Int32
ADS_SD_FORMAT_IID: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_FORMAT_ENUM = 1
ADS_SD_FORMAT_RAW: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_FORMAT_ENUM = 2
ADS_SD_FORMAT_HEXSTRING: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_FORMAT_ENUM = 3
ADS_SD_REVISION_ENUM = Int32
ADS_SD_REVISION_DS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SD_REVISION_ENUM = 4
ADS_SEARCHPREF_ENUM = Int32
ADS_SEARCHPREF_ASYNCHRONOUS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 0
ADS_SEARCHPREF_DEREF_ALIASES: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 1
ADS_SEARCHPREF_SIZE_LIMIT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 2
ADS_SEARCHPREF_TIME_LIMIT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 3
ADS_SEARCHPREF_ATTRIBTYPES_ONLY: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 4
ADS_SEARCHPREF_SEARCH_SCOPE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 5
ADS_SEARCHPREF_TIMEOUT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 6
ADS_SEARCHPREF_PAGESIZE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 7
ADS_SEARCHPREF_PAGED_TIME_LIMIT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 8
ADS_SEARCHPREF_CHASE_REFERRALS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 9
ADS_SEARCHPREF_SORT_ON: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 10
ADS_SEARCHPREF_CACHE_RESULTS: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 11
ADS_SEARCHPREF_DIRSYNC: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 12
ADS_SEARCHPREF_TOMBSTONE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 13
ADS_SEARCHPREF_VLV: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 14
ADS_SEARCHPREF_ATTRIBUTE_QUERY: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 15
ADS_SEARCHPREF_SECURITY_MASK: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 16
ADS_SEARCHPREF_DIRSYNC_FLAG: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 17
ADS_SEARCHPREF_EXTENDED_DN: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM = 18
class ADS_SEARCHPREF_INFO(Structure):
    dwSearchPref: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_ENUM
    vValue: win32more.Windows.Win32.Networking.ActiveDirectory.ADSVALUE
    dwStatus: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_STATUSENUM
class ADS_SEARCH_COLUMN(Structure):
    pszAttrName: win32more.Windows.Win32.Foundation.PWSTR
    dwADsType: win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE
    pADsValues: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADSVALUE)
    dwNumValues: UInt32
    hReserved: win32more.Windows.Win32.Foundation.HANDLE
ADS_SEARCH_HANDLE = IntPtr
ADS_SECURITY_INFO_ENUM = Int32
ADS_SECURITY_INFO_OWNER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SECURITY_INFO_ENUM = 1
ADS_SECURITY_INFO_GROUP: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SECURITY_INFO_ENUM = 2
ADS_SECURITY_INFO_DACL: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SECURITY_INFO_ENUM = 4
ADS_SECURITY_INFO_SACL: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SECURITY_INFO_ENUM = 8
ADS_SETTYPE_ENUM = Int32
ADS_SETTYPE_FULL: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SETTYPE_ENUM = 1
ADS_SETTYPE_PROVIDER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SETTYPE_ENUM = 2
ADS_SETTYPE_SERVER: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SETTYPE_ENUM = 3
ADS_SETTYPE_DN: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SETTYPE_ENUM = 4
class ADS_SORTKEY(Structure):
    pszAttrType: win32more.Windows.Win32.Foundation.PWSTR
    pszReserved: win32more.Windows.Win32.Foundation.PWSTR
    fReverseorder: win32more.Windows.Win32.Foundation.BOOLEAN
ADS_STATUSENUM = Int32
ADS_STATUS_S_OK: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_STATUSENUM = 0
ADS_STATUS_INVALID_SEARCHPREF: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_STATUSENUM = 1
ADS_STATUS_INVALID_SEARCHPREFVALUE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_STATUSENUM = 2
ADS_SYSTEMFLAG_ENUM = Int32
ADS_SYSTEMFLAG_DISALLOW_DELETE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SYSTEMFLAG_ENUM = -2147483648
ADS_SYSTEMFLAG_CONFIG_ALLOW_RENAME: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SYSTEMFLAG_ENUM = 1073741824
ADS_SYSTEMFLAG_CONFIG_ALLOW_MOVE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SYSTEMFLAG_ENUM = 536870912
ADS_SYSTEMFLAG_CONFIG_ALLOW_LIMITED_MOVE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SYSTEMFLAG_ENUM = 268435456
ADS_SYSTEMFLAG_DOMAIN_DISALLOW_RENAME: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SYSTEMFLAG_ENUM = 134217728
ADS_SYSTEMFLAG_DOMAIN_DISALLOW_MOVE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SYSTEMFLAG_ENUM = 67108864
ADS_SYSTEMFLAG_CR_NTDS_NC: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SYSTEMFLAG_ENUM = 1
ADS_SYSTEMFLAG_CR_NTDS_DOMAIN: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SYSTEMFLAG_ENUM = 2
ADS_SYSTEMFLAG_ATTR_NOT_REPLICATED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SYSTEMFLAG_ENUM = 1
ADS_SYSTEMFLAG_ATTR_IS_CONSTRUCTED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SYSTEMFLAG_ENUM = 4
class ADS_TIMESTAMP(Structure):
    WholeSeconds: UInt32
    EventID: UInt32
class ADS_TYPEDNAME(Structure):
    ObjectName: win32more.Windows.Win32.Foundation.PWSTR
    Level: UInt32
    Interval: UInt32
ADS_USER_FLAG_ENUM = Int32
ADS_UF_SCRIPT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 1
ADS_UF_ACCOUNTDISABLE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 2
ADS_UF_HOMEDIR_REQUIRED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 8
ADS_UF_LOCKOUT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 16
ADS_UF_PASSWD_NOTREQD: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 32
ADS_UF_PASSWD_CANT_CHANGE: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 64
ADS_UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 128
ADS_UF_TEMP_DUPLICATE_ACCOUNT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 256
ADS_UF_NORMAL_ACCOUNT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 512
ADS_UF_INTERDOMAIN_TRUST_ACCOUNT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 2048
ADS_UF_WORKSTATION_TRUST_ACCOUNT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 4096
ADS_UF_SERVER_TRUST_ACCOUNT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 8192
ADS_UF_DONT_EXPIRE_PASSWD: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 65536
ADS_UF_MNS_LOGON_ACCOUNT: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 131072
ADS_UF_SMARTCARD_REQUIRED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 262144
ADS_UF_TRUSTED_FOR_DELEGATION: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 524288
ADS_UF_NOT_DELEGATED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 1048576
ADS_UF_USE_DES_KEY_ONLY: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 2097152
ADS_UF_DONT_REQUIRE_PREAUTH: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 4194304
ADS_UF_PASSWORD_EXPIRED: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 8388608
ADS_UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_USER_FLAG_ENUM = 16777216
class ADS_VLV(Structure):
    dwBeforeCount: UInt32
    dwAfterCount: UInt32
    dwOffset: UInt32
    dwContentCount: UInt32
    pszTarget: win32more.Windows.Win32.Foundation.PWSTR
    dwContextIDLength: UInt32
    lpContextID: POINTER(Byte)
ADSystemInfo = Guid('{50b6327f-afd1-11d2-9cb9-0000f87a369e}')
ADsSecurityUtility = Guid('{f270c64a-ffb8-4ae4-85fe-3a75e5347966}')
AccessControlEntry = Guid('{b75ac000-9bdd-11d0-852c-00c04fd8d503}')
AccessControlList = Guid('{b85ea052-9bdd-11d0-852c-00c04fd8d503}')
WM_ADSPROP_NOTIFY_PAGEINIT: UInt32 = 2125
WM_ADSPROP_NOTIFY_PAGEHWND: UInt32 = 2126
WM_ADSPROP_NOTIFY_CHANGE: UInt32 = 2127
WM_ADSPROP_NOTIFY_APPLY: UInt32 = 2128
WM_ADSPROP_NOTIFY_SETFOCUS: UInt32 = 2129
WM_ADSPROP_NOTIFY_FOREGROUND: UInt32 = 2130
WM_ADSPROP_NOTIFY_EXIT: UInt32 = 2131
WM_ADSPROP_NOTIFY_ERROR: UInt32 = 2134
CLSID_CommonQuery: Guid = Guid('{83bc5ec0-6f2a-11d0-a1c4-00aa00c16e65}')
QUERYFORM_CHANGESFORMLIST: UInt64 = 1
QUERYFORM_CHANGESOPTFORMLIST: UInt64 = 2
CQFF_NOGLOBALPAGES: UInt32 = 1
CQFF_ISOPTIONAL: UInt32 = 2
CQPM_INITIALIZE: UInt32 = 1
CQPM_RELEASE: UInt32 = 2
CQPM_ENABLE: UInt32 = 3
CQPM_GETPARAMETERS: UInt32 = 5
CQPM_CLEARFORM: UInt32 = 6
CQPM_PERSIST: UInt32 = 7
CQPM_HELP: UInt32 = 8
CQPM_SETDEFAULTPARAMETERS: UInt32 = 9
CQPM_HANDLERSPECIFIC: UInt32 = 268435456
OQWF_OKCANCEL: UInt32 = 1
OQWF_DEFAULTFORM: UInt32 = 2
OQWF_SINGLESELECT: UInt32 = 4
OQWF_LOADQUERY: UInt32 = 8
OQWF_REMOVESCOPES: UInt32 = 16
OQWF_REMOVEFORMS: UInt32 = 32
OQWF_ISSUEONOPEN: UInt32 = 64
OQWF_SHOWOPTIONAL: UInt32 = 128
OQWF_SAVEQUERYONOK: UInt32 = 512
OQWF_HIDEMENUS: UInt32 = 1024
OQWF_HIDESEARCHUI: UInt32 = 2048
OQWF_PARAMISPROPERTYBAG: UInt32 = 2147483648
CLSID_DsAdminCreateObj: Guid = Guid('{e301a009-f901-11d2-82b9-00c04f68928b}')
DSA_NEWOBJ_CTX_PRECOMMIT: UInt32 = 1
DSA_NEWOBJ_CTX_COMMIT: UInt32 = 2
DSA_NEWOBJ_CTX_POSTCOMMIT: UInt32 = 3
DSA_NEWOBJ_CTX_CLEANUP: UInt32 = 4
DSA_NOTIFY_DEL: UInt32 = 1
DSA_NOTIFY_REN: UInt32 = 2
DSA_NOTIFY_MOV: UInt32 = 4
DSA_NOTIFY_PROP: UInt32 = 8
DSA_NOTIFY_FLAG_ADDITIONAL_DATA: UInt32 = 2
DSA_NOTIFY_FLAG_FORCE_ADDITIONAL_DATA: UInt32 = 1
CLSID_MicrosoftDS: Guid = Guid('{fe1290f0-cfbd-11cf-a330-00aa00c16e65}')
CLSID_DsPropertyPages: Guid = Guid('{0d45d530-764b-11d0-a1ca-00aa00c16e65}')
CLSID_DsDomainTreeBrowser: Guid = Guid('{1698790a-e2b4-11d0-b0b1-00c04fd8dca6}')
CLSID_DsDisplaySpecifier: Guid = Guid('{1ab4a8c0-6a0b-11d2-ad49-00c04fa31a86}')
CLSID_DsFolderProperties: Guid = Guid('{9e51e0d0-6e0f-11d2-9601-00c04fa31a86}')
DSOBJECT_ISCONTAINER: UInt32 = 1
DSOBJECT_READONLYPAGES: UInt32 = 2147483648
DSPROVIDER_UNUSED_0: UInt32 = 1
DSPROVIDER_UNUSED_1: UInt32 = 2
DSPROVIDER_UNUSED_2: UInt32 = 4
DSPROVIDER_UNUSED_3: UInt32 = 8
DSPROVIDER_ADVANCED: UInt32 = 16
DSPROVIDER_AD_LDS: UInt32 = 32
CFSTR_DSOBJECTNAMES: String = 'DsObjectNames'
CFSTR_DS_DISPLAY_SPEC_OPTIONS: String = 'DsDisplaySpecOptions'
CFSTR_DSDISPLAYSPECOPTIONS: String = 'DsDisplaySpecOptions'
DS_PROP_SHELL_PREFIX: String = 'shell'
DS_PROP_ADMIN_PREFIX: String = 'admin'
DSDSOF_HASUSERANDSERVERINFO: UInt32 = 1
DSDSOF_SIMPLEAUTHENTICATE: UInt32 = 2
DSDSOF_DONTSIGNSEAL: UInt32 = 4
DSDSOF_DSAVAILABLE: UInt32 = 1073741824
CFSTR_DSPROPERTYPAGEINFO: String = 'DsPropPageInfo'
DSPROP_ATTRCHANGED_MSG: String = 'DsPropAttrChanged'
DBDTF_RETURNFQDN: UInt32 = 1
DBDTF_RETURNMIXEDDOMAINS: UInt32 = 2
DBDTF_RETURNEXTERNAL: UInt32 = 4
DBDTF_RETURNINBOUND: UInt32 = 8
DBDTF_RETURNINOUTBOUND: UInt32 = 16
DSSSF_SIMPLEAUTHENTICATE: UInt32 = 1
DSSSF_DONTSIGNSEAL: UInt32 = 2
DSSSF_DSAVAILABLE: UInt32 = 2147483648
DSGIF_ISNORMAL: UInt32 = 0
DSGIF_ISOPEN: UInt32 = 1
DSGIF_ISDISABLED: UInt32 = 2
DSGIF_ISMASK: UInt32 = 15
DSGIF_GETDEFAULTICON: UInt32 = 16
DSGIF_DEFAULTISCONTAINER: UInt32 = 32
DSICCF_IGNORETREATASLEAF: UInt32 = 1
DSECAF_NOTLISTED: UInt32 = 1
DSCCIF_HASWIZARDDIALOG: UInt32 = 1
DSCCIF_HASWIZARDPRIMARYPAGE: UInt32 = 2
DSBI_NOBUTTONS: UInt32 = 1
DSBI_NOLINES: UInt32 = 2
DSBI_NOLINESATROOT: UInt32 = 4
DSBI_CHECKBOXES: UInt32 = 256
DSBI_NOROOT: UInt32 = 65536
DSBI_INCLUDEHIDDEN: UInt32 = 131072
DSBI_EXPANDONOPEN: UInt32 = 262144
DSBI_ENTIREDIRECTORY: UInt32 = 589824
DSBI_RETURN_FORMAT: UInt32 = 1048576
DSBI_HASCREDENTIALS: UInt32 = 2097152
DSBI_IGNORETREATASLEAF: UInt32 = 4194304
DSBI_SIMPLEAUTHENTICATE: UInt32 = 8388608
DSBI_RETURNOBJECTCLASS: UInt32 = 16777216
DSBI_DONTSIGNSEAL: UInt32 = 33554432
DSB_MAX_DISPLAYNAME_CHARS: UInt32 = 64
DSBF_STATE: UInt32 = 1
DSBF_ICONLOCATION: UInt32 = 2
DSBF_DISPLAYNAME: UInt32 = 4
DSBS_CHECKED: UInt32 = 1
DSBS_HIDDEN: UInt32 = 2
DSBS_ROOT: UInt32 = 4
DSBM_QUERYINSERTW: UInt32 = 100
DSBM_QUERYINSERTA: UInt32 = 101
DSBM_QUERYINSERT: UInt32 = 100
DSBM_CHANGEIMAGESTATE: UInt32 = 102
DSBM_HELP: UInt32 = 103
DSBM_CONTEXTMENU: UInt32 = 104
DSBID_BANNER: UInt32 = 256
DSBID_CONTAINERLIST: UInt32 = 257
DS_FORCE_REDISCOVERY: UInt32 = 1
DS_DIRECTORY_SERVICE_REQUIRED: UInt32 = 16
DS_DIRECTORY_SERVICE_PREFERRED: UInt32 = 32
DS_GC_SERVER_REQUIRED: UInt32 = 64
DS_PDC_REQUIRED: UInt32 = 128
DS_BACKGROUND_ONLY: UInt32 = 256
DS_IP_REQUIRED: UInt32 = 512
DS_KDC_REQUIRED: UInt32 = 1024
DS_TIMESERV_REQUIRED: UInt32 = 2048
DS_WRITABLE_REQUIRED: UInt32 = 4096
DS_GOOD_TIMESERV_PREFERRED: UInt32 = 8192
DS_AVOID_SELF: UInt32 = 16384
DS_ONLY_LDAP_NEEDED: UInt32 = 32768
DS_IS_FLAT_NAME: UInt32 = 65536
DS_IS_DNS_NAME: UInt32 = 131072
DS_TRY_NEXTCLOSEST_SITE: UInt32 = 262144
DS_DIRECTORY_SERVICE_6_REQUIRED: UInt32 = 524288
DS_WEB_SERVICE_REQUIRED: UInt32 = 1048576
DS_DIRECTORY_SERVICE_8_REQUIRED: UInt32 = 2097152
DS_DIRECTORY_SERVICE_9_REQUIRED: UInt32 = 4194304
DS_DIRECTORY_SERVICE_10_REQUIRED: UInt32 = 8388608
DS_KEY_LIST_SUPPORT_REQUIRED: UInt32 = 16777216
DS_RETURN_DNS_NAME: UInt32 = 1073741824
DS_RETURN_FLAT_NAME: UInt32 = 2147483648
DS_PDC_FLAG: UInt32 = 1
DS_GC_FLAG: UInt32 = 4
DS_LDAP_FLAG: UInt32 = 8
DS_DS_FLAG: UInt32 = 16
DS_KDC_FLAG: UInt32 = 32
DS_TIMESERV_FLAG: UInt32 = 64
DS_CLOSEST_FLAG: UInt32 = 128
DS_WRITABLE_FLAG: UInt32 = 256
DS_GOOD_TIMESERV_FLAG: UInt32 = 512
DS_NDNC_FLAG: UInt32 = 1024
DS_SELECT_SECRET_DOMAIN_6_FLAG: UInt32 = 2048
DS_FULL_SECRET_DOMAIN_6_FLAG: UInt32 = 4096
DS_WS_FLAG: UInt32 = 8192
DS_DS_8_FLAG: UInt32 = 16384
DS_DS_9_FLAG: UInt32 = 32768
DS_DS_10_FLAG: UInt32 = 65536
DS_KEY_LIST_FLAG: UInt32 = 131072
DS_PING_FLAGS: UInt32 = 1048575
DS_DNS_CONTROLLER_FLAG: UInt32 = 536870912
DS_DNS_DOMAIN_FLAG: UInt32 = 1073741824
DS_DNS_FOREST_FLAG: UInt32 = 2147483648
DS_DOMAIN_IN_FOREST: UInt32 = 1
DS_DOMAIN_DIRECT_OUTBOUND: UInt32 = 2
DS_DOMAIN_TREE_ROOT: UInt32 = 4
DS_DOMAIN_PRIMARY: UInt32 = 8
DS_DOMAIN_NATIVE_MODE: UInt32 = 16
DS_DOMAIN_DIRECT_INBOUND: UInt32 = 32
DS_GFTI_UPDATE_TDO: UInt32 = 1
DS_GFTI_VALID_FLAGS: UInt32 = 1
DS_ONLY_DO_SITE_NAME: UInt32 = 1
DS_NOTIFY_AFTER_SITE_RECORDS: UInt32 = 2
CLSID_DsQuery: Guid = Guid('{8a23e65e-31c2-11d0-891c-00a024ab2dbb}')
CLSID_DsFindObjects: Guid = Guid('{83ee3fe1-57d9-11d0-b932-00a024ab2dbb}')
CLSID_DsFindPeople: Guid = Guid('{83ee3fe2-57d9-11d0-b932-00a024ab2dbb}')
CLSID_DsFindPrinter: Guid = Guid('{b577f070-7ee2-11d0-913f-00aa00c16e65}')
CLSID_DsFindComputer: Guid = Guid('{16006700-87ad-11d0-9140-00aa00c16e65}')
CLSID_DsFindVolume: Guid = Guid('{c1b3cbf1-886a-11d0-9140-00aa00c16e65}')
CLSID_DsFindContainer: Guid = Guid('{c1b3cbf2-886a-11d0-9140-00aa00c16e65}')
CLSID_DsFindAdvanced: Guid = Guid('{83ee3fe3-57d9-11d0-b932-00a024ab2dbb}')
CLSID_DsFindDomainController: Guid = Guid('{538c7b7e-d25e-11d0-9742-00a0c906af45}')
CLSID_DsFindWriteableDomainController: Guid = Guid('{7cbef079-aa84-444b-bc70-68e41283eabc}')
CLSID_DsFindFrsMembers: Guid = Guid('{94ce4b18-b3d3-11d1-b9b4-00c04fd8d5b0}')
DSQPF_NOSAVE: UInt32 = 1
DSQPF_SAVELOCATION: UInt32 = 2
DSQPF_SHOWHIDDENOBJECTS: UInt32 = 4
DSQPF_ENABLEADMINFEATURES: UInt32 = 8
DSQPF_ENABLEADVANCEDFEATURES: UInt32 = 16
DSQPF_HASCREDENTIALS: UInt32 = 32
DSQPF_NOCHOOSECOLUMNS: UInt32 = 64
CFSTR_DSQUERYPARAMS: String = 'DsQueryParameters'
CFSTR_DSQUERYSCOPE: String = 'DsQueryScope'
DSQPM_GETCLASSLIST: UInt32 = 268435456
DSQPM_HELPTOPICS: UInt32 = 268435457
DSROLE_PRIMARY_DS_RUNNING: UInt32 = 1
DSROLE_PRIMARY_DS_MIXED_MODE: UInt32 = 2
DSROLE_UPGRADE_IN_PROGRESS: UInt32 = 4
DSROLE_PRIMARY_DS_READONLY: UInt32 = 8
DSROLE_PRIMARY_DOMAIN_GUID_PRESENT: UInt32 = 16777216
ADS_ATTR_CLEAR: UInt32 = 1
ADS_ATTR_UPDATE: UInt32 = 2
ADS_ATTR_APPEND: UInt32 = 3
ADS_ATTR_DELETE: UInt32 = 4
ADS_EXT_MINEXTDISPID: UInt32 = 1
ADS_EXT_MAXEXTDISPID: UInt32 = 16777215
ADS_EXT_INITCREDENTIALS: UInt32 = 1
ADS_EXT_INITIALIZE_COMPLETE: UInt32 = 2
DS_BEHAVIOR_WIN2000: UInt32 = 0
DS_BEHAVIOR_WIN2003_WITH_MIXED_DOMAINS: UInt32 = 1
DS_BEHAVIOR_WIN2003: UInt32 = 2
DS_BEHAVIOR_WIN2008: UInt32 = 3
DS_BEHAVIOR_WIN2008R2: UInt32 = 4
DS_BEHAVIOR_WIN2012: UInt32 = 5
DS_BEHAVIOR_WIN2012R2: UInt32 = 6
DS_BEHAVIOR_WIN2016: UInt32 = 7
DS_BEHAVIOR_LONGHORN: UInt32 = 3
DS_BEHAVIOR_WIN7: UInt32 = 4
DS_BEHAVIOR_WIN8: UInt32 = 5
DS_BEHAVIOR_WINBLUE: UInt32 = 6
DS_BEHAVIOR_WINTHRESHOLD: UInt32 = 7
DS_SYNCED_EVENT_NAME: String = 'NTDSInitialSyncsCompleted'
DS_SYNCED_EVENT_NAME_W: String = 'NTDSInitialSyncsCompleted'
ACTRL_DS_OPEN: UInt32 = 0
ACTRL_DS_CREATE_CHILD: UInt32 = 1
ACTRL_DS_DELETE_CHILD: UInt32 = 2
ACTRL_DS_LIST: UInt32 = 4
ACTRL_DS_SELF: UInt32 = 8
ACTRL_DS_READ_PROP: UInt32 = 16
ACTRL_DS_WRITE_PROP: UInt32 = 32
ACTRL_DS_DELETE_TREE: UInt32 = 64
ACTRL_DS_LIST_OBJECT: UInt32 = 128
ACTRL_DS_CONTROL_ACCESS: UInt32 = 256
NTDSAPI_BIND_ALLOW_DELEGATION: UInt32 = 1
NTDSAPI_BIND_FIND_BINDING: UInt32 = 2
NTDSAPI_BIND_FORCE_KERBEROS: UInt32 = 4
DS_REPSYNC_ASYNCHRONOUS_OPERATION: UInt32 = 1
DS_REPSYNC_WRITEABLE: UInt32 = 2
DS_REPSYNC_PERIODIC: UInt32 = 4
DS_REPSYNC_INTERSITE_MESSAGING: UInt32 = 8
DS_REPSYNC_FULL: UInt32 = 32
DS_REPSYNC_URGENT: UInt32 = 64
DS_REPSYNC_NO_DISCARD: UInt32 = 128
DS_REPSYNC_FORCE: UInt32 = 256
DS_REPSYNC_ADD_REFERENCE: UInt32 = 512
DS_REPSYNC_NEVER_COMPLETED: UInt32 = 1024
DS_REPSYNC_TWO_WAY: UInt32 = 2048
DS_REPSYNC_NEVER_NOTIFY: UInt32 = 4096
DS_REPSYNC_INITIAL: UInt32 = 8192
DS_REPSYNC_USE_COMPRESSION: UInt32 = 16384
DS_REPSYNC_ABANDONED: UInt32 = 32768
DS_REPSYNC_SELECT_SECRETS: UInt32 = 32768
DS_REPSYNC_INITIAL_IN_PROGRESS: UInt32 = 65536
DS_REPSYNC_PARTIAL_ATTRIBUTE_SET: UInt32 = 131072
DS_REPSYNC_REQUEUE: UInt32 = 262144
DS_REPSYNC_NOTIFICATION: UInt32 = 524288
DS_REPSYNC_ASYNCHRONOUS_REPLICA: UInt32 = 1048576
DS_REPSYNC_CRITICAL: UInt32 = 2097152
DS_REPSYNC_FULL_IN_PROGRESS: UInt32 = 4194304
DS_REPSYNC_PREEMPTED: UInt32 = 8388608
DS_REPSYNC_NONGC_RO_REPLICA: UInt32 = 16777216
DS_REPADD_ASYNCHRONOUS_OPERATION: UInt32 = 1
DS_REPADD_WRITEABLE: UInt32 = 2
DS_REPADD_INITIAL: UInt32 = 4
DS_REPADD_PERIODIC: UInt32 = 8
DS_REPADD_INTERSITE_MESSAGING: UInt32 = 16
DS_REPADD_ASYNCHRONOUS_REPLICA: UInt32 = 32
DS_REPADD_DISABLE_NOTIFICATION: UInt32 = 64
DS_REPADD_DISABLE_PERIODIC: UInt32 = 128
DS_REPADD_USE_COMPRESSION: UInt32 = 256
DS_REPADD_NEVER_NOTIFY: UInt32 = 512
DS_REPADD_TWO_WAY: UInt32 = 1024
DS_REPADD_CRITICAL: UInt32 = 2048
DS_REPADD_SELECT_SECRETS: UInt32 = 4096
DS_REPADD_NONGC_RO_REPLICA: UInt32 = 16777216
DS_REPDEL_ASYNCHRONOUS_OPERATION: UInt32 = 1
DS_REPDEL_WRITEABLE: UInt32 = 2
DS_REPDEL_INTERSITE_MESSAGING: UInt32 = 4
DS_REPDEL_IGNORE_ERRORS: UInt32 = 8
DS_REPDEL_LOCAL_ONLY: UInt32 = 16
DS_REPDEL_NO_SOURCE: UInt32 = 32
DS_REPDEL_REF_OK: UInt32 = 64
DS_REPMOD_ASYNCHRONOUS_OPERATION: UInt32 = 1
DS_REPMOD_WRITEABLE: UInt32 = 2
DS_REPMOD_UPDATE_FLAGS: UInt32 = 1
DS_REPMOD_UPDATE_INSTANCE: UInt32 = 2
DS_REPMOD_UPDATE_ADDRESS: UInt32 = 2
DS_REPMOD_UPDATE_SCHEDULE: UInt32 = 4
DS_REPMOD_UPDATE_RESULT: UInt32 = 8
DS_REPMOD_UPDATE_TRANSPORT: UInt32 = 16
DS_REPUPD_ASYNCHRONOUS_OPERATION: UInt32 = 1
DS_REPUPD_WRITEABLE: UInt32 = 2
DS_REPUPD_ADD_REFERENCE: UInt32 = 4
DS_REPUPD_DELETE_REFERENCE: UInt32 = 8
DS_REPUPD_REFERENCE_GCSPN: UInt32 = 16
DS_INSTANCETYPE_IS_NC_HEAD: UInt32 = 1
DS_INSTANCETYPE_NC_IS_WRITEABLE: UInt32 = 4
DS_INSTANCETYPE_NC_COMING: UInt32 = 16
DS_INSTANCETYPE_NC_GOING: UInt32 = 32
NTDSDSA_OPT_IS_GC: UInt32 = 1
NTDSDSA_OPT_DISABLE_INBOUND_REPL: UInt32 = 2
NTDSDSA_OPT_DISABLE_OUTBOUND_REPL: UInt32 = 4
NTDSDSA_OPT_DISABLE_NTDSCONN_XLATE: UInt32 = 8
NTDSDSA_OPT_DISABLE_SPN_REGISTRATION: UInt32 = 16
NTDSDSA_OPT_GENERATE_OWN_TOPO: UInt32 = 32
NTDSDSA_OPT_BLOCK_RPC: UInt32 = 64
NTDSCONN_OPT_IS_GENERATED: UInt32 = 1
NTDSCONN_OPT_TWOWAY_SYNC: UInt32 = 2
NTDSCONN_OPT_OVERRIDE_NOTIFY_DEFAULT: UInt32 = 4
NTDSCONN_OPT_USE_NOTIFY: UInt32 = 8
NTDSCONN_OPT_DISABLE_INTERSITE_COMPRESSION: UInt32 = 16
NTDSCONN_OPT_USER_OWNED_SCHEDULE: UInt32 = 32
NTDSCONN_OPT_RODC_TOPOLOGY: UInt32 = 64
NTDSCONN_KCC_NO_REASON: UInt32 = 0
NTDSCONN_KCC_GC_TOPOLOGY: UInt32 = 1
NTDSCONN_KCC_RING_TOPOLOGY: UInt32 = 2
NTDSCONN_KCC_MINIMIZE_HOPS_TOPOLOGY: UInt32 = 4
NTDSCONN_KCC_STALE_SERVERS_TOPOLOGY: UInt32 = 8
NTDSCONN_KCC_OSCILLATING_CONNECTION_TOPOLOGY: UInt32 = 16
NTDSCONN_KCC_INTERSITE_GC_TOPOLOGY: UInt32 = 32
NTDSCONN_KCC_INTERSITE_TOPOLOGY: UInt32 = 64
NTDSCONN_KCC_SERVER_FAILOVER_TOPOLOGY: UInt32 = 128
NTDSCONN_KCC_SITE_FAILOVER_TOPOLOGY: UInt32 = 256
NTDSCONN_KCC_REDUNDANT_SERVER_TOPOLOGY: UInt32 = 512
FRSCONN_PRIORITY_MASK: UInt32 = 1879048192
FRSCONN_MAX_PRIORITY: UInt32 = 8
NTDSCONN_OPT_IGNORE_SCHEDULE_MASK: UInt32 = 2147483648
NTDSSETTINGS_OPT_IS_AUTO_TOPOLOGY_DISABLED: UInt32 = 1
NTDSSETTINGS_OPT_IS_TOPL_CLEANUP_DISABLED: UInt32 = 2
NTDSSETTINGS_OPT_IS_TOPL_MIN_HOPS_DISABLED: UInt32 = 4
NTDSSETTINGS_OPT_IS_TOPL_DETECT_STALE_DISABLED: UInt32 = 8
NTDSSETTINGS_OPT_IS_INTER_SITE_AUTO_TOPOLOGY_DISABLED: UInt32 = 16
NTDSSETTINGS_OPT_IS_GROUP_CACHING_ENABLED: UInt32 = 32
NTDSSETTINGS_OPT_FORCE_KCC_WHISTLER_BEHAVIOR: UInt32 = 64
NTDSSETTINGS_OPT_FORCE_KCC_W2K_ELECTION: UInt32 = 128
NTDSSETTINGS_OPT_IS_RAND_BH_SELECTION_DISABLED: UInt32 = 256
NTDSSETTINGS_OPT_IS_SCHEDULE_HASHING_ENABLED: UInt32 = 512
NTDSSETTINGS_OPT_IS_REDUNDANT_SERVER_TOPOLOGY_ENABLED: UInt32 = 1024
NTDSSETTINGS_OPT_W2K3_IGNORE_SCHEDULES: UInt32 = 2048
NTDSSETTINGS_OPT_W2K3_BRIDGES_REQUIRED: UInt32 = 4096
NTDSSETTINGS_DEFAULT_SERVER_REDUNDANCY: UInt32 = 2
NTDSTRANSPORT_OPT_IGNORE_SCHEDULES: UInt32 = 1
NTDSTRANSPORT_OPT_BRIDGES_REQUIRED: UInt32 = 2
NTDSSITECONN_OPT_USE_NOTIFY: UInt32 = 1
NTDSSITECONN_OPT_TWOWAY_SYNC: UInt32 = 2
NTDSSITECONN_OPT_DISABLE_COMPRESSION: UInt32 = 4
NTDSSITELINK_OPT_USE_NOTIFY: UInt32 = 1
NTDSSITELINK_OPT_TWOWAY_SYNC: UInt32 = 2
NTDSSITELINK_OPT_DISABLE_COMPRESSION: UInt32 = 4
GUID_USERS_CONTAINER_A: String = 'a9d1ca15768811d1aded00c04fd8d5cd'
GUID_COMPUTRS_CONTAINER_A: String = 'aa312825768811d1aded00c04fd8d5cd'
GUID_SYSTEMS_CONTAINER_A: String = 'ab1d30f3768811d1aded00c04fd8d5cd'
GUID_DOMAIN_CONTROLLERS_CONTAINER_A: String = 'a361b2ffffd211d1aa4b00c04fd7d83a'
GUID_INFRASTRUCTURE_CONTAINER_A: String = '2fbac1870ade11d297c400c04fd8d5cd'
GUID_DELETED_OBJECTS_CONTAINER_A: String = '18e2ea80684f11d2b9aa00c04f79f805'
GUID_LOSTANDFOUND_CONTAINER_A: String = 'ab8153b7768811d1aded00c04fd8d5cd'
GUID_FOREIGNSECURITYPRINCIPALS_CONTAINER_A: String = '22b70c67d56e4efb91e9300fca3dc1aa'
GUID_PROGRAM_DATA_CONTAINER_A: String = '09460c08ae1e4a4ea0f64aee7daa1e5a'
GUID_MICROSOFT_PROGRAM_DATA_CONTAINER_A: String = 'f4be92a4c777485e878e9421d53087db'
GUID_NTDS_QUOTAS_CONTAINER_A: String = '6227f0af1fc2410d8e3bb10615bb5b0f'
GUID_USERS_CONTAINER_W: String = 'a9d1ca15768811d1aded00c04fd8d5cd'
GUID_COMPUTRS_CONTAINER_W: String = 'aa312825768811d1aded00c04fd8d5cd'
GUID_SYSTEMS_CONTAINER_W: String = 'ab1d30f3768811d1aded00c04fd8d5cd'
GUID_DOMAIN_CONTROLLERS_CONTAINER_W: String = 'a361b2ffffd211d1aa4b00c04fd7d83a'
GUID_INFRASTRUCTURE_CONTAINER_W: String = '2fbac1870ade11d297c400c04fd8d5cd'
GUID_DELETED_OBJECTS_CONTAINER_W: String = '18e2ea80684f11d2b9aa00c04f79f805'
GUID_LOSTANDFOUND_CONTAINER_W: String = 'ab8153b7768811d1aded00c04fd8d5cd'
GUID_FOREIGNSECURITYPRINCIPALS_CONTAINER_W: String = '22b70c67d56e4efb91e9300fca3dc1aa'
GUID_PROGRAM_DATA_CONTAINER_W: String = '09460c08ae1e4a4ea0f64aee7daa1e5a'
GUID_MICROSOFT_PROGRAM_DATA_CONTAINER_W: String = 'f4be92a4c777485e878e9421d53087db'
GUID_NTDS_QUOTAS_CONTAINER_W: String = '6227f0af1fc2410d8e3bb10615bb5b0f'
GUID_MANAGED_SERVICE_ACCOUNTS_CONTAINER_W: String = '1EB93889E40C45DF9F0C64D23BBB6237'
GUID_KEYS_CONTAINER_W: String = '683A24E2E8164BD3AF86AC3C2CF3F981'
DS_REPSYNCALL_NO_OPTIONS: UInt32 = 0
DS_REPSYNCALL_ABORT_IF_SERVER_UNAVAILABLE: UInt32 = 1
DS_REPSYNCALL_SYNC_ADJACENT_SERVERS_ONLY: UInt32 = 2
DS_REPSYNCALL_ID_SERVERS_BY_DN: UInt32 = 4
DS_REPSYNCALL_DO_NOT_SYNC: UInt32 = 8
DS_REPSYNCALL_SKIP_INITIAL_CHECK: UInt32 = 16
DS_REPSYNCALL_PUSH_CHANGES_OUTWARD: UInt32 = 32
DS_REPSYNCALL_CROSS_SITE_BOUNDARIES: UInt32 = 64
DS_LIST_DSA_OBJECT_FOR_SERVER: UInt32 = 0
DS_LIST_DNS_HOST_NAME_FOR_SERVER: UInt32 = 1
DS_LIST_ACCOUNT_OBJECT_FOR_SERVER: UInt32 = 2
DS_ROLE_SCHEMA_OWNER: UInt32 = 0
DS_ROLE_DOMAIN_OWNER: UInt32 = 1
DS_ROLE_PDC_OWNER: UInt32 = 2
DS_ROLE_RID_OWNER: UInt32 = 3
DS_ROLE_INFRASTRUCTURE_OWNER: UInt32 = 4
DS_SCHEMA_GUID_NOT_FOUND: UInt32 = 0
DS_SCHEMA_GUID_ATTR: UInt32 = 1
DS_SCHEMA_GUID_ATTR_SET: UInt32 = 2
DS_SCHEMA_GUID_CLASS: UInt32 = 3
DS_SCHEMA_GUID_CONTROL_RIGHT: UInt32 = 4
DS_KCC_FLAG_ASYNC_OP: UInt32 = 1
DS_KCC_FLAG_DAMPED: UInt32 = 2
DS_EXIST_ADVISORY_MODE: UInt32 = 1
DS_REPL_INFO_FLAG_IMPROVE_LINKED_ATTRS: UInt32 = 1
DS_REPL_NBR_WRITEABLE: UInt32 = 16
DS_REPL_NBR_SYNC_ON_STARTUP: UInt32 = 32
DS_REPL_NBR_DO_SCHEDULED_SYNCS: UInt32 = 64
DS_REPL_NBR_USE_ASYNC_INTERSITE_TRANSPORT: UInt32 = 128
DS_REPL_NBR_TWO_WAY_SYNC: UInt32 = 512
DS_REPL_NBR_NONGC_RO_REPLICA: UInt32 = 1024
DS_REPL_NBR_RETURN_OBJECT_PARENTS: UInt32 = 2048
DS_REPL_NBR_SELECT_SECRETS: UInt32 = 4096
DS_REPL_NBR_FULL_SYNC_IN_PROGRESS: UInt32 = 65536
DS_REPL_NBR_FULL_SYNC_NEXT_PACKET: UInt32 = 131072
DS_REPL_NBR_GCSPN: UInt32 = 1048576
DS_REPL_NBR_NEVER_SYNCED: UInt32 = 2097152
DS_REPL_NBR_PREEMPTED: UInt32 = 16777216
DS_REPL_NBR_IGNORE_CHANGE_NOTIFICATIONS: UInt32 = 67108864
DS_REPL_NBR_DISABLE_SCHEDULED_SYNC: UInt32 = 134217728
DS_REPL_NBR_COMPRESS_CHANGES: UInt32 = 268435456
DS_REPL_NBR_NO_CHANGE_NOTIFICATIONS: UInt32 = 536870912
DS_REPL_NBR_PARTIAL_ATTRIBUTE_SET: UInt32 = 1073741824
ADAM_SCP_SITE_NAME_STRING: String = 'site:'
ADAM_SCP_SITE_NAME_STRING_W: String = 'site:'
ADAM_SCP_PARTITION_STRING: String = 'partition:'
ADAM_SCP_PARTITION_STRING_W: String = 'partition:'
ADAM_SCP_INSTANCE_NAME_STRING: String = 'instance:'
ADAM_SCP_INSTANCE_NAME_STRING_W: String = 'instance:'
ADAM_SCP_FSMO_STRING: String = 'fsmo:'
ADAM_SCP_FSMO_STRING_W: String = 'fsmo:'
ADAM_SCP_FSMO_NAMING_STRING: String = 'naming'
ADAM_SCP_FSMO_NAMING_STRING_W: String = 'naming'
ADAM_SCP_FSMO_SCHEMA_STRING: String = 'schema'
ADAM_SCP_FSMO_SCHEMA_STRING_W: String = 'schema'
ADAM_REPL_AUTHENTICATION_MODE_NEGOTIATE_PASS_THROUGH: UInt32 = 0
ADAM_REPL_AUTHENTICATION_MODE_NEGOTIATE: UInt32 = 1
ADAM_REPL_AUTHENTICATION_MODE_MUTUAL_AUTH_REQUIRED: UInt32 = 2
FLAG_FOREST_OPTIONAL_FEATURE: UInt32 = 1
FLAG_DOMAIN_OPTIONAL_FEATURE: UInt32 = 2
FLAG_DISABLABLE_OPTIONAL_FEATURE: UInt32 = 4
FLAG_SERVER_OPTIONAL_FEATURE: UInt32 = 8
GUID_RECYCLE_BIN_OPTIONAL_FEATURE_A: String = 'd8dc6d76d0ac5e44f3b9a7f9b6744f2a'
GUID_RECYCLE_BIN_OPTIONAL_FEATURE_W: String = 'd8dc6d76d0ac5e44f3b9a7f9b6744f2a'
GUID_PRIVILEGED_ACCESS_MANAGEMENT_OPTIONAL_FEATURE_A: String = '73e843ece8cc4046b4ab07ffe4ab5bcd'
GUID_PRIVILEGED_ACCESS_MANAGEMENT_OPTIONAL_FEATURE_W: String = '73e843ece8cc4046b4ab07ffe4ab5bcd'
CFSTR_DSOP_DS_SELECTION_LIST: String = 'CFSTR_DSOP_DS_SELECTION_LIST'
DSOP_SCOPE_TYPE_TARGET_COMPUTER: UInt32 = 1
DSOP_SCOPE_TYPE_UPLEVEL_JOINED_DOMAIN: UInt32 = 2
DSOP_SCOPE_TYPE_DOWNLEVEL_JOINED_DOMAIN: UInt32 = 4
DSOP_SCOPE_TYPE_ENTERPRISE_DOMAIN: UInt32 = 8
DSOP_SCOPE_TYPE_GLOBAL_CATALOG: UInt32 = 16
DSOP_SCOPE_TYPE_EXTERNAL_UPLEVEL_DOMAIN: UInt32 = 32
DSOP_SCOPE_TYPE_EXTERNAL_DOWNLEVEL_DOMAIN: UInt32 = 64
DSOP_SCOPE_TYPE_WORKGROUP: UInt32 = 128
DSOP_SCOPE_TYPE_USER_ENTERED_UPLEVEL_SCOPE: UInt32 = 256
DSOP_SCOPE_TYPE_USER_ENTERED_DOWNLEVEL_SCOPE: UInt32 = 512
DSOP_SCOPE_FLAG_STARTING_SCOPE: UInt32 = 1
DSOP_SCOPE_FLAG_WANT_PROVIDER_WINNT: UInt32 = 2
DSOP_SCOPE_FLAG_WANT_PROVIDER_LDAP: UInt32 = 4
DSOP_SCOPE_FLAG_WANT_PROVIDER_GC: UInt32 = 8
DSOP_SCOPE_FLAG_WANT_SID_PATH: UInt32 = 16
DSOP_SCOPE_FLAG_WANT_DOWNLEVEL_BUILTIN_PATH: UInt32 = 32
DSOP_SCOPE_FLAG_DEFAULT_FILTER_USERS: UInt32 = 64
DSOP_SCOPE_FLAG_DEFAULT_FILTER_GROUPS: UInt32 = 128
DSOP_SCOPE_FLAG_DEFAULT_FILTER_COMPUTERS: UInt32 = 256
DSOP_SCOPE_FLAG_DEFAULT_FILTER_CONTACTS: UInt32 = 512
DSOP_SCOPE_FLAG_DEFAULT_FILTER_SERVICE_ACCOUNTS: UInt32 = 1024
DSOP_SCOPE_FLAG_DEFAULT_FILTER_PASSWORDSETTINGS_OBJECTS: UInt32 = 2048
DSOP_FILTER_INCLUDE_ADVANCED_VIEW: UInt32 = 1
DSOP_FILTER_USERS: UInt32 = 2
DSOP_FILTER_BUILTIN_GROUPS: UInt32 = 4
DSOP_FILTER_WELL_KNOWN_PRINCIPALS: UInt32 = 8
DSOP_FILTER_UNIVERSAL_GROUPS_DL: UInt32 = 16
DSOP_FILTER_UNIVERSAL_GROUPS_SE: UInt32 = 32
DSOP_FILTER_GLOBAL_GROUPS_DL: UInt32 = 64
DSOP_FILTER_GLOBAL_GROUPS_SE: UInt32 = 128
DSOP_FILTER_DOMAIN_LOCAL_GROUPS_DL: UInt32 = 256
DSOP_FILTER_DOMAIN_LOCAL_GROUPS_SE: UInt32 = 512
DSOP_FILTER_CONTACTS: UInt32 = 1024
DSOP_FILTER_COMPUTERS: UInt32 = 2048
DSOP_FILTER_SERVICE_ACCOUNTS: UInt32 = 4096
DSOP_FILTER_PASSWORDSETTINGS_OBJECTS: UInt32 = 8192
DSOP_DOWNLEVEL_FILTER_USERS: UInt32 = 2147483649
DSOP_DOWNLEVEL_FILTER_LOCAL_GROUPS: UInt32 = 2147483650
DSOP_DOWNLEVEL_FILTER_GLOBAL_GROUPS: UInt32 = 2147483652
DSOP_DOWNLEVEL_FILTER_COMPUTERS: UInt32 = 2147483656
DSOP_DOWNLEVEL_FILTER_WORLD: UInt32 = 2147483664
DSOP_DOWNLEVEL_FILTER_AUTHENTICATED_USER: UInt32 = 2147483680
DSOP_DOWNLEVEL_FILTER_ANONYMOUS: UInt32 = 2147483712
DSOP_DOWNLEVEL_FILTER_BATCH: UInt32 = 2147483776
DSOP_DOWNLEVEL_FILTER_CREATOR_OWNER: UInt32 = 2147483904
DSOP_DOWNLEVEL_FILTER_CREATOR_GROUP: UInt32 = 2147484160
DSOP_DOWNLEVEL_FILTER_DIALUP: UInt32 = 2147484672
DSOP_DOWNLEVEL_FILTER_INTERACTIVE: UInt32 = 2147485696
DSOP_DOWNLEVEL_FILTER_NETWORK: UInt32 = 2147487744
DSOP_DOWNLEVEL_FILTER_SERVICE: UInt32 = 2147491840
DSOP_DOWNLEVEL_FILTER_SYSTEM: UInt32 = 2147500032
DSOP_DOWNLEVEL_FILTER_EXCLUDE_BUILTIN_GROUPS: UInt32 = 2147516416
DSOP_DOWNLEVEL_FILTER_TERMINAL_SERVER: UInt32 = 2147549184
DSOP_DOWNLEVEL_FILTER_ALL_WELLKNOWN_SIDS: UInt32 = 2147614720
DSOP_DOWNLEVEL_FILTER_LOCAL_SERVICE: UInt32 = 2147745792
DSOP_DOWNLEVEL_FILTER_NETWORK_SERVICE: UInt32 = 2148007936
DSOP_DOWNLEVEL_FILTER_REMOTE_LOGON: UInt32 = 2148532224
DSOP_DOWNLEVEL_FILTER_INTERNET_USER: UInt32 = 2149580800
DSOP_DOWNLEVEL_FILTER_OWNER_RIGHTS: UInt32 = 2151677952
DSOP_DOWNLEVEL_FILTER_SERVICES: UInt32 = 2155872256
DSOP_DOWNLEVEL_FILTER_LOCAL_LOGON: UInt32 = 2164260864
DSOP_DOWNLEVEL_FILTER_THIS_ORG_CERT: UInt32 = 2181038080
DSOP_DOWNLEVEL_FILTER_IIS_APP_POOL: UInt32 = 2214592512
DSOP_DOWNLEVEL_FILTER_ALL_APP_PACKAGES: UInt32 = 2281701376
DSOP_DOWNLEVEL_FILTER_LOCAL_ACCOUNTS: UInt32 = 2415919104
DSOP_FLAG_MULTISELECT: UInt32 = 1
DSOP_FLAG_SKIP_TARGET_COMPUTER_DC_CHECK: UInt32 = 2
SCHEDULE_INTERVAL: UInt32 = 0
SCHEDULE_BANDWIDTH: UInt32 = 1
SCHEDULE_PRIORITY: UInt32 = 2
FACILITY_NTDSB: UInt32 = 2048
FACILITY_BACKUP: UInt32 = 2047
FACILITY_SYSTEM: UInt32 = 0
hrNone: win32more.Windows.Win32.Foundation.HRESULT = 0
hrNyi: win32more.Windows.Win32.Foundation.HRESULT = -1073741823
hrInvalidParam: win32more.Windows.Win32.Foundation.HRESULT = -939589631
hrError: win32more.Windows.Win32.Foundation.HRESULT = -939589630
hrInvalidHandle: win32more.Windows.Win32.Foundation.HRESULT = -939589629
hrRestoreInProgress: win32more.Windows.Win32.Foundation.HRESULT = -939589628
hrAlreadyOpen: win32more.Windows.Win32.Foundation.HRESULT = -939589627
hrInvalidRecips: win32more.Windows.Win32.Foundation.HRESULT = -939589626
hrCouldNotConnect: win32more.Windows.Win32.Foundation.HRESULT = -939589625
hrRestoreMapExists: win32more.Windows.Win32.Foundation.HRESULT = -939589624
hrIncrementalBackupDisabled: win32more.Windows.Win32.Foundation.HRESULT = -939589623
hrLogFileNotFound: win32more.Windows.Win32.Foundation.HRESULT = -939589622
hrCircularLogging: win32more.Windows.Win32.Foundation.HRESULT = -939589621
hrNoFullRestore: win32more.Windows.Win32.Foundation.HRESULT = -939589620
hrCommunicationError: win32more.Windows.Win32.Foundation.HRESULT = -939589619
hrFullBackupNotTaken: win32more.Windows.Win32.Foundation.HRESULT = -939589618
hrMissingExpiryToken: win32more.Windows.Win32.Foundation.HRESULT = -939589617
hrUnknownExpiryTokenFormat: win32more.Windows.Win32.Foundation.HRESULT = -939589616
hrContentsExpired: win32more.Windows.Win32.Foundation.HRESULT = -939589615
hrFileClose: win32more.Windows.Win32.Foundation.HRESULT = -939523994
hrOutOfThreads: win32more.Windows.Win32.Foundation.HRESULT = -939523993
hrTooManyIO: win32more.Windows.Win32.Foundation.HRESULT = -939523991
hrBFNotSynchronous: win32more.Windows.Win32.Foundation.HRESULT = -2013265720
hrBFPageNotFound: win32more.Windows.Win32.Foundation.HRESULT = -2013265719
hrBFInUse: win32more.Windows.Win32.Foundation.HRESULT = -939523894
hrPMRecDeleted: win32more.Windows.Win32.Foundation.HRESULT = -939523794
hrRemainingVersions: win32more.Windows.Win32.Foundation.HRESULT = -2013265599
hrFLDKeyTooBig: win32more.Windows.Win32.Foundation.HRESULT = -2013265520
hrFLDTooManySegments: win32more.Windows.Win32.Foundation.HRESULT = -939523695
hrFLDNullKey: win32more.Windows.Win32.Foundation.HRESULT = -2013265518
hrLogFileCorrupt: win32more.Windows.Win32.Foundation.HRESULT = -939523595
hrNoBackupDirectory: win32more.Windows.Win32.Foundation.HRESULT = -939523593
hrBackupDirectoryNotEmpty: win32more.Windows.Win32.Foundation.HRESULT = -939523592
hrBackupInProgress: win32more.Windows.Win32.Foundation.HRESULT = -939523591
hrMissingPreviousLogFile: win32more.Windows.Win32.Foundation.HRESULT = -939523587
hrLogWriteFail: win32more.Windows.Win32.Foundation.HRESULT = -939523586
hrBadLogVersion: win32more.Windows.Win32.Foundation.HRESULT = -939523582
hrInvalidLogSequence: win32more.Windows.Win32.Foundation.HRESULT = -939523581
hrLoggingDisabled: win32more.Windows.Win32.Foundation.HRESULT = -939523580
hrLogBufferTooSmall: win32more.Windows.Win32.Foundation.HRESULT = -939523579
hrLogSequenceEnd: win32more.Windows.Win32.Foundation.HRESULT = -939523577
hrNoBackup: win32more.Windows.Win32.Foundation.HRESULT = -939523576
hrInvalidBackupSequence: win32more.Windows.Win32.Foundation.HRESULT = -939523575
hrBackupNotAllowedYet: win32more.Windows.Win32.Foundation.HRESULT = -939523573
hrDeleteBackupFileFail: win32more.Windows.Win32.Foundation.HRESULT = -939523572
hrMakeBackupDirectoryFail: win32more.Windows.Win32.Foundation.HRESULT = -939523571
hrInvalidBackup: win32more.Windows.Win32.Foundation.HRESULT = -939523570
hrRecoveredWithErrors: win32more.Windows.Win32.Foundation.HRESULT = -939523569
hrMissingLogFile: win32more.Windows.Win32.Foundation.HRESULT = -939523568
hrLogDiskFull: win32more.Windows.Win32.Foundation.HRESULT = -939523567
hrBadLogSignature: win32more.Windows.Win32.Foundation.HRESULT = -939523566
hrBadDbSignature: win32more.Windows.Win32.Foundation.HRESULT = -939523565
hrBadCheckpointSignature: win32more.Windows.Win32.Foundation.HRESULT = -939523564
hrCheckpointCorrupt: win32more.Windows.Win32.Foundation.HRESULT = -939523563
hrDatabaseInconsistent: win32more.Windows.Win32.Foundation.HRESULT = -939523546
hrConsistentTimeMismatch: win32more.Windows.Win32.Foundation.HRESULT = -939523545
hrPatchFileMismatch: win32more.Windows.Win32.Foundation.HRESULT = -939523544
hrRestoreLogTooLow: win32more.Windows.Win32.Foundation.HRESULT = -939523543
hrRestoreLogTooHigh: win32more.Windows.Win32.Foundation.HRESULT = -939523542
hrGivenLogFileHasBadSignature: win32more.Windows.Win32.Foundation.HRESULT = -939523541
hrGivenLogFileIsNotContiguous: win32more.Windows.Win32.Foundation.HRESULT = -939523540
hrMissingRestoreLogFiles: win32more.Windows.Win32.Foundation.HRESULT = -939523539
hrExistingLogFileHasBadSignature: win32more.Windows.Win32.Foundation.HRESULT = -2013265362
hrExistingLogFileIsNotContiguous: win32more.Windows.Win32.Foundation.HRESULT = -2013265361
hrMissingFullBackup: win32more.Windows.Win32.Foundation.HRESULT = -939523536
hrBadBackupDatabaseSize: win32more.Windows.Win32.Foundation.HRESULT = -939523535
hrTermInProgress: win32more.Windows.Win32.Foundation.HRESULT = -939523096
hrFeatureNotAvailable: win32more.Windows.Win32.Foundation.HRESULT = -939523095
hrInvalidName: win32more.Windows.Win32.Foundation.HRESULT = -939523094
hrInvalidParameter: win32more.Windows.Win32.Foundation.HRESULT = -939523093
hrColumnNull: win32more.Windows.Win32.Foundation.HRESULT = -2013264916
hrBufferTruncated: win32more.Windows.Win32.Foundation.HRESULT = -2013264914
hrDatabaseAttached: win32more.Windows.Win32.Foundation.HRESULT = -2013264913
hrInvalidDatabaseId: win32more.Windows.Win32.Foundation.HRESULT = -939523086
hrOutOfMemory: win32more.Windows.Win32.Foundation.HRESULT = -939523085
hrOutOfDatabaseSpace: win32more.Windows.Win32.Foundation.HRESULT = -939523084
hrOutOfCursors: win32more.Windows.Win32.Foundation.HRESULT = -939523083
hrOutOfBuffers: win32more.Windows.Win32.Foundation.HRESULT = -939523082
hrTooManyIndexes: win32more.Windows.Win32.Foundation.HRESULT = -939523081
hrTooManyKeys: win32more.Windows.Win32.Foundation.HRESULT = -939523080
hrRecordDeleted: win32more.Windows.Win32.Foundation.HRESULT = -939523079
hrReadVerifyFailure: win32more.Windows.Win32.Foundation.HRESULT = -939523078
hrOutOfFileHandles: win32more.Windows.Win32.Foundation.HRESULT = -939523076
hrDiskIO: win32more.Windows.Win32.Foundation.HRESULT = -939523074
hrInvalidPath: win32more.Windows.Win32.Foundation.HRESULT = -939523073
hrRecordTooBig: win32more.Windows.Win32.Foundation.HRESULT = -939523070
hrTooManyOpenDatabases: win32more.Windows.Win32.Foundation.HRESULT = -939523069
hrInvalidDatabase: win32more.Windows.Win32.Foundation.HRESULT = -939523068
hrNotInitialized: win32more.Windows.Win32.Foundation.HRESULT = -939523067
hrAlreadyInitialized: win32more.Windows.Win32.Foundation.HRESULT = -939523066
hrFileAccessDenied: win32more.Windows.Win32.Foundation.HRESULT = -939523064
hrBufferTooSmall: win32more.Windows.Win32.Foundation.HRESULT = -939523058
hrSeekNotEqual: win32more.Windows.Win32.Foundation.HRESULT = -2013264881
hrTooManyColumns: win32more.Windows.Win32.Foundation.HRESULT = -939523056
hrContainerNotEmpty: win32more.Windows.Win32.Foundation.HRESULT = -939523053
hrInvalidFilename: win32more.Windows.Win32.Foundation.HRESULT = -939523052
hrInvalidBookmark: win32more.Windows.Win32.Foundation.HRESULT = -939523051
hrColumnInUse: win32more.Windows.Win32.Foundation.HRESULT = -939523050
hrInvalidBufferSize: win32more.Windows.Win32.Foundation.HRESULT = -939523049
hrColumnNotUpdatable: win32more.Windows.Win32.Foundation.HRESULT = -939523048
hrIndexInUse: win32more.Windows.Win32.Foundation.HRESULT = -939523045
hrNullKeyDisallowed: win32more.Windows.Win32.Foundation.HRESULT = -939523043
hrNotInTransaction: win32more.Windows.Win32.Foundation.HRESULT = -939523042
hrNoIdleActivity: win32more.Windows.Win32.Foundation.HRESULT = -2013264862
hrTooManyActiveUsers: win32more.Windows.Win32.Foundation.HRESULT = -939523037
hrInvalidCountry: win32more.Windows.Win32.Foundation.HRESULT = -939523035
hrInvalidLanguageId: win32more.Windows.Win32.Foundation.HRESULT = -939523034
hrInvalidCodePage: win32more.Windows.Win32.Foundation.HRESULT = -939523033
hrNoWriteLock: win32more.Windows.Win32.Foundation.HRESULT = -2013264853
hrColumnSetNull: win32more.Windows.Win32.Foundation.HRESULT = -2013264852
hrVersionStoreOutOfMemory: win32more.Windows.Win32.Foundation.HRESULT = -939523027
hrCurrencyStackOutOfMemory: win32more.Windows.Win32.Foundation.HRESULT = -939523026
hrOutOfSessions: win32more.Windows.Win32.Foundation.HRESULT = -939522995
hrWriteConflict: win32more.Windows.Win32.Foundation.HRESULT = -939522994
hrTransTooDeep: win32more.Windows.Win32.Foundation.HRESULT = -939522993
hrInvalidSesid: win32more.Windows.Win32.Foundation.HRESULT = -939522992
hrSessionWriteConflict: win32more.Windows.Win32.Foundation.HRESULT = -939522989
hrInTransaction: win32more.Windows.Win32.Foundation.HRESULT = -939522988
hrDatabaseDuplicate: win32more.Windows.Win32.Foundation.HRESULT = -939522895
hrDatabaseInUse: win32more.Windows.Win32.Foundation.HRESULT = -939522894
hrDatabaseNotFound: win32more.Windows.Win32.Foundation.HRESULT = -939522893
hrDatabaseInvalidName: win32more.Windows.Win32.Foundation.HRESULT = -939522892
hrDatabaseInvalidPages: win32more.Windows.Win32.Foundation.HRESULT = -939522891
hrDatabaseCorrupted: win32more.Windows.Win32.Foundation.HRESULT = -939522890
hrDatabaseLocked: win32more.Windows.Win32.Foundation.HRESULT = -939522889
hrTableEmpty: win32more.Windows.Win32.Foundation.HRESULT = -2013264619
hrTableLocked: win32more.Windows.Win32.Foundation.HRESULT = -939522794
hrTableDuplicate: win32more.Windows.Win32.Foundation.HRESULT = -939522793
hrTableInUse: win32more.Windows.Win32.Foundation.HRESULT = -939522792
hrObjectNotFound: win32more.Windows.Win32.Foundation.HRESULT = -939522791
hrCannotRename: win32more.Windows.Win32.Foundation.HRESULT = -939522790
hrDensityInvalid: win32more.Windows.Win32.Foundation.HRESULT = -939522789
hrTableNotEmpty: win32more.Windows.Win32.Foundation.HRESULT = -939522788
hrInvalidTableId: win32more.Windows.Win32.Foundation.HRESULT = -939522786
hrTooManyOpenTables: win32more.Windows.Win32.Foundation.HRESULT = -939522785
hrIllegalOperation: win32more.Windows.Win32.Foundation.HRESULT = -939522784
hrObjectDuplicate: win32more.Windows.Win32.Foundation.HRESULT = -939522782
hrInvalidObject: win32more.Windows.Win32.Foundation.HRESULT = -939522780
hrIndexCantBuild: win32more.Windows.Win32.Foundation.HRESULT = -939522695
hrIndexHasPrimary: win32more.Windows.Win32.Foundation.HRESULT = -939522694
hrIndexDuplicate: win32more.Windows.Win32.Foundation.HRESULT = -939522693
hrIndexNotFound: win32more.Windows.Win32.Foundation.HRESULT = -939522692
hrIndexMustStay: win32more.Windows.Win32.Foundation.HRESULT = -939522691
hrIndexInvalidDef: win32more.Windows.Win32.Foundation.HRESULT = -939522690
hrIndexHasClustered: win32more.Windows.Win32.Foundation.HRESULT = -939522688
hrCreateIndexFailed: win32more.Windows.Win32.Foundation.HRESULT = -2013264511
hrTooManyOpenIndexes: win32more.Windows.Win32.Foundation.HRESULT = -939522686
hrColumnLong: win32more.Windows.Win32.Foundation.HRESULT = -939522595
hrColumnDoesNotFit: win32more.Windows.Win32.Foundation.HRESULT = -939522593
hrNullInvalid: win32more.Windows.Win32.Foundation.HRESULT = -939522592
hrColumnIndexed: win32more.Windows.Win32.Foundation.HRESULT = -939522591
hrColumnTooBig: win32more.Windows.Win32.Foundation.HRESULT = -939522590
hrColumnNotFound: win32more.Windows.Win32.Foundation.HRESULT = -939522589
hrColumnDuplicate: win32more.Windows.Win32.Foundation.HRESULT = -939522588
hrColumn2ndSysMaint: win32more.Windows.Win32.Foundation.HRESULT = -939522586
hrInvalidColumnType: win32more.Windows.Win32.Foundation.HRESULT = -939522585
hrColumnMaxTruncated: win32more.Windows.Win32.Foundation.HRESULT = -2013264408
hrColumnCannotIndex: win32more.Windows.Win32.Foundation.HRESULT = -939522583
hrTaggedNotNULL: win32more.Windows.Win32.Foundation.HRESULT = -939522582
hrNoCurrentIndex: win32more.Windows.Win32.Foundation.HRESULT = -939522581
hrKeyIsMade: win32more.Windows.Win32.Foundation.HRESULT = -939522580
hrBadColumnId: win32more.Windows.Win32.Foundation.HRESULT = -939522579
hrBadItagSequence: win32more.Windows.Win32.Foundation.HRESULT = -939522578
hrCannotBeTagged: win32more.Windows.Win32.Foundation.HRESULT = -939522575
hrRecordNotFound: win32more.Windows.Win32.Foundation.HRESULT = -939522495
hrNoCurrentRecord: win32more.Windows.Win32.Foundation.HRESULT = -939522493
hrRecordClusteredChanged: win32more.Windows.Win32.Foundation.HRESULT = -939522492
hrKeyDuplicate: win32more.Windows.Win32.Foundation.HRESULT = -939522491
hrAlreadyPrepared: win32more.Windows.Win32.Foundation.HRESULT = -939522489
hrKeyNotMade: win32more.Windows.Win32.Foundation.HRESULT = -939522488
hrUpdateNotPrepared: win32more.Windows.Win32.Foundation.HRESULT = -939522487
hrwrnDataHasChanged: win32more.Windows.Win32.Foundation.HRESULT = -2013264310
hrerrDataHasChanged: win32more.Windows.Win32.Foundation.HRESULT = -939522485
hrKeyChanged: win32more.Windows.Win32.Foundation.HRESULT = -2013264302
hrTooManySorts: win32more.Windows.Win32.Foundation.HRESULT = -939522395
hrInvalidOnSort: win32more.Windows.Win32.Foundation.HRESULT = -939522394
hrTempFileOpenError: win32more.Windows.Win32.Foundation.HRESULT = -939522293
hrTooManyAttachedDatabases: win32more.Windows.Win32.Foundation.HRESULT = -939522291
hrDiskFull: win32more.Windows.Win32.Foundation.HRESULT = -939522288
hrPermissionDenied: win32more.Windows.Win32.Foundation.HRESULT = -939522287
hrFileNotFound: win32more.Windows.Win32.Foundation.HRESULT = -939522285
hrFileOpenReadOnly: win32more.Windows.Win32.Foundation.HRESULT = -2013264107
hrAfterInitialization: win32more.Windows.Win32.Foundation.HRESULT = -939522246
hrLogCorrupted: win32more.Windows.Win32.Foundation.HRESULT = -939522244
hrInvalidOperation: win32more.Windows.Win32.Foundation.HRESULT = -939522190
hrAccessDenied: win32more.Windows.Win32.Foundation.HRESULT = -939522189
CLSID_DsObjectPicker: Guid = Guid('{17d6ccd8-3b7b-11d2-b9e0-00c04fd8dbf7}')
@winfunctype('ACTIVEDS.dll')
def ADsGetObject(lpszPathName: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def ADsBuildEnumerator(pADsContainer: win32more.Windows.Win32.Networking.ActiveDirectory.IADsContainer, ppEnumVariant: POINTER(win32more.Windows.Win32.System.Ole.IEnumVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def ADsFreeEnumerator(pEnumVariant: win32more.Windows.Win32.System.Ole.IEnumVARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def ADsEnumerateNext(pEnumVariant: win32more.Windows.Win32.System.Ole.IEnumVARIANT, cElements: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pcElementsFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def ADsBuildVarArrayStr(lppPathNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwPathNames: UInt32, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def ADsBuildVarArrayInt(lpdwObjectTypes: POINTER(UInt32), dwObjectTypes: UInt32, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def ADsOpenObject(lpszPathName: win32more.Windows.Win32.Foundation.PWSTR, lpszUserName: win32more.Windows.Win32.Foundation.PWSTR, lpszPassword: win32more.Windows.Win32.Foundation.PWSTR, dwReserved: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_AUTHENTICATION_ENUM, riid: POINTER(Guid), ppObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def ADsGetLastError(lpError: POINTER(UInt32), lpErrorBuf: win32more.Windows.Win32.Foundation.PWSTR, dwErrorBufLen: UInt32, lpNameBuf: win32more.Windows.Win32.Foundation.PWSTR, dwNameBufLen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def ADsSetLastError(dwErr: UInt32, pszError: win32more.Windows.Win32.Foundation.PWSTR, pszProvider: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('ACTIVEDS.dll')
def AllocADsMem(cb: UInt32) -> VoidPtr: ...
@winfunctype('ACTIVEDS.dll')
def FreeADsMem(pMem: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ACTIVEDS.dll')
def ReallocADsMem(pOldMem: VoidPtr, cbOld: UInt32, cbNew: UInt32) -> VoidPtr: ...
@winfunctype('ACTIVEDS.dll')
def AllocADsStr(pStr: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('ACTIVEDS.dll')
def FreeADsStr(pStr: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ACTIVEDS.dll')
def ReallocADsStr(ppStr: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pStr: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ACTIVEDS.dll')
def ADsEncodeBinaryData(pbSrcData: POINTER(Byte), dwSrcLen: UInt32, ppszDestData: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def ADsDecodeBinaryData(szSrcData: win32more.Windows.Win32.Foundation.PWSTR, ppbDestData: POINTER(POINTER(Byte)), pdwDestLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def PropVariantToAdsType(pVariant: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), dwNumVariant: UInt32, ppAdsValues: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADSVALUE)), pdwNumValues: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def AdsTypeToPropVariant(pAdsValues: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADSVALUE), dwNumValues: UInt32, pVariant: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def AdsFreeAdsValues(pAdsValues: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADSVALUE), dwNumValues: UInt32) -> Void: ...
@winfunctype('ACTIVEDS.dll')
def BinarySDToSecurityDescriptor(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, pVarsec: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pszServerName: win32more.Windows.Win32.Foundation.PWSTR, userName: win32more.Windows.Win32.Foundation.PWSTR, passWord: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ACTIVEDS.dll')
def SecurityDescriptorToBinarySD(vVarSecDes: win32more.Windows.Win32.System.Variant.VARIANT, ppSecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), pdwSDLength: POINTER(UInt32), pszServerName: win32more.Windows.Win32.Foundation.PWSTR, userName: win32more.Windows.Win32.Foundation.PWSTR, passWord: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dsuiext.dll')
def DsBrowseForContainerW(pInfo: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DSBROWSEINFOW)) -> Int32: ...
DsBrowseForContainer = UnicodeAlias('DsBrowseForContainerW')
@winfunctype('dsuiext.dll')
def DsBrowseForContainerA(pInfo: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DSBROWSEINFOA)) -> Int32: ...
@winfunctype('dsuiext.dll')
def DsGetIcon(dwFlags: UInt32, pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, cxImage: Int32, cyImage: Int32) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('dsuiext.dll')
def DsGetFriendlyClassName(pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, pszBuffer: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dsprop.dll')
def ADsPropCreateNotifyObj(pAppThdDataObj: win32more.Windows.Win32.System.Com.IDataObject, pwzADsObjName: win32more.Windows.Win32.Foundation.PWSTR, phNotifyObj: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dsprop.dll')
def ADsPropGetInitInfo(hNotifyObj: win32more.Windows.Win32.Foundation.HWND, pInitParams: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADSPROPINITPARAMS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dsprop.dll')
def ADsPropSetHwndWithTitle(hNotifyObj: win32more.Windows.Win32.Foundation.HWND, hPage: win32more.Windows.Win32.Foundation.HWND, ptzTitle: POINTER(SByte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dsprop.dll')
def ADsPropSetHwnd(hNotifyObj: win32more.Windows.Win32.Foundation.HWND, hPage: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dsprop.dll')
def ADsPropCheckIfWritable(pwzAttr: win32more.Windows.Win32.Foundation.PWSTR, pWritableAttrs: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ATTR_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dsprop.dll')
def ADsPropSendErrorMessage(hNotifyObj: win32more.Windows.Win32.Foundation.HWND, pError: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADSPROPERROR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dsprop.dll')
def ADsPropShowErrorDialog(hNotifyObj: win32more.Windows.Win32.Foundation.HWND, hPage: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('DSPARSE.dll')
def DsMakeSpnW(ServiceClass: win32more.Windows.Win32.Foundation.PWSTR, ServiceName: win32more.Windows.Win32.Foundation.PWSTR, InstanceName: win32more.Windows.Win32.Foundation.PWSTR, InstancePort: UInt16, Referrer: win32more.Windows.Win32.Foundation.PWSTR, pcSpnLength: POINTER(UInt32), pszSpn: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
DsMakeSpn = UnicodeAlias('DsMakeSpnW')
@winfunctype('DSPARSE.dll')
def DsMakeSpnA(ServiceClass: win32more.Windows.Win32.Foundation.PSTR, ServiceName: win32more.Windows.Win32.Foundation.PSTR, InstanceName: win32more.Windows.Win32.Foundation.PSTR, InstancePort: UInt16, Referrer: win32more.Windows.Win32.Foundation.PSTR, pcSpnLength: POINTER(UInt32), pszSpn: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('DSPARSE.dll')
def DsCrackSpnA(pszSpn: win32more.Windows.Win32.Foundation.PSTR, pcServiceClass: POINTER(UInt32), ServiceClass: win32more.Windows.Win32.Foundation.PSTR, pcServiceName: POINTER(UInt32), ServiceName: win32more.Windows.Win32.Foundation.PSTR, pcInstanceName: POINTER(UInt32), InstanceName: win32more.Windows.Win32.Foundation.PSTR, pInstancePort: POINTER(UInt16)) -> UInt32: ...
@winfunctype('DSPARSE.dll')
def DsCrackSpnW(pszSpn: win32more.Windows.Win32.Foundation.PWSTR, pcServiceClass: POINTER(UInt32), ServiceClass: win32more.Windows.Win32.Foundation.PWSTR, pcServiceName: POINTER(UInt32), ServiceName: win32more.Windows.Win32.Foundation.PWSTR, pcInstanceName: POINTER(UInt32), InstanceName: win32more.Windows.Win32.Foundation.PWSTR, pInstancePort: POINTER(UInt16)) -> UInt32: ...
DsCrackSpn = UnicodeAlias('DsCrackSpnW')
@winfunctype('DSPARSE.dll')
def DsQuoteRdnValueW(cUnquotedRdnValueLength: UInt32, psUnquotedRdnValue: win32more.Windows.Win32.Foundation.PWSTR, pcQuotedRdnValueLength: POINTER(UInt32), psQuotedRdnValue: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
DsQuoteRdnValue = UnicodeAlias('DsQuoteRdnValueW')
@winfunctype('DSPARSE.dll')
def DsQuoteRdnValueA(cUnquotedRdnValueLength: UInt32, psUnquotedRdnValue: win32more.Windows.Win32.Foundation.PSTR, pcQuotedRdnValueLength: POINTER(UInt32), psQuotedRdnValue: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('DSPARSE.dll')
def DsUnquoteRdnValueW(cQuotedRdnValueLength: UInt32, psQuotedRdnValue: win32more.Windows.Win32.Foundation.PWSTR, pcUnquotedRdnValueLength: POINTER(UInt32), psUnquotedRdnValue: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
DsUnquoteRdnValue = UnicodeAlias('DsUnquoteRdnValueW')
@winfunctype('DSPARSE.dll')
def DsUnquoteRdnValueA(cQuotedRdnValueLength: UInt32, psQuotedRdnValue: win32more.Windows.Win32.Foundation.PSTR, pcUnquotedRdnValueLength: POINTER(UInt32), psUnquotedRdnValue: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('DSPARSE.dll')
def DsGetRdnW(ppDN: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcDN: POINTER(UInt32), ppKey: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcKey: POINTER(UInt32), ppVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcVal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DSPARSE.dll')
def DsCrackUnquotedMangledRdnW(pszRDN: win32more.Windows.Win32.Foundation.PWSTR, cchRDN: UInt32, pGuid: POINTER(Guid), peDsMangleFor: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_MANGLE_FOR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
DsCrackUnquotedMangledRdn = UnicodeAlias('DsCrackUnquotedMangledRdnW')
@winfunctype('DSPARSE.dll')
def DsCrackUnquotedMangledRdnA(pszRDN: win32more.Windows.Win32.Foundation.PSTR, cchRDN: UInt32, pGuid: POINTER(Guid), peDsMangleFor: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_MANGLE_FOR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('DSPARSE.dll')
def DsIsMangledRdnValueW(pszRdn: win32more.Windows.Win32.Foundation.PWSTR, cRdn: UInt32, eDsMangleForDesired: win32more.Windows.Win32.Networking.ActiveDirectory.DS_MANGLE_FOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
DsIsMangledRdnValue = UnicodeAlias('DsIsMangledRdnValueW')
@winfunctype('DSPARSE.dll')
def DsIsMangledRdnValueA(pszRdn: win32more.Windows.Win32.Foundation.PSTR, cRdn: UInt32, eDsMangleForDesired: win32more.Windows.Win32.Networking.ActiveDirectory.DS_MANGLE_FOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('DSPARSE.dll')
def DsIsMangledDnA(pszDn: win32more.Windows.Win32.Foundation.PSTR, eDsMangleFor: win32more.Windows.Win32.Networking.ActiveDirectory.DS_MANGLE_FOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('DSPARSE.dll')
def DsIsMangledDnW(pszDn: win32more.Windows.Win32.Foundation.PWSTR, eDsMangleFor: win32more.Windows.Win32.Networking.ActiveDirectory.DS_MANGLE_FOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
DsIsMangledDn = UnicodeAlias('DsIsMangledDnW')
@winfunctype('DSPARSE.dll')
def DsCrackSpn2A(pszSpn: win32more.Windows.Win32.Foundation.PSTR, cSpn: UInt32, pcServiceClass: POINTER(UInt32), ServiceClass: win32more.Windows.Win32.Foundation.PSTR, pcServiceName: POINTER(UInt32), ServiceName: win32more.Windows.Win32.Foundation.PSTR, pcInstanceName: POINTER(UInt32), InstanceName: win32more.Windows.Win32.Foundation.PSTR, pInstancePort: POINTER(UInt16)) -> UInt32: ...
@winfunctype('DSPARSE.dll')
def DsCrackSpn2W(pszSpn: win32more.Windows.Win32.Foundation.PWSTR, cSpn: UInt32, pcServiceClass: POINTER(UInt32), ServiceClass: win32more.Windows.Win32.Foundation.PWSTR, pcServiceName: POINTER(UInt32), ServiceName: win32more.Windows.Win32.Foundation.PWSTR, pcInstanceName: POINTER(UInt32), InstanceName: win32more.Windows.Win32.Foundation.PWSTR, pInstancePort: POINTER(UInt16)) -> UInt32: ...
DsCrackSpn2 = UnicodeAlias('DsCrackSpn2W')
@winfunctype('DSPARSE.dll')
def DsCrackSpn3W(pszSpn: win32more.Windows.Win32.Foundation.PWSTR, cSpn: UInt32, pcHostName: POINTER(UInt32), HostName: win32more.Windows.Win32.Foundation.PWSTR, pcInstanceName: POINTER(UInt32), InstanceName: win32more.Windows.Win32.Foundation.PWSTR, pPortNumber: POINTER(UInt16), pcDomainName: POINTER(UInt32), DomainName: win32more.Windows.Win32.Foundation.PWSTR, pcRealmName: POINTER(UInt32), RealmName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DSPARSE.dll')
def DsCrackSpn4W(pszSpn: win32more.Windows.Win32.Foundation.PWSTR, cSpn: UInt32, pcHostName: POINTER(UInt32), HostName: win32more.Windows.Win32.Foundation.PWSTR, pcInstanceName: POINTER(UInt32), InstanceName: win32more.Windows.Win32.Foundation.PWSTR, pcPortName: POINTER(UInt32), PortName: win32more.Windows.Win32.Foundation.PWSTR, pcDomainName: POINTER(UInt32), DomainName: win32more.Windows.Win32.Foundation.PWSTR, pcRealmName: POINTER(UInt32), RealmName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsBindW(DomainControllerName: win32more.Windows.Win32.Foundation.PWSTR, DnsDomainName: win32more.Windows.Win32.Foundation.PWSTR, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
DsBind = UnicodeAlias('DsBindW')
@winfunctype('NTDSAPI.dll')
def DsBindA(DomainControllerName: win32more.Windows.Win32.Foundation.PSTR, DnsDomainName: win32more.Windows.Win32.Foundation.PSTR, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsBindWithCredW(DomainControllerName: win32more.Windows.Win32.Foundation.PWSTR, DnsDomainName: win32more.Windows.Win32.Foundation.PWSTR, AuthIdentity: VoidPtr, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
DsBindWithCred = UnicodeAlias('DsBindWithCredW')
@winfunctype('NTDSAPI.dll')
def DsBindWithCredA(DomainControllerName: win32more.Windows.Win32.Foundation.PSTR, DnsDomainName: win32more.Windows.Win32.Foundation.PSTR, AuthIdentity: VoidPtr, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsBindWithSpnW(DomainControllerName: win32more.Windows.Win32.Foundation.PWSTR, DnsDomainName: win32more.Windows.Win32.Foundation.PWSTR, AuthIdentity: VoidPtr, ServicePrincipalName: win32more.Windows.Win32.Foundation.PWSTR, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
DsBindWithSpn = UnicodeAlias('DsBindWithSpnW')
@winfunctype('NTDSAPI.dll')
def DsBindWithSpnA(DomainControllerName: win32more.Windows.Win32.Foundation.PSTR, DnsDomainName: win32more.Windows.Win32.Foundation.PSTR, AuthIdentity: VoidPtr, ServicePrincipalName: win32more.Windows.Win32.Foundation.PSTR, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsBindWithSpnExW(DomainControllerName: win32more.Windows.Win32.Foundation.PWSTR, DnsDomainName: win32more.Windows.Win32.Foundation.PWSTR, AuthIdentity: VoidPtr, ServicePrincipalName: win32more.Windows.Win32.Foundation.PWSTR, BindFlags: UInt32, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
DsBindWithSpnEx = UnicodeAlias('DsBindWithSpnExW')
@winfunctype('NTDSAPI.dll')
def DsBindWithSpnExA(DomainControllerName: win32more.Windows.Win32.Foundation.PSTR, DnsDomainName: win32more.Windows.Win32.Foundation.PSTR, AuthIdentity: VoidPtr, ServicePrincipalName: win32more.Windows.Win32.Foundation.PSTR, BindFlags: UInt32, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsBindByInstanceW(ServerName: win32more.Windows.Win32.Foundation.PWSTR, Annotation: win32more.Windows.Win32.Foundation.PWSTR, InstanceGuid: POINTER(Guid), DnsDomainName: win32more.Windows.Win32.Foundation.PWSTR, AuthIdentity: VoidPtr, ServicePrincipalName: win32more.Windows.Win32.Foundation.PWSTR, BindFlags: UInt32, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
DsBindByInstance = UnicodeAlias('DsBindByInstanceW')
@winfunctype('NTDSAPI.dll')
def DsBindByInstanceA(ServerName: win32more.Windows.Win32.Foundation.PSTR, Annotation: win32more.Windows.Win32.Foundation.PSTR, InstanceGuid: POINTER(Guid), DnsDomainName: win32more.Windows.Win32.Foundation.PSTR, AuthIdentity: VoidPtr, ServicePrincipalName: win32more.Windows.Win32.Foundation.PSTR, BindFlags: UInt32, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsBindToISTGW(SiteName: win32more.Windows.Win32.Foundation.PWSTR, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
DsBindToISTG = UnicodeAlias('DsBindToISTGW')
@winfunctype('NTDSAPI.dll')
def DsBindToISTGA(SiteName: win32more.Windows.Win32.Foundation.PSTR, phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsBindingSetTimeout(hDS: win32more.Windows.Win32.Foundation.HANDLE, cTimeoutSecs: UInt32) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsUnBindW(phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
DsUnBind = UnicodeAlias('DsUnBindW')
@winfunctype('NTDSAPI.dll')
def DsUnBindA(phDS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsMakePasswordCredentialsW(User: win32more.Windows.Win32.Foundation.PWSTR, Domain: win32more.Windows.Win32.Foundation.PWSTR, Password: win32more.Windows.Win32.Foundation.PWSTR, pAuthIdentity: POINTER(VoidPtr)) -> UInt32: ...
DsMakePasswordCredentials = UnicodeAlias('DsMakePasswordCredentialsW')
@winfunctype('NTDSAPI.dll')
def DsMakePasswordCredentialsA(User: win32more.Windows.Win32.Foundation.PSTR, Domain: win32more.Windows.Win32.Foundation.PSTR, Password: win32more.Windows.Win32.Foundation.PSTR, pAuthIdentity: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsFreePasswordCredentials(AuthIdentity: VoidPtr) -> Void: ...
@winfunctype('NTDSAPI.dll')
def DsCrackNamesW(hDS: win32more.Windows.Win32.Foundation.HANDLE, flags: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FLAGS, formatOffered: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT, formatDesired: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT, cNames: UInt32, rpNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppResult: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTW))) -> UInt32: ...
DsCrackNames = UnicodeAlias('DsCrackNamesW')
@winfunctype('NTDSAPI.dll')
def DsCrackNamesA(hDS: win32more.Windows.Win32.Foundation.HANDLE, flags: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FLAGS, formatOffered: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT, formatDesired: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT, cNames: UInt32, rpNames: POINTER(win32more.Windows.Win32.Foundation.PSTR), ppResult: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTA))) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsFreeNameResultW(pResult: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTW)) -> Void: ...
DsFreeNameResult = UnicodeAlias('DsFreeNameResultW')
@winfunctype('NTDSAPI.dll')
def DsFreeNameResultA(pResult: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTA)) -> Void: ...
@winfunctype('NTDSAPI.dll')
def DsGetSpnA(ServiceType: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_NAME_TYPE, ServiceClass: win32more.Windows.Win32.Foundation.PSTR, ServiceName: win32more.Windows.Win32.Foundation.PSTR, InstancePort: UInt16, cInstanceNames: UInt16, pInstanceNames: POINTER(win32more.Windows.Win32.Foundation.PSTR), pInstancePorts: POINTER(UInt16), pcSpn: POINTER(UInt32), prpszSpn: POINTER(POINTER(win32more.Windows.Win32.Foundation.PSTR))) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsGetSpnW(ServiceType: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_NAME_TYPE, ServiceClass: win32more.Windows.Win32.Foundation.PWSTR, ServiceName: win32more.Windows.Win32.Foundation.PWSTR, InstancePort: UInt16, cInstanceNames: UInt16, pInstanceNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pInstancePorts: POINTER(UInt16), pcSpn: POINTER(UInt32), prpszSpn: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))) -> UInt32: ...
DsGetSpn = UnicodeAlias('DsGetSpnW')
@winfunctype('NTDSAPI.dll')
def DsFreeSpnArrayA(cSpn: UInt32, rpszSpn: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> Void: ...
@winfunctype('NTDSAPI.dll')
def DsFreeSpnArrayW(cSpn: UInt32, rpszSpn: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> Void: ...
DsFreeSpnArray = UnicodeAlias('DsFreeSpnArrayW')
@winfunctype('NTDSAPI.dll')
def DsWriteAccountSpnA(hDS: win32more.Windows.Win32.Foundation.HANDLE, Operation: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_WRITE_OP, pszAccount: win32more.Windows.Win32.Foundation.PSTR, cSpn: UInt32, rpszSpn: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsWriteAccountSpnW(hDS: win32more.Windows.Win32.Foundation.HANDLE, Operation: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_WRITE_OP, pszAccount: win32more.Windows.Win32.Foundation.PWSTR, cSpn: UInt32, rpszSpn: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
DsWriteAccountSpn = UnicodeAlias('DsWriteAccountSpnW')
@winfunctype('NTDSAPI.dll')
def DsClientMakeSpnForTargetServerW(ServiceClass: win32more.Windows.Win32.Foundation.PWSTR, ServiceName: win32more.Windows.Win32.Foundation.PWSTR, pcSpnLength: POINTER(UInt32), pszSpn: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
DsClientMakeSpnForTargetServer = UnicodeAlias('DsClientMakeSpnForTargetServerW')
@winfunctype('NTDSAPI.dll')
def DsClientMakeSpnForTargetServerA(ServiceClass: win32more.Windows.Win32.Foundation.PSTR, ServiceName: win32more.Windows.Win32.Foundation.PSTR, pcSpnLength: POINTER(UInt32), pszSpn: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsServerRegisterSpnA(Operation: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_WRITE_OP, ServiceClass: win32more.Windows.Win32.Foundation.PSTR, UserObjectDN: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsServerRegisterSpnW(Operation: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_WRITE_OP, ServiceClass: win32more.Windows.Win32.Foundation.PWSTR, UserObjectDN: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
DsServerRegisterSpn = UnicodeAlias('DsServerRegisterSpnW')
@winfunctype('NTDSAPI.dll')
def DsReplicaSyncA(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PSTR, pUuidDsaSrc: POINTER(Guid), Options: UInt32) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsReplicaSyncW(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PWSTR, pUuidDsaSrc: POINTER(Guid), Options: UInt32) -> UInt32: ...
DsReplicaSync = UnicodeAlias('DsReplicaSyncW')
@winfunctype('NTDSAPI.dll')
def DsReplicaAddA(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PSTR, SourceDsaDn: win32more.Windows.Win32.Foundation.PSTR, TransportDn: win32more.Windows.Win32.Foundation.PSTR, SourceDsaAddress: win32more.Windows.Win32.Foundation.PSTR, pSchedule: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.SCHEDULE), Options: UInt32) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsReplicaAddW(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PWSTR, SourceDsaDn: win32more.Windows.Win32.Foundation.PWSTR, TransportDn: win32more.Windows.Win32.Foundation.PWSTR, SourceDsaAddress: win32more.Windows.Win32.Foundation.PWSTR, pSchedule: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.SCHEDULE), Options: UInt32) -> UInt32: ...
DsReplicaAdd = UnicodeAlias('DsReplicaAddW')
@winfunctype('NTDSAPI.dll')
def DsReplicaDelA(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PSTR, DsaSrc: win32more.Windows.Win32.Foundation.PSTR, Options: UInt32) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsReplicaDelW(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PWSTR, DsaSrc: win32more.Windows.Win32.Foundation.PWSTR, Options: UInt32) -> UInt32: ...
DsReplicaDel = UnicodeAlias('DsReplicaDelW')
@winfunctype('NTDSAPI.dll')
def DsReplicaModifyA(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PSTR, pUuidSourceDsa: POINTER(Guid), TransportDn: win32more.Windows.Win32.Foundation.PSTR, SourceDsaAddress: win32more.Windows.Win32.Foundation.PSTR, pSchedule: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.SCHEDULE), ReplicaFlags: UInt32, ModifyFields: UInt32, Options: UInt32) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsReplicaModifyW(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PWSTR, pUuidSourceDsa: POINTER(Guid), TransportDn: win32more.Windows.Win32.Foundation.PWSTR, SourceDsaAddress: win32more.Windows.Win32.Foundation.PWSTR, pSchedule: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.SCHEDULE), ReplicaFlags: UInt32, ModifyFields: UInt32, Options: UInt32) -> UInt32: ...
DsReplicaModify = UnicodeAlias('DsReplicaModifyW')
@winfunctype('NTDSAPI.dll')
def DsReplicaUpdateRefsA(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PSTR, DsaDest: win32more.Windows.Win32.Foundation.PSTR, pUuidDsaDest: POINTER(Guid), Options: UInt32) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsReplicaUpdateRefsW(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PWSTR, DsaDest: win32more.Windows.Win32.Foundation.PWSTR, pUuidDsaDest: POINTER(Guid), Options: UInt32) -> UInt32: ...
DsReplicaUpdateRefs = UnicodeAlias('DsReplicaUpdateRefsW')
@winfunctype('NTDSAPI.dll')
def DsReplicaSyncAllA(hDS: win32more.Windows.Win32.Foundation.HANDLE, pszNameContext: win32more.Windows.Win32.Foundation.PSTR, ulFlags: UInt32, pFnCallBack: IntPtr, pCallbackData: VoidPtr, pErrors: POINTER(POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_ERRINFOA)))) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsReplicaSyncAllW(hDS: win32more.Windows.Win32.Foundation.HANDLE, pszNameContext: win32more.Windows.Win32.Foundation.PWSTR, ulFlags: UInt32, pFnCallBack: IntPtr, pCallbackData: VoidPtr, pErrors: POINTER(POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_ERRINFOW)))) -> UInt32: ...
DsReplicaSyncAll = UnicodeAlias('DsReplicaSyncAllW')
@winfunctype('NTDSAPI.dll')
def DsRemoveDsServerW(hDs: win32more.Windows.Win32.Foundation.HANDLE, ServerDN: win32more.Windows.Win32.Foundation.PWSTR, DomainDN: win32more.Windows.Win32.Foundation.PWSTR, fLastDcInDomain: POINTER(win32more.Windows.Win32.Foundation.BOOL), fCommit: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
DsRemoveDsServer = UnicodeAlias('DsRemoveDsServerW')
@winfunctype('NTDSAPI.dll')
def DsRemoveDsServerA(hDs: win32more.Windows.Win32.Foundation.HANDLE, ServerDN: win32more.Windows.Win32.Foundation.PSTR, DomainDN: win32more.Windows.Win32.Foundation.PSTR, fLastDcInDomain: POINTER(win32more.Windows.Win32.Foundation.BOOL), fCommit: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsRemoveDsDomainW(hDs: win32more.Windows.Win32.Foundation.HANDLE, DomainDN: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
DsRemoveDsDomain = UnicodeAlias('DsRemoveDsDomainW')
@winfunctype('NTDSAPI.dll')
def DsRemoveDsDomainA(hDs: win32more.Windows.Win32.Foundation.HANDLE, DomainDN: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsListSitesA(hDs: win32more.Windows.Win32.Foundation.HANDLE, ppSites: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTA))) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsListSitesW(hDs: win32more.Windows.Win32.Foundation.HANDLE, ppSites: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTW))) -> UInt32: ...
DsListSites = UnicodeAlias('DsListSitesW')
@winfunctype('NTDSAPI.dll')
def DsListServersInSiteA(hDs: win32more.Windows.Win32.Foundation.HANDLE, site: win32more.Windows.Win32.Foundation.PSTR, ppServers: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTA))) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsListServersInSiteW(hDs: win32more.Windows.Win32.Foundation.HANDLE, site: win32more.Windows.Win32.Foundation.PWSTR, ppServers: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTW))) -> UInt32: ...
DsListServersInSite = UnicodeAlias('DsListServersInSiteW')
@winfunctype('NTDSAPI.dll')
def DsListDomainsInSiteA(hDs: win32more.Windows.Win32.Foundation.HANDLE, site: win32more.Windows.Win32.Foundation.PSTR, ppDomains: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTA))) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsListDomainsInSiteW(hDs: win32more.Windows.Win32.Foundation.HANDLE, site: win32more.Windows.Win32.Foundation.PWSTR, ppDomains: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTW))) -> UInt32: ...
DsListDomainsInSite = UnicodeAlias('DsListDomainsInSiteW')
@winfunctype('NTDSAPI.dll')
def DsListServersForDomainInSiteA(hDs: win32more.Windows.Win32.Foundation.HANDLE, domain: win32more.Windows.Win32.Foundation.PSTR, site: win32more.Windows.Win32.Foundation.PSTR, ppServers: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTA))) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsListServersForDomainInSiteW(hDs: win32more.Windows.Win32.Foundation.HANDLE, domain: win32more.Windows.Win32.Foundation.PWSTR, site: win32more.Windows.Win32.Foundation.PWSTR, ppServers: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTW))) -> UInt32: ...
DsListServersForDomainInSite = UnicodeAlias('DsListServersForDomainInSiteW')
@winfunctype('NTDSAPI.dll')
def DsListInfoForServerA(hDs: win32more.Windows.Win32.Foundation.HANDLE, server: win32more.Windows.Win32.Foundation.PSTR, ppInfo: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTA))) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsListInfoForServerW(hDs: win32more.Windows.Win32.Foundation.HANDLE, server: win32more.Windows.Win32.Foundation.PWSTR, ppInfo: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTW))) -> UInt32: ...
DsListInfoForServer = UnicodeAlias('DsListInfoForServerW')
@winfunctype('NTDSAPI.dll')
def DsListRolesA(hDs: win32more.Windows.Win32.Foundation.HANDLE, ppRoles: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTA))) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsListRolesW(hDs: win32more.Windows.Win32.Foundation.HANDLE, ppRoles: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULTW))) -> UInt32: ...
DsListRoles = UnicodeAlias('DsListRolesW')
@winfunctype('NTDSAPI.dll')
def DsQuerySitesByCostW(hDS: win32more.Windows.Win32.Foundation.HANDLE, pwszFromSite: win32more.Windows.Win32.Foundation.PWSTR, rgwszToSites: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cToSites: UInt32, dwFlags: UInt32, prgSiteInfo: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_SITE_COST_INFO))) -> UInt32: ...
DsQuerySitesByCost = UnicodeAlias('DsQuerySitesByCostW')
@winfunctype('NTDSAPI.dll')
def DsQuerySitesByCostA(hDS: win32more.Windows.Win32.Foundation.HANDLE, pszFromSite: win32more.Windows.Win32.Foundation.PSTR, rgszToSites: POINTER(win32more.Windows.Win32.Foundation.PSTR), cToSites: UInt32, dwFlags: UInt32, prgSiteInfo: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_SITE_COST_INFO))) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsQuerySitesFree(rgSiteInfo: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_SITE_COST_INFO)) -> Void: ...
@winfunctype('NTDSAPI.dll')
def DsMapSchemaGuidsA(hDs: win32more.Windows.Win32.Foundation.HANDLE, cGuids: UInt32, rGuids: POINTER(Guid), ppGuidMap: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_SCHEMA_GUID_MAPA))) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsFreeSchemaGuidMapA(pGuidMap: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_SCHEMA_GUID_MAPA)) -> Void: ...
@winfunctype('NTDSAPI.dll')
def DsMapSchemaGuidsW(hDs: win32more.Windows.Win32.Foundation.HANDLE, cGuids: UInt32, rGuids: POINTER(Guid), ppGuidMap: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_SCHEMA_GUID_MAPW))) -> UInt32: ...
DsMapSchemaGuids = UnicodeAlias('DsMapSchemaGuidsW')
@winfunctype('NTDSAPI.dll')
def DsFreeSchemaGuidMapW(pGuidMap: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_SCHEMA_GUID_MAPW)) -> Void: ...
DsFreeSchemaGuidMap = UnicodeAlias('DsFreeSchemaGuidMapW')
@winfunctype('NTDSAPI.dll')
def DsGetDomainControllerInfoA(hDs: win32more.Windows.Win32.Foundation.HANDLE, DomainName: win32more.Windows.Win32.Foundation.PSTR, InfoLevel: UInt32, pcOut: POINTER(UInt32), ppInfo: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsGetDomainControllerInfoW(hDs: win32more.Windows.Win32.Foundation.HANDLE, DomainName: win32more.Windows.Win32.Foundation.PWSTR, InfoLevel: UInt32, pcOut: POINTER(UInt32), ppInfo: POINTER(VoidPtr)) -> UInt32: ...
DsGetDomainControllerInfo = UnicodeAlias('DsGetDomainControllerInfoW')
@winfunctype('NTDSAPI.dll')
def DsFreeDomainControllerInfoA(InfoLevel: UInt32, cInfo: UInt32, pInfo: VoidPtr) -> Void: ...
@winfunctype('NTDSAPI.dll')
def DsFreeDomainControllerInfoW(InfoLevel: UInt32, cInfo: UInt32, pInfo: VoidPtr) -> Void: ...
DsFreeDomainControllerInfo = UnicodeAlias('DsFreeDomainControllerInfoW')
@winfunctype('NTDSAPI.dll')
def DsReplicaConsistencyCheck(hDS: win32more.Windows.Win32.Foundation.HANDLE, TaskID: win32more.Windows.Win32.Networking.ActiveDirectory.DS_KCC_TASKID, dwFlags: UInt32) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsReplicaVerifyObjectsW(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PWSTR, pUuidDsaSrc: POINTER(Guid), ulOptions: UInt32) -> UInt32: ...
DsReplicaVerifyObjects = UnicodeAlias('DsReplicaVerifyObjectsW')
@winfunctype('NTDSAPI.dll')
def DsReplicaVerifyObjectsA(hDS: win32more.Windows.Win32.Foundation.HANDLE, NameContext: win32more.Windows.Win32.Foundation.PSTR, pUuidDsaSrc: POINTER(Guid), ulOptions: UInt32) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsReplicaGetInfoW(hDS: win32more.Windows.Win32.Foundation.HANDLE, InfoType: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE, pszObject: win32more.Windows.Win32.Foundation.PWSTR, puuidForSourceDsaObjGuid: POINTER(Guid), ppInfo: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsReplicaGetInfo2W(hDS: win32more.Windows.Win32.Foundation.HANDLE, InfoType: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE, pszObject: win32more.Windows.Win32.Foundation.PWSTR, puuidForSourceDsaObjGuid: POINTER(Guid), pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwEnumerationContext: UInt32, ppInfo: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsReplicaFreeInfo(InfoType: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE, pInfo: VoidPtr) -> Void: ...
@winfunctype('NTDSAPI.dll')
def DsAddSidHistoryW(hDS: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32, SrcDomain: win32more.Windows.Win32.Foundation.PWSTR, SrcPrincipal: win32more.Windows.Win32.Foundation.PWSTR, SrcDomainController: win32more.Windows.Win32.Foundation.PWSTR, SrcDomainCreds: VoidPtr, DstDomain: win32more.Windows.Win32.Foundation.PWSTR, DstPrincipal: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
DsAddSidHistory = UnicodeAlias('DsAddSidHistoryW')
@winfunctype('NTDSAPI.dll')
def DsAddSidHistoryA(hDS: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32, SrcDomain: win32more.Windows.Win32.Foundation.PSTR, SrcPrincipal: win32more.Windows.Win32.Foundation.PSTR, SrcDomainController: win32more.Windows.Win32.Foundation.PSTR, SrcDomainCreds: VoidPtr, DstDomain: win32more.Windows.Win32.Foundation.PSTR, DstPrincipal: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('NTDSAPI.dll')
def DsInheritSecurityIdentityW(hDS: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32, SrcPrincipal: win32more.Windows.Win32.Foundation.PWSTR, DstPrincipal: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
DsInheritSecurityIdentity = UnicodeAlias('DsInheritSecurityIdentityW')
@winfunctype('NTDSAPI.dll')
def DsInheritSecurityIdentityA(hDS: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32, SrcPrincipal: win32more.Windows.Win32.Foundation.PSTR, DstPrincipal: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsRoleGetPrimaryDomainInformation(lpServer: win32more.Windows.Win32.Foundation.PWSTR, InfoLevel: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_PRIMARY_DOMAIN_INFO_LEVEL, Buffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsRoleFreeMemory(Buffer: VoidPtr) -> Void: ...
@winfunctype('NETAPI32.dll')
def DsGetDcNameA(ComputerName: win32more.Windows.Win32.Foundation.PSTR, DomainName: win32more.Windows.Win32.Foundation.PSTR, DomainGuid: POINTER(Guid), SiteName: win32more.Windows.Win32.Foundation.PSTR, Flags: UInt32, DomainControllerInfo: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DOMAIN_CONTROLLER_INFOA))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsGetDcNameW(ComputerName: win32more.Windows.Win32.Foundation.PWSTR, DomainName: win32more.Windows.Win32.Foundation.PWSTR, DomainGuid: POINTER(Guid), SiteName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32, DomainControllerInfo: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DOMAIN_CONTROLLER_INFOW))) -> UInt32: ...
DsGetDcName = UnicodeAlias('DsGetDcNameW')
@winfunctype('NETAPI32.dll')
def DsGetSiteNameA(ComputerName: win32more.Windows.Win32.Foundation.PSTR, SiteName: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsGetSiteNameW(ComputerName: win32more.Windows.Win32.Foundation.PWSTR, SiteName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
DsGetSiteName = UnicodeAlias('DsGetSiteNameW')
@winfunctype('NETAPI32.dll')
def DsValidateSubnetNameW(SubnetName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
DsValidateSubnetName = UnicodeAlias('DsValidateSubnetNameW')
@winfunctype('NETAPI32.dll')
def DsValidateSubnetNameA(SubnetName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsAddressToSiteNamesW(ComputerName: win32more.Windows.Win32.Foundation.PWSTR, EntryCount: UInt32, SocketAddresses: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS), SiteNames: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))) -> UInt32: ...
DsAddressToSiteNames = UnicodeAlias('DsAddressToSiteNamesW')
@winfunctype('NETAPI32.dll')
def DsAddressToSiteNamesA(ComputerName: win32more.Windows.Win32.Foundation.PSTR, EntryCount: UInt32, SocketAddresses: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS), SiteNames: POINTER(POINTER(win32more.Windows.Win32.Foundation.PSTR))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsAddressToSiteNamesExW(ComputerName: win32more.Windows.Win32.Foundation.PWSTR, EntryCount: UInt32, SocketAddresses: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS), SiteNames: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), SubnetNames: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))) -> UInt32: ...
DsAddressToSiteNamesEx = UnicodeAlias('DsAddressToSiteNamesExW')
@winfunctype('NETAPI32.dll')
def DsAddressToSiteNamesExA(ComputerName: win32more.Windows.Win32.Foundation.PSTR, EntryCount: UInt32, SocketAddresses: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS), SiteNames: POINTER(POINTER(win32more.Windows.Win32.Foundation.PSTR)), SubnetNames: POINTER(POINTER(win32more.Windows.Win32.Foundation.PSTR))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsEnumerateDomainTrustsW(ServerName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32, Domains: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_DOMAIN_TRUSTSW)), DomainCount: POINTER(UInt32)) -> UInt32: ...
DsEnumerateDomainTrusts = UnicodeAlias('DsEnumerateDomainTrustsW')
@winfunctype('NETAPI32.dll')
def DsEnumerateDomainTrustsA(ServerName: win32more.Windows.Win32.Foundation.PSTR, Flags: UInt32, Domains: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_DOMAIN_TRUSTSA)), DomainCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsGetForestTrustInformationW(ServerName: win32more.Windows.Win32.Foundation.PWSTR, TrustedDomainName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32, ForestTrustInfo: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.Identity.LSA_FOREST_TRUST_INFORMATION))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsMergeForestTrustInformationW(DomainName: win32more.Windows.Win32.Foundation.PWSTR, NewForestTrustInfo: POINTER(win32more.Windows.Win32.Security.Authentication.Identity.LSA_FOREST_TRUST_INFORMATION), OldForestTrustInfo: POINTER(win32more.Windows.Win32.Security.Authentication.Identity.LSA_FOREST_TRUST_INFORMATION), MergedForestTrustInfo: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.Identity.LSA_FOREST_TRUST_INFORMATION))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsGetDcSiteCoverageW(ServerName: win32more.Windows.Win32.Foundation.PWSTR, EntryCount: POINTER(UInt32), SiteNames: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))) -> UInt32: ...
DsGetDcSiteCoverage = UnicodeAlias('DsGetDcSiteCoverageW')
@winfunctype('NETAPI32.dll')
def DsGetDcSiteCoverageA(ServerName: win32more.Windows.Win32.Foundation.PSTR, EntryCount: POINTER(UInt32), SiteNames: POINTER(POINTER(win32more.Windows.Win32.Foundation.PSTR))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsDeregisterDnsHostRecordsW(ServerName: win32more.Windows.Win32.Foundation.PWSTR, DnsDomainName: win32more.Windows.Win32.Foundation.PWSTR, DomainGuid: POINTER(Guid), DsaGuid: POINTER(Guid), DnsHostName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
DsDeregisterDnsHostRecords = UnicodeAlias('DsDeregisterDnsHostRecordsW')
@winfunctype('NETAPI32.dll')
def DsDeregisterDnsHostRecordsA(ServerName: win32more.Windows.Win32.Foundation.PSTR, DnsDomainName: win32more.Windows.Win32.Foundation.PSTR, DomainGuid: POINTER(Guid), DsaGuid: POINTER(Guid), DnsHostName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsGetDcOpenW(DnsName: win32more.Windows.Win32.Foundation.PWSTR, OptionFlags: UInt32, SiteName: win32more.Windows.Win32.Foundation.PWSTR, DomainGuid: POINTER(Guid), DnsForestName: win32more.Windows.Win32.Foundation.PWSTR, DcFlags: UInt32, RetGetDcContext: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
DsGetDcOpen = UnicodeAlias('DsGetDcOpenW')
@winfunctype('NETAPI32.dll')
def DsGetDcOpenA(DnsName: win32more.Windows.Win32.Foundation.PSTR, OptionFlags: UInt32, SiteName: win32more.Windows.Win32.Foundation.PSTR, DomainGuid: POINTER(Guid), DnsForestName: win32more.Windows.Win32.Foundation.PSTR, DcFlags: UInt32, RetGetDcContext: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsGetDcNextW(GetDcContextHandle: win32more.Windows.Win32.Foundation.HANDLE, SockAddressCount: POINTER(UInt32), SockAddresses: POINTER(POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS)), DnsHostName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
DsGetDcNext = UnicodeAlias('DsGetDcNextW')
@winfunctype('NETAPI32.dll')
def DsGetDcNextA(GetDcContextHandle: win32more.Windows.Win32.Foundation.HANDLE, SockAddressCount: POINTER(UInt32), SockAddresses: POINTER(POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS)), DnsHostName: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DsGetDcCloseW(GetDcContextHandle: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
BackLink = Guid('{fcbf906f-4080-11d1-a3ac-00c04fb950dc}')
class CQFORM(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    clsid: Guid
    hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    pszTitle: win32more.Windows.Win32.Foundation.PWSTR
class CQPAGE(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    pPageProc: win32more.Windows.Win32.Networking.ActiveDirectory.LPCQPAGEPROC
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    idPageName: Int32
    idPageTemplate: Int32
    pDlgProc: win32more.Windows.Win32.UI.WindowsAndMessaging.DLGPROC
    lParam: win32more.Windows.Win32.Foundation.LPARAM
CaseIgnoreList = Guid('{15f88a55-4680-11d1-a3b4-00c04fb950dc}')
DNWithBinary = Guid('{7e99c0a3-f935-11d2-ba96-00c04fb6d0d1}')
DNWithString = Guid('{334857cc-f934-11d2-ba96-00c04fb6d0d1}')
class DOMAINDESC(Structure):
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    pszPath: win32more.Windows.Win32.Foundation.PWSTR
    pszNCName: win32more.Windows.Win32.Foundation.PWSTR
    pszTrustParent: win32more.Windows.Win32.Foundation.PWSTR
    pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR
    ulFlags: UInt32
    fDownLevel: win32more.Windows.Win32.Foundation.BOOL
    pdChildList: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DOMAINDESC)
    pdNextSibling: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DOMAINDESC)
class DOMAIN_CONTROLLER_INFOA(Structure):
    DomainControllerName: win32more.Windows.Win32.Foundation.PSTR
    DomainControllerAddress: win32more.Windows.Win32.Foundation.PSTR
    DomainControllerAddressType: UInt32
    DomainGuid: Guid
    DomainName: win32more.Windows.Win32.Foundation.PSTR
    DnsForestName: win32more.Windows.Win32.Foundation.PSTR
    Flags: UInt32
    DcSiteName: win32more.Windows.Win32.Foundation.PSTR
    ClientSiteName: win32more.Windows.Win32.Foundation.PSTR
class DOMAIN_CONTROLLER_INFOW(Structure):
    DomainControllerName: win32more.Windows.Win32.Foundation.PWSTR
    DomainControllerAddress: win32more.Windows.Win32.Foundation.PWSTR
    DomainControllerAddressType: UInt32
    DomainGuid: Guid
    DomainName: win32more.Windows.Win32.Foundation.PWSTR
    DnsForestName: win32more.Windows.Win32.Foundation.PWSTR
    Flags: UInt32
    DcSiteName: win32more.Windows.Win32.Foundation.PWSTR
    ClientSiteName: win32more.Windows.Win32.Foundation.PWSTR
DOMAIN_CONTROLLER_INFO = UnicodeAlias('DOMAIN_CONTROLLER_INFOW')
class DOMAIN_TREE(Structure):
    dsSize: UInt32
    dwCount: UInt32
    aDomains: win32more.Windows.Win32.Networking.ActiveDirectory.DOMAINDESC * 1
class DSA_NEWOBJ_DISPINFO(Structure):
    dwSize: UInt32
    hObjClassIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    lpszWizTitle: win32more.Windows.Win32.Foundation.PWSTR
    lpszContDisplayName: win32more.Windows.Win32.Foundation.PWSTR
class DSBITEMA(Structure):
    cbStruct: UInt32
    pszADsPath: win32more.Windows.Win32.Foundation.PWSTR
    pszClass: win32more.Windows.Win32.Foundation.PWSTR
    dwMask: UInt32
    dwState: UInt32
    dwStateMask: UInt32
    szDisplayName: win32more.Windows.Win32.Foundation.CHAR * 64
    szIconLocation: win32more.Windows.Win32.Foundation.CHAR * 260
    iIconResID: Int32
class DSBITEMW(Structure):
    cbStruct: UInt32
    pszADsPath: win32more.Windows.Win32.Foundation.PWSTR
    pszClass: win32more.Windows.Win32.Foundation.PWSTR
    dwMask: UInt32
    dwState: UInt32
    dwStateMask: UInt32
    szDisplayName: Char * 64
    szIconLocation: Char * 260
    iIconResID: Int32
DSBITEM = UnicodeAlias('DSBITEMW')
class DSBROWSEINFOA(Structure):
    cbStruct: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    pszCaption: win32more.Windows.Win32.Foundation.PSTR
    pszTitle: win32more.Windows.Win32.Foundation.PSTR
    pszRoot: win32more.Windows.Win32.Foundation.PWSTR
    pszPath: win32more.Windows.Win32.Foundation.PWSTR
    cchPath: UInt32
    dwFlags: UInt32
    pfnCallback: win32more.Windows.Win32.UI.Shell.BFFCALLBACK
    lParam: win32more.Windows.Win32.Foundation.LPARAM
    dwReturnFormat: UInt32
    pUserName: win32more.Windows.Win32.Foundation.PWSTR
    pPassword: win32more.Windows.Win32.Foundation.PWSTR
    pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR
    cchObjectClass: UInt32
class DSBROWSEINFOW(Structure):
    cbStruct: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    pszCaption: win32more.Windows.Win32.Foundation.PWSTR
    pszTitle: win32more.Windows.Win32.Foundation.PWSTR
    pszRoot: win32more.Windows.Win32.Foundation.PWSTR
    pszPath: win32more.Windows.Win32.Foundation.PWSTR
    cchPath: UInt32
    dwFlags: UInt32
    pfnCallback: win32more.Windows.Win32.UI.Shell.BFFCALLBACK
    lParam: win32more.Windows.Win32.Foundation.LPARAM
    dwReturnFormat: UInt32
    pUserName: win32more.Windows.Win32.Foundation.PWSTR
    pPassword: win32more.Windows.Win32.Foundation.PWSTR
    pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR
    cchObjectClass: UInt32
DSBROWSEINFO = UnicodeAlias('DSBROWSEINFOW')
class DSCLASSCREATIONINFO(Structure):
    dwFlags: UInt32
    clsidWizardDialog: Guid
    clsidWizardPrimaryPage: Guid
    cWizardExtensions: UInt32
    aWizardExtensions: Guid * 1
class DSCOLUMN(Structure):
    dwFlags: UInt32
    fmt: Int32
    cx: Int32
    idsName: Int32
    offsetProperty: Int32
    dwReserved: UInt32
class DSDISPLAYSPECOPTIONS(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    offsetAttribPrefix: UInt32
    offsetUserName: UInt32
    offsetPassword: UInt32
    offsetServer: UInt32
    offsetServerConfigPath: UInt32
class DSOBJECT(Structure):
    dwFlags: UInt32
    dwProviderFlags: UInt32
    offsetName: UInt32
    offsetClass: UInt32
class DSOBJECTNAMES(Structure):
    clsidNamespace: Guid
    cItems: UInt32
    aObjects: win32more.Windows.Win32.Networking.ActiveDirectory.DSOBJECT * 1
class DSOP_FILTER_FLAGS(Structure):
    Uplevel: win32more.Windows.Win32.Networking.ActiveDirectory.DSOP_UPLEVEL_FILTER_FLAGS
    flDownlevel: UInt32
class DSOP_INIT_INFO(Structure):
    cbSize: UInt32
    pwzTargetComputer: win32more.Windows.Win32.Foundation.PWSTR
    cDsScopeInfos: UInt32
    aDsScopeInfos: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DSOP_SCOPE_INIT_INFO)
    flOptions: UInt32
    cAttributesToFetch: UInt32
    apwzAttributeNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
class DSOP_SCOPE_INIT_INFO(Structure):
    cbSize: UInt32
    flType: UInt32
    flScope: UInt32
    FilterFlags: win32more.Windows.Win32.Networking.ActiveDirectory.DSOP_FILTER_FLAGS
    pwzDcName: win32more.Windows.Win32.Foundation.PWSTR
    pwzADsPath: win32more.Windows.Win32.Foundation.PWSTR
    hr: win32more.Windows.Win32.Foundation.HRESULT
class DSOP_UPLEVEL_FILTER_FLAGS(Structure):
    flBothModes: UInt32
    flMixedModeOnly: UInt32
    flNativeModeOnly: UInt32
class DSPROPERTYPAGEINFO(Structure):
    offsetString: UInt32
class DSQUERYCLASSLIST(Structure):
    cbStruct: UInt32
    cClasses: Int32
    offsetClass: UInt32 * 1
class DSQUERYINITPARAMS(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    pDefaultScope: win32more.Windows.Win32.Foundation.PWSTR
    pDefaultSaveLocation: win32more.Windows.Win32.Foundation.PWSTR
    pUserName: win32more.Windows.Win32.Foundation.PWSTR
    pPassword: win32more.Windows.Win32.Foundation.PWSTR
    pServer: win32more.Windows.Win32.Foundation.PWSTR
class DSQUERYPARAMS(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    offsetQuery: Int32
    iColumns: Int32
    dwReserved: UInt32
    aColumns: win32more.Windows.Win32.Networking.ActiveDirectory.DSCOLUMN * 1
DSROLE_MACHINE_ROLE = Int32
DsRole_RoleStandaloneWorkstation: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_MACHINE_ROLE = 0
DsRole_RoleMemberWorkstation: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_MACHINE_ROLE = 1
DsRole_RoleStandaloneServer: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_MACHINE_ROLE = 2
DsRole_RoleMemberServer: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_MACHINE_ROLE = 3
DsRole_RoleBackupDomainController: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_MACHINE_ROLE = 4
DsRole_RolePrimaryDomainController: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_MACHINE_ROLE = 5
DSROLE_OPERATION_STATE = Int32
DsRoleOperationIdle: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_OPERATION_STATE = 0
DsRoleOperationActive: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_OPERATION_STATE = 1
DsRoleOperationNeedReboot: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_OPERATION_STATE = 2
class DSROLE_OPERATION_STATE_INFO(Structure):
    OperationState: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_OPERATION_STATE
class DSROLE_PRIMARY_DOMAIN_INFO_BASIC(Structure):
    MachineRole: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_MACHINE_ROLE
    Flags: UInt32
    DomainNameFlat: win32more.Windows.Win32.Foundation.PWSTR
    DomainNameDns: win32more.Windows.Win32.Foundation.PWSTR
    DomainForestName: win32more.Windows.Win32.Foundation.PWSTR
    DomainGuid: Guid
DSROLE_PRIMARY_DOMAIN_INFO_LEVEL = Int32
DsRolePrimaryDomainInfoBasic: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_PRIMARY_DOMAIN_INFO_LEVEL = 1
DsRoleUpgradeStatus: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_PRIMARY_DOMAIN_INFO_LEVEL = 2
DsRoleOperationState: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_PRIMARY_DOMAIN_INFO_LEVEL = 3
DSROLE_SERVER_STATE = Int32
DsRoleServerUnknown: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_SERVER_STATE = 0
DsRoleServerPrimary: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_SERVER_STATE = 1
DsRoleServerBackup: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_SERVER_STATE = 2
class DSROLE_UPGRADE_STATUS_INFO(Structure):
    OperationState: UInt32
    PreviousServerState: win32more.Windows.Win32.Networking.ActiveDirectory.DSROLE_SERVER_STATE
class DS_DOMAIN_CONTROLLER_INFO_1A(Structure):
    NetbiosName: win32more.Windows.Win32.Foundation.PSTR
    DnsHostName: win32more.Windows.Win32.Foundation.PSTR
    SiteName: win32more.Windows.Win32.Foundation.PSTR
    ComputerObjectName: win32more.Windows.Win32.Foundation.PSTR
    ServerObjectName: win32more.Windows.Win32.Foundation.PSTR
    fIsPdc: win32more.Windows.Win32.Foundation.BOOL
    fDsEnabled: win32more.Windows.Win32.Foundation.BOOL
class DS_DOMAIN_CONTROLLER_INFO_1W(Structure):
    NetbiosName: win32more.Windows.Win32.Foundation.PWSTR
    DnsHostName: win32more.Windows.Win32.Foundation.PWSTR
    SiteName: win32more.Windows.Win32.Foundation.PWSTR
    ComputerObjectName: win32more.Windows.Win32.Foundation.PWSTR
    ServerObjectName: win32more.Windows.Win32.Foundation.PWSTR
    fIsPdc: win32more.Windows.Win32.Foundation.BOOL
    fDsEnabled: win32more.Windows.Win32.Foundation.BOOL
DS_DOMAIN_CONTROLLER_INFO_1 = UnicodeAlias('DS_DOMAIN_CONTROLLER_INFO_1W')
class DS_DOMAIN_CONTROLLER_INFO_2A(Structure):
    NetbiosName: win32more.Windows.Win32.Foundation.PSTR
    DnsHostName: win32more.Windows.Win32.Foundation.PSTR
    SiteName: win32more.Windows.Win32.Foundation.PSTR
    SiteObjectName: win32more.Windows.Win32.Foundation.PSTR
    ComputerObjectName: win32more.Windows.Win32.Foundation.PSTR
    ServerObjectName: win32more.Windows.Win32.Foundation.PSTR
    NtdsDsaObjectName: win32more.Windows.Win32.Foundation.PSTR
    fIsPdc: win32more.Windows.Win32.Foundation.BOOL
    fDsEnabled: win32more.Windows.Win32.Foundation.BOOL
    fIsGc: win32more.Windows.Win32.Foundation.BOOL
    SiteObjectGuid: Guid
    ComputerObjectGuid: Guid
    ServerObjectGuid: Guid
    NtdsDsaObjectGuid: Guid
class DS_DOMAIN_CONTROLLER_INFO_2W(Structure):
    NetbiosName: win32more.Windows.Win32.Foundation.PWSTR
    DnsHostName: win32more.Windows.Win32.Foundation.PWSTR
    SiteName: win32more.Windows.Win32.Foundation.PWSTR
    SiteObjectName: win32more.Windows.Win32.Foundation.PWSTR
    ComputerObjectName: win32more.Windows.Win32.Foundation.PWSTR
    ServerObjectName: win32more.Windows.Win32.Foundation.PWSTR
    NtdsDsaObjectName: win32more.Windows.Win32.Foundation.PWSTR
    fIsPdc: win32more.Windows.Win32.Foundation.BOOL
    fDsEnabled: win32more.Windows.Win32.Foundation.BOOL
    fIsGc: win32more.Windows.Win32.Foundation.BOOL
    SiteObjectGuid: Guid
    ComputerObjectGuid: Guid
    ServerObjectGuid: Guid
    NtdsDsaObjectGuid: Guid
DS_DOMAIN_CONTROLLER_INFO_2 = UnicodeAlias('DS_DOMAIN_CONTROLLER_INFO_2W')
class DS_DOMAIN_CONTROLLER_INFO_3A(Structure):
    NetbiosName: win32more.Windows.Win32.Foundation.PSTR
    DnsHostName: win32more.Windows.Win32.Foundation.PSTR
    SiteName: win32more.Windows.Win32.Foundation.PSTR
    SiteObjectName: win32more.Windows.Win32.Foundation.PSTR
    ComputerObjectName: win32more.Windows.Win32.Foundation.PSTR
    ServerObjectName: win32more.Windows.Win32.Foundation.PSTR
    NtdsDsaObjectName: win32more.Windows.Win32.Foundation.PSTR
    fIsPdc: win32more.Windows.Win32.Foundation.BOOL
    fDsEnabled: win32more.Windows.Win32.Foundation.BOOL
    fIsGc: win32more.Windows.Win32.Foundation.BOOL
    fIsRodc: win32more.Windows.Win32.Foundation.BOOL
    SiteObjectGuid: Guid
    ComputerObjectGuid: Guid
    ServerObjectGuid: Guid
    NtdsDsaObjectGuid: Guid
class DS_DOMAIN_CONTROLLER_INFO_3W(Structure):
    NetbiosName: win32more.Windows.Win32.Foundation.PWSTR
    DnsHostName: win32more.Windows.Win32.Foundation.PWSTR
    SiteName: win32more.Windows.Win32.Foundation.PWSTR
    SiteObjectName: win32more.Windows.Win32.Foundation.PWSTR
    ComputerObjectName: win32more.Windows.Win32.Foundation.PWSTR
    ServerObjectName: win32more.Windows.Win32.Foundation.PWSTR
    NtdsDsaObjectName: win32more.Windows.Win32.Foundation.PWSTR
    fIsPdc: win32more.Windows.Win32.Foundation.BOOL
    fDsEnabled: win32more.Windows.Win32.Foundation.BOOL
    fIsGc: win32more.Windows.Win32.Foundation.BOOL
    fIsRodc: win32more.Windows.Win32.Foundation.BOOL
    SiteObjectGuid: Guid
    ComputerObjectGuid: Guid
    ServerObjectGuid: Guid
    NtdsDsaObjectGuid: Guid
DS_DOMAIN_CONTROLLER_INFO_3 = UnicodeAlias('DS_DOMAIN_CONTROLLER_INFO_3W')
class DS_DOMAIN_TRUSTSA(Structure):
    NetbiosDomainName: win32more.Windows.Win32.Foundation.PSTR
    DnsDomainName: win32more.Windows.Win32.Foundation.PSTR
    Flags: UInt32
    ParentIndex: UInt32
    TrustType: UInt32
    TrustAttributes: UInt32
    DomainSid: win32more.Windows.Win32.Security.PSID
    DomainGuid: Guid
class DS_DOMAIN_TRUSTSW(Structure):
    NetbiosDomainName: win32more.Windows.Win32.Foundation.PWSTR
    DnsDomainName: win32more.Windows.Win32.Foundation.PWSTR
    Flags: UInt32
    ParentIndex: UInt32
    TrustType: UInt32
    TrustAttributes: UInt32
    DomainSid: win32more.Windows.Win32.Security.PSID
    DomainGuid: Guid
DS_DOMAIN_TRUSTS = UnicodeAlias('DS_DOMAIN_TRUSTSW')
DS_KCC_TASKID = Int32
DS_KCC_TASKID_UPDATE_TOPOLOGY: win32more.Windows.Win32.Networking.ActiveDirectory.DS_KCC_TASKID = 0
DS_MANGLE_FOR = Int32
DS_MANGLE_UNKNOWN: win32more.Windows.Win32.Networking.ActiveDirectory.DS_MANGLE_FOR = 0
DS_MANGLE_OBJECT_RDN_FOR_DELETION: win32more.Windows.Win32.Networking.ActiveDirectory.DS_MANGLE_FOR = 1
DS_MANGLE_OBJECT_RDN_FOR_NAME_CONFLICT: win32more.Windows.Win32.Networking.ActiveDirectory.DS_MANGLE_FOR = 2
DS_NAME_ERROR = Int32
DS_NAME_NO_ERROR: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_ERROR = 0
DS_NAME_ERROR_RESOLVING: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_ERROR = 1
DS_NAME_ERROR_NOT_FOUND: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_ERROR = 2
DS_NAME_ERROR_NOT_UNIQUE: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_ERROR = 3
DS_NAME_ERROR_NO_MAPPING: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_ERROR = 4
DS_NAME_ERROR_DOMAIN_ONLY: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_ERROR = 5
DS_NAME_ERROR_NO_SYNTACTICAL_MAPPING: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_ERROR = 6
DS_NAME_ERROR_TRUST_REFERRAL: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_ERROR = 7
DS_NAME_FLAGS = Int32
DS_NAME_NO_FLAGS: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FLAGS = 0
DS_NAME_FLAG_SYNTACTICAL_ONLY: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FLAGS = 1
DS_NAME_FLAG_EVAL_AT_DC: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FLAGS = 2
DS_NAME_FLAG_GCVERIFY: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FLAGS = 4
DS_NAME_FLAG_TRUST_REFERRAL: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FLAGS = 8
DS_NAME_FORMAT = Int32
DS_UNKNOWN_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT = 0
DS_FQDN_1779_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT = 1
DS_NT4_ACCOUNT_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT = 2
DS_DISPLAY_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT = 3
DS_UNIQUE_ID_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT = 6
DS_CANONICAL_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT = 7
DS_USER_PRINCIPAL_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT = 8
DS_CANONICAL_NAME_EX: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT = 9
DS_SERVICE_PRINCIPAL_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT = 10
DS_SID_OR_SID_HISTORY_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT = 11
DS_DNS_DOMAIN_NAME: win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_FORMAT = 12
class DS_NAME_RESULTA(Structure):
    cItems: UInt32
    rItems: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULT_ITEMA)
class DS_NAME_RESULTW(Structure):
    cItems: UInt32
    rItems: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_NAME_RESULT_ITEMW)
DS_NAME_RESULT = UnicodeAlias('DS_NAME_RESULTW')
class DS_NAME_RESULT_ITEMA(Structure):
    status: UInt32
    pDomain: win32more.Windows.Win32.Foundation.PSTR
    pName: win32more.Windows.Win32.Foundation.PSTR
class DS_NAME_RESULT_ITEMW(Structure):
    status: UInt32
    pDomain: win32more.Windows.Win32.Foundation.PWSTR
    pName: win32more.Windows.Win32.Foundation.PWSTR
DS_NAME_RESULT_ITEM = UnicodeAlias('DS_NAME_RESULT_ITEMW')
class DS_REPL_ATTR_META_DATA(Structure):
    pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR
    dwVersion: UInt32
    ftimeLastOriginatingChange: win32more.Windows.Win32.Foundation.FILETIME
    uuidLastOriginatingDsaInvocationID: Guid
    usnOriginatingChange: Int64
    usnLocalChange: Int64
class DS_REPL_ATTR_META_DATA_2(Structure):
    pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR
    dwVersion: UInt32
    ftimeLastOriginatingChange: win32more.Windows.Win32.Foundation.FILETIME
    uuidLastOriginatingDsaInvocationID: Guid
    usnOriginatingChange: Int64
    usnLocalChange: Int64
    pszLastOriginatingDsaDN: win32more.Windows.Win32.Foundation.PWSTR
class DS_REPL_ATTR_META_DATA_BLOB(Structure):
    oszAttributeName: UInt32
    dwVersion: UInt32
    ftimeLastOriginatingChange: win32more.Windows.Win32.Foundation.FILETIME
    uuidLastOriginatingDsaInvocationID: Guid
    usnOriginatingChange: Int64
    usnLocalChange: Int64
    oszLastOriginatingDsaDN: UInt32
class DS_REPL_ATTR_VALUE_META_DATA(Structure):
    cNumEntries: UInt32
    dwEnumerationContext: UInt32
    rgMetaData: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_VALUE_META_DATA * 1
class DS_REPL_ATTR_VALUE_META_DATA_2(Structure):
    cNumEntries: UInt32
    dwEnumerationContext: UInt32
    rgMetaData: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_VALUE_META_DATA_2 * 1
class DS_REPL_ATTR_VALUE_META_DATA_EXT(Structure):
    cNumEntries: UInt32
    dwEnumerationContext: UInt32
    rgMetaData: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_VALUE_META_DATA_EXT * 1
class DS_REPL_CURSOR(Structure):
    uuidSourceDsaInvocationID: Guid
    usnAttributeFilter: Int64
class DS_REPL_CURSORS(Structure):
    cNumCursors: UInt32
    dwReserved: UInt32
    rgCursor: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_CURSOR * 1
class DS_REPL_CURSORS_2(Structure):
    cNumCursors: UInt32
    dwEnumerationContext: UInt32
    rgCursor: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_CURSOR_2 * 1
class DS_REPL_CURSORS_3W(Structure):
    cNumCursors: UInt32
    dwEnumerationContext: UInt32
    rgCursor: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_CURSOR_3W * 1
class DS_REPL_CURSOR_2(Structure):
    uuidSourceDsaInvocationID: Guid
    usnAttributeFilter: Int64
    ftimeLastSyncSuccess: win32more.Windows.Win32.Foundation.FILETIME
class DS_REPL_CURSOR_3W(Structure):
    uuidSourceDsaInvocationID: Guid
    usnAttributeFilter: Int64
    ftimeLastSyncSuccess: win32more.Windows.Win32.Foundation.FILETIME
    pszSourceDsaDN: win32more.Windows.Win32.Foundation.PWSTR
class DS_REPL_CURSOR_BLOB(Structure):
    uuidSourceDsaInvocationID: Guid
    usnAttributeFilter: Int64
    ftimeLastSyncSuccess: win32more.Windows.Win32.Foundation.FILETIME
    oszSourceDsaDN: UInt32
DS_REPL_INFO_TYPE = Int32
DS_REPL_INFO_NEIGHBORS: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 0
DS_REPL_INFO_CURSORS_FOR_NC: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 1
DS_REPL_INFO_METADATA_FOR_OBJ: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 2
DS_REPL_INFO_KCC_DSA_CONNECT_FAILURES: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 3
DS_REPL_INFO_KCC_DSA_LINK_FAILURES: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 4
DS_REPL_INFO_PENDING_OPS: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 5
DS_REPL_INFO_METADATA_FOR_ATTR_VALUE: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 6
DS_REPL_INFO_CURSORS_2_FOR_NC: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 7
DS_REPL_INFO_CURSORS_3_FOR_NC: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 8
DS_REPL_INFO_METADATA_2_FOR_OBJ: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 9
DS_REPL_INFO_METADATA_2_FOR_ATTR_VALUE: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 10
DS_REPL_INFO_METADATA_EXT_FOR_ATTR_VALUE: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 11
DS_REPL_INFO_TYPE_MAX: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_INFO_TYPE = 12
class DS_REPL_KCC_DSA_FAILURESW(Structure):
    cNumEntries: UInt32
    dwReserved: UInt32
    rgDsaFailure: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_KCC_DSA_FAILUREW * 1
class DS_REPL_KCC_DSA_FAILUREW(Structure):
    pszDsaDN: win32more.Windows.Win32.Foundation.PWSTR
    uuidDsaObjGuid: Guid
    ftimeFirstFailure: win32more.Windows.Win32.Foundation.FILETIME
    cNumFailures: UInt32
    dwLastResult: UInt32
class DS_REPL_KCC_DSA_FAILUREW_BLOB(Structure):
    oszDsaDN: UInt32
    uuidDsaObjGuid: Guid
    ftimeFirstFailure: win32more.Windows.Win32.Foundation.FILETIME
    cNumFailures: UInt32
    dwLastResult: UInt32
class DS_REPL_NEIGHBORSW(Structure):
    cNumNeighbors: UInt32
    dwReserved: UInt32
    rgNeighbor: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_NEIGHBORW * 1
class DS_REPL_NEIGHBORW(Structure):
    pszNamingContext: win32more.Windows.Win32.Foundation.PWSTR
    pszSourceDsaDN: win32more.Windows.Win32.Foundation.PWSTR
    pszSourceDsaAddress: win32more.Windows.Win32.Foundation.PWSTR
    pszAsyncIntersiteTransportDN: win32more.Windows.Win32.Foundation.PWSTR
    dwReplicaFlags: UInt32
    dwReserved: UInt32
    uuidNamingContextObjGuid: Guid
    uuidSourceDsaObjGuid: Guid
    uuidSourceDsaInvocationID: Guid
    uuidAsyncIntersiteTransportObjGuid: Guid
    usnLastObjChangeSynced: Int64
    usnAttributeFilter: Int64
    ftimeLastSyncSuccess: win32more.Windows.Win32.Foundation.FILETIME
    ftimeLastSyncAttempt: win32more.Windows.Win32.Foundation.FILETIME
    dwLastSyncResult: UInt32
    cNumConsecutiveSyncFailures: UInt32
class DS_REPL_NEIGHBORW_BLOB(Structure):
    oszNamingContext: UInt32
    oszSourceDsaDN: UInt32
    oszSourceDsaAddress: UInt32
    oszAsyncIntersiteTransportDN: UInt32
    dwReplicaFlags: UInt32
    dwReserved: UInt32
    uuidNamingContextObjGuid: Guid
    uuidSourceDsaObjGuid: Guid
    uuidSourceDsaInvocationID: Guid
    uuidAsyncIntersiteTransportObjGuid: Guid
    usnLastObjChangeSynced: Int64
    usnAttributeFilter: Int64
    ftimeLastSyncSuccess: win32more.Windows.Win32.Foundation.FILETIME
    ftimeLastSyncAttempt: win32more.Windows.Win32.Foundation.FILETIME
    dwLastSyncResult: UInt32
    cNumConsecutiveSyncFailures: UInt32
class DS_REPL_OBJ_META_DATA(Structure):
    cNumEntries: UInt32
    dwReserved: UInt32
    rgMetaData: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_ATTR_META_DATA * 1
class DS_REPL_OBJ_META_DATA_2(Structure):
    cNumEntries: UInt32
    dwReserved: UInt32
    rgMetaData: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_ATTR_META_DATA_2 * 1
class DS_REPL_OPW(Structure):
    ftimeEnqueued: win32more.Windows.Win32.Foundation.FILETIME
    ulSerialNumber: UInt32
    ulPriority: UInt32
    OpType: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_OP_TYPE
    ulOptions: UInt32
    pszNamingContext: win32more.Windows.Win32.Foundation.PWSTR
    pszDsaDN: win32more.Windows.Win32.Foundation.PWSTR
    pszDsaAddress: win32more.Windows.Win32.Foundation.PWSTR
    uuidNamingContextObjGuid: Guid
    uuidDsaObjGuid: Guid
class DS_REPL_OPW_BLOB(Structure):
    ftimeEnqueued: win32more.Windows.Win32.Foundation.FILETIME
    ulSerialNumber: UInt32
    ulPriority: UInt32
    OpType: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_OP_TYPE
    ulOptions: UInt32
    oszNamingContext: UInt32
    oszDsaDN: UInt32
    oszDsaAddress: UInt32
    uuidNamingContextObjGuid: Guid
    uuidDsaObjGuid: Guid
DS_REPL_OP_TYPE = Int32
DS_REPL_OP_TYPE_SYNC: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_OP_TYPE = 0
DS_REPL_OP_TYPE_ADD: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_OP_TYPE = 1
DS_REPL_OP_TYPE_DELETE: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_OP_TYPE = 2
DS_REPL_OP_TYPE_MODIFY: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_OP_TYPE = 3
DS_REPL_OP_TYPE_UPDATE_REFS: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_OP_TYPE = 4
class DS_REPL_PENDING_OPSW(Structure):
    ftimeCurrentOpStarted: win32more.Windows.Win32.Foundation.FILETIME
    cNumPendingOps: UInt32
    rgPendingOp: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPL_OPW * 1
class DS_REPL_QUEUE_STATISTICSW(Structure):
    ftimeCurrentOpStarted: win32more.Windows.Win32.Foundation.FILETIME
    cNumPendingOps: UInt32
    ftimeOldestSync: win32more.Windows.Win32.Foundation.FILETIME
    ftimeOldestAdd: win32more.Windows.Win32.Foundation.FILETIME
    ftimeOldestMod: win32more.Windows.Win32.Foundation.FILETIME
    ftimeOldestDel: win32more.Windows.Win32.Foundation.FILETIME
    ftimeOldestUpdRefs: win32more.Windows.Win32.Foundation.FILETIME
class DS_REPL_VALUE_META_DATA(Structure):
    pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR
    pszObjectDn: win32more.Windows.Win32.Foundation.PWSTR
    cbData: UInt32
    pbData: POINTER(Byte)
    ftimeDeleted: win32more.Windows.Win32.Foundation.FILETIME
    ftimeCreated: win32more.Windows.Win32.Foundation.FILETIME
    dwVersion: UInt32
    ftimeLastOriginatingChange: win32more.Windows.Win32.Foundation.FILETIME
    uuidLastOriginatingDsaInvocationID: Guid
    usnOriginatingChange: Int64
    usnLocalChange: Int64
class DS_REPL_VALUE_META_DATA_2(Structure):
    pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR
    pszObjectDn: win32more.Windows.Win32.Foundation.PWSTR
    cbData: UInt32
    pbData: POINTER(Byte)
    ftimeDeleted: win32more.Windows.Win32.Foundation.FILETIME
    ftimeCreated: win32more.Windows.Win32.Foundation.FILETIME
    dwVersion: UInt32
    ftimeLastOriginatingChange: win32more.Windows.Win32.Foundation.FILETIME
    uuidLastOriginatingDsaInvocationID: Guid
    usnOriginatingChange: Int64
    usnLocalChange: Int64
    pszLastOriginatingDsaDN: win32more.Windows.Win32.Foundation.PWSTR
class DS_REPL_VALUE_META_DATA_BLOB(Structure):
    oszAttributeName: UInt32
    oszObjectDn: UInt32
    cbData: UInt32
    obData: UInt32
    ftimeDeleted: win32more.Windows.Win32.Foundation.FILETIME
    ftimeCreated: win32more.Windows.Win32.Foundation.FILETIME
    dwVersion: UInt32
    ftimeLastOriginatingChange: win32more.Windows.Win32.Foundation.FILETIME
    uuidLastOriginatingDsaInvocationID: Guid
    usnOriginatingChange: Int64
    usnLocalChange: Int64
    oszLastOriginatingDsaDN: UInt32
class DS_REPL_VALUE_META_DATA_BLOB_EXT(Structure):
    oszAttributeName: UInt32
    oszObjectDn: UInt32
    cbData: UInt32
    obData: UInt32
    ftimeDeleted: win32more.Windows.Win32.Foundation.FILETIME
    ftimeCreated: win32more.Windows.Win32.Foundation.FILETIME
    dwVersion: UInt32
    ftimeLastOriginatingChange: win32more.Windows.Win32.Foundation.FILETIME
    uuidLastOriginatingDsaInvocationID: Guid
    usnOriginatingChange: Int64
    usnLocalChange: Int64
    oszLastOriginatingDsaDN: UInt32
    dwUserIdentifier: UInt32
    dwPriorLinkState: UInt32
    dwCurrentLinkState: UInt32
class DS_REPL_VALUE_META_DATA_EXT(Structure):
    pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR
    pszObjectDn: win32more.Windows.Win32.Foundation.PWSTR
    cbData: UInt32
    pbData: POINTER(Byte)
    ftimeDeleted: win32more.Windows.Win32.Foundation.FILETIME
    ftimeCreated: win32more.Windows.Win32.Foundation.FILETIME
    dwVersion: UInt32
    ftimeLastOriginatingChange: win32more.Windows.Win32.Foundation.FILETIME
    uuidLastOriginatingDsaInvocationID: Guid
    usnOriginatingChange: Int64
    usnLocalChange: Int64
    pszLastOriginatingDsaDN: win32more.Windows.Win32.Foundation.PWSTR
    dwUserIdentifier: UInt32
    dwPriorLinkState: UInt32
    dwCurrentLinkState: UInt32
class DS_REPSYNCALL_ERRINFOA(Structure):
    pszSvrId: win32more.Windows.Win32.Foundation.PSTR
    error: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_ERROR
    dwWin32Err: UInt32
    pszSrcId: win32more.Windows.Win32.Foundation.PSTR
class DS_REPSYNCALL_ERRINFOW(Structure):
    pszSvrId: win32more.Windows.Win32.Foundation.PWSTR
    error: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_ERROR
    dwWin32Err: UInt32
    pszSrcId: win32more.Windows.Win32.Foundation.PWSTR
DS_REPSYNCALL_ERRINFO = UnicodeAlias('DS_REPSYNCALL_ERRINFOW')
DS_REPSYNCALL_ERROR = Int32
DS_REPSYNCALL_WIN32_ERROR_CONTACTING_SERVER: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_ERROR = 0
DS_REPSYNCALL_WIN32_ERROR_REPLICATING: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_ERROR = 1
DS_REPSYNCALL_SERVER_UNREACHABLE: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_ERROR = 2
DS_REPSYNCALL_EVENT = Int32
DS_REPSYNCALL_EVENT_ERROR: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_EVENT = 0
DS_REPSYNCALL_EVENT_SYNC_STARTED: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_EVENT = 1
DS_REPSYNCALL_EVENT_SYNC_COMPLETED: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_EVENT = 2
DS_REPSYNCALL_EVENT_FINISHED: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_EVENT = 3
class DS_REPSYNCALL_SYNCA(Structure):
    pszSrcId: win32more.Windows.Win32.Foundation.PSTR
    pszDstId: win32more.Windows.Win32.Foundation.PSTR
    pszNC: win32more.Windows.Win32.Foundation.PSTR
    pguidSrc: POINTER(Guid)
    pguidDst: POINTER(Guid)
class DS_REPSYNCALL_SYNCW(Structure):
    pszSrcId: win32more.Windows.Win32.Foundation.PWSTR
    pszDstId: win32more.Windows.Win32.Foundation.PWSTR
    pszNC: win32more.Windows.Win32.Foundation.PWSTR
    pguidSrc: POINTER(Guid)
    pguidDst: POINTER(Guid)
DS_REPSYNCALL_SYNC = UnicodeAlias('DS_REPSYNCALL_SYNCW')
class DS_REPSYNCALL_UPDATEA(Structure):
    event: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_EVENT
    pErrInfo: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_ERRINFOA)
    pSync: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_SYNCA)
class DS_REPSYNCALL_UPDATEW(Structure):
    event: win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_EVENT
    pErrInfo: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_ERRINFOW)
    pSync: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DS_REPSYNCALL_SYNCW)
DS_REPSYNCALL_UPDATE = UnicodeAlias('DS_REPSYNCALL_UPDATEW')
class DS_SCHEMA_GUID_MAPA(Structure):
    guid: Guid
    guidType: UInt32
    pName: win32more.Windows.Win32.Foundation.PSTR
class DS_SCHEMA_GUID_MAPW(Structure):
    guid: Guid
    guidType: UInt32
    pName: win32more.Windows.Win32.Foundation.PWSTR
DS_SCHEMA_GUID_MAP = UnicodeAlias('DS_SCHEMA_GUID_MAPW')
class DS_SELECTION(Structure):
    pwzName: win32more.Windows.Win32.Foundation.PWSTR
    pwzADsPath: win32more.Windows.Win32.Foundation.PWSTR
    pwzClass: win32more.Windows.Win32.Foundation.PWSTR
    pwzUPN: win32more.Windows.Win32.Foundation.PWSTR
    pvarFetchedAttributes: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)
    flScopeType: UInt32
class DS_SELECTION_LIST(Structure):
    cItems: UInt32
    cFetchedAttributes: UInt32
    aDsSelection: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SELECTION * 1
class DS_SITE_COST_INFO(Structure):
    errorCode: UInt32
    cost: UInt32
DS_SPN_NAME_TYPE = Int32
DS_SPN_DNS_HOST: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_NAME_TYPE = 0
DS_SPN_DN_HOST: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_NAME_TYPE = 1
DS_SPN_NB_HOST: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_NAME_TYPE = 2
DS_SPN_DOMAIN: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_NAME_TYPE = 3
DS_SPN_NB_DOMAIN: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_NAME_TYPE = 4
DS_SPN_SERVICE: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_NAME_TYPE = 5
DS_SPN_WRITE_OP = Int32
DS_SPN_ADD_SPN_OP: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_WRITE_OP = 0
DS_SPN_REPLACE_SPN_OP: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_WRITE_OP = 1
DS_SPN_DELETE_SPN_OP: win32more.Windows.Win32.Networking.ActiveDirectory.DS_SPN_WRITE_OP = 2
Email = Guid('{8f92a857-478e-11d1-a3b4-00c04fb950dc}')
FaxNumber = Guid('{a5062215-4681-11d1-a3b4-00c04fb950dc}')
Hold = Guid('{b3ad3e13-4080-11d1-a3ac-00c04fb950dc}')
class IADs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fd8256d0-fd15-11ce-abc4-02608c9e7553}')
    @commethod(7)
    def get_Name(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Class(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_GUID(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ADsPath(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Parent(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Schema(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInfo(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetInfo(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Get(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, pvProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Put(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, vProp: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetEx(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, pvProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def PutEx(self, lnControlCode: Int32, bstrName: win32more.Windows.Win32.Foundation.BSTR, vProp: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetInfoEx(self, vProperties: win32more.Windows.Win32.System.Variant.VARIANT, lnReserved: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsADSystemInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{5bb11929-afd1-11d2-9cb9-0000f87a369e}')
    @commethod(7)
    def get_UserName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ComputerName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SiteName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DomainShortName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DomainDNSName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ForestDNSName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_PDCRoleOwner(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_SchemaRoleOwner(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsNativeMode(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetAnyDCName(self, pszDCName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDCSiteName(self, szServer: win32more.Windows.Win32.Foundation.BSTR, pszSiteName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RefreshSchemaCache(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetTrees(self, pvTrees: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsAccessControlEntry(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b4f3a14c-9bdd-11d0-852c-00c04fd8d503}')
    @commethod(7)
    def get_AccessMask(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AccessMask(self, lnAccessMask: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AceType(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_AceType(self, lnAceType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AceFlags(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_AceFlags(self, lnAceFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Flags(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Flags(self, lnFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ObjectType(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ObjectType(self, bstrObjectType: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_InheritedObjectType(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_InheritedObjectType(self, bstrInheritedObjectType: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Trustee(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_Trustee(self, bstrTrustee: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsAccessControlList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b7ee91cc-9bdd-11d0-852c-00c04fd8d503}')
    @commethod(7)
    def get_AclRevision(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AclRevision(self, lnAclRevision: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AceCount(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_AceCount(self, lnAceCount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddAce(self, pAccessControlEntry: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveAce(self, pAccessControlEntry: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CopyAccessList(self, ppAccessControlList: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get__NewEnum(self, retval: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsAcl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8452d3ab-0869-11d1-a377-00c04fb950dc}')
    @commethod(7)
    def get_ProtectedAttrName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_ProtectedAttrName(self, bstrProtectedAttrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SubjectName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_SubjectName(self, bstrSubjectName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Privileges(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Privileges(self, lnPrivileges: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CopyAcl(self, ppAcl: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsAggregatee(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1346ce8c-9039-11d0-8528-00c04fd8d503}')
    @commethod(3)
    def ConnectAsAggregatee(self, pOuterUnknown: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisconnectAsAggregatee(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RelinquishInterface(self, riid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RestoreInterface(self, riid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsAggregator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{52db5fb0-941f-11d0-8529-00c04fd8d503}')
    @commethod(3)
    def ConnectAsAggregator(self, pAggregatee: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisconnectAsAggregator(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsBackLink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fd1302bd-4080-11d1-a3ac-00c04fb950dc}')
    @commethod(7)
    def get_RemoteID(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_RemoteID(self, lnRemoteID: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ObjectName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ObjectName(self, bstrObjectName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsCaseIgnoreList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7b66b533-4680-11d1-a3b4-00c04fb950dc}')
    @commethod(7)
    def get_CaseIgnoreList(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_CaseIgnoreList(self, vCaseIgnoreList: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsClass(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{c8f93dd0-4ae0-11cf-9e73-00aa004a5691}')
    @commethod(20)
    def get_PrimaryInterface(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_CLSID(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_CLSID(self, bstrCLSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_OID(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_OID(self, bstrOID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Abstract(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Abstract(self, fAbstract: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Auxiliary(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Auxiliary(self, fAuxiliary: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_MandatoryProperties(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_MandatoryProperties(self, vMandatoryProperties: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_OptionalProperties(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_OptionalProperties(self, vOptionalProperties: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_NamingProperties(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_NamingProperties(self, vNamingProperties: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_DerivedFrom(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_DerivedFrom(self, vDerivedFrom: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_AuxDerivedFrom(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_AuxDerivedFrom(self, vAuxDerivedFrom: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_PossibleSuperiors(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_PossibleSuperiors(self, vPossibleSuperiors: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_Containment(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_Containment(self, vContainment: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_Container(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def put_Container(self, fContainer: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_HelpFileName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_HelpFileName(self, bstrHelpFileName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_HelpFileContext(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def put_HelpFileContext(self, lnHelpFileContext: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def Qualifiers(self, ppQualifiers: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.IADsCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{72b945e0-253b-11cf-a988-00aa006bc149}')
    @commethod(7)
    def get__NewEnum(self, ppEnumerator: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Add(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, vItem: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Remove(self, bstrItemToBeRemoved: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetObject(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, pvItem: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsComputer(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{efe3cc70-1d9f-11cf-b1f3-02608c9e7553}')
    @commethod(20)
    def get_ComputerID(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Site(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Description(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Location(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Location(self, bstrLocation: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_PrimaryUser(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_PrimaryUser(self, bstrPrimaryUser: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Owner(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Owner(self, bstrOwner: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Division(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Division(self, bstrDivision: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_Department(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_Department(self, bstrDepartment: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_Role(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_Role(self, bstrRole: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_OperatingSystem(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_OperatingSystem(self, bstrOperatingSystem: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_OperatingSystemVersion(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_OperatingSystemVersion(self, bstrOperatingSystemVersion: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_Model(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_Model(self, bstrModel: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_Processor(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_Processor(self, bstrProcessor: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_ProcessorCount(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_ProcessorCount(self, bstrProcessorCount: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_MemorySize(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_MemorySize(self, bstrMemorySize: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_StorageCapacity(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_StorageCapacity(self, bstrStorageCapacity: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_NetAddresses(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def put_NetAddresses(self, vNetAddresses: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsComputerOperations(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{ef497680-1d9f-11cf-b1f3-02608c9e7553}')
    @commethod(20)
    def Status(self, ppObject: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Shutdown(self, bReboot: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsContainer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{001677d0-fd16-11ce-abc4-02608c9e7553}')
    @commethod(7)
    def get_Count(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, retval: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Filter(self, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Filter(self, Var: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Hints(self, pvFilter: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Hints(self, vHints: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetObject(self, ClassName: win32more.Windows.Win32.Foundation.BSTR, RelativeName: win32more.Windows.Win32.Foundation.BSTR, ppObject: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Create(self, ClassName: win32more.Windows.Win32.Foundation.BSTR, RelativeName: win32more.Windows.Win32.Foundation.BSTR, ppObject: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Delete(self, bstrClassName: win32more.Windows.Win32.Foundation.BSTR, bstrRelativeName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CopyHere(self, SourceName: win32more.Windows.Win32.Foundation.BSTR, NewName: win32more.Windows.Win32.Foundation.BSTR, ppObject: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def MoveHere(self, SourceName: win32more.Windows.Win32.Foundation.BSTR, NewName: win32more.Windows.Win32.Foundation.BSTR, ppObject: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsDNWithBinary(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7e99c0a2-f935-11d2-ba96-00c04fb6d0d1}')
    @commethod(7)
    def get_BinaryValue(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BinaryValue(self, vBinaryValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DNString(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_DNString(self, bstrDNString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsDNWithString(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{370df02e-f934-11d2-ba96-00c04fb6d0d1}')
    @commethod(7)
    def get_StringValue(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_StringValue(self, bstrStringValue: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DNString(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_DNString(self, bstrDNString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsDeleteOps(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b2bd0902-8878-11d1-8c21-00c04fd8d503}')
    @commethod(7)
    def DeleteObject(self, lnFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsDomain(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{00e4c220-fd16-11ce-abc4-02608c9e7553}')
    @commethod(20)
    def get_IsWorkgroup(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_MinPasswordLength(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_MinPasswordLength(self, lnMinPasswordLength: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_MinPasswordAge(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_MinPasswordAge(self, lnMinPasswordAge: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_MaxPasswordAge(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_MaxPasswordAge(self, lnMaxPasswordAge: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_MaxBadPasswordsAllowed(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_MaxBadPasswordsAllowed(self, lnMaxBadPasswordsAllowed: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_PasswordHistoryLength(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_PasswordHistoryLength(self, lnPasswordHistoryLength: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_PasswordAttributes(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_PasswordAttributes(self, lnPasswordAttributes: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_AutoUnlockInterval(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_AutoUnlockInterval(self, lnAutoUnlockInterval: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_LockoutObservationInterval(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_LockoutObservationInterval(self, lnLockoutObservationInterval: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsEmail(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{97af011a-478e-11d1-a3b4-00c04fb950dc}')
    @commethod(7)
    def get_Type(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Type(self, lnType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Address(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Address(self, bstrAddress: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsExtension(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d35553c-d2b0-11d1-b17b-0000f87593a0}')
    @commethod(3)
    def Operate(self, dwCode: UInt32, varData1: win32more.Windows.Win32.System.Variant.VARIANT, varData2: win32more.Windows.Win32.System.Variant.VARIANT, varData3: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PrivateGetIDsOfNames(self, riid: POINTER(Guid), rgszNames: POINTER(POINTER(UInt16)), cNames: UInt32, lcid: UInt32, rgDispid: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PrivateInvoke(self, dispidMember: Int32, riid: POINTER(Guid), lcid: UInt32, wFlags: UInt16, pdispparams: POINTER(win32more.Windows.Win32.System.Com.DISPPARAMS), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO), puArgErr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsFaxNumber(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a910dea9-4680-11d1-a3b4-00c04fb950dc}')
    @commethod(7)
    def get_TelephoneNumber(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_TelephoneNumber(self, bstrTelephoneNumber: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Parameters(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Parameters(self, vParameters: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsFileService(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADsService
    _iid_ = Guid('{a89d1900-31ca-11cf-a98a-00aa006bc149}')
    @commethod(44)
    def get_Description(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_MaxUserCount(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_MaxUserCount(self, lnMaxUserCount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsFileServiceOperations(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADsServiceOperations
    _iid_ = Guid('{a02ded10-31ca-11cf-a98a-00aa006bc149}')
    @commethod(26)
    def Sessions(self, ppSessions: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.IADsCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Resources(self, ppResources: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.IADsCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsFileShare(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{eb6dcaf0-4b83-11cf-a995-00aa006bc149}')
    @commethod(20)
    def get_CurrentUserCount(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Description(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_HostComputer(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_HostComputer(self, bstrHostComputer: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Path(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Path(self, bstrPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_MaxUserCount(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_MaxUserCount(self, lnMaxUserCount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsGroup(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{27636b00-410f-11cf-b1ff-02608c9e7553}')
    @commethod(20)
    def get_Description(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Members(self, ppMembers: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.IADsMembers)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def IsMember(self, bstrMember: win32more.Windows.Win32.Foundation.BSTR, bMember: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Add(self, bstrNewItem: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Remove(self, bstrItemToBeRemoved: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsHold(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b3eb3b37-4080-11d1-a3ac-00c04fb950dc}')
    @commethod(7)
    def get_ObjectName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_ObjectName(self, bstrObjectName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Amount(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Amount(self, lnAmount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsLargeInteger(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9068270b-0939-11d1-8be1-00c04fd8d503}')
    @commethod(7)
    def get_HighPart(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_HighPart(self, lnHighPart: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LowPart(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_LowPart(self, lnLowPart: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsLocality(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{a05e03a2-effe-11cf-8abc-00c04fd8d503}')
    @commethod(20)
    def get_Description(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_LocalityName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_LocalityName(self, bstrLocalityName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_PostalAddress(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_PostalAddress(self, bstrPostalAddress: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_SeeAlso(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_SeeAlso(self, vSeeAlso: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsMembers(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{451a0030-72ec-11cf-b03b-00aa006e0975}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, ppEnumerator: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Filter(self, pvFilter: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Filter(self, pvFilter: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsNameTranslate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b1b272a3-3625-11d1-a3a4-00c04fb950dc}')
    @commethod(7)
    def put_ChaseReferral(self, lnChaseReferral: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Init(self, lnSetType: Int32, bstrADsPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def InitEx(self, lnSetType: Int32, bstrADsPath: win32more.Windows.Win32.Foundation.BSTR, bstrUserID: win32more.Windows.Win32.Foundation.BSTR, bstrDomain: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Set(self, lnSetType: Int32, bstrADsPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Get(self, lnFormatType: Int32, pbstrADsPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetEx(self, lnFormatType: Int32, pvar: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEx(self, lnFormatType: Int32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsNamespaces(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{28b96ba0-b330-11cf-a9ad-00aa006bc149}')
    @commethod(20)
    def get_DefaultContainer(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_DefaultContainer(self, bstrDefaultContainer: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsNetAddress(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b21a50a9-4080-11d1-a3ac-00c04fb950dc}')
    @commethod(7)
    def get_AddressType(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AddressType(self, lnAddressType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Address(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Address(self, vAddress: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsO(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{a1cd2dc6-effe-11cf-8abc-00c04fd8d503}')
    @commethod(20)
    def get_Description(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_LocalityName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_LocalityName(self, bstrLocalityName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_PostalAddress(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_PostalAddress(self, bstrPostalAddress: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_TelephoneNumber(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_TelephoneNumber(self, bstrTelephoneNumber: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_FaxNumber(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_FaxNumber(self, bstrFaxNumber: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_SeeAlso(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_SeeAlso(self, vSeeAlso: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsOU(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{a2f733b8-effe-11cf-8abc-00c04fd8d503}')
    @commethod(20)
    def get_Description(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_LocalityName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_LocalityName(self, bstrLocalityName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_PostalAddress(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_PostalAddress(self, bstrPostalAddress: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_TelephoneNumber(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_TelephoneNumber(self, bstrTelephoneNumber: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_FaxNumber(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_FaxNumber(self, bstrFaxNumber: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_SeeAlso(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_SeeAlso(self, vSeeAlso: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_BusinessCategory(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_BusinessCategory(self, bstrBusinessCategory: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsObjectOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{46f14fda-232b-11d1-a808-00c04fd8d5a8}')
    @commethod(7)
    def GetOption(self, lnOption: Int32, pvValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetOption(self, lnOption: Int32, vValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsOctetList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7b28b80f-4680-11d1-a3b4-00c04fb950dc}')
    @commethod(7)
    def get_OctetList(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_OctetList(self, vOctetList: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsOpenDSObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ddf2891e-0f9c-11d0-8ad4-00c04fd8d503}')
    @commethod(7)
    def OpenDSObject(self, lpszDNName: win32more.Windows.Win32.Foundation.BSTR, lpszUserName: win32more.Windows.Win32.Foundation.BSTR, lpszPassword: win32more.Windows.Win32.Foundation.BSTR, lnReserved: Int32, ppOleDsObj: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsPath(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b287fcd5-4080-11d1-a3ac-00c04fb950dc}')
    @commethod(7)
    def get_Type(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Type(self, lnType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_VolumeName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_VolumeName(self, bstrVolumeName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Path(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Path(self, bstrPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsPathname(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d592aed4-f420-11d0-a36e-00c04fb950dc}')
    @commethod(7)
    def Set(self, bstrADsPath: win32more.Windows.Win32.Foundation.BSTR, lnSetType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDisplayType(self, lnDisplayType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Retrieve(self, lnFormatType: Int32, pbstrADsPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetNumElements(self, plnNumPathElements: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetElement(self, lnElementIndex: Int32, pbstrElement: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddLeafElement(self, bstrLeafElement: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RemoveLeafElement(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CopyPath(self, ppAdsPath: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetEscapedElement(self, lnReserved: Int32, bstrInStr: win32more.Windows.Win32.Foundation.BSTR, pbstrOutStr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_EscapedMode(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_EscapedMode(self, lnEscapedMode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsPostalAddress(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7adecf29-4680-11d1-a3b4-00c04fb950dc}')
    @commethod(7)
    def get_PostalAddress(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_PostalAddress(self, vPostalAddress: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsPrintJob(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{32fb6780-1ed0-11cf-a988-00aa006bc149}')
    @commethod(20)
    def get_HostPrintQueue(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_User(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_UserPath(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_TimeSubmitted(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_TotalPages(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Size(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_Description(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Priority(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Priority(self, lnPriority: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_StartTime(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_StartTime(self, daStartTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_UntilTime(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_UntilTime(self, daUntilTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_Notify(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_Notify(self, bstrNotify: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_NotifyPath(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_NotifyPath(self, bstrNotifyPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsPrintJobOperations(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{9a52db30-1ecf-11cf-a988-00aa006bc149}')
    @commethod(20)
    def get_Status(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TimeElapsed(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_PagesPrinted(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_Position(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_Position(self, lnPosition: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsPrintQueue(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{b15160d0-1226-11cf-a985-00aa006bc149}')
    @commethod(20)
    def get_PrinterPath(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_PrinterPath(self, bstrPrinterPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Model(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_Model(self, bstrModel: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Datatype(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Datatype(self, bstrDatatype: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_PrintProcessor(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_PrintProcessor(self, bstrPrintProcessor: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Description(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Location(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Location(self, bstrLocation: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_StartTime(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_StartTime(self, daStartTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_UntilTime(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_UntilTime(self, daUntilTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_DefaultJobPriority(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_DefaultJobPriority(self, lnDefaultJobPriority: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_Priority(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_Priority(self, lnPriority: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_BannerPage(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_BannerPage(self, bstrBannerPage: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_PrintDevices(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_PrintDevices(self, vPrintDevices: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_NetAddresses(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_NetAddresses(self, vNetAddresses: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsPrintQueueOperations(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{124be5c0-156e-11cf-a986-00aa006bc149}')
    @commethod(20)
    def get_Status(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def PrintJobs(self, pObject: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.IADsCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Purge(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsProperty(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{c8f93dd3-4ae0-11cf-9e73-00aa004a5691}')
    @commethod(20)
    def get_OID(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_OID(self, bstrOID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Syntax(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_Syntax(self, bstrSyntax: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_MaxRange(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_MaxRange(self, lnMaxRange: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_MinRange(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_MinRange(self, lnMinRange: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_MultiValued(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_MultiValued(self, fMultiValued: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Qualifiers(self, ppQualifiers: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.IADsCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsPropertyEntry(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{05792c8e-941f-11d0-8529-00c04fd8d503}')
    @commethod(7)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Name(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Name(self, bstrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ADsType(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_ADsType(self, lnADsType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ControlCode(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_ControlCode(self, lnControlCode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Values(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Values(self, vValues: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsPropertyList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c6f602b6-8f69-11d0-8528-00c04fd8d503}')
    @commethod(7)
    def get_PropertyCount(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Next(self, pVariant: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Skip(self, cElements: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Item(self, varIndex: win32more.Windows.Win32.System.Variant.VARIANT, pVariant: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPropertyItem(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, lnADsType: Int32, pVariant: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def PutPropertyItem(self, varData: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ResetPropertyItem(self, varEntry: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def PurgePropertyList(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsPropertyValue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{79fa9ad0-a97c-11d0-8534-00c04fd8d503}')
    @commethod(7)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ADsType(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_ADsType(self, lnADsType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DNString(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_DNString(self, bstrDNString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CaseExactString(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_CaseExactString(self, bstrCaseExactString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CaseIgnoreString(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_CaseIgnoreString(self, bstrCaseIgnoreString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_PrintableString(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_PrintableString(self, bstrPrintableString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_NumericString(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_NumericString(self, bstrNumericString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Boolean(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_Boolean(self, lnBoolean: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Integer(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_Integer(self, lnInteger: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_OctetString(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_OctetString(self, vOctetString: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_SecurityDescriptor(self, retval: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_SecurityDescriptor(self, pSecurityDescriptor: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_LargeInteger(self, retval: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_LargeInteger(self, pLargeInteger: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_UTCTime(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_UTCTime(self, daUTCTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsPropertyValue2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{306e831c-5bc7-11d1-a3b8-00c04fb950dc}')
    @commethod(7)
    def GetObjectProperty(self, lnADsType: POINTER(Int32), pvProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PutObjectProperty(self, lnADsType: Int32, vProp: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsReplicaPointer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f60fb803-4080-11d1-a3ac-00c04fb950dc}')
    @commethod(7)
    def get_ServerName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_ServerName(self, bstrServerName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ReplicaType(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ReplicaType(self, lnReplicaType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ReplicaNumber(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ReplicaNumber(self, lnReplicaNumber: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Count(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Count(self, lnCount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ReplicaAddressHints(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ReplicaAddressHints(self, vReplicaAddressHints: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsResource(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{34a05b20-4aab-11cf-ae2c-00aa006ebfb9}')
    @commethod(20)
    def get_User(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_UserPath(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Path(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_LockCount(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsSecurityDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b8c787ca-9bdd-11d0-852c-00c04fd8d503}')
    @commethod(7)
    def get_Revision(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Revision(self, lnRevision: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Control(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Control(self, lnControl: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Owner(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Owner(self, bstrOwner: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_OwnerDefaulted(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_OwnerDefaulted(self, fOwnerDefaulted: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Group(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Group(self, bstrGroup: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_GroupDefaulted(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_GroupDefaulted(self, fGroupDefaulted: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DiscretionaryAcl(self, retval: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_DiscretionaryAcl(self, pDiscretionaryAcl: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_DaclDefaulted(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DaclDefaulted(self, fDaclDefaulted: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_SystemAcl(self, retval: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_SystemAcl(self, pSystemAcl: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_SaclDefaulted(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_SaclDefaulted(self, fSaclDefaulted: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def CopySecurityDescriptor(self, ppSecurityDescriptor: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsSecurityUtility(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a63251b2-5f21-474b-ab52-4a8efad10895}')
    @commethod(7)
    def GetSecurityDescriptor(self, varPath: win32more.Windows.Win32.System.Variant.VARIANT, lPathFormat: Int32, lFormat: Int32, pVariant: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetSecurityDescriptor(self, varPath: win32more.Windows.Win32.System.Variant.VARIANT, lPathFormat: Int32, varData: win32more.Windows.Win32.System.Variant.VARIANT, lDataFormat: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ConvertSecurityDescriptor(self, varSD: win32more.Windows.Win32.System.Variant.VARIANT, lDataFormat: Int32, lOutFormat: Int32, pResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_SecurityMask(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_SecurityMask(self, lnSecurityMask: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsService(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{68af66e0-31ca-11cf-a98a-00aa006bc149}')
    @commethod(20)
    def get_HostComputer(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_HostComputer(self, bstrHostComputer: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_DisplayName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_DisplayName(self, bstrDisplayName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Version(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Version(self, bstrVersion: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_ServiceType(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_ServiceType(self, lnServiceType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_StartType(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_StartType(self, lnStartType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Path(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Path(self, bstrPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_StartupParameters(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_StartupParameters(self, bstrStartupParameters: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_ErrorControl(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_ErrorControl(self, lnErrorControl: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_LoadOrderGroup(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_LoadOrderGroup(self, bstrLoadOrderGroup: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_ServiceAccountName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_ServiceAccountName(self, bstrServiceAccountName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_ServiceAccountPath(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_ServiceAccountPath(self, bstrServiceAccountPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_Dependencies(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_Dependencies(self, vDependencies: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsServiceOperations(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{5d7b33f0-31ca-11cf-a98a-00aa006bc149}')
    @commethod(20)
    def get_Status(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Start(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Continue(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetPassword(self, bstrNewPassword: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsSession(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{398b7da0-4aab-11cf-ae2c-00aa006ebfb9}')
    @commethod(20)
    def get_User(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_UserPath(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Computer(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ComputerPath(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_ConnectTime(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_IdleTime(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsSyntax(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{c8f93dd2-4ae0-11cf-9e73-00aa004a5691}')
    @commethod(20)
    def get_OleAutoDataType(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_OleAutoDataType(self, lnOleAutoDataType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsTimestamp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b2f5a901-4080-11d1-a3ac-00c04fb950dc}')
    @commethod(7)
    def get_WholeSeconds(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_WholeSeconds(self, lnWholeSeconds: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EventID(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_EventID(self, lnEventID: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsTypedName(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b371a349-4080-11d1-a3ac-00c04fb950dc}')
    @commethod(7)
    def get_ObjectName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_ObjectName(self, bstrObjectName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Level(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Level(self, lnLevel: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Interval(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Interval(self, lnInterval: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsUser(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IADs
    _iid_ = Guid('{3e37e320-17e2-11cf-abc4-02608c9e7553}')
    @commethod(20)
    def get_BadLoginAddress(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_BadLoginCount(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_LastLogin(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_LastLogoff(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_LastFailedLogin(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_PasswordLastChanged(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_Description(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Division(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Division(self, bstrDivision: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Department(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Department(self, bstrDepartment: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_EmployeeID(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_EmployeeID(self, bstrEmployeeID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_FullName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_FullName(self, bstrFullName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_FirstName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_FirstName(self, bstrFirstName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_LastName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_LastName(self, bstrLastName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_OtherName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_OtherName(self, bstrOtherName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_NamePrefix(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_NamePrefix(self, bstrNamePrefix: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_NameSuffix(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_NameSuffix(self, bstrNameSuffix: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_Title(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_Title(self, bstrTitle: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_Manager(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_Manager(self, bstrManager: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_TelephoneHome(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def put_TelephoneHome(self, vTelephoneHome: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_TelephoneMobile(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def put_TelephoneMobile(self, vTelephoneMobile: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def get_TelephoneNumber(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def put_TelephoneNumber(self, vTelephoneNumber: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def get_TelephonePager(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def put_TelephonePager(self, vTelephonePager: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def get_FaxNumber(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def put_FaxNumber(self, vFaxNumber: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def get_OfficeLocations(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def put_OfficeLocations(self, vOfficeLocations: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def get_PostalAddresses(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def put_PostalAddresses(self, vPostalAddresses: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def get_PostalCodes(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def put_PostalCodes(self, vPostalCodes: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def get_SeeAlso(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def put_SeeAlso(self, vSeeAlso: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def get_AccountDisabled(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def put_AccountDisabled(self, fAccountDisabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def get_AccountExpirationDate(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def put_AccountExpirationDate(self, daAccountExpirationDate: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def get_GraceLoginsAllowed(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def put_GraceLoginsAllowed(self, lnGraceLoginsAllowed: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def get_GraceLoginsRemaining(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def put_GraceLoginsRemaining(self, lnGraceLoginsRemaining: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def get_IsAccountLocked(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def put_IsAccountLocked(self, fIsAccountLocked: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def get_LoginHours(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def put_LoginHours(self, vLoginHours: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def get_LoginWorkstations(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def put_LoginWorkstations(self, vLoginWorkstations: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def get_MaxLogins(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def put_MaxLogins(self, lnMaxLogins: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def get_MaxStorage(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def put_MaxStorage(self, lnMaxStorage: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def get_PasswordExpirationDate(self, retval: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def put_PasswordExpirationDate(self, daPasswordExpirationDate: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def get_PasswordMinimumLength(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def put_PasswordMinimumLength(self, lnPasswordMinimumLength: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def get_PasswordRequired(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(91)
    def put_PasswordRequired(self, fPasswordRequired: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def get_RequireUniquePassword(self, retval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def put_RequireUniquePassword(self, fRequireUniquePassword: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def get_EmailAddress(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def put_EmailAddress(self, bstrEmailAddress: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def get_HomeDirectory(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(97)
    def put_HomeDirectory(self, bstrHomeDirectory: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def get_Languages(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(99)
    def put_Languages(self, vLanguages: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(100)
    def get_Profile(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(101)
    def put_Profile(self, bstrProfile: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(102)
    def get_LoginScript(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(103)
    def put_LoginScript(self, bstrLoginScript: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(104)
    def get_Picture(self, retval: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(105)
    def put_Picture(self, vPicture: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(106)
    def get_HomePage(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(107)
    def put_HomePage(self, bstrHomePage: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(108)
    def Groups(self, ppGroups: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.IADsMembers)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(109)
    def SetPassword(self, NewPassword: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(110)
    def ChangePassword(self, bstrOldPassword: win32more.Windows.Win32.Foundation.BSTR, bstrNewPassword: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IADsWinNTSystemInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6c6d65dc-afd1-11d2-9cb9-0000f87a369e}')
    @commethod(7)
    def get_UserName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ComputerName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DomainName(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PDC(self, retval: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICommonQuery(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ab50dec0-6f1d-11d0-a1c4-00aa00c16e65}')
    @commethod(3)
    def OpenQueryWindow(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, pQueryWnd: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.OPENQUERYWINDOW), ppDataObject: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectoryObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e798de2c-22e4-11d0-84fe-00c04fd8d503}')
    @commethod(3)
    def GetObjectInformation(self, ppObjInfo: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_OBJECT_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObjectAttributes(self, pAttributeNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwNumberAttributes: UInt32, ppAttributeEntries: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ATTR_INFO)), pdwNumAttributesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetObjectAttributes(self, pAttributeEntries: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ATTR_INFO), dwNumAttributes: UInt32, pdwNumAttributesModified: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateDSObject(self, pszRDNName: win32more.Windows.Win32.Foundation.PWSTR, pAttributeEntries: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ATTR_INFO), dwNumAttributes: UInt32, ppObject: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DeleteDSObject(self, pszRDNName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectorySchemaMgmt(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75db3b9c-a4d8-11d0-a79c-00c04fd8d5a8}')
    @commethod(3)
    def EnumAttributes(self, ppszAttrNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwNumAttributes: UInt32, ppAttrDefinition: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ATTR_DEF)), pdwNumAttributes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateAttributeDefinition(self, pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR, pAttributeDefinition: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ATTR_DEF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WriteAttributeDefinition(self, pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR, pAttributeDefinition: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_ATTR_DEF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteAttributeDefinition(self, pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumClasses(self, ppszClassNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwNumClasses: UInt32, ppClassDefinition: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_CLASS_DEF)), pdwNumClasses: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WriteClassDefinition(self, pszClassName: win32more.Windows.Win32.Foundation.PWSTR, pClassDefinition: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_CLASS_DEF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateClassDefinition(self, pszClassName: win32more.Windows.Win32.Foundation.PWSTR, pClassDefinition: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_CLASS_DEF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteClassDefinition(self, pszClassName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectorySearch(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{109ba8ec-92f0-11d0-a790-00c04fd8d5a8}')
    @commethod(3)
    def SetSearchPreference(self, pSearchPrefs: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCHPREF_INFO), dwNumPrefs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ExecuteSearch(self, pszSearchFilter: win32more.Windows.Win32.Foundation.PWSTR, pAttributeNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwNumberAttributes: UInt32, phSearchResult: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCH_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AbandonSearch(self, phSearchResult: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCH_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFirstRow(self, hSearchResult: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCH_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNextRow(self, hSearchResult: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCH_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPreviousRow(self, hSearchResult: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCH_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNextColumnName(self, hSearchHandle: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCH_HANDLE, ppszColumnName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetColumn(self, hSearchResult: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCH_HANDLE, szColumnName: win32more.Windows.Win32.Foundation.PWSTR, pSearchColumn: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCH_COLUMN)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FreeColumn(self, pSearchColumn: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCH_COLUMN)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CloseSearchHandle(self, hSearchResult: win32more.Windows.Win32.Networking.ActiveDirectory.ADS_SEARCH_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDsAdminCreateObj(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{53554a38-f902-11d2-82b9-00c04f68928b}')
    @commethod(3)
    def Initialize(self, pADsContainerObj: win32more.Windows.Win32.Networking.ActiveDirectory.IADsContainer, pADsCopySource: win32more.Windows.Win32.Networking.ActiveDirectory.IADs, lpszClassName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateModal(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, ppADsObj: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.IADs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDsAdminNewObj(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f2573587-e6fc-11d2-82af-00c04f68928b}')
    @commethod(3)
    def SetButtons(self, nCurrIndex: UInt32, bValid: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPageCounts(self, pnTotal: POINTER(Int32), pnStartIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDsAdminNewObjExt(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6088eae2-e7bf-11d2-82af-00c04f68928b}')
    @commethod(3)
    def Initialize(self, pADsContainerObj: win32more.Windows.Win32.Networking.ActiveDirectory.IADsContainer, pADsCopySource: win32more.Windows.Win32.Networking.ActiveDirectory.IADs, lpszClassName: win32more.Windows.Win32.Foundation.PWSTR, pDsAdminNewObj: win32more.Windows.Win32.Networking.ActiveDirectory.IDsAdminNewObj, pDispInfo: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DSA_NEWOBJ_DISPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPages(self, lpfnAddPage: win32more.Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetObject(self, pADsObj: win32more.Windows.Win32.Networking.ActiveDirectory.IADs) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteData(self, hWnd: win32more.Windows.Win32.Foundation.HWND, uContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnError(self, hWnd: win32more.Windows.Win32.Foundation.HWND, hr: win32more.Windows.Win32.Foundation.HRESULT, uContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSummaryInfo(self, pBstrText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDsAdminNewObjPrimarySite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{be2b487e-f904-11d2-82b9-00c04f68928b}')
    @commethod(3)
    def CreateNew(self, pszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDsAdminNotifyHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e4a2b8b3-5a18-11d2-97c1-00a0c9a06d2d}')
    @commethod(3)
    def Initialize(self, pExtraInfo: win32more.Windows.Win32.System.Com.IDataObject, puEventFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Begin(self, uEvent: UInt32, pArg1: win32more.Windows.Win32.System.Com.IDataObject, pArg2: win32more.Windows.Win32.System.Com.IDataObject, puFlags: POINTER(UInt32), pBstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Notify(self, nItem: UInt32, uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def End(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDsBrowseDomainTree(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7cabcf1e-78f5-11d2-960c-00c04fa31a86}')
    @commethod(3)
    def BrowseTo(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, ppszTargetPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDomains(self, ppDomainTree: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DOMAIN_TREE)), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FreeDomains(self, ppDomainTree: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DOMAIN_TREE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FlushCachedDomains(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetComputer(self, pszComputerName: win32more.Windows.Win32.Foundation.PWSTR, pszUserName: win32more.Windows.Win32.Foundation.PWSTR, pszPassword: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDsDisplaySpecifier(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1ab4a8c0-6a0b-11d2-ad49-00c04fa31a86}')
    @commethod(3)
    def SetServer(self, pszServer: win32more.Windows.Win32.Foundation.PWSTR, pszUserName: win32more.Windows.Win32.Foundation.PWSTR, pszPassword: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLanguageID(self, langid: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDisplaySpecifier(self, pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIconLocation(self, pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszBuffer: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: Int32, presid: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetIcon(self, pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, cxIcon: Int32, cyIcon: Int32) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HICON: ...
    @commethod(8)
    def GetFriendlyClassName(self, pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, pszBuffer: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFriendlyAttributeName(self, pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR, pszBuffer: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsClassContainer(self, pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, pszADsPath: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(11)
    def GetClassCreationInfo(self, pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, ppdscci: POINTER(POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DSCLASSCREATIONINFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnumClassAttributes(self, pszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, pcbEnum: win32more.Windows.Win32.Networking.ActiveDirectory.LPDSENUMATTRIBUTES, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetAttributeADsType(self, pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Networking.ActiveDirectory.ADSTYPE: ...
class IDsObjectPicker(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0c87e64e-3b7a-11d2-b9e0-00c04fd8dbf7}')
    @commethod(3)
    def Initialize(self, pInitInfo: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.DSOP_INIT_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeDialog(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, ppdoSelections: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDsObjectPickerCredentials(ComPtr):
    extends: win32more.Windows.Win32.Networking.ActiveDirectory.IDsObjectPicker
    _iid_ = Guid('{e2d3ec9b-d041-445a-8f16-4748de8fb1cf}')
    @commethod(5)
    def SetCredentials(self, szUserName: win32more.Windows.Win32.Foundation.PWSTR, szPassword: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistQuery(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{1a3114b8-a62e-11d0-a6c5-00a0c906af45}')
    @commethod(4)
    def WriteString(self, pSection: win32more.Windows.Win32.Foundation.PWSTR, pValueName: win32more.Windows.Win32.Foundation.PWSTR, pValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReadString(self, pSection: win32more.Windows.Win32.Foundation.PWSTR, pValueName: win32more.Windows.Win32.Foundation.PWSTR, pBuffer: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteInt(self, pSection: win32more.Windows.Win32.Foundation.PWSTR, pValueName: win32more.Windows.Win32.Foundation.PWSTR, value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReadInt(self, pSection: win32more.Windows.Win32.Foundation.PWSTR, pValueName: win32more.Windows.Win32.Foundation.PWSTR, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WriteStruct(self, pSection: win32more.Windows.Win32.Foundation.PWSTR, pValueName: win32more.Windows.Win32.Foundation.PWSTR, pStruct: VoidPtr, cbStruct: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ReadStruct(self, pSection: win32more.Windows.Win32.Foundation.PWSTR, pValueName: win32more.Windows.Win32.Foundation.PWSTR, pStruct: VoidPtr, cbStruct: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrivateDispatch(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{86ab4bbe-65f6-11d1-8c13-00c04fd8d503}')
    @commethod(3)
    def ADSIInitializeDispatchManager(self, dwExtensionId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ADSIGetTypeInfoCount(self, pctinfo: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ADSIGetTypeInfo(self, itinfo: UInt32, lcid: UInt32, pptinfo: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ADSIGetIDsOfNames(self, riid: POINTER(Guid), rgszNames: POINTER(POINTER(UInt16)), cNames: UInt32, lcid: UInt32, rgdispid: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ADSIInvoke(self, dispidMember: Int32, riid: POINTER(Guid), lcid: UInt32, wFlags: UInt16, pdispparams: POINTER(win32more.Windows.Win32.System.Com.DISPPARAMS), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO), puArgErr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrivateUnknown(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{89126bab-6ead-11d1-8c18-00c04fd8d503}')
    @commethod(3)
    def ADSIInitializeObject(self, lpszUserName: win32more.Windows.Win32.Foundation.BSTR, lpszPassword: win32more.Windows.Win32.Foundation.BSTR, lnReserved: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ADSIReleaseObject(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQueryForm(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8cfcee30-39bd-11d0-b8d1-00a024ab2dbb}')
    @commethod(3)
    def Initialize(self, hkForm: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddForms(self, pAddFormsProc: win32more.Windows.Win32.Networking.ActiveDirectory.LPCQADDFORMSPROC, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddPages(self, pAddPagesProc: win32more.Windows.Win32.Networking.ActiveDirectory.LPCQADDPAGESPROC, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPCQADDFORMSPROC(lParam: win32more.Windows.Win32.Foundation.LPARAM, pForm: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.CQFORM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPCQADDPAGESPROC(lParam: win32more.Windows.Win32.Foundation.LPARAM, clsidForm: POINTER(Guid), pPage: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.CQPAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPCQPAGEPROC(pPage: POINTER(win32more.Windows.Win32.Networking.ActiveDirectory.CQPAGE), hwnd: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPDSENUMATTRIBUTES(lParam: win32more.Windows.Win32.Foundation.LPARAM, pszAttributeName: win32more.Windows.Win32.Foundation.PWSTR, pszDisplayName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LargeInteger = Guid('{927971f5-0939-11d1-8be1-00c04fd8d503}')
NameTranslate = Guid('{274fae1f-3626-11d1-a3a4-00c04fb950dc}')
NetAddress = Guid('{b0b71247-4080-11d1-a3ac-00c04fb950dc}')
class OPENQUERYWINDOW(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    clsidHandler: Guid
    pHandlerParameters: VoidPtr
    clsidDefaultForm: Guid
    pPersistQuery: win32more.Windows.Win32.Networking.ActiveDirectory.IPersistQuery
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        pFormParameters: VoidPtr
        ppbFormParameters: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag
OctetList = Guid('{1241400f-4680-11d1-a3b4-00c04fb950dc}')
Path = Guid('{b2538919-4080-11d1-a3ac-00c04fb950dc}')
Pathname = Guid('{080d0d78-f421-11d0-a36e-00c04fb950dc}')
PostalAddress = Guid('{0a75afcd-4680-11d1-a3b4-00c04fb950dc}')
PropertyEntry = Guid('{72d3edc2-a4c4-11d0-8533-00c04fd8d503}')
PropertyValue = Guid('{7b9e38b0-a97c-11d0-8534-00c04fd8d503}')
ReplicaPointer = Guid('{f5d1badf-4080-11d1-a3ac-00c04fb950dc}')
class SCHEDULE(Structure):
    Size: UInt32
    Bandwidth: UInt32
    NumberOfSchedules: UInt32
    Schedules: win32more.Windows.Win32.Networking.ActiveDirectory.SCHEDULE_HEADER * 1
class SCHEDULE_HEADER(Structure):
    Type: UInt32
    Offset: UInt32
SecurityDescriptor = Guid('{b958f73c-9bdd-11d0-852c-00c04fd8d503}')
Timestamp = Guid('{b2bed2eb-4080-11d1-a3ac-00c04fb950dc}')
TypedName = Guid('{b33143cb-4080-11d1-a3ac-00c04fb950dc}')
WinNTSystemInfo = Guid('{66182ec4-afd1-11d2-9cb9-0000f87a369e}')


make_ready(__name__)
