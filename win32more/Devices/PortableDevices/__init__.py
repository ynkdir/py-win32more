from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
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
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_DEVPKEY_MTPBTH_IsConnected():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('ea1237fa-589d-4472-84-e4-0a-be-36-fd-62-ef'), pid=2)
def _define_GUID_DEVINTERFACE_WPD():
    return Guid('6ac27878-a6fa-4155-ba-85-f9-8f-49-1d-4f-33')
def _define_GUID_DEVINTERFACE_WPD_PRIVATE():
    return Guid('ba0c718f-4ded-49b7-bd-d3-fa-be-28-66-12-11')
def _define_GUID_DEVINTERFACE_WPD_SERVICE():
    return Guid('9ef44f80-3d64-4246-a6-aa-20-6f-32-8d-1e-dc')
WPD_CONTROL_FUNCTION_GENERIC_MESSAGE = 66
IOCTL_WPD_MESSAGE_READWRITE_ACCESS = 4243720
IOCTL_WPD_MESSAGE_READ_ACCESS = 4210952
WPD_DEVICE_OBJECT_ID = 'DEVICE'
PORTABLE_DEVICE_TYPE = 'PortableDeviceType'
PORTABLE_DEVICE_ICON = 'Icons'
PORTABLE_DEVICE_NAMESPACE_TIMEOUT = 'PortableDeviceNameSpaceTimeout'
PORTABLE_DEVICE_NAMESPACE_EXCLUDE_FROM_SHELL = 'PortableDeviceNameSpaceExcludeFromShell'
PORTABLE_DEVICE_NAMESPACE_THUMBNAIL_CONTENT_TYPES = 'PortableDeviceNameSpaceThumbnailContentTypes'
PORTABLE_DEVICE_IS_MASS_STORAGE = 'PortableDeviceIsMassStorage'
PORTABLE_DEVICE_DRM_SCHEME_WMDRM10_PD = 'WMDRM10-PD'
PORTABLE_DEVICE_DRM_SCHEME_PDDRM = 'PDDRM'
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
def _define_WPD_EVENT_NOTIFICATION():
    return Guid('2ba2e40a-6b4c-4295-bb-43-26-32-2b-99-ae-b2')
def _define_WPD_EVENT_OBJECT_ADDED():
    return Guid('a726da95-e207-4b02-8d-44-be-f2-e8-6c-bf-fc')
def _define_WPD_EVENT_OBJECT_REMOVED():
    return Guid('be82ab88-a52c-4823-96-e5-d0-27-26-71-fc-38')
def _define_WPD_EVENT_OBJECT_UPDATED():
    return Guid('1445a759-2e01-485d-9f-27-ff-07-da-e6-97-ab')
def _define_WPD_EVENT_DEVICE_RESET():
    return Guid('7755cf53-c1ed-44f3-b5-a2-45-1e-2c-37-6b-27')
def _define_WPD_EVENT_DEVICE_CAPABILITIES_UPDATED():
    return Guid('36885aa1-cd54-4daa-b3-d0-af-b3-e0-3f-59-99')
def _define_WPD_EVENT_STORAGE_FORMAT():
    return Guid('3782616b-22bc-4474-a2-51-30-70-f8-d3-88-57')
def _define_WPD_EVENT_OBJECT_TRANSFER_REQUESTED():
    return Guid('8d16a0a1-f2c6-41da-8f-19-5e-53-72-1a-db-f2')
def _define_WPD_EVENT_DEVICE_REMOVED():
    return Guid('e4cbca1b-6918-48b9-85-ee-02-be-7c-85-0a-f9')
def _define_WPD_EVENT_SERVICE_METHOD_COMPLETE():
    return Guid('8a33f5f8-0acc-4d9b-9c-c4-11-2d-35-3b-86-ca')
def _define_WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT():
    return Guid('99ed0160-17ff-4c44-9d-98-1d-7a-6f-94-19-21')
def _define_WPD_CONTENT_TYPE_FOLDER():
    return Guid('27e2e392-a111-48e0-ab-0c-e1-77-05-a0-5f-85')
def _define_WPD_CONTENT_TYPE_IMAGE():
    return Guid('ef2107d5-a52a-4243-a2-6b-62-d4-17-6d-76-03')
def _define_WPD_CONTENT_TYPE_DOCUMENT():
    return Guid('680adf52-950a-4041-9b-41-65-e3-93-64-81-55')
def _define_WPD_CONTENT_TYPE_CONTACT():
    return Guid('eaba8313-4525-4707-9f-0e-87-c6-80-8e-94-35')
def _define_WPD_CONTENT_TYPE_CONTACT_GROUP():
    return Guid('346b8932-4c36-40d8-94-15-18-28-29-1f-9d-e9')
def _define_WPD_CONTENT_TYPE_AUDIO():
    return Guid('4ad2c85e-5e2d-45e5-88-64-4f-22-9e-3c-6c-f0')
def _define_WPD_CONTENT_TYPE_VIDEO():
    return Guid('9261b03c-3d78-4519-85-e3-02-c5-e1-f5-0b-b9')
def _define_WPD_CONTENT_TYPE_TELEVISION():
    return Guid('60a169cf-f2ae-4e21-93-75-96-77-f1-1c-1c-6e')
def _define_WPD_CONTENT_TYPE_PLAYLIST():
    return Guid('1a33f7e4-af13-48f5-99-4e-77-36-9d-fe-04-a3')
def _define_WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM():
    return Guid('00f0c3ac-a593-49ac-92-19-24-ab-ca-5a-25-63')
def _define_WPD_CONTENT_TYPE_AUDIO_ALBUM():
    return Guid('aa18737e-5009-48fa-ae-21-85-f2-43-83-b4-e6')
def _define_WPD_CONTENT_TYPE_IMAGE_ALBUM():
    return Guid('75793148-15f5-4a30-a8-13-54-ed-8a-37-e2-26')
def _define_WPD_CONTENT_TYPE_VIDEO_ALBUM():
    return Guid('012b0db7-d4c1-45d6-b0-81-94-b8-77-79-61-4f')
def _define_WPD_CONTENT_TYPE_MEMO():
    return Guid('9cd20ecf-3b50-414f-a6-41-e4-73-ff-e4-57-51')
def _define_WPD_CONTENT_TYPE_EMAIL():
    return Guid('8038044a-7e51-4f8f-88-3d-1d-06-23-d1-45-33')
def _define_WPD_CONTENT_TYPE_APPOINTMENT():
    return Guid('0fed060e-8793-4b1e-90-c9-48-ac-38-9a-c6-31')
def _define_WPD_CONTENT_TYPE_TASK():
    return Guid('63252f2c-887f-4cb6-b1-ac-d2-98-55-dc-ef-6c')
def _define_WPD_CONTENT_TYPE_PROGRAM():
    return Guid('d269f96a-247c-4bff-98-fb-97-f3-c4-92-20-e6')
def _define_WPD_CONTENT_TYPE_GENERIC_FILE():
    return Guid('0085e0a6-8d34-45d7-bc-5c-44-7e-59-c7-3d-48')
def _define_WPD_CONTENT_TYPE_CALENDAR():
    return Guid('a1fd5967-6023-49a0-9d-f1-f8-06-0b-e7-51-b0')
def _define_WPD_CONTENT_TYPE_GENERIC_MESSAGE():
    return Guid('e80eaaf8-b2db-4133-b6-7e-1b-ef-4b-4a-6e-5f')
def _define_WPD_CONTENT_TYPE_NETWORK_ASSOCIATION():
    return Guid('031da7ee-18c8-4205-84-7e-89-a1-12-61-d0-f3')
def _define_WPD_CONTENT_TYPE_CERTIFICATE():
    return Guid('dc3876e8-a948-4060-90-50-cb-d7-7e-8a-3d-87')
def _define_WPD_CONTENT_TYPE_WIRELESS_PROFILE():
    return Guid('0bac070a-9f5f-4da4-a8-f6-3d-e4-4d-68-fd-6c')
def _define_WPD_CONTENT_TYPE_MEDIA_CAST():
    return Guid('5e88b3cc-3e65-4e62-bf-ff-22-94-95-25-3a-b0')
def _define_WPD_CONTENT_TYPE_SECTION():
    return Guid('821089f5-1d91-4dc9-be-3c-bb-b1-b3-5b-18-ce')
def _define_WPD_CONTENT_TYPE_UNSPECIFIED():
    return Guid('28d8d31e-249c-454e-aa-bc-34-88-31-68-e6-34')
def _define_WPD_CONTENT_TYPE_ALL():
    return Guid('80e170d2-1055-4a3e-b9-52-82-cc-4f-8a-86-89')
def _define_WPD_FUNCTIONAL_CATEGORY_DEVICE():
    return Guid('08ea466b-e3a4-4336-a1-f3-a4-4d-2b-5c-43-8c')
def _define_WPD_FUNCTIONAL_CATEGORY_STORAGE():
    return Guid('23f05bbc-15de-4c2a-a5-5b-a9-af-5c-e4-12-ef')
def _define_WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE():
    return Guid('613ca327-ab93-4900-b4-fa-89-5b-b5-87-4b-79')
def _define_WPD_FUNCTIONAL_CATEGORY_AUDIO_CAPTURE():
    return Guid('3f2a1919-c7c2-4a00-85-5d-f5-7c-f0-6d-eb-bb')
def _define_WPD_FUNCTIONAL_CATEGORY_VIDEO_CAPTURE():
    return Guid('e23e5f6b-7243-43aa-8d-f1-0e-b3-d9-68-a9-18')
def _define_WPD_FUNCTIONAL_CATEGORY_SMS():
    return Guid('0044a0b1-c1e9-4afd-b3-58-a6-2c-61-17-c9-cf')
def _define_WPD_FUNCTIONAL_CATEGORY_RENDERING_INFORMATION():
    return Guid('08600ba4-a7ba-4a01-ab-0e-00-65-d0-a3-56-d3')
def _define_WPD_FUNCTIONAL_CATEGORY_NETWORK_CONFIGURATION():
    return Guid('48f4db72-7c6a-4ab0-9e-1a-47-0e-3c-db-f2-6a')
def _define_WPD_FUNCTIONAL_CATEGORY_ALL():
    return Guid('2d8a6512-a74c-448e-ba-8a-f4-ac-07-c4-93-99')
def _define_WPD_OBJECT_FORMAT_ICON():
    return Guid('077232ed-102c-4638-9c-22-83-f1-42-bf-c8-22')
def _define_WPD_OBJECT_FORMAT_M4A():
    return Guid('30aba7ac-6ffd-4c23-a3-59-3e-9b-52-f3-f1-c8')
def _define_WPD_OBJECT_FORMAT_NETWORK_ASSOCIATION():
    return Guid('b1020000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_X509V3CERTIFICATE():
    return Guid('b1030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_MICROSOFT_WFC():
    return Guid('b1040000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_3GPA():
    return Guid('e5172730-f971-41ef-a1-0b-22-71-a0-01-9d-7a')
def _define_WPD_OBJECT_FORMAT_3G2A():
    return Guid('1a11202d-8759-4e34-ba-5e-b1-21-10-87-ee-e4')
def _define_WPD_OBJECT_FORMAT_ALL():
    return Guid('c1f62eb2-4bb3-479c-9c-fa-05-b5-f3-a5-7b-22')
def _define_WPD_CATEGORY_NULL():
    return Guid('00000000-0000-0000-00-00-00-00-00-00-00-00')
def _define_WPD_PROPERTY_NULL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00000000-0000-0000-00-00-00-00-00-00-00-00'), pid=0)
def _define_WPD_OBJECT_PROPERTIES_V1():
    return Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c')
def _define_WPD_OBJECT_CONTENT_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=7)
def _define_WPD_OBJECT_REFERENCES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=14)
def _define_WPD_OBJECT_CONTAINER_FUNCTIONAL_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=23)
def _define_WPD_OBJECT_GENERATE_THUMBNAIL_FROM_RESOURCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=24)
def _define_WPD_OBJECT_HINT_LOCATION_DISPLAY_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=25)
def _define_WPD_OBJECT_PROPERTIES_V2():
    return Guid('0373cd3d-4a46-40d7-b4-d8-73-e8-da-74-e7-75')
def _define_WPD_OBJECT_SUPPORTED_UNITS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0373cd3d-4a46-40d7-b4-d8-73-e8-da-74-e7-75'), pid=2)
def _define_WPD_FUNCTIONAL_OBJECT_PROPERTIES_V1():
    return Guid('8f052d93-abca-4fc5-a5-ac-b0-1d-f4-db-e5-98')
def _define_WPD_FUNCTIONAL_OBJECT_CATEGORY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8f052d93-abca-4fc5-a5-ac-b0-1d-f4-db-e5-98'), pid=2)
def _define_WPD_STORAGE_OBJECT_PROPERTIES_V1():
    return Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a')
def _define_WPD_STORAGE_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=2)
def _define_WPD_STORAGE_FILE_SYSTEM_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=3)
def _define_WPD_STORAGE_CAPACITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=4)
def _define_WPD_STORAGE_FREE_SPACE_IN_BYTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=5)
def _define_WPD_STORAGE_FREE_SPACE_IN_OBJECTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=6)
def _define_WPD_STORAGE_DESCRIPTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=7)
def _define_WPD_STORAGE_SERIAL_NUMBER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=8)
def _define_WPD_STORAGE_MAX_OBJECT_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=9)
def _define_WPD_STORAGE_CAPACITY_IN_OBJECTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=10)
def _define_WPD_STORAGE_ACCESS_CAPABILITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=11)
def _define_WPD_NETWORK_ASSOCIATION_PROPERTIES_V1():
    return Guid('e4c93c1f-b203-43f1-a1-00-5a-07-d1-1b-02-74')
def _define_WPD_NETWORK_ASSOCIATION_HOST_NETWORK_IDENTIFIERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4c93c1f-b203-43f1-a1-00-5a-07-d1-1b-02-74'), pid=2)
def _define_WPD_NETWORK_ASSOCIATION_X509V3SEQUENCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4c93c1f-b203-43f1-a1-00-5a-07-d1-1b-02-74'), pid=3)
def _define_WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1():
    return Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60')
def _define_WPD_STILL_IMAGE_CAPTURE_RESOLUTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=2)
def _define_WPD_STILL_IMAGE_CAPTURE_FORMAT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=3)
def _define_WPD_STILL_IMAGE_COMPRESSION_SETTING():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=4)
def _define_WPD_STILL_IMAGE_WHITE_BALANCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=5)
def _define_WPD_STILL_IMAGE_RGB_GAIN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=6)
def _define_WPD_STILL_IMAGE_FNUMBER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=7)
def _define_WPD_STILL_IMAGE_FOCAL_LENGTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=8)
def _define_WPD_STILL_IMAGE_FOCUS_DISTANCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=9)
def _define_WPD_STILL_IMAGE_FOCUS_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=10)
def _define_WPD_STILL_IMAGE_EXPOSURE_METERING_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=11)
def _define_WPD_STILL_IMAGE_FLASH_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=12)
def _define_WPD_STILL_IMAGE_EXPOSURE_TIME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=13)
def _define_WPD_STILL_IMAGE_EXPOSURE_PROGRAM_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=14)
def _define_WPD_STILL_IMAGE_EXPOSURE_INDEX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=15)
def _define_WPD_STILL_IMAGE_EXPOSURE_BIAS_COMPENSATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=16)
def _define_WPD_STILL_IMAGE_CAPTURE_DELAY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=17)
def _define_WPD_STILL_IMAGE_CAPTURE_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=18)
def _define_WPD_STILL_IMAGE_CONTRAST():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=19)
def _define_WPD_STILL_IMAGE_SHARPNESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=20)
def _define_WPD_STILL_IMAGE_DIGITAL_ZOOM():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=21)
def _define_WPD_STILL_IMAGE_EFFECT_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=22)
def _define_WPD_STILL_IMAGE_BURST_NUMBER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=23)
def _define_WPD_STILL_IMAGE_BURST_INTERVAL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=24)
def _define_WPD_STILL_IMAGE_TIMELAPSE_NUMBER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=25)
def _define_WPD_STILL_IMAGE_TIMELAPSE_INTERVAL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=26)
def _define_WPD_STILL_IMAGE_FOCUS_METERING_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=27)
def _define_WPD_STILL_IMAGE_UPLOAD_URL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=28)
def _define_WPD_STILL_IMAGE_ARTIST():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=29)
def _define_WPD_STILL_IMAGE_CAMERA_MODEL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=30)
def _define_WPD_STILL_IMAGE_CAMERA_MANUFACTURER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=31)
def _define_WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1():
    return Guid('c53d039f-ee23-4a31-85-90-76-39-87-98-70-b4')
def _define_WPD_RENDERING_INFORMATION_PROFILES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c53d039f-ee23-4a31-85-90-76-39-87-98-70-b4'), pid=2)
def _define_WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c53d039f-ee23-4a31-85-90-76-39-87-98-70-b4'), pid=3)
def _define_WPD_RENDERING_INFORMATION_PROFILE_ENTRY_CREATABLE_RESOURCES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c53d039f-ee23-4a31-85-90-76-39-87-98-70-b4'), pid=4)
def _define_WPD_CLIENT_INFORMATION_PROPERTIES_V1():
    return Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59')
def _define_WPD_CLIENT_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=2)
def _define_WPD_CLIENT_MAJOR_VERSION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=3)
def _define_WPD_CLIENT_MINOR_VERSION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=4)
def _define_WPD_CLIENT_REVISION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=5)
def _define_WPD_CLIENT_WMDRM_APPLICATION_PRIVATE_KEY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=6)
def _define_WPD_CLIENT_WMDRM_APPLICATION_CERTIFICATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=7)
def _define_WPD_CLIENT_SECURITY_QUALITY_OF_SERVICE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=8)
def _define_WPD_CLIENT_DESIRED_ACCESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=9)
def _define_WPD_CLIENT_SHARE_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=10)
def _define_WPD_CLIENT_EVENT_COOKIE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=11)
def _define_WPD_CLIENT_MINIMUM_RESULTS_BUFFER_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=12)
def _define_WPD_CLIENT_MANUAL_CLOSE_ON_DISCONNECT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=13)
def _define_WPD_PROPERTY_ATTRIBUTES_V1():
    return Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37')
def _define_WPD_PROPERTY_ATTRIBUTE_FORM():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=2)
def _define_WPD_PROPERTY_ATTRIBUTE_CAN_READ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=3)
def _define_WPD_PROPERTY_ATTRIBUTE_CAN_WRITE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=4)
def _define_WPD_PROPERTY_ATTRIBUTE_CAN_DELETE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=5)
def _define_WPD_PROPERTY_ATTRIBUTE_DEFAULT_VALUE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=6)
def _define_WPD_PROPERTY_ATTRIBUTE_FAST_PROPERTY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=7)
def _define_WPD_PROPERTY_ATTRIBUTE_RANGE_MIN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=8)
def _define_WPD_PROPERTY_ATTRIBUTE_RANGE_MAX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=9)
def _define_WPD_PROPERTY_ATTRIBUTE_RANGE_STEP():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=10)
def _define_WPD_PROPERTY_ATTRIBUTE_ENUMERATION_ELEMENTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=11)
def _define_WPD_PROPERTY_ATTRIBUTE_REGULAR_EXPRESSION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=12)
def _define_WPD_PROPERTY_ATTRIBUTE_MAX_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=13)
def _define_WPD_PROPERTY_ATTRIBUTES_V2():
    return Guid('5d9da160-74ae-43cc-85-a9-fe-55-5a-80-79-8e')
def _define_WPD_PROPERTY_ATTRIBUTE_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5d9da160-74ae-43cc-85-a9-fe-55-5a-80-79-8e'), pid=2)
def _define_WPD_PROPERTY_ATTRIBUTE_VARTYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5d9da160-74ae-43cc-85-a9-fe-55-5a-80-79-8e'), pid=3)
def _define_WPD_CLASS_EXTENSION_OPTIONS_V1():
    return Guid('6309ffef-a87c-4ca7-84-34-79-75-76-e4-0a-96')
def _define_WPD_CLASS_EXTENSION_OPTIONS_SUPPORTED_CONTENT_TYPES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6309ffef-a87c-4ca7-84-34-79-75-76-e4-0a-96'), pid=2)
def _define_WPD_CLASS_EXTENSION_OPTIONS_DONT_REGISTER_WPD_DEVICE_INTERFACE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6309ffef-a87c-4ca7-84-34-79-75-76-e4-0a-96'), pid=3)
def _define_WPD_CLASS_EXTENSION_OPTIONS_REGISTER_WPD_PRIVATE_DEVICE_INTERFACE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6309ffef-a87c-4ca7-84-34-79-75-76-e4-0a-96'), pid=4)
def _define_WPD_CLASS_EXTENSION_OPTIONS_V2():
    return Guid('3e3595da-4d71-49fe-a0-b4-d4-40-6c-3a-e9-3f')
def _define_WPD_CLASS_EXTENSION_OPTIONS_MULTITRANSPORT_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3e3595da-4d71-49fe-a0-b4-d4-40-6c-3a-e9-3f'), pid=2)
def _define_WPD_CLASS_EXTENSION_OPTIONS_DEVICE_IDENTIFICATION_VALUES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3e3595da-4d71-49fe-a0-b4-d4-40-6c-3a-e9-3f'), pid=3)
def _define_WPD_CLASS_EXTENSION_OPTIONS_TRANSPORT_BANDWIDTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3e3595da-4d71-49fe-a0-b4-d4-40-6c-3a-e9-3f'), pid=4)
def _define_WPD_CLASS_EXTENSION_OPTIONS_V3():
    return Guid('65c160f8-1367-4ce2-93-9d-83-10-83-9f-0d-30')
def _define_WPD_CLASS_EXTENSION_OPTIONS_SILENCE_AUTOPLAY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('65c160f8-1367-4ce2-93-9d-83-10-83-9f-0d-30'), pid=2)
def _define_WPD_RESOURCE_ATTRIBUTES_V1():
    return Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6')
def _define_WPD_RESOURCE_ATTRIBUTE_TOTAL_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=2)
def _define_WPD_RESOURCE_ATTRIBUTE_CAN_READ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=3)
def _define_WPD_RESOURCE_ATTRIBUTE_CAN_WRITE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=4)
def _define_WPD_RESOURCE_ATTRIBUTE_CAN_DELETE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=5)
def _define_WPD_RESOURCE_ATTRIBUTE_OPTIMAL_READ_BUFFER_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=6)
def _define_WPD_RESOURCE_ATTRIBUTE_OPTIMAL_WRITE_BUFFER_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=7)
def _define_WPD_RESOURCE_ATTRIBUTE_FORMAT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=8)
def _define_WPD_RESOURCE_ATTRIBUTE_RESOURCE_KEY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=9)
def _define_WPD_DEVICE_PROPERTIES_V1():
    return Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc')
def _define_WPD_DEVICE_SYNC_PARTNER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=2)
def _define_WPD_DEVICE_FIRMWARE_VERSION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=3)
def _define_WPD_DEVICE_POWER_LEVEL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=4)
def _define_WPD_DEVICE_POWER_SOURCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=5)
def _define_WPD_DEVICE_PROTOCOL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=6)
def _define_WPD_DEVICE_MANUFACTURER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=7)
def _define_WPD_DEVICE_MODEL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=8)
def _define_WPD_DEVICE_SERIAL_NUMBER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=9)
def _define_WPD_DEVICE_SUPPORTS_NON_CONSUMABLE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=10)
def _define_WPD_DEVICE_DATETIME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=11)
def _define_WPD_DEVICE_FRIENDLY_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=12)
def _define_WPD_DEVICE_SUPPORTED_DRM_SCHEMES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=13)
def _define_WPD_DEVICE_SUPPORTED_FORMATS_ARE_ORDERED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=14)
def _define_WPD_DEVICE_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=15)
def _define_WPD_DEVICE_NETWORK_IDENTIFIER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=16)
def _define_WPD_DEVICE_PROPERTIES_V2():
    return Guid('463dd662-7fc4-4291-91-1c-7f-4c-9c-ca-97-99')
def _define_WPD_DEVICE_FUNCTIONAL_UNIQUE_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('463dd662-7fc4-4291-91-1c-7f-4c-9c-ca-97-99'), pid=2)
def _define_WPD_DEVICE_MODEL_UNIQUE_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('463dd662-7fc4-4291-91-1c-7f-4c-9c-ca-97-99'), pid=3)
def _define_WPD_DEVICE_TRANSPORT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('463dd662-7fc4-4291-91-1c-7f-4c-9c-ca-97-99'), pid=4)
def _define_WPD_DEVICE_USE_DEVICE_STAGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('463dd662-7fc4-4291-91-1c-7f-4c-9c-ca-97-99'), pid=5)
def _define_WPD_DEVICE_PROPERTIES_V3():
    return Guid('6c2b878c-c2ec-490d-b4-25-d7-a7-5e-23-e5-ed')
def _define_WPD_DEVICE_EDP_IDENTITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6c2b878c-c2ec-490d-b4-25-d7-a7-5e-23-e5-ed'), pid=1)
def _define_WPD_SERVICE_PROPERTIES_V1():
    return Guid('7510698a-cb54-481c-b8-db-0d-75-c9-3f-1c-06')
def _define_WPD_SERVICE_VERSION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7510698a-cb54-481c-b8-db-0d-75-c9-3f-1c-06'), pid=2)
def _define_WPD_EVENT_PROPERTIES_V1():
    return Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0')
def _define_WPD_EVENT_PARAMETER_PNP_DEVICE_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=2)
def _define_WPD_EVENT_PARAMETER_EVENT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=3)
def _define_WPD_EVENT_PARAMETER_OPERATION_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=4)
def _define_WPD_EVENT_PARAMETER_OPERATION_PROGRESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=5)
def _define_WPD_EVENT_PARAMETER_OBJECT_PARENT_PERSISTENT_UNIQUE_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=6)
def _define_WPD_EVENT_PARAMETER_OBJECT_CREATION_COOKIE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=7)
def _define_WPD_EVENT_PARAMETER_CHILD_HIERARCHY_CHANGED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=8)
def _define_WPD_EVENT_PROPERTIES_V2():
    return Guid('52807b8a-4914-4323-9b-9a-74-f6-54-b2-b8-46')
def _define_WPD_EVENT_PARAMETER_SERVICE_METHOD_CONTEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('52807b8a-4914-4323-9b-9a-74-f6-54-b2-b8-46'), pid=2)
def _define_WPD_EVENT_OPTIONS_V1():
    return Guid('b3d8dad7-a361-4b83-8a-48-5b-02-ce-10-71-3b')
def _define_WPD_EVENT_OPTION_IS_BROADCAST_EVENT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3d8dad7-a361-4b83-8a-48-5b-02-ce-10-71-3b'), pid=2)
def _define_WPD_EVENT_OPTION_IS_AUTOPLAY_EVENT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3d8dad7-a361-4b83-8a-48-5b-02-ce-10-71-3b'), pid=3)
def _define_WPD_EVENT_ATTRIBUTES_V1():
    return Guid('10c96578-2e81-4111-ad-de-e0-8c-a6-13-8f-6d')
def _define_WPD_EVENT_ATTRIBUTE_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10c96578-2e81-4111-ad-de-e0-8c-a6-13-8f-6d'), pid=2)
def _define_WPD_EVENT_ATTRIBUTE_PARAMETERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10c96578-2e81-4111-ad-de-e0-8c-a6-13-8f-6d'), pid=3)
def _define_WPD_EVENT_ATTRIBUTE_OPTIONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10c96578-2e81-4111-ad-de-e0-8c-a6-13-8f-6d'), pid=4)
def _define_WPD_API_OPTIONS_V1():
    return Guid('10e54a3e-052d-4777-a1-3c-de-76-14-be-2b-c4')
def _define_WPD_API_OPTION_USE_CLEAR_DATA_STREAM():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10e54a3e-052d-4777-a1-3c-de-76-14-be-2b-c4'), pid=2)
def _define_WPD_API_OPTION_IOCTL_ACCESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10e54a3e-052d-4777-a1-3c-de-76-14-be-2b-c4'), pid=3)
def _define_WPD_FORMAT_ATTRIBUTES_V1():
    return Guid('a0a02000-bcaf-4be8-b3-f5-23-3f-23-1c-f5-8f')
def _define_WPD_FORMAT_ATTRIBUTE_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a0a02000-bcaf-4be8-b3-f5-23-3f-23-1c-f5-8f'), pid=2)
def _define_WPD_FORMAT_ATTRIBUTE_MIMETYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a0a02000-bcaf-4be8-b3-f5-23-3f-23-1c-f5-8f'), pid=3)
def _define_WPD_METHOD_ATTRIBUTES_V1():
    return Guid('f17a5071-f039-44af-8e-fe-43-2c-f3-2e-43-2a')
def _define_WPD_METHOD_ATTRIBUTE_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f17a5071-f039-44af-8e-fe-43-2c-f3-2e-43-2a'), pid=2)
def _define_WPD_METHOD_ATTRIBUTE_ASSOCIATED_FORMAT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f17a5071-f039-44af-8e-fe-43-2c-f3-2e-43-2a'), pid=3)
def _define_WPD_METHOD_ATTRIBUTE_ACCESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f17a5071-f039-44af-8e-fe-43-2c-f3-2e-43-2a'), pid=4)
def _define_WPD_METHOD_ATTRIBUTE_PARAMETERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f17a5071-f039-44af-8e-fe-43-2c-f3-2e-43-2a'), pid=5)
def _define_WPD_PARAMETER_ATTRIBUTES_V1():
    return Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58')
