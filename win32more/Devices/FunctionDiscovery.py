from win32more import *
import win32more.Devices.FunctionDiscovery
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
FD_EVENTID_PRIVATE = 100
FD_EVENTID = 1000
FD_EVENTID_SEARCHCOMPLETE = 1000
FD_EVENTID_ASYNCTHREADEXIT = 1001
FD_EVENTID_SEARCHSTART = 1002
FD_EVENTID_IPADDRESSCHANGE = 1003
FD_EVENTID_QUERYREFRESH = 1004
SID_PnpProvider = '8101368e-cabb-4426-acff-96c410812000'
SID_UPnPActivator = '0d0d66eb-cf74-4164-b52f-08344672dd46'
SID_EnumInterface = '40eab0b9-4d7f-4b53-a334-1581dd9041f4'
SID_PNPXPropertyStore = 'a86530b1-542f-439f-b71c-b0756b13677a'
SID_PNPXAssociation = 'cee8ccc9-4f6b-4469-a235-5a22869eef03'
SID_PNPXServiceCollection = '439e80ee-a217-4712-9fa6-deabd9c2a727'
SID_FDPairingHandler = '383b69fa-5486-49da-91f5-d63c24c8e9d0'
SID_EnumDeviceFunction = '13e0e9e2-c3fa-4e3c-906e-64502fa4dc95'
SID_UnpairProvider = '89a502fc-857b-4698-a0b7-027192002f9e'
SID_DeviceDisplayStatusManager = 'f59aa553-8309-46ca-9736-1ac3c62d6031'
SID_FunctionDiscoveryProviderRefresh = '2b4cbdc9-31c4-40d4-a62d-772aa174ed52'
SID_UninstallDeviceFunction = 'c920566e-5671-4496-8025-bf0b89bd44cd'
PKEY_FunctionInstance = PROPERTYKEY(Fmtid='08c0c253-a154-4746-9005-82de5317148b', Pid=1)
FMTID_FD = '904b03a2-471d-423c-a584-f3483238a146'
FD_Visibility_Default = 0
FD_Visibility_Hidden = 1
FMTID_Device = '78c34fc8-104a-4aca-9ea4-524d52996e57'
FMTID_DeviceInterface = '53808008-07bb-4661-bc3c-b5953e708560'
PKEY_DeviceDisplay_Address = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=51)
PKEY_DeviceDisplay_DiscoveryMethod = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=52)
PKEY_DeviceDisplay_IsEncrypted = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=53)
PKEY_DeviceDisplay_IsAuthenticated = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=54)
PKEY_DeviceDisplay_IsConnected = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=55)
PKEY_DeviceDisplay_IsPaired = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=56)
PKEY_DeviceDisplay_Icon = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=57)
PKEY_DeviceDisplay_Version = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=65)
PKEY_DeviceDisplay_Last_Seen = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=66)
PKEY_DeviceDisplay_Last_Connected = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=67)
PKEY_DeviceDisplay_IsShowInDisconnectedState = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=68)
PKEY_DeviceDisplay_IsLocalMachine = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=70)
PKEY_DeviceDisplay_MetadataPath = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=71)
PKEY_DeviceDisplay_IsMetadataSearchInProgress = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=72)
PKEY_DeviceDisplay_MetadataChecksum = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=73)
PKEY_DeviceDisplay_IsNotInterestingForDisplay = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=74)
PKEY_DeviceDisplay_LaunchDeviceStageOnDeviceConnect = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=76)
PKEY_DeviceDisplay_LaunchDeviceStageFromExplorer = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=77)
PKEY_DeviceDisplay_BaselineExperienceId = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=78)
PKEY_DeviceDisplay_IsDeviceUniquelyIdentifiable = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=79)
PKEY_DeviceDisplay_AssociationArray = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=80)
PKEY_DeviceDisplay_DeviceDescription1 = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=81)
PKEY_DeviceDisplay_DeviceDescription2 = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=82)
PKEY_DeviceDisplay_IsNotWorkingProperly = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=83)
PKEY_DeviceDisplay_IsSharedDevice = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=84)
PKEY_DeviceDisplay_IsNetworkDevice = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=85)
PKEY_DeviceDisplay_IsDefaultDevice = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=86)
PKEY_DeviceDisplay_MetadataCabinet = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=87)
PKEY_DeviceDisplay_RequiresPairingElevation = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=88)
PKEY_DeviceDisplay_ExperienceId = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=89)
PKEY_DeviceDisplay_Category = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=90)
PKEY_DeviceDisplay_Category_Desc_Singular = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=91)
PKEY_DeviceDisplay_Category_Desc_Plural = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=92)
PKEY_DeviceDisplay_Category_Icon = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=93)
PKEY_DeviceDisplay_CategoryGroup_Desc = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=94)
PKEY_DeviceDisplay_CategoryGroup_Icon = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=95)
PKEY_DeviceDisplay_PrimaryCategory = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=97)
PKEY_DeviceDisplay_UnpairUninstall = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=98)
PKEY_DeviceDisplay_RequiresUninstallElevation = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=99)
PKEY_DeviceDisplay_DeviceFunctionSubRank = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=100)
PKEY_DeviceDisplay_AlwaysShowDeviceAsConnected = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=101)
PKEY_DeviceDisplay_FriendlyName = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12288)
PKEY_DeviceDisplay_Manufacturer = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8192)
PKEY_DeviceDisplay_ModelName = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8194)
PKEY_DeviceDisplay_ModelNumber = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8195)
PKEY_DeviceDisplay_InstallInProgress = PROPERTYKEY(Fmtid='83da6326-97a6-4088-9453-a1923f573b29', Pid=9)
FMTID_Pairing = '8807cae6-7db6-4f10-8ee4-435eaa1392bc'
PKEY_Pairing_ListItemText = PROPERTYKEY(Fmtid='8807cae6-7db6-4f10-8ee4-435eaa1392bc', Pid=1)
PKEY_Pairing_ListItemDescription = PROPERTYKEY(Fmtid='8807cae6-7db6-4f10-8ee4-435eaa1392bc', Pid=2)
PKEY_Pairing_ListItemIcon = PROPERTYKEY(Fmtid='8807cae6-7db6-4f10-8ee4-435eaa1392bc', Pid=3)
PKEY_Pairing_ListItemDefault = PROPERTYKEY(Fmtid='8807cae6-7db6-4f10-8ee4-435eaa1392bc', Pid=4)
PKEY_Pairing_IsWifiOnlyDevice = PROPERTYKEY(Fmtid='8807cae6-7db6-4f10-8ee4-435eaa1392bc', Pid=16)
PKEY_Device_BIOSVersion = PROPERTYKEY(Fmtid='eaee7f1d-6a33-44d1-9441-5f46def23198', Pid=9)
FMTID_WSD = '92506491-ff95-4724-a05a-5b81885a7c92'
FMTID_PNPX = '656a3bb3-ecc0-43fd-8477-4ae0404a96cd'
PKEY_PNPX_GlobalIdentity = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=4096)
PKEY_PNPX_Types = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=4097)
PKEY_PNPX_Scopes = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=4098)
PKEY_PNPX_XAddrs = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=4099)
PKEY_PNPX_MetadataVersion = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=4100)
PKEY_PNPX_ID = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=4101)
PKEY_PNPX_RemoteAddress = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=4102)
PKEY_PNPX_RootProxy = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=4103)
PKEY_PNPX_ManufacturerUrl = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8193)
PKEY_PNPX_ModelUrl = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8196)
PKEY_PNPX_Upc = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8197)
PKEY_PNPX_PresentationUrl = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8198)
PKEY_PNPX_FirmwareVersion = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12289)
PKEY_PNPX_SerialNumber = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12290)
PKEY_PNPX_DeviceCategory = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12292)
PKEY_PNPX_SecureChannel = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=28673)
PKEY_PNPX_CompactSignature = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=28674)
PKEY_PNPX_DeviceCertHash = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=28675)
PKEY_PNPX_DeviceCategory_Desc = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12293)
PKEY_PNPX_Category_Desc_NonPlural = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12304)
PKEY_PNPX_PhysicalAddress = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12294)
PKEY_PNPX_NetworkInterfaceLuid = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12295)
PKEY_PNPX_NetworkInterfaceGuid = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12296)
PKEY_PNPX_IpAddress = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12297)
PKEY_PNPX_ServiceAddress = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=16384)
PKEY_PNPX_ServiceId = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=16385)
PKEY_PNPX_ServiceTypes = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=16386)
PKEY_PNPX_ServiceControlUrl = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=16388)
PKEY_PNPX_ServiceDescUrl = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=16389)
PKEY_PNPX_ServiceEventSubUrl = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=16390)
PKEY_PNPX_DomainName = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=20480)
PKEY_PNPX_ShareName = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=20482)
PKEY_SSDP_AltLocationInfo = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=24576)
PKEY_SSDP_DevLifeTime = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=24577)
PKEY_SSDP_NetworkInterface = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=24578)
FMTID_PNPXDynamicProperty = '4fc5077e-b686-44be-93e3-86cafe368ccd'
PKEY_PNPX_Installable = PROPERTYKEY(Fmtid='4fc5077e-b686-44be-93e3-86cafe368ccd', Pid=1)
PKEY_PNPX_Associated = PROPERTYKEY(Fmtid='4fc5077e-b686-44be-93e3-86cafe368ccd', Pid=2)
PKEY_PNPX_CompatibleTypes = PROPERTYKEY(Fmtid='4fc5077e-b686-44be-93e3-86cafe368ccd', Pid=3)
PKEY_PNPX_InstallState = PROPERTYKEY(Fmtid='4fc5077e-b686-44be-93e3-86cafe368ccd', Pid=4)
PNPX_INSTALLSTATE_NOTINSTALLED = 0
PNPX_INSTALLSTATE_INSTALLED = 1
PNPX_INSTALLSTATE_INSTALLING = 2
PNPX_INSTALLSTATE_FAILED = 3
PKEY_PNPX_Removable = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=28672)
PKEY_PNPX_IPBusEnumerated = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=28688)
PKEY_WNET_Scope = PROPERTYKEY(Fmtid='debda43a-37b3-4383-91e7-4498da2995ab', Pid=1)
PKEY_WNET_Type = PROPERTYKEY(Fmtid='debda43a-37b3-4383-91e7-4498da2995ab', Pid=2)
PKEY_WNET_DisplayType = PROPERTYKEY(Fmtid='debda43a-37b3-4383-91e7-4498da2995ab', Pid=3)
PKEY_WNET_Usage = PROPERTYKEY(Fmtid='debda43a-37b3-4383-91e7-4498da2995ab', Pid=4)
PKEY_WNET_LocalName = PROPERTYKEY(Fmtid='debda43a-37b3-4383-91e7-4498da2995ab', Pid=5)
PKEY_WNET_RemoteName = PROPERTYKEY(Fmtid='debda43a-37b3-4383-91e7-4498da2995ab', Pid=6)
PKEY_WNET_Comment = PROPERTYKEY(Fmtid='debda43a-37b3-4383-91e7-4498da2995ab', Pid=7)
PKEY_WNET_Provider = PROPERTYKEY(Fmtid='debda43a-37b3-4383-91e7-4498da2995ab', Pid=8)
PKEY_WCN_Version = PROPERTYKEY(Fmtid='88190b80-4684-11da-a26a-0002b3988e81', Pid=1)
PKEY_WCN_RequestType = PROPERTYKEY(Fmtid='88190b81-4684-11da-a26a-0002b3988e81', Pid=2)
PKEY_WCN_AuthType = PROPERTYKEY(Fmtid='88190b82-4684-11da-a26a-0002b3988e81', Pid=3)
PKEY_WCN_EncryptType = PROPERTYKEY(Fmtid='88190b83-4684-11da-a26a-0002b3988e81', Pid=4)
PKEY_WCN_ConnType = PROPERTYKEY(Fmtid='88190b84-4684-11da-a26a-0002b3988e81', Pid=5)
PKEY_WCN_ConfigMethods = PROPERTYKEY(Fmtid='88190b85-4684-11da-a26a-0002b3988e81', Pid=6)
PKEY_WCN_RfBand = PROPERTYKEY(Fmtid='88190b87-4684-11da-a26a-0002b3988e81', Pid=8)
PKEY_WCN_AssocState = PROPERTYKEY(Fmtid='88190b88-4684-11da-a26a-0002b3988e81', Pid=9)
PKEY_WCN_ConfigError = PROPERTYKEY(Fmtid='88190b89-4684-11da-a26a-0002b3988e81', Pid=10)
PKEY_WCN_ConfigState = PROPERTYKEY(Fmtid='88190b89-4684-11da-a26a-0002b3988e81', Pid=11)
PKEY_WCN_DevicePasswordId = PROPERTYKEY(Fmtid='88190b89-4684-11da-a26a-0002b3988e81', Pid=12)
PKEY_WCN_OSVersion = PROPERTYKEY(Fmtid='88190b89-4684-11da-a26a-0002b3988e81', Pid=13)
PKEY_WCN_VendorExtension = PROPERTYKEY(Fmtid='88190b8a-4684-11da-a26a-0002b3988e81', Pid=14)
PKEY_WCN_RegistrarType = PROPERTYKEY(Fmtid='88190b8b-4684-11da-a26a-0002b3988e81', Pid=15)
PKEY_Hardware_Devinst = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=4097)
PKEY_Hardware_DisplayAttribute = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=5)
PKEY_Hardware_DriverDate = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=11)
PKEY_Hardware_DriverProvider = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=10)
PKEY_Hardware_DriverVersion = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=9)
PKEY_Hardware_Function = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=4099)
PKEY_Hardware_Icon = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=3)
PKEY_Hardware_Image = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=4098)
PKEY_Hardware_Manufacturer = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=6)
PKEY_Hardware_Model = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=7)
PKEY_Hardware_Name = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=2)
PKEY_Hardware_SerialNumber = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=8)
PKEY_Hardware_ShellAttributes = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=4100)
PKEY_Hardware_Status = PROPERTYKEY(Fmtid='5eaf3ef2-e0ca-4598-bf06-71ed1d9dd953', Pid=4096)
PKEY_NAME = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=10)
PKEY_Device_DeviceDesc = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=2)
PKEY_Device_HardwareIds = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=3)
PKEY_Device_CompatibleIds = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=4)
PKEY_Device_Service = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=6)
PKEY_Device_Class = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=9)
PKEY_Device_ClassGuid = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=10)
PKEY_Device_Driver = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=11)
PKEY_Device_ConfigFlags = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=12)
PKEY_Device_Manufacturer = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=13)
PKEY_Device_FriendlyName = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=14)
PKEY_Device_LocationInfo = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=15)
PKEY_Device_PDOName = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=16)
PKEY_Device_Capabilities = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=17)
PKEY_Device_UINumber = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=18)
PKEY_Device_UpperFilters = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=19)
PKEY_Device_LowerFilters = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=20)
PKEY_Device_BusTypeGuid = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=21)
PKEY_Device_LegacyBusType = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=22)
PKEY_Device_BusNumber = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=23)
PKEY_Device_EnumeratorName = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=24)
PKEY_Device_Security = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=25)
PKEY_Device_SecuritySDS = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=26)
PKEY_Device_DevType = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=27)
PKEY_Device_Exclusive = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=28)
PKEY_Device_Characteristics = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=29)
PKEY_Device_Address = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=30)
PKEY_Device_UINumberDescFormat = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=31)
PKEY_Device_PowerData = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=32)
PKEY_Device_RemovalPolicy = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=33)
PKEY_Device_RemovalPolicyDefault = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=34)
PKEY_Device_RemovalPolicyOverride = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=35)
PKEY_Device_InstallState = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=36)
PKEY_Device_LocationPaths = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=37)
PKEY_Device_BaseContainerId = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=38)
PKEY_Device_DevNodeStatus = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=2)
PKEY_Device_ProblemCode = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=3)
PKEY_Device_EjectionRelations = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=4)
PKEY_Device_RemovalRelations = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=5)
PKEY_Device_PowerRelations = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=6)
PKEY_Device_BusRelations = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=7)
PKEY_Device_Parent = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=8)
PKEY_Device_Children = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=9)
PKEY_Device_Siblings = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=10)
PKEY_Device_TransportRelations = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=11)
PKEY_Device_Reported = PROPERTYKEY(Fmtid='80497100-8c73-48b9-aad9-ce387e19c56e', Pid=2)
PKEY_Device_Legacy = PROPERTYKEY(Fmtid='80497100-8c73-48b9-aad9-ce387e19c56e', Pid=3)
PKEY_Device_InstanceId = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=256)
PKEY_Device_ContainerId = PROPERTYKEY(Fmtid='8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c', Pid=2)
PKEY_Device_ModelId = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=2)
PKEY_Device_FriendlyNameAttributes = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=3)
PKEY_Device_ManufacturerAttributes = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=4)
PKEY_Device_PresenceNotForDevice = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=5)
PKEY_Device_SignalStrength = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=6)
PKEY_Device_IsAssociateableByUserAction = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=7)
PKEY_Numa_Proximity_Domain = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=1)
PKEY_Device_DHP_Rebalance_Policy = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=2)
PKEY_Device_Numa_Node = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=3)
PKEY_Device_BusReportedDeviceDesc = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=4)
PKEY_Device_InstallInProgress = PROPERTYKEY(Fmtid='83da6326-97a6-4088-9453-a1923f573b29', Pid=9)
PKEY_Device_DriverDate = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=2)
PKEY_Device_DriverVersion = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=3)
PKEY_Device_DriverDesc = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=4)
PKEY_Device_DriverInfPath = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=5)
PKEY_Device_DriverInfSection = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=6)
PKEY_Device_DriverInfSectionExt = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=7)
PKEY_Device_MatchingDeviceId = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=8)
PKEY_Device_DriverProvider = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=9)
PKEY_Device_DriverPropPageProvider = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=10)
PKEY_Device_DriverCoInstallers = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=11)
PKEY_Device_ResourcePickerTags = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=12)
PKEY_Device_ResourcePickerExceptions = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=13)
PKEY_Device_DriverRank = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=14)
PKEY_Device_DriverLogoLevel = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=15)
PKEY_Device_NoConnectSound = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=17)
PKEY_Device_GenericDriverInstalled = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=18)
PKEY_Device_AdditionalSoftwareRequested = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=19)
PKEY_Device_SafeRemovalRequired = PROPERTYKEY(Fmtid='afd97640-86a3-4210-b67c-289c41aabe55', Pid=2)
PKEY_Device_SafeRemovalRequiredOverride = PROPERTYKEY(Fmtid='afd97640-86a3-4210-b67c-289c41aabe55', Pid=3)
PKEY_DrvPkg_Model = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=2)
PKEY_DrvPkg_VendorWebSite = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=3)
PKEY_DrvPkg_DetailedDescription = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=4)
PKEY_DrvPkg_DocumentationLink = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=5)
PKEY_DrvPkg_Icon = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=6)
PKEY_DrvPkg_BrandingIcon = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=7)
PKEY_DeviceClass_UpperFilters = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=19)
PKEY_DeviceClass_LowerFilters = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=20)
PKEY_DeviceClass_Security = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=25)
PKEY_DeviceClass_SecuritySDS = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=26)
PKEY_DeviceClass_DevType = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=27)
PKEY_DeviceClass_Exclusive = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=28)
PKEY_DeviceClass_Characteristics = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=29)
PKEY_DeviceClass_Name = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=2)
PKEY_DeviceClass_ClassName = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=3)
PKEY_DeviceClass_Icon = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=4)
PKEY_DeviceClass_ClassInstaller = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=5)
PKEY_DeviceClass_PropPageProvider = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=6)
PKEY_DeviceClass_NoInstallClass = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=7)
PKEY_DeviceClass_NoDisplayClass = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=8)
PKEY_DeviceClass_SilentInstall = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=9)
PKEY_DeviceClass_NoUseClass = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=10)
PKEY_DeviceClass_DefaultService = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=11)
PKEY_DeviceClass_IconPath = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=12)
PKEY_DeviceClass_ClassCoInstallers = PROPERTYKEY(Fmtid='713d1703-a2e2-49f5-9214-56472ef3da5c', Pid=2)
PKEY_DeviceInterface_FriendlyName = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=2)
PKEY_DeviceInterface_Enabled = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=3)
PKEY_DeviceInterface_ClassGuid = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=4)
PKEY_DeviceInterfaceClass_DefaultInterface = PROPERTYKEY(Fmtid='14c83a99-0b3f-44b7-be4c-a178d3990564', Pid=2)
FD_LONGHORN = 1
MAX_FDCONSTRAINTNAME_LENGTH = 100
MAX_FDCONSTRAINTVALUE_LENGTH = 1000
E_FDPAIRING_NOCONNECTION = -1882193919
E_FDPAIRING_HWFAILURE = -1882193918
E_FDPAIRING_AUTHFAILURE = -1882193917
E_FDPAIRING_CONNECTTIMEOUT = -1882193916
E_FDPAIRING_TOOMANYCONNECTIONS = -1882193915
E_FDPAIRING_AUTHNOTALLOWED = -1882193914
E_FDPAIRING_IPBUSDISABLED = -1882193913
E_FDPAIRING_NOPROFILES = -1882193912
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
SystemVisibilityFlags = Int32
SVF_SYSTEM = 0
SVF_USER = 1
QueryUpdateAction = Int32
QUA_ADD = 0
QUA_REMOVE = 1
QUA_CHANGE = 2
QueryCategoryType = Int32
QCT_PROVIDER = 0
QCT_LAYERED = 1
def _define_IFunctionDiscoveryNotification_head():
    class IFunctionDiscoveryNotification(win32more.System.Com.IUnknown_head):
        Guid = Guid('5f6c1ba8-5330-422e-a368-572b244d3f87')
    return IFunctionDiscoveryNotification
