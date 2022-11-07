from win32more import *
import win32more.Devices.PortableDevices
import win32more.Foundation
import win32more.Storage.EnhancedStorage
import win32more.System.Com
import win32more.UI.Shell.PropertiesSystem

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
GUID_DEVINTERFACE_ENHANCED_STORAGE_SILO = '3897f6a4-fd35-4bc8-a0b7-5dbba36adafa'
WPD_CATEGORY_ENHANCED_STORAGE = '91248166-b832-4ad4-baa4-7ca0b6b2798c'
ENHANCED_STORAGE_COMMAND_SILO_IS_AUTHENTICATION_SILO = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=6)
ENHANCED_STORAGE_COMMAND_SILO_GET_AUTHENTICATION_STATE = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=7)
ENHANCED_STORAGE_COMMAND_SILO_ENUMERATE_SILOS = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=11)
ENHANCED_STORAGE_COMMAND_CERT_HOST_CERTIFICATE_AUTHENTICATION = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=101)
ENHANCED_STORAGE_COMMAND_CERT_DEVICE_CERTIFICATE_AUTHENTICATION = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=102)
ENHANCED_STORAGE_COMMAND_CERT_ADMIN_CERTIFICATE_AUTHENTICATION = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=103)
ENHANCED_STORAGE_COMMAND_CERT_INITIALIZE_TO_MANUFACTURER_STATE = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=104)
ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE_COUNT = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=105)
ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=106)
ENHANCED_STORAGE_COMMAND_CERT_SET_CERTIFICATE = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=107)
ENHANCED_STORAGE_COMMAND_CERT_CREATE_CERTIFICATE_REQUEST = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=108)
ENHANCED_STORAGE_COMMAND_CERT_UNAUTHENTICATION = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=110)
ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITY = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=111)
ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITIES = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=112)
ENHANCED_STORAGE_COMMAND_CERT_GET_ACT_FRIENDLY_NAME = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=113)
ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_GUID = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=114)
ENHANCED_STORAGE_COMMAND_PASSWORD_AUTHORIZE_ACT_ACCESS = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=203)
ENHANCED_STORAGE_COMMAND_PASSWORD_UNAUTHORIZE_ACT_ACCESS = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=204)
ENHANCED_STORAGE_COMMAND_PASSWORD_QUERY_INFORMATION = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=205)
ENHANCED_STORAGE_COMMAND_PASSWORD_CONFIG_ADMINISTRATOR = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=206)
ENHANCED_STORAGE_COMMAND_PASSWORD_CREATE_USER = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=207)
ENHANCED_STORAGE_COMMAND_PASSWORD_DELETE_USER = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=208)
ENHANCED_STORAGE_COMMAND_PASSWORD_CHANGE_PASSWORD = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=209)
ENHANCED_STORAGE_COMMAND_PASSWORD_INITIALIZE_USER_PASSWORD = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=210)
ENHANCED_STORAGE_COMMAND_PASSWORD_START_INITIALIZE_TO_MANUFACTURER_STATE = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=211)
ENHANCED_STORAGE_PROPERTY_AUTHENTICATION_STATE = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=1006)
ENHANCED_STORAGE_AUTHN_STATE_UNKNOWN = 0
ENHANCED_STORAGE_AUTHN_STATE_NO_AUTHENTICATION_REQUIRED = 1
ENHANCED_STORAGE_AUTHN_STATE_NOT_AUTHENTICATED = 2
ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATED = 3
ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATION_DENIED = 2147483649
ENHANCED_STORAGE_AUTHN_STATE_DEVICE_ERROR = 2147483650
ENHANCED_STORAGE_PROPERTY_IS_AUTHENTICATION_SILO = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=1009)
ENHANCED_STORAGE_PROPERTY_TEMPORARY_UNAUTHENTICATION = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=1010)
ENHANCED_STORAGE_PROPERTY_MAX_AUTH_FAILURES = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2001)
ENHANCED_STORAGE_PROPERTY_PASSWORD = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2004)
ENHANCED_STORAGE_PROPERTY_OLD_PASSWORD = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2005)
ENHANCED_STORAGE_PROPERTY_PASSWORD_INDICATOR = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2006)
ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD_INDICATOR = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2007)
ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2008)
ENHANCED_STORAGE_PROPERTY_USER_HINT = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2009)
ENHANCED_STORAGE_PROPERTY_USER_NAME = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2010)
ENHANCED_STORAGE_PROPERTY_ADMIN_HINT = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2011)
ENHANCED_STORAGE_PROPERTY_SILO_NAME = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2012)
ENHANCED_STORAGE_PROPERTY_SILO_FRIENDLYNAME_SPECIFIED = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2013)
ENHANCED_STORAGE_PROPERTY_PASSWORD_SILO_INFO = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2014)
ENHANCED_STORAGE_PROPERTY_SECURITY_IDENTIFIER = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2015)
ENHANCED_STORAGE_PROPERTY_QUERY_SILO_TYPE = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2016)
ENHANCED_STORAGE_PROPERTY_QUERY_SILO_RESULTS = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=2017)
ENHANCED_STORAGE_PROPERTY_MAX_CERTIFICATE_COUNT = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3001)
ENHANCED_STORAGE_PROPERTY_STORED_CERTIFICATE_COUNT = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3002)
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_INDEX = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3003)
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_TYPE = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3004)
CERT_TYPE_EMPTY = 0
CERT_TYPE_ASCm = 1
CERT_TYPE_PCp = 2
CERT_TYPE_ASCh = 3
CERT_TYPE_HCh = 4
CERT_TYPE_SIGNER = 6
ENHANCED_STORAGE_PROPERTY_VALIDATION_POLICY = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3005)
CERT_VALIDATION_POLICY_RESERVED = 0
CERT_VALIDATION_POLICY_NONE = 1
CERT_VALIDATION_POLICY_BASIC = 2
CERT_VALIDATION_POLICY_EXTENDED = 3
ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_INDEX = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3006)
ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_OF_TYPE_INDEX = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3007)
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_LENGTH = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3008)
ENHANCED_STORAGE_PROPERTY_CERTIFICATE = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3009)
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_REQUEST = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3010)
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_CAPABILITY_TYPE = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3011)
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITY = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3012)
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITIES = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3013)
CERT_CAPABILITY_HASH_ALG = 1
CERT_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY = 2
CERT_CAPABILITY_SIGNATURE_ALG = 3
CERT_CAPABILITY_CERTIFICATE_SUPPORT = 4
CERT_CAPABILITY_OPTIONAL_FEATURES = 5
CERT_MAX_CAPABILITY = 255
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_ACT_FRIENDLY_NAME = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3014)
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_GUID = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3015)
ENHANCED_STORAGE_PROPERTY_SIGNER_CERTIFICATE_INDEX = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=3016)
ENHANCED_STORAGE_CAPABILITY_HASH_ALGS = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=4001)
ENHANCED_STORAGE_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=4002)
ENHANCED_STORAGE_CAPABILITY_SIGNING_ALGS = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=4003)
ENHANCED_STORAGE_CAPABILITY_RENDER_USER_DATA_UNUSABLE = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=4004)
ENHANCED_STORAGE_CAPABILITY_CERTIFICATE_EXTENSION_PARSING = PROPERTYKEY(Fmtid='91248166-b832-4ad4-baa4-7ca0b6b2798c', Pid=4005)
PKEY_Address_Country = PROPERTYKEY(Fmtid='c07b4199-e1df-4493-b1e1-de5946fb58f8', Pid=100)
PKEY_Address_CountryCode = PROPERTYKEY(Fmtid='c07b4199-e1df-4493-b1e1-de5946fb58f8', Pid=101)
PKEY_Address_Region = PROPERTYKEY(Fmtid='c07b4199-e1df-4493-b1e1-de5946fb58f8', Pid=102)
PKEY_Address_RegionCode = PROPERTYKEY(Fmtid='c07b4199-e1df-4493-b1e1-de5946fb58f8', Pid=103)
PKEY_Address_Town = PROPERTYKEY(Fmtid='c07b4199-e1df-4493-b1e1-de5946fb58f8', Pid=104)
PKEY_Audio_ChannelCount = PROPERTYKEY(Fmtid='64440490-4c8b-11d1-8b70-080036b11a03', Pid=7)
AUDIO_CHANNELCOUNT_MONO = 1
AUDIO_CHANNELCOUNT_STEREO = 2
PKEY_Audio_Compression = PROPERTYKEY(Fmtid='64440490-4c8b-11d1-8b70-080036b11a03', Pid=10)
PKEY_Audio_EncodingBitrate = PROPERTYKEY(Fmtid='64440490-4c8b-11d1-8b70-080036b11a03', Pid=4)
PKEY_Audio_Format = PROPERTYKEY(Fmtid='64440490-4c8b-11d1-8b70-080036b11a03', Pid=2)
PKEY_Audio_IsVariableBitRate = PROPERTYKEY(Fmtid='e6822fee-8c17-4d62-823c-8e9cfcbd1d5c', Pid=100)
PKEY_Audio_PeakValue = PROPERTYKEY(Fmtid='2579e5d0-1116-4084-bd9a-9b4f7cb4df5e', Pid=100)
PKEY_Audio_SampleRate = PROPERTYKEY(Fmtid='64440490-4c8b-11d1-8b70-080036b11a03', Pid=5)
PKEY_Audio_SampleSize = PROPERTYKEY(Fmtid='64440490-4c8b-11d1-8b70-080036b11a03', Pid=6)
PKEY_Audio_StreamName = PROPERTYKEY(Fmtid='64440490-4c8b-11d1-8b70-080036b11a03', Pid=9)
PKEY_Audio_StreamNumber = PROPERTYKEY(Fmtid='64440490-4c8b-11d1-8b70-080036b11a03', Pid=8)
PKEY_Calendar_Duration = PROPERTYKEY(Fmtid='293ca35a-09aa-4dd2-b180-1fe245728a52', Pid=100)
PKEY_Calendar_IsOnline = PROPERTYKEY(Fmtid='bfee9149-e3e2-49a7-a862-c05988145cec', Pid=100)
PKEY_Calendar_IsRecurring = PROPERTYKEY(Fmtid='315b9c8d-80a9-4ef9-ae16-8e746da51d70', Pid=100)
PKEY_Calendar_Location = PROPERTYKEY(Fmtid='f6272d18-cecc-40b1-b26a-3911717aa7bd', Pid=100)
PKEY_Calendar_OptionalAttendeeAddresses = PROPERTYKEY(Fmtid='d55bae5a-3892-417a-a649-c6ac5aaaeab3', Pid=100)
PKEY_Calendar_OptionalAttendeeNames = PROPERTYKEY(Fmtid='09429607-582d-437f-84c3-de93a2b24c3c', Pid=100)
PKEY_Calendar_OrganizerAddress = PROPERTYKEY(Fmtid='744c8242-4df5-456c-ab9e-014efb9021e3', Pid=100)
PKEY_Calendar_OrganizerName = PROPERTYKEY(Fmtid='aaa660f9-9865-458e-b484-01bc7fe3973e', Pid=100)
PKEY_Calendar_ReminderTime = PROPERTYKEY(Fmtid='72fc5ba4-24f9-4011-9f3f-add27afad818', Pid=100)
PKEY_Calendar_RequiredAttendeeAddresses = PROPERTYKEY(Fmtid='0ba7d6c3-568d-4159-ab91-781a91fb71e5', Pid=100)
PKEY_Calendar_RequiredAttendeeNames = PROPERTYKEY(Fmtid='b33af30b-f552-4584-936c-cb93e5cda29f', Pid=100)
PKEY_Calendar_Resources = PROPERTYKEY(Fmtid='00f58a38-c54b-4c40-8696-97235980eae1', Pid=100)
PKEY_Calendar_ResponseStatus = PROPERTYKEY(Fmtid='188c1f91-3c40-4132-9ec5-d8b03b72a8a2', Pid=100)
PKEY_Calendar_ShowTimeAs = PROPERTYKEY(Fmtid='5bf396d4-5eb2-466f-bde9-2fb3f2361d6e', Pid=100)
PKEY_Calendar_ShowTimeAsText = PROPERTYKEY(Fmtid='53da57cf-62c0-45c4-81de-7610bcefd7f5', Pid=100)
PKEY_Communication_AccountName = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=9)
PKEY_Communication_DateItemExpires = PROPERTYKEY(Fmtid='428040ac-a177-4c8a-9760-f6f761227f9a', Pid=100)
PKEY_Communication_Direction = PROPERTYKEY(Fmtid='8e531030-b960-4346-ae0d-66bc9a86fb94', Pid=100)
PKEY_Communication_FollowupIconIndex = PROPERTYKEY(Fmtid='83a6347e-6fe4-4f40-ba9c-c4865240d1f4', Pid=100)
PKEY_Communication_HeaderItem = PROPERTYKEY(Fmtid='c9c34f84-2241-4401-b607-bd20ed75ae7f', Pid=100)
PKEY_Communication_PolicyTag = PROPERTYKEY(Fmtid='ec0b4191-ab0b-4c66-90b6-c6637cdebbab', Pid=100)
PKEY_Communication_SecurityFlags = PROPERTYKEY(Fmtid='8619a4b6-9f4d-4429-8c0f-b996ca59e335', Pid=100)
PKEY_Communication_Suffix = PROPERTYKEY(Fmtid='807b653a-9e91-43ef-8f97-11ce04ee20c5', Pid=100)
PKEY_Communication_TaskStatus = PROPERTYKEY(Fmtid='be1a72c6-9a1d-46b7-afe7-afaf8cef4999', Pid=100)
PKEY_Communication_TaskStatusText = PROPERTYKEY(Fmtid='a6744477-c237-475b-a075-54f34498292a', Pid=100)
PKEY_Computer_DecoratedFreeSpace = PROPERTYKEY(Fmtid='9b174b35-40ff-11d2-a27e-00c04fc30871', Pid=7)
PKEY_Contact_AccountPictureDynamicVideo = PROPERTYKEY(Fmtid='0b8bb018-2725-4b44-92ba-7933aeb2dde7', Pid=2)
PKEY_Contact_AccountPictureLarge = PROPERTYKEY(Fmtid='0b8bb018-2725-4b44-92ba-7933aeb2dde7', Pid=3)
PKEY_Contact_AccountPictureSmall = PROPERTYKEY(Fmtid='0b8bb018-2725-4b44-92ba-7933aeb2dde7', Pid=4)
PKEY_Contact_Anniversary = PROPERTYKEY(Fmtid='9ad5badb-cea7-4470-a03d-b84e51b9949e', Pid=100)
PKEY_Contact_AssistantName = PROPERTYKEY(Fmtid='cd102c9c-5540-4a88-a6f6-64e4981c8cd1', Pid=100)
PKEY_Contact_AssistantTelephone = PROPERTYKEY(Fmtid='9a93244d-a7ad-4ff8-9b99-45ee4cc09af6', Pid=100)
PKEY_Contact_Birthday = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=47)
PKEY_Contact_BusinessAddress = PROPERTYKEY(Fmtid='730fb6dd-cf7c-426b-a03f-bd166cc9ee24', Pid=100)
PKEY_Contact_BusinessAddress1Country = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=119)
PKEY_Contact_BusinessAddress1Locality = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=117)
PKEY_Contact_BusinessAddress1PostalCode = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=120)
PKEY_Contact_BusinessAddress1Region = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=118)
PKEY_Contact_BusinessAddress1Street = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=116)
PKEY_Contact_BusinessAddress2Country = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=124)
PKEY_Contact_BusinessAddress2Locality = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=122)
PKEY_Contact_BusinessAddress2PostalCode = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=125)
PKEY_Contact_BusinessAddress2Region = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=123)
PKEY_Contact_BusinessAddress2Street = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=121)
PKEY_Contact_BusinessAddress3Country = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=129)
PKEY_Contact_BusinessAddress3Locality = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=127)
PKEY_Contact_BusinessAddress3PostalCode = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=130)
PKEY_Contact_BusinessAddress3Region = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=128)
PKEY_Contact_BusinessAddress3Street = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=126)
PKEY_Contact_BusinessAddressCity = PROPERTYKEY(Fmtid='402b5934-ec5a-48c3-93e6-85e86a2d934e', Pid=100)
PKEY_Contact_BusinessAddressCountry = PROPERTYKEY(Fmtid='b0b87314-fcf6-4feb-8dff-a50da6af561c', Pid=100)
PKEY_Contact_BusinessAddressPostalCode = PROPERTYKEY(Fmtid='e1d4a09e-d758-4cd1-b6ec-34a8b5a73f80', Pid=100)
PKEY_Contact_BusinessAddressPostOfficeBox = PROPERTYKEY(Fmtid='bc4e71ce-17f9-48d5-bee9-021df0ea5409', Pid=100)
PKEY_Contact_BusinessAddressState = PROPERTYKEY(Fmtid='446f787f-10c4-41cb-a6c4-4d0343551597', Pid=100)
PKEY_Contact_BusinessAddressStreet = PROPERTYKEY(Fmtid='ddd1460f-c0bf-4553-8ce4-10433c908fb0', Pid=100)
PKEY_Contact_BusinessEmailAddresses = PROPERTYKEY(Fmtid='f271c659-7e5e-471f-ba25-7f77b286f836', Pid=100)
PKEY_Contact_BusinessFaxNumber = PROPERTYKEY(Fmtid='91eff6f3-2e27-42ca-933e-7c999fbe310b', Pid=100)
PKEY_Contact_BusinessHomePage = PROPERTYKEY(Fmtid='56310920-2491-4919-99ce-eadb06fafdb2', Pid=100)
PKEY_Contact_BusinessTelephone = PROPERTYKEY(Fmtid='6a15e5a0-0a1e-4cd7-bb8c-d2f1b0c929bc', Pid=100)
PKEY_Contact_CallbackTelephone = PROPERTYKEY(Fmtid='bf53d1c3-49e0-4f7f-8567-5a821d8ac542', Pid=100)
PKEY_Contact_CarTelephone = PROPERTYKEY(Fmtid='8fdc6dea-b929-412b-ba90-397a257465fe', Pid=100)
PKEY_Contact_Children = PROPERTYKEY(Fmtid='d4729704-8ef1-43ef-9024-2bd381187fd5', Pid=100)
PKEY_Contact_CompanyMainTelephone = PROPERTYKEY(Fmtid='8589e481-6040-473d-b171-7fa89c2708ed', Pid=100)
PKEY_Contact_ConnectedServiceDisplayName = PROPERTYKEY(Fmtid='39b77f4f-a104-4863-b395-2db2ad8f7bc1', Pid=100)
PKEY_Contact_ConnectedServiceIdentities = PROPERTYKEY(Fmtid='80f41eb8-afc4-4208-aa5f-cce21a627281', Pid=100)
PKEY_Contact_ConnectedServiceName = PROPERTYKEY(Fmtid='b5c84c9e-5927-46b5-a3cc-933c21b78469', Pid=100)
PKEY_Contact_ConnectedServiceSupportedActions = PROPERTYKEY(Fmtid='a19fb7a9-024b-4371-a8bf-4d29c3e4e9c9', Pid=100)
PKEY_Contact_DataSuppliers = PROPERTYKEY(Fmtid='9660c283-fc3a-4a08-a096-eed3aac46da2', Pid=100)
PKEY_Contact_Department = PROPERTYKEY(Fmtid='fc9f7306-ff8f-4d49-9fb6-3ffe5c0951ec', Pid=100)
PKEY_Contact_DisplayBusinessPhoneNumbers = PROPERTYKEY(Fmtid='364028da-d895-41fe-a584-302b1bb70a76', Pid=100)
PKEY_Contact_DisplayHomePhoneNumbers = PROPERTYKEY(Fmtid='5068bcdf-d697-4d85-8c53-1f1cdab01763', Pid=100)
PKEY_Contact_DisplayMobilePhoneNumbers = PROPERTYKEY(Fmtid='9cb0c358-9d7a-46b1-b466-dcc6f1a3d93d', Pid=100)
PKEY_Contact_DisplayOtherPhoneNumbers = PROPERTYKEY(Fmtid='03089873-8ee8-4191-bd60-d31f72b7900b', Pid=100)
PKEY_Contact_EmailAddress = PROPERTYKEY(Fmtid='f8fa7fa3-d12b-4785-8a4e-691a94f7a3e7', Pid=100)
PKEY_Contact_EmailAddress2 = PROPERTYKEY(Fmtid='38965063-edc8-4268-8491-b7723172cf29', Pid=100)
PKEY_Contact_EmailAddress3 = PROPERTYKEY(Fmtid='644d37b4-e1b3-4bad-b099-7e7c04966aca', Pid=100)
PKEY_Contact_EmailAddresses = PROPERTYKEY(Fmtid='84d8f337-981d-44b3-9615-c7596dba17e3', Pid=100)
PKEY_Contact_EmailName = PROPERTYKEY(Fmtid='cc6f4f24-6083-4bd4-8754-674d0de87ab8', Pid=100)
PKEY_Contact_FileAsName = PROPERTYKEY(Fmtid='f1a24aa7-9ca7-40f6-89ec-97def9ffe8db', Pid=100)
PKEY_Contact_FirstName = PROPERTYKEY(Fmtid='14977844-6b49-4aad-a714-a4513bf60460', Pid=100)
PKEY_Contact_FullName = PROPERTYKEY(Fmtid='635e9051-50a5-4ba2-b9db-4ed056c77296', Pid=100)
PKEY_Contact_Gender = PROPERTYKEY(Fmtid='3c8cee58-d4f0-4cf9-b756-4e5d24447bcd', Pid=100)
PKEY_Contact_GenderValue = PROPERTYKEY(Fmtid='3c8cee58-d4f0-4cf9-b756-4e5d24447bcd', Pid=101)
PKEY_Contact_Hobbies = PROPERTYKEY(Fmtid='5dc2253f-5e11-4adf-9cfe-910dd01e3e70', Pid=100)
PKEY_Contact_HomeAddress = PROPERTYKEY(Fmtid='98f98354-617a-46b8-8560-5b1b64bf1f89', Pid=100)
PKEY_Contact_HomeAddress1Country = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=104)
PKEY_Contact_HomeAddress1Locality = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=102)
PKEY_Contact_HomeAddress1PostalCode = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=105)
PKEY_Contact_HomeAddress1Region = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=103)
PKEY_Contact_HomeAddress1Street = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=101)
PKEY_Contact_HomeAddress2Country = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=109)
PKEY_Contact_HomeAddress2Locality = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=107)
PKEY_Contact_HomeAddress2PostalCode = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=110)
PKEY_Contact_HomeAddress2Region = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=108)
PKEY_Contact_HomeAddress2Street = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=106)
PKEY_Contact_HomeAddress3Country = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=114)
PKEY_Contact_HomeAddress3Locality = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=112)
PKEY_Contact_HomeAddress3PostalCode = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=115)
PKEY_Contact_HomeAddress3Region = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=113)
PKEY_Contact_HomeAddress3Street = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=111)
PKEY_Contact_HomeAddressCity = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=65)
PKEY_Contact_HomeAddressCountry = PROPERTYKEY(Fmtid='08a65aa1-f4c9-43dd-9ddf-a33d8e7ead85', Pid=100)
PKEY_Contact_HomeAddressPostalCode = PROPERTYKEY(Fmtid='8afcc170-8a46-4b53-9eee-90bae7151e62', Pid=100)
PKEY_Contact_HomeAddressPostOfficeBox = PROPERTYKEY(Fmtid='7b9f6399-0a3f-4b12-89bd-4adc51c918af', Pid=100)
PKEY_Contact_HomeAddressState = PROPERTYKEY(Fmtid='c89a23d0-7d6d-4eb8-87d4-776a82d493e5', Pid=100)
PKEY_Contact_HomeAddressStreet = PROPERTYKEY(Fmtid='0adef160-db3f-4308-9a21-06237b16fa2a', Pid=100)
PKEY_Contact_HomeEmailAddresses = PROPERTYKEY(Fmtid='56c90e9d-9d46-4963-886f-2e1cd9a694ef', Pid=100)
PKEY_Contact_HomeFaxNumber = PROPERTYKEY(Fmtid='660e04d6-81ab-4977-a09f-82313113ab26', Pid=100)
PKEY_Contact_HomeTelephone = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=20)
PKEY_Contact_IMAddress = PROPERTYKEY(Fmtid='d68dbd8a-3374-4b81-9972-3ec30682db3d', Pid=100)
PKEY_Contact_Initials = PROPERTYKEY(Fmtid='f3d8f40d-50cb-44a2-9718-40cb9119495d', Pid=100)
PKEY_Contact_JA_CompanyNamePhonetic = PROPERTYKEY(Fmtid='897b3694-fe9e-43e6-8066-260f590c0100', Pid=2)
PKEY_Contact_JA_FirstNamePhonetic = PROPERTYKEY(Fmtid='897b3694-fe9e-43e6-8066-260f590c0100', Pid=3)
PKEY_Contact_JA_LastNamePhonetic = PROPERTYKEY(Fmtid='897b3694-fe9e-43e6-8066-260f590c0100', Pid=4)
PKEY_Contact_JobInfo1CompanyAddress = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=120)
PKEY_Contact_JobInfo1CompanyName = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=102)
PKEY_Contact_JobInfo1Department = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=106)
PKEY_Contact_JobInfo1Manager = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=105)
PKEY_Contact_JobInfo1OfficeLocation = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=104)
PKEY_Contact_JobInfo1Title = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=103)
PKEY_Contact_JobInfo1YomiCompanyName = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=101)
PKEY_Contact_JobInfo2CompanyAddress = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=121)
PKEY_Contact_JobInfo2CompanyName = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=108)
PKEY_Contact_JobInfo2Department = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=113)
PKEY_Contact_JobInfo2Manager = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=112)
PKEY_Contact_JobInfo2OfficeLocation = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=110)
PKEY_Contact_JobInfo2Title = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=109)
PKEY_Contact_JobInfo2YomiCompanyName = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=107)
PKEY_Contact_JobInfo3CompanyAddress = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=123)
PKEY_Contact_JobInfo3CompanyName = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=115)
PKEY_Contact_JobInfo3Department = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=119)
PKEY_Contact_JobInfo3Manager = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=118)
PKEY_Contact_JobInfo3OfficeLocation = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=117)
PKEY_Contact_JobInfo3Title = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=116)
PKEY_Contact_JobInfo3YomiCompanyName = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=114)
PKEY_Contact_JobTitle = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=6)
PKEY_Contact_Label = PROPERTYKEY(Fmtid='97b0ad89-df49-49cc-834e-660974fd755b', Pid=100)
PKEY_Contact_LastName = PROPERTYKEY(Fmtid='8f367200-c270-457c-b1d4-e07c5bcd90c7', Pid=100)
PKEY_Contact_MailingAddress = PROPERTYKEY(Fmtid='c0ac206a-827e-4650-95ae-77e2bb74fcc9', Pid=100)
PKEY_Contact_MiddleName = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=71)
PKEY_Contact_MobileTelephone = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=35)
PKEY_Contact_NickName = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=74)
PKEY_Contact_OfficeLocation = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=7)
PKEY_Contact_OtherAddress = PROPERTYKEY(Fmtid='508161fa-313b-43d5-83a1-c1accf68622c', Pid=100)
PKEY_Contact_OtherAddress1Country = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=134)
PKEY_Contact_OtherAddress1Locality = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=132)
PKEY_Contact_OtherAddress1PostalCode = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=135)
PKEY_Contact_OtherAddress1Region = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=133)
PKEY_Contact_OtherAddress1Street = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=131)
PKEY_Contact_OtherAddress2Country = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=139)
PKEY_Contact_OtherAddress2Locality = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=137)
PKEY_Contact_OtherAddress2PostalCode = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=140)
PKEY_Contact_OtherAddress2Region = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=138)
PKEY_Contact_OtherAddress2Street = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=136)
PKEY_Contact_OtherAddress3Country = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=144)
PKEY_Contact_OtherAddress3Locality = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=142)
PKEY_Contact_OtherAddress3PostalCode = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=145)
PKEY_Contact_OtherAddress3Region = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=143)
PKEY_Contact_OtherAddress3Street = PROPERTYKEY(Fmtid='a7b6f596-d678-4bc1-b05f-0203d27e8aa1', Pid=141)
PKEY_Contact_OtherAddressCity = PROPERTYKEY(Fmtid='6e682923-7f7b-4f0c-a337-cfca296687bf', Pid=100)
PKEY_Contact_OtherAddressCountry = PROPERTYKEY(Fmtid='8f167568-0aae-4322-8ed9-6055b7b0e398', Pid=100)
PKEY_Contact_OtherAddressPostalCode = PROPERTYKEY(Fmtid='95c656c1-2abf-4148-9ed3-9ec602e3b7cd', Pid=100)
PKEY_Contact_OtherAddressPostOfficeBox = PROPERTYKEY(Fmtid='8b26ea41-058f-43f6-aecc-4035681ce977', Pid=100)
PKEY_Contact_OtherAddressState = PROPERTYKEY(Fmtid='71b377d6-e570-425f-a170-809fae73e54e', Pid=100)
PKEY_Contact_OtherAddressStreet = PROPERTYKEY(Fmtid='ff962609-b7d6-4999-862d-95180d529aea', Pid=100)
PKEY_Contact_OtherEmailAddresses = PROPERTYKEY(Fmtid='11d6336b-38c4-4ec9-84d6-eb38d0b150af', Pid=100)
PKEY_Contact_PagerTelephone = PROPERTYKEY(Fmtid='d6304e01-f8f5-4f45-8b15-d024a6296789', Pid=100)
PKEY_Contact_PersonalTitle = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=69)
PKEY_Contact_PhoneNumbersCanonical = PROPERTYKEY(Fmtid='d042d2a1-927e-40b5-a503-6edbd42a517e', Pid=100)
PKEY_Contact_Prefix = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=75)
PKEY_Contact_PrimaryAddressCity = PROPERTYKEY(Fmtid='c8ea94f0-a9e3-4969-a94b-9c62a95324e0', Pid=100)
PKEY_Contact_PrimaryAddressCountry = PROPERTYKEY(Fmtid='e53d799d-0f3f-466e-b2ff-74634a3cb7a4', Pid=100)
PKEY_Contact_PrimaryAddressPostalCode = PROPERTYKEY(Fmtid='18bbd425-ecfd-46ef-b612-7b4a6034eda0', Pid=100)
PKEY_Contact_PrimaryAddressPostOfficeBox = PROPERTYKEY(Fmtid='de5ef3c7-46e1-484e-9999-62c5308394c1', Pid=100)
PKEY_Contact_PrimaryAddressState = PROPERTYKEY(Fmtid='f1176dfe-7138-4640-8b4c-ae375dc70a6d', Pid=100)
PKEY_Contact_PrimaryAddressStreet = PROPERTYKEY(Fmtid='63c25b20-96be-488f-8788-c09c407ad812', Pid=100)
PKEY_Contact_PrimaryEmailAddress = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=48)
PKEY_Contact_PrimaryTelephone = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=25)
PKEY_Contact_Profession = PROPERTYKEY(Fmtid='7268af55-1ce4-4f6e-a41f-b6e4ef10e4a9', Pid=100)
PKEY_Contact_SpouseName = PROPERTYKEY(Fmtid='9d2408b6-3167-422b-82b0-f583b7a7cfe3', Pid=100)
PKEY_Contact_Suffix = PROPERTYKEY(Fmtid='176dc63c-2688-4e89-8143-a347800f25e9', Pid=73)
PKEY_Contact_TelexNumber = PROPERTYKEY(Fmtid='c554493c-c1f7-40c1-a76c-ef8c0614003e', Pid=100)
PKEY_Contact_TTYTDDTelephone = PROPERTYKEY(Fmtid='aaf16bac-2b55-45e6-9f6d-415eb94910df', Pid=100)
PKEY_Contact_WebPage = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=18)
PKEY_Contact_Webpage2 = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=124)
PKEY_Contact_Webpage3 = PROPERTYKEY(Fmtid='00f63dd8-22bd-4a5d-ba34-5cb0b9bdcb03', Pid=125)
PKEY_AcquisitionID = PROPERTYKEY(Fmtid='65a98875-3c80-40ab-abbc-efdaf77dbee2', Pid=100)
PKEY_ApplicationDefinedProperties = PROPERTYKEY(Fmtid='cdbfc167-337e-41d8-af7c-8c09205429c7', Pid=100)
PKEY_ApplicationName = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=18)
PKEY_AppZoneIdentifier = PROPERTYKEY(Fmtid='502cfeab-47eb-459c-b960-e6d8728f7701', Pid=102)
PKEY_Author = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=4)
PKEY_CachedFileUpdaterContentIdForConflictResolution = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=114)
PKEY_CachedFileUpdaterContentIdForStream = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=113)
PKEY_Capacity = PROPERTYKEY(Fmtid='9b174b35-40ff-11d2-a27e-00c04fc30871', Pid=3)
PKEY_Category = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=2)
PKEY_Comment = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=6)
PKEY_Company = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=15)
PKEY_ComputerName = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=5)
PKEY_ContainedItems = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=29)
PKEY_ContentId = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=132)
PKEY_ContentStatus = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=27)
PKEY_ContentType = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=26)
PKEY_ContentUri = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=131)
PKEY_Copyright = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=11)
PKEY_CreatorAppId = PROPERTYKEY(Fmtid='c2ea046e-033c-4e91-bd5b-d4942f6bbe49', Pid=2)
PKEY_CreatorOpenWithUIOptions = PROPERTYKEY(Fmtid='c2ea046e-033c-4e91-bd5b-d4942f6bbe49', Pid=3)
CREATOROPENWITHUIOPTION_HIDDEN = 0
CREATOROPENWITHUIOPTION_VISIBLE = 1
PKEY_DataObjectFormat = PROPERTYKEY(Fmtid='1e81a3f8-a30f-4247-b9ee-1d0368a9425c', Pid=2)
PKEY_DateAccessed = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=16)
PKEY_DateAcquired = PROPERTYKEY(Fmtid='2cbaa8f5-d81f-47ca-b17a-f8d822300131', Pid=100)
PKEY_DateArchived = PROPERTYKEY(Fmtid='43f8d7b7-a444-4f87-9383-52271c9b915c', Pid=100)
PKEY_DateCompleted = PROPERTYKEY(Fmtid='72fab781-acda-43e5-b155-b2434f85e678', Pid=100)
PKEY_DateCreated = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=15)
PKEY_DateImported = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=18258)
PKEY_DateModified = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=14)
PKEY_DefaultSaveLocationDisplay = PROPERTYKEY(Fmtid='5d76b67f-9b3d-44bb-b6ae-25da4f638a67', Pid=10)
ISDEFAULTSAVE_NONE = 0
ISDEFAULTSAVE_OWNER = 1
ISDEFAULTSAVE_NONOWNER = 2
ISDEFAULTSAVE_BOTH = 3
PKEY_DueDate = PROPERTYKEY(Fmtid='3f8472b5-e0af-4db2-8071-c53fe76ae7ce', Pid=100)
PKEY_EndDate = PROPERTYKEY(Fmtid='c75faa05-96fd-49e7-9cb4-9f601082d553', Pid=100)
PKEY_ExpandoProperties = PROPERTYKEY(Fmtid='6fa20de6-d11c-4d9d-a154-64317628c12d', Pid=100)
PKEY_FileAllocationSize = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=18)
PKEY_FileAttributes = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=13)
PKEY_FileCount = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=12)
PKEY_FileDescription = PROPERTYKEY(Fmtid='0cef7d53-fa64-11d1-a203-0000f81fedee', Pid=3)
PKEY_FileExtension = PROPERTYKEY(Fmtid='e4f10a3c-49e6-405d-8288-a23bd4eeaa6c', Pid=100)
PKEY_FileFRN = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=21)
PKEY_FileName = PROPERTYKEY(Fmtid='41cf5ae0-f75a-4806-bd87-59c7d9248eb9', Pid=100)
PKEY_FileOfflineAvailabilityStatus = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=100)
FILEOFFLINEAVAILABILITYSTATUS_NOTAVAILABLEOFFLINE = 0
FILEOFFLINEAVAILABILITYSTATUS_PARTIAL = 1
FILEOFFLINEAVAILABILITYSTATUS_COMPLETE = 2
FILEOFFLINEAVAILABILITYSTATUS_COMPLETE_PINNED = 3
FILEOFFLINEAVAILABILITYSTATUS_EXCLUDED = 4
FILEOFFLINEAVAILABILITYSTATUS_FOLDER_EMPTY = 5
PKEY_FileOwner = PROPERTYKEY(Fmtid='9b174b34-40ff-11d2-a27e-00c04fc30871', Pid=4)
PKEY_FilePlaceholderStatus = PROPERTYKEY(Fmtid='b2f9b9d6-fec4-4dd5-94d7-8957488c807b', Pid=2)
PKEY_FileVersion = PROPERTYKEY(Fmtid='0cef7d53-fa64-11d1-a203-0000f81fedee', Pid=4)
PKEY_FindData = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=0)
PKEY_FlagColor = PROPERTYKEY(Fmtid='67df94de-0ca7-4d6f-b792-053a3e4f03cf', Pid=100)
PKEY_FlagColorText = PROPERTYKEY(Fmtid='45eae747-8e2a-40ae-8cbf-ca52aba6152a', Pid=100)
PKEY_FlagStatus = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=12)
FLAGSTATUS_NOTFLAGGED = 0
FLAGSTATUS_COMPLETED = 1
FLAGSTATUS_FOLLOWUP = 2
PKEY_FlagStatusText = PROPERTYKEY(Fmtid='dc54fd2e-189d-4871-aa01-08c2f57a4abc', Pid=100)
PKEY_FolderKind = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=101)
PKEY_FolderNameDisplay = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=25)
PKEY_FreeSpace = PROPERTYKEY(Fmtid='9b174b35-40ff-11d2-a27e-00c04fc30871', Pid=2)
PKEY_FullText = PROPERTYKEY(Fmtid='1e3ee840-bc2b-476c-8237-2acd1a839b22', Pid=6)
PKEY_HighKeywords = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=24)
PKEY_Identity = PROPERTYKEY(Fmtid='a26f4afc-7346-4299-be47-eb1ae613139f', Pid=100)
PKEY_Identity_Blob = PROPERTYKEY(Fmtid='8c3b93a4-baed-1a83-9a32-102ee313f6eb', Pid=100)
PKEY_Identity_DisplayName = PROPERTYKEY(Fmtid='7d683fc9-d155-45a8-bb1f-89d19bcb792f', Pid=100)
PKEY_Identity_InternetSid = PROPERTYKEY(Fmtid='6d6d5d49-265d-4688-9f4e-1fdd33e7cc83', Pid=100)
PKEY_Identity_IsMeIdentity = PROPERTYKEY(Fmtid='a4108708-09df-4377-9dfc-6d99986d5a67', Pid=100)
PKEY_Identity_KeyProviderContext = PROPERTYKEY(Fmtid='a26f4afc-7346-4299-be47-eb1ae613139f', Pid=17)
PKEY_Identity_KeyProviderName = PROPERTYKEY(Fmtid='a26f4afc-7346-4299-be47-eb1ae613139f', Pid=16)
PKEY_Identity_LogonStatusString = PROPERTYKEY(Fmtid='f18dedf3-337f-42c0-9e03-cee08708a8c3', Pid=100)
PKEY_Identity_PrimaryEmailAddress = PROPERTYKEY(Fmtid='fcc16823-baed-4f24-9b32-a0982117f7fa', Pid=100)
PKEY_Identity_PrimarySid = PROPERTYKEY(Fmtid='2b1b801e-c0c1-4987-9ec5-72fa89814787', Pid=100)
PKEY_Identity_ProviderData = PROPERTYKEY(Fmtid='a8a74b92-361b-4e9a-b722-7c4a7330a312', Pid=100)
PKEY_Identity_ProviderID = PROPERTYKEY(Fmtid='74a7de49-fa11-4d3d-a006-db7e08675916', Pid=100)
PKEY_Identity_QualifiedUserName = PROPERTYKEY(Fmtid='da520e51-f4e9-4739-ac82-02e0a95c9030', Pid=100)
PKEY_Identity_UniqueID = PROPERTYKEY(Fmtid='e55fc3b0-2b60-4220-918e-b21e8bf16016', Pid=100)
PKEY_Identity_UserName = PROPERTYKEY(Fmtid='c4322503-78ca-49c6-9acc-a68e2afd7b6b', Pid=100)
PKEY_IdentityProvider_Name = PROPERTYKEY(Fmtid='b96eff7b-35ca-4a35-8607-29e3a54c46ea', Pid=100)
PKEY_IdentityProvider_Picture = PROPERTYKEY(Fmtid='2425166f-5642-4864-992f-98fd98f294c3', Pid=100)
PKEY_ImageParsingName = PROPERTYKEY(Fmtid='d7750ee0-c6a4-48ec-b53e-b87b52e6d073', Pid=100)
PKEY_Importance = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=11)
IMPORTANCE_LOW_MIN = 0
IMPORTANCE_LOW_SET = 1
IMPORTANCE_LOW_MAX = 1
IMPORTANCE_NORMAL_MIN = 2
IMPORTANCE_NORMAL_SET = 3
IMPORTANCE_NORMAL_MAX = 4
IMPORTANCE_HIGH_MIN = 5
IMPORTANCE_HIGH_SET = 5
IMPORTANCE_HIGH_MAX = 5
PKEY_ImportanceText = PROPERTYKEY(Fmtid='a3b29791-7713-4e1d-bb40-17db85f01831', Pid=100)
PKEY_IsAttachment = PROPERTYKEY(Fmtid='f23f425c-71a1-4fa8-922f-678ea4a60408', Pid=100)
PKEY_IsDefaultNonOwnerSaveLocation = PROPERTYKEY(Fmtid='5d76b67f-9b3d-44bb-b6ae-25da4f638a67', Pid=5)
PKEY_IsDefaultSaveLocation = PROPERTYKEY(Fmtid='5d76b67f-9b3d-44bb-b6ae-25da4f638a67', Pid=3)
PKEY_IsDeleted = PROPERTYKEY(Fmtid='5cda5fc8-33ee-4ff3-9094-ae7bd8868c4d', Pid=100)
PKEY_IsEncrypted = PROPERTYKEY(Fmtid='90e5e14e-648b-4826-b2aa-acaf790e3513', Pid=10)
PKEY_IsFlagged = PROPERTYKEY(Fmtid='5da84765-e3ff-4278-86b0-a27967fbdd03', Pid=100)
PKEY_IsFlaggedComplete = PROPERTYKEY(Fmtid='a6f360d2-55f9-48de-b909-620e090a647c', Pid=100)
PKEY_IsIncomplete = PROPERTYKEY(Fmtid='346c8bd1-2e6a-4c45-89a4-61b78e8e700f', Pid=100)
PKEY_IsLocationSupported = PROPERTYKEY(Fmtid='5d76b67f-9b3d-44bb-b6ae-25da4f638a67', Pid=8)
PKEY_IsPinnedToNameSpaceTree = PROPERTYKEY(Fmtid='5d76b67f-9b3d-44bb-b6ae-25da4f638a67', Pid=2)
PKEY_IsRead = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=10)
PKEY_IsSearchOnlyItem = PROPERTYKEY(Fmtid='5d76b67f-9b3d-44bb-b6ae-25da4f638a67', Pid=4)
PKEY_IsSendToTarget = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=33)
PKEY_IsShared = PROPERTYKEY(Fmtid='ef884c5b-2bfe-41bb-aae5-76eedf4f9902', Pid=100)
PKEY_ItemAuthors = PROPERTYKEY(Fmtid='d0a04f0a-462a-48a4-bb2f-3706e88dbd7d', Pid=100)
PKEY_ItemClassType = PROPERTYKEY(Fmtid='048658ad-2db8-41a4-bbb6-ac1ef1207eb1', Pid=100)
PKEY_ItemDate = PROPERTYKEY(Fmtid='f7db74b4-4287-4103-afba-f1b13dcd75cf', Pid=100)
PKEY_ItemFolderNameDisplay = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=2)
PKEY_ItemFolderPathDisplay = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=6)
PKEY_ItemFolderPathDisplayNarrow = PROPERTYKEY(Fmtid='dabd30ed-0043-4789-a7f8-d013a4736622', Pid=100)
PKEY_ItemName = PROPERTYKEY(Fmtid='6b8da074-3b5c-43bc-886f-0a2cdce00b6f', Pid=100)
PKEY_ItemNameDisplay = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=10)
PKEY_ItemNameDisplayWithoutExtension = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=24)
PKEY_ItemNamePrefix = PROPERTYKEY(Fmtid='d7313ff1-a77a-401c-8c99-3dbdd68add36', Pid=100)
PKEY_ItemNameSortOverride = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=23)
PKEY_ItemParticipants = PROPERTYKEY(Fmtid='d4d0aa16-9948-41a4-aa85-d97ff9646993', Pid=100)
PKEY_ItemPathDisplay = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=7)
PKEY_ItemPathDisplayNarrow = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=8)
PKEY_ItemSubType = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=37)
PKEY_ItemType = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=11)
PKEY_ItemTypeText = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=4)
PKEY_ItemUrl = PROPERTYKEY(Fmtid='49691c90-7e17-101a-a91c-08002b2ecda9', Pid=9)
PKEY_Keywords = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=5)
PKEY_Kind = PROPERTYKEY(Fmtid='1e3ee840-bc2b-476c-8237-2acd1a839b22', Pid=3)
PKEY_KindText = PROPERTYKEY(Fmtid='f04bef95-c585-4197-a2b7-df46fdc9ee6d', Pid=100)
PKEY_Language = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=28)
PKEY_LastSyncError = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=107)
PKEY_LastSyncWarning = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=128)
PKEY_LastWriterPackageFamilyName = PROPERTYKEY(Fmtid='502cfeab-47eb-459c-b960-e6d8728f7701', Pid=101)
PKEY_LowKeywords = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=25)
PKEY_MediumKeywords = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=26)
PKEY_MileageInformation = PROPERTYKEY(Fmtid='fdf84370-031a-4add-9e91-0d775f1c6605', Pid=100)
PKEY_MIMEType = PROPERTYKEY(Fmtid='0b63e350-9ccc-11d0-bcdb-00805fccce04', Pid=5)
PKEY_Null = PROPERTYKEY(Fmtid='00000000-0000-0000-0000-000000000000', Pid=0)
PKEY_OfflineAvailability = PROPERTYKEY(Fmtid='a94688b6-7d9f-4570-a648-e3dfc0ab2b3f', Pid=100)
OFFLINEAVAILABILITY_NOT_AVAILABLE = 0
OFFLINEAVAILABILITY_AVAILABLE = 1
OFFLINEAVAILABILITY_ALWAYS_AVAILABLE = 2
PKEY_OfflineStatus = PROPERTYKEY(Fmtid='6d24888f-4718-4bda-afed-ea0fb4386cd8', Pid=100)
OFFLINESTATUS_ONLINE = 0
OFFLINESTATUS_OFFLINE = 1
OFFLINESTATUS_OFFLINE_FORCED = 2
OFFLINESTATUS_OFFLINE_SLOW = 3
OFFLINESTATUS_OFFLINE_ERROR = 4
OFFLINESTATUS_OFFLINE_ITEM_VERSION_CONFLICT = 5
OFFLINESTATUS_OFFLINE_SUSPENDED = 6
PKEY_OriginalFileName = PROPERTYKEY(Fmtid='0cef7d53-fa64-11d1-a203-0000f81fedee', Pid=6)
PKEY_OwnerSID = PROPERTYKEY(Fmtid='5d76b67f-9b3d-44bb-b6ae-25da4f638a67', Pid=6)
PKEY_ParentalRating = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=21)
PKEY_ParentalRatingReason = PROPERTYKEY(Fmtid='10984e0a-f9f2-4321-b7ef-baf195af4319', Pid=100)
PKEY_ParentalRatingsOrganization = PROPERTYKEY(Fmtid='a7fe0840-1344-46f0-8d37-52ed712a4bf9', Pid=100)
PKEY_ParsingBindContext = PROPERTYKEY(Fmtid='dfb9a04d-362f-4ca3-b30b-0254b17b5b84', Pid=100)
PKEY_ParsingName = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=24)
PKEY_ParsingPath = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=30)
PKEY_PerceivedType = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=9)
PKEY_PercentFull = PROPERTYKEY(Fmtid='9b174b35-40ff-11d2-a27e-00c04fc30871', Pid=5)
PKEY_Priority = PROPERTYKEY(Fmtid='9c1fcf74-2d97-41ba-b4ae-cb2e3661a6e4', Pid=5)
PKEY_PriorityText = PROPERTYKEY(Fmtid='d98be98b-b86b-4095-bf52-9d23b2e0a752', Pid=100)
PKEY_Project = PROPERTYKEY(Fmtid='39a7f922-477c-48de-8bc8-b28441e342e3', Pid=100)
PKEY_ProviderItemID = PROPERTYKEY(Fmtid='f21d9941-81f0-471a-adee-4e74b49217ed', Pid=100)
PKEY_Rating = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=9)
RATING_ONE_STAR_MIN = 1
RATING_ONE_STAR_SET = 1
RATING_ONE_STAR_MAX = 12
RATING_TWO_STARS_MIN = 13
RATING_TWO_STARS_SET = 25
RATING_TWO_STARS_MAX = 37
RATING_THREE_STARS_MIN = 38
RATING_THREE_STARS_SET = 50
RATING_THREE_STARS_MAX = 62
RATING_FOUR_STARS_MIN = 63
RATING_FOUR_STARS_SET = 75
RATING_FOUR_STARS_MAX = 87
RATING_FIVE_STARS_MIN = 88
RATING_FIVE_STARS_SET = 99
RATING_FIVE_STARS_MAX = 99
PKEY_RatingText = PROPERTYKEY(Fmtid='90197ca7-fd8f-4e8c-9da3-b57e1e609295', Pid=100)
PKEY_RemoteConflictingFile = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=115)
PKEY_Security_AllowedEnterpriseDataProtectionIdentities = PROPERTYKEY(Fmtid='38d43380-d418-4830-84d5-46935a81c5c6', Pid=32)
PKEY_Security_EncryptionOwners = PROPERTYKEY(Fmtid='5f5aff6a-37e5-4780-97ea-80c7565cf535', Pid=34)
PKEY_Security_EncryptionOwnersDisplay = PROPERTYKEY(Fmtid='de621b8f-e125-43a3-a32d-5665446d632a', Pid=25)
PKEY_Sensitivity = PROPERTYKEY(Fmtid='f8d3f6ac-4874-42cb-be59-ab454b30716a', Pid=100)
PKEY_SensitivityText = PROPERTYKEY(Fmtid='d0c7f054-3f72-4725-8527-129a577cb269', Pid=100)
PKEY_SFGAOFlags = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=25)
PKEY_SharedWith = PROPERTYKEY(Fmtid='ef884c5b-2bfe-41bb-aae5-76eedf4f9902', Pid=200)
PKEY_ShareUserRating = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=12)
PKEY_SharingStatus = PROPERTYKEY(Fmtid='ef884c5b-2bfe-41bb-aae5-76eedf4f9902', Pid=300)
SHARINGSTATUS_NOTSHARED = 0
SHARINGSTATUS_SHARED = 1
SHARINGSTATUS_PRIVATE = 2
PKEY_Shell_OmitFromView = PROPERTYKEY(Fmtid='de35258c-c695-4cbc-b982-38b0ad24ced0', Pid=2)
PKEY_SimpleRating = PROPERTYKEY(Fmtid='a09f084e-ad41-489f-8076-aa5be3082bca', Pid=100)
PKEY_Size = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=12)
PKEY_SoftwareUsed = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=305)
PKEY_SourceItem = PROPERTYKEY(Fmtid='668cdfa5-7a1b-4323-ae4b-e527393a1d81', Pid=100)
PKEY_SourcePackageFamilyName = PROPERTYKEY(Fmtid='ffae9db7-1c8d-43ff-818c-84403aa3732d', Pid=100)
PKEY_StartDate = PROPERTYKEY(Fmtid='48fd6ec8-8a12-4cdf-a03e-4ec5a511edde', Pid=100)
PKEY_Status = PROPERTYKEY(Fmtid='000214a1-0000-0000-c000-000000000046', Pid=9)
PKEY_StorageProviderCallerVersionInformation = PROPERTYKEY(Fmtid='b2f9b9d6-fec4-4dd5-94d7-8957488c807b', Pid=7)
PKEY_StorageProviderError = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=109)
PKEY_StorageProviderFileChecksum = PROPERTYKEY(Fmtid='b2f9b9d6-fec4-4dd5-94d7-8957488c807b', Pid=5)
PKEY_StorageProviderFileFlags = PROPERTYKEY(Fmtid='b2f9b9d6-fec4-4dd5-94d7-8957488c807b', Pid=8)
PKEY_StorageProviderFileHasConflict = PROPERTYKEY(Fmtid='b2f9b9d6-fec4-4dd5-94d7-8957488c807b', Pid=9)
PKEY_StorageProviderFileIdentifier = PROPERTYKEY(Fmtid='b2f9b9d6-fec4-4dd5-94d7-8957488c807b', Pid=3)
PKEY_StorageProviderFileRemoteUri = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=112)
PKEY_StorageProviderFileVersion = PROPERTYKEY(Fmtid='b2f9b9d6-fec4-4dd5-94d7-8957488c807b', Pid=4)
PKEY_StorageProviderFileVersionWaterline = PROPERTYKEY(Fmtid='b2f9b9d6-fec4-4dd5-94d7-8957488c807b', Pid=6)
PKEY_StorageProviderId = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=108)
PKEY_StorageProviderShareStatuses = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=111)
PKEY_StorageProviderSharingStatus = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=117)
STORAGE_PROVIDER_SHARINGSTATUS_NOTSHARED = 0
STORAGE_PROVIDER_SHARINGSTATUS_SHARED = 1
STORAGE_PROVIDER_SHARINGSTATUS_PRIVATE = 2
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC = 3
STORAGE_PROVIDER_SHARINGSTATUS_SHARED_OWNED = 4
STORAGE_PROVIDER_SHARINGSTATUS_SHARED_COOWNED = 5
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_OWNED = 6
STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_COOWNED = 7
PKEY_StorageProviderStatus = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=110)
PKEY_Subject = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=3)
PKEY_SyncTransferStatus = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=103)
PKEY_Thumbnail = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=17)
PKEY_ThumbnailCacheId = PROPERTYKEY(Fmtid='446d16b1-8dad-4870-a748-402ea43d788c', Pid=100)
PKEY_ThumbnailStream = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=27)
PKEY_Title = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=2)
PKEY_TitleSortOverride = PROPERTYKEY(Fmtid='f0f7984d-222e-4ad2-82ab-1dd8ea40e57e', Pid=300)
PKEY_TotalFileSize = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=14)
PKEY_Trademarks = PROPERTYKEY(Fmtid='0cef7d53-fa64-11d1-a203-0000f81fedee', Pid=9)
PKEY_TransferOrder = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=106)
PKEY_TransferPosition = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=104)
PKEY_TransferSize = PROPERTYKEY(Fmtid='fceff153-e839-4cf3-a9e7-ea22832094b8', Pid=105)
PKEY_VolumeId = PROPERTYKEY(Fmtid='446d16b1-8dad-4870-a748-402ea43d788c', Pid=104)
PKEY_ZoneIdentifier = PROPERTYKEY(Fmtid='502cfeab-47eb-459c-b960-e6d8728f7701', Pid=100)
PKEY_Device_PrinterURL = PROPERTYKEY(Fmtid='0b48f35a-be6e-4f17-b108-3c4073d1669a', Pid=15)
PKEY_DeviceInterface_Bluetooth_DeviceAddress = PROPERTYKEY(Fmtid='2bd67d8b-8beb-48d5-87e0-6cda3428040a', Pid=1)
PKEY_DeviceInterface_Bluetooth_Flags = PROPERTYKEY(Fmtid='2bd67d8b-8beb-48d5-87e0-6cda3428040a', Pid=3)
PKEY_DeviceInterface_Bluetooth_LastConnectedTime = PROPERTYKEY(Fmtid='2bd67d8b-8beb-48d5-87e0-6cda3428040a', Pid=11)
PKEY_DeviceInterface_Bluetooth_Manufacturer = PROPERTYKEY(Fmtid='2bd67d8b-8beb-48d5-87e0-6cda3428040a', Pid=4)
PKEY_DeviceInterface_Bluetooth_ModelNumber = PROPERTYKEY(Fmtid='2bd67d8b-8beb-48d5-87e0-6cda3428040a', Pid=5)
PKEY_DeviceInterface_Bluetooth_ProductId = PROPERTYKEY(Fmtid='2bd67d8b-8beb-48d5-87e0-6cda3428040a', Pid=8)
PKEY_DeviceInterface_Bluetooth_ProductVersion = PROPERTYKEY(Fmtid='2bd67d8b-8beb-48d5-87e0-6cda3428040a', Pid=9)
PKEY_DeviceInterface_Bluetooth_ServiceGuid = PROPERTYKEY(Fmtid='2bd67d8b-8beb-48d5-87e0-6cda3428040a', Pid=2)
PKEY_DeviceInterface_Bluetooth_VendorId = PROPERTYKEY(Fmtid='2bd67d8b-8beb-48d5-87e0-6cda3428040a', Pid=7)
PKEY_DeviceInterface_Bluetooth_VendorIdSource = PROPERTYKEY(Fmtid='2bd67d8b-8beb-48d5-87e0-6cda3428040a', Pid=6)
PKEY_DeviceInterface_Hid_IsReadOnly = PROPERTYKEY(Fmtid='cbf38310-4a17-4310-a1eb-247f0b67593b', Pid=4)
PKEY_DeviceInterface_Hid_ProductId = PROPERTYKEY(Fmtid='cbf38310-4a17-4310-a1eb-247f0b67593b', Pid=6)
PKEY_DeviceInterface_Hid_UsageId = PROPERTYKEY(Fmtid='cbf38310-4a17-4310-a1eb-247f0b67593b', Pid=3)
PKEY_DeviceInterface_Hid_UsagePage = PROPERTYKEY(Fmtid='cbf38310-4a17-4310-a1eb-247f0b67593b', Pid=2)
PKEY_DeviceInterface_Hid_VendorId = PROPERTYKEY(Fmtid='cbf38310-4a17-4310-a1eb-247f0b67593b', Pid=5)
PKEY_DeviceInterface_Hid_VersionNumber = PROPERTYKEY(Fmtid='cbf38310-4a17-4310-a1eb-247f0b67593b', Pid=7)
PKEY_DeviceInterface_PrinterDriverDirectory = PROPERTYKEY(Fmtid='847c66de-b8d6-4af9-abc3-6f4f926bc039', Pid=14)
PKEY_DeviceInterface_PrinterDriverName = PROPERTYKEY(Fmtid='afc47170-14f5-498c-8f30-b0d19be449c6', Pid=11)
PKEY_DeviceInterface_PrinterEnumerationFlag = PROPERTYKEY(Fmtid='a00742a1-cd8c-4b37-95ab-70755587767a', Pid=3)
PKEY_DeviceInterface_PrinterName = PROPERTYKEY(Fmtid='0a7b84ef-0c27-463f-84ef-06c5070001be', Pid=10)
PKEY_DeviceInterface_PrinterPortName = PROPERTYKEY(Fmtid='eec7b761-6f94-41b1-949f-c729720dd13c', Pid=12)
PKEY_DeviceInterface_Proximity_SupportsNfc = PROPERTYKEY(Fmtid='fb3842cd-9e2a-4f83-8fcc-4b0761139ae9', Pid=2)
PKEY_DeviceInterface_Serial_PortName = PROPERTYKEY(Fmtid='4c6bf15c-4c03-4aac-91f5-64c0f852bcf4', Pid=4)
PKEY_DeviceInterface_Serial_UsbProductId = PROPERTYKEY(Fmtid='4c6bf15c-4c03-4aac-91f5-64c0f852bcf4', Pid=3)
PKEY_DeviceInterface_Serial_UsbVendorId = PROPERTYKEY(Fmtid='4c6bf15c-4c03-4aac-91f5-64c0f852bcf4', Pid=2)
PKEY_DeviceInterface_WinUsb_DeviceInterfaceClasses = PROPERTYKEY(Fmtid='95e127b5-79cc-4e83-9c9e-8422187b3e0e', Pid=7)
PKEY_DeviceInterface_WinUsb_UsbClass = PROPERTYKEY(Fmtid='95e127b5-79cc-4e83-9c9e-8422187b3e0e', Pid=4)
PKEY_DeviceInterface_WinUsb_UsbProductId = PROPERTYKEY(Fmtid='95e127b5-79cc-4e83-9c9e-8422187b3e0e', Pid=3)
PKEY_DeviceInterface_WinUsb_UsbProtocol = PROPERTYKEY(Fmtid='95e127b5-79cc-4e83-9c9e-8422187b3e0e', Pid=6)
PKEY_DeviceInterface_WinUsb_UsbSubClass = PROPERTYKEY(Fmtid='95e127b5-79cc-4e83-9c9e-8422187b3e0e', Pid=5)
PKEY_DeviceInterface_WinUsb_UsbVendorId = PROPERTYKEY(Fmtid='95e127b5-79cc-4e83-9c9e-8422187b3e0e', Pid=2)
PKEY_Devices_Aep_AepId = PROPERTYKEY(Fmtid='3b2ce006-5e61-4fde-bab8-9b8aac9b26df', Pid=8)
PKEY_Devices_Aep_Bluetooth_Cod_Major = PROPERTYKEY(Fmtid='5fbd34cd-561a-412e-ba98-478a6b0fef1d', Pid=2)
PKEY_Devices_Aep_Bluetooth_Cod_Minor = PROPERTYKEY(Fmtid='5fbd34cd-561a-412e-ba98-478a6b0fef1d', Pid=3)
PKEY_Devices_Aep_Bluetooth_Cod_Services_Audio = PROPERTYKEY(Fmtid='5fbd34cd-561a-412e-ba98-478a6b0fef1d', Pid=10)
PKEY_Devices_Aep_Bluetooth_Cod_Services_Capturing = PROPERTYKEY(Fmtid='5fbd34cd-561a-412e-ba98-478a6b0fef1d', Pid=8)
PKEY_Devices_Aep_Bluetooth_Cod_Services_Information = PROPERTYKEY(Fmtid='5fbd34cd-561a-412e-ba98-478a6b0fef1d', Pid=12)
PKEY_Devices_Aep_Bluetooth_Cod_Services_LimitedDiscovery = PROPERTYKEY(Fmtid='5fbd34cd-561a-412e-ba98-478a6b0fef1d', Pid=4)
PKEY_Devices_Aep_Bluetooth_Cod_Services_Networking = PROPERTYKEY(Fmtid='5fbd34cd-561a-412e-ba98-478a6b0fef1d', Pid=6)
PKEY_Devices_Aep_Bluetooth_Cod_Services_ObjectXfer = PROPERTYKEY(Fmtid='5fbd34cd-561a-412e-ba98-478a6b0fef1d', Pid=9)
PKEY_Devices_Aep_Bluetooth_Cod_Services_Positioning = PROPERTYKEY(Fmtid='5fbd34cd-561a-412e-ba98-478a6b0fef1d', Pid=5)
PKEY_Devices_Aep_Bluetooth_Cod_Services_Rendering = PROPERTYKEY(Fmtid='5fbd34cd-561a-412e-ba98-478a6b0fef1d', Pid=7)
PKEY_Devices_Aep_Bluetooth_Cod_Services_Telephony = PROPERTYKEY(Fmtid='5fbd34cd-561a-412e-ba98-478a6b0fef1d', Pid=11)
PKEY_Devices_Aep_Bluetooth_LastSeenTime = PROPERTYKEY(Fmtid='2bd67d8b-8beb-48d5-87e0-6cda3428040a', Pid=12)
PKEY_Devices_Aep_Bluetooth_Le_AddressType = PROPERTYKEY(Fmtid='995ef0b0-7eb3-4a8b-b9ce-068bb3f4af69', Pid=4)
BLUETOOTH_ADDRESS_TYPE_PUBLIC = 0
BLUETOOTH_ADDRESS_TYPE_RANDOM = 1
PKEY_Devices_Aep_Bluetooth_Le_Appearance = PROPERTYKEY(Fmtid='995ef0b0-7eb3-4a8b-b9ce-068bb3f4af69', Pid=1)
PKEY_Devices_Aep_Bluetooth_Le_Appearance_Category = PROPERTYKEY(Fmtid='995ef0b0-7eb3-4a8b-b9ce-068bb3f4af69', Pid=5)
PKEY_Devices_Aep_Bluetooth_Le_Appearance_Subcategory = PROPERTYKEY(Fmtid='995ef0b0-7eb3-4a8b-b9ce-068bb3f4af69', Pid=6)
PKEY_Devices_Aep_Bluetooth_Le_IsConnectable = PROPERTYKEY(Fmtid='995ef0b0-7eb3-4a8b-b9ce-068bb3f4af69', Pid=8)
PKEY_Devices_Aep_CanPair = PROPERTYKEY(Fmtid='e7c3fb29-caa7-4f47-8c8b-be59b330d4c5', Pid=3)
PKEY_Devices_Aep_Category = PROPERTYKEY(Fmtid='a35996ab-11cf-4935-8b61-a6761081ecdf', Pid=17)
PKEY_Devices_Aep_ContainerId = PROPERTYKEY(Fmtid='e7c3fb29-caa7-4f47-8c8b-be59b330d4c5', Pid=2)
PKEY_Devices_Aep_DeviceAddress = PROPERTYKEY(Fmtid='a35996ab-11cf-4935-8b61-a6761081ecdf', Pid=12)
PKEY_Devices_Aep_IsConnected = PROPERTYKEY(Fmtid='a35996ab-11cf-4935-8b61-a6761081ecdf', Pid=7)
PKEY_Devices_Aep_IsPaired = PROPERTYKEY(Fmtid='a35996ab-11cf-4935-8b61-a6761081ecdf', Pid=16)
PKEY_Devices_Aep_IsPresent = PROPERTYKEY(Fmtid='a35996ab-11cf-4935-8b61-a6761081ecdf', Pid=9)
PKEY_Devices_Aep_Manufacturer = PROPERTYKEY(Fmtid='a35996ab-11cf-4935-8b61-a6761081ecdf', Pid=5)
PKEY_Devices_Aep_ModelId = PROPERTYKEY(Fmtid='a35996ab-11cf-4935-8b61-a6761081ecdf', Pid=4)
PKEY_Devices_Aep_ModelName = PROPERTYKEY(Fmtid='a35996ab-11cf-4935-8b61-a6761081ecdf', Pid=3)
PKEY_Devices_Aep_PointOfService_ConnectionTypes = PROPERTYKEY(Fmtid='d4bf61b3-442e-4ada-882d-fa7b70c832d9', Pid=6)
PKEY_Devices_Aep_ProtocolId = PROPERTYKEY(Fmtid='3b2ce006-5e61-4fde-bab8-9b8aac9b26df', Pid=5)
PKEY_Devices_Aep_SignalStrength = PROPERTYKEY(Fmtid='a35996ab-11cf-4935-8b61-a6761081ecdf', Pid=6)
PKEY_Devices_AepContainer_CanPair = PROPERTYKEY(Fmtid='0bba1ede-7566-4f47-90ec-25fc567ced2a', Pid=3)
PKEY_Devices_AepContainer_Categories = PROPERTYKEY(Fmtid='0bba1ede-7566-4f47-90ec-25fc567ced2a', Pid=9)
PKEY_Devices_AepContainer_Children = PROPERTYKEY(Fmtid='0bba1ede-7566-4f47-90ec-25fc567ced2a', Pid=2)
PKEY_Devices_AepContainer_ContainerId = PROPERTYKEY(Fmtid='0bba1ede-7566-4f47-90ec-25fc567ced2a', Pid=12)
PKEY_Devices_AepContainer_DialProtocol_InstalledApplications = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=6)
PKEY_Devices_AepContainer_IsPaired = PROPERTYKEY(Fmtid='0bba1ede-7566-4f47-90ec-25fc567ced2a', Pid=4)
PKEY_Devices_AepContainer_IsPresent = PROPERTYKEY(Fmtid='0bba1ede-7566-4f47-90ec-25fc567ced2a', Pid=11)
PKEY_Devices_AepContainer_Manufacturer = PROPERTYKEY(Fmtid='0bba1ede-7566-4f47-90ec-25fc567ced2a', Pid=6)
PKEY_Devices_AepContainer_ModelIds = PROPERTYKEY(Fmtid='0bba1ede-7566-4f47-90ec-25fc567ced2a', Pid=8)
PKEY_Devices_AepContainer_ModelName = PROPERTYKEY(Fmtid='0bba1ede-7566-4f47-90ec-25fc567ced2a', Pid=7)
PKEY_Devices_AepContainer_ProtocolIds = PROPERTYKEY(Fmtid='0bba1ede-7566-4f47-90ec-25fc567ced2a', Pid=13)
PKEY_Devices_AepContainer_SupportedUriSchemes = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=5)
PKEY_Devices_AepContainer_SupportsAudio = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=2)
PKEY_Devices_AepContainer_SupportsCapturing = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=11)
PKEY_Devices_AepContainer_SupportsImages = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=4)
PKEY_Devices_AepContainer_SupportsInformation = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=14)
PKEY_Devices_AepContainer_SupportsLimitedDiscovery = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=7)
PKEY_Devices_AepContainer_SupportsNetworking = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=9)
PKEY_Devices_AepContainer_SupportsObjectTransfer = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=12)
PKEY_Devices_AepContainer_SupportsPositioning = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=8)
PKEY_Devices_AepContainer_SupportsRendering = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=10)
PKEY_Devices_AepContainer_SupportsTelephony = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=13)
PKEY_Devices_AepContainer_SupportsVideo = PROPERTYKEY(Fmtid='6af55d45-38db-4495-acb0-d4728a3b8314', Pid=3)
PKEY_Devices_AepService_AepId = PROPERTYKEY(Fmtid='c9c141a9-1b4c-4f17-a9d1-f298538cadb8', Pid=6)
PKEY_Devices_AepService_Bluetooth_CacheMode = PROPERTYKEY(Fmtid='9744311e-7951-4b2e-b6f0-ecb293cac119', Pid=5)
BLUETOOTH_CACHE_MODE_CACHED = 0
BLUETOOTH_CACHED_MODE_UNCACHED = 1
PKEY_Devices_AepService_Bluetooth_ServiceGuid = PROPERTYKEY(Fmtid='a399aac7-c265-474e-b073-ffce57721716', Pid=2)
PKEY_Devices_AepService_Bluetooth_TargetDevice = PROPERTYKEY(Fmtid='9744311e-7951-4b2e-b6f0-ecb293cac119', Pid=6)
PKEY_Devices_AepService_ContainerId = PROPERTYKEY(Fmtid='71724756-3e74-4432-9b59-e7b2f668a593', Pid=4)
PKEY_Devices_AepService_FriendlyName = PROPERTYKEY(Fmtid='71724756-3e74-4432-9b59-e7b2f668a593', Pid=2)
PKEY_Devices_AepService_IoT_ServiceInterfaces = PROPERTYKEY(Fmtid='79d94e82-4d79-45aa-821a-74858b4e4ca6', Pid=2)
PKEY_Devices_AepService_ParentAepIsPaired = PROPERTYKEY(Fmtid='c9c141a9-1b4c-4f17-a9d1-f298538cadb8', Pid=7)
PKEY_Devices_AepService_ProtocolId = PROPERTYKEY(Fmtid='c9c141a9-1b4c-4f17-a9d1-f298538cadb8', Pid=5)
PKEY_Devices_AepService_ServiceClassId = PROPERTYKEY(Fmtid='71724756-3e74-4432-9b59-e7b2f668a593', Pid=3)
PKEY_Devices_AepService_ServiceId = PROPERTYKEY(Fmtid='c9c141a9-1b4c-4f17-a9d1-f298538cadb8', Pid=2)
PKEY_Devices_AppPackageFamilyName = PROPERTYKEY(Fmtid='51236583-0c4a-4fe8-b81f-166aec13f510', Pid=100)
PKEY_Devices_AudioDevice_Microphone_IsFarField = PROPERTYKEY(Fmtid='8943b373-388c-4395-b557-bc6dbaffafdb', Pid=6)
PKEY_Devices_AudioDevice_Microphone_SensitivityInDbfs = PROPERTYKEY(Fmtid='8943b373-388c-4395-b557-bc6dbaffafdb', Pid=3)
PKEY_Devices_AudioDevice_Microphone_SensitivityInDbfs2 = PROPERTYKEY(Fmtid='8943b373-388c-4395-b557-bc6dbaffafdb', Pid=5)
PKEY_Devices_AudioDevice_Microphone_SignalToNoiseRatioInDb = PROPERTYKEY(Fmtid='8943b373-388c-4395-b557-bc6dbaffafdb', Pid=4)
PKEY_Devices_AudioDevice_RawProcessingSupported = PROPERTYKEY(Fmtid='8943b373-388c-4395-b557-bc6dbaffafdb', Pid=2)
PKEY_Devices_AudioDevice_SpeechProcessingSupported = PROPERTYKEY(Fmtid='fb1de864-e06d-47f4-82a6-8a0aef44493c', Pid=2)
PKEY_Devices_BatteryLife = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=10)
PKEY_Devices_BatteryPlusCharging = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=22)
PKEY_Devices_BatteryPlusChargingText = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=23)
PKEY_Devices_Category = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=91)
PKEY_Devices_CategoryGroup = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=94)
PKEY_Devices_CategoryIds = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=90)
PKEY_Devices_CategoryPlural = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=92)
PKEY_Devices_ChallengeAep = PROPERTYKEY(Fmtid='0774315e-b714-48ec-8de8-8125c077ac11', Pid=2)
PKEY_Devices_ChargingState = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=11)
PKEY_Devices_Children = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=9)
PKEY_Devices_ClassGuid = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=10)
PKEY_Devices_CompatibleIds = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=4)
PKEY_Devices_Connected = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=55)
PKEY_Devices_ContainerId = PROPERTYKEY(Fmtid='8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c', Pid=2)
PKEY_Devices_DefaultTooltip = PROPERTYKEY(Fmtid='880f70a2-6082-47ac-8aab-a739d1a300c3', Pid=153)
PKEY_Devices_DeviceCapabilities = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=17)
PKEY_Devices_DeviceCharacteristics = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=29)
PKEY_Devices_DeviceDescription1 = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=81)
PKEY_Devices_DeviceDescription2 = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=82)
PKEY_Devices_DeviceHasProblem = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=6)
PKEY_Devices_DeviceInstanceId = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=256)
PKEY_Devices_DeviceManufacturer = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=13)
PKEY_Devices_DevObjectType = PROPERTYKEY(Fmtid='13673f42-a3d6-49f6-b4da-ae46e0c5237c', Pid=2)
PKEY_Devices_DialProtocol_InstalledApplications = PROPERTYKEY(Fmtid='6845cc72-1b71-48c3-af86-b09171a19b14', Pid=3)
PKEY_Devices_DiscoveryMethod = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=52)
PKEY_Devices_Dnssd_Domain = PROPERTYKEY(Fmtid='bf79c0ab-bb74-4cee-b070-470b5ae202ea', Pid=3)
PKEY_Devices_Dnssd_FullName = PROPERTYKEY(Fmtid='bf79c0ab-bb74-4cee-b070-470b5ae202ea', Pid=5)
PKEY_Devices_Dnssd_HostName = PROPERTYKEY(Fmtid='bf79c0ab-bb74-4cee-b070-470b5ae202ea', Pid=7)
PKEY_Devices_Dnssd_InstanceName = PROPERTYKEY(Fmtid='bf79c0ab-bb74-4cee-b070-470b5ae202ea', Pid=4)
PKEY_Devices_Dnssd_NetworkAdapterId = PROPERTYKEY(Fmtid='bf79c0ab-bb74-4cee-b070-470b5ae202ea', Pid=11)
PKEY_Devices_Dnssd_PortNumber = PROPERTYKEY(Fmtid='bf79c0ab-bb74-4cee-b070-470b5ae202ea', Pid=12)
PKEY_Devices_Dnssd_Priority = PROPERTYKEY(Fmtid='bf79c0ab-bb74-4cee-b070-470b5ae202ea', Pid=9)
PKEY_Devices_Dnssd_ServiceName = PROPERTYKEY(Fmtid='bf79c0ab-bb74-4cee-b070-470b5ae202ea', Pid=2)
PKEY_Devices_Dnssd_TextAttributes = PROPERTYKEY(Fmtid='bf79c0ab-bb74-4cee-b070-470b5ae202ea', Pid=6)
PKEY_Devices_Dnssd_Ttl = PROPERTYKEY(Fmtid='bf79c0ab-bb74-4cee-b070-470b5ae202ea', Pid=10)
PKEY_Devices_Dnssd_Weight = PROPERTYKEY(Fmtid='bf79c0ab-bb74-4cee-b070-470b5ae202ea', Pid=8)
PKEY_Devices_FriendlyName = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12288)
PKEY_Devices_FunctionPaths = PROPERTYKEY(Fmtid='d08dd4c0-3a9e-462e-8290-7b636b2576b9', Pid=3)
PKEY_Devices_GlyphIcon = PROPERTYKEY(Fmtid='51236583-0c4a-4fe8-b81f-166aec13f510', Pid=123)
PKEY_Devices_HardwareIds = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=3)
PKEY_Devices_Icon = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=57)
PKEY_Devices_InLocalMachineContainer = PROPERTYKEY(Fmtid='8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c', Pid=4)
PKEY_Devices_InterfaceClassGuid = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=4)
PKEY_Devices_InterfaceEnabled = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=3)
PKEY_Devices_InterfacePaths = PROPERTYKEY(Fmtid='d08dd4c0-3a9e-462e-8290-7b636b2576b9', Pid=2)
PKEY_Devices_IpAddress = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12297)
PKEY_Devices_IsDefault = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=86)
PKEY_Devices_IsNetworkConnected = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=85)
PKEY_Devices_IsShared = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=84)
PKEY_Devices_IsSoftwareInstalling = PROPERTYKEY(Fmtid='83da6326-97a6-4088-9453-a1923f573b29', Pid=9)
PKEY_Devices_LaunchDeviceStageFromExplorer = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=77)
PKEY_Devices_LocalMachine = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=70)
PKEY_Devices_LocationPaths = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=37)
PKEY_Devices_Manufacturer = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8192)
PKEY_Devices_MetadataPath = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=71)
PKEY_Devices_MicrophoneArray_Geometry = PROPERTYKEY(Fmtid='a1829ea2-27eb-459e-935d-b2fad7b07762', Pid=2)
PKEY_Devices_MissedCalls = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=5)
PKEY_Devices_ModelId = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=2)
PKEY_Devices_ModelName = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8194)
PKEY_Devices_ModelNumber = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8195)
PKEY_Devices_NetworkedTooltip = PROPERTYKEY(Fmtid='880f70a2-6082-47ac-8aab-a739d1a300c3', Pid=152)
PKEY_Devices_NetworkName = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=7)
PKEY_Devices_NetworkType = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=8)
PKEY_Devices_NewPictures = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=4)
PKEY_Devices_Notification = PROPERTYKEY(Fmtid='06704b0c-e830-4c81-9178-91e4e95a80a0', Pid=3)
PKEY_Devices_Notifications_LowBattery = PROPERTYKEY(Fmtid='c4c07f2b-8524-4e66-ae3a-a6235f103beb', Pid=2)
PKEY_Devices_Notifications_MissedCall = PROPERTYKEY(Fmtid='6614ef48-4efe-4424-9eda-c79f404edf3e', Pid=2)
PKEY_Devices_Notifications_NewMessage = PROPERTYKEY(Fmtid='2be9260a-2012-4742-a555-f41b638b7dcb', Pid=2)
PKEY_Devices_Notifications_NewVoicemail = PROPERTYKEY(Fmtid='59569556-0a08-4212-95b9-fae2ad6413db', Pid=2)
PKEY_Devices_Notifications_StorageFull = PROPERTYKEY(Fmtid='a0e00ee1-f0c7-4d41-b8e7-26a7bd8d38b0', Pid=2)
PKEY_Devices_Notifications_StorageFullLinkText = PROPERTYKEY(Fmtid='a0e00ee1-f0c7-4d41-b8e7-26a7bd8d38b0', Pid=3)
PKEY_Devices_NotificationStore = PROPERTYKEY(Fmtid='06704b0c-e830-4c81-9178-91e4e95a80a0', Pid=2)
PKEY_Devices_NotWorkingProperly = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=83)
PKEY_Devices_Paired = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=56)
PKEY_Devices_Panel_PanelGroup = PROPERTYKEY(Fmtid='8dbc9c86-97a9-4bff-9bc6-bfe95d3e6dad', Pid=3)
PKEY_Devices_Panel_PanelId = PROPERTYKEY(Fmtid='8dbc9c86-97a9-4bff-9bc6-bfe95d3e6dad', Pid=2)
PKEY_Devices_Parent = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=8)
PKEY_Devices_PhoneLineTransportDevice_Connected = PROPERTYKEY(Fmtid='aecf2fe8-1d00-4fee-8a6d-a70d719b772b', Pid=2)
PKEY_Devices_PhysicalDeviceLocation = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=9)
PKEY_Devices_PlaybackPositionPercent = PROPERTYKEY(Fmtid='3633de59-6825-4381-a49b-9f6ba13a1471', Pid=5)
PKEY_Devices_PlaybackState = PROPERTYKEY(Fmtid='3633de59-6825-4381-a49b-9f6ba13a1471', Pid=2)
PLAYBACKSTATE_UNKNOWN = 0
PLAYBACKSTATE_STOPPED = 1
PLAYBACKSTATE_PLAYING = 2
PLAYBACKSTATE_TRANSITIONING = 3
PLAYBACKSTATE_PAUSED = 4
PLAYBACKSTATE_RECORDINGPAUSED = 5
PLAYBACKSTATE_RECORDING = 6
PLAYBACKSTATE_NOMEDIA = 7
PKEY_Devices_PlaybackTitle = PROPERTYKEY(Fmtid='3633de59-6825-4381-a49b-9f6ba13a1471', Pid=3)
PKEY_Devices_Present = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=5)
PKEY_Devices_PresentationUrl = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8198)
PKEY_Devices_PrimaryCategory = PROPERTYKEY(Fmtid='d08dd4c0-3a9e-462e-8290-7b636b2576b9', Pid=10)
PKEY_Devices_RemainingDuration = PROPERTYKEY(Fmtid='3633de59-6825-4381-a49b-9f6ba13a1471', Pid=4)
PKEY_Devices_RestrictedInterface = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=6)
PKEY_Devices_Roaming = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=9)
PKEY_Devices_SafeRemovalRequired = PROPERTYKEY(Fmtid='afd97640-86a3-4210-b67c-289c41aabe55', Pid=2)
PKEY_Devices_SchematicName = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=9)
PKEY_Devices_ServiceAddress = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=16384)
PKEY_Devices_ServiceId = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=16385)
PKEY_Devices_SharedTooltip = PROPERTYKEY(Fmtid='880f70a2-6082-47ac-8aab-a739d1a300c3', Pid=151)
PKEY_Devices_SignalStrength = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=2)
PKEY_Devices_SmartCards_ReaderKind = PROPERTYKEY(Fmtid='d6b5b883-18bd-4b4d-b2ec-9e38affeda82', Pid=2)
PKEY_Devices_Status = PROPERTYKEY(Fmtid='d08dd4c0-3a9e-462e-8290-7b636b2576b9', Pid=259)
PKEY_Devices_Status1 = PROPERTYKEY(Fmtid='d08dd4c0-3a9e-462e-8290-7b636b2576b9', Pid=257)
PKEY_Devices_Status2 = PROPERTYKEY(Fmtid='d08dd4c0-3a9e-462e-8290-7b636b2576b9', Pid=258)
PKEY_Devices_StorageCapacity = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=12)
PKEY_Devices_StorageFreeSpace = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=13)
PKEY_Devices_StorageFreeSpacePercent = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=14)
PKEY_Devices_TextMessages = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=3)
PKEY_Devices_Voicemail = PROPERTYKEY(Fmtid='49cd1f76-5626-4b17-a4e8-18b4aa1a2213', Pid=6)
PKEY_Devices_WiaDeviceType = PROPERTYKEY(Fmtid='6bdd1fc6-810f-11d0-bec7-08002be2092f', Pid=2)
PKEY_Devices_WiFi_InterfaceGuid = PROPERTYKEY(Fmtid='ef1167eb-cbfc-4341-a568-a7c91a68982c', Pid=2)
PKEY_Devices_WiFiDirect_DeviceAddress = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=13)
PKEY_Devices_WiFiDirect_GroupId = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=4)
PKEY_Devices_WiFiDirect_InformationElements = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=12)
PKEY_Devices_WiFiDirect_InterfaceAddress = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=2)
PKEY_Devices_WiFiDirect_InterfaceGuid = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=3)
PKEY_Devices_WiFiDirect_IsConnected = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=5)
PKEY_Devices_WiFiDirect_IsLegacyDevice = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=7)
PKEY_Devices_WiFiDirect_IsMiracastLcpSupported = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=9)
PKEY_Devices_WiFiDirect_IsVisible = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=6)
PKEY_Devices_WiFiDirect_MiracastVersion = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=8)
PKEY_Devices_WiFiDirect_Services = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=10)
PKEY_Devices_WiFiDirect_SupportedChannelList = PROPERTYKEY(Fmtid='1506935d-e3e7-450f-8637-82233ebe5f6e', Pid=11)
PKEY_Devices_WiFiDirectServices_AdvertisementId = PROPERTYKEY(Fmtid='31b37743-7c5e-4005-93e6-e953f92b82e9', Pid=5)
PKEY_Devices_WiFiDirectServices_RequestServiceInformation = PROPERTYKEY(Fmtid='31b37743-7c5e-4005-93e6-e953f92b82e9', Pid=7)
PKEY_Devices_WiFiDirectServices_ServiceAddress = PROPERTYKEY(Fmtid='31b37743-7c5e-4005-93e6-e953f92b82e9', Pid=2)
PKEY_Devices_WiFiDirectServices_ServiceConfigMethods = PROPERTYKEY(Fmtid='31b37743-7c5e-4005-93e6-e953f92b82e9', Pid=6)
PKEY_Devices_WiFiDirectServices_ServiceInformation = PROPERTYKEY(Fmtid='31b37743-7c5e-4005-93e6-e953f92b82e9', Pid=4)
PKEY_Devices_WiFiDirectServices_ServiceName = PROPERTYKEY(Fmtid='31b37743-7c5e-4005-93e6-e953f92b82e9', Pid=3)
PKEY_Devices_WinPhone8CameraFlags = PROPERTYKEY(Fmtid='b7b4d61c-5a64-4187-a52e-b1539f359099', Pid=2)
PKEY_Devices_Wwan_InterfaceGuid = PROPERTYKEY(Fmtid='ff1167eb-cbfc-4341-a568-a7c91a68982c', Pid=2)
PKEY_Storage_Portable = PROPERTYKEY(Fmtid='4d1ebee8-0803-4774-9842-b77db50265e9', Pid=2)
PKEY_Storage_RemovableMedia = PROPERTYKEY(Fmtid='4d1ebee8-0803-4774-9842-b77db50265e9', Pid=3)
PKEY_Storage_SystemCritical = PROPERTYKEY(Fmtid='4d1ebee8-0803-4774-9842-b77db50265e9', Pid=4)
PKEY_Document_ByteCount = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=4)
PKEY_Document_CharacterCount = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=16)
PKEY_Document_ClientID = PROPERTYKEY(Fmtid='276d7bb0-5b34-4fb0-aa4b-158ed12a1809', Pid=100)
PKEY_Document_Contributor = PROPERTYKEY(Fmtid='f334115e-da1b-4509-9b3d-119504dc7abb', Pid=100)
PKEY_Document_DateCreated = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=12)
PKEY_Document_DatePrinted = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=11)
PKEY_Document_DateSaved = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=13)
PKEY_Document_Division = PROPERTYKEY(Fmtid='1e005ee6-bf27-428b-b01c-79676acd2870', Pid=100)
PKEY_Document_DocumentID = PROPERTYKEY(Fmtid='e08805c8-e395-40df-80d2-54f0d6c43154', Pid=100)
PKEY_Document_HiddenSlideCount = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=9)
PKEY_Document_LastAuthor = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=8)
PKEY_Document_LineCount = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=5)
PKEY_Document_Manager = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=14)
PKEY_Document_MultimediaClipCount = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=10)
PKEY_Document_NoteCount = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=8)
PKEY_Document_PageCount = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=14)
PKEY_Document_ParagraphCount = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=6)
PKEY_Document_PresentationFormat = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=3)
PKEY_Document_RevisionNumber = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=9)
PKEY_Document_Security = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=19)
PKEY_Document_SlideCount = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=7)
PKEY_Document_Template = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=7)
PKEY_Document_TotalEditingTime = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=10)
PKEY_Document_Version = PROPERTYKEY(Fmtid='d5cdd502-2e9c-101b-9397-08002b2cf9ae', Pid=29)
PKEY_Document_WordCount = PROPERTYKEY(Fmtid='f29f85e0-4ff9-1068-ab91-08002b27b3d9', Pid=15)
PKEY_DRM_DatePlayExpires = PROPERTYKEY(Fmtid='aeac19e4-89ae-4508-b9b7-bb867abee2ed', Pid=6)
PKEY_DRM_DatePlayStarts = PROPERTYKEY(Fmtid='aeac19e4-89ae-4508-b9b7-bb867abee2ed', Pid=5)
PKEY_DRM_Description = PROPERTYKEY(Fmtid='aeac19e4-89ae-4508-b9b7-bb867abee2ed', Pid=3)
PKEY_DRM_IsDisabled = PROPERTYKEY(Fmtid='aeac19e4-89ae-4508-b9b7-bb867abee2ed', Pid=7)
PKEY_DRM_IsProtected = PROPERTYKEY(Fmtid='aeac19e4-89ae-4508-b9b7-bb867abee2ed', Pid=2)
PKEY_DRM_PlayCount = PROPERTYKEY(Fmtid='aeac19e4-89ae-4508-b9b7-bb867abee2ed', Pid=4)
PKEY_GPS_Altitude = PROPERTYKEY(Fmtid='827edb4f-5b73-44a7-891d-fdffabea35ca', Pid=100)
PKEY_GPS_AltitudeDenominator = PROPERTYKEY(Fmtid='78342dcb-e358-4145-ae9a-6bfe4e0f9f51', Pid=100)
PKEY_GPS_AltitudeNumerator = PROPERTYKEY(Fmtid='2dad1eb7-816d-40d3-9ec3-c9773be2aade', Pid=100)
PKEY_GPS_AltitudeRef = PROPERTYKEY(Fmtid='46ac629d-75ea-4515-867f-6dc4321c5844', Pid=100)
PKEY_GPS_AreaInformation = PROPERTYKEY(Fmtid='972e333e-ac7e-49f1-8adf-a70d07a9bcab', Pid=100)
PKEY_GPS_Date = PROPERTYKEY(Fmtid='3602c812-0f3b-45f0-85ad-603468d69423', Pid=100)
PKEY_GPS_DestBearing = PROPERTYKEY(Fmtid='c66d4b3c-e888-47cc-b99f-9dca3ee34dea', Pid=100)
PKEY_GPS_DestBearingDenominator = PROPERTYKEY(Fmtid='7abcf4f8-7c3f-4988-ac91-8d2c2e97eca5', Pid=100)
PKEY_GPS_DestBearingNumerator = PROPERTYKEY(Fmtid='ba3b1da9-86ee-4b5d-a2a4-a271a429f0cf', Pid=100)
PKEY_GPS_DestBearingRef = PROPERTYKEY(Fmtid='9ab84393-2a0f-4b75-bb22-7279786977cb', Pid=100)
PKEY_GPS_DestDistance = PROPERTYKEY(Fmtid='a93eae04-6804-4f24-ac81-09b266452118', Pid=100)
PKEY_GPS_DestDistanceDenominator = PROPERTYKEY(Fmtid='9bc2c99b-ac71-4127-9d1c-2596d0d7dcb7', Pid=100)
PKEY_GPS_DestDistanceNumerator = PROPERTYKEY(Fmtid='2bda47da-08c6-4fe1-80bc-a72fc517c5d0', Pid=100)
PKEY_GPS_DestDistanceRef = PROPERTYKEY(Fmtid='ed4df2d3-8695-450b-856f-f5c1c53acb66', Pid=100)
PKEY_GPS_DestLatitude = PROPERTYKEY(Fmtid='9d1d7cc5-5c39-451c-86b3-928e2d18cc47', Pid=100)
PKEY_GPS_DestLatitudeDenominator = PROPERTYKEY(Fmtid='3a372292-7fca-49a7-99d5-e47bb2d4e7ab', Pid=100)
PKEY_GPS_DestLatitudeNumerator = PROPERTYKEY(Fmtid='ecf4b6f6-d5a6-433c-bb92-4076650fc890', Pid=100)
PKEY_GPS_DestLatitudeRef = PROPERTYKEY(Fmtid='cea820b9-ce61-4885-a128-005d9087c192', Pid=100)
PKEY_GPS_DestLongitude = PROPERTYKEY(Fmtid='47a96261-cb4c-4807-8ad3-40b9d9dbc6bc', Pid=100)
PKEY_GPS_DestLongitudeDenominator = PROPERTYKEY(Fmtid='425d69e5-48ad-4900-8d80-6eb6b8d0ac86', Pid=100)
PKEY_GPS_DestLongitudeNumerator = PROPERTYKEY(Fmtid='a3250282-fb6d-48d5-9a89-dbcace75cccf', Pid=100)
PKEY_GPS_DestLongitudeRef = PROPERTYKEY(Fmtid='182c1ea6-7c1c-4083-ab4b-ac6c9f4ed128', Pid=100)
PKEY_GPS_Differential = PROPERTYKEY(Fmtid='aaf4ee25-bd3b-4dd7-bfc4-47f77bb00f6d', Pid=100)
PKEY_GPS_DOP = PROPERTYKEY(Fmtid='0cf8fb02-1837-42f1-a697-a7017aa289b9', Pid=100)
PKEY_GPS_DOPDenominator = PROPERTYKEY(Fmtid='a0be94c5-50ba-487b-bd35-0654be8881ed', Pid=100)
PKEY_GPS_DOPNumerator = PROPERTYKEY(Fmtid='47166b16-364f-4aa0-9f31-e2ab3df449c3', Pid=100)
PKEY_GPS_ImgDirection = PROPERTYKEY(Fmtid='16473c91-d017-4ed9-ba4d-b6baa55dbcf8', Pid=100)
PKEY_GPS_ImgDirectionDenominator = PROPERTYKEY(Fmtid='10b24595-41a2-4e20-93c2-5761c1395f32', Pid=100)
PKEY_GPS_ImgDirectionNumerator = PROPERTYKEY(Fmtid='dc5877c7-225f-45f7-bac7-e81334b6130a', Pid=100)
PKEY_GPS_ImgDirectionRef = PROPERTYKEY(Fmtid='a4aaa5b7-1ad0-445f-811a-0f8f6e67f6b5', Pid=100)
PKEY_GPS_Latitude = PROPERTYKEY(Fmtid='8727cfff-4868-4ec6-ad5b-81b98521d1ab', Pid=100)
PKEY_GPS_LatitudeDecimal = PROPERTYKEY(Fmtid='0f55cde2-4f49-450d-92c1-dcd16301b1b7', Pid=100)
PKEY_GPS_LatitudeDenominator = PROPERTYKEY(Fmtid='16e634ee-2bff-497b-bd8a-4341ad39eeb9', Pid=100)
PKEY_GPS_LatitudeNumerator = PROPERTYKEY(Fmtid='7ddaaad1-ccc8-41ae-b750-b2cb8031aea2', Pid=100)
PKEY_GPS_LatitudeRef = PROPERTYKEY(Fmtid='029c0252-5b86-46c7-aca0-2769ffc8e3d4', Pid=100)
PKEY_GPS_Longitude = PROPERTYKEY(Fmtid='c4c4dbb2-b593-466b-bbda-d03d27d5e43a', Pid=100)
PKEY_GPS_LongitudeDecimal = PROPERTYKEY(Fmtid='4679c1b5-844d-4590-baf5-f322231f1b81', Pid=100)
PKEY_GPS_LongitudeDenominator = PROPERTYKEY(Fmtid='be6e176c-4534-4d2c-ace5-31dedac1606b', Pid=100)
PKEY_GPS_LongitudeNumerator = PROPERTYKEY(Fmtid='02b0f689-a914-4e45-821d-1dda452ed2c4', Pid=100)
PKEY_GPS_LongitudeRef = PROPERTYKEY(Fmtid='33dcf22b-28d5-464c-8035-1ee9efd25278', Pid=100)
PKEY_GPS_MapDatum = PROPERTYKEY(Fmtid='2ca2dae6-eddc-407d-bef1-773942abfa95', Pid=100)
PKEY_GPS_MeasureMode = PROPERTYKEY(Fmtid='a015ed5d-aaea-4d58-8a86-3c586920ea0b', Pid=100)
PKEY_GPS_ProcessingMethod = PROPERTYKEY(Fmtid='59d49e61-840f-4aa9-a939-e2099b7f6399', Pid=100)
PKEY_GPS_Satellites = PROPERTYKEY(Fmtid='467ee575-1f25-4557-ad4e-b8b58b0d9c15', Pid=100)
PKEY_GPS_Speed = PROPERTYKEY(Fmtid='da5d0862-6e76-4e1b-babd-70021bd25494', Pid=100)
PKEY_GPS_SpeedDenominator = PROPERTYKEY(Fmtid='7d122d5a-ae5e-4335-8841-d71e7ce72f53', Pid=100)
PKEY_GPS_SpeedNumerator = PROPERTYKEY(Fmtid='acc9ce3d-c213-4942-8b48-6d0820f21c6d', Pid=100)
PKEY_GPS_SpeedRef = PROPERTYKEY(Fmtid='ecf7f4c9-544f-4d6d-9d98-8ad79adaf453', Pid=100)
PKEY_GPS_Status = PROPERTYKEY(Fmtid='125491f4-818f-46b2-91b5-d537753617b2', Pid=100)
PKEY_GPS_Track = PROPERTYKEY(Fmtid='76c09943-7c33-49e3-9e7e-cdba872cfada', Pid=100)
PKEY_GPS_TrackDenominator = PROPERTYKEY(Fmtid='c8d1920c-01f6-40c0-ac86-2f3a4ad00770', Pid=100)
PKEY_GPS_TrackNumerator = PROPERTYKEY(Fmtid='702926f4-44a6-43e1-ae71-45627116893b', Pid=100)
PKEY_GPS_TrackRef = PROPERTYKEY(Fmtid='35dbe6fe-44c3-4400-aaae-d2c799c407e8', Pid=100)
PKEY_GPS_VersionID = PROPERTYKEY(Fmtid='22704da4-c6b2-4a99-8e56-f16df8c92599', Pid=100)
PKEY_History_VisitCount = PROPERTYKEY(Fmtid='5cbf2787-48cf-4208-b90e-ee5e5d420294', Pid=7)
PKEY_Image_BitDepth = PROPERTYKEY(Fmtid='6444048f-4c8b-11d1-8b70-080036b11a03', Pid=7)
PKEY_Image_ColorSpace = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=40961)
PKEY_Image_CompressedBitsPerPixel = PROPERTYKEY(Fmtid='364b6fa9-37ab-482a-be2b-ae02f60d4318', Pid=100)
PKEY_Image_CompressedBitsPerPixelDenominator = PROPERTYKEY(Fmtid='1f8844e1-24ad-4508-9dfd-5326a415ce02', Pid=100)
PKEY_Image_CompressedBitsPerPixelNumerator = PROPERTYKEY(Fmtid='d21a7148-d32c-4624-8900-277210f79c0f', Pid=100)
PKEY_Image_Compression = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=259)
PKEY_Image_CompressionText = PROPERTYKEY(Fmtid='3f08e66f-2f44-4bb9-a682-ac35d2562322', Pid=100)
PKEY_Image_Dimensions = PROPERTYKEY(Fmtid='6444048f-4c8b-11d1-8b70-080036b11a03', Pid=13)
PKEY_Image_HorizontalResolution = PROPERTYKEY(Fmtid='6444048f-4c8b-11d1-8b70-080036b11a03', Pid=5)
PKEY_Image_HorizontalSize = PROPERTYKEY(Fmtid='6444048f-4c8b-11d1-8b70-080036b11a03', Pid=3)
PKEY_Image_ImageID = PROPERTYKEY(Fmtid='10dabe05-32aa-4c29-bf1a-63e2d220587f', Pid=100)
PKEY_Image_ResolutionUnit = PROPERTYKEY(Fmtid='19b51fa6-1f92-4a5c-ab48-7df0abd67444', Pid=100)
PKEY_Image_VerticalResolution = PROPERTYKEY(Fmtid='6444048f-4c8b-11d1-8b70-080036b11a03', Pid=6)
PKEY_Image_VerticalSize = PROPERTYKEY(Fmtid='6444048f-4c8b-11d1-8b70-080036b11a03', Pid=4)
PKEY_Journal_Contacts = PROPERTYKEY(Fmtid='dea7c82c-1d89-4a66-9427-a4e3debabcb1', Pid=100)
PKEY_Journal_EntryType = PROPERTYKEY(Fmtid='95beb1fc-326d-4644-b396-cd3ed90e6ddf', Pid=100)
PKEY_LayoutPattern_ContentViewModeForBrowse = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=500)
PKEY_LayoutPattern_ContentViewModeForSearch = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=501)
PKEY_History_SelectionCount = PROPERTYKEY(Fmtid='1ce0d6bc-536c-4600-b0dd-7e0c66b350d5', Pid=8)
PKEY_History_TargetUrlHostName = PROPERTYKEY(Fmtid='1ce0d6bc-536c-4600-b0dd-7e0c66b350d5', Pid=9)
PKEY_Link_Arguments = PROPERTYKEY(Fmtid='436f2667-14e2-4feb-b30a-146c53b5b674', Pid=100)
PKEY_Link_Comment = PROPERTYKEY(Fmtid='b9b4b3fc-2b51-4a42-b5d8-324146afcf25', Pid=5)
PKEY_Link_DateVisited = PROPERTYKEY(Fmtid='5cbf2787-48cf-4208-b90e-ee5e5d420294', Pid=23)
PKEY_Link_Description = PROPERTYKEY(Fmtid='5cbf2787-48cf-4208-b90e-ee5e5d420294', Pid=21)
PKEY_Link_FeedItemLocalId = PROPERTYKEY(Fmtid='8a2f99f9-3c37-465d-a8d7-69777a246d0c', Pid=2)
PKEY_Link_Status = PROPERTYKEY(Fmtid='b9b4b3fc-2b51-4a42-b5d8-324146afcf25', Pid=3)
LINK_STATUS_RESOLVED = 1
LINK_STATUS_BROKEN = 2
PKEY_Link_TargetExtension = PROPERTYKEY(Fmtid='7a7d76f4-b630-4bd7-95ff-37cc51a975c9', Pid=2)
PKEY_Link_TargetParsingPath = PROPERTYKEY(Fmtid='b9b4b3fc-2b51-4a42-b5d8-324146afcf25', Pid=2)
PKEY_Link_TargetSFGAOFlags = PROPERTYKEY(Fmtid='b9b4b3fc-2b51-4a42-b5d8-324146afcf25', Pid=8)
PKEY_Link_TargetUrlHostName = PROPERTYKEY(Fmtid='8a2f99f9-3c37-465d-a8d7-69777a246d0c', Pid=5)
PKEY_Link_TargetUrlPath = PROPERTYKEY(Fmtid='8a2f99f9-3c37-465d-a8d7-69777a246d0c', Pid=6)
PKEY_Media_AuthorUrl = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=32)
PKEY_Media_AverageLevel = PROPERTYKEY(Fmtid='09edd5b6-b301-43c5-9990-d00302effd46', Pid=100)
PKEY_Media_ClassPrimaryID = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=13)
PKEY_Media_ClassSecondaryID = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=14)
PKEY_Media_CollectionGroupID = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=24)
PKEY_Media_CollectionID = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=25)
PKEY_Media_ContentDistributor = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=18)
PKEY_Media_ContentID = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=26)
PKEY_Media_CreatorApplication = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=27)
PKEY_Media_CreatorApplicationVersion = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=28)
PKEY_Media_DateEncoded = PROPERTYKEY(Fmtid='2e4b640d-5019-46d8-8881-55414cc5caa0', Pid=100)
PKEY_Media_DateReleased = PROPERTYKEY(Fmtid='de41cc29-6971-4290-b472-f59f2e2f31e2', Pid=100)
PKEY_Media_DlnaProfileID = PROPERTYKEY(Fmtid='cfa31b45-525d-4998-bb44-3f7d81542fa4', Pid=100)
PKEY_Media_Duration = PROPERTYKEY(Fmtid='64440490-4c8b-11d1-8b70-080036b11a03', Pid=3)
PKEY_Media_DVDID = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=15)
PKEY_Media_EncodedBy = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=36)
PKEY_Media_EncodingSettings = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=37)
PKEY_Media_EpisodeNumber = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=100)
PKEY_Media_FrameCount = PROPERTYKEY(Fmtid='6444048f-4c8b-11d1-8b70-080036b11a03', Pid=12)
PKEY_Media_MCDI = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=16)
PKEY_Media_MetadataContentProvider = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=17)
PKEY_Media_Producer = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=22)
PKEY_Media_PromotionUrl = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=33)
PKEY_Media_ProtectionType = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=38)
PKEY_Media_ProviderRating = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=39)
PKEY_Media_ProviderStyle = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=40)
PKEY_Media_Publisher = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=30)
PKEY_Media_SeasonNumber = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=101)
PKEY_Media_SeriesName = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=42)
PKEY_Media_SubscriptionContentId = PROPERTYKEY(Fmtid='9aebae7a-9644-487d-a92c-657585ed751a', Pid=100)
PKEY_Media_SubTitle = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=38)
PKEY_Media_ThumbnailLargePath = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=47)
PKEY_Media_ThumbnailLargeUri = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=48)
PKEY_Media_ThumbnailSmallPath = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=49)
PKEY_Media_ThumbnailSmallUri = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=50)
PKEY_Media_UniqueFileIdentifier = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=35)
PKEY_Media_UserNoAutoInfo = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=41)
PKEY_Media_UserWebUrl = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=34)
PKEY_Media_Writer = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=23)
PKEY_Media_Year = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=5)
PKEY_Message_AttachmentContents = PROPERTYKEY(Fmtid='3143bf7c-80a8-4854-8880-e2e40189bdd0', Pid=100)
PKEY_Message_AttachmentNames = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=21)
PKEY_Message_BccAddress = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=2)
PKEY_Message_BccName = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=3)
PKEY_Message_CcAddress = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=4)
PKEY_Message_CcName = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=5)
PKEY_Message_ConversationID = PROPERTYKEY(Fmtid='dc8f80bd-af1e-4289-85b6-3dfc1b493992', Pid=100)
PKEY_Message_ConversationIndex = PROPERTYKEY(Fmtid='dc8f80bd-af1e-4289-85b6-3dfc1b493992', Pid=101)
PKEY_Message_DateReceived = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=20)
PKEY_Message_DateSent = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=19)
PKEY_Message_Flags = PROPERTYKEY(Fmtid='a82d9ee7-ca67-4312-965e-226bcea85023', Pid=100)
PKEY_Message_FromAddress = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=13)
PKEY_Message_FromName = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=14)
PKEY_Message_HasAttachments = PROPERTYKEY(Fmtid='9c1fcf74-2d97-41ba-b4ae-cb2e3661a6e4', Pid=8)
PKEY_Message_IsFwdOrReply = PROPERTYKEY(Fmtid='9a9bc088-4f6d-469e-9919-e705412040f9', Pid=100)
PKEY_Message_MessageClass = PROPERTYKEY(Fmtid='cd9ed458-08ce-418f-a70e-f912c7bb9c5c', Pid=103)
PKEY_Message_Participants = PROPERTYKEY(Fmtid='1a9ba605-8e7c-4d11-ad7d-a50ada18ba1b', Pid=2)
PKEY_Message_ProofInProgress = PROPERTYKEY(Fmtid='9098f33c-9a7d-48a8-8de5-2e1227a64e91', Pid=100)
PKEY_Message_SenderAddress = PROPERTYKEY(Fmtid='0be1c8e7-1981-4676-ae14-fdd78f05a6e7', Pid=100)
PKEY_Message_SenderName = PROPERTYKEY(Fmtid='0da41cfa-d224-4a18-ae2f-596158db4b3a', Pid=100)
PKEY_Message_Store = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=15)
PKEY_Message_ToAddress = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=16)
PKEY_Message_ToDoFlags = PROPERTYKEY(Fmtid='1f856a9f-6900-4aba-9505-2d5f1b4d66cb', Pid=100)
PKEY_Message_ToDoTitle = PROPERTYKEY(Fmtid='bccc8a3c-8cef-42e5-9b1c-c69079398bc7', Pid=100)
PKEY_Message_ToName = PROPERTYKEY(Fmtid='e3e0584c-b788-4a5a-bb20-7f5a44c9acdd', Pid=17)
PKEY_Music_AlbumArtist = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=13)
PKEY_Music_AlbumArtistSortOverride = PROPERTYKEY(Fmtid='f1fdb4af-f78c-466c-bb05-56e92db0b8ec', Pid=103)
PKEY_Music_AlbumID = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=100)
PKEY_Music_AlbumTitle = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=4)
PKEY_Music_AlbumTitleSortOverride = PROPERTYKEY(Fmtid='13eb7ffc-ec89-4346-b19d-ccc6f1784223', Pid=101)
PKEY_Music_Artist = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=2)
PKEY_Music_ArtistSortOverride = PROPERTYKEY(Fmtid='deeb2db5-0696-4ce0-94fe-a01f77a45fb5', Pid=102)
PKEY_Music_BeatsPerMinute = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=35)
PKEY_Music_Composer = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=19)
PKEY_Music_ComposerSortOverride = PROPERTYKEY(Fmtid='00bc20a3-bd48-4085-872c-a88d77f5097e', Pid=105)
PKEY_Music_Conductor = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=36)
PKEY_Music_ContentGroupDescription = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=33)
PKEY_Music_DiscNumber = PROPERTYKEY(Fmtid='6afe7437-9bcd-49c7-80fe-4a5c65fa5874', Pid=104)
PKEY_Music_DisplayArtist = PROPERTYKEY(Fmtid='fd122953-fa93-4ef7-92c3-04c946b2f7c8', Pid=100)
PKEY_Music_Genre = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=11)
PKEY_Music_InitialKey = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=34)
PKEY_Music_IsCompilation = PROPERTYKEY(Fmtid='c449d5cb-9ea4-4809-82e8-af9d59ded6d1', Pid=100)
PKEY_Music_Lyrics = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=12)
PKEY_Music_Mood = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=39)
PKEY_Music_PartOfSet = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=37)
PKEY_Music_Period = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=31)
PKEY_Music_SynchronizedLyrics = PROPERTYKEY(Fmtid='6b223b6a-162e-4aa9-b39f-05d678fc6d77', Pid=100)
PKEY_Music_TrackNumber = PROPERTYKEY(Fmtid='56a3372e-ce9c-11d2-9f0e-006097c686f6', Pid=7)
PKEY_Note_Color = PROPERTYKEY(Fmtid='4776cafa-bce4-4cb1-a23e-265e76d8eb11', Pid=100)
PKEY_Note_ColorText = PROPERTYKEY(Fmtid='46b4e8de-cdb2-440d-885c-1658eb65b914', Pid=100)
PKEY_Photo_Aperture = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=37378)
PKEY_Photo_ApertureDenominator = PROPERTYKEY(Fmtid='e1a9a38b-6685-46bd-875e-570dc7ad7320', Pid=100)
PKEY_Photo_ApertureNumerator = PROPERTYKEY(Fmtid='0337ecec-39fb-4581-a0bd-4c4cc51e9914', Pid=100)
PKEY_Photo_Brightness = PROPERTYKEY(Fmtid='1a701bf6-478c-4361-83ab-3701bb053c58', Pid=100)
PKEY_Photo_BrightnessDenominator = PROPERTYKEY(Fmtid='6ebe6946-2321-440a-90f0-c043efd32476', Pid=100)
PKEY_Photo_BrightnessNumerator = PROPERTYKEY(Fmtid='9e7d118f-b314-45a0-8cfb-d654b917c9e9', Pid=100)
PKEY_Photo_CameraManufacturer = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=271)
PKEY_Photo_CameraModel = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=272)
PKEY_Photo_CameraSerialNumber = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=273)
PKEY_Photo_Contrast = PROPERTYKEY(Fmtid='2a785ba9-8d23-4ded-82e6-60a350c86a10', Pid=100)
PHOTO_CONTRAST_NORMAL = 0
PHOTO_CONTRAST_SOFT = 1
PHOTO_CONTRAST_HARD = 2
PKEY_Photo_ContrastText = PROPERTYKEY(Fmtid='59dde9f2-5253-40ea-9a8b-479e96c6249a', Pid=100)
PKEY_Photo_DateTaken = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=36867)
PKEY_Photo_DigitalZoom = PROPERTYKEY(Fmtid='f85bf840-a925-4bc2-b0c4-8e36b598679e', Pid=100)
PKEY_Photo_DigitalZoomDenominator = PROPERTYKEY(Fmtid='745baf0e-e5c1-4cfb-8a1b-d031a0a52393', Pid=100)
PKEY_Photo_DigitalZoomNumerator = PROPERTYKEY(Fmtid='16cbb924-6500-473b-a5be-f1599bcbe413', Pid=100)
PKEY_Photo_Event = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=18248)
PKEY_Photo_EXIFVersion = PROPERTYKEY(Fmtid='d35f743a-eb2e-47f2-a286-844132cb1427', Pid=100)
PKEY_Photo_ExposureBias = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=37380)
PKEY_Photo_ExposureBiasDenominator = PROPERTYKEY(Fmtid='ab205e50-04b7-461c-a18c-2f233836e627', Pid=100)
PKEY_Photo_ExposureBiasNumerator = PROPERTYKEY(Fmtid='738bf284-1d87-420b-92cf-5834bf6ef9ed', Pid=100)
PKEY_Photo_ExposureIndex = PROPERTYKEY(Fmtid='967b5af8-995a-46ed-9e11-35b3c5b9782d', Pid=100)
PKEY_Photo_ExposureIndexDenominator = PROPERTYKEY(Fmtid='93112f89-c28b-492f-8a9d-4be2062cee8a', Pid=100)
PKEY_Photo_ExposureIndexNumerator = PROPERTYKEY(Fmtid='cdedcf30-8919-44df-8f4c-4eb2ffdb8d89', Pid=100)
PKEY_Photo_ExposureProgram = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=34850)
PHOTO_EXPOSUREPROGRAM_UNKNOWN = 0
PHOTO_EXPOSUREPROGRAM_MANUAL = 1
PHOTO_EXPOSUREPROGRAM_NORMAL = 2
PHOTO_EXPOSUREPROGRAM_APERTURE = 3
PHOTO_EXPOSUREPROGRAM_SHUTTER = 4
PHOTO_EXPOSUREPROGRAM_CREATIVE = 5
PHOTO_EXPOSUREPROGRAM_ACTION = 6
PHOTO_EXPOSUREPROGRAM_PORTRAIT = 7
PHOTO_EXPOSUREPROGRAM_LANDSCAPE = 8
PKEY_Photo_ExposureProgramText = PROPERTYKEY(Fmtid='fec690b7-5f30-4646-ae47-4caafba884a3', Pid=100)
PKEY_Photo_ExposureTime = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=33434)
PKEY_Photo_ExposureTimeDenominator = PROPERTYKEY(Fmtid='55e98597-ad16-42e0-b624-21599a199838', Pid=100)
PKEY_Photo_ExposureTimeNumerator = PROPERTYKEY(Fmtid='257e44e2-9031-4323-ac38-85c552871b2e', Pid=100)
PKEY_Photo_Flash = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=37385)
PHOTO_FLASH_NONE = 0
PHOTO_FLASH_FLASH = 1
PHOTO_FLASH_WITHOUTSTROBE = 5
PHOTO_FLASH_WITHSTROBE = 7
PHOTO_FLASH_FLASH_COMPULSORY = 9
PHOTO_FLASH_FLASH_COMPULSORY_NORETURNLIGHT = 13
PHOTO_FLASH_FLASH_COMPULSORY_RETURNLIGHT = 15
PHOTO_FLASH_NONE_COMPULSORY = 16
PHOTO_FLASH_NONE_AUTO = 24
PHOTO_FLASH_FLASH_AUTO = 25
PHOTO_FLASH_FLASH_AUTO_NORETURNLIGHT = 29
PHOTO_FLASH_FLASH_AUTO_RETURNLIGHT = 31
PHOTO_FLASH_NOFUNCTION = 32
PHOTO_FLASH_FLASH_REDEYE = 65
PHOTO_FLASH_FLASH_REDEYE_NORETURNLIGHT = 69
PHOTO_FLASH_FLASH_REDEYE_RETURNLIGHT = 71
PHOTO_FLASH_FLASH_COMPULSORY_REDEYE = 73
PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_NORETURNLIGHT = 77
PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_RETURNLIGHT = 79
PHOTO_FLASH_FLASH_AUTO_REDEYE = 89
PHOTO_FLASH_FLASH_AUTO_REDEYE_NORETURNLIGHT = 93
PHOTO_FLASH_FLASH_AUTO_REDEYE_RETURNLIGHT = 95
PKEY_Photo_FlashEnergy = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=41483)
PKEY_Photo_FlashEnergyDenominator = PROPERTYKEY(Fmtid='d7b61c70-6323-49cd-a5fc-c84277162c97', Pid=100)
PKEY_Photo_FlashEnergyNumerator = PROPERTYKEY(Fmtid='fcad3d3d-0858-400f-aaa3-2f66cce2a6bc', Pid=100)
PKEY_Photo_FlashManufacturer = PROPERTYKEY(Fmtid='aabaf6c9-e0c5-4719-8585-57b103e584fe', Pid=100)
PKEY_Photo_FlashModel = PROPERTYKEY(Fmtid='fe83bb35-4d1a-42e2-916b-06f3e1af719e', Pid=100)
PKEY_Photo_FlashText = PROPERTYKEY(Fmtid='6b8b68f6-200b-47ea-8d25-d8050f57339f', Pid=100)
PKEY_Photo_FNumber = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=33437)
PKEY_Photo_FNumberDenominator = PROPERTYKEY(Fmtid='e92a2496-223b-4463-a4e3-30eabba79d80', Pid=100)
PKEY_Photo_FNumberNumerator = PROPERTYKEY(Fmtid='1b97738a-fdfc-462f-9d93-1957e08be90c', Pid=100)
PKEY_Photo_FocalLength = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=37386)
PKEY_Photo_FocalLengthDenominator = PROPERTYKEY(Fmtid='305bc615-dca1-44a5-9fd4-10c0ba79412e', Pid=100)
PKEY_Photo_FocalLengthInFilm = PROPERTYKEY(Fmtid='a0e74609-b84d-4f49-b860-462bd9971f98', Pid=100)
PKEY_Photo_FocalLengthNumerator = PROPERTYKEY(Fmtid='776b6b3b-1e3d-4b0c-9a0e-8fbaf2a8492a', Pid=100)
PKEY_Photo_FocalPlaneXResolution = PROPERTYKEY(Fmtid='cfc08d97-c6f7-4484-89dd-ebef4356fe76', Pid=100)
PKEY_Photo_FocalPlaneXResolutionDenominator = PROPERTYKEY(Fmtid='0933f3f5-4786-4f46-a8e8-d64dd37fa521', Pid=100)
PKEY_Photo_FocalPlaneXResolutionNumerator = PROPERTYKEY(Fmtid='dccb10af-b4e2-4b88-95f9-031b4d5ab490', Pid=100)
PKEY_Photo_FocalPlaneYResolution = PROPERTYKEY(Fmtid='4fffe4d0-914f-4ac4-8d6f-c9c61de169b1', Pid=100)
PKEY_Photo_FocalPlaneYResolutionDenominator = PROPERTYKEY(Fmtid='1d6179a6-a876-4031-b013-3347b2b64dc8', Pid=100)
PKEY_Photo_FocalPlaneYResolutionNumerator = PROPERTYKEY(Fmtid='a2e541c5-4440-4ba8-867e-75cfc06828cd', Pid=100)
PKEY_Photo_GainControl = PROPERTYKEY(Fmtid='fa304789-00c7-4d80-904a-1e4dcc7265aa', Pid=100)
PHOTO_GAINCONTROL_NONE = 0
PHOTO_GAINCONTROL_LOWGAINUP = 1
PHOTO_GAINCONTROL_HIGHGAINUP = 2
PHOTO_GAINCONTROL_LOWGAINDOWN = 3
PHOTO_GAINCONTROL_HIGHGAINDOWN = 4
PKEY_Photo_GainControlDenominator = PROPERTYKEY(Fmtid='42864dfd-9da4-4f77-bded-4aad7b256735', Pid=100)
PKEY_Photo_GainControlNumerator = PROPERTYKEY(Fmtid='8e8ecf7c-b7b8-4eb8-a63f-0ee715c96f9e', Pid=100)
PKEY_Photo_GainControlText = PROPERTYKEY(Fmtid='c06238b2-0bf9-4279-a723-25856715cb9d', Pid=100)
PKEY_Photo_ISOSpeed = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=34855)
PKEY_Photo_LensManufacturer = PROPERTYKEY(Fmtid='e6ddcaf7-29c5-4f0a-9a68-d19412ec7090', Pid=100)
PKEY_Photo_LensModel = PROPERTYKEY(Fmtid='e1277516-2b5f-4869-89b1-2e585bd38b7a', Pid=100)
PKEY_Photo_LightSource = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=37384)
PHOTO_LIGHTSOURCE_UNKNOWN = 0
PHOTO_LIGHTSOURCE_DAYLIGHT = 1
PHOTO_LIGHTSOURCE_FLUORESCENT = 2
PHOTO_LIGHTSOURCE_TUNGSTEN = 3
PHOTO_LIGHTSOURCE_STANDARD_A = 17
PHOTO_LIGHTSOURCE_STANDARD_B = 18
PHOTO_LIGHTSOURCE_STANDARD_C = 19
PHOTO_LIGHTSOURCE_D55 = 20
PHOTO_LIGHTSOURCE_D65 = 21
PHOTO_LIGHTSOURCE_D75 = 22
PKEY_Photo_MakerNote = PROPERTYKEY(Fmtid='fa303353-b659-4052-85e9-bcac79549b84', Pid=100)
PKEY_Photo_MakerNoteOffset = PROPERTYKEY(Fmtid='813f4124-34e6-4d17-ab3e-6b1f3c2247a1', Pid=100)
PKEY_Photo_MaxAperture = PROPERTYKEY(Fmtid='08f6d7c2-e3f2-44fc-af1e-5aa5c81a2d3e', Pid=100)
PKEY_Photo_MaxApertureDenominator = PROPERTYKEY(Fmtid='c77724d4-601f-46c5-9b89-c53f93bceb77', Pid=100)
PKEY_Photo_MaxApertureNumerator = PROPERTYKEY(Fmtid='c107e191-a459-44c5-9ae6-b952ad4b906d', Pid=100)
PKEY_Photo_MeteringMode = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=37383)
PKEY_Photo_MeteringModeText = PROPERTYKEY(Fmtid='f628fd8c-7ba8-465a-a65b-c5aa79263a9e', Pid=100)
PKEY_Photo_Orientation = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=274)
PKEY_Photo_OrientationText = PROPERTYKEY(Fmtid='a9ea193c-c511-498a-a06b-58e2776dcc28', Pid=100)
PKEY_Photo_PeopleNames = PROPERTYKEY(Fmtid='e8309b6e-084c-49b4-b1fc-90a80331b638', Pid=100)
PKEY_Photo_PhotometricInterpretation = PROPERTYKEY(Fmtid='341796f1-1df9-4b1c-a564-91bdefa43877', Pid=100)
PKEY_Photo_PhotometricInterpretationText = PROPERTYKEY(Fmtid='821437d6-9eab-4765-a589-3b1cbbd22a61', Pid=100)
PKEY_Photo_ProgramMode = PROPERTYKEY(Fmtid='6d217f6d-3f6a-4825-b470-5f03ca2fbe9b', Pid=100)
PHOTO_PROGRAMMODE_NOTDEFINED = 0
PHOTO_PROGRAMMODE_MANUAL = 1
PHOTO_PROGRAMMODE_NORMAL = 2
PHOTO_PROGRAMMODE_APERTURE = 3
PHOTO_PROGRAMMODE_SHUTTER = 4
PHOTO_PROGRAMMODE_CREATIVE = 5
PHOTO_PROGRAMMODE_ACTION = 6
PHOTO_PROGRAMMODE_PORTRAIT = 7
PHOTO_PROGRAMMODE_LANDSCAPE = 8
PKEY_Photo_ProgramModeText = PROPERTYKEY(Fmtid='7fe3aa27-2648-42f3-89b0-454e5cb150c3', Pid=100)
PKEY_Photo_RelatedSoundFile = PROPERTYKEY(Fmtid='318a6b45-087f-4dc2-b8cc-05359551fc9e', Pid=100)
PKEY_Photo_Saturation = PROPERTYKEY(Fmtid='49237325-a95a-4f67-b211-816b2d45d2e0', Pid=100)
PHOTO_SATURATION_NORMAL = 0
PHOTO_SATURATION_LOW = 1
PHOTO_SATURATION_HIGH = 2
PKEY_Photo_SaturationText = PROPERTYKEY(Fmtid='61478c08-b600-4a84-bbe4-e99c45f0a072', Pid=100)
PKEY_Photo_Sharpness = PROPERTYKEY(Fmtid='fc6976db-8349-4970-ae97-b3c5316a08f0', Pid=100)
PHOTO_SHARPNESS_NORMAL = 0
PHOTO_SHARPNESS_SOFT = 1
PHOTO_SHARPNESS_HARD = 2
PKEY_Photo_SharpnessText = PROPERTYKEY(Fmtid='51ec3f47-dd50-421d-8769-334f50424b1e', Pid=100)
PKEY_Photo_ShutterSpeed = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=37377)
PKEY_Photo_ShutterSpeedDenominator = PROPERTYKEY(Fmtid='e13d8975-81c7-4948-ae3f-37cae11e8ff7', Pid=100)
PKEY_Photo_ShutterSpeedNumerator = PROPERTYKEY(Fmtid='16ea4042-d6f4-4bca-8349-7c78d30fb333', Pid=100)
PKEY_Photo_SubjectDistance = PROPERTYKEY(Fmtid='14b81da1-0135-4d31-96d9-6cbfc9671a99', Pid=37382)
PKEY_Photo_SubjectDistanceDenominator = PROPERTYKEY(Fmtid='0c840a88-b043-466d-9766-d4b26da3fa77', Pid=100)
PKEY_Photo_SubjectDistanceNumerator = PROPERTYKEY(Fmtid='8af4961c-f526-43e5-aa81-db768219178d', Pid=100)
PKEY_Photo_TagViewAggregate = PROPERTYKEY(Fmtid='b812f15d-c2d8-4bbf-bacd-79744346113f', Pid=100)
PKEY_Photo_TranscodedForSync = PROPERTYKEY(Fmtid='9a8ebb75-6458-4e82-bacb-35c0095b03bb', Pid=100)
PKEY_Photo_WhiteBalance = PROPERTYKEY(Fmtid='ee3d3d8a-5381-4cfa-b13b-aaf66b5f4ec9', Pid=100)
PHOTO_WHITEBALANCE_AUTO = 0
PHOTO_WHITEBALANCE_MANUAL = 1
PKEY_Photo_WhiteBalanceText = PROPERTYKEY(Fmtid='6336b95e-c7a7-426d-86fd-7ae3d39c84b4', Pid=100)
PKEY_PropGroup_Advanced = PROPERTYKEY(Fmtid='900a403b-097b-4b95-8ae2-071fdaeeb118', Pid=100)
PKEY_PropGroup_Audio = PROPERTYKEY(Fmtid='2804d469-788f-48aa-8570-71b9c187e138', Pid=100)
PKEY_PropGroup_Calendar = PROPERTYKEY(Fmtid='9973d2b5-bfd8-438a-ba94-5349b293181a', Pid=100)
PKEY_PropGroup_Camera = PROPERTYKEY(Fmtid='de00de32-547e-4981-ad4b-542f2e9007d8', Pid=100)
PKEY_PropGroup_Contact = PROPERTYKEY(Fmtid='df975fd3-250a-4004-858f-34e29a3e37aa', Pid=100)
PKEY_PropGroup_Content = PROPERTYKEY(Fmtid='d0dab0ba-368a-4050-a882-6c010fd19a4f', Pid=100)
PKEY_PropGroup_Description = PROPERTYKEY(Fmtid='8969b275-9475-4e00-a887-ff93b8b41e44', Pid=100)
PKEY_PropGroup_FileSystem = PROPERTYKEY(Fmtid='e3a7d2c1-80fc-4b40-8f34-30ea111bdc2e', Pid=100)
PKEY_PropGroup_General = PROPERTYKEY(Fmtid='cc301630-b192-4c22-b372-9f4c6d338e07', Pid=100)
PKEY_PropGroup_GPS = PROPERTYKEY(Fmtid='f3713ada-90e3-4e11-aae5-fdc17685b9be', Pid=100)
PKEY_PropGroup_Image = PROPERTYKEY(Fmtid='e3690a87-0fa8-4a2a-9a9f-fce8827055ac', Pid=100)
PKEY_PropGroup_Media = PROPERTYKEY(Fmtid='61872cf7-6b5e-4b4b-ac2d-59da84459248', Pid=100)
PKEY_PropGroup_MediaAdvanced = PROPERTYKEY(Fmtid='8859a284-de7e-4642-99ba-d431d044b1ec', Pid=100)
PKEY_PropGroup_Message = PROPERTYKEY(Fmtid='7fd7259d-16b4-4135-9f97-7c96ecd2fa9e', Pid=100)
PKEY_PropGroup_Music = PROPERTYKEY(Fmtid='68dd6094-7216-40f1-a029-43fe7127043f', Pid=100)
PKEY_PropGroup_Origin = PROPERTYKEY(Fmtid='2598d2fb-5569-4367-95df-5cd3a177e1a5', Pid=100)
PKEY_PropGroup_PhotoAdvanced = PROPERTYKEY(Fmtid='0cb2bf5a-9ee7-4a86-8222-f01e07fdadaf', Pid=100)
PKEY_PropGroup_RecordedTV = PROPERTYKEY(Fmtid='e7b33238-6584-4170-a5c0-ac25efd9da56', Pid=100)
PKEY_PropGroup_Video = PROPERTYKEY(Fmtid='bebe0920-7671-4c54-a3eb-49fddfc191ee', Pid=100)
PKEY_InfoTipText = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=17)
PKEY_PropList_ConflictPrompt = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=11)
PKEY_PropList_ContentViewModeForBrowse = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=13)
PKEY_PropList_ContentViewModeForSearch = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=14)
PKEY_PropList_ExtendedTileInfo = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=9)
PKEY_PropList_FileOperationPrompt = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=10)
PKEY_PropList_FullDetails = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=2)
PKEY_PropList_InfoTip = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=4)
PKEY_PropList_NonPersonal = PROPERTYKEY(Fmtid='49d1091f-082e-493f-b23f-d2308aa9668c', Pid=100)
PKEY_PropList_PreviewDetails = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=8)
PKEY_PropList_PreviewTitle = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=6)
PKEY_PropList_QuickTip = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=5)
PKEY_PropList_TileInfo = PROPERTYKEY(Fmtid='c9944a21-a406-48fe-8225-aec7e24c211b', Pid=3)
PKEY_PropList_XPDetailsPanel = PROPERTYKEY(Fmtid='f2275480-f782-4291-bd94-f13693513aec', Pid=0)
PKEY_RecordedTV_ChannelNumber = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=7)
PKEY_RecordedTV_Credits = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=4)
PKEY_RecordedTV_DateContentExpires = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=15)
PKEY_RecordedTV_EpisodeName = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=2)
PKEY_RecordedTV_IsATSCContent = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=16)
PKEY_RecordedTV_IsClosedCaptioningAvailable = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=12)
PKEY_RecordedTV_IsDTVContent = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=17)
PKEY_RecordedTV_IsHDContent = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=18)
PKEY_RecordedTV_IsRepeatBroadcast = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=13)
PKEY_RecordedTV_IsSAP = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=14)
PKEY_RecordedTV_NetworkAffiliation = PROPERTYKEY(Fmtid='2c53c813-fb63-4e22-a1ab-0b331ca1e273', Pid=100)
PKEY_RecordedTV_OriginalBroadcastDate = PROPERTYKEY(Fmtid='4684fe97-8765-4842-9c13-f006447b178c', Pid=100)
PKEY_RecordedTV_ProgramDescription = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=3)
PKEY_RecordedTV_RecordingTime = PROPERTYKEY(Fmtid='a5477f61-7a82-4eca-9dde-98b69b2479b3', Pid=100)
PKEY_RecordedTV_StationCallSign = PROPERTYKEY(Fmtid='6d748de2-8d38-4cc3-ac60-f009b057c557', Pid=5)
PKEY_RecordedTV_StationName = PROPERTYKEY(Fmtid='1b5439e7-eba1-4af8-bdd7-7af1d4549493', Pid=100)
PKEY_Search_AutoSummary = PROPERTYKEY(Fmtid='560c36c0-503a-11cf-baa1-00004c752a9a', Pid=2)
PKEY_Search_ContainerHash = PROPERTYKEY(Fmtid='bceee283-35df-4d53-826a-f36a3eefc6be', Pid=100)
PKEY_Search_Contents = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=19)
PKEY_Search_EntryID = PROPERTYKEY(Fmtid='49691c90-7e17-101a-a91c-08002b2ecda9', Pid=5)
PKEY_Search_ExtendedProperties = PROPERTYKEY(Fmtid='7b03b546-fa4f-4a52-a2fe-03d5311e5865', Pid=100)
PKEY_Search_GatherTime = PROPERTYKEY(Fmtid='0b63e350-9ccc-11d0-bcdb-00805fccce04', Pid=8)
PKEY_Search_HitCount = PROPERTYKEY(Fmtid='49691c90-7e17-101a-a91c-08002b2ecda9', Pid=4)
PKEY_Search_IsClosedDirectory = PROPERTYKEY(Fmtid='0b63e343-9ccc-11d0-bcdb-00805fccce04', Pid=23)
PKEY_Search_IsFullyContained = PROPERTYKEY(Fmtid='0b63e343-9ccc-11d0-bcdb-00805fccce04', Pid=24)
PKEY_Search_QueryFocusedSummary = PROPERTYKEY(Fmtid='560c36c0-503a-11cf-baa1-00004c752a9a', Pid=3)
PKEY_Search_QueryFocusedSummaryWithFallback = PROPERTYKEY(Fmtid='560c36c0-503a-11cf-baa1-00004c752a9a', Pid=4)
PKEY_Search_QueryPropertyHits = PROPERTYKEY(Fmtid='49691c90-7e17-101a-a91c-08002b2ecda9', Pid=21)
PKEY_Search_Rank = PROPERTYKEY(Fmtid='49691c90-7e17-101a-a91c-08002b2ecda9', Pid=3)
PKEY_Search_Store = PROPERTYKEY(Fmtid='a06992b3-8caf-4ed7-a547-b259e32ac9fc', Pid=100)
PKEY_Search_UrlToIndex = PROPERTYKEY(Fmtid='0b63e343-9ccc-11d0-bcdb-00805fccce04', Pid=2)
PKEY_Search_UrlToIndexWithModificationTime = PROPERTYKEY(Fmtid='0b63e343-9ccc-11d0-bcdb-00805fccce04', Pid=12)
PKEY_Supplemental_Album = PROPERTYKEY(Fmtid='0c73b141-39d6-4653-a683-cab291eaf95b', Pid=6)
PKEY_Supplemental_AlbumID = PROPERTYKEY(Fmtid='0c73b141-39d6-4653-a683-cab291eaf95b', Pid=2)
PKEY_Supplemental_Location = PROPERTYKEY(Fmtid='0c73b141-39d6-4653-a683-cab291eaf95b', Pid=5)
PKEY_Supplemental_Person = PROPERTYKEY(Fmtid='0c73b141-39d6-4653-a683-cab291eaf95b', Pid=7)
PKEY_Supplemental_ResourceId = PROPERTYKEY(Fmtid='0c73b141-39d6-4653-a683-cab291eaf95b', Pid=3)
PKEY_Supplemental_Tag = PROPERTYKEY(Fmtid='0c73b141-39d6-4653-a683-cab291eaf95b', Pid=4)
PKEY_DescriptionID = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=2)
PKEY_InternalName = PROPERTYKEY(Fmtid='0cef7d53-fa64-11d1-a203-0000f81fedee', Pid=5)
PKEY_LibraryLocationsCount = PROPERTYKEY(Fmtid='908696c7-8f87-44f2-80ed-a8c1c6894575', Pid=2)
PKEY_Link_TargetSFGAOFlagsStrings = PROPERTYKEY(Fmtid='d6942081-d53b-443d-ad47-5e059d9cd27a', Pid=3)
PKEY_Link_TargetUrl = PROPERTYKEY(Fmtid='5cbf2787-48cf-4208-b90e-ee5e5d420294', Pid=2)
PKEY_NamespaceCLSID = PROPERTYKEY(Fmtid='28636aa6-953d-11d2-b5d6-00c04fd918d0', Pid=6)
PKEY_Shell_SFGAOFlagsStrings = PROPERTYKEY(Fmtid='d6942081-d53b-443d-ad47-5e059d9cd27a', Pid=2)
PKEY_StatusBarSelectedItemCount = PROPERTYKEY(Fmtid='26dc287c-6e3d-4bd3-b2b0-6a26ba2e346d', Pid=3)
PKEY_StatusBarViewItemCount = PROPERTYKEY(Fmtid='26dc287c-6e3d-4bd3-b2b0-6a26ba2e346d', Pid=2)
PKEY_AppUserModel_ExcludeFromShowInNewInstall = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=8)
PKEY_AppUserModel_ID = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=5)
PKEY_AppUserModel_IsDestListSeparator = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=6)
PKEY_AppUserModel_IsDualMode = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=11)
PKEY_AppUserModel_PreventPinning = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=9)
PKEY_AppUserModel_RelaunchCommand = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=2)
PKEY_AppUserModel_RelaunchDisplayNameResource = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=4)
PKEY_AppUserModel_RelaunchIconResource = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=3)
PKEY_AppUserModel_SettingsCommand = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=38)
PKEY_AppUserModel_StartPinOption = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=12)
APPUSERMODEL_STARTPINOPTION_DEFAULT = 0
APPUSERMODEL_STARTPINOPTION_NOPINONINSTALL = 1
APPUSERMODEL_STARTPINOPTION_USERPINNED = 2
PKEY_AppUserModel_ToastActivatorCLSID = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=26)
PKEY_AppUserModel_UninstallCommand = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=37)
PKEY_AppUserModel_VisualElementsManifestHintPath = PROPERTYKEY(Fmtid='9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3', Pid=31)
PKEY_EdgeGesture_DisableTouchWhenFullscreen = PROPERTYKEY(Fmtid='32ce38b2-2c9a-41b1-9bc5-b3784394aa44', Pid=2)
PKEY_Software_DateLastUsed = PROPERTYKEY(Fmtid='841e4f90-ff59-4d16-8947-e81bbffab36d', Pid=16)
PKEY_Software_ProductName = PROPERTYKEY(Fmtid='0cef7d53-fa64-11d1-a203-0000f81fedee', Pid=7)
PKEY_Sync_Comments = PROPERTYKEY(Fmtid='7bd5533e-af15-44db-b8c8-bd6624e1d032', Pid=13)
PKEY_Sync_ConflictDescription = PROPERTYKEY(Fmtid='ce50c159-2fb8-41fd-be68-d3e042e274bc', Pid=4)
PKEY_Sync_ConflictFirstLocation = PROPERTYKEY(Fmtid='ce50c159-2fb8-41fd-be68-d3e042e274bc', Pid=6)
PKEY_Sync_ConflictSecondLocation = PROPERTYKEY(Fmtid='ce50c159-2fb8-41fd-be68-d3e042e274bc', Pid=7)
PKEY_Sync_HandlerCollectionID = PROPERTYKEY(Fmtid='7bd5533e-af15-44db-b8c8-bd6624e1d032', Pid=2)
PKEY_Sync_HandlerID = PROPERTYKEY(Fmtid='7bd5533e-af15-44db-b8c8-bd6624e1d032', Pid=3)
PKEY_Sync_HandlerName = PROPERTYKEY(Fmtid='ce50c159-2fb8-41fd-be68-d3e042e274bc', Pid=2)
PKEY_Sync_HandlerType = PROPERTYKEY(Fmtid='7bd5533e-af15-44db-b8c8-bd6624e1d032', Pid=8)
SYNC_HANDLERTYPE_OTHER = 0
SYNC_HANDLERTYPE_PROGRAMS = 1
SYNC_HANDLERTYPE_DEVICES = 2
SYNC_HANDLERTYPE_FOLDERS = 3
SYNC_HANDLERTYPE_WEBSERVICES = 4
SYNC_HANDLERTYPE_COMPUTERS = 5
PKEY_Sync_HandlerTypeLabel = PROPERTYKEY(Fmtid='7bd5533e-af15-44db-b8c8-bd6624e1d032', Pid=9)
PKEY_Sync_ItemID = PROPERTYKEY(Fmtid='7bd5533e-af15-44db-b8c8-bd6624e1d032', Pid=6)
PKEY_Sync_ItemName = PROPERTYKEY(Fmtid='ce50c159-2fb8-41fd-be68-d3e042e274bc', Pid=3)
PKEY_Sync_ProgressPercentage = PROPERTYKEY(Fmtid='7bd5533e-af15-44db-b8c8-bd6624e1d032', Pid=23)
PKEY_Sync_State = PROPERTYKEY(Fmtid='7bd5533e-af15-44db-b8c8-bd6624e1d032', Pid=24)
SYNC_STATE_NOTSETUP = 0
SYNC_STATE_SYNCNOTRUN = 1
SYNC_STATE_IDLE = 2
SYNC_STATE_ERROR = 3
SYNC_STATE_PENDING = 4
SYNC_STATE_SYNCING = 5
PKEY_Sync_Status = PROPERTYKEY(Fmtid='7bd5533e-af15-44db-b8c8-bd6624e1d032', Pid=10)
PKEY_Task_BillingInformation = PROPERTYKEY(Fmtid='d37d52c6-261c-4303-82b3-08b926ac6f12', Pid=100)
PKEY_Task_CompletionStatus = PROPERTYKEY(Fmtid='084d8a0a-e6d5-40de-bf1f-c8820e7c877c', Pid=100)
PKEY_Task_Owner = PROPERTYKEY(Fmtid='08c7cc5f-60f2-4494-ad75-55e3e0b5add0', Pid=100)
PKEY_Video_Compression = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=10)
PKEY_Video_Director = PROPERTYKEY(Fmtid='64440492-4c8b-11d1-8b70-080036b11a03', Pid=20)
PKEY_Video_EncodingBitrate = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=8)
PKEY_Video_FourCC = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=44)
PKEY_Video_FrameHeight = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=4)
PKEY_Video_FrameRate = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=6)
PKEY_Video_FrameWidth = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=3)
PKEY_Video_HorizontalAspectRatio = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=42)
PKEY_Video_IsSpherical = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=100)
PKEY_Video_IsStereo = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=98)
PKEY_Video_Orientation = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=99)
PKEY_Video_SampleSize = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=9)
PKEY_Video_StreamName = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=2)
PKEY_Video_StreamNumber = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=11)
PKEY_Video_TotalBitrate = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=43)
PKEY_Video_TranscodedForSync = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=46)
PKEY_Video_VerticalAspectRatio = PROPERTYKEY(Fmtid='64440491-4c8b-11d1-8b70-080036b11a03', Pid=45)
PKEY_Volume_FileSystem = PROPERTYKEY(Fmtid='9b174b35-40ff-11d2-a27e-00c04fc30871', Pid=4)
PKEY_Volume_IsMappedDrive = PROPERTYKEY(Fmtid='149c0b69-2c2d-48fc-808f-d318d78c4636', Pid=2)
PKEY_Volume_IsRoot = PROPERTYKEY(Fmtid='9b174b35-40ff-11d2-a27e-00c04fc30871', Pid=10)
ACT_AUTHORIZE_ON_RESUME = 1
ACT_AUTHORIZE_ON_SESSION_UNLOCK = 2
ACT_UNAUTHORIZE_ON_SUSPEND = 1
ACT_UNAUTHORIZE_ON_SESSION_LOCK = 2
ES_RESERVED_COM_ERROR_START = 0
ES_RESERVED_COM_ERROR_END = 511
ES_GENERAL_ERROR_START = 512
ES_GENERAL_ERROR_END = 1023
ES_AUTHN_ERROR_START = 1024
ES_AUTHN_ERROR_END = 1279
ES_RESERVED_SILO_ERROR_START = 1280
ES_RESERVED_SILO_ERROR_END = 4095
ES_PW_SILO_ERROR_START = 4352
ES_PW_SILO_ERROR_END = 4607
ES_RESERVED_SILO_SPECIFIC_ERROR_START = 4608
ES_RESERVED_SILO_SPECIFIC_ERROR_END = 49151
ES_VENDOR_ERROR_START = 49152
ES_VENDOR_ERROR_END = 65535
FACILITY_ENHANCED_STORAGE = 4
def _define_ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION_head():
    class ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION(Structure):
        pass
    return ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION
