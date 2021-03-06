from win32more import *
import win32more.Devices.PortableDevices
import win32more.Devices.Properties
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.StructuredStorage
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
DEVPKEY_MTPBTH_IsConnected = PROPERTYKEY(Fmtid='ea1237fa-589d-4472-84e4-0abe36fd62ef', Pid=2)
GUID_DEVINTERFACE_WPD = '6ac27878-a6fa-4155-ba85-f98f491d4f33'
GUID_DEVINTERFACE_WPD_PRIVATE = 'ba0c718f-4ded-49b7-bdd3-fabe28661211'
GUID_DEVINTERFACE_WPD_SERVICE = '9ef44f80-3d64-4246-a6aa-206f328d1edc'
WPD_CONTROL_FUNCTION_GENERIC_MESSAGE = 66
IOCTL_WPD_MESSAGE_READWRITE_ACCESS = 4243720
IOCTL_WPD_MESSAGE_READ_ACCESS = 4210952
FACILITY_WPD = 42
E_WPD_DEVICE_ALREADY_OPENED = -2144731135
E_WPD_DEVICE_NOT_OPEN = -2144731134
E_WPD_OBJECT_ALREADY_ATTACHED_TO_DEVICE = -2144731133
E_WPD_OBJECT_NOT_ATTACHED_TO_DEVICE = -2144731132
E_WPD_OBJECT_NOT_COMMITED = -2144731131
E_WPD_DEVICE_IS_HUNG = -2144731130
E_WPD_SMS_INVALID_RECIPIENT = -2144731036
E_WPD_SMS_INVALID_MESSAGE_BODY = -2144731035
E_WPD_SMS_SERVICE_UNAVAILABLE = -2144731034
E_WPD_SERVICE_ALREADY_OPENED = -2144730936
E_WPD_SERVICE_NOT_OPEN = -2144730935
E_WPD_OBJECT_ALREADY_ATTACHED_TO_SERVICE = -2144730934
E_WPD_OBJECT_NOT_ATTACHED_TO_SERVICE = -2144730933
E_WPD_SERVICE_BAD_PARAMETER_ORDER = -2144730932
WPD_EVENT_NOTIFICATION = '2ba2e40a-6b4c-4295-bb43-26322b99aeb2'
WPD_EVENT_OBJECT_ADDED = 'a726da95-e207-4b02-8d44-bef2e86cbffc'
WPD_EVENT_OBJECT_REMOVED = 'be82ab88-a52c-4823-96e5-d0272671fc38'
WPD_EVENT_OBJECT_UPDATED = '1445a759-2e01-485d-9f27-ff07dae697ab'
WPD_EVENT_DEVICE_RESET = '7755cf53-c1ed-44f3-b5a2-451e2c376b27'
WPD_EVENT_DEVICE_CAPABILITIES_UPDATED = '36885aa1-cd54-4daa-b3d0-afb3e03f5999'
WPD_EVENT_STORAGE_FORMAT = '3782616b-22bc-4474-a251-3070f8d38857'
WPD_EVENT_OBJECT_TRANSFER_REQUESTED = '8d16a0a1-f2c6-41da-8f19-5e53721adbf2'
WPD_EVENT_DEVICE_REMOVED = 'e4cbca1b-6918-48b9-85ee-02be7c850af9'
WPD_EVENT_SERVICE_METHOD_COMPLETE = '8a33f5f8-0acc-4d9b-9cc4-112d353b86ca'
WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT = '99ed0160-17ff-4c44-9d98-1d7a6f941921'
WPD_CONTENT_TYPE_FOLDER = '27e2e392-a111-48e0-ab0c-e17705a05f85'
WPD_CONTENT_TYPE_IMAGE = 'ef2107d5-a52a-4243-a26b-62d4176d7603'
WPD_CONTENT_TYPE_DOCUMENT = '680adf52-950a-4041-9b41-65e393648155'
WPD_CONTENT_TYPE_CONTACT = 'eaba8313-4525-4707-9f0e-87c6808e9435'
WPD_CONTENT_TYPE_CONTACT_GROUP = '346b8932-4c36-40d8-9415-1828291f9de9'
WPD_CONTENT_TYPE_AUDIO = '4ad2c85e-5e2d-45e5-8864-4f229e3c6cf0'
WPD_CONTENT_TYPE_VIDEO = '9261b03c-3d78-4519-85e3-02c5e1f50bb9'
WPD_CONTENT_TYPE_TELEVISION = '60a169cf-f2ae-4e21-9375-9677f11c1c6e'
WPD_CONTENT_TYPE_PLAYLIST = '1a33f7e4-af13-48f5-994e-77369dfe04a3'
WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM = '00f0c3ac-a593-49ac-9219-24abca5a2563'
WPD_CONTENT_TYPE_AUDIO_ALBUM = 'aa18737e-5009-48fa-ae21-85f24383b4e6'
WPD_CONTENT_TYPE_IMAGE_ALBUM = '75793148-15f5-4a30-a813-54ed8a37e226'
WPD_CONTENT_TYPE_VIDEO_ALBUM = '012b0db7-d4c1-45d6-b081-94b87779614f'
WPD_CONTENT_TYPE_MEMO = '9cd20ecf-3b50-414f-a641-e473ffe45751'
WPD_CONTENT_TYPE_EMAIL = '8038044a-7e51-4f8f-883d-1d0623d14533'
WPD_CONTENT_TYPE_APPOINTMENT = '0fed060e-8793-4b1e-90c9-48ac389ac631'
WPD_CONTENT_TYPE_TASK = '63252f2c-887f-4cb6-b1ac-d29855dcef6c'
WPD_CONTENT_TYPE_PROGRAM = 'd269f96a-247c-4bff-98fb-97f3c49220e6'
WPD_CONTENT_TYPE_GENERIC_FILE = '0085e0a6-8d34-45d7-bc5c-447e59c73d48'
WPD_CONTENT_TYPE_CALENDAR = 'a1fd5967-6023-49a0-9df1-f8060be751b0'
WPD_CONTENT_TYPE_GENERIC_MESSAGE = 'e80eaaf8-b2db-4133-b67e-1bef4b4a6e5f'
WPD_CONTENT_TYPE_NETWORK_ASSOCIATION = '031da7ee-18c8-4205-847e-89a11261d0f3'
WPD_CONTENT_TYPE_CERTIFICATE = 'dc3876e8-a948-4060-9050-cbd77e8a3d87'
WPD_CONTENT_TYPE_WIRELESS_PROFILE = '0bac070a-9f5f-4da4-a8f6-3de44d68fd6c'
WPD_CONTENT_TYPE_MEDIA_CAST = '5e88b3cc-3e65-4e62-bfff-229495253ab0'
WPD_CONTENT_TYPE_SECTION = '821089f5-1d91-4dc9-be3c-bbb1b35b18ce'
WPD_CONTENT_TYPE_UNSPECIFIED = '28d8d31e-249c-454e-aabc-34883168e634'
WPD_CONTENT_TYPE_ALL = '80e170d2-1055-4a3e-b952-82cc4f8a8689'
WPD_FUNCTIONAL_CATEGORY_DEVICE = '08ea466b-e3a4-4336-a1f3-a44d2b5c438c'
WPD_FUNCTIONAL_CATEGORY_STORAGE = '23f05bbc-15de-4c2a-a55b-a9af5ce412ef'
WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE = '613ca327-ab93-4900-b4fa-895bb5874b79'
WPD_FUNCTIONAL_CATEGORY_AUDIO_CAPTURE = '3f2a1919-c7c2-4a00-855d-f57cf06debbb'
WPD_FUNCTIONAL_CATEGORY_VIDEO_CAPTURE = 'e23e5f6b-7243-43aa-8df1-0eb3d968a918'
WPD_FUNCTIONAL_CATEGORY_SMS = '0044a0b1-c1e9-4afd-b358-a62c6117c9cf'
WPD_FUNCTIONAL_CATEGORY_RENDERING_INFORMATION = '08600ba4-a7ba-4a01-ab0e-0065d0a356d3'
WPD_FUNCTIONAL_CATEGORY_NETWORK_CONFIGURATION = '48f4db72-7c6a-4ab0-9e1a-470e3cdbf26a'
WPD_FUNCTIONAL_CATEGORY_ALL = '2d8a6512-a74c-448e-ba8a-f4ac07c49399'
WPD_OBJECT_FORMAT_ICON = '077232ed-102c-4638-9c22-83f142bfc822'
WPD_OBJECT_FORMAT_M4A = '30aba7ac-6ffd-4c23-a359-3e9b52f3f1c8'
WPD_OBJECT_FORMAT_NETWORK_ASSOCIATION = 'b1020000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_X509V3CERTIFICATE = 'b1030000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_MICROSOFT_WFC = 'b1040000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_3GPA = 'e5172730-f971-41ef-a10b-2271a0019d7a'
WPD_OBJECT_FORMAT_3G2A = '1a11202d-8759-4e34-ba5e-b1211087eee4'
WPD_OBJECT_FORMAT_ALL = 'c1f62eb2-4bb3-479c-9cfa-05b5f3a57b22'
WPD_CATEGORY_NULL = '00000000-0000-0000-0000-000000000000'
WPD_OBJECT_PROPERTIES_V1 = 'ef6b490d-5cd8-437a-affc-da8b60ee4a3c'
WPD_OBJECT_PROPERTIES_V2 = '0373cd3d-4a46-40d7-b4d8-73e8da74e775'
WPD_FUNCTIONAL_OBJECT_PROPERTIES_V1 = '8f052d93-abca-4fc5-a5ac-b01df4dbe598'
WPD_STORAGE_OBJECT_PROPERTIES_V1 = '01a3057a-74d6-4e80-bea7-dc4c212ce50a'
WPD_NETWORK_ASSOCIATION_PROPERTIES_V1 = 'e4c93c1f-b203-43f1-a100-5a07d11b0274'
WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1 = '58c571ec-1bcb-42a7-8ac5-bb291573a260'
WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1 = 'c53d039f-ee23-4a31-8590-7639879870b4'
WPD_CLIENT_INFORMATION_PROPERTIES_V1 = '204d9f0c-2292-4080-9f42-40664e70f859'
WPD_PROPERTY_ATTRIBUTES_V1 = 'ab7943d8-6332-445f-a00d-8d5ef1e96f37'
WPD_PROPERTY_ATTRIBUTES_V2 = '5d9da160-74ae-43cc-85a9-fe555a80798e'
WPD_CLASS_EXTENSION_OPTIONS_V1 = '6309ffef-a87c-4ca7-8434-797576e40a96'
WPD_CLASS_EXTENSION_OPTIONS_V2 = '3e3595da-4d71-49fe-a0b4-d4406c3ae93f'
WPD_CLASS_EXTENSION_OPTIONS_V3 = '65c160f8-1367-4ce2-939d-8310839f0d30'
WPD_RESOURCE_ATTRIBUTES_V1 = '1eb6f604-9278-429f-93cc-5bb8c06656b6'
WPD_DEVICE_PROPERTIES_V1 = '26d4979a-e643-4626-9e2b-736dc0c92fdc'
WPD_DEVICE_PROPERTIES_V2 = '463dd662-7fc4-4291-911c-7f4c9cca9799'
WPD_DEVICE_PROPERTIES_V3 = '6c2b878c-c2ec-490d-b425-d7a75e23e5ed'
WPD_SERVICE_PROPERTIES_V1 = '7510698a-cb54-481c-b8db-0d75c93f1c06'
WPD_EVENT_PROPERTIES_V1 = '15ab1953-f817-4fef-a921-5676e838f6e0'
WPD_EVENT_PROPERTIES_V2 = '52807b8a-4914-4323-9b9a-74f654b2b846'
WPD_EVENT_OPTIONS_V1 = 'b3d8dad7-a361-4b83-8a48-5b02ce10713b'
WPD_EVENT_ATTRIBUTES_V1 = '10c96578-2e81-4111-adde-e08ca6138f6d'
WPD_API_OPTIONS_V1 = '10e54a3e-052d-4777-a13c-de7614be2bc4'
WPD_FORMAT_ATTRIBUTES_V1 = 'a0a02000-bcaf-4be8-b3f5-233f231cf58f'
WPD_METHOD_ATTRIBUTES_V1 = 'f17a5071-f039-44af-8efe-432cf32e432a'
WPD_PARAMETER_ATTRIBUTES_V1 = 'e6864dd7-f325-45ea-a1d5-97cf73b6ca58'
WPD_CATEGORY_COMMON = 'f0422a9c-5dc8-4440-b5bd-5df28835658a'
WPD_CATEGORY_OBJECT_ENUMERATION = 'b7474e91-e7f8-4ad9-b400-ad1a4b58eeec'
WPD_CATEGORY_OBJECT_PROPERTIES = '9e5582e4-0814-44e6-981a-b2998d583804'
WPD_CATEGORY_OBJECT_PROPERTIES_BULK = '11c824dd-04cd-4e4e-8c7b-f6efb794d84e'
WPD_CATEGORY_OBJECT_RESOURCES = 'b3a2b22d-a595-4108-be0a-fc3c965f3d4a'
WPD_CATEGORY_OBJECT_MANAGEMENT = 'ef1e43dd-a9ed-4341-8bcc-186192aea089'
WPD_CATEGORY_CAPABILITIES = '0cabec78-6b74-41c6-9216-2639d1fce356'
WPD_CATEGORY_STORAGE = 'd8f907a6-34cc-45fa-97fb-d007fa47ec94'
WPD_CATEGORY_SMS = 'afc25d66-fe0d-4114-9097-970c93e920d1'
WPD_CATEGORY_STILL_IMAGE_CAPTURE = '4fcd6982-22a2-4b05-a48b-62d38bf27b32'
WPD_CATEGORY_MEDIA_CAPTURE = '59b433ba-fe44-4d8d-808c-6bcb9b0f15e8'
WPD_CATEGORY_DEVICE_HINTS = '0d5fb92b-cb46-4c4f-8343-0bc3d3f17c84'
WPD_CLASS_EXTENSION_V1 = '33fb0d11-64a3-4fac-b4c7-3dfeaa99b051'
WPD_CLASS_EXTENSION_V2 = '7f0779b5-fa2b-4766-9cb2-f73ba30b6758'
WPD_CATEGORY_NETWORK_CONFIGURATION = '78f9c6fc-79b8-473c-9060-6bd23dd072c4'
WPD_CATEGORY_SERVICE_COMMON = '322f071d-36ef-477f-b4b5-6f52d734baee'
WPD_CATEGORY_SERVICE_CAPABILITIES = '24457e74-2e9f-44f9-8c57-1d1bcb170b89'
WPD_CATEGORY_SERVICE_METHODS = '2d521ca8-c1b0-4268-a342-cf19321569bc'
WPD_OBJECT_FORMAT_PROPERTIES_ONLY = '30010000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_UNSPECIFIED = '30000000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_SCRIPT = '30020000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_EXECUTABLE = '30030000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_TEXT = '30040000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_HTML = '30050000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_DPOF = '30060000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_AIFF = '30070000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_WAVE = '30080000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_MP3 = '30090000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_AVI = '300a0000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_MPEG = '300b0000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_ASF = '300c0000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_EXIF = '38010000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_TIFFEP = '38020000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_FLASHPIX = '38030000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_BMP = '38040000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_CIFF = '38050000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_GIF = '38070000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_JFIF = '38080000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_PCD = '38090000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_PICT = '380a0000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_PNG = '380b0000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_TIFF = '380d0000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_TIFFIT = '380e0000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_JP2 = '380f0000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_JPX = '38100000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_WBMP = 'b8030000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_JPEGXR = 'b8040000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_WINDOWSIMAGEFORMAT = 'b8810000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_WMA = 'b9010000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_WMV = 'b9810000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_WPLPLAYLIST = 'ba100000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_M3UPLAYLIST = 'ba110000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_MPLPLAYLIST = 'ba120000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_ASXPLAYLIST = 'ba130000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_PLSPLAYLIST = 'ba140000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_ABSTRACT_CONTACT_GROUP = 'ba060000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_ABSTRACT_MEDIA_CAST = 'ba0b0000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_VCALENDAR1 = 'be020000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_ICALENDAR = 'be030000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_ABSTRACT_CONTACT = 'bb810000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_VCARD2 = 'bb820000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_VCARD3 = 'bb830000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_XML = 'ba820000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_AAC = 'b9030000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_AUDIBLE = 'b9040000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_FLAC = 'b9060000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_QCELP = 'b9070000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_AMR = 'b9080000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_OGG = 'b9020000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_MP4 = 'b9820000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_MP2 = 'b9830000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_MICROSOFT_WORD = 'ba830000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_MHT_COMPILED_HTML = 'ba840000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_MICROSOFT_EXCEL = 'ba850000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_MICROSOFT_POWERPOINT = 'ba860000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_3GP = 'b9840000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_3G2 = 'b9850000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_AVCHD = 'b9860000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_ATSCTS = 'b9870000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_DVBTS = 'b9880000-ae6c-4804-98ba-c57b46965fe7'
WPD_OBJECT_FORMAT_MKV = 'b9900000-ae6c-4804-98ba-c57b46965fe7'
WPD_FOLDER_OBJECT_PROPERTIES_V1 = '7e9a7abf-e568-4b34-aa2f-13bb12ab177d'
WPD_IMAGE_OBJECT_PROPERTIES_V1 = '63d64908-9fa1-479f-85ba-9952216447db'
WPD_DOCUMENT_OBJECT_PROPERTIES_V1 = '0b110203-eb95-4f02-93e0-97c631493ad5'
WPD_MEDIA_PROPERTIES_V1 = '2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8'
WPD_CONTACT_OBJECT_PROPERTIES_V1 = 'fbd4fdab-987d-4777-b3f9-726185a9312b'
WPD_MUSIC_OBJECT_PROPERTIES_V1 = 'b324f56a-dc5d-46e5-b6df-d2ea414888c6'
WPD_VIDEO_OBJECT_PROPERTIES_V1 = '346f2163-f998-4146-8b01-d19b4c00de9a'
WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1 = 'b28ae94b-05a4-4e8e-be01-72cc7e099d8f'
WPD_MEMO_OBJECT_PROPERTIES_V1 = '5ffbfc7b-7483-41ad-afb9-da3f4e592b8d'
WPD_EMAIL_OBJECT_PROPERTIES_V1 = '41f8f65a-5484-4782-b13d-4740dd7c37c5'
WPD_APPOINTMENT_OBJECT_PROPERTIES_V1 = 'f99efd03-431d-40d8-a1c9-4e220d9c88d3'
WPD_TASK_OBJECT_PROPERTIES_V1 = 'e354e95e-d8a0-4637-a03a-0cb26838dbc7'
WPD_SMS_OBJECT_PROPERTIES_V1 = '7e1074cc-50ff-4dd1-a742-53be6f093a0d'
WPD_SECTION_OBJECT_PROPERTIES_V1 = '516afd2b-c64e-44f0-98dc-bee1c88f7d66'
DEVSVC_SERVICEINFO_VERSION = 100
DEVSVCTYPE_DEFAULT = 0
DEVSVCTYPE_ABSTRACT = 1
TYPE_CalendarSvc = 0
ENUM_CalendarObj_BusyStatusFree = 0
ENUM_CalendarObj_BusyStatusBusy = 1
ENUM_CalendarObj_BusyStatusOutOfOffice = 2
ENUM_CalendarObj_BusyStatusTentative = 3
TYPE_HintsSvc = 0
TYPE_MessageSvc = 0
ENUM_MessageObj_PriorityHighest = 2
ENUM_MessageObj_PriorityNormal = 1
ENUM_MessageObj_PriorityLowest = 0
ENUM_MessageObj_ReadFalse = 0
ENUM_MessageObj_ReadTrue = 255
ENUM_MessageObj_PatternTypeDaily = 1
ENUM_MessageObj_PatternTypeWeekly = 2
ENUM_MessageObj_PatternTypeMonthly = 3
ENUM_MessageObj_PatternTypeYearly = 4
FLAG_MessageObj_DayOfWeekNone = 0
FLAG_MessageObj_DayOfWeekSunday = 1
FLAG_MessageObj_DayOfWeekMonday = 2
FLAG_MessageObj_DayOfWeekTuesday = 4
FLAG_MessageObj_DayOfWeekWednesday = 8
FLAG_MessageObj_DayOfWeekThursday = 16
FLAG_MessageObj_DayOfWeekFriday = 32
FLAG_MessageObj_DayOfWeekSaturday = 64
RANGEMIN_MessageObj_PatternDayOfMonth = 1
RANGEMAX_MessageObj_PatternDayOfMonth = 31
RANGESTEP_MessageObj_PatternDayOfMonth = 1
RANGEMIN_MessageObj_PatternMonthOfYear = 1
RANGEMAX_MessageObj_PatternMonthOfYear = 12
RANGESTEP_MessageObj_PatternMonthOfYear = 1
ENUM_MessageObj_PatternInstanceNone = 0
ENUM_MessageObj_PatternInstanceFirst = 1
ENUM_MessageObj_PatternInstanceSecond = 2
ENUM_MessageObj_PatternInstanceThird = 3
ENUM_MessageObj_PatternInstanceFourth = 4
ENUM_MessageObj_PatternInstanceLast = 5
TYPE_DeviceMetadataSvc = 0
ENUM_DeviceMetadataObj_DefaultCABFalse = 0
ENUM_DeviceMetadataObj_DefaultCABTrue = 1
TYPE_NotesSvc = 0
TYPE_StatusSvc = 0
RANGEMIN_StatusSvc_SignalStrength = 0
RANGEMAX_StatusSvc_SignalStrength = 4
RANGESTEP_StatusSvc_SignalStrength = 1
RANGEMAX_StatusSvc_TextMessages = 255
RANGEMAX_StatusSvc_NewPictures = 65535
RANGEMAX_StatusSvc_MissedCalls = 255
RANGEMAX_StatusSvc_VoiceMail = 255
ENUM_StatusSvc_RoamingInactive = 0
ENUM_StatusSvc_RoamingActive = 1
ENUM_StatusSvc_RoamingUnknown = 2
RANGEMIN_StatusSvc_BatteryLife = 0
RANGEMAX_StatusSvc_BatteryLife = 100
RANGESTEP_StatusSvc_BatteryLife = 1
ENUM_StatusSvc_ChargingInactive = 0
ENUM_StatusSvc_ChargingActive = 1
ENUM_StatusSvc_ChargingUnknown = 2
SYNCSVC_FILTER_NONE = 0
SYNCSVC_FILTER_CONTACTS_WITH_PHONE = 1
SYNCSVC_FILTER_TASK_ACTIVE = 2
SYNCSVC_FILTER_CALENDAR_WINDOW_WITH_RECURRENCE = 3
ENUM_SyncSvc_SyncObjectReferencesDisabled = 0
ENUM_SyncSvc_SyncObjectReferencesEnabled = 255
TYPE_TasksSvc = 0
ENUM_TaskObj_CompleteFalse = 0
ENUM_TaskObj_CompleteTrue = 255
WPD_CATEGORY_MTP_EXT_VENDOR_OPERATIONS = '4d545058-1a2e-4106-a357-771e0819fc56'
WPD_PROPERTIES_MTP_VENDOR_EXTENDED_OBJECT_PROPS = '4d545058-4fce-4578-95c8-8698a9bc0f49'
WPD_PROPERTIES_MTP_VENDOR_EXTENDED_DEVICE_PROPS = '4d545058-8900-40b3-8f1d-dc246e1e8370'
WPD_EVENT_MTP_VENDOR_EXTENDED_EVENTS = '00000000-5738-4ff2-8445-be3126691059'
CLSID_WPD_NAMESPACE_EXTENSION = '35786d3c-b075-49b9-88dd-029876e11c01'
WPDNSE_OBJECT_PROPERTIES_V1 = '34d71409-4b47-4d80-aaac-3a28a4a3b3e6'
WPDNSE_PROPSHEET_DEVICE_GENERAL = 1
WPDNSE_PROPSHEET_STORAGE_GENERAL = 2
WPDNSE_PROPSHEET_CONTENT_GENERAL = 4
WPDNSE_PROPSHEET_CONTENT_REFERENCES = 8
WPDNSE_PROPSHEET_CONTENT_RESOURCES = 16
WPDNSE_PROPSHEET_CONTENT_DETAILS = 32
TYPE_ContactsSvc = 0
TYPE_RingtonesSvc = 0
TYPE_AnchorSyncSvc = 1
ENUM_AnchorResults_AnchorStateNormal = 0
ENUM_AnchorResults_AnchorStateInvalid = 1
ENUM_AnchorResults_AnchorStateOld = 2
ENUM_AnchorResults_ItemStateInvalid = 0
ENUM_AnchorResults_ItemStateDeleted = 1
ENUM_AnchorResults_ItemStateCreated = 2
ENUM_AnchorResults_ItemStateUpdated = 3
ENUM_AnchorResults_ItemStateChanged = 4
TYPE_FullEnumSyncSvc = 1
DELETE_OBJECT_OPTIONS = Int32
PORTABLE_DEVICE_DELETE_NO_RECURSION = 0
PORTABLE_DEVICE_DELETE_WITH_RECURSION = 1
WPD_DEVICE_TYPES = Int32
WPD_DEVICE_TYPE_GENERIC = 0
WPD_DEVICE_TYPE_CAMERA = 1
WPD_DEVICE_TYPE_MEDIA_PLAYER = 2
WPD_DEVICE_TYPE_PHONE = 3
WPD_DEVICE_TYPE_VIDEO = 4
WPD_DEVICE_TYPE_PERSONAL_INFORMATION_MANAGER = 5
WPD_DEVICE_TYPE_AUDIO_RECORDER = 6
WpdAttributeForm = Int32
WPD_PROPERTY_ATTRIBUTE_FORM_UNSPECIFIED = 0
WPD_PROPERTY_ATTRIBUTE_FORM_RANGE = 1
WPD_PROPERTY_ATTRIBUTE_FORM_ENUMERATION = 2
WPD_PROPERTY_ATTRIBUTE_FORM_REGULAR_EXPRESSION = 3
WPD_PROPERTY_ATTRIBUTE_FORM_OBJECT_IDENTIFIER = 4
WpdParameterAttributeForm = Int32
WPD_PARAMETER_ATTRIBUTE_FORM_UNSPECIFIED = 0
WPD_PARAMETER_ATTRIBUTE_FORM_RANGE = 1
WPD_PARAMETER_ATTRIBUTE_FORM_ENUMERATION = 2
WPD_PARAMETER_ATTRIBUTE_FORM_REGULAR_EXPRESSION = 3
WPD_PARAMETER_ATTRIBUTE_FORM_OBJECT_IDENTIFIER = 4
WPD_DEVICE_TRANSPORTS = Int32
WPD_DEVICE_TRANSPORT_UNSPECIFIED = 0
WPD_DEVICE_TRANSPORT_USB = 1
WPD_DEVICE_TRANSPORT_IP = 2
WPD_DEVICE_TRANSPORT_BLUETOOTH = 3
WPD_STORAGE_TYPE_VALUES = Int32
WPD_STORAGE_TYPE_UNDEFINED = 0
WPD_STORAGE_TYPE_FIXED_ROM = 1
WPD_STORAGE_TYPE_REMOVABLE_ROM = 2
WPD_STORAGE_TYPE_FIXED_RAM = 3
WPD_STORAGE_TYPE_REMOVABLE_RAM = 4
WPD_STORAGE_ACCESS_CAPABILITY_VALUES = Int32
WPD_STORAGE_ACCESS_CAPABILITY_READWRITE = 0
WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITHOUT_OBJECT_DELETION = 1
WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITH_OBJECT_DELETION = 2
WPD_SMS_ENCODING_TYPES = Int32
SMS_ENCODING_7_BIT = 0
SMS_ENCODING_8_BIT = 1
SMS_ENCODING_UTF_16 = 2
SMS_MESSAGE_TYPES = Int32
SMS_TEXT_MESSAGE = 0
SMS_BINARY_MESSAGE = 1
WPD_POWER_SOURCES = Int32
WPD_POWER_SOURCE_BATTERY = 0
WPD_POWER_SOURCE_EXTERNAL = 1
WPD_WHITE_BALANCE_SETTINGS = Int32
WPD_WHITE_BALANCE_UNDEFINED = 0
WPD_WHITE_BALANCE_MANUAL = 1
WPD_WHITE_BALANCE_AUTOMATIC = 2
WPD_WHITE_BALANCE_ONE_PUSH_AUTOMATIC = 3
WPD_WHITE_BALANCE_DAYLIGHT = 4
WPD_WHITE_BALANCE_FLORESCENT = 5
WPD_WHITE_BALANCE_TUNGSTEN = 6
WPD_WHITE_BALANCE_FLASH = 7
WPD_FOCUS_MODES = Int32
WPD_FOCUS_UNDEFINED = 0
WPD_FOCUS_MANUAL = 1
WPD_FOCUS_AUTOMATIC = 2
WPD_FOCUS_AUTOMATIC_MACRO = 3
WPD_EXPOSURE_METERING_MODES = Int32
WPD_EXPOSURE_METERING_MODE_UNDEFINED = 0
WPD_EXPOSURE_METERING_MODE_AVERAGE = 1
WPD_EXPOSURE_METERING_MODE_CENTER_WEIGHTED_AVERAGE = 2
WPD_EXPOSURE_METERING_MODE_MULTI_SPOT = 3
WPD_EXPOSURE_METERING_MODE_CENTER_SPOT = 4
WPD_FLASH_MODES = Int32
WPD_FLASH_MODE_UNDEFINED = 0
WPD_FLASH_MODE_AUTO = 1
WPD_FLASH_MODE_OFF = 2
WPD_FLASH_MODE_FILL = 3
WPD_FLASH_MODE_RED_EYE_AUTO = 4
WPD_FLASH_MODE_RED_EYE_FILL = 5
WPD_FLASH_MODE_EXTERNAL_SYNC = 6
WPD_EXPOSURE_PROGRAM_MODES = Int32
WPD_EXPOSURE_PROGRAM_MODE_UNDEFINED = 0
WPD_EXPOSURE_PROGRAM_MODE_MANUAL = 1
WPD_EXPOSURE_PROGRAM_MODE_AUTO = 2
WPD_EXPOSURE_PROGRAM_MODE_APERTURE_PRIORITY = 3
WPD_EXPOSURE_PROGRAM_MODE_SHUTTER_PRIORITY = 4
WPD_EXPOSURE_PROGRAM_MODE_CREATIVE = 5
WPD_EXPOSURE_PROGRAM_MODE_ACTION = 6
WPD_EXPOSURE_PROGRAM_MODE_PORTRAIT = 7
WPD_CAPTURE_MODES = Int32
WPD_CAPTURE_MODE_UNDEFINED = 0
WPD_CAPTURE_MODE_NORMAL = 1
WPD_CAPTURE_MODE_BURST = 2
WPD_CAPTURE_MODE_TIMELAPSE = 3
WPD_EFFECT_MODES = Int32
WPD_EFFECT_MODE_UNDEFINED = 0
WPD_EFFECT_MODE_COLOR = 1
WPD_EFFECT_MODE_BLACK_AND_WHITE = 2
WPD_EFFECT_MODE_SEPIA = 3
WPD_FOCUS_METERING_MODES = Int32
WPD_FOCUS_METERING_MODE_UNDEFINED = 0
WPD_FOCUS_METERING_MODE_CENTER_SPOT = 1
WPD_FOCUS_METERING_MODE_MULTI_SPOT = 2
WPD_BITRATE_TYPES = Int32
WPD_BITRATE_TYPE_UNUSED = 0
WPD_BITRATE_TYPE_DISCRETE = 1
WPD_BITRATE_TYPE_VARIABLE = 2
WPD_BITRATE_TYPE_FREE = 3
WPD_META_GENRES = Int32
WPD_META_GENRE_UNUSED = 0
WPD_META_GENRE_GENERIC_MUSIC_AUDIO_FILE = 1
WPD_META_GENRE_GENERIC_NON_MUSIC_AUDIO_FILE = 17
WPD_META_GENRE_SPOKEN_WORD_AUDIO_BOOK_FILES = 18
WPD_META_GENRE_SPOKEN_WORD_FILES_NON_AUDIO_BOOK = 19
WPD_META_GENRE_SPOKEN_WORD_NEWS = 20
WPD_META_GENRE_SPOKEN_WORD_TALK_SHOWS = 21
WPD_META_GENRE_GENERIC_VIDEO_FILE = 33
WPD_META_GENRE_NEWS_VIDEO_FILE = 34
WPD_META_GENRE_MUSIC_VIDEO_FILE = 35
WPD_META_GENRE_HOME_VIDEO_FILE = 36
WPD_META_GENRE_FEATURE_FILM_VIDEO_FILE = 37
WPD_META_GENRE_TELEVISION_VIDEO_FILE = 38
WPD_META_GENRE_TRAINING_EDUCATIONAL_VIDEO_FILE = 39
WPD_META_GENRE_PHOTO_MONTAGE_VIDEO_FILE = 40
WPD_META_GENRE_GENERIC_NON_AUDIO_NON_VIDEO = 48
WPD_META_GENRE_AUDIO_PODCAST = 64
WPD_META_GENRE_VIDEO_PODCAST = 65
WPD_META_GENRE_MIXED_PODCAST = 66
WPD_CROPPED_STATUS_VALUES = Int32
WPD_CROPPED_STATUS_NOT_CROPPED = 0
WPD_CROPPED_STATUS_CROPPED = 1
WPD_CROPPED_STATUS_SHOULD_NOT_BE_CROPPED = 2
WPD_COLOR_CORRECTED_STATUS_VALUES = Int32
WPD_COLOR_CORRECTED_STATUS_NOT_CORRECTED = 0
WPD_COLOR_CORRECTED_STATUS_CORRECTED = 1
WPD_COLOR_CORRECTED_STATUS_SHOULD_NOT_BE_CORRECTED = 2
WPD_VIDEO_SCAN_TYPES = Int32
WPD_VIDEO_SCAN_TYPE_UNUSED = 0
WPD_VIDEO_SCAN_TYPE_PROGRESSIVE = 1
WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_UPPER_FIRST = 2
WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_LOWER_FIRST = 3
WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_UPPER_FIRST = 4
WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_LOWER_FIRST = 5
WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE = 6
WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE_AND_PROGRESSIVE = 7
WPD_OPERATION_STATES = Int32
WPD_OPERATION_STATE_UNSPECIFIED = 0
WPD_OPERATION_STATE_STARTED = 1
WPD_OPERATION_STATE_RUNNING = 2
WPD_OPERATION_STATE_PAUSED = 3
WPD_OPERATION_STATE_CANCELLED = 4
WPD_OPERATION_STATE_FINISHED = 5
WPD_OPERATION_STATE_ABORTED = 6
WPD_SECTION_DATA_UNITS_VALUES = Int32
WPD_SECTION_DATA_UNITS_BYTES = 0
WPD_SECTION_DATA_UNITS_MILLISECONDS = 1
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES = Int32
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_OBJECT = 0
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_RESOURCE = 1
WPD_COMMAND_ACCESS_TYPES = Int32
WPD_COMMAND_ACCESS_READ = 1
WPD_COMMAND_ACCESS_READWRITE = 3
WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_STGM_ACCESS = 4
WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_FILE_ACCESS = 8
WPD_COMMAND_ACCESS_FROM_ATTRIBUTE_WITH_METHOD_ACCESS = 16
WPD_SERVICE_INHERITANCE_TYPES = Int32
WPD_SERVICE_INHERITANCE_IMPLEMENTATION = 0
WPD_PARAMETER_USAGE_TYPES = Int32
WPD_PARAMETER_USAGE_RETURN = 0
WPD_PARAMETER_USAGE_IN = 1
WPD_PARAMETER_USAGE_OUT = 2
WPD_PARAMETER_USAGE_INOUT = 3
def _define_WPD_COMMAND_ACCESS_LOOKUP_ENTRY_head():
    class WPD_COMMAND_ACCESS_LOOKUP_ENTRY(Structure):
        pass
    return WPD_COMMAND_ACCESS_LOOKUP_ENTRY
