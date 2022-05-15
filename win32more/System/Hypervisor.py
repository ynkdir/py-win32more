from win32more import *
import win32more.System.Hypervisor
import win32more.Foundation
import win32more.System.HostComputeSystem
import win32more.System.Power

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.System.Hypervisor, name, globals()[f"_define_{name}"]())
    return getattr(win32more.System.Hypervisor, name)
def __dir__():
    return __all__
HVSOCKET_CONNECT_TIMEOUT = 1
HVSOCKET_CONNECT_TIMEOUT_MAX = 300000
HVSOCKET_CONTAINER_PASSTHRU = 2
HVSOCKET_CONNECTED_SUSPEND = 4
HV_PROTOCOL_RAW = 1
HVSOCKET_ADDRESS_FLAG_PASSTHRU = 1
WHV_PROCESSOR_FEATURES_BANKS_COUNT = 2
WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS_COUNT = 1
WHV_READ_WRITE_GPA_RANGE_MAX_SIZE = 16
WHV_HYPERCALL_CONTEXT_MAX_XMM_REGISTERS = 6
WHV_MAX_DEVICE_ID_SIZE_IN_CHARS = 200
WHV_VPCI_TYPE0_BAR_COUNT = 6
WHV_ANY_VP = 4294967295
WHV_SYNIC_MESSAGE_SIZE = 256
IOCTL_VMGENCOUNTER_READ = 3325956
HDV_PCI_BAR_COUNT = 6
HV_GUID_ZERO = '00000000-0000-0000-0000-000000000000'
HV_GUID_BROADCAST = 'ffffffff-ffff-ffff-ffff-ffffffffffff'
HV_GUID_CHILDREN = '90db8b89-0d35-4f79-8ce9-49ea0ac8b7cd'
HV_GUID_LOOPBACK = 'e0e16197-dd56-4a10-9195-5ee7a155a838'
HV_GUID_PARENT = 'a42e7cda-d03f-480c-9cc2-a4de20abb878'
HV_GUID_SILOHOST = '36bd0c5c-7276-4223-88ba-7d03b654c568'
HV_GUID_VSOCK_TEMPLATE = '00000000-facb-11e6-bd58-64006a7986d3'
GUID_DEVINTERFACE_VM_GENCOUNTER = '3ff2c92b-6598-4e60-8e1c-0ccf4927e319'
WHV_PARTITION_HANDLE = IntPtr
WHV_CAPABILITY_CODE = Int32
WHV_CAPABILITY_CODE_WHvCapabilityCodeHypervisorPresent = 0
WHV_CAPABILITY_CODE_WHvCapabilityCodeFeatures = 1
WHV_CAPABILITY_CODE_WHvCapabilityCodeExtendedVmExits = 2
WHV_CAPABILITY_CODE_WHvCapabilityCodeExceptionExitBitmap = 3
WHV_CAPABILITY_CODE_WHvCapabilityCodeX64MsrExitBitmap = 4
WHV_CAPABILITY_CODE_WHvCapabilityCodeGpaRangePopulateFlags = 5
WHV_CAPABILITY_CODE_WHvCapabilityCodeSchedulerFeatures = 6
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorVendor = 4096
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFeatures = 4097
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorClFlushSize = 4098
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorXsaveFeatures = 4099
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorClockFrequency = 4100
WHV_CAPABILITY_CODE_WHvCapabilityCodeInterruptClockFrequency = 4101
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFeaturesBanks = 4102
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFrequencyCap = 4103
WHV_CAPABILITY_CODE_WHvCapabilityCodeSyntheticProcessorFeaturesBanks = 4104
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorPerfmonFeatures = 4105
def _define_WHV_CAPABILITY_FEATURES_head():
    class WHV_CAPABILITY_FEATURES(Union):
        pass
    return WHV_CAPABILITY_FEATURES