def _define_IFunctionDiscoveryNotification():
    IFunctionDiscoveryNotification = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head
    IFunctionDiscoveryNotification.OnUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.QueryUpdateAction,UInt64,win32more.Devices.FunctionDiscovery.IFunctionInstance_head, use_last_error=False)(3, 'OnUpdate', ((1, 'enumQueryUpdateAction'),(1, 'fdqcQueryContext'),(1, 'pIFunctionInstance'),)))
    IFunctionDiscoveryNotification.OnError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt64,win32more.Foundation.PWSTR, use_last_error=False)(4, 'OnError', ((1, 'hr'),(1, 'fdqcQueryContext'),(1, 'pszProvider'),)))
    IFunctionDiscoveryNotification.OnEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt64,win32more.Foundation.PWSTR, use_last_error=False)(5, 'OnEvent', ((1, 'dwEventID'),(1, 'fdqcQueryContext'),(1, 'pszProvider'),)))
    return IFunctionDiscoveryNotification
def _define_IFunctionDiscovery_head():
    class IFunctionDiscovery(win32more.System.Com.IUnknown_head):
        Guid = Guid('4df99b70-e148-4432-b004-4c9eeb535a5e')
    return IFunctionDiscovery
def _define_IFunctionDiscovery():
    IFunctionDiscovery = win32more.Devices.FunctionDiscovery.IFunctionDiscovery_head
    IFunctionDiscovery.GetInstanceCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head), use_last_error=False)(3, 'GetInstanceCollection', ((1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'fIncludeAllSubCategories'),(1, 'ppIFunctionInstanceCollection'),)))
    IFunctionDiscovery.GetInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(4, 'GetInstance', ((1, 'pszFunctionInstanceIdentity'),(1, 'ppIFunctionInstance'),)))
    IFunctionDiscovery.CreateInstanceCollectionQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head,POINTER(UInt64),POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollectionQuery_head), use_last_error=False)(5, 'CreateInstanceCollectionQuery', ((1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'fIncludeAllSubCategories'),(1, 'pIFunctionDiscoveryNotification'),(1, 'pfdqcQueryContext'),(1, 'ppIFunctionInstanceCollectionQuery'),)))
    IFunctionDiscovery.CreateInstanceQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head,POINTER(UInt64),POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceQuery_head), use_last_error=False)(6, 'CreateInstanceQuery', ((1, 'pszFunctionInstanceIdentity'),(1, 'pIFunctionDiscoveryNotification'),(1, 'pfdqcQueryContext'),(1, 'ppIFunctionInstanceQuery'),)))
    IFunctionDiscovery.AddInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(7, 'AddInstance', ((1, 'enumSystemVisibility'),(1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'pszCategoryIdentity'),(1, 'ppIFunctionInstance'),)))
    IFunctionDiscovery.RemoveInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(8, 'RemoveInstance', ((1, 'enumSystemVisibility'),(1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'pszCategoryIdentity'),)))
    return IFunctionDiscovery