def _define_ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION():
    ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION = win32more.Storage.EnhancedStorage.ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION_head
    ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION._fields_ = [
        ("CurrentAdminFailures", Byte),
        ("CurrentUserFailures", Byte),
        ("TotalUserAuthenticationCount", UInt32),
        ("TotalAdminAuthenticationCount", UInt32),
        ("FipsCompliant", win32more.Foundation.BOOL),
        ("SecurityIDAvailable", win32more.Foundation.BOOL),
        ("InitializeInProgress", win32more.Foundation.BOOL),
        ("ITMSArmed", win32more.Foundation.BOOL),
        ("ITMSArmable", win32more.Foundation.BOOL),
        ("UserCreated", win32more.Foundation.BOOL),
        ("ResetOnPORDefault", win32more.Foundation.BOOL),
        ("ResetOnPORCurrent", win32more.Foundation.BOOL),
        ("MaxAdminFailures", Byte),
        ("MaxUserFailures", Byte),
        ("TimeToCompleteInitialization", UInt32),
        ("TimeRemainingToCompleteInitialization", UInt32),
        ("MinTimeToAuthenticate", UInt32),
        ("MaxAdminPasswordSize", Byte),
        ("MinAdminPasswordSize", Byte),
        ("MaxAdminHintSize", Byte),
        ("MaxUserPasswordSize", Byte),
        ("MinUserPasswordSize", Byte),
        ("MaxUserHintSize", Byte),
        ("MaxUserNameSize", Byte),
        ("MaxSiloNameSize", Byte),
        ("MaxChallengeSize", UInt16),
    ]
    return ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION
EnumEnhancedStorageACT = Guid('fe841493-835c-4fa3-b6cc-b4b2d4719848')
EnhancedStorageACT = Guid('af076a15-2ece-4ad4-bb21-29f040e176d8')
EnhancedStorageSilo = Guid('cb25220c-76c7-4fee-842b-f3383cd022bc')
EnhancedStorageSiloAction = Guid('886d29dd-b506-466b-9fbf-b44ff383fb3f')
def _define_ACT_AUTHORIZATION_STATE_head():
    class ACT_AUTHORIZATION_STATE(Structure):
        pass
    return ACT_AUTHORIZATION_STATE
def _define_ACT_AUTHORIZATION_STATE():
    ACT_AUTHORIZATION_STATE = win32more.Storage.EnhancedStorage.ACT_AUTHORIZATION_STATE_head
    ACT_AUTHORIZATION_STATE._fields_ = [
        ("ulState", UInt32),
    ]
    return ACT_AUTHORIZATION_STATE
def _define_SILO_INFO_head():
    class SILO_INFO(Structure):
        pass
    return SILO_INFO
def _define_SILO_INFO():
    SILO_INFO = win32more.Storage.EnhancedStorage.SILO_INFO_head
    SILO_INFO._fields_ = [
        ("ulSTID", UInt32),
        ("SpecificationMajor", Byte),
        ("SpecificationMinor", Byte),
        ("ImplementationMajor", Byte),
        ("ImplementationMinor", Byte),
        ("type", Byte),
        ("capabilities", Byte),
    ]
    return SILO_INFO