def _define_WPD_COMMAND_ACCESS_LOOKUP_ENTRY():
    WPD_COMMAND_ACCESS_LOOKUP_ENTRY = win32more.Devices.PortableDevices.WPD_COMMAND_ACCESS_LOOKUP_ENTRY_head
    WPD_COMMAND_ACCESS_LOOKUP_ENTRY._fields_ = [
        ("Command", win32more.UI.Shell.PropertiesSystem.PROPERTYKEY),
        ("AccessType", UInt32),
        ("AccessProperty", win32more.UI.Shell.PropertiesSystem.PROPERTYKEY),
    ]
    return WPD_COMMAND_ACCESS_LOOKUP_ENTRY
WpdSerializer = Guid('0b91a74b-ad7c-4a9d-b563-29eef9167172')
PortableDeviceValues = Guid('0c15d503-d017-47ce-9016-7b3f978721cc')
PortableDeviceKeyCollection = Guid('de2d022d-2480-43be-97f0-d1fa2cf98f4f')
PortableDevicePropVariantCollection = Guid('08a99e2f-6d6d-4b80-af5a-baf2bcbe4cb9')
PortableDeviceValuesCollection = Guid('3882134d-14cf-4220-9cb4-435f86d83f60')
WPD_STREAM_UNITS = Int32
WPD_STREAM_UNITS_BYTES = 0
WPD_STREAM_UNITS_FRAMES = 1
WPD_STREAM_UNITS_ROWS = 2
WPD_STREAM_UNITS_MILLISECONDS = 4
WPD_STREAM_UNITS_MICROSECONDS = 8
def _define_IWpdSerializer_head():
    class IWpdSerializer(win32more.System.Com.IUnknown_head):
        Guid = Guid('b32f4002-bb27-45ff-af4f-06631c1e8dad')
    return IWpdSerializer