def _define_WPD_PARAMETER_ATTRIBUTE_ORDER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=2)
def _define_WPD_PARAMETER_ATTRIBUTE_USAGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=3)
def _define_WPD_PARAMETER_ATTRIBUTE_FORM():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=4)
def _define_WPD_PARAMETER_ATTRIBUTE_DEFAULT_VALUE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=5)
def _define_WPD_PARAMETER_ATTRIBUTE_RANGE_MIN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=6)
def _define_WPD_PARAMETER_ATTRIBUTE_RANGE_MAX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=7)
def _define_WPD_PARAMETER_ATTRIBUTE_RANGE_STEP():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=8)
def _define_WPD_PARAMETER_ATTRIBUTE_ENUMERATION_ELEMENTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=9)
def _define_WPD_PARAMETER_ATTRIBUTE_REGULAR_EXPRESSION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=10)
def _define_WPD_PARAMETER_ATTRIBUTE_MAX_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=11)
def _define_WPD_PARAMETER_ATTRIBUTE_VARTYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=12)
def _define_WPD_PARAMETER_ATTRIBUTE_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=13)
def _define_WPD_CATEGORY_COMMON():
    return Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a')
def _define_WPD_COMMAND_COMMON_RESET_DEVICE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=2)
def _define_WPD_COMMAND_COMMON_GET_OBJECT_IDS_FROM_PERSISTENT_UNIQUE_IDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=3)
def _define_WPD_COMMAND_COMMON_SAVE_CLIENT_INFORMATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=4)
def _define_WPD_PROPERTY_COMMON_COMMAND_CATEGORY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1001)
def _define_WPD_PROPERTY_COMMON_COMMAND_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1002)
def _define_WPD_PROPERTY_COMMON_HRESULT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1003)
def _define_WPD_PROPERTY_COMMON_DRIVER_ERROR_CODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1004)
def _define_WPD_PROPERTY_COMMON_COMMAND_TARGET():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1006)
def _define_WPD_PROPERTY_COMMON_PERSISTENT_UNIQUE_IDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1007)
def _define_WPD_PROPERTY_COMMON_OBJECT_IDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1008)
def _define_WPD_PROPERTY_COMMON_CLIENT_INFORMATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1009)
def _define_WPD_PROPERTY_COMMON_CLIENT_INFORMATION_CONTEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1010)
def _define_WPD_PROPERTY_COMMON_ACTIVITY_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1011)
def _define_WPD_OPTION_VALID_OBJECT_IDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=5001)
def _define_WPD_CATEGORY_OBJECT_ENUMERATION():
    return Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec')
def _define_WPD_COMMAND_OBJECT_ENUMERATION_START_FIND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=2)
def _define_WPD_COMMAND_OBJECT_ENUMERATION_FIND_NEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=3)
def _define_WPD_COMMAND_OBJECT_ENUMERATION_END_FIND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=4)
def _define_WPD_PROPERTY_OBJECT_ENUMERATION_PARENT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=1001)
def _define_WPD_PROPERTY_OBJECT_ENUMERATION_FILTER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=1002)
def _define_WPD_PROPERTY_OBJECT_ENUMERATION_OBJECT_IDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=1003)
def _define_WPD_PROPERTY_OBJECT_ENUMERATION_CONTEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=1004)
def _define_WPD_PROPERTY_OBJECT_ENUMERATION_NUM_OBJECTS_REQUESTED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=1005)
def _define_WPD_CATEGORY_OBJECT_PROPERTIES():
    return Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04')
def _define_WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=2)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=3)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_GET():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=4)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_SET():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=5)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=6)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_DELETE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=7)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1001)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1002)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1003)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1004)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1005)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_DELETE_RESULTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1006)
def _define_WPD_CATEGORY_OBJECT_PROPERTIES_BULK():
    return Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e')
def _define_WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_START():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=2)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_NEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=3)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_END():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=4)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_START():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=5)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_NEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=6)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_END():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=7)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_START():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=8)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_NEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=9)
def _define_WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_END():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=10)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_IDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1001)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1002)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_BULK_VALUES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1003)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PROPERTY_KEYS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1004)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_BULK_DEPTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1005)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PARENT_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1006)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_FORMAT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1007)
def _define_WPD_PROPERTY_OBJECT_PROPERTIES_BULK_WRITE_RESULTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1008)
def _define_WPD_CATEGORY_OBJECT_RESOURCES():
    return Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a')
def _define_WPD_COMMAND_OBJECT_RESOURCES_GET_SUPPORTED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=2)
def _define_WPD_COMMAND_OBJECT_RESOURCES_GET_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=3)
def _define_WPD_COMMAND_OBJECT_RESOURCES_OPEN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=4)
def _define_WPD_COMMAND_OBJECT_RESOURCES_READ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=5)
def _define_WPD_COMMAND_OBJECT_RESOURCES_WRITE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=6)
def _define_WPD_COMMAND_OBJECT_RESOURCES_CLOSE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=7)
def _define_WPD_COMMAND_OBJECT_RESOURCES_DELETE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=8)
def _define_WPD_COMMAND_OBJECT_RESOURCES_CREATE_RESOURCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=9)
def _define_WPD_COMMAND_OBJECT_RESOURCES_REVERT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=10)
def _define_WPD_COMMAND_OBJECT_RESOURCES_SEEK():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=11)
def _define_WPD_COMMAND_OBJECT_RESOURCES_COMMIT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=12)
def _define_WPD_COMMAND_OBJECT_RESOURCES_SEEK_IN_UNITS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=13)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1001)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1002)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1003)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1004)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1005)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_READ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1006)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_READ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1007)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_WRITE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1008)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_WRITTEN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1009)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_DATA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1010)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1011)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_SEEK_OFFSET():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1012)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1013)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1014)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_SUPPORTS_UNITS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1015)
def _define_WPD_PROPERTY_OBJECT_RESOURCES_STREAM_UNITS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1016)
def _define_WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_READ_SUPPORTED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=5001)
def _define_WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_WRITE_SUPPORTED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=5002)
def _define_WPD_OPTION_OBJECT_RESOURCES_NO_INPUT_BUFFER_ON_READ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=5003)
def _define_WPD_CATEGORY_OBJECT_MANAGEMENT():
    return Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89')
def _define_WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_ONLY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=2)
def _define_WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_AND_DATA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=3)
def _define_WPD_COMMAND_OBJECT_MANAGEMENT_WRITE_OBJECT_DATA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=4)
def _define_WPD_COMMAND_OBJECT_MANAGEMENT_COMMIT_OBJECT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=5)
def _define_WPD_COMMAND_OBJECT_MANAGEMENT_REVERT_OBJECT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=6)
def _define_WPD_COMMAND_OBJECT_MANAGEMENT_DELETE_OBJECTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=7)
def _define_WPD_COMMAND_OBJECT_MANAGEMENT_MOVE_OBJECTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=8)
def _define_WPD_COMMAND_OBJECT_MANAGEMENT_COPY_OBJECTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=9)
def _define_WPD_COMMAND_OBJECT_MANAGEMENT_UPDATE_OBJECT_WITH_PROPERTIES_AND_DATA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=10)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_CREATION_PROPERTIES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1001)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1002)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_TO_WRITE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1003)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_WRITTEN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1004)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_DATA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1005)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1006)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_OPTIONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1007)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_OPTIMAL_TRANSFER_BUFFER_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1008)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_IDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1009)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_RESULTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1010)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_DESTINATION_FOLDER_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1011)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_MOVE_RESULTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1012)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_COPY_RESULTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1013)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_UPDATE_PROPERTIES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1014)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_PROPERTY_KEYS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1015)
def _define_WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_FORMAT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1016)
def _define_WPD_OPTION_OBJECT_MANAGEMENT_RECURSIVE_DELETE_SUPPORTED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=5001)
def _define_WPD_CATEGORY_CAPABILITIES():
    return Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56')
def _define_WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=2)
def _define_WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=3)
def _define_WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=4)
def _define_WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=5)
def _define_WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=6)
def _define_WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=7)
def _define_WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=8)
def _define_WPD_COMMAND_CAPABILITIES_GET_FIXED_PROPERTY_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=9)
def _define_WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=10)
def _define_WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=11)
def _define_WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1001)
def _define_WPD_PROPERTY_CAPABILITIES_COMMAND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1002)
def _define_WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1003)
def _define_WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1004)
def _define_WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1005)
def _define_WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1006)
def _define_WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1007)
def _define_WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1008)
def _define_WPD_PROPERTY_CAPABILITIES_FORMATS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1009)
def _define_WPD_PROPERTY_CAPABILITIES_FORMAT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1010)
def _define_WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1011)
def _define_WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1012)
def _define_WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1013)
def _define_WPD_PROPERTY_CAPABILITIES_EVENT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1014)
def _define_WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1015)
def _define_WPD_CATEGORY_STORAGE():
    return Guid('d8f907a6-34cc-45fa-97-fb-d0-07-fa-47-ec-94')
def _define_WPD_COMMAND_STORAGE_FORMAT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d8f907a6-34cc-45fa-97-fb-d0-07-fa-47-ec-94'), pid=2)
def _define_WPD_COMMAND_STORAGE_EJECT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d8f907a6-34cc-45fa-97-fb-d0-07-fa-47-ec-94'), pid=4)
def _define_WPD_PROPERTY_STORAGE_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d8f907a6-34cc-45fa-97-fb-d0-07-fa-47-ec-94'), pid=1001)
def _define_WPD_PROPERTY_STORAGE_DESTINATION_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d8f907a6-34cc-45fa-97-fb-d0-07-fa-47-ec-94'), pid=1002)
def _define_WPD_CATEGORY_SMS():
    return Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1')
def _define_WPD_COMMAND_SMS_SEND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=2)
def _define_WPD_PROPERTY_SMS_RECIPIENT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=1001)
def _define_WPD_PROPERTY_SMS_MESSAGE_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=1002)
def _define_WPD_PROPERTY_SMS_TEXT_MESSAGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=1003)
def _define_WPD_PROPERTY_SMS_BINARY_MESSAGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=1004)
def _define_WPD_OPTION_SMS_BINARY_MESSAGE_SUPPORTED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=5001)
def _define_WPD_CATEGORY_STILL_IMAGE_CAPTURE():
    return Guid('4fcd6982-22a2-4b05-a4-8b-62-d3-8b-f2-7b-32')
def _define_WPD_COMMAND_STILL_IMAGE_CAPTURE_INITIATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4fcd6982-22a2-4b05-a4-8b-62-d3-8b-f2-7b-32'), pid=2)
def _define_WPD_CATEGORY_MEDIA_CAPTURE():
    return Guid('59b433ba-fe44-4d8d-80-8c-6b-cb-9b-0f-15-e8')
def _define_WPD_COMMAND_MEDIA_CAPTURE_START():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('59b433ba-fe44-4d8d-80-8c-6b-cb-9b-0f-15-e8'), pid=2)
def _define_WPD_COMMAND_MEDIA_CAPTURE_STOP():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('59b433ba-fe44-4d8d-80-8c-6b-cb-9b-0f-15-e8'), pid=3)
def _define_WPD_COMMAND_MEDIA_CAPTURE_PAUSE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('59b433ba-fe44-4d8d-80-8c-6b-cb-9b-0f-15-e8'), pid=4)
def _define_WPD_CATEGORY_DEVICE_HINTS():
    return Guid('0d5fb92b-cb46-4c4f-83-43-0b-c3-d3-f1-7c-84')
def _define_WPD_COMMAND_DEVICE_HINTS_GET_CONTENT_LOCATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0d5fb92b-cb46-4c4f-83-43-0b-c3-d3-f1-7c-84'), pid=2)
def _define_WPD_PROPERTY_DEVICE_HINTS_CONTENT_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0d5fb92b-cb46-4c4f-83-43-0b-c3-d3-f1-7c-84'), pid=1001)
def _define_WPD_PROPERTY_DEVICE_HINTS_CONTENT_LOCATIONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0d5fb92b-cb46-4c4f-83-43-0b-c3-d3-f1-7c-84'), pid=1002)
def _define_WPD_CLASS_EXTENSION_V1():
    return Guid('33fb0d11-64a3-4fac-b4-c7-3d-fe-aa-99-b0-51')
def _define_WPD_COMMAND_CLASS_EXTENSION_WRITE_DEVICE_INFORMATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('33fb0d11-64a3-4fac-b4-c7-3d-fe-aa-99-b0-51'), pid=2)
def _define_WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_VALUES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('33fb0d11-64a3-4fac-b4-c7-3d-fe-aa-99-b0-51'), pid=1001)
def _define_WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_WRITE_RESULTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('33fb0d11-64a3-4fac-b4-c7-3d-fe-aa-99-b0-51'), pid=1002)
def _define_WPD_CLASS_EXTENSION_V2():
    return Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58')
def _define_WPD_COMMAND_CLASS_EXTENSION_REGISTER_SERVICE_INTERFACES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58'), pid=2)
def _define_WPD_COMMAND_CLASS_EXTENSION_UNREGISTER_SERVICE_INTERFACES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58'), pid=3)
def _define_WPD_PROPERTY_CLASS_EXTENSION_SERVICE_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58'), pid=1001)
def _define_WPD_PROPERTY_CLASS_EXTENSION_SERVICE_INTERFACES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58'), pid=1002)
def _define_WPD_PROPERTY_CLASS_EXTENSION_SERVICE_REGISTRATION_RESULTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58'), pid=1003)
def _define_WPD_CATEGORY_NETWORK_CONFIGURATION():
    return Guid('78f9c6fc-79b8-473c-90-60-6b-d2-3d-d0-72-c4')
def _define_WPD_COMMAND_GENERATE_KEYPAIR():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78f9c6fc-79b8-473c-90-60-6b-d2-3d-d0-72-c4'), pid=2)
def _define_WPD_COMMAND_COMMIT_KEYPAIR():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78f9c6fc-79b8-473c-90-60-6b-d2-3d-d0-72-c4'), pid=3)
def _define_WPD_COMMAND_PROCESS_WIRELESS_PROFILE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78f9c6fc-79b8-473c-90-60-6b-d2-3d-d0-72-c4'), pid=4)
def _define_WPD_PROPERTY_PUBLIC_KEY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78f9c6fc-79b8-473c-90-60-6b-d2-3d-d0-72-c4'), pid=1001)
def _define_WPD_CATEGORY_SERVICE_COMMON():
    return Guid('322f071d-36ef-477f-b4-b5-6f-52-d7-34-ba-ee')
def _define_WPD_COMMAND_SERVICE_COMMON_GET_SERVICE_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('322f071d-36ef-477f-b4-b5-6f-52-d7-34-ba-ee'), pid=2)
def _define_WPD_PROPERTY_SERVICE_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('322f071d-36ef-477f-b4-b5-6f-52-d7-34-ba-ee'), pid=1001)
def _define_WPD_CATEGORY_SERVICE_CAPABILITIES():
    return Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89')
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=2)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS_BY_FORMAT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=3)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=4)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_PARAMETER_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=5)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMATS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=6)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=7)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=8)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_PROPERTY_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=9)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_EVENTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=10)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=11)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_PARAMETER_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=12)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_INHERITED_SERVICES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=13)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_RENDERING_PROFILES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=14)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_COMMANDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=15)
def _define_WPD_COMMAND_SERVICE_CAPABILITIES_GET_COMMAND_OPTIONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=16)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_METHODS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1001)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1002)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1003)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1004)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1005)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1006)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_FORMATS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1007)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1008)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_KEYS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1009)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1010)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_EVENTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1011)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1012)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT_ATTRIBUTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1013)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITANCE_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1014)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITED_SERVICES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1015)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_RENDERING_PROFILES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1016)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_COMMANDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1017)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1018)
def _define_WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND_OPTIONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1019)
def _define_WPD_CATEGORY_SERVICE_METHODS():
    return Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc')
def _define_WPD_COMMAND_SERVICE_METHODS_START_INVOKE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=2)
def _define_WPD_COMMAND_SERVICE_METHODS_CANCEL_INVOKE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=3)
def _define_WPD_COMMAND_SERVICE_METHODS_END_INVOKE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=4)
def _define_WPD_PROPERTY_SERVICE_METHOD():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=1001)
def _define_WPD_PROPERTY_SERVICE_METHOD_PARAMETER_VALUES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=1002)
def _define_WPD_PROPERTY_SERVICE_METHOD_RESULT_VALUES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=1003)
def _define_WPD_PROPERTY_SERVICE_METHOD_CONTEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=1004)
def _define_WPD_PROPERTY_SERVICE_METHOD_HRESULT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=1005)
def _define_WPD_RESOURCE_DEFAULT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e81e79be-34f0-41bf-b5-3f-f1-a0-6a-e8-78-42'), pid=0)
def _define_WPD_RESOURCE_CONTACT_PHOTO():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2c4d6803-80ea-4580-af-9a-5b-e1-a2-3e-dd-cb'), pid=0)
def _define_WPD_RESOURCE_THUMBNAIL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c7c407ba-98fa-46b5-99-60-23-fe-c1-24-cf-de'), pid=0)
def _define_WPD_RESOURCE_ICON():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f195fed8-aa28-4ee3-b1-53-e1-82-dd-5e-dc-39'), pid=0)
def _define_WPD_RESOURCE_AUDIO_CLIP():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3bc13982-85b1-48e0-95-a6-8d-3a-d0-6b-e1-17'), pid=0)
def _define_WPD_RESOURCE_ALBUM_ART():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f02aa354-2300-4e2d-a1-b9-3b-67-30-f7-fa-21'), pid=0)
def _define_WPD_RESOURCE_GENERIC():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b9b9f515-ba70-4647-94-dc-fa-49-25-e9-5a-07'), pid=0)
def _define_WPD_RESOURCE_VIDEO_CLIP():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b566ee42-6368-4290-86-62-70-18-2f-b7-9f-20'), pid=0)
def _define_WPD_RESOURCE_BRANDING_ART():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b633b1ae-6caf-4a87-95-89-22-de-d6-dd-58-99'), pid=0)
def _define_WPD_OBJECT_FORMAT_PROPERTIES_ONLY():
    return Guid('30010000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_UNSPECIFIED():
    return Guid('30000000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_SCRIPT():
    return Guid('30020000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_EXECUTABLE():
    return Guid('30030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_TEXT():
    return Guid('30040000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_HTML():
    return Guid('30050000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_DPOF():
    return Guid('30060000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_AIFF():
    return Guid('30070000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_WAVE():
    return Guid('30080000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_MP3():
    return Guid('30090000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_AVI():
    return Guid('300a0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_MPEG():
    return Guid('300b0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_ASF():
    return Guid('300c0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_EXIF():
    return Guid('38010000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_TIFFEP():
    return Guid('38020000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_FLASHPIX():
    return Guid('38030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_BMP():
    return Guid('38040000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_CIFF():
    return Guid('38050000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_GIF():
    return Guid('38070000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_JFIF():
    return Guid('38080000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_PCD():
    return Guid('38090000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_PICT():
    return Guid('380a0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_PNG():
    return Guid('380b0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_TIFF():
    return Guid('380d0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_TIFFIT():
    return Guid('380e0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_JP2():
    return Guid('380f0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_JPX():
    return Guid('38100000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_WBMP():
    return Guid('b8030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_JPEGXR():
    return Guid('b8040000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_WINDOWSIMAGEFORMAT():
    return Guid('b8810000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_WMA():
    return Guid('b9010000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_WMV():
    return Guid('b9810000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_WPLPLAYLIST():
    return Guid('ba100000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_M3UPLAYLIST():
    return Guid('ba110000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_MPLPLAYLIST():
    return Guid('ba120000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_ASXPLAYLIST():
    return Guid('ba130000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_PLSPLAYLIST():
    return Guid('ba140000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_ABSTRACT_CONTACT_GROUP():
    return Guid('ba060000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_ABSTRACT_MEDIA_CAST():
    return Guid('ba0b0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_VCALENDAR1():
    return Guid('be020000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_ICALENDAR():
    return Guid('be030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_ABSTRACT_CONTACT():
    return Guid('bb810000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_VCARD2():
    return Guid('bb820000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_VCARD3():
    return Guid('bb830000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_XML():
    return Guid('ba820000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_AAC():
    return Guid('b9030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_AUDIBLE():
    return Guid('b9040000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_FLAC():
    return Guid('b9060000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_QCELP():
    return Guid('b9070000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_AMR():
    return Guid('b9080000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_OGG():
    return Guid('b9020000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_MP4():
    return Guid('b9820000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_MP2():
    return Guid('b9830000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_MICROSOFT_WORD():
    return Guid('ba830000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_MHT_COMPILED_HTML():
    return Guid('ba840000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_MICROSOFT_EXCEL():
    return Guid('ba850000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_MICROSOFT_POWERPOINT():
    return Guid('ba860000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_3GP():
    return Guid('b9840000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_3G2():
    return Guid('b9850000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_AVCHD():
    return Guid('b9860000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_ATSCTS():
    return Guid('b9870000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_DVBTS():
    return Guid('b9880000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_FORMAT_MKV():
    return Guid('b9900000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def _define_WPD_OBJECT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=2)
def _define_WPD_OBJECT_PARENT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=3)
def _define_WPD_OBJECT_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=4)
def _define_WPD_OBJECT_PERSISTENT_UNIQUE_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=5)
def _define_WPD_OBJECT_FORMAT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=6)
def _define_WPD_OBJECT_ISHIDDEN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=9)
def _define_WPD_OBJECT_ISSYSTEM():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=10)
def _define_WPD_OBJECT_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=11)
def _define_WPD_OBJECT_ORIGINAL_FILE_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=12)
def _define_WPD_OBJECT_NON_CONSUMABLE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=13)
def _define_WPD_OBJECT_KEYWORDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=15)
def _define_WPD_OBJECT_SYNC_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=16)
def _define_WPD_OBJECT_IS_DRM_PROTECTED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=17)
def _define_WPD_OBJECT_DATE_CREATED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=18)
def _define_WPD_OBJECT_DATE_MODIFIED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=19)
def _define_WPD_OBJECT_DATE_AUTHORED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=20)
def _define_WPD_OBJECT_BACK_REFERENCES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=21)
def _define_WPD_OBJECT_CAN_DELETE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=26)
def _define_WPD_OBJECT_LANGUAGE_LOCALE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=27)
def _define_WPD_FOLDER_OBJECT_PROPERTIES_V1():
    return Guid('7e9a7abf-e568-4b34-aa-2f-13-bb-12-ab-17-7d')
def _define_WPD_FOLDER_CONTENT_TYPES_ALLOWED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7e9a7abf-e568-4b34-aa-2f-13-bb-12-ab-17-7d'), pid=2)
def _define_WPD_IMAGE_OBJECT_PROPERTIES_V1():
    return Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db')
def _define_WPD_IMAGE_BITDEPTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=3)
def _define_WPD_IMAGE_CROPPED_STATUS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=4)
def _define_WPD_IMAGE_COLOR_CORRECTED_STATUS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=5)
def _define_WPD_IMAGE_FNUMBER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=6)
def _define_WPD_IMAGE_EXPOSURE_TIME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=7)
def _define_WPD_IMAGE_EXPOSURE_INDEX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=8)
def _define_WPD_IMAGE_HORIZONTAL_RESOLUTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=9)
def _define_WPD_IMAGE_VERTICAL_RESOLUTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=10)
def _define_WPD_DOCUMENT_OBJECT_PROPERTIES_V1():
    return Guid('0b110203-eb95-4f02-93-e0-97-c6-31-49-3a-d5')
def _define_WPD_MEDIA_PROPERTIES_V1():
    return Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8')
def _define_WPD_MEDIA_TOTAL_BITRATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=2)
def _define_WPD_MEDIA_BITRATE_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=3)
def _define_WPD_MEDIA_COPYRIGHT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=4)
def _define_WPD_MEDIA_SUBSCRIPTION_CONTENT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=5)
def _define_WPD_MEDIA_USE_COUNT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=6)
def _define_WPD_MEDIA_SKIP_COUNT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=7)
def _define_WPD_MEDIA_LAST_ACCESSED_TIME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=8)
def _define_WPD_MEDIA_PARENTAL_RATING():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=9)
def _define_WPD_MEDIA_META_GENRE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=10)
def _define_WPD_MEDIA_COMPOSER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=11)
def _define_WPD_MEDIA_EFFECTIVE_RATING():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=12)
def _define_WPD_MEDIA_SUB_TITLE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=13)
def _define_WPD_MEDIA_RELEASE_DATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=14)
def _define_WPD_MEDIA_SAMPLE_RATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=15)
def _define_WPD_MEDIA_STAR_RATING():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=16)
def _define_WPD_MEDIA_USER_EFFECTIVE_RATING():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=17)
def _define_WPD_MEDIA_TITLE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=18)
def _define_WPD_MEDIA_DURATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=19)
def _define_WPD_MEDIA_BUY_NOW():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=20)
def _define_WPD_MEDIA_ENCODING_PROFILE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=21)
def _define_WPD_MEDIA_WIDTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=22)
def _define_WPD_MEDIA_HEIGHT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=23)
def _define_WPD_MEDIA_ARTIST():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=24)
def _define_WPD_MEDIA_ALBUM_ARTIST():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=25)
def _define_WPD_MEDIA_OWNER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=26)
def _define_WPD_MEDIA_MANAGING_EDITOR():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=27)
def _define_WPD_MEDIA_WEBMASTER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=28)
def _define_WPD_MEDIA_SOURCE_URL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=29)
def _define_WPD_MEDIA_DESTINATION_URL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=30)
def _define_WPD_MEDIA_DESCRIPTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=31)
def _define_WPD_MEDIA_GENRE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=32)
def _define_WPD_MEDIA_TIME_BOOKMARK():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=33)
def _define_WPD_MEDIA_OBJECT_BOOKMARK():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=34)
def _define_WPD_MEDIA_LAST_BUILD_DATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=35)
def _define_WPD_MEDIA_BYTE_BOOKMARK():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=36)
def _define_WPD_MEDIA_TIME_TO_LIVE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=37)
def _define_WPD_MEDIA_GUID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=38)
def _define_WPD_MEDIA_SUB_DESCRIPTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=39)
def _define_WPD_MEDIA_AUDIO_ENCODING_PROFILE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=49)
def _define_WPD_CONTACT_OBJECT_PROPERTIES_V1():
    return Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b')
def _define_WPD_CONTACT_DISPLAY_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=2)
def _define_WPD_CONTACT_FIRST_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=3)
def _define_WPD_CONTACT_MIDDLE_NAMES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=4)
def _define_WPD_CONTACT_LAST_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=5)
def _define_WPD_CONTACT_PREFIX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=6)
def _define_WPD_CONTACT_SUFFIX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=7)
def _define_WPD_CONTACT_PHONETIC_FIRST_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=8)
def _define_WPD_CONTACT_PHONETIC_LAST_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=9)
def _define_WPD_CONTACT_PERSONAL_FULL_POSTAL_ADDRESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=10)
def _define_WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE1():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=11)
def _define_WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=12)
def _define_WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_CITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=13)
def _define_WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_REGION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=14)
def _define_WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_POSTAL_CODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=15)
def _define_WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_COUNTRY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=16)
def _define_WPD_CONTACT_BUSINESS_FULL_POSTAL_ADDRESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=17)
def _define_WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE1():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=18)
def _define_WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=19)
def _define_WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_CITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=20)
def _define_WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_REGION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=21)
def _define_WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_POSTAL_CODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=22)
def _define_WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_COUNTRY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=23)
def _define_WPD_CONTACT_OTHER_FULL_POSTAL_ADDRESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=24)
def _define_WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE1():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=25)
def _define_WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=26)
def _define_WPD_CONTACT_OTHER_POSTAL_ADDRESS_CITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=27)
def _define_WPD_CONTACT_OTHER_POSTAL_ADDRESS_REGION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=28)
def _define_WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_CODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=29)
def _define_WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_COUNTRY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=30)
def _define_WPD_CONTACT_PRIMARY_EMAIL_ADDRESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=31)
def _define_WPD_CONTACT_PERSONAL_EMAIL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=32)
def _define_WPD_CONTACT_PERSONAL_EMAIL2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=33)
def _define_WPD_CONTACT_BUSINESS_EMAIL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=34)
def _define_WPD_CONTACT_BUSINESS_EMAIL2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=35)
def _define_WPD_CONTACT_OTHER_EMAILS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=36)
def _define_WPD_CONTACT_PRIMARY_PHONE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=37)
def _define_WPD_CONTACT_PERSONAL_PHONE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=38)
def _define_WPD_CONTACT_PERSONAL_PHONE2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=39)
def _define_WPD_CONTACT_BUSINESS_PHONE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=40)
def _define_WPD_CONTACT_BUSINESS_PHONE2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=41)
def _define_WPD_CONTACT_MOBILE_PHONE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=42)
def _define_WPD_CONTACT_MOBILE_PHONE2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=43)
def _define_WPD_CONTACT_PERSONAL_FAX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=44)
def _define_WPD_CONTACT_BUSINESS_FAX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=45)
def _define_WPD_CONTACT_PAGER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=46)
def _define_WPD_CONTACT_OTHER_PHONES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=47)
def _define_WPD_CONTACT_PRIMARY_WEB_ADDRESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=48)
def _define_WPD_CONTACT_PERSONAL_WEB_ADDRESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=49)
def _define_WPD_CONTACT_BUSINESS_WEB_ADDRESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=50)
def _define_WPD_CONTACT_INSTANT_MESSENGER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=51)
def _define_WPD_CONTACT_INSTANT_MESSENGER2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=52)
def _define_WPD_CONTACT_INSTANT_MESSENGER3():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=53)
def _define_WPD_CONTACT_COMPANY_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=54)
def _define_WPD_CONTACT_PHONETIC_COMPANY_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=55)
def _define_WPD_CONTACT_ROLE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=56)
def _define_WPD_CONTACT_BIRTHDATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=57)
def _define_WPD_CONTACT_PRIMARY_FAX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=58)
def _define_WPD_CONTACT_SPOUSE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=59)
def _define_WPD_CONTACT_CHILDREN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=60)
def _define_WPD_CONTACT_ASSISTANT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=61)
def _define_WPD_CONTACT_ANNIVERSARY_DATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=62)
def _define_WPD_CONTACT_RINGTONE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=63)
def _define_WPD_MUSIC_OBJECT_PROPERTIES_V1():
    return Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6')