ACT_AUTHORIZATION_STATE_VALUE = Int32
ACT_UNAUTHORIZED = 0
ACT_AUTHORIZED = 1
def _define_IEnumEnhancedStorageACT_head():
    class IEnumEnhancedStorageACT(win32more.System.Com.IUnknown_head):
        Guid = Guid('09b224bd-1335-4631-a7ff-cfd3a92646d7')
    return IEnumEnhancedStorageACT
def _define_IEnumEnhancedStorageACT():
    IEnumEnhancedStorageACT = win32more.Storage.EnhancedStorage.IEnumEnhancedStorageACT_head
    IEnumEnhancedStorageACT.GetACTs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Storage.EnhancedStorage.IEnhancedStorageACT_head)),POINTER(UInt32), use_last_error=False)(3, 'GetACTs', ((1, 'pppIEnhancedStorageACTs'),(1, 'pcEnhancedStorageACTs'),)))
    IEnumEnhancedStorageACT.GetMatchingACT = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.EnhancedStorage.IEnhancedStorageACT_head), use_last_error=False)(4, 'GetMatchingACT', ((1, 'szVolume'),(1, 'ppIEnhancedStorageACT'),)))
    win32more.System.Com.IUnknown
    return IEnumEnhancedStorageACT
def _define_IEnhancedStorageACT_head():
    class IEnhancedStorageACT(win32more.System.Com.IUnknown_head):
        Guid = Guid('6e7781f4-e0f2-4239-b976-a01abab52930')
    return IEnhancedStorageACT
