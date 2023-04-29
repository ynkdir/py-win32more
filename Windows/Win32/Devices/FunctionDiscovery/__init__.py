from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Devices.FunctionDiscovery
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
FD_EVENTID_PRIVATE: UInt32 = 100
FD_EVENTID: UInt32 = 1000
FD_EVENTID_SEARCHCOMPLETE: UInt32 = 1000
FD_EVENTID_ASYNCTHREADEXIT: UInt32 = 1001
FD_EVENTID_SEARCHSTART: UInt32 = 1002
FD_EVENTID_IPADDRESSCHANGE: UInt32 = 1003
FD_EVENTID_QUERYREFRESH: UInt32 = 1004
SID_PnpProvider: Guid = Guid('8101368e-cabb-4426-ac-ff-96-c4-10-81-20-00')
SID_UPnPActivator: Guid = Guid('0d0d66eb-cf74-4164-b5-2f-08-34-46-72-dd-46')
SID_EnumInterface: Guid = Guid('40eab0b9-4d7f-4b53-a3-34-15-81-dd-90-41-f4')
SID_PNPXPropertyStore: Guid = Guid('a86530b1-542f-439f-b7-1c-b0-75-6b-13-67-7a')
SID_PNPXAssociation: Guid = Guid('cee8ccc9-4f6b-4469-a2-35-5a-22-86-9e-ef-03')
SID_PNPXServiceCollection: Guid = Guid('439e80ee-a217-4712-9f-a6-de-ab-d9-c2-a7-27')
SID_FDPairingHandler: Guid = Guid('383b69fa-5486-49da-91-f5-d6-3c-24-c8-e9-d0')
SID_EnumDeviceFunction: Guid = Guid('13e0e9e2-c3fa-4e3c-90-6e-64-50-2f-a4-dc-95')
SID_UnpairProvider: Guid = Guid('89a502fc-857b-4698-a0-b7-02-71-92-00-2f-9e')
SID_DeviceDisplayStatusManager: Guid = Guid('f59aa553-8309-46ca-97-36-1a-c3-c6-2d-60-31')
SID_FunctionDiscoveryProviderRefresh: Guid = Guid('2b4cbdc9-31c4-40d4-a6-2d-77-2a-a1-74-ed-52')
SID_UninstallDeviceFunction: Guid = Guid('c920566e-5671-4496-80-25-bf-0b-89-bd-44-cd')
def PKEY_FunctionInstance():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('08c0c253-a154-4746-90-05-82-de-53-17-14-8b'), pid=1)
FMTID_FD: Guid = Guid('904b03a2-471d-423c-a5-84-f3-48-32-38-a1-46')
FD_Visibility_Default: UInt32 = 0
FD_Visibility_Hidden: UInt32 = 1
FMTID_Device: Guid = Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57')
FMTID_DeviceInterface: Guid = Guid('53808008-07bb-4661-bc-3c-b5-95-3e-70-85-60')
def PKEY_DeviceDisplay_Address():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=51)
def PKEY_DeviceDisplay_DiscoveryMethod():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=52)
def PKEY_DeviceDisplay_IsEncrypted():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=53)
def PKEY_DeviceDisplay_IsAuthenticated():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=54)
def PKEY_DeviceDisplay_IsConnected():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=55)
def PKEY_DeviceDisplay_IsPaired():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=56)
def PKEY_DeviceDisplay_Icon():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=57)
def PKEY_DeviceDisplay_Version():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=65)
def PKEY_DeviceDisplay_Last_Seen():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=66)
def PKEY_DeviceDisplay_Last_Connected():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=67)
def PKEY_DeviceDisplay_IsShowInDisconnectedState():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=68)
def PKEY_DeviceDisplay_IsLocalMachine():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=70)
def PKEY_DeviceDisplay_MetadataPath():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=71)
def PKEY_DeviceDisplay_IsMetadataSearchInProgress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=72)
def PKEY_DeviceDisplay_MetadataChecksum():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=73)
def PKEY_DeviceDisplay_IsNotInterestingForDisplay():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=74)
def PKEY_DeviceDisplay_LaunchDeviceStageOnDeviceConnect():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=76)
def PKEY_DeviceDisplay_LaunchDeviceStageFromExplorer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=77)
def PKEY_DeviceDisplay_BaselineExperienceId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=78)
def PKEY_DeviceDisplay_IsDeviceUniquelyIdentifiable():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=79)
def PKEY_DeviceDisplay_AssociationArray():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=80)
def PKEY_DeviceDisplay_DeviceDescription1():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=81)
def PKEY_DeviceDisplay_DeviceDescription2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=82)
def PKEY_DeviceDisplay_IsNotWorkingProperly():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=83)
def PKEY_DeviceDisplay_IsSharedDevice():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=84)
def PKEY_DeviceDisplay_IsNetworkDevice():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=85)
def PKEY_DeviceDisplay_IsDefaultDevice():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=86)
def PKEY_DeviceDisplay_MetadataCabinet():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=87)
def PKEY_DeviceDisplay_RequiresPairingElevation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=88)
def PKEY_DeviceDisplay_ExperienceId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=89)
def PKEY_DeviceDisplay_Category():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=90)
def PKEY_DeviceDisplay_Category_Desc_Singular():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=91)
def PKEY_DeviceDisplay_Category_Desc_Plural():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=92)
def PKEY_DeviceDisplay_Category_Icon():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=93)
def PKEY_DeviceDisplay_CategoryGroup_Desc():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=94)
def PKEY_DeviceDisplay_CategoryGroup_Icon():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=95)
def PKEY_DeviceDisplay_PrimaryCategory():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=97)
def PKEY_DeviceDisplay_UnpairUninstall():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=98)
def PKEY_DeviceDisplay_RequiresUninstallElevation():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=99)
def PKEY_DeviceDisplay_DeviceFunctionSubRank():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=100)
def PKEY_DeviceDisplay_AlwaysShowDeviceAsConnected():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=101)
def PKEY_DeviceDisplay_FriendlyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12288)
def PKEY_DeviceDisplay_Manufacturer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8192)
def PKEY_DeviceDisplay_ModelName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8194)
def PKEY_DeviceDisplay_ModelNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8195)
def PKEY_DeviceDisplay_InstallInProgress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=9)
FMTID_Pairing: Guid = Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc')
def PKEY_Pairing_ListItemText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc'), pid=1)
def PKEY_Pairing_ListItemDescription():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc'), pid=2)
def PKEY_Pairing_ListItemIcon():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc'), pid=3)
def PKEY_Pairing_ListItemDefault():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc'), pid=4)
def PKEY_Pairing_IsWifiOnlyDevice():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8807cae6-7db6-4f10-8e-e4-43-5e-aa-13-92-bc'), pid=16)
DEVICEDISPLAY_DISCOVERYMETHOD_BLUETOOTH: String = 'Bluetooth'
DEVICEDISPLAY_DISCOVERYMETHOD_BLUETOOTH_LE: String = 'Bluetooth Low Energy'
DEVICEDISPLAY_DISCOVERYMETHOD_NETBIOS: String = 'NetBIOS'
DEVICEDISPLAY_DISCOVERYMETHOD_AD_PRINTER: String = 'Published Printer'
DEVICEDISPLAY_DISCOVERYMETHOD_PNP: String = 'PnP'
DEVICEDISPLAY_DISCOVERYMETHOD_UPNP: String = 'UPnP'
DEVICEDISPLAY_DISCOVERYMETHOD_WSD: String = 'WSD'
DEVICEDISPLAY_DISCOVERYMETHOD_WUSB: String = 'WUSB'
DEVICEDISPLAY_DISCOVERYMETHOD_WFD: String = 'WiFiDirect'
DEVICEDISPLAY_DISCOVERYMETHOD_ASP_INFRA: String = 'AspInfra'
def PKEY_Device_BIOSVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('eaee7f1d-6a33-44d1-94-41-5f-46-de-f2-31-98'), pid=9)
FMTID_WSD: Guid = Guid('92506491-ff95-4724-a0-5a-5b-81-88-5a-7c-92')
FMTID_PNPX: Guid = Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd')
def PKEY_PNPX_GlobalIdentity():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4096)
def PKEY_PNPX_Types():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4097)
def PKEY_PNPX_Scopes():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4098)
def PKEY_PNPX_XAddrs():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4099)
def PKEY_PNPX_MetadataVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4100)
def PKEY_PNPX_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4101)
def PKEY_PNPX_RemoteAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4102)
def PKEY_PNPX_RootProxy():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=4103)
def PKEY_PNPX_ManufacturerUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8193)
def PKEY_PNPX_ModelUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8196)
def PKEY_PNPX_Upc():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8197)
def PKEY_PNPX_PresentationUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8198)
def PKEY_PNPX_FirmwareVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12289)
def PKEY_PNPX_SerialNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12290)
def PKEY_PNPX_DeviceCategory():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12292)
def PKEY_PNPX_SecureChannel():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=28673)
def PKEY_PNPX_CompactSignature():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=28674)
def PKEY_PNPX_DeviceCertHash():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=28675)
PNPX_DEVICECATEGORY_COMPUTER: String = 'Computers'
PNPX_DEVICECATEGORY_INPUTDEVICE: String = 'Input'
PNPX_DEVICECATEGORY_PRINTER: String = 'Printers'
PNPX_DEVICECATEGORY_SCANNER: String = 'Scanners'
PNPX_DEVICECATEGORY_FAX: String = 'FAX'
PNPX_DEVICECATEGORY_MFP: String = 'MFP'
PNPX_DEVICECATEGORY_CAMERA: String = 'Cameras'
PNPX_DEVICECATEGORY_STORAGE: String = 'Storage'
PNPX_DEVICECATEGORY_NETWORK_INFRASTRUCTURE: String = 'NetworkInfrastructure'
PNPX_DEVICECATEGORY_DISPLAYS: String = 'Displays'
PNPX_DEVICECATEGORY_MULTIMEDIA_DEVICE: String = 'MediaDevices'
PNPX_DEVICECATEGORY_GAMING_DEVICE: String = 'Gaming'
PNPX_DEVICECATEGORY_TELEPHONE: String = 'Phones'
PNPX_DEVICECATEGORY_HOME_AUTOMATION_SYSTEM: String = 'HomeAutomation'
PNPX_DEVICECATEGORY_HOME_SECURITY_SYSTEM: String = 'HomeSecurity'
PNPX_DEVICECATEGORY_OTHER: String = 'Other'
def PKEY_PNPX_DeviceCategory_Desc():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12293)
def PKEY_PNPX_Category_Desc_NonPlural():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12304)
def PKEY_PNPX_PhysicalAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12294)
def PKEY_PNPX_NetworkInterfaceLuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12295)
def PKEY_PNPX_NetworkInterfaceGuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12296)
def PKEY_PNPX_IpAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12297)
def PKEY_PNPX_ServiceAddress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16384)
def PKEY_PNPX_ServiceId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16385)
def PKEY_PNPX_ServiceTypes():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16386)
def PKEY_PNPX_ServiceControlUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16388)
def PKEY_PNPX_ServiceDescUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16389)
def PKEY_PNPX_ServiceEventSubUrl():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=16390)
def PKEY_PNPX_DomainName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=20480)
def PKEY_PNPX_ShareName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=20482)
def PKEY_SSDP_AltLocationInfo():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=24576)
def PKEY_SSDP_DevLifeTime():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=24577)
def PKEY_SSDP_NetworkInterface():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=24578)
FMTID_PNPXDynamicProperty: Guid = Guid('4fc5077e-b686-44be-93-e3-86-ca-fe-36-8c-cd')
def PKEY_PNPX_Installable():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4fc5077e-b686-44be-93-e3-86-ca-fe-36-8c-cd'), pid=1)
def PKEY_PNPX_Associated():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4fc5077e-b686-44be-93-e3-86-ca-fe-36-8c-cd'), pid=2)
def PKEY_PNPX_CompatibleTypes():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4fc5077e-b686-44be-93-e3-86-ca-fe-36-8c-cd'), pid=3)
def PKEY_PNPX_InstallState():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4fc5077e-b686-44be-93-e3-86-ca-fe-36-8c-cd'), pid=4)
PNPX_INSTALLSTATE_NOTINSTALLED: UInt32 = 0
PNPX_INSTALLSTATE_INSTALLED: UInt32 = 1
PNPX_INSTALLSTATE_INSTALLING: UInt32 = 2
PNPX_INSTALLSTATE_FAILED: UInt32 = 3
def PKEY_PNPX_Removable():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=28672)
def PKEY_PNPX_IPBusEnumerated():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=28688)
def PKEY_WNET_Scope():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=1)
def PKEY_WNET_Type():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=2)
def PKEY_WNET_DisplayType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=3)
def PKEY_WNET_Usage():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=4)
def PKEY_WNET_LocalName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=5)
def PKEY_WNET_RemoteName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=6)
def PKEY_WNET_Comment():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=7)
def PKEY_WNET_Provider():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('debda43a-37b3-4383-91-e7-44-98-da-29-95-ab'), pid=8)
def PKEY_WCN_Version():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b80-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=1)
def PKEY_WCN_RequestType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b81-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=2)
def PKEY_WCN_AuthType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b82-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=3)
def PKEY_WCN_EncryptType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b83-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=4)
def PKEY_WCN_ConnType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b84-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=5)
def PKEY_WCN_ConfigMethods():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b85-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=6)
def PKEY_WCN_RfBand():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b87-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=8)
def PKEY_WCN_AssocState():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b88-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=9)
def PKEY_WCN_ConfigError():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b89-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=10)
def PKEY_WCN_ConfigState():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b89-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=11)
def PKEY_WCN_DevicePasswordId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b89-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=12)
def PKEY_WCN_OSVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b89-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=13)
def PKEY_WCN_VendorExtension():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b8a-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=14)
def PKEY_WCN_RegistrarType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b8b-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=15)
def PKEY_Hardware_Devinst():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=4097)
def PKEY_Hardware_DisplayAttribute():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=5)
def PKEY_Hardware_DriverDate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=11)
def PKEY_Hardware_DriverProvider():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=10)
def PKEY_Hardware_DriverVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=9)
def PKEY_Hardware_Function():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=4099)
def PKEY_Hardware_Icon():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=3)
def PKEY_Hardware_Image():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=4098)
def PKEY_Hardware_Manufacturer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=6)
def PKEY_Hardware_Model():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=7)
def PKEY_Hardware_Name():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=2)
def PKEY_Hardware_SerialNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=8)
def PKEY_Hardware_ShellAttributes():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=4100)
def PKEY_Hardware_Status():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('5eaf3ef2-e0ca-4598-bf-06-71-ed-1d-9d-d9-53'), pid=4096)
def PKEY_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=10)
def PKEY_Device_DeviceDesc():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=2)
def PKEY_Device_HardwareIds():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=3)
def PKEY_Device_CompatibleIds():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=4)
def PKEY_Device_Service():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=6)
def PKEY_Device_Class():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=9)
def PKEY_Device_ClassGuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=10)
def PKEY_Device_Driver():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=11)
def PKEY_Device_ConfigFlags():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=12)
def PKEY_Device_Manufacturer():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=13)
def PKEY_Device_FriendlyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=14)
def PKEY_Device_LocationInfo():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=15)
def PKEY_Device_PDOName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=16)
def PKEY_Device_Capabilities():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=17)
def PKEY_Device_UINumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=18)
def PKEY_Device_UpperFilters():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=19)
def PKEY_Device_LowerFilters():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=20)
def PKEY_Device_BusTypeGuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=21)
def PKEY_Device_LegacyBusType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=22)
def PKEY_Device_BusNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=23)
def PKEY_Device_EnumeratorName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=24)
def PKEY_Device_Security():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=25)
def PKEY_Device_SecuritySDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=26)
def PKEY_Device_DevType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=27)
def PKEY_Device_Exclusive():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=28)
def PKEY_Device_Characteristics():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=29)
def PKEY_Device_Address():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=30)
def PKEY_Device_UINumberDescFormat():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=31)
def PKEY_Device_PowerData():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=32)
def PKEY_Device_RemovalPolicy():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=33)
def PKEY_Device_RemovalPolicyDefault():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=34)
def PKEY_Device_RemovalPolicyOverride():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=35)
def PKEY_Device_InstallState():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=36)
def PKEY_Device_LocationPaths():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=37)
def PKEY_Device_BaseContainerId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=38)
def PKEY_Device_DevNodeStatus():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=2)
def PKEY_Device_ProblemCode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=3)
def PKEY_Device_EjectionRelations():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=4)
def PKEY_Device_RemovalRelations():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=5)
def PKEY_Device_PowerRelations():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=6)
def PKEY_Device_BusRelations():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=7)
def PKEY_Device_Parent():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=8)
def PKEY_Device_Children():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=9)
def PKEY_Device_Siblings():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=10)
def PKEY_Device_TransportRelations():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=11)
def PKEY_Device_Reported():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80497100-8c73-48b9-aa-d9-ce-38-7e-19-c5-6e'), pid=2)
def PKEY_Device_Legacy():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80497100-8c73-48b9-aa-d9-ce-38-7e-19-c5-6e'), pid=3)
def PKEY_Device_InstanceId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=256)
def PKEY_Device_ContainerId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8c7ed206-3f8a-4827-b3-ab-ae-9e-1f-ae-fc-6c'), pid=2)
def PKEY_Device_ModelId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=2)
def PKEY_Device_FriendlyNameAttributes():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=3)
def PKEY_Device_ManufacturerAttributes():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=4)
def PKEY_Device_PresenceNotForDevice():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=5)
def PKEY_Device_SignalStrength():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=6)
def PKEY_Device_IsAssociateableByUserAction():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=7)
def PKEY_Numa_Proximity_Domain():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=1)
def PKEY_Device_DHP_Rebalance_Policy():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=2)
def PKEY_Device_Numa_Node():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=3)
def PKEY_Device_BusReportedDeviceDesc():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=4)
def PKEY_Device_InstallInProgress():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=9)
def PKEY_Device_DriverDate():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=2)
def PKEY_Device_DriverVersion():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=3)
def PKEY_Device_DriverDesc():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=4)
def PKEY_Device_DriverInfPath():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=5)
def PKEY_Device_DriverInfSection():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=6)
def PKEY_Device_DriverInfSectionExt():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=7)
def PKEY_Device_MatchingDeviceId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=8)
def PKEY_Device_DriverProvider():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=9)
def PKEY_Device_DriverPropPageProvider():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=10)
def PKEY_Device_DriverCoInstallers():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=11)
def PKEY_Device_ResourcePickerTags():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=12)
def PKEY_Device_ResourcePickerExceptions():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=13)
def PKEY_Device_DriverRank():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=14)
def PKEY_Device_DriverLogoLevel():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=15)
def PKEY_Device_NoConnectSound():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=17)
def PKEY_Device_GenericDriverInstalled():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=18)
def PKEY_Device_AdditionalSoftwareRequested():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=19)
def PKEY_Device_SafeRemovalRequired():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afd97640-86a3-4210-b6-7c-28-9c-41-aa-be-55'), pid=2)
def PKEY_Device_SafeRemovalRequiredOverride():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('afd97640-86a3-4210-b6-7c-28-9c-41-aa-be-55'), pid=3)
def PKEY_DrvPkg_Model():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=2)
def PKEY_DrvPkg_VendorWebSite():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=3)
def PKEY_DrvPkg_DetailedDescription():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=4)
def PKEY_DrvPkg_DocumentationLink():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=5)
def PKEY_DrvPkg_Icon():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=6)
def PKEY_DrvPkg_BrandingIcon():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=7)
def PKEY_DeviceClass_UpperFilters():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=19)
def PKEY_DeviceClass_LowerFilters():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=20)
def PKEY_DeviceClass_Security():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=25)
def PKEY_DeviceClass_SecuritySDS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=26)
def PKEY_DeviceClass_DevType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=27)
def PKEY_DeviceClass_Exclusive():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=28)
def PKEY_DeviceClass_Characteristics():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=29)
def PKEY_DeviceClass_Name():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=2)
def PKEY_DeviceClass_ClassName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=3)
def PKEY_DeviceClass_Icon():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=4)
def PKEY_DeviceClass_ClassInstaller():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=5)
def PKEY_DeviceClass_PropPageProvider():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=6)
def PKEY_DeviceClass_NoInstallClass():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=7)
def PKEY_DeviceClass_NoDisplayClass():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=8)
def PKEY_DeviceClass_SilentInstall():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=9)
def PKEY_DeviceClass_NoUseClass():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=10)
def PKEY_DeviceClass_DefaultService():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=11)
def PKEY_DeviceClass_IconPath():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=12)
def PKEY_DeviceClass_ClassCoInstallers():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('713d1703-a2e2-49f5-92-14-56-47-2e-f3-da-5c'), pid=2)
def PKEY_DeviceInterface_FriendlyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=2)
def PKEY_DeviceInterface_Enabled():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=3)
def PKEY_DeviceInterface_ClassGuid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=4)
def PKEY_DeviceInterfaceClass_DefaultInterface():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14c83a99-0b3f-44b7-be-4c-a1-78-d3-99-05-64'), pid=2)
FD_LONGHORN: UInt32 = 1
FD_SUBKEY: String = 'SOFTWARE\\Microsoft\\Function Discovery\\'
FCTN_CATEGORY_PNP: String = 'Provider\\Microsoft.Base.PnP'
FCTN_CATEGORY_REGISTRY: String = 'Provider\\Microsoft.Base.Registry'
FCTN_CATEGORY_SSDP: String = 'Provider\\Microsoft.Networking.SSDP'
FCTN_CATEGORY_WSDISCOVERY: String = 'Provider\\Microsoft.Networking.WSD'
FCTN_CATEGORY_NETBIOS: String = 'Provider\\Microsoft.Networking.Netbios'
FCTN_CATEGORY_WCN: String = 'Provider\\Microsoft.Networking.WCN'
FCTN_CATEGORY_PUBLICATION: String = 'Provider\\Microsoft.Base.Publication'
FCTN_CATEGORY_PNPXASSOCIATION: String = 'Provider\\Microsoft.PnPX.Association'
FCTN_CATEGORY_BT: String = 'Provider\\Microsoft.Devices.Bluetooth'
FCTN_CATEGORY_WUSB: String = 'Provider\\Microsoft.Devices.WirelessUSB'
FCTN_CATEGORY_DEVICEDISPLAYOBJECTS: String = 'Provider\\Microsoft.Base.DeviceDisplayObjects'
FCTN_CATEGORY_DEVQUERYOBJECTS: String = 'Provider\\Microsoft.Base.DevQueryObjects'
FCTN_CATEGORY_NETWORKDEVICES: String = 'Layered\\Microsoft.Networking.Devices'
FCTN_CATEGORY_DEVICES: String = 'Layered\\Microsoft.Base.Devices'
FCTN_CATEGORY_DEVICEFUNCTIONENUMERATORS: String = 'Layered\\Microsoft.Devices.FunctionEnumerators'
FCTN_CATEGORY_DEVICEPAIRING: String = 'Layered\\Microsoft.Base.DevicePairing'
FCTN_SUBCAT_DEVICES_WSDPRINTERS: String = 'WSDPrinters'
FCTN_SUBCAT_NETWORKDEVICES_SSDP: String = 'SSDP'
FCTN_SUBCAT_NETWORKDEVICES_WSD: String = 'WSD'
FCTN_SUBCAT_REG_PUBLICATION: String = 'Publication'
FCTN_SUBCAT_REG_DIRECTED: String = 'Directed'
MAX_FDCONSTRAINTNAME_LENGTH: UInt32 = 100
MAX_FDCONSTRAINTVALUE_LENGTH: UInt32 = 1000
FD_QUERYCONSTRAINT_PROVIDERINSTANCEID: String = 'ProviderInstanceID'
FD_QUERYCONSTRAINT_SUBCATEGORY: String = 'Subcategory'
FD_QUERYCONSTRAINT_RECURSESUBCATEGORY: String = 'RecurseSubcategory'
FD_QUERYCONSTRAINT_VISIBILITY: String = 'Visibility'
FD_QUERYCONSTRAINT_COMCLSCONTEXT: String = 'COMClsContext'
FD_QUERYCONSTRAINT_ROUTINGSCOPE: String = 'RoutingScope'
FD_CONSTRAINTVALUE_TRUE: String = 'TRUE'
FD_CONSTRAINTVALUE_FALSE: String = 'FALSE'
FD_CONSTRAINTVALUE_RECURSESUBCATEGORY_TRUE: String = 'TRUE'
FD_CONSTRAINTVALUE_VISIBILITY_DEFAULT: String = '0'
FD_CONSTRAINTVALUE_VISIBILITY_ALL: String = '1'
FD_CONSTRAINTVALUE_COMCLSCONTEXT_INPROC_SERVER: String = '1'
FD_CONSTRAINTVALUE_COMCLSCONTEXT_LOCAL_SERVER: String = '4'
FD_CONSTRAINTVALUE_PAIRED: String = 'Paired'
FD_CONSTRAINTVALUE_UNPAIRED: String = 'UnPaired'
FD_CONSTRAINTVALUE_ALL: String = 'All'
FD_CONSTRAINTVALUE_ROUTINGSCOPE_ALL: String = 'All'
FD_CONSTRAINTVALUE_ROUTINGSCOPE_DIRECT: String = 'Direct'
FD_QUERYCONSTRAINT_PAIRING_STATE: String = 'PairingState'
FD_QUERYCONSTRAINT_INQUIRY_TIMEOUT: String = 'InquiryModeTimeout'
PROVIDERPNP_QUERYCONSTRAINT_INTERFACECLASS: String = 'InterfaceClass'
PROVIDERPNP_QUERYCONSTRAINT_NOTPRESENT: String = 'NotPresent'
PROVIDERPNP_QUERYCONSTRAINT_NOTIFICATIONSONLY: String = 'NotifyOnly'
PNP_CONSTRAINTVALUE_NOTPRESENT: String = 'TRUE'
PNP_CONSTRAINTVALUE_NOTIFICATIONSONLY: String = 'TRUE'
PROVIDERSSDP_QUERYCONSTRAINT_TYPE: String = 'Type'
PROVIDERSSDP_QUERYCONSTRAINT_CUSTOMXMLPROPERTY: String = 'CustomXmlProperty'
SSDP_CONSTRAINTVALUE_TYPE_ALL: String = 'ssdp:all'
SSDP_CONSTRAINTVALUE_TYPE_ROOT: String = 'upnp:rootdevice'
SSDP_CONSTRAINTVALUE_TYPE_DEVICE_PREFIX: String = 'urn:schemas-upnp-org:device:'
SSDP_CONSTRAINTVALUE_TYPE_SVC_PREFIX: String = 'urn:schemas-upnp-org:service:'
PROVIDERWSD_QUERYCONSTRAINT_DIRECTEDADDRESS: String = 'RemoteAddress'
PROVIDERWSD_QUERYCONSTRAINT_TYPE: String = 'Type'
PROVIDERWSD_QUERYCONSTRAINT_SCOPE: String = 'Scope'
PROVIDERWSD_QUERYCONSTRAINT_SECURITY_REQUIREMENTS: String = 'SecurityRequirements'
PROVIDERWSD_QUERYCONSTRAINT_SSL_CERT_FOR_CLIENT_AUTH: String = 'SSLClientAuthCert'
PROVIDERWSD_QUERYCONSTRAINT_SSL_CERTHASH_FOR_SERVER_AUTH: String = 'SSLServerAuthCertHash'
WSD_CONSTRAINTVALUE_REQUIRE_SECURECHANNEL: String = '1'
WSD_CONSTRAINTVALUE_REQUIRE_SECURECHANNEL_AND_COMPACTSIGNATURE: String = '2'
WSD_CONSTRAINTVALUE_NO_TRUST_VERIFICATION: String = '3'
PROVIDERWNET_QUERYCONSTRAINT_TYPE: String = 'Type'
PROVIDERWNET_QUERYCONSTRAINT_PROPERTIES: String = 'Properties'
PROVIDERWNET_QUERYCONSTRAINT_RESOURCETYPE: String = 'ResourceType'
WNET_CONSTRAINTVALUE_TYPE_ALL: String = 'All'
WNET_CONSTRAINTVALUE_TYPE_SERVER: String = 'Server'
WNET_CONSTRAINTVALUE_TYPE_DOMAIN: String = 'Domain'
WNET_CONSTRAINTVALUE_PROPERTIES_ALL: String = 'All'
WNET_CONSTRAINTVALUE_PROPERTIES_LIMITED: String = 'Limited'
WNET_CONSTRAINTVALUE_RESOURCETYPE_DISK: String = 'Disk'
WNET_CONSTRAINTVALUE_RESOURCETYPE_PRINTER: String = 'Printer'
WNET_CONSTRAINTVALUE_RESOURCETYPE_DISKORPRINTER: String = 'DiskOrPrinter'
ONLINE_PROVIDER_DEVICES_QUERYCONSTRAINT_OWNERNAME: String = 'OwnerName'
PROVIDERDDO_QUERYCONSTRAINT_DEVICEFUNCTIONDISPLAYOBJECTS: String = 'DeviceFunctionDisplayObjects'
PROVIDERDDO_QUERYCONSTRAINT_ONLYCONNECTEDDEVICES: String = 'OnlyConnectedDevices'
PROVIDERDDO_QUERYCONSTRAINT_DEVICEINTERFACES: String = 'DeviceInterfaces'
E_FDPAIRING_NOCONNECTION: Windows.Win32.Foundation.HRESULT = -1882193919
E_FDPAIRING_HWFAILURE: Windows.Win32.Foundation.HRESULT = -1882193918
E_FDPAIRING_AUTHFAILURE: Windows.Win32.Foundation.HRESULT = -1882193917
E_FDPAIRING_CONNECTTIMEOUT: Windows.Win32.Foundation.HRESULT = -1882193916
E_FDPAIRING_TOOMANYCONNECTIONS: Windows.Win32.Foundation.HRESULT = -1882193915
E_FDPAIRING_AUTHNOTALLOWED: Windows.Win32.Foundation.HRESULT = -1882193914
E_FDPAIRING_IPBUSDISABLED: Windows.Win32.Foundation.HRESULT = -1882193913
E_FDPAIRING_NOPROFILES: Windows.Win32.Foundation.HRESULT = -1882193912
FunctionDiscovery = Guid('c72be2ec-8e90-452c-b2-9a-ab-8f-f1-c0-71-fc')
FunctionInstanceCollection = Guid('ba818ce5-b55f-443f-ad-39-2f-e8-9b-e6-19-1f')
class IFunctionDiscovery(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4df99b70-e148-4432-b0-04-4c-9e-eb-53-5a-5e')
    @commethod(3)
    def GetInstanceCollection(self, pszCategory: Windows.Win32.Foundation.PWSTR, pszSubCategory: Windows.Win32.Foundation.PWSTR, fIncludeAllSubCategories: Windows.Win32.Foundation.BOOL, ppIFunctionInstanceCollection: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInstance(self, pszFunctionInstanceIdentity: Windows.Win32.Foundation.PWSTR, ppIFunctionInstance: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateInstanceCollectionQuery(self, pszCategory: Windows.Win32.Foundation.PWSTR, pszSubCategory: Windows.Win32.Foundation.PWSTR, fIncludeAllSubCategories: Windows.Win32.Foundation.BOOL, pIFunctionDiscoveryNotification: Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head, pfdqcQueryContext: POINTER(UInt64), ppIFunctionInstanceCollectionQuery: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceCollectionQuery_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateInstanceQuery(self, pszFunctionInstanceIdentity: Windows.Win32.Foundation.PWSTR, pIFunctionDiscoveryNotification: Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head, pfdqcQueryContext: POINTER(UInt64), ppIFunctionInstanceQuery: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceQuery_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddInstance(self, enumSystemVisibility: Windows.Win32.Devices.FunctionDiscovery.SystemVisibilityFlags, pszCategory: Windows.Win32.Foundation.PWSTR, pszSubCategory: Windows.Win32.Foundation.PWSTR, pszCategoryIdentity: Windows.Win32.Foundation.PWSTR, ppIFunctionInstance: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveInstance(self, enumSystemVisibility: Windows.Win32.Devices.FunctionDiscovery.SystemVisibilityFlags, pszCategory: Windows.Win32.Foundation.PWSTR, pszSubCategory: Windows.Win32.Foundation.PWSTR, pszCategoryIdentity: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFunctionDiscoveryNotification(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5f6c1ba8-5330-422e-a3-68-57-2b-24-4d-3f-87')
    @commethod(3)
    def OnUpdate(self, enumQueryUpdateAction: Windows.Win32.Devices.FunctionDiscovery.QueryUpdateAction, fdqcQueryContext: UInt64, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnError(self, hr: Windows.Win32.Foundation.HRESULT, fdqcQueryContext: UInt64, pszProvider: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEvent(self, dwEventID: UInt32, fdqcQueryContext: UInt64, pszProvider: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFunctionDiscoveryProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcde394f-1478-4813-a4-02-f6-fb-10-65-72-22')
    @commethod(3)
    def Initialize(self, pIFunctionDiscoveryProviderFactory: Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryProviderFactory_head, pIFunctionDiscoveryNotification: Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head, lcidUserDefault: UInt32, pdwStgAccessCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Query(self, pIFunctionDiscoveryProviderQuery: Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryProviderQuery_head, ppIFunctionInstanceCollection: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndQuery(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InstancePropertyStoreValidateAccess(self, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head, iProviderInstanceContext: IntPtr, dwStgAccess: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InstancePropertyStoreOpen(self, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head, iProviderInstanceContext: IntPtr, dwStgAccess: UInt32, ppIPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InstancePropertyStoreFlush(self, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head, iProviderInstanceContext: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def InstanceQueryService(self, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head, iProviderInstanceContext: IntPtr, guidService: POINTER(Guid), riid: POINTER(Guid), ppIUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def InstanceReleased(self, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head, iProviderInstanceContext: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IFunctionDiscoveryProviderFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('86443ff0-1ad5-4e68-a4-5a-40-c2-c3-29-de-3b')
    @commethod(3)
    def CreatePropertyStore(self, ppIPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateInstance(self, pszSubCategory: Windows.Win32.Foundation.PWSTR, pszProviderInstanceIdentity: Windows.Win32.Foundation.PWSTR, iProviderInstanceContext: IntPtr, pIPropertyStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, pIFunctionDiscoveryProvider: Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryProvider_head, ppIFunctionInstance: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateFunctionInstanceCollection(self, ppIFunctionInstanceCollection: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFunctionDiscoveryProviderQuery(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6876ea98-baec-46db-bc-20-75-a7-6e-26-7a-3a')
    @commethod(3)
    def IsInstanceQuery(self, pisInstanceQuery: POINTER(Windows.Win32.Foundation.BOOL), ppszConstraintValue: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsSubcategoryQuery(self, pisSubcategoryQuery: POINTER(Windows.Win32.Foundation.BOOL), ppszConstraintValue: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetQueryConstraints(self, ppIProviderQueryConstraints: POINTER(Windows.Win32.Devices.FunctionDiscovery.IProviderQueryConstraintCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyConstraints(self, ppIProviderPropertyConstraints: POINTER(Windows.Win32.Devices.FunctionDiscovery.IProviderPropertyConstraintCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFunctionDiscoveryServiceProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4c81ed02-1b04-43f2-a4-51-69-96-6c-bc-d1-c2')
    @commethod(3)
    def Initialize(self, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IFunctionInstance(ComPtr):
    extends: Windows.Win32.System.Com.IServiceProvider
    Guid = Guid('33591c10-0bed-4f02-b0-ab-15-30-d5-53-3e-e9')
    @commethod(4)
    def GetID(self, ppszCoMemIdentity: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProviderInstanceID(self, ppszCoMemProviderInstanceIdentity: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OpenPropertyStore(self, dwStgAccess: Windows.Win32.System.Com.STGM, ppIPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCategory(self, ppszCoMemCategory: POINTER(POINTER(UInt16)), ppszCoMemSubCategory: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
class IFunctionInstanceCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f0a3d895-855c-42a2-94-8d-2f-97-d4-50-ec-b1')
    @commethod(3)
    def GetCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Get(self, pszInstanceIdentity: Windows.Win32.Foundation.PWSTR, pdwIndex: POINTER(UInt32), ppIFunctionInstance: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, dwIndex: UInt32, ppIFunctionInstance: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Add(self, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Remove(self, dwIndex: UInt32, ppIFunctionInstance: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Delete(self, dwIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteAll(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFunctionInstanceCollectionQuery(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('57cc6fd2-c09a-4289-bb-72-25-f0-41-42-05-8e')
    @commethod(3)
    def AddQueryConstraint(self, pszConstraintName: Windows.Win32.Foundation.PWSTR, pszConstraintValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPropertyConstraint(self, Key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pv: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), enumPropertyConstraint: Windows.Win32.Devices.FunctionDiscovery.PropertyConstraint) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Execute(self, ppIFunctionInstanceCollection: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFunctionInstanceQuery(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6242bc6b-90ec-4b37-bb-46-e2-29-fd-84-ed-95')
    @commethod(3)
    def Execute(self, ppIFunctionInstance: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPNPXAssociation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0bd7e521-4da6-42d5-81-ba-19-81-b6-b9-40-75')
    @commethod(3)
    def Associate(self, pszSubcategory: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unassociate(self, pszSubcategory: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(self, pszSubcategory: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IPNPXDeviceAssociation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('eed366d0-35b8-4fc5-8d-20-7e-5b-d3-1f-6d-ed')
    @commethod(3)
    def Associate(self, pszSubCategory: Windows.Win32.Foundation.PWSTR, pIFunctionDiscoveryNotification: Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unassociate(self, pszSubCategory: Windows.Win32.Foundation.PWSTR, pIFunctionDiscoveryNotification: Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(self, pszSubcategory: Windows.Win32.Foundation.PWSTR, pIFunctionDiscoveryNotification: Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyStoreCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d14d9c30-12d2-42d8-bc-e4-c6-0c-2b-b2-26-fa')
    @commethod(3)
    def GetCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Get(self, pszInstanceIdentity: Windows.Win32.Foundation.PWSTR, pdwIndex: POINTER(UInt32), ppIPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, dwIndex: UInt32, ppIPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Add(self, pIPropertyStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Remove(self, dwIndex: UInt32, pIPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Delete(self, dwIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteAll(self) -> Windows.Win32.Foundation.HRESULT: ...
class IProviderProperties(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cf986ea6-3b5f-4c5f-b8-8a-2f-8b-20-ce-ef-17')
    @commethod(3)
    def GetCount(self, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head, iProviderInstanceContext: IntPtr, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head, iProviderInstanceContext: IntPtr, dwIndex: UInt32, pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetValue(self, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head, iProviderInstanceContext: IntPtr, Key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropVar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetValue(self, pIFunctionInstance: Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head, iProviderInstanceContext: IntPtr, Key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropVar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IProviderPropertyConstraintCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f4fae42f-5778-4a13-85-40-b5-fd-8c-13-98-dd')
    @commethod(3)
    def GetCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Get(self, Key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pPropVar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pdwPropertyConstraint: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, dwIndex: UInt32, pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pPropVar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pdwPropertyConstraint: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Next(self, pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pPropVar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pdwPropertyConstraint: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Skip(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
class IProviderPublishing(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cd1b9a04-206c-4a05-a0-c8-16-35-a2-1a-2b-7c')
    @commethod(3)
    def CreateInstance(self, enumVisibilityFlags: Windows.Win32.Devices.FunctionDiscovery.SystemVisibilityFlags, pszSubCategory: Windows.Win32.Foundation.PWSTR, pszProviderInstanceIdentity: Windows.Win32.Foundation.PWSTR, ppIFunctionInstance: POINTER(Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveInstance(self, enumVisibilityFlags: Windows.Win32.Devices.FunctionDiscovery.SystemVisibilityFlags, pszSubCategory: Windows.Win32.Foundation.PWSTR, pszProviderInstanceIdentity: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IProviderQueryConstraintCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9c243e11-3261-4bcd-b9-22-84-a8-73-d4-60-ae')
    @commethod(3)
    def GetCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Get(self, pszConstraintName: Windows.Win32.Foundation.PWSTR, ppszConstraintValue: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, dwIndex: UInt32, ppszConstraintName: POINTER(POINTER(UInt16)), ppszConstraintValue: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Next(self, ppszConstraintName: POINTER(POINTER(UInt16)), ppszConstraintValue: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Skip(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
PNPXAssociation = Guid('cee8ccc9-4f6b-4469-a2-35-5a-22-86-9e-ef-03')
PNPXPairingHandler = Guid('b8a27942-ade7-4085-aa-6e-4f-ad-c7-ad-a1-ef')
PropertyConstraint = Int32
QC_EQUALS: PropertyConstraint = 0
QC_NOTEQUAL: PropertyConstraint = 1
QC_LESSTHAN: PropertyConstraint = 2
QC_LESSTHANOREQUAL: PropertyConstraint = 3
QC_GREATERTHAN: PropertyConstraint = 4
QC_GREATERTHANOREQUAL: PropertyConstraint = 5
QC_STARTSWITH: PropertyConstraint = 6
QC_EXISTS: PropertyConstraint = 7
QC_DOESNOTEXIST: PropertyConstraint = 8
QC_CONTAINS: PropertyConstraint = 9
PropertyStore = Guid('e4796550-df61-448b-91-93-13-fc-13-41-b1-63')
PropertyStoreCollection = Guid('edd36029-d753-4862-aa-5b-5b-cc-ad-2a-4d-29')
QueryCategoryType = Int32
QCT_PROVIDER: QueryCategoryType = 0
QCT_LAYERED: QueryCategoryType = 1
QueryUpdateAction = Int32
QUA_ADD: QueryUpdateAction = 0
QUA_REMOVE: QueryUpdateAction = 1
QUA_CHANGE: QueryUpdateAction = 2
SystemVisibilityFlags = Int32
SVF_SYSTEM: SystemVisibilityFlags = 0
SVF_USER: SystemVisibilityFlags = 1
make_head(_module, 'PKEY_FunctionInstance')
make_head(_module, 'PKEY_DeviceDisplay_Address')
make_head(_module, 'PKEY_DeviceDisplay_DiscoveryMethod')
make_head(_module, 'PKEY_DeviceDisplay_IsEncrypted')
make_head(_module, 'PKEY_DeviceDisplay_IsAuthenticated')
make_head(_module, 'PKEY_DeviceDisplay_IsConnected')
make_head(_module, 'PKEY_DeviceDisplay_IsPaired')
make_head(_module, 'PKEY_DeviceDisplay_Icon')
make_head(_module, 'PKEY_DeviceDisplay_Version')
make_head(_module, 'PKEY_DeviceDisplay_Last_Seen')
make_head(_module, 'PKEY_DeviceDisplay_Last_Connected')
make_head(_module, 'PKEY_DeviceDisplay_IsShowInDisconnectedState')
make_head(_module, 'PKEY_DeviceDisplay_IsLocalMachine')
make_head(_module, 'PKEY_DeviceDisplay_MetadataPath')
make_head(_module, 'PKEY_DeviceDisplay_IsMetadataSearchInProgress')
make_head(_module, 'PKEY_DeviceDisplay_MetadataChecksum')
make_head(_module, 'PKEY_DeviceDisplay_IsNotInterestingForDisplay')
make_head(_module, 'PKEY_DeviceDisplay_LaunchDeviceStageOnDeviceConnect')
make_head(_module, 'PKEY_DeviceDisplay_LaunchDeviceStageFromExplorer')
make_head(_module, 'PKEY_DeviceDisplay_BaselineExperienceId')
make_head(_module, 'PKEY_DeviceDisplay_IsDeviceUniquelyIdentifiable')
make_head(_module, 'PKEY_DeviceDisplay_AssociationArray')
make_head(_module, 'PKEY_DeviceDisplay_DeviceDescription1')
make_head(_module, 'PKEY_DeviceDisplay_DeviceDescription2')
make_head(_module, 'PKEY_DeviceDisplay_IsNotWorkingProperly')
make_head(_module, 'PKEY_DeviceDisplay_IsSharedDevice')
make_head(_module, 'PKEY_DeviceDisplay_IsNetworkDevice')
make_head(_module, 'PKEY_DeviceDisplay_IsDefaultDevice')
make_head(_module, 'PKEY_DeviceDisplay_MetadataCabinet')
make_head(_module, 'PKEY_DeviceDisplay_RequiresPairingElevation')
make_head(_module, 'PKEY_DeviceDisplay_ExperienceId')
make_head(_module, 'PKEY_DeviceDisplay_Category')
make_head(_module, 'PKEY_DeviceDisplay_Category_Desc_Singular')
make_head(_module, 'PKEY_DeviceDisplay_Category_Desc_Plural')
make_head(_module, 'PKEY_DeviceDisplay_Category_Icon')
make_head(_module, 'PKEY_DeviceDisplay_CategoryGroup_Desc')
make_head(_module, 'PKEY_DeviceDisplay_CategoryGroup_Icon')
make_head(_module, 'PKEY_DeviceDisplay_PrimaryCategory')
make_head(_module, 'PKEY_DeviceDisplay_UnpairUninstall')
make_head(_module, 'PKEY_DeviceDisplay_RequiresUninstallElevation')
make_head(_module, 'PKEY_DeviceDisplay_DeviceFunctionSubRank')
make_head(_module, 'PKEY_DeviceDisplay_AlwaysShowDeviceAsConnected')
make_head(_module, 'PKEY_DeviceDisplay_FriendlyName')
make_head(_module, 'PKEY_DeviceDisplay_Manufacturer')
make_head(_module, 'PKEY_DeviceDisplay_ModelName')
make_head(_module, 'PKEY_DeviceDisplay_ModelNumber')
make_head(_module, 'PKEY_DeviceDisplay_InstallInProgress')
make_head(_module, 'PKEY_Pairing_ListItemText')
make_head(_module, 'PKEY_Pairing_ListItemDescription')
make_head(_module, 'PKEY_Pairing_ListItemIcon')
make_head(_module, 'PKEY_Pairing_ListItemDefault')
make_head(_module, 'PKEY_Pairing_IsWifiOnlyDevice')
make_head(_module, 'PKEY_Device_BIOSVersion')
make_head(_module, 'PKEY_PNPX_GlobalIdentity')
make_head(_module, 'PKEY_PNPX_Types')
make_head(_module, 'PKEY_PNPX_Scopes')
make_head(_module, 'PKEY_PNPX_XAddrs')
make_head(_module, 'PKEY_PNPX_MetadataVersion')
make_head(_module, 'PKEY_PNPX_ID')
make_head(_module, 'PKEY_PNPX_RemoteAddress')
make_head(_module, 'PKEY_PNPX_RootProxy')
make_head(_module, 'PKEY_PNPX_ManufacturerUrl')
make_head(_module, 'PKEY_PNPX_ModelUrl')
make_head(_module, 'PKEY_PNPX_Upc')
make_head(_module, 'PKEY_PNPX_PresentationUrl')
make_head(_module, 'PKEY_PNPX_FirmwareVersion')
make_head(_module, 'PKEY_PNPX_SerialNumber')
make_head(_module, 'PKEY_PNPX_DeviceCategory')
make_head(_module, 'PKEY_PNPX_SecureChannel')
make_head(_module, 'PKEY_PNPX_CompactSignature')
make_head(_module, 'PKEY_PNPX_DeviceCertHash')
make_head(_module, 'PKEY_PNPX_DeviceCategory_Desc')
make_head(_module, 'PKEY_PNPX_Category_Desc_NonPlural')
make_head(_module, 'PKEY_PNPX_PhysicalAddress')
make_head(_module, 'PKEY_PNPX_NetworkInterfaceLuid')
make_head(_module, 'PKEY_PNPX_NetworkInterfaceGuid')
make_head(_module, 'PKEY_PNPX_IpAddress')
make_head(_module, 'PKEY_PNPX_ServiceAddress')
make_head(_module, 'PKEY_PNPX_ServiceId')
make_head(_module, 'PKEY_PNPX_ServiceTypes')
make_head(_module, 'PKEY_PNPX_ServiceControlUrl')
make_head(_module, 'PKEY_PNPX_ServiceDescUrl')
make_head(_module, 'PKEY_PNPX_ServiceEventSubUrl')
make_head(_module, 'PKEY_PNPX_DomainName')
make_head(_module, 'PKEY_PNPX_ShareName')
make_head(_module, 'PKEY_SSDP_AltLocationInfo')
make_head(_module, 'PKEY_SSDP_DevLifeTime')
make_head(_module, 'PKEY_SSDP_NetworkInterface')
make_head(_module, 'PKEY_PNPX_Installable')
make_head(_module, 'PKEY_PNPX_Associated')
make_head(_module, 'PKEY_PNPX_CompatibleTypes')
make_head(_module, 'PKEY_PNPX_InstallState')
make_head(_module, 'PKEY_PNPX_Removable')
make_head(_module, 'PKEY_PNPX_IPBusEnumerated')
make_head(_module, 'PKEY_WNET_Scope')
make_head(_module, 'PKEY_WNET_Type')
make_head(_module, 'PKEY_WNET_DisplayType')
make_head(_module, 'PKEY_WNET_Usage')
make_head(_module, 'PKEY_WNET_LocalName')
make_head(_module, 'PKEY_WNET_RemoteName')
make_head(_module, 'PKEY_WNET_Comment')
make_head(_module, 'PKEY_WNET_Provider')
make_head(_module, 'PKEY_WCN_Version')
make_head(_module, 'PKEY_WCN_RequestType')
make_head(_module, 'PKEY_WCN_AuthType')
make_head(_module, 'PKEY_WCN_EncryptType')
make_head(_module, 'PKEY_WCN_ConnType')
make_head(_module, 'PKEY_WCN_ConfigMethods')
make_head(_module, 'PKEY_WCN_RfBand')
make_head(_module, 'PKEY_WCN_AssocState')
make_head(_module, 'PKEY_WCN_ConfigError')
make_head(_module, 'PKEY_WCN_ConfigState')
make_head(_module, 'PKEY_WCN_DevicePasswordId')
make_head(_module, 'PKEY_WCN_OSVersion')
make_head(_module, 'PKEY_WCN_VendorExtension')
make_head(_module, 'PKEY_WCN_RegistrarType')
make_head(_module, 'PKEY_Hardware_Devinst')
make_head(_module, 'PKEY_Hardware_DisplayAttribute')
make_head(_module, 'PKEY_Hardware_DriverDate')
make_head(_module, 'PKEY_Hardware_DriverProvider')
make_head(_module, 'PKEY_Hardware_DriverVersion')
make_head(_module, 'PKEY_Hardware_Function')
make_head(_module, 'PKEY_Hardware_Icon')
make_head(_module, 'PKEY_Hardware_Image')
make_head(_module, 'PKEY_Hardware_Manufacturer')
make_head(_module, 'PKEY_Hardware_Model')
make_head(_module, 'PKEY_Hardware_Name')
make_head(_module, 'PKEY_Hardware_SerialNumber')
make_head(_module, 'PKEY_Hardware_ShellAttributes')
make_head(_module, 'PKEY_Hardware_Status')
make_head(_module, 'PKEY_NAME')
make_head(_module, 'PKEY_Device_DeviceDesc')
make_head(_module, 'PKEY_Device_HardwareIds')
make_head(_module, 'PKEY_Device_CompatibleIds')
make_head(_module, 'PKEY_Device_Service')
make_head(_module, 'PKEY_Device_Class')
make_head(_module, 'PKEY_Device_ClassGuid')
make_head(_module, 'PKEY_Device_Driver')
make_head(_module, 'PKEY_Device_ConfigFlags')
make_head(_module, 'PKEY_Device_Manufacturer')
make_head(_module, 'PKEY_Device_FriendlyName')
make_head(_module, 'PKEY_Device_LocationInfo')
make_head(_module, 'PKEY_Device_PDOName')
make_head(_module, 'PKEY_Device_Capabilities')
make_head(_module, 'PKEY_Device_UINumber')
make_head(_module, 'PKEY_Device_UpperFilters')
make_head(_module, 'PKEY_Device_LowerFilters')
make_head(_module, 'PKEY_Device_BusTypeGuid')
make_head(_module, 'PKEY_Device_LegacyBusType')
make_head(_module, 'PKEY_Device_BusNumber')
make_head(_module, 'PKEY_Device_EnumeratorName')
make_head(_module, 'PKEY_Device_Security')
make_head(_module, 'PKEY_Device_SecuritySDS')
make_head(_module, 'PKEY_Device_DevType')
make_head(_module, 'PKEY_Device_Exclusive')
make_head(_module, 'PKEY_Device_Characteristics')
make_head(_module, 'PKEY_Device_Address')
make_head(_module, 'PKEY_Device_UINumberDescFormat')
make_head(_module, 'PKEY_Device_PowerData')
make_head(_module, 'PKEY_Device_RemovalPolicy')
make_head(_module, 'PKEY_Device_RemovalPolicyDefault')
make_head(_module, 'PKEY_Device_RemovalPolicyOverride')
make_head(_module, 'PKEY_Device_InstallState')
make_head(_module, 'PKEY_Device_LocationPaths')
make_head(_module, 'PKEY_Device_BaseContainerId')
make_head(_module, 'PKEY_Device_DevNodeStatus')
make_head(_module, 'PKEY_Device_ProblemCode')
make_head(_module, 'PKEY_Device_EjectionRelations')
make_head(_module, 'PKEY_Device_RemovalRelations')
make_head(_module, 'PKEY_Device_PowerRelations')
make_head(_module, 'PKEY_Device_BusRelations')
make_head(_module, 'PKEY_Device_Parent')
make_head(_module, 'PKEY_Device_Children')
make_head(_module, 'PKEY_Device_Siblings')
make_head(_module, 'PKEY_Device_TransportRelations')
make_head(_module, 'PKEY_Device_Reported')
make_head(_module, 'PKEY_Device_Legacy')
make_head(_module, 'PKEY_Device_InstanceId')
make_head(_module, 'PKEY_Device_ContainerId')
make_head(_module, 'PKEY_Device_ModelId')
make_head(_module, 'PKEY_Device_FriendlyNameAttributes')
make_head(_module, 'PKEY_Device_ManufacturerAttributes')
make_head(_module, 'PKEY_Device_PresenceNotForDevice')
make_head(_module, 'PKEY_Device_SignalStrength')
make_head(_module, 'PKEY_Device_IsAssociateableByUserAction')
make_head(_module, 'PKEY_Numa_Proximity_Domain')
make_head(_module, 'PKEY_Device_DHP_Rebalance_Policy')
make_head(_module, 'PKEY_Device_Numa_Node')
make_head(_module, 'PKEY_Device_BusReportedDeviceDesc')
make_head(_module, 'PKEY_Device_InstallInProgress')
make_head(_module, 'PKEY_Device_DriverDate')
make_head(_module, 'PKEY_Device_DriverVersion')
make_head(_module, 'PKEY_Device_DriverDesc')
make_head(_module, 'PKEY_Device_DriverInfPath')
make_head(_module, 'PKEY_Device_DriverInfSection')
make_head(_module, 'PKEY_Device_DriverInfSectionExt')
make_head(_module, 'PKEY_Device_MatchingDeviceId')
make_head(_module, 'PKEY_Device_DriverProvider')
make_head(_module, 'PKEY_Device_DriverPropPageProvider')
make_head(_module, 'PKEY_Device_DriverCoInstallers')
make_head(_module, 'PKEY_Device_ResourcePickerTags')
make_head(_module, 'PKEY_Device_ResourcePickerExceptions')
make_head(_module, 'PKEY_Device_DriverRank')
make_head(_module, 'PKEY_Device_DriverLogoLevel')
make_head(_module, 'PKEY_Device_NoConnectSound')
make_head(_module, 'PKEY_Device_GenericDriverInstalled')
make_head(_module, 'PKEY_Device_AdditionalSoftwareRequested')
make_head(_module, 'PKEY_Device_SafeRemovalRequired')
make_head(_module, 'PKEY_Device_SafeRemovalRequiredOverride')
make_head(_module, 'PKEY_DrvPkg_Model')
make_head(_module, 'PKEY_DrvPkg_VendorWebSite')
make_head(_module, 'PKEY_DrvPkg_DetailedDescription')
make_head(_module, 'PKEY_DrvPkg_DocumentationLink')
make_head(_module, 'PKEY_DrvPkg_Icon')
make_head(_module, 'PKEY_DrvPkg_BrandingIcon')
make_head(_module, 'PKEY_DeviceClass_UpperFilters')
make_head(_module, 'PKEY_DeviceClass_LowerFilters')
make_head(_module, 'PKEY_DeviceClass_Security')
make_head(_module, 'PKEY_DeviceClass_SecuritySDS')
make_head(_module, 'PKEY_DeviceClass_DevType')
make_head(_module, 'PKEY_DeviceClass_Exclusive')
make_head(_module, 'PKEY_DeviceClass_Characteristics')
make_head(_module, 'PKEY_DeviceClass_Name')
make_head(_module, 'PKEY_DeviceClass_ClassName')
make_head(_module, 'PKEY_DeviceClass_Icon')
make_head(_module, 'PKEY_DeviceClass_ClassInstaller')
make_head(_module, 'PKEY_DeviceClass_PropPageProvider')
make_head(_module, 'PKEY_DeviceClass_NoInstallClass')
make_head(_module, 'PKEY_DeviceClass_NoDisplayClass')
make_head(_module, 'PKEY_DeviceClass_SilentInstall')
make_head(_module, 'PKEY_DeviceClass_NoUseClass')
make_head(_module, 'PKEY_DeviceClass_DefaultService')
make_head(_module, 'PKEY_DeviceClass_IconPath')
make_head(_module, 'PKEY_DeviceClass_ClassCoInstallers')
make_head(_module, 'PKEY_DeviceInterface_FriendlyName')
make_head(_module, 'PKEY_DeviceInterface_Enabled')
make_head(_module, 'PKEY_DeviceInterface_ClassGuid')
make_head(_module, 'PKEY_DeviceInterfaceClass_DefaultInterface')
make_head(_module, 'IFunctionDiscovery')
make_head(_module, 'IFunctionDiscoveryNotification')
make_head(_module, 'IFunctionDiscoveryProvider')
make_head(_module, 'IFunctionDiscoveryProviderFactory')
make_head(_module, 'IFunctionDiscoveryProviderQuery')
make_head(_module, 'IFunctionDiscoveryServiceProvider')
make_head(_module, 'IFunctionInstance')
make_head(_module, 'IFunctionInstanceCollection')
make_head(_module, 'IFunctionInstanceCollectionQuery')
make_head(_module, 'IFunctionInstanceQuery')
make_head(_module, 'IPNPXAssociation')
make_head(_module, 'IPNPXDeviceAssociation')
make_head(_module, 'IPropertyStoreCollection')
make_head(_module, 'IProviderProperties')
make_head(_module, 'IProviderPropertyConstraintCollection')
make_head(_module, 'IProviderPublishing')
make_head(_module, 'IProviderQueryConstraintCollection')