def _define_IWpdSerializer():
    IWpdSerializer = win32more.Devices.PortableDevices.IWpdSerializer_head
    IWpdSerializer.GetIPortableDeviceValuesFromBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(3, 'GetIPortableDeviceValuesFromBuffer', ((1, 'pBuffer'),(1, 'dwInputBufferLength'),(1, 'ppParams'),)))
    IWpdSerializer.WriteIPortableDeviceValuesToBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(Byte),POINTER(UInt32), use_last_error=False)(4, 'WriteIPortableDeviceValuesToBuffer', ((1, 'dwOutputBufferLength'),(1, 'pResults'),(1, 'pBuffer'),(1, 'pdwBytesWritten'),)))
    IWpdSerializer.GetBufferFromIPortableDeviceValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(5, 'GetBufferFromIPortableDeviceValues', ((1, 'pSource'),(1, 'ppBuffer'),(1, 'pdwBufferSize'),)))
    IWpdSerializer.GetSerializedSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(UInt32), use_last_error=False)(6, 'GetSerializedSize', ((1, 'pSource'),(1, 'pdwSize'),)))
    return IWpdSerializer
def _define_IPortableDeviceValues_head():
    class IPortableDeviceValues(win32more.System.Com.IUnknown_head):
        Guid = Guid('6848f6f2-3155-4f86-b6f5-263eeeab3143')
    return IPortableDeviceValues
def _define_IPortableDeviceValues():
    IPortableDeviceValues = win32more.Devices.PortableDevices.IPortableDeviceValues_head
    IPortableDeviceValues.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pcelt'),)))
    IPortableDeviceValues.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(4, 'GetAt', ((1, 'index'),(1, 'pKey'),(1, 'pValue'),)))
    IPortableDeviceValues.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(5, 'SetValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(6, 'GetValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetStringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Foundation.PWSTR, use_last_error=False)(7, 'SetStringValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetStringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(8, 'GetStringValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetUnsignedIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32, use_last_error=False)(9, 'SetUnsignedIntegerValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetUnsignedIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(UInt32), use_last_error=False)(10, 'GetUnsignedIntegerValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetSignedIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),Int32, use_last_error=False)(11, 'SetSignedIntegerValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetSignedIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Int32), use_last_error=False)(12, 'GetSignedIntegerValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetUnsignedLargeIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt64, use_last_error=False)(13, 'SetUnsignedLargeIntegerValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetUnsignedLargeIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(UInt64), use_last_error=False)(14, 'GetUnsignedLargeIntegerValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetSignedLargeIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),Int64, use_last_error=False)(15, 'SetSignedLargeIntegerValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetSignedLargeIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Int64), use_last_error=False)(16, 'GetSignedLargeIntegerValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetFloatValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),Single, use_last_error=False)(17, 'SetFloatValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetFloatValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Single), use_last_error=False)(18, 'GetFloatValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetErrorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Foundation.HRESULT, use_last_error=False)(19, 'SetErrorValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetErrorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.HRESULT), use_last_error=False)(20, 'GetErrorValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetKeyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(21, 'SetKeyValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetKeyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(22, 'GetKeyValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetBoolValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Foundation.BOOL, use_last_error=False)(23, 'SetBoolValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetBoolValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(24, 'GetBoolValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetIUnknownValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.System.Com.IUnknown_head, use_last_error=False)(25, 'SetIUnknownValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetIUnknownValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(26, 'GetIUnknownValue', ((1, 'key'),(1, 'ppValue'),)))
    IPortableDeviceValues.SetGuidValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Guid), use_last_error=False)(27, 'SetGuidValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetGuidValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Guid), use_last_error=False)(28, 'GetGuidValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetBufferValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Byte),UInt32, use_last_error=False)(29, 'SetBufferValue', ((1, 'key'),(1, 'pValue'),(1, 'cbValue'),)))
    IPortableDeviceValues.GetBufferValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(30, 'GetBufferValue', ((1, 'key'),(1, 'ppValue'),(1, 'pcbValue'),)))
    IPortableDeviceValues.SetIPortableDeviceValuesValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Devices.PortableDevices.IPortableDeviceValues_head, use_last_error=False)(31, 'SetIPortableDeviceValuesValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetIPortableDeviceValuesValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(32, 'GetIPortableDeviceValuesValue', ((1, 'key'),(1, 'ppValue'),)))
    IPortableDeviceValues.SetIPortableDevicePropVariantCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head, use_last_error=False)(33, 'SetIPortableDevicePropVariantCollectionValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetIPortableDevicePropVariantCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(34, 'GetIPortableDevicePropVariantCollectionValue', ((1, 'key'),(1, 'ppValue'),)))
    IPortableDeviceValues.SetIPortableDeviceKeyCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head, use_last_error=False)(35, 'SetIPortableDeviceKeyCollectionValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetIPortableDeviceKeyCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head), use_last_error=False)(36, 'GetIPortableDeviceKeyCollectionValue', ((1, 'key'),(1, 'ppValue'),)))
    IPortableDeviceValues.SetIPortableDeviceValuesCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head, use_last_error=False)(37, 'SetIPortableDeviceValuesCollectionValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetIPortableDeviceValuesCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head), use_last_error=False)(38, 'GetIPortableDeviceValuesCollectionValue', ((1, 'key'),(1, 'ppValue'),)))
    IPortableDeviceValues.RemoveValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(39, 'RemoveValue', ((1, 'key'),)))
    IPortableDeviceValues.CopyValuesFromPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, use_last_error=False)(40, 'CopyValuesFromPropertyStore', ((1, 'pStore'),)))
    IPortableDeviceValues.CopyValuesToPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, use_last_error=False)(41, 'CopyValuesToPropertyStore', ((1, 'pStore'),)))
    IPortableDeviceValues.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(42, 'Clear', ()))
    return IPortableDeviceValues