def _define_IEnhancedStorageACT():
    IEnhancedStorageACT = win32more.Storage.EnhancedStorage.IEnhancedStorageACT_head
    IEnhancedStorageACT.Authorize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(3, 'Authorize', ((1, 'hwndParent'),(1, 'dwFlags'),)))
    IEnhancedStorageACT.Unauthorize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Unauthorize', ()))
    IEnhancedStorageACT.GetAuthorizationState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.EnhancedStorage.ACT_AUTHORIZATION_STATE_head), use_last_error=False)(5, 'GetAuthorizationState', ((1, 'pState'),)))
    IEnhancedStorageACT.GetMatchingVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetMatchingVolume', ((1, 'ppwszVolume'),)))
    IEnhancedStorageACT.GetUniqueIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetUniqueIdentity', ((1, 'ppwszIdentity'),)))
    IEnhancedStorageACT.GetSilos = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Storage.EnhancedStorage.IEnhancedStorageSilo_head)),POINTER(UInt32), use_last_error=False)(8, 'GetSilos', ((1, 'pppIEnhancedStorageSilos'),(1, 'pcEnhancedStorageSilos'),)))
    win32more.System.Com.IUnknown
    return IEnhancedStorageACT
def _define_IEnhancedStorageACT2_head():
    class IEnhancedStorageACT2(win32more.Storage.EnhancedStorage.IEnhancedStorageACT_head):
        Guid = Guid('4da57d2e-8eb3-41f6-a07e-98b52b88242b')
    return IEnhancedStorageACT2