def _define_WPD_MUSIC_ALBUM():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=3)
def _define_WPD_MUSIC_TRACK():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=4)
def _define_WPD_MUSIC_LYRICS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=6)
def _define_WPD_MUSIC_MOOD():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=8)
def _define_WPD_AUDIO_BITRATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=9)
def _define_WPD_AUDIO_CHANNEL_COUNT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=10)
def _define_WPD_AUDIO_FORMAT_CODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=11)
def _define_WPD_AUDIO_BIT_DEPTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=12)
def _define_WPD_AUDIO_BLOCK_ALIGNMENT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=13)
def _define_WPD_VIDEO_OBJECT_PROPERTIES_V1():
    return Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a')
def _define_WPD_VIDEO_AUTHOR():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=2)
def _define_WPD_VIDEO_RECORDEDTV_STATION_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=4)
def _define_WPD_VIDEO_RECORDEDTV_CHANNEL_NUMBER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=5)
def _define_WPD_VIDEO_RECORDEDTV_REPEAT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=7)
def _define_WPD_VIDEO_BUFFER_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=8)
def _define_WPD_VIDEO_CREDITS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=9)
def _define_WPD_VIDEO_KEY_FRAME_DISTANCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=10)
def _define_WPD_VIDEO_QUALITY_SETTING():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=11)
def _define_WPD_VIDEO_SCAN_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=12)
def _define_WPD_VIDEO_BITRATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=13)
def _define_WPD_VIDEO_FOURCC_CODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=14)
def _define_WPD_VIDEO_FRAMERATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=15)
def _define_WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1():
    return Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f')
def _define_WPD_COMMON_INFORMATION_SUBJECT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=2)
def _define_WPD_COMMON_INFORMATION_BODY_TEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=3)
def _define_WPD_COMMON_INFORMATION_PRIORITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=4)
def _define_WPD_COMMON_INFORMATION_START_DATETIME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=5)
def _define_WPD_COMMON_INFORMATION_END_DATETIME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=6)
def _define_WPD_COMMON_INFORMATION_NOTES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=7)
def _define_WPD_MEMO_OBJECT_PROPERTIES_V1():
    return Guid('5ffbfc7b-7483-41ad-af-b9-da-3f-4e-59-2b-8d')
def _define_WPD_EMAIL_OBJECT_PROPERTIES_V1():
    return Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5')
def _define_WPD_EMAIL_TO_LINE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=2)
def _define_WPD_EMAIL_CC_LINE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=3)
def _define_WPD_EMAIL_BCC_LINE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=4)
def _define_WPD_EMAIL_HAS_BEEN_READ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=7)
def _define_WPD_EMAIL_RECEIVED_TIME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=8)
def _define_WPD_EMAIL_HAS_ATTACHMENTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=9)
def _define_WPD_EMAIL_SENDER_ADDRESS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=10)
def _define_WPD_APPOINTMENT_OBJECT_PROPERTIES_V1():
    return Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3')
def _define_WPD_APPOINTMENT_LOCATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=3)
def _define_WPD_APPOINTMENT_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=7)
def _define_WPD_APPOINTMENT_REQUIRED_ATTENDEES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=8)
def _define_WPD_APPOINTMENT_OPTIONAL_ATTENDEES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=9)
def _define_WPD_APPOINTMENT_ACCEPTED_ATTENDEES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=10)
def _define_WPD_APPOINTMENT_RESOURCES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=11)
def _define_WPD_APPOINTMENT_TENTATIVE_ATTENDEES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=12)
def _define_WPD_APPOINTMENT_DECLINED_ATTENDEES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=13)
def _define_WPD_TASK_OBJECT_PROPERTIES_V1():
    return Guid('e354e95e-d8a0-4637-a0-3a-0c-b2-68-38-db-c7')
def _define_WPD_TASK_STATUS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e354e95e-d8a0-4637-a0-3a-0c-b2-68-38-db-c7'), pid=6)
def _define_WPD_TASK_PERCENT_COMPLETE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e354e95e-d8a0-4637-a0-3a-0c-b2-68-38-db-c7'), pid=8)
def _define_WPD_TASK_REMINDER_DATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e354e95e-d8a0-4637-a0-3a-0c-b2-68-38-db-c7'), pid=10)
def _define_WPD_TASK_OWNER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e354e95e-d8a0-4637-a0-3a-0c-b2-68-38-db-c7'), pid=11)
def _define_WPD_SMS_OBJECT_PROPERTIES_V1():
    return Guid('7e1074cc-50ff-4dd1-a7-42-53-be-6f-09-3a-0d')
def _define_WPD_SMS_PROVIDER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7e1074cc-50ff-4dd1-a7-42-53-be-6f-09-3a-0d'), pid=2)
def _define_WPD_SMS_TIMEOUT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7e1074cc-50ff-4dd1-a7-42-53-be-6f-09-3a-0d'), pid=3)
def _define_WPD_SMS_MAX_PAYLOAD():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7e1074cc-50ff-4dd1-a7-42-53-be-6f-09-3a-0d'), pid=4)
def _define_WPD_SMS_ENCODING():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7e1074cc-50ff-4dd1-a7-42-53-be-6f-09-3a-0d'), pid=5)
def _define_WPD_SECTION_OBJECT_PROPERTIES_V1():
    return Guid('516afd2b-c64e-44f0-98-dc-be-e1-c8-8f-7d-66')
def _define_WPD_SECTION_DATA_OFFSET():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('516afd2b-c64e-44f0-98-dc-be-e1-c8-8f-7d-66'), pid=2)
def _define_WPD_SECTION_DATA_LENGTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('516afd2b-c64e-44f0-98-dc-be-e1-c8-8f-7d-66'), pid=3)
def _define_WPD_SECTION_DATA_UNITS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('516afd2b-c64e-44f0-98-dc-be-e1-c8-8f-7d-66'), pid=4)
def _define_WPD_SECTION_DATA_REFERENCED_OBJECT_RESOURCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('516afd2b-c64e-44f0-98-dc-be-e1-c8-8f-7d-66'), pid=5)
NAME_Undefined = 'Undefined'
NAME_Association = 'Association'
NAME_DeviceScript = 'DeviceScript'
NAME_DeviceExecutable = 'DeviceExecutable'
NAME_TextDocument = 'TextDocument'
NAME_HTMLDocument = 'HTMLDocument'
NAME_DPOFDocument = 'DPOFDocument'
NAME_AIFFFile = 'AIFFFile'
NAME_WAVFile = 'WAVFile'
NAME_MP3File = 'MP3File'
NAME_AVIFile = 'AVIFile'
NAME_MPEGFile = 'MPEGFile'
NAME_ASFFile = 'ASFFile'
NAME_UnknownImage = 'UnknownImage'
NAME_EXIFImage = 'EXIFImage'
NAME_TIFFEPImage = 'TIFFEPImage'
NAME_FlashPixImage = 'FlashPixImage'
NAME_BMPImage = 'BMPImage'
NAME_CIFFImage = 'CIFFImage'
NAME_GIFImage = 'GIFImage'
NAME_JFIFImage = 'JFIFImage'
NAME_PCDImage = 'PCDImage'
NAME_PICTImage = 'PICTImage'
NAME_PNGImage = 'PNGImage'
NAME_TIFFImage = 'TIFFImage'
NAME_TIFFITImage = 'TIFFITImage'
NAME_JP2Image = 'JP2Image'
NAME_JPXImage = 'JPXImage'
NAME_FirmwareFile = 'FirmwareFile'
NAME_WBMPImage = 'WBMPImage'
NAME_JPEGXRImage = 'JPEGXRImage'
NAME_HDPhotoImage = 'HDPhotoImage'
NAME_UndefinedAudio = 'UndefinedAudio'
NAME_WMAFile = 'WMAFile'
NAME_OGGFile = 'OGGFile'
NAME_AACFile = 'AACFile'
NAME_AudibleFile = 'AudibleFile'
NAME_FLACFile = 'FLACFile'
NAME_QCELPFile = 'QCELPFile'
NAME_AMRFile = 'AMRFile'
NAME_UndefinedVideo = 'UndefinedVideo'
NAME_WMVFile = 'WMVFile'
NAME_MPEG4File = 'MPEG4File'
NAME_MPEG2File = 'MPEG2File'
NAME_3GPPFile = '3GPPFile'
NAME_3GPP2File = '3GPP2File'
NAME_AVCHDFile = 'AVCHDFile'
NAME_ATSCTSFile = 'ATSCTSFile'
NAME_DVBTSFile = 'DVBTSFile'
NAME_UndefinedCollection = 'UndefinedCollection'
NAME_AbstractMultimediaAlbum = 'AbstractMultimediaAlbum'
NAME_AbstractImageAlbum = 'AbstractImageAlbum'
NAME_AbstractAudioAlbum = 'AbstractAudioAlbum'
NAME_AbstractVideoAlbum = 'AbstractVideoAlbum'
NAME_AbstractAudioVideoAlbum = 'AbstractAudioVideoAlbum'
NAME_AbstractChapteredProduction = 'AbstractChapteredProduction'
NAME_AbstractAudioPlaylist = 'AbstractAudioPlaylist'
NAME_AbstractVideoPlaylist = 'AbstractVideoPlaylist'
NAME_AbstractMediacast = 'AbstractMediacast'
NAME_WPLPlaylist = 'WPLPlaylist'
NAME_M3UPlaylist = 'M3UPlaylist'
NAME_MPLPlaylist = 'MPLPlaylist'
NAME_ASXPlaylist = 'ASXPlaylist'
NAME_PSLPlaylist = 'PSLPlaylist'
NAME_UndefinedDocument = 'UndefinedDocument'
NAME_AbstractDocument = 'AbstractDocument'
NAME_XMLDocument = 'XMLDocument'
NAME_WordDocument = 'WordDocument'
NAME_MHTDocument = 'MHTDocument'
NAME_ExcelDocument = 'ExcelDocument'
NAME_PowerPointDocument = 'PowerPointDocument'
NAME_GenericObj_ObjectID = 'ObjectID'
NAME_GenericObj_ReferenceParentID = 'ReferenceParentID'
NAME_GenericObj_StorageID = 'StorageID'
NAME_GenericObj_ObjectFormat = 'ObjectFormat'
NAME_GenericObj_ProtectionStatus = 'ProtectionStatus'
NAME_GenericObj_ObjectSize = 'ObjectSize'
NAME_GenericObj_AssociationType = 'AssociationType'
NAME_GenericObj_AssociationDesc = 'AssociationDesc'
NAME_GenericObj_ObjectFileName = 'ObjectFileName'
NAME_GenericObj_DateCreated = 'DateCreated'
NAME_GenericObj_DateModified = 'DateModified'
NAME_GenericObj_Keywords = 'Keywords'
NAME_GenericObj_ParentID = 'ParentID'
NAME_GenericObj_AllowedFolderContents = 'AllowedFolderContents'
NAME_GenericObj_Hidden = 'Hidden'
NAME_GenericObj_SystemObject = 'SystemObject'
NAME_GenericObj_PersistentUID = 'PersistentUID'
NAME_GenericObj_SyncID = 'SyncID'
NAME_GenericObj_PropertyBag = 'PropertyBag'
NAME_GenericObj_Name = 'Name'
NAME_MediaObj_Artist = 'Artist'
NAME_GenericObj_DateAuthored = 'DateAuthored'
NAME_GenericObj_Description = 'Description'
NAME_GenericObj_LanguageLocale = 'LanguageLocale'
NAME_GenericObj_Copyright = 'Copyright'
NAME_VideoObj_Source = 'Source'
NAME_MediaObj_GeographicOrigin = 'GeographicOrigin'
NAME_GenericObj_DateAdded = 'DateAdded'
NAME_GenericObj_NonConsumable = 'NonConsumable'
NAME_GenericObj_Corrupt = 'Corrupt'
NAME_MediaObj_Width = 'Width'
NAME_MediaObj_Height = 'Height'
NAME_MediaObj_Duration = 'Duration'
NAME_MediaObj_UserRating = 'UserRating'
NAME_MediaObj_Track = 'Track'
NAME_MediaObj_Genre = 'Genre'
NAME_MediaObj_Credits = 'Credits'
NAME_AudioObj_Lyrics = 'Lyrics'
NAME_MediaObj_SubscriptionContentID = 'SubscriptionContentID'
NAME_MediaObj_Producer = 'Producer'
NAME_MediaObj_UseCount = 'UseCount'
NAME_MediaObj_SkipCount = 'SkipCount'
NAME_GenericObj_DateAccessed = 'DateAccessed'
NAME_MediaObj_ParentalRating = 'ParentalRating'
NAME_MediaObj_MediaType = 'MediaType'
NAME_MediaObj_Composer = 'Composer'
NAME_MediaObj_EffectiveRating = 'EffectiveRating'
NAME_MediaObj_Subtitle = 'Subtitle'
NAME_MediaObj_DateOriginalRelease = 'DateOriginalRelease'
NAME_MediaObj_AlbumName = 'AlbumName'
NAME_MediaObj_AlbumArtist = 'AlbumArtist'
NAME_MediaObj_Mood = 'Mood'
NAME_GenericObj_DRMStatus = 'DRMStatus'
NAME_GenericObj_SubDescription = 'SubDescription'
NAME_ImageObj_IsCropped = 'IsCropped'
NAME_ImageObj_IsColorCorrected = 'IsColorCorrected'
NAME_ImageObj_ImageBitDepth = 'ImageBitDepth'
NAME_ImageObj_Aperature = 'Aperature'
NAME_ImageObj_Exposure = 'Exposure'
NAME_ImageObj_ISOSpeed = 'ISOSpeed'
NAME_MediaObj_Owner = 'Owner'
NAME_MediaObj_Editor = 'Editor'
NAME_MediaObj_WebMaster = 'WebMaster'
NAME_MediaObj_URLSource = 'URLSource'
NAME_MediaObj_URLLink = 'URLLink'
NAME_MediaObj_BookmarkTime = 'BookmarkTime'
NAME_MediaObj_BookmarkObject = 'BookmarkObject'
NAME_MediaObj_BookmarkByte = 'BookmarkByte'
NAME_GenericObj_DateRevised = 'DateRevised'
NAME_GenericObj_TimeToLive = 'TimeToLive'
NAME_MediaObj_MediaUID = 'MediaUID'
NAME_MediaObj_TotalBitRate = 'TotalBitRate'
NAME_MediaObj_BitRateType = 'BitRateType'
NAME_MediaObj_SampleRate = 'SampleRate'
NAME_AudioObj_Channels = 'Channels'
NAME_AudioObj_AudioBitDepth = 'AudioBitDepth'
NAME_AudioObj_AudioBlockAlignment = 'AudioBlockAlignment'
NAME_VideoObj_ScanType = 'ScanType'
NAME_AudioObj_AudioFormatCode = 'AudioFormatCode'
NAME_AudioObj_AudioBitRate = 'AudioBitRate'
NAME_VideoObj_VideoFormatCode = 'VideoFormatCode'
NAME_VideoObj_VideoBitRate = 'VideoBitRate'
NAME_VideoObj_VideoFrameRate = 'VideoFrameRate'
NAME_VideoObj_KeyFrameDistance = 'KeyFrameDistance'
NAME_MediaObj_BufferSize = 'BufferSize'
NAME_MediaObj_EncodingQuality = 'EncodingQuality'
NAME_MediaObj_EncodingProfile = 'EncodingProfile'
NAME_MediaObj_AudioEncodingProfile = 'AudioEncodingProfile'
DEVSVC_SERVICEINFO_VERSION = 100
DEVSVCTYPE_DEFAULT = 0
DEVSVCTYPE_ABSTRACT = 1
NAME_Services_ServiceDisplayName = 'ServiceDisplayName'
NAME_Services_ServiceIcon = 'ServiceIcon'
NAME_Services_ServiceLocale = 'ServiceLocale'
NAME_CalendarSvc = 'Calendar'
TYPE_CalendarSvc = 0
NAME_CalendarSvc_SyncWindowStart = 'SyncWindowStart'
NAME_CalendarSvc_SyncWindowEnd = 'SyncWindowEnd'
NAME_AbstractActivity = 'AbstractActivity'
NAME_AbstractActivityOccurrence = 'AbstractActivityOccurrence'
NAME_VCalendar1Activity = 'VCalendar1'
NAME_ICalendarActivity = 'ICalendar'
NAME_CalendarObj_Location = 'Location'
NAME_CalendarObj_Accepted = 'Accepted'
NAME_CalendarObj_Tentative = 'Tentative'
NAME_CalendarObj_Declined = 'Declined'
NAME_CalendarObj_TimeZone = 'TimeZone'
NAME_CalendarObj_ReminderOffset = 'ReminderOffset'
NAME_CalendarObj_BusyStatus = 'BusyStatus'
ENUM_CalendarObj_BusyStatusFree = 0
ENUM_CalendarObj_BusyStatusBusy = 1
ENUM_CalendarObj_BusyStatusOutOfOffice = 2
ENUM_CalendarObj_BusyStatusTentative = 3
NAME_CalendarObj_PatternStartTime = 'PatternStartTime'
NAME_CalendarObj_PatternDuration = 'PatternDuration'
NAME_CalendarObj_BeginDateTime = 'BeginDateTime'
NAME_CalendarObj_EndDateTime = 'EndDateTime'
NAME_HintsSvc = 'Hints'
TYPE_HintsSvc = 0
NAME_MessageSvc = 'Message'
TYPE_MessageSvc = 0
NAME_AbstractMessage = 'AbstractMessage'
NAME_AbstractMessageFolder = 'AbstractMessageFolder'
NAME_MessageObj_Subject = 'Subject'
NAME_MessageObj_Body = 'Body'
NAME_MessageObj_Priority = 'Priority'
ENUM_MessageObj_PriorityHighest = 2
ENUM_MessageObj_PriorityNormal = 1
ENUM_MessageObj_PriorityLowest = 0
NAME_MessageObj_Category = 'Category'
NAME_MessageObj_Sender = 'Sender'
NAME_MessageObj_To = 'To'
NAME_MessageObj_CC = 'CC'
NAME_MessageObj_BCC = 'BCC'
NAME_MessageObj_Read = 'Read'
ENUM_MessageObj_ReadFalse = 0
ENUM_MessageObj_ReadTrue = 255
NAME_MessageObj_ReceivedTime = 'ReceivedTime'
NAME_MessageObj_PatternOriginalDateTime = 'PatternOriginalDateTime'
NAME_MessageObj_PatternType = 'PatternType'
ENUM_MessageObj_PatternTypeDaily = 1
ENUM_MessageObj_PatternTypeWeekly = 2
ENUM_MessageObj_PatternTypeMonthly = 3
ENUM_MessageObj_PatternTypeYearly = 4
NAME_MessageObj_PatternValidStartDate = 'PatternValidStartDate'
NAME_MessageObj_PatternValidEndDate = 'PatternValidEndDate'
NAME_MessageObj_PatternPeriod = 'PatternPeriod'
NAME_MessageObj_PatternDayOfWeek = 'PatternDayOfWeek'
FLAG_MessageObj_DayOfWeekNone = 0
FLAG_MessageObj_DayOfWeekSunday = 1
FLAG_MessageObj_DayOfWeekMonday = 2
FLAG_MessageObj_DayOfWeekTuesday = 4
FLAG_MessageObj_DayOfWeekWednesday = 8
FLAG_MessageObj_DayOfWeekThursday = 16
FLAG_MessageObj_DayOfWeekFriday = 32
FLAG_MessageObj_DayOfWeekSaturday = 64
NAME_MessageObj_PatternDayOfMonth = 'PatternDayOfMonth'
RANGEMIN_MessageObj_PatternDayOfMonth = 1
RANGEMAX_MessageObj_PatternDayOfMonth = 31
RANGESTEP_MessageObj_PatternDayOfMonth = 1
NAME_MessageObj_PatternMonthOfYear = 'PatternMonthOfYear'
RANGEMIN_MessageObj_PatternMonthOfYear = 1
RANGEMAX_MessageObj_PatternMonthOfYear = 12
RANGESTEP_MessageObj_PatternMonthOfYear = 1
NAME_MessageObj_PatternInstance = 'PatternInstance'
ENUM_MessageObj_PatternInstanceNone = 0
ENUM_MessageObj_PatternInstanceFirst = 1
ENUM_MessageObj_PatternInstanceSecond = 2
ENUM_MessageObj_PatternInstanceThird = 3
ENUM_MessageObj_PatternInstanceFourth = 4
ENUM_MessageObj_PatternInstanceLast = 5
NAME_MessageObj_PatternDeleteDates = 'PatternDeleteDates'
NAME_DeviceMetadataSvc = 'Metadata'
TYPE_DeviceMetadataSvc = 0
NAME_DeviceMetadataCAB = 'DeviceMetadataCAB'
NAME_DeviceMetadataObj_ContentID = 'ContentID'
NAME_DeviceMetadataObj_DefaultCAB = 'DefaultCAB'
ENUM_DeviceMetadataObj_DefaultCABFalse = 0
ENUM_DeviceMetadataObj_DefaultCABTrue = 1
NAME_NotesSvc = 'Notes'
TYPE_NotesSvc = 0
NAME_AbstractNote = 'AbstractNote'
NAME_StatusSvc = 'Status'
TYPE_StatusSvc = 0
NAME_StatusSvc_SignalStrength = 'SignalStrength'
RANGEMIN_StatusSvc_SignalStrength = 0
RANGEMAX_StatusSvc_SignalStrength = 4
RANGESTEP_StatusSvc_SignalStrength = 1
NAME_StatusSvc_TextMessages = 'TextMessages'
RANGEMAX_StatusSvc_TextMessages = 255
NAME_StatusSvc_NewPictures = 'NewPictures'
RANGEMAX_StatusSvc_NewPictures = 65535
NAME_StatusSvc_MissedCalls = 'MissedCalls'
RANGEMAX_StatusSvc_MissedCalls = 255
NAME_StatusSvc_VoiceMail = 'VoiceMail'
RANGEMAX_StatusSvc_VoiceMail = 255
NAME_StatusSvc_NetworkName = 'NetworkName'
NAME_StatusSvc_NetworkType = 'NetworkType'
NAME_StatusSvc_Roaming = 'Roaming'
ENUM_StatusSvc_RoamingInactive = 0
ENUM_StatusSvc_RoamingActive = 1
ENUM_StatusSvc_RoamingUnknown = 2
NAME_StatusSvc_BatteryLife = 'BatteryLife'
RANGEMIN_StatusSvc_BatteryLife = 0
RANGEMAX_StatusSvc_BatteryLife = 100
RANGESTEP_StatusSvc_BatteryLife = 1
NAME_StatusSvc_ChargingState = 'ChargingState'
ENUM_StatusSvc_ChargingInactive = 0
ENUM_StatusSvc_ChargingActive = 1
ENUM_StatusSvc_ChargingUnknown = 2
NAME_StatusSvc_StorageCapacity = 'StorageCapacity'
NAME_StatusSvc_StorageFreeSpace = 'StorageFreeSpace'
NAME_SyncSvc_SyncFormat = 'SyncFormat'
NAME_SyncSvc_LocalOnlyDelete = 'LocalOnlyDelete'
NAME_SyncSvc_FilterType = 'FilterType'
SYNCSVC_FILTER_NONE = 0
SYNCSVC_FILTER_CONTACTS_WITH_PHONE = 1
SYNCSVC_FILTER_TASK_ACTIVE = 2
SYNCSVC_FILTER_CALENDAR_WINDOW_WITH_RECURRENCE = 3
NAME_SyncSvc_SyncObjectReferences = 'SyncObjectReferences'
ENUM_SyncSvc_SyncObjectReferencesDisabled = 0
ENUM_SyncSvc_SyncObjectReferencesEnabled = 255
NAME_SyncObj_LastAuthorProxyID = 'LastAuthorProxyID'
NAME_SyncSvc_BeginSync = 'BeginSync'
NAME_SyncSvc_EndSync = 'EndSync'
NAME_TasksSvc = 'Tasks'
TYPE_TasksSvc = 0
NAME_TasksSvc_SyncActiveOnly = 'FilterType'
NAME_AbstractTask = 'AbstractTask'
NAME_TaskObj_ReminderDateTime = 'ReminderDateTime'
NAME_TaskObj_Complete = 'Complete'
ENUM_TaskObj_CompleteFalse = 0
ENUM_TaskObj_CompleteTrue = 255
NAME_TaskObj_BeginDate = 'BeginDate'
NAME_TaskObj_EndDate = 'EndDate'
def _define_WPD_CATEGORY_MTP_EXT_VENDOR_OPERATIONS():
    return Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56')
def _define_WPD_COMMAND_MTP_EXT_GET_SUPPORTED_VENDOR_OPCODES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=11)
def _define_WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITHOUT_DATA_PHASE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=12)
def _define_WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITH_DATA_TO_READ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=13)
def _define_WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITH_DATA_TO_WRITE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=14)
def _define_WPD_COMMAND_MTP_EXT_READ_DATA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=15)
def _define_WPD_COMMAND_MTP_EXT_WRITE_DATA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=16)
def _define_WPD_COMMAND_MTP_EXT_END_DATA_TRANSFER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=17)
def _define_WPD_COMMAND_MTP_EXT_GET_VENDOR_EXTENSION_DESCRIPTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=18)
def _define_WPD_PROPERTY_MTP_EXT_OPERATION_CODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1001)
def _define_WPD_PROPERTY_MTP_EXT_OPERATION_PARAMS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1002)
def _define_WPD_PROPERTY_MTP_EXT_RESPONSE_CODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1003)
def _define_WPD_PROPERTY_MTP_EXT_RESPONSE_PARAMS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1004)
def _define_WPD_PROPERTY_MTP_EXT_VENDOR_OPERATION_CODES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1005)
def _define_WPD_PROPERTY_MTP_EXT_TRANSFER_CONTEXT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1006)
def _define_WPD_PROPERTY_MTP_EXT_TRANSFER_TOTAL_DATA_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1007)
def _define_WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_TO_READ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1008)
def _define_WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_READ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1009)
def _define_WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_TO_WRITE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1010)
def _define_WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_WRITTEN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1011)
def _define_WPD_PROPERTY_MTP_EXT_TRANSFER_DATA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1012)
def _define_WPD_PROPERTY_MTP_EXT_OPTIMAL_TRANSFER_BUFFER_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1013)
def _define_WPD_PROPERTY_MTP_EXT_VENDOR_EXTENSION_DESCRIPTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1014)
def _define_WPD_PROPERTIES_MTP_VENDOR_EXTENDED_OBJECT_PROPS():
    return Guid('4d545058-4fce-4578-95-c8-86-98-a9-bc-0f-49')
def _define_WPD_PROPERTIES_MTP_VENDOR_EXTENDED_DEVICE_PROPS():
    return Guid('4d545058-8900-40b3-8f-1d-dc-24-6e-1e-83-70')
def _define_WPD_EVENT_MTP_VENDOR_EXTENDED_EVENTS():
    return Guid('00000000-5738-4ff2-84-45-be-31-26-69-10-59')
def _define_WPD_PROPERTY_MTP_EXT_EVENT_PARAMS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-ef88-4e4d-95-c3-4f-32-7f-72-8a-96'), pid=1011)
def _define_CLSID_WPD_NAMESPACE_EXTENSION():
    return Guid('35786d3c-b075-49b9-88-dd-02-98-76-e1-1c-01')
def _define_WPDNSE_OBJECT_PROPERTIES_V1():
    return Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6')
