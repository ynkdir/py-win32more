from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.PortableDevices
import win32more.Windows.Win32.Devices.Properties
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.UI.Shell.PropertiesSystem
DEVPKEY_MTPBTH_IsConnected: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{ea1237fa-589d-4472-84e4-0abe36fd62ef}'), pid=2)
GUID_DEVINTERFACE_WPD: Guid = Guid('{6ac27878-a6fa-4155-ba85-f98f491d4f33}')
GUID_DEVINTERFACE_WPD_PRIVATE: Guid = Guid('{ba0c718f-4ded-49b7-bdd3-fabe28661211}')
GUID_DEVINTERFACE_WPD_SERVICE: Guid = Guid('{9ef44f80-3d64-4246-a6aa-206f328d1edc}')
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
E_WPD_DEVICE_ALREADY_OPENED: win32more.Windows.Win32.Foundation.HRESULT = -2144731135
E_WPD_DEVICE_NOT_OPEN: win32more.Windows.Win32.Foundation.HRESULT = -2144731134
E_WPD_OBJECT_ALREADY_ATTACHED_TO_DEVICE: win32more.Windows.Win32.Foundation.HRESULT = -2144731133
E_WPD_OBJECT_NOT_ATTACHED_TO_DEVICE: win32more.Windows.Win32.Foundation.HRESULT = -2144731132
E_WPD_OBJECT_NOT_COMMITED: win32more.Windows.Win32.Foundation.HRESULT = -2144731131
E_WPD_DEVICE_IS_HUNG: win32more.Windows.Win32.Foundation.HRESULT = -2144731130
E_WPD_SMS_INVALID_RECIPIENT: win32more.Windows.Win32.Foundation.HRESULT = -2144731036
E_WPD_SMS_INVALID_MESSAGE_BODY: win32more.Windows.Win32.Foundation.HRESULT = -2144731035
E_WPD_SMS_SERVICE_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2144731034
E_WPD_SERVICE_ALREADY_OPENED: win32more.Windows.Win32.Foundation.HRESULT = -2144730936
E_WPD_SERVICE_NOT_OPEN: win32more.Windows.Win32.Foundation.HRESULT = -2144730935
E_WPD_OBJECT_ALREADY_ATTACHED_TO_SERVICE: win32more.Windows.Win32.Foundation.HRESULT = -2144730934
E_WPD_OBJECT_NOT_ATTACHED_TO_SERVICE: win32more.Windows.Win32.Foundation.HRESULT = -2144730933
E_WPD_SERVICE_BAD_PARAMETER_ORDER: win32more.Windows.Win32.Foundation.HRESULT = -2144730932
WPD_EVENT_NOTIFICATION: Guid = Guid('{2ba2e40a-6b4c-4295-bb43-26322b99aeb2}')
WPD_EVENT_OBJECT_ADDED: Guid = Guid('{a726da95-e207-4b02-8d44-bef2e86cbffc}')
WPD_EVENT_OBJECT_REMOVED: Guid = Guid('{be82ab88-a52c-4823-96e5-d0272671fc38}')
WPD_EVENT_OBJECT_UPDATED: Guid = Guid('{1445a759-2e01-485d-9f27-ff07dae697ab}')
WPD_EVENT_DEVICE_RESET: Guid = Guid('{7755cf53-c1ed-44f3-b5a2-451e2c376b27}')
WPD_EVENT_DEVICE_CAPABILITIES_UPDATED: Guid = Guid('{36885aa1-cd54-4daa-b3d0-afb3e03f5999}')
WPD_EVENT_STORAGE_FORMAT: Guid = Guid('{3782616b-22bc-4474-a251-3070f8d38857}')
WPD_EVENT_OBJECT_TRANSFER_REQUESTED: Guid = Guid('{8d16a0a1-f2c6-41da-8f19-5e53721adbf2}')
WPD_EVENT_DEVICE_REMOVED: Guid = Guid('{e4cbca1b-6918-48b9-85ee-02be7c850af9}')
WPD_EVENT_SERVICE_METHOD_COMPLETE: Guid = Guid('{8a33f5f8-0acc-4d9b-9cc4-112d353b86ca}')
WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT: Guid = Guid('{99ed0160-17ff-4c44-9d98-1d7a6f941921}')
WPD_CONTENT_TYPE_FOLDER: Guid = Guid('{27e2e392-a111-48e0-ab0c-e17705a05f85}')
WPD_CONTENT_TYPE_IMAGE: Guid = Guid('{ef2107d5-a52a-4243-a26b-62d4176d7603}')
WPD_CONTENT_TYPE_DOCUMENT: Guid = Guid('{680adf52-950a-4041-9b41-65e393648155}')
WPD_CONTENT_TYPE_CONTACT: Guid = Guid('{eaba8313-4525-4707-9f0e-87c6808e9435}')
WPD_CONTENT_TYPE_CONTACT_GROUP: Guid = Guid('{346b8932-4c36-40d8-9415-1828291f9de9}')
WPD_CONTENT_TYPE_AUDIO: Guid = Guid('{4ad2c85e-5e2d-45e5-8864-4f229e3c6cf0}')
WPD_CONTENT_TYPE_VIDEO: Guid = Guid('{9261b03c-3d78-4519-85e3-02c5e1f50bb9}')
WPD_CONTENT_TYPE_TELEVISION: Guid = Guid('{60a169cf-f2ae-4e21-9375-9677f11c1c6e}')
WPD_CONTENT_TYPE_PLAYLIST: Guid = Guid('{1a33f7e4-af13-48f5-994e-77369dfe04a3}')
WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM: Guid = Guid('{00f0c3ac-a593-49ac-9219-24abca5a2563}')
WPD_CONTENT_TYPE_AUDIO_ALBUM: Guid = Guid('{aa18737e-5009-48fa-ae21-85f24383b4e6}')
WPD_CONTENT_TYPE_IMAGE_ALBUM: Guid = Guid('{75793148-15f5-4a30-a813-54ed8a37e226}')
WPD_CONTENT_TYPE_VIDEO_ALBUM: Guid = Guid('{012b0db7-d4c1-45d6-b081-94b87779614f}')
WPD_CONTENT_TYPE_MEMO: Guid = Guid('{9cd20ecf-3b50-414f-a641-e473ffe45751}')
WPD_CONTENT_TYPE_EMAIL: Guid = Guid('{8038044a-7e51-4f8f-883d-1d0623d14533}')
WPD_CONTENT_TYPE_APPOINTMENT: Guid = Guid('{0fed060e-8793-4b1e-90c9-48ac389ac631}')
WPD_CONTENT_TYPE_TASK: Guid = Guid('{63252f2c-887f-4cb6-b1ac-d29855dcef6c}')
WPD_CONTENT_TYPE_PROGRAM: Guid = Guid('{d269f96a-247c-4bff-98fb-97f3c49220e6}')
WPD_CONTENT_TYPE_GENERIC_FILE: Guid = Guid('{0085e0a6-8d34-45d7-bc5c-447e59c73d48}')
WPD_CONTENT_TYPE_CALENDAR: Guid = Guid('{a1fd5967-6023-49a0-9df1-f8060be751b0}')
WPD_CONTENT_TYPE_GENERIC_MESSAGE: Guid = Guid('{e80eaaf8-b2db-4133-b67e-1bef4b4a6e5f}')
WPD_CONTENT_TYPE_NETWORK_ASSOCIATION: Guid = Guid('{031da7ee-18c8-4205-847e-89a11261d0f3}')
WPD_CONTENT_TYPE_CERTIFICATE: Guid = Guid('{dc3876e8-a948-4060-9050-cbd77e8a3d87}')
WPD_CONTENT_TYPE_WIRELESS_PROFILE: Guid = Guid('{0bac070a-9f5f-4da4-a8f6-3de44d68fd6c}')
WPD_CONTENT_TYPE_MEDIA_CAST: Guid = Guid('{5e88b3cc-3e65-4e62-bfff-229495253ab0}')
WPD_CONTENT_TYPE_SECTION: Guid = Guid('{821089f5-1d91-4dc9-be3c-bbb1b35b18ce}')
WPD_CONTENT_TYPE_UNSPECIFIED: Guid = Guid('{28d8d31e-249c-454e-aabc-34883168e634}')
WPD_CONTENT_TYPE_ALL: Guid = Guid('{80e170d2-1055-4a3e-b952-82cc4f8a8689}')
WPD_FUNCTIONAL_CATEGORY_DEVICE: Guid = Guid('{08ea466b-e3a4-4336-a1f3-a44d2b5c438c}')
WPD_FUNCTIONAL_CATEGORY_STORAGE: Guid = Guid('{23f05bbc-15de-4c2a-a55b-a9af5ce412ef}')
WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE: Guid = Guid('{613ca327-ab93-4900-b4fa-895bb5874b79}')
WPD_FUNCTIONAL_CATEGORY_AUDIO_CAPTURE: Guid = Guid('{3f2a1919-c7c2-4a00-855d-f57cf06debbb}')
WPD_FUNCTIONAL_CATEGORY_VIDEO_CAPTURE: Guid = Guid('{e23e5f6b-7243-43aa-8df1-0eb3d968a918}')
WPD_FUNCTIONAL_CATEGORY_SMS: Guid = Guid('{0044a0b1-c1e9-4afd-b358-a62c6117c9cf}')
WPD_FUNCTIONAL_CATEGORY_RENDERING_INFORMATION: Guid = Guid('{08600ba4-a7ba-4a01-ab0e-0065d0a356d3}')
WPD_FUNCTIONAL_CATEGORY_NETWORK_CONFIGURATION: Guid = Guid('{48f4db72-7c6a-4ab0-9e1a-470e3cdbf26a}')
WPD_FUNCTIONAL_CATEGORY_ALL: Guid = Guid('{2d8a6512-a74c-448e-ba8a-f4ac07c49399}')
WPD_OBJECT_FORMAT_ICON: Guid = Guid('{077232ed-102c-4638-9c22-83f142bfc822}')
WPD_OBJECT_FORMAT_M4A: Guid = Guid('{30aba7ac-6ffd-4c23-a359-3e9b52f3f1c8}')
WPD_OBJECT_FORMAT_NETWORK_ASSOCIATION: Guid = Guid('{b1020000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_X509V3CERTIFICATE: Guid = Guid('{b1030000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_MICROSOFT_WFC: Guid = Guid('{b1040000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_3GPA: Guid = Guid('{e5172730-f971-41ef-a10b-2271a0019d7a}')
WPD_OBJECT_FORMAT_3G2A: Guid = Guid('{1a11202d-8759-4e34-ba5e-b1211087eee4}')
WPD_OBJECT_FORMAT_ALL: Guid = Guid('{c1f62eb2-4bb3-479c-9cfa-05b5f3a57b22}')
WPD_CATEGORY_NULL: Guid = Guid('{00000000-0000-0000-0000-000000000000}')
WPD_PROPERTY_NULL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{00000000-0000-0000-0000-000000000000}'), pid=0)
WPD_OBJECT_PROPERTIES_V1: Guid = Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}')
WPD_OBJECT_CONTENT_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=7)
WPD_OBJECT_REFERENCES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=14)
WPD_OBJECT_CONTAINER_FUNCTIONAL_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=23)
WPD_OBJECT_GENERATE_THUMBNAIL_FROM_RESOURCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=24)
WPD_OBJECT_HINT_LOCATION_DISPLAY_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=25)
WPD_OBJECT_PROPERTIES_V2: Guid = Guid('{0373cd3d-4a46-40d7-b4d8-73e8da74e775}')
WPD_OBJECT_SUPPORTED_UNITS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0373cd3d-4a46-40d7-b4d8-73e8da74e775}'), pid=2)
WPD_FUNCTIONAL_OBJECT_PROPERTIES_V1: Guid = Guid('{8f052d93-abca-4fc5-a5ac-b01df4dbe598}')
WPD_FUNCTIONAL_OBJECT_CATEGORY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8f052d93-abca-4fc5-a5ac-b01df4dbe598}'), pid=2)
WPD_STORAGE_OBJECT_PROPERTIES_V1: Guid = Guid('{01a3057a-74d6-4e80-bea7-dc4c212ce50a}')
WPD_STORAGE_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{01a3057a-74d6-4e80-bea7-dc4c212ce50a}'), pid=2)
WPD_STORAGE_FILE_SYSTEM_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{01a3057a-74d6-4e80-bea7-dc4c212ce50a}'), pid=3)
WPD_STORAGE_CAPACITY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{01a3057a-74d6-4e80-bea7-dc4c212ce50a}'), pid=4)
WPD_STORAGE_FREE_SPACE_IN_BYTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{01a3057a-74d6-4e80-bea7-dc4c212ce50a}'), pid=5)
WPD_STORAGE_FREE_SPACE_IN_OBJECTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{01a3057a-74d6-4e80-bea7-dc4c212ce50a}'), pid=6)
WPD_STORAGE_DESCRIPTION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{01a3057a-74d6-4e80-bea7-dc4c212ce50a}'), pid=7)
WPD_STORAGE_SERIAL_NUMBER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{01a3057a-74d6-4e80-bea7-dc4c212ce50a}'), pid=8)
WPD_STORAGE_MAX_OBJECT_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{01a3057a-74d6-4e80-bea7-dc4c212ce50a}'), pid=9)
WPD_STORAGE_CAPACITY_IN_OBJECTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{01a3057a-74d6-4e80-bea7-dc4c212ce50a}'), pid=10)
WPD_STORAGE_ACCESS_CAPABILITY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{01a3057a-74d6-4e80-bea7-dc4c212ce50a}'), pid=11)
WPD_NETWORK_ASSOCIATION_PROPERTIES_V1: Guid = Guid('{e4c93c1f-b203-43f1-a100-5a07d11b0274}')
WPD_NETWORK_ASSOCIATION_HOST_NETWORK_IDENTIFIERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e4c93c1f-b203-43f1-a100-5a07d11b0274}'), pid=2)
WPD_NETWORK_ASSOCIATION_X509V3SEQUENCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e4c93c1f-b203-43f1-a100-5a07d11b0274}'), pid=3)
WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1: Guid = Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}')
WPD_STILL_IMAGE_CAPTURE_RESOLUTION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=2)
WPD_STILL_IMAGE_CAPTURE_FORMAT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=3)
WPD_STILL_IMAGE_COMPRESSION_SETTING: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=4)
WPD_STILL_IMAGE_WHITE_BALANCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=5)
WPD_STILL_IMAGE_RGB_GAIN: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=6)
WPD_STILL_IMAGE_FNUMBER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=7)
WPD_STILL_IMAGE_FOCAL_LENGTH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=8)
WPD_STILL_IMAGE_FOCUS_DISTANCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=9)
WPD_STILL_IMAGE_FOCUS_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=10)
WPD_STILL_IMAGE_EXPOSURE_METERING_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=11)
WPD_STILL_IMAGE_FLASH_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=12)
WPD_STILL_IMAGE_EXPOSURE_TIME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=13)
WPD_STILL_IMAGE_EXPOSURE_PROGRAM_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=14)
WPD_STILL_IMAGE_EXPOSURE_INDEX: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=15)
WPD_STILL_IMAGE_EXPOSURE_BIAS_COMPENSATION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=16)
WPD_STILL_IMAGE_CAPTURE_DELAY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=17)
WPD_STILL_IMAGE_CAPTURE_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=18)
WPD_STILL_IMAGE_CONTRAST: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=19)
WPD_STILL_IMAGE_SHARPNESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=20)
WPD_STILL_IMAGE_DIGITAL_ZOOM: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=21)
WPD_STILL_IMAGE_EFFECT_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=22)
WPD_STILL_IMAGE_BURST_NUMBER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=23)
WPD_STILL_IMAGE_BURST_INTERVAL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=24)
WPD_STILL_IMAGE_TIMELAPSE_NUMBER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=25)
WPD_STILL_IMAGE_TIMELAPSE_INTERVAL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=26)
WPD_STILL_IMAGE_FOCUS_METERING_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=27)
WPD_STILL_IMAGE_UPLOAD_URL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=28)
WPD_STILL_IMAGE_ARTIST: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=29)
WPD_STILL_IMAGE_CAMERA_MODEL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=30)
WPD_STILL_IMAGE_CAMERA_MANUFACTURER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{58c571ec-1bcb-42a7-8ac5-bb291573a260}'), pid=31)
WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1: Guid = Guid('{c53d039f-ee23-4a31-8590-7639879870b4}')
WPD_RENDERING_INFORMATION_PROFILES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{c53d039f-ee23-4a31-8590-7639879870b4}'), pid=2)
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{c53d039f-ee23-4a31-8590-7639879870b4}'), pid=3)
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_CREATABLE_RESOURCES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{c53d039f-ee23-4a31-8590-7639879870b4}'), pid=4)
WPD_CLIENT_INFORMATION_PROPERTIES_V1: Guid = Guid('{204d9f0c-2292-4080-9f42-40664e70f859}')
WPD_CLIENT_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=2)
WPD_CLIENT_MAJOR_VERSION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=3)
WPD_CLIENT_MINOR_VERSION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=4)
WPD_CLIENT_REVISION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=5)
WPD_CLIENT_WMDRM_APPLICATION_PRIVATE_KEY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=6)
WPD_CLIENT_WMDRM_APPLICATION_CERTIFICATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=7)
WPD_CLIENT_SECURITY_QUALITY_OF_SERVICE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=8)
WPD_CLIENT_DESIRED_ACCESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=9)
WPD_CLIENT_SHARE_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=10)
WPD_CLIENT_EVENT_COOKIE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=11)
WPD_CLIENT_MINIMUM_RESULTS_BUFFER_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=12)
WPD_CLIENT_MANUAL_CLOSE_ON_DISCONNECT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{204d9f0c-2292-4080-9f42-40664e70f859}'), pid=13)
WPD_PROPERTY_ATTRIBUTES_V1: Guid = Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}')
WPD_PROPERTY_ATTRIBUTE_FORM: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=2)
WPD_PROPERTY_ATTRIBUTE_CAN_READ: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=3)
WPD_PROPERTY_ATTRIBUTE_CAN_WRITE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=4)
WPD_PROPERTY_ATTRIBUTE_CAN_DELETE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=5)
WPD_PROPERTY_ATTRIBUTE_DEFAULT_VALUE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=6)
WPD_PROPERTY_ATTRIBUTE_FAST_PROPERTY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=7)
WPD_PROPERTY_ATTRIBUTE_RANGE_MIN: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=8)
WPD_PROPERTY_ATTRIBUTE_RANGE_MAX: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=9)
WPD_PROPERTY_ATTRIBUTE_RANGE_STEP: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=10)
WPD_PROPERTY_ATTRIBUTE_ENUMERATION_ELEMENTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=11)
WPD_PROPERTY_ATTRIBUTE_REGULAR_EXPRESSION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=12)
WPD_PROPERTY_ATTRIBUTE_MAX_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ab7943d8-6332-445f-a00d-8d5ef1e96f37}'), pid=13)
WPD_PROPERTY_ATTRIBUTES_V2: Guid = Guid('{5d9da160-74ae-43cc-85a9-fe555a80798e}')
WPD_PROPERTY_ATTRIBUTE_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{5d9da160-74ae-43cc-85a9-fe555a80798e}'), pid=2)
WPD_PROPERTY_ATTRIBUTE_VARTYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{5d9da160-74ae-43cc-85a9-fe555a80798e}'), pid=3)
WPD_CLASS_EXTENSION_OPTIONS_V1: Guid = Guid('{6309ffef-a87c-4ca7-8434-797576e40a96}')
WPD_CLASS_EXTENSION_OPTIONS_SUPPORTED_CONTENT_TYPES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{6309ffef-a87c-4ca7-8434-797576e40a96}'), pid=2)
WPD_CLASS_EXTENSION_OPTIONS_DONT_REGISTER_WPD_DEVICE_INTERFACE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{6309ffef-a87c-4ca7-8434-797576e40a96}'), pid=3)
WPD_CLASS_EXTENSION_OPTIONS_REGISTER_WPD_PRIVATE_DEVICE_INTERFACE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{6309ffef-a87c-4ca7-8434-797576e40a96}'), pid=4)
WPD_CLASS_EXTENSION_OPTIONS_V2: Guid = Guid('{3e3595da-4d71-49fe-a0b4-d4406c3ae93f}')
WPD_CLASS_EXTENSION_OPTIONS_MULTITRANSPORT_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3e3595da-4d71-49fe-a0b4-d4406c3ae93f}'), pid=2)
WPD_CLASS_EXTENSION_OPTIONS_DEVICE_IDENTIFICATION_VALUES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3e3595da-4d71-49fe-a0b4-d4406c3ae93f}'), pid=3)
WPD_CLASS_EXTENSION_OPTIONS_TRANSPORT_BANDWIDTH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3e3595da-4d71-49fe-a0b4-d4406c3ae93f}'), pid=4)
WPD_CLASS_EXTENSION_OPTIONS_V3: Guid = Guid('{65c160f8-1367-4ce2-939d-8310839f0d30}')
WPD_CLASS_EXTENSION_OPTIONS_SILENCE_AUTOPLAY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{65c160f8-1367-4ce2-939d-8310839f0d30}'), pid=2)
WPD_RESOURCE_ATTRIBUTES_V1: Guid = Guid('{1eb6f604-9278-429f-93cc-5bb8c06656b6}')
WPD_RESOURCE_ATTRIBUTE_TOTAL_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1eb6f604-9278-429f-93cc-5bb8c06656b6}'), pid=2)
WPD_RESOURCE_ATTRIBUTE_CAN_READ: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1eb6f604-9278-429f-93cc-5bb8c06656b6}'), pid=3)
WPD_RESOURCE_ATTRIBUTE_CAN_WRITE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1eb6f604-9278-429f-93cc-5bb8c06656b6}'), pid=4)
WPD_RESOURCE_ATTRIBUTE_CAN_DELETE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1eb6f604-9278-429f-93cc-5bb8c06656b6}'), pid=5)
WPD_RESOURCE_ATTRIBUTE_OPTIMAL_READ_BUFFER_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1eb6f604-9278-429f-93cc-5bb8c06656b6}'), pid=6)
WPD_RESOURCE_ATTRIBUTE_OPTIMAL_WRITE_BUFFER_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1eb6f604-9278-429f-93cc-5bb8c06656b6}'), pid=7)
WPD_RESOURCE_ATTRIBUTE_FORMAT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1eb6f604-9278-429f-93cc-5bb8c06656b6}'), pid=8)
WPD_RESOURCE_ATTRIBUTE_RESOURCE_KEY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1eb6f604-9278-429f-93cc-5bb8c06656b6}'), pid=9)
WPD_DEVICE_PROPERTIES_V1: Guid = Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}')
WPD_DEVICE_SYNC_PARTNER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=2)
WPD_DEVICE_FIRMWARE_VERSION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=3)
WPD_DEVICE_POWER_LEVEL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=4)
WPD_DEVICE_POWER_SOURCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=5)
WPD_DEVICE_PROTOCOL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=6)
WPD_DEVICE_MANUFACTURER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=7)
WPD_DEVICE_MODEL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=8)
WPD_DEVICE_SERIAL_NUMBER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=9)
WPD_DEVICE_SUPPORTS_NON_CONSUMABLE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=10)
WPD_DEVICE_DATETIME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=11)
WPD_DEVICE_FRIENDLY_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=12)
WPD_DEVICE_SUPPORTED_DRM_SCHEMES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=13)
WPD_DEVICE_SUPPORTED_FORMATS_ARE_ORDERED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=14)
WPD_DEVICE_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=15)
WPD_DEVICE_NETWORK_IDENTIFIER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{26d4979a-e643-4626-9e2b-736dc0c92fdc}'), pid=16)
WPD_DEVICE_PROPERTIES_V2: Guid = Guid('{463dd662-7fc4-4291-911c-7f4c9cca9799}')
WPD_DEVICE_FUNCTIONAL_UNIQUE_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{463dd662-7fc4-4291-911c-7f4c9cca9799}'), pid=2)
WPD_DEVICE_MODEL_UNIQUE_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{463dd662-7fc4-4291-911c-7f4c9cca9799}'), pid=3)
WPD_DEVICE_TRANSPORT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{463dd662-7fc4-4291-911c-7f4c9cca9799}'), pid=4)
WPD_DEVICE_USE_DEVICE_STAGE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{463dd662-7fc4-4291-911c-7f4c9cca9799}'), pid=5)
WPD_DEVICE_PROPERTIES_V3: Guid = Guid('{6c2b878c-c2ec-490d-b425-d7a75e23e5ed}')
WPD_DEVICE_EDP_IDENTITY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{6c2b878c-c2ec-490d-b425-d7a75e23e5ed}'), pid=1)
WPD_SERVICE_PROPERTIES_V1: Guid = Guid('{7510698a-cb54-481c-b8db-0d75c93f1c06}')
WPD_SERVICE_VERSION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7510698a-cb54-481c-b8db-0d75c93f1c06}'), pid=2)
WPD_EVENT_PROPERTIES_V1: Guid = Guid('{15ab1953-f817-4fef-a921-5676e838f6e0}')
WPD_EVENT_PARAMETER_PNP_DEVICE_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{15ab1953-f817-4fef-a921-5676e838f6e0}'), pid=2)
WPD_EVENT_PARAMETER_EVENT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{15ab1953-f817-4fef-a921-5676e838f6e0}'), pid=3)
WPD_EVENT_PARAMETER_OPERATION_STATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{15ab1953-f817-4fef-a921-5676e838f6e0}'), pid=4)
WPD_EVENT_PARAMETER_OPERATION_PROGRESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{15ab1953-f817-4fef-a921-5676e838f6e0}'), pid=5)
WPD_EVENT_PARAMETER_OBJECT_PARENT_PERSISTENT_UNIQUE_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{15ab1953-f817-4fef-a921-5676e838f6e0}'), pid=6)
WPD_EVENT_PARAMETER_OBJECT_CREATION_COOKIE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{15ab1953-f817-4fef-a921-5676e838f6e0}'), pid=7)
WPD_EVENT_PARAMETER_CHILD_HIERARCHY_CHANGED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{15ab1953-f817-4fef-a921-5676e838f6e0}'), pid=8)
WPD_EVENT_PROPERTIES_V2: Guid = Guid('{52807b8a-4914-4323-9b9a-74f654b2b846}')
WPD_EVENT_PARAMETER_SERVICE_METHOD_CONTEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{52807b8a-4914-4323-9b9a-74f654b2b846}'), pid=2)
WPD_EVENT_OPTIONS_V1: Guid = Guid('{b3d8dad7-a361-4b83-8a48-5b02ce10713b}')
WPD_EVENT_OPTION_IS_BROADCAST_EVENT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3d8dad7-a361-4b83-8a48-5b02ce10713b}'), pid=2)
WPD_EVENT_OPTION_IS_AUTOPLAY_EVENT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3d8dad7-a361-4b83-8a48-5b02ce10713b}'), pid=3)
WPD_EVENT_ATTRIBUTES_V1: Guid = Guid('{10c96578-2e81-4111-adde-e08ca6138f6d}')
WPD_EVENT_ATTRIBUTE_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{10c96578-2e81-4111-adde-e08ca6138f6d}'), pid=2)
WPD_EVENT_ATTRIBUTE_PARAMETERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{10c96578-2e81-4111-adde-e08ca6138f6d}'), pid=3)
WPD_EVENT_ATTRIBUTE_OPTIONS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{10c96578-2e81-4111-adde-e08ca6138f6d}'), pid=4)
WPD_API_OPTIONS_V1: Guid = Guid('{10e54a3e-052d-4777-a13c-de7614be2bc4}')
WPD_API_OPTION_USE_CLEAR_DATA_STREAM: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{10e54a3e-052d-4777-a13c-de7614be2bc4}'), pid=2)
WPD_API_OPTION_IOCTL_ACCESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{10e54a3e-052d-4777-a13c-de7614be2bc4}'), pid=3)
WPD_FORMAT_ATTRIBUTES_V1: Guid = Guid('{a0a02000-bcaf-4be8-b3f5-233f231cf58f}')
WPD_FORMAT_ATTRIBUTE_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{a0a02000-bcaf-4be8-b3f5-233f231cf58f}'), pid=2)
WPD_FORMAT_ATTRIBUTE_MIMETYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{a0a02000-bcaf-4be8-b3f5-233f231cf58f}'), pid=3)
WPD_METHOD_ATTRIBUTES_V1: Guid = Guid('{f17a5071-f039-44af-8efe-432cf32e432a}')
WPD_METHOD_ATTRIBUTE_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f17a5071-f039-44af-8efe-432cf32e432a}'), pid=2)
WPD_METHOD_ATTRIBUTE_ASSOCIATED_FORMAT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f17a5071-f039-44af-8efe-432cf32e432a}'), pid=3)
WPD_METHOD_ATTRIBUTE_ACCESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f17a5071-f039-44af-8efe-432cf32e432a}'), pid=4)
WPD_METHOD_ATTRIBUTE_PARAMETERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f17a5071-f039-44af-8efe-432cf32e432a}'), pid=5)
WPD_PARAMETER_ATTRIBUTES_V1: Guid = Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}')
WPD_PARAMETER_ATTRIBUTE_ORDER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=2)
WPD_PARAMETER_ATTRIBUTE_USAGE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=3)
WPD_PARAMETER_ATTRIBUTE_FORM: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=4)
WPD_PARAMETER_ATTRIBUTE_DEFAULT_VALUE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=5)
WPD_PARAMETER_ATTRIBUTE_RANGE_MIN: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=6)
WPD_PARAMETER_ATTRIBUTE_RANGE_MAX: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=7)
WPD_PARAMETER_ATTRIBUTE_RANGE_STEP: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=8)
WPD_PARAMETER_ATTRIBUTE_ENUMERATION_ELEMENTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=9)
WPD_PARAMETER_ATTRIBUTE_REGULAR_EXPRESSION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=10)
WPD_PARAMETER_ATTRIBUTE_MAX_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=11)
WPD_PARAMETER_ATTRIBUTE_VARTYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=12)
WPD_PARAMETER_ATTRIBUTE_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e6864dd7-f325-45ea-a1d5-97cf73b6ca58}'), pid=13)
WPD_CATEGORY_COMMON: Guid = Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}')
WPD_COMMAND_COMMON_RESET_DEVICE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=2)
WPD_COMMAND_COMMON_GET_OBJECT_IDS_FROM_PERSISTENT_UNIQUE_IDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=3)
WPD_COMMAND_COMMON_SAVE_CLIENT_INFORMATION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=4)
WPD_PROPERTY_COMMON_COMMAND_CATEGORY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=1001)
WPD_PROPERTY_COMMON_COMMAND_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=1002)
WPD_PROPERTY_COMMON_HRESULT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=1003)
WPD_PROPERTY_COMMON_DRIVER_ERROR_CODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=1004)
WPD_PROPERTY_COMMON_COMMAND_TARGET: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=1006)
WPD_PROPERTY_COMMON_PERSISTENT_UNIQUE_IDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=1007)
WPD_PROPERTY_COMMON_OBJECT_IDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=1008)
WPD_PROPERTY_COMMON_CLIENT_INFORMATION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=1009)
WPD_PROPERTY_COMMON_CLIENT_INFORMATION_CONTEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=1010)
WPD_PROPERTY_COMMON_ACTIVITY_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=1011)
WPD_OPTION_VALID_OBJECT_IDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f0422a9c-5dc8-4440-b5bd-5df28835658a}'), pid=5001)
WPD_CATEGORY_OBJECT_ENUMERATION: Guid = Guid('{b7474e91-e7f8-4ad9-b400-ad1a4b58eeec}')
WPD_COMMAND_OBJECT_ENUMERATION_START_FIND: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b7474e91-e7f8-4ad9-b400-ad1a4b58eeec}'), pid=2)
WPD_COMMAND_OBJECT_ENUMERATION_FIND_NEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b7474e91-e7f8-4ad9-b400-ad1a4b58eeec}'), pid=3)
WPD_COMMAND_OBJECT_ENUMERATION_END_FIND: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b7474e91-e7f8-4ad9-b400-ad1a4b58eeec}'), pid=4)
WPD_PROPERTY_OBJECT_ENUMERATION_PARENT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b7474e91-e7f8-4ad9-b400-ad1a4b58eeec}'), pid=1001)
WPD_PROPERTY_OBJECT_ENUMERATION_FILTER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b7474e91-e7f8-4ad9-b400-ad1a4b58eeec}'), pid=1002)
WPD_PROPERTY_OBJECT_ENUMERATION_OBJECT_IDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b7474e91-e7f8-4ad9-b400-ad1a4b58eeec}'), pid=1003)
WPD_PROPERTY_OBJECT_ENUMERATION_CONTEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b7474e91-e7f8-4ad9-b400-ad1a4b58eeec}'), pid=1004)
WPD_PROPERTY_OBJECT_ENUMERATION_NUM_OBJECTS_REQUESTED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b7474e91-e7f8-4ad9-b400-ad1a4b58eeec}'), pid=1005)
WPD_CATEGORY_OBJECT_PROPERTIES: Guid = Guid('{9e5582e4-0814-44e6-981a-b2998d583804}')
WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=2)
WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=3)
WPD_COMMAND_OBJECT_PROPERTIES_GET: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=4)
WPD_COMMAND_OBJECT_PROPERTIES_SET: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=5)
WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=6)
WPD_COMMAND_OBJECT_PROPERTIES_DELETE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=7)
WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=1001)
WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=1002)
WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=1003)
WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=1004)
WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=1005)
WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_DELETE_RESULTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{9e5582e4-0814-44e6-981a-b2998d583804}'), pid=1006)
WPD_CATEGORY_OBJECT_PROPERTIES_BULK: Guid = Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}')
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_START: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=2)
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_NEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=3)
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_END: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=4)
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_START: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=5)
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_NEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=6)
WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_END: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=7)
WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_START: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=8)
WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_NEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=9)
WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_END: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=10)
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_IDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=1001)
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=1002)
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_VALUES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=1003)
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PROPERTY_KEYS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=1004)
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_DEPTH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=1005)
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PARENT_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=1006)
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_FORMAT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=1007)
WPD_PROPERTY_OBJECT_PROPERTIES_BULK_WRITE_RESULTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{11c824dd-04cd-4e4e-8c7b-f6efb794d84e}'), pid=1008)
WPD_CATEGORY_OBJECT_RESOURCES: Guid = Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}')
WPD_COMMAND_OBJECT_RESOURCES_GET_SUPPORTED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=2)
WPD_COMMAND_OBJECT_RESOURCES_GET_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=3)
WPD_COMMAND_OBJECT_RESOURCES_OPEN: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=4)
WPD_COMMAND_OBJECT_RESOURCES_READ: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=5)
WPD_COMMAND_OBJECT_RESOURCES_WRITE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=6)
WPD_COMMAND_OBJECT_RESOURCES_CLOSE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=7)
WPD_COMMAND_OBJECT_RESOURCES_DELETE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=8)
WPD_COMMAND_OBJECT_RESOURCES_CREATE_RESOURCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=9)
WPD_COMMAND_OBJECT_RESOURCES_REVERT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=10)
WPD_COMMAND_OBJECT_RESOURCES_SEEK: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=11)
WPD_COMMAND_OBJECT_RESOURCES_COMMIT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=12)
WPD_COMMAND_OBJECT_RESOURCES_SEEK_IN_UNITS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=13)
WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1001)
WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1002)
WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1003)
WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1004)
WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1005)
WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_READ: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1006)
WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_READ: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1007)
WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_WRITE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1008)
WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_WRITTEN: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1009)
WPD_PROPERTY_OBJECT_RESOURCES_DATA: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1010)
WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1011)
WPD_PROPERTY_OBJECT_RESOURCES_SEEK_OFFSET: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1012)
WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1013)
WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1014)
WPD_PROPERTY_OBJECT_RESOURCES_SUPPORTS_UNITS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1015)
WPD_PROPERTY_OBJECT_RESOURCES_STREAM_UNITS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=1016)
WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_READ_SUPPORTED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=5001)
WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_WRITE_SUPPORTED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=5002)
WPD_OPTION_OBJECT_RESOURCES_NO_INPUT_BUFFER_ON_READ: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b3a2b22d-a595-4108-be0a-fc3c965f3d4a}'), pid=5003)
WPD_CATEGORY_OBJECT_MANAGEMENT: Guid = Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}')
WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_ONLY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=2)
WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_AND_DATA: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=3)
WPD_COMMAND_OBJECT_MANAGEMENT_WRITE_OBJECT_DATA: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=4)
WPD_COMMAND_OBJECT_MANAGEMENT_COMMIT_OBJECT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=5)
WPD_COMMAND_OBJECT_MANAGEMENT_REVERT_OBJECT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=6)
WPD_COMMAND_OBJECT_MANAGEMENT_DELETE_OBJECTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=7)
WPD_COMMAND_OBJECT_MANAGEMENT_MOVE_OBJECTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=8)
WPD_COMMAND_OBJECT_MANAGEMENT_COPY_OBJECTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=9)
WPD_COMMAND_OBJECT_MANAGEMENT_UPDATE_OBJECT_WITH_PROPERTIES_AND_DATA: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=10)
WPD_PROPERTY_OBJECT_MANAGEMENT_CREATION_PROPERTIES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1001)
WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1002)
WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_TO_WRITE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1003)
WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_WRITTEN: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1004)
WPD_PROPERTY_OBJECT_MANAGEMENT_DATA: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1005)
WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1006)
WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_OPTIONS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1007)
WPD_PROPERTY_OBJECT_MANAGEMENT_OPTIMAL_TRANSFER_BUFFER_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1008)
WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_IDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1009)
WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_RESULTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1010)
WPD_PROPERTY_OBJECT_MANAGEMENT_DESTINATION_FOLDER_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1011)
WPD_PROPERTY_OBJECT_MANAGEMENT_MOVE_RESULTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1012)
WPD_PROPERTY_OBJECT_MANAGEMENT_COPY_RESULTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1013)
WPD_PROPERTY_OBJECT_MANAGEMENT_UPDATE_PROPERTIES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1014)
WPD_PROPERTY_OBJECT_MANAGEMENT_PROPERTY_KEYS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1015)
WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_FORMAT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=1016)
WPD_OPTION_OBJECT_MANAGEMENT_RECURSIVE_DELETE_SUPPORTED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef1e43dd-a9ed-4341-8bcc-186192aea089}'), pid=5001)
WPD_CATEGORY_CAPABILITIES: Guid = Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}')
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=2)
WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=3)
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=4)
WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=5)
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=6)
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=7)
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=8)
WPD_COMMAND_CAPABILITIES_GET_FIXED_PROPERTY_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=9)
WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=10)
WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=11)
WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1001)
WPD_PROPERTY_CAPABILITIES_COMMAND: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1002)
WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1003)
WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1004)
WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1005)
WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1006)
WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1007)
WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1008)
WPD_PROPERTY_CAPABILITIES_FORMATS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1009)
WPD_PROPERTY_CAPABILITIES_FORMAT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1010)
WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1011)
WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1012)
WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1013)
WPD_PROPERTY_CAPABILITIES_EVENT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1014)
WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0cabec78-6b74-41c6-9216-2639d1fce356}'), pid=1015)
WPD_CATEGORY_STORAGE: Guid = Guid('{d8f907a6-34cc-45fa-97fb-d007fa47ec94}')
WPD_COMMAND_STORAGE_FORMAT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d8f907a6-34cc-45fa-97fb-d007fa47ec94}'), pid=2)
WPD_COMMAND_STORAGE_EJECT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d8f907a6-34cc-45fa-97fb-d007fa47ec94}'), pid=4)
WPD_PROPERTY_STORAGE_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d8f907a6-34cc-45fa-97fb-d007fa47ec94}'), pid=1001)
WPD_PROPERTY_STORAGE_DESTINATION_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d8f907a6-34cc-45fa-97fb-d007fa47ec94}'), pid=1002)
WPD_CATEGORY_SMS: Guid = Guid('{afc25d66-fe0d-4114-9097-970c93e920d1}')
WPD_COMMAND_SMS_SEND: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{afc25d66-fe0d-4114-9097-970c93e920d1}'), pid=2)
WPD_PROPERTY_SMS_RECIPIENT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{afc25d66-fe0d-4114-9097-970c93e920d1}'), pid=1001)
WPD_PROPERTY_SMS_MESSAGE_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{afc25d66-fe0d-4114-9097-970c93e920d1}'), pid=1002)
WPD_PROPERTY_SMS_TEXT_MESSAGE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{afc25d66-fe0d-4114-9097-970c93e920d1}'), pid=1003)
WPD_PROPERTY_SMS_BINARY_MESSAGE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{afc25d66-fe0d-4114-9097-970c93e920d1}'), pid=1004)
WPD_OPTION_SMS_BINARY_MESSAGE_SUPPORTED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{afc25d66-fe0d-4114-9097-970c93e920d1}'), pid=5001)
WPD_CATEGORY_STILL_IMAGE_CAPTURE: Guid = Guid('{4fcd6982-22a2-4b05-a48b-62d38bf27b32}')
WPD_COMMAND_STILL_IMAGE_CAPTURE_INITIATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4fcd6982-22a2-4b05-a48b-62d38bf27b32}'), pid=2)
WPD_CATEGORY_MEDIA_CAPTURE: Guid = Guid('{59b433ba-fe44-4d8d-808c-6bcb9b0f15e8}')
WPD_COMMAND_MEDIA_CAPTURE_START: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{59b433ba-fe44-4d8d-808c-6bcb9b0f15e8}'), pid=2)
WPD_COMMAND_MEDIA_CAPTURE_STOP: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{59b433ba-fe44-4d8d-808c-6bcb9b0f15e8}'), pid=3)
WPD_COMMAND_MEDIA_CAPTURE_PAUSE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{59b433ba-fe44-4d8d-808c-6bcb9b0f15e8}'), pid=4)
WPD_CATEGORY_DEVICE_HINTS: Guid = Guid('{0d5fb92b-cb46-4c4f-8343-0bc3d3f17c84}')
WPD_COMMAND_DEVICE_HINTS_GET_CONTENT_LOCATION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0d5fb92b-cb46-4c4f-8343-0bc3d3f17c84}'), pid=2)
WPD_PROPERTY_DEVICE_HINTS_CONTENT_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0d5fb92b-cb46-4c4f-8343-0bc3d3f17c84}'), pid=1001)
WPD_PROPERTY_DEVICE_HINTS_CONTENT_LOCATIONS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{0d5fb92b-cb46-4c4f-8343-0bc3d3f17c84}'), pid=1002)
WPD_CLASS_EXTENSION_V1: Guid = Guid('{33fb0d11-64a3-4fac-b4c7-3dfeaa99b051}')
WPD_COMMAND_CLASS_EXTENSION_WRITE_DEVICE_INFORMATION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{33fb0d11-64a3-4fac-b4c7-3dfeaa99b051}'), pid=2)
WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_VALUES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{33fb0d11-64a3-4fac-b4c7-3dfeaa99b051}'), pid=1001)
WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_WRITE_RESULTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{33fb0d11-64a3-4fac-b4c7-3dfeaa99b051}'), pid=1002)
WPD_CLASS_EXTENSION_V2: Guid = Guid('{7f0779b5-fa2b-4766-9cb2-f73ba30b6758}')
WPD_COMMAND_CLASS_EXTENSION_REGISTER_SERVICE_INTERFACES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f0779b5-fa2b-4766-9cb2-f73ba30b6758}'), pid=2)
WPD_COMMAND_CLASS_EXTENSION_UNREGISTER_SERVICE_INTERFACES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f0779b5-fa2b-4766-9cb2-f73ba30b6758}'), pid=3)
WPD_PROPERTY_CLASS_EXTENSION_SERVICE_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f0779b5-fa2b-4766-9cb2-f73ba30b6758}'), pid=1001)
WPD_PROPERTY_CLASS_EXTENSION_SERVICE_INTERFACES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f0779b5-fa2b-4766-9cb2-f73ba30b6758}'), pid=1002)
WPD_PROPERTY_CLASS_EXTENSION_SERVICE_REGISTRATION_RESULTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f0779b5-fa2b-4766-9cb2-f73ba30b6758}'), pid=1003)
WPD_CATEGORY_NETWORK_CONFIGURATION: Guid = Guid('{78f9c6fc-79b8-473c-9060-6bd23dd072c4}')
WPD_COMMAND_GENERATE_KEYPAIR: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{78f9c6fc-79b8-473c-9060-6bd23dd072c4}'), pid=2)
WPD_COMMAND_COMMIT_KEYPAIR: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{78f9c6fc-79b8-473c-9060-6bd23dd072c4}'), pid=3)
WPD_COMMAND_PROCESS_WIRELESS_PROFILE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{78f9c6fc-79b8-473c-9060-6bd23dd072c4}'), pid=4)
WPD_PROPERTY_PUBLIC_KEY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{78f9c6fc-79b8-473c-9060-6bd23dd072c4}'), pid=1001)
WPD_CATEGORY_SERVICE_COMMON: Guid = Guid('{322f071d-36ef-477f-b4b5-6f52d734baee}')
WPD_COMMAND_SERVICE_COMMON_GET_SERVICE_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{322f071d-36ef-477f-b4b5-6f52d734baee}'), pid=2)
WPD_PROPERTY_SERVICE_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{322f071d-36ef-477f-b4b5-6f52d734baee}'), pid=1001)
WPD_CATEGORY_SERVICE_CAPABILITIES: Guid = Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}')
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=2)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS_BY_FORMAT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=3)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=4)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_PARAMETER_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=5)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMATS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=6)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=7)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=8)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_PROPERTY_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=9)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_EVENTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=10)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=11)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_PARAMETER_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=12)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_INHERITED_SERVICES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=13)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_RENDERING_PROFILES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=14)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_COMMANDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=15)
WPD_COMMAND_SERVICE_CAPABILITIES_GET_COMMAND_OPTIONS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=16)
WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_METHODS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1001)
WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1002)
WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1003)
WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1004)
WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1005)
WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1006)
WPD_PROPERTY_SERVICE_CAPABILITIES_FORMATS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1007)
WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1008)
WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_KEYS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1009)
WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1010)
WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_EVENTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1011)
WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1012)
WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT_ATTRIBUTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1013)
WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITANCE_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1014)
WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITED_SERVICES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1015)
WPD_PROPERTY_SERVICE_CAPABILITIES_RENDERING_PROFILES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1016)
WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_COMMANDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1017)
WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1018)
WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND_OPTIONS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{24457e74-2e9f-44f9-8c57-1d1bcb170b89}'), pid=1019)
WPD_CATEGORY_SERVICE_METHODS: Guid = Guid('{2d521ca8-c1b0-4268-a342-cf19321569bc}')
WPD_COMMAND_SERVICE_METHODS_START_INVOKE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2d521ca8-c1b0-4268-a342-cf19321569bc}'), pid=2)
WPD_COMMAND_SERVICE_METHODS_CANCEL_INVOKE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2d521ca8-c1b0-4268-a342-cf19321569bc}'), pid=3)
WPD_COMMAND_SERVICE_METHODS_END_INVOKE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2d521ca8-c1b0-4268-a342-cf19321569bc}'), pid=4)
WPD_PROPERTY_SERVICE_METHOD: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2d521ca8-c1b0-4268-a342-cf19321569bc}'), pid=1001)
WPD_PROPERTY_SERVICE_METHOD_PARAMETER_VALUES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2d521ca8-c1b0-4268-a342-cf19321569bc}'), pid=1002)
WPD_PROPERTY_SERVICE_METHOD_RESULT_VALUES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2d521ca8-c1b0-4268-a342-cf19321569bc}'), pid=1003)
WPD_PROPERTY_SERVICE_METHOD_CONTEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2d521ca8-c1b0-4268-a342-cf19321569bc}'), pid=1004)
WPD_PROPERTY_SERVICE_METHOD_HRESULT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2d521ca8-c1b0-4268-a342-cf19321569bc}'), pid=1005)
WPD_RESOURCE_DEFAULT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e81e79be-34f0-41bf-b53f-f1a06ae87842}'), pid=0)
WPD_RESOURCE_CONTACT_PHOTO: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2c4d6803-80ea-4580-af9a-5be1a23eddcb}'), pid=0)
WPD_RESOURCE_THUMBNAIL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{c7c407ba-98fa-46b5-9960-23fec124cfde}'), pid=0)
WPD_RESOURCE_ICON: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f195fed8-aa28-4ee3-b153-e182dd5edc39}'), pid=0)
WPD_RESOURCE_AUDIO_CLIP: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3bc13982-85b1-48e0-95a6-8d3ad06be117}'), pid=0)
WPD_RESOURCE_ALBUM_ART: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f02aa354-2300-4e2d-a1b9-3b6730f7fa21}'), pid=0)
WPD_RESOURCE_GENERIC: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b9b9f515-ba70-4647-94dc-fa4925e95a07}'), pid=0)
WPD_RESOURCE_VIDEO_CLIP: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b566ee42-6368-4290-8662-70182fb79f20}'), pid=0)
WPD_RESOURCE_BRANDING_ART: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b633b1ae-6caf-4a87-9589-22ded6dd5899}'), pid=0)
WPD_OBJECT_FORMAT_PROPERTIES_ONLY: Guid = Guid('{30010000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_UNSPECIFIED: Guid = Guid('{30000000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_SCRIPT: Guid = Guid('{30020000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_EXECUTABLE: Guid = Guid('{30030000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_TEXT: Guid = Guid('{30040000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_HTML: Guid = Guid('{30050000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_DPOF: Guid = Guid('{30060000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_AIFF: Guid = Guid('{30070000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_WAVE: Guid = Guid('{30080000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_MP3: Guid = Guid('{30090000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_AVI: Guid = Guid('{300a0000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_MPEG: Guid = Guid('{300b0000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_ASF: Guid = Guid('{300c0000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_EXIF: Guid = Guid('{38010000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_TIFFEP: Guid = Guid('{38020000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_FLASHPIX: Guid = Guid('{38030000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_BMP: Guid = Guid('{38040000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_CIFF: Guid = Guid('{38050000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_GIF: Guid = Guid('{38070000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_JFIF: Guid = Guid('{38080000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_PCD: Guid = Guid('{38090000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_PICT: Guid = Guid('{380a0000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_PNG: Guid = Guid('{380b0000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_TIFF: Guid = Guid('{380d0000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_TIFFIT: Guid = Guid('{380e0000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_JP2: Guid = Guid('{380f0000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_JPX: Guid = Guid('{38100000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_WBMP: Guid = Guid('{b8030000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_JPEGXR: Guid = Guid('{b8040000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_WINDOWSIMAGEFORMAT: Guid = Guid('{b8810000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_WMA: Guid = Guid('{b9010000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_WMV: Guid = Guid('{b9810000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_WPLPLAYLIST: Guid = Guid('{ba100000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_M3UPLAYLIST: Guid = Guid('{ba110000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_MPLPLAYLIST: Guid = Guid('{ba120000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_ASXPLAYLIST: Guid = Guid('{ba130000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_PLSPLAYLIST: Guid = Guid('{ba140000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_ABSTRACT_CONTACT_GROUP: Guid = Guid('{ba060000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_ABSTRACT_MEDIA_CAST: Guid = Guid('{ba0b0000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_VCALENDAR1: Guid = Guid('{be020000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_ICALENDAR: Guid = Guid('{be030000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_ABSTRACT_CONTACT: Guid = Guid('{bb810000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_VCARD2: Guid = Guid('{bb820000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_VCARD3: Guid = Guid('{bb830000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_XML: Guid = Guid('{ba820000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_AAC: Guid = Guid('{b9030000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_AUDIBLE: Guid = Guid('{b9040000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_FLAC: Guid = Guid('{b9060000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_QCELP: Guid = Guid('{b9070000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_AMR: Guid = Guid('{b9080000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_OGG: Guid = Guid('{b9020000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_MP4: Guid = Guid('{b9820000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_MP2: Guid = Guid('{b9830000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_MICROSOFT_WORD: Guid = Guid('{ba830000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_MHT_COMPILED_HTML: Guid = Guid('{ba840000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_MICROSOFT_EXCEL: Guid = Guid('{ba850000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_MICROSOFT_POWERPOINT: Guid = Guid('{ba860000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_3GP: Guid = Guid('{b9840000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_3G2: Guid = Guid('{b9850000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_AVCHD: Guid = Guid('{b9860000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_ATSCTS: Guid = Guid('{b9870000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_DVBTS: Guid = Guid('{b9880000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_FORMAT_MKV: Guid = Guid('{b9900000-ae6c-4804-98ba-c57b46965fe7}')
WPD_OBJECT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=2)
WPD_OBJECT_PARENT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=3)
WPD_OBJECT_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=4)
WPD_OBJECT_PERSISTENT_UNIQUE_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=5)
WPD_OBJECT_FORMAT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=6)
WPD_OBJECT_ISHIDDEN: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=9)
WPD_OBJECT_ISSYSTEM: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=10)
WPD_OBJECT_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=11)
WPD_OBJECT_ORIGINAL_FILE_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=12)
WPD_OBJECT_NON_CONSUMABLE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=13)
WPD_OBJECT_KEYWORDS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=15)
WPD_OBJECT_SYNC_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=16)
WPD_OBJECT_IS_DRM_PROTECTED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=17)
WPD_OBJECT_DATE_CREATED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=18)
WPD_OBJECT_DATE_MODIFIED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=19)
WPD_OBJECT_DATE_AUTHORED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=20)
WPD_OBJECT_BACK_REFERENCES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=21)
WPD_OBJECT_CAN_DELETE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=26)
WPD_OBJECT_LANGUAGE_LOCALE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{ef6b490d-5cd8-437a-affc-da8b60ee4a3c}'), pid=27)
WPD_FOLDER_OBJECT_PROPERTIES_V1: Guid = Guid('{7e9a7abf-e568-4b34-aa2f-13bb12ab177d}')
WPD_FOLDER_CONTENT_TYPES_ALLOWED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7e9a7abf-e568-4b34-aa2f-13bb12ab177d}'), pid=2)
WPD_IMAGE_OBJECT_PROPERTIES_V1: Guid = Guid('{63d64908-9fa1-479f-85ba-9952216447db}')
WPD_IMAGE_BITDEPTH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{63d64908-9fa1-479f-85ba-9952216447db}'), pid=3)
WPD_IMAGE_CROPPED_STATUS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{63d64908-9fa1-479f-85ba-9952216447db}'), pid=4)
WPD_IMAGE_COLOR_CORRECTED_STATUS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{63d64908-9fa1-479f-85ba-9952216447db}'), pid=5)
WPD_IMAGE_FNUMBER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{63d64908-9fa1-479f-85ba-9952216447db}'), pid=6)
WPD_IMAGE_EXPOSURE_TIME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{63d64908-9fa1-479f-85ba-9952216447db}'), pid=7)
WPD_IMAGE_EXPOSURE_INDEX: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{63d64908-9fa1-479f-85ba-9952216447db}'), pid=8)
WPD_IMAGE_HORIZONTAL_RESOLUTION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{63d64908-9fa1-479f-85ba-9952216447db}'), pid=9)
WPD_IMAGE_VERTICAL_RESOLUTION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{63d64908-9fa1-479f-85ba-9952216447db}'), pid=10)
WPD_DOCUMENT_OBJECT_PROPERTIES_V1: Guid = Guid('{0b110203-eb95-4f02-93e0-97c631493ad5}')
WPD_MEDIA_PROPERTIES_V1: Guid = Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}')
WPD_MEDIA_TOTAL_BITRATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=2)
WPD_MEDIA_BITRATE_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=3)
WPD_MEDIA_COPYRIGHT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=4)
WPD_MEDIA_SUBSCRIPTION_CONTENT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=5)
WPD_MEDIA_USE_COUNT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=6)
WPD_MEDIA_SKIP_COUNT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=7)
WPD_MEDIA_LAST_ACCESSED_TIME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=8)
WPD_MEDIA_PARENTAL_RATING: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=9)
WPD_MEDIA_META_GENRE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=10)
WPD_MEDIA_COMPOSER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=11)
WPD_MEDIA_EFFECTIVE_RATING: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=12)
WPD_MEDIA_SUB_TITLE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=13)
WPD_MEDIA_RELEASE_DATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=14)
WPD_MEDIA_SAMPLE_RATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=15)
WPD_MEDIA_STAR_RATING: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=16)
WPD_MEDIA_USER_EFFECTIVE_RATING: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=17)
WPD_MEDIA_TITLE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=18)
WPD_MEDIA_DURATION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=19)
WPD_MEDIA_BUY_NOW: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=20)
WPD_MEDIA_ENCODING_PROFILE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=21)
WPD_MEDIA_WIDTH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=22)
WPD_MEDIA_HEIGHT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=23)
WPD_MEDIA_ARTIST: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=24)
WPD_MEDIA_ALBUM_ARTIST: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=25)
WPD_MEDIA_OWNER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=26)
WPD_MEDIA_MANAGING_EDITOR: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=27)
WPD_MEDIA_WEBMASTER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=28)
WPD_MEDIA_SOURCE_URL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=29)
WPD_MEDIA_DESTINATION_URL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=30)
WPD_MEDIA_DESCRIPTION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=31)
WPD_MEDIA_GENRE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=32)
WPD_MEDIA_TIME_BOOKMARK: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=33)
WPD_MEDIA_OBJECT_BOOKMARK: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=34)
WPD_MEDIA_LAST_BUILD_DATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=35)
WPD_MEDIA_BYTE_BOOKMARK: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=36)
WPD_MEDIA_TIME_TO_LIVE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=37)
WPD_MEDIA_GUID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=38)
WPD_MEDIA_SUB_DESCRIPTION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=39)
WPD_MEDIA_AUDIO_ENCODING_PROFILE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2ed8ba05-0ad3-42dc-b0d0-bc95ac396ac8}'), pid=49)
WPD_CONTACT_OBJECT_PROPERTIES_V1: Guid = Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}')
WPD_CONTACT_DISPLAY_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=2)
WPD_CONTACT_FIRST_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=3)
WPD_CONTACT_MIDDLE_NAMES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=4)
WPD_CONTACT_LAST_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=5)
WPD_CONTACT_PREFIX: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=6)
WPD_CONTACT_SUFFIX: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=7)
WPD_CONTACT_PHONETIC_FIRST_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=8)
WPD_CONTACT_PHONETIC_LAST_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=9)
WPD_CONTACT_PERSONAL_FULL_POSTAL_ADDRESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=10)
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE1: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=11)
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE2: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=12)
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_CITY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=13)
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_REGION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=14)
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_POSTAL_CODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=15)
WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_COUNTRY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=16)
WPD_CONTACT_BUSINESS_FULL_POSTAL_ADDRESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=17)
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE1: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=18)
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE2: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=19)
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_CITY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=20)
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_REGION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=21)
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_POSTAL_CODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=22)
WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_COUNTRY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=23)
WPD_CONTACT_OTHER_FULL_POSTAL_ADDRESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=24)
WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE1: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=25)
WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE2: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=26)
WPD_CONTACT_OTHER_POSTAL_ADDRESS_CITY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=27)
WPD_CONTACT_OTHER_POSTAL_ADDRESS_REGION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=28)
WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_CODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=29)
WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_COUNTRY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=30)
WPD_CONTACT_PRIMARY_EMAIL_ADDRESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=31)
WPD_CONTACT_PERSONAL_EMAIL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=32)
WPD_CONTACT_PERSONAL_EMAIL2: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=33)
WPD_CONTACT_BUSINESS_EMAIL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=34)
WPD_CONTACT_BUSINESS_EMAIL2: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=35)
WPD_CONTACT_OTHER_EMAILS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=36)
WPD_CONTACT_PRIMARY_PHONE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=37)
WPD_CONTACT_PERSONAL_PHONE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=38)
WPD_CONTACT_PERSONAL_PHONE2: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=39)
WPD_CONTACT_BUSINESS_PHONE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=40)
WPD_CONTACT_BUSINESS_PHONE2: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=41)
WPD_CONTACT_MOBILE_PHONE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=42)
WPD_CONTACT_MOBILE_PHONE2: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=43)
WPD_CONTACT_PERSONAL_FAX: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=44)
WPD_CONTACT_BUSINESS_FAX: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=45)
WPD_CONTACT_PAGER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=46)
WPD_CONTACT_OTHER_PHONES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=47)
WPD_CONTACT_PRIMARY_WEB_ADDRESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=48)
WPD_CONTACT_PERSONAL_WEB_ADDRESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=49)
WPD_CONTACT_BUSINESS_WEB_ADDRESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=50)
WPD_CONTACT_INSTANT_MESSENGER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=51)
WPD_CONTACT_INSTANT_MESSENGER2: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=52)
WPD_CONTACT_INSTANT_MESSENGER3: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=53)
WPD_CONTACT_COMPANY_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=54)
WPD_CONTACT_PHONETIC_COMPANY_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=55)
WPD_CONTACT_ROLE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=56)
WPD_CONTACT_BIRTHDATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=57)
WPD_CONTACT_PRIMARY_FAX: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=58)
WPD_CONTACT_SPOUSE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=59)
WPD_CONTACT_CHILDREN: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=60)
WPD_CONTACT_ASSISTANT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=61)
WPD_CONTACT_ANNIVERSARY_DATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=62)
WPD_CONTACT_RINGTONE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{fbd4fdab-987d-4777-b3f9-726185a9312b}'), pid=63)
WPD_MUSIC_OBJECT_PROPERTIES_V1: Guid = Guid('{b324f56a-dc5d-46e5-b6df-d2ea414888c6}')
WPD_MUSIC_ALBUM: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b324f56a-dc5d-46e5-b6df-d2ea414888c6}'), pid=3)
WPD_MUSIC_TRACK: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b324f56a-dc5d-46e5-b6df-d2ea414888c6}'), pid=4)
WPD_MUSIC_LYRICS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b324f56a-dc5d-46e5-b6df-d2ea414888c6}'), pid=6)
WPD_MUSIC_MOOD: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b324f56a-dc5d-46e5-b6df-d2ea414888c6}'), pid=8)
WPD_AUDIO_BITRATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b324f56a-dc5d-46e5-b6df-d2ea414888c6}'), pid=9)
WPD_AUDIO_CHANNEL_COUNT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b324f56a-dc5d-46e5-b6df-d2ea414888c6}'), pid=10)
WPD_AUDIO_FORMAT_CODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b324f56a-dc5d-46e5-b6df-d2ea414888c6}'), pid=11)
WPD_AUDIO_BIT_DEPTH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b324f56a-dc5d-46e5-b6df-d2ea414888c6}'), pid=12)
WPD_AUDIO_BLOCK_ALIGNMENT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b324f56a-dc5d-46e5-b6df-d2ea414888c6}'), pid=13)
WPD_VIDEO_OBJECT_PROPERTIES_V1: Guid = Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}')
WPD_VIDEO_AUTHOR: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=2)
WPD_VIDEO_RECORDEDTV_STATION_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=4)
WPD_VIDEO_RECORDEDTV_CHANNEL_NUMBER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=5)
WPD_VIDEO_RECORDEDTV_REPEAT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=7)
WPD_VIDEO_BUFFER_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=8)
WPD_VIDEO_CREDITS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=9)
WPD_VIDEO_KEY_FRAME_DISTANCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=10)
WPD_VIDEO_QUALITY_SETTING: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=11)
WPD_VIDEO_SCAN_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=12)
WPD_VIDEO_BITRATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=13)
WPD_VIDEO_FOURCC_CODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=14)
WPD_VIDEO_FRAMERATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{346f2163-f998-4146-8b01-d19b4c00de9a}'), pid=15)
WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1: Guid = Guid('{b28ae94b-05a4-4e8e-be01-72cc7e099d8f}')
WPD_COMMON_INFORMATION_SUBJECT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b28ae94b-05a4-4e8e-be01-72cc7e099d8f}'), pid=2)
WPD_COMMON_INFORMATION_BODY_TEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b28ae94b-05a4-4e8e-be01-72cc7e099d8f}'), pid=3)
WPD_COMMON_INFORMATION_PRIORITY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b28ae94b-05a4-4e8e-be01-72cc7e099d8f}'), pid=4)
WPD_COMMON_INFORMATION_START_DATETIME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b28ae94b-05a4-4e8e-be01-72cc7e099d8f}'), pid=5)
WPD_COMMON_INFORMATION_END_DATETIME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b28ae94b-05a4-4e8e-be01-72cc7e099d8f}'), pid=6)
WPD_COMMON_INFORMATION_NOTES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b28ae94b-05a4-4e8e-be01-72cc7e099d8f}'), pid=7)
WPD_MEMO_OBJECT_PROPERTIES_V1: Guid = Guid('{5ffbfc7b-7483-41ad-afb9-da3f4e592b8d}')
WPD_EMAIL_OBJECT_PROPERTIES_V1: Guid = Guid('{41f8f65a-5484-4782-b13d-4740dd7c37c5}')
WPD_EMAIL_TO_LINE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{41f8f65a-5484-4782-b13d-4740dd7c37c5}'), pid=2)
WPD_EMAIL_CC_LINE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{41f8f65a-5484-4782-b13d-4740dd7c37c5}'), pid=3)
WPD_EMAIL_BCC_LINE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{41f8f65a-5484-4782-b13d-4740dd7c37c5}'), pid=4)
WPD_EMAIL_HAS_BEEN_READ: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{41f8f65a-5484-4782-b13d-4740dd7c37c5}'), pid=7)
WPD_EMAIL_RECEIVED_TIME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{41f8f65a-5484-4782-b13d-4740dd7c37c5}'), pid=8)
WPD_EMAIL_HAS_ATTACHMENTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{41f8f65a-5484-4782-b13d-4740dd7c37c5}'), pid=9)
WPD_EMAIL_SENDER_ADDRESS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{41f8f65a-5484-4782-b13d-4740dd7c37c5}'), pid=10)
WPD_APPOINTMENT_OBJECT_PROPERTIES_V1: Guid = Guid('{f99efd03-431d-40d8-a1c9-4e220d9c88d3}')
WPD_APPOINTMENT_LOCATION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f99efd03-431d-40d8-a1c9-4e220d9c88d3}'), pid=3)
WPD_APPOINTMENT_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f99efd03-431d-40d8-a1c9-4e220d9c88d3}'), pid=7)
WPD_APPOINTMENT_REQUIRED_ATTENDEES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f99efd03-431d-40d8-a1c9-4e220d9c88d3}'), pid=8)
WPD_APPOINTMENT_OPTIONAL_ATTENDEES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f99efd03-431d-40d8-a1c9-4e220d9c88d3}'), pid=9)
WPD_APPOINTMENT_ACCEPTED_ATTENDEES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f99efd03-431d-40d8-a1c9-4e220d9c88d3}'), pid=10)
WPD_APPOINTMENT_RESOURCES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f99efd03-431d-40d8-a1c9-4e220d9c88d3}'), pid=11)
WPD_APPOINTMENT_TENTATIVE_ATTENDEES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f99efd03-431d-40d8-a1c9-4e220d9c88d3}'), pid=12)
WPD_APPOINTMENT_DECLINED_ATTENDEES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f99efd03-431d-40d8-a1c9-4e220d9c88d3}'), pid=13)
WPD_TASK_OBJECT_PROPERTIES_V1: Guid = Guid('{e354e95e-d8a0-4637-a03a-0cb26838dbc7}')
WPD_TASK_STATUS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e354e95e-d8a0-4637-a03a-0cb26838dbc7}'), pid=6)
WPD_TASK_PERCENT_COMPLETE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e354e95e-d8a0-4637-a03a-0cb26838dbc7}'), pid=8)
WPD_TASK_REMINDER_DATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e354e95e-d8a0-4637-a03a-0cb26838dbc7}'), pid=10)
WPD_TASK_OWNER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e354e95e-d8a0-4637-a03a-0cb26838dbc7}'), pid=11)
WPD_SMS_OBJECT_PROPERTIES_V1: Guid = Guid('{7e1074cc-50ff-4dd1-a742-53be6f093a0d}')
WPD_SMS_PROVIDER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7e1074cc-50ff-4dd1-a742-53be6f093a0d}'), pid=2)
WPD_SMS_TIMEOUT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7e1074cc-50ff-4dd1-a742-53be6f093a0d}'), pid=3)
WPD_SMS_MAX_PAYLOAD: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7e1074cc-50ff-4dd1-a742-53be6f093a0d}'), pid=4)
WPD_SMS_ENCODING: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7e1074cc-50ff-4dd1-a742-53be6f093a0d}'), pid=5)
WPD_SECTION_OBJECT_PROPERTIES_V1: Guid = Guid('{516afd2b-c64e-44f0-98dc-bee1c88f7d66}')
WPD_SECTION_DATA_OFFSET: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{516afd2b-c64e-44f0-98dc-bee1c88f7d66}'), pid=2)
WPD_SECTION_DATA_LENGTH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{516afd2b-c64e-44f0-98dc-bee1c88f7d66}'), pid=3)
WPD_SECTION_DATA_UNITS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{516afd2b-c64e-44f0-98dc-bee1c88f7d66}'), pid=4)
WPD_SECTION_DATA_REFERENCED_OBJECT_RESOURCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{516afd2b-c64e-44f0-98dc-bee1c88f7d66}'), pid=5)
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
WPD_CATEGORY_MTP_EXT_VENDOR_OPERATIONS: Guid = Guid('{4d545058-1a2e-4106-a357-771e0819fc56}')
WPD_COMMAND_MTP_EXT_GET_SUPPORTED_VENDOR_OPCODES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=11)
WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITHOUT_DATA_PHASE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=12)
WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITH_DATA_TO_READ: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=13)
WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITH_DATA_TO_WRITE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=14)
WPD_COMMAND_MTP_EXT_READ_DATA: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=15)
WPD_COMMAND_MTP_EXT_WRITE_DATA: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=16)
WPD_COMMAND_MTP_EXT_END_DATA_TRANSFER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=17)
WPD_COMMAND_MTP_EXT_GET_VENDOR_EXTENSION_DESCRIPTION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=18)
WPD_PROPERTY_MTP_EXT_OPERATION_CODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1001)
WPD_PROPERTY_MTP_EXT_OPERATION_PARAMS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1002)
WPD_PROPERTY_MTP_EXT_RESPONSE_CODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1003)
WPD_PROPERTY_MTP_EXT_RESPONSE_PARAMS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1004)
WPD_PROPERTY_MTP_EXT_VENDOR_OPERATION_CODES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1005)
WPD_PROPERTY_MTP_EXT_TRANSFER_CONTEXT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1006)
WPD_PROPERTY_MTP_EXT_TRANSFER_TOTAL_DATA_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1007)
WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_TO_READ: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1008)
WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_READ: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1009)
WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_TO_WRITE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1010)
WPD_PROPERTY_MTP_EXT_TRANSFER_NUM_BYTES_WRITTEN: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1011)
WPD_PROPERTY_MTP_EXT_TRANSFER_DATA: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1012)
WPD_PROPERTY_MTP_EXT_OPTIMAL_TRANSFER_BUFFER_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1013)
WPD_PROPERTY_MTP_EXT_VENDOR_EXTENSION_DESCRIPTION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-1a2e-4106-a357-771e0819fc56}'), pid=1014)
WPD_PROPERTIES_MTP_VENDOR_EXTENDED_OBJECT_PROPS: Guid = Guid('{4d545058-4fce-4578-95c8-8698a9bc0f49}')
WPD_PROPERTIES_MTP_VENDOR_EXTENDED_DEVICE_PROPS: Guid = Guid('{4d545058-8900-40b3-8f1d-dc246e1e8370}')
WPD_EVENT_MTP_VENDOR_EXTENDED_EVENTS: Guid = Guid('{00000000-5738-4ff2-8445-be3126691059}')
WPD_PROPERTY_MTP_EXT_EVENT_PARAMS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{4d545058-ef88-4e4d-95c3-4f327f728a96}'), pid=1011)
CLSID_WPD_NAMESPACE_EXTENSION: Guid = Guid('{35786d3c-b075-49b9-88dd-029876e11c01}')
WPDNSE_OBJECT_PROPERTIES_V1: Guid = Guid('{34d71409-4b47-4d80-aaac-3a28a4a3b3e6}')
WPDNSE_OBJECT_HAS_CONTACT_PHOTO: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{34d71409-4b47-4d80-aaac-3a28a4a3b3e6}'), pid=2)
WPDNSE_OBJECT_HAS_THUMBNAIL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{34d71409-4b47-4d80-aaac-3a28a4a3b3e6}'), pid=3)
WPDNSE_OBJECT_HAS_ICON: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{34d71409-4b47-4d80-aaac-3a28a4a3b3e6}'), pid=4)
WPDNSE_OBJECT_HAS_AUDIO_CLIP: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{34d71409-4b47-4d80-aaac-3a28a4a3b3e6}'), pid=5)
WPDNSE_OBJECT_HAS_ALBUM_ART: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{34d71409-4b47-4d80-aaac-3a28a4a3b3e6}'), pid=6)
WPDNSE_OBJECT_OPTIMAL_READ_BLOCK_SIZE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{34d71409-4b47-4d80-aaac-3a28a4a3b3e6}'), pid=7)
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
def DMProcessConfigXMLFiltered(pszXmlIn: win32more.Windows.Win32.Foundation.PWSTR, rgszAllowedCspNodes: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwNumAllowedCspNodes: UInt32, pbstrXmlOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DELETE_OBJECT_OPTIONS = Int32
PORTABLE_DEVICE_DELETE_NO_RECURSION: win32more.Windows.Win32.Devices.PortableDevices.DELETE_OBJECT_OPTIONS = 0
PORTABLE_DEVICE_DELETE_WITH_RECURSION: win32more.Windows.Win32.Devices.PortableDevices.DELETE_OBJECT_OPTIONS = 1
DEVICE_RADIO_STATE = Int32
DRS_RADIO_ON: win32more.Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE = 0
DRS_SW_RADIO_OFF: win32more.Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE = 1
DRS_HW_RADIO_OFF: win32more.Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE = 2
DRS_SW_HW_RADIO_OFF: win32more.Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE = 3
DRS_HW_RADIO_ON_UNCONTROLLABLE: win32more.Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE = 4
DRS_RADIO_INVALID: win32more.Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE = 5
DRS_HW_RADIO_OFF_UNCONTROLLABLE: win32more.Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE = 6
DRS_RADIO_MAX: win32more.Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE = 6
EnumBthMtpConnectors = Guid('{a1570149-e645-4f43-8b0d-409b061db2fc}')
class IConnectionRequestCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{272c9ae0-7161-4ae0-91bd-9f448ee9c427}')
    @commethod(3)
    def OnComplete(self, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumPortableDeviceConnectors(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bfdef549-9247-454f-bd82-06fe80853faa}')
    @commethod(3)
    def Next(self, cRequested: UInt32, pConnectors: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceConnector), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cConnectors: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IEnumPortableDeviceConnectors)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumPortableDeviceObjectIDs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{10ece955-cf41-4728-bfa0-41eedf1bbf19}')
    @commethod(3)
    def Next(self, cObjects: UInt32, pObjIDs: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cObjects: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IEnumPortableDeviceObjectIDs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaRadioManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6cfdcab5-fc47-42a5-9241-074b58830e73}')
    @commethod(3)
    def GetRadioInstances(self, ppCollection: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IRadioInstanceCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSystemRadioStateChange(self, sysRadioState: win32more.Windows.Win32.Devices.PortableDevices.SYSTEM_RADIO_STATE, uTimeoutSec: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaRadioManagerNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{89d81f5f-c147-49ed-a11c-77b20c31e7c9}')
    @commethod(3)
    def OnInstanceAdd(self, pRadioInstance: win32more.Windows.Win32.Devices.PortableDevices.IRadioInstance) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnInstanceRemove(self, bstrRadioInstanceId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnInstanceRadioChange(self, bstrRadioInstanceId: win32more.Windows.Win32.Foundation.BSTR, radioState: win32more.Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{625e2df8-6392-4cf0-9ad1-3cfa5f17775c}')
    @commethod(3)
    def Open(self, pszPnPDeviceID: win32more.Windows.Win32.Foundation.PWSTR, pClientInfo: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendCommand(self, dwFlags: UInt32, pParameters: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppResults: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Content(self, ppContent: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceContent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Capabilities(self, ppCapabilities: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceCapabilities)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Advise(self, dwFlags: UInt32, pCallback: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceEventCallback, pParameters: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppszCookie: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Unadvise(self, pszCookie: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPnPDeviceID(self, ppszPnPDeviceID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2c8c6dbf-e3dc-4061-becc-8542e810d126}')
    @commethod(3)
    def GetSupportedCommands(self, ppCommands: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCommandOptions(self, Command: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppOptions: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFunctionalCategories(self, ppCategories: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFunctionalObjects(self, Category: POINTER(Guid), ppObjectIDs: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSupportedContentTypes(self, Category: POINTER(Guid), ppContentTypes: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSupportedFormats(self, ContentType: POINTER(Guid), ppFormats: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSupportedFormatProperties(self, Format: POINTER(Guid), ppKeys: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFixedPropertyAttributes(self, Format: POINTER(Guid), Key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppAttributes: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSupportedEvents(self, ppEvents: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEventOptions(self, Event: POINTER(Guid), ppOptions: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceConnector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{625e2df8-6392-4cf0-9ad1-3cfa5f17775c}')
    @commethod(3)
    def Connect(self, pCallback: win32more.Windows.Win32.Devices.PortableDevices.IConnectionRequestCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect(self, pCallback: win32more.Windows.Win32.Devices.PortableDevices.IConnectionRequestCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Cancel(self, pCallback: win32more.Windows.Win32.Devices.PortableDevices.IConnectionRequestCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProperty(self, pPropertyKey: POINTER(win32more.Windows.Win32.Foundation.DEVPROPKEY), pPropertyType: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE), ppData: POINTER(POINTER(Byte)), pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetProperty(self, pPropertyKey: POINTER(win32more.Windows.Win32.Foundation.DEVPROPKEY), PropertyType: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE, pData: POINTER(Byte), cbData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPnPID(self, ppwszPnPID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceContent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6a96ed84-7c73-4480-9938-bf5af477d426}')
    @commethod(3)
    def EnumObjects(self, dwFlags: UInt32, pszParentObjectID: win32more.Windows.Win32.Foundation.PWSTR, pFilter: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppEnum: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IEnumPortableDeviceObjectIDs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Properties(self, ppProperties: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Transfer(self, ppResources: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceResources)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateObjectWithPropertiesOnly(self, pValues: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppszObjectID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateObjectWithPropertiesAndData(self, pValues: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppData: POINTER(win32more.Windows.Win32.System.Com.IStream), pdwOptimalWriteBufferSize: POINTER(UInt32), ppszCookie: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Delete(self, dwOptions: UInt32, pObjectIDs: win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection, ppResults: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetObjectIDsFromPersistentUniqueIDs(self, pPersistentUniqueIDs: win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection, ppObjectIDs: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Move(self, pObjectIDs: win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection, pszDestinationFolderObjectID: win32more.Windows.Win32.Foundation.PWSTR, ppResults: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Copy(self, pObjectIDs: win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection, pszDestinationFolderObjectID: win32more.Windows.Win32.Foundation.PWSTR, ppResults: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceContent2(ComPtr):
    extends: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceContent
    _iid_ = Guid('{9b4add96-f6bf-4034-8708-eca72bf10554}')
    @commethod(13)
    def UpdateObjectWithPropertiesAndData(self, pszObjectID: win32more.Windows.Win32.Foundation.PWSTR, pProperties: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppData: POINTER(win32more.Windows.Win32.System.Com.IStream), pdwOptimalWriteBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceDataStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IStream
    _iid_ = Guid('{88e04db3-1012-4d64-9996-f703a950d3f4}')
    @commethod(14)
    def GetObjectID(self, ppszObjectID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceDispatchFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5e1eafc3-e3d7-4132-96fa-759c0f9d1e0f}')
    @commethod(3)
    def GetDeviceDispatch(self, pszPnPDeviceID: win32more.Windows.Win32.Foundation.PWSTR, ppDeviceDispatch: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceEventCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a8792a31-f385-493c-a893-40f64eb45f6e}')
    @commethod(3)
    def OnEvent(self, pEventParameters: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceKeyCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dada2357-e0ad-492e-98db-dd61c53ba353}')
    @commethod(3)
    def GetCount(self, pcElems: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, dwIndex: UInt32, pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, Key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(self, dwIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a1567595-4c2f-4574-a6fa-ecef917b9a40}')
    @commethod(3)
    def GetDevices(self, pPnPDeviceIDs: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcPnPDeviceIDs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RefreshDeviceList(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeviceFriendlyName(self, pszPnPDeviceID: win32more.Windows.Win32.Foundation.PWSTR, pDeviceFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, pcchDeviceFriendlyName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDeviceDescription(self, pszPnPDeviceID: win32more.Windows.Win32.Foundation.PWSTR, pDeviceDescription: win32more.Windows.Win32.Foundation.PWSTR, pcchDeviceDescription: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeviceManufacturer(self, pszPnPDeviceID: win32more.Windows.Win32.Foundation.PWSTR, pDeviceManufacturer: win32more.Windows.Win32.Foundation.PWSTR, pcchDeviceManufacturer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDeviceProperty(self, pszPnPDeviceID: win32more.Windows.Win32.Foundation.PWSTR, pszDevicePropertyName: win32more.Windows.Win32.Foundation.PWSTR, pData: POINTER(Byte), pcbData: POINTER(UInt32), pdwType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPrivateDevices(self, pPnPDeviceIDs: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcPnPDeviceIDs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDevicePropVariantCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{89b2e422-4f1b-4316-bcef-a44afea83eb3}')
    @commethod(3)
    def GetCount(self, pcElems: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, dwIndex: UInt32, pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetType(self, pvt: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ChangeType(self, vt: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveAt(self, dwIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7f6d695c-03df-4439-a809-59266beee3a6}')
    @commethod(3)
    def GetSupportedProperties(self, pszObjectID: win32more.Windows.Win32.Foundation.PWSTR, ppKeys: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyAttributes(self, pszObjectID: win32more.Windows.Win32.Foundation.PWSTR, Key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppAttributes: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetValues(self, pszObjectID: win32more.Windows.Win32.Foundation.PWSTR, pKeys: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection, ppValues: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetValues(self, pszObjectID: win32more.Windows.Win32.Foundation.PWSTR, pValues: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppResults: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Delete(self, pszObjectID: win32more.Windows.Win32.Foundation.PWSTR, pKeys: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDevicePropertiesBulk(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{482b05c0-4056-44ed-9e0f-5e23b009da93}')
    @commethod(3)
    def QueueGetValuesByObjectList(self, pObjectIDs: win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection, pKeys: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection, pCallback: win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback, pContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueueGetValuesByObjectFormat(self, pguidObjectFormat: POINTER(Guid), pszParentObjectID: win32more.Windows.Win32.Foundation.PWSTR, dwDepth: UInt32, pKeys: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection, pCallback: win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback, pContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueueSetValuesByObjectList(self, pObjectValues: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValuesCollection, pCallback: win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropertiesBulkCallback, pContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Start(self, pContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Cancel(self, pContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDevicePropertiesBulkCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9deacb80-11e8-40e3-a9f3-f557986a7845}')
    @commethod(3)
    def OnStart(self, pContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnProgress(self, pContext: POINTER(Guid), pResults: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValuesCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEnd(self, pContext: POINTER(Guid), hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceResources(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fd8878ac-d841-4d17-891c-e6829cdb6934}')
    @commethod(3)
    def GetSupportedResources(self, pszObjectID: win32more.Windows.Win32.Foundation.PWSTR, ppKeys: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResourceAttributes(self, pszObjectID: win32more.Windows.Win32.Foundation.PWSTR, Key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppResourceAttributes: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStream(self, pszObjectID: win32more.Windows.Win32.Foundation.PWSTR, Key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), dwMode: UInt32, pdwOptimalBufferSize: POINTER(UInt32), ppStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Delete(self, pszObjectID: win32more.Windows.Win32.Foundation.PWSTR, pKeys: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateResource(self, pResourceAttributes: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppData: POINTER(win32more.Windows.Win32.System.Com.IStream), pdwOptimalWriteBufferSize: POINTER(UInt32), ppszCookie: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d3bd3a44-d7b5-40a9-98b7-2fa4d01dec08}')
    @commethod(3)
    def Open(self, pszPnPServiceID: win32more.Windows.Win32.Foundation.PWSTR, pClientInfo: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Capabilities(self, ppCapabilities: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceServiceCapabilities)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Content(self, ppContent: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceContent2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Methods(self, ppMethods: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceServiceMethods)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetServiceObjectID(self, ppszServiceObjectID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPnPServiceID(self, ppszPnPServiceID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Advise(self, dwFlags: UInt32, pCallback: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceEventCallback, pParameters: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppszCookie: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Unadvise(self, pszCookie: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SendCommand(self, dwFlags: UInt32, pParameters: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppResults: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceActivation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e56b0534-d9b9-425c-9b99-75f97cb3d7c8}')
    @commethod(3)
    def OpenAsync(self, pszPnPServiceID: win32more.Windows.Win32.Foundation.PWSTR, pClientInfo: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, pCallback: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceServiceOpenCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelOpenAsync(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{24dbd89d-413e-43e0-bd5b-197f3c56c886}')
    @commethod(3)
    def GetSupportedMethods(self, ppMethods: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSupportedMethodsByFormat(self, Format: POINTER(Guid), ppMethods: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMethodAttributes(self, Method: POINTER(Guid), ppAttributes: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMethodParameterAttributes(self, Method: POINTER(Guid), Parameter: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppAttributes: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSupportedFormats(self, ppFormats: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFormatAttributes(self, Format: POINTER(Guid), ppAttributes: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSupportedFormatProperties(self, Format: POINTER(Guid), ppKeys: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFormatPropertyAttributes(self, Format: POINTER(Guid), Property: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppAttributes: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSupportedEvents(self, ppEvents: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetEventAttributes(self, Event: POINTER(Guid), ppAttributes: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEventParameterAttributes(self, Event: POINTER(Guid), Parameter: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppAttributes: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetInheritedServices(self, dwInheritanceType: UInt32, ppServices: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetFormatRenderingProfiles(self, Format: POINTER(Guid), ppRenderingProfiles: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValuesCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSupportedCommands(self, ppCommands: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCommandOptions(self, Command: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppOptions: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a8abc4e9-a84a-47a9-80b3-c5d9b172a961}')
    @commethod(3)
    def GetDeviceServices(self, pszPnPDeviceID: win32more.Windows.Win32.Foundation.PWSTR, guidServiceCategory: POINTER(Guid), pServices: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcServices: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceForService(self, pszPnPServiceID: win32more.Windows.Win32.Foundation.PWSTR, ppszPnPDeviceID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceMethodCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c424233c-afce-4828-a756-7ed7a2350083}')
    @commethod(3)
    def OnComplete(self, hrStatus: win32more.Windows.Win32.Foundation.HRESULT, pResults: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceMethods(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e20333c9-fd34-412d-a381-cc6f2d820df7}')
    @commethod(3)
    def Invoke(self, Method: POINTER(Guid), pParameters: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppResults: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeAsync(self, Method: POINTER(Guid), pParameters: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, pCallback: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceServiceMethodCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Cancel(self, pCallback: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceServiceMethodCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceServiceOpenCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bced49c8-8efe-41ed-960b-61313abd47a9}')
    @commethod(3)
    def OnComplete(self, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceUnitsStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5e98025f-bfc4-47a2-9a5f-bc900a507c67}')
    @commethod(3)
    def SeekInUnits(self, dlibMove: Int64, units: win32more.Windows.Win32.Devices.PortableDevices.WPD_STREAM_UNITS, dwOrigin: UInt32, plibNewPosition: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceValues(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6848f6f2-3155-4f86-b6f5-263eeeab3143}')
    @commethod(3)
    def GetCount(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, index: UInt32, pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetStringValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Value: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStringValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetUnsignedIntegerValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Value: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetUnsignedIntegerValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetSignedIntegerValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSignedIntegerValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetUnsignedLargeIntegerValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Value: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetUnsignedLargeIntegerValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetSignedLargeIntegerValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Value: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSignedLargeIntegerValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetFloatValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetFloatValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetErrorValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Value: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetErrorValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetKeyValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Value: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetKeyValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetBoolValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Value: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetBoolValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetIUnknownValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetIUnknownValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppValue: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetGuidValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Value: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetGuidValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetBufferValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(Byte), cbValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetBufferValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppValue: POINTER(POINTER(Byte)), pcbValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetIPortableDeviceValuesValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetIPortableDeviceValuesValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppValue: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetIPortableDevicePropVariantCollectionValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetIPortableDevicePropVariantCollectionValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppValue: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDevicePropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetIPortableDeviceKeyCollectionValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetIPortableDeviceKeyCollectionValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppValue: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetIPortableDeviceValuesCollectionValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValuesCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetIPortableDeviceValuesCollectionValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppValue: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValuesCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def RemoveValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def CopyValuesFromPropertyStore(self, pStore: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def CopyValuesToPropertyStore(self, pStore: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceValuesCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6e3f2d79-4e07-48c4-8208-d8c2e5af4a99}')
    @commethod(3)
    def GetCount(self, pcElems: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, dwIndex: UInt32, ppValues: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pValues: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(self, dwIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPortableDeviceWebControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{94fc7953-5ca1-483a-8aee-df52e7747d00}')
    @commethod(7)
    def GetDeviceFromId(self, deviceId: win32more.Windows.Win32.Foundation.BSTR, ppDevice: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDeviceFromIdAsync(self, deviceId: win32more.Windows.Win32.Foundation.BSTR, pCompletionHandler: win32more.Windows.Win32.System.Com.IDispatch, pErrorHandler: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRadioInstance(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70aa1c9e-f2b4-4c61-86d3-6b9fb75fd1a2}')
    @commethod(3)
    def GetRadioManagerSignature(self, pguidSignature: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInstanceSignature(self, pbstrId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFriendlyName(self, lcid: UInt32, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRadioState(self, pRadioState: POINTER(win32more.Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetRadioState(self, radioState: win32more.Windows.Win32.Devices.PortableDevices.DEVICE_RADIO_STATE, uTimeoutSec: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsMultiComm(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(9)
    def IsAssociatingDevice(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IRadioInstanceCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e5791fae-5665-4e0c-95be-5fde31644185}')
    @commethod(3)
    def GetCount(self, pcInstance: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, uIndex: UInt32, ppRadioInstance: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IRadioInstance)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWpdSerializer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b32f4002-bb27-45ff-af4f-06631c1e8dad}')
    @commethod(3)
    def GetIPortableDeviceValuesFromBuffer(self, pBuffer: POINTER(Byte), dwInputBufferLength: UInt32, ppParams: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteIPortableDeviceValuesToBuffer(self, dwOutputBufferLength: UInt32, pResults: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, pBuffer: POINTER(Byte), pdwBytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBufferFromIPortableDeviceValues(self, pSource: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppBuffer: POINTER(POINTER(Byte)), pdwBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSerializedSize(self, pSource: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PortableDevice = Guid('{728a21c5-3d9e-48d7-9810-864848f0f404}')
PortableDeviceDispatchFactory = Guid('{43232233-8338-4658-ae01-0b4ae830b6b0}')
PortableDeviceFTM = Guid('{f7c0039a-4762-488a-b4b3-760ef9a1ba9b}')
PortableDeviceKeyCollection = Guid('{de2d022d-2480-43be-97f0-d1fa2cf98f4f}')
PortableDeviceManager = Guid('{0af10cec-2ecd-4b92-9581-34f6ae0637f3}')
PortableDevicePropVariantCollection = Guid('{08a99e2f-6d6d-4b80-af5a-baf2bcbe4cb9}')
PortableDeviceService = Guid('{ef5db4c2-9312-422c-9152-411cd9c4dd84}')
PortableDeviceServiceFTM = Guid('{1649b154-c794-497a-9b03-f3f0121302f3}')
PortableDeviceValues = Guid('{0c15d503-d017-47ce-9016-7b3f978721cc}')
PortableDeviceValuesCollection = Guid('{3882134d-14cf-4220-9cb4-435f86d83f60}')
PortableDeviceWebControl = Guid('{186dd02c-2dec-41b5-a7d4-b59056fade51}')
SMS_MESSAGE_TYPES = Int32
SMS_TEXT_MESSAGE: win32more.Windows.Win32.Devices.PortableDevices.SMS_MESSAGE_TYPES = 0
SMS_BINARY_MESSAGE: win32more.Windows.Win32.Devices.PortableDevices.SMS_MESSAGE_TYPES = 1
SYSTEM_RADIO_STATE = Int32
SRS_RADIO_ENABLED: win32more.Windows.Win32.Devices.PortableDevices.SYSTEM_RADIO_STATE = 0
SRS_RADIO_DISABLED: win32more.Windows.Win32.Devices.PortableDevices.SYSTEM_RADIO_STATE = 1
WPD_BITRATE_TYPES = Int32
WPD_BITRATE_TYPE_UNUSED: win32more.Windows.Win32.Devices.PortableDevices.WPD_BITRATE_TYPES = 0
WPD_BITRATE_TYPE_DISCRETE: win32more.Windows.Win32.Devices.PortableDevices.WPD_BITRATE_TYPES = 1
WPD_BITRATE_TYPE_VARIABLE: win32more.Windows.Win32.Devices.PortableDevices.WPD_BITRATE_TYPES = 2
WPD_BITRATE_TYPE_FREE: win32more.Windows.Win32.Devices.PortableDevices.WPD_BITRATE_TYPES = 3
WPD_CAPTURE_MODES = Int32
WPD_CAPTURE_MODE_UNDEFINED: win32more.Windows.Win32.Devices.PortableDevices.WPD_CAPTURE_MODES = 0
WPD_CAPTURE_MODE_NORMAL: win32more.Windows.Win32.Devices.PortableDevices.WPD_CAPTURE_MODES = 1
WPD_CAPTURE_MODE_BURST: win32more.Windows.Win32.Devices.PortableDevices.WPD_CAPTURE_MODES = 2
WPD_CAPTURE_MODE_TIMELAPSE: win32more.Windows.Win32.Devices.PortableDevices.WPD_CAPTURE_MODES = 3
WPD_COLOR_CORRECTED_STATUS_VALUES = Int32
WPD_COLOR_CORRECTED_STATUS_NOT_CORRECTED: win32more.Windows.Win32.Devices.PortableDevices.WPD_COLOR_CORRECTED_STATUS_VALUES = 0
WPD_COLOR_CORRECTED_STATUS_CORRECTED: win32more.Windows.Win32.Devices.PortableDevices.WPD_COLOR_CORRECTED_STATUS_VALUES = 1
WPD_COLOR_CORRECTED_STATUS_SHOULD_NOT_BE_CORRECTED: win32more.Windows.Win32.Devices.PortableDevices.WPD_COLOR_CORRECTED_STATUS_VALUES = 2
class WPD_COMMAND_ACCESS_LOOKUP_ENTRY(Structure):
    Command: win32more.Windows.Win32.Foundation.PROPERTYKEY
    AccessType: UInt32
    AccessProperty: win32more.Windows.Win32.Foundation.PROPERTYKEY
WPD_COMMAND_ACCESS_TYPES = Int32
WPD_COMMAND_ACCESS_READ: win32more.Windows.Win32.Devices.PortableDevices.WPD_COMMAND_ACCESS_TYPES = 1
WPD_COMMAND_ACCESS_READWRITE: win32more.Windows.Win32.Devices.PortableDevices.WPD_COMMAND_ACCESS_TYPES = 3
WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_STGM_ACCESS: win32more.Windows.Win32.Devices.PortableDevices.WPD_COMMAND_ACCESS_TYPES = 4
WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_FILE_ACCESS: win32more.Windows.Win32.Devices.PortableDevices.WPD_COMMAND_ACCESS_TYPES = 8
WPD_COMMAND_ACCESS_FROM_ATTRIBUTE_WITH_METHOD_ACCESS: win32more.Windows.Win32.Devices.PortableDevices.WPD_COMMAND_ACCESS_TYPES = 16
WPD_CROPPED_STATUS_VALUES = Int32
WPD_CROPPED_STATUS_NOT_CROPPED: win32more.Windows.Win32.Devices.PortableDevices.WPD_CROPPED_STATUS_VALUES = 0
WPD_CROPPED_STATUS_CROPPED: win32more.Windows.Win32.Devices.PortableDevices.WPD_CROPPED_STATUS_VALUES = 1
WPD_CROPPED_STATUS_SHOULD_NOT_BE_CROPPED: win32more.Windows.Win32.Devices.PortableDevices.WPD_CROPPED_STATUS_VALUES = 2
WPD_DEVICE_TRANSPORTS = Int32
WPD_DEVICE_TRANSPORT_UNSPECIFIED: win32more.Windows.Win32.Devices.PortableDevices.WPD_DEVICE_TRANSPORTS = 0
WPD_DEVICE_TRANSPORT_USB: win32more.Windows.Win32.Devices.PortableDevices.WPD_DEVICE_TRANSPORTS = 1
WPD_DEVICE_TRANSPORT_IP: win32more.Windows.Win32.Devices.PortableDevices.WPD_DEVICE_TRANSPORTS = 2
WPD_DEVICE_TRANSPORT_BLUETOOTH: win32more.Windows.Win32.Devices.PortableDevices.WPD_DEVICE_TRANSPORTS = 3
WPD_DEVICE_TYPES = Int32
WPD_DEVICE_TYPE_GENERIC: win32more.Windows.Win32.Devices.PortableDevices.WPD_DEVICE_TYPES = 0
WPD_DEVICE_TYPE_CAMERA: win32more.Windows.Win32.Devices.PortableDevices.WPD_DEVICE_TYPES = 1
WPD_DEVICE_TYPE_MEDIA_PLAYER: win32more.Windows.Win32.Devices.PortableDevices.WPD_DEVICE_TYPES = 2
WPD_DEVICE_TYPE_PHONE: win32more.Windows.Win32.Devices.PortableDevices.WPD_DEVICE_TYPES = 3
WPD_DEVICE_TYPE_VIDEO: win32more.Windows.Win32.Devices.PortableDevices.WPD_DEVICE_TYPES = 4
WPD_DEVICE_TYPE_PERSONAL_INFORMATION_MANAGER: win32more.Windows.Win32.Devices.PortableDevices.WPD_DEVICE_TYPES = 5
WPD_DEVICE_TYPE_AUDIO_RECORDER: win32more.Windows.Win32.Devices.PortableDevices.WPD_DEVICE_TYPES = 6
WPD_EFFECT_MODES = Int32
WPD_EFFECT_MODE_UNDEFINED: win32more.Windows.Win32.Devices.PortableDevices.WPD_EFFECT_MODES = 0
WPD_EFFECT_MODE_COLOR: win32more.Windows.Win32.Devices.PortableDevices.WPD_EFFECT_MODES = 1
WPD_EFFECT_MODE_BLACK_AND_WHITE: win32more.Windows.Win32.Devices.PortableDevices.WPD_EFFECT_MODES = 2
WPD_EFFECT_MODE_SEPIA: win32more.Windows.Win32.Devices.PortableDevices.WPD_EFFECT_MODES = 3
WPD_EXPOSURE_METERING_MODES = Int32
WPD_EXPOSURE_METERING_MODE_UNDEFINED: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_METERING_MODES = 0
WPD_EXPOSURE_METERING_MODE_AVERAGE: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_METERING_MODES = 1
WPD_EXPOSURE_METERING_MODE_CENTER_WEIGHTED_AVERAGE: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_METERING_MODES = 2
WPD_EXPOSURE_METERING_MODE_MULTI_SPOT: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_METERING_MODES = 3
WPD_EXPOSURE_METERING_MODE_CENTER_SPOT: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_METERING_MODES = 4
WPD_EXPOSURE_PROGRAM_MODES = Int32
WPD_EXPOSURE_PROGRAM_MODE_UNDEFINED: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_PROGRAM_MODES = 0
WPD_EXPOSURE_PROGRAM_MODE_MANUAL: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_PROGRAM_MODES = 1
WPD_EXPOSURE_PROGRAM_MODE_AUTO: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_PROGRAM_MODES = 2
WPD_EXPOSURE_PROGRAM_MODE_APERTURE_PRIORITY: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_PROGRAM_MODES = 3
WPD_EXPOSURE_PROGRAM_MODE_SHUTTER_PRIORITY: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_PROGRAM_MODES = 4
WPD_EXPOSURE_PROGRAM_MODE_CREATIVE: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_PROGRAM_MODES = 5
WPD_EXPOSURE_PROGRAM_MODE_ACTION: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_PROGRAM_MODES = 6
WPD_EXPOSURE_PROGRAM_MODE_PORTRAIT: win32more.Windows.Win32.Devices.PortableDevices.WPD_EXPOSURE_PROGRAM_MODES = 7
WPD_FLASH_MODES = Int32
WPD_FLASH_MODE_UNDEFINED: win32more.Windows.Win32.Devices.PortableDevices.WPD_FLASH_MODES = 0
WPD_FLASH_MODE_AUTO: win32more.Windows.Win32.Devices.PortableDevices.WPD_FLASH_MODES = 1
WPD_FLASH_MODE_OFF: win32more.Windows.Win32.Devices.PortableDevices.WPD_FLASH_MODES = 2
WPD_FLASH_MODE_FILL: win32more.Windows.Win32.Devices.PortableDevices.WPD_FLASH_MODES = 3
WPD_FLASH_MODE_RED_EYE_AUTO: win32more.Windows.Win32.Devices.PortableDevices.WPD_FLASH_MODES = 4
WPD_FLASH_MODE_RED_EYE_FILL: win32more.Windows.Win32.Devices.PortableDevices.WPD_FLASH_MODES = 5
WPD_FLASH_MODE_EXTERNAL_SYNC: win32more.Windows.Win32.Devices.PortableDevices.WPD_FLASH_MODES = 6
WPD_FOCUS_METERING_MODES = Int32
WPD_FOCUS_METERING_MODE_UNDEFINED: win32more.Windows.Win32.Devices.PortableDevices.WPD_FOCUS_METERING_MODES = 0
WPD_FOCUS_METERING_MODE_CENTER_SPOT: win32more.Windows.Win32.Devices.PortableDevices.WPD_FOCUS_METERING_MODES = 1
WPD_FOCUS_METERING_MODE_MULTI_SPOT: win32more.Windows.Win32.Devices.PortableDevices.WPD_FOCUS_METERING_MODES = 2
WPD_FOCUS_MODES = Int32
WPD_FOCUS_UNDEFINED: win32more.Windows.Win32.Devices.PortableDevices.WPD_FOCUS_MODES = 0
WPD_FOCUS_MANUAL: win32more.Windows.Win32.Devices.PortableDevices.WPD_FOCUS_MODES = 1
WPD_FOCUS_AUTOMATIC: win32more.Windows.Win32.Devices.PortableDevices.WPD_FOCUS_MODES = 2
WPD_FOCUS_AUTOMATIC_MACRO: win32more.Windows.Win32.Devices.PortableDevices.WPD_FOCUS_MODES = 3
WPD_META_GENRES = Int32
WPD_META_GENRE_UNUSED: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 0
WPD_META_GENRE_GENERIC_MUSIC_AUDIO_FILE: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 1
WPD_META_GENRE_GENERIC_NON_MUSIC_AUDIO_FILE: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 17
WPD_META_GENRE_SPOKEN_WORD_AUDIO_BOOK_FILES: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 18
WPD_META_GENRE_SPOKEN_WORD_FILES_NON_AUDIO_BOOK: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 19
WPD_META_GENRE_SPOKEN_WORD_NEWS: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 20
WPD_META_GENRE_SPOKEN_WORD_TALK_SHOWS: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 21
WPD_META_GENRE_GENERIC_VIDEO_FILE: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 33
WPD_META_GENRE_NEWS_VIDEO_FILE: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 34
WPD_META_GENRE_MUSIC_VIDEO_FILE: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 35
WPD_META_GENRE_HOME_VIDEO_FILE: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 36
WPD_META_GENRE_FEATURE_FILM_VIDEO_FILE: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 37
WPD_META_GENRE_TELEVISION_VIDEO_FILE: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 38
WPD_META_GENRE_TRAINING_EDUCATIONAL_VIDEO_FILE: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 39
WPD_META_GENRE_PHOTO_MONTAGE_VIDEO_FILE: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 40
WPD_META_GENRE_GENERIC_NON_AUDIO_NON_VIDEO: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 48
WPD_META_GENRE_AUDIO_PODCAST: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 64
WPD_META_GENRE_VIDEO_PODCAST: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 65
WPD_META_GENRE_MIXED_PODCAST: win32more.Windows.Win32.Devices.PortableDevices.WPD_META_GENRES = 66
WPD_OPERATION_STATES = Int32
WPD_OPERATION_STATE_UNSPECIFIED: win32more.Windows.Win32.Devices.PortableDevices.WPD_OPERATION_STATES = 0
WPD_OPERATION_STATE_STARTED: win32more.Windows.Win32.Devices.PortableDevices.WPD_OPERATION_STATES = 1
WPD_OPERATION_STATE_RUNNING: win32more.Windows.Win32.Devices.PortableDevices.WPD_OPERATION_STATES = 2
WPD_OPERATION_STATE_PAUSED: win32more.Windows.Win32.Devices.PortableDevices.WPD_OPERATION_STATES = 3
WPD_OPERATION_STATE_CANCELLED: win32more.Windows.Win32.Devices.PortableDevices.WPD_OPERATION_STATES = 4
WPD_OPERATION_STATE_FINISHED: win32more.Windows.Win32.Devices.PortableDevices.WPD_OPERATION_STATES = 5
WPD_OPERATION_STATE_ABORTED: win32more.Windows.Win32.Devices.PortableDevices.WPD_OPERATION_STATES = 6
WPD_PARAMETER_USAGE_TYPES = Int32
WPD_PARAMETER_USAGE_RETURN: win32more.Windows.Win32.Devices.PortableDevices.WPD_PARAMETER_USAGE_TYPES = 0
WPD_PARAMETER_USAGE_IN: win32more.Windows.Win32.Devices.PortableDevices.WPD_PARAMETER_USAGE_TYPES = 1
WPD_PARAMETER_USAGE_OUT: win32more.Windows.Win32.Devices.PortableDevices.WPD_PARAMETER_USAGE_TYPES = 2
WPD_PARAMETER_USAGE_INOUT: win32more.Windows.Win32.Devices.PortableDevices.WPD_PARAMETER_USAGE_TYPES = 3
WPD_POWER_SOURCES = Int32
WPD_POWER_SOURCE_BATTERY: win32more.Windows.Win32.Devices.PortableDevices.WPD_POWER_SOURCES = 0
WPD_POWER_SOURCE_EXTERNAL: win32more.Windows.Win32.Devices.PortableDevices.WPD_POWER_SOURCES = 1
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES = Int32
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_OBJECT: win32more.Windows.Win32.Devices.PortableDevices.WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES = 0
WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_RESOURCE: win32more.Windows.Win32.Devices.PortableDevices.WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES = 1
WPD_SECTION_DATA_UNITS_VALUES = Int32
WPD_SECTION_DATA_UNITS_BYTES: win32more.Windows.Win32.Devices.PortableDevices.WPD_SECTION_DATA_UNITS_VALUES = 0
WPD_SECTION_DATA_UNITS_MILLISECONDS: win32more.Windows.Win32.Devices.PortableDevices.WPD_SECTION_DATA_UNITS_VALUES = 1
WPD_SERVICE_INHERITANCE_TYPES = Int32
WPD_SERVICE_INHERITANCE_IMPLEMENTATION: win32more.Windows.Win32.Devices.PortableDevices.WPD_SERVICE_INHERITANCE_TYPES = 0
WPD_SMS_ENCODING_TYPES = Int32
SMS_ENCODING_7_BIT: win32more.Windows.Win32.Devices.PortableDevices.WPD_SMS_ENCODING_TYPES = 0
SMS_ENCODING_8_BIT: win32more.Windows.Win32.Devices.PortableDevices.WPD_SMS_ENCODING_TYPES = 1
SMS_ENCODING_UTF_16: win32more.Windows.Win32.Devices.PortableDevices.WPD_SMS_ENCODING_TYPES = 2
WPD_STORAGE_ACCESS_CAPABILITY_VALUES = Int32
WPD_STORAGE_ACCESS_CAPABILITY_READWRITE: win32more.Windows.Win32.Devices.PortableDevices.WPD_STORAGE_ACCESS_CAPABILITY_VALUES = 0
WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITHOUT_OBJECT_DELETION: win32more.Windows.Win32.Devices.PortableDevices.WPD_STORAGE_ACCESS_CAPABILITY_VALUES = 1
WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITH_OBJECT_DELETION: win32more.Windows.Win32.Devices.PortableDevices.WPD_STORAGE_ACCESS_CAPABILITY_VALUES = 2
WPD_STORAGE_TYPE_VALUES = Int32
WPD_STORAGE_TYPE_UNDEFINED: win32more.Windows.Win32.Devices.PortableDevices.WPD_STORAGE_TYPE_VALUES = 0
WPD_STORAGE_TYPE_FIXED_ROM: win32more.Windows.Win32.Devices.PortableDevices.WPD_STORAGE_TYPE_VALUES = 1
WPD_STORAGE_TYPE_REMOVABLE_ROM: win32more.Windows.Win32.Devices.PortableDevices.WPD_STORAGE_TYPE_VALUES = 2
WPD_STORAGE_TYPE_FIXED_RAM: win32more.Windows.Win32.Devices.PortableDevices.WPD_STORAGE_TYPE_VALUES = 3
WPD_STORAGE_TYPE_REMOVABLE_RAM: win32more.Windows.Win32.Devices.PortableDevices.WPD_STORAGE_TYPE_VALUES = 4
WPD_STREAM_UNITS = Int32
WPD_STREAM_UNITS_BYTES: win32more.Windows.Win32.Devices.PortableDevices.WPD_STREAM_UNITS = 0
WPD_STREAM_UNITS_FRAMES: win32more.Windows.Win32.Devices.PortableDevices.WPD_STREAM_UNITS = 1
WPD_STREAM_UNITS_ROWS: win32more.Windows.Win32.Devices.PortableDevices.WPD_STREAM_UNITS = 2
WPD_STREAM_UNITS_MILLISECONDS: win32more.Windows.Win32.Devices.PortableDevices.WPD_STREAM_UNITS = 4
WPD_STREAM_UNITS_MICROSECONDS: win32more.Windows.Win32.Devices.PortableDevices.WPD_STREAM_UNITS = 8
WPD_VIDEO_SCAN_TYPES = Int32
WPD_VIDEO_SCAN_TYPE_UNUSED: win32more.Windows.Win32.Devices.PortableDevices.WPD_VIDEO_SCAN_TYPES = 0
WPD_VIDEO_SCAN_TYPE_PROGRESSIVE: win32more.Windows.Win32.Devices.PortableDevices.WPD_VIDEO_SCAN_TYPES = 1
WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_UPPER_FIRST: win32more.Windows.Win32.Devices.PortableDevices.WPD_VIDEO_SCAN_TYPES = 2
WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_LOWER_FIRST: win32more.Windows.Win32.Devices.PortableDevices.WPD_VIDEO_SCAN_TYPES = 3
WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_UPPER_FIRST: win32more.Windows.Win32.Devices.PortableDevices.WPD_VIDEO_SCAN_TYPES = 4
WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_LOWER_FIRST: win32more.Windows.Win32.Devices.PortableDevices.WPD_VIDEO_SCAN_TYPES = 5
WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE: win32more.Windows.Win32.Devices.PortableDevices.WPD_VIDEO_SCAN_TYPES = 6
WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE_AND_PROGRESSIVE: win32more.Windows.Win32.Devices.PortableDevices.WPD_VIDEO_SCAN_TYPES = 7
WPD_WHITE_BALANCE_SETTINGS = Int32
WPD_WHITE_BALANCE_UNDEFINED: win32more.Windows.Win32.Devices.PortableDevices.WPD_WHITE_BALANCE_SETTINGS = 0
WPD_WHITE_BALANCE_MANUAL: win32more.Windows.Win32.Devices.PortableDevices.WPD_WHITE_BALANCE_SETTINGS = 1
WPD_WHITE_BALANCE_AUTOMATIC: win32more.Windows.Win32.Devices.PortableDevices.WPD_WHITE_BALANCE_SETTINGS = 2
WPD_WHITE_BALANCE_ONE_PUSH_AUTOMATIC: win32more.Windows.Win32.Devices.PortableDevices.WPD_WHITE_BALANCE_SETTINGS = 3
WPD_WHITE_BALANCE_DAYLIGHT: win32more.Windows.Win32.Devices.PortableDevices.WPD_WHITE_BALANCE_SETTINGS = 4
WPD_WHITE_BALANCE_FLORESCENT: win32more.Windows.Win32.Devices.PortableDevices.WPD_WHITE_BALANCE_SETTINGS = 5
WPD_WHITE_BALANCE_TUNGSTEN: win32more.Windows.Win32.Devices.PortableDevices.WPD_WHITE_BALANCE_SETTINGS = 6
WPD_WHITE_BALANCE_FLASH: win32more.Windows.Win32.Devices.PortableDevices.WPD_WHITE_BALANCE_SETTINGS = 7
WpdAttributeForm = Int32
WPD_PROPERTY_ATTRIBUTE_FORM_UNSPECIFIED: win32more.Windows.Win32.Devices.PortableDevices.WpdAttributeForm = 0
WPD_PROPERTY_ATTRIBUTE_FORM_RANGE: win32more.Windows.Win32.Devices.PortableDevices.WpdAttributeForm = 1
WPD_PROPERTY_ATTRIBUTE_FORM_ENUMERATION: win32more.Windows.Win32.Devices.PortableDevices.WpdAttributeForm = 2
WPD_PROPERTY_ATTRIBUTE_FORM_REGULAR_EXPRESSION: win32more.Windows.Win32.Devices.PortableDevices.WpdAttributeForm = 3
WPD_PROPERTY_ATTRIBUTE_FORM_OBJECT_IDENTIFIER: win32more.Windows.Win32.Devices.PortableDevices.WpdAttributeForm = 4
WpdParameterAttributeForm = Int32
WPD_PARAMETER_ATTRIBUTE_FORM_UNSPECIFIED: win32more.Windows.Win32.Devices.PortableDevices.WpdParameterAttributeForm = 0
WPD_PARAMETER_ATTRIBUTE_FORM_RANGE: win32more.Windows.Win32.Devices.PortableDevices.WpdParameterAttributeForm = 1
WPD_PARAMETER_ATTRIBUTE_FORM_ENUMERATION: win32more.Windows.Win32.Devices.PortableDevices.WpdParameterAttributeForm = 2
WPD_PARAMETER_ATTRIBUTE_FORM_REGULAR_EXPRESSION: win32more.Windows.Win32.Devices.PortableDevices.WpdParameterAttributeForm = 3
WPD_PARAMETER_ATTRIBUTE_FORM_OBJECT_IDENTIFIER: win32more.Windows.Win32.Devices.PortableDevices.WpdParameterAttributeForm = 4
WpdSerializer = Guid('{0b91a74b-ad7c-4a9d-b563-29eef9167172}')


make_ready(__name__)