def _define_IEnhancedStorageACT2():
    IEnhancedStorageACT2 = win32more.Storage.EnhancedStorage.IEnhancedStorageACT2_head
    IEnhancedStorageACT2.GetDeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(9, 'GetDeviceName', ((1, 'ppwszDeviceName'),)))
    IEnhancedStorageACT2.IsDeviceRemovable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'IsDeviceRemovable', ((1, 'pIsDeviceRemovable'),)))
    win32more.Storage.EnhancedStorage.IEnhancedStorageACT
    return IEnhancedStorageACT2
def _define_IEnhancedStorageACT3_head():
    class IEnhancedStorageACT3(win32more.Storage.EnhancedStorage.IEnhancedStorageACT2_head):
        Guid = Guid('022150a1-113d-11df-bb61-001aa01bbc58')
    return IEnhancedStorageACT3
def _define_IEnhancedStorageACT3():
    IEnhancedStorageACT3 = win32more.Storage.EnhancedStorage.IEnhancedStorageACT3_head
    IEnhancedStorageACT3.UnauthorizeEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'UnauthorizeEx', ((1, 'dwFlags'),)))
    IEnhancedStorageACT3.IsQueueFrozen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'IsQueueFrozen', ((1, 'pIsQueueFrozen'),)))
    IEnhancedStorageACT3.GetShellExtSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'GetShellExtSupport', ((1, 'pShellExtSupport'),)))
    win32more.Storage.EnhancedStorage.IEnhancedStorageACT2
    return IEnhancedStorageACT3