def _define_WPDNSE_OBJECT_HAS_CONTACT_PHOTO():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=2)
def _define_WPDNSE_OBJECT_HAS_THUMBNAIL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=3)
def _define_WPDNSE_OBJECT_HAS_ICON():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=4)
def _define_WPDNSE_OBJECT_HAS_AUDIO_CLIP():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=5)
def _define_WPDNSE_OBJECT_HAS_ALBUM_ART():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=6)
def _define_WPDNSE_OBJECT_OPTIMAL_READ_BLOCK_SIZE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=7)
WPDNSE_PROPSHEET_DEVICE_GENERAL = 1
WPDNSE_PROPSHEET_STORAGE_GENERAL = 2
WPDNSE_PROPSHEET_CONTENT_GENERAL = 4
WPDNSE_PROPSHEET_CONTENT_REFERENCES = 8
WPDNSE_PROPSHEET_CONTENT_RESOURCES = 16
WPDNSE_PROPSHEET_CONTENT_DETAILS = 32
STR_WPDNSE_FAST_ENUM = 'WPDNSE Fast Enum'
STR_WPDNSE_SIMPLE_ITEM = 'WPDNSE SimpleItem'
NAME_ContactsSvc = 'Contacts'
TYPE_ContactsSvc = 0
NAME_ContactSvc_SyncWithPhoneOnly = 'FilterType'
NAME_AbstractContact = 'AbstractContact'
NAME_VCard2Contact = 'VCard2Contact'
NAME_VCard3Contact = 'VCard3Contact'
NAME_AbstractContactGroup = 'AbstractContactGroup'
NAME_ContactObj_GivenName = 'GivenName'
NAME_ContactObj_MiddleNames = 'MiddleNames'
NAME_ContactObj_FamilyName = 'FamilyName'
NAME_ContactObj_Title = 'Title'
NAME_ContactObj_Suffix = 'Suffix'
NAME_ContactObj_PhoneticGivenName = 'PhoneticGivenName'
NAME_ContactObj_PhoneticFamilyName = 'PhoneticFamilyName'
NAME_ContactObj_PersonalAddressFull = 'PersonalAddressFull'
NAME_ContactObj_PersonalAddressStreet = 'PersonalAddressStreet'
NAME_ContactObj_PersonalAddressLine2 = 'PersonalAddressLine2'
NAME_ContactObj_PersonalAddressCity = 'PersonalAddressCity'
NAME_ContactObj_PersonalAddressRegion = 'PersonalAddressRegion'
NAME_ContactObj_PersonalAddressPostalCode = 'PersonalAddressPostalCode'
NAME_ContactObj_PersonalAddressCountry = 'PersonalAddressCountry'
NAME_ContactObj_BusinessAddressFull = 'BusinessAddressFull'
NAME_ContactObj_BusinessAddressStreet = 'BusinessAddressStreet'
NAME_ContactObj_BusinessAddressLine2 = 'BusinessAddressLine2'
NAME_ContactObj_BusinessAddressCity = 'BusinessAddressCity'
NAME_ContactObj_BusinessAddressRegion = 'BusinessAddressRegion'
NAME_ContactObj_BusinessAddressPostalCode = 'BusinessAddressPostalCode'
NAME_ContactObj_BusinessAddressCountry = 'BusinessAddressCountry'
NAME_ContactObj_OtherAddressFull = 'OtherAddressFull'
NAME_ContactObj_OtherAddressStreet = 'OtherAddressStreet'
NAME_ContactObj_OtherAddressLine2 = 'OtherAddressLine2'
NAME_ContactObj_OtherAddressCity = 'OtherAddressCity'
NAME_ContactObj_OtherAddressRegion = 'OtherAddressRegion'
NAME_ContactObj_OtherAddressPostalCode = 'OtherAddressPostalCode'
NAME_ContactObj_OtherAddressCountry = 'OtherAddressCountry'
NAME_ContactObj_Email = 'Email'
NAME_ContactObj_PersonalEmail = 'PersonalEmail'
NAME_ContactObj_PersonalEmail2 = 'PersonalEmail2'
NAME_ContactObj_BusinessEmail = 'BusinessEmail'
NAME_ContactObj_BusinessEmail2 = 'BusinessEmail2'
NAME_ContactObj_OtherEmail = 'OtherEmail'
NAME_ContactObj_Phone = 'Phone'
NAME_ContactObj_PersonalPhone = 'PersonalPhone'
NAME_ContactObj_PersonalPhone2 = 'PersonalPhone2'
NAME_ContactObj_BusinessPhone = 'BusinessPhone'
NAME_ContactObj_BusinessPhone2 = 'BusinessPhone2'
NAME_ContactObj_MobilePhone = 'MobilePhone'
NAME_ContactObj_MobilePhone2 = 'MobilePhone2'
NAME_ContactObj_PersonalFax = 'PersonalFax'
NAME_ContactObj_BusinessFax = 'BusinessFax'
NAME_ContactObj_Pager = 'Pager'
NAME_ContactObj_OtherPhone = 'OtherPhone'
NAME_ContactObj_WebAddress = 'WebAddress'
NAME_ContactObj_PersonalWebAddress = 'PersonalWebAddress'
NAME_ContactObj_BusinessWebAddress = 'BusinessWebAddress'
NAME_ContactObj_IMAddress = 'IMAddress'
NAME_ContactObj_IMAddress2 = 'IMAddress2'
NAME_ContactObj_IMAddress3 = 'IMAddress3'
NAME_ContactObj_Organization = 'Organization'
NAME_ContactObj_PhoneticOrganization = 'PhoneticOrganization'
NAME_ContactObj_Role = 'Role'
NAME_ContactObj_Fax = 'Fax'
NAME_ContactObj_Spouse = 'Spouse'
NAME_ContactObj_Children = 'Children'
NAME_ContactObj_Assistant = 'Assistant'
NAME_ContactObj_Ringtone = 'Ringtone'
NAME_ContactObj_Birthdate = 'Birthdate'
NAME_ContactObj_AnniversaryDate = 'AnniversaryDate'
NAME_RingtonesSvc = 'Ringtones'
TYPE_RingtonesSvc = 0
NAME_RingtonesSvc_DefaultRingtone = 'DefaultRingtone'
NAME_AnchorSyncSvc = 'AnchorSync'
TYPE_AnchorSyncSvc = 1
NAME_AnchorSyncSvc_VersionProps = 'AnchorVersionProps'
NAME_AnchorSyncSvc_ReplicaID = 'AnchorReplicaID'
NAME_AnchorSyncSvc_KnowledgeObjectID = 'AnchorKnowledgeObjectID'
NAME_AnchorSyncSvc_LastSyncProxyID = 'AnchorLastSyncProxyID'
NAME_AnchorSyncSvc_CurrentAnchor = 'AnchorCurrentAnchor'
NAME_AnchorSyncSvc_ProviderVersion = 'AnchorProviderVersion'
NAME_AnchorSyncSvc_SyncFormat = 'SyncFormat'
NAME_AnchorSyncSvc_LocalOnlyDelete = 'LocalOnlyDelete'
NAME_AnchorSyncSvc_FilterType = 'FilterType'
NAME_AnchorSyncKnowledge = 'AnchorSyncKnowledge'
NAME_AnchorResults = 'AnchorResults'
NAME_AnchorResults_AnchorState = 'AnchorState'
ENUM_AnchorResults_AnchorStateNormal = 0
ENUM_AnchorResults_AnchorStateInvalid = 1
ENUM_AnchorResults_AnchorStateOld = 2
NAME_AnchorResults_Anchor = 'Anchor'
NAME_AnchorResults_ResultObjectID = 'ResultObjectID'
NAME_AnchorSyncSvc_GetChangesSinceAnchor = 'GetChangesSinceAnchor'
NAME_AnchorSyncSvc_BeginSync = 'BeginSync'
NAME_AnchorSyncSvc_EndSync = 'EndSync'
ENUM_AnchorResults_ItemStateInvalid = 0
ENUM_AnchorResults_ItemStateDeleted = 1
ENUM_AnchorResults_ItemStateCreated = 2
ENUM_AnchorResults_ItemStateUpdated = 3
ENUM_AnchorResults_ItemStateChanged = 4
NAME_FullEnumSyncSvc = 'FullEnumSync'
TYPE_FullEnumSyncSvc = 1
NAME_FullEnumSyncSvc_VersionProps = 'FullEnumVersionProps'
NAME_FullEnumSyncSvc_ReplicaID = 'FullEnumReplicaID'
NAME_FullEnumSyncSvc_KnowledgeObjectID = 'FullEnumKnowledgeObjectID'
NAME_FullEnumSyncSvc_LastSyncProxyID = 'FullEnumLastSyncProxyID'
NAME_FullEnumSyncSvc_ProviderVersion = 'FullEnumProviderVersion'
NAME_FullEnumSyncSvc_SyncFormat = 'SyncFormat'
NAME_FullEnumSyncSvc_LocalOnlyDelete = 'LocalOnlyDelete'
NAME_FullEnumSyncSvc_FilterType = 'FilterType'
NAME_FullEnumSyncKnowledge = 'FullEnumSyncKnowledge'
NAME_FullEnumSyncSvc_BeginSync = 'BeginSync'
NAME_FullEnumSyncSvc_EndSync = 'EndSync'
def _define_DMProcessConfigXMLFiltered():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.Foundation.BSTR))(('DMProcessConfigXMLFiltered', windll['DMProcessXMLFiltered.dll']), ((1, 'pszXmlIn'),(1, 'rgszAllowedCspNodes'),(1, 'dwNumAllowedCspNodes'),(1, 'pbstrXmlOut'),))
    except (FileNotFoundError, AttributeError):
        return None
DELETE_OBJECT_OPTIONS = Int32
PORTABLE_DEVICE_DELETE_NO_RECURSION = 0
PORTABLE_DEVICE_DELETE_WITH_RECURSION = 1
DEVICE_RADIO_STATE = Int32
DRS_RADIO_ON = 0
DRS_SW_RADIO_OFF = 1
DRS_HW_RADIO_OFF = 2
DRS_SW_HW_RADIO_OFF = 3
DRS_HW_RADIO_ON_UNCONTROLLABLE = 4
DRS_RADIO_INVALID = 5
DRS_HW_RADIO_OFF_UNCONTROLLABLE = 6
DRS_RADIO_MAX = 6
EnumBthMtpConnectors = Guid('a1570149-e645-4f43-8b-0d-40-9b-06-1d-b2-fc')
def _define_IConnectionRequestCallback_head():
    class IConnectionRequestCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('272c9ae0-7161-4ae0-91-bd-9f-44-8e-e9-c4-27')
    return IConnectionRequestCallback
def _define_IConnectionRequestCallback():
    IConnectionRequestCallback = win32more.Devices.PortableDevices.IConnectionRequestCallback_head
    IConnectionRequestCallback.OnComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(3, 'OnComplete', ((1, 'hrStatus'),)))
    win32more.System.Com.IUnknown
    return IConnectionRequestCallback
def _define_IEnumPortableDeviceConnectors_head():
    class IEnumPortableDeviceConnectors(win32more.System.Com.IUnknown_head):
        Guid = Guid('bfdef549-9247-454f-bd-82-06-fe-80-85-3f-aa')
    return IEnumPortableDeviceConnectors
def _define_IEnumPortableDeviceConnectors():
    IEnumPortableDeviceConnectors = win32more.Devices.PortableDevices.IEnumPortableDeviceConnectors_head
    IEnumPortableDeviceConnectors.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.PortableDevices.IPortableDeviceConnector_head),POINTER(UInt32))(3, 'Next', ((1, 'cRequested'),(1, 'pConnectors'),(1, 'pcFetched'),)))
    IEnumPortableDeviceConnectors.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'cConnectors'),)))
    IEnumPortableDeviceConnectors.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumPortableDeviceConnectors.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IEnumPortableDeviceConnectors_head))(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumPortableDeviceConnectors
def _define_IEnumPortableDeviceObjectIDs_head():
    class IEnumPortableDeviceObjectIDs(win32more.System.Com.IUnknown_head):
        Guid = Guid('10ece955-cf41-4728-bf-a0-41-ee-df-1b-bf-19')
    return IEnumPortableDeviceObjectIDs
def _define_IEnumPortableDeviceObjectIDs():
    IEnumPortableDeviceObjectIDs = win32more.Devices.PortableDevices.IEnumPortableDeviceObjectIDs_head
    IEnumPortableDeviceObjectIDs.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(3, 'Next', ((1, 'cObjects'),(1, 'pObjIDs'),(1, 'pcFetched'),)))
    IEnumPortableDeviceObjectIDs.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'cObjects'),)))
    IEnumPortableDeviceObjectIDs.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumPortableDeviceObjectIDs.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IEnumPortableDeviceObjectIDs_head))(6, 'Clone', ((1, 'ppEnum'),)))
    IEnumPortableDeviceObjectIDs.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Cancel', ()))
    win32more.System.Com.IUnknown
    return IEnumPortableDeviceObjectIDs
def _define_IMediaRadioManager_head():
    class IMediaRadioManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('6cfdcab5-fc47-42a5-92-41-07-4b-58-83-0e-73')
    return IMediaRadioManager
def _define_IMediaRadioManager():
    IMediaRadioManager = win32more.Devices.PortableDevices.IMediaRadioManager_head
    IMediaRadioManager.GetRadioInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IRadioInstanceCollection_head))(3, 'GetRadioInstances', ((1, 'ppCollection'),)))
    IMediaRadioManager.OnSystemRadioStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.SYSTEM_RADIO_STATE,UInt32)(4, 'OnSystemRadioStateChange', ((1, 'sysRadioState'),(1, 'uTimeoutSec'),)))
    win32more.System.Com.IUnknown
    return IMediaRadioManager
def _define_IMediaRadioManagerNotifySink_head():
    class IMediaRadioManagerNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('89d81f5f-c147-49ed-a1-1c-77-b2-0c-31-e7-c9')
    return IMediaRadioManagerNotifySink
def _define_IMediaRadioManagerNotifySink():
    IMediaRadioManagerNotifySink = win32more.Devices.PortableDevices.IMediaRadioManagerNotifySink_head
    IMediaRadioManagerNotifySink.OnInstanceAdd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IRadioInstance_head)(3, 'OnInstanceAdd', ((1, 'pRadioInstance'),)))
    IMediaRadioManagerNotifySink.OnInstanceRemove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(4, 'OnInstanceRemove', ((1, 'bstrRadioInstanceId'),)))
    IMediaRadioManagerNotifySink.OnInstanceRadioChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Devices.PortableDevices.DEVICE_RADIO_STATE)(5, 'OnInstanceRadioChange', ((1, 'bstrRadioInstanceId'),(1, 'radioState'),)))
    win32more.System.Com.IUnknown
    return IMediaRadioManagerNotifySink
def _define_IPortableDevice_head():
    class IPortableDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('625e2df8-6392-4cf0-9a-d1-3c-fa-5f-17-77-5c')
    return IPortableDevice
def _define_IPortableDevice():
    IPortableDevice = win32more.Devices.PortableDevices.IPortableDevice_head
    IPortableDevice.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head)(3, 'Open', ((1, 'pszPnPDeviceID'),(1, 'pClientInfo'),)))
    IPortableDevice.SendCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(4, 'SendCommand', ((1, 'dwFlags'),(1, 'pParameters'),(1, 'ppResults'),)))
    IPortableDevice.Content = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceContent_head))(5, 'Content', ((1, 'ppContent'),)))
    IPortableDevice.Capabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceCapabilities_head))(6, 'Capabilities', ((1, 'ppCapabilities'),)))
    IPortableDevice.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Cancel', ()))
    IPortableDevice.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Close', ()))
    IPortableDevice.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDeviceEventCallback_head,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Foundation.PWSTR))(9, 'Advise', ((1, 'dwFlags'),(1, 'pCallback'),(1, 'pParameters'),(1, 'ppszCookie'),)))
    IPortableDevice.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(10, 'Unadvise', ((1, 'pszCookie'),)))
    IPortableDevice.GetPnPDeviceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(11, 'GetPnPDeviceID', ((1, 'ppszPnPDeviceID'),)))
    win32more.System.Com.IUnknown
    return IPortableDevice
def _define_IPortableDeviceCapabilities_head():
    class IPortableDeviceCapabilities(win32more.System.Com.IUnknown_head):
        Guid = Guid('2c8c6dbf-e3dc-4061-be-cc-85-42-e8-10-d1-26')
    return IPortableDeviceCapabilities
def _define_IPortableDeviceCapabilities():
    IPortableDeviceCapabilities = win32more.Devices.PortableDevices.IPortableDeviceCapabilities_head
    IPortableDeviceCapabilities.GetSupportedCommands = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head))(3, 'GetSupportedCommands', ((1, 'ppCommands'),)))
    IPortableDeviceCapabilities.GetCommandOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(4, 'GetCommandOptions', ((1, 'Command'),(1, 'ppOptions'),)))
    IPortableDeviceCapabilities.GetFunctionalCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(5, 'GetFunctionalCategories', ((1, 'ppCategories'),)))
    IPortableDeviceCapabilities.GetFunctionalObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(6, 'GetFunctionalObjects', ((1, 'Category'),(1, 'ppObjectIDs'),)))
    IPortableDeviceCapabilities.GetSupportedContentTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(7, 'GetSupportedContentTypes', ((1, 'Category'),(1, 'ppContentTypes'),)))
    IPortableDeviceCapabilities.GetSupportedFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(8, 'GetSupportedFormats', ((1, 'ContentType'),(1, 'ppFormats'),)))
    IPortableDeviceCapabilities.GetSupportedFormatProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head))(9, 'GetSupportedFormatProperties', ((1, 'Format'),(1, 'ppKeys'),)))
    IPortableDeviceCapabilities.GetFixedPropertyAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(10, 'GetFixedPropertyAttributes', ((1, 'Format'),(1, 'Key'),(1, 'ppAttributes'),)))
    IPortableDeviceCapabilities.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'Cancel', ()))
    IPortableDeviceCapabilities.GetSupportedEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(12, 'GetSupportedEvents', ((1, 'ppEvents'),)))
    IPortableDeviceCapabilities.GetEventOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(13, 'GetEventOptions', ((1, 'Event'),(1, 'ppOptions'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceCapabilities
def _define_IPortableDeviceConnector_head():
    class IPortableDeviceConnector(win32more.System.Com.IUnknown_head):
        Guid = Guid('625e2df8-6392-4cf0-9a-d1-3c-fa-5f-17-77-5c')
    return IPortableDeviceConnector
def _define_IPortableDeviceConnector():
    IPortableDeviceConnector = win32more.Devices.PortableDevices.IPortableDeviceConnector_head
    IPortableDeviceConnector.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IConnectionRequestCallback_head)(3, 'Connect', ((1, 'pCallback'),)))
    IPortableDeviceConnector.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IConnectionRequestCallback_head)(4, 'Disconnect', ((1, 'pCallback'),)))
    IPortableDeviceConnector.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IConnectionRequestCallback_head)(5, 'Cancel', ((1, 'pCallback'),)))
    IPortableDeviceConnector.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Properties.DEVPROPKEY_head),POINTER(UInt32),POINTER(c_char_p_no),POINTER(UInt32))(6, 'GetProperty', ((1, 'pPropertyKey'),(1, 'pPropertyType'),(1, 'ppData'),(1, 'pcbData'),)))
    IPortableDeviceConnector.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Properties.DEVPROPKEY_head),UInt32,c_char_p_no,UInt32)(7, 'SetProperty', ((1, 'pPropertyKey'),(1, 'PropertyType'),(1, 'pData'),(1, 'cbData'),)))
    IPortableDeviceConnector.GetPnPID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(8, 'GetPnPID', ((1, 'ppwszPnPID'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceConnector
def _define_IPortableDeviceContent_head():
    class IPortableDeviceContent(win32more.System.Com.IUnknown_head):
        Guid = Guid('6a96ed84-7c73-4480-99-38-bf-5a-f4-77-d4-26')
    return IPortableDeviceContent
def _define_IPortableDeviceContent():
    IPortableDeviceContent = win32more.Devices.PortableDevices.IPortableDeviceContent_head
    IPortableDeviceContent.EnumObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IEnumPortableDeviceObjectIDs_head))(3, 'EnumObjects', ((1, 'dwFlags'),(1, 'pszParentObjectID'),(1, 'pFilter'),(1, 'ppEnum'),)))
    IPortableDeviceContent.Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceProperties_head))(4, 'Properties', ((1, 'ppProperties'),)))
    IPortableDeviceContent.Transfer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceResources_head))(5, 'Transfer', ((1, 'ppResources'),)))
    IPortableDeviceContent.CreateObjectWithPropertiesOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Foundation.PWSTR))(6, 'CreateObjectWithPropertiesOnly', ((1, 'pValues'),(1, 'ppszObjectID'),)))
    IPortableDeviceContent.CreateObjectWithPropertiesAndData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.System.Com.IStream_head),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(7, 'CreateObjectWithPropertiesAndData', ((1, 'pValues'),(1, 'ppData'),(1, 'pdwOptimalWriteBufferSize'),(1, 'ppszCookie'),)))
    IPortableDeviceContent.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(8, 'Delete', ((1, 'dwOptions'),(1, 'pObjectIDs'),(1, 'ppResults'),)))
    IPortableDeviceContent.GetObjectIDsFromPersistentUniqueIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(9, 'GetObjectIDsFromPersistentUniqueIDs', ((1, 'pPersistentUniqueIDs'),(1, 'ppObjectIDs'),)))
    IPortableDeviceContent.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'Cancel', ()))
    IPortableDeviceContent.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head,win32more.Foundation.PWSTR,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(11, 'Move', ((1, 'pObjectIDs'),(1, 'pszDestinationFolderObjectID'),(1, 'ppResults'),)))
    IPortableDeviceContent.Copy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head,win32more.Foundation.PWSTR,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(12, 'Copy', ((1, 'pObjectIDs'),(1, 'pszDestinationFolderObjectID'),(1, 'ppResults'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceContent
def _define_IPortableDeviceContent2_head():
    class IPortableDeviceContent2(win32more.Devices.PortableDevices.IPortableDeviceContent_head):
        Guid = Guid('9b4add96-f6bf-4034-87-08-ec-a7-2b-f1-05-54')
    return IPortableDeviceContent2
def _define_IPortableDeviceContent2():
    IPortableDeviceContent2 = win32more.Devices.PortableDevices.IPortableDeviceContent2_head
    IPortableDeviceContent2.UpdateObjectWithPropertiesAndData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.System.Com.IStream_head),POINTER(UInt32))(13, 'UpdateObjectWithPropertiesAndData', ((1, 'pszObjectID'),(1, 'pProperties'),(1, 'ppData'),(1, 'pdwOptimalWriteBufferSize'),)))
    win32more.Devices.PortableDevices.IPortableDeviceContent
    return IPortableDeviceContent2
def _define_IPortableDeviceDataStream_head():
    class IPortableDeviceDataStream(win32more.System.Com.IStream_head):
        Guid = Guid('88e04db3-1012-4d64-99-96-f7-03-a9-50-d3-f4')
    return IPortableDeviceDataStream
def _define_IPortableDeviceDataStream():
    IPortableDeviceDataStream = win32more.Devices.PortableDevices.IPortableDeviceDataStream_head
    IPortableDeviceDataStream.GetObjectID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(14, 'GetObjectID', ((1, 'ppszObjectID'),)))
    IPortableDeviceDataStream.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'Cancel', ()))
    win32more.System.Com.IStream
    return IPortableDeviceDataStream
def _define_IPortableDeviceDispatchFactory_head():
    class IPortableDeviceDispatchFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('5e1eafc3-e3d7-4132-96-fa-75-9c-0f-9d-1e-0f')
    return IPortableDeviceDispatchFactory
def _define_IPortableDeviceDispatchFactory():
    IPortableDeviceDispatchFactory = win32more.Devices.PortableDevices.IPortableDeviceDispatchFactory_head
    IPortableDeviceDispatchFactory.GetDeviceDispatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IDispatch_head))(3, 'GetDeviceDispatch', ((1, 'pszPnPDeviceID'),(1, 'ppDeviceDispatch'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceDispatchFactory
def _define_IPortableDeviceEventCallback_head():
    class IPortableDeviceEventCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('a8792a31-f385-493c-a8-93-40-f6-4e-b4-5f-6e')
    return IPortableDeviceEventCallback
def _define_IPortableDeviceEventCallback():
    IPortableDeviceEventCallback = win32more.Devices.PortableDevices.IPortableDeviceEventCallback_head
    IPortableDeviceEventCallback.OnEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head)(3, 'OnEvent', ((1, 'pEventParameters'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceEventCallback
def _define_IPortableDeviceKeyCollection_head():
    class IPortableDeviceKeyCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('dada2357-e0ad-492e-98-db-dd-61-c5-3b-a3-53')
    return IPortableDeviceKeyCollection
def _define_IPortableDeviceKeyCollection():
    IPortableDeviceKeyCollection = win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head
    IPortableDeviceKeyCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pcElems'),)))
    IPortableDeviceKeyCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(4, 'GetAt', ((1, 'dwIndex'),(1, 'pKey'),)))
    IPortableDeviceKeyCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(5, 'Add', ((1, 'Key'),)))
    IPortableDeviceKeyCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Clear', ()))
    IPortableDeviceKeyCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'RemoveAt', ((1, 'dwIndex'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceKeyCollection
def _define_IPortableDeviceManager_head():
    class IPortableDeviceManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1567595-4c2f-4574-a6-fa-ec-ef-91-7b-9a-40')
    return IPortableDeviceManager
def _define_IPortableDeviceManager():
    IPortableDeviceManager = win32more.Devices.PortableDevices.IPortableDeviceManager_head
    IPortableDeviceManager.GetDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(3, 'GetDevices', ((1, 'pPnPDeviceIDs'),(1, 'pcPnPDeviceIDs'),)))
    IPortableDeviceManager.RefreshDeviceList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'RefreshDeviceList', ()))
    IPortableDeviceManager.GetDeviceFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(5, 'GetDeviceFriendlyName', ((1, 'pszPnPDeviceID'),(1, 'pDeviceFriendlyName'),(1, 'pcchDeviceFriendlyName'),)))
    IPortableDeviceManager.GetDeviceDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(6, 'GetDeviceDescription', ((1, 'pszPnPDeviceID'),(1, 'pDeviceDescription'),(1, 'pcchDeviceDescription'),)))
    IPortableDeviceManager.GetDeviceManufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(7, 'GetDeviceManufacturer', ((1, 'pszPnPDeviceID'),(1, 'pDeviceManufacturer'),(1, 'pcchDeviceManufacturer'),)))
    IPortableDeviceManager.GetDeviceProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,POINTER(UInt32),POINTER(UInt32))(8, 'GetDeviceProperty', ((1, 'pszPnPDeviceID'),(1, 'pszDevicePropertyName'),(1, 'pData'),(1, 'pcbData'),(1, 'pdwType'),)))
    IPortableDeviceManager.GetPrivateDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(9, 'GetPrivateDevices', ((1, 'pPnPDeviceIDs'),(1, 'pcPnPDeviceIDs'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceManager
def _define_IPortableDeviceProperties_head():
    class IPortableDeviceProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('7f6d695c-03df-4439-a8-09-59-26-6b-ee-e3-a6')
    return IPortableDeviceProperties
def _define_IPortableDeviceProperties():
    IPortableDeviceProperties = win32more.Devices.PortableDevices.IPortableDeviceProperties_head
    IPortableDeviceProperties.GetSupportedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head))(3, 'GetSupportedProperties', ((1, 'pszObjectID'),(1, 'ppKeys'),)))
    IPortableDeviceProperties.GetPropertyAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(4, 'GetPropertyAttributes', ((1, 'pszObjectID'),(1, 'Key'),(1, 'ppAttributes'),)))
    IPortableDeviceProperties.GetValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(5, 'GetValues', ((1, 'pszObjectID'),(1, 'pKeys'),(1, 'ppValues'),)))
    IPortableDeviceProperties.SetValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(6, 'SetValues', ((1, 'pszObjectID'),(1, 'pValues'),(1, 'ppResults'),)))
    IPortableDeviceProperties.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head)(7, 'Delete', ((1, 'pszObjectID'),(1, 'pKeys'),)))
    IPortableDeviceProperties.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Cancel', ()))
    win32more.System.Com.IUnknown
    return IPortableDeviceProperties
def _define_IPortableDevicePropertiesBulk_head():
    class IPortableDevicePropertiesBulk(win32more.System.Com.IUnknown_head):
        Guid = Guid('482b05c0-4056-44ed-9e-0f-5e-23-b0-09-da-93')
    return IPortableDevicePropertiesBulk
def _define_IPortableDevicePropertiesBulk():
    IPortableDevicePropertiesBulk = win32more.Devices.PortableDevices.IPortableDevicePropertiesBulk_head
    IPortableDevicePropertiesBulk.QueueGetValuesByObjectList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head,win32more.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback_head,POINTER(Guid))(3, 'QueueGetValuesByObjectList', ((1, 'pObjectIDs'),(1, 'pKeys'),(1, 'pCallback'),(1, 'pContext'),)))
    IPortableDevicePropertiesBulk.QueueGetValuesByObjectFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head,win32more.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback_head,POINTER(Guid))(4, 'QueueGetValuesByObjectFormat', ((1, 'pguidObjectFormat'),(1, 'pszParentObjectID'),(1, 'dwDepth'),(1, 'pKeys'),(1, 'pCallback'),(1, 'pContext'),)))
    IPortableDevicePropertiesBulk.QueueSetValuesByObjectList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head,win32more.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback_head,POINTER(Guid))(5, 'QueueSetValuesByObjectList', ((1, 'pObjectValues'),(1, 'pCallback'),(1, 'pContext'),)))
    IPortableDevicePropertiesBulk.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(6, 'Start', ((1, 'pContext'),)))
    IPortableDevicePropertiesBulk.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(7, 'Cancel', ((1, 'pContext'),)))
    win32more.System.Com.IUnknown
    return IPortableDevicePropertiesBulk
