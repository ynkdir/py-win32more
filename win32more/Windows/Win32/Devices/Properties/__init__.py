from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Properties
import win32more.Windows.Win32.Foundation
DEVPROP_TRUE: win32more.Windows.Win32.Devices.Properties.DEVPROP_BOOLEAN = 255
DEVPROP_FALSE: win32more.Windows.Win32.Devices.Properties.DEVPROP_BOOLEAN = 0
def DEVPKEY_DeviceInterface_Autoplay_Silent():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{434dd28f-9e75-450a-9ab9-ff61e618bad0}'), pid=2)
def DEVPKEY_NAME():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=10)
def DEVPKEY_Device_DeviceDesc():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=2)
def DEVPKEY_Device_HardwareIds():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=3)
def DEVPKEY_Device_CompatibleIds():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=4)
def DEVPKEY_Device_Service():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=6)
def DEVPKEY_Device_Class():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=9)
def DEVPKEY_Device_ClassGuid():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=10)
def DEVPKEY_Device_Driver():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=11)
def DEVPKEY_Device_ConfigFlags():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=12)
def DEVPKEY_Device_Manufacturer():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=13)
def DEVPKEY_Device_FriendlyName():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=14)
def DEVPKEY_Device_LocationInfo():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=15)
def DEVPKEY_Device_PDOName():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=16)
def DEVPKEY_Device_Capabilities():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=17)
def DEVPKEY_Device_UINumber():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=18)
def DEVPKEY_Device_UpperFilters():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=19)
def DEVPKEY_Device_LowerFilters():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=20)
def DEVPKEY_Device_BusTypeGuid():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=21)
def DEVPKEY_Device_LegacyBusType():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=22)
def DEVPKEY_Device_BusNumber():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=23)
def DEVPKEY_Device_EnumeratorName():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=24)
def DEVPKEY_Device_Security():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=25)
def DEVPKEY_Device_SecuritySDS():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=26)
def DEVPKEY_Device_DevType():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=27)
def DEVPKEY_Device_Exclusive():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=28)
def DEVPKEY_Device_Characteristics():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=29)
def DEVPKEY_Device_Address():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=30)
def DEVPKEY_Device_UINumberDescFormat():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=31)
def DEVPKEY_Device_PowerData():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=32)
def DEVPKEY_Device_RemovalPolicy():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=33)
def DEVPKEY_Device_RemovalPolicyDefault():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=34)
def DEVPKEY_Device_RemovalPolicyOverride():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=35)
def DEVPKEY_Device_InstallState():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=36)
def DEVPKEY_Device_LocationPaths():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=37)
def DEVPKEY_Device_BaseContainerId():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=38)
def DEVPKEY_Device_InstanceId():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=256)
def DEVPKEY_Device_DevNodeStatus():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=2)
def DEVPKEY_Device_ProblemCode():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=3)
def DEVPKEY_Device_EjectionRelations():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=4)
def DEVPKEY_Device_RemovalRelations():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=5)
def DEVPKEY_Device_PowerRelations():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=6)
def DEVPKEY_Device_BusRelations():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=7)
def DEVPKEY_Device_Parent():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=8)
def DEVPKEY_Device_Children():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=9)
def DEVPKEY_Device_Siblings():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=10)
def DEVPKEY_Device_TransportRelations():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=11)
def DEVPKEY_Device_ProblemStatus():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=12)
def DEVPKEY_Device_Reported():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{80497100-8c73-48b9-aad9-ce387e19c56e}'), pid=2)
def DEVPKEY_Device_Legacy():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{80497100-8c73-48b9-aad9-ce387e19c56e}'), pid=3)
def DEVPKEY_Device_ContainerId():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c}'), pid=2)
def DEVPKEY_Device_InLocalMachineContainer():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c}'), pid=4)
def DEVPKEY_Device_Model():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=39)
def DEVPKEY_Device_ModelId():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=2)
def DEVPKEY_Device_FriendlyNameAttributes():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=3)
def DEVPKEY_Device_ManufacturerAttributes():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=4)
def DEVPKEY_Device_PresenceNotForDevice():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=5)
def DEVPKEY_Device_SignalStrength():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=6)
def DEVPKEY_Device_IsAssociateableByUserAction():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=7)
def DEVPKEY_Device_ShowInUninstallUI():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=8)
def DEVPKEY_Device_Numa_Proximity_Domain():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=1)
def DEVPKEY_Device_DHP_Rebalance_Policy():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=2)
def DEVPKEY_Device_Numa_Node():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=3)
def DEVPKEY_Device_BusReportedDeviceDesc():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=4)
def DEVPKEY_Device_IsPresent():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=5)
def DEVPKEY_Device_HasProblem():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=6)
def DEVPKEY_Device_ConfigurationId():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=7)
def DEVPKEY_Device_ReportedDeviceIdsHash():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=8)
def DEVPKEY_Device_PhysicalDeviceLocation():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=9)
def DEVPKEY_Device_BiosDeviceName():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=10)
def DEVPKEY_Device_DriverProblemDesc():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=11)
def DEVPKEY_Device_DebuggerSafe():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=12)
def DEVPKEY_Device_PostInstallInProgress():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=13)
def DEVPKEY_Device_Stack():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=14)
def DEVPKEY_Device_ExtendedConfigurationIds():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=15)
def DEVPKEY_Device_IsRebootRequired():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=16)
def DEVPKEY_Device_FirmwareDate():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=17)
def DEVPKEY_Device_FirmwareVersion():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=18)
def DEVPKEY_Device_FirmwareRevision():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=19)
def DEVPKEY_Device_DependencyProviders():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=20)
def DEVPKEY_Device_DependencyDependents():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=21)
def DEVPKEY_Device_SoftRestartSupported():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=22)
def DEVPKEY_Device_ExtendedAddress():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=23)
def DEVPKEY_Device_AssignedToGuest():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=24)
def DEVPKEY_Device_CreatorProcessId():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=25)
def DEVPKEY_Device_FirmwareVendor():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=26)
def DEVPKEY_Device_SessionId():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=6)
def DEVPKEY_Device_InstallDate():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=100)
def DEVPKEY_Device_FirstInstallDate():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=101)
def DEVPKEY_Device_LastArrivalDate():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=102)
def DEVPKEY_Device_LastRemovalDate():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=103)
def DEVPKEY_Device_DriverDate():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=2)
def DEVPKEY_Device_DriverVersion():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=3)
def DEVPKEY_Device_DriverDesc():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=4)
def DEVPKEY_Device_DriverInfPath():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=5)
def DEVPKEY_Device_DriverInfSection():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=6)
def DEVPKEY_Device_DriverInfSectionExt():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=7)
def DEVPKEY_Device_MatchingDeviceId():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=8)
def DEVPKEY_Device_DriverProvider():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=9)
def DEVPKEY_Device_DriverPropPageProvider():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=10)
def DEVPKEY_Device_DriverCoInstallers():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=11)
def DEVPKEY_Device_ResourcePickerTags():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=12)
def DEVPKEY_Device_ResourcePickerExceptions():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=13)
def DEVPKEY_Device_DriverRank():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=14)
def DEVPKEY_Device_DriverLogoLevel():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=15)
def DEVPKEY_Device_NoConnectSound():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=17)
def DEVPKEY_Device_GenericDriverInstalled():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=18)
def DEVPKEY_Device_AdditionalSoftwareRequested():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=19)
def DEVPKEY_Device_SafeRemovalRequired():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{afd97640-86a3-4210-b67c-289c41aabe55}'), pid=2)
def DEVPKEY_Device_SafeRemovalRequiredOverride():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{afd97640-86a3-4210-b67c-289c41aabe55}'), pid=3)
def DEVPKEY_DrvPkg_Model():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=2)
def DEVPKEY_DrvPkg_VendorWebSite():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=3)
def DEVPKEY_DrvPkg_DetailedDescription():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=4)
def DEVPKEY_DrvPkg_DocumentationLink():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=5)
def DEVPKEY_DrvPkg_Icon():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=6)
def DEVPKEY_DrvPkg_BrandingIcon():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=7)
def DEVPKEY_DeviceClass_UpperFilters():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=19)
def DEVPKEY_DeviceClass_LowerFilters():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=20)
def DEVPKEY_DeviceClass_Security():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=25)
def DEVPKEY_DeviceClass_SecuritySDS():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=26)
def DEVPKEY_DeviceClass_DevType():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=27)
def DEVPKEY_DeviceClass_Exclusive():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=28)
def DEVPKEY_DeviceClass_Characteristics():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=29)
def DEVPKEY_DeviceClass_Name():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=2)
def DEVPKEY_DeviceClass_ClassName():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=3)
def DEVPKEY_DeviceClass_Icon():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=4)
def DEVPKEY_DeviceClass_ClassInstaller():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=5)
def DEVPKEY_DeviceClass_PropPageProvider():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=6)
def DEVPKEY_DeviceClass_NoInstallClass():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=7)
def DEVPKEY_DeviceClass_NoDisplayClass():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=8)
def DEVPKEY_DeviceClass_SilentInstall():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=9)
def DEVPKEY_DeviceClass_NoUseClass():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=10)
def DEVPKEY_DeviceClass_DefaultService():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=11)
def DEVPKEY_DeviceClass_IconPath():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=12)
def DEVPKEY_DeviceClass_DHPRebalanceOptOut():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{d14d3ef3-66cf-4ba2-9d38-0ddb37ab4701}'), pid=2)
def DEVPKEY_DeviceClass_ClassCoInstallers():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{713d1703-a2e2-49f5-9214-56472ef3da5c}'), pid=2)
def DEVPKEY_DeviceInterface_FriendlyName():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=2)
def DEVPKEY_DeviceInterface_Enabled():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=3)
def DEVPKEY_DeviceInterface_ClassGuid():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=4)
def DEVPKEY_DeviceInterface_ReferenceString():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=5)
def DEVPKEY_DeviceInterface_Restricted():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=6)
def DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=8)
def DEVPKEY_DeviceInterface_SchematicName():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=9)
def DEVPKEY_DeviceInterfaceClass_DefaultInterface():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{14c83a99-0b3f-44b7-be4c-a178d3990564}'), pid=2)
def DEVPKEY_DeviceInterfaceClass_Name():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{14c83a99-0b3f-44b7-be4c-a178d3990564}'), pid=3)
def DEVPKEY_DeviceContainer_Address():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=51)
def DEVPKEY_DeviceContainer_DiscoveryMethod():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=52)
def DEVPKEY_DeviceContainer_IsEncrypted():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=53)
def DEVPKEY_DeviceContainer_IsAuthenticated():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=54)
def DEVPKEY_DeviceContainer_IsConnected():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=55)
def DEVPKEY_DeviceContainer_IsPaired():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=56)
def DEVPKEY_DeviceContainer_Icon():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=57)
def DEVPKEY_DeviceContainer_Version():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=65)
def DEVPKEY_DeviceContainer_Last_Seen():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=66)
def DEVPKEY_DeviceContainer_Last_Connected():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=67)
def DEVPKEY_DeviceContainer_IsShowInDisconnectedState():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=68)
def DEVPKEY_DeviceContainer_IsLocalMachine():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=70)
def DEVPKEY_DeviceContainer_MetadataPath():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=71)
def DEVPKEY_DeviceContainer_IsMetadataSearchInProgress():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=72)
def DEVPKEY_DeviceContainer_MetadataChecksum():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=73)
def DEVPKEY_DeviceContainer_IsNotInterestingForDisplay():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=74)
def DEVPKEY_DeviceContainer_LaunchDeviceStageOnDeviceConnect():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=76)
def DEVPKEY_DeviceContainer_LaunchDeviceStageFromExplorer():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=77)
def DEVPKEY_DeviceContainer_BaselineExperienceId():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=78)
def DEVPKEY_DeviceContainer_IsDeviceUniquelyIdentifiable():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=79)
def DEVPKEY_DeviceContainer_AssociationArray():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=80)
def DEVPKEY_DeviceContainer_DeviceDescription1():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=81)
def DEVPKEY_DeviceContainer_DeviceDescription2():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=82)
def DEVPKEY_DeviceContainer_HasProblem():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=83)
def DEVPKEY_DeviceContainer_IsSharedDevice():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=84)
def DEVPKEY_DeviceContainer_IsNetworkDevice():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=85)
def DEVPKEY_DeviceContainer_IsDefaultDevice():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=86)
def DEVPKEY_DeviceContainer_MetadataCabinet():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=87)
def DEVPKEY_DeviceContainer_RequiresPairingElevation():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=88)
def DEVPKEY_DeviceContainer_ExperienceId():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=89)
def DEVPKEY_DeviceContainer_Category():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=90)
def DEVPKEY_DeviceContainer_Category_Desc_Singular():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=91)
def DEVPKEY_DeviceContainer_Category_Desc_Plural():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=92)
def DEVPKEY_DeviceContainer_Category_Icon():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=93)
def DEVPKEY_DeviceContainer_CategoryGroup_Desc():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=94)
def DEVPKEY_DeviceContainer_CategoryGroup_Icon():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=95)
def DEVPKEY_DeviceContainer_PrimaryCategory():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=97)
def DEVPKEY_DeviceContainer_UnpairUninstall():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=98)
def DEVPKEY_DeviceContainer_RequiresUninstallElevation():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=99)
def DEVPKEY_DeviceContainer_DeviceFunctionSubRank():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=100)
def DEVPKEY_DeviceContainer_AlwaysShowDeviceAsConnected():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=101)
def DEVPKEY_DeviceContainer_ConfigFlags():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=105)
def DEVPKEY_DeviceContainer_PrivilegedPackageFamilyNames():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=106)
def DEVPKEY_DeviceContainer_CustomPrivilegedPackageFamilyNames():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=107)
def DEVPKEY_DeviceContainer_IsRebootRequired():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=108)
def DEVPKEY_DeviceContainer_FriendlyName():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12288)
def DEVPKEY_DeviceContainer_Manufacturer():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8192)
def DEVPKEY_DeviceContainer_ModelName():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8194)
def DEVPKEY_DeviceContainer_ModelNumber():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8195)
def DEVPKEY_DeviceContainer_InstallInProgress():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=9)
def DEVPKEY_DevQuery_ObjectType():
    return win32more.Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{13673f42-a3d6-49f6-b4da-ae46e0c5237c}'), pid=2)