def _define_IFunctionInstance_head():
    class IFunctionInstance(win32more.System.Com.IServiceProvider_head):
        Guid = Guid('33591c10-0bed-4f02-b0ab-1530d5533ee9')
    return IFunctionInstance
def _define_IFunctionInstance():
    IFunctionInstance = win32more.Devices.FunctionDiscovery.IFunctionInstance_head
    IFunctionInstance.GetID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(4, 'GetID', ((1, 'ppszCoMemIdentity'),)))
    IFunctionInstance.GetProviderInstanceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(5, 'GetProviderInstanceID', ((1, 'ppszCoMemProviderInstanceIdentity'),)))
    IFunctionInstance.OpenPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(6, 'OpenPropertyStore', ((1, 'dwStgAccess'),(1, 'ppIPropertyStore'),)))
    IFunctionInstance.GetCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)), use_last_error=False)(7, 'GetCategory', ((1, 'ppszCoMemCategory'),(1, 'ppszCoMemSubCategory'),)))
    return IFunctionInstance
def _define_IFunctionInstanceCollection_head():
    class IFunctionInstanceCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('f0a3d895-855c-42a2-948d-2f97d450ecb1')
    return IFunctionInstanceCollection
def _define_IFunctionInstanceCollection():
    IFunctionInstanceCollection = win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head
    IFunctionInstanceCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pdwCount'),)))
    IFunctionInstanceCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(4, 'Get', ((1, 'pszInstanceIdentity'),(1, 'pdwIndex'),(1, 'ppIFunctionInstance'),)))
    IFunctionInstanceCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(5, 'Item', ((1, 'dwIndex'),(1, 'ppIFunctionInstance'),)))
    IFunctionInstanceCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head, use_last_error=False)(6, 'Add', ((1, 'pIFunctionInstance'),)))
    IFunctionInstanceCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(7, 'Remove', ((1, 'dwIndex'),(1, 'ppIFunctionInstance'),)))
    IFunctionInstanceCollection.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'Delete', ((1, 'dwIndex'),)))
    IFunctionInstanceCollection.DeleteAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'DeleteAll', ()))
    return IFunctionInstanceCollection