def _define_IPortableDeviceKeyCollection_head():
    class IPortableDeviceKeyCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('dada2357-e0ad-492e-98db-dd61c53ba353')
    return IPortableDeviceKeyCollection
def _define_IPortableDeviceKeyCollection():
    IPortableDeviceKeyCollection = win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head
    IPortableDeviceKeyCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pcElems'),)))
    IPortableDeviceKeyCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(4, 'GetAt', ((1, 'dwIndex'),(1, 'pKey'),)))
    IPortableDeviceKeyCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(5, 'Add', ((1, 'Key'),)))
    IPortableDeviceKeyCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Clear', ()))
    IPortableDeviceKeyCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'RemoveAt', ((1, 'dwIndex'),)))
    return IPortableDeviceKeyCollection
def _define_IPortableDevicePropVariantCollection_head():
    class IPortableDevicePropVariantCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('89b2e422-4f1b-4316-bcef-a44afea83eb3')
    return IPortableDevicePropVariantCollection
def _define_IPortableDevicePropVariantCollection():
    IPortableDevicePropVariantCollection = win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head
    IPortableDevicePropVariantCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pcElems'),)))
    IPortableDevicePropVariantCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(4, 'GetAt', ((1, 'dwIndex'),(1, 'pValue'),)))
    IPortableDevicePropVariantCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(5, 'Add', ((1, 'pValue'),)))
    IPortableDevicePropVariantCollection.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(6, 'GetType', ((1, 'pvt'),)))
    IPortableDevicePropVariantCollection.ChangeType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(7, 'ChangeType', ((1, 'vt'),)))
    IPortableDevicePropVariantCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Clear', ()))
    IPortableDevicePropVariantCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'RemoveAt', ((1, 'dwIndex'),)))
    return IPortableDevicePropVariantCollection
def _define_IPortableDeviceValuesCollection_head():
    class IPortableDeviceValuesCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('6e3f2d79-4e07-48c4-8208-d8c2e5af4a99')
    return IPortableDeviceValuesCollection
def _define_IPortableDeviceValuesCollection():
    IPortableDeviceValuesCollection = win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head
    IPortableDeviceValuesCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pcElems'),)))
    IPortableDeviceValuesCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(4, 'GetAt', ((1, 'dwIndex'),(1, 'ppValues'),)))
    IPortableDeviceValuesCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head, use_last_error=False)(5, 'Add', ((1, 'pValues'),)))
    IPortableDeviceValuesCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Clear', ()))
    IPortableDeviceValuesCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'RemoveAt', ((1, 'dwIndex'),)))
    return IPortableDeviceValuesCollection
PortableDevice = Guid('728a21c5-3d9e-48d7-9810-864848f0f404')
PortableDeviceManager = Guid('0af10cec-2ecd-4b92-9581-34f6ae0637f3')
PortableDeviceService = Guid('ef5db4c2-9312-422c-9152-411cd9c4dd84')
PortableDeviceDispatchFactory = Guid('43232233-8338-4658-ae01-0b4ae830b6b0')
PortableDeviceFTM = Guid('f7c0039a-4762-488a-b4b3-760ef9a1ba9b')
PortableDeviceServiceFTM = Guid('1649b154-c794-497a-9b03-f3f0121302f3')
PortableDeviceWebControl = Guid('186dd02c-2dec-41b5-a7d4-b59056fade51')
def _define_IPortableDeviceManager_head():
    class IPortableDeviceManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1567595-4c2f-4574-a6fa-ecef917b9a40')
    return IPortableDeviceManager
def _define_IPortableDeviceManager():
    IPortableDeviceManager = win32more.Devices.PortableDevices.IPortableDeviceManager_head
    IPortableDeviceManager.GetDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(3, 'GetDevices', ((1, 'pPnPDeviceIDs'),(1, 'pcPnPDeviceIDs'),)))
    IPortableDeviceManager.RefreshDeviceList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'RefreshDeviceList', ()))
    IPortableDeviceManager.GetDeviceFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(5, 'GetDeviceFriendlyName', ((1, 'pszPnPDeviceID'),(1, 'pDeviceFriendlyName'),(1, 'pcchDeviceFriendlyName'),)))
    IPortableDeviceManager.GetDeviceDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(6, 'GetDeviceDescription', ((1, 'pszPnPDeviceID'),(1, 'pDeviceDescription'),(1, 'pcchDeviceDescription'),)))
    IPortableDeviceManager.GetDeviceManufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(7, 'GetDeviceManufacturer', ((1, 'pszPnPDeviceID'),(1, 'pDeviceManufacturer'),(1, 'pcchDeviceManufacturer'),)))
    IPortableDeviceManager.GetDeviceProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(8, 'GetDeviceProperty', ((1, 'pszPnPDeviceID'),(1, 'pszDevicePropertyName'),(1, 'pData'),(1, 'pcbData'),(1, 'pdwType'),)))
    IPortableDeviceManager.GetPrivateDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(9, 'GetPrivateDevices', ((1, 'pPnPDeviceIDs'),(1, 'pcPnPDeviceIDs'),)))
    return IPortableDeviceManager
def _define_IPortableDevice_head():
    class IPortableDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('625e2df8-6392-4cf0-9ad1-3cfa5f17775c')
    return IPortableDevice
def _define_IPortableDevice():
    IPortableDevice = win32more.Devices.PortableDevices.IPortableDevice_head
    IPortableDevice.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head, use_last_error=False)(3, 'Open', ((1, 'pszPnPDeviceID'),(1, 'pClientInfo'),)))
    IPortableDevice.SendCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(4, 'SendCommand', ((1, 'dwFlags'),(1, 'pParameters'),(1, 'ppResults'),)))
    IPortableDevice.Content = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceContent_head), use_last_error=False)(5, 'Content', ((1, 'ppContent'),)))
    IPortableDevice.Capabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceCapabilities_head), use_last_error=False)(6, 'Capabilities', ((1, 'ppCapabilities'),)))
    IPortableDevice.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Cancel', ()))
    IPortableDevice.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Close', ()))
    IPortableDevice.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDeviceEventCallback_head,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(9, 'Advise', ((1, 'dwFlags'),(1, 'pCallback'),(1, 'pParameters'),(1, 'ppszCookie'),)))
    IPortableDevice.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(10, 'Unadvise', ((1, 'pszCookie'),)))
    IPortableDevice.GetPnPDeviceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(11, 'GetPnPDeviceID', ((1, 'ppszPnPDeviceID'),)))
    return IPortableDevice
def _define_IPortableDeviceContent_head():
    class IPortableDeviceContent(win32more.System.Com.IUnknown_head):
        Guid = Guid('6a96ed84-7c73-4480-9938-bf5af477d426')
    return IPortableDeviceContent
def _define_IPortableDeviceContent():
    IPortableDeviceContent = win32more.Devices.PortableDevices.IPortableDeviceContent_head
    IPortableDeviceContent.EnumObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IEnumPortableDeviceObjectIDs_head), use_last_error=False)(3, 'EnumObjects', ((1, 'dwFlags'),(1, 'pszParentObjectID'),(1, 'pFilter'),(1, 'ppEnum'),)))
    IPortableDeviceContent.Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceProperties_head), use_last_error=False)(4, 'Properties', ((1, 'ppProperties'),)))
    IPortableDeviceContent.Transfer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceResources_head), use_last_error=False)(5, 'Transfer', ((1, 'ppResources'),)))
    IPortableDeviceContent.CreateObjectWithPropertiesOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'CreateObjectWithPropertiesOnly', ((1, 'pValues'),(1, 'ppszObjectID'),)))
    IPortableDeviceContent.CreateObjectWithPropertiesAndData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.System.Com.IStream_head),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'CreateObjectWithPropertiesAndData', ((1, 'pValues'),(1, 'ppData'),(1, 'pdwOptimalWriteBufferSize'),(1, 'ppszCookie'),)))
    IPortableDeviceContent.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(8, 'Delete', ((1, 'dwOptions'),(1, 'pObjectIDs'),(1, 'ppResults'),)))
    IPortableDeviceContent.GetObjectIDsFromPersistentUniqueIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(9, 'GetObjectIDsFromPersistentUniqueIDs', ((1, 'pPersistentUniqueIDs'),(1, 'ppObjectIDs'),)))
    IPortableDeviceContent.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Cancel', ()))
    IPortableDeviceContent.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head,win32more.Foundation.PWSTR,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(11, 'Move', ((1, 'pObjectIDs'),(1, 'pszDestinationFolderObjectID'),(1, 'ppResults'),)))
    IPortableDeviceContent.Copy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head,win32more.Foundation.PWSTR,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(12, 'Copy', ((1, 'pObjectIDs'),(1, 'pszDestinationFolderObjectID'),(1, 'ppResults'),)))
    return IPortableDeviceContent
def _define_IPortableDeviceContent2_head():
    class IPortableDeviceContent2(win32more.Devices.PortableDevices.IPortableDeviceContent_head):
        Guid = Guid('9b4add96-f6bf-4034-8708-eca72bf10554')
    return IPortableDeviceContent2
def _define_IPortableDeviceContent2():
    IPortableDeviceContent2 = win32more.Devices.PortableDevices.IPortableDeviceContent2_head
    IPortableDeviceContent2.UpdateObjectWithPropertiesAndData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.System.Com.IStream_head),POINTER(UInt32), use_last_error=False)(13, 'UpdateObjectWithPropertiesAndData', ((1, 'pszObjectID'),(1, 'pProperties'),(1, 'ppData'),(1, 'pdwOptimalWriteBufferSize'),)))
    return IPortableDeviceContent2
def _define_IEnumPortableDeviceObjectIDs_head():
    class IEnumPortableDeviceObjectIDs(win32more.System.Com.IUnknown_head):
        Guid = Guid('10ece955-cf41-4728-bfa0-41eedf1bbf19')
    return IEnumPortableDeviceObjectIDs
def _define_IEnumPortableDeviceObjectIDs():
    IEnumPortableDeviceObjectIDs = win32more.Devices.PortableDevices.IEnumPortableDeviceObjectIDs_head
    IEnumPortableDeviceObjectIDs.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cObjects'),(1, 'pObjIDs'),(1, 'pcFetched'),)))
    IEnumPortableDeviceObjectIDs.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cObjects'),)))
    IEnumPortableDeviceObjectIDs.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumPortableDeviceObjectIDs.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IEnumPortableDeviceObjectIDs_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    IEnumPortableDeviceObjectIDs.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Cancel', ()))
    return IEnumPortableDeviceObjectIDs
def _define_IPortableDeviceProperties_head():
    class IPortableDeviceProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('7f6d695c-03df-4439-a809-59266beee3a6')
    return IPortableDeviceProperties
def _define_IPortableDeviceProperties():
    IPortableDeviceProperties = win32more.Devices.PortableDevices.IPortableDeviceProperties_head
    IPortableDeviceProperties.GetSupportedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head), use_last_error=False)(3, 'GetSupportedProperties', ((1, 'pszObjectID'),(1, 'ppKeys'),)))
    IPortableDeviceProperties.GetPropertyAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(4, 'GetPropertyAttributes', ((1, 'pszObjectID'),(1, 'Key'),(1, 'ppAttributes'),)))
    IPortableDeviceProperties.GetValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(5, 'GetValues', ((1, 'pszObjectID'),(1, 'pKeys'),(1, 'ppValues'),)))
    IPortableDeviceProperties.SetValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(6, 'SetValues', ((1, 'pszObjectID'),(1, 'pValues'),(1, 'ppResults'),)))
    IPortableDeviceProperties.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head, use_last_error=False)(7, 'Delete', ((1, 'pszObjectID'),(1, 'pKeys'),)))
    IPortableDeviceProperties.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Cancel', ()))
    return IPortableDeviceProperties
def _define_IPortableDeviceResources_head():
    class IPortableDeviceResources(win32more.System.Com.IUnknown_head):
        Guid = Guid('fd8878ac-d841-4d17-891c-e6829cdb6934')
    return IPortableDeviceResources
def _define_IPortableDeviceResources():
    IPortableDeviceResources = win32more.Devices.PortableDevices.IPortableDeviceResources_head
    IPortableDeviceResources.GetSupportedResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head), use_last_error=False)(3, 'GetSupportedResources', ((1, 'pszObjectID'),(1, 'ppKeys'),)))
    IPortableDeviceResources.GetResourceAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(4, 'GetResourceAttributes', ((1, 'pszObjectID'),(1, 'Key'),(1, 'ppResourceAttributes'),)))
    IPortableDeviceResources.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32,POINTER(UInt32),POINTER(win32more.System.Com.IStream_head), use_last_error=False)(5, 'GetStream', ((1, 'pszObjectID'),(1, 'Key'),(1, 'dwMode'),(1, 'pdwOptimalBufferSize'),(1, 'ppStream'),)))
    IPortableDeviceResources.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head, use_last_error=False)(6, 'Delete', ((1, 'pszObjectID'),(1, 'pKeys'),)))
    IPortableDeviceResources.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Cancel', ()))
    IPortableDeviceResources.CreateResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.System.Com.IStream_head),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(8, 'CreateResource', ((1, 'pResourceAttributes'),(1, 'ppData'),(1, 'pdwOptimalWriteBufferSize'),(1, 'ppszCookie'),)))
    return IPortableDeviceResources
