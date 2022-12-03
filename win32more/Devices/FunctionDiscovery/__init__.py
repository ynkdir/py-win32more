from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Devices.FunctionDiscovery
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
FD_EVENTID_PRIVATE = 100
FD_EVENTID = 1000
FD_EVENTID_SEARCHCOMPLETE = 1000
FD_EVENTID_ASYNCTHREADEXIT = 1001
FD_EVENTID_SEARCHSTART = 1002
FD_EVENTID_IPADDRESSCHANGE = 1003
FD_EVENTID_QUERYREFRESH = 1004
def _define_SID_PnpProvider():
    return Guid('8101368e-cabb-4426-ac-ff-96-c4-10-81-20-00')
def _define_SID_UPnPActivator():
    return Guid('0d0d66eb-cf74-4164-b5-2f-08-34-46-72-dd-46')
def _define_SID_EnumInterface():
    return Guid('40eab0b9-4d7f-4b53-a3-34-15-81-dd-90-41-f4')
def _define_SID_PNPXPropertyStore():
    return Guid('a86530b1-542f-439f-b7-1c-b0-75-6b-13-67-7a')
def _define_SID_PNPXAssociation():
    return Guid('cee8ccc9-4f6b-4469-a2-35-5a-22-86-9e-ef-03')
def _define_SID_PNPXServiceCollection():
    return Guid('439e80ee-a217-4712-9f-a6-de-ab-d9-c2-a7-27')
def _define_SID_FDPairingHandler():
    return Guid('383b69fa-5486-49da-91-f5-d6-3c-24-c8-e9-d0')
def _define_SID_EnumDeviceFunction():
    return Guid('13e0e9e2-c3fa-4e3c-90-6e-64-50-2f-a4-dc-95')
def _define_SID_UnpairProvider():
    return Guid('89a502fc-857b-4698-a0-b7-02-71-92-00-2f-9e')
def _define_SID_DeviceDisplayStatusManager():
    return Guid('f59aa553-8309-46ca-97-36-1a-c3-c6-2d-60-31')
def _define_SID_FunctionDiscoveryProviderRefresh():
    return Guid('2b4cbdc9-31c4-40d4-a6-2d-77-2a-a1-74-ed-52')
def _define_SID_UninstallDeviceFunction():
    return Guid('c920566e-5671-4496-80-25-bf-0b-89-bd-44-cd')
def _define_PKEY_FunctionInstance():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('08c0c253-a154-4746-90-05-82-de-53-17-14-8b'), pid=1)
def _define_FMTID_FD():
    return Guid('904b03a2-471d-423c-a5-84-f3-48-32-38-a1-46')
FD_Visibility_Default = 0
FD_Visibility_Hidden = 1
def _define_FMTID_Device():
    return Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57')
def _define_FMTID_DeviceInterface():
    return Guid('53808008-07bb-4661-bc-3c-b5-95-3e-70-85-60')
def _define_PKEY_DeviceDisplay_Address():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=51)
def _define_PKEY_DeviceDisplay_DiscoveryMethod():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=52)
def _define_PKEY_DeviceDisplay_IsEncrypted():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=53)
def _define_PKEY_DeviceDisplay_IsAuthenticated():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=54)
def _define_PKEY_DeviceDisplay_IsConnected():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=55)
def _define_PKEY_DeviceDisplay_IsPaired():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=56)
def _define_PKEY_DeviceDisplay_Icon():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=57)
def _define_PKEY_DeviceDisplay_Version():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=65)
def _define_PKEY_DeviceDisplay_Last_Seen():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=66)
def _define_PKEY_DeviceDisplay_Last_Connected():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=67)
def _define_PKEY_DeviceDisplay_IsShowInDisconnectedState():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=68)
def _define_PKEY_DeviceDisplay_IsLocalMachine():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=70)
def _define_PKEY_DeviceDisplay_MetadataPath():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=71)
def _define_PKEY_DeviceDisplay_IsMetadataSearchInProgress():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=72)
def _define_PKEY_DeviceDisplay_MetadataChecksum():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=73)
def _define_PKEY_DeviceDisplay_IsNotInterestingForDisplay():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=74)
def _define_PKEY_DeviceDisplay_LaunchDeviceStageOnDeviceConnect():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=76)
def _define_PKEY_DeviceDisplay_LaunchDeviceStageFromExplorer():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=77)
def _define_PKEY_DeviceDisplay_BaselineExperienceId():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=78)
def _define_PKEY_DeviceDisplay_IsDeviceUniquelyIdentifiable():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=79)
def _define_PKEY_DeviceDisplay_AssociationArray():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=80)
def _define_PKEY_DeviceDisplay_DeviceDescription1():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=81)
def _define_PKEY_DeviceDisplay_DeviceDescription2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=82)
def _define_PKEY_DeviceDisplay_IsNotWorkingProperly():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=83)
def _define_PKEY_DeviceDisplay_IsSharedDevice():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=84)
def _define_PKEY_DeviceDisplay_IsNetworkDevice():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=85)
def _define_PKEY_DeviceDisplay_IsDefaultDevice():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=86)
def _define_PKEY_DeviceDisplay_MetadataCabinet():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=87)
def _define_PKEY_DeviceDisplay_RequiresPairingElevation():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=88)
def _define_PKEY_DeviceDisplay_ExperienceId():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=89)
def _define_PKEY_DeviceDisplay_Category():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=90)
def _define_PKEY_DeviceDisplay_Category_Desc_Singular():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=91)
def _define_PKEY_DeviceDisplay_Category_Desc_Plural():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=92)
def _define_PKEY_DeviceDisplay_Category_Icon():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=93)
def _define_PKEY_DeviceDisplay_CategoryGroup_Desc():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=94)
def _define_PKEY_DeviceDisplay_CategoryGroup_Icon():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=95)
def _define_PKEY_DeviceDisplay_PrimaryCategory():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=97)
def _define_PKEY_DeviceDisplay_UnpairUninstall():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=98)
def _define_PKEY_DeviceDisplay_RequiresUninstallElevation():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=99)
def _define_PKEY_DeviceDisplay_DeviceFunctionSubRank():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=100)
def _define_PKEY_DeviceDisplay_AlwaysShowDeviceAsConnected():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=101)
def _define_PKEY_DeviceDisplay_FriendlyName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12288)
def _define_PKEY_DeviceDisplay_Manufacturer():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8192)
def _define_PKEY_DeviceDisplay_ModelName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8194)
def _define_PKEY_DeviceDisplay_ModelNumber():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8195)
def _define_PKEY_DeviceDisplay_InstallInProgress():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=9)
def _define_FMTID_Pairing():
    return Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc')
def _define_PKEY_Pairing_ListItemText():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc'), pid=1)
def _define_PKEY_Pairing_ListItemDescription():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc'), pid=2)
def _define_PKEY_Pairing_ListItemIcon():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc'), pid=3)
def _define_PKEY_Pairing_ListItemDefault():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc'), pid=4)
def _define_PKEY_Pairing_IsWifiOnlyDevice():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc'), pid=16)
DEVICEDISPLAY_DISCOVERYMETHOD_BLUETOOTH = 'Bluetooth'
DEVICEDISPLAY_DISCOVERYMETHOD_BLUETOOTH_LE = 'Bluetooth Low Energy'
DEVICEDISPLAY_DISCOVERYMETHOD_NETBIOS = 'NetBIOS'
DEVICEDISPLAY_DISCOVERYMETHOD_AD_PRINTER = 'Published Printer'
DEVICEDISPLAY_DISCOVERYMETHOD_PNP = 'PnP'
DEVICEDISPLAY_DISCOVERYMETHOD_UPNP = 'UPnP'
DEVICEDISPLAY_DISCOVERYMETHOD_WSD = 'WSD'
DEVICEDISPLAY_DISCOVERYMETHOD_WUSB = 'WUSB'
DEVICEDISPLAY_DISCOVERYMETHOD_WFD = 'WiFiDirect'
DEVICEDISPLAY_DISCOVERYMETHOD_ASP_INFRA = 'AspInfra'
def _define_PKEY_Device_BIOSVersion():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('eaee7f1d-6a33-44d1-94-41-5f-46-de-f2-31-98'), pid=9)
def _define_FMTID_WSD():
    return Guid('92506491-ff95-4724-a0-5a-5b-81-88-5a-7c-92')
def _define_FMTID_PNPX():
    return Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd')