DEVPROP_TYPEMOD_ARRAY: UInt32 = 4096
DEVPROP_TYPEMOD_LIST: UInt32 = 8192
MAX_DEVPROP_TYPE: UInt32 = 25
MAX_DEVPROP_TYPEMOD: UInt32 = 8192
DEVPROP_MASK_TYPE: UInt32 = 4095
DEVPROP_MASK_TYPEMOD: UInt32 = 61440
DEVPROPID_FIRST_USABLE: UInt32 = 2
class DEVPROPCOMPKEY(EasyCastStructure):
    Key: win32more.Windows.Win32.Devices.Properties.DEVPROPKEY
    Store: win32more.Windows.Win32.Devices.Properties.DEVPROPSTORE
    LocaleName: win32more.Windows.Win32.Foundation.PWSTR
class DEVPROPERTY(EasyCastStructure):
    CompKey: win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY
    Type: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE
    BufferSize: UInt32
    Buffer: VoidPtr
class DEVPROPKEY(EasyCastStructure):
    fmtid: Guid
    pid: UInt32
DEVPROPSTORE = Int32
DEVPROP_STORE_SYSTEM: win32more.Windows.Win32.Devices.Properties.DEVPROPSTORE = 0
DEVPROP_STORE_USER: win32more.Windows.Win32.Devices.Properties.DEVPROPSTORE = 1
DEVPROPTYPE = UInt32
DEVPROP_TYPE_EMPTY: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 0
DEVPROP_TYPE_NULL: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 1
DEVPROP_TYPE_SBYTE: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 2
DEVPROP_TYPE_BYTE: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 3
DEVPROP_TYPE_INT16: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 4
DEVPROP_TYPE_UINT16: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 5
DEVPROP_TYPE_INT32: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 6
DEVPROP_TYPE_UINT32: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 7
DEVPROP_TYPE_INT64: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 8
DEVPROP_TYPE_UINT64: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 9
DEVPROP_TYPE_FLOAT: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 10
DEVPROP_TYPE_DOUBLE: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 11
DEVPROP_TYPE_DECIMAL: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 12
DEVPROP_TYPE_GUID: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 13
DEVPROP_TYPE_CURRENCY: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 14
DEVPROP_TYPE_DATE: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 15
DEVPROP_TYPE_FILETIME: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 16
DEVPROP_TYPE_BOOLEAN: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 17
DEVPROP_TYPE_STRING: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 18
DEVPROP_TYPE_STRING_LIST: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 8210
DEVPROP_TYPE_SECURITY_DESCRIPTOR: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 19
DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 20
DEVPROP_TYPE_DEVPROPKEY: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 21
DEVPROP_TYPE_DEVPROPTYPE: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 22
DEVPROP_TYPE_BINARY: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 4099
DEVPROP_TYPE_ERROR: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 23
DEVPROP_TYPE_NTSTATUS: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 24
DEVPROP_TYPE_STRING_INDIRECT: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 25
DEVPROP_BOOLEAN = Byte


make_ready(__name__)