def _define_IPortableDevicePropertiesBulkCallback_head():
    class IPortableDevicePropertiesBulkCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('9deacb80-11e8-40e3-a9-f3-f5-57-98-6a-78-45')
    return IPortableDevicePropertiesBulkCallback
def _define_IPortableDevicePropertiesBulkCallback():
    IPortableDevicePropertiesBulkCallback = win32more.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback_head
    IPortableDevicePropertiesBulkCallback.OnStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'OnStart', ((1, 'pContext'),)))
    IPortableDevicePropertiesBulkCallback.OnProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head)(4, 'OnProgress', ((1, 'pContext'),(1, 'pResults'),)))
    IPortableDevicePropertiesBulkCallback.OnEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.HRESULT)(5, 'OnEnd', ((1, 'pContext'),(1, 'hrStatus'),)))
    win32more.System.Com.IUnknown
    return IPortableDevicePropertiesBulkCallback
def _define_IPortableDevicePropVariantCollection_head():
    class IPortableDevicePropVariantCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('89b2e422-4f1b-4316-bc-ef-a4-4a-fe-a8-3e-b3')
    return IPortableDevicePropVariantCollection
def _define_IPortableDevicePropVariantCollection():
    IPortableDevicePropVariantCollection = win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head
    IPortableDevicePropVariantCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pcElems'),)))
    IPortableDevicePropVariantCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(4, 'GetAt', ((1, 'dwIndex'),(1, 'pValue'),)))
    IPortableDevicePropVariantCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(5, 'Add', ((1, 'pValue'),)))
    IPortableDevicePropVariantCollection.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16))(6, 'GetType', ((1, 'pvt'),)))
    IPortableDevicePropVariantCollection.ChangeType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16)(7, 'ChangeType', ((1, 'vt'),)))
    IPortableDevicePropVariantCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Clear', ()))
    IPortableDevicePropVariantCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(9, 'RemoveAt', ((1, 'dwIndex'),)))
    win32more.System.Com.IUnknown
    return IPortableDevicePropVariantCollection
def _define_IPortableDeviceResources_head():
    class IPortableDeviceResources(win32more.System.Com.IUnknown_head):
        Guid = Guid('fd8878ac-d841-4d17-89-1c-e6-82-9c-db-69-34')
    return IPortableDeviceResources
def _define_IPortableDeviceResources():
    IPortableDeviceResources = win32more.Devices.PortableDevices.IPortableDeviceResources_head
    IPortableDeviceResources.GetSupportedResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head))(3, 'GetSupportedResources', ((1, 'pszObjectID'),(1, 'ppKeys'),)))
    IPortableDeviceResources.GetResourceAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(4, 'GetResourceAttributes', ((1, 'pszObjectID'),(1, 'Key'),(1, 'ppResourceAttributes'),)))
    IPortableDeviceResources.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32,POINTER(UInt32),POINTER(win32more.System.Com.IStream_head))(5, 'GetStream', ((1, 'pszObjectID'),(1, 'Key'),(1, 'dwMode'),(1, 'pdwOptimalBufferSize'),(1, 'ppStream'),)))
    IPortableDeviceResources.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head)(6, 'Delete', ((1, 'pszObjectID'),(1, 'pKeys'),)))
    IPortableDeviceResources.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Cancel', ()))
    IPortableDeviceResources.CreateResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.System.Com.IStream_head),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(8, 'CreateResource', ((1, 'pResourceAttributes'),(1, 'ppData'),(1, 'pdwOptimalWriteBufferSize'),(1, 'ppszCookie'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceResources
def _define_IPortableDeviceService_head():
    class IPortableDeviceService(win32more.System.Com.IUnknown_head):
        Guid = Guid('d3bd3a44-d7b5-40a9-98-b7-2f-a4-d0-1d-ec-08')
    return IPortableDeviceService
def _define_IPortableDeviceService():
    IPortableDeviceService = win32more.Devices.PortableDevices.IPortableDeviceService_head
    IPortableDeviceService.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head)(3, 'Open', ((1, 'pszPnPServiceID'),(1, 'pClientInfo'),)))
    IPortableDeviceService.Capabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceServiceCapabilities_head))(4, 'Capabilities', ((1, 'ppCapabilities'),)))
    IPortableDeviceService.Content = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceContent2_head))(5, 'Content', ((1, 'ppContent'),)))
    IPortableDeviceService.Methods = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceServiceMethods_head))(6, 'Methods', ((1, 'ppMethods'),)))
    IPortableDeviceService.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Cancel', ()))
    IPortableDeviceService.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Close', ()))
    IPortableDeviceService.GetServiceObjectID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(9, 'GetServiceObjectID', ((1, 'ppszServiceObjectID'),)))
    IPortableDeviceService.GetPnPServiceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(10, 'GetPnPServiceID', ((1, 'ppszPnPServiceID'),)))
    IPortableDeviceService.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDeviceEventCallback_head,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Foundation.PWSTR))(11, 'Advise', ((1, 'dwFlags'),(1, 'pCallback'),(1, 'pParameters'),(1, 'ppszCookie'),)))
    IPortableDeviceService.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(12, 'Unadvise', ((1, 'pszCookie'),)))
    IPortableDeviceService.SendCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(13, 'SendCommand', ((1, 'dwFlags'),(1, 'pParameters'),(1, 'ppResults'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceService
def _define_IPortableDeviceServiceActivation_head():
    class IPortableDeviceServiceActivation(win32more.System.Com.IUnknown_head):
        Guid = Guid('e56b0534-d9b9-425c-9b-99-75-f9-7c-b3-d7-c8')
    return IPortableDeviceServiceActivation
def _define_IPortableDeviceServiceActivation():
    IPortableDeviceServiceActivation = win32more.Devices.PortableDevices.IPortableDeviceServiceActivation_head
    IPortableDeviceServiceActivation.OpenAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.PortableDevices.IPortableDeviceValues_head,win32more.Devices.PortableDevices.IPortableDeviceServiceOpenCallback_head)(3, 'OpenAsync', ((1, 'pszPnPServiceID'),(1, 'pClientInfo'),(1, 'pCallback'),)))
    IPortableDeviceServiceActivation.CancelOpenAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'CancelOpenAsync', ()))
    win32more.System.Com.IUnknown
    return IPortableDeviceServiceActivation
def _define_IPortableDeviceServiceCapabilities_head():
    class IPortableDeviceServiceCapabilities(win32more.System.Com.IUnknown_head):
        Guid = Guid('24dbd89d-413e-43e0-bd-5b-19-7f-3c-56-c8-86')
    return IPortableDeviceServiceCapabilities
def _define_IPortableDeviceServiceCapabilities():
    IPortableDeviceServiceCapabilities = win32more.Devices.PortableDevices.IPortableDeviceServiceCapabilities_head
    IPortableDeviceServiceCapabilities.GetSupportedMethods = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(3, 'GetSupportedMethods', ((1, 'ppMethods'),)))
    IPortableDeviceServiceCapabilities.GetSupportedMethodsByFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(4, 'GetSupportedMethodsByFormat', ((1, 'Format'),(1, 'ppMethods'),)))
    IPortableDeviceServiceCapabilities.GetMethodAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(5, 'GetMethodAttributes', ((1, 'Method'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetMethodParameterAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(6, 'GetMethodParameterAttributes', ((1, 'Method'),(1, 'Parameter'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetSupportedFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(7, 'GetSupportedFormats', ((1, 'ppFormats'),)))
    IPortableDeviceServiceCapabilities.GetFormatAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(8, 'GetFormatAttributes', ((1, 'Format'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetSupportedFormatProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head))(9, 'GetSupportedFormatProperties', ((1, 'Format'),(1, 'ppKeys'),)))
    IPortableDeviceServiceCapabilities.GetFormatPropertyAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(10, 'GetFormatPropertyAttributes', ((1, 'Format'),(1, 'Property'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetSupportedEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(11, 'GetSupportedEvents', ((1, 'ppEvents'),)))
    IPortableDeviceServiceCapabilities.GetEventAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(12, 'GetEventAttributes', ((1, 'Event'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetEventParameterAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(13, 'GetEventParameterAttributes', ((1, 'Event'),(1, 'Parameter'),(1, 'ppAttributes'),)))
    IPortableDeviceServiceCapabilities.GetInheritedServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(14, 'GetInheritedServices', ((1, 'dwInheritanceType'),(1, 'ppServices'),)))
    IPortableDeviceServiceCapabilities.GetFormatRenderingProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head))(15, 'GetFormatRenderingProfiles', ((1, 'Format'),(1, 'ppRenderingProfiles'),)))
    IPortableDeviceServiceCapabilities.GetSupportedCommands = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head))(16, 'GetSupportedCommands', ((1, 'ppCommands'),)))
    IPortableDeviceServiceCapabilities.GetCommandOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(17, 'GetCommandOptions', ((1, 'Command'),(1, 'ppOptions'),)))
    IPortableDeviceServiceCapabilities.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(18, 'Cancel', ()))
    win32more.System.Com.IUnknown
    return IPortableDeviceServiceCapabilities
def _define_IPortableDeviceServiceManager_head():
    class IPortableDeviceServiceManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('a8abc4e9-a84a-47a9-80-b3-c5-d9-b1-72-a9-61')
    return IPortableDeviceServiceManager
def _define_IPortableDeviceServiceManager():
    IPortableDeviceServiceManager = win32more.Devices.PortableDevices.IPortableDeviceServiceManager_head
    IPortableDeviceServiceManager.GetDeviceServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(3, 'GetDeviceServices', ((1, 'pszPnPDeviceID'),(1, 'guidServiceCategory'),(1, 'pServices'),(1, 'pcServices'),)))
    IPortableDeviceServiceManager.GetDeviceForService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(4, 'GetDeviceForService', ((1, 'pszPnPServiceID'),(1, 'ppszPnPDeviceID'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceServiceManager
def _define_IPortableDeviceServiceMethodCallback_head():
    class IPortableDeviceServiceMethodCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('c424233c-afce-4828-a7-56-7e-d7-a2-35-00-83')
    return IPortableDeviceServiceMethodCallback
def _define_IPortableDeviceServiceMethodCallback():
    IPortableDeviceServiceMethodCallback = win32more.Devices.PortableDevices.IPortableDeviceServiceMethodCallback_head
    IPortableDeviceServiceMethodCallback.OnComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head)(3, 'OnComplete', ((1, 'hrStatus'),(1, 'pResults'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceServiceMethodCallback
def _define_IPortableDeviceServiceMethods_head():
    class IPortableDeviceServiceMethods(win32more.System.Com.IUnknown_head):
        Guid = Guid('e20333c9-fd34-412d-a3-81-cc-6f-2d-82-0d-f7')
    return IPortableDeviceServiceMethods
def _define_IPortableDeviceServiceMethods():
    IPortableDeviceServiceMethods = win32more.Devices.PortableDevices.IPortableDeviceServiceMethods_head
    IPortableDeviceServiceMethods.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(3, 'Invoke', ((1, 'Method'),(1, 'pParameters'),(1, 'ppResults'),)))
    IPortableDeviceServiceMethods.InvokeAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Devices.PortableDevices.IPortableDeviceValues_head,win32more.Devices.PortableDevices.IPortableDeviceServiceMethodCallback_head)(4, 'InvokeAsync', ((1, 'Method'),(1, 'pParameters'),(1, 'pCallback'),)))
    IPortableDeviceServiceMethods.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceServiceMethodCallback_head)(5, 'Cancel', ((1, 'pCallback'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceServiceMethods
def _define_IPortableDeviceServiceOpenCallback_head():
    class IPortableDeviceServiceOpenCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('bced49c8-8efe-41ed-96-0b-61-31-3a-bd-47-a9')
    return IPortableDeviceServiceOpenCallback
def _define_IPortableDeviceServiceOpenCallback():
    IPortableDeviceServiceOpenCallback = win32more.Devices.PortableDevices.IPortableDeviceServiceOpenCallback_head
    IPortableDeviceServiceOpenCallback.OnComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(3, 'OnComplete', ((1, 'hrStatus'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceServiceOpenCallback
def _define_IPortableDeviceUnitsStream_head():
    class IPortableDeviceUnitsStream(win32more.System.Com.IUnknown_head):
        Guid = Guid('5e98025f-bfc4-47a2-9a-5f-bc-90-0a-50-7c-67')
    return IPortableDeviceUnitsStream
def _define_IPortableDeviceUnitsStream():
    IPortableDeviceUnitsStream = win32more.Devices.PortableDevices.IPortableDeviceUnitsStream_head
    IPortableDeviceUnitsStream.SeekInUnits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LARGE_INTEGER,win32more.Devices.PortableDevices.WPD_STREAM_UNITS,UInt32,POINTER(win32more.Foundation.ULARGE_INTEGER_head))(3, 'SeekInUnits', ((1, 'dlibMove'),(1, 'units'),(1, 'dwOrigin'),(1, 'plibNewPosition'),)))
    IPortableDeviceUnitsStream.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Cancel', ()))
    win32more.System.Com.IUnknown
    return IPortableDeviceUnitsStream
def _define_IPortableDeviceValues_head():
    class IPortableDeviceValues(win32more.System.Com.IUnknown_head):
        Guid = Guid('6848f6f2-3155-4f86-b6-f5-26-3e-ee-ab-31-43')
    return IPortableDeviceValues
def _define_IPortableDeviceValues():
    IPortableDeviceValues = win32more.Devices.PortableDevices.IPortableDeviceValues_head
    IPortableDeviceValues.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pcelt'),)))
    IPortableDeviceValues.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(4, 'GetAt', ((1, 'index'),(1, 'pKey'),(1, 'pValue'),)))
    IPortableDeviceValues.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(5, 'SetValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(6, 'GetValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetStringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Foundation.PWSTR)(7, 'SetStringValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetStringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.PWSTR))(8, 'GetStringValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetUnsignedIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32)(9, 'SetUnsignedIntegerValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetUnsignedIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(UInt32))(10, 'GetUnsignedIntegerValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetSignedIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),Int32)(11, 'SetSignedIntegerValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetSignedIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Int32))(12, 'GetSignedIntegerValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetUnsignedLargeIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt64)(13, 'SetUnsignedLargeIntegerValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetUnsignedLargeIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(UInt64))(14, 'GetUnsignedLargeIntegerValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetSignedLargeIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),Int64)(15, 'SetSignedLargeIntegerValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetSignedLargeIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Int64))(16, 'GetSignedLargeIntegerValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetFloatValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),Single)(17, 'SetFloatValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetFloatValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Single))(18, 'GetFloatValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetErrorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Foundation.HRESULT)(19, 'SetErrorValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetErrorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.HRESULT))(20, 'GetErrorValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetKeyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(21, 'SetKeyValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetKeyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(22, 'GetKeyValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetBoolValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Foundation.BOOL)(23, 'SetBoolValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetBoolValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.BOOL))(24, 'GetBoolValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetIUnknownValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.System.Com.IUnknown_head)(25, 'SetIUnknownValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetIUnknownValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.IUnknown_head))(26, 'GetIUnknownValue', ((1, 'key'),(1, 'ppValue'),)))
    IPortableDeviceValues.SetGuidValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Guid))(27, 'SetGuidValue', ((1, 'key'),(1, 'Value'),)))
    IPortableDeviceValues.GetGuidValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Guid))(28, 'GetGuidValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.SetBufferValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),c_char_p_no,UInt32)(29, 'SetBufferValue', ((1, 'key'),(1, 'pValue'),(1, 'cbValue'),)))
    IPortableDeviceValues.GetBufferValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(c_char_p_no),POINTER(UInt32))(30, 'GetBufferValue', ((1, 'key'),(1, 'ppValue'),(1, 'pcbValue'),)))
    IPortableDeviceValues.SetIPortableDeviceValuesValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Devices.PortableDevices.IPortableDeviceValues_head)(31, 'SetIPortableDeviceValuesValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetIPortableDeviceValuesValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(32, 'GetIPortableDeviceValuesValue', ((1, 'key'),(1, 'ppValue'),)))
    IPortableDeviceValues.SetIPortableDevicePropVariantCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)(33, 'SetIPortableDevicePropVariantCollectionValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetIPortableDevicePropVariantCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDevicePropVariantCollection_head))(34, 'GetIPortableDevicePropVariantCollectionValue', ((1, 'key'),(1, 'ppValue'),)))
    IPortableDeviceValues.SetIPortableDeviceKeyCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head)(35, 'SetIPortableDeviceKeyCollectionValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetIPortableDeviceKeyCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head))(36, 'GetIPortableDeviceKeyCollectionValue', ((1, 'key'),(1, 'ppValue'),)))
    IPortableDeviceValues.SetIPortableDeviceValuesCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head)(37, 'SetIPortableDeviceValuesCollectionValue', ((1, 'key'),(1, 'pValue'),)))
    IPortableDeviceValues.GetIPortableDeviceValuesCollectionValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head))(38, 'GetIPortableDeviceValuesCollectionValue', ((1, 'key'),(1, 'ppValue'),)))
    IPortableDeviceValues.RemoveValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(39, 'RemoveValue', ((1, 'key'),)))
    IPortableDeviceValues.CopyValuesFromPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)(40, 'CopyValuesFromPropertyStore', ((1, 'pStore'),)))
    IPortableDeviceValues.CopyValuesToPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)(41, 'CopyValuesToPropertyStore', ((1, 'pStore'),)))
    IPortableDeviceValues.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(42, 'Clear', ()))
    win32more.System.Com.IUnknown
    return IPortableDeviceValues
def _define_IPortableDeviceValuesCollection_head():
    class IPortableDeviceValuesCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('6e3f2d79-4e07-48c4-82-08-d8-c2-e5-af-4a-99')
    return IPortableDeviceValuesCollection
def _define_IPortableDeviceValuesCollection():
    IPortableDeviceValuesCollection = win32more.Devices.PortableDevices.IPortableDeviceValuesCollection_head
    IPortableDeviceValuesCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pcElems'),)))
    IPortableDeviceValuesCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(4, 'GetAt', ((1, 'dwIndex'),(1, 'ppValues'),)))
    IPortableDeviceValuesCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head)(5, 'Add', ((1, 'pValues'),)))
    IPortableDeviceValuesCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Clear', ()))
    IPortableDeviceValuesCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'RemoveAt', ((1, 'dwIndex'),)))
    win32more.System.Com.IUnknown
    return IPortableDeviceValuesCollection
def _define_IPortableDeviceWebControl_head():
    class IPortableDeviceWebControl(win32more.System.Com.IDispatch_head):
        Guid = Guid('94fc7953-5ca1-483a-8a-ee-df-52-e7-74-7d-00')
    return IPortableDeviceWebControl
def _define_IPortableDeviceWebControl():
    IPortableDeviceWebControl = win32more.Devices.PortableDevices.IPortableDeviceWebControl_head
    IPortableDeviceWebControl.GetDeviceFromId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head))(7, 'GetDeviceFromId', ((1, 'deviceId'),(1, 'ppDevice'),)))
    IPortableDeviceWebControl.GetDeviceFromIdAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head)(8, 'GetDeviceFromIdAsync', ((1, 'deviceId'),(1, 'pCompletionHandler'),(1, 'pErrorHandler'),)))
    win32more.System.Com.IDispatch
    return IPortableDeviceWebControl
def _define_IRadioInstance_head():
    class IRadioInstance(win32more.System.Com.IUnknown_head):
        Guid = Guid('70aa1c9e-f2b4-4c61-86-d3-6b-9f-b7-5f-d1-a2')
    return IRadioInstance
def _define_IRadioInstance():
    IRadioInstance = win32more.Devices.PortableDevices.IRadioInstance_head
    IRadioInstance.GetRadioManagerSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetRadioManagerSignature', ((1, 'pguidSignature'),)))
    IRadioInstance.GetInstanceSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'GetInstanceSignature', ((1, 'pbstrId'),)))
    IRadioInstance.GetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR))(5, 'GetFriendlyName', ((1, 'lcid'),(1, 'pbstrName'),)))
    IRadioInstance.GetRadioState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.DEVICE_RADIO_STATE))(6, 'GetRadioState', ((1, 'pRadioState'),)))
    IRadioInstance.SetRadioState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.DEVICE_RADIO_STATE,UInt32)(7, 'SetRadioState', ((1, 'radioState'),(1, 'uTimeoutSec'),)))
    IRadioInstance.IsMultiComm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(8, 'IsMultiComm', ()))
    IRadioInstance.IsAssociatingDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(9, 'IsAssociatingDevice', ()))
    win32more.System.Com.IUnknown
    return IRadioInstance
def _define_IRadioInstanceCollection_head():
    class IRadioInstanceCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('e5791fae-5665-4e0c-95-be-5f-de-31-64-41-85')
    return IRadioInstanceCollection
def _define_IRadioInstanceCollection():
    IRadioInstanceCollection = win32more.Devices.PortableDevices.IRadioInstanceCollection_head
    IRadioInstanceCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pcInstance'),)))
    IRadioInstanceCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.PortableDevices.IRadioInstance_head))(4, 'GetAt', ((1, 'uIndex'),(1, 'ppRadioInstance'),)))
    win32more.System.Com.IUnknown
    return IRadioInstanceCollection
def _define_IWpdSerializer_head():
    class IWpdSerializer(win32more.System.Com.IUnknown_head):
        Guid = Guid('b32f4002-bb27-45ff-af-4f-06-63-1c-1e-8d-ad')
    return IWpdSerializer
def _define_IWpdSerializer():
    IWpdSerializer = win32more.Devices.PortableDevices.IWpdSerializer_head
    IWpdSerializer.GetIPortableDeviceValuesFromBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(3, 'GetIPortableDeviceValuesFromBuffer', ((1, 'pBuffer'),(1, 'dwInputBufferLength'),(1, 'ppParams'),)))
    IWpdSerializer.WriteIPortableDeviceValuesToBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.PortableDevices.IPortableDeviceValues_head,c_char_p_no,POINTER(UInt32))(4, 'WriteIPortableDeviceValuesToBuffer', ((1, 'dwOutputBufferLength'),(1, 'pResults'),(1, 'pBuffer'),(1, 'pdwBytesWritten'),)))
    IWpdSerializer.GetBufferFromIPortableDeviceValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(c_char_p_no),POINTER(UInt32))(5, 'GetBufferFromIPortableDeviceValues', ((1, 'pSource'),(1, 'ppBuffer'),(1, 'pdwBufferSize'),)))
    IWpdSerializer.GetSerializedSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(UInt32))(6, 'GetSerializedSize', ((1, 'pSource'),(1, 'pdwSize'),)))
    win32more.System.Com.IUnknown
    return IWpdSerializer
PortableDevice = Guid('728a21c5-3d9e-48d7-98-10-86-48-48-f0-f4-04')
PortableDeviceDispatchFactory = Guid('43232233-8338-4658-ae-01-0b-4a-e8-30-b6-b0')
PortableDeviceFTM = Guid('f7c0039a-4762-488a-b4-b3-76-0e-f9-a1-ba-9b')
PortableDeviceKeyCollection = Guid('de2d022d-2480-43be-97-f0-d1-fa-2c-f9-8f-4f')
PortableDeviceManager = Guid('0af10cec-2ecd-4b92-95-81-34-f6-ae-06-37-f3')
PortableDevicePropVariantCollection = Guid('08a99e2f-6d6d-4b80-af-5a-ba-f2-bc-be-4c-b9')
PortableDeviceService = Guid('ef5db4c2-9312-422c-91-52-41-1c-d9-c4-dd-84')
PortableDeviceServiceFTM = Guid('1649b154-c794-497a-9b-03-f3-f0-12-13-02-f3')
PortableDeviceValues = Guid('0c15d503-d017-47ce-90-16-7b-3f-97-87-21-cc')
PortableDeviceValuesCollection = Guid('3882134d-14cf-4220-9c-b4-43-5f-86-d8-3f-60')
PortableDeviceWebControl = Guid('186dd02c-2dec-41b5-a7-d4-b5-90-56-fa-de-51')
SMS_MESSAGE_TYPES = Int32
SMS_TEXT_MESSAGE = 0
SMS_BINARY_MESSAGE = 1
SYSTEM_RADIO_STATE = Int32
SRS_RADIO_ENABLED = 0
SRS_RADIO_DISABLED = 1
WPD_BITRATE_TYPES = Int32
WPD_BITRATE_TYPE_UNUSED = 0
WPD_BITRATE_TYPE_DISCRETE = 1
WPD_BITRATE_TYPE_VARIABLE = 2
WPD_BITRATE_TYPE_FREE = 3
WPD_CAPTURE_MODES = Int32
WPD_CAPTURE_MODE_UNDEFINED = 0
WPD_CAPTURE_MODE_NORMAL = 1
WPD_CAPTURE_MODE_BURST = 2
WPD_CAPTURE_MODE_TIMELAPSE = 3
WPD_COLOR_CORRECTED_STATUS_VALUES = Int32
WPD_COLOR_CORRECTED_STATUS_NOT_CORRECTED = 0
WPD_COLOR_CORRECTED_STATUS_CORRECTED = 1
WPD_COLOR_CORRECTED_STATUS_SHOULD_NOT_BE_CORRECTED = 2
def _define_WPD_COMMAND_ACCESS_LOOKUP_ENTRY_head():
    class WPD_COMMAND_ACCESS_LOOKUP_ENTRY(Structure):
        pass
    return WPD_COMMAND_ACCESS_LOOKUP_ENTRY
def _define_WPD_COMMAND_ACCESS_LOOKUP_ENTRY():
    WPD_COMMAND_ACCESS_LOOKUP_ENTRY = win32more.Devices.PortableDevices.WPD_COMMAND_ACCESS_LOOKUP_ENTRY_head
    WPD_COMMAND_ACCESS_LOOKUP_ENTRY._fields_ = [
        ('Command', win32more.UI.Shell.PropertiesSystem.PROPERTYKEY),
        ('AccessType', UInt32),
        ('AccessProperty', win32more.UI.Shell.PropertiesSystem.PROPERTYKEY),
    ]
    return WPD_COMMAND_ACCESS_LOOKUP_ENTRY