def _define_PKEY_PNPX_GlobalIdentity():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4096)
def _define_PKEY_PNPX_Types():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4097)
def _define_PKEY_PNPX_Scopes():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4098)
def _define_PKEY_PNPX_XAddrs():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4099)
def _define_PKEY_PNPX_MetadataVersion():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4100)
def _define_PKEY_PNPX_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4101)
def _define_PKEY_PNPX_RemoteAddress():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4102)
def _define_PKEY_PNPX_RootProxy():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4103)
def _define_PKEY_PNPX_ManufacturerUrl():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8193)
def _define_PKEY_PNPX_ModelUrl():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8196)
def _define_PKEY_PNPX_Upc():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8197)
def _define_PKEY_PNPX_PresentationUrl():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8198)
def _define_PKEY_PNPX_FirmwareVersion():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12289)
def _define_PKEY_PNPX_SerialNumber():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12290)
def _define_PKEY_PNPX_DeviceCategory():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12292)
def _define_PKEY_PNPX_SecureChannel():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=28673)
def _define_PKEY_PNPX_CompactSignature():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=28674)
def _define_PKEY_PNPX_DeviceCertHash():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=28675)
PNPX_DEVICECATEGORY_COMPUTER = 'Computers'
PNPX_DEVICECATEGORY_INPUTDEVICE = 'Input'
PNPX_DEVICECATEGORY_PRINTER = 'Printers'
PNPX_DEVICECATEGORY_SCANNER = 'Scanners'
PNPX_DEVICECATEGORY_FAX = 'FAX'
PNPX_DEVICECATEGORY_MFP = 'MFP'
PNPX_DEVICECATEGORY_CAMERA = 'Cameras'
PNPX_DEVICECATEGORY_STORAGE = 'Storage'
PNPX_DEVICECATEGORY_NETWORK_INFRASTRUCTURE = 'NetworkInfrastructure'
PNPX_DEVICECATEGORY_DISPLAYS = 'Displays'
PNPX_DEVICECATEGORY_MULTIMEDIA_DEVICE = 'MediaDevices'
PNPX_DEVICECATEGORY_GAMING_DEVICE = 'Gaming'
PNPX_DEVICECATEGORY_TELEPHONE = 'Phones'
PNPX_DEVICECATEGORY_HOME_AUTOMATION_SYSTEM = 'HomeAutomation'
PNPX_DEVICECATEGORY_HOME_SECURITY_SYSTEM = 'HomeSecurity'
PNPX_DEVICECATEGORY_OTHER = 'Other'
def _define_PKEY_PNPX_DeviceCategory_Desc():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12293)
def _define_PKEY_PNPX_Category_Desc_NonPlural():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12304)
def _define_PKEY_PNPX_PhysicalAddress():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12294)
def _define_PKEY_PNPX_NetworkInterfaceLuid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12295)
def _define_PKEY_PNPX_NetworkInterfaceGuid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12296)
def _define_PKEY_PNPX_IpAddress():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12297)
def _define_PKEY_PNPX_ServiceAddress():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16384)
def _define_PKEY_PNPX_ServiceId():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16385)
def _define_PKEY_PNPX_ServiceTypes():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16386)
def _define_PKEY_PNPX_ServiceControlUrl():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16388)
def _define_PKEY_PNPX_ServiceDescUrl():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16389)
def _define_PKEY_PNPX_ServiceEventSubUrl():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16390)
def _define_PKEY_PNPX_DomainName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=20480)
def _define_PKEY_PNPX_ShareName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=20482)
def _define_PKEY_SSDP_AltLocationInfo():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=24576)
def _define_PKEY_SSDP_DevLifeTime():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=24577)
def _define_PKEY_SSDP_NetworkInterface():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=24578)
def _define_FMTID_PNPXDynamicProperty():
    return Guid('4fc5077e-b686-44be-93-e3-86-ca-fe-36-8c-cd')