def _define_IEnhancedStorageSilo_head():
    class IEnhancedStorageSilo(win32more.System.Com.IUnknown_head):
        Guid = Guid('5aef78c6-2242-4703-bf49-44b29357a359')
    return IEnhancedStorageSilo
def _define_IEnhancedStorageSilo():
    IEnhancedStorageSilo = win32more.Storage.EnhancedStorage.IEnhancedStorageSilo_head
    IEnhancedStorageSilo.GetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.EnhancedStorage.SILO_INFO_head), use_last_error=False)(3, 'GetInfo', ((1, 'pSiloInfo'),)))
    IEnhancedStorageSilo.GetActions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Storage.EnhancedStorage.IEnhancedStorageSiloAction_head)),POINTER(UInt32), use_last_error=False)(4, 'GetActions', ((1, 'pppIEnhancedStorageSiloActions'),(1, 'pcEnhancedStorageSiloActions'),)))
    IEnhancedStorageSilo.SendCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(Byte),UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(5, 'SendCommand', ((1, 'Command'),(1, 'pbCommandBuffer'),(1, 'cbCommandBuffer'),(1, 'pbResponseBuffer'),(1, 'pcbResponseBuffer'),)))
    IEnhancedStorageSilo.GetPortableDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevice_head), use_last_error=False)(6, 'GetPortableDevice', ((1, 'ppIPortableDevice'),)))
    IEnhancedStorageSilo.GetDevicePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetDevicePath', ((1, 'ppwszSiloDevicePath'),)))
    win32more.System.Com.IUnknown
    return IEnhancedStorageSilo
def _define_IEnhancedStorageSiloAction_head():
    class IEnhancedStorageSiloAction(win32more.System.Com.IUnknown_head):
        Guid = Guid('b6f7f311-206f-4ff8-9c4b-27efee77a86f')
    return IEnhancedStorageSiloAction
def _define_IEnhancedStorageSiloAction():
    IEnhancedStorageSiloAction = win32more.Storage.EnhancedStorage.IEnhancedStorageSiloAction_head
    IEnhancedStorageSiloAction.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetName', ((1, 'ppwszActionName'),)))
    IEnhancedStorageSiloAction.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetDescription', ((1, 'ppwszActionDescription'),)))
    IEnhancedStorageSiloAction.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Invoke', ()))
    win32more.System.Com.IUnknown
    return IEnhancedStorageSiloAction