def _define_IPortableDeviceCapabilities_head():
    class IPortableDeviceCapabilities(win32more.System.Com.IUnknown_head):
        Guid = Guid('2c8c6dbf-e3dc-4061-becc-8542e810d126')
    return IPortableDeviceCapabilities
def _define_IPortableDeviceCapabilities():
    IPortableDeviceCapabilities = win32more.Devices.PortableDevices.IPortableDeviceCapabilities_head
    IPortableDeviceCapabilities.GetSupportedCommands = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head), use_last_error=False)(3, 'GetSupportedCommands', ((1, 'ppCommands'),)))
    IPortableDeviceCapabilities.GetCommandOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(4, 'GetCommandOptions', ((1, 'Command'),(1, 'ppOptions'),)))
    IPortableDeviceCapabilities.GetFunctionalCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(5, 'GetFunctionalCategories', ((1, 'ppCategories'),)))
    IPortableDeviceCapabilities.GetFunctionalObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(6, 'GetFunctionalObjects', ((1, 'Category'),(1, 'ppObjectIDs'),)))
    IPortableDeviceCapabilities.GetSupportedContentTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(7, 'GetSupportedContentTypes', ((1, 'Category'),(1, 'ppContentTypes'),)))
    IPortableDeviceCapabilities.GetSupportedFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(8, 'GetSupportedFormats', ((1, 'ContentType'),(1, 'ppFormats'),)))
    IPortableDeviceCapabilities.GetSupportedFormatProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head), use_last_error=False)(9, 'GetSupportedFormatProperties', ((1, 'Format'),(1, 'ppKeys'),)))
    IPortableDeviceCapabilities.GetFixedPropertyAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(10, 'GetFixedPropertyAttributes', ((1, 'Format'),(1, 'Key'),(1, 'ppAttributes'),)))
    IPortableDeviceCapabilities.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Cancel', ()))
    IPortableDeviceCapabilities.GetSupportedEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(12, 'GetSupportedEvents', ((1, 'ppEvents'),)))
    IPortableDeviceCapabilities.GetEventOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(13, 'GetEventOptions', ((1, 'Event'),(1, 'ppOptions'),)))
    return IPortableDeviceCapabilities
def _define_IPortableDeviceEventCallback_head():
    class IPortableDeviceEventCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('a8792a31-f385-493c-a893-40f64eb45f6e')
    return IPortableDeviceEventCallback
def _define_IPortableDeviceEventCallback():
    IPortableDeviceEventCallback = win32more.Devices.PortableDevices.IPortableDeviceEventCallback_head
    IPortableDeviceEventCallback.OnEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head, use_last_error=False)(3, 'OnEvent', ((1, 'pEventParameters'),)))
    return IPortableDeviceEventCallback
def _define_IPortableDeviceDataStream_head():
    class IPortableDeviceDataStream(win32more.System.Com.IStream_head):
        Guid = Guid('88e04db3-1012-4d64-9996-f703a950d3f4')
    return IPortableDeviceDataStream
def _define_IPortableDeviceDataStream():
    IPortableDeviceDataStream = win32more.Devices.PortableDevices.IPortableDeviceDataStream_head
    IPortableDeviceDataStream.GetObjectID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(14, 'GetObjectID', ((1, 'ppszObjectID'),)))
    IPortableDeviceDataStream.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'Cancel', ()))
    return IPortableDeviceDataStream
def _define_IPortableDeviceUnitsStream_head():
    class IPortableDeviceUnitsStream(win32more.System.Com.IUnknown_head):
        Guid = Guid('5e98025f-bfc4-47a2-9a5f-bc900a507c67')
    return IPortableDeviceUnitsStream
def _define_IPortableDeviceUnitsStream():
    IPortableDeviceUnitsStream = win32more.Devices.PortableDevices.IPortableDeviceUnitsStream_head
    IPortableDeviceUnitsStream.SeekInUnits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LARGE_INTEGER,win32more.Devices.PortableDevices.WPD_STREAM_UNITS,UInt32,POINTER(win32more.Foundation.ULARGE_INTEGER_head), use_last_error=False)(3, 'SeekInUnits', ((1, 'dlibMove'),(1, 'units'),(1, 'dwOrigin'),(1, 'plibNewPosition'),)))
    IPortableDeviceUnitsStream.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Cancel', ()))
    return IPortableDeviceUnitsStream
def _define_IPortableDevicePropertiesBulk_head():
    class IPortableDevicePropertiesBulk(win32more.System.Com.IUnknown_head):
        Guid = Guid('482b05c0-4056-44ed-9e0f-5e23b009da93')
    return IPortableDevicePropertiesBulk
def _define_IPortableDevicePropertiesBulk():
    IPortableDevicePropertiesBulk = win32more.Devices.PortableDevices.IPortableDevicePropertiesBulk_head
    IPortableDevicePropertiesBulk.QueueGetValuesByObjectList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head,win32more.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback_head,POINTER(Guid), use_last_error=False)(3, 'QueueGetValuesByObjectList', ((1, 'pObjectIDs'),(1, 'pKeys'),(1, 'pCallback'),(1, 'pContext'),)))
    IPortableDevicePropertiesBulk.QueueGetValuesByObjectFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head,win32more.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback_head,POINTER(Guid), use_last_error=False)(4, 'QueueGetValuesByObjectFormat', ((1, 'pguidObjectFormat'),(1, 'pszParentObjectID'),(1, 'dwDepth'),(1, 'pKeys'),(1, 'pCallback'),(1, 'pContext'),)))
    IPortableDevicePropertiesBulk.QueueSetValuesByObjectList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head,win32more.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback_head,POINTER(Guid), use_last_error=False)(5, 'QueueSetValuesByObjectList', ((1, 'pObjectValues'),(1, 'pCallback'),(1, 'pContext'),)))
    IPortableDevicePropertiesBulk.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(6, 'Start', ((1, 'pContext'),)))
    IPortableDevicePropertiesBulk.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(7, 'Cancel', ((1, 'pContext'),)))
    return IPortableDevicePropertiesBulk
def _define_IPortableDevicePropertiesBulkCallback_head():
    class IPortableDevicePropertiesBulkCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('9deacb80-11e8-40e3-a9f3-f557986a7845')
    return IPortableDevicePropertiesBulkCallback
def _define_IPortableDevicePropertiesBulkCallback():
    IPortableDevicePropertiesBulkCallback = win32more.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback_head
    IPortableDevicePropertiesBulkCallback.OnStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'OnStart', ((1, 'pContext'),)))
    IPortableDevicePropertiesBulkCallback.OnProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head, use_last_error=False)(4, 'OnProgress', ((1, 'pContext'),(1, 'pResults'),)))
    IPortableDevicePropertiesBulkCallback.OnEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.HRESULT, use_last_error=False)(5, 'OnEnd', ((1, 'pContext'),(1, 'hrStatus'),)))
    return IPortableDevicePropertiesBulkCallback
def _define_IPortableDeviceServiceManager_head():
    class IPortableDeviceServiceManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('a8abc4e9-a84a-47a9-80b3-c5d9b172a961')
    return IPortableDeviceServiceManager
def _define_IPortableDeviceServiceManager():
    IPortableDeviceServiceManager = win32more.Devices.PortableDevices.IPortableDeviceServiceManager_head
    IPortableDeviceServiceManager.GetDeviceServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(3, 'GetDeviceServices', ((1, 'pszPnPDeviceID'),(1, 'guidServiceCategory'),(1, 'pServices'),(1, 'pcServices'),)))
    IPortableDeviceServiceManager.GetDeviceForService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetDeviceForService', ((1, 'pszPnPServiceID'),(1, 'ppszPnPDeviceID'),)))
    return IPortableDeviceServiceManager
def _define_IPortableDeviceService_head():
    class IPortableDeviceService(win32more.System.Com.IUnknown_head):
        Guid = Guid('d3bd3a44-d7b5-40a9-98b7-2fa4d01dec08')
    return IPortableDeviceService
def _define_IPortableDeviceService():
    IPortableDeviceService = win32more.Devices.PortableDevices.IPortableDeviceService_head
    IPortableDeviceService.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head, use_last_error=False)(3, 'Open', ((1, 'pszPnPServiceID'),(1, 'pClientInfo'),)))
    IPortableDeviceService.Capabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceServiceCapabilities_head), use_last_error=False)(4, 'Capabilities', ((1, 'ppCapabilities'),)))
    IPortableDeviceService.Content = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceContent2_head), use_last_error=False)(5, 'Content', ((1, 'ppContent'),)))
    IPortableDeviceService.Methods = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceServiceMethods_head), use_last_error=False)(6, 'Methods', ((1, 'ppMethods'),)))
    IPortableDeviceService.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Cancel', ()))
    IPortableDeviceService.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Close', ()))
    IPortableDeviceService.GetServiceObjectID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(9, 'GetServiceObjectID', ((1, 'ppszServiceObjectID'),)))
    IPortableDeviceService.GetPnPServiceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(10, 'GetPnPServiceID', ((1, 'ppszPnPServiceID'),)))
    IPortableDeviceService.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDeviceEventCallback_head,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(11, 'Advise', ((1, 'dwFlags'),(1, 'pCallback'),(1, 'pParameters'),(1, 'ppszCookie'),)))
    IPortableDeviceService.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(12, 'Unadvise', ((1, 'pszCookie'),)))
    IPortableDeviceService.SendCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(13, 'SendCommand', ((1, 'dwFlags'),(1, 'pParameters'),(1, 'ppResults'),)))
    return IPortableDeviceService
def _define_IPortableDeviceServiceCapabilities_head():
    class IPortableDeviceServiceCapabilities(win32more.System.Com.IUnknown_head):
        Guid = Guid('24dbd89d-413e-43e0-bd5b-197f3c56c886')
    return IPortableDeviceServiceCapabilities
def _define_IPortableDeviceServiceCapabilities():
    IPortableDeviceServiceCapabilities = win32more.Devices.PortableDevices.IPortableDeviceServiceCapabilities_head
    IPortableDeviceServiceCapabilities.GetSupportedMethods = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(3, 'GetSupportedMethods', ((1, 'ppMethods'),)))
    IPortableDeviceServiceCapabilities.GetSupportedMethodsByFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(4, 'GetSupportedMethodsByFormat', ((1, 'Format'),(1, 'ppMethods'),)))
    IPortableDeviceServiceCapabilities.GetMethodAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(5, 'GetMethodAttributes', ((1, 'Method'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetMethodParameterAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(6, 'GetMethodParameterAttributes', ((1, 'Method'),(1, 'Parameter'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetSupportedFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(7, 'GetSupportedFormats', ((1, 'ppFormats'),)))
    IPortableDeviceServiceCapabilities.GetFormatAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(8, 'GetFormatAttributes', ((1, 'Format'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetSupportedFormatProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head), use_last_error=False)(9, 'GetSupportedFormatProperties', ((1, 'Format'),(1, 'ppKeys'),)))
    IPortableDeviceServiceCapabilities.GetFormatPropertyAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(10, 'GetFormatPropertyAttributes', ((1, 'Format'),(1, 'Property'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetSupportedEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(11, 'GetSupportedEvents', ((1, 'ppEvents'),)))
    IPortableDeviceServiceCapabilities.GetEventAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(12, 'GetEventAttributes', ((1, 'Event'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetEventParameterAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(13, 'GetEventParameterAttributes', ((1, 'Event'),(1, 'Parameter'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetInheritedServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head), use_last_error=False)(14, 'GetInheritedServices', ((1, 'dwInheritanceType'),(1, 'ppServices'),)))
    IPortableDeviceServiceCapabilities.GetFormatRenderingProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head), use_last_error=False)(15, 'GetFormatRenderingProfiles', ((1, 'Format'),(1, 'ppRenderingProfiles'),)))
    IPortableDeviceServiceCapabilities.GetSupportedCommands = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head), use_last_error=False)(16, 'GetSupportedCommands', ((1, 'ppCommands'),)))
    IPortableDeviceServiceCapabilities.GetCommandOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(17, 'GetCommandOptions', ((1, 'Command'),(1, 'ppOptions'),)))
    IPortableDeviceServiceCapabilities.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'Cancel', ()))
    return IPortableDeviceServiceCapabilities
def _define_IPortableDeviceServiceMethods_head():
    class IPortableDeviceServiceMethods(win32more.System.Com.IUnknown_head):
        Guid = Guid('e20333c9-fd34-412d-a381-cc6f2d820df7')
    return IPortableDeviceServiceMethods
def _define_IPortableDeviceServiceMethods():
    IPortableDeviceServiceMethods = win32more.Devices.PortableDevices.IPortableDeviceServiceMethods_head
    IPortableDeviceServiceMethods.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(3, 'Invoke', ((1, 'Method'),(1, 'pParameters'),(1, 'ppResults'),)))
    IPortableDeviceServiceMethods.InvokeAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Devices.PortableDevices.IPortableDeviceValues_head,win32more.Devices.PortableDevices.IPortableDeviceServiceMethodCallback_head, use_last_error=False)(4, 'InvokeAsync', ((1, 'Method'),(1, 'pParameters'),(1, 'pCallback'),)))
    IPortableDeviceServiceMethods.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceServiceMethodCallback_head, use_last_error=False)(5, 'Cancel', ((1, 'pCallback'),)))
    return IPortableDeviceServiceMethods
def _define_IPortableDeviceServiceMethodCallback_head():
    class IPortableDeviceServiceMethodCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('c424233c-afce-4828-a756-7ed7a2350083')
    return IPortableDeviceServiceMethodCallback
def _define_IPortableDeviceServiceMethodCallback():
    IPortableDeviceServiceMethodCallback = win32more.Devices.PortableDevices.IPortableDeviceServiceMethodCallback_head
    IPortableDeviceServiceMethodCallback.OnComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head, use_last_error=False)(3, 'OnComplete', ((1, 'hrStatus'),(1, 'pResults'),)))
    return IPortableDeviceServiceMethodCallback