def _define_PKEY_PNPX_Installable():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4fc5077e-b686-44be-93-e3-86-ca-fe-36-8c-cd'), pid=1)
def _define_PKEY_PNPX_Associated():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4fc5077e-b686-44be-93-e3-86-ca-fe-36-8c-cd'), pid=2)
def _define_PKEY_PNPX_CompatibleTypes():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4fc5077e-b686-44be-93-e3-86-ca-fe-36-8c-cd'), pid=3)
def _define_PKEY_PNPX_InstallState():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4fc5077e-b686-44be-93-e3-86-ca-fe-36-8c-cd'), pid=4)
PNPX_INSTALLSTATE_NOTINSTALLED = 0
PNPX_INSTALLSTATE_INSTALLED = 1
PNPX_INSTALLSTATE_INSTALLING = 2
PNPX_INSTALLSTATE_FAILED = 3
def _define_PKEY_PNPX_Removable():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=28672)
def _define_PKEY_PNPX_IPBusEnumerated():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=28688)
def _define_PKEY_WNET_Scope():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=1)
def _define_PKEY_WNET_Type():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=2)
def _define_PKEY_WNET_DisplayType():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=3)
def _define_PKEY_WNET_Usage():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=4)
def _define_PKEY_WNET_LocalName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=5)
def _define_PKEY_WNET_RemoteName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=6)
def _define_PKEY_WNET_Comment():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=7)
def _define_PKEY_WNET_Provider():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=8)
def _define_PKEY_WCN_Version():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b80-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=1)
def _define_PKEY_WCN_RequestType():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b81-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=2)
def _define_PKEY_WCN_AuthType():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b82-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=3)
def _define_PKEY_WCN_EncryptType():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b83-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=4)
def _define_PKEY_WCN_ConnType():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b84-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=5)
def _define_PKEY_WCN_ConfigMethods():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b85-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=6)
def _define_PKEY_WCN_RfBand():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b87-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=8)
def _define_PKEY_WCN_AssocState():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b88-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=9)
def _define_PKEY_WCN_ConfigError():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b89-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=10)
def _define_PKEY_WCN_ConfigState():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b89-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=11)
def _define_PKEY_WCN_DevicePasswordId():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b89-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=12)
def _define_PKEY_WCN_OSVersion():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b89-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=13)
def _define_PKEY_WCN_VendorExtension():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b8a-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=14)
def _define_PKEY_WCN_RegistrarType():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b8b-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=15)
def _define_PKEY_Hardware_Devinst():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=4097)
def _define_PKEY_Hardware_DisplayAttribute():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=5)
def _define_PKEY_Hardware_DriverDate():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=11)
def _define_PKEY_Hardware_DriverProvider():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=10)
def _define_PKEY_Hardware_DriverVersion():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=9)
def _define_PKEY_Hardware_Function():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=4099)
def _define_PKEY_Hardware_Icon():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=3)
def _define_PKEY_Hardware_Image():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=4098)
def _define_PKEY_Hardware_Manufacturer():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=6)
def _define_PKEY_Hardware_Model():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=7)
def _define_PKEY_Hardware_Name():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=2)
def _define_PKEY_Hardware_SerialNumber():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=8)
def _define_PKEY_Hardware_ShellAttributes():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=4100)
def _define_PKEY_Hardware_Status():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=4096)
def _define_PKEY_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=10)
def _define_PKEY_Device_DeviceDesc():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=2)
def _define_PKEY_Device_HardwareIds():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=3)
def _define_PKEY_Device_CompatibleIds():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=4)
def _define_PKEY_Device_Service():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=6)
def _define_PKEY_Device_Class():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=9)
def _define_PKEY_Device_ClassGuid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=10)
def _define_PKEY_Device_Driver():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=11)
def _define_PKEY_Device_ConfigFlags():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=12)
def _define_PKEY_Device_Manufacturer():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=13)
def _define_PKEY_Device_FriendlyName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=14)
def _define_PKEY_Device_LocationInfo():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=15)
def _define_PKEY_Device_PDOName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=16)
def _define_PKEY_Device_Capabilities():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=17)
def _define_PKEY_Device_UINumber():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=18)
def _define_PKEY_Device_UpperFilters():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=19)
def _define_PKEY_Device_LowerFilters():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=20)
def _define_PKEY_Device_BusTypeGuid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=21)
def _define_PKEY_Device_LegacyBusType():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=22)
def _define_PKEY_Device_BusNumber():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=23)
def _define_PKEY_Device_EnumeratorName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=24)
def _define_PKEY_Device_Security():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=25)
def _define_PKEY_Device_SecuritySDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=26)
def _define_PKEY_Device_DevType():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=27)
def _define_PKEY_Device_Exclusive():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=28)
def _define_PKEY_Device_Characteristics():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=29)
def _define_PKEY_Device_Address():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=30)
def _define_PKEY_Device_UINumberDescFormat():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=31)
def _define_PKEY_Device_PowerData():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=32)
def _define_PKEY_Device_RemovalPolicy():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=33)
def _define_PKEY_Device_RemovalPolicyDefault():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=34)
def _define_PKEY_Device_RemovalPolicyOverride():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=35)
def _define_PKEY_Device_InstallState():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=36)
def _define_PKEY_Device_LocationPaths():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=37)
def _define_PKEY_Device_BaseContainerId():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=38)
def _define_PKEY_Device_DevNodeStatus():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=2)
def _define_PKEY_Device_ProblemCode():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=3)
def _define_PKEY_Device_EjectionRelations():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=4)
def _define_PKEY_Device_RemovalRelations():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=5)
def _define_PKEY_Device_PowerRelations():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=6)
def _define_PKEY_Device_BusRelations():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=7)
def _define_PKEY_Device_Parent():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=8)
def _define_PKEY_Device_Children():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=9)
def _define_PKEY_Device_Siblings():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=10)
def _define_PKEY_Device_TransportRelations():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=11)
def _define_PKEY_Device_Reported():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80497100-8c73-48b9-aa-d9-ce-38-7e-19-c5-6e'), pid=2)
def _define_PKEY_Device_Legacy():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80497100-8c73-48b9-aa-d9-ce-38-7e-19-c5-6e'), pid=3)
def _define_PKEY_Device_InstanceId():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=256)
def _define_PKEY_Device_ContainerId():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8c7ed206-3f8a-4827-b3-ab-ae-9e-1f-ae-fc-6c'), pid=2)
def _define_PKEY_Device_ModelId():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=2)
def _define_PKEY_Device_FriendlyNameAttributes():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=3)
def _define_PKEY_Device_ManufacturerAttributes():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=4)
def _define_PKEY_Device_PresenceNotForDevice():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=5)
def _define_PKEY_Device_SignalStrength():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=6)
def _define_PKEY_Device_IsAssociateableByUserAction():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=7)
def _define_PKEY_Numa_Proximity_Domain():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=1)
def _define_PKEY_Device_DHP_Rebalance_Policy():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=2)
def _define_PKEY_Device_Numa_Node():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=3)
def _define_PKEY_Device_BusReportedDeviceDesc():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=4)
def _define_PKEY_Device_InstallInProgress():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=9)
def _define_PKEY_Device_DriverDate():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=2)
def _define_PKEY_Device_DriverVersion():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=3)
def _define_PKEY_Device_DriverDesc():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=4)
def _define_PKEY_Device_DriverInfPath():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=5)
def _define_PKEY_Device_DriverInfSection():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=6)
def _define_PKEY_Device_DriverInfSectionExt():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=7)
def _define_PKEY_Device_MatchingDeviceId():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=8)
def _define_PKEY_Device_DriverProvider():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=9)
def _define_PKEY_Device_DriverPropPageProvider():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=10)
def _define_PKEY_Device_DriverCoInstallers():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=11)
def _define_PKEY_Device_ResourcePickerTags():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=12)
def _define_PKEY_Device_ResourcePickerExceptions():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=13)
def _define_PKEY_Device_DriverRank():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=14)
def _define_PKEY_Device_DriverLogoLevel():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=15)
def _define_PKEY_Device_NoConnectSound():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=17)
def _define_PKEY_Device_GenericDriverInstalled():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=18)
def _define_PKEY_Device_AdditionalSoftwareRequested():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=19)
def _define_PKEY_Device_SafeRemovalRequired():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afd97640-86a3-4210-b6-7c-28-9c-41-aa-be-55'), pid=2)
def _define_PKEY_Device_SafeRemovalRequiredOverride():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afd97640-86a3-4210-b6-7c-28-9c-41-aa-be-55'), pid=3)
def _define_PKEY_DrvPkg_Model():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=2)
def _define_PKEY_DrvPkg_VendorWebSite():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=3)
def _define_PKEY_DrvPkg_DetailedDescription():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=4)
def _define_PKEY_DrvPkg_DocumentationLink():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=5)
def _define_PKEY_DrvPkg_Icon():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=6)
def _define_PKEY_DrvPkg_BrandingIcon():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=7)
def _define_PKEY_DeviceClass_UpperFilters():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=19)
def _define_PKEY_DeviceClass_LowerFilters():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=20)
def _define_PKEY_DeviceClass_Security():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=25)
def _define_PKEY_DeviceClass_SecuritySDS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=26)
def _define_PKEY_DeviceClass_DevType():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=27)
def _define_PKEY_DeviceClass_Exclusive():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=28)
def _define_PKEY_DeviceClass_Characteristics():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=29)
def _define_PKEY_DeviceClass_Name():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=2)
def _define_PKEY_DeviceClass_ClassName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=3)
def _define_PKEY_DeviceClass_Icon():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=4)
def _define_PKEY_DeviceClass_ClassInstaller():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=5)
def _define_PKEY_DeviceClass_PropPageProvider():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=6)
def _define_PKEY_DeviceClass_NoInstallClass():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=7)
def _define_PKEY_DeviceClass_NoDisplayClass():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=8)
def _define_PKEY_DeviceClass_SilentInstall():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=9)
def _define_PKEY_DeviceClass_NoUseClass():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=10)
def _define_PKEY_DeviceClass_DefaultService():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=11)
def _define_PKEY_DeviceClass_IconPath():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=12)
def _define_PKEY_DeviceClass_ClassCoInstallers():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('713d1703-a2e2-49f5-92-14-56-47-2e-f3-da-5c'), pid=2)
def _define_PKEY_DeviceInterface_FriendlyName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=2)
def _define_PKEY_DeviceInterface_Enabled():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=3)
def _define_PKEY_DeviceInterface_ClassGuid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=4)
def _define_PKEY_DeviceInterfaceClass_DefaultInterface():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14c83a99-0b3f-44b7-be-4c-a1-78-d3-99-05-64'), pid=2)
FD_LONGHORN = 1
FD_SUBKEY = 'SOFTWARE\\Microsoft\\Function Discovery\\'
FCTN_CATEGORY_PNP = 'Provider\\Microsoft.Base.PnP'
FCTN_CATEGORY_REGISTRY = 'Provider\\Microsoft.Base.Registry'
FCTN_CATEGORY_SSDP = 'Provider\\Microsoft.Networking.SSDP'
FCTN_CATEGORY_WSDISCOVERY = 'Provider\\Microsoft.Networking.WSD'
FCTN_CATEGORY_NETBIOS = 'Provider\\Microsoft.Networking.Netbios'
FCTN_CATEGORY_WCN = 'Provider\\Microsoft.Networking.WCN'
FCTN_CATEGORY_PUBLICATION = 'Provider\\Microsoft.Base.Publication'
FCTN_CATEGORY_PNPXASSOCIATION = 'Provider\\Microsoft.PnPX.Association'
FCTN_CATEGORY_BT = 'Provider\\Microsoft.Devices.Bluetooth'
FCTN_CATEGORY_WUSB = 'Provider\\Microsoft.Devices.WirelessUSB'
FCTN_CATEGORY_DEVICEDISPLAYOBJECTS = 'Provider\\Microsoft.Base.DeviceDisplayObjects'
FCTN_CATEGORY_DEVQUERYOBJECTS = 'Provider\\Microsoft.Base.DevQueryObjects'
FCTN_CATEGORY_NETWORKDEVICES = 'Layered\\Microsoft.Networking.Devices'
FCTN_CATEGORY_DEVICES = 'Layered\\Microsoft.Base.Devices'
FCTN_CATEGORY_DEVICEFUNCTIONENUMERATORS = 'Layered\\Microsoft.Devices.FunctionEnumerators'
FCTN_CATEGORY_DEVICEPAIRING = 'Layered\\Microsoft.Base.DevicePairing'
FCTN_SUBCAT_DEVICES_WSDPRINTERS = 'WSDPrinters'
FCTN_SUBCAT_NETWORKDEVICES_SSDP = 'SSDP'
FCTN_SUBCAT_NETWORKDEVICES_WSD = 'WSD'
FCTN_SUBCAT_REG_PUBLICATION = 'Publication'
FCTN_SUBCAT_REG_DIRECTED = 'Directed'
MAX_FDCONSTRAINTNAME_LENGTH = 100
MAX_FDCONSTRAINTVALUE_LENGTH = 1000
FD_QUERYCONSTRAINT_PROVIDERINSTANCEID = 'ProviderInstanceID'
FD_QUERYCONSTRAINT_SUBCATEGORY = 'Subcategory'
FD_QUERYCONSTRAINT_RECURSESUBCATEGORY = 'RecurseSubcategory'
FD_QUERYCONSTRAINT_VISIBILITY = 'Visibility'
FD_QUERYCONSTRAINT_COMCLSCONTEXT = 'COMClsContext'
FD_QUERYCONSTRAINT_ROUTINGSCOPE = 'RoutingScope'
FD_CONSTRAINTVALUE_TRUE = 'TRUE'
FD_CONSTRAINTVALUE_FALSE = 'FALSE'
FD_CONSTRAINTVALUE_RECURSESUBCATEGORY_TRUE = 'TRUE'
FD_CONSTRAINTVALUE_VISIBILITY_DEFAULT = '0'
FD_CONSTRAINTVALUE_VISIBILITY_ALL = '1'
FD_CONSTRAINTVALUE_COMCLSCONTEXT_INPROC_SERVER = '1'
FD_CONSTRAINTVALUE_COMCLSCONTEXT_LOCAL_SERVER = '4'
FD_CONSTRAINTVALUE_PAIRED = 'Paired'
FD_CONSTRAINTVALUE_UNPAIRED = 'UnPaired'
FD_CONSTRAINTVALUE_ALL = 'All'
FD_CONSTRAINTVALUE_ROUTINGSCOPE_ALL = 'All'
FD_CONSTRAINTVALUE_ROUTINGSCOPE_DIRECT = 'Direct'
FD_QUERYCONSTRAINT_PAIRING_STATE = 'PairingState'
FD_QUERYCONSTRAINT_INQUIRY_TIMEOUT = 'InquiryModeTimeout'
PROVIDERPNP_QUERYCONSTRAINT_INTERFACECLASS = 'InterfaceClass'
PROVIDERPNP_QUERYCONSTRAINT_NOTPRESENT = 'NotPresent'
PROVIDERPNP_QUERYCONSTRAINT_NOTIFICATIONSONLY = 'NotifyOnly'
PNP_CONSTRAINTVALUE_NOTPRESENT = 'TRUE'
PNP_CONSTRAINTVALUE_NOTIFICATIONSONLY = 'TRUE'
PROVIDERSSDP_QUERYCONSTRAINT_TYPE = 'Type'
PROVIDERSSDP_QUERYCONSTRAINT_CUSTOMXMLPROPERTY = 'CustomXmlProperty'
SSDP_CONSTRAINTVALUE_TYPE_ALL = 'ssdp:all'
SSDP_CONSTRAINTVALUE_TYPE_ROOT = 'upnp:rootdevice'
SSDP_CONSTRAINTVALUE_TYPE_DEVICE_PREFIX = 'urn:schemas-upnp-org:device:'
SSDP_CONSTRAINTVALUE_TYPE_SVC_PREFIX = 'urn:schemas-upnp-org:service:'
PROVIDERWSD_QUERYCONSTRAINT_DIRECTEDADDRESS = 'RemoteAddress'
PROVIDERWSD_QUERYCONSTRAINT_TYPE = 'Type'
PROVIDERWSD_QUERYCONSTRAINT_SCOPE = 'Scope'
PROVIDERWSD_QUERYCONSTRAINT_SECURITY_REQUIREMENTS = 'SecurityRequirements'
PROVIDERWSD_QUERYCONSTRAINT_SSL_CERT_FOR_CLIENT_AUTH = 'SSLClientAuthCert'
PROVIDERWSD_QUERYCONSTRAINT_SSL_CERTHASH_FOR_SERVER_AUTH = 'SSLServerAuthCertHash'
WSD_CONSTRAINTVALUE_REQUIRE_SECURECHANNEL = '1'
WSD_CONSTRAINTVALUE_REQUIRE_SECURECHANNEL_AND_COMPACTSIGNATURE = '2'
WSD_CONSTRAINTVALUE_NO_TRUST_VERIFICATION = '3'
PROVIDERWNET_QUERYCONSTRAINT_TYPE = 'Type'
PROVIDERWNET_QUERYCONSTRAINT_PROPERTIES = 'Properties'
PROVIDERWNET_QUERYCONSTRAINT_RESOURCETYPE = 'ResourceType'
WNET_CONSTRAINTVALUE_TYPE_ALL = 'All'
WNET_CONSTRAINTVALUE_TYPE_SERVER = 'Server'
WNET_CONSTRAINTVALUE_TYPE_DOMAIN = 'Domain'
WNET_CONSTRAINTVALUE_PROPERTIES_ALL = 'All'
WNET_CONSTRAINTVALUE_PROPERTIES_LIMITED = 'Limited'
WNET_CONSTRAINTVALUE_RESOURCETYPE_DISK = 'Disk'
WNET_CONSTRAINTVALUE_RESOURCETYPE_PRINTER = 'Printer'
WNET_CONSTRAINTVALUE_RESOURCETYPE_DISKORPRINTER = 'DiskOrPrinter'
ONLINE_PROVIDER_DEVICES_QUERYCONSTRAINT_OWNERNAME = 'OwnerName'
PROVIDERDDO_QUERYCONSTRAINT_DEVICEFUNCTIONDISPLAYOBJECTS = 'DeviceFunctionDisplayObjects'
PROVIDERDDO_QUERYCONSTRAINT_ONLYCONNECTEDDEVICES = 'OnlyConnectedDevices'
PROVIDERDDO_QUERYCONSTRAINT_DEVICEINTERFACES = 'DeviceInterfaces'
E_FDPAIRING_NOCONNECTION = -1882193919
E_FDPAIRING_HWFAILURE = -1882193918
E_FDPAIRING_AUTHFAILURE = -1882193917
E_FDPAIRING_CONNECTTIMEOUT = -1882193916
E_FDPAIRING_TOOMANYCONNECTIONS = -1882193915
E_FDPAIRING_AUTHNOTALLOWED = -1882193914
E_FDPAIRING_IPBUSDISABLED = -1882193913
E_FDPAIRING_NOPROFILES = -1882193912
FunctionDiscovery = Guid('c72be2ec-8e90-452c-b2-9a-ab-8f-f1-c0-71-fc')
FunctionInstanceCollection = Guid('ba818ce5-b55f-443f-ad-39-2f-e8-9b-e6-19-1f')
def _define_IFunctionDiscovery_head():
    class IFunctionDiscovery(win32more.System.Com.IUnknown_head):
        Guid = Guid('4df99b70-e148-4432-b0-04-4c-9e-eb-53-5a-5e')
    return IFunctionDiscovery
