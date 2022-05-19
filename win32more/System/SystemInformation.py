from win32more import *
import win32more.Foundation
import win32more.System.Diagnostics.Debug
import win32more.System.SystemInformation

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
NTDDI_WIN2K = 83886080
NTDDI_WINXP = 83951616
NTDDI_WINXPSP2 = 83952128
NTDDI_WS03SP1 = 84017408
NTDDI_VISTA = 100663296
NTDDI_VISTASP1 = 100663552
NTDDI_WIN7 = 100728832
NTDDI_WIN8 = 100794368
NTDDI_WINBLUE = 100859904
NTDDI_WINTHRESHOLD = 167772160
SYSTEM_CPU_SET_INFORMATION_PARKED = 1
SYSTEM_CPU_SET_INFORMATION_ALLOCATED = 2
SYSTEM_CPU_SET_INFORMATION_ALLOCATED_TO_TARGET_PROCESS = 4
SYSTEM_CPU_SET_INFORMATION_REALTIME = 8
_WIN32_WINNT_NT4 = 1024
_WIN32_WINNT_WIN2K = 1280
_WIN32_WINNT_WINXP = 1281
_WIN32_WINNT_WS03 = 1282
_WIN32_WINNT_WIN6 = 1536
_WIN32_WINNT_VISTA = 1536
_WIN32_WINNT_WS08 = 1536
_WIN32_WINNT_LONGHORN = 1536
_WIN32_WINNT_WIN7 = 1537
_WIN32_WINNT_WIN8 = 1538
_WIN32_WINNT_WINBLUE = 1539
_WIN32_WINNT_WINTHRESHOLD = 2560
_WIN32_WINNT_WIN10 = 2560
_WIN32_IE_IE20 = 512
_WIN32_IE_IE30 = 768
_WIN32_IE_IE302 = 770
_WIN32_IE_IE40 = 1024
_WIN32_IE_IE401 = 1025
_WIN32_IE_IE50 = 1280
_WIN32_IE_IE501 = 1281
_WIN32_IE_IE55 = 1360
_WIN32_IE_IE60 = 1536
_WIN32_IE_IE60SP1 = 1537
_WIN32_IE_IE60SP2 = 1539
_WIN32_IE_IE70 = 1792
_WIN32_IE_IE80 = 2048
_WIN32_IE_IE90 = 2304
_WIN32_IE_IE100 = 2560
_WIN32_IE_IE110 = 2560
_WIN32_IE_NT4 = 512
_WIN32_IE_NT4SP1 = 512
_WIN32_IE_NT4SP2 = 512
_WIN32_IE_NT4SP3 = 770
_WIN32_IE_NT4SP4 = 1025
_WIN32_IE_NT4SP5 = 1025
_WIN32_IE_NT4SP6 = 1280
_WIN32_IE_WIN98 = 1025
_WIN32_IE_WIN98SE = 1280
_WIN32_IE_WINME = 1360
_WIN32_IE_WIN2K = 1281
_WIN32_IE_WIN2KSP1 = 1281
_WIN32_IE_WIN2KSP2 = 1281
_WIN32_IE_WIN2KSP3 = 1281
_WIN32_IE_WIN2KSP4 = 1281
_WIN32_IE_XP = 1536
_WIN32_IE_XPSP1 = 1537
_WIN32_IE_XPSP2 = 1539
_WIN32_IE_WS03 = 1538
_WIN32_IE_WS03SP1 = 1539
_WIN32_IE_WIN6 = 1792
_WIN32_IE_LONGHORN = 1792
_WIN32_IE_WIN7 = 2048
_WIN32_IE_WIN8 = 2560
_WIN32_IE_WINBLUE = 2560
_WIN32_IE_WINTHRESHOLD = 2560
_WIN32_IE_WIN10 = 2560
NTDDI_WIN4 = 67108864
NTDDI_WIN2KSP1 = 83886336
NTDDI_WIN2KSP2 = 83886592
NTDDI_WIN2KSP3 = 83886848
NTDDI_WIN2KSP4 = 83887104
NTDDI_WINXPSP1 = 83951872
NTDDI_WINXPSP3 = 83952384
NTDDI_WINXPSP4 = 83952640
NTDDI_WS03 = 84017152
NTDDI_WS03SP2 = 84017664
NTDDI_WS03SP3 = 84017920
NTDDI_WS03SP4 = 84018176
NTDDI_WIN6 = 100663296
NTDDI_WIN6SP1 = 100663552
NTDDI_WIN6SP2 = 100663808
NTDDI_WIN6SP3 = 100664064
NTDDI_WIN6SP4 = 100664320
NTDDI_VISTASP2 = 100663808
NTDDI_VISTASP3 = 100664064
NTDDI_VISTASP4 = 100664320
NTDDI_LONGHORN = 100663296
NTDDI_WS08 = 100663552
NTDDI_WS08SP2 = 100663808
NTDDI_WS08SP3 = 100664064
NTDDI_WS08SP4 = 100664320
NTDDI_WIN10 = 167772160
NTDDI_WIN10_TH2 = 167772161
NTDDI_WIN10_RS1 = 167772162
NTDDI_WIN10_RS2 = 167772163
NTDDI_WIN10_RS3 = 167772164
NTDDI_WIN10_RS4 = 167772165
NTDDI_WIN10_RS5 = 167772166
NTDDI_WIN10_19H1 = 167772167
NTDDI_WIN10_VB = 167772168
NTDDI_WIN10_MN = 167772169
NTDDI_WIN10_FE = 167772170
NTDDI_WIN10_CO = 167772171
WDK_NTDDI_VERSION = 167772171
OSVERSION_MASK = 4294901760
SPVERSION_MASK = 65280
SUBVERSION_MASK = 255
NTDDI_VERSION = 167772171
SCEX2_ALT_NETBIOS_NAME = 1
VER_FLAGS = UInt32
VER_MINORVERSION = 1
VER_MAJORVERSION = 2
VER_BUILDNUMBER = 4
VER_PLATFORMID = 8
VER_SERVICEPACKMINOR = 16
VER_SERVICEPACKMAJOR = 32
VER_SUITENAME = 64
VER_PRODUCT_TYPE = 128
FIRMWARE_TABLE_PROVIDER = UInt32
ACPI = 1094930505
FIRM = 1179210317
RSMB = 1381190978
USER_CET_ENVIRONMENT = UInt32
USER_CET_ENVIRONMENT_WIN32_PROCESS = 0
USER_CET_ENVIRONMENT_SGX2_ENCLAVE = 2
USER_CET_ENVIRONMENT_VBS_ENCLAVE = 16
USER_CET_ENVIRONMENT_VBS_BASIC_ENCLAVE = 17
OS_PRODUCT_TYPE = UInt32
PRODUCT_BUSINESS = 6
PRODUCT_BUSINESS_N = 16
PRODUCT_CLUSTER_SERVER = 18
PRODUCT_CLUSTER_SERVER_V = 64
PRODUCT_CORE = 101
PRODUCT_CORE_COUNTRYSPECIFIC = 99
PRODUCT_CORE_N = 98
PRODUCT_CORE_SINGLELANGUAGE = 100
PRODUCT_DATACENTER_EVALUATION_SERVER = 80
PRODUCT_DATACENTER_A_SERVER_CORE = 145
PRODUCT_STANDARD_A_SERVER_CORE = 146
PRODUCT_DATACENTER_SERVER = 8
PRODUCT_DATACENTER_SERVER_CORE = 12
PRODUCT_DATACENTER_SERVER_CORE_V = 39
PRODUCT_DATACENTER_SERVER_V = 37
PRODUCT_EDUCATION = 121
PRODUCT_EDUCATION_N = 122
PRODUCT_ENTERPRISE = 4
PRODUCT_ENTERPRISE_E = 70
PRODUCT_ENTERPRISE_EVALUATION = 72
PRODUCT_ENTERPRISE_N = 27
PRODUCT_ENTERPRISE_N_EVALUATION = 84
PRODUCT_ENTERPRISE_S = 125
PRODUCT_ENTERPRISE_S_EVALUATION = 129
PRODUCT_ENTERPRISE_S_N = 126
PRODUCT_ENTERPRISE_S_N_EVALUATION = 130
PRODUCT_ENTERPRISE_SERVER = 10
PRODUCT_ENTERPRISE_SERVER_CORE = 14
PRODUCT_ENTERPRISE_SERVER_CORE_V = 41
PRODUCT_ENTERPRISE_SERVER_IA64 = 15
PRODUCT_ENTERPRISE_SERVER_V = 38
PRODUCT_ESSENTIALBUSINESS_SERVER_ADDL = 60
PRODUCT_ESSENTIALBUSINESS_SERVER_ADDLSVC = 62
PRODUCT_ESSENTIALBUSINESS_SERVER_MGMT = 59
PRODUCT_ESSENTIALBUSINESS_SERVER_MGMTSVC = 61
PRODUCT_HOME_BASIC = 2
PRODUCT_HOME_BASIC_E = 67
PRODUCT_HOME_BASIC_N = 5
PRODUCT_HOME_PREMIUM = 3
PRODUCT_HOME_PREMIUM_E = 68
PRODUCT_HOME_PREMIUM_N = 26
PRODUCT_HOME_PREMIUM_SERVER = 34
PRODUCT_HOME_SERVER = 19
PRODUCT_HYPERV = 42
PRODUCT_IOTUAP = 123
PRODUCT_IOTUAPCOMMERCIAL = 131
PRODUCT_MEDIUMBUSINESS_SERVER_MANAGEMENT = 30
PRODUCT_MEDIUMBUSINESS_SERVER_MESSAGING = 32
PRODUCT_MEDIUMBUSINESS_SERVER_SECURITY = 31
PRODUCT_MOBILE_CORE = 104
PRODUCT_MOBILE_ENTERPRISE = 133
PRODUCT_MULTIPOINT_PREMIUM_SERVER = 77
PRODUCT_MULTIPOINT_STANDARD_SERVER = 76
PRODUCT_PRO_WORKSTATION = 161
PRODUCT_PRO_WORKSTATION_N = 162
PRODUCT_PROFESSIONAL = 48
PRODUCT_PROFESSIONAL_E = 69
PRODUCT_PROFESSIONAL_N = 49
PRODUCT_PROFESSIONAL_WMC = 103
PRODUCT_SB_SOLUTION_SERVER = 50
PRODUCT_SB_SOLUTION_SERVER_EM = 54
PRODUCT_SERVER_FOR_SB_SOLUTIONS = 51
PRODUCT_SERVER_FOR_SB_SOLUTIONS_EM = 55
PRODUCT_SERVER_FOR_SMALLBUSINESS = 24
PRODUCT_SERVER_FOR_SMALLBUSINESS_V = 35
PRODUCT_SERVER_FOUNDATION = 33
PRODUCT_SMALLBUSINESS_SERVER = 9
PRODUCT_SMALLBUSINESS_SERVER_PREMIUM = 25
PRODUCT_SMALLBUSINESS_SERVER_PREMIUM_CORE = 63
PRODUCT_SOLUTION_EMBEDDEDSERVER = 56
PRODUCT_STANDARD_EVALUATION_SERVER = 79
PRODUCT_STANDARD_SERVER = 7
PRODUCT_STANDARD_SERVER_CORE_ = 13
PRODUCT_STANDARD_SERVER_CORE_V = 40
PRODUCT_STANDARD_SERVER_V = 36
PRODUCT_STANDARD_SERVER_SOLUTIONS = 52
PRODUCT_STANDARD_SERVER_SOLUTIONS_CORE = 53
PRODUCT_STARTER = 11
PRODUCT_STARTER_E = 66
PRODUCT_STARTER_N = 47
PRODUCT_STORAGE_ENTERPRISE_SERVER = 23
PRODUCT_STORAGE_ENTERPRISE_SERVER_CORE = 46
PRODUCT_STORAGE_EXPRESS_SERVER = 20
PRODUCT_STORAGE_EXPRESS_SERVER_CORE = 43
PRODUCT_STORAGE_STANDARD_EVALUATION_SERVER = 96
PRODUCT_STORAGE_STANDARD_SERVER = 21
PRODUCT_STORAGE_STANDARD_SERVER_CORE = 44
PRODUCT_STORAGE_WORKGROUP_EVALUATION_SERVER = 95
PRODUCT_STORAGE_WORKGROUP_SERVER = 22
PRODUCT_STORAGE_WORKGROUP_SERVER_CORE = 45
PRODUCT_ULTIMATE = 1
PRODUCT_ULTIMATE_E = 71
PRODUCT_ULTIMATE_N = 28
PRODUCT_UNDEFINED = 0
PRODUCT_WEB_SERVER = 17
PRODUCT_WEB_SERVER_CORE = 29
DEVICEFAMILYINFOENUM = UInt32
DEVICEFAMILYINFOENUM_UAP = 0
DEVICEFAMILYINFOENUM_WINDOWS_8X = 1
DEVICEFAMILYINFOENUM_WINDOWS_PHONE_8X = 2
DEVICEFAMILYINFOENUM_DESKTOP = 3
DEVICEFAMILYINFOENUM_MOBILE = 4
DEVICEFAMILYINFOENUM_XBOX = 5
DEVICEFAMILYINFOENUM_TEAM = 6
DEVICEFAMILYINFOENUM_IOT = 7
DEVICEFAMILYINFOENUM_IOT_HEADLESS = 8
DEVICEFAMILYINFOENUM_SERVER = 9
DEVICEFAMILYINFOENUM_HOLOGRAPHIC = 10
DEVICEFAMILYINFOENUM_XBOXSRA = 11
DEVICEFAMILYINFOENUM_XBOXERA = 12
DEVICEFAMILYINFOENUM_SERVER_NANO = 13
DEVICEFAMILYINFOENUM_8828080 = 14
DEVICEFAMILYINFOENUM_7067329 = 15
DEVICEFAMILYINFOENUM_WINDOWS_CORE = 16
DEVICEFAMILYINFOENUM_WINDOWS_CORE_HEADLESS = 17
DEVICEFAMILYINFOENUM_MAX = 17
DEVICEFAMILYDEVICEFORM = UInt32
DEVICEFAMILYDEVICEFORM_UNKNOWN = 0
DEVICEFAMILYDEVICEFORM_PHONE = 1
DEVICEFAMILYDEVICEFORM_TABLET = 2
DEVICEFAMILYDEVICEFORM_DESKTOP = 3
DEVICEFAMILYDEVICEFORM_NOTEBOOK = 4
DEVICEFAMILYDEVICEFORM_CONVERTIBLE = 5
DEVICEFAMILYDEVICEFORM_DETACHABLE = 6
DEVICEFAMILYDEVICEFORM_ALLINONE = 7
DEVICEFAMILYDEVICEFORM_STICKPC = 8
DEVICEFAMILYDEVICEFORM_PUCK = 9
DEVICEFAMILYDEVICEFORM_LARGESCREEN = 10
DEVICEFAMILYDEVICEFORM_HMD = 11
DEVICEFAMILYDEVICEFORM_INDUSTRY_HANDHELD = 12
DEVICEFAMILYDEVICEFORM_INDUSTRY_TABLET = 13
DEVICEFAMILYDEVICEFORM_BANKING = 14
DEVICEFAMILYDEVICEFORM_BUILDING_AUTOMATION = 15
DEVICEFAMILYDEVICEFORM_DIGITAL_SIGNAGE = 16
DEVICEFAMILYDEVICEFORM_GAMING = 17
DEVICEFAMILYDEVICEFORM_HOME_AUTOMATION = 18
DEVICEFAMILYDEVICEFORM_INDUSTRIAL_AUTOMATION = 19
DEVICEFAMILYDEVICEFORM_KIOSK = 20
DEVICEFAMILYDEVICEFORM_MAKER_BOARD = 21
DEVICEFAMILYDEVICEFORM_MEDICAL = 22
DEVICEFAMILYDEVICEFORM_NETWORKING = 23
DEVICEFAMILYDEVICEFORM_POINT_OF_SERVICE = 24
DEVICEFAMILYDEVICEFORM_PRINTING = 25
DEVICEFAMILYDEVICEFORM_THIN_CLIENT = 26
DEVICEFAMILYDEVICEFORM_TOY = 27
DEVICEFAMILYDEVICEFORM_VENDING = 28
DEVICEFAMILYDEVICEFORM_INDUSTRY_OTHER = 29
DEVICEFAMILYDEVICEFORM_XBOX_ONE = 30
DEVICEFAMILYDEVICEFORM_XBOX_ONE_S = 31
DEVICEFAMILYDEVICEFORM_XBOX_ONE_X = 32
DEVICEFAMILYDEVICEFORM_XBOX_ONE_X_DEVKIT = 33
DEVICEFAMILYDEVICEFORM_XBOX_SERIES_X = 34
DEVICEFAMILYDEVICEFORM_XBOX_SERIES_X_DEVKIT = 35
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_00 = 36
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_01 = 37
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_02 = 38
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_03 = 39
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_04 = 40
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_05 = 41
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_06 = 42
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_07 = 43
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_08 = 44
DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_09 = 45
DEVICEFAMILYDEVICEFORM_MAX = 45
FIRMWARE_TABLE_ID = UInt32
def _define_GROUP_AFFINITY_head():
    class GROUP_AFFINITY(Structure):
        pass
    return GROUP_AFFINITY
