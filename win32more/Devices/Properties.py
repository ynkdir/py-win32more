from win32more import *
import win32more.Devices.Properties
import win32more.Foundation
import win32more.UI.Shell.PropertiesSystem

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Devices.Properties, name, eval(f"_define_{name}()"))
    return getattr(win32more.Devices.Properties, name)
DEVPKEY_DeviceInterface_Autoplay_Silent = PROPERTYKEY(Fmtid='434dd28f-9e75-450a-9ab9-ff61e618bad0', Pid=2)
DEVPKEY_NAME = PROPERTYKEY(Fmtid='b725f130-47ef-101a-a5f1-02608c9eebac', Pid=10)
DEVPKEY_Device_DeviceDesc = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=2)
DEVPKEY_Device_HardwareIds = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=3)
DEVPKEY_Device_CompatibleIds = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=4)
DEVPKEY_Device_Service = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=6)
DEVPKEY_Device_Class = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=9)
DEVPKEY_Device_ClassGuid = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=10)
DEVPKEY_Device_Driver = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=11)
DEVPKEY_Device_ConfigFlags = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=12)
DEVPKEY_Device_Manufacturer = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=13)
DEVPKEY_Device_FriendlyName = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=14)
DEVPKEY_Device_LocationInfo = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=15)
DEVPKEY_Device_PDOName = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=16)
DEVPKEY_Device_Capabilities = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=17)
DEVPKEY_Device_UINumber = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=18)
DEVPKEY_Device_UpperFilters = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=19)
DEVPKEY_Device_LowerFilters = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=20)
DEVPKEY_Device_BusTypeGuid = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=21)
DEVPKEY_Device_LegacyBusType = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=22)
DEVPKEY_Device_BusNumber = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=23)
DEVPKEY_Device_EnumeratorName = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=24)
DEVPKEY_Device_Security = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=25)
DEVPKEY_Device_SecuritySDS = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=26)
DEVPKEY_Device_DevType = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=27)
DEVPKEY_Device_Exclusive = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=28)
DEVPKEY_Device_Characteristics = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=29)
DEVPKEY_Device_Address = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=30)
DEVPKEY_Device_UINumberDescFormat = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=31)
DEVPKEY_Device_PowerData = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=32)
DEVPKEY_Device_RemovalPolicy = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=33)
DEVPKEY_Device_RemovalPolicyDefault = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=34)
DEVPKEY_Device_RemovalPolicyOverride = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=35)
DEVPKEY_Device_InstallState = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=36)
DEVPKEY_Device_LocationPaths = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=37)
DEVPKEY_Device_BaseContainerId = PROPERTYKEY(Fmtid='a45c254e-df1c-4efd-8020-67d146a850e0', Pid=38)
DEVPKEY_Device_InstanceId = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=256)
DEVPKEY_Device_DevNodeStatus = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=2)
DEVPKEY_Device_ProblemCode = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=3)
DEVPKEY_Device_EjectionRelations = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=4)
DEVPKEY_Device_RemovalRelations = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=5)
DEVPKEY_Device_PowerRelations = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=6)
DEVPKEY_Device_BusRelations = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=7)
DEVPKEY_Device_Parent = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=8)
DEVPKEY_Device_Children = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=9)
DEVPKEY_Device_Siblings = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=10)
DEVPKEY_Device_TransportRelations = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=11)
DEVPKEY_Device_ProblemStatus = PROPERTYKEY(Fmtid='4340a6c5-93fa-4706-972c-7b648008a5a7', Pid=12)
DEVPKEY_Device_Reported = PROPERTYKEY(Fmtid='80497100-8c73-48b9-aad9-ce387e19c56e', Pid=2)
DEVPKEY_Device_Legacy = PROPERTYKEY(Fmtid='80497100-8c73-48b9-aad9-ce387e19c56e', Pid=3)
DEVPKEY_Device_ContainerId = PROPERTYKEY(Fmtid='8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c', Pid=2)
DEVPKEY_Device_InLocalMachineContainer = PROPERTYKEY(Fmtid='8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c', Pid=4)
DEVPKEY_Device_Model = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=39)
DEVPKEY_Device_ModelId = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=2)
DEVPKEY_Device_FriendlyNameAttributes = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=3)
DEVPKEY_Device_ManufacturerAttributes = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=4)
DEVPKEY_Device_PresenceNotForDevice = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=5)
DEVPKEY_Device_SignalStrength = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=6)
DEVPKEY_Device_IsAssociateableByUserAction = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=7)
DEVPKEY_Device_ShowInUninstallUI = PROPERTYKEY(Fmtid='80d81ea6-7473-4b0c-8216-efc11a2c4c8b', Pid=8)
DEVPKEY_Device_Numa_Proximity_Domain = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=1)
DEVPKEY_Device_DHP_Rebalance_Policy = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=2)
DEVPKEY_Device_Numa_Node = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=3)
DEVPKEY_Device_BusReportedDeviceDesc = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=4)
DEVPKEY_Device_IsPresent = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=5)
DEVPKEY_Device_HasProblem = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=6)
DEVPKEY_Device_ConfigurationId = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=7)
DEVPKEY_Device_ReportedDeviceIdsHash = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=8)
DEVPKEY_Device_PhysicalDeviceLocation = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=9)
DEVPKEY_Device_BiosDeviceName = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=10)
DEVPKEY_Device_DriverProblemDesc = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=11)
DEVPKEY_Device_DebuggerSafe = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=12)
DEVPKEY_Device_PostInstallInProgress = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=13)
DEVPKEY_Device_Stack = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=14)
DEVPKEY_Device_ExtendedConfigurationIds = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=15)
DEVPKEY_Device_IsRebootRequired = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=16)
DEVPKEY_Device_FirmwareDate = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=17)
DEVPKEY_Device_FirmwareVersion = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=18)
DEVPKEY_Device_FirmwareRevision = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=19)
DEVPKEY_Device_DependencyProviders = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=20)
DEVPKEY_Device_DependencyDependents = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=21)
DEVPKEY_Device_SoftRestartSupported = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=22)
DEVPKEY_Device_ExtendedAddress = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=23)
DEVPKEY_Device_AssignedToGuest = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=24)
DEVPKEY_Device_CreatorProcessId = PROPERTYKEY(Fmtid='540b947e-8b40-45bc-a8a2-6a0b894cbda2', Pid=25)
DEVPKEY_Device_SessionId = PROPERTYKEY(Fmtid='83da6326-97a6-4088-9453-a1923f573b29', Pid=6)
DEVPKEY_Device_InstallDate = PROPERTYKEY(Fmtid='83da6326-97a6-4088-9453-a1923f573b29', Pid=100)
DEVPKEY_Device_FirstInstallDate = PROPERTYKEY(Fmtid='83da6326-97a6-4088-9453-a1923f573b29', Pid=101)
DEVPKEY_Device_LastArrivalDate = PROPERTYKEY(Fmtid='83da6326-97a6-4088-9453-a1923f573b29', Pid=102)
DEVPKEY_Device_LastRemovalDate = PROPERTYKEY(Fmtid='83da6326-97a6-4088-9453-a1923f573b29', Pid=103)
DEVPKEY_Device_DriverDate = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=2)
DEVPKEY_Device_DriverVersion = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=3)
DEVPKEY_Device_DriverDesc = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=4)
DEVPKEY_Device_DriverInfPath = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=5)
DEVPKEY_Device_DriverInfSection = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=6)
DEVPKEY_Device_DriverInfSectionExt = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=7)
DEVPKEY_Device_MatchingDeviceId = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=8)
DEVPKEY_Device_DriverProvider = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=9)
DEVPKEY_Device_DriverPropPageProvider = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=10)
DEVPKEY_Device_DriverCoInstallers = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=11)
DEVPKEY_Device_ResourcePickerTags = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=12)
DEVPKEY_Device_ResourcePickerExceptions = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=13)
DEVPKEY_Device_DriverRank = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=14)
DEVPKEY_Device_DriverLogoLevel = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=15)
DEVPKEY_Device_NoConnectSound = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=17)
DEVPKEY_Device_GenericDriverInstalled = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=18)
DEVPKEY_Device_AdditionalSoftwareRequested = PROPERTYKEY(Fmtid='a8b865dd-2e3d-4094-ad97-e593a70c75d6', Pid=19)
DEVPKEY_Device_SafeRemovalRequired = PROPERTYKEY(Fmtid='afd97640-86a3-4210-b67c-289c41aabe55', Pid=2)
DEVPKEY_Device_SafeRemovalRequiredOverride = PROPERTYKEY(Fmtid='afd97640-86a3-4210-b67c-289c41aabe55', Pid=3)
DEVPKEY_DrvPkg_Model = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=2)
DEVPKEY_DrvPkg_VendorWebSite = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=3)
DEVPKEY_DrvPkg_DetailedDescription = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=4)
DEVPKEY_DrvPkg_DocumentationLink = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=5)
DEVPKEY_DrvPkg_Icon = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=6)
DEVPKEY_DrvPkg_BrandingIcon = PROPERTYKEY(Fmtid='cf73bb51-3abf-44a2-85e0-9a3dc7a12132', Pid=7)
DEVPKEY_DeviceClass_UpperFilters = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=19)
DEVPKEY_DeviceClass_LowerFilters = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=20)
DEVPKEY_DeviceClass_Security = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=25)
DEVPKEY_DeviceClass_SecuritySDS = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=26)
DEVPKEY_DeviceClass_DevType = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=27)
DEVPKEY_DeviceClass_Exclusive = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=28)
DEVPKEY_DeviceClass_Characteristics = PROPERTYKEY(Fmtid='4321918b-f69e-470d-a5de-4d88c75ad24b', Pid=29)
DEVPKEY_DeviceClass_Name = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=2)
DEVPKEY_DeviceClass_ClassName = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=3)
DEVPKEY_DeviceClass_Icon = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=4)
DEVPKEY_DeviceClass_ClassInstaller = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=5)
DEVPKEY_DeviceClass_PropPageProvider = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=6)
DEVPKEY_DeviceClass_NoInstallClass = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=7)
DEVPKEY_DeviceClass_NoDisplayClass = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=8)
DEVPKEY_DeviceClass_SilentInstall = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=9)
DEVPKEY_DeviceClass_NoUseClass = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=10)
DEVPKEY_DeviceClass_DefaultService = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=11)
DEVPKEY_DeviceClass_IconPath = PROPERTYKEY(Fmtid='259abffc-50a7-47ce-af08-68c9a7d73366', Pid=12)
DEVPKEY_DeviceClass_DHPRebalanceOptOut = PROPERTYKEY(Fmtid='d14d3ef3-66cf-4ba2-9d38-0ddb37ab4701', Pid=2)
DEVPKEY_DeviceClass_ClassCoInstallers = PROPERTYKEY(Fmtid='713d1703-a2e2-49f5-9214-56472ef3da5c', Pid=2)
DEVPKEY_DeviceInterface_FriendlyName = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=2)
DEVPKEY_DeviceInterface_Enabled = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=3)
DEVPKEY_DeviceInterface_ClassGuid = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=4)
DEVPKEY_DeviceInterface_ReferenceString = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=5)
DEVPKEY_DeviceInterface_Restricted = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=6)
DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=8)
DEVPKEY_DeviceInterface_SchematicName = PROPERTYKEY(Fmtid='026e516e-b814-414b-83cd-856d6fef4822', Pid=9)
DEVPKEY_DeviceInterfaceClass_DefaultInterface = PROPERTYKEY(Fmtid='14c83a99-0b3f-44b7-be4c-a178d3990564', Pid=2)
DEVPKEY_DeviceInterfaceClass_Name = PROPERTYKEY(Fmtid='14c83a99-0b3f-44b7-be4c-a178d3990564', Pid=3)
DEVPKEY_DeviceContainer_Address = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=51)
DEVPKEY_DeviceContainer_DiscoveryMethod = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=52)
DEVPKEY_DeviceContainer_IsEncrypted = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=53)
DEVPKEY_DeviceContainer_IsAuthenticated = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=54)
DEVPKEY_DeviceContainer_IsConnected = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=55)
DEVPKEY_DeviceContainer_IsPaired = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=56)
DEVPKEY_DeviceContainer_Icon = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=57)
DEVPKEY_DeviceContainer_Version = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=65)
DEVPKEY_DeviceContainer_Last_Seen = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=66)
DEVPKEY_DeviceContainer_Last_Connected = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=67)
DEVPKEY_DeviceContainer_IsShowInDisconnectedState = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=68)
DEVPKEY_DeviceContainer_IsLocalMachine = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=70)
DEVPKEY_DeviceContainer_MetadataPath = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=71)
DEVPKEY_DeviceContainer_IsMetadataSearchInProgress = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=72)
DEVPKEY_DeviceContainer_MetadataChecksum = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=73)
DEVPKEY_DeviceContainer_IsNotInterestingForDisplay = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=74)
DEVPKEY_DeviceContainer_LaunchDeviceStageOnDeviceConnect = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=76)
DEVPKEY_DeviceContainer_LaunchDeviceStageFromExplorer = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=77)
DEVPKEY_DeviceContainer_BaselineExperienceId = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=78)
DEVPKEY_DeviceContainer_IsDeviceUniquelyIdentifiable = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=79)
DEVPKEY_DeviceContainer_AssociationArray = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=80)
DEVPKEY_DeviceContainer_DeviceDescription1 = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=81)
DEVPKEY_DeviceContainer_DeviceDescription2 = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=82)
DEVPKEY_DeviceContainer_HasProblem = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=83)
DEVPKEY_DeviceContainer_IsSharedDevice = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=84)
DEVPKEY_DeviceContainer_IsNetworkDevice = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=85)
DEVPKEY_DeviceContainer_IsDefaultDevice = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=86)
DEVPKEY_DeviceContainer_MetadataCabinet = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=87)
DEVPKEY_DeviceContainer_RequiresPairingElevation = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=88)
DEVPKEY_DeviceContainer_ExperienceId = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=89)
DEVPKEY_DeviceContainer_Category = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=90)
DEVPKEY_DeviceContainer_Category_Desc_Singular = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=91)
DEVPKEY_DeviceContainer_Category_Desc_Plural = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=92)
DEVPKEY_DeviceContainer_Category_Icon = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=93)
DEVPKEY_DeviceContainer_CategoryGroup_Desc = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=94)
DEVPKEY_DeviceContainer_CategoryGroup_Icon = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=95)
DEVPKEY_DeviceContainer_PrimaryCategory = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=97)
DEVPKEY_DeviceContainer_UnpairUninstall = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=98)
DEVPKEY_DeviceContainer_RequiresUninstallElevation = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=99)
DEVPKEY_DeviceContainer_DeviceFunctionSubRank = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=100)
DEVPKEY_DeviceContainer_AlwaysShowDeviceAsConnected = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=101)
DEVPKEY_DeviceContainer_ConfigFlags = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=105)
DEVPKEY_DeviceContainer_PrivilegedPackageFamilyNames = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=106)
DEVPKEY_DeviceContainer_CustomPrivilegedPackageFamilyNames = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=107)
DEVPKEY_DeviceContainer_IsRebootRequired = PROPERTYKEY(Fmtid='78c34fc8-104a-4aca-9ea4-524d52996e57', Pid=108)
DEVPKEY_DeviceContainer_FriendlyName = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=12288)
DEVPKEY_DeviceContainer_Manufacturer = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8192)
DEVPKEY_DeviceContainer_ModelName = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8194)
DEVPKEY_DeviceContainer_ModelNumber = PROPERTYKEY(Fmtid='656a3bb3-ecc0-43fd-8477-4ae0404a96cd', Pid=8195)
DEVPKEY_DeviceContainer_InstallInProgress = PROPERTYKEY(Fmtid='83da6326-97a6-4088-9453-a1923f573b29', Pid=9)
DEVPKEY_DevQuery_ObjectType = PROPERTYKEY(Fmtid='13673f42-a3d6-49f6-b4da-ae46e0c5237c', Pid=2)
DEVPROP_TYPEMOD_ARRAY = 4096
DEVPROP_TYPEMOD_LIST = 8192
DEVPROP_TYPE_EMPTY = 0
DEVPROP_TYPE_NULL = 1
DEVPROP_TYPE_SBYTE = 2
DEVPROP_TYPE_BYTE = 3
DEVPROP_TYPE_INT16 = 4
DEVPROP_TYPE_UINT16 = 5
DEVPROP_TYPE_INT32 = 6
DEVPROP_TYPE_UINT32 = 7
DEVPROP_TYPE_INT64 = 8
DEVPROP_TYPE_UINT64 = 9
DEVPROP_TYPE_FLOAT = 10
DEVPROP_TYPE_DOUBLE = 11
DEVPROP_TYPE_DECIMAL = 12
DEVPROP_TYPE_GUID = 13
DEVPROP_TYPE_CURRENCY = 14
DEVPROP_TYPE_DATE = 15
DEVPROP_TYPE_FILETIME = 16
DEVPROP_TYPE_BOOLEAN = 17
DEVPROP_TYPE_STRING = 18
DEVPROP_TYPE_SECURITY_DESCRIPTOR = 19
DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING = 20
DEVPROP_TYPE_DEVPROPKEY = 21
DEVPROP_TYPE_DEVPROPTYPE = 22
DEVPROP_TYPE_ERROR = 23
DEVPROP_TYPE_NTSTATUS = 24
DEVPROP_TYPE_STRING_INDIRECT = 25
MAX_DEVPROP_TYPE = 25
MAX_DEVPROP_TYPEMOD = 8192
DEVPROP_MASK_TYPE = 4095
DEVPROP_MASK_TYPEMOD = 61440
DEVPROPID_FIRST_USABLE = 2
def _define_DEVPROPKEY_head():
    class DEVPROPKEY(Structure):
        pass
    return DEVPROPKEY