def _define_IFunctionDiscovery():
    IFunctionDiscovery = win32more.Devices.FunctionDiscovery.IFunctionDiscovery_head
    IFunctionDiscovery.GetInstanceCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head))(3, 'GetInstanceCollection', ((1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'fIncludeAllSubCategories'),(1, 'ppIFunctionInstanceCollection'),)))
    IFunctionDiscovery.GetInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head))(4, 'GetInstance', ((1, 'pszFunctionInstanceIdentity'),(1, 'ppIFunctionInstance'),)))
    IFunctionDiscovery.CreateInstanceCollectionQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head,POINTER(UInt64),POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollectionQuery_head))(5, 'CreateInstanceCollectionQuery', ((1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'fIncludeAllSubCategories'),(1, 'pIFunctionDiscoveryNotification'),(1, 'pfdqcQueryContext'),(1, 'ppIFunctionInstanceCollectionQuery'),)))
    IFunctionDiscovery.CreateInstanceQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head,POINTER(UInt64),POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceQuery_head))(6, 'CreateInstanceQuery', ((1, 'pszFunctionInstanceIdentity'),(1, 'pIFunctionDiscoveryNotification'),(1, 'pfdqcQueryContext'),(1, 'ppIFunctionInstanceQuery'),)))
    IFunctionDiscovery.AddInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head))(7, 'AddInstance', ((1, 'enumSystemVisibility'),(1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'pszCategoryIdentity'),(1, 'ppIFunctionInstance'),)))
    IFunctionDiscovery.RemoveInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(8, 'RemoveInstance', ((1, 'enumSystemVisibility'),(1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'pszCategoryIdentity'),)))
    win32more.System.Com.IUnknown
    return IFunctionDiscovery
def _define_IFunctionDiscoveryNotification_head():
    class IFunctionDiscoveryNotification(win32more.System.Com.IUnknown_head):
        Guid = Guid('5f6c1ba8-5330-422e-a3-68-57-2b-24-4d-3f-87')
    return IFunctionDiscoveryNotification
def _define_IFunctionDiscoveryNotification():
    IFunctionDiscoveryNotification = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head
    IFunctionDiscoveryNotification.OnUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.QueryUpdateAction,UInt64,win32more.Devices.FunctionDiscovery.IFunctionInstance_head)(3, 'OnUpdate', ((1, 'enumQueryUpdateAction'),(1, 'fdqcQueryContext'),(1, 'pIFunctionInstance'),)))
    IFunctionDiscoveryNotification.OnError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt64,win32more.Foundation.PWSTR)(4, 'OnError', ((1, 'hr'),(1, 'fdqcQueryContext'),(1, 'pszProvider'),)))
    IFunctionDiscoveryNotification.OnEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt64,win32more.Foundation.PWSTR)(5, 'OnEvent', ((1, 'dwEventID'),(1, 'fdqcQueryContext'),(1, 'pszProvider'),)))
    win32more.System.Com.IUnknown
    return IFunctionDiscoveryNotification
def _define_IFunctionDiscoveryProvider_head():
    class IFunctionDiscoveryProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcde394f-1478-4813-a4-02-f6-fb-10-65-72-22')
    return IFunctionDiscoveryProvider
def _define_IFunctionDiscoveryProvider():
    IFunctionDiscoveryProvider = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProvider_head
    IFunctionDiscoveryProvider.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderFactory_head,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head,UInt32,POINTER(UInt32))(3, 'Initialize', ((1, 'pIFunctionDiscoveryProviderFactory'),(1, 'pIFunctionDiscoveryNotification'),(1, 'lcidUserDefault'),(1, 'pdwStgAccessCapabilities'),)))
    IFunctionDiscoveryProvider.Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderQuery_head,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head))(4, 'Query', ((1, 'pIFunctionDiscoveryProviderQuery'),(1, 'ppIFunctionInstanceCollection'),)))
    IFunctionDiscoveryProvider.EndQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'EndQuery', ()))
    IFunctionDiscoveryProvider.InstancePropertyStoreValidateAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,UInt32)(6, 'InstancePropertyStoreValidateAccess', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'dwStgAccess'),)))
    IFunctionDiscoveryProvider.InstancePropertyStoreOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head))(7, 'InstancePropertyStoreOpen', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'dwStgAccess'),(1, 'ppIPropertyStore'),)))
    IFunctionDiscoveryProvider.InstancePropertyStoreFlush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr)(8, 'InstancePropertyStoreFlush', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),)))
    IFunctionDiscoveryProvider.InstanceQueryService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(9, 'InstanceQueryService', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'guidService'),(1, 'riid'),(1, 'ppIUnknown'),)))
    IFunctionDiscoveryProvider.InstanceReleased = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr)(10, 'InstanceReleased', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),)))
    win32more.System.Com.IUnknown
    return IFunctionDiscoveryProvider
def _define_IFunctionDiscoveryProviderFactory_head():
    class IFunctionDiscoveryProviderFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('86443ff0-1ad5-4e68-a4-5a-40-c2-c3-29-de-3b')
    return IFunctionDiscoveryProviderFactory
def _define_IFunctionDiscoveryProviderFactory():
    IFunctionDiscoveryProviderFactory = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderFactory_head
    IFunctionDiscoveryProviderFactory.CreatePropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head))(3, 'CreatePropertyStore', ((1, 'ppIPropertyStore'),)))
    IFunctionDiscoveryProviderFactory.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,IntPtr,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProvider_head,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head))(4, 'CreateInstance', ((1, 'pszSubCategory'),(1, 'pszProviderInstanceIdentity'),(1, 'iProviderInstanceContext'),(1, 'pIPropertyStore'),(1, 'pIFunctionDiscoveryProvider'),(1, 'ppIFunctionInstance'),)))
    IFunctionDiscoveryProviderFactory.CreateFunctionInstanceCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head))(5, 'CreateFunctionInstanceCollection', ((1, 'ppIFunctionInstanceCollection'),)))
    win32more.System.Com.IUnknown
    return IFunctionDiscoveryProviderFactory
def _define_IFunctionDiscoveryProviderQuery_head():
    class IFunctionDiscoveryProviderQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('6876ea98-baec-46db-bc-20-75-a7-6e-26-7a-3a')
    return IFunctionDiscoveryProviderQuery