def _define_WHV_CAPABILITY_FEATURES():
    WHV_CAPABILITY_FEATURES = win32more.System.Hypervisor.WHV_CAPABILITY_FEATURES_head
    class WHV_CAPABILITY_FEATURES__Anonymous_e__Struct(Structure):
        pass
    WHV_CAPABILITY_FEATURES__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_CAPABILITY_FEATURES._anonymous_ = [
        'Anonymous',
    ]
    WHV_CAPABILITY_FEATURES._fields_ = [
        ("Anonymous", WHV_CAPABILITY_FEATURES__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_CAPABILITY_FEATURES
def _define_WHV_EXTENDED_VM_EXITS_head():
    class WHV_EXTENDED_VM_EXITS(Union):
        pass
    return WHV_EXTENDED_VM_EXITS
def _define_WHV_EXTENDED_VM_EXITS():
    WHV_EXTENDED_VM_EXITS = win32more.System.Hypervisor.WHV_EXTENDED_VM_EXITS_head
    class WHV_EXTENDED_VM_EXITS__Anonymous_e__Struct(Structure):
        pass
    WHV_EXTENDED_VM_EXITS__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_EXTENDED_VM_EXITS._anonymous_ = [
        'Anonymous',
    ]
    WHV_EXTENDED_VM_EXITS._fields_ = [
        ("Anonymous", WHV_EXTENDED_VM_EXITS__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_EXTENDED_VM_EXITS
WHV_PROCESSOR_VENDOR = Int32
WHV_PROCESSOR_VENDOR_WHvProcessorVendorAmd = 0
WHV_PROCESSOR_VENDOR_WHvProcessorVendorIntel = 1
WHV_PROCESSOR_VENDOR_WHvProcessorVendorHygon = 2
def _define_WHV_PROCESSOR_FEATURES_head():
    class WHV_PROCESSOR_FEATURES(Union):
        pass
    return WHV_PROCESSOR_FEATURES
def _define_WHV_PROCESSOR_FEATURES():
    WHV_PROCESSOR_FEATURES = win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES_head
    class WHV_PROCESSOR_FEATURES__Anonymous_e__Struct(Structure):
        pass
    WHV_PROCESSOR_FEATURES__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_PROCESSOR_FEATURES._anonymous_ = [
        'Anonymous',
    ]
    WHV_PROCESSOR_FEATURES._fields_ = [
        ("Anonymous", WHV_PROCESSOR_FEATURES__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_PROCESSOR_FEATURES
def _define_WHV_PROCESSOR_FEATURES1_head():
    class WHV_PROCESSOR_FEATURES1(Union):
        pass
    return WHV_PROCESSOR_FEATURES1
def _define_WHV_PROCESSOR_FEATURES1():
    WHV_PROCESSOR_FEATURES1 = win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES1_head
    class WHV_PROCESSOR_FEATURES1__Anonymous_e__Struct(Structure):
        pass
    WHV_PROCESSOR_FEATURES1__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_PROCESSOR_FEATURES1._anonymous_ = [
        'Anonymous',
    ]
    WHV_PROCESSOR_FEATURES1._fields_ = [
        ("Anonymous", WHV_PROCESSOR_FEATURES1__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_PROCESSOR_FEATURES1
def _define_WHV_PROCESSOR_FEATURES_BANKS_head():
    class WHV_PROCESSOR_FEATURES_BANKS(Structure):
        pass
    return WHV_PROCESSOR_FEATURES_BANKS
def _define_WHV_PROCESSOR_FEATURES_BANKS():
    WHV_PROCESSOR_FEATURES_BANKS = win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES_BANKS_head
    class WHV_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union(Union):
        pass
    class WHV_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    WHV_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Bank0", win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES),
        ("Bank1", win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES1),
    ]
    WHV_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    WHV_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union._fields_ = [
        ("Anonymous", WHV_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union__Anonymous_e__Struct),
        ("AsUINT64", UInt64 * 2),
    ]
    WHV_PROCESSOR_FEATURES_BANKS._anonymous_ = [
        'Anonymous',
    ]
    WHV_PROCESSOR_FEATURES_BANKS._fields_ = [
        ("BanksCount", UInt32),
        ("Reserved0", UInt32),
        ("Anonymous", WHV_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union),
    ]
    return WHV_PROCESSOR_FEATURES_BANKS
def _define_WHV_SYNTHETIC_PROCESSOR_FEATURES_head():
    class WHV_SYNTHETIC_PROCESSOR_FEATURES(Union):
        pass
    return WHV_SYNTHETIC_PROCESSOR_FEATURES
def _define_WHV_SYNTHETIC_PROCESSOR_FEATURES():
    WHV_SYNTHETIC_PROCESSOR_FEATURES = win32more.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_head
    class WHV_SYNTHETIC_PROCESSOR_FEATURES__Anonymous_e__Struct(Structure):
        pass
    WHV_SYNTHETIC_PROCESSOR_FEATURES__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_SYNTHETIC_PROCESSOR_FEATURES._anonymous_ = [
        'Anonymous',
    ]
    WHV_SYNTHETIC_PROCESSOR_FEATURES._fields_ = [
        ("Anonymous", WHV_SYNTHETIC_PROCESSOR_FEATURES__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_SYNTHETIC_PROCESSOR_FEATURES
def _define_WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS_head():
    class WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS(Structure):
        pass
    return WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS
def _define_WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS():
    WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS = win32more.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS_head
    class WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union(Union):
        pass
    class WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Bank0", win32more.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES),
    ]
    WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union._fields_ = [
        ("Anonymous", WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union__Anonymous_e__Struct),
        ("AsUINT64", UInt64 * 0),
    ]
    WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS._anonymous_ = [
        'Anonymous',
    ]
    WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS._fields_ = [
        ("BanksCount", UInt32),
        ("Reserved0", UInt32),
        ("Anonymous", WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS__Anonymous_e__Union),
    ]
    return WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS
WHV_PARTITION_PROPERTY_CODE = Int32
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeExtendedVmExits = 1
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeExceptionExitBitmap = 2
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeSeparateSecurityDomain = 3
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeNestedVirtualization = 4
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeX64MsrExitBitmap = 5
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodePrimaryNumaNode = 6
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuReserve = 7
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuCap = 8
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuWeight = 9
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuGroupId = 10
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFrequencyCap = 11
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeAllowDeviceAssignment = 12
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeDisableSmt = 13
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFeatures = 4097
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorClFlushSize = 4098
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidExitList = 4099
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidResultList = 4100
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeLocalApicEmulationMode = 4101
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorXsaveFeatures = 4102
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorClockFrequency = 4103
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeInterruptClockFrequency = 4104
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeApicRemoteReadSupport = 4105
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFeaturesBanks = 4106
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeReferenceTime = 4107
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeSyntheticProcessorFeaturesBanks = 4108
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidResultList2 = 4109
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorPerfmonFeatures = 4110
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeMsrActionList = 4111
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeUnimplementedMsrAction = 4112
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorCount = 8191
def _define_WHV_PROCESSOR_XSAVE_FEATURES_head():
    class WHV_PROCESSOR_XSAVE_FEATURES(Union):
        pass
    return WHV_PROCESSOR_XSAVE_FEATURES
def _define_WHV_PROCESSOR_XSAVE_FEATURES():
    WHV_PROCESSOR_XSAVE_FEATURES = win32more.System.Hypervisor.WHV_PROCESSOR_XSAVE_FEATURES_head
    class WHV_PROCESSOR_XSAVE_FEATURES__Anonymous_e__Struct(Structure):
        pass
    WHV_PROCESSOR_XSAVE_FEATURES__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_PROCESSOR_XSAVE_FEATURES._anonymous_ = [
        'Anonymous',
    ]
    WHV_PROCESSOR_XSAVE_FEATURES._fields_ = [
        ("Anonymous", WHV_PROCESSOR_XSAVE_FEATURES__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_PROCESSOR_XSAVE_FEATURES
def _define_WHV_PROCESSOR_PERFMON_FEATURES_head():
    class WHV_PROCESSOR_PERFMON_FEATURES(Union):
        pass
    return WHV_PROCESSOR_PERFMON_FEATURES
def _define_WHV_PROCESSOR_PERFMON_FEATURES():
    WHV_PROCESSOR_PERFMON_FEATURES = win32more.System.Hypervisor.WHV_PROCESSOR_PERFMON_FEATURES_head
    class WHV_PROCESSOR_PERFMON_FEATURES__Anonymous_e__Struct(Structure):
        pass
    WHV_PROCESSOR_PERFMON_FEATURES__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_PROCESSOR_PERFMON_FEATURES._anonymous_ = [
        'Anonymous',
    ]
    WHV_PROCESSOR_PERFMON_FEATURES._fields_ = [
        ("Anonymous", WHV_PROCESSOR_PERFMON_FEATURES__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_PROCESSOR_PERFMON_FEATURES
def _define_WHV_X64_MSR_EXIT_BITMAP_head():
    class WHV_X64_MSR_EXIT_BITMAP(Union):
        pass
    return WHV_X64_MSR_EXIT_BITMAP
def _define_WHV_X64_MSR_EXIT_BITMAP():
    WHV_X64_MSR_EXIT_BITMAP = win32more.System.Hypervisor.WHV_X64_MSR_EXIT_BITMAP_head
    class WHV_X64_MSR_EXIT_BITMAP__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_MSR_EXIT_BITMAP__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_X64_MSR_EXIT_BITMAP._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_MSR_EXIT_BITMAP._fields_ = [
        ("AsUINT64", UInt64),
        ("Anonymous", WHV_X64_MSR_EXIT_BITMAP__Anonymous_e__Struct),
    ]
    return WHV_X64_MSR_EXIT_BITMAP
def _define_WHV_MEMORY_RANGE_ENTRY_head():
    class WHV_MEMORY_RANGE_ENTRY(Structure):
        pass
    return WHV_MEMORY_RANGE_ENTRY
def _define_WHV_MEMORY_RANGE_ENTRY():
    WHV_MEMORY_RANGE_ENTRY = win32more.System.Hypervisor.WHV_MEMORY_RANGE_ENTRY_head
    WHV_MEMORY_RANGE_ENTRY._fields_ = [
        ("GuestAddress", UInt64),
        ("SizeInBytes", UInt64),
    ]
    return WHV_MEMORY_RANGE_ENTRY
def _define_WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS_head():
    class WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS(Union):
        pass
    return WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS
def _define_WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS():
    WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS = win32more.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS_head
    class WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS__Anonymous_e__Struct(Structure):
        pass
    WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS._anonymous_ = [
        'Anonymous',
    ]
    WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS._fields_ = [
        ("AsUINT32", UInt32),
        ("Anonymous", WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS__Anonymous_e__Struct),
    ]
    return WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS
WHV_MEMORY_ACCESS_TYPE = Int32
WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessRead = 0
WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessWrite = 1
WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessExecute = 2
def _define_WHV_ADVISE_GPA_RANGE_POPULATE_head():
    class WHV_ADVISE_GPA_RANGE_POPULATE(Structure):
        pass
    return WHV_ADVISE_GPA_RANGE_POPULATE
def _define_WHV_ADVISE_GPA_RANGE_POPULATE():
    WHV_ADVISE_GPA_RANGE_POPULATE = win32more.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE_head
    WHV_ADVISE_GPA_RANGE_POPULATE._fields_ = [
        ("Flags", win32more.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS),
        ("AccessType", win32more.System.Hypervisor.WHV_MEMORY_ACCESS_TYPE),
    ]
    return WHV_ADVISE_GPA_RANGE_POPULATE
def _define_WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP_head():
    class WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP(Structure):
        pass
    return WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP
def _define_WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP():
    WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP = win32more.System.Hypervisor.WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP_head
    WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP._fields_ = [
        ("_bitfield", UInt32),
        ("HighestFrequencyMhz", UInt32),
        ("NominalFrequencyMhz", UInt32),
        ("LowestFrequencyMhz", UInt32),
        ("FrequencyStepMhz", UInt32),
    ]
    return WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP
def _define_WHV_SCHEDULER_FEATURES_head():
    class WHV_SCHEDULER_FEATURES(Union):
        pass
    return WHV_SCHEDULER_FEATURES
def _define_WHV_SCHEDULER_FEATURES():
    WHV_SCHEDULER_FEATURES = win32more.System.Hypervisor.WHV_SCHEDULER_FEATURES_head
    class WHV_SCHEDULER_FEATURES__Anonymous_e__Struct(Structure):
        pass
    WHV_SCHEDULER_FEATURES__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_SCHEDULER_FEATURES._anonymous_ = [
        'Anonymous',
    ]
    WHV_SCHEDULER_FEATURES._fields_ = [
        ("Anonymous", WHV_SCHEDULER_FEATURES__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_SCHEDULER_FEATURES
def _define_WHV_CAPABILITY_head():
    class WHV_CAPABILITY(Union):
        pass
    return WHV_CAPABILITY
def _define_WHV_CAPABILITY():
    WHV_CAPABILITY = win32more.System.Hypervisor.WHV_CAPABILITY_head
    WHV_CAPABILITY._fields_ = [
        ("HypervisorPresent", win32more.Foundation.BOOL),
        ("Features", win32more.System.Hypervisor.WHV_CAPABILITY_FEATURES),
        ("ExtendedVmExits", win32more.System.Hypervisor.WHV_EXTENDED_VM_EXITS),
        ("ProcessorVendor", win32more.System.Hypervisor.WHV_PROCESSOR_VENDOR),
        ("ProcessorFeatures", win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES),
        ("SyntheticProcessorFeaturesBanks", win32more.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS),
        ("ProcessorXsaveFeatures", win32more.System.Hypervisor.WHV_PROCESSOR_XSAVE_FEATURES),
        ("ProcessorClFlushSize", Byte),
        ("ExceptionExitBitmap", UInt64),
        ("X64MsrExitBitmap", win32more.System.Hypervisor.WHV_X64_MSR_EXIT_BITMAP),
        ("ProcessorClockFrequency", UInt64),
        ("InterruptClockFrequency", UInt64),
        ("ProcessorFeaturesBanks", win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES_BANKS),
        ("GpaRangePopulateFlags", win32more.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS),
        ("ProcessorFrequencyCap", win32more.System.Hypervisor.WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP),
        ("ProcessorPerfmonFeatures", win32more.System.Hypervisor.WHV_PROCESSOR_PERFMON_FEATURES),
        ("SchedulerFeatures", win32more.System.Hypervisor.WHV_SCHEDULER_FEATURES),
    ]
    return WHV_CAPABILITY
def _define_WHV_X64_CPUID_RESULT_head():
    class WHV_X64_CPUID_RESULT(Structure):
        pass
    return WHV_X64_CPUID_RESULT
def _define_WHV_X64_CPUID_RESULT():
    WHV_X64_CPUID_RESULT = win32more.System.Hypervisor.WHV_X64_CPUID_RESULT_head
    WHV_X64_CPUID_RESULT._fields_ = [
        ("Function", UInt32),
        ("Reserved", UInt32 * 3),
        ("Eax", UInt32),
        ("Ebx", UInt32),
        ("Ecx", UInt32),
        ("Edx", UInt32),
    ]
    return WHV_X64_CPUID_RESULT
WHV_X64_CPUID_RESULT2_FLAGS = UInt32
WHV_X64_CPUID_RESULT2_FLAGS_WHvX64CpuidResult2FlagSubleafSpecific = 1
WHV_X64_CPUID_RESULT2_FLAGS_WHvX64CpuidResult2FlagVpSpecific = 2
def _define_WHV_CPUID_OUTPUT_head():
    class WHV_CPUID_OUTPUT(Structure):
        pass
    return WHV_CPUID_OUTPUT
def _define_WHV_CPUID_OUTPUT():
    WHV_CPUID_OUTPUT = win32more.System.Hypervisor.WHV_CPUID_OUTPUT_head
    WHV_CPUID_OUTPUT._fields_ = [
        ("Eax", UInt32),
        ("Ebx", UInt32),
        ("Ecx", UInt32),
        ("Edx", UInt32),
    ]
    return WHV_CPUID_OUTPUT
def _define_WHV_X64_CPUID_RESULT2_head():
    class WHV_X64_CPUID_RESULT2(Structure):
        pass
    return WHV_X64_CPUID_RESULT2
def _define_WHV_X64_CPUID_RESULT2():
    WHV_X64_CPUID_RESULT2 = win32more.System.Hypervisor.WHV_X64_CPUID_RESULT2_head
    WHV_X64_CPUID_RESULT2._fields_ = [
        ("Function", UInt32),
        ("Index", UInt32),
        ("VpIndex", UInt32),
        ("Flags", win32more.System.Hypervisor.WHV_X64_CPUID_RESULT2_FLAGS),
        ("Output", win32more.System.Hypervisor.WHV_CPUID_OUTPUT),
        ("Mask", win32more.System.Hypervisor.WHV_CPUID_OUTPUT),
    ]
    return WHV_X64_CPUID_RESULT2
def _define_WHV_MSR_ACTION_ENTRY_head():
    class WHV_MSR_ACTION_ENTRY(Structure):
        pass
    return WHV_MSR_ACTION_ENTRY
def _define_WHV_MSR_ACTION_ENTRY():
    WHV_MSR_ACTION_ENTRY = win32more.System.Hypervisor.WHV_MSR_ACTION_ENTRY_head
    WHV_MSR_ACTION_ENTRY._fields_ = [
        ("Index", UInt32),
        ("ReadAction", Byte),
        ("WriteAction", Byte),
        ("Reserved", UInt16),
    ]
    return WHV_MSR_ACTION_ENTRY
WHV_MSR_ACTION = Int32
WHV_MSR_ACTION_WHvMsrActionArchitectureDefault = 0
WHV_MSR_ACTION_WHvMsrActionIgnoreWriteReadZero = 1
WHV_MSR_ACTION_WHvMsrActionExit = 2
WHV_EXCEPTION_TYPE = Int32
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDivideErrorFault = 0
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDebugTrapOrFault = 1
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeBreakpointTrap = 3
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeOverflowTrap = 4
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeBoundRangeFault = 5
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeInvalidOpcodeFault = 6
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDeviceNotAvailableFault = 7
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDoubleFaultAbort = 8
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeInvalidTaskStateSegmentFault = 10
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeSegmentNotPresentFault = 11
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeStackFault = 12
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeGeneralProtectionFault = 13
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypePageFault = 14
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeFloatingPointErrorFault = 16
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeAlignmentCheckFault = 17
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeMachineCheckAbort = 18
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeSimdFloatingPointFault = 19
WHV_X64_LOCAL_APIC_EMULATION_MODE = Int32
WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeNone = 0
WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeXApic = 1
WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeX2Apic = 2
def _define_WHV_PARTITION_PROPERTY_head():
    class WHV_PARTITION_PROPERTY(Union):
        pass
    return WHV_PARTITION_PROPERTY
def _define_WHV_PARTITION_PROPERTY():
    WHV_PARTITION_PROPERTY = win32more.System.Hypervisor.WHV_PARTITION_PROPERTY_head
    WHV_PARTITION_PROPERTY._fields_ = [
        ("ExtendedVmExits", win32more.System.Hypervisor.WHV_EXTENDED_VM_EXITS),
        ("ProcessorFeatures", win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES),
        ("SyntheticProcessorFeaturesBanks", win32more.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS),
        ("ProcessorXsaveFeatures", win32more.System.Hypervisor.WHV_PROCESSOR_XSAVE_FEATURES),
        ("ProcessorClFlushSize", Byte),
        ("ProcessorCount", UInt32),
        ("CpuidExitList", UInt32 * 0),
        ("CpuidResultList", win32more.System.Hypervisor.WHV_X64_CPUID_RESULT * 0),
        ("CpuidResultList2", win32more.System.Hypervisor.WHV_X64_CPUID_RESULT2 * 0),
        ("MsrActionList", win32more.System.Hypervisor.WHV_MSR_ACTION_ENTRY * 0),
        ("UnimplementedMsrAction", win32more.System.Hypervisor.WHV_MSR_ACTION),
        ("ExceptionExitBitmap", UInt64),
        ("LocalApicEmulationMode", win32more.System.Hypervisor.WHV_X64_LOCAL_APIC_EMULATION_MODE),
        ("SeparateSecurityDomain", win32more.Foundation.BOOL),
        ("NestedVirtualization", win32more.Foundation.BOOL),
        ("X64MsrExitBitmap", win32more.System.Hypervisor.WHV_X64_MSR_EXIT_BITMAP),
        ("ProcessorClockFrequency", UInt64),
        ("InterruptClockFrequency", UInt64),
        ("ApicRemoteRead", win32more.Foundation.BOOL),
        ("ProcessorFeaturesBanks", win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES_BANKS),
        ("ReferenceTime", UInt64),
        ("PrimaryNumaNode", UInt16),
        ("CpuReserve", UInt32),
        ("CpuCap", UInt32),
        ("CpuWeight", UInt32),
        ("CpuGroupId", UInt64),
        ("ProcessorFrequencyCap", UInt32),
        ("AllowDeviceAssignment", win32more.Foundation.BOOL),
        ("ProcessorPerfmonFeatures", win32more.System.Hypervisor.WHV_PROCESSOR_PERFMON_FEATURES),
        ("DisableSmt", win32more.Foundation.BOOL),
    ]
    return WHV_PARTITION_PROPERTY
WHV_MAP_GPA_RANGE_FLAGS = UInt32
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagNone = 0
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagRead = 1
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagWrite = 2
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagExecute = 4
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagTrackDirtyPages = 8
WHV_TRANSLATE_GVA_FLAGS = UInt32
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagNone = 0
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateRead = 1
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateWrite = 2
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateExecute = 4
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagPrivilegeExempt = 8
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagSetPageTableBits = 16
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagEnforceSmap = 256
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagOverrideSmap = 512
WHV_TRANSLATE_GVA_RESULT_CODE = Int32
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultSuccess = 0
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultPageNotPresent = 1
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultPrivilegeViolation = 2
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultInvalidPageTableFlags = 3
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaUnmapped = 4
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaNoReadAccess = 5
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaNoWriteAccess = 6
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaIllegalOverlayAccess = 7
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultIntercept = 8
def _define_WHV_TRANSLATE_GVA_RESULT_head():
    class WHV_TRANSLATE_GVA_RESULT(Structure):
        pass
    return WHV_TRANSLATE_GVA_RESULT
def _define_WHV_TRANSLATE_GVA_RESULT():
    WHV_TRANSLATE_GVA_RESULT = win32more.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_head
    WHV_TRANSLATE_GVA_RESULT._fields_ = [
        ("ResultCode", win32more.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE),
        ("Reserved", UInt32),
    ]
    return WHV_TRANSLATE_GVA_RESULT
def _define_WHV_ADVISE_GPA_RANGE_head():
    class WHV_ADVISE_GPA_RANGE(Union):
        pass
    return WHV_ADVISE_GPA_RANGE
def _define_WHV_ADVISE_GPA_RANGE():
    WHV_ADVISE_GPA_RANGE = win32more.System.Hypervisor.WHV_ADVISE_GPA_RANGE_head
    WHV_ADVISE_GPA_RANGE._fields_ = [
        ("Populate", win32more.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE),
    ]
    return WHV_ADVISE_GPA_RANGE
WHV_CACHE_TYPE = Int32
WHV_CACHE_TYPE_WHvCacheTypeUncached = 0
WHV_CACHE_TYPE_WHvCacheTypeWriteCombining = 1
WHV_CACHE_TYPE_WHvCacheTypeWriteThrough = 4
WHV_CACHE_TYPE_WHvCacheTypeWriteProtected = 5
WHV_CACHE_TYPE_WHvCacheTypeWriteBack = 6
def _define_WHV_ACCESS_GPA_CONTROLS_head():
    class WHV_ACCESS_GPA_CONTROLS(Union):
        pass
    return WHV_ACCESS_GPA_CONTROLS
def _define_WHV_ACCESS_GPA_CONTROLS():
    WHV_ACCESS_GPA_CONTROLS = win32more.System.Hypervisor.WHV_ACCESS_GPA_CONTROLS_head
    class WHV_ACCESS_GPA_CONTROLS__Anonymous_e__Struct(Structure):
        pass
    WHV_ACCESS_GPA_CONTROLS__Anonymous_e__Struct._fields_ = [
        ("CacheType", win32more.System.Hypervisor.WHV_CACHE_TYPE),
        ("Reserved", UInt32),
    ]
    WHV_ACCESS_GPA_CONTROLS._anonymous_ = [
        'Anonymous',
    ]
    WHV_ACCESS_GPA_CONTROLS._fields_ = [
        ("AsUINT64", UInt64),
        ("Anonymous", WHV_ACCESS_GPA_CONTROLS__Anonymous_e__Struct),
    ]
    return WHV_ACCESS_GPA_CONTROLS
WHV_REGISTER_NAME = Int32
WHV_REGISTER_NAME_WHvX64RegisterRax = 0
WHV_REGISTER_NAME_WHvX64RegisterRcx = 1
WHV_REGISTER_NAME_WHvX64RegisterRdx = 2
WHV_REGISTER_NAME_WHvX64RegisterRbx = 3
WHV_REGISTER_NAME_WHvX64RegisterRsp = 4
WHV_REGISTER_NAME_WHvX64RegisterRbp = 5
WHV_REGISTER_NAME_WHvX64RegisterRsi = 6
WHV_REGISTER_NAME_WHvX64RegisterRdi = 7
WHV_REGISTER_NAME_WHvX64RegisterR8 = 8
WHV_REGISTER_NAME_WHvX64RegisterR9 = 9
WHV_REGISTER_NAME_WHvX64RegisterR10 = 10
WHV_REGISTER_NAME_WHvX64RegisterR11 = 11
WHV_REGISTER_NAME_WHvX64RegisterR12 = 12
WHV_REGISTER_NAME_WHvX64RegisterR13 = 13
WHV_REGISTER_NAME_WHvX64RegisterR14 = 14
WHV_REGISTER_NAME_WHvX64RegisterR15 = 15
WHV_REGISTER_NAME_WHvX64RegisterRip = 16
WHV_REGISTER_NAME_WHvX64RegisterRflags = 17
WHV_REGISTER_NAME_WHvX64RegisterEs = 18
WHV_REGISTER_NAME_WHvX64RegisterCs = 19
WHV_REGISTER_NAME_WHvX64RegisterSs = 20
WHV_REGISTER_NAME_WHvX64RegisterDs = 21
WHV_REGISTER_NAME_WHvX64RegisterFs = 22
WHV_REGISTER_NAME_WHvX64RegisterGs = 23
WHV_REGISTER_NAME_WHvX64RegisterLdtr = 24
WHV_REGISTER_NAME_WHvX64RegisterTr = 25
WHV_REGISTER_NAME_WHvX64RegisterIdtr = 26
WHV_REGISTER_NAME_WHvX64RegisterGdtr = 27
WHV_REGISTER_NAME_WHvX64RegisterCr0 = 28
WHV_REGISTER_NAME_WHvX64RegisterCr2 = 29
WHV_REGISTER_NAME_WHvX64RegisterCr3 = 30
WHV_REGISTER_NAME_WHvX64RegisterCr4 = 31
WHV_REGISTER_NAME_WHvX64RegisterCr8 = 32
WHV_REGISTER_NAME_WHvX64RegisterDr0 = 33
WHV_REGISTER_NAME_WHvX64RegisterDr1 = 34
WHV_REGISTER_NAME_WHvX64RegisterDr2 = 35
WHV_REGISTER_NAME_WHvX64RegisterDr3 = 36
WHV_REGISTER_NAME_WHvX64RegisterDr6 = 37
WHV_REGISTER_NAME_WHvX64RegisterDr7 = 38
WHV_REGISTER_NAME_WHvX64RegisterXCr0 = 39
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr0 = 40
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr3 = 41
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr4 = 42
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr8 = 43
WHV_REGISTER_NAME_WHvX64RegisterXmm0 = 4096
WHV_REGISTER_NAME_WHvX64RegisterXmm1 = 4097
WHV_REGISTER_NAME_WHvX64RegisterXmm2 = 4098
WHV_REGISTER_NAME_WHvX64RegisterXmm3 = 4099
WHV_REGISTER_NAME_WHvX64RegisterXmm4 = 4100
WHV_REGISTER_NAME_WHvX64RegisterXmm5 = 4101
WHV_REGISTER_NAME_WHvX64RegisterXmm6 = 4102
WHV_REGISTER_NAME_WHvX64RegisterXmm7 = 4103
WHV_REGISTER_NAME_WHvX64RegisterXmm8 = 4104
WHV_REGISTER_NAME_WHvX64RegisterXmm9 = 4105
WHV_REGISTER_NAME_WHvX64RegisterXmm10 = 4106
WHV_REGISTER_NAME_WHvX64RegisterXmm11 = 4107
WHV_REGISTER_NAME_WHvX64RegisterXmm12 = 4108
WHV_REGISTER_NAME_WHvX64RegisterXmm13 = 4109
WHV_REGISTER_NAME_WHvX64RegisterXmm14 = 4110
WHV_REGISTER_NAME_WHvX64RegisterXmm15 = 4111
WHV_REGISTER_NAME_WHvX64RegisterFpMmx0 = 4112
WHV_REGISTER_NAME_WHvX64RegisterFpMmx1 = 4113
WHV_REGISTER_NAME_WHvX64RegisterFpMmx2 = 4114
WHV_REGISTER_NAME_WHvX64RegisterFpMmx3 = 4115
WHV_REGISTER_NAME_WHvX64RegisterFpMmx4 = 4116
WHV_REGISTER_NAME_WHvX64RegisterFpMmx5 = 4117
WHV_REGISTER_NAME_WHvX64RegisterFpMmx6 = 4118
WHV_REGISTER_NAME_WHvX64RegisterFpMmx7 = 4119
WHV_REGISTER_NAME_WHvX64RegisterFpControlStatus = 4120
WHV_REGISTER_NAME_WHvX64RegisterXmmControlStatus = 4121
WHV_REGISTER_NAME_WHvX64RegisterTsc = 8192
WHV_REGISTER_NAME_WHvX64RegisterEfer = 8193
WHV_REGISTER_NAME_WHvX64RegisterKernelGsBase = 8194
WHV_REGISTER_NAME_WHvX64RegisterApicBase = 8195
WHV_REGISTER_NAME_WHvX64RegisterPat = 8196
WHV_REGISTER_NAME_WHvX64RegisterSysenterCs = 8197
WHV_REGISTER_NAME_WHvX64RegisterSysenterEip = 8198
WHV_REGISTER_NAME_WHvX64RegisterSysenterEsp = 8199
WHV_REGISTER_NAME_WHvX64RegisterStar = 8200
WHV_REGISTER_NAME_WHvX64RegisterLstar = 8201
WHV_REGISTER_NAME_WHvX64RegisterCstar = 8202
WHV_REGISTER_NAME_WHvX64RegisterSfmask = 8203
WHV_REGISTER_NAME_WHvX64RegisterInitialApicId = 8204
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrCap = 8205
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrDefType = 8206
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase0 = 8208
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase1 = 8209
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase2 = 8210
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase3 = 8211
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase4 = 8212
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase5 = 8213
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase6 = 8214
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase7 = 8215
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase8 = 8216
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase9 = 8217
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseA = 8218
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseB = 8219
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseC = 8220
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseD = 8221
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseE = 8222
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseF = 8223
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask0 = 8256
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask1 = 8257
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask2 = 8258
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask3 = 8259
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask4 = 8260
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask5 = 8261
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask6 = 8262
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask7 = 8263
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask8 = 8264
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask9 = 8265
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskA = 8266
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskB = 8267
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskC = 8268
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskD = 8269
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskE = 8270
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskF = 8271
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix64k00000 = 8304
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix16k80000 = 8305
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix16kA0000 = 8306
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kC0000 = 8307
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kC8000 = 8308
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kD0000 = 8309
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kD8000 = 8310
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kE0000 = 8311
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kE8000 = 8312
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kF0000 = 8313
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kF8000 = 8314
WHV_REGISTER_NAME_WHvX64RegisterTscAux = 8315
WHV_REGISTER_NAME_WHvX64RegisterBndcfgs = 8316
WHV_REGISTER_NAME_WHvX64RegisterMCount = 8318
WHV_REGISTER_NAME_WHvX64RegisterACount = 8319
WHV_REGISTER_NAME_WHvX64RegisterSpecCtrl = 8324
WHV_REGISTER_NAME_WHvX64RegisterPredCmd = 8325
WHV_REGISTER_NAME_WHvX64RegisterTscVirtualOffset = 8327
WHV_REGISTER_NAME_WHvX64RegisterTsxCtrl = 8328
WHV_REGISTER_NAME_WHvX64RegisterXss = 8331
WHV_REGISTER_NAME_WHvX64RegisterUCet = 8332
WHV_REGISTER_NAME_WHvX64RegisterSCet = 8333
WHV_REGISTER_NAME_WHvX64RegisterSsp = 8334
WHV_REGISTER_NAME_WHvX64RegisterPl0Ssp = 8335
WHV_REGISTER_NAME_WHvX64RegisterPl1Ssp = 8336
WHV_REGISTER_NAME_WHvX64RegisterPl2Ssp = 8337
WHV_REGISTER_NAME_WHvX64RegisterPl3Ssp = 8338
WHV_REGISTER_NAME_WHvX64RegisterInterruptSspTableAddr = 8339
WHV_REGISTER_NAME_WHvX64RegisterTscDeadline = 8341
WHV_REGISTER_NAME_WHvX64RegisterTscAdjust = 8342
WHV_REGISTER_NAME_WHvX64RegisterUmwaitControl = 8344
WHV_REGISTER_NAME_WHvX64RegisterXfd = 8345
WHV_REGISTER_NAME_WHvX64RegisterXfdErr = 8346
WHV_REGISTER_NAME_WHvX64RegisterApicId = 12290
WHV_REGISTER_NAME_WHvX64RegisterApicVersion = 12291
WHV_REGISTER_NAME_WHvX64RegisterApicTpr = 12296
WHV_REGISTER_NAME_WHvX64RegisterApicPpr = 12298
WHV_REGISTER_NAME_WHvX64RegisterApicEoi = 12299
WHV_REGISTER_NAME_WHvX64RegisterApicLdr = 12301
WHV_REGISTER_NAME_WHvX64RegisterApicSpurious = 12303
WHV_REGISTER_NAME_WHvX64RegisterApicIsr0 = 12304
WHV_REGISTER_NAME_WHvX64RegisterApicIsr1 = 12305
WHV_REGISTER_NAME_WHvX64RegisterApicIsr2 = 12306
WHV_REGISTER_NAME_WHvX64RegisterApicIsr3 = 12307
WHV_REGISTER_NAME_WHvX64RegisterApicIsr4 = 12308
WHV_REGISTER_NAME_WHvX64RegisterApicIsr5 = 12309
WHV_REGISTER_NAME_WHvX64RegisterApicIsr6 = 12310
WHV_REGISTER_NAME_WHvX64RegisterApicIsr7 = 12311
WHV_REGISTER_NAME_WHvX64RegisterApicTmr0 = 12312
WHV_REGISTER_NAME_WHvX64RegisterApicTmr1 = 12313
WHV_REGISTER_NAME_WHvX64RegisterApicTmr2 = 12314
WHV_REGISTER_NAME_WHvX64RegisterApicTmr3 = 12315
WHV_REGISTER_NAME_WHvX64RegisterApicTmr4 = 12316
WHV_REGISTER_NAME_WHvX64RegisterApicTmr5 = 12317
WHV_REGISTER_NAME_WHvX64RegisterApicTmr6 = 12318
WHV_REGISTER_NAME_WHvX64RegisterApicTmr7 = 12319
WHV_REGISTER_NAME_WHvX64RegisterApicIrr0 = 12320
WHV_REGISTER_NAME_WHvX64RegisterApicIrr1 = 12321
WHV_REGISTER_NAME_WHvX64RegisterApicIrr2 = 12322
WHV_REGISTER_NAME_WHvX64RegisterApicIrr3 = 12323
WHV_REGISTER_NAME_WHvX64RegisterApicIrr4 = 12324
WHV_REGISTER_NAME_WHvX64RegisterApicIrr5 = 12325
WHV_REGISTER_NAME_WHvX64RegisterApicIrr6 = 12326
WHV_REGISTER_NAME_WHvX64RegisterApicIrr7 = 12327
WHV_REGISTER_NAME_WHvX64RegisterApicEse = 12328
WHV_REGISTER_NAME_WHvX64RegisterApicIcr = 12336
WHV_REGISTER_NAME_WHvX64RegisterApicLvtTimer = 12338
WHV_REGISTER_NAME_WHvX64RegisterApicLvtThermal = 12339
WHV_REGISTER_NAME_WHvX64RegisterApicLvtPerfmon = 12340
WHV_REGISTER_NAME_WHvX64RegisterApicLvtLint0 = 12341
WHV_REGISTER_NAME_WHvX64RegisterApicLvtLint1 = 12342
WHV_REGISTER_NAME_WHvX64RegisterApicLvtError = 12343
WHV_REGISTER_NAME_WHvX64RegisterApicInitCount = 12344
WHV_REGISTER_NAME_WHvX64RegisterApicCurrentCount = 12345
WHV_REGISTER_NAME_WHvX64RegisterApicDivide = 12350
WHV_REGISTER_NAME_WHvX64RegisterApicSelfIpi = 12351
WHV_REGISTER_NAME_WHvRegisterSint0 = 16384
WHV_REGISTER_NAME_WHvRegisterSint1 = 16385
WHV_REGISTER_NAME_WHvRegisterSint2 = 16386
WHV_REGISTER_NAME_WHvRegisterSint3 = 16387
WHV_REGISTER_NAME_WHvRegisterSint4 = 16388
WHV_REGISTER_NAME_WHvRegisterSint5 = 16389
WHV_REGISTER_NAME_WHvRegisterSint6 = 16390
WHV_REGISTER_NAME_WHvRegisterSint7 = 16391
WHV_REGISTER_NAME_WHvRegisterSint8 = 16392
WHV_REGISTER_NAME_WHvRegisterSint9 = 16393
WHV_REGISTER_NAME_WHvRegisterSint10 = 16394
WHV_REGISTER_NAME_WHvRegisterSint11 = 16395
WHV_REGISTER_NAME_WHvRegisterSint12 = 16396
WHV_REGISTER_NAME_WHvRegisterSint13 = 16397
WHV_REGISTER_NAME_WHvRegisterSint14 = 16398
WHV_REGISTER_NAME_WHvRegisterSint15 = 16399
WHV_REGISTER_NAME_WHvRegisterScontrol = 16400
WHV_REGISTER_NAME_WHvRegisterSversion = 16401
WHV_REGISTER_NAME_WHvRegisterSiefp = 16402
WHV_REGISTER_NAME_WHvRegisterSimp = 16403
WHV_REGISTER_NAME_WHvRegisterEom = 16404
WHV_REGISTER_NAME_WHvRegisterVpRuntime = 20480
WHV_REGISTER_NAME_WHvX64RegisterHypercall = 20481
WHV_REGISTER_NAME_WHvRegisterGuestOsId = 20482
WHV_REGISTER_NAME_WHvRegisterVpAssistPage = 20499
WHV_REGISTER_NAME_WHvRegisterReferenceTsc = 20503
WHV_REGISTER_NAME_WHvRegisterReferenceTscSequence = 20506
WHV_REGISTER_NAME_WHvRegisterPendingInterruption = -2147483648
WHV_REGISTER_NAME_WHvRegisterInterruptState = -2147483647
WHV_REGISTER_NAME_WHvRegisterPendingEvent = -2147483646
WHV_REGISTER_NAME_WHvX64RegisterDeliverabilityNotifications = -2147483644
WHV_REGISTER_NAME_WHvRegisterInternalActivityState = -2147483643
WHV_REGISTER_NAME_WHvX64RegisterPendingDebugException = -2147483642
def _define_WHV_UINT128_head():
    class WHV_UINT128(Union):
        pass
    return WHV_UINT128
def _define_WHV_UINT128():
    WHV_UINT128 = win32more.System.Hypervisor.WHV_UINT128_head
    class WHV_UINT128__Anonymous_e__Struct(Structure):
        pass
    WHV_UINT128__Anonymous_e__Struct._fields_ = [
        ("Low64", UInt64),
        ("High64", UInt64),
    ]
    WHV_UINT128._anonymous_ = [
        'Anonymous',
    ]
    WHV_UINT128._fields_ = [
        ("Anonymous", WHV_UINT128__Anonymous_e__Struct),
        ("Dword", UInt32 * 4),
    ]
    return WHV_UINT128
def _define_WHV_X64_FP_REGISTER_head():
    class WHV_X64_FP_REGISTER(Union):
        pass
    return WHV_X64_FP_REGISTER
def _define_WHV_X64_FP_REGISTER():
    WHV_X64_FP_REGISTER = win32more.System.Hypervisor.WHV_X64_FP_REGISTER_head
    class WHV_X64_FP_REGISTER__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_FP_REGISTER__Anonymous_e__Struct._fields_ = [
        ("Mantissa", UInt64),
        ("_bitfield", UInt64),
    ]
    WHV_X64_FP_REGISTER._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_FP_REGISTER._fields_ = [
        ("Anonymous", WHV_X64_FP_REGISTER__Anonymous_e__Struct),
        ("AsUINT128", win32more.System.Hypervisor.WHV_UINT128),
    ]
    return WHV_X64_FP_REGISTER
def _define_WHV_X64_FP_CONTROL_STATUS_REGISTER_head():
    class WHV_X64_FP_CONTROL_STATUS_REGISTER(Union):
        pass
    return WHV_X64_FP_CONTROL_STATUS_REGISTER
def _define_WHV_X64_FP_CONTROL_STATUS_REGISTER():
    WHV_X64_FP_CONTROL_STATUS_REGISTER = win32more.System.Hypervisor.WHV_X64_FP_CONTROL_STATUS_REGISTER_head
    class WHV_X64_FP_CONTROL_STATUS_REGISTER__Anonymous_e__Struct(Structure):
        pass
    class WHV_X64_FP_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union(Union):
        pass
    class WHV_X64_FP_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_FP_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("LastFpEip", UInt32),
        ("LastFpCs", UInt16),
        ("Reserved2", UInt16),
    ]
    WHV_X64_FP_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_FP_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union._fields_ = [
        ("LastFpRip", UInt64),
        ("Anonymous", WHV_X64_FP_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    WHV_X64_FP_CONTROL_STATUS_REGISTER__Anonymous_e__Struct._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_FP_CONTROL_STATUS_REGISTER__Anonymous_e__Struct._fields_ = [
        ("FpControl", UInt16),
        ("FpStatus", UInt16),
        ("FpTag", Byte),
        ("Reserved", Byte),
        ("LastFpOp", UInt16),
        ("Anonymous", WHV_X64_FP_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union),
    ]
    WHV_X64_FP_CONTROL_STATUS_REGISTER._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_FP_CONTROL_STATUS_REGISTER._fields_ = [
        ("Anonymous", WHV_X64_FP_CONTROL_STATUS_REGISTER__Anonymous_e__Struct),
        ("AsUINT128", win32more.System.Hypervisor.WHV_UINT128),
    ]
    return WHV_X64_FP_CONTROL_STATUS_REGISTER
def _define_WHV_X64_XMM_CONTROL_STATUS_REGISTER_head():
    class WHV_X64_XMM_CONTROL_STATUS_REGISTER(Union):
        pass
    return WHV_X64_XMM_CONTROL_STATUS_REGISTER
def _define_WHV_X64_XMM_CONTROL_STATUS_REGISTER():
    WHV_X64_XMM_CONTROL_STATUS_REGISTER = win32more.System.Hypervisor.WHV_X64_XMM_CONTROL_STATUS_REGISTER_head
    class WHV_X64_XMM_CONTROL_STATUS_REGISTER__Anonymous_e__Struct(Structure):
        pass
    class WHV_X64_XMM_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union(Union):
        pass
    class WHV_X64_XMM_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_XMM_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("LastFpDp", UInt32),
        ("LastFpDs", UInt16),
        ("Reserved", UInt16),
    ]
    WHV_X64_XMM_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_XMM_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union._fields_ = [
        ("LastFpRdp", UInt64),
        ("Anonymous", WHV_X64_XMM_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    WHV_X64_XMM_CONTROL_STATUS_REGISTER__Anonymous_e__Struct._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_XMM_CONTROL_STATUS_REGISTER__Anonymous_e__Struct._fields_ = [
        ("Anonymous", WHV_X64_XMM_CONTROL_STATUS_REGISTER__Anonymous_e__Struct__Anonymous_e__Union),
        ("XmmStatusControl", UInt32),
        ("XmmStatusControlMask", UInt32),
    ]
    WHV_X64_XMM_CONTROL_STATUS_REGISTER._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_XMM_CONTROL_STATUS_REGISTER._fields_ = [
        ("Anonymous", WHV_X64_XMM_CONTROL_STATUS_REGISTER__Anonymous_e__Struct),
        ("AsUINT128", win32more.System.Hypervisor.WHV_UINT128),
    ]
    return WHV_X64_XMM_CONTROL_STATUS_REGISTER
def _define_WHV_X64_SEGMENT_REGISTER_head():
    class WHV_X64_SEGMENT_REGISTER(Structure):
        pass
    return WHV_X64_SEGMENT_REGISTER
def _define_WHV_X64_SEGMENT_REGISTER():
    WHV_X64_SEGMENT_REGISTER = win32more.System.Hypervisor.WHV_X64_SEGMENT_REGISTER_head
    class WHV_X64_SEGMENT_REGISTER__Anonymous_e__Union(Union):
        pass
    class WHV_X64_SEGMENT_REGISTER__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_SEGMENT_REGISTER__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt16),
    ]
    WHV_X64_SEGMENT_REGISTER__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_SEGMENT_REGISTER__Anonymous_e__Union._fields_ = [
        ("Anonymous", WHV_X64_SEGMENT_REGISTER__Anonymous_e__Union__Anonymous_e__Struct),
        ("Attributes", UInt16),
    ]
    WHV_X64_SEGMENT_REGISTER._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_SEGMENT_REGISTER._fields_ = [
        ("Base", UInt64),
        ("Limit", UInt32),
        ("Selector", UInt16),
        ("Anonymous", WHV_X64_SEGMENT_REGISTER__Anonymous_e__Union),
    ]
    return WHV_X64_SEGMENT_REGISTER
def _define_WHV_X64_TABLE_REGISTER_head():
    class WHV_X64_TABLE_REGISTER(Structure):
        pass
    return WHV_X64_TABLE_REGISTER
def _define_WHV_X64_TABLE_REGISTER():
    WHV_X64_TABLE_REGISTER = win32more.System.Hypervisor.WHV_X64_TABLE_REGISTER_head
    WHV_X64_TABLE_REGISTER._fields_ = [
        ("Pad", UInt16 * 3),
        ("Limit", UInt16),
        ("Base", UInt64),
    ]
    return WHV_X64_TABLE_REGISTER
def _define_WHV_X64_INTERRUPT_STATE_REGISTER_head():
    class WHV_X64_INTERRUPT_STATE_REGISTER(Union):
        pass
    return WHV_X64_INTERRUPT_STATE_REGISTER
def _define_WHV_X64_INTERRUPT_STATE_REGISTER():
    WHV_X64_INTERRUPT_STATE_REGISTER = win32more.System.Hypervisor.WHV_X64_INTERRUPT_STATE_REGISTER_head
    class WHV_X64_INTERRUPT_STATE_REGISTER__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_INTERRUPT_STATE_REGISTER__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_X64_INTERRUPT_STATE_REGISTER._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_INTERRUPT_STATE_REGISTER._fields_ = [
        ("Anonymous", WHV_X64_INTERRUPT_STATE_REGISTER__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_X64_INTERRUPT_STATE_REGISTER
def _define_WHV_X64_PENDING_INTERRUPTION_REGISTER_head():
    class WHV_X64_PENDING_INTERRUPTION_REGISTER(Union):
        pass
    return WHV_X64_PENDING_INTERRUPTION_REGISTER
def _define_WHV_X64_PENDING_INTERRUPTION_REGISTER():
    WHV_X64_PENDING_INTERRUPTION_REGISTER = win32more.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_REGISTER_head
    class WHV_X64_PENDING_INTERRUPTION_REGISTER__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_PENDING_INTERRUPTION_REGISTER__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
        ("ErrorCode", UInt32),
    ]
    WHV_X64_PENDING_INTERRUPTION_REGISTER._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_PENDING_INTERRUPTION_REGISTER._fields_ = [
        ("Anonymous", WHV_X64_PENDING_INTERRUPTION_REGISTER__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_X64_PENDING_INTERRUPTION_REGISTER
def _define_WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER_head():
    class WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER(Union):
        pass
    return WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER
def _define_WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER():
    WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER = win32more.System.Hypervisor.WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER_head
    class WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER._fields_ = [
        ("Anonymous", WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER
WHV_X64_PENDING_EVENT_TYPE = Int32
WHV_X64_PENDING_EVENT_TYPE_WHvX64PendingEventException = 0
WHV_X64_PENDING_EVENT_TYPE_WHvX64PendingEventExtInt = 5
def _define_WHV_X64_PENDING_EXCEPTION_EVENT_head():
    class WHV_X64_PENDING_EXCEPTION_EVENT(Union):
        pass
    return WHV_X64_PENDING_EXCEPTION_EVENT
def _define_WHV_X64_PENDING_EXCEPTION_EVENT():
    WHV_X64_PENDING_EXCEPTION_EVENT = win32more.System.Hypervisor.WHV_X64_PENDING_EXCEPTION_EVENT_head
    class WHV_X64_PENDING_EXCEPTION_EVENT__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_PENDING_EXCEPTION_EVENT__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
        ("ErrorCode", UInt32),
        ("ExceptionParameter", UInt64),
    ]
    WHV_X64_PENDING_EXCEPTION_EVENT._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_PENDING_EXCEPTION_EVENT._fields_ = [
        ("Anonymous", WHV_X64_PENDING_EXCEPTION_EVENT__Anonymous_e__Struct),
        ("AsUINT128", win32more.System.Hypervisor.WHV_UINT128),
    ]
    return WHV_X64_PENDING_EXCEPTION_EVENT
def _define_WHV_X64_PENDING_EXT_INT_EVENT_head():
    class WHV_X64_PENDING_EXT_INT_EVENT(Union):
        pass
    return WHV_X64_PENDING_EXT_INT_EVENT
def _define_WHV_X64_PENDING_EXT_INT_EVENT():
    WHV_X64_PENDING_EXT_INT_EVENT = win32more.System.Hypervisor.WHV_X64_PENDING_EXT_INT_EVENT_head
    class WHV_X64_PENDING_EXT_INT_EVENT__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_PENDING_EXT_INT_EVENT__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
        ("Reserved2", UInt64),
    ]
    WHV_X64_PENDING_EXT_INT_EVENT._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_PENDING_EXT_INT_EVENT._fields_ = [
        ("Anonymous", WHV_X64_PENDING_EXT_INT_EVENT__Anonymous_e__Struct),
        ("AsUINT128", win32more.System.Hypervisor.WHV_UINT128),
    ]
    return WHV_X64_PENDING_EXT_INT_EVENT
def _define_WHV_INTERNAL_ACTIVITY_REGISTER_head():
    class WHV_INTERNAL_ACTIVITY_REGISTER(Union):
        pass
    return WHV_INTERNAL_ACTIVITY_REGISTER
def _define_WHV_INTERNAL_ACTIVITY_REGISTER():
    WHV_INTERNAL_ACTIVITY_REGISTER = win32more.System.Hypervisor.WHV_INTERNAL_ACTIVITY_REGISTER_head
    class WHV_INTERNAL_ACTIVITY_REGISTER__Anonymous_e__Struct(Structure):
        pass
    WHV_INTERNAL_ACTIVITY_REGISTER__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_INTERNAL_ACTIVITY_REGISTER._anonymous_ = [
        'Anonymous',
    ]
    WHV_INTERNAL_ACTIVITY_REGISTER._fields_ = [
        ("Anonymous", WHV_INTERNAL_ACTIVITY_REGISTER__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_INTERNAL_ACTIVITY_REGISTER
def _define_WHV_X64_PENDING_DEBUG_EXCEPTION_head():
    class WHV_X64_PENDING_DEBUG_EXCEPTION(Union):
        pass
    return WHV_X64_PENDING_DEBUG_EXCEPTION
def _define_WHV_X64_PENDING_DEBUG_EXCEPTION():
    WHV_X64_PENDING_DEBUG_EXCEPTION = win32more.System.Hypervisor.WHV_X64_PENDING_DEBUG_EXCEPTION_head
    class WHV_X64_PENDING_DEBUG_EXCEPTION__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_PENDING_DEBUG_EXCEPTION__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_X64_PENDING_DEBUG_EXCEPTION._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_PENDING_DEBUG_EXCEPTION._fields_ = [
        ("AsUINT64", UInt64),
        ("Anonymous", WHV_X64_PENDING_DEBUG_EXCEPTION__Anonymous_e__Struct),
    ]
    return WHV_X64_PENDING_DEBUG_EXCEPTION
def _define_WHV_SYNIC_SINT_DELIVERABLE_CONTEXT_head():
    class WHV_SYNIC_SINT_DELIVERABLE_CONTEXT(Structure):
        pass
    return WHV_SYNIC_SINT_DELIVERABLE_CONTEXT
def _define_WHV_SYNIC_SINT_DELIVERABLE_CONTEXT():
    WHV_SYNIC_SINT_DELIVERABLE_CONTEXT = win32more.System.Hypervisor.WHV_SYNIC_SINT_DELIVERABLE_CONTEXT_head
    WHV_SYNIC_SINT_DELIVERABLE_CONTEXT._fields_ = [
        ("DeliverableSints", UInt16),
        ("Reserved1", UInt16),
        ("Reserved2", UInt32),
    ]
    return WHV_SYNIC_SINT_DELIVERABLE_CONTEXT
def _define_WHV_REGISTER_VALUE_head():
    class WHV_REGISTER_VALUE(Union):
        pass
    return WHV_REGISTER_VALUE
def _define_WHV_REGISTER_VALUE():
    WHV_REGISTER_VALUE = win32more.System.Hypervisor.WHV_REGISTER_VALUE_head
    WHV_REGISTER_VALUE._fields_ = [
        ("Reg128", win32more.System.Hypervisor.WHV_UINT128),
        ("Reg64", UInt64),
        ("Reg32", UInt32),
        ("Reg16", UInt16),
        ("Reg8", Byte),
        ("Fp", win32more.System.Hypervisor.WHV_X64_FP_REGISTER),
        ("FpControlStatus", win32more.System.Hypervisor.WHV_X64_FP_CONTROL_STATUS_REGISTER),
        ("XmmControlStatus", win32more.System.Hypervisor.WHV_X64_XMM_CONTROL_STATUS_REGISTER),
        ("Segment", win32more.System.Hypervisor.WHV_X64_SEGMENT_REGISTER),
        ("Table", win32more.System.Hypervisor.WHV_X64_TABLE_REGISTER),
        ("InterruptState", win32more.System.Hypervisor.WHV_X64_INTERRUPT_STATE_REGISTER),
        ("PendingInterruption", win32more.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_REGISTER),
        ("DeliverabilityNotifications", win32more.System.Hypervisor.WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER),
        ("ExceptionEvent", win32more.System.Hypervisor.WHV_X64_PENDING_EXCEPTION_EVENT),
        ("ExtIntEvent", win32more.System.Hypervisor.WHV_X64_PENDING_EXT_INT_EVENT),
        ("InternalActivity", win32more.System.Hypervisor.WHV_INTERNAL_ACTIVITY_REGISTER),
        ("PendingDebugException", win32more.System.Hypervisor.WHV_X64_PENDING_DEBUG_EXCEPTION),
    ]
    return WHV_REGISTER_VALUE
WHV_RUN_VP_EXIT_REASON = Int32
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonNone = 0
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonMemoryAccess = 1
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64IoPortAccess = 2
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonUnrecoverableException = 4
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonInvalidVpRegisterValue = 5
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonUnsupportedFeature = 6
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64InterruptWindow = 7
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Halt = 8
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicEoi = 9
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonSynicSintDeliverable = 10
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64MsrAccess = 4096
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Cpuid = 4097
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonException = 4098
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Rdtsc = 4099
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicSmiTrap = 4100
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonHypercall = 4101
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicInitSipiTrap = 4102
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicWriteTrap = 4103
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonCanceled = 8193
def _define_WHV_X64_VP_EXECUTION_STATE_head():
    class WHV_X64_VP_EXECUTION_STATE(Union):
        pass
    return WHV_X64_VP_EXECUTION_STATE
def _define_WHV_X64_VP_EXECUTION_STATE():
    WHV_X64_VP_EXECUTION_STATE = win32more.System.Hypervisor.WHV_X64_VP_EXECUTION_STATE_head
    class WHV_X64_VP_EXECUTION_STATE__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_VP_EXECUTION_STATE__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt16),
    ]
    WHV_X64_VP_EXECUTION_STATE._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_VP_EXECUTION_STATE._fields_ = [
        ("Anonymous", WHV_X64_VP_EXECUTION_STATE__Anonymous_e__Struct),
        ("AsUINT16", UInt16),
    ]
    return WHV_X64_VP_EXECUTION_STATE
def _define_WHV_VP_EXIT_CONTEXT_head():
    class WHV_VP_EXIT_CONTEXT(Structure):
        pass
    return WHV_VP_EXIT_CONTEXT
def _define_WHV_VP_EXIT_CONTEXT():
    WHV_VP_EXIT_CONTEXT = win32more.System.Hypervisor.WHV_VP_EXIT_CONTEXT_head
    WHV_VP_EXIT_CONTEXT._fields_ = [
        ("ExecutionState", win32more.System.Hypervisor.WHV_X64_VP_EXECUTION_STATE),
        ("_bitfield", Byte),
        ("Reserved", Byte),
        ("Reserved2", UInt32),
        ("Cs", win32more.System.Hypervisor.WHV_X64_SEGMENT_REGISTER),
        ("Rip", UInt64),
        ("Rflags", UInt64),
    ]
    return WHV_VP_EXIT_CONTEXT
def _define_WHV_MEMORY_ACCESS_INFO_head():
    class WHV_MEMORY_ACCESS_INFO(Union):
        pass
    return WHV_MEMORY_ACCESS_INFO
def _define_WHV_MEMORY_ACCESS_INFO():
    WHV_MEMORY_ACCESS_INFO = win32more.System.Hypervisor.WHV_MEMORY_ACCESS_INFO_head
    class WHV_MEMORY_ACCESS_INFO__Anonymous_e__Struct(Structure):
        pass
    WHV_MEMORY_ACCESS_INFO__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    WHV_MEMORY_ACCESS_INFO._anonymous_ = [
        'Anonymous',
    ]
    WHV_MEMORY_ACCESS_INFO._fields_ = [
        ("Anonymous", WHV_MEMORY_ACCESS_INFO__Anonymous_e__Struct),
        ("AsUINT32", UInt32),
    ]
    return WHV_MEMORY_ACCESS_INFO
def _define_WHV_MEMORY_ACCESS_CONTEXT_head():
    class WHV_MEMORY_ACCESS_CONTEXT(Structure):
        pass
    return WHV_MEMORY_ACCESS_CONTEXT
def _define_WHV_MEMORY_ACCESS_CONTEXT():
    WHV_MEMORY_ACCESS_CONTEXT = win32more.System.Hypervisor.WHV_MEMORY_ACCESS_CONTEXT_head
    WHV_MEMORY_ACCESS_CONTEXT._fields_ = [
        ("InstructionByteCount", Byte),
        ("Reserved", Byte * 3),
        ("InstructionBytes", Byte * 16),
        ("AccessInfo", win32more.System.Hypervisor.WHV_MEMORY_ACCESS_INFO),
        ("Gpa", UInt64),
        ("Gva", UInt64),
    ]
    return WHV_MEMORY_ACCESS_CONTEXT
def _define_WHV_X64_IO_PORT_ACCESS_INFO_head():
    class WHV_X64_IO_PORT_ACCESS_INFO(Union):
        pass
    return WHV_X64_IO_PORT_ACCESS_INFO
def _define_WHV_X64_IO_PORT_ACCESS_INFO():
    WHV_X64_IO_PORT_ACCESS_INFO = win32more.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_INFO_head
    class WHV_X64_IO_PORT_ACCESS_INFO__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_IO_PORT_ACCESS_INFO__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    WHV_X64_IO_PORT_ACCESS_INFO._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_IO_PORT_ACCESS_INFO._fields_ = [
        ("Anonymous", WHV_X64_IO_PORT_ACCESS_INFO__Anonymous_e__Struct),
        ("AsUINT32", UInt32),
    ]
    return WHV_X64_IO_PORT_ACCESS_INFO
def _define_WHV_X64_IO_PORT_ACCESS_CONTEXT_head():
    class WHV_X64_IO_PORT_ACCESS_CONTEXT(Structure):
        pass
    return WHV_X64_IO_PORT_ACCESS_CONTEXT
def _define_WHV_X64_IO_PORT_ACCESS_CONTEXT():
    WHV_X64_IO_PORT_ACCESS_CONTEXT = win32more.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_CONTEXT_head
    WHV_X64_IO_PORT_ACCESS_CONTEXT._fields_ = [
        ("InstructionByteCount", Byte),
        ("Reserved", Byte * 3),
        ("InstructionBytes", Byte * 16),
        ("AccessInfo", win32more.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_INFO),
        ("PortNumber", UInt16),
        ("Reserved2", UInt16 * 3),
        ("Rax", UInt64),
        ("Rcx", UInt64),
        ("Rsi", UInt64),
        ("Rdi", UInt64),
        ("Ds", win32more.System.Hypervisor.WHV_X64_SEGMENT_REGISTER),
        ("Es", win32more.System.Hypervisor.WHV_X64_SEGMENT_REGISTER),
    ]
    return WHV_X64_IO_PORT_ACCESS_CONTEXT
def _define_WHV_X64_MSR_ACCESS_INFO_head():
    class WHV_X64_MSR_ACCESS_INFO(Union):
        pass
    return WHV_X64_MSR_ACCESS_INFO
def _define_WHV_X64_MSR_ACCESS_INFO():
    WHV_X64_MSR_ACCESS_INFO = win32more.System.Hypervisor.WHV_X64_MSR_ACCESS_INFO_head
    class WHV_X64_MSR_ACCESS_INFO__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_MSR_ACCESS_INFO__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    WHV_X64_MSR_ACCESS_INFO._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_MSR_ACCESS_INFO._fields_ = [
        ("Anonymous", WHV_X64_MSR_ACCESS_INFO__Anonymous_e__Struct),
        ("AsUINT32", UInt32),
    ]
    return WHV_X64_MSR_ACCESS_INFO
def _define_WHV_X64_MSR_ACCESS_CONTEXT_head():
    class WHV_X64_MSR_ACCESS_CONTEXT(Structure):
        pass
    return WHV_X64_MSR_ACCESS_CONTEXT
def _define_WHV_X64_MSR_ACCESS_CONTEXT():
    WHV_X64_MSR_ACCESS_CONTEXT = win32more.System.Hypervisor.WHV_X64_MSR_ACCESS_CONTEXT_head
    WHV_X64_MSR_ACCESS_CONTEXT._fields_ = [
        ("AccessInfo", win32more.System.Hypervisor.WHV_X64_MSR_ACCESS_INFO),
        ("MsrNumber", UInt32),
        ("Rax", UInt64),
        ("Rdx", UInt64),
    ]
    return WHV_X64_MSR_ACCESS_CONTEXT
def _define_WHV_X64_CPUID_ACCESS_CONTEXT_head():
    class WHV_X64_CPUID_ACCESS_CONTEXT(Structure):
        pass
    return WHV_X64_CPUID_ACCESS_CONTEXT
def _define_WHV_X64_CPUID_ACCESS_CONTEXT():
    WHV_X64_CPUID_ACCESS_CONTEXT = win32more.System.Hypervisor.WHV_X64_CPUID_ACCESS_CONTEXT_head
    WHV_X64_CPUID_ACCESS_CONTEXT._fields_ = [
        ("Rax", UInt64),
        ("Rcx", UInt64),
        ("Rdx", UInt64),
        ("Rbx", UInt64),
        ("DefaultResultRax", UInt64),
        ("DefaultResultRcx", UInt64),
        ("DefaultResultRdx", UInt64),
        ("DefaultResultRbx", UInt64),
    ]
    return WHV_X64_CPUID_ACCESS_CONTEXT
def _define_WHV_VP_EXCEPTION_INFO_head():
    class WHV_VP_EXCEPTION_INFO(Union):
        pass
    return WHV_VP_EXCEPTION_INFO
def _define_WHV_VP_EXCEPTION_INFO():
    WHV_VP_EXCEPTION_INFO = win32more.System.Hypervisor.WHV_VP_EXCEPTION_INFO_head
    class WHV_VP_EXCEPTION_INFO__Anonymous_e__Struct(Structure):
        pass
    WHV_VP_EXCEPTION_INFO__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    WHV_VP_EXCEPTION_INFO._anonymous_ = [
        'Anonymous',
    ]
    WHV_VP_EXCEPTION_INFO._fields_ = [
        ("Anonymous", WHV_VP_EXCEPTION_INFO__Anonymous_e__Struct),
        ("AsUINT32", UInt32),
    ]
    return WHV_VP_EXCEPTION_INFO
def _define_WHV_VP_EXCEPTION_CONTEXT_head():
    class WHV_VP_EXCEPTION_CONTEXT(Structure):
        pass
    return WHV_VP_EXCEPTION_CONTEXT
def _define_WHV_VP_EXCEPTION_CONTEXT():
    WHV_VP_EXCEPTION_CONTEXT = win32more.System.Hypervisor.WHV_VP_EXCEPTION_CONTEXT_head
    WHV_VP_EXCEPTION_CONTEXT._fields_ = [
        ("InstructionByteCount", Byte),
        ("Reserved", Byte * 3),
        ("InstructionBytes", Byte * 16),
        ("ExceptionInfo", win32more.System.Hypervisor.WHV_VP_EXCEPTION_INFO),
        ("ExceptionType", Byte),
        ("Reserved2", Byte * 3),
        ("ErrorCode", UInt32),
        ("ExceptionParameter", UInt64),
    ]
    return WHV_VP_EXCEPTION_CONTEXT
WHV_X64_UNSUPPORTED_FEATURE_CODE = Int32
WHV_X64_UNSUPPORTED_FEATURE_CODE_WHvUnsupportedFeatureIntercept = 1
WHV_X64_UNSUPPORTED_FEATURE_CODE_WHvUnsupportedFeatureTaskSwitchTss = 2
def _define_WHV_X64_UNSUPPORTED_FEATURE_CONTEXT_head():
    class WHV_X64_UNSUPPORTED_FEATURE_CONTEXT(Structure):
        pass
    return WHV_X64_UNSUPPORTED_FEATURE_CONTEXT
def _define_WHV_X64_UNSUPPORTED_FEATURE_CONTEXT():
    WHV_X64_UNSUPPORTED_FEATURE_CONTEXT = win32more.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CONTEXT_head
    WHV_X64_UNSUPPORTED_FEATURE_CONTEXT._fields_ = [
        ("FeatureCode", win32more.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CODE),
        ("Reserved", UInt32),
        ("FeatureParameter", UInt64),
    ]
    return WHV_X64_UNSUPPORTED_FEATURE_CONTEXT
WHV_RUN_VP_CANCEL_REASON = Int32
WHV_RUN_VP_CANCEL_REASON_WHvRunVpCancelReasonUser = 0
def _define_WHV_RUN_VP_CANCELED_CONTEXT_head():
    class WHV_RUN_VP_CANCELED_CONTEXT(Structure):
        pass
    return WHV_RUN_VP_CANCELED_CONTEXT
def _define_WHV_RUN_VP_CANCELED_CONTEXT():
    WHV_RUN_VP_CANCELED_CONTEXT = win32more.System.Hypervisor.WHV_RUN_VP_CANCELED_CONTEXT_head
    WHV_RUN_VP_CANCELED_CONTEXT._fields_ = [
        ("CancelReason", win32more.System.Hypervisor.WHV_RUN_VP_CANCEL_REASON),
    ]
    return WHV_RUN_VP_CANCELED_CONTEXT
WHV_X64_PENDING_INTERRUPTION_TYPE = Int32
WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingInterrupt = 0
WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingNmi = 2
WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingException = 3
def _define_WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT_head():
    class WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT(Structure):
        pass
    return WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT
def _define_WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT():
    WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT = win32more.System.Hypervisor.WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT_head
    WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT._fields_ = [
        ("DeliverableType", win32more.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_TYPE),
    ]
    return WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT
def _define_WHV_X64_APIC_EOI_CONTEXT_head():
    class WHV_X64_APIC_EOI_CONTEXT(Structure):
        pass
    return WHV_X64_APIC_EOI_CONTEXT
def _define_WHV_X64_APIC_EOI_CONTEXT():
    WHV_X64_APIC_EOI_CONTEXT = win32more.System.Hypervisor.WHV_X64_APIC_EOI_CONTEXT_head
    WHV_X64_APIC_EOI_CONTEXT._fields_ = [
        ("InterruptVector", UInt32),
    ]
    return WHV_X64_APIC_EOI_CONTEXT
def _define_WHV_X64_RDTSC_INFO_head():
    class WHV_X64_RDTSC_INFO(Union):
        pass
    return WHV_X64_RDTSC_INFO
def _define_WHV_X64_RDTSC_INFO():
    WHV_X64_RDTSC_INFO = win32more.System.Hypervisor.WHV_X64_RDTSC_INFO_head
    class WHV_X64_RDTSC_INFO__Anonymous_e__Struct(Structure):
        pass
    WHV_X64_RDTSC_INFO__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    WHV_X64_RDTSC_INFO._anonymous_ = [
        'Anonymous',
    ]
    WHV_X64_RDTSC_INFO._fields_ = [
        ("Anonymous", WHV_X64_RDTSC_INFO__Anonymous_e__Struct),
        ("AsUINT64", UInt64),
    ]
    return WHV_X64_RDTSC_INFO
def _define_WHV_X64_RDTSC_CONTEXT_head():
    class WHV_X64_RDTSC_CONTEXT(Structure):
        pass
    return WHV_X64_RDTSC_CONTEXT
def _define_WHV_X64_RDTSC_CONTEXT():
    WHV_X64_RDTSC_CONTEXT = win32more.System.Hypervisor.WHV_X64_RDTSC_CONTEXT_head
    WHV_X64_RDTSC_CONTEXT._fields_ = [
        ("TscAux", UInt64),
        ("VirtualOffset", UInt64),
        ("Tsc", UInt64),
        ("ReferenceTime", UInt64),
        ("RdtscInfo", win32more.System.Hypervisor.WHV_X64_RDTSC_INFO),
    ]
    return WHV_X64_RDTSC_CONTEXT
def _define_WHV_X64_APIC_SMI_CONTEXT_head():
    class WHV_X64_APIC_SMI_CONTEXT(Structure):
        pass
    return WHV_X64_APIC_SMI_CONTEXT
def _define_WHV_X64_APIC_SMI_CONTEXT():
    WHV_X64_APIC_SMI_CONTEXT = win32more.System.Hypervisor.WHV_X64_APIC_SMI_CONTEXT_head
    WHV_X64_APIC_SMI_CONTEXT._fields_ = [
        ("ApicIcr", UInt64),
    ]
    return WHV_X64_APIC_SMI_CONTEXT
def _define_WHV_HYPERCALL_CONTEXT_head():
    class WHV_HYPERCALL_CONTEXT(Structure):
        pass
    return WHV_HYPERCALL_CONTEXT
def _define_WHV_HYPERCALL_CONTEXT():
    WHV_HYPERCALL_CONTEXT = win32more.System.Hypervisor.WHV_HYPERCALL_CONTEXT_head
    WHV_HYPERCALL_CONTEXT._fields_ = [
        ("Rax", UInt64),
        ("Rbx", UInt64),
        ("Rcx", UInt64),
        ("Rdx", UInt64),
        ("R8", UInt64),
        ("Rsi", UInt64),
        ("Rdi", UInt64),
        ("Reserved0", UInt64),
        ("XmmRegisters", win32more.System.Hypervisor.WHV_UINT128 * 6),
        ("Reserved1", UInt64 * 2),
    ]
    return WHV_HYPERCALL_CONTEXT
def _define_WHV_X64_APIC_INIT_SIPI_CONTEXT_head():
    class WHV_X64_APIC_INIT_SIPI_CONTEXT(Structure):
        pass
    return WHV_X64_APIC_INIT_SIPI_CONTEXT
def _define_WHV_X64_APIC_INIT_SIPI_CONTEXT():
    WHV_X64_APIC_INIT_SIPI_CONTEXT = win32more.System.Hypervisor.WHV_X64_APIC_INIT_SIPI_CONTEXT_head
    WHV_X64_APIC_INIT_SIPI_CONTEXT._fields_ = [
        ("ApicIcr", UInt64),
    ]
    return WHV_X64_APIC_INIT_SIPI_CONTEXT
WHV_X64_APIC_WRITE_TYPE = Int32
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLdr = 208
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeDfr = 224
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeSvr = 240
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLint0 = 848
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLint1 = 864
def _define_WHV_X64_APIC_WRITE_CONTEXT_head():
    class WHV_X64_APIC_WRITE_CONTEXT(Structure):
        pass
    return WHV_X64_APIC_WRITE_CONTEXT
def _define_WHV_X64_APIC_WRITE_CONTEXT():
    WHV_X64_APIC_WRITE_CONTEXT = win32more.System.Hypervisor.WHV_X64_APIC_WRITE_CONTEXT_head
    WHV_X64_APIC_WRITE_CONTEXT._fields_ = [
        ("Type", win32more.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE),
        ("Reserved", UInt32),
        ("WriteValue", UInt64),
    ]
    return WHV_X64_APIC_WRITE_CONTEXT
def _define_WHV_RUN_VP_EXIT_CONTEXT_head():
    class WHV_RUN_VP_EXIT_CONTEXT(Structure):
        pass
    return WHV_RUN_VP_EXIT_CONTEXT
def _define_WHV_RUN_VP_EXIT_CONTEXT():
    WHV_RUN_VP_EXIT_CONTEXT = win32more.System.Hypervisor.WHV_RUN_VP_EXIT_CONTEXT_head
    class WHV_RUN_VP_EXIT_CONTEXT__Anonymous_e__Union(Union):
        pass
    WHV_RUN_VP_EXIT_CONTEXT__Anonymous_e__Union._fields_ = [
        ("MemoryAccess", win32more.System.Hypervisor.WHV_MEMORY_ACCESS_CONTEXT),
        ("IoPortAccess", win32more.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_CONTEXT),
        ("MsrAccess", win32more.System.Hypervisor.WHV_X64_MSR_ACCESS_CONTEXT),
        ("CpuidAccess", win32more.System.Hypervisor.WHV_X64_CPUID_ACCESS_CONTEXT),
        ("VpException", win32more.System.Hypervisor.WHV_VP_EXCEPTION_CONTEXT),
        ("InterruptWindow", win32more.System.Hypervisor.WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT),
        ("UnsupportedFeature", win32more.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CONTEXT),
        ("CancelReason", win32more.System.Hypervisor.WHV_RUN_VP_CANCELED_CONTEXT),
        ("ApicEoi", win32more.System.Hypervisor.WHV_X64_APIC_EOI_CONTEXT),
        ("ReadTsc", win32more.System.Hypervisor.WHV_X64_RDTSC_CONTEXT),
        ("ApicSmi", win32more.System.Hypervisor.WHV_X64_APIC_SMI_CONTEXT),
        ("Hypercall", win32more.System.Hypervisor.WHV_HYPERCALL_CONTEXT),
        ("ApicInitSipi", win32more.System.Hypervisor.WHV_X64_APIC_INIT_SIPI_CONTEXT),
        ("ApicWrite", win32more.System.Hypervisor.WHV_X64_APIC_WRITE_CONTEXT),
        ("SynicSintDeliverable", win32more.System.Hypervisor.WHV_SYNIC_SINT_DELIVERABLE_CONTEXT),
    ]
    WHV_RUN_VP_EXIT_CONTEXT._anonymous_ = [
        'Anonymous',
    ]
    WHV_RUN_VP_EXIT_CONTEXT._fields_ = [
        ("ExitReason", win32more.System.Hypervisor.WHV_RUN_VP_EXIT_REASON),
        ("Reserved", UInt32),
        ("VpContext", win32more.System.Hypervisor.WHV_VP_EXIT_CONTEXT),
        ("Anonymous", WHV_RUN_VP_EXIT_CONTEXT__Anonymous_e__Union),
    ]
    return WHV_RUN_VP_EXIT_CONTEXT
WHV_INTERRUPT_TYPE = Int32
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeFixed = 0
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeLowestPriority = 1
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeNmi = 4
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeInit = 5
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeSipi = 6
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeLocalInt1 = 9
WHV_INTERRUPT_DESTINATION_MODE = Int32
WHV_INTERRUPT_DESTINATION_MODE_WHvX64InterruptDestinationModePhysical = 0
WHV_INTERRUPT_DESTINATION_MODE_WHvX64InterruptDestinationModeLogical = 1
WHV_INTERRUPT_TRIGGER_MODE = Int32
WHV_INTERRUPT_TRIGGER_MODE_WHvX64InterruptTriggerModeEdge = 0
WHV_INTERRUPT_TRIGGER_MODE_WHvX64InterruptTriggerModeLevel = 1
def _define_WHV_INTERRUPT_CONTROL_head():
    class WHV_INTERRUPT_CONTROL(Structure):
        pass
    return WHV_INTERRUPT_CONTROL
def _define_WHV_INTERRUPT_CONTROL():
    WHV_INTERRUPT_CONTROL = win32more.System.Hypervisor.WHV_INTERRUPT_CONTROL_head
    WHV_INTERRUPT_CONTROL._fields_ = [
        ("_bitfield", UInt64),
        ("Destination", UInt32),
        ("Vector", UInt32),
    ]
    return WHV_INTERRUPT_CONTROL
def _define_WHV_DOORBELL_MATCH_DATA_head():
    class WHV_DOORBELL_MATCH_DATA(Structure):
        pass
    return WHV_DOORBELL_MATCH_DATA
def _define_WHV_DOORBELL_MATCH_DATA():
    WHV_DOORBELL_MATCH_DATA = win32more.System.Hypervisor.WHV_DOORBELL_MATCH_DATA_head
    WHV_DOORBELL_MATCH_DATA._fields_ = [
        ("GuestAddress", UInt64),
        ("Value", UInt64),
        ("Length", UInt32),
        ("_bitfield", UInt32),
    ]
    return WHV_DOORBELL_MATCH_DATA
WHV_PARTITION_COUNTER_SET = Int32
WHV_PARTITION_COUNTER_SET_WHvPartitionCounterSetMemory = 0
def _define_WHV_PARTITION_MEMORY_COUNTERS_head():
    class WHV_PARTITION_MEMORY_COUNTERS(Structure):
        pass
    return WHV_PARTITION_MEMORY_COUNTERS
def _define_WHV_PARTITION_MEMORY_COUNTERS():
    WHV_PARTITION_MEMORY_COUNTERS = win32more.System.Hypervisor.WHV_PARTITION_MEMORY_COUNTERS_head
    WHV_PARTITION_MEMORY_COUNTERS._fields_ = [
        ("Mapped4KPageCount", UInt64),
        ("Mapped2MPageCount", UInt64),
        ("Mapped1GPageCount", UInt64),
    ]
    return WHV_PARTITION_MEMORY_COUNTERS
WHV_PROCESSOR_COUNTER_SET = Int32
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetRuntime = 0
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetIntercepts = 1
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetEvents = 2
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetApic = 3
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetSyntheticFeatures = 4
def _define_WHV_PROCESSOR_RUNTIME_COUNTERS_head():
    class WHV_PROCESSOR_RUNTIME_COUNTERS(Structure):
        pass
    return WHV_PROCESSOR_RUNTIME_COUNTERS
def _define_WHV_PROCESSOR_RUNTIME_COUNTERS():
    WHV_PROCESSOR_RUNTIME_COUNTERS = win32more.System.Hypervisor.WHV_PROCESSOR_RUNTIME_COUNTERS_head
    WHV_PROCESSOR_RUNTIME_COUNTERS._fields_ = [
        ("TotalRuntime100ns", UInt64),
        ("HypervisorRuntime100ns", UInt64),
    ]
    return WHV_PROCESSOR_RUNTIME_COUNTERS
def _define_WHV_PROCESSOR_INTERCEPT_COUNTER_head():
    class WHV_PROCESSOR_INTERCEPT_COUNTER(Structure):
        pass
    return WHV_PROCESSOR_INTERCEPT_COUNTER
def _define_WHV_PROCESSOR_INTERCEPT_COUNTER():
    WHV_PROCESSOR_INTERCEPT_COUNTER = win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER_head
    WHV_PROCESSOR_INTERCEPT_COUNTER._fields_ = [
        ("Count", UInt64),
        ("Time100ns", UInt64),
    ]
    return WHV_PROCESSOR_INTERCEPT_COUNTER
def _define_WHV_PROCESSOR_INTERCEPT_COUNTERS_head():
    class WHV_PROCESSOR_INTERCEPT_COUNTERS(Structure):
        pass
    return WHV_PROCESSOR_INTERCEPT_COUNTERS
def _define_WHV_PROCESSOR_INTERCEPT_COUNTERS():
    WHV_PROCESSOR_INTERCEPT_COUNTERS = win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTERS_head
    WHV_PROCESSOR_INTERCEPT_COUNTERS._fields_ = [
        ("PageInvalidations", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("ControlRegisterAccesses", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("IoInstructions", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("HaltInstructions", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("CpuidInstructions", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("MsrAccesses", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("OtherIntercepts", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("PendingInterrupts", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("EmulatedInstructions", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("DebugRegisterAccesses", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("PageFaultIntercepts", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("NestedPageFaultIntercepts", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("Hypercalls", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
        ("RdpmcInstructions", win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER),
    ]
    return WHV_PROCESSOR_INTERCEPT_COUNTERS
def _define_WHV_PROCESSOR_EVENT_COUNTERS_head():
    class WHV_PROCESSOR_EVENT_COUNTERS(Structure):
        pass
    return WHV_PROCESSOR_EVENT_COUNTERS
def _define_WHV_PROCESSOR_EVENT_COUNTERS():
    WHV_PROCESSOR_EVENT_COUNTERS = win32more.System.Hypervisor.WHV_PROCESSOR_EVENT_COUNTERS_head
    WHV_PROCESSOR_EVENT_COUNTERS._fields_ = [
        ("PageFaultCount", UInt64),
        ("ExceptionCount", UInt64),
        ("InterruptCount", UInt64),
    ]
    return WHV_PROCESSOR_EVENT_COUNTERS
def _define_WHV_PROCESSOR_APIC_COUNTERS_head():
    class WHV_PROCESSOR_APIC_COUNTERS(Structure):
        pass
    return WHV_PROCESSOR_APIC_COUNTERS
def _define_WHV_PROCESSOR_APIC_COUNTERS():
    WHV_PROCESSOR_APIC_COUNTERS = win32more.System.Hypervisor.WHV_PROCESSOR_APIC_COUNTERS_head
    WHV_PROCESSOR_APIC_COUNTERS._fields_ = [
        ("MmioAccessCount", UInt64),
        ("EoiAccessCount", UInt64),
        ("TprAccessCount", UInt64),
        ("SentIpiCount", UInt64),
        ("SelfIpiCount", UInt64),
    ]
    return WHV_PROCESSOR_APIC_COUNTERS
def _define_WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS_head():
    class WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS(Structure):
        pass
    return WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS
def _define_WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS():
    WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS = win32more.System.Hypervisor.WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS_head
    WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS._fields_ = [
        ("SyntheticInterruptsCount", UInt64),
        ("LongSpinWaitHypercallsCount", UInt64),
        ("OtherHypercallsCount", UInt64),
        ("SyntheticInterruptHypercallsCount", UInt64),
        ("VirtualInterruptHypercallsCount", UInt64),
        ("VirtualMmuHypercallsCount", UInt64),
    ]
    return WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS
WHV_ADVISE_GPA_RANGE_CODE = Int32
WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodePopulate = 0
WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodePin = 1
WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodeUnpin = 2
WHV_VIRTUAL_PROCESSOR_STATE_TYPE = Int32
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicMessagePage = 0
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicEventFlagPage = 1
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicTimerState = 2
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeInterruptControllerState2 = 4096
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeXsaveState = 4097
def _define_WHV_SYNIC_EVENT_PARAMETERS_head():
    class WHV_SYNIC_EVENT_PARAMETERS(Structure):
        pass
    return WHV_SYNIC_EVENT_PARAMETERS
def _define_WHV_SYNIC_EVENT_PARAMETERS():
    WHV_SYNIC_EVENT_PARAMETERS = win32more.System.Hypervisor.WHV_SYNIC_EVENT_PARAMETERS_head
    WHV_SYNIC_EVENT_PARAMETERS._fields_ = [
        ("VpIndex", UInt32),
        ("TargetSint", Byte),
        ("Reserved", Byte),
        ("FlagNumber", UInt16),
    ]
    return WHV_SYNIC_EVENT_PARAMETERS
WHV_ALLOCATE_VPCI_RESOURCE_FLAGS = UInt32
WHV_ALLOCATE_VPCI_RESOURCE_FLAGS_WHvAllocateVpciResourceFlagNone = 0
WHV_ALLOCATE_VPCI_RESOURCE_FLAGS_WHvAllocateVpciResourceFlagAllowDirectP2P = 1
def _define_WHV_SRIOV_RESOURCE_DESCRIPTOR_head():
    class WHV_SRIOV_RESOURCE_DESCRIPTOR(Structure):
        pass
    return WHV_SRIOV_RESOURCE_DESCRIPTOR
def _define_WHV_SRIOV_RESOURCE_DESCRIPTOR():
    WHV_SRIOV_RESOURCE_DESCRIPTOR = win32more.System.Hypervisor.WHV_SRIOV_RESOURCE_DESCRIPTOR_head
    WHV_SRIOV_RESOURCE_DESCRIPTOR._fields_ = [
        ("PnpInstanceId", Char * 200),
        ("VirtualFunctionId", win32more.Foundation.LUID),
        ("VirtualFunctionIndex", UInt16),
        ("Reserved", UInt16),
    ]
    return WHV_SRIOV_RESOURCE_DESCRIPTOR
WHV_VPCI_DEVICE_NOTIFICATION_TYPE = Int32
WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationUndefined = 0
WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationMmioRemapping = 1
WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationSurpriseRemoval = 2
def _define_WHV_VPCI_DEVICE_NOTIFICATION_head():
    class WHV_VPCI_DEVICE_NOTIFICATION(Structure):
        pass
    return WHV_VPCI_DEVICE_NOTIFICATION
def _define_WHV_VPCI_DEVICE_NOTIFICATION():
    WHV_VPCI_DEVICE_NOTIFICATION = win32more.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_head
    class WHV_VPCI_DEVICE_NOTIFICATION__Anonymous_e__Union(Union):
        pass
    WHV_VPCI_DEVICE_NOTIFICATION__Anonymous_e__Union._fields_ = [
        ("Reserved2", UInt64),
    ]
    WHV_VPCI_DEVICE_NOTIFICATION._anonymous_ = [
        'Anonymous',
    ]
    WHV_VPCI_DEVICE_NOTIFICATION._fields_ = [
        ("NotificationType", win32more.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_TYPE),
        ("Reserved1", UInt32),
        ("Anonymous", WHV_VPCI_DEVICE_NOTIFICATION__Anonymous_e__Union),
    ]
    return WHV_VPCI_DEVICE_NOTIFICATION
WHV_CREATE_VPCI_DEVICE_FLAGS = UInt32
WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagNone = 0
WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagPhysicallyBacked = 1
WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagUseLogicalInterrupts = 2
WHV_VPCI_DEVICE_PROPERTY_CODE = Int32
WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeUndefined = 0
WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeHardwareIDs = 1
WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeProbedBARs = 2
def _define_WHV_VPCI_HARDWARE_IDS_head():
    class WHV_VPCI_HARDWARE_IDS(Structure):
        pass
    return WHV_VPCI_HARDWARE_IDS
def _define_WHV_VPCI_HARDWARE_IDS():
    WHV_VPCI_HARDWARE_IDS = win32more.System.Hypervisor.WHV_VPCI_HARDWARE_IDS_head
    WHV_VPCI_HARDWARE_IDS._fields_ = [
        ("VendorID", UInt16),
        ("DeviceID", UInt16),
        ("RevisionID", Byte),
        ("ProgIf", Byte),
        ("SubClass", Byte),
        ("BaseClass", Byte),
        ("SubVendorID", UInt16),
        ("SubSystemID", UInt16),
    ]
    return WHV_VPCI_HARDWARE_IDS
def _define_WHV_VPCI_PROBED_BARS_head():
    class WHV_VPCI_PROBED_BARS(Structure):
        pass
    return WHV_VPCI_PROBED_BARS
def _define_WHV_VPCI_PROBED_BARS():
    WHV_VPCI_PROBED_BARS = win32more.System.Hypervisor.WHV_VPCI_PROBED_BARS_head
    WHV_VPCI_PROBED_BARS._fields_ = [
        ("Value", UInt32 * 6),
    ]
    return WHV_VPCI_PROBED_BARS
WHV_VPCI_MMIO_RANGE_FLAGS = UInt32
WHV_VPCI_MMIO_RANGE_FLAGS_WHvVpciMmioRangeFlagReadAccess = 1
WHV_VPCI_MMIO_RANGE_FLAGS_WHvVpciMmioRangeFlagWriteAccess = 2
WHV_VPCI_DEVICE_REGISTER_SPACE = Int32
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciConfigSpace = -1
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar0 = 0
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar1 = 1
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar2 = 2
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar3 = 3
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar4 = 4
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar5 = 5
def _define_WHV_VPCI_MMIO_MAPPING_head():
    class WHV_VPCI_MMIO_MAPPING(Structure):
        pass
    return WHV_VPCI_MMIO_MAPPING
def _define_WHV_VPCI_MMIO_MAPPING():
    WHV_VPCI_MMIO_MAPPING = win32more.System.Hypervisor.WHV_VPCI_MMIO_MAPPING_head
    WHV_VPCI_MMIO_MAPPING._fields_ = [
        ("Location", win32more.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE),
        ("Flags", win32more.System.Hypervisor.WHV_VPCI_MMIO_RANGE_FLAGS),
        ("SizeInBytes", UInt64),
        ("OffsetInBytes", UInt64),
        ("VirtualAddress", c_void_p),
    ]
    return WHV_VPCI_MMIO_MAPPING
def _define_WHV_VPCI_DEVICE_REGISTER_head():
    class WHV_VPCI_DEVICE_REGISTER(Structure):
        pass
    return WHV_VPCI_DEVICE_REGISTER
def _define_WHV_VPCI_DEVICE_REGISTER():
    WHV_VPCI_DEVICE_REGISTER = win32more.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_head
    WHV_VPCI_DEVICE_REGISTER._fields_ = [
        ("Location", win32more.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE),
        ("SizeInBytes", UInt32),
        ("OffsetInBytes", UInt64),
    ]
    return WHV_VPCI_DEVICE_REGISTER
WHV_VPCI_INTERRUPT_TARGET_FLAGS = UInt32
WHV_VPCI_INTERRUPT_TARGET_FLAGS_WHvVpciInterruptTargetFlagNone = 0
WHV_VPCI_INTERRUPT_TARGET_FLAGS_WHvVpciInterruptTargetFlagMulticast = 1
def _define_WHV_VPCI_INTERRUPT_TARGET_head():
    class WHV_VPCI_INTERRUPT_TARGET(Structure):
        pass
    return WHV_VPCI_INTERRUPT_TARGET
def _define_WHV_VPCI_INTERRUPT_TARGET():
    WHV_VPCI_INTERRUPT_TARGET = win32more.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_head
    WHV_VPCI_INTERRUPT_TARGET._fields_ = [
        ("Vector", UInt32),
        ("Flags", win32more.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_FLAGS),
        ("ProcessorCount", UInt32),
        ("Processors", UInt32 * 0),
    ]
    return WHV_VPCI_INTERRUPT_TARGET
WHV_TRIGGER_TYPE = Int32
WHV_TRIGGER_TYPE_WHvTriggerTypeInterrupt = 0
WHV_TRIGGER_TYPE_WHvTriggerTypeSynicEvent = 1
WHV_TRIGGER_TYPE_WHvTriggerTypeDeviceInterrupt = 2
def _define_WHV_TRIGGER_PARAMETERS_head():
    class WHV_TRIGGER_PARAMETERS(Structure):
        pass
    return WHV_TRIGGER_PARAMETERS
def _define_WHV_TRIGGER_PARAMETERS():
    WHV_TRIGGER_PARAMETERS = win32more.System.Hypervisor.WHV_TRIGGER_PARAMETERS_head
    class WHV_TRIGGER_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class WHV_TRIGGER_PARAMETERS__Anonymous_e__Union__DeviceInterrupt_e__Struct(Structure):
        pass
    WHV_TRIGGER_PARAMETERS__Anonymous_e__Union__DeviceInterrupt_e__Struct._fields_ = [
        ("LogicalDeviceId", UInt64),
        ("MsiAddress", UInt64),
        ("MsiData", UInt32),
        ("Reserved", UInt32),
    ]
    WHV_TRIGGER_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Interrupt", win32more.System.Hypervisor.WHV_INTERRUPT_CONTROL),
        ("SynicEvent", win32more.System.Hypervisor.WHV_SYNIC_EVENT_PARAMETERS),
        ("DeviceInterrupt", WHV_TRIGGER_PARAMETERS__Anonymous_e__Union__DeviceInterrupt_e__Struct),
    ]
    WHV_TRIGGER_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    WHV_TRIGGER_PARAMETERS._fields_ = [
        ("TriggerType", win32more.System.Hypervisor.WHV_TRIGGER_TYPE),
        ("Reserved", UInt32),
        ("Anonymous", WHV_TRIGGER_PARAMETERS__Anonymous_e__Union),
    ]
    return WHV_TRIGGER_PARAMETERS
WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE = Int32
WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE_WHvVirtualProcessorPropertyCodeNumaNode = 0
def _define_WHV_VIRTUAL_PROCESSOR_PROPERTY_head():
    class WHV_VIRTUAL_PROCESSOR_PROPERTY(Structure):
        pass
    return WHV_VIRTUAL_PROCESSOR_PROPERTY
def _define_WHV_VIRTUAL_PROCESSOR_PROPERTY():
    WHV_VIRTUAL_PROCESSOR_PROPERTY = win32more.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_PROPERTY_head
    class WHV_VIRTUAL_PROCESSOR_PROPERTY__Anonymous_e__Union(Union):
        pass
    WHV_VIRTUAL_PROCESSOR_PROPERTY__Anonymous_e__Union._fields_ = [
        ("NumaNode", UInt16),
        ("Padding", UInt64),
    ]
    WHV_VIRTUAL_PROCESSOR_PROPERTY._anonymous_ = [
        'Anonymous',
    ]
    WHV_VIRTUAL_PROCESSOR_PROPERTY._fields_ = [
        ("PropertyCode", win32more.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE),
        ("Reserved", UInt32),
        ("Anonymous", WHV_VIRTUAL_PROCESSOR_PROPERTY__Anonymous_e__Union),
    ]
    return WHV_VIRTUAL_PROCESSOR_PROPERTY
WHV_NOTIFICATION_PORT_TYPE = Int32
WHV_NOTIFICATION_PORT_TYPE_WHvNotificationPortTypeEvent = 2
WHV_NOTIFICATION_PORT_TYPE_WHvNotificationPortTypeDoorbell = 4
def _define_WHV_NOTIFICATION_PORT_PARAMETERS_head():
    class WHV_NOTIFICATION_PORT_PARAMETERS(Structure):
        pass
    return WHV_NOTIFICATION_PORT_PARAMETERS
def _define_WHV_NOTIFICATION_PORT_PARAMETERS():
    WHV_NOTIFICATION_PORT_PARAMETERS = win32more.System.Hypervisor.WHV_NOTIFICATION_PORT_PARAMETERS_head
    class WHV_NOTIFICATION_PORT_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class WHV_NOTIFICATION_PORT_PARAMETERS__Anonymous_e__Union__Event_e__Struct(Structure):
        pass
    WHV_NOTIFICATION_PORT_PARAMETERS__Anonymous_e__Union__Event_e__Struct._fields_ = [
        ("ConnectionId", UInt32),
    ]
    WHV_NOTIFICATION_PORT_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Doorbell", win32more.System.Hypervisor.WHV_DOORBELL_MATCH_DATA),
        ("Event", WHV_NOTIFICATION_PORT_PARAMETERS__Anonymous_e__Union__Event_e__Struct),
    ]
    WHV_NOTIFICATION_PORT_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    WHV_NOTIFICATION_PORT_PARAMETERS._fields_ = [
        ("NotificationPortType", win32more.System.Hypervisor.WHV_NOTIFICATION_PORT_TYPE),
        ("Reserved", UInt32),
        ("Anonymous", WHV_NOTIFICATION_PORT_PARAMETERS__Anonymous_e__Union),
    ]
    return WHV_NOTIFICATION_PORT_PARAMETERS
WHV_NOTIFICATION_PORT_PROPERTY_CODE = Int32
WHV_NOTIFICATION_PORT_PROPERTY_CODE_WHvNotificationPortPropertyPreferredTargetVp = 1
WHV_NOTIFICATION_PORT_PROPERTY_CODE_WHvNotificationPortPropertyPreferredTargetDuration = 5
def _define_WHV_EMULATOR_STATUS_head():
    class WHV_EMULATOR_STATUS(Union):
        pass
    return WHV_EMULATOR_STATUS
def _define_WHV_EMULATOR_STATUS():
    WHV_EMULATOR_STATUS = win32more.System.Hypervisor.WHV_EMULATOR_STATUS_head
    class WHV_EMULATOR_STATUS__Anonymous_e__Struct(Structure):
        pass
    WHV_EMULATOR_STATUS__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    WHV_EMULATOR_STATUS._anonymous_ = [
        'Anonymous',
    ]
    WHV_EMULATOR_STATUS._fields_ = [
        ("Anonymous", WHV_EMULATOR_STATUS__Anonymous_e__Struct),
        ("AsUINT32", UInt32),
    ]
    return WHV_EMULATOR_STATUS
def _define_WHV_EMULATOR_MEMORY_ACCESS_INFO_head():
    class WHV_EMULATOR_MEMORY_ACCESS_INFO(Structure):
        pass
    return WHV_EMULATOR_MEMORY_ACCESS_INFO
def _define_WHV_EMULATOR_MEMORY_ACCESS_INFO():
    WHV_EMULATOR_MEMORY_ACCESS_INFO = win32more.System.Hypervisor.WHV_EMULATOR_MEMORY_ACCESS_INFO_head
    WHV_EMULATOR_MEMORY_ACCESS_INFO._fields_ = [
        ("GpaAddress", UInt64),
        ("Direction", Byte),
        ("AccessSize", Byte),
        ("Data", Byte * 8),
    ]
    return WHV_EMULATOR_MEMORY_ACCESS_INFO
def _define_WHV_EMULATOR_IO_ACCESS_INFO_head():
    class WHV_EMULATOR_IO_ACCESS_INFO(Structure):
        pass
    return WHV_EMULATOR_IO_ACCESS_INFO
def _define_WHV_EMULATOR_IO_ACCESS_INFO():
    WHV_EMULATOR_IO_ACCESS_INFO = win32more.System.Hypervisor.WHV_EMULATOR_IO_ACCESS_INFO_head
    WHV_EMULATOR_IO_ACCESS_INFO._fields_ = [
        ("Direction", Byte),
        ("Port", UInt16),
        ("AccessSize", UInt16),
        ("Data", UInt32),
    ]
    return WHV_EMULATOR_IO_ACCESS_INFO
def _define_WHV_EMULATOR_IO_PORT_CALLBACK():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.Hypervisor.WHV_EMULATOR_IO_ACCESS_INFO_head), use_last_error=False)
def _define_WHV_EMULATOR_MEMORY_CALLBACK():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.Hypervisor.WHV_EMULATOR_MEMORY_ACCESS_INFO_head), use_last_error=False)
def _define_WHV_EMULATOR_GET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.Hypervisor.WHV_REGISTER_NAME),UInt32,POINTER(win32more.System.Hypervisor.WHV_REGISTER_VALUE), use_last_error=False)
def _define_WHV_EMULATOR_SET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.Hypervisor.WHV_REGISTER_NAME),UInt32,POINTER(win32more.System.Hypervisor.WHV_REGISTER_VALUE), use_last_error=False)
def _define_WHV_EMULATOR_TRANSLATE_GVA_PAGE_CALLBACK():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,win32more.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS,POINTER(win32more.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE),POINTER(UInt64), use_last_error=False)
def _define_WHV_EMULATOR_CALLBACKS_head():
    class WHV_EMULATOR_CALLBACKS(Structure):
        pass
    return WHV_EMULATOR_CALLBACKS
def _define_WHV_EMULATOR_CALLBACKS():
    WHV_EMULATOR_CALLBACKS = win32more.System.Hypervisor.WHV_EMULATOR_CALLBACKS_head
    WHV_EMULATOR_CALLBACKS._fields_ = [
        ("Size", UInt32),
        ("Reserved", UInt32),
        ("WHvEmulatorIoPortCallback", win32more.System.Hypervisor.WHV_EMULATOR_IO_PORT_CALLBACK),
        ("WHvEmulatorMemoryCallback", win32more.System.Hypervisor.WHV_EMULATOR_MEMORY_CALLBACK),
        ("WHvEmulatorGetVirtualProcessorRegisters", win32more.System.Hypervisor.WHV_EMULATOR_GET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK),
        ("WHvEmulatorSetVirtualProcessorRegisters", win32more.System.Hypervisor.WHV_EMULATOR_SET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK),
        ("WHvEmulatorTranslateGvaPage", win32more.System.Hypervisor.WHV_EMULATOR_TRANSLATE_GVA_PAGE_CALLBACK),
    ]
    return WHV_EMULATOR_CALLBACKS
def _define_SOCKADDR_HV_head():
    class SOCKADDR_HV(Structure):
        pass
    return SOCKADDR_HV
def _define_SOCKADDR_HV():
    SOCKADDR_HV = win32more.System.Hypervisor.SOCKADDR_HV_head
    SOCKADDR_HV._fields_ = [
        ("Family", UInt16),
        ("Reserved", UInt16),
        ("VmId", Guid),
        ("ServiceId", Guid),
    ]
    return SOCKADDR_HV
def _define_HVSOCKET_ADDRESS_INFO_head():
    class HVSOCKET_ADDRESS_INFO(Structure):
        pass
    return HVSOCKET_ADDRESS_INFO
def _define_HVSOCKET_ADDRESS_INFO():
    HVSOCKET_ADDRESS_INFO = win32more.System.Hypervisor.HVSOCKET_ADDRESS_INFO_head
    HVSOCKET_ADDRESS_INFO._fields_ = [
        ("SystemId", Guid),
        ("VirtualMachineId", Guid),
        ("SiloId", Guid),
        ("Flags", UInt32),
    ]
    return HVSOCKET_ADDRESS_INFO
def _define_VM_GENCOUNTER_head():
    class VM_GENCOUNTER(Structure):
        pass
    return VM_GENCOUNTER
def _define_VM_GENCOUNTER():
    VM_GENCOUNTER = win32more.System.Hypervisor.VM_GENCOUNTER_head
    VM_GENCOUNTER._fields_ = [
        ("GenerationCount", UInt64),
        ("GenerationCountHigh", UInt64),
    ]
    return VM_GENCOUNTER
HDV_DEVICE_TYPE = Int32
HDV_DEVICE_TYPE_HdvDeviceTypeUndefined = 0
HDV_DEVICE_TYPE_HdvDeviceTypePCI = 1
def _define_HDV_PCI_PNP_ID_head():
    class HDV_PCI_PNP_ID(Structure):
        pass
    return HDV_PCI_PNP_ID
def _define_HDV_PCI_PNP_ID():
    HDV_PCI_PNP_ID = win32more.System.Hypervisor.HDV_PCI_PNP_ID_head
    HDV_PCI_PNP_ID._fields_ = [
        ("VendorID", UInt16),
        ("DeviceID", UInt16),
        ("RevisionID", Byte),
        ("ProgIf", Byte),
        ("SubClass", Byte),
        ("BaseClass", Byte),
        ("SubVendorID", UInt16),
        ("SubSystemID", UInt16),
    ]
    return HDV_PCI_PNP_ID
HDV_PCI_BAR_SELECTOR = Int32
HDV_PCI_BAR0 = 0
HDV_PCI_BAR1 = 1
HDV_PCI_BAR2 = 2
HDV_PCI_BAR3 = 3
HDV_PCI_BAR4 = 4
HDV_PCI_BAR5 = 5
HDV_DOORBELL_FLAGS = Int32
HDV_DOORBELL_FLAG_TRIGGER_SIZE_ANY = 0
HDV_DOORBELL_FLAG_TRIGGER_SIZE_BYTE = 1
HDV_DOORBELL_FLAG_TRIGGER_SIZE_WORD = 2
HDV_DOORBELL_FLAG_TRIGGER_SIZE_DWORD = 3
HDV_DOORBELL_FLAG_TRIGGER_SIZE_QWORD = 4
HDV_DOORBELL_FLAG_TRIGGER_ANY_VALUE = -2147483648
HDV_MMIO_MAPPING_FLAGS = UInt32
HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagNone = 0
HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagWriteable = 1
HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagExecutable = 2
def _define_HDV_PCI_DEVICE_INITIALIZE():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)
def _define_HDV_PCI_DEVICE_TEARDOWN():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_HDV_PCI_DEVICE_SET_CONFIGURATION():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)
def _define_HDV_PCI_DEVICE_GET_DETAILS():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.Hypervisor.HDV_PCI_PNP_ID_head),UInt32,POINTER(UInt32), use_last_error=False)
def _define_HDV_PCI_DEVICE_START():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)
def _define_HDV_PCI_DEVICE_STOP():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_HDV_PCI_READ_CONFIG_SPACE():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)
def _define_HDV_PCI_WRITE_CONFIG_SPACE():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt32, use_last_error=False)
def _define_HDV_PCI_READ_INTERCEPTED_MEMORY():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR,UInt64,UInt64,POINTER(Byte), use_last_error=False)
def _define_HDV_PCI_WRITE_INTERCEPTED_MEMORY():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR,UInt64,UInt64,POINTER(Byte), use_last_error=False)
HDV_PCI_INTERFACE_VERSION = Int32
HDV_PCI_INTERFACE_VERSION_HdvPciDeviceInterfaceVersionInvalid = 0
HDV_PCI_INTERFACE_VERSION_HdvPciDeviceInterfaceVersion1 = 1
def _define_HDV_PCI_DEVICE_INTERFACE_head():
    class HDV_PCI_DEVICE_INTERFACE(Structure):
        pass
    return HDV_PCI_DEVICE_INTERFACE
def _define_HDV_PCI_DEVICE_INTERFACE():
    HDV_PCI_DEVICE_INTERFACE = win32more.System.Hypervisor.HDV_PCI_DEVICE_INTERFACE_head
    HDV_PCI_DEVICE_INTERFACE._fields_ = [
        ("Version", win32more.System.Hypervisor.HDV_PCI_INTERFACE_VERSION),
        ("Initialize", win32more.System.Hypervisor.HDV_PCI_DEVICE_INITIALIZE),
        ("Teardown", win32more.System.Hypervisor.HDV_PCI_DEVICE_TEARDOWN),
        ("SetConfiguration", win32more.System.Hypervisor.HDV_PCI_DEVICE_SET_CONFIGURATION),
        ("GetDetails", win32more.System.Hypervisor.HDV_PCI_DEVICE_GET_DETAILS),
        ("Start", win32more.System.Hypervisor.HDV_PCI_DEVICE_START),
        ("Stop", win32more.System.Hypervisor.HDV_PCI_DEVICE_STOP),
        ("ReadConfigSpace", win32more.System.Hypervisor.HDV_PCI_READ_CONFIG_SPACE),
        ("WriteConfigSpace", win32more.System.Hypervisor.HDV_PCI_WRITE_CONFIG_SPACE),
        ("ReadInterceptedMemory", win32more.System.Hypervisor.HDV_PCI_READ_INTERCEPTED_MEMORY),
        ("WriteInterceptedMemory", win32more.System.Hypervisor.HDV_PCI_WRITE_INTERCEPTED_MEMORY),
    ]
    return HDV_PCI_DEVICE_INTERFACE
PAGING_MODE = Int32
Paging_Invalid = 0
Paging_NonPaged = 1
Paging_32Bit = 2
Paging_Pae = 3
Paging_Long = 4
Paging_Armv8 = 5
def _define_GPA_MEMORY_CHUNK_head():
    class GPA_MEMORY_CHUNK(Structure):
        pass
    return GPA_MEMORY_CHUNK
def _define_GPA_MEMORY_CHUNK():
    GPA_MEMORY_CHUNK = win32more.System.Hypervisor.GPA_MEMORY_CHUNK_head
    GPA_MEMORY_CHUNK._fields_ = [
        ("GuestPhysicalStartPageIndex", UInt64),
        ("PageCount", UInt64),
    ]
    return GPA_MEMORY_CHUNK
VIRTUAL_PROCESSOR_ARCH = Int32
Arch_Unknown = 0
Arch_x86 = 1
Arch_x64 = 2
Arch_Armv8 = 3
VIRTUAL_PROCESSOR_VENDOR = Int32
ProcessorVendor_Unknown = 0
ProcessorVendor_Amd = 1
ProcessorVendor_Intel = 2
ProcessorVendor_Hygon = 3
ProcessorVendor_Arm = 4
GUEST_OS_VENDOR = Int32
GUEST_OS_VENDOR_GuestOsVendorUndefined = 0
GUEST_OS_VENDOR_GuestOsVendorMicrosoft = 1
GUEST_OS_VENDOR_GuestOsVendorHPE = 2
GUEST_OS_VENDOR_GuestOsVendorLANCOM = 512
GUEST_OS_MICROSOFT_IDS = Int32
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftUndefined = 0
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftMSDOS = 1
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindows3x = 2
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindows9x = 3
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindowsNT = 4
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindowsCE = 5
GUEST_OS_OPENSOURCE_IDS = Int32
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceUndefined = 0
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceLinux = 1
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceFreeBSD = 2
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceXen = 3
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceIllumos = 4
def _define_GUEST_OS_INFO_head():
    class GUEST_OS_INFO(Union):
        pass
    return GUEST_OS_INFO
def _define_GUEST_OS_INFO():
    GUEST_OS_INFO = win32more.System.Hypervisor.GUEST_OS_INFO_head
    class GUEST_OS_INFO__OpenSource_e__Struct(Structure):
        pass
    GUEST_OS_INFO__OpenSource_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    class GUEST_OS_INFO__ClosedSource_e__Struct(Structure):
        pass
    GUEST_OS_INFO__ClosedSource_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    GUEST_OS_INFO._fields_ = [
        ("AsUINT64", UInt64),
        ("ClosedSource", GUEST_OS_INFO__ClosedSource_e__Struct),
        ("OpenSource", GUEST_OS_INFO__OpenSource_e__Struct),
    ]
    return GUEST_OS_INFO
REGISTER_ID = Int32
X64_RegisterRax = 0
X64_RegisterRcx = 1
X64_RegisterRdx = 2
X64_RegisterRbx = 3
X64_RegisterRsp = 4
X64_RegisterRbp = 5
X64_RegisterRsi = 6
X64_RegisterRdi = 7
X64_RegisterR8 = 8
X64_RegisterR9 = 9
X64_RegisterR10 = 10
X64_RegisterR11 = 11
X64_RegisterR12 = 12
X64_RegisterR13 = 13
X64_RegisterR14 = 14
X64_RegisterR15 = 15
X64_RegisterRip = 16
X64_RegisterRFlags = 17
X64_RegisterXmm0 = 18
X64_RegisterXmm1 = 19
X64_RegisterXmm2 = 20
X64_RegisterXmm3 = 21
X64_RegisterXmm4 = 22
X64_RegisterXmm5 = 23
X64_RegisterXmm6 = 24
X64_RegisterXmm7 = 25
X64_RegisterXmm8 = 26
X64_RegisterXmm9 = 27
X64_RegisterXmm10 = 28
X64_RegisterXmm11 = 29
X64_RegisterXmm12 = 30
X64_RegisterXmm13 = 31
X64_RegisterXmm14 = 32
X64_RegisterXmm15 = 33
X64_RegisterFpMmx0 = 34
X64_RegisterFpMmx1 = 35
X64_RegisterFpMmx2 = 36
X64_RegisterFpMmx3 = 37
X64_RegisterFpMmx4 = 38
X64_RegisterFpMmx5 = 39
X64_RegisterFpMmx6 = 40
X64_RegisterFpMmx7 = 41
X64_RegisterFpControlStatus = 42
X64_RegisterXmmControlStatus = 43
X64_RegisterCr0 = 44
X64_RegisterCr2 = 45
X64_RegisterCr3 = 46
X64_RegisterCr4 = 47
X64_RegisterCr8 = 48
X64_RegisterEfer = 49
X64_RegisterDr0 = 50
X64_RegisterDr1 = 51
X64_RegisterDr2 = 52
X64_RegisterDr3 = 53
X64_RegisterDr6 = 54
X64_RegisterDr7 = 55
X64_RegisterEs = 56
X64_RegisterCs = 57
X64_RegisterSs = 58
X64_RegisterDs = 59
X64_RegisterFs = 60
X64_RegisterGs = 61
X64_RegisterLdtr = 62
X64_RegisterTr = 63
X64_RegisterIdtr = 64
X64_RegisterGdtr = 65
X64_RegisterMax = 66
ARM64_RegisterX0 = 67
ARM64_RegisterX1 = 68
ARM64_RegisterX2 = 69
ARM64_RegisterX3 = 70
ARM64_RegisterX4 = 71
ARM64_RegisterX5 = 72
ARM64_RegisterX6 = 73
ARM64_RegisterX7 = 74
ARM64_RegisterX8 = 75
ARM64_RegisterX9 = 76
ARM64_RegisterX10 = 77
ARM64_RegisterX11 = 78
ARM64_RegisterX12 = 79
ARM64_RegisterX13 = 80
ARM64_RegisterX14 = 81
ARM64_RegisterX15 = 82
ARM64_RegisterX16 = 83
ARM64_RegisterX17 = 84
ARM64_RegisterX18 = 85
ARM64_RegisterX19 = 86
ARM64_RegisterX20 = 87
ARM64_RegisterX21 = 88
ARM64_RegisterX22 = 89
ARM64_RegisterX23 = 90
ARM64_RegisterX24 = 91
ARM64_RegisterX25 = 92
ARM64_RegisterX26 = 93
ARM64_RegisterX27 = 94
ARM64_RegisterX28 = 95
ARM64_RegisterXFp = 96
ARM64_RegisterXLr = 97
ARM64_RegisterPc = 98
ARM64_RegisterSpEl0 = 99
ARM64_RegisterSpEl1 = 100
ARM64_RegisterCpsr = 101
ARM64_RegisterQ0 = 102
ARM64_RegisterQ1 = 103
ARM64_RegisterQ2 = 104
ARM64_RegisterQ3 = 105
ARM64_RegisterQ4 = 106
ARM64_RegisterQ5 = 107
ARM64_RegisterQ6 = 108
ARM64_RegisterQ7 = 109
ARM64_RegisterQ8 = 110
ARM64_RegisterQ9 = 111
ARM64_RegisterQ10 = 112
ARM64_RegisterQ11 = 113
ARM64_RegisterQ12 = 114
ARM64_RegisterQ13 = 115
ARM64_RegisterQ14 = 116
ARM64_RegisterQ15 = 117
ARM64_RegisterQ16 = 118
ARM64_RegisterQ17 = 119
ARM64_RegisterQ18 = 120
ARM64_RegisterQ19 = 121
ARM64_RegisterQ20 = 122
ARM64_RegisterQ21 = 123
ARM64_RegisterQ22 = 124
ARM64_RegisterQ23 = 125
ARM64_RegisterQ24 = 126
ARM64_RegisterQ25 = 127
ARM64_RegisterQ26 = 128
ARM64_RegisterQ27 = 129
ARM64_RegisterQ28 = 130
ARM64_RegisterQ29 = 131
ARM64_RegisterQ30 = 132
ARM64_RegisterQ31 = 133
ARM64_RegisterFpStatus = 134
ARM64_RegisterFpControl = 135
ARM64_RegisterEsrEl1 = 136
ARM64_RegisterSpsrEl1 = 137
ARM64_RegisterFarEl1 = 138
ARM64_RegisterParEl1 = 139
ARM64_RegisterElrEl1 = 140
ARM64_RegisterTtbr0El1 = 141
ARM64_RegisterTtbr1El1 = 142
ARM64_RegisterVbarEl1 = 143
ARM64_RegisterSctlrEl1 = 144
ARM64_RegisterActlrEl1 = 145
ARM64_RegisterTcrEl1 = 146
ARM64_RegisterMairEl1 = 147
ARM64_RegisterAmairEl1 = 148
ARM64_RegisterTpidrEl0 = 149
ARM64_RegisterTpidrroEl0 = 150
ARM64_RegisterTpidrEl1 = 151
ARM64_RegisterContextIdrEl1 = 152
ARM64_RegisterCpacrEl1 = 153
ARM64_RegisterCsselrEl1 = 154
ARM64_RegisterCntkctlEl1 = 155
ARM64_RegisterCntvCvalEl0 = 156
ARM64_RegisterCntvCtlEl0 = 157
ARM64_RegisterMax = 158
def _define_VIRTUAL_PROCESSOR_REGISTER_head():
    class VIRTUAL_PROCESSOR_REGISTER(Union):
        pass
    return VIRTUAL_PROCESSOR_REGISTER
def _define_VIRTUAL_PROCESSOR_REGISTER():
    VIRTUAL_PROCESSOR_REGISTER = win32more.System.Hypervisor.VIRTUAL_PROCESSOR_REGISTER_head
    class VIRTUAL_PROCESSOR_REGISTER__X64_e__Union(Union):
        pass
    class VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__XmmControlStatus_e__Struct(Structure):
        pass
    class VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__XmmControlStatus_e__Struct__Anonymous_e__Union(Union):
        pass
    class VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__XmmControlStatus_e__Struct__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__XmmControlStatus_e__Struct__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("LastFpDp", UInt32),
        ("LastFpDs", UInt16),
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__XmmControlStatus_e__Struct__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__XmmControlStatus_e__Struct__Anonymous_e__Union._fields_ = [
        ("LastFpRdp", UInt64),
        ("Anonymous", VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__XmmControlStatus_e__Struct__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__XmmControlStatus_e__Struct._anonymous_ = [
        'Anonymous',
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__XmmControlStatus_e__Struct._fields_ = [
        ("Anonymous", VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__XmmControlStatus_e__Struct__Anonymous_e__Union),
        ("XmmStatusControl", UInt32),
        ("XmmStatusControlMask", UInt32),
    ]
    class VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__FpControlStatus_e__Struct(Structure):
        pass
    class VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__FpControlStatus_e__Struct__Anonymous_e__Union(Union):
        pass
    class VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__FpControlStatus_e__Struct__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__FpControlStatus_e__Struct__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("LastFpEip", UInt32),
        ("LastFpCs", UInt16),
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__FpControlStatus_e__Struct__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__FpControlStatus_e__Struct__Anonymous_e__Union._fields_ = [
        ("LastFpRip", UInt64),
        ("Anonymous", VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__FpControlStatus_e__Struct__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__FpControlStatus_e__Struct._anonymous_ = [
        'Anonymous',
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__FpControlStatus_e__Struct._fields_ = [
        ("FpControl", UInt16),
        ("FpStatus", UInt16),
        ("FpTag", Byte),
        ("Reserved", Byte),
        ("LastFpOp", UInt16),
        ("Anonymous", VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__FpControlStatus_e__Struct__Anonymous_e__Union),
    ]
    class VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Segment_e__Struct(Structure):
        pass
    class VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Segment_e__Struct__Anonymous_e__Union(Union):
        pass
    class VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Segment_e__Struct__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Segment_e__Struct__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt16),
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Segment_e__Struct__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Segment_e__Struct__Anonymous_e__Union._fields_ = [
        ("Attributes", UInt16),
        ("Anonymous", VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Segment_e__Struct__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Segment_e__Struct._anonymous_ = [
        'Anonymous',
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Segment_e__Struct._fields_ = [
        ("Base", UInt64),
        ("Limit", UInt32),
        ("Selector", UInt16),
        ("Anonymous", VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Segment_e__Struct__Anonymous_e__Union),
    ]
    class VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Table_e__Struct(Structure):
        pass
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Table_e__Struct._fields_ = [
        ("Limit", UInt16),
        ("Base", UInt64),
    ]
    VIRTUAL_PROCESSOR_REGISTER__X64_e__Union._fields_ = [
        ("Segment", VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Segment_e__Struct),
        ("Table", VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__Table_e__Struct),
        ("FpControlStatus", VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__FpControlStatus_e__Struct),
        ("XmmControlStatus", VIRTUAL_PROCESSOR_REGISTER__X64_e__Union__XmmControlStatus_e__Struct),
    ]
    class VIRTUAL_PROCESSOR_REGISTER__Reg128_e__Struct(Structure):
        pass
    VIRTUAL_PROCESSOR_REGISTER__Reg128_e__Struct._fields_ = [
        ("Low64", UInt64),
        ("High64", UInt64),
    ]
    VIRTUAL_PROCESSOR_REGISTER._fields_ = [
        ("Reg64", UInt64),
        ("Reg32", UInt32),
        ("Reg16", UInt16),
        ("Reg8", Byte),
        ("Reg128", VIRTUAL_PROCESSOR_REGISTER__Reg128_e__Struct),
        ("X64", VIRTUAL_PROCESSOR_REGISTER__X64_e__Union),
    ]
    return VIRTUAL_PROCESSOR_REGISTER
def _define_DOS_IMAGE_INFO_head():
    class DOS_IMAGE_INFO(Structure):
        pass
    return DOS_IMAGE_INFO
def _define_DOS_IMAGE_INFO():
    DOS_IMAGE_INFO = win32more.System.Hypervisor.DOS_IMAGE_INFO_head
    DOS_IMAGE_INFO._fields_ = [
        ("PdbName", win32more.Foundation.PSTR),
        ("ImageBaseAddress", UInt64),
        ("ImageSize", UInt32),
        ("Timestamp", UInt32),
    ]
    return DOS_IMAGE_INFO
def _define_GUEST_SYMBOLS_PROVIDER_DEBUG_INFO_CALLBACK():
    return CFUNCTYPE(Void,win32more.Foundation.PSTR, use_last_error=False)
def _define_FOUND_IMAGE_CALLBACK():
    return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.System.Hypervisor.DOS_IMAGE_INFO_head), use_last_error=False)
def _define_MODULE_INFO_head():
    class MODULE_INFO(Structure):
        pass
    return MODULE_INFO
def _define_MODULE_INFO():
    MODULE_INFO = win32more.System.Hypervisor.MODULE_INFO_head
    MODULE_INFO._fields_ = [
        ("ProcessImageName", win32more.Foundation.PSTR),
        ("Image", win32more.System.Hypervisor.DOS_IMAGE_INFO),
    ]
    return MODULE_INFO
def _define_WHvGetCapability():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_CAPABILITY_CODE,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("WHvGetCapability", windll["WinHvPlatform"]), ((1, 'CapabilityCode'),(1, 'CapabilityBuffer'),(1, 'CapabilityBufferSizeInBytes'),(1, 'WrittenSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvCreatePartition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Hypervisor.WHV_PARTITION_HANDLE), use_last_error=False)(("WHvCreatePartition", windll["WinHvPlatform"]), ((1, 'Partition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvSetupPartition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE, use_last_error=False)(("WHvSetupPartition", windll["WinHvPlatform"]), ((1, 'Partition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvResetPartition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE, use_last_error=False)(("WHvResetPartition", windll["WinHvPlatform"]), ((1, 'Partition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvDeletePartition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE, use_last_error=False)(("WHvDeletePartition", windll["WinHvPlatform"]), ((1, 'Partition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetPartitionProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,win32more.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("WHvGetPartitionProperty", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'PropertyCode'),(1, 'PropertyBuffer'),(1, 'PropertyBufferSizeInBytes'),(1, 'WrittenSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvSetPartitionProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,win32more.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE,c_void_p,UInt32, use_last_error=False)(("WHvSetPartitionProperty", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'PropertyCode'),(1, 'PropertyBuffer'),(1, 'PropertyBufferSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvSuspendPartitionTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE, use_last_error=False)(("WHvSuspendPartitionTime", windll["WinHvPlatform"]), ((1, 'Partition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvResumePartitionTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE, use_last_error=False)(("WHvResumePartitionTime", windll["WinHvPlatform"]), ((1, 'Partition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvMapGpaRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,c_void_p,UInt64,UInt64,win32more.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS, use_last_error=False)(("WHvMapGpaRange", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'SourceAddress'),(1, 'GuestAddress'),(1, 'SizeInBytes'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvMapGpaRange2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,win32more.Foundation.HANDLE,c_void_p,UInt64,UInt64,win32more.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS, use_last_error=False)(("WHvMapGpaRange2", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'Process'),(1, 'SourceAddress'),(1, 'GuestAddress'),(1, 'SizeInBytes'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvUnmapGpaRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,UInt64, use_last_error=False)(("WHvUnmapGpaRange", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'GuestAddress'),(1, 'SizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvTranslateGva():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,UInt64,win32more.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS,POINTER(win32more.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_head),POINTER(UInt64), use_last_error=False)(("WHvTranslateGva", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'Gva'),(1, 'TranslateFlags'),(1, 'TranslationResult'),(1, 'Gpa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvCreateVirtualProcessor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,UInt32, use_last_error=False)(("WHvCreateVirtualProcessor", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvCreateVirtualProcessor2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,POINTER(win32more.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_PROPERTY),UInt32, use_last_error=False)(("WHvCreateVirtualProcessor2", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'Properties'),(1, 'PropertyCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvDeleteVirtualProcessor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32, use_last_error=False)(("WHvDeleteVirtualProcessor", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvRunVirtualProcessor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,c_void_p,UInt32, use_last_error=False)(("WHvRunVirtualProcessor", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'ExitContext'),(1, 'ExitContextSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvCancelRunVirtualProcessor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,UInt32, use_last_error=False)(("WHvCancelRunVirtualProcessor", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetVirtualProcessorRegisters():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,POINTER(win32more.System.Hypervisor.WHV_REGISTER_NAME),UInt32,POINTER(win32more.System.Hypervisor.WHV_REGISTER_VALUE), use_last_error=False)(("WHvGetVirtualProcessorRegisters", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'RegisterNames'),(1, 'RegisterCount'),(1, 'RegisterValues'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvSetVirtualProcessorRegisters():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,POINTER(win32more.System.Hypervisor.WHV_REGISTER_NAME),UInt32,POINTER(win32more.System.Hypervisor.WHV_REGISTER_VALUE), use_last_error=False)(("WHvSetVirtualProcessorRegisters", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'RegisterNames'),(1, 'RegisterCount'),(1, 'RegisterValues'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetVirtualProcessorInterruptControllerState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("WHvGetVirtualProcessorInterruptControllerState", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'State'),(1, 'StateSize'),(1, 'WrittenSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvSetVirtualProcessorInterruptControllerState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,c_void_p,UInt32, use_last_error=False)(("WHvSetVirtualProcessorInterruptControllerState", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'State'),(1, 'StateSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvRequestInterrupt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,POINTER(win32more.System.Hypervisor.WHV_INTERRUPT_CONTROL_head),UInt32, use_last_error=False)(("WHvRequestInterrupt", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'Interrupt'),(1, 'InterruptControlSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetVirtualProcessorXsaveState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("WHvGetVirtualProcessorXsaveState", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'Buffer'),(1, 'BufferSizeInBytes'),(1, 'BytesWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvSetVirtualProcessorXsaveState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,c_void_p,UInt32, use_last_error=False)(("WHvSetVirtualProcessorXsaveState", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'Buffer'),(1, 'BufferSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvQueryGpaRangeDirtyBitmap():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,UInt64,POINTER(UInt64),UInt32, use_last_error=False)(("WHvQueryGpaRangeDirtyBitmap", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'GuestAddress'),(1, 'RangeSizeInBytes'),(1, 'Bitmap'),(1, 'BitmapSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetPartitionCounters():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,win32more.System.Hypervisor.WHV_PARTITION_COUNTER_SET,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("WHvGetPartitionCounters", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'CounterSet'),(1, 'Buffer'),(1, 'BufferSizeInBytes'),(1, 'BytesWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetVirtualProcessorCounters():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,win32more.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("WHvGetVirtualProcessorCounters", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'CounterSet'),(1, 'Buffer'),(1, 'BufferSizeInBytes'),(1, 'BytesWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetVirtualProcessorInterruptControllerState2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("WHvGetVirtualProcessorInterruptControllerState2", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'State'),(1, 'StateSize'),(1, 'WrittenSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvSetVirtualProcessorInterruptControllerState2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,c_void_p,UInt32, use_last_error=False)(("WHvSetVirtualProcessorInterruptControllerState2", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'State'),(1, 'StateSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvRegisterPartitionDoorbellEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,POINTER(win32more.System.Hypervisor.WHV_DOORBELL_MATCH_DATA_head),win32more.Foundation.HANDLE, use_last_error=False)(("WHvRegisterPartitionDoorbellEvent", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'MatchData'),(1, 'EventHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvUnregisterPartitionDoorbellEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,POINTER(win32more.System.Hypervisor.WHV_DOORBELL_MATCH_DATA_head), use_last_error=False)(("WHvUnregisterPartitionDoorbellEvent", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'MatchData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvAdviseGpaRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,POINTER(win32more.System.Hypervisor.WHV_MEMORY_RANGE_ENTRY),UInt32,win32more.System.Hypervisor.WHV_ADVISE_GPA_RANGE_CODE,c_void_p,UInt32, use_last_error=False)(("WHvAdviseGpaRange", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'GpaRanges'),(1, 'GpaRangesCount'),(1, 'Advice'),(1, 'AdviceBuffer'),(1, 'AdviceBufferSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvReadGpaRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,UInt64,win32more.System.Hypervisor.WHV_ACCESS_GPA_CONTROLS,c_void_p,UInt32, use_last_error=False)(("WHvReadGpaRange", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'GuestAddress'),(1, 'Controls'),(1, 'Data'),(1, 'DataSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvWriteGpaRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,UInt64,win32more.System.Hypervisor.WHV_ACCESS_GPA_CONTROLS,c_void_p,UInt32, use_last_error=False)(("WHvWriteGpaRange", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'GuestAddress'),(1, 'Controls'),(1, 'Data'),(1, 'DataSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvSignalVirtualProcessorSynicEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,win32more.System.Hypervisor.WHV_SYNIC_EVENT_PARAMETERS,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("WHvSignalVirtualProcessorSynicEvent", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'SynicEvent'),(1, 'NewlySignaled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetVirtualProcessorState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,win32more.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("WHvGetVirtualProcessorState", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'StateType'),(1, 'Buffer'),(1, 'BufferSizeInBytes'),(1, 'BytesWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvSetVirtualProcessorState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,win32more.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE,c_void_p,UInt32, use_last_error=False)(("WHvSetVirtualProcessorState", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'StateType'),(1, 'Buffer'),(1, 'BufferSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvAllocateVpciResource():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Hypervisor.WHV_ALLOCATE_VPCI_RESOURCE_FLAGS,POINTER(Void),UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("WHvAllocateVpciResource", windll["WinHvPlatform"]), ((1, 'ProviderId'),(1, 'Flags'),(1, 'ResourceDescriptor'),(1, 'ResourceDescriptorSizeInBytes'),(1, 'VpciResource'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvCreateVpciDevice():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,win32more.Foundation.HANDLE,win32more.System.Hypervisor.WHV_CREATE_VPCI_DEVICE_FLAGS,win32more.Foundation.HANDLE, use_last_error=False)(("WHvCreateVpciDevice", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'VpciResource'),(1, 'Flags'),(1, 'NotificationEventHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvDeleteVpciDevice():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64, use_last_error=False)(("WHvDeleteVpciDevice", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetVpciDeviceProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,win32more.System.Hypervisor.WHV_VPCI_DEVICE_PROPERTY_CODE,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("WHvGetVpciDeviceProperty", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'PropertyCode'),(1, 'PropertyBuffer'),(1, 'PropertyBufferSizeInBytes'),(1, 'WrittenSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetVpciDeviceNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,POINTER(win32more.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_head),UInt32, use_last_error=False)(("WHvGetVpciDeviceNotification", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'Notification'),(1, 'NotificationSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvMapVpciDeviceMmioRanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,POINTER(UInt32),POINTER(POINTER(win32more.System.Hypervisor.WHV_VPCI_MMIO_MAPPING_head)), use_last_error=False)(("WHvMapVpciDeviceMmioRanges", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'MappingCount'),(1, 'Mappings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvUnmapVpciDeviceMmioRanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64, use_last_error=False)(("WHvUnmapVpciDeviceMmioRanges", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvSetVpciDevicePowerState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,win32more.System.Power.DEVICE_POWER_STATE, use_last_error=False)(("WHvSetVpciDevicePowerState", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'PowerState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvReadVpciDeviceRegister():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,POINTER(win32more.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_head),c_void_p, use_last_error=False)(("WHvReadVpciDeviceRegister", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'Register'),(1, 'Data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvWriteVpciDeviceRegister():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,POINTER(win32more.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_head),c_void_p, use_last_error=False)(("WHvWriteVpciDeviceRegister", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'Register'),(1, 'Data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvMapVpciDeviceInterrupt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,UInt32,UInt32,POINTER(win32more.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_head),POINTER(UInt64),POINTER(UInt32), use_last_error=False)(("WHvMapVpciDeviceInterrupt", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'Index'),(1, 'MessageCount'),(1, 'Target'),(1, 'MsiAddress'),(1, 'MsiData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvUnmapVpciDeviceInterrupt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,UInt32, use_last_error=False)(("WHvUnmapVpciDeviceInterrupt", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'Index'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvRetargetVpciDeviceInterrupt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,UInt64,UInt32,POINTER(win32more.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_head), use_last_error=False)(("WHvRetargetVpciDeviceInterrupt", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'MsiAddress'),(1, 'MsiData'),(1, 'Target'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvRequestVpciDeviceInterrupt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,UInt64,UInt32, use_last_error=False)(("WHvRequestVpciDeviceInterrupt", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'MsiAddress'),(1, 'MsiData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetVpciDeviceInterruptTarget():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,UInt32,UInt32,POINTER(win32more.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_head),UInt32,POINTER(UInt32), use_last_error=False)(("WHvGetVpciDeviceInterruptTarget", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'LogicalDeviceId'),(1, 'Index'),(1, 'MultiMessageNumber'),(1, 'Target'),(1, 'TargetSizeInBytes'),(1, 'BytesWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvCreateTrigger():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,POINTER(win32more.System.Hypervisor.WHV_TRIGGER_PARAMETERS_head),POINTER(c_void_p),POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("WHvCreateTrigger", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'Parameters'),(1, 'TriggerHandle'),(1, 'EventHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvUpdateTriggerParameters():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,POINTER(win32more.System.Hypervisor.WHV_TRIGGER_PARAMETERS_head),c_void_p, use_last_error=False)(("WHvUpdateTriggerParameters", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'Parameters'),(1, 'TriggerHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvDeleteTrigger():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,c_void_p, use_last_error=False)(("WHvDeleteTrigger", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'TriggerHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvCreateNotificationPort():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,POINTER(win32more.System.Hypervisor.WHV_NOTIFICATION_PORT_PARAMETERS_head),win32more.Foundation.HANDLE,POINTER(c_void_p), use_last_error=False)(("WHvCreateNotificationPort", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'Parameters'),(1, 'EventHandle'),(1, 'PortHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvSetNotificationPortProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,c_void_p,win32more.System.Hypervisor.WHV_NOTIFICATION_PORT_PROPERTY_CODE,UInt64, use_last_error=False)(("WHvSetNotificationPortProperty", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'PortHandle'),(1, 'PropertyCode'),(1, 'PropertyValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvDeleteNotificationPort():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,c_void_p, use_last_error=False)(("WHvDeleteNotificationPort", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'PortHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvPostVirtualProcessorSynicMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,UInt32,c_void_p,UInt32, use_last_error=False)(("WHvPostVirtualProcessorSynicMessage", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'SintIndex'),(1, 'Message'),(1, 'MessageSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetVirtualProcessorCpuidOutput():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt32,UInt32,UInt32,POINTER(win32more.System.Hypervisor.WHV_CPUID_OUTPUT_head), use_last_error=False)(("WHvGetVirtualProcessorCpuidOutput", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'VpIndex'),(1, 'Eax'),(1, 'Ecx'),(1, 'CpuidOutput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvGetInterruptTargetVpSet():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,UInt64,win32more.System.Hypervisor.WHV_INTERRUPT_DESTINATION_MODE,POINTER(UInt32),UInt32,POINTER(UInt32), use_last_error=False)(("WHvGetInterruptTargetVpSet", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'Destination'),(1, 'DestinationMode'),(1, 'TargetVps'),(1, 'VpCount'),(1, 'TargetVpCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvStartPartitionMigration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("WHvStartPartitionMigration", windll["WinHvPlatform"]), ((1, 'Partition'),(1, 'MigrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvCancelPartitionMigration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE, use_last_error=False)(("WHvCancelPartitionMigration", windll["WinHvPlatform"]), ((1, 'Partition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvCompletePartitionMigration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Hypervisor.WHV_PARTITION_HANDLE, use_last_error=False)(("WHvCompletePartitionMigration", windll["WinHvPlatform"]), ((1, 'Partition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvAcceptPartitionMigration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.System.Hypervisor.WHV_PARTITION_HANDLE), use_last_error=False)(("WHvAcceptPartitionMigration", windll["WinHvPlatform"]), ((1, 'MigrationHandle'),(1, 'Partition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvEmulatorCreateEmulator():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Hypervisor.WHV_EMULATOR_CALLBACKS_head),POINTER(c_void_p), use_last_error=False)(("WHvEmulatorCreateEmulator", windll["WinHvEmulation"]), ((1, 'Callbacks'),(1, 'Emulator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvEmulatorDestroyEmulator():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("WHvEmulatorDestroyEmulator", windll["WinHvEmulation"]), ((1, 'Emulator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvEmulatorTryIoEmulation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,POINTER(win32more.System.Hypervisor.WHV_VP_EXIT_CONTEXT_head),POINTER(win32more.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_CONTEXT_head),POINTER(win32more.System.Hypervisor.WHV_EMULATOR_STATUS_head), use_last_error=False)(("WHvEmulatorTryIoEmulation", windll["WinHvEmulation"]), ((1, 'Emulator'),(1, 'Context'),(1, 'VpContext'),(1, 'IoInstructionContext'),(1, 'EmulatorReturnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WHvEmulatorTryMmioEmulation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,POINTER(win32more.System.Hypervisor.WHV_VP_EXIT_CONTEXT_head),POINTER(win32more.System.Hypervisor.WHV_MEMORY_ACCESS_CONTEXT_head),POINTER(win32more.System.Hypervisor.WHV_EMULATOR_STATUS_head), use_last_error=False)(("WHvEmulatorTryMmioEmulation", windll["WinHvEmulation"]), ((1, 'Emulator'),(1, 'Context'),(1, 'VpContext'),(1, 'MmioInstructionContext'),(1, 'EmulatorReturnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvInitializeDeviceHost():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,POINTER(c_void_p), use_last_error=False)(("HdvInitializeDeviceHost", windll["vmdevicehost"]), ((1, 'computeSystem'),(1, 'deviceHostHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvTeardownDeviceHost():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("HdvTeardownDeviceHost", windll["vmdevicehost"]), ((1, 'deviceHostHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvCreateDeviceInstance():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Hypervisor.HDV_DEVICE_TYPE,POINTER(Guid),POINTER(Guid),c_void_p,c_void_p,POINTER(c_void_p), use_last_error=False)(("HdvCreateDeviceInstance", windll["vmdevicehost"]), ((1, 'deviceHostHandle'),(1, 'deviceType'),(1, 'deviceClassId'),(1, 'deviceInstanceId'),(1, 'deviceInterface'),(1, 'deviceContext'),(1, 'deviceHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvReadGuestMemory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,UInt32,POINTER(Byte), use_last_error=False)(("HdvReadGuestMemory", windll["vmdevicehost"]), ((1, 'requestor'),(1, 'guestPhysicalAddress'),(1, 'byteCount'),(1, 'buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvWriteGuestMemory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,UInt32,POINTER(Byte), use_last_error=False)(("HdvWriteGuestMemory", windll["vmdevicehost"]), ((1, 'requestor'),(1, 'guestPhysicalAddress'),(1, 'byteCount'),(1, 'buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvCreateGuestMemoryAperture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,UInt32,win32more.Foundation.BOOL,POINTER(c_void_p), use_last_error=False)(("HdvCreateGuestMemoryAperture", windll["vmdevicehost"]), ((1, 'requestor'),(1, 'guestPhysicalAddress'),(1, 'byteCount'),(1, 'writeProtected'),(1, 'mappedAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvDestroyGuestMemoryAperture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p, use_last_error=False)(("HdvDestroyGuestMemoryAperture", windll["vmdevicehost"]), ((1, 'requestor'),(1, 'mappedAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvDeliverGuestInterrupt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,UInt32, use_last_error=False)(("HdvDeliverGuestInterrupt", windll["vmdevicehost"]), ((1, 'requestor'),(1, 'msiAddress'),(1, 'msiData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvRegisterDoorbell():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR,UInt64,UInt64,UInt64,win32more.Foundation.HANDLE, use_last_error=False)(("HdvRegisterDoorbell", windll["vmdevicehost"]), ((1, 'requestor'),(1, 'BarIndex'),(1, 'BarOffset'),(1, 'TriggerValue'),(1, 'Flags'),(1, 'DoorbellEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvUnregisterDoorbell():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR,UInt64,UInt64,UInt64, use_last_error=False)(("HdvUnregisterDoorbell", windll["vmdevicehost"]), ((1, 'requestor'),(1, 'BarIndex'),(1, 'BarOffset'),(1, 'TriggerValue'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvCreateSectionBackedMmioRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR,UInt64,UInt64,win32more.System.Hypervisor.HDV_MMIO_MAPPING_FLAGS,win32more.Foundation.HANDLE,UInt64, use_last_error=False)(("HdvCreateSectionBackedMmioRange", windll["vmdevicehost"]), ((1, 'requestor'),(1, 'barIndex'),(1, 'offsetInPages'),(1, 'lengthInPages'),(1, 'MappingFlags'),(1, 'sectionHandle'),(1, 'sectionOffsetInPages'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HdvDestroySectionBackedMmioRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR,UInt64, use_last_error=False)(("HdvDestroySectionBackedMmioRange", windll["vmdevicehost"]), ((1, 'requestor'),(1, 'barIndex'),(1, 'offsetInPages'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocateSavedStateFiles():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("LocateSavedStateFiles", windll["VmSavedStateDumpProvider"]), ((1, 'vmName'),(1, 'snapshotName'),(1, 'binPath'),(1, 'vsvPath'),(1, 'vmrsPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadSavedStateFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("LoadSavedStateFile", windll["VmSavedStateDumpProvider"]), ((1, 'vmrsFile'),(1, 'vmSavedStateDumpHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ApplyPendingSavedStateFileReplayLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("ApplyPendingSavedStateFileReplayLog", windll["VmSavedStateDumpProvider"]), ((1, 'vmrsFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadSavedStateFiles():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("LoadSavedStateFiles", windll["VmSavedStateDumpProvider"]), ((1, 'binFile'),(1, 'vsvFile'),(1, 'vmSavedStateDumpHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseSavedStateFiles():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("ReleaseSavedStateFiles", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGuestEnabledVirtualTrustLevels():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32), use_last_error=False)(("GetGuestEnabledVirtualTrustLevels", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'virtualTrustLevels'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGuestOsInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,Byte,POINTER(win32more.System.Hypervisor.GUEST_OS_INFO_head), use_last_error=False)(("GetGuestOsInfo", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'virtualTrustLevel'),(1, 'guestOsInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVpCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32), use_last_error=False)(("GetVpCount", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetArchitecture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH), use_last_error=False)(("GetArchitecture", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'architecture'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ForceArchitecture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH, use_last_error=False)(("ForceArchitecture", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'architecture'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetActiveVirtualTrustLevel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,c_char_p_no, use_last_error=False)(("GetActiveVirtualTrustLevel", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'virtualTrustLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnabledVirtualTrustLevels():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("GetEnabledVirtualTrustLevels", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'virtualTrustLevels'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ForceActiveVirtualTrustLevel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,Byte, use_last_error=False)(("ForceActiveVirtualTrustLevel", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'virtualTrustLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsActiveVirtualTrustLevelEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("IsActiveVirtualTrustLevelEnabled", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'activeVirtualTrustLevelEnabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsNestedVirtualizationEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("IsNestedVirtualizationEnabled", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'enabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNestedVirtualizationMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("GetNestedVirtualizationMode", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'enabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ForceNestedHostMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("ForceNestedHostMode", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'hostMode'),(1, 'oldMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InKernelSpace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("InKernelSpace", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'inKernelSpace'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRegisterValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt32,POINTER(win32more.System.Hypervisor.VIRTUAL_PROCESSOR_REGISTER_head), use_last_error=False)(("GetRegisterValue", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'registerId'),(1, 'registerValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPagingMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.Hypervisor.PAGING_MODE), use_last_error=False)(("GetPagingMode", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'pagingMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ForcePagingMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.System.Hypervisor.PAGING_MODE, use_last_error=False)(("ForcePagingMode", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'pagingMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadGuestPhysicalAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("ReadGuestPhysicalAddress", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'physicalAddress'),(1, 'buffer'),(1, 'bufferSize'),(1, 'bytesRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GuestVirtualAddressToPhysicalAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt64,POINTER(UInt64),POINTER(UInt64), use_last_error=False)(("GuestVirtualAddressToPhysicalAddress", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'virtualAddress'),(1, 'physicalAddress'),(1, 'unmappedRegionSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGuestPhysicalMemoryChunks():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt64),POINTER(win32more.System.Hypervisor.GPA_MEMORY_CHUNK_head),POINTER(UInt64), use_last_error=False)(("GetGuestPhysicalMemoryChunks", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'memoryChunkPageSize'),(1, 'memoryChunks'),(1, 'memoryChunkCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GuestPhysicalAddressToRawSavedMemoryOffset():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,POINTER(UInt64), use_last_error=False)(("GuestPhysicalAddressToRawSavedMemoryOffset", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'physicalAddress'),(1, 'rawSavedMemoryOffset'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadGuestRawSavedMemory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("ReadGuestRawSavedMemory", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'rawSavedMemoryOffset'),(1, 'buffer'),(1, 'bufferSize'),(1, 'bytesRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGuestRawSavedMemorySize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt64), use_last_error=False)(("GetGuestRawSavedMemorySize", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'guestRawSavedMemorySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMemoryBlockCacheLimit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64, use_last_error=False)(("SetMemoryBlockCacheLimit", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'memoryBlockCacheLimit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMemoryBlockCacheLimit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt64), use_last_error=False)(("GetMemoryBlockCacheLimit", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'memoryBlockCacheLimit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ApplyGuestMemoryFix():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt64,c_void_p,UInt32, use_last_error=False)(("ApplyGuestMemoryFix", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'virtualAddress'),(1, 'fixBuffer'),(1, 'fixBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadSavedStateSymbolProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("LoadSavedStateSymbolProvider", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'userSymbols'),(1, 'force'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseSavedStateSymbolProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("ReleaseSavedStateSymbolProvider", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSavedStateSymbolProviderHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,c_void_p, use_last_error=False)(("GetSavedStateSymbolProviderHandle", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSavedStateSymbolProviderDebugInfoCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Hypervisor.GUEST_SYMBOLS_PROVIDER_DEBUG_INFO_CALLBACK, use_last_error=False)(("SetSavedStateSymbolProviderDebugInfoCallback", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'Callback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadSavedStateModuleSymbols():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt64,UInt32, use_last_error=False)(("LoadSavedStateModuleSymbols", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'imageName'),(1, 'moduleName'),(1, 'baseAddress'),(1, 'sizeOfBase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadSavedStateModuleSymbolsEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,UInt64,UInt32, use_last_error=False)(("LoadSavedStateModuleSymbolsEx", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'imageName'),(1, 'imageTimestamp'),(1, 'moduleName'),(1, 'baseAddress'),(1, 'sizeOfBase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResolveSavedStateGlobalVariableAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Foundation.PSTR,POINTER(UInt64),POINTER(UInt32), use_last_error=False)(("ResolveSavedStateGlobalVariableAddress", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'globalName'),(1, 'virtualAddress'),(1, 'size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadSavedStateGlobalVariable():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Foundation.PSTR,c_void_p,UInt32, use_last_error=False)(("ReadSavedStateGlobalVariable", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'globalName'),(1, 'buffer'),(1, 'bufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSavedStateSymbolTypeSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("GetSavedStateSymbolTypeSize", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'typeName'),(1, 'size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindSavedStateSymbolFieldInType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Foundation.PSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(("FindSavedStateSymbolFieldInType", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'typeName'),(1, 'fieldName'),(1, 'offset'),(1, 'found'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSavedStateSymbolFieldInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("GetSavedStateSymbolFieldInfo", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'typeName'),(1, 'typeFieldInfoMap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScanMemoryForDosImages():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt64,UInt64,c_void_p,win32more.System.Hypervisor.FOUND_IMAGE_CALLBACK,POINTER(UInt64),UInt32, use_last_error=False)(("ScanMemoryForDosImages", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'startAddress'),(1, 'endAddress'),(1, 'callbackContext'),(1, 'foundImageCallback'),(1, 'standaloneAddress'),(1, 'standaloneAddressCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CallStackUnwind():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.Hypervisor.MODULE_INFO_head),UInt32,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("CallStackUnwind", windll["VmSavedStateDumpProvider"]), ((1, 'vmSavedStateDumpHandle'),(1, 'vpId'),(1, 'imageInfo'),(1, 'imageInfoCount'),(1, 'frameCount'),(1, 'callStack'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "HVSOCKET_CONNECT_TIMEOUT",
    "HVSOCKET_CONNECT_TIMEOUT_MAX",
    "HVSOCKET_CONTAINER_PASSTHRU",
    "HVSOCKET_CONNECTED_SUSPEND",
    "HV_PROTOCOL_RAW",
    "HVSOCKET_ADDRESS_FLAG_PASSTHRU",
    "WHV_PROCESSOR_FEATURES_BANKS_COUNT",
    "WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS_COUNT",
    "WHV_READ_WRITE_GPA_RANGE_MAX_SIZE",
    "WHV_HYPERCALL_CONTEXT_MAX_XMM_REGISTERS",
    "WHV_MAX_DEVICE_ID_SIZE_IN_CHARS",
    "WHV_VPCI_TYPE0_BAR_COUNT",
    "WHV_ANY_VP",
    "WHV_SYNIC_MESSAGE_SIZE",
    "IOCTL_VMGENCOUNTER_READ",
    "HDV_PCI_BAR_COUNT",
    "HV_GUID_ZERO",
    "HV_GUID_BROADCAST",
    "HV_GUID_CHILDREN",
    "HV_GUID_LOOPBACK",
    "HV_GUID_PARENT",
    "HV_GUID_SILOHOST",
    "HV_GUID_VSOCK_TEMPLATE",
    "GUID_DEVINTERFACE_VM_GENCOUNTER",
    "WHV_PARTITION_HANDLE",
    "WHV_CAPABILITY_CODE",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeHypervisorPresent",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeFeatures",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeExtendedVmExits",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeExceptionExitBitmap",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeX64MsrExitBitmap",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeGpaRangePopulateFlags",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeSchedulerFeatures",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorVendor",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFeatures",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorClFlushSize",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorXsaveFeatures",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorClockFrequency",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeInterruptClockFrequency",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFeaturesBanks",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFrequencyCap",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeSyntheticProcessorFeaturesBanks",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorPerfmonFeatures",
    "WHV_CAPABILITY_FEATURES",
    "WHV_EXTENDED_VM_EXITS",
    "WHV_PROCESSOR_VENDOR",
    "WHV_PROCESSOR_VENDOR_WHvProcessorVendorAmd",
    "WHV_PROCESSOR_VENDOR_WHvProcessorVendorIntel",
    "WHV_PROCESSOR_VENDOR_WHvProcessorVendorHygon",
    "WHV_PROCESSOR_FEATURES",
    "WHV_PROCESSOR_FEATURES1",
    "WHV_PROCESSOR_FEATURES_BANKS",
    "WHV_SYNTHETIC_PROCESSOR_FEATURES",
    "WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS",
    "WHV_PARTITION_PROPERTY_CODE",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeExtendedVmExits",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeExceptionExitBitmap",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeSeparateSecurityDomain",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeNestedVirtualization",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeX64MsrExitBitmap",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodePrimaryNumaNode",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuReserve",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuCap",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuWeight",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuGroupId",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFrequencyCap",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeAllowDeviceAssignment",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeDisableSmt",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFeatures",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorClFlushSize",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidExitList",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidResultList",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeLocalApicEmulationMode",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorXsaveFeatures",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorClockFrequency",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeInterruptClockFrequency",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeApicRemoteReadSupport",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFeaturesBanks",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeReferenceTime",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeSyntheticProcessorFeaturesBanks",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidResultList2",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorPerfmonFeatures",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeMsrActionList",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeUnimplementedMsrAction",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorCount",
    "WHV_PROCESSOR_XSAVE_FEATURES",
    "WHV_PROCESSOR_PERFMON_FEATURES",
    "WHV_X64_MSR_EXIT_BITMAP",
    "WHV_MEMORY_RANGE_ENTRY",
    "WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS",
    "WHV_MEMORY_ACCESS_TYPE",
    "WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessRead",
    "WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessWrite",
    "WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessExecute",
    "WHV_ADVISE_GPA_RANGE_POPULATE",
    "WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP",
    "WHV_SCHEDULER_FEATURES",
    "WHV_CAPABILITY",
    "WHV_X64_CPUID_RESULT",
    "WHV_X64_CPUID_RESULT2_FLAGS",
    "WHV_X64_CPUID_RESULT2_FLAGS_WHvX64CpuidResult2FlagSubleafSpecific",
    "WHV_X64_CPUID_RESULT2_FLAGS_WHvX64CpuidResult2FlagVpSpecific",
    "WHV_CPUID_OUTPUT",
    "WHV_X64_CPUID_RESULT2",
    "WHV_MSR_ACTION_ENTRY",
    "WHV_MSR_ACTION",
    "WHV_MSR_ACTION_WHvMsrActionArchitectureDefault",
    "WHV_MSR_ACTION_WHvMsrActionIgnoreWriteReadZero",
    "WHV_MSR_ACTION_WHvMsrActionExit",
    "WHV_EXCEPTION_TYPE",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDivideErrorFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDebugTrapOrFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeBreakpointTrap",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeOverflowTrap",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeBoundRangeFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeInvalidOpcodeFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDeviceNotAvailableFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDoubleFaultAbort",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeInvalidTaskStateSegmentFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeSegmentNotPresentFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeStackFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeGeneralProtectionFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypePageFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeFloatingPointErrorFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeAlignmentCheckFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeMachineCheckAbort",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeSimdFloatingPointFault",
    "WHV_X64_LOCAL_APIC_EMULATION_MODE",
    "WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeNone",
    "WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeXApic",
    "WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeX2Apic",
    "WHV_PARTITION_PROPERTY",
    "WHV_MAP_GPA_RANGE_FLAGS",
    "WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagNone",
    "WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagRead",
    "WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagWrite",
    "WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagExecute",
    "WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagTrackDirtyPages",
    "WHV_TRANSLATE_GVA_FLAGS",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagNone",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateRead",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateWrite",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateExecute",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagPrivilegeExempt",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagSetPageTableBits",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagEnforceSmap",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagOverrideSmap",
    "WHV_TRANSLATE_GVA_RESULT_CODE",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultSuccess",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultPageNotPresent",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultPrivilegeViolation",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultInvalidPageTableFlags",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaUnmapped",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaNoReadAccess",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaNoWriteAccess",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaIllegalOverlayAccess",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultIntercept",
    "WHV_TRANSLATE_GVA_RESULT",
    "WHV_ADVISE_GPA_RANGE",
    "WHV_CACHE_TYPE",
    "WHV_CACHE_TYPE_WHvCacheTypeUncached",
    "WHV_CACHE_TYPE_WHvCacheTypeWriteCombining",
    "WHV_CACHE_TYPE_WHvCacheTypeWriteThrough",
    "WHV_CACHE_TYPE_WHvCacheTypeWriteProtected",
    "WHV_CACHE_TYPE_WHvCacheTypeWriteBack",
    "WHV_ACCESS_GPA_CONTROLS",
    "WHV_REGISTER_NAME",
    "WHV_REGISTER_NAME_WHvX64RegisterRax",
    "WHV_REGISTER_NAME_WHvX64RegisterRcx",
    "WHV_REGISTER_NAME_WHvX64RegisterRdx",
    "WHV_REGISTER_NAME_WHvX64RegisterRbx",
    "WHV_REGISTER_NAME_WHvX64RegisterRsp",
    "WHV_REGISTER_NAME_WHvX64RegisterRbp",
    "WHV_REGISTER_NAME_WHvX64RegisterRsi",
    "WHV_REGISTER_NAME_WHvX64RegisterRdi",
    "WHV_REGISTER_NAME_WHvX64RegisterR8",
    "WHV_REGISTER_NAME_WHvX64RegisterR9",
    "WHV_REGISTER_NAME_WHvX64RegisterR10",
    "WHV_REGISTER_NAME_WHvX64RegisterR11",
    "WHV_REGISTER_NAME_WHvX64RegisterR12",
    "WHV_REGISTER_NAME_WHvX64RegisterR13",
    "WHV_REGISTER_NAME_WHvX64RegisterR14",
    "WHV_REGISTER_NAME_WHvX64RegisterR15",
    "WHV_REGISTER_NAME_WHvX64RegisterRip",
    "WHV_REGISTER_NAME_WHvX64RegisterRflags",
    "WHV_REGISTER_NAME_WHvX64RegisterEs",
    "WHV_REGISTER_NAME_WHvX64RegisterCs",
    "WHV_REGISTER_NAME_WHvX64RegisterSs",
    "WHV_REGISTER_NAME_WHvX64RegisterDs",
    "WHV_REGISTER_NAME_WHvX64RegisterFs",
    "WHV_REGISTER_NAME_WHvX64RegisterGs",
    "WHV_REGISTER_NAME_WHvX64RegisterLdtr",
    "WHV_REGISTER_NAME_WHvX64RegisterTr",
    "WHV_REGISTER_NAME_WHvX64RegisterIdtr",
    "WHV_REGISTER_NAME_WHvX64RegisterGdtr",
    "WHV_REGISTER_NAME_WHvX64RegisterCr0",
    "WHV_REGISTER_NAME_WHvX64RegisterCr2",
    "WHV_REGISTER_NAME_WHvX64RegisterCr3",
    "WHV_REGISTER_NAME_WHvX64RegisterCr4",
    "WHV_REGISTER_NAME_WHvX64RegisterCr8",
    "WHV_REGISTER_NAME_WHvX64RegisterDr0",
    "WHV_REGISTER_NAME_WHvX64RegisterDr1",
    "WHV_REGISTER_NAME_WHvX64RegisterDr2",
    "WHV_REGISTER_NAME_WHvX64RegisterDr3",
    "WHV_REGISTER_NAME_WHvX64RegisterDr6",
    "WHV_REGISTER_NAME_WHvX64RegisterDr7",
    "WHV_REGISTER_NAME_WHvX64RegisterXCr0",
    "WHV_REGISTER_NAME_WHvX64RegisterVirtualCr0",
    "WHV_REGISTER_NAME_WHvX64RegisterVirtualCr3",
    "WHV_REGISTER_NAME_WHvX64RegisterVirtualCr4",
    "WHV_REGISTER_NAME_WHvX64RegisterVirtualCr8",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm0",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm1",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm2",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm3",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm4",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm5",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm6",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm7",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm8",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm9",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm10",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm11",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm12",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm13",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm14",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm15",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx0",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx1",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx2",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx3",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx4",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx5",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx6",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx7",
    "WHV_REGISTER_NAME_WHvX64RegisterFpControlStatus",
    "WHV_REGISTER_NAME_WHvX64RegisterXmmControlStatus",
    "WHV_REGISTER_NAME_WHvX64RegisterTsc",
    "WHV_REGISTER_NAME_WHvX64RegisterEfer",
    "WHV_REGISTER_NAME_WHvX64RegisterKernelGsBase",
    "WHV_REGISTER_NAME_WHvX64RegisterApicBase",
    "WHV_REGISTER_NAME_WHvX64RegisterPat",
    "WHV_REGISTER_NAME_WHvX64RegisterSysenterCs",
    "WHV_REGISTER_NAME_WHvX64RegisterSysenterEip",
    "WHV_REGISTER_NAME_WHvX64RegisterSysenterEsp",
    "WHV_REGISTER_NAME_WHvX64RegisterStar",
    "WHV_REGISTER_NAME_WHvX64RegisterLstar",
    "WHV_REGISTER_NAME_WHvX64RegisterCstar",
    "WHV_REGISTER_NAME_WHvX64RegisterSfmask",
    "WHV_REGISTER_NAME_WHvX64RegisterInitialApicId",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrCap",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrDefType",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase0",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase1",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase2",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase3",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase4",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase5",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase6",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase7",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase8",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase9",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseA",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseB",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseC",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseD",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseE",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseF",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask0",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask1",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask2",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask3",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask4",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask5",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask6",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask7",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask8",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask9",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskA",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskB",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskC",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskD",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskE",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskF",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix64k00000",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix16k80000",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix16kA0000",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kC0000",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kC8000",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kD0000",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kD8000",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kE0000",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kE8000",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kF0000",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kF8000",
    "WHV_REGISTER_NAME_WHvX64RegisterTscAux",
    "WHV_REGISTER_NAME_WHvX64RegisterBndcfgs",
    "WHV_REGISTER_NAME_WHvX64RegisterMCount",
    "WHV_REGISTER_NAME_WHvX64RegisterACount",
    "WHV_REGISTER_NAME_WHvX64RegisterSpecCtrl",
    "WHV_REGISTER_NAME_WHvX64RegisterPredCmd",
    "WHV_REGISTER_NAME_WHvX64RegisterTscVirtualOffset",
    "WHV_REGISTER_NAME_WHvX64RegisterTsxCtrl",
    "WHV_REGISTER_NAME_WHvX64RegisterXss",
    "WHV_REGISTER_NAME_WHvX64RegisterUCet",
    "WHV_REGISTER_NAME_WHvX64RegisterSCet",
    "WHV_REGISTER_NAME_WHvX64RegisterSsp",
    "WHV_REGISTER_NAME_WHvX64RegisterPl0Ssp",
    "WHV_REGISTER_NAME_WHvX64RegisterPl1Ssp",
    "WHV_REGISTER_NAME_WHvX64RegisterPl2Ssp",
    "WHV_REGISTER_NAME_WHvX64RegisterPl3Ssp",
    "WHV_REGISTER_NAME_WHvX64RegisterInterruptSspTableAddr",
    "WHV_REGISTER_NAME_WHvX64RegisterTscDeadline",
    "WHV_REGISTER_NAME_WHvX64RegisterTscAdjust",
    "WHV_REGISTER_NAME_WHvX64RegisterUmwaitControl",
    "WHV_REGISTER_NAME_WHvX64RegisterXfd",
    "WHV_REGISTER_NAME_WHvX64RegisterXfdErr",
    "WHV_REGISTER_NAME_WHvX64RegisterApicId",
    "WHV_REGISTER_NAME_WHvX64RegisterApicVersion",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTpr",
    "WHV_REGISTER_NAME_WHvX64RegisterApicPpr",
    "WHV_REGISTER_NAME_WHvX64RegisterApicEoi",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLdr",
    "WHV_REGISTER_NAME_WHvX64RegisterApicSpurious",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr0",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr1",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr2",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr3",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr4",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr5",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr6",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr7",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr0",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr1",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr2",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr3",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr4",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr5",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr6",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr7",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr0",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr1",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr2",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr3",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr4",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr5",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr6",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr7",
    "WHV_REGISTER_NAME_WHvX64RegisterApicEse",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIcr",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtTimer",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtThermal",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtPerfmon",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtLint0",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtLint1",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtError",
    "WHV_REGISTER_NAME_WHvX64RegisterApicInitCount",
    "WHV_REGISTER_NAME_WHvX64RegisterApicCurrentCount",
    "WHV_REGISTER_NAME_WHvX64RegisterApicDivide",
    "WHV_REGISTER_NAME_WHvX64RegisterApicSelfIpi",
    "WHV_REGISTER_NAME_WHvRegisterSint0",
    "WHV_REGISTER_NAME_WHvRegisterSint1",
    "WHV_REGISTER_NAME_WHvRegisterSint2",
    "WHV_REGISTER_NAME_WHvRegisterSint3",
    "WHV_REGISTER_NAME_WHvRegisterSint4",
    "WHV_REGISTER_NAME_WHvRegisterSint5",
    "WHV_REGISTER_NAME_WHvRegisterSint6",
    "WHV_REGISTER_NAME_WHvRegisterSint7",
    "WHV_REGISTER_NAME_WHvRegisterSint8",
    "WHV_REGISTER_NAME_WHvRegisterSint9",
    "WHV_REGISTER_NAME_WHvRegisterSint10",
    "WHV_REGISTER_NAME_WHvRegisterSint11",
    "WHV_REGISTER_NAME_WHvRegisterSint12",
    "WHV_REGISTER_NAME_WHvRegisterSint13",
    "WHV_REGISTER_NAME_WHvRegisterSint14",
    "WHV_REGISTER_NAME_WHvRegisterSint15",
    "WHV_REGISTER_NAME_WHvRegisterScontrol",
    "WHV_REGISTER_NAME_WHvRegisterSversion",
    "WHV_REGISTER_NAME_WHvRegisterSiefp",
    "WHV_REGISTER_NAME_WHvRegisterSimp",
    "WHV_REGISTER_NAME_WHvRegisterEom",
    "WHV_REGISTER_NAME_WHvRegisterVpRuntime",
    "WHV_REGISTER_NAME_WHvX64RegisterHypercall",
    "WHV_REGISTER_NAME_WHvRegisterGuestOsId",
    "WHV_REGISTER_NAME_WHvRegisterVpAssistPage",
    "WHV_REGISTER_NAME_WHvRegisterReferenceTsc",
    "WHV_REGISTER_NAME_WHvRegisterReferenceTscSequence",
    "WHV_REGISTER_NAME_WHvRegisterPendingInterruption",
    "WHV_REGISTER_NAME_WHvRegisterInterruptState",
    "WHV_REGISTER_NAME_WHvRegisterPendingEvent",
    "WHV_REGISTER_NAME_WHvX64RegisterDeliverabilityNotifications",
    "WHV_REGISTER_NAME_WHvRegisterInternalActivityState",
    "WHV_REGISTER_NAME_WHvX64RegisterPendingDebugException",
    "WHV_UINT128",
    "WHV_X64_FP_REGISTER",
    "WHV_X64_FP_CONTROL_STATUS_REGISTER",
    "WHV_X64_XMM_CONTROL_STATUS_REGISTER",
    "WHV_X64_SEGMENT_REGISTER",
    "WHV_X64_TABLE_REGISTER",
    "WHV_X64_INTERRUPT_STATE_REGISTER",
    "WHV_X64_PENDING_INTERRUPTION_REGISTER",
    "WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER",
    "WHV_X64_PENDING_EVENT_TYPE",
    "WHV_X64_PENDING_EVENT_TYPE_WHvX64PendingEventException",
    "WHV_X64_PENDING_EVENT_TYPE_WHvX64PendingEventExtInt",
    "WHV_X64_PENDING_EXCEPTION_EVENT",
    "WHV_X64_PENDING_EXT_INT_EVENT",
    "WHV_INTERNAL_ACTIVITY_REGISTER",
    "WHV_X64_PENDING_DEBUG_EXCEPTION",
    "WHV_SYNIC_SINT_DELIVERABLE_CONTEXT",
    "WHV_REGISTER_VALUE",
    "WHV_RUN_VP_EXIT_REASON",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonNone",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonMemoryAccess",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64IoPortAccess",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonUnrecoverableException",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonInvalidVpRegisterValue",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonUnsupportedFeature",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64InterruptWindow",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Halt",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicEoi",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonSynicSintDeliverable",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64MsrAccess",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Cpuid",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonException",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Rdtsc",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicSmiTrap",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonHypercall",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicInitSipiTrap",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicWriteTrap",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonCanceled",
    "WHV_X64_VP_EXECUTION_STATE",
    "WHV_VP_EXIT_CONTEXT",
    "WHV_MEMORY_ACCESS_INFO",
    "WHV_MEMORY_ACCESS_CONTEXT",
    "WHV_X64_IO_PORT_ACCESS_INFO",
    "WHV_X64_IO_PORT_ACCESS_CONTEXT",
    "WHV_X64_MSR_ACCESS_INFO",
    "WHV_X64_MSR_ACCESS_CONTEXT",
    "WHV_X64_CPUID_ACCESS_CONTEXT",
    "WHV_VP_EXCEPTION_INFO",
    "WHV_VP_EXCEPTION_CONTEXT",
    "WHV_X64_UNSUPPORTED_FEATURE_CODE",
    "WHV_X64_UNSUPPORTED_FEATURE_CODE_WHvUnsupportedFeatureIntercept",
    "WHV_X64_UNSUPPORTED_FEATURE_CODE_WHvUnsupportedFeatureTaskSwitchTss",
    "WHV_X64_UNSUPPORTED_FEATURE_CONTEXT",
    "WHV_RUN_VP_CANCEL_REASON",
    "WHV_RUN_VP_CANCEL_REASON_WHvRunVpCancelReasonUser",
    "WHV_RUN_VP_CANCELED_CONTEXT",
    "WHV_X64_PENDING_INTERRUPTION_TYPE",
    "WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingInterrupt",
    "WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingNmi",
    "WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingException",
    "WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT",
    "WHV_X64_APIC_EOI_CONTEXT",
    "WHV_X64_RDTSC_INFO",
    "WHV_X64_RDTSC_CONTEXT",
    "WHV_X64_APIC_SMI_CONTEXT",
    "WHV_HYPERCALL_CONTEXT",
    "WHV_X64_APIC_INIT_SIPI_CONTEXT",
    "WHV_X64_APIC_WRITE_TYPE",
    "WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLdr",
    "WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeDfr",
    "WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeSvr",
    "WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLint0",
    "WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLint1",
    "WHV_X64_APIC_WRITE_CONTEXT",
    "WHV_RUN_VP_EXIT_CONTEXT",
    "WHV_INTERRUPT_TYPE",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeFixed",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeLowestPriority",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeNmi",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeInit",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeSipi",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeLocalInt1",
    "WHV_INTERRUPT_DESTINATION_MODE",
    "WHV_INTERRUPT_DESTINATION_MODE_WHvX64InterruptDestinationModePhysical",
    "WHV_INTERRUPT_DESTINATION_MODE_WHvX64InterruptDestinationModeLogical",
    "WHV_INTERRUPT_TRIGGER_MODE",
    "WHV_INTERRUPT_TRIGGER_MODE_WHvX64InterruptTriggerModeEdge",
    "WHV_INTERRUPT_TRIGGER_MODE_WHvX64InterruptTriggerModeLevel",
    "WHV_INTERRUPT_CONTROL",
    "WHV_DOORBELL_MATCH_DATA",
    "WHV_PARTITION_COUNTER_SET",
    "WHV_PARTITION_COUNTER_SET_WHvPartitionCounterSetMemory",
    "WHV_PARTITION_MEMORY_COUNTERS",
    "WHV_PROCESSOR_COUNTER_SET",
    "WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetRuntime",
    "WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetIntercepts",
    "WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetEvents",
    "WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetApic",
    "WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetSyntheticFeatures",
    "WHV_PROCESSOR_RUNTIME_COUNTERS",
    "WHV_PROCESSOR_INTERCEPT_COUNTER",
    "WHV_PROCESSOR_INTERCEPT_COUNTERS",
    "WHV_PROCESSOR_EVENT_COUNTERS",
    "WHV_PROCESSOR_APIC_COUNTERS",
    "WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS",
    "WHV_ADVISE_GPA_RANGE_CODE",
    "WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodePopulate",
    "WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodePin",
    "WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodeUnpin",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicMessagePage",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicEventFlagPage",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicTimerState",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeInterruptControllerState2",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeXsaveState",
    "WHV_SYNIC_EVENT_PARAMETERS",
    "WHV_ALLOCATE_VPCI_RESOURCE_FLAGS",
    "WHV_ALLOCATE_VPCI_RESOURCE_FLAGS_WHvAllocateVpciResourceFlagNone",
    "WHV_ALLOCATE_VPCI_RESOURCE_FLAGS_WHvAllocateVpciResourceFlagAllowDirectP2P",
    "WHV_SRIOV_RESOURCE_DESCRIPTOR",
    "WHV_VPCI_DEVICE_NOTIFICATION_TYPE",
    "WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationUndefined",
    "WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationMmioRemapping",
    "WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationSurpriseRemoval",
    "WHV_VPCI_DEVICE_NOTIFICATION",
    "WHV_CREATE_VPCI_DEVICE_FLAGS",
    "WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagNone",
    "WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagPhysicallyBacked",
    "WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagUseLogicalInterrupts",
    "WHV_VPCI_DEVICE_PROPERTY_CODE",
    "WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeUndefined",
    "WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeHardwareIDs",
    "WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeProbedBARs",
    "WHV_VPCI_HARDWARE_IDS",
    "WHV_VPCI_PROBED_BARS",
    "WHV_VPCI_MMIO_RANGE_FLAGS",
    "WHV_VPCI_MMIO_RANGE_FLAGS_WHvVpciMmioRangeFlagReadAccess",
    "WHV_VPCI_MMIO_RANGE_FLAGS_WHvVpciMmioRangeFlagWriteAccess",
    "WHV_VPCI_DEVICE_REGISTER_SPACE",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciConfigSpace",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar0",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar1",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar2",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar3",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar4",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar5",
    "WHV_VPCI_MMIO_MAPPING",
    "WHV_VPCI_DEVICE_REGISTER",
    "WHV_VPCI_INTERRUPT_TARGET_FLAGS",
    "WHV_VPCI_INTERRUPT_TARGET_FLAGS_WHvVpciInterruptTargetFlagNone",
    "WHV_VPCI_INTERRUPT_TARGET_FLAGS_WHvVpciInterruptTargetFlagMulticast",
    "WHV_VPCI_INTERRUPT_TARGET",
    "WHV_TRIGGER_TYPE",
    "WHV_TRIGGER_TYPE_WHvTriggerTypeInterrupt",
    "WHV_TRIGGER_TYPE_WHvTriggerTypeSynicEvent",
    "WHV_TRIGGER_TYPE_WHvTriggerTypeDeviceInterrupt",
    "WHV_TRIGGER_PARAMETERS",
    "WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE",
    "WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE_WHvVirtualProcessorPropertyCodeNumaNode",
    "WHV_VIRTUAL_PROCESSOR_PROPERTY",
    "WHV_NOTIFICATION_PORT_TYPE",
    "WHV_NOTIFICATION_PORT_TYPE_WHvNotificationPortTypeEvent",
    "WHV_NOTIFICATION_PORT_TYPE_WHvNotificationPortTypeDoorbell",
    "WHV_NOTIFICATION_PORT_PARAMETERS",
    "WHV_NOTIFICATION_PORT_PROPERTY_CODE",
    "WHV_NOTIFICATION_PORT_PROPERTY_CODE_WHvNotificationPortPropertyPreferredTargetVp",
    "WHV_NOTIFICATION_PORT_PROPERTY_CODE_WHvNotificationPortPropertyPreferredTargetDuration",
    "WHV_EMULATOR_STATUS",
    "WHV_EMULATOR_MEMORY_ACCESS_INFO",
    "WHV_EMULATOR_IO_ACCESS_INFO",
    "WHV_EMULATOR_IO_PORT_CALLBACK",
    "WHV_EMULATOR_MEMORY_CALLBACK",
    "WHV_EMULATOR_GET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK",
    "WHV_EMULATOR_SET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK",
    "WHV_EMULATOR_TRANSLATE_GVA_PAGE_CALLBACK",
    "WHV_EMULATOR_CALLBACKS",
    "SOCKADDR_HV",
    "HVSOCKET_ADDRESS_INFO",
    "VM_GENCOUNTER",
    "HDV_DEVICE_TYPE",
    "HDV_DEVICE_TYPE_HdvDeviceTypeUndefined",
    "HDV_DEVICE_TYPE_HdvDeviceTypePCI",
    "HDV_PCI_PNP_ID",
    "HDV_PCI_BAR_SELECTOR",
    "HDV_PCI_BAR0",
    "HDV_PCI_BAR1",
    "HDV_PCI_BAR2",
    "HDV_PCI_BAR3",
    "HDV_PCI_BAR4",
    "HDV_PCI_BAR5",
    "HDV_DOORBELL_FLAGS",
    "HDV_DOORBELL_FLAG_TRIGGER_SIZE_ANY",
    "HDV_DOORBELL_FLAG_TRIGGER_SIZE_BYTE",
    "HDV_DOORBELL_FLAG_TRIGGER_SIZE_WORD",
    "HDV_DOORBELL_FLAG_TRIGGER_SIZE_DWORD",
    "HDV_DOORBELL_FLAG_TRIGGER_SIZE_QWORD",
    "HDV_DOORBELL_FLAG_TRIGGER_ANY_VALUE",
    "HDV_MMIO_MAPPING_FLAGS",
    "HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagNone",
    "HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagWriteable",
    "HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagExecutable",
    "HDV_PCI_DEVICE_INITIALIZE",
    "HDV_PCI_DEVICE_TEARDOWN",
    "HDV_PCI_DEVICE_SET_CONFIGURATION",
    "HDV_PCI_DEVICE_GET_DETAILS",
    "HDV_PCI_DEVICE_START",
    "HDV_PCI_DEVICE_STOP",
    "HDV_PCI_READ_CONFIG_SPACE",
    "HDV_PCI_WRITE_CONFIG_SPACE",
    "HDV_PCI_READ_INTERCEPTED_MEMORY",
    "HDV_PCI_WRITE_INTERCEPTED_MEMORY",
    "HDV_PCI_INTERFACE_VERSION",
    "HDV_PCI_INTERFACE_VERSION_HdvPciDeviceInterfaceVersionInvalid",
    "HDV_PCI_INTERFACE_VERSION_HdvPciDeviceInterfaceVersion1",
    "HDV_PCI_DEVICE_INTERFACE",
    "PAGING_MODE",
    "Paging_Invalid",
    "Paging_NonPaged",
    "Paging_32Bit",
    "Paging_Pae",
    "Paging_Long",
    "Paging_Armv8",
    "GPA_MEMORY_CHUNK",
    "VIRTUAL_PROCESSOR_ARCH",
    "Arch_Unknown",
    "Arch_x86",
    "Arch_x64",
    "Arch_Armv8",
    "VIRTUAL_PROCESSOR_VENDOR",
    "ProcessorVendor_Unknown",
    "ProcessorVendor_Amd",
    "ProcessorVendor_Intel",
    "ProcessorVendor_Hygon",
    "ProcessorVendor_Arm",
    "GUEST_OS_VENDOR",
    "GUEST_OS_VENDOR_GuestOsVendorUndefined",
    "GUEST_OS_VENDOR_GuestOsVendorMicrosoft",
    "GUEST_OS_VENDOR_GuestOsVendorHPE",
    "GUEST_OS_VENDOR_GuestOsVendorLANCOM",
    "GUEST_OS_MICROSOFT_IDS",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftUndefined",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftMSDOS",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindows3x",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindows9x",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindowsNT",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindowsCE",
    "GUEST_OS_OPENSOURCE_IDS",
    "GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceUndefined",
    "GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceLinux",
    "GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceFreeBSD",
    "GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceXen",
    "GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceIllumos",
    "GUEST_OS_INFO",
    "REGISTER_ID",
    "X64_RegisterRax",
    "X64_RegisterRcx",
    "X64_RegisterRdx",
    "X64_RegisterRbx",
    "X64_RegisterRsp",
    "X64_RegisterRbp",
    "X64_RegisterRsi",
    "X64_RegisterRdi",
    "X64_RegisterR8",
    "X64_RegisterR9",
    "X64_RegisterR10",
    "X64_RegisterR11",
    "X64_RegisterR12",
    "X64_RegisterR13",
    "X64_RegisterR14",
    "X64_RegisterR15",
    "X64_RegisterRip",
    "X64_RegisterRFlags",
    "X64_RegisterXmm0",
    "X64_RegisterXmm1",
    "X64_RegisterXmm2",
    "X64_RegisterXmm3",
    "X64_RegisterXmm4",
    "X64_RegisterXmm5",
    "X64_RegisterXmm6",
    "X64_RegisterXmm7",
    "X64_RegisterXmm8",
    "X64_RegisterXmm9",
    "X64_RegisterXmm10",
    "X64_RegisterXmm11",
    "X64_RegisterXmm12",
    "X64_RegisterXmm13",
    "X64_RegisterXmm14",
    "X64_RegisterXmm15",
    "X64_RegisterFpMmx0",
    "X64_RegisterFpMmx1",
    "X64_RegisterFpMmx2",
    "X64_RegisterFpMmx3",
    "X64_RegisterFpMmx4",
    "X64_RegisterFpMmx5",
    "X64_RegisterFpMmx6",
    "X64_RegisterFpMmx7",
    "X64_RegisterFpControlStatus",
    "X64_RegisterXmmControlStatus",
    "X64_RegisterCr0",
    "X64_RegisterCr2",
    "X64_RegisterCr3",
    "X64_RegisterCr4",
    "X64_RegisterCr8",
    "X64_RegisterEfer",
    "X64_RegisterDr0",
    "X64_RegisterDr1",
    "X64_RegisterDr2",
    "X64_RegisterDr3",
    "X64_RegisterDr6",
    "X64_RegisterDr7",
    "X64_RegisterEs",
    "X64_RegisterCs",
    "X64_RegisterSs",
    "X64_RegisterDs",
    "X64_RegisterFs",
    "X64_RegisterGs",
    "X64_RegisterLdtr",
    "X64_RegisterTr",
    "X64_RegisterIdtr",
    "X64_RegisterGdtr",
    "X64_RegisterMax",
    "ARM64_RegisterX0",
    "ARM64_RegisterX1",
    "ARM64_RegisterX2",
    "ARM64_RegisterX3",
    "ARM64_RegisterX4",
    "ARM64_RegisterX5",
    "ARM64_RegisterX6",
    "ARM64_RegisterX7",
    "ARM64_RegisterX8",
    "ARM64_RegisterX9",
    "ARM64_RegisterX10",
    "ARM64_RegisterX11",
    "ARM64_RegisterX12",
    "ARM64_RegisterX13",
    "ARM64_RegisterX14",
    "ARM64_RegisterX15",
    "ARM64_RegisterX16",
    "ARM64_RegisterX17",
    "ARM64_RegisterX18",
    "ARM64_RegisterX19",
    "ARM64_RegisterX20",
    "ARM64_RegisterX21",
    "ARM64_RegisterX22",
    "ARM64_RegisterX23",
    "ARM64_RegisterX24",
    "ARM64_RegisterX25",
    "ARM64_RegisterX26",
    "ARM64_RegisterX27",
    "ARM64_RegisterX28",
    "ARM64_RegisterXFp",
    "ARM64_RegisterXLr",
    "ARM64_RegisterPc",
    "ARM64_RegisterSpEl0",
    "ARM64_RegisterSpEl1",
    "ARM64_RegisterCpsr",
    "ARM64_RegisterQ0",
    "ARM64_RegisterQ1",
    "ARM64_RegisterQ2",
    "ARM64_RegisterQ3",
    "ARM64_RegisterQ4",
    "ARM64_RegisterQ5",
    "ARM64_RegisterQ6",
    "ARM64_RegisterQ7",
    "ARM64_RegisterQ8",
    "ARM64_RegisterQ9",
    "ARM64_RegisterQ10",
    "ARM64_RegisterQ11",
    "ARM64_RegisterQ12",
    "ARM64_RegisterQ13",
    "ARM64_RegisterQ14",
    "ARM64_RegisterQ15",
    "ARM64_RegisterQ16",
    "ARM64_RegisterQ17",
    "ARM64_RegisterQ18",
    "ARM64_RegisterQ19",
    "ARM64_RegisterQ20",
    "ARM64_RegisterQ21",
    "ARM64_RegisterQ22",
    "ARM64_RegisterQ23",
    "ARM64_RegisterQ24",
    "ARM64_RegisterQ25",
    "ARM64_RegisterQ26",
    "ARM64_RegisterQ27",
    "ARM64_RegisterQ28",
    "ARM64_RegisterQ29",
    "ARM64_RegisterQ30",
    "ARM64_RegisterQ31",
    "ARM64_RegisterFpStatus",
    "ARM64_RegisterFpControl",
    "ARM64_RegisterEsrEl1",
    "ARM64_RegisterSpsrEl1",
    "ARM64_RegisterFarEl1",
    "ARM64_RegisterParEl1",
    "ARM64_RegisterElrEl1",
    "ARM64_RegisterTtbr0El1",
    "ARM64_RegisterTtbr1El1",
    "ARM64_RegisterVbarEl1",
    "ARM64_RegisterSctlrEl1",
    "ARM64_RegisterActlrEl1",
    "ARM64_RegisterTcrEl1",
    "ARM64_RegisterMairEl1",
    "ARM64_RegisterAmairEl1",
    "ARM64_RegisterTpidrEl0",
    "ARM64_RegisterTpidrroEl0",
    "ARM64_RegisterTpidrEl1",
    "ARM64_RegisterContextIdrEl1",
    "ARM64_RegisterCpacrEl1",
    "ARM64_RegisterCsselrEl1",
    "ARM64_RegisterCntkctlEl1",
    "ARM64_RegisterCntvCvalEl0",
    "ARM64_RegisterCntvCtlEl0",
    "ARM64_RegisterMax",
    "VIRTUAL_PROCESSOR_REGISTER",
    "DOS_IMAGE_INFO",
    "GUEST_SYMBOLS_PROVIDER_DEBUG_INFO_CALLBACK",
    "FOUND_IMAGE_CALLBACK",
    "MODULE_INFO",
    "WHvGetCapability",
    "WHvCreatePartition",
    "WHvSetupPartition",
    "WHvResetPartition",
    "WHvDeletePartition",
    "WHvGetPartitionProperty",
    "WHvSetPartitionProperty",
    "WHvSuspendPartitionTime",
    "WHvResumePartitionTime",
    "WHvMapGpaRange",
    "WHvMapGpaRange2",
    "WHvUnmapGpaRange",
    "WHvTranslateGva",
    "WHvCreateVirtualProcessor",
    "WHvCreateVirtualProcessor2",
    "WHvDeleteVirtualProcessor",
    "WHvRunVirtualProcessor",
    "WHvCancelRunVirtualProcessor",
    "WHvGetVirtualProcessorRegisters",
    "WHvSetVirtualProcessorRegisters",
    "WHvGetVirtualProcessorInterruptControllerState",
    "WHvSetVirtualProcessorInterruptControllerState",
    "WHvRequestInterrupt",
    "WHvGetVirtualProcessorXsaveState",
    "WHvSetVirtualProcessorXsaveState",
    "WHvQueryGpaRangeDirtyBitmap",
    "WHvGetPartitionCounters",
    "WHvGetVirtualProcessorCounters",
    "WHvGetVirtualProcessorInterruptControllerState2",
    "WHvSetVirtualProcessorInterruptControllerState2",
    "WHvRegisterPartitionDoorbellEvent",
    "WHvUnregisterPartitionDoorbellEvent",
    "WHvAdviseGpaRange",
    "WHvReadGpaRange",
    "WHvWriteGpaRange",
    "WHvSignalVirtualProcessorSynicEvent",
    "WHvGetVirtualProcessorState",
    "WHvSetVirtualProcessorState",
    "WHvAllocateVpciResource",
    "WHvCreateVpciDevice",
    "WHvDeleteVpciDevice",
    "WHvGetVpciDeviceProperty",
    "WHvGetVpciDeviceNotification",
    "WHvMapVpciDeviceMmioRanges",
    "WHvUnmapVpciDeviceMmioRanges",
    "WHvSetVpciDevicePowerState",
    "WHvReadVpciDeviceRegister",
    "WHvWriteVpciDeviceRegister",
    "WHvMapVpciDeviceInterrupt",
    "WHvUnmapVpciDeviceInterrupt",
    "WHvRetargetVpciDeviceInterrupt",
    "WHvRequestVpciDeviceInterrupt",
    "WHvGetVpciDeviceInterruptTarget",
    "WHvCreateTrigger",
    "WHvUpdateTriggerParameters",
    "WHvDeleteTrigger",
    "WHvCreateNotificationPort",
    "WHvSetNotificationPortProperty",
    "WHvDeleteNotificationPort",
    "WHvPostVirtualProcessorSynicMessage",
    "WHvGetVirtualProcessorCpuidOutput",
    "WHvGetInterruptTargetVpSet",
    "WHvStartPartitionMigration",
    "WHvCancelPartitionMigration",
    "WHvCompletePartitionMigration",
    "WHvAcceptPartitionMigration",
    "WHvEmulatorCreateEmulator",
    "WHvEmulatorDestroyEmulator",
    "WHvEmulatorTryIoEmulation",
    "WHvEmulatorTryMmioEmulation",
    "HdvInitializeDeviceHost",
    "HdvTeardownDeviceHost",
    "HdvCreateDeviceInstance",
    "HdvReadGuestMemory",
    "HdvWriteGuestMemory",
    "HdvCreateGuestMemoryAperture",
    "HdvDestroyGuestMemoryAperture",
    "HdvDeliverGuestInterrupt",
    "HdvRegisterDoorbell",
    "HdvUnregisterDoorbell",
    "HdvCreateSectionBackedMmioRange",
    "HdvDestroySectionBackedMmioRange",
    "LocateSavedStateFiles",
    "LoadSavedStateFile",
    "ApplyPendingSavedStateFileReplayLog",
    "LoadSavedStateFiles",
    "ReleaseSavedStateFiles",
    "GetGuestEnabledVirtualTrustLevels",
    "GetGuestOsInfo",
    "GetVpCount",
    "GetArchitecture",
    "ForceArchitecture",
    "GetActiveVirtualTrustLevel",
    "GetEnabledVirtualTrustLevels",
    "ForceActiveVirtualTrustLevel",
    "IsActiveVirtualTrustLevelEnabled",
    "IsNestedVirtualizationEnabled",
    "GetNestedVirtualizationMode",
    "ForceNestedHostMode",
    "InKernelSpace",
    "GetRegisterValue",
    "GetPagingMode",
    "ForcePagingMode",
    "ReadGuestPhysicalAddress",
    "GuestVirtualAddressToPhysicalAddress",
    "GetGuestPhysicalMemoryChunks",
    "GuestPhysicalAddressToRawSavedMemoryOffset",
    "ReadGuestRawSavedMemory",
    "GetGuestRawSavedMemorySize",
    "SetMemoryBlockCacheLimit",
    "GetMemoryBlockCacheLimit",
    "ApplyGuestMemoryFix",
    "LoadSavedStateSymbolProvider",
    "ReleaseSavedStateSymbolProvider",
    "GetSavedStateSymbolProviderHandle",
    "SetSavedStateSymbolProviderDebugInfoCallback",
    "LoadSavedStateModuleSymbols",
    "LoadSavedStateModuleSymbolsEx",
    "ResolveSavedStateGlobalVariableAddress",
    "ReadSavedStateGlobalVariable",
    "GetSavedStateSymbolTypeSize",
    "FindSavedStateSymbolFieldInType",
    "GetSavedStateSymbolFieldInfo",
    "ScanMemoryForDosImages",
    "CallStackUnwind",
]
