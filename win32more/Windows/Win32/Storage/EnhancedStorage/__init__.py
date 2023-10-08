from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.PortableDevices
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.EnhancedStorage
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ACT_AUTHORIZATION_STATE(EasyCastStructure):
    ulState: UInt32
ACT_AUTHORIZATION_STATE_VALUE = Int32
ACT_UNAUTHORIZED: ACT_AUTHORIZATION_STATE_VALUE = 0
ACT_AUTHORIZED: ACT_AUTHORIZATION_STATE_VALUE = 1
GUID_DEVINTERFACE_ENHANCED_STORAGE_SILO: Guid = Guid('{3897f6a4-fd35-4bc8-a0b7-5dbba36adafa}')
WPD_CATEGORY_ENHANCED_STORAGE: Guid = Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}')
def ENHANCED_STORAGE_COMMAND_SILO_IS_AUTHENTICATION_SILO():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=6)
def ENHANCED_STORAGE_COMMAND_SILO_GET_AUTHENTICATION_STATE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=7)
def ENHANCED_STORAGE_COMMAND_SILO_ENUMERATE_SILOS():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=11)
def ENHANCED_STORAGE_COMMAND_CERT_HOST_CERTIFICATE_AUTHENTICATION():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=101)
def ENHANCED_STORAGE_COMMAND_CERT_DEVICE_CERTIFICATE_AUTHENTICATION():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=102)
def ENHANCED_STORAGE_COMMAND_CERT_ADMIN_CERTIFICATE_AUTHENTICATION():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=103)
def ENHANCED_STORAGE_COMMAND_CERT_INITIALIZE_TO_MANUFACTURER_STATE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=104)
def ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE_COUNT():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=105)
def ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=106)
def ENHANCED_STORAGE_COMMAND_CERT_SET_CERTIFICATE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=107)
def ENHANCED_STORAGE_COMMAND_CERT_CREATE_CERTIFICATE_REQUEST():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=108)
def ENHANCED_STORAGE_COMMAND_CERT_UNAUTHENTICATION():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=110)
def ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITY():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=111)
def ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITIES():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=112)
def ENHANCED_STORAGE_COMMAND_CERT_GET_ACT_FRIENDLY_NAME():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=113)
def ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_GUID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=114)
def ENHANCED_STORAGE_COMMAND_PASSWORD_AUTHORIZE_ACT_ACCESS():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=203)
def ENHANCED_STORAGE_COMMAND_PASSWORD_UNAUTHORIZE_ACT_ACCESS():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=204)
def ENHANCED_STORAGE_COMMAND_PASSWORD_QUERY_INFORMATION():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=205)
def ENHANCED_STORAGE_COMMAND_PASSWORD_CONFIG_ADMINISTRATOR():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=206)
def ENHANCED_STORAGE_COMMAND_PASSWORD_CREATE_USER():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=207)
def ENHANCED_STORAGE_COMMAND_PASSWORD_DELETE_USER():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=208)
def ENHANCED_STORAGE_COMMAND_PASSWORD_CHANGE_PASSWORD():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=209)
def ENHANCED_STORAGE_COMMAND_PASSWORD_INITIALIZE_USER_PASSWORD():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=210)
def ENHANCED_STORAGE_COMMAND_PASSWORD_START_INITIALIZE_TO_MANUFACTURER_STATE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=211)
def ENHANCED_STORAGE_PROPERTY_AUTHENTICATION_STATE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=1006)
ENHANCED_STORAGE_AUTHN_STATE_UNKNOWN: UInt32 = 0
ENHANCED_STORAGE_AUTHN_STATE_NO_AUTHENTICATION_REQUIRED: UInt32 = 1
ENHANCED_STORAGE_AUTHN_STATE_NOT_AUTHENTICATED: UInt32 = 2
ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATED: UInt32 = 3
ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATION_DENIED: UInt32 = 2147483649
ENHANCED_STORAGE_AUTHN_STATE_DEVICE_ERROR: UInt32 = 2147483650
def ENHANCED_STORAGE_PROPERTY_IS_AUTHENTICATION_SILO():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=1009)
def ENHANCED_STORAGE_PROPERTY_TEMPORARY_UNAUTHENTICATION():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=1010)
def ENHANCED_STORAGE_PROPERTY_MAX_AUTH_FAILURES():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2001)
def ENHANCED_STORAGE_PROPERTY_PASSWORD():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2004)
def ENHANCED_STORAGE_PROPERTY_OLD_PASSWORD():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2005)
def ENHANCED_STORAGE_PROPERTY_PASSWORD_INDICATOR():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2006)
def ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD_INDICATOR():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2007)
def ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2008)
def ENHANCED_STORAGE_PROPERTY_USER_HINT():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2009)
def ENHANCED_STORAGE_PROPERTY_USER_NAME():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2010)
def ENHANCED_STORAGE_PROPERTY_ADMIN_HINT():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2011)
def ENHANCED_STORAGE_PROPERTY_SILO_NAME():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2012)
def ENHANCED_STORAGE_PROPERTY_SILO_FRIENDLYNAME_SPECIFIED():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2013)
def ENHANCED_STORAGE_PROPERTY_PASSWORD_SILO_INFO():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2014)
def ENHANCED_STORAGE_PROPERTY_SECURITY_IDENTIFIER():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2015)
def ENHANCED_STORAGE_PROPERTY_QUERY_SILO_TYPE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2016)
def ENHANCED_STORAGE_PROPERTY_QUERY_SILO_RESULTS():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=2017)
def ENHANCED_STORAGE_PROPERTY_MAX_CERTIFICATE_COUNT():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3001)
def ENHANCED_STORAGE_PROPERTY_STORED_CERTIFICATE_COUNT():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3002)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_INDEX():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3003)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_TYPE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3004)
CERT_TYPE_EMPTY: UInt32 = 0
CERT_TYPE_ASCm: UInt32 = 1
CERT_TYPE_PCp: UInt32 = 2
CERT_TYPE_ASCh: UInt32 = 3
CERT_TYPE_HCh: UInt32 = 4
CERT_TYPE_SIGNER: UInt32 = 6
def ENHANCED_STORAGE_PROPERTY_VALIDATION_POLICY():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3005)
CERT_VALIDATION_POLICY_RESERVED: UInt32 = 0
CERT_VALIDATION_POLICY_NONE: UInt32 = 1
CERT_VALIDATION_POLICY_BASIC: UInt32 = 2
CERT_VALIDATION_POLICY_EXTENDED: UInt32 = 3
def ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_INDEX():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3006)
def ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_OF_TYPE_INDEX():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3007)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_LENGTH():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3008)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3009)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_REQUEST():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3010)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_CAPABILITY_TYPE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3011)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITY():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3012)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITIES():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3013)
CERT_CAPABILITY_HASH_ALG: UInt32 = 1
CERT_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY: UInt32 = 2
CERT_CAPABILITY_SIGNATURE_ALG: UInt32 = 3
CERT_CAPABILITY_CERTIFICATE_SUPPORT: UInt32 = 4
CERT_CAPABILITY_OPTIONAL_FEATURES: UInt32 = 5
CERT_MAX_CAPABILITY: UInt32 = 255
CERT_RSA_1024_OID: String = '1.2.840.113549.1.1.1,1024'
CERT_RSA_2048_OID: String = '1.2.840.113549.1.1.1,2048'
CERT_RSA_3072_OID: String = '1.2.840.113549.1.1.1,3072'
CERT_RSASSA_PSS_SHA1_OID: String = '1.2.840.113549.1.1.10,1.3.14.3.2.26'
CERT_RSASSA_PSS_SHA256_OID: String = '1.2.840.113549.1.1.10,2.16.840.1.101.3.4.2.1'
CERT_RSASSA_PSS_SHA384_OID: String = '1.2.840.113549.1.1.10,2.16.840.1.101.3.4.2.2'
CERT_RSASSA_PSS_SHA512_OID: String = '1.2.840.113549.1.1.10,2.16.840.1.101.3.4.2.3'
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_ACT_FRIENDLY_NAME():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3014)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_GUID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3015)
def ENHANCED_STORAGE_PROPERTY_SIGNER_CERTIFICATE_INDEX():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=3016)
def ENHANCED_STORAGE_CAPABILITY_HASH_ALGS():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=4001)
def ENHANCED_STORAGE_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=4002)
def ENHANCED_STORAGE_CAPABILITY_SIGNING_ALGS():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=4003)
def ENHANCED_STORAGE_CAPABILITY_RENDER_USER_DATA_UNUSABLE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=4004)
def ENHANCED_STORAGE_CAPABILITY_CERTIFICATE_EXTENSION_PARSING():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91248166-b832-4ad4-baa4-7ca0b6b2798c}'), pid=4005)
def PKEY_Address_Country():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c07b4199-e1df-4493-b1e1-de5946fb58f8}'), pid=100)
def PKEY_Address_CountryCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c07b4199-e1df-4493-b1e1-de5946fb58f8}'), pid=101)
def PKEY_Address_Region():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c07b4199-e1df-4493-b1e1-de5946fb58f8}'), pid=102)
def PKEY_Address_RegionCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c07b4199-e1df-4493-b1e1-de5946fb58f8}'), pid=103)
def PKEY_Address_Town():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c07b4199-e1df-4493-b1e1-de5946fb58f8}'), pid=104)
def PKEY_Audio_ChannelCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440490-4c8b-11d1-8b70-080036b11a03}'), pid=7)
AUDIO_CHANNELCOUNT_MONO: UInt32 = 1
AUDIO_CHANNELCOUNT_STEREO: UInt32 = 2
def PKEY_Audio_Compression():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440490-4c8b-11d1-8b70-080036b11a03}'), pid=10)
def PKEY_Audio_EncodingBitrate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440490-4c8b-11d1-8b70-080036b11a03}'), pid=4)
def PKEY_Audio_Format():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440490-4c8b-11d1-8b70-080036b11a03}'), pid=2)
def PKEY_Audio_IsVariableBitRate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e6822fee-8c17-4d62-823c-8e9cfcbd1d5c}'), pid=100)
def PKEY_Audio_PeakValue():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2579e5d0-1116-4084-bd9a-9b4f7cb4df5e}'), pid=100)
def PKEY_Audio_SampleRate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440490-4c8b-11d1-8b70-080036b11a03}'), pid=5)
def PKEY_Audio_SampleSize():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440490-4c8b-11d1-8b70-080036b11a03}'), pid=6)
def PKEY_Audio_StreamName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440490-4c8b-11d1-8b70-080036b11a03}'), pid=9)
def PKEY_Audio_StreamNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440490-4c8b-11d1-8b70-080036b11a03}'), pid=8)
def PKEY_Calendar_Duration():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{293ca35a-09aa-4dd2-b180-1fe245728a52}'), pid=100)
def PKEY_Calendar_IsOnline():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bfee9149-e3e2-49a7-a862-c05988145cec}'), pid=100)
def PKEY_Calendar_IsRecurring():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{315b9c8d-80a9-4ef9-ae16-8e746da51d70}'), pid=100)
def PKEY_Calendar_Location():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f6272d18-cecc-40b1-b26a-3911717aa7bd}'), pid=100)
def PKEY_Calendar_OptionalAttendeeAddresses():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d55bae5a-3892-417a-a649-c6ac5aaaeab3}'), pid=100)
def PKEY_Calendar_OptionalAttendeeNames():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{09429607-582d-437f-84c3-de93a2b24c3c}'), pid=100)
def PKEY_Calendar_OrganizerAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{744c8242-4df5-456c-ab9e-014efb9021e3}'), pid=100)
def PKEY_Calendar_OrganizerName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{aaa660f9-9865-458e-b484-01bc7fe3973e}'), pid=100)
def PKEY_Calendar_ReminderTime():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{72fc5ba4-24f9-4011-9f3f-add27afad818}'), pid=100)
def PKEY_Calendar_RequiredAttendeeAddresses():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0ba7d6c3-568d-4159-ab91-781a91fb71e5}'), pid=100)
def PKEY_Calendar_RequiredAttendeeNames():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b33af30b-f552-4584-936c-cb93e5cda29f}'), pid=100)
def PKEY_Calendar_Resources():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f58a38-c54b-4c40-8696-97235980eae1}'), pid=100)
def PKEY_Calendar_ResponseStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{188c1f91-3c40-4132-9ec5-d8b03b72a8a2}'), pid=100)
def PKEY_Calendar_ShowTimeAs():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5bf396d4-5eb2-466f-bde9-2fb3f2361d6e}'), pid=100)
def PKEY_Calendar_ShowTimeAsText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{53da57cf-62c0-45c4-81de-7610bcefd7f5}'), pid=100)
def PKEY_Communication_AccountName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=9)
def PKEY_Communication_DateItemExpires():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{428040ac-a177-4c8a-9760-f6f761227f9a}'), pid=100)
def PKEY_Communication_Direction():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8e531030-b960-4346-ae0d-66bc9a86fb94}'), pid=100)
def PKEY_Communication_FollowupIconIndex():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{83a6347e-6fe4-4f40-ba9c-c4865240d1f4}'), pid=100)
def PKEY_Communication_HeaderItem():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9c34f84-2241-4401-b607-bd20ed75ae7f}'), pid=100)
def PKEY_Communication_PolicyTag():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ec0b4191-ab0b-4c66-90b6-c6637cdebbab}'), pid=100)
def PKEY_Communication_SecurityFlags():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8619a4b6-9f4d-4429-8c0f-b996ca59e335}'), pid=100)
def PKEY_Communication_Suffix():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{807b653a-9e91-43ef-8f97-11ce04ee20c5}'), pid=100)
def PKEY_Communication_TaskStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{be1a72c6-9a1d-46b7-afe7-afaf8cef4999}'), pid=100)
def PKEY_Communication_TaskStatusText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a6744477-c237-475b-a075-54f34498292a}'), pid=100)
def PKEY_Computer_DecoratedFreeSpace():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9b174b35-40ff-11d2-a27e-00c04fc30871}'), pid=7)
def PKEY_Contact_AccountPictureDynamicVideo():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0b8bb018-2725-4b44-92ba-7933aeb2dde7}'), pid=2)
def PKEY_Contact_AccountPictureLarge():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0b8bb018-2725-4b44-92ba-7933aeb2dde7}'), pid=3)
def PKEY_Contact_AccountPictureSmall():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0b8bb018-2725-4b44-92ba-7933aeb2dde7}'), pid=4)
def PKEY_Contact_Anniversary():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9ad5badb-cea7-4470-a03d-b84e51b9949e}'), pid=100)
def PKEY_Contact_AssistantName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cd102c9c-5540-4a88-a6f6-64e4981c8cd1}'), pid=100)
def PKEY_Contact_AssistantTelephone():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9a93244d-a7ad-4ff8-9b99-45ee4cc09af6}'), pid=100)
def PKEY_Contact_Birthday():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=47)
def PKEY_Contact_BusinessAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{730fb6dd-cf7c-426b-a03f-bd166cc9ee24}'), pid=100)
def PKEY_Contact_BusinessAddress1Country():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=119)
def PKEY_Contact_BusinessAddress1Locality():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=117)
def PKEY_Contact_BusinessAddress1PostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=120)
def PKEY_Contact_BusinessAddress1Region():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=118)
def PKEY_Contact_BusinessAddress1Street():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=116)
def PKEY_Contact_BusinessAddress2Country():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=124)
def PKEY_Contact_BusinessAddress2Locality():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=122)
def PKEY_Contact_BusinessAddress2PostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=125)
def PKEY_Contact_BusinessAddress2Region():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=123)
def PKEY_Contact_BusinessAddress2Street():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=121)
def PKEY_Contact_BusinessAddress3Country():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=129)
def PKEY_Contact_BusinessAddress3Locality():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=127)
def PKEY_Contact_BusinessAddress3PostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=130)
def PKEY_Contact_BusinessAddress3Region():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=128)
def PKEY_Contact_BusinessAddress3Street():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=126)
def PKEY_Contact_BusinessAddressCity():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{402b5934-ec5a-48c3-93e6-85e86a2d934e}'), pid=100)
def PKEY_Contact_BusinessAddressCountry():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b0b87314-fcf6-4feb-8dff-a50da6af561c}'), pid=100)
def PKEY_Contact_BusinessAddressPostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e1d4a09e-d758-4cd1-b6ec-34a8b5a73f80}'), pid=100)
def PKEY_Contact_BusinessAddressPostOfficeBox():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bc4e71ce-17f9-48d5-bee9-021df0ea5409}'), pid=100)
def PKEY_Contact_BusinessAddressState():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{446f787f-10c4-41cb-a6c4-4d0343551597}'), pid=100)
def PKEY_Contact_BusinessAddressStreet():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ddd1460f-c0bf-4553-8ce4-10433c908fb0}'), pid=100)
def PKEY_Contact_BusinessEmailAddresses():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f271c659-7e5e-471f-ba25-7f77b286f836}'), pid=100)
def PKEY_Contact_BusinessFaxNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{91eff6f3-2e27-42ca-933e-7c999fbe310b}'), pid=100)
def PKEY_Contact_BusinessHomePage():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56310920-2491-4919-99ce-eadb06fafdb2}'), pid=100)
def PKEY_Contact_BusinessTelephone():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6a15e5a0-0a1e-4cd7-bb8c-d2f1b0c929bc}'), pid=100)
def PKEY_Contact_CallbackTelephone():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf53d1c3-49e0-4f7f-8567-5a821d8ac542}'), pid=100)
def PKEY_Contact_CarTelephone():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8fdc6dea-b929-412b-ba90-397a257465fe}'), pid=100)
def PKEY_Contact_Children():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d4729704-8ef1-43ef-9024-2bd381187fd5}'), pid=100)
def PKEY_Contact_CompanyMainTelephone():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8589e481-6040-473d-b171-7fa89c2708ed}'), pid=100)
def PKEY_Contact_ConnectedServiceDisplayName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{39b77f4f-a104-4863-b395-2db2ad8f7bc1}'), pid=100)
def PKEY_Contact_ConnectedServiceIdentities():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{80f41eb8-afc4-4208-aa5f-cce21a627281}'), pid=100)
def PKEY_Contact_ConnectedServiceName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b5c84c9e-5927-46b5-a3cc-933c21b78469}'), pid=100)
def PKEY_Contact_ConnectedServiceSupportedActions():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a19fb7a9-024b-4371-a8bf-4d29c3e4e9c9}'), pid=100)
def PKEY_Contact_DataSuppliers():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9660c283-fc3a-4a08-a096-eed3aac46da2}'), pid=100)
def PKEY_Contact_Department():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fc9f7306-ff8f-4d49-9fb6-3ffe5c0951ec}'), pid=100)
def PKEY_Contact_DisplayBusinessPhoneNumbers():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{364028da-d895-41fe-a584-302b1bb70a76}'), pid=100)
def PKEY_Contact_DisplayHomePhoneNumbers():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5068bcdf-d697-4d85-8c53-1f1cdab01763}'), pid=100)
def PKEY_Contact_DisplayMobilePhoneNumbers():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9cb0c358-9d7a-46b1-b466-dcc6f1a3d93d}'), pid=100)
def PKEY_Contact_DisplayOtherPhoneNumbers():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{03089873-8ee8-4191-bd60-d31f72b7900b}'), pid=100)
def PKEY_Contact_EmailAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f8fa7fa3-d12b-4785-8a4e-691a94f7a3e7}'), pid=100)
def PKEY_Contact_EmailAddress2():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{38965063-edc8-4268-8491-b7723172cf29}'), pid=100)
def PKEY_Contact_EmailAddress3():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{644d37b4-e1b3-4bad-b099-7e7c04966aca}'), pid=100)
def PKEY_Contact_EmailAddresses():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84d8f337-981d-44b3-9615-c7596dba17e3}'), pid=100)
def PKEY_Contact_EmailName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cc6f4f24-6083-4bd4-8754-674d0de87ab8}'), pid=100)
def PKEY_Contact_FileAsName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f1a24aa7-9ca7-40f6-89ec-97def9ffe8db}'), pid=100)
def PKEY_Contact_FirstName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14977844-6b49-4aad-a714-a4513bf60460}'), pid=100)
def PKEY_Contact_FullName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{635e9051-50a5-4ba2-b9db-4ed056c77296}'), pid=100)
def PKEY_Contact_Gender():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3c8cee58-d4f0-4cf9-b756-4e5d24447bcd}'), pid=100)
def PKEY_Contact_GenderValue():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3c8cee58-d4f0-4cf9-b756-4e5d24447bcd}'), pid=101)
def PKEY_Contact_Hobbies():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5dc2253f-5e11-4adf-9cfe-910dd01e3e70}'), pid=100)
def PKEY_Contact_HomeAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{98f98354-617a-46b8-8560-5b1b64bf1f89}'), pid=100)
def PKEY_Contact_HomeAddress1Country():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=104)
def PKEY_Contact_HomeAddress1Locality():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=102)
def PKEY_Contact_HomeAddress1PostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=105)
def PKEY_Contact_HomeAddress1Region():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=103)
def PKEY_Contact_HomeAddress1Street():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=101)
def PKEY_Contact_HomeAddress2Country():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=109)
def PKEY_Contact_HomeAddress2Locality():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=107)
def PKEY_Contact_HomeAddress2PostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=110)
def PKEY_Contact_HomeAddress2Region():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=108)
def PKEY_Contact_HomeAddress2Street():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=106)
def PKEY_Contact_HomeAddress3Country():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=114)
def PKEY_Contact_HomeAddress3Locality():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=112)
def PKEY_Contact_HomeAddress3PostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=115)
def PKEY_Contact_HomeAddress3Region():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=113)
def PKEY_Contact_HomeAddress3Street():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=111)
def PKEY_Contact_HomeAddressCity():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=65)
def PKEY_Contact_HomeAddressCountry():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{08a65aa1-f4c9-43dd-9ddf-a33d8e7ead85}'), pid=100)
def PKEY_Contact_HomeAddressPostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8afcc170-8a46-4b53-9eee-90bae7151e62}'), pid=100)
def PKEY_Contact_HomeAddressPostOfficeBox():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7b9f6399-0a3f-4b12-89bd-4adc51c918af}'), pid=100)
def PKEY_Contact_HomeAddressState():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c89a23d0-7d6d-4eb8-87d4-776a82d493e5}'), pid=100)
def PKEY_Contact_HomeAddressStreet():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0adef160-db3f-4308-9a21-06237b16fa2a}'), pid=100)
def PKEY_Contact_HomeEmailAddresses():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56c90e9d-9d46-4963-886f-2e1cd9a694ef}'), pid=100)
def PKEY_Contact_HomeFaxNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{660e04d6-81ab-4977-a09f-82313113ab26}'), pid=100)
def PKEY_Contact_HomeTelephone():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=20)
def PKEY_Contact_IMAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d68dbd8a-3374-4b81-9972-3ec30682db3d}'), pid=100)
def PKEY_Contact_Initials():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f3d8f40d-50cb-44a2-9718-40cb9119495d}'), pid=100)
def PKEY_Contact_JA_CompanyNamePhonetic():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{897b3694-fe9e-43e6-8066-260f590c0100}'), pid=2)
def PKEY_Contact_JA_FirstNamePhonetic():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{897b3694-fe9e-43e6-8066-260f590c0100}'), pid=3)
def PKEY_Contact_JA_LastNamePhonetic():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{897b3694-fe9e-43e6-8066-260f590c0100}'), pid=4)
def PKEY_Contact_JobInfo1CompanyAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=120)
def PKEY_Contact_JobInfo1CompanyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=102)
def PKEY_Contact_JobInfo1Department():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=106)
def PKEY_Contact_JobInfo1Manager():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=105)
def PKEY_Contact_JobInfo1OfficeLocation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=104)
def PKEY_Contact_JobInfo1Title():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=103)
def PKEY_Contact_JobInfo1YomiCompanyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=101)
def PKEY_Contact_JobInfo2CompanyAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=121)
def PKEY_Contact_JobInfo2CompanyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=108)
def PKEY_Contact_JobInfo2Department():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=113)
def PKEY_Contact_JobInfo2Manager():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=112)
def PKEY_Contact_JobInfo2OfficeLocation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=110)
def PKEY_Contact_JobInfo2Title():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=109)
def PKEY_Contact_JobInfo2YomiCompanyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=107)
def PKEY_Contact_JobInfo3CompanyAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=123)
def PKEY_Contact_JobInfo3CompanyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=115)
def PKEY_Contact_JobInfo3Department():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=119)
def PKEY_Contact_JobInfo3Manager():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=118)
def PKEY_Contact_JobInfo3OfficeLocation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=117)
def PKEY_Contact_JobInfo3Title():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=116)
def PKEY_Contact_JobInfo3YomiCompanyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=114)
def PKEY_Contact_JobTitle():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=6)
def PKEY_Contact_Label():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{97b0ad89-df49-49cc-834e-660974fd755b}'), pid=100)
def PKEY_Contact_LastName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8f367200-c270-457c-b1d4-e07c5bcd90c7}'), pid=100)
def PKEY_Contact_MailingAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c0ac206a-827e-4650-95ae-77e2bb74fcc9}'), pid=100)
def PKEY_Contact_MiddleName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=71)
def PKEY_Contact_MobileTelephone():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=35)
def PKEY_Contact_NickName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=74)
def PKEY_Contact_OfficeLocation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=7)
def PKEY_Contact_OtherAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{508161fa-313b-43d5-83a1-c1accf68622c}'), pid=100)
def PKEY_Contact_OtherAddress1Country():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=134)
def PKEY_Contact_OtherAddress1Locality():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=132)
def PKEY_Contact_OtherAddress1PostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=135)
def PKEY_Contact_OtherAddress1Region():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=133)
def PKEY_Contact_OtherAddress1Street():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=131)
def PKEY_Contact_OtherAddress2Country():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=139)
def PKEY_Contact_OtherAddress2Locality():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=137)
def PKEY_Contact_OtherAddress2PostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=140)
def PKEY_Contact_OtherAddress2Region():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=138)
def PKEY_Contact_OtherAddress2Street():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=136)
def PKEY_Contact_OtherAddress3Country():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=144)
def PKEY_Contact_OtherAddress3Locality():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=142)
def PKEY_Contact_OtherAddress3PostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=145)
def PKEY_Contact_OtherAddress3Region():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=143)
def PKEY_Contact_OtherAddress3Street():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7b6f596-d678-4bc1-b05f-0203d27e8aa1}'), pid=141)
def PKEY_Contact_OtherAddressCity():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6e682923-7f7b-4f0c-a337-cfca296687bf}'), pid=100)
def PKEY_Contact_OtherAddressCountry():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8f167568-0aae-4322-8ed9-6055b7b0e398}'), pid=100)
def PKEY_Contact_OtherAddressPostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{95c656c1-2abf-4148-9ed3-9ec602e3b7cd}'), pid=100)
def PKEY_Contact_OtherAddressPostOfficeBox():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8b26ea41-058f-43f6-aecc-4035681ce977}'), pid=100)
def PKEY_Contact_OtherAddressState():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{71b377d6-e570-425f-a170-809fae73e54e}'), pid=100)
def PKEY_Contact_OtherAddressStreet():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ff962609-b7d6-4999-862d-95180d529aea}'), pid=100)
def PKEY_Contact_OtherEmailAddresses():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{11d6336b-38c4-4ec9-84d6-eb38d0b150af}'), pid=100)
def PKEY_Contact_PagerTelephone():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d6304e01-f8f5-4f45-8b15-d024a6296789}'), pid=100)
def PKEY_Contact_PersonalTitle():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=69)
def PKEY_Contact_PhoneNumbersCanonical():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d042d2a1-927e-40b5-a503-6edbd42a517e}'), pid=100)
def PKEY_Contact_Prefix():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=75)
def PKEY_Contact_PrimaryAddressCity():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c8ea94f0-a9e3-4969-a94b-9c62a95324e0}'), pid=100)
def PKEY_Contact_PrimaryAddressCountry():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e53d799d-0f3f-466e-b2ff-74634a3cb7a4}'), pid=100)
def PKEY_Contact_PrimaryAddressPostalCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{18bbd425-ecfd-46ef-b612-7b4a6034eda0}'), pid=100)
def PKEY_Contact_PrimaryAddressPostOfficeBox():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{de5ef3c7-46e1-484e-9999-62c5308394c1}'), pid=100)
def PKEY_Contact_PrimaryAddressState():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f1176dfe-7138-4640-8b4c-ae375dc70a6d}'), pid=100)
def PKEY_Contact_PrimaryAddressStreet():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{63c25b20-96be-488f-8788-c09c407ad812}'), pid=100)
def PKEY_Contact_PrimaryEmailAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=48)
def PKEY_Contact_PrimaryTelephone():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=25)
def PKEY_Contact_Profession():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7268af55-1ce4-4f6e-a41f-b6e4ef10e4a9}'), pid=100)
def PKEY_Contact_SpouseName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9d2408b6-3167-422b-82b0-f583b7a7cfe3}'), pid=100)
def PKEY_Contact_Suffix():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{176dc63c-2688-4e89-8143-a347800f25e9}'), pid=73)
def PKEY_Contact_TelexNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c554493c-c1f7-40c1-a76c-ef8c0614003e}'), pid=100)
def PKEY_Contact_TTYTDDTelephone():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{aaf16bac-2b55-45e6-9f6d-415eb94910df}'), pid=100)
def PKEY_Contact_WebPage():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=18)
def PKEY_Contact_Webpage2():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=124)
def PKEY_Contact_Webpage3():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03}'), pid=125)
def PKEY_AcquisitionID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{65a98875-3c80-40ab-abbc-efdaf77dbee2}'), pid=100)
def PKEY_ApplicationDefinedProperties():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cdbfc167-337e-41d8-af7c-8c09205429c7}'), pid=100)
def PKEY_ApplicationName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=18)
def PKEY_AppZoneIdentifier():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{502cfeab-47eb-459c-b960-e6d8728f7701}'), pid=102)
def PKEY_Author():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=4)
def PKEY_CachedFileUpdaterContentIdForConflictResolution():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=114)
def PKEY_CachedFileUpdaterContentIdForStream():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=113)
def PKEY_Capacity():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9b174b35-40ff-11d2-a27e-00c04fc30871}'), pid=3)
def PKEY_Category():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=2)
def PKEY_Comment():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=6)
def PKEY_Company():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=15)
def PKEY_ComputerName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=5)
def PKEY_ContainedItems():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=29)
def PKEY_ContentId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=132)
def PKEY_ContentStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=27)
def PKEY_ContentType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=26)
def PKEY_ContentUri():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=131)
def PKEY_Copyright():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=11)
def PKEY_CreatorAppId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c2ea046e-033c-4e91-bd5b-d4942f6bbe49}'), pid=2)
def PKEY_CreatorOpenWithUIOptions():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c2ea046e-033c-4e91-bd5b-d4942f6bbe49}'), pid=3)
CREATOROPENWITHUIOPTION_HIDDEN: UInt32 = 0
CREATOROPENWITHUIOPTION_VISIBLE: UInt32 = 1
def PKEY_DataObjectFormat():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1e81a3f8-a30f-4247-b9ee-1d0368a9425c}'), pid=2)
def PKEY_DateAccessed():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=16)
def PKEY_DateAcquired():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2cbaa8f5-d81f-47ca-b17a-f8d822300131}'), pid=100)
def PKEY_DateArchived():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{43f8d7b7-a444-4f87-9383-52271c9b915c}'), pid=100)
def PKEY_DateCompleted():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{72fab781-acda-43e5-b155-b2434f85e678}'), pid=100)
def PKEY_DateCreated():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=15)
def PKEY_DateImported():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=18258)
def PKEY_DateModified():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=14)
def PKEY_DefaultSaveLocationDisplay():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5d76b67f-9b3d-44bb-b6ae-25da4f638a67}'), pid=10)
ISDEFAULTSAVE_NONE: UInt32 = 0
ISDEFAULTSAVE_OWNER: UInt32 = 1
ISDEFAULTSAVE_NONOWNER: UInt32 = 2
ISDEFAULTSAVE_BOTH: UInt32 = 3
def PKEY_DueDate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8472b5-e0af-4db2-8071-c53fe76ae7ce}'), pid=100)
def PKEY_EndDate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c75faa05-96fd-49e7-9cb4-9f601082d553}'), pid=100)
def PKEY_ExpandoProperties():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6fa20de6-d11c-4d9d-a154-64317628c12d}'), pid=100)
def PKEY_FileAllocationSize():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=18)
def PKEY_FileAttributes():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=13)
def PKEY_FileCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=12)
def PKEY_FileDescription():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0cef7d53-fa64-11d1-a203-0000f81fedee}'), pid=3)
def PKEY_FileExtension():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e4f10a3c-49e6-405d-8288-a23bd4eeaa6c}'), pid=100)
def PKEY_FileFRN():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=21)
def PKEY_FileName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{41cf5ae0-f75a-4806-bd87-59c7d9248eb9}'), pid=100)
def PKEY_FileOfflineAvailabilityStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=100)
FILEOFFLINEAVAILABILITYSTATUS_NOTAVAILABLEOFFLINE: UInt32 = 0
FILEOFFLINEAVAILABILITYSTATUS_PARTIAL: UInt32 = 1
FILEOFFLINEAVAILABILITYSTATUS_COMPLETE: UInt32 = 2
FILEOFFLINEAVAILABILITYSTATUS_COMPLETE_PINNED: UInt32 = 3
FILEOFFLINEAVAILABILITYSTATUS_EXCLUDED: UInt32 = 4
FILEOFFLINEAVAILABILITYSTATUS_FOLDER_EMPTY: UInt32 = 5
def PKEY_FileOwner():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9b174b34-40ff-11d2-a27e-00c04fc30871}'), pid=4)
def PKEY_FilePlaceholderStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b2f9b9d6-fec4-4dd5-94d7-8957488c807b}'), pid=2)
def PKEY_FileVersion():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0cef7d53-fa64-11d1-a203-0000f81fedee}'), pid=4)
def PKEY_FindData():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=0)
def PKEY_FlagColor():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{67df94de-0ca7-4d6f-b792-053a3e4f03cf}'), pid=100)
def PKEY_FlagColorText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{45eae747-8e2a-40ae-8cbf-ca52aba6152a}'), pid=100)
def PKEY_FlagStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=12)
FLAGSTATUS_NOTFLAGGED: Int32 = 0
FLAGSTATUS_COMPLETED: Int32 = 1
FLAGSTATUS_FOLLOWUP: Int32 = 2
def PKEY_FlagStatusText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{dc54fd2e-189d-4871-aa01-08c2f57a4abc}'), pid=100)
def PKEY_FolderKind():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=101)
def PKEY_FolderNameDisplay():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=25)
def PKEY_FreeSpace():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9b174b35-40ff-11d2-a27e-00c04fc30871}'), pid=2)
def PKEY_FullText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1e3ee840-bc2b-476c-8237-2acd1a839b22}'), pid=6)
def PKEY_HighKeywords():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=24)
def PKEY_Identity():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a26f4afc-7346-4299-be47-eb1ae613139f}'), pid=100)
def PKEY_Identity_Blob():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8c3b93a4-baed-1a83-9a32-102ee313f6eb}'), pid=100)
def PKEY_Identity_DisplayName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7d683fc9-d155-45a8-bb1f-89d19bcb792f}'), pid=100)
def PKEY_Identity_InternetSid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d6d5d49-265d-4688-9f4e-1fdd33e7cc83}'), pid=100)
def PKEY_Identity_IsMeIdentity():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a4108708-09df-4377-9dfc-6d99986d5a67}'), pid=100)
def PKEY_Identity_KeyProviderContext():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a26f4afc-7346-4299-be47-eb1ae613139f}'), pid=17)
def PKEY_Identity_KeyProviderName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a26f4afc-7346-4299-be47-eb1ae613139f}'), pid=16)
def PKEY_Identity_LogonStatusString():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f18dedf3-337f-42c0-9e03-cee08708a8c3}'), pid=100)
def PKEY_Identity_PrimaryEmailAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fcc16823-baed-4f24-9b32-a0982117f7fa}'), pid=100)
def PKEY_Identity_PrimarySid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2b1b801e-c0c1-4987-9ec5-72fa89814787}'), pid=100)
def PKEY_Identity_ProviderData():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8a74b92-361b-4e9a-b722-7c4a7330a312}'), pid=100)
def PKEY_Identity_ProviderID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{74a7de49-fa11-4d3d-a006-db7e08675916}'), pid=100)
def PKEY_Identity_QualifiedUserName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{da520e51-f4e9-4739-ac82-02e0a95c9030}'), pid=100)
def PKEY_Identity_UniqueID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e55fc3b0-2b60-4220-918e-b21e8bf16016}'), pid=100)
def PKEY_Identity_UserName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c4322503-78ca-49c6-9acc-a68e2afd7b6b}'), pid=100)
def PKEY_IdentityProvider_Name():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b96eff7b-35ca-4a35-8607-29e3a54c46ea}'), pid=100)
def PKEY_IdentityProvider_Picture():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2425166f-5642-4864-992f-98fd98f294c3}'), pid=100)
def PKEY_ImageParsingName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d7750ee0-c6a4-48ec-b53e-b87b52e6d073}'), pid=100)
def PKEY_Importance():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=11)
IMPORTANCE_LOW_MIN: Int32 = 0
IMPORTANCE_LOW_SET: Int32 = 1
IMPORTANCE_LOW_MAX: Int32 = 1
IMPORTANCE_NORMAL_MIN: Int32 = 2
IMPORTANCE_NORMAL_SET: Int32 = 3
IMPORTANCE_NORMAL_MAX: Int32 = 4
IMPORTANCE_HIGH_MIN: Int32 = 5
IMPORTANCE_HIGH_SET: Int32 = 5
IMPORTANCE_HIGH_MAX: Int32 = 5
def PKEY_ImportanceText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a3b29791-7713-4e1d-bb40-17db85f01831}'), pid=100)
def PKEY_IsAttachment():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f23f425c-71a1-4fa8-922f-678ea4a60408}'), pid=100)
def PKEY_IsDefaultNonOwnerSaveLocation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5d76b67f-9b3d-44bb-b6ae-25da4f638a67}'), pid=5)
def PKEY_IsDefaultSaveLocation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5d76b67f-9b3d-44bb-b6ae-25da4f638a67}'), pid=3)
def PKEY_IsDeleted():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5cda5fc8-33ee-4ff3-9094-ae7bd8868c4d}'), pid=100)
def PKEY_IsEncrypted():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{90e5e14e-648b-4826-b2aa-acaf790e3513}'), pid=10)
def PKEY_IsFlagged():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5da84765-e3ff-4278-86b0-a27967fbdd03}'), pid=100)
def PKEY_IsFlaggedComplete():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a6f360d2-55f9-48de-b909-620e090a647c}'), pid=100)
def PKEY_IsIncomplete():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{346c8bd1-2e6a-4c45-89a4-61b78e8e700f}'), pid=100)
def PKEY_IsLocationSupported():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5d76b67f-9b3d-44bb-b6ae-25da4f638a67}'), pid=8)
def PKEY_IsPinnedToNameSpaceTree():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5d76b67f-9b3d-44bb-b6ae-25da4f638a67}'), pid=2)
def PKEY_IsRead():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=10)
def PKEY_IsSearchOnlyItem():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5d76b67f-9b3d-44bb-b6ae-25da4f638a67}'), pid=4)
def PKEY_IsSendToTarget():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=33)
def PKEY_IsShared():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ef884c5b-2bfe-41bb-aae5-76eedf4f9902}'), pid=100)
def PKEY_ItemAuthors():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d0a04f0a-462a-48a4-bb2f-3706e88dbd7d}'), pid=100)
def PKEY_ItemClassType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{048658ad-2db8-41a4-bbb6-ac1ef1207eb1}'), pid=100)
def PKEY_ItemDate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f7db74b4-4287-4103-afba-f1b13dcd75cf}'), pid=100)
def PKEY_ItemFolderNameDisplay():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=2)
def PKEY_ItemFolderPathDisplay():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=6)
def PKEY_ItemFolderPathDisplayNarrow():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{dabd30ed-0043-4789-a7f8-d013a4736622}'), pid=100)
def PKEY_ItemName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6b8da074-3b5c-43bc-886f-0a2cdce00b6f}'), pid=100)
def PKEY_ItemNameDisplay():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=10)
def PKEY_ItemNameDisplayWithoutExtension():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=24)
def PKEY_ItemNamePrefix():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d7313ff1-a77a-401c-8c99-3dbdd68add36}'), pid=100)
def PKEY_ItemNameSortOverride():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=23)
def PKEY_ItemParticipants():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d4d0aa16-9948-41a4-aa85-d97ff9646993}'), pid=100)
def PKEY_ItemPathDisplay():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=7)
def PKEY_ItemPathDisplayNarrow():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=8)
def PKEY_ItemSubType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=37)
def PKEY_ItemType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=11)
def PKEY_ItemTypeText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=4)
def PKEY_ItemUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49691c90-7e17-101a-a91c-08002b2ecda9}'), pid=9)
def PKEY_Keywords():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=5)
def PKEY_Kind():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1e3ee840-bc2b-476c-8237-2acd1a839b22}'), pid=3)
KIND_CALENDAR: String = 'calendar'
KIND_COMMUNICATION: String = 'communication'
KIND_CONTACT: String = 'contact'
KIND_DOCUMENT: String = 'document'
KIND_EMAIL: String = 'email'
KIND_FEED: String = 'feed'
KIND_FOLDER: String = 'folder'
KIND_GAME: String = 'game'
KIND_INSTANTMESSAGE: String = 'instantmessage'
KIND_JOURNAL: String = 'journal'
KIND_LINK: String = 'link'
KIND_MOVIE: String = 'movie'
KIND_MUSIC: String = 'music'
KIND_NOTE: String = 'note'
KIND_PICTURE: String = 'picture'
KIND_PLAYLIST: String = 'playlist'
KIND_PROGRAM: String = 'program'
KIND_RECORDEDTV: String = 'recordedtv'
KIND_SEARCHFOLDER: String = 'searchfolder'
KIND_TASK: String = 'task'
KIND_VIDEO: String = 'video'
KIND_WEBHISTORY: String = 'webhistory'
KIND_UNKNOWN: String = 'unknown'
def PKEY_KindText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f04bef95-c585-4197-a2b7-df46fdc9ee6d}'), pid=100)
def PKEY_Language():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=28)
def PKEY_LastSyncError():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=107)
def PKEY_LastSyncWarning():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=128)
def PKEY_LastWriterPackageFamilyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{502cfeab-47eb-459c-b960-e6d8728f7701}'), pid=101)
def PKEY_LowKeywords():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=25)
def PKEY_MediumKeywords():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=26)
def PKEY_MileageInformation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fdf84370-031a-4add-9e91-0d775f1c6605}'), pid=100)
def PKEY_MIMEType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0b63e350-9ccc-11d0-bcdb-00805fccce04}'), pid=5)
def PKEY_Null():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00000000-0000-0000-0000-000000000000}'), pid=0)
def PKEY_OfflineAvailability():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a94688b6-7d9f-4570-a648-e3dfc0ab2b3f}'), pid=100)
OFFLINEAVAILABILITY_NOT_AVAILABLE: UInt32 = 0
OFFLINEAVAILABILITY_AVAILABLE: UInt32 = 1
OFFLINEAVAILABILITY_ALWAYS_AVAILABLE: UInt32 = 2
def PKEY_OfflineStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d24888f-4718-4bda-afed-ea0fb4386cd8}'), pid=100)
OFFLINESTATUS_ONLINE: UInt32 = 0
OFFLINESTATUS_OFFLINE: UInt32 = 1
OFFLINESTATUS_OFFLINE_FORCED: UInt32 = 2
OFFLINESTATUS_OFFLINE_SLOW: UInt32 = 3
OFFLINESTATUS_OFFLINE_ERROR: UInt32 = 4
OFFLINESTATUS_OFFLINE_ITEM_VERSION_CONFLICT: UInt32 = 5
OFFLINESTATUS_OFFLINE_SUSPENDED: UInt32 = 6
def PKEY_OriginalFileName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0cef7d53-fa64-11d1-a203-0000f81fedee}'), pid=6)
def PKEY_OwnerSID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5d76b67f-9b3d-44bb-b6ae-25da4f638a67}'), pid=6)
def PKEY_ParentalRating():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=21)
def PKEY_ParentalRatingReason():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{10984e0a-f9f2-4321-b7ef-baf195af4319}'), pid=100)
def PKEY_ParentalRatingsOrganization():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a7fe0840-1344-46f0-8d37-52ed712a4bf9}'), pid=100)
def PKEY_ParsingBindContext():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{dfb9a04d-362f-4ca3-b30b-0254b17b5b84}'), pid=100)
def PKEY_ParsingName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=24)
def PKEY_ParsingPath():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=30)
def PKEY_PerceivedType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=9)
def PKEY_PercentFull():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9b174b35-40ff-11d2-a27e-00c04fc30871}'), pid=5)
def PKEY_Priority():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9c1fcf74-2d97-41ba-b4ae-cb2e3661a6e4}'), pid=5)
def PKEY_PriorityText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d98be98b-b86b-4095-bf52-9d23b2e0a752}'), pid=100)
def PKEY_Project():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{39a7f922-477c-48de-8bc8-b28441e342e3}'), pid=100)
def PKEY_ProviderItemID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f21d9941-81f0-471a-adee-4e74b49217ed}'), pid=100)
def PKEY_Rating():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=9)
RATING_ONE_STAR_MIN: UInt32 = 1
RATING_ONE_STAR_SET: UInt32 = 1
RATING_ONE_STAR_MAX: UInt32 = 12
RATING_TWO_STARS_MIN: UInt32 = 13
RATING_TWO_STARS_SET: UInt32 = 25
RATING_TWO_STARS_MAX: UInt32 = 37
RATING_THREE_STARS_MIN: UInt32 = 38
RATING_THREE_STARS_SET: UInt32 = 50
RATING_THREE_STARS_MAX: UInt32 = 62
RATING_FOUR_STARS_MIN: UInt32 = 63
RATING_FOUR_STARS_SET: UInt32 = 75
RATING_FOUR_STARS_MAX: UInt32 = 87
RATING_FIVE_STARS_MIN: UInt32 = 88
RATING_FIVE_STARS_SET: UInt32 = 99
RATING_FIVE_STARS_MAX: UInt32 = 99
def PKEY_RatingText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{90197ca7-fd8f-4e8c-9da3-b57e1e609295}'), pid=100)
def PKEY_RemoteConflictingFile():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=115)
def PKEY_Security_AllowedEnterpriseDataProtectionIdentities():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{38d43380-d418-4830-84d5-46935a81c5c6}'), pid=32)
def PKEY_Security_EncryptionOwners():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5f5aff6a-37e5-4780-97ea-80c7565cf535}'), pid=34)
def PKEY_Security_EncryptionOwnersDisplay():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{de621b8f-e125-43a3-a32d-5665446d632a}'), pid=25)
def PKEY_Sensitivity():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f8d3f6ac-4874-42cb-be59-ab454b30716a}'), pid=100)
def PKEY_SensitivityText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d0c7f054-3f72-4725-8527-129a577cb269}'), pid=100)
def PKEY_SFGAOFlags():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=25)
def PKEY_SharedWith():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ef884c5b-2bfe-41bb-aae5-76eedf4f9902}'), pid=200)
def PKEY_ShareUserRating():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=12)
def PKEY_SharingStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ef884c5b-2bfe-41bb-aae5-76eedf4f9902}'), pid=300)
SHARINGSTATUS_NOTSHARED: UInt32 = 0
SHARINGSTATUS_SHARED: UInt32 = 1
SHARINGSTATUS_PRIVATE: UInt32 = 2
def PKEY_Shell_OmitFromView():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{de35258c-c695-4cbc-b982-38b0ad24ced0}'), pid=2)
def PKEY_SimpleRating():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a09f084e-ad41-489f-8076-aa5be3082bca}'), pid=100)
def PKEY_Size():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=12)
def PKEY_SoftwareUsed():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=305)
def PKEY_SourceItem():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{668cdfa5-7a1b-4323-ae4b-e527393a1d81}'), pid=100)
def PKEY_SourcePackageFamilyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ffae9db7-1c8d-43ff-818c-84403aa3732d}'), pid=100)
def PKEY_StartDate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{48fd6ec8-8a12-4cdf-a03e-4ec5a511edde}'), pid=100)
def PKEY_Status():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{000214a1-0000-0000-c000-000000000046}'), pid=9)
def PKEY_StorageProviderCallerVersionInformation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b2f9b9d6-fec4-4dd5-94d7-8957488c807b}'), pid=7)
def PKEY_StorageProviderError():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=109)
def PKEY_StorageProviderFileChecksum():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b2f9b9d6-fec4-4dd5-94d7-8957488c807b}'), pid=5)
def PKEY_StorageProviderFileFlags():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b2f9b9d6-fec4-4dd5-94d7-8957488c807b}'), pid=8)
def PKEY_StorageProviderFileHasConflict():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b2f9b9d6-fec4-4dd5-94d7-8957488c807b}'), pid=9)
def PKEY_StorageProviderFileIdentifier():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b2f9b9d6-fec4-4dd5-94d7-8957488c807b}'), pid=3)
def PKEY_StorageProviderFileRemoteUri():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=112)
def PKEY_StorageProviderFileVersion():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b2f9b9d6-fec4-4dd5-94d7-8957488c807b}'), pid=4)
def PKEY_StorageProviderFileVersionWaterline():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b2f9b9d6-fec4-4dd5-94d7-8957488c807b}'), pid=6)
def PKEY_StorageProviderId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=108)
def PKEY_StorageProviderShareStatuses():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=111)
STORAGE_PROVIDER_SHARE_STATUS_PRIVATE: String = 'Private'
STORAGE_PROVIDER_SHARE_STATUS_SHARED: String = 'Shared'
STORAGE_PROVIDER_SHARE_STATUS_PUBLIC: String = 'Public'
STORAGE_PROVIDER_SHARE_STATUS_GROUP: String = 'Group'
STORAGE_PROVIDER_SHARE_STATUS_OWNER: String = 'Owner'
def PKEY_StorageProviderSharingStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=117)
STORAGE_PROVIDER_SHARINGSTATUS_NOTSHARED: UInt32 = 0
STORAGE_PROVIDER_SHARINGSTATUS_SHARED: UInt32 = 1
STORAGE_PROVIDER_SHARINGSTATUS_PRIVATE: UInt32 = 2
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC: UInt32 = 3
STORAGE_PROVIDER_SHARINGSTATUS_SHARED_OWNED: UInt32 = 4
STORAGE_PROVIDER_SHARINGSTATUS_SHARED_COOWNED: UInt32 = 5
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_OWNED: UInt32 = 6
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_COOWNED: UInt32 = 7
def PKEY_StorageProviderStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=110)
def PKEY_Subject():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=3)
def PKEY_SyncTransferStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=103)
def PKEY_Thumbnail():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=17)
def PKEY_ThumbnailCacheId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{446d16b1-8dad-4870-a748-402ea43d788c}'), pid=100)
def PKEY_ThumbnailStream():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=27)
def PKEY_Title():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=2)
def PKEY_TitleSortOverride():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f0f7984d-222e-4ad2-82ab-1dd8ea40e57e}'), pid=300)
def PKEY_TotalFileSize():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=14)
def PKEY_Trademarks():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0cef7d53-fa64-11d1-a203-0000f81fedee}'), pid=9)
def PKEY_TransferOrder():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=106)
def PKEY_TransferPosition():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=104)
def PKEY_TransferSize():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fceff153-e839-4cf3-a9e7-ea22832094b8}'), pid=105)
def PKEY_VolumeId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{446d16b1-8dad-4870-a748-402ea43d788c}'), pid=104)
def PKEY_ZoneIdentifier():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{502cfeab-47eb-459c-b960-e6d8728f7701}'), pid=100)
def PKEY_Device_PrinterURL():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0b48f35a-be6e-4f17-b108-3c4073d1669a}'), pid=15)
def PKEY_DeviceInterface_Bluetooth_DeviceAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=1)
def PKEY_DeviceInterface_Bluetooth_Flags():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=3)
def PKEY_DeviceInterface_Bluetooth_LastConnectedTime():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=11)
def PKEY_DeviceInterface_Bluetooth_Manufacturer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=4)
def PKEY_DeviceInterface_Bluetooth_ModelNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=5)
def PKEY_DeviceInterface_Bluetooth_ProductId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=8)
def PKEY_DeviceInterface_Bluetooth_ProductVersion():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=9)
def PKEY_DeviceInterface_Bluetooth_ServiceGuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=2)
def PKEY_DeviceInterface_Bluetooth_VendorId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=7)
def PKEY_DeviceInterface_Bluetooth_VendorIdSource():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=6)
def PKEY_DeviceInterface_Hid_IsReadOnly():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cbf38310-4a17-4310-a1eb-247f0b67593b}'), pid=4)
def PKEY_DeviceInterface_Hid_ProductId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cbf38310-4a17-4310-a1eb-247f0b67593b}'), pid=6)
def PKEY_DeviceInterface_Hid_UsageId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cbf38310-4a17-4310-a1eb-247f0b67593b}'), pid=3)
def PKEY_DeviceInterface_Hid_UsagePage():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cbf38310-4a17-4310-a1eb-247f0b67593b}'), pid=2)
def PKEY_DeviceInterface_Hid_VendorId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cbf38310-4a17-4310-a1eb-247f0b67593b}'), pid=5)
def PKEY_DeviceInterface_Hid_VersionNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cbf38310-4a17-4310-a1eb-247f0b67593b}'), pid=7)
def PKEY_DeviceInterface_PrinterDriverDirectory():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{847c66de-b8d6-4af9-abc3-6f4f926bc039}'), pid=14)
def PKEY_DeviceInterface_PrinterDriverName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{afc47170-14f5-498c-8f30-b0d19be449c6}'), pid=11)
def PKEY_DeviceInterface_PrinterEnumerationFlag():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a00742a1-cd8c-4b37-95ab-70755587767a}'), pid=3)
def PKEY_DeviceInterface_PrinterName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0a7b84ef-0c27-463f-84ef-06c5070001be}'), pid=10)
def PKEY_DeviceInterface_PrinterPortName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{eec7b761-6f94-41b1-949f-c729720dd13c}'), pid=12)
def PKEY_DeviceInterface_Proximity_SupportsNfc():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fb3842cd-9e2a-4f83-8fcc-4b0761139ae9}'), pid=2)
def PKEY_DeviceInterface_Serial_PortName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4c6bf15c-4c03-4aac-91f5-64c0f852bcf4}'), pid=4)
def PKEY_DeviceInterface_Serial_UsbProductId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4c6bf15c-4c03-4aac-91f5-64c0f852bcf4}'), pid=3)
def PKEY_DeviceInterface_Serial_UsbVendorId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4c6bf15c-4c03-4aac-91f5-64c0f852bcf4}'), pid=2)
def PKEY_DeviceInterface_WinUsb_DeviceInterfaceClasses():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{95e127b5-79cc-4e83-9c9e-8422187b3e0e}'), pid=7)
def PKEY_DeviceInterface_WinUsb_UsbClass():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{95e127b5-79cc-4e83-9c9e-8422187b3e0e}'), pid=4)
def PKEY_DeviceInterface_WinUsb_UsbProductId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{95e127b5-79cc-4e83-9c9e-8422187b3e0e}'), pid=3)
def PKEY_DeviceInterface_WinUsb_UsbProtocol():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{95e127b5-79cc-4e83-9c9e-8422187b3e0e}'), pid=6)
def PKEY_DeviceInterface_WinUsb_UsbSubClass():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{95e127b5-79cc-4e83-9c9e-8422187b3e0e}'), pid=5)
def PKEY_DeviceInterface_WinUsb_UsbVendorId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{95e127b5-79cc-4e83-9c9e-8422187b3e0e}'), pid=2)
def PKEY_Devices_Aep_AepId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3b2ce006-5e61-4fde-bab8-9b8aac9b26df}'), pid=8)
def PKEY_Devices_Aep_Bluetooth_Cod_Major():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5fbd34cd-561a-412e-ba98-478a6b0fef1d}'), pid=2)
def PKEY_Devices_Aep_Bluetooth_Cod_Minor():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5fbd34cd-561a-412e-ba98-478a6b0fef1d}'), pid=3)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Audio():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5fbd34cd-561a-412e-ba98-478a6b0fef1d}'), pid=10)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Capturing():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5fbd34cd-561a-412e-ba98-478a6b0fef1d}'), pid=8)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Information():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5fbd34cd-561a-412e-ba98-478a6b0fef1d}'), pid=12)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_LimitedDiscovery():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5fbd34cd-561a-412e-ba98-478a6b0fef1d}'), pid=4)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Networking():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5fbd34cd-561a-412e-ba98-478a6b0fef1d}'), pid=6)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_ObjectXfer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5fbd34cd-561a-412e-ba98-478a6b0fef1d}'), pid=9)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Positioning():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5fbd34cd-561a-412e-ba98-478a6b0fef1d}'), pid=5)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Rendering():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5fbd34cd-561a-412e-ba98-478a6b0fef1d}'), pid=7)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Telephony():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5fbd34cd-561a-412e-ba98-478a6b0fef1d}'), pid=11)
def PKEY_Devices_Aep_Bluetooth_LastSeenTime():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=12)
def PKEY_Devices_Aep_Bluetooth_Le_AddressType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{995ef0b0-7eb3-4a8b-b9ce-068bb3f4af69}'), pid=4)
BLUETOOTH_ADDRESS_TYPE_PUBLIC: UInt32 = 0
BLUETOOTH_ADDRESS_TYPE_RANDOM: UInt32 = 1
def PKEY_Devices_Aep_Bluetooth_Le_Appearance():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{995ef0b0-7eb3-4a8b-b9ce-068bb3f4af69}'), pid=1)
def PKEY_Devices_Aep_Bluetooth_Le_Appearance_Category():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{995ef0b0-7eb3-4a8b-b9ce-068bb3f4af69}'), pid=5)
def PKEY_Devices_Aep_Bluetooth_Le_Appearance_Subcategory():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{995ef0b0-7eb3-4a8b-b9ce-068bb3f4af69}'), pid=6)
def PKEY_Devices_Aep_Bluetooth_Le_IsConnectable():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{995ef0b0-7eb3-4a8b-b9ce-068bb3f4af69}'), pid=8)
def PKEY_Devices_Aep_CanPair():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e7c3fb29-caa7-4f47-8c8b-be59b330d4c5}'), pid=3)
def PKEY_Devices_Aep_Category():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a35996ab-11cf-4935-8b61-a6761081ecdf}'), pid=17)
def PKEY_Devices_Aep_ContainerId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e7c3fb29-caa7-4f47-8c8b-be59b330d4c5}'), pid=2)
def PKEY_Devices_Aep_DeviceAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a35996ab-11cf-4935-8b61-a6761081ecdf}'), pid=12)
def PKEY_Devices_Aep_IsConnected():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a35996ab-11cf-4935-8b61-a6761081ecdf}'), pid=7)
def PKEY_Devices_Aep_IsPaired():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a35996ab-11cf-4935-8b61-a6761081ecdf}'), pid=16)
def PKEY_Devices_Aep_IsPresent():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a35996ab-11cf-4935-8b61-a6761081ecdf}'), pid=9)
def PKEY_Devices_Aep_Manufacturer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a35996ab-11cf-4935-8b61-a6761081ecdf}'), pid=5)
def PKEY_Devices_Aep_ModelId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a35996ab-11cf-4935-8b61-a6761081ecdf}'), pid=4)
def PKEY_Devices_Aep_ModelName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a35996ab-11cf-4935-8b61-a6761081ecdf}'), pid=3)
def PKEY_Devices_Aep_PointOfService_ConnectionTypes():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d4bf61b3-442e-4ada-882d-fa7b70c832d9}'), pid=6)
def PKEY_Devices_Aep_ProtocolId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3b2ce006-5e61-4fde-bab8-9b8aac9b26df}'), pid=5)
def PKEY_Devices_Aep_SignalStrength():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a35996ab-11cf-4935-8b61-a6761081ecdf}'), pid=6)
def PKEY_Devices_AepContainer_CanPair():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0bba1ede-7566-4f47-90ec-25fc567ced2a}'), pid=3)
def PKEY_Devices_AepContainer_Categories():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0bba1ede-7566-4f47-90ec-25fc567ced2a}'), pid=9)
def PKEY_Devices_AepContainer_Children():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0bba1ede-7566-4f47-90ec-25fc567ced2a}'), pid=2)
def PKEY_Devices_AepContainer_ContainerId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0bba1ede-7566-4f47-90ec-25fc567ced2a}'), pid=12)
def PKEY_Devices_AepContainer_DialProtocol_InstalledApplications():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=6)
def PKEY_Devices_AepContainer_IsPaired():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0bba1ede-7566-4f47-90ec-25fc567ced2a}'), pid=4)
def PKEY_Devices_AepContainer_IsPresent():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0bba1ede-7566-4f47-90ec-25fc567ced2a}'), pid=11)
def PKEY_Devices_AepContainer_Manufacturer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0bba1ede-7566-4f47-90ec-25fc567ced2a}'), pid=6)
def PKEY_Devices_AepContainer_ModelIds():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0bba1ede-7566-4f47-90ec-25fc567ced2a}'), pid=8)
def PKEY_Devices_AepContainer_ModelName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0bba1ede-7566-4f47-90ec-25fc567ced2a}'), pid=7)
def PKEY_Devices_AepContainer_ProtocolIds():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0bba1ede-7566-4f47-90ec-25fc567ced2a}'), pid=13)
def PKEY_Devices_AepContainer_SupportedUriSchemes():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=5)
def PKEY_Devices_AepContainer_SupportsAudio():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=2)
def PKEY_Devices_AepContainer_SupportsCapturing():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=11)
def PKEY_Devices_AepContainer_SupportsImages():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=4)
def PKEY_Devices_AepContainer_SupportsInformation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=14)
def PKEY_Devices_AepContainer_SupportsLimitedDiscovery():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=7)
def PKEY_Devices_AepContainer_SupportsNetworking():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=9)
def PKEY_Devices_AepContainer_SupportsObjectTransfer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=12)
def PKEY_Devices_AepContainer_SupportsPositioning():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=8)
def PKEY_Devices_AepContainer_SupportsRendering():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=10)
def PKEY_Devices_AepContainer_SupportsTelephony():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=13)
def PKEY_Devices_AepContainer_SupportsVideo():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6af55d45-38db-4495-acb0-d4728a3b8314}'), pid=3)
def PKEY_Devices_AepService_AepId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9c141a9-1b4c-4f17-a9d1-f298538cadb8}'), pid=6)
def PKEY_Devices_AepService_Bluetooth_CacheMode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9744311e-7951-4b2e-b6f0-ecb293cac119}'), pid=5)
BLUETOOTH_CACHE_MODE_CACHED: UInt32 = 0
BLUETOOTH_CACHED_MODE_UNCACHED: UInt32 = 1
def PKEY_Devices_AepService_Bluetooth_ServiceGuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a399aac7-c265-474e-b073-ffce57721716}'), pid=2)
def PKEY_Devices_AepService_Bluetooth_TargetDevice():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9744311e-7951-4b2e-b6f0-ecb293cac119}'), pid=6)
def PKEY_Devices_AepService_ContainerId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{71724756-3e74-4432-9b59-e7b2f668a593}'), pid=4)
def PKEY_Devices_AepService_FriendlyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{71724756-3e74-4432-9b59-e7b2f668a593}'), pid=2)
def PKEY_Devices_AepService_IoT_ServiceInterfaces():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{79d94e82-4d79-45aa-821a-74858b4e4ca6}'), pid=2)
def PKEY_Devices_AepService_ParentAepIsPaired():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9c141a9-1b4c-4f17-a9d1-f298538cadb8}'), pid=7)
def PKEY_Devices_AepService_ProtocolId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9c141a9-1b4c-4f17-a9d1-f298538cadb8}'), pid=5)
def PKEY_Devices_AepService_ServiceClassId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{71724756-3e74-4432-9b59-e7b2f668a593}'), pid=3)
def PKEY_Devices_AepService_ServiceId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9c141a9-1b4c-4f17-a9d1-f298538cadb8}'), pid=2)
def PKEY_Devices_AppPackageFamilyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{51236583-0c4a-4fe8-b81f-166aec13f510}'), pid=100)
def PKEY_Devices_AudioDevice_Microphone_IsFarField():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8943b373-388c-4395-b557-bc6dbaffafdb}'), pid=6)
def PKEY_Devices_AudioDevice_Microphone_SensitivityInDbfs():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8943b373-388c-4395-b557-bc6dbaffafdb}'), pid=3)
def PKEY_Devices_AudioDevice_Microphone_SensitivityInDbfs2():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8943b373-388c-4395-b557-bc6dbaffafdb}'), pid=5)
def PKEY_Devices_AudioDevice_Microphone_SignalToNoiseRatioInDb():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8943b373-388c-4395-b557-bc6dbaffafdb}'), pid=4)
def PKEY_Devices_AudioDevice_RawProcessingSupported():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8943b373-388c-4395-b557-bc6dbaffafdb}'), pid=2)
def PKEY_Devices_AudioDevice_SpeechProcessingSupported():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fb1de864-e06d-47f4-82a6-8a0aef44493c}'), pid=2)
def PKEY_Devices_BatteryLife():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=10)
def PKEY_Devices_BatteryPlusCharging():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=22)
def PKEY_Devices_BatteryPlusChargingText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=23)
def PKEY_Devices_Category():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=91)
def PKEY_Devices_CategoryGroup():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=94)
def PKEY_Devices_CategoryIds():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=90)
def PKEY_Devices_CategoryPlural():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=92)
def PKEY_Devices_ChallengeAep():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0774315e-b714-48ec-8de8-8125c077ac11}'), pid=2)
def PKEY_Devices_ChargingState():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=11)
def PKEY_Devices_Children():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=9)
def PKEY_Devices_ClassGuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=10)
def PKEY_Devices_CompatibleIds():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=4)
def PKEY_Devices_Connected():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=55)
def PKEY_Devices_ContainerId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c}'), pid=2)
def PKEY_Devices_DefaultTooltip():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{880f70a2-6082-47ac-8aab-a739d1a300c3}'), pid=153)
def PKEY_Devices_DeviceCapabilities():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=17)
def PKEY_Devices_DeviceCharacteristics():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=29)
def PKEY_Devices_DeviceDescription1():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=81)
def PKEY_Devices_DeviceDescription2():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=82)
def PKEY_Devices_DeviceHasProblem():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=6)
def PKEY_Devices_DeviceInstanceId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=256)
def PKEY_Devices_DeviceManufacturer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=13)
def PKEY_Devices_DevObjectType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{13673f42-a3d6-49f6-b4da-ae46e0c5237c}'), pid=2)
def PKEY_Devices_DialProtocol_InstalledApplications():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6845cc72-1b71-48c3-af86-b09171a19b14}'), pid=3)
def PKEY_Devices_DiscoveryMethod():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=52)
def PKEY_Devices_Dnssd_Domain():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf79c0ab-bb74-4cee-b070-470b5ae202ea}'), pid=3)
def PKEY_Devices_Dnssd_FullName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf79c0ab-bb74-4cee-b070-470b5ae202ea}'), pid=5)
def PKEY_Devices_Dnssd_HostName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf79c0ab-bb74-4cee-b070-470b5ae202ea}'), pid=7)
def PKEY_Devices_Dnssd_InstanceName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf79c0ab-bb74-4cee-b070-470b5ae202ea}'), pid=4)
def PKEY_Devices_Dnssd_NetworkAdapterId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf79c0ab-bb74-4cee-b070-470b5ae202ea}'), pid=11)
def PKEY_Devices_Dnssd_PortNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf79c0ab-bb74-4cee-b070-470b5ae202ea}'), pid=12)
def PKEY_Devices_Dnssd_Priority():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf79c0ab-bb74-4cee-b070-470b5ae202ea}'), pid=9)
def PKEY_Devices_Dnssd_ServiceName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf79c0ab-bb74-4cee-b070-470b5ae202ea}'), pid=2)
def PKEY_Devices_Dnssd_TextAttributes():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf79c0ab-bb74-4cee-b070-470b5ae202ea}'), pid=6)
def PKEY_Devices_Dnssd_Ttl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf79c0ab-bb74-4cee-b070-470b5ae202ea}'), pid=10)
def PKEY_Devices_Dnssd_Weight():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bf79c0ab-bb74-4cee-b070-470b5ae202ea}'), pid=8)
def PKEY_Devices_FriendlyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12288)
def PKEY_Devices_FunctionPaths():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d08dd4c0-3a9e-462e-8290-7b636b2576b9}'), pid=3)
def PKEY_Devices_GlyphIcon():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{51236583-0c4a-4fe8-b81f-166aec13f510}'), pid=123)
def PKEY_Devices_HardwareIds():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=3)
def PKEY_Devices_Icon():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=57)
def PKEY_Devices_InLocalMachineContainer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c}'), pid=4)
def PKEY_Devices_InterfaceClassGuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=4)
def PKEY_Devices_InterfaceEnabled():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=3)
def PKEY_Devices_InterfacePaths():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d08dd4c0-3a9e-462e-8290-7b636b2576b9}'), pid=2)
def PKEY_Devices_IpAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12297)
def PKEY_Devices_IsDefault():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=86)
def PKEY_Devices_IsNetworkConnected():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=85)
def PKEY_Devices_IsShared():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=84)
def PKEY_Devices_IsSoftwareInstalling():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=9)
def PKEY_Devices_LaunchDeviceStageFromExplorer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=77)
def PKEY_Devices_LocalMachine():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=70)
def PKEY_Devices_LocationPaths():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=37)
def PKEY_Devices_Manufacturer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8192)
def PKEY_Devices_MetadataPath():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=71)
def PKEY_Devices_MicrophoneArray_Geometry():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a1829ea2-27eb-459e-935d-b2fad7b07762}'), pid=2)
def PKEY_Devices_MissedCalls():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=5)
def PKEY_Devices_ModelId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=2)
def PKEY_Devices_ModelName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8194)
def PKEY_Devices_ModelNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8195)
def PKEY_Devices_NetworkedTooltip():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{880f70a2-6082-47ac-8aab-a739d1a300c3}'), pid=152)
def PKEY_Devices_NetworkName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=7)
def PKEY_Devices_NetworkType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=8)
def PKEY_Devices_NewPictures():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=4)
def PKEY_Devices_Notification():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{06704b0c-e830-4c81-9178-91e4e95a80a0}'), pid=3)
def PKEY_Devices_Notifications_LowBattery():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c4c07f2b-8524-4e66-ae3a-a6235f103beb}'), pid=2)
def PKEY_Devices_Notifications_MissedCall():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6614ef48-4efe-4424-9eda-c79f404edf3e}'), pid=2)
def PKEY_Devices_Notifications_NewMessage():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2be9260a-2012-4742-a555-f41b638b7dcb}'), pid=2)
def PKEY_Devices_Notifications_NewVoicemail():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{59569556-0a08-4212-95b9-fae2ad6413db}'), pid=2)
def PKEY_Devices_Notifications_StorageFull():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a0e00ee1-f0c7-4d41-b8e7-26a7bd8d38b0}'), pid=2)
def PKEY_Devices_Notifications_StorageFullLinkText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a0e00ee1-f0c7-4d41-b8e7-26a7bd8d38b0}'), pid=3)
def PKEY_Devices_NotificationStore():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{06704b0c-e830-4c81-9178-91e4e95a80a0}'), pid=2)
def PKEY_Devices_NotWorkingProperly():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=83)
def PKEY_Devices_Paired():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=56)
def PKEY_Devices_Panel_PanelGroup():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8dbc9c86-97a9-4bff-9bc6-bfe95d3e6dad}'), pid=3)
def PKEY_Devices_Panel_PanelId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8dbc9c86-97a9-4bff-9bc6-bfe95d3e6dad}'), pid=2)
def PKEY_Devices_Parent():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=8)
def PKEY_Devices_PhoneLineTransportDevice_Connected():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{aecf2fe8-1d00-4fee-8a6d-a70d719b772b}'), pid=2)
def PKEY_Devices_PhysicalDeviceLocation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=9)
def PKEY_Devices_PlaybackPositionPercent():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3633de59-6825-4381-a49b-9f6ba13a1471}'), pid=5)
def PKEY_Devices_PlaybackState():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3633de59-6825-4381-a49b-9f6ba13a1471}'), pid=2)
PLAYBACKSTATE_UNKNOWN: UInt32 = 0
PLAYBACKSTATE_STOPPED: UInt32 = 1
PLAYBACKSTATE_PLAYING: UInt32 = 2
PLAYBACKSTATE_TRANSITIONING: UInt32 = 3
PLAYBACKSTATE_PAUSED: UInt32 = 4
PLAYBACKSTATE_RECORDINGPAUSED: UInt32 = 5
PLAYBACKSTATE_RECORDING: UInt32 = 6
PLAYBACKSTATE_NOMEDIA: UInt32 = 7
def PKEY_Devices_PlaybackTitle():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3633de59-6825-4381-a49b-9f6ba13a1471}'), pid=3)
def PKEY_Devices_Present():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=5)
def PKEY_Devices_PresentationUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8198)
def PKEY_Devices_PrimaryCategory():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d08dd4c0-3a9e-462e-8290-7b636b2576b9}'), pid=10)
def PKEY_Devices_RemainingDuration():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3633de59-6825-4381-a49b-9f6ba13a1471}'), pid=4)
def PKEY_Devices_RestrictedInterface():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=6)
def PKEY_Devices_Roaming():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=9)
def PKEY_Devices_SafeRemovalRequired():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{afd97640-86a3-4210-b67c-289c41aabe55}'), pid=2)
def PKEY_Devices_SchematicName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=9)
def PKEY_Devices_ServiceAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=16384)
def PKEY_Devices_ServiceId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=16385)
def PKEY_Devices_SharedTooltip():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{880f70a2-6082-47ac-8aab-a739d1a300c3}'), pid=151)
def PKEY_Devices_SignalStrength():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=2)
def PKEY_Devices_SmartCards_ReaderKind():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d6b5b883-18bd-4b4d-b2ec-9e38affeda82}'), pid=2)
def PKEY_Devices_Status():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d08dd4c0-3a9e-462e-8290-7b636b2576b9}'), pid=259)
def PKEY_Devices_Status1():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d08dd4c0-3a9e-462e-8290-7b636b2576b9}'), pid=257)
def PKEY_Devices_Status2():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d08dd4c0-3a9e-462e-8290-7b636b2576b9}'), pid=258)
def PKEY_Devices_StorageCapacity():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=12)
def PKEY_Devices_StorageFreeSpace():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=13)
def PKEY_Devices_StorageFreeSpacePercent():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=14)
def PKEY_Devices_TextMessages():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=3)
def PKEY_Devices_Voicemail():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49cd1f76-5626-4b17-a4e8-18b4aa1a2213}'), pid=6)
def PKEY_Devices_WiaDeviceType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6bdd1fc6-810f-11d0-bec7-08002be2092f}'), pid=2)
def PKEY_Devices_WiFi_InterfaceGuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ef1167eb-cbfc-4341-a568-a7c91a68982c}'), pid=2)
def PKEY_Devices_WiFiDirect_DeviceAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=13)
def PKEY_Devices_WiFiDirect_GroupId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=4)
def PKEY_Devices_WiFiDirect_InformationElements():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=12)
def PKEY_Devices_WiFiDirect_InterfaceAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=2)
def PKEY_Devices_WiFiDirect_InterfaceGuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=3)
def PKEY_Devices_WiFiDirect_IsConnected():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=5)
def PKEY_Devices_WiFiDirect_IsLegacyDevice():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=7)
def PKEY_Devices_WiFiDirect_IsMiracastLcpSupported():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=9)
def PKEY_Devices_WiFiDirect_IsVisible():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=6)
def PKEY_Devices_WiFiDirect_MiracastVersion():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=8)
def PKEY_Devices_WiFiDirect_Services():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=10)
def PKEY_Devices_WiFiDirect_SupportedChannelList():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1506935d-e3e7-450f-8637-82233ebe5f6e}'), pid=11)
def PKEY_Devices_WiFiDirectServices_AdvertisementId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{31b37743-7c5e-4005-93e6-e953f92b82e9}'), pid=5)
def PKEY_Devices_WiFiDirectServices_RequestServiceInformation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{31b37743-7c5e-4005-93e6-e953f92b82e9}'), pid=7)
def PKEY_Devices_WiFiDirectServices_ServiceAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{31b37743-7c5e-4005-93e6-e953f92b82e9}'), pid=2)
def PKEY_Devices_WiFiDirectServices_ServiceConfigMethods():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{31b37743-7c5e-4005-93e6-e953f92b82e9}'), pid=6)
def PKEY_Devices_WiFiDirectServices_ServiceInformation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{31b37743-7c5e-4005-93e6-e953f92b82e9}'), pid=4)
def PKEY_Devices_WiFiDirectServices_ServiceName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{31b37743-7c5e-4005-93e6-e953f92b82e9}'), pid=3)
def PKEY_Devices_WinPhone8CameraFlags():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b7b4d61c-5a64-4187-a52e-b1539f359099}'), pid=2)
def PKEY_Devices_Wwan_InterfaceGuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ff1167eb-cbfc-4341-a568-a7c91a68982c}'), pid=2)
def PKEY_Storage_Portable():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4d1ebee8-0803-4774-9842-b77db50265e9}'), pid=2)
def PKEY_Storage_RemovableMedia():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4d1ebee8-0803-4774-9842-b77db50265e9}'), pid=3)
def PKEY_Storage_SystemCritical():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4d1ebee8-0803-4774-9842-b77db50265e9}'), pid=4)
def PKEY_Document_ByteCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=4)
def PKEY_Document_CharacterCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=16)
def PKEY_Document_ClientID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{276d7bb0-5b34-4fb0-aa4b-158ed12a1809}'), pid=100)
def PKEY_Document_Contributor():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f334115e-da1b-4509-9b3d-119504dc7abb}'), pid=100)
def PKEY_Document_DateCreated():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=12)
def PKEY_Document_DatePrinted():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=11)
def PKEY_Document_DateSaved():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=13)
def PKEY_Document_Division():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1e005ee6-bf27-428b-b01c-79676acd2870}'), pid=100)
def PKEY_Document_DocumentID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e08805c8-e395-40df-80d2-54f0d6c43154}'), pid=100)
def PKEY_Document_HiddenSlideCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=9)
def PKEY_Document_LastAuthor():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=8)
def PKEY_Document_LineCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=5)
def PKEY_Document_Manager():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=14)
def PKEY_Document_MultimediaClipCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=10)
def PKEY_Document_NoteCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=8)
def PKEY_Document_PageCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=14)
def PKEY_Document_ParagraphCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=6)
def PKEY_Document_PresentationFormat():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=3)
def PKEY_Document_RevisionNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=9)
def PKEY_Document_Security():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=19)
def PKEY_Document_SlideCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=7)
def PKEY_Document_Template():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=7)
def PKEY_Document_TotalEditingTime():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=10)
def PKEY_Document_Version():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}'), pid=29)
def PKEY_Document_WordCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}'), pid=15)
def PKEY_DRM_DatePlayExpires():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{aeac19e4-89ae-4508-b9b7-bb867abee2ed}'), pid=6)
def PKEY_DRM_DatePlayStarts():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{aeac19e4-89ae-4508-b9b7-bb867abee2ed}'), pid=5)
def PKEY_DRM_Description():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{aeac19e4-89ae-4508-b9b7-bb867abee2ed}'), pid=3)
def PKEY_DRM_IsDisabled():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{aeac19e4-89ae-4508-b9b7-bb867abee2ed}'), pid=7)
def PKEY_DRM_IsProtected():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{aeac19e4-89ae-4508-b9b7-bb867abee2ed}'), pid=2)
def PKEY_DRM_PlayCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{aeac19e4-89ae-4508-b9b7-bb867abee2ed}'), pid=4)
def PKEY_GPS_Altitude():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{827edb4f-5b73-44a7-891d-fdffabea35ca}'), pid=100)
def PKEY_GPS_AltitudeDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78342dcb-e358-4145-ae9a-6bfe4e0f9f51}'), pid=100)
def PKEY_GPS_AltitudeNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2dad1eb7-816d-40d3-9ec3-c9773be2aade}'), pid=100)
def PKEY_GPS_AltitudeRef():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{46ac629d-75ea-4515-867f-6dc4321c5844}'), pid=100)
def PKEY_GPS_AreaInformation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{972e333e-ac7e-49f1-8adf-a70d07a9bcab}'), pid=100)
def PKEY_GPS_Date():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3602c812-0f3b-45f0-85ad-603468d69423}'), pid=100)
def PKEY_GPS_DestBearing():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c66d4b3c-e888-47cc-b99f-9dca3ee34dea}'), pid=100)
def PKEY_GPS_DestBearingDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7abcf4f8-7c3f-4988-ac91-8d2c2e97eca5}'), pid=100)
def PKEY_GPS_DestBearingNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ba3b1da9-86ee-4b5d-a2a4-a271a429f0cf}'), pid=100)
def PKEY_GPS_DestBearingRef():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9ab84393-2a0f-4b75-bb22-7279786977cb}'), pid=100)
def PKEY_GPS_DestDistance():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a93eae04-6804-4f24-ac81-09b266452118}'), pid=100)
def PKEY_GPS_DestDistanceDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9bc2c99b-ac71-4127-9d1c-2596d0d7dcb7}'), pid=100)
def PKEY_GPS_DestDistanceNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2bda47da-08c6-4fe1-80bc-a72fc517c5d0}'), pid=100)
def PKEY_GPS_DestDistanceRef():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ed4df2d3-8695-450b-856f-f5c1c53acb66}'), pid=100)
def PKEY_GPS_DestLatitude():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9d1d7cc5-5c39-451c-86b3-928e2d18cc47}'), pid=100)
def PKEY_GPS_DestLatitudeDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3a372292-7fca-49a7-99d5-e47bb2d4e7ab}'), pid=100)
def PKEY_GPS_DestLatitudeNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ecf4b6f6-d5a6-433c-bb92-4076650fc890}'), pid=100)
def PKEY_GPS_DestLatitudeRef():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cea820b9-ce61-4885-a128-005d9087c192}'), pid=100)
def PKEY_GPS_DestLongitude():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{47a96261-cb4c-4807-8ad3-40b9d9dbc6bc}'), pid=100)
def PKEY_GPS_DestLongitudeDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{425d69e5-48ad-4900-8d80-6eb6b8d0ac86}'), pid=100)
def PKEY_GPS_DestLongitudeNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a3250282-fb6d-48d5-9a89-dbcace75cccf}'), pid=100)
def PKEY_GPS_DestLongitudeRef():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{182c1ea6-7c1c-4083-ab4b-ac6c9f4ed128}'), pid=100)
def PKEY_GPS_Differential():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{aaf4ee25-bd3b-4dd7-bfc4-47f77bb00f6d}'), pid=100)
def PKEY_GPS_DOP():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0cf8fb02-1837-42f1-a697-a7017aa289b9}'), pid=100)
def PKEY_GPS_DOPDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a0be94c5-50ba-487b-bd35-0654be8881ed}'), pid=100)
def PKEY_GPS_DOPNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{47166b16-364f-4aa0-9f31-e2ab3df449c3}'), pid=100)
def PKEY_GPS_ImgDirection():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{16473c91-d017-4ed9-ba4d-b6baa55dbcf8}'), pid=100)
def PKEY_GPS_ImgDirectionDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{10b24595-41a2-4e20-93c2-5761c1395f32}'), pid=100)
def PKEY_GPS_ImgDirectionNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{dc5877c7-225f-45f7-bac7-e81334b6130a}'), pid=100)
def PKEY_GPS_ImgDirectionRef():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a4aaa5b7-1ad0-445f-811a-0f8f6e67f6b5}'), pid=100)
def PKEY_GPS_Latitude():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8727cfff-4868-4ec6-ad5b-81b98521d1ab}'), pid=100)
def PKEY_GPS_LatitudeDecimal():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0f55cde2-4f49-450d-92c1-dcd16301b1b7}'), pid=100)
def PKEY_GPS_LatitudeDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{16e634ee-2bff-497b-bd8a-4341ad39eeb9}'), pid=100)
def PKEY_GPS_LatitudeNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7ddaaad1-ccc8-41ae-b750-b2cb8031aea2}'), pid=100)
def PKEY_GPS_LatitudeRef():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{029c0252-5b86-46c7-aca0-2769ffc8e3d4}'), pid=100)
def PKEY_GPS_Longitude():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c4c4dbb2-b593-466b-bbda-d03d27d5e43a}'), pid=100)
def PKEY_GPS_LongitudeDecimal():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4679c1b5-844d-4590-baf5-f322231f1b81}'), pid=100)
def PKEY_GPS_LongitudeDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{be6e176c-4534-4d2c-ace5-31dedac1606b}'), pid=100)
def PKEY_GPS_LongitudeNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{02b0f689-a914-4e45-821d-1dda452ed2c4}'), pid=100)
def PKEY_GPS_LongitudeRef():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{33dcf22b-28d5-464c-8035-1ee9efd25278}'), pid=100)
def PKEY_GPS_MapDatum():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2ca2dae6-eddc-407d-bef1-773942abfa95}'), pid=100)
def PKEY_GPS_MeasureMode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a015ed5d-aaea-4d58-8a86-3c586920ea0b}'), pid=100)
def PKEY_GPS_ProcessingMethod():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{59d49e61-840f-4aa9-a939-e2099b7f6399}'), pid=100)
def PKEY_GPS_Satellites():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{467ee575-1f25-4557-ad4e-b8b58b0d9c15}'), pid=100)
def PKEY_GPS_Speed():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{da5d0862-6e76-4e1b-babd-70021bd25494}'), pid=100)
def PKEY_GPS_SpeedDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7d122d5a-ae5e-4335-8841-d71e7ce72f53}'), pid=100)
def PKEY_GPS_SpeedNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{acc9ce3d-c213-4942-8b48-6d0820f21c6d}'), pid=100)
def PKEY_GPS_SpeedRef():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ecf7f4c9-544f-4d6d-9d98-8ad79adaf453}'), pid=100)
def PKEY_GPS_Status():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{125491f4-818f-46b2-91b5-d537753617b2}'), pid=100)
def PKEY_GPS_Track():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{76c09943-7c33-49e3-9e7e-cdba872cfada}'), pid=100)
def PKEY_GPS_TrackDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c8d1920c-01f6-40c0-ac86-2f3a4ad00770}'), pid=100)
def PKEY_GPS_TrackNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{702926f4-44a6-43e1-ae71-45627116893b}'), pid=100)
def PKEY_GPS_TrackRef():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{35dbe6fe-44c3-4400-aaae-d2c799c407e8}'), pid=100)
def PKEY_GPS_VersionID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{22704da4-c6b2-4a99-8e56-f16df8c92599}'), pid=100)
def PKEY_History_VisitCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5cbf2787-48cf-4208-b90e-ee5e5d420294}'), pid=7)
def PKEY_Image_BitDepth():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6444048f-4c8b-11d1-8b70-080036b11a03}'), pid=7)
def PKEY_Image_ColorSpace():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=40961)
def PKEY_Image_CompressedBitsPerPixel():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{364b6fa9-37ab-482a-be2b-ae02f60d4318}'), pid=100)
def PKEY_Image_CompressedBitsPerPixelDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1f8844e1-24ad-4508-9dfd-5326a415ce02}'), pid=100)
def PKEY_Image_CompressedBitsPerPixelNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d21a7148-d32c-4624-8900-277210f79c0f}'), pid=100)
def PKEY_Image_Compression():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=259)
def PKEY_Image_CompressionText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f08e66f-2f44-4bb9-a682-ac35d2562322}'), pid=100)
def PKEY_Image_Dimensions():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6444048f-4c8b-11d1-8b70-080036b11a03}'), pid=13)
def PKEY_Image_HorizontalResolution():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6444048f-4c8b-11d1-8b70-080036b11a03}'), pid=5)
def PKEY_Image_HorizontalSize():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6444048f-4c8b-11d1-8b70-080036b11a03}'), pid=3)
def PKEY_Image_ImageID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{10dabe05-32aa-4c29-bf1a-63e2d220587f}'), pid=100)
def PKEY_Image_ResolutionUnit():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{19b51fa6-1f92-4a5c-ab48-7df0abd67444}'), pid=100)
def PKEY_Image_VerticalResolution():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6444048f-4c8b-11d1-8b70-080036b11a03}'), pid=6)
def PKEY_Image_VerticalSize():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6444048f-4c8b-11d1-8b70-080036b11a03}'), pid=4)
def PKEY_Journal_Contacts():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{dea7c82c-1d89-4a66-9427-a4e3debabcb1}'), pid=100)
def PKEY_Journal_EntryType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{95beb1fc-326d-4644-b396-cd3ed90e6ddf}'), pid=100)
def PKEY_LayoutPattern_ContentViewModeForBrowse():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=500)
LAYOUTPATTERN_CVMFB_ALPHA: String = 'alpha'
LAYOUTPATTERN_CVMFB_BETA: String = 'beta'
LAYOUTPATTERN_CVMFB_GAMMA: String = 'gamma'
LAYOUTPATTERN_CVMFB_DELTA: String = 'delta'
def PKEY_LayoutPattern_ContentViewModeForSearch():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=501)
LAYOUTPATTERN_CVMFS_ALPHA: String = 'alpha'
LAYOUTPATTERN_CVMFS_BETA: String = 'beta'
LAYOUTPATTERN_CVMFS_GAMMA: String = 'gamma'
LAYOUTPATTERN_CVMFS_DELTA: String = 'delta'
def PKEY_History_SelectionCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1ce0d6bc-536c-4600-b0dd-7e0c66b350d5}'), pid=8)
def PKEY_History_TargetUrlHostName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1ce0d6bc-536c-4600-b0dd-7e0c66b350d5}'), pid=9)
def PKEY_Link_Arguments():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{436f2667-14e2-4feb-b30a-146c53b5b674}'), pid=100)
def PKEY_Link_Comment():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b9b4b3fc-2b51-4a42-b5d8-324146afcf25}'), pid=5)
def PKEY_Link_DateVisited():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5cbf2787-48cf-4208-b90e-ee5e5d420294}'), pid=23)
def PKEY_Link_Description():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5cbf2787-48cf-4208-b90e-ee5e5d420294}'), pid=21)
def PKEY_Link_FeedItemLocalId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8a2f99f9-3c37-465d-a8d7-69777a246d0c}'), pid=2)
def PKEY_Link_Status():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b9b4b3fc-2b51-4a42-b5d8-324146afcf25}'), pid=3)
LINK_STATUS_RESOLVED: Int32 = 1
LINK_STATUS_BROKEN: Int32 = 2
def PKEY_Link_TargetExtension():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7a7d76f4-b630-4bd7-95ff-37cc51a975c9}'), pid=2)
def PKEY_Link_TargetParsingPath():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b9b4b3fc-2b51-4a42-b5d8-324146afcf25}'), pid=2)
def PKEY_Link_TargetSFGAOFlags():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b9b4b3fc-2b51-4a42-b5d8-324146afcf25}'), pid=8)
def PKEY_Link_TargetUrlHostName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8a2f99f9-3c37-465d-a8d7-69777a246d0c}'), pid=5)
def PKEY_Link_TargetUrlPath():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8a2f99f9-3c37-465d-a8d7-69777a246d0c}'), pid=6)
def PKEY_Media_AuthorUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=32)
def PKEY_Media_AverageLevel():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{09edd5b6-b301-43c5-9990-d00302effd46}'), pid=100)
def PKEY_Media_ClassPrimaryID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=13)
def PKEY_Media_ClassSecondaryID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=14)
def PKEY_Media_CollectionGroupID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=24)
def PKEY_Media_CollectionID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=25)
def PKEY_Media_ContentDistributor():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=18)
def PKEY_Media_ContentID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=26)
def PKEY_Media_CreatorApplication():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=27)
def PKEY_Media_CreatorApplicationVersion():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=28)
def PKEY_Media_DateEncoded():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2e4b640d-5019-46d8-8881-55414cc5caa0}'), pid=100)
def PKEY_Media_DateReleased():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{de41cc29-6971-4290-b472-f59f2e2f31e2}'), pid=100)
def PKEY_Media_DlnaProfileID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cfa31b45-525d-4998-bb44-3f7d81542fa4}'), pid=100)
def PKEY_Media_Duration():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440490-4c8b-11d1-8b70-080036b11a03}'), pid=3)
def PKEY_Media_DVDID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=15)
def PKEY_Media_EncodedBy():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=36)
def PKEY_Media_EncodingSettings():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=37)
def PKEY_Media_EpisodeNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=100)
def PKEY_Media_FrameCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6444048f-4c8b-11d1-8b70-080036b11a03}'), pid=12)
def PKEY_Media_MCDI():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=16)
def PKEY_Media_MetadataContentProvider():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=17)
def PKEY_Media_Producer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=22)
def PKEY_Media_PromotionUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=33)
def PKEY_Media_ProtectionType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=38)
def PKEY_Media_ProviderRating():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=39)
def PKEY_Media_ProviderStyle():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=40)
def PKEY_Media_Publisher():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=30)
def PKEY_Media_SeasonNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=101)
def PKEY_Media_SeriesName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=42)
def PKEY_Media_SubscriptionContentId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9aebae7a-9644-487d-a92c-657585ed751a}'), pid=100)
def PKEY_Media_SubTitle():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=38)
def PKEY_Media_ThumbnailLargePath():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=47)
def PKEY_Media_ThumbnailLargeUri():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=48)
def PKEY_Media_ThumbnailSmallPath():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=49)
def PKEY_Media_ThumbnailSmallUri():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=50)
def PKEY_Media_UniqueFileIdentifier():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=35)
def PKEY_Media_UserNoAutoInfo():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=41)
def PKEY_Media_UserWebUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=34)
def PKEY_Media_Writer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=23)
def PKEY_Media_Year():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=5)
def PKEY_Message_AttachmentContents():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3143bf7c-80a8-4854-8880-e2e40189bdd0}'), pid=100)
def PKEY_Message_AttachmentNames():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=21)
def PKEY_Message_BccAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=2)
def PKEY_Message_BccName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=3)
def PKEY_Message_CcAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=4)
def PKEY_Message_CcName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=5)
def PKEY_Message_ConversationID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{dc8f80bd-af1e-4289-85b6-3dfc1b493992}'), pid=100)
def PKEY_Message_ConversationIndex():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{dc8f80bd-af1e-4289-85b6-3dfc1b493992}'), pid=101)
def PKEY_Message_DateReceived():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=20)
def PKEY_Message_DateSent():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=19)
def PKEY_Message_Flags():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a82d9ee7-ca67-4312-965e-226bcea85023}'), pid=100)
def PKEY_Message_FromAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=13)
def PKEY_Message_FromName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=14)
def PKEY_Message_HasAttachments():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9c1fcf74-2d97-41ba-b4ae-cb2e3661a6e4}'), pid=8)
def PKEY_Message_IsFwdOrReply():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9a9bc088-4f6d-469e-9919-e705412040f9}'), pid=100)
def PKEY_Message_MessageClass():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cd9ed458-08ce-418f-a70e-f912c7bb9c5c}'), pid=103)
def PKEY_Message_Participants():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1a9ba605-8e7c-4d11-ad7d-a50ada18ba1b}'), pid=2)
def PKEY_Message_ProofInProgress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9098f33c-9a7d-48a8-8de5-2e1227a64e91}'), pid=100)
def PKEY_Message_SenderAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0be1c8e7-1981-4676-ae14-fdd78f05a6e7}'), pid=100)
def PKEY_Message_SenderName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0da41cfa-d224-4a18-ae2f-596158db4b3a}'), pid=100)
def PKEY_Message_Store():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=15)
def PKEY_Message_ToAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=16)
def PKEY_Message_ToDoFlags():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1f856a9f-6900-4aba-9505-2d5f1b4d66cb}'), pid=100)
def PKEY_Message_ToDoTitle():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bccc8a3c-8cef-42e5-9b1c-c69079398bc7}'), pid=100)
def PKEY_Message_ToName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3e0584c-b788-4a5a-bb20-7f5a44c9acdd}'), pid=17)
def PKEY_Music_AlbumArtist():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=13)
def PKEY_Music_AlbumArtistSortOverride():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f1fdb4af-f78c-466c-bb05-56e92db0b8ec}'), pid=103)
def PKEY_Music_AlbumID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=100)
def PKEY_Music_AlbumTitle():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=4)
def PKEY_Music_AlbumTitleSortOverride():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{13eb7ffc-ec89-4346-b19d-ccc6f1784223}'), pid=101)
def PKEY_Music_Artist():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=2)
def PKEY_Music_ArtistSortOverride():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{deeb2db5-0696-4ce0-94fe-a01f77a45fb5}'), pid=102)
def PKEY_Music_BeatsPerMinute():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=35)
def PKEY_Music_Composer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=19)
def PKEY_Music_ComposerSortOverride():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00bc20a3-bd48-4085-872c-a88d77f5097e}'), pid=105)
def PKEY_Music_Conductor():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=36)
def PKEY_Music_ContentGroupDescription():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=33)
def PKEY_Music_DiscNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6afe7437-9bcd-49c7-80fe-4a5c65fa5874}'), pid=104)
def PKEY_Music_DisplayArtist():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fd122953-fa93-4ef7-92c3-04c946b2f7c8}'), pid=100)
def PKEY_Music_Genre():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=11)
def PKEY_Music_InitialKey():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=34)
def PKEY_Music_IsCompilation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c449d5cb-9ea4-4809-82e8-af9d59ded6d1}'), pid=100)
def PKEY_Music_Lyrics():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=12)
def PKEY_Music_Mood():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=39)
def PKEY_Music_PartOfSet():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=37)
def PKEY_Music_Period():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=31)
def PKEY_Music_SynchronizedLyrics():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6b223b6a-162e-4aa9-b39f-05d678fc6d77}'), pid=100)
def PKEY_Music_TrackNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}'), pid=7)
def PKEY_Note_Color():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4776cafa-bce4-4cb1-a23e-265e76d8eb11}'), pid=100)
def PKEY_Note_ColorText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{46b4e8de-cdb2-440d-885c-1658eb65b914}'), pid=100)
def PKEY_Photo_Aperture():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=37378)
def PKEY_Photo_ApertureDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e1a9a38b-6685-46bd-875e-570dc7ad7320}'), pid=100)
def PKEY_Photo_ApertureNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0337ecec-39fb-4581-a0bd-4c4cc51e9914}'), pid=100)
def PKEY_Photo_Brightness():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1a701bf6-478c-4361-83ab-3701bb053c58}'), pid=100)
def PKEY_Photo_BrightnessDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6ebe6946-2321-440a-90f0-c043efd32476}'), pid=100)
def PKEY_Photo_BrightnessNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9e7d118f-b314-45a0-8cfb-d654b917c9e9}'), pid=100)
def PKEY_Photo_CameraManufacturer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=271)
def PKEY_Photo_CameraModel():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=272)
def PKEY_Photo_CameraSerialNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=273)
def PKEY_Photo_Contrast():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2a785ba9-8d23-4ded-82e6-60a350c86a10}'), pid=100)
PHOTO_CONTRAST_NORMAL: UInt32 = 0
PHOTO_CONTRAST_SOFT: UInt32 = 1
PHOTO_CONTRAST_HARD: UInt32 = 2
def PKEY_Photo_ContrastText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{59dde9f2-5253-40ea-9a8b-479e96c6249a}'), pid=100)
def PKEY_Photo_DateTaken():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=36867)
def PKEY_Photo_DigitalZoom():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f85bf840-a925-4bc2-b0c4-8e36b598679e}'), pid=100)
def PKEY_Photo_DigitalZoomDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{745baf0e-e5c1-4cfb-8a1b-d031a0a52393}'), pid=100)
def PKEY_Photo_DigitalZoomNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{16cbb924-6500-473b-a5be-f1599bcbe413}'), pid=100)
def PKEY_Photo_Event():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=18248)
def PKEY_Photo_EXIFVersion():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d35f743a-eb2e-47f2-a286-844132cb1427}'), pid=100)
def PKEY_Photo_ExposureBias():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=37380)
def PKEY_Photo_ExposureBiasDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ab205e50-04b7-461c-a18c-2f233836e627}'), pid=100)
def PKEY_Photo_ExposureBiasNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{738bf284-1d87-420b-92cf-5834bf6ef9ed}'), pid=100)
def PKEY_Photo_ExposureIndex():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{967b5af8-995a-46ed-9e11-35b3c5b9782d}'), pid=100)
def PKEY_Photo_ExposureIndexDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{93112f89-c28b-492f-8a9d-4be2062cee8a}'), pid=100)
def PKEY_Photo_ExposureIndexNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cdedcf30-8919-44df-8f4c-4eb2ffdb8d89}'), pid=100)
def PKEY_Photo_ExposureProgram():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=34850)
PHOTO_EXPOSUREPROGRAM_UNKNOWN: UInt32 = 0
PHOTO_EXPOSUREPROGRAM_MANUAL: UInt32 = 1
PHOTO_EXPOSUREPROGRAM_NORMAL: UInt32 = 2
PHOTO_EXPOSUREPROGRAM_APERTURE: UInt32 = 3
PHOTO_EXPOSUREPROGRAM_SHUTTER: UInt32 = 4
PHOTO_EXPOSUREPROGRAM_CREATIVE: UInt32 = 5
PHOTO_EXPOSUREPROGRAM_ACTION: UInt32 = 6
PHOTO_EXPOSUREPROGRAM_PORTRAIT: UInt32 = 7
PHOTO_EXPOSUREPROGRAM_LANDSCAPE: UInt32 = 8
def PKEY_Photo_ExposureProgramText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fec690b7-5f30-4646-ae47-4caafba884a3}'), pid=100)
def PKEY_Photo_ExposureTime():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=33434)
def PKEY_Photo_ExposureTimeDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{55e98597-ad16-42e0-b624-21599a199838}'), pid=100)
def PKEY_Photo_ExposureTimeNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{257e44e2-9031-4323-ac38-85c552871b2e}'), pid=100)
def PKEY_Photo_Flash():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=37385)
PHOTO_FLASH_NONE: UInt32 = 0
PHOTO_FLASH_FLASH: UInt32 = 1
PHOTO_FLASH_WITHOUTSTROBE: UInt32 = 5
PHOTO_FLASH_WITHSTROBE: UInt32 = 7
PHOTO_FLASH_FLASH_COMPULSORY: UInt32 = 9
PHOTO_FLASH_FLASH_COMPULSORY_NORETURNLIGHT: UInt32 = 13
PHOTO_FLASH_FLASH_COMPULSORY_RETURNLIGHT: UInt32 = 15
PHOTO_FLASH_NONE_COMPULSORY: UInt32 = 16
PHOTO_FLASH_NONE_AUTO: UInt32 = 24
PHOTO_FLASH_FLASH_AUTO: UInt32 = 25
PHOTO_FLASH_FLASH_AUTO_NORETURNLIGHT: UInt32 = 29
PHOTO_FLASH_FLASH_AUTO_RETURNLIGHT: UInt32 = 31
PHOTO_FLASH_NOFUNCTION: UInt32 = 32
PHOTO_FLASH_FLASH_REDEYE: UInt32 = 65
PHOTO_FLASH_FLASH_REDEYE_NORETURNLIGHT: UInt32 = 69
PHOTO_FLASH_FLASH_REDEYE_RETURNLIGHT: UInt32 = 71
PHOTO_FLASH_FLASH_COMPULSORY_REDEYE: UInt32 = 73
PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_NORETURNLIGHT: UInt32 = 77
PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_RETURNLIGHT: UInt32 = 79
PHOTO_FLASH_FLASH_AUTO_REDEYE: UInt32 = 89
PHOTO_FLASH_FLASH_AUTO_REDEYE_NORETURNLIGHT: UInt32 = 93
PHOTO_FLASH_FLASH_AUTO_REDEYE_RETURNLIGHT: UInt32 = 95
def PKEY_Photo_FlashEnergy():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=41483)
def PKEY_Photo_FlashEnergyDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d7b61c70-6323-49cd-a5fc-c84277162c97}'), pid=100)
def PKEY_Photo_FlashEnergyNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fcad3d3d-0858-400f-aaa3-2f66cce2a6bc}'), pid=100)
def PKEY_Photo_FlashManufacturer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{aabaf6c9-e0c5-4719-8585-57b103e584fe}'), pid=100)
def PKEY_Photo_FlashModel():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fe83bb35-4d1a-42e2-916b-06f3e1af719e}'), pid=100)
def PKEY_Photo_FlashText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6b8b68f6-200b-47ea-8d25-d8050f57339f}'), pid=100)
def PKEY_Photo_FNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=33437)
def PKEY_Photo_FNumberDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e92a2496-223b-4463-a4e3-30eabba79d80}'), pid=100)
def PKEY_Photo_FNumberNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1b97738a-fdfc-462f-9d93-1957e08be90c}'), pid=100)
def PKEY_Photo_FocalLength():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=37386)
def PKEY_Photo_FocalLengthDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{305bc615-dca1-44a5-9fd4-10c0ba79412e}'), pid=100)
def PKEY_Photo_FocalLengthInFilm():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a0e74609-b84d-4f49-b860-462bd9971f98}'), pid=100)
def PKEY_Photo_FocalLengthNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{776b6b3b-1e3d-4b0c-9a0e-8fbaf2a8492a}'), pid=100)
def PKEY_Photo_FocalPlaneXResolution():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cfc08d97-c6f7-4484-89dd-ebef4356fe76}'), pid=100)
def PKEY_Photo_FocalPlaneXResolutionDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0933f3f5-4786-4f46-a8e8-d64dd37fa521}'), pid=100)
def PKEY_Photo_FocalPlaneXResolutionNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{dccb10af-b4e2-4b88-95f9-031b4d5ab490}'), pid=100)
def PKEY_Photo_FocalPlaneYResolution():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4fffe4d0-914f-4ac4-8d6f-c9c61de169b1}'), pid=100)
def PKEY_Photo_FocalPlaneYResolutionDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1d6179a6-a876-4031-b013-3347b2b64dc8}'), pid=100)
def PKEY_Photo_FocalPlaneYResolutionNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a2e541c5-4440-4ba8-867e-75cfc06828cd}'), pid=100)
def PKEY_Photo_GainControl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fa304789-00c7-4d80-904a-1e4dcc7265aa}'), pid=100)
PHOTO_GAINCONTROL_NONE: Double = 0
PHOTO_GAINCONTROL_LOWGAINUP: Double = 1
PHOTO_GAINCONTROL_HIGHGAINUP: Double = 2
PHOTO_GAINCONTROL_LOWGAINDOWN: Double = 3
PHOTO_GAINCONTROL_HIGHGAINDOWN: Double = 4
def PKEY_Photo_GainControlDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{42864dfd-9da4-4f77-bded-4aad7b256735}'), pid=100)
def PKEY_Photo_GainControlNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8e8ecf7c-b7b8-4eb8-a63f-0ee715c96f9e}'), pid=100)
def PKEY_Photo_GainControlText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c06238b2-0bf9-4279-a723-25856715cb9d}'), pid=100)
def PKEY_Photo_ISOSpeed():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=34855)
def PKEY_Photo_LensManufacturer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e6ddcaf7-29c5-4f0a-9a68-d19412ec7090}'), pid=100)
def PKEY_Photo_LensModel():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e1277516-2b5f-4869-89b1-2e585bd38b7a}'), pid=100)
def PKEY_Photo_LightSource():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=37384)
PHOTO_LIGHTSOURCE_UNKNOWN: UInt32 = 0
PHOTO_LIGHTSOURCE_DAYLIGHT: UInt32 = 1
PHOTO_LIGHTSOURCE_FLUORESCENT: UInt32 = 2
PHOTO_LIGHTSOURCE_TUNGSTEN: UInt32 = 3
PHOTO_LIGHTSOURCE_STANDARD_A: UInt32 = 17
PHOTO_LIGHTSOURCE_STANDARD_B: UInt32 = 18
PHOTO_LIGHTSOURCE_STANDARD_C: UInt32 = 19
PHOTO_LIGHTSOURCE_D55: UInt32 = 20
PHOTO_LIGHTSOURCE_D65: UInt32 = 21
PHOTO_LIGHTSOURCE_D75: UInt32 = 22
def PKEY_Photo_MakerNote():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fa303353-b659-4052-85e9-bcac79549b84}'), pid=100)
def PKEY_Photo_MakerNoteOffset():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{813f4124-34e6-4d17-ab3e-6b1f3c2247a1}'), pid=100)
def PKEY_Photo_MaxAperture():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{08f6d7c2-e3f2-44fc-af1e-5aa5c81a2d3e}'), pid=100)
def PKEY_Photo_MaxApertureDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c77724d4-601f-46c5-9b89-c53f93bceb77}'), pid=100)
def PKEY_Photo_MaxApertureNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c107e191-a459-44c5-9ae6-b952ad4b906d}'), pid=100)
def PKEY_Photo_MeteringMode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=37383)
def PKEY_Photo_MeteringModeText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f628fd8c-7ba8-465a-a65b-c5aa79263a9e}'), pid=100)
def PKEY_Photo_Orientation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=274)
def PKEY_Photo_OrientationText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a9ea193c-c511-498a-a06b-58e2776dcc28}'), pid=100)
def PKEY_Photo_PeopleNames():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e8309b6e-084c-49b4-b1fc-90a80331b638}'), pid=100)
def PKEY_Photo_PhotometricInterpretation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{341796f1-1df9-4b1c-a564-91bdefa43877}'), pid=100)
def PKEY_Photo_PhotometricInterpretationText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{821437d6-9eab-4765-a589-3b1cbbd22a61}'), pid=100)
def PKEY_Photo_ProgramMode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d217f6d-3f6a-4825-b470-5f03ca2fbe9b}'), pid=100)
PHOTO_PROGRAMMODE_NOTDEFINED: UInt32 = 0
PHOTO_PROGRAMMODE_MANUAL: UInt32 = 1
PHOTO_PROGRAMMODE_NORMAL: UInt32 = 2
PHOTO_PROGRAMMODE_APERTURE: UInt32 = 3
PHOTO_PROGRAMMODE_SHUTTER: UInt32 = 4
PHOTO_PROGRAMMODE_CREATIVE: UInt32 = 5
PHOTO_PROGRAMMODE_ACTION: UInt32 = 6
PHOTO_PROGRAMMODE_PORTRAIT: UInt32 = 7
PHOTO_PROGRAMMODE_LANDSCAPE: UInt32 = 8
def PKEY_Photo_ProgramModeText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7fe3aa27-2648-42f3-89b0-454e5cb150c3}'), pid=100)
def PKEY_Photo_RelatedSoundFile():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{318a6b45-087f-4dc2-b8cc-05359551fc9e}'), pid=100)
def PKEY_Photo_Saturation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49237325-a95a-4f67-b211-816b2d45d2e0}'), pid=100)
PHOTO_SATURATION_NORMAL: UInt32 = 0
PHOTO_SATURATION_LOW: UInt32 = 1
PHOTO_SATURATION_HIGH: UInt32 = 2
def PKEY_Photo_SaturationText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{61478c08-b600-4a84-bbe4-e99c45f0a072}'), pid=100)
def PKEY_Photo_Sharpness():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{fc6976db-8349-4970-ae97-b3c5316a08f0}'), pid=100)
PHOTO_SHARPNESS_NORMAL: UInt32 = 0
PHOTO_SHARPNESS_SOFT: UInt32 = 1
PHOTO_SHARPNESS_HARD: UInt32 = 2
def PKEY_Photo_SharpnessText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{51ec3f47-dd50-421d-8769-334f50424b1e}'), pid=100)
def PKEY_Photo_ShutterSpeed():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=37377)
def PKEY_Photo_ShutterSpeedDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e13d8975-81c7-4948-ae3f-37cae11e8ff7}'), pid=100)
def PKEY_Photo_ShutterSpeedNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{16ea4042-d6f4-4bca-8349-7c78d30fb333}'), pid=100)
def PKEY_Photo_SubjectDistance():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}'), pid=37382)
def PKEY_Photo_SubjectDistanceDenominator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0c840a88-b043-466d-9766-d4b26da3fa77}'), pid=100)
def PKEY_Photo_SubjectDistanceNumerator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8af4961c-f526-43e5-aa81-db768219178d}'), pid=100)
def PKEY_Photo_TagViewAggregate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b812f15d-c2d8-4bbf-bacd-79744346113f}'), pid=100)
def PKEY_Photo_TranscodedForSync():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9a8ebb75-6458-4e82-bacb-35c0095b03bb}'), pid=100)
def PKEY_Photo_WhiteBalance():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ee3d3d8a-5381-4cfa-b13b-aaf66b5f4ec9}'), pid=100)
PHOTO_WHITEBALANCE_AUTO: UInt32 = 0
PHOTO_WHITEBALANCE_MANUAL: UInt32 = 1
def PKEY_Photo_WhiteBalanceText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6336b95e-c7a7-426d-86fd-7ae3d39c84b4}'), pid=100)
def PKEY_PropGroup_Advanced():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{900a403b-097b-4b95-8ae2-071fdaeeb118}'), pid=100)
def PKEY_PropGroup_Audio():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2804d469-788f-48aa-8570-71b9c187e138}'), pid=100)
def PKEY_PropGroup_Calendar():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9973d2b5-bfd8-438a-ba94-5349b293181a}'), pid=100)
def PKEY_PropGroup_Camera():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{de00de32-547e-4981-ad4b-542f2e9007d8}'), pid=100)
def PKEY_PropGroup_Contact():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{df975fd3-250a-4004-858f-34e29a3e37aa}'), pid=100)
def PKEY_PropGroup_Content():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d0dab0ba-368a-4050-a882-6c010fd19a4f}'), pid=100)
def PKEY_PropGroup_Description():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8969b275-9475-4e00-a887-ff93b8b41e44}'), pid=100)
def PKEY_PropGroup_FileSystem():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3a7d2c1-80fc-4b40-8f34-30ea111bdc2e}'), pid=100)
def PKEY_PropGroup_General():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cc301630-b192-4c22-b372-9f4c6d338e07}'), pid=100)
def PKEY_PropGroup_GPS():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f3713ada-90e3-4e11-aae5-fdc17685b9be}'), pid=100)
def PKEY_PropGroup_Image():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e3690a87-0fa8-4a2a-9a9f-fce8827055ac}'), pid=100)
def PKEY_PropGroup_Media():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{61872cf7-6b5e-4b4b-ac2d-59da84459248}'), pid=100)
def PKEY_PropGroup_MediaAdvanced():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8859a284-de7e-4642-99ba-d431d044b1ec}'), pid=100)
def PKEY_PropGroup_Message():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7fd7259d-16b4-4135-9f97-7c96ecd2fa9e}'), pid=100)
def PKEY_PropGroup_Music():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{68dd6094-7216-40f1-a029-43fe7127043f}'), pid=100)
def PKEY_PropGroup_Origin():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2598d2fb-5569-4367-95df-5cd3a177e1a5}'), pid=100)
def PKEY_PropGroup_PhotoAdvanced():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0cb2bf5a-9ee7-4a86-8222-f01e07fdadaf}'), pid=100)
def PKEY_PropGroup_RecordedTV():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e7b33238-6584-4170-a5c0-ac25efd9da56}'), pid=100)
def PKEY_PropGroup_Video():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bebe0920-7671-4c54-a3eb-49fddfc191ee}'), pid=100)
def PKEY_InfoTipText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=17)
def PKEY_PropList_ConflictPrompt():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=11)
def PKEY_PropList_ContentViewModeForBrowse():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=13)
def PKEY_PropList_ContentViewModeForSearch():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=14)
def PKEY_PropList_ExtendedTileInfo():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=9)
def PKEY_PropList_FileOperationPrompt():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=10)
def PKEY_PropList_FullDetails():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=2)
def PKEY_PropList_InfoTip():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=4)
def PKEY_PropList_NonPersonal():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49d1091f-082e-493f-b23f-d2308aa9668c}'), pid=100)
def PKEY_PropList_PreviewDetails():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=8)
def PKEY_PropList_PreviewTitle():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=6)
def PKEY_PropList_QuickTip():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=5)
def PKEY_PropList_TileInfo():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{c9944a21-a406-48fe-8225-aec7e24c211b}'), pid=3)
def PKEY_PropList_XPDetailsPanel():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{f2275480-f782-4291-bd94-f13693513aec}'), pid=0)
def PKEY_RecordedTV_ChannelNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=7)
def PKEY_RecordedTV_Credits():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=4)
def PKEY_RecordedTV_DateContentExpires():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=15)
def PKEY_RecordedTV_EpisodeName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=2)
def PKEY_RecordedTV_IsATSCContent():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=16)
def PKEY_RecordedTV_IsClosedCaptioningAvailable():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=12)
def PKEY_RecordedTV_IsDTVContent():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=17)
def PKEY_RecordedTV_IsHDContent():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=18)
def PKEY_RecordedTV_IsRepeatBroadcast():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=13)
def PKEY_RecordedTV_IsSAP():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=14)
def PKEY_RecordedTV_NetworkAffiliation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2c53c813-fb63-4e22-a1ab-0b331ca1e273}'), pid=100)
def PKEY_RecordedTV_OriginalBroadcastDate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4684fe97-8765-4842-9c13-f006447b178c}'), pid=100)
def PKEY_RecordedTV_ProgramDescription():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=3)
def PKEY_RecordedTV_RecordingTime():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a5477f61-7a82-4eca-9dde-98b69b2479b3}'), pid=100)
def PKEY_RecordedTV_StationCallSign():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{6d748de2-8d38-4cc3-ac60-f009b057c557}'), pid=5)
def PKEY_RecordedTV_StationName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1b5439e7-eba1-4af8-bdd7-7af1d4549493}'), pid=100)
def PKEY_Search_AutoSummary():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{560c36c0-503a-11cf-baa1-00004c752a9a}'), pid=2)
def PKEY_Search_ContainerHash():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bceee283-35df-4d53-826a-f36a3eefc6be}'), pid=100)
def PKEY_Search_Contents():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=19)
def PKEY_Search_EntryID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49691c90-7e17-101a-a91c-08002b2ecda9}'), pid=5)
def PKEY_Search_ExtendedProperties():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7b03b546-fa4f-4a52-a2fe-03d5311e5865}'), pid=100)
def PKEY_Search_GatherTime():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0b63e350-9ccc-11d0-bcdb-00805fccce04}'), pid=8)
def PKEY_Search_HitCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49691c90-7e17-101a-a91c-08002b2ecda9}'), pid=4)
def PKEY_Search_IsClosedDirectory():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0b63e343-9ccc-11d0-bcdb-00805fccce04}'), pid=23)
def PKEY_Search_IsFullyContained():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0b63e343-9ccc-11d0-bcdb-00805fccce04}'), pid=24)
def PKEY_Search_QueryFocusedSummary():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{560c36c0-503a-11cf-baa1-00004c752a9a}'), pid=3)
def PKEY_Search_QueryFocusedSummaryWithFallback():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{560c36c0-503a-11cf-baa1-00004c752a9a}'), pid=4)
def PKEY_Search_QueryPropertyHits():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49691c90-7e17-101a-a91c-08002b2ecda9}'), pid=21)
def PKEY_Search_Rank():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{49691c90-7e17-101a-a91c-08002b2ecda9}'), pid=3)
def PKEY_Search_Store():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a06992b3-8caf-4ed7-a547-b259e32ac9fc}'), pid=100)
def PKEY_Search_UrlToIndex():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0b63e343-9ccc-11d0-bcdb-00805fccce04}'), pid=2)
def PKEY_Search_UrlToIndexWithModificationTime():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0b63e343-9ccc-11d0-bcdb-00805fccce04}'), pid=12)
def PKEY_Supplemental_Album():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0c73b141-39d6-4653-a683-cab291eaf95b}'), pid=6)
def PKEY_Supplemental_AlbumID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0c73b141-39d6-4653-a683-cab291eaf95b}'), pid=2)
def PKEY_Supplemental_Location():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0c73b141-39d6-4653-a683-cab291eaf95b}'), pid=5)
def PKEY_Supplemental_Person():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0c73b141-39d6-4653-a683-cab291eaf95b}'), pid=7)
def PKEY_Supplemental_ResourceId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0c73b141-39d6-4653-a683-cab291eaf95b}'), pid=3)
def PKEY_Supplemental_Tag():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0c73b141-39d6-4653-a683-cab291eaf95b}'), pid=4)
def PKEY_DescriptionID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=2)
def PKEY_InternalName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0cef7d53-fa64-11d1-a203-0000f81fedee}'), pid=5)
def PKEY_LibraryLocationsCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{908696c7-8f87-44f2-80ed-a8c1c6894575}'), pid=2)
def PKEY_Link_TargetSFGAOFlagsStrings():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d6942081-d53b-443d-ad47-5e059d9cd27a}'), pid=3)
def PKEY_Link_TargetUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5cbf2787-48cf-4208-b90e-ee5e5d420294}'), pid=2)
def PKEY_NamespaceCLSID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}'), pid=6)
def PKEY_Shell_SFGAOFlagsStrings():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d6942081-d53b-443d-ad47-5e059d9cd27a}'), pid=2)
SFGAOSTR_FILESYS: String = 'filesys'
SFGAOSTR_FILEANC: String = 'fileanc'
SFGAOSTR_STORAGEANC: String = 'storageanc'
SFGAOSTR_STREAM: String = 'stream'
SFGAOSTR_LINK: String = 'link'
SFGAOSTR_HIDDEN: String = 'hidden'
SFGAOSTR_SUPERHIDDEN: String = 'superhidden'
SFGAOSTR_FOLDER: String = 'folder'
SFGAOSTR_NONENUM: String = 'nonenum'
SFGAOSTR_BROWSABLE: String = 'browsable'
SFGAOSTR_SYSTEM: String = 'system'
SFGAOSTR_PLACEHOLDER: String = 'placeholder'
def PKEY_StatusBarSelectedItemCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{26dc287c-6e3d-4bd3-b2b0-6a26ba2e346d}'), pid=3)
def PKEY_StatusBarViewItemCount():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{26dc287c-6e3d-4bd3-b2b0-6a26ba2e346d}'), pid=2)
def PKEY_AppUserModel_ExcludeFromShowInNewInstall():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=8)
def PKEY_AppUserModel_ID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=5)
def PKEY_AppUserModel_IsDestListSeparator():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=6)
def PKEY_AppUserModel_IsDualMode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=11)
def PKEY_AppUserModel_PreventPinning():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=9)
def PKEY_AppUserModel_RelaunchCommand():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=2)
def PKEY_AppUserModel_RelaunchDisplayNameResource():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=4)
def PKEY_AppUserModel_RelaunchIconResource():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=3)
def PKEY_AppUserModel_SettingsCommand():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=38)
def PKEY_AppUserModel_StartPinOption():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=12)
APPUSERMODEL_STARTPINOPTION_DEFAULT: UInt32 = 0
APPUSERMODEL_STARTPINOPTION_NOPINONINSTALL: UInt32 = 1
APPUSERMODEL_STARTPINOPTION_USERPINNED: UInt32 = 2
def PKEY_AppUserModel_ToastActivatorCLSID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=26)
def PKEY_AppUserModel_UninstallCommand():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=37)
def PKEY_AppUserModel_VisualElementsManifestHintPath():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3}'), pid=31)
def PKEY_EdgeGesture_DisableTouchWhenFullscreen():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{32ce38b2-2c9a-41b1-9bc5-b3784394aa44}'), pid=2)
def PKEY_Software_DateLastUsed():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{841e4f90-ff59-4d16-8947-e81bbffab36d}'), pid=16)
def PKEY_Software_ProductName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{0cef7d53-fa64-11d1-a203-0000f81fedee}'), pid=7)
def PKEY_Sync_Comments():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7bd5533e-af15-44db-b8c8-bd6624e1d032}'), pid=13)
def PKEY_Sync_ConflictDescription():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ce50c159-2fb8-41fd-be68-d3e042e274bc}'), pid=4)
def PKEY_Sync_ConflictFirstLocation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ce50c159-2fb8-41fd-be68-d3e042e274bc}'), pid=6)
def PKEY_Sync_ConflictSecondLocation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ce50c159-2fb8-41fd-be68-d3e042e274bc}'), pid=7)
def PKEY_Sync_HandlerCollectionID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7bd5533e-af15-44db-b8c8-bd6624e1d032}'), pid=2)
def PKEY_Sync_HandlerID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7bd5533e-af15-44db-b8c8-bd6624e1d032}'), pid=3)
def PKEY_Sync_HandlerName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ce50c159-2fb8-41fd-be68-d3e042e274bc}'), pid=2)
def PKEY_Sync_HandlerType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7bd5533e-af15-44db-b8c8-bd6624e1d032}'), pid=8)
SYNC_HANDLERTYPE_OTHER: UInt32 = 0
SYNC_HANDLERTYPE_PROGRAMS: UInt32 = 1
SYNC_HANDLERTYPE_DEVICES: UInt32 = 2
SYNC_HANDLERTYPE_FOLDERS: UInt32 = 3
SYNC_HANDLERTYPE_WEBSERVICES: UInt32 = 4
SYNC_HANDLERTYPE_COMPUTERS: UInt32 = 5
def PKEY_Sync_HandlerTypeLabel():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7bd5533e-af15-44db-b8c8-bd6624e1d032}'), pid=9)
def PKEY_Sync_ItemID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7bd5533e-af15-44db-b8c8-bd6624e1d032}'), pid=6)
def PKEY_Sync_ItemName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{ce50c159-2fb8-41fd-be68-d3e042e274bc}'), pid=3)
def PKEY_Sync_ProgressPercentage():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7bd5533e-af15-44db-b8c8-bd6624e1d032}'), pid=23)
def PKEY_Sync_State():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7bd5533e-af15-44db-b8c8-bd6624e1d032}'), pid=24)
SYNC_STATE_NOTSETUP: UInt32 = 0
SYNC_STATE_SYNCNOTRUN: UInt32 = 1
SYNC_STATE_IDLE: UInt32 = 2
SYNC_STATE_ERROR: UInt32 = 3
SYNC_STATE_PENDING: UInt32 = 4
SYNC_STATE_SYNCING: UInt32 = 5
def PKEY_Sync_Status():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7bd5533e-af15-44db-b8c8-bd6624e1d032}'), pid=10)
def PKEY_Task_BillingInformation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d37d52c6-261c-4303-82b3-08b926ac6f12}'), pid=100)
def PKEY_Task_CompletionStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{084d8a0a-e6d5-40de-bf1f-c8820e7c877c}'), pid=100)
def PKEY_Task_Owner():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{08c7cc5f-60f2-4494-ad75-55e3e0b5add0}'), pid=100)
def PKEY_Video_Compression():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=10)
def PKEY_Video_Director():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440492-4c8b-11d1-8b70-080036b11a03}'), pid=20)
def PKEY_Video_EncodingBitrate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=8)
def PKEY_Video_FourCC():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=44)
def PKEY_Video_FrameHeight():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=4)
def PKEY_Video_FrameRate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=6)
def PKEY_Video_FrameWidth():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=3)
def PKEY_Video_HorizontalAspectRatio():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=42)
def PKEY_Video_IsSpherical():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=100)
def PKEY_Video_IsStereo():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=98)
def PKEY_Video_Orientation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=99)
def PKEY_Video_SampleSize():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=9)
def PKEY_Video_StreamName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=2)
def PKEY_Video_StreamNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=11)
def PKEY_Video_TotalBitrate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=43)
def PKEY_Video_TranscodedForSync():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=46)
def PKEY_Video_VerticalAspectRatio():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64440491-4c8b-11d1-8b70-080036b11a03}'), pid=45)
def PKEY_Volume_FileSystem():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9b174b35-40ff-11d2-a27e-00c04fc30871}'), pid=4)
def PKEY_Volume_IsMappedDrive():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{149c0b69-2c2d-48fc-808f-d318d78c4636}'), pid=2)
def PKEY_Volume_IsRoot():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{9b174b35-40ff-11d2-a27e-00c04fc30871}'), pid=10)
ACT_AUTHORIZE_ON_RESUME: UInt32 = 1
ACT_AUTHORIZE_ON_SESSION_UNLOCK: UInt32 = 2
ACT_UNAUTHORIZE_ON_SUSPEND: UInt32 = 1
ACT_UNAUTHORIZE_ON_SESSION_LOCK: UInt32 = 2
ES_RESERVED_COM_ERROR_START: UInt32 = 0
ES_RESERVED_COM_ERROR_END: UInt32 = 511
ES_GENERAL_ERROR_START: UInt32 = 512
ES_GENERAL_ERROR_END: UInt32 = 1023
ES_AUTHN_ERROR_START: UInt32 = 1024
ES_AUTHN_ERROR_END: UInt32 = 1279
ES_RESERVED_SILO_ERROR_START: UInt32 = 1280
ES_RESERVED_SILO_ERROR_END: UInt32 = 4095
ES_PW_SILO_ERROR_START: UInt32 = 4352
ES_PW_SILO_ERROR_END: UInt32 = 4607
ES_RESERVED_SILO_SPECIFIC_ERROR_START: UInt32 = 4608
ES_RESERVED_SILO_SPECIFIC_ERROR_END: UInt32 = 49151
ES_VENDOR_ERROR_START: UInt32 = 49152
ES_VENDOR_ERROR_END: UInt32 = 65535
FACILITY_ENHANCED_STORAGE: UInt32 = 4
ES_E_INVALID_RESPONSE: UInt32 = 3221488128
ES_E_UNPROVISIONED_HARDWARE: UInt32 = 3221488132
ES_E_UNSUPPORTED_HARDWARE: UInt32 = 3221488133
ES_E_INCOMPLETE_COMMAND: UInt32 = 3221488134
ES_E_BAD_SEQUENCE: UInt32 = 3221488135
ES_E_NO_PROBE: UInt32 = 3221488136
ES_E_INVALID_SILO: UInt32 = 3221488137
ES_E_INVALID_CAPABILITY: UInt32 = 3221488138
ES_E_GROUP_POLICY_FORBIDDEN_USE: UInt32 = 3221488139
ES_E_GROUP_POLICY_FORBIDDEN_OPERATION: UInt32 = 3221488140
ES_E_INVALID_PARAM_COMBINATION: UInt32 = 3221488141
ES_E_INVALID_PARAM_LENGTH: UInt32 = 3221488142
ES_E_INCONSISTENT_PARAM_LENGTH: UInt32 = 3221488143
ES_E_NO_AUTHENTICATION_REQUIRED: UInt32 = 3221488640
ES_E_INVALID_FIELD_IDENTIFIER: UInt32 = 3221491968
ES_E_CHALLENGE_MISMATCH: UInt32 = 3221491969
ES_E_CHALLENGE_SIZE_MISMATCH: UInt32 = 3221491970
ES_E_FRIENDLY_NAME_TOO_LONG: UInt32 = 3221491971
ES_E_SILO_NAME_TOO_LONG: UInt32 = 3221491972
ES_E_PASSWORD_TOO_LONG: UInt32 = 3221491973
ES_E_PASSWORD_HINT_TOO_LONG: UInt32 = 3221491974
ES_E_OTHER_SECURITY_PROTOCOL_ACTIVE: UInt32 = 3221491975
ES_E_DEVICE_DIGEST_MISSING: UInt32 = 3221491976
ES_E_NOT_AUTHORIZED_UNEXPECTED: UInt32 = 3221491977
ES_E_AUTHORIZED_UNEXPECTED: UInt32 = 3221491978
ES_E_PROVISIONED_UNEXPECTED: UInt32 = 3221491979
ES_E_UNKNOWN_DIGEST_ALGORITHM: UInt32 = 3221491980
class ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION(EasyCastStructure):
    CurrentAdminFailures: Byte
    CurrentUserFailures: Byte
    TotalUserAuthenticationCount: UInt32
    TotalAdminAuthenticationCount: UInt32
    FipsCompliant: win32more.Windows.Win32.Foundation.BOOL
    SecurityIDAvailable: win32more.Windows.Win32.Foundation.BOOL
    InitializeInProgress: win32more.Windows.Win32.Foundation.BOOL
    ITMSArmed: win32more.Windows.Win32.Foundation.BOOL
    ITMSArmable: win32more.Windows.Win32.Foundation.BOOL
    UserCreated: win32more.Windows.Win32.Foundation.BOOL
    ResetOnPORDefault: win32more.Windows.Win32.Foundation.BOOL
    ResetOnPORCurrent: win32more.Windows.Win32.Foundation.BOOL
    MaxAdminFailures: Byte
    MaxUserFailures: Byte
    TimeToCompleteInitialization: UInt32
    TimeRemainingToCompleteInitialization: UInt32
    MinTimeToAuthenticate: UInt32
    MaxAdminPasswordSize: Byte
    MinAdminPasswordSize: Byte
    MaxAdminHintSize: Byte
    MaxUserPasswordSize: Byte
    MinUserPasswordSize: Byte
    MaxUserHintSize: Byte
    MaxUserNameSize: Byte
    MaxSiloNameSize: Byte
    MaxChallengeSize: UInt16