def _define_IPropertyStoreCollection_head():
    class IPropertyStoreCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('d14d9c30-12d2-42d8-bce4-c60c2bb226fa')
    return IPropertyStoreCollection
def _define_IPropertyStoreCollection():
    IPropertyStoreCollection = win32more.Devices.FunctionDiscovery.IPropertyStoreCollection_head
    IPropertyStoreCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pdwCount'),)))
    IPropertyStoreCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(4, 'Get', ((1, 'pszInstanceIdentity'),(1, 'pdwIndex'),(1, 'ppIPropertyStore'),)))
    IPropertyStoreCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(5, 'Item', ((1, 'dwIndex'),(1, 'ppIPropertyStore'),)))
    IPropertyStoreCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, use_last_error=False)(6, 'Add', ((1, 'pIPropertyStore'),)))
    IPropertyStoreCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(7, 'Remove', ((1, 'dwIndex'),(1, 'pIPropertyStore'),)))
    IPropertyStoreCollection.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'Delete', ((1, 'dwIndex'),)))
    IPropertyStoreCollection.DeleteAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'DeleteAll', ()))
    return IPropertyStoreCollection
def _define_IFunctionInstanceQuery_head():
    class IFunctionInstanceQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('6242bc6b-90ec-4b37-bb46-e229fd84ed95')
    return IFunctionInstanceQuery