def _define_GROUP_AFFINITY():
    GROUP_AFFINITY = win32more.System.SystemInformation.GROUP_AFFINITY_head
    GROUP_AFFINITY._fields_ = [
        ("Mask", UIntPtr),
        ("Group", UInt16),
        ("Reserved", UInt16 * 3),
    ]
    return GROUP_AFFINITY
def _define_SYSTEM_INFO_head():
    class SYSTEM_INFO(Structure):
        pass
    return SYSTEM_INFO
def _define_SYSTEM_INFO():
    SYSTEM_INFO = win32more.System.SystemInformation.SYSTEM_INFO_head
    class SYSTEM_INFO__Anonymous_e__Union(Union):
        pass
    class SYSTEM_INFO__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    SYSTEM_INFO__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("wProcessorArchitecture", win32more.System.Diagnostics.Debug.PROCESSOR_ARCHITECTURE),
        ("wReserved", UInt16),
    ]
    SYSTEM_INFO__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    SYSTEM_INFO__Anonymous_e__Union._fields_ = [
        ("dwOemId", UInt32),
        ("Anonymous", SYSTEM_INFO__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    SYSTEM_INFO._anonymous_ = [
        'Anonymous',
    ]
    SYSTEM_INFO._fields_ = [
        ("Anonymous", SYSTEM_INFO__Anonymous_e__Union),
        ("dwPageSize", UInt32),
        ("lpMinimumApplicationAddress", c_void_p),
        ("lpMaximumApplicationAddress", c_void_p),
        ("dwActiveProcessorMask", UIntPtr),
        ("dwNumberOfProcessors", UInt32),
        ("dwProcessorType", UInt32),
        ("dwAllocationGranularity", UInt32),
        ("wProcessorLevel", UInt16),
        ("wProcessorRevision", UInt16),
    ]
    return SYSTEM_INFO
def _define_MEMORYSTATUSEX_head():
    class MEMORYSTATUSEX(Structure):
        pass
    return MEMORYSTATUSEX
def _define_MEMORYSTATUSEX():
    MEMORYSTATUSEX = win32more.System.SystemInformation.MEMORYSTATUSEX_head
    MEMORYSTATUSEX._fields_ = [
        ("dwLength", UInt32),
        ("dwMemoryLoad", UInt32),
        ("ullTotalPhys", UInt64),
        ("ullAvailPhys", UInt64),
        ("ullTotalPageFile", UInt64),
        ("ullAvailPageFile", UInt64),
        ("ullTotalVirtual", UInt64),
        ("ullAvailVirtual", UInt64),
        ("ullAvailExtendedVirtual", UInt64),
    ]
    return MEMORYSTATUSEX
COMPUTER_NAME_FORMAT = Int32
COMPUTER_NAME_FORMAT_ComputerNameNetBIOS = 0
COMPUTER_NAME_FORMAT_ComputerNameDnsHostname = 1
COMPUTER_NAME_FORMAT_ComputerNameDnsDomain = 2
COMPUTER_NAME_FORMAT_ComputerNameDnsFullyQualified = 3
COMPUTER_NAME_FORMAT_ComputerNamePhysicalNetBIOS = 4
COMPUTER_NAME_FORMAT_ComputerNamePhysicalDnsHostname = 5
COMPUTER_NAME_FORMAT_ComputerNamePhysicalDnsDomain = 6
COMPUTER_NAME_FORMAT_ComputerNamePhysicalDnsFullyQualified = 7
COMPUTER_NAME_FORMAT_ComputerNameMax = 8
FIRMWARE_TYPE = Int32
FIRMWARE_TYPE_FirmwareTypeUnknown = 0
FIRMWARE_TYPE_FirmwareTypeBios = 1
FIRMWARE_TYPE_FirmwareTypeUefi = 2
FIRMWARE_TYPE_FirmwareTypeMax = 3
LOGICAL_PROCESSOR_RELATIONSHIP = Int32
LOGICAL_PROCESSOR_RELATIONSHIP_RelationProcessorCore = 0
LOGICAL_PROCESSOR_RELATIONSHIP_RelationNumaNode = 1
LOGICAL_PROCESSOR_RELATIONSHIP_RelationCache = 2
LOGICAL_PROCESSOR_RELATIONSHIP_RelationProcessorPackage = 3
LOGICAL_PROCESSOR_RELATIONSHIP_RelationGroup = 4
LOGICAL_PROCESSOR_RELATIONSHIP_RelationProcessorDie = 5
LOGICAL_PROCESSOR_RELATIONSHIP_RelationNumaNodeEx = 6
LOGICAL_PROCESSOR_RELATIONSHIP_RelationProcessorModule = 7
LOGICAL_PROCESSOR_RELATIONSHIP_RelationAll = 65535
PROCESSOR_CACHE_TYPE = Int32
PROCESSOR_CACHE_TYPE_CacheUnified = 0
PROCESSOR_CACHE_TYPE_CacheInstruction = 1
PROCESSOR_CACHE_TYPE_CacheData = 2
PROCESSOR_CACHE_TYPE_CacheTrace = 3
def _define_CACHE_DESCRIPTOR_head():
    class CACHE_DESCRIPTOR(Structure):
        pass
    return CACHE_DESCRIPTOR
def _define_CACHE_DESCRIPTOR():
    CACHE_DESCRIPTOR = win32more.System.SystemInformation.CACHE_DESCRIPTOR_head
    CACHE_DESCRIPTOR._fields_ = [
        ("Level", Byte),
        ("Associativity", Byte),
        ("LineSize", UInt16),
        ("Size", UInt32),
        ("Type", win32more.System.SystemInformation.PROCESSOR_CACHE_TYPE),
    ]
    return CACHE_DESCRIPTOR
def _define_SYSTEM_LOGICAL_PROCESSOR_INFORMATION_head():
    class SYSTEM_LOGICAL_PROCESSOR_INFORMATION(Structure):
        pass
    return SYSTEM_LOGICAL_PROCESSOR_INFORMATION
def _define_SYSTEM_LOGICAL_PROCESSOR_INFORMATION():
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION = win32more.System.SystemInformation.SYSTEM_LOGICAL_PROCESSOR_INFORMATION_head
    class SYSTEM_LOGICAL_PROCESSOR_INFORMATION__Anonymous_e__Union(Union):
        pass
    class SYSTEM_LOGICAL_PROCESSOR_INFORMATION__Anonymous_e__Union__ProcessorCore_e__Struct(Structure):
        pass
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION__Anonymous_e__Union__ProcessorCore_e__Struct._fields_ = [
        ("Flags", Byte),
    ]
    class SYSTEM_LOGICAL_PROCESSOR_INFORMATION__Anonymous_e__Union__NumaNode_e__Struct(Structure):
        pass
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION__Anonymous_e__Union__NumaNode_e__Struct._fields_ = [
        ("NodeNumber", UInt32),
    ]
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION__Anonymous_e__Union._fields_ = [
        ("ProcessorCore", SYSTEM_LOGICAL_PROCESSOR_INFORMATION__Anonymous_e__Union__ProcessorCore_e__Struct),
        ("NumaNode", SYSTEM_LOGICAL_PROCESSOR_INFORMATION__Anonymous_e__Union__NumaNode_e__Struct),
        ("Cache", win32more.System.SystemInformation.CACHE_DESCRIPTOR),
        ("Reserved", UInt64 * 2),
    ]
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION._anonymous_ = [
        'Anonymous',
    ]
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION._fields_ = [
        ("ProcessorMask", UIntPtr),
        ("Relationship", win32more.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP),
        ("Anonymous", SYSTEM_LOGICAL_PROCESSOR_INFORMATION__Anonymous_e__Union),
    ]
    return SYSTEM_LOGICAL_PROCESSOR_INFORMATION
def _define_PROCESSOR_RELATIONSHIP_head():
    class PROCESSOR_RELATIONSHIP(Structure):
        pass
    return PROCESSOR_RELATIONSHIP
def _define_PROCESSOR_RELATIONSHIP():
    PROCESSOR_RELATIONSHIP = win32more.System.SystemInformation.PROCESSOR_RELATIONSHIP_head
    PROCESSOR_RELATIONSHIP._fields_ = [
        ("Flags", Byte),
        ("EfficiencyClass", Byte),
        ("Reserved", Byte * 20),
        ("GroupCount", UInt16),
        ("GroupMask", win32more.System.SystemInformation.GROUP_AFFINITY * 0),
    ]
    return PROCESSOR_RELATIONSHIP
def _define_NUMA_NODE_RELATIONSHIP_head():
    class NUMA_NODE_RELATIONSHIP(Structure):
        pass
    return NUMA_NODE_RELATIONSHIP
def _define_NUMA_NODE_RELATIONSHIP():
    NUMA_NODE_RELATIONSHIP = win32more.System.SystemInformation.NUMA_NODE_RELATIONSHIP_head
    class NUMA_NODE_RELATIONSHIP__Anonymous_e__Union(Union):
        pass
    NUMA_NODE_RELATIONSHIP__Anonymous_e__Union._fields_ = [
        ("GroupMask", win32more.System.SystemInformation.GROUP_AFFINITY),
        ("GroupMasks", win32more.System.SystemInformation.GROUP_AFFINITY * 0),
    ]
    NUMA_NODE_RELATIONSHIP._anonymous_ = [
        'Anonymous',
    ]
    NUMA_NODE_RELATIONSHIP._fields_ = [
        ("NodeNumber", UInt32),
        ("Reserved", Byte * 18),
        ("GroupCount", UInt16),
        ("Anonymous", NUMA_NODE_RELATIONSHIP__Anonymous_e__Union),
    ]
    return NUMA_NODE_RELATIONSHIP
def _define_CACHE_RELATIONSHIP_head():
    class CACHE_RELATIONSHIP(Structure):
        pass
    return CACHE_RELATIONSHIP
def _define_CACHE_RELATIONSHIP():
    CACHE_RELATIONSHIP = win32more.System.SystemInformation.CACHE_RELATIONSHIP_head
    class CACHE_RELATIONSHIP__Anonymous_e__Union(Union):
        pass
    CACHE_RELATIONSHIP__Anonymous_e__Union._fields_ = [
        ("GroupMask", win32more.System.SystemInformation.GROUP_AFFINITY),
        ("GroupMasks", win32more.System.SystemInformation.GROUP_AFFINITY * 0),
    ]
    CACHE_RELATIONSHIP._anonymous_ = [
        'Anonymous',
    ]
    CACHE_RELATIONSHIP._fields_ = [
        ("Level", Byte),
        ("Associativity", Byte),
        ("LineSize", UInt16),
        ("CacheSize", UInt32),
        ("Type", win32more.System.SystemInformation.PROCESSOR_CACHE_TYPE),
        ("Reserved", Byte * 18),
        ("GroupCount", UInt16),
        ("Anonymous", CACHE_RELATIONSHIP__Anonymous_e__Union),
    ]
    return CACHE_RELATIONSHIP
def _define_PROCESSOR_GROUP_INFO_head():
    class PROCESSOR_GROUP_INFO(Structure):
        pass
    return PROCESSOR_GROUP_INFO
def _define_PROCESSOR_GROUP_INFO():
    PROCESSOR_GROUP_INFO = win32more.System.SystemInformation.PROCESSOR_GROUP_INFO_head
    PROCESSOR_GROUP_INFO._fields_ = [
        ("MaximumProcessorCount", Byte),
        ("ActiveProcessorCount", Byte),
        ("Reserved", Byte * 38),
        ("ActiveProcessorMask", UIntPtr),
    ]
    return PROCESSOR_GROUP_INFO
def _define_GROUP_RELATIONSHIP_head():
    class GROUP_RELATIONSHIP(Structure):
        pass
    return GROUP_RELATIONSHIP
def _define_GROUP_RELATIONSHIP():
    GROUP_RELATIONSHIP = win32more.System.SystemInformation.GROUP_RELATIONSHIP_head
    GROUP_RELATIONSHIP._fields_ = [
        ("MaximumGroupCount", UInt16),
        ("ActiveGroupCount", UInt16),
        ("Reserved", Byte * 20),
        ("GroupInfo", win32more.System.SystemInformation.PROCESSOR_GROUP_INFO * 0),
    ]
    return GROUP_RELATIONSHIP
def _define_SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX_head():
    class SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX(Structure):
        pass
    return SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX
def _define_SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX():
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX = win32more.System.SystemInformation.SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX_head
    class SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX__Anonymous_e__Union(Union):
        pass
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX__Anonymous_e__Union._fields_ = [
        ("Processor", win32more.System.SystemInformation.PROCESSOR_RELATIONSHIP),
        ("NumaNode", win32more.System.SystemInformation.NUMA_NODE_RELATIONSHIP),
        ("Cache", win32more.System.SystemInformation.CACHE_RELATIONSHIP),
        ("Group", win32more.System.SystemInformation.GROUP_RELATIONSHIP),
    ]
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX._anonymous_ = [
        'Anonymous',
    ]
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX._fields_ = [
        ("Relationship", win32more.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP),
        ("Size", UInt32),
        ("Anonymous", SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX__Anonymous_e__Union),
    ]
    return SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX
CPU_SET_INFORMATION_TYPE = Int32
CPU_SET_INFORMATION_TYPE_CpuSetInformation = 0
def _define_SYSTEM_CPU_SET_INFORMATION_head():
    class SYSTEM_CPU_SET_INFORMATION(Structure):
        pass
    return SYSTEM_CPU_SET_INFORMATION
def _define_SYSTEM_CPU_SET_INFORMATION():
    SYSTEM_CPU_SET_INFORMATION = win32more.System.SystemInformation.SYSTEM_CPU_SET_INFORMATION_head
    class SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union(Union):
        pass
    class SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct(Structure):
        pass
    class SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct__Anonymous1_e__Union(Union):
        pass
    class SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct__Anonymous1_e__Union__Anonymous_e__Struct(Structure):
        pass
    SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct__Anonymous1_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", Byte),
    ]
    SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct__Anonymous1_e__Union._anonymous_ = [
        'Anonymous',
    ]
    SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct__Anonymous1_e__Union._fields_ = [
        ("AllFlags", Byte),
        ("Anonymous", SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct__Anonymous1_e__Union__Anonymous_e__Struct),
    ]
    class SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct__Anonymous2_e__Union(Union):
        pass
    SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct__Anonymous2_e__Union._fields_ = [
        ("Reserved", UInt32),
        ("SchedulingClass", Byte),
    ]
    SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct._fields_ = [
        ("Id", UInt32),
        ("Group", UInt16),
        ("LogicalProcessorIndex", Byte),
        ("CoreIndex", Byte),
        ("LastLevelCacheIndex", Byte),
        ("NumaNodeIndex", Byte),
        ("EfficiencyClass", Byte),
        ("Anonymous1", SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct__Anonymous1_e__Union),
        ("Anonymous2", SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct__Anonymous2_e__Union),
        ("AllocationTag", UInt64),
    ]
    SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union._fields_ = [
        ("CpuSet", SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union__CpuSet_e__Struct),
    ]
    SYSTEM_CPU_SET_INFORMATION._anonymous_ = [
        'Anonymous',
    ]
    SYSTEM_CPU_SET_INFORMATION._fields_ = [
        ("Size", UInt32),
        ("Type", win32more.System.SystemInformation.CPU_SET_INFORMATION_TYPE),
        ("Anonymous", SYSTEM_CPU_SET_INFORMATION__Anonymous_e__Union),
    ]
    return SYSTEM_CPU_SET_INFORMATION
def _define_SYSTEM_POOL_ZEROING_INFORMATION_head():
    class SYSTEM_POOL_ZEROING_INFORMATION(Structure):
        pass
    return SYSTEM_POOL_ZEROING_INFORMATION
def _define_SYSTEM_POOL_ZEROING_INFORMATION():
    SYSTEM_POOL_ZEROING_INFORMATION = win32more.System.SystemInformation.SYSTEM_POOL_ZEROING_INFORMATION_head
    SYSTEM_POOL_ZEROING_INFORMATION._fields_ = [
        ("PoolZeroingSupportPresent", win32more.Foundation.BOOLEAN),
    ]
    return SYSTEM_POOL_ZEROING_INFORMATION
def _define_SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION_head():
    class SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION(Structure):
        pass
    return SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION
def _define_SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION():
    SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION = win32more.System.SystemInformation.SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION_head
    SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION._fields_ = [
        ("CycleTime", UInt64),
    ]
    return SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION
def _define_SYSTEM_SUPPORTED_PROCESSOR_ARCHITECTURES_INFORMATION_head():
    class SYSTEM_SUPPORTED_PROCESSOR_ARCHITECTURES_INFORMATION(Structure):
        pass
    return SYSTEM_SUPPORTED_PROCESSOR_ARCHITECTURES_INFORMATION
def _define_SYSTEM_SUPPORTED_PROCESSOR_ARCHITECTURES_INFORMATION():
    SYSTEM_SUPPORTED_PROCESSOR_ARCHITECTURES_INFORMATION = win32more.System.SystemInformation.SYSTEM_SUPPORTED_PROCESSOR_ARCHITECTURES_INFORMATION_head
    SYSTEM_SUPPORTED_PROCESSOR_ARCHITECTURES_INFORMATION._fields_ = [
        ("_bitfield", UInt32),
    ]
    return SYSTEM_SUPPORTED_PROCESSOR_ARCHITECTURES_INFORMATION
def _define_OSVERSIONINFOA_head():
    class OSVERSIONINFOA(Structure):
        pass
    return OSVERSIONINFOA
def _define_OSVERSIONINFOA():
    OSVERSIONINFOA = win32more.System.SystemInformation.OSVERSIONINFOA_head
    OSVERSIONINFOA._fields_ = [
        ("dwOSVersionInfoSize", UInt32),
        ("dwMajorVersion", UInt32),
        ("dwMinorVersion", UInt32),
        ("dwBuildNumber", UInt32),
        ("dwPlatformId", UInt32),
        ("szCSDVersion", win32more.Foundation.CHAR * 128),
    ]
    return OSVERSIONINFOA
def _define_OSVERSIONINFOW_head():
    class OSVERSIONINFOW(Structure):
        pass
    return OSVERSIONINFOW
def _define_OSVERSIONINFOW():
    OSVERSIONINFOW = win32more.System.SystemInformation.OSVERSIONINFOW_head
    OSVERSIONINFOW._fields_ = [
        ("dwOSVersionInfoSize", UInt32),
        ("dwMajorVersion", UInt32),
        ("dwMinorVersion", UInt32),
        ("dwBuildNumber", UInt32),
        ("dwPlatformId", UInt32),
        ("szCSDVersion", Char * 128),
    ]
    return OSVERSIONINFOW
def _define_OSVERSIONINFOEXA_head():
    class OSVERSIONINFOEXA(Structure):
        pass
    return OSVERSIONINFOEXA
def _define_OSVERSIONINFOEXA():
    OSVERSIONINFOEXA = win32more.System.SystemInformation.OSVERSIONINFOEXA_head
    OSVERSIONINFOEXA._fields_ = [
        ("dwOSVersionInfoSize", UInt32),
        ("dwMajorVersion", UInt32),
        ("dwMinorVersion", UInt32),
        ("dwBuildNumber", UInt32),
        ("dwPlatformId", UInt32),
        ("szCSDVersion", win32more.Foundation.CHAR * 128),
        ("wServicePackMajor", UInt16),
        ("wServicePackMinor", UInt16),
        ("wSuiteMask", UInt16),
        ("wProductType", Byte),
        ("wReserved", Byte),
    ]
    return OSVERSIONINFOEXA
def _define_OSVERSIONINFOEXW_head():
    class OSVERSIONINFOEXW(Structure):
        pass
    return OSVERSIONINFOEXW
def _define_OSVERSIONINFOEXW():
    OSVERSIONINFOEXW = win32more.System.SystemInformation.OSVERSIONINFOEXW_head
    OSVERSIONINFOEXW._fields_ = [
        ("dwOSVersionInfoSize", UInt32),
        ("dwMajorVersion", UInt32),
        ("dwMinorVersion", UInt32),
        ("dwBuildNumber", UInt32),
        ("dwPlatformId", UInt32),
        ("szCSDVersion", Char * 128),
        ("wServicePackMajor", UInt16),
        ("wServicePackMinor", UInt16),
        ("wSuiteMask", UInt16),
        ("wProductType", Byte),
        ("wReserved", Byte),
    ]
    return OSVERSIONINFOEXW
OS_DEPLOYEMENT_STATE_VALUES = Int32
OS_DEPLOYMENT_STANDARD = 1
OS_DEPLOYMENT_COMPACT = 2
RTL_SYSTEM_GLOBAL_DATA_ID = Int32
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdUnknown = 0
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdRngSeedVersion = 1
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdInterruptTime = 2
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdTimeZoneBias = 3
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdImageNumberLow = 4
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdImageNumberHigh = 5
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdTimeZoneId = 6
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdNtMajorVersion = 7
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdNtMinorVersion = 8
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdSystemExpirationDate = 9
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdKdDebuggerEnabled = 10
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdCyclesPerYield = 11
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdSafeBootMode = 12
RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdLastSystemRITEventTickCount = 13
def _define_MEMORYSTATUS_head():
    class MEMORYSTATUS(Structure):
        pass
    return MEMORYSTATUS
def _define_MEMORYSTATUS():
    MEMORYSTATUS = win32more.System.SystemInformation.MEMORYSTATUS_head
    MEMORYSTATUS._fields_ = [
        ("dwLength", UInt32),
        ("dwMemoryLoad", UInt32),
        ("dwTotalPhys", UIntPtr),
        ("dwAvailPhys", UIntPtr),
        ("dwTotalPageFile", UIntPtr),
        ("dwAvailPageFile", UIntPtr),
        ("dwTotalVirtual", UIntPtr),
        ("dwAvailVirtual", UIntPtr),
    ]
    return MEMORYSTATUS
DEP_SYSTEM_POLICY_TYPE = Int32
DEP_SYSTEM_POLICY_TYPE_DEPPolicyAlwaysOff = 0
DEP_SYSTEM_POLICY_TYPE_DEPPolicyAlwaysOn = 1
DEP_SYSTEM_POLICY_TYPE_DEPPolicyOptIn = 2
DEP_SYSTEM_POLICY_TYPE_DEPPolicyOptOut = 3
DEP_SYSTEM_POLICY_TYPE_DEPTotalPolicyCount = 4
def _define_PGET_SYSTEM_WOW64_DIRECTORY_A():
    return CFUNCTYPE(UInt32,POINTER(Byte),UInt32, use_last_error=False)
def _define_PGET_SYSTEM_WOW64_DIRECTORY_W():
    return CFUNCTYPE(UInt32,POINTER(Char),UInt32, use_last_error=False)
def _define_GlobalMemoryStatusEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.SystemInformation.MEMORYSTATUSEX_head), use_last_error=True)(("GlobalMemoryStatusEx", windll["KERNEL32"]), ((1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemInfo():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SystemInformation.SYSTEM_INFO_head), use_last_error=False)(("GetSystemInfo", windll["KERNEL32"]), ((1, 'lpSystemInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemTime():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=False)(("GetSystemTime", windll["KERNEL32"]), ((1, 'lpSystemTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemTimeAsFileTime():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("GetSystemTimeAsFileTime", windll["KERNEL32"]), ((1, 'lpSystemTimeAsFileTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLocalTime():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=False)(("GetLocalTime", windll["KERNEL32"]), ((1, 'lpSystemTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsUserCetAvailableInEnvironment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.SystemInformation.USER_CET_ENVIRONMENT, use_last_error=False)(("IsUserCetAvailableInEnvironment", windll["KERNEL32"]), ((1, 'UserCetEnvironment'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemLeapSecondInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL),POINTER(UInt32), use_last_error=False)(("GetSystemLeapSecondInformation", windll["KERNEL32"]), ((1, 'Enabled'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVersion():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetVersion", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetLocalTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=True)(("SetLocalTime", windll["KERNEL32"]), ((1, 'lpSystemTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTickCount():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetTickCount", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTickCount64():
    try:
        return WINFUNCTYPE(UInt64, use_last_error=False)(("GetTickCount64", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemTimeAdjustment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=True)(("GetSystemTimeAdjustment", windll["KERNEL32"]), ((1, 'lpTimeAdjustment'),(1, 'lpTimeIncrement'),(1, 'lpTimeAdjustmentDisabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemTimeAdjustmentPrecise():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt64),POINTER(UInt64),POINTER(win32more.Foundation.BOOL), use_last_error=True)(("GetSystemTimeAdjustmentPrecise", windll["api-ms-win-core-sysinfo-l1-2-4"]), ((1, 'lpTimeAdjustment'),(1, 'lpTimeIncrement'),(1, 'lpTimeAdjustmentDisabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemDirectoryA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Byte),UInt32, use_last_error=True)(("GetSystemDirectoryA", windll["KERNEL32"]), ((1, 'lpBuffer'),(1, 'uSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemDirectoryW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Char),UInt32, use_last_error=True)(("GetSystemDirectoryW", windll["KERNEL32"]), ((1, 'lpBuffer'),(1, 'uSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemDirectory():
    return win32more.System.SystemInformation.GetSystemDirectoryW
def _define_GetWindowsDirectoryA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Byte),UInt32, use_last_error=True)(("GetWindowsDirectoryA", windll["KERNEL32"]), ((1, 'lpBuffer'),(1, 'uSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowsDirectoryW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Char),UInt32, use_last_error=True)(("GetWindowsDirectoryW", windll["KERNEL32"]), ((1, 'lpBuffer'),(1, 'uSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowsDirectory():
    return win32more.System.SystemInformation.GetWindowsDirectoryW
def _define_GetSystemWindowsDirectoryA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Byte),UInt32, use_last_error=True)(("GetSystemWindowsDirectoryA", windll["KERNEL32"]), ((1, 'lpBuffer'),(1, 'uSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemWindowsDirectoryW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Char),UInt32, use_last_error=True)(("GetSystemWindowsDirectoryW", windll["KERNEL32"]), ((1, 'lpBuffer'),(1, 'uSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemWindowsDirectory():
    return win32more.System.SystemInformation.GetSystemWindowsDirectoryW
def _define_GetComputerNameExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.SystemInformation.COMPUTER_NAME_FORMAT,POINTER(Byte),POINTER(UInt32), use_last_error=True)(("GetComputerNameExA", windll["KERNEL32"]), ((1, 'NameType'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetComputerNameExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.SystemInformation.COMPUTER_NAME_FORMAT,POINTER(Char),POINTER(UInt32), use_last_error=True)(("GetComputerNameExW", windll["KERNEL32"]), ((1, 'NameType'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetComputerNameEx():
    return win32more.System.SystemInformation.GetComputerNameExW
def _define_SetComputerNameExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.SystemInformation.COMPUTER_NAME_FORMAT,win32more.Foundation.PWSTR, use_last_error=True)(("SetComputerNameExW", windll["KERNEL32"]), ((1, 'NameType'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetComputerNameEx():
    return win32more.System.SystemInformation.SetComputerNameExW
def _define_SetSystemTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=True)(("SetSystemTime", windll["KERNEL32"]), ((1, 'lpSystemTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVersionExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.SystemInformation.OSVERSIONINFOA_head), use_last_error=True)(("GetVersionExA", windll["KERNEL32"]), ((1, 'lpVersionInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVersionExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.SystemInformation.OSVERSIONINFOW_head), use_last_error=True)(("GetVersionExW", windll["KERNEL32"]), ((1, 'lpVersionInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVersionEx():
    return win32more.System.SystemInformation.GetVersionExW
def _define_GetLogicalProcessorInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.SystemInformation.SYSTEM_LOGICAL_PROCESSOR_INFORMATION_head),POINTER(UInt32), use_last_error=True)(("GetLogicalProcessorInformation", windll["KERNEL32"]), ((1, 'Buffer'),(1, 'ReturnedLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLogicalProcessorInformationEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.SystemInformation.LOGICAL_PROCESSOR_RELATIONSHIP,POINTER(win32more.System.SystemInformation.SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX_head),POINTER(UInt32), use_last_error=True)(("GetLogicalProcessorInformationEx", windll["KERNEL32"]), ((1, 'RelationshipType'),(1, 'Buffer'),(1, 'ReturnedLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNativeSystemInfo():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SystemInformation.SYSTEM_INFO_head), use_last_error=False)(("GetNativeSystemInfo", windll["KERNEL32"]), ((1, 'lpSystemInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemTimePreciseAsFileTime():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("GetSystemTimePreciseAsFileTime", windll["KERNEL32"]), ((1, 'lpSystemTimeAsFileTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProductInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,UInt32,UInt32,POINTER(win32more.System.SystemInformation.OS_PRODUCT_TYPE), use_last_error=False)(("GetProductInfo", windll["KERNEL32"]), ((1, 'dwOSMajorVersion'),(1, 'dwOSMinorVersion'),(1, 'dwSpMajorVersion'),(1, 'dwSpMinorVersion'),(1, 'pdwReturnedProductType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerSetConditionMask():
    try:
        return WINFUNCTYPE(UInt64,UInt64,win32more.System.SystemInformation.VER_FLAGS,Byte, use_last_error=False)(("VerSetConditionMask", windll["KERNEL32"]), ((1, 'ConditionMask'),(1, 'TypeMask'),(1, 'Condition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOsSafeBootMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32), use_last_error=False)(("GetOsSafeBootMode", windll["api-ms-win-core-sysinfo-l1-2-0"]), ((1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumSystemFirmwareTables():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.SystemInformation.FIRMWARE_TABLE_PROVIDER,POINTER(win32more.System.SystemInformation.FIRMWARE_TABLE_ID),UInt32, use_last_error=True)(("EnumSystemFirmwareTables", windll["KERNEL32"]), ((1, 'FirmwareTableProviderSignature'),(1, 'pFirmwareTableEnumBuffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemFirmwareTable():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.SystemInformation.FIRMWARE_TABLE_PROVIDER,win32more.System.SystemInformation.FIRMWARE_TABLE_ID,c_void_p,UInt32, use_last_error=True)(("GetSystemFirmwareTable", windll["KERNEL32"]), ((1, 'FirmwareTableProviderSignature'),(1, 'FirmwareTableID'),(1, 'pFirmwareTableBuffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsHostnameToComputerNameExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32), use_last_error=False)(("DnsHostnameToComputerNameExW", windll["KERNEL32"]), ((1, 'Hostname'),(1, 'ComputerName'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPhysicallyInstalledSystemMemory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt64), use_last_error=True)(("GetPhysicallyInstalledSystemMemory", windll["KERNEL32"]), ((1, 'TotalMemoryInKilobytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetComputerNameEx2W():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.SystemInformation.COMPUTER_NAME_FORMAT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("SetComputerNameEx2W", windll["KERNEL32"]), ((1, 'NameType'),(1, 'Flags'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSystemTimeAdjustment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.BOOL, use_last_error=True)(("SetSystemTimeAdjustment", windll["KERNEL32"]), ((1, 'dwTimeAdjustment'),(1, 'bTimeAdjustmentDisabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSystemTimeAdjustmentPrecise():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt64,win32more.Foundation.BOOL, use_last_error=True)(("SetSystemTimeAdjustmentPrecise", windll["api-ms-win-core-sysinfo-l1-2-4"]), ((1, 'dwTimeAdjustment'),(1, 'bTimeAdjustmentDisabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessorSystemCycleTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt16,POINTER(win32more.System.SystemInformation.SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION_head),POINTER(UInt32), use_last_error=True)(("GetProcessorSystemCycleTime", windll["KERNEL32"]), ((1, 'Group'),(1, 'Buffer'),(1, 'ReturnedLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOsManufacturingMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("GetOsManufacturingMode", windll["api-ms-win-core-sysinfo-l1-2-3"]), ((1, 'pbEnabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIntegratedDisplaySize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(("GetIntegratedDisplaySize", windll["api-ms-win-core-sysinfo-l1-2-3"]), ((1, 'sizeInInches'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetComputerNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR, use_last_error=True)(("SetComputerNameA", windll["KERNEL32"]), ((1, 'lpComputerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetComputerNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=True)(("SetComputerNameW", windll["KERNEL32"]), ((1, 'lpComputerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetComputerName():
    return win32more.System.SystemInformation.SetComputerNameW
def _define_SetComputerNameExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.SystemInformation.COMPUTER_NAME_FORMAT,win32more.Foundation.PSTR, use_last_error=True)(("SetComputerNameExA", windll["KERNEL32"]), ((1, 'NameType'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemCpuSetInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.SystemInformation.SYSTEM_CPU_SET_INFORMATION_head),UInt32,POINTER(UInt32),win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("GetSystemCpuSetInformation", windll["KERNEL32"]), ((1, 'Information'),(1, 'BufferLength'),(1, 'ReturnedLength'),(1, 'Process'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemWow64DirectoryA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Byte),UInt32, use_last_error=True)(("GetSystemWow64DirectoryA", windll["KERNEL32"]), ((1, 'lpBuffer'),(1, 'uSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemWow64DirectoryW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Char),UInt32, use_last_error=True)(("GetSystemWow64DirectoryW", windll["KERNEL32"]), ((1, 'lpBuffer'),(1, 'uSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemWow64Directory():
    return win32more.System.SystemInformation.GetSystemWow64DirectoryW
def _define_GetSystemWow64Directory2A():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Byte),UInt32,UInt16, use_last_error=True)(("GetSystemWow64Directory2A", windll["api-ms-win-core-wow64-l1-1-1"]), ((1, 'lpBuffer'),(1, 'uSize'),(1, 'ImageFileMachineType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemWow64Directory2W():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Char),UInt32,UInt16, use_last_error=True)(("GetSystemWow64Directory2W", windll["api-ms-win-core-wow64-l1-1-1"]), ((1, 'lpBuffer'),(1, 'uSize'),(1, 'ImageFileMachineType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemWow64Directory2():
    return win32more.System.SystemInformation.GetSystemWow64Directory2W
def _define_IsWow64GuestMachineSupported():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL), use_last_error=True)(("IsWow64GuestMachineSupported", windll["KERNEL32"]), ((1, 'WowGuestMachine'),(1, 'MachineIsSupported'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlGetProductInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,UInt32,UInt32,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(("RtlGetProductInfo", windll["ntdll"]), ((1, 'OSMajorVersion'),(1, 'OSMinorVersion'),(1, 'SpMajorVersion'),(1, 'SpMinorVersion'),(1, 'ReturnedProductType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlOsDeploymentState():
    try:
        return WINFUNCTYPE(win32more.System.SystemInformation.OS_DEPLOYEMENT_STATE_VALUES,UInt32, use_last_error=False)(("RtlOsDeploymentState", windll["ntdll"]), ((1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlGetSystemGlobalData():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.SystemInformation.RTL_SYSTEM_GLOBAL_DATA_ID,c_void_p,UInt32, use_last_error=False)(("RtlGetSystemGlobalData", windll["ntdllk"]), ((1, 'DataId'),(1, 'Buffer'),(1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlGetDeviceFamilyInfoEnum():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt64),POINTER(win32more.System.SystemInformation.DEVICEFAMILYINFOENUM),POINTER(win32more.System.SystemInformation.DEVICEFAMILYDEVICEFORM), use_last_error=False)(("RtlGetDeviceFamilyInfoEnum", windll["ntdll"]), ((1, 'pullUAPInfo'),(1, 'pulDeviceFamily'),(1, 'pulDeviceForm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlConvertDeviceFamilyInfoToString():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(UInt32),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RtlConvertDeviceFamilyInfoToString", windll["ntdll"]), ((1, 'pulDeviceFamilyBufferSize'),(1, 'pulDeviceFormBufferSize'),(1, 'DeviceFamily'),(1, 'DeviceForm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlSwitchedVVI():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.SystemInformation.OSVERSIONINFOEXW_head),UInt32,UInt64, use_last_error=False)(("RtlSwitchedVVI", windll["ntdll"]), ((1, 'VersionInfo'),(1, 'TypeMask'),(1, 'ConditionMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalMemoryStatus():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SystemInformation.MEMORYSTATUS_head), use_last_error=False)(("GlobalMemoryStatus", windll["KERNEL32"]), ((1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemDEPPolicy():
    try:
        return WINFUNCTYPE(win32more.System.SystemInformation.DEP_SYSTEM_POLICY_TYPE, use_last_error=False)(("GetSystemDEPPolicy", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFirmwareType():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.SystemInformation.FIRMWARE_TYPE), use_last_error=True)(("GetFirmwareType", windll["KERNEL32"]), ((1, 'FirmwareType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerifyVersionInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.SystemInformation.OSVERSIONINFOEXA_head),win32more.System.SystemInformation.VER_FLAGS,UInt64, use_last_error=True)(("VerifyVersionInfoA", windll["KERNEL32"]), ((1, 'lpVersionInformation'),(1, 'dwTypeMask'),(1, 'dwlConditionMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerifyVersionInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.SystemInformation.OSVERSIONINFOEXW_head),win32more.System.SystemInformation.VER_FLAGS,UInt64, use_last_error=True)(("VerifyVersionInfoW", windll["KERNEL32"]), ((1, 'lpVersionInformation'),(1, 'dwTypeMask'),(1, 'dwlConditionMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerifyVersionInfo():
    return win32more.System.SystemInformation.VerifyVersionInfoW
__all__ = [
    "NTDDI_WIN2K",
    "NTDDI_WINXP",
    "NTDDI_WINXPSP2",
    "NTDDI_WS03SP1",
    "NTDDI_VISTA",
    "NTDDI_VISTASP1",
    "NTDDI_WIN7",
    "NTDDI_WIN8",
    "NTDDI_WINBLUE",
    "NTDDI_WINTHRESHOLD",
    "SYSTEM_CPU_SET_INFORMATION_PARKED",
    "SYSTEM_CPU_SET_INFORMATION_ALLOCATED",
    "SYSTEM_CPU_SET_INFORMATION_ALLOCATED_TO_TARGET_PROCESS",
    "SYSTEM_CPU_SET_INFORMATION_REALTIME",
    "_WIN32_WINNT_NT4",
    "_WIN32_WINNT_WIN2K",
    "_WIN32_WINNT_WINXP",
    "_WIN32_WINNT_WS03",
    "_WIN32_WINNT_WIN6",
    "_WIN32_WINNT_VISTA",
    "_WIN32_WINNT_WS08",
    "_WIN32_WINNT_LONGHORN",
    "_WIN32_WINNT_WIN7",
    "_WIN32_WINNT_WIN8",
    "_WIN32_WINNT_WINBLUE",
    "_WIN32_WINNT_WINTHRESHOLD",
    "_WIN32_WINNT_WIN10",
    "_WIN32_IE_IE20",
    "_WIN32_IE_IE30",
    "_WIN32_IE_IE302",
    "_WIN32_IE_IE40",
    "_WIN32_IE_IE401",
    "_WIN32_IE_IE50",
    "_WIN32_IE_IE501",
    "_WIN32_IE_IE55",
    "_WIN32_IE_IE60",
    "_WIN32_IE_IE60SP1",
    "_WIN32_IE_IE60SP2",
    "_WIN32_IE_IE70",
    "_WIN32_IE_IE80",
    "_WIN32_IE_IE90",
    "_WIN32_IE_IE100",
    "_WIN32_IE_IE110",
    "_WIN32_IE_NT4",
    "_WIN32_IE_NT4SP1",
    "_WIN32_IE_NT4SP2",
    "_WIN32_IE_NT4SP3",
    "_WIN32_IE_NT4SP4",
    "_WIN32_IE_NT4SP5",
    "_WIN32_IE_NT4SP6",
    "_WIN32_IE_WIN98",
    "_WIN32_IE_WIN98SE",
    "_WIN32_IE_WINME",
    "_WIN32_IE_WIN2K",
    "_WIN32_IE_WIN2KSP1",
    "_WIN32_IE_WIN2KSP2",
    "_WIN32_IE_WIN2KSP3",
    "_WIN32_IE_WIN2KSP4",
    "_WIN32_IE_XP",
    "_WIN32_IE_XPSP1",
    "_WIN32_IE_XPSP2",
    "_WIN32_IE_WS03",
    "_WIN32_IE_WS03SP1",
    "_WIN32_IE_WIN6",
    "_WIN32_IE_LONGHORN",
    "_WIN32_IE_WIN7",
    "_WIN32_IE_WIN8",
    "_WIN32_IE_WINBLUE",
    "_WIN32_IE_WINTHRESHOLD",
    "_WIN32_IE_WIN10",
    "NTDDI_WIN4",
    "NTDDI_WIN2KSP1",
    "NTDDI_WIN2KSP2",
    "NTDDI_WIN2KSP3",
    "NTDDI_WIN2KSP4",
    "NTDDI_WINXPSP1",
    "NTDDI_WINXPSP3",
    "NTDDI_WINXPSP4",
    "NTDDI_WS03",
    "NTDDI_WS03SP2",
    "NTDDI_WS03SP3",
    "NTDDI_WS03SP4",
    "NTDDI_WIN6",
    "NTDDI_WIN6SP1",
    "NTDDI_WIN6SP2",
    "NTDDI_WIN6SP3",
    "NTDDI_WIN6SP4",
    "NTDDI_VISTASP2",
    "NTDDI_VISTASP3",
    "NTDDI_VISTASP4",
    "NTDDI_LONGHORN",
    "NTDDI_WS08",
    "NTDDI_WS08SP2",
    "NTDDI_WS08SP3",
    "NTDDI_WS08SP4",
    "NTDDI_WIN10",
    "NTDDI_WIN10_TH2",
    "NTDDI_WIN10_RS1",
    "NTDDI_WIN10_RS2",
    "NTDDI_WIN10_RS3",
    "NTDDI_WIN10_RS4",
    "NTDDI_WIN10_RS5",
    "NTDDI_WIN10_19H1",
    "NTDDI_WIN10_VB",
    "NTDDI_WIN10_MN",
    "NTDDI_WIN10_FE",
    "NTDDI_WIN10_CO",
    "WDK_NTDDI_VERSION",
    "OSVERSION_MASK",
    "SPVERSION_MASK",
    "SUBVERSION_MASK",
    "NTDDI_VERSION",
    "SCEX2_ALT_NETBIOS_NAME",
    "VER_FLAGS",
    "VER_MINORVERSION",
    "VER_MAJORVERSION",
    "VER_BUILDNUMBER",
    "VER_PLATFORMID",
    "VER_SERVICEPACKMINOR",
    "VER_SERVICEPACKMAJOR",
    "VER_SUITENAME",
    "VER_PRODUCT_TYPE",
    "FIRMWARE_TABLE_PROVIDER",
    "ACPI",
    "FIRM",
    "RSMB",
    "USER_CET_ENVIRONMENT",
    "USER_CET_ENVIRONMENT_WIN32_PROCESS",
    "USER_CET_ENVIRONMENT_SGX2_ENCLAVE",
    "USER_CET_ENVIRONMENT_VBS_ENCLAVE",
    "USER_CET_ENVIRONMENT_VBS_BASIC_ENCLAVE",
    "OS_PRODUCT_TYPE",
    "PRODUCT_BUSINESS",
    "PRODUCT_BUSINESS_N",
    "PRODUCT_CLUSTER_SERVER",
    "PRODUCT_CLUSTER_SERVER_V",
    "PRODUCT_CORE",
    "PRODUCT_CORE_COUNTRYSPECIFIC",
    "PRODUCT_CORE_N",
    "PRODUCT_CORE_SINGLELANGUAGE",
    "PRODUCT_DATACENTER_EVALUATION_SERVER",
    "PRODUCT_DATACENTER_A_SERVER_CORE",
    "PRODUCT_STANDARD_A_SERVER_CORE",
    "PRODUCT_DATACENTER_SERVER",
    "PRODUCT_DATACENTER_SERVER_CORE",
    "PRODUCT_DATACENTER_SERVER_CORE_V",
    "PRODUCT_DATACENTER_SERVER_V",
    "PRODUCT_EDUCATION",
    "PRODUCT_EDUCATION_N",
    "PRODUCT_ENTERPRISE",
    "PRODUCT_ENTERPRISE_E",
    "PRODUCT_ENTERPRISE_EVALUATION",
    "PRODUCT_ENTERPRISE_N",
    "PRODUCT_ENTERPRISE_N_EVALUATION",
    "PRODUCT_ENTERPRISE_S",
    "PRODUCT_ENTERPRISE_S_EVALUATION",
    "PRODUCT_ENTERPRISE_S_N",
    "PRODUCT_ENTERPRISE_S_N_EVALUATION",
    "PRODUCT_ENTERPRISE_SERVER",
    "PRODUCT_ENTERPRISE_SERVER_CORE",
    "PRODUCT_ENTERPRISE_SERVER_CORE_V",
    "PRODUCT_ENTERPRISE_SERVER_IA64",
    "PRODUCT_ENTERPRISE_SERVER_V",
    "PRODUCT_ESSENTIALBUSINESS_SERVER_ADDL",
    "PRODUCT_ESSENTIALBUSINESS_SERVER_ADDLSVC",
    "PRODUCT_ESSENTIALBUSINESS_SERVER_MGMT",
    "PRODUCT_ESSENTIALBUSINESS_SERVER_MGMTSVC",
    "PRODUCT_HOME_BASIC",
    "PRODUCT_HOME_BASIC_E",
    "PRODUCT_HOME_BASIC_N",
    "PRODUCT_HOME_PREMIUM",
    "PRODUCT_HOME_PREMIUM_E",
    "PRODUCT_HOME_PREMIUM_N",
    "PRODUCT_HOME_PREMIUM_SERVER",
    "PRODUCT_HOME_SERVER",
    "PRODUCT_HYPERV",
    "PRODUCT_IOTUAP",
    "PRODUCT_IOTUAPCOMMERCIAL",
    "PRODUCT_MEDIUMBUSINESS_SERVER_MANAGEMENT",
    "PRODUCT_MEDIUMBUSINESS_SERVER_MESSAGING",
    "PRODUCT_MEDIUMBUSINESS_SERVER_SECURITY",
    "PRODUCT_MOBILE_CORE",
    "PRODUCT_MOBILE_ENTERPRISE",
    "PRODUCT_MULTIPOINT_PREMIUM_SERVER",
    "PRODUCT_MULTIPOINT_STANDARD_SERVER",
    "PRODUCT_PRO_WORKSTATION",
    "PRODUCT_PRO_WORKSTATION_N",
    "PRODUCT_PROFESSIONAL",
    "PRODUCT_PROFESSIONAL_E",
    "PRODUCT_PROFESSIONAL_N",
    "PRODUCT_PROFESSIONAL_WMC",
    "PRODUCT_SB_SOLUTION_SERVER",
    "PRODUCT_SB_SOLUTION_SERVER_EM",
    "PRODUCT_SERVER_FOR_SB_SOLUTIONS",
    "PRODUCT_SERVER_FOR_SB_SOLUTIONS_EM",
    "PRODUCT_SERVER_FOR_SMALLBUSINESS",
    "PRODUCT_SERVER_FOR_SMALLBUSINESS_V",
    "PRODUCT_SERVER_FOUNDATION",
    "PRODUCT_SMALLBUSINESS_SERVER",
    "PRODUCT_SMALLBUSINESS_SERVER_PREMIUM",
    "PRODUCT_SMALLBUSINESS_SERVER_PREMIUM_CORE",
    "PRODUCT_SOLUTION_EMBEDDEDSERVER",
    "PRODUCT_STANDARD_EVALUATION_SERVER",
    "PRODUCT_STANDARD_SERVER",
    "PRODUCT_STANDARD_SERVER_CORE_",
    "PRODUCT_STANDARD_SERVER_CORE_V",
    "PRODUCT_STANDARD_SERVER_V",
    "PRODUCT_STANDARD_SERVER_SOLUTIONS",
    "PRODUCT_STANDARD_SERVER_SOLUTIONS_CORE",
    "PRODUCT_STARTER",
    "PRODUCT_STARTER_E",
    "PRODUCT_STARTER_N",
    "PRODUCT_STORAGE_ENTERPRISE_SERVER",
    "PRODUCT_STORAGE_ENTERPRISE_SERVER_CORE",
    "PRODUCT_STORAGE_EXPRESS_SERVER",
    "PRODUCT_STORAGE_EXPRESS_SERVER_CORE",
    "PRODUCT_STORAGE_STANDARD_EVALUATION_SERVER",
    "PRODUCT_STORAGE_STANDARD_SERVER",
    "PRODUCT_STORAGE_STANDARD_SERVER_CORE",
    "PRODUCT_STORAGE_WORKGROUP_EVALUATION_SERVER",
    "PRODUCT_STORAGE_WORKGROUP_SERVER",
    "PRODUCT_STORAGE_WORKGROUP_SERVER_CORE",
    "PRODUCT_ULTIMATE",
    "PRODUCT_ULTIMATE_E",
    "PRODUCT_ULTIMATE_N",
    "PRODUCT_UNDEFINED",
    "PRODUCT_WEB_SERVER",
    "PRODUCT_WEB_SERVER_CORE",
    "DEVICEFAMILYINFOENUM",
    "DEVICEFAMILYINFOENUM_UAP",
    "DEVICEFAMILYINFOENUM_WINDOWS_8X",
    "DEVICEFAMILYINFOENUM_WINDOWS_PHONE_8X",
    "DEVICEFAMILYINFOENUM_DESKTOP",
    "DEVICEFAMILYINFOENUM_MOBILE",
    "DEVICEFAMILYINFOENUM_XBOX",
    "DEVICEFAMILYINFOENUM_TEAM",
    "DEVICEFAMILYINFOENUM_IOT",
    "DEVICEFAMILYINFOENUM_IOT_HEADLESS",
    "DEVICEFAMILYINFOENUM_SERVER",
    "DEVICEFAMILYINFOENUM_HOLOGRAPHIC",
    "DEVICEFAMILYINFOENUM_XBOXSRA",
    "DEVICEFAMILYINFOENUM_XBOXERA",
    "DEVICEFAMILYINFOENUM_SERVER_NANO",
    "DEVICEFAMILYINFOENUM_8828080",
    "DEVICEFAMILYINFOENUM_7067329",
    "DEVICEFAMILYINFOENUM_WINDOWS_CORE",
    "DEVICEFAMILYINFOENUM_WINDOWS_CORE_HEADLESS",
    "DEVICEFAMILYINFOENUM_MAX",
    "DEVICEFAMILYDEVICEFORM",
    "DEVICEFAMILYDEVICEFORM_UNKNOWN",
    "DEVICEFAMILYDEVICEFORM_PHONE",
    "DEVICEFAMILYDEVICEFORM_TABLET",
    "DEVICEFAMILYDEVICEFORM_DESKTOP",
    "DEVICEFAMILYDEVICEFORM_NOTEBOOK",
    "DEVICEFAMILYDEVICEFORM_CONVERTIBLE",
    "DEVICEFAMILYDEVICEFORM_DETACHABLE",
    "DEVICEFAMILYDEVICEFORM_ALLINONE",
    "DEVICEFAMILYDEVICEFORM_STICKPC",
    "DEVICEFAMILYDEVICEFORM_PUCK",
    "DEVICEFAMILYDEVICEFORM_LARGESCREEN",
    "DEVICEFAMILYDEVICEFORM_HMD",
    "DEVICEFAMILYDEVICEFORM_INDUSTRY_HANDHELD",
    "DEVICEFAMILYDEVICEFORM_INDUSTRY_TABLET",
    "DEVICEFAMILYDEVICEFORM_BANKING",
    "DEVICEFAMILYDEVICEFORM_BUILDING_AUTOMATION",
    "DEVICEFAMILYDEVICEFORM_DIGITAL_SIGNAGE",
    "DEVICEFAMILYDEVICEFORM_GAMING",
    "DEVICEFAMILYDEVICEFORM_HOME_AUTOMATION",
    "DEVICEFAMILYDEVICEFORM_INDUSTRIAL_AUTOMATION",
    "DEVICEFAMILYDEVICEFORM_KIOSK",
    "DEVICEFAMILYDEVICEFORM_MAKER_BOARD",
    "DEVICEFAMILYDEVICEFORM_MEDICAL",
    "DEVICEFAMILYDEVICEFORM_NETWORKING",
    "DEVICEFAMILYDEVICEFORM_POINT_OF_SERVICE",
    "DEVICEFAMILYDEVICEFORM_PRINTING",
    "DEVICEFAMILYDEVICEFORM_THIN_CLIENT",
    "DEVICEFAMILYDEVICEFORM_TOY",
    "DEVICEFAMILYDEVICEFORM_VENDING",
    "DEVICEFAMILYDEVICEFORM_INDUSTRY_OTHER",
    "DEVICEFAMILYDEVICEFORM_XBOX_ONE",
    "DEVICEFAMILYDEVICEFORM_XBOX_ONE_S",
    "DEVICEFAMILYDEVICEFORM_XBOX_ONE_X",
    "DEVICEFAMILYDEVICEFORM_XBOX_ONE_X_DEVKIT",
    "DEVICEFAMILYDEVICEFORM_XBOX_SERIES_X",
    "DEVICEFAMILYDEVICEFORM_XBOX_SERIES_X_DEVKIT",
    "DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_00",
    "DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_01",
    "DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_02",
    "DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_03",
    "DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_04",
    "DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_05",
    "DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_06",
    "DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_07",
    "DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_08",
    "DEVICEFAMILYDEVICEFORM_XBOX_RESERVED_09",
    "DEVICEFAMILYDEVICEFORM_MAX",
    "FIRMWARE_TABLE_ID",
    "GROUP_AFFINITY",
    "SYSTEM_INFO",
    "MEMORYSTATUSEX",
    "COMPUTER_NAME_FORMAT",
    "COMPUTER_NAME_FORMAT_ComputerNameNetBIOS",
    "COMPUTER_NAME_FORMAT_ComputerNameDnsHostname",
    "COMPUTER_NAME_FORMAT_ComputerNameDnsDomain",
    "COMPUTER_NAME_FORMAT_ComputerNameDnsFullyQualified",
    "COMPUTER_NAME_FORMAT_ComputerNamePhysicalNetBIOS",
    "COMPUTER_NAME_FORMAT_ComputerNamePhysicalDnsHostname",
    "COMPUTER_NAME_FORMAT_ComputerNamePhysicalDnsDomain",
    "COMPUTER_NAME_FORMAT_ComputerNamePhysicalDnsFullyQualified",
    "COMPUTER_NAME_FORMAT_ComputerNameMax",
    "FIRMWARE_TYPE",
    "FIRMWARE_TYPE_FirmwareTypeUnknown",
    "FIRMWARE_TYPE_FirmwareTypeBios",
    "FIRMWARE_TYPE_FirmwareTypeUefi",
    "FIRMWARE_TYPE_FirmwareTypeMax",
    "LOGICAL_PROCESSOR_RELATIONSHIP",
    "LOGICAL_PROCESSOR_RELATIONSHIP_RelationProcessorCore",
    "LOGICAL_PROCESSOR_RELATIONSHIP_RelationNumaNode",
    "LOGICAL_PROCESSOR_RELATIONSHIP_RelationCache",
    "LOGICAL_PROCESSOR_RELATIONSHIP_RelationProcessorPackage",
    "LOGICAL_PROCESSOR_RELATIONSHIP_RelationGroup",
    "LOGICAL_PROCESSOR_RELATIONSHIP_RelationProcessorDie",
    "LOGICAL_PROCESSOR_RELATIONSHIP_RelationNumaNodeEx",
    "LOGICAL_PROCESSOR_RELATIONSHIP_RelationProcessorModule",
    "LOGICAL_PROCESSOR_RELATIONSHIP_RelationAll",
    "PROCESSOR_CACHE_TYPE",
    "PROCESSOR_CACHE_TYPE_CacheUnified",
    "PROCESSOR_CACHE_TYPE_CacheInstruction",
    "PROCESSOR_CACHE_TYPE_CacheData",
    "PROCESSOR_CACHE_TYPE_CacheTrace",
    "CACHE_DESCRIPTOR",
    "SYSTEM_LOGICAL_PROCESSOR_INFORMATION",
    "PROCESSOR_RELATIONSHIP",
    "NUMA_NODE_RELATIONSHIP",
    "CACHE_RELATIONSHIP",
    "PROCESSOR_GROUP_INFO",
    "GROUP_RELATIONSHIP",
    "SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX",
    "CPU_SET_INFORMATION_TYPE",
    "CPU_SET_INFORMATION_TYPE_CpuSetInformation",
    "SYSTEM_CPU_SET_INFORMATION",
    "SYSTEM_POOL_ZEROING_INFORMATION",
    "SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION",
    "SYSTEM_SUPPORTED_PROCESSOR_ARCHITECTURES_INFORMATION",
    "OSVERSIONINFOA",
    "OSVERSIONINFOW",
    "OSVERSIONINFOEXA",
    "OSVERSIONINFOEXW",
    "OS_DEPLOYEMENT_STATE_VALUES",
    "OS_DEPLOYMENT_STANDARD",
    "OS_DEPLOYMENT_COMPACT",
    "RTL_SYSTEM_GLOBAL_DATA_ID",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdUnknown",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdRngSeedVersion",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdInterruptTime",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdTimeZoneBias",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdImageNumberLow",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdImageNumberHigh",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdTimeZoneId",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdNtMajorVersion",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdNtMinorVersion",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdSystemExpirationDate",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdKdDebuggerEnabled",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdCyclesPerYield",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdSafeBootMode",
    "RTL_SYSTEM_GLOBAL_DATA_ID_GlobalDataIdLastSystemRITEventTickCount",
    "MEMORYSTATUS",
    "DEP_SYSTEM_POLICY_TYPE",
    "DEP_SYSTEM_POLICY_TYPE_DEPPolicyAlwaysOff",
    "DEP_SYSTEM_POLICY_TYPE_DEPPolicyAlwaysOn",
    "DEP_SYSTEM_POLICY_TYPE_DEPPolicyOptIn",
    "DEP_SYSTEM_POLICY_TYPE_DEPPolicyOptOut",
    "DEP_SYSTEM_POLICY_TYPE_DEPTotalPolicyCount",
    "PGET_SYSTEM_WOW64_DIRECTORY_A",
    "PGET_SYSTEM_WOW64_DIRECTORY_W",
    "GlobalMemoryStatusEx",
    "GetSystemInfo",
    "GetSystemTime",
    "GetSystemTimeAsFileTime",
    "GetLocalTime",
    "IsUserCetAvailableInEnvironment",
    "GetSystemLeapSecondInformation",
    "GetVersion",
    "SetLocalTime",
    "GetTickCount",
    "GetTickCount64",
    "GetSystemTimeAdjustment",
    "GetSystemTimeAdjustmentPrecise",
    "GetSystemDirectoryA",
    "GetSystemDirectoryW",
    "GetSystemDirectory",
    "GetWindowsDirectoryA",
    "GetWindowsDirectoryW",
    "GetWindowsDirectory",
    "GetSystemWindowsDirectoryA",
    "GetSystemWindowsDirectoryW",
    "GetSystemWindowsDirectory",
    "GetComputerNameExA",
    "GetComputerNameExW",
    "GetComputerNameEx",
    "SetComputerNameExW",
    "SetComputerNameEx",
    "SetSystemTime",
    "GetVersionExA",
    "GetVersionExW",
    "GetVersionEx",
    "GetLogicalProcessorInformation",
    "GetLogicalProcessorInformationEx",
    "GetNativeSystemInfo",
    "GetSystemTimePreciseAsFileTime",
    "GetProductInfo",
    "VerSetConditionMask",
    "GetOsSafeBootMode",
    "EnumSystemFirmwareTables",
    "GetSystemFirmwareTable",
    "DnsHostnameToComputerNameExW",
    "GetPhysicallyInstalledSystemMemory",
    "SetComputerNameEx2W",
    "SetSystemTimeAdjustment",
    "SetSystemTimeAdjustmentPrecise",
    "GetProcessorSystemCycleTime",
    "GetOsManufacturingMode",
    "GetIntegratedDisplaySize",
    "SetComputerNameA",
    "SetComputerNameW",
    "SetComputerName",
    "SetComputerNameExA",
    "GetSystemCpuSetInformation",
    "GetSystemWow64DirectoryA",
    "GetSystemWow64DirectoryW",
    "GetSystemWow64Directory",
    "GetSystemWow64Directory2A",
    "GetSystemWow64Directory2W",
    "GetSystemWow64Directory2",
    "IsWow64GuestMachineSupported",
    "RtlGetProductInfo",
    "RtlOsDeploymentState",
    "RtlGetSystemGlobalData",
    "RtlGetDeviceFamilyInfoEnum",
    "RtlConvertDeviceFamilyInfoToString",
    "RtlSwitchedVVI",
    "GlobalMemoryStatus",
    "GetSystemDEPPolicy",
    "GetFirmwareType",
    "VerifyVersionInfoA",
    "VerifyVersionInfoW",
    "VerifyVersionInfo",
]
