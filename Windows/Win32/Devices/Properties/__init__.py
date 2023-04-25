from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Devices.Properties
import Windows.Win32.Foundation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def DEVPKEY_DeviceInterface_Autoplay_Silent():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('434dd28f-9e75-450a-9a-b9-ff-61-e6-18-ba-d0'), pid=2)
def DEVPKEY_NAME():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=10)
def DEVPKEY_Device_DeviceDesc():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=2)
def DEVPKEY_Device_HardwareIds():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=3)
def DEVPKEY_Device_CompatibleIds():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=4)
def DEVPKEY_Device_Service():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=6)
def DEVPKEY_Device_Class():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=9)
def DEVPKEY_Device_ClassGuid():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=10)
def DEVPKEY_Device_Driver():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=11)
def DEVPKEY_Device_ConfigFlags():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=12)
def DEVPKEY_Device_Manufacturer():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=13)
def DEVPKEY_Device_FriendlyName():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=14)
def DEVPKEY_Device_LocationInfo():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=15)
def DEVPKEY_Device_PDOName():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=16)
def DEVPKEY_Device_Capabilities():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=17)
def DEVPKEY_Device_UINumber():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=18)
def DEVPKEY_Device_UpperFilters():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=19)
def DEVPKEY_Device_LowerFilters():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=20)
def DEVPKEY_Device_BusTypeGuid():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=21)
def DEVPKEY_Device_LegacyBusType():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=22)
def DEVPKEY_Device_BusNumber():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=23)
def DEVPKEY_Device_EnumeratorName():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=24)
def DEVPKEY_Device_Security():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=25)
def DEVPKEY_Device_SecuritySDS():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=26)
def DEVPKEY_Device_DevType():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=27)
def DEVPKEY_Device_Exclusive():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=28)
def DEVPKEY_Device_Characteristics():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=29)
def DEVPKEY_Device_Address():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=30)
def DEVPKEY_Device_UINumberDescFormat():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=31)
def DEVPKEY_Device_PowerData():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=32)
def DEVPKEY_Device_RemovalPolicy():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=33)
def DEVPKEY_Device_RemovalPolicyDefault():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=34)
def DEVPKEY_Device_RemovalPolicyOverride():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=35)
def DEVPKEY_Device_InstallState():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=36)
def DEVPKEY_Device_LocationPaths():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=37)
def DEVPKEY_Device_BaseContainerId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=38)
def DEVPKEY_Device_InstanceId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=256)
def DEVPKEY_Device_DevNodeStatus():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=2)
def DEVPKEY_Device_ProblemCode():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=3)
def DEVPKEY_Device_EjectionRelations():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=4)
def DEVPKEY_Device_RemovalRelations():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=5)
def DEVPKEY_Device_PowerRelations():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=6)
def DEVPKEY_Device_BusRelations():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=7)
def DEVPKEY_Device_Parent():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=8)
def DEVPKEY_Device_Children():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=9)
def DEVPKEY_Device_Siblings():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=10)
def DEVPKEY_Device_TransportRelations():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=11)
def DEVPKEY_Device_ProblemStatus():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=12)
def DEVPKEY_Device_Reported():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('80497100-8c73-48b9-aa-d9-ce-38-7e-19-c5-6e'), pid=2)
def DEVPKEY_Device_Legacy():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('80497100-8c73-48b9-aa-d9-ce-38-7e-19-c5-6e'), pid=3)
def DEVPKEY_Device_ContainerId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('8c7ed206-3f8a-4827-b3-ab-ae-9e-1f-ae-fc-6c'), pid=2)
def DEVPKEY_Device_InLocalMachineContainer():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('8c7ed206-3f8a-4827-b3-ab-ae-9e-1f-ae-fc-6c'), pid=4)
def DEVPKEY_Device_Model():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=39)
def DEVPKEY_Device_ModelId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=2)
def DEVPKEY_Device_FriendlyNameAttributes():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=3)
def DEVPKEY_Device_ManufacturerAttributes():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=4)
def DEVPKEY_Device_PresenceNotForDevice():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=5)
def DEVPKEY_Device_SignalStrength():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=6)
def DEVPKEY_Device_IsAssociateableByUserAction():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=7)
def DEVPKEY_Device_ShowInUninstallUI():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=8)
def DEVPKEY_Device_Numa_Proximity_Domain():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=1)
def DEVPKEY_Device_DHP_Rebalance_Policy():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=2)
def DEVPKEY_Device_Numa_Node():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=3)
def DEVPKEY_Device_BusReportedDeviceDesc():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=4)
def DEVPKEY_Device_IsPresent():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=5)
def DEVPKEY_Device_HasProblem():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=6)
def DEVPKEY_Device_ConfigurationId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=7)
def DEVPKEY_Device_ReportedDeviceIdsHash():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=8)
def DEVPKEY_Device_PhysicalDeviceLocation():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=9)
def DEVPKEY_Device_BiosDeviceName():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=10)
def DEVPKEY_Device_DriverProblemDesc():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=11)
def DEVPKEY_Device_DebuggerSafe():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=12)
def DEVPKEY_Device_PostInstallInProgress():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=13)
def DEVPKEY_Device_Stack():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=14)
def DEVPKEY_Device_ExtendedConfigurationIds():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=15)
def DEVPKEY_Device_IsRebootRequired():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=16)
def DEVPKEY_Device_FirmwareDate():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=17)
def DEVPKEY_Device_FirmwareVersion():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=18)
def DEVPKEY_Device_FirmwareRevision():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=19)
def DEVPKEY_Device_DependencyProviders():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=20)
def DEVPKEY_Device_DependencyDependents():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=21)
def DEVPKEY_Device_SoftRestartSupported():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=22)
def DEVPKEY_Device_ExtendedAddress():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=23)
def DEVPKEY_Device_AssignedToGuest():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=24)
def DEVPKEY_Device_CreatorProcessId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=25)
def DEVPKEY_Device_FirmwareVendor():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=26)
def DEVPKEY_Device_SessionId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=6)
def DEVPKEY_Device_InstallDate():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=100)
def DEVPKEY_Device_FirstInstallDate():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=101)
def DEVPKEY_Device_LastArrivalDate():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=102)
def DEVPKEY_Device_LastRemovalDate():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=103)
def DEVPKEY_Device_DriverDate():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=2)
def DEVPKEY_Device_DriverVersion():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=3)
def DEVPKEY_Device_DriverDesc():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=4)
def DEVPKEY_Device_DriverInfPath():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=5)
def DEVPKEY_Device_DriverInfSection():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=6)
def DEVPKEY_Device_DriverInfSectionExt():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=7)
def DEVPKEY_Device_MatchingDeviceId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=8)
def DEVPKEY_Device_DriverProvider():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=9)
def DEVPKEY_Device_DriverPropPageProvider():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=10)
def DEVPKEY_Device_DriverCoInstallers():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=11)
def DEVPKEY_Device_ResourcePickerTags():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=12)
def DEVPKEY_Device_ResourcePickerExceptions():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=13)
def DEVPKEY_Device_DriverRank():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=14)
def DEVPKEY_Device_DriverLogoLevel():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=15)
def DEVPKEY_Device_NoConnectSound():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=17)
def DEVPKEY_Device_GenericDriverInstalled():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=18)
def DEVPKEY_Device_AdditionalSoftwareRequested():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=19)
def DEVPKEY_Device_SafeRemovalRequired():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('afd97640-86a3-4210-b6-7c-28-9c-41-aa-be-55'), pid=2)
def DEVPKEY_Device_SafeRemovalRequiredOverride():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('afd97640-86a3-4210-b6-7c-28-9c-41-aa-be-55'), pid=3)
def DEVPKEY_DrvPkg_Model():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=2)
def DEVPKEY_DrvPkg_VendorWebSite():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=3)
def DEVPKEY_DrvPkg_DetailedDescription():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=4)
def DEVPKEY_DrvPkg_DocumentationLink():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=5)
def DEVPKEY_DrvPkg_Icon():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=6)
def DEVPKEY_DrvPkg_BrandingIcon():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=7)
def DEVPKEY_DeviceClass_UpperFilters():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=19)
def DEVPKEY_DeviceClass_LowerFilters():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=20)
def DEVPKEY_DeviceClass_Security():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=25)
def DEVPKEY_DeviceClass_SecuritySDS():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=26)
def DEVPKEY_DeviceClass_DevType():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=27)
def DEVPKEY_DeviceClass_Exclusive():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=28)
def DEVPKEY_DeviceClass_Characteristics():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=29)
def DEVPKEY_DeviceClass_Name():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=2)
def DEVPKEY_DeviceClass_ClassName():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=3)
def DEVPKEY_DeviceClass_Icon():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=4)
def DEVPKEY_DeviceClass_ClassInstaller():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=5)
def DEVPKEY_DeviceClass_PropPageProvider():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=6)
def DEVPKEY_DeviceClass_NoInstallClass():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=7)
def DEVPKEY_DeviceClass_NoDisplayClass():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=8)
def DEVPKEY_DeviceClass_SilentInstall():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=9)
def DEVPKEY_DeviceClass_NoUseClass():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=10)
def DEVPKEY_DeviceClass_DefaultService():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=11)
def DEVPKEY_DeviceClass_IconPath():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=12)
def DEVPKEY_DeviceClass_DHPRebalanceOptOut():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('d14d3ef3-66cf-4ba2-9d-38-0d-db-37-ab-47-01'), pid=2)
def DEVPKEY_DeviceClass_ClassCoInstallers():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('713d1703-a2e2-49f5-92-14-56-47-2e-f3-da-5c'), pid=2)
def DEVPKEY_DeviceInterface_FriendlyName():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=2)
def DEVPKEY_DeviceInterface_Enabled():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=3)
def DEVPKEY_DeviceInterface_ClassGuid():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=4)
def DEVPKEY_DeviceInterface_ReferenceString():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=5)
def DEVPKEY_DeviceInterface_Restricted():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=6)
def DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=8)
def DEVPKEY_DeviceInterface_SchematicName():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=9)
def DEVPKEY_DeviceInterfaceClass_DefaultInterface():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('14c83a99-0b3f-44b7-be-4c-a1-78-d3-99-05-64'), pid=2)
def DEVPKEY_DeviceInterfaceClass_Name():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('14c83a99-0b3f-44b7-be-4c-a1-78-d3-99-05-64'), pid=3)
def DEVPKEY_DeviceContainer_Address():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=51)
def DEVPKEY_DeviceContainer_DiscoveryMethod():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=52)
def DEVPKEY_DeviceContainer_IsEncrypted():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=53)
def DEVPKEY_DeviceContainer_IsAuthenticated():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=54)
def DEVPKEY_DeviceContainer_IsConnected():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=55)
def DEVPKEY_DeviceContainer_IsPaired():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=56)
def DEVPKEY_DeviceContainer_Icon():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=57)
def DEVPKEY_DeviceContainer_Version():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=65)
def DEVPKEY_DeviceContainer_Last_Seen():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=66)
def DEVPKEY_DeviceContainer_Last_Connected():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=67)
def DEVPKEY_DeviceContainer_IsShowInDisconnectedState():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=68)
def DEVPKEY_DeviceContainer_IsLocalMachine():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=70)
def DEVPKEY_DeviceContainer_MetadataPath():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=71)
def DEVPKEY_DeviceContainer_IsMetadataSearchInProgress():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=72)
def DEVPKEY_DeviceContainer_MetadataChecksum():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=73)
def DEVPKEY_DeviceContainer_IsNotInterestingForDisplay():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=74)
def DEVPKEY_DeviceContainer_LaunchDeviceStageOnDeviceConnect():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=76)
def DEVPKEY_DeviceContainer_LaunchDeviceStageFromExplorer():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=77)
def DEVPKEY_DeviceContainer_BaselineExperienceId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=78)
def DEVPKEY_DeviceContainer_IsDeviceUniquelyIdentifiable():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=79)
def DEVPKEY_DeviceContainer_AssociationArray():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=80)
def DEVPKEY_DeviceContainer_DeviceDescription1():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=81)
def DEVPKEY_DeviceContainer_DeviceDescription2():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=82)
def DEVPKEY_DeviceContainer_HasProblem():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=83)
def DEVPKEY_DeviceContainer_IsSharedDevice():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=84)
def DEVPKEY_DeviceContainer_IsNetworkDevice():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=85)
def DEVPKEY_DeviceContainer_IsDefaultDevice():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=86)
def DEVPKEY_DeviceContainer_MetadataCabinet():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=87)
def DEVPKEY_DeviceContainer_RequiresPairingElevation():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=88)
def DEVPKEY_DeviceContainer_ExperienceId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=89)
def DEVPKEY_DeviceContainer_Category():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=90)
def DEVPKEY_DeviceContainer_Category_Desc_Singular():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=91)
def DEVPKEY_DeviceContainer_Category_Desc_Plural():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=92)
def DEVPKEY_DeviceContainer_Category_Icon():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=93)
def DEVPKEY_DeviceContainer_CategoryGroup_Desc():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=94)
def DEVPKEY_DeviceContainer_CategoryGroup_Icon():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=95)
def DEVPKEY_DeviceContainer_PrimaryCategory():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=97)
def DEVPKEY_DeviceContainer_UnpairUninstall():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=98)
def DEVPKEY_DeviceContainer_RequiresUninstallElevation():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=99)
def DEVPKEY_DeviceContainer_DeviceFunctionSubRank():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=100)
def DEVPKEY_DeviceContainer_AlwaysShowDeviceAsConnected():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=101)
def DEVPKEY_DeviceContainer_ConfigFlags():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=105)
def DEVPKEY_DeviceContainer_PrivilegedPackageFamilyNames():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=106)
def DEVPKEY_DeviceContainer_CustomPrivilegedPackageFamilyNames():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=107)
def DEVPKEY_DeviceContainer_IsRebootRequired():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=108)
def DEVPKEY_DeviceContainer_FriendlyName():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12288)
def DEVPKEY_DeviceContainer_Manufacturer():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8192)
def DEVPKEY_DeviceContainer_ModelName():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8194)
def DEVPKEY_DeviceContainer_ModelNumber():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8195)
def DEVPKEY_DeviceContainer_InstallInProgress():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=9)
def DEVPKEY_DevQuery_ObjectType():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('13673f42-a3d6-49f6-b4-da-ae-46-e0-c5-23-7c'), pid=2)
DEVPROP_TYPEMOD_ARRAY: UInt32 = 4096
DEVPROP_TYPEMOD_LIST: UInt32 = 8192
MAX_DEVPROP_TYPE: UInt32 = 25
MAX_DEVPROP_TYPEMOD: UInt32 = 8192
DEVPROP_MASK_TYPE: UInt32 = 4095
DEVPROP_MASK_TYPEMOD: UInt32 = 61440
DEVPROPID_FIRST_USABLE: UInt32 = 2
class DEVPROPCOMPKEY(EasyCastStructure):
    Key: Windows.Win32.Devices.Properties.DEVPROPKEY
    Store: Windows.Win32.Devices.Properties.DEVPROPSTORE
    LocaleName: Windows.Win32.Foundation.PWSTR