def _define_IFunctionInstanceQuery():
    IFunctionInstanceQuery = win32more.Devices.FunctionDiscovery.IFunctionInstanceQuery_head
    IFunctionInstanceQuery.Execute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(3, 'Execute', ((1, 'ppIFunctionInstance'),)))
    return IFunctionInstanceQuery
def _define_IFunctionInstanceCollectionQuery_head():
    class IFunctionInstanceCollectionQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('57cc6fd2-c09a-4289-bb72-25f04142058e')
    return IFunctionInstanceCollectionQuery
def _define_IFunctionInstanceCollectionQuery():
    IFunctionInstanceCollectionQuery = win32more.Devices.FunctionDiscovery.IFunctionInstanceCollectionQuery_head
    IFunctionInstanceCollectionQuery.AddQueryConstraint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'AddQueryConstraint', ((1, 'pszConstraintName'),(1, 'pszConstraintValue'),)))
    IFunctionInstanceCollectionQuery.AddPropertyConstraint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.Devices.FunctionDiscovery.PropertyConstraint, use_last_error=False)(4, 'AddPropertyConstraint', ((1, 'Key'),(1, 'pv'),(1, 'enumPropertyConstraint'),)))
    IFunctionInstanceCollectionQuery.Execute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head), use_last_error=False)(5, 'Execute', ((1, 'ppIFunctionInstanceCollection'),)))
    return IFunctionInstanceCollectionQuery
def _define_IFunctionDiscoveryProvider_head():
    class IFunctionDiscoveryProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcde394f-1478-4813-a402-f6fb10657222')
    return IFunctionDiscoveryProvider
def _define_IFunctionDiscoveryProvider():
    IFunctionDiscoveryProvider = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProvider_head
    IFunctionDiscoveryProvider.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderFactory_head,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head,UInt32,POINTER(UInt32), use_last_error=False)(3, 'Initialize', ((1, 'pIFunctionDiscoveryProviderFactory'),(1, 'pIFunctionDiscoveryNotification'),(1, 'lcidUserDefault'),(1, 'pdwStgAccessCapabilities'),)))
    IFunctionDiscoveryProvider.Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderQuery_head,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head), use_last_error=False)(4, 'Query', ((1, 'pIFunctionDiscoveryProviderQuery'),(1, 'ppIFunctionInstanceCollection'),)))
    IFunctionDiscoveryProvider.EndQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'EndQuery', ()))
    IFunctionDiscoveryProvider.InstancePropertyStoreValidateAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,UInt32, use_last_error=False)(6, 'InstancePropertyStoreValidateAccess', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'dwStgAccess'),)))
    IFunctionDiscoveryProvider.InstancePropertyStoreOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(7, 'InstancePropertyStoreOpen', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'dwStgAccess'),(1, 'ppIPropertyStore'),)))
    IFunctionDiscoveryProvider.InstancePropertyStoreFlush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr, use_last_error=False)(8, 'InstancePropertyStoreFlush', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),)))
    IFunctionDiscoveryProvider.InstanceQueryService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'InstanceQueryService', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'guidService'),(1, 'riid'),(1, 'ppIUnknown'),)))
    IFunctionDiscoveryProvider.InstanceReleased = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr, use_last_error=False)(10, 'InstanceReleased', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),)))
    return IFunctionDiscoveryProvider
def _define_IProviderProperties_head():
    class IProviderProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('cf986ea6-3b5f-4c5f-b88a-2f8b20ceef17')
    return IProviderProperties
def _define_IProviderProperties():
    IProviderProperties = win32more.Devices.FunctionDiscovery.IProviderProperties_head
    IProviderProperties.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'pdwCount'),)))
    IProviderProperties.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(4, 'GetAt', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'dwIndex'),(1, 'pKey'),)))
    IProviderProperties.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(5, 'GetValue', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'Key'),(1, 'ppropVar'),)))
    IProviderProperties.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(6, 'SetValue', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'Key'),(1, 'ppropVar'),)))
    return IProviderProperties
def _define_IProviderPublishing_head():
    class IProviderPublishing(win32more.System.Com.IUnknown_head):
        Guid = Guid('cd1b9a04-206c-4a05-a0c8-1635a21a2b7c')
    return IProviderPublishing
def _define_IProviderPublishing():
    IProviderPublishing = win32more.Devices.FunctionDiscovery.IProviderPublishing_head
    IProviderPublishing.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(3, 'CreateInstance', ((1, 'enumVisibilityFlags'),(1, 'pszSubCategory'),(1, 'pszProviderInstanceIdentity'),(1, 'ppIFunctionInstance'),)))
    IProviderPublishing.RemoveInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(4, 'RemoveInstance', ((1, 'enumVisibilityFlags'),(1, 'pszSubCategory'),(1, 'pszProviderInstanceIdentity'),)))
    return IProviderPublishing
def _define_IFunctionDiscoveryProviderFactory_head():
    class IFunctionDiscoveryProviderFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('86443ff0-1ad5-4e68-a45a-40c2c329de3b')
    return IFunctionDiscoveryProviderFactory
def _define_IFunctionDiscoveryProviderFactory():
    IFunctionDiscoveryProviderFactory = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderFactory_head
    IFunctionDiscoveryProviderFactory.CreatePropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(3, 'CreatePropertyStore', ((1, 'ppIPropertyStore'),)))
    IFunctionDiscoveryProviderFactory.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,IntPtr,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProvider_head,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(4, 'CreateInstance', ((1, 'pszSubCategory'),(1, 'pszProviderInstanceIdentity'),(1, 'iProviderInstanceContext'),(1, 'pIPropertyStore'),(1, 'pIFunctionDiscoveryProvider'),(1, 'ppIFunctionInstance'),)))
    IFunctionDiscoveryProviderFactory.CreateFunctionInstanceCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head), use_last_error=False)(5, 'CreateFunctionInstanceCollection', ((1, 'ppIFunctionInstanceCollection'),)))
    return IFunctionDiscoveryProviderFactory
def _define_IFunctionDiscoveryProviderQuery_head():
    class IFunctionDiscoveryProviderQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('6876ea98-baec-46db-bc20-75a76e267a3a')
    return IFunctionDiscoveryProviderQuery
def _define_IFunctionDiscoveryProviderQuery():
    IFunctionDiscoveryProviderQuery = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderQuery_head
    IFunctionDiscoveryProviderQuery.IsInstanceQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(POINTER(UInt16)), use_last_error=False)(3, 'IsInstanceQuery', ((1, 'pisInstanceQuery'),(1, 'ppszConstraintValue'),)))
    IFunctionDiscoveryProviderQuery.IsSubcategoryQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(POINTER(UInt16)), use_last_error=False)(4, 'IsSubcategoryQuery', ((1, 'pisSubcategoryQuery'),(1, 'ppszConstraintValue'),)))
    IFunctionDiscoveryProviderQuery.GetQueryConstraints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IProviderQueryConstraintCollection_head), use_last_error=False)(5, 'GetQueryConstraints', ((1, 'ppIProviderQueryConstraints'),)))
    IFunctionDiscoveryProviderQuery.GetPropertyConstraints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IProviderPropertyConstraintCollection_head), use_last_error=False)(6, 'GetPropertyConstraints', ((1, 'ppIProviderPropertyConstraints'),)))
    return IFunctionDiscoveryProviderQuery