def _define_DEVPROPKEY():
    DEVPROPKEY = win32more.Devices.Properties.DEVPROPKEY_head
    DEVPROPKEY._fields_ = [
        ("fmtid", Guid),
        ("pid", UInt32),
    ]
    return DEVPROPKEY
DEVPROPSTORE = Int32
DEVPROP_STORE_SYSTEM = 0
DEVPROP_STORE_USER = 1
def _define_DEVPROPCOMPKEY_head():
    class DEVPROPCOMPKEY(Structure):
        pass
    return DEVPROPCOMPKEY
def _define_DEVPROPCOMPKEY():
    DEVPROPCOMPKEY = win32more.Devices.Properties.DEVPROPCOMPKEY_head
    DEVPROPCOMPKEY._fields_ = [
        ("Key", win32more.Devices.Properties.DEVPROPKEY),
        ("Store", win32more.Devices.Properties.DEVPROPSTORE),
        ("LocaleName", win32more.Foundation.PWSTR),
    ]
    return DEVPROPCOMPKEY
def _define_DEVPROPERTY_head():
    class DEVPROPERTY(Structure):
        pass
    return DEVPROPERTY
def _define_DEVPROPERTY():
    DEVPROPERTY = win32more.Devices.Properties.DEVPROPERTY_head
    DEVPROPERTY._fields_ = [
        ("CompKey", win32more.Devices.Properties.DEVPROPCOMPKEY),
        ("Type", UInt32),
        ("BufferSize", UInt32),
        ("Buffer", c_void_p),
    ]
    return DEVPROPERTY
