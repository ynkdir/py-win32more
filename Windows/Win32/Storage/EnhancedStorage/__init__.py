from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Devices.PortableDevices
import Windows.Win32.Foundation
import Windows.Win32.Storage.EnhancedStorage
import Windows.Win32.System.Com
import Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class ACT_AUTHORIZATION_STATE(Structure):
    ulState: UInt32
ACT_AUTHORIZATION_STATE_VALUE = Int32
ACT_UNAUTHORIZED: ACT_AUTHORIZATION_STATE_VALUE = 0
ACT_AUTHORIZED: ACT_AUTHORIZATION_STATE_VALUE = 1
GUID_DEVINTERFACE_ENHANCED_STORAGE_SILO: Guid = Guid('3897f6a4-fd35-4bc8-a0-b7-5d-bb-a3-6a-da-fa')
WPD_CATEGORY_ENHANCED_STORAGE: Guid = Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c')
def ENHANCED_STORAGE_COMMAND_SILO_IS_AUTHENTICATION_SILO():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=6)
def ENHANCED_STORAGE_COMMAND_SILO_GET_AUTHENTICATION_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=7)
def ENHANCED_STORAGE_COMMAND_SILO_ENUMERATE_SILOS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=11)
def ENHANCED_STORAGE_COMMAND_CERT_HOST_CERTIFICATE_AUTHENTICATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=101)
def ENHANCED_STORAGE_COMMAND_CERT_DEVICE_CERTIFICATE_AUTHENTICATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=102)
def ENHANCED_STORAGE_COMMAND_CERT_ADMIN_CERTIFICATE_AUTHENTICATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=103)
def ENHANCED_STORAGE_COMMAND_CERT_INITIALIZE_TO_MANUFACTURER_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=104)
def ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE_COUNT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=105)
def ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=106)
def ENHANCED_STORAGE_COMMAND_CERT_SET_CERTIFICATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=107)
def ENHANCED_STORAGE_COMMAND_CERT_CREATE_CERTIFICATE_REQUEST():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=108)
def ENHANCED_STORAGE_COMMAND_CERT_UNAUTHENTICATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=110)
def ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=111)
def ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITIES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=112)
def ENHANCED_STORAGE_COMMAND_CERT_GET_ACT_FRIENDLY_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=113)
def ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_GUID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=114)
def ENHANCED_STORAGE_COMMAND_PASSWORD_AUTHORIZE_ACT_ACCESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=203)
def ENHANCED_STORAGE_COMMAND_PASSWORD_UNAUTHORIZE_ACT_ACCESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=204)
def ENHANCED_STORAGE_COMMAND_PASSWORD_QUERY_INFORMATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=205)
def ENHANCED_STORAGE_COMMAND_PASSWORD_CONFIG_ADMINISTRATOR():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=206)
def ENHANCED_STORAGE_COMMAND_PASSWORD_CREATE_USER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=207)
def ENHANCED_STORAGE_COMMAND_PASSWORD_DELETE_USER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=208)
def ENHANCED_STORAGE_COMMAND_PASSWORD_CHANGE_PASSWORD():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=209)
def ENHANCED_STORAGE_COMMAND_PASSWORD_INITIALIZE_USER_PASSWORD():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=210)
def ENHANCED_STORAGE_COMMAND_PASSWORD_START_INITIALIZE_TO_MANUFACTURER_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=211)
def ENHANCED_STORAGE_PROPERTY_AUTHENTICATION_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=1006)
ENHANCED_STORAGE_AUTHN_STATE_UNKNOWN: UInt32 = 0
ENHANCED_STORAGE_AUTHN_STATE_NO_AUTHENTICATION_REQUIRED: UInt32 = 1
ENHANCED_STORAGE_AUTHN_STATE_NOT_AUTHENTICATED: UInt32 = 2
ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATED: UInt32 = 3
ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATION_DENIED: UInt32 = 2147483649
ENHANCED_STORAGE_AUTHN_STATE_DEVICE_ERROR: UInt32 = 2147483650
def ENHANCED_STORAGE_PROPERTY_IS_AUTHENTICATION_SILO():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=1009)
def ENHANCED_STORAGE_PROPERTY_TEMPORARY_UNAUTHENTICATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=1010)
def ENHANCED_STORAGE_PROPERTY_MAX_AUTH_FAILURES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2001)
def ENHANCED_STORAGE_PROPERTY_PASSWORD():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2004)
def ENHANCED_STORAGE_PROPERTY_OLD_PASSWORD():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2005)
def ENHANCED_STORAGE_PROPERTY_PASSWORD_INDICATOR():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2006)
def ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD_INDICATOR():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2007)
def ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2008)
def ENHANCED_STORAGE_PROPERTY_USER_HINT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2009)
def ENHANCED_STORAGE_PROPERTY_USER_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2010)
def ENHANCED_STORAGE_PROPERTY_ADMIN_HINT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2011)
def ENHANCED_STORAGE_PROPERTY_SILO_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2012)
def ENHANCED_STORAGE_PROPERTY_SILO_FRIENDLYNAME_SPECIFIED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2013)
def ENHANCED_STORAGE_PROPERTY_PASSWORD_SILO_INFO():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2014)
def ENHANCED_STORAGE_PROPERTY_SECURITY_IDENTIFIER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2015)
def ENHANCED_STORAGE_PROPERTY_QUERY_SILO_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2016)
def ENHANCED_STORAGE_PROPERTY_QUERY_SILO_RESULTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=2017)
def ENHANCED_STORAGE_PROPERTY_MAX_CERTIFICATE_COUNT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3001)
def ENHANCED_STORAGE_PROPERTY_STORED_CERTIFICATE_COUNT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3002)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_INDEX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3003)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3004)
CERT_TYPE_EMPTY: UInt32 = 0
CERT_TYPE_ASCm: UInt32 = 1
CERT_TYPE_PCp: UInt32 = 2
CERT_TYPE_ASCh: UInt32 = 3
CERT_TYPE_HCh: UInt32 = 4
CERT_TYPE_SIGNER: UInt32 = 6
def ENHANCED_STORAGE_PROPERTY_VALIDATION_POLICY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3005)
CERT_VALIDATION_POLICY_RESERVED: UInt32 = 0
CERT_VALIDATION_POLICY_NONE: UInt32 = 1
CERT_VALIDATION_POLICY_BASIC: UInt32 = 2
CERT_VALIDATION_POLICY_EXTENDED: UInt32 = 3
def ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_INDEX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3006)
def ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_OF_TYPE_INDEX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3007)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_LENGTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3008)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3009)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_REQUEST():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3010)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_CAPABILITY_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3011)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3012)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITIES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3013)
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
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3014)
def ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_GUID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3015)
def ENHANCED_STORAGE_PROPERTY_SIGNER_CERTIFICATE_INDEX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=3016)
def ENHANCED_STORAGE_CAPABILITY_HASH_ALGS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=4001)
def ENHANCED_STORAGE_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=4002)
def ENHANCED_STORAGE_CAPABILITY_SIGNING_ALGS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=4003)
def ENHANCED_STORAGE_CAPABILITY_RENDER_USER_DATA_UNUSABLE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=4004)
def ENHANCED_STORAGE_CAPABILITY_CERTIFICATE_EXTENSION_PARSING():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91248166-b832-4ad4-ba-a4-7c-a0-b6-b2-79-8c'), pid=4005)
def PKEY_Address_Country():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c07b4199-e1df-4493-b1-e1-de-59-46-fb-58-f8'), pid=100)
def PKEY_Address_CountryCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c07b4199-e1df-4493-b1-e1-de-59-46-fb-58-f8'), pid=101)
def PKEY_Address_Region():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c07b4199-e1df-4493-b1-e1-de-59-46-fb-58-f8'), pid=102)
def PKEY_Address_RegionCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c07b4199-e1df-4493-b1-e1-de-59-46-fb-58-f8'), pid=103)
def PKEY_Address_Town():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c07b4199-e1df-4493-b1-e1-de-59-46-fb-58-f8'), pid=104)
def PKEY_Audio_ChannelCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440490-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=7)
AUDIO_CHANNELCOUNT_MONO: UInt32 = 1
AUDIO_CHANNELCOUNT_STEREO: UInt32 = 2
def PKEY_Audio_Compression():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440490-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=10)
def PKEY_Audio_EncodingBitrate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440490-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=4)
def PKEY_Audio_Format():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440490-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=2)
def PKEY_Audio_IsVariableBitRate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6822fee-8c17-4d62-82-3c-8e-9c-fc-bd-1d-5c'), pid=100)
def PKEY_Audio_PeakValue():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2579e5d0-1116-4084-bd-9a-9b-4f-7c-b4-df-5e'), pid=100)
def PKEY_Audio_SampleRate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440490-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=5)
def PKEY_Audio_SampleSize():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440490-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=6)
def PKEY_Audio_StreamName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440490-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=9)
def PKEY_Audio_StreamNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440490-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=8)
def PKEY_Calendar_Duration():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('293ca35a-09aa-4dd2-b1-80-1f-e2-45-72-8a-52'), pid=100)
def PKEY_Calendar_IsOnline():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bfee9149-e3e2-49a7-a8-62-c0-59-88-14-5c-ec'), pid=100)
def PKEY_Calendar_IsRecurring():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('315b9c8d-80a9-4ef9-ae-16-8e-74-6d-a5-1d-70'), pid=100)
def PKEY_Calendar_Location():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f6272d18-cecc-40b1-b2-6a-39-11-71-7a-a7-bd'), pid=100)
def PKEY_Calendar_OptionalAttendeeAddresses():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d55bae5a-3892-417a-a6-49-c6-ac-5a-aa-ea-b3'), pid=100)
def PKEY_Calendar_OptionalAttendeeNames():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('09429607-582d-437f-84-c3-de-93-a2-b2-4c-3c'), pid=100)
def PKEY_Calendar_OrganizerAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('744c8242-4df5-456c-ab-9e-01-4e-fb-90-21-e3'), pid=100)
def PKEY_Calendar_OrganizerName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('aaa660f9-9865-458e-b4-84-01-bc-7f-e3-97-3e'), pid=100)
def PKEY_Calendar_ReminderTime():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('72fc5ba4-24f9-4011-9f-3f-ad-d2-7a-fa-d8-18'), pid=100)
def PKEY_Calendar_RequiredAttendeeAddresses():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0ba7d6c3-568d-4159-ab-91-78-1a-91-fb-71-e5'), pid=100)
def PKEY_Calendar_RequiredAttendeeNames():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b33af30b-f552-4584-93-6c-cb-93-e5-cd-a2-9f'), pid=100)
def PKEY_Calendar_Resources():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f58a38-c54b-4c40-86-96-97-23-59-80-ea-e1'), pid=100)
def PKEY_Calendar_ResponseStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('188c1f91-3c40-4132-9e-c5-d8-b0-3b-72-a8-a2'), pid=100)
def PKEY_Calendar_ShowTimeAs():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5bf396d4-5eb2-466f-bd-e9-2f-b3-f2-36-1d-6e'), pid=100)
def PKEY_Calendar_ShowTimeAsText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('53da57cf-62c0-45c4-81-de-76-10-bc-ef-d7-f5'), pid=100)
def PKEY_Communication_AccountName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=9)
def PKEY_Communication_DateItemExpires():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('428040ac-a177-4c8a-97-60-f6-f7-61-22-7f-9a'), pid=100)
def PKEY_Communication_Direction():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8e531030-b960-4346-ae-0d-66-bc-9a-86-fb-94'), pid=100)
def PKEY_Communication_FollowupIconIndex():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('83a6347e-6fe4-4f40-ba-9c-c4-86-52-40-d1-f4'), pid=100)
def PKEY_Communication_HeaderItem():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9c34f84-2241-4401-b6-07-bd-20-ed-75-ae-7f'), pid=100)
def PKEY_Communication_PolicyTag():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ec0b4191-ab0b-4c66-90-b6-c6-63-7c-de-bb-ab'), pid=100)
def PKEY_Communication_SecurityFlags():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8619a4b6-9f4d-4429-8c-0f-b9-96-ca-59-e3-35'), pid=100)
def PKEY_Communication_Suffix():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('807b653a-9e91-43ef-8f-97-11-ce-04-ee-20-c5'), pid=100)
def PKEY_Communication_TaskStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('be1a72c6-9a1d-46b7-af-e7-af-af-8c-ef-49-99'), pid=100)
def PKEY_Communication_TaskStatusText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a6744477-c237-475b-a0-75-54-f3-44-98-29-2a'), pid=100)
def PKEY_Computer_DecoratedFreeSpace():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9b174b35-40ff-11d2-a2-7e-00-c0-4f-c3-08-71'), pid=7)
def PKEY_Contact_AccountPictureDynamicVideo():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0b8bb018-2725-4b44-92-ba-79-33-ae-b2-dd-e7'), pid=2)
def PKEY_Contact_AccountPictureLarge():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0b8bb018-2725-4b44-92-ba-79-33-ae-b2-dd-e7'), pid=3)
def PKEY_Contact_AccountPictureSmall():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0b8bb018-2725-4b44-92-ba-79-33-ae-b2-dd-e7'), pid=4)
def PKEY_Contact_Anniversary():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9ad5badb-cea7-4470-a0-3d-b8-4e-51-b9-94-9e'), pid=100)
def PKEY_Contact_AssistantName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cd102c9c-5540-4a88-a6-f6-64-e4-98-1c-8c-d1'), pid=100)
def PKEY_Contact_AssistantTelephone():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9a93244d-a7ad-4ff8-9b-99-45-ee-4c-c0-9a-f6'), pid=100)
def PKEY_Contact_Birthday():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=47)
def PKEY_Contact_BusinessAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('730fb6dd-cf7c-426b-a0-3f-bd-16-6c-c9-ee-24'), pid=100)
def PKEY_Contact_BusinessAddress1Country():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=119)
def PKEY_Contact_BusinessAddress1Locality():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=117)
def PKEY_Contact_BusinessAddress1PostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=120)
def PKEY_Contact_BusinessAddress1Region():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=118)
def PKEY_Contact_BusinessAddress1Street():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=116)
def PKEY_Contact_BusinessAddress2Country():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=124)
def PKEY_Contact_BusinessAddress2Locality():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=122)
def PKEY_Contact_BusinessAddress2PostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=125)
def PKEY_Contact_BusinessAddress2Region():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=123)
def PKEY_Contact_BusinessAddress2Street():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=121)
def PKEY_Contact_BusinessAddress3Country():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=129)
def PKEY_Contact_BusinessAddress3Locality():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=127)
def PKEY_Contact_BusinessAddress3PostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=130)
def PKEY_Contact_BusinessAddress3Region():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=128)
def PKEY_Contact_BusinessAddress3Street():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=126)
def PKEY_Contact_BusinessAddressCity():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('402b5934-ec5a-48c3-93-e6-85-e8-6a-2d-93-4e'), pid=100)
def PKEY_Contact_BusinessAddressCountry():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b0b87314-fcf6-4feb-8d-ff-a5-0d-a6-af-56-1c'), pid=100)
def PKEY_Contact_BusinessAddressPostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e1d4a09e-d758-4cd1-b6-ec-34-a8-b5-a7-3f-80'), pid=100)
def PKEY_Contact_BusinessAddressPostOfficeBox():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bc4e71ce-17f9-48d5-be-e9-02-1d-f0-ea-54-09'), pid=100)
def PKEY_Contact_BusinessAddressState():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('446f787f-10c4-41cb-a6-c4-4d-03-43-55-15-97'), pid=100)
def PKEY_Contact_BusinessAddressStreet():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ddd1460f-c0bf-4553-8c-e4-10-43-3c-90-8f-b0'), pid=100)
def PKEY_Contact_BusinessEmailAddresses():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f271c659-7e5e-471f-ba-25-7f-77-b2-86-f8-36'), pid=100)
def PKEY_Contact_BusinessFaxNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('91eff6f3-2e27-42ca-93-3e-7c-99-9f-be-31-0b'), pid=100)
def PKEY_Contact_BusinessHomePage():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56310920-2491-4919-99-ce-ea-db-06-fa-fd-b2'), pid=100)
def PKEY_Contact_BusinessTelephone():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6a15e5a0-0a1e-4cd7-bb-8c-d2-f1-b0-c9-29-bc'), pid=100)
def PKEY_Contact_CallbackTelephone():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf53d1c3-49e0-4f7f-85-67-5a-82-1d-8a-c5-42'), pid=100)
def PKEY_Contact_CarTelephone():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8fdc6dea-b929-412b-ba-90-39-7a-25-74-65-fe'), pid=100)
def PKEY_Contact_Children():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d4729704-8ef1-43ef-90-24-2b-d3-81-18-7f-d5'), pid=100)
def PKEY_Contact_CompanyMainTelephone():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8589e481-6040-473d-b1-71-7f-a8-9c-27-08-ed'), pid=100)
def PKEY_Contact_ConnectedServiceDisplayName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('39b77f4f-a104-4863-b3-95-2d-b2-ad-8f-7b-c1'), pid=100)
def PKEY_Contact_ConnectedServiceIdentities():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80f41eb8-afc4-4208-aa-5f-cc-e2-1a-62-72-81'), pid=100)
def PKEY_Contact_ConnectedServiceName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b5c84c9e-5927-46b5-a3-cc-93-3c-21-b7-84-69'), pid=100)
def PKEY_Contact_ConnectedServiceSupportedActions():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a19fb7a9-024b-4371-a8-bf-4d-29-c3-e4-e9-c9'), pid=100)
def PKEY_Contact_DataSuppliers():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9660c283-fc3a-4a08-a0-96-ee-d3-aa-c4-6d-a2'), pid=100)
def PKEY_Contact_Department():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fc9f7306-ff8f-4d49-9f-b6-3f-fe-5c-09-51-ec'), pid=100)
def PKEY_Contact_DisplayBusinessPhoneNumbers():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('364028da-d895-41fe-a5-84-30-2b-1b-b7-0a-76'), pid=100)
def PKEY_Contact_DisplayHomePhoneNumbers():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5068bcdf-d697-4d85-8c-53-1f-1c-da-b0-17-63'), pid=100)
def PKEY_Contact_DisplayMobilePhoneNumbers():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9cb0c358-9d7a-46b1-b4-66-dc-c6-f1-a3-d9-3d'), pid=100)
def PKEY_Contact_DisplayOtherPhoneNumbers():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('03089873-8ee8-4191-bd-60-d3-1f-72-b7-90-0b'), pid=100)
def PKEY_Contact_EmailAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f8fa7fa3-d12b-4785-8a-4e-69-1a-94-f7-a3-e7'), pid=100)
def PKEY_Contact_EmailAddress2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38965063-edc8-4268-84-91-b7-72-31-72-cf-29'), pid=100)
def PKEY_Contact_EmailAddress3():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('644d37b4-e1b3-4bad-b0-99-7e-7c-04-96-6a-ca'), pid=100)
def PKEY_Contact_EmailAddresses():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('84d8f337-981d-44b3-96-15-c7-59-6d-ba-17-e3'), pid=100)
def PKEY_Contact_EmailName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cc6f4f24-6083-4bd4-87-54-67-4d-0d-e8-7a-b8'), pid=100)
def PKEY_Contact_FileAsName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f1a24aa7-9ca7-40f6-89-ec-97-de-f9-ff-e8-db'), pid=100)
def PKEY_Contact_FirstName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14977844-6b49-4aad-a7-14-a4-51-3b-f6-04-60'), pid=100)
def PKEY_Contact_FullName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('635e9051-50a5-4ba2-b9-db-4e-d0-56-c7-72-96'), pid=100)
def PKEY_Contact_Gender():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3c8cee58-d4f0-4cf9-b7-56-4e-5d-24-44-7b-cd'), pid=100)
def PKEY_Contact_GenderValue():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3c8cee58-d4f0-4cf9-b7-56-4e-5d-24-44-7b-cd'), pid=101)
def PKEY_Contact_Hobbies():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5dc2253f-5e11-4adf-9c-fe-91-0d-d0-1e-3e-70'), pid=100)
def PKEY_Contact_HomeAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('98f98354-617a-46b8-85-60-5b-1b-64-bf-1f-89'), pid=100)
def PKEY_Contact_HomeAddress1Country():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=104)
def PKEY_Contact_HomeAddress1Locality():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=102)
def PKEY_Contact_HomeAddress1PostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=105)
def PKEY_Contact_HomeAddress1Region():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=103)
def PKEY_Contact_HomeAddress1Street():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=101)
def PKEY_Contact_HomeAddress2Country():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=109)
def PKEY_Contact_HomeAddress2Locality():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=107)
def PKEY_Contact_HomeAddress2PostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=110)
def PKEY_Contact_HomeAddress2Region():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=108)
def PKEY_Contact_HomeAddress2Street():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=106)
def PKEY_Contact_HomeAddress3Country():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=114)
def PKEY_Contact_HomeAddress3Locality():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=112)
def PKEY_Contact_HomeAddress3PostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=115)
def PKEY_Contact_HomeAddress3Region():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=113)
def PKEY_Contact_HomeAddress3Street():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=111)
def PKEY_Contact_HomeAddressCity():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=65)
def PKEY_Contact_HomeAddressCountry():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('08a65aa1-f4c9-43dd-9d-df-a3-3d-8e-7e-ad-85'), pid=100)
def PKEY_Contact_HomeAddressPostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8afcc170-8a46-4b53-9e-ee-90-ba-e7-15-1e-62'), pid=100)
def PKEY_Contact_HomeAddressPostOfficeBox():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7b9f6399-0a3f-4b12-89-bd-4a-dc-51-c9-18-af'), pid=100)
def PKEY_Contact_HomeAddressState():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c89a23d0-7d6d-4eb8-87-d4-77-6a-82-d4-93-e5'), pid=100)
def PKEY_Contact_HomeAddressStreet():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0adef160-db3f-4308-9a-21-06-23-7b-16-fa-2a'), pid=100)
def PKEY_Contact_HomeEmailAddresses():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56c90e9d-9d46-4963-88-6f-2e-1c-d9-a6-94-ef'), pid=100)
def PKEY_Contact_HomeFaxNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('660e04d6-81ab-4977-a0-9f-82-31-31-13-ab-26'), pid=100)
def PKEY_Contact_HomeTelephone():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=20)
def PKEY_Contact_IMAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d68dbd8a-3374-4b81-99-72-3e-c3-06-82-db-3d'), pid=100)
def PKEY_Contact_Initials():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f3d8f40d-50cb-44a2-97-18-40-cb-91-19-49-5d'), pid=100)
def PKEY_Contact_JA_CompanyNamePhonetic():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('897b3694-fe9e-43e6-80-66-26-0f-59-0c-01-00'), pid=2)
def PKEY_Contact_JA_FirstNamePhonetic():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('897b3694-fe9e-43e6-80-66-26-0f-59-0c-01-00'), pid=3)
def PKEY_Contact_JA_LastNamePhonetic():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('897b3694-fe9e-43e6-80-66-26-0f-59-0c-01-00'), pid=4)
def PKEY_Contact_JobInfo1CompanyAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=120)
def PKEY_Contact_JobInfo1CompanyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=102)
def PKEY_Contact_JobInfo1Department():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=106)
def PKEY_Contact_JobInfo1Manager():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=105)
def PKEY_Contact_JobInfo1OfficeLocation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=104)
def PKEY_Contact_JobInfo1Title():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=103)
def PKEY_Contact_JobInfo1YomiCompanyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=101)
def PKEY_Contact_JobInfo2CompanyAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=121)
def PKEY_Contact_JobInfo2CompanyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=108)
def PKEY_Contact_JobInfo2Department():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=113)
def PKEY_Contact_JobInfo2Manager():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=112)
def PKEY_Contact_JobInfo2OfficeLocation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=110)
def PKEY_Contact_JobInfo2Title():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=109)
def PKEY_Contact_JobInfo2YomiCompanyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=107)
def PKEY_Contact_JobInfo3CompanyAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=123)
def PKEY_Contact_JobInfo3CompanyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=115)
def PKEY_Contact_JobInfo3Department():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=119)
def PKEY_Contact_JobInfo3Manager():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=118)
def PKEY_Contact_JobInfo3OfficeLocation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=117)
def PKEY_Contact_JobInfo3Title():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=116)
def PKEY_Contact_JobInfo3YomiCompanyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=114)
def PKEY_Contact_JobTitle():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=6)
def PKEY_Contact_Label():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('97b0ad89-df49-49cc-83-4e-66-09-74-fd-75-5b'), pid=100)
def PKEY_Contact_LastName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8f367200-c270-457c-b1-d4-e0-7c-5b-cd-90-c7'), pid=100)
def PKEY_Contact_MailingAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c0ac206a-827e-4650-95-ae-77-e2-bb-74-fc-c9'), pid=100)
def PKEY_Contact_MiddleName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=71)
def PKEY_Contact_MobileTelephone():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=35)
def PKEY_Contact_NickName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=74)
def PKEY_Contact_OfficeLocation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=7)
def PKEY_Contact_OtherAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('508161fa-313b-43d5-83-a1-c1-ac-cf-68-62-2c'), pid=100)
def PKEY_Contact_OtherAddress1Country():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=134)
def PKEY_Contact_OtherAddress1Locality():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=132)
def PKEY_Contact_OtherAddress1PostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=135)
def PKEY_Contact_OtherAddress1Region():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=133)
def PKEY_Contact_OtherAddress1Street():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=131)
def PKEY_Contact_OtherAddress2Country():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=139)
def PKEY_Contact_OtherAddress2Locality():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=137)
def PKEY_Contact_OtherAddress2PostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=140)
def PKEY_Contact_OtherAddress2Region():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=138)
def PKEY_Contact_OtherAddress2Street():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=136)
def PKEY_Contact_OtherAddress3Country():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=144)
def PKEY_Contact_OtherAddress3Locality():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=142)
def PKEY_Contact_OtherAddress3PostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=145)
def PKEY_Contact_OtherAddress3Region():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=143)
def PKEY_Contact_OtherAddress3Street():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7b6f596-d678-4bc1-b0-5f-02-03-d2-7e-8a-a1'), pid=141)
def PKEY_Contact_OtherAddressCity():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6e682923-7f7b-4f0c-a3-37-cf-ca-29-66-87-bf'), pid=100)
def PKEY_Contact_OtherAddressCountry():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8f167568-0aae-4322-8e-d9-60-55-b7-b0-e3-98'), pid=100)
def PKEY_Contact_OtherAddressPostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('95c656c1-2abf-4148-9e-d3-9e-c6-02-e3-b7-cd'), pid=100)
def PKEY_Contact_OtherAddressPostOfficeBox():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8b26ea41-058f-43f6-ae-cc-40-35-68-1c-e9-77'), pid=100)
def PKEY_Contact_OtherAddressState():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('71b377d6-e570-425f-a1-70-80-9f-ae-73-e5-4e'), pid=100)
def PKEY_Contact_OtherAddressStreet():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ff962609-b7d6-4999-86-2d-95-18-0d-52-9a-ea'), pid=100)
def PKEY_Contact_OtherEmailAddresses():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11d6336b-38c4-4ec9-84-d6-eb-38-d0-b1-50-af'), pid=100)
def PKEY_Contact_PagerTelephone():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d6304e01-f8f5-4f45-8b-15-d0-24-a6-29-67-89'), pid=100)
def PKEY_Contact_PersonalTitle():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=69)
def PKEY_Contact_PhoneNumbersCanonical():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d042d2a1-927e-40b5-a5-03-6e-db-d4-2a-51-7e'), pid=100)
def PKEY_Contact_Prefix():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=75)
def PKEY_Contact_PrimaryAddressCity():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c8ea94f0-a9e3-4969-a9-4b-9c-62-a9-53-24-e0'), pid=100)
def PKEY_Contact_PrimaryAddressCountry():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e53d799d-0f3f-466e-b2-ff-74-63-4a-3c-b7-a4'), pid=100)
def PKEY_Contact_PrimaryAddressPostalCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('18bbd425-ecfd-46ef-b6-12-7b-4a-60-34-ed-a0'), pid=100)
def PKEY_Contact_PrimaryAddressPostOfficeBox():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('de5ef3c7-46e1-484e-99-99-62-c5-30-83-94-c1'), pid=100)
def PKEY_Contact_PrimaryAddressState():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f1176dfe-7138-4640-8b-4c-ae-37-5d-c7-0a-6d'), pid=100)
def PKEY_Contact_PrimaryAddressStreet():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63c25b20-96be-488f-87-88-c0-9c-40-7a-d8-12'), pid=100)
def PKEY_Contact_PrimaryEmailAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=48)
def PKEY_Contact_PrimaryTelephone():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=25)
def PKEY_Contact_Profession():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7268af55-1ce4-4f6e-a4-1f-b6-e4-ef-10-e4-a9'), pid=100)
def PKEY_Contact_SpouseName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9d2408b6-3167-422b-82-b0-f5-83-b7-a7-cf-e3'), pid=100)
def PKEY_Contact_Suffix():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('176dc63c-2688-4e89-81-43-a3-47-80-0f-25-e9'), pid=73)
def PKEY_Contact_TelexNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c554493c-c1f7-40c1-a7-6c-ef-8c-06-14-00-3e'), pid=100)
def PKEY_Contact_TTYTDDTelephone():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('aaf16bac-2b55-45e6-9f-6d-41-5e-b9-49-10-df'), pid=100)
def PKEY_Contact_WebPage():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=18)
def PKEY_Contact_Webpage2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=124)
def PKEY_Contact_Webpage3():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f63dd8-22bd-4a5d-ba-34-5c-b0-b9-bd-cb-03'), pid=125)
def PKEY_AcquisitionID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('65a98875-3c80-40ab-ab-bc-ef-da-f7-7d-be-e2'), pid=100)
def PKEY_ApplicationDefinedProperties():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cdbfc167-337e-41d8-af-7c-8c-09-20-54-29-c7'), pid=100)
def PKEY_ApplicationName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=18)
def PKEY_AppZoneIdentifier():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('502cfeab-47eb-459c-b9-60-e6-d8-72-8f-77-01'), pid=102)
def PKEY_Author():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=4)
def PKEY_CachedFileUpdaterContentIdForConflictResolution():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=114)
def PKEY_CachedFileUpdaterContentIdForStream():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=113)
def PKEY_Capacity():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9b174b35-40ff-11d2-a2-7e-00-c0-4f-c3-08-71'), pid=3)
def PKEY_Category():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=2)
def PKEY_Comment():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=6)
def PKEY_Company():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=15)
def PKEY_ComputerName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=5)
def PKEY_ContainedItems():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=29)
def PKEY_ContentId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=132)
def PKEY_ContentStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=27)
def PKEY_ContentType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=26)
def PKEY_ContentUri():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=131)
def PKEY_Copyright():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=11)
def PKEY_CreatorAppId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c2ea046e-033c-4e91-bd-5b-d4-94-2f-6b-be-49'), pid=2)
def PKEY_CreatorOpenWithUIOptions():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c2ea046e-033c-4e91-bd-5b-d4-94-2f-6b-be-49'), pid=3)
CREATOROPENWITHUIOPTION_HIDDEN: UInt32 = 0
CREATOROPENWITHUIOPTION_VISIBLE: UInt32 = 1
def PKEY_DataObjectFormat():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1e81a3f8-a30f-4247-b9-ee-1d-03-68-a9-42-5c'), pid=2)
def PKEY_DateAccessed():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=16)
def PKEY_DateAcquired():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2cbaa8f5-d81f-47ca-b1-7a-f8-d8-22-30-01-31'), pid=100)
def PKEY_DateArchived():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('43f8d7b7-a444-4f87-93-83-52-27-1c-9b-91-5c'), pid=100)
def PKEY_DateCompleted():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('72fab781-acda-43e5-b1-55-b2-43-4f-85-e6-78'), pid=100)
def PKEY_DateCreated():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=15)
def PKEY_DateImported():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=18258)
def PKEY_DateModified():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=14)
def PKEY_DefaultSaveLocationDisplay():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5d76b67f-9b3d-44bb-b6-ae-25-da-4f-63-8a-67'), pid=10)
ISDEFAULTSAVE_NONE: UInt32 = 0
ISDEFAULTSAVE_OWNER: UInt32 = 1
ISDEFAULTSAVE_NONOWNER: UInt32 = 2
ISDEFAULTSAVE_BOTH: UInt32 = 3
def PKEY_DueDate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8472b5-e0af-4db2-80-71-c5-3f-e7-6a-e7-ce'), pid=100)
def PKEY_EndDate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c75faa05-96fd-49e7-9c-b4-9f-60-10-82-d5-53'), pid=100)
def PKEY_ExpandoProperties():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6fa20de6-d11c-4d9d-a1-54-64-31-76-28-c1-2d'), pid=100)
def PKEY_FileAllocationSize():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=18)
def PKEY_FileAttributes():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=13)
def PKEY_FileCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=12)
def PKEY_FileDescription():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cef7d53-fa64-11d1-a2-03-00-00-f8-1f-ed-ee'), pid=3)
def PKEY_FileExtension():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4f10a3c-49e6-405d-82-88-a2-3b-d4-ee-aa-6c'), pid=100)
def PKEY_FileFRN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=21)
def PKEY_FileName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41cf5ae0-f75a-4806-bd-87-59-c7-d9-24-8e-b9'), pid=100)
def PKEY_FileOfflineAvailabilityStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=100)
FILEOFFLINEAVAILABILITYSTATUS_NOTAVAILABLEOFFLINE: UInt32 = 0
FILEOFFLINEAVAILABILITYSTATUS_PARTIAL: UInt32 = 1
FILEOFFLINEAVAILABILITYSTATUS_COMPLETE: UInt32 = 2
FILEOFFLINEAVAILABILITYSTATUS_COMPLETE_PINNED: UInt32 = 3
FILEOFFLINEAVAILABILITYSTATUS_EXCLUDED: UInt32 = 4
FILEOFFLINEAVAILABILITYSTATUS_FOLDER_EMPTY: UInt32 = 5
def PKEY_FileOwner():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9b174b34-40ff-11d2-a2-7e-00-c0-4f-c3-08-71'), pid=4)
def PKEY_FilePlaceholderStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b2f9b9d6-fec4-4dd5-94-d7-89-57-48-8c-80-7b'), pid=2)
def PKEY_FileVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cef7d53-fa64-11d1-a2-03-00-00-f8-1f-ed-ee'), pid=4)
def PKEY_FindData():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=0)
def PKEY_FlagColor():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('67df94de-0ca7-4d6f-b7-92-05-3a-3e-4f-03-cf'), pid=100)
def PKEY_FlagColorText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('45eae747-8e2a-40ae-8c-bf-ca-52-ab-a6-15-2a'), pid=100)
def PKEY_FlagStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=12)
FLAGSTATUS_NOTFLAGGED: Int32 = 0
FLAGSTATUS_COMPLETED: Int32 = 1
FLAGSTATUS_FOLLOWUP: Int32 = 2
def PKEY_FlagStatusText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('dc54fd2e-189d-4871-aa-01-08-c2-f5-7a-4a-bc'), pid=100)
def PKEY_FolderKind():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=101)
def PKEY_FolderNameDisplay():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=25)
def PKEY_FreeSpace():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9b174b35-40ff-11d2-a2-7e-00-c0-4f-c3-08-71'), pid=2)
def PKEY_FullText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1e3ee840-bc2b-476c-82-37-2a-cd-1a-83-9b-22'), pid=6)
def PKEY_HighKeywords():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=24)
def PKEY_Identity():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a26f4afc-7346-4299-be-47-eb-1a-e6-13-13-9f'), pid=100)
def PKEY_Identity_Blob():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8c3b93a4-baed-1a83-9a-32-10-2e-e3-13-f6-eb'), pid=100)
def PKEY_Identity_DisplayName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7d683fc9-d155-45a8-bb-1f-89-d1-9b-cb-79-2f'), pid=100)
def PKEY_Identity_InternetSid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d6d5d49-265d-4688-9f-4e-1f-dd-33-e7-cc-83'), pid=100)
def PKEY_Identity_IsMeIdentity():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a4108708-09df-4377-9d-fc-6d-99-98-6d-5a-67'), pid=100)
def PKEY_Identity_KeyProviderContext():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a26f4afc-7346-4299-be-47-eb-1a-e6-13-13-9f'), pid=17)
def PKEY_Identity_KeyProviderName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a26f4afc-7346-4299-be-47-eb-1a-e6-13-13-9f'), pid=16)
def PKEY_Identity_LogonStatusString():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f18dedf3-337f-42c0-9e-03-ce-e0-87-08-a8-c3'), pid=100)
def PKEY_Identity_PrimaryEmailAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fcc16823-baed-4f24-9b-32-a0-98-21-17-f7-fa'), pid=100)
def PKEY_Identity_PrimarySid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2b1b801e-c0c1-4987-9e-c5-72-fa-89-81-47-87'), pid=100)
def PKEY_Identity_ProviderData():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8a74b92-361b-4e9a-b7-22-7c-4a-73-30-a3-12'), pid=100)
def PKEY_Identity_ProviderID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('74a7de49-fa11-4d3d-a0-06-db-7e-08-67-59-16'), pid=100)
def PKEY_Identity_QualifiedUserName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('da520e51-f4e9-4739-ac-82-02-e0-a9-5c-90-30'), pid=100)
def PKEY_Identity_UniqueID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e55fc3b0-2b60-4220-91-8e-b2-1e-8b-f1-60-16'), pid=100)
def PKEY_Identity_UserName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c4322503-78ca-49c6-9a-cc-a6-8e-2a-fd-7b-6b'), pid=100)
def PKEY_IdentityProvider_Name():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b96eff7b-35ca-4a35-86-07-29-e3-a5-4c-46-ea'), pid=100)
def PKEY_IdentityProvider_Picture():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2425166f-5642-4864-99-2f-98-fd-98-f2-94-c3'), pid=100)
def PKEY_ImageParsingName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d7750ee0-c6a4-48ec-b5-3e-b8-7b-52-e6-d0-73'), pid=100)
def PKEY_Importance():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=11)
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
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a3b29791-7713-4e1d-bb-40-17-db-85-f0-18-31'), pid=100)
def PKEY_IsAttachment():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f23f425c-71a1-4fa8-92-2f-67-8e-a4-a6-04-08'), pid=100)
def PKEY_IsDefaultNonOwnerSaveLocation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5d76b67f-9b3d-44bb-b6-ae-25-da-4f-63-8a-67'), pid=5)
def PKEY_IsDefaultSaveLocation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5d76b67f-9b3d-44bb-b6-ae-25-da-4f-63-8a-67'), pid=3)
def PKEY_IsDeleted():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5cda5fc8-33ee-4ff3-90-94-ae-7b-d8-86-8c-4d'), pid=100)
def PKEY_IsEncrypted():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('90e5e14e-648b-4826-b2-aa-ac-af-79-0e-35-13'), pid=10)
def PKEY_IsFlagged():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5da84765-e3ff-4278-86-b0-a2-79-67-fb-dd-03'), pid=100)
def PKEY_IsFlaggedComplete():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a6f360d2-55f9-48de-b9-09-62-0e-09-0a-64-7c'), pid=100)
def PKEY_IsIncomplete():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346c8bd1-2e6a-4c45-89-a4-61-b7-8e-8e-70-0f'), pid=100)
def PKEY_IsLocationSupported():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5d76b67f-9b3d-44bb-b6-ae-25-da-4f-63-8a-67'), pid=8)
def PKEY_IsPinnedToNameSpaceTree():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5d76b67f-9b3d-44bb-b6-ae-25-da-4f-63-8a-67'), pid=2)
def PKEY_IsRead():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=10)
def PKEY_IsSearchOnlyItem():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5d76b67f-9b3d-44bb-b6-ae-25-da-4f-63-8a-67'), pid=4)
def PKEY_IsSendToTarget():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=33)
def PKEY_IsShared():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef884c5b-2bfe-41bb-aa-e5-76-ee-df-4f-99-02'), pid=100)
def PKEY_ItemAuthors():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d0a04f0a-462a-48a4-bb-2f-37-06-e8-8d-bd-7d'), pid=100)
def PKEY_ItemClassType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('048658ad-2db8-41a4-bb-b6-ac-1e-f1-20-7e-b1'), pid=100)
def PKEY_ItemDate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f7db74b4-4287-4103-af-ba-f1-b1-3d-cd-75-cf'), pid=100)
def PKEY_ItemFolderNameDisplay():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=2)
def PKEY_ItemFolderPathDisplay():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=6)
def PKEY_ItemFolderPathDisplayNarrow():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('dabd30ed-0043-4789-a7-f8-d0-13-a4-73-66-22'), pid=100)
def PKEY_ItemName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6b8da074-3b5c-43bc-88-6f-0a-2c-dc-e0-0b-6f'), pid=100)
def PKEY_ItemNameDisplay():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=10)
def PKEY_ItemNameDisplayWithoutExtension():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=24)
def PKEY_ItemNamePrefix():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d7313ff1-a77a-401c-8c-99-3d-bd-d6-8a-dd-36'), pid=100)
def PKEY_ItemNameSortOverride():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=23)
def PKEY_ItemParticipants():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d4d0aa16-9948-41a4-aa-85-d9-7f-f9-64-69-93'), pid=100)
def PKEY_ItemPathDisplay():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=7)
def PKEY_ItemPathDisplayNarrow():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=8)
def PKEY_ItemSubType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=37)
def PKEY_ItemType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=11)
def PKEY_ItemTypeText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=4)
def PKEY_ItemUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49691c90-7e17-101a-a9-1c-08-00-2b-2e-cd-a9'), pid=9)
def PKEY_Keywords():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=5)
def PKEY_Kind():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1e3ee840-bc2b-476c-82-37-2a-cd-1a-83-9b-22'), pid=3)
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
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f04bef95-c585-4197-a2-b7-df-46-fd-c9-ee-6d'), pid=100)
def PKEY_Language():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=28)
def PKEY_LastSyncError():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=107)
def PKEY_LastSyncWarning():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=128)
def PKEY_LastWriterPackageFamilyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('502cfeab-47eb-459c-b9-60-e6-d8-72-8f-77-01'), pid=101)
def PKEY_LowKeywords():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=25)
def PKEY_MediumKeywords():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=26)
def PKEY_MileageInformation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fdf84370-031a-4add-9e-91-0d-77-5f-1c-66-05'), pid=100)
def PKEY_MIMEType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0b63e350-9ccc-11d0-bc-db-00-80-5f-cc-ce-04'), pid=5)
def PKEY_Null():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00000000-0000-0000-00-00-00-00-00-00-00-00'), pid=0)
def PKEY_OfflineAvailability():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a94688b6-7d9f-4570-a6-48-e3-df-c0-ab-2b-3f'), pid=100)
OFFLINEAVAILABILITY_NOT_AVAILABLE: UInt32 = 0
OFFLINEAVAILABILITY_AVAILABLE: UInt32 = 1
OFFLINEAVAILABILITY_ALWAYS_AVAILABLE: UInt32 = 2
def PKEY_OfflineStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d24888f-4718-4bda-af-ed-ea-0f-b4-38-6c-d8'), pid=100)
OFFLINESTATUS_ONLINE: UInt32 = 0
OFFLINESTATUS_OFFLINE: UInt32 = 1
OFFLINESTATUS_OFFLINE_FORCED: UInt32 = 2
OFFLINESTATUS_OFFLINE_SLOW: UInt32 = 3
OFFLINESTATUS_OFFLINE_ERROR: UInt32 = 4
OFFLINESTATUS_OFFLINE_ITEM_VERSION_CONFLICT: UInt32 = 5
OFFLINESTATUS_OFFLINE_SUSPENDED: UInt32 = 6
def PKEY_OriginalFileName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cef7d53-fa64-11d1-a2-03-00-00-f8-1f-ed-ee'), pid=6)
def PKEY_OwnerSID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5d76b67f-9b3d-44bb-b6-ae-25-da-4f-63-8a-67'), pid=6)
def PKEY_ParentalRating():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=21)
def PKEY_ParentalRatingReason():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10984e0a-f9f2-4321-b7-ef-ba-f1-95-af-43-19'), pid=100)
def PKEY_ParentalRatingsOrganization():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a7fe0840-1344-46f0-8d-37-52-ed-71-2a-4b-f9'), pid=100)
def PKEY_ParsingBindContext():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('dfb9a04d-362f-4ca3-b3-0b-02-54-b1-7b-5b-84'), pid=100)
def PKEY_ParsingName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=24)
def PKEY_ParsingPath():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=30)
def PKEY_PerceivedType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=9)
def PKEY_PercentFull():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9b174b35-40ff-11d2-a2-7e-00-c0-4f-c3-08-71'), pid=5)
def PKEY_Priority():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9c1fcf74-2d97-41ba-b4-ae-cb-2e-36-61-a6-e4'), pid=5)
def PKEY_PriorityText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d98be98b-b86b-4095-bf-52-9d-23-b2-e0-a7-52'), pid=100)
def PKEY_Project():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('39a7f922-477c-48de-8b-c8-b2-84-41-e3-42-e3'), pid=100)
def PKEY_ProviderItemID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f21d9941-81f0-471a-ad-ee-4e-74-b4-92-17-ed'), pid=100)
def PKEY_Rating():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=9)
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
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('90197ca7-fd8f-4e8c-9d-a3-b5-7e-1e-60-92-95'), pid=100)
def PKEY_RemoteConflictingFile():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=115)
def PKEY_Security_AllowedEnterpriseDataProtectionIdentities():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38d43380-d418-4830-84-d5-46-93-5a-81-c5-c6'), pid=32)
def PKEY_Security_EncryptionOwners():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5f5aff6a-37e5-4780-97-ea-80-c7-56-5c-f5-35'), pid=34)
def PKEY_Security_EncryptionOwnersDisplay():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('de621b8f-e125-43a3-a3-2d-56-65-44-6d-63-2a'), pid=25)
def PKEY_Sensitivity():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f8d3f6ac-4874-42cb-be-59-ab-45-4b-30-71-6a'), pid=100)
def PKEY_SensitivityText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d0c7f054-3f72-4725-85-27-12-9a-57-7c-b2-69'), pid=100)
def PKEY_SFGAOFlags():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=25)
def PKEY_SharedWith():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef884c5b-2bfe-41bb-aa-e5-76-ee-df-4f-99-02'), pid=200)
def PKEY_ShareUserRating():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=12)
def PKEY_SharingStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef884c5b-2bfe-41bb-aa-e5-76-ee-df-4f-99-02'), pid=300)
SHARINGSTATUS_NOTSHARED: UInt32 = 0
SHARINGSTATUS_SHARED: UInt32 = 1
SHARINGSTATUS_PRIVATE: UInt32 = 2
def PKEY_Shell_OmitFromView():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('de35258c-c695-4cbc-b9-82-38-b0-ad-24-ce-d0'), pid=2)
def PKEY_SimpleRating():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a09f084e-ad41-489f-80-76-aa-5b-e3-08-2b-ca'), pid=100)
def PKEY_Size():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=12)
def PKEY_SoftwareUsed():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=305)
def PKEY_SourceItem():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('668cdfa5-7a1b-4323-ae-4b-e5-27-39-3a-1d-81'), pid=100)
def PKEY_SourcePackageFamilyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ffae9db7-1c8d-43ff-81-8c-84-40-3a-a3-73-2d'), pid=100)
def PKEY_StartDate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('48fd6ec8-8a12-4cdf-a0-3e-4e-c5-a5-11-ed-de'), pid=100)
def PKEY_Status():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('000214a1-0000-0000-c0-00-00-00-00-00-00-46'), pid=9)
def PKEY_StorageProviderCallerVersionInformation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b2f9b9d6-fec4-4dd5-94-d7-89-57-48-8c-80-7b'), pid=7)
def PKEY_StorageProviderError():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=109)
def PKEY_StorageProviderFileChecksum():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b2f9b9d6-fec4-4dd5-94-d7-89-57-48-8c-80-7b'), pid=5)
def PKEY_StorageProviderFileFlags():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b2f9b9d6-fec4-4dd5-94-d7-89-57-48-8c-80-7b'), pid=8)
def PKEY_StorageProviderFileHasConflict():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b2f9b9d6-fec4-4dd5-94-d7-89-57-48-8c-80-7b'), pid=9)
def PKEY_StorageProviderFileIdentifier():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b2f9b9d6-fec4-4dd5-94-d7-89-57-48-8c-80-7b'), pid=3)
def PKEY_StorageProviderFileRemoteUri():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=112)
def PKEY_StorageProviderFileVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b2f9b9d6-fec4-4dd5-94-d7-89-57-48-8c-80-7b'), pid=4)
def PKEY_StorageProviderFileVersionWaterline():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b2f9b9d6-fec4-4dd5-94-d7-89-57-48-8c-80-7b'), pid=6)
def PKEY_StorageProviderId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=108)
def PKEY_StorageProviderShareStatuses():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=111)
STORAGE_PROVIDER_SHARE_STATUS_PRIVATE: String = 'Private'
STORAGE_PROVIDER_SHARE_STATUS_SHARED: String = 'Shared'
STORAGE_PROVIDER_SHARE_STATUS_PUBLIC: String = 'Public'
STORAGE_PROVIDER_SHARE_STATUS_GROUP: String = 'Group'
STORAGE_PROVIDER_SHARE_STATUS_OWNER: String = 'Owner'
def PKEY_StorageProviderSharingStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=117)
STORAGE_PROVIDER_SHARINGSTATUS_NOTSHARED: UInt32 = 0
STORAGE_PROVIDER_SHARINGSTATUS_SHARED: UInt32 = 1
STORAGE_PROVIDER_SHARINGSTATUS_PRIVATE: UInt32 = 2
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC: UInt32 = 3
STORAGE_PROVIDER_SHARINGSTATUS_SHARED_OWNED: UInt32 = 4
STORAGE_PROVIDER_SHARINGSTATUS_SHARED_COOWNED: UInt32 = 5
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_OWNED: UInt32 = 6
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_COOWNED: UInt32 = 7
def PKEY_StorageProviderStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=110)
def PKEY_Subject():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=3)
def PKEY_SyncTransferStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=103)
def PKEY_Thumbnail():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=17)
def PKEY_ThumbnailCacheId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('446d16b1-8dad-4870-a7-48-40-2e-a4-3d-78-8c'), pid=100)
def PKEY_ThumbnailStream():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=27)
def PKEY_Title():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=2)
def PKEY_TitleSortOverride():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0f7984d-222e-4ad2-82-ab-1d-d8-ea-40-e5-7e'), pid=300)
def PKEY_TotalFileSize():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=14)
def PKEY_Trademarks():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cef7d53-fa64-11d1-a2-03-00-00-f8-1f-ed-ee'), pid=9)
def PKEY_TransferOrder():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=106)
def PKEY_TransferPosition():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=104)
def PKEY_TransferSize():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fceff153-e839-4cf3-a9-e7-ea-22-83-20-94-b8'), pid=105)
def PKEY_VolumeId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('446d16b1-8dad-4870-a7-48-40-2e-a4-3d-78-8c'), pid=104)
def PKEY_ZoneIdentifier():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('502cfeab-47eb-459c-b9-60-e6-d8-72-8f-77-01'), pid=100)
def PKEY_Device_PrinterURL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0b48f35a-be6e-4f17-b1-08-3c-40-73-d1-66-9a'), pid=15)
def PKEY_DeviceInterface_Bluetooth_DeviceAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bd67d8b-8beb-48d5-87-e0-6c-da-34-28-04-0a'), pid=1)
def PKEY_DeviceInterface_Bluetooth_Flags():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bd67d8b-8beb-48d5-87-e0-6c-da-34-28-04-0a'), pid=3)
def PKEY_DeviceInterface_Bluetooth_LastConnectedTime():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bd67d8b-8beb-48d5-87-e0-6c-da-34-28-04-0a'), pid=11)
def PKEY_DeviceInterface_Bluetooth_Manufacturer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bd67d8b-8beb-48d5-87-e0-6c-da-34-28-04-0a'), pid=4)
def PKEY_DeviceInterface_Bluetooth_ModelNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bd67d8b-8beb-48d5-87-e0-6c-da-34-28-04-0a'), pid=5)
def PKEY_DeviceInterface_Bluetooth_ProductId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bd67d8b-8beb-48d5-87-e0-6c-da-34-28-04-0a'), pid=8)
def PKEY_DeviceInterface_Bluetooth_ProductVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bd67d8b-8beb-48d5-87-e0-6c-da-34-28-04-0a'), pid=9)
def PKEY_DeviceInterface_Bluetooth_ServiceGuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bd67d8b-8beb-48d5-87-e0-6c-da-34-28-04-0a'), pid=2)
def PKEY_DeviceInterface_Bluetooth_VendorId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bd67d8b-8beb-48d5-87-e0-6c-da-34-28-04-0a'), pid=7)
def PKEY_DeviceInterface_Bluetooth_VendorIdSource():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bd67d8b-8beb-48d5-87-e0-6c-da-34-28-04-0a'), pid=6)
def PKEY_DeviceInterface_Hid_IsReadOnly():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cbf38310-4a17-4310-a1-eb-24-7f-0b-67-59-3b'), pid=4)
def PKEY_DeviceInterface_Hid_ProductId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cbf38310-4a17-4310-a1-eb-24-7f-0b-67-59-3b'), pid=6)
def PKEY_DeviceInterface_Hid_UsageId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cbf38310-4a17-4310-a1-eb-24-7f-0b-67-59-3b'), pid=3)
def PKEY_DeviceInterface_Hid_UsagePage():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cbf38310-4a17-4310-a1-eb-24-7f-0b-67-59-3b'), pid=2)
def PKEY_DeviceInterface_Hid_VendorId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cbf38310-4a17-4310-a1-eb-24-7f-0b-67-59-3b'), pid=5)
def PKEY_DeviceInterface_Hid_VersionNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cbf38310-4a17-4310-a1-eb-24-7f-0b-67-59-3b'), pid=7)
def PKEY_DeviceInterface_PrinterDriverDirectory():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('847c66de-b8d6-4af9-ab-c3-6f-4f-92-6b-c0-39'), pid=14)
def PKEY_DeviceInterface_PrinterDriverName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc47170-14f5-498c-8f-30-b0-d1-9b-e4-49-c6'), pid=11)
def PKEY_DeviceInterface_PrinterEnumerationFlag():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a00742a1-cd8c-4b37-95-ab-70-75-55-87-76-7a'), pid=3)
def PKEY_DeviceInterface_PrinterName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0a7b84ef-0c27-463f-84-ef-06-c5-07-00-01-be'), pid=10)
def PKEY_DeviceInterface_PrinterPortName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('eec7b761-6f94-41b1-94-9f-c7-29-72-0d-d1-3c'), pid=12)
def PKEY_DeviceInterface_Proximity_SupportsNfc():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fb3842cd-9e2a-4f83-8f-cc-4b-07-61-13-9a-e9'), pid=2)
def PKEY_DeviceInterface_Serial_PortName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4c6bf15c-4c03-4aac-91-f5-64-c0-f8-52-bc-f4'), pid=4)
def PKEY_DeviceInterface_Serial_UsbProductId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4c6bf15c-4c03-4aac-91-f5-64-c0-f8-52-bc-f4'), pid=3)
def PKEY_DeviceInterface_Serial_UsbVendorId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4c6bf15c-4c03-4aac-91-f5-64-c0-f8-52-bc-f4'), pid=2)
def PKEY_DeviceInterface_WinUsb_DeviceInterfaceClasses():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('95e127b5-79cc-4e83-9c-9e-84-22-18-7b-3e-0e'), pid=7)
def PKEY_DeviceInterface_WinUsb_UsbClass():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('95e127b5-79cc-4e83-9c-9e-84-22-18-7b-3e-0e'), pid=4)
def PKEY_DeviceInterface_WinUsb_UsbProductId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('95e127b5-79cc-4e83-9c-9e-84-22-18-7b-3e-0e'), pid=3)
def PKEY_DeviceInterface_WinUsb_UsbProtocol():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('95e127b5-79cc-4e83-9c-9e-84-22-18-7b-3e-0e'), pid=6)
def PKEY_DeviceInterface_WinUsb_UsbSubClass():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('95e127b5-79cc-4e83-9c-9e-84-22-18-7b-3e-0e'), pid=5)
def PKEY_DeviceInterface_WinUsb_UsbVendorId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('95e127b5-79cc-4e83-9c-9e-84-22-18-7b-3e-0e'), pid=2)
def PKEY_Devices_Aep_AepId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3b2ce006-5e61-4fde-ba-b8-9b-8a-ac-9b-26-df'), pid=8)
def PKEY_Devices_Aep_Bluetooth_Cod_Major():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5fbd34cd-561a-412e-ba-98-47-8a-6b-0f-ef-1d'), pid=2)
def PKEY_Devices_Aep_Bluetooth_Cod_Minor():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5fbd34cd-561a-412e-ba-98-47-8a-6b-0f-ef-1d'), pid=3)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Audio():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5fbd34cd-561a-412e-ba-98-47-8a-6b-0f-ef-1d'), pid=10)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Capturing():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5fbd34cd-561a-412e-ba-98-47-8a-6b-0f-ef-1d'), pid=8)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Information():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5fbd34cd-561a-412e-ba-98-47-8a-6b-0f-ef-1d'), pid=12)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_LimitedDiscovery():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5fbd34cd-561a-412e-ba-98-47-8a-6b-0f-ef-1d'), pid=4)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Networking():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5fbd34cd-561a-412e-ba-98-47-8a-6b-0f-ef-1d'), pid=6)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_ObjectXfer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5fbd34cd-561a-412e-ba-98-47-8a-6b-0f-ef-1d'), pid=9)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Positioning():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5fbd34cd-561a-412e-ba-98-47-8a-6b-0f-ef-1d'), pid=5)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Rendering():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5fbd34cd-561a-412e-ba-98-47-8a-6b-0f-ef-1d'), pid=7)
def PKEY_Devices_Aep_Bluetooth_Cod_Services_Telephony():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5fbd34cd-561a-412e-ba-98-47-8a-6b-0f-ef-1d'), pid=11)
def PKEY_Devices_Aep_Bluetooth_LastSeenTime():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bd67d8b-8beb-48d5-87-e0-6c-da-34-28-04-0a'), pid=12)
def PKEY_Devices_Aep_Bluetooth_Le_AddressType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('995ef0b0-7eb3-4a8b-b9-ce-06-8b-b3-f4-af-69'), pid=4)
BLUETOOTH_ADDRESS_TYPE_PUBLIC: UInt32 = 0
BLUETOOTH_ADDRESS_TYPE_RANDOM: UInt32 = 1
def PKEY_Devices_Aep_Bluetooth_Le_Appearance():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('995ef0b0-7eb3-4a8b-b9-ce-06-8b-b3-f4-af-69'), pid=1)
def PKEY_Devices_Aep_Bluetooth_Le_Appearance_Category():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('995ef0b0-7eb3-4a8b-b9-ce-06-8b-b3-f4-af-69'), pid=5)
def PKEY_Devices_Aep_Bluetooth_Le_Appearance_Subcategory():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('995ef0b0-7eb3-4a8b-b9-ce-06-8b-b3-f4-af-69'), pid=6)
def PKEY_Devices_Aep_Bluetooth_Le_IsConnectable():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('995ef0b0-7eb3-4a8b-b9-ce-06-8b-b3-f4-af-69'), pid=8)
def PKEY_Devices_Aep_CanPair():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e7c3fb29-caa7-4f47-8c-8b-be-59-b3-30-d4-c5'), pid=3)
def PKEY_Devices_Aep_Category():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a35996ab-11cf-4935-8b-61-a6-76-10-81-ec-df'), pid=17)
def PKEY_Devices_Aep_ContainerId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e7c3fb29-caa7-4f47-8c-8b-be-59-b3-30-d4-c5'), pid=2)
def PKEY_Devices_Aep_DeviceAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a35996ab-11cf-4935-8b-61-a6-76-10-81-ec-df'), pid=12)
def PKEY_Devices_Aep_IsConnected():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a35996ab-11cf-4935-8b-61-a6-76-10-81-ec-df'), pid=7)
def PKEY_Devices_Aep_IsPaired():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a35996ab-11cf-4935-8b-61-a6-76-10-81-ec-df'), pid=16)
def PKEY_Devices_Aep_IsPresent():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a35996ab-11cf-4935-8b-61-a6-76-10-81-ec-df'), pid=9)
def PKEY_Devices_Aep_Manufacturer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a35996ab-11cf-4935-8b-61-a6-76-10-81-ec-df'), pid=5)
def PKEY_Devices_Aep_ModelId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a35996ab-11cf-4935-8b-61-a6-76-10-81-ec-df'), pid=4)
def PKEY_Devices_Aep_ModelName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a35996ab-11cf-4935-8b-61-a6-76-10-81-ec-df'), pid=3)
def PKEY_Devices_Aep_PointOfService_ConnectionTypes():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d4bf61b3-442e-4ada-88-2d-fa-7b-70-c8-32-d9'), pid=6)
def PKEY_Devices_Aep_ProtocolId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3b2ce006-5e61-4fde-ba-b8-9b-8a-ac-9b-26-df'), pid=5)
def PKEY_Devices_Aep_SignalStrength():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a35996ab-11cf-4935-8b-61-a6-76-10-81-ec-df'), pid=6)
def PKEY_Devices_AepContainer_CanPair():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0bba1ede-7566-4f47-90-ec-25-fc-56-7c-ed-2a'), pid=3)
def PKEY_Devices_AepContainer_Categories():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0bba1ede-7566-4f47-90-ec-25-fc-56-7c-ed-2a'), pid=9)
def PKEY_Devices_AepContainer_Children():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0bba1ede-7566-4f47-90-ec-25-fc-56-7c-ed-2a'), pid=2)
def PKEY_Devices_AepContainer_ContainerId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0bba1ede-7566-4f47-90-ec-25-fc-56-7c-ed-2a'), pid=12)
def PKEY_Devices_AepContainer_DialProtocol_InstalledApplications():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=6)
def PKEY_Devices_AepContainer_IsPaired():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0bba1ede-7566-4f47-90-ec-25-fc-56-7c-ed-2a'), pid=4)
def PKEY_Devices_AepContainer_IsPresent():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0bba1ede-7566-4f47-90-ec-25-fc-56-7c-ed-2a'), pid=11)
def PKEY_Devices_AepContainer_Manufacturer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0bba1ede-7566-4f47-90-ec-25-fc-56-7c-ed-2a'), pid=6)
def PKEY_Devices_AepContainer_ModelIds():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0bba1ede-7566-4f47-90-ec-25-fc-56-7c-ed-2a'), pid=8)
def PKEY_Devices_AepContainer_ModelName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0bba1ede-7566-4f47-90-ec-25-fc-56-7c-ed-2a'), pid=7)
def PKEY_Devices_AepContainer_ProtocolIds():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0bba1ede-7566-4f47-90-ec-25-fc-56-7c-ed-2a'), pid=13)
def PKEY_Devices_AepContainer_SupportedUriSchemes():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=5)
def PKEY_Devices_AepContainer_SupportsAudio():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=2)
def PKEY_Devices_AepContainer_SupportsCapturing():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=11)
def PKEY_Devices_AepContainer_SupportsImages():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=4)
def PKEY_Devices_AepContainer_SupportsInformation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=14)
def PKEY_Devices_AepContainer_SupportsLimitedDiscovery():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=7)
def PKEY_Devices_AepContainer_SupportsNetworking():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=9)
def PKEY_Devices_AepContainer_SupportsObjectTransfer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=12)
def PKEY_Devices_AepContainer_SupportsPositioning():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=8)
def PKEY_Devices_AepContainer_SupportsRendering():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=10)
def PKEY_Devices_AepContainer_SupportsTelephony():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=13)
def PKEY_Devices_AepContainer_SupportsVideo():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6af55d45-38db-4495-ac-b0-d4-72-8a-3b-83-14'), pid=3)
def PKEY_Devices_AepService_AepId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9c141a9-1b4c-4f17-a9-d1-f2-98-53-8c-ad-b8'), pid=6)
def PKEY_Devices_AepService_Bluetooth_CacheMode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9744311e-7951-4b2e-b6-f0-ec-b2-93-ca-c1-19'), pid=5)
BLUETOOTH_CACHE_MODE_CACHED: UInt32 = 0
BLUETOOTH_CACHED_MODE_UNCACHED: UInt32 = 1
def PKEY_Devices_AepService_Bluetooth_ServiceGuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a399aac7-c265-474e-b0-73-ff-ce-57-72-17-16'), pid=2)
def PKEY_Devices_AepService_Bluetooth_TargetDevice():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9744311e-7951-4b2e-b6-f0-ec-b2-93-ca-c1-19'), pid=6)
def PKEY_Devices_AepService_ContainerId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('71724756-3e74-4432-9b-59-e7-b2-f6-68-a5-93'), pid=4)
def PKEY_Devices_AepService_FriendlyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('71724756-3e74-4432-9b-59-e7-b2-f6-68-a5-93'), pid=2)
def PKEY_Devices_AepService_IoT_ServiceInterfaces():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('79d94e82-4d79-45aa-82-1a-74-85-8b-4e-4c-a6'), pid=2)
def PKEY_Devices_AepService_ParentAepIsPaired():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9c141a9-1b4c-4f17-a9-d1-f2-98-53-8c-ad-b8'), pid=7)
def PKEY_Devices_AepService_ProtocolId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9c141a9-1b4c-4f17-a9-d1-f2-98-53-8c-ad-b8'), pid=5)
def PKEY_Devices_AepService_ServiceClassId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('71724756-3e74-4432-9b-59-e7-b2-f6-68-a5-93'), pid=3)
def PKEY_Devices_AepService_ServiceId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9c141a9-1b4c-4f17-a9-d1-f2-98-53-8c-ad-b8'), pid=2)
def PKEY_Devices_AppPackageFamilyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('51236583-0c4a-4fe8-b8-1f-16-6a-ec-13-f5-10'), pid=100)
def PKEY_Devices_AudioDevice_Microphone_IsFarField():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8943b373-388c-4395-b5-57-bc-6d-ba-ff-af-db'), pid=6)
def PKEY_Devices_AudioDevice_Microphone_SensitivityInDbfs():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8943b373-388c-4395-b5-57-bc-6d-ba-ff-af-db'), pid=3)
def PKEY_Devices_AudioDevice_Microphone_SensitivityInDbfs2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8943b373-388c-4395-b5-57-bc-6d-ba-ff-af-db'), pid=5)
def PKEY_Devices_AudioDevice_Microphone_SignalToNoiseRatioInDb():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8943b373-388c-4395-b5-57-bc-6d-ba-ff-af-db'), pid=4)
def PKEY_Devices_AudioDevice_RawProcessingSupported():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8943b373-388c-4395-b5-57-bc-6d-ba-ff-af-db'), pid=2)
def PKEY_Devices_AudioDevice_SpeechProcessingSupported():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fb1de864-e06d-47f4-82-a6-8a-0a-ef-44-49-3c'), pid=2)
def PKEY_Devices_BatteryLife():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=10)
def PKEY_Devices_BatteryPlusCharging():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=22)
def PKEY_Devices_BatteryPlusChargingText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=23)
def PKEY_Devices_Category():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=91)
def PKEY_Devices_CategoryGroup():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=94)
def PKEY_Devices_CategoryIds():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=90)
def PKEY_Devices_CategoryPlural():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=92)
def PKEY_Devices_ChallengeAep():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0774315e-b714-48ec-8d-e8-81-25-c0-77-ac-11'), pid=2)
def PKEY_Devices_ChargingState():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=11)
def PKEY_Devices_Children():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=9)
def PKEY_Devices_ClassGuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=10)
def PKEY_Devices_CompatibleIds():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=4)
def PKEY_Devices_Connected():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=55)
def PKEY_Devices_ContainerId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8c7ed206-3f8a-4827-b3-ab-ae-9e-1f-ae-fc-6c'), pid=2)
def PKEY_Devices_DefaultTooltip():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('880f70a2-6082-47ac-8a-ab-a7-39-d1-a3-00-c3'), pid=153)
def PKEY_Devices_DeviceCapabilities():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=17)
def PKEY_Devices_DeviceCharacteristics():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=29)
def PKEY_Devices_DeviceDescription1():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=81)
def PKEY_Devices_DeviceDescription2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=82)
def PKEY_Devices_DeviceHasProblem():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=6)
def PKEY_Devices_DeviceInstanceId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=256)
def PKEY_Devices_DeviceManufacturer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=13)
def PKEY_Devices_DevObjectType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('13673f42-a3d6-49f6-b4-da-ae-46-e0-c5-23-7c'), pid=2)
def PKEY_Devices_DialProtocol_InstalledApplications():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6845cc72-1b71-48c3-af-86-b0-91-71-a1-9b-14'), pid=3)
def PKEY_Devices_DiscoveryMethod():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=52)
def PKEY_Devices_Dnssd_Domain():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf79c0ab-bb74-4cee-b0-70-47-0b-5a-e2-02-ea'), pid=3)
def PKEY_Devices_Dnssd_FullName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf79c0ab-bb74-4cee-b0-70-47-0b-5a-e2-02-ea'), pid=5)
def PKEY_Devices_Dnssd_HostName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf79c0ab-bb74-4cee-b0-70-47-0b-5a-e2-02-ea'), pid=7)
def PKEY_Devices_Dnssd_InstanceName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf79c0ab-bb74-4cee-b0-70-47-0b-5a-e2-02-ea'), pid=4)
def PKEY_Devices_Dnssd_NetworkAdapterId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf79c0ab-bb74-4cee-b0-70-47-0b-5a-e2-02-ea'), pid=11)
def PKEY_Devices_Dnssd_PortNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf79c0ab-bb74-4cee-b0-70-47-0b-5a-e2-02-ea'), pid=12)
def PKEY_Devices_Dnssd_Priority():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf79c0ab-bb74-4cee-b0-70-47-0b-5a-e2-02-ea'), pid=9)
def PKEY_Devices_Dnssd_ServiceName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf79c0ab-bb74-4cee-b0-70-47-0b-5a-e2-02-ea'), pid=2)
def PKEY_Devices_Dnssd_TextAttributes():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf79c0ab-bb74-4cee-b0-70-47-0b-5a-e2-02-ea'), pid=6)
def PKEY_Devices_Dnssd_Ttl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf79c0ab-bb74-4cee-b0-70-47-0b-5a-e2-02-ea'), pid=10)
def PKEY_Devices_Dnssd_Weight():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bf79c0ab-bb74-4cee-b0-70-47-0b-5a-e2-02-ea'), pid=8)
def PKEY_Devices_FriendlyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12288)
def PKEY_Devices_FunctionPaths():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d08dd4c0-3a9e-462e-82-90-7b-63-6b-25-76-b9'), pid=3)
def PKEY_Devices_GlyphIcon():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('51236583-0c4a-4fe8-b8-1f-16-6a-ec-13-f5-10'), pid=123)
def PKEY_Devices_HardwareIds():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=3)
def PKEY_Devices_Icon():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=57)
def PKEY_Devices_InLocalMachineContainer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8c7ed206-3f8a-4827-b3-ab-ae-9e-1f-ae-fc-6c'), pid=4)
def PKEY_Devices_InterfaceClassGuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=4)
def PKEY_Devices_InterfaceEnabled():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=3)
def PKEY_Devices_InterfacePaths():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d08dd4c0-3a9e-462e-82-90-7b-63-6b-25-76-b9'), pid=2)
def PKEY_Devices_IpAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12297)
def PKEY_Devices_IsDefault():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=86)
def PKEY_Devices_IsNetworkConnected():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=85)
def PKEY_Devices_IsShared():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=84)
def PKEY_Devices_IsSoftwareInstalling():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=9)
def PKEY_Devices_LaunchDeviceStageFromExplorer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=77)
def PKEY_Devices_LocalMachine():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=70)
def PKEY_Devices_LocationPaths():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=37)
def PKEY_Devices_Manufacturer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8192)
def PKEY_Devices_MetadataPath():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=71)
def PKEY_Devices_MicrophoneArray_Geometry():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a1829ea2-27eb-459e-93-5d-b2-fa-d7-b0-77-62'), pid=2)
def PKEY_Devices_MissedCalls():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=5)
def PKEY_Devices_ModelId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=2)
def PKEY_Devices_ModelName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8194)
def PKEY_Devices_ModelNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8195)
def PKEY_Devices_NetworkedTooltip():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('880f70a2-6082-47ac-8a-ab-a7-39-d1-a3-00-c3'), pid=152)
def PKEY_Devices_NetworkName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=7)
def PKEY_Devices_NetworkType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=8)
def PKEY_Devices_NewPictures():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=4)
def PKEY_Devices_Notification():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('06704b0c-e830-4c81-91-78-91-e4-e9-5a-80-a0'), pid=3)
def PKEY_Devices_Notifications_LowBattery():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c4c07f2b-8524-4e66-ae-3a-a6-23-5f-10-3b-eb'), pid=2)
def PKEY_Devices_Notifications_MissedCall():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6614ef48-4efe-4424-9e-da-c7-9f-40-4e-df-3e'), pid=2)
def PKEY_Devices_Notifications_NewMessage():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2be9260a-2012-4742-a5-55-f4-1b-63-8b-7d-cb'), pid=2)
def PKEY_Devices_Notifications_NewVoicemail():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('59569556-0a08-4212-95-b9-fa-e2-ad-64-13-db'), pid=2)
def PKEY_Devices_Notifications_StorageFull():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a0e00ee1-f0c7-4d41-b8-e7-26-a7-bd-8d-38-b0'), pid=2)
def PKEY_Devices_Notifications_StorageFullLinkText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a0e00ee1-f0c7-4d41-b8-e7-26-a7-bd-8d-38-b0'), pid=3)
def PKEY_Devices_NotificationStore():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('06704b0c-e830-4c81-91-78-91-e4-e9-5a-80-a0'), pid=2)
def PKEY_Devices_NotWorkingProperly():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=83)
def PKEY_Devices_Paired():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=56)
def PKEY_Devices_Panel_PanelGroup():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8dbc9c86-97a9-4bff-9b-c6-bf-e9-5d-3e-6d-ad'), pid=3)
def PKEY_Devices_Panel_PanelId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8dbc9c86-97a9-4bff-9b-c6-bf-e9-5d-3e-6d-ad'), pid=2)
def PKEY_Devices_Parent():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=8)
def PKEY_Devices_PhoneLineTransportDevice_Connected():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('aecf2fe8-1d00-4fee-8a-6d-a7-0d-71-9b-77-2b'), pid=2)
def PKEY_Devices_PhysicalDeviceLocation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=9)
def PKEY_Devices_PlaybackPositionPercent():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3633de59-6825-4381-a4-9b-9f-6b-a1-3a-14-71'), pid=5)
def PKEY_Devices_PlaybackState():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3633de59-6825-4381-a4-9b-9f-6b-a1-3a-14-71'), pid=2)
PLAYBACKSTATE_UNKNOWN: UInt32 = 0
PLAYBACKSTATE_STOPPED: UInt32 = 1
PLAYBACKSTATE_PLAYING: UInt32 = 2
PLAYBACKSTATE_TRANSITIONING: UInt32 = 3
PLAYBACKSTATE_PAUSED: UInt32 = 4
PLAYBACKSTATE_RECORDINGPAUSED: UInt32 = 5
PLAYBACKSTATE_RECORDING: UInt32 = 6
PLAYBACKSTATE_NOMEDIA: UInt32 = 7
def PKEY_Devices_PlaybackTitle():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3633de59-6825-4381-a4-9b-9f-6b-a1-3a-14-71'), pid=3)
def PKEY_Devices_Present():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=5)
def PKEY_Devices_PresentationUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8198)
def PKEY_Devices_PrimaryCategory():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d08dd4c0-3a9e-462e-82-90-7b-63-6b-25-76-b9'), pid=10)
def PKEY_Devices_RemainingDuration():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3633de59-6825-4381-a4-9b-9f-6b-a1-3a-14-71'), pid=4)
def PKEY_Devices_RestrictedInterface():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=6)
def PKEY_Devices_Roaming():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=9)
def PKEY_Devices_SafeRemovalRequired():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afd97640-86a3-4210-b6-7c-28-9c-41-aa-be-55'), pid=2)
def PKEY_Devices_SchematicName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=9)
def PKEY_Devices_ServiceAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16384)
def PKEY_Devices_ServiceId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16385)
def PKEY_Devices_SharedTooltip():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('880f70a2-6082-47ac-8a-ab-a7-39-d1-a3-00-c3'), pid=151)
def PKEY_Devices_SignalStrength():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=2)
def PKEY_Devices_SmartCards_ReaderKind():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d6b5b883-18bd-4b4d-b2-ec-9e-38-af-fe-da-82'), pid=2)
def PKEY_Devices_Status():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d08dd4c0-3a9e-462e-82-90-7b-63-6b-25-76-b9'), pid=259)
def PKEY_Devices_Status1():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d08dd4c0-3a9e-462e-82-90-7b-63-6b-25-76-b9'), pid=257)
def PKEY_Devices_Status2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d08dd4c0-3a9e-462e-82-90-7b-63-6b-25-76-b9'), pid=258)
def PKEY_Devices_StorageCapacity():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=12)
def PKEY_Devices_StorageFreeSpace():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=13)
def PKEY_Devices_StorageFreeSpacePercent():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=14)
def PKEY_Devices_TextMessages():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=3)
def PKEY_Devices_Voicemail():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49cd1f76-5626-4b17-a4-e8-18-b4-aa-1a-22-13'), pid=6)
def PKEY_Devices_WiaDeviceType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6bdd1fc6-810f-11d0-be-c7-08-00-2b-e2-09-2f'), pid=2)
def PKEY_Devices_WiFi_InterfaceGuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1167eb-cbfc-4341-a5-68-a7-c9-1a-68-98-2c'), pid=2)
def PKEY_Devices_WiFiDirect_DeviceAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=13)
def PKEY_Devices_WiFiDirect_GroupId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=4)
def PKEY_Devices_WiFiDirect_InformationElements():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=12)
def PKEY_Devices_WiFiDirect_InterfaceAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=2)
def PKEY_Devices_WiFiDirect_InterfaceGuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=3)
def PKEY_Devices_WiFiDirect_IsConnected():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=5)
def PKEY_Devices_WiFiDirect_IsLegacyDevice():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=7)
def PKEY_Devices_WiFiDirect_IsMiracastLcpSupported():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=9)
def PKEY_Devices_WiFiDirect_IsVisible():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=6)
def PKEY_Devices_WiFiDirect_MiracastVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=8)
def PKEY_Devices_WiFiDirect_Services():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=10)
def PKEY_Devices_WiFiDirect_SupportedChannelList():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1506935d-e3e7-450f-86-37-82-23-3e-be-5f-6e'), pid=11)
def PKEY_Devices_WiFiDirectServices_AdvertisementId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('31b37743-7c5e-4005-93-e6-e9-53-f9-2b-82-e9'), pid=5)
def PKEY_Devices_WiFiDirectServices_RequestServiceInformation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('31b37743-7c5e-4005-93-e6-e9-53-f9-2b-82-e9'), pid=7)
def PKEY_Devices_WiFiDirectServices_ServiceAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('31b37743-7c5e-4005-93-e6-e9-53-f9-2b-82-e9'), pid=2)
def PKEY_Devices_WiFiDirectServices_ServiceConfigMethods():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('31b37743-7c5e-4005-93-e6-e9-53-f9-2b-82-e9'), pid=6)
def PKEY_Devices_WiFiDirectServices_ServiceInformation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('31b37743-7c5e-4005-93-e6-e9-53-f9-2b-82-e9'), pid=4)
def PKEY_Devices_WiFiDirectServices_ServiceName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('31b37743-7c5e-4005-93-e6-e9-53-f9-2b-82-e9'), pid=3)
def PKEY_Devices_WinPhone8CameraFlags():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7b4d61c-5a64-4187-a5-2e-b1-53-9f-35-90-99'), pid=2)
def PKEY_Devices_Wwan_InterfaceGuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ff1167eb-cbfc-4341-a5-68-a7-c9-1a-68-98-2c'), pid=2)
def PKEY_Storage_Portable():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d1ebee8-0803-4774-98-42-b7-7d-b5-02-65-e9'), pid=2)
def PKEY_Storage_RemovableMedia():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d1ebee8-0803-4774-98-42-b7-7d-b5-02-65-e9'), pid=3)
def PKEY_Storage_SystemCritical():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d1ebee8-0803-4774-98-42-b7-7d-b5-02-65-e9'), pid=4)
def PKEY_Document_ByteCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=4)
def PKEY_Document_CharacterCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=16)
def PKEY_Document_ClientID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('276d7bb0-5b34-4fb0-aa-4b-15-8e-d1-2a-18-09'), pid=100)
def PKEY_Document_Contributor():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f334115e-da1b-4509-9b-3d-11-95-04-dc-7a-bb'), pid=100)
def PKEY_Document_DateCreated():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=12)
def PKEY_Document_DatePrinted():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=11)
def PKEY_Document_DateSaved():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=13)
def PKEY_Document_Division():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1e005ee6-bf27-428b-b0-1c-79-67-6a-cd-28-70'), pid=100)
def PKEY_Document_DocumentID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e08805c8-e395-40df-80-d2-54-f0-d6-c4-31-54'), pid=100)
def PKEY_Document_HiddenSlideCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=9)
def PKEY_Document_LastAuthor():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=8)
def PKEY_Document_LineCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=5)
def PKEY_Document_Manager():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=14)
def PKEY_Document_MultimediaClipCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=10)
def PKEY_Document_NoteCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=8)
def PKEY_Document_PageCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=14)
def PKEY_Document_ParagraphCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=6)
def PKEY_Document_PresentationFormat():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=3)
def PKEY_Document_RevisionNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=9)
def PKEY_Document_Security():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=19)
def PKEY_Document_SlideCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=7)
def PKEY_Document_Template():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=7)
def PKEY_Document_TotalEditingTime():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=10)
def PKEY_Document_Version():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d5cdd502-2e9c-101b-93-97-08-00-2b-2c-f9-ae'), pid=29)
def PKEY_Document_WordCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f29f85e0-4ff9-1068-ab-91-08-00-2b-27-b3-d9'), pid=15)
def PKEY_DRM_DatePlayExpires():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('aeac19e4-89ae-4508-b9-b7-bb-86-7a-be-e2-ed'), pid=6)
def PKEY_DRM_DatePlayStarts():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('aeac19e4-89ae-4508-b9-b7-bb-86-7a-be-e2-ed'), pid=5)
def PKEY_DRM_Description():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('aeac19e4-89ae-4508-b9-b7-bb-86-7a-be-e2-ed'), pid=3)
def PKEY_DRM_IsDisabled():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('aeac19e4-89ae-4508-b9-b7-bb-86-7a-be-e2-ed'), pid=7)
def PKEY_DRM_IsProtected():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('aeac19e4-89ae-4508-b9-b7-bb-86-7a-be-e2-ed'), pid=2)
def PKEY_DRM_PlayCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('aeac19e4-89ae-4508-b9-b7-bb-86-7a-be-e2-ed'), pid=4)
def PKEY_GPS_Altitude():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('827edb4f-5b73-44a7-89-1d-fd-ff-ab-ea-35-ca'), pid=100)
def PKEY_GPS_AltitudeDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78342dcb-e358-4145-ae-9a-6b-fe-4e-0f-9f-51'), pid=100)
def PKEY_GPS_AltitudeNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2dad1eb7-816d-40d3-9e-c3-c9-77-3b-e2-aa-de'), pid=100)
def PKEY_GPS_AltitudeRef():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('46ac629d-75ea-4515-86-7f-6d-c4-32-1c-58-44'), pid=100)
def PKEY_GPS_AreaInformation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('972e333e-ac7e-49f1-8a-df-a7-0d-07-a9-bc-ab'), pid=100)
def PKEY_GPS_Date():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3602c812-0f3b-45f0-85-ad-60-34-68-d6-94-23'), pid=100)
def PKEY_GPS_DestBearing():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c66d4b3c-e888-47cc-b9-9f-9d-ca-3e-e3-4d-ea'), pid=100)
def PKEY_GPS_DestBearingDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7abcf4f8-7c3f-4988-ac-91-8d-2c-2e-97-ec-a5'), pid=100)
def PKEY_GPS_DestBearingNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ba3b1da9-86ee-4b5d-a2-a4-a2-71-a4-29-f0-cf'), pid=100)
def PKEY_GPS_DestBearingRef():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9ab84393-2a0f-4b75-bb-22-72-79-78-69-77-cb'), pid=100)
def PKEY_GPS_DestDistance():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a93eae04-6804-4f24-ac-81-09-b2-66-45-21-18'), pid=100)
def PKEY_GPS_DestDistanceDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9bc2c99b-ac71-4127-9d-1c-25-96-d0-d7-dc-b7'), pid=100)
def PKEY_GPS_DestDistanceNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2bda47da-08c6-4fe1-80-bc-a7-2f-c5-17-c5-d0'), pid=100)
def PKEY_GPS_DestDistanceRef():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ed4df2d3-8695-450b-85-6f-f5-c1-c5-3a-cb-66'), pid=100)
def PKEY_GPS_DestLatitude():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9d1d7cc5-5c39-451c-86-b3-92-8e-2d-18-cc-47'), pid=100)
def PKEY_GPS_DestLatitudeDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3a372292-7fca-49a7-99-d5-e4-7b-b2-d4-e7-ab'), pid=100)
def PKEY_GPS_DestLatitudeNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ecf4b6f6-d5a6-433c-bb-92-40-76-65-0f-c8-90'), pid=100)
def PKEY_GPS_DestLatitudeRef():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cea820b9-ce61-4885-a1-28-00-5d-90-87-c1-92'), pid=100)
def PKEY_GPS_DestLongitude():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('47a96261-cb4c-4807-8a-d3-40-b9-d9-db-c6-bc'), pid=100)
def PKEY_GPS_DestLongitudeDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('425d69e5-48ad-4900-8d-80-6e-b6-b8-d0-ac-86'), pid=100)
def PKEY_GPS_DestLongitudeNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a3250282-fb6d-48d5-9a-89-db-ca-ce-75-cc-cf'), pid=100)
def PKEY_GPS_DestLongitudeRef():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('182c1ea6-7c1c-4083-ab-4b-ac-6c-9f-4e-d1-28'), pid=100)
def PKEY_GPS_Differential():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('aaf4ee25-bd3b-4dd7-bf-c4-47-f7-7b-b0-0f-6d'), pid=100)
def PKEY_GPS_DOP():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cf8fb02-1837-42f1-a6-97-a7-01-7a-a2-89-b9'), pid=100)
def PKEY_GPS_DOPDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a0be94c5-50ba-487b-bd-35-06-54-be-88-81-ed'), pid=100)
def PKEY_GPS_DOPNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('47166b16-364f-4aa0-9f-31-e2-ab-3d-f4-49-c3'), pid=100)
def PKEY_GPS_ImgDirection():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('16473c91-d017-4ed9-ba-4d-b6-ba-a5-5d-bc-f8'), pid=100)
def PKEY_GPS_ImgDirectionDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10b24595-41a2-4e20-93-c2-57-61-c1-39-5f-32'), pid=100)
def PKEY_GPS_ImgDirectionNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('dc5877c7-225f-45f7-ba-c7-e8-13-34-b6-13-0a'), pid=100)
def PKEY_GPS_ImgDirectionRef():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a4aaa5b7-1ad0-445f-81-1a-0f-8f-6e-67-f6-b5'), pid=100)
def PKEY_GPS_Latitude():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8727cfff-4868-4ec6-ad-5b-81-b9-85-21-d1-ab'), pid=100)
def PKEY_GPS_LatitudeDecimal():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0f55cde2-4f49-450d-92-c1-dc-d1-63-01-b1-b7'), pid=100)
def PKEY_GPS_LatitudeDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('16e634ee-2bff-497b-bd-8a-43-41-ad-39-ee-b9'), pid=100)
def PKEY_GPS_LatitudeNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7ddaaad1-ccc8-41ae-b7-50-b2-cb-80-31-ae-a2'), pid=100)
def PKEY_GPS_LatitudeRef():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('029c0252-5b86-46c7-ac-a0-27-69-ff-c8-e3-d4'), pid=100)
def PKEY_GPS_Longitude():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c4c4dbb2-b593-466b-bb-da-d0-3d-27-d5-e4-3a'), pid=100)
def PKEY_GPS_LongitudeDecimal():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4679c1b5-844d-4590-ba-f5-f3-22-23-1f-1b-81'), pid=100)
def PKEY_GPS_LongitudeDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('be6e176c-4534-4d2c-ac-e5-31-de-da-c1-60-6b'), pid=100)
def PKEY_GPS_LongitudeNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('02b0f689-a914-4e45-82-1d-1d-da-45-2e-d2-c4'), pid=100)
def PKEY_GPS_LongitudeRef():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('33dcf22b-28d5-464c-80-35-1e-e9-ef-d2-52-78'), pid=100)
def PKEY_GPS_MapDatum():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ca2dae6-eddc-407d-be-f1-77-39-42-ab-fa-95'), pid=100)
def PKEY_GPS_MeasureMode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a015ed5d-aaea-4d58-8a-86-3c-58-69-20-ea-0b'), pid=100)
def PKEY_GPS_ProcessingMethod():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('59d49e61-840f-4aa9-a9-39-e2-09-9b-7f-63-99'), pid=100)
def PKEY_GPS_Satellites():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('467ee575-1f25-4557-ad-4e-b8-b5-8b-0d-9c-15'), pid=100)
def PKEY_GPS_Speed():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('da5d0862-6e76-4e1b-ba-bd-70-02-1b-d2-54-94'), pid=100)
def PKEY_GPS_SpeedDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7d122d5a-ae5e-4335-88-41-d7-1e-7c-e7-2f-53'), pid=100)
def PKEY_GPS_SpeedNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('acc9ce3d-c213-4942-8b-48-6d-08-20-f2-1c-6d'), pid=100)
def PKEY_GPS_SpeedRef():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ecf7f4c9-544f-4d6d-9d-98-8a-d7-9a-da-f4-53'), pid=100)
def PKEY_GPS_Status():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('125491f4-818f-46b2-91-b5-d5-37-75-36-17-b2'), pid=100)
def PKEY_GPS_Track():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('76c09943-7c33-49e3-9e-7e-cd-ba-87-2c-fa-da'), pid=100)
def PKEY_GPS_TrackDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c8d1920c-01f6-40c0-ac-86-2f-3a-4a-d0-07-70'), pid=100)
def PKEY_GPS_TrackNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('702926f4-44a6-43e1-ae-71-45-62-71-16-89-3b'), pid=100)
def PKEY_GPS_TrackRef():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('35dbe6fe-44c3-4400-aa-ae-d2-c7-99-c4-07-e8'), pid=100)
def PKEY_GPS_VersionID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('22704da4-c6b2-4a99-8e-56-f1-6d-f8-c9-25-99'), pid=100)
def PKEY_History_VisitCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5cbf2787-48cf-4208-b9-0e-ee-5e-5d-42-02-94'), pid=7)
def PKEY_Image_BitDepth():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6444048f-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=7)
def PKEY_Image_ColorSpace():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=40961)
def PKEY_Image_CompressedBitsPerPixel():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('364b6fa9-37ab-482a-be-2b-ae-02-f6-0d-43-18'), pid=100)
def PKEY_Image_CompressedBitsPerPixelDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1f8844e1-24ad-4508-9d-fd-53-26-a4-15-ce-02'), pid=100)
def PKEY_Image_CompressedBitsPerPixelNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d21a7148-d32c-4624-89-00-27-72-10-f7-9c-0f'), pid=100)
def PKEY_Image_Compression():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=259)
def PKEY_Image_CompressionText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f08e66f-2f44-4bb9-a6-82-ac-35-d2-56-23-22'), pid=100)
def PKEY_Image_Dimensions():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6444048f-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=13)
def PKEY_Image_HorizontalResolution():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6444048f-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=5)
def PKEY_Image_HorizontalSize():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6444048f-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=3)
def PKEY_Image_ImageID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10dabe05-32aa-4c29-bf-1a-63-e2-d2-20-58-7f'), pid=100)
def PKEY_Image_ResolutionUnit():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('19b51fa6-1f92-4a5c-ab-48-7d-f0-ab-d6-74-44'), pid=100)
def PKEY_Image_VerticalResolution():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6444048f-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=6)
def PKEY_Image_VerticalSize():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6444048f-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=4)
def PKEY_Journal_Contacts():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('dea7c82c-1d89-4a66-94-27-a4-e3-de-ba-bc-b1'), pid=100)
def PKEY_Journal_EntryType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('95beb1fc-326d-4644-b3-96-cd-3e-d9-0e-6d-df'), pid=100)
def PKEY_LayoutPattern_ContentViewModeForBrowse():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=500)
LAYOUTPATTERN_CVMFB_ALPHA: String = 'alpha'
LAYOUTPATTERN_CVMFB_BETA: String = 'beta'
LAYOUTPATTERN_CVMFB_GAMMA: String = 'gamma'
LAYOUTPATTERN_CVMFB_DELTA: String = 'delta'
def PKEY_LayoutPattern_ContentViewModeForSearch():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=501)
LAYOUTPATTERN_CVMFS_ALPHA: String = 'alpha'
LAYOUTPATTERN_CVMFS_BETA: String = 'beta'
LAYOUTPATTERN_CVMFS_GAMMA: String = 'gamma'
LAYOUTPATTERN_CVMFS_DELTA: String = 'delta'
def PKEY_History_SelectionCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1ce0d6bc-536c-4600-b0-dd-7e-0c-66-b3-50-d5'), pid=8)
def PKEY_History_TargetUrlHostName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1ce0d6bc-536c-4600-b0-dd-7e-0c-66-b3-50-d5'), pid=9)
def PKEY_Link_Arguments():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('436f2667-14e2-4feb-b3-0a-14-6c-53-b5-b6-74'), pid=100)
def PKEY_Link_Comment():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b9b4b3fc-2b51-4a42-b5-d8-32-41-46-af-cf-25'), pid=5)
def PKEY_Link_DateVisited():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5cbf2787-48cf-4208-b9-0e-ee-5e-5d-42-02-94'), pid=23)
def PKEY_Link_Description():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5cbf2787-48cf-4208-b9-0e-ee-5e-5d-42-02-94'), pid=21)
def PKEY_Link_FeedItemLocalId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8a2f99f9-3c37-465d-a8-d7-69-77-7a-24-6d-0c'), pid=2)
def PKEY_Link_Status():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b9b4b3fc-2b51-4a42-b5-d8-32-41-46-af-cf-25'), pid=3)
LINK_STATUS_RESOLVED: Int32 = 1
LINK_STATUS_BROKEN: Int32 = 2
def PKEY_Link_TargetExtension():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7a7d76f4-b630-4bd7-95-ff-37-cc-51-a9-75-c9'), pid=2)
def PKEY_Link_TargetParsingPath():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b9b4b3fc-2b51-4a42-b5-d8-32-41-46-af-cf-25'), pid=2)
def PKEY_Link_TargetSFGAOFlags():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b9b4b3fc-2b51-4a42-b5-d8-32-41-46-af-cf-25'), pid=8)
def PKEY_Link_TargetUrlHostName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8a2f99f9-3c37-465d-a8-d7-69-77-7a-24-6d-0c'), pid=5)
def PKEY_Link_TargetUrlPath():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8a2f99f9-3c37-465d-a8-d7-69-77-7a-24-6d-0c'), pid=6)
def PKEY_Media_AuthorUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=32)
def PKEY_Media_AverageLevel():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('09edd5b6-b301-43c5-99-90-d0-03-02-ef-fd-46'), pid=100)
def PKEY_Media_ClassPrimaryID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=13)
def PKEY_Media_ClassSecondaryID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=14)
def PKEY_Media_CollectionGroupID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=24)
def PKEY_Media_CollectionID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=25)
def PKEY_Media_ContentDistributor():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=18)
def PKEY_Media_ContentID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=26)
def PKEY_Media_CreatorApplication():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=27)
def PKEY_Media_CreatorApplicationVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=28)
def PKEY_Media_DateEncoded():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2e4b640d-5019-46d8-88-81-55-41-4c-c5-ca-a0'), pid=100)
def PKEY_Media_DateReleased():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('de41cc29-6971-4290-b4-72-f5-9f-2e-2f-31-e2'), pid=100)
def PKEY_Media_DlnaProfileID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cfa31b45-525d-4998-bb-44-3f-7d-81-54-2f-a4'), pid=100)
def PKEY_Media_Duration():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440490-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=3)
def PKEY_Media_DVDID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=15)
def PKEY_Media_EncodedBy():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=36)
def PKEY_Media_EncodingSettings():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=37)
def PKEY_Media_EpisodeNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=100)
def PKEY_Media_FrameCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6444048f-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=12)
def PKEY_Media_MCDI():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=16)
def PKEY_Media_MetadataContentProvider():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=17)
def PKEY_Media_Producer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=22)
def PKEY_Media_PromotionUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=33)
def PKEY_Media_ProtectionType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=38)
def PKEY_Media_ProviderRating():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=39)
def PKEY_Media_ProviderStyle():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=40)
def PKEY_Media_Publisher():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=30)
def PKEY_Media_SeasonNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=101)
def PKEY_Media_SeriesName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=42)
def PKEY_Media_SubscriptionContentId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9aebae7a-9644-487d-a9-2c-65-75-85-ed-75-1a'), pid=100)
def PKEY_Media_SubTitle():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=38)
def PKEY_Media_ThumbnailLargePath():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=47)
def PKEY_Media_ThumbnailLargeUri():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=48)
def PKEY_Media_ThumbnailSmallPath():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=49)
def PKEY_Media_ThumbnailSmallUri():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=50)
def PKEY_Media_UniqueFileIdentifier():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=35)
def PKEY_Media_UserNoAutoInfo():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=41)
def PKEY_Media_UserWebUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=34)
def PKEY_Media_Writer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=23)
def PKEY_Media_Year():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=5)
def PKEY_Message_AttachmentContents():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3143bf7c-80a8-4854-88-80-e2-e4-01-89-bd-d0'), pid=100)
def PKEY_Message_AttachmentNames():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=21)
def PKEY_Message_BccAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=2)
def PKEY_Message_BccName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=3)
def PKEY_Message_CcAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=4)
def PKEY_Message_CcName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=5)
def PKEY_Message_ConversationID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('dc8f80bd-af1e-4289-85-b6-3d-fc-1b-49-39-92'), pid=100)
def PKEY_Message_ConversationIndex():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('dc8f80bd-af1e-4289-85-b6-3d-fc-1b-49-39-92'), pid=101)
def PKEY_Message_DateReceived():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=20)
def PKEY_Message_DateSent():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=19)
def PKEY_Message_Flags():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a82d9ee7-ca67-4312-96-5e-22-6b-ce-a8-50-23'), pid=100)
def PKEY_Message_FromAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=13)
def PKEY_Message_FromName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=14)
def PKEY_Message_HasAttachments():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9c1fcf74-2d97-41ba-b4-ae-cb-2e-36-61-a6-e4'), pid=8)
def PKEY_Message_IsFwdOrReply():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9a9bc088-4f6d-469e-99-19-e7-05-41-20-40-f9'), pid=100)
def PKEY_Message_MessageClass():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cd9ed458-08ce-418f-a7-0e-f9-12-c7-bb-9c-5c'), pid=103)
def PKEY_Message_Participants():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1a9ba605-8e7c-4d11-ad-7d-a5-0a-da-18-ba-1b'), pid=2)
def PKEY_Message_ProofInProgress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9098f33c-9a7d-48a8-8d-e5-2e-12-27-a6-4e-91'), pid=100)
def PKEY_Message_SenderAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0be1c8e7-1981-4676-ae-14-fd-d7-8f-05-a6-e7'), pid=100)
def PKEY_Message_SenderName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0da41cfa-d224-4a18-ae-2f-59-61-58-db-4b-3a'), pid=100)
def PKEY_Message_Store():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=15)
def PKEY_Message_ToAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=16)
def PKEY_Message_ToDoFlags():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1f856a9f-6900-4aba-95-05-2d-5f-1b-4d-66-cb'), pid=100)
def PKEY_Message_ToDoTitle():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bccc8a3c-8cef-42e5-9b-1c-c6-90-79-39-8b-c7'), pid=100)
def PKEY_Message_ToName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3e0584c-b788-4a5a-bb-20-7f-5a-44-c9-ac-dd'), pid=17)
def PKEY_Music_AlbumArtist():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=13)
def PKEY_Music_AlbumArtistSortOverride():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f1fdb4af-f78c-466c-bb-05-56-e9-2d-b0-b8-ec'), pid=103)
def PKEY_Music_AlbumID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=100)
def PKEY_Music_AlbumTitle():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=4)
def PKEY_Music_AlbumTitleSortOverride():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('13eb7ffc-ec89-4346-b1-9d-cc-c6-f1-78-42-23'), pid=101)
def PKEY_Music_Artist():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=2)
def PKEY_Music_ArtistSortOverride():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('deeb2db5-0696-4ce0-94-fe-a0-1f-77-a4-5f-b5'), pid=102)
def PKEY_Music_BeatsPerMinute():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=35)
def PKEY_Music_Composer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=19)
def PKEY_Music_ComposerSortOverride():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00bc20a3-bd48-4085-87-2c-a8-8d-77-f5-09-7e'), pid=105)
def PKEY_Music_Conductor():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=36)
def PKEY_Music_ContentGroupDescription():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=33)
def PKEY_Music_DiscNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6afe7437-9bcd-49c7-80-fe-4a-5c-65-fa-58-74'), pid=104)
def PKEY_Music_DisplayArtist():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fd122953-fa93-4ef7-92-c3-04-c9-46-b2-f7-c8'), pid=100)
def PKEY_Music_Genre():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=11)
def PKEY_Music_InitialKey():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=34)
def PKEY_Music_IsCompilation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c449d5cb-9ea4-4809-82-e8-af-9d-59-de-d6-d1'), pid=100)
def PKEY_Music_Lyrics():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=12)
def PKEY_Music_Mood():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=39)
def PKEY_Music_PartOfSet():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=37)
def PKEY_Music_Period():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=31)
def PKEY_Music_SynchronizedLyrics():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6b223b6a-162e-4aa9-b3-9f-05-d6-78-fc-6d-77'), pid=100)
def PKEY_Music_TrackNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6'), pid=7)
def PKEY_Note_Color():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4776cafa-bce4-4cb1-a2-3e-26-5e-76-d8-eb-11'), pid=100)
def PKEY_Note_ColorText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('46b4e8de-cdb2-440d-88-5c-16-58-eb-65-b9-14'), pid=100)
def PKEY_Photo_Aperture():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=37378)
def PKEY_Photo_ApertureDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e1a9a38b-6685-46bd-87-5e-57-0d-c7-ad-73-20'), pid=100)
def PKEY_Photo_ApertureNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0337ecec-39fb-4581-a0-bd-4c-4c-c5-1e-99-14'), pid=100)
def PKEY_Photo_Brightness():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1a701bf6-478c-4361-83-ab-37-01-bb-05-3c-58'), pid=100)
def PKEY_Photo_BrightnessDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6ebe6946-2321-440a-90-f0-c0-43-ef-d3-24-76'), pid=100)
def PKEY_Photo_BrightnessNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e7d118f-b314-45a0-8c-fb-d6-54-b9-17-c9-e9'), pid=100)
def PKEY_Photo_CameraManufacturer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=271)
def PKEY_Photo_CameraModel():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=272)
def PKEY_Photo_CameraSerialNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=273)
def PKEY_Photo_Contrast():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2a785ba9-8d23-4ded-82-e6-60-a3-50-c8-6a-10'), pid=100)
PHOTO_CONTRAST_NORMAL: UInt32 = 0
PHOTO_CONTRAST_SOFT: UInt32 = 1
PHOTO_CONTRAST_HARD: UInt32 = 2
def PKEY_Photo_ContrastText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('59dde9f2-5253-40ea-9a-8b-47-9e-96-c6-24-9a'), pid=100)
def PKEY_Photo_DateTaken():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=36867)
def PKEY_Photo_DigitalZoom():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f85bf840-a925-4bc2-b0-c4-8e-36-b5-98-67-9e'), pid=100)
def PKEY_Photo_DigitalZoomDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('745baf0e-e5c1-4cfb-8a-1b-d0-31-a0-a5-23-93'), pid=100)
def PKEY_Photo_DigitalZoomNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('16cbb924-6500-473b-a5-be-f1-59-9b-cb-e4-13'), pid=100)
def PKEY_Photo_Event():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=18248)
def PKEY_Photo_EXIFVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d35f743a-eb2e-47f2-a2-86-84-41-32-cb-14-27'), pid=100)
def PKEY_Photo_ExposureBias():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=37380)
def PKEY_Photo_ExposureBiasDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab205e50-04b7-461c-a1-8c-2f-23-38-36-e6-27'), pid=100)
def PKEY_Photo_ExposureBiasNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('738bf284-1d87-420b-92-cf-58-34-bf-6e-f9-ed'), pid=100)
def PKEY_Photo_ExposureIndex():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('967b5af8-995a-46ed-9e-11-35-b3-c5-b9-78-2d'), pid=100)
def PKEY_Photo_ExposureIndexDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('93112f89-c28b-492f-8a-9d-4b-e2-06-2c-ee-8a'), pid=100)
def PKEY_Photo_ExposureIndexNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cdedcf30-8919-44df-8f-4c-4e-b2-ff-db-8d-89'), pid=100)
def PKEY_Photo_ExposureProgram():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=34850)
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
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fec690b7-5f30-4646-ae-47-4c-aa-fb-a8-84-a3'), pid=100)
def PKEY_Photo_ExposureTime():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=33434)
def PKEY_Photo_ExposureTimeDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('55e98597-ad16-42e0-b6-24-21-59-9a-19-98-38'), pid=100)
def PKEY_Photo_ExposureTimeNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('257e44e2-9031-4323-ac-38-85-c5-52-87-1b-2e'), pid=100)
def PKEY_Photo_Flash():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=37385)
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
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=41483)
def PKEY_Photo_FlashEnergyDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d7b61c70-6323-49cd-a5-fc-c8-42-77-16-2c-97'), pid=100)
def PKEY_Photo_FlashEnergyNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fcad3d3d-0858-400f-aa-a3-2f-66-cc-e2-a6-bc'), pid=100)
def PKEY_Photo_FlashManufacturer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('aabaf6c9-e0c5-4719-85-85-57-b1-03-e5-84-fe'), pid=100)
def PKEY_Photo_FlashModel():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fe83bb35-4d1a-42e2-91-6b-06-f3-e1-af-71-9e'), pid=100)
def PKEY_Photo_FlashText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6b8b68f6-200b-47ea-8d-25-d8-05-0f-57-33-9f'), pid=100)
def PKEY_Photo_FNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=33437)
def PKEY_Photo_FNumberDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e92a2496-223b-4463-a4-e3-30-ea-bb-a7-9d-80'), pid=100)
def PKEY_Photo_FNumberNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1b97738a-fdfc-462f-9d-93-19-57-e0-8b-e9-0c'), pid=100)
def PKEY_Photo_FocalLength():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=37386)
def PKEY_Photo_FocalLengthDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('305bc615-dca1-44a5-9f-d4-10-c0-ba-79-41-2e'), pid=100)
def PKEY_Photo_FocalLengthInFilm():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a0e74609-b84d-4f49-b8-60-46-2b-d9-97-1f-98'), pid=100)
def PKEY_Photo_FocalLengthNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('776b6b3b-1e3d-4b0c-9a-0e-8f-ba-f2-a8-49-2a'), pid=100)
def PKEY_Photo_FocalPlaneXResolution():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cfc08d97-c6f7-4484-89-dd-eb-ef-43-56-fe-76'), pid=100)
def PKEY_Photo_FocalPlaneXResolutionDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0933f3f5-4786-4f46-a8-e8-d6-4d-d3-7f-a5-21'), pid=100)
def PKEY_Photo_FocalPlaneXResolutionNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('dccb10af-b4e2-4b88-95-f9-03-1b-4d-5a-b4-90'), pid=100)
def PKEY_Photo_FocalPlaneYResolution():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4fffe4d0-914f-4ac4-8d-6f-c9-c6-1d-e1-69-b1'), pid=100)
def PKEY_Photo_FocalPlaneYResolutionDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1d6179a6-a876-4031-b0-13-33-47-b2-b6-4d-c8'), pid=100)
def PKEY_Photo_FocalPlaneYResolutionNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a2e541c5-4440-4ba8-86-7e-75-cf-c0-68-28-cd'), pid=100)
def PKEY_Photo_GainControl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fa304789-00c7-4d80-90-4a-1e-4d-cc-72-65-aa'), pid=100)
PHOTO_GAINCONTROL_NONE: Double = 0
PHOTO_GAINCONTROL_LOWGAINUP: Double = 1
PHOTO_GAINCONTROL_HIGHGAINUP: Double = 2
PHOTO_GAINCONTROL_LOWGAINDOWN: Double = 3
PHOTO_GAINCONTROL_HIGHGAINDOWN: Double = 4
def PKEY_Photo_GainControlDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('42864dfd-9da4-4f77-bd-ed-4a-ad-7b-25-67-35'), pid=100)
def PKEY_Photo_GainControlNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8e8ecf7c-b7b8-4eb8-a6-3f-0e-e7-15-c9-6f-9e'), pid=100)
def PKEY_Photo_GainControlText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c06238b2-0bf9-4279-a7-23-25-85-67-15-cb-9d'), pid=100)
def PKEY_Photo_ISOSpeed():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=34855)
def PKEY_Photo_LensManufacturer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6ddcaf7-29c5-4f0a-9a-68-d1-94-12-ec-70-90'), pid=100)
def PKEY_Photo_LensModel():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e1277516-2b5f-4869-89-b1-2e-58-5b-d3-8b-7a'), pid=100)
def PKEY_Photo_LightSource():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=37384)
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
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fa303353-b659-4052-85-e9-bc-ac-79-54-9b-84'), pid=100)
def PKEY_Photo_MakerNoteOffset():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('813f4124-34e6-4d17-ab-3e-6b-1f-3c-22-47-a1'), pid=100)
def PKEY_Photo_MaxAperture():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('08f6d7c2-e3f2-44fc-af-1e-5a-a5-c8-1a-2d-3e'), pid=100)
def PKEY_Photo_MaxApertureDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c77724d4-601f-46c5-9b-89-c5-3f-93-bc-eb-77'), pid=100)
def PKEY_Photo_MaxApertureNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c107e191-a459-44c5-9a-e6-b9-52-ad-4b-90-6d'), pid=100)
def PKEY_Photo_MeteringMode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=37383)
def PKEY_Photo_MeteringModeText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f628fd8c-7ba8-465a-a6-5b-c5-aa-79-26-3a-9e'), pid=100)
def PKEY_Photo_Orientation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=274)
def PKEY_Photo_OrientationText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a9ea193c-c511-498a-a0-6b-58-e2-77-6d-cc-28'), pid=100)
def PKEY_Photo_PeopleNames():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e8309b6e-084c-49b4-b1-fc-90-a8-03-31-b6-38'), pid=100)
def PKEY_Photo_PhotometricInterpretation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('341796f1-1df9-4b1c-a5-64-91-bd-ef-a4-38-77'), pid=100)
def PKEY_Photo_PhotometricInterpretationText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('821437d6-9eab-4765-a5-89-3b-1c-bb-d2-2a-61'), pid=100)
def PKEY_Photo_ProgramMode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d217f6d-3f6a-4825-b4-70-5f-03-ca-2f-be-9b'), pid=100)
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
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7fe3aa27-2648-42f3-89-b0-45-4e-5c-b1-50-c3'), pid=100)
def PKEY_Photo_RelatedSoundFile():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('318a6b45-087f-4dc2-b8-cc-05-35-95-51-fc-9e'), pid=100)
def PKEY_Photo_Saturation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49237325-a95a-4f67-b2-11-81-6b-2d-45-d2-e0'), pid=100)
PHOTO_SATURATION_NORMAL: UInt32 = 0
PHOTO_SATURATION_LOW: UInt32 = 1
PHOTO_SATURATION_HIGH: UInt32 = 2
def PKEY_Photo_SaturationText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('61478c08-b600-4a84-bb-e4-e9-9c-45-f0-a0-72'), pid=100)
def PKEY_Photo_Sharpness():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fc6976db-8349-4970-ae-97-b3-c5-31-6a-08-f0'), pid=100)
PHOTO_SHARPNESS_NORMAL: UInt32 = 0
PHOTO_SHARPNESS_SOFT: UInt32 = 1
PHOTO_SHARPNESS_HARD: UInt32 = 2
def PKEY_Photo_SharpnessText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('51ec3f47-dd50-421d-87-69-33-4f-50-42-4b-1e'), pid=100)
def PKEY_Photo_ShutterSpeed():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=37377)
def PKEY_Photo_ShutterSpeedDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e13d8975-81c7-4948-ae-3f-37-ca-e1-1e-8f-f7'), pid=100)
def PKEY_Photo_ShutterSpeedNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('16ea4042-d6f4-4bca-83-49-7c-78-d3-0f-b3-33'), pid=100)
def PKEY_Photo_SubjectDistance():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99'), pid=37382)
def PKEY_Photo_SubjectDistanceDenominator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0c840a88-b043-466d-97-66-d4-b2-6d-a3-fa-77'), pid=100)
def PKEY_Photo_SubjectDistanceNumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8af4961c-f526-43e5-aa-81-db-76-82-19-17-8d'), pid=100)
def PKEY_Photo_TagViewAggregate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b812f15d-c2d8-4bbf-ba-cd-79-74-43-46-11-3f'), pid=100)
def PKEY_Photo_TranscodedForSync():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9a8ebb75-6458-4e82-ba-cb-35-c0-09-5b-03-bb'), pid=100)
def PKEY_Photo_WhiteBalance():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ee3d3d8a-5381-4cfa-b1-3b-aa-f6-6b-5f-4e-c9'), pid=100)
PHOTO_WHITEBALANCE_AUTO: UInt32 = 0
PHOTO_WHITEBALANCE_MANUAL: UInt32 = 1
def PKEY_Photo_WhiteBalanceText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6336b95e-c7a7-426d-86-fd-7a-e3-d3-9c-84-b4'), pid=100)
def PKEY_PropGroup_Advanced():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('900a403b-097b-4b95-8a-e2-07-1f-da-ee-b1-18'), pid=100)
def PKEY_PropGroup_Audio():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2804d469-788f-48aa-85-70-71-b9-c1-87-e1-38'), pid=100)
def PKEY_PropGroup_Calendar():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9973d2b5-bfd8-438a-ba-94-53-49-b2-93-18-1a'), pid=100)
def PKEY_PropGroup_Camera():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('de00de32-547e-4981-ad-4b-54-2f-2e-90-07-d8'), pid=100)
def PKEY_PropGroup_Contact():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('df975fd3-250a-4004-85-8f-34-e2-9a-3e-37-aa'), pid=100)
def PKEY_PropGroup_Content():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d0dab0ba-368a-4050-a8-82-6c-01-0f-d1-9a-4f'), pid=100)
def PKEY_PropGroup_Description():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8969b275-9475-4e00-a8-87-ff-93-b8-b4-1e-44'), pid=100)
def PKEY_PropGroup_FileSystem():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3a7d2c1-80fc-4b40-8f-34-30-ea-11-1b-dc-2e'), pid=100)
def PKEY_PropGroup_General():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cc301630-b192-4c22-b3-72-9f-4c-6d-33-8e-07'), pid=100)
def PKEY_PropGroup_GPS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f3713ada-90e3-4e11-aa-e5-fd-c1-76-85-b9-be'), pid=100)
def PKEY_PropGroup_Image():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e3690a87-0fa8-4a2a-9a-9f-fc-e8-82-70-55-ac'), pid=100)
def PKEY_PropGroup_Media():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('61872cf7-6b5e-4b4b-ac-2d-59-da-84-45-92-48'), pid=100)
def PKEY_PropGroup_MediaAdvanced():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8859a284-de7e-4642-99-ba-d4-31-d0-44-b1-ec'), pid=100)
def PKEY_PropGroup_Message():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7fd7259d-16b4-4135-9f-97-7c-96-ec-d2-fa-9e'), pid=100)
def PKEY_PropGroup_Music():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('68dd6094-7216-40f1-a0-29-43-fe-71-27-04-3f'), pid=100)
def PKEY_PropGroup_Origin():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2598d2fb-5569-4367-95-df-5c-d3-a1-77-e1-a5'), pid=100)
def PKEY_PropGroup_PhotoAdvanced():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cb2bf5a-9ee7-4a86-82-22-f0-1e-07-fd-ad-af'), pid=100)
def PKEY_PropGroup_RecordedTV():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e7b33238-6584-4170-a5-c0-ac-25-ef-d9-da-56'), pid=100)
def PKEY_PropGroup_Video():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bebe0920-7671-4c54-a3-eb-49-fd-df-c1-91-ee'), pid=100)
def PKEY_InfoTipText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=17)
def PKEY_PropList_ConflictPrompt():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=11)
def PKEY_PropList_ContentViewModeForBrowse():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=13)
def PKEY_PropList_ContentViewModeForSearch():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=14)
def PKEY_PropList_ExtendedTileInfo():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=9)
def PKEY_PropList_FileOperationPrompt():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=10)
def PKEY_PropList_FullDetails():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=2)
def PKEY_PropList_InfoTip():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=4)
def PKEY_PropList_NonPersonal():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49d1091f-082e-493f-b2-3f-d2-30-8a-a9-66-8c'), pid=100)
def PKEY_PropList_PreviewDetails():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=8)
def PKEY_PropList_PreviewTitle():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=6)
def PKEY_PropList_QuickTip():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=5)
def PKEY_PropList_TileInfo():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c9944a21-a406-48fe-82-25-ae-c7-e2-4c-21-1b'), pid=3)
def PKEY_PropList_XPDetailsPanel():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f2275480-f782-4291-bd-94-f1-36-93-51-3a-ec'), pid=0)
def PKEY_RecordedTV_ChannelNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=7)
def PKEY_RecordedTV_Credits():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=4)
def PKEY_RecordedTV_DateContentExpires():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=15)
def PKEY_RecordedTV_EpisodeName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=2)
def PKEY_RecordedTV_IsATSCContent():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=16)
def PKEY_RecordedTV_IsClosedCaptioningAvailable():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=12)
def PKEY_RecordedTV_IsDTVContent():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=17)
def PKEY_RecordedTV_IsHDContent():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=18)
def PKEY_RecordedTV_IsRepeatBroadcast():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=13)
def PKEY_RecordedTV_IsSAP():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=14)
def PKEY_RecordedTV_NetworkAffiliation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2c53c813-fb63-4e22-a1-ab-0b-33-1c-a1-e2-73'), pid=100)
def PKEY_RecordedTV_OriginalBroadcastDate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4684fe97-8765-4842-9c-13-f0-06-44-7b-17-8c'), pid=100)
def PKEY_RecordedTV_ProgramDescription():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=3)
def PKEY_RecordedTV_RecordingTime():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a5477f61-7a82-4eca-9d-de-98-b6-9b-24-79-b3'), pid=100)
def PKEY_RecordedTV_StationCallSign():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6d748de2-8d38-4cc3-ac-60-f0-09-b0-57-c5-57'), pid=5)
def PKEY_RecordedTV_StationName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1b5439e7-eba1-4af8-bd-d7-7a-f1-d4-54-94-93'), pid=100)
def PKEY_Search_AutoSummary():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('560c36c0-503a-11cf-ba-a1-00-00-4c-75-2a-9a'), pid=2)
def PKEY_Search_ContainerHash():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bceee283-35df-4d53-82-6a-f3-6a-3e-ef-c6-be'), pid=100)
def PKEY_Search_Contents():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=19)
def PKEY_Search_EntryID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49691c90-7e17-101a-a9-1c-08-00-2b-2e-cd-a9'), pid=5)
def PKEY_Search_ExtendedProperties():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7b03b546-fa4f-4a52-a2-fe-03-d5-31-1e-58-65'), pid=100)
def PKEY_Search_GatherTime():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0b63e350-9ccc-11d0-bc-db-00-80-5f-cc-ce-04'), pid=8)
def PKEY_Search_HitCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49691c90-7e17-101a-a9-1c-08-00-2b-2e-cd-a9'), pid=4)
def PKEY_Search_IsClosedDirectory():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0b63e343-9ccc-11d0-bc-db-00-80-5f-cc-ce-04'), pid=23)
def PKEY_Search_IsFullyContained():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0b63e343-9ccc-11d0-bc-db-00-80-5f-cc-ce-04'), pid=24)
def PKEY_Search_QueryFocusedSummary():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('560c36c0-503a-11cf-ba-a1-00-00-4c-75-2a-9a'), pid=3)
def PKEY_Search_QueryFocusedSummaryWithFallback():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('560c36c0-503a-11cf-ba-a1-00-00-4c-75-2a-9a'), pid=4)
def PKEY_Search_QueryPropertyHits():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49691c90-7e17-101a-a9-1c-08-00-2b-2e-cd-a9'), pid=21)
def PKEY_Search_Rank():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('49691c90-7e17-101a-a9-1c-08-00-2b-2e-cd-a9'), pid=3)
def PKEY_Search_Store():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a06992b3-8caf-4ed7-a5-47-b2-59-e3-2a-c9-fc'), pid=100)
def PKEY_Search_UrlToIndex():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0b63e343-9ccc-11d0-bc-db-00-80-5f-cc-ce-04'), pid=2)
def PKEY_Search_UrlToIndexWithModificationTime():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0b63e343-9ccc-11d0-bc-db-00-80-5f-cc-ce-04'), pid=12)
def PKEY_Supplemental_Album():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0c73b141-39d6-4653-a6-83-ca-b2-91-ea-f9-5b'), pid=6)
def PKEY_Supplemental_AlbumID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0c73b141-39d6-4653-a6-83-ca-b2-91-ea-f9-5b'), pid=2)
def PKEY_Supplemental_Location():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0c73b141-39d6-4653-a6-83-ca-b2-91-ea-f9-5b'), pid=5)
def PKEY_Supplemental_Person():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0c73b141-39d6-4653-a6-83-ca-b2-91-ea-f9-5b'), pid=7)
def PKEY_Supplemental_ResourceId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0c73b141-39d6-4653-a6-83-ca-b2-91-ea-f9-5b'), pid=3)
def PKEY_Supplemental_Tag():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0c73b141-39d6-4653-a6-83-ca-b2-91-ea-f9-5b'), pid=4)
def PKEY_DescriptionID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=2)
def PKEY_InternalName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cef7d53-fa64-11d1-a2-03-00-00-f8-1f-ed-ee'), pid=5)
def PKEY_LibraryLocationsCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('908696c7-8f87-44f2-80-ed-a8-c1-c6-89-45-75'), pid=2)
def PKEY_Link_TargetSFGAOFlagsStrings():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d6942081-d53b-443d-ad-47-5e-05-9d-9c-d2-7a'), pid=3)
def PKEY_Link_TargetUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5cbf2787-48cf-4208-b9-0e-ee-5e-5d-42-02-94'), pid=2)
def PKEY_NamespaceCLSID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0'), pid=6)
def PKEY_Shell_SFGAOFlagsStrings():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d6942081-d53b-443d-ad-47-5e-05-9d-9c-d2-7a'), pid=2)
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
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26dc287c-6e3d-4bd3-b2-b0-6a-26-ba-2e-34-6d'), pid=3)
def PKEY_StatusBarViewItemCount():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26dc287c-6e3d-4bd3-b2-b0-6a-26-ba-2e-34-6d'), pid=2)
def PKEY_AppUserModel_ExcludeFromShowInNewInstall():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=8)
def PKEY_AppUserModel_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=5)
def PKEY_AppUserModel_IsDestListSeparator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=6)
def PKEY_AppUserModel_IsDualMode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=11)
def PKEY_AppUserModel_PreventPinning():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=9)
def PKEY_AppUserModel_RelaunchCommand():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=2)
def PKEY_AppUserModel_RelaunchDisplayNameResource():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=4)
def PKEY_AppUserModel_RelaunchIconResource():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=3)
def PKEY_AppUserModel_SettingsCommand():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=38)
def PKEY_AppUserModel_StartPinOption():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=12)
APPUSERMODEL_STARTPINOPTION_DEFAULT: UInt32 = 0
APPUSERMODEL_STARTPINOPTION_NOPINONINSTALL: UInt32 = 1
APPUSERMODEL_STARTPINOPTION_USERPINNED: UInt32 = 2
def PKEY_AppUserModel_ToastActivatorCLSID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=26)
def PKEY_AppUserModel_UninstallCommand():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=37)
def PKEY_AppUserModel_VisualElementsManifestHintPath():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9f4c2855-9f79-4b39-a8-d0-e1-d4-2d-e1-d5-f3'), pid=31)
def PKEY_EdgeGesture_DisableTouchWhenFullscreen():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('32ce38b2-2c9a-41b1-9b-c5-b3-78-43-94-aa-44'), pid=2)
def PKEY_Software_DateLastUsed():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('841e4f90-ff59-4d16-89-47-e8-1b-bf-fa-b3-6d'), pid=16)
def PKEY_Software_ProductName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cef7d53-fa64-11d1-a2-03-00-00-f8-1f-ed-ee'), pid=7)
def PKEY_Sync_Comments():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7bd5533e-af15-44db-b8-c8-bd-66-24-e1-d0-32'), pid=13)
def PKEY_Sync_ConflictDescription():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ce50c159-2fb8-41fd-be-68-d3-e0-42-e2-74-bc'), pid=4)
def PKEY_Sync_ConflictFirstLocation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ce50c159-2fb8-41fd-be-68-d3-e0-42-e2-74-bc'), pid=6)
def PKEY_Sync_ConflictSecondLocation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ce50c159-2fb8-41fd-be-68-d3-e0-42-e2-74-bc'), pid=7)
def PKEY_Sync_HandlerCollectionID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7bd5533e-af15-44db-b8-c8-bd-66-24-e1-d0-32'), pid=2)
def PKEY_Sync_HandlerID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7bd5533e-af15-44db-b8-c8-bd-66-24-e1-d0-32'), pid=3)
def PKEY_Sync_HandlerName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ce50c159-2fb8-41fd-be-68-d3-e0-42-e2-74-bc'), pid=2)
def PKEY_Sync_HandlerType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7bd5533e-af15-44db-b8-c8-bd-66-24-e1-d0-32'), pid=8)
SYNC_HANDLERTYPE_OTHER: UInt32 = 0
SYNC_HANDLERTYPE_PROGRAMS: UInt32 = 1
SYNC_HANDLERTYPE_DEVICES: UInt32 = 2
SYNC_HANDLERTYPE_FOLDERS: UInt32 = 3
SYNC_HANDLERTYPE_WEBSERVICES: UInt32 = 4
SYNC_HANDLERTYPE_COMPUTERS: UInt32 = 5
def PKEY_Sync_HandlerTypeLabel():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7bd5533e-af15-44db-b8-c8-bd-66-24-e1-d0-32'), pid=9)
def PKEY_Sync_ItemID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7bd5533e-af15-44db-b8-c8-bd-66-24-e1-d0-32'), pid=6)
def PKEY_Sync_ItemName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ce50c159-2fb8-41fd-be-68-d3-e0-42-e2-74-bc'), pid=3)
def PKEY_Sync_ProgressPercentage():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7bd5533e-af15-44db-b8-c8-bd-66-24-e1-d0-32'), pid=23)
def PKEY_Sync_State():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7bd5533e-af15-44db-b8-c8-bd-66-24-e1-d0-32'), pid=24)
SYNC_STATE_NOTSETUP: UInt32 = 0
SYNC_STATE_SYNCNOTRUN: UInt32 = 1
SYNC_STATE_IDLE: UInt32 = 2
SYNC_STATE_ERROR: UInt32 = 3
SYNC_STATE_PENDING: UInt32 = 4
SYNC_STATE_SYNCING: UInt32 = 5
def PKEY_Sync_Status():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7bd5533e-af15-44db-b8-c8-bd-66-24-e1-d0-32'), pid=10)
def PKEY_Task_BillingInformation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d37d52c6-261c-4303-82-b3-08-b9-26-ac-6f-12'), pid=100)
def PKEY_Task_CompletionStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('084d8a0a-e6d5-40de-bf-1f-c8-82-0e-7c-87-7c'), pid=100)
def PKEY_Task_Owner():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('08c7cc5f-60f2-4494-ad-75-55-e3-e0-b5-ad-d0'), pid=100)
def PKEY_Video_Compression():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=10)
def PKEY_Video_Director():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440492-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=20)
def PKEY_Video_EncodingBitrate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=8)
def PKEY_Video_FourCC():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=44)
def PKEY_Video_FrameHeight():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=4)
def PKEY_Video_FrameRate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=6)
def PKEY_Video_FrameWidth():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=3)
def PKEY_Video_HorizontalAspectRatio():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=42)
def PKEY_Video_IsSpherical():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=100)
def PKEY_Video_IsStereo():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=98)
def PKEY_Video_Orientation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=99)
def PKEY_Video_SampleSize():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=9)
def PKEY_Video_StreamName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=2)
def PKEY_Video_StreamNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=11)
def PKEY_Video_TotalBitrate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=43)
def PKEY_Video_TranscodedForSync():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=46)
def PKEY_Video_VerticalAspectRatio():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64440491-4c8b-11d1-8b-70-08-00-36-b1-1a-03'), pid=45)
def PKEY_Volume_FileSystem():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9b174b35-40ff-11d2-a2-7e-00-c0-4f-c3-08-71'), pid=4)
def PKEY_Volume_IsMappedDrive():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('149c0b69-2c2d-48fc-80-8f-d3-18-d7-8c-46-36'), pid=2)
def PKEY_Volume_IsRoot():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9b174b35-40ff-11d2-a2-7e-00-c0-4f-c3-08-71'), pid=10)
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
class ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION(Structure):
    CurrentAdminFailures: Byte
    CurrentUserFailures: Byte
    TotalUserAuthenticationCount: UInt32
    TotalAdminAuthenticationCount: UInt32
    FipsCompliant: Windows.Win32.Foundation.BOOL
    SecurityIDAvailable: Windows.Win32.Foundation.BOOL
    InitializeInProgress: Windows.Win32.Foundation.BOOL
    ITMSArmed: Windows.Win32.Foundation.BOOL
    ITMSArmable: Windows.Win32.Foundation.BOOL
    UserCreated: Windows.Win32.Foundation.BOOL
    ResetOnPORDefault: Windows.Win32.Foundation.BOOL
    ResetOnPORCurrent: Windows.Win32.Foundation.BOOL
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
EnhancedStorageACT = Guid('af076a15-2ece-4ad4-bb-21-29-f0-40-e1-76-d8')
EnhancedStorageSilo = Guid('cb25220c-76c7-4fee-84-2b-f3-38-3c-d0-22-bc')
EnhancedStorageSiloAction = Guid('886d29dd-b506-466b-9f-bf-b4-4f-f3-83-fb-3f')
EnumEnhancedStorageACT = Guid('fe841493-835c-4fa3-b6-cc-b4-b2-d4-71-98-48')
class IEnhancedStorageACT(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6e7781f4-e0f2-4239-b9-76-a0-1a-ba-b5-29-30')
    @commethod(3)
    def Authorize(hwndParent: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unauthorize() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAuthorizationState(pState: POINTER(Windows.Win32.Storage.EnhancedStorage.ACT_AUTHORIZATION_STATE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMatchingVolume(ppwszVolume: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUniqueIdentity(ppwszIdentity: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSilos(pppIEnhancedStorageSilos: POINTER(POINTER(Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageSilo_head)), pcEnhancedStorageSilos: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnhancedStorageACT2(c_void_p):
    extends: Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageACT
    Guid = Guid('4da57d2e-8eb3-41f6-a0-7e-98-b5-2b-88-24-2b')
    @commethod(9)
    def GetDeviceName(ppwszDeviceName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsDeviceRemovable(pIsDeviceRemovable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnhancedStorageACT3(c_void_p):
    extends: Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageACT2
    Guid = Guid('022150a1-113d-11df-bb-61-00-1a-a0-1b-bc-58')
    @commethod(11)
    def UnauthorizeEx(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsQueueFrozen(pIsQueueFrozen: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetShellExtSupport(pShellExtSupport: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnhancedStorageSilo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5aef78c6-2242-4703-bf-49-44-b2-93-57-a3-59')
    @commethod(3)
    def GetInfo(pSiloInfo: POINTER(Windows.Win32.Storage.EnhancedStorage.SILO_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetActions(pppIEnhancedStorageSiloActions: POINTER(POINTER(Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageSiloAction_head)), pcEnhancedStorageSiloActions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SendCommand(Command: Byte, pbCommandBuffer: c_char_p_no, cbCommandBuffer: UInt32, pbResponseBuffer: c_char_p_no, pcbResponseBuffer: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPortableDevice(ppIPortableDevice: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDevicePath(ppwszSiloDevicePath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnhancedStorageSiloAction(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b6f7f311-206f-4ff8-9c-4b-27-ef-ee-77-a8-6f')
    @commethod(3)
    def GetName(ppwszActionName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(ppwszActionDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Invoke() -> Windows.Win32.Foundation.HRESULT: ...
class IEnumEnhancedStorageACT(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('09b224bd-1335-4631-a7-ff-cf-d3-a9-26-46-d7')
    @commethod(3)
    def GetACTs(pppIEnhancedStorageACTs: POINTER(POINTER(Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageACT_head)), pcEnhancedStorageACTs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMatchingACT(szVolume: Windows.Win32.Foundation.PWSTR, ppIEnhancedStorageACT: POINTER(Windows.Win32.Storage.EnhancedStorage.IEnhancedStorageACT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class SILO_INFO(Structure):
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
__all__ = [
    "ACT_AUTHORIZATION_STATE",
    "ACT_AUTHORIZATION_STATE_VALUE",
    "ACT_AUTHORIZED",
    "ACT_AUTHORIZE_ON_RESUME",
    "ACT_AUTHORIZE_ON_SESSION_UNLOCK",
    "ACT_UNAUTHORIZED",
    "ACT_UNAUTHORIZE_ON_SESSION_LOCK",
    "ACT_UNAUTHORIZE_ON_SUSPEND",
    "APPUSERMODEL_STARTPINOPTION_DEFAULT",
    "APPUSERMODEL_STARTPINOPTION_NOPINONINSTALL",
    "APPUSERMODEL_STARTPINOPTION_USERPINNED",
    "AUDIO_CHANNELCOUNT_MONO",
    "AUDIO_CHANNELCOUNT_STEREO",
    "BLUETOOTH_ADDRESS_TYPE_PUBLIC",
    "BLUETOOTH_ADDRESS_TYPE_RANDOM",
    "BLUETOOTH_CACHED_MODE_UNCACHED",
    "BLUETOOTH_CACHE_MODE_CACHED",
    "CERT_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY",
    "CERT_CAPABILITY_CERTIFICATE_SUPPORT",
    "CERT_CAPABILITY_HASH_ALG",
    "CERT_CAPABILITY_OPTIONAL_FEATURES",
    "CERT_CAPABILITY_SIGNATURE_ALG",
    "CERT_MAX_CAPABILITY",
    "CERT_RSASSA_PSS_SHA1_OID",
    "CERT_RSASSA_PSS_SHA256_OID",
    "CERT_RSASSA_PSS_SHA384_OID",
    "CERT_RSASSA_PSS_SHA512_OID",
    "CERT_RSA_1024_OID",
    "CERT_RSA_2048_OID",
    "CERT_RSA_3072_OID",
    "CERT_TYPE_ASCh",
    "CERT_TYPE_ASCm",
    "CERT_TYPE_EMPTY",
    "CERT_TYPE_HCh",
    "CERT_TYPE_PCp",
    "CERT_TYPE_SIGNER",
    "CERT_VALIDATION_POLICY_BASIC",
    "CERT_VALIDATION_POLICY_EXTENDED",
    "CERT_VALIDATION_POLICY_NONE",
    "CERT_VALIDATION_POLICY_RESERVED",
    "CREATOROPENWITHUIOPTION_HIDDEN",
    "CREATOROPENWITHUIOPTION_VISIBLE",
    "ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATED",
    "ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATION_DENIED",
    "ENHANCED_STORAGE_AUTHN_STATE_DEVICE_ERROR",
    "ENHANCED_STORAGE_AUTHN_STATE_NOT_AUTHENTICATED",
    "ENHANCED_STORAGE_AUTHN_STATE_NO_AUTHENTICATION_REQUIRED",
    "ENHANCED_STORAGE_AUTHN_STATE_UNKNOWN",
    "ENHANCED_STORAGE_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY",
    "ENHANCED_STORAGE_CAPABILITY_CERTIFICATE_EXTENSION_PARSING",
    "ENHANCED_STORAGE_CAPABILITY_HASH_ALGS",
    "ENHANCED_STORAGE_CAPABILITY_RENDER_USER_DATA_UNUSABLE",
    "ENHANCED_STORAGE_CAPABILITY_SIGNING_ALGS",
    "ENHANCED_STORAGE_COMMAND_CERT_ADMIN_CERTIFICATE_AUTHENTICATION",
    "ENHANCED_STORAGE_COMMAND_CERT_CREATE_CERTIFICATE_REQUEST",
    "ENHANCED_STORAGE_COMMAND_CERT_DEVICE_CERTIFICATE_AUTHENTICATION",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_ACT_FRIENDLY_NAME",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE_COUNT",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITIES",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITY",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_GUID",
    "ENHANCED_STORAGE_COMMAND_CERT_HOST_CERTIFICATE_AUTHENTICATION",
    "ENHANCED_STORAGE_COMMAND_CERT_INITIALIZE_TO_MANUFACTURER_STATE",
    "ENHANCED_STORAGE_COMMAND_CERT_SET_CERTIFICATE",
    "ENHANCED_STORAGE_COMMAND_CERT_UNAUTHENTICATION",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_AUTHORIZE_ACT_ACCESS",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_CHANGE_PASSWORD",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_CONFIG_ADMINISTRATOR",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_CREATE_USER",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_DELETE_USER",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_INITIALIZE_USER_PASSWORD",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_QUERY_INFORMATION",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_START_INITIALIZE_TO_MANUFACTURER_STATE",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_UNAUTHORIZE_ACT_ACCESS",
    "ENHANCED_STORAGE_COMMAND_SILO_ENUMERATE_SILOS",
    "ENHANCED_STORAGE_COMMAND_SILO_GET_AUTHENTICATION_STATE",
    "ENHANCED_STORAGE_COMMAND_SILO_IS_AUTHENTICATION_SILO",
    "ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION",
    "ENHANCED_STORAGE_PROPERTY_ADMIN_HINT",
    "ENHANCED_STORAGE_PROPERTY_AUTHENTICATION_STATE",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_ACT_FRIENDLY_NAME",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_CAPABILITY_TYPE",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_INDEX",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_LENGTH",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_REQUEST",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITIES",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITY",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_GUID",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_TYPE",
    "ENHANCED_STORAGE_PROPERTY_IS_AUTHENTICATION_SILO",
    "ENHANCED_STORAGE_PROPERTY_MAX_AUTH_FAILURES",
    "ENHANCED_STORAGE_PROPERTY_MAX_CERTIFICATE_COUNT",
    "ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD",
    "ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD_INDICATOR",
    "ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_INDEX",
    "ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_OF_TYPE_INDEX",
    "ENHANCED_STORAGE_PROPERTY_OLD_PASSWORD",
    "ENHANCED_STORAGE_PROPERTY_PASSWORD",
    "ENHANCED_STORAGE_PROPERTY_PASSWORD_INDICATOR",
    "ENHANCED_STORAGE_PROPERTY_PASSWORD_SILO_INFO",
    "ENHANCED_STORAGE_PROPERTY_QUERY_SILO_RESULTS",
    "ENHANCED_STORAGE_PROPERTY_QUERY_SILO_TYPE",
    "ENHANCED_STORAGE_PROPERTY_SECURITY_IDENTIFIER",
    "ENHANCED_STORAGE_PROPERTY_SIGNER_CERTIFICATE_INDEX",
    "ENHANCED_STORAGE_PROPERTY_SILO_FRIENDLYNAME_SPECIFIED",
    "ENHANCED_STORAGE_PROPERTY_SILO_NAME",
    "ENHANCED_STORAGE_PROPERTY_STORED_CERTIFICATE_COUNT",
    "ENHANCED_STORAGE_PROPERTY_TEMPORARY_UNAUTHENTICATION",
    "ENHANCED_STORAGE_PROPERTY_USER_HINT",
    "ENHANCED_STORAGE_PROPERTY_USER_NAME",
    "ENHANCED_STORAGE_PROPERTY_VALIDATION_POLICY",
    "ES_AUTHN_ERROR_END",
    "ES_AUTHN_ERROR_START",
    "ES_E_AUTHORIZED_UNEXPECTED",
    "ES_E_BAD_SEQUENCE",
    "ES_E_CHALLENGE_MISMATCH",
    "ES_E_CHALLENGE_SIZE_MISMATCH",
    "ES_E_DEVICE_DIGEST_MISSING",
    "ES_E_FRIENDLY_NAME_TOO_LONG",
    "ES_E_GROUP_POLICY_FORBIDDEN_OPERATION",
    "ES_E_GROUP_POLICY_FORBIDDEN_USE",
    "ES_E_INCOMPLETE_COMMAND",
    "ES_E_INCONSISTENT_PARAM_LENGTH",
    "ES_E_INVALID_CAPABILITY",
    "ES_E_INVALID_FIELD_IDENTIFIER",
    "ES_E_INVALID_PARAM_COMBINATION",
    "ES_E_INVALID_PARAM_LENGTH",
    "ES_E_INVALID_RESPONSE",
    "ES_E_INVALID_SILO",
    "ES_E_NOT_AUTHORIZED_UNEXPECTED",
    "ES_E_NO_AUTHENTICATION_REQUIRED",
    "ES_E_NO_PROBE",
    "ES_E_OTHER_SECURITY_PROTOCOL_ACTIVE",
    "ES_E_PASSWORD_HINT_TOO_LONG",
    "ES_E_PASSWORD_TOO_LONG",
    "ES_E_PROVISIONED_UNEXPECTED",
    "ES_E_SILO_NAME_TOO_LONG",
    "ES_E_UNKNOWN_DIGEST_ALGORITHM",
    "ES_E_UNPROVISIONED_HARDWARE",
    "ES_E_UNSUPPORTED_HARDWARE",
    "ES_GENERAL_ERROR_END",
    "ES_GENERAL_ERROR_START",
    "ES_PW_SILO_ERROR_END",
    "ES_PW_SILO_ERROR_START",
    "ES_RESERVED_COM_ERROR_END",
    "ES_RESERVED_COM_ERROR_START",
    "ES_RESERVED_SILO_ERROR_END",
    "ES_RESERVED_SILO_ERROR_START",
    "ES_RESERVED_SILO_SPECIFIC_ERROR_END",
    "ES_RESERVED_SILO_SPECIFIC_ERROR_START",
    "ES_VENDOR_ERROR_END",
    "ES_VENDOR_ERROR_START",
    "EnhancedStorageACT",
    "EnhancedStorageSilo",
    "EnhancedStorageSiloAction",
    "EnumEnhancedStorageACT",
    "FACILITY_ENHANCED_STORAGE",
    "FILEOFFLINEAVAILABILITYSTATUS_COMPLETE",
    "FILEOFFLINEAVAILABILITYSTATUS_COMPLETE_PINNED",
    "FILEOFFLINEAVAILABILITYSTATUS_EXCLUDED",
    "FILEOFFLINEAVAILABILITYSTATUS_FOLDER_EMPTY",
    "FILEOFFLINEAVAILABILITYSTATUS_NOTAVAILABLEOFFLINE",
    "FILEOFFLINEAVAILABILITYSTATUS_PARTIAL",
    "FLAGSTATUS_COMPLETED",
    "FLAGSTATUS_FOLLOWUP",
    "FLAGSTATUS_NOTFLAGGED",
    "GUID_DEVINTERFACE_ENHANCED_STORAGE_SILO",
    "IEnhancedStorageACT",
    "IEnhancedStorageACT2",
    "IEnhancedStorageACT3",
    "IEnhancedStorageSilo",
    "IEnhancedStorageSiloAction",
    "IEnumEnhancedStorageACT",
    "IMPORTANCE_HIGH_MAX",
    "IMPORTANCE_HIGH_MIN",
    "IMPORTANCE_HIGH_SET",
    "IMPORTANCE_LOW_MAX",
    "IMPORTANCE_LOW_MIN",
    "IMPORTANCE_LOW_SET",
    "IMPORTANCE_NORMAL_MAX",
    "IMPORTANCE_NORMAL_MIN",
    "IMPORTANCE_NORMAL_SET",
    "ISDEFAULTSAVE_BOTH",
    "ISDEFAULTSAVE_NONE",
    "ISDEFAULTSAVE_NONOWNER",
    "ISDEFAULTSAVE_OWNER",
    "KIND_CALENDAR",
    "KIND_COMMUNICATION",
    "KIND_CONTACT",
    "KIND_DOCUMENT",
    "KIND_EMAIL",
    "KIND_FEED",
    "KIND_FOLDER",
    "KIND_GAME",
    "KIND_INSTANTMESSAGE",
    "KIND_JOURNAL",
    "KIND_LINK",
    "KIND_MOVIE",
    "KIND_MUSIC",
    "KIND_NOTE",
    "KIND_PICTURE",
    "KIND_PLAYLIST",
    "KIND_PROGRAM",
    "KIND_RECORDEDTV",
    "KIND_SEARCHFOLDER",
    "KIND_TASK",
    "KIND_UNKNOWN",
    "KIND_VIDEO",
    "KIND_WEBHISTORY",
    "LAYOUTPATTERN_CVMFB_ALPHA",
    "LAYOUTPATTERN_CVMFB_BETA",
    "LAYOUTPATTERN_CVMFB_DELTA",
    "LAYOUTPATTERN_CVMFB_GAMMA",
    "LAYOUTPATTERN_CVMFS_ALPHA",
    "LAYOUTPATTERN_CVMFS_BETA",
    "LAYOUTPATTERN_CVMFS_DELTA",
    "LAYOUTPATTERN_CVMFS_GAMMA",
    "LINK_STATUS_BROKEN",
    "LINK_STATUS_RESOLVED",
    "OFFLINEAVAILABILITY_ALWAYS_AVAILABLE",
    "OFFLINEAVAILABILITY_AVAILABLE",
    "OFFLINEAVAILABILITY_NOT_AVAILABLE",
    "OFFLINESTATUS_OFFLINE",
    "OFFLINESTATUS_OFFLINE_ERROR",
    "OFFLINESTATUS_OFFLINE_FORCED",
    "OFFLINESTATUS_OFFLINE_ITEM_VERSION_CONFLICT",
    "OFFLINESTATUS_OFFLINE_SLOW",
    "OFFLINESTATUS_OFFLINE_SUSPENDED",
    "OFFLINESTATUS_ONLINE",
    "PHOTO_CONTRAST_HARD",
    "PHOTO_CONTRAST_NORMAL",
    "PHOTO_CONTRAST_SOFT",
    "PHOTO_EXPOSUREPROGRAM_ACTION",
    "PHOTO_EXPOSUREPROGRAM_APERTURE",
    "PHOTO_EXPOSUREPROGRAM_CREATIVE",
    "PHOTO_EXPOSUREPROGRAM_LANDSCAPE",
    "PHOTO_EXPOSUREPROGRAM_MANUAL",
    "PHOTO_EXPOSUREPROGRAM_NORMAL",
    "PHOTO_EXPOSUREPROGRAM_PORTRAIT",
    "PHOTO_EXPOSUREPROGRAM_SHUTTER",
    "PHOTO_EXPOSUREPROGRAM_UNKNOWN",
    "PHOTO_FLASH_FLASH",
    "PHOTO_FLASH_FLASH_AUTO",
    "PHOTO_FLASH_FLASH_AUTO_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_AUTO_REDEYE",
    "PHOTO_FLASH_FLASH_AUTO_REDEYE_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_AUTO_REDEYE_RETURNLIGHT",
    "PHOTO_FLASH_FLASH_AUTO_RETURNLIGHT",
    "PHOTO_FLASH_FLASH_COMPULSORY",
    "PHOTO_FLASH_FLASH_COMPULSORY_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_COMPULSORY_REDEYE",
    "PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_RETURNLIGHT",
    "PHOTO_FLASH_FLASH_COMPULSORY_RETURNLIGHT",
    "PHOTO_FLASH_FLASH_REDEYE",
    "PHOTO_FLASH_FLASH_REDEYE_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_REDEYE_RETURNLIGHT",
    "PHOTO_FLASH_NOFUNCTION",
    "PHOTO_FLASH_NONE",
    "PHOTO_FLASH_NONE_AUTO",
    "PHOTO_FLASH_NONE_COMPULSORY",
    "PHOTO_FLASH_WITHOUTSTROBE",
    "PHOTO_FLASH_WITHSTROBE",
    "PHOTO_GAINCONTROL_HIGHGAINDOWN",
    "PHOTO_GAINCONTROL_HIGHGAINUP",
    "PHOTO_GAINCONTROL_LOWGAINDOWN",
    "PHOTO_GAINCONTROL_LOWGAINUP",
    "PHOTO_GAINCONTROL_NONE",
    "PHOTO_LIGHTSOURCE_D55",
    "PHOTO_LIGHTSOURCE_D65",
    "PHOTO_LIGHTSOURCE_D75",
    "PHOTO_LIGHTSOURCE_DAYLIGHT",
    "PHOTO_LIGHTSOURCE_FLUORESCENT",
    "PHOTO_LIGHTSOURCE_STANDARD_A",
    "PHOTO_LIGHTSOURCE_STANDARD_B",
    "PHOTO_LIGHTSOURCE_STANDARD_C",
    "PHOTO_LIGHTSOURCE_TUNGSTEN",
    "PHOTO_LIGHTSOURCE_UNKNOWN",
    "PHOTO_PROGRAMMODE_ACTION",
    "PHOTO_PROGRAMMODE_APERTURE",
    "PHOTO_PROGRAMMODE_CREATIVE",
    "PHOTO_PROGRAMMODE_LANDSCAPE",
    "PHOTO_PROGRAMMODE_MANUAL",
    "PHOTO_PROGRAMMODE_NORMAL",
    "PHOTO_PROGRAMMODE_NOTDEFINED",
    "PHOTO_PROGRAMMODE_PORTRAIT",
    "PHOTO_PROGRAMMODE_SHUTTER",
    "PHOTO_SATURATION_HIGH",
    "PHOTO_SATURATION_LOW",
    "PHOTO_SATURATION_NORMAL",
    "PHOTO_SHARPNESS_HARD",
    "PHOTO_SHARPNESS_NORMAL",
    "PHOTO_SHARPNESS_SOFT",
    "PHOTO_WHITEBALANCE_AUTO",
    "PHOTO_WHITEBALANCE_MANUAL",
    "PKEY_AcquisitionID",
    "PKEY_Address_Country",
    "PKEY_Address_CountryCode",
    "PKEY_Address_Region",
    "PKEY_Address_RegionCode",
    "PKEY_Address_Town",
    "PKEY_AppUserModel_ExcludeFromShowInNewInstall",
    "PKEY_AppUserModel_ID",
    "PKEY_AppUserModel_IsDestListSeparator",
    "PKEY_AppUserModel_IsDualMode",
    "PKEY_AppUserModel_PreventPinning",
    "PKEY_AppUserModel_RelaunchCommand",
    "PKEY_AppUserModel_RelaunchDisplayNameResource",
    "PKEY_AppUserModel_RelaunchIconResource",
    "PKEY_AppUserModel_SettingsCommand",
    "PKEY_AppUserModel_StartPinOption",
    "PKEY_AppUserModel_ToastActivatorCLSID",
    "PKEY_AppUserModel_UninstallCommand",
    "PKEY_AppUserModel_VisualElementsManifestHintPath",
    "PKEY_AppZoneIdentifier",
    "PKEY_ApplicationDefinedProperties",
    "PKEY_ApplicationName",
    "PKEY_Audio_ChannelCount",
    "PKEY_Audio_Compression",
    "PKEY_Audio_EncodingBitrate",
    "PKEY_Audio_Format",
    "PKEY_Audio_IsVariableBitRate",
    "PKEY_Audio_PeakValue",
    "PKEY_Audio_SampleRate",
    "PKEY_Audio_SampleSize",
    "PKEY_Audio_StreamName",
    "PKEY_Audio_StreamNumber",
    "PKEY_Author",
    "PKEY_CachedFileUpdaterContentIdForConflictResolution",
    "PKEY_CachedFileUpdaterContentIdForStream",
    "PKEY_Calendar_Duration",
    "PKEY_Calendar_IsOnline",
    "PKEY_Calendar_IsRecurring",
    "PKEY_Calendar_Location",
    "PKEY_Calendar_OptionalAttendeeAddresses",
    "PKEY_Calendar_OptionalAttendeeNames",
    "PKEY_Calendar_OrganizerAddress",
    "PKEY_Calendar_OrganizerName",
    "PKEY_Calendar_ReminderTime",
    "PKEY_Calendar_RequiredAttendeeAddresses",
    "PKEY_Calendar_RequiredAttendeeNames",
    "PKEY_Calendar_Resources",
    "PKEY_Calendar_ResponseStatus",
    "PKEY_Calendar_ShowTimeAs",
    "PKEY_Calendar_ShowTimeAsText",
    "PKEY_Capacity",
    "PKEY_Category",
    "PKEY_Comment",
    "PKEY_Communication_AccountName",
    "PKEY_Communication_DateItemExpires",
    "PKEY_Communication_Direction",
    "PKEY_Communication_FollowupIconIndex",
    "PKEY_Communication_HeaderItem",
    "PKEY_Communication_PolicyTag",
    "PKEY_Communication_SecurityFlags",
    "PKEY_Communication_Suffix",
    "PKEY_Communication_TaskStatus",
    "PKEY_Communication_TaskStatusText",
    "PKEY_Company",
    "PKEY_ComputerName",
    "PKEY_Computer_DecoratedFreeSpace",
    "PKEY_Contact_AccountPictureDynamicVideo",
    "PKEY_Contact_AccountPictureLarge",
    "PKEY_Contact_AccountPictureSmall",
    "PKEY_Contact_Anniversary",
    "PKEY_Contact_AssistantName",
    "PKEY_Contact_AssistantTelephone",
    "PKEY_Contact_Birthday",
    "PKEY_Contact_BusinessAddress",
    "PKEY_Contact_BusinessAddress1Country",
    "PKEY_Contact_BusinessAddress1Locality",
    "PKEY_Contact_BusinessAddress1PostalCode",
    "PKEY_Contact_BusinessAddress1Region",
    "PKEY_Contact_BusinessAddress1Street",
    "PKEY_Contact_BusinessAddress2Country",
    "PKEY_Contact_BusinessAddress2Locality",
    "PKEY_Contact_BusinessAddress2PostalCode",
    "PKEY_Contact_BusinessAddress2Region",
    "PKEY_Contact_BusinessAddress2Street",
    "PKEY_Contact_BusinessAddress3Country",
    "PKEY_Contact_BusinessAddress3Locality",
    "PKEY_Contact_BusinessAddress3PostalCode",
    "PKEY_Contact_BusinessAddress3Region",
    "PKEY_Contact_BusinessAddress3Street",
    "PKEY_Contact_BusinessAddressCity",
    "PKEY_Contact_BusinessAddressCountry",
    "PKEY_Contact_BusinessAddressPostOfficeBox",
    "PKEY_Contact_BusinessAddressPostalCode",
    "PKEY_Contact_BusinessAddressState",
    "PKEY_Contact_BusinessAddressStreet",
    "PKEY_Contact_BusinessEmailAddresses",
    "PKEY_Contact_BusinessFaxNumber",
    "PKEY_Contact_BusinessHomePage",
    "PKEY_Contact_BusinessTelephone",
    "PKEY_Contact_CallbackTelephone",
    "PKEY_Contact_CarTelephone",
    "PKEY_Contact_Children",
    "PKEY_Contact_CompanyMainTelephone",
    "PKEY_Contact_ConnectedServiceDisplayName",
    "PKEY_Contact_ConnectedServiceIdentities",
    "PKEY_Contact_ConnectedServiceName",
    "PKEY_Contact_ConnectedServiceSupportedActions",
    "PKEY_Contact_DataSuppliers",
    "PKEY_Contact_Department",
    "PKEY_Contact_DisplayBusinessPhoneNumbers",
    "PKEY_Contact_DisplayHomePhoneNumbers",
    "PKEY_Contact_DisplayMobilePhoneNumbers",
    "PKEY_Contact_DisplayOtherPhoneNumbers",
    "PKEY_Contact_EmailAddress",
    "PKEY_Contact_EmailAddress2",
    "PKEY_Contact_EmailAddress3",
    "PKEY_Contact_EmailAddresses",
    "PKEY_Contact_EmailName",
    "PKEY_Contact_FileAsName",
    "PKEY_Contact_FirstName",
    "PKEY_Contact_FullName",
    "PKEY_Contact_Gender",
    "PKEY_Contact_GenderValue",
    "PKEY_Contact_Hobbies",
    "PKEY_Contact_HomeAddress",
    "PKEY_Contact_HomeAddress1Country",
    "PKEY_Contact_HomeAddress1Locality",
    "PKEY_Contact_HomeAddress1PostalCode",
    "PKEY_Contact_HomeAddress1Region",
    "PKEY_Contact_HomeAddress1Street",
    "PKEY_Contact_HomeAddress2Country",
    "PKEY_Contact_HomeAddress2Locality",
    "PKEY_Contact_HomeAddress2PostalCode",
    "PKEY_Contact_HomeAddress2Region",
    "PKEY_Contact_HomeAddress2Street",
    "PKEY_Contact_HomeAddress3Country",
    "PKEY_Contact_HomeAddress3Locality",
    "PKEY_Contact_HomeAddress3PostalCode",
    "PKEY_Contact_HomeAddress3Region",
    "PKEY_Contact_HomeAddress3Street",
    "PKEY_Contact_HomeAddressCity",
    "PKEY_Contact_HomeAddressCountry",
    "PKEY_Contact_HomeAddressPostOfficeBox",
    "PKEY_Contact_HomeAddressPostalCode",
    "PKEY_Contact_HomeAddressState",
    "PKEY_Contact_HomeAddressStreet",
    "PKEY_Contact_HomeEmailAddresses",
    "PKEY_Contact_HomeFaxNumber",
    "PKEY_Contact_HomeTelephone",
    "PKEY_Contact_IMAddress",
    "PKEY_Contact_Initials",
    "PKEY_Contact_JA_CompanyNamePhonetic",
    "PKEY_Contact_JA_FirstNamePhonetic",
    "PKEY_Contact_JA_LastNamePhonetic",
    "PKEY_Contact_JobInfo1CompanyAddress",
    "PKEY_Contact_JobInfo1CompanyName",
    "PKEY_Contact_JobInfo1Department",
    "PKEY_Contact_JobInfo1Manager",
    "PKEY_Contact_JobInfo1OfficeLocation",
    "PKEY_Contact_JobInfo1Title",
    "PKEY_Contact_JobInfo1YomiCompanyName",
    "PKEY_Contact_JobInfo2CompanyAddress",
    "PKEY_Contact_JobInfo2CompanyName",
    "PKEY_Contact_JobInfo2Department",
    "PKEY_Contact_JobInfo2Manager",
    "PKEY_Contact_JobInfo2OfficeLocation",
    "PKEY_Contact_JobInfo2Title",
    "PKEY_Contact_JobInfo2YomiCompanyName",
    "PKEY_Contact_JobInfo3CompanyAddress",
    "PKEY_Contact_JobInfo3CompanyName",
    "PKEY_Contact_JobInfo3Department",
    "PKEY_Contact_JobInfo3Manager",
    "PKEY_Contact_JobInfo3OfficeLocation",
    "PKEY_Contact_JobInfo3Title",
    "PKEY_Contact_JobInfo3YomiCompanyName",
    "PKEY_Contact_JobTitle",
    "PKEY_Contact_Label",
    "PKEY_Contact_LastName",
    "PKEY_Contact_MailingAddress",
    "PKEY_Contact_MiddleName",
    "PKEY_Contact_MobileTelephone",
    "PKEY_Contact_NickName",
    "PKEY_Contact_OfficeLocation",
    "PKEY_Contact_OtherAddress",
    "PKEY_Contact_OtherAddress1Country",
    "PKEY_Contact_OtherAddress1Locality",
    "PKEY_Contact_OtherAddress1PostalCode",
    "PKEY_Contact_OtherAddress1Region",
    "PKEY_Contact_OtherAddress1Street",
    "PKEY_Contact_OtherAddress2Country",
    "PKEY_Contact_OtherAddress2Locality",
    "PKEY_Contact_OtherAddress2PostalCode",
    "PKEY_Contact_OtherAddress2Region",
    "PKEY_Contact_OtherAddress2Street",
    "PKEY_Contact_OtherAddress3Country",
    "PKEY_Contact_OtherAddress3Locality",
    "PKEY_Contact_OtherAddress3PostalCode",
    "PKEY_Contact_OtherAddress3Region",
    "PKEY_Contact_OtherAddress3Street",
    "PKEY_Contact_OtherAddressCity",
    "PKEY_Contact_OtherAddressCountry",
    "PKEY_Contact_OtherAddressPostOfficeBox",
    "PKEY_Contact_OtherAddressPostalCode",
    "PKEY_Contact_OtherAddressState",
    "PKEY_Contact_OtherAddressStreet",
    "PKEY_Contact_OtherEmailAddresses",
    "PKEY_Contact_PagerTelephone",
    "PKEY_Contact_PersonalTitle",
    "PKEY_Contact_PhoneNumbersCanonical",
    "PKEY_Contact_Prefix",
    "PKEY_Contact_PrimaryAddressCity",
    "PKEY_Contact_PrimaryAddressCountry",
    "PKEY_Contact_PrimaryAddressPostOfficeBox",
    "PKEY_Contact_PrimaryAddressPostalCode",
    "PKEY_Contact_PrimaryAddressState",
    "PKEY_Contact_PrimaryAddressStreet",
    "PKEY_Contact_PrimaryEmailAddress",
    "PKEY_Contact_PrimaryTelephone",
    "PKEY_Contact_Profession",
    "PKEY_Contact_SpouseName",
    "PKEY_Contact_Suffix",
    "PKEY_Contact_TTYTDDTelephone",
    "PKEY_Contact_TelexNumber",
    "PKEY_Contact_WebPage",
    "PKEY_Contact_Webpage2",
    "PKEY_Contact_Webpage3",
    "PKEY_ContainedItems",
    "PKEY_ContentId",
    "PKEY_ContentStatus",
    "PKEY_ContentType",
    "PKEY_ContentUri",
    "PKEY_Copyright",
    "PKEY_CreatorAppId",
    "PKEY_CreatorOpenWithUIOptions",
    "PKEY_DRM_DatePlayExpires",
    "PKEY_DRM_DatePlayStarts",
    "PKEY_DRM_Description",
    "PKEY_DRM_IsDisabled",
    "PKEY_DRM_IsProtected",
    "PKEY_DRM_PlayCount",
    "PKEY_DataObjectFormat",
    "PKEY_DateAccessed",
    "PKEY_DateAcquired",
    "PKEY_DateArchived",
    "PKEY_DateCompleted",
    "PKEY_DateCreated",
    "PKEY_DateImported",
    "PKEY_DateModified",
    "PKEY_DefaultSaveLocationDisplay",
    "PKEY_DescriptionID",
    "PKEY_DeviceInterface_Bluetooth_DeviceAddress",
    "PKEY_DeviceInterface_Bluetooth_Flags",
    "PKEY_DeviceInterface_Bluetooth_LastConnectedTime",
    "PKEY_DeviceInterface_Bluetooth_Manufacturer",
    "PKEY_DeviceInterface_Bluetooth_ModelNumber",
    "PKEY_DeviceInterface_Bluetooth_ProductId",
    "PKEY_DeviceInterface_Bluetooth_ProductVersion",
    "PKEY_DeviceInterface_Bluetooth_ServiceGuid",
    "PKEY_DeviceInterface_Bluetooth_VendorId",
    "PKEY_DeviceInterface_Bluetooth_VendorIdSource",
    "PKEY_DeviceInterface_Hid_IsReadOnly",
    "PKEY_DeviceInterface_Hid_ProductId",
    "PKEY_DeviceInterface_Hid_UsageId",
    "PKEY_DeviceInterface_Hid_UsagePage",
    "PKEY_DeviceInterface_Hid_VendorId",
    "PKEY_DeviceInterface_Hid_VersionNumber",
    "PKEY_DeviceInterface_PrinterDriverDirectory",
    "PKEY_DeviceInterface_PrinterDriverName",
    "PKEY_DeviceInterface_PrinterEnumerationFlag",
    "PKEY_DeviceInterface_PrinterName",
    "PKEY_DeviceInterface_PrinterPortName",
    "PKEY_DeviceInterface_Proximity_SupportsNfc",
    "PKEY_DeviceInterface_Serial_PortName",
    "PKEY_DeviceInterface_Serial_UsbProductId",
    "PKEY_DeviceInterface_Serial_UsbVendorId",
    "PKEY_DeviceInterface_WinUsb_DeviceInterfaceClasses",
    "PKEY_DeviceInterface_WinUsb_UsbClass",
    "PKEY_DeviceInterface_WinUsb_UsbProductId",
    "PKEY_DeviceInterface_WinUsb_UsbProtocol",
    "PKEY_DeviceInterface_WinUsb_UsbSubClass",
    "PKEY_DeviceInterface_WinUsb_UsbVendorId",
    "PKEY_Device_PrinterURL",
    "PKEY_Devices_AepContainer_CanPair",
    "PKEY_Devices_AepContainer_Categories",
    "PKEY_Devices_AepContainer_Children",
    "PKEY_Devices_AepContainer_ContainerId",
    "PKEY_Devices_AepContainer_DialProtocol_InstalledApplications",
    "PKEY_Devices_AepContainer_IsPaired",
    "PKEY_Devices_AepContainer_IsPresent",
    "PKEY_Devices_AepContainer_Manufacturer",
    "PKEY_Devices_AepContainer_ModelIds",
    "PKEY_Devices_AepContainer_ModelName",
    "PKEY_Devices_AepContainer_ProtocolIds",
    "PKEY_Devices_AepContainer_SupportedUriSchemes",
    "PKEY_Devices_AepContainer_SupportsAudio",
    "PKEY_Devices_AepContainer_SupportsCapturing",
    "PKEY_Devices_AepContainer_SupportsImages",
    "PKEY_Devices_AepContainer_SupportsInformation",
    "PKEY_Devices_AepContainer_SupportsLimitedDiscovery",
    "PKEY_Devices_AepContainer_SupportsNetworking",
    "PKEY_Devices_AepContainer_SupportsObjectTransfer",
    "PKEY_Devices_AepContainer_SupportsPositioning",
    "PKEY_Devices_AepContainer_SupportsRendering",
    "PKEY_Devices_AepContainer_SupportsTelephony",
    "PKEY_Devices_AepContainer_SupportsVideo",
    "PKEY_Devices_AepService_AepId",
    "PKEY_Devices_AepService_Bluetooth_CacheMode",
    "PKEY_Devices_AepService_Bluetooth_ServiceGuid",
    "PKEY_Devices_AepService_Bluetooth_TargetDevice",
    "PKEY_Devices_AepService_ContainerId",
    "PKEY_Devices_AepService_FriendlyName",
    "PKEY_Devices_AepService_IoT_ServiceInterfaces",
    "PKEY_Devices_AepService_ParentAepIsPaired",
    "PKEY_Devices_AepService_ProtocolId",
    "PKEY_Devices_AepService_ServiceClassId",
    "PKEY_Devices_AepService_ServiceId",
    "PKEY_Devices_Aep_AepId",
    "PKEY_Devices_Aep_Bluetooth_Cod_Major",
    "PKEY_Devices_Aep_Bluetooth_Cod_Minor",
    "PKEY_Devices_Aep_Bluetooth_Cod_Services_Audio",
    "PKEY_Devices_Aep_Bluetooth_Cod_Services_Capturing",
    "PKEY_Devices_Aep_Bluetooth_Cod_Services_Information",
    "PKEY_Devices_Aep_Bluetooth_Cod_Services_LimitedDiscovery",
    "PKEY_Devices_Aep_Bluetooth_Cod_Services_Networking",
    "PKEY_Devices_Aep_Bluetooth_Cod_Services_ObjectXfer",
    "PKEY_Devices_Aep_Bluetooth_Cod_Services_Positioning",
    "PKEY_Devices_Aep_Bluetooth_Cod_Services_Rendering",
    "PKEY_Devices_Aep_Bluetooth_Cod_Services_Telephony",
    "PKEY_Devices_Aep_Bluetooth_LastSeenTime",
    "PKEY_Devices_Aep_Bluetooth_Le_AddressType",
    "PKEY_Devices_Aep_Bluetooth_Le_Appearance",
    "PKEY_Devices_Aep_Bluetooth_Le_Appearance_Category",
    "PKEY_Devices_Aep_Bluetooth_Le_Appearance_Subcategory",
    "PKEY_Devices_Aep_Bluetooth_Le_IsConnectable",
    "PKEY_Devices_Aep_CanPair",
    "PKEY_Devices_Aep_Category",
    "PKEY_Devices_Aep_ContainerId",
    "PKEY_Devices_Aep_DeviceAddress",
    "PKEY_Devices_Aep_IsConnected",
    "PKEY_Devices_Aep_IsPaired",
    "PKEY_Devices_Aep_IsPresent",
    "PKEY_Devices_Aep_Manufacturer",
    "PKEY_Devices_Aep_ModelId",
    "PKEY_Devices_Aep_ModelName",
    "PKEY_Devices_Aep_PointOfService_ConnectionTypes",
    "PKEY_Devices_Aep_ProtocolId",
    "PKEY_Devices_Aep_SignalStrength",
    "PKEY_Devices_AppPackageFamilyName",
    "PKEY_Devices_AudioDevice_Microphone_IsFarField",
    "PKEY_Devices_AudioDevice_Microphone_SensitivityInDbfs",
    "PKEY_Devices_AudioDevice_Microphone_SensitivityInDbfs2",
    "PKEY_Devices_AudioDevice_Microphone_SignalToNoiseRatioInDb",
    "PKEY_Devices_AudioDevice_RawProcessingSupported",
    "PKEY_Devices_AudioDevice_SpeechProcessingSupported",
    "PKEY_Devices_BatteryLife",
    "PKEY_Devices_BatteryPlusCharging",
    "PKEY_Devices_BatteryPlusChargingText",
    "PKEY_Devices_Category",
    "PKEY_Devices_CategoryGroup",
    "PKEY_Devices_CategoryIds",
    "PKEY_Devices_CategoryPlural",
    "PKEY_Devices_ChallengeAep",
    "PKEY_Devices_ChargingState",
    "PKEY_Devices_Children",
    "PKEY_Devices_ClassGuid",
    "PKEY_Devices_CompatibleIds",
    "PKEY_Devices_Connected",
    "PKEY_Devices_ContainerId",
    "PKEY_Devices_DefaultTooltip",
    "PKEY_Devices_DevObjectType",
    "PKEY_Devices_DeviceCapabilities",
    "PKEY_Devices_DeviceCharacteristics",
    "PKEY_Devices_DeviceDescription1",
    "PKEY_Devices_DeviceDescription2",
    "PKEY_Devices_DeviceHasProblem",
    "PKEY_Devices_DeviceInstanceId",
    "PKEY_Devices_DeviceManufacturer",
    "PKEY_Devices_DialProtocol_InstalledApplications",
    "PKEY_Devices_DiscoveryMethod",
    "PKEY_Devices_Dnssd_Domain",
    "PKEY_Devices_Dnssd_FullName",
    "PKEY_Devices_Dnssd_HostName",
    "PKEY_Devices_Dnssd_InstanceName",
    "PKEY_Devices_Dnssd_NetworkAdapterId",
    "PKEY_Devices_Dnssd_PortNumber",
    "PKEY_Devices_Dnssd_Priority",
    "PKEY_Devices_Dnssd_ServiceName",
    "PKEY_Devices_Dnssd_TextAttributes",
    "PKEY_Devices_Dnssd_Ttl",
    "PKEY_Devices_Dnssd_Weight",
    "PKEY_Devices_FriendlyName",
    "PKEY_Devices_FunctionPaths",
    "PKEY_Devices_GlyphIcon",
    "PKEY_Devices_HardwareIds",
    "PKEY_Devices_Icon",
    "PKEY_Devices_InLocalMachineContainer",
    "PKEY_Devices_InterfaceClassGuid",
    "PKEY_Devices_InterfaceEnabled",
    "PKEY_Devices_InterfacePaths",
    "PKEY_Devices_IpAddress",
    "PKEY_Devices_IsDefault",
    "PKEY_Devices_IsNetworkConnected",
    "PKEY_Devices_IsShared",
    "PKEY_Devices_IsSoftwareInstalling",
    "PKEY_Devices_LaunchDeviceStageFromExplorer",
    "PKEY_Devices_LocalMachine",
    "PKEY_Devices_LocationPaths",
    "PKEY_Devices_Manufacturer",
    "PKEY_Devices_MetadataPath",
    "PKEY_Devices_MicrophoneArray_Geometry",
    "PKEY_Devices_MissedCalls",
    "PKEY_Devices_ModelId",
    "PKEY_Devices_ModelName",
    "PKEY_Devices_ModelNumber",
    "PKEY_Devices_NetworkName",
    "PKEY_Devices_NetworkType",
    "PKEY_Devices_NetworkedTooltip",
    "PKEY_Devices_NewPictures",
    "PKEY_Devices_NotWorkingProperly",
    "PKEY_Devices_Notification",
    "PKEY_Devices_NotificationStore",
    "PKEY_Devices_Notifications_LowBattery",
    "PKEY_Devices_Notifications_MissedCall",
    "PKEY_Devices_Notifications_NewMessage",
    "PKEY_Devices_Notifications_NewVoicemail",
    "PKEY_Devices_Notifications_StorageFull",
    "PKEY_Devices_Notifications_StorageFullLinkText",
    "PKEY_Devices_Paired",
    "PKEY_Devices_Panel_PanelGroup",
    "PKEY_Devices_Panel_PanelId",
    "PKEY_Devices_Parent",
    "PKEY_Devices_PhoneLineTransportDevice_Connected",
    "PKEY_Devices_PhysicalDeviceLocation",
    "PKEY_Devices_PlaybackPositionPercent",
    "PKEY_Devices_PlaybackState",
    "PKEY_Devices_PlaybackTitle",
    "PKEY_Devices_Present",
    "PKEY_Devices_PresentationUrl",
    "PKEY_Devices_PrimaryCategory",
    "PKEY_Devices_RemainingDuration",
    "PKEY_Devices_RestrictedInterface",
    "PKEY_Devices_Roaming",
    "PKEY_Devices_SafeRemovalRequired",
    "PKEY_Devices_SchematicName",
    "PKEY_Devices_ServiceAddress",
    "PKEY_Devices_ServiceId",
    "PKEY_Devices_SharedTooltip",
    "PKEY_Devices_SignalStrength",
    "PKEY_Devices_SmartCards_ReaderKind",
    "PKEY_Devices_Status",
    "PKEY_Devices_Status1",
    "PKEY_Devices_Status2",
    "PKEY_Devices_StorageCapacity",
    "PKEY_Devices_StorageFreeSpace",
    "PKEY_Devices_StorageFreeSpacePercent",
    "PKEY_Devices_TextMessages",
    "PKEY_Devices_Voicemail",
    "PKEY_Devices_WiFiDirectServices_AdvertisementId",
    "PKEY_Devices_WiFiDirectServices_RequestServiceInformation",
    "PKEY_Devices_WiFiDirectServices_ServiceAddress",
    "PKEY_Devices_WiFiDirectServices_ServiceConfigMethods",
    "PKEY_Devices_WiFiDirectServices_ServiceInformation",
    "PKEY_Devices_WiFiDirectServices_ServiceName",
    "PKEY_Devices_WiFiDirect_DeviceAddress",
    "PKEY_Devices_WiFiDirect_GroupId",
    "PKEY_Devices_WiFiDirect_InformationElements",
    "PKEY_Devices_WiFiDirect_InterfaceAddress",
    "PKEY_Devices_WiFiDirect_InterfaceGuid",
    "PKEY_Devices_WiFiDirect_IsConnected",
    "PKEY_Devices_WiFiDirect_IsLegacyDevice",
    "PKEY_Devices_WiFiDirect_IsMiracastLcpSupported",
    "PKEY_Devices_WiFiDirect_IsVisible",
    "PKEY_Devices_WiFiDirect_MiracastVersion",
    "PKEY_Devices_WiFiDirect_Services",
    "PKEY_Devices_WiFiDirect_SupportedChannelList",
    "PKEY_Devices_WiFi_InterfaceGuid",
    "PKEY_Devices_WiaDeviceType",
    "PKEY_Devices_WinPhone8CameraFlags",
    "PKEY_Devices_Wwan_InterfaceGuid",
    "PKEY_Document_ByteCount",
    "PKEY_Document_CharacterCount",
    "PKEY_Document_ClientID",
    "PKEY_Document_Contributor",
    "PKEY_Document_DateCreated",
    "PKEY_Document_DatePrinted",
    "PKEY_Document_DateSaved",
    "PKEY_Document_Division",
    "PKEY_Document_DocumentID",
    "PKEY_Document_HiddenSlideCount",
    "PKEY_Document_LastAuthor",
    "PKEY_Document_LineCount",
    "PKEY_Document_Manager",
    "PKEY_Document_MultimediaClipCount",
    "PKEY_Document_NoteCount",
    "PKEY_Document_PageCount",
    "PKEY_Document_ParagraphCount",
    "PKEY_Document_PresentationFormat",
    "PKEY_Document_RevisionNumber",
    "PKEY_Document_Security",
    "PKEY_Document_SlideCount",
    "PKEY_Document_Template",
    "PKEY_Document_TotalEditingTime",
    "PKEY_Document_Version",
    "PKEY_Document_WordCount",
    "PKEY_DueDate",
    "PKEY_EdgeGesture_DisableTouchWhenFullscreen",
    "PKEY_EndDate",
    "PKEY_ExpandoProperties",
    "PKEY_FileAllocationSize",
    "PKEY_FileAttributes",
    "PKEY_FileCount",
    "PKEY_FileDescription",
    "PKEY_FileExtension",
    "PKEY_FileFRN",
    "PKEY_FileName",
    "PKEY_FileOfflineAvailabilityStatus",
    "PKEY_FileOwner",
    "PKEY_FilePlaceholderStatus",
    "PKEY_FileVersion",
    "PKEY_FindData",
    "PKEY_FlagColor",
    "PKEY_FlagColorText",
    "PKEY_FlagStatus",
    "PKEY_FlagStatusText",
    "PKEY_FolderKind",
    "PKEY_FolderNameDisplay",
    "PKEY_FreeSpace",
    "PKEY_FullText",
    "PKEY_GPS_Altitude",
    "PKEY_GPS_AltitudeDenominator",
    "PKEY_GPS_AltitudeNumerator",
    "PKEY_GPS_AltitudeRef",
    "PKEY_GPS_AreaInformation",
    "PKEY_GPS_DOP",
    "PKEY_GPS_DOPDenominator",
    "PKEY_GPS_DOPNumerator",
    "PKEY_GPS_Date",
    "PKEY_GPS_DestBearing",
    "PKEY_GPS_DestBearingDenominator",
    "PKEY_GPS_DestBearingNumerator",
    "PKEY_GPS_DestBearingRef",
    "PKEY_GPS_DestDistance",
    "PKEY_GPS_DestDistanceDenominator",
    "PKEY_GPS_DestDistanceNumerator",
    "PKEY_GPS_DestDistanceRef",
    "PKEY_GPS_DestLatitude",
    "PKEY_GPS_DestLatitudeDenominator",
    "PKEY_GPS_DestLatitudeNumerator",
    "PKEY_GPS_DestLatitudeRef",
    "PKEY_GPS_DestLongitude",
    "PKEY_GPS_DestLongitudeDenominator",
    "PKEY_GPS_DestLongitudeNumerator",
    "PKEY_GPS_DestLongitudeRef",
    "PKEY_GPS_Differential",
    "PKEY_GPS_ImgDirection",
    "PKEY_GPS_ImgDirectionDenominator",
    "PKEY_GPS_ImgDirectionNumerator",
    "PKEY_GPS_ImgDirectionRef",
    "PKEY_GPS_Latitude",
    "PKEY_GPS_LatitudeDecimal",
    "PKEY_GPS_LatitudeDenominator",
    "PKEY_GPS_LatitudeNumerator",
    "PKEY_GPS_LatitudeRef",
    "PKEY_GPS_Longitude",
    "PKEY_GPS_LongitudeDecimal",
    "PKEY_GPS_LongitudeDenominator",
    "PKEY_GPS_LongitudeNumerator",
    "PKEY_GPS_LongitudeRef",
    "PKEY_GPS_MapDatum",
    "PKEY_GPS_MeasureMode",
    "PKEY_GPS_ProcessingMethod",
    "PKEY_GPS_Satellites",
    "PKEY_GPS_Speed",
    "PKEY_GPS_SpeedDenominator",
    "PKEY_GPS_SpeedNumerator",
    "PKEY_GPS_SpeedRef",
    "PKEY_GPS_Status",
    "PKEY_GPS_Track",
    "PKEY_GPS_TrackDenominator",
    "PKEY_GPS_TrackNumerator",
    "PKEY_GPS_TrackRef",
    "PKEY_GPS_VersionID",
    "PKEY_HighKeywords",
    "PKEY_History_SelectionCount",
    "PKEY_History_TargetUrlHostName",
    "PKEY_History_VisitCount",
    "PKEY_Identity",
    "PKEY_IdentityProvider_Name",
    "PKEY_IdentityProvider_Picture",
    "PKEY_Identity_Blob",
    "PKEY_Identity_DisplayName",
    "PKEY_Identity_InternetSid",
    "PKEY_Identity_IsMeIdentity",
    "PKEY_Identity_KeyProviderContext",
    "PKEY_Identity_KeyProviderName",
    "PKEY_Identity_LogonStatusString",
    "PKEY_Identity_PrimaryEmailAddress",
    "PKEY_Identity_PrimarySid",
    "PKEY_Identity_ProviderData",
    "PKEY_Identity_ProviderID",
    "PKEY_Identity_QualifiedUserName",
    "PKEY_Identity_UniqueID",
    "PKEY_Identity_UserName",
    "PKEY_ImageParsingName",
    "PKEY_Image_BitDepth",
    "PKEY_Image_ColorSpace",
    "PKEY_Image_CompressedBitsPerPixel",
    "PKEY_Image_CompressedBitsPerPixelDenominator",
    "PKEY_Image_CompressedBitsPerPixelNumerator",
    "PKEY_Image_Compression",
    "PKEY_Image_CompressionText",
    "PKEY_Image_Dimensions",
    "PKEY_Image_HorizontalResolution",
    "PKEY_Image_HorizontalSize",
    "PKEY_Image_ImageID",
    "PKEY_Image_ResolutionUnit",
    "PKEY_Image_VerticalResolution",
    "PKEY_Image_VerticalSize",
    "PKEY_Importance",
    "PKEY_ImportanceText",
    "PKEY_InfoTipText",
    "PKEY_InternalName",
    "PKEY_IsAttachment",
    "PKEY_IsDefaultNonOwnerSaveLocation",
    "PKEY_IsDefaultSaveLocation",
    "PKEY_IsDeleted",
    "PKEY_IsEncrypted",
    "PKEY_IsFlagged",
    "PKEY_IsFlaggedComplete",
    "PKEY_IsIncomplete",
    "PKEY_IsLocationSupported",
    "PKEY_IsPinnedToNameSpaceTree",
    "PKEY_IsRead",
    "PKEY_IsSearchOnlyItem",
    "PKEY_IsSendToTarget",
    "PKEY_IsShared",
    "PKEY_ItemAuthors",
    "PKEY_ItemClassType",
    "PKEY_ItemDate",
    "PKEY_ItemFolderNameDisplay",
    "PKEY_ItemFolderPathDisplay",
    "PKEY_ItemFolderPathDisplayNarrow",
    "PKEY_ItemName",
    "PKEY_ItemNameDisplay",
    "PKEY_ItemNameDisplayWithoutExtension",
    "PKEY_ItemNamePrefix",
    "PKEY_ItemNameSortOverride",
    "PKEY_ItemParticipants",
    "PKEY_ItemPathDisplay",
    "PKEY_ItemPathDisplayNarrow",
    "PKEY_ItemSubType",
    "PKEY_ItemType",
    "PKEY_ItemTypeText",
    "PKEY_ItemUrl",
    "PKEY_Journal_Contacts",
    "PKEY_Journal_EntryType",
    "PKEY_Keywords",
    "PKEY_Kind",
    "PKEY_KindText",
    "PKEY_Language",
    "PKEY_LastSyncError",
    "PKEY_LastSyncWarning",
    "PKEY_LastWriterPackageFamilyName",
    "PKEY_LayoutPattern_ContentViewModeForBrowse",
    "PKEY_LayoutPattern_ContentViewModeForSearch",
    "PKEY_LibraryLocationsCount",
    "PKEY_Link_Arguments",
    "PKEY_Link_Comment",
    "PKEY_Link_DateVisited",
    "PKEY_Link_Description",
    "PKEY_Link_FeedItemLocalId",
    "PKEY_Link_Status",
    "PKEY_Link_TargetExtension",
    "PKEY_Link_TargetParsingPath",
    "PKEY_Link_TargetSFGAOFlags",
    "PKEY_Link_TargetSFGAOFlagsStrings",
    "PKEY_Link_TargetUrl",
    "PKEY_Link_TargetUrlHostName",
    "PKEY_Link_TargetUrlPath",
    "PKEY_LowKeywords",
    "PKEY_MIMEType",
    "PKEY_Media_AuthorUrl",
    "PKEY_Media_AverageLevel",
    "PKEY_Media_ClassPrimaryID",
    "PKEY_Media_ClassSecondaryID",
    "PKEY_Media_CollectionGroupID",
    "PKEY_Media_CollectionID",
    "PKEY_Media_ContentDistributor",
    "PKEY_Media_ContentID",
    "PKEY_Media_CreatorApplication",
    "PKEY_Media_CreatorApplicationVersion",
    "PKEY_Media_DVDID",
    "PKEY_Media_DateEncoded",
    "PKEY_Media_DateReleased",
    "PKEY_Media_DlnaProfileID",
    "PKEY_Media_Duration",
    "PKEY_Media_EncodedBy",
    "PKEY_Media_EncodingSettings",
    "PKEY_Media_EpisodeNumber",
    "PKEY_Media_FrameCount",
    "PKEY_Media_MCDI",
    "PKEY_Media_MetadataContentProvider",
    "PKEY_Media_Producer",
    "PKEY_Media_PromotionUrl",
    "PKEY_Media_ProtectionType",
    "PKEY_Media_ProviderRating",
    "PKEY_Media_ProviderStyle",
    "PKEY_Media_Publisher",
    "PKEY_Media_SeasonNumber",
    "PKEY_Media_SeriesName",
    "PKEY_Media_SubTitle",
    "PKEY_Media_SubscriptionContentId",
    "PKEY_Media_ThumbnailLargePath",
    "PKEY_Media_ThumbnailLargeUri",
    "PKEY_Media_ThumbnailSmallPath",
    "PKEY_Media_ThumbnailSmallUri",
    "PKEY_Media_UniqueFileIdentifier",
    "PKEY_Media_UserNoAutoInfo",
    "PKEY_Media_UserWebUrl",
    "PKEY_Media_Writer",
    "PKEY_Media_Year",
    "PKEY_MediumKeywords",
    "PKEY_Message_AttachmentContents",
    "PKEY_Message_AttachmentNames",
    "PKEY_Message_BccAddress",
    "PKEY_Message_BccName",
    "PKEY_Message_CcAddress",
    "PKEY_Message_CcName",
    "PKEY_Message_ConversationID",
    "PKEY_Message_ConversationIndex",
    "PKEY_Message_DateReceived",
    "PKEY_Message_DateSent",
    "PKEY_Message_Flags",
    "PKEY_Message_FromAddress",
    "PKEY_Message_FromName",
    "PKEY_Message_HasAttachments",
    "PKEY_Message_IsFwdOrReply",
    "PKEY_Message_MessageClass",
    "PKEY_Message_Participants",
    "PKEY_Message_ProofInProgress",
    "PKEY_Message_SenderAddress",
    "PKEY_Message_SenderName",
    "PKEY_Message_Store",
    "PKEY_Message_ToAddress",
    "PKEY_Message_ToDoFlags",
    "PKEY_Message_ToDoTitle",
    "PKEY_Message_ToName",
    "PKEY_MileageInformation",
    "PKEY_Music_AlbumArtist",
    "PKEY_Music_AlbumArtistSortOverride",
    "PKEY_Music_AlbumID",
    "PKEY_Music_AlbumTitle",
    "PKEY_Music_AlbumTitleSortOverride",
    "PKEY_Music_Artist",
    "PKEY_Music_ArtistSortOverride",
    "PKEY_Music_BeatsPerMinute",
    "PKEY_Music_Composer",
    "PKEY_Music_ComposerSortOverride",
    "PKEY_Music_Conductor",
    "PKEY_Music_ContentGroupDescription",
    "PKEY_Music_DiscNumber",
    "PKEY_Music_DisplayArtist",
    "PKEY_Music_Genre",
    "PKEY_Music_InitialKey",
    "PKEY_Music_IsCompilation",
    "PKEY_Music_Lyrics",
    "PKEY_Music_Mood",
    "PKEY_Music_PartOfSet",
    "PKEY_Music_Period",
    "PKEY_Music_SynchronizedLyrics",
    "PKEY_Music_TrackNumber",
    "PKEY_NamespaceCLSID",
    "PKEY_Note_Color",
    "PKEY_Note_ColorText",
    "PKEY_Null",
    "PKEY_OfflineAvailability",
    "PKEY_OfflineStatus",
    "PKEY_OriginalFileName",
    "PKEY_OwnerSID",
    "PKEY_ParentalRating",
    "PKEY_ParentalRatingReason",
    "PKEY_ParentalRatingsOrganization",
    "PKEY_ParsingBindContext",
    "PKEY_ParsingName",
    "PKEY_ParsingPath",
    "PKEY_PerceivedType",
    "PKEY_PercentFull",
    "PKEY_Photo_Aperture",
    "PKEY_Photo_ApertureDenominator",
    "PKEY_Photo_ApertureNumerator",
    "PKEY_Photo_Brightness",
    "PKEY_Photo_BrightnessDenominator",
    "PKEY_Photo_BrightnessNumerator",
    "PKEY_Photo_CameraManufacturer",
    "PKEY_Photo_CameraModel",
    "PKEY_Photo_CameraSerialNumber",
    "PKEY_Photo_Contrast",
    "PKEY_Photo_ContrastText",
    "PKEY_Photo_DateTaken",
    "PKEY_Photo_DigitalZoom",
    "PKEY_Photo_DigitalZoomDenominator",
    "PKEY_Photo_DigitalZoomNumerator",
    "PKEY_Photo_EXIFVersion",
    "PKEY_Photo_Event",
    "PKEY_Photo_ExposureBias",
    "PKEY_Photo_ExposureBiasDenominator",
    "PKEY_Photo_ExposureBiasNumerator",
    "PKEY_Photo_ExposureIndex",
    "PKEY_Photo_ExposureIndexDenominator",
    "PKEY_Photo_ExposureIndexNumerator",
    "PKEY_Photo_ExposureProgram",
    "PKEY_Photo_ExposureProgramText",
    "PKEY_Photo_ExposureTime",
    "PKEY_Photo_ExposureTimeDenominator",
    "PKEY_Photo_ExposureTimeNumerator",
    "PKEY_Photo_FNumber",
    "PKEY_Photo_FNumberDenominator",
    "PKEY_Photo_FNumberNumerator",
    "PKEY_Photo_Flash",
    "PKEY_Photo_FlashEnergy",
    "PKEY_Photo_FlashEnergyDenominator",
    "PKEY_Photo_FlashEnergyNumerator",
    "PKEY_Photo_FlashManufacturer",
    "PKEY_Photo_FlashModel",
    "PKEY_Photo_FlashText",
    "PKEY_Photo_FocalLength",
    "PKEY_Photo_FocalLengthDenominator",
    "PKEY_Photo_FocalLengthInFilm",
    "PKEY_Photo_FocalLengthNumerator",
    "PKEY_Photo_FocalPlaneXResolution",
    "PKEY_Photo_FocalPlaneXResolutionDenominator",
    "PKEY_Photo_FocalPlaneXResolutionNumerator",
    "PKEY_Photo_FocalPlaneYResolution",
    "PKEY_Photo_FocalPlaneYResolutionDenominator",
    "PKEY_Photo_FocalPlaneYResolutionNumerator",
    "PKEY_Photo_GainControl",
    "PKEY_Photo_GainControlDenominator",
    "PKEY_Photo_GainControlNumerator",
    "PKEY_Photo_GainControlText",
    "PKEY_Photo_ISOSpeed",
    "PKEY_Photo_LensManufacturer",
    "PKEY_Photo_LensModel",
    "PKEY_Photo_LightSource",
    "PKEY_Photo_MakerNote",
    "PKEY_Photo_MakerNoteOffset",
    "PKEY_Photo_MaxAperture",
    "PKEY_Photo_MaxApertureDenominator",
    "PKEY_Photo_MaxApertureNumerator",
    "PKEY_Photo_MeteringMode",
    "PKEY_Photo_MeteringModeText",
    "PKEY_Photo_Orientation",
    "PKEY_Photo_OrientationText",
    "PKEY_Photo_PeopleNames",
    "PKEY_Photo_PhotometricInterpretation",
    "PKEY_Photo_PhotometricInterpretationText",
    "PKEY_Photo_ProgramMode",
    "PKEY_Photo_ProgramModeText",
    "PKEY_Photo_RelatedSoundFile",
    "PKEY_Photo_Saturation",
    "PKEY_Photo_SaturationText",
    "PKEY_Photo_Sharpness",
    "PKEY_Photo_SharpnessText",
    "PKEY_Photo_ShutterSpeed",
    "PKEY_Photo_ShutterSpeedDenominator",
    "PKEY_Photo_ShutterSpeedNumerator",
    "PKEY_Photo_SubjectDistance",
    "PKEY_Photo_SubjectDistanceDenominator",
    "PKEY_Photo_SubjectDistanceNumerator",
    "PKEY_Photo_TagViewAggregate",
    "PKEY_Photo_TranscodedForSync",
    "PKEY_Photo_WhiteBalance",
    "PKEY_Photo_WhiteBalanceText",
    "PKEY_Priority",
    "PKEY_PriorityText",
    "PKEY_Project",
    "PKEY_PropGroup_Advanced",
    "PKEY_PropGroup_Audio",
    "PKEY_PropGroup_Calendar",
    "PKEY_PropGroup_Camera",
    "PKEY_PropGroup_Contact",
    "PKEY_PropGroup_Content",
    "PKEY_PropGroup_Description",
    "PKEY_PropGroup_FileSystem",
    "PKEY_PropGroup_GPS",
    "PKEY_PropGroup_General",
    "PKEY_PropGroup_Image",
    "PKEY_PropGroup_Media",
    "PKEY_PropGroup_MediaAdvanced",
    "PKEY_PropGroup_Message",
    "PKEY_PropGroup_Music",
    "PKEY_PropGroup_Origin",
    "PKEY_PropGroup_PhotoAdvanced",
    "PKEY_PropGroup_RecordedTV",
    "PKEY_PropGroup_Video",
    "PKEY_PropList_ConflictPrompt",
    "PKEY_PropList_ContentViewModeForBrowse",
    "PKEY_PropList_ContentViewModeForSearch",
    "PKEY_PropList_ExtendedTileInfo",
    "PKEY_PropList_FileOperationPrompt",
    "PKEY_PropList_FullDetails",
    "PKEY_PropList_InfoTip",
    "PKEY_PropList_NonPersonal",
    "PKEY_PropList_PreviewDetails",
    "PKEY_PropList_PreviewTitle",
    "PKEY_PropList_QuickTip",
    "PKEY_PropList_TileInfo",
    "PKEY_PropList_XPDetailsPanel",
    "PKEY_ProviderItemID",
    "PKEY_Rating",
    "PKEY_RatingText",
    "PKEY_RecordedTV_ChannelNumber",
    "PKEY_RecordedTV_Credits",
    "PKEY_RecordedTV_DateContentExpires",
    "PKEY_RecordedTV_EpisodeName",
    "PKEY_RecordedTV_IsATSCContent",
    "PKEY_RecordedTV_IsClosedCaptioningAvailable",
    "PKEY_RecordedTV_IsDTVContent",
    "PKEY_RecordedTV_IsHDContent",
    "PKEY_RecordedTV_IsRepeatBroadcast",
    "PKEY_RecordedTV_IsSAP",
    "PKEY_RecordedTV_NetworkAffiliation",
    "PKEY_RecordedTV_OriginalBroadcastDate",
    "PKEY_RecordedTV_ProgramDescription",
    "PKEY_RecordedTV_RecordingTime",
    "PKEY_RecordedTV_StationCallSign",
    "PKEY_RecordedTV_StationName",
    "PKEY_RemoteConflictingFile",
    "PKEY_SFGAOFlags",
    "PKEY_Search_AutoSummary",
    "PKEY_Search_ContainerHash",
    "PKEY_Search_Contents",
    "PKEY_Search_EntryID",
    "PKEY_Search_ExtendedProperties",
    "PKEY_Search_GatherTime",
    "PKEY_Search_HitCount",
    "PKEY_Search_IsClosedDirectory",
    "PKEY_Search_IsFullyContained",
    "PKEY_Search_QueryFocusedSummary",
    "PKEY_Search_QueryFocusedSummaryWithFallback",
    "PKEY_Search_QueryPropertyHits",
    "PKEY_Search_Rank",
    "PKEY_Search_Store",
    "PKEY_Search_UrlToIndex",
    "PKEY_Search_UrlToIndexWithModificationTime",
    "PKEY_Security_AllowedEnterpriseDataProtectionIdentities",
    "PKEY_Security_EncryptionOwners",
    "PKEY_Security_EncryptionOwnersDisplay",
    "PKEY_Sensitivity",
    "PKEY_SensitivityText",
    "PKEY_ShareUserRating",
    "PKEY_SharedWith",
    "PKEY_SharingStatus",
    "PKEY_Shell_OmitFromView",
    "PKEY_Shell_SFGAOFlagsStrings",
    "PKEY_SimpleRating",
    "PKEY_Size",
    "PKEY_SoftwareUsed",
    "PKEY_Software_DateLastUsed",
    "PKEY_Software_ProductName",
    "PKEY_SourceItem",
    "PKEY_SourcePackageFamilyName",
    "PKEY_StartDate",
    "PKEY_Status",
    "PKEY_StatusBarSelectedItemCount",
    "PKEY_StatusBarViewItemCount",
    "PKEY_StorageProviderCallerVersionInformation",
    "PKEY_StorageProviderError",
    "PKEY_StorageProviderFileChecksum",
    "PKEY_StorageProviderFileFlags",
    "PKEY_StorageProviderFileHasConflict",
    "PKEY_StorageProviderFileIdentifier",
    "PKEY_StorageProviderFileRemoteUri",
    "PKEY_StorageProviderFileVersion",
    "PKEY_StorageProviderFileVersionWaterline",
    "PKEY_StorageProviderId",
    "PKEY_StorageProviderShareStatuses",
    "PKEY_StorageProviderSharingStatus",
    "PKEY_StorageProviderStatus",
    "PKEY_Storage_Portable",
    "PKEY_Storage_RemovableMedia",
    "PKEY_Storage_SystemCritical",
    "PKEY_Subject",
    "PKEY_Supplemental_Album",
    "PKEY_Supplemental_AlbumID",
    "PKEY_Supplemental_Location",
    "PKEY_Supplemental_Person",
    "PKEY_Supplemental_ResourceId",
    "PKEY_Supplemental_Tag",
    "PKEY_SyncTransferStatus",
    "PKEY_Sync_Comments",
    "PKEY_Sync_ConflictDescription",
    "PKEY_Sync_ConflictFirstLocation",
    "PKEY_Sync_ConflictSecondLocation",
    "PKEY_Sync_HandlerCollectionID",
    "PKEY_Sync_HandlerID",
    "PKEY_Sync_HandlerName",
    "PKEY_Sync_HandlerType",
    "PKEY_Sync_HandlerTypeLabel",
    "PKEY_Sync_ItemID",
    "PKEY_Sync_ItemName",
    "PKEY_Sync_ProgressPercentage",
    "PKEY_Sync_State",
    "PKEY_Sync_Status",
    "PKEY_Task_BillingInformation",
    "PKEY_Task_CompletionStatus",
    "PKEY_Task_Owner",
    "PKEY_Thumbnail",
    "PKEY_ThumbnailCacheId",
    "PKEY_ThumbnailStream",
    "PKEY_Title",
    "PKEY_TitleSortOverride",
    "PKEY_TotalFileSize",
    "PKEY_Trademarks",
    "PKEY_TransferOrder",
    "PKEY_TransferPosition",
    "PKEY_TransferSize",
    "PKEY_Video_Compression",
    "PKEY_Video_Director",
    "PKEY_Video_EncodingBitrate",
    "PKEY_Video_FourCC",
    "PKEY_Video_FrameHeight",
    "PKEY_Video_FrameRate",
    "PKEY_Video_FrameWidth",
    "PKEY_Video_HorizontalAspectRatio",
    "PKEY_Video_IsSpherical",
    "PKEY_Video_IsStereo",
    "PKEY_Video_Orientation",
    "PKEY_Video_SampleSize",
    "PKEY_Video_StreamName",
    "PKEY_Video_StreamNumber",
    "PKEY_Video_TotalBitrate",
    "PKEY_Video_TranscodedForSync",
    "PKEY_Video_VerticalAspectRatio",
    "PKEY_VolumeId",
    "PKEY_Volume_FileSystem",
    "PKEY_Volume_IsMappedDrive",
    "PKEY_Volume_IsRoot",
    "PKEY_ZoneIdentifier",
    "PLAYBACKSTATE_NOMEDIA",
    "PLAYBACKSTATE_PAUSED",
    "PLAYBACKSTATE_PLAYING",
    "PLAYBACKSTATE_RECORDING",
    "PLAYBACKSTATE_RECORDINGPAUSED",
    "PLAYBACKSTATE_STOPPED",
    "PLAYBACKSTATE_TRANSITIONING",
    "PLAYBACKSTATE_UNKNOWN",
    "RATING_FIVE_STARS_MAX",
    "RATING_FIVE_STARS_MIN",
    "RATING_FIVE_STARS_SET",
    "RATING_FOUR_STARS_MAX",
    "RATING_FOUR_STARS_MIN",
    "RATING_FOUR_STARS_SET",
    "RATING_ONE_STAR_MAX",
    "RATING_ONE_STAR_MIN",
    "RATING_ONE_STAR_SET",
    "RATING_THREE_STARS_MAX",
    "RATING_THREE_STARS_MIN",
    "RATING_THREE_STARS_SET",
    "RATING_TWO_STARS_MAX",
    "RATING_TWO_STARS_MIN",
    "RATING_TWO_STARS_SET",
    "SFGAOSTR_BROWSABLE",
    "SFGAOSTR_FILEANC",
    "SFGAOSTR_FILESYS",
    "SFGAOSTR_FOLDER",
    "SFGAOSTR_HIDDEN",
    "SFGAOSTR_LINK",
    "SFGAOSTR_NONENUM",
    "SFGAOSTR_PLACEHOLDER",
    "SFGAOSTR_STORAGEANC",
    "SFGAOSTR_STREAM",
    "SFGAOSTR_SUPERHIDDEN",
    "SFGAOSTR_SYSTEM",
    "SHARINGSTATUS_NOTSHARED",
    "SHARINGSTATUS_PRIVATE",
    "SHARINGSTATUS_SHARED",
    "SILO_INFO",
    "STORAGE_PROVIDER_SHARE_STATUS_GROUP",
    "STORAGE_PROVIDER_SHARE_STATUS_OWNER",
    "STORAGE_PROVIDER_SHARE_STATUS_PRIVATE",
    "STORAGE_PROVIDER_SHARE_STATUS_PUBLIC",
    "STORAGE_PROVIDER_SHARE_STATUS_SHARED",
    "STORAGE_PROVIDER_SHARINGSTATUS_NOTSHARED",
    "STORAGE_PROVIDER_SHARINGSTATUS_PRIVATE",
    "STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC",
    "STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_COOWNED",
    "STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_OWNED",
    "STORAGE_PROVIDER_SHARINGSTATUS_SHARED",
    "STORAGE_PROVIDER_SHARINGSTATUS_SHARED_COOWNED",
    "STORAGE_PROVIDER_SHARINGSTATUS_SHARED_OWNED",
    "SYNC_HANDLERTYPE_COMPUTERS",
    "SYNC_HANDLERTYPE_DEVICES",
    "SYNC_HANDLERTYPE_FOLDERS",
    "SYNC_HANDLERTYPE_OTHER",
    "SYNC_HANDLERTYPE_PROGRAMS",
    "SYNC_HANDLERTYPE_WEBSERVICES",
    "SYNC_STATE_ERROR",
    "SYNC_STATE_IDLE",
    "SYNC_STATE_NOTSETUP",
    "SYNC_STATE_PENDING",
    "SYNC_STATE_SYNCING",
    "SYNC_STATE_SYNCNOTRUN",
    "WPD_CATEGORY_ENHANCED_STORAGE",
]
_arch_optional = [
]
