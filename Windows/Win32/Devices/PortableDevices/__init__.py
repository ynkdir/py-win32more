from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Devices.PortableDevices
import Windows.Win32.Devices.Properties
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def DEVPKEY_MTPBTH_IsConnected():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('ea1237fa-589d-4472-84-e4-0a-be-36-fd-62-ef'), pid=2)
GUID_DEVINTERFACE_WPD: Guid = Guid('6ac27878-a6fa-4155-ba-85-f9-8f-49-1d-4f-33')
GUID_DEVINTERFACE_WPD_PRIVATE: Guid = Guid('ba0c718f-4ded-49b7-bd-d3-fa-be-28-66-12-11')
GUID_DEVINTERFACE_WPD_SERVICE: Guid = Guid('9ef44f80-3d64-4246-a6-aa-20-6f-32-8d-1e-dc')
WPD_CONTROL_FUNCTION_GENERIC_MESSAGE: UInt32 = 66
IOCTL_WPD_MESSAGE_READWRITE_ACCESS: UInt32 = 4243720
IOCTL_WPD_MESSAGE_READ_ACCESS: UInt32 = 4210952
WPD_DEVICE_OBJECT_ID: String = 'DEVICE'
PORTABLE_DEVICE_TYPE: String = 'PortableDeviceType'
PORTABLE_DEVICE_ICON: String = 'Icons'
PORTABLE_DEVICE_NAMESPACE_TIMEOUT: String = 'PortableDeviceNameSpaceTimeout'
PORTABLE_DEVICE_NAMESPACE_EXCLUDE_FROM_SHELL: String = 'PortableDeviceNameSpaceExcludeFromShell'
PORTABLE_DEVICE_NAMESPACE_THUMBNAIL_CONTENT_TYPES: String = 'PortableDeviceNameSpaceThumbnailContentTypes'
PORTABLE_DEVICE_IS_MASS_STORAGE: String = 'PortableDeviceIsMassStorage'
PORTABLE_DEVICE_DRM_SCHEME_WMDRM10_PD: String = 'WMDRM10-PD'
PORTABLE_DEVICE_DRM_SCHEME_PDDRM: String = 'PDDRM'
FACILITY_WPD: UInt32 = 42
E_WPD_DEVICE_ALREADY_OPENED: Windows.Win32.Foundation.HRESULT = -2144731135
E_WPD_DEVICE_NOT_OPEN: Windows.Win32.Foundation.HRESULT = -2144731134
E_WPD_OBJECT_ALREADY_ATTACHED_TO_DEVICE: Windows.Win32.Foundation.HRESULT = -2144731133
E_WPD_OBJECT_NOT_ATTACHED_TO_DEVICE: Windows.Win32.Foundation.HRESULT = -2144731132
E_WPD_OBJECT_NOT_COMMITED: Windows.Win32.Foundation.HRESULT = -2144731131
E_WPD_DEVICE_IS_HUNG: Windows.Win32.Foundation.HRESULT = -2144731130
E_WPD_SMS_INVALID_RECIPIENT: Windows.Win32.Foundation.HRESULT = -2144731036
E_WPD_SMS_INVALID_MESSAGE_BODY: Windows.Win32.Foundation.HRESULT = -2144731035
E_WPD_SMS_SERVICE_UNAVAILABLE: Windows.Win32.Foundation.HRESULT = -2144731034
E_WPD_SERVICE_ALREADY_OPENED: Windows.Win32.Foundation.HRESULT = -2144730936
E_WPD_SERVICE_NOT_OPEN: Windows.Win32.Foundation.HRESULT = -2144730935
E_WPD_OBJECT_ALREADY_ATTACHED_TO_SERVICE: Windows.Win32.Foundation.HRESULT = -2144730934
E_WPD_OBJECT_NOT_ATTACHED_TO_SERVICE: Windows.Win32.Foundation.HRESULT = -2144730933
E_WPD_SERVICE_BAD_PARAMETER_ORDER: Windows.Win32.Foundation.HRESULT = -2144730932
WPD_EVENT_NOTIFICATION: Guid = Guid('2ba2e40a-6b4c-4295-bb-43-26-32-2b-99-ae-b2')
WPD_EVENT_OBJECT_ADDED: Guid = Guid('a726da95-e207-4b02-8d-44-be-f2-e8-6c-bf-fc')
WPD_EVENT_OBJECT_REMOVED: Guid = Guid('be82ab88-a52c-4823-96-e5-d0-27-26-71-fc-38')
WPD_EVENT_OBJECT_UPDATED: Guid = Guid('1445a759-2e01-485d-9f-27-ff-07-da-e6-97-ab')
WPD_EVENT_DEVICE_RESET: Guid = Guid('7755cf53-c1ed-44f3-b5-a2-45-1e-2c-37-6b-27')
WPD_EVENT_DEVICE_CAPABILITIES_UPDATED: Guid = Guid('36885aa1-cd54-4daa-b3-d0-af-b3-e0-3f-59-99')
WPD_EVENT_STORAGE_FORMAT: Guid = Guid('3782616b-22bc-4474-a2-51-30-70-f8-d3-88-57')
WPD_EVENT_OBJECT_TRANSFER_REQUESTED: Guid = Guid('8d16a0a1-f2c6-41da-8f-19-5e-53-72-1a-db-f2')
WPD_EVENT_DEVICE_REMOVED: Guid = Guid('e4cbca1b-6918-48b9-85-ee-02-be-7c-85-0a-f9')
WPD_EVENT_SERVICE_METHOD_COMPLETE: Guid = Guid('8a33f5f8-0acc-4d9b-9c-c4-11-2d-35-3b-86-ca')
WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT: Guid = Guid('99ed0160-17ff-4c44-9d-98-1d-7a-6f-94-19-21')
WPD_CONTENT_TYPE_FOLDER: Guid = Guid('27e2e392-a111-48e0-ab-0c-e1-77-05-a0-5f-85')
WPD_CONTENT_TYPE_IMAGE: Guid = Guid('ef2107d5-a52a-4243-a2-6b-62-d4-17-6d-76-03')
WPD_CONTENT_TYPE_DOCUMENT: Guid = Guid('680adf52-950a-4041-9b-41-65-e3-93-64-81-55')
WPD_CONTENT_TYPE_CONTACT: Guid = Guid('eaba8313-4525-4707-9f-0e-87-c6-80-8e-94-35')
WPD_CONTENT_TYPE_CONTACT_GROUP: Guid = Guid('346b8932-4c36-40d8-94-15-18-28-29-1f-9d-e9')
WPD_CONTENT_TYPE_AUDIO: Guid = Guid('4ad2c85e-5e2d-45e5-88-64-4f-22-9e-3c-6c-f0')
WPD_CONTENT_TYPE_VIDEO: Guid = Guid('9261b03c-3d78-4519-85-e3-02-c5-e1-f5-0b-b9')
WPD_CONTENT_TYPE_TELEVISION: Guid = Guid('60a169cf-f2ae-4e21-93-75-96-77-f1-1c-1c-6e')
WPD_CONTENT_TYPE_PLAYLIST: Guid = Guid('1a33f7e4-af13-48f5-99-4e-77-36-9d-fe-04-a3')
WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM: Guid = Guid('00f0c3ac-a593-49ac-92-19-24-ab-ca-5a-25-63')
WPD_CONTENT_TYPE_AUDIO_ALBUM: Guid = Guid('aa18737e-5009-48fa-ae-21-85-f2-43-83-b4-e6')
WPD_CONTENT_TYPE_IMAGE_ALBUM: Guid = Guid('75793148-15f5-4a30-a8-13-54-ed-8a-37-e2-26')
WPD_CONTENT_TYPE_VIDEO_ALBUM: Guid = Guid('012b0db7-d4c1-45d6-b0-81-94-b8-77-79-61-4f')
WPD_CONTENT_TYPE_MEMO: Guid = Guid('9cd20ecf-3b50-414f-a6-41-e4-73-ff-e4-57-51')
WPD_CONTENT_TYPE_EMAIL: Guid = Guid('8038044a-7e51-4f8f-88-3d-1d-06-23-d1-45-33')
WPD_CONTENT_TYPE_APPOINTMENT: Guid = Guid('0fed060e-8793-4b1e-90-c9-48-ac-38-9a-c6-31')
WPD_CONTENT_TYPE_TASK: Guid = Guid('63252f2c-887f-4cb6-b1-ac-d2-98-55-dc-ef-6c')
WPD_CONTENT_TYPE_PROGRAM: Guid = Guid('d269f96a-247c-4bff-98-fb-97-f3-c4-92-20-e6')
WPD_CONTENT_TYPE_GENERIC_FILE: Guid = Guid('0085e0a6-8d34-45d7-bc-5c-44-7e-59-c7-3d-48')
WPD_CONTENT_TYPE_CALENDAR: Guid = Guid('a1fd5967-6023-49a0-9d-f1-f8-06-0b-e7-51-b0')
WPD_CONTENT_TYPE_GENERIC_MESSAGE: Guid = Guid('e80eaaf8-b2db-4133-b6-7e-1b-ef-4b-4a-6e-5f')
WPD_CONTENT_TYPE_NETWORK_ASSOCIATION: Guid = Guid('031da7ee-18c8-4205-84-7e-89-a1-12-61-d0-f3')
WPD_CONTENT_TYPE_CERTIFICATE: Guid = Guid('dc3876e8-a948-4060-90-50-cb-d7-7e-8a-3d-87')
WPD_CONTENT_TYPE_WIRELESS_PROFILE: Guid = Guid('0bac070a-9f5f-4da4-a8-f6-3d-e4-4d-68-fd-6c')
WPD_CONTENT_TYPE_MEDIA_CAST: Guid = Guid('5e88b3cc-3e65-4e62-bf-ff-22-94-95-25-3a-b0')
WPD_CONTENT_TYPE_SECTION: Guid = Guid('821089f5-1d91-4dc9-be-3c-bb-b1-b3-5b-18-ce')
WPD_CONTENT_TYPE_UNSPECIFIED: Guid = Guid('28d8d31e-249c-454e-aa-bc-34-88-31-68-e6-34')
WPD_CONTENT_TYPE_ALL: Guid = Guid('80e170d2-1055-4a3e-b9-52-82-cc-4f-8a-86-89')
WPD_FUNCTIONAL_CATEGORY_DEVICE: Guid = Guid('08ea466b-e3a4-4336-a1-f3-a4-4d-2b-5c-43-8c')
WPD_FUNCTIONAL_CATEGORY_STORAGE: Guid = Guid('23f05bbc-15de-4c2a-a5-5b-a9-af-5c-e4-12-ef')
WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE: Guid = Guid('613ca327-ab93-4900-b4-fa-89-5b-b5-87-4b-79')
WPD_FUNCTIONAL_CATEGORY_AUDIO_CAPTURE: Guid = Guid('3f2a1919-c7c2-4a00-85-5d-f5-7c-f0-6d-eb-bb')
WPD_FUNCTIONAL_CATEGORY_VIDEO_CAPTURE: Guid = Guid('e23e5f6b-7243-43aa-8d-f1-0e-b3-d9-68-a9-18')
WPD_FUNCTIONAL_CATEGORY_SMS: Guid = Guid('0044a0b1-c1e9-4afd-b3-58-a6-2c-61-17-c9-cf')
WPD_FUNCTIONAL_CATEGORY_RENDERING_INFORMATION: Guid = Guid('08600ba4-a7ba-4a01-ab-0e-00-65-d0-a3-56-d3')
WPD_FUNCTIONAL_CATEGORY_NETWORK_CONFIGURATION: Guid = Guid('48f4db72-7c6a-4ab0-9e-1a-47-0e-3c-db-f2-6a')
WPD_FUNCTIONAL_CATEGORY_ALL: Guid = Guid('2d8a6512-a74c-448e-ba-8a-f4-ac-07-c4-93-99')
WPD_OBJECT_FORMAT_ICON: Guid = Guid('077232ed-102c-4638-9c-22-83-f1-42-bf-c8-22')
WPD_OBJECT_FORMAT_M4A: Guid = Guid('30aba7ac-6ffd-4c23-a3-59-3e-9b-52-f3-f1-c8')
WPD_OBJECT_FORMAT_NETWORK_ASSOCIATION: Guid = Guid('b1020000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_X509V3CERTIFICATE: Guid = Guid('b1030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_MICROSOFT_WFC: Guid = Guid('b1040000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_3GPA: Guid = Guid('e5172730-f971-41ef-a1-0b-22-71-a0-01-9d-7a')
WPD_OBJECT_FORMAT_3G2A: Guid = Guid('1a11202d-8759-4e34-ba-5e-b1-21-10-87-ee-e4')
WPD_OBJECT_FORMAT_ALL: Guid = Guid('c1f62eb2-4bb3-479c-9c-fa-05-b5-f3-a5-7b-22')
WPD_CATEGORY_NULL: Guid = Guid('00000000-0000-0000-00-00-00-00-00-00-00-00')
def WPD_PROPERTY_NULL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00000000-0000-0000-00-00-00-00-00-00-00-00'), pid=0)
WPD_OBJECT_PROPERTIES_V1: Guid = Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c')
def WPD_OBJECT_CONTENT_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=7)
def WPD_OBJECT_REFERENCES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=14)
def WPD_OBJECT_CONTAINER_FUNCTIONAL_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=23)
def WPD_OBJECT_GENERATE_THUMBNAIL_FROM_RESOURCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=24)
def WPD_OBJECT_HINT_LOCATION_DISPLAY_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=25)
WPD_OBJECT_PROPERTIES_V2: Guid = Guid('0373cd3d-4a46-40d7-b4-d8-73-e8-da-74-e7-75')
def WPD_OBJECT_SUPPORTED_UNITS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0373cd3d-4a46-40d7-b4-d8-73-e8-da-74-e7-75'), pid=2)
WPD_FUNCTIONAL_OBJECT_PROPERTIES_V1: Guid = Guid('8f052d93-abca-4fc5-a5-ac-b0-1d-f4-db-e5-98')
def WPD_FUNCTIONAL_OBJECT_CATEGORY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8f052d93-abca-4fc5-a5-ac-b0-1d-f4-db-e5-98'), pid=2)
WPD_STORAGE_OBJECT_PROPERTIES_V1: Guid = Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a')
def WPD_STORAGE_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=2)
def WPD_STORAGE_FILE_SYSTEM_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=3)
def WPD_STORAGE_CAPACITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=4)
def WPD_STORAGE_FREE_SPACE_IN_BYTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=5)
def WPD_STORAGE_FREE_SPACE_IN_OBJECTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=6)
def WPD_STORAGE_DESCRIPTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=7)
def WPD_STORAGE_SERIAL_NUMBER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=8)
def WPD_STORAGE_MAX_OBJECT_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=9)
def WPD_STORAGE_CAPACITY_IN_OBJECTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=10)
def WPD_STORAGE_ACCESS_CAPABILITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('01a3057a-74d6-4e80-be-a7-dc-4c-21-2c-e5-0a'), pid=11)
WPD_NETWORK_ASSOCIATION_PROPERTIES_V1: Guid = Guid('e4c93c1f-b203-43f1-a1-00-5a-07-d1-1b-02-74')
def WPD_NETWORK_ASSOCIATION_HOST_NETWORK_IDENTIFIERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4c93c1f-b203-43f1-a1-00-5a-07-d1-1b-02-74'), pid=2)
def WPD_NETWORK_ASSOCIATION_X509V3SEQUENCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4c93c1f-b203-43f1-a1-00-5a-07-d1-1b-02-74'), pid=3)
WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1: Guid = Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60')
def WPD_STILL_IMAGE_CAPTURE_RESOLUTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=2)
def WPD_STILL_IMAGE_CAPTURE_FORMAT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=3)
def WPD_STILL_IMAGE_COMPRESSION_SETTING():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=4)
def WPD_STILL_IMAGE_WHITE_BALANCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=5)
def WPD_STILL_IMAGE_RGB_GAIN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=6)
def WPD_STILL_IMAGE_FNUMBER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=7)
def WPD_STILL_IMAGE_FOCAL_LENGTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=8)
def WPD_STILL_IMAGE_FOCUS_DISTANCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=9)
def WPD_STILL_IMAGE_FOCUS_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=10)
def WPD_STILL_IMAGE_EXPOSURE_METERING_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=11)
def WPD_STILL_IMAGE_FLASH_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=12)
def WPD_STILL_IMAGE_EXPOSURE_TIME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=13)
def WPD_STILL_IMAGE_EXPOSURE_PROGRAM_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=14)
def WPD_STILL_IMAGE_EXPOSURE_INDEX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=15)
def WPD_STILL_IMAGE_EXPOSURE_BIAS_COMPENSATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=16)
def WPD_STILL_IMAGE_CAPTURE_DELAY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=17)
def WPD_STILL_IMAGE_CAPTURE_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=18)
def WPD_STILL_IMAGE_CONTRAST():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=19)
def WPD_STILL_IMAGE_SHARPNESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=20)
def WPD_STILL_IMAGE_DIGITAL_ZOOM():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=21)
def WPD_STILL_IMAGE_EFFECT_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=22)
def WPD_STILL_IMAGE_BURST_NUMBER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=23)
def WPD_STILL_IMAGE_BURST_INTERVAL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=24)
def WPD_STILL_IMAGE_TIMELAPSE_NUMBER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=25)
def WPD_STILL_IMAGE_TIMELAPSE_INTERVAL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=26)
def WPD_STILL_IMAGE_FOCUS_METERING_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=27)
def WPD_STILL_IMAGE_UPLOAD_URL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=28)
def WPD_STILL_IMAGE_ARTIST():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=29)
def WPD_STILL_IMAGE_CAMERA_MODEL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=30)
def WPD_STILL_IMAGE_CAMERA_MANUFACTURER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('58c571ec-1bcb-42a7-8a-c5-bb-29-15-73-a2-60'), pid=31)
WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1: Guid = Guid('c53d039f-ee23-4a31-85-90-76-39-87-98-70-b4')
def WPD_RENDERING_INFORMATION_PROFILES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c53d039f-ee23-4a31-85-90-76-39-87-98-70-b4'), pid=2)
def WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c53d039f-ee23-4a31-85-90-76-39-87-98-70-b4'), pid=3)
def WPD_RENDERING_INFORMATION_PROFILE_ENTRY_CREATABLE_RESOURCES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c53d039f-ee23-4a31-85-90-76-39-87-98-70-b4'), pid=4)
WPD_CLIENT_INFORMATION_PROPERTIES_V1: Guid = Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59')
def WPD_CLIENT_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=2)
def WPD_CLIENT_MAJOR_VERSION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=3)
def WPD_CLIENT_MINOR_VERSION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=4)
def WPD_CLIENT_REVISION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=5)
def WPD_CLIENT_WMDRM_APPLICATION_PRIVATE_KEY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=6)
def WPD_CLIENT_WMDRM_APPLICATION_CERTIFICATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=7)
def WPD_CLIENT_SECURITY_QUALITY_OF_SERVICE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=8)
def WPD_CLIENT_DESIRED_ACCESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=9)
def WPD_CLIENT_SHARE_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=10)
def WPD_CLIENT_EVENT_COOKIE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=11)
def WPD_CLIENT_MINIMUM_RESULTS_BUFFER_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=12)
def WPD_CLIENT_MANUAL_CLOSE_ON_DISCONNECT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('204d9f0c-2292-4080-9f-42-40-66-4e-70-f8-59'), pid=13)
WPD_PROPERTY_ATTRIBUTES_V1: Guid = Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37')
def WPD_PROPERTY_ATTRIBUTE_FORM():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=2)
def WPD_PROPERTY_ATTRIBUTE_CAN_READ():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=3)
def WPD_PROPERTY_ATTRIBUTE_CAN_WRITE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=4)
def WPD_PROPERTY_ATTRIBUTE_CAN_DELETE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=5)
def WPD_PROPERTY_ATTRIBUTE_DEFAULT_VALUE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=6)
def WPD_PROPERTY_ATTRIBUTE_FAST_PROPERTY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=7)
def WPD_PROPERTY_ATTRIBUTE_RANGE_MIN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=8)
def WPD_PROPERTY_ATTRIBUTE_RANGE_MAX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=9)
def WPD_PROPERTY_ATTRIBUTE_RANGE_STEP():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=10)
def WPD_PROPERTY_ATTRIBUTE_ENUMERATION_ELEMENTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=11)
def WPD_PROPERTY_ATTRIBUTE_REGULAR_EXPRESSION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=12)
def WPD_PROPERTY_ATTRIBUTE_MAX_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ab7943d8-6332-445f-a0-0d-8d-5e-f1-e9-6f-37'), pid=13)
WPD_PROPERTY_ATTRIBUTES_V2: Guid = Guid('5d9da160-74ae-43cc-85-a9-fe-55-5a-80-79-8e')
def WPD_PROPERTY_ATTRIBUTE_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5d9da160-74ae-43cc-85-a9-fe-55-5a-80-79-8e'), pid=2)
def WPD_PROPERTY_ATTRIBUTE_VARTYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5d9da160-74ae-43cc-85-a9-fe-55-5a-80-79-8e'), pid=3)
WPD_CLASS_EXTENSION_OPTIONS_V1: Guid = Guid('6309ffef-a87c-4ca7-84-34-79-75-76-e4-0a-96')
def WPD_CLASS_EXTENSION_OPTIONS_SUPPORTED_CONTENT_TYPES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6309ffef-a87c-4ca7-84-34-79-75-76-e4-0a-96'), pid=2)
def WPD_CLASS_EXTENSION_OPTIONS_DONT_REGISTER_WPD_DEVICE_INTERFACE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6309ffef-a87c-4ca7-84-34-79-75-76-e4-0a-96'), pid=3)
def WPD_CLASS_EXTENSION_OPTIONS_REGISTER_WPD_PRIVATE_DEVICE_INTERFACE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6309ffef-a87c-4ca7-84-34-79-75-76-e4-0a-96'), pid=4)
WPD_CLASS_EXTENSION_OPTIONS_V2: Guid = Guid('3e3595da-4d71-49fe-a0-b4-d4-40-6c-3a-e9-3f')
def WPD_CLASS_EXTENSION_OPTIONS_MULTITRANSPORT_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3e3595da-4d71-49fe-a0-b4-d4-40-6c-3a-e9-3f'), pid=2)
def WPD_CLASS_EXTENSION_OPTIONS_DEVICE_IDENTIFICATION_VALUES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3e3595da-4d71-49fe-a0-b4-d4-40-6c-3a-e9-3f'), pid=3)
def WPD_CLASS_EXTENSION_OPTIONS_TRANSPORT_BANDWIDTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3e3595da-4d71-49fe-a0-b4-d4-40-6c-3a-e9-3f'), pid=4)
WPD_CLASS_EXTENSION_OPTIONS_V3: Guid = Guid('65c160f8-1367-4ce2-93-9d-83-10-83-9f-0d-30')
def WPD_CLASS_EXTENSION_OPTIONS_SILENCE_AUTOPLAY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('65c160f8-1367-4ce2-93-9d-83-10-83-9f-0d-30'), pid=2)
WPD_RESOURCE_ATTRIBUTES_V1: Guid = Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6')
def WPD_RESOURCE_ATTRIBUTE_TOTAL_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=2)
def WPD_RESOURCE_ATTRIBUTE_CAN_READ():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=3)
def WPD_RESOURCE_ATTRIBUTE_CAN_WRITE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=4)
def WPD_RESOURCE_ATTRIBUTE_CAN_DELETE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=5)
def WPD_RESOURCE_ATTRIBUTE_OPTIMAL_READ_BUFFER_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=6)
def WPD_RESOURCE_ATTRIBUTE_OPTIMAL_WRITE_BUFFER_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=7)
def WPD_RESOURCE_ATTRIBUTE_FORMAT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=8)
def WPD_RESOURCE_ATTRIBUTE_RESOURCE_KEY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1eb6f604-9278-429f-93-cc-5b-b8-c0-66-56-b6'), pid=9)
WPD_DEVICE_PROPERTIES_V1: Guid = Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc')
def WPD_DEVICE_SYNC_PARTNER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=2)
def WPD_DEVICE_FIRMWARE_VERSION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=3)
def WPD_DEVICE_POWER_LEVEL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=4)
def WPD_DEVICE_POWER_SOURCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=5)
def WPD_DEVICE_PROTOCOL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=6)
def WPD_DEVICE_MANUFACTURER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=7)
def WPD_DEVICE_MODEL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=8)
def WPD_DEVICE_SERIAL_NUMBER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=9)
def WPD_DEVICE_SUPPORTS_NON_CONSUMABLE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=10)
def WPD_DEVICE_DATETIME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=11)
def WPD_DEVICE_FRIENDLY_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=12)
def WPD_DEVICE_SUPPORTED_DRM_SCHEMES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=13)
def WPD_DEVICE_SUPPORTED_FORMATS_ARE_ORDERED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=14)
def WPD_DEVICE_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=15)
def WPD_DEVICE_NETWORK_IDENTIFIER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('26d4979a-e643-4626-9e-2b-73-6d-c0-c9-2f-dc'), pid=16)
WPD_DEVICE_PROPERTIES_V2: Guid = Guid('463dd662-7fc4-4291-91-1c-7f-4c-9c-ca-97-99')
def WPD_DEVICE_FUNCTIONAL_UNIQUE_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('463dd662-7fc4-4291-91-1c-7f-4c-9c-ca-97-99'), pid=2)
def WPD_DEVICE_MODEL_UNIQUE_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('463dd662-7fc4-4291-91-1c-7f-4c-9c-ca-97-99'), pid=3)
def WPD_DEVICE_TRANSPORT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('463dd662-7fc4-4291-91-1c-7f-4c-9c-ca-97-99'), pid=4)
def WPD_DEVICE_USE_DEVICE_STAGE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('463dd662-7fc4-4291-91-1c-7f-4c-9c-ca-97-99'), pid=5)
WPD_DEVICE_PROPERTIES_V3: Guid = Guid('6c2b878c-c2ec-490d-b4-25-d7-a7-5e-23-e5-ed')
def WPD_DEVICE_EDP_IDENTITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('6c2b878c-c2ec-490d-b4-25-d7-a7-5e-23-e5-ed'), pid=1)
WPD_SERVICE_PROPERTIES_V1: Guid = Guid('7510698a-cb54-481c-b8-db-0d-75-c9-3f-1c-06')
def WPD_SERVICE_VERSION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7510698a-cb54-481c-b8-db-0d-75-c9-3f-1c-06'), pid=2)
WPD_EVENT_PROPERTIES_V1: Guid = Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0')
def WPD_EVENT_PARAMETER_PNP_DEVICE_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=2)
def WPD_EVENT_PARAMETER_EVENT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=3)
def WPD_EVENT_PARAMETER_OPERATION_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=4)
def WPD_EVENT_PARAMETER_OPERATION_PROGRESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=5)
def WPD_EVENT_PARAMETER_OBJECT_PARENT_PERSISTENT_UNIQUE_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=6)
def WPD_EVENT_PARAMETER_OBJECT_CREATION_COOKIE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=7)
def WPD_EVENT_PARAMETER_CHILD_HIERARCHY_CHANGED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('15ab1953-f817-4fef-a9-21-56-76-e8-38-f6-e0'), pid=8)
WPD_EVENT_PROPERTIES_V2: Guid = Guid('52807b8a-4914-4323-9b-9a-74-f6-54-b2-b8-46')
def WPD_EVENT_PARAMETER_SERVICE_METHOD_CONTEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('52807b8a-4914-4323-9b-9a-74-f6-54-b2-b8-46'), pid=2)
WPD_EVENT_OPTIONS_V1: Guid = Guid('b3d8dad7-a361-4b83-8a-48-5b-02-ce-10-71-3b')
def WPD_EVENT_OPTION_IS_BROADCAST_EVENT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3d8dad7-a361-4b83-8a-48-5b-02-ce-10-71-3b'), pid=2)
def WPD_EVENT_OPTION_IS_AUTOPLAY_EVENT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3d8dad7-a361-4b83-8a-48-5b-02-ce-10-71-3b'), pid=3)
WPD_EVENT_ATTRIBUTES_V1: Guid = Guid('10c96578-2e81-4111-ad-de-e0-8c-a6-13-8f-6d')
def WPD_EVENT_ATTRIBUTE_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10c96578-2e81-4111-ad-de-e0-8c-a6-13-8f-6d'), pid=2)
def WPD_EVENT_ATTRIBUTE_PARAMETERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10c96578-2e81-4111-ad-de-e0-8c-a6-13-8f-6d'), pid=3)
def WPD_EVENT_ATTRIBUTE_OPTIONS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10c96578-2e81-4111-ad-de-e0-8c-a6-13-8f-6d'), pid=4)
WPD_API_OPTIONS_V1: Guid = Guid('10e54a3e-052d-4777-a1-3c-de-76-14-be-2b-c4')
def WPD_API_OPTION_USE_CLEAR_DATA_STREAM():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10e54a3e-052d-4777-a1-3c-de-76-14-be-2b-c4'), pid=2)
def WPD_API_OPTION_IOCTL_ACCESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('10e54a3e-052d-4777-a1-3c-de-76-14-be-2b-c4'), pid=3)
WPD_FORMAT_ATTRIBUTES_V1: Guid = Guid('a0a02000-bcaf-4be8-b3-f5-23-3f-23-1c-f5-8f')
def WPD_FORMAT_ATTRIBUTE_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a0a02000-bcaf-4be8-b3-f5-23-3f-23-1c-f5-8f'), pid=2)
def WPD_FORMAT_ATTRIBUTE_MIMETYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a0a02000-bcaf-4be8-b3-f5-23-3f-23-1c-f5-8f'), pid=3)
WPD_METHOD_ATTRIBUTES_V1: Guid = Guid('f17a5071-f039-44af-8e-fe-43-2c-f3-2e-43-2a')
def WPD_METHOD_ATTRIBUTE_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f17a5071-f039-44af-8e-fe-43-2c-f3-2e-43-2a'), pid=2)
def WPD_METHOD_ATTRIBUTE_ASSOCIATED_FORMAT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f17a5071-f039-44af-8e-fe-43-2c-f3-2e-43-2a'), pid=3)
def WPD_METHOD_ATTRIBUTE_ACCESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f17a5071-f039-44af-8e-fe-43-2c-f3-2e-43-2a'), pid=4)
def WPD_METHOD_ATTRIBUTE_PARAMETERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f17a5071-f039-44af-8e-fe-43-2c-f3-2e-43-2a'), pid=5)
WPD_PARAMETER_ATTRIBUTES_V1: Guid = Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58')
def WPD_PARAMETER_ATTRIBUTE_ORDER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=2)
def WPD_PARAMETER_ATTRIBUTE_USAGE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=3)
def WPD_PARAMETER_ATTRIBUTE_FORM():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=4)
def WPD_PARAMETER_ATTRIBUTE_DEFAULT_VALUE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=5)
def WPD_PARAMETER_ATTRIBUTE_RANGE_MIN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=6)
def WPD_PARAMETER_ATTRIBUTE_RANGE_MAX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=7)
def WPD_PARAMETER_ATTRIBUTE_RANGE_STEP():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=8)
def WPD_PARAMETER_ATTRIBUTE_ENUMERATION_ELEMENTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=9)
def WPD_PARAMETER_ATTRIBUTE_REGULAR_EXPRESSION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=10)
def WPD_PARAMETER_ATTRIBUTE_MAX_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=11)
def WPD_PARAMETER_ATTRIBUTE_VARTYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=12)
def WPD_PARAMETER_ATTRIBUTE_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e6864dd7-f325-45ea-a1-d5-97-cf-73-b6-ca-58'), pid=13)
WPD_CATEGORY_COMMON: Guid = Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a')
def WPD_COMMAND_COMMON_RESET_DEVICE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=2)
def WPD_COMMAND_COMMON_GET_OBJECT_IDS_FROM_PERSISTENT_UNIQUE_IDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=3)
def WPD_COMMAND_COMMON_SAVE_CLIENT_INFORMATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=4)
def WPD_PROPERTY_COMMON_COMMAND_CATEGORY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1001)
def WPD_PROPERTY_COMMON_COMMAND_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1002)
def WPD_PROPERTY_COMMON_HRESULT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1003)
def WPD_PROPERTY_COMMON_DRIVER_ERROR_CODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1004)
def WPD_PROPERTY_COMMON_COMMAND_TARGET():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1006)
def WPD_PROPERTY_COMMON_PERSISTENT_UNIQUE_IDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1007)
def WPD_PROPERTY_COMMON_OBJECT_IDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1008)
def WPD_PROPERTY_COMMON_CLIENT_INFORMATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1009)
def WPD_PROPERTY_COMMON_CLIENT_INFORMATION_CONTEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1010)
def WPD_PROPERTY_COMMON_ACTIVITY_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=1011)
def WPD_OPTION_VALID_OBJECT_IDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f0422a9c-5dc8-4440-b5-bd-5d-f2-88-35-65-8a'), pid=5001)
WPD_CATEGORY_OBJECT_ENUMERATION: Guid = Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec')
def WPD_COMMAND_OBJECT_ENUMERATION_START_FIND():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=2)
def WPD_COMMAND_OBJECT_ENUMERATION_FIND_NEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=3)
def WPD_COMMAND_OBJECT_ENUMERATION_END_FIND():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=4)
def WPD_PROPERTY_OBJECT_ENUMERATION_PARENT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=1001)
def WPD_PROPERTY_OBJECT_ENUMERATION_FILTER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=1002)
def WPD_PROPERTY_OBJECT_ENUMERATION_OBJECT_IDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=1003)
def WPD_PROPERTY_OBJECT_ENUMERATION_CONTEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=1004)
def WPD_PROPERTY_OBJECT_ENUMERATION_NUM_OBJECTS_REQUESTED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b7474e91-e7f8-4ad9-b4-00-ad-1a-4b-58-ee-ec'), pid=1005)
WPD_CATEGORY_OBJECT_PROPERTIES: Guid = Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04')
def WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=2)
def WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=3)
def WPD_COMMAND_OBJECT_PROPERTIES_GET():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=4)
def WPD_COMMAND_OBJECT_PROPERTIES_SET():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=5)
def WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=6)
def WPD_COMMAND_OBJECT_PROPERTIES_DELETE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=7)
def WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1001)
def WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1002)
def WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1003)
def WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1004)
def WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1005)
def WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_DELETE_RESULTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('9e5582e4-0814-44e6-98-1a-b2-99-8d-58-38-04'), pid=1006)
WPD_CATEGORY_OBJECT_PROPERTIES_BULK: Guid = Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e')
def WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_START():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=2)
def WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_NEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=3)
def WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_END():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=4)
def WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_START():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=5)
def WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_NEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=6)
def WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_END():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=7)
def WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_START():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=8)
def WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_NEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=9)
def WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_END():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=10)
def WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_IDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1001)
def WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1002)
def WPD_PROPERTY_OBJECT_PROPERTIES_BULK_VALUES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1003)
def WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PROPERTY_KEYS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1004)
def WPD_PROPERTY_OBJECT_PROPERTIES_BULK_DEPTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1005)
def WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PARENT_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1006)
def WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_FORMAT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1007)
def WPD_PROPERTY_OBJECT_PROPERTIES_BULK_WRITE_RESULTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('11c824dd-04cd-4e4e-8c-7b-f6-ef-b7-94-d8-4e'), pid=1008)
WPD_CATEGORY_OBJECT_RESOURCES: Guid = Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a')
def WPD_COMMAND_OBJECT_RESOURCES_GET_SUPPORTED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=2)
def WPD_COMMAND_OBJECT_RESOURCES_GET_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=3)
def WPD_COMMAND_OBJECT_RESOURCES_OPEN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=4)
def WPD_COMMAND_OBJECT_RESOURCES_READ():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=5)
def WPD_COMMAND_OBJECT_RESOURCES_WRITE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=6)
def WPD_COMMAND_OBJECT_RESOURCES_CLOSE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=7)
def WPD_COMMAND_OBJECT_RESOURCES_DELETE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=8)
def WPD_COMMAND_OBJECT_RESOURCES_CREATE_RESOURCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=9)
def WPD_COMMAND_OBJECT_RESOURCES_REVERT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=10)
def WPD_COMMAND_OBJECT_RESOURCES_SEEK():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=11)
def WPD_COMMAND_OBJECT_RESOURCES_COMMIT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=12)
def WPD_COMMAND_OBJECT_RESOURCES_SEEK_IN_UNITS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=13)
def WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1001)
def WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1002)
def WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1003)
def WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1004)
def WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1005)
def WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_READ():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1006)
def WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_READ():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1007)
def WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_WRITE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1008)
def WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_WRITTEN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1009)
def WPD_PROPERTY_OBJECT_RESOURCES_DATA():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1010)
def WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1011)
def WPD_PROPERTY_OBJECT_RESOURCES_SEEK_OFFSET():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1012)
def WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1013)
def WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1014)
def WPD_PROPERTY_OBJECT_RESOURCES_SUPPORTS_UNITS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1015)
def WPD_PROPERTY_OBJECT_RESOURCES_STREAM_UNITS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=1016)
def WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_READ_SUPPORTED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=5001)
def WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_WRITE_SUPPORTED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=5002)
def WPD_OPTION_OBJECT_RESOURCES_NO_INPUT_BUFFER_ON_READ():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b3a2b22d-a595-4108-be-0a-fc-3c-96-5f-3d-4a'), pid=5003)
WPD_CATEGORY_OBJECT_MANAGEMENT: Guid = Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89')
def WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_ONLY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=2)
def WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_AND_DATA():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=3)
def WPD_COMMAND_OBJECT_MANAGEMENT_WRITE_OBJECT_DATA():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=4)
def WPD_COMMAND_OBJECT_MANAGEMENT_COMMIT_OBJECT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=5)
def WPD_COMMAND_OBJECT_MANAGEMENT_REVERT_OBJECT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=6)
def WPD_COMMAND_OBJECT_MANAGEMENT_DELETE_OBJECTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=7)
def WPD_COMMAND_OBJECT_MANAGEMENT_MOVE_OBJECTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=8)
def WPD_COMMAND_OBJECT_MANAGEMENT_COPY_OBJECTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=9)
def WPD_COMMAND_OBJECT_MANAGEMENT_UPDATE_OBJECT_WITH_PROPERTIES_AND_DATA():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=10)
def WPD_PROPERTY_OBJECT_MANAGEMENT_CREATION_PROPERTIES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1001)
def WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1002)
def WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_TO_WRITE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1003)
def WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_WRITTEN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1004)
def WPD_PROPERTY_OBJECT_MANAGEMENT_DATA():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1005)
def WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1006)
def WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_OPTIONS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1007)
def WPD_PROPERTY_OBJECT_MANAGEMENT_OPTIMAL_TRANSFER_BUFFER_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1008)
def WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_IDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1009)
def WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_RESULTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1010)
def WPD_PROPERTY_OBJECT_MANAGEMENT_DESTINATION_FOLDER_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1011)
def WPD_PROPERTY_OBJECT_MANAGEMENT_MOVE_RESULTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1012)
def WPD_PROPERTY_OBJECT_MANAGEMENT_COPY_RESULTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1013)
def WPD_PROPERTY_OBJECT_MANAGEMENT_UPDATE_PROPERTIES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1014)
def WPD_PROPERTY_OBJECT_MANAGEMENT_PROPERTY_KEYS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1015)
def WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_FORMAT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=1016)
def WPD_OPTION_OBJECT_MANAGEMENT_RECURSIVE_DELETE_SUPPORTED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef1e43dd-a9ed-4341-8b-cc-18-61-92-ae-a0-89'), pid=5001)
WPD_CATEGORY_CAPABILITIES: Guid = Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56')
def WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=2)
def WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=3)
def WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=4)
def WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=5)
def WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=6)
def WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=7)
def WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=8)
def WPD_COMMAND_CAPABILITIES_GET_FIXED_PROPERTY_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=9)
def WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=10)
def WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=11)
def WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1001)
def WPD_PROPERTY_CAPABILITIES_COMMAND():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1002)
def WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1003)
def WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1004)
def WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1005)
def WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1006)
def WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1007)
def WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1008)
def WPD_PROPERTY_CAPABILITIES_FORMATS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1009)
def WPD_PROPERTY_CAPABILITIES_FORMAT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1010)
def WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1011)
def WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1012)
def WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1013)
def WPD_PROPERTY_CAPABILITIES_EVENT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1014)
def WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0cabec78-6b74-41c6-92-16-26-39-d1-fc-e3-56'), pid=1015)
WPD_CATEGORY_STORAGE: Guid = Guid('d8f907a6-34cc-45fa-97-fb-d0-07-fa-47-ec-94')
def WPD_COMMAND_STORAGE_FORMAT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d8f907a6-34cc-45fa-97-fb-d0-07-fa-47-ec-94'), pid=2)
def WPD_COMMAND_STORAGE_EJECT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d8f907a6-34cc-45fa-97-fb-d0-07-fa-47-ec-94'), pid=4)
def WPD_PROPERTY_STORAGE_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d8f907a6-34cc-45fa-97-fb-d0-07-fa-47-ec-94'), pid=1001)
def WPD_PROPERTY_STORAGE_DESTINATION_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d8f907a6-34cc-45fa-97-fb-d0-07-fa-47-ec-94'), pid=1002)
WPD_CATEGORY_SMS: Guid = Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1')
def WPD_COMMAND_SMS_SEND():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=2)
def WPD_PROPERTY_SMS_RECIPIENT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=1001)
def WPD_PROPERTY_SMS_MESSAGE_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=1002)
def WPD_PROPERTY_SMS_TEXT_MESSAGE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=1003)
def WPD_PROPERTY_SMS_BINARY_MESSAGE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=1004)
def WPD_OPTION_SMS_BINARY_MESSAGE_SUPPORTED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afc25d66-fe0d-4114-90-97-97-0c-93-e9-20-d1'), pid=5001)
WPD_CATEGORY_STILL_IMAGE_CAPTURE: Guid = Guid('4fcd6982-22a2-4b05-a4-8b-62-d3-8b-f2-7b-32')
def WPD_COMMAND_STILL_IMAGE_CAPTURE_INITIATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4fcd6982-22a2-4b05-a4-8b-62-d3-8b-f2-7b-32'), pid=2)
WPD_CATEGORY_MEDIA_CAPTURE: Guid = Guid('59b433ba-fe44-4d8d-80-8c-6b-cb-9b-0f-15-e8')
def WPD_COMMAND_MEDIA_CAPTURE_START():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('59b433ba-fe44-4d8d-80-8c-6b-cb-9b-0f-15-e8'), pid=2)
def WPD_COMMAND_MEDIA_CAPTURE_STOP():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('59b433ba-fe44-4d8d-80-8c-6b-cb-9b-0f-15-e8'), pid=3)
def WPD_COMMAND_MEDIA_CAPTURE_PAUSE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('59b433ba-fe44-4d8d-80-8c-6b-cb-9b-0f-15-e8'), pid=4)
WPD_CATEGORY_DEVICE_HINTS: Guid = Guid('0d5fb92b-cb46-4c4f-83-43-0b-c3-d3-f1-7c-84')
def WPD_COMMAND_DEVICE_HINTS_GET_CONTENT_LOCATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0d5fb92b-cb46-4c4f-83-43-0b-c3-d3-f1-7c-84'), pid=2)
def WPD_PROPERTY_DEVICE_HINTS_CONTENT_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0d5fb92b-cb46-4c4f-83-43-0b-c3-d3-f1-7c-84'), pid=1001)
def WPD_PROPERTY_DEVICE_HINTS_CONTENT_LOCATIONS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('0d5fb92b-cb46-4c4f-83-43-0b-c3-d3-f1-7c-84'), pid=1002)
WPD_CLASS_EXTENSION_V1: Guid = Guid('33fb0d11-64a3-4fac-b4-c7-3d-fe-aa-99-b0-51')
def WPD_COMMAND_CLASS_EXTENSION_WRITE_DEVICE_INFORMATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('33fb0d11-64a3-4fac-b4-c7-3d-fe-aa-99-b0-51'), pid=2)
def WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_VALUES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('33fb0d11-64a3-4fac-b4-c7-3d-fe-aa-99-b0-51'), pid=1001)
def WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_WRITE_RESULTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('33fb0d11-64a3-4fac-b4-c7-3d-fe-aa-99-b0-51'), pid=1002)
WPD_CLASS_EXTENSION_V2: Guid = Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58')
def WPD_COMMAND_CLASS_EXTENSION_REGISTER_SERVICE_INTERFACES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58'), pid=2)
def WPD_COMMAND_CLASS_EXTENSION_UNREGISTER_SERVICE_INTERFACES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58'), pid=3)
def WPD_PROPERTY_CLASS_EXTENSION_SERVICE_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58'), pid=1001)
def WPD_PROPERTY_CLASS_EXTENSION_SERVICE_INTERFACES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58'), pid=1002)
def WPD_PROPERTY_CLASS_EXTENSION_SERVICE_REGISTRATION_RESULTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f0779b5-fa2b-4766-9c-b2-f7-3b-a3-0b-67-58'), pid=1003)
WPD_CATEGORY_NETWORK_CONFIGURATION: Guid = Guid('78f9c6fc-79b8-473c-90-60-6b-d2-3d-d0-72-c4')
def WPD_COMMAND_GENERATE_KEYPAIR():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78f9c6fc-79b8-473c-90-60-6b-d2-3d-d0-72-c4'), pid=2)
def WPD_COMMAND_COMMIT_KEYPAIR():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78f9c6fc-79b8-473c-90-60-6b-d2-3d-d0-72-c4'), pid=3)
def WPD_COMMAND_PROCESS_WIRELESS_PROFILE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78f9c6fc-79b8-473c-90-60-6b-d2-3d-d0-72-c4'), pid=4)
def WPD_PROPERTY_PUBLIC_KEY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78f9c6fc-79b8-473c-90-60-6b-d2-3d-d0-72-c4'), pid=1001)
WPD_CATEGORY_SERVICE_COMMON: Guid = Guid('322f071d-36ef-477f-b4-b5-6f-52-d7-34-ba-ee')
def WPD_COMMAND_SERVICE_COMMON_GET_SERVICE_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('322f071d-36ef-477f-b4-b5-6f-52-d7-34-ba-ee'), pid=2)
def WPD_PROPERTY_SERVICE_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('322f071d-36ef-477f-b4-b5-6f-52-d7-34-ba-ee'), pid=1001)
WPD_CATEGORY_SERVICE_CAPABILITIES: Guid = Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89')
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=2)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS_BY_FORMAT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=3)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=4)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_PARAMETER_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=5)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMATS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=6)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=7)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=8)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_PROPERTY_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=9)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_EVENTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=10)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=11)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_PARAMETER_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=12)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_INHERITED_SERVICES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=13)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_RENDERING_PROFILES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=14)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_COMMANDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=15)
def WPD_COMMAND_SERVICE_CAPABILITIES_GET_COMMAND_OPTIONS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=16)
def WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_METHODS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1001)
def WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1002)
def WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1003)
def WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1004)
def WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1005)
def WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1006)
def WPD_PROPERTY_SERVICE_CAPABILITIES_FORMATS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1007)
def WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1008)
def WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_KEYS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1009)
def WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1010)
def WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_EVENTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1011)
def WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1012)
def WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT_ATTRIBUTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1013)
def WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITANCE_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1014)
def WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITED_SERVICES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1015)
def WPD_PROPERTY_SERVICE_CAPABILITIES_RENDERING_PROFILES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1016)
def WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_COMMANDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1017)
def WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1018)
def WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND_OPTIONS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('24457e74-2e9f-44f9-8c-57-1d-1b-cb-17-0b-89'), pid=1019)
WPD_CATEGORY_SERVICE_METHODS: Guid = Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc')
def WPD_COMMAND_SERVICE_METHODS_START_INVOKE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=2)
def WPD_COMMAND_SERVICE_METHODS_CANCEL_INVOKE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=3)
def WPD_COMMAND_SERVICE_METHODS_END_INVOKE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=4)
def WPD_PROPERTY_SERVICE_METHOD():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=1001)
def WPD_PROPERTY_SERVICE_METHOD_PARAMETER_VALUES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=1002)
def WPD_PROPERTY_SERVICE_METHOD_RESULT_VALUES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=1003)
def WPD_PROPERTY_SERVICE_METHOD_CONTEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=1004)
def WPD_PROPERTY_SERVICE_METHOD_HRESULT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2d521ca8-c1b0-4268-a3-42-cf-19-32-15-69-bc'), pid=1005)
def WPD_RESOURCE_DEFAULT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e81e79be-34f0-41bf-b5-3f-f1-a0-6a-e8-78-42'), pid=0)
def WPD_RESOURCE_CONTACT_PHOTO():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2c4d6803-80ea-4580-af-9a-5b-e1-a2-3e-dd-cb'), pid=0)
def WPD_RESOURCE_THUMBNAIL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('c7c407ba-98fa-46b5-99-60-23-fe-c1-24-cf-de'), pid=0)
def WPD_RESOURCE_ICON():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f195fed8-aa28-4ee3-b1-53-e1-82-dd-5e-dc-39'), pid=0)
def WPD_RESOURCE_AUDIO_CLIP():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3bc13982-85b1-48e0-95-a6-8d-3a-d0-6b-e1-17'), pid=0)
def WPD_RESOURCE_ALBUM_ART():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f02aa354-2300-4e2d-a1-b9-3b-67-30-f7-fa-21'), pid=0)
def WPD_RESOURCE_GENERIC():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b9b9f515-ba70-4647-94-dc-fa-49-25-e9-5a-07'), pid=0)
def WPD_RESOURCE_VIDEO_CLIP():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b566ee42-6368-4290-86-62-70-18-2f-b7-9f-20'), pid=0)
def WPD_RESOURCE_BRANDING_ART():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b633b1ae-6caf-4a87-95-89-22-de-d6-dd-58-99'), pid=0)
WPD_OBJECT_FORMAT_PROPERTIES_ONLY: Guid = Guid('30010000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_UNSPECIFIED: Guid = Guid('30000000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_SCRIPT: Guid = Guid('30020000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_EXECUTABLE: Guid = Guid('30030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_TEXT: Guid = Guid('30040000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_HTML: Guid = Guid('30050000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_DPOF: Guid = Guid('30060000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_AIFF: Guid = Guid('30070000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_WAVE: Guid = Guid('30080000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_MP3: Guid = Guid('30090000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_AVI: Guid = Guid('300a0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_MPEG: Guid = Guid('300b0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_ASF: Guid = Guid('300c0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_EXIF: Guid = Guid('38010000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_TIFFEP: Guid = Guid('38020000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_FLASHPIX: Guid = Guid('38030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_BMP: Guid = Guid('38040000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_CIFF: Guid = Guid('38050000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_GIF: Guid = Guid('38070000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_JFIF: Guid = Guid('38080000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_PCD: Guid = Guid('38090000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_PICT: Guid = Guid('380a0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_PNG: Guid = Guid('380b0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_TIFF: Guid = Guid('380d0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_TIFFIT: Guid = Guid('380e0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_JP2: Guid = Guid('380f0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_JPX: Guid = Guid('38100000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_WBMP: Guid = Guid('b8030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_JPEGXR: Guid = Guid('b8040000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_WINDOWSIMAGEFORMAT: Guid = Guid('b8810000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_WMA: Guid = Guid('b9010000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_WMV: Guid = Guid('b9810000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_WPLPLAYLIST: Guid = Guid('ba100000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_M3UPLAYLIST: Guid = Guid('ba110000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_MPLPLAYLIST: Guid = Guid('ba120000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_ASXPLAYLIST: Guid = Guid('ba130000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_PLSPLAYLIST: Guid = Guid('ba140000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_ABSTRACT_CONTACT_GROUP: Guid = Guid('ba060000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_ABSTRACT_MEDIA_CAST: Guid = Guid('ba0b0000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_VCALENDAR1: Guid = Guid('be020000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_ICALENDAR: Guid = Guid('be030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_ABSTRACT_CONTACT: Guid = Guid('bb810000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_VCARD2: Guid = Guid('bb820000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_VCARD3: Guid = Guid('bb830000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_XML: Guid = Guid('ba820000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_AAC: Guid = Guid('b9030000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_AUDIBLE: Guid = Guid('b9040000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_FLAC: Guid = Guid('b9060000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_QCELP: Guid = Guid('b9070000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_AMR: Guid = Guid('b9080000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_OGG: Guid = Guid('b9020000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_MP4: Guid = Guid('b9820000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_MP2: Guid = Guid('b9830000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_MICROSOFT_WORD: Guid = Guid('ba830000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_MHT_COMPILED_HTML: Guid = Guid('ba840000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_MICROSOFT_EXCEL: Guid = Guid('ba850000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_MICROSOFT_POWERPOINT: Guid = Guid('ba860000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_3GP: Guid = Guid('b9840000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_3G2: Guid = Guid('b9850000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_AVCHD: Guid = Guid('b9860000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_ATSCTS: Guid = Guid('b9870000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_DVBTS: Guid = Guid('b9880000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
WPD_OBJECT_FORMAT_MKV: Guid = Guid('b9900000-ae6c-4804-98-ba-c5-7b-46-96-5f-e7')
def WPD_OBJECT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=2)
def WPD_OBJECT_PARENT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=3)
def WPD_OBJECT_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=4)
def WPD_OBJECT_PERSISTENT_UNIQUE_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=5)
def WPD_OBJECT_FORMAT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=6)
def WPD_OBJECT_ISHIDDEN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=9)
def WPD_OBJECT_ISSYSTEM():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=10)
def WPD_OBJECT_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=11)
def WPD_OBJECT_ORIGINAL_FILE_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=12)
def WPD_OBJECT_NON_CONSUMABLE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=13)
def WPD_OBJECT_KEYWORDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=15)
def WPD_OBJECT_SYNC_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=16)
def WPD_OBJECT_IS_DRM_PROTECTED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=17)
def WPD_OBJECT_DATE_CREATED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=18)
def WPD_OBJECT_DATE_MODIFIED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=19)
def WPD_OBJECT_DATE_AUTHORED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=20)
def WPD_OBJECT_BACK_REFERENCES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=21)
def WPD_OBJECT_CAN_DELETE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=26)
def WPD_OBJECT_LANGUAGE_LOCALE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('ef6b490d-5cd8-437a-af-fc-da-8b-60-ee-4a-3c'), pid=27)
WPD_FOLDER_OBJECT_PROPERTIES_V1: Guid = Guid('7e9a7abf-e568-4b34-aa-2f-13-bb-12-ab-17-7d')
def WPD_FOLDER_CONTENT_TYPES_ALLOWED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7e9a7abf-e568-4b34-aa-2f-13-bb-12-ab-17-7d'), pid=2)
WPD_IMAGE_OBJECT_PROPERTIES_V1: Guid = Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db')
def WPD_IMAGE_BITDEPTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=3)
def WPD_IMAGE_CROPPED_STATUS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=4)
def WPD_IMAGE_COLOR_CORRECTED_STATUS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=5)
def WPD_IMAGE_FNUMBER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=6)
def WPD_IMAGE_EXPOSURE_TIME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=7)
def WPD_IMAGE_EXPOSURE_INDEX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=8)
def WPD_IMAGE_HORIZONTAL_RESOLUTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=9)
def WPD_IMAGE_VERTICAL_RESOLUTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('63d64908-9fa1-479f-85-ba-99-52-21-64-47-db'), pid=10)
WPD_DOCUMENT_OBJECT_PROPERTIES_V1: Guid = Guid('0b110203-eb95-4f02-93-e0-97-c6-31-49-3a-d5')
WPD_MEDIA_PROPERTIES_V1: Guid = Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8')
def WPD_MEDIA_TOTAL_BITRATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=2)
def WPD_MEDIA_BITRATE_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=3)
def WPD_MEDIA_COPYRIGHT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=4)
def WPD_MEDIA_SUBSCRIPTION_CONTENT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=5)
def WPD_MEDIA_USE_COUNT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=6)
def WPD_MEDIA_SKIP_COUNT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=7)
def WPD_MEDIA_LAST_ACCESSED_TIME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=8)
def WPD_MEDIA_PARENTAL_RATING():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=9)
def WPD_MEDIA_META_GENRE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=10)
def WPD_MEDIA_COMPOSER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=11)
def WPD_MEDIA_EFFECTIVE_RATING():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=12)
def WPD_MEDIA_SUB_TITLE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=13)
def WPD_MEDIA_RELEASE_DATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=14)
def WPD_MEDIA_SAMPLE_RATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=15)
def WPD_MEDIA_STAR_RATING():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=16)
def WPD_MEDIA_USER_EFFECTIVE_RATING():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=17)
def WPD_MEDIA_TITLE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=18)
def WPD_MEDIA_DURATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=19)
def WPD_MEDIA_BUY_NOW():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=20)
def WPD_MEDIA_ENCODING_PROFILE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=21)
def WPD_MEDIA_WIDTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=22)
def WPD_MEDIA_HEIGHT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=23)
def WPD_MEDIA_ARTIST():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=24)
def WPD_MEDIA_ALBUM_ARTIST():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=25)
def WPD_MEDIA_OWNER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=26)
def WPD_MEDIA_MANAGING_EDITOR():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=27)
def WPD_MEDIA_WEBMASTER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=28)
def WPD_MEDIA_SOURCE_URL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=29)
def WPD_MEDIA_DESTINATION_URL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=30)
def WPD_MEDIA_DESCRIPTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=31)
def WPD_MEDIA_GENRE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=32)
def WPD_MEDIA_TIME_BOOKMARK():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=33)
def WPD_MEDIA_OBJECT_BOOKMARK():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=34)
def WPD_MEDIA_LAST_BUILD_DATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=35)
def WPD_MEDIA_BYTE_BOOKMARK():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=36)
def WPD_MEDIA_TIME_TO_LIVE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=37)
def WPD_MEDIA_GUID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=38)
def WPD_MEDIA_SUB_DESCRIPTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=39)
def WPD_MEDIA_AUDIO_ENCODING_PROFILE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2ed8ba05-0ad3-42dc-b0-d0-bc-95-ac-39-6a-c8'), pid=49)
WPD_CONTACT_OBJECT_PROPERTIES_V1: Guid = Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b')
def WPD_CONTACT_DISPLAY_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=2)
def WPD_CONTACT_FIRST_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=3)
def WPD_CONTACT_MIDDLE_NAMES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=4)
def WPD_CONTACT_LAST_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=5)
def WPD_CONTACT_PREFIX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=6)
def WPD_CONTACT_SUFFIX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=7)
def WPD_CONTACT_PHONETIC_FIRST_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=8)
def WPD_CONTACT_PHONETIC_LAST_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=9)
def WPD_CONTACT_PERSONAL_FULL_POSTAL_ADDRESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=10)
def WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE1():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=11)
def WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=12)
def WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_CITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=13)
def WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_REGION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=14)
def WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_POSTAL_CODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=15)
def WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_COUNTRY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=16)
def WPD_CONTACT_BUSINESS_FULL_POSTAL_ADDRESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=17)
def WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE1():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=18)
def WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=19)
def WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_CITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=20)
def WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_REGION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=21)
def WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_POSTAL_CODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=22)
def WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_COUNTRY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=23)
def WPD_CONTACT_OTHER_FULL_POSTAL_ADDRESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=24)
def WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE1():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=25)
def WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=26)
def WPD_CONTACT_OTHER_POSTAL_ADDRESS_CITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=27)
def WPD_CONTACT_OTHER_POSTAL_ADDRESS_REGION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=28)
def WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_CODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=29)
def WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_COUNTRY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=30)
def WPD_CONTACT_PRIMARY_EMAIL_ADDRESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=31)
def WPD_CONTACT_PERSONAL_EMAIL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=32)
def WPD_CONTACT_PERSONAL_EMAIL2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=33)
def WPD_CONTACT_BUSINESS_EMAIL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=34)
def WPD_CONTACT_BUSINESS_EMAIL2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=35)
def WPD_CONTACT_OTHER_EMAILS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=36)
def WPD_CONTACT_PRIMARY_PHONE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=37)
def WPD_CONTACT_PERSONAL_PHONE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=38)
def WPD_CONTACT_PERSONAL_PHONE2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=39)
def WPD_CONTACT_BUSINESS_PHONE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=40)
def WPD_CONTACT_BUSINESS_PHONE2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=41)
def WPD_CONTACT_MOBILE_PHONE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=42)
def WPD_CONTACT_MOBILE_PHONE2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=43)
def WPD_CONTACT_PERSONAL_FAX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=44)
def WPD_CONTACT_BUSINESS_FAX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=45)
def WPD_CONTACT_PAGER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=46)
def WPD_CONTACT_OTHER_PHONES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=47)
def WPD_CONTACT_PRIMARY_WEB_ADDRESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=48)
def WPD_CONTACT_PERSONAL_WEB_ADDRESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=49)
def WPD_CONTACT_BUSINESS_WEB_ADDRESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=50)
def WPD_CONTACT_INSTANT_MESSENGER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=51)
def WPD_CONTACT_INSTANT_MESSENGER2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=52)
def WPD_CONTACT_INSTANT_MESSENGER3():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=53)
def WPD_CONTACT_COMPANY_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=54)
def WPD_CONTACT_PHONETIC_COMPANY_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=55)
def WPD_CONTACT_ROLE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=56)
def WPD_CONTACT_BIRTHDATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=57)
def WPD_CONTACT_PRIMARY_FAX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=58)
def WPD_CONTACT_SPOUSE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=59)
def WPD_CONTACT_CHILDREN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=60)
def WPD_CONTACT_ASSISTANT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=61)
def WPD_CONTACT_ANNIVERSARY_DATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=62)
def WPD_CONTACT_RINGTONE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('fbd4fdab-987d-4777-b3-f9-72-61-85-a9-31-2b'), pid=63)
WPD_MUSIC_OBJECT_PROPERTIES_V1: Guid = Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6')
def WPD_MUSIC_ALBUM():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=3)
def WPD_MUSIC_TRACK():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=4)
def WPD_MUSIC_LYRICS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=6)
def WPD_MUSIC_MOOD():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=8)
def WPD_AUDIO_BITRATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=9)
def WPD_AUDIO_CHANNEL_COUNT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=10)
def WPD_AUDIO_FORMAT_CODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=11)
def WPD_AUDIO_BIT_DEPTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=12)
def WPD_AUDIO_BLOCK_ALIGNMENT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b324f56a-dc5d-46e5-b6-df-d2-ea-41-48-88-c6'), pid=13)
WPD_VIDEO_OBJECT_PROPERTIES_V1: Guid = Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a')
def WPD_VIDEO_AUTHOR():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=2)
def WPD_VIDEO_RECORDEDTV_STATION_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=4)
def WPD_VIDEO_RECORDEDTV_CHANNEL_NUMBER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=5)
def WPD_VIDEO_RECORDEDTV_REPEAT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=7)
def WPD_VIDEO_BUFFER_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=8)
def WPD_VIDEO_CREDITS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=9)
def WPD_VIDEO_KEY_FRAME_DISTANCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=10)
def WPD_VIDEO_QUALITY_SETTING():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=11)
def WPD_VIDEO_SCAN_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=12)
def WPD_VIDEO_BITRATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=13)
def WPD_VIDEO_FOURCC_CODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=14)
def WPD_VIDEO_FRAMERATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('346f2163-f998-4146-8b-01-d1-9b-4c-00-de-9a'), pid=15)
WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1: Guid = Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f')
def WPD_COMMON_INFORMATION_SUBJECT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=2)
def WPD_COMMON_INFORMATION_BODY_TEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=3)
def WPD_COMMON_INFORMATION_PRIORITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=4)
def WPD_COMMON_INFORMATION_START_DATETIME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=5)
def WPD_COMMON_INFORMATION_END_DATETIME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=6)
def WPD_COMMON_INFORMATION_NOTES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b28ae94b-05a4-4e8e-be-01-72-cc-7e-09-9d-8f'), pid=7)
WPD_MEMO_OBJECT_PROPERTIES_V1: Guid = Guid('5ffbfc7b-7483-41ad-af-b9-da-3f-4e-59-2b-8d')
WPD_EMAIL_OBJECT_PROPERTIES_V1: Guid = Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5')
def WPD_EMAIL_TO_LINE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=2)
def WPD_EMAIL_CC_LINE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=3)
def WPD_EMAIL_BCC_LINE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=4)
def WPD_EMAIL_HAS_BEEN_READ():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=7)
def WPD_EMAIL_RECEIVED_TIME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=8)
def WPD_EMAIL_HAS_ATTACHMENTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=9)
def WPD_EMAIL_SENDER_ADDRESS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('41f8f65a-5484-4782-b1-3d-47-40-dd-7c-37-c5'), pid=10)
WPD_APPOINTMENT_OBJECT_PROPERTIES_V1: Guid = Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3')
def WPD_APPOINTMENT_LOCATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=3)
def WPD_APPOINTMENT_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=7)
def WPD_APPOINTMENT_REQUIRED_ATTENDEES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=8)
def WPD_APPOINTMENT_OPTIONAL_ATTENDEES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=9)
def WPD_APPOINTMENT_ACCEPTED_ATTENDEES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=10)
def WPD_APPOINTMENT_RESOURCES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=11)
def WPD_APPOINTMENT_TENTATIVE_ATTENDEES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=12)
def WPD_APPOINTMENT_DECLINED_ATTENDEES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f99efd03-431d-40d8-a1-c9-4e-22-0d-9c-88-d3'), pid=13)
WPD_TASK_OBJECT_PROPERTIES_V1: Guid = Guid('e354e95e-d8a0-4637-a0-3a-0c-b2-68-38-db-c7')
def WPD_TASK_STATUS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e354e95e-d8a0-4637-a0-3a-0c-b2-68-38-db-c7'), pid=6)
def WPD_TASK_PERCENT_COMPLETE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e354e95e-d8a0-4637-a0-3a-0c-b2-68-38-db-c7'), pid=8)
def WPD_TASK_REMINDER_DATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e354e95e-d8a0-4637-a0-3a-0c-b2-68-38-db-c7'), pid=10)
def WPD_TASK_OWNER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e354e95e-d8a0-4637-a0-3a-0c-b2-68-38-db-c7'), pid=11)
WPD_SMS_OBJECT_PROPERTIES_V1: Guid = Guid('7e1074cc-50ff-4dd1-a7-42-53-be-6f-09-3a-0d')
def WPD_SMS_PROVIDER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7e1074cc-50ff-4dd1-a7-42-53-be-6f-09-3a-0d'), pid=2)
def WPD_SMS_TIMEOUT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7e1074cc-50ff-4dd1-a7-42-53-be-6f-09-3a-0d'), pid=3)
def WPD_SMS_MAX_PAYLOAD():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7e1074cc-50ff-4dd1-a7-42-53-be-6f-09-3a-0d'), pid=4)
def WPD_SMS_ENCODING():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7e1074cc-50ff-4dd1-a7-42-53-be-6f-09-3a-0d'), pid=5)
WPD_SECTION_OBJECT_PROPERTIES_V1: Guid = Guid('516afd2b-c64e-44f0-98-dc-be-e1-c8-8f-7d-66')
def WPD_SECTION_DATA_OFFSET():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('516afd2b-c64e-44f0-98-dc-be-e1-c8-8f-7d-66'), pid=2)
def WPD_SECTION_DATA_LENGTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('516afd2b-c64e-44f0-98-dc-be-e1-c8-8f-7d-66'), pid=3)
def WPD_SECTION_DATA_UNITS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('516afd2b-c64e-44f0-98-dc-be-e1-c8-8f-7d-66'), pid=4)
def WPD_SECTION_DATA_REFERENCED_OBJECT_RESOURCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('516afd2b-c64e-44f0-98-dc-be-e1-c8-8f-7d-66'), pid=5)
NAME_Undefined: String = 'Undefined'
NAME_Association: String = 'Association'
NAME_DeviceScript: String = 'DeviceScript'
NAME_DeviceExecutable: String = 'DeviceExecutable'
NAME_TextDocument: String = 'TextDocument'
NAME_HTMLDocument: String = 'HTMLDocument'
NAME_DPOFDocument: String = 'DPOFDocument'
NAME_AIFFFile: String = 'AIFFFile'
NAME_WAVFile: String = 'WAVFile'
NAME_MP3File: String = 'MP3File'
NAME_AVIFile: String = 'AVIFile'
NAME_MPEGFile: String = 'MPEGFile'
NAME_ASFFile: String = 'ASFFile'
NAME_UnknownImage: String = 'UnknownImage'
NAME_EXIFImage: String = 'EXIFImage'
NAME_TIFFEPImage: String = 'TIFFEPImage'
NAME_FlashPixImage: String = 'FlashPixImage'
NAME_BMPImage: String = 'BMPImage'
NAME_CIFFImage: String = 'CIFFImage'
NAME_GIFImage: String = 'GIFImage'
NAME_JFIFImage: String = 'JFIFImage'
NAME_PCDImage: String = 'PCDImage'
NAME_PICTImage: String = 'PICTImage'
NAME_PNGImage: String = 'PNGImage'
NAME_TIFFImage: String = 'TIFFImage'
NAME_TIFFITImage: String = 'TIFFITImage'
NAME_JP2Image: String = 'JP2Image'
NAME_JPXImage: String = 'JPXImage'
NAME_FirmwareFile: String = 'FirmwareFile'
NAME_WBMPImage: String = 'WBMPImage'
NAME_JPEGXRImage: String = 'JPEGXRImage'
NAME_HDPhotoImage: String = 'HDPhotoImage'
NAME_UndefinedAudio: String = 'UndefinedAudio'
NAME_WMAFile: String = 'WMAFile'
NAME_OGGFile: String = 'OGGFile'
NAME_AACFile: String = 'AACFile'
NAME_AudibleFile: String = 'AudibleFile'
NAME_FLACFile: String = 'FLACFile'
NAME_QCELPFile: String = 'QCELPFile'
NAME_AMRFile: String = 'AMRFile'
NAME_UndefinedVideo: String = 'UndefinedVideo'
NAME_WMVFile: String = 'WMVFile'
NAME_MPEG4File: String = 'MPEG4File'
NAME_MPEG2File: String = 'MPEG2File'
NAME_3GPPFile: String = '3GPPFile'
NAME_3GPP2File: String = '3GPP2File'
NAME_AVCHDFile: String = 'AVCHDFile'
NAME_ATSCTSFile: String = 'ATSCTSFile'
NAME_DVBTSFile: String = 'DVBTSFile'
NAME_UndefinedCollection: String = 'UndefinedCollection'
NAME_AbstractMultimediaAlbum: String = 'AbstractMultimediaAlbum'
NAME_AbstractImageAlbum: String = 'AbstractImageAlbum'
NAME_AbstractAudioAlbum: String = 'AbstractAudioAlbum'
NAME_AbstractVideoAlbum: String = 'AbstractVideoAlbum'
NAME_AbstractAudioVideoAlbum: String = 'AbstractAudioVideoAlbum'
NAME_AbstractChapteredProduction: String = 'AbstractChapteredProduction'
NAME_AbstractAudioPlaylist: String = 'AbstractAudioPlaylist'
NAME_AbstractVideoPlaylist: String = 'AbstractVideoPlaylist'
NAME_AbstractMediacast: String = 'AbstractMediacast'
NAME_WPLPlaylist: String = 'WPLPlaylist'
NAME_M3UPlaylist: String = 'M3UPlaylist'
NAME_MPLPlaylist: String = 'MPLPlaylist'
NAME_ASXPlaylist: String = 'ASXPlaylist'
NAME_PSLPlaylist: String = 'PSLPlaylist'
NAME_UndefinedDocument: String = 'UndefinedDocument'
NAME_AbstractDocument: String = 'AbstractDocument'
NAME_XMLDocument: String = 'XMLDocument'
NAME_WordDocument: String = 'WordDocument'
NAME_MHTDocument: String = 'MHTDocument'
NAME_ExcelDocument: String = 'ExcelDocument'
NAME_PowerPointDocument: String = 'PowerPointDocument'
NAME_GenericObj_ObjectID: String = 'ObjectID'
NAME_GenericObj_ReferenceParentID: String = 'ReferenceParentID'
NAME_GenericObj_StorageID: String = 'StorageID'
NAME_GenericObj_ObjectFormat: String = 'ObjectFormat'
NAME_GenericObj_ProtectionStatus: String = 'ProtectionStatus'
NAME_GenericObj_ObjectSize: String = 'ObjectSize'
NAME_GenericObj_AssociationType: String = 'AssociationType'
NAME_GenericObj_AssociationDesc: String = 'AssociationDesc'
NAME_GenericObj_ObjectFileName: String = 'ObjectFileName'
NAME_GenericObj_DateCreated: String = 'DateCreated'
NAME_GenericObj_DateModified: String = 'DateModified'
NAME_GenericObj_Keywords: String = 'Keywords'
NAME_GenericObj_ParentID: String = 'ParentID'
NAME_GenericObj_AllowedFolderContents: String = 'AllowedFolderContents'
NAME_GenericObj_Hidden: String = 'Hidden'
NAME_GenericObj_SystemObject: String = 'SystemObject'
NAME_GenericObj_PersistentUID: String = 'PersistentUID'
NAME_GenericObj_SyncID: String = 'SyncID'
NAME_GenericObj_PropertyBag: String = 'PropertyBag'
NAME_GenericObj_Name: String = 'Name'
NAME_MediaObj_Artist: String = 'Artist'
NAME_GenericObj_DateAuthored: String = 'DateAuthored'
NAME_GenericObj_Description: String = 'Description'
NAME_GenericObj_LanguageLocale: String = 'LanguageLocale'
NAME_GenericObj_Copyright: String = 'Copyright'
NAME_VideoObj_Source: String = 'Source'
NAME_MediaObj_GeographicOrigin: String = 'GeographicOrigin'
NAME_GenericObj_DateAdded: String = 'DateAdded'
NAME_GenericObj_NonConsumable: String = 'NonConsumable'
NAME_GenericObj_Corrupt: String = 'Corrupt'
NAME_MediaObj_Width: String = 'Width'
NAME_MediaObj_Height: String = 'Height'
NAME_MediaObj_Duration: String = 'Duration'
NAME_MediaObj_UserRating: String = 'UserRating'
NAME_MediaObj_Track: String = 'Track'
NAME_MediaObj_Genre: String = 'Genre'
NAME_MediaObj_Credits: String = 'Credits'
NAME_AudioObj_Lyrics: String = 'Lyrics'
NAME_MediaObj_SubscriptionContentID: String = 'SubscriptionContentID'
NAME_MediaObj_Producer: String = 'Producer'
NAME_MediaObj_UseCount: String = 'UseCount'
NAME_MediaObj_SkipCount: String = 'SkipCount'
NAME_GenericObj_DateAccessed: String = 'DateAccessed'
NAME_MediaObj_ParentalRating: String = 'ParentalRating'
NAME_MediaObj_MediaType: String = 'MediaType'
NAME_MediaObj_Composer: String = 'Composer'
NAME_MediaObj_EffectiveRating: String = 'EffectiveRating'
NAME_MediaObj_Subtitle: String = 'Subtitle'
NAME_MediaObj_DateOriginalRelease: String = 'DateOriginalRelease'
NAME_MediaObj_AlbumName: String = 'AlbumName'
NAME_MediaObj_AlbumArtist: String = 'AlbumArtist'
NAME_MediaObj_Mood: String = 'Mood'
NAME_GenericObj_DRMStatus: String = 'DRMStatus'
NAME_GenericObj_SubDescription: String = 'SubDescription'
NAME_ImageObj_IsCropped: String = 'IsCropped'
NAME_ImageObj_IsColorCorrected: String = 'IsColorCorrected'
NAME_ImageObj_ImageBitDepth: String = 'ImageBitDepth'
NAME_ImageObj_Aperature: String = 'Aperature'
NAME_ImageObj_Exposure: String = 'Exposure'
NAME_ImageObj_ISOSpeed: String = 'ISOSpeed'
NAME_MediaObj_Owner: String = 'Owner'
NAME_MediaObj_Editor: String = 'Editor'
NAME_MediaObj_WebMaster: String = 'WebMaster'
NAME_MediaObj_URLSource: String = 'URLSource'
NAME_MediaObj_URLLink: String = 'URLLink'
NAME_MediaObj_BookmarkTime: String = 'BookmarkTime'
NAME_MediaObj_BookmarkObject: String = 'BookmarkObject'
NAME_MediaObj_BookmarkByte: String = 'BookmarkByte'
NAME_GenericObj_DateRevised: String = 'DateRevised'
NAME_GenericObj_TimeToLive: String = 'TimeToLive'
NAME_MediaObj_MediaUID: String = 'MediaUID'
NAME_MediaObj_TotalBitRate: String = 'TotalBitRate'
NAME_MediaObj_BitRateType: String = 'BitRateType'
NAME_MediaObj_SampleRate: String = 'SampleRate'
NAME_AudioObj_Channels: String = 'Channels'
NAME_AudioObj_AudioBitDepth: String = 'AudioBitDepth'
NAME_AudioObj_AudioBlockAlignment: String = 'AudioBlockAlignment'
NAME_VideoObj_ScanType: String = 'ScanType'
NAME_AudioObj_AudioFormatCode: String = 'AudioFormatCode'
NAME_AudioObj_AudioBitRate: String = 'AudioBitRate'
NAME_VideoObj_VideoFormatCode: String = 'VideoFormatCode'
NAME_VideoObj_VideoBitRate: String = 'VideoBitRate'
NAME_VideoObj_VideoFrameRate: String = 'VideoFrameRate'
NAME_VideoObj_KeyFrameDistance: String = 'KeyFrameDistance'
NAME_MediaObj_BufferSize: String = 'BufferSize'
NAME_MediaObj_EncodingQuality: String = 'EncodingQuality'
NAME_MediaObj_EncodingProfile: String = 'EncodingProfile'
NAME_MediaObj_AudioEncodingProfile: String = 'AudioEncodingProfile'
DEVSVC_SERVICEINFO_VERSION: UInt32 = 100
DEVSVCTYPE_DEFAULT: UInt32 = 0
DEVSVCTYPE_ABSTRACT: UInt32 = 1
NAME_Services_ServiceDisplayName: String = 'ServiceDisplayName'
NAME_Services_ServiceIcon: String = 'ServiceIcon'
NAME_Services_ServiceLocale: String = 'ServiceLocale'
NAME_CalendarSvc: String = 'Calendar'
TYPE_CalendarSvc: UInt32 = 0
NAME_CalendarSvc_SyncWindowStart: String = 'SyncWindowStart'
NAME_CalendarSvc_SyncWindowEnd: String = 'SyncWindowEnd'
NAME_AbstractActivity: String = 'AbstractActivity'
NAME_AbstractActivityOccurrence: String = 'AbstractActivityOccurrence'
NAME_VCalendar1Activity: String = 'VCalendar1'
NAME_ICalendarActivity: String = 'ICalendar'
NAME_CalendarObj_Location: String = 'Location'
NAME_CalendarObj_Accepted: String = 'Accepted'
NAME_CalendarObj_Tentative: String = 'Tentative'
NAME_CalendarObj_Declined: String = 'Declined'
NAME_CalendarObj_TimeZone: String = 'TimeZone'
NAME_CalendarObj_ReminderOffset: String = 'ReminderOffset'
NAME_CalendarObj_BusyStatus: String = 'BusyStatus'
ENUM_CalendarObj_BusyStatusFree: UInt32 = 0
ENUM_CalendarObj_BusyStatusBusy: UInt32 = 1
ENUM_CalendarObj_BusyStatusOutOfOffice: UInt32 = 2
ENUM_CalendarObj_BusyStatusTentative: UInt32 = 3
NAME_CalendarObj_PatternStartTime: String = 'PatternStartTime'
NAME_CalendarObj_PatternDuration: String = 'PatternDuration'
NAME_CalendarObj_BeginDateTime: String = 'BeginDateTime'
NAME_CalendarObj_EndDateTime: String = 'EndDateTime'
NAME_HintsSvc: String = 'Hints'
TYPE_HintsSvc: UInt32 = 0
NAME_MessageSvc: String = 'Message'
TYPE_MessageSvc: UInt32 = 0
NAME_AbstractMessage: String = 'AbstractMessage'
NAME_AbstractMessageFolder: String = 'AbstractMessageFolder'
NAME_MessageObj_Subject: String = 'Subject'
NAME_MessageObj_Body: String = 'Body'
NAME_MessageObj_Priority: String = 'Priority'
ENUM_MessageObj_PriorityHighest: UInt32 = 2
ENUM_MessageObj_PriorityNormal: UInt32 = 1
ENUM_MessageObj_PriorityLowest: UInt32 = 0
NAME_MessageObj_Category: String = 'Category'
NAME_MessageObj_Sender: String = 'Sender'
NAME_MessageObj_To: String = 'To'
NAME_MessageObj_CC: String = 'CC'
NAME_MessageObj_BCC: String = 'BCC'
NAME_MessageObj_Read: String = 'Read'
ENUM_MessageObj_ReadFalse: UInt32 = 0
ENUM_MessageObj_ReadTrue: UInt32 = 255
NAME_MessageObj_ReceivedTime: String = 'ReceivedTime'
NAME_MessageObj_PatternOriginalDateTime: String = 'PatternOriginalDateTime'
NAME_MessageObj_PatternType: String = 'PatternType'
ENUM_MessageObj_PatternTypeDaily: UInt32 = 1
ENUM_MessageObj_PatternTypeWeekly: UInt32 = 2
ENUM_MessageObj_PatternTypeMonthly: UInt32 = 3
ENUM_MessageObj_PatternTypeYearly: UInt32 = 4
NAME_MessageObj_PatternValidStartDate: String = 'PatternValidStartDate'
NAME_MessageObj_PatternValidEndDate: String = 'PatternValidEndDate'
NAME_MessageObj_PatternPeriod: String = 'PatternPeriod'
NAME_MessageObj_PatternDayOfWeek: String = 'PatternDayOfWeek'
FLAG_MessageObj_DayOfWeekNone: UInt32 = 0
FLAG_MessageObj_DayOfWeekSunday: UInt32 = 1
FLAG_MessageObj_DayOfWeekMonday: UInt32 = 2
FLAG_MessageObj_DayOfWeekTuesday: UInt32 = 4
FLAG_MessageObj_DayOfWeekWednesday: UInt32 = 8
FLAG_MessageObj_DayOfWeekThursday: UInt32 = 16
FLAG_MessageObj_DayOfWeekFriday: UInt32 = 32
FLAG_MessageObj_DayOfWeekSaturday: UInt32 = 64
NAME_MessageObj_PatternDayOfMonth: String = 'PatternDayOfMonth'
RANGEMIN_MessageObj_PatternDayOfMonth: UInt32 = 1
RANGEMAX_MessageObj_PatternDayOfMonth: UInt32 = 31
RANGESTEP_MessageObj_PatternDayOfMonth: UInt32 = 1
NAME_MessageObj_PatternMonthOfYear: String = 'PatternMonthOfYear'
RANGEMIN_MessageObj_PatternMonthOfYear: UInt32 = 1
RANGEMAX_MessageObj_PatternMonthOfYear: UInt32 = 12
RANGESTEP_MessageObj_PatternMonthOfYear: UInt32 = 1
NAME_MessageObj_PatternInstance: String = 'PatternInstance'
ENUM_MessageObj_PatternInstanceNone: UInt32 = 0
ENUM_MessageObj_PatternInstanceFirst: UInt32 = 1
ENUM_MessageObj_PatternInstanceSecond: UInt32 = 2
ENUM_MessageObj_PatternInstanceThird: UInt32 = 3
ENUM_MessageObj_PatternInstanceFourth: UInt32 = 4
ENUM_MessageObj_PatternInstanceLast: UInt32 = 5
NAME_MessageObj_PatternDeleteDates: String = 'PatternDeleteDates'
NAME_DeviceMetadataSvc: String = 'Metadata'
TYPE_DeviceMetadataSvc: UInt32 = 0
NAME_DeviceMetadataCAB: String = 'DeviceMetadataCAB'
NAME_DeviceMetadataObj_ContentID: String = 'ContentID'
NAME_DeviceMetadataObj_DefaultCAB: String = 'DefaultCAB'
ENUM_DeviceMetadataObj_DefaultCABFalse: UInt32 = 0
ENUM_DeviceMetadataObj_DefaultCABTrue: UInt32 = 1
NAME_NotesSvc: String = 'Notes'
TYPE_NotesSvc: UInt32 = 0
NAME_AbstractNote: String = 'AbstractNote'
NAME_StatusSvc: String = 'Status'
TYPE_StatusSvc: UInt32 = 0
NAME_StatusSvc_SignalStrength: String = 'SignalStrength'
RANGEMIN_StatusSvc_SignalStrength: UInt32 = 0
RANGEMAX_StatusSvc_SignalStrength: UInt32 = 4
RANGESTEP_StatusSvc_SignalStrength: UInt32 = 1
NAME_StatusSvc_TextMessages: String = 'TextMessages'
RANGEMAX_StatusSvc_TextMessages: UInt32 = 255
NAME_StatusSvc_NewPictures: String = 'NewPictures'
RANGEMAX_StatusSvc_NewPictures: UInt32 = 65535
NAME_StatusSvc_MissedCalls: String = 'MissedCalls'
RANGEMAX_StatusSvc_MissedCalls: UInt32 = 255
NAME_StatusSvc_VoiceMail: String = 'VoiceMail'
RANGEMAX_StatusSvc_VoiceMail: UInt32 = 255
NAME_StatusSvc_NetworkName: String = 'NetworkName'
NAME_StatusSvc_NetworkType: String = 'NetworkType'
NAME_StatusSvc_Roaming: String = 'Roaming'
ENUM_StatusSvc_RoamingInactive: UInt32 = 0
ENUM_StatusSvc_RoamingActive: UInt32 = 1
ENUM_StatusSvc_RoamingUnknown: UInt32 = 2
NAME_StatusSvc_BatteryLife: String = 'BatteryLife'
RANGEMIN_StatusSvc_BatteryLife: UInt32 = 0
RANGEMAX_StatusSvc_BatteryLife: UInt32 = 100
RANGESTEP_StatusSvc_BatteryLife: UInt32 = 1
NAME_StatusSvc_ChargingState: String = 'ChargingState'
ENUM_StatusSvc_ChargingInactive: UInt32 = 0
ENUM_StatusSvc_ChargingActive: UInt32 = 1
ENUM_StatusSvc_ChargingUnknown: UInt32 = 2
NAME_StatusSvc_StorageCapacity: String = 'StorageCapacity'
NAME_StatusSvc_StorageFreeSpace: String = 'StorageFreeSpace'
NAME_SyncSvc_SyncFormat: String = 'SyncFormat'
NAME_SyncSvc_LocalOnlyDelete: String = 'LocalOnlyDelete'
NAME_SyncSvc_FilterType: String = 'FilterType'
SYNCSVC_FILTER_NONE: UInt32 = 0
SYNCSVC_FILTER_CONTACTS_WITH_PHONE: UInt32 = 1
SYNCSVC_FILTER_TASK_ACTIVE: UInt32 = 2
SYNCSVC_FILTER_CALENDAR_WINDOW_WITH_RECURRENCE: UInt32 = 3
NAME_SyncSvc_SyncObjectReferences: String = 'SyncObjectReferences'
ENUM_SyncSvc_SyncObjectReferencesDisabled: UInt32 = 0
ENUM_SyncSvc_SyncObjectReferencesEnabled: UInt32 = 255
NAME_SyncObj_LastAuthorProxyID: String = 'LastAuthorProxyID'
NAME_SyncSvc_BeginSync: String = 'BeginSync'
NAME_SyncSvc_EndSync: String = 'EndSync'
NAME_TasksSvc: String = 'Tasks'
TYPE_TasksSvc: UInt32 = 0
NAME_TasksSvc_SyncActiveOnly: String = 'FilterType'
NAME_AbstractTask: String = 'AbstractTask'
NAME_TaskObj_ReminderDateTime: String = 'ReminderDateTime'
NAME_TaskObj_Complete: String = 'Complete'
ENUM_TaskObj_CompleteFalse: UInt32 = 0
ENUM_TaskObj_CompleteTrue: UInt32 = 255
NAME_TaskObj_BeginDate: String = 'BeginDate'
NAME_TaskObj_EndDate: String = 'EndDate'
WPD_CATEGORY_MTP_EXT_VENDOR_OPERATIONS: Guid = Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56')
def WPD_COMMAND_MTP_EXT_GET_SUPPORTED_VENDOR_OPCODES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=11)
def WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITHOUT_DATA_PHASE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=12)
def WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITH_DATA_TO_READ():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=13)
def WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITH_DATA_TO_WRITE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=14)
def WPD_COMMAND_MTP_EXT_READ_DATA():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=15)
def WPD_COMMAND_MTP_EXT_WRITE_DATA():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=16)
def WPD_COMMAND_MTP_EXT_END_DATA_TRANSFER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=17)
def WPD_COMMAND_MTP_EXT_GET_VENDOR_EXTENSION_DESCRIPTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=18)
def WPD_PROPERTY_MTP_EXT_OPERATION_CODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1001)
def WPD_PROPERTY_MTP_EXT_OPERATION_PARAMS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1002)
def WPD_PROPERTY_MTP_EXT_RESPONSE_CODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1003)
def WPD_PROPERTY_MTP_EXT_RESPONSE_PARAMS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1004)
def WPD_PROPERTY_MTP_EXT_VENDOR_OPERATION_CODES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1005)
def WPD_PROPERTY_MTP_EXT_TRANSFER_CONTEXT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1006)
def WPD_PROPERTY_MTP_EXT_TRANSFER_TOTAL_DATA_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1007)
def WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_TO_READ():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1008)
def WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_READ():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1009)
def WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_TO_WRITE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1010)
def WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_WRITTEN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1011)
def WPD_PROPERTY_MTP_EXT_TRANSFER_DATA():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1012)
def WPD_PROPERTY_MTP_EXT_OPTIMAL_TRANSFER_BUFFER_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1013)
def WPD_PROPERTY_MTP_EXT_VENDOR_EXTENSION_DESCRIPTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-1a2e-4106-a3-57-77-1e-08-19-fc-56'), pid=1014)
WPD_PROPERTIES_MTP_VENDOR_EXTENDED_OBJECT_PROPS: Guid = Guid('4d545058-4fce-4578-95-c8-86-98-a9-bc-0f-49')
WPD_PROPERTIES_MTP_VENDOR_EXTENDED_DEVICE_PROPS: Guid = Guid('4d545058-8900-40b3-8f-1d-dc-24-6e-1e-83-70')
WPD_EVENT_MTP_VENDOR_EXTENDED_EVENTS: Guid = Guid('00000000-5738-4ff2-84-45-be-31-26-69-10-59')
def WPD_PROPERTY_MTP_EXT_EVENT_PARAMS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4d545058-ef88-4e4d-95-c3-4f-32-7f-72-8a-96'), pid=1011)
CLSID_WPD_NAMESPACE_EXTENSION: Guid = Guid('35786d3c-b075-49b9-88-dd-02-98-76-e1-1c-01')
WPDNSE_OBJECT_PROPERTIES_V1: Guid = Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6')
def WPDNSE_OBJECT_HAS_CONTACT_PHOTO():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=2)
def WPDNSE_OBJECT_HAS_THUMBNAIL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=3)
def WPDNSE_OBJECT_HAS_ICON():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=4)
def WPDNSE_OBJECT_HAS_AUDIO_CLIP():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=5)
def WPDNSE_OBJECT_HAS_ALBUM_ART():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=6)
def WPDNSE_OBJECT_OPTIMAL_READ_BLOCK_SIZE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('34d71409-4b47-4d80-aa-ac-3a-28-a4-a3-b3-e6'), pid=7)
WPDNSE_PROPSHEET_DEVICE_GENERAL: UInt32 = 1
WPDNSE_PROPSHEET_STORAGE_GENERAL: UInt32 = 2
WPDNSE_PROPSHEET_CONTENT_GENERAL: UInt32 = 4
WPDNSE_PROPSHEET_CONTENT_REFERENCES: UInt32 = 8
WPDNSE_PROPSHEET_CONTENT_RESOURCES: UInt32 = 16
WPDNSE_PROPSHEET_CONTENT_DETAILS: UInt32 = 32
STR_WPDNSE_FAST_ENUM: String = 'WPDNSE Fast Enum'
STR_WPDNSE_SIMPLE_ITEM: String = 'WPDNSE SimpleItem'
NAME_ContactsSvc: String = 'Contacts'
TYPE_ContactsSvc: UInt32 = 0
NAME_ContactSvc_SyncWithPhoneOnly: String = 'FilterType'
NAME_AbstractContact: String = 'AbstractContact'
NAME_VCard2Contact: String = 'VCard2Contact'
NAME_VCard3Contact: String = 'VCard3Contact'
NAME_AbstractContactGroup: String = 'AbstractContactGroup'
NAME_ContactObj_GivenName: String = 'GivenName'
NAME_ContactObj_MiddleNames: String = 'MiddleNames'
NAME_ContactObj_FamilyName: String = 'FamilyName'
NAME_ContactObj_Title: String = 'Title'
NAME_ContactObj_Suffix: String = 'Suffix'
NAME_ContactObj_PhoneticGivenName: String = 'PhoneticGivenName'
NAME_ContactObj_PhoneticFamilyName: String = 'PhoneticFamilyName'
NAME_ContactObj_PersonalAddressFull: String = 'PersonalAddressFull'
NAME_ContactObj_PersonalAddressStreet: String = 'PersonalAddressStreet'
NAME_ContactObj_PersonalAddressLine2: String = 'PersonalAddressLine2'
NAME_ContactObj_PersonalAddressCity: String = 'PersonalAddressCity'
NAME_ContactObj_PersonalAddressRegion: String = 'PersonalAddressRegion'
NAME_ContactObj_PersonalAddressPostalCode: String = 'PersonalAddressPostalCode'
NAME_ContactObj_PersonalAddressCountry: String = 'PersonalAddressCountry'
NAME_ContactObj_BusinessAddressFull: String = 'BusinessAddressFull'
NAME_ContactObj_BusinessAddressStreet: String = 'BusinessAddressStreet'
NAME_ContactObj_BusinessAddressLine2: String = 'BusinessAddressLine2'
NAME_ContactObj_BusinessAddressCity: String = 'BusinessAddressCity'
NAME_ContactObj_BusinessAddressRegion: String = 'BusinessAddressRegion'
NAME_ContactObj_BusinessAddressPostalCode: String = 'BusinessAddressPostalCode'
NAME_ContactObj_BusinessAddressCountry: String = 'BusinessAddressCountry'
NAME_ContactObj_OtherAddressFull: String = 'OtherAddressFull'
NAME_ContactObj_OtherAddressStreet: String = 'OtherAddressStreet'
NAME_ContactObj_OtherAddressLine2: String = 'OtherAddressLine2'
NAME_ContactObj_OtherAddressCity: String = 'OtherAddressCity'
NAME_ContactObj_OtherAddressRegion: String = 'OtherAddressRegion'
NAME_ContactObj_OtherAddressPostalCode: String = 'OtherAddressPostalCode'
NAME_ContactObj_OtherAddressCountry: String = 'OtherAddressCountry'
NAME_ContactObj_Email: String = 'Email'
NAME_ContactObj_PersonalEmail: String = 'PersonalEmail'
NAME_ContactObj_PersonalEmail2: String = 'PersonalEmail2'
NAME_ContactObj_BusinessEmail: String = 'BusinessEmail'
NAME_ContactObj_BusinessEmail2: String = 'BusinessEmail2'
NAME_ContactObj_OtherEmail: String = 'OtherEmail'
NAME_ContactObj_Phone: String = 'Phone'
NAME_ContactObj_PersonalPhone: String = 'PersonalPhone'
NAME_ContactObj_PersonalPhone2: String = 'PersonalPhone2'
NAME_ContactObj_BusinessPhone: String = 'BusinessPhone'
NAME_ContactObj_BusinessPhone2: String = 'BusinessPhone2'
NAME_ContactObj_MobilePhone: String = 'MobilePhone'
NAME_ContactObj_MobilePhone2: String = 'MobilePhone2'
NAME_ContactObj_PersonalFax: String = 'PersonalFax'
NAME_ContactObj_BusinessFax: String = 'BusinessFax'
NAME_ContactObj_Pager: String = 'Pager'
NAME_ContactObj_OtherPhone: String = 'OtherPhone'
NAME_ContactObj_WebAddress: String = 'WebAddress'
NAME_ContactObj_PersonalWebAddress: String = 'PersonalWebAddress'
NAME_ContactObj_BusinessWebAddress: String = 'BusinessWebAddress'
NAME_ContactObj_IMAddress: String = 'IMAddress'
NAME_ContactObj_IMAddress2: String = 'IMAddress2'
NAME_ContactObj_IMAddress3: String = 'IMAddress3'
NAME_ContactObj_Organization: String = 'Organization'
NAME_ContactObj_PhoneticOrganization: String = 'PhoneticOrganization'
NAME_ContactObj_Role: String = 'Role'
NAME_ContactObj_Fax: String = 'Fax'
NAME_ContactObj_Spouse: String = 'Spouse'
NAME_ContactObj_Children: String = 'Children'
NAME_ContactObj_Assistant: String = 'Assistant'
NAME_ContactObj_Ringtone: String = 'Ringtone'
NAME_ContactObj_Birthdate: String = 'Birthdate'
NAME_ContactObj_AnniversaryDate: String = 'AnniversaryDate'
NAME_RingtonesSvc: String = 'Ringtones'
TYPE_RingtonesSvc: UInt32 = 0
NAME_RingtonesSvc_DefaultRingtone: String = 'DefaultRingtone'
NAME_AnchorSyncSvc: String = 'AnchorSync'
TYPE_AnchorSyncSvc: UInt32 = 1
NAME_AnchorSyncSvc_VersionProps: String = 'AnchorVersionProps'
NAME_AnchorSyncSvc_ReplicaID: String = 'AnchorReplicaID'
NAME_AnchorSyncSvc_KnowledgeObjectID: String = 'AnchorKnowledgeObjectID'
NAME_AnchorSyncSvc_LastSyncProxyID: String = 'AnchorLastSyncProxyID'
NAME_AnchorSyncSvc_CurrentAnchor: String = 'AnchorCurrentAnchor'
NAME_AnchorSyncSvc_ProviderVersion: String = 'AnchorProviderVersion'
NAME_AnchorSyncSvc_SyncFormat: String = 'SyncFormat'
NAME_AnchorSyncSvc_LocalOnlyDelete: String = 'LocalOnlyDelete'
NAME_AnchorSyncSvc_FilterType: String = 'FilterType'
NAME_AnchorSyncKnowledge: String = 'AnchorSyncKnowledge'
NAME_AnchorResults: String = 'AnchorResults'
NAME_AnchorResults_AnchorState: String = 'AnchorState'
ENUM_AnchorResults_AnchorStateNormal: UInt32 = 0
ENUM_AnchorResults_AnchorStateInvalid: UInt32 = 1
ENUM_AnchorResults_AnchorStateOld: UInt32 = 2
NAME_AnchorResults_Anchor: String = 'Anchor'
NAME_AnchorResults_ResultObjectID: String = 'ResultObjectID'
NAME_AnchorSyncSvc_GetChangesSinceAnchor: String = 'GetChangesSinceAnchor'
NAME_AnchorSyncSvc_BeginSync: String = 'BeginSync'
NAME_AnchorSyncSvc_EndSync: String = 'EndSync'
ENUM_AnchorResults_ItemStateInvalid: UInt32 = 0
ENUM_AnchorResults_ItemStateDeleted: UInt32 = 1
ENUM_AnchorResults_ItemStateCreated: UInt32 = 2
ENUM_AnchorResults_ItemStateUpdated: UInt32 = 3
ENUM_AnchorResults_ItemStateChanged: UInt32 = 4
NAME_FullEnumSyncSvc: String = 'FullEnumSync'
TYPE_FullEnumSyncSvc: UInt32 = 1
NAME_FullEnumSyncSvc_VersionProps: String = 'FullEnumVersionProps'
NAME_FullEnumSyncSvc_ReplicaID: String = 'FullEnumReplicaID'
NAME_FullEnumSyncSvc_KnowledgeObjectID: String = 'FullEnumKnowledgeObjectID'
NAME_FullEnumSyncSvc_LastSyncProxyID: String = 'FullEnumLastSyncProxyID'
NAME_FullEnumSyncSvc_ProviderVersion: String = 'FullEnumProviderVersion'
NAME_FullEnumSyncSvc_SyncFormat: String = 'SyncFormat'
NAME_FullEnumSyncSvc_LocalOnlyDelete: String = 'LocalOnlyDelete'
NAME_FullEnumSyncSvc_FilterType: String = 'FilterType'
NAME_FullEnumSyncKnowledge: String = 'FullEnumSyncKnowledge'
NAME_FullEnumSyncSvc_BeginSync: String = 'BeginSync'
NAME_FullEnumSyncSvc_EndSync: String = 'EndSync'
@winfunctype('DMProcessXMLFiltered.dll')
def DMProcessConfigXMLFiltered(pszXmlIn: Windows.Win32.Foundation.PWSTR, rgszAllowedCspNodes: POINTER(Windows.Win32.Foundation.PWSTR), dwNumAllowedCspNodes: UInt32, pbstrXmlOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
DELETE_OBJECT_OPTIONS = Int32
PORTABLE_DEVICE_DELETE_NO_RECURSION: DELETE_OBJECT_OPTIONS = 0
PORTABLE_DEVICE_DELETE_WITH_RECURSION: DELETE_OBJECT_OPTIONS = 1
DEVICE_RADIO_STATE = Int32
DRS_RADIO_ON: DEVICE_RADIO_STATE = 0
DRS_SW_RADIO_OFF: DEVICE_RADIO_STATE = 1
DRS_HW_RADIO_OFF: DEVICE_RADIO_STATE = 2
DRS_SW_HW_RADIO_OFF: DEVICE_RADIO_STATE = 3
DRS_HW_RADIO_ON_UNCONTROLLABLE: DEVICE_RADIO_STATE = 4
DRS_RADIO_INVALID: DEVICE_RADIO_STATE = 5
DRS_HW_RADIO_OFF_UNCONTROLLABLE: DEVICE_RADIO_STATE = 6
DRS_RADIO_MAX: DEVICE_RADIO_STATE = 6
EnumBthMtpConnectors = Guid('a1570149-e645-4f43-8b-0d-40-9b-06-1d-b2-fc')
class IConnectionRequestCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('272c9ae0-7161-4ae0-91-bd-9f-44-8e-e9-c4-27')
    @commethod(3)
    def OnComplete(self, hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumPortableDeviceConnectors(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bfdef549-9247-454f-bd-82-06-fe-80-85-3f-aa')
    @commethod(3)
    def Next(self, cRequested: UInt32, pConnectors: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceConnector_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cConnectors: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.Devices.PortableDevices.IEnumPortableDeviceConnectors_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumPortableDeviceObjectIDs(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('10ece955-cf41-4728-bf-a0-41-ee-df-1b-bf-19')
    @commethod(3)
    def Next(self, cObjects: UInt32, pObjIDs: POINTER(Windows.Win32.Foundation.PWSTR), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cObjects: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.Devices.PortableDevices.IEnumPortableDeviceObjectIDs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMediaRadioManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6cfdcab5-fc47-42a5-92-41-07-4b-58-83-0e-73')
    @commethod(3)
    def GetRadioInstances(self, ppCollection: POINTER(Windows.Win32.Devices.PortableDevices.IRadioInstanceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSystemRadioStateChange(self, sysRadioState: Windows.Win32.Devices.PortableDevices.SYSTEM_RADIO_STATE, uTimeoutSec: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMediaRadioManagerNotifySink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('89d81f5f-c147-49ed-a1-1c-77-b2-0c-31-e7-c9')
    @commethod(3)
    def OnInstanceAdd(self, pRadioInstance: Windows.Win32.Devices.PortableDevices.IRadioInstance_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnInstanceRemove(self, bstrRadioInstanceId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnInstanceRadioChange(self, bstrRadioInstanceId: Windows.Win32.Foundation.BSTR, radioState: Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDevice(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('625e2df8-6392-4cf0-9a-d1-3c-fa-5f-17-77-5c')
    @commethod(3)
    def Open(self, pszPnPDeviceID: Windows.Win32.Foundation.PWSTR, pClientInfo: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendCommand(self, dwFlags: UInt32, pParameters: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppResults: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Content(self, ppContent: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceContent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Capabilities(self, ppCapabilities: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceCapabilities_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Advise(self, dwFlags: UInt32, pCallback: Windows.Win32.Devices.PortableDevices.IPortableDeviceEventCallback_head, pParameters: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppszCookie: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Unadvise(self, pszCookie: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPnPDeviceID(self, ppszPnPDeviceID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceCapabilities(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2c8c6dbf-e3dc-4061-be-cc-85-42-e8-10-d1-26')
    @commethod(3)
    def GetSupportedCommands(self, ppCommands: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCommandOptions(self, Command: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppOptions: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFunctionalCategories(self, ppCategories: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFunctionalObjects(self, Category: POINTER(Guid), ppObjectIDs: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSupportedContentTypes(self, Category: POINTER(Guid), ppContentTypes: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSupportedFormats(self, ContentType: POINTER(Guid), ppFormats: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSupportedFormatProperties(self, Format: POINTER(Guid), ppKeys: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFixedPropertyAttributes(self, Format: POINTER(Guid), Key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppAttributes: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSupportedEvents(self, ppEvents: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEventOptions(self, Event: POINTER(Guid), ppOptions: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceConnector(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('625e2df8-6392-4cf0-9a-d1-3c-fa-5f-17-77-5c')
    @commethod(3)
    def Connect(self, pCallback: Windows.Win32.Devices.PortableDevices.IConnectionRequestCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect(self, pCallback: Windows.Win32.Devices.PortableDevices.IConnectionRequestCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Cancel(self, pCallback: Windows.Win32.Devices.PortableDevices.IConnectionRequestCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProperty(self, pPropertyKey: POINTER(Windows.Win32.Devices.Properties.DEVPROPKEY_head), pPropertyType: POINTER(Windows.Win32.Devices.Properties.DEVPROPTYPE), ppData: POINTER(POINTER(Byte)), pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetProperty(self, pPropertyKey: POINTER(Windows.Win32.Devices.Properties.DEVPROPKEY_head), PropertyType: Windows.Win32.Devices.Properties.DEVPROPTYPE, pData: POINTER(Byte), cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPnPID(self, ppwszPnPID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceContent(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6a96ed84-7c73-4480-99-38-bf-5a-f4-77-d4-26')
    @commethod(3)
    def EnumObjects(self, dwFlags: UInt32, pszParentObjectID: Windows.Win32.Foundation.PWSTR, pFilter: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppEnum: POINTER(Windows.Win32.Devices.PortableDevices.IEnumPortableDeviceObjectIDs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Properties(self, ppProperties: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Transfer(self, ppResources: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceResources_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateObjectWithPropertiesOnly(self, pValues: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppszObjectID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateObjectWithPropertiesAndData(self, pValues: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppData: POINTER(Windows.Win32.System.Com.IStream_head), pdwOptimalWriteBufferSize: POINTER(UInt32), ppszCookie: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Delete(self, dwOptions: UInt32, pObjectIDs: Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head, ppResults: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetObjectIDsFromPersistentUniqueIDs(self, pPersistentUniqueIDs: Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head, ppObjectIDs: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Move(self, pObjectIDs: Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head, pszDestinationFolderObjectID: Windows.Win32.Foundation.PWSTR, ppResults: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Copy(self, pObjectIDs: Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head, pszDestinationFolderObjectID: Windows.Win32.Foundation.PWSTR, ppResults: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceContent2(c_void_p):
    extends: Windows.Win32.Devices.PortableDevices.IPortableDeviceContent
    Guid = Guid('9b4add96-f6bf-4034-87-08-ec-a7-2b-f1-05-54')
    @commethod(13)
    def UpdateObjectWithPropertiesAndData(self, pszObjectID: Windows.Win32.Foundation.PWSTR, pProperties: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppData: POINTER(Windows.Win32.System.Com.IStream_head), pdwOptimalWriteBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceDataStream(c_void_p):
    extends: Windows.Win32.System.Com.IStream
    Guid = Guid('88e04db3-1012-4d64-99-96-f7-03-a9-50-d3-f4')
    @commethod(14)
    def GetObjectID(self, ppszObjectID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceDispatchFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5e1eafc3-e3d7-4132-96-fa-75-9c-0f-9d-1e-0f')
    @commethod(3)
    def GetDeviceDispatch(self, pszPnPDeviceID: Windows.Win32.Foundation.PWSTR, ppDeviceDispatch: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceEventCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a8792a31-f385-493c-a8-93-40-f6-4e-b4-5f-6e')
    @commethod(3)
    def OnEvent(self, pEventParameters: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceKeyCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dada2357-e0ad-492e-98-db-dd-61-c5-3b-a3-53')
    @commethod(3)
    def GetCount(self, pcElems: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, dwIndex: UInt32, pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, Key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(self, dwIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1567595-4c2f-4574-a6-fa-ec-ef-91-7b-9a-40')
    @commethod(3)
    def GetDevices(self, pPnPDeviceIDs: POINTER(Windows.Win32.Foundation.PWSTR), pcPnPDeviceIDs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RefreshDeviceList(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeviceFriendlyName(self, pszPnPDeviceID: Windows.Win32.Foundation.PWSTR, pDeviceFriendlyName: Windows.Win32.Foundation.PWSTR, pcchDeviceFriendlyName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDeviceDescription(self, pszPnPDeviceID: Windows.Win32.Foundation.PWSTR, pDeviceDescription: Windows.Win32.Foundation.PWSTR, pcchDeviceDescription: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeviceManufacturer(self, pszPnPDeviceID: Windows.Win32.Foundation.PWSTR, pDeviceManufacturer: Windows.Win32.Foundation.PWSTR, pcchDeviceManufacturer: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDeviceProperty(self, pszPnPDeviceID: Windows.Win32.Foundation.PWSTR, pszDevicePropertyName: Windows.Win32.Foundation.PWSTR, pData: POINTER(Byte), pcbData: POINTER(UInt32), pdwType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPrivateDevices(self, pPnPDeviceIDs: POINTER(Windows.Win32.Foundation.PWSTR), pcPnPDeviceIDs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDevicePropVariantCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('89b2e422-4f1b-4316-bc-ef-a4-4a-fe-a8-3e-b3')
    @commethod(3)
    def GetCount(self, pcElems: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, dwIndex: UInt32, pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetType(self, pvt: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ChangeType(self, vt: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveAt(self, dwIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceProperties(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7f6d695c-03df-4439-a8-09-59-26-6b-ee-e3-a6')
    @commethod(3)
    def GetSupportedProperties(self, pszObjectID: Windows.Win32.Foundation.PWSTR, ppKeys: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyAttributes(self, pszObjectID: Windows.Win32.Foundation.PWSTR, Key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppAttributes: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetValues(self, pszObjectID: Windows.Win32.Foundation.PWSTR, pKeys: Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head, ppValues: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetValues(self, pszObjectID: Windows.Win32.Foundation.PWSTR, pValues: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppResults: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Delete(self, pszObjectID: Windows.Win32.Foundation.PWSTR, pKeys: Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDevicePropertiesBulk(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('482b05c0-4056-44ed-9e-0f-5e-23-b0-09-da-93')
    @commethod(3)
    def QueueGetValuesByObjectList(self, pObjectIDs: Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head, pKeys: Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head, pCallback: Windows.Win32.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback_head, pContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueueGetValuesByObjectFormat(self, pguidObjectFormat: POINTER(Guid), pszParentObjectID: Windows.Win32.Foundation.PWSTR, dwDepth: UInt32, pKeys: Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head, pCallback: Windows.Win32.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback_head, pContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueueSetValuesByObjectList(self, pObjectValues: Windows.Win32.Devices.PortableDevices.IPortableDeviceValuesCollection_head, pCallback: Windows.Win32.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback_head, pContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Start(self, pContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Cancel(self, pContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDevicePropertiesBulkCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9deacb80-11e8-40e3-a9-f3-f5-57-98-6a-78-45')
    @commethod(3)
    def OnStart(self, pContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnProgress(self, pContext: POINTER(Guid), pResults: Windows.Win32.Devices.PortableDevices.IPortableDeviceValuesCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEnd(self, pContext: POINTER(Guid), hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceResources(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fd8878ac-d841-4d17-89-1c-e6-82-9c-db-69-34')
    @commethod(3)
    def GetSupportedResources(self, pszObjectID: Windows.Win32.Foundation.PWSTR, ppKeys: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResourceAttributes(self, pszObjectID: Windows.Win32.Foundation.PWSTR, Key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppResourceAttributes: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStream(self, pszObjectID: Windows.Win32.Foundation.PWSTR, Key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), dwMode: UInt32, pdwOptimalBufferSize: POINTER(UInt32), ppStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Delete(self, pszObjectID: Windows.Win32.Foundation.PWSTR, pKeys: Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateResource(self, pResourceAttributes: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppData: POINTER(Windows.Win32.System.Com.IStream_head), pdwOptimalWriteBufferSize: POINTER(UInt32), ppszCookie: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d3bd3a44-d7b5-40a9-98-b7-2f-a4-d0-1d-ec-08')
    @commethod(3)
    def Open(self, pszPnPServiceID: Windows.Win32.Foundation.PWSTR, pClientInfo: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Capabilities(self, ppCapabilities: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceServiceCapabilities_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Content(self, ppContent: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceContent2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Methods(self, ppMethods: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceServiceMethods_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetServiceObjectID(self, ppszServiceObjectID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPnPServiceID(self, ppszPnPServiceID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Advise(self, dwFlags: UInt32, pCallback: Windows.Win32.Devices.PortableDevices.IPortableDeviceEventCallback_head, pParameters: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppszCookie: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Unadvise(self, pszCookie: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SendCommand(self, dwFlags: UInt32, pParameters: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppResults: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceActivation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e56b0534-d9b9-425c-9b-99-75-f9-7c-b3-d7-c8')
    @commethod(3)
    def OpenAsync(self, pszPnPServiceID: Windows.Win32.Foundation.PWSTR, pClientInfo: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, pCallback: Windows.Win32.Devices.PortableDevices.IPortableDeviceServiceOpenCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelOpenAsync(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceCapabilities(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('24dbd89d-413e-43e0-bd-5b-19-7f-3c-56-c8-86')
    @commethod(3)
    def GetSupportedMethods(self, ppMethods: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSupportedMethodsByFormat(self, Format: POINTER(Guid), ppMethods: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMethodAttributes(self, Method: POINTER(Guid), ppAttributes: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMethodParameterAttributes(self, Method: POINTER(Guid), Parameter: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppAttributes: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSupportedFormats(self, ppFormats: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFormatAttributes(self, Format: POINTER(Guid), ppAttributes: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSupportedFormatProperties(self, Format: POINTER(Guid), ppKeys: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFormatPropertyAttributes(self, Format: POINTER(Guid), Property: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppAttributes: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSupportedEvents(self, ppEvents: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetEventAttributes(self, Event: POINTER(Guid), ppAttributes: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEventParameterAttributes(self, Event: POINTER(Guid), Parameter: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppAttributes: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetInheritedServices(self, dwInheritanceType: UInt32, ppServices: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetFormatRenderingProfiles(self, Format: POINTER(Guid), ppRenderingProfiles: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValuesCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSupportedCommands(self, ppCommands: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCommandOptions(self, Command: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppOptions: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a8abc4e9-a84a-47a9-80-b3-c5-d9-b1-72-a9-61')
    @commethod(3)
    def GetDeviceServices(self, pszPnPDeviceID: Windows.Win32.Foundation.PWSTR, guidServiceCategory: POINTER(Guid), pServices: POINTER(Windows.Win32.Foundation.PWSTR), pcServices: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceForService(self, pszPnPServiceID: Windows.Win32.Foundation.PWSTR, ppszPnPDeviceID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceMethodCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c424233c-afce-4828-a7-56-7e-d7-a2-35-00-83')
    @commethod(3)
    def OnComplete(self, hrStatus: Windows.Win32.Foundation.HRESULT, pResults: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceMethods(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e20333c9-fd34-412d-a3-81-cc-6f-2d-82-0d-f7')
    @commethod(3)
    def Invoke(self, Method: POINTER(Guid), pParameters: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppResults: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeAsync(self, Method: POINTER(Guid), pParameters: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, pCallback: Windows.Win32.Devices.PortableDevices.IPortableDeviceServiceMethodCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Cancel(self, pCallback: Windows.Win32.Devices.PortableDevices.IPortableDeviceServiceMethodCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceOpenCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bced49c8-8efe-41ed-96-0b-61-31-3a-bd-47-a9')
    @commethod(3)
    def OnComplete(self, hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceUnitsStream(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5e98025f-bfc4-47a2-9a-5f-bc-90-0a-50-7c-67')
    @commethod(3)
    def SeekInUnits(self, dlibMove: Int64, units: Windows.Win32.Devices.PortableDevices.WPD_STREAM_UNITS, dwOrigin: UInt32, plibNewPosition: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceValues(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6848f6f2-3155-4f86-b6-f5-26-3e-ee-ab-31-43')
    @commethod(3)
    def GetCount(self, pcelt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, index: UInt32, pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetStringValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Value: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStringValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetUnsignedIntegerValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Value: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetUnsignedIntegerValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetSignedIntegerValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Value: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSignedIntegerValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetUnsignedLargeIntegerValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Value: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetUnsignedLargeIntegerValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetSignedLargeIntegerValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Value: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSignedLargeIntegerValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetFloatValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Value: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetFloatValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetErrorValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Value: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetErrorValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetKeyValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Value: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetKeyValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetBoolValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Value: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetBoolValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetIUnknownValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetIUnknownValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppValue: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetGuidValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Value: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetGuidValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetBufferValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Byte), cbValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetBufferValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppValue: POINTER(POINTER(Byte)), pcbValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetIPortableDeviceValuesValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetIPortableDeviceValuesValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppValue: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetIPortableDevicePropVariantCollectionValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetIPortableDevicePropVariantCollectionValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppValue: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetIPortableDeviceKeyCollectionValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetIPortableDeviceKeyCollectionValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppValue: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetIPortableDeviceValuesCollectionValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: Windows.Win32.Devices.PortableDevices.IPortableDeviceValuesCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetIPortableDeviceValuesCollectionValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppValue: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValuesCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def RemoveValue(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def CopyValuesFromPropertyStore(self, pStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def CopyValuesToPropertyStore(self, pStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceValuesCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6e3f2d79-4e07-48c4-82-08-d8-c2-e5-af-4a-99')
    @commethod(3)
    def GetCount(self, pcElems: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, dwIndex: UInt32, ppValues: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pValues: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(self, dwIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceWebControl(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('94fc7953-5ca1-483a-8a-ee-df-52-e7-74-7d-00')
    @commethod(7)
    def GetDeviceFromId(self, deviceId: Windows.Win32.Foundation.BSTR, ppDevice: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDeviceFromIdAsync(self, deviceId: Windows.Win32.Foundation.BSTR, pCompletionHandler: Windows.Win32.System.Com.IDispatch_head, pErrorHandler: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
class IRadioInstance(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('70aa1c9e-f2b4-4c61-86-d3-6b-9f-b7-5f-d1-a2')
    @commethod(3)
    def GetRadioManagerSignature(self, pguidSignature: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInstanceSignature(self, pbstrId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFriendlyName(self, lcid: UInt32, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRadioState(self, pRadioState: POINTER(Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetRadioState(self, radioState: Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE, uTimeoutSec: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsMultiComm(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(9)
    def IsAssociatingDevice(self) -> Windows.Win32.Foundation.BOOL: ...
class IRadioInstanceCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e5791fae-5665-4e0c-95-be-5f-de-31-64-41-85')
    @commethod(3)
    def GetCount(self, pcInstance: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, uIndex: UInt32, ppRadioInstance: POINTER(Windows.Win32.Devices.PortableDevices.IRadioInstance_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWpdSerializer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b32f4002-bb27-45ff-af-4f-06-63-1c-1e-8d-ad')
    @commethod(3)
    def GetIPortableDeviceValuesFromBuffer(self, pBuffer: POINTER(Byte), dwInputBufferLength: UInt32, ppParams: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteIPortableDeviceValuesToBuffer(self, dwOutputBufferLength: UInt32, pResults: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, pBuffer: POINTER(Byte), pdwBytesWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBufferFromIPortableDeviceValues(self, pSource: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppBuffer: POINTER(POINTER(Byte)), pdwBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSerializedSize(self, pSource: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
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
SMS_TEXT_MESSAGE: SMS_MESSAGE_TYPES = 0
SMS_BINARY_MESSAGE: SMS_MESSAGE_TYPES = 1
SYSTEM_RADIO_STATE = Int32
SRS_RADIO_ENABLED: SYSTEM_RADIO_STATE = 0
SRS_RADIO_DISABLED: SYSTEM_RADIO_STATE = 1
WPD_BITRATE_TYPES = Int32
WPD_BITRATE_TYPE_UNUSED: WPD_BITRATE_TYPES = 0
WPD_BITRATE_TYPE_DISCRETE: WPD_BITRATE_TYPES = 1
WPD_BITRATE_TYPE_VARIABLE: WPD_BITRATE_TYPES = 2
WPD_BITRATE_TYPE_FREE: WPD_BITRATE_TYPES = 3
WPD_CAPTURE_MODES = Int32
WPD_CAPTURE_MODE_UNDEFINED: WPD_CAPTURE_MODES = 0
WPD_CAPTURE_MODE_NORMAL: WPD_CAPTURE_MODES = 1
WPD_CAPTURE_MODE_BURST: WPD_CAPTURE_MODES = 2
WPD_CAPTURE_MODE_TIMELAPSE: WPD_CAPTURE_MODES = 3
WPD_COLOR_CORRECTED_STATUS_VALUES = Int32
WPD_COLOR_CORRECTED_STATUS_NOT_CORRECTED: WPD_COLOR_CORRECTED_STATUS_VALUES = 0
WPD_COLOR_CORRECTED_STATUS_CORRECTED: WPD_COLOR_CORRECTED_STATUS_VALUES = 1
WPD_COLOR_CORRECTED_STATUS_SHOULD_NOT_BE_CORRECTED: WPD_COLOR_CORRECTED_STATUS_VALUES = 2
class WPD_COMMAND_ACCESS_LOOKUP_ENTRY(EasyCastStructure):
    Command: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY
    AccessType: UInt32
    AccessProperty: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY
WPD_COMMAND_ACCESS_TYPES = Int32
WPD_COMMAND_ACCESS_READ: WPD_COMMAND_ACCESS_TYPES = 1
WPD_COMMAND_ACCESS_READWRITE: WPD_COMMAND_ACCESS_TYPES = 3
WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_STGM_ACCESS: WPD_COMMAND_ACCESS_TYPES = 4
WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_FILE_ACCESS: WPD_COMMAND_ACCESS_TYPES = 8
WPD_COMMAND_ACCESS_FROM_ATTRIBUTE_WITH_METHOD_ACCESS: WPD_COMMAND_ACCESS_TYPES = 16
WPD_CROPPED_STATUS_VALUES = Int32
WPD_CROPPED_STATUS_NOT_CROPPED: WPD_CROPPED_STATUS_VALUES = 0
WPD_CROPPED_STATUS_CROPPED: WPD_CROPPED_STATUS_VALUES = 1
WPD_CROPPED_STATUS_SHOULD_NOT_BE_CROPPED: WPD_CROPPED_STATUS_VALUES = 2
WPD_DEVICE_TRANSPORTS = Int32
WPD_DEVICE_TRANSPORT_UNSPECIFIED: WPD_DEVICE_TRANSPORTS = 0
WPD_DEVICE_TRANSPORT_USB: WPD_DEVICE_TRANSPORTS = 1
WPD_DEVICE_TRANSPORT_IP: WPD_DEVICE_TRANSPORTS = 2
WPD_DEVICE_TRANSPORT_BLUETOOTH: WPD_DEVICE_TRANSPORTS = 3
WPD_DEVICE_TYPES = Int32
WPD_DEVICE_TYPE_GENERIC: WPD_DEVICE_TYPES = 0
WPD_DEVICE_TYPE_CAMERA: WPD_DEVICE_TYPES = 1
WPD_DEVICE_TYPE_MEDIA_PLAYER: WPD_DEVICE_TYPES = 2
WPD_DEVICE_TYPE_PHONE: WPD_DEVICE_TYPES = 3
WPD_DEVICE_TYPE_VIDEO: WPD_DEVICE_TYPES = 4
WPD_DEVICE_TYPE_PERSONAL_INFORMATION_MANAGER: WPD_DEVICE_TYPES = 5
WPD_DEVICE_TYPE_AUDIO_RECORDER: WPD_DEVICE_TYPES = 6
WPD_EFFECT_MODES = Int32
WPD_EFFECT_MODE_UNDEFINED: WPD_EFFECT_MODES = 0
WPD_EFFECT_MODE_COLOR: WPD_EFFECT_MODES = 1
WPD_EFFECT_MODE_BLACK_AND_WHITE: WPD_EFFECT_MODES = 2
WPD_EFFECT_MODE_SEPIA: WPD_EFFECT_MODES = 3
WPD_EXPOSURE_METERING_MODES = Int32
WPD_EXPOSURE_METERING_MODE_UNDEFINED: WPD_EXPOSURE_METERING_MODES = 0
WPD_EXPOSURE_METERING_MODE_AVERAGE: WPD_EXPOSURE_METERING_MODES = 1
WPD_EXPOSURE_METERING_MODE_CENTER_WEIGHTED_AVERAGE: WPD_EXPOSURE_METERING_MODES = 2
WPD_EXPOSURE_METERING_MODE_MULTI_SPOT: WPD_EXPOSURE_METERING_MODES = 3
WPD_EXPOSURE_METERING_MODE_CENTER_SPOT: WPD_EXPOSURE_METERING_MODES = 4
WPD_EXPOSURE_PROGRAM_MODES = Int32
WPD_EXPOSURE_PROGRAM_MODE_UNDEFINED: WPD_EXPOSURE_PROGRAM_MODES = 0
WPD_EXPOSURE_PROGRAM_MODE_MANUAL: WPD_EXPOSURE_PROGRAM_MODES = 1
WPD_EXPOSURE_PROGRAM_MODE_AUTO: WPD_EXPOSURE_PROGRAM_MODES = 2
WPD_EXPOSURE_PROGRAM_MODE_APERTURE_PRIORITY: WPD_EXPOSURE_PROGRAM_MODES = 3
WPD_EXPOSURE_PROGRAM_MODE_SHUTTER_PRIORITY: WPD_EXPOSURE_PROGRAM_MODES = 4
WPD_EXPOSURE_PROGRAM_MODE_CREATIVE: WPD_EXPOSURE_PROGRAM_MODES = 5
WPD_EXPOSURE_PROGRAM_MODE_ACTION: WPD_EXPOSURE_PROGRAM_MODES = 6
WPD_EXPOSURE_PROGRAM_MODE_PORTRAIT: WPD_EXPOSURE_PROGRAM_MODES = 7
WPD_FLASH_MODES = Int32
WPD_FLASH_MODE_UNDEFINED: WPD_FLASH_MODES = 0
WPD_FLASH_MODE_AUTO: WPD_FLASH_MODES = 1
WPD_FLASH_MODE_OFF: WPD_FLASH_MODES = 2
WPD_FLASH_MODE_FILL: WPD_FLASH_MODES = 3
WPD_FLASH_MODE_RED_EYE_AUTO: WPD_FLASH_MODES = 4
WPD_FLASH_MODE_RED_EYE_FILL: WPD_FLASH_MODES = 5
WPD_FLASH_MODE_EXTERNAL_SYNC: WPD_FLASH_MODES = 6
WPD_FOCUS_METERING_MODES = Int32
WPD_FOCUS_METERING_MODE_UNDEFINED: WPD_FOCUS_METERING_MODES = 0
WPD_FOCUS_METERING_MODE_CENTER_SPOT: WPD_FOCUS_METERING_MODES = 1
WPD_FOCUS_METERING_MODE_MULTI_SPOT: WPD_FOCUS_METERING_MODES = 2
WPD_FOCUS_MODES = Int32
WPD_FOCUS_UNDEFINED: WPD_FOCUS_MODES = 0
WPD_FOCUS_MANUAL: WPD_FOCUS_MODES = 1
WPD_FOCUS_AUTOMATIC: WPD_FOCUS_MODES = 2
WPD_FOCUS_AUTOMATIC_MACRO: WPD_FOCUS_MODES = 3
WPD_META_GENRES = Int32
WPD_META_GENRE_UNUSED: WPD_META_GENRES = 0
WPD_META_GENRE_GENERIC_MUSIC_AUDIO_FILE: WPD_META_GENRES = 1
WPD_META_GENRE_GENERIC_NON_MUSIC_AUDIO_FILE: WPD_META_GENRES = 17
WPD_META_GENRE_SPOKEN_WORD_AUDIO_BOOK_FILES: WPD_META_GENRES = 18
WPD_META_GENRE_SPOKEN_WORD_FILES_NON_AUDIO_BOOK: WPD_META_GENRES = 19
WPD_META_GENRE_SPOKEN_WORD_NEWS: WPD_META_GENRES = 20
WPD_META_GENRE_SPOKEN_WORD_TALK_SHOWS: WPD_META_GENRES = 21
WPD_META_GENRE_GENERIC_VIDEO_FILE: WPD_META_GENRES = 33
WPD_META_GENRE_NEWS_VIDEO_FILE: WPD_META_GENRES = 34
WPD_META_GENRE_MUSIC_VIDEO_FILE: WPD_META_GENRES = 35
WPD_META_GENRE_HOME_VIDEO_FILE: WPD_META_GENRES = 36
WPD_META_GENRE_FEATURE_FILM_VIDEO_FILE: WPD_META_GENRES = 37
WPD_META_GENRE_TELEVISION_VIDEO_FILE: WPD_META_GENRES = 38
WPD_META_GENRE_TRAINING_EDUCATIONAL_VIDEO_FILE: WPD_META_GENRES = 39
WPD_META_GENRE_PHOTO_MONTAGE_VIDEO_FILE: WPD_META_GENRES = 40
WPD_META_GENRE_GENERIC_NON_AUDIO_NON_VIDEO: WPD_META_GENRES = 48
WPD_META_GENRE_AUDIO_PODCAST: WPD_META_GENRES = 64
WPD_META_GENRE_VIDEO_PODCAST: WPD_META_GENRES = 65
WPD_META_GENRE_MIXED_PODCAST: WPD_META_GENRES = 66
WPD_OPERATION_STATES = Int32
WPD_OPERATION_STATE_UNSPECIFIED: WPD_OPERATION_STATES = 0
WPD_OPERATION_STATE_STARTED: WPD_OPERATION_STATES = 1
WPD_OPERATION_STATE_RUNNING: WPD_OPERATION_STATES = 2
WPD_OPERATION_STATE_PAUSED: WPD_OPERATION_STATES = 3
WPD_OPERATION_STATE_CANCELLED: WPD_OPERATION_STATES = 4
WPD_OPERATION_STATE_FINISHED: WPD_OPERATION_STATES = 5
WPD_OPERATION_STATE_ABORTED: WPD_OPERATION_STATES = 6
WPD_PARAMETER_USAGE_TYPES = Int32
WPD_PARAMETER_USAGE_RETURN: WPD_PARAMETER_USAGE_TYPES = 0
WPD_PARAMETER_USAGE_IN: WPD_PARAMETER_USAGE_TYPES = 1
WPD_PARAMETER_USAGE_OUT: WPD_PARAMETER_USAGE_TYPES = 2
WPD_PARAMETER_USAGE_INOUT: WPD_PARAMETER_USAGE_TYPES = 3
WPD_POWER_SOURCES = Int32
WPD_POWER_SOURCE_BATTERY: WPD_POWER_SOURCES = 0
WPD_POWER_SOURCE_EXTERNAL: WPD_POWER_SOURCES = 1
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES = Int32
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_OBJECT: WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES = 0
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_RESOURCE: WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES = 1
WPD_SECTION_DATA_UNITS_VALUES = Int32
WPD_SECTION_DATA_UNITS_BYTES: WPD_SECTION_DATA_UNITS_VALUES = 0
WPD_SECTION_DATA_UNITS_MILLISECONDS: WPD_SECTION_DATA_UNITS_VALUES = 1
WPD_SERVICE_INHERITANCE_TYPES = Int32
WPD_SERVICE_INHERITANCE_IMPLEMENTATION: WPD_SERVICE_INHERITANCE_TYPES = 0
WPD_SMS_ENCODING_TYPES = Int32
SMS_ENCODING_7_BIT: WPD_SMS_ENCODING_TYPES = 0
SMS_ENCODING_8_BIT: WPD_SMS_ENCODING_TYPES = 1
SMS_ENCODING_UTF_16: WPD_SMS_ENCODING_TYPES = 2
WPD_STORAGE_ACCESS_CAPABILITY_VALUES = Int32
WPD_STORAGE_ACCESS_CAPABILITY_READWRITE: WPD_STORAGE_ACCESS_CAPABILITY_VALUES = 0
WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITHOUT_OBJECT_DELETION: WPD_STORAGE_ACCESS_CAPABILITY_VALUES = 1
WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITH_OBJECT_DELETION: WPD_STORAGE_ACCESS_CAPABILITY_VALUES = 2
WPD_STORAGE_TYPE_VALUES = Int32
WPD_STORAGE_TYPE_UNDEFINED: WPD_STORAGE_TYPE_VALUES = 0
WPD_STORAGE_TYPE_FIXED_ROM: WPD_STORAGE_TYPE_VALUES = 1
WPD_STORAGE_TYPE_REMOVABLE_ROM: WPD_STORAGE_TYPE_VALUES = 2
WPD_STORAGE_TYPE_FIXED_RAM: WPD_STORAGE_TYPE_VALUES = 3
WPD_STORAGE_TYPE_REMOVABLE_RAM: WPD_STORAGE_TYPE_VALUES = 4
WPD_STREAM_UNITS = Int32
WPD_STREAM_UNITS_BYTES: WPD_STREAM_UNITS = 0
WPD_STREAM_UNITS_FRAMES: WPD_STREAM_UNITS = 1
WPD_STREAM_UNITS_ROWS: WPD_STREAM_UNITS = 2
WPD_STREAM_UNITS_MILLISECONDS: WPD_STREAM_UNITS = 4
WPD_STREAM_UNITS_MICROSECONDS: WPD_STREAM_UNITS = 8
WPD_VIDEO_SCAN_TYPES = Int32
WPD_VIDEO_SCAN_TYPE_UNUSED: WPD_VIDEO_SCAN_TYPES = 0
WPD_VIDEO_SCAN_TYPE_PROGRESSIVE: WPD_VIDEO_SCAN_TYPES = 1
WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_UPPER_FIRST: WPD_VIDEO_SCAN_TYPES = 2
WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_LOWER_FIRST: WPD_VIDEO_SCAN_TYPES = 3
WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_UPPER_FIRST: WPD_VIDEO_SCAN_TYPES = 4
WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_LOWER_FIRST: WPD_VIDEO_SCAN_TYPES = 5
WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE: WPD_VIDEO_SCAN_TYPES = 6
WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE_AND_PROGRESSIVE: WPD_VIDEO_SCAN_TYPES = 7
WPD_WHITE_BALANCE_SETTINGS = Int32
WPD_WHITE_BALANCE_UNDEFINED: WPD_WHITE_BALANCE_SETTINGS = 0
WPD_WHITE_BALANCE_MANUAL: WPD_WHITE_BALANCE_SETTINGS = 1
WPD_WHITE_BALANCE_AUTOMATIC: WPD_WHITE_BALANCE_SETTINGS = 2
WPD_WHITE_BALANCE_ONE_PUSH_AUTOMATIC: WPD_WHITE_BALANCE_SETTINGS = 3
WPD_WHITE_BALANCE_DAYLIGHT: WPD_WHITE_BALANCE_SETTINGS = 4
WPD_WHITE_BALANCE_FLORESCENT: WPD_WHITE_BALANCE_SETTINGS = 5
WPD_WHITE_BALANCE_TUNGSTEN: WPD_WHITE_BALANCE_SETTINGS = 6
WPD_WHITE_BALANCE_FLASH: WPD_WHITE_BALANCE_SETTINGS = 7
WpdAttributeForm = Int32
WPD_PROPERTY_ATTRIBUTE_FORM_UNSPECIFIED: WpdAttributeForm = 0
WPD_PROPERTY_ATTRIBUTE_FORM_RANGE: WpdAttributeForm = 1
WPD_PROPERTY_ATTRIBUTE_FORM_ENUMERATION: WpdAttributeForm = 2
WPD_PROPERTY_ATTRIBUTE_FORM_REGULAR_EXPRESSION: WpdAttributeForm = 3
WPD_PROPERTY_ATTRIBUTE_FORM_OBJECT_IDENTIFIER: WpdAttributeForm = 4
WpdParameterAttributeForm = Int32
WPD_PARAMETER_ATTRIBUTE_FORM_UNSPECIFIED: WpdParameterAttributeForm = 0
WPD_PARAMETER_ATTRIBUTE_FORM_RANGE: WpdParameterAttributeForm = 1
WPD_PARAMETER_ATTRIBUTE_FORM_ENUMERATION: WpdParameterAttributeForm = 2
WPD_PARAMETER_ATTRIBUTE_FORM_REGULAR_EXPRESSION: WpdParameterAttributeForm = 3
WPD_PARAMETER_ATTRIBUTE_FORM_OBJECT_IDENTIFIER: WpdParameterAttributeForm = 4
WpdSerializer = Guid('0b91a74b-ad7c-4a9d-b5-63-29-ee-f9-16-71-72')
make_head(_module, 'DEVPKEY_MTPBTH_IsConnected')
make_head(_module, 'WPD_PROPERTY_NULL')
make_head(_module, 'WPD_OBJECT_CONTENT_TYPE')
make_head(_module, 'WPD_OBJECT_REFERENCES')
make_head(_module, 'WPD_OBJECT_CONTAINER_FUNCTIONAL_OBJECT_ID')
make_head(_module, 'WPD_OBJECT_GENERATE_THUMBNAIL_FROM_RESOURCE')
make_head(_module, 'WPD_OBJECT_HINT_LOCATION_DISPLAY_NAME')
make_head(_module, 'WPD_OBJECT_SUPPORTED_UNITS')
make_head(_module, 'WPD_FUNCTIONAL_OBJECT_CATEGORY')
make_head(_module, 'WPD_STORAGE_TYPE')
make_head(_module, 'WPD_STORAGE_FILE_SYSTEM_TYPE')
make_head(_module, 'WPD_STORAGE_CAPACITY')
make_head(_module, 'WPD_STORAGE_FREE_SPACE_IN_BYTES')
make_head(_module, 'WPD_STORAGE_FREE_SPACE_IN_OBJECTS')
make_head(_module, 'WPD_STORAGE_DESCRIPTION')
make_head(_module, 'WPD_STORAGE_SERIAL_NUMBER')
make_head(_module, 'WPD_STORAGE_MAX_OBJECT_SIZE')
make_head(_module, 'WPD_STORAGE_CAPACITY_IN_OBJECTS')
make_head(_module, 'WPD_STORAGE_ACCESS_CAPABILITY')
make_head(_module, 'WPD_NETWORK_ASSOCIATION_HOST_NETWORK_IDENTIFIERS')
make_head(_module, 'WPD_NETWORK_ASSOCIATION_X509V3SEQUENCE')
make_head(_module, 'WPD_STILL_IMAGE_CAPTURE_RESOLUTION')
make_head(_module, 'WPD_STILL_IMAGE_CAPTURE_FORMAT')
make_head(_module, 'WPD_STILL_IMAGE_COMPRESSION_SETTING')
make_head(_module, 'WPD_STILL_IMAGE_WHITE_BALANCE')
make_head(_module, 'WPD_STILL_IMAGE_RGB_GAIN')
make_head(_module, 'WPD_STILL_IMAGE_FNUMBER')
make_head(_module, 'WPD_STILL_IMAGE_FOCAL_LENGTH')
make_head(_module, 'WPD_STILL_IMAGE_FOCUS_DISTANCE')
make_head(_module, 'WPD_STILL_IMAGE_FOCUS_MODE')
make_head(_module, 'WPD_STILL_IMAGE_EXPOSURE_METERING_MODE')
make_head(_module, 'WPD_STILL_IMAGE_FLASH_MODE')
make_head(_module, 'WPD_STILL_IMAGE_EXPOSURE_TIME')
make_head(_module, 'WPD_STILL_IMAGE_EXPOSURE_PROGRAM_MODE')
make_head(_module, 'WPD_STILL_IMAGE_EXPOSURE_INDEX')
make_head(_module, 'WPD_STILL_IMAGE_EXPOSURE_BIAS_COMPENSATION')
make_head(_module, 'WPD_STILL_IMAGE_CAPTURE_DELAY')
make_head(_module, 'WPD_STILL_IMAGE_CAPTURE_MODE')
make_head(_module, 'WPD_STILL_IMAGE_CONTRAST')
make_head(_module, 'WPD_STILL_IMAGE_SHARPNESS')
make_head(_module, 'WPD_STILL_IMAGE_DIGITAL_ZOOM')
make_head(_module, 'WPD_STILL_IMAGE_EFFECT_MODE')
make_head(_module, 'WPD_STILL_IMAGE_BURST_NUMBER')
make_head(_module, 'WPD_STILL_IMAGE_BURST_INTERVAL')
make_head(_module, 'WPD_STILL_IMAGE_TIMELAPSE_NUMBER')
make_head(_module, 'WPD_STILL_IMAGE_TIMELAPSE_INTERVAL')
make_head(_module, 'WPD_STILL_IMAGE_FOCUS_METERING_MODE')
make_head(_module, 'WPD_STILL_IMAGE_UPLOAD_URL')
make_head(_module, 'WPD_STILL_IMAGE_ARTIST')
make_head(_module, 'WPD_STILL_IMAGE_CAMERA_MODEL')
make_head(_module, 'WPD_STILL_IMAGE_CAMERA_MANUFACTURER')
make_head(_module, 'WPD_RENDERING_INFORMATION_PROFILES')
make_head(_module, 'WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE')
make_head(_module, 'WPD_RENDERING_INFORMATION_PROFILE_ENTRY_CREATABLE_RESOURCES')
make_head(_module, 'WPD_CLIENT_NAME')
make_head(_module, 'WPD_CLIENT_MAJOR_VERSION')
make_head(_module, 'WPD_CLIENT_MINOR_VERSION')
make_head(_module, 'WPD_CLIENT_REVISION')
make_head(_module, 'WPD_CLIENT_WMDRM_APPLICATION_PRIVATE_KEY')
make_head(_module, 'WPD_CLIENT_WMDRM_APPLICATION_CERTIFICATE')
make_head(_module, 'WPD_CLIENT_SECURITY_QUALITY_OF_SERVICE')
make_head(_module, 'WPD_CLIENT_DESIRED_ACCESS')
make_head(_module, 'WPD_CLIENT_SHARE_MODE')
make_head(_module, 'WPD_CLIENT_EVENT_COOKIE')
make_head(_module, 'WPD_CLIENT_MINIMUM_RESULTS_BUFFER_SIZE')
make_head(_module, 'WPD_CLIENT_MANUAL_CLOSE_ON_DISCONNECT')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_FORM')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_CAN_READ')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_CAN_WRITE')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_CAN_DELETE')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_DEFAULT_VALUE')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_FAST_PROPERTY')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_RANGE_MIN')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_RANGE_MAX')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_RANGE_STEP')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_ENUMERATION_ELEMENTS')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_REGULAR_EXPRESSION')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_MAX_SIZE')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_NAME')
make_head(_module, 'WPD_PROPERTY_ATTRIBUTE_VARTYPE')
make_head(_module, 'WPD_CLASS_EXTENSION_OPTIONS_SUPPORTED_CONTENT_TYPES')
make_head(_module, 'WPD_CLASS_EXTENSION_OPTIONS_DONT_REGISTER_WPD_DEVICE_INTERFACE')
make_head(_module, 'WPD_CLASS_EXTENSION_OPTIONS_REGISTER_WPD_PRIVATE_DEVICE_INTERFACE')
make_head(_module, 'WPD_CLASS_EXTENSION_OPTIONS_MULTITRANSPORT_MODE')
make_head(_module, 'WPD_CLASS_EXTENSION_OPTIONS_DEVICE_IDENTIFICATION_VALUES')
make_head(_module, 'WPD_CLASS_EXTENSION_OPTIONS_TRANSPORT_BANDWIDTH')
make_head(_module, 'WPD_CLASS_EXTENSION_OPTIONS_SILENCE_AUTOPLAY')
make_head(_module, 'WPD_RESOURCE_ATTRIBUTE_TOTAL_SIZE')
make_head(_module, 'WPD_RESOURCE_ATTRIBUTE_CAN_READ')
make_head(_module, 'WPD_RESOURCE_ATTRIBUTE_CAN_WRITE')
make_head(_module, 'WPD_RESOURCE_ATTRIBUTE_CAN_DELETE')
make_head(_module, 'WPD_RESOURCE_ATTRIBUTE_OPTIMAL_READ_BUFFER_SIZE')
make_head(_module, 'WPD_RESOURCE_ATTRIBUTE_OPTIMAL_WRITE_BUFFER_SIZE')
make_head(_module, 'WPD_RESOURCE_ATTRIBUTE_FORMAT')
make_head(_module, 'WPD_RESOURCE_ATTRIBUTE_RESOURCE_KEY')
make_head(_module, 'WPD_DEVICE_SYNC_PARTNER')
make_head(_module, 'WPD_DEVICE_FIRMWARE_VERSION')
make_head(_module, 'WPD_DEVICE_POWER_LEVEL')
make_head(_module, 'WPD_DEVICE_POWER_SOURCE')
make_head(_module, 'WPD_DEVICE_PROTOCOL')
make_head(_module, 'WPD_DEVICE_MANUFACTURER')
make_head(_module, 'WPD_DEVICE_MODEL')
make_head(_module, 'WPD_DEVICE_SERIAL_NUMBER')
make_head(_module, 'WPD_DEVICE_SUPPORTS_NON_CONSUMABLE')
make_head(_module, 'WPD_DEVICE_DATETIME')
make_head(_module, 'WPD_DEVICE_FRIENDLY_NAME')
make_head(_module, 'WPD_DEVICE_SUPPORTED_DRM_SCHEMES')
make_head(_module, 'WPD_DEVICE_SUPPORTED_FORMATS_ARE_ORDERED')
make_head(_module, 'WPD_DEVICE_TYPE')
make_head(_module, 'WPD_DEVICE_NETWORK_IDENTIFIER')
make_head(_module, 'WPD_DEVICE_FUNCTIONAL_UNIQUE_ID')
make_head(_module, 'WPD_DEVICE_MODEL_UNIQUE_ID')
make_head(_module, 'WPD_DEVICE_TRANSPORT')
make_head(_module, 'WPD_DEVICE_USE_DEVICE_STAGE')
make_head(_module, 'WPD_DEVICE_EDP_IDENTITY')
make_head(_module, 'WPD_SERVICE_VERSION')
make_head(_module, 'WPD_EVENT_PARAMETER_PNP_DEVICE_ID')
make_head(_module, 'WPD_EVENT_PARAMETER_EVENT_ID')
make_head(_module, 'WPD_EVENT_PARAMETER_OPERATION_STATE')
make_head(_module, 'WPD_EVENT_PARAMETER_OPERATION_PROGRESS')
make_head(_module, 'WPD_EVENT_PARAMETER_OBJECT_PARENT_PERSISTENT_UNIQUE_ID')
make_head(_module, 'WPD_EVENT_PARAMETER_OBJECT_CREATION_COOKIE')
make_head(_module, 'WPD_EVENT_PARAMETER_CHILD_HIERARCHY_CHANGED')
make_head(_module, 'WPD_EVENT_PARAMETER_SERVICE_METHOD_CONTEXT')
make_head(_module, 'WPD_EVENT_OPTION_IS_BROADCAST_EVENT')
make_head(_module, 'WPD_EVENT_OPTION_IS_AUTOPLAY_EVENT')
make_head(_module, 'WPD_EVENT_ATTRIBUTE_NAME')
make_head(_module, 'WPD_EVENT_ATTRIBUTE_PARAMETERS')
make_head(_module, 'WPD_EVENT_ATTRIBUTE_OPTIONS')
make_head(_module, 'WPD_API_OPTION_USE_CLEAR_DATA_STREAM')
make_head(_module, 'WPD_API_OPTION_IOCTL_ACCESS')
make_head(_module, 'WPD_FORMAT_ATTRIBUTE_NAME')
make_head(_module, 'WPD_FORMAT_ATTRIBUTE_MIMETYPE')
make_head(_module, 'WPD_METHOD_ATTRIBUTE_NAME')
make_head(_module, 'WPD_METHOD_ATTRIBUTE_ASSOCIATED_FORMAT')
make_head(_module, 'WPD_METHOD_ATTRIBUTE_ACCESS')
make_head(_module, 'WPD_METHOD_ATTRIBUTE_PARAMETERS')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_ORDER')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_USAGE')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_FORM')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_DEFAULT_VALUE')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_RANGE_MIN')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_RANGE_MAX')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_RANGE_STEP')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_ENUMERATION_ELEMENTS')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_REGULAR_EXPRESSION')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_MAX_SIZE')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_VARTYPE')
make_head(_module, 'WPD_PARAMETER_ATTRIBUTE_NAME')
make_head(_module, 'WPD_COMMAND_COMMON_RESET_DEVICE')
make_head(_module, 'WPD_COMMAND_COMMON_GET_OBJECT_IDS_FROM_PERSISTENT_UNIQUE_IDS')
make_head(_module, 'WPD_COMMAND_COMMON_SAVE_CLIENT_INFORMATION')
make_head(_module, 'WPD_PROPERTY_COMMON_COMMAND_CATEGORY')
make_head(_module, 'WPD_PROPERTY_COMMON_COMMAND_ID')
make_head(_module, 'WPD_PROPERTY_COMMON_HRESULT')
make_head(_module, 'WPD_PROPERTY_COMMON_DRIVER_ERROR_CODE')
make_head(_module, 'WPD_PROPERTY_COMMON_COMMAND_TARGET')
make_head(_module, 'WPD_PROPERTY_COMMON_PERSISTENT_UNIQUE_IDS')
make_head(_module, 'WPD_PROPERTY_COMMON_OBJECT_IDS')
make_head(_module, 'WPD_PROPERTY_COMMON_CLIENT_INFORMATION')
make_head(_module, 'WPD_PROPERTY_COMMON_CLIENT_INFORMATION_CONTEXT')
make_head(_module, 'WPD_PROPERTY_COMMON_ACTIVITY_ID')
make_head(_module, 'WPD_OPTION_VALID_OBJECT_IDS')
make_head(_module, 'WPD_COMMAND_OBJECT_ENUMERATION_START_FIND')
make_head(_module, 'WPD_COMMAND_OBJECT_ENUMERATION_FIND_NEXT')
make_head(_module, 'WPD_COMMAND_OBJECT_ENUMERATION_END_FIND')
make_head(_module, 'WPD_PROPERTY_OBJECT_ENUMERATION_PARENT_ID')
make_head(_module, 'WPD_PROPERTY_OBJECT_ENUMERATION_FILTER')
make_head(_module, 'WPD_PROPERTY_OBJECT_ENUMERATION_OBJECT_IDS')
make_head(_module, 'WPD_PROPERTY_OBJECT_ENUMERATION_CONTEXT')
make_head(_module, 'WPD_PROPERTY_OBJECT_ENUMERATION_NUM_OBJECTS_REQUESTED')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_GET')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_SET')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_DELETE')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_DELETE_RESULTS')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_START')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_NEXT')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_END')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_START')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_NEXT')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_END')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_START')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_NEXT')
make_head(_module, 'WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_END')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_IDS')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_BULK_VALUES')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PROPERTY_KEYS')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_BULK_DEPTH')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PARENT_OBJECT_ID')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_FORMAT')
make_head(_module, 'WPD_PROPERTY_OBJECT_PROPERTIES_BULK_WRITE_RESULTS')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_GET_SUPPORTED')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_GET_ATTRIBUTES')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_OPEN')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_READ')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_WRITE')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_CLOSE')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_DELETE')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_CREATE_RESOURCE')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_REVERT')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_SEEK')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_COMMIT')
make_head(_module, 'WPD_COMMAND_OBJECT_RESOURCES_SEEK_IN_UNITS')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_ATTRIBUTES')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_READ')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_READ')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_WRITE')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_WRITTEN')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_DATA')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_SEEK_OFFSET')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_SUPPORTS_UNITS')
make_head(_module, 'WPD_PROPERTY_OBJECT_RESOURCES_STREAM_UNITS')
make_head(_module, 'WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_READ_SUPPORTED')
make_head(_module, 'WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_WRITE_SUPPORTED')
make_head(_module, 'WPD_OPTION_OBJECT_RESOURCES_NO_INPUT_BUFFER_ON_READ')
make_head(_module, 'WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_ONLY')
make_head(_module, 'WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_AND_DATA')
make_head(_module, 'WPD_COMMAND_OBJECT_MANAGEMENT_WRITE_OBJECT_DATA')
make_head(_module, 'WPD_COMMAND_OBJECT_MANAGEMENT_COMMIT_OBJECT')
make_head(_module, 'WPD_COMMAND_OBJECT_MANAGEMENT_REVERT_OBJECT')
make_head(_module, 'WPD_COMMAND_OBJECT_MANAGEMENT_DELETE_OBJECTS')
make_head(_module, 'WPD_COMMAND_OBJECT_MANAGEMENT_MOVE_OBJECTS')
make_head(_module, 'WPD_COMMAND_OBJECT_MANAGEMENT_COPY_OBJECTS')
make_head(_module, 'WPD_COMMAND_OBJECT_MANAGEMENT_UPDATE_OBJECT_WITH_PROPERTIES_AND_DATA')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_CREATION_PROPERTIES')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_TO_WRITE')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_WRITTEN')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_DATA')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_ID')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_OPTIONS')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_OPTIMAL_TRANSFER_BUFFER_SIZE')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_IDS')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_RESULTS')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_DESTINATION_FOLDER_OBJECT_ID')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_MOVE_RESULTS')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_COPY_RESULTS')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_UPDATE_PROPERTIES')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_PROPERTY_KEYS')
make_head(_module, 'WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_FORMAT')
make_head(_module, 'WPD_OPTION_OBJECT_MANAGEMENT_RECURSIVE_DELETE_SUPPORTED')
make_head(_module, 'WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS')
make_head(_module, 'WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS')
make_head(_module, 'WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES')
make_head(_module, 'WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS')
make_head(_module, 'WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES')
make_head(_module, 'WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS')
make_head(_module, 'WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES')
make_head(_module, 'WPD_COMMAND_CAPABILITIES_GET_FIXED_PROPERTY_ATTRIBUTES')
make_head(_module, 'WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS')
make_head(_module, 'WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_COMMAND')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_FORMATS')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_FORMAT')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_EVENT')
make_head(_module, 'WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS')
make_head(_module, 'WPD_COMMAND_STORAGE_FORMAT')
make_head(_module, 'WPD_COMMAND_STORAGE_EJECT')
make_head(_module, 'WPD_PROPERTY_STORAGE_OBJECT_ID')
make_head(_module, 'WPD_PROPERTY_STORAGE_DESTINATION_OBJECT_ID')
make_head(_module, 'WPD_COMMAND_SMS_SEND')
make_head(_module, 'WPD_PROPERTY_SMS_RECIPIENT')
make_head(_module, 'WPD_PROPERTY_SMS_MESSAGE_TYPE')
make_head(_module, 'WPD_PROPERTY_SMS_TEXT_MESSAGE')
make_head(_module, 'WPD_PROPERTY_SMS_BINARY_MESSAGE')
make_head(_module, 'WPD_OPTION_SMS_BINARY_MESSAGE_SUPPORTED')
make_head(_module, 'WPD_COMMAND_STILL_IMAGE_CAPTURE_INITIATE')
make_head(_module, 'WPD_COMMAND_MEDIA_CAPTURE_START')
make_head(_module, 'WPD_COMMAND_MEDIA_CAPTURE_STOP')
make_head(_module, 'WPD_COMMAND_MEDIA_CAPTURE_PAUSE')
make_head(_module, 'WPD_COMMAND_DEVICE_HINTS_GET_CONTENT_LOCATION')
make_head(_module, 'WPD_PROPERTY_DEVICE_HINTS_CONTENT_TYPE')
make_head(_module, 'WPD_PROPERTY_DEVICE_HINTS_CONTENT_LOCATIONS')
make_head(_module, 'WPD_COMMAND_CLASS_EXTENSION_WRITE_DEVICE_INFORMATION')
make_head(_module, 'WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_VALUES')
make_head(_module, 'WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_WRITE_RESULTS')
make_head(_module, 'WPD_COMMAND_CLASS_EXTENSION_REGISTER_SERVICE_INTERFACES')
make_head(_module, 'WPD_COMMAND_CLASS_EXTENSION_UNREGISTER_SERVICE_INTERFACES')
make_head(_module, 'WPD_PROPERTY_CLASS_EXTENSION_SERVICE_OBJECT_ID')
make_head(_module, 'WPD_PROPERTY_CLASS_EXTENSION_SERVICE_INTERFACES')
make_head(_module, 'WPD_PROPERTY_CLASS_EXTENSION_SERVICE_REGISTRATION_RESULTS')
make_head(_module, 'WPD_COMMAND_GENERATE_KEYPAIR')
make_head(_module, 'WPD_COMMAND_COMMIT_KEYPAIR')
make_head(_module, 'WPD_COMMAND_PROCESS_WIRELESS_PROFILE')
make_head(_module, 'WPD_PROPERTY_PUBLIC_KEY')
make_head(_module, 'WPD_COMMAND_SERVICE_COMMON_GET_SERVICE_OBJECT_ID')
make_head(_module, 'WPD_PROPERTY_SERVICE_OBJECT_ID')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS_BY_FORMAT')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_ATTRIBUTES')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_PARAMETER_ATTRIBUTES')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMATS')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_ATTRIBUTES')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_PROPERTY_ATTRIBUTES')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_EVENTS')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_ATTRIBUTES')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_PARAMETER_ATTRIBUTES')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_INHERITED_SERVICES')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_RENDERING_PROFILES')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_COMMANDS')
make_head(_module, 'WPD_COMMAND_SERVICE_CAPABILITIES_GET_COMMAND_OPTIONS')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_METHODS')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD_ATTRIBUTES')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER_ATTRIBUTES')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_FORMATS')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT_ATTRIBUTES')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_KEYS')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_ATTRIBUTES')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_EVENTS')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT_ATTRIBUTES')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITANCE_TYPE')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITED_SERVICES')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_RENDERING_PROFILES')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_COMMANDS')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND')
make_head(_module, 'WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND_OPTIONS')
make_head(_module, 'WPD_COMMAND_SERVICE_METHODS_START_INVOKE')
make_head(_module, 'WPD_COMMAND_SERVICE_METHODS_CANCEL_INVOKE')
make_head(_module, 'WPD_COMMAND_SERVICE_METHODS_END_INVOKE')
make_head(_module, 'WPD_PROPERTY_SERVICE_METHOD')
make_head(_module, 'WPD_PROPERTY_SERVICE_METHOD_PARAMETER_VALUES')
make_head(_module, 'WPD_PROPERTY_SERVICE_METHOD_RESULT_VALUES')
make_head(_module, 'WPD_PROPERTY_SERVICE_METHOD_CONTEXT')
make_head(_module, 'WPD_PROPERTY_SERVICE_METHOD_HRESULT')
make_head(_module, 'WPD_RESOURCE_DEFAULT')
make_head(_module, 'WPD_RESOURCE_CONTACT_PHOTO')
make_head(_module, 'WPD_RESOURCE_THUMBNAIL')
make_head(_module, 'WPD_RESOURCE_ICON')
make_head(_module, 'WPD_RESOURCE_AUDIO_CLIP')
make_head(_module, 'WPD_RESOURCE_ALBUM_ART')
make_head(_module, 'WPD_RESOURCE_GENERIC')
make_head(_module, 'WPD_RESOURCE_VIDEO_CLIP')
make_head(_module, 'WPD_RESOURCE_BRANDING_ART')
make_head(_module, 'WPD_OBJECT_ID')
make_head(_module, 'WPD_OBJECT_PARENT_ID')
make_head(_module, 'WPD_OBJECT_NAME')
make_head(_module, 'WPD_OBJECT_PERSISTENT_UNIQUE_ID')
make_head(_module, 'WPD_OBJECT_FORMAT')
make_head(_module, 'WPD_OBJECT_ISHIDDEN')
make_head(_module, 'WPD_OBJECT_ISSYSTEM')
make_head(_module, 'WPD_OBJECT_SIZE')
make_head(_module, 'WPD_OBJECT_ORIGINAL_FILE_NAME')
make_head(_module, 'WPD_OBJECT_NON_CONSUMABLE')
make_head(_module, 'WPD_OBJECT_KEYWORDS')
make_head(_module, 'WPD_OBJECT_SYNC_ID')
make_head(_module, 'WPD_OBJECT_IS_DRM_PROTECTED')
make_head(_module, 'WPD_OBJECT_DATE_CREATED')
make_head(_module, 'WPD_OBJECT_DATE_MODIFIED')
make_head(_module, 'WPD_OBJECT_DATE_AUTHORED')
make_head(_module, 'WPD_OBJECT_BACK_REFERENCES')
make_head(_module, 'WPD_OBJECT_CAN_DELETE')
make_head(_module, 'WPD_OBJECT_LANGUAGE_LOCALE')
make_head(_module, 'WPD_FOLDER_CONTENT_TYPES_ALLOWED')
make_head(_module, 'WPD_IMAGE_BITDEPTH')
make_head(_module, 'WPD_IMAGE_CROPPED_STATUS')
make_head(_module, 'WPD_IMAGE_COLOR_CORRECTED_STATUS')
make_head(_module, 'WPD_IMAGE_FNUMBER')
make_head(_module, 'WPD_IMAGE_EXPOSURE_TIME')
make_head(_module, 'WPD_IMAGE_EXPOSURE_INDEX')
make_head(_module, 'WPD_IMAGE_HORIZONTAL_RESOLUTION')
make_head(_module, 'WPD_IMAGE_VERTICAL_RESOLUTION')
make_head(_module, 'WPD_MEDIA_TOTAL_BITRATE')
make_head(_module, 'WPD_MEDIA_BITRATE_TYPE')
make_head(_module, 'WPD_MEDIA_COPYRIGHT')
make_head(_module, 'WPD_MEDIA_SUBSCRIPTION_CONTENT_ID')
make_head(_module, 'WPD_MEDIA_USE_COUNT')
make_head(_module, 'WPD_MEDIA_SKIP_COUNT')
make_head(_module, 'WPD_MEDIA_LAST_ACCESSED_TIME')
make_head(_module, 'WPD_MEDIA_PARENTAL_RATING')
make_head(_module, 'WPD_MEDIA_META_GENRE')
make_head(_module, 'WPD_MEDIA_COMPOSER')
make_head(_module, 'WPD_MEDIA_EFFECTIVE_RATING')
make_head(_module, 'WPD_MEDIA_SUB_TITLE')
make_head(_module, 'WPD_MEDIA_RELEASE_DATE')
make_head(_module, 'WPD_MEDIA_SAMPLE_RATE')
make_head(_module, 'WPD_MEDIA_STAR_RATING')
make_head(_module, 'WPD_MEDIA_USER_EFFECTIVE_RATING')
make_head(_module, 'WPD_MEDIA_TITLE')
make_head(_module, 'WPD_MEDIA_DURATION')
make_head(_module, 'WPD_MEDIA_BUY_NOW')
make_head(_module, 'WPD_MEDIA_ENCODING_PROFILE')
make_head(_module, 'WPD_MEDIA_WIDTH')
make_head(_module, 'WPD_MEDIA_HEIGHT')
make_head(_module, 'WPD_MEDIA_ARTIST')
make_head(_module, 'WPD_MEDIA_ALBUM_ARTIST')
make_head(_module, 'WPD_MEDIA_OWNER')
make_head(_module, 'WPD_MEDIA_MANAGING_EDITOR')
make_head(_module, 'WPD_MEDIA_WEBMASTER')
make_head(_module, 'WPD_MEDIA_SOURCE_URL')
make_head(_module, 'WPD_MEDIA_DESTINATION_URL')
make_head(_module, 'WPD_MEDIA_DESCRIPTION')
make_head(_module, 'WPD_MEDIA_GENRE')
make_head(_module, 'WPD_MEDIA_TIME_BOOKMARK')
make_head(_module, 'WPD_MEDIA_OBJECT_BOOKMARK')
make_head(_module, 'WPD_MEDIA_LAST_BUILD_DATE')
make_head(_module, 'WPD_MEDIA_BYTE_BOOKMARK')
make_head(_module, 'WPD_MEDIA_TIME_TO_LIVE')
make_head(_module, 'WPD_MEDIA_GUID')
make_head(_module, 'WPD_MEDIA_SUB_DESCRIPTION')
make_head(_module, 'WPD_MEDIA_AUDIO_ENCODING_PROFILE')
make_head(_module, 'WPD_CONTACT_DISPLAY_NAME')
make_head(_module, 'WPD_CONTACT_FIRST_NAME')
make_head(_module, 'WPD_CONTACT_MIDDLE_NAMES')
make_head(_module, 'WPD_CONTACT_LAST_NAME')
make_head(_module, 'WPD_CONTACT_PREFIX')
make_head(_module, 'WPD_CONTACT_SUFFIX')
make_head(_module, 'WPD_CONTACT_PHONETIC_FIRST_NAME')
make_head(_module, 'WPD_CONTACT_PHONETIC_LAST_NAME')
make_head(_module, 'WPD_CONTACT_PERSONAL_FULL_POSTAL_ADDRESS')
make_head(_module, 'WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE1')
make_head(_module, 'WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE2')
make_head(_module, 'WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_CITY')
make_head(_module, 'WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_REGION')
make_head(_module, 'WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_POSTAL_CODE')
make_head(_module, 'WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_COUNTRY')
make_head(_module, 'WPD_CONTACT_BUSINESS_FULL_POSTAL_ADDRESS')
make_head(_module, 'WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE1')
make_head(_module, 'WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE2')
make_head(_module, 'WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_CITY')
make_head(_module, 'WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_REGION')
make_head(_module, 'WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_POSTAL_CODE')
make_head(_module, 'WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_COUNTRY')
make_head(_module, 'WPD_CONTACT_OTHER_FULL_POSTAL_ADDRESS')
make_head(_module, 'WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE1')
make_head(_module, 'WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE2')
make_head(_module, 'WPD_CONTACT_OTHER_POSTAL_ADDRESS_CITY')
make_head(_module, 'WPD_CONTACT_OTHER_POSTAL_ADDRESS_REGION')
make_head(_module, 'WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_CODE')
make_head(_module, 'WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_COUNTRY')
make_head(_module, 'WPD_CONTACT_PRIMARY_EMAIL_ADDRESS')
make_head(_module, 'WPD_CONTACT_PERSONAL_EMAIL')
make_head(_module, 'WPD_CONTACT_PERSONAL_EMAIL2')
make_head(_module, 'WPD_CONTACT_BUSINESS_EMAIL')
make_head(_module, 'WPD_CONTACT_BUSINESS_EMAIL2')
make_head(_module, 'WPD_CONTACT_OTHER_EMAILS')
make_head(_module, 'WPD_CONTACT_PRIMARY_PHONE')
make_head(_module, 'WPD_CONTACT_PERSONAL_PHONE')
make_head(_module, 'WPD_CONTACT_PERSONAL_PHONE2')
make_head(_module, 'WPD_CONTACT_BUSINESS_PHONE')
make_head(_module, 'WPD_CONTACT_BUSINESS_PHONE2')
make_head(_module, 'WPD_CONTACT_MOBILE_PHONE')
make_head(_module, 'WPD_CONTACT_MOBILE_PHONE2')
make_head(_module, 'WPD_CONTACT_PERSONAL_FAX')
make_head(_module, 'WPD_CONTACT_BUSINESS_FAX')
make_head(_module, 'WPD_CONTACT_PAGER')
make_head(_module, 'WPD_CONTACT_OTHER_PHONES')
make_head(_module, 'WPD_CONTACT_PRIMARY_WEB_ADDRESS')
make_head(_module, 'WPD_CONTACT_PERSONAL_WEB_ADDRESS')
make_head(_module, 'WPD_CONTACT_BUSINESS_WEB_ADDRESS')
make_head(_module, 'WPD_CONTACT_INSTANT_MESSENGER')
make_head(_module, 'WPD_CONTACT_INSTANT_MESSENGER2')
make_head(_module, 'WPD_CONTACT_INSTANT_MESSENGER3')
make_head(_module, 'WPD_CONTACT_COMPANY_NAME')
make_head(_module, 'WPD_CONTACT_PHONETIC_COMPANY_NAME')
make_head(_module, 'WPD_CONTACT_ROLE')
make_head(_module, 'WPD_CONTACT_BIRTHDATE')
make_head(_module, 'WPD_CONTACT_PRIMARY_FAX')
make_head(_module, 'WPD_CONTACT_SPOUSE')
make_head(_module, 'WPD_CONTACT_CHILDREN')
make_head(_module, 'WPD_CONTACT_ASSISTANT')
make_head(_module, 'WPD_CONTACT_ANNIVERSARY_DATE')
make_head(_module, 'WPD_CONTACT_RINGTONE')
make_head(_module, 'WPD_MUSIC_ALBUM')
make_head(_module, 'WPD_MUSIC_TRACK')
make_head(_module, 'WPD_MUSIC_LYRICS')
make_head(_module, 'WPD_MUSIC_MOOD')
make_head(_module, 'WPD_AUDIO_BITRATE')
make_head(_module, 'WPD_AUDIO_CHANNEL_COUNT')
make_head(_module, 'WPD_AUDIO_FORMAT_CODE')
make_head(_module, 'WPD_AUDIO_BIT_DEPTH')
make_head(_module, 'WPD_AUDIO_BLOCK_ALIGNMENT')
make_head(_module, 'WPD_VIDEO_AUTHOR')
make_head(_module, 'WPD_VIDEO_RECORDEDTV_STATION_NAME')
make_head(_module, 'WPD_VIDEO_RECORDEDTV_CHANNEL_NUMBER')
make_head(_module, 'WPD_VIDEO_RECORDEDTV_REPEAT')
make_head(_module, 'WPD_VIDEO_BUFFER_SIZE')
make_head(_module, 'WPD_VIDEO_CREDITS')
make_head(_module, 'WPD_VIDEO_KEY_FRAME_DISTANCE')
make_head(_module, 'WPD_VIDEO_QUALITY_SETTING')
make_head(_module, 'WPD_VIDEO_SCAN_TYPE')
make_head(_module, 'WPD_VIDEO_BITRATE')
make_head(_module, 'WPD_VIDEO_FOURCC_CODE')
make_head(_module, 'WPD_VIDEO_FRAMERATE')
make_head(_module, 'WPD_COMMON_INFORMATION_SUBJECT')
make_head(_module, 'WPD_COMMON_INFORMATION_BODY_TEXT')
make_head(_module, 'WPD_COMMON_INFORMATION_PRIORITY')
make_head(_module, 'WPD_COMMON_INFORMATION_START_DATETIME')
make_head(_module, 'WPD_COMMON_INFORMATION_END_DATETIME')
make_head(_module, 'WPD_COMMON_INFORMATION_NOTES')
make_head(_module, 'WPD_EMAIL_TO_LINE')
make_head(_module, 'WPD_EMAIL_CC_LINE')
make_head(_module, 'WPD_EMAIL_BCC_LINE')
make_head(_module, 'WPD_EMAIL_HAS_BEEN_READ')
make_head(_module, 'WPD_EMAIL_RECEIVED_TIME')
make_head(_module, 'WPD_EMAIL_HAS_ATTACHMENTS')
make_head(_module, 'WPD_EMAIL_SENDER_ADDRESS')
make_head(_module, 'WPD_APPOINTMENT_LOCATION')
make_head(_module, 'WPD_APPOINTMENT_TYPE')
make_head(_module, 'WPD_APPOINTMENT_REQUIRED_ATTENDEES')
make_head(_module, 'WPD_APPOINTMENT_OPTIONAL_ATTENDEES')
make_head(_module, 'WPD_APPOINTMENT_ACCEPTED_ATTENDEES')
make_head(_module, 'WPD_APPOINTMENT_RESOURCES')
make_head(_module, 'WPD_APPOINTMENT_TENTATIVE_ATTENDEES')
make_head(_module, 'WPD_APPOINTMENT_DECLINED_ATTENDEES')
make_head(_module, 'WPD_TASK_STATUS')
make_head(_module, 'WPD_TASK_PERCENT_COMPLETE')
make_head(_module, 'WPD_TASK_REMINDER_DATE')
make_head(_module, 'WPD_TASK_OWNER')
make_head(_module, 'WPD_SMS_PROVIDER')
make_head(_module, 'WPD_SMS_TIMEOUT')
make_head(_module, 'WPD_SMS_MAX_PAYLOAD')
make_head(_module, 'WPD_SMS_ENCODING')
make_head(_module, 'WPD_SECTION_DATA_OFFSET')
make_head(_module, 'WPD_SECTION_DATA_LENGTH')
make_head(_module, 'WPD_SECTION_DATA_UNITS')
make_head(_module, 'WPD_SECTION_DATA_REFERENCED_OBJECT_RESOURCE')
make_head(_module, 'WPD_COMMAND_MTP_EXT_GET_SUPPORTED_VENDOR_OPCODES')
make_head(_module, 'WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITHOUT_DATA_PHASE')
make_head(_module, 'WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITH_DATA_TO_READ')
make_head(_module, 'WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITH_DATA_TO_WRITE')
make_head(_module, 'WPD_COMMAND_MTP_EXT_READ_DATA')
make_head(_module, 'WPD_COMMAND_MTP_EXT_WRITE_DATA')
make_head(_module, 'WPD_COMMAND_MTP_EXT_END_DATA_TRANSFER')
make_head(_module, 'WPD_COMMAND_MTP_EXT_GET_VENDOR_EXTENSION_DESCRIPTION')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_OPERATION_CODE')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_OPERATION_PARAMS')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_RESPONSE_CODE')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_RESPONSE_PARAMS')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_VENDOR_OPERATION_CODES')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_TRANSFER_CONTEXT')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_TRANSFER_TOTAL_DATA_SIZE')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_TO_READ')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_READ')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_TO_WRITE')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_WRITTEN')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_TRANSFER_DATA')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_OPTIMAL_TRANSFER_BUFFER_SIZE')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_VENDOR_EXTENSION_DESCRIPTION')
make_head(_module, 'WPD_PROPERTY_MTP_EXT_EVENT_PARAMS')
make_head(_module, 'WPDNSE_OBJECT_HAS_CONTACT_PHOTO')
make_head(_module, 'WPDNSE_OBJECT_HAS_THUMBNAIL')
make_head(_module, 'WPDNSE_OBJECT_HAS_ICON')
make_head(_module, 'WPDNSE_OBJECT_HAS_AUDIO_CLIP')
make_head(_module, 'WPDNSE_OBJECT_HAS_ALBUM_ART')
make_head(_module, 'WPDNSE_OBJECT_OPTIMAL_READ_BLOCK_SIZE')
make_head(_module, 'IConnectionRequestCallback')
make_head(_module, 'IEnumPortableDeviceConnectors')
make_head(_module, 'IEnumPortableDeviceObjectIDs')
make_head(_module, 'IMediaRadioManager')
make_head(_module, 'IMediaRadioManagerNotifySink')
make_head(_module, 'IPortableDevice')
make_head(_module, 'IPortableDeviceCapabilities')
make_head(_module, 'IPortableDeviceConnector')
make_head(_module, 'IPortableDeviceContent')
make_head(_module, 'IPortableDeviceContent2')
make_head(_module, 'IPortableDeviceDataStream')
make_head(_module, 'IPortableDeviceDispatchFactory')
make_head(_module, 'IPortableDeviceEventCallback')
make_head(_module, 'IPortableDeviceKeyCollection')
make_head(_module, 'IPortableDeviceManager')
make_head(_module, 'IPortableDevicePropVariantCollection')
make_head(_module, 'IPortableDeviceProperties')
make_head(_module, 'IPortableDevicePropertiesBulk')
make_head(_module, 'IPortableDevicePropertiesBulkCallback')
make_head(_module, 'IPortableDeviceResources')
make_head(_module, 'IPortableDeviceService')
make_head(_module, 'IPortableDeviceServiceActivation')
make_head(_module, 'IPortableDeviceServiceCapabilities')
make_head(_module, 'IPortableDeviceServiceManager')
make_head(_module, 'IPortableDeviceServiceMethodCallback')
make_head(_module, 'IPortableDeviceServiceMethods')
make_head(_module, 'IPortableDeviceServiceOpenCallback')
make_head(_module, 'IPortableDeviceUnitsStream')
make_head(_module, 'IPortableDeviceValues')
make_head(_module, 'IPortableDeviceValuesCollection')
make_head(_module, 'IPortableDeviceWebControl')
make_head(_module, 'IRadioInstance')
make_head(_module, 'IRadioInstanceCollection')
make_head(_module, 'IWpdSerializer')
make_head(_module, 'WPD_COMMAND_ACCESS_LOOKUP_ENTRY')