def _define_IPortableDeviceServiceActivation_head():
    class IPortableDeviceServiceActivation(win32more.System.Com.IUnknown_head):
        Guid = Guid('e56b0534-d9b9-425c-9b99-75f97cb3d7c8')
    return IPortableDeviceServiceActivation
def _define_IPortableDeviceServiceActivation():
    IPortableDeviceServiceActivation = win32more.Devices.PortableDevices.IPortableDeviceServiceActivation_head
    IPortableDeviceServiceActivation.OpenAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head,win32more.Devices.PortableDevices.IPortableDeviceServiceOpenCallback_head, use_last_error=False)(3, 'OpenAsync', ((1, 'pszPnPServiceID'),(1, 'pClientInfo'),(1, 'pCallback'),)))
    IPortableDeviceServiceActivation.CancelOpenAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'CancelOpenAsync', ()))
    return IPortableDeviceServiceActivation
def _define_IPortableDeviceServiceOpenCallback_head():
    class IPortableDeviceServiceOpenCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('bced49c8-8efe-41ed-960b-61313abd47a9')
    return IPortableDeviceServiceOpenCallback
def _define_IPortableDeviceServiceOpenCallback():
    IPortableDeviceServiceOpenCallback = win32more.Devices.PortableDevices.IPortableDeviceServiceOpenCallback_head
    IPortableDeviceServiceOpenCallback.OnComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnComplete', ((1, 'hrStatus'),)))
    return IPortableDeviceServiceOpenCallback
def _define_IPortableDeviceDispatchFactory_head():
    class IPortableDeviceDispatchFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('5e1eafc3-e3d7-4132-96fa-759c0f9d1e0f')
    return IPortableDeviceDispatchFactory
def _define_IPortableDeviceDispatchFactory():
    IPortableDeviceDispatchFactory = win32more.Devices.PortableDevices.IPortableDeviceDispatchFactory_head
    IPortableDeviceDispatchFactory.GetDeviceDispatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(3, 'GetDeviceDispatch', ((1, 'pszPnPDeviceID'),(1, 'ppDeviceDispatch'),)))
    return IPortableDeviceDispatchFactory
def _define_IPortableDeviceWebControl_head():
    class IPortableDeviceWebControl(win32more.System.Com.IDispatch_head):
        Guid = Guid('94fc7953-5ca1-483a-8aee-df52e7747d00')
    return IPortableDeviceWebControl
def _define_IPortableDeviceWebControl():
    IPortableDeviceWebControl = win32more.Devices.PortableDevices.IPortableDeviceWebControl_head
    IPortableDeviceWebControl.GetDeviceFromId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(7, 'GetDeviceFromId', ((1, 'deviceId'),(1, 'ppDevice'),)))
    IPortableDeviceWebControl.GetDeviceFromIdAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(8, 'GetDeviceFromIdAsync', ((1, 'deviceId'),(1, 'pCompletionHandler'),(1, 'pErrorHandler'),)))
    return IPortableDeviceWebControl
EnumBthMtpConnectors = Guid('a1570149-e645-4f43-8b0d-409b061db2fc')
def _define_IEnumPortableDeviceConnectors_head():
    class IEnumPortableDeviceConnectors(win32more.System.Com.IUnknown_head):
        Guid = Guid('bfdef549-9247-454f-bd82-06fe80853faa')
    return IEnumPortableDeviceConnectors
def _define_IEnumPortableDeviceConnectors():
    IEnumPortableDeviceConnectors = win32more.Devices.PortableDevices.IEnumPortableDeviceConnectors_head
    IEnumPortableDeviceConnectors.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.PortableDevices.IPortableDeviceConnector_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cRequested'),(1, 'pConnectors'),(1, 'pcFetched'),)))
    IEnumPortableDeviceConnectors.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cConnectors'),)))
    IEnumPortableDeviceConnectors.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumPortableDeviceConnectors.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IEnumPortableDeviceConnectors_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    return IEnumPortableDeviceConnectors
def _define_IPortableDeviceConnector_head():
    class IPortableDeviceConnector(win32more.System.Com.IUnknown_head):
        Guid = Guid('625e2df8-6392-4cf0-9ad1-3cfa5f17775c')
    return IPortableDeviceConnector
def _define_IPortableDeviceConnector():
    IPortableDeviceConnector = win32more.Devices.PortableDevices.IPortableDeviceConnector_head
    IPortableDeviceConnector.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IConnectionRequestCallback_head, use_last_error=False)(3, 'Connect', ((1, 'pCallback'),)))
    IPortableDeviceConnector.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IConnectionRequestCallback_head, use_last_error=False)(4, 'Disconnect', ((1, 'pCallback'),)))
    IPortableDeviceConnector.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IConnectionRequestCallback_head, use_last_error=False)(5, 'Cancel', ((1, 'pCallback'),)))
    IPortableDeviceConnector.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Properties.DEVPROPKEY_head),POINTER(UInt32),POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(6, 'GetProperty', ((1, 'pPropertyKey'),(1, 'pPropertyType'),(1, 'ppData'),(1, 'pcbData'),)))
    IPortableDeviceConnector.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Properties.DEVPROPKEY_head),UInt32,POINTER(Byte),UInt32, use_last_error=False)(7, 'SetProperty', ((1, 'pPropertyKey'),(1, 'PropertyType'),(1, 'pData'),(1, 'cbData'),)))
    IPortableDeviceConnector.GetPnPID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(8, 'GetPnPID', ((1, 'ppwszPnPID'),)))
    return IPortableDeviceConnector
def _define_IConnectionRequestCallback_head():
    class IConnectionRequestCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('272c9ae0-7161-4ae0-91bd-9f448ee9c427')
    return IConnectionRequestCallback
def _define_IConnectionRequestCallback():
    IConnectionRequestCallback = win32more.Devices.PortableDevices.IConnectionRequestCallback_head
    IConnectionRequestCallback.OnComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnComplete', ((1, 'hrStatus'),)))
    return IConnectionRequestCallback
DEVICE_RADIO_STATE = Int32
DRS_RADIO_ON = 0
DRS_SW_RADIO_OFF = 1
DRS_HW_RADIO_OFF = 2
DRS_SW_HW_RADIO_OFF = 3
DRS_HW_RADIO_ON_UNCONTROLLABLE = 4
DRS_RADIO_INVALID = 5
DRS_HW_RADIO_OFF_UNCONTROLLABLE = 6
DRS_RADIO_MAX = 6
SYSTEM_RADIO_STATE = Int32
SRS_RADIO_ENABLED = 0
SRS_RADIO_DISABLED = 1
def _define_IMediaRadioManager_head():
    class IMediaRadioManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('6cfdcab5-fc47-42a5-9241-074b58830e73')
    return IMediaRadioManager
def _define_IMediaRadioManager():
    IMediaRadioManager = win32more.Devices.PortableDevices.IMediaRadioManager_head
    IMediaRadioManager.GetRadioInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IRadioInstanceCollection_head), use_last_error=False)(3, 'GetRadioInstances', ((1, 'ppCollection'),)))
    IMediaRadioManager.OnSystemRadioStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.SYSTEM_RADIO_STATE,UInt32, use_last_error=False)(4, 'OnSystemRadioStateChange', ((1, 'sysRadioState'),(1, 'uTimeoutSec'),)))
    return IMediaRadioManager
def _define_IRadioInstanceCollection_head():
    class IRadioInstanceCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('e5791fae-5665-4e0c-95be-5fde31644185')
    return IRadioInstanceCollection
def _define_IRadioInstanceCollection():
    IRadioInstanceCollection = win32more.Devices.PortableDevices.IRadioInstanceCollection_head
    IRadioInstanceCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pcInstance'),)))
    IRadioInstanceCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.PortableDevices.IRadioInstance_head), use_last_error=False)(4, 'GetAt', ((1, 'uIndex'),(1, 'ppRadioInstance'),)))
    return IRadioInstanceCollection
def _define_IRadioInstance_head():
    class IRadioInstance(win32more.System.Com.IUnknown_head):
        Guid = Guid('70aa1c9e-f2b4-4c61-86d3-6b9fb75fd1a2')
    return IRadioInstance
def _define_IRadioInstance():
    IRadioInstance = win32more.Devices.PortableDevices.IRadioInstance_head
    IRadioInstance.GetRadioManagerSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetRadioManagerSignature', ((1, 'pguidSignature'),)))
    IRadioInstance.GetInstanceSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetInstanceSignature', ((1, 'pbstrId'),)))
    IRadioInstance.GetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'GetFriendlyName', ((1, 'lcid'),(1, 'pbstrName'),)))
    IRadioInstance.GetRadioState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.DEVICE_RADIO_STATE), use_last_error=False)(6, 'GetRadioState', ((1, 'pRadioState'),)))
    IRadioInstance.SetRadioState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.DEVICE_RADIO_STATE,UInt32, use_last_error=False)(7, 'SetRadioState', ((1, 'radioState'),(1, 'uTimeoutSec'),)))
    IRadioInstance.IsMultiComm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(8, 'IsMultiComm', ()))
    IRadioInstance.IsAssociatingDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(9, 'IsAssociatingDevice', ()))
    return IRadioInstance
def _define_IMediaRadioManagerNotifySink_head():
    class IMediaRadioManagerNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('89d81f5f-c147-49ed-a11c-77b20c31e7c9')
    return IMediaRadioManagerNotifySink
def _define_IMediaRadioManagerNotifySink():
    IMediaRadioManagerNotifySink = win32more.Devices.PortableDevices.IMediaRadioManagerNotifySink_head
    IMediaRadioManagerNotifySink.OnInstanceAdd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IRadioInstance_head, use_last_error=False)(3, 'OnInstanceAdd', ((1, 'pRadioInstance'),)))
    IMediaRadioManagerNotifySink.OnInstanceRemove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(4, 'OnInstanceRemove', ((1, 'bstrRadioInstanceId'),)))
    IMediaRadioManagerNotifySink.OnInstanceRadioChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Devices.PortableDevices.DEVICE_RADIO_STATE, use_last_error=False)(5, 'OnInstanceRadioChange', ((1, 'bstrRadioInstanceId'),(1, 'radioState'),)))
    return IMediaRadioManagerNotifySink