__all__ = [
    "DEVPKEY_DeviceInterface_Autoplay_Silent",
    "DEVPKEY_NAME",
    "DEVPKEY_Device_DeviceDesc",
    "DEVPKEY_Device_HardwareIds",
    "DEVPKEY_Device_CompatibleIds",
    "DEVPKEY_Device_Service",
    "DEVPKEY_Device_Class",
    "DEVPKEY_Device_ClassGuid",
    "DEVPKEY_Device_Driver",
    "DEVPKEY_Device_ConfigFlags",
    "DEVPKEY_Device_Manufacturer",
    "DEVPKEY_Device_FriendlyName",
    "DEVPKEY_Device_LocationInfo",
    "DEVPKEY_Device_PDOName",
    "DEVPKEY_Device_Capabilities",
    "DEVPKEY_Device_UINumber",
    "DEVPKEY_Device_UpperFilters",
    "DEVPKEY_Device_LowerFilters",
    "DEVPKEY_Device_BusTypeGuid",
    "DEVPKEY_Device_LegacyBusType",
    "DEVPKEY_Device_BusNumber",
    "DEVPKEY_Device_EnumeratorName",
    "DEVPKEY_Device_Security",
    "DEVPKEY_Device_SecuritySDS",
    "DEVPKEY_Device_DevType",
    "DEVPKEY_Device_Exclusive",
    "DEVPKEY_Device_Characteristics",
    "DEVPKEY_Device_Address",
    "DEVPKEY_Device_UINumberDescFormat",
    "DEVPKEY_Device_PowerData",
    "DEVPKEY_Device_RemovalPolicy",
    "DEVPKEY_Device_RemovalPolicyDefault",
    "DEVPKEY_Device_RemovalPolicyOverride",
    "DEVPKEY_Device_InstallState",
    "DEVPKEY_Device_LocationPaths",
    "DEVPKEY_Device_BaseContainerId",
    "DEVPKEY_Device_InstanceId",
    "DEVPKEY_Device_DevNodeStatus",
    "DEVPKEY_Device_ProblemCode",
    "DEVPKEY_Device_EjectionRelations",
    "DEVPKEY_Device_RemovalRelations",
    "DEVPKEY_Device_PowerRelations",
    "DEVPKEY_Device_BusRelations",
    "DEVPKEY_Device_Parent",
    "DEVPKEY_Device_Children",
    "DEVPKEY_Device_Siblings",
    "DEVPKEY_Device_TransportRelations",
    "DEVPKEY_Device_ProblemStatus",
    "DEVPKEY_Device_Reported",
    "DEVPKEY_Device_Legacy",
    "DEVPKEY_Device_ContainerId",
    "DEVPKEY_Device_InLocalMachineContainer",
    "DEVPKEY_Device_Model",
    "DEVPKEY_Device_ModelId",
    "DEVPKEY_Device_FriendlyNameAttributes",
    "DEVPKEY_Device_ManufacturerAttributes",
    "DEVPKEY_Device_PresenceNotForDevice",
    "DEVPKEY_Device_SignalStrength",
    "DEVPKEY_Device_IsAssociateableByUserAction",
    "DEVPKEY_Device_ShowInUninstallUI",
    "DEVPKEY_Device_Numa_Proximity_Domain",
    "DEVPKEY_Device_DHP_Rebalance_Policy",
    "DEVPKEY_Device_Numa_Node",
    "DEVPKEY_Device_BusReportedDeviceDesc",
    "DEVPKEY_Device_IsPresent",
    "DEVPKEY_Device_HasProblem",
    "DEVPKEY_Device_ConfigurationId",
    "DEVPKEY_Device_ReportedDeviceIdsHash",
    "DEVPKEY_Device_PhysicalDeviceLocation",
    "DEVPKEY_Device_BiosDeviceName",
    "DEVPKEY_Device_DriverProblemDesc",
    "DEVPKEY_Device_DebuggerSafe",
    "DEVPKEY_Device_PostInstallInProgress",
    "DEVPKEY_Device_Stack",
    "DEVPKEY_Device_ExtendedConfigurationIds",
    "DEVPKEY_Device_IsRebootRequired",
    "DEVPKEY_Device_FirmwareDate",
    "DEVPKEY_Device_FirmwareVersion",
    "DEVPKEY_Device_FirmwareRevision",
    "DEVPKEY_Device_DependencyProviders",
    "DEVPKEY_Device_DependencyDependents",
    "DEVPKEY_Device_SoftRestartSupported",
    "DEVPKEY_Device_ExtendedAddress",
    "DEVPKEY_Device_AssignedToGuest",
    "DEVPKEY_Device_CreatorProcessId",
    "DEVPKEY_Device_SessionId",
    "DEVPKEY_Device_InstallDate",
    "DEVPKEY_Device_FirstInstallDate",
    "DEVPKEY_Device_LastArrivalDate",
    "DEVPKEY_Device_LastRemovalDate",
    "DEVPKEY_Device_DriverDate",
    "DEVPKEY_Device_DriverVersion",
    "DEVPKEY_Device_DriverDesc",
    "DEVPKEY_Device_DriverInfPath",
    "DEVPKEY_Device_DriverInfSection",
    "DEVPKEY_Device_DriverInfSectionExt",
    "DEVPKEY_Device_MatchingDeviceId",
    "DEVPKEY_Device_DriverProvider",
    "DEVPKEY_Device_DriverPropPageProvider",
    "DEVPKEY_Device_DriverCoInstallers",
    "DEVPKEY_Device_ResourcePickerTags",
    "DEVPKEY_Device_ResourcePickerExceptions",
    "DEVPKEY_Device_DriverRank",
    "DEVPKEY_Device_DriverLogoLevel",
    "DEVPKEY_Device_NoConnectSound",
    "DEVPKEY_Device_GenericDriverInstalled",
    "DEVPKEY_Device_AdditionalSoftwareRequested",
    "DEVPKEY_Device_SafeRemovalRequired",
    "DEVPKEY_Device_SafeRemovalRequiredOverride",
    "DEVPKEY_DrvPkg_Model",
    "DEVPKEY_DrvPkg_VendorWebSite",
    "DEVPKEY_DrvPkg_DetailedDescription",
    "DEVPKEY_DrvPkg_DocumentationLink",
    "DEVPKEY_DrvPkg_Icon",
    "DEVPKEY_DrvPkg_BrandingIcon",
    "DEVPKEY_DeviceClass_UpperFilters",
    "DEVPKEY_DeviceClass_LowerFilters",
    "DEVPKEY_DeviceClass_Security",
    "DEVPKEY_DeviceClass_SecuritySDS",
    "DEVPKEY_DeviceClass_DevType",
    "DEVPKEY_DeviceClass_Exclusive",
    "DEVPKEY_DeviceClass_Characteristics",
    "DEVPKEY_DeviceClass_Name",
    "DEVPKEY_DeviceClass_ClassName",
    "DEVPKEY_DeviceClass_Icon",
    "DEVPKEY_DeviceClass_ClassInstaller",
    "DEVPKEY_DeviceClass_PropPageProvider",
    "DEVPKEY_DeviceClass_NoInstallClass",
    "DEVPKEY_DeviceClass_NoDisplayClass",
    "DEVPKEY_DeviceClass_SilentInstall",
    "DEVPKEY_DeviceClass_NoUseClass",
    "DEVPKEY_DeviceClass_DefaultService",
    "DEVPKEY_DeviceClass_IconPath",
    "DEVPKEY_DeviceClass_DHPRebalanceOptOut",
    "DEVPKEY_DeviceClass_ClassCoInstallers",
    "DEVPKEY_DeviceInterface_FriendlyName",
    "DEVPKEY_DeviceInterface_Enabled",
    "DEVPKEY_DeviceInterface_ClassGuid",
    "DEVPKEY_DeviceInterface_ReferenceString",
    "DEVPKEY_DeviceInterface_Restricted",
    "DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities",
    "DEVPKEY_DeviceInterface_SchematicName",
    "DEVPKEY_DeviceInterfaceClass_DefaultInterface",
    "DEVPKEY_DeviceInterfaceClass_Name",
    "DEVPKEY_DeviceContainer_Address",
    "DEVPKEY_DeviceContainer_DiscoveryMethod",
    "DEVPKEY_DeviceContainer_IsEncrypted",
    "DEVPKEY_DeviceContainer_IsAuthenticated",
    "DEVPKEY_DeviceContainer_IsConnected",
    "DEVPKEY_DeviceContainer_IsPaired",
    "DEVPKEY_DeviceContainer_Icon",
    "DEVPKEY_DeviceContainer_Version",
    "DEVPKEY_DeviceContainer_Last_Seen",
    "DEVPKEY_DeviceContainer_Last_Connected",
    "DEVPKEY_DeviceContainer_IsShowInDisconnectedState",
    "DEVPKEY_DeviceContainer_IsLocalMachine",
    "DEVPKEY_DeviceContainer_MetadataPath",
    "DEVPKEY_DeviceContainer_IsMetadataSearchInProgress",
    "DEVPKEY_DeviceContainer_MetadataChecksum",
    "DEVPKEY_DeviceContainer_IsNotInterestingForDisplay",
    "DEVPKEY_DeviceContainer_LaunchDeviceStageOnDeviceConnect",
    "DEVPKEY_DeviceContainer_LaunchDeviceStageFromExplorer",
    "DEVPKEY_DeviceContainer_BaselineExperienceId",
    "DEVPKEY_DeviceContainer_IsDeviceUniquelyIdentifiable",
    "DEVPKEY_DeviceContainer_AssociationArray",
    "DEVPKEY_DeviceContainer_DeviceDescription1",
    "DEVPKEY_DeviceContainer_DeviceDescription2",
    "DEVPKEY_DeviceContainer_HasProblem",
    "DEVPKEY_DeviceContainer_IsSharedDevice",
    "DEVPKEY_DeviceContainer_IsNetworkDevice",
    "DEVPKEY_DeviceContainer_IsDefaultDevice",
    "DEVPKEY_DeviceContainer_MetadataCabinet",
    "DEVPKEY_DeviceContainer_RequiresPairingElevation",
    "DEVPKEY_DeviceContainer_ExperienceId",
    "DEVPKEY_DeviceContainer_Category",
    "DEVPKEY_DeviceContainer_Category_Desc_Singular",
    "DEVPKEY_DeviceContainer_Category_Desc_Plural",
    "DEVPKEY_DeviceContainer_Category_Icon",
    "DEVPKEY_DeviceContainer_CategoryGroup_Desc",
    "DEVPKEY_DeviceContainer_CategoryGroup_Icon",
    "DEVPKEY_DeviceContainer_PrimaryCategory",
    "DEVPKEY_DeviceContainer_UnpairUninstall",
    "DEVPKEY_DeviceContainer_RequiresUninstallElevation",
    "DEVPKEY_DeviceContainer_DeviceFunctionSubRank",
    "DEVPKEY_DeviceContainer_AlwaysShowDeviceAsConnected",
    "DEVPKEY_DeviceContainer_ConfigFlags",
    "DEVPKEY_DeviceContainer_PrivilegedPackageFamilyNames",
    "DEVPKEY_DeviceContainer_CustomPrivilegedPackageFamilyNames",
    "DEVPKEY_DeviceContainer_IsRebootRequired",
    "DEVPKEY_DeviceContainer_FriendlyName",
    "DEVPKEY_DeviceContainer_Manufacturer",
    "DEVPKEY_DeviceContainer_ModelName",
    "DEVPKEY_DeviceContainer_ModelNumber",
    "DEVPKEY_DeviceContainer_InstallInProgress",
    "DEVPKEY_DevQuery_ObjectType",
    "DEVPROP_TYPEMOD_ARRAY",
    "DEVPROP_TYPEMOD_LIST",
    "DEVPROP_TYPE_EMPTY",
    "DEVPROP_TYPE_NULL",
    "DEVPROP_TYPE_SBYTE",
    "DEVPROP_TYPE_BYTE",
    "DEVPROP_TYPE_INT16",
    "DEVPROP_TYPE_UINT16",
    "DEVPROP_TYPE_INT32",
    "DEVPROP_TYPE_UINT32",
    "DEVPROP_TYPE_INT64",
    "DEVPROP_TYPE_UINT64",
    "DEVPROP_TYPE_FLOAT",
    "DEVPROP_TYPE_DOUBLE",
    "DEVPROP_TYPE_DECIMAL",
    "DEVPROP_TYPE_GUID",
    "DEVPROP_TYPE_CURRENCY",
    "DEVPROP_TYPE_DATE",
    "DEVPROP_TYPE_FILETIME",
    "DEVPROP_TYPE_BOOLEAN",
    "DEVPROP_TYPE_STRING",
    "DEVPROP_TYPE_SECURITY_DESCRIPTOR",
    "DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING",
    "DEVPROP_TYPE_DEVPROPKEY",
    "DEVPROP_TYPE_DEVPROPTYPE",
    "DEVPROP_TYPE_ERROR",
    "DEVPROP_TYPE_NTSTATUS",
    "DEVPROP_TYPE_STRING_INDIRECT",
    "MAX_DEVPROP_TYPE",
    "MAX_DEVPROP_TYPEMOD",
    "DEVPROP_MASK_TYPE",
    "DEVPROP_MASK_TYPEMOD",
    "DEVPROPID_FIRST_USABLE",
    "DEVPROPKEY",
    "DEVPROPSTORE",
    "DEVPROP_STORE_SYSTEM",
    "DEVPROP_STORE_USER",
    "DEVPROPCOMPKEY",
    "DEVPROPERTY",
]
