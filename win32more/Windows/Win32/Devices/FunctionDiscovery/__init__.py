from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
import win32more.Windows.Win32.Devices.FunctionDiscovery
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.UI.Shell.PropertiesSystem
FD_EVENTID_PRIVATE: UInt32 = 100
FD_EVENTID: UInt32 = 1000
FD_EVENTID_SEARCHCOMPLETE: UInt32 = 1000
FD_EVENTID_ASYNCTHREADEXIT: UInt32 = 1001
FD_EVENTID_SEARCHSTART: UInt32 = 1002
FD_EVENTID_IPADDRESSCHANGE: UInt32 = 1003
FD_EVENTID_QUERYREFRESH: UInt32 = 1004
SID_PnpProvider: Guid = Guid('{8101368e-cabb-4426-acff-96c410812000}')
SID_UPnPActivator: Guid = Guid('{0d0d66eb-cf74-4164-b52f-08344672dd46}')
SID_EnumInterface: Guid = Guid('{40eab0b9-4d7f-4b53-a334-1581dd9041f4}')
SID_PNPXPropertyStore: Guid = Guid('{a86530b1-542f-439f-b71c-b0756b13677a}')
SID_PNPXAssociation: Guid = Guid('{cee8ccc9-4f6b-4469-a235-5a22869eef03}')
SID_PNPXServiceCollection: Guid = Guid('{439e80ee-a217-4712-9fa6-deabd9c2a727}')
SID_FDPairingHandler: Guid = Guid('{383b69fa-5486-49da-91f5-d63c24c8e9d0}')
SID_EnumDeviceFunction: Guid = Guid('{13e0e9e2-c3fa-4e3c-906e-64502fa4dc95}')
SID_UnpairProvider: Guid = Guid('{89a502fc-857b-4698-a0b7-027192002f9e}')
SID_DeviceDisplayStatusManager: Guid = Guid('{f59aa553-8309-46ca-9736-1ac3c62d6031}')
SID_FunctionDiscoveryProviderRefresh: Guid = Guid('{2b4cbdc9-31c4-40d4-a62d-772aa174ed52}')
SID_UninstallDeviceFunction: Guid = Guid('{c920566e-5671-4496-8025-bf0b89bd44cd}')
def PKEY_FunctionInstance():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{08c0c253-a154-4746-9005-82de5317148b}'), pid=1)
FMTID_FD: Guid = Guid('{904b03a2-471d-423c-a584-f3483238a146}')
FD_Visibility_Default: UInt32 = 0
FD_Visibility_Hidden: UInt32 = 1
FMTID_Device: Guid = Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}')
FMTID_DeviceInterface: Guid = Guid('{53808008-07bb-4661-bc3c-b5953e708560}')
def PKEY_DeviceDisplay_Address():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=51)
def PKEY_DeviceDisplay_DiscoveryMethod():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=52)
def PKEY_DeviceDisplay_IsEncrypted():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=53)
def PKEY_DeviceDisplay_IsAuthenticated():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=54)
def PKEY_DeviceDisplay_IsConnected():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=55)
def PKEY_DeviceDisplay_IsPaired():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=56)
def PKEY_DeviceDisplay_Icon():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=57)
def PKEY_DeviceDisplay_Version():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=65)
def PKEY_DeviceDisplay_Last_Seen():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=66)
def PKEY_DeviceDisplay_Last_Connected():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=67)
def PKEY_DeviceDisplay_IsShowInDisconnectedState():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=68)
def PKEY_DeviceDisplay_IsLocalMachine():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=70)
def PKEY_DeviceDisplay_MetadataPath():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=71)
def PKEY_DeviceDisplay_IsMetadataSearchInProgress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=72)
def PKEY_DeviceDisplay_MetadataChecksum():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=73)
def PKEY_DeviceDisplay_IsNotInterestingForDisplay():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=74)
def PKEY_DeviceDisplay_LaunchDeviceStageOnDeviceConnect():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=76)
def PKEY_DeviceDisplay_LaunchDeviceStageFromExplorer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=77)
def PKEY_DeviceDisplay_BaselineExperienceId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=78)
def PKEY_DeviceDisplay_IsDeviceUniquelyIdentifiable():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=79)
def PKEY_DeviceDisplay_AssociationArray():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=80)
def PKEY_DeviceDisplay_DeviceDescription1():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=81)
def PKEY_DeviceDisplay_DeviceDescription2():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=82)
def PKEY_DeviceDisplay_IsNotWorkingProperly():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=83)
def PKEY_DeviceDisplay_IsSharedDevice():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=84)
def PKEY_DeviceDisplay_IsNetworkDevice():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=85)
def PKEY_DeviceDisplay_IsDefaultDevice():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=86)
def PKEY_DeviceDisplay_MetadataCabinet():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=87)
def PKEY_DeviceDisplay_RequiresPairingElevation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=88)
def PKEY_DeviceDisplay_ExperienceId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=89)
def PKEY_DeviceDisplay_Category():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=90)
def PKEY_DeviceDisplay_Category_Desc_Singular():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=91)
def PKEY_DeviceDisplay_Category_Desc_Plural():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=92)
def PKEY_DeviceDisplay_Category_Icon():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=93)
def PKEY_DeviceDisplay_CategoryGroup_Desc():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=94)
def PKEY_DeviceDisplay_CategoryGroup_Icon():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=95)
def PKEY_DeviceDisplay_PrimaryCategory():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=97)
def PKEY_DeviceDisplay_UnpairUninstall():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=98)
def PKEY_DeviceDisplay_RequiresUninstallElevation():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=99)
def PKEY_DeviceDisplay_DeviceFunctionSubRank():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=100)
def PKEY_DeviceDisplay_AlwaysShowDeviceAsConnected():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=101)
def PKEY_DeviceDisplay_FriendlyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12288)
def PKEY_DeviceDisplay_Manufacturer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8192)
def PKEY_DeviceDisplay_ModelName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8194)
def PKEY_DeviceDisplay_ModelNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8195)
def PKEY_DeviceDisplay_InstallInProgress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=9)
FMTID_Pairing: Guid = Guid('{8807cae6-7db6-4f10-8ee4-435eaa1392bc}')
def PKEY_Pairing_ListItemText():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8807cae6-7db6-4f10-8ee4-435eaa1392bc}'), pid=1)
def PKEY_Pairing_ListItemDescription():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8807cae6-7db6-4f10-8ee4-435eaa1392bc}'), pid=2)
def PKEY_Pairing_ListItemIcon():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8807cae6-7db6-4f10-8ee4-435eaa1392bc}'), pid=3)
def PKEY_Pairing_ListItemDefault():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8807cae6-7db6-4f10-8ee4-435eaa1392bc}'), pid=4)
def PKEY_Pairing_IsWifiOnlyDevice():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8807cae6-7db6-4f10-8ee4-435eaa1392bc}'), pid=16)
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
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{eaee7f1d-6a33-44d1-9441-5f46def23198}'), pid=9)
FMTID_WSD: Guid = Guid('{92506491-ff95-4724-a05a-5b81885a7c92}')
FMTID_PNPX: Guid = Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}')
def PKEY_PNPX_GlobalIdentity():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=4096)
def PKEY_PNPX_Types():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=4097)
def PKEY_PNPX_Scopes():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=4098)
def PKEY_PNPX_XAddrs():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=4099)
def PKEY_PNPX_MetadataVersion():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=4100)
def PKEY_PNPX_ID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=4101)
def PKEY_PNPX_RemoteAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=4102)
def PKEY_PNPX_RootProxy():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=4103)
def PKEY_PNPX_ManufacturerUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8193)
def PKEY_PNPX_ModelUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8196)
def PKEY_PNPX_Upc():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8197)
def PKEY_PNPX_PresentationUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8198)
def PKEY_PNPX_FirmwareVersion():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12289)
def PKEY_PNPX_SerialNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12290)
def PKEY_PNPX_DeviceCategory():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12292)
def PKEY_PNPX_SecureChannel():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=28673)
def PKEY_PNPX_CompactSignature():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=28674)
def PKEY_PNPX_DeviceCertHash():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=28675)
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
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12293)
def PKEY_PNPX_Category_Desc_NonPlural():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12304)
def PKEY_PNPX_PhysicalAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12294)
def PKEY_PNPX_NetworkInterfaceLuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12295)
def PKEY_PNPX_NetworkInterfaceGuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12296)
def PKEY_PNPX_IpAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12297)
def PKEY_PNPX_ServiceAddress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=16384)
def PKEY_PNPX_ServiceId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=16385)
def PKEY_PNPX_ServiceTypes():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=16386)
def PKEY_PNPX_ServiceControlUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=16388)
def PKEY_PNPX_ServiceDescUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=16389)
def PKEY_PNPX_ServiceEventSubUrl():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=16390)
def PKEY_PNPX_DomainName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=20480)
def PKEY_PNPX_ShareName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=20482)
def PKEY_SSDP_AltLocationInfo():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=24576)
def PKEY_SSDP_DevLifeTime():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=24577)
def PKEY_SSDP_NetworkInterface():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=24578)
FMTID_PNPXDynamicProperty: Guid = Guid('{4fc5077e-b686-44be-93e3-86cafe368ccd}')
def PKEY_PNPX_Installable():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4fc5077e-b686-44be-93e3-86cafe368ccd}'), pid=1)
def PKEY_PNPX_Associated():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4fc5077e-b686-44be-93e3-86cafe368ccd}'), pid=2)
def PKEY_PNPX_CompatibleTypes():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4fc5077e-b686-44be-93e3-86cafe368ccd}'), pid=3)
def PKEY_PNPX_InstallState():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4fc5077e-b686-44be-93e3-86cafe368ccd}'), pid=4)
PNPX_INSTALLSTATE_NOTINSTALLED: UInt32 = 0
PNPX_INSTALLSTATE_INSTALLED: UInt32 = 1
PNPX_INSTALLSTATE_INSTALLING: UInt32 = 2
PNPX_INSTALLSTATE_FAILED: UInt32 = 3
def PKEY_PNPX_Removable():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=28672)
def PKEY_PNPX_IPBusEnumerated():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=28688)
def PKEY_WNET_Scope():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{debda43a-37b3-4383-91e7-4498da2995ab}'), pid=1)
def PKEY_WNET_Type():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{debda43a-37b3-4383-91e7-4498da2995ab}'), pid=2)
def PKEY_WNET_DisplayType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{debda43a-37b3-4383-91e7-4498da2995ab}'), pid=3)
def PKEY_WNET_Usage():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{debda43a-37b3-4383-91e7-4498da2995ab}'), pid=4)
def PKEY_WNET_LocalName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{debda43a-37b3-4383-91e7-4498da2995ab}'), pid=5)
def PKEY_WNET_RemoteName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{debda43a-37b3-4383-91e7-4498da2995ab}'), pid=6)
def PKEY_WNET_Comment():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{debda43a-37b3-4383-91e7-4498da2995ab}'), pid=7)
def PKEY_WNET_Provider():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{debda43a-37b3-4383-91e7-4498da2995ab}'), pid=8)
def PKEY_WCN_Version():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b80-4684-11da-a26a-0002b3988e81}'), pid=1)
def PKEY_WCN_RequestType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b81-4684-11da-a26a-0002b3988e81}'), pid=2)
def PKEY_WCN_AuthType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b82-4684-11da-a26a-0002b3988e81}'), pid=3)
def PKEY_WCN_EncryptType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b83-4684-11da-a26a-0002b3988e81}'), pid=4)
def PKEY_WCN_ConnType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b84-4684-11da-a26a-0002b3988e81}'), pid=5)
def PKEY_WCN_ConfigMethods():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b85-4684-11da-a26a-0002b3988e81}'), pid=6)
def PKEY_WCN_RfBand():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b87-4684-11da-a26a-0002b3988e81}'), pid=8)
def PKEY_WCN_AssocState():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b88-4684-11da-a26a-0002b3988e81}'), pid=9)
def PKEY_WCN_ConfigError():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b89-4684-11da-a26a-0002b3988e81}'), pid=10)
def PKEY_WCN_ConfigState():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b89-4684-11da-a26a-0002b3988e81}'), pid=11)
def PKEY_WCN_DevicePasswordId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b89-4684-11da-a26a-0002b3988e81}'), pid=12)
def PKEY_WCN_OSVersion():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b89-4684-11da-a26a-0002b3988e81}'), pid=13)
def PKEY_WCN_VendorExtension():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b8a-4684-11da-a26a-0002b3988e81}'), pid=14)
def PKEY_WCN_RegistrarType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{88190b8b-4684-11da-a26a-0002b3988e81}'), pid=15)
def PKEY_Hardware_Devinst():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=4097)
def PKEY_Hardware_DisplayAttribute():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=5)
def PKEY_Hardware_DriverDate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=11)
def PKEY_Hardware_DriverProvider():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=10)
def PKEY_Hardware_DriverVersion():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=9)
def PKEY_Hardware_Function():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=4099)
def PKEY_Hardware_Icon():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=3)
def PKEY_Hardware_Image():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=4098)
def PKEY_Hardware_Manufacturer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=6)
def PKEY_Hardware_Model():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=7)
def PKEY_Hardware_Name():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=2)
def PKEY_Hardware_SerialNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=8)
def PKEY_Hardware_ShellAttributes():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=4100)
def PKEY_Hardware_Status():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953}'), pid=4096)
def PKEY_NAME():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=10)
def PKEY_Device_DeviceDesc():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=2)
def PKEY_Device_HardwareIds():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=3)
def PKEY_Device_CompatibleIds():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=4)
def PKEY_Device_Service():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=6)
def PKEY_Device_Class():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=9)
def PKEY_Device_ClassGuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=10)
def PKEY_Device_Driver():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=11)
def PKEY_Device_ConfigFlags():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=12)
def PKEY_Device_Manufacturer():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=13)
def PKEY_Device_FriendlyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=14)
def PKEY_Device_LocationInfo():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=15)
def PKEY_Device_PDOName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=16)
def PKEY_Device_Capabilities():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=17)
def PKEY_Device_UINumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=18)
def PKEY_Device_UpperFilters():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=19)
def PKEY_Device_LowerFilters():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=20)
def PKEY_Device_BusTypeGuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=21)
def PKEY_Device_LegacyBusType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=22)
def PKEY_Device_BusNumber():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=23)
def PKEY_Device_EnumeratorName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=24)
def PKEY_Device_Security():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=25)
def PKEY_Device_SecuritySDS():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=26)
def PKEY_Device_DevType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=27)
def PKEY_Device_Exclusive():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=28)
def PKEY_Device_Characteristics():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=29)
def PKEY_Device_Address():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=30)
def PKEY_Device_UINumberDescFormat():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=31)
def PKEY_Device_PowerData():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=32)
def PKEY_Device_RemovalPolicy():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=33)
def PKEY_Device_RemovalPolicyDefault():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=34)
def PKEY_Device_RemovalPolicyOverride():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=35)
def PKEY_Device_InstallState():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=36)
def PKEY_Device_LocationPaths():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=37)
def PKEY_Device_BaseContainerId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=38)
def PKEY_Device_DevNodeStatus():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=2)
def PKEY_Device_ProblemCode():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=3)
def PKEY_Device_EjectionRelations():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=4)
def PKEY_Device_RemovalRelations():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=5)
def PKEY_Device_PowerRelations():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=6)
def PKEY_Device_BusRelations():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=7)
def PKEY_Device_Parent():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=8)
def PKEY_Device_Children():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=9)
def PKEY_Device_Siblings():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=10)
def PKEY_Device_TransportRelations():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=11)
def PKEY_Device_Reported():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{80497100-8c73-48b9-aad9-ce387e19c56e}'), pid=2)
def PKEY_Device_Legacy():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{80497100-8c73-48b9-aad9-ce387e19c56e}'), pid=3)
def PKEY_Device_InstanceId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=256)
def PKEY_Device_ContainerId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c}'), pid=2)
def PKEY_Device_ModelId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=2)
def PKEY_Device_FriendlyNameAttributes():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=3)
def PKEY_Device_ManufacturerAttributes():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=4)
def PKEY_Device_PresenceNotForDevice():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=5)
def PKEY_Device_SignalStrength():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=6)
def PKEY_Device_IsAssociateableByUserAction():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=7)
def PKEY_Numa_Proximity_Domain():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=1)
def PKEY_Device_DHP_Rebalance_Policy():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=2)
def PKEY_Device_Numa_Node():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=3)
def PKEY_Device_BusReportedDeviceDesc():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=4)
def PKEY_Device_InstallInProgress():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=9)
def PKEY_Device_DriverDate():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=2)
def PKEY_Device_DriverVersion():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=3)
def PKEY_Device_DriverDesc():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=4)
def PKEY_Device_DriverInfPath():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=5)
def PKEY_Device_DriverInfSection():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=6)
def PKEY_Device_DriverInfSectionExt():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=7)
def PKEY_Device_MatchingDeviceId():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=8)
def PKEY_Device_DriverProvider():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=9)
def PKEY_Device_DriverPropPageProvider():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=10)
def PKEY_Device_DriverCoInstallers():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=11)
def PKEY_Device_ResourcePickerTags():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=12)
def PKEY_Device_ResourcePickerExceptions():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=13)
def PKEY_Device_DriverRank():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=14)
def PKEY_Device_DriverLogoLevel():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=15)
def PKEY_Device_NoConnectSound():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=17)
def PKEY_Device_GenericDriverInstalled():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=18)
def PKEY_Device_AdditionalSoftwareRequested():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=19)
def PKEY_Device_SafeRemovalRequired():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{afd97640-86a3-4210-b67c-289c41aabe55}'), pid=2)
def PKEY_Device_SafeRemovalRequiredOverride():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{afd97640-86a3-4210-b67c-289c41aabe55}'), pid=3)
def PKEY_DrvPkg_Model():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=2)
def PKEY_DrvPkg_VendorWebSite():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=3)
def PKEY_DrvPkg_DetailedDescription():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=4)
def PKEY_DrvPkg_DocumentationLink():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=5)
def PKEY_DrvPkg_Icon():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=6)
def PKEY_DrvPkg_BrandingIcon():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=7)
def PKEY_DeviceClass_UpperFilters():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=19)
def PKEY_DeviceClass_LowerFilters():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=20)
def PKEY_DeviceClass_Security():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=25)
def PKEY_DeviceClass_SecuritySDS():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=26)
def PKEY_DeviceClass_DevType():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=27)
def PKEY_DeviceClass_Exclusive():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=28)
def PKEY_DeviceClass_Characteristics():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=29)
def PKEY_DeviceClass_Name():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=2)
def PKEY_DeviceClass_ClassName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=3)
def PKEY_DeviceClass_Icon():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=4)
def PKEY_DeviceClass_ClassInstaller():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=5)
def PKEY_DeviceClass_PropPageProvider():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=6)
def PKEY_DeviceClass_NoInstallClass():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=7)
def PKEY_DeviceClass_NoDisplayClass():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=8)
def PKEY_DeviceClass_SilentInstall():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=9)
def PKEY_DeviceClass_NoUseClass():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=10)
def PKEY_DeviceClass_DefaultService():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=11)
def PKEY_DeviceClass_IconPath():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=12)
def PKEY_DeviceClass_ClassCoInstallers():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{713d1703-a2e2-49f5-9214-56472ef3da5c}'), pid=2)
def PKEY_DeviceInterface_FriendlyName():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=2)
def PKEY_DeviceInterface_Enabled():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=3)
def PKEY_DeviceInterface_ClassGuid():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=4)
def PKEY_DeviceInterfaceClass_DefaultInterface():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{14c83a99-0b3f-44b7-be4c-a178d3990564}'), pid=2)
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
E_FDPAIRING_NOCONNECTION: win32more.Windows.Win32.Foundation.HRESULT = -1882193919
E_FDPAIRING_HWFAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1882193918
E_FDPAIRING_AUTHFAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1882193917
E_FDPAIRING_CONNECTTIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -1882193916
E_FDPAIRING_TOOMANYCONNECTIONS: win32more.Windows.Win32.Foundation.HRESULT = -1882193915
E_FDPAIRING_AUTHNOTALLOWED: win32more.Windows.Win32.Foundation.HRESULT = -1882193914
E_FDPAIRING_IPBUSDISABLED: win32more.Windows.Win32.Foundation.HRESULT = -1882193913
E_FDPAIRING_NOPROFILES: win32more.Windows.Win32.Foundation.HRESULT = -1882193912
FunctionDiscovery = Guid('{c72be2ec-8e90-452c-b29a-ab8ff1c071fc}')
FunctionInstanceCollection = Guid('{ba818ce5-b55f-443f-ad39-2fe89be6191f}')
class IFunctionDiscovery(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4df99b70-e148-4432-b004-4c9eeb535a5e}')
    @commethod(3)
    def GetInstanceCollection(self, pszCategory: win32more.Windows.Win32.Foundation.PWSTR, pszSubCategory: win32more.Windows.Win32.Foundation.PWSTR, fIncludeAllSubCategories: win32more.Windows.Win32.Foundation.BOOL, ppIFunctionInstanceCollection: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInstance(self, pszFunctionInstanceIdentity: win32more.Windows.Win32.Foundation.PWSTR, ppIFunctionInstance: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateInstanceCollectionQuery(self, pszCategory: win32more.Windows.Win32.Foundation.PWSTR, pszSubCategory: win32more.Windows.Win32.Foundation.PWSTR, fIncludeAllSubCategories: win32more.Windows.Win32.Foundation.BOOL, pIFunctionDiscoveryNotification: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification, pfdqcQueryContext: POINTER(UInt64), ppIFunctionInstanceCollectionQuery: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceCollectionQuery)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateInstanceQuery(self, pszFunctionInstanceIdentity: win32more.Windows.Win32.Foundation.PWSTR, pIFunctionDiscoveryNotification: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification, pfdqcQueryContext: POINTER(UInt64), ppIFunctionInstanceQuery: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceQuery)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddInstance(self, enumSystemVisibility: win32more.Windows.Win32.Devices.FunctionDiscovery.SystemVisibilityFlags, pszCategory: win32more.Windows.Win32.Foundation.PWSTR, pszSubCategory: win32more.Windows.Win32.Foundation.PWSTR, pszCategoryIdentity: win32more.Windows.Win32.Foundation.PWSTR, ppIFunctionInstance: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveInstance(self, enumSystemVisibility: win32more.Windows.Win32.Devices.FunctionDiscovery.SystemVisibilityFlags, pszCategory: win32more.Windows.Win32.Foundation.PWSTR, pszSubCategory: win32more.Windows.Win32.Foundation.PWSTR, pszCategoryIdentity: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFunctionDiscoveryNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5f6c1ba8-5330-422e-a368-572b244d3f87}')
    @commethod(3)
    def OnUpdate(self, enumQueryUpdateAction: win32more.Windows.Win32.Devices.FunctionDiscovery.QueryUpdateAction, fdqcQueryContext: UInt64, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnError(self, hr: win32more.Windows.Win32.Foundation.HRESULT, fdqcQueryContext: UInt64, pszProvider: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEvent(self, dwEventID: UInt32, fdqcQueryContext: UInt64, pszProvider: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFunctionDiscoveryProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcde394f-1478-4813-a402-f6fb10657222}')
    @commethod(3)
    def Initialize(self, pIFunctionDiscoveryProviderFactory: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryProviderFactory, pIFunctionDiscoveryNotification: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification, lcidUserDefault: UInt32, pdwStgAccessCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Query(self, pIFunctionDiscoveryProviderQuery: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryProviderQuery, ppIFunctionInstanceCollection: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndQuery(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InstancePropertyStoreValidateAccess(self, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance, iProviderInstanceContext: IntPtr, dwStgAccess: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InstancePropertyStoreOpen(self, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance, iProviderInstanceContext: IntPtr, dwStgAccess: UInt32, ppIPropertyStore: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InstancePropertyStoreFlush(self, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance, iProviderInstanceContext: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def InstanceQueryService(self, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance, iProviderInstanceContext: IntPtr, guidService: POINTER(Guid), riid: POINTER(Guid), ppIUnknown: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def InstanceReleased(self, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance, iProviderInstanceContext: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFunctionDiscoveryProviderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{86443ff0-1ad5-4e68-a45a-40c2c329de3b}')
    @commethod(3)
    def CreatePropertyStore(self, ppIPropertyStore: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateInstance(self, pszSubCategory: win32more.Windows.Win32.Foundation.PWSTR, pszProviderInstanceIdentity: win32more.Windows.Win32.Foundation.PWSTR, iProviderInstanceContext: IntPtr, pIPropertyStore: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore, pIFunctionDiscoveryProvider: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryProvider, ppIFunctionInstance: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateFunctionInstanceCollection(self, ppIFunctionInstanceCollection: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFunctionDiscoveryProviderQuery(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6876ea98-baec-46db-bc20-75a76e267a3a}')
    @commethod(3)
    def IsInstanceQuery(self, pisInstanceQuery: POINTER(win32more.Windows.Win32.Foundation.BOOL), ppszConstraintValue: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsSubcategoryQuery(self, pisSubcategoryQuery: POINTER(win32more.Windows.Win32.Foundation.BOOL), ppszConstraintValue: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetQueryConstraints(self, ppIProviderQueryConstraints: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IProviderQueryConstraintCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyConstraints(self, ppIProviderPropertyConstraints: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IProviderPropertyConstraintCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFunctionDiscoveryServiceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4c81ed02-1b04-43f2-a451-69966cbcd1c2}')
    @commethod(3)
    def Initialize(self, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFunctionInstance(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IServiceProvider
    _iid_ = Guid('{33591c10-0bed-4f02-b0ab-1530d5533ee9}')
    @commethod(4)
    def GetID(self, ppszCoMemIdentity: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProviderInstanceID(self, ppszCoMemProviderInstanceIdentity: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OpenPropertyStore(self, dwStgAccess: win32more.Windows.Win32.System.Com.STGM, ppIPropertyStore: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCategory(self, ppszCoMemCategory: POINTER(POINTER(UInt16)), ppszCoMemSubCategory: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFunctionInstanceCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f0a3d895-855c-42a2-948d-2f97d450ecb1}')
    @commethod(3)
    def GetCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Get(self, pszInstanceIdentity: win32more.Windows.Win32.Foundation.PWSTR, pdwIndex: POINTER(UInt32), ppIFunctionInstance: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, dwIndex: UInt32, ppIFunctionInstance: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Add(self, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Remove(self, dwIndex: UInt32, ppIFunctionInstance: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Delete(self, dwIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFunctionInstanceCollectionQuery(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{57cc6fd2-c09a-4289-bb72-25f04142058e}')
    @commethod(3)
    def AddQueryConstraint(self, pszConstraintName: win32more.Windows.Win32.Foundation.PWSTR, pszConstraintValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPropertyConstraint(self, Key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY), pv: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), enumPropertyConstraint: win32more.Windows.Win32.Devices.FunctionDiscovery.PropertyConstraint) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Execute(self, ppIFunctionInstanceCollection: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstanceCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFunctionInstanceQuery(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6242bc6b-90ec-4b37-bb46-e229fd84ed95}')
    @commethod(3)
    def Execute(self, ppIFunctionInstance: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPNPXAssociation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0bd7e521-4da6-42d5-81ba-1981b6b94075}')
    @commethod(3)
    def Associate(self, pszSubcategory: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unassociate(self, pszSubcategory: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(self, pszSubcategory: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPNPXDeviceAssociation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eed366d0-35b8-4fc5-8d20-7e5bd31f6ded}')
    @commethod(3)
    def Associate(self, pszSubCategory: win32more.Windows.Win32.Foundation.PWSTR, pIFunctionDiscoveryNotification: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unassociate(self, pszSubCategory: win32more.Windows.Win32.Foundation.PWSTR, pIFunctionDiscoveryNotification: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(self, pszSubcategory: win32more.Windows.Win32.Foundation.PWSTR, pIFunctionDiscoveryNotification: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionDiscoveryNotification) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyStoreCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d14d9c30-12d2-42d8-bce4-c60c2bb226fa}')
    @commethod(3)
    def GetCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Get(self, pszInstanceIdentity: win32more.Windows.Win32.Foundation.PWSTR, pdwIndex: POINTER(UInt32), ppIPropertyStore: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, dwIndex: UInt32, ppIPropertyStore: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Add(self, pIPropertyStore: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Remove(self, dwIndex: UInt32, pIPropertyStore: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Delete(self, dwIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProviderProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cf986ea6-3b5f-4c5f-b88a-2f8b20ceef17}')
    @commethod(3)
    def GetCount(self, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance, iProviderInstanceContext: IntPtr, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance, iProviderInstanceContext: IntPtr, dwIndex: UInt32, pKey: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetValue(self, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance, iProviderInstanceContext: IntPtr, Key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY), ppropVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetValue(self, pIFunctionInstance: win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance, iProviderInstanceContext: IntPtr, Key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY), ppropVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProviderPropertyConstraintCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f4fae42f-5778-4a13-8540-b5fd8c1398dd}')
    @commethod(3)
    def GetCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Get(self, Key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY), pPropVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pdwPropertyConstraint: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, dwIndex: UInt32, pKey: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY), pPropVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pdwPropertyConstraint: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Next(self, pKey: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY), pPropVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pdwPropertyConstraint: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Skip(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProviderPublishing(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cd1b9a04-206c-4a05-a0c8-1635a21a2b7c}')
    @commethod(3)
    def CreateInstance(self, enumVisibilityFlags: win32more.Windows.Win32.Devices.FunctionDiscovery.SystemVisibilityFlags, pszSubCategory: win32more.Windows.Win32.Foundation.PWSTR, pszProviderInstanceIdentity: win32more.Windows.Win32.Foundation.PWSTR, ppIFunctionInstance: POINTER(win32more.Windows.Win32.Devices.FunctionDiscovery.IFunctionInstance)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveInstance(self, enumVisibilityFlags: win32more.Windows.Win32.Devices.FunctionDiscovery.SystemVisibilityFlags, pszSubCategory: win32more.Windows.Win32.Foundation.PWSTR, pszProviderInstanceIdentity: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProviderQueryConstraintCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c243e11-3261-4bcd-b922-84a873d460ae}')
    @commethod(3)
    def GetCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Get(self, pszConstraintName: win32more.Windows.Win32.Foundation.PWSTR, ppszConstraintValue: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, dwIndex: UInt32, ppszConstraintName: POINTER(POINTER(UInt16)), ppszConstraintValue: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Next(self, ppszConstraintName: POINTER(POINTER(UInt16)), ppszConstraintValue: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Skip(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PNPXAssociation = Guid('{cee8ccc9-4f6b-4469-a235-5a22869eef03}')
PNPXPairingHandler = Guid('{b8a27942-ade7-4085-aa6e-4fadc7ada1ef}')
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
PropertyStore = Guid('{e4796550-df61-448b-9193-13fc1341b163}')
PropertyStoreCollection = Guid('{edd36029-d753-4862-aa5b-5bccad2a4d29}')
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
make_ready(__name__)