__all__ = [
    "GUID_DEVINTERFACE_ENHANCED_STORAGE_SILO",
    "WPD_CATEGORY_ENHANCED_STORAGE",
    "ENHANCED_STORAGE_COMMAND_SILO_IS_AUTHENTICATION_SILO",
    "ENHANCED_STORAGE_COMMAND_SILO_GET_AUTHENTICATION_STATE",
    "ENHANCED_STORAGE_COMMAND_SILO_ENUMERATE_SILOS",
    "ENHANCED_STORAGE_COMMAND_CERT_HOST_CERTIFICATE_AUTHENTICATION",
    "ENHANCED_STORAGE_COMMAND_CERT_DEVICE_CERTIFICATE_AUTHENTICATION",
    "ENHANCED_STORAGE_COMMAND_CERT_ADMIN_CERTIFICATE_AUTHENTICATION",
    "ENHANCED_STORAGE_COMMAND_CERT_INITIALIZE_TO_MANUFACTURER_STATE",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE_COUNT",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE",
    "ENHANCED_STORAGE_COMMAND_CERT_SET_CERTIFICATE",
    "ENHANCED_STORAGE_COMMAND_CERT_CREATE_CERTIFICATE_REQUEST",
    "ENHANCED_STORAGE_COMMAND_CERT_UNAUTHENTICATION",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITY",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITIES",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_ACT_FRIENDLY_NAME",
    "ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_GUID",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_AUTHORIZE_ACT_ACCESS",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_UNAUTHORIZE_ACT_ACCESS",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_QUERY_INFORMATION",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_CONFIG_ADMINISTRATOR",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_CREATE_USER",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_DELETE_USER",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_CHANGE_PASSWORD",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_INITIALIZE_USER_PASSWORD",
    "ENHANCED_STORAGE_COMMAND_PASSWORD_START_INITIALIZE_TO_MANUFACTURER_STATE",
    "ENHANCED_STORAGE_PROPERTY_AUTHENTICATION_STATE",
    "ENHANCED_STORAGE_AUTHN_STATE_UNKNOWN",
    "ENHANCED_STORAGE_AUTHN_STATE_NO_AUTHENTICATION_REQUIRED",
    "ENHANCED_STORAGE_AUTHN_STATE_NOT_AUTHENTICATED",
    "ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATED",
    "ENHANCED_STORAGE_AUTHN_STATE_AUTHENTICATION_DENIED",
    "ENHANCED_STORAGE_AUTHN_STATE_DEVICE_ERROR",
    "ENHANCED_STORAGE_PROPERTY_IS_AUTHENTICATION_SILO",
    "ENHANCED_STORAGE_PROPERTY_TEMPORARY_UNAUTHENTICATION",
    "ENHANCED_STORAGE_PROPERTY_MAX_AUTH_FAILURES",
    "ENHANCED_STORAGE_PROPERTY_PASSWORD",
    "ENHANCED_STORAGE_PROPERTY_OLD_PASSWORD",
    "ENHANCED_STORAGE_PROPERTY_PASSWORD_INDICATOR",
    "ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD_INDICATOR",
    "ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD",
    "ENHANCED_STORAGE_PROPERTY_USER_HINT",
    "ENHANCED_STORAGE_PROPERTY_USER_NAME",
    "ENHANCED_STORAGE_PROPERTY_ADMIN_HINT",
    "ENHANCED_STORAGE_PROPERTY_SILO_NAME",
    "ENHANCED_STORAGE_PROPERTY_SILO_FRIENDLYNAME_SPECIFIED",
    "ENHANCED_STORAGE_PROPERTY_PASSWORD_SILO_INFO",
    "ENHANCED_STORAGE_PROPERTY_SECURITY_IDENTIFIER",
    "ENHANCED_STORAGE_PROPERTY_QUERY_SILO_TYPE",
    "ENHANCED_STORAGE_PROPERTY_QUERY_SILO_RESULTS",
    "ENHANCED_STORAGE_PROPERTY_MAX_CERTIFICATE_COUNT",
    "ENHANCED_STORAGE_PROPERTY_STORED_CERTIFICATE_COUNT",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_INDEX",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_TYPE",
    "CERT_TYPE_EMPTY",
    "CERT_TYPE_ASCm",
    "CERT_TYPE_PCp",
    "CERT_TYPE_ASCh",
    "CERT_TYPE_HCh",
    "CERT_TYPE_SIGNER",
    "ENHANCED_STORAGE_PROPERTY_VALIDATION_POLICY",
    "CERT_VALIDATION_POLICY_RESERVED",
    "CERT_VALIDATION_POLICY_NONE",
    "CERT_VALIDATION_POLICY_BASIC",
    "CERT_VALIDATION_POLICY_EXTENDED",
    "ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_INDEX",
    "ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_OF_TYPE_INDEX",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_LENGTH",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_REQUEST",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_CAPABILITY_TYPE",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITY",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITIES",
    "CERT_CAPABILITY_HASH_ALG",
    "CERT_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY",
    "CERT_CAPABILITY_SIGNATURE_ALG",
    "CERT_CAPABILITY_CERTIFICATE_SUPPORT",
    "CERT_CAPABILITY_OPTIONAL_FEATURES",
    "CERT_MAX_CAPABILITY",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_ACT_FRIENDLY_NAME",
    "ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_GUID",
    "ENHANCED_STORAGE_PROPERTY_SIGNER_CERTIFICATE_INDEX",
    "ENHANCED_STORAGE_CAPABILITY_HASH_ALGS",
    "ENHANCED_STORAGE_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY",
    "ENHANCED_STORAGE_CAPABILITY_SIGNING_ALGS",
    "ENHANCED_STORAGE_CAPABILITY_RENDER_USER_DATA_UNUSABLE",
    "ENHANCED_STORAGE_CAPABILITY_CERTIFICATE_EXTENSION_PARSING",
    "PKEY_Address_Country",
    "PKEY_Address_CountryCode",
    "PKEY_Address_Region",
    "PKEY_Address_RegionCode",
    "PKEY_Address_Town",
    "PKEY_Audio_ChannelCount",
    "AUDIO_CHANNELCOUNT_MONO",
    "AUDIO_CHANNELCOUNT_STEREO",
    "PKEY_Audio_Compression",
    "PKEY_Audio_EncodingBitrate",
    "PKEY_Audio_Format",
    "PKEY_Audio_IsVariableBitRate",
    "PKEY_Audio_PeakValue",
    "PKEY_Audio_SampleRate",
    "PKEY_Audio_SampleSize",
    "PKEY_Audio_StreamName",
    "PKEY_Audio_StreamNumber",
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
    "PKEY_Contact_BusinessAddressPostalCode",
    "PKEY_Contact_BusinessAddressPostOfficeBox",
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
    "PKEY_Contact_HomeAddressPostalCode",
    "PKEY_Contact_HomeAddressPostOfficeBox",
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
    "PKEY_Contact_OtherAddressPostalCode",
    "PKEY_Contact_OtherAddressPostOfficeBox",
    "PKEY_Contact_OtherAddressState",
    "PKEY_Contact_OtherAddressStreet",
    "PKEY_Contact_OtherEmailAddresses",
    "PKEY_Contact_PagerTelephone",
    "PKEY_Contact_PersonalTitle",
    "PKEY_Contact_PhoneNumbersCanonical",
    "PKEY_Contact_Prefix",
    "PKEY_Contact_PrimaryAddressCity",
    "PKEY_Contact_PrimaryAddressCountry",
    "PKEY_Contact_PrimaryAddressPostalCode",
    "PKEY_Contact_PrimaryAddressPostOfficeBox",
    "PKEY_Contact_PrimaryAddressState",
    "PKEY_Contact_PrimaryAddressStreet",
    "PKEY_Contact_PrimaryEmailAddress",
    "PKEY_Contact_PrimaryTelephone",
    "PKEY_Contact_Profession",
    "PKEY_Contact_SpouseName",
    "PKEY_Contact_Suffix",
    "PKEY_Contact_TelexNumber",
    "PKEY_Contact_TTYTDDTelephone",
    "PKEY_Contact_WebPage",
    "PKEY_Contact_Webpage2",
    "PKEY_Contact_Webpage3",
    "PKEY_AcquisitionID",
    "PKEY_ApplicationDefinedProperties",
    "PKEY_ApplicationName",
    "PKEY_AppZoneIdentifier",
    "PKEY_Author",
    "PKEY_CachedFileUpdaterContentIdForConflictResolution",
    "PKEY_CachedFileUpdaterContentIdForStream",
    "PKEY_Capacity",
    "PKEY_Category",
    "PKEY_Comment",
    "PKEY_Company",
    "PKEY_ComputerName",
    "PKEY_ContainedItems",
    "PKEY_ContentId",
    "PKEY_ContentStatus",
    "PKEY_ContentType",
    "PKEY_ContentUri",
    "PKEY_Copyright",
    "PKEY_CreatorAppId",
    "PKEY_CreatorOpenWithUIOptions",
    "CREATOROPENWITHUIOPTION_HIDDEN",
    "CREATOROPENWITHUIOPTION_VISIBLE",
    "PKEY_DataObjectFormat",
    "PKEY_DateAccessed",
    "PKEY_DateAcquired",
    "PKEY_DateArchived",
    "PKEY_DateCompleted",
    "PKEY_DateCreated",
    "PKEY_DateImported",
    "PKEY_DateModified",
    "PKEY_DefaultSaveLocationDisplay",
    "ISDEFAULTSAVE_NONE",
    "ISDEFAULTSAVE_OWNER",
    "ISDEFAULTSAVE_NONOWNER",
    "ISDEFAULTSAVE_BOTH",
    "PKEY_DueDate",
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
    "FILEOFFLINEAVAILABILITYSTATUS_NOTAVAILABLEOFFLINE",
    "FILEOFFLINEAVAILABILITYSTATUS_PARTIAL",
    "FILEOFFLINEAVAILABILITYSTATUS_COMPLETE",
    "FILEOFFLINEAVAILABILITYSTATUS_COMPLETE_PINNED",
    "FILEOFFLINEAVAILABILITYSTATUS_EXCLUDED",
    "FILEOFFLINEAVAILABILITYSTATUS_FOLDER_EMPTY",
    "PKEY_FileOwner",
    "PKEY_FilePlaceholderStatus",
    "PKEY_FileVersion",
    "PKEY_FindData",
    "PKEY_FlagColor",
    "PKEY_FlagColorText",
    "PKEY_FlagStatus",
    "FLAGSTATUS_NOTFLAGGED",
    "FLAGSTATUS_COMPLETED",
    "FLAGSTATUS_FOLLOWUP",
    "PKEY_FlagStatusText",
    "PKEY_FolderKind",
    "PKEY_FolderNameDisplay",
    "PKEY_FreeSpace",
    "PKEY_FullText",
    "PKEY_HighKeywords",
    "PKEY_Identity",
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
    "PKEY_IdentityProvider_Name",
    "PKEY_IdentityProvider_Picture",
    "PKEY_ImageParsingName",
    "PKEY_Importance",
    "IMPORTANCE_LOW_MIN",
    "IMPORTANCE_LOW_SET",
    "IMPORTANCE_LOW_MAX",
    "IMPORTANCE_NORMAL_MIN",
    "IMPORTANCE_NORMAL_SET",
    "IMPORTANCE_NORMAL_MAX",
    "IMPORTANCE_HIGH_MIN",
    "IMPORTANCE_HIGH_SET",
    "IMPORTANCE_HIGH_MAX",
    "PKEY_ImportanceText",
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
    "PKEY_Keywords",
    "PKEY_Kind",
    "PKEY_KindText",
    "PKEY_Language",
    "PKEY_LastSyncError",
    "PKEY_LastSyncWarning",
    "PKEY_LastWriterPackageFamilyName",
    "PKEY_LowKeywords",
    "PKEY_MediumKeywords",
    "PKEY_MileageInformation",
    "PKEY_MIMEType",
    "PKEY_Null",
    "PKEY_OfflineAvailability",
    "OFFLINEAVAILABILITY_NOT_AVAILABLE",
    "OFFLINEAVAILABILITY_AVAILABLE",
    "OFFLINEAVAILABILITY_ALWAYS_AVAILABLE",
    "PKEY_OfflineStatus",
    "OFFLINESTATUS_ONLINE",
    "OFFLINESTATUS_OFFLINE",
    "OFFLINESTATUS_OFFLINE_FORCED",
    "OFFLINESTATUS_OFFLINE_SLOW",
    "OFFLINESTATUS_OFFLINE_ERROR",
    "OFFLINESTATUS_OFFLINE_ITEM_VERSION_CONFLICT",
    "OFFLINESTATUS_OFFLINE_SUSPENDED",
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
    "PKEY_Priority",
    "PKEY_PriorityText",
    "PKEY_Project",
    "PKEY_ProviderItemID",
    "PKEY_Rating",
    "RATING_ONE_STAR_MIN",
    "RATING_ONE_STAR_SET",
    "RATING_ONE_STAR_MAX",
    "RATING_TWO_STARS_MIN",
    "RATING_TWO_STARS_SET",
    "RATING_TWO_STARS_MAX",
    "RATING_THREE_STARS_MIN",
    "RATING_THREE_STARS_SET",
    "RATING_THREE_STARS_MAX",
    "RATING_FOUR_STARS_MIN",
    "RATING_FOUR_STARS_SET",
    "RATING_FOUR_STARS_MAX",
    "RATING_FIVE_STARS_MIN",
    "RATING_FIVE_STARS_SET",
    "RATING_FIVE_STARS_MAX",
    "PKEY_RatingText",
    "PKEY_RemoteConflictingFile",
    "PKEY_Security_AllowedEnterpriseDataProtectionIdentities",
    "PKEY_Security_EncryptionOwners",
    "PKEY_Security_EncryptionOwnersDisplay",
    "PKEY_Sensitivity",
    "PKEY_SensitivityText",
    "PKEY_SFGAOFlags",
    "PKEY_SharedWith",
    "PKEY_ShareUserRating",
    "PKEY_SharingStatus",
    "SHARINGSTATUS_NOTSHARED",
    "SHARINGSTATUS_SHARED",
    "SHARINGSTATUS_PRIVATE",
    "PKEY_Shell_OmitFromView",
    "PKEY_SimpleRating",
    "PKEY_Size",
    "PKEY_SoftwareUsed",
    "PKEY_SourceItem",
    "PKEY_SourcePackageFamilyName",
    "PKEY_StartDate",
    "PKEY_Status",
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
    "STORAGE_PROVIDER_SHARINGSTATUS_NOTSHARED",
    "STORAGE_PROVIDER_SHARINGSTATUS_SHARED",
    "STORAGE_PROVIDER_SHARINGSTATUS_PRIVATE",
    "STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC",
    "STORAGE_PROVIDER_SHARINGSTATUS_SHARED_OWNED",
    "STORAGE_PROVIDER_SHARINGSTATUS_SHARED_COOWNED",
    "STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_OWNED",
    "STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_COOWNED",
    "PKEY_StorageProviderStatus",
    "PKEY_Subject",
    "PKEY_SyncTransferStatus",
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
    "PKEY_VolumeId",
    "PKEY_ZoneIdentifier",
    "PKEY_Device_PrinterURL",
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
    "BLUETOOTH_ADDRESS_TYPE_PUBLIC",
    "BLUETOOTH_ADDRESS_TYPE_RANDOM",
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
    "BLUETOOTH_CACHE_MODE_CACHED",
    "BLUETOOTH_CACHED_MODE_UNCACHED",
    "PKEY_Devices_AepService_Bluetooth_ServiceGuid",
    "PKEY_Devices_AepService_Bluetooth_TargetDevice",
    "PKEY_Devices_AepService_ContainerId",
    "PKEY_Devices_AepService_FriendlyName",
    "PKEY_Devices_AepService_IoT_ServiceInterfaces",
    "PKEY_Devices_AepService_ParentAepIsPaired",
    "PKEY_Devices_AepService_ProtocolId",
    "PKEY_Devices_AepService_ServiceClassId",
    "PKEY_Devices_AepService_ServiceId",
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
    "PKEY_Devices_DeviceCapabilities",
    "PKEY_Devices_DeviceCharacteristics",
    "PKEY_Devices_DeviceDescription1",
    "PKEY_Devices_DeviceDescription2",
    "PKEY_Devices_DeviceHasProblem",
    "PKEY_Devices_DeviceInstanceId",
    "PKEY_Devices_DeviceManufacturer",
    "PKEY_Devices_DevObjectType",
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
    "PKEY_Devices_NetworkedTooltip",
    "PKEY_Devices_NetworkName",
    "PKEY_Devices_NetworkType",
    "PKEY_Devices_NewPictures",
    "PKEY_Devices_Notification",
    "PKEY_Devices_Notifications_LowBattery",
    "PKEY_Devices_Notifications_MissedCall",
    "PKEY_Devices_Notifications_NewMessage",
    "PKEY_Devices_Notifications_NewVoicemail",
    "PKEY_Devices_Notifications_StorageFull",
    "PKEY_Devices_Notifications_StorageFullLinkText",
    "PKEY_Devices_NotificationStore",
    "PKEY_Devices_NotWorkingProperly",
    "PKEY_Devices_Paired",
    "PKEY_Devices_Panel_PanelGroup",
    "PKEY_Devices_Panel_PanelId",
    "PKEY_Devices_Parent",
    "PKEY_Devices_PhoneLineTransportDevice_Connected",
    "PKEY_Devices_PhysicalDeviceLocation",
    "PKEY_Devices_PlaybackPositionPercent",
    "PKEY_Devices_PlaybackState",
    "PLAYBACKSTATE_UNKNOWN",
    "PLAYBACKSTATE_STOPPED",
    "PLAYBACKSTATE_PLAYING",
    "PLAYBACKSTATE_TRANSITIONING",
    "PLAYBACKSTATE_PAUSED",
    "PLAYBACKSTATE_RECORDINGPAUSED",
    "PLAYBACKSTATE_RECORDING",
    "PLAYBACKSTATE_NOMEDIA",
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
    "PKEY_Devices_WiaDeviceType",
    "PKEY_Devices_WiFi_InterfaceGuid",
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
    "PKEY_Devices_WiFiDirectServices_AdvertisementId",
    "PKEY_Devices_WiFiDirectServices_RequestServiceInformation",
    "PKEY_Devices_WiFiDirectServices_ServiceAddress",
    "PKEY_Devices_WiFiDirectServices_ServiceConfigMethods",
    "PKEY_Devices_WiFiDirectServices_ServiceInformation",
    "PKEY_Devices_WiFiDirectServices_ServiceName",
    "PKEY_Devices_WinPhone8CameraFlags",
    "PKEY_Devices_Wwan_InterfaceGuid",
    "PKEY_Storage_Portable",
    "PKEY_Storage_RemovableMedia",
    "PKEY_Storage_SystemCritical",
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
    "PKEY_DRM_DatePlayExpires",
    "PKEY_DRM_DatePlayStarts",
    "PKEY_DRM_Description",
    "PKEY_DRM_IsDisabled",
    "PKEY_DRM_IsProtected",
    "PKEY_DRM_PlayCount",
    "PKEY_GPS_Altitude",
    "PKEY_GPS_AltitudeDenominator",
    "PKEY_GPS_AltitudeNumerator",
    "PKEY_GPS_AltitudeRef",
    "PKEY_GPS_AreaInformation",
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
    "PKEY_GPS_DOP",
    "PKEY_GPS_DOPDenominator",
    "PKEY_GPS_DOPNumerator",
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
    "PKEY_History_VisitCount",
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
    "PKEY_Journal_Contacts",
    "PKEY_Journal_EntryType",
    "PKEY_LayoutPattern_ContentViewModeForBrowse",
    "PKEY_LayoutPattern_ContentViewModeForSearch",
    "PKEY_History_SelectionCount",
    "PKEY_History_TargetUrlHostName",
    "PKEY_Link_Arguments",
    "PKEY_Link_Comment",
    "PKEY_Link_DateVisited",
    "PKEY_Link_Description",
    "PKEY_Link_FeedItemLocalId",
    "PKEY_Link_Status",
    "LINK_STATUS_RESOLVED",
    "LINK_STATUS_BROKEN",
    "PKEY_Link_TargetExtension",
    "PKEY_Link_TargetParsingPath",
    "PKEY_Link_TargetSFGAOFlags",
    "PKEY_Link_TargetUrlHostName",
    "PKEY_Link_TargetUrlPath",
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
    "PKEY_Media_DateEncoded",
    "PKEY_Media_DateReleased",
    "PKEY_Media_DlnaProfileID",
    "PKEY_Media_Duration",
    "PKEY_Media_DVDID",
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
    "PKEY_Media_SubscriptionContentId",
    "PKEY_Media_SubTitle",
    "PKEY_Media_ThumbnailLargePath",
    "PKEY_Media_ThumbnailLargeUri",
    "PKEY_Media_ThumbnailSmallPath",
    "PKEY_Media_ThumbnailSmallUri",
    "PKEY_Media_UniqueFileIdentifier",
    "PKEY_Media_UserNoAutoInfo",
    "PKEY_Media_UserWebUrl",
    "PKEY_Media_Writer",
    "PKEY_Media_Year",
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
    "PKEY_Note_Color",
    "PKEY_Note_ColorText",
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
    "PHOTO_CONTRAST_NORMAL",
    "PHOTO_CONTRAST_SOFT",
    "PHOTO_CONTRAST_HARD",
    "PKEY_Photo_ContrastText",
    "PKEY_Photo_DateTaken",
    "PKEY_Photo_DigitalZoom",
    "PKEY_Photo_DigitalZoomDenominator",
    "PKEY_Photo_DigitalZoomNumerator",
    "PKEY_Photo_Event",
    "PKEY_Photo_EXIFVersion",
    "PKEY_Photo_ExposureBias",
    "PKEY_Photo_ExposureBiasDenominator",
    "PKEY_Photo_ExposureBiasNumerator",
    "PKEY_Photo_ExposureIndex",
    "PKEY_Photo_ExposureIndexDenominator",
    "PKEY_Photo_ExposureIndexNumerator",
    "PKEY_Photo_ExposureProgram",
    "PHOTO_EXPOSUREPROGRAM_UNKNOWN",
    "PHOTO_EXPOSUREPROGRAM_MANUAL",
    "PHOTO_EXPOSUREPROGRAM_NORMAL",
    "PHOTO_EXPOSUREPROGRAM_APERTURE",
    "PHOTO_EXPOSUREPROGRAM_SHUTTER",
    "PHOTO_EXPOSUREPROGRAM_CREATIVE",
    "PHOTO_EXPOSUREPROGRAM_ACTION",
    "PHOTO_EXPOSUREPROGRAM_PORTRAIT",
    "PHOTO_EXPOSUREPROGRAM_LANDSCAPE",
    "PKEY_Photo_ExposureProgramText",
    "PKEY_Photo_ExposureTime",
    "PKEY_Photo_ExposureTimeDenominator",
    "PKEY_Photo_ExposureTimeNumerator",
    "PKEY_Photo_Flash",
    "PHOTO_FLASH_NONE",
    "PHOTO_FLASH_FLASH",
    "PHOTO_FLASH_WITHOUTSTROBE",
    "PHOTO_FLASH_WITHSTROBE",
    "PHOTO_FLASH_FLASH_COMPULSORY",
    "PHOTO_FLASH_FLASH_COMPULSORY_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_COMPULSORY_RETURNLIGHT",
    "PHOTO_FLASH_NONE_COMPULSORY",
    "PHOTO_FLASH_NONE_AUTO",
    "PHOTO_FLASH_FLASH_AUTO",
    "PHOTO_FLASH_FLASH_AUTO_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_AUTO_RETURNLIGHT",
    "PHOTO_FLASH_NOFUNCTION",
    "PHOTO_FLASH_FLASH_REDEYE",
    "PHOTO_FLASH_FLASH_REDEYE_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_REDEYE_RETURNLIGHT",
    "PHOTO_FLASH_FLASH_COMPULSORY_REDEYE",
    "PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_RETURNLIGHT",
    "PHOTO_FLASH_FLASH_AUTO_REDEYE",
    "PHOTO_FLASH_FLASH_AUTO_REDEYE_NORETURNLIGHT",
    "PHOTO_FLASH_FLASH_AUTO_REDEYE_RETURNLIGHT",
    "PKEY_Photo_FlashEnergy",
    "PKEY_Photo_FlashEnergyDenominator",
    "PKEY_Photo_FlashEnergyNumerator",
    "PKEY_Photo_FlashManufacturer",
    "PKEY_Photo_FlashModel",
    "PKEY_Photo_FlashText",
    "PKEY_Photo_FNumber",
    "PKEY_Photo_FNumberDenominator",
    "PKEY_Photo_FNumberNumerator",
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
    "PHOTO_GAINCONTROL_NONE",
    "PHOTO_GAINCONTROL_LOWGAINUP",
    "PHOTO_GAINCONTROL_HIGHGAINUP",
    "PHOTO_GAINCONTROL_LOWGAINDOWN",
    "PHOTO_GAINCONTROL_HIGHGAINDOWN",
    "PKEY_Photo_GainControlDenominator",
    "PKEY_Photo_GainControlNumerator",
    "PKEY_Photo_GainControlText",
    "PKEY_Photo_ISOSpeed",
    "PKEY_Photo_LensManufacturer",
    "PKEY_Photo_LensModel",
    "PKEY_Photo_LightSource",
    "PHOTO_LIGHTSOURCE_UNKNOWN",
    "PHOTO_LIGHTSOURCE_DAYLIGHT",
    "PHOTO_LIGHTSOURCE_FLUORESCENT",
    "PHOTO_LIGHTSOURCE_TUNGSTEN",
    "PHOTO_LIGHTSOURCE_STANDARD_A",
    "PHOTO_LIGHTSOURCE_STANDARD_B",
    "PHOTO_LIGHTSOURCE_STANDARD_C",
    "PHOTO_LIGHTSOURCE_D55",
    "PHOTO_LIGHTSOURCE_D65",
    "PHOTO_LIGHTSOURCE_D75",
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
    "PHOTO_PROGRAMMODE_NOTDEFINED",
    "PHOTO_PROGRAMMODE_MANUAL",
    "PHOTO_PROGRAMMODE_NORMAL",
    "PHOTO_PROGRAMMODE_APERTURE",
    "PHOTO_PROGRAMMODE_SHUTTER",
    "PHOTO_PROGRAMMODE_CREATIVE",
    "PHOTO_PROGRAMMODE_ACTION",
    "PHOTO_PROGRAMMODE_PORTRAIT",
    "PHOTO_PROGRAMMODE_LANDSCAPE",
    "PKEY_Photo_ProgramModeText",
    "PKEY_Photo_RelatedSoundFile",
    "PKEY_Photo_Saturation",
    "PHOTO_SATURATION_NORMAL",
    "PHOTO_SATURATION_LOW",
    "PHOTO_SATURATION_HIGH",
    "PKEY_Photo_SaturationText",
    "PKEY_Photo_Sharpness",
    "PHOTO_SHARPNESS_NORMAL",
    "PHOTO_SHARPNESS_SOFT",
    "PHOTO_SHARPNESS_HARD",
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
    "PHOTO_WHITEBALANCE_AUTO",
    "PHOTO_WHITEBALANCE_MANUAL",
    "PKEY_Photo_WhiteBalanceText",
    "PKEY_PropGroup_Advanced",
    "PKEY_PropGroup_Audio",
    "PKEY_PropGroup_Calendar",
    "PKEY_PropGroup_Camera",
    "PKEY_PropGroup_Contact",
    "PKEY_PropGroup_Content",
    "PKEY_PropGroup_Description",
    "PKEY_PropGroup_FileSystem",
    "PKEY_PropGroup_General",
    "PKEY_PropGroup_GPS",
    "PKEY_PropGroup_Image",
    "PKEY_PropGroup_Media",
    "PKEY_PropGroup_MediaAdvanced",
    "PKEY_PropGroup_Message",
    "PKEY_PropGroup_Music",
    "PKEY_PropGroup_Origin",
    "PKEY_PropGroup_PhotoAdvanced",
    "PKEY_PropGroup_RecordedTV",
    "PKEY_PropGroup_Video",
    "PKEY_InfoTipText",
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
    "PKEY_Supplemental_Album",
    "PKEY_Supplemental_AlbumID",
    "PKEY_Supplemental_Location",
    "PKEY_Supplemental_Person",
    "PKEY_Supplemental_ResourceId",
    "PKEY_Supplemental_Tag",
    "PKEY_DescriptionID",
    "PKEY_InternalName",
    "PKEY_LibraryLocationsCount",
    "PKEY_Link_TargetSFGAOFlagsStrings",
    "PKEY_Link_TargetUrl",
    "PKEY_NamespaceCLSID",
    "PKEY_Shell_SFGAOFlagsStrings",
    "PKEY_StatusBarSelectedItemCount",
    "PKEY_StatusBarViewItemCount",
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
    "APPUSERMODEL_STARTPINOPTION_DEFAULT",
    "APPUSERMODEL_STARTPINOPTION_NOPINONINSTALL",
    "APPUSERMODEL_STARTPINOPTION_USERPINNED",
    "PKEY_AppUserModel_ToastActivatorCLSID",
    "PKEY_AppUserModel_UninstallCommand",
    "PKEY_AppUserModel_VisualElementsManifestHintPath",
    "PKEY_EdgeGesture_DisableTouchWhenFullscreen",
    "PKEY_Software_DateLastUsed",
    "PKEY_Software_ProductName",
    "PKEY_Sync_Comments",
    "PKEY_Sync_ConflictDescription",
    "PKEY_Sync_ConflictFirstLocation",
    "PKEY_Sync_ConflictSecondLocation",
    "PKEY_Sync_HandlerCollectionID",
    "PKEY_Sync_HandlerID",
    "PKEY_Sync_HandlerName",
    "PKEY_Sync_HandlerType",
    "SYNC_HANDLERTYPE_OTHER",
    "SYNC_HANDLERTYPE_PROGRAMS",
    "SYNC_HANDLERTYPE_DEVICES",
    "SYNC_HANDLERTYPE_FOLDERS",
    "SYNC_HANDLERTYPE_WEBSERVICES",
    "SYNC_HANDLERTYPE_COMPUTERS",
    "PKEY_Sync_HandlerTypeLabel",
    "PKEY_Sync_ItemID",
    "PKEY_Sync_ItemName",
    "PKEY_Sync_ProgressPercentage",
    "PKEY_Sync_State",
    "SYNC_STATE_NOTSETUP",
    "SYNC_STATE_SYNCNOTRUN",
    "SYNC_STATE_IDLE",
    "SYNC_STATE_ERROR",
    "SYNC_STATE_PENDING",
    "SYNC_STATE_SYNCING",
    "PKEY_Sync_Status",
    "PKEY_Task_BillingInformation",
    "PKEY_Task_CompletionStatus",
    "PKEY_Task_Owner",
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
    "PKEY_Volume_FileSystem",
    "PKEY_Volume_IsMappedDrive",
    "PKEY_Volume_IsRoot",
    "ACT_AUTHORIZE_ON_RESUME",
    "ACT_AUTHORIZE_ON_SESSION_UNLOCK",
    "ACT_UNAUTHORIZE_ON_SUSPEND",
    "ACT_UNAUTHORIZE_ON_SESSION_LOCK",
    "ES_RESERVED_COM_ERROR_START",
    "ES_RESERVED_COM_ERROR_END",
    "ES_GENERAL_ERROR_START",
    "ES_GENERAL_ERROR_END",
    "ES_AUTHN_ERROR_START",
    "ES_AUTHN_ERROR_END",
    "ES_RESERVED_SILO_ERROR_START",
    "ES_RESERVED_SILO_ERROR_END",
    "ES_PW_SILO_ERROR_START",
    "ES_PW_SILO_ERROR_END",
    "ES_RESERVED_SILO_SPECIFIC_ERROR_START",
    "ES_RESERVED_SILO_SPECIFIC_ERROR_END",
    "ES_VENDOR_ERROR_START",
    "ES_VENDOR_ERROR_END",
    "FACILITY_ENHANCED_STORAGE",
    "ENHANCED_STORAGE_PASSWORD_SILO_INFORMATION",
    "EnumEnhancedStorageACT",
    "EnhancedStorageACT",
    "EnhancedStorageSilo",
    "EnhancedStorageSiloAction",
    "ACT_AUTHORIZATION_STATE",
    "SILO_INFO",
    "ACT_AUTHORIZATION_STATE_VALUE",
    "ACT_UNAUTHORIZED",
    "ACT_AUTHORIZED",
    "IEnumEnhancedStorageACT",
    "IEnhancedStorageACT",
    "IEnhancedStorageACT2",
    "IEnhancedStorageACT3",
    "IEnhancedStorageSilo",
    "IEnhancedStorageSiloAction",
]