class DEVPROPERTY(EasyCastStructure):
    CompKey: Windows.Win32.Devices.Properties.DEVPROPCOMPKEY
    Type: Windows.Win32.Devices.Properties.DEVPROPTYPE
    BufferSize: UInt32
    Buffer: c_void_p
class DEVPROPKEY(EasyCastStructure):
    fmtid: Guid
    pid: UInt32
DEVPROPSTORE = Int32
DEVPROP_STORE_SYSTEM: DEVPROPSTORE = 0
DEVPROP_STORE_USER: DEVPROPSTORE = 1
DEVPROPTYPE = UInt32
DEVPROP_TYPE_EMPTY: DEVPROPTYPE = 0
DEVPROP_TYPE_NULL: DEVPROPTYPE = 1
DEVPROP_TYPE_SBYTE: DEVPROPTYPE = 2
DEVPROP_TYPE_BYTE: DEVPROPTYPE = 3
DEVPROP_TYPE_INT16: DEVPROPTYPE = 4
DEVPROP_TYPE_UINT16: DEVPROPTYPE = 5
DEVPROP_TYPE_INT32: DEVPROPTYPE = 6
DEVPROP_TYPE_UINT32: DEVPROPTYPE = 7
DEVPROP_TYPE_INT64: DEVPROPTYPE = 8
DEVPROP_TYPE_UINT64: DEVPROPTYPE = 9
DEVPROP_TYPE_FLOAT: DEVPROPTYPE = 10
DEVPROP_TYPE_DOUBLE: DEVPROPTYPE = 11
DEVPROP_TYPE_DECIMAL: DEVPROPTYPE = 12
DEVPROP_TYPE_GUID: DEVPROPTYPE = 13
DEVPROP_TYPE_CURRENCY: DEVPROPTYPE = 14
DEVPROP_TYPE_DATE: DEVPROPTYPE = 15
DEVPROP_TYPE_FILETIME: DEVPROPTYPE = 16
DEVPROP_TYPE_BOOLEAN: DEVPROPTYPE = 17
DEVPROP_TYPE_STRING: DEVPROPTYPE = 18
DEVPROP_TYPE_STRING_LIST: DEVPROPTYPE = 8210
DEVPROP_TYPE_SECURITY_DESCRIPTOR: DEVPROPTYPE = 19
DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING: DEVPROPTYPE = 20
DEVPROP_TYPE_DEVPROPKEY: DEVPROPTYPE = 21
DEVPROP_TYPE_DEVPROPTYPE: DEVPROPTYPE = 22
DEVPROP_TYPE_BINARY: DEVPROPTYPE = 4099
DEVPROP_TYPE_ERROR: DEVPROPTYPE = 23
DEVPROP_TYPE_NTSTATUS: DEVPROPTYPE = 24
DEVPROP_TYPE_STRING_INDIRECT: DEVPROPTYPE = 25
make_head(_module, 'DEVPKEY_DeviceInterface_Autoplay_Silent')
make_head(_module, 'DEVPKEY_NAME')
make_head(_module, 'DEVPKEY_Device_DeviceDesc')
make_head(_module, 'DEVPKEY_Device_HardwareIds')
make_head(_module, 'DEVPKEY_Device_CompatibleIds')
make_head(_module, 'DEVPKEY_Device_Service')
make_head(_module, 'DEVPKEY_Device_Class')
make_head(_module, 'DEVPKEY_Device_ClassGuid')
make_head(_module, 'DEVPKEY_Device_Driver')
make_head(_module, 'DEVPKEY_Device_ConfigFlags')
make_head(_module, 'DEVPKEY_Device_Manufacturer')
make_head(_module, 'DEVPKEY_Device_FriendlyName')
make_head(_module, 'DEVPKEY_Device_LocationInfo')
make_head(_module, 'DEVPKEY_Device_PDOName')
make_head(_module, 'DEVPKEY_Device_Capabilities')
make_head(_module, 'DEVPKEY_Device_UINumber')
make_head(_module, 'DEVPKEY_Device_UpperFilters')
make_head(_module, 'DEVPKEY_Device_LowerFilters')
make_head(_module, 'DEVPKEY_Device_BusTypeGuid')
make_head(_module, 'DEVPKEY_Device_LegacyBusType')
make_head(_module, 'DEVPKEY_Device_BusNumber')
make_head(_module, 'DEVPKEY_Device_EnumeratorName')
make_head(_module, 'DEVPKEY_Device_Security')
make_head(_module, 'DEVPKEY_Device_SecuritySDS')
make_head(_module, 'DEVPKEY_Device_DevType')
make_head(_module, 'DEVPKEY_Device_Exclusive')
make_head(_module, 'DEVPKEY_Device_Characteristics')
make_head(_module, 'DEVPKEY_Device_Address')
make_head(_module, 'DEVPKEY_Device_UINumberDescFormat')
make_head(_module, 'DEVPKEY_Device_PowerData')
make_head(_module, 'DEVPKEY_Device_RemovalPolicy')
make_head(_module, 'DEVPKEY_Device_RemovalPolicyDefault')
make_head(_module, 'DEVPKEY_Device_RemovalPolicyOverride')
make_head(_module, 'DEVPKEY_Device_InstallState')
make_head(_module, 'DEVPKEY_Device_LocationPaths')
make_head(_module, 'DEVPKEY_Device_BaseContainerId')
make_head(_module, 'DEVPKEY_Device_InstanceId')
make_head(_module, 'DEVPKEY_Device_DevNodeStatus')
make_head(_module, 'DEVPKEY_Device_ProblemCode')
make_head(_module, 'DEVPKEY_Device_EjectionRelations')
make_head(_module, 'DEVPKEY_Device_RemovalRelations')
make_head(_module, 'DEVPKEY_Device_PowerRelations')
make_head(_module, 'DEVPKEY_Device_BusRelations')
make_head(_module, 'DEVPKEY_Device_Parent')
make_head(_module, 'DEVPKEY_Device_Children')
make_head(_module, 'DEVPKEY_Device_Siblings')
make_head(_module, 'DEVPKEY_Device_TransportRelations')
make_head(_module, 'DEVPKEY_Device_ProblemStatus')
make_head(_module, 'DEVPKEY_Device_Reported')
make_head(_module, 'DEVPKEY_Device_Legacy')
make_head(_module, 'DEVPKEY_Device_ContainerId')
make_head(_module, 'DEVPKEY_Device_InLocalMachineContainer')
make_head(_module, 'DEVPKEY_Device_Model')
make_head(_module, 'DEVPKEY_Device_ModelId')
make_head(_module, 'DEVPKEY_Device_FriendlyNameAttributes')
make_head(_module, 'DEVPKEY_Device_ManufacturerAttributes')
make_head(_module, 'DEVPKEY_Device_PresenceNotForDevice')
make_head(_module, 'DEVPKEY_Device_SignalStrength')
make_head(_module, 'DEVPKEY_Device_IsAssociateableByUserAction')
make_head(_module, 'DEVPKEY_Device_ShowInUninstallUI')
make_head(_module, 'DEVPKEY_Device_Numa_Proximity_Domain')
make_head(_module, 'DEVPKEY_Device_DHP_Rebalance_Policy')
make_head(_module, 'DEVPKEY_Device_Numa_Node')
make_head(_module, 'DEVPKEY_Device_BusReportedDeviceDesc')
make_head(_module, 'DEVPKEY_Device_IsPresent')
make_head(_module, 'DEVPKEY_Device_HasProblem')
make_head(_module, 'DEVPKEY_Device_ConfigurationId')
make_head(_module, 'DEVPKEY_Device_ReportedDeviceIdsHash')
make_head(_module, 'DEVPKEY_Device_PhysicalDeviceLocation')
make_head(_module, 'DEVPKEY_Device_BiosDeviceName')
make_head(_module, 'DEVPKEY_Device_DriverProblemDesc')
make_head(_module, 'DEVPKEY_Device_DebuggerSafe')
make_head(_module, 'DEVPKEY_Device_PostInstallInProgress')
make_head(_module, 'DEVPKEY_Device_Stack')
make_head(_module, 'DEVPKEY_Device_ExtendedConfigurationIds')
make_head(_module, 'DEVPKEY_Device_IsRebootRequired')
make_head(_module, 'DEVPKEY_Device_FirmwareDate')
make_head(_module, 'DEVPKEY_Device_FirmwareVersion')
make_head(_module, 'DEVPKEY_Device_FirmwareRevision')
make_head(_module, 'DEVPKEY_Device_DependencyProviders')
make_head(_module, 'DEVPKEY_Device_DependencyDependents')
make_head(_module, 'DEVPKEY_Device_SoftRestartSupported')
make_head(_module, 'DEVPKEY_Device_ExtendedAddress')
make_head(_module, 'DEVPKEY_Device_AssignedToGuest')
make_head(_module, 'DEVPKEY_Device_CreatorProcessId')
make_head(_module, 'DEVPKEY_Device_FirmwareVendor')
make_head(_module, 'DEVPKEY_Device_SessionId')
make_head(_module, 'DEVPKEY_Device_InstallDate')
make_head(_module, 'DEVPKEY_Device_FirstInstallDate')
make_head(_module, 'DEVPKEY_Device_LastArrivalDate')
make_head(_module, 'DEVPKEY_Device_LastRemovalDate')
make_head(_module, 'DEVPKEY_Device_DriverDate')
make_head(_module, 'DEVPKEY_Device_DriverVersion')
make_head(_module, 'DEVPKEY_Device_DriverDesc')
make_head(_module, 'DEVPKEY_Device_DriverInfPath')
make_head(_module, 'DEVPKEY_Device_DriverInfSection')
make_head(_module, 'DEVPKEY_Device_DriverInfSectionExt')
make_head(_module, 'DEVPKEY_Device_MatchingDeviceId')
make_head(_module, 'DEVPKEY_Device_DriverProvider')
make_head(_module, 'DEVPKEY_Device_DriverPropPageProvider')
make_head(_module, 'DEVPKEY_Device_DriverCoInstallers')
make_head(_module, 'DEVPKEY_Device_ResourcePickerTags')
make_head(_module, 'DEVPKEY_Device_ResourcePickerExceptions')
make_head(_module, 'DEVPKEY_Device_DriverRank')
make_head(_module, 'DEVPKEY_Device_DriverLogoLevel')
make_head(_module, 'DEVPKEY_Device_NoConnectSound')
make_head(_module, 'DEVPKEY_Device_GenericDriverInstalled')
make_head(_module, 'DEVPKEY_Device_AdditionalSoftwareRequested')
make_head(_module, 'DEVPKEY_Device_SafeRemovalRequired')
make_head(_module, 'DEVPKEY_Device_SafeRemovalRequiredOverride')
make_head(_module, 'DEVPKEY_DrvPkg_Model')
make_head(_module, 'DEVPKEY_DrvPkg_VendorWebSite')
make_head(_module, 'DEVPKEY_DrvPkg_DetailedDescription')
make_head(_module, 'DEVPKEY_DrvPkg_DocumentationLink')
make_head(_module, 'DEVPKEY_DrvPkg_Icon')
make_head(_module, 'DEVPKEY_DrvPkg_BrandingIcon')
make_head(_module, 'DEVPKEY_DeviceClass_UpperFilters')
make_head(_module, 'DEVPKEY_DeviceClass_LowerFilters')
make_head(_module, 'DEVPKEY_DeviceClass_Security')
make_head(_module, 'DEVPKEY_DeviceClass_SecuritySDS')
make_head(_module, 'DEVPKEY_DeviceClass_DevType')
make_head(_module, 'DEVPKEY_DeviceClass_Exclusive')
make_head(_module, 'DEVPKEY_DeviceClass_Characteristics')
make_head(_module, 'DEVPKEY_DeviceClass_Name')
make_head(_module, 'DEVPKEY_DeviceClass_ClassName')
make_head(_module, 'DEVPKEY_DeviceClass_Icon')
make_head(_module, 'DEVPKEY_DeviceClass_ClassInstaller')
make_head(_module, 'DEVPKEY_DeviceClass_PropPageProvider')
make_head(_module, 'DEVPKEY_DeviceClass_NoInstallClass')
make_head(_module, 'DEVPKEY_DeviceClass_NoDisplayClass')
make_head(_module, 'DEVPKEY_DeviceClass_SilentInstall')
make_head(_module, 'DEVPKEY_DeviceClass_NoUseClass')
make_head(_module, 'DEVPKEY_DeviceClass_DefaultService')
make_head(_module, 'DEVPKEY_DeviceClass_IconPath')
make_head(_module, 'DEVPKEY_DeviceClass_DHPRebalanceOptOut')
make_head(_module, 'DEVPKEY_DeviceClass_ClassCoInstallers')
make_head(_module, 'DEVPKEY_DeviceInterface_FriendlyName')
make_head(_module, 'DEVPKEY_DeviceInterface_Enabled')
make_head(_module, 'DEVPKEY_DeviceInterface_ClassGuid')
make_head(_module, 'DEVPKEY_DeviceInterface_ReferenceString')
make_head(_module, 'DEVPKEY_DeviceInterface_Restricted')
make_head(_module, 'DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities')
make_head(_module, 'DEVPKEY_DeviceInterface_SchematicName')
make_head(_module, 'DEVPKEY_DeviceInterfaceClass_DefaultInterface')
make_head(_module, 'DEVPKEY_DeviceInterfaceClass_Name')
make_head(_module, 'DEVPKEY_DeviceContainer_Address')
make_head(_module, 'DEVPKEY_DeviceContainer_DiscoveryMethod')
make_head(_module, 'DEVPKEY_DeviceContainer_IsEncrypted')
make_head(_module, 'DEVPKEY_DeviceContainer_IsAuthenticated')
make_head(_module, 'DEVPKEY_DeviceContainer_IsConnected')
make_head(_module, 'DEVPKEY_DeviceContainer_IsPaired')
make_head(_module, 'DEVPKEY_DeviceContainer_Icon')
make_head(_module, 'DEVPKEY_DeviceContainer_Version')
make_head(_module, 'DEVPKEY_DeviceContainer_Last_Seen')
make_head(_module, 'DEVPKEY_DeviceContainer_Last_Connected')
make_head(_module, 'DEVPKEY_DeviceContainer_IsShowInDisconnectedState')
make_head(_module, 'DEVPKEY_DeviceContainer_IsLocalMachine')
make_head(_module, 'DEVPKEY_DeviceContainer_MetadataPath')
make_head(_module, 'DEVPKEY_DeviceContainer_IsMetadataSearchInProgress')
make_head(_module, 'DEVPKEY_DeviceContainer_MetadataChecksum')
make_head(_module, 'DEVPKEY_DeviceContainer_IsNotInterestingForDisplay')
make_head(_module, 'DEVPKEY_DeviceContainer_LaunchDeviceStageOnDeviceConnect')
make_head(_module, 'DEVPKEY_DeviceContainer_LaunchDeviceStageFromExplorer')
make_head(_module, 'DEVPKEY_DeviceContainer_BaselineExperienceId')
make_head(_module, 'DEVPKEY_DeviceContainer_IsDeviceUniquelyIdentifiable')
make_head(_module, 'DEVPKEY_DeviceContainer_AssociationArray')
make_head(_module, 'DEVPKEY_DeviceContainer_DeviceDescription1')
make_head(_module, 'DEVPKEY_DeviceContainer_DeviceDescription2')
make_head(_module, 'DEVPKEY_DeviceContainer_HasProblem')
make_head(_module, 'DEVPKEY_DeviceContainer_IsSharedDevice')
make_head(_module, 'DEVPKEY_DeviceContainer_IsNetworkDevice')
make_head(_module, 'DEVPKEY_DeviceContainer_IsDefaultDevice')
make_head(_module, 'DEVPKEY_DeviceContainer_MetadataCabinet')
make_head(_module, 'DEVPKEY_DeviceContainer_RequiresPairingElevation')
make_head(_module, 'DEVPKEY_DeviceContainer_ExperienceId')
make_head(_module, 'DEVPKEY_DeviceContainer_Category')
make_head(_module, 'DEVPKEY_DeviceContainer_Category_Desc_Singular')
make_head(_module, 'DEVPKEY_DeviceContainer_Category_Desc_Plural')
make_head(_module, 'DEVPKEY_DeviceContainer_Category_Icon')
make_head(_module, 'DEVPKEY_DeviceContainer_CategoryGroup_Desc')
make_head(_module, 'DEVPKEY_DeviceContainer_CategoryGroup_Icon')
make_head(_module, 'DEVPKEY_DeviceContainer_PrimaryCategory')
make_head(_module, 'DEVPKEY_DeviceContainer_UnpairUninstall')
make_head(_module, 'DEVPKEY_DeviceContainer_RequiresUninstallElevation')
make_head(_module, 'DEVPKEY_DeviceContainer_DeviceFunctionSubRank')
make_head(_module, 'DEVPKEY_DeviceContainer_AlwaysShowDeviceAsConnected')
make_head(_module, 'DEVPKEY_DeviceContainer_ConfigFlags')
make_head(_module, 'DEVPKEY_DeviceContainer_PrivilegedPackageFamilyNames')
make_head(_module, 'DEVPKEY_DeviceContainer_CustomPrivilegedPackageFamilyNames')
make_head(_module, 'DEVPKEY_DeviceContainer_IsRebootRequired')
make_head(_module, 'DEVPKEY_DeviceContainer_FriendlyName')
make_head(_module, 'DEVPKEY_DeviceContainer_Manufacturer')
make_head(_module, 'DEVPKEY_DeviceContainer_ModelName')
make_head(_module, 'DEVPKEY_DeviceContainer_ModelNumber')
make_head(_module, 'DEVPKEY_DeviceContainer_InstallInProgress')
make_head(_module, 'DEVPKEY_DevQuery_ObjectType')
make_head(_module, 'DEVPROPCOMPKEY')
make_head(_module, 'DEVPROPERTY')
make_head(_module, 'DEVPROPKEY')