def _define_IProviderQueryConstraintCollection_head():
    class IProviderQueryConstraintCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('9c243e11-3261-4bcd-b922-84a873d460ae')
    return IProviderQueryConstraintCollection
def _define_IProviderQueryConstraintCollection():
    IProviderQueryConstraintCollection = win32more.Devices.FunctionDiscovery.IProviderQueryConstraintCollection_head
    IProviderQueryConstraintCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pdwCount'),)))
    IProviderQueryConstraintCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)), use_last_error=False)(4, 'Get', ((1, 'pszConstraintName'),(1, 'ppszConstraintValue'),)))
    IProviderQueryConstraintCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)), use_last_error=False)(5, 'Item', ((1, 'dwIndex'),(1, 'ppszConstraintName'),(1, 'ppszConstraintValue'),)))
    IProviderQueryConstraintCollection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)), use_last_error=False)(6, 'Next', ((1, 'ppszConstraintName'),(1, 'ppszConstraintValue'),)))
    IProviderQueryConstraintCollection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Skip', ()))
    IProviderQueryConstraintCollection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Reset', ()))
    return IProviderQueryConstraintCollection
def _define_IProviderPropertyConstraintCollection_head():
    class IProviderPropertyConstraintCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('f4fae42f-5778-4a13-8540-b5fd8c1398dd')
    return IProviderPropertyConstraintCollection
def _define_IProviderPropertyConstraintCollection():
    IProviderPropertyConstraintCollection = win32more.Devices.FunctionDiscovery.IProviderPropertyConstraintCollection_head
    IProviderPropertyConstraintCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pdwCount'),)))
    IProviderPropertyConstraintCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32), use_last_error=False)(4, 'Get', ((1, 'Key'),(1, 'pPropVar'),(1, 'pdwPropertyConstraint'),)))
    IProviderPropertyConstraintCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32), use_last_error=False)(5, 'Item', ((1, 'dwIndex'),(1, 'pKey'),(1, 'pPropVar'),(1, 'pdwPropertyConstraint'),)))
    IProviderPropertyConstraintCollection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32), use_last_error=False)(6, 'Next', ((1, 'pKey'),(1, 'pPropVar'),(1, 'pdwPropertyConstraint'),)))
    IProviderPropertyConstraintCollection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Skip', ()))
    IProviderPropertyConstraintCollection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Reset', ()))
    return IProviderPropertyConstraintCollection
def _define_IFunctionDiscoveryServiceProvider_head():
    class IFunctionDiscoveryServiceProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('4c81ed02-1b04-43f2-a451-69966cbcd1c2')
    return IFunctionDiscoveryServiceProvider
def _define_IFunctionDiscoveryServiceProvider():
    IFunctionDiscoveryServiceProvider = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryServiceProvider_head
    IFunctionDiscoveryServiceProvider.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'Initialize', ((1, 'pIFunctionInstance'),(1, 'riid'),(1, 'ppv'),)))
    return IFunctionDiscoveryServiceProvider
PNPXAssociation = Guid('cee8ccc9-4f6b-4469-a235-5a22869eef03')
PNPXPairingHandler = Guid('b8a27942-ade7-4085-aa6e-4fadc7ada1ef')
def _define_IPNPXAssociation_head():
    class IPNPXAssociation(win32more.System.Com.IUnknown_head):
        Guid = Guid('0bd7e521-4da6-42d5-81ba-1981b6b94075')
    return IPNPXAssociation
def _define_IPNPXAssociation():
    IPNPXAssociation = win32more.Devices.FunctionDiscovery.IPNPXAssociation_head
    IPNPXAssociation.Associate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'Associate', ((1, 'pszSubcategory'),)))
    IPNPXAssociation.Unassociate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'Unassociate', ((1, 'pszSubcategory'),)))
    IPNPXAssociation.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'Delete', ((1, 'pszSubcategory'),)))
    return IPNPXAssociation
def _define_IPNPXDeviceAssociation_head():
    class IPNPXDeviceAssociation(win32more.System.Com.IUnknown_head):
        Guid = Guid('eed366d0-35b8-4fc5-8d20-7e5bd31f6ded')
    return IPNPXDeviceAssociation
def _define_IPNPXDeviceAssociation():
    IPNPXDeviceAssociation = win32more.Devices.FunctionDiscovery.IPNPXDeviceAssociation_head
    IPNPXDeviceAssociation.Associate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head, use_last_error=False)(3, 'Associate', ((1, 'pszSubCategory'),(1, 'pIFunctionDiscoveryNotification'),)))
    IPNPXDeviceAssociation.Unassociate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head, use_last_error=False)(4, 'Unassociate', ((1, 'pszSubCategory'),(1, 'pIFunctionDiscoveryNotification'),)))
    IPNPXDeviceAssociation.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head, use_last_error=False)(5, 'Delete', ((1, 'pszSubcategory'),(1, 'pIFunctionDiscoveryNotification'),)))
    return IPNPXDeviceAssociation