def _define_IFunctionDiscoveryProviderQuery():
    IFunctionDiscoveryProviderQuery = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderQuery_head
    IFunctionDiscoveryProviderQuery.IsInstanceQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(POINTER(UInt16)))(3, 'IsInstanceQuery', ((1, 'pisInstanceQuery'),(1, 'ppszConstraintValue'),)))
    IFunctionDiscoveryProviderQuery.IsSubcategoryQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(POINTER(UInt16)))(4, 'IsSubcategoryQuery', ((1, 'pisSubcategoryQuery'),(1, 'ppszConstraintValue'),)))
    IFunctionDiscoveryProviderQuery.GetQueryConstraints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IProviderQueryConstraintCollection_head))(5, 'GetQueryConstraints', ((1, 'ppIProviderQueryConstraints'),)))
    IFunctionDiscoveryProviderQuery.GetPropertyConstraints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IProviderPropertyConstraintCollection_head))(6, 'GetPropertyConstraints', ((1, 'ppIProviderPropertyConstraints'),)))
    win32more.System.Com.IUnknown
    return IFunctionDiscoveryProviderQuery
def _define_IFunctionDiscoveryServiceProvider_head():
    class IFunctionDiscoveryServiceProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('4c81ed02-1b04-43f2-a4-51-69-96-6c-bc-d1-c2')
    return IFunctionDiscoveryServiceProvider
def _define_IFunctionDiscoveryServiceProvider():
    IFunctionDiscoveryServiceProvider = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryServiceProvider_head
    IFunctionDiscoveryServiceProvider.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,POINTER(Guid),POINTER(c_void_p))(3, 'Initialize', ((1, 'pIFunctionInstance'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IFunctionDiscoveryServiceProvider
def _define_IFunctionInstance_head():
    class IFunctionInstance(win32more.System.Com.IServiceProvider_head):
        Guid = Guid('33591c10-0bed-4f02-b0-ab-15-30-d5-53-3e-e9')
    return IFunctionInstance
def _define_IFunctionInstance():
    IFunctionInstance = win32more.Devices.FunctionDiscovery.IFunctionInstance_head
    IFunctionInstance.GetID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)))(4, 'GetID', ((1, 'ppszCoMemIdentity'),)))
    IFunctionInstance.GetProviderInstanceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)))(5, 'GetProviderInstanceID', ((1, 'ppszCoMemProviderInstanceIdentity'),)))
    IFunctionInstance.OpenPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.STGM,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head))(6, 'OpenPropertyStore', ((1, 'dwStgAccess'),(1, 'ppIPropertyStore'),)))
    IFunctionInstance.GetCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)))(7, 'GetCategory', ((1, 'ppszCoMemCategory'),(1, 'ppszCoMemSubCategory'),)))
    win32more.System.Com.IServiceProvider
    return IFunctionInstance
def _define_IFunctionInstanceCollection_head():
    class IFunctionInstanceCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('f0a3d895-855c-42a2-94-8d-2f-97-d4-50-ec-b1')
    return IFunctionInstanceCollection
def _define_IFunctionInstanceCollection():
    IFunctionInstanceCollection = win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head
    IFunctionInstanceCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pdwCount'),)))
    IFunctionInstanceCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head))(4, 'Get', ((1, 'pszInstanceIdentity'),(1, 'pdwIndex'),(1, 'ppIFunctionInstance'),)))
    IFunctionInstanceCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head))(5, 'Item', ((1, 'dwIndex'),(1, 'ppIFunctionInstance'),)))
    IFunctionInstanceCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head)(6, 'Add', ((1, 'pIFunctionInstance'),)))
    IFunctionInstanceCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head))(7, 'Remove', ((1, 'dwIndex'),(1, 'ppIFunctionInstance'),)))
    IFunctionInstanceCollection.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(8, 'Delete', ((1, 'dwIndex'),)))
    IFunctionInstanceCollection.DeleteAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'DeleteAll', ()))
    win32more.System.Com.IUnknown
    return IFunctionInstanceCollection
def _define_IFunctionInstanceCollectionQuery_head():
    class IFunctionInstanceCollectionQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('57cc6fd2-c09a-4289-bb-72-25-f0-41-42-05-8e')
    return IFunctionInstanceCollectionQuery
def _define_IFunctionInstanceCollectionQuery():
    IFunctionInstanceCollectionQuery = win32more.Devices.FunctionDiscovery.IFunctionInstanceCollectionQuery_head
    IFunctionInstanceCollectionQuery.AddQueryConstraint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(3, 'AddQueryConstraint', ((1, 'pszConstraintName'),(1, 'pszConstraintValue'),)))
    IFunctionInstanceCollectionQuery.AddPropertyConstraint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.Devices.FunctionDiscovery.PropertyConstraint)(4, 'AddPropertyConstraint', ((1, 'Key'),(1, 'pv'),(1, 'enumPropertyConstraint'),)))
    IFunctionInstanceCollectionQuery.Execute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head))(5, 'Execute', ((1, 'ppIFunctionInstanceCollection'),)))
    win32more.System.Com.IUnknown
    return IFunctionInstanceCollectionQuery
def _define_IFunctionInstanceQuery_head():
    class IFunctionInstanceQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('6242bc6b-90ec-4b37-bb-46-e2-29-fd-84-ed-95')
    return IFunctionInstanceQuery
def _define_IFunctionInstanceQuery():
    IFunctionInstanceQuery = win32more.Devices.FunctionDiscovery.IFunctionInstanceQuery_head
    IFunctionInstanceQuery.Execute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head))(3, 'Execute', ((1, 'ppIFunctionInstance'),)))
    win32more.System.Com.IUnknown
    return IFunctionInstanceQuery
def _define_IPNPXAssociation_head():
    class IPNPXAssociation(win32more.System.Com.IUnknown_head):
        Guid = Guid('0bd7e521-4da6-42d5-81-ba-19-81-b6-b9-40-75')
    return IPNPXAssociation
def _define_IPNPXAssociation():
    IPNPXAssociation = win32more.Devices.FunctionDiscovery.IPNPXAssociation_head
    IPNPXAssociation.Associate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'Associate', ((1, 'pszSubcategory'),)))
    IPNPXAssociation.Unassociate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(4, 'Unassociate', ((1, 'pszSubcategory'),)))
    IPNPXAssociation.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(5, 'Delete', ((1, 'pszSubcategory'),)))
    win32more.System.Com.IUnknown
    return IPNPXAssociation
def _define_IPNPXDeviceAssociation_head():
    class IPNPXDeviceAssociation(win32more.System.Com.IUnknown_head):
        Guid = Guid('eed366d0-35b8-4fc5-8d-20-7e-5b-d3-1f-6d-ed')
    return IPNPXDeviceAssociation
def _define_IPNPXDeviceAssociation():
    IPNPXDeviceAssociation = win32more.Devices.FunctionDiscovery.IPNPXDeviceAssociation_head
    IPNPXDeviceAssociation.Associate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head)(3, 'Associate', ((1, 'pszSubCategory'),(1, 'pIFunctionDiscoveryNotification'),)))
    IPNPXDeviceAssociation.Unassociate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head)(4, 'Unassociate', ((1, 'pszSubCategory'),(1, 'pIFunctionDiscoveryNotification'),)))
    IPNPXDeviceAssociation.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head)(5, 'Delete', ((1, 'pszSubcategory'),(1, 'pIFunctionDiscoveryNotification'),)))
    win32more.System.Com.IUnknown
    return IPNPXDeviceAssociation
def _define_IPropertyStoreCollection_head():
    class IPropertyStoreCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('d14d9c30-12d2-42d8-bc-e4-c6-0c-2b-b2-26-fa')
    return IPropertyStoreCollection
def _define_IPropertyStoreCollection():
    IPropertyStoreCollection = win32more.Devices.FunctionDiscovery.IPropertyStoreCollection_head
    IPropertyStoreCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pdwCount'),)))
    IPropertyStoreCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head))(4, 'Get', ((1, 'pszInstanceIdentity'),(1, 'pdwIndex'),(1, 'ppIPropertyStore'),)))
    IPropertyStoreCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head))(5, 'Item', ((1, 'dwIndex'),(1, 'ppIPropertyStore'),)))
    IPropertyStoreCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)(6, 'Add', ((1, 'pIPropertyStore'),)))
    IPropertyStoreCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head))(7, 'Remove', ((1, 'dwIndex'),(1, 'pIPropertyStore'),)))
    IPropertyStoreCollection.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(8, 'Delete', ((1, 'dwIndex'),)))
    IPropertyStoreCollection.DeleteAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'DeleteAll', ()))
    win32more.System.Com.IUnknown
    return IPropertyStoreCollection
def _define_IProviderProperties_head():
    class IProviderProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('cf986ea6-3b5f-4c5f-b8-8a-2f-8b-20-ce-ef-17')
    return IProviderProperties
def _define_IProviderProperties():
    IProviderProperties = win32more.Devices.FunctionDiscovery.IProviderProperties_head
    IProviderProperties.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(UInt32))(3, 'GetCount', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'pdwCount'),)))
    IProviderProperties.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(4, 'GetAt', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'dwIndex'),(1, 'pKey'),)))
    IProviderProperties.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(5, 'GetValue', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'Key'),(1, 'ppropVar'),)))
    IProviderProperties.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(6, 'SetValue', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'Key'),(1, 'ppropVar'),)))
    win32more.System.Com.IUnknown
    return IProviderProperties