def _define_DMProcessConfigXMLFiltered():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("DMProcessConfigXMLFiltered", windll["DMProcessXMLFiltered"]), ((1, 'pszXmlIn'),(1, 'rgszAllowedCspNodes'),(1, 'dwNumAllowedCspNodes'),(1, 'pbstrXmlOut'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DEVPKEY_MTPBTH_IsConnected",
    "GUID_DEVINTERFACE_WPD",
    "GUID_DEVINTERFACE_WPD_PRIVATE",
    "GUID_DEVINTERFACE_WPD_SERVICE",
    "WPD_CONTROL_FUNCTION_GENERIC_MESSAGE",
    "IOCTL_WPD_MESSAGE_READWRITE_ACCESS",
    "IOCTL_WPD_MESSAGE_READ_ACCESS",
    "FACILITY_WPD",
    "E_WPD_DEVICE_ALREADY_OPENED",
    "E_WPD_DEVICE_NOT_OPEN",
    "E_WPD_OBJECT_ALREADY_ATTACHED_TO_DEVICE",
    "E_WPD_OBJECT_NOT_ATTACHED_TO_DEVICE",
    "E_WPD_OBJECT_NOT_COMMITED",
    "E_WPD_DEVICE_IS_HUNG",
    "E_WPD_SMS_INVALID_RECIPIENT",
    "E_WPD_SMS_INVALID_MESSAGE_BODY",
    "E_WPD_SMS_SERVICE_UNAVAILABLE",
    "E_WPD_SERVICE_ALREADY_OPENED",
    "E_WPD_SERVICE_NOT_OPEN",
    "E_WPD_OBJECT_ALREADY_ATTACHED_TO_SERVICE",
    "E_WPD_OBJECT_NOT_ATTACHED_TO_SERVICE",
    "E_WPD_SERVICE_BAD_PARAMETER_ORDER",
    "WPD_EVENT_NOTIFICATION",
    "WPD_EVENT_OBJECT_ADDED",
    "WPD_EVENT_OBJECT_REMOVED",
    "WPD_EVENT_OBJECT_UPDATED",
    "WPD_EVENT_DEVICE_RESET",
    "WPD_EVENT_DEVICE_CAPABILITIES_UPDATED",
    "WPD_EVENT_STORAGE_FORMAT",
    "WPD_EVENT_OBJECT_TRANSFER_REQUESTED",
    "WPD_EVENT_DEVICE_REMOVED",
    "WPD_EVENT_SERVICE_METHOD_COMPLETE",
    "WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT",
    "WPD_CONTENT_TYPE_FOLDER",
    "WPD_CONTENT_TYPE_IMAGE",
    "WPD_CONTENT_TYPE_DOCUMENT",
    "WPD_CONTENT_TYPE_CONTACT",
    "WPD_CONTENT_TYPE_CONTACT_GROUP",
    "WPD_CONTENT_TYPE_AUDIO",
    "WPD_CONTENT_TYPE_VIDEO",
    "WPD_CONTENT_TYPE_TELEVISION",
    "WPD_CONTENT_TYPE_PLAYLIST",
    "WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM",
    "WPD_CONTENT_TYPE_AUDIO_ALBUM",
    "WPD_CONTENT_TYPE_IMAGE_ALBUM",
    "WPD_CONTENT_TYPE_VIDEO_ALBUM",
    "WPD_CONTENT_TYPE_MEMO",
    "WPD_CONTENT_TYPE_EMAIL",
    "WPD_CONTENT_TYPE_APPOINTMENT",
    "WPD_CONTENT_TYPE_TASK",
    "WPD_CONTENT_TYPE_PROGRAM",
    "WPD_CONTENT_TYPE_GENERIC_FILE",
    "WPD_CONTENT_TYPE_CALENDAR",
    "WPD_CONTENT_TYPE_GENERIC_MESSAGE",
    "WPD_CONTENT_TYPE_NETWORK_ASSOCIATION",
    "WPD_CONTENT_TYPE_CERTIFICATE",
    "WPD_CONTENT_TYPE_WIRELESS_PROFILE",
    "WPD_CONTENT_TYPE_MEDIA_CAST",
    "WPD_CONTENT_TYPE_SECTION",
    "WPD_CONTENT_TYPE_UNSPECIFIED",
    "WPD_CONTENT_TYPE_ALL",
    "WPD_FUNCTIONAL_CATEGORY_DEVICE",
    "WPD_FUNCTIONAL_CATEGORY_STORAGE",
    "WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE",
    "WPD_FUNCTIONAL_CATEGORY_AUDIO_CAPTURE",
    "WPD_FUNCTIONAL_CATEGORY_VIDEO_CAPTURE",
    "WPD_FUNCTIONAL_CATEGORY_SMS",
    "WPD_FUNCTIONAL_CATEGORY_RENDERING_INFORMATION",
    "WPD_FUNCTIONAL_CATEGORY_NETWORK_CONFIGURATION",
    "WPD_FUNCTIONAL_CATEGORY_ALL",
    "WPD_OBJECT_FORMAT_ICON",
    "WPD_OBJECT_FORMAT_M4A",
    "WPD_OBJECT_FORMAT_NETWORK_ASSOCIATION",
    "WPD_OBJECT_FORMAT_X509V3CERTIFICATE",
    "WPD_OBJECT_FORMAT_MICROSOFT_WFC",
    "WPD_OBJECT_FORMAT_3GPA",
    "WPD_OBJECT_FORMAT_3G2A",
    "WPD_OBJECT_FORMAT_ALL",
    "WPD_CATEGORY_NULL",
    "WPD_OBJECT_PROPERTIES_V1",
    "WPD_OBJECT_PROPERTIES_V2",
    "WPD_FUNCTIONAL_OBJECT_PROPERTIES_V1",
    "WPD_STORAGE_OBJECT_PROPERTIES_V1",
    "WPD_NETWORK_ASSOCIATION_PROPERTIES_V1",
    "WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1",
    "WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1",
    "WPD_CLIENT_INFORMATION_PROPERTIES_V1",
    "WPD_PROPERTY_ATTRIBUTES_V1",
    "WPD_PROPERTY_ATTRIBUTES_V2",
    "WPD_CLASS_EXTENSION_OPTIONS_V1",
    "WPD_CLASS_EXTENSION_OPTIONS_V2",
    "WPD_CLASS_EXTENSION_OPTIONS_V3",
    "WPD_RESOURCE_ATTRIBUTES_V1",
    "WPD_DEVICE_PROPERTIES_V1",
    "WPD_DEVICE_PROPERTIES_V2",
    "WPD_DEVICE_PROPERTIES_V3",
    "WPD_SERVICE_PROPERTIES_V1",
    "WPD_EVENT_PROPERTIES_V1",
    "WPD_EVENT_PROPERTIES_V2",
    "WPD_EVENT_OPTIONS_V1",
    "WPD_EVENT_ATTRIBUTES_V1",
    "WPD_API_OPTIONS_V1",
    "WPD_FORMAT_ATTRIBUTES_V1",
    "WPD_METHOD_ATTRIBUTES_V1",
    "WPD_PARAMETER_ATTRIBUTES_V1",
    "WPD_CATEGORY_COMMON",
    "WPD_CATEGORY_OBJECT_ENUMERATION",
    "WPD_CATEGORY_OBJECT_PROPERTIES",
    "WPD_CATEGORY_OBJECT_PROPERTIES_BULK",
    "WPD_CATEGORY_OBJECT_RESOURCES",
    "WPD_CATEGORY_OBJECT_MANAGEMENT",
    "WPD_CATEGORY_CAPABILITIES",
    "WPD_CATEGORY_STORAGE",
    "WPD_CATEGORY_SMS",
    "WPD_CATEGORY_STILL_IMAGE_CAPTURE",
    "WPD_CATEGORY_MEDIA_CAPTURE",
    "WPD_CATEGORY_DEVICE_HINTS",
    "WPD_CLASS_EXTENSION_V1",
    "WPD_CLASS_EXTENSION_V2",
    "WPD_CATEGORY_NETWORK_CONFIGURATION",
    "WPD_CATEGORY_SERVICE_COMMON",
    "WPD_CATEGORY_SERVICE_CAPABILITIES",
    "WPD_CATEGORY_SERVICE_METHODS",
    "WPD_OBJECT_FORMAT_PROPERTIES_ONLY",
    "WPD_OBJECT_FORMAT_UNSPECIFIED",
    "WPD_OBJECT_FORMAT_SCRIPT",
    "WPD_OBJECT_FORMAT_EXECUTABLE",
    "WPD_OBJECT_FORMAT_TEXT",
    "WPD_OBJECT_FORMAT_HTML",
    "WPD_OBJECT_FORMAT_DPOF",
    "WPD_OBJECT_FORMAT_AIFF",
    "WPD_OBJECT_FORMAT_WAVE",
    "WPD_OBJECT_FORMAT_MP3",
    "WPD_OBJECT_FORMAT_AVI",
    "WPD_OBJECT_FORMAT_MPEG",
    "WPD_OBJECT_FORMAT_ASF",
    "WPD_OBJECT_FORMAT_EXIF",
    "WPD_OBJECT_FORMAT_TIFFEP",
    "WPD_OBJECT_FORMAT_FLASHPIX",
    "WPD_OBJECT_FORMAT_BMP",
    "WPD_OBJECT_FORMAT_CIFF",
    "WPD_OBJECT_FORMAT_GIF",
    "WPD_OBJECT_FORMAT_JFIF",
    "WPD_OBJECT_FORMAT_PCD",
    "WPD_OBJECT_FORMAT_PICT",
    "WPD_OBJECT_FORMAT_PNG",
    "WPD_OBJECT_FORMAT_TIFF",
    "WPD_OBJECT_FORMAT_TIFFIT",
    "WPD_OBJECT_FORMAT_JP2",
    "WPD_OBJECT_FORMAT_JPX",
    "WPD_OBJECT_FORMAT_WBMP",
    "WPD_OBJECT_FORMAT_JPEGXR",
    "WPD_OBJECT_FORMAT_WINDOWSIMAGEFORMAT",
    "WPD_OBJECT_FORMAT_WMA",
    "WPD_OBJECT_FORMAT_WMV",
    "WPD_OBJECT_FORMAT_WPLPLAYLIST",
    "WPD_OBJECT_FORMAT_M3UPLAYLIST",
    "WPD_OBJECT_FORMAT_MPLPLAYLIST",
    "WPD_OBJECT_FORMAT_ASXPLAYLIST",
    "WPD_OBJECT_FORMAT_PLSPLAYLIST",
    "WPD_OBJECT_FORMAT_ABSTRACT_CONTACT_GROUP",
    "WPD_OBJECT_FORMAT_ABSTRACT_MEDIA_CAST",
    "WPD_OBJECT_FORMAT_VCALENDAR1",
    "WPD_OBJECT_FORMAT_ICALENDAR",
    "WPD_OBJECT_FORMAT_ABSTRACT_CONTACT",
    "WPD_OBJECT_FORMAT_VCARD2",
    "WPD_OBJECT_FORMAT_VCARD3",
    "WPD_OBJECT_FORMAT_XML",
    "WPD_OBJECT_FORMAT_AAC",
    "WPD_OBJECT_FORMAT_AUDIBLE",
    "WPD_OBJECT_FORMAT_FLAC",
    "WPD_OBJECT_FORMAT_QCELP",
    "WPD_OBJECT_FORMAT_AMR",
    "WPD_OBJECT_FORMAT_OGG",
    "WPD_OBJECT_FORMAT_MP4",
    "WPD_OBJECT_FORMAT_MP2",
    "WPD_OBJECT_FORMAT_MICROSOFT_WORD",
    "WPD_OBJECT_FORMAT_MHT_COMPILED_HTML",
    "WPD_OBJECT_FORMAT_MICROSOFT_EXCEL",
    "WPD_OBJECT_FORMAT_MICROSOFT_POWERPOINT",
    "WPD_OBJECT_FORMAT_3GP",
    "WPD_OBJECT_FORMAT_3G2",
    "WPD_OBJECT_FORMAT_AVCHD",
    "WPD_OBJECT_FORMAT_ATSCTS",
    "WPD_OBJECT_FORMAT_DVBTS",
    "WPD_OBJECT_FORMAT_MKV",
    "WPD_FOLDER_OBJECT_PROPERTIES_V1",
    "WPD_IMAGE_OBJECT_PROPERTIES_V1",
    "WPD_DOCUMENT_OBJECT_PROPERTIES_V1",
    "WPD_MEDIA_PROPERTIES_V1",
    "WPD_CONTACT_OBJECT_PROPERTIES_V1",
    "WPD_MUSIC_OBJECT_PROPERTIES_V1",
    "WPD_VIDEO_OBJECT_PROPERTIES_V1",
    "WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1",
    "WPD_MEMO_OBJECT_PROPERTIES_V1",
    "WPD_EMAIL_OBJECT_PROPERTIES_V1",
    "WPD_APPOINTMENT_OBJECT_PROPERTIES_V1",
    "WPD_TASK_OBJECT_PROPERTIES_V1",
    "WPD_SMS_OBJECT_PROPERTIES_V1",
    "WPD_SECTION_OBJECT_PROPERTIES_V1",
    "DEVSVC_SERVICEINFO_VERSION",
    "DEVSVCTYPE_DEFAULT",
    "DEVSVCTYPE_ABSTRACT",
    "TYPE_CalendarSvc",
    "ENUM_CalendarObj_BusyStatusFree",
    "ENUM_CalendarObj_BusyStatusBusy",
    "ENUM_CalendarObj_BusyStatusOutOfOffice",
    "ENUM_CalendarObj_BusyStatusTentative",
    "TYPE_HintsSvc",
    "TYPE_MessageSvc",
    "ENUM_MessageObj_PriorityHighest",
    "ENUM_MessageObj_PriorityNormal",
    "ENUM_MessageObj_PriorityLowest",
    "ENUM_MessageObj_ReadFalse",
    "ENUM_MessageObj_ReadTrue",
    "ENUM_MessageObj_PatternTypeDaily",
    "ENUM_MessageObj_PatternTypeWeekly",
    "ENUM_MessageObj_PatternTypeMonthly",
    "ENUM_MessageObj_PatternTypeYearly",
    "FLAG_MessageObj_DayOfWeekNone",
    "FLAG_MessageObj_DayOfWeekSunday",
    "FLAG_MessageObj_DayOfWeekMonday",
    "FLAG_MessageObj_DayOfWeekTuesday",
    "FLAG_MessageObj_DayOfWeekWednesday",
    "FLAG_MessageObj_DayOfWeekThursday",
    "FLAG_MessageObj_DayOfWeekFriday",
    "FLAG_MessageObj_DayOfWeekSaturday",
    "RANGEMIN_MessageObj_PatternDayOfMonth",
    "RANGEMAX_MessageObj_PatternDayOfMonth",
    "RANGESTEP_MessageObj_PatternDayOfMonth",
    "RANGEMIN_MessageObj_PatternMonthOfYear",
    "RANGEMAX_MessageObj_PatternMonthOfYear",
    "RANGESTEP_MessageObj_PatternMonthOfYear",
    "ENUM_MessageObj_PatternInstanceNone",
    "ENUM_MessageObj_PatternInstanceFirst",
    "ENUM_MessageObj_PatternInstanceSecond",
    "ENUM_MessageObj_PatternInstanceThird",
    "ENUM_MessageObj_PatternInstanceFourth",
    "ENUM_MessageObj_PatternInstanceLast",
    "TYPE_DeviceMetadataSvc",
    "ENUM_DeviceMetadataObj_DefaultCABFalse",
    "ENUM_DeviceMetadataObj_DefaultCABTrue",
    "TYPE_NotesSvc",
    "TYPE_StatusSvc",
    "RANGEMIN_StatusSvc_SignalStrength",
    "RANGEMAX_StatusSvc_SignalStrength",
    "RANGESTEP_StatusSvc_SignalStrength",
    "RANGEMAX_StatusSvc_TextMessages",
    "RANGEMAX_StatusSvc_NewPictures",
    "RANGEMAX_StatusSvc_MissedCalls",
    "RANGEMAX_StatusSvc_VoiceMail",
    "ENUM_StatusSvc_RoamingInactive",
    "ENUM_StatusSvc_RoamingActive",
    "ENUM_StatusSvc_RoamingUnknown",
    "RANGEMIN_StatusSvc_BatteryLife",
    "RANGEMAX_StatusSvc_BatteryLife",
    "RANGESTEP_StatusSvc_BatteryLife",
    "ENUM_StatusSvc_ChargingInactive",
    "ENUM_StatusSvc_ChargingActive",
    "ENUM_StatusSvc_ChargingUnknown",
    "SYNCSVC_FILTER_NONE",
    "SYNCSVC_FILTER_CONTACTS_WITH_PHONE",
    "SYNCSVC_FILTER_TASK_ACTIVE",
    "SYNCSVC_FILTER_CALENDAR_WINDOW_WITH_RECURRENCE",
    "ENUM_SyncSvc_SyncObjectReferencesDisabled",
    "ENUM_SyncSvc_SyncObjectReferencesEnabled",
    "TYPE_TasksSvc",
    "ENUM_TaskObj_CompleteFalse",
    "ENUM_TaskObj_CompleteTrue",
    "WPD_CATEGORY_MTP_EXT_VENDOR_OPERATIONS",
    "WPD_PROPERTIES_MTP_VENDOR_EXTENDED_OBJECT_PROPS",
    "WPD_PROPERTIES_MTP_VENDOR_EXTENDED_DEVICE_PROPS",
    "WPD_EVENT_MTP_VENDOR_EXTENDED_EVENTS",
    "CLSID_WPD_NAMESPACE_EXTENSION",
    "WPDNSE_OBJECT_PROPERTIES_V1",
    "WPDNSE_PROPSHEET_DEVICE_GENERAL",
    "WPDNSE_PROPSHEET_STORAGE_GENERAL",
    "WPDNSE_PROPSHEET_CONTENT_GENERAL",
    "WPDNSE_PROPSHEET_CONTENT_REFERENCES",
    "WPDNSE_PROPSHEET_CONTENT_RESOURCES",
    "WPDNSE_PROPSHEET_CONTENT_DETAILS",
    "TYPE_ContactsSvc",
    "TYPE_RingtonesSvc",
    "TYPE_AnchorSyncSvc",
    "ENUM_AnchorResults_AnchorStateNormal",
    "ENUM_AnchorResults_AnchorStateInvalid",
    "ENUM_AnchorResults_AnchorStateOld",
    "ENUM_AnchorResults_ItemStateInvalid",
    "ENUM_AnchorResults_ItemStateDeleted",
    "ENUM_AnchorResults_ItemStateCreated",
    "ENUM_AnchorResults_ItemStateUpdated",
    "ENUM_AnchorResults_ItemStateChanged",
    "TYPE_FullEnumSyncSvc",
    "DELETE_OBJECT_OPTIONS",
    "PORTABLE_DEVICE_DELETE_NO_RECURSION",
    "PORTABLE_DEVICE_DELETE_WITH_RECURSION",
    "WPD_DEVICE_TYPES",
    "WPD_DEVICE_TYPE_GENERIC",
    "WPD_DEVICE_TYPE_CAMERA",
    "WPD_DEVICE_TYPE_MEDIA_PLAYER",
    "WPD_DEVICE_TYPE_PHONE",
    "WPD_DEVICE_TYPE_VIDEO",
    "WPD_DEVICE_TYPE_PERSONAL_INFORMATION_MANAGER",
    "WPD_DEVICE_TYPE_AUDIO_RECORDER",
    "WpdAttributeForm",
    "WPD_PROPERTY_ATTRIBUTE_FORM_UNSPECIFIED",
    "WPD_PROPERTY_ATTRIBUTE_FORM_RANGE",
    "WPD_PROPERTY_ATTRIBUTE_FORM_ENUMERATION",
    "WPD_PROPERTY_ATTRIBUTE_FORM_REGULAR_EXPRESSION",
    "WPD_PROPERTY_ATTRIBUTE_FORM_OBJECT_IDENTIFIER",
    "WpdParameterAttributeForm",
    "WPD_PARAMETER_ATTRIBUTE_FORM_UNSPECIFIED",
    "WPD_PARAMETER_ATTRIBUTE_FORM_RANGE",
    "WPD_PARAMETER_ATTRIBUTE_FORM_ENUMERATION",
    "WPD_PARAMETER_ATTRIBUTE_FORM_REGULAR_EXPRESSION",
    "WPD_PARAMETER_ATTRIBUTE_FORM_OBJECT_IDENTIFIER",
    "WPD_DEVICE_TRANSPORTS",
    "WPD_DEVICE_TRANSPORT_UNSPECIFIED",
    "WPD_DEVICE_TRANSPORT_USB",
    "WPD_DEVICE_TRANSPORT_IP",
    "WPD_DEVICE_TRANSPORT_BLUETOOTH",
    "WPD_STORAGE_TYPE_VALUES",
    "WPD_STORAGE_TYPE_UNDEFINED",
    "WPD_STORAGE_TYPE_FIXED_ROM",
    "WPD_STORAGE_TYPE_REMOVABLE_ROM",
    "WPD_STORAGE_TYPE_FIXED_RAM",
    "WPD_STORAGE_TYPE_REMOVABLE_RAM",
    "WPD_STORAGE_ACCESS_CAPABILITY_VALUES",
    "WPD_STORAGE_ACCESS_CAPABILITY_READWRITE",
    "WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITHOUT_OBJECT_DELETION",
    "WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITH_OBJECT_DELETION",
    "WPD_SMS_ENCODING_TYPES",
    "SMS_ENCODING_7_BIT",
    "SMS_ENCODING_8_BIT",
    "SMS_ENCODING_UTF_16",
    "SMS_MESSAGE_TYPES",
    "SMS_TEXT_MESSAGE",
    "SMS_BINARY_MESSAGE",
    "WPD_POWER_SOURCES",
    "WPD_POWER_SOURCE_BATTERY",
    "WPD_POWER_SOURCE_EXTERNAL",
    "WPD_WHITE_BALANCE_SETTINGS",
    "WPD_WHITE_BALANCE_UNDEFINED",
    "WPD_WHITE_BALANCE_MANUAL",
    "WPD_WHITE_BALANCE_AUTOMATIC",
    "WPD_WHITE_BALANCE_ONE_PUSH_AUTOMATIC",
    "WPD_WHITE_BALANCE_DAYLIGHT",
    "WPD_WHITE_BALANCE_FLORESCENT",
    "WPD_WHITE_BALANCE_TUNGSTEN",
    "WPD_WHITE_BALANCE_FLASH",
    "WPD_FOCUS_MODES",
    "WPD_FOCUS_UNDEFINED",
    "WPD_FOCUS_MANUAL",
    "WPD_FOCUS_AUTOMATIC",
    "WPD_FOCUS_AUTOMATIC_MACRO",
    "WPD_EXPOSURE_METERING_MODES",
    "WPD_EXPOSURE_METERING_MODE_UNDEFINED",
    "WPD_EXPOSURE_METERING_MODE_AVERAGE",
    "WPD_EXPOSURE_METERING_MODE_CENTER_WEIGHTED_AVERAGE",
    "WPD_EXPOSURE_METERING_MODE_MULTI_SPOT",
    "WPD_EXPOSURE_METERING_MODE_CENTER_SPOT",
    "WPD_FLASH_MODES",
    "WPD_FLASH_MODE_UNDEFINED",
    "WPD_FLASH_MODE_AUTO",
    "WPD_FLASH_MODE_OFF",
    "WPD_FLASH_MODE_FILL",
    "WPD_FLASH_MODE_RED_EYE_AUTO",
    "WPD_FLASH_MODE_RED_EYE_FILL",
    "WPD_FLASH_MODE_EXTERNAL_SYNC",
    "WPD_EXPOSURE_PROGRAM_MODES",
    "WPD_EXPOSURE_PROGRAM_MODE_UNDEFINED",
    "WPD_EXPOSURE_PROGRAM_MODE_MANUAL",
    "WPD_EXPOSURE_PROGRAM_MODE_AUTO",
    "WPD_EXPOSURE_PROGRAM_MODE_APERTURE_PRIORITY",
    "WPD_EXPOSURE_PROGRAM_MODE_SHUTTER_PRIORITY",
    "WPD_EXPOSURE_PROGRAM_MODE_CREATIVE",
    "WPD_EXPOSURE_PROGRAM_MODE_ACTION",
    "WPD_EXPOSURE_PROGRAM_MODE_PORTRAIT",
    "WPD_CAPTURE_MODES",
    "WPD_CAPTURE_MODE_UNDEFINED",
    "WPD_CAPTURE_MODE_NORMAL",
    "WPD_CAPTURE_MODE_BURST",
    "WPD_CAPTURE_MODE_TIMELAPSE",
    "WPD_EFFECT_MODES",
    "WPD_EFFECT_MODE_UNDEFINED",
    "WPD_EFFECT_MODE_COLOR",
    "WPD_EFFECT_MODE_BLACK_AND_WHITE",
    "WPD_EFFECT_MODE_SEPIA",
    "WPD_FOCUS_METERING_MODES",
    "WPD_FOCUS_METERING_MODE_UNDEFINED",
    "WPD_FOCUS_METERING_MODE_CENTER_SPOT",
    "WPD_FOCUS_METERING_MODE_MULTI_SPOT",
    "WPD_BITRATE_TYPES",
    "WPD_BITRATE_TYPE_UNUSED",
    "WPD_BITRATE_TYPE_DISCRETE",
    "WPD_BITRATE_TYPE_VARIABLE",
    "WPD_BITRATE_TYPE_FREE",
    "WPD_META_GENRES",
    "WPD_META_GENRE_UNUSED",
    "WPD_META_GENRE_GENERIC_MUSIC_AUDIO_FILE",
    "WPD_META_GENRE_GENERIC_NON_MUSIC_AUDIO_FILE",
    "WPD_META_GENRE_SPOKEN_WORD_AUDIO_BOOK_FILES",
    "WPD_META_GENRE_SPOKEN_WORD_FILES_NON_AUDIO_BOOK",
    "WPD_META_GENRE_SPOKEN_WORD_NEWS",
    "WPD_META_GENRE_SPOKEN_WORD_TALK_SHOWS",
    "WPD_META_GENRE_GENERIC_VIDEO_FILE",
    "WPD_META_GENRE_NEWS_VIDEO_FILE",
    "WPD_META_GENRE_MUSIC_VIDEO_FILE",
    "WPD_META_GENRE_HOME_VIDEO_FILE",
    "WPD_META_GENRE_FEATURE_FILM_VIDEO_FILE",
    "WPD_META_GENRE_TELEVISION_VIDEO_FILE",
    "WPD_META_GENRE_TRAINING_EDUCATIONAL_VIDEO_FILE",
    "WPD_META_GENRE_PHOTO_MONTAGE_VIDEO_FILE",
    "WPD_META_GENRE_GENERIC_NON_AUDIO_NON_VIDEO",
    "WPD_META_GENRE_AUDIO_PODCAST",
    "WPD_META_GENRE_VIDEO_PODCAST",
    "WPD_META_GENRE_MIXED_PODCAST",
    "WPD_CROPPED_STATUS_VALUES",
    "WPD_CROPPED_STATUS_NOT_CROPPED",
    "WPD_CROPPED_STATUS_CROPPED",
    "WPD_CROPPED_STATUS_SHOULD_NOT_BE_CROPPED",
    "WPD_COLOR_CORRECTED_STATUS_VALUES",
    "WPD_COLOR_CORRECTED_STATUS_NOT_CORRECTED",
    "WPD_COLOR_CORRECTED_STATUS_CORRECTED",
    "WPD_COLOR_CORRECTED_STATUS_SHOULD_NOT_BE_CORRECTED",
    "WPD_VIDEO_SCAN_TYPES",
    "WPD_VIDEO_SCAN_TYPE_UNUSED",
    "WPD_VIDEO_SCAN_TYPE_PROGRESSIVE",
    "WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_UPPER_FIRST",
    "WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_LOWER_FIRST",
    "WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_UPPER_FIRST",
    "WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_LOWER_FIRST",
    "WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE",
    "WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE_AND_PROGRESSIVE",
    "WPD_OPERATION_STATES",
    "WPD_OPERATION_STATE_UNSPECIFIED",
    "WPD_OPERATION_STATE_STARTED",
    "WPD_OPERATION_STATE_RUNNING",
    "WPD_OPERATION_STATE_PAUSED",
    "WPD_OPERATION_STATE_CANCELLED",
    "WPD_OPERATION_STATE_FINISHED",
    "WPD_OPERATION_STATE_ABORTED",
    "WPD_SECTION_DATA_UNITS_VALUES",
    "WPD_SECTION_DATA_UNITS_BYTES",
    "WPD_SECTION_DATA_UNITS_MILLISECONDS",
    "WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES",
    "WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_OBJECT",
    "WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_RESOURCE",
    "WPD_COMMAND_ACCESS_TYPES",
    "WPD_COMMAND_ACCESS_READ",
    "WPD_COMMAND_ACCESS_READWRITE",
    "WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_STGM_ACCESS",
    "WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_FILE_ACCESS",
    "WPD_COMMAND_ACCESS_FROM_ATTRIBUTE_WITH_METHOD_ACCESS",
    "WPD_SERVICE_INHERITANCE_TYPES",
    "WPD_SERVICE_INHERITANCE_IMPLEMENTATION",
    "WPD_PARAMETER_USAGE_TYPES",
    "WPD_PARAMETER_USAGE_RETURN",
    "WPD_PARAMETER_USAGE_IN",
    "WPD_PARAMETER_USAGE_OUT",
    "WPD_PARAMETER_USAGE_INOUT",
    "WPD_COMMAND_ACCESS_LOOKUP_ENTRY",
    "WpdSerializer",
    "PortableDeviceValues",
    "PortableDeviceKeyCollection",
    "PortableDevicePropVariantCollection",
    "PortableDeviceValuesCollection",
    "WPD_STREAM_UNITS",
    "WPD_STREAM_UNITS_BYTES",
    "WPD_STREAM_UNITS_FRAMES",
    "WPD_STREAM_UNITS_ROWS",
    "WPD_STREAM_UNITS_MILLISECONDS",
    "WPD_STREAM_UNITS_MICROSECONDS",
    "IWpdSerializer",
    "IPortableDeviceValues",
    "IPortableDeviceKeyCollection",
    "IPortableDevicePropVariantCollection",
    "IPortableDeviceValuesCollection",
    "PortableDevice",
    "PortableDeviceManager",
    "PortableDeviceService",
    "PortableDeviceDispatchFactory",
    "PortableDeviceFTM",
    "PortableDeviceServiceFTM",
    "PortableDeviceWebControl",
    "IPortableDeviceManager",
    "IPortableDevice",
    "IPortableDeviceContent",
    "IPortableDeviceContent2",
    "IEnumPortableDeviceObjectIDs",
    "IPortableDeviceProperties",
    "IPortableDeviceResources",
    "IPortableDeviceCapabilities",
    "IPortableDeviceEventCallback",
    "IPortableDeviceDataStream",
    "IPortableDeviceUnitsStream",
    "IPortableDevicePropertiesBulk",
    "IPortableDevicePropertiesBulkCallback",
    "IPortableDeviceServiceManager",
    "IPortableDeviceService",
    "IPortableDeviceServiceCapabilities",
    "IPortableDeviceServiceMethods",
    "IPortableDeviceServiceMethodCallback",
    "IPortableDeviceServiceActivation",
    "IPortableDeviceServiceOpenCallback",
    "IPortableDeviceDispatchFactory",
    "IPortableDeviceWebControl",
    "EnumBthMtpConnectors",
    "IEnumPortableDeviceConnectors",
    "IPortableDeviceConnector",
    "IConnectionRequestCallback",
    "DEVICE_RADIO_STATE",
    "DRS_RADIO_ON",
    "DRS_SW_RADIO_OFF",
    "DRS_HW_RADIO_OFF",
    "DRS_SW_HW_RADIO_OFF",
    "DRS_HW_RADIO_ON_UNCONTROLLABLE",
    "DRS_RADIO_INVALID",
    "DRS_HW_RADIO_OFF_UNCONTROLLABLE",
    "DRS_RADIO_MAX",
    "SYSTEM_RADIO_STATE",
    "SRS_RADIO_ENABLED",
    "SRS_RADIO_DISABLED",
    "IMediaRadioManager",
    "IRadioInstanceCollection",
    "IRadioInstance",
    "IMediaRadioManagerNotifySink",
    "DMProcessConfigXMLFiltered",
]