FunctionDiscovery = Guid('c72be2ec-8e90-452c-b29a-ab8ff1c071fc')
PropertyStore = Guid('e4796550-df61-448b-9193-13fc1341b163')
FunctionInstanceCollection = Guid('ba818ce5-b55f-443f-ad39-2fe89be6191f')
PropertyStoreCollection = Guid('edd36029-d753-4862-aa5b-5bccad2a4d29')
__all__ = [
    "FD_EVENTID_PRIVATE",
    "FD_EVENTID",
    "FD_EVENTID_SEARCHCOMPLETE",
    "FD_EVENTID_ASYNCTHREADEXIT",
    "FD_EVENTID_SEARCHSTART",
    "FD_EVENTID_IPADDRESSCHANGE",
    "FD_EVENTID_QUERYREFRESH",
    "SID_PnpProvider",
    "SID_UPnPActivator",
    "SID_EnumInterface",
    "SID_PNPXPropertyStore",
    "SID_PNPXAssociation",
    "SID_PNPXServiceCollection",
    "SID_FDPairingHandler",
    "SID_EnumDeviceFunction",
    "SID_UnpairProvider",
    "SID_DeviceDisplayStatusManager",
    "SID_FunctionDiscoveryProviderRefresh",
    "SID_UninstallDeviceFunction",
    "PKEY_FunctionInstance",
    "FMTID_FD",
    "FD_Visibility_Default",
    "FD_Visibility_Hidden",
    "FMTID_Device",
    "FMTID_DeviceInterface",
    "PKEY_DeviceDisplay_Address",
    "PKEY_DeviceDisplay_DiscoveryMethod",
    "PKEY_DeviceDisplay_IsEncrypted",
    "PKEY_DeviceDisplay_IsAuthenticated",
    "PKEY_DeviceDisplay_IsConnected",
    "PKEY_DeviceDisplay_IsPaired",
    "PKEY_DeviceDisplay_Icon",
    "PKEY_DeviceDisplay_Version",
    "PKEY_DeviceDisplay_Last_Seen",
    "PKEY_DeviceDisplay_Last_Connected",
    "PKEY_DeviceDisplay_IsShowInDisconnectedState",
    "PKEY_DeviceDisplay_IsLocalMachine",
    "PKEY_DeviceDisplay_MetadataPath",
    "PKEY_DeviceDisplay_IsMetadataSearchInProgress",
    "PKEY_DeviceDisplay_MetadataChecksum",
    "PKEY_DeviceDisplay_IsNotInterestingForDisplay",
    "PKEY_DeviceDisplay_LaunchDeviceStageOnDeviceConnect",
    "PKEY_DeviceDisplay_LaunchDeviceStageFromExplorer",
    "PKEY_DeviceDisplay_BaselineExperienceId",
    "PKEY_DeviceDisplay_IsDeviceUniquelyIdentifiable",
    "PKEY_DeviceDisplay_AssociationArray",
    "PKEY_DeviceDisplay_DeviceDescription1",
    "PKEY_DeviceDisplay_DeviceDescription2",
    "PKEY_DeviceDisplay_IsNotWorkingProperly",
    "PKEY_DeviceDisplay_IsSharedDevice",
    "PKEY_DeviceDisplay_IsNetworkDevice",
    "PKEY_DeviceDisplay_IsDefaultDevice",
    "PKEY_DeviceDisplay_MetadataCabinet",
    "PKEY_DeviceDisplay_RequiresPairingElevation",
    "PKEY_DeviceDisplay_ExperienceId",
    "PKEY_DeviceDisplay_Category",
    "PKEY_DeviceDisplay_Category_Desc_Singular",
    "PKEY_DeviceDisplay_Category_Desc_Plural",
    "PKEY_DeviceDisplay_Category_Icon",
    "PKEY_DeviceDisplay_CategoryGroup_Desc",
    "PKEY_DeviceDisplay_CategoryGroup_Icon",
    "PKEY_DeviceDisplay_PrimaryCategory",
    "PKEY_DeviceDisplay_UnpairUninstall",
    "PKEY_DeviceDisplay_RequiresUninstallElevation",
    "PKEY_DeviceDisplay_DeviceFunctionSubRank",
    "PKEY_DeviceDisplay_AlwaysShowDeviceAsConnected",
    "PKEY_DeviceDisplay_FriendlyName",
    "PKEY_DeviceDisplay_Manufacturer",
    "PKEY_DeviceDisplay_ModelName",
    "PKEY_DeviceDisplay_ModelNumber",
    "PKEY_DeviceDisplay_InstallInProgress",
    "FMTID_Pairing",
    "PKEY_Pairing_ListItemText",
    "PKEY_Pairing_ListItemDescription",
    "PKEY_Pairing_ListItemIcon",
    "PKEY_Pairing_ListItemDefault",
    "PKEY_Pairing_IsWifiOnlyDevice",
    "PKEY_Device_BIOSVersion",
    "FMTID_WSD",
    "FMTID_PNPX",
    "PKEY_PNPX_GlobalIdentity",
    "PKEY_PNPX_Types",
    "PKEY_PNPX_Scopes",
    "PKEY_PNPX_XAddrs",
    "PKEY_PNPX_MetadataVersion",
    "PKEY_PNPX_ID",
    "PKEY_PNPX_RemoteAddress",
    "PKEY_PNPX_RootProxy",
    "PKEY_PNPX_ManufacturerUrl",
    "PKEY_PNPX_ModelUrl",
    "PKEY_PNPX_Upc",
    "PKEY_PNPX_PresentationUrl",
    "PKEY_PNPX_FirmwareVersion",
    "PKEY_PNPX_SerialNumber",
    "PKEY_PNPX_DeviceCategory",
    "PKEY_PNPX_SecureChannel",
    "PKEY_PNPX_CompactSignature",
    "PKEY_PNPX_DeviceCertHash",
    "PKEY_PNPX_DeviceCategory_Desc",
    "PKEY_PNPX_Category_Desc_NonPlural",
    "PKEY_PNPX_PhysicalAddress",
    "PKEY_PNPX_NetworkInterfaceLuid",
    "PKEY_PNPX_NetworkInterfaceGuid",
    "PKEY_PNPX_IpAddress",
    "PKEY_PNPX_ServiceAddress",
    "PKEY_PNPX_ServiceId",
    "PKEY_PNPX_ServiceTypes",
    "PKEY_PNPX_ServiceControlUrl",
    "PKEY_PNPX_ServiceDescUrl",
    "PKEY_PNPX_ServiceEventSubUrl",
    "PKEY_PNPX_DomainName",
    "PKEY_PNPX_ShareName",
    "PKEY_SSDP_AltLocationInfo",
    "PKEY_SSDP_DevLifeTime",
    "PKEY_SSDP_NetworkInterface",
    "FMTID_PNPXDynamicProperty",
    "PKEY_PNPX_Installable",
    "PKEY_PNPX_Associated",
    "PKEY_PNPX_CompatibleTypes",
    "PKEY_PNPX_InstallState",
    "PNPX_INSTALLSTATE_NOTINSTALLED",
    "PNPX_INSTALLSTATE_INSTALLED",
    "PNPX_INSTALLSTATE_INSTALLING",
    "PNPX_INSTALLSTATE_FAILED",
    "PKEY_PNPX_Removable",
    "PKEY_PNPX_IPBusEnumerated",
    "PKEY_WNET_Scope",
    "PKEY_WNET_Type",
    "PKEY_WNET_DisplayType",
    "PKEY_WNET_Usage",
    "PKEY_WNET_LocalName",
    "PKEY_WNET_RemoteName",
    "PKEY_WNET_Comment",
    "PKEY_WNET_Provider",
    "PKEY_WCN_Version",
    "PKEY_WCN_RequestType",
    "PKEY_WCN_AuthType",
    "PKEY_WCN_EncryptType",
    "PKEY_WCN_ConnType",
    "PKEY_WCN_ConfigMethods",
    "PKEY_WCN_RfBand",
    "PKEY_WCN_AssocState",
    "PKEY_WCN_ConfigError",
    "PKEY_WCN_ConfigState",
    "PKEY_WCN_DevicePasswordId",
    "PKEY_WCN_OSVersion",
    "PKEY_WCN_VendorExtension",
    "PKEY_WCN_RegistrarType",
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
    "PKEY_Device_DeviceDesc",
    "PKEY_Device_HardwareIds",
    "PKEY_Device_CompatibleIds",
    "PKEY_Device_Service",
    "PKEY_Device_Class",
    "PKEY_Device_ClassGuid",
    "PKEY_Device_Driver",
    "PKEY_Device_ConfigFlags",
    "PKEY_Device_Manufacturer",
    "PKEY_Device_FriendlyName",
    "PKEY_Device_LocationInfo",
    "PKEY_Device_PDOName",
    "PKEY_Device_Capabilities",
    "PKEY_Device_UINumber",
    "PKEY_Device_UpperFilters",
    "PKEY_Device_LowerFilters",
    "PKEY_Device_BusTypeGuid",
    "PKEY_Device_LegacyBusType",
    "PKEY_Device_BusNumber",
    "PKEY_Device_EnumeratorName",
    "PKEY_Device_Security",
    "PKEY_Device_SecuritySDS",
    "PKEY_Device_DevType",
    "PKEY_Device_Exclusive",
    "PKEY_Device_Characteristics",
    "PKEY_Device_Address",
    "PKEY_Device_UINumberDescFormat",
    "PKEY_Device_PowerData",
    "PKEY_Device_RemovalPolicy",
    "PKEY_Device_RemovalPolicyDefault",
    "PKEY_Device_RemovalPolicyOverride",
    "PKEY_Device_InstallState",
    "PKEY_Device_LocationPaths",
    "PKEY_Device_BaseContainerId",
    "PKEY_Device_DevNodeStatus",
    "PKEY_Device_ProblemCode",
    "PKEY_Device_EjectionRelations",
    "PKEY_Device_RemovalRelations",
    "PKEY_Device_PowerRelations",
    "PKEY_Device_BusRelations",
    "PKEY_Device_Parent",
    "PKEY_Device_Children",
    "PKEY_Device_Siblings",
    "PKEY_Device_TransportRelations",
    "PKEY_Device_Reported",
    "PKEY_Device_Legacy",
    "PKEY_Device_InstanceId",
    "PKEY_Device_ContainerId",
    "PKEY_Device_ModelId",
    "PKEY_Device_FriendlyNameAttributes",
    "PKEY_Device_ManufacturerAttributes",
    "PKEY_Device_PresenceNotForDevice",
    "PKEY_Device_SignalStrength",
    "PKEY_Device_IsAssociateableByUserAction",
    "PKEY_Numa_Proximity_Domain",
    "PKEY_Device_DHP_Rebalance_Policy",
    "PKEY_Device_Numa_Node",
    "PKEY_Device_BusReportedDeviceDesc",
    "PKEY_Device_InstallInProgress",
    "PKEY_Device_DriverDate",
    "PKEY_Device_DriverVersion",
    "PKEY_Device_DriverDesc",
    "PKEY_Device_DriverInfPath",
    "PKEY_Device_DriverInfSection",
    "PKEY_Device_DriverInfSectionExt",
    "PKEY_Device_MatchingDeviceId",
    "PKEY_Device_DriverProvider",
    "PKEY_Device_DriverPropPageProvider",
    "PKEY_Device_DriverCoInstallers",
    "PKEY_Device_ResourcePickerTags",
    "PKEY_Device_ResourcePickerExceptions",
    "PKEY_Device_DriverRank",
    "PKEY_Device_DriverLogoLevel",
    "PKEY_Device_NoConnectSound",
    "PKEY_Device_GenericDriverInstalled",
    "PKEY_Device_AdditionalSoftwareRequested",
    "PKEY_Device_SafeRemovalRequired",
    "PKEY_Device_SafeRemovalRequiredOverride",
    "PKEY_DrvPkg_Model",
    "PKEY_DrvPkg_VendorWebSite",
    "PKEY_DrvPkg_DetailedDescription",
    "PKEY_DrvPkg_DocumentationLink",
    "PKEY_DrvPkg_Icon",
    "PKEY_DrvPkg_BrandingIcon",
    "PKEY_DeviceClass_UpperFilters",
    "PKEY_DeviceClass_LowerFilters",
    "PKEY_DeviceClass_Security",
    "PKEY_DeviceClass_SecuritySDS",
    "PKEY_DeviceClass_DevType",
    "PKEY_DeviceClass_Exclusive",
    "PKEY_DeviceClass_Characteristics",
    "PKEY_DeviceClass_Name",
    "PKEY_DeviceClass_ClassName",
    "PKEY_DeviceClass_Icon",
    "PKEY_DeviceClass_ClassInstaller",
    "PKEY_DeviceClass_PropPageProvider",
    "PKEY_DeviceClass_NoInstallClass",
    "PKEY_DeviceClass_NoDisplayClass",
    "PKEY_DeviceClass_SilentInstall",
    "PKEY_DeviceClass_NoUseClass",
    "PKEY_DeviceClass_DefaultService",
    "PKEY_DeviceClass_IconPath",
    "PKEY_DeviceClass_ClassCoInstallers",
    "PKEY_DeviceInterface_FriendlyName",
    "PKEY_DeviceInterface_Enabled",
    "PKEY_DeviceInterface_ClassGuid",
    "PKEY_DeviceInterfaceClass_DefaultInterface",
    "FD_LONGHORN",
    "MAX_FDCONSTRAINTNAME_LENGTH",
    "MAX_FDCONSTRAINTVALUE_LENGTH",
    "E_FDPAIRING_NOCONNECTION",
    "E_FDPAIRING_HWFAILURE",
    "E_FDPAIRING_AUTHFAILURE",
    "E_FDPAIRING_CONNECTTIMEOUT",
    "E_FDPAIRING_TOOMANYCONNECTIONS",
    "E_FDPAIRING_AUTHNOTALLOWED",
    "E_FDPAIRING_IPBUSDISABLED",
    "E_FDPAIRING_NOPROFILES",
    "PropertyConstraint",
    "QC_EQUALS",
    "QC_NOTEQUAL",
    "QC_LESSTHAN",
    "QC_LESSTHANOREQUAL",
    "QC_GREATERTHAN",
    "QC_GREATERTHANOREQUAL",
    "QC_STARTSWITH",
    "QC_EXISTS",
    "QC_DOESNOTEXIST",
    "QC_CONTAINS",
    "SystemVisibilityFlags",
    "SVF_SYSTEM",
    "SVF_USER",
    "QueryUpdateAction",
    "QUA_ADD",
    "QUA_REMOVE",
    "QUA_CHANGE",
    "QueryCategoryType",
    "QCT_PROVIDER",
    "QCT_LAYERED",
    "IFunctionDiscoveryNotification",
    "IFunctionDiscovery",
    "IFunctionInstance",
    "IFunctionInstanceCollection",
    "IPropertyStoreCollection",
    "IFunctionInstanceQuery",
    "IFunctionInstanceCollectionQuery",
    "IFunctionDiscoveryProvider",
    "IProviderProperties",
    "IProviderPublishing",
    "IFunctionDiscoveryProviderFactory",
    "IFunctionDiscoveryProviderQuery",
    "IProviderQueryConstraintCollection",
    "IProviderPropertyConstraintCollection",
    "IFunctionDiscoveryServiceProvider",
    "PNPXAssociation",
    "PNPXPairingHandler",
    "IPNPXAssociation",
    "IPNPXDeviceAssociation",
    "FunctionDiscovery",
    "PropertyStore",
    "FunctionInstanceCollection",
    "PropertyStoreCollection",
]