EnhancedStorageACT = Guid('{af076a15-2ece-4ad4-bb21-29f040e176d8}')
EnhancedStorageSilo = Guid('{cb25220c-76c7-4fee-842b-f3383cd022bc}')
EnhancedStorageSiloAction = Guid('{886d29dd-b506-466b-9fbf-b44ff383fb3f}')
EnumEnhancedStorageACT = Guid('{fe841493-835c-4fa3-b6cc-b4b2d4719848}')
class IEnhancedStorageACT(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6e7781f4-e0f2-4239-b976-a01abab52930}')
    @commethod(3)
    def Authorize(self, hwndParent: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unauthorize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAuthorizationState(self, pState: POINTER(win32more.Windows.Win32.Storage.EnhancedStorage.ACT_AUTHORIZATION_STATE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMatchingVolume(self, ppwszVolume: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUniqueIdentity(self, ppwszIdentity: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSilos(self, pppIEnhancedStorageSilos: POINTER(POINTER(win32more.Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageSilo_head)), pcEnhancedStorageSilos: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnhancedStorageACT2(ComPtr):
    extends: win32more.Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageACT
    _iid_ = Guid('{4da57d2e-8eb3-41f6-a07e-98b52b88242b}')
    @commethod(9)
    def GetDeviceName(self, ppwszDeviceName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsDeviceRemovable(self, pIsDeviceRemovable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnhancedStorageACT3(ComPtr):
    extends: win32more.Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageACT2
    _iid_ = Guid('{022150a1-113d-11df-bb61-001aa01bbc58}')
    @commethod(11)
    def UnauthorizeEx(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsQueueFrozen(self, pIsQueueFrozen: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetShellExtSupport(self, pShellExtSupport: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnhancedStorageSilo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5aef78c6-2242-4703-bf49-44b29357a359}')
    @commethod(3)
    def GetInfo(self, pSiloInfo: POINTER(win32more.Windows.Win32.Storage.EnhancedStorage.SILO_INFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetActions(self, pppIEnhancedStorageSiloActions: POINTER(POINTER(win32more.Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageSiloAction_head)), pcEnhancedStorageSiloActions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SendCommand(self, Command: Byte, pbCommandBuffer: POINTER(Byte), cbCommandBuffer: UInt32, pbResponseBuffer: POINTER(Byte), pcbResponseBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPortableDevice(self, ppIPortableDevice: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevice_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDevicePath(self, ppwszSiloDevicePath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnhancedStorageSiloAction(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b6f7f311-206f-4ff8-9c4b-27efee77a86f}')
    @commethod(3)
    def GetName(self, ppwszActionName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(self, ppwszActionDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Invoke(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumEnhancedStorageACT(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09b224bd-1335-4631-a7ff-cfd3a92646d7}')
    @commethod(3)
    def GetACTs(self, pppIEnhancedStorageACTs: POINTER(POINTER(win32more.Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageACT_head)), pcEnhancedStorageACTs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMatchingACT(self, szVolume: win32more.Windows.Win32.Foundation.PWSTR, ppIEnhancedStorageACT: POINTER(win32more.Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageACT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class SILO_INFO(EasyCastStructure):
    ulSTID: UInt32
    SpecificationMajor: Byte
    SpecificationMinor: Byte
    ImplementationMajor: Byte
    ImplementationMinor: Byte
    type: Byte
    capabilities: Byte
make_head(_module, 'ACT_AUTHORIZATION_STATE')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_SILO_IS_AUTHENTICATION_SILO')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_SILO_GET_AUTHENTICATION_STATE')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_SILO_ENUMERATE_SILOS')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_HOST_CERTIFICATE_AUTHENTICATION')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_DEVICE_CERTIFICATE_AUTHENTICATION')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_ADMIN_CERTIFICATE_AUTHENTICATION')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_INITIALIZE_TO_MANUFACTURER_STATE')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE_COUNT')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_SET_CERTIFICATE')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_CREATE_CERTIFICATE_REQUEST')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_UNAUTHENTICATION')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITY')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITIES')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_GET_ACT_FRIENDLY_NAME')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_GUID')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_PASSWORD_AUTHORIZE_ACT_ACCESS')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_PASSWORD_UNAUTHORIZE_ACT_ACCESS')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_PASSWORD_QUERY_INFORMATION')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_PASSWORD_CONFIG_ADMINISTRATOR')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_PASSWORD_CREATE_USER')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_PASSWORD_DELETE_USER')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_PASSWORD_CHANGE_PASSWORD')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_PASSWORD_INITIALIZE_USER_PASSWORD')
make_head(_module, 'ENHANCED_STORAGE_COMMAND_PASSWORD_START_INITIALIZE_TO_MANUFACTURER_STATE')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_AUTHENTICATION_STATE')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_IS_AUTHENTICATION_SILO')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_TEMPORARY_UNAUTHENTICATION')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_MAX_AUTH_FAILURES')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_PASSWORD')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_OLD_PASSWORD')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_PASSWORD_INDICATOR')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD_INDICATOR')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_USER_HINT')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_USER_NAME')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_ADMIN_HINT')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_SILO_NAME')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_SILO_FRIENDLYNAME_SPECIFIED')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_PASSWORD_SILO_INFO')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_SECURITY_IDENTIFIER')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_QUERY_SILO_TYPE')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_QUERY_SILO_RESULTS')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_MAX_CERTIFICATE_COUNT')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_STORED_CERTIFICATE_COUNT')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_CERTIFICATE_INDEX')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_CERTIFICATE_TYPE')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_VALIDATION_POLICY')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_INDEX')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_OF_TYPE_INDEX')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_CERTIFICATE_LENGTH')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_CERTIFICATE')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_CERTIFICATE_REQUEST')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_CERTIFICATE_CAPABILITY_TYPE')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITY')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITIES')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_CERTIFICATE_ACT_FRIENDLY_NAME')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_GUID')
make_head(_module, 'ENHANCED_STORAGE_PROPERTY_SIGNER_CERTIFICATE_INDEX')
make_head(_module, 'ENHANCED_STORAGE_CAPABILITY_HASH_ALGS')
make_head(_module, 'ENHANCED_STORAGE_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY')
make_head(_module, 'ENHANCED_STORAGE_CAPABILITY_SIGNING_ALGS')
make_head(_module, 'ENHANCED_STORAGE_CAPABILITY_RENDER_USER_DATA_UNUSABLE')
make_head(_module, 'ENHANCED_STORAGE_CAPABILITY_CERTIFICATE_EXTENSION_PARSING')
make_head(_module, 'PKEY_Address_Country')
make_head(_module, 'PKEY_Address_CountryCode')
make_head(_module, 'PKEY_Address_Region')
make_head(_module, 'PKEY_Address_RegionCode')
make_head(_module, 'PKEY_Address_Town')
make_head(_module, 'PKEY_Audio_ChannelCount')
make_head(_module, 'PKEY_Audio_Compression')
make_head(_module, 'PKEY_Audio_EncodingBitrate')
make_head(_module, 'PKEY_Audio_Format')
make_head(_module, 'PKEY_Audio_IsVariableBitRate')
make_head(_module, 'PKEY_Audio_PeakValue')
make_head(_module, 'PKEY_Audio_SampleRate')
make_head(_module, 'PKEY_Audio_SampleSize')
make_head(_module, 'PKEY_Audio_StreamName')
make_head(_module, 'PKEY_Audio_StreamNumber')
make_head(_module, 'PKEY_Calendar_Duration')
make_head(_module, 'PKEY_Calendar_IsOnline')
make_head(_module, 'PKEY_Calendar_IsRecurring')
make_head(_module, 'PKEY_Calendar_Location')
make_head(_module, 'PKEY_Calendar_OptionalAttendeeAddresses')
make_head(_module, 'PKEY_Calendar_OptionalAttendeeNames')
make_head(_module, 'PKEY_Calendar_OrganizerAddress')
make_head(_module, 'PKEY_Calendar_OrganizerName')
make_head(_module, 'PKEY_Calendar_ReminderTime')
make_head(_module, 'PKEY_Calendar_RequiredAttendeeAddresses')
make_head(_module, 'PKEY_Calendar_RequiredAttendeeNames')
make_head(_module, 'PKEY_Calendar_Resources')
make_head(_module, 'PKEY_Calendar_ResponseStatus')
make_head(_module, 'PKEY_Calendar_ShowTimeAs')
make_head(_module, 'PKEY_Calendar_ShowTimeAsText')
make_head(_module, 'PKEY_Communication_AccountName')
make_head(_module, 'PKEY_Communication_DateItemExpires')
make_head(_module, 'PKEY_Communication_Direction')
make_head(_module, 'PKEY_Communication_FollowupIconIndex')
make_head(_module, 'PKEY_Communication_HeaderItem')
make_head(_module, 'PKEY_Communication_PolicyTag')
make_head(_module, 'PKEY_Communication_SecurityFlags')
make_head(_module, 'PKEY_Communication_Suffix')
make_head(_module, 'PKEY_Communication_TaskStatus')
make_head(_module, 'PKEY_Communication_TaskStatusText')
make_head(_module, 'PKEY_Computer_DecoratedFreeSpace')
make_head(_module, 'PKEY_Contact_AccountPictureDynamicVideo')
make_head(_module, 'PKEY_Contact_AccountPictureLarge')
make_head(_module, 'PKEY_Contact_AccountPictureSmall')
make_head(_module, 'PKEY_Contact_Anniversary')
make_head(_module, 'PKEY_Contact_AssistantName')
make_head(_module, 'PKEY_Contact_AssistantTelephone')
make_head(_module, 'PKEY_Contact_Birthday')
make_head(_module, 'PKEY_Contact_BusinessAddress')
make_head(_module, 'PKEY_Contact_BusinessAddress1Country')
make_head(_module, 'PKEY_Contact_BusinessAddress1Locality')
make_head(_module, 'PKEY_Contact_BusinessAddress1PostalCode')
make_head(_module, 'PKEY_Contact_BusinessAddress1Region')
make_head(_module, 'PKEY_Contact_BusinessAddress1Street')
make_head(_module, 'PKEY_Contact_BusinessAddress2Country')
make_head(_module, 'PKEY_Contact_BusinessAddress2Locality')
make_head(_module, 'PKEY_Contact_BusinessAddress2PostalCode')
make_head(_module, 'PKEY_Contact_BusinessAddress2Region')
make_head(_module, 'PKEY_Contact_BusinessAddress2Street')
make_head(_module, 'PKEY_Contact_BusinessAddress3Country')
make_head(_module, 'PKEY_Contact_BusinessAddress3Locality')
make_head(_module, 'PKEY_Contact_BusinessAddress3PostalCode')
make_head(_module, 'PKEY_Contact_BusinessAddress3Region')
make_head(_module, 'PKEY_Contact_BusinessAddress3Street')
make_head(_module, 'PKEY_Contact_BusinessAddressCity')
make_head(_module, 'PKEY_Contact_BusinessAddressCountry')
make_head(_module, 'PKEY_Contact_BusinessAddressPostalCode')
make_head(_module, 'PKEY_Contact_BusinessAddressPostOfficeBox')
make_head(_module, 'PKEY_Contact_BusinessAddressState')
make_head(_module, 'PKEY_Contact_BusinessAddressStreet')
make_head(_module, 'PKEY_Contact_BusinessEmailAddresses')
make_head(_module, 'PKEY_Contact_BusinessFaxNumber')
make_head(_module, 'PKEY_Contact_BusinessHomePage')
make_head(_module, 'PKEY_Contact_BusinessTelephone')
make_head(_module, 'PKEY_Contact_CallbackTelephone')
make_head(_module, 'PKEY_Contact_CarTelephone')
make_head(_module, 'PKEY_Contact_Children')
make_head(_module, 'PKEY_Contact_CompanyMainTelephone')
make_head(_module, 'PKEY_Contact_ConnectedServiceDisplayName')
make_head(_module, 'PKEY_Contact_ConnectedServiceIdentities')
make_head(_module, 'PKEY_Contact_ConnectedServiceName')
make_head(_module, 'PKEY_Contact_ConnectedServiceSupportedActions')
make_head(_module, 'PKEY_Contact_DataSuppliers')
make_head(_module, 'PKEY_Contact_Department')
make_head(_module, 'PKEY_Contact_DisplayBusinessPhoneNumbers')
make_head(_module, 'PKEY_Contact_DisplayHomePhoneNumbers')
make_head(_module, 'PKEY_Contact_DisplayMobilePhoneNumbers')
make_head(_module, 'PKEY_Contact_DisplayOtherPhoneNumbers')
make_head(_module, 'PKEY_Contact_EmailAddress')
make_head(_module, 'PKEY_Contact_EmailAddress2')
make_head(_module, 'PKEY_Contact_EmailAddress3')
make_head(_module, 'PKEY_Contact_EmailAddresses')
make_head(_module, 'PKEY_Contact_EmailName')
make_head(_module, 'PKEY_Contact_FileAsName')
make_head(_module, 'PKEY_Contact_FirstName')
make_head(_module, 'PKEY_Contact_FullName')
make_head(_module, 'PKEY_Contact_Gender')
make_head(_module, 'PKEY_Contact_GenderValue')
make_head(_module, 'PKEY_Contact_Hobbies')
make_head(_module, 'PKEY_Contact_HomeAddress')
make_head(_module, 'PKEY_Contact_HomeAddress1Country')
make_head(_module, 'PKEY_Contact_HomeAddress1Locality')
make_head(_module, 'PKEY_Contact_HomeAddress1PostalCode')
make_head(_module, 'PKEY_Contact_HomeAddress1Region')
make_head(_module, 'PKEY_Contact_HomeAddress1Street')
make_head(_module, 'PKEY_Contact_HomeAddress2Country')
make_head(_module, 'PKEY_Contact_HomeAddress2Locality')
make_head(_module, 'PKEY_Contact_HomeAddress2PostalCode')
make_head(_module, 'PKEY_Contact_HomeAddress2Region')
make_head(_module, 'PKEY_Contact_HomeAddress2Street')
make_head(_module, 'PKEY_Contact_HomeAddress3Country')
make_head(_module, 'PKEY_Contact_HomeAddress3Locality')
make_head(_module, 'PKEY_Contact_HomeAddress3PostalCode')
make_head(_module, 'PKEY_Contact_HomeAddress3Region')
make_head(_module, 'PKEY_Contact_HomeAddress3Street')
make_head(_module, 'PKEY_Contact_HomeAddressCity')
make_head(_module, 'PKEY_Contact_HomeAddressCountry')
make_head(_module, 'PKEY_Contact_HomeAddressPostalCode')
make_head(_module, 'PKEY_Contact_HomeAddressPostOfficeBox')
make_head(_module, 'PKEY_Contact_HomeAddressState')
make_head(_module, 'PKEY_Contact_HomeAddressStreet')
make_head(_module, 'PKEY_Contact_HomeEmailAddresses')
make_head(_module, 'PKEY_Contact_HomeFaxNumber')
make_head(_module, 'PKEY_Contact_HomeTelephone')
make_head(_module, 'PKEY_Contact_IMAddress')
make_head(_module, 'PKEY_Contact_Initials')
make_head(_module, 'PKEY_Contact_JA_CompanyNamePhonetic')
make_head(_module, 'PKEY_Contact_JA_FirstNamePhonetic')
make_head(_module, 'PKEY_Contact_JA_LastNamePhonetic')
make_head(_module, 'PKEY_Contact_JobInfo1CompanyAddress')
make_head(_module, 'PKEY_Contact_JobInfo1CompanyName')
make_head(_module, 'PKEY_Contact_JobInfo1Department')
make_head(_module, 'PKEY_Contact_JobInfo1Manager')
make_head(_module, 'PKEY_Contact_JobInfo1OfficeLocation')
make_head(_module, 'PKEY_Contact_JobInfo1Title')
make_head(_module, 'PKEY_Contact_JobInfo1YomiCompanyName')
make_head(_module, 'PKEY_Contact_JobInfo2CompanyAddress')
make_head(_module, 'PKEY_Contact_JobInfo2CompanyName')
make_head(_module, 'PKEY_Contact_JobInfo2Department')
make_head(_module, 'PKEY_Contact_JobInfo2Manager')
make_head(_module, 'PKEY_Contact_JobInfo2OfficeLocation')
make_head(_module, 'PKEY_Contact_JobInfo2Title')
make_head(_module, 'PKEY_Contact_JobInfo2YomiCompanyName')
make_head(_module, 'PKEY_Contact_JobInfo3CompanyAddress')
make_head(_module, 'PKEY_Contact_JobInfo3CompanyName')
make_head(_module, 'PKEY_Contact_JobInfo3Department')
make_head(_module, 'PKEY_Contact_JobInfo3Manager')
make_head(_module, 'PKEY_Contact_JobInfo3OfficeLocation')
make_head(_module, 'PKEY_Contact_JobInfo3Title')
make_head(_module, 'PKEY_Contact_JobInfo3YomiCompanyName')
make_head(_module, 'PKEY_Contact_JobTitle')
make_head(_module, 'PKEY_Contact_Label')
make_head(_module, 'PKEY_Contact_LastName')
make_head(_module, 'PKEY_Contact_MailingAddress')
make_head(_module, 'PKEY_Contact_MiddleName')
make_head(_module, 'PKEY_Contact_MobileTelephone')
make_head(_module, 'PKEY_Contact_NickName')
make_head(_module, 'PKEY_Contact_OfficeLocation')
make_head(_module, 'PKEY_Contact_OtherAddress')
make_head(_module, 'PKEY_Contact_OtherAddress1Country')
make_head(_module, 'PKEY_Contact_OtherAddress1Locality')
make_head(_module, 'PKEY_Contact_OtherAddress1PostalCode')
make_head(_module, 'PKEY_Contact_OtherAddress1Region')
make_head(_module, 'PKEY_Contact_OtherAddress1Street')
make_head(_module, 'PKEY_Contact_OtherAddress2Country')
make_head(_module, 'PKEY_Contact_OtherAddress2Locality')
make_head(_module, 'PKEY_Contact_OtherAddress2PostalCode')
make_head(_module, 'PKEY_Contact_OtherAddress2Region')
make_head(_module, 'PKEY_Contact_OtherAddress2Street')
make_head(_module, 'PKEY_Contact_OtherAddress3Country')
make_head(_module, 'PKEY_Contact_OtherAddress3Locality')
make_head(_module, 'PKEY_Contact_OtherAddress3PostalCode')
make_head(_module, 'PKEY_Contact_OtherAddress3Region')
make_head(_module, 'PKEY_Contact_OtherAddress3Street')
make_head(_module, 'PKEY_Contact_OtherAddressCity')
make_head(_module, 'PKEY_Contact_OtherAddressCountry')
make_head(_module, 'PKEY_Contact_OtherAddressPostalCode')
make_head(_module, 'PKEY_Contact_OtherAddressPostOfficeBox')
make_head(_module, 'PKEY_Contact_OtherAddressState')
make_head(_module, 'PKEY_Contact_OtherAddressStreet')
make_head(_module, 'PKEY_Contact_OtherEmailAddresses')
make_head(_module, 'PKEY_Contact_PagerTelephone')
make_head(_module, 'PKEY_Contact_PersonalTitle')
make_head(_module, 'PKEY_Contact_PhoneNumbersCanonical')
make_head(_module, 'PKEY_Contact_Prefix')
make_head(_module, 'PKEY_Contact_PrimaryAddressCity')
make_head(_module, 'PKEY_Contact_PrimaryAddressCountry')
make_head(_module, 'PKEY_Contact_PrimaryAddressPostalCode')
make_head(_module, 'PKEY_Contact_PrimaryAddressPostOfficeBox')
make_head(_module, 'PKEY_Contact_PrimaryAddressState')
make_head(_module, 'PKEY_Contact_PrimaryAddressStreet')
make_head(_module, 'PKEY_Contact_PrimaryEmailAddress')
make_head(_module, 'PKEY_Contact_PrimaryTelephone')
make_head(_module, 'PKEY_Contact_Profession')
make_head(_module, 'PKEY_Contact_SpouseName')
make_head(_module, 'PKEY_Contact_Suffix')
make_head(_module, 'PKEY_Contact_TelexNumber')
make_head(_module, 'PKEY_Contact_TTYTDDTelephone')
make_head(_module, 'PKEY_Contact_WebPage')
make_head(_module, 'PKEY_Contact_Webpage2')
make_head(_module, 'PKEY_Contact_Webpage3')
make_head(_module, 'PKEY_AcquisitionID')
make_head(_module, 'PKEY_ApplicationDefinedProperties')
make_head(_module, 'PKEY_ApplicationName')
make_head(_module, 'PKEY_AppZoneIdentifier')
make_head(_module, 'PKEY_Author')
make_head(_module, 'PKEY_CachedFileUpdaterContentIdForConflictResolution')
make_head(_module, 'PKEY_CachedFileUpdaterContentIdForStream')
make_head(_module, 'PKEY_Capacity')
make_head(_module, 'PKEY_Category')
make_head(_module, 'PKEY_Comment')
make_head(_module, 'PKEY_Company')
make_head(_module, 'PKEY_ComputerName')
make_head(_module, 'PKEY_ContainedItems')
make_head(_module, 'PKEY_ContentId')
make_head(_module, 'PKEY_ContentStatus')
make_head(_module, 'PKEY_ContentType')
make_head(_module, 'PKEY_ContentUri')
make_head(_module, 'PKEY_Copyright')
make_head(_module, 'PKEY_CreatorAppId')
make_head(_module, 'PKEY_CreatorOpenWithUIOptions')
make_head(_module, 'PKEY_DataObjectFormat')
make_head(_module, 'PKEY_DateAccessed')
make_head(_module, 'PKEY_DateAcquired')
make_head(_module, 'PKEY_DateArchived')
make_head(_module, 'PKEY_DateCompleted')
make_head(_module, 'PKEY_DateCreated')
make_head(_module, 'PKEY_DateImported')
make_head(_module, 'PKEY_DateModified')
make_head(_module, 'PKEY_DefaultSaveLocationDisplay')
make_head(_module, 'PKEY_DueDate')
make_head(_module, 'PKEY_EndDate')
make_head(_module, 'PKEY_ExpandoProperties')
make_head(_module, 'PKEY_FileAllocationSize')
make_head(_module, 'PKEY_FileAttributes')
make_head(_module, 'PKEY_FileCount')
make_head(_module, 'PKEY_FileDescription')
make_head(_module, 'PKEY_FileExtension')
make_head(_module, 'PKEY_FileFRN')
make_head(_module, 'PKEY_FileName')
make_head(_module, 'PKEY_FileOfflineAvailabilityStatus')
make_head(_module, 'PKEY_FileOwner')
make_head(_module, 'PKEY_FilePlaceholderStatus')
make_head(_module, 'PKEY_FileVersion')
make_head(_module, 'PKEY_FindData')
make_head(_module, 'PKEY_FlagColor')
make_head(_module, 'PKEY_FlagColorText')
make_head(_module, 'PKEY_FlagStatus')
make_head(_module, 'PKEY_FlagStatusText')
make_head(_module, 'PKEY_FolderKind')
make_head(_module, 'PKEY_FolderNameDisplay')
make_head(_module, 'PKEY_FreeSpace')
make_head(_module, 'PKEY_FullText')
make_head(_module, 'PKEY_HighKeywords')
make_head(_module, 'PKEY_Identity')
make_head(_module, 'PKEY_Identity_Blob')
make_head(_module, 'PKEY_Identity_DisplayName')
make_head(_module, 'PKEY_Identity_InternetSid')
make_head(_module, 'PKEY_Identity_IsMeIdentity')
make_head(_module, 'PKEY_Identity_KeyProviderContext')
make_head(_module, 'PKEY_Identity_KeyProviderName')
make_head(_module, 'PKEY_Identity_LogonStatusString')
make_head(_module, 'PKEY_Identity_PrimaryEmailAddress')
make_head(_module, 'PKEY_Identity_PrimarySid')
make_head(_module, 'PKEY_Identity_ProviderData')
make_head(_module, 'PKEY_Identity_ProviderID')
make_head(_module, 'PKEY_Identity_QualifiedUserName')
make_head(_module, 'PKEY_Identity_UniqueID')
make_head(_module, 'PKEY_Identity_UserName')
make_head(_module, 'PKEY_IdentityProvider_Name')
make_head(_module, 'PKEY_IdentityProvider_Picture')
make_head(_module, 'PKEY_ImageParsingName')
make_head(_module, 'PKEY_Importance')
make_head(_module, 'PKEY_ImportanceText')
make_head(_module, 'PKEY_IsAttachment')
make_head(_module, 'PKEY_IsDefaultNonOwnerSaveLocation')
make_head(_module, 'PKEY_IsDefaultSaveLocation')
make_head(_module, 'PKEY_IsDeleted')
make_head(_module, 'PKEY_IsEncrypted')
make_head(_module, 'PKEY_IsFlagged')
make_head(_module, 'PKEY_IsFlaggedComplete')
make_head(_module, 'PKEY_IsIncomplete')
make_head(_module, 'PKEY_IsLocationSupported')
make_head(_module, 'PKEY_IsPinnedToNameSpaceTree')
make_head(_module, 'PKEY_IsRead')
make_head(_module, 'PKEY_IsSearchOnlyItem')
make_head(_module, 'PKEY_IsSendToTarget')
make_head(_module, 'PKEY_IsShared')
make_head(_module, 'PKEY_ItemAuthors')
make_head(_module, 'PKEY_ItemClassType')
make_head(_module, 'PKEY_ItemDate')
make_head(_module, 'PKEY_ItemFolderNameDisplay')
make_head(_module, 'PKEY_ItemFolderPathDisplay')
make_head(_module, 'PKEY_ItemFolderPathDisplayNarrow')
make_head(_module, 'PKEY_ItemName')
make_head(_module, 'PKEY_ItemNameDisplay')
make_head(_module, 'PKEY_ItemNameDisplayWithoutExtension')
make_head(_module, 'PKEY_ItemNamePrefix')
make_head(_module, 'PKEY_ItemNameSortOverride')
make_head(_module, 'PKEY_ItemParticipants')
make_head(_module, 'PKEY_ItemPathDisplay')
make_head(_module, 'PKEY_ItemPathDisplayNarrow')
make_head(_module, 'PKEY_ItemSubType')
make_head(_module, 'PKEY_ItemType')
make_head(_module, 'PKEY_ItemTypeText')
make_head(_module, 'PKEY_ItemUrl')
make_head(_module, 'PKEY_Keywords')
make_head(_module, 'PKEY_Kind')
make_head(_module, 'PKEY_KindText')
make_head(_module, 'PKEY_Language')
make_head(_module, 'PKEY_LastSyncError')
make_head(_module, 'PKEY_LastSyncWarning')
make_head(_module, 'PKEY_LastWriterPackageFamilyName')
make_head(_module, 'PKEY_LowKeywords')
make_head(_module, 'PKEY_MediumKeywords')
make_head(_module, 'PKEY_MileageInformation')
make_head(_module, 'PKEY_MIMEType')
make_head(_module, 'PKEY_Null')
make_head(_module, 'PKEY_OfflineAvailability')
make_head(_module, 'PKEY_OfflineStatus')
make_head(_module, 'PKEY_OriginalFileName')
make_head(_module, 'PKEY_OwnerSID')
make_head(_module, 'PKEY_ParentalRating')
make_head(_module, 'PKEY_ParentalRatingReason')
make_head(_module, 'PKEY_ParentalRatingsOrganization')
make_head(_module, 'PKEY_ParsingBindContext')
make_head(_module, 'PKEY_ParsingName')
make_head(_module, 'PKEY_ParsingPath')
make_head(_module, 'PKEY_PerceivedType')
make_head(_module, 'PKEY_PercentFull')
make_head(_module, 'PKEY_Priority')
make_head(_module, 'PKEY_PriorityText')
make_head(_module, 'PKEY_Project')
make_head(_module, 'PKEY_ProviderItemID')
make_head(_module, 'PKEY_Rating')
make_head(_module, 'PKEY_RatingText')
make_head(_module, 'PKEY_RemoteConflictingFile')
make_head(_module, 'PKEY_Security_AllowedEnterpriseDataProtectionIdentities')
make_head(_module, 'PKEY_Security_EncryptionOwners')
make_head(_module, 'PKEY_Security_EncryptionOwnersDisplay')
make_head(_module, 'PKEY_Sensitivity')
make_head(_module, 'PKEY_SensitivityText')
make_head(_module, 'PKEY_SFGAOFlags')
make_head(_module, 'PKEY_SharedWith')
make_head(_module, 'PKEY_ShareUserRating')
make_head(_module, 'PKEY_SharingStatus')
make_head(_module, 'PKEY_Shell_OmitFromView')
make_head(_module, 'PKEY_SimpleRating')
make_head(_module, 'PKEY_Size')
make_head(_module, 'PKEY_SoftwareUsed')
make_head(_module, 'PKEY_SourceItem')
make_head(_module, 'PKEY_SourcePackageFamilyName')
make_head(_module, 'PKEY_StartDate')
make_head(_module, 'PKEY_Status')
make_head(_module, 'PKEY_StorageProviderCallerVersionInformation')
make_head(_module, 'PKEY_StorageProviderError')
make_head(_module, 'PKEY_StorageProviderFileChecksum')
make_head(_module, 'PKEY_StorageProviderFileFlags')
make_head(_module, 'PKEY_StorageProviderFileHasConflict')
make_head(_module, 'PKEY_StorageProviderFileIdentifier')
make_head(_module, 'PKEY_StorageProviderFileRemoteUri')
make_head(_module, 'PKEY_StorageProviderFileVersion')
make_head(_module, 'PKEY_StorageProviderFileVersionWaterline')
make_head(_module, 'PKEY_StorageProviderId')
make_head(_module, 'PKEY_StorageProviderShareStatuses')
make_head(_module, 'PKEY_StorageProviderSharingStatus')
make_head(_module, 'PKEY_StorageProviderStatus')
make_head(_module, 'PKEY_Subject')
make_head(_module, 'PKEY_SyncTransferStatus')
make_head(_module, 'PKEY_Thumbnail')
make_head(_module, 'PKEY_ThumbnailCacheId')
make_head(_module, 'PKEY_ThumbnailStream')
make_head(_module, 'PKEY_Title')
make_head(_module, 'PKEY_TitleSortOverride')
make_head(_module, 'PKEY_TotalFileSize')
make_head(_module, 'PKEY_Trademarks')
make_head(_module, 'PKEY_TransferOrder')
make_head(_module, 'PKEY_TransferPosition')
make_head(_module, 'PKEY_TransferSize')
make_head(_module, 'PKEY_VolumeId')
make_head(_module, 'PKEY_ZoneIdentifier')
make_head(_module, 'PKEY_Device_PrinterURL')
make_head(_module, 'PKEY_DeviceInterface_Bluetooth_DeviceAddress')
make_head(_module, 'PKEY_DeviceInterface_Bluetooth_Flags')
make_head(_module, 'PKEY_DeviceInterface_Bluetooth_LastConnectedTime')
make_head(_module, 'PKEY_DeviceInterface_Bluetooth_Manufacturer')
make_head(_module, 'PKEY_DeviceInterface_Bluetooth_ModelNumber')
make_head(_module, 'PKEY_DeviceInterface_Bluetooth_ProductId')
make_head(_module, 'PKEY_DeviceInterface_Bluetooth_ProductVersion')
make_head(_module, 'PKEY_DeviceInterface_Bluetooth_ServiceGuid')
make_head(_module, 'PKEY_DeviceInterface_Bluetooth_VendorId')
make_head(_module, 'PKEY_DeviceInterface_Bluetooth_VendorIdSource')
make_head(_module, 'PKEY_DeviceInterface_Hid_IsReadOnly')
make_head(_module, 'PKEY_DeviceInterface_Hid_ProductId')
make_head(_module, 'PKEY_DeviceInterface_Hid_UsageId')
make_head(_module, 'PKEY_DeviceInterface_Hid_UsagePage')
make_head(_module, 'PKEY_DeviceInterface_Hid_VendorId')
make_head(_module, 'PKEY_DeviceInterface_Hid_VersionNumber')
make_head(_module, 'PKEY_DeviceInterface_PrinterDriverDirectory')
make_head(_module, 'PKEY_DeviceInterface_PrinterDriverName')
make_head(_module, 'PKEY_DeviceInterface_PrinterEnumerationFlag')
make_head(_module, 'PKEY_DeviceInterface_PrinterName')
make_head(_module, 'PKEY_DeviceInterface_PrinterPortName')
make_head(_module, 'PKEY_DeviceInterface_Proximity_SupportsNfc')
make_head(_module, 'PKEY_DeviceInterface_Serial_PortName')
make_head(_module, 'PKEY_DeviceInterface_Serial_UsbProductId')
make_head(_module, 'PKEY_DeviceInterface_Serial_UsbVendorId')
make_head(_module, 'PKEY_DeviceInterface_WinUsb_DeviceInterfaceClasses')
make_head(_module, 'PKEY_DeviceInterface_WinUsb_UsbClass')
make_head(_module, 'PKEY_DeviceInterface_WinUsb_UsbProductId')
make_head(_module, 'PKEY_DeviceInterface_WinUsb_UsbProtocol')
make_head(_module, 'PKEY_DeviceInterface_WinUsb_UsbSubClass')
make_head(_module, 'PKEY_DeviceInterface_WinUsb_UsbVendorId')
make_head(_module, 'PKEY_Devices_Aep_AepId')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Cod_Major')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Cod_Minor')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Cod_Services_Audio')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Cod_Services_Capturing')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Cod_Services_Information')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Cod_Services_LimitedDiscovery')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Cod_Services_Networking')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Cod_Services_ObjectXfer')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Cod_Services_Positioning')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Cod_Services_Rendering')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Cod_Services_Telephony')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_LastSeenTime')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Le_AddressType')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Le_Appearance')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Le_Appearance_Category')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Le_Appearance_Subcategory')
make_head(_module, 'PKEY_Devices_Aep_Bluetooth_Le_IsConnectable')
make_head(_module, 'PKEY_Devices_Aep_CanPair')
make_head(_module, 'PKEY_Devices_Aep_Category')
make_head(_module, 'PKEY_Devices_Aep_ContainerId')
make_head(_module, 'PKEY_Devices_Aep_DeviceAddress')
make_head(_module, 'PKEY_Devices_Aep_IsConnected')
make_head(_module, 'PKEY_Devices_Aep_IsPaired')
make_head(_module, 'PKEY_Devices_Aep_IsPresent')
make_head(_module, 'PKEY_Devices_Aep_Manufacturer')
make_head(_module, 'PKEY_Devices_Aep_ModelId')
make_head(_module, 'PKEY_Devices_Aep_ModelName')
make_head(_module, 'PKEY_Devices_Aep_PointOfService_ConnectionTypes')
make_head(_module, 'PKEY_Devices_Aep_ProtocolId')
make_head(_module, 'PKEY_Devices_Aep_SignalStrength')
make_head(_module, 'PKEY_Devices_AepContainer_CanPair')
make_head(_module, 'PKEY_Devices_AepContainer_Categories')
make_head(_module, 'PKEY_Devices_AepContainer_Children')
make_head(_module, 'PKEY_Devices_AepContainer_ContainerId')
make_head(_module, 'PKEY_Devices_AepContainer_DialProtocol_InstalledApplications')
make_head(_module, 'PKEY_Devices_AepContainer_IsPaired')
make_head(_module, 'PKEY_Devices_AepContainer_IsPresent')
make_head(_module, 'PKEY_Devices_AepContainer_Manufacturer')
make_head(_module, 'PKEY_Devices_AepContainer_ModelIds')
make_head(_module, 'PKEY_Devices_AepContainer_ModelName')
make_head(_module, 'PKEY_Devices_AepContainer_ProtocolIds')
make_head(_module, 'PKEY_Devices_AepContainer_SupportedUriSchemes')
make_head(_module, 'PKEY_Devices_AepContainer_SupportsAudio')
make_head(_module, 'PKEY_Devices_AepContainer_SupportsCapturing')
make_head(_module, 'PKEY_Devices_AepContainer_SupportsImages')
make_head(_module, 'PKEY_Devices_AepContainer_SupportsInformation')
make_head(_module, 'PKEY_Devices_AepContainer_SupportsLimitedDiscovery')
make_head(_module, 'PKEY_Devices_AepContainer_SupportsNetworking')
make_head(_module, 'PKEY_Devices_AepContainer_SupportsObjectTransfer')
make_head(_module, 'PKEY_Devices_AepContainer_SupportsPositioning')
make_head(_module, 'PKEY_Devices_AepContainer_SupportsRendering')
make_head(_module, 'PKEY_Devices_AepContainer_SupportsTelephony')
make_head(_module, 'PKEY_Devices_AepContainer_SupportsVideo')
make_head(_module, 'PKEY_Devices_AepService_AepId')
make_head(_module, 'PKEY_Devices_AepService_Bluetooth_CacheMode')
make_head(_module, 'PKEY_Devices_AepService_Bluetooth_ServiceGuid')
make_head(_module, 'PKEY_Devices_AepService_Bluetooth_TargetDevice')
make_head(_module, 'PKEY_Devices_AepService_ContainerId')
make_head(_module, 'PKEY_Devices_AepService_FriendlyName')
make_head(_module, 'PKEY_Devices_AepService_IoT_ServiceInterfaces')
make_head(_module, 'PKEY_Devices_AepService_ParentAepIsPaired')
make_head(_module, 'PKEY_Devices_AepService_ProtocolId')
make_head(_module, 'PKEY_Devices_AepService_ServiceClassId')
make_head(_module, 'PKEY_Devices_AepService_ServiceId')
make_head(_module, 'PKEY_Devices_AppPackageFamilyName')
make_head(_module, 'PKEY_Devices_AudioDevice_Microphone_IsFarField')
make_head(_module, 'PKEY_Devices_AudioDevice_Microphone_SensitivityInDbfs')
make_head(_module, 'PKEY_Devices_AudioDevice_Microphone_SensitivityInDbfs2')
make_head(_module, 'PKEY_Devices_AudioDevice_Microphone_SignalToNoiseRatioInDb')
make_head(_module, 'PKEY_Devices_AudioDevice_RawProcessingSupported')
make_head(_module, 'PKEY_Devices_AudioDevice_SpeechProcessingSupported')
make_head(_module, 'PKEY_Devices_BatteryLife')
make_head(_module, 'PKEY_Devices_BatteryPlusCharging')
make_head(_module, 'PKEY_Devices_BatteryPlusChargingText')
make_head(_module, 'PKEY_Devices_Category')
make_head(_module, 'PKEY_Devices_CategoryGroup')
make_head(_module, 'PKEY_Devices_CategoryIds')
make_head(_module, 'PKEY_Devices_CategoryPlural')
make_head(_module, 'PKEY_Devices_ChallengeAep')
make_head(_module, 'PKEY_Devices_ChargingState')
make_head(_module, 'PKEY_Devices_Children')
make_head(_module, 'PKEY_Devices_ClassGuid')
make_head(_module, 'PKEY_Devices_CompatibleIds')
make_head(_module, 'PKEY_Devices_Connected')
make_head(_module, 'PKEY_Devices_ContainerId')
make_head(_module, 'PKEY_Devices_DefaultTooltip')
make_head(_module, 'PKEY_Devices_DeviceCapabilities')
make_head(_module, 'PKEY_Devices_DeviceCharacteristics')
make_head(_module, 'PKEY_Devices_DeviceDescription1')
make_head(_module, 'PKEY_Devices_DeviceDescription2')
make_head(_module, 'PKEY_Devices_DeviceHasProblem')
make_head(_module, 'PKEY_Devices_DeviceInstanceId')
make_head(_module, 'PKEY_Devices_DeviceManufacturer')
make_head(_module, 'PKEY_Devices_DevObjectType')
make_head(_module, 'PKEY_Devices_DialProtocol_InstalledApplications')
make_head(_module, 'PKEY_Devices_DiscoveryMethod')
make_head(_module, 'PKEY_Devices_Dnssd_Domain')
make_head(_module, 'PKEY_Devices_Dnssd_FullName')
make_head(_module, 'PKEY_Devices_Dnssd_HostName')
make_head(_module, 'PKEY_Devices_Dnssd_InstanceName')
make_head(_module, 'PKEY_Devices_Dnssd_NetworkAdapterId')
make_head(_module, 'PKEY_Devices_Dnssd_PortNumber')
make_head(_module, 'PKEY_Devices_Dnssd_Priority')
make_head(_module, 'PKEY_Devices_Dnssd_ServiceName')
make_head(_module, 'PKEY_Devices_Dnssd_TextAttributes')
make_head(_module, 'PKEY_Devices_Dnssd_Ttl')
make_head(_module, 'PKEY_Devices_Dnssd_Weight')
make_head(_module, 'PKEY_Devices_FriendlyName')
make_head(_module, 'PKEY_Devices_FunctionPaths')
make_head(_module, 'PKEY_Devices_GlyphIcon')
make_head(_module, 'PKEY_Devices_HardwareIds')
make_head(_module, 'PKEY_Devices_Icon')
make_head(_module, 'PKEY_Devices_InLocalMachineContainer')
make_head(_module, 'PKEY_Devices_InterfaceClassGuid')
make_head(_module, 'PKEY_Devices_InterfaceEnabled')
make_head(_module, 'PKEY_Devices_InterfacePaths')
make_head(_module, 'PKEY_Devices_IpAddress')
make_head(_module, 'PKEY_Devices_IsDefault')
make_head(_module, 'PKEY_Devices_IsNetworkConnected')
make_head(_module, 'PKEY_Devices_IsShared')
make_head(_module, 'PKEY_Devices_IsSoftwareInstalling')
make_head(_module, 'PKEY_Devices_LaunchDeviceStageFromExplorer')
make_head(_module, 'PKEY_Devices_LocalMachine')
make_head(_module, 'PKEY_Devices_LocationPaths')
make_head(_module, 'PKEY_Devices_Manufacturer')
make_head(_module, 'PKEY_Devices_MetadataPath')
make_head(_module, 'PKEY_Devices_MicrophoneArray_Geometry')
make_head(_module, 'PKEY_Devices_MissedCalls')
make_head(_module, 'PKEY_Devices_ModelId')
make_head(_module, 'PKEY_Devices_ModelName')
make_head(_module, 'PKEY_Devices_ModelNumber')
make_head(_module, 'PKEY_Devices_NetworkedTooltip')
make_head(_module, 'PKEY_Devices_NetworkName')
make_head(_module, 'PKEY_Devices_NetworkType')
make_head(_module, 'PKEY_Devices_NewPictures')
make_head(_module, 'PKEY_Devices_Notification')
make_head(_module, 'PKEY_Devices_Notifications_LowBattery')
make_head(_module, 'PKEY_Devices_Notifications_MissedCall')
make_head(_module, 'PKEY_Devices_Notifications_NewMessage')
make_head(_module, 'PKEY_Devices_Notifications_NewVoicemail')
make_head(_module, 'PKEY_Devices_Notifications_StorageFull')
make_head(_module, 'PKEY_Devices_Notifications_StorageFullLinkText')
make_head(_module, 'PKEY_Devices_NotificationStore')
make_head(_module, 'PKEY_Devices_NotWorkingProperly')
make_head(_module, 'PKEY_Devices_Paired')
make_head(_module, 'PKEY_Devices_Panel_PanelGroup')
make_head(_module, 'PKEY_Devices_Panel_PanelId')
make_head(_module, 'PKEY_Devices_Parent')
make_head(_module, 'PKEY_Devices_PhoneLineTransportDevice_Connected')
make_head(_module, 'PKEY_Devices_PhysicalDeviceLocation')
make_head(_module, 'PKEY_Devices_PlaybackPositionPercent')
make_head(_module, 'PKEY_Devices_PlaybackState')
make_head(_module, 'PKEY_Devices_PlaybackTitle')
make_head(_module, 'PKEY_Devices_Present')
make_head(_module, 'PKEY_Devices_PresentationUrl')
make_head(_module, 'PKEY_Devices_PrimaryCategory')
make_head(_module, 'PKEY_Devices_RemainingDuration')
make_head(_module, 'PKEY_Devices_RestrictedInterface')
make_head(_module, 'PKEY_Devices_Roaming')
make_head(_module, 'PKEY_Devices_SafeRemovalRequired')
make_head(_module, 'PKEY_Devices_SchematicName')
make_head(_module, 'PKEY_Devices_ServiceAddress')
make_head(_module, 'PKEY_Devices_ServiceId')
make_head(_module, 'PKEY_Devices_SharedTooltip')
make_head(_module, 'PKEY_Devices_SignalStrength')
make_head(_module, 'PKEY_Devices_SmartCards_ReaderKind')
make_head(_module, 'PKEY_Devices_Status')
make_head(_module, 'PKEY_Devices_Status1')
make_head(_module, 'PKEY_Devices_Status2')
make_head(_module, 'PKEY_Devices_StorageCapacity')
make_head(_module, 'PKEY_Devices_StorageFreeSpace')
make_head(_module, 'PKEY_Devices_StorageFreeSpacePercent')
make_head(_module, 'PKEY_Devices_TextMessages')
make_head(_module, 'PKEY_Devices_Voicemail')
make_head(_module, 'PKEY_Devices_WiaDeviceType')
make_head(_module, 'PKEY_Devices_WiFi_InterfaceGuid')
make_head(_module, 'PKEY_Devices_WiFiDirect_DeviceAddress')
make_head(_module, 'PKEY_Devices_WiFiDirect_GroupId')
make_head(_module, 'PKEY_Devices_WiFiDirect_InformationElements')
make_head(_module, 'PKEY_Devices_WiFiDirect_InterfaceAddress')
make_head(_module, 'PKEY_Devices_WiFiDirect_InterfaceGuid')
make_head(_module, 'PKEY_Devices_WiFiDirect_IsConnected')
make_head(_module, 'PKEY_Devices_WiFiDirect_IsLegacyDevice')
make_head(_module, 'PKEY_Devices_WiFiDirect_IsMiracastLcpSupported')
make_head(_module, 'PKEY_Devices_WiFiDirect_IsVisible')
make_head(_module, 'PKEY_Devices_WiFiDirect_MiracastVersion')
make_head(_module, 'PKEY_Devices_WiFiDirect_Services')
make_head(_module, 'PKEY_Devices_WiFiDirect_SupportedChannelList')
make_head(_module, 'PKEY_Devices_WiFiDirectServices_AdvertisementId')
make_head(_module, 'PKEY_Devices_WiFiDirectServices_RequestServiceInformation')
make_head(_module, 'PKEY_Devices_WiFiDirectServices_ServiceAddress')
make_head(_module, 'PKEY_Devices_WiFiDirectServices_ServiceConfigMethods')
make_head(_module, 'PKEY_Devices_WiFiDirectServices_ServiceInformation')
make_head(_module, 'PKEY_Devices_WiFiDirectServices_ServiceName')
make_head(_module, 'PKEY_Devices_WinPhone8CameraFlags')
make_head(_module, 'PKEY_Devices_Wwan_InterfaceGuid')
make_head(_module, 'PKEY_Storage_Portable')
make_head(_module, 'PKEY_Storage_RemovableMedia')
make_head(_module, 'PKEY_Storage_SystemCritical')
make_head(_module, 'PKEY_Document_ByteCount')
make_head(_module, 'PKEY_Document_CharacterCount')
make_head(_module, 'PKEY_Document_ClientID')
make_head(_module, 'PKEY_Document_Contributor')
make_head(_module, 'PKEY_Document_DateCreated')
make_head(_module, 'PKEY_Document_DatePrinted')
make_head(_module, 'PKEY_Document_DateSaved')
make_head(_module, 'PKEY_Document_Division')
make_head(_module, 'PKEY_Document_DocumentID')
make_head(_module, 'PKEY_Document_HiddenSlideCount')
make_head(_module, 'PKEY_Document_LastAuthor')
make_head(_module, 'PKEY_Document_LineCount')
make_head(_module, 'PKEY_Document_Manager')
make_head(_module, 'PKEY_Document_MultimediaClipCount')
make_head(_module, 'PKEY_Document_NoteCount')
make_head(_module, 'PKEY_Document_PageCount')
make_head(_module, 'PKEY_Document_ParagraphCount')
make_head(_module, 'PKEY_Document_PresentationFormat')
make_head(_module, 'PKEY_Document_RevisionNumber')
make_head(_module, 'PKEY_Document_Security')
make_head(_module, 'PKEY_Document_SlideCount')
make_head(_module, 'PKEY_Document_Template')
make_head(_module, 'PKEY_Document_TotalEditingTime')
make_head(_module, 'PKEY_Document_Version')
make_head(_module, 'PKEY_Document_WordCount')
make_head(_module, 'PKEY_DRM_DatePlayExpires')
make_head(_module, 'PKEY_DRM_DatePlayStarts')
make_head(_module, 'PKEY_DRM_Description')
make_head(_module, 'PKEY_DRM_IsDisabled')
make_head(_module, 'PKEY_DRM_IsProtected')
make_head(_module, 'PKEY_DRM_PlayCount')
make_head(_module, 'PKEY_GPS_Altitude')
make_head(_module, 'PKEY_GPS_AltitudeDenominator')
make_head(_module, 'PKEY_GPS_AltitudeNumerator')
make_head(_module, 'PKEY_GPS_AltitudeRef')
make_head(_module, 'PKEY_GPS_AreaInformation')
make_head(_module, 'PKEY_GPS_Date')
make_head(_module, 'PKEY_GPS_DestBearing')
make_head(_module, 'PKEY_GPS_DestBearingDenominator')
make_head(_module, 'PKEY_GPS_DestBearingNumerator')
make_head(_module, 'PKEY_GPS_DestBearingRef')
make_head(_module, 'PKEY_GPS_DestDistance')
make_head(_module, 'PKEY_GPS_DestDistanceDenominator')
make_head(_module, 'PKEY_GPS_DestDistanceNumerator')
make_head(_module, 'PKEY_GPS_DestDistanceRef')
make_head(_module, 'PKEY_GPS_DestLatitude')
make_head(_module, 'PKEY_GPS_DestLatitudeDenominator')
make_head(_module, 'PKEY_GPS_DestLatitudeNumerator')
make_head(_module, 'PKEY_GPS_DestLatitudeRef')
make_head(_module, 'PKEY_GPS_DestLongitude')
make_head(_module, 'PKEY_GPS_DestLongitudeDenominator')
make_head(_module, 'PKEY_GPS_DestLongitudeNumerator')
make_head(_module, 'PKEY_GPS_DestLongitudeRef')
make_head(_module, 'PKEY_GPS_Differential')
make_head(_module, 'PKEY_GPS_DOP')
make_head(_module, 'PKEY_GPS_DOPDenominator')
make_head(_module, 'PKEY_GPS_DOPNumerator')
make_head(_module, 'PKEY_GPS_ImgDirection')
make_head(_module, 'PKEY_GPS_ImgDirectionDenominator')
make_head(_module, 'PKEY_GPS_ImgDirectionNumerator')
make_head(_module, 'PKEY_GPS_ImgDirectionRef')
make_head(_module, 'PKEY_GPS_Latitude')
make_head(_module, 'PKEY_GPS_LatitudeDecimal')
make_head(_module, 'PKEY_GPS_LatitudeDenominator')
make_head(_module, 'PKEY_GPS_LatitudeNumerator')
make_head(_module, 'PKEY_GPS_LatitudeRef')
make_head(_module, 'PKEY_GPS_Longitude')
make_head(_module, 'PKEY_GPS_LongitudeDecimal')
make_head(_module, 'PKEY_GPS_LongitudeDenominator')
make_head(_module, 'PKEY_GPS_LongitudeNumerator')
make_head(_module, 'PKEY_GPS_LongitudeRef')
make_head(_module, 'PKEY_GPS_MapDatum')
make_head(_module, 'PKEY_GPS_MeasureMode')
make_head(_module, 'PKEY_GPS_ProcessingMethod')
make_head(_module, 'PKEY_GPS_Satellites')
make_head(_module, 'PKEY_GPS_Speed')
make_head(_module, 'PKEY_GPS_SpeedDenominator')
make_head(_module, 'PKEY_GPS_SpeedNumerator')
make_head(_module, 'PKEY_GPS_SpeedRef')
make_head(_module, 'PKEY_GPS_Status')
make_head(_module, 'PKEY_GPS_Track')
make_head(_module, 'PKEY_GPS_TrackDenominator')
make_head(_module, 'PKEY_GPS_TrackNumerator')
make_head(_module, 'PKEY_GPS_TrackRef')
make_head(_module, 'PKEY_GPS_VersionID')
make_head(_module, 'PKEY_History_VisitCount')
make_head(_module, 'PKEY_Image_BitDepth')
make_head(_module, 'PKEY_Image_ColorSpace')
make_head(_module, 'PKEY_Image_CompressedBitsPerPixel')
make_head(_module, 'PKEY_Image_CompressedBitsPerPixelDenominator')
make_head(_module, 'PKEY_Image_CompressedBitsPerPixelNumerator')
make_head(_module, 'PKEY_Image_Compression')
make_head(_module, 'PKEY_Image_CompressionText')
make_head(_module, 'PKEY_Image_Dimensions')
make_head(_module, 'PKEY_Image_HorizontalResolution')
make_head(_module, 'PKEY_Image_HorizontalSize')
make_head(_module, 'PKEY_Image_ImageID')
make_head(_module, 'PKEY_Image_ResolutionUnit')
make_head(_module, 'PKEY_Image_VerticalResolution')
make_head(_module, 'PKEY_Image_VerticalSize')
make_head(_module, 'PKEY_Journal_Contacts')
make_head(_module, 'PKEY_Journal_EntryType')
make_head(_module, 'PKEY_LayoutPattern_ContentViewModeForBrowse')
make_head(_module, 'PKEY_LayoutPattern_ContentViewModeForSearch')
make_head(_module, 'PKEY_History_SelectionCount')
make_head(_module, 'PKEY_History_TargetUrlHostName')
make_head(_module, 'PKEY_Link_Arguments')
make_head(_module, 'PKEY_Link_Comment')
make_head(_module, 'PKEY_Link_DateVisited')
make_head(_module, 'PKEY_Link_Description')
make_head(_module, 'PKEY_Link_FeedItemLocalId')
make_head(_module, 'PKEY_Link_Status')
make_head(_module, 'PKEY_Link_TargetExtension')
make_head(_module, 'PKEY_Link_TargetParsingPath')
make_head(_module, 'PKEY_Link_TargetSFGAOFlags')
make_head(_module, 'PKEY_Link_TargetUrlHostName')
make_head(_module, 'PKEY_Link_TargetUrlPath')
make_head(_module, 'PKEY_Media_AuthorUrl')
make_head(_module, 'PKEY_Media_AverageLevel')
make_head(_module, 'PKEY_Media_ClassPrimaryID')
make_head(_module, 'PKEY_Media_ClassSecondaryID')
make_head(_module, 'PKEY_Media_CollectionGroupID')
make_head(_module, 'PKEY_Media_CollectionID')
make_head(_module, 'PKEY_Media_ContentDistributor')
make_head(_module, 'PKEY_Media_ContentID')
make_head(_module, 'PKEY_Media_CreatorApplication')
make_head(_module, 'PKEY_Media_CreatorApplicationVersion')
make_head(_module, 'PKEY_Media_DateEncoded')
make_head(_module, 'PKEY_Media_DateReleased')
make_head(_module, 'PKEY_Media_DlnaProfileID')
make_head(_module, 'PKEY_Media_Duration')
make_head(_module, 'PKEY_Media_DVDID')
make_head(_module, 'PKEY_Media_EncodedBy')
make_head(_module, 'PKEY_Media_EncodingSettings')
make_head(_module, 'PKEY_Media_EpisodeNumber')
make_head(_module, 'PKEY_Media_FrameCount')
make_head(_module, 'PKEY_Media_MCDI')
make_head(_module, 'PKEY_Media_MetadataContentProvider')
make_head(_module, 'PKEY_Media_Producer')
make_head(_module, 'PKEY_Media_PromotionUrl')
make_head(_module, 'PKEY_Media_ProtectionType')
make_head(_module, 'PKEY_Media_ProviderRating')
make_head(_module, 'PKEY_Media_ProviderStyle')
make_head(_module, 'PKEY_Media_Publisher')
make_head(_module, 'PKEY_Media_SeasonNumber')
make_head(_module, 'PKEY_Media_SeriesName')
make_head(_module, 'PKEY_Media_SubscriptionContentId')
make_head(_module, 'PKEY_Media_SubTitle')
make_head(_module, 'PKEY_Media_ThumbnailLargePath')
make_head(_module, 'PKEY_Media_ThumbnailLargeUri')
make_head(_module, 'PKEY_Media_ThumbnailSmallPath')
make_head(_module, 'PKEY_Media_ThumbnailSmallUri')
make_head(_module, 'PKEY_Media_UniqueFileIdentifier')
make_head(_module, 'PKEY_Media_UserNoAutoInfo')
make_head(_module, 'PKEY_Media_UserWebUrl')
make_head(_module, 'PKEY_Media_Writer')
make_head(_module, 'PKEY_Media_Year')
make_head(_module, 'PKEY_Message_AttachmentContents')
make_head(_module, 'PKEY_Message_AttachmentNames')
make_head(_module, 'PKEY_Message_BccAddress')
make_head(_module, 'PKEY_Message_BccName')
make_head(_module, 'PKEY_Message_CcAddress')
make_head(_module, 'PKEY_Message_CcName')
make_head(_module, 'PKEY_Message_ConversationID')
make_head(_module, 'PKEY_Message_ConversationIndex')
make_head(_module, 'PKEY_Message_DateReceived')
make_head(_module, 'PKEY_Message_DateSent')
make_head(_module, 'PKEY_Message_Flags')
make_head(_module, 'PKEY_Message_FromAddress')
make_head(_module, 'PKEY_Message_FromName')
make_head(_module, 'PKEY_Message_HasAttachments')
make_head(_module, 'PKEY_Message_IsFwdOrReply')
make_head(_module, 'PKEY_Message_MessageClass')
make_head(_module, 'PKEY_Message_Participants')
make_head(_module, 'PKEY_Message_ProofInProgress')
make_head(_module, 'PKEY_Message_SenderAddress')
make_head(_module, 'PKEY_Message_SenderName')
make_head(_module, 'PKEY_Message_Store')
make_head(_module, 'PKEY_Message_ToAddress')
make_head(_module, 'PKEY_Message_ToDoFlags')
make_head(_module, 'PKEY_Message_ToDoTitle')
make_head(_module, 'PKEY_Message_ToName')
make_head(_module, 'PKEY_Music_AlbumArtist')
make_head(_module, 'PKEY_Music_AlbumArtistSortOverride')
make_head(_module, 'PKEY_Music_AlbumID')
make_head(_module, 'PKEY_Music_AlbumTitle')
make_head(_module, 'PKEY_Music_AlbumTitleSortOverride')
make_head(_module, 'PKEY_Music_Artist')
make_head(_module, 'PKEY_Music_ArtistSortOverride')
make_head(_module, 'PKEY_Music_BeatsPerMinute')
make_head(_module, 'PKEY_Music_Composer')
make_head(_module, 'PKEY_Music_ComposerSortOverride')
make_head(_module, 'PKEY_Music_Conductor')
make_head(_module, 'PKEY_Music_ContentGroupDescription')
make_head(_module, 'PKEY_Music_DiscNumber')
make_head(_module, 'PKEY_Music_DisplayArtist')
make_head(_module, 'PKEY_Music_Genre')
make_head(_module, 'PKEY_Music_InitialKey')
make_head(_module, 'PKEY_Music_IsCompilation')
make_head(_module, 'PKEY_Music_Lyrics')
make_head(_module, 'PKEY_Music_Mood')
make_head(_module, 'PKEY_Music_PartOfSet')
make_head(_module, 'PKEY_Music_Period')
make_head(_module, 'PKEY_Music_SynchronizedLyrics')
make_head(_module, 'PKEY_Music_TrackNumber')
make_head(_module, 'PKEY_Note_Color')
make_head(_module, 'PKEY_Note_ColorText')
make_head(_module, 'PKEY_Photo_Aperture')
make_head(_module, 'PKEY_Photo_ApertureDenominator')
make_head(_module, 'PKEY_Photo_ApertureNumerator')
make_head(_module, 'PKEY_Photo_Brightness')
make_head(_module, 'PKEY_Photo_BrightnessDenominator')
make_head(_module, 'PKEY_Photo_BrightnessNumerator')
make_head(_module, 'PKEY_Photo_CameraManufacturer')
make_head(_module, 'PKEY_Photo_CameraModel')
make_head(_module, 'PKEY_Photo_CameraSerialNumber')
make_head(_module, 'PKEY_Photo_Contrast')
make_head(_module, 'PKEY_Photo_ContrastText')
make_head(_module, 'PKEY_Photo_DateTaken')
make_head(_module, 'PKEY_Photo_DigitalZoom')
make_head(_module, 'PKEY_Photo_DigitalZoomDenominator')
make_head(_module, 'PKEY_Photo_DigitalZoomNumerator')
make_head(_module, 'PKEY_Photo_Event')
make_head(_module, 'PKEY_Photo_EXIFVersion')
make_head(_module, 'PKEY_Photo_ExposureBias')
make_head(_module, 'PKEY_Photo_ExposureBiasDenominator')
make_head(_module, 'PKEY_Photo_ExposureBiasNumerator')
make_head(_module, 'PKEY_Photo_ExposureIndex')
make_head(_module, 'PKEY_Photo_ExposureIndexDenominator')
make_head(_module, 'PKEY_Photo_ExposureIndexNumerator')
make_head(_module, 'PKEY_Photo_ExposureProgram')
make_head(_module, 'PKEY_Photo_ExposureProgramText')
make_head(_module, 'PKEY_Photo_ExposureTime')
make_head(_module, 'PKEY_Photo_ExposureTimeDenominator')
make_head(_module, 'PKEY_Photo_ExposureTimeNumerator')
make_head(_module, 'PKEY_Photo_Flash')
make_head(_module, 'PKEY_Photo_FlashEnergy')
make_head(_module, 'PKEY_Photo_FlashEnergyDenominator')
make_head(_module, 'PKEY_Photo_FlashEnergyNumerator')
make_head(_module, 'PKEY_Photo_FlashManufacturer')
make_head(_module, 'PKEY_Photo_FlashModel')
make_head(_module, 'PKEY_Photo_FlashText')
make_head(_module, 'PKEY_Photo_FNumber')
make_head(_module, 'PKEY_Photo_FNumberDenominator')
make_head(_module, 'PKEY_Photo_FNumberNumerator')
make_head(_module, 'PKEY_Photo_FocalLength')
make_head(_module, 'PKEY_Photo_FocalLengthDenominator')
make_head(_module, 'PKEY_Photo_FocalLengthInFilm')
make_head(_module, 'PKEY_Photo_FocalLengthNumerator')
make_head(_module, 'PKEY_Photo_FocalPlaneXResolution')
make_head(_module, 'PKEY_Photo_FocalPlaneXResolutionDenominator')
make_head(_module, 'PKEY_Photo_FocalPlaneXResolutionNumerator')
make_head(_module, 'PKEY_Photo_FocalPlaneYResolution')
make_head(_module, 'PKEY_Photo_FocalPlaneYResolutionDenominator')
make_head(_module, 'PKEY_Photo_FocalPlaneYResolutionNumerator')
make_head(_module, 'PKEY_Photo_GainControl')
make_head(_module, 'PKEY_Photo_GainControlDenominator')
make_head(_module, 'PKEY_Photo_GainControlNumerator')
make_head(_module, 'PKEY_Photo_GainControlText')
make_head(_module, 'PKEY_Photo_ISOSpeed')
make_head(_module, 'PKEY_Photo_LensManufacturer')
make_head(_module, 'PKEY_Photo_LensModel')
make_head(_module, 'PKEY_Photo_LightSource')
make_head(_module, 'PKEY_Photo_MakerNote')
make_head(_module, 'PKEY_Photo_MakerNoteOffset')
make_head(_module, 'PKEY_Photo_MaxAperture')
make_head(_module, 'PKEY_Photo_MaxApertureDenominator')
make_head(_module, 'PKEY_Photo_MaxApertureNumerator')
make_head(_module, 'PKEY_Photo_MeteringMode')
make_head(_module, 'PKEY_Photo_MeteringModeText')
make_head(_module, 'PKEY_Photo_Orientation')
make_head(_module, 'PKEY_Photo_OrientationText')
make_head(_module, 'PKEY_Photo_PeopleNames')
make_head(_module, 'PKEY_Photo_PhotometricInterpretation')
make_head(_module, 'PKEY_Photo_PhotometricInterpretationText')
make_head(_module, 'PKEY_Photo_ProgramMode')
make_head(_module, 'PKEY_Photo_ProgramModeText')
make_head(_module, 'PKEY_Photo_RelatedSoundFile')
make_head(_module, 'PKEY_Photo_Saturation')
make_head(_module, 'PKEY_Photo_SaturationText')
make_head(_module, 'PKEY_Photo_Sharpness')
make_head(_module, 'PKEY_Photo_SharpnessText')
make_head(_module, 'PKEY_Photo_ShutterSpeed')
make_head(_module, 'PKEY_Photo_ShutterSpeedDenominator')
make_head(_module, 'PKEY_Photo_ShutterSpeedNumerator')
make_head(_module, 'PKEY_Photo_SubjectDistance')
make_head(_module, 'PKEY_Photo_SubjectDistanceDenominator')
make_head(_module, 'PKEY_Photo_SubjectDistanceNumerator')
make_head(_module, 'PKEY_Photo_TagViewAggregate')
make_head(_module, 'PKEY_Photo_TranscodedForSync')
make_head(_module, 'PKEY_Photo_WhiteBalance')
make_head(_module, 'PKEY_Photo_WhiteBalanceText')
make_head(_module, 'PKEY_PropGroup_Advanced')
make_head(_module, 'PKEY_PropGroup_Audio')
make_head(_module, 'PKEY_PropGroup_Calendar')
make_head(_module, 'PKEY_PropGroup_Camera')
make_head(_module, 'PKEY_PropGroup_Contact')
make_head(_module, 'PKEY_PropGroup_Content')
make_head(_module, 'PKEY_PropGroup_Description')
make_head(_module, 'PKEY_PropGroup_FileSystem')
make_head(_module, 'PKEY_PropGroup_General')
make_head(_module, 'PKEY_PropGroup_GPS')
make_head(_module, 'PKEY_PropGroup_Image')
make_head(_module, 'PKEY_PropGroup_Media')
make_head(_module, 'PKEY_PropGroup_MediaAdvanced')
make_head(_module, 'PKEY_PropGroup_Message')
make_head(_module, 'PKEY_PropGroup_Music')
make_head(_module, 'PKEY_PropGroup_Origin')
make_head(_module, 'PKEY_PropGroup_PhotoAdvanced')
make_head(_module, 'PKEY_PropGroup_RecordedTV')
make_head(_module, 'PKEY_PropGroup_Video')
make_head(_module, 'PKEY_InfoTipText')
make_head(_module, 'PKEY_PropList_ConflictPrompt')
make_head(_module, 'PKEY_PropList_ContentViewModeForBrowse')
make_head(_module, 'PKEY_PropList_ContentViewModeForSearch')
make_head(_module, 'PKEY_PropList_ExtendedTileInfo')
make_head(_module, 'PKEY_PropList_FileOperationPrompt')
make_head(_module, 'PKEY_PropList_FullDetails')
make_head(_module, 'PKEY_PropList_InfoTip')
make_head(_module, 'PKEY_PropList_NonPersonal')
make_head(_module, 'PKEY_PropList_PreviewDetails')
make_head(_module, 'PKEY_PropList_PreviewTitle')
make_head(_module, 'PKEY_PropList_QuickTip')
make_head(_module, 'PKEY_PropList_TileInfo')
make_head(_module, 'PKEY_PropList_XPDetailsPanel')
make_head(_module, 'PKEY_RecordedTV_ChannelNumber')
make_head(_module, 'PKEY_RecordedTV_Credits')
make_head(_module, 'PKEY_RecordedTV_DateContentExpires')
make_head(_module, 'PKEY_RecordedTV_EpisodeName')
make_head(_module, 'PKEY_RecordedTV_IsATSCContent')
make_head(_module, 'PKEY_RecordedTV_IsClosedCaptioningAvailable')
make_head(_module, 'PKEY_RecordedTV_IsDTVContent')
make_head(_module, 'PKEY_RecordedTV_IsHDContent')
make_head(_module, 'PKEY_RecordedTV_IsRepeatBroadcast')
make_head(_module, 'PKEY_RecordedTV_IsSAP')
make_head(_module, 'PKEY_RecordedTV_NetworkAffiliation')
make_head(_module, 'PKEY_RecordedTV_OriginalBroadcastDate')
make_head(_module, 'PKEY_RecordedTV_ProgramDescription')
make_head(_module, 'PKEY_RecordedTV_RecordingTime')
make_head(_module, 'PKEY_RecordedTV_StationCallSign')
make_head(_module, 'PKEY_RecordedTV_StationName')
make_head(_module, 'PKEY_Search_AutoSummary')
make_head(_module, 'PKEY_Search_ContainerHash')
make_head(_module, 'PKEY_Search_Contents')
make_head(_module, 'PKEY_Search_EntryID')
make_head(_module, 'PKEY_Search_ExtendedProperties')
make_head(_module, 'PKEY_Search_GatherTime')
make_head(_module, 'PKEY_Search_HitCount')
make_head(_module, 'PKEY_Search_IsClosedDirectory')
make_head(_module, 'PKEY_Search_IsFullyContained')
make_head(_module, 'PKEY_Search_QueryFocusedSummary')
make_head(_module, 'PKEY_Search_QueryFocusedSummaryWithFallback')
make_head(_module, 'PKEY_Search_QueryPropertyHits')
make_head(_module, 'PKEY_Search_Rank')
make_head(_module, 'PKEY_Search_Store')
make_head(_module, 'PKEY_Search_UrlToIndex')
make_head(_module, 'PKEY_Search_UrlToIndexWithModificationTime')
make_head(_module, 'PKEY_Supplemental_Album')
make_head(_module, 'PKEY_Supplemental_AlbumID')
make_head(_module, 'PKEY_Supplemental_Location')
make_head(_module, 'PKEY_Supplemental_Person')
make_head(_module, 'PKEY_Supplemental_ResourceId')
make_head(_module, 'PKEY_Supplemental_Tag')
make_head(_module, 'PKEY_DescriptionID')
make_head(_module, 'PKEY_InternalName')
make_head(_module, 'PKEY_LibraryLocationsCount')
make_head(_module, 'PKEY_Link_TargetSFGAOFlagsStrings')
make_head(_module, 'PKEY_Link_TargetUrl')
make_head(_module, 'PKEY_NamespaceCLSID')
make_head(_module, 'PKEY_Shell_SFGAOFlagsStrings')
make_head(_module, 'PKEY_StatusBarSelectedItemCount')
make_head(_module, 'PKEY_StatusBarViewItemCount')
make_head(_module, 'PKEY_AppUserModel_ExcludeFromShowInNewInstall')
make_head(_module, 'PKEY_AppUserModel_ID')
make_head(_module, 'PKEY_AppUserModel_IsDestListSeparator')
make_head(_module, 'PKEY_AppUserModel_IsDualMode')
make_head(_module, 'PKEY_AppUserModel_PreventPinning')
make_head(_module, 'PKEY_AppUserModel_RelaunchCommand')
make_head(_module, 'PKEY_AppUserModel_RelaunchDisplayNameResource')
make_head(_module, 'PKEY_AppUserModel_RelaunchIconResource')
make_head(_module, 'PKEY_AppUserModel_SettingsCommand')
make_head(_module, 'PKEY_AppUserModel_StartPinOption')
make_head(_module, 'PKEY_AppUserModel_ToastActivatorCLSID')
make_head(_module, 'PKEY_AppUserModel_UninstallCommand')
make_head(_module, 'PKEY_AppUserModel_VisualElementsManifestHintPath')
make_head(_module, 'PKEY_EdgeGesture_DisableTouchWhenFullscreen')
make_head(_module, 'PKEY_Software_DateLastUsed')
make_head(_module, 'PKEY_Software_ProductName')
make_head(_module, 'PKEY_Sync_Comments')
make_head(_module, 'PKEY_Sync_ConflictDescription')
make_head(_module, 'PKEY_Sync_ConflictFirstLocation')
make_head(_module, 'PKEY_Sync_ConflictSecondLocation')
make_head(_module, 'PKEY_Sync_HandlerCollectionID')
make_head(_module, 'PKEY_Sync_HandlerID')
make_head(_module, 'PKEY_Sync_HandlerName')
make_head(_module, 'PKEY_Sync_HandlerType')
make_head(_module, 'PKEY_Sync_HandlerTypeLabel')
make_head(_module, 'PKEY_Sync_ItemID')
make_head(_module, 'PKEY_Sync_ItemName')
make_head(_module, 'PKEY_Sync_ProgressPercentage')
make_head(_module, 'PKEY_Sync_State')
make_head(_module, 'PKEY_Sync_Status')
make_head(_module, 'PKEY_Task_BillingInformation')
make_head(_module, 'PKEY_Task_CompletionStatus')
make_head(_module, 'PKEY_Task_Owner')
make_head(_module, 'PKEY_Video_Compression')
make_head(_module, 'PKEY_Video_Director')
make_head(_module, 'PKEY_Video_EncodingBitrate')
make_head(_module, 'PKEY_Video_FourCC')
make_head(_module, 'PKEY_Video_FrameHeight')
make_head(_module, 'PKEY_Video_FrameRate')
make_head(_module, 'PKEY_Video_FrameWidth')
make_head(_module, 'PKEY_Video_HorizontalAspectRatio')
make_head(_module, 'PKEY_Video_IsSpherical')
make_head(_module, 'PKEY_Video_IsStereo')
make_head(_module, 'PKEY_Video_Orientation')
make_head(_module, 'PKEY_Video_SampleSize')
make_head(_module, 'PKEY_Video_StreamName')
make_head(_module, 'PKEY_Video_StreamNumber')
make_head(_module, 'PKEY_Video_TotalBitrate')
make_head(_module, 'PKEY_Video_TranscodedForSync')
make_head(_module, 'PKEY_Video_VerticalAspectRatio')
make_head(_module, 'PKEY_Volume_FileSystem')
make_head(_module, 'PKEY_Volume_IsMappedDrive')
make_head(_module, 'PKEY_Volume_IsRoot')
make_head(_module, 'ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION')
make_head(_module, 'IEnhancedStorageACT')
make_head(_module, 'IEnhancedStorageACT2')
make_head(_module, 'IEnhancedStorageACT3')
make_head(_module, 'IEnhancedStorageSilo')
make_head(_module, 'IEnhancedStorageSiloAction')
make_head(_module, 'IEnumEnhancedStorageACT')
make_head(_module, 'SILO_INFO')