WPD_COMMAND_ACCESS_TYPES = Int32
WPD_COMMAND_ACCESS_READ = 1
WPD_COMMAND_ACCESS_READWRITE = 3
WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_STGM_ACCESS = 4
WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_FILE_ACCESS = 8
WPD_COMMAND_ACCESS_FROM_ATTRIBUTE_WITH_METHOD_ACCESS = 16
WPD_CROPPED_STATUS_VALUES = Int32
WPD_CROPPED_STATUS_NOT_CROPPED = 0
WPD_CROPPED_STATUS_CROPPED = 1
WPD_CROPPED_STATUS_SHOULD_NOT_BE_CROPPED = 2
WPD_DEVICE_TRANSPORTS = Int32
WPD_DEVICE_TRANSPORT_UNSPECIFIED = 0
WPD_DEVICE_TRANSPORT_USB = 1
WPD_DEVICE_TRANSPORT_IP = 2
WPD_DEVICE_TRANSPORT_BLUETOOTH = 3
WPD_DEVICE_TYPES = Int32
WPD_DEVICE_TYPE_GENERIC = 0
WPD_DEVICE_TYPE_CAMERA = 1
WPD_DEVICE_TYPE_MEDIA_PLAYER = 2
WPD_DEVICE_TYPE_PHONE = 3
WPD_DEVICE_TYPE_VIDEO = 4
WPD_DEVICE_TYPE_PERSONAL_INFORMATION_MANAGER = 5
WPD_DEVICE_TYPE_AUDIO_RECORDER = 6
WPD_EFFECT_MODES = Int32
WPD_EFFECT_MODE_UNDEFINED = 0
WPD_EFFECT_MODE_COLOR = 1
WPD_EFFECT_MODE_BLACK_AND_WHITE = 2
WPD_EFFECT_MODE_SEPIA = 3
WPD_EXPOSURE_METERING_MODES = Int32
WPD_EXPOSURE_METERING_MODE_UNDEFINED = 0
WPD_EXPOSURE_METERING_MODE_AVERAGE = 1
WPD_EXPOSURE_METERING_MODE_CENTER_WEIGHTED_AVERAGE = 2
WPD_EXPOSURE_METERING_MODE_MULTI_SPOT = 3
WPD_EXPOSURE_METERING_MODE_CENTER_SPOT = 4
WPD_EXPOSURE_PROGRAM_MODES = Int32
WPD_EXPOSURE_PROGRAM_MODE_UNDEFINED = 0
WPD_EXPOSURE_PROGRAM_MODE_MANUAL = 1
WPD_EXPOSURE_PROGRAM_MODE_AUTO = 2
WPD_EXPOSURE_PROGRAM_MODE_APERTURE_PRIORITY = 3
WPD_EXPOSURE_PROGRAM_MODE_SHUTTER_PRIORITY = 4
WPD_EXPOSURE_PROGRAM_MODE_CREATIVE = 5
WPD_EXPOSURE_PROGRAM_MODE_ACTION = 6
WPD_EXPOSURE_PROGRAM_MODE_PORTRAIT = 7
WPD_FLASH_MODES = Int32
WPD_FLASH_MODE_UNDEFINED = 0
WPD_FLASH_MODE_AUTO = 1
WPD_FLASH_MODE_OFF = 2
WPD_FLASH_MODE_FILL = 3
WPD_FLASH_MODE_RED_EYE_AUTO = 4
WPD_FLASH_MODE_RED_EYE_FILL = 5
WPD_FLASH_MODE_EXTERNAL_SYNC = 6
WPD_FOCUS_METERING_MODES = Int32
WPD_FOCUS_METERING_MODE_UNDEFINED = 0
WPD_FOCUS_METERING_MODE_CENTER_SPOT = 1
WPD_FOCUS_METERING_MODE_MULTI_SPOT = 2
WPD_FOCUS_MODES = Int32
WPD_FOCUS_UNDEFINED = 0
WPD_FOCUS_MANUAL = 1
WPD_FOCUS_AUTOMATIC = 2
WPD_FOCUS_AUTOMATIC_MACRO = 3
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
WPD_OPERATION_STATES = Int32
WPD_OPERATION_STATE_UNSPECIFIED = 0
WPD_OPERATION_STATE_STARTED = 1
WPD_OPERATION_STATE_RUNNING = 2
WPD_OPERATION_STATE_PAUSED = 3
WPD_OPERATION_STATE_CANCELLED = 4
WPD_OPERATION_STATE_FINISHED = 5
WPD_OPERATION_STATE_ABORTED = 6
WPD_PARAMETER_USAGE_TYPES = Int32
WPD_PARAMETER_USAGE_RETURN = 0
WPD_PARAMETER_USAGE_IN = 1
WPD_PARAMETER_USAGE_OUT = 2
WPD_PARAMETER_USAGE_INOUT = 3
WPD_POWER_SOURCES = Int32
WPD_POWER_SOURCE_BATTERY = 0
WPD_POWER_SOURCE_EXTERNAL = 1
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES = Int32
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_OBJECT = 0
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_RESOURCE = 1
WPD_SECTION_DATA_UNITS_VALUES = Int32
WPD_SECTION_DATA_UNITS_BYTES = 0
WPD_SECTION_DATA_UNITS_MILLISECONDS = 1
WPD_SERVICE_INHERITANCE_TYPES = Int32
WPD_SERVICE_INHERITANCE_IMPLEMENTATION = 0
WPD_SMS_ENCODING_TYPES = Int32
SMS_ENCODING_7_BIT = 0
SMS_ENCODING_8_BIT = 1
SMS_ENCODING_UTF_16 = 2
WPD_STORAGE_ACCESS_CAPABILITY_VALUES = Int32
WPD_STORAGE_ACCESS_CAPABILITY_READWRITE = 0
WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITHOUT_OBJECT_DELETION = 1
WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITH_OBJECT_DELETION = 2
WPD_STORAGE_TYPE_VALUES = Int32
WPD_STORAGE_TYPE_UNDEFINED = 0
WPD_STORAGE_TYPE_FIXED_ROM = 1
WPD_STORAGE_TYPE_REMOVABLE_ROM = 2
WPD_STORAGE_TYPE_FIXED_RAM = 3
WPD_STORAGE_TYPE_REMOVABLE_RAM = 4
WPD_STREAM_UNITS = Int32
WPD_STREAM_UNITS_BYTES = 0
WPD_STREAM_UNITS_FRAMES = 1
WPD_STREAM_UNITS_ROWS = 2
WPD_STREAM_UNITS_MILLISECONDS = 4
WPD_STREAM_UNITS_MICROSECONDS = 8
WPD_VIDEO_SCAN_TYPES = Int32
WPD_VIDEO_SCAN_TYPE_UNUSED = 0
WPD_VIDEO_SCAN_TYPE_PROGRESSIVE = 1
WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_UPPER_FIRST = 2
WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_LOWER_FIRST = 3
WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_UPPER_FIRST = 4
WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_LOWER_FIRST = 5
WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE = 6
WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE_AND_PROGRESSIVE = 7
WPD_WHITE_BALANCE_SETTINGS = Int32
WPD_WHITE_BALANCE_UNDEFINED = 0
WPD_WHITE_BALANCE_MANUAL = 1
WPD_WHITE_BALANCE_AUTOMATIC = 2
WPD_WHITE_BALANCE_ONE_PUSH_AUTOMATIC = 3
WPD_WHITE_BALANCE_DAYLIGHT = 4
WPD_WHITE_BALANCE_FLORESCENT = 5
WPD_WHITE_BALANCE_TUNGSTEN = 6
WPD_WHITE_BALANCE_FLASH = 7
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
WpdSerializer = Guid('0b91a74b-ad7c-4a9d-b5-63-29-ee-f9-16-71-72')
__all__ = [
    "CLSID_WPD_NAMESPACE_EXTENSION",
    "DELETE_OBJECT_OPTIONS",
    "DEVICE_RADIO_STATE",
    "DEVPKEY_MTPBTH_IsConnected",
    "DEVSVCTYPE_ABSTRACT",
    "DEVSVCTYPE_DEFAULT",
    "DEVSVC_SERVICEINFO_VERSION",
    "DMProcessConfigXMLFiltered",
    "DRS_HW_RADIO_OFF",
    "DRS_HW_RADIO_OFF_UNCONTROLLABLE",
    "DRS_HW_RADIO_ON_UNCONTROLLABLE",
    "DRS_RADIO_INVALID",
    "DRS_RADIO_MAX",
    "DRS_RADIO_ON",
    "DRS_SW_HW_RADIO_OFF",
    "DRS_SW_RADIO_OFF",
    "ENUM_AnchorResults_AnchorStateInvalid",
    "ENUM_AnchorResults_AnchorStateNormal",
    "ENUM_AnchorResults_AnchorStateOld",
    "ENUM_AnchorResults_ItemStateChanged",
    "ENUM_AnchorResults_ItemStateCreated",
    "ENUM_AnchorResults_ItemStateDeleted",
    "ENUM_AnchorResults_ItemStateInvalid",
    "ENUM_AnchorResults_ItemStateUpdated",
    "ENUM_CalendarObj_BusyStatusBusy",
    "ENUM_CalendarObj_BusyStatusFree",
    "ENUM_CalendarObj_BusyStatusOutOfOffice",
    "ENUM_CalendarObj_BusyStatusTentative",
    "ENUM_DeviceMetadataObj_DefaultCABFalse",
    "ENUM_DeviceMetadataObj_DefaultCABTrue",
    "ENUM_MessageObj_PatternInstanceFirst",
    "ENUM_MessageObj_PatternInstanceFourth",
    "ENUM_MessageObj_PatternInstanceLast",
    "ENUM_MessageObj_PatternInstanceNone",
    "ENUM_MessageObj_PatternInstanceSecond",
    "ENUM_MessageObj_PatternInstanceThird",
    "ENUM_MessageObj_PatternTypeDaily",
    "ENUM_MessageObj_PatternTypeMonthly",
    "ENUM_MessageObj_PatternTypeWeekly",
    "ENUM_MessageObj_PatternTypeYearly",
    "ENUM_MessageObj_PriorityHighest",
    "ENUM_MessageObj_PriorityLowest",
    "ENUM_MessageObj_PriorityNormal",
    "ENUM_MessageObj_ReadFalse",
    "ENUM_MessageObj_ReadTrue",
    "ENUM_StatusSvc_ChargingActive",
    "ENUM_StatusSvc_ChargingInactive",
    "ENUM_StatusSvc_ChargingUnknown",
    "ENUM_StatusSvc_RoamingActive",
    "ENUM_StatusSvc_RoamingInactive",
    "ENUM_StatusSvc_RoamingUnknown",
    "ENUM_SyncSvc_SyncObjectReferencesDisabled",
    "ENUM_SyncSvc_SyncObjectReferencesEnabled",
    "ENUM_TaskObj_CompleteFalse",
    "ENUM_TaskObj_CompleteTrue",
    "E_WPD_DEVICE_ALREADY_OPENED",
    "E_WPD_DEVICE_IS_HUNG",
    "E_WPD_DEVICE_NOT_OPEN",
    "E_WPD_OBJECT_ALREADY_ATTACHED_TO_DEVICE",
    "E_WPD_OBJECT_ALREADY_ATTACHED_TO_SERVICE",
    "E_WPD_OBJECT_NOT_ATTACHED_TO_DEVICE",
    "E_WPD_OBJECT_NOT_ATTACHED_TO_SERVICE",
    "E_WPD_OBJECT_NOT_COMMITED",
    "E_WPD_SERVICE_ALREADY_OPENED",
    "E_WPD_SERVICE_BAD_PARAMETER_ORDER",
    "E_WPD_SERVICE_NOT_OPEN",
    "E_WPD_SMS_INVALID_MESSAGE_BODY",
    "E_WPD_SMS_INVALID_RECIPIENT",
    "E_WPD_SMS_SERVICE_UNAVAILABLE",
    "EnumBthMtpConnectors",
    "FACILITY_WPD",
    "FLAG_MessageObj_DayOfWeekFriday",
    "FLAG_MessageObj_DayOfWeekMonday",
    "FLAG_MessageObj_DayOfWeekNone",
    "FLAG_MessageObj_DayOfWeekSaturday",
    "FLAG_MessageObj_DayOfWeekSunday",
    "FLAG_MessageObj_DayOfWeekThursday",
    "FLAG_MessageObj_DayOfWeekTuesday",
    "FLAG_MessageObj_DayOfWeekWednesday",
    "GUID_DEVINTERFACE_WPD",
    "GUID_DEVINTERFACE_WPD_PRIVATE",
    "GUID_DEVINTERFACE_WPD_SERVICE",
    "IConnectionRequestCallback",
    "IEnumPortableDeviceConnectors",
    "IEnumPortableDeviceObjectIDs",
    "IMediaRadioManager",
    "IMediaRadioManagerNotifySink",
    "IOCTL_WPD_MESSAGE_READWRITE_ACCESS",
    "IOCTL_WPD_MESSAGE_READ_ACCESS",
    "IPortableDevice",
    "IPortableDeviceCapabilities",
    "IPortableDeviceConnector",
    "IPortableDeviceContent",
    "IPortableDeviceContent2",
    "IPortableDeviceDataStream",
    "IPortableDeviceDispatchFactory",
    "IPortableDeviceEventCallback",
    "IPortableDeviceKeyCollection",
    "IPortableDeviceManager",
    "IPortableDevicePropVariantCollection",
    "IPortableDeviceProperties",
    "IPortableDevicePropertiesBulk",
    "IPortableDevicePropertiesBulkCallback",
    "IPortableDeviceResources",
    "IPortableDeviceService",
    "IPortableDeviceServiceActivation",
    "IPortableDeviceServiceCapabilities",
    "IPortableDeviceServiceManager",
    "IPortableDeviceServiceMethodCallback",
    "IPortableDeviceServiceMethods",
    "IPortableDeviceServiceOpenCallback",
    "IPortableDeviceUnitsStream",
    "IPortableDeviceValues",
    "IPortableDeviceValuesCollection",
    "IPortableDeviceWebControl",
    "IRadioInstance",
    "IRadioInstanceCollection",
    "IWpdSerializer",
    "NAME_3GPP2File",
    "NAME_3GPPFile",
    "NAME_AACFile",
    "NAME_AIFFFile",
    "NAME_AMRFile",
    "NAME_ASFFile",
    "NAME_ASXPlaylist",
    "NAME_ATSCTSFile",
    "NAME_AVCHDFile",
    "NAME_AVIFile",
    "NAME_AbstractActivity",
    "NAME_AbstractActivityOccurrence",
    "NAME_AbstractAudioAlbum",
    "NAME_AbstractAudioPlaylist",
    "NAME_AbstractAudioVideoAlbum",
    "NAME_AbstractChapteredProduction",
    "NAME_AbstractContact",
    "NAME_AbstractContactGroup",
    "NAME_AbstractDocument",
    "NAME_AbstractImageAlbum",
    "NAME_AbstractMediacast",
    "NAME_AbstractMessage",
    "NAME_AbstractMessageFolder",
    "NAME_AbstractMultimediaAlbum",
    "NAME_AbstractNote",
    "NAME_AbstractTask",
    "NAME_AbstractVideoAlbum",
    "NAME_AbstractVideoPlaylist",
    "NAME_AnchorResults",
    "NAME_AnchorResults_Anchor",
    "NAME_AnchorResults_AnchorState",
    "NAME_AnchorResults_ResultObjectID",
    "NAME_AnchorSyncKnowledge",
    "NAME_AnchorSyncSvc",
    "NAME_AnchorSyncSvc_BeginSync",
    "NAME_AnchorSyncSvc_CurrentAnchor",
    "NAME_AnchorSyncSvc_EndSync",
    "NAME_AnchorSyncSvc_FilterType",
    "NAME_AnchorSyncSvc_GetChangesSinceAnchor",
    "NAME_AnchorSyncSvc_KnowledgeObjectID",
    "NAME_AnchorSyncSvc_LastSyncProxyID",
    "NAME_AnchorSyncSvc_LocalOnlyDelete",
    "NAME_AnchorSyncSvc_ProviderVersion",
    "NAME_AnchorSyncSvc_ReplicaID",
    "NAME_AnchorSyncSvc_SyncFormat",
    "NAME_AnchorSyncSvc_VersionProps",
    "NAME_Association",
    "NAME_AudibleFile",
    "NAME_AudioObj_AudioBitDepth",
    "NAME_AudioObj_AudioBitRate",
    "NAME_AudioObj_AudioBlockAlignment",
    "NAME_AudioObj_AudioFormatCode",
    "NAME_AudioObj_Channels",
    "NAME_AudioObj_Lyrics",
    "NAME_BMPImage",
    "NAME_CIFFImage",
    "NAME_CalendarObj_Accepted",
    "NAME_CalendarObj_BeginDateTime",
    "NAME_CalendarObj_BusyStatus",
    "NAME_CalendarObj_Declined",
    "NAME_CalendarObj_EndDateTime",
    "NAME_CalendarObj_Location",
    "NAME_CalendarObj_PatternDuration",
    "NAME_CalendarObj_PatternStartTime",
    "NAME_CalendarObj_ReminderOffset",
    "NAME_CalendarObj_Tentative",
    "NAME_CalendarObj_TimeZone",
    "NAME_CalendarSvc",
    "NAME_CalendarSvc_SyncWindowEnd",
    "NAME_CalendarSvc_SyncWindowStart",
    "NAME_ContactObj_AnniversaryDate",
    "NAME_ContactObj_Assistant",
    "NAME_ContactObj_Birthdate",
    "NAME_ContactObj_BusinessAddressCity",
    "NAME_ContactObj_BusinessAddressCountry",
    "NAME_ContactObj_BusinessAddressFull",
    "NAME_ContactObj_BusinessAddressLine2",
    "NAME_ContactObj_BusinessAddressPostalCode",
    "NAME_ContactObj_BusinessAddressRegion",
    "NAME_ContactObj_BusinessAddressStreet",
    "NAME_ContactObj_BusinessEmail",
    "NAME_ContactObj_BusinessEmail2",
    "NAME_ContactObj_BusinessFax",
    "NAME_ContactObj_BusinessPhone",
    "NAME_ContactObj_BusinessPhone2",
    "NAME_ContactObj_BusinessWebAddress",
    "NAME_ContactObj_Children",
    "NAME_ContactObj_Email",
    "NAME_ContactObj_FamilyName",
    "NAME_ContactObj_Fax",
    "NAME_ContactObj_GivenName",
    "NAME_ContactObj_IMAddress",
    "NAME_ContactObj_IMAddress2",
    "NAME_ContactObj_IMAddress3",
    "NAME_ContactObj_MiddleNames",
    "NAME_ContactObj_MobilePhone",
    "NAME_ContactObj_MobilePhone2",
    "NAME_ContactObj_Organization",
    "NAME_ContactObj_OtherAddressCity",
    "NAME_ContactObj_OtherAddressCountry",
    "NAME_ContactObj_OtherAddressFull",
    "NAME_ContactObj_OtherAddressLine2",
    "NAME_ContactObj_OtherAddressPostalCode",
    "NAME_ContactObj_OtherAddressRegion",
    "NAME_ContactObj_OtherAddressStreet",
    "NAME_ContactObj_OtherEmail",
    "NAME_ContactObj_OtherPhone",
    "NAME_ContactObj_Pager",
    "NAME_ContactObj_PersonalAddressCity",
    "NAME_ContactObj_PersonalAddressCountry",
    "NAME_ContactObj_PersonalAddressFull",
    "NAME_ContactObj_PersonalAddressLine2",
    "NAME_ContactObj_PersonalAddressPostalCode",
    "NAME_ContactObj_PersonalAddressRegion",
    "NAME_ContactObj_PersonalAddressStreet",
    "NAME_ContactObj_PersonalEmail",
    "NAME_ContactObj_PersonalEmail2",
    "NAME_ContactObj_PersonalFax",
    "NAME_ContactObj_PersonalPhone",
    "NAME_ContactObj_PersonalPhone2",
    "NAME_ContactObj_PersonalWebAddress",
    "NAME_ContactObj_Phone",
    "NAME_ContactObj_PhoneticFamilyName",
    "NAME_ContactObj_PhoneticGivenName",
    "NAME_ContactObj_PhoneticOrganization",
    "NAME_ContactObj_Ringtone",
    "NAME_ContactObj_Role",
    "NAME_ContactObj_Spouse",
    "NAME_ContactObj_Suffix",
    "NAME_ContactObj_Title",
    "NAME_ContactObj_WebAddress",
    "NAME_ContactSvc_SyncWithPhoneOnly",
    "NAME_ContactsSvc",
    "NAME_DPOFDocument",
    "NAME_DVBTSFile",
    "NAME_DeviceExecutable",
    "NAME_DeviceMetadataCAB",
    "NAME_DeviceMetadataObj_ContentID",
    "NAME_DeviceMetadataObj_DefaultCAB",
    "NAME_DeviceMetadataSvc",
    "NAME_DeviceScript",
    "NAME_EXIFImage",
    "NAME_ExcelDocument",
    "NAME_FLACFile",
    "NAME_FirmwareFile",
    "NAME_FlashPixImage",
    "NAME_FullEnumSyncKnowledge",
    "NAME_FullEnumSyncSvc",
    "NAME_FullEnumSyncSvc_BeginSync",
    "NAME_FullEnumSyncSvc_EndSync",
    "NAME_FullEnumSyncSvc_FilterType",
    "NAME_FullEnumSyncSvc_KnowledgeObjectID",
    "NAME_FullEnumSyncSvc_LastSyncProxyID",
    "NAME_FullEnumSyncSvc_LocalOnlyDelete",
    "NAME_FullEnumSyncSvc_ProviderVersion",
    "NAME_FullEnumSyncSvc_ReplicaID",
    "NAME_FullEnumSyncSvc_SyncFormat",
    "NAME_FullEnumSyncSvc_VersionProps",
    "NAME_GIFImage",
    "NAME_GenericObj_AllowedFolderContents",
    "NAME_GenericObj_AssociationDesc",
    "NAME_GenericObj_AssociationType",
    "NAME_GenericObj_Copyright",
    "NAME_GenericObj_Corrupt",
    "NAME_GenericObj_DRMStatus",
    "NAME_GenericObj_DateAccessed",
    "NAME_GenericObj_DateAdded",
    "NAME_GenericObj_DateAuthored",
    "NAME_GenericObj_DateCreated",
    "NAME_GenericObj_DateModified",
    "NAME_GenericObj_DateRevised",
    "NAME_GenericObj_Description",
    "NAME_GenericObj_Hidden",
    "NAME_GenericObj_Keywords",
    "NAME_GenericObj_LanguageLocale",
    "NAME_GenericObj_Name",
    "NAME_GenericObj_NonConsumable",
    "NAME_GenericObj_ObjectFileName",
    "NAME_GenericObj_ObjectFormat",
    "NAME_GenericObj_ObjectID",
    "NAME_GenericObj_ObjectSize",
    "NAME_GenericObj_ParentID",
    "NAME_GenericObj_PersistentUID",
    "NAME_GenericObj_PropertyBag",
    "NAME_GenericObj_ProtectionStatus",
    "NAME_GenericObj_ReferenceParentID",
    "NAME_GenericObj_StorageID",
    "NAME_GenericObj_SubDescription",
    "NAME_GenericObj_SyncID",
    "NAME_GenericObj_SystemObject",
    "NAME_GenericObj_TimeToLive",
    "NAME_HDPhotoImage",
    "NAME_HTMLDocument",
    "NAME_HintsSvc",
    "NAME_ICalendarActivity",
    "NAME_ImageObj_Aperature",
    "NAME_ImageObj_Exposure",
    "NAME_ImageObj_ISOSpeed",
    "NAME_ImageObj_ImageBitDepth",
    "NAME_ImageObj_IsColorCorrected",
    "NAME_ImageObj_IsCropped",
    "NAME_JFIFImage",
    "NAME_JP2Image",
    "NAME_JPEGXRImage",
    "NAME_JPXImage",
    "NAME_M3UPlaylist",
    "NAME_MHTDocument",
    "NAME_MP3File",
    "NAME_MPEG2File",
    "NAME_MPEG4File",
    "NAME_MPEGFile",
    "NAME_MPLPlaylist",
    "NAME_MediaObj_AlbumArtist",
    "NAME_MediaObj_AlbumName",
    "NAME_MediaObj_Artist",
    "NAME_MediaObj_AudioEncodingProfile",
    "NAME_MediaObj_BitRateType",
    "NAME_MediaObj_BookmarkByte",
    "NAME_MediaObj_BookmarkObject",
    "NAME_MediaObj_BookmarkTime",
    "NAME_MediaObj_BufferSize",
    "NAME_MediaObj_Composer",
    "NAME_MediaObj_Credits",
    "NAME_MediaObj_DateOriginalRelease",
    "NAME_MediaObj_Duration",
    "NAME_MediaObj_Editor",
    "NAME_MediaObj_EffectiveRating",
    "NAME_MediaObj_EncodingProfile",
    "NAME_MediaObj_EncodingQuality",
    "NAME_MediaObj_Genre",
    "NAME_MediaObj_GeographicOrigin",
    "NAME_MediaObj_Height",
    "NAME_MediaObj_MediaType",
    "NAME_MediaObj_MediaUID",
    "NAME_MediaObj_Mood",
    "NAME_MediaObj_Owner",
    "NAME_MediaObj_ParentalRating",
    "NAME_MediaObj_Producer",
    "NAME_MediaObj_SampleRate",
    "NAME_MediaObj_SkipCount",
    "NAME_MediaObj_SubscriptionContentID",
    "NAME_MediaObj_Subtitle",
    "NAME_MediaObj_TotalBitRate",
    "NAME_MediaObj_Track",
    "NAME_MediaObj_URLLink",
    "NAME_MediaObj_URLSource",
    "NAME_MediaObj_UseCount",
    "NAME_MediaObj_UserRating",
    "NAME_MediaObj_WebMaster",
    "NAME_MediaObj_Width",
    "NAME_MessageObj_BCC",
    "NAME_MessageObj_Body",
    "NAME_MessageObj_CC",
    "NAME_MessageObj_Category",
    "NAME_MessageObj_PatternDayOfMonth",
    "NAME_MessageObj_PatternDayOfWeek",
    "NAME_MessageObj_PatternDeleteDates",
    "NAME_MessageObj_PatternInstance",
    "NAME_MessageObj_PatternMonthOfYear",
    "NAME_MessageObj_PatternOriginalDateTime",
    "NAME_MessageObj_PatternPeriod",
    "NAME_MessageObj_PatternType",
    "NAME_MessageObj_PatternValidEndDate",
    "NAME_MessageObj_PatternValidStartDate",
    "NAME_MessageObj_Priority",
    "NAME_MessageObj_Read",
    "NAME_MessageObj_ReceivedTime",
    "NAME_MessageObj_Sender",
    "NAME_MessageObj_Subject",
    "NAME_MessageObj_To",
    "NAME_MessageSvc",
    "NAME_NotesSvc",
    "NAME_OGGFile",
    "NAME_PCDImage",
    "NAME_PICTImage",
    "NAME_PNGImage",
    "NAME_PSLPlaylist",
    "NAME_PowerPointDocument",
    "NAME_QCELPFile",
    "NAME_RingtonesSvc",
    "NAME_RingtonesSvc_DefaultRingtone",
    "NAME_Services_ServiceDisplayName",
    "NAME_Services_ServiceIcon",
    "NAME_Services_ServiceLocale",
    "NAME_StatusSvc",
    "NAME_StatusSvc_BatteryLife",
    "NAME_StatusSvc_ChargingState",
    "NAME_StatusSvc_MissedCalls",
    "NAME_StatusSvc_NetworkName",
    "NAME_StatusSvc_NetworkType",
    "NAME_StatusSvc_NewPictures",
    "NAME_StatusSvc_Roaming",
    "NAME_StatusSvc_SignalStrength",
    "NAME_StatusSvc_StorageCapacity",
    "NAME_StatusSvc_StorageFreeSpace",
    "NAME_StatusSvc_TextMessages",
    "NAME_StatusSvc_VoiceMail",
    "NAME_SyncObj_LastAuthorProxyID",
    "NAME_SyncSvc_BeginSync",
    "NAME_SyncSvc_EndSync",
    "NAME_SyncSvc_FilterType",
    "NAME_SyncSvc_LocalOnlyDelete",
    "NAME_SyncSvc_SyncFormat",
    "NAME_SyncSvc_SyncObjectReferences",
    "NAME_TIFFEPImage",
    "NAME_TIFFITImage",
    "NAME_TIFFImage",
    "NAME_TaskObj_BeginDate",
    "NAME_TaskObj_Complete",
    "NAME_TaskObj_EndDate",
    "NAME_TaskObj_ReminderDateTime",
    "NAME_TasksSvc",
    "NAME_TasksSvc_SyncActiveOnly",
    "NAME_TextDocument",
    "NAME_Undefined",
    "NAME_UndefinedAudio",
    "NAME_UndefinedCollection",
    "NAME_UndefinedDocument",
    "NAME_UndefinedVideo",
    "NAME_UnknownImage",
    "NAME_VCalendar1Activity",
    "NAME_VCard2Contact",
    "NAME_VCard3Contact",
    "NAME_VideoObj_KeyFrameDistance",
    "NAME_VideoObj_ScanType",
    "NAME_VideoObj_Source",
    "NAME_VideoObj_VideoBitRate",
    "NAME_VideoObj_VideoFormatCode",
    "NAME_VideoObj_VideoFrameRate",
    "NAME_WAVFile",
    "NAME_WBMPImage",
    "NAME_WMAFile",
    "NAME_WMVFile",
    "NAME_WPLPlaylist",
    "NAME_WordDocument",
    "NAME_XMLDocument",
    "PORTABLE_DEVICE_DELETE_NO_RECURSION",
    "PORTABLE_DEVICE_DELETE_WITH_RECURSION",
    "PORTABLE_DEVICE_DRM_SCHEME_PDDRM",
    "PORTABLE_DEVICE_DRM_SCHEME_WMDRM10_PD",
    "PORTABLE_DEVICE_ICON",
    "PORTABLE_DEVICE_IS_MASS_STORAGE",
    "PORTABLE_DEVICE_NAMESPACE_EXCLUDE_FROM_SHELL",
    "PORTABLE_DEVICE_NAMESPACE_THUMBNAIL_CONTENT_TYPES",
    "PORTABLE_DEVICE_NAMESPACE_TIMEOUT",
    "PORTABLE_DEVICE_TYPE",
    "PortableDevice",
    "PortableDeviceDispatchFactory",
    "PortableDeviceFTM",
    "PortableDeviceKeyCollection",
    "PortableDeviceManager",
    "PortableDevicePropVariantCollection",
    "PortableDeviceService",
    "PortableDeviceServiceFTM",
    "PortableDeviceValues",
    "PortableDeviceValuesCollection",
    "PortableDeviceWebControl",
    "RANGEMAX_MessageObj_PatternDayOfMonth",
    "RANGEMAX_MessageObj_PatternMonthOfYear",
    "RANGEMAX_StatusSvc_BatteryLife",
    "RANGEMAX_StatusSvc_MissedCalls",
    "RANGEMAX_StatusSvc_NewPictures",
    "RANGEMAX_StatusSvc_SignalStrength",
    "RANGEMAX_StatusSvc_TextMessages",
    "RANGEMAX_StatusSvc_VoiceMail",
    "RANGEMIN_MessageObj_PatternDayOfMonth",
    "RANGEMIN_MessageObj_PatternMonthOfYear",
    "RANGEMIN_StatusSvc_BatteryLife",
    "RANGEMIN_StatusSvc_SignalStrength",
    "RANGESTEP_MessageObj_PatternDayOfMonth",
    "RANGESTEP_MessageObj_PatternMonthOfYear",
    "RANGESTEP_StatusSvc_BatteryLife",
    "RANGESTEP_StatusSvc_SignalStrength",
    "SMS_BINARY_MESSAGE",
    "SMS_ENCODING_7_BIT",
    "SMS_ENCODING_8_BIT",
    "SMS_ENCODING_UTF_16",
    "SMS_MESSAGE_TYPES",
    "SMS_TEXT_MESSAGE",
    "SRS_RADIO_DISABLED",
    "SRS_RADIO_ENABLED",
    "STR_WPDNSE_FAST_ENUM",
    "STR_WPDNSE_SIMPLE_ITEM",
    "SYNCSVC_FILTER_CALENDAR_WINDOW_WITH_RECURRENCE",
    "SYNCSVC_FILTER_CONTACTS_WITH_PHONE",
    "SYNCSVC_FILTER_NONE",
    "SYNCSVC_FILTER_TASK_ACTIVE",
    "SYSTEM_RADIO_STATE",
    "TYPE_AnchorSyncSvc",
    "TYPE_CalendarSvc",
    "TYPE_ContactsSvc",
    "TYPE_DeviceMetadataSvc",
    "TYPE_FullEnumSyncSvc",
    "TYPE_HintsSvc",
    "TYPE_MessageSvc",
    "TYPE_NotesSvc",
    "TYPE_RingtonesSvc",
    "TYPE_StatusSvc",
    "TYPE_TasksSvc",
    "WPDNSE_OBJECT_HAS_ALBUM_ART",
    "WPDNSE_OBJECT_HAS_AUDIO_CLIP",
    "WPDNSE_OBJECT_HAS_CONTACT_PHOTO",
    "WPDNSE_OBJECT_HAS_ICON",
    "WPDNSE_OBJECT_HAS_THUMBNAIL",
    "WPDNSE_OBJECT_OPTIMAL_READ_BLOCK_SIZE",
    "WPDNSE_OBJECT_PROPERTIES_V1",
    "WPDNSE_PROPSHEET_CONTENT_DETAILS",
    "WPDNSE_PROPSHEET_CONTENT_GENERAL",
    "WPDNSE_PROPSHEET_CONTENT_REFERENCES",
    "WPDNSE_PROPSHEET_CONTENT_RESOURCES",
    "WPDNSE_PROPSHEET_DEVICE_GENERAL",
    "WPDNSE_PROPSHEET_STORAGE_GENERAL",
    "WPD_API_OPTIONS_V1",
    "WPD_API_OPTION_IOCTL_ACCESS",
    "WPD_API_OPTION_USE_CLEAR_DATA_STREAM",
    "WPD_APPOINTMENT_ACCEPTED_ATTENDEES",
    "WPD_APPOINTMENT_DECLINED_ATTENDEES",
    "WPD_APPOINTMENT_LOCATION",
    "WPD_APPOINTMENT_OBJECT_PROPERTIES_V1",
    "WPD_APPOINTMENT_OPTIONAL_ATTENDEES",
    "WPD_APPOINTMENT_REQUIRED_ATTENDEES",
    "WPD_APPOINTMENT_RESOURCES",
    "WPD_APPOINTMENT_TENTATIVE_ATTENDEES",
    "WPD_APPOINTMENT_TYPE",
    "WPD_AUDIO_BITRATE",
    "WPD_AUDIO_BIT_DEPTH",
    "WPD_AUDIO_BLOCK_ALIGNMENT",
    "WPD_AUDIO_CHANNEL_COUNT",
    "WPD_AUDIO_FORMAT_CODE",
    "WPD_BITRATE_TYPES",
    "WPD_BITRATE_TYPE_DISCRETE",
    "WPD_BITRATE_TYPE_FREE",
    "WPD_BITRATE_TYPE_UNUSED",
    "WPD_BITRATE_TYPE_VARIABLE",
    "WPD_CAPTURE_MODES",
    "WPD_CAPTURE_MODE_BURST",
    "WPD_CAPTURE_MODE_NORMAL",
    "WPD_CAPTURE_MODE_TIMELAPSE",
    "WPD_CAPTURE_MODE_UNDEFINED",
    "WPD_CATEGORY_CAPABILITIES",
    "WPD_CATEGORY_COMMON",
    "WPD_CATEGORY_DEVICE_HINTS",
    "WPD_CATEGORY_MEDIA_CAPTURE",
    "WPD_CATEGORY_MTP_EXT_VENDOR_OPERATIONS",
    "WPD_CATEGORY_NETWORK_CONFIGURATION",
    "WPD_CATEGORY_NULL",
    "WPD_CATEGORY_OBJECT_ENUMERATION",
    "WPD_CATEGORY_OBJECT_MANAGEMENT",
    "WPD_CATEGORY_OBJECT_PROPERTIES",
    "WPD_CATEGORY_OBJECT_PROPERTIES_BULK",
    "WPD_CATEGORY_OBJECT_RESOURCES",
    "WPD_CATEGORY_SERVICE_CAPABILITIES",
    "WPD_CATEGORY_SERVICE_COMMON",
    "WPD_CATEGORY_SERVICE_METHODS",
    "WPD_CATEGORY_SMS",
    "WPD_CATEGORY_STILL_IMAGE_CAPTURE",
    "WPD_CATEGORY_STORAGE",
    "WPD_CLASS_EXTENSION_OPTIONS_DEVICE_IDENTIFICATION_VALUES",
    "WPD_CLASS_EXTENSION_OPTIONS_DONT_REGISTER_WPD_DEVICE_INTERFACE",
    "WPD_CLASS_EXTENSION_OPTIONS_MULTITRANSPORT_MODE",
    "WPD_CLASS_EXTENSION_OPTIONS_REGISTER_WPD_PRIVATE_DEVICE_INTERFACE",
    "WPD_CLASS_EXTENSION_OPTIONS_SILENCE_AUTOPLAY",
    "WPD_CLASS_EXTENSION_OPTIONS_SUPPORTED_CONTENT_TYPES",
    "WPD_CLASS_EXTENSION_OPTIONS_TRANSPORT_BANDWIDTH",
    "WPD_CLASS_EXTENSION_OPTIONS_V1",
    "WPD_CLASS_EXTENSION_OPTIONS_V2",
    "WPD_CLASS_EXTENSION_OPTIONS_V3",
    "WPD_CLASS_EXTENSION_V1",
    "WPD_CLASS_EXTENSION_V2",
    "WPD_CLIENT_DESIRED_ACCESS",
    "WPD_CLIENT_EVENT_COOKIE",
    "WPD_CLIENT_INFORMATION_PROPERTIES_V1",
    "WPD_CLIENT_MAJOR_VERSION",
    "WPD_CLIENT_MANUAL_CLOSE_ON_DISCONNECT",
    "WPD_CLIENT_MINIMUM_RESULTS_BUFFER_SIZE",
    "WPD_CLIENT_MINOR_VERSION",
    "WPD_CLIENT_NAME",
    "WPD_CLIENT_REVISION",
    "WPD_CLIENT_SECURITY_QUALITY_OF_SERVICE",
    "WPD_CLIENT_SHARE_MODE",
    "WPD_CLIENT_WMDRM_APPLICATION_CERTIFICATE",
    "WPD_CLIENT_WMDRM_APPLICATION_PRIVATE_KEY",
    "WPD_COLOR_CORRECTED_STATUS_CORRECTED",
    "WPD_COLOR_CORRECTED_STATUS_NOT_CORRECTED",
    "WPD_COLOR_CORRECTED_STATUS_SHOULD_NOT_BE_CORRECTED",
    "WPD_COLOR_CORRECTED_STATUS_VALUES",
    "WPD_COMMAND_ACCESS_FROM_ATTRIBUTE_WITH_METHOD_ACCESS",
    "WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_FILE_ACCESS",
    "WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_STGM_ACCESS",
    "WPD_COMMAND_ACCESS_LOOKUP_ENTRY",
    "WPD_COMMAND_ACCESS_READ",
    "WPD_COMMAND_ACCESS_READWRITE",
    "WPD_COMMAND_ACCESS_TYPES",
    "WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS",
    "WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS",
    "WPD_COMMAND_CAPABILITIES_GET_FIXED_PROPERTY_ATTRIBUTES",
    "WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS",
    "WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS",
    "WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES",
    "WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS",
    "WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS",
    "WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES",
    "WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES",
    "WPD_COMMAND_CLASS_EXTENSION_REGISTER_SERVICE_INTERFACES",
    "WPD_COMMAND_CLASS_EXTENSION_UNREGISTER_SERVICE_INTERFACES",
    "WPD_COMMAND_CLASS_EXTENSION_WRITE_DEVICE_INFORMATION",
    "WPD_COMMAND_COMMIT_KEYPAIR",
    "WPD_COMMAND_COMMON_GET_OBJECT_IDS_FROM_PERSISTENT_UNIQUE_IDS",
    "WPD_COMMAND_COMMON_RESET_DEVICE",
    "WPD_COMMAND_COMMON_SAVE_CLIENT_INFORMATION",
    "WPD_COMMAND_DEVICE_HINTS_GET_CONTENT_LOCATION",
    "WPD_COMMAND_GENERATE_KEYPAIR",
    "WPD_COMMAND_MEDIA_CAPTURE_PAUSE",
    "WPD_COMMAND_MEDIA_CAPTURE_START",
    "WPD_COMMAND_MEDIA_CAPTURE_STOP",
    "WPD_COMMAND_MTP_EXT_END_DATA_TRANSFER",
    "WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITHOUT_DATA_PHASE",
    "WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITH_DATA_TO_READ",
    "WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITH_DATA_TO_WRITE",
    "WPD_COMMAND_MTP_EXT_GET_SUPPORTED_VENDOR_OPCODES",
    "WPD_COMMAND_MTP_EXT_GET_VENDOR_EXTENSION_DESCRIPTION",
    "WPD_COMMAND_MTP_EXT_READ_DATA",
    "WPD_COMMAND_MTP_EXT_WRITE_DATA",
    "WPD_COMMAND_OBJECT_ENUMERATION_END_FIND",
    "WPD_COMMAND_OBJECT_ENUMERATION_FIND_NEXT",
    "WPD_COMMAND_OBJECT_ENUMERATION_START_FIND",
    "WPD_COMMAND_OBJECT_MANAGEMENT_COMMIT_OBJECT",
    "WPD_COMMAND_OBJECT_MANAGEMENT_COPY_OBJECTS",
    "WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_AND_DATA",
    "WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_ONLY",
    "WPD_COMMAND_OBJECT_MANAGEMENT_DELETE_OBJECTS",
    "WPD_COMMAND_OBJECT_MANAGEMENT_MOVE_OBJECTS",
    "WPD_COMMAND_OBJECT_MANAGEMENT_REVERT_OBJECT",
    "WPD_COMMAND_OBJECT_MANAGEMENT_UPDATE_OBJECT_WITH_PROPERTIES_AND_DATA",
    "WPD_COMMAND_OBJECT_MANAGEMENT_WRITE_OBJECT_DATA",
    "WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_END",
    "WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_NEXT",
    "WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_START",
    "WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_END",
    "WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_NEXT",
    "WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_START",
    "WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_END",
    "WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_NEXT",
    "WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_START",
    "WPD_COMMAND_OBJECT_PROPERTIES_DELETE",
    "WPD_COMMAND_OBJECT_PROPERTIES_GET",
    "WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL",
    "WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES",
    "WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED",
    "WPD_COMMAND_OBJECT_PROPERTIES_SET",
    "WPD_COMMAND_OBJECT_RESOURCES_CLOSE",
    "WPD_COMMAND_OBJECT_RESOURCES_COMMIT",
    "WPD_COMMAND_OBJECT_RESOURCES_CREATE_RESOURCE",
    "WPD_COMMAND_OBJECT_RESOURCES_DELETE",
    "WPD_COMMAND_OBJECT_RESOURCES_GET_ATTRIBUTES",
    "WPD_COMMAND_OBJECT_RESOURCES_GET_SUPPORTED",
    "WPD_COMMAND_OBJECT_RESOURCES_OPEN",
    "WPD_COMMAND_OBJECT_RESOURCES_READ",
    "WPD_COMMAND_OBJECT_RESOURCES_REVERT",
    "WPD_COMMAND_OBJECT_RESOURCES_SEEK",
    "WPD_COMMAND_OBJECT_RESOURCES_SEEK_IN_UNITS",
    "WPD_COMMAND_OBJECT_RESOURCES_WRITE",
    "WPD_COMMAND_PROCESS_WIRELESS_PROFILE",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_COMMAND_OPTIONS",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_ATTRIBUTES",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_PARAMETER_ATTRIBUTES",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_ATTRIBUTES",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_PROPERTY_ATTRIBUTES",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_RENDERING_PROFILES",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_INHERITED_SERVICES",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_ATTRIBUTES",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_PARAMETER_ATTRIBUTES",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_COMMANDS",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_EVENTS",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMATS",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS",
    "WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS_BY_FORMAT",
    "WPD_COMMAND_SERVICE_COMMON_GET_SERVICE_OBJECT_ID",
    "WPD_COMMAND_SERVICE_METHODS_CANCEL_INVOKE",
    "WPD_COMMAND_SERVICE_METHODS_END_INVOKE",
    "WPD_COMMAND_SERVICE_METHODS_START_INVOKE",
    "WPD_COMMAND_SMS_SEND",
    "WPD_COMMAND_STILL_IMAGE_CAPTURE_INITIATE",
    "WPD_COMMAND_STORAGE_EJECT",
    "WPD_COMMAND_STORAGE_FORMAT",
    "WPD_COMMON_INFORMATION_BODY_TEXT",
    "WPD_COMMON_INFORMATION_END_DATETIME",
    "WPD_COMMON_INFORMATION_NOTES",
    "WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1",
    "WPD_COMMON_INFORMATION_PRIORITY",
    "WPD_COMMON_INFORMATION_START_DATETIME",
    "WPD_COMMON_INFORMATION_SUBJECT",
    "WPD_CONTACT_ANNIVERSARY_DATE",
    "WPD_CONTACT_ASSISTANT",
    "WPD_CONTACT_BIRTHDATE",
    "WPD_CONTACT_BUSINESS_EMAIL",
    "WPD_CONTACT_BUSINESS_EMAIL2",
    "WPD_CONTACT_BUSINESS_FAX",
    "WPD_CONTACT_BUSINESS_FULL_POSTAL_ADDRESS",
    "WPD_CONTACT_BUSINESS_PHONE",
    "WPD_CONTACT_BUSINESS_PHONE2",
    "WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_CITY",
    "WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_COUNTRY",
    "WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE1",
    "WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE2",
    "WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_POSTAL_CODE",
    "WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_REGION",
    "WPD_CONTACT_BUSINESS_WEB_ADDRESS",
    "WPD_CONTACT_CHILDREN",
    "WPD_CONTACT_COMPANY_NAME",
    "WPD_CONTACT_DISPLAY_NAME",
    "WPD_CONTACT_FIRST_NAME",
    "WPD_CONTACT_INSTANT_MESSENGER",
    "WPD_CONTACT_INSTANT_MESSENGER2",
    "WPD_CONTACT_INSTANT_MESSENGER3",
    "WPD_CONTACT_LAST_NAME",
    "WPD_CONTACT_MIDDLE_NAMES",
    "WPD_CONTACT_MOBILE_PHONE",
    "WPD_CONTACT_MOBILE_PHONE2",
    "WPD_CONTACT_OBJECT_PROPERTIES_V1",
    "WPD_CONTACT_OTHER_EMAILS",
    "WPD_CONTACT_OTHER_FULL_POSTAL_ADDRESS",
    "WPD_CONTACT_OTHER_PHONES",
    "WPD_CONTACT_OTHER_POSTAL_ADDRESS_CITY",
    "WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE1",
    "WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE2",
    "WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_CODE",
    "WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_COUNTRY",
    "WPD_CONTACT_OTHER_POSTAL_ADDRESS_REGION",
    "WPD_CONTACT_PAGER",
    "WPD_CONTACT_PERSONAL_EMAIL",
    "WPD_CONTACT_PERSONAL_EMAIL2",
    "WPD_CONTACT_PERSONAL_FAX",
    "WPD_CONTACT_PERSONAL_FULL_POSTAL_ADDRESS",
    "WPD_CONTACT_PERSONAL_PHONE",
    "WPD_CONTACT_PERSONAL_PHONE2",
    "WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_CITY",
    "WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_COUNTRY",
    "WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE1",
    "WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE2",
    "WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_POSTAL_CODE",
    "WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_REGION",
    "WPD_CONTACT_PERSONAL_WEB_ADDRESS",
    "WPD_CONTACT_PHONETIC_COMPANY_NAME",
    "WPD_CONTACT_PHONETIC_FIRST_NAME",
    "WPD_CONTACT_PHONETIC_LAST_NAME",
    "WPD_CONTACT_PREFIX",
    "WPD_CONTACT_PRIMARY_EMAIL_ADDRESS",
    "WPD_CONTACT_PRIMARY_FAX",
    "WPD_CONTACT_PRIMARY_PHONE",
    "WPD_CONTACT_PRIMARY_WEB_ADDRESS",
    "WPD_CONTACT_RINGTONE",
    "WPD_CONTACT_ROLE",
    "WPD_CONTACT_SPOUSE",
    "WPD_CONTACT_SUFFIX",
    "WPD_CONTENT_TYPE_ALL",
    "WPD_CONTENT_TYPE_APPOINTMENT",
    "WPD_CONTENT_TYPE_AUDIO",
    "WPD_CONTENT_TYPE_AUDIO_ALBUM",
    "WPD_CONTENT_TYPE_CALENDAR",
    "WPD_CONTENT_TYPE_CERTIFICATE",
    "WPD_CONTENT_TYPE_CONTACT",
    "WPD_CONTENT_TYPE_CONTACT_GROUP",
    "WPD_CONTENT_TYPE_DOCUMENT",
    "WPD_CONTENT_TYPE_EMAIL",
    "WPD_CONTENT_TYPE_FOLDER",
    "WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT",
    "WPD_CONTENT_TYPE_GENERIC_FILE",
    "WPD_CONTENT_TYPE_GENERIC_MESSAGE",
    "WPD_CONTENT_TYPE_IMAGE",
    "WPD_CONTENT_TYPE_IMAGE_ALBUM",
    "WPD_CONTENT_TYPE_MEDIA_CAST",
    "WPD_CONTENT_TYPE_MEMO",
    "WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM",
    "WPD_CONTENT_TYPE_NETWORK_ASSOCIATION",
    "WPD_CONTENT_TYPE_PLAYLIST",
    "WPD_CONTENT_TYPE_PROGRAM",
    "WPD_CONTENT_TYPE_SECTION",
    "WPD_CONTENT_TYPE_TASK",
    "WPD_CONTENT_TYPE_TELEVISION",
    "WPD_CONTENT_TYPE_UNSPECIFIED",
    "WPD_CONTENT_TYPE_VIDEO",
    "WPD_CONTENT_TYPE_VIDEO_ALBUM",
    "WPD_CONTENT_TYPE_WIRELESS_PROFILE",
    "WPD_CONTROL_FUNCTION_GENERIC_MESSAGE",
    "WPD_CROPPED_STATUS_CROPPED",
    "WPD_CROPPED_STATUS_NOT_CROPPED",
    "WPD_CROPPED_STATUS_SHOULD_NOT_BE_CROPPED",
    "WPD_CROPPED_STATUS_VALUES",
    "WPD_DEVICE_DATETIME",
    "WPD_DEVICE_EDP_IDENTITY",
    "WPD_DEVICE_FIRMWARE_VERSION",
    "WPD_DEVICE_FRIENDLY_NAME",
    "WPD_DEVICE_FUNCTIONAL_UNIQUE_ID",
    "WPD_DEVICE_MANUFACTURER",
    "WPD_DEVICE_MODEL",
    "WPD_DEVICE_MODEL_UNIQUE_ID",
    "WPD_DEVICE_NETWORK_IDENTIFIER",
    "WPD_DEVICE_OBJECT_ID",
    "WPD_DEVICE_POWER_LEVEL",
    "WPD_DEVICE_POWER_SOURCE",
    "WPD_DEVICE_PROPERTIES_V1",
    "WPD_DEVICE_PROPERTIES_V2",
    "WPD_DEVICE_PROPERTIES_V3",
    "WPD_DEVICE_PROTOCOL",
    "WPD_DEVICE_SERIAL_NUMBER",
    "WPD_DEVICE_SUPPORTED_DRM_SCHEMES",
    "WPD_DEVICE_SUPPORTED_FORMATS_ARE_ORDERED",
    "WPD_DEVICE_SUPPORTS_NON_CONSUMABLE",
    "WPD_DEVICE_SYNC_PARTNER",
    "WPD_DEVICE_TRANSPORT",
    "WPD_DEVICE_TRANSPORTS",
    "WPD_DEVICE_TRANSPORT_BLUETOOTH",
    "WPD_DEVICE_TRANSPORT_IP",
    "WPD_DEVICE_TRANSPORT_UNSPECIFIED",
    "WPD_DEVICE_TRANSPORT_USB",
    "WPD_DEVICE_TYPE",
    "WPD_DEVICE_TYPES",
    "WPD_DEVICE_TYPE_AUDIO_RECORDER",
    "WPD_DEVICE_TYPE_CAMERA",
    "WPD_DEVICE_TYPE_GENERIC",
    "WPD_DEVICE_TYPE_MEDIA_PLAYER",
    "WPD_DEVICE_TYPE_PERSONAL_INFORMATION_MANAGER",
    "WPD_DEVICE_TYPE_PHONE",
    "WPD_DEVICE_TYPE_VIDEO",
    "WPD_DEVICE_USE_DEVICE_STAGE",
    "WPD_DOCUMENT_OBJECT_PROPERTIES_V1",
    "WPD_EFFECT_MODES",
    "WPD_EFFECT_MODE_BLACK_AND_WHITE",
    "WPD_EFFECT_MODE_COLOR",
    "WPD_EFFECT_MODE_SEPIA",
    "WPD_EFFECT_MODE_UNDEFINED",
    "WPD_EMAIL_BCC_LINE",
    "WPD_EMAIL_CC_LINE",
    "WPD_EMAIL_HAS_ATTACHMENTS",
    "WPD_EMAIL_HAS_BEEN_READ",
    "WPD_EMAIL_OBJECT_PROPERTIES_V1",
    "WPD_EMAIL_RECEIVED_TIME",
    "WPD_EMAIL_SENDER_ADDRESS",
    "WPD_EMAIL_TO_LINE",
    "WPD_EVENT_ATTRIBUTES_V1",
    "WPD_EVENT_ATTRIBUTE_NAME",
    "WPD_EVENT_ATTRIBUTE_OPTIONS",
    "WPD_EVENT_ATTRIBUTE_PARAMETERS",
    "WPD_EVENT_DEVICE_CAPABILITIES_UPDATED",
    "WPD_EVENT_DEVICE_REMOVED",
    "WPD_EVENT_DEVICE_RESET",
    "WPD_EVENT_MTP_VENDOR_EXTENDED_EVENTS",
    "WPD_EVENT_NOTIFICATION",
    "WPD_EVENT_OBJECT_ADDED",
    "WPD_EVENT_OBJECT_REMOVED",
    "WPD_EVENT_OBJECT_TRANSFER_REQUESTED",
    "WPD_EVENT_OBJECT_UPDATED",
    "WPD_EVENT_OPTIONS_V1",
    "WPD_EVENT_OPTION_IS_AUTOPLAY_EVENT",
    "WPD_EVENT_OPTION_IS_BROADCAST_EVENT",
    "WPD_EVENT_PARAMETER_CHILD_HIERARCHY_CHANGED",
    "WPD_EVENT_PARAMETER_EVENT_ID",
    "WPD_EVENT_PARAMETER_OBJECT_CREATION_COOKIE",
    "WPD_EVENT_PARAMETER_OBJECT_PARENT_PERSISTENT_UNIQUE_ID",
    "WPD_EVENT_PARAMETER_OPERATION_PROGRESS",
    "WPD_EVENT_PARAMETER_OPERATION_STATE",
    "WPD_EVENT_PARAMETER_PNP_DEVICE_ID",
    "WPD_EVENT_PARAMETER_SERVICE_METHOD_CONTEXT",
    "WPD_EVENT_PROPERTIES_V1",
    "WPD_EVENT_PROPERTIES_V2",
    "WPD_EVENT_SERVICE_METHOD_COMPLETE",
    "WPD_EVENT_STORAGE_FORMAT",
    "WPD_EXPOSURE_METERING_MODES",
    "WPD_EXPOSURE_METERING_MODE_AVERAGE",
    "WPD_EXPOSURE_METERING_MODE_CENTER_SPOT",
    "WPD_EXPOSURE_METERING_MODE_CENTER_WEIGHTED_AVERAGE",
    "WPD_EXPOSURE_METERING_MODE_MULTI_SPOT",
    "WPD_EXPOSURE_METERING_MODE_UNDEFINED",
    "WPD_EXPOSURE_PROGRAM_MODES",
    "WPD_EXPOSURE_PROGRAM_MODE_ACTION",
    "WPD_EXPOSURE_PROGRAM_MODE_APERTURE_PRIORITY",
    "WPD_EXPOSURE_PROGRAM_MODE_AUTO",
    "WPD_EXPOSURE_PROGRAM_MODE_CREATIVE",
    "WPD_EXPOSURE_PROGRAM_MODE_MANUAL",
    "WPD_EXPOSURE_PROGRAM_MODE_PORTRAIT",
    "WPD_EXPOSURE_PROGRAM_MODE_SHUTTER_PRIORITY",
    "WPD_EXPOSURE_PROGRAM_MODE_UNDEFINED",
    "WPD_FLASH_MODES",
    "WPD_FLASH_MODE_AUTO",
    "WPD_FLASH_MODE_EXTERNAL_SYNC",
    "WPD_FLASH_MODE_FILL",
    "WPD_FLASH_MODE_OFF",
    "WPD_FLASH_MODE_RED_EYE_AUTO",
    "WPD_FLASH_MODE_RED_EYE_FILL",
    "WPD_FLASH_MODE_UNDEFINED",
    "WPD_FOCUS_AUTOMATIC",
    "WPD_FOCUS_AUTOMATIC_MACRO",
    "WPD_FOCUS_MANUAL",
    "WPD_FOCUS_METERING_MODES",
    "WPD_FOCUS_METERING_MODE_CENTER_SPOT",
    "WPD_FOCUS_METERING_MODE_MULTI_SPOT",
    "WPD_FOCUS_METERING_MODE_UNDEFINED",
    "WPD_FOCUS_MODES",
    "WPD_FOCUS_UNDEFINED",
    "WPD_FOLDER_CONTENT_TYPES_ALLOWED",
    "WPD_FOLDER_OBJECT_PROPERTIES_V1",
    "WPD_FORMAT_ATTRIBUTES_V1",
    "WPD_FORMAT_ATTRIBUTE_MIMETYPE",
    "WPD_FORMAT_ATTRIBUTE_NAME",
    "WPD_FUNCTIONAL_CATEGORY_ALL",
    "WPD_FUNCTIONAL_CATEGORY_AUDIO_CAPTURE",
    "WPD_FUNCTIONAL_CATEGORY_DEVICE",
    "WPD_FUNCTIONAL_CATEGORY_NETWORK_CONFIGURATION",
    "WPD_FUNCTIONAL_CATEGORY_RENDERING_INFORMATION",
    "WPD_FUNCTIONAL_CATEGORY_SMS",
    "WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE",
    "WPD_FUNCTIONAL_CATEGORY_STORAGE",
    "WPD_FUNCTIONAL_CATEGORY_VIDEO_CAPTURE",
    "WPD_FUNCTIONAL_OBJECT_CATEGORY",
    "WPD_FUNCTIONAL_OBJECT_PROPERTIES_V1",
    "WPD_IMAGE_BITDEPTH",
    "WPD_IMAGE_COLOR_CORRECTED_STATUS",
    "WPD_IMAGE_CROPPED_STATUS",
    "WPD_IMAGE_EXPOSURE_INDEX",
    "WPD_IMAGE_EXPOSURE_TIME",
    "WPD_IMAGE_FNUMBER",
    "WPD_IMAGE_HORIZONTAL_RESOLUTION",
    "WPD_IMAGE_OBJECT_PROPERTIES_V1",
    "WPD_IMAGE_VERTICAL_RESOLUTION",
    "WPD_MEDIA_ALBUM_ARTIST",
    "WPD_MEDIA_ARTIST",
    "WPD_MEDIA_AUDIO_ENCODING_PROFILE",
    "WPD_MEDIA_BITRATE_TYPE",
    "WPD_MEDIA_BUY_NOW",
    "WPD_MEDIA_BYTE_BOOKMARK",
    "WPD_MEDIA_COMPOSER",
    "WPD_MEDIA_COPYRIGHT",
    "WPD_MEDIA_DESCRIPTION",
    "WPD_MEDIA_DESTINATION_URL",
    "WPD_MEDIA_DURATION",
    "WPD_MEDIA_EFFECTIVE_RATING",
    "WPD_MEDIA_ENCODING_PROFILE",
    "WPD_MEDIA_GENRE",
    "WPD_MEDIA_GUID",
    "WPD_MEDIA_HEIGHT",
    "WPD_MEDIA_LAST_ACCESSED_TIME",
    "WPD_MEDIA_LAST_BUILD_DATE",
    "WPD_MEDIA_MANAGING_EDITOR",
    "WPD_MEDIA_META_GENRE",
    "WPD_MEDIA_OBJECT_BOOKMARK",
    "WPD_MEDIA_OWNER",
    "WPD_MEDIA_PARENTAL_RATING",
    "WPD_MEDIA_PROPERTIES_V1",
    "WPD_MEDIA_RELEASE_DATE",
    "WPD_MEDIA_SAMPLE_RATE",
    "WPD_MEDIA_SKIP_COUNT",
    "WPD_MEDIA_SOURCE_URL",
    "WPD_MEDIA_STAR_RATING",
    "WPD_MEDIA_SUBSCRIPTION_CONTENT_ID",
    "WPD_MEDIA_SUB_DESCRIPTION",
    "WPD_MEDIA_SUB_TITLE",
    "WPD_MEDIA_TIME_BOOKMARK",
    "WPD_MEDIA_TIME_TO_LIVE",
    "WPD_MEDIA_TITLE",
    "WPD_MEDIA_TOTAL_BITRATE",
    "WPD_MEDIA_USER_EFFECTIVE_RATING",
    "WPD_MEDIA_USE_COUNT",
    "WPD_MEDIA_WEBMASTER",
    "WPD_MEDIA_WIDTH",
    "WPD_MEMO_OBJECT_PROPERTIES_V1",
    "WPD_META_GENRES",
    "WPD_META_GENRE_AUDIO_PODCAST",
    "WPD_META_GENRE_FEATURE_FILM_VIDEO_FILE",
    "WPD_META_GENRE_GENERIC_MUSIC_AUDIO_FILE",
    "WPD_META_GENRE_GENERIC_NON_AUDIO_NON_VIDEO",
    "WPD_META_GENRE_GENERIC_NON_MUSIC_AUDIO_FILE",
    "WPD_META_GENRE_GENERIC_VIDEO_FILE",
    "WPD_META_GENRE_HOME_VIDEO_FILE",
    "WPD_META_GENRE_MIXED_PODCAST",
    "WPD_META_GENRE_MUSIC_VIDEO_FILE",
    "WPD_META_GENRE_NEWS_VIDEO_FILE",
    "WPD_META_GENRE_PHOTO_MONTAGE_VIDEO_FILE",
    "WPD_META_GENRE_SPOKEN_WORD_AUDIO_BOOK_FILES",
    "WPD_META_GENRE_SPOKEN_WORD_FILES_NON_AUDIO_BOOK",
    "WPD_META_GENRE_SPOKEN_WORD_NEWS",
    "WPD_META_GENRE_SPOKEN_WORD_TALK_SHOWS",
    "WPD_META_GENRE_TELEVISION_VIDEO_FILE",
    "WPD_META_GENRE_TRAINING_EDUCATIONAL_VIDEO_FILE",
    "WPD_META_GENRE_UNUSED",
    "WPD_META_GENRE_VIDEO_PODCAST",
    "WPD_METHOD_ATTRIBUTES_V1",
    "WPD_METHOD_ATTRIBUTE_ACCESS",
    "WPD_METHOD_ATTRIBUTE_ASSOCIATED_FORMAT",
    "WPD_METHOD_ATTRIBUTE_NAME",
    "WPD_METHOD_ATTRIBUTE_PARAMETERS",
    "WPD_MUSIC_ALBUM",
    "WPD_MUSIC_LYRICS",
    "WPD_MUSIC_MOOD",
    "WPD_MUSIC_OBJECT_PROPERTIES_V1",
    "WPD_MUSIC_TRACK",
    "WPD_NETWORK_ASSOCIATION_HOST_NETWORK_IDENTIFIERS",
    "WPD_NETWORK_ASSOCIATION_PROPERTIES_V1",
    "WPD_NETWORK_ASSOCIATION_X509V3SEQUENCE",
    "WPD_OBJECT_BACK_REFERENCES",
    "WPD_OBJECT_CAN_DELETE",
    "WPD_OBJECT_CONTAINER_FUNCTIONAL_OBJECT_ID",
    "WPD_OBJECT_CONTENT_TYPE",
    "WPD_OBJECT_DATE_AUTHORED",
    "WPD_OBJECT_DATE_CREATED",
    "WPD_OBJECT_DATE_MODIFIED",
    "WPD_OBJECT_FORMAT",
    "WPD_OBJECT_FORMAT_3G2",
    "WPD_OBJECT_FORMAT_3G2A",
    "WPD_OBJECT_FORMAT_3GP",
    "WPD_OBJECT_FORMAT_3GPA",
    "WPD_OBJECT_FORMAT_AAC",
    "WPD_OBJECT_FORMAT_ABSTRACT_CONTACT",
    "WPD_OBJECT_FORMAT_ABSTRACT_CONTACT_GROUP",
    "WPD_OBJECT_FORMAT_ABSTRACT_MEDIA_CAST",
    "WPD_OBJECT_FORMAT_AIFF",
    "WPD_OBJECT_FORMAT_ALL",
    "WPD_OBJECT_FORMAT_AMR",
    "WPD_OBJECT_FORMAT_ASF",
    "WPD_OBJECT_FORMAT_ASXPLAYLIST",
    "WPD_OBJECT_FORMAT_ATSCTS",
    "WPD_OBJECT_FORMAT_AUDIBLE",
    "WPD_OBJECT_FORMAT_AVCHD",
    "WPD_OBJECT_FORMAT_AVI",
    "WPD_OBJECT_FORMAT_BMP",
    "WPD_OBJECT_FORMAT_CIFF",
    "WPD_OBJECT_FORMAT_DPOF",
    "WPD_OBJECT_FORMAT_DVBTS",
    "WPD_OBJECT_FORMAT_EXECUTABLE",
    "WPD_OBJECT_FORMAT_EXIF",
    "WPD_OBJECT_FORMAT_FLAC",
    "WPD_OBJECT_FORMAT_FLASHPIX",
    "WPD_OBJECT_FORMAT_GIF",
    "WPD_OBJECT_FORMAT_HTML",
    "WPD_OBJECT_FORMAT_ICALENDAR",
    "WPD_OBJECT_FORMAT_ICON",
    "WPD_OBJECT_FORMAT_JFIF",
    "WPD_OBJECT_FORMAT_JP2",
    "WPD_OBJECT_FORMAT_JPEGXR",
    "WPD_OBJECT_FORMAT_JPX",
    "WPD_OBJECT_FORMAT_M3UPLAYLIST",
    "WPD_OBJECT_FORMAT_M4A",
    "WPD_OBJECT_FORMAT_MHT_COMPILED_HTML",
    "WPD_OBJECT_FORMAT_MICROSOFT_EXCEL",
    "WPD_OBJECT_FORMAT_MICROSOFT_POWERPOINT",
    "WPD_OBJECT_FORMAT_MICROSOFT_WFC",
    "WPD_OBJECT_FORMAT_MICROSOFT_WORD",
    "WPD_OBJECT_FORMAT_MKV",
    "WPD_OBJECT_FORMAT_MP2",
    "WPD_OBJECT_FORMAT_MP3",
    "WPD_OBJECT_FORMAT_MP4",
    "WPD_OBJECT_FORMAT_MPEG",
    "WPD_OBJECT_FORMAT_MPLPLAYLIST",
    "WPD_OBJECT_FORMAT_NETWORK_ASSOCIATION",
    "WPD_OBJECT_FORMAT_OGG",
    "WPD_OBJECT_FORMAT_PCD",
    "WPD_OBJECT_FORMAT_PICT",
    "WPD_OBJECT_FORMAT_PLSPLAYLIST",
    "WPD_OBJECT_FORMAT_PNG",
    "WPD_OBJECT_FORMAT_PROPERTIES_ONLY",
    "WPD_OBJECT_FORMAT_QCELP",
    "WPD_OBJECT_FORMAT_SCRIPT",
    "WPD_OBJECT_FORMAT_TEXT",
    "WPD_OBJECT_FORMAT_TIFF",
    "WPD_OBJECT_FORMAT_TIFFEP",
    "WPD_OBJECT_FORMAT_TIFFIT",
    "WPD_OBJECT_FORMAT_UNSPECIFIED",
    "WPD_OBJECT_FORMAT_VCALENDAR1",
    "WPD_OBJECT_FORMAT_VCARD2",
    "WPD_OBJECT_FORMAT_VCARD3",
    "WPD_OBJECT_FORMAT_WAVE",
    "WPD_OBJECT_FORMAT_WBMP",
    "WPD_OBJECT_FORMAT_WINDOWSIMAGEFORMAT",
    "WPD_OBJECT_FORMAT_WMA",
    "WPD_OBJECT_FORMAT_WMV",
    "WPD_OBJECT_FORMAT_WPLPLAYLIST",
    "WPD_OBJECT_FORMAT_X509V3CERTIFICATE",
    "WPD_OBJECT_FORMAT_XML",
    "WPD_OBJECT_GENERATE_THUMBNAIL_FROM_RESOURCE",
    "WPD_OBJECT_HINT_LOCATION_DISPLAY_NAME",
    "WPD_OBJECT_ID",
    "WPD_OBJECT_ISHIDDEN",
    "WPD_OBJECT_ISSYSTEM",
    "WPD_OBJECT_IS_DRM_PROTECTED",
    "WPD_OBJECT_KEYWORDS",
    "WPD_OBJECT_LANGUAGE_LOCALE",
    "WPD_OBJECT_NAME",
    "WPD_OBJECT_NON_CONSUMABLE",
    "WPD_OBJECT_ORIGINAL_FILE_NAME",
    "WPD_OBJECT_PARENT_ID",
    "WPD_OBJECT_PERSISTENT_UNIQUE_ID",
    "WPD_OBJECT_PROPERTIES_V1",
    "WPD_OBJECT_PROPERTIES_V2",
    "WPD_OBJECT_REFERENCES",
    "WPD_OBJECT_SIZE",
    "WPD_OBJECT_SUPPORTED_UNITS",
    "WPD_OBJECT_SYNC_ID",
    "WPD_OPERATION_STATES",
    "WPD_OPERATION_STATE_ABORTED",
    "WPD_OPERATION_STATE_CANCELLED",
    "WPD_OPERATION_STATE_FINISHED",
    "WPD_OPERATION_STATE_PAUSED",
    "WPD_OPERATION_STATE_RUNNING",
    "WPD_OPERATION_STATE_STARTED",
    "WPD_OPERATION_STATE_UNSPECIFIED",
    "WPD_OPTION_OBJECT_MANAGEMENT_RECURSIVE_DELETE_SUPPORTED",
    "WPD_OPTION_OBJECT_RESOURCES_NO_INPUT_BUFFER_ON_READ",
    "WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_READ_SUPPORTED",
    "WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_WRITE_SUPPORTED",
    "WPD_OPTION_SMS_BINARY_MESSAGE_SUPPORTED",
    "WPD_OPTION_VALID_OBJECT_IDS",
    "WPD_PARAMETER_ATTRIBUTES_V1",
    "WPD_PARAMETER_ATTRIBUTE_DEFAULT_VALUE",
    "WPD_PARAMETER_ATTRIBUTE_ENUMERATION_ELEMENTS",
    "WPD_PARAMETER_ATTRIBUTE_FORM",
    "WPD_PARAMETER_ATTRIBUTE_FORM_ENUMERATION",
    "WPD_PARAMETER_ATTRIBUTE_FORM_OBJECT_IDENTIFIER",
    "WPD_PARAMETER_ATTRIBUTE_FORM_RANGE",
    "WPD_PARAMETER_ATTRIBUTE_FORM_REGULAR_EXPRESSION",
    "WPD_PARAMETER_ATTRIBUTE_FORM_UNSPECIFIED",
    "WPD_PARAMETER_ATTRIBUTE_MAX_SIZE",
    "WPD_PARAMETER_ATTRIBUTE_NAME",
    "WPD_PARAMETER_ATTRIBUTE_ORDER",
    "WPD_PARAMETER_ATTRIBUTE_RANGE_MAX",
    "WPD_PARAMETER_ATTRIBUTE_RANGE_MIN",
    "WPD_PARAMETER_ATTRIBUTE_RANGE_STEP",
    "WPD_PARAMETER_ATTRIBUTE_REGULAR_EXPRESSION",
    "WPD_PARAMETER_ATTRIBUTE_USAGE",
    "WPD_PARAMETER_ATTRIBUTE_VARTYPE",
    "WPD_PARAMETER_USAGE_IN",
    "WPD_PARAMETER_USAGE_INOUT",
    "WPD_PARAMETER_USAGE_OUT",
    "WPD_PARAMETER_USAGE_RETURN",
    "WPD_PARAMETER_USAGE_TYPES",
    "WPD_POWER_SOURCES",
    "WPD_POWER_SOURCE_BATTERY",
    "WPD_POWER_SOURCE_EXTERNAL",
    "WPD_PROPERTIES_MTP_VENDOR_EXTENDED_DEVICE_PROPS",
    "WPD_PROPERTIES_MTP_VENDOR_EXTENDED_OBJECT_PROPS",
    "WPD_PROPERTY_ATTRIBUTES_V1",
    "WPD_PROPERTY_ATTRIBUTES_V2",
    "WPD_PROPERTY_ATTRIBUTE_CAN_DELETE",
    "WPD_PROPERTY_ATTRIBUTE_CAN_READ",
    "WPD_PROPERTY_ATTRIBUTE_CAN_WRITE",
    "WPD_PROPERTY_ATTRIBUTE_DEFAULT_VALUE",
    "WPD_PROPERTY_ATTRIBUTE_ENUMERATION_ELEMENTS",
    "WPD_PROPERTY_ATTRIBUTE_FAST_PROPERTY",
    "WPD_PROPERTY_ATTRIBUTE_FORM",
    "WPD_PROPERTY_ATTRIBUTE_FORM_ENUMERATION",
    "WPD_PROPERTY_ATTRIBUTE_FORM_OBJECT_IDENTIFIER",
    "WPD_PROPERTY_ATTRIBUTE_FORM_RANGE",
    "WPD_PROPERTY_ATTRIBUTE_FORM_REGULAR_EXPRESSION",
    "WPD_PROPERTY_ATTRIBUTE_FORM_UNSPECIFIED",
    "WPD_PROPERTY_ATTRIBUTE_MAX_SIZE",
    "WPD_PROPERTY_ATTRIBUTE_NAME",
    "WPD_PROPERTY_ATTRIBUTE_RANGE_MAX",
    "WPD_PROPERTY_ATTRIBUTE_RANGE_MIN",
    "WPD_PROPERTY_ATTRIBUTE_RANGE_STEP",
    "WPD_PROPERTY_ATTRIBUTE_REGULAR_EXPRESSION",
    "WPD_PROPERTY_ATTRIBUTE_VARTYPE",
    "WPD_PROPERTY_CAPABILITIES_COMMAND",
    "WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS",
    "WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE",
    "WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES",
    "WPD_PROPERTY_CAPABILITIES_EVENT",
    "WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS",
    "WPD_PROPERTY_CAPABILITIES_FORMAT",
    "WPD_PROPERTY_CAPABILITIES_FORMATS",
    "WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES",
    "WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY",
    "WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS",
    "WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES",
    "WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS",
    "WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS",
    "WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS",
    "WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_VALUES",
    "WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_WRITE_RESULTS",
    "WPD_PROPERTY_CLASS_EXTENSION_SERVICE_INTERFACES",
    "WPD_PROPERTY_CLASS_EXTENSION_SERVICE_OBJECT_ID",
    "WPD_PROPERTY_CLASS_EXTENSION_SERVICE_REGISTRATION_RESULTS",
    "WPD_PROPERTY_COMMON_ACTIVITY_ID",
    "WPD_PROPERTY_COMMON_CLIENT_INFORMATION",
    "WPD_PROPERTY_COMMON_CLIENT_INFORMATION_CONTEXT",
    "WPD_PROPERTY_COMMON_COMMAND_CATEGORY",
    "WPD_PROPERTY_COMMON_COMMAND_ID",
    "WPD_PROPERTY_COMMON_COMMAND_TARGET",
    "WPD_PROPERTY_COMMON_DRIVER_ERROR_CODE",
    "WPD_PROPERTY_COMMON_HRESULT",
    "WPD_PROPERTY_COMMON_OBJECT_IDS",
    "WPD_PROPERTY_COMMON_PERSISTENT_UNIQUE_IDS",
    "WPD_PROPERTY_DEVICE_HINTS_CONTENT_LOCATIONS",
    "WPD_PROPERTY_DEVICE_HINTS_CONTENT_TYPE",
    "WPD_PROPERTY_MTP_EXT_EVENT_PARAMS",
    "WPD_PROPERTY_MTP_EXT_OPERATION_CODE",
    "WPD_PROPERTY_MTP_EXT_OPERATION_PARAMS",
    "WPD_PROPERTY_MTP_EXT_OPTIMAL_TRANSFER_BUFFER_SIZE",
    "WPD_PROPERTY_MTP_EXT_RESPONSE_CODE",
    "WPD_PROPERTY_MTP_EXT_RESPONSE_PARAMS",
    "WPD_PROPERTY_MTP_EXT_TRANSFER_CONTEXT",
    "WPD_PROPERTY_MTP_EXT_TRANSFER_DATA",
    "WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_READ",
    "WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_TO_READ",
    "WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_TO_WRITE",
    "WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_WRITTEN",
    "WPD_PROPERTY_MTP_EXT_TRANSFER_TOTAL_DATA_SIZE",
    "WPD_PROPERTY_MTP_EXT_VENDOR_EXTENSION_DESCRIPTION",
    "WPD_PROPERTY_MTP_EXT_VENDOR_OPERATION_CODES",
    "WPD_PROPERTY_NULL",
    "WPD_PROPERTY_OBJECT_ENUMERATION_CONTEXT",
    "WPD_PROPERTY_OBJECT_ENUMERATION_FILTER",
    "WPD_PROPERTY_OBJECT_ENUMERATION_NUM_OBJECTS_REQUESTED",
    "WPD_PROPERTY_OBJECT_ENUMERATION_OBJECT_IDS",
    "WPD_PROPERTY_OBJECT_ENUMERATION_PARENT_ID",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_COPY_RESULTS",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_CREATION_PROPERTIES",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_DATA",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_OPTIONS",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_RESULTS",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_DESTINATION_FOLDER_OBJECT_ID",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_MOVE_RESULTS",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_TO_WRITE",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_WRITTEN",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_FORMAT",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_ID",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_IDS",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_OPTIMAL_TRANSFER_BUFFER_SIZE",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_PROPERTY_KEYS",
    "WPD_PROPERTY_OBJECT_MANAGEMENT_UPDATE_PROPERTIES",
    "WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT",
    "WPD_PROPERTY_OBJECT_PROPERTIES_BULK_DEPTH",
    "WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_FORMAT",
    "WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_IDS",
    "WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PARENT_OBJECT_ID",
    "WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PROPERTY_KEYS",
    "WPD_PROPERTY_OBJECT_PROPERTIES_BULK_VALUES",
    "WPD_PROPERTY_OBJECT_PROPERTIES_BULK_WRITE_RESULTS",
    "WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID",
    "WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES",
    "WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_DELETE_RESULTS",
    "WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS",
    "WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES",
    "WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS",
    "WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE",
    "WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT",
    "WPD_PROPERTY_OBJECT_RESOURCES_DATA",
    "WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_READ",
    "WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_READ",
    "WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_WRITE",
    "WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_WRITTEN",
    "WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID",
    "WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE",
    "WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START",
    "WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_ATTRIBUTES",
    "WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS",
    "WPD_PROPERTY_OBJECT_RESOURCES_SEEK_OFFSET",
    "WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG",
    "WPD_PROPERTY_OBJECT_RESOURCES_STREAM_UNITS",
    "WPD_PROPERTY_OBJECT_RESOURCES_SUPPORTS_UNITS",
    "WPD_PROPERTY_PUBLIC_KEY",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND_OPTIONS",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT_ATTRIBUTES",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_FORMATS",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT_ATTRIBUTES",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITANCE_TYPE",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITED_SERVICES",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD_ATTRIBUTES",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER_ATTRIBUTES",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_ATTRIBUTES",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_KEYS",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_RENDERING_PROFILES",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_COMMANDS",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_EVENTS",
    "WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_METHODS",
    "WPD_PROPERTY_SERVICE_METHOD",
    "WPD_PROPERTY_SERVICE_METHOD_CONTEXT",
    "WPD_PROPERTY_SERVICE_METHOD_HRESULT",
    "WPD_PROPERTY_SERVICE_METHOD_PARAMETER_VALUES",
    "WPD_PROPERTY_SERVICE_METHOD_RESULT_VALUES",
    "WPD_PROPERTY_SERVICE_OBJECT_ID",
    "WPD_PROPERTY_SMS_BINARY_MESSAGE",
    "WPD_PROPERTY_SMS_MESSAGE_TYPE",
    "WPD_PROPERTY_SMS_RECIPIENT",
    "WPD_PROPERTY_SMS_TEXT_MESSAGE",
    "WPD_PROPERTY_STORAGE_DESTINATION_OBJECT_ID",
    "WPD_PROPERTY_STORAGE_OBJECT_ID",
    "WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1",
    "WPD_RENDERING_INFORMATION_PROFILES",
    "WPD_RENDERING_INFORMATION_PROFILE_ENTRY_CREATABLE_RESOURCES",
    "WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE",
    "WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES",
    "WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_OBJECT",
    "WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_RESOURCE",
    "WPD_RESOURCE_ALBUM_ART",
    "WPD_RESOURCE_ATTRIBUTES_V1",
    "WPD_RESOURCE_ATTRIBUTE_CAN_DELETE",
    "WPD_RESOURCE_ATTRIBUTE_CAN_READ",
    "WPD_RESOURCE_ATTRIBUTE_CAN_WRITE",
    "WPD_RESOURCE_ATTRIBUTE_FORMAT",
    "WPD_RESOURCE_ATTRIBUTE_OPTIMAL_READ_BUFFER_SIZE",
    "WPD_RESOURCE_ATTRIBUTE_OPTIMAL_WRITE_BUFFER_SIZE",
    "WPD_RESOURCE_ATTRIBUTE_RESOURCE_KEY",
    "WPD_RESOURCE_ATTRIBUTE_TOTAL_SIZE",
    "WPD_RESOURCE_AUDIO_CLIP",
    "WPD_RESOURCE_BRANDING_ART",
    "WPD_RESOURCE_CONTACT_PHOTO",
    "WPD_RESOURCE_DEFAULT",
    "WPD_RESOURCE_GENERIC",
    "WPD_RESOURCE_ICON",
    "WPD_RESOURCE_THUMBNAIL",
    "WPD_RESOURCE_VIDEO_CLIP",
    "WPD_SECTION_DATA_LENGTH",
    "WPD_SECTION_DATA_OFFSET",
    "WPD_SECTION_DATA_REFERENCED_OBJECT_RESOURCE",
    "WPD_SECTION_DATA_UNITS",
    "WPD_SECTION_DATA_UNITS_BYTES",
    "WPD_SECTION_DATA_UNITS_MILLISECONDS",
    "WPD_SECTION_DATA_UNITS_VALUES",
    "WPD_SECTION_OBJECT_PROPERTIES_V1",
    "WPD_SERVICE_INHERITANCE_IMPLEMENTATION",
    "WPD_SERVICE_INHERITANCE_TYPES",
    "WPD_SERVICE_PROPERTIES_V1",
    "WPD_SERVICE_VERSION",
    "WPD_SMS_ENCODING",
    "WPD_SMS_ENCODING_TYPES",
    "WPD_SMS_MAX_PAYLOAD",
    "WPD_SMS_OBJECT_PROPERTIES_V1",
    "WPD_SMS_PROVIDER",
    "WPD_SMS_TIMEOUT",
    "WPD_STILL_IMAGE_ARTIST",
    "WPD_STILL_IMAGE_BURST_INTERVAL",
    "WPD_STILL_IMAGE_BURST_NUMBER",
    "WPD_STILL_IMAGE_CAMERA_MANUFACTURER",
    "WPD_STILL_IMAGE_CAMERA_MODEL",
    "WPD_STILL_IMAGE_CAPTURE_DELAY",
    "WPD_STILL_IMAGE_CAPTURE_FORMAT",
    "WPD_STILL_IMAGE_CAPTURE_MODE",
    "WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1",
    "WPD_STILL_IMAGE_CAPTURE_RESOLUTION",
    "WPD_STILL_IMAGE_COMPRESSION_SETTING",
    "WPD_STILL_IMAGE_CONTRAST",
    "WPD_STILL_IMAGE_DIGITAL_ZOOM",
    "WPD_STILL_IMAGE_EFFECT_MODE",
    "WPD_STILL_IMAGE_EXPOSURE_BIAS_COMPENSATION",
    "WPD_STILL_IMAGE_EXPOSURE_INDEX",
    "WPD_STILL_IMAGE_EXPOSURE_METERING_MODE",
    "WPD_STILL_IMAGE_EXPOSURE_PROGRAM_MODE",
    "WPD_STILL_IMAGE_EXPOSURE_TIME",
    "WPD_STILL_IMAGE_FLASH_MODE",
    "WPD_STILL_IMAGE_FNUMBER",
    "WPD_STILL_IMAGE_FOCAL_LENGTH",
    "WPD_STILL_IMAGE_FOCUS_DISTANCE",
    "WPD_STILL_IMAGE_FOCUS_METERING_MODE",
    "WPD_STILL_IMAGE_FOCUS_MODE",
    "WPD_STILL_IMAGE_RGB_GAIN",
    "WPD_STILL_IMAGE_SHARPNESS",
    "WPD_STILL_IMAGE_TIMELAPSE_INTERVAL",
    "WPD_STILL_IMAGE_TIMELAPSE_NUMBER",
    "WPD_STILL_IMAGE_UPLOAD_URL",
    "WPD_STILL_IMAGE_WHITE_BALANCE",
    "WPD_STORAGE_ACCESS_CAPABILITY",
    "WPD_STORAGE_ACCESS_CAPABILITY_READWRITE",
    "WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITHOUT_OBJECT_DELETION",
    "WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITH_OBJECT_DELETION",
    "WPD_STORAGE_ACCESS_CAPABILITY_VALUES",
    "WPD_STORAGE_CAPACITY",
    "WPD_STORAGE_CAPACITY_IN_OBJECTS",
    "WPD_STORAGE_DESCRIPTION",
    "WPD_STORAGE_FILE_SYSTEM_TYPE",
    "WPD_STORAGE_FREE_SPACE_IN_BYTES",
    "WPD_STORAGE_FREE_SPACE_IN_OBJECTS",
    "WPD_STORAGE_MAX_OBJECT_SIZE",
    "WPD_STORAGE_OBJECT_PROPERTIES_V1",
    "WPD_STORAGE_SERIAL_NUMBER",
    "WPD_STORAGE_TYPE",
    "WPD_STORAGE_TYPE_FIXED_RAM",
    "WPD_STORAGE_TYPE_FIXED_ROM",
    "WPD_STORAGE_TYPE_REMOVABLE_RAM",
    "WPD_STORAGE_TYPE_REMOVABLE_ROM",
    "WPD_STORAGE_TYPE_UNDEFINED",
    "WPD_STORAGE_TYPE_VALUES",
    "WPD_STREAM_UNITS",
    "WPD_STREAM_UNITS_BYTES",
    "WPD_STREAM_UNITS_FRAMES",
    "WPD_STREAM_UNITS_MICROSECONDS",
    "WPD_STREAM_UNITS_MILLISECONDS",
    "WPD_STREAM_UNITS_ROWS",
    "WPD_TASK_OBJECT_PROPERTIES_V1",
    "WPD_TASK_OWNER",
    "WPD_TASK_PERCENT_COMPLETE",
    "WPD_TASK_REMINDER_DATE",
    "WPD_TASK_STATUS",
    "WPD_VIDEO_AUTHOR",
    "WPD_VIDEO_BITRATE",
    "WPD_VIDEO_BUFFER_SIZE",
    "WPD_VIDEO_CREDITS",
    "WPD_VIDEO_FOURCC_CODE",
    "WPD_VIDEO_FRAMERATE",
    "WPD_VIDEO_KEY_FRAME_DISTANCE",
    "WPD_VIDEO_OBJECT_PROPERTIES_V1",
    "WPD_VIDEO_QUALITY_SETTING",
    "WPD_VIDEO_RECORDEDTV_CHANNEL_NUMBER",
    "WPD_VIDEO_RECORDEDTV_REPEAT",
    "WPD_VIDEO_RECORDEDTV_STATION_NAME",
    "WPD_VIDEO_SCAN_TYPE",
    "WPD_VIDEO_SCAN_TYPES",
    "WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_LOWER_FIRST",
    "WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_UPPER_FIRST",
    "WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_LOWER_FIRST",
    "WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_UPPER_FIRST",
    "WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE",
    "WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE_AND_PROGRESSIVE",
    "WPD_VIDEO_SCAN_TYPE_PROGRESSIVE",
    "WPD_VIDEO_SCAN_TYPE_UNUSED",
    "WPD_WHITE_BALANCE_AUTOMATIC",
    "WPD_WHITE_BALANCE_DAYLIGHT",
    "WPD_WHITE_BALANCE_FLASH",
    "WPD_WHITE_BALANCE_FLORESCENT",
    "WPD_WHITE_BALANCE_MANUAL",
    "WPD_WHITE_BALANCE_ONE_PUSH_AUTOMATIC",
    "WPD_WHITE_BALANCE_SETTINGS",
    "WPD_WHITE_BALANCE_TUNGSTEN",
    "WPD_WHITE_BALANCE_UNDEFINED",
    "WpdAttributeForm",
    "WpdParameterAttributeForm",
    "WpdSerializer",
]