def _define_IProviderPropertyConstraintCollection_head():
    class IProviderPropertyConstraintCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('f4fae42f-5778-4a13-85-40-b5-fd-8c-13-98-dd')
    return IProviderPropertyConstraintCollection
def _define_IProviderPropertyConstraintCollection():
    IProviderPropertyConstraintCollection = win32more.Devices.FunctionDiscovery.IProviderPropertyConstraintCollection_head
    IProviderPropertyConstraintCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pdwCount'),)))
    IProviderPropertyConstraintCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32))(4, 'Get', ((1, 'Key'),(1, 'pPropVar'),(1, 'pdwPropertyConstraint'),)))
    IProviderPropertyConstraintCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32))(5, 'Item', ((1, 'dwIndex'),(1, 'pKey'),(1, 'pPropVar'),(1, 'pdwPropertyConstraint'),)))
    IProviderPropertyConstraintCollection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32))(6, 'Next', ((1, 'pKey'),(1, 'pPropVar'),(1, 'pdwPropertyConstraint'),)))
    IProviderPropertyConstraintCollection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Skip', ()))
    IProviderPropertyConstraintCollection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Reset', ()))
    win32more.System.Com.IUnknown
    return IProviderPropertyConstraintCollection
def _define_IProviderPublishing_head():
    class IProviderPublishing(win32more.System.Com.IUnknown_head):
        Guid = Guid('cd1b9a04-206c-4a05-a0-c8-16-35-a2-1a-2b-7c')
    return IProviderPublishing
def _define_IProviderPublishing():
    IProviderPublishing = win32more.Devices.FunctionDiscovery.IProviderPublishing_head
    IProviderPublishing.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head))(3, 'CreateInstance', ((1, 'enumVisibilityFlags'),(1, 'pszSubCategory'),(1, 'pszProviderInstanceIdentity'),(1, 'ppIFunctionInstance'),)))
    IProviderPublishing.RemoveInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(4, 'RemoveInstance', ((1, 'enumVisibilityFlags'),(1, 'pszSubCategory'),(1, 'pszProviderInstanceIdentity'),)))
    win32more.System.Com.IUnknown
    return IProviderPublishing
def _define_IProviderQueryConstraintCollection_head():
    class IProviderQueryConstraintCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('9c243e11-3261-4bcd-b9-22-84-a8-73-d4-60-ae')
    return IProviderQueryConstraintCollection
def _define_IProviderQueryConstraintCollection():
    IProviderQueryConstraintCollection = win32more.Devices.FunctionDiscovery.IProviderQueryConstraintCollection_head
    IProviderQueryConstraintCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pdwCount'),)))
    IProviderQueryConstraintCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)))(4, 'Get', ((1, 'pszConstraintName'),(1, 'ppszConstraintValue'),)))
    IProviderQueryConstraintCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)))(5, 'Item', ((1, 'dwIndex'),(1, 'ppszConstraintName'),(1, 'ppszConstraintValue'),)))
    IProviderQueryConstraintCollection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)))(6, 'Next', ((1, 'ppszConstraintName'),(1, 'ppszConstraintValue'),)))
    IProviderQueryConstraintCollection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Skip', ()))
    IProviderQueryConstraintCollection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Reset', ()))
    win32more.System.Com.IUnknown
    return IProviderQueryConstraintCollection
