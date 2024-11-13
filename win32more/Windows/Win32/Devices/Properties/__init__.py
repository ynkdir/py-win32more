from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Properties
import win32more.Windows.Win32.Foundation
DEVPROP_TRUE: win32more.Windows.Win32.Devices.Properties.DEVPROP_BOOLEAN = 255
DEVPROP_FALSE: win32more.Windows.Win32.Devices.Properties.DEVPROP_BOOLEAN = 0
DEVPKEY_DeviceInterface_Autoplay_Silent: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{434dd28f-9e75-450a-9ab9-ff61e618bad0}'), pid=2)
DEVPKEY_NAME: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}'), pid=10)
DEVPKEY_Device_DeviceDesc: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=2)
DEVPKEY_Device_HardwareIds: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=3)
DEVPKEY_Device_CompatibleIds: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=4)
DEVPKEY_Device_Service: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=6)
DEVPKEY_Device_Class: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=9)
DEVPKEY_Device_ClassGuid: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=10)
DEVPKEY_Device_Driver: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=11)
DEVPKEY_Device_ConfigFlags: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=12)
DEVPKEY_Device_Manufacturer: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=13)
DEVPKEY_Device_FriendlyName: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=14)
DEVPKEY_Device_LocationInfo: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=15)
DEVPKEY_Device_PDOName: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=16)
DEVPKEY_Device_Capabilities: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=17)
DEVPKEY_Device_UINumber: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=18)
DEVPKEY_Device_UpperFilters: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=19)
DEVPKEY_Device_LowerFilters: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=20)
DEVPKEY_Device_BusTypeGuid: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=21)
DEVPKEY_Device_LegacyBusType: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=22)
DEVPKEY_Device_BusNumber: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=23)
DEVPKEY_Device_EnumeratorName: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=24)
DEVPKEY_Device_Security: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=25)
DEVPKEY_Device_SecuritySDS: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=26)
DEVPKEY_Device_DevType: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=27)
DEVPKEY_Device_Exclusive: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=28)
DEVPKEY_Device_Characteristics: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=29)
DEVPKEY_Device_Address: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=30)
DEVPKEY_Device_UINumberDescFormat: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=31)
DEVPKEY_Device_PowerData: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=32)
DEVPKEY_Device_RemovalPolicy: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=33)
DEVPKEY_Device_RemovalPolicyDefault: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=34)
DEVPKEY_Device_RemovalPolicyOverride: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=35)
DEVPKEY_Device_InstallState: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=36)
DEVPKEY_Device_LocationPaths: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=37)
DEVPKEY_Device_BaseContainerId: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a45c254e-df1c-4efd-8020-67d146a850e0}'), pid=38)
DEVPKEY_Device_InstanceId: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=256)
DEVPKEY_Device_DevNodeStatus: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=2)
DEVPKEY_Device_ProblemCode: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=3)
DEVPKEY_Device_EjectionRelations: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=4)
DEVPKEY_Device_RemovalRelations: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=5)
DEVPKEY_Device_PowerRelations: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=6)
DEVPKEY_Device_BusRelations: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=7)
DEVPKEY_Device_Parent: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=8)
DEVPKEY_Device_Children: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=9)
DEVPKEY_Device_Siblings: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=10)
DEVPKEY_Device_TransportRelations: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=11)
DEVPKEY_Device_ProblemStatus: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4340a6c5-93fa-4706-972c-7b648008a5a7}'), pid=12)
DEVPKEY_Device_Reported: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{80497100-8c73-48b9-aad9-ce387e19c56e}'), pid=2)
DEVPKEY_Device_Legacy: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{80497100-8c73-48b9-aad9-ce387e19c56e}'), pid=3)
DEVPKEY_Device_ContainerId: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c}'), pid=2)
DEVPKEY_Device_InLocalMachineContainer: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c}'), pid=4)
DEVPKEY_Device_Model: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=39)
DEVPKEY_Device_ModelId: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=2)
DEVPKEY_Device_FriendlyNameAttributes: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=3)
DEVPKEY_Device_ManufacturerAttributes: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=4)
DEVPKEY_Device_PresenceNotForDevice: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=5)
DEVPKEY_Device_SignalStrength: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=6)
DEVPKEY_Device_IsAssociateableByUserAction: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=7)
DEVPKEY_Device_ShowInUninstallUI: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}'), pid=8)
DEVPKEY_Device_CompanionApps: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{6a742654-d0b2-4420-a523-e068352ac1df}'), pid=2)
DEVPKEY_Device_PrimaryCompanionApp: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{6a742654-d0b2-4420-a523-e068352ac1df}'), pid=3)
DEVPKEY_Device_Numa_Proximity_Domain: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=1)
DEVPKEY_Device_DHP_Rebalance_Policy: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=2)
DEVPKEY_Device_Numa_Node: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=3)
DEVPKEY_Device_BusReportedDeviceDesc: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=4)
DEVPKEY_Device_IsPresent: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=5)
DEVPKEY_Device_HasProblem: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=6)
DEVPKEY_Device_ConfigurationId: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=7)
DEVPKEY_Device_ReportedDeviceIdsHash: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=8)
DEVPKEY_Device_PhysicalDeviceLocation: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=9)
DEVPKEY_Device_BiosDeviceName: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=10)
DEVPKEY_Device_DriverProblemDesc: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=11)
DEVPKEY_Device_DebuggerSafe: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=12)
DEVPKEY_Device_PostInstallInProgress: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=13)
DEVPKEY_Device_Stack: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=14)
DEVPKEY_Device_ExtendedConfigurationIds: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=15)
DEVPKEY_Device_IsRebootRequired: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=16)
DEVPKEY_Device_FirmwareDate: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=17)
DEVPKEY_Device_FirmwareVersion: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=18)
DEVPKEY_Device_FirmwareRevision: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=19)
DEVPKEY_Device_DependencyProviders: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=20)
DEVPKEY_Device_DependencyDependents: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=21)
DEVPKEY_Device_SoftRestartSupported: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=22)
DEVPKEY_Device_ExtendedAddress: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=23)
DEVPKEY_Device_AssignedToGuest: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=24)
DEVPKEY_Device_CreatorProcessId: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=25)
DEVPKEY_Device_FirmwareVendor: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}'), pid=26)
DEVPKEY_Device_SessionId: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=6)
DEVPKEY_Device_InstallDate: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=100)
DEVPKEY_Device_FirstInstallDate: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=101)
DEVPKEY_Device_LastArrivalDate: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=102)
DEVPKEY_Device_LastRemovalDate: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=103)
DEVPKEY_Device_DriverDate: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=2)
DEVPKEY_Device_DriverVersion: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=3)
DEVPKEY_Device_DriverDesc: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=4)
DEVPKEY_Device_DriverInfPath: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=5)
DEVPKEY_Device_DriverInfSection: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=6)
DEVPKEY_Device_DriverInfSectionExt: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=7)
DEVPKEY_Device_MatchingDeviceId: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=8)
DEVPKEY_Device_DriverProvider: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=9)
DEVPKEY_Device_DriverPropPageProvider: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=10)
DEVPKEY_Device_DriverCoInstallers: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=11)
DEVPKEY_Device_ResourcePickerTags: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=12)
DEVPKEY_Device_ResourcePickerExceptions: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=13)
DEVPKEY_Device_DriverRank: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=14)
DEVPKEY_Device_DriverLogoLevel: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=15)
DEVPKEY_Device_NoConnectSound: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=17)
DEVPKEY_Device_GenericDriverInstalled: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=18)
DEVPKEY_Device_AdditionalSoftwareRequested: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}'), pid=19)
DEVPKEY_Device_SafeRemovalRequired: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{afd97640-86a3-4210-b67c-289c41aabe55}'), pid=2)
DEVPKEY_Device_SafeRemovalRequiredOverride: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{afd97640-86a3-4210-b67c-289c41aabe55}'), pid=3)
DEVPKEY_DrvPkg_Model: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=2)
DEVPKEY_DrvPkg_VendorWebSite: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=3)
DEVPKEY_DrvPkg_DetailedDescription: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=4)
DEVPKEY_DrvPkg_DocumentationLink: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=5)
DEVPKEY_DrvPkg_Icon: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=6)
DEVPKEY_DrvPkg_BrandingIcon: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}'), pid=7)
DEVPKEY_DeviceClass_UpperFilters: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=19)
DEVPKEY_DeviceClass_LowerFilters: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=20)
DEVPKEY_DeviceClass_Security: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=25)
DEVPKEY_DeviceClass_SecuritySDS: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=26)
DEVPKEY_DeviceClass_DevType: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=27)
DEVPKEY_DeviceClass_Exclusive: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=28)
DEVPKEY_DeviceClass_Characteristics: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{4321918b-f69e-470d-a5de-4d88c75ad24b}'), pid=29)
DEVPKEY_DeviceClass_Name: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=2)
DEVPKEY_DeviceClass_ClassName: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=3)
DEVPKEY_DeviceClass_Icon: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=4)
DEVPKEY_DeviceClass_ClassInstaller: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=5)
DEVPKEY_DeviceClass_PropPageProvider: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=6)
DEVPKEY_DeviceClass_NoInstallClass: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=7)
DEVPKEY_DeviceClass_NoDisplayClass: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=8)
DEVPKEY_DeviceClass_SilentInstall: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=9)
DEVPKEY_DeviceClass_NoUseClass: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=10)
DEVPKEY_DeviceClass_DefaultService: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=11)
DEVPKEY_DeviceClass_IconPath: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{259abffc-50a7-47ce-af08-68c9a7d73366}'), pid=12)
DEVPKEY_DeviceClass_DHPRebalanceOptOut: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{d14d3ef3-66cf-4ba2-9d38-0ddb37ab4701}'), pid=2)
DEVPKEY_DeviceClass_ClassCoInstallers: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{713d1703-a2e2-49f5-9214-56472ef3da5c}'), pid=2)
DEVPKEY_DeviceInterface_FriendlyName: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=2)
DEVPKEY_DeviceInterface_Enabled: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=3)
DEVPKEY_DeviceInterface_ClassGuid: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=4)
DEVPKEY_DeviceInterface_ReferenceString: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=5)
DEVPKEY_DeviceInterface_Restricted: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=6)
DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=8)
DEVPKEY_DeviceInterface_SchematicName: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{026e516e-b814-414b-83cd-856d6fef4822}'), pid=9)
DEVPKEY_DeviceInterfaceClass_DefaultInterface: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{14c83a99-0b3f-44b7-be4c-a178d3990564}'), pid=2)
DEVPKEY_DeviceInterfaceClass_Name: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{14c83a99-0b3f-44b7-be4c-a178d3990564}'), pid=3)
DEVPKEY_DeviceContainer_Address: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=51)
DEVPKEY_DeviceContainer_DiscoveryMethod: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=52)
DEVPKEY_DeviceContainer_IsEncrypted: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=53)
DEVPKEY_DeviceContainer_IsAuthenticated: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=54)
DEVPKEY_DeviceContainer_IsConnected: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=55)
DEVPKEY_DeviceContainer_IsPaired: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=56)
DEVPKEY_DeviceContainer_Icon: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=57)
DEVPKEY_DeviceContainer_Version: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=65)
DEVPKEY_DeviceContainer_Last_Seen: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=66)
DEVPKEY_DeviceContainer_Last_Connected: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=67)
DEVPKEY_DeviceContainer_IsShowInDisconnectedState: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=68)
DEVPKEY_DeviceContainer_IsLocalMachine: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=70)
DEVPKEY_DeviceContainer_MetadataPath: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=71)
DEVPKEY_DeviceContainer_IsMetadataSearchInProgress: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=72)
DEVPKEY_DeviceContainer_MetadataChecksum: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=73)
DEVPKEY_DeviceContainer_IsNotInterestingForDisplay: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=74)
DEVPKEY_DeviceContainer_LaunchDeviceStageOnDeviceConnect: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=76)
DEVPKEY_DeviceContainer_LaunchDeviceStageFromExplorer: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=77)
DEVPKEY_DeviceContainer_BaselineExperienceId: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=78)
DEVPKEY_DeviceContainer_IsDeviceUniquelyIdentifiable: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=79)
DEVPKEY_DeviceContainer_AssociationArray: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=80)
DEVPKEY_DeviceContainer_DeviceDescription1: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=81)
DEVPKEY_DeviceContainer_DeviceDescription2: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=82)
DEVPKEY_DeviceContainer_HasProblem: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=83)
DEVPKEY_DeviceContainer_IsSharedDevice: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=84)
DEVPKEY_DeviceContainer_IsNetworkDevice: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=85)
DEVPKEY_DeviceContainer_IsDefaultDevice: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=86)
DEVPKEY_DeviceContainer_MetadataCabinet: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=87)
DEVPKEY_DeviceContainer_RequiresPairingElevation: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=88)
DEVPKEY_DeviceContainer_ExperienceId: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=89)
DEVPKEY_DeviceContainer_Category: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=90)
DEVPKEY_DeviceContainer_Category_Desc_Singular: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=91)
DEVPKEY_DeviceContainer_Category_Desc_Plural: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=92)
DEVPKEY_DeviceContainer_Category_Icon: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=93)
DEVPKEY_DeviceContainer_CategoryGroup_Desc: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=94)
DEVPKEY_DeviceContainer_CategoryGroup_Icon: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=95)
DEVPKEY_DeviceContainer_PrimaryCategory: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=97)
DEVPKEY_DeviceContainer_UnpairUninstall: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=98)
DEVPKEY_DeviceContainer_RequiresUninstallElevation: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=99)
DEVPKEY_DeviceContainer_DeviceFunctionSubRank: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=100)
DEVPKEY_DeviceContainer_AlwaysShowDeviceAsConnected: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=101)
DEVPKEY_DeviceContainer_ConfigFlags: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=105)
DEVPKEY_DeviceContainer_PrivilegedPackageFamilyNames: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=106)
DEVPKEY_DeviceContainer_CustomPrivilegedPackageFamilyNames: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=107)
DEVPKEY_DeviceContainer_IsRebootRequired: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{78c34fc8-104a-4aca-9ea4-524d52996e57}'), pid=108)
DEVPKEY_DeviceContainer_FriendlyName: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=12288)
DEVPKEY_DeviceContainer_Manufacturer: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8192)
DEVPKEY_DeviceContainer_ModelName: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8194)
DEVPKEY_DeviceContainer_ModelNumber: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{656a3bb3-ecc0-43fd-8477-4ae0404a96cd}'), pid=8195)
DEVPKEY_DeviceContainer_InstallInProgress: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{83da6326-97a6-4088-9453-a1923f573b29}'), pid=9)
DEVPKEY_DevQuery_ObjectType: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{13673f42-a3d6-49f6-b4da-ae46e0c5237c}'), pid=2)
MAX_DEVPROP_TYPE: UInt32 = 25
MAX_DEVPROP_TYPEMOD: UInt32 = 8192
DEVPROP_MASK_TYPE: UInt32 = 4095
DEVPROP_MASK_TYPEMOD: UInt32 = 61440
DEVPROPID_FIRST_USABLE: UInt32 = 2
class DEVPROPCOMPKEY(Structure):
    Key: win32more.Windows.Win32.Foundation.DEVPROPKEY
    Store: win32more.Windows.Win32.Devices.Properties.DEVPROPSTORE
    LocaleName: win32more.Windows.Win32.Foundation.PWSTR
class DEVPROPERTY(Structure):
    CompKey: win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY
    Type: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE
    BufferSize: UInt32
    Buffer: VoidPtr
DEVPROPSTORE = Int32
DEVPROP_STORE_SYSTEM: win32more.Windows.Win32.Devices.Properties.DEVPROPSTORE = 0
DEVPROP_STORE_USER: win32more.Windows.Win32.Devices.Properties.DEVPROPSTORE = 1
DEVPROPTYPE = UInt32
DEVPROP_TYPEMOD_ARRAY: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 4096
DEVPROP_TYPEMOD_LIST: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE = 8192
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
