from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.SystemInformation
NTDDI_WIN2K: UInt32 = 83886080
NTDDI_WINXP: UInt32 = 83951616
NTDDI_WINXPSP2: UInt32 = 83952128
NTDDI_WS03SP1: UInt32 = 84017408
NTDDI_VISTA: UInt32 = 100663296
NTDDI_VISTASP1: UInt32 = 100663552
NTDDI_WIN7: UInt32 = 100728832
NTDDI_WIN8: UInt32 = 100794368
NTDDI_WINBLUE: UInt32 = 100859904
NTDDI_WINTHRESHOLD: UInt32 = 167772160
SYSTEM_CPU_SET_INFORMATION_PARKED: UInt32 = 1
SYSTEM_CPU_SET_INFORMATION_ALLOCATED: UInt32 = 2
SYSTEM_CPU_SET_INFORMATION_ALLOCATED_TO_TARGET_PROCESS: UInt32 = 4
SYSTEM_CPU_SET_INFORMATION_REALTIME: UInt32 = 8
_WIN32_WINNT_NT4: UInt32 = 1024
_WIN32_WINNT_WIN2K: UInt32 = 1280
_WIN32_WINNT_WINXP: UInt32 = 1281
_WIN32_WINNT_WS03: UInt32 = 1282
_WIN32_WINNT_WIN6: UInt32 = 1536
_WIN32_WINNT_VISTA: UInt32 = 1536
_WIN32_WINNT_WS08: UInt32 = 1536
_WIN32_WINNT_LONGHORN: UInt32 = 1536
_WIN32_WINNT_WIN7: UInt32 = 1537
_WIN32_WINNT_WIN8: UInt32 = 1538
_WIN32_WINNT_WINBLUE: UInt32 = 1539
_WIN32_WINNT_WINTHRESHOLD: UInt32 = 2560
_WIN32_WINNT_WIN10: UInt32 = 2560
_WIN32_IE_IE20: UInt32 = 512
_WIN32_IE_IE30: UInt32 = 768
_WIN32_IE_IE302: UInt32 = 770
_WIN32_IE_IE40: UInt32 = 1024
_WIN32_IE_IE401: UInt32 = 1025
_WIN32_IE_IE50: UInt32 = 1280
_WIN32_IE_IE501: UInt32 = 1281
_WIN32_IE_IE55: UInt32 = 1360
_WIN32_IE_IE60: UInt32 = 1536
_WIN32_IE_IE60SP1: UInt32 = 1537
_WIN32_IE_IE60SP2: UInt32 = 1539
_WIN32_IE_IE70: UInt32 = 1792
_WIN32_IE_IE80: UInt32 = 2048
_WIN32_IE_IE90: UInt32 = 2304
_WIN32_IE_IE100: UInt32 = 2560
_WIN32_IE_IE110: UInt32 = 2560
_WIN32_IE_NT4: UInt32 = 512
_WIN32_IE_NT4SP1: UInt32 = 512
_WIN32_IE_NT4SP2: UInt32 = 512
_WIN32_IE_NT4SP3: UInt32 = 770
_WIN32_IE_NT4SP4: UInt32 = 1025
_WIN32_IE_NT4SP5: UInt32 = 1025
_WIN32_IE_NT4SP6: UInt32 = 1280
_WIN32_IE_WIN98: UInt32 = 1025
_WIN32_IE_WIN98SE: UInt32 = 1280
_WIN32_IE_WINME: UInt32 = 1360
_WIN32_IE_WIN2K: UInt32 = 1281
_WIN32_IE_WIN2KSP1: UInt32 = 1281
_WIN32_IE_WIN2KSP2: UInt32 = 1281
_WIN32_IE_WIN2KSP3: UInt32 = 1281
_WIN32_IE_WIN2KSP4: UInt32 = 1281
_WIN32_IE_XP: UInt32 = 1536
_WIN32_IE_XPSP1: UInt32 = 1537
_WIN32_IE_XPSP2: UInt32 = 1539
_WIN32_IE_WS03: UInt32 = 1538
_WIN32_IE_WS03SP1: UInt32 = 1539
_WIN32_IE_WIN6: UInt32 = 1792
_WIN32_IE_LONGHORN: UInt32 = 1792
_WIN32_IE_WIN7: UInt32 = 2048
_WIN32_IE_WIN8: UInt32 = 2560
_WIN32_IE_WINBLUE: UInt32 = 2560
_WIN32_IE_WINTHRESHOLD: UInt32 = 2560
_WIN32_IE_WIN10: UInt32 = 2560
NTDDI_WIN4: UInt32 = 67108864
NTDDI_WIN2KSP1: UInt32 = 83886336
NTDDI_WIN2KSP2: UInt32 = 83886592
NTDDI_WIN2KSP3: UInt32 = 83886848
NTDDI_WIN2KSP4: UInt32 = 83887104
NTDDI_WINXPSP1: UInt32 = 83951872
NTDDI_WINXPSP3: UInt32 = 83952384
NTDDI_WINXPSP4: UInt32 = 83952640
NTDDI_WS03: UInt32 = 84017152
NTDDI_WS03SP2: UInt32 = 84017664
NTDDI_WS03SP3: UInt32 = 84017920
NTDDI_WS03SP4: UInt32 = 84018176
NTDDI_WIN6: UInt32 = 100663296
NTDDI_WIN6SP1: UInt32 = 100663552
NTDDI_WIN6SP2: UInt32 = 100663808
NTDDI_WIN6SP3: UInt32 = 100664064
NTDDI_WIN6SP4: UInt32 = 100664320
NTDDI_VISTASP2: UInt32 = 100663808
NTDDI_VISTASP3: UInt32 = 100664064
NTDDI_VISTASP4: UInt32 = 100664320
NTDDI_LONGHORN: UInt32 = 100663296
NTDDI_WS08: UInt32 = 100663552
NTDDI_WS08SP2: UInt32 = 100663808
NTDDI_WS08SP3: UInt32 = 100664064
NTDDI_WS08SP4: UInt32 = 100664320
NTDDI_WIN10: UInt32 = 167772160
NTDDI_WIN10_TH2: UInt32 = 167772161
NTDDI_WIN10_RS1: UInt32 = 167772162
NTDDI_WIN10_RS2: UInt32 = 167772163
NTDDI_WIN10_RS3: UInt32 = 167772164
NTDDI_WIN10_RS4: UInt32 = 167772165
NTDDI_WIN10_RS5: UInt32 = 167772166
NTDDI_WIN10_19H1: UInt32 = 167772167
NTDDI_WIN10_VB: UInt32 = 167772168
NTDDI_WIN10_MN: UInt32 = 167772169
NTDDI_WIN10_FE: UInt32 = 167772170
NTDDI_WIN10_CO: UInt32 = 167772171
NTDDI_WIN10_NI: UInt32 = 167772172
WDK_NTDDI_VERSION: UInt32 = 167772172
OSVERSION_MASK: UInt32 = 4294901760
SPVERSION_MASK: UInt32 = 65280
SUBVERSION_MASK: UInt32 = 255
NTDDI_VERSION: UInt32 = 167772172
SCEX2_ALT_NETBIOS_NAME: UInt32 = 1
@winfunctype('KERNEL32.dll')
def GlobalMemoryStatusEx(lpBuffer: POINTER(win32more.Windows.Win32.System.SystemInformation.MEMORYSTATUSEX)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetSystemInfo(lpSystemInfo: POINTER(win32more.Windows.Win32.System.SystemInformation.SYSTEM_INFO)) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetSystemTime(lpSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetSystemTimeAsFileTime(lpSystemTimeAsFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetLocalTime(lpSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> Void: ...
@winfunctype('KERNEL32.dll')
def IsUserCetAvailableInEnvironment(UserCetEnvironment: win32more.Windows.Win32.System.SystemInformation.USER_CET_ENVIRONMENT) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetSystemLeapSecondInformation(Enabled: POINTER(win32more.Windows.Win32.Foundation.BOOL), Flags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVersion() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetLocalTime(lpSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetTickCount() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTickCount64() -> UInt64: ...
@winfunctype('KERNEL32.dll')
def GetSystemTimeAdjustment(lpTimeAdjustment: POINTER(UInt32), lpTimeIncrement: POINTER(UInt32), lpTimeAdjustmentDisabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-sysinfo-l1-2-4.dll')
def GetSystemTimeAdjustmentPrecise(lpTimeAdjustment: POINTER(UInt64), lpTimeIncrement: POINTER(UInt64), lpTimeAdjustmentDisabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetSystemDirectoryA(lpBuffer: win32more.Windows.Win32.Foundation.PSTR, uSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetSystemDirectoryW(lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, uSize: UInt32) -> UInt32: ...
GetSystemDirectory = UnicodeAlias('GetSystemDirectoryW')
@winfunctype('KERNEL32.dll')
def GetWindowsDirectoryA(lpBuffer: win32more.Windows.Win32.Foundation.PSTR, uSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetWindowsDirectoryW(lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, uSize: UInt32) -> UInt32: ...
GetWindowsDirectory = UnicodeAlias('GetWindowsDirectoryW')
@winfunctype('KERNEL32.dll')
def GetSystemWindowsDirectoryA(lpBuffer: win32more.Windows.Win32.Foundation.PSTR, uSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetSystemWindowsDirectoryW(lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, uSize: UInt32) -> UInt32: ...
GetSystemWindowsDirectory = UnicodeAlias('GetSystemWindowsDirectoryW')
@winfunctype('KERNEL32.dll')
def GetComputerNameExA(NameType: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, nSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetComputerNameExW(NameType: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, nSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetComputerNameEx = UnicodeAlias('GetComputerNameExW')
@winfunctype('KERNEL32.dll')
def SetComputerNameExW(NameType: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetComputerNameEx = UnicodeAlias('SetComputerNameExW')
@winfunctype('KERNEL32.dll')
def SetSystemTime(lpSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVersionExA(lpVersionInformation: POINTER(win32more.Windows.Win32.System.SystemInformation.OSVERSIONINFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVersionExW(lpVersionInformation: POINTER(win32more.Windows.Win32.System.SystemInformation.OSVERSIONINFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetVersionEx = UnicodeAlias('GetVersionExW')
@winfunctype('KERNEL32.dll')
def GetLogicalProcessorInformation(Buffer: POINTER(win32more.Windows.Win32.System.SystemInformation.SYSTEM_LOGICAL_PROCESSOR_INFORMATION), ReturnedLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetLogicalProcessorInformationEx(RelationshipType: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP, Buffer: POINTER(win32more.Windows.Win32.System.SystemInformation.SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX), ReturnedLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNativeSystemInfo(lpSystemInfo: POINTER(win32more.Windows.Win32.System.SystemInformation.SYSTEM_INFO)) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetSystemTimePreciseAsFileTime(lpSystemTimeAsFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetProductInfo(dwOSMajorVersion: UInt32, dwOSMinorVersion: UInt32, dwSpMajorVersion: UInt32, dwSpMinorVersion: UInt32, pdwReturnedProductType: POINTER(win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VerSetConditionMask(ConditionMask: UInt64, TypeMask: win32more.Windows.Win32.System.SystemInformation.VER_FLAGS, Condition: Byte) -> UInt64: ...
@winfunctype('api-ms-win-core-sysinfo-l1-2-0.dll')
def GetOsSafeBootMode(Flags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumSystemFirmwareTables(FirmwareTableProviderSignature: win32more.Windows.Win32.System.SystemInformation.FIRMWARE_TABLE_PROVIDER, pFirmwareTableEnumBuffer: POINTER(Byte), BufferSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetSystemFirmwareTable(FirmwareTableProviderSignature: win32more.Windows.Win32.System.SystemInformation.FIRMWARE_TABLE_PROVIDER, FirmwareTableID: UInt32, pFirmwareTableBuffer: POINTER(Byte), BufferSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def DnsHostnameToComputerNameExW(Hostname: win32more.Windows.Win32.Foundation.PWSTR, ComputerName: win32more.Windows.Win32.Foundation.PWSTR, nSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetPhysicallyInstalledSystemMemory(TotalMemoryInKilobytes: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetComputerNameEx2W(NameType: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT, Flags: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetSystemTimeAdjustment(dwTimeAdjustment: UInt32, bTimeAdjustmentDisabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-sysinfo-l1-2-4.dll')
def SetSystemTimeAdjustmentPrecise(dwTimeAdjustment: UInt64, bTimeAdjustmentDisabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessorSystemCycleTime(Group: UInt16, Buffer: POINTER(win32more.Windows.Win32.System.SystemInformation.SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION), ReturnedLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-sysinfo-l1-2-3.dll')
def GetOsManufacturingMode(pbEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-sysinfo-l1-2-3.dll')
def GetIntegratedDisplaySize(sizeInInches: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def SetComputerNameA(lpComputerName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetComputerNameW(lpComputerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetComputerName = UnicodeAlias('SetComputerNameW')
@winfunctype('KERNEL32.dll')
def SetComputerNameExA(NameType: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT, lpBuffer: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-sysinfo-l1-2-6.dll')
def GetDeveloperDriveEnablementState() -> win32more.Windows.Win32.System.SystemInformation.DEVELOPER_DRIVE_ENABLEMENT_STATE: ...
@winfunctype('KERNEL32.dll')
def GetSystemCpuSetInformation(Information: POINTER(win32more.Windows.Win32.System.SystemInformation.SYSTEM_CPU_SET_INFORMATION), BufferLength: UInt32, ReturnedLength: POINTER(UInt32), Process: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetSystemWow64DirectoryA(lpBuffer: win32more.Windows.Win32.Foundation.PSTR, uSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetSystemWow64DirectoryW(lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, uSize: UInt32) -> UInt32: ...
GetSystemWow64Directory = UnicodeAlias('GetSystemWow64DirectoryW')
@winfunctype('api-ms-win-core-wow64-l1-1-1.dll')
def GetSystemWow64Directory2A(lpBuffer: win32more.Windows.Win32.Foundation.PSTR, uSize: UInt32, ImageFileMachineType: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE) -> UInt32: ...
@winfunctype('api-ms-win-core-wow64-l1-1-1.dll')
def GetSystemWow64Directory2W(lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, uSize: UInt32, ImageFileMachineType: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE) -> UInt32: ...
GetSystemWow64Directory2 = UnicodeAlias('GetSystemWow64Directory2W')
@winfunctype('KERNEL32.dll')
def IsWow64GuestMachineSupported(WowGuestMachine: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE, MachineIsSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ntdll.dll')
def RtlGetProductInfo(OSMajorVersion: UInt32, OSMinorVersion: UInt32, SpMajorVersion: UInt32, SpMinorVersion: UInt32, ReturnedProductType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('ntdll.dll')
def RtlOsDeploymentState(Flags: UInt32) -> win32more.Windows.Win32.System.SystemInformation.OS_DEPLOYEMENT_STATE_VALUES: ...
@winfunctype('ntdllk.dll')
def RtlGetSystemGlobalData(DataId: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID, Buffer: VoidPtr, Size: UInt32) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlGetDeviceFamilyInfoEnum(pullUAPInfo: POINTER(UInt64), pulDeviceFamily: POINTER(win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM), pulDeviceForm: POINTER(win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM)) -> Void: ...
@winfunctype('ntdll.dll')
def RtlConvertDeviceFamilyInfoToString(pulDeviceFamilyBufferSize: POINTER(UInt32), pulDeviceFormBufferSize: POINTER(UInt32), DeviceFamily: win32more.Windows.Win32.Foundation.PWSTR, DeviceForm: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlSwitchedVVI(VersionInfo: POINTER(win32more.Windows.Win32.System.SystemInformation.OSVERSIONINFOEXW), TypeMask: UInt32, ConditionMask: UInt64) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GlobalMemoryStatus(lpBuffer: POINTER(win32more.Windows.Win32.System.SystemInformation.MEMORYSTATUS)) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetSystemDEPPolicy() -> win32more.Windows.Win32.System.SystemInformation.DEP_SYSTEM_POLICY_TYPE: ...
@winfunctype('KERNEL32.dll')
def GetFirmwareType(FirmwareType: POINTER(win32more.Windows.Win32.System.SystemInformation.FIRMWARE_TYPE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VerifyVersionInfoA(lpVersionInformation: POINTER(win32more.Windows.Win32.System.SystemInformation.OSVERSIONINFOEXA), dwTypeMask: win32more.Windows.Win32.System.SystemInformation.VER_FLAGS, dwlConditionMask: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VerifyVersionInfoW(lpVersionInformation: POINTER(win32more.Windows.Win32.System.SystemInformation.OSVERSIONINFOEXW), dwTypeMask: win32more.Windows.Win32.System.SystemInformation.VER_FLAGS, dwlConditionMask: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
VerifyVersionInfo = UnicodeAlias('VerifyVersionInfoW')
class CACHE_DESCRIPTOR(Structure):
    Level: Byte
    Associativity: Byte
    LineSize: UInt16
    Size: UInt32
    Type: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_CACHE_TYPE
class CACHE_RELATIONSHIP(Structure):
    Level: Byte
    Associativity: Byte
    LineSize: UInt16
    CacheSize: UInt32
    Type: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_CACHE_TYPE
    Reserved: Byte * 18
    GroupCount: UInt16
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        GroupMask: win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY
        GroupMasks: win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY * 1
COMPUTER_NAME_FORMAT = Int32
ComputerNameNetBIOS: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT = 0
ComputerNameDnsHostname: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT = 1
ComputerNameDnsDomain: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT = 2
ComputerNameDnsFullyQualified: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT = 3
ComputerNamePhysicalNetBIOS: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT = 4
ComputerNamePhysicalDnsHostname: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT = 5
ComputerNamePhysicalDnsDomain: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT = 6
ComputerNamePhysicalDnsFullyQualified: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT = 7
ComputerNameMax: win32more.Windows.Win32.System.SystemInformation.COMPUTER_NAME_FORMAT = 8
CPU_SET_INFORMATION_TYPE = Int32
CpuSetInformation: win32more.Windows.Win32.System.SystemInformation.CPU_SET_INFORMATION_TYPE = 0
DEP_SYSTEM_POLICY_TYPE = Int32
DEPPolicyAlwaysOff: win32more.Windows.Win32.System.SystemInformation.DEP_SYSTEM_POLICY_TYPE = 0
DEPPolicyAlwaysOn: win32more.Windows.Win32.System.SystemInformation.DEP_SYSTEM_POLICY_TYPE = 1
DEPPolicyOptIn: win32more.Windows.Win32.System.SystemInformation.DEP_SYSTEM_POLICY_TYPE = 2
DEPPolicyOptOut: win32more.Windows.Win32.System.SystemInformation.DEP_SYSTEM_POLICY_TYPE = 3
DEPTotalPolicyCount: win32more.Windows.Win32.System.SystemInformation.DEP_SYSTEM_POLICY_TYPE = 4
DEVELOPER_DRIVE_ENABLEMENT_STATE = Int32
DeveloperDriveEnablementStateError: win32more.Windows.Win32.System.SystemInformation.DEVELOPER_DRIVE_ENABLEMENT_STATE = 0
DeveloperDriveEnabled: win32more.Windows.Win32.System.SystemInformation.DEVELOPER_DRIVE_ENABLEMENT_STATE = 1
DeveloperDriveDisabledBySystemPolicy: win32more.Windows.Win32.System.SystemInformation.DEVELOPER_DRIVE_ENABLEMENT_STATE = 2
DeveloperDriveDisabledByGroupPolicy: win32more.Windows.Win32.System.SystemInformation.DEVELOPER_DRIVE_ENABLEMENT_STATE = 3
DEVICEFAMILYDEVICEFORM = UInt32
DEVICEFAMILYDEVICEFORM_UNKNOWN: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 0
DEVICEFAMILYDEVICEFORM_PHONE: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 1
DEVICEFAMILYDEVICEFORM_TABLET: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 2
DEVICEFAMILYDEVICEFORM_DESKTOP: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 3
DEVICEFAMILYDEVICEFORM_NOTEBOOK: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 4
DEVICEFAMILYDEVICEFORM_CONVERTIBLE: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 5
DEVICEFAMILYDEVICEFORM_DETACHABLE: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 6
DEVICEFAMILYDEVICEFORM_ALLINONE: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 7
DEVICEFAMILYDEVICEFORM_STICKPC: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 8
DEVICEFAMILYDEVICEFORM_PUCK: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 9
DEVICEFAMILYDEVICEFORM_LARGESCREEN: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 10
DEVICEFAMILYDEVICEFORM_HMD: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 11
DEVICEFAMILYDEVICEFORM_INDUSTRY_HANDHELD: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 12
DEVICEFAMILYDEVICEFORM_INDUSTRY_TABLET: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 13
DEVICEFAMILYDEVICEFORM_BANKING: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 14
DEVICEFAMILYDEVICEFORM_BUILDING_AUTOMATION: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 15
DEVICEFAMILYDEVICEFORM_DIGITAL_SIGNAGE: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 16
DEVICEFAMILYDEVICEFORM_GAMING: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 17
DEVICEFAMILYDEVICEFORM_HOME_AUTOMATION: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 18
DEVICEFAMILYDEVICEFORM_INDUSTRIAL_AUTOMATION: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 19
DEVICEFAMILYDEVICEFORM_KIOSK: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 20
DEVICEFAMILYDEVICEFORM_MAKER_BOARD: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 21
DEVICEFAMILYDEVICEFORM_MEDICAL: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 22
DEVICEFAMILYDEVICEFORM_NETWORKING: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 23
DEVICEFAMILYDEVICEFORM_POINT_OF_SERVICE: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 24
DEVICEFAMILYDEVICEFORM_PRINTING: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 25
DEVICEFAMILYDEVICEFORM_THIN_CLIENT: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 26
DEVICEFAMILYDEVICEFORM_TOY: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 27
DEVICEFAMILYDEVICEFORM_VENDING: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 28
DEVICEFAMILYDEVICEFORM_INDUSTRY_OTHER: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 29
DEVICEFAMILYDEVICEFORM_XBOX_ONE: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 30
DEVICEFAMILYDEVICEFORM_XBOX_ONE_S: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 31
DEVICEFAMILYDEVICEFORM_XBOX_ONE_X: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 32
DEVICEFAMILYDEVICEFORM_XBOX_ONE_X_DEVKIT: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 33
DEVICEFAMILYDEVICEFORM_XBOX_SERIES_X: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 34
DEVICEFAMILYDEVICEFORM_XBOX_SERIES_X_DEVKIT: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 35
DEVICEFAMILYDEVICEFORM_XBOX_SERIES_S: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 36
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_01: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 37
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_02: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 38
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_03: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 39
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_04: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 40
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_05: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 41
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_06: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 42
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_07: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 43
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_08: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 44
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_09: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 45
DEVICEFAMILYDEVICEFORM_MAX: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYDEVICEFORM = 45
DEVICEFAMILYINFOENUM = UInt32
DEVICEFAMILYINFOENUM_UAP: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 0
DEVICEFAMILYINFOENUM_WINDOWS_8X: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 1
DEVICEFAMILYINFOENUM_WINDOWS_PHONE_8X: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 2
DEVICEFAMILYINFOENUM_DESKTOP: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 3
DEVICEFAMILYINFOENUM_MOBILE: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 4
DEVICEFAMILYINFOENUM_XBOX: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 5
DEVICEFAMILYINFOENUM_TEAM: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 6
DEVICEFAMILYINFOENUM_IOT: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 7
DEVICEFAMILYINFOENUM_IOT_HEADLESS: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 8
DEVICEFAMILYINFOENUM_SERVER: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 9
DEVICEFAMILYINFOENUM_HOLOGRAPHIC: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 10
DEVICEFAMILYINFOENUM_XBOXSRA: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 11
DEVICEFAMILYINFOENUM_XBOXERA: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 12
DEVICEFAMILYINFOENUM_SERVER_NANO: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 13
DEVICEFAMILYINFOENUM_8828080: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 14
DEVICEFAMILYINFOENUM_7067329: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 15
DEVICEFAMILYINFOENUM_WINDOWS_CORE: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 16
DEVICEFAMILYINFOENUM_WINDOWS_CORE_HEADLESS: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 17
DEVICEFAMILYINFOENUM_MAX: win32more.Windows.Win32.System.SystemInformation.DEVICEFAMILYINFOENUM = 17
FIRMWARE_TABLE_PROVIDER = UInt32
ACPI: win32more.Windows.Win32.System.SystemInformation.FIRMWARE_TABLE_PROVIDER = 1094930505
FIRM: win32more.Windows.Win32.System.SystemInformation.FIRMWARE_TABLE_PROVIDER = 1179210317
RSMB: win32more.Windows.Win32.System.SystemInformation.FIRMWARE_TABLE_PROVIDER = 1381190978
FIRMWARE_TYPE = Int32
FirmwareTypeUnknown: win32more.Windows.Win32.System.SystemInformation.FIRMWARE_TYPE = 0
FirmwareTypeBios: win32more.Windows.Win32.System.SystemInformation.FIRMWARE_TYPE = 1
FirmwareTypeUefi: win32more.Windows.Win32.System.SystemInformation.FIRMWARE_TYPE = 2
FirmwareTypeMax: win32more.Windows.Win32.System.SystemInformation.FIRMWARE_TYPE = 3
class GROUP_AFFINITY(Structure):
    Mask: UIntPtr
    Group: UInt16
    Reserved: UInt16 * 3
class GROUP_RELATIONSHIP(Structure):
    MaximumGroupCount: UInt16
    ActiveGroupCount: UInt16
    Reserved: Byte * 20
    GroupInfo: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_GROUP_INFO * 1
IMAGE_FILE_MACHINE = UInt16
IMAGE_FILE_MACHINE_AXP64: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 644
IMAGE_FILE_MACHINE_I386: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 332
IMAGE_FILE_MACHINE_IA64: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 512
IMAGE_FILE_MACHINE_AMD64: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 34404
IMAGE_FILE_MACHINE_UNKNOWN: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 0
IMAGE_FILE_MACHINE_TARGET_HOST: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 1
IMAGE_FILE_MACHINE_R3000: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 354
IMAGE_FILE_MACHINE_R4000: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 358
IMAGE_FILE_MACHINE_R10000: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 360
IMAGE_FILE_MACHINE_WCEMIPSV2: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 361
IMAGE_FILE_MACHINE_ALPHA: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 388
IMAGE_FILE_MACHINE_SH3: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 418
IMAGE_FILE_MACHINE_SH3DSP: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 419
IMAGE_FILE_MACHINE_SH3E: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 420
IMAGE_FILE_MACHINE_SH4: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 422
IMAGE_FILE_MACHINE_SH5: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 424
IMAGE_FILE_MACHINE_ARM: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 448
IMAGE_FILE_MACHINE_THUMB: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 450
IMAGE_FILE_MACHINE_ARMNT: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 452
IMAGE_FILE_MACHINE_AM33: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 467
IMAGE_FILE_MACHINE_POWERPC: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 496
IMAGE_FILE_MACHINE_POWERPCFP: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 497
IMAGE_FILE_MACHINE_MIPS16: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 614
IMAGE_FILE_MACHINE_ALPHA64: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 644
IMAGE_FILE_MACHINE_MIPSFPU: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 870
IMAGE_FILE_MACHINE_MIPSFPU16: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 1126
IMAGE_FILE_MACHINE_TRICORE: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 1312
IMAGE_FILE_MACHINE_CEF: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 3311
IMAGE_FILE_MACHINE_EBC: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 3772
IMAGE_FILE_MACHINE_M32R: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 36929
IMAGE_FILE_MACHINE_ARM64: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 43620
IMAGE_FILE_MACHINE_CEE: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE = 49390
LOGICAL_PROCESSOR_RELATIONSHIP = Int32
RelationProcessorCore: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP = 0
RelationNumaNode: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP = 1
RelationCache: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP = 2
RelationProcessorPackage: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP = 3
RelationGroup: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP = 4
RelationProcessorDie: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP = 5
RelationNumaNodeEx: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP = 6
RelationProcessorModule: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP = 7
RelationAll: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP = 65535
class MEMORYSTATUS(Structure):
    dwLength: UInt32
    dwMemoryLoad: UInt32
    dwTotalPhys: UIntPtr
    dwAvailPhys: UIntPtr
    dwTotalPageFile: UIntPtr
    dwAvailPageFile: UIntPtr
    dwTotalVirtual: UIntPtr
    dwAvailVirtual: UIntPtr
class MEMORYSTATUSEX(Structure):
    dwLength: UInt32
    dwMemoryLoad: UInt32
    ullTotalPhys: UInt64
    ullAvailPhys: UInt64
    ullTotalPageFile: UInt64
    ullAvailPageFile: UInt64
    ullTotalVirtual: UInt64
    ullAvailVirtual: UInt64
    ullAvailExtendedVirtual: UInt64
class NUMA_NODE_RELATIONSHIP(Structure):
    NodeNumber: UInt32
    Reserved: Byte * 18
    GroupCount: UInt16
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        GroupMask: win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY
        GroupMasks: win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY * 1
class OSVERSIONINFOA(Structure):
    dwOSVersionInfoSize: UInt32
    dwMajorVersion: UInt32
    dwMinorVersion: UInt32
    dwBuildNumber: UInt32
    dwPlatformId: UInt32
    szCSDVersion: win32more.Windows.Win32.Foundation.CHAR * 128
class OSVERSIONINFOEXA(Structure):
    dwOSVersionInfoSize: UInt32
    dwMajorVersion: UInt32
    dwMinorVersion: UInt32
    dwBuildNumber: UInt32
    dwPlatformId: UInt32
    szCSDVersion: win32more.Windows.Win32.Foundation.CHAR * 128
    wServicePackMajor: UInt16
    wServicePackMinor: UInt16
    wSuiteMask: UInt16
    wProductType: Byte
    wReserved: Byte
class OSVERSIONINFOEXW(Structure):
    dwOSVersionInfoSize: UInt32
    dwMajorVersion: UInt32
    dwMinorVersion: UInt32
    dwBuildNumber: UInt32
    dwPlatformId: UInt32
    szCSDVersion: Char * 128
    wServicePackMajor: UInt16
    wServicePackMinor: UInt16
    wSuiteMask: UInt16
    wProductType: Byte
    wReserved: Byte
OSVERSIONINFOEX = UnicodeAlias('OSVERSIONINFOEXW')
class OSVERSIONINFOW(Structure):
    dwOSVersionInfoSize: UInt32
    dwMajorVersion: UInt32
    dwMinorVersion: UInt32
    dwBuildNumber: UInt32
    dwPlatformId: UInt32
    szCSDVersion: Char * 128
OSVERSIONINFO = UnicodeAlias('OSVERSIONINFOW')
OS_DEPLOYEMENT_STATE_VALUES = Int32
OS_DEPLOYMENT_STANDARD: win32more.Windows.Win32.System.SystemInformation.OS_DEPLOYEMENT_STATE_VALUES = 1
OS_DEPLOYMENT_COMPACT: win32more.Windows.Win32.System.SystemInformation.OS_DEPLOYEMENT_STATE_VALUES = 2
OS_PRODUCT_TYPE = UInt32
PRODUCT_BUSINESS: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 6
PRODUCT_BUSINESS_N: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 16
PRODUCT_CLUSTER_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 18
PRODUCT_CLUSTER_SERVER_V: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 64
PRODUCT_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 101
PRODUCT_CORE_COUNTRYSPECIFIC: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 99
PRODUCT_CORE_N: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 98
PRODUCT_CORE_SINGLELANGUAGE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 100
PRODUCT_DATACENTER_EVALUATION_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 80
PRODUCT_DATACENTER_A_SERVER_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 145
PRODUCT_STANDARD_A_SERVER_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 146
PRODUCT_DATACENTER_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 8
PRODUCT_DATACENTER_SERVER_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 12
PRODUCT_DATACENTER_SERVER_CORE_V: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 39
PRODUCT_DATACENTER_SERVER_V: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 37
PRODUCT_EDUCATION: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 121
PRODUCT_EDUCATION_N: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 122
PRODUCT_ENTERPRISE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 4
PRODUCT_ENTERPRISE_E: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 70
PRODUCT_ENTERPRISE_EVALUATION: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 72
PRODUCT_ENTERPRISE_N: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 27
PRODUCT_ENTERPRISE_N_EVALUATION: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 84
PRODUCT_ENTERPRISE_S: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 125
PRODUCT_ENTERPRISE_S_EVALUATION: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 129
PRODUCT_ENTERPRISE_S_N: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 126
PRODUCT_ENTERPRISE_S_N_EVALUATION: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 130
PRODUCT_ENTERPRISE_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 10
PRODUCT_ENTERPRISE_SERVER_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 14
PRODUCT_ENTERPRISE_SERVER_CORE_V: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 41
PRODUCT_ENTERPRISE_SERVER_IA64: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 15
PRODUCT_ENTERPRISE_SERVER_V: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 38
PRODUCT_ESSENTIALBUSINESS_SERVER_ADDL: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 60
PRODUCT_ESSENTIALBUSINESS_SERVER_ADDLSVC: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 62
PRODUCT_ESSENTIALBUSINESS_SERVER_MGMT: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 59
PRODUCT_ESSENTIALBUSINESS_SERVER_MGMTSVC: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 61
PRODUCT_HOME_BASIC: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 2
PRODUCT_HOME_BASIC_E: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 67
PRODUCT_HOME_BASIC_N: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 5
PRODUCT_HOME_PREMIUM: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 3
PRODUCT_HOME_PREMIUM_E: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 68
PRODUCT_HOME_PREMIUM_N: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 26
PRODUCT_HOME_PREMIUM_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 34
PRODUCT_HOME_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 19
PRODUCT_HYPERV: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 42
PRODUCT_IOTUAP: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 123
PRODUCT_IOTUAPCOMMERCIAL: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 131
PRODUCT_MEDIUMBUSINESS_SERVER_MANAGEMENT: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 30
PRODUCT_MEDIUMBUSINESS_SERVER_MESSAGING: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 32
PRODUCT_MEDIUMBUSINESS_SERVER_SECURITY: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 31
PRODUCT_MOBILE_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 104
PRODUCT_MOBILE_ENTERPRISE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 133
PRODUCT_MULTIPOINT_PREMIUM_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 77
PRODUCT_MULTIPOINT_STANDARD_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 76
PRODUCT_PRO_WORKSTATION: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 161
PRODUCT_PRO_WORKSTATION_N: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 162
PRODUCT_PROFESSIONAL: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 48
PRODUCT_PROFESSIONAL_E: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 69
PRODUCT_PROFESSIONAL_N: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 49
PRODUCT_PROFESSIONAL_WMC: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 103
PRODUCT_SB_SOLUTION_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 50
PRODUCT_SB_SOLUTION_SERVER_EM: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 54
PRODUCT_SERVER_FOR_SB_SOLUTIONS: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 51
PRODUCT_SERVER_FOR_SB_SOLUTIONS_EM: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 55
PRODUCT_SERVER_FOR_SMALLBUSINESS: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 24
PRODUCT_SERVER_FOR_SMALLBUSINESS_V: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 35
PRODUCT_SERVER_FOUNDATION: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 33
PRODUCT_SMALLBUSINESS_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 9
PRODUCT_SMALLBUSINESS_SERVER_PREMIUM: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 25
PRODUCT_SMALLBUSINESS_SERVER_PREMIUM_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 63
PRODUCT_SOLUTION_EMBEDDEDSERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 56
PRODUCT_STANDARD_EVALUATION_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 79
PRODUCT_STANDARD_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 7
PRODUCT_STANDARD_SERVER_CORE_: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 13
PRODUCT_STANDARD_SERVER_CORE_V: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 40
PRODUCT_STANDARD_SERVER_V: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 36
PRODUCT_STANDARD_SERVER_SOLUTIONS: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 52
PRODUCT_STANDARD_SERVER_SOLUTIONS_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 53
PRODUCT_STARTER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 11
PRODUCT_STARTER_E: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 66
PRODUCT_STARTER_N: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 47
PRODUCT_STORAGE_ENTERPRISE_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 23
PRODUCT_STORAGE_ENTERPRISE_SERVER_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 46
PRODUCT_STORAGE_EXPRESS_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 20
PRODUCT_STORAGE_EXPRESS_SERVER_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 43
PRODUCT_STORAGE_STANDARD_EVALUATION_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 96
PRODUCT_STORAGE_STANDARD_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 21
PRODUCT_STORAGE_STANDARD_SERVER_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 44
PRODUCT_STORAGE_WORKGROUP_EVALUATION_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 95
PRODUCT_STORAGE_WORKGROUP_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 22
PRODUCT_STORAGE_WORKGROUP_SERVER_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 45
PRODUCT_ULTIMATE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 1
PRODUCT_ULTIMATE_E: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 71
PRODUCT_ULTIMATE_N: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 28
PRODUCT_UNDEFINED: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 0
PRODUCT_WEB_SERVER: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 17
PRODUCT_WEB_SERVER_CORE: win32more.Windows.Win32.System.SystemInformation.OS_PRODUCT_TYPE = 29
@winfunctype_pointer
def PGET_SYSTEM_WOW64_DIRECTORY_A(lpBuffer: win32more.Windows.Win32.Foundation.PSTR, uSize: UInt32) -> UInt32: ...
@winfunctype_pointer
def PGET_SYSTEM_WOW64_DIRECTORY_W(lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, uSize: UInt32) -> UInt32: ...
PGET_SYSTEM_WOW64_DIRECTORY = UnicodeAlias('PGET_SYSTEM_WOW64_DIRECTORY_W')
PROCESSOR_ARCHITECTURE = UInt16
PROCESSOR_ARCHITECTURE_INTEL: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 0
PROCESSOR_ARCHITECTURE_MIPS: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 1
PROCESSOR_ARCHITECTURE_ALPHA: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 2
PROCESSOR_ARCHITECTURE_PPC: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 3
PROCESSOR_ARCHITECTURE_SHX: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 4
PROCESSOR_ARCHITECTURE_ARM: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 5
PROCESSOR_ARCHITECTURE_IA64: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 6
PROCESSOR_ARCHITECTURE_ALPHA64: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 7
PROCESSOR_ARCHITECTURE_MSIL: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 8
PROCESSOR_ARCHITECTURE_AMD64: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 9
PROCESSOR_ARCHITECTURE_IA32_ON_WIN64: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 10
PROCESSOR_ARCHITECTURE_NEUTRAL: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 11
PROCESSOR_ARCHITECTURE_ARM64: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 12
PROCESSOR_ARCHITECTURE_ARM32_ON_WIN64: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 13
PROCESSOR_ARCHITECTURE_IA32_ON_ARM64: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 14
PROCESSOR_ARCHITECTURE_UNKNOWN: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE = 65535
PROCESSOR_CACHE_TYPE = Int32
CacheUnified: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_CACHE_TYPE = 0
CacheInstruction: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_CACHE_TYPE = 1
CacheData: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_CACHE_TYPE = 2
CacheTrace: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_CACHE_TYPE = 3
class PROCESSOR_GROUP_INFO(Structure):
    MaximumProcessorCount: Byte
    ActiveProcessorCount: Byte
    Reserved: Byte * 38
    ActiveProcessorMask: UIntPtr
class PROCESSOR_RELATIONSHIP(Structure):
    Flags: Byte
    EfficiencyClass: Byte
    Reserved: Byte * 20
    GroupCount: UInt16
    GroupMask: win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY * 1
RTL_SYSTEM_GLOBAL_DATA_ID = Int32
GlobalDataIdUnknown: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 0
GlobalDataIdRngSeedVersion: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 1
GlobalDataIdInterruptTime: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 2
GlobalDataIdTimeZoneBias: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 3
GlobalDataIdImageNumberLow: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 4
GlobalDataIdImageNumberHigh: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 5
GlobalDataIdTimeZoneId: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 6
GlobalDataIdNtMajorVersion: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 7
GlobalDataIdNtMinorVersion: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 8
GlobalDataIdSystemExpirationDate: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 9
GlobalDataIdKdDebuggerEnabled: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 10
GlobalDataIdCyclesPerYield: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 11
GlobalDataIdSafeBootMode: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 12
GlobalDataIdLastSystemRITEventTickCount: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 13
GlobalDataIdConsoleSharedDataFlags: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 14
GlobalDataIdNtSystemRootDrive: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 15
GlobalDataIdQpcShift: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 16
GlobalDataIdQpcBypassEnabled: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 17
GlobalDataIdQpcData: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 18
GlobalDataIdQpcBias: win32more.Windows.Win32.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID = 19
class SYSTEM_CPU_SET_INFORMATION(Structure):
    Size: UInt32
    Type: win32more.Windows.Win32.System.SystemInformation.CPU_SET_INFORMATION_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        CpuSet: _CpuSet_e__Struct
        class _CpuSet_e__Struct(Structure):
            Id: UInt32
            Group: UInt16
            LogicalProcessorIndex: Byte
            CoreIndex: Byte
            LastLevelCacheIndex: Byte
            NumaNodeIndex: Byte
            EfficiencyClass: Byte
            Anonymous1: _Anonymous1_e__Union
            Anonymous2: _Anonymous2_e__Union
            AllocationTag: UInt64
            class _Anonymous1_e__Union(Union):
                AllFlags: Byte
                Anonymous: _Anonymous_e__Struct
                class _Anonymous_e__Struct(Structure):
                    Parked: Annotated[Byte, 1]
                    Allocated: Annotated[Byte, 1]
                    AllocatedToTargetProcess: Annotated[Byte, 1]
                    RealTime: Annotated[Byte, 1]
                    ReservedFlags: Annotated[Byte, 4]
            class _Anonymous2_e__Union(Union):
                Reserved: UInt32
                SchedulingClass: Byte
class SYSTEM_INFO(Structure):
    Anonymous: _Anonymous_e__Union
    dwPageSize: UInt32
    lpMinimumApplicationAddress: VoidPtr
    lpMaximumApplicationAddress: VoidPtr
    dwActiveProcessorMask: UIntPtr
    dwNumberOfProcessors: UInt32
    dwProcessorType: UInt32
    dwAllocationGranularity: UInt32
    wProcessorLevel: UInt16
    wProcessorRevision: UInt16
    class _Anonymous_e__Union(Union):
        dwOemId: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            wProcessorArchitecture: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE
            wReserved: UInt16
class SYSTEM_LOGICAL_PROCESSOR_INFORMATION(Structure):
    ProcessorMask: UIntPtr
    Relationship: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ProcessorCore: _ProcessorCore_e__Struct
        NumaNode: _NumaNode_e__Struct
        Cache: win32more.Windows.Win32.System.SystemInformation.CACHE_DESCRIPTOR
        Reserved: UInt64 * 2
        class _ProcessorCore_e__Struct(Structure):
            Flags: Byte
        class _NumaNode_e__Struct(Structure):
            NodeNumber: UInt32
class SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX(Structure):
    Relationship: win32more.Windows.Win32.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP
    Size: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Processor: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_RELATIONSHIP
        NumaNode: win32more.Windows.Win32.System.SystemInformation.NUMA_NODE_RELATIONSHIP
        Cache: win32more.Windows.Win32.System.SystemInformation.CACHE_RELATIONSHIP
        Group: win32more.Windows.Win32.System.SystemInformation.GROUP_RELATIONSHIP
class SYSTEM_POOL_ZEROING_INFORMATION(Structure):
    PoolZeroingSupportPresent: win32more.Windows.Win32.Foundation.BOOLEAN
class SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION(Structure):
    CycleTime: UInt64
class SYSTEM_SUPPORTED_PROCESSOR_ARCHITECTURES_INFORMATION(Structure):
    Machine: Annotated[UInt32, 16]
    KernelMode: Annotated[UInt32, 1]
    UserMode: Annotated[UInt32, 1]
    Native: Annotated[UInt32, 1]
    Process: Annotated[UInt32, 1]
    WoW64Container: Annotated[UInt32, 1]
    ReservedZero0: Annotated[UInt32, 11]
USER_CET_ENVIRONMENT = UInt32
USER_CET_ENVIRONMENT_WIN32_PROCESS: win32more.Windows.Win32.System.SystemInformation.USER_CET_ENVIRONMENT = 0
USER_CET_ENVIRONMENT_SGX2_ENCLAVE: win32more.Windows.Win32.System.SystemInformation.USER_CET_ENVIRONMENT = 2
USER_CET_ENVIRONMENT_VBS_ENCLAVE: win32more.Windows.Win32.System.SystemInformation.USER_CET_ENVIRONMENT = 16
USER_CET_ENVIRONMENT_VBS_BASIC_ENCLAVE: win32more.Windows.Win32.System.SystemInformation.USER_CET_ENVIRONMENT = 17
VER_FLAGS = UInt32
VER_MINORVERSION: win32more.Windows.Win32.System.SystemInformation.VER_FLAGS = 1
VER_MAJORVERSION: win32more.Windows.Win32.System.SystemInformation.VER_FLAGS = 2
VER_BUILDNUMBER: win32more.Windows.Win32.System.SystemInformation.VER_FLAGS = 4
VER_PLATFORMID: win32more.Windows.Win32.System.SystemInformation.VER_FLAGS = 8
VER_SERVICEPACKMINOR: win32more.Windows.Win32.System.SystemInformation.VER_FLAGS = 16
VER_SERVICEPACKMAJOR: win32more.Windows.Win32.System.SystemInformation.VER_FLAGS = 32
VER_SUITENAME: win32more.Windows.Win32.System.SystemInformation.VER_FLAGS = 64
VER_PRODUCT_TYPE: win32more.Windows.Win32.System.SystemInformation.VER_FLAGS = 128


make_ready(__name__)