PNPXAssociation = Guid('cee8ccc9-4f6b-4469-a2-35-5a-22-86-9e-ef-03')
PNPXPairingHandler = Guid('b8a27942-ade7-4085-aa-6e-4f-ad-c7-ad-a1-ef')
PropertyConstraint = Int32
QC_EQUALS = 0
QC_NOTEQUAL = 1
QC_LESSTHAN = 2
QC_LESSTHANOREQUAL = 3
QC_GREATERTHAN = 4
QC_GREATERTHANOREQUAL = 5
QC_STARTSWITH = 6
QC_EXISTS = 7
QC_DOESNOTEXIST = 8
QC_CONTAINS = 9
PropertyStore = Guid('e4796550-df61-448b-91-93-13-fc-13-41-b1-63')
PropertyStoreCollection = Guid('edd36029-d753-4862-aa-5b-5b-cc-ad-2a-4d-29')
QueryCategoryType = Int32
QCT_PROVIDER = 0
QCT_LAYERED = 1
QueryUpdateAction = Int32
QUA_ADD = 0
QUA_REMOVE = 1
QUA_CHANGE = 2
SystemVisibilityFlags = Int32
SVF_SYSTEM = 0
SVF_USER = 1
__all__ = [
    "DEVICEDISPLAY_DISCOVERYMETHOD_AD_PRINTER",
    "DEVICEDISPLAY_DISCOVERYMETHOD_ASP_INFRA",
    "DEVICEDISPLAY_DISCOVERYMETHOD_BLUETOOTH",
    "DEVICEDISPLAY_DISCOVERYMETHOD_BLUETOOTH_LE",
    "DEVICEDISPLAY_DISCOVERYMETHOD_NETBIOS",
    "DEVICEDISPLAY_DISCOVERYMETHOD_PNP",
    "DEVICEDISPLAY_DISCOVERYMETHOD_UPNP",
    "DEVICEDISPLAY_DISCOVERYMETHOD_WFD",
    "DEVICEDISPLAY_DISCOVERYMETHOD_WSD",
    "DEVICEDISPLAY_DISCOVERYMETHOD_WUSB",
    "E_FDPAIRING_AUTHFAILURE",
    "E_FDPAIRING_AUTHNOTALLOWED",
    "E_FDPAIRING_CONNECTTIMEOUT",
    "E_FDPAIRING_HWFAILURE",
    "E_FDPAIRING_IPBUSDISABLED",
    "E_FDPAIRING_NOCONNECTION",
    "E_FDPAIRING_NOPROFILES",
    "E_FDPAIRING_TOOMANYCONNECTIONS",
    "FCTN_CATEGORY_BT",
    "FCTN_CATEGORY_DEVICEDISPLAYOBJECTS",
    "FCTN_CATEGORY_DEVICEFUNCTIONENUMERATORS",
    "FCTN_CATEGORY_DEVICEPAIRING",
    "FCTN_CATEGORY_DEVICES",
    "FCTN_CATEGORY_DEVQUERYOBJECTS",
    "FCTN_CATEGORY_NETBIOS",
    "FCTN_CATEGORY_NETWORKDEVICES",
    "FCTN_CATEGORY_PNP",
    "FCTN_CATEGORY_PNPXASSOCIATION",
    "FCTN_CATEGORY_PUBLICATION",
    "FCTN_CATEGORY_REGISTRY",
    "FCTN_CATEGORY_SSDP",
    "FCTN_CATEGORY_WCN",
    "FCTN_CATEGORY_WSDISCOVERY",
    "FCTN_CATEGORY_WUSB",
    "FCTN_SUBCAT_DEVICES_WSDPRINTERS",
    "FCTN_SUBCAT_NETWORKDEVICES_SSDP",
    "FCTN_SUBCAT_NETWORKDEVICES_WSD",
    "FCTN_SUBCAT_REG_DIRECTED",
    "FCTN_SUBCAT_REG_PUBLICATION",
    "FD_CONSTRAINTVALUE_ALL",
    "FD_CONSTRAINTVALUE_COMCLSCONTEXT_INPROC_SERVER",
    "FD_CONSTRAINTVALUE_COMCLSCONTEXT_LOCAL_SERVER",
    "FD_CONSTRAINTVALUE_FALSE",
    "FD_CONSTRAINTVALUE_PAIRED",
    "FD_CONSTRAINTVALUE_RECURSESUBCATEGORY_TRUE",
    "FD_CONSTRAINTVALUE_ROUTINGSCOPE_ALL",
    "FD_CONSTRAINTVALUE_ROUTINGSCOPE_DIRECT",
    "FD_CONSTRAINTVALUE_TRUE",
    "FD_CONSTRAINTVALUE_UNPAIRED",
    "FD_CONSTRAINTVALUE_VISIBILITY_ALL",
    "FD_CONSTRAINTVALUE_VISIBILITY_DEFAULT",
    "FD_EVENTID",
    "FD_EVENTID_ASYNCTHREADEXIT",
    "FD_EVENTID_IPADDRESSCHANGE",
    "FD_EVENTID_PRIVATE",
    "FD_EVENTID_QUERYREFRESH",
    "FD_EVENTID_SEARCHCOMPLETE",
    "FD_EVENTID_SEARCHSTART",
    "FD_LONGHORN",
    "FD_QUERYCONSTRAINT_COMCLSCONTEXT",
    "FD_QUERYCONSTRAINT_INQUIRY_TIMEOUT",
    "FD_QUERYCONSTRAINT_PAIRING_STATE",
    "FD_QUERYCONSTRAINT_PROVIDERINSTANCEID",
    "FD_QUERYCONSTRAINT_RECURSESUBCATEGORY",
    "FD_QUERYCONSTRAINT_ROUTINGSCOPE",
    "FD_QUERYCONSTRAINT_SUBCATEGORY",
    "FD_QUERYCONSTRAINT_VISIBILITY",
    "FD_SUBKEY",
    "FD_Visibility_Default",
    "FD_Visibility_Hidden",
    "FMTID_Device",
    "FMTID_DeviceInterface",
    "FMTID_FD",
    "FMTID_PNPX",
    "FMTID_PNPXDynamicProperty",
    "FMTID_Pairing",
    "FMTID_WSD",
    "FunctionDiscovery",
    "FunctionInstanceCollection",
    "IFunctionDiscovery",
    "IFunctionDiscoveryNotification",
    "IFunctionDiscoveryProvider",
    "IFunctionDiscoveryProviderFactory",
    "IFunctionDiscoveryProviderQuery",
    "IFunctionDiscoveryServiceProvider",
    "IFunctionInstance",
    "IFunctionInstanceCollection",
    "IFunctionInstanceCollectionQuery",
    "IFunctionInstanceQuery",
    "IPNPXAssociation",
    "IPNPXDeviceAssociation",
    "IPropertyStoreCollection",
    "IProviderProperties",
    "IProviderPropertyConstraintCollection",
    "IProviderPublishing",
    "IProviderQueryConstraintCollection",
    "MAX_FDCONSTRAINTNAME_LENGTH",
    "MAX_FDCONSTRAINTVALUE_LENGTH",
    "ONLINE_PROVIDER_DEVICES_QUERYCONSTRAINT_OWNERNAME",
    "PKEY_DeviceClass_Characteristics",
    "PKEY_DeviceClass_ClassCoInstallers",
    "PKEY_DeviceClass_ClassInstaller",
    "PKEY_DeviceClass_ClassName",
    "PKEY_DeviceClass_DefaultService",
    "PKEY_DeviceClass_DevType",
    "PKEY_DeviceClass_Exclusive",
    "PKEY_DeviceClass_Icon",
    "PKEY_DeviceClass_IconPath",
    "PKEY_DeviceClass_LowerFilters",
    "PKEY_DeviceClass_Name",
    "PKEY_DeviceClass_NoDisplayClass",
    "PKEY_DeviceClass_NoInstallClass",
    "PKEY_DeviceClass_NoUseClass",
    "PKEY_DeviceClass_PropPageProvider",
    "PKEY_DeviceClass_Security",
    "PKEY_DeviceClass_SecuritySDS",
    "PKEY_DeviceClass_SilentInstall",
    "PKEY_DeviceClass_UpperFilters",
    "PKEY_DeviceDisplay_Address",
    "PKEY_DeviceDisplay_AlwaysShowDeviceAsConnected",
    "PKEY_DeviceDisplay_AssociationArray",
    "PKEY_DeviceDisplay_BaselineExperienceId",
    "PKEY_DeviceDisplay_Category",
    "PKEY_DeviceDisplay_CategoryGroup_Desc",
    "PKEY_DeviceDisplay_CategoryGroup_Icon",
    "PKEY_DeviceDisplay_Category_Desc_Plural",
    "PKEY_DeviceDisplay_Category_Desc_Singular",
    "PKEY_DeviceDisplay_Category_Icon",
    "PKEY_DeviceDisplay_DeviceDescription1",
    "PKEY_DeviceDisplay_DeviceDescription2",
    "PKEY_DeviceDisplay_DeviceFunctionSubRank",
    "PKEY_DeviceDisplay_DiscoveryMethod",
    "PKEY_DeviceDisplay_ExperienceId",
    "PKEY_DeviceDisplay_FriendlyName",
    "PKEY_DeviceDisplay_Icon",
    "PKEY_DeviceDisplay_InstallInProgress",
    "PKEY_DeviceDisplay_IsAuthenticated",
    "PKEY_DeviceDisplay_IsConnected",
    "PKEY_DeviceDisplay_IsDefaultDevice",
    "PKEY_DeviceDisplay_IsDeviceUniquelyIdentifiable",
    "PKEY_DeviceDisplay_IsEncrypted",
    "PKEY_DeviceDisplay_IsLocalMachine",
    "PKEY_DeviceDisplay_IsMetadataSearchInProgress",
    "PKEY_DeviceDisplay_IsNetworkDevice",
    "PKEY_DeviceDisplay_IsNotInterestingForDisplay",
    "PKEY_DeviceDisplay_IsNotWorkingProperly",
    "PKEY_DeviceDisplay_IsPaired",
    "PKEY_DeviceDisplay_IsSharedDevice",
    "PKEY_DeviceDisplay_IsShowInDisconnectedState",
    "PKEY_DeviceDisplay_Last_Connected",
    "PKEY_DeviceDisplay_Last_Seen",
    "PKEY_DeviceDisplay_LaunchDeviceStageFromExplorer",
    "PKEY_DeviceDisplay_LaunchDeviceStageOnDeviceConnect",
    "PKEY_DeviceDisplay_Manufacturer",
    "PKEY_DeviceDisplay_MetadataCabinet",
    "PKEY_DeviceDisplay_MetadataChecksum",
    "PKEY_DeviceDisplay_MetadataPath",
    "PKEY_DeviceDisplay_ModelName",
    "PKEY_DeviceDisplay_ModelNumber",
    "PKEY_DeviceDisplay_PrimaryCategory",
    "PKEY_DeviceDisplay_RequiresPairingElevation",
    "PKEY_DeviceDisplay_RequiresUninstallElevation",
    "PKEY_DeviceDisplay_UnpairUninstall",
    "PKEY_DeviceDisplay_Version",
    "PKEY_DeviceInterfaceClass_DefaultInterface",
    "PKEY_DeviceInterface_ClassGuid",
    "PKEY_DeviceInterface_Enabled",
    "PKEY_DeviceInterface_FriendlyName",
    "PKEY_Device_AdditionalSoftwareRequested",
    "PKEY_Device_Address",
    "PKEY_Device_BIOSVersion",
    "PKEY_Device_BaseContainerId",
    "PKEY_Device_BusNumber",
    "PKEY_Device_BusRelations",
    "PKEY_Device_BusReportedDeviceDesc",
    "PKEY_Device_BusTypeGuid",
    "PKEY_Device_Capabilities",
    "PKEY_Device_Characteristics",
    "PKEY_Device_Children",
    "PKEY_Device_Class",
    "PKEY_Device_ClassGuid",
    "PKEY_Device_CompatibleIds",
    "PKEY_Device_ConfigFlags",
    "PKEY_Device_ContainerId",
    "PKEY_Device_DHP_Rebalance_Policy",
    "PKEY_Device_DevNodeStatus",
    "PKEY_Device_DevType",
    "PKEY_Device_DeviceDesc",
    "PKEY_Device_Driver",
    "PKEY_Device_DriverCoInstallers",
    "PKEY_Device_DriverDate",
    "PKEY_Device_DriverDesc",
    "PKEY_Device_DriverInfPath",
    "PKEY_Device_DriverInfSection",
    "PKEY_Device_DriverInfSectionExt",
    "PKEY_Device_DriverLogoLevel",
    "PKEY_Device_DriverPropPageProvider",
    "PKEY_Device_DriverProvider",
    "PKEY_Device_DriverRank",
    "PKEY_Device_DriverVersion",
    "PKEY_Device_EjectionRelations",
    "PKEY_Device_EnumeratorName",
    "PKEY_Device_Exclusive",
    "PKEY_Device_FriendlyName",
    "PKEY_Device_FriendlyNameAttributes",
    "PKEY_Device_GenericDriverInstalled",
    "PKEY_Device_HardwareIds",
    "PKEY_Device_InstallInProgress",
    "PKEY_Device_InstallState",
    "PKEY_Device_InstanceId",
    "PKEY_Device_IsAssociateableByUserAction",
    "PKEY_Device_Legacy",
    "PKEY_Device_LegacyBusType",
    "PKEY_Device_LocationInfo",
    "PKEY_Device_LocationPaths",
    "PKEY_Device_LowerFilters",
    "PKEY_Device_Manufacturer",
    "PKEY_Device_ManufacturerAttributes",
    "PKEY_Device_MatchingDeviceId",
    "PKEY_Device_ModelId",
    "PKEY_Device_NoConnectSound",
    "PKEY_Device_Numa_Node",
    "PKEY_Device_PDOName",
    "PKEY_Device_Parent",
    "PKEY_Device_PowerData",
    "PKEY_Device_PowerRelations",
    "PKEY_Device_PresenceNotForDevice",
    "PKEY_Device_ProblemCode",
    "PKEY_Device_RemovalPolicy",
    "PKEY_Device_RemovalPolicyDefault",
    "PKEY_Device_RemovalPolicyOverride",
    "PKEY_Device_RemovalRelations",
    "PKEY_Device_Reported",
    "PKEY_Device_ResourcePickerExceptions",
    "PKEY_Device_ResourcePickerTags",
    "PKEY_Device_SafeRemovalRequired",
    "PKEY_Device_SafeRemovalRequiredOverride",
    "PKEY_Device_Security",
    "PKEY_Device_SecuritySDS",
    "PKEY_Device_Service",
    "PKEY_Device_Siblings",
    "PKEY_Device_SignalStrength",
    "PKEY_Device_TransportRelations",
    "PKEY_Device_UINumber",
    "PKEY_Device_UINumberDescFormat",
    "PKEY_Device_UpperFilters",
    "PKEY_DrvPkg_BrandingIcon",
    "PKEY_DrvPkg_DetailedDescription",
    "PKEY_DrvPkg_DocumentationLink",
    "PKEY_DrvPkg_Icon",
    "PKEY_DrvPkg_Model",
    "PKEY_DrvPkg_VendorWebSite",
    "PKEY_FunctionInstance",
    "PKEY_Hardware_Devinst",
    "PKEY_Hardware_DisplayAttribute",
    "PKEY_Hardware_DriverDate",
    "PKEY_Hardware_DriverProvider",
    "PKEY_Hardware_DriverVersion",
    "PKEY_Hardware_Function",
    "PKEY_Hardware_Icon",
    "PKEY_Hardware_Image",
    "PKEY_Hardware_Manufacturer",
    "PKEY_Hardware_Model",
    "PKEY_Hardware_Name",
    "PKEY_Hardware_SerialNumber",
    "PKEY_Hardware_ShellAttributes",
    "PKEY_Hardware_Status",
    "PKEY_NAME",
    "PKEY_Numa_Proximity_Domain",
    "PKEY_PNPX_Associated",
    "PKEY_PNPX_Category_Desc_NonPlural",
    "PKEY_PNPX_CompactSignature",
    "PKEY_PNPX_CompatibleTypes",
    "PKEY_PNPX_DeviceCategory",
    "PKEY_PNPX_DeviceCategory_Desc",
    "PKEY_PNPX_DeviceCertHash",
    "PKEY_PNPX_DomainName",
    "PKEY_PNPX_FirmwareVersion",
    "PKEY_PNPX_GlobalIdentity",
    "PKEY_PNPX_ID",
    "PKEY_PNPX_IPBusEnumerated",
    "PKEY_PNPX_InstallState",
    "PKEY_PNPX_Installable",
    "PKEY_PNPX_IpAddress",
    "PKEY_PNPX_ManufacturerUrl",
    "PKEY_PNPX_MetadataVersion",
    "PKEY_PNPX_ModelUrl",
    "PKEY_PNPX_NetworkInterfaceGuid",
    "PKEY_PNPX_NetworkInterfaceLuid",
    "PKEY_PNPX_PhysicalAddress",
    "PKEY_PNPX_PresentationUrl",
    "PKEY_PNPX_RemoteAddress",
    "PKEY_PNPX_Removable",
    "PKEY_PNPX_RootProxy",
    "PKEY_PNPX_Scopes",
    "PKEY_PNPX_SecureChannel",
    "PKEY_PNPX_SerialNumber",
    "PKEY_PNPX_ServiceAddress",
    "PKEY_PNPX_ServiceControlUrl",
    "PKEY_PNPX_ServiceDescUrl",
    "PKEY_PNPX_ServiceEventSubUrl",
    "PKEY_PNPX_ServiceId",
    "PKEY_PNPX_ServiceTypes",
    "PKEY_PNPX_ShareName",
    "PKEY_PNPX_Types",
    "PKEY_PNPX_Upc",
    "PKEY_PNPX_XAddrs",
    "PKEY_Pairing_IsWifiOnlyDevice",
    "PKEY_Pairing_ListItemDefault",
    "PKEY_Pairing_ListItemDescription",
    "PKEY_Pairing_ListItemIcon",
    "PKEY_Pairing_ListItemText",
    "PKEY_SSDP_AltLocationInfo",
    "PKEY_SSDP_DevLifeTime",
    "PKEY_SSDP_NetworkInterface",
    "PKEY_WCN_AssocState",
    "PKEY_WCN_AuthType",
    "PKEY_WCN_ConfigError",
    "PKEY_WCN_ConfigMethods",
    "PKEY_WCN_ConfigState",
    "PKEY_WCN_ConnType",
    "PKEY_WCN_DevicePasswordId",
    "PKEY_WCN_EncryptType",
    "PKEY_WCN_OSVersion",
    "PKEY_WCN_RegistrarType",
    "PKEY_WCN_RequestType",
    "PKEY_WCN_RfBand",
    "PKEY_WCN_VendorExtension",
    "PKEY_WCN_Version",
    "PKEY_WNET_Comment",
    "PKEY_WNET_DisplayType",
    "PKEY_WNET_LocalName",
    "PKEY_WNET_Provider",
    "PKEY_WNET_RemoteName",
    "PKEY_WNET_Scope",
    "PKEY_WNET_Type",
    "PKEY_WNET_Usage",
    "PNPXAssociation",
    "PNPXPairingHandler",
    "PNPX_DEVICECATEGORY_CAMERA",
    "PNPX_DEVICECATEGORY_COMPUTER",
    "PNPX_DEVICECATEGORY_DISPLAYS",
    "PNPX_DEVICECATEGORY_FAX",
    "PNPX_DEVICECATEGORY_GAMING_DEVICE",
    "PNPX_DEVICECATEGORY_HOME_AUTOMATION_SYSTEM",
    "PNPX_DEVICECATEGORY_HOME_SECURITY_SYSTEM",
    "PNPX_DEVICECATEGORY_INPUTDEVICE",
    "PNPX_DEVICECATEGORY_MFP",
    "PNPX_DEVICECATEGORY_MULTIMEDIA_DEVICE",
    "PNPX_DEVICECATEGORY_NETWORK_INFRASTRUCTURE",
    "PNPX_DEVICECATEGORY_OTHER",
    "PNPX_DEVICECATEGORY_PRINTER",
    "PNPX_DEVICECATEGORY_SCANNER",
    "PNPX_DEVICECATEGORY_STORAGE",
    "PNPX_DEVICECATEGORY_TELEPHONE",
    "PNPX_INSTALLSTATE_FAILED",
    "PNPX_INSTALLSTATE_INSTALLED",
    "PNPX_INSTALLSTATE_INSTALLING",
    "PNPX_INSTALLSTATE_NOTINSTALLED",
    "PNP_CONSTRAINTVALUE_NOTIFICATIONSONLY",
    "PNP_CONSTRAINTVALUE_NOTPRESENT",
    "PROVIDERDDO_QUERYCONSTRAINT_DEVICEFUNCTIONDISPLAYOBJECTS",
    "PROVIDERDDO_QUERYCONSTRAINT_DEVICEINTERFACES",
    "PROVIDERDDO_QUERYCONSTRAINT_ONLYCONNECTEDDEVICES",
    "PROVIDERPNP_QUERYCONSTRAINT_INTERFACECLASS",
    "PROVIDERPNP_QUERYCONSTRAINT_NOTIFICATIONSONLY",
    "PROVIDERPNP_QUERYCONSTRAINT_NOTPRESENT",
    "PROVIDERSSDP_QUERYCONSTRAINT_CUSTOMXMLPROPERTY",
    "PROVIDERSSDP_QUERYCONSTRAINT_TYPE",
    "PROVIDERWNET_QUERYCONSTRAINT_PROPERTIES",
    "PROVIDERWNET_QUERYCONSTRAINT_RESOURCETYPE",
    "PROVIDERWNET_QUERYCONSTRAINT_TYPE",
    "PROVIDERWSD_QUERYCONSTRAINT_DIRECTEDADDRESS",
    "PROVIDERWSD_QUERYCONSTRAINT_SCOPE",
    "PROVIDERWSD_QUERYCONSTRAINT_SECURITY_REQUIREMENTS",
    "PROVIDERWSD_QUERYCONSTRAINT_SSL_CERTHASH_FOR_SERVER_AUTH",
    "PROVIDERWSD_QUERYCONSTRAINT_SSL_CERT_FOR_CLIENT_AUTH",
    "PROVIDERWSD_QUERYCONSTRAINT_TYPE",
    "PropertyConstraint",
    "PropertyStore",
    "PropertyStoreCollection",
    "QCT_LAYERED",
    "QCT_PROVIDER",
    "QC_CONTAINS",
    "QC_DOESNOTEXIST",
    "QC_EQUALS",
    "QC_EXISTS",
    "QC_GREATERTHAN",
    "QC_GREATERTHANOREQUAL",
    "QC_LESSTHAN",
    "QC_LESSTHANOREQUAL",
    "QC_NOTEQUAL",
    "QC_STARTSWITH",
    "QUA_ADD",
    "QUA_CHANGE",
    "QUA_REMOVE",
    "QueryCategoryType",
    "QueryUpdateAction",
    "SID_DeviceDisplayStatusManager",
    "SID_EnumDeviceFunction",
    "SID_EnumInterface",
    "SID_FDPairingHandler",
    "SID_FunctionDiscoveryProviderRefresh",
    "SID_PNPXAssociation",
    "SID_PNPXPropertyStore",
    "SID_PNPXServiceCollection",
    "SID_PnpProvider",
    "SID_UPnPActivator",
    "SID_UninstallDeviceFunction",
    "SID_UnpairProvider",
    "SSDP_CONSTRAINTVALUE_TYPE_ALL",
    "SSDP_CONSTRAINTVALUE_TYPE_DEVICE_PREFIX",
    "SSDP_CONSTRAINTVALUE_TYPE_ROOT",
    "SSDP_CONSTRAINTVALUE_TYPE_SVC_PREFIX",
    "SVF_SYSTEM",
    "SVF_USER",
    "SystemVisibilityFlags",
    "WNET_CONSTRAINTVALUE_PROPERTIES_ALL",
    "WNET_CONSTRAINTVALUE_PROPERTIES_LIMITED",
    "WNET_CONSTRAINTVALUE_RESOURCETYPE_DISK",
    "WNET_CONSTRAINTVALUE_RESOURCETYPE_DISKORPRINTER",
    "WNET_CONSTRAINTVALUE_RESOURCETYPE_PRINTER",
    "WNET_CONSTRAINTVALUE_TYPE_ALL",
    "WNET_CONSTRAINTVALUE_TYPE_DOMAIN",
    "WNET_CONSTRAINTVALUE_TYPE_SERVER",
    "WSD_CONSTRAINTVALUE_NO_TRUST_VERIFICATION",
    "WSD_CONSTRAINTVALUE_REQUIRE_SECURECHANNEL",
    "WSD_CONSTRAINTVALUE_REQUIRE_SECURECHANNEL_AND_COMPACTSIGNATURE",
]
